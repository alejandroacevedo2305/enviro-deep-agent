---
title: Sin título
author: Alberto
date: D:20240814234837-04'00'
language: es
type: manual
pages: 18
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Anexo 1.4 MEMORIA DE CÁLCULO HIDRÁULICO RÍO DIGUILLÍN
-->

### DECLARACIÓN DE IMPACTO AMBIENTAL

# Anexo 1.4 MEMORIA DE CÁLCULO HIDRÁULICO RÍO DIGUILLÍN

### PROYECTO "AMPLIACIÓN DEL VOLUMEN DE EXTRACCIÓN Y PROCESAMIENTO DE ÁRIDOS PLANTA EL CARMEN" ÁRIDOS MISAEL MAYO 2024

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

## ÍNDICE

1. INTRODUCCIÓN _______________________________________________________ 1

2. TOPOGRAFÍA__________________________________________________________ 1

3. ZONA DE ESTUDIO _____________________________________________________ 2

4. CAUDALES ASOCIADOS AL MODELO HIDRÁULICO ______________________________ 3

5. SOFTWARE DE MODELACIÓN _______________________________________________ 3

5.1 RUGOSIDADES _________________________________________________________ 3

5.1.1 RUGOSIDAD DE MANNING PARA EL LECHO DEL CAUCE _________________________ 3

5.1.2 RUGOSIDADES PLANICIES DE INUNDACIÓN__________________________________ 5

5. 2 CONSTRUCCIÓN DEL MODELO ____________________________________________ 8

5. 3 CONDICIONES DE BORDE, INICIALES E INTERNAS DE LOS MODELOS _______________ 8

5. 4 PLANES DE SIMULACIÓN ________________________________________________ 10

6. RESULTADOS ________________________________________________________ 10

6.1 SITUACIÓN ACTUAL_____________________________________________________ 10

7. ANÁLISIS, VERIFICACIONES DE LAS SIMULACIONES Y COMPARACIÓN DE RESULTADOS 13

7. 1 VELOCIDADES ________________________________________________________ 14

8. CONCLUSIONES ______________________________________________________ 15

9. BIBLIOGRAFÍA________________________________________________________ 16

## ÍNDICE DE TABLAS

Tabla 1. Resumen de caudales en modelación hidráulica_____________________________ 3
Tabla 2. Valores de rugosidad según Cowan________________________________________ 4
Tabla 3. Valores en cauce principal_______________________________________________ 5
Tabla 4. Coeficientes de Manning para corrientes naturales__________________________ 6
Tabla 5. Valores utilizados en modelo hidráulico____________________________________ 7
Tabla 6. Hidrograma asociado a la modelación_____________________________________ 9
Tabla 7. Condiciones de borde asociados a la entrada y salida de la modelación_________ 9
Tabla 8. Resumen del plan simulados en HEC-RAS__________________________________ 10

## ÍNDICE DE FIGURAS

Figura 1. Zona de estudio________________________________________________________ 2
Figura 2. Coeficiente de manning para distintas zonas del modelo______________________ 7
Figura 3. Malla modelos en HEC-RAS 6.3.1._________________________________________ 8
Figura 4. Resultados situación actual______________________________________________ 11
Figura 5. Perfil longitudinal de modelación en Río Diguillín en situación actual con Q100___ 11
Figura 6. Perfil transversal Km 0.600 de modelación en situación actual con Q100________ 12
Figura 7. Resultados para distintos caudales con periodos de retorno___________________ 13
Figura 8. Resultados Hec-Ras velocidades para Q100________________________________ 14

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

### 1. INTRODUCCIÓN

El presente estudio tiene como finalidad evaluar las zonas inundables en el sector de

emplazamiento de la planta de extracción de áridos desde pozo lastrero del Proyecto

denominado "Ampliación del volumen de extracción y procesamiento de áridos Planta El

Carmen". Para ello, primero se ha procedido a realizar una revisión de antecedentes, luego un

estudio hidrológico de la cuenca. Posteriormente con la información topográfica se procede a

modelar en 2D con el software HEC-RAS 6.3.1, para distinguir las zonas inundables y realizar el

análisis de afectación, así se define si es que el terreno donde se emplaza el Proyecto es

inundado o no.

### 2. TOPOGRAFÍA

La metodología empleada para el traslado de coordenadas y establecimiento de puntos de

referencia para el levantamiento topográfico de la zona de estudio se hizo en base a las

recomendaciones del documento “Especificaciones Técnicas Topográficas ETT-DOH”.

El instrumental utilizado para el traslado de coordenadas fue un GPS marca STONEX modelo S9

III (Tercera generación), con capacidad de mediciones diferenciales en tiempo real (RTK) con

precisión horizontal de 1cm + 1ppm (rms) y vertical de 2cm + 1ppm (rms).

Con las coordenadas del monolito obtenidas, se procedió a levantar en modo RTK, con una

tolerancia máxima de 5cm, vale decir, que si el GPS marcaba más de 5cm de error, este no

permitía guardar la medición del punto, para esto, se ubicó el receptor base en uno de los

monolitos, y con el receptor móvil, se levantó el terreno, procurando tomar los accidentes

topográficos relevantes, y en los sectores planos haciendo una cuadricula de puntos.

En los sectores donde la señal GPS no era suficiente para emplear el equipo, se procedió a

levantar con estación total Pentax R-326, con precisión angular de 6 segundos, y precisión en

medición de distancia de 5mm + 3ppm.

1

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

### 3. ZONA DE ESTUDIO

El estudio está emplazado en el Río Diguillín, donde se evaluarán 1.180 metros de Río, con una

pendiente promedio de 0.0063 m/m, además sus grados de irregularidades son moderados y

no se encuentra con obstrucciones significativas. En el entorno (Figura 1), se aprecia vegetación

estacional, con bosque en toda la ribera norte y sur del río.

Figura 1. Zona de estudio.

2

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

### 4. CAUDALES ASOCIADOS AL MODELO HIDRÁULICO

A continuación, se presenta la determinación del eje hidráulico en el río Diguillín para la zona de

estudio, con un caudal de crecida de 2, 5, 50 y 100 años de período de retorno. Se indican las

consideraciones técnicas adoptadas para su validación, así como los resultados y zona de

influencia con respecto a la zona de extracción de áridos. Los caudales para el estudio son los

siguientes:

Tabla 1. Resumen de caudales en modelación hidráulica.

|Escenario|T [años]|Caudal [m3/s]|
|---|---|---|
|Actual<br>|2|72.2|
|<br> <br>|5|101.9|
|<br> <br>|50|163.2|
|<br> <br>|100|184.6|

### 5. SOFTWARE DE MODELACIÓN

Para el presente estudio se hace uso del software HEC-RAS 6.3.1, el cual es de distribución libre,

y fue desarrollado por U.S. Army Corps of Engineers (USACE). El software permite simular el flujo

de agua, combinando modelos 1D (unidimensional) con 2D (bidimensional), o simplemente

utilizando modelos 2D; su aplicación se basa en las ecuaciones de Onda Difusiva y Saint Venant,

en donde el usuario es quien elige cual utilizar para hacer correr el modelo; las ecuaciones se

resuelven por el algoritmo de Volúmenes Finitos Implícitos [1].

Por otro lado, un modelo de tales características bidimensionales, permite definir distintos

parámetros y variables físicas del sector; entregando resultados más realistas. Luego, para el

presente estudio, se utiliza la modelación en 2D.

### 5.1 RUGOSIDADES 5.1.1 RUGOSIDAD DE MANNING PARA EL LECHO DEL CAUCE

La determinación de la rugosidad en el lecho del cauce se determinará utilizando la relación de

Cowan [2], la cual se presenta a continuación:

_n_ = ( _n_ 0 + _n_ 1 + _n_ 2 + _n_ 3 + _n_ 4 ) _m_ 5

Dónde:

3

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

_[n]_ 0
: Valor básico del coeficiente de rugosidad para un tramo recto y uniforme.

_[n]_ 1
: Incremento por irregularidades de las secciones.

#### _n_

: Incremento por variaciones de forma y dimensiones de las secciones. 2

_n_
3 : Incremento por obstrucciones.

#### [n] 4

: Incremento por vegetación en el cauce.

_m_
5 : Factor correctivo por curvas y meandros del río.

Los valores de Cowan se muestran en la siguiente Tabla 2.

Tabla 2. Valores de rugosidad según Cowan.

4

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

Conforme a la Tabla 2 y a las características propias del río, donde se determinan los valores n,

propios de la morfología, se determinarán los valores de los coeficientes adoptados con lo que

indica la Tabla 3 siguiente:

Tabla 3. Valores en cauce principal.

|Características|Descripción|Valor utilizado|
|---|---|---|
|0<br>_n_ : Valor básico ideal para mismo material|Grava Gruesa|0.028|
|1_n_ : Grado de irregularidades.|Moderado|0.01|
|2_n_ : <br>Variaciones<br>de<br>las<br>secciones<br>transversales.|Ocasionalmente<br>alternamente|0.005|
|3_n_ : Obstrucciones.|Menor|0.01|
|4_n_ : Incremento por vegetación en el cauce.|Media|0.01|
|5<br>_m_ : Factor correctivo por curvas y meandros<br>del río|Menor|0.01|

n= (n 0 + n 1 + n 2 + n 3 + n 4 )m5

n= (0.028 + 0.01 + 0.005 + 0.01 + 0.01) ∗0.01

n= 0.063

### 5.1.2 RUGOSIDADES PLANICIES DE INUNDACIÓN

Para la determinación de las rugosidades en las planicies de inundación, se utilizará la Tabla

3.707.104.A del Manual de Carreteras [3], donde indica las rugosidades para planicies de

inundación.

5

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

Tabla 4. Coeficientes de Manning para corrientes naturales.

6

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

Finalmente, las rugosidades ingresadas al modelo se muestran en la Figura 2.

Figura 2. Coeficiente de manning para distintas zonas del modelo.

Una vez obtenidos los valores de coeficiente de manning asociados a la metodología de Cowan

y Manual de Carretera se proceden a ingresar los valores al modelo hidráulico, los cuales se

muestran a continuación en la Tabla 5.

Tabla 5. Valores utilizados en modelo hidráulico.

7

|Zona inundación|Manning|
|---|---|
|Pasto|0.03|
|Boque|0.20|
|Matorrales|0.05|
|Río|0.063|

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

### 5. 2 CONSTRUCCIÓN DEL MODELO

Conforme al levantamiento topográfico del sector, se realizó la construcción del modelo. Para

ello, primeramente, se incluye la información topográfica del terreno, luego se generan los

RASTER de rugosidad que permiten hacer el enmallado, la Figura 3 muestra el enmallado para

la zona de estudio.

Entrada

Salida

Figura 3. Malla modelos en HEC-RAS 6.3.1.

### 5. 3 CONDICIONES DE BORDE, INICIALES E INTERNAS DE LOS MODELOS

Para el modelo se consideran las condiciones de borde dadas por la entrada y salida de flujo.

La entrada de flujo es asociada a un hidrograma de caudal de crecida hasta alcanzar los valores

de período de retorno de 2, 5, 50 y 100 años, lo que se muestra en la Tabla 6. Luego, se asignan

en mismo punto las pendientes de energía, las cuales se igualan a las pendientes de terreno,

los primeros 140 metros. La condición de borde para la salida de flujo es asociada a una

condición de flujo normal, por lo que se aproxima la pendiente de energía a la pendiente de

terreno existente en el sector en los últimos 140 metros (Tabla 7).

Las condiciones internas usadas para los modelos son las que traen por defecto el software, y

para el tiempo de “procesamiento” se iguala a una o dos horas, para aquellos casos donde

exista inestabilidad.

8

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

Tabla 6. Hidrograma asociado a la modelación.

|Hidrograma|Col2|
|---|---|
||_Entrada_|
|Hora|_Caudal [m3/s]_<br>|
|0:00|~~0 ~~<br>|
|1:00|~~0.1~~<br>|
|2:00|~~0.5~~<br>|
|3:00|~~1 ~~<br>|
|4:00|~~2 ~~|
|5:00|3|
|6:00|4|
|7:00|5 <br>|
|8:00|~~10~~<br>|
|9:00|~~15~~<br>|
|10:00|~~20~~<br>|
|11:00|~~25~~<br>|
|12:00|~~30~~|
|13:00|35|
|14:00|40<br>|
|15:00|~~50~~<br>|
|16:00|~~60~~<br>|
|17:00|~~72.2~~<br>|
|18:00|~~72.2~~<br>|
|19:00|~~101.9~~|
|20:00|101.9|
|21:00|163.2|
|22:00|163.2<br>|
|23:00|~~184.6~~<br>|
|24:00:00|<br>~~184.6~~|

Tabla 7. Condiciones de borde asociados a la entrada y salida de la modelación.

|Nombre Plan|Condición|
|---|---|
|Plan 01<br>|Condición entrada: pendiente de energía igual a pendiente del lecho<br>de fondo aguas arriba (if= 0.0065m/m), Condición salida: fondo<br>aguas abajo (if=0.0027m/m)|

9

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

### 5. 4 PLANES DE SIMULACIÓN

Para determinar el comportamiento de las obras proyectadas, se han establecido los siguientes

planes de modelación:

 - Situación Actual (Plan 01): Se calcula el eje hidráulico en la situación actual, con

un hidrograma que incluye el caudal con periodos de retorno de 2, 5, 50 y 100

años.

En la Tabla 8 se presentan el caso a analizar:

Tabla 8. Resumen del plan simulados en HEC-RAS.

|Nombre Plan|Escenario|Obras Incorporadas|Q [m3/s]|
|---|---|---|---|
|Plan 01|Actual|-|72.2 - 101.9 - 135 - 184.6|

### 6. RESULTADOS 6.1 SITUACIÓN ACTUAL

Este escenario corresponde a la simulación del Río Diguillín en su situación actual (Figura 4),

para un caudal de crecida con período de retorno de 100 años. Observando los resultados de la

simulación en el software Hec-Ras 6.3.1, se tiene lo siguiente:

10

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

Área extracción

de áridos

Figura 4. Resultados situación actual.

Cota agua 320.63 m

Figura 5. Perfil longitudinal de modelación en Río Diguillín en situación actual con Q100.

11

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

Figura 6. Perfil transversal Km 0.600 de modelación en situación actual con Q100.

De las Figuras 4, 5 y 6 se observan las siguientes situaciones preponderantes:

1. No existen desbordes con crecida centenaria en la zona de interés en condiciones

actuales.

2. La cota del eje hidráulico es de 320.63 m y la cota de la zona de estudio es de 326.12.

12

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

### 7. ANÁLISIS, VERIFICACIONES DE LAS SIMULACIONES Y COMPARACIÓN DE RESULTADOS

A continuación, se analizan las comparaciones en situación actual con caudales con periodo de
retorno de 2, 5, 50 y 100 años.

Figura 7. Resultados para distintos caudales con periodos de retorno.

13

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

### 7. 1 VELOCIDADES

En la figura siguiente se muestran las velocidades localizadas entregadas por la simulación en

la situación actual.

Figura 8. Resultados Hec-Ras velocidades para Q100.

De la figura anterior se observa que las velocidades máximas fluctúan entre los 2 y 3 m/s.

14

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

### 8. CONCLUSIONES

De acuerdo con los resultados de los cálculos presentados en el presente documento, es posible

concluir lo siguiente:

a) La zona de extracción de áridos no se ve afectada con la crecida centenaria, sino más

bien existe desborde en el lado norte de la ribera del río.

b) El área de inundación de encuentra aproximadamente a 25 metros de la extracción de

áridos.

WALDO LAMA TORRES

INGENIERO CIVIL AGRÍCOLA

15

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

Anexo 1.4 Memoria Cálculo Hidráulico

Proyecto "Ampliación del Volumen de Extracción y Procesamiento de Áridos Planta El Carmen"

### 9. BIBLIOGRAFÍA

La bibliografía considerada para el diseño de las obras es la siguiente:

[1]: U.S. Army Corps of Engineers, “HEC-RAS 2D Modeling User’s Manual”, 2018.

[2]: Guías Metodologicas para la presentación y revisió técnica de proyectos de modificación

de cauces natulares y artificiales, DGA 2016.

[3]: Manual de Carreteras.

16

EW Group Consultores Limitada
ewgrouplimitada@gmail.com
+56 9 3214 1193

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Resumen de caudales en modelación hidráulica.**

| Escenario | T [años] | Caudal [m3/s] |
| --- | --- | --- |
| Actual<br> | 2 | 72.2 |
| <br> <br> | 5 | 101.9 |
| <br> <br> | 50 | 163.2 |
| <br> <br> | 100 | 184.6 |

**Tabla 3.: Valores en cauce principal.**

| Características | Descripción | Valor utilizado |
| --- | --- | --- |
| 0<br>_n_ : Valor básico ideal para mismo material | Grava Gruesa | 0.028 |
| 1_n_ : Grado de irregularidades. | Moderado | 0.01 |
| 2_n_ : <br>Variaciones<br>de<br>las<br>secciones<br>transversales. | Ocasionalmente<br>alternamente | 0.005 |
| 3_n_ : Obstrucciones. | Menor | 0.01 |
| 4_n_ : Incremento por vegetación en el cauce. | Media | 0.01 |
| 5<br>_m_ : Factor correctivo por curvas y meandros<br>del río | Menor | 0.01 |

**Tabla 5.: Valores utilizados en modelo hidráulico.**

| Zona inundación | Manning |
| --- | --- |
| Pasto | 0.03 |
| Boque | 0.20 |
| Matorrales | 0.05 |
| Río | 0.063 |

**Tabla 6.: Hidrograma asociado a la modelación.**

| Hidrograma | Col2 |
| --- | --- |
|  | _Entrada_ |
| Hora | _Caudal [m3/s]_<br> |
| 0:00 | ~~0 ~~<br> |
| 1:00 | ~~0.1~~<br> |
| 2:00 | ~~0.5~~<br> |
| 3:00 | ~~1 ~~<br> |
| 4:00 | ~~2 ~~ |
| 5:00 | 3 |
| 6:00 | 4 |
| 7:00 | 5 <br> |
| 8:00 | ~~10~~<br> |
| 9:00 | ~~15~~<br> |
| 10:00 | ~~20~~<br> |
| 11:00 | ~~25~~<br> |
| 12:00 | ~~30~~ |
| 13:00 | 35 |
| 14:00 | 40<br> |
| 15:00 | ~~50~~<br> |
| 16:00 | ~~60~~<br> |
| 17:00 | ~~72.2~~<br> |
| 18:00 | ~~72.2~~<br> |
| 19:00 | ~~101.9~~ |
| 20:00 | 101.9 |
| 21:00 | 163.2 |
| 22:00 | 163.2<br> |
| 23:00 | ~~184.6~~<br> |
| 24:00:00 | <br>~~184.6~~ |

**Tabla 7.: Condiciones de borde asociados a la entrada y salida de la modelación.**

| Nombre Plan | Condición |
| --- | --- |
| Plan 01<br> | Condición entrada: pendiente de energía igual a pendiente del lecho<br>de fondo aguas arriba (if= 0.0065m/m), Condición salida: fondo<br>aguas abajo (if=0.0027m/m) |

**Tabla 8.: Resumen del plan simulados en HEC-RAS.**

| Nombre Plan | Escenario | Obras Incorporadas | Q [m3/s] |
| --- | --- | --- | --- |
| Plan 01 | Actual | - | 72.2 - 101.9 - 135 - 184.6 |
