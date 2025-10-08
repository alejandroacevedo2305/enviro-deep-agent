---
title: Sin título
author: Javiera Manetti
date: D:20231213160732-03'00'
language: es
type: report
pages: 34
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1. INTRODUCCIÓN
  - 2. OBJETIVOS
  - 3. METODOLOGÍA
  - 4. CARACTERIZACIÓN DEL ÁREA DE ESTUDIO
  - 5. ANÁLISIS HIDROLÓGICO DE LA ZONA DE ESTUDIO
  - 6. MODELACIÓN HIDRÁULICA
  - 7. RESULTADOS MODELACIÓN 1D
  - 8. CONCLUSIONES
-->

|ELABORÓ : JMM|EDICIÓN|
|---|---|
|**REVISÓ**<br>: JSI|B <br>|
|**FECHA**<br>: Noviembre - 2023<br><br><br><br>|**FECHA**<br>: Noviembre - 2023<br><br><br><br>|

**Índice**

1. INTRODUCCIÓN .................................................................................................................................................................................. 5

1.1. UBICACIÓN DEL PROYECTO .................................................................................................................................................. 5

2. OBJETIVOS .......................................................................................................................................................................................... 7

2.1. OBJETIVO GENERAL ............................................................................................................................................................... 7

2.2. OBJETIVOS ESPECÍFICOS ...................................................................................................................................................... 7

3. METODOLOGÍA ................................................................................................................................................................................... 8

3.1. VISITA A TERRENO .................................................................................................................................................................. 8

3.2. REVISIÓN DE INFORMACIÓN SECUNDARIA ......................................................................................................................... 8

3.3. TRABAJO DE GABINETE ......................................................................................................................................................... 9

3.3.1. Fotointerpretación y Análisis Hidrológico .............................................................................................................................. 9

3.3.2. Análisis Geomorfológico ........................................................................................................................................................ 9

3.3.3. Tiempo de concentración ...................................................................................................................................................... 9

3.3.4. Caudal Máximo ................................................................................................................................................................... 10

4. CARACTERIZACIÓN DEL ÁREA DE ESTUDIO ................................................................................................................................ 13

4.1. ÁREA DE INFLUENCIA ........................................................................................................................................................... 13

4.2. HIDROLOGÍA REGIONAL ....................................................................................................................................................... 14

4.3. HIDROLOGÍA LOCAL .............................................................................................................................................................. 15

4.3.1. Visita a terreno .................................................................................................................................................................... 16

4.3.2. Características de las áreas aportantes a la zona de estudio ............................................................................................. 18

4.4. CLIMATOLOGÍA DEL SECTOR .............................................................................................................................................. 20

5. ANÁLISIS HIDROLÓGICO DE LA ZONA DE ESTUDIO .................................................................................................................... 21

5.1. ANÁLISIS HIDROLÓGICO DE LA ZONA DE ESTUDIO ......................................................................................................... 21

5.1.1. Estaciones meteorológicas del sector ................................................................................................................................. 21

5.1.2. Registros de precipitaciones ............................................................................................................................................... 22

5.1.3. Análisis de frecuencias ........................................................................................................................................................ 23

5.1.4. Precipitaciones máximas ..................................................................................................................................................... 24

5.2. CAUDALES MÁXIMOS DE CRECIDA ..................................................................................................................................... 24

Contacto : contacto@emergeingenieria.cl
**1**
Teléfono : +56 9 5659 1903

6. MODELACIÓN HIDRÁULICA ............................................................................................................................................................. 26

6.1. ZONA DE ANÁLISIS ................................................................................................................................................................ 26

6.2. METODOLOGÍA MODELACIÓN 1D ........................................................................................................................................ 27

6.2.1. Características geométricas del modelo ............................................................................................................................. 27

6.2.2. Estimación del coeficiente de rugosidad ............................................................................................................................. 27

6.2.3. Características de la modelación ........................................................................................................................................ 28

7. RESULTADOS MODELACIÓN 1D ..................................................................................................................................................... 29

8. CONCLUSIONES ............................................................................................................................................................................... 33

Contacto : contacto@emergeingenieria.cl
**2**
Teléfono : +56 9 5659 1903

**Índice de figuras**

Figura 1.1. Ubicación general del proyecto ................................................................................................................................................... 5

Figura 1.2. Ubicación local del proyecto ........................................................................................................................................................ 6

Figura 4.1. Área de Influencia del Proyecto ................................................................................................................................................ 13

Figura 4.2. Hidrología regional .................................................................................................................................................................... 14

Figura 4.3. Hidrología local .......................................................................................................................................................................... 15

Figura 4.4. Ubicación de fotografías de terreno .......................................................................................................................................... 16

Figura 4.5. Áreas aportantes a la zona de estudio ...................................................................................................................................... 18

Figura 4.6. Clasificación de climas Köppen e isoyetas de precipitación de la zona de estudio .................................................................. 20

Figura 5.1. Estaciones meteorológicas cercanas al Proyecto ..................................................................................................................... 21

Figura 5.2. Análisis de frecuencia ............................................................................................................................................................... 23

Figura 6.1. Ubicación zona de análisis ........................................................................................................................................................ 26

Figura 7.1. Ubicación perfiles transversales asignados para la modelación hidráulica .............................................................................. 29

Figura 7.2. Área de inundación para T=100 años ....................................................................................................................................... 31

Figura 7.3. Área de inundación para T=150 años ....................................................................................................................................... 32

Contacto : contacto@emergeingenieria.cl
**3**
Teléfono : +56 9 5659 1903

**Índice de tablas**

Tabla 3.1. Base de datos consultadas .......................................................................................................................................................... 8

Tabla 3.2. Coeficiente de escorrentía (C) .................................................................................................................................................... 10

Tabla 4.1. Datos de las cuencas donde se ubica el Proyecto ..................................................................................................................... 14

Tabla 4.2. Set fotográfico visita a terreno .................................................................................................................................................... 17

Tabla 4.3. Parámetros morfométricos de áreas aportantes ........................................................................................................................ 19

Tabla 4.4. Resultados tiempo de concentración ......................................................................................................................................... 19

Tabla 5.1. Datos estaciones meteorológicas ............................................................................................................................................... 22

Tabla 5.2. Precipitación máxima en 24 horas ............................................................................................................................................. 22

Tabla 5.3. Prueba de bondad de ajuste Kolmogorov-Smirnov ................................................................................................................... 24

Tabla 5.4. Precipitaciones máximas diarias para distintos periodos de retorno .......................................................................................... 24

Tabla 5.5. Coeficiente de escorrentía (C) .................................................................................................................................................... 25

Tabla 5.6. Resultados de caudal máximo, Área Aportante C1 .................................................................................................................... 25

Tabla 6.1. Definición y valores para parámetros de la ecuación de Cowan ................................................................................................ 27

Tabla 6.2. Valores de parámetros y Manning obtenido mediante método de Cowan ................................................................................. 28

Tabla 7.1. Resultados modelación, quebrada Q1 ....................................................................................................................................... 30

Contacto : contacto@emergeingenieria.cl
**4**
Teléfono : +56 9 5659 1903

# 1. INTRODUCCIÓN

El Proyecto “Arena BESS” (en adelante, el “Proyecto”) está ubicado en la Región de Antofagasta, provincia de Antofagasta,

específicamente en la comuna de Taltal, al cual se accede por la Ruta 5.

La finalidad de este estudio es caracterizar la componente hidrológica del área de estudio, determinando los caudales máximos para

diferentes periodos de retorno, y posteriormente, con la modelación hidráulica, se definen las áreas de inundación de los cauces existentes

que interactúan con el Proyecto. La modelación hidráulica se realiza utilizando el software de libre acceso HEC-RAS (Hydraulic

Engineering Center - River Analysis System), desarrollado por el US Corp Engineers, el cual es aceptado en proyectos hidráulicos por la

Dirección General de Aguas (DGA) y la Dirección de Obras Hidráulicas (DOH).

## 1.1. UBICACIÓN DEL PROYECTO

El Proyecto se encuentra emplazado en la comuna de Taltal, provincia de Antofagasta, en la Región de Antofagasta. En la Figura 1.1 se

muestra la ubicación general del Proyecto y en la Figura 1.2 se muestran las partes que lo componen.

**Figura 1.1. Ubicación general del proyecto**

Contacto : contacto@emergeingenieria.cl
**5**
Teléfono : +56 9 5659 1903

**Figura 1.2. Ubicación local del proyecto**

Contacto : contacto@emergeingenieria.cl
**6**
Teléfono : +56 9 5659 1903

# 2. OBJETIVOS

## 2.1. OBJETIVO GENERAL

El presente documento tiene por finalidad elaborar la línea base de la componente hidrológica para el área de influencia del Proyecto,

considerando para su ejecución tanto la disponibilidad de información pública y bibliográfica existente, como la información recopilada

durante la visita a terreno efectuada el día 17 de junio de 2023.

## 2.2. OBJETIVOS ESPECÍFICOS

Los objetivos específicos de este informe son los siguientes:

 - Definir área de influencia de la componente hidrológica.

 - Caracterizar la hidrografía del área de estudio, tanto regional como local.

 - Caracterizar la red de drenaje local de la zona del Proyecto.

 - Caracterizar la pluviometría del área de estudio.

 - Determinar caudales máximos en la red de drenaje con mayor influencia en la zona de estudio.

 - Establecer posibles impactos del Proyecto sobre los escurrimientos existentes.

Contacto : contacto@emergeingenieria.cl
**7**
Teléfono : +56 9 5659 1903

# 3. METODOLOGÍA

A continuación, se describe la metodología empleada para el cumplimiento de cada uno de los objetivos específicos establecidos para

este estudio.

Inicialmente se realizó una caracterización hidrográfica regional del área de estudio donde se identificaron sectores hidrológicos y la

principal red hidrográfica asociada al área de estudio.

A continuación, se realizó una caracterización hidrográfica local, con el fin de identificar la red de drenaje del sector.

Posteriormente, se realizó una caracterización de la pluviometría del área donde se desarrolla el Proyecto, con el objetivo de establecer

los valores de precipitaciones para distintos periodos de retorno.

Finalmente, se realizó el cálculo de caudales máximos para diferentes periodos de retorno.

Para la elaboración del presente informe, se consideraron principalmente las siguientes actividades:

## 3.1. VISITA A TERRENO

Se efectuó una visita al área del Proyecto, donde se visualizó el contexto general de la ubicación de éste y su relación con la hidrología

del sector. Adicionalmente, se obtuvo un registro fotográfico con el fin de respaldar el trabajo de gabinete.

## 3.2. REVISIÓN DE INFORMACIÓN SECUNDARIA

Para recopilar los antecedentes necesarios para caracterizar la componente hidrológica, se consultaron las bases de datos indicadas en

la Tabla 3.1.

**Tabla 3.1. Base de datos consultadas**

|Base de datos|Información consultada|
|---|---|
|Dirección General de Aguas (DGA)|~~Antecedentes para definir la hidrología regional y local (cuencas~~<br>donde se ubica el Proyecto, red hidrográfica, revisión de estaciones<br>meteorológicas cercanas al Proyecto, obtener registros de<br>precipitaciones, revisión de metodología para determinar caudales<br>máximos de crecida)<br>|
|Dirección General de Obras Hidráulicas (DOH)<br>|~~Revisión de antecedentes para seleccionar el software a utilizar en la~~<br>modelación hidráulica<br>|
|~~Ministerio de Obras Públicas (MOP)~~|~~Determinar caudales máximos de crecida~~<br>|
|Infraestructura de Datos Geoespaciales de Chile (IDEChile)|~~Revisión de antecedentes (ubicación del Proyecto, clima, red~~<br>hidrográfica, red vial).<br>|
|Servicio de Evaluación Ambiental (SEA)|~~Revisión de antecedentes para definir el área de influencia para la~~<br>componente hidrológica.|

Contacto : contacto@emergeingenieria.cl
**8**
Teléfono : +56 9 5659 1903

|Base de datos|Información consultada|
|---|---|
|Centro de Información de Recursos Naturales (CIREN)|~~Características del área donde se ubica el Proyecto (revisión de~~<br>antecedentes).<br>|
|Instituto Geográfico Militar (IGM)|~~Cartografía IGM para definir la red hidrográfica asociada al área del~~<br>Proyecto.|

## 3.3. TRABAJO DE GABINETE

El trabajo de gabinete consideró la ejecución de las siguientes actividades:

### 3.3.1. Fotointerpretación y Análisis Hidrológico

Se revisó la carta IGM asociada al sector y el archivo vectorial _Red Hidrográfica_ (disponible en la Biblioteca del Congreso Nacional de

Chile), con el fin de identificar las posibles redes de escurrimiento y/o quebradas naturales. Adicionalmente, con el registro fotográfico de

la visita a terreno realizada, se verifica la presencia de puntos de interés en la zona de estudio.

### 3.3.2. Análisis Geomorfológico

Consiste en la identificación y caracterización de la red de drenaje del sector, y de las áreas aportantes a los cauces que la componen.

Para esto, se utilizan imágenes satelitales e información topográfica de la misión de la NASA “SRTM Worldwide Elevation Data”.

Los parámetros geomorfológicos de interés son los que se indican a continuación:

A p : Área aportante pluvial (km [2] )

L : Longitud del cauce principal (km)

H : Desnivel máximo de la cuenca (m), este se obtiene de la diferencia entre la cota máxima (Hmax) y cota mínima (Hmin) de la

cuenca en estudio.

### 3.3.3. Tiempo de concentración

La determinación del tiempo de concentración de las áreas aportantes se calculó por medio de expresiones producto de resultados

empíricos, las que se indican a continuación:

Kirpich : tt cc = 0,066 ∗
൬ [LL]

√SS

Kirpich : tt cc = 0,066 ∗
൬ [LL]

~~൰~~

0,77

California Culverts Practice : tt cc = 0,95 ∗ ቆ [LL] HH [3] [ቇ]

California Culverts Practice : tt cc = 0,95 ∗ ቆ [LL] HH [3]

0,385

Contacto : contacto@emergeingenieria.cl
**9**
Teléfono : +56 9 5659 1903

Giandotti : tt cc = [൫] [4√AA+ 1,5LL] ൫ 0,8√HH ൯ [൯]

Siempre que LL/3,6 ≥ tt cc ≥LL/(3,6 + 1,5)

Donde:

tt cc : Tiempo de concentración (horas)

LL : Longitud del cauce principal (km)

SS : Pendiente (m/m)

AA : Área pluvial aportante (km [2] )

HH : Diferencia de nivel total entre cotas extremas (m)

### 3.3.4. Caudal Máximo

La modelación hidráulica está enfocada en el polígono donde se ubican las obras y la LT, por lo que la metodología utilizada para la

estimación de caudales de crecida, considerando el análisis de una cuenca sin información fluviométrica, es la sugerida por la _Guía de_

_Presentación y Aprobación de Proyectos de Modificación de Cauce_ (DGA, 2016) y el _Manual de Carretera Volumen No3_ (MOP, 2021).

Por lo tanto, para determinar los caudales máximos, se utilizará el Método Racional para cuencas pequeñas, de acuerdo con lo indicado

en el acápite 3.702.5 del _Manual de Carreteras Volumen 3_ (MOP, 2021). Este método consta de las siguientes etapas:

**a)** **Coeficiente de escorrentía**

El coeficiente de escorrentía para distintos periodos de retorno se obtiene con lo indicado en la Tabla 3.2, de acuerdo con las

características de la ubicación de la zona de estudio.

**Tabla 3.2. Coeficiente de escorrentía (C)**

|Factor|Extremo|Alto|Normal|Bajo|
|---|---|---|---|---|
|Relieve|~~0,28-0,35~~<br>|~~0,20-0,28~~<br>|~~0,14-0,20~~<br>|~~0,08-0,14~~<br>|
|Relieve|~~Escarpado con~~<br>pendientes mayores<br>que 30 %<br>|~~Montañoso con~~<br>pendientes entre 10 y<br>30 %<br>|~~Con cerros y~~<br>pendientes entre 5 y<br>10 %<br>|~~Relativamente plano con~~<br>pendientes menores al 5 %<br>|
|Infiltración|~~0,12-0,16~~<br>|~~0,08-0,12~~<br>|~~0,06-0,08~~<br>|~~0,04-0,06~~<br>|
|Infiltración|~~Suelos rocosos, o~~<br>arcilloso con capacidad<br>de infiltración<br>despreciable<br>|~~Suelos arcillosos o~~<br>limosos con baja<br>capacidad de infiltración,<br>mal drenados<br>|~~Normales, bien~~<br>drenados, textura<br>mediana, limos<br>arenosos, suelos<br>arenosos<br>|~~Suelos profundos de arena u~~<br>otros suelos bien drenados<br>con alta capacidad de<br>infiltración<br>|
|Cobertura<br>vegetal|~~0,12-0,16~~<br>|~~0,08-0,12~~<br>|~~0,06-0,08~~<br>|~~0,04-0,06~~<br>|
|Cobertura<br>vegetal|~~Cobertura escasa,~~<br>terreno sin vegetación o<br>escasa cobertura|~~Poca vegetación terrenos~~<br>cultivados o naturales,<br>menos del 20 % del área<br>con buena cobertura<br>vegetal|~~Regular a buena; 50 %~~<br>del área con praderas<br>o bosques, no más del<br>50 % cultivado|~~Buena a excelente; 90 % del~~<br>área con praderas, bosques<br>o cobertura equivalente|

Contacto : contacto@emergeingenieria.cl
**10**
Teléfono : +56 9 5659 1903

**L**

**L**

**L**

**L**

**L**

**L**

**L**

**L**

**L**

|Factor|Extremo|Alto|Normal|Bajo|
|---|---|---|---|---|
|Almacena-<br>miento<br>superficial<br>|~~0,10-0,12~~<br>|~~0,08-0,10~~<br>|~~0,06-0,08~~<br>|~~0,04-0,06~~<br>|
|Almacena-<br>miento<br>superficial<br>|~~Despreciable, pocas~~<br>depresiones<br>superficiales sin zonas<br>húmedas<br>|~~Baja, sistema de cauces~~<br>superficiales pequeños<br>bien definidos, sin zonas<br>húmedas|~~Normal; posibilidad de~~<br>almacenamiento<br>buena, zonas<br>húmedas, pantanos,<br>lagunas y lagos|~~Capacidad alta, sistema~~<br>hidrográfico poco definido,<br>buenas planicies de<br>inundación o gran cantidad<br>de zonas húmedas, lagunas<br>o pantanos|
|~~Si T > 10 años amplificar resultado por:~~<br>T=25; C*1,10 T=50; C*1,20 T=100; C*1,25<br>|~~Si T > 10 años amplificar resultado por:~~<br>T=25; C*1,10 T=50; C*1,20 T=100; C*1,25<br>|~~Si T > 10 años amplificar resultado por:~~<br>T=25; C*1,10 T=50; C*1,20 T=100; C*1,25<br>|~~Si T > 10 años amplificar resultado por:~~<br>T=25; C*1,10 T=50; C*1,20 T=100; C*1,25<br>|~~Si T > 10 años amplificar resultado por:~~<br>T=25; C*1,10 T=50; C*1,20 T=100; C*1,25<br>|

Fuente: Tabla 3.702.503(B) del Manual de Carreteas Volumen 3 (MOP, 2021).

**b)** **Coeficiente de duración y de frecuencia**

Los coeficientes de duración y de frecuencia propuestos por Bell cumplen las siguientes relaciones:

C
tt [= (0,54tt] [0,25] [ −0,50)]

C TT = (0,21 ∗L **L** (TT) + 0,52)

Donde:

CD : Coeficiente de duración

CF : Coeficiente de frecuencia

t : Duración de la lluvia (minutos)

T : Periodo de retorno en años

**c)** **Intensidad de lluvia**

La intensidad de las precipitaciones obtenidas para el tiempo de concentración (t c ) y cada periodo de retorno se obtiene por medio de la

siguiente expresión:

**L**

TT

**L**

TT

TT = [PP] [t]

**L**

ii t

**L**

tt cc

**L**

Donde:

ii tTT : Intensidad con periodo de retorno T, asociada a una duración tc horas (mm/h)

PP tTT : Precipitación con periodo de retorno T, asociada a una duración tc horas (mm)

tt cc : Tiempo de concentración de la cuenca (h)

Contacto : contacto@emergeingenieria.cl
**11**
Teléfono : +56 9 5659 1903

**d)** **Caudal para cada periodo de retorno**

Para estimar los caudales máximos de crecida, se emplea la siguiente expresión:

TT ∗AA

QQ= [CC(TT) ∗ii] [t]

3,6

Donde:

Q : Caudal instantáneo máximo de periodo de retorno T (m [3] /s)

CC : Coeficiente de escorrentía asociada al periodo de retorno T

ii tTT : Intensidad media de lluvia asociada al periodo de retorno T y una duración igual al tiempo de concentración de la cuenca

pluvial (mm/h)

A : Área pluvial aportante (km [2] )

Contacto : contacto@emergeingenieria.cl
**12**
Teléfono : +56 9 5659 1903

# 4. CARACTERIZACIÓN DEL ÁREA DE ESTUDIO

## 4.1. ÁREA DE INFLUENCIA

De acuerdo con lo establecido por el Artículo 19o letra b.1. del Reglamento del Sistema de Evaluación de Impacto Ambiental (RSEIA), se

define y justifica el área de influencia para la componente hidrológica, considerando los impactos ambientales al recurso hídrico. El área

de influencia ha sido establecida a partir de todas las obras y/o acciones asociadas al Proyecto que, en sus distintas fases, pudiesen

afectar potencialmente a la hidrología local. De esta forma, se definió que el área de influencia comprende todas las zonas de intervención

directa en relación con la construcción y operación del Proyecto durante sus distintas fases.

Considerando lo anterior, en la Figura 4.1 se muestra el área de influencia del Proyecto.

**Figura 4.1. Área de Influencia del Proyecto**

Contacto : contacto@emergeingenieria.cl
**13**
Teléfono : +56 9 5659 1903

## 4.2. HIDROLOGÍA REGIONAL

La zona de estudio se encuentra al interior de la cuenca Costeras entre Q. la Negra y Q. Pan de Azúcar, en la subcuenca Quebradas

Entre Quebrada de Guanillos y Quebrada de Taltal, específicamente en la subsubcuenca Quebradas Entre Quebrada de Guanillos y

Quebrada de Taltal. En la Figura 4.2 se muestra el sistema de cuencas donde su ubica el Proyecto, y en la Tabla 4.1 se resume su

información principal.

**Figura 4.2. Hidrología regional**

**Tabla 4.1. Datos de las cuencas donde se ubica el Proyecto**

|Unidad|Nombre|Código|Área (km2)|
|---|---|---|---|
|~~Cuenca~~<br>|~~Costeras entre Q. la Negra y Q. Pan de Azúcar~~<br>|~~029~~<br>|~~16.897,51~~<br>|
|~~Subcuenca~~ <br>|~~Quebradas entre Quebrada de Guanillos y Quebrada de Taltal~~<br>|~~0293~~<br>|~~3.079,12~~<br>|
|~~Subsubcuenca~~|~~Quebradas entre Quebrada de Guanillos y Quebrada de Taltal~~|~~02930~~|~~3.079,12~~|

Contacto : contacto@emergeingenieria.cl
**14**
Teléfono : +56 9 5659 1903

## 4.3. HIDROLOGÍA LOCAL

Para realizar el análisis de la hidrología local se utilizó como base la cartografía IGM Oficina Alemania C-03 (código 5-04-03-0003-00), y

el archivo vectorial _Red Hidrográfica_ (disponible en la Biblioteca del Congreso Nacional de Chile).

En la Figura 4.3 se muestra la ubicación del Proyecto y los cauces identificados. De acuerdo con la carta IGM Oficina Alemania (C-03) y

el archivo vectorial _Red Hidrográfica_, no se identifican cauces que pasen por el polígono donde se ubican las obras.

**Figura 4.3. Hidrología local**

Contacto : contacto@emergeingenieria.cl
**15**
Teléfono : +56 9 5659 1903

### 4.3.1. Visita a terreno

La visita a terreno se realizó el día 17 de junio de 2023, donde se obtuvo un set de fotografías enfocadas en mostrar el área del Proyecto

y los cauces identificados.

En la Figura 4.4 se muestra la ubicación espacial de las fotografías respecto a la ubicación del Proyecto, y en la Tabla 4.2 se muestran

las fotografías obtenidas,

**Figura 4.4. Ubicación de fotografías de terreno**

Contacto : contacto@emergeingenieria.cl
**16**
Teléfono : +56 9 5659 1903

**Tabla 4.2. Set fotográfico visita a terreno**

|Fotografía 1|Fotografía 2|
|---|---|
|||
|~~Cauce identificado en el sector noreste del Proyecto.~~ <br> <br>|~~Zona sin presencia de red de drenaje, escurrimientos de tipo~~<br>laminar.<br> <br>|
|~~**Fotografía 3**~~|~~**Fotografía 4**~~|
|||
|~~Cauce identificado en zona noroeste del Proyecto.~~ <br>|~~Zona de acumulación identificada en sector sur del Proyecto.~~|

Destacar que el área presenta un drenaje con flujos de tipo laminar, donde no se identifican cauces o zonas de escurrimiento preferente.

Se identifican de igual modo, zonas bajas que actúan como zonas de retención, las cuales en periodos de precipitaciones acumulan los

escurrimientos, dejando amplias zonas con evidente sedimentación una vez que el agua es infiltrada o evaporada.

Contacto : contacto@emergeingenieria.cl
**17**
Teléfono : +56 9 5659 1903

### 4.3.2. Características del área aportante a la zona de estudio

Para la caracterización de la hidrografía local se consideró como base imágenes satelitales SRTM utilizando las herramientas hidrológicas

del software Global Mapper V20, donde con la utilización de la herramienta hidrológica se procedió a la delimitación del área aportante.

Finalmente, la delimitación del área aportante se realizó considerando como base la información topográfica disponible, la red hidrográfica

obtenida desde la cartografía que dispone la DGA y los mapas vectoriales de la Biblioteca del Congreso Nacional de Chile.

En la Figura 4.5 se muestra el área aportante definida para la zona de estudio, y en la Tabla 4.3 se resumen las principales características

del área aportante.

**Figura 4.5. Área aportante a la zona de estudio**

Contacto : contacto@emergeingenieria.cl
**18**
Teléfono : +56 9 5659 1903

**Tabla 4.3. Parámetros morfométricos del área aportante**

|Cuenca aportante|A (km2)<br>t|L (km)|H (m)<br>min|H (m)<br>máx|
|---|---|---|---|---|
|~~Área aportante C1~~|~~5,18~~|~~6,61~~|~~2.096,00~~|~~1.960,00~~|

Donde:

A t : Superficie total del área aportante (km [2] )

LL : Longitud cauce principal (km)

H min : Cota menor del área aportante (m)

H máx : Cota mayor del área aportante (m)

En la Tabla 4.4 se muestran los resultados de tiempo de concentración obtenidos con las expresiones anteriores (acápite 3.3.3). Dadas

las condiciones del terreno, para el tiempo de concentración adoptado se consideró un promedio entre los resultados obtenidos con los

métodos Kirpich y California Culverts Practice (C.C.P.).

**Tabla 4.4. Resultados tiempo de concentración**

|Cuenca|Tiempo de concentración (horas)|Col3|Col4|Col5|
|---|---|---|---|---|
|**Cuenca** <br>|~~**Kirpich**~~<br>|~~**C.C.P.**~~<br>|~~**Giandotti**~~<br>|tc~~** adoptado**~~<br>|
|~~Área aportante C1~~|~~1,27~~|~~1,27~~|~~No aplica~~|~~1,27~~|

Contacto : contacto@emergeingenieria.cl
**19**
Teléfono : +56 9 5659 1903

## 4.4. CLIMATOLOGÍA DEL SECTOR

La caracterización climática de la zona se realizó mediante la clasificación climática de Köppen, que organiza diferentes zonas

homogéneas en base a dos elementos climáticos, la temperatura del aire y la cantidad de agua disponible.

En la Figura 4.6 se muestra la clasificación para la zona de estudio, predominando exclusivamente el clima desértico frío (BWk),

encontrándose en sus cercanías una zona con clima desértico frio de lluvia invernal (BWk (s)). Al considerar el plano de isoyetas, el área

del Proyecto se encuentra entre los valores de precipitaciones medias anuales de 10 y 20 mm.

**Figura 4.6. Clasificación de climas Köppen e isoyetas de precipitación de la zona de estudio**

Contacto : contacto@emergeingenieria.cl
**20**
Teléfono : +56 9 5659 1903

# 5. ANÁLISIS HIDROLÓGICO DE LA ZONA DE ESTUDIO

## 5.1. ANÁLISIS HIDROLÓGICO DE LA ZONA DE ESTUDIO

### 5.1.1. Estaciones meteorológicas del sector

El cálculo de las precipitaciones medias y máximas se realizó verificando las estaciones meteorológicas de la DGA cercanas al lugar de

estudio, que se encuentren en estado vigente y que posean una altitud similar a la zona de estudio.

Considerando lo anterior, en la Figura 5.1 se muestra la ubicación espacial de las estaciones cercanas a la zona de estudio respecto al

área del Proyecto, y en la Tabla 5.1 se resume su información principal.

**Figura 5.1. Estaciones meteorológicas cercanas al Proyecto**

Contacto : contacto@emergeingenieria.cl
**21**
Teléfono : +56 9 5659 1903

**Tabla 5.1. Datos estaciones meteorológicas**

|Código BNA|Nombre Estación|Coordenadas<br>WGS 84 UTM 19 S|Col4|Altitud<br>(m.s.n.m.)|Fecha inicio|Estado|
|---|---|---|---|---|---|---|
|**Código BNA**<br>|**Nombre Estación**<br>|~~**Este (m)**~~<br>|~~**Norte (m)**~~<br>|~~**Norte (m)**~~<br>|~~**Norte (m)**~~<br>|~~**Norte (m)**~~<br>|
|~~02943001-2~~<br>|~~Tal-Tal~~<br>|~~350.495~~<br>|~~7.189.132~~<br>|~~9 ~~<br>|~~01-10-1971~~<br>|~~Suspendida~~<br>|
|~~02943003-9~~<br>|~~Quebrada Taltal~~<br>|~~351.156~~<br>|~~7.189.527~~<br>|~~90~~<br>|~~01-04-2016~~<br>|~~Suspendida~~<br>|
|~~02942001-7~~<br>|~~Aguas Verdes~~<br>|~~403.184~~<br>|~~7.190.296~~<br>|~~1560~~<br>|~~01-09-1987~~<br>|~~Vigente~~<br>|
|~~02943002-0~~|~~Tal-Tal (DCP)~~<br>|~~351.156~~<br>|~~7.189.527~~<br>|~~36~~<br>|~~27/04/2015~~<br>|~~Vigente~~|

Fuente: Información Oficial Hidrometeorológica y de Calidad de Aguas en Línea (DGA, 2023)

Por ser la única estación cercana al Proyecto en estado vigente y por estar ubicada en la misma cuenca hidrológica, el análisis se realizará

solo para la estación Aguas Verdes. Se descarta la utilización de la estación Tal-Tal (DCP) por contar solo con 6 años de valores

registrados (desde 2015 a 2020).

### 5.1.2. Registros de precipitaciones

En la Tabla 5.2 se muestran los valores de precipitaciones registrados por la estación Aguas Verdes, los que corresponden a 34 años de

valores registrados (desde 1987 a 2020).

**Tabla 5.2. Precipitación máxima en 24 horas**

|Año|Fecha|Precipitación (mm)|
|---|---|---|
|~~1987~~<br>|~~01/09~~<br>|~~0,00~~<br>|
|~~1988~~<br>|~~01/01~~<br>|~~0,00~~<br>|
|~~1989~~<br>|~~01/01~~<br>|~~0,00~~<br>|
|~~1990~~<br>|~~01/01~~<br>|~~0,00~~<br>|
|~~1991~~<br>|~~17/06~~<br>|~~33,60~~<br>|
|~~1992~~<br>|~~29/05~~<br>|~~2,00~~<br>|
|~~1993~~<br>|~~01/01~~<br>|~~0,00~~<br>|
|~~1994~~<br>|~~01/01~~<br>|~~0,00~~<br>|
|~~1995~~<br>|~~01/01~~<br>|~~0,00~~<br>|
|~~1996~~<br>|~~01/01~~<br>|~~0,00~~<br>|
|~~1997~~<br>|~~04/06~~<br>|~~4,00~~<br>|
|~~1998~~<br>|~~08/02~~<br>|~~3,50~~<br>|
|~~1999~~<br>|~~27/06~~<br>|~~6,50~~<br>|
|~~2000~~<br>|~~21/07~~<br>|~~2,50~~<br>|
|~~2001~~<br>|~~01/01~~<br>|~~0,00~~<br>|
|~~2002~~<br>|~~25/05~~<br>|~~5,00~~<br>|
|~~2003~~<br>|~~01/01~~<br>|~~0,00~~<br>|
|~~2004~~<br>|~~01/01~~<br>|~~0,00~~<br>|
|~~2005~~<br>|~~24/04~~<br>|~~19,50~~<br>|
|~~2006~~<br>|~~29/08~~<br>|~~31,00~~<br>|
|~~2007~~<br>|~~16/09~~<br>|~~1,00~~<br>|
|~~2008~~<br>|~~16/06~~<br>|~~1,00~~<br>|
|~~2009~~<br>|~~01/01~~<br>|~~0,00~~<br>|
|~~2010~~|~~15/05~~|~~5,00~~|

Contacto : contacto@emergeingenieria.cl
**22**
Teléfono : +56 9 5659 1903

|Año|Fecha|Precipitación (mm)|
|---|---|---|
|~~2011~~<br>|~~06/07~~<br>|~~19,50~~<br>|
|~~2012~~<br>|~~12/04~~<br>|~~10,50~~<br>|
|~~2013~~<br>|~~12/06~~<br>|~~1,50~~<br>|
|~~2014~~<br>|~~01/01~~<br>|~~0,00~~<br>|
|~~2015~~<br>|~~24/03~~<br>|~~52,00~~<br>|
|~~2016~~<br>|~~01/01~~<br>|~~0,00~~<br>|
|~~2017~~<br>|~~06/06~~<br>|~~3,00~~<br>|
|~~2018~~<br>|~~01/01~~<br>|~~0,00~~<br>|
|~~2019~~<br>|~~07/09~~<br>|~~1,00~~<br>|
|~~2020~~|~~01/01~~|~~0,00~~|

Se evidencia que las precipitaciones se concentran entre los meses de mayo a julio, y la máxima precipitación registrada ocurrió en el

mes de marzo del año 2015, llegando a 52,00 mm.

### 5.1.3. Análisis de frecuencias

Las precipitaciones máximas para distintos períodos de retorno se obtuvieron mediante un análisis de frecuencia para la curva formada

por los registros históricos de precipitación, el cual consistió en generar una curva de ajuste a la curva Weibull. Para el análisis se utilizaron

las distribuciones de probabilidad Normal, LogNormal, Exponencial, Gamma, Pearson III, Log Pearson III y Weibull.

En la Figura 5.2 se muestra gráficamente el análisis de frecuencia, y en la Tabla 5.3 se muestran los resultados de realizar la prueba de

bondad de ajuste Kolmogorov-Smirnov.

**Figura 5.2. Análisis de frecuencia**

Contacto : contacto@emergeingenieria.cl
**23**
Teléfono : +56 9 5659 1903

**Tabla 5.3. Prueba de bondad de ajuste Kolmogorov-Smirnov**

|Test Kolmogorov-Smirnov|a=1 %|a=5 %|a=10 %|Porcentaje|DMax|
|---|---|---|---|---|---|
|~~Normal~~<br>|~~Rechazo~~<br>|~~Rechazo~~<br>|~~Rechazo~~<br>|~~0,31 %~~<br>|~~0,303~~<br>|
|~~Log Normal~~<br>|~~Rechazo~~<br>|~~Rechazo~~<br>|~~Rechazo~~<br>|~~0,12 %~~<br>|~~0,324~~<br>|
|~~Exponencial~~<br>|~~Rechazo~~<br>|~~Rechazo~~<br>|~~Rechazo~~<br>|~~0,02 %~~<br>|~~0,363~~<br>|
|~~Gamma~~<br>|~~Rechazo~~<br>|~~Rechazo~~<br>|~~Rechazo~~<br>|~~0,00 %~~<br>|~~0,457~~<br>|
|~~Pearson III~~<br>|~~Rechazo~~<br>|~~Rechazo~~<br>|~~Rechazo~~<br>|~~0,01 %~~<br>|~~0,379~~<br>|
|~~Log Pearson III~~<br>|~~Rechazo~~<br>|~~Rechazo~~<br>|~~Rechazo~~<br>|~~0,00 %~~<br>|~~0,459~~<br>|
|~~Weibull~~|~~Acepto~~|~~Acepto~~|~~Acepto~~|~~43,65 %~~|~~0,144~~|

De acuerdo con los resultados anteriores, la distribución de probabilidad Weibull es la que presenta el mayor ajuste en comparación con

las demás distribuciones analizadas, por lo tanto, el set de precipitaciones será obtenido con esta distribución.

### 5.1.4. Precipitaciones máximas

En la Tabla 5.4 se muestran los valores de precipitación máxima diaria obtenidos para distintos periodos de retorno. Las precipitaciones

máximas en 24 horas se aumentaron considerando el coeficiente de corrección de 1,1 de acuerdo con lo indicado en el _Manual de_

_Carreteras Volumen N°3_ (MOP, 2021)

**Tabla 5.4. Precipitaciones máximas diarias para distintos periodos de retorno**

|Periodo de retorno, T (años)|Pp máxima 24 horas (mm)|Pp máxima diaria (mm)|
|---|---|---|
|~~2 ~~<br>|~~1,76 ~~<br>|~~1,94~~<br>|
|~~5 ~~<br>|~~8,24 ~~<br>|~~9,06~~<br>|
|~~10~~<br>|~~15,90 ~~<br>|~~17,49~~<br>|
|~~25~~<br>|~~29,40 ~~<br>|~~32,34~~<br>|
|~~50~~<br>|~~42,04 ~~<br>|~~46,64~~<br>|
|~~100~~<br>|~~56,71 ~~<br>|~~62,38~~<br>|
|~~150~~|~~66,20 ~~|~~72,82~~|

## 5.2. CAUDALES MÁXIMOS DE CRECIDA

De acuerdo con lo indicado en el acápite 3.3.4 y considerando las características de la cuenca aportante, la metodología a utilizar para la

obtención de los caudales máximos corresponde al Método Racional para cuencas pequeñas.

**a)** **Coeficiente de escorrentía**

El coeficiente de escorrentía para distintos periodos de retorno se obtiene con lo indicado en la Tabla 3.2, de acuerdo con las

características de la ubicación de la zona de estudio. En la Tabla 5.5 se muestran los valores obtenidos.

Contacto : contacto@emergeingenieria.cl
**24**
Teléfono : +56 9 5659 1903

**Tabla 5.5. Coeficiente de escorrentía (C)**

|Factor|Área Aportante C1|
|---|---|
|~~Relieve~~<br>|~~0,14~~<br>|
|~~Infiltración~~<br>|~~0,05~~<br>|
|~~Cobertura vegetal~~<br>|~~0,16~~<br>|
|~~Almacenamiento superficial~~<br>|~~0,12~~<br>|
|~~**Coeficiente Escorrentía (C)**~~|~~**0,47**~~|

**b)** **Coeficiente de duración**

Para obtener la precipitación con periodo de retorno T (en años) y duración de una hora se consideró el coeficiente de duración indicado

en la Tabla 4.3.4 del _Manual de Drenaje Urbano_ (MOP, 2013). El valor utilizado para este estudio corresponde a la ciudad de Antofagasta

y es C tt,1 hrr [=] [0,206. ]

**c)** **Caudal Máximo**

En la Tabla 5.6 se muestran los resultados obtenidos de caudales máximos, utilizando la metodología descrita anteriormente y las

precipitaciones estimadas en el acápite 5.1.4.

**Tabla 5.6. Resultados de caudal máximo, Área Aportante C1**

|Periodo de retorno, T (años)|C(T)|PPTT (mm)<br>t|iiTT (mm/h)<br>tct P|Q (m3/s)<br>máximo|
|---|---|---|---|---|
|~~2 ~~<br>|~~0,47~~<br>|~~2,62~~<br>|~~2,07~~<br>|~~1,40~~<br>|
|~~5 ~~<br>|~~0,47~~<br>|~~3,38~~<br>|~~2,67~~<br>|~~1,81~~<br>|
|~~10~~<br>|~~0,47~~<br>|~~3,96~~<br>|~~3,12~~<br>|~~2,11~~<br>|
|~~25~~<br>|~~0,52~~<br>|~~4,72~~<br>|~~3,72~~<br>|~~2,77~~<br>|
|~~50~~<br>|~~0,56~~<br>|~~5,29~~<br>|~~4,18~~<br>|~~3,39~~<br>|
|~~100~~<br>|~~0,59~~<br>|~~5,86~~<br>|~~4,63~~<br>|~~3,91~~<br>|
|~~150~~|~~0,59~~|~~6,20~~|~~4,89~~|~~4,14~~|

Contacto : contacto@emergeingenieria.cl
**25**
Teléfono : +56 9 5659 1903

# 6. MODELACIÓN HIDRÁULICA

En esta etapa se contemplan la caracterización de las condiciones hidráulicas que posee la zona de estudio. Esto se realiza por medio

de la modelación hidrodinámica del sistema en HEC-RAS V5.0.7.

## 6.1. ZONA DE ANÁLISIS

Considerando el área del Proyecto, se analiza su interacción con la lámina de inundación de los cauces identificados. Determinar las

áreas de inundación consiste en verificar la interacción de las quebradas con el área del Proyecto, lo que se analiza para un periodo de

retorno de 100 y 150 años.

En la Figura 6.1 se muestra el tramo analizado para la ubicación del proyecto y sus respectivas curvas de nivel.

**Figura 6.1. Ubicación zona de análisis**

Contacto : contacto@emergeingenieria.cl
**26**
Teléfono : +56 9 5659 1903

## 6.2. METODOLOGÍA MODELACIÓN 1D

Para definir el eje hidráulico, primero se genera un levantamiento topográfico del cauce mediante el programa Autocad Civil 3D, sobre el

levantamiento topográfico se define el trazado de cada eje de cauce y de sus perfiles transversales, para luego exportar esta información

al software de libre acceso HEC-RAS (Hydraulic Engineering Center - River Analysis System), desarrollado por el US Corp Engineers, el

cual resuelve la ecuación unidimensional del balance de energía, y en situaciones donde la superficie del agua varía rápidamente utiliza

la ecuación de momento.

Los datos requeridos para la modelación son:

1. Geometría del tramo del río por medio de secciones transversales

2. Rugosidad relativa del tramo a modelar (n de Manning)

3. Pendiente media aguas arriba y aguas abajo de la zona de interés

### 6.2.1. Características geométricas del modelo

En cuanto a la caracterización geométrica se utilizaron los levantamientos topográficos disponibles, caracterizado por medio de perfiles

transversales en sentido del escurrimiento. Los perfiles transversales fueron extraídos cada 20 m, logrando obtener una representación

adecuada de la batimetría del tramo de cauce estudiado, cada perfil cuenta con un largo variable dependiendo de la característica de las

planicies de inundación adyacentes, siempre garantizando cubrir todo el tramo del cauce inundado producto del caudal de crecida.

### 6.2.2. Estimación del coeficiente de rugosidad

El coeficiente de rugosidad para los cauces se obtuvo mediante el método de Cowan (1956), el cual estima el número de Manning a partir

de la separación de diversos factores, dado por la siguiente ecuación:

n = (n 0 + n 1 + n 2 + n 3 + n 4 ) ∗m 5

En la Tabla 6.1 se definen los parámetros y valores de dicha relación.

**Tabla 6.1. Definición y valores para parámetros de la ecuación de Cowan**

|Condiciones del canal|Col2|Valor|Col4|
|---|---|---|---|
|Material del lecho|~~Tierra~~<br>|n0|~~0,020~~<br>|
|Material del lecho|~~Roca cortada~~<br>|~~Roca cortada~~<br>|~~0,025~~<br>|
|Material del lecho|~~Grava fina~~<br>|~~Grava fina~~<br>|~~0,024~~<br>|
|Material del lecho|~~Grava gruesa~~<br>|~~Grava gruesa~~<br>|~~0,028~~<br>|
|Grado de irregularidad perímetro mojado|~~Despreciable~~<br>|n1|~~0,000~~<br>|
|Grado de irregularidad perímetro mojado|~~Leve~~<br>|~~Leve~~<br>|~~0,001-0,005~~<br>|
|Grado de irregularidad perímetro mojado|~~Moderado~~<br>|~~Moderado~~<br>|~~0,006-0,010~~<br>|
|Grado de irregularidad perímetro mojado|~~Alto~~|~~Alto~~|~~0,011-0,020~~|

Contacto : contacto@emergeingenieria.cl
**27**
Teléfono : +56 9 5659 1903

|Condiciones del canal|Col2|Valor|Col4|
|---|---|---|---|
|Variación de las secciones|~~Graduales~~<br>|n2|~~0,000~~<br>|
|Variación de las secciones|~~Alternándose ocasionalmente~~<br>|~~Alternándose ocasionalmente~~<br>|~~0,001-0,005~~<br>|
|Variación de las secciones|~~Alternándose frecuentemente~~<br>|~~Alternándose frecuentemente~~<br>|~~0,010-0,015~~<br>|
|Efecto relativo de las obstrucciones|~~Despreciable~~<br>|n3|~~0,000-0,004~~<br>|
|Efecto relativo de las obstrucciones|~~Leve~~<br>|~~Leve~~<br>|~~0,005-0,015~~<br>|
|Efecto relativo de las obstrucciones|~~Apreciable~~<br>|~~Apreciable~~<br>|~~0,020-0,030~~<br>|
|Efecto relativo de las obstrucciones|~~Alto~~<br>|~~Alto~~<br>|~~0,040-0,060~~<br>|
|Densidad de vegetación|~~Baja~~<br>|n4|~~0,005-0,010~~<br>|
|Densidad de vegetación|~~Media~~<br>|~~Media~~<br>|~~0,010-0,025~~<br>|
|Densidad de vegetación|~~Alta~~<br>|~~Alta~~<br>|~~0,025-0,050~~<br>|
|Densidad de vegetación|~~Muy alta~~<br>|~~Muy alta~~<br>|~~0,050-0,100~~<br>|
|Sinuosidad y frecuencia de meandros<br>|~~Leve~~<br>|m5 <br>|~~1,000~~<br>|
|Sinuosidad y frecuencia de meandros<br>|~~Apreciable~~<br>|~~Apreciable~~<br>|~~1,150~~<br>|
|Sinuosidad y frecuencia de meandros<br>|~~Alto~~<br>|~~Alto~~<br>|~~1,300~~|

Fuente: Tabla 3.707.104B del Manual de Carreteras Volumen 3 (MOP, 2021).

En la Tabla 6.2 se indican los valores de los parámetros y el coeficiente de rugosidad (n) determinado mediante el método de Cowan.

**Tabla 6.2. Valores de parámetros y Manning obtenido mediante método de Cowan**

|Zona|n<br>0|n<br>1|n<br>2|n<br>3|n<br>4|m<br>5|n|
|---|---|---|---|---|---|---|---|
|~~Quebrada C1~~|~~0,020~~|~~0,000~~|~~0,000~~|~~0,000~~|~~0,005~~|~~1,000~~|~~**0,025**~~|

### 6.2.3. Características de la modelación

En los tramos donde no se observa la presencia de grandes obstrucciones ni cambios bruscos en el eje del flujo, se consideran los

coeficientes de contracción y expansión C CON = 0,1 y C EXP = 0,3 sugeridos por defecto en el software HEC-RAS. Las condiciones de

borde ingresadas al modelo corresponden a la pendiente normal aguas arriba y aguas abajo, con régimen de flujo mixto.

Contacto : contacto@emergeingenieria.cl
**28**
Teléfono : +56 9 5659 1903

# 7. RESULTADOS MODELACIÓN 1D

En la Figura 7.1 se muestran los perfiles transversales realizados y su ubicación respecto al Proyecto. Para la modelación hidráulica se

ha denominado como Q1 a la quebrada asociada al área aportante C1.

Es importante destacar que las zonas que no fueron modeladas corresponden a sectores donde, con la topografía del terreno, se verifica

que no se identifica un cauce definido, por lo que corresponden a zonas bajas que actúan como zonas de retención.

**Figura 7.1. Ubicación perfiles transversales asignados para la modelación hidráulica**

Contacto : contacto@emergeingenieria.cl
**29**
Teléfono : +56 9 5659 1903

En la Tabla 7.1 se muestran los resultados obtenidos en los perfiles analizados, con los caudales para periodos de retorno de T=100 y

T=150 años.

**Tabla 7.1. Resultados modelación, quebrada Q1**

|Perfil|T = 100 años (Q = 3,91 m3/s)|Col3|Col4|Col5|Col6|T = 150 años (Q = 4,14 m3/s)|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Perfil**<br>|**Cota de**<br>**fondo**<br>**(m.s.n.m.)**<br>|**Cota de agua**<br>**(m.s.n.m.)**<br>|**Pendiente de**<br>**energía (m/m)**<br>|**Velocidad**<br>**(m/s)**<br>|**Fr**<br>|**Cota de**<br>**fondo**<br>**(m.s.n.m.)**<br>|**Cota de agua**<br>**(m.s.n.m.)**<br>|**Pendiente de**<br>**energía (m/m)**<br>|**Velocidad**<br>**(m/s)**<br>|**Fr**<br>|
|~~0 ~~<br>|~~1981,42~~<br>|~~1982,85~~<br>|~~0,018~~<br>|~~1,28~~<br>|~~1,21~~<br>|~~1981,42~~<br>|~~1982,85~~<br>|~~0,019~~<br>|~~1,31~~<br>|~~1,23~~<br>|
|~~20~~<br>|~~1981,79~~<br>|~~1983,27~~<br>|~~0,027~~<br>|~~1,46~~<br>|~~1,45~~<br>|~~1981,79~~<br>|~~1983,28~~<br>|~~0,026~~<br>|~~1,45~~<br>|~~1,42~~<br>|
|~~40~~<br>|~~1982,21~~<br>|~~1983,66~~<br>|~~0,014~~<br>|~~1,36~~<br>|~~1,09~~<br>|~~1982,21~~<br>|~~1983,67~~<br>|~~0,015~~<br>|~~1,41~~<br>|~~1,13~~<br>|
|~~60~~<br>|~~1982,67~~<br>|~~1983,95~~<br>|~~0,015~~<br>|~~1,41~~<br>|~~1,16~~<br>|~~1982,67~~<br>|~~1983,96~~<br>|~~0,014~~<br>|~~1,40~~<br>|~~1,12~~<br>|
|~~80~~<br>|~~1983,09~~<br>|~~1984,27~~<br>|~~0,019~~<br>|~~1,50~~<br>|~~1,26~~<br>|~~1983,09~~<br>|~~1984,27~~<br>|~~0,020~~<br>|~~1,56~~<br>|~~1,30~~<br>|
|~~100~~<br>|~~1983,29~~<br>|~~1984,68~~<br>|~~0,023~~<br>|~~1,48~~<br>|~~1,36~~<br>|~~1983,29~~<br>|~~1984,69~~<br>|~~0,021~~<br>|~~1,45~~<br>|~~1,30~~<br>|
|~~120~~<br>|~~1983,68~~<br>|~~1985,12~~<br>|~~0,018~~<br>|~~1,25~~<br>|~~1,18~~<br>|~~1983,68~~<br>|~~1985,12~~<br>|~~0,020~~<br>|~~1,32~~<br>|~~1,25~~<br>|
|~~140~~<br>|~~1984,11~~<br>|~~1985,57~~<br>|~~0,032~~<br>|~~1,33~~<br>|~~1,50~~<br>|~~1984,11~~<br>|~~1985,58~~<br>|~~0,026~~<br>|~~1,27~~<br>|~~1,38~~<br>|
|~~160~~<br>|~~1984,40~~<br>|~~1985,97~~<br>|~~0,013~~<br>|~~1,25~~<br>|~~1,05~~<br>|~~1984,40~~<br>|~~1985,97~~<br>|~~0,015~~<br>|~~1,35~~<br>|~~1,13~~<br>|
|~~180~~<br>|~~1984,49~~<br>|~~1986,26~~<br>|~~0,015~~<br>|~~1,16~~<br>|~~1,10~~<br>|~~1984,49~~<br>|~~1986,27~~<br>|~~0,013~~<br>|~~1,09~~<br>|~~1,01~~<br>|
|~~200~~<br>|~~1984,80~~<br>|~~1986,57~~<br>|~~0,018~~<br>|~~1,10~~<br>|~~1,14~~<br>|~~1984,80~~<br>|~~1986,57~~<br>|~~0,018~~<br>|~~1,13~~<br>|~~1,17~~<br>|
|~~220~~<br>|~~1985,29~~<br>|~~1986,92~~<br>|~~0,016~~<br>|~~0,92~~<br>|~~1,06~~<br>|~~1985,29~~<br>|~~1986,93~~<br>|~~0,016~~<br>|~~0,93~~<br>|~~1,05~~<br>|
|~~240~~<br>|~~1985,86~~<br>|~~1987,27~~<br>|~~0,019~~<br>|~~0,96~~<br>|~~1,14~~<br>|~~1985,86~~<br>|~~1987,28~~<br>|~~0,020~~<br>|~~0,98~~<br>|~~1,17~~<br>|
|~~260~~<br>|~~1986,32~~<br>|~~1987,63~~<br>|~~0,016~~<br>|~~0,89~~<br>|~~1,05~~<br>|~~1986,32~~<br>|~~1987,64~~<br>|~~0,015~~<br>|~~0,88~~<br>|~~1,03~~<br>|
|~~280~~<br>|~~1986,75~~<br>|~~1987,98~~<br>|~~0,020~~<br>|~~0,97~~<br>|~~1,15~~<br>|~~1986,75~~<br>|~~1987,98~~<br>|~~0,020~~<br>|~~0,99~~<br>|~~1,17~~<br>|
|~~300~~<br>|~~1987,37~~<br>|~~1988,33~~<br>|~~0,019~~<br>|~~1,32~~<br>|~~1,23~~<br>|~~1987,37~~<br>|~~1988,34~~<br>|~~0,019~~<br>|~~1,33~~<br>|~~1,22~~<br>|
|~~320~~<br>|~~1987,83~~<br>|~~1988,75~~<br>|~~0,022~~<br>|~~1,27~~<br>|~~1,28~~<br>|~~1987,83~~<br>|~~1988,75~~<br>|~~0,022~~<br>|~~1,30~~<br>|~~1,30~~<br>|
|~~340~~<br>|~~1988,41~~<br>|~~1989,17~~<br>|~~0,021~~<br>|~~1,33~~<br>|~~1,27~~<br>|~~1988,41~~<br>|~~1989,17~~<br>|~~0,020~~<br>|~~1,35~~<br>|~~1,27~~<br>|
|~~360~~<br>|~~1988,98~~<br>|~~1989,63~~<br>|~~0,027~~<br>|~~1,43~~<br>|~~1,43~~<br>|~~1988,98~~<br>|~~1989,63~~<br>|~~0,027~~<br>|~~1,45~~<br>|~~1,44~~<br>|
|~~380~~<br>|~~1989,55~~<br>|~~1990,08~~<br>|~~0,016~~<br>|~~1,20~~<br>|~~1,14~~<br>|~~1989,55~~<br>|~~1990,08~~<br>|~~0,016~~<br>|~~1,21~~<br>|~~1,13~~<br>|
|~~400~~<br>|~~1990,02~~<br>|~~1990,38~~<br>|~~0,013~~<br>|~~1,14~~<br>|~~1,04~~<br>|~~1990,02~~<br>|~~1990,38~~<br>|~~0,013~~<br>|~~1,16~~<br>|~~1,05~~<br>|
|~~420~~<br>|~~1990,49~~<br>|~~1990,71~~<br>|~~0,023~~<br>|~~1,17~~<br>|~~1,28~~<br>|~~1990,49~~<br>|~~1990,72~~<br>|~~0,022~~<br>|~~1,17~~<br>|~~1,26~~<br>|
|~~440~~<br>|~~1990,85~~<br>|~~1991,06~~<br>|~~0,028~~<br>|~~1,38~~<br>|~~1,43~~<br>|~~1990,85~~<br>|~~1991,06~~<br>|~~0,027~~<br>|~~1,39~~<br>|~~1,42~~<br>|
|~~460~~<br>|~~1991,33~~<br>|~~1991,53~~<br>|~~0,017~~<br>|~~0,96~~<br>|~~1,08~~<br>|~~1991,33~~<br>|~~1991,53~~<br>|~~0,017~~<br>|~~0,98~~<br>|~~1,09~~<br>|
|~~480~~<br>|~~1991,83~~<br>|~~1992,02~~<br>|~~0,046~~<br>|~~1,24~~<br>|~~1,68~~<br>|~~1991,83~~<br>|~~1992,03~~<br>|~~0,043~~<br>|~~1,22~~<br>|~~1,65~~<br>|
|~~500~~<br>|~~1992,42~~<br>|~~1992,58~~<br>|~~0,016~~<br>|~~0,86~~<br>|~~1,04~~<br>|~~1992,42~~<br>|~~1992,58~~<br>|~~0,017~~<br>|~~0,88~~<br>|~~1,06~~<br>|
|~~520~~<br>|~~1992,84~~<br>|~~1992,99~~<br>|~~0,036~~<br>|~~1,45~~<br>|~~1,61~~<br>|~~1992,84~~<br>|~~1993,00~~<br>|~~0,035~~<br>|~~1,46~~<br>|~~1,59~~<br>|
|~~540~~<br>|~~1993,34~~<br>|~~1993,55~~<br>|~~0,018~~<br>|~~0,94~~<br>|~~1,10~~<br>|~~1993,34~~<br>|~~1993,56~~<br>|~~0,018~~<br>|~~0,96~~<br>|~~1,12~~<br>|
|~~560~~<br>|~~1993,83~~<br>|~~1993,94~~<br>|~~0,022~~<br>|~~1,03~~<br>|~~1,22~~<br>|~~1993,83~~<br>|~~1993,95~~<br>|~~0,022~~<br>|~~1,05~~<br>|~~1,23~~<br>|
|~~580~~|~~1994,22~~|~~1994,34~~|~~0,017~~|~~0,94~~|~~1,09~~|~~1994,22~~|~~1994,35~~|~~0,017~~|~~0,96~~|~~1,10~~|

Finalmente, en la Figura 7.2 y Figura 7.3 se muestra el área de inundación de las quebradas y su interacción con el área del Proyecto,

para 100 y 150 años de periodos de retorno, respectivamente.

Contacto : contacto@emergeingenieria.cl
**30**
Teléfono : +56 9 5659 1903

**Figura 7.2. Área de inundación para T=100 años**

Contacto : contacto@emergeingenieria.cl
**31**
Teléfono : +56 9 5659 1903

**Figura 7.3. Área de inundación para T=150 años**

Con los resultados anteriores se observa que las estructuras 1 y 3 interactúan con el área de inundación, por lo que se recomienda la

construcción de obras de protección.

Contacto : contacto@emergeingenieria.cl
**32**
Teléfono : +56 9 5659 1903

# 8. CONCLUSIONES

 El área del proyecto presenta una escasa red de drenaje, por lo que las precipitaciones escurren preferencialmente de forma

laminar, descartándose de este modo riesgos de socavación que puedan afectar las partes del proyecto.

 Las zonas identificadas como cauce se emplazan únicamente en el trazado de la LAT y camino de acceso, y en todos los casos

se proyectan profundidades del orden de decenas de centímetros y velocidades de moderadas a bajas, por lo que el riesgo de

socavación es acotado.

 En términos generales, se puede concluir que el proyecto presenta escaso o nulo riesgo desde el punto de vista hidrológico.

 Las estructuras 1 y 3 interactúan con la potencial área de inundación, por lo que se identifica la aplicabilidad del PAS 156.

Dadas las bajas profundidades y velocidades moderadas, no se identifica en principio la necesidad de proyectar defensas que

impliquen la aplicación del PAS 157.

 Los antecedentes para el otorgamiento del PAS 156 se presentan en el Anexo 3-6 de la presente DIA.

Contacto : contacto@emergeingenieria.cl
**33**
Teléfono : +56 9 5659 1903

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3.1.: Base de datos consultadas****

| Base de datos | Información consultada |
| --- | --- |
| Dirección General de Aguas (DGA) | ~~Antecedentes para definir la hidrología regional y local (cuencas~~<br>donde se ubica el Proyecto, red hidrográfica, revisión de estaciones<br>meteorológicas cercanas al Proyecto, obtener registros de<br>precipitaciones, revisión de metodología para determinar caudales<br>máximos de crecida)<br> |
| Dirección General de Obras Hidráulicas (DOH)<br> | ~~Revisión de antecedentes para seleccionar el software a utilizar en la~~<br>modelación hidráulica<br> |
| ~~Ministerio de Obras Públicas (MOP)~~ | ~~Determinar caudales máximos de crecida~~<br> |
| Infraestructura de Datos Geoespaciales de Chile (IDEChile) | ~~Revisión de antecedentes (ubicación del Proyecto, clima, red~~<br>hidrográfica, red vial).<br> |
| Servicio de Evaluación Ambiental (SEA) | ~~Revisión de antecedentes para definir el área de influencia para la~~<br>componente hidrológica. |

**Tabla 3.2.: Coeficiente de escorrentía (C)****

| Factor | Extremo | Alto | Normal | Bajo |
| --- | --- | --- | --- | --- |
| Relieve | ~~0,28-0,35~~<br> | ~~0,20-0,28~~<br> | ~~0,14-0,20~~<br> | ~~0,08-0,14~~<br> |
| Relieve | ~~Escarpado con~~<br>pendientes mayores<br>que 30 %<br> | ~~Montañoso con~~<br>pendientes entre 10 y<br>30 %<br> | ~~Con cerros y~~<br>pendientes entre 5 y<br>10 %<br> | ~~Relativamente plano con~~<br>pendientes menores al 5 %<br> |
| Infiltración | ~~0,12-0,16~~<br> | ~~0,08-0,12~~<br> | ~~0,06-0,08~~<br> | ~~0,04-0,06~~<br> |
| Infiltración | ~~Suelos rocosos, o~~<br>arcilloso con capacidad<br>de infiltración<br>despreciable<br> | ~~Suelos arcillosos o~~<br>limosos con baja<br>capacidad de infiltración,<br>mal drenados<br> | ~~Normales, bien~~<br>drenados, textura<br>mediana, limos<br>arenosos, suelos<br>arenosos<br> | ~~Suelos profundos de arena u~~<br>otros suelos bien drenados<br>con alta capacidad de<br>infiltración<br> |
| Cobertura<br>vegetal | ~~0,12-0,16~~<br> | ~~0,08-0,12~~<br> | ~~0,06-0,08~~<br> | ~~0,04-0,06~~<br> |
| Cobertura<br>vegetal | ~~Cobertura escasa,~~<br>terreno sin vegetación o<br>escasa cobertura | ~~Poca vegetación terrenos~~<br>cultivados o naturales,<br>menos del 20 % del área<br>con buena cobertura<br>vegetal | ~~Regular a buena; 50 %~~<br>del área con praderas<br>o bosques, no más del<br>50 % cultivado | ~~Buena a excelente; 90 % del~~<br>área con praderas, bosques<br>o cobertura equivalente |

**Tabla 4.1.: Datos de las cuencas donde se ubica el Proyecto****

| Unidad | Nombre | Código | Área (km2) |
| --- | --- | --- | --- |
| ~~Cuenca~~<br> | ~~Costeras entre Q. la Negra y Q. Pan de Azúcar~~<br> | ~~029~~<br> | ~~16.897,51~~<br> |
| ~~Subcuenca~~ <br> | ~~Quebradas entre Quebrada de Guanillos y Quebrada de Taltal~~<br> | ~~0293~~<br> | ~~3.079,12~~<br> |
| ~~Subsubcuenca~~ | ~~Quebradas entre Quebrada de Guanillos y Quebrada de Taltal~~ | ~~02930~~ | ~~3.079,12~~ |

**Tabla 4.2.: Set fotográfico visita a terreno****

| Fotografía 1 | Fotografía 2 |
| --- | --- |
|  |  |
| ~~Cauce identificado en el sector noreste del Proyecto.~~ <br> <br> | ~~Zona sin presencia de red de drenaje, escurrimientos de tipo~~<br>laminar.<br> <br> |
| ~~**Fotografía 3**~~ | ~~**Fotografía 4**~~ |
|  |  |
| ~~Cauce identificado en zona noroeste del Proyecto.~~ <br> | ~~Zona de acumulación identificada en sector sur del Proyecto.~~ |

**Tabla 4.3.: Parámetros morfométricos del área aportante****

| Cuenca aportante | A (km2)<br>t | L (km) | H (m)<br>min | H (m)<br>máx |
| --- | --- | --- | --- | --- |
| ~~Área aportante C1~~ | ~~5,18~~ | ~~6,61~~ | ~~2.096,00~~ | ~~1.960,00~~ |

**Tabla 4.4.: Resultados tiempo de concentración****

| Cuenca | Tiempo de concentración (horas) | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Cuenca** <br> | ~~**Kirpich**~~<br> | ~~**C.C.P.**~~<br> | ~~**Giandotti**~~<br> | tc~~** adoptado**~~<br> |
| ~~Área aportante C1~~ | ~~1,27~~ | ~~1,27~~ | ~~No aplica~~ | ~~1,27~~ |

**Tabla 5.1.: Datos estaciones meteorológicas****

| Código BNA | Nombre Estación | Coordenadas<br>WGS 84 UTM 19 S | Col4 | Altitud<br>(m.s.n.m.) | Fecha inicio | Estado |
| --- | --- | --- | --- | --- | --- | --- |
| **Código BNA**<br> | **Nombre Estación**<br> | ~~**Este (m)**~~<br> | ~~**Norte (m)**~~<br> | ~~**Norte (m)**~~<br> | ~~**Norte (m)**~~<br> | ~~**Norte (m)**~~<br> |
| ~~02943001-2~~<br> | ~~Tal-Tal~~<br> | ~~350.495~~<br> | ~~7.189.132~~<br> | ~~9 ~~<br> | ~~01-10-1971~~<br> | ~~Suspendida~~<br> |
| ~~02943003-9~~<br> | ~~Quebrada Taltal~~<br> | ~~351.156~~<br> | ~~7.189.527~~<br> | ~~90~~<br> | ~~01-04-2016~~<br> | ~~Suspendida~~<br> |
| ~~02942001-7~~<br> | ~~Aguas Verdes~~<br> | ~~403.184~~<br> | ~~7.190.296~~<br> | ~~1560~~<br> | ~~01-09-1987~~<br> | ~~Vigente~~<br> |
| ~~02943002-0~~ | ~~Tal-Tal (DCP)~~<br> | ~~351.156~~<br> | ~~7.189.527~~<br> | ~~36~~<br> | ~~27/04/2015~~<br> | ~~Vigente~~ |

**Tabla 5.2.: Precipitación máxima en 24 horas****

| Año | Fecha | Precipitación (mm) |
| --- | --- | --- |
| ~~1987~~<br> | ~~01/09~~<br> | ~~0,00~~<br> |
| ~~1988~~<br> | ~~01/01~~<br> | ~~0,00~~<br> |
| ~~1989~~<br> | ~~01/01~~<br> | ~~0,00~~<br> |
| ~~1990~~<br> | ~~01/01~~<br> | ~~0,00~~<br> |
| ~~1991~~<br> | ~~17/06~~<br> | ~~33,60~~<br> |
| ~~1992~~<br> | ~~29/05~~<br> | ~~2,00~~<br> |
| ~~1993~~<br> | ~~01/01~~<br> | ~~0,00~~<br> |
| ~~1994~~<br> | ~~01/01~~<br> | ~~0,00~~<br> |
| ~~1995~~<br> | ~~01/01~~<br> | ~~0,00~~<br> |
| ~~1996~~<br> | ~~01/01~~<br> | ~~0,00~~<br> |
| ~~1997~~<br> | ~~04/06~~<br> | ~~4,00~~<br> |
| ~~1998~~<br> | ~~08/02~~<br> | ~~3,50~~<br> |
| ~~1999~~<br> | ~~27/06~~<br> | ~~6,50~~<br> |
| ~~2000~~<br> | ~~21/07~~<br> | ~~2,50~~<br> |
| ~~2001~~<br> | ~~01/01~~<br> | ~~0,00~~<br> |
| ~~2002~~<br> | ~~25/05~~<br> | ~~5,00~~<br> |
| ~~2003~~<br> | ~~01/01~~<br> | ~~0,00~~<br> |
| ~~2004~~<br> | ~~01/01~~<br> | ~~0,00~~<br> |
| ~~2005~~<br> | ~~24/04~~<br> | ~~19,50~~<br> |
| ~~2006~~<br> | ~~29/08~~<br> | ~~31,00~~<br> |
| ~~2007~~<br> | ~~16/09~~<br> | ~~1,00~~<br> |
| ~~2008~~<br> | ~~16/06~~<br> | ~~1,00~~<br> |
| ~~2009~~<br> | ~~01/01~~<br> | ~~0,00~~<br> |
| ~~2010~~ | ~~15/05~~ | ~~5,00~~ |

**Tabla 5.3.: Prueba de bondad de ajuste Kolmogorov-Smirnov****

| Test Kolmogorov-Smirnov | a=1 % | a=5 % | a=10 % | Porcentaje | DMax |
| --- | --- | --- | --- | --- | --- |
| ~~Normal~~<br> | ~~Rechazo~~<br> | ~~Rechazo~~<br> | ~~Rechazo~~<br> | ~~0,31 %~~<br> | ~~0,303~~<br> |
| ~~Log Normal~~<br> | ~~Rechazo~~<br> | ~~Rechazo~~<br> | ~~Rechazo~~<br> | ~~0,12 %~~<br> | ~~0,324~~<br> |
| ~~Exponencial~~<br> | ~~Rechazo~~<br> | ~~Rechazo~~<br> | ~~Rechazo~~<br> | ~~0,02 %~~<br> | ~~0,363~~<br> |
| ~~Gamma~~<br> | ~~Rechazo~~<br> | ~~Rechazo~~<br> | ~~Rechazo~~<br> | ~~0,00 %~~<br> | ~~0,457~~<br> |
| ~~Pearson III~~<br> | ~~Rechazo~~<br> | ~~Rechazo~~<br> | ~~Rechazo~~<br> | ~~0,01 %~~<br> | ~~0,379~~<br> |
| ~~Log Pearson III~~<br> | ~~Rechazo~~<br> | ~~Rechazo~~<br> | ~~Rechazo~~<br> | ~~0,00 %~~<br> | ~~0,459~~<br> |
| ~~Weibull~~ | ~~Acepto~~ | ~~Acepto~~ | ~~Acepto~~ | ~~43,65 %~~ | ~~0,144~~ |

**Tabla 5.4.: Precipitaciones máximas diarias para distintos periodos de retorno****

| Periodo de retorno, T (años) | Pp máxima 24 horas (mm) | Pp máxima diaria (mm) |
| --- | --- | --- |
| ~~2 ~~<br> | ~~1,76 ~~<br> | ~~1,94~~<br> |
| ~~5 ~~<br> | ~~8,24 ~~<br> | ~~9,06~~<br> |
| ~~10~~<br> | ~~15,90 ~~<br> | ~~17,49~~<br> |
| ~~25~~<br> | ~~29,40 ~~<br> | ~~32,34~~<br> |
| ~~50~~<br> | ~~42,04 ~~<br> | ~~46,64~~<br> |
| ~~100~~<br> | ~~56,71 ~~<br> | ~~62,38~~<br> |
| ~~150~~ | ~~66,20 ~~ | ~~72,82~~ |

**Tabla 5.5.: Coeficiente de escorrentía (C)****

| Factor | Área Aportante C1 |
| --- | --- |
| ~~Relieve~~<br> | ~~0,14~~<br> |
| ~~Infiltración~~<br> | ~~0,05~~<br> |
| ~~Cobertura vegetal~~<br> | ~~0,16~~<br> |
| ~~Almacenamiento superficial~~<br> | ~~0,12~~<br> |
| ~~**Coeficiente Escorrentía (C)**~~ | ~~**0,47**~~ |

**Tabla 5.6.: Resultados de caudal máximo, Área Aportante C1****

| Periodo de retorno, T (años) | C(T) | PPTT (mm)<br>t | iiTT (mm/h)<br>tct P | Q (m3/s)<br>máximo |
| --- | --- | --- | --- | --- |
| ~~2 ~~<br> | ~~0,47~~<br> | ~~2,62~~<br> | ~~2,07~~<br> | ~~1,40~~<br> |
| ~~5 ~~<br> | ~~0,47~~<br> | ~~3,38~~<br> | ~~2,67~~<br> | ~~1,81~~<br> |
| ~~10~~<br> | ~~0,47~~<br> | ~~3,96~~<br> | ~~3,12~~<br> | ~~2,11~~<br> |
| ~~25~~<br> | ~~0,52~~<br> | ~~4,72~~<br> | ~~3,72~~<br> | ~~2,77~~<br> |
| ~~50~~<br> | ~~0,56~~<br> | ~~5,29~~<br> | ~~4,18~~<br> | ~~3,39~~<br> |
| ~~100~~<br> | ~~0,59~~<br> | ~~5,86~~<br> | ~~4,63~~<br> | ~~3,91~~<br> |
| ~~150~~ | ~~0,59~~ | ~~6,20~~ | ~~4,89~~ | ~~4,14~~ |

**Tabla 6.1.: Definición y valores para parámetros de la ecuación de Cowan****

| Condiciones del canal | Col2 | Valor | Col4 |
| --- | --- | --- | --- |
| Material del lecho | ~~Tierra~~<br> | n0 | ~~0,020~~<br> |
| Material del lecho | ~~Roca cortada~~<br> | ~~Roca cortada~~<br> | ~~0,025~~<br> |
| Material del lecho | ~~Grava fina~~<br> | ~~Grava fina~~<br> | ~~0,024~~<br> |
| Material del lecho | ~~Grava gruesa~~<br> | ~~Grava gruesa~~<br> | ~~0,028~~<br> |
| Grado de irregularidad perímetro mojado | ~~Despreciable~~<br> | n1 | ~~0,000~~<br> |
| Grado de irregularidad perímetro mojado | ~~Leve~~<br> | ~~Leve~~<br> | ~~0,001-0,005~~<br> |
| Grado de irregularidad perímetro mojado | ~~Moderado~~<br> | ~~Moderado~~<br> | ~~0,006-0,010~~<br> |
| Grado de irregularidad perímetro mojado | ~~Alto~~ | ~~Alto~~ | ~~0,011-0,020~~ |

**Tabla 6.2.: Valores de parámetros y Manning obtenido mediante método de Cowan****

| Zona | n<br>0 | n<br>1 | n<br>2 | n<br>3 | n<br>4 | m<br>5 | n |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ~~Quebrada C1~~ | ~~0,020~~ | ~~0,000~~ | ~~0,000~~ | ~~0,000~~ | ~~0,005~~ | ~~1,000~~ | ~~**0,025**~~ |

**Tabla 7.1.: Resultados modelación, quebrada Q1****

| Perfil | T = 100 años (Q = 3,91 m3/s) | Col3 | Col4 | Col5 | Col6 | T = 150 años (Q = 4,14 m3/s) | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Perfil**<br> | **Cota de**<br>**fondo**<br>**(m.s.n.m.)**<br> | **Cota de agua**<br>**(m.s.n.m.)**<br> | **Pendiente de**<br>**energía (m/m)**<br> | **Velocidad**<br>**(m/s)**<br> | **Fr**<br> | **Cota de**<br>**fondo**<br>**(m.s.n.m.)**<br> | **Cota de agua**<br>**(m.s.n.m.)**<br> | **Pendiente de**<br>**energía (m/m)**<br> | **Velocidad**<br>**(m/s)**<br> | **Fr**<br> |
| ~~0 ~~<br> | ~~1981,42~~<br> | ~~1982,85~~<br> | ~~0,018~~<br> | ~~1,28~~<br> | ~~1,21~~<br> | ~~1981,42~~<br> | ~~1982,85~~<br> | ~~0,019~~<br> | ~~1,31~~<br> | ~~1,23~~<br> |
| ~~20~~<br> | ~~1981,79~~<br> | ~~1983,27~~<br> | ~~0,027~~<br> | ~~1,46~~<br> | ~~1,45~~<br> | ~~1981,79~~<br> | ~~1983,28~~<br> | ~~0,026~~<br> | ~~1,45~~<br> | ~~1,42~~<br> |
| ~~40~~<br> | ~~1982,21~~<br> | ~~1983,66~~<br> | ~~0,014~~<br> | ~~1,36~~<br> | ~~1,09~~<br> | ~~1982,21~~<br> | ~~1983,67~~<br> | ~~0,015~~<br> | ~~1,41~~<br> | ~~1,13~~<br> |
| ~~60~~<br> | ~~1982,67~~<br> | ~~1983,95~~<br> | ~~0,015~~<br> | ~~1,41~~<br> | ~~1,16~~<br> | ~~1982,67~~<br> | ~~1983,96~~<br> | ~~0,014~~<br> | ~~1,40~~<br> | ~~1,12~~<br> |
| ~~80~~<br> | ~~1983,09~~<br> | ~~1984,27~~<br> | ~~0,019~~<br> | ~~1,50~~<br> | ~~1,26~~<br> | ~~1983,09~~<br> | ~~1984,27~~<br> | ~~0,020~~<br> | ~~1,56~~<br> | ~~1,30~~<br> |
| ~~100~~<br> | ~~1983,29~~<br> | ~~1984,68~~<br> | ~~0,023~~<br> | ~~1,48~~<br> | ~~1,36~~<br> | ~~1983,29~~<br> | ~~1984,69~~<br> | ~~0,021~~<br> | ~~1,45~~<br> | ~~1,30~~<br> |
| ~~120~~<br> | ~~1983,68~~<br> | ~~1985,12~~<br> | ~~0,018~~<br> | ~~1,25~~<br> | ~~1,18~~<br> | ~~1983,68~~<br> | ~~1985,12~~<br> | ~~0,020~~<br> | ~~1,32~~<br> | ~~1,25~~<br> |
| ~~140~~<br> | ~~1984,11~~<br> | ~~1985,57~~<br> | ~~0,032~~<br> | ~~1,33~~<br> | ~~1,50~~<br> | ~~1984,11~~<br> | ~~1985,58~~<br> | ~~0,026~~<br> | ~~1,27~~<br> | ~~1,38~~<br> |
| ~~160~~<br> | ~~1984,40~~<br> | ~~1985,97~~<br> | ~~0,013~~<br> | ~~1,25~~<br> | ~~1,05~~<br> | ~~1984,40~~<br> | ~~1985,97~~<br> | ~~0,015~~<br> | ~~1,35~~<br> | ~~1,13~~<br> |
| ~~180~~<br> | ~~1984,49~~<br> | ~~1986,26~~<br> | ~~0,015~~<br> | ~~1,16~~<br> | ~~1,10~~<br> | ~~1984,49~~<br> | ~~1986,27~~<br> | ~~0,013~~<br> | ~~1,09~~<br> | ~~1,01~~<br> |
| ~~200~~<br> | ~~1984,80~~<br> | ~~1986,57~~<br> | ~~0,018~~<br> | ~~1,10~~<br> | ~~1,14~~<br> | ~~1984,80~~<br> | ~~1986,57~~<br> | ~~0,018~~<br> | ~~1,13~~<br> | ~~1,17~~<br> |
| ~~220~~<br> | ~~1985,29~~<br> | ~~1986,92~~<br> | ~~0,016~~<br> | ~~0,92~~<br> | ~~1,06~~<br> | ~~1985,29~~<br> | ~~1986,93~~<br> | ~~0,016~~<br> | ~~0,93~~<br> | ~~1,05~~<br> |
| ~~240~~<br> | ~~1985,86~~<br> | ~~1987,27~~<br> | ~~0,019~~<br> | ~~0,96~~<br> | ~~1,14~~<br> | ~~1985,86~~<br> | ~~1987,28~~<br> | ~~0,020~~<br> | ~~0,98~~<br> | ~~1,17~~<br> |
| ~~260~~<br> | ~~1986,32~~<br> | ~~1987,63~~<br> | ~~0,016~~<br> | ~~0,89~~<br> | ~~1,05~~<br> | ~~1986,32~~<br> | ~~1987,64~~<br> | ~~0,015~~<br> | ~~0,88~~<br> | ~~1,03~~<br> |
| ~~280~~<br> | ~~1986,75~~<br> | ~~1987,98~~<br> | ~~0,020~~<br> | ~~0,97~~<br> | ~~1,15~~<br> | ~~1986,75~~<br> | ~~1987,98~~<br> | ~~0,020~~<br> | ~~0,99~~<br> | ~~1,17~~<br> |
| ~~300~~<br> | ~~1987,37~~<br> | ~~1988,33~~<br> | ~~0,019~~<br> | ~~1,32~~<br> | ~~1,23~~<br> | ~~1987,37~~<br> | ~~1988,34~~<br> | ~~0,019~~<br> | ~~1,33~~<br> | ~~1,22~~<br> |
| ~~320~~<br> | ~~1987,83~~<br> | ~~1988,75~~<br> | ~~0,022~~<br> | ~~1,27~~<br> | ~~1,28~~<br> | ~~1987,83~~<br> | ~~1988,75~~<br> | ~~0,022~~<br> | ~~1,30~~<br> | ~~1,30~~<br> |
| ~~340~~<br> | ~~1988,41~~<br> | ~~1989,17~~<br> | ~~0,021~~<br> | ~~1,33~~<br> | ~~1,27~~<br> | ~~1988,41~~<br> | ~~1989,17~~<br> | ~~0,020~~<br> | ~~1,35~~<br> | ~~1,27~~<br> |
| ~~360~~<br> | ~~1988,98~~<br> | ~~1989,63~~<br> | ~~0,027~~<br> | ~~1,43~~<br> | ~~1,43~~<br> | ~~1988,98~~<br> | ~~1989,63~~<br> | ~~0,027~~<br> | ~~1,45~~<br> | ~~1,44~~<br> |
| ~~380~~<br> | ~~1989,55~~<br> | ~~1990,08~~<br> | ~~0,016~~<br> | ~~1,20~~<br> | ~~1,14~~<br> | ~~1989,55~~<br> | ~~1990,08~~<br> | ~~0,016~~<br> | ~~1,21~~<br> | ~~1,13~~<br> |
| ~~400~~<br> | ~~1990,02~~<br> | ~~1990,38~~<br> | ~~0,013~~<br> | ~~1,14~~<br> | ~~1,04~~<br> | ~~1990,02~~<br> | ~~1990,38~~<br> | ~~0,013~~<br> | ~~1,16~~<br> | ~~1,05~~<br> |
| ~~420~~<br> | ~~1990,49~~<br> | ~~1990,71~~<br> | ~~0,023~~<br> | ~~1,17~~<br> | ~~1,28~~<br> | ~~1990,49~~<br> | ~~1990,72~~<br> | ~~0,022~~<br> | ~~1,17~~<br> | ~~1,26~~<br> |
| ~~440~~<br> | ~~1990,85~~<br> | ~~1991,06~~<br> | ~~0,028~~<br> | ~~1,38~~<br> | ~~1,43~~<br> | ~~1990,85~~<br> | ~~1991,06~~<br> | ~~0,027~~<br> | ~~1,39~~<br> | ~~1,42~~<br> |
| ~~460~~<br> | ~~1991,33~~<br> | ~~1991,53~~<br> | ~~0,017~~<br> | ~~0,96~~<br> | ~~1,08~~<br> | ~~1991,33~~<br> | ~~1991,53~~<br> | ~~0,017~~<br> | ~~0,98~~<br> | ~~1,09~~<br> |
| ~~480~~<br> | ~~1991,83~~<br> | ~~1992,02~~<br> | ~~0,046~~<br> | ~~1,24~~<br> | ~~1,68~~<br> | ~~1991,83~~<br> | ~~1992,03~~<br> | ~~0,043~~<br> | ~~1,22~~<br> | ~~1,65~~<br> |
| ~~500~~<br> | ~~1992,42~~<br> | ~~1992,58~~<br> | ~~0,016~~<br> | ~~0,86~~<br> | ~~1,04~~<br> | ~~1992,42~~<br> | ~~1992,58~~<br> | ~~0,017~~<br> | ~~0,88~~<br> | ~~1,06~~<br> |
| ~~520~~<br> | ~~1992,84~~<br> | ~~1992,99~~<br> | ~~0,036~~<br> | ~~1,45~~<br> | ~~1,61~~<br> | ~~1992,84~~<br> | ~~1993,00~~<br> | ~~0,035~~<br> | ~~1,46~~<br> | ~~1,59~~<br> |
| ~~540~~<br> | ~~1993,34~~<br> | ~~1993,55~~<br> | ~~0,018~~<br> | ~~0,94~~<br> | ~~1,10~~<br> | ~~1993,34~~<br> | ~~1993,56~~<br> | ~~0,018~~<br> | ~~0,96~~<br> | ~~1,12~~<br> |
| ~~560~~<br> | ~~1993,83~~<br> | ~~1993,94~~<br> | ~~0,022~~<br> | ~~1,03~~<br> | ~~1,22~~<br> | ~~1993,83~~<br> | ~~1993,95~~<br> | ~~0,022~~<br> | ~~1,05~~<br> | ~~1,23~~<br> |
| ~~580~~ | ~~1994,22~~ | ~~1994,34~~ | ~~0,017~~ | ~~0,94~~ | ~~1,09~~ | ~~1994,22~~ | ~~1994,35~~ | ~~0,017~~ | ~~0,96~~ | ~~1,10~~ |
