---
title: Sin título
author: pc
date: D:20240214092031-03'00'
language: es
type: report
pages: 13
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME ESTUDIO DE CAMPOS ELECTROMAGNÉTICOS PARQUE SOLAR MAUTZ Nelson Morales Osorio Febrero 2024
  - CONTENIDO
-->

# INFORME ESTUDIO DE CAMPOS ELECTROMAGNÉTICOS PARQUE SOLAR MAUTZ Nelson Morales Osorio Febrero 2024

# CONTENIDO

1 OBJETIVOS ....................................................................................................................... 3

2 Descripción del proyecto................................................................................................. 3

2.1 Parque Fotovoltaico ................................................................................................. 3

2.2 Centros de conversión y transformación ................................................................. 4

2.3 Sistema BESS (Battery Energy Storage System) ....................................................... 5

2.4 Línea de transmisión ................................................................................................ 5

3 Campo electromagnético ................................................................................................... 6

4 Campo electromagnético de centros de transformación ............................................... 8

5 CAMPO ELECTROMAGNÉTICO DE sistema bess.............................................................. 9

6 Campo electromagnético generado por línea de transmisión ......................................... 10

7 Conclusiones .................................................................................................................... 12

REFERENCIAS ........................................................................................................................ 13

**FIGURAS**

Figura 1 Parque Solar Mautz y Punto de Conexión ................................................................ 4

Figura 2 Esquema de Centro de Transformación referencial ................................................. 5

Figura 3 Estructuras de soporte de línea de transmisión ....................................................... 6
Figura 4 Campo eléctrico cerca de un transformador de 15/0,4kV, 630KVA ....................... 8

Figura 5 Malla de elementos finitos ..................................................................................... 10

Figura 6 Campo eléctrico a 1m sobre el suelo ..................................................................... 11

Figura 7 Inducción magnética a 1m sobre el suelo .............................................................. 11

**TABLAS**

Tabla 1 Variación de la inducción magnética con distancia al transformador ...................... 9

Tabla 2 Valores de campo bajo la línea .............................................................................. 12

Tabla 3 Resumen de valores resultantes ............................................................................. 12

**1** **OBJETIVOS**

Este Informe presenta una estimación de los campos electromagnéticos de baja frecuencia

que pueden presentarse en el entorno de las instalaciones del Proyecto Parque Solar Mautz,

durante su operación, específicamente los equipos del parque solar y la línea de

transmisión.

Se presenta en primer lugar una descripción de las instalaciones del proyecto, pertinentes

al estudio. Luego se entrega información respecto del campo electromagnético generado

por centros de transformación y los resultados de una simulación para el campo eléctrico y

el campo magnético en el entorno de la línea de transmisión. Para determinar la magnitud

de estos campos, se utiliza un programa computacional que aplica el método de elementos

finitos [1] para modelar la configuración y resolver la ecuación diferencial parcial que rige

el comportamiento de los campos en la región a estudiar.

Los valores indicados se confrontan con las recomendaciones y límites admisibles [2], [3],

[4], para establecer finalmente una conclusión respecto al impacto ambiental de las

instalaciones del parque solar, desde el punto de vista técnico de la emisión

electromagnética de baja frecuencia.

**2** **DESCRIPCIÓN DEL PROYECTO**

El Proyecto Parque Solar Mautz se ubica en la comuna de La Unión, provincia del Ranco,

región de Los Ríos. El proyecto inyectará una potencia nominal de 9 MW de forma

constante, en horas solares por los paneles (9 MW) y no solares por baterías (9 MW).

**2.1** **Parque Fotovoltaico**

El parque solar estará conformado por 30.464 módulos solares en un área de 28,924 ha, los

cuales están agrupados en strings. El Parque incluye 6 centros de transformación

compuestos de inversores y transformadores para convertir la corriente continua en

corriente alterna y evacuar toda la energía generada por medio de una línea aérea de

transmisión en 13,2 kV, que se extenderá desde la caseta de transferencia (como circuito

simple) hasta el punto de conexión, que se encuentra en el mismo predio.

**Figura 1 Parque Solar Mautz y Punto de Conexión**

Fuente: Titular del Proyecto

Los paneles fotovoltaicos estarán elaborados para soportar temperaturas extremas y

corresponderán a paneles monocristalinos con una dimensión aproximada de 2384 x 1303

mm y generan como máximo una potencia de 670 [W] en corriente continua.

El transporte de corriente desde los centros de conversión y transformación hasta la Sala

de Telecomunicaciones se realizará por cables de media tensión subterráneos.

**2.2** **Centros de conversión y transformación**

Los centros de transformación consistirán en una solución compacta, realizado en acero

galvanizado de alta resistencia, en el que se encuentran integrados los inversores junto con

el transformador de potencia, las celdas de protección y todo el equipamiento de media

tensión que lo acompaña.

Los inversores son dispositivos eléctricos que convierte la corriente continua en corriente

alterna a una determinada frecuencia mediante un puente IGBT, el cual produce pulsos

secuenciales en la corriente continua, los cuales dan lugar a una onda de tipo sinusoidal,

siendo ésta la corriente alterna. Cuenta con un banco de condensadores el cual permite

corregir el factor de potencia, un sistema de monitorización que permite ver las diferentes

variables del sistema y un sistema de comunicación para monitorización a distancia.

El proyecto dispondrá de 6 centros de transformación de 3 MW, donde los transformadores

elevarán la tensión a un nivel de 13,2kV.

**Figura 2 Esquema de Centro de Transformación**

Fuente: Catálogo SUNGROW

**2.3** **Sistema BESS (Battery Energy Storage System)**

El proyecto contará con estructura de almacenamiento de baterías, o sistema BESS. Este

sistema de baterías entrega la capacidad de almacenar la energía generada en exceso en el

Parque Solar. Esta quedará almacenada y podrá entregarla al SEN en horarios nocturnos. Se

proyecta un sistema de baterías con capacidad de 72 MWh (9 MWac / 8 horas). Aunque la

capacidad instalada es lo suficiente para inyectar durante el día, el sistema BESS se presenta

como un servicio adicional.

**2.4** **Línea de transmisión**

La línea de transmisión se extenderá desde la caseta de transferencia (como circuito simple)

hasta el punto de conexión, que se encuentra en el mismo predio. Este poste corresponde

al No POC 502453 correspondiente al alimentador La Unión Creo en 13,2 kV, que llega a la

subestación La Unión, propiedad de la distribuidora SAESA.

Para la construcción de la Línea de Transmisión se considera una franja de intervención de

4 m sobre toda la extensión, esto equivale a 2 metros en cada lado del eje de la línea de

media tensión. Los postes de soporte de las cadenas de aisladores y de los 3 conductores

que forman el circuito simple de la Línea de Transmisión, se entierran a una profundidad de

2 metros, y tienen una altura de 11,5 metros y de ancho de 0,43 metros, aproximadamente.

**Figura 3 Estructuras de soporte de línea de transmisión**

Fuente: Titular del proyecto

**3 CAMPO ELECTROMAGNÉTICO**

La unidad del campo eléctrico es el Volt por metro [V/m] o Kilo Volt por metro [KV/m] en

media y alta tensión; es dependiente del voltaje de los conductores, en el caso en estudio,

13,2kV entre fases y 13,2/√3 KV fase a tierra.

El campo magnético se debe a la corriente que circula por los conductores. La magnitud

representativa del campo magnético es la “Inducción Magnética” o “Densidad de Flujo

Magnético” B **,** que tiene como unidad de medida práctica el mili Gauss (1 mG = 10 [-3] Gauss)

o el micro Tesla (1T = 10 [-6] Tesla ) y se relacionan por: 1 T = 10 mG.

Para investigar los efectos de los campos electromagnéticos, se acostumbra caracterizar al

campo eléctrico y el campo magnético cerca de una instalación de alta tensión por el

concepto “Campo a nivel del suelo”, que corresponde al campo eléctrico o magnético

medido o calculado a 1 metro de altura sobre el suelo, en ausencia de otros objetos.

En nuestro país no existe reglamentación específica relativa a los valores límites permitidos

de exposición de las personas a los campos electromagnéticos de frecuencia industrial. No

obstante, la regulación ambiental que rige el tema de emisiones señala que, de no existir

una regulación nacional, debe aplicarse como norma de referencia aquella que se

encuentre vigente en estados específicos.

La recomendación de uso más frecuente para público general y exposición permanente, es

la publicada por la ICNIRP [2], organismo no gubernamental reconocido por la Organización

Mundial de la Salud como referente en el tema, que establece 5.000 [V/m] para el campo

eléctrico y 200 [micro Tesla], para la inducción magnética, valores que han sido acogidos

por la normativa de diversos países incluidos en la nómina anterior.

El año 2021 se publicó el Pliego Técnico Normativo RPTD N°07 [3], dictado por Resolución

Exenta No 33.277, de fecha 10/09/2020, de la Superintendencia de Electricidad y

Combustibles, que en su Artículo 4.7 establece:

_“Los límites máximos permisibles para la seguridad de las personas, en cuanto a la emisión_

_de campo electromagnético para el diseño de líneas aéreas de corriente alterna de 50 Hz de_

_frecuencia, y que será evaluado en el exterior de la franja de seguridad, a 1 metro sobre el_

_nivel del suelo, en condiciones normales de operación de la línea, con los conductores en_

_reposo, serán los que determinen las normas respectivas. En ausencia de regulación técnica_

_nacional, se debe cumplir con lo siguiente:_

_5 kV/m para campo eléctrico (valor RMS)_

_100 micro Tesla para campo magnético (valor RMS).”_

Recientemente, en junio de 2023, el Servicio de Evaluación Ambiental (SEA) publicó el
documento “CRITERIO DE EVALUACIÓN EN EL SEIA: Evaluación de impactos por radiación

electromagnética en proyectos de transmisión eléctrica”,[4] en el cual se confirma los

valores límites de campo eléctrico y campo magnético establecidos por el reglamente

chileno RPTD N° 07 y los límites establecidos por la ICNIRP en su publicación de 1998.

Se procede a continuación a efectuar el análisis de campos generados por las instalaciones

del proyecto.

**4** **CAMPO ELECTROMAGNÉTICO DE CENTROS DE TRANSFORMACIÓN**

Los equipos de los Centros de Transformación incorporan conductores aislados y

adicionalmente se ubican dentro de un compartimiento metálico tipo conteiner, el cual

apantalla el campo eléctrico generado al interior, de modo que el campo eléctrico exterior

puede considerarse nulo. No obstante, el transformador es el equipo que genera campo

eléctrico y campo magnético hacia el exterior.

Para efectuar una estimación del campo eléctrico generado por el transformador, se

reproduce de la referencia [5], los resultados de medidas efectuadas a 1,7m de altura en la

vecindad de un transformador de 15/0,4kV, 630KVA.

**Figura 4 Campo eléctrico cerca de un transformador de 15/0,4kV, 630KVA**

Fuente: Referencia [4]

En el artículo se indica que el campo eléctrico máximo es aproximadamente 200[V/m] y se

midió cerca del switchgear de MT; a 5m del transformador, el campo eléctrico es inferior a

5[V/m]. A pesar de tratarse de un transformador de mucho menor potencia que los

transformadores del parque, con respecto al campo eléctrico la información es válida,

puesto que la fuente del campo eléctrico es el voltaje.

Respecto del campo magnético, la densidad de flujo B está muy relacionada con la potencia

aparente nominal de un transformador. En base a una serie de experiencias y resultados

obtenidos en una amplia gama de potencias, en la referencia [6] se sugiere una relación

simple para el valor efectivo de la inducción magnética en la vecindad de un transformador:

B rms (r) = k Tr P N /r [3] [micro Tesla]

P N : Potencia Nominal del transformador [kVA]

r: Distancia desde el centro del transformador [m]

k Tr : Coeficiente de Campo [ms/A], [Tm [3] /VA]

Un valor establecido de k Tr en la misma referencia es: 0,04 Tm [3] /kVA.

El Proyecto dispondrá de 6 unidades de transformadores las cuales individualmente

contarán con una potencia de 3.000kVA. De acuerdo a la expresión anterior, con un

transformador de 3.000KVA, la densidad de flujo magnético B a una distancia D desde el

centro del transformador es la siguiente:

**Tabla 1 Variación de la inducción magnética con distancia al transformador**

|Distancia D[m]|2|4|6|8|10|
|---|---|---|---|---|---|
|Inducción magnética B [micro Tesla]|15,00|1,875|0,556|0,234|0,12|

Fuente: Elaboración propia

Se observa que a partir de 5m de distancia desde el transformador, la inducción magnética

se reduce a un valor inferior a 1,0 [micro Tesla]. Por lo tanto, el área de influencia para el

campo magnético de los transformadores de la Planta abarca menos de 5m en torno al

transformador, con lo cual su impacto hacia el exterior de la Planta es despreciable.

**5** **CAMPO ELECTROMAGNÉTICO DE SISTEMA BESS**

Con respecto al campo electromagnético generado por los Sistemas de Almacenamiento

por Baterías (o sistemas BESS por las siglas en inglés), no es relevante el campo eléctrico

pues normalmente se limita a sistemas de media tensión con cables aislados; en el caso en

estudio, en 13,2 kV, instalados en recintos cerrados (containers), cuyas paredes metálicas

amortiguan aún más el campo eléctrico.

Tanto en el proceso de carga como en la etapa de entrega de energía, se produce un flujo

de corriente continua dirigido hacia los inversores, generando en torno a los conductores

que trasportan esta energía un campo magnético. Sin embargo, este campo magnético es

muy localizado, quedando contenido en el interior del parque. No existe en consecuencia

un impacto ambiental hacia el exterior. Donde se aglutina la energía es en los Centros de

Transformación, cuyo efecto se analizó anteriormente.

**6 CAMPO ELECTROMAGNÉTICO GENERADO POR LÍNEA DE TRANSMISIÓN**

A continuación, se desarrolla el estudio para determinar la magnitud de los efectos

electromagnéticos susceptibles de generarse por la operación de la línea de evacuación del

Parque. Para determinar la magnitud de estos campos, se utiliza un programa

computacional que aplica el método de elementos finitos [1] para modelar la configuración

y resolver la ecuación diferencial parcial que rige el comportamiento de los campos en un

plano transversal a la línea. El voltaje de la línea se consideró en 13,2 kV fase fase, 7,621kV

fase tierra y la corriente por fase en 393,65 Amperes, correspondiente a una potencia de 9

MW.

La línea transversal en la figura señala la superficie del suelo; la flecha muestra la ubicación

del poste; en los gráficos, las líneas rojas señalan los bordes de la franja.

**Figura 5 Malla de elementos finitos**

Fuente: Elaboración propia

**Figura 6 Campo eléctrico a 1m sobre el suelo**

Fuente: Elaboración propia

**Figura 7 Inducción magnética a 1m sobre el suelo**

Fuente: Elaboración propia

En la Tabla siguiente se presenta los valores obtenidos a 1m de altura sobre el suelo, bajo

la línea.

**Tabla 2 Valores de campo bajo la línea**

|Campo eléctrico<br>[V/m]|Col2|Inducción magnética [micro<br>Tesla]|Col4|
|---|---|---|---|
|Máximo|Borde franja|Máximo|Borde franja|
|138,3|122|0,794|0,772|

Fuente: Elaboración propia

**7 CONCLUSIONES**

De los resultados obtenidos en las modelaciones efectuadas y en la investigación

bibliográfica, se obtiene los siguientes valores en las ubicaciones que se indica, contrastados

con los valores máximos señalados por la normativa vigente:

**Tabla 3 Resumen de valores resultantes**

|Equipo|Campo eléctrico<br>[V/m]|Inducción<br>magnética<br>[micro Tesla]|Ubicación|
|---|---|---|---|
|Centro de<br>Transformación|5,0|<1,0|A 5m del equipo|
|Línea 12kV aérea<br>|138,3<br>122|0,794<br>0,772|Bajo línea<br>Borde franja|
|Límite RPTD N°07|5.000|100||
|Límite ICNIRP|5.000|200||
|Criterio SEA|5.000|100||

Fuente: Elaboración propia

De los resultados presentados en la Tabla anterior, se concluye que las instalaciones del

Parque Solar Mautz satisfacen la normativa vigente respecto de campos electromagnéticos

y conforme al Criterio SEA, los valores de campo electromagnético generados por sus

instalaciones, son seguros para las personas.

**REFERENCIAS**

[1] Students' QuickField (TM) Finite Element Analysis System. Copyright (C) Tera

[Analysis Company, www.quickfield.com](http://www.quickfield.com/)

[2] ICNIRP Guidelines for limiting exposure to time varying electric and magnetic fields

(1 Hz - 100 kHz)

Published in: Health Physics 99(6):818 - 836; 2010

International Commission on Non-Ionizing Radiation Protection

ICNIRP Publication - 2010

[3] PLIEGO TÉCNICO NORMATIVO RPTDN°07, dictado por Resolución Exenta

No 33.277, de fecha 10/09/2020,

Superintendencia de Electricidad y Combustibles

[4] CRITERIO DE EVALUACIÓN EN EL SEA: Evaluación de impactos por radiación

electromagnética en proyectos de transmisión eléctrica

Servicio de Evaluación Ambiental, Primera Edición, Santiago, junio 2023

[5] Low Frecuency Electromagnetics Fields in Power Transformer Rooms

Tony Richard O. Almeida, A. Paulo Coimbra, Carlos F. R. Lemos Antunes

Laboratorio de CAD/CAE, I.S.R.

Departamento de Engenharia Electrotécnica, Universidade de Coimbra, Portugal

[6] Gerhard Bräunlich, Reinhold Bräunlich

Worst Case Evaluation of Magnetic Field in the vicinity of Electric Power

Substations.

ETH Zürich, Switzerland; FKH Fachkommission für Hochspannungsfragen.

Proceedings, 20th Int.

Zurich Symposium on EMC, Zurich 2009

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: Variación de la inducción magnética con distancia al transformador****

| Distancia D[m] | 2 | 4 | 6 | 8 | 10 |
| --- | --- | --- | --- | --- | --- |
| Inducción magnética B [micro Tesla] | 15,00 | 1,875 | 0,556 | 0,234 | 0,12 |

**Tabla 2: Valores de campo bajo la línea****

| Campo eléctrico<br>[V/m] | Col2 | Inducción magnética [micro<br>Tesla] | Col4 |
| --- | --- | --- | --- |
| Máximo | Borde franja | Máximo | Borde franja |
| 138,3 | 122 | 0,794 | 0,772 |

**Tabla 3: Resumen de valores resultantes****

| Equipo | Campo eléctrico<br>[V/m] | Inducción<br>magnética<br>[micro Tesla] | Ubicación |
| --- | --- | --- | --- |
| Centro de<br>Transformación | 5,0 | <1,0 | A 5m del equipo |
| Línea 12kV aérea<br> | 138,3<br>122 | 0,794<br>0,772 | Bajo línea<br>Borde franja |
| Límite RPTD N°07 | 5.000 | 100 |  |
| Límite ICNIRP | 5.000 | 200 |  |
| Criterio SEA | 5.000 | 100 |  |
