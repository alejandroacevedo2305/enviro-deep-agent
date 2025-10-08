---
title: INFORME DE MODELACION DE EMISIONES ATMOSFERICAS
author: IGNACIO GOIC
date: D:20210908175249-03'00'
language: es
type: report
pages: 10
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1 INTRODUCCION
  - 2 AREA DE INFLUENCIA
  - 3 MODELACIÓN DE CONTAMINANTES
  - 4 CONCLUSIONES
  - 5 BIBLIOGRAFÍA
-->

_Nueva Planta Tratamiento Riles y Actualización Bodega de Vinos, Planta Panquehue_

**INDICE GENERAL**

**1** **INTRODUCCION** **3**

**2** **AREA DE INFLUENCIA** **4**

**3** **MODELACIÓN DE CONTAMINANTES** **6**

**3.1** **PARÁMETROS DE INGRESO** **7**
**3.2** **RESULTADOS DE LA MODELACIÓN** **8**

**4** **CONCLUSIONES** **10**

**5** **BIBLIOGRAFÍA** **10**

Informe de Calidad del Aire Pág. 2

_Nueva Planta Tratamiento Riles y Actualización Bodega de Vinos, Planta Panquehue_

# 1 INTRODUCCION

El proyecto en evaluación se ubica en la comuna de Panquehue, Provincia de San Felipe, Región de
Valparaíso, tal como se muestra en la siguiente figura.

**Figura 1. Ubicación proyecto.**

Proyecto

El presente informe corresponde a la modelación de dispersión y depositación de material particulado
total, respirable y fino, debido a las emisiones generadas por la construcción y operación del proyecto
sometido a evaluación.

La modelación se realizará con un modelo simplificado, inicialmente para descartar la necesidad de
realizar un estudio mas acabado, tal como se menciona en la “Guía para el uso de modelos de calidad
del aire en el SEIA”, publicada por el Servicio de Evaluación Ambiental en 2012. En caso de que el
impacto sea de mayor envergadura, se realizará una modelación más compleja.

Informe de Calidad del Aire Pág. 3

_Nueva Planta Tratamiento Riles y Actualización Bodega de Vinos, Planta Panquehue_

# 2 AREA DE INFLUENCIA

De acuerdo con la definición indicada en la letra a), artículo 2, del RSEIA, el área de influencia de un
Proyecto corresponde “al área o espacio geográfico, cuyos atributos, elementos naturales o
socioculturales deben ser considerados con la finalidad de definir si el Proyecto o actividad genera o
presenta alguno de los efectos, características o circunstancias del artículo 11 de la Ley, o bien para
justificar la inexistencia de dichos efectos, características o circunstancias”.

En este marco, el área de influencia de cada componente ambiental ha considerado la superficie donde
se prevea que el Proyecto podría generar eventualmente algún “Efecto Adverso Significativo sobre la
cantidad y calidad de los recursos naturales renovables, incluidos, suelo, agua y aire”. Para definir dicha
área, se ha tenido en consideración lo siguiente:

- Las características del Proyecto;

- El emplazamiento de las partes del Proyecto, obras o acciones;

- Las etapas del Proyecto (construcción y operación);

- Las características del medio en que se emplaza el Proyecto;

- Las emisiones, efluentes o residuos generados por el Proyecto, que pudieran afectar el medio
ambiente.

Por su parte, la letra d) del artículo 18 del RSEIA, señala que el área de influencia debe ser determinada
y justificada para cada elemento afectado del medio ambiente, tomando en consideración los impactos
ambientales potencialmente significativos sobre ellos, así como el espacio geográfico en el cual se
emplazarán las partes, obras y/o acciones del Proyecto.

Particularmente para la componente Calidad del Aire y siguiendo el lineamiento de la “Guía para la
Descripción de la Calidad del Aire en el Área de Influencia de Proyectos que Ingresan al SEIA”, se
determina que, dada la naturaleza de las emisiones del Proyecto, estas son de rápida dispersión y
decantamiento, y también por la geografía del área del Proyecto.

En la comuna de Panquehue, el proyecto se encuentra a 3 km al sur de la Ruta 60, en una zona
dominada por predios agrícolas y algunas casas alrededor del predio del proyecto.

Los principales efectos potenciales de las actividades del Proyecto sobre la calidad del aire son el
deterioro temporal por emisiones de material particulado y gases de combustión, sobre las áreas de
trabajo y efectos sobre las poblaciones cercanas durante la etapa de construcción. Éstas son de
carácter puntual ya que se concentran en la zona del Proyecto u obras y originarán la emisión de gases
de combustión y material particulado procedente del uso y tránsito de maquinaria, equipos y camiones.

Por todo lo anterior, el área de influencia se determina como un área circular con el proyecto en el
centro y un radio de 1 km.

Informe de Calidad del Aire Pág. 4

_Nueva Planta Tratamiento Riles y Actualización Bodega de Vinos, Planta Panquehue_

**Figura 2. Área de influencia del proyecto**

Informe de Calidad del Aire Pág. 5

_Nueva Planta Tratamiento Riles y Actualización Bodega de Vinos, Planta Panquehue_

# 3 MODELACIÓN DE CONTAMINANTES

Los valores de concentración de material particulado en el aire se obtuvieron mediante el modelo
computacional AERScreen. Esta versión es una versión simplificada del modelo original AERMod, el
cual permite obtener concentraciones para todo tipo de proyectos simples, sin terrenos complejos,
múltiples fuentes simultáneas, información meteorológica detallada, etc. Normalmente este tipo de
modelos consideran el peor caso posible.

Este modelo simplificado, es del tipo Screen, el cual es utilizado exclusivamente para determinar la
necesidad o no de realizar un estudio más acabado. El modelo permite al usuario modelar fuentes de
área rectangular con una relación de longitud / ancho de hasta 10:1. El nuevo algoritmo también
proporciona estimaciones de concentración dentro de la misma fuente de área. El algoritmo es el
siguiente:




 []














 2

χ = _Q_ _A_ _K_ _V_  exp − 5.0  _y_ 
2 π _u_ ∫ σ σ  [] ∫   [] σ  []








 

_y_

 [] σ  []
 _y_ 

= _Q_ _A_ _K_ _V_  exp − 5.0 
∫ ∫  []

[]

_A_ _K_ _V_  exp − 5.0 _y_  _dy_ 

_u_ ∫ σ σ  [] ∫   [] σ  []   []

_Q_ _A_ _K_ _V_  exp − 5.0 _y_  _dy_  _dx_

2 π _u_ ∫ σ σ  [] ∫   [] σ  []   []

_s_ _x_ _y_ _z_ _y_ _y_

 []


donde:

χ = concentración máxima del contaminante
QA= tasa de emisión de la fuente de área (g/m [2] s)
K = coeficiente de conversión de la concentración calculada a unidades deseadas. Valor
predeterminado de 1 x 10 [6] para Q A en g/m [2] s y concentraciones en μg/m [3] .
Us = velocidad del viento

σx, σy, σz = Coeficiente de dispersividad o desviación estándar de la velocidad del viento en cada
dirección.
V = término vertical que da cuenta de la distribución vertical de la pluma Gaussiana,
incluyendo los efectos de elevación de la fuente, elevación del receptor y mezclado
vertical limitado.

El modelo simplificado de la versión actual de AERMOD, obliga a los cálculos del modelo a representar
valores para la línea central de la pluma, independientemente de la orientación de la fuente y receptor
en la dirección del viento. Esta opción se incluye en AERMOD para facilitar el uso del modelo en un
modo simplificado para estimar los impactos en el peor de los casos.

El modelo puede funcionar con todo tipo de fuentes, ya sea puntual, área, volumen o antorchas. Posee
la capacidad de distinguir estructuras como edificios cercanos a las fuentes de emisiones que generan
distorsiones puntuales a la pluma generando puntos de impacto distintos a la dispersión simple.

El modelo AERScreen, incluye subrutinas especiales en caso de que los contaminantes sean NO X para
su conversión a NO 2, como se exigen en las normas de calidad del aire de dióxido de nitrógeno.

Los resultados del modelo se presentan en formato radial respecto al centro de la fuente, de modo que
independiente de la dirección del viento, siempre se calcula el peor escenario disponible en las
subrutinas internas de modelación.

El objetivo de este tipo de modelos es descartar el uso de modelos más complejos y precisos. De esta
manera si los resultados están por debajo del 30% de las normas de calidad, se entiende que en ningún
caso se superará la respectiva norma de calidad del aire y se descarta el impacto en los receptores.

Informe de Calidad del Aire Pág. 6

_Nueva Planta Tratamiento Riles y Actualización Bodega de Vinos, Planta Panquehue_

## 3.1 PARÁMETROS DE INGRESO

La Tabla siguiente contiene los parámetros de ingreso para el modelo. Este dato, expresado en las
unidades que se muestra en la tabla, se ingresa al modelo, el cual entrega como resultado la
concentración máxima esperada y la distancia a la cual ocurre.

**Tabla 1: Parámetros de ingreso para el modelo**

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La Tabla siguiente contiene los parámetros de ingreso para el modelo. Este dato, expresado en las unidades que se muestra en la tabla, se ingresa al modelo, el cual entrega como resultado la concentración máxima esperada y la distancia a la cual ocurre. -->

**Tabla 1: Parámetros de ingreso para el modelo****

| Parámetro | Unidad | Valor |
| --- | --- | --- |
| Velocidad viento | m/s | 3.0 |
| Máxima Temperatura ambiente | K | 310 |
| Mínima Temperatura ambiente | K | 270 |
| Tipo de Algoritmo | - | Rural |
| Elevación de la fuente | m | 2 |
| Altura de anemómetro<br> | m | 10 |

<!-- Estadísticas: 6 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Fuente:** Elaboración propia. Las emisiones consideradas para la modelación corresponden a las mayores emisiones determinadas en el capítulo de estimación de emisiones, las que corresponden a la etapa de operación actual y -->
<!-- FIN TABLA 1 -->


|Parámetro|Unidad|Valor|
|---|---|---|
|Velocidad viento|m/s|3.0|
|Máxima Temperatura ambiente|K|310|
|Mínima Temperatura ambiente|K|270|
|Tipo de Algoritmo|-|Rural|
|Elevación de la fuente|m|2|
|Altura de anemómetro<br>|m|10|

**Fuente:** Elaboración propia.

Las emisiones consideradas para la modelación corresponden a las mayores emisiones determinadas
en el capítulo de estimación de emisiones, las que corresponden a la etapa de operación actual y
construcción de la nueva PTRiles del año 1, cuyos valores se presentan en la siguiente tabla.

La duración anual de la etapa de construcción más operación actual es de 12 meses (operación
continua), por lo que se modelará en base a los promedios diarios para comparar con la respectiva
norma de calidad del aire.

**Tabla 2: Emisiones consideradas para el ingreso para el modelo (construcción de la nueva PTRiles +**

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La duración anual de la etapa de construcción más operación actual es de 12 meses (operación continua), por lo que se modelará en base a los promedios diarios para comparar con la respectiva norma de calidad del aire. -->

**Tabla 2: Emisiones consideradas para el ingreso para el modelo (construcción de la nueva PTRiles +****

| Contaminante | Unidad | Emisión |
| --- | --- | --- |
| Material Particulado respirable (MP10) | Ton/año | 0.84 |
| Material Particulado fino (MP2.5) | Ton/año | 0.24 |
| Material Particulado Total (MPT)<br> | Ton/año<br> | 3.40 |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Fuente:** Anexo Estudio de Emisiones atmosféricas del proyecto. El modelo AERScreen contiene una subrutina de generación de una matriz meteorológica que permite determinar la peor condición para el área del proyecto en evaluación. Esta subrutina, determina la peor -->
<!-- FIN TABLA 2 -->

**operación actual)**

|Contaminante|Unidad|Emisión|
|---|---|---|
|Material Particulado respirable (MP10)|Ton/año|0.84|
|Material Particulado fino (MP2.5)|Ton/año|0.24|
|Material Particulado Total (MPT)<br>|Ton/año<br>|3.40|

**Fuente:** Anexo Estudio de Emisiones atmosféricas del proyecto.

El modelo AERScreen contiene una subrutina de generación de una matriz meteorológica que permite
determinar la peor condición para el área del proyecto en evaluación. Esta subrutina, determina la peor
condición, en base a tablas estacionales y considerando las condiciones de borde que se han ingresado
de temperaturas máxima, mínima y velocidad mínima del viento.

Informe de Calidad del Aire Pág. 7

_Nueva Planta Tratamiento Riles y Actualización Bodega de Vinos, Planta Panquehue_

## 3.2 RESULTADOS DE LA MODELACIÓN

La siguiente tabla muestra los resultados obtenidos al hacer correr el modelo.

**Tabla 3: Resultados modelación dispersión**

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- ## 3.2 RESULTADOS DE LA MODELACIÓN La siguiente tabla muestra los resultados obtenidos al hacer correr el modelo. -->

**Tabla 3: Resultados modelación dispersión****

| Contaminante | Aporte del proyecto | Distancia<br>(m) | Norma de calidad<br>del aire | % Respecto a<br>Norma |
| --- | --- | --- | --- | --- |
| MP10 | 17.16 [ug/m3N] | 100 | 150 | 11.4% |
| MP2.5 | 4.68 [ug/m3N] | 100 | 50 | 9.4% |
| MPS<br> | 86.59 [mg/m2/día]<br> | 100<br> | 150<br> | 57.7%<br> |

<!-- Estadísticas: 3 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **Nota:** Aporte del proyecto y normas de calidad están expresadas en [ug/m3N], para cada período considerado. MPS está expresado como [mg/m [2] /día] y la norma de referencia corresponde a la confederación Suiza. Para obtener una mejor referencia de la dispersión de los contaminantes, se presentan gráficos con la -->
<!-- FIN TABLA 3 -->


|Contaminante|Aporte del proyecto|Distancia<br>(m)|Norma de calidad<br>del aire|% Respecto a<br>Norma|
|---|---|---|---|---|
|MP10|17.16 [ug/m3N]|100|150|11.4%|
|MP2.5|4.68 [ug/m3N]|100|50|9.4%|
|MPS<br>|86.59 [mg/m2/día]<br>|100<br>|150<br>|57.7%<br>|

**Nota:** Aporte del proyecto y normas de calidad están expresadas en [ug/m3N], para cada período considerado.
MPS está expresado como [mg/m [2] /día] y la norma de referencia corresponde a la confederación Suiza.

Para obtener una mejor referencia de la dispersión de los contaminantes, se presentan gráficos con la
evolución de la calidad del aire a medida que el receptor se aleja de la fuente de proyecto.

**Figura 3: Resultados modelación de dispersión de MP10**

**Fuente:** Elaboración propia.

**Figura 4: Resultados modelación de dispersión de MP2.5**

**Fuente:** Elaboración propia.

Informe de Calidad del Aire Pág. 8

_Nueva Planta Tratamiento Riles y Actualización Bodega de Vinos, Planta Panquehue_

**Figura 5: Resultados modelación de dispersión de MPS**

31.44 [mg/m [3] ]

56.88 [mg/m [3] ]

86.59 [mg/m [3] ]

**Fuente:** Elaboración propia.

Informe de Calidad del Aire Pág. 9

_Nueva Planta Tratamiento Riles y Actualización Bodega de Vinos, Planta Panquehue_

# 4 CONCLUSIONES

Desde el punto de vista de dispersión de contaminantes se aprecia que la emisión se dispersa
rápidamente, debido a la baja energía ascendente del flujo de emisión, típico de las actividades de
movimientos de tierra, que al no tener suficiente momentum se dispersa y decae rápidamente.

Los resultados de la modelación de dispersión de emisiones atmosféricas permiten confirmar el área
de influencia directa del Proyecto como un círculo alrededor del área de ocupación del proyecto, con
impacto en menos de 1 km, toda vez que, a menos de 500 m de la fuente, el aporte cae por debajo del
50%.

Se puede apreciar en la tabla 3 y las figuras 3, 4 y 5, que no se superará la norma de calidad de aire
para Material Particulado inferior a 10 micrones (MP10), Material Particulado inferior a 2.5 micrones
(MP2.5) y Material Particulado Sedimentable (MPS) y que el nivel de calidad del aire en el punto de
máximo impacto es del orden del 10% de la norma primaria de calidad de aire para Material Particulado
inferior a 10 micrones, establecida en el DS59/1998 del Ministerio Secretaría General de la República.
De igual manera, para las normas de calidad del aire de material particulado inferior a 2.5 micrones, el
aporte máximo no alcanza el 10% de las respectivas normas, lo que asegura que el proyecto no genera
impacto en la salud de las personas. En el caso, del Material Particulado Sedimentable no existe una
norma nacional para este contaminante y se utiliza la norma de la Confederación Suiza como
referencia, que para este proyecto es inferior al 60%, sin embargo, este valor ocurre dentro del área
del proyecto y al extenderlo al receptor más cercano, el nivel ha caído por debajo del 40% de la norma.

Dado que la modelación de dispersión para el año de mayor emisión cumple con las normas de calidad
del aire, se entiende que en las demás etapas del proyecto (Operación y cierre) el aporte es
proporcionalmente menor y por ende cumple las normas de calidad del aire con mayor margen.

De los resultados obtenidos, se observa que no es necesario realizar un estudio de dispersión de
contaminantes más acabado, tal como es descrito en el capítulo 3 de la “Guía para el uso de modelos
de calidad del aire en el SEIA” elaborada por el Servicio de Evaluación Ambiental en 2012, toda vez
que los aportes son inferiores al 5% de las respectivas normas de calidad.

Por lo tanto, se puede concluir que a nivel de calidad del aire el proyecto no genera un impacto
significativo, y que dado el bajo aporte y la rápida dispersión se puede confirmar el área de influencia
inicialmente considerado.

# 5 BIBLIOGRAFÍA

1. Air Pollution Control Engineering, N. De Nevers, 1995.
2. Guía para el uso de modelos de calidad del aire en el SEIA, Servicio de Evaluación Ambiental,
2012.
3. Atmospheric dispersion modeling compliance guide, Karl B. Schnelle & Partha R. Dey, 2000.
4. DS59/98 Establece norma de calidad primaria para material particulado respirable MP10,
Ministerio Secretaria General de la Presidencia de la República.

Informe de Calidad del Aire Pág. 10