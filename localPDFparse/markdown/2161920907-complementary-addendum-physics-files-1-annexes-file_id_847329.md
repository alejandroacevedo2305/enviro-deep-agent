---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: manual
pages: 83
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - APÉNDICE 3. MODELO HIDRÁULICO PAS 156 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO EMÚ para TIKUNA
  - APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO EMÚ para TIKUNA
  - Contenidos
  - Figuras
  - Tablas
  - 1. Introducción
  - 2. Descripción del modelo
  - 3. Parámetros de entrada
  - 4. Resultados
  - 5. Referencias
  ... y 9 secciones más
-->

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# APÉNDICE 3. MODELO HIDRÁULICO PAS 156 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO EMÚ para TIKUNA

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO EMÚ para TIKUNA

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
|0|-|06/03/2025|Adenda comp.|DPP|BGP|ABL|
|A|-|27/02/2025|Revisión cliente|DPP/CHR|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comuna de Marchigüe<br>Región de O’Higgins|Col3|
|---|---|---|
||Apéndice 3.01. Modelo Hidráulico PAS 156.<br>OA 01 y OA 03|Rev. 0|

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

# Contenidos

1. Introducción ......................................................................................................................................... 6

2. Descripción del modelo ...................................................................................................................... 6

3. Parámetros de entrada ...................................................................................................................... 7

3.1. Topografía .............................................................................................................................................. 7
3.2. Obras proyectadas............................................................................................................................... 8

3.2.1. Proyección obra de atravieso OA 01 ....................................................................................................... 8

3.2.2. Proyección obra de atravieso OA 03 ...................................................................................................... 9

3.3. Coeficiente de rugosidad .................................................................................................................. 10
3.4. Condiciones de borde e iniciales ...................................................................................................... 12

3.5. Otras consideraciones ........................................................................................................................ 16

4. Resultados .......................................................................................................................................... 17

4.1. Resultados modelo completo .......................................................................................................... 17

4.1.1. Condición sin proyecto .............................................................................................................................. 17

4.1.2. Condición con proyecto .............................................................................................................................22

4.2. Resultados obra de atravieso OA 01 .............................................................................................. 27

4.2.1. Condición sin proyecto .............................................................................................................................. 27

4.2.2. Condición con proyecto ............................................................................................................................ 29

4.3. Resultados obra de atravieso OA 03 .............................................................................................32

4.3.1. Condición sin proyecto ............................................................................................................................. 32

4.3.2. Condición con proyecto ............................................................................................................................ 34

4.4. Resumen de resultados .................................................................................................................... 36

5. Referencias ........................................................................................................................................ 39

# Figuras

Figura 3-1. Representación del modelo digital de terreno (MDT) ............................................................................... 7

Figura 3-2: Topografía de la zona de estudio de la obra OA 01, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Sin Proyecto ...................................................................... 8

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 3-3. Topografía de la zona de estudio de la obra OA 01, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Con Proyecto ..................................................................... 9

Figura 3-4: Topografía de la zona de estudio de la obra OA 03, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Sin Proyecto ...................................................................... 9

Figura 3-5. Topografía de la zona de estudio de la obra OA 03, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Con Proyecto .................................................................... 10

Figura 3-6. Ortofoto de terreno en ubicación de las obras OA 01 y OA 03 .............................................................. 11

Figura 3-7. Registro fotográfico visita a terreno en ubicación de las obras OA 01 (izquierda) y OA 03

(derecha). Cauce C_01 ............................................................................................................................................................ 11

Figura 3-8. Ubicación condiciones de borde y layout (negro) .................................................................................... 13

Figura 3-9. Esquema general para la obtención de condiciones de borde .............................................................. 14

Figura 3-10. Hidrogramas de entrada. Crecida de diseño (50 años) ......................................................................... 15

Figura 3-11. Hidrogramas de entrada. Crecida de verificación (100 años) ............................................................... 16

Figura 4-1. Profundidad máxima [m] con layout proyecto (color negro). Crecida de diseño (50 años).

Condición Sin Proyecto ......................................................................................................................................................... 17

Figura 4-2. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de diseño (50 años).

Condición Sin Proyecto ......................................................................................................................................................... 18

Figura 4-3. Profundidad máxima [m] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Sin Proyecto ......................................................................................................................................................... 19

Figura 4-4. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Sin Proyecto ........................................................................................................................................................ 20

Figura 4-5. Hidrograma a la salida del modelo. Condición Sin Proyecto ................................................................. 21

Figura 4-6. Profundidad máxima [m] con layout proyecto (color negro). Crecida de diseño (50 años).

Condición Con Proyecto .......................................................................................................................................................22

Figura 4-7. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de diseño (50 años). Condición

Con Proyecto.......................................................................................................................................................................... 23

Figura 4-8. Profundidad máxima [m] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Con Proyecto ...................................................................................................................................................... 24

Figura 4-9. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Con Proyecto ...................................................................................................................................................... 25

Figura 4-10. Hidrograma a la salida del modelo. Condición Con Proyecto ............................................................ 26

Figura 4-11. Profundidad máxima [m] en la ubicación de la obra OA 01. Crecida de diseño (50 años). Condición

Sin Proyecto ............................................................................................................................................................................ 27

Figura 4-12. Velocidad máxima [m/s] en la ubicación de la obra OA 01. Crecida de diseño (50 años). Condición

Sin Proyecto ........................................................................................................................................................................... 28

Figura 4-13. Profundidad máxima [m] en la ubicación de la obra OA 01. Crecida de verificación (100 años).

Condición Sin Proyecto ........................................................................................................................................................ 28

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-14. Velocidad máxima [m/s] en la ubicación de la obra OA 01. Crecida de verificación (100 años).

Condición Sin Proyecto ........................................................................................................................................................ 29

Figura 4-15. Profundidad máxima [m] en la ubicación de la obra OA 01. Crecida de diseño (50 años). Condición

Con Proyecto.......................................................................................................................................................................... 29

Figura 4-16. Velocidad máxima [m/s] en la ubicación de la obra OA 01. Crecida de diseño (50 años). Condición

Con Proyecto.......................................................................................................................................................................... 30

Figura 4-17. Profundidad máxima [m] en la ubicación de la obra OA 01. Crecida de verificación (100 años).

Condición Con Proyecto ...................................................................................................................................................... 30

Figura 4-18. Velocidad máxima [m/s] en la ubicación de la obra OA 01. Crecida de verificación (100 años).

Condición Con Proyecto ....................................................................................................................................................... 31

Figura 4-19. Profundidad máxima [m] en la ubicación de la obra OA 03. Crecida de diseño (50 años).

Condición Sin Proyecto ........................................................................................................................................................ 32

Figura 4-20. Velocidad máxima [m/s] en la ubicación de la obra OA 03. Crecida de diseño (50 años). Condición

Sin Proyecto ........................................................................................................................................................................... 33

Figura 4-21. Profundidad máxima [m] en la ubicación de la obra OA 03. Crecida de verificación (100 años).

Condición Sin Proyecto ........................................................................................................................................................ 33

Figura 4-22. Velocidad máxima [m/s] en la ubicación de la obra OA 03. Crecida de verificación (100 años).

Condición Sin Proyecto ........................................................................................................................................................ 34

Figura 4-23. Profundidad máxima [m] en la ubicación de la obra OA 03. Crecida de diseño (50 años).

Condición Con Proyecto ...................................................................................................................................................... 34

Figura 4-24. Velocidad máxima [m/s] en la ubicación de la obra OA 03. Crecida de diseño (50 años). Condición

Con Proyecto.......................................................................................................................................................................... 35

Figura 4-25. Profundidad máxima [m] en la ubicación de la obra OA 03. Crecida de verificación (100 años).

Condición Con Proyecto ...................................................................................................................................................... 35

Figura 4-26. Velocidad máxima [m/s] en la ubicación de la obra OA 03. Crecida de verificación (100 años).

Condición Con Proyecto ...................................................................................................................................................... 36

Figura 4-27. Área de interés (rojo) y perfiles aguas arriba y aguas abajo (púrpura) referenciales para los

resultados de la obra OA 01 ................................................................................................................................................37

Figura 4-28. Área de interés (rojo) y perfiles aguas arriba y aguas abajo (púrpura) referenciales para los

resultados de la obra OA 03 ............................................................................................................................................... 38

# Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................... 6

Tabla 3-1. Coeficiente de rugosidad de Manning con método Cowan ..................................................................... 12

Tabla 3-2. Condiciones de borde e iniciales ..................................................................................................................... 13

Tabla 3-3. -Curva de descarga a la salida del cauce C_01 ............................................................................................ 13

iv Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Tabla 4-1. Resultados área de interés aguas arriba de la obra OA 01 ......................................................................37

Tabla 4-2. Resultados área de interés aguas abajo de la obra OA 01 ......................................................................37

Tabla 4-3. Resultados área de interés aguas arriba de la obra OA 03 .................................................................... 38

Tabla 4-4. Resultados área de interés aguas abajo de la obra OA 03 .................................................................... 38

v Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

# 1. Introducción

Se construyó el modelo hidráulico de las obras de atravieso OA 01 y OA 03 emplazadas sobre el cauce C_01,

empleando para ello el software HEC-RAS (HEC, 2024). El objetivo del modelo es representar la condición

actual del cauce sin proyecto y su condición futura, con proyecto, para los caudales de diseño y verificación

de la obra

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados relevantes de cada caso.

# 2. Descripción del modelo

El modelo se construyó con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La

descripción general de cada modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|Sin Proyecto|Representa la condición actual del cauce, en una extensión total de<br>658 m a lo largo de su eje y manteniendo más de 130 m hacia aguas<br>arriba y hacia aguas abajo desde el inicio y fin de cada obra proyectada.|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|Con Proyecto|Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, pero además se incorporan las obras<br>proyectadas: (i) OA 01, correspondiente a una alcantarilla bajo camino<br>interno de cajón de hormigón armado de sección 2.0 x 1.5 m y longitud<br>de 15.1 m; y (ii) OA 03, alcantarilla bajo cerco perimetral de cajón de<br>hormigón armado de sección 2.0 x 1.5 m y longitud de 7.0 m.|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

# 3. Parámetros de entrada

## 3.1. Topografía

La empresa FORESTIA SPA realizó un levantamiento topográfico mediante LiDAR aerotransportado en

septiembre de 2023. La ventaja del vuelo LiDAR frente a otro tipo de levantamientos es que permite filtrar

algunos elementos ajenos a la superficie de terreno, como, por ejemplo, la vegetación, logrando de esta

forma una mejor representación del fondo de los cauces.

Como producto del levantamiento se generó un Modelo Digital de Terreno (MDT) con resolución de 0.5 m,

el cual representa el terreno sin objetos ajenos como infraestructura o árboles, los que fueron removidos

con técnicas de postproceso y filtrado. La representación del MDT se muestra a continuación:

Figura 3-1. Representación del modelo digital de terreno (MDT)

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

## 3.2. Obras proyectadas

La plataforma del camino y las obras de atravieso se proyectaron mediante las herramientas de geometría

de HEC-RAS y las modificaciones de terreno de RAS Mapper. A continuación, se muestra el terreno sin y con

las obras incorporadas.

### 3.2.1. Proyección obra de atravieso OA 01

Figura 3-2: Topografía de la zona de estudio de la obra OA 01, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Sin Proyecto

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 3-3. Topografía de la zona de estudio de la obra OA 01, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Con Proyecto

### 3.2.2. Proyección obra de atravieso OA 03

Figura 3-4: Topografía de la zona de estudio de la obra OA 03, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Sin Proyecto

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 3-5. Topografía de la zona de estudio de la obra OA 03, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Con Proyecto

## 3.3. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método de Cowan (MOP, 2023), que emplea

la siguiente ecuación:

## n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

n : coeficiente de rugosidad de Manning

m : coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : coeficiente asociado al material del lecho

n 1 : coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : coeficiente asociado a la variación de las secciones transversales

## n 3 : coeficiente asociado al efecto relativo de las obstrucciones

n 4 : coeficiente asociado a la densidad de vegetación

De esta forma, el coeficiente de rugosidad se estimó según las características de los cauces observadas en

terreno y lo evidenciado en la ortofoto del proyecto. En la Figura 3-6 se muestra la ortofoto, mientras que

en la Figura 3-7 se presentan fotografías de los cauces.

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 3-6. Ortofoto de terreno en ubicación de las obras OA 01 y OA 03

Figura 3-7. Registro fotográfico visita a terreno en ubicación de las obras OA 01 (izquierda) y OA 03

(derecha). Cauce C_01

La Tabla 3-1 muestra la condición de los cauces según los criterios del método y los valores del coeficiente

de rugosidad de Manning para el cauce.

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Tabla 3-1. Coeficiente de rugosidad de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Alternándose<br>ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Despreciable|n3|0.000|
|Densidad de vegetación|Media|n4|0.015|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.045|

En cambio, para las obras proyectadas correspondientes a alcantarillas de cajón de hormigón se asignó un

valor de rugosidad igual a 0.014, basado en valores tabulados en la literatura (Chow, 1994).

## 3.4. Condiciones de borde e iniciales

Se definieron tres tipos de condiciones de borde (CB): (i) inicial o aguas arriba, (ii) intermedia y (iii) final o

aguas abajo. La CB de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés. Por

otro lado, parte del modelo posee una longitud de cauce significativa y sus caudales pueden variar entre su

inicio y final, ya que el área drenante de su cuenca aumenta a medida que se avanza hacia aguas abajo. En

estos casos se agrega una CB intermedia, cuyo objetivo es añadir un incremento de caudal al modelo para

representar el aumento del flujo a lo largo del cauce. Por último, se incluye la CB aguas abajo para permitir

la salida del flujo.

En resumen, las CB aguas arriba e intermedias incluyen parámetros de caudal en función de su ubicación a

lo largo del cauce y, además, incorporan un parámetro de pendiente normal a partir de la topografía del

modelo. Por otro lado, para la CB aguas abajo normalmente se utiliza la pendiente normal, pero en este caso

se optó por otro tipo de condición. En concreto, se empleó una condición de curva de descarga, con la

finalidad de representar de mejor manera la restricción que tiene el flujo al llegar al camino público,

planteando así un escenario más realista y conservador respecto a una condición de pendiente normal. Esta

condición establece una relación entre el caudal y la cota de agua, la cual fue calibrada a partir de los

resultados del modelo hidráulico desarrollado para el estudio de inundación.

Los caudales de CB inicial o intermedia están asociados a los periodos de retorno de diseño y verificación de

las obras, correspondientes a 50 y 100 años, respectivamente. Un resumen de las CB y su ubicación se

presenta en la Tabla 3-2 y Figura 3-8. Por otro lado, la relación cota vs caudal de la curva de descarga se

muestra en la Tabla 3-3.

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB<br>intermedia|CB aguas<br>abajo|Caudal de<br>diseño<br>[m3/s]|Caudal de<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|---|
|US_00||✅||0.14|0.16|0.020|
|US_01|✅|||2.70|3.18|0.025|
|DS|||✅|-|-|-|

Tabla 3-3. -Curva de descarga a la salida del cauce C_01

|Cota de agua<br>(msnm)|Caudal (m3/s)|
|---|---|
|196.49|0|
|196.95|1.89|
|197.51|3.22|
|198.57|3.35|

Figura 3-8. Ubicación condiciones de borde y layout (negro)

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

A continuación, se muestra un esquema general para la obtención de los caudales intermedios y aguas arriba

indicados en la Figura 3-9:

Figura 3-9. Esquema general para la obtención de condiciones de borde

Donde:

Q 0 : caudal de la cuenca ubicada aguas arriba

Q i : caudal de las cuencas intermedias, donde i= 1,2

US 0 : caudal asociado a la condición de borde aguas arriba ubicada en el cierre de la cuenca 0

US i : caudal asociado a la condición de borde intermedia ubicada en el cierre de la cuenca i

Cabe mencionar que, para mantener el orden, se conservó la numeración de las cuencas delimitadas en la

condición intermedia o aguas arriba. Los detalles de los valores de los caudales asociados a las cuencas se

presentan en el Anexo 1.

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Por otro lado, si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere

de un hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma

constante a la simulación, se optó por añadir un hidrograma que van de cero al máximo en un periodo de 1

hora y permanece constante por, a lo más, un periodo de 2 horas.

Los hidrogramas de entrada utilizados para el modelo del cauce natural sin nombre se muestra a

continuación:

Figura 3-10. Hidrogramas de entrada. Crecida de diseño (50 años)

15 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 3-11. Hidrogramas de entrada. Crecida de verificación (100 años)

## 3.5. Otras consideraciones

En el modelo, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción SWE-ELM

en HEC-RAS 6.5). Además, el área de flujo se discretizó en celdas de 1.0 x 1.0 m y se utilizó un paso de tiempo

de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.1 y un máximo

de 0.3. Se consideró un tiempo de modelo de 3 horas para que el flujo entrara en régimen permanente, con

caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

Adicionalmente, se consideró un breakline a lo largo del eje del cauce, que mantiene celdas de 1.0 x 1.0 m,

tal como se muestra en la Figura 3-8 (en color rojo). El objetivo de esto es representar de mejor forma el

cauce y plantear una mejor situación para el cálculo iterativo del modelo y eventuales inestabilidades

numéricas.

Para terminar, en el caso de la condición con proyecto, en las alcantarillas se aumentó el coeficiente de

perdida en la entrada a 1 para plantear un escenario conservador.

16 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

# 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación del modelo:

## 4.1. Resultados modelo completo

### 4.1.1. Condición sin proyecto

Figura 4-1. Profundidad máxima [m] con layout proyecto (color negro). Crecida de diseño (50 años).

Condición Sin Proyecto

17 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-2. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de diseño (50 años).

Condición Sin Proyecto

18 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-3. Profundidad máxima [m] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Sin Proyecto

19 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-4. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Sin Proyecto

20 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-5. Hidrograma a la salida del modelo. Condición Sin Proyecto

21 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

### 4.1.2. Condición con proyecto

Figura 4-6. Profundidad máxima [m] con layout proyecto (color negro). Crecida de diseño (50 años).

Condición Con Proyecto

22 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-7. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de diseño (50 años).

Condición Con Proyecto

23 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-8. Profundidad máxima [m] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Con Proyecto

24 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-9. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Con Proyecto

25 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-10. Hidrograma a la salida del modelo. Condición Con Proyecto

26 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

## 4.2. Resultados obra de atravieso OA 01

### 4.2.1. Condición sin proyecto

Figura 4-11. Profundidad máxima [m] en la ubicación de la obra OA 01. Crecida de diseño (50 años).

Condición Sin Proyecto

27 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-12. Velocidad máxima [m/s] en la ubicación de la obra OA 01. Crecida de diseño (50 años).

Condición Sin Proyecto

Figura 4-13. Profundidad máxima [m] en la ubicación de la obra OA 01. Crecida de verificación (100 años).

Condición Sin Proyecto

28 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-14. Velocidad máxima [m/s] en la ubicación de la obra OA 01. Crecida de verificación (100 años).

Condición Sin Proyecto

### 4.2.2. Condición con proyecto

Figura 4-15. Profundidad máxima [m] en la ubicación de la obra OA 01. Crecida de diseño (50 años).

Condición Con Proyecto

29 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-16. Velocidad máxima [m/s] en la ubicación de la obra OA 01. Crecida de diseño (50 años).

Condición Con Proyecto

Figura 4-17. Profundidad máxima [m] en la ubicación de la obra OA 01. Crecida de verificación (100 años).

Condición Con Proyecto

30 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-18. Velocidad máxima [m/s] en la ubicación de la obra OA 01. Crecida de verificación (100 años).

Condición Con Proyecto

31 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

## 4.3. Resultados obra de atravieso OA 03

### 4.3.1. Condición sin proyecto

Figura 4-19. Profundidad máxima [m] en la ubicación de la obra OA 03. Crecida de diseño (50 años).

Condición Sin Proyecto

32 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-20. Velocidad máxima [m/s] en la ubicación de la obra OA 03. Crecida de diseño (50 años).

Condición Sin Proyecto

Figura 4-21. Profundidad máxima [m] en la ubicación de la obra OA 03. Crecida de verificación (100 años).

Condición Sin Proyecto

33 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-22. Velocidad máxima [m/s] en la ubicación de la obra OA 03. Crecida de verificación (100 años).

Condición Sin Proyecto

### 4.3.2. Condición con proyecto

Figura 4-23. Profundidad máxima [m] en la ubicación de la obra OA 03. Crecida de diseño (50 años).

Condición Con Proyecto

34 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-24. Velocidad máxima [m/s] en la ubicación de la obra OA 03. Crecida de diseño (50 años).

Condición Con Proyecto

Figura 4-25. Profundidad máxima [m] en la ubicación de la obra OA 03. Crecida de verificación (100 años).

Condición Con Proyecto

35 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-26. Velocidad máxima [m/s] en la ubicación de la obra OA 03. Crecida de verificación (100 años).

Condición Con Proyecto

## 4.4. Resumen de resultados

A continuación, se presenta un resumen de los resultados de profundidad y velocidad, incluyendo los valores

mínimo, máximo y promedio para la condición de diseño. Los resultados fueron extraídos de un buffer de 5

m medidos hacia aguas arriba y aguas abajo desde el inicio y fin de la obra, respectivamente (ver Figura 4-27

y Figura 4-28).

36 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-27. Área de interés (rojo) y perfiles aguas arriba y aguas abajo (púrpura) referenciales para los

resultados de la obra OA 01

Tabla 4-1. Resultados área de interés aguas arriba de la obra OA 01

|Condición|Profundidad<br>[m]|Col3|Col4|Velocidad<br>[m/s]|Col6|Col7|
|---|---|---|---|---|---|---|
|Condición|Máx.|Med.|Mín.|Máx.|Med.|Mín.|
|Sin Proyecto|~~0.439~~|~~0.247~~|~~0.006~~|~~2.051~~|~~1.128~~|~~0.057~~|
|Con Proyecto|0.795|0.404|0.024|1.297|0.272|0.000|
|Diferencia(*)|~~-0.356~~|~~-0.157~~|~~-0.018~~|~~0.754~~|~~0.856~~|~~0.057~~|

(*) Condición SP - Condición CP

Tabla 4-2. Resultados área de interés aguas abajo de la obra OA 01

|Condición|Profundidad<br>[m]|Col3|Col4|Velocidad<br>[m/s]|Col6|Col7|
|---|---|---|---|---|---|---|
|Condición|Máx.|Med.|Mín.|Máx.|Med.|Mín.|
|Sin Proyecto|~~0.551~~|~~0.319~~|~~0.083~~|~~3.018~~|~~1.794~~|~~0.084~~|
|Con Proyecto|0.631|0.371|0.098|2.814|1.605|0.457|
|Diferencia(*)|-0.08|-0.052|-0.015|0.204|0.189|-0.373|

(*) Condición SP - Condición CP

37 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-28. Área de interés (rojo) y perfiles aguas arriba y aguas abajo (púrpura) referenciales para los

resultados de la obra OA 03

Tabla 4-3. Resultados área de interés aguas arriba de la obra OA 03

|Condición|Profundidad<br>[m]|Col3|Col4|Velocidad<br>[m/s]|Col6|Col7|
|---|---|---|---|---|---|---|
|Condición|Máx.|Med.|Mín.|Máx.|Med.|Mín.|
|Sin Proyecto|~~0.825~~|~~0.549~~|~~0.062~~|~~1.722~~|~~0.876~~|~~0.043~~|
|Con Proyecto|1.150|0.450|0.030|1.107|0.626|0.052|
|Diferencia(*)|~~-0.325~~|~~0.099~~|~~0.032~~|~~0.615~~|~~0.25~~|~~-0.009~~|

(*) Condición SP - Condición CP

Tabla 4-4. Resultados área de interés aguas abajo de la obra OA 03

|Condición|Profundidad<br>[m]|Col3|Col4|Velocidad<br>[m/s]|Col6|Col7|
|---|---|---|---|---|---|---|
|Condición|Máx.|Med.|Mín.|Máx.|Med.|Mín.|
|Sin Proyecto|0.619|0.405|0.093|2.470|2.018|1.351|
|Con Proyecto|2.013|1.321|0.551|0.668|0.373|0.003|
|Diferencia(*)|~~-1.394~~|~~-0.916~~|~~-0.458~~|~~1.802~~|~~1.645~~|~~1.348~~|

(*) Condición SP - Condición CP

38 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.01. MODELO HIDRÁULICO PAS 156. OA 01 Y OA 03

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

# 5. Referencias

HEC. (2024). HEC-RAS. Versión 6.6. HEC-RAS. Versión 6.6. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2023). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

39 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO EMÚ para TIKUNA

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
|0|-|06/03/2025|Adenda comp.|DPP|BGP|ABL|
|A|-|27/02/2025|Revisión cliente|DPP/CHR|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comuna de Marchigüe<br>Región de O’Higgins|Col3|
|---|---|---|
||Apéndice 3.02. Modelo Hidráulico PAS 156.<br>OA 02 y OA 04|Rev. 0|

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

# Contenidos

1. Introducción ......................................................................................................................................... 6

2. Descripción del modelo ...................................................................................................................... 6

3. Parámetros de entrada ...................................................................................................................... 6

3.1. Topografía ............................................................................................................................................. 6
3.2. Obras proyectadas................................................................................................................................ 7

3.2.1. Proyección obra de atravieso OA 02 ...................................................................................................... 8

3.2.2. Proyección obra de atravieso OA 04 ..................................................................................................... 10

3.3. Coeficiente de rugosidad ................................................................................................................... 11
3.4. Condiciones de borde e iniciales ...................................................................................................... 13

3.5. Otras consideraciones ........................................................................................................................ 17

4. Resultados ......................................................................................................................................... 18

4.1. Resultados modelo completo .......................................................................................................... 18

4.1.1. Condición sin proyecto .............................................................................................................................. 18

4.1.2. Condición con proyecto ............................................................................................................................ 23

4.2. Resultados obra de atravieso OA 02 ............................................................................................ 28

4.2.1. Condición sin proyecto ............................................................................................................................. 28

4.2.2. Condición con proyecto ............................................................................................................................. 31

4.3. Resultados obra de atravieso OA 04 ............................................................................................ 34

4.3.1. Condición sin proyecto ............................................................................................................................. 34

4.3.2. Condición con proyecto ............................................................................................................................ 36

4.4. Resumen de resultados .................................................................................................................... 38

5. Referencias ........................................................................................................................................ 41

# Figuras

Figura 3-1. Representación del modelo digital de terreno (MDT) ............................................................................... 7

Figura 3-2: Topografía de la zona de estudio de la obra OA 02, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Sin Proyecto ...................................................................... 8

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 3-3. Topografía de la zona de estudio de la obra OA 02, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Con Proyecto ..................................................................... 9

Figura 3-4: Topografía de la zona de estudio de la obra OA 04, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Sin Proyecto ..................................................................... 10

Figura 3-5. Topografía de la zona de estudio de la obra OA 04, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Con Proyecto .................................................................... 10

Figura 3-6. Ortofoto de terreno en ubicación de las obras OA 02 y OA 04 ............................................................ 12

Figura 3-7. Registro fotográfico visita a terreno en ubicación de las obras OA 02 (izquierda) y OA 04

(derecha). Cauce C_02 .......................................................................................................................................................... 12

Figura 3-8. Ubicación condiciones de borde y layout (negro) .................................................................................... 14

Figura 3-9. Esquema general para la obtención de condiciones de borde .............................................................. 15

Figura 3-10. Hidrogramas de entrada. Crecida de diseño (50 años) ......................................................................... 16

Figura 3-11. Hidrogramas de entrada. Crecida de verificación (100 años) ............................................................... 17

Figura 4-1. Profundidad máxima [m] con layout proyecto (color negro). Crecida de diseño (50 años).

Condición Sin Proyecto ......................................................................................................................................................... 18

Figura 4-2. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de diseño (50 años).

Condición Sin Proyecto ......................................................................................................................................................... 19

Figura 4-3. Profundidad máxima [m] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Sin Proyecto ........................................................................................................................................................ 20

Figura 4-4. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Sin Proyecto ......................................................................................................................................................... 21

Figura 4-5. Hidrograma a la salida del modelo. Condición Sin Proyecto .................................................................22

Figura 4-6. Profundidad máxima [m] con layout proyecto (color negro). Crecida de diseño (50 años).

Condición Con Proyecto ...................................................................................................................................................... 23

Figura 4-7. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de diseño (50 años). Condición

Con Proyecto.......................................................................................................................................................................... 24

Figura 4-8. Profundidad máxima [m] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Con Proyecto ...................................................................................................................................................... 25

Figura 4-9. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Con Proyecto ...................................................................................................................................................... 26

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto .............................................................. 27

Figura 4-11. Profundidad máxima [m] en la ubicación de la obra OA 02. Crecida de diseño (50 años). Condición

Sin Proyecto ........................................................................................................................................................................... 28

Figura 4-12. Velocidad máxima [m/s] en la ubicación de la obra OA 02. Crecida de diseño (50 años). Condición

Sin Proyecto ........................................................................................................................................................................... 29

Figura 4-13. Profundidad máxima [m] en la ubicación de la obra OA 02. Crecida de verificación (100 años).

Condición Sin Proyecto ........................................................................................................................................................ 30

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-14. Velocidad máxima [m/s] en la ubicación de la obra OA 02. Crecida de verificación (100 años).

Condición Sin Proyecto ........................................................................................................................................................ 30

Figura 4-15. Profundidad máxima [m] en la ubicación de la obra OA 02. Crecida de diseño (50 años).

Condición Con Proyecto ....................................................................................................................................................... 31

Figura 4-16. Velocidad máxima [m/s] en la ubicación de la obra OA 02. Crecida de diseño (50 años). Condición

Con Proyecto.......................................................................................................................................................................... 32

Figura 4-17. Profundidad máxima [m] en la ubicación de la obra OA 02. Crecida de verificación (100 años).

Condición Con Proyecto ...................................................................................................................................................... 32

Figura 4-18. Velocidad máxima [m/s] en la ubicación de la obra OA 02. Crecida de verificación (100 años).

Condición Con Proyecto ...................................................................................................................................................... 33

Figura 4-19. Profundidad máxima [m] en la ubicación de la obra OA 04. Crecida de diseño (50 años).

Condición Sin Proyecto ........................................................................................................................................................ 34

Figura 4-20. Velocidad máxima [m/s] en la ubicación de la obra OA 04. Crecida de diseño (50 años).

Condición Sin Proyecto ........................................................................................................................................................ 35

Figura 4-21. Profundidad máxima [m] en la ubicación de la obra OA 04. Crecida de verificación (100 años).

Condición Sin Proyecto ........................................................................................................................................................ 35

Figura 4-22. Velocidad máxima [m/s] en la ubicación de la obra OA 04. Crecida de verificación (100 años).

Condición Sin Proyecto ........................................................................................................................................................ 36

Figura 4-23. Profundidad máxima [m] en la ubicación de la obra OA 04. Crecida de diseño (50 años).

Condición Con Proyecto ...................................................................................................................................................... 36

Figura 4-24. Velocidad máxima [m/s] en la ubicación de la obra OA 04. Crecida de diseño (50 años). Condición

Con Proyecto...........................................................................................................................................................................37

Figura 4-25. Profundidad máxima [m] en la ubicación de la obra OA 04. Crecida de verificación (100 años).

Condición Con Proyecto .......................................................................................................................................................37

Figura 4-26. Velocidad máxima [m/s] en la ubicación de la obra OA 04. Crecida de verificación (100 años).

Condición Con Proyecto ...................................................................................................................................................... 38

Figura 4-27. Área de interés (rojo) y perfiles aguas arriba y aguas abajo (púrpura) referenciales para los

resultados de la obra OA 02 ............................................................................................................................................... 39

Figura 4-28. Área de interés (rojo) y perfiles aguas arriba y aguas abajo (púrpura) referenciales para los

resultados de la obra OA 04 ..............................................................................................................................................40

# Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................... 6

Tabla 3-1. Coeficiente de rugosidad de Manning con método Cowan ..................................................................... 13

Tabla 3-2. Condiciones de borde e iniciales ..................................................................................................................... 14

Tabla 3-3. Curva de descarga a la salida del cauce C_01 .............................................................................................. 14

iv Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Tabla 4-1. Resultados área de interés aguas arriba de la obra OA 02 ..................................................................... 39

Tabla 4-2. Resultados área de interés aguas abajo de la obra OA 02 ..................................................................... 39

Tabla 4-3. Resultados área de interés aguas arriba de la obra OA 04 ...................................................................40

Tabla 4-4. Resultados área de interés aguas abajo de la obra OA 04 ....................................................................40

v Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

# 1. Introducción

Se construyó el modelo hidráulico de las obras de atravieso OA 02 y OA 04 emplazadas sobre el cauce C_02,

empleando para ello el software HEC-RAS (HEC, 2024). El objetivo del modelo es representar la condición

actual del cauce sin proyecto y su condición futura, con proyecto, para los caudales de diseño y verificación

de la obra

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados relevantes de cada caso.

# 2. Descripción del modelo

El modelo se construyó con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La

descripción general de cada modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|Sin Proyecto|Representa la condición actual del cauce, en una extensión total de<br>760 m a lo largo de su eje y manteniendo más de 130 m hacia aguas<br>arriba y hacia aguas abajo desde el inicio y fin de cada obra proyectada.|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|Con Proyecto|Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, pero además se incorporan las obras<br>proyectadas: (i) OA 02, correspondiente a una alcantarilla bajo camino<br>interno de cajón de hormigón armado de sección 2.0 x 1.5 m y longitud<br>de 11.3 m; y (ii) OA 04, alcantarilla bajo cerco perimetral de cajón de<br>hormigón armado de sección 2.0 x 1.5 m y longitud de 6.0 m.|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

# 3. Parámetros de entrada

## 3.1. Topografía

La empresa FORESTIA SPA realizó un levantamiento topográfico mediante LiDAR aerotransportado en

septiembre de 2023. La ventaja del vuelo LiDAR frente a otro tipo de levantamientos es que permite filtrar

algunos elementos ajenos a la superficie de terreno, como, por ejemplo, la vegetación, logrando de esta

forma una mejor representación del fondo de los cauces.

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Como producto del levantamiento se generó un Modelo Digital de Terreno (MDT) con resolución de 0.5 m,

el cual representa el terreno sin objetos ajenos como infraestructura o árboles, los que fueron removidos

con técnicas de postproceso y filtrado. La representación del MDT se muestra a continuación:

Figura 3-1. Representación del modelo digital de terreno (MDT)

## 3.2. Obras proyectadas

La plataforma del camino y las obras de atravieso se proyectaron mediante las herramientas de geometría

de HEC-RAS y las modificaciones de terreno de RAS Mapper. A continuación, se muestra el terreno con las

obras incorporadas.

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

### 3.2.1. Proyección obra de atravieso OA 02

Figura 3-2: Topografía de la zona de estudio de la obra OA 02, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Sin Proyecto

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 3-3. Topografía de la zona de estudio de la obra OA 02, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Con Proyecto

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

### 3.2.2. Proyección obra de atravieso OA 04

Figura 3-4: Topografía de la zona de estudio de la obra OA 04, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Sin Proyecto

Figura 3-5. Topografía de la zona de estudio de la obra OA 04, incluyendo una representación del cerco

perimetral y caminos internos (color negro). Condición Con Proyecto

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

## 3.3. Coeficiente de rugosidad

Se estimó el coeficiente de rugosidad de cada cauce a partir del método de Cowan (MOP, 2023), que emplea

la siguiente ecuación:

## n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

n : coeficiente de rugosidad de Manning

m : coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : coeficiente asociado al material del lecho

n 1 : coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : coeficiente asociado a la variación de las secciones transversales

## n 3 : coeficiente asociado al efecto relativo de las obstrucciones

n 4 : coeficiente asociado a la densidad de vegetación

De esta forma, el coeficiente de rugosidad se estimó según las características de los cauces observadas en

terreno y lo evidenciado en la ortofoto del proyecto. En la Figura 3-6 se muestra la ortofoto, mientras que

en la Figura 3-7 se presentan fotografías de los cauces.

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 3-6. Ortofoto de terreno en ubicación de las obras OA 02 y OA 04

Figura 3-7. Registro fotográfico visita a terreno en ubicación de las obras OA 02 (izquierda) y OA 04

(derecha). Cauce C_02

La Tabla 3-1 muestra la condición de los cauces según los criterios del método y los valores del coeficiente

de rugosidad de Manning para el cauce.

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Tabla 3-1. Coeficiente de rugosidad de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Alternándose<br>ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Despreciable|n3|0.000|
|Densidad de vegetación|Media|n4|0.015|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.045|

En cambio, para las obras proyectadas correspondientes a alcantarillas de cajón de hormigón se asignó un

valor de rugosidad igual a 0.014, basado en valores tabulados en la literatura (Chow, 1994).

## 3.4. Condiciones de borde e iniciales

Se definieron tres tipos de condiciones de borde (CB): (i) inicial o aguas arriba, (ii) intermedia y (iii) final o

aguas abajo. La CB de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés. Por

otro lado, parte del modelo posee una longitud de cauce significativa y sus caudales pueden variar entre su

inicio y final, ya que el área drenante de su cuenca aumenta a medida que se avanza hacia aguas abajo. En

estos casos se agrega una CB intermedia, cuyo objetivo es añadir un incremento de caudal al modelo para

representar el aumento del flujo a lo largo del cauce. Por último, se incluye la CB aguas abajo para permitir

la salida del flujo.

En resumen, las CB aguas arriba e intermedias incluyen parámetros de caudal en función de su ubicación a

lo largo del cauce y, además, incorporan un parámetro de pendiente normal a partir de la topografía del

modelo. Por otro lado, para la CB aguas abajo normalmente se utiliza la pendiente normal, pero en este caso

se optó por otro tipo de condición. En concreto, se empleó una condición de curva de descarga, con la

finalidad de representar de mejor manera la restricción que tiene el flujo al llegar al camino público,

planteando así un escenario más realista y conservador respecto a una condición de pendiente normal. Esta

condición establece una relación entre el caudal y la cota de agua, la cual fue calibrada a partir de los

resultados del modelo hidráulico desarrollado para el estudio de inundación.

Los caudales de CB inicial o intermedia están asociados a los periodos de retorno de diseño y verificación de

las obras, correspondientes a 50 y 100 años, respectivamente. Un resumen de las CB y su ubicación se

presenta en la Tabla 3-2 y Figura 3-8: Por otro lado, la relación cota vs caudal de la curva de descarga se

muestra en la Tabla 3-3.

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB<br>intermedia|CB aguas<br>abajo|Caudal de<br>diseño<br>[m3/s]|Caudal de<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|---|
|US_00||✅||0.54|0.63|0.01|
|US_01|✅|||1.98|2.34|0.03|
|DS|||✅|-|-|-|

Tabla 3-3. Curva de descarga a la salida del cauce C_01

|Cota de agua<br>(msnm)|Caudal (m3/s)|
|---|---|
|196.4|0|
|196.8|1.56|
|197|2.04|
|197.5|2.45|
|197.9|2.79|
|198.5|2.91|
|198.6|2.99|

Figura 3-8. Ubicación condiciones de borde y layout (negro)

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

A continuación, se muestra un esquema general para la obtención de los caudales intermedios y aguas arriba

indicados en la Figura 3-9:

Figura 3-9. Esquema general para la obtención de condiciones de borde

Donde:

Q 0 : caudal de la cuenca ubicada aguas arriba

Q i : caudal de las cuencas intermedias, donde i= 1,2

US 0 : caudal asociado a la condición de borde aguas arriba ubicada en el cierre de la cuenca 0

US i : caudal asociado a la condición de borde intermedia ubicada en el cierre de la cuenca i

Cabe mencionar que, para mantener el orden, se conservó la numeración de las cuencas delimitadas en la

condición intermedia o aguas arriba. Los detalles de los valores de los caudales asociados a las cuencas se

presentan en el Anexo 1.

15 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Por otro lado, si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere

de un hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma

constante a la simulación, se optó por añadir un hidrograma que van de cero al máximo en un periodo de 1

hora y permanece constante por, a lo más, un periodo de 2 horas.

Los hidrogramas de entrada utilizados para el modelo del cauce natural sin nombre se muestra a

continuación:

Figura 3-10. Hidrogramas de entrada. Crecida de diseño (50 años)

16 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 3-11. Hidrogramas de entrada. Crecida de verificación (100 años)

## 3.5. Otras consideraciones

En el modelo, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción SWE-ELM

en HEC-RAS 6.5). Además, el área de flujo se discretizó en celdas de 1.0 x 1.0 m y se utilizó un paso de tiempo

de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.2 y un máximo

de 0.05. Se consideró un tiempo de modelo de 3 horas para que el flujo entrara en régimen permanente, con

caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

Adicionalmente, se consideró una zona de refinamiento con celdas de 0.2 x 0.2 m, un breakline a lo largo del

cauce con celdas de 1.0 x 1.0 m y dos breaklines con celdas de 0.25 x 0.25 m, los cuales se muestran en la

Figura 3-8 (con color rojo). El objetivo de esto es representar de mejor forma el cauce y plantear una mejor

situación para el cálculo iterativo del modelo y eventuales inestabilidades numéricas.

Para terminar, en el caso de la condición con proyecto, en las alcantarillas se aumentó el coeficiente de

perdida en la entrada a 1 para plantear un escenario conservador.

17 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

# 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación del modelo:

## 4.1. Resultados modelo completo

### 4.1.1. Condición sin proyecto

Figura 4-1. Profundidad máxima [m] con layout proyecto (color negro). Crecida de diseño (50 años).

Condición Sin Proyecto

18 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-2. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de diseño (50 años).

Condición Sin Proyecto

19 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-3. Profundidad máxima [m] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Sin Proyecto

20 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-4. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Sin Proyecto

21 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-5. Hidrograma a la salida del modelo. Condición Sin Proyecto

22 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

### 4.1.2. Condición con proyecto

Figura 4-6. Profundidad máxima [m] con layout proyecto (color negro). Crecida de diseño (50 años).

Condición Con Proyecto

23 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-7. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de diseño (50 años).

Condición Con Proyecto

24 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-8. Profundidad máxima [m] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Con Proyecto

25 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-9. Velocidad máxima [m/s] con layout proyecto (color negro). Crecida de verificación (100 años).

Condición Con Proyecto

26 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto

27 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

## 4.2. Resultados obra de atravieso OA 02

### 4.2.1. Condición sin proyecto

Figura 4-11. Profundidad máxima [m] en la ubicación de la obra OA 02. Crecida de diseño (50 años).

Condición Sin Proyecto

28 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-12. Velocidad máxima [m/s] en la ubicación de la obra OA 02. Crecida de diseño (50 años).

Condición Sin Proyecto

29 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-13. Profundidad máxima [m] en la ubicación de la obra OA 02. Crecida de verificación (100 años).

Condición Sin Proyecto

Figura 4-14. Velocidad máxima [m/s] en la ubicación de la obra OA 02. Crecida de verificación (100 años).

Condición Sin Proyecto

30 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

### 4.2.2. Condición con proyecto

Figura 4-15. Profundidad máxima [m] en la ubicación de la obra OA 02. Crecida de diseño (50 años).

Condición Con Proyecto

31 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-16. Velocidad máxima [m/s] en la ubicación de la obra OA 02. Crecida de diseño (50 años).

Condición Con Proyecto

Figura 4-17. Profundidad máxima [m] en la ubicación de la obra OA 02. Crecida de verificación (100 años).

Condición Con Proyecto

32 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-18. Velocidad máxima [m/s] en la ubicación de la obra OA 02. Crecida de verificación (100 años).

Condición Con Proyecto

33 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

## 4.3. Resultados obra de atravieso OA 04

### 4.3.1. Condición sin proyecto

Figura 4-19. Profundidad máxima [m] en la ubicación de la obra OA 04. Crecida de diseño (50 años).

Condición Sin Proyecto

34 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-20. Velocidad máxima [m/s] en la ubicación de la obra OA 04. Crecida de diseño (50 años).

Condición Sin Proyecto

Figura 4-21. Profundidad máxima [m] en la ubicación de la obra OA 04. Crecida de verificación (100 años).

Condición Sin Proyecto

35 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-22. Velocidad máxima [m/s] en la ubicación de la obra OA 04. Crecida de verificación (100 años).

Condición Sin Proyecto

### 4.3.2. Condición con proyecto

Figura 4-23. Profundidad máxima [m] en la ubicación de la obra OA 04. Crecida de diseño (50 años).

Condición Con Proyecto

36 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-24. Velocidad máxima [m/s] en la ubicación de la obra OA 04. Crecida de diseño (50 años).

Condición Con Proyecto

Figura 4-25. Profundidad máxima [m] en la ubicación de la obra OA 04. Crecida de verificación (100 años).

Condición Con Proyecto

37 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-26. Velocidad máxima [m/s] en la ubicación de la obra OA 04. Crecida de verificación (100 años).

Condición Con Proyecto

## 4.4. Resumen de resultados

A continuación, se presenta un resumen de los resultados de profundidad y velocidad, incluyendo los valores

mínimo, máximo y promedio para la condición de diseño. Los resultados fueron extraídos de un buffer de 5

m medidos hacia aguas arriba y aguas abajo desde el inicio y fin de la obra, respectivamente (ver Figura 4-27

y Figura 4-28).

38 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-27. Área de interés (rojo) y perfiles aguas arriba y aguas abajo (púrpura) referenciales para los

resultados de la obra OA 02

Tabla 4-1. Resultados área de interés aguas arriba de la obra OA 02

|Condición|Profundidad<br>[m]|Col3|Col4|Velocidad<br>[m/s]|Col6|Col7|
|---|---|---|---|---|---|---|
|Condición|Máx.|Med.|Mín.|Máx.|Med.|Mín.|
|Sin Proyecto|0.440|0.124|0.001|2.467|1.063|0.021|
|Con Proyecto|0.970|0.245|0.001|2.636|1.080|0.016|
|Diferencia(*)|~~-0.53~~|~~-0.121~~|~~0.000~~|~~-0.169~~|~~-0.017~~|~~0.005~~|

(*) Condición SP - Condición CP

Tabla 4-2. Resultados área de interés aguas abajo de la obra OA 02

|Condición|Profundidad<br>[m]|Col3|Col4|Velocidad<br>[m/s]|Col6|Col7|
|---|---|---|---|---|---|---|
|Condición|Máx.|Med.|Mín.|Máx.|Med.|Mín.|
|Sin Proyecto|~~1.240~~|~~0.270~~|~~0.003~~|~~2.188~~|~~0.796~~|~~0.007~~|
|Con Proyecto|0.916|0.536|0.013|0.667|0.481|0.050|
|Diferencia(*)|~~0.324~~|~~-0.266~~|~~-0.01~~|~~1.521~~|~~0.315~~|~~-0.043~~|

(*) Condición SP - Condición CP

39 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

Figura 4-28. Área de interés (rojo) y perfiles aguas arriba y aguas abajo (púrpura) referenciales para los

resultados de la obra OA 04

Tabla 4-3. Resultados área de interés aguas arriba de la obra OA 04

|Condición|Profundidad<br>[m]|Col3|Col4|Velocidad<br>[m/s]|Col6|Col7|
|---|---|---|---|---|---|---|
|Condición|Máx.|Med.|Mín.|Máx.|Med.|Mín.|
|Sin Proyecto|0.909|0.438|0.136|3.354|1.692|0.244|
|Con Proyecto|1.104|0.660|0.019|2.877|1.730|0.072|
|Diferencia(*)|~~-0.195~~|~~-0.222~~|~~0.117~~|~~0.477~~|~~-0.038~~|~~0.172~~|

(*) Condición SP - Condición CP

Tabla 4-4. Resultados área de interés aguas abajo de la obra OA 04

|Condición|Profundidad<br>[m]|Col3|Col4|Velocidad<br>[m/s]|Col6|Col7|
|---|---|---|---|---|---|---|
|Condición|Máx.|Med.|Mín.|Máx.|Med.|Mín.|
|Sin Proyecto|~~0.880~~|~~0.418~~|~~0.008~~|~~1.880~~|~~0.781~~|~~0.070~~|
|Con Proyecto|0.977|0.489|0.003|1.343|0.651|0.024|
|Diferencia(*)|~~-0.097~~|~~-0.071~~|~~0.005~~|~~0.537~~|~~0.13~~|~~0.046~~|

(*) Condición SP - Condición CP

40 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

APÉNDICE 3.02. MODELO HIDRÁULICO PAS 156. OA 02 Y OA 04

PERMISO AMBIENTAL SECTORIAL 156
PARQUE FOTOVOLTAICO EMÚ

# 5. Referencias

HEC. (2024). HEC-RAS. Versión 6.6. HEC-RAS. Versión 6.6. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2023). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

41 Baqua Ingeniería
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
| Sin Proyecto | Representa la condición actual del cauce, en una extensión total de<br>760 m a lo largo de su eje y manteniendo más de 130 m hacia aguas<br>arriba y hacia aguas abajo desde el inicio y fin de cada obra proyectada. | Representar<br>la<br>condición<br>actual<br>del<br>cauce |
| Con Proyecto | Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, pero además se incorporan las obras<br>proyectadas: (i) OA 02, correspondiente a una alcantarilla bajo camino<br>interno de cajón de hormigón armado de sección 2.0 x 1.5 m y longitud<br>de 11.3 m; y (ii) OA 04, alcantarilla bajo cerco perimetral de cajón de<br>hormigón armado de sección 2.0 x 1.5 m y longitud de 6.0 m. | Representar<br>la<br>condición<br>futura<br>del<br>cauce |

**Tabla 3-1.: Coeficiente de rugosidad de Manning con método Cowan**

| Condición del cauce | Col2 | Símbolo | Valor |
| --- | --- | --- | --- |
| Material del lecho | Tierra | n0 | 0.020 |
| Grado de irregularidad del perímetro mojado | Leve | n1 | 0.005 |
| Variación de las secciones transversales | Alternándose<br>ocasionalmente | n2 | 0.005 |
| Efecto relativo de las obstrucciones | Despreciable | n3 | 0.000 |
| Densidad de vegetación | Media | n4 | 0.015 |
| Sinuosidad y frecuencia de meandros | Leve | m | 1.000 |
| Coeficiente de rugosidad | Coeficiente de rugosidad | n | 0.045 |

**Tabla 3-2.: Condiciones de borde e iniciales**

| Nombre CB | CB aguas<br>arriba | CB<br>intermedia | CB aguas<br>abajo | Caudal de<br>diseño<br>[m3/s] | Caudal de<br>verificación<br>[m3/s] | Pendiente<br>[m/m] |
| --- | --- | --- | --- | --- | --- | --- |
| US_00 |  | ✅ |  | 0.54 | 0.63 | 0.01 |
| US_01 | ✅ |  |  | 1.98 | 2.34 | 0.03 |
| DS |  |  | ✅ | - | - | - |

**Tabla 3-3.: Curva de descarga a la salida del cauce C_01**

| Cota de agua<br>(msnm) | Caudal (m3/s) |
| --- | --- |
| 196.4 | 0 |
| 196.8 | 1.56 |
| 197 | 2.04 |
| 197.5 | 2.45 |
| 197.9 | 2.79 |
| 198.5 | 2.91 |
| 198.6 | 2.99 |

**Tabla 4-1.: Resultados área de interés aguas arriba de la obra OA 02**

| Condición | Profundidad<br>[m] | Col3 | Col4 | Velocidad<br>[m/s] | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Condición | Máx. | Med. | Mín. | Máx. | Med. | Mín. |
| Sin Proyecto | 0.440 | 0.124 | 0.001 | 2.467 | 1.063 | 0.021 |
| Con Proyecto | 0.970 | 0.245 | 0.001 | 2.636 | 1.080 | 0.016 |
| Diferencia(*) | ~~-0.53~~ | ~~-0.121~~ | ~~0.000~~ | ~~-0.169~~ | ~~-0.017~~ | ~~0.005~~ |

**Tabla 4-2.: Resultados área de interés aguas abajo de la obra OA 02**

| Condición | Profundidad<br>[m] | Col3 | Col4 | Velocidad<br>[m/s] | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Condición | Máx. | Med. | Mín. | Máx. | Med. | Mín. |
| Sin Proyecto | ~~1.240~~ | ~~0.270~~ | ~~0.003~~ | ~~2.188~~ | ~~0.796~~ | ~~0.007~~ |
| Con Proyecto | 0.916 | 0.536 | 0.013 | 0.667 | 0.481 | 0.050 |
| Diferencia(*) | ~~0.324~~ | ~~-0.266~~ | ~~-0.01~~ | ~~1.521~~ | ~~0.315~~ | ~~-0.043~~ |

**Tabla 4-3.: Resultados área de interés aguas arriba de la obra OA 04**

| Condición | Profundidad<br>[m] | Col3 | Col4 | Velocidad<br>[m/s] | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Condición | Máx. | Med. | Mín. | Máx. | Med. | Mín. |
| Sin Proyecto | 0.909 | 0.438 | 0.136 | 3.354 | 1.692 | 0.244 |
| Con Proyecto | 1.104 | 0.660 | 0.019 | 2.877 | 1.730 | 0.072 |
| Diferencia(*) | ~~-0.195~~ | ~~-0.222~~ | ~~0.117~~ | ~~0.477~~ | ~~-0.038~~ | ~~0.172~~ |

**Tabla 4-4.: Resultados área de interés aguas abajo de la obra OA 04**

| Condición | Profundidad<br>[m] | Col3 | Col4 | Velocidad<br>[m/s] | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Condición | Máx. | Med. | Mín. | Máx. | Med. | Mín. |
| Sin Proyecto | ~~0.880~~ | ~~0.418~~ | ~~0.008~~ | ~~1.880~~ | ~~0.781~~ | ~~0.070~~ |
| Con Proyecto | 0.977 | 0.489 | 0.003 | 1.343 | 0.651 | 0.024 |
| Diferencia(*) | ~~-0.097~~ | ~~-0.071~~ | ~~0.005~~ | ~~0.537~~ | ~~0.13~~ | ~~0.046~~ |
