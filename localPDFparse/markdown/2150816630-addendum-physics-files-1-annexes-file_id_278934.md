---
title: Sin título
author: profe
date: D:20210825162233-04'00'
language: es
type: report
pages: 17
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1 Objetivos y Alcance del Estudio
  - 2 Descripción del Proyecto
  - 5 Campo electromagnético de centros de transformación
  - 6 Análisis del campo electromagnético de la línea
-->

**Apéndice IV-3**
**Estudio de Campos Electromagnéticos**

**ESTUDIO DE CAMPO ELECTROMAGNETICO**

**AMPLIACIÓN PARQUE FOTOVOLTAICO EL MONTE SOLAR**

**Nelson Morales Osorio**

**Junio 2021**

**CONTENIDO**

1 Objetivos y Alcance del Estudio............................................................................... 3

2 Descripción del Proyecto ........................................................................................ 3

3 Normas de referencia para campos electromagnéticos de 50 Hz .............................. 5

4 Campo electromagnético en alta tensión ................................................................ 7

5 Campo magnético de centros de transformación ..................................................... 7

6 Análisis del campo electromagnético de la línea ...................................................... 9

7 Conclusiones ..................................................................................................... 14

Referencias ............................................................................................................ 16

**FIGURAS**

Figura 1 Ubicación Proyecto El Monte Solar ....................................................... 4

Figura 2 Instalaciones proyecto El Monte Solar .................................................. 5

Figura 3 Reducción de la inducción magnética de equipos con la distancia ......... 9

Figura 4 Silueta de poste de la línea ............................................................... 10

Figura 5 Malla de elementos finitos ................................................................ 11

Figura 6 Distribución de equipotenciales eléctricas........................................... 11

Figura 7 Campo eléctrico a 1m sobre el suelo bajo línea .................................. 12

Figura 8 Distribución de equipotenciales magnéticas ........................................ 12

Figura 9 Inducción magnética a 1m sobre el suelo bajo línea ........................... 13

**TABLAS**

Tabla 1 Variación de la inducción magnética con distancia al transformador ......... 8

Tabla 2 Valores de campo y confrontación con norma .................................... 13

# 1 Objetivos y Alcance del Estudio

Este Informe presenta una estimación de los campos electromagnéticos de baja y alta

frecuencia que pueden presentarse debido a la ampliación del Parque Fotovoltaico El

Monte Solar, durante la operación de sus instalaciones, con el propósito de dar

respuesta a una consulta de ICSARA.

Se entrega información respecto del campo electromagnético generado por centros de

transformación y los resultados de una simulación para el campo eléctrico y el campo

magnético en el entorno de la línea de transmisión. Para determinar la magnitud de

estos campos, se utiliza un programa computacional que aplica el método de elementos

finitos [1] para modelar la configuración y resolver la ecuación diferencial parcial que

rige el comportamiento de los campos en la región a estudiar.

Los valores indicados se confrontan con las recomendaciones y límites admisibles

[2],[3] para establecer finalmente una conclusión respecto al impacto ambiental de las

instalaciones del parque solar, desde el punto de vista técnico de la emisión

electromagnética de baja frecuencia.

# 2 Descripción del Proyecto

El presente Proyecto corresponde a la ampliación de un proyecto fotovoltaico declarado

en construcción - ante la CNE-, denominado “El Monte Solar” que cuenta con

Resolución Exenta N.° 0098 con fecha 14 de febrero de 2020 otorgado por el Servicio

de Evaluación Ambiental de la Región Metropolitana de Santiago. El Proyecto requiere

aumentar la potencia total nominal del proyecto “El Monte Solar” de 2,99MWac a 9

MWac.

El proyecto se emplaza en la Región Metropolitana de Santiago, Provincia de Talagante,

comuna de El Monte, específicamente en el inmueble denominado "Hijuela Número Uno

Fundo Monte Blanco".

**Figura 1 Ubicación Proyecto El Monte Solar**

Fuente: Titular del proyecto

Se requiere aumentar la potencia nominal del proyecto “El Monte Solar” mediante la

instalación de 20.722 paneles fotovoltaicos, con potencias de 435 y 535 Watts,

aumentando la potencia nominal total a 9 MWac, que corresponderá a la potencia que

finalmente se inyectará a la red de distribución del Sistema Eléctrico Nacional (SEN).

La energía eléctrica producida en los paneles fotovoltaicos se conduce, a través de

cables soterrados, hacia los equipos denominados inversores eléctricos, que convierten

la corriente continua a alterna. Se instalarán un total de 54 inversores.

Luego, esta corriente es conducida hacia un transformador que eleva su nivel de

tensión a 13,2kV. El Proyecto dispondrá de 3 unidades de transformadores las cuales

individualmente cuentan con una potencia 3.150 kVA.

La evacuación de la energía eléctrica producida en el parque fotovoltaico se realizará

mediante una línea aérea de media tensión (13,2 kV) que conectará el Proyecto con su

punto de conexión al poste N° 5-025414. Esta línea eléctrica tendrá una longitud

aproximada de 1.430,0 m. La línea eléctrica aérea estará conformada por postes

simples de hormigón armado, de 11,5 m de altura e irán enterrados a una profundidad

de 1,8 m bajo el nivel del suelo.

**Figura 2 Instalaciones proyecto El Monte Solar**

Fuente: Titular del proyecto

**3 NORMAS DE REFERENCIA PARA CAMPOS ELECTROMAGNÉTICOS DE 50 HZ**

En nuestro país no existe reglamentación específica relativa a los valores límites

permitidos de exposición de las personas a los campos electromagnéticos de frecuencia

industrial. No obstante, la regulación ambiental que rige el tema de emisiones señala

que de no existir una regulación nacional, debe aplicarse como norma de referencia

aquella que se encuentre vigente en estados específicos. El Decreto No 40 del Ministerio

del Medio Ambiente, “Aprueba Reglamento del Sistema de Evaluación de Impacto

Ambiental”, publicado el 12-08-2013, y que entró en vigencia el 24-12-2013, indica en

su Artículo 11:

“Las normas de calidad ambiental y de emisión que se utilizarán como referencia para

los efectos de evaluar si se genera o presenta el riesgo indicado en la letra a) y los

efectos adversos señalados en la letra b), ambas del artículo 11 de la Ley, serán

aquellas vigentes en los siguientes Estados: República Federal de Alemania, República

Argentina, Australia, República Federativa del Brasil, Canadá, Reino de España, Estados

Unidos Mexicanos, Estados Unidos de América, Nueva Zelandia, Reino de los Países

Bajos, República Italiana, Japón, Reino de Suecia y Confederación Suiza. Para la

utilización de las normas de referencia, se priorizará aquel Estado que posea similitud

en sus componentes ambientales, con la situación nacional y/o local, lo que será

justificado razonablemente por el proponente.

La recomendación de uso más frecuente para público general y exposición permanente,

es la publicada por la ICNIRP [2], organismo no gubernamental reconocido por la

Organización Mundial de la Salud como referente en el tema, que establece 5.000

[V/m] para el campo eléctrico y 200 [micro Tesla], para la inducción magnética,

valores que han sido acogidos por la normativa de diversos países incluidos en la

nómina anterior.

Recientemente se ha publicado el PLIEGO TÉCNICO NORMATIVO RPTD N°07 [3],

dictado por Resolución Exenta No 33.277, de fecha 10/09/2020, de la Superintendencia

de Electricidad y Combustibles, que en su Artículo 4.7 establece:

“Los límites máximos permisibles para la seguridad de las personas, en cuanto a la

emisión de campo electromagnético para el diseño de líneas aéreas de corriente alterna

de 50 Hz de frecuencia, y que será evaluado en el exterior de la franja de seguridad, a

1 metro sobre el nivel del suelo, en condiciones normales de operación de la línea, con

los conductores en reposo, serán los que determinen las normas respectivas. En

ausencia de regulación técnica nacional, se debe cumplir con lo siguiente:

5 kV/m para campo eléctrico (valor RMS)

100 μT para campo magnético (valor RMS).”

**4 CAMPO ELECTROMAGNÉTICO EN ALTA TENSIÓN**

La unidad del campo eléctrico es el Volt por metro [V/m] o Kilo Volt por metro [KV/m]

en alta tensión; es dependiente del voltaje de los conductores, en el caso en estudio,

13,2 kV entre fases y 13,2/√3 KV fase a tierra.

El campo magnético se debe a la corriente que circula por los conductores. La magnitud

representativa del campo magnético es la “Inducción Magnética” o “Densidad de Flujo

Magnético” B **,** que tiene como unidad de medida práctica el mili Gauss (1 mG = 10 [-3]

Gauss) o el micro Tesla (1μT = 10 [-6] Tesla ) y se relacionan por: 1 μT = 10 mG.

Para investigar los efectos de los campos electromagnéticos, se acostumbra caracterizar

al campo eléctrico y el campo magnético cerca de una instalación de alta tensión por el

concepto “Campo a nivel del suelo”, que corresponde al campo eléctrico o campo

magnético medido o calculado a 1 metro de altura sobre el suelo, en ausencia de otros

objetos.

# 5 Campo electromagnético de centros de transformación

Los centros de transformación involucran inversores, transformador y equipos anexos,

encontrándose todos sus conductores recubiertos con aislación eléctrica sólida, y

encapsulados, evitando la emisión de campo eléctrico. Adicionalmente, los centros de

transformación se instalan en recintos cerrados. Estas características permiten afirmar

que el campo eléctrico ambiental generado por los centros de transformación será

prácticamente nulo.

Como fuente magnética, el equipo principal de un centro de transformación es el

transformador. La densidad de flujo B está muy relacionada con la potencia aparente

nominal de un transformador. En base a una serie de experiencias y resultados

obtenidos en una amplia gama de potencias, en la referencia [5] se sugiere una

relación simple para el valor efectivo de la inducción magnética en la vecindad de un

transformador:

B rms (r) = k Tr P N /r [3] [micro Tesla]

P N : Potencia Nominal del transformador [kVA]

r: Distancia desde el centro del transformador [m]

k Tr : Coeficiente de Campo [ms/A], [Tm [3] /VA]

Un valor establecido de k Tr en la misma referencia es: 0,04 Tm [3] /kVA.

Esta expresión indica que la densidad de flujo magnético de transformadores decrece

rápidamente al alejarse del transformador (relación inversa con la tercera potencia de la

distancia). El Proyecto dispondrá de 3 unidades de transformadores las cuales

individualmente cuentan con una potencia de 3.150 kVA .

De acuerdo a la expresión anterior, con un transformador de 3.150 KVA, la densidad de

flujo magnético B a una distancia D desde el centro del transformador es la siguiente:

**Tabla 1 Variación de la inducción magnética con distancia al transformador**

|Distancia D[m]|2|4|6|8|10|
|---|---|---|---|---|---|
|~~Inducción magnética B [micro Tesla]~~<br>|15,75<br>|1,97<br>|0,58<br>|0,25|0,13|

Fuente: Elaboración propia

Se observa que a partir de 5m de cualquier transformador, la inducción magnética se

reduce a un valor inferior a 1,0 [micro Tesla]. Por lo tanto, el área de influencia para el

campo magnético de los transformadores del Parque abarca menos de 5m en torno al

transformador.

La referencia [5] también entrega un ábaco que se reproduce en la Figura siguiente, de

valores medidos en transformadores y switchgear de HV y MV.

**Figura 3 Reducción de la inducción magnética de equipos con la distancia**

Fuente: Referencia [5]

Por lo tanto, el campo magnético generado por cada Centro de Transformación,

incluyendo transformador y equipos anexos, decrece rápidamente siendo no relevante a

8 m de distancia, pues decae a menos de 1 [micro Tesla], no representando impacto

hacia el exterior del Parque.

# 6 Análisis del campo electromagnético de la línea

Para determinar la magnitud de estos campos, se utiliza un programa computacional

que aplica el método de elementos finitos [1] para modelar la configuración y resolver

la ecuación diferencial parcial que rige el comportamiento de los campos en un plano

transversal a la línea.

En la vecindad de una línea aérea energizada, el campo eléctrico se debe al voltaje

aplicado al conductor, el cual está expuesto al aire (no existe aislamiento sólido, el

aislamiento está definido por espaciamientos de aire). El campo magnético se debe a la

corriente que circula por los conductores. En este caso, los valores nominales son

13,2kV para el voltaje y 394 Amperes de corriente de fase.

**Figura 4 Silueta de poste de la línea**

Fuente: Titular del proyecto

A continuación se presentan los resultados para el campo eléctrico y el campo

magnético para la línea aérea; la línea transversal en la figura señala la superficie del

suelo; las líneas rojas en los gráficos indican el borde de la franja de seguridad,

estimada en 5m hacia cada lado y la flecha muestra la ubicación del poste.

**Figura 5 Malla de elementos finitos**

Fuente : Elaboración propia

**Figura 6 Distribución de equipotenciales eléctricas**

Fuente : Elaboración propia

**Figura 7 Campo eléctrico a 1m sobre el suelo bajo línea**

Fuente : Elaboración propia

**Figura 8 Distribución de equipotenciales magnéticas**

Fuente : Elaboración propia

**Figura 9 Inducción magnética a 1m sobre el suelo bajo línea**

Fuente : Elaboración propia

En la Tabla siguiente se presenta los máximos valores obtenidos a 1m de altura sobre el

suelo, bajo la línea, y la confrontación con los límites señalados por la ICNIRP [2] y el

PLIEGO TÉCNICO NORMATIVO RPTD N°07.

**Tabla 2 Valores de campo y confrontación con norma**

|Col1|Campo eléctrico<br>[V/m]|Inducción magnética<br>[micro Tesla]|
|---|---|---|
|~~Línea~~<br>|~~141~~<br>|~~1,21~~<br>|
|~~Límite RPTDN°07~~<br>|~~5.000~~<br>|~~100~~<br>|
|~~Límite ICNIRP~~<br>|~~5.000~~<br>|~~200~~<br>|
|~~CUMPLE~~|~~SI~~<br>|~~SI~~<br>|

Fuente: Elaboración propia

**7 CONCLUSIONES**

De la investigación bibliográfica y las simulaciones efectuadas para estimación de la

magnitud de los efectos electromagnéticos provocados por las diversas instalaciones del

proyecto Ampliación Parque Fotovoltaico El Monte Solar, se obtiene los resultados

presentados en la Tabla siguiente, conforme a los criterios de norma, indicando la

ubicación donde se presentan dichos valores; se incluye en la Tabla también los límites

establecidos por las respectivas normativas.

**Table 1 Valores de campo resultantes del estudio**

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- ubicación donde se presentan dichos valores; se incluye en la Tabla también los límites establecidos por las respectivas normativas. -->

**Tabla 1: Valores de campo resultantes del estudio****

| Col1 | Campo eléctrico<br>[V/m] | Inducción<br>magnética<br>[micro Tesla] | Ubicación valor |
| --- | --- | --- | --- |
| ~~Transformador~~<br>3.150KVA<br> | ~~- ~~<br> | ~~1,0~~<br> | ~~A 5m del equipo~~<br> |
| ~~Centro de~~<br>transformación<br> | ~~- ~~<br> | ~~1,0~~<br> | ~~A 8m del equipo~~<br> |
| ~~Línea de~~<br>transmisión aérea<br> | ~~147~~<br> | ~~0,25~~<br> | ~~Borde franja~~<br> |
| ~~Límite ICNIRP~~<br> | ~~5.000~~<br> | ~~200~~<br> | <br> |
| ~~Límite RPTDN°07~~ | ~~5.000~~<br> | ~~100~~<br> |  |

<!-- Estadísticas: 5 filas, 4 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia Con respecto al eventual “riesgo para la salud de la población debido a la generación de -->
<!-- FIN TABLA 1 -->


|Col1|Campo eléctrico<br>[V/m]|Inducción<br>magnética<br>[micro Tesla]|Ubicación valor|
|---|---|---|---|
|~~Transformador~~<br>3.150KVA<br>|~~- ~~<br>|~~1,0~~<br>|~~A 5m del equipo~~<br>|
|~~Centro de~~<br>transformación<br>|~~- ~~<br>|~~1,0~~<br>|~~A 8m del equipo~~<br>|
|~~Línea de~~<br>transmisión aérea<br>|~~147~~<br>|~~0,25~~<br>|~~Borde franja~~<br>|
|~~Límite ICNIRP~~<br>|~~5.000~~<br>|~~200~~<br>|<br>|
|~~Límite RPTDN°07~~|~~5.000~~<br>|~~100~~<br>||

Fuente: Elaboración propia

Con respecto al eventual “riesgo para la salud de la población debido a la generación de

campos electromagnéticos durante la fase de operación”, se tiene en primer lugar el

cumplimiento de la normativa, la cual se orienta precisamente a definir valores máximos

de campo eléctrico y magnético que evitan completamente el riesgo para las personas.

El principal organismo mundial que vela por la salud de la población humana, la

Organización Mundial de la Salud (OMS o WHO en la sigla en inglés), reconoce a la

ICNIRP como el organismo experto de consulta en temas de radiaciones no ionizantes.

También la ICNIRP ha sido reconocida por la Organización Internacional del Trabajo

(International Labour Organization - ILO) y la Unión Europea.

En 2010 la ICNIRP produjo el documento titulado "Guidelines for Limiting Exposure to

Time-Varying Electric, Magnetic, and Electromagnetic Fields (1 Hz - 100 kHz)", el que

se ha convertido en el documento base para múltiples legislaciones que presentan

máximos valores de exposición permanente a campos electromagnéticos. Para campos

de 50Hz, que corresponde a la frecuencia de potencia, recogiendo investigaciones en

este tema desde 1998 y en base a elaboración científica, este documento estableció los

valores 5.000[V/m] para el campo eléctrico y 200 [micro Tesla] para el campo

magnético, como valores máximos de exposición permanente para público general, que

no representan riesgo para el ser humano.

En el caso particular del Proyecto Ampliación Parque Fotovoltaico El Monte Solar, los

valores límites anteriores son muy superiores a las magnitudes de campo eléctrico y

magnético ambientales generados por las instalaciones del Proyecto, lo cual asegura

que no existe riesgo para la salud de la población.

**REFERENCIAS**

[1] Students' QuickField (TM) Finite Element Analysis System. Copyright (C) Tera

Analysis Company,. [www.quickfield.com](http://www.quickfield.com/)

[2] ICNIRP Guidelines for limiting exposure to time varying electric and magnetic

fields (1 Hz - 100 kHz)

Published in: Health Physics 99(6):818 - 836; 2010

International Commission on Non-Ionizing Radiation Protection

ICNIRP Publication - 2010

[3] PLIEGO TÉCNICO NORMATIVO RPTDN°07, dictado por Resolución Exenta No

33.277, de fecha 10/09/2020, Superintendencia de Electricidad y Combustibles

[4] Worst Case Evaluation of Magnetic Field in the vicinity of Electric Power

Substations Gerhard Bräunlich, Reinhold Bräunlich. ETH Zürich, Switzerland; FKH

Fachkommission für Hochspannungsfragen. Proceedings, 20th Int. Zurich

Symposium on EMC, Zurich 2009

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2: Valores de campo y confrontación con norma****

| Col1 | Campo eléctrico<br>[V/m] | Inducción magnética<br>[micro Tesla] |
| --- | --- | --- |
| ~~Línea~~<br> | ~~141~~<br> | ~~1,21~~<br> |
| ~~Límite RPTDN°07~~<br> | ~~5.000~~<br> | ~~100~~<br> |
| ~~Límite ICNIRP~~<br> | ~~5.000~~<br> | ~~200~~<br> |
| ~~CUMPLE~~ | ~~SI~~<br> | ~~SI~~<br> |
