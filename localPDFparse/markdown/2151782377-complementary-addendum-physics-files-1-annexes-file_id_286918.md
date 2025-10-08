---
title: Sin título
author: Desconocido
date: D:20220113010013-03'00'
language: es
type: report
pages: 17
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 12 MODELACIÓN -MPS LOS LLANOS
-->

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

# ANEXO 12 MODELACIÓN -MPS LOS LLANOS

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

**ÍNDICE DE CONTENIDO**

**1.** **INTRODUCCIÓN .......................................................................................................................... 3**

**2.** **PRESENTACIÓN DEL MODELO ..................................................................................................... 3**

**MARCO LEGAL .................................................................................................................................... 5**

**3.** **MODELACIÓN DEL MATERIAL PARTICULADO SEDIMENTABLE ...................................................... 6**

3.1. Fuentes emisoras ......................................................................................................................... 6

a. Área Parque ................................................................................................................................. 6

3.2. Receptores ................................................................................................................................... 6

3.3. Otros parámetros de modelación considerados ......................................................................... 8

3.4. Estimación de las tasas de depositación de MPS......................................................................... 8

3.5. Resultados de la modelación ....................................................................................................... 8

3.6. Aportes del Proyecto ................................................................................................................... 8

**4.** **CONCLUSIONES ........................................................................................................................ 12**

**5.** **BIBLIOGRAFÍA .......................................................................................................................... 13**

**ÍNDICE DE TABLAS**

Tabla 1. Parámetros de entrada del modelo ................................................................................................. 5

Tabla 2. Normas de Calidad del Aire Consideradas en el Estudio. ................................................................ 5

Tabla 3 Caracterización del sector área Parque ............................................................................................ 6

Tabla 4 Receptores para Área Parque ........................................................................................................... 6

Tabla 5 Aporte de Proyecto MPS Promedio Anual, Área Parque Norma de referencia chilena ................... 9

Tabla 6 Aporte de Proyecto MPS Promedio Anual, Área Parque Norma de referencia Ordenanza Suiza ... 9

Tabla 6 Aporte de Proyecto MPS Promedio Mensual, Área Parque ............................................................. 9

Tabla 7. MPS según distancia respecto del Área Parque ............................................................................ 11

**ÍNDICE DE FIGURAS**

Figura 1 Ubicación de Fuentes Emisora Área Parque y Receptores Evaluados ............................................ 7

Figura 2 Comportamiento de las Concentraciones MPS según las distancias Área Parque ....................... 10

**Anexo 12 - Modelación MPS** **2**

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

**1.** **INTRODUCCIÓN**

En el presente documento se estiman los aportes del Proyecto a las tasas de depositación de material
particulado sedimentable (MPS) generadas por el Proyecto “Parque Fotovoltaico Los Llanos” ubicado en
la comuna de Copiapó, Provincia de Copiapó, Región de Atacama.

La información presentada se enmarca en dar respuesta a la Pregunta N°5.1 del último “Informe
Consolidado de Solicitud de Aclaraciones, Rectificaciones y/o Ampliaciones” (ICSARA), en la cual se solicita
evaluar el impacto ambiental que generará el Proyecto en las actividades ganaderas y de recolección de
recursos naturales existentes, mediante la evaluación del MPS en la zona.

Lo anterior se realizará a través de una modelación con SCREEN3 (utilizando el programa SCREEN View
versión 4.0.1) y los límites de la norma de calidad secundaria de referencia (Decreto Exento N°4 1992 y de
la norma de la Ordenanza Suiza).

Cabe destacar que el modelo de tipo “Screening” denominado SREEN3 es de tipo pluma Gaussiana
aprobado por la U.S. EPA. Este modelo emplea un rango de clases de estabilidad y velocidades del viento
para identificar el " **peor caso** " de condiciones meteorológicas, que resulta en máximas concentraciones a
nivel de piso. Sus características lo convierten en un modelo de dispersión muy conservador, recomendado
principalmente para descartar la necesidad de usar modelos de dispersión más refinados. En concordancia
con esto, la “Guía para el uso de modelos de calidad del aire en el SEIA” (2012) menciona que este tipo de
modelos permiten decidir si se debe hacer una estimación de impactos a través de modelación con mayor

detalle.

**2.** **PRESENTACIÓN DEL MODELO**

SCREEN3 es un modelo de pluma Gaussiana, aprobado por la U.S. EPA, que constituye una herramienta de
modelación simplificada, incorporando factores de la fuente y meteorológicos para calcular la
concentración de contaminantes provenientes de fuentes con emisiones continuas. El modelo asume que
el contaminante no experimenta ninguna reacción química y que ningún proceso de remoción (húmeda o
seca) actúa sobre la pluma durante el transporte desde la fuente.

SCREEN3 realiza cálculos de corto plazo (horarios) que incluyen la estimación de concentraciones máximas
a nivel del suelo y la distancia a la cual ocurren estas concentraciones (viento abajo de la fuente emisora).
El modelo incorpora, también, efectos por edificios cercanos, fumigación, etc. Para estos efectos, utiliza
un modelo de dispersión de penacho gaussiano modificado, incorporando factores meteorológicos. El
software permite calcular concentraciones máximas a cualquier distancia especificada por el usuario
(hasta 100 km). Examina un rango de clases de estabilidad y velocidades del viento para identificar una
condición meteorológica de "peor escenario", es decir, la peor combinación de velocidad del viento y
estabilidad que resulta en las concentraciones de contaminantes más altas a nivel del suelo.

El modelo SCREEN3 está basado en la ecuación de distribución gaussiana de difusión y calcula niveles de
concentración a distintas distancias de la fuente sin considerar la dirección de los vientos. Luego, a partir
de este modelo se generan curvas de isconcentraciones para todas las direcciones que pueda tener el
viento identificando claramente la isolínea donde se encuentra el punto de máximo impacto. La ecuación
gaussiana se muestra a continuación:

**Anexo 12 - Modelación MPS** **3**

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

**Ecuación 1 - Ecuación Gaussiana**

_Fuente: “Aplicación de un modelo de dispersión atmosférica” (J.A. Cabrera, 2012)_

Donde:

c : Concentración (g/m [3] )

u : Velocidad del viento a la altura efectiva de la fuente (m/s)

Q : Emisión del contaminante (g/s)

σ y : Coeficiente de dispersión horizontal (m)

σ z : Coeficiente de dispersión vertical (m)

H : Altura efectiva de la emisión (m)

y : Coordenada horizontal, en la dirección del viento, tomando como origen el punto de emisión (m)

z : Coordenada vertical, tomando como origen el punto de emisión (m)

La ecuación se corrige por reflexión en el suelo y en la altura de mezcla, quedando de la forma:

**Ecuación 2 - Ecuación Gaussiana corregida por reflexión y altura de mezcla**

Fuente: “Aplicación de un modelo de dispersión atmosférica” (J.A. Cabrera, 2012)

Como todo tipo de modelo, SCREEN3 se basa en una serie de supuestos para simular el proceso de
dispersión del penacho, los cuales son:

- El contaminante no sufre cambios químicos luego de ser emitidos.

- No existen otros procesos de remoción, como depositación seca o húmeda.

- El terreno no presenta variaciones de altura superiores a los 200 m.

**Anexo 12 - Modelación MPS**
**4**

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

El modelo requiere una serie de datos de entrada que caracterizan la fuente emisora, lo cual dependerá si
se trata de una fuente puntual, areal o volumétrica. Por ejemplo, la Tabla 1 muestra algunos de los datos
de entrada requeridos para una fuente areal:

**Tabla 1. Parámetros de entrada del modelo**

|Parámetro|Unidad|
|---|---|
|Tasa de Emisión de la fuente|g/s-m2|
|Altura de emisión|metros|
|Altura del receptor sobre el suelo|metros|
|Longitud del lado más largo del área rectangular|metros|
|Longitud del lado más corto del área rectangular|metros|

_Fuente: Elaboración propia._

SCREEN3 además ofrece la opción de incluir coeficientes de dispersión urbano o rural. La determinación
de la aplicabilidad de la dispersión urbana o rural se basa en el uso del suelo o densidad de población.
Además, respecto a la meteorología, el modelo da la opción de “Meteorología Completa (Full
meteorology)”, que utiliza todas las clases de estabilidad y velocidad de viento para encontrar la condición
de dispersión más desfavorable, o también permite indicar la clase de estabilidad y la velocidad del viento
específica para la zona analizada.

Para estimar las concentraciones máximas a diferentes distancias en torno a las fuentes emisoras del

Proyecto, se utilizan las herramientas de distancia automática y distancia discreta que proporciona SCREEN

View.

**MARCO LEGAL**

En el contexto legal, se ha considerado como norma de referencia según el Decreto Exento N°4 1992 que
establece normas de calidad del aire para material particulado sedimentable en la Cuenca del Río Huasco
Región de Atacama. Los estadísticos a evaluar se presentan en la Tabla ~~2Tabla 2:~~

**Tabla 2. Normas de Calidad del Aire Consideradas en el Estudio.**

|Parámetro|Norma|Estadístico|Valor límite|Referencia|
|---|---|---|---|---|
|MPS|Secundaria|Promedio Anual|100 mg/m2-día|D.S. Exento N° 4/92 MINAGRI|
|MPS|Secundaria|Promedio Mensual|150 mg/ m2-día|150 mg/ m2-día|
|MPS|Secundaria|Promedio Anual|100 mg/m2-día|Ordenanza Suiza|

**Anexo 12 - Modelación MPS**
**5**

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

**3.** **MODELACIÓN DEL MATERIAL PARTICULADO SEDIMENTABLE**

**3.1.** **Fuentes emisoras**

Para la fuente de emisión se determinó su tasa de emisión de material particulado sedimentable
respectiva, considerando que es una fuente areal. Para el caso del Parque se consideró un área de 297.000

m2.

A continuación, se presentan las características de la fuente emisora areal considerada en el modelo para

la fase de construcción.

**a.** **Área Parque**

La caracterización de la fuente del área del Parque, se constituye por las actividades realizadas al interior
del polígono definido por el Proyecto y las actividades a considerar se especifican en la Tabla 3.

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **a.** **Área Parque** La caracterización de la fuente del área del Parque, se constituye por las actividades realizadas al interior del polígono definido por el Proyecto y las actividades a considerar se especifican en la Tabla 3. -->

**Tabla 3: Caracterización del sector área Parque****

| Contaminante | Dimensiones (metros) | Tasa de emisión (g/s-m2) | Descripción |
| --- | --- | --- | --- |
| MPS | 540 x 550 | 7,97E-08 | Sector Parque: erosión,<br>transferencia de material,<br>combustión maquinarias,<br>grupos generadores, camino<br>no pavimentado y<br>combustión de vehículos |

<!-- Estadísticas: 1 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: Elaboración propia._ **3.2.** **Receptores** -->
<!-- FIN TABLA 3 -->


**Tabla 3 Caracterización del sector área Parque**

|Contaminante|Dimensiones (metros)|Tasa de emisión (g/s-m2)|Descripción|
|---|---|---|---|
|MPS|540 x 550|7,97E-08|Sector Parque: erosión,<br>transferencia de material,<br>combustión maquinarias,<br>grupos generadores, camino<br>no pavimentado y<br>combustión de vehículos|

_Fuente: Elaboración propia._

**3.2.** **Receptores**

Si bien el modelo considera distancias por defecto, se han considerado cuatro receptores para el área
Parque que corresponden puntos específicos representativos y más cercanos respecto de la fuente
emisora. Cabe señalar que las distancias dependen de la fuente considerada, es que a continuación se
presentan las distancias de estos receptores respecto de la fuente.

**Tabla 4 Receptores para Área Parque**

|Receptor|Distancia respecto de la<br>fuente (metros)|Coordenadas UTM (WGS84)|Col4|
|---|---|---|---|
|**Receptor**|**Distancia respecto de la**<br>**fuente (metros)**|**Este (m)**|**Este (m)**|
|Punto Ruta Trashumancia 1|844|334.669|6.970.119|
|Punto Ruta Trashumancia 2|1.195|335.291|6.969.623|
|Bosque Chañar|2.032|335.884|6.968.530|
|Punto Ruta Trashumancia 3|2.860|336.955|6.969.488|

_Fuente: Elaboración propia._

Por otra parte en la

**Anexo 12 - Modelación MPS** **6**

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

Figura 1 ~~Figura 1~~ se presentan los receptores descritos anteriormente y la fuente de emisión considerada.

**Figura 1 Ubicación de Fuentes Emisora Área Parque y Receptores Evaluados**

_Fuente: Elaboración propia._

**Anexo 12 - Modelación MPS**
**7**

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

**3.3.** **Otros parámetros de modelación considerados**

Además de las tasas de emisión indicadas en la sección anterior, para la modelación en SCREEN3 se
consideró la altura de la fuente emisora promedio de 1 metro. Se asumió terreno simple plano y un
coeficiente de dispersión rural, debido a las características del área de emplazamiento del Proyecto.

Respecto a la meteorología se consideró la opción “Full Meteorology”, con la cual se estiman todas las
combinaciones de clases de estabilidad y rangos de velocidad del viento, estimando las concentraciones
máximas horarios bajo la condición más desfavorable posible.

**3.4.** **Estimación de las tasas de depositación de MPS**

Con los datos de entrada indicados anteriormente, se modeló el escenario de mayor emisión del Proyecto,
el cual corresponde al período de la fase de construcción. De esta forma, se obtuvieron las
concentraciones máximas horarias de PTS a causa de las emisiones del Proyecto, a distintas distancias
desde cada una de las fuentes emisoras consideradas. No obstante, los resultados de SCREEN3
representan la máxima concentración horaria, por lo que para expresarlos en términos de concentración
en 24 horas y media anual se requiere aplicar factores de conversión. En este caso, se utilizaron los
factores propuestos en el documento “Screening Procedures for Estimating the Air Quality Impact of
Stationary Sources” de la EPA (sección 4.3, paso 5), referenciado en la Guía del Usuario del Modelo
SCREEN3, en el cual se indica un factor de 0,4 para convertir de concentraciones máximas horarias a
máxima media en 24 horas, y un factor de 0,08 para obtener la máxima media anual.

Es importarte señalar que para evaluar el cumplimiento de la norma mensual se ha considerado como
peor condición el valor de 24 horas.

Posteriormente, con las concentraciones de PTS expresadas en términos de media anual y mensual se
procedió a estimar las tasas de depositación en cada una de las distancias incluidas en la modelación, para
lo cual se supone una velocidad de sedimentación de 0,01 m/s [1] .

**3.5.** **Resultados de la modelación**

Las siguientes Tablas muestran los resultados de las tasas de depositación de MPS asociadas, a distintas
distancias de cada una de las fuentes emisoras. Por otra parte, se consideraron aportes por defecto a
distintas distancias entre el rango de los 50 metros y los 3000 metros. Así, se puede observar que los
mayores aportes del Proyecto se concentran en los primeros metros.

**3.6.** **Aportes del Proyecto**

A continuación, se presentan los aportes del Proyecto en el escenario de modelación además del
porcentaje respecto al valor normado.

1 Fuente: Química Física del Ambiente y de los Procesos Medioambientales (Juan E. Figueruelo, Martin Marino Dávila), 2004

**Anexo 12 - Modelación MPS** **8**

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

 **Área Parque**

En la fuente emisora Área Parque, se contemplan las actividades de erosión, compactación, nivelación y
excavación, además de las emisiones de maquinaria.

**Tabla 5 Aporte de Proyecto MPS Promedio Anual, Área Parque Norma de referencia chilena**

|Receptor|Distancia<br>respecto de la<br>Fuente (metros)|Valor Anual (mg/m2-día)|Valor Norma de<br>Referencia (mg/m2-día)|% de la Norma|
|---|---|---|---|---|
|Punto Ruta Trashumancia 1|844|0,3|100|0,3%|
|Punto Ruta Trashumancia 2|1.195|0,2|100|0,2%|
|Bosque Chañar|2.032|0,1|100|0,1%|
|Punto Ruta Trashumancia 3|2.860|0,1|100|0,1%|
|Punto de máximo impacto|400|0,5|100|0,5%|

_Fuente: Elaboración propia, según Salida SCREEN3_

**Tabla 6 Aporte de Proyecto MPS Promedio Anual, Área Parque Norma de referencia Ordenanza Suiza**

|Receptor|Distancia<br>respecto de la<br>Fuente (metros)|Valor Anual (mg/m2-día)|Valor Norma de<br>Referencia (mg/m2-día)|% de la Norma|
|---|---|---|---|---|
|Punto Ruta Trashumancia 1|844|0,3|200|0,1%|
|Punto Ruta Trashumancia 2|1.195|0,2|200|0,1%|
|Bosque Chañar|2.032|0,1|200|0,1%|
|Punto Ruta Trashumancia 3|2.860|0,1|200|0,1%|
|Punto de máximo impacto|400|0,5|200|0,3%|

_Fuente: Elaboración propia, según Salida SCREEN3_

**Tabla** ~~**76**~~ **Aporte de Proyecto MPS Promedio Mensual, Área Parque**

|Receptor|Distancia<br>respecto de la<br>Fuente (metros)|Valor Anual (mg/m2-día)|Valor Norma de<br>Referencia (mg/m2-día)|% de la Norma|
|---|---|---|---|---|
|Punto Ruta Trashumancia 1|844|1,3|150|0,9%|
|Punto Ruta Trashumancia 2|1.195|1,0|150|0,7%|
|Bosque Chañar|2.032|0,7|150|0,5%|
|Punto Ruta Trashumancia 3|2.860|0,5|150|0,4%|
|Punto de máximo impacto|400|2,7|150|1,8%|

_Fuente: Elaboración propia, según Salida SCREEN3_

A continuación, en la

**Anexo 12 - Modelación MPS** **9**

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

Figura 2 ~~Figura 2~~ se presenta el comportamiento de las concentraciones máximas horarias de MPS hasta

una distancia de 3.000 metros.

**Anexo 12 - Modelación MPS** **10**

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

**Figura 2 Comportamiento de las Concentraciones MPS según las distancias Área Parque**

_Fuente: Salida SCREEN3 máxima horaria_

**Anexo 12 - Modelación MPS**
**11**

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

**Tabla** ~~**87.**~~ **MPS según distancia respecto del Área Parque**

|Distancia (m)|Concentración PTS (μg/m3)|Col3|Col4|Tasa de depositación MPS<br>(mg/m2-día)|Col6|
|---|---|---|---|---|---|
|**Distancia (m)**|**Max Horaria**|**Máximo diario**|**Media Anual**|**Media Anual**|**Media Mensual**|
|50|5,6|2,2|0,4|0,4|1,9|
|100|6,0|2,4|0,5|0,4|2,1|
|200|6,7|2,7|0,5|0,5|2,3|
|300|7,3|2,9|0,6|0,5|2,5|
|400|7,7|3,1|0,6|0,5|2,7|
|500|6,3|2,5|0,5|0,4|2,2|
|600|5,3|2,1|0,4|0,4|1,8|
|700|4,5|1,8|0,4|0,3|1,6|
|800|4,0|1,6|0,3|0,3|1,4|
|900|3,6|1,5|0,3|0,3|1,3|
|1.000|3,3|1,3|0,3|0,2|1,2|
|1.100|3,1|1,2|0,2|0,2|1,1|
|1.200|2,9|1,2|0,2|0,2|1,0|
|1.300|2,7|1,1|0,2|0,2|0,9|
|1.400|2,6|1,0|0,2|0,2|0,9|
|1.500|2,5|1,0|0,2|0,2|0,8|
|1.600|2,3|0,9|0,2|0,2|0,8|
|1.700|2,2|0,9|0,2|0,2|0,8|
|1.800|2,1|0,9|0,2|0,1|0,7|
|1.900|2,1|0,8|0,2|0,1|0,7|
|2.000|2,0|0,8|0,2|0,1|0,7|
|2.100|1,9|0,8|0,2|0,1|0,7|
|2.200|1,8|0,7|0,1|0,1|0,6|
|2.300|1,8|0,7|0,1|0,1|0,6|
|2.400|1,7|0,7|0,1|0,1|0,6|
|2.500|1,7|0,7|0,1|0,1|0,6|
|2.600|1,6|0,7|0,1|0,1|0,6|
|2.700|1,6|0,6|0,1|0,1|0,5|
|2.800|1,5|0,6|0,1|0,1|0,5|
|2.900|1,5|0,6|0,1|0,1|0,5|
|3.000|1,5|0,6|0,1|0,1|0,5|

Fuente: Elaboración propia

**Anexo 12 - Modelación MPS** **12**

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

**4.** **CONCLUSIONES**

Los resultados de la modelación de las concentraciones de PTS con SCREEN3 y la estimación de los aportes
a las tasas de despositación de MPS a distintas distancias desde el Proyecto, muestran que los aportes en
los receptores identificados se encuentran bajos los límites permisibles establecidos por la norma de
referencia anual y mensual del Decreto Exento N°4/1992 además respecto de la norma referencia anual
de la Ordenanza Suiza. Estos aportes máximos se producen durante la Fase de Construcción, puesto que
durante este periodo se concentra la mayor parte de la emisión de material particulado, disminuyendo
considerablemente durante el resto de la vida útil del Proyecto.

Cabe recalcar que los resultados de SCREEN3 representan las concentraciones máximas a nivel de piso,
pues prueba distintas combinaciones de meteorología (clases de estabilidad y velocidades del viento),
definiendo la más desfavorable. No obstante, debido a que este modelo de dispersión no considera las
condiciones reales ni locales de meteorología, tampoco las características topográficas del área de
emplazamiento del Proyecto, sus resultados sólo pueden ser utilizados para determinar el radio máximo
en el que se tienen ciertos niveles de aporte a las concentraciones.

Al considerar el aporte de material particulado sedimentable proveniente del área definida como Parque
en los receptores sensibles identificados alcanza un máximo del 0,9% respecto al valor del límite mensual
permisible (150 mg/m [2] -día) y un 0,3 % de la norma anual (100 mg/m [2] -día) . El punto de máximo impacto
se alcanza a 400 metros donde la depositación anual alcanza 0,5 mg/m [2] -día, mientras que la mensual a
2,7 mg/m [2] -día.

**Anexo 12 - Modelación MPS** **13**

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

**5.** **BIBLIOGRAFÍA**

 - Guía para el uso de modelos de calidad del aire en el SEIA”, Servicio de Evaluación Ambiental,

2012.

 - Guía del Usuario del Modelo SCREEN3, US-EPA, 2000.

 - Screening Procedures for Estimating the Air Quality Impact of Stationary Sources, US-EPA, 1992.

 - Aplicación de un modelo de dispersión atmosférica, J.A. Cabrera, PUCV, 2012.

 - Química Física del Ambiente y de los Procesos Medioambientales (Juan E. Figueruelo, Martin

Marino Dávila), 2004.

**Anexo 12 - Modelación MPS**
**14**

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

**Apéndice 1**

**Salidas SCREEN3**

**Anexo 12 - Modelación MPS**
**15**

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

**Área Parque**

SIMPLE TERRAIN INPUTS:

SOURCE TYPE = AREA

EMISSION RATE (G/(S-M**2)) = 0.797000E-07
SOURCE HEIGHT (M) = 1.0000
LENGTH OF LARGER SIDE (M) = 550.0000
LENGTH OF SMALLER SIDE (M) = 540.0000
RECEPTOR HEIGHT (M) = 2.0000
URBAN/RURAL OPTION = RURAL
THE REGULATORY (DEFAULT) MIXING HEIGHT OPTION WAS SELECTED.
THE REGULATORY (DEFAULT) ANEMOMETER HEIGHT OF 10.0 METERS WAS ENTERED.

MODEL ESTIMATES DIRECTION TO MAX CONCENTRATION

BUOY. FLUX = 0.000 M**4/S**3; MOM. FLUX = 0.000 M**4/S**2.

*** FULL METEOROLOGY ***

**********************************

*** SCREEN AUTOMATED DISTANCES ***

**********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING DISTANCES ***

DIST CONC U10M USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
50. 5.619 6 1.0 1.0 10000.0 1.00 44.

100. 6.018 6 1.0 1.0 10000.0 1.00 44.

200. 6.712 6 1.0 1.0 10000.0 1.00 44.

300. 7.265 6 1.0 1.0 10000.0 1.00 44.

400. 7.680 6 1.0 1.0 10000.0 1.00 44.

500. 6.305 6 1.0 1.0 10000.0 1.00 44.

600. 5.251 6 1.0 1.0 10000.0 1.00 44.

700. 4.538 6 1.0 1.0 10000.0 1.00 44.

800. 4.026 6 1.0 1.0 10000.0 1.00 44.

900. 3.642 6 1.0 1.0 10000.0 1.00 44.

1000. 3.342 6 1.0 1.0 10000.0 1.00 44.

1100. 3.103 6 1.0 1.0 10000.0 1.00 44.

1200. 2.903 6 1.0 1.0 10000.0 1.00 44.

1300. 2.733 6 1.0 1.0 10000.0 1.00 44.

1400. 2.586 6 1.0 1.0 10000.0 1.00 44.

1500. 2.456 6 1.0 1.0 10000.0 1.00 44.

1600. 2.340 6 1.0 1.0 10000.0 1.00 44.

1700. 2.235 6 1.0 1.0 10000.0 1.00 44.

**Anexo 12 - Modelación MPS** **16**

|Col1|ADENDA|Col3|
|---|---|---|
||PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|PROYECTO PARQUE FOTOVOLTAICO LOS LLANOS|

1800. 2.141 6 1.0 1.0 10000.0 1.00 44.

1900. 2.056 6 1.0 1.0 10000.0 1.00 44.

2000. 1.979 6 1.0 1.0 10000.0 1.00 44.

2100. 1.909 6 1.0 1.0 10000.0 1.00 44.

2200. 1.845 6 1.0 1.0 10000.0 1.00 44.

2300. 1.787 6 1.0 1.0 10000.0 1.00 44.

2400. 1.733 6 1.0 1.0 10000.0 1.00 44.

2500. 1.683 6 1.0 1.0 10000.0 1.00 44.

2600. 1.636 6 1.0 1.0 10000.0 1.00 44.

2700. 1.591 6 1.0 1.0 10000.0 1.00 44.

2800. 1.549 6 1.0 1.0 10000.0 1.00 44.

2900. 1.510 6 1.0 1.0 10000.0 1.00 44.

3000. 1.474 6 1.0 1.0 10000.0 1.00 44.

MAXIMUM 1-HR CONCENTRATION AT OR BEYOND 50. M:

400. 7.680 6 1.0 1.0 10000.0 1.00 44.

*********************************

*** SCREEN DISCRETE DISTANCES ***

*********************************

*** TERRAIN HEIGHT OF 0. M ABOVE STACK BASE USED FOR FOLLOWING DISTANCES ***

DIST CONC U10M USTK MIX HT PLUME MAX DIR

(M) (UG/M**3) STAB (M/S) (M/S) (M) HT (M) (DEG)

------- ---------- ---- ----- ----- ------ ------ ------
844. 3.845 6 1.0 1.0 10000.0 1.00 44.

1195. 2.913 6 1.0 1.0 10000.0 1.00 44.

2032. 1.955 6 1.0 1.0 10000.0 1.00 44.

2860. 1.526 6 1.0 1.0 10000.0 1.00 44.

***************************************

*** SUMMARY OF SCREEN MODEL RESULTS ***

***************************************

CALCULATION MAX CONC DIST TO TERRAIN

PROCEDURE (UG/M**3) MAX (M) HT (M)

-------------- ----------- --------- ------
SIMPLE TERRAIN 7.680 400. 0.

***************************************************

** REMEMBER TO INCLUDE BACKGROUND CONCENTRATIONS **

***************************************************

**Anexo 12 - Modelación MPS**
**17**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Parámetros de entrada del modelo****

| Parámetro | Unidad |
| --- | --- |
| Tasa de Emisión de la fuente | g/s-m2 |
| Altura de emisión | metros |
| Altura del receptor sobre el suelo | metros |
| Longitud del lado más largo del área rectangular | metros |
| Longitud del lado más corto del área rectangular | metros |

**Tabla 2.: Normas de Calidad del Aire Consideradas en el Estudio.****

| Parámetro | Norma | Estadístico | Valor límite | Referencia |
| --- | --- | --- | --- | --- |
| MPS | Secundaria | Promedio Anual | 100 mg/m2-día | D.S. Exento N° 4/92 MINAGRI |
| MPS | Secundaria | Promedio Mensual | 150 mg/ m2-día | 150 mg/ m2-día |
| MPS | Secundaria | Promedio Anual | 100 mg/m2-día | Ordenanza Suiza |

**Tabla 4: Receptores para Área Parque****

| Receptor | Distancia respecto de la<br>fuente (metros) | Coordenadas UTM (WGS84) | Col4 |
| --- | --- | --- | --- |
| **Receptor** | **Distancia respecto de la**<br>**fuente (metros)** | **Este (m)** | **Este (m)** |
| Punto Ruta Trashumancia 1 | 844 | 334.669 | 6.970.119 |
| Punto Ruta Trashumancia 2 | 1.195 | 335.291 | 6.969.623 |
| Bosque Chañar | 2.032 | 335.884 | 6.968.530 |
| Punto Ruta Trashumancia 3 | 2.860 | 336.955 | 6.969.488 |

**Tabla 5: Aporte de Proyecto MPS Promedio Anual, Área Parque Norma de referencia chilena****

| Receptor | Distancia<br>respecto de la<br>Fuente (metros) | Valor Anual (mg/m2-día) | Valor Norma de<br>Referencia (mg/m2-día) | % de la Norma |
| --- | --- | --- | --- | --- |
| Punto Ruta Trashumancia 1 | 844 | 0,3 | 100 | 0,3% |
| Punto Ruta Trashumancia 2 | 1.195 | 0,2 | 100 | 0,2% |
| Bosque Chañar | 2.032 | 0,1 | 100 | 0,1% |
| Punto Ruta Trashumancia 3 | 2.860 | 0,1 | 100 | 0,1% |
| Punto de máximo impacto | 400 | 0,5 | 100 | 0,5% |

**Tabla 6: Aporte de Proyecto MPS Promedio Anual, Área Parque Norma de referencia Ordenanza Suiza****

| Receptor | Distancia<br>respecto de la<br>Fuente (metros) | Valor Anual (mg/m2-día) | Valor Norma de<br>Referencia (mg/m2-día) | % de la Norma |
| --- | --- | --- | --- | --- |
| Punto Ruta Trashumancia 1 | 844 | 0,3 | 200 | 0,1% |
| Punto Ruta Trashumancia 2 | 1.195 | 0,2 | 200 | 0,1% |
| Bosque Chañar | 2.032 | 0,1 | 200 | 0,1% |
| Punto Ruta Trashumancia 3 | 2.860 | 0,1 | 200 | 0,1% |
| Punto de máximo impacto | 400 | 0,5 | 200 | 0,3% |
