---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: manual
pages: 233
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 2. MODELO HIDRÁULICO PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANDINO
  - para ANDES SOLAR
  - ANEXO 2.01. MODELO HIDRÁULICO OA 01 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANDINO
  - para ANDES SOLAR
  - Contenidos
  - Figuras
  - Tablas
  - Copyright
  - 1. Introducción
  - 2. Descripción del modelo
  ... y 135 secciones más
-->

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# ANEXO 2. MODELO HIDRÁULICO PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANDINO

LONGOTOMA

# para ANDES SOLAR

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# ANEXO 2.01. MODELO HIDRÁULICO OA 01 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANDINO

LONGOTOMA

# para ANDES SOLAR

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|26/10/2023|Revisión cliente|JCP|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comunas de La Ligua y Papudo<br>Región de Valparaíso|Col3|
|---|---|---|
||AND-B23014(2)-PAS156-DOC-02.01-A|Rev. A|

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Contenidos

1. Introducción ............................................................................................................................................. 4

2. Descripción del modelo.......................................................................................................................... 4

3. Parámetros de entrada ......................................................................................................................... 5

3.1. Obra proyectada ................................................................................................................................... 5
3.2. Coeficiente de rugosidad ................................................................................................................... 6
3.3. Condiciones de borde e iniciales ...................................................................................................... 6

3.4. Otras consideraciones......................................................................................................................... 9

4. Resultados ............................................................................................................................................... 9

4.1. Modelo HEC-RAS ............................................................................................................................... 10

4.1.1. Condición sin proyecto ........................................................................................................................... 10

4.1.2. Condición con proyecto .......................................................................................................................... 14

4.2. Modelo OA 01 ...................................................................................................................................... 18

4.2.1. Condición sin proyecto ........................................................................................................................... 18

4.2.2. Condición con proyecto .......................................................................................................................... 20

5. Referencias ............................................................................................................................................ 23

# Figuras

Figura 3-1. Topografía de la zona de estudio de la obra OA 01 y layout (negro). Condición sin proyecto ....... 5

Figura 3-2. Topografía de la zona de estudio de la obra OA 01 y layout (negro). Condición con proyecto ..... 5

Figura 3-3. Ubicación condiciones de borde ................................................................................................................. 7

Figura 3-4. Hidrogramas de entrada. Crecida de diseño (50 años) ......................................................................... 8

Figura 3-5. Hidrogramas de entrada. Crecida de verificación (100 años) ............................................................... 8

Figura 3-5. Hidrogramas de entrada US_03 ................................................................................................................ 9

Figura 4-1. Profundidad máxima. Crecida de diseño (50 años). Condición sin proyecto ................................... 10

Figura 4-2. Velocidad máxima. Crecida de diseño (50 años). Condición sin proyecto .........................................11

Figura 4-3. Profundidad máxima. Crecida de verificación (100 años). Condición sin proyecto ........................ 12

Figura 4-4. Velocidad máxima. Crecida de verificación (100 años). Condición sin proyecto ............................. 13

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto ............................................................... 13

Figura 4-6. Profundidad máxima. Crecida de diseño (50 años). Condición con proyecto................................. 14

Figura 4-7. Velocidad máxima. Crecida de diseño (50 años). Condición con proyecto ....................................... 15

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-8. Profundidad máxima. Crecida de verificación (100 años). Condición con proyecto .......................16

Figura 4-9. Velocidad máxima. Crecida de verificación (100 años). Condición con proyecto ............................ 17

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto ............................................................ 17

Figura 4-1. Profundidad máxima OA 01. Crecida de diseño (50 años). Condición sin proyecto ....................... 18

Figura 4-2. Velocidad máxima OA 01. Crecida de diseño (50 años). Condición sin proyecto ........................... 18

Figura 4-3. Profundidad máxima OA 01. Crecida de verificación (100 años). Condición sin proyecto .............19

Figura 4-4. Velocidad máxima OA 01. Crecida de verificación (100 años). Condición sin proyecto .................19

Figura 4-5. Hidrograma a la salida de la obra. Condición sin proyecto ................................................................. 20

Figura 4-6. Profundidad máxima OA 01. Crecida de diseño (50 años). Condición con proyecto ..................... 20

Figura 4-7. Velocidad máxima OA 01. Crecida de diseño (50 años). Condición con proyecto ........................... 21

Figura 4-8. Profundidad máxima OA 01. Crecida de verificación (100 años). Condición con proyecto ........... 21

Figura 4-9. Velocidad máxima OA 01. Crecida de verificación (100 años). Condición con proyecto ............... 22

Figura 4-10. Hidrograma a la salida de la obra. Condición con proyecto.............................................................. 22

# Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................ 4

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan ....................... 6

Tabla 3-2. Condiciones de borde e iniciales .................................................................................................................. 7

# Copyright

Este documento, sus anexos y planos son de propiedad exclusiva de Baqua Ingeniería y están destinados

únicamente al uso de Andes Solar. La copia, reproducción o divulgación no autorizada de su contenido está

estrictamente prohibida.

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 1. Introducción

Se construyó el modelo hidráulico de la obra de atravieso denominada OA 01, empleando para ello el

software HEC-RAS (2022). El objetivo del modelo es representar la condición actual del cauce, sin proyecto,

y su condición futura, con proyecto, para los caudales de diseño y verificación de la obra.

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados más relevantes de cada caso.

# 2. Descripción del modelo

El modelo se construyó con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La

descripción general de cada modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|Sin Proyecto|Representa la condición actual del cauce, en una extensión total de<br>200 m a lo largo de su eje, manteniendo 50 m hacia aguas arriba desde<br>el inicio de la obra existente, 60 m hacia aguas arriba desde el inicio de<br>la obra proyectada y, al menos, 100 m aguas abajo desde el fin de<br>ambas obras.<br>Este modelo incluye la representación de una obra existente,<br>correspondiente a dos alcantarillas de acero corrugado de diámetro<br>0.6 m y longitud de 11 m.|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|Con Proyecto|Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, además de incorporar la obra proyectada,<br>correspondiente a una alcantarilla de acero corrugado de diámetro 0.5<br>m y longitud de 12.5 m.|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

Nótese que el modelo no abarca una mayor extensión hacia aguas arriba porque las obras se encuentran

cerca de la cabecera de la cuenca y la forma del cauce no se aprecia más allá de los 50 y 60 m,

respectivamente.

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 3. Parámetros de entrada

## 3.1. Obra proyectada

La obra de atravieso se proyectó mediante herramientas de geometría de HEC-RAS y las modificaciones de

terreno de RAS Mapper. A continuación, se muestra el terreno sin y con la obra incorporada.

Figura 3-1. Topografía de la zona de estudio de la obra OA 01 y layout (negro). Condición sin proyecto

Figura 3-2. Topografía de la zona de estudio de la obra OA 01 y layout (negro). Condición con proyecto

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 3.2. Coeficiente de rugosidad

Para el cauce natural, se estimó el coeficiente de rugosidad a partir del método de Cowan (MOP, 2020):

## n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

## n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 3-1 muestra la condición del cauce según los criterios del método

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Alternándose ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.012|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.047|

Para la obra proyectada se asignó un valor de rugosidad igual a 0.024 basado en valores tabulados en la

literatura (Chow, 1994).

## 3.3. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales están asociados a los periodos de retorno de diseño

y verificación de la obra, correspondientes a 50 y 100 años, respectivamente. Un resumen de las CB y su

ubicación se presenta en la Tabla 3-2 y en la Figura 3-3:

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>diseño<br>[m3/s]|Caudal<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅||0.09|0.12|0.45|
|US_01|✅||0.12|0.16|0.13|
|US_02|✅||0.16|0.20|0.04|
|US_03|✅||8.17|10.66|0.07|
|DS||✅|-|-|0.05|

Figura 3-3. Ubicación condiciones de borde

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

Los hidrogramas de entrada utilizados para el modelo se muestran a continuación:

Figura 3-4. Hidrogramas de entrada. Crecida de diseño (50 años)

Figura 3-5. Hidrogramas de entrada. Crecida de verificación (100 años)

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 3-6. Hidrogramas de entrada US_03

## 3.4. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.3). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 40 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

Debido a que el modelo abarca un área muy extensa, se presentan los resultados de este con una

aproximación a la obra OA 01 en la Sección 4.2

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 4.1. Modelo HEC-RAS

### 4.1.1. Condición sin proyecto

Figura 4-1. Profundidad máxima. Crecida de diseño (50 años). Condición sin proyecto

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-2. Velocidad máxima. Crecida de diseño (50 años). Condición sin proyecto

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-3. Profundidad máxima. Crecida de verificación (100 años). Condición sin proyecto

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-4. Velocidad máxima. Crecida de verificación (100 años). Condición sin proyecto

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

### 4.1.2. Condición con proyecto

Figura 4-6. Profundidad máxima. Crecida de diseño (50 años). Condición con proyecto

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-7. Velocidad máxima. Crecida de diseño (50 años). Condición con proyecto

15 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-8. Profundidad máxima. Crecida de verificación (100 años). Condición con proyecto

16 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-9. Velocidad máxima. Crecida de verificación (100 años). Condición con proyecto

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto

17 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 4.2. Modelo OA 01

### 4.2.1. Condición sin proyecto

Figura 4-11. Profundidad máxima OA 01. Crecida de diseño (50 años). Condición sin proyecto

Figura 4-12. Velocidad máxima OA 01. Crecida de diseño (50 años). Condición sin proyecto

18 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-13. Profundidad máxima OA 01. Crecida de verificación (100 años). Condición sin proyecto

Figura 4-14. Velocidad máxima OA 01. Crecida de verificación (100 años). Condición sin proyecto

19 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-15. Hidrograma a la salida de la obra. Condición sin proyecto

### 4.2.2. Condición con proyecto

Figura 4-16. Profundidad máxima OA 01. Crecida de diseño (50 años). Condición con proyecto

20 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-17. Velocidad máxima OA 01. Crecida de diseño (50 años). Condición con proyecto

Figura 4-18. Profundidad máxima OA 01. Crecida de verificación (100 años). Condición con proyecto

21 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-19. Velocidad máxima OA 01. Crecida de verificación (100 años). Condición con proyecto

Figura 4-20. Hidrograma a la salida de la obra. Condición con proyecto

22 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.01. MODELO HIDRÁULICO OA 01

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 5. Referencias

Chow, V. T. (1994). Hidráulica de canales abiertos. Colombia: McGraw-Hill.

Chow, V. T., Maidment, D. R., & Mays, L. W. (1988). Applied hydrology. Singapore: McGraw-Hill.

HEC. (2022). HEC-RAS. Versión 6.3. HEC-RAS. Versión 6.3. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

23 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# ANEXO 2.02 MODELO HIDRÁULICO OA 02 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANDINO

LONGOTOMA

# para ANDES SOLAR

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|26/10/2023|Revisión cliente|CHR|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comunas de La Ligua y Papudo<br>Región de Valparaíso|Col3|
|---|---|---|
||AND-B23014(2)-PAS156-DOC-02.02-A|Rev. A|

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Contenidos

1. Introducción ............................................................................................................................................. 4

2. Descripción del modelo.......................................................................................................................... 4

3. Parámetros de entrada ......................................................................................................................... 4

3.1. Obra proyectada .................................................................................................................................. 4
3.2. Coeficiente de rugosidad .................................................................................................................... 5
3.3. Condiciones de borde e iniciales ...................................................................................................... 6

3.4. Otras consideraciones......................................................................................................................... 8

4. Resultados ............................................................................................................................................... 9

4.1. Condición sin proyecto ....................................................................................................................... 9
4.2. Condición con proyecto ..................................................................................................................... 14

5. Referencias ............................................................................................................................................ 18

# Figuras

Figura 3-1. Topografía de la zona de estudio de la obra OA 02. Condición sin proyecto ..................................... 5

Figura 3-2. Topografía de la zona de estudio de la obra OA 02. Condición con proyecto ................................... 5

Figura 3-3. Ubicación condiciones de borde ................................................................................................................. 7

Figura 3-4. Hidrogramas de entrada ............................................................................................................................. 8

Figura 4-1. Profundidad máxima. Crecida de diseño (50 años). Condición sin proyecto ..................................... 9

Figura 4-2. Velocidad máxima. Crecida de diseño (50 años). Condición sin proyecto ....................................... 10

Figura 4-3. Profundidad máxima. Crecida de verificación (100 años). Condición sin proyecto .........................11

Figura 4-4. Velocidad máxima. Crecida de verificación (100 años). Condición sin proyecto ............................. 12

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto ............................................................... 13

Figura 4-1. Profundidad máxima. Crecida de diseño (50 años). Condición con proyecto ................................. 14

Figura 4-2. Velocidad máxima. Crecida de diseño (50 años). Condición con proyecto ....................................... 15

Figura 4-3. Profundidad máxima. Crecida de verificación (100 años). Condición con proyecto .......................16

Figura 4-4. Velocidad máxima. Crecida de verificación (100 años). Condición con proyecto ............................ 17

Figura 4-5. Hidrograma a la salida del modelo. Condición con proyecto ............................................................. 18

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................ 4

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan ....................... 6

Tabla 3-2. Condiciones de borde e iniciales .................................................................................................................. 7

# Copyright

Este documento, sus anexos y planos son de propiedad exclusiva de Baqua Ingeniería y están destinados

únicamente al uso de Andes Solar. La copia, reproducción o divulgación no autorizada de su contenido está

estrictamente prohibida.

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 1. Introducción

Se construyó el modelo hidráulico de la obra de atravieso denominada OA 02, empleando para ello el

software HEC-RAS (2022). El objetivo del modelo es representar la condición actual del cauce, sin proyecto,

y su condición futura, con proyecto, para los caudales de diseño y verificación de la obra.

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados más relevantes de cada caso.

# 2. Descripción del modelo

El modelo se construyó con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La

descripción general de cada modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|Sin Proyecto|Representa la condición actual del cauce, en una extensión total de<br>282.8 m a lo largo de su eje, centrado en la obra proyectada y<br>manteniendo más de 60.5 m hacia aguas arriba y 206.2 m aguas abajo<br>desde el inicio y fin de la obra.|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|Con Proyecto|Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, además de incorporar la obra proyectada,<br>correspondiente a una alcantarilla de acero corrugado de diámetro 0.5<br>m y longitud de 16.3 m.|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

Nótese que el modelo no abarca una mayor extensión hacia aguas arriba porque la obra se encuentra cerca

de la cabecera de la cuenca y la forma del cauce no se aprecia más allá de los 60.5 m.

# 3. Parámetros de entrada

## 3.1. Obra proyectada

La obra de atravieso se proyectó mediante herramientas de geometría de HEC-RAS y las modificaciones de

terreno de RAS Mapper. A continuación, se muestra el terreno sin y con la obra incorporada.

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 3-1. Topografía de la zona de estudio de la obra OA 02. Condición sin proyecto

Figura 3-2. Topografía de la zona de estudio de la obra OA 02. Condición con proyecto

## 3.2. Coeficiente de rugosidad

Para el cauce natural, se estimó el coeficiente de rugosidad a partir del método de Cowan (MOP, 2020):

## n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

## n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 3-1 muestra la condición del cauce según los criterios del método

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Alternándose ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.010|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.045|

Para la obra proyectada se asignó un valor de rugosidad igual a 0.024 basado en valores tabulados en la

literatura (Chow, 1994).

## 3.3. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales están asociados a los periodos de retorno de diseño

y verificación de la obra, correspondientes a 50 y 100 años, respectivamente. Un resumen de las CB y su

ubicación se presenta en la Tabla 3-2 y en la Figura 3-3:

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>diseño<br>[m3/s]|Caudal<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅||0.076|0.087|0.12|
|DS||✅|-|-|0.03|

Figura 3-3. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

Los hidrogramas de entrada utilizados para el modelo se muestran a continuación:

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 3-4. Hidrogramas de entrada

## 3.4. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.3). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 40 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo

## 4.1. Condición sin proyecto

Figura 4-1. Profundidad máxima. Crecida de diseño (50 años). Condición sin proyecto

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-2. Velocidad máxima. Crecida de diseño (50 años). Condición sin proyecto

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-3. Profundidad máxima. Crecida de verificación (100 años). Condición sin proyecto

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-4. Velocidad máxima. Crecida de verificación (100 años). Condición sin proyecto

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 4.2. Condición con proyecto

Figura 4-6. Profundidad máxima. Crecida de diseño (50 años). Condición con proyecto

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-7. Velocidad máxima. Crecida de diseño (50 años). Condición con proyecto

15 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-8. Profundidad máxima. Crecida de verificación (100 años). Condición con proyecto

16 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-9. Velocidad máxima. Crecida de verificación (100 años). Condición con proyecto

17 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.02 MODELO HIDRÁULICO OA 02

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto

# 5. Referencias

Chow, V. T. (1994). Hidráulica de canales abiertos. Colombia: McGraw-Hill.

Chow, V. T., Maidment, D. R., & Mays, L. W. (1988). Applied hydrology. Singapore: McGraw-Hill.

HEC. (2022). HEC-RAS. Versión 6.3. HEC-RAS. Versión 6.3. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

18 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# ANEXO 2.03 MODELO HIDRÁULICO OA 03 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANDINO

LONGOTOMA

# para ANDES SOLAR

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|26/10/2023|Revisión cliente|JCP|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comunas de La Ligua y Papudo<br>Región de Valparaíso|Col3|
|---|---|---|
||AND-B23014(2)-PAS156-DOC-02.03-A|Rev. A|

ANEXO 2.03 MODELO HIDRÁULICO OA 03

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Contenidos

1. Introducción ............................................................................................................................................. 4

2. Descripción del modelo.......................................................................................................................... 4

3. Parámetros de entrada ......................................................................................................................... 5

3.1. Obra proyectada ................................................................................................................................... 5
3.2. Coeficiente de rugosidad ................................................................................................................... 6
3.3. Condiciones de borde e iniciales ....................................................................................................... 7

3.4. Otras consideraciones......................................................................................................................... 8

4. Resultados ............................................................................................................................................... 9

4.1. Condición sin proyecto ....................................................................................................................... 9
4.2. Condición con proyecto ..................................................................................................................... 12

5. Referencias .............................................................................................................................................14

# Figuras

Figura 3-1. Topografía de la zona de estudio de la obra OA 03 y layout (negro). Condición sin proyecto ...... 5

Figura 3-2. Topografía de la zona de estudio de la obra OA 03 y layout (negro). Condición con proyecto .... 5

Figura 3-3. Ubicación condiciones de borde ................................................................................................................. 7

Figura 3-4. Hidrogramas de entrada ............................................................................................................................. 8

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto ................................... 9

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto ..................................... 10

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición sin proyecto ........................ 10

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición sin proyecto ..............................11

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto ................................................................11

Figura 4-6. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto ................................ 12

Figura 4-7. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto ..................................... 12

Figura 4-8. Profundidad máxima. Crecida de verificación (150 años). Condición con proyecto ....................... 13

Figura 4-9. Velocidad máxima. Crecida de verificación (150 años). Condición con proyecto ............................ 13

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto ........................................................... 14

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.03 MODELO HIDRÁULICO OA 03

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................ 4

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan ....................... 6

Tabla 3-2. Condiciones de borde e iniciales .................................................................................................................. 7

# Copyright

Este documento, sus anexos y planos son de propiedad exclusiva de Baqua Ingeniería y están destinados

únicamente al uso de Andes Solar. La copia, reproducción o divulgación no autorizada de su contenido está

estrictamente prohibida.

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.03 MODELO HIDRÁULICO OA 03

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 1. Introducción

Se construyó el modelo hidráulico de la obra de atravieso denominada OA 03, empleando para ello el

software HEC-RAS (2022). El objetivo del modelo es representar la condición actual del cauce, sin proyecto,

y su condición futura, con proyecto, para los caudales de diseño y verificación de la obra.

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados más relevantes de cada caso.

# 2. Descripción del modelo

El modelo se construyó con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La

descripción general de cada modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|Sin Proyecto|Representa la condición actual del cauce, en una extensión total de<br>290 m a lo largo de su eje, centrado en la obra proyectada y<br>manteniendo más de 140 m hacia aguas arriba y aguas abajo desde el<br>inicio y fin de la obra.<br>|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|Con Proyecto|Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, además de incorporar la obra proyectada,<br>correspondiente a un badén de mampostería de piedra con ancho<br>basal de 2 m, altura de 0.4 m, talud de 10:1 (H:V) y longitud de 13 m<br>(medida en el sentido del cauce). Posterior al badén, se incorporó un<br>disipador de energía de impacto, compuesto por: (i) Un canal de ancho<br>de 1 m, altura de 0.4 m y longitud de 7 m. A lo largo del tramo presenta<br>diferentes pendientes, los primeros 5 m posee una de 3:2 (H:V) y los<br>últimos 2 m una de 3:1 (H:V); y (ii) Un foso rectangular ubicado al final<br>del canal, cuya longitud es de 3 m, ancho 1 m y profundidad 0.3 m.|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.03 MODELO HIDRÁULICO OA 03

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 3. Parámetros de entrada

## 3.1. Obra proyectada

La obra de atravieso se proyectó mediante herramientas de geometría de HEC-RAS y las modificaciones de

terreno de RAS Mapper. A continuación, se muestra el terreno sin y con la obra incorporada.

Figura 3-1. Topografía de la zona de estudio de la obra OA 03 y layout (negro). Condición sin proyecto

Figura 3-2. Topografía de la zona de estudio de la obra OA 03 y layout (negro). Condición con proyecto

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.03 MODELO HIDRÁULICO OA 03

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 3.2. Coeficiente de rugosidad

Para el cauce natural, se estimó el coeficiente de rugosidad a partir del método de Cowan (MOP, 2020):

## n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

## n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 3-1 muestra la condición del cauce según los criterios del método

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Alternándose ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Baja|n4|0.010|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.045|

Para el badén se asignó un valor de rugosidad igual a 0.025, y para el disipador de energía un valor de 0.014

basado en valores tabulados en la literatura (Chow, 1994).

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.03 MODELO HIDRÁULICO OA 03

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 3.3. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales están asociados a los periodos de retorno de diseño

y verificación de la obra, correspondientes a 100 y 150 años, respectivamente. Un resumen de las CB y su

ubicación se presenta en la Tabla 3-2 y en la Figura 3-3:

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>diseño<br>[m3/s]|Caudal<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US|✅||0.09|0.12|0.09|
|DS||✅|-|-|0.05|

Figura 3-3. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.03 MODELO HIDRÁULICO OA 03

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

Los hidrogramas de entrada utilizados para el modelo se muestran a continuación:

Figura 3-4. Hidrogramas de entrada

## 3.4. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.3). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 40 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

Adicionalmente, se consideró el refinamiento de la malla de cálculo a celdas de 0.5 x 0.5 m, en las zonas que

se muestran en la Figura 3-3 (con color rojo). El objetivo de estos refinamientos es representar de mejor

forma las características de la obra proyectada y solucionar algunas inestabilidades numéricas del modelo.

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.03 MODELO HIDRÁULICO OA 03

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo

## 4.1. Condición sin proyecto

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.03 MODELO HIDRÁULICO OA 03

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición sin proyecto

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.03 MODELO HIDRÁULICO OA 03

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición sin proyecto

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.03 MODELO HIDRÁULICO OA 03

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 4.2. Condición con proyecto

Figura 4-6. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto

Figura 4-7. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.03 MODELO HIDRÁULICO OA 03

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-8. Profundidad máxima. Crecida de verificación (150 años). Condición con proyecto

Figura 4-9. Velocidad máxima. Crecida de verificación (150 años). Condición con proyecto

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.03 MODELO HIDRÁULICO OA 03

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto

# 5. Referencias

Chow, V. T. (1994). Hidráulica de canales abiertos. Colombia: McGraw-Hill.

Chow, V. T., Maidment, D. R., & Mays, L. W. (1988). Applied hydrology. Singapore: McGraw-Hill.

HEC. (2022). HEC-RAS. Versión 6.3. HEC-RAS. Versión 6.3. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# ANEXO 2.04. MODELO HIDRÁULICO OA 04 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANDINO

LONGOTOMA

# para ANDES SOLAR

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|26/10/2023|Revisión cliente|IDC|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comunas de La Ligua y Papudo<br>Región de Valparaíso|Col3|
|---|---|---|
||AND-B23014(2)-PAS156-DOC-02.04-A|Rev. A|

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Contenidos

1. Introducción ............................................................................................................................................. 4

2. Descripción del modelo.......................................................................................................................... 4

3. Parámetros de entrada ......................................................................................................................... 4

3.1. Obra proyectada .................................................................................................................................. 4
3.2. Coeficiente de rugosidad .................................................................................................................... 5
3.3. Condiciones de borde e iniciales ...................................................................................................... 6

3.4. Otras consideraciones......................................................................................................................... 8

4. Resultados ............................................................................................................................................... 8

4.1. Condición sin proyecto ....................................................................................................................... 9
4.2. Condición con proyecto ..................................................................................................................... 13

5. Referencias ............................................................................................................................................. 17

# Figuras

Figura 3-1. Topografía de la zona de estudio de la obra OA 04. Condición sin proyecto .................................... 5

Figura 3-2. Topografía de la zona de estudio de la obra OA 04. Condición con proyecto .................................. 5

Figura 3-3. Ubicación condiciones de borde ................................................................................................................. 7

Figura 3-4. Hidrogramas de entrada ............................................................................................................................. 8

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto ................................... 9

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto ..................................... 10

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición sin proyecto ..........................11

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición sin proyecto ............................. 12

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto ............................................................... 12

Figura 4-6. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto ................................ 13

Figura 4-7. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto .................................... 14

Figura 4-8. Profundidad máxima. Crecida de verificación (150 años). Condición con proyecto ....................... 15

Figura 4-9. Velocidad máxima. Crecida de verificación (150 años). Condición con proyecto ............................16

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto ............................................................16

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................ 4

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan ....................... 6

Tabla 3-2. Condiciones de borde e iniciales .................................................................................................................. 7

# Copyright

Este documento, sus anexos y planos son de propiedad exclusiva de Baqua Ingeniería y están destinados

únicamente al uso de Andes Solar. La copia, reproducción o divulgación no autorizada de su contenido está

estrictamente prohibida.

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 1. Introducción

Se construyó el modelo hidráulico de la obra de atravieso denominada OA 04, empleando para ello el

software HEC-RAS (2022). El objetivo del modelo es representar la condición actual del cauce, sin proyecto,

y su condición futura, con proyecto, para los caudales de diseño y verificación de la obra.

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados más relevantes de cada caso.

# 2. Descripción del modelo

El modelo se construyó con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La

descripción general de cada modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|Sin Proyecto|Representa la condición actual del cauce, en una extensión total de 210<br>m a lo largo de su eje, centrado en la obra proyectada y manteniendo<br>más de 43.7 m hacia aguas arriba y 148.6 m hacia aguas abajo, desde<br>el inicio y fin de la obra.|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|Con Proyecto|Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, además de incorporar la obra proyectada,<br>correspondiente a un badén de mampostería de piedra con base de 1<br>m, altura de 0.3 m, talud de 10:1 (H:V) y longitud de 11.5 m (medida en<br>el sentido del cauce).|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

Nótese que el modelo no abarca una mayor extensión hacia aguas arriba porque la obra se encuentra cerca

de la cabecera de la cuenca y la forma del cauce no se aprecia más allá de los 43.7 m.

# 3. Parámetros de entrada

## 3.1. Obra proyectada

La obra de atravieso se proyectó mediante herramientas de geometría de HEC-RAS y las modificaciones de

terreno de RAS Mapper. A continuación, se muestra el terreno sin y con la obra incorporada.

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 3-1. Topografía de la zona de estudio de la obra OA 04. Condición sin proyecto

Figura 3-2. Topografía de la zona de estudio de la obra OA 04. Condición con proyecto

## 3.2. Coeficiente de rugosidad

Para el cauce natural, se estimó el coeficiente de rugosidad a partir del método de Cowan (MOP, 2020):

## n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

## n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 3-1 muestra la condición del cauce según los criterios del método

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Alternándose<br>ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Baja|n4|0.010|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.045|

Para la obra proyectada se asignó un valor de rugosidad igual a 0.025 basado en valores tabulados en la

literatura (Chow, 1994).

## 3.3. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales están asociados a los periodos de retorno de diseño

y verificación de la obra, correspondientes a 100 y 150 años, respectivamente. Un resumen de las CB y su

ubicación se presenta en la Tabla 3-2 y en la Figura 3-3:

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>diseño<br>[m3/s]|Caudal<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅||0.040|0.044|0.080|
|DS||✅|-|-|0.081|

Figura 3-3. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

Los hidrogramas de entrada utilizados para el modelo se muestran a continuación:

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 3-4. Hidrogramas de entrada

## 3.4. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.3). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 2 horas para que el flujo entrara en régimen

permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie inundada.

Adicionalmente, se consideró el refinamiento de la malla de cálculo a celdas de 0.5 x 0.5 m, en las zonas que

se muestran en la Figura 3-3 (con color rojo). El objetivo de estos refinamientos es representar de mejor

forma las características de la obra proyectada y solucionar algunas inestabilidades numéricas del modelo.

# 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 4.1. Condición sin proyecto

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición sin proyecto

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición sin proyecto

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 4.2. Condición con proyecto

Figura 4-6. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-7. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-8. Profundidad máxima. Crecida de verificación (150 años). Condición con proyecto

15 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-9. Velocidad máxima. Crecida de verificación (150 años). Condición con proyecto

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto

16 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.04. MODELO HIDRÁULICO OA 04

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 5. Referencias

Chow, V. T. (1994). Hidráulica de canales abiertos. Colombia: McGraw-Hill.

Chow, V. T., Maidment, D. R., & Mays, L. W. (1988). Applied hydrology. Singapore: McGraw-Hill.

HEC. (2022). HEC-RAS. Versión 6.3. HEC-RAS. Versión 6.3. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

17 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# ANEXO 2.05 MODELO HIDRÁULICO OA 05 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANDINO

LONGOTOMA

# para ANDES SOLAR

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|26/10/2023|Revisión cliente|CHR|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comunas de La Ligua y Papudo<br>Región de Valparaíso|Col3|
|---|---|---|
||AND-B23014(2)-PAS156-DOC-02.05-A|Rev. A|

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Contenidos

1. Introducción ............................................................................................................................................. 4

2. Descripción del modelo.......................................................................................................................... 4

3. Parámetros de entrada ......................................................................................................................... 5

3.1. Obra proyectada ................................................................................................................................... 5
3.2. Coeficiente de rugosidad ................................................................................................................... 6
3.3. Condiciones de borde e iniciales ...................................................................................................... 6

3.4. Otras consideraciones......................................................................................................................... 8

4. Resultados ............................................................................................................................................... 9

4.1. Condición sin proyecto ....................................................................................................................... 9
4.2. Condición con proyecto ..................................................................................................................... 13

5. Referencias ............................................................................................................................................. 17

# Figuras

Figura 3-1. Topografía de la zona de estudio de la obra OA 05. Condición sin proyecto .................................... 5

Figura 3-2. Topografía de la zona de estudio de la obra OA 05. Condición con proyecto ................................... 5

Figura 3-3. Ubicación condiciones de borde ................................................................................................................. 7

Figura 3-4. Hidrogramas de entrada ............................................................................................................................. 8

Figura 4-1. Profundidad máxima. Crecida de diseño (50 años). Condición sin proyecto ..................................... 9

Figura 4-2. Velocidad máxima. Crecida de diseño (50 años). Condición sin proyecto ....................................... 10

Figura 4-3. Profundidad máxima. Crecida de verificación (100 años). Condición sin proyecto .........................11

Figura 4-4. Velocidad máxima. Crecida de verificación (100 años). Condición sin proyecto ............................. 12

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto ............................................................... 12

Figura 4-1. Profundidad máxima. Crecida de diseño (50 años). Condición con proyecto .................................. 13

Figura 4-2. Velocidad máxima. Crecida de diseño (50 años). Condición con proyecto ...................................... 14

Figura 4-3. Profundidad máxima. Crecida de verificación (100 años). Condición con proyecto ....................... 15

Figura 4-4. Velocidad máxima. Crecida de verificación (100 años). Condición con proyecto ............................16

Figura 4-5. Hidrograma a la salida del modelo. Condición con proyecto ..............................................................16

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................ 4

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan ....................... 6

Tabla 3-2. Condiciones de borde e iniciales .................................................................................................................. 7

# Copyright

Este documento, sus anexos y planos son de propiedad exclusiva de Baqua Ingeniería y están destinados

únicamente al uso de Andes Solar. La copia, reproducción o divulgación no autorizada de su contenido está

estrictamente prohibida.

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 1. Introducción

Se construyó el modelo hidráulico de la obra de atravieso denominada OA 05, empleando para ello el

software HEC-RAS (2022). El objetivo del modelo es representar la condición actual del cauce, sin proyecto,

y su condición futura, con proyecto, para los caudales de diseño y verificación de la obra.

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados más relevantes de cada caso.

# 2. Descripción del modelo

El modelo se construyó con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La

descripción general de cada modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|Sin Proyecto|Representa la condición actual del cauce, en una extensión total de<br>240.2 m a lo largo de su eje, centrado en la obra proyectada y<br>manteniendo más de 87 m hacia aguas arriba y 126.8 m aguas abajo<br>desde el inicio y fin de la obra.<br> <br>Este modelo incluye la representación de una obra existente,<br>correspondiente a una alcantarilla de hormigón de diámetro 0.6 m y<br>longitud aproximada de 10.3 m.<br>|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|Con Proyecto|Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, además de incorporar la obra proyectada,<br>correspondiente a una alcantarilla compuesta por 1 cajón de hormigón<br>de sección 1.5 x 1.5 m y longitud de 20 m..|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

Nótese que el modelo no abarca una extensión superior a 87 m hacia aguas arriba de la obra, debido a que

el cauce se encuentra intervenido por un embalse.

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 3. Parámetros de entrada

## 3.1. Obra proyectada

La obra de atravieso se proyectó mediante herramientas de geometría de HEC-RAS y las modificaciones de

terreno de RAS Mapper. A continuación, se muestra el terreno sin y con la obra incorporada.

Figura 3-1. Topografía de la zona de estudio de la obra OA 05. Condición sin proyecto

Figura 3-2. Topografía de la zona de estudio de la obra OA 05. Condición con proyecto

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 3.2. Coeficiente de rugosidad

Para el cauce natural, se estimó el coeficiente de rugosidad a partir del método de Cowan (MOP, 2020):

## n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

## n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 3-1 muestra la condición del cauce según los criterios del método

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Alternándose ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Baja|n4|0.010|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.045|

Para la obra proyectada se asignó un valor de rugosidad igual a 0.014 basado en valores tabulados en la

literatura (Chow, 1994).

## 3.3. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales están asociados a los periodos de retorno de diseño

y verificación de la obra, correspondientes a 50 y 100 años, respectivamente. Un resumen de las CB y su

ubicación se presenta en la Tabla 3-2 y en la Figura 3-3:

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>diseño<br>[m3/s]|Caudal<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅||1.79|2.33|0.057|
|DS||✅|-|-|0.022|

Figura 3-3. Ubicación condiciones de borde

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

Los hidrogramas de entrada utilizados para el modelo se muestran a continuación:

Figura 3-4. Hidrogramas de entrada

## 3.4. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.3). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 2 horas y 10 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo

## 4.1. Condición sin proyecto

Figura 4-1. Profundidad máxima. Crecida de diseño (50 años). Condición sin proyecto

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-2. Velocidad máxima. Crecida de diseño (50 años). Condición sin proyecto

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-3. Profundidad máxima. Crecida de verificación (100 años). Condición sin proyecto

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-4. Velocidad máxima. Crecida de verificación (100 años). Condición sin proyecto

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 4.2. Condición con proyecto

Figura 4-6. Profundidad máxima. Crecida de diseño (50 años). Condición con proyecto

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-7. Velocidad máxima. Crecida de diseño (50 años). Condición con proyecto

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-8. Profundidad máxima. Crecida de verificación (100 años). Condición con proyecto

15 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-9. Velocidad máxima. Crecida de verificación (100 años). Condición con proyecto

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto

16 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.05 MODELO HIDRÁULICO OA 05

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 5. Referencias

Chow, V. T. (1994). Hidráulica de canales abiertos. Colombia: McGraw-Hill.

Chow, V. T., Maidment, D. R., & Mays, L. W. (1988). Applied hydrology. Singapore: McGraw-Hill.

HEC. (2022). HEC-RAS. Versión 6.3. HEC-RAS. Versión 6.3. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

17 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# ANEXO 2.06. MODELO HIDRÁULICO OA 06 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANDINO

LONGOTOMA

# para ANDES SOLAR

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|26/10/2023|Revisión cliente|IDC|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comunas de La Ligua y Papudo<br>Región de Valparaíso|Col3|
|---|---|---|
||AND-B23014(2)-PAS156-DOC-02.06-A|Rev. A|

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Contenidos

1. Introducción ............................................................................................................................................. 4

2. Descripción del modelo.......................................................................................................................... 4

3. Parámetros de entrada ......................................................................................................................... 5

3.1. Obra proyectada ................................................................................................................................... 5
3.2. Coeficiente de rugosidad ................................................................................................................... 6
3.3. Condiciones de borde e iniciales ....................................................................................................... 7

3.4. Otras consideraciones........................................................................................................................ 10

4. Resultados ............................................................................................................................................. 10

4.1. Condición (i) Sin Proyecto A............................................................................................................. 10
4.2. Condición (ii) Sin Proyecto................................................................................................................ 13
4.3. Condición (iii) Con Proyecto ............................................................................................................. 16

5. Referencias ............................................................................................................................................. 19

# Figuras

Figura 3-1. Topografía de la zona de estudio de la obra OA 06. Condición (i) Sin Proyecto A ........................... 5

Figura 3-2. Topografía de la zona de estudio de la obra OA 06. Condición (ii) Sin Proyecto B ......................... 6

Figura 3-3. Topografía de la zona de estudio de la obra OA 06. Condición (iii) Con Proyecto ........................... 6

Figura 3-4. Ubicación condiciones de borde ................................................................................................................ 8

Figura 3-5. Hidrogramas de entrada US_00 ............................................................................................................... 9

Figura 3-6. Hidrogramas de entrada US_01 ................................................................................................................ 9

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición (i) Sin Proyecto A........................ 10

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición (i) Sin Proyecto A ..............................11

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición (i) Sin Proyecto A .................11

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición (i) Sin Proyecto A .................... 12

Figura 4-5. Hidrograma a la salida del modelo. Condición (i) Sin Proyecto A ...................................................... 12

Figura 4-6. Profundidad máxima. Crecida de diseño (100 años). Condición (ii) Sin Proyecto B ....................... 13

Figura 4-7. Velocidad máxima. Crecida de diseño (100 años). Condición (ii) Sin Proyecto B ........................... 14

Figura 4-8. Profundidad máxima. Crecida de verificación (150 años). Condición (ii) Sin Proyecto B ............. 14

Figura 4-9. Velocidad máxima. Crecida de verificación (150 años). Condición (ii) Sin Proyecto B ................... 15

Figura 4-10. Hidrograma a la salida del modelo. Condición (ii) Sin Proyecto B ................................................... 15

Figura 4-11. Profundidad máxima. Crecida de diseño (100 años). Condición (iii) Con Proyecto........................16

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-12. Velocidad máxima. Crecida de diseño (100 años). Condición (iii) Con Proyecto ............................ 17

Figura 4-13. Profundidad máxima. Crecida de verificación (150 años). Condición (iii) Con Proyecto............... 17

Figura 4-14. Velocidad máxima. Crecida de verificación (150 años). Condición (iii) Con Proyecto .................. 18

Figura 4-15. Hidrograma a la salida del modelo. Condición con proyecto ............................................................ 18

# Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................ 4

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan ....................... 7

Tabla 3-2. Condiciones de borde e iniciales .................................................................................................................. 8

# Copyright

Este documento, sus anexos y planos son de propiedad exclusiva de Baqua Ingeniería y están destinados

únicamente al uso de Andes Solar. La copia, reproducción o divulgación no autorizada de su contenido está

estrictamente prohibida.

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 1. Introducción

Se construyó el modelo hidráulico de la obra de atravieso denominada OA 06, empleando para ello el

software HEC-RAS (2022). El objetivo del modelo es representar la condición actual del cauce, sin proyecto,

y su condición futura, con proyecto, para los caudales de diseño y verificación de la obra.

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados más relevantes de cada caso.

# 2. Descripción del modelo

La particularidad de este modelo es que, a diferencia del resto de las obras asociadas al Proyecto Parque

Fotovoltaico Andino Longotoma, se modelaron tres escenarios: (i) Sin proyecto representando la condición

actual del cauce, el cual cuenta con la presencia de un embalse de baja envergadura construido con un muro

de tierra, (ii) Sin proyecto removiendo la estructura del embalse y (iii) Con proyecto. El modelo se construyó

con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La descripción general de cada

modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|(i) Sin Proyecto A|Representa la condición actual del cauce, en una extensión total de<br>338 m a lo largo de su eje, centrado en la obra proyectada y<br>manteniendo más de 151 m hacia aguas arriba y aguas abajo desde<br>el inicio y fin de la obra.<br> <br>Este modelo incluye la representación de dos obras existentes: (a)<br>Un embalse con un muro de tierra de altura 0.65 m<br>aproximadamente y longitud de 50 m medida en el eje de la obra. Y<br>(b) una alcantarilla de hormigón con diámetro 0.6 m y longitud<br>aproximada de 12 m.|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|(ii) Sin proyecto B|Representa el cauce actual, removiendo el muro de embalse<br>existente y manteniendo la extensión de la condición (i) Sin Proyecto<br>A.|Representar<br>la<br>condición<br>actual<br>del<br>cauce sin el embalse|
|(iii) Con Proyecto|Representa la condición futura del cauce. Mantiene las<br>características del modelo (ii) Sin Proyecto B, además de incorporar<br>la obra proyectada, correspondiente a un badén de mampostería de|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

|Condición|Descripción|Objetivo|
|---|---|---|
||piedra con base de 3 m, altura de 0.5 m, talud de 10:1 (H:V) y longitud<br>de 11.7 m (medida en el sentido del cauce).||

# 3. Parámetros de entrada

## 3.1. Obra proyectada

La obra de atravieso se proyectó mediante herramientas de geometría de HEC-RAS y las modificaciones de

terreno de RAS Mapper. A continuación, se muestra el terreno sin y con la obra incorporada.

Figura 3-1. Topografía de la zona de estudio de la obra OA 06. Condición (i) Sin Proyecto A

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 3-2. Topografía de la zona de estudio de la obra OA 06. Condición (ii) Sin Proyecto B

Figura 3-3. Topografía de la zona de estudio de la obra OA 06. Condición (iii) Con Proyecto

## 3.2. Coeficiente de rugosidad

Para el cauce natural, se estimó el coeficiente de rugosidad a partir del método de Cowan (MOP, 2020):

## n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

## n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 3-1 muestra la condición del cauce según los criterios del método

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Alternándose<br>ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Baja|n4|0.010|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.045|

Para la obra proyectada se asignó un valor de rugosidad igual a 0.025 basado en valores tabulados en la

literatura (Chow, 1994).

## 3.3. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales están asociados a los periodos de retorno de diseño

y verificación de la obra, correspondientes a 100 y 150 años, respectivamente. Un resumen de las CB y su

ubicación se presenta en la Tabla 3-2 y en la Figura 3-4:

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Cabe mencionar que, tal como se describe en el Análisis Hidrológico, la cuenca que determina el caudal

asociado a la OA 06 tiene como punto de cierre la ubicación de la obra. Sin embargo, al revisar la topografía

se visualizan dos cauces tributarios de similares características. Con el fin de simplificar el modelo hidráulico,

los caudales obtenidos del Análisis Hidrológico (0.97 m [3] /s de diseño y 1.11 m [3] /s de verificación) se dividieron

en partes iguales y fueron asignados a dos CB iniciales aguas arriba de la obra, de este modo se asegura que

los caudales que atraviesan la OA 06 corresponden a los obtenidos a partir del Análisis Hidrológico para el

diseño y verificación de la obra.

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>diseño<br>[m3/s]|Caudal<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅||0.485|0.555|0.52|
|US_01|✅||0.485|0.555|0.04|
|DS||✅|-|-|0.04|

Figura 3-4. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

Los hidrogramas de entrada utilizados para el modelo se muestran a continuación:

Figura 3-5. Hidrogramas de entrada US_00

Figura 3-6. Hidrogramas de entrada US_01

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 3.4. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.3). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 50 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo

## 4.1. Condición (i) Sin Proyecto A

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición (i) Sin Proyecto A

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición (i) Sin Proyecto A

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición (i) Sin Proyecto A

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición (i) Sin Proyecto A

Figura 4-5. Hidrograma a la salida del modelo. Condición (i) Sin Proyecto A

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 4.2. Condición (ii) Sin Proyecto

Figura 4-6. Profundidad máxima. Crecida de diseño (100 años). Condición (ii) Sin Proyecto B

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-7. Velocidad máxima. Crecida de diseño (100 años). Condición (ii) Sin Proyecto B

Figura 4-8. Profundidad máxima. Crecida de verificación (150 años). Condición (ii) Sin Proyecto B

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-9. Velocidad máxima. Crecida de verificación (150 años). Condición (ii) Sin Proyecto B

Figura 4-10. Hidrograma a la salida del modelo. Condición (ii) Sin Proyecto B

15 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 4.3. Condición (iii) Con Proyecto

Figura 4-11. Profundidad máxima. Crecida de diseño (100 años). Condición (iii) Con Proyecto

16 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-12. Velocidad máxima. Crecida de diseño (100 años). Condición (iii) Con Proyecto

Figura 4-13. Profundidad máxima. Crecida de verificación (150 años). Condición (iii) Con Proyecto

17 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-14. Velocidad máxima. Crecida de verificación (150 años). Condición (iii) Con Proyecto

Figura 4-15. Hidrograma a la salida del modelo. Condición con proyecto

18 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.06. MODELO HIDRÁULICO OA 06

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 5. Referencias

Chow, V. T. (1994). Hidráulica de canales abiertos. Colombia: McGraw-Hill.

Chow, V. T., Maidment, D. R., & Mays, L. W. (1988). Applied hydrology. Singapore: McGraw-Hill.

HEC. (2022). HEC-RAS. Versión 6.3. HEC-RAS. Versión 6.3. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

19 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# ANEXO 2.07. MODELO HIDRÁULICO OA 07 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANDINO

LONGOTOMA

# para ANDES SOLAR

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|26/10/2023|Revisión cliente|IDC|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comunas de La Ligua y Papudo<br>Región de Valparaíso|Col3|
|---|---|---|
||AND-B23014(2)-PAS156-DOC-02.07-A|Rev. A|

ANEXO 2.07. MODELO HIDRÁULICO OA 07

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Contenidos

1. Introducción ............................................................................................................................................. 4

2. Descripción del modelo.......................................................................................................................... 4

3. Parámetros de entrada ......................................................................................................................... 5

3.1. Obra proyectada ................................................................................................................................... 5
3.2. Coeficiente de rugosidad ................................................................................................................... 6
3.3. Condiciones de borde e iniciales ...................................................................................................... 6

3.4. Otras consideraciones......................................................................................................................... 8

4. Resultados ............................................................................................................................................... 9

4.1. Condición sin proyecto ....................................................................................................................... 9
4.2. Condición con proyecto ..................................................................................................................... 12

5. Referencias .............................................................................................................................................14

# Figuras

Figura 3-1. Topografía de la zona de estudio de la obra OA 07. Condición sin proyecto ..................................... 5

Figura 3-2. Topografía de la zona de estudio de la obra OA 07. Condición con proyecto ................................... 5

Figura 3-3. Ubicación condiciones de borde ................................................................................................................. 7

Figura 3-4. Hidrogramas de entrada ............................................................................................................................. 8

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto ................................... 9

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto ..................................... 10

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición sin proyecto ........................ 10

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición sin proyecto ..............................11

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto ................................................................11

Figura 4-6. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto ................................ 12

Figura 4-7. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto ..................................... 12

Figura 4-8. Profundidad máxima. Crecida de verificación (150 años). Condición con proyecto ....................... 13

Figura 4-9. Velocidad máxima. Crecida de verificación (150 años). Condición con proyecto ............................ 13

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto ........................................................... 14

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.07. MODELO HIDRÁULICO OA 07

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................ 4

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan ....................... 6

Tabla 3-2. Condiciones de borde e iniciales .................................................................................................................. 7

# Copyright

Este documento, sus anexos y planos son de propiedad exclusiva de Baqua Ingeniería y están destinados

únicamente al uso de Andes Solar. La copia, reproducción o divulgación no autorizada de su contenido está

estrictamente prohibida.

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.07. MODELO HIDRÁULICO OA 07

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 1. Introducción

Se construyó el modelo hidráulico de la obra de atravieso denominada OA 07, empleando para ello el

software HEC-RAS (2022). El objetivo del modelo es representar la condición actual del cauce, sin proyecto,

y su condición futura, con proyecto, para los caudales de diseño y verificación de la obra.

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados más relevantes de cada caso.

# 2. Descripción del modelo

El modelo se construyó con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La

descripción general de cada modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|Sin Proyecto|Representa la condición actual del cauce, en una extensión total de 275<br>m a lo largo de su eje, centrado en la obra proyectada y manteniendo<br>más de 121.9 m hacia aguas arriba y aguas abajo desde el inicio y fin de<br>la obra.<br> <br>Este modelo incluye la representación de una obra existente,<br>correspondiente a dos alcantarillas de hormigón de diámetro 0.6 m y<br>longitud aproximada de 11 m.|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|Con Proyecto|Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, además de incorporar la obra proyectada,<br>correspondiente a un badén de mampostería de piedra de sección<br>variable con base mínima y máxima respectiva de 13.3 y 20.9 m, altura<br>de 0.7 m, talud de 10:1 (H:V) y longitud de 10.2 m (medida en el sentido<br>del cauce).|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.07. MODELO HIDRÁULICO OA 07

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 3. Parámetros de entrada

## 3.1. Obra proyectada

La obra de atravieso se proyectó mediante herramientas de geometría de HEC-RAS y las modificaciones de

terreno de RAS Mapper. A continuación, se muestra el terreno sin y con la obra incorporada.

Figura 3-1. Topografía de la zona de estudio de la obra OA 07. Condición sin proyecto

Figura 3-2. Topografía de la zona de estudio de la obra OA 07. Condición con proyecto

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.07. MODELO HIDRÁULICO OA 07

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 3.2. Coeficiente de rugosidad

Para el cauce natural, se estimó el coeficiente de rugosidad a partir del método de Cowan (MOP, 2020):

## n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

## n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 3-1 muestra la condición del cauce según los criterios del método

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Grava fina|n0|0.024|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Alternándose<br>ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.013|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.052|

Para la obra proyectada se asignó un valor de rugosidad igual a 0.025 basado en valores tabulados en la

literatura (Chow, 1994).

## 3.3. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.07. MODELO HIDRÁULICO OA 07

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales están asociados a los periodos de retorno de diseño

y verificación de la obra, correspondientes a 100 y 150 años, respectivamente. Un resumen de las CB y su

ubicación se presenta en la Tabla 3-2 y en la Figura 3-3:

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>diseño<br>[m3/s]|Caudal<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅||12.02|13.80|0.020|
|DS||✅|-|-|0.016|

Figura 3-3. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

Los hidrogramas de entrada utilizados para el modelo se muestran a continuación:

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.07. MODELO HIDRÁULICO OA 07

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 3-4. Hidrogramas de entrada

## 3.4. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.3). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 40 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.07. MODELO HIDRÁULICO OA 07

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo

## 4.1. Condición sin proyecto

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.07. MODELO HIDRÁULICO OA 07

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición sin proyecto

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.07. MODELO HIDRÁULICO OA 07

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición sin proyecto

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.07. MODELO HIDRÁULICO OA 07

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 4.2. Condición con proyecto

Figura 4-6. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto

Figura 4-7. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.07. MODELO HIDRÁULICO OA 07

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-8. Profundidad máxima. Crecida de verificación (150 años). Condición con proyecto

Figura 4-9. Velocidad máxima. Crecida de verificación (150 años). Condición con proyecto

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.07. MODELO HIDRÁULICO OA 07

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto

# 5. Referencias

Chow, V. T. (1994). Hidráulica de canales abiertos. Colombia: McGraw-Hill.

Chow, V. T., Maidment, D. R., & Mays, L. W. (1988). Applied hydrology. Singapore: McGraw-Hill.

HEC. (2022). HEC-RAS. Versión 6.3. HEC-RAS. Versión 6.3. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# ANEXO 2.08. MODELO HIDRÁULICO OA 08 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANDINO

LONGOTOMA

# para ANDES SOLAR

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|26/10/2023|Revisión cliente|IDC|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comunas de La Ligua y Papudo<br>Región de Valparaíso|Col3|
|---|---|---|
||AND-B23014(2)-PAS156-DOC-02.08-A|Rev. A|

ANEXO 2.08. MODELO HIDRÁULICO OA 08

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Contenidos

1. Introducción ............................................................................................................................................. 4

2. Descripción del modelo.......................................................................................................................... 4

3. Parámetros de entrada ......................................................................................................................... 4

3.1. Obra proyectada .................................................................................................................................. 4
3.2. Coeficiente de rugosidad ................................................................................................................... 6
3.3. Condiciones de borde e iniciales ...................................................................................................... 6

3.4. Otras consideraciones......................................................................................................................... 8

4. Resultados ............................................................................................................................................... 9

4.1. Condición sin proyecto ....................................................................................................................... 9
4.2. Condición con proyecto ..................................................................................................................... 12

5. Referencias .............................................................................................................................................14

# Figuras

Figura 3-1. Topografía de la zona de estudio de la obra OA 08. Condición sin proyecto .................................... 5

Figura 3-2. Topografía de la zona de estudio de la obra OA 08. Condición con proyecto .................................. 5

Figura 3-3. Ubicación condiciones de borde ................................................................................................................. 7

Figura 3-4. Hidrogramas de entrada ............................................................................................................................. 8

Figura 4-1. Profundidad máxima. Crecida de diseño (50 años). Condición sin proyecto ..................................... 9

Figura 4-2. Velocidad máxima. Crecida de diseño (50 años). Condición sin proyecto ....................................... 10

Figura 4-3. Profundidad máxima. Crecida de verificación (100 años). Condición sin proyecto ....................... 10

Figura 4-4. Velocidad máxima. Crecida de verificación (100 años). Condición sin proyecto ..............................11

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto ................................................................11

Figura 4-6. Profundidad máxima. Crecida de diseño (50 años). Condición con proyecto.................................. 12

Figura 4-7. Velocidad máxima. Crecida de diseño (50 años). Condición con proyecto ....................................... 12

Figura 4-8. Profundidad máxima. Crecida de verificación (100 años). Condición con proyecto ....................... 13

Figura 4-9. Velocidad máxima. Crecida de verificación (100 años). Condición con proyecto ............................ 13

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto ........................................................... 14

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.08. MODELO HIDRÁULICO OA 08

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................ 4

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan ....................... 6

Tabla 3-2. Condiciones de borde e iniciales .................................................................................................................. 7

# Copyright

Este documento, sus anexos y planos son de propiedad exclusiva de Baqua Ingeniería y están destinados

únicamente al uso de Andes Solar. La copia, reproducción o divulgación no autorizada de su contenido está

estrictamente prohibida.

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.08. MODELO HIDRÁULICO OA 08

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 1. Introducción

Se construyó el modelo hidráulico de la obra de atravieso denominada OA 08, empleando para ello el

software HEC-RAS (2022). El objetivo del modelo es representar la condición actual del cauce, sin proyecto,

y su condición futura, con proyecto, para los caudales de diseño y verificación de la obra.

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados más relevantes de cada caso.

# 2. Descripción del modelo

El modelo se construyó con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La

descripción general de cada modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|Sin Proyecto|Representa la condición actual del cauce, en una extensión total de<br>364 m a lo largo de su eje, centrado en la obra proyectada y<br>manteniendo más de 138 m hacia aguas arriba y aguas abajo desde el<br>inicio y fin de la obra.<br> <br>Este modelo incluye la representación de una obra existente,<br>correspondiente a dos alcantarillas de hormigón de diámetro 0.6 m y<br>aproximada longitud de 12 m.|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|Con Proyecto|Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, además de incorporar la obra proyectada,<br>correspondiente a una alcantarilla compuesta por un cajón de<br>hormigón de sección 2x2 m y longitud de 22 m.|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

# 3. Parámetros de entrada

## 3.1. Obra proyectada

La obra de atravieso se proyectó mediante herramientas de geometría de HEC-RAS y las modificaciones de

terreno de RAS Mapper. A continuación, se muestra el terreno sin y con la obra incorporada.

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.08. MODELO HIDRÁULICO OA 08

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 3-1. Topografía de la zona de estudio de la obra OA 08. Condición sin proyecto

Figura 3-2. Topografía de la zona de estudio de la obra OA 08. Condición con proyecto

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.08. MODELO HIDRÁULICO OA 08

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 3.2. Coeficiente de rugosidad

Para el cauce natural, se estimó el coeficiente de rugosidad a partir del método de Cowan (MOP, 2020):

## n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

## n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 3-1 muestra la condición del cauce según los criterios del método

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Alternándose<br>ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Baja|n4|0.010|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.045|

Para la obra proyectada se asignó un valor de rugosidad igual a 0.014 basado en valores tabulados en la

literatura (Chow, 1994).

## 3.3. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.08. MODELO HIDRÁULICO OA 08

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales están asociados a los periodos de retorno de diseño

y verificación de la obra, correspondientes a 50 y 100 años, respectivamente. Un resumen de las CB y su

ubicación se presenta en la Tabla 3-2 y en la Figura 3-3:

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>diseño<br>[m3/s]|Caudal<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅||3.73|4.87|0.035|
|DS||✅|-|-|0.014|

Figura 3-3. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.08. MODELO HIDRÁULICO OA 08

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Los hidrogramas de entrada utilizados para el modelo se muestran a continuación:

Figura 3-4. Hidrogramas de entrada

## 3.4. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.3). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 40 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.08. MODELO HIDRÁULICO OA 08

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo

## 4.1. Condición sin proyecto

Figura 4-1. Profundidad máxima. Crecida de diseño (50 años). Condición sin proyecto

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.08. MODELO HIDRÁULICO OA 08

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-2. Velocidad máxima. Crecida de diseño (50 años). Condición sin proyecto

Figura 4-3. Profundidad máxima. Crecida de verificación (100 años). Condición sin proyecto

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.08. MODELO HIDRÁULICO OA 08

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-4. Velocidad máxima. Crecida de verificación (100 años). Condición sin proyecto

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.08. MODELO HIDRÁULICO OA 08

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 4.2. Condición con proyecto

Figura 4-6. Profundidad máxima. Crecida de diseño (50 años). Condición con proyecto

Figura 4-7. Velocidad máxima. Crecida de diseño (50 años). Condición con proyecto

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.08. MODELO HIDRÁULICO OA 08

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-8. Profundidad máxima. Crecida de verificación (100 años). Condición con proyecto

Figura 4-9. Velocidad máxima. Crecida de verificación (100 años). Condición con proyecto

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.08. MODELO HIDRÁULICO OA 08

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto

# 5. Referencias

Chow, V. T. (1994). Hidráulica de canales abiertos. Colombia: McGraw-Hill.

Chow, V. T., Maidment, D. R., & Mays, L. W. (1988). Applied hydrology. Singapore: McGraw-Hill.

HEC. (2022). HEC-RAS. Versión 6.3. HEC-RAS. Versión 6.3. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# ANEXO 2.09 MODELO HIDRÁULICO OA 09 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANDINO

LONGOTOMA

# para ANDES SOLAR

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|26/10/2023|Revisión cliente|JCP|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comunas de La Ligua y Papudo<br>Región de Valparaíso|Col3|
|---|---|---|
||AND-B23014(2)-PAS156-DOC-02.09-A|Rev. A|

ANEXO 2.09 MODELO HIDRÁULICO OA 09

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Contenidos

1. Introducción ............................................................................................................................................. 4

2. Descripción del modelo.......................................................................................................................... 4

3. Parámetros de entrada ......................................................................................................................... 4

3.1. Obra proyectada .................................................................................................................................. 4
3.2. Coeficiente de rugosidad ................................................................................................................... 6
3.3. Condiciones de borde e iniciales ...................................................................................................... 6

3.4. Otras consideraciones......................................................................................................................... 9

4. Resultados ............................................................................................................................................... 9

4.1. Condición sin proyecto ....................................................................................................................... 9
4.2. Condición con proyecto ..................................................................................................................... 12

5. Referencias ............................................................................................................................................. 15

# Figuras

Figura 3-1. Topografía de la zona de estudio de la obra OA 09 y layout (negro). Condición sin proyecto ...... 5

Figura 3-2. Topografía de la zona de estudio de la obra OA 09 y layout (negro). Condición con proyecto .... 5

Figura 3-3. Ubicación condiciones de borde ................................................................................................................. 7

Figura 3-4. Hidrogramas de entrada. Crecida de diseño (50 años) ......................................................................... 8

Figura 3-5. Hidrogramas de entrada. Crecida de verificación (100 años) ............................................................... 8

Figura 4-1. Profundidad máxima. Crecida de diseño (50 años). Condición sin proyecto ..................................... 9

Figura 4-2. Velocidad máxima. Crecida de diseño (50 años). Condición sin proyecto ....................................... 10

Figura 4-3. Profundidad máxima. Crecida de verificación (100 años). Condición sin proyecto ....................... 10

Figura 4-4. Velocidad máxima. Crecida de verificación (100 años). Condición sin proyecto ..............................11

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto ................................................................11

Figura 4-6. Profundidad máxima. Crecida de diseño (50 años). Condición con proyecto.................................. 12

Figura 4-7. Velocidad máxima. Crecida de diseño (50 años). Condición con proyecto ....................................... 13

Figura 4-8. Profundidad máxima. Crecida de verificación (100 años). Condición con proyecto ....................... 13

Figura 4-9. Velocidad máxima. Crecida de verificación (100 años). Condición con proyecto ........................... 14

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto ........................................................... 14

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.09 MODELO HIDRÁULICO OA 09

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................ 4

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan ....................... 6

Tabla 3-2. Condiciones de borde e iniciales .................................................................................................................. 7

# Copyright

Este documento, sus anexos y planos son de propiedad exclusiva de Baqua Ingeniería y están destinados

únicamente al uso de Andes Solar. La copia, reproducción o divulgación no autorizada de su contenido está

estrictamente prohibida.

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.09 MODELO HIDRÁULICO OA 09

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 1. Introducción

Se construyó el modelo hidráulico de la obra de atravieso denominada OA 09, empleando para ello el

software HEC-RAS (2022). El objetivo del modelo es representar la condición actual del cauce, sin proyecto,

y su condición futura, con proyecto, para los caudales de diseño y verificación de la obra.

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados más relevantes de cada caso.

# 2. Descripción del modelo

El modelo se construyó con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La

descripción general de cada modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|Sin Proyecto|Representa la condición actual del cauce, en una extensión total de<br>280 m a lo largo de su eje, centrado en la obra proyectada y<br>manteniendo más de 120 m hacia aguas arriba y aguas abajo desde el<br>inicio y fin de la obra.|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|Con Proyecto|Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, además de incorporar la obra proyectada,<br>correspondiente a una alcantarilla compuesta por dos cajones de<br>hormigón de sección 1.5 x 1.5 m y longitud de 12.5 m.|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

# 3. Parámetros de entrada

## 3.1. Obra proyectada

La obra de atravieso se proyectó mediante herramientas de geometría de HEC-RAS y las modificaciones de

terreno de RAS Mapper. A continuación, se muestra el terreno sin y con la obra incorporada.

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.09 MODELO HIDRÁULICO OA 09

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 3-1. Topografía de la zona de estudio de la obra OA 09 y layout (negro). Condición sin proyecto

Figura 3-2. Topografía de la zona de estudio de la obra OA 09 y layout (negro). Condición con proyecto

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.09 MODELO HIDRÁULICO OA 09

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 3.2. Coeficiente de rugosidad

Para el cauce natural, se estimó el coeficiente de rugosidad a partir del método de Cowan (MOP, 2020):

## n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

## n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 3-1 muestra la condición del cauce según los criterios del método

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Grava fina|n0|0.024|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Alternándose ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.013|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.052|

Para la obra proyectada se asignó un valor de rugosidad igual a 0.014 basado en valores tabulados en la

literatura (Chow, 1994).

## 3.3. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.09 MODELO HIDRÁULICO OA 09

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales están asociados a los periodos de retorno de diseño

y verificación de la obra, correspondientes a 50 y 100 años, respectivamente. Un resumen de las CB y su

ubicación se presenta en la Tabla 3-2 y en la Figura 3-3:

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>diseño<br>[m3/s]|Caudal<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_OO|✅||3.21|4.19|0.016|
|US_01|✅||0.31|0.40|0.003|
|DS||✅|-|-|0.017|

Figura 3-3. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.09 MODELO HIDRÁULICO OA 09

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

Los hidrogramas de entrada utilizados para el modelo se muestran a continuación:

Figura 3-4. Hidrogramas de entrada. Crecida de diseño (50 años)

Figura 3-5. Hidrogramas de entrada. Crecida de verificación (100 años)

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.09 MODELO HIDRÁULICO OA 09

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 3.4. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.3). Además, el área de flujo se discretizó en celdas de 1 x 1 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 40 minutos para que el flujo entrara

en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su superficie

inundada.

# 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo

## 4.1. Condición sin proyecto

Figura 4-1. Profundidad máxima. Crecida de diseño (50 años). Condición sin proyecto

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.09 MODELO HIDRÁULICO OA 09

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-2. Velocidad máxima. Crecida de diseño (50 años). Condición sin proyecto

Figura 4-3. Profundidad máxima. Crecida de verificación (100 años). Condición sin proyecto

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.09 MODELO HIDRÁULICO OA 09

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-4. Velocidad máxima. Crecida de verificación (100 años). Condición sin proyecto

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.09 MODELO HIDRÁULICO OA 09

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 4.2. Condición con proyecto

Figura 4-6. Profundidad máxima. Crecida de diseño (50 años). Condición con proyecto

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.09 MODELO HIDRÁULICO OA 09

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-7. Velocidad máxima. Crecida de diseño (50 años). Condición con proyecto

Figura 4-8. Profundidad máxima. Crecida de verificación (100 años). Condición con proyecto

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.09 MODELO HIDRÁULICO OA 09

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-9. Velocidad máxima. Crecida de verificación (100 años). Condición con proyecto

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.09 MODELO HIDRÁULICO OA 09

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 5. Referencias

Chow, V. T. (1994). Hidráulica de canales abiertos. Colombia: McGraw-Hill.

Chow, V. T., Maidment, D. R., & Mays, L. W. (1988). Applied hydrology. Singapore: McGraw-Hill.

HEC. (2022). HEC-RAS. Versión 6.3. HEC-RAS. Versión 6.3. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

15 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# ANEXO 2.10 MODELO HIDRÁULICO OA 10 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANDINO

LONGOTOMA

# para ANDES SOLAR

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|26/10/2023|Revisión cliente|JCP|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comunas de La Ligua y Papudo<br>Región de Valparaíso|Col3|
|---|---|---|
||AND-B23014(2)-PAS156-DOC-02.10-A|Rev. A|

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Contenidos

1. Introducción ............................................................................................................................................. 4

2. Descripción del modelo.......................................................................................................................... 4

3. Parámetros de entrada ......................................................................................................................... 4

3.1. Obra proyectada .................................................................................................................................. 4
3.2. Coeficiente de rugosidad ................................................................................................................... 6
3.3. Condiciones de borde e iniciales ...................................................................................................... 6

3.4. Otras consideraciones......................................................................................................................... 8

4. Resultados ............................................................................................................................................... 9

4.1. Condición sin proyecto ....................................................................................................................... 9
4.2. Condición con proyecto ..................................................................................................................... 13

5. Referencias ............................................................................................................................................. 17

# Figuras

Figura 3-1. Topografía de la zona de estudio de la obra OA 10 y layout (negro). Condición sin proyecto ....... 5

Figura 3-2. Topografía de la zona de estudio de la obra OA 10 y layout (negro). Condición con proyecto ..... 5

Figura 3-3. Ubicación condiciones de borde ................................................................................................................. 7

Figura 3-4. Hidrogramas de entrada ............................................................................................................................. 8

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto ................................... 9

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto ..................................... 10

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición sin proyecto ..........................11

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición sin proyecto ............................. 12

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto ............................................................... 12

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto ................................. 13

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto .................................... 14

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición con proyecto ........................ 15

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición con proyecto ............................16

Figura 4-5. Hidrograma a la salida del modelo. Condición con proyecto ..............................................................16

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................ 4

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan ....................... 6

Tabla 3-2. Condiciones de borde e iniciales .................................................................................................................. 7

# Copyright

Este documento, sus anexos y planos son de propiedad exclusiva de Baqua Ingeniería y están destinados

únicamente al uso de Andes Solar. La copia, reproducción o divulgación no autorizada de su contenido está

estrictamente prohibida.

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 1. Introducción

Se construyó el modelo hidráulico de la obra de atravieso denominada OA 10, empleando para ello el

software HEC-RAS (2022). El objetivo del modelo es representar la condición actual del cauce, sin proyecto,

y su condición futura, con proyecto, para los caudales de diseño y verificación de la obra.

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados más relevantes de cada caso.

# 2. Descripción del modelo

El modelo se construyó con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La

descripción general de cada modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|Sin Proyecto|Representa la condición actual del cauce, en una extensión total de<br>100 m a lo largo de su eje, centrado en la obra proyectada y<br>manteniendo 50 m hacia aguas arriba y aguas abajo desde el inicio y<br>fin de la obra.|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|Con Proyecto|Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, además de incorporar la obra proyectada,<br>correspondiente a un badén con ancho basal de 4 m, altura de 0.4 m,<br>talud 10:1 (H:V) y longitud de 12.3 m (medida en el sentido del cauce).|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

Nótese que el modelo no abarca una mayor extensión hacia aguas arriba porque la obra se encuentra cerca

de la cabecera de la cuenca y la forma del cauce no se aprecia más allá de los 50 m. Asimismo, la extensión

aguas abajo del modelo no supera los 50 m debido a la alta intervención en el terreno.

# 3. Parámetros de entrada

## 3.1. Obra proyectada

La obra de atravieso se proyectó mediante herramientas de geometría de HEC-RAS y las modificaciones de

terreno de RAS Mapper. A continuación, se muestra el terreno sin y con la obra incorporada.

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 3-1. Topografía de la zona de estudio de la obra OA 10 y layout (negro). Condición sin proyecto

Figura 3-2. Topografía de la zona de estudio de la obra OA 10 y layout (negro). Condición con proyecto

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 3.2. Coeficiente de rugosidad

Para el cauce natural, se estimó el coeficiente de rugosidad a partir del método de Cowan (MOP, 2020):

## n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

## n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 3-1 muestra la condición del cauce según los criterios del método

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Alternándose ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Baja|n4|0.005|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.040|

Para la obra proyectada se asignó un valor de rugosidad igual a 0.025 basado en valores tabulados en la

literatura (Chow, 1994).

## 3.3. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales están asociados a los periodos de retorno de diseño

y verificación de la obra, correspondientes a 100 y 150 años, respectivamente. Un resumen de las CB y su

ubicación se presenta en la Tabla 3-2 y en la Figura 3-3:

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>diseño<br>[m3/s]|Caudal<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US|✅||0.37|0.43|0.10|
|DS||✅|-|-|0.14|

Figura 3-3. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Los hidrogramas de entrada utilizados para el modelo se muestran a continuación:

Figura 3-4. Hidrogramas de entrada

## 3.4. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.3). Además, el área de flujo se discretizó en celdas de 0.5 x 0.5 m y se utilizó un

paso de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo

de 0.15 y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 40 minutos para que el flujo

entrara en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su

superficie inundada.

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo

## 4.1. Condición sin proyecto

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición sin proyecto

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición sin proyecto

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 4.2. Condición con proyecto

Figura 4-6. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-7. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-8. Profundidad máxima. Crecida de verificación (150 años). Condición con proyecto

15 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-9. Velocidad máxima. Crecida de verificación (150 años). Condición con proyecto

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto

16 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.10 MODELO HIDRÁULICO OA 10

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 5. Referencias

Chow, V. T. (1994). Hidráulica de canales abiertos. Colombia: McGraw-Hill.

Chow, V. T., Maidment, D. R., & Mays, L. W. (1988). Applied hydrology. Singapore: McGraw-Hill.

HEC. (2022). HEC-RAS. Versión 6.3. HEC-RAS. Versión 6.3. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

17 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# ANEXO 2.11. MODELO HIDRÁULICO OA 11 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANTINO

LONGOTOMA

# para ANDES SOLAR

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|26/10/2023|Revisión cliente|IDC|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comunas de La Ligua y Papudo<br>Región de Valparaíso|Col3|
|---|---|---|
||AND-B23014(2)-PAS156-DOC-02.11-A|Rev. A|

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

# Contenidos

1. Introducción ............................................................................................................................................. 4

2. Descripción del modelo.......................................................................................................................... 4

3. Parámetros de entrada ......................................................................................................................... 4

3.1. Obra proyectada .................................................................................................................................. 4
3.2. Coeficiente de rugosidad .................................................................................................................... 5
3.3. Condiciones de borde e iniciales ...................................................................................................... 6

3.4. Otras consideraciones......................................................................................................................... 8

4. Resultados ............................................................................................................................................... 9

4.1. Condición sin proyecto ....................................................................................................................... 9
4.2. Condición con proyecto ..................................................................................................................... 13

5. Referencias ............................................................................................................................................. 17

# Figuras

Figura 3-1. Topografía de la zona de estudio de la obra OA 11. Condición sin proyecto ...................................... 5

Figura 3-2. Topografía de la zona de estudio de la obra OA 11. Condición con proyecto..................................... 5

Figura 3-3. Ubicación condiciones de borde ................................................................................................................. 7

Figura 3-4. Hidrogramas de entrada ............................................................................................................................. 8

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto ................................... 9

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto ..................................... 10

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición sin proyecto ..........................11

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición sin proyecto ............................. 12

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto ............................................................... 12

Figura 4-6. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto ................................ 13

Figura 4-7. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto .................................... 14

Figura 4-8. Profundidad máxima. Crecida de verificación (150 años). Condición con proyecto ....................... 15

Figura 4-9. Velocidad máxima. Crecida de verificación (150 años). Condición con proyecto ............................16

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto ............................................................16

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

# Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................ 4

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan ....................... 6

Tabla 3-2. Condiciones de borde e iniciales .................................................................................................................. 7

# Copyright

Este documento, sus anexos y planos son de propiedad exclusiva de Baqua Ingeniería y están destinados

únicamente al uso de Andes Solar. La copia, reproducción o divulgación no autorizada de su contenido está

estrictamente prohibida.

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

# 1. Introducción

Se construyó el modelo hidráulico de la obra de atravieso denominada OA 11, empleando para ello el

software HEC-RAS (2022). El objetivo del modelo es representar la condición actual del cauce, sin proyecto,

y su condición futura, con proyecto, para los caudales de diseño y verificación de la obra.

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados más relevantes de cada caso.

# 2. Descripción del modelo

El modelo se construyó con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La

descripción general de cada modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|Sin Proyecto|Representa la condición actual del cauce, en una extensión total de 251<br>m a lo largo de su eje, centrado en la obra proyectada y manteniendo<br>más de 154 m hacia aguas arriba y 91 m aguas abajo, desde el inicio y<br>fin de la obra.|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|Con Proyecto|Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, además de incorporar la obra proyectada,<br>correspondiente a un mejoramiento de cauce de hormigón proyectado<br>con base de 2.5 m, altura de 0.5 m, talud de 3:1 (H:V) y longitud de 4.1<br>m (medida en el sentido del cauce).|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

Nótese que el modelo no abarca una mayor extensión hacia aguas abajo debido a que la obra se encuentra

cerca de la confluencia del cauce con el Río Petorca y su forma no se aprecia más allá de los 91 m.

# 3. Parámetros de entrada

## 3.1. Obra proyectada

La obra de atravieso se proyectó mediante herramientas de geometría de HEC-RAS y las modificaciones de

terreno de RAS Mapper. A continuación, se muestra el terreno sin y con la obra incorporada.

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

Figura 3-1. Topografía de la zona de estudio de la obra OA 11. Condición sin proyecto

Figura 3-2. Topografía de la zona de estudio de la obra OA 11. Condición con proyecto

## 3.2. Coeficiente de rugosidad

Para el cauce natural, se estimó el coeficiente de rugosidad a partir del método de Cowan (MOP, 2020):

## n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

## n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 3-1 muestra la condición del cauce según los criterios del método

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Despreciable|n1|0.000|
|Variación de las secciones transversales|Alternándose<br>ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.010|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.045|

Para la obra proyectada se asignó un valor de rugosidad igual a 0.019 basado en valores tabulados en la

literatura (Chow, 1994).

## 3.3. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales están asociados a los periodos de retorno de diseño

y verificación de la obra, correspondientes a 100 y 150 años, respectivamente. Un resumen de las CB y su

ubicación se presenta en la Tabla 3-2 y en la Figura 3-3:

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>diseño<br>[m3/s]|Caudal<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅||0.833|0.952|0.022|
|DS||✅|-|-|0.210|

Figura 3-3. Ubicación condiciones de borde

Si bien la hidrología entregó un caudal máximo instantáneo, el modelo bidimensional requiere de un

hidrograma de crecida. Debido a las inestabilidades numéricas que podría inducir un hidrograma constante

a la simulación, se optó por añadir hidrogramas que van de cero al máximo en un periodo de 1 hora y

permanecen constantes por, a lo más, un periodo de 2 horas.

Los hidrogramas de entrada utilizados para el modelo se muestran a continuación:

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

Figura 3-4. Hidrogramas de entrada

## 3.4. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.3). Además, el área de flujo se discretizó en celdas de 0.5 x 0.5 m y se utilizó un

paso de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo

de 0.15 y un máximo de 0.40. Se consideró un tiempo de modelo de 1 hora y 50 minutos para que el flujo

entrara en régimen permanente, con caudales de entrada iguales a los de salida, maximizando así su

superficie inundada.

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

# 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo

## 4.1. Condición sin proyecto

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición sin proyecto

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición sin proyecto

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

## 4.2. Condición con proyecto

Figura 4-6. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

Figura 4-7. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

Figura 4-8. Profundidad máxima. Crecida de verificación (150 años). Condición con proyecto

15 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

Figura 4-9. Velocidad máxima. Crecida de verificación (150 años). Condición con proyecto

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto

16 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.11. MODELO HIDRÁULICO OA 11

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANTINO LONGOTOMA

# 5. Referencias

Chow, V. T. (1994). Hidráulica de canales abiertos. Colombia: McGraw-Hill.

Chow, V. T., Maidment, D. R., & Mays, L. W. (1988). Applied hydrology. Singapore: McGraw-Hill.

HEC. (2022). HEC-RAS. Versión 6.3. HEC-RAS. Versión 6.3. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

17 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# ANEXO 2.12. MODELO HIDRÁULICO OA 12 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANDINO

LONGOTOMA

# para ANDES SOLAR

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|26/10/2023|Revisión cliente|IDC|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comunas de La Ligua y Papudo<br>Región de Valparaíso|Col3|
|---|---|---|
||AND-B23014(2)-PAS156-DOC-02.12-A|Rev. A|

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Contenidos

1. Introducción ............................................................................................................................................. 4

2. Descripción del modelo.......................................................................................................................... 4

3. Parámetros de entrada ......................................................................................................................... 4

3.1. Obra proyectada .................................................................................................................................. 4
3.2. Coeficiente de rugosidad .................................................................................................................... 5
3.3. Condiciones de borde e iniciales ...................................................................................................... 6

3.4. Otras consideraciones......................................................................................................................... 8

4. Resultados ............................................................................................................................................... 9

4.1. Condición sin proyecto ....................................................................................................................... 9
4.2. Condición con proyecto ..................................................................................................................... 13

5. Referencias ............................................................................................................................................. 17

# Figuras

Figura 3-1. Topografía de la zona de estudio de la obra OA 12. Condición sin proyecto ...................................... 5

Figura 3-2. Topografía de la zona de estudio de la obra OA 12. Condición con proyecto .................................... 5

Figura 3-3. Ubicación condiciones de borde ................................................................................................................. 7

Figura 3-4. Hidrogramas de entrada ............................................................................................................................. 8

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto ................................... 9

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto ..................................... 10

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición sin proyecto ..........................11

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición sin proyecto ............................. 12

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto ............................................................... 12

Figura 4-6. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto ................................ 13

Figura 4-7. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto .................................... 14

Figura 4-8. Profundidad máxima. Crecida de verificación (150 años). Condición con proyecto ....................... 15

Figura 4-9. Velocidad máxima. Crecida de verificación (150 años). Condición con proyecto ............................16

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto ............................................................16

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................ 4

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan ....................... 6

Tabla 3-2. Condiciones de borde e iniciales .................................................................................................................. 7

# Copyright

Este documento, sus anexos y planos son de propiedad exclusiva de Baqua Ingeniería y están destinados

únicamente al uso de Andes Solar. La copia, reproducción o divulgación no autorizada de su contenido está

estrictamente prohibida.

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 1. Introducción

Se construyó el modelo hidráulico de la obra de atravieso denominada OA 12, empleando para ello el

software HEC-RAS (2022). El objetivo del modelo es representar la condición actual del cauce, sin proyecto,

y su condición futura, con proyecto, para los caudales de diseño y verificación de la obra.

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados más relevantes de cada caso.

# 2. Descripción del modelo

El modelo se construyó con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La

descripción general de cada modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|Sin Proyecto|Representa la condición actual del cauce, en una extensión total de<br>3970 m a lo largo de su eje, centrado en la obra proyectada y<br>manteniendo más de 1780 m hacia aguas arriba y aguas abajo desde<br>el inicio y fin de la obra.|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|Con Proyecto|Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, además de incorporar la obra proyectada,<br>correspondiente a una estabilización del camino existente con un<br>ancho basal de 8 m y una longitud total de 415 m.|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

# 3. Parámetros de entrada

## 3.1. Obra proyectada

La obra de atravieso se proyectó mediante herramientas de geometría de HEC-RAS y las modificaciones de

terreno de RAS Mapper. A continuación, se muestra el terreno sin y con la obra incorporada.

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 3-1. Topografía de la zona de estudio de la obra OA 12. Condición sin proyecto

Figura 3-2. Topografía de la zona de estudio de la obra OA 12. Condición con proyecto

## 3.2. Coeficiente de rugosidad

Para el cauce natural, se estimó el coeficiente de rugosidad a partir del método de Cowan (MOP, 2020):

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

## n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 3-1 muestra la condición del cauce según los criterios del método

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Alternándose<br>ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.010|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.050|

Para la obra proyectada se asignó un valor de rugosidad igual a 0.036 basado en valores tabulados en la

literatura (Chow, 1994).

## 3.3. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. Todos los caudales están asociados a los periodos de retorno de diseño

y verificación de la obra, correspondientes a 100 y 150 años, respectivamente. Un resumen de las CB y su

ubicación se presenta en la Tabla 3-2 y en la Figura 3-3:

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Peak caudal<br>diseño<br>[m3/s]|Peak caudal<br>verificación<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|---|
|US_00|✅||1199.40|1448.69|0.006|
|DS||✅|-|-|0.005|

Figura 3-3. Ubicación condiciones de borde

Los hidrogramas de crecida se presentan en la siguiente figura:

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 3-4. Hidrogramas de entrada

## 3.4. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.3). Además, el área de flujo se discretizó en celdas de 4 x 4 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. El tiempo de modelación se consideró en función del tiempo de llegada al peak del

hidrograma de crecida, en particular el modelo de la OA 12 tiene un tiempo de modelación de 48 horas. Cabe

mencionar que, como se aprecia en Figura 3-4, el hidrograma de salida no alcanza a mostrar la crecida

completa, sin embargo, sí se logra apreciar su peak y la mayor parte de la cola de salida del hidrograma.

Adicionalmente, se consideró el refinamiento de la malla de cálculo a celdas de 1 x 1 m, en las zonas que se

muestran en la Figura 3-3 (con color rojo). El objetivo de estos refinamientos es representar de mejor forma

las características de la obra proyectada y solucionar algunas inestabilidades numéricas del modelo.

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo

## 4.1. Condición sin proyecto

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-3. Profundidad máxima. Crecida de verificación (150 años). Condición sin proyecto

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-4. Velocidad máxima. Crecida de verificación (150 años). Condición sin proyecto

Figura 4-5. Hidrograma a la salida del modelo. Condición sin proyecto

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## 4.2. Condición con proyecto

Figura 4-6. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-7. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-8. Profundidad máxima. Crecida de verificación (150 años). Condición con proyecto

15 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-9. Velocidad máxima. Crecida de verificación (150 años). Condición con proyecto

Figura 4-10. Hidrograma a la salida del modelo. Condición con proyecto

16 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.12. MODELO HIDRÁULICO OA 12

PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 5. Referencias

Chow, V. T. (1994). Hidráulica de canales abiertos. Colombia: McGraw-Hill.

Chow, V. T., Maidment, D. R., & Mays, L. W. (1988). Applied hydrology. Singapore: McGraw-Hill.

HEC. (2022). HEC-RAS. Versión 6.3. HEC-RAS. Versión 6.3. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

17 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

+56 9 5001 9945
[www.baqua.cl](https://www.baqua.cl/)

+56 9 5001 3096

Baqua Ingeniería

[www.baqua.cl](https://www.baqua.cl/)
[contacto@baqua.cl](mailto:contacto@baqua.cl)

# ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02 PERMISO AMBIENTAL SECTORIAL 156 PARQUE FOTOVOLTAICO ANDINO

LONGOTOMA

# para ANDES SOLAR

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
||||||||
|A|-|26/10/2023|Revisión cliente|IDC|BGP|ABL|
|Rev.|Rev. Int.|Fecha|Emitido para|Emitido por|Revisado por|Aprobado por|

|Col1|Comunas de La Ligua y Papudo<br>Región de Valparaíso|Col3|
|---|---|---|
||AND-B23014(2)-PAS156-DOC-02.13-A|Rev. A|

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# Contenidos

1. Introducción ............................................................................................................................................. 4

2. Descripción del modelo.......................................................................................................................... 4

3. Parámetros de entrada ......................................................................................................................... 4

3.1. Obra proyectada .................................................................................................................................. 4

3.1.1. Proyección obra de defensa OP 01 ........................................................................................................ 5

3.1.2. Proyección obra de defensa OP 02 ........................................................................................................ 6

3.2. Coeficiente de rugosidad ................................................................................................................... 6
3.3. Condiciones de borde e iniciales ....................................................................................................... 7

3.4. Otras consideraciones......................................................................................................................... 9

4. Resultados ............................................................................................................................................. 10

4.1. Modelo HEC-RAS ............................................................................................................................... 10

4.1.1. Condición sin proyecto ........................................................................................................................... 10

4.1.2. Condición con proyecto ............................................................................................................................11

4.2. Modelo OP 01 ...................................................................................................................................... 13

4.2.1. Condición sin proyecto ............................................................................................................................ 13

4.2.2. Condición con proyecto .......................................................................................................................... 14

4.3. Modelo OP 02 ...................................................................................................................................... 15

4.3.1. Condición sin proyecto ............................................................................................................................ 15

4.3.2. Condición con proyecto ......................................................................................................................16

5. Referencias ............................................................................................................................................. 17

# Figuras

Figura 3-1. Topografía de la zona de estudio de la obra OP 01. Condición sin proyecto ..................................... 5

Figura 3-2. Topografía de la zona de estudio de la obra OP 01. Condición con proyecto.................................... 5

Figura 3-3. Topografía de la zona de estudio de la obra OP 02. Condición sin proyecto .................................... 6

Figura 3-4. Topografía de la zona de estudio de la obra OP 02. Condición con proyecto .................................. 6

Figura 3-5. Ubicación condiciones de borde ................................................................................................................. 8

Figura 3-6. Hidrogramas de crecida US_00 ................................................................................................................. 9

ii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto ................................. 10

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto .......................................11

Figura 4-3. Hidrograma a la salida del modelo. Condición sin proyecto ................................................................11

Figura 4-4. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto................................ 12

Figura 4-5. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto ..................................... 12

Figura 4-6. Hidrograma a la salida del modelo. Condición con proyecto .............................................................. 13

Figura 4-7. Profundidad máxima OP 01. Crecida de diseño (100 años). Condición sin proyecto. Incluye líneas

de flujo (color blanco) ...................................................................................................................................................... 13

Figura 4-8. Velocidad máxima OP 01. Crecida de diseño (100 años). Condición sin proyecto. Incluye líneas de

flujo (color blanco) ........................................................................................................................................................... 14

Figura 4-9. Profundidad máxima OP 01. Crecida de diseño (100 años). Condición con proyecto. Incluye líneas

de flujo (color blanco) ..................................................................................................................................................... 14

Figura 4-10. Velocidad máxima OP 01. Crecida de diseño (100 años). Condición con proyecto. Incluye líneas

de flujo (color blanco) ...................................................................................................................................................... 15

Figura 4-11. Profundidad máxima OP 02. Crecida de diseño (100 años). Condición sin proyecto. Incluye líneas

de flujo (color blanco) ...................................................................................................................................................... 15

Figura 4-12. Velocidad máxima OP 02. Crecida de diseño (100 años). Condición sin proyecto. Incluye líneas

de flujo (color blanco) ......................................................................................................................................................16

Figura 4-13. Profundidad máxima OP 02. Crecida de diseño (100 años). Condición con proyecto. Incluye líneas

de flujo (color blanco) ......................................................................................................................................................16

Figura 4-14. Velocidad máxima OP 02. Crecida de diseño (100 años). Condición con proyecto. Incluye líneas

de flujo (color blanco) ...................................................................................................................................................... 17

# Tablas

Tabla 2-1. Descripción general de los modelos hidráulicos ........................................................................................ 4

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan ....................... 7

Tabla 3-2. Condiciones de borde e iniciales .................................................................................................................. 8

# Copyright

Este documento, sus anexos y planos son de propiedad exclusiva de Baqua Ingeniería y están destinados

únicamente al uso de Andes Solar. La copia, reproducción o divulgación no autorizada de su contenido está

estrictamente prohibida.

iii Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 1. Introducción

Se construyó el modelo hidráulico de las obras de defensa denominadas OP 01 y OP 02, cuyo objetivo es dar

protección a las torres 15 y 14 de la línea alta tensión del proyecto, respectivamente, empleando para ello el

software HEC-RAS (2022). El objetivo del modelo es representar la condición actual del cauce, sin proyecto,

y su condición futura, con proyecto, para el caudal de diseño asociado a un periodo de retorno de 100 años.

Los resultados entregados por el software permitirán conocer las características del flujo y la superficie

inundada para cada condición. A continuación, se presentan las principales consideraciones para elaborar los

modelos y los resultados más relevantes de cada caso.

# 2. Descripción del modelo

El modelo se construyó con el software HEC-RAS, utilizando para su cálculo un flujo bidimensional. La

descripción general de cada modelo se representa en la Tabla 2-1.

Tabla 2-1. Descripción general de los modelos hidráulicos

|Condición|Descripción|Objetivo|
|---|---|---|
|Sin Proyecto|Representa la condición actual del cauce, en una extensión total de 3.4<br>km a lo largo del eje del Río La Ligua.|Representar<br>la<br>condición<br>actual<br>del<br>cauce|
|Con Proyecto|Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, además de incorporar las obras proyectadas,<br>correspondiente a dos muros de gaviones, uno para cada torre (Torres<br>14 y 15), que están formados por gaviones de 2.0x1.0x1.0 m, con una<br>forma hexagonal vista en planta.|Representar<br>la<br>condición<br>futura<br>del<br>cauce|

# 3. Parámetros de entrada

## 3.1. Obra proyectada

Las obras de defensa se proyectaron mediante herramientas de geometría de HEC-RAS y las modificaciones

de terreno de RAS Mapper. A continuación, se muestra el terreno sin y con las obras incorporadas.

4 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

### 3.1.1. Proyección obra de defensa OP 01

Figura 3-1. Topografía de la zona de estudio de la obra OP 01. Condición sin proyecto

Figura 3-2. Topografía de la zona de estudio de la obra OP 01. Condición con proyecto

5 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

### 3.1.2. Proyección obra de defensa OP 02

Figura 3-3. Topografía de la zona de estudio de la obra OP 02. Condición sin proyecto

Figura 3-4. Topografía de la zona de estudio de la obra OP 02. Condición con proyecto

## 3.2. Coeficiente de rugosidad

Para el cauce natural, se estimó el coeficiente de rugosidad a partir del método de Cowan (MOP, 2020):

6 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

## n= m⋅(n 0 + n 1 + n 2 + n 3 + n 4 ) (1)

Donde:

m : Coeficiente asociado a la sinuosidad y frecuencia de meandros

n 0 : Coeficiente asociado al material del lecho

n 1 : Coeficiente asociado al grado de irregularidad del perímetro mojado

n 2 : Coeficiente asociado a la variación de las secciones transversales

## n 3 : Coeficiente asociado al efecto relativo de las obstrucciones

n 4 : Coeficiente asociado a la densidad de vegetación

La Tabla 3-1 muestra la condición del cauce según los criterios del método

Tabla 3-1. Condición del cauce para el cálculo del coeficiente de Manning con método Cowan

|Condición del cauce|Col2|Símbolo|Valor|
|---|---|---|---|
|Material del lecho|Tierra|n0|0.020|
|Grado de irregularidad del perímetro mojado|Leve|n1|0.005|
|Variación de las secciones transversales|Alternándose<br>ocasionalmente|n2|0.005|
|Efecto relativo de las obstrucciones|Leve|n3|0.010|
|Densidad de vegetación|Media|n4|0.010|
|Sinuosidad y frecuencia de meandros|Leve|m|1.000|
|Coeficiente de rugosidad|Coeficiente de rugosidad|n|0.050|

## 3.3. Condiciones de borde e iniciales

Se definieron dos tipos de condiciones de borde (CB): (i) inicial o aguas arriba y (ii) final o aguas abajo. La CB

de aguas arriba incorpora el caudal de la cuenca desde el inicio del área de interés y se incluye la CB aguas

abajo para permitir la salida del flujo.

Además, las CB poseen condición de borde de altura normal, definiendo el parámetro de pendiente normal

a partir de la topografía del modelo. El caudal está asociado al periodo de retorno de diseño de la obra,

correspondientes a 100 años, respectivamente. Un resumen de las CB y su ubicación se presenta en la Tabla

3-2 y en la Figura 3-5:

7 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Tabla 3-2. Condiciones de borde e iniciales

|Nombre CB|CB aguas<br>arriba|CB aguas<br>abajo|Caudal<br>peak<br>[m3/s]|Pendiente<br>[m/m]|
|---|---|---|---|---|
|US_00|✅||1039.69|0.009|
|DS||✅|-|0.006|

Figura 3-5. Ubicación condiciones de borde

El hidrograma de crecida se presenta en la siguiente figura:

8 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 3-6. Hidrogramas de crecida US_00

## 3.4. Otras consideraciones

En todos los modelos, el flujo bidimensional se calculó empleando las ecuaciones de Saint Venant (opción

SWE-ELM en HEC-RAS 6.3). Además, el área de flujo se discretizó en celdas de 4 x 4 m y se utilizó un paso

de tiempo de 1 s ajustado en función de los números de Courant del modelo, con un Courant mínimo de 0.15

y un máximo de 0.40. El tiempo de modelación se consideró en función del tiempo de llegada al peak del

hidrograma de crecida, en particular el modelo de las OP 01 y OP 02 tiene un tiempo de modelación de 48

horas. Cabe mencionar que, como se aprecia en Figura 3-6, el hidrograma de salida no alcanza a mostrar la

crecida completa, sin embargo, sí se logra apreciar su peak y la mayor parte de la cola de salida del

hidrograma.

Adicionalmente, se consideró el refinamiento de la malla de cálculo a celdas de 1 x 1 m, en las zonas que se

muestran en la Figura 3-5 (con color rojo). El objetivo de estos refinamientos es representar de mejor forma

las características de la obra proyectada y solucionar algunas inestabilidades numéricas del modelo.

9 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

# 4. Resultados

A continuación, se presentan los resultados de profundidad y velocidad de inundación de cada modelo.

Debido a que el modelo abarca un área muy extensa, se presentan los resultados de este con una

aproximación a las obras OP 01 y OP 02, en la Sección 4.2 y la Sección 4.3, respectivamente.

## 4.1. Modelo HEC-RAS

### 4.1.1. Condición sin proyecto

Figura 4-1. Profundidad máxima. Crecida de diseño (100 años). Condición sin proyecto

10 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-2. Velocidad máxima. Crecida de diseño (100 años). Condición sin proyecto

Figura 4-3. Hidrograma a la salida del modelo. Condición sin proyecto

### 4.1.2. Condición con proyecto

11 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-4. Profundidad máxima. Crecida de diseño (100 años). Condición con proyecto

Figura 4-5. Velocidad máxima. Crecida de diseño (100 años). Condición con proyecto

12 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-6. Hidrograma a la salida del modelo. Condición con proyecto

## 4.2. Modelo OP 01

### 4.2.1. Condición sin proyecto

Figura 4-7. Profundidad máxima OP 01. Crecida de diseño (100 años). Condición sin proyecto. Incluye

líneas de flujo (color blanco)

13 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-8. Velocidad máxima OP 01. Crecida de diseño (100 años). Condición sin proyecto. Incluye líneas

de flujo (color blanco)

### 4.2.2. Condición con proyecto

Figura 4-9. Profundidad máxima OP 01. Crecida de diseño (100 años). Condición con proyecto. Incluye

líneas de flujo (color blanco)

14 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-10. Velocidad máxima OP 01. Crecida de diseño (100 años). Condición con proyecto. Incluye líneas

de flujo (color blanco)

## 4.3. Modelo OP 02

### 4.3.1. Condición sin proyecto

Figura 4-11. Profundidad máxima OP 02. Crecida de diseño (100 años). Condición sin proyecto. Incluye

líneas de flujo (color blanco)

15 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-12. Velocidad máxima OP 02. Crecida de diseño (100 años). Condición sin proyecto. Incluye líneas

de flujo (color blanco)

### 4.3.2. Condición con proyecto

Figura 4-13. Profundidad máxima OP 02. Crecida de diseño (100 años). Condición con proyecto. Incluye

líneas de flujo (color blanco)

16 Baqua Ingeniería
[www.baqua.cl](http://www.baqua.cl/)

ANEXO 2.13. MODELO HIDRÁULICO OP 01 y 02
PERMISO AMBIENTAL SECTORIAL 156

PARQUE FOTOVOLTAICO ANDINO LONGOTOMA

Figura 4-14. Velocidad máxima OP 02. Crecida de diseño (100 años). Condición con proyecto. Incluye líneas

de flujo (color blanco)

# 5. Referencias

Chow, V. T. (1994). Hidráulica de canales abiertos. Colombia: McGraw-Hill.

Chow, V. T., Maidment, D. R., & Mays, L. W. (1988). Applied hydrology. Singapore: McGraw-Hill.

HEC. (2022). HEC-RAS. Versión 6.3. HEC-RAS. Versión 6.3. Hydrologic Engineering Center. Obtenido de

https://www.hec.usace.army.mil/software/hec-ras/

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

17 Baqua Ingeniería
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
| Sin Proyecto | Representa la condición actual del cauce, en una extensión total de 3.4<br>km a lo largo del eje del Río La Ligua. | Representar<br>la<br>condición<br>actual<br>del<br>cauce |
| Con Proyecto | Representa la condición futura del cauce. Mantiene las características<br>del modelo Sin Proyecto, además de incorporar las obras proyectadas,<br>correspondiente a dos muros de gaviones, uno para cada torre (Torres<br>14 y 15), que están formados por gaviones de 2.0x1.0x1.0 m, con una<br>forma hexagonal vista en planta. | Representar<br>la<br>condición<br>futura<br>del<br>cauce |

**Tabla 3-1.: Condición del cauce para el cálculo del coeficiente de Manning con método Cowan**

| Condición del cauce | Col2 | Símbolo | Valor |
| --- | --- | --- | --- |
| Material del lecho | Tierra | n0 | 0.020 |
| Grado de irregularidad del perímetro mojado | Leve | n1 | 0.005 |
| Variación de las secciones transversales | Alternándose<br>ocasionalmente | n2 | 0.005 |
| Efecto relativo de las obstrucciones | Leve | n3 | 0.010 |
| Densidad de vegetación | Media | n4 | 0.010 |
| Sinuosidad y frecuencia de meandros | Leve | m | 1.000 |
| Coeficiente de rugosidad | Coeficiente de rugosidad | n | 0.050 |

**Tabla 3-2.: Condiciones de borde e iniciales**

| Nombre CB | CB aguas<br>arriba | CB aguas<br>abajo | Caudal<br>peak<br>[m3/s] | Pendiente<br>[m/m] |
| --- | --- | --- | --- | --- |
| US_00 | ✅ |  | 1039.69 | 0.009 |
| DS |  | ✅ | - | 0.006 |
