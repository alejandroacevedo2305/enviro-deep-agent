---
title: Sin título
author: Laptop
date: D:20250805161048-04'00'
language: es
type: report
pages: 29
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Modelación Calidad del Aire - Adenda Complementaria
-->

# Modelación Calidad del Aire - Adenda Complementaria

### P ROYECTO : U SO DE E FLUENTES P LANTA DE T RATAMIENTO DE RIL ES . D ESARROLLADO PARA : C RIADEROS C HILE M INK L TDA .

**Elaborado Por:**

Mewlen Asesoría

Especialistas en Calidad de Aire

[contacto@mewlenasesoria.cl](mailto:contacto@mewlenasesoria.cl)

**Especialista:**

Christian Alexis Bustos Cancino

Ingeniero Civil en Geografía

## Índice de Contenidos

1 Introducción .......................................................................................................................................... 3

2 Objetivos .............................................................................................................................................. 4

2.1 Objetivo General ............................................................................................................................ 4

2.2 Objetivos Específicos ..................................................................................................................... 4

3 Antecedentes Generales ...................................................................................................................... 5

3.1 Ubicación del Proyecto .................................................................................................................. 5

3.2 Descripción del Proyecto ............................................................................................................... 5

3.2.1 Mejoras a la Planta de Tratamiento de RILes ......................................................................... 5

3.2.2 Ampliación de las formas de Descarga de los Efluentes ........................................................ 6

4 Materiales y Métodos ........................................................................................................................... 7

4.1 Evaluación Cumplimiento Normativo ............................................................................................. 7

4.1.1 Evaluación Sobre Normas de Calidad .................................................................................... 7

4.1.2 Criterio de Evaluación en el SEIA para Zonas Saturadas ....................................................... 7

4.2 Descripción modelo Screen3 ......................................................................................................... 8

4.3 Fuentes emisoras......................................................................................................................... 12

4.4 Receptores considerados en la modelación ................................................................................ 14

5 Resultados ......................................................................................................................................... 18

5.1 Resultados de la Modelación ....................................................................................................... 18

5.1.1 Proyección de las concentraciones en receptores discretos respecto a norma D.S. 12/2021.
18

5.2 Evaluación en receptores sensibles ............................................................................................. 22

6 Discusiones ........................................................................................................................................ 23

6.1 Evaluación del incremento significativo en la concentración de material particulado (MP 10 ) ....... 23

6.2 Curva de decaimiento de las concentraciones ............................................................................. 25

6.3 Evaluación en receptores sensibles ............................................................................................. 25

7 Conclusiones ...................................................................................................................................... 27

8 Referencias ........................................................................................................................................ 28

**Apéndice A:** Archivos Digitales, salida de modelación.

### 1 I NTRODUCCIÓN

El presente informe desarrolla una metodología de estimación y evaluación de los potenciales impactos

ambientales en la calidad del aire que pudieran generarse producto de la materialización de las partes y

obras del proyecto “ **Uso de Efluentes Planta de Tratamiento de RILes** ” (en adelante el Proyecto), ubicado

en la comuna de San Francisco de Mostazal, provincia de Cachapoal, Región del Libertador General

Bernardo O’Higgins.

El presente Proyecto contempla una modificación únicamente al Sistema de Tratamiento de RILes, sin

modificación en la tasa de descarga de efluentes, considerando mejoras tecnológicas que permiten el uso

de estas descargas para el riego de un sector aledaño de aproximadamente 3 ha. En esta área de riego se

realizará el cultivo de vegetación para forraje, la cual se busca entregar a precio costo a algún beneficiario

de la zona y que este pueda utilizarlo como alimento de animales. Las mejoras consideradas corresponden

a la implementación de un homogeneizador; un DAF; un Filtro de Membranas y un Estanque de
Acumulación de Efluentes. Adicionalmente, la eliminación del sistema de lombrifiltros (sistema TOHÁ), en

cuenta que se incorpora un sistema de filtrado más eficiente

Dada las características del proyecto, las actividades asociadas a las obras de construcción e instalación

del sistema de regadío, y las actividades asociadas a la fase de operación donde se cultivará vegetación

para forraje, lo que se consolida como las principales fuentes de emisión de material particulado respirable,

por lo tanto, las que revisten mayor interés de análisis. En virtud de lo anterior, la metodología considera la

integración de información de la condición ambiental base, el inventario de emisiones atmosféricas

realizado para el presente DIA y la proyección de las concentraciones de material particulado (MP10) en

receptores potencialmente susceptibles. Del análisis integrado de estas variables, es posible definir el área

de influencia del Proyecto, así como también los potenciales impactos que deriven en la implementación

de un modelo complejo de acuerdo a las propias recomendaciones metodológicas que establece la Guía

para el Uso de Modelos de Calidad de Aire en el SEIA.

Por otra parte, para la modelación se utilizó la metodología screening recomendada por la Agencia

Ambiental de Estados Unidos “Environmental Protection Agency (EPA)” en su documento Apéndice W

parte 51-40 CFR Directrices para Modelos de Calidad del Aire (Guideline on Air Quality Models) siguiendo

las recomendaciones de la Guía respecto a la forma de realizar el diagnóstico.

La estructura del informe considera en primer lugar la presentación de los resultados de la estimación de

emisiones atmosféricas de las fases de construcción y operación del Proyecto, cuyo desarrollo forma parte

de la presente DIA (ver Anexo 6.4), seguido de la identificación de los receptores de interés considerados

en la modelación, y las tablas del aporte del Proyecto sobre estos.

### 2 O BJETIVOS

**2.1 O** **BJETIVO** **G** **ENERAL**

El objetivo general del presente estudio es evaluar las concentraciones ambientales de material particulado

respirable (MP 10 y MP 2,5 ), en los receptores identificados para el Proyecto, producto de las emisiones

asociadas a sus fases de construcción y operación.

**2.2 O** **BJETIVOS** **E** **SPECÍFICOS**

 - Modelar la dispersión atmosférica de las emisiones de material particulado y gases de combustión,

generadas por el Proyecto durante las fases de construcción y operación, utilizando la metodología

screening recomendada por la Agencia Ambiental de Estados Unidos “Environmental Protection

Agency (EPA)”.

 - Comparar los valores de inmisión de material particulado respirable, registrados en los receptores

identificados, con los niveles establecidos en las normativas nacionales de referencia en la materia.

 - Comparar los valores de inmisión de material particulado respirable, registrados en los receptores

identificados, con la línea base de emisiones generada en la Región del Libertador General

Bernardo O’Higgins, más específicamente en la zona declarada saturada para MP 10 y MP 2,5 .

### 3 A NTECEDENTES G ENERALES

**3.1 U** **BICACIÓN DEL** **P** **ROYECTO**

ubicado en la comuna de San Francisco de Mostazal, provincia de Cachapoal, Región del Libertador
General Bernardo O’Higgins. La Figura 3-1, presenta la localización de las partes y obras del proyecto.

**Figura 3-1: Ubicación del Proyecto**

Fuente: Elaboración Propia.

**3.2 D** **ESCRIPCIÓN DEL** **P** **ROYECTO**

3.2.1 M EJORAS A LA P LANTA DE T RATAMIENTO DE RIL ES

El Proyecto contempla el uso de los efluentes para el riego, implementando un área verde de

aproximadamente 3,0 ha, o su infiltración en un área de 0,4 ha, ambas de propiedad del Titular. Por último,

se considera la posibilidad de entrega de agua a terceros colindantes a la empresa, para su uso como agua

para riego.

Para lo anterior, se realizaron mejoras a la Planta de Tratamiento de RILes que permiten incrementar la

capacidad de depuración de los RILes, sin modificar la tasa de tratamiento de los RILes. Además de los

cambios consultados a la Autoridad mediante Consulta de Pertinencia de Ingreso al SEIA del proyecto

“Mejoras al Sistema de Tratamiento de RILes Chilemink”, individualizada precedentemente, y en el mismo

sentido de mejorar la calidad de los efluentes, se implementaron en el Sistema de Tratamiento de RILes,

las siguientes etapas de tratamiento:

 - Homogeneización.

 - DAF (Dissolved Air Flotation Unit).

 - Filtro de Membranas.

 - Piscina de Acumulación de Efluentes.

 - Modificación de una de las unidades de lombrifiltro sin uso del sistema Toha para implementación

del secado de lodos.

3.2.2 A MPLIACIÓN DE LAS FORMAS DE D ESCARGA DE LOS E FLUENTES

El presente proyecto considera el uso de los efluentes del Sistema de Tratamiento de RILes, para el riego

y/o infiltración, aledañas a la Planta de Tratamiento de RILes, en la cual se implementarán áreas verdes

ornamentales, del tipo pradera. Se considera, además, el uso de pozos de infiltración existentes, para

aquellos meses donde el efluente no pueda ser utilizado en su totalidad para el riego. Manteniendo la

opción de descarga al alcantarillado en caso de ser necesario.

Los cambios antes descritos, en conjunto, permiten alcanzar una capacidad de tratamiento de 300 m3 /día,

sin embargo, no existirá un aumento en la capacidad de generación de RILes por parte del área productiva.

El delta adicional, permitirá contar con espacio ocioso en caso de requerir reprocesamiento del efluente o

ante una ampliación del proceso productivo, para alcanzar los parámetros requeridos para el riego

### 4 M ATERIALES Y M ÉTODOS

**4.1 E** **VALUACIÓN** **C** **UMPLIMIENTO** **N** **ORMATIVO**

4.1.1 E VALUACIÓN S OBRE N ORMAS DE C ALIDAD

Para evaluar el cumplimiento normativo del Proyecto, se utilizaron los siguientes valores límites

establecidos en las normativas vigentes de calidad del aire, para regular cada uno de los parámetros

analizados en el presente informe.

**Tabla 4-1. Normativa primaria asociada a calidad del aire.**

|Parámetro|N° Decreto/año|Valor Norma|Periodo de Evaluación de<br>Cumplimiento de Norma|
|---|---|---|---|
|Material<br>Particulado<br>Respirable<br>(MP10)|Decreto Supremo<br>N°12/2022 (MMA)|130<br>μg/Nm3, <br>como<br>concentración de 24 horas|Percentil<br>98<br>de<br>las<br>concentraciones<br>de<br>24<br>horas<br>registradas durante un período<br>anual|
|Material<br>Particulado<br>Respirable<br>(MP10)|Decreto Supremo<br>N°12/2022 (MMA)|50<br>μg/Nm3, <br>como<br>concentración media anual|Media aritmética trianual|
|Material<br>Particulado<br>Respirable<br>Fino (MP2,5)|Decreto Supremo<br>N°12/2022 (MMA)|50<br>μg/m3, <br>como<br>concentración 24 horas|Percentil<br>98<br>de<br>las<br>concentraciones<br>de<br>24<br>horas<br>registradas durante un período<br>anual|
|Material<br>Particulado<br>Respirable<br>Fino (MP2,5)|Decreto Supremo<br>N°12/2022 (MMA)|20<br>μg/m3, <br>como<br>concentración media anual|Media aritmética trianual|

Fuente: Mewlen, 2025.

4.1.2 C RITERIO DE E VALUACIÓN EN EL SEIA PARA Z ONAS S ATURADAS

De acuerdo con el "Criterio de Evaluación en el SEIA: Impacto de Emisiones en Zonas Saturadas por

Material Particulado Respirable MP 10 y Material Particulado Fino Respirable MP 2,5 " (SEA, 2023), se

establece que cualquier proyecto o actividad que requiera el uso de un modelo de calidad del aire para

cuantificar el aporte a las concentraciones de MP 10 y MP 2,5 de sus emisiones y que supere, en los receptores

humanos identificados, los valores indicados en la Tabla 1 de dicho criterio, según la duración del impacto,

se considerará como una configuración del literal a) del artículo 11 de la Ley N°19.800. Esto implica que

los niveles de concentración a los que está expuesta la población en el área de influencia aumentarían

significativamente. En tales casos, el proyecto deberá someterse a evaluación ambiental a través de un

EIA, especificando las medidas destinadas a mitigar el impacto ambiental significativo y el seguimiento de

la variable ambiental afectada.

En la Tabla 4-2 se presentan los valores considerados como significativos para la evaluación de impacto

en un escenario de riesgo preexistente, en relación con el aporte o incremento de concentraciones de MP 10
y MP 2,5 en los receptores humanos de interés situados en el Área de Influencia, para un período igual o

superior a 3 años. Para evaluaciones de impactos con una duración menor a 3 años, como en la fase de

construcción del Proyecto, la guía presenta diferentes valores en función de los meses de duración del

proyecto. En este contexto, la Tabla 4-3 muestra los valores de incremento de MP 10 y MP 2,5 para un periodo

de 12 meses, que será el período evaluado en la modelación de calidad del aire durante la fase de

construcción del Proyecto (peor escenario).

**Tabla 4-2. Valores de significancia para el aumento de concentraciones de MP** **10** **y MP** **2,5** **sobre**
**receptores humanos en un periodo igual o mayor a 3 años en zonas que sobrepasen el valor de la**

**norma.**

|Parámetro|Periodo|Incremento concentración<br>(μg/m3)|
|---|---|---|
|Material Particulado Respirable (MP10)|24 horas|5,0|
|Material Particulado Respirable (MP10)|Anual|1,0|
|Material Particulado Respirable Fino<br>(MP2,5)<br>|24 horas|1,71|
|Material Particulado Respirable Fino<br>(MP2,5)<br>|Anual<br>|0,33|

_Fuente: Mewlen, 2025._

**Tabla 4-3. Valores de significancia para el aumento de concentraciones de MP** **10** **y MP** **2,5** **sobre**
**receptores humanos corregidos para impactos con una duración menor a 3 años en zonas que**

**sobrepasen el valor de la norma.**

|Parámetro|Periodo|Incremento concentración<br>(μg/m3)|
|---|---|---|
|Material Particulado Respirable (MP10)|24 horas|10,00|
|Material Particulado Respirable (MP10)|Anual|3,00|
|Material Particulado Respirable Fino<br>(MP2,5)<br>|24 horas|5,13|
|Material Particulado Respirable Fino<br>(MP2,5)<br>|Anual<br>|0,99|

_Fuente: Mewlen, 2025._

**4.2 D** **ESCRIPCIÓN MODELO** **S** **CREEN** **3**

El análisis del aporte de las concentraciones del Proyecto fue realizado utilizando la metodología screening

recomendada por la Agencia Ambiental de Estados Unidos “Environmental Protection Agency (EPA)” en

su documento Apéndice W parte 51-40 CFR Directrices para Modelos de Calidad del Aire (Guideline on Air

Quality Models).

En dicho modelo se distinguen dos niveles de sofisticación en modelos de dispersión, el primer nivel

consiste de una técnica simple de estimación, que generalmente considera el peor escenario de

condiciones meteorológicas, de modo de proveer estimaciones conservadoras sobre el potencial impacto

en la calidad del aire de una fuente específica o una categoría de fuentes. El segundo nivel corresponde a

un análisis más refinado, que se debe llevar a cabo cuando las técnicas de screening indican que la

concentración contribuida por la fuente excede o cumple de manera ajustada las normas de calidad del

aire, lo cual se condice con lo señalado en la Guía para el Uso de Modelos de Calidad del Aire en el SEIA.

Este método centra sus análisis en relación a las condiciones atmosféricas más desfavorables que se

pudiesen presentar, y de la característica de la fuente que será la emisora de las emisiones (puntual, areal,

volumétrica o llamarada). En cuanto a los resultados, estos permiten determinar el aporte de contaminantes

expresados en concentraciones en función a la distancia que se producen de la fuente emisora.

Este análisis permite estimar las concentraciones de una fuente, respecto a un punto de máximo alcance,

cuyos resultados se expresan en cantidad o concentración por unidad de tiempo (1 hora, 24 horas y un

año). Las variables de entrada del Screen3 corresponden fundamentalmente a datos meteorológicos y

aspectos técnicos de la fuente de emisión como:

 - Tasa de emisión de la fuente (g/s).

 - Superficie de emisión (m [2] ).

 - Altura del receptor sobre el suelo (m).

 - Opción de modelación zona (urbana/rural).

Los supuestos del método establecen que los contaminantes no reaccionan en la atmosfera ni tampoco

experimentan procesos de remoción como depositación (húmedo o seca). Una de las consideraciones es

que no determina, es la dirección en la cual se produce la dispersión de los contaminantes, debido a que

las distancias se reconocen radiales y como centro la fuente emisora.

Dependiendo del tipo de fuente considerada (puntual o de área), el modelo usa distintos datos de entrada.

Los datos de entrada corresponden a las características de la fuente y de las emisiones (tasa de emisión,

dimensiones de la fuente, entre otros), entregando como resultado, un listado con las concentraciones a

nivel del suelo a diferentes distancias de la fuente emisora. Es decir, que estamina un rango de clases de

estabilidad y velocidades del viento para identificar una condición meteorológica de “peor escenario”, para

lo cual, identifica la peor combinación de velocidad del viento y estabilidad que resulta en las

concentraciones de contaminantes más altas a nivel del suelo.

Dado que las emisiones del Proyecto en construcción se estiman en 0,0648 ton/año de MP 10 (excluyendo

las emisiones por circulación y combustión de vehículos), y para su fase de operación se estiman en 0,0012

ton/año de MP 10 (excluyendo las emisiones por circulación en camino pavimentado). Por lo anterior y

considerando que las emisiones que puedan afectar a los receptores cercanos se estima que el área de

trabajo para ambas fases mencionadas es igual a 30 ha y dentro del software será considerada como una

fuente de tipo “areal”. Además, como se presenta más adelante estas emisiones descritas deben ser
transformadas a “g/s/m [2] ” al ser una fuente de tipo areal.

Las concentraciones estimadas por el modelo Screen3 representan promedio horarios, por lo tanto, cuando

se requieren resultados para diferentes periodos, es necesario aplicar un factor de corrección. Los factores

de corrección según EPA se presentan en la Tabla 4-4 a continuación:

**Tabla 4-4: Factor de corrección para concentraciones de Screen3**

<!-- INICIO TABLA 4-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- se requieren resultados para diferentes periodos, es necesario aplicar un factor de corrección. Los factores de corrección según EPA se presentan en la Tabla 4-4 a continuación: -->

**Tabla 4-4: Factor de corrección para concentraciones de Screen3****

| Periodo | Factor de Corrección |
| --- | --- |
| 8 horas | 0,7 |
| 24 horas | 0,4 |
| Anual | 0,08 |

<!-- Estadísticas: 3 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: EPA, 2011. En la siguiente figura es posible observar los parámetros solicitados de input por el software Screen3: -->
<!-- FIN TABLA 4-4 -->


|Periodo|Factor de Corrección|
|---|---|
|8 horas|0,7|
|24 horas|0,4|
|Anual|0,08|

Fuente: EPA, 2011.

En la siguiente figura es posible observar los parámetros solicitados de input por el software Screen3:

**Figura 4-1: Variables de entrada del Screen View**

Fuente: Guía de usuario de SCREEN View. Lakes Environmental software.

A continuación, se presentan los datos que fueron utilizados como input’s en el software:

 - Altura de liberación de la fuente. Dado que se consideró una fuente de área, se estimó 1 metro de

altura de liberación, dado que las actividades relacionadas a la emisión acontecen a ras de suelo.

 - Especificar el lado del rectángulo utilizado. Se debe especificar el largo y ancho del rectángulo

utilizado para la simulación, de lo por lo que se utilizó 230 m por 130,44 m para confirmar

aproximadamente el área de 30 ha de la superficie.

 - Búsqueda en toda gama de direcciones del viento. Dado que la concentración a una distancia

determinada desde un área rectangular depende de la orientación del área con respecto a la

dirección del viento. El método Screen ofrece dos opciones para el tratamiento de la dirección del

viento. En este caso y considerando que se está evaluando el caso más desfavorable,

independiente de la información que se conozca del sector, se consideró la opción “SI” para la cual

el modelo buscara direcciones para encontrar la concentración máxima, por otra parte, es la opción

más recomendada para ser utilizada.

Luego en el módulo de opciones se considera la meteorología y tipo de terreno que será representado.

 - Terreno Simple. Es la opción que se da por defecto al considerar que la fuente es de área y también

considera que el terreno es plano (es la opción determinada por defecto).

 - Meteorología. Con la finalidad de representar el escenario más desfavorable de modelación tanto

en periodo diurno como nocturno, es que se consideró la utilización de la opción “Clase de

estabilidad única y velocidad del viento”. Esta opción permite considerar una sola estabilidad y un

valor para la velocidad del viento. El valor de la velocidad del viento debe estar dentro de los rangos

de la clase de estabilidad especificada. Acá es utilizada para considerar el peor escenario las

categorías de estabilidad propuestas por Pasquill, a continuación, se presenta en la siguiente

figura:

**Tabla 4-5: Categorías de estabilidad propuestas por Pasquill- Gifford,**

 - Fuente: Meteorological Monitoring Guidance for Regulatory Modeling Applications.



Las clases de estabilidad “Pasquill- Gifford” representan seis niveles de estabilidad atmosférica, las cuales

son importantes, ya que estas influyen en la tasa de dispersión de contaminantes. Aumento de las

turbulencias causan que los contaminantes se dispersen más rápidamente que con condiciones

atmosféricas más estables. Las clases de estabilidad A, B y C se consideran condiciones inestables y se

asocian con la generación mecánica de turbulencia o condiciones de nublado. La clase de estabilidad D se

conoce como condiciones neutras y se asocia con la generación mecánica de turbulencias o condiciones

de nublado. Las clases de estabilidad E y F en tanto, se consideran estables, en las cuales las turbulencias

se encuentran suprimidas.

De lo expuesto y considerando la evaluación del peor escenario, así como la velocidad promedio anual del

viento (extraída desde agrometeorología, aeródromo la independencia Rancagua) igual a 2,31 m/s, se

utilizará la estabilidad atmosférica **Clase B- Inestable** .

**4.3 F** **UENTES EMISORAS**

De acuerdo a lo indicado en el Anexo 6.4 Estimación de Emisiones Atmosféricas del presente EIA, las

principales emisiones a la atmósfera durante la fase de construcción del Proyecto corresponden en su

mayoría a material particulado grueso (MP 10 ), las que se asocian principalmente al escarpe del área de

riego. Por otro lado, las emisiones de la fase de operación del Proyecto corresponden principalmente a

material particulado grueso y asociadas a la circulación de vehículos por caminos no pavimentados.

La siguiente tabla presenta el resumen de la estimación de emisiones atmosféricas en la fase de

construcción del Proyecto, para aquellos parámetros que fueron considerados en el presente estudio de

calidad del aire, las cuales se distribuyen en el territorio como se presenta en la Figura 3-1.

**Tabla 4-6: Resumen estimación de emisiones (MP** **10** **) ampliación Chilemink - Fase de Construcción**

<!-- INICIO TABLA 4-6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- construcción del Proyecto, para aquellos parámetros que fueron considerados en el presente estudio de calidad del aire, las cuales se distribuyen en el territorio como se presenta en la Figura 3-1. -->

**Tabla 4-6: Resumen estimación de emisiones (MP** **10** **) ampliación Chilemink - Fase de Construcción****

| Actividades | MP [ton/año]<br>10 |
| --- | --- |
| Escarpe | 0,0610 |
| Excavación | 0,0018 |
| Circulación de vehículos por caminos pavimentados | 0,0017 |
| Circulación de vehículos por caminos no pavimentados | 0,0060 |
| Gases de combustión de vehículos | 0,0000 |
| Gases de combustión de maquinaria | 0,0017 |
| **Total [ton/año]** | **0,06461 ** |

<!-- Estadísticas: 7 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia. **Tabla 4-7: Resumen estimación de emisiones (MP** **2,5** **) ampliación Chilemink - Fase de Construcción** -->
<!-- FIN TABLA 4-6 -->


|Actividades|MP [ton/año]<br>10|
|---|---|
|Escarpe|0,0610|
|Excavación|0,0018|
|Circulación de vehículos por caminos pavimentados|0,0017|
|Circulación de vehículos por caminos no pavimentados|0,0060|
|Gases de combustión de vehículos|0,0000|
|Gases de combustión de maquinaria|0,0017|
|**Total [ton/año]**|**0,06461 **|

Fuente: Elaboración Propia.

**Tabla 4-7: Resumen estimación de emisiones (MP** **2,5** **) ampliación Chilemink - Fase de Construcción**

<!-- INICIO TABLA 4-7 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Gases de combustión de maquinaria|0,0017| |**Total [ton/año]**|**0,06461 **| Fuente: Elaboración Propia. -->

**Tabla 4-7: Resumen estimación de emisiones (MP** **2,5** **) ampliación Chilemink - Fase de Construcción****

| Actividades | MP [ton/año]<br>2,5 |
| --- | --- |
| Escarpe | 0,0092 |
| Excavación | 0,0010 |
| Circulación de vehículos por caminos pavimentados | 0,0004 |
| Circulación de vehículos por caminos no pavimentados | 0,0006 |
| Gases de combustión de vehículos | 0,0000 |

<!-- Estadísticas: 5 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- 1 Excluye de la sumatoria aquellas actividades en rojo. |Actividades|MP [ton/año]<br>2,5| |---|---| -->
<!-- FIN TABLA 4-7 -->


|Actividades|MP [ton/año]<br>2,5|
|---|---|
|Escarpe|0,0092|
|Excavación|0,0010|
|Circulación de vehículos por caminos pavimentados|0,0004|
|Circulación de vehículos por caminos no pavimentados|0,0006|
|Gases de combustión de vehículos|0,0000|

1 Excluye de la sumatoria aquellas actividades en rojo.

|Actividades|MP [ton/año]<br>2,5|
|---|---|
|Gases de combustión de maquinaria|0,0016|
|**Total [ton/año]**|**0,0118**|

Fuente: Elaboración Propia.

**Tabla 4-8: Resumen estimación de emisiones (MP** **10** **) ampliación Chilemink - Fase de Operación**

<!-- INICIO TABLA 4-8 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Gases de combustión de maquinaria|0,0016| |**Total [ton/año]**|**0,0118**| Fuente: Elaboración Propia. -->

**Tabla 4-8: Resumen estimación de emisiones (MP** **10** **) ampliación Chilemink - Fase de Operación****

| Actividades | MP [ton/año]<br>10 |
| --- | --- |
| Escarpe | 0,0610 |
| Circulación de vehículos por caminos pavimentados | 0,0030 |
| Circulación de vehículos por caminos no pavimentados | 0,0892 |
| Gases de combustión de vehículos | 0,0000 |
| Gases de combustión de maquinaria | 0,0028 |
| Gases de combustión de grupo electrógeno | 0,0175 |
| **Total [ton/año]** | **0,1705** |

<!-- Estadísticas: 7 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia. **Tabla 4-9: Resumen estimación de emisiones (MP** **2,5** **) ampliación Chilemink - Fase de Operación** -->
<!-- FIN TABLA 4-8 -->


|Actividades|MP [ton/año]<br>10|
|---|---|
|Escarpe|0,0610|
|Circulación de vehículos por caminos pavimentados|0,0030|
|Circulación de vehículos por caminos no pavimentados|0,0892|
|Gases de combustión de vehículos|0,0000|
|Gases de combustión de maquinaria|0,0028|
|Gases de combustión de grupo electrógeno|0,0175|
|**Total [ton/año]**|**0,1705**|

Fuente: Elaboración Propia.

**Tabla 4-9: Resumen estimación de emisiones (MP** **2,5** **) ampliación Chilemink - Fase de Operación**

<!-- INICIO TABLA 4-9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Gases de combustión de grupo electrógeno|0,0175| |**Total [ton/año]**|**0,1705**| Fuente: Elaboración Propia. -->

**Tabla 4-9: Resumen estimación de emisiones (MP** **2,5** **) ampliación Chilemink - Fase de Operación****

| Actividades | MP [ton/año]<br>2,5 |
| --- | --- |
| Escarpe | 0,0092 |
| Circulación de vehículos por caminos pavimentados | 0,0007 |
| Circulación de vehículos por caminos no pavimentados | 0,0089 |
| Gases de combustión de vehículos | 0,0000 |
| Gases de combustión de maquinaria | 0,0027 |
| Gases de combustión de grupo electrógeno | 0,0175 |
| **Total [ton/año]** | **0,0383** |

<!-- Estadísticas: 7 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia. Para la modelación, su análisis y evaluación se excluyen el material particulado fino (MP 2,5 ) y los gases de -->
<!-- FIN TABLA 4-9 -->


|Actividades|MP [ton/año]<br>2,5|
|---|---|
|Escarpe|0,0092|
|Circulación de vehículos por caminos pavimentados|0,0007|
|Circulación de vehículos por caminos no pavimentados|0,0089|
|Gases de combustión de vehículos|0,0000|
|Gases de combustión de maquinaria|0,0027|
|Gases de combustión de grupo electrógeno|0,0175|
|**Total [ton/año]**|**0,0383**|

Fuente: Elaboración Propia.

Para la modelación, su análisis y evaluación se excluyen el material particulado fino (MP 2,5 ) y los gases de

combustión como CO, NO x, NH 3, SO x, y COV’s. Esto se determina debido al bajo aporte en niveles de

emisión que el Anexo 6.4, correspondiente a la estimación de emisiones arrojó al realizar los cálculos y

proyecciones. Si bien los niveles de MP 10 también se podrían considerar mínimos, es el contaminante que

mayor carga posee en fase de construcción y operación. Adicionalmente las actividades de circulación de

vehículos por caminos pavimentados y no pavimentados se excluyen del análisis debido a que no se

realizan propiamente tal en el área de influencia del Proyecto en su fase de construcción; mientras que

para la fase de operación se integran al análisis aquellos trayectos por caminos no pavimentados dado que

suceden dentro de las instalaciones de Chilemink.

**4.4 R** **ECEPTORES CONSIDERADOS EN LA MODELACIÓN**

A continuación, se presentan los receptores identificados para el Proyecto, los cuales son correspondientes

con los utilizados en la modelación de dispersión de olores (ver Anexo VI de DIA).

**Tabla 4-10: Receptores en el área de influencia**

<!-- INICIO TABLA 4-10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- A continuación, se presentan los receptores identificados para el Proyecto, los cuales son correspondientes con los utilizados en la modelación de dispersión de olores (ver Anexo VI de DIA). -->

**Tabla 4-10: Receptores en el área de influencia****

| ID | Descripción | Uso<br>efectivo | Coordenadas UTM<br>Datum WGS 84 Huso 19 K | Col5 |
| --- | --- | --- | --- | --- |
| **ID** | **Descripción** | **Uso**<br>**efectivo** | **Este (m)** | **Norte (m)** |
| **R1** | Angostura Golf Country Club ubicado al<br>norponiente de la Planta | Habitacional | 342.708 | 6.241.943 |
| **R2** | Loteo residencial ubicado al poniente de la<br>Planta | Habitacional | 343.030 | 6.240.455 |
| **R3** | Viviendas ubicadas al sur de la Planta | Habitacional | 343.418 | 6.239.582 |
| **R4** | Localidad de O’Higgins de Pilay ubicada al<br>nororiente de la Planta | Habitacional | 347.452 | 6.242.217 |
| **R5** | Vivienda ubicada al poniente de la Planta2 | Habitacional | 343.766 | 6.240.449 |
| **R6** | Vivienda ubicada al sur de la Planta3 | Habitacional | 343.991 | 6.240.377 |
| **R7** | Galpón Planta el Milagro Agrosuper ubicada<br>al oriente de la Planta4 | Industrial | 344.035 | 6.240.530 |
| **R8** | Galpón Industrial ubicado al norponiente de<br>la Planta5 | Industrial | 343.528 | 6.240.747 |

<!-- Estadísticas: 9 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia. 2 Corresponde al Receptor N°1 del Informe de Ruido y Vibraciones (Anexo II-2 de la DIA). 3 Corresponde al Receptor N°2 del Informe de Ruido y Vibraciones (Anexo II-2 de la DIA). -->
<!-- FIN TABLA 4-10 -->


|ID|Descripción|Uso<br>efectivo|Coordenadas UTM<br>Datum WGS 84 Huso 19 K|Col5|
|---|---|---|---|---|
|**ID**|**Descripción**|**Uso**<br>**efectivo**|**Este (m)**|**Norte (m)**|
|**R1**|Angostura Golf Country Club ubicado al<br>norponiente de la Planta|Habitacional|342.708|6.241.943|
|**R2**|Loteo residencial ubicado al poniente de la<br>Planta|Habitacional|343.030|6.240.455|
|**R3**|Viviendas ubicadas al sur de la Planta|Habitacional|343.418|6.239.582|
|**R4**|Localidad de O’Higgins de Pilay ubicada al<br>nororiente de la Planta|Habitacional|347.452|6.242.217|
|**R5**|Vivienda ubicada al poniente de la Planta2|Habitacional|343.766|6.240.449|
|**R6**|Vivienda ubicada al sur de la Planta3|Habitacional|343.991|6.240.377|
|**R7**|Galpón Planta el Milagro Agrosuper ubicada<br>al oriente de la Planta4|Industrial|344.035|6.240.530|
|**R8**|Galpón Industrial ubicado al norponiente de<br>la Planta5|Industrial|343.528|6.240.747|

Fuente: Elaboración Propia.

2 Corresponde al Receptor N°1 del Informe de Ruido y Vibraciones (Anexo II-2 de la DIA).
3 Corresponde al Receptor N°2 del Informe de Ruido y Vibraciones (Anexo II-2 de la DIA).
4 Corresponde al Receptor N°3 del Informe de Ruido y Vibraciones (Anexo II-2 de la DIA).
5 Corresponde al Receptor N°4 del Informe de Ruido y Vibraciones (Anexo II-2 de la DIA).

**Figura 4-2: Ubicación receptores de discretos**

Fuente: Elaboración Propia.

A continuación, en la Tabla 4-11 y Tabla 4-12, se presentan las tasas de emisión de material particulado

grueso (MP10) generadas durante la fase de construcción del proyecto en relación a los gramos emitidos

por segundo por metro cuadrado en una superficie que corresponde al área destinada al riego y cultivo de

forraje (30.000 m2).

**Tabla 4-11: Tasas de emisión MP** **10** **- Fase de Construcción**

<!-- INICIO TABLA 4-11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- por segundo por metro cuadrado en una superficie que corresponde al área destinada al riego y cultivo de forraje (30.000 m2). -->

**Tabla 4-11: Tasas de emisión MP** **10** **- Fase de Construcción****

| Fuente de emisión | MP (ton/año)<br>10 | MP (g/s)<br>10 | MP (g/s/m2)<br>10 |
| --- | --- | --- | --- |
| Gases de combustión de vehículos | 0,0000 | 0,0000 | 1,E-11 |
| Gases de combustión de maquinaria | 0,0017 | 0,0001 | 2,E-09 |
| **Total [ton/año]** | **0,0646** | **0,0020** | **7,E-08** |

<!-- Estadísticas: 3 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia. **Tabla 4-12: Tasas de emisión MP** **2,5** **- Fase de Construcción** -->
<!-- FIN TABLA 4-11 -->


|Fuente de emisión|MP (ton/año)<br>10|MP (g/s)<br>10|MP (g/s/m2)<br>10|
|---|---|---|---|
|Escarpe|0,0610|0,0019|6,E-08|
|Excavación|0,0018|0,0001|2,E-09|
|Circulación de vehículos por caminos<br>pavimentados|0,0017|0,0001|2,E-09|
|Circulación de vehículos por caminos<br>no pavimentados|0,0060|0,0002|6,E-09|

|Fuente de emisión|MP (ton/año)<br>10|MP (g/s)<br>10|MP (g/s/m2)<br>10|
|---|---|---|---|
|Gases de combustión de vehículos|0,0000|0,0000|1,E-11|
|Gases de combustión de maquinaria|0,0017|0,0001|2,E-09|
|**Total [ton/año]**|**0,0646**|**0,0020**|**7,E-08**|

Fuente: Elaboración Propia.

**Tabla 4-12: Tasas de emisión MP** **2,5** **- Fase de Construcción**

<!-- INICIO TABLA 4-12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Gases de combustión de maquinaria|0,0017|0,0001|2,E-09| |**Total [ton/año]**|**0,0646**|**0,0020**|**7,E-08**| Fuente: Elaboración Propia. -->

**Tabla 4-12: Tasas de emisión MP** **2,5** **- Fase de Construcción****

| Fuente de emisión | MP (ton/año)<br>2,5 | MP (g/s)<br>2,5 | MP (g/s/m2)<br>2,5 |
| --- | --- | --- | --- |
| Escarpe | 0,0092 | 0,0003 | 1,E-08 |
| Excavación | 0,0010 | 0,0000 | 1,E-09 |
| Circulación de vehículos por caminos<br>pavimentados | 0,0004 | 0,0000 | 4,E-10 |
| Circulación de vehículos por caminos<br>no pavimentados | 0,0006 | 0,0000 | 6,E-10 |
| Gases de combustión de vehículos | 0,0000 | 0,0000 | 1,E-11 |
| Gases de combustión de maquinaria | 0,0016 | 0,0001 | 2,E-09 |
| **Total [ton/año]** | **0,0118** | **0,0004** | **0,0000** |

<!-- Estadísticas: 7 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia. A continuación, en la Tabla 4-13 y Tabla 4-14, se presentan las tasas de emisión de material particulado -->
<!-- FIN TABLA 4-12 -->


|Fuente de emisión|MP (ton/año)<br>2,5|MP (g/s)<br>2,5|MP (g/s/m2)<br>2,5|
|---|---|---|---|
|Escarpe|0,0092|0,0003|1,E-08|
|Excavación|0,0010|0,0000|1,E-09|
|Circulación de vehículos por caminos<br>pavimentados|0,0004|0,0000|4,E-10|
|Circulación de vehículos por caminos<br>no pavimentados|0,0006|0,0000|6,E-10|
|Gases de combustión de vehículos|0,0000|0,0000|1,E-11|
|Gases de combustión de maquinaria|0,0016|0,0001|2,E-09|
|**Total [ton/año]**|**0,0118**|**0,0004**|**0,0000**|

Fuente: Elaboración Propia.

A continuación, en la Tabla 4-13 y Tabla 4-14, se presentan las tasas de emisión de material particulado

grueso (MP10) generadas durante la fase de operación del proyecto en relación a los gramos emitidos por

segundo por metro cuadrado en una superficie que corresponde al área destinada al riego y cultivo de

forraje (30.000 m2). Si bien la circulación de vehículos por caminos no pavimentados (actividad con mayor

carga de emisión) no ocurre en el área de riego y cultivo de forraje, se modela igualmente en esta zona a

modo de simplificar la proyección del modelo.

**Tabla 4-13: Tasas de emisión MP** **10** **- Fase de Operación**

<!-- INICIO TABLA 4-13 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- carga de emisión) no ocurre en el área de riego y cultivo de forraje, se modela igualmente en esta zona a modo de simplificar la proyección del modelo. -->

**Tabla 4-13: Tasas de emisión MP** **10** **- Fase de Operación****

| Fuente de emisión | MP (ton/año)<br>10 | MP (g/s)<br>10 | MP (g/s/m2)<br>10 |
| --- | --- | --- | --- |
| Gases de combustión de vehículos | 0,0000 | 0,0000 | 3,E-11 |
| Gases de combustión de maquinaria | 0,0028 | 0,0001 | 3,E-09 |
| Gases de combustión de grupo<br>electrógeno | 0,0175 | 0,0006 | 2,E-08 |
| **Total [ton/año]**<br> | **0,1705**<br> | **0,0054** | **2,E-07** |

<!-- Estadísticas: 4 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia. **Tabla 4-14: Tasas de emisión MP** **2,5** **- Fase de Operación** -->
<!-- FIN TABLA 4-13 -->


|Fuente de emisión|MP (ton/año)<br>10|MP (g/s)<br>10|MP (g/s/m2)<br>10|
|---|---|---|---|
|Escarpe|0,0610|0,0019|6,E-08|
|Circulación de vehículos por caminos<br>pavimentados|0,0030|0,0001|3,E-09|
|Circulación de vehículos por caminos<br>no pavimentados|0,0892|0,0028|9,E-08|

|Fuente de emisión|MP (ton/año)<br>10|MP (g/s)<br>10|MP (g/s/m2)<br>10|
|---|---|---|---|
|Gases de combustión de vehículos|0,0000|0,0000|3,E-11|
|Gases de combustión de maquinaria|0,0028|0,0001|3,E-09|
|Gases de combustión de grupo<br>electrógeno|0,0175|0,0006|2,E-08|
|**Total [ton/año]**<br>|**0,1705**<br>|**0,0054**|**2,E-07**|

Fuente: Elaboración Propia.

**Tabla 4-14: Tasas de emisión MP** **2,5** **- Fase de Operación**

<!-- INICIO TABLA 4-14 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Gases de combustión de grupo<br>electrógeno|0,0175|0,0006|2,E-08| |**Total [ton/año]**<br>|**0,1705**<br>|**0,0054**|**2,E-07**| Fuente: Elaboración Propia. -->

**Tabla 4-14: Tasas de emisión MP** **2,5** **- Fase de Operación****

| Fuente de emisión | MP (ton/año)<br>2,5 | MP (g/s)<br>2,5 | MP (g/s/m2)<br>2,5 |
| --- | --- | --- | --- |
| Escarpe | 0,0092 | 0,0003 | 1,E-08 |
| Circulación de vehículos por caminos<br>pavimentados | 0,0007 | 0,0000 | 8,E-10 |
| Circulación de vehículos por caminos<br>no pavimentados | 0,0089 | 0,0003 | 9,E-09 |
| Gases de combustión de vehículos | 0,0000 | 0,0000 | 3,E-11 |
| Gases de combustión de maquinaria | 0,0027 | 0,0001 | 3,E-09 |
| Gases de combustión de grupo<br>electrógeno | 0,0175 | 0,0006 | 2,E-08 |
| **Total [ton/año]**<br> | **0,0383**<br> | **0,0012** | **4,E-08** |

<!-- Estadísticas: 7 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia. ### 5 R ESULTADOS -->
<!-- FIN TABLA 4-14 -->


|Fuente de emisión|MP (ton/año)<br>2,5|MP (g/s)<br>2,5|MP (g/s/m2)<br>2,5|
|---|---|---|---|
|Escarpe|0,0092|0,0003|1,E-08|
|Circulación de vehículos por caminos<br>pavimentados|0,0007|0,0000|8,E-10|
|Circulación de vehículos por caminos<br>no pavimentados|0,0089|0,0003|9,E-09|
|Gases de combustión de vehículos|0,0000|0,0000|3,E-11|
|Gases de combustión de maquinaria|0,0027|0,0001|3,E-09|
|Gases de combustión de grupo<br>electrógeno|0,0175|0,0006|2,E-08|
|**Total [ton/año]**<br>|**0,0383**<br>|**0,0012**|**4,E-08**|

Fuente: Elaboración Propia.

### 5 R ESULTADOS

**5.1 R** **ESULTADOS DE LA** **M** **ODELACIÓN**

A continuación, se exponen los resultados del modelo screening configurado para representar las

condiciones de Proyecto. En Apéndice A se adjuntan los archivos de salida de la modelación.

5.1.1 P ROYECCIÓN DE LAS CONCENTRACIONES EN RECEPTORES DISCRETOS RESPECTO A

NORMA D.S. 12/2021.

A continuación, se presentan los resultados de las concentraciones de material particulado respirable en

su fracción gruesa (MP 10 ) para las concentraciones en 24 horas y anuales. Como es posible apreciar los

valores se encuentran muy por debajo del valor normativo (130 μ/m [3] MP 10 en 24 horas y 50 μ/m [3] N MP 10

anual), los cuales no es posible representar en las gráficas considerando las bajas concentraciones

resultantes. En la Tabla 5-1 se presentan las concentraciones horarias para la fase de construcción del

Proyecto, extraídas desde Screen View y estas mismas calculadas con sus factores de corrección

correspondientes a los aportes diarios y anuales de MP 10 para ser evaluados con respecto a la norma del

contaminante.

**Tabla 5-1: Concentraciones MP** **10** **- Fase de Construcción**

<!-- INICIO TABLA 5-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- correspondientes a los aportes diarios y anuales de MP 10 para ser evaluados con respecto a la norma del contaminante. -->

**Tabla 5-1: Concentraciones MP** **10** **- Fase de Construcción****

| Receptores<br>Discretos | Distancia al<br>centro del<br>área (m) | Concentración<br>Horaria MP<br>10<br>(μ/m3) | Aporte del Proyecto MP<br>10<br>(μ/m3) | Col5 | Norma MP<br>10<br>(μ/m3) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptores**<br>**Discretos** | **Distancia al**<br>**centro del**<br>**área (m)** | **Concentración**<br>**Horaria MP10**<br>**(μ/m3) ** | **Diaria (24 h)** | **Anual** | **Diaria**<br>**(24 h)** | **Anual** |
| R1 | 1.642 | 0,0337 | 0,0135 | 0,0027 | 130 | 50 |
| R2 | 663 | 0,0877 | 0,0351 | 0,0070 | 130 | 50 |
| R3 | 1.066 | 0,0490 | 0,0196 | 0,0039 | 130 | 50 |
| R4 | 4.106 | 0,0151 | 0,0060 | 0,0012 | 130 | 50 |
| R5 | 187 | 0,7440 | 0,2976 | 0,0595 | 130 | 50 |
| R6 | 392 | 0,2262 | 0,0905 | 0,0181 | 130 | 50 |
| R7 | 372 | 0,2478 | 0,0991 | 0,0198 | 130 | 50 |
| R8 | 201 | 0,6595<br> | 0,2638<br> | 0,0528 | 130 | 50 |

<!-- Estadísticas: 9 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia. Como es posible ver en la tabla anterior se evidencian aportes poco significativos a la atmosfera en MP 10 -->
<!-- FIN TABLA 5-1 -->


|Receptores<br>Discretos|Distancia al<br>centro del<br>área (m)|Concentración<br>Horaria MP<br>10<br>(μ/m3)|Aporte del Proyecto MP<br>10<br>(μ/m3)|Col5|Norma MP<br>10<br>(μ/m3)|Col7|
|---|---|---|---|---|---|---|
|**Receptores**<br>**Discretos**|**Distancia al**<br>**centro del**<br>**área (m)**|**Concentración**<br>**Horaria MP10**<br>**(μ/m3) **|**Diaria (24 h)**|**Anual**|**Diaria**<br>**(24 h)**|**Anual**|
|R1|1.642|0,0337|0,0135|0,0027|130|50|
|R2|663|0,0877|0,0351|0,0070|130|50|
|R3|1.066|0,0490|0,0196|0,0039|130|50|
|R4|4.106|0,0151|0,0060|0,0012|130|50|
|R5|187|0,7440|0,2976|0,0595|130|50|
|R6|392|0,2262|0,0905|0,0181|130|50|
|R7|372|0,2478|0,0991|0,0198|130|50|
|R8|201|0,6595<br>|0,2638<br>|0,0528|130|50|

Fuente: Elaboración Propia.

Como es posible ver en la tabla anterior se evidencian aportes poco significativos a la atmosfera en MP 10

considerando que el receptor más cercano (187m) presenta una concentración diaria de 0,2976 μg/m3 y

anual de 0,0595 μg/m3 los que claramente se van reduciendo a medida que aumenta la distancia desde el

centro del área de emisión hasta los diferentes receptores. Adicionalmente se presenta el grafico resultante

de la modelación en Screen View a continuación:

**Figura 5-1: Concentraciones MP** **10** **VS distancia (fase de construcción)**

Fuente: Elaboración Propia.

**Tabla 5-2: Concentraciones MP** **2,5** **- Fase de Construcción**

<!-- INICIO TABLA 5-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Figura 5-1: Concentraciones MP** **10** **VS distancia (fase de construcción)** Fuente: Elaboración Propia. -->

**Tabla 5-2: Concentraciones MP** **2,5** **- Fase de Construcción****

| Receptores<br>Discretos | Distancia al<br>centro del<br>área (m) | Concentración<br>Horaria MP<br>2,5<br>(μ/m3) | Aporte del Proyecto MP<br>2,5<br>(μ/m3) | Col5 | Norma MP<br>2,5<br>(μ/m3) | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptores**<br>**Discretos** | **Distancia al**<br>**centro del**<br>**área (m)** | **Concentración**<br>**Horaria MP2,5**<br>**(μ/m3) ** | **Diaria (24 h)** | **Anual** | **Diaria**<br>**(24 h)** | **Anual** |
| R1 | 1.642 | 0,0613 | 0,0245 | 0,0049 | 50 | 20 |
| R2 | 663 | 0,0160 | 0,0064 | 0,0013 | 50 | 20 |
| R3 | 1.066 | 0,0089 | 0,0036 | 0,0007 | 50 | 20 |
| R4 | 4.106 | 0,0027 | 0,0011 | 0,0002 | 50 | 20 |
| R5 | 187 | 0,1355 | 0,0542 | 0,0108 | 50 | 20 |
| R6 | 392 | 0,0412 | 0,0165 | 0,0033 | 50 | 20 |
| R7 | 372 | 0,0451 | 0,0180 | 0,0036 | 50 | 20 |
| R8 | 201 | 0,1201<br> | 0,0480<br> | 0,0096 | 50 | 20 |

<!-- Estadísticas: 9 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia. Como es posible ver en la tabla anterior se evidencian aportes poco significativos a la atmosfera en MP 2,5 -->
<!-- FIN TABLA 5-2 -->


|Receptores<br>Discretos|Distancia al<br>centro del<br>área (m)|Concentración<br>Horaria MP<br>2,5<br>(μ/m3)|Aporte del Proyecto MP<br>2,5<br>(μ/m3)|Col5|Norma MP<br>2,5<br>(μ/m3)|Col7|
|---|---|---|---|---|---|---|
|**Receptores**<br>**Discretos**|**Distancia al**<br>**centro del**<br>**área (m)**|**Concentración**<br>**Horaria MP2,5**<br>**(μ/m3) **|**Diaria (24 h)**|**Anual**|**Diaria**<br>**(24 h)**|**Anual**|
|R1|1.642|0,0613|0,0245|0,0049|50|20|
|R2|663|0,0160|0,0064|0,0013|50|20|
|R3|1.066|0,0089|0,0036|0,0007|50|20|
|R4|4.106|0,0027|0,0011|0,0002|50|20|
|R5|187|0,1355|0,0542|0,0108|50|20|
|R6|392|0,0412|0,0165|0,0033|50|20|
|R7|372|0,0451|0,0180|0,0036|50|20|
|R8|201|0,1201<br>|0,0480<br>|0,0096|50|20|

Fuente: Elaboración Propia.

Como es posible ver en la tabla anterior se evidencian aportes poco significativos a la atmosfera en MP 2,5

considerando que el receptor más cercano (187m) presenta una concentración diaria de 0,0542 μg/m3 y

anual de 0,0108 μg/m3 los que claramente se van reduciendo a medida que aumenta la distancia desde el

centro del área de emisión hasta los diferentes receptores. Adicionalmente se presenta el grafico resultante

de la modelación en Screen View a continuación:

**Figura 5-2: Concentraciones MP** **2,5** **VS distancia (fase de construcción)**

Fuente: Elaboración Propia.

En la Tabla 5-3 se presentan las concentraciones horarias para la fase de operación del Proyecto, extraídas

desde Screen View y estas mismas calculadas con sus factores de corrección correspondientes a los

aportes diarios y anuales de MP 10 y MP 2,5 para ser evaluados con respecto a la norma del contaminante.

**Tabla 5-3: Concentraciones MP** **10** **- Fase de Operación**

<!-- INICIO TABLA 5-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- desde Screen View y estas mismas calculadas con sus factores de corrección correspondientes a los aportes diarios y anuales de MP 10 y MP 2,5 para ser evaluados con respecto a la norma del contaminante. -->

**Tabla 5-3: Concentraciones MP** **10** **- Fase de Operación****

| Receptores<br>Discretos | Distancia al<br>centro del<br>área (m) | Concentración<br>Horaria MP<br>10<br>(μ/m3) | Aporte del Proyecto MP<br>10<br>(μ/m3) | Col5 | Norma MP (μ/m3)<br>10 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptores**<br>**Discretos** | **Distancia al**<br>**centro del**<br>**área (m)** | **Concentración**<br>**Horaria MP10**<br>**(μ/m3) ** | **Diaria (24 h)** | **Anual** | **Diaria**<br>**(24 h)** | **Anual** |
| R1 | 1.642 | 0,0889 | 0,0356 | 0,0071 | 130 | 50 |
| R2 | 663 | 0,2317 | 0,0927 | 0,0185 | 130 | 50 |
| R3 | 1.066 | 0,1295 | 0,0518 | 0,0104 | 130 | 50 |
| R4 | 4.106 | 0,0398 | 0,0159 | 0,0032 | 130 | 50 |
| R5 | 187 | 1,9650 | 0,7860 | 0,1572 | 130 | 50 |
| R6 | 392 | 0,5975 | 0,2390 | 0,0478 | 130 | 50 |
| R7 | 372 | 0,6544 | 0,2618 | 0,0524 | 130 | 50 |
| R8 | 201 | 1,7420<br> | 0,6968<br> | 0,1394 | 130 | 50 |

<!-- Estadísticas: 9 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia. Como es posible ver en la tabla anterior se evidencian aportes poco significativos a la atmosfera en MP 10 -->
<!-- FIN TABLA 5-3 -->


|Receptores<br>Discretos|Distancia al<br>centro del<br>área (m)|Concentración<br>Horaria MP<br>10<br>(μ/m3)|Aporte del Proyecto MP<br>10<br>(μ/m3)|Col5|Norma MP (μ/m3)<br>10|Col7|
|---|---|---|---|---|---|---|
|**Receptores**<br>**Discretos**|**Distancia al**<br>**centro del**<br>**área (m)**|**Concentración**<br>**Horaria MP10**<br>**(μ/m3) **|**Diaria (24 h)**|**Anual**|**Diaria**<br>**(24 h)**|**Anual**|
|R1|1.642|0,0889|0,0356|0,0071|130|50|
|R2|663|0,2317|0,0927|0,0185|130|50|
|R3|1.066|0,1295|0,0518|0,0104|130|50|
|R4|4.106|0,0398|0,0159|0,0032|130|50|
|R5|187|1,9650|0,7860|0,1572|130|50|
|R6|392|0,5975|0,2390|0,0478|130|50|
|R7|372|0,6544|0,2618|0,0524|130|50|
|R8|201|1,7420<br>|0,6968<br>|0,1394|130|50|

Fuente: Elaboración Propia.

Como es posible ver en la tabla anterior se evidencian aportes poco significativos a la atmosfera en MP 10

considerando que el receptor más cercano (187m) presenta una concentración diaria de 0,7860 μg/m3 y

anual de 0,1572 μg/m3 los que claramente se van reduciendo a medida que aumenta la distancia desde el

centro del área de emisión hasta los diferentes receptores. Adicionalmente se presenta el grafico resultante

de la modelación en Screen View a continuación:

**Figura 5-3: Concentraciones MP** **10** **VS distancia (fase de operación)**

Fuente: Elaboración Propia.

**Tabla 5-4: Concentraciones MP** **2,5** **- Fase de Operación**

<!-- INICIO TABLA 5-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **Figura 5-3: Concentraciones MP** **10** **VS distancia (fase de operación)** Fuente: Elaboración Propia. -->

**Tabla 5-4: Concentraciones MP** **2,5** **- Fase de Operación****

| Receptores<br>Discretos | Distancia al<br>centro del<br>área (m) | Concentración<br>Horaria MP<br>2,5<br>(μ/m3) | Aporte del Proyecto MP<br>2,5<br>(μ/m3) | Col5 | Norma MP (μ/m3)<br>2,5 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptores**<br>**Discretos** | **Distancia al**<br>**centro del**<br>**área (m)** | **Concentración**<br>**Horaria MP2,5 **<br>**(μ/m3) ** | **Diaria (24 h)** | **Anual** | **Diaria**<br>**(24 h)** | **Anual** |
| R1 | 1.642 | 0,0199 | 0,0080 | 0,0016 | 50 | 20 |
| R2 | 663 | 0,0520 | 0,0208 | 0,0042 | 50 | 20 |
| R3 | 1.066 | 0,0291 | 0,0116 | 0,0023 | 50 | 20 |
| R4 | 4.106 | 0,0089 | 0,0036 | 0,0007 | 50 | 20 |
| R5 | 187 | 0,4410 | 0,1764 | 0,0353 | 50 | 20 |
| R6 | 392 | 0,1341 | 0,0536 | 0,0107 | 50 | 20 |
| R7 | 372 | 0,1468 | 0,0587 | 0,0117 | 50 | 20 |
| R8 | 201 | 0,3909<br> | 0,1564<br> | 0,0313 | 50 | 20 |

<!-- Estadísticas: 9 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración Propia. Como es posible ver en la tabla anterior se evidencian aportes poco significativos a la atmosfera en MP 10 -->
<!-- FIN TABLA 5-4 -->


|Receptores<br>Discretos|Distancia al<br>centro del<br>área (m)|Concentración<br>Horaria MP<br>2,5<br>(μ/m3)|Aporte del Proyecto MP<br>2,5<br>(μ/m3)|Col5|Norma MP (μ/m3)<br>2,5|Col7|
|---|---|---|---|---|---|---|
|**Receptores**<br>**Discretos**|**Distancia al**<br>**centro del**<br>**área (m)**|**Concentración**<br>**Horaria MP2,5 **<br>**(μ/m3) **|**Diaria (24 h)**|**Anual**|**Diaria**<br>**(24 h)**|**Anual**|
|R1|1.642|0,0199|0,0080|0,0016|50|20|
|R2|663|0,0520|0,0208|0,0042|50|20|
|R3|1.066|0,0291|0,0116|0,0023|50|20|
|R4|4.106|0,0089|0,0036|0,0007|50|20|
|R5|187|0,4410|0,1764|0,0353|50|20|
|R6|392|0,1341|0,0536|0,0107|50|20|
|R7|372|0,1468|0,0587|0,0117|50|20|
|R8|201|0,3909<br>|0,1564<br>|0,0313|50|20|

Fuente: Elaboración Propia.

Como es posible ver en la tabla anterior se evidencian aportes poco significativos a la atmosfera en MP 10

considerando que el receptor más cercano (187m) presenta una concentración diaria de 0,1764 μg/m3 y

anual de 0,0353 μg/m3 los que claramente se van reduciendo a medida que aumenta la distancia desde el

centro del área de emisión hasta los diferentes receptores. Adicionalmente se presenta el grafico resultante

de la modelación en Screen View a continuación:

**Figura 5-4: Concentraciones MP** **2,5** **VS distancia (fase de operación)**

Fuente: Elaboración Propia.

**5.2 E** **VALUACIÓN EN RECEPTORES SENSIBLES**

De acuerdo con los resultados expuestos para la fase de construcción del Proyecto (Tabla 5-1) es posible

señalar que las concentraciones de MP 10 obtenidas a través de las modelaciones de Screen3 son de 0,23%

diario, y 0,12% anual con respecto al receptor discreto más cercano (vivienda ubicada al poniente de la

planta a 187m).

Por otro lado, con los resultados expuestos para la fase de operación del Proyecto (Tabla 5-3) es posible

señalar que las concentraciones de MP 10 obtenidas a través de las modelaciones de Screen3 son de 0,61%

diario, y 0,31% anual con respecto al receptor discreto más cercano (vivienda ubicada al poniente de la

planta a 187m).

### 6 D ISCUSIONES

**6.1 E** **VALUACIÓN DEL INCREMENTO SIGNIFICATIVO EN LA CONCENTRACIÓN DE MATERIAL**

**PARTICULADO** **(MP** **10** **)**

Para evaluar la significancia en el incremento de las concentraciones obtenidas a través de la modelación

de emisiones atmosféricas en el software Screen View se utilizan como parámetros los criterios contenidos

en la guía “Evaluación significancia del impacto de las emisiones de un proyecto o actividad en zonas

saturadas en el marco del SEIA”, los que se pueden observar en las siguientes tablas presentadas a

continuacion.

A las concentraciones horarias de la modelación realizada en el software se les aplico un factor de

corrección para obtener las concentraciones diarias (24 horas) y anuales con el propósito de considerar la

condición de no superación establecida por D.S. N°12/2022 “Establece norma primaria de calidad ambiental

para material particulado respirable (MP 10 y MP 2,5 )” D.S. N°12/2022 del Ministerio del Medio Ambiente. Pero

adicionalmente los resultados diarios y anuales serán observados respecto los criterios recomendados de

incremento significativo en la concentración de contaminantes atmosféricos en zonas saturadas.

**Tabla 6-1. Comparación de resultados para MP** **10** **- fase de construcción y valores de**
**significancia para el aumento de concentraciones de MP** **10** **sobre receptores humanos**
**discretos para impactos con una duración menor a 3 años en zonas que sobrepasen el**

**valor de la norma**

|Distancia al centro del<br>área (m)|Aporte Proyecto MP (μ/m3)<br>10|Col3|Condición de no<br>Superación (MP )<br>10<br>(μ/m3)|Col5|Condición de<br>no Superación<br>(MP ) (μ/m3)<br>10|Col7|
|---|---|---|---|---|---|---|
|**Distancia al centro del**<br>**área (m)**|**Diaria (24 h)**|**Anual**|**Diaria (24 h)**|**Anual**|**Diaria**<br>**(24 h)**|**Anual**|
|1.642|0,0135|0,0027|10|3|Cumple|Cumple|
|663|0,0351|0,0070|10|3|Cumple|Cumple|
|1.066|0,0196|0,0039|10|3|Cumple|Cumple|
|4.106|0,0060|0,0012|10|3|Cumple|Cumple|
|187|0,2976|0,0595|10|3|Cumple|Cumple|
|392|0,0905|0,0181|10|3|Cumple|Cumple|
|372|0,0991|0,0198|10|3|Cumple|Cumple|
|201|0,2638|0,0528|10|3|Cumple|Cumple|

Fuente: Elaboración Propia.

**Tabla 6-2. Comparación de resultados para MP** **2,5** **- fase de construcción y valores de**
**significancia para el aumento de concentraciones de MP** **2,5** **sobre receptores humanos**
**discretos para impactos con una duración menor a 3 años en zonas que sobrepasen el**

**valor de la norma**

|Distancia al centro del<br>área (m)|Aporte Proyecto MP (μ/m3)<br>2,5|Col3|Condición de no<br>Superación (MP )<br>2,5<br>(μ/m3)|Col5|Condición de<br>no Superación<br>(MP ) (μ/m3)<br>2,5|Col7|
|---|---|---|---|---|---|---|
|**Distancia al centro del**<br>**área (m)**|**Diaria (24 h)**|**Anual**|**Diaria (24 h)**|**Anual**|**Diaria**<br>**(24 h)**|**Anual**|
|1.642|0,0245|0,0049|5,13|0,99|Cumple|Cumple|
|663|0,0064|0,0013|5,13|0,99|Cumple|Cumple|
|1.066|0,0036|0,0007|5,13|0,99|Cumple|Cumple|
|4.106|0,0011|0,0002|5,13|0,99|Cumple|Cumple|
|187|0,0542|0,0108|5,13|0,99|Cumple|Cumple|
|392|0,0165|0,0033|5,13|0,99|Cumple|Cumple|
|372|0,0180|0,0036|5,13|0,99|Cumple|Cumple|
|201|0,0480 <br>|0,0096 <br>|5,13|0,99|Cumple|Cumple|

Fuente: Elaboración Propia.

**Tabla 6-3. Comparación de resultados para MP** **10** **- fase de construcción y valores de**
**significancia para el aumento de concentraciones de MP** **10** **sobre receptores humanos**
**discretos para impactos en un período igual o mayor a 3 años en zonas que sobrepasen el**

**valor de la norma**

|Distancia al centro del<br>área (m)|Aporte Proyecto MP (μ/m3)<br>10|Col3|Condición de no<br>Superación (MP )<br>10<br>(μ/m3)|Col5|Condición de<br>no Superación<br>(MP ) (μ/m3)<br>10|Col7|
|---|---|---|---|---|---|---|
|**Distancia al centro del**<br>**área (m)**|**Diaria (24 h)**|**Anual**|**Diaria (24 h)**|**Anual**|**Diaria**<br>**(24 h)**|**Anual**|
|1.642|0,0356|0,0071|5|1|Cumple|Cumple|
|663|0,0927|0,0185|5|1|Cumple|Cumple|
|1.066|0,0518|0,0104|5|1|Cumple|Cumple|
|4.106|0,0159|0,0032|5|1|Cumple|Cumple|
|187|0,7860|0,1572|5|1|Cumple|Cumple|
|392|0,2390|0,0478|5|1|Cumple|Cumple|
|372|0,2618|0,0524|5|1|Cumple|Cumple|
|201|0,6968|0,1394|5|1|Cumple|Cumple|

Fuente: Elaboración Propia.

**Tabla 6-4. Comparación de resultados para MP** **2,5** **- fase de construcción y valores de**
**significancia para el aumento de concentraciones de MP** **2,5** **sobre receptores humanos**
**discretos para impactos en un período igual o mayor a 3 años en zonas que sobrepasen el**

**valor de la norma**

|Distancia al centro del<br>área (m)|Aporte Proyecto MP (μ/m3)<br>2,5|Col3|Condición de no<br>Superación (MP )<br>2,5<br>(μ/m3)|Col5|Condición de<br>no Superación<br>(MP ) (μ/m3)<br>2,5|Col7|
|---|---|---|---|---|---|---|
|**Distancia al centro del**<br>**área (m)**|**Diaria (24 h)**|**Anual**|**Diaria (24 h)**|**Anual**|**Diaria**<br>**(24 h)**|**Anual**|
|1.642|0,0080|0,0016|1,71|0,33|Cumple|Cumple|
|663|0,0208|0,0042|1,71|0,33|Cumple|Cumple|
|1.066|0,0116|0,0023|1,71|0,33|Cumple|Cumple|
|4.106|0,0036|0,0007|1,71|0,33|Cumple|Cumple|
|187|0,1764|0,0353|1,71|0,33|Cumple|Cumple|
|392|0,0536|0,0107|1,71|0,33|Cumple|Cumple|
|372|0,0587|0,0117|1,71|0,33|Cumple|Cumple|
|201|0,1564 <br>|0,0313 <br>|1,71|0,33|Cumple|Cumple|

Fuente: Elaboración Propia.

**6.2 C** **URVA DE DECAIMIENTO DE LAS CONCENTRACIONES**

Las concentraciones de material particulado en su fracción gruesa (MP 10 ) proveniente de las tasas de

emisiones estimadas a partir del inventario de emisiones realizado para esta evaluación, permite evidenciar

que a medida que las concentraciones se alejan de la fuente emisora tienden a ser nulas, lo que se puede

apreciar en la Figura 5-1 y la Figura 5-3.

En término netos, se estima que sobre los 100 m las concentraciones serán menores a 0,3 μg/m [3] en la

fase de construcción y operación del Proyecto. Adicionalmente se establece que desde la distancia del

receptor discreto más lejano (4.106 metros) las concentraciones se consideran prácticamente nulas.

**6.3 E** **VALUACIÓN EN RECEPTORES SENSIBLES**

Los resultados de la modelación en los receptores sensibles presentan concentraciones muy inferiores a

los valores normativos referenciados. Durante la fase de construcción se observa que, para el MP 10 en 24

horas, tiene su máximo valor en el receptor R5 con 0,298 μg/m [3] y el mínimo valor registrado al R4 con
0,006 μg/m [3] ; En tanto los valores anuales para el contaminante fluctúan entre 0,059 y 0,001 μg/m [3] para los

mismos receptores respectivamente. Durante la fase de construcción se observa que, para el MP 2,5 en 24
horas, tiene su máximo valor en el receptor R5 con 0,054 μg/m [3] y el mínimo valor registrado al R4 con
0,001 μg/m [3] ; En tanto los valores anuales para el contaminante fluctúan entre 0,011 y 0,0002 μg/m [3] para

los mismos receptores respectivamente.

Durante la fase de operación se observa que, para el MP 10 en 24 horas, tiene su máximo valor en el receptor

R5 con 0,786 μg/m [3] y el mínimo valores registrado al R4 con 0,016 μg/m [3] ; En tanto los valores anuales

para el contaminante fluctúan entre 0,157 y 0,003 μg/m [3] para los mismos receptores respectivamente.

Durante la fase de operación se observa que, para el MP 2,5 en 24 horas, tiene su máximo valor en el
receptor R5 con 0,1764 μg/m [3] y el mínimo valores registrado al R4 con 0,004 μg/m [3] ; En tanto los valores
anuales para el contaminante fluctúan entre 0,035 y 0,0007 μg/m [3] para los mismos receptores

respectivamente.

### 7 C ONCLUSIONES

Respecto de la caracterización de línea de base realizada para el Proyecto, es posible evidenciar que la

evaluación corresponde al entorno de la zona en la que se evaluaran las partes, obras y acciones del

Proyecto, las cuales no presentan una condición crítica ambiental determinada por alguna superación de

los umbrales permisibles establecidos en normas primarias de calidad de aire y que deriven en una

situación de latencia (80% del valor de norma) o una saturación de partículas (100% del umbral de norma).

De acuerdo a la modelación realizada, los resultados presentan que las concentraciones obtenidas

representan menos del 0,7% de los valores normativos de referencia utilizados para el material particulado

en su fracción gruesa (MP 10 ) en todas sus fases. Dichos valores fueron obtenidos mediante el empleo de

la metodología screening recomendad por la EPA para el análisis preliminar y conservador del

comportamiento de las emisiones en receptores de interés. En base a lo anterior es posible establecer que

no se requiere un modelo más refinado para descartar una posible afectación de la condición inicial de la

calidad del aire, toda vez que las emisiones presentan concentraciones de poca significancia.

En cuanto a la fase de operación, y considerando que las actividades principales corresponden al riego con

aguas tratadas en la planta de Chilemink del cultivo de material de forraje, y la propia cosecha del mismo.

Por ende, la actividad asociada será periódica durante el año y no relevante desde el punto de vista de la

influencia de las emisiones. De acuerdo a los datos del inventario, se estiman un total de 0,17 ton/año de

MP 10 para la fase de operación del proyecto, los cuales se distribuyen en la trayectoria de los caminos de

tránsito, no constituyéndose como un elemento crítico que demande interés en proyectar su impacto.

### 8 R EFERENCIAS

Decreto Supremo N°12/2022 Ministerio del Medio Ambiente, Establece norma primaria de calidad

ambiental para material particulado respirable (MP 10 ).

EPA, Apéndice W parte 51-40 CFR Directrices para Modelos de Calidad del Aire (Guideline on Air Quality

Models).

Evaluación significancia del impacto de las emisiones de un proyecto o actividad en zonas saturadas en el

marco del SEIA, DICTUC Greenlab, Informe final, marzo de 2022.

SEA 2012, Guía Para el Uso de Modelos de Calidad del Aire en el SEIA

**APÉNDICE A: SALIDAS MODELO SCREEN VIEW**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4-1.: Normativa primaria asociada a calidad del aire.****

| Parámetro | N° Decreto/año | Valor Norma | Periodo de Evaluación de<br>Cumplimiento de Norma |
| --- | --- | --- | --- |
| Material<br>Particulado<br>Respirable<br>(MP10) | Decreto Supremo<br>N°12/2022 (MMA) | 130<br>μg/Nm3, <br>como<br>concentración de 24 horas | Percentil<br>98<br>de<br>las<br>concentraciones<br>de<br>24<br>horas<br>registradas durante un período<br>anual |
| Material<br>Particulado<br>Respirable<br>(MP10) | Decreto Supremo<br>N°12/2022 (MMA) | 50<br>μg/Nm3, <br>como<br>concentración media anual | Media aritmética trianual |
| Material<br>Particulado<br>Respirable<br>Fino (MP2,5) | Decreto Supremo<br>N°12/2022 (MMA) | 50<br>μg/m3, <br>como<br>concentración 24 horas | Percentil<br>98<br>de<br>las<br>concentraciones<br>de<br>24<br>horas<br>registradas durante un período<br>anual |
| Material<br>Particulado<br>Respirable<br>Fino (MP2,5) | Decreto Supremo<br>N°12/2022 (MMA) | 20<br>μg/m3, <br>como<br>concentración media anual | Media aritmética trianual |

**Tabla 4-2.: Valores de significancia para el aumento de concentraciones de MP** **10** **y MP** **2,5** **sobre****

| Parámetro | Periodo | Incremento concentración<br>(μg/m3) |
| --- | --- | --- |
| Material Particulado Respirable (MP10) | 24 horas | 5,0 |
| Material Particulado Respirable (MP10) | Anual | 1,0 |
| Material Particulado Respirable Fino<br>(MP2,5)<br> | 24 horas | 1,71 |
| Material Particulado Respirable Fino<br>(MP2,5)<br> | Anual<br> | 0,33 |

**Tabla 4-3.: Valores de significancia para el aumento de concentraciones de MP** **10** **y MP** **2,5** **sobre****

| Parámetro | Periodo | Incremento concentración<br>(μg/m3) |
| --- | --- | --- |
| Material Particulado Respirable (MP10) | 24 horas | 10,00 |
| Material Particulado Respirable (MP10) | Anual | 3,00 |
| Material Particulado Respirable Fino<br>(MP2,5)<br> | 24 horas | 5,13 |
| Material Particulado Respirable Fino<br>(MP2,5)<br> | Anual<br> | 0,99 |

**Tabla 6-1.: Comparación de resultados para MP** **10** **- fase de construcción y valores de****

| Distancia al centro del<br>área (m) | Aporte Proyecto MP (μ/m3)<br>10 | Col3 | Condición de no<br>Superación (MP )<br>10<br>(μ/m3) | Col5 | Condición de<br>no Superación<br>(MP ) (μ/m3)<br>10 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Distancia al centro del**<br>**área (m)** | **Diaria (24 h)** | **Anual** | **Diaria (24 h)** | **Anual** | **Diaria**<br>**(24 h)** | **Anual** |
| 1.642 | 0,0135 | 0,0027 | 10 | 3 | Cumple | Cumple |
| 663 | 0,0351 | 0,0070 | 10 | 3 | Cumple | Cumple |
| 1.066 | 0,0196 | 0,0039 | 10 | 3 | Cumple | Cumple |
| 4.106 | 0,0060 | 0,0012 | 10 | 3 | Cumple | Cumple |
| 187 | 0,2976 | 0,0595 | 10 | 3 | Cumple | Cumple |
| 392 | 0,0905 | 0,0181 | 10 | 3 | Cumple | Cumple |
| 372 | 0,0991 | 0,0198 | 10 | 3 | Cumple | Cumple |
| 201 | 0,2638 | 0,0528 | 10 | 3 | Cumple | Cumple |

**Tabla 6-2.: Comparación de resultados para MP** **2,5** **- fase de construcción y valores de****

| Distancia al centro del<br>área (m) | Aporte Proyecto MP (μ/m3)<br>2,5 | Col3 | Condición de no<br>Superación (MP )<br>2,5<br>(μ/m3) | Col5 | Condición de<br>no Superación<br>(MP ) (μ/m3)<br>2,5 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Distancia al centro del**<br>**área (m)** | **Diaria (24 h)** | **Anual** | **Diaria (24 h)** | **Anual** | **Diaria**<br>**(24 h)** | **Anual** |
| 1.642 | 0,0245 | 0,0049 | 5,13 | 0,99 | Cumple | Cumple |
| 663 | 0,0064 | 0,0013 | 5,13 | 0,99 | Cumple | Cumple |
| 1.066 | 0,0036 | 0,0007 | 5,13 | 0,99 | Cumple | Cumple |
| 4.106 | 0,0011 | 0,0002 | 5,13 | 0,99 | Cumple | Cumple |
| 187 | 0,0542 | 0,0108 | 5,13 | 0,99 | Cumple | Cumple |
| 392 | 0,0165 | 0,0033 | 5,13 | 0,99 | Cumple | Cumple |
| 372 | 0,0180 | 0,0036 | 5,13 | 0,99 | Cumple | Cumple |
| 201 | 0,0480 <br> | 0,0096 <br> | 5,13 | 0,99 | Cumple | Cumple |

**Tabla 6-3.: Comparación de resultados para MP** **10** **- fase de construcción y valores de****

| Distancia al centro del<br>área (m) | Aporte Proyecto MP (μ/m3)<br>10 | Col3 | Condición de no<br>Superación (MP )<br>10<br>(μ/m3) | Col5 | Condición de<br>no Superación<br>(MP ) (μ/m3)<br>10 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Distancia al centro del**<br>**área (m)** | **Diaria (24 h)** | **Anual** | **Diaria (24 h)** | **Anual** | **Diaria**<br>**(24 h)** | **Anual** |
| 1.642 | 0,0356 | 0,0071 | 5 | 1 | Cumple | Cumple |
| 663 | 0,0927 | 0,0185 | 5 | 1 | Cumple | Cumple |
| 1.066 | 0,0518 | 0,0104 | 5 | 1 | Cumple | Cumple |
| 4.106 | 0,0159 | 0,0032 | 5 | 1 | Cumple | Cumple |
| 187 | 0,7860 | 0,1572 | 5 | 1 | Cumple | Cumple |
| 392 | 0,2390 | 0,0478 | 5 | 1 | Cumple | Cumple |
| 372 | 0,2618 | 0,0524 | 5 | 1 | Cumple | Cumple |
| 201 | 0,6968 | 0,1394 | 5 | 1 | Cumple | Cumple |

**Tabla 6-4.: Comparación de resultados para MP** **2,5** **- fase de construcción y valores de****

| Distancia al centro del<br>área (m) | Aporte Proyecto MP (μ/m3)<br>2,5 | Col3 | Condición de no<br>Superación (MP )<br>2,5<br>(μ/m3) | Col5 | Condición de<br>no Superación<br>(MP ) (μ/m3)<br>2,5 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Distancia al centro del**<br>**área (m)** | **Diaria (24 h)** | **Anual** | **Diaria (24 h)** | **Anual** | **Diaria**<br>**(24 h)** | **Anual** |
| 1.642 | 0,0080 | 0,0016 | 1,71 | 0,33 | Cumple | Cumple |
| 663 | 0,0208 | 0,0042 | 1,71 | 0,33 | Cumple | Cumple |
| 1.066 | 0,0116 | 0,0023 | 1,71 | 0,33 | Cumple | Cumple |
| 4.106 | 0,0036 | 0,0007 | 1,71 | 0,33 | Cumple | Cumple |
| 187 | 0,1764 | 0,0353 | 1,71 | 0,33 | Cumple | Cumple |
| 392 | 0,0536 | 0,0107 | 1,71 | 0,33 | Cumple | Cumple |
| 372 | 0,0587 | 0,0117 | 1,71 | 0,33 | Cumple | Cumple |
| 201 | 0,1564 <br> | 0,0313 <br> | 1,71 | 0,33 | Cumple | Cumple |
