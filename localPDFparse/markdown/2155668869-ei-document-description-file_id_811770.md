---
title: Sin título
author: pc
date: D:20220418193110-04'00'
language: es
type: report
pages: 36
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME CAMPOS ELECTROMAGNÉTICOS LÍNEA ELÉCTRICA 1X220 KV RIHUE - PER
-->

# INFORME CAMPOS ELECTROMAGNÉTICOS LÍNEA ELÉCTRICA 1X220 KV RIHUE - PER

## Nelson Morales Osorio Abril 2022

**INDICE**

1. Propósito ..................................................................................................................................... 4

2. Metodología ................................................................................................................................ 4

3. Características del Proyecto ........................................................................................................ 4

4. Análisis del campo electromagnético de la línea ............................................................................ 6

5. Análisis de radio interferencia de la línea ....................................................................................... 7

6. Análisis de campos en cruce de líneas ............................................................................................ 8

6.1 Cruce con Línea 1x220 kV Santa Fé - Celulosa Pacífico ............................................................ 9

6.2 Cruce con Línea Eléctrica 1x66 kV Los Angeles - Angol .......................................................... 10

6.3 Cruce con Línea Eléctrica 1x220 kV Tolpán - San Gabriel ....................................................... 11

7. Análisis de campos en situación de paralelismo ........................................................................... 12

8. Límites de radio interferencia provocada por instalaciones de alta tensión. ............................... 14

9. Normas de exposición humana a campos electromagnéticos de 50 Hz ....................................... 14

10. Conclusiones................................................................................................................................ 15

11. Área de Influencia ................................................................................................................. 16

Referencias ........................................................................................................................................ 17

APÉNDICE 1 ESTRUCTURAS LÍNEA 1X220 KV ................................................................................... 18

APÉNDICE 2 CÁLCULO DEL CAMPO ELECTROMAGNÉTICO ............................................................... 24

A2.1 Línea soportada por estructura 22A1.1C+0 .......................................................................... 24

A2.2 Línea soportada por estructura 22A30.1C+3 ........................................................................ 26

A2.3 Línea soportada por estructura 22A70.1C-3 ......................................................................... 29

APÉNDICE 3 ....................................................................................................................................... 32

Estimación de niveles de perturbaciones por efecto corona ............................................................ 32

A3.1 Línea soportada por Estructura tipo 22A1.1C+0 ................................................................... 32

A3.2 Línea soportada por Estructura tipo 22A30.1C+0 ................................................................. 34

A3.3 Línea soportada por Estructura tipo 22A70.1C-3 ................................................................. 35

**FIGURAS**

Figura 1 Trazado línea 1x220 kV Rihue - PER ..................................................................................... 5

Figura 2 Cruces con líneas existentes .................................................................................................. 8

Figura 3 Malla de elementos finitos en cruce .................................................................................... 9

Figura 4 Campo eléctrico a 1m sobre el suelo en cruce con línea ..................................................... 9

Figura 5 Inducción magnética a 1m sobre el suelo en cruce con línea ............................................ 10

Figura 6 Malla de elementos finitos en cruce de líneas .................................................................... 10

Figura 7 Campo eléctrico a 1m sobre el suelo en cruce de líneas ................................................... 11

Figura 8 Inducción magnética a 1m sobre el suelo en cruce de líneas ............................................ 11

Figura 9 Malla de elementos finitos en paralelismo de líneas ......................................................... 12

Figura 10 Campo eléctrico a 1m sobre el suelo en paralelismo de líneas ....................................... 13

Figura 11 Inducción magnética a 1m sobre el suelo en paralelismo de líneas ................................ 13

Figura A1. 1 Estructura Suspensión 22A1.1C +0. .............................................................................. 18

Figura A1. 2 Estructura Suspensión 22A1.1C +3. .............................................................................. 19

Figura A1. 3 Estructura Suspensión 22A1.1C +8. .............................................................................. 20

Figura A1. 4 Estructura Anclaje 22A30.1C+0. .................................................................................... 21

Figura A1. 5 Estructura Anclaje 22A30.1C+3. .................................................................................... 22

Figura A1. 6 Estructura de Remate 22A70.1C -3. .............................................................................. 23

Figura A2. 1 Malla de elementos finitos............................................................................................ 24

Figura A2. 2 Diagrama de equipotenciales eléctricas ...................................................................... 24

Figura A2. 3 Campo eléctrico a 1m sobre el suelo ........................................................................... 25

Figura A2. 4 Diagrama de equipotenciales magnéticas ................................................................... 25

Figura A2. 5 Inducción magnética a 1m sobre el suelo .................................................................... 26

Figura A2. 6 Malla de elementos finitos ........................................................................................... 26

Figura A2. 7 Diagrama de equipotenciales eléctricas ....................................................................... 27

Figura A2. 8 Campo eléctrico a 1m sobre el suelo ........................................................................... 27

Figura A2. 9 Diagrama de equipotenciales magnéticas ................................................................... 28

Figura A2. 10 Inducción magnética a 1m sobre el suelo .................................................................. 28

Figura A2. 11 Malla de elementos finitos ......................................................................................... 29

Figura A2. 12 Diagrama de equipotenciales eléctricas .................................................................... 29

Figura A2. 13 Campo eléctrico a 1m sobre el suelo ......................................................................... 30

Figura A2. 14 Diagrama de equipotenciales magnéticas ................................................................. 30

Figura A2. 15 Inducción magnética a 1m sobre el suelo .................................................................. 31

**TABLAS**

Tabla 1 Características generales de la línea ...................................................................................... 5

Tabla 2 Características del cable de potencia ..................................................................................... 6

Tabla 3 Características del cable de guardia OPGW ........................................................................... 6

Tabla 4 Valores de campo en el borde de la franja ............................................................................. 7

Tabla 5. Magnitudes de radio interferencia ....................................................................................... 8

Tabla 6 Valores de campo en paralelismo de líneas ........................................................................ 13

Tabla 7 Límite de Interferencias de Radio ........................................................................................ 14

Tabla 8 Valores de campo resultantes y confrontación con normas ............................................... 15

Tabla 9 Valores de radio interferencia y confrontación con norma ................................................ 16

**1.** **Propósito**

El propósito de este estudio es estimar la magnitud de los campos electromagnéticos de baja y alta

frecuencia provocados por la operación de la línea de transmisión de 1x220 kV de la SE Rihue a la

SE Central Parque Renaico; confrontar los valores estimados con los respectivos valores tolerables

por el ser humano, indicados por organismos nacionales e internacionales, con el objeto de evaluar

el impacto ambiental de la componente campos electromagnéticos del Proyecto.

**2.** **Metodología**

Se revisa en primer lugar las características pertinentes del proyecto y luego se presenta los

resultados de una modelación de las estructuras de la línea, que definen la configuración de

conductores, mediante la aplicación del software QuickField [1] que utiliza el método de elementos

finitos y que permite obtener el campo eléctrico y el campo magnético de baja frecuencia generado

en el entorno de la línea. El campo eléctrico es fundamentalmente dependiente del voltaje de los

conductores y la fuente del campo magnético es la corriente por los conductores. Se incluye en el

estudio de campos la interacción de la línea con otras líneas existentes.

Similarmente, aplicando métodos aproximados de conocimiento general [5], se realiza una

estimación del nivel de campo perturbador a frecuencias de radio generado por la línea de

transmisión debido al fenómeno corona.

Finalmente se presenta las normas de referencia internacional respecto de magnitudes aceptables

de radio interferencia [2] y las normas aplicables en Chile para la exposición humana a campos

electromagnéticos de 50 Hz [3], [4], con el propósito de confrontar estos valores con las

estimaciones efectuadas y evaluar el efecto de las nuevas instalaciones desde el punto de vista

técnico de su emisión electromagnética de baja y alta frecuencia.

**3.** **Características del Proyecto**

La línea de evacuación tendrá una potencia proyectada de 100 MW, la longitud total del trazado es

de 19.691,17 metros y estará ubicada entre las comunas de Renaico, provincia de Malleco, Región

de la Araucanía y la comuna de Negrete, provincia de Bío Bío, Región del Bío Bío. El trazado de la

Línea Eléctrica 1x220 kV Rihue - PER será aéreo y comenzará en la estructura ML RH ubicada al

interior de la subestación Rihue y terminará en el ML PER al interior de la subestación Central Parque

Eólico Renaico. Esta Línea Eléctrica permitirá la conexión del Parque Eólico Rihue al Sistema Eléctrico

Nacional.

**Figura 1 Trazado línea 1x220 kV Rihue - PER**

El sistema eléctrico en el que operará el proyecto tiene las siguientes características principales:

**Tabla 1 Características generales de la línea**

|Categoría (según RPTD N°2) :|Alta Tensión|
|---|---|
|Voltaje nominal :|220 kV|
|Potencia :|100 MW|
|Frecuencia nominal :|50 Hz|
|No circuitos de potencia :|1|
|Tipo de cable de potencia :|AAAC Flint|
|Disposición de conductores :|Triangular|
|Subconductores por fase :|1|
|No circuitos de guardia :|1|
|Tipo de cable de guardia :|OPGW|

El conductor de fase presenta las siguientes características:

**Tabla 2 Características del cable de potencia**

|Tipo|AAAC|
|---|---|
|Nombre|Flint|
|Sección|375,35 mm2|
|Diámetro|25,17 mm|
|Peso|1,028 kg/m|
|Tensión nominal de rotura|11.068 kgf|
|Coeficiente Dilatación lineal|23 x 10-6 1/°C|
|Módulo de Elasticidad|6.250 kgf/mm2|

A su vez, el cable de guardia tendrá las siguientes características:

**Tabla 3 Características del cable de guardia OPGW**

|Tipo|OPGW|
|---|---|
|Sección|120,70 mm2|
|Diámetro|15,20 mm|
|Peso|0,558 kg/m|
|Tensión nominal de ruptura|8.881 kgf|
|Coeficiente Dilatación lineal|16 x 10-6 1/°C|
|Módulo de Elasticidad|10.533 kgf/mm2|

Los conjuntos de aislación se formarán por la siguiente cantidad de aisladores para ambos tramos:

 14 aisladores para el conjunto de aislación de suspensión

 15 aisladores para el conjunto de aislación de anclaje

Las estructuras serán de acero reticulado del tipo autosoportadas y estructuras tubulares de simple

circuito con disposición triangular - vertical y canastillo para cable de guardia. Se utilizarán 67

estructuras de acero reticulado:

 37 estructuras de suspensión 22A1.1

 6 estructuras de anclaje 22A30.1

 - 16 estructura de remate 22A70.1

 8 estructura de anclaje-remate 22A90.1

En el Apéndice 1 se ilustra las siluetas de las estructuras.

**4. Análisis del campo electromagnético de la línea**

En la vecindad de una línea aérea de alta tensión, el campo eléctrico se debe a que el conductor de

alta tensión está directamente expuesto al aire (no existe aislamiento sólido, el aislamiento está

definido por espaciamientos de aire) y sobre dicho conductor está aplicado alto voltaje respecto de

tierra, que actúa como conductor de referencia a potencial cero. Sus unidades son Volt por metro

[V/m] o Kilovolt por metro kV/m] en alta tensión; en el caso en estudio, 220KV entre fases y 220/√3

KV fase a tierra.

El campo magnético se debe a la corriente que circula por los conductores y no depende del nivel

de voltaje de la línea, pero sí del consumo. Para este estudio se consideró una potencia máxima a

transmitir por la línea de 100 MVA por el simple circuito, lo que define 263 Amperes como corriente

máxima por fase. La magnitud representativa del campo magnético es la “inducción Magnética” o

“densidad de flujo Magnético” B **,** que tiene como unidad de medida práctica el mili Gauss (1 mG =
10 [-3] Gauss) o el micro Tesla (1μT = 10 [-6] Tesla) y se relacionan por: 1 μT = 10 mG.

Para investigar los efectos de los campos electromagnéticos, se acostumbra caracterizar al campo

eléctrico y el campo magnético cerca de una instalación de alta tensión por el concepto “Campo a

nivel del suelo”, que corresponde al campo eléctrico o magnético medido o calculado a 1 metro de

altura sobre el suelo, en ausencia de otros objetos.

Para el análisis se ha considerado las estructuras expuestas en el Apéndice 1, seleccionando la

opción más exigente para los campos, que corresponde a aquella alternativa de menor altura de

conductores; por ejemplo, entre las estructuras 22A1.1C, se optó por analizar la alternativa +0, en

vez de las alternativas +3 o +8. El análisis mediante elementos finitos para el concepto campo a nivel

del suelo, se incluye en el Apéndice 2. Los valores de campo obtenidos a 1m de altura sobre el suelo

en el borde de la franja de seguridad, para cada estructura, se resumen en la Tabla siguiente. El

ancho mínimo de la franja de seguridad se consideró en 20 m, 10m a cada lado del eje.

**Tabla 4** **Valores de campo en el borde de la franja**

|Línea soportada por estructura|Campo eléctrico<br>[V/m]|Inducción magnética<br>[micro Tesla]|
|---|---|---|
|22A1.1C+0|2.650|1,05|
|22A30.1C+0|3.030|1,21|
|22A70.1C-3|3.620|1,47|

**5. Análisis de radio interferencia de la línea**

La descarga corona en líneas de alta tensión corresponde a descargas eléctricas parciales en el aire

alrededor de los conductores, generadas por alto campo eléctrico, que provoca ionización del aire.

Este fenómeno emite campos electromagnéticos desde frecuencias de audio hasta alta frecuencia

en la banda de frecuencia de radio y televisión.

Mediante la aplicación del software LINEAS, de elaboración propia, se determina el campo eléctrico

en la superficie de los conductores y la radio interferencia emitida por la línea soportada por las

distintas estructuras. El programa ocupa el Método de Simulación de Cargas [5] para determinar el

campo eléctrico superficial y el procedimiento CIGRE para evaluar nivel de interferencia [5]. En el

Apéndice 3 se incorpora el listado de salida del programa, para cada una de las torres analizadas.

Los gráficos siguientes muestran la variación de la radio interferencia con la distancia desde el eje,

para cada tipo de estructura.

La Tabla siguiente resume las magnitudes de radio interferencia calculada para cada una de las

estructuras analizadas, a 0,5 MHz y a 15m de distancia lateral desde el conductor externo, según

norma canadiense [2].

**Tabla 5. Magnitudes de radio interferencia**

|Línea en Estructura|RI [dB/uV/m]|
|---|---|
|22A1.1C+0|42,39|
|22A30.1C+0|41,91|
|22A70.1C-3|42,93|

Fuente: Elaboración propia

**6. Análisis de campos en cruce de líneas**

La línea del Proyecto presenta tres cruces con líneas existentes:

 Con Línea 1x220 kV Santa Fé - Celulosa Pacífico, entre estructuras 12-13 (línea verde en la

Figura)

 Con Línea 1x66 kV Los Angeles - Angol, entre estructuras 31-32 (línea celeste en la Figura)

 Con Línea 1x220 kV Tolpán - San Gabriel, entre estructuras 38-39.

**Figura 2 Cruces con líneas existentes**

El análisis de campos se realiza con apoyo del software QuickField para modelar conductores y
estructuras. A continuación, se presenta en cada caso la malla de elementos finitos y los respectivos
gráficos de campo. La línea transversal en la Figura representa el plano de tierra; en los gráficos se
indica con una flecha a ubicación del cruce y con líneas rojas los bordes de la franja de seguridad de

la línea.

**6.1 Cruce con Línea 1x220 kV Santa Fé - Celulosa Pacífico**

**Figura 3 Malla de elementos finitos en cruce**

**Figura 4 Campo eléctrico a 1m sobre el suelo en cruce con línea**

No se dispone de información respecto de la potencia nominal de la línea 1x220 kV Santa FéCelulosa Pacífico; se asumirá 100MVA, con una corriente por fase de 262 Amperes.

**Figura 5 Inducción magnética** **a 1m sobre el suelo en cruce con línea**

**6.2 Cruce con Línea Eléctrica 1x66 kV Los Angeles - Angol**

**Figura 6 Malla de elementos finitos en cruce de líneas**

**Figura 7 Campo eléctrico a 1m sobre el suelo en cruce de líneas**

La potencia nominal declarada de la línea 1x66 kV Los Angeles - Angol es 73MVA, con una

corriente nominal de 638 Amperes.

**Figura 8 Inducción magnética a 1m sobre el suelo en cruce de líneas**

**6.3 Cruce con Línea Eléctrica 1x220 kV Tolpán - San Gabriel**

No se dispone de mayor información de esta línea por lo que se considerará una situación similar

al cruce con la línea 1x220 kV Santa Fé - Celulosa Pacífico.

En la Tabla siguiente se resume las magnitudes de campo encontradas en el borde de la franja

mínima de seguridad de la línea del Proyecto, en los cruces de línea.

**Tabla 6 Valores de campo en cruce de líneas**

|Cruce con línea|Campo eléctrico<br>[V/m]|Inducción magnética<br>[micro Tesla]|
|---|---|---|
|Línea 1x220 kV Santa Fé - Celulosa Pacífico|3.240|1,51|
|Línea Eléctrica 1x66 kV Los Angeles - Angol|2.660|3,20|
|Línea Eléctrica 1x220 kV Tolpán - San Gabriel|3.240|1,51|

En los cruces con las líneas de 1x220kV las magnitudes se mantienen similares a las de la línea

individual; en el cruce con la línea de 1x66kV, esta línea amortigua el campo eléctrico, pero refuerza

el campo magnético, duplicando su valor en relación al caso individual.

**7. Análisis de campos en situación de paralelismo**

La Línea Eléctrica 1x220 kV Rihue - PER presenta 3 paralelismos con líneas existentes:

 - Paralelismo con Línea 1x220 kV Santa Fé - Pacífico

 Paralelismo con Línea 1x220 kV Tolpán - San Gabriel

 Paralelismo con Línea 1x220 kV Tap Bureo - Parque Eólico Renaico

Puesto que no existe información disponible en todos los casos, se resolverá el paralelismo con
Línea 1x220 kV Santa Fé - Pacífico, y los otros casos se asumirán equivalentes, dado que todos
corresponden a líneas de 1x220kV.

.

**Figura 9 Malla de elementos finitos en paralelismo de líneas**

**Figura 10 Campo eléctrico a 1m sobre el suelo en paralelismo de líneas**

**Figura 11 Inducción magnética a 1m sobre el suelo en paralelismo de líneas**

La tabla siguiente presenta los valores de campo en el borde de franja de la línea del Proyecto.

**Tabla 7** **Valores de campo en paralelismo de líneas**

|Campo eléctrico<br>[V/m]|Inducción magnética<br>[micro Tesla]|
|---|---|
|2.750|1,53|

Se observa que, debido a la proximidad de las líneas, no se alcanza a anular completamente los

campos en el sector entre líneas, pero no se modifica significativamente los valores de campo en el

borde de la franja del Proyecto.

**8. Límites de radio interferencia provocada por instalaciones de alta tensión.**

Canadian Standards Association [2] entrega la siguiente recomendación para el límite de campo

electromagnético perturbador de alta frecuencia (radio interferencia) emitida por líneas de

transmisión y subestaciones, según su nivel de tensión:

**Tabla 8** **Límite de Interferencias de Radio**

|Voltaje nominal entre fases|Nivel de Radio Interferencia|
|---|---|
|**(KV)**|**(dB/ 1μV/m)**|
|Menos de 70|43|
|70 - 200|49|
|200 - 300|53|
|400 - 600|60|
|Sobre 600|63|

Fuente: (Canadian Standards Association, 1984)

Para líneas de transmisión, los valores indicados son a 15 m de la fase externa y a 0,5 MHz. Para

subestaciones, los valores son medidos a 15 m del cerco del recinto de la subestación. Para una línea

de transmisión o subestación de 220 kV, el valor límite corresponde a 53 [dB/ 1uV/m].

**9. Normas de exposición humana a campos electromagnéticos de 50 Hz**

En nuestro país no existe reglamentación específica relativa a los valores límites permitidos de

exposición de las personas a los campos electromagnéticos de frecuencia industrial. No obstante, la

regulación ambiental que rige el tema de emisiones señala que, de no existir una regulación

nacional, debe aplicarse como norma de referencia aquella que se encuentre vigente en estados

específicos. El Decreto Supremo No 40 del Ministerio del Medio Ambiente, promulgado con fecha

30/10/2012, indica en su Artículo 11:

_“Artículo 11... Para los efectos de evaluar el riesgo indicado en la letra a) y los efectos adversos_

_señalados en la letra b), se considerará lo establecido en las normas de calidad ambiental y de_

_emisión vigentes. A falta de tales normas, se utilizarán como referencia las vigentes en los Estados_

_que señale el reglamento._

La recomendación de uso más frecuente para público general y exposición permanente, es la

publicada por la ICNIRP [3], organismo no gubernamental reconocido por la Organización Mundial

de la Salud como referente en el tema, que establece 5.000 [V/m] para el campo eléctrico y 200

[micro Tesla] para la inducción magnética, valores que han sido acogidos por la normativa de

diversos países incluidos en la nómina anterior.

En el año 2021 se publicó en nuestro país el Pliego Técnico Normativo RPTD N°07, [4] dictado por

Resolución Exenta No 33.277, de fecha 10/09/2020, de la Superintendencia de Electricidad y

Combustibles, que en su Artículo 4.7 establece:

_“Los límites máximos permisibles para la seguridad de las personas, en cuanto a la emisión de campo_

_electromagnético para el diseño de líneas aéreas de corriente alterna de 50 Hz de frecuencia, y que_

_será evaluado en el exterior de la franja de seguridad, a 1 metro sobre el nivel del suelo, en_

_condiciones normales de operación de la línea, con los conductores en reposo, serán los que_

_determinen las normas respectivas. En ausencia de regulación técnica nacional, se debe cumplir con_

_lo siguiente:_

_5 [kV/m] para campo eléctrico (valor RMS)_

_100_ _[μT] para campo magnético (valor RMS).”_

**10. Conclusiones**

Mediante modelaciones de la línea y sus estructuras, con apoyo de un software que aplica el método

de elementos finitos, se ha obtenido las magnitudes de campo eléctrico y campo magnético

generadas durante su operación por la línea 1x220 kV de la SE Rihue a la SE Central Parque Renaico.

Se analizó igualmente las situaciones de cruce y paralelismo de la línea con otras líneas existentes.

La tabla siguiente resume los valores resultantes, incorporando los valores límites establecidos por

las respectivas normativas y de acuerdo a las condiciones de norma.

**Tabla 9 Valores de campo resultantes y confrontación con normas**

|Línea en Estructura|Campo eléctrico<br>[V/m]|Inducción magnética<br>[micro Tesla]|
|---|---|---|
|22A1.1C+0|2.650|1,05|
|22A30.1C+0|3.030|1,21|
|22A70.1C-3|3.620|1,47|
|**Cruce de líneas**|||
|Línea 1x220 kV Santa Fé - Celulosa Pacífico|3.240|1,51|
|Línea Eléctrica 1x66 kV Los Angeles - Angol|2.660|3,20|
|Línea Eléctrica 1x220 kV Tolpán - San Gabriel|3.240|1,51|
|**Paralelismo de líneas**|||
|Línea 1x220 kV Santa Fé - Pacífico|2.750|1,53|
|Línea 1x220 kV Tolpán - San Gabriel|2.750|1,53|
|Línea 1x220 kV Tap Bureo - Parque Eólico<br>Renaico|2.750|1,53|

|Línea en Estructura|Campo eléctrico<br>[V/m]|Inducción magnética<br>[micro Tesla]|
|---|---|---|
|**Límite ICNIRP**|5.000|200|
|**Límite RPTDN°07**|5.000|100|

Fuente: Elaboración propia

Aplicando métodos aproximados de aplicación habitual, se realizó una estimación del nivel de

campo perturbador, o radio interferencia, generado por la línea de transmisión debido al fenómeno

corona. Los resultados para las distintas estructuras de soporte se presentan en la Tabla siguiente,

confrontados con el respectivo límite de norma.

**Tabla 10 Valores de radio interferencia y confrontación con norma**

|Línea en Estructura|RI [dB/uV/m]|
|---|---|
|22A1.1C+0|42,39|
|22A30.1C+0|41,91|
|22A70.1C-3|42,93|
|**Límite norma canadiense**|**53**|

Fuente: Elaboración propia

De los resultados obtenidos en las modelaciones efectuadas, presentados en las Tablas anteriores,

se concluye que durante su operación, la línea 1x220 kV de la SE Rihue a la SE Central Parque

Renaico, satisface la normativa referente a campo electromagnético de baja frecuencia y alta

frecuencia.

**11.** **Área de Influencia**

En base a los efectos ambientales evaluados en este Informe, se determina que el área de influencia

de la línea de transmisión del proyecto, para la componente campos electromagnéticos,

corresponde a una franja de ancho total 20m, 10 m a cada lado del eje, a lo largo de la extensión de

la línea; este valor se asume por concordancia con la franja de seguridad mínima de la línea.

**Referencias**

[1] Students' QuickField (TM) Finite Element Analysis System

Version 5.8 User’s Guide

Copyright (C) Tera Analysis Company, 2010.

[2] Association canadienne de normalisation, Valeurs limites et methods de mesure du

bruit électromagnétique (0,15 à 30 MHz) produit par les reseaux de courant alternatif.

CAN3-C108.3.1 - M84. Octobre 1984.Reaffirmed 2009

[3] International Commission on Non‐Ionizing Radiation Protection

ICNIRP Publication - 2010

ICNIRP Guidelines for limiting exposure to time‐varying electric and magnetic fields (1 hz100 kHz) Published in: Health Physics 99(6):818‐836; 2010

[4] PLIEGO TÉCNICO NORMATIVO RPTDN°07, [4] dictado por Resolución Exenta No 33.277, de

fecha 10/09/2020, de la Superintendencia de Electricidad y Combustibles

[5] N. Morales, "Fenómeno corona en líneas de transmisión y sus efectos".

Publicación T(P)/9, Departamento de Ingeniería Eléctrica. Noviembre 1986.

**APÉNDICE 1 ESTRUCTURAS LÍNEA 1X220 KV**

Las Figuras siguientes ilustran las siluetas de las diferentes estructuras de la línea 1x220 kV de la SE

Rihue a la SE Central Parque Renaico, con sus dimensiones en mm.

**Figura A1. 1** **Estructura Suspensión 22A1.1C +0.**

**Figura A1. 2** **Estructura Suspensión 22A1.1C +3.**

**Figura A1. 3** **Estructura Suspensión 22A1.1C +8.**

**Figura A1. 4** **Estructura Anclaje 22A30.1C+0.**

**Figura A1. 5** **Estructura Anclaje 22A30.1C+3.**

**Figura A1. 6** **Estructura de Remate 22A70.1C -3.**

**APÉNDICE 2 CÁLCULO DEL CAMPO ELECTROMAGNÉTICO**

Se incluye en este Apéndice los resultados de la aplicación del software utilitario QuickField para la

obtención gráfica de los campos generados por la línea, soportada por las distintas estructuras.

En las Figuras, la línea transversal señala la superficie del suelo. En los gráficos de campo se indica

con una flecha la posición de la línea; las líneas rojas señalan los bordes de la franja de servidumbre.

**A2.1 Línea soportada por estructura 22A1.1C+0**

**Figura A2. 1 Malla de elementos finitos**

**Figura A2. 2 Diagrama de equipotenciales eléctricas**

**Figura A2. 3 Campo eléctrico a 1m sobre el suelo**

**Figura A2. 4 Diagrama de equipotenciales magnéticas**

**Figura A2. 5 Inducción magnética a 1m sobre el suelo**

**A2.2 Línea soportada por estructura 22A30.1C+3**

**Figura A2. 6 Malla de elementos finitos**

**Figura A2. 7 Diagrama de equipotenciales eléctricas**

**Figura A2. 8 Campo eléctrico a 1m sobre el suelo**

**Figura A2. 9 Diagrama de equipotenciales magnéticas**

**Figura A2. 10 Inducción magnética a 1m sobre el suelo**

**A2.3 Línea soportada por estructura 22A70.1C-3**

**Figura A2. 11 Malla de elementos finitos**

**Figura A2. 12 Diagrama de equipotenciales eléctricas**

**Figura A2. 13 Campo eléctrico a 1m sobre el suelo**

**Figura A2. 14 Diagrama de equipotenciales magnéticas**

**Figura A2. 15 Inducción magnética a 1m sobre el suelo**

**APÉNDICE 3**

**Estimación de niveles de perturbaciones por efecto corona**

El valor de radio interferencia máximo provocado por una línea está normalizado, para

medida o estimación, a una frecuencia de 0,5 MHz; a una distancia lateral de 15 metros de la fase

externa y una altura de 2 metros sobre el suelo; existen factores de corrección para evaluar la

perturbación a otras distancias y otras frecuencias [3].

A continuación se incluye el listado de salida del software LINEAS, de elaboración propia,

que permite determinar gradiente en la superficie de conductores de líneas de Alta Tensión y radio

interferencia, aplicado a las configuraciones estudiadas anteriormente, y según las condiciones de

norma.

Nota: El programa utiliza punto decimal (.) en vez de coma (,). No utiliza tildes.

**A3.1 Línea soportada por Estructura tipo 22A1.1C+0**

_CAMPO ELECTRICO Y POTENCIAL INDUCIDO EN TORNO A LINEAS DE TRANSMISION_

_Numero total de conductores : 4_

_Numero de conductores activos : 3_

_Numero de cables de guardia : 1_

|Fase|1|2|3|C.de G.|
|---|---|---|---|---|
|_ Numero de subconductores_|_1 _|_1 _|_1 _|_1 _|
|_ Radio del subconductor (cm)_|_1.258_|_1.258_|_1.258_|_0.760_|
|_Ubicacion lateral del conductor (m)_|_-4.200_|_4.200_|_3.700_|_0.000_|
|_ Altura conductor sobre el suelo (m)_|_16.000_|_16.000_|_21.000_|_23.200_|

_Matriz de coeficientes (amplif. por (2 πε_ _0_ _))_

_7.8414 1.3708 1.3979 1.2671_

_1.3708 7.8414 1.9966 1.2671_

_1.3979 1.9966 8.1133 1.8628_

_1.2671 1.2671 1.8628 8.8906_

_Matriz de capacitancias (amplif. por 1/(2 πε_ _0_ _))_

_.1356 -.0175 -.0160 -.0135_

_-.0175 .1397 -.0288 -.0114_

_-.0160 -.0288 .1383 -.0226_

_-.0135 -.0114 -.0226 .1208_

_Potenciales de conductores ( KVolts)_

_( 127.0170, 0.0000 ) 127.0170_
_( -63.5085, -110.0000 ) 127.0170_
_( -63.5085, 110.0000 ) 127.0170_
_( 0.0000, 0.0000 ) 0.0000_

_Cargas en conductores (Cb)/( 2 πε_ _0_ _)_

_( 19.3477, 0.1639 ) 19.3484_
_( -9.2661, -18.5362 ) 20.7233_
_( -8.9832, 18.3740 ) 20.4524_
_( 0.4454, -1.2314 ) 1.3095_

_Gradientes superficiales (kVef./cm)_

_( 15.3797, 0.1303 ) 15.3803_
_( -7.3658, -14.7347 ) 16.4732_
_( -7.1409, 14.6057 ) 16.2579_
_( 0.5860, -1.6203 ) 1.7230_

_Radio interferencia [dB/uV/m]_

|RI1|RI2|RI3|Col4|RI|
|---|---|---|---|---|
|_34,48_|_42,39_|_39,08_||_42,39_|

**A3.2 Línea soportada por Estructura tipo 22A30.1C+0**

_CAMPO ELECTRICO Y POTENCIAL INDUCIDO EN TORNO A LINEAS DE TRANSMISION_

_Numero total de conductores : 4_

_Numero de conductores activos : 3_

_Numero de cables de guardia : 1_

|Fase|1|2|3|C.de G.|
|---|---|---|---|---|
|_ Numero de subconductores_|_1 _|_1 _|_1 _|_1 _|
|_ Radio del subconductor (cm)_|_1.258_|_1.258_|_1.258_|_0.760_|
|_Ubicacion lateral del conductor (m)_|_-4.710_|_4.710_|_4.210_|_0.000_|
|_ Altura conductor sobre el suelo (m)_|_16.000_|_16.000_|_21.000_|_23.200_|

_Matriz de coeficientes (amplif. por (2 πε_ _0_ _))_

_7.8414 1.2645 1.3143 1.5236_

_1.2645 7.8414 1.9966 1.5236_

_1.3143 1.9966 8.1133 2.2351_

_1.5236 1.5236 2.2351 8.7169_

_Matriz de capacitancias (amplif. por 1/(2 πε_ _0_ _))_

_.1356 -.0150 -.0134 -.0176_

_-.0150 .1399 -.0280 -.0147_

_-.0134 -.0280 .1402 -.0287_

_-.0176 -.0147 -.0287 .1277_

_Potenciales de conductores ( KVolts)_

_( 127.0170, 0.0000 ) 127.0170_
_( -63.5085, -110.0000 ) 127.0170_
_( -63.5085, 110.0000 ) 127.0170_
_( 0.0000, 0.0000 ) 0.0000_

_Cargas en conductores (Cb)/( 2 πε_ _0_ _)_

_( 19.0332, 0.1777 ) 19.0340_
_( -9.0192, -18.4667 ) 20.5515_
_( -8.8330, 18.4997 ) 20.5003_
_( 0.5145, -1.5466 ) 1.6300_

_Gradientes superficiales (kVef./cm)_

_( 15.1297, 0.1413 ) 15.1304_
_( -7.1695, -14.6794 ) 16.3367_
_( -7.0215, 14.7056 ) 16.2959_
_( 0.6769, -2.0351 ) 2.1447_

_Radio interferencia [dB/uV/m]_

|RI1|RI2|RI3|Col4|RI|
|---|---|---|---|---|
|_33,16_|_41,91_|_39,21_||_41,91_|

**A3.3 Línea soportada por Estructura tipo 22A70.1C-3**

_CAMPO ELECTRICO Y POTENCIAL INDUCIDO EN TORNO A LINEAS DE TRANSMISION_

_Numero total de conductores : 4_

_Numero de conductores activos : 3_

_Numero de cables de guardia : 1_

|Fase|1|2|3|C.de G.|
|---|---|---|---|---|
|_ Numero de subconductores_|_1 _|_1 _|_1 _|_1 _|
|_ Radio del subconductor (cm)_|_1.258_|_1.258_|_1.258_|_0.760_|
|_Ubicacion lateral del conductor (m)_|_-4.060_|_4.060_|_3.560_|_0.000_|
|_ Altura conductor sobre el suelo (m)_|_15.000_|_15.000_|_20.000_|_23.560_|

_Matriz de coeficientes (amplif. por (2 πε_ _0_ _))_

_7.7768 1.3422 1.3687 1.4092_

_1.3422 7.7768 1.9410 1.4092_

_1.3687 1.9410 8.0645 2.1611_

_1.4092 1.4092 2.1611 8.7323_

_Matriz de capacitancias (amplif. por 1/(2 πε_ _0_ _))_

_.1370 -.0171 -.0149 -.0157_

_-.0171 .1408 -.0275 -.0132_

_-.0149 -.0275 .1406 -.0280_

_-.0157 -.0132 -.0280 .1261_

_Potenciales de conductores ( KVolts)_

_( 127.0170, 0.0000 ) 127.0170_
_( -63.5085, -110.0000 ) 127.0170_

_( -63.5085, 110.0000 ) 127.0170_
_( 0.0000, 0.0000 ) 0.0000_

_Cargas en conductores (Cb)/( 2 πε_ _0_ _)_

_( 19.4353, 0.2345 ) 19.4367_
_( -9.3659, -18.5051 ) 20.7403_
_( -9.0865, 18.4903 ) 20.6023_
_( 0.6238, -1.6277 ) 1.7432_

_Gradientes superficiales (kVef./cm)_

_( 15.4494, 0.1864 ) 15.4505_
_( -7.4450, -14.7100 ) 16.4867_
_( -7.2230, 14.6982 ) 16.3771_
_( 0.8208, -2.1417 ) 2.2936_

_Radio interferencia [dB/uV/m]_

|RI1|RI2|RI3|Col4|RI|
|---|---|---|---|---|
|_35,13_|_42,91_|_39,95_||_42,93_|

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: Características generales de la línea****

| Categoría (según RPTD N°2) : | Alta Tensión |
| --- | --- |
| Voltaje nominal : | 220 kV |
| Potencia : | 100 MW |
| Frecuencia nominal : | 50 Hz |
| No circuitos de potencia : | 1 |
| Tipo de cable de potencia : | AAAC Flint |
| Disposición de conductores : | Triangular |
| Subconductores por fase : | 1 |
| No circuitos de guardia : | 1 |
| Tipo de cable de guardia : | OPGW |

**Tabla 2: Características del cable de potencia****

| Tipo | AAAC |
| --- | --- |
| Nombre | Flint |
| Sección | 375,35 mm2 |
| Diámetro | 25,17 mm |
| Peso | 1,028 kg/m |
| Tensión nominal de rotura | 11.068 kgf |
| Coeficiente Dilatación lineal | 23 x 10-6 1/°C |
| Módulo de Elasticidad | 6.250 kgf/mm2 |

**Tabla 3: Características del cable de guardia OPGW****

| Tipo | OPGW |
| --- | --- |
| Sección | 120,70 mm2 |
| Diámetro | 15,20 mm |
| Peso | 0,558 kg/m |
| Tensión nominal de ruptura | 8.881 kgf |
| Coeficiente Dilatación lineal | 16 x 10-6 1/°C |
| Módulo de Elasticidad | 10.533 kgf/mm2 |

**Tabla 4: ** **Valores de campo en el borde de la franja****

| Línea soportada por estructura | Campo eléctrico<br>[V/m] | Inducción magnética<br>[micro Tesla] |
| --- | --- | --- |
| 22A1.1C+0 | 2.650 | 1,05 |
| 22A30.1C+0 | 3.030 | 1,21 |
| 22A70.1C-3 | 3.620 | 1,47 |

**Tabla 5.: Magnitudes de radio interferencia****

| Línea en Estructura | RI [dB/uV/m] |
| --- | --- |
| 22A1.1C+0 | 42,39 |
| 22A30.1C+0 | 41,91 |
| 22A70.1C-3 | 42,93 |

**Tabla 6: Valores de campo en cruce de líneas****

| Cruce con línea | Campo eléctrico<br>[V/m] | Inducción magnética<br>[micro Tesla] |
| --- | --- | --- |
| Línea 1x220 kV Santa Fé - Celulosa Pacífico | 3.240 | 1,51 |
| Línea Eléctrica 1x66 kV Los Angeles - Angol | 2.660 | 3,20 |
| Línea Eléctrica 1x220 kV Tolpán - San Gabriel | 3.240 | 1,51 |

**Tabla 7: ** **Valores de campo en paralelismo de líneas****

| Campo eléctrico<br>[V/m] | Inducción magnética<br>[micro Tesla] |
| --- | --- |
| 2.750 | 1,53 |

**Tabla 8: ** **Límite de Interferencias de Radio****

| Voltaje nominal entre fases | Nivel de Radio Interferencia |
| --- | --- |
| **(KV)** | **(dB/ 1μV/m)** |
| Menos de 70 | 43 |
| 70 - 200 | 49 |
| 200 - 300 | 53 |
| 400 - 600 | 60 |
| Sobre 600 | 63 |

**Tabla 9: Valores de campo resultantes y confrontación con normas****

| Línea en Estructura | Campo eléctrico<br>[V/m] | Inducción magnética<br>[micro Tesla] |
| --- | --- | --- |
| 22A1.1C+0 | 2.650 | 1,05 |
| 22A30.1C+0 | 3.030 | 1,21 |
| 22A70.1C-3 | 3.620 | 1,47 |
| **Cruce de líneas** |  |  |
| Línea 1x220 kV Santa Fé - Celulosa Pacífico | 3.240 | 1,51 |
| Línea Eléctrica 1x66 kV Los Angeles - Angol | 2.660 | 3,20 |
| Línea Eléctrica 1x220 kV Tolpán - San Gabriel | 3.240 | 1,51 |
| **Paralelismo de líneas** |  |  |
| Línea 1x220 kV Santa Fé - Pacífico | 2.750 | 1,53 |
| Línea 1x220 kV Tolpán - San Gabriel | 2.750 | 1,53 |
| Línea 1x220 kV Tap Bureo - Parque Eólico<br>Renaico | 2.750 | 1,53 |

**Tabla 10: Valores de radio interferencia y confrontación con norma****

| Línea en Estructura | RI [dB/uV/m] |
| --- | --- |
| 22A1.1C+0 | 42,39 |
| 22A30.1C+0 | 41,91 |
| 22A70.1C-3 | 42,93 |
| **Límite norma canadiense** | **53** |
