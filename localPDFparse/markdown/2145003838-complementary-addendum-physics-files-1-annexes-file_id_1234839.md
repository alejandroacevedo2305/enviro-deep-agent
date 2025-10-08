---
title: Microsoft Word - 5228-0000-RH-INF-002_0 Simulaciones DMH DIA.docx
author: roherrer
date: D:20200817121352-04'00'
language: es
type: report
pages: 29
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - CONTACTOS
  - CONTENIDO
-->

## ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**CÓDIGO ARCADIS: N° 5228-0000-RH-INF-002_0**

## SIMULACIONES PARA EVALUAR EFECTOS DEL DRENAJE FUTURO DEL RAJO DE DMH A DIC 2028, INFORME PARA DIA AUMENTO MOVIMIENTO MINA

A GOSTO 2020

# CONTACTOS

**EDGARDO DZOGOLYK**

**Administrador de Contratos**

T +562 2 3816343

e edgardo.dzogolyk@arcadis.com

V

Copyright © 2015 Arcadis. All rights reserved. arcadis.com

Arcadis.

Av. Antonio Varas 621

Providencia, CP 7500966
Santiago | Chile

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

# CONTENIDO

**1** **INTRODUCCIÓN ............................................................................................................... 1**
**1.1** **Aspectos generales ........................................................................................................................ 1**
**1.2** **Objetivos y alcances ...................................................................................................................... 1**

**2** **REFERENCIAS ................................................................................................................. 1**

**3** **RESUMEN DE UNIDADES HIDROGEOLÓGICAS ............................................................ 2**

**4** **MODELO HIDROGEOLÓGICO NUMÉRICO ..................................................................... 6**
**4.1** **Aspectos generales ........................................................................................................................ 6**
**4.2** **Calibración del modelo numérico ............................................................................................... 10**

**5** **ANÁLISIS DEL EFECTO FUTURO DEL DRENAJE DEL RAJO DMH ............................ 15**
**5.1** **Descripción de escenarios .......................................................................................................... 15**
**5.2** **Resultados .................................................................................................................................... 15**
5.2.1 Niveles de agua ........................................................................................................................... 15
5.2.2 Caudal en punto de aforo (RSSN) para nacientes río San Salvador .......................................... 19

**6** **CONCLUSIONES ............................................................................................................ 20**

**LISTADO DE ANEXOS**

Anexo A Hidrogramas de calibración adicionales

**LISTADO DE TABLAS**

Tabla 5-1: Umbrales para pozos en Línea de No Afectación ................................................................ 16

<!-- INICIO TABLA 5-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- La Línea de No Afectación (LNA) sobre los recursos hídricos se encuentra aprobada en el proceso de revisión de la RCA 311/2005 (25 quinquies), a través de la Resolución Exenta N°0002/2018 la cual define los pozos y sus umbrales (Tabla 5-1). Cabe mencionar que el pozo SI-23C fue reemplazado por el CC-17 a través del Ord. N° 761 (30/11/2016). -->

**Tabla 5-1: Umbrales para pozos en Línea de No Afectación****

| Mes inicial<br>Sistema de aguas<br>Pozo Umbral (m.snm) de Nota Fuente<br>subterráneas<br>aplicación | Col2 | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| CC-3<br>-0,064*Mes+2237,76<br>42<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018 | CC-3<br>-0,064*Mes+2237,76<br>42<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018 | CC-3<br>-0,064*Mes+2237,76<br>42<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018 | CC-3<br>-0,064*Mes+2237,76<br>42<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018 | CC-3<br>-0,064*Mes+2237,76<br>42<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018 | CC-3<br>-0,064*Mes+2237,76<br>42<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018 |
| CC-6<br>-0,078*Mes+2249,00<br>40<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018 | CC-6<br>-0,078*Mes+2249,00<br>40<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018 | CC-6<br>-0,078*Mes+2249,00<br>40<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018 | CC-6<br>-0,078*Mes+2249,00<br>40<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018 | CC-6<br>-0,078*Mes+2249,00<br>40<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018 | CC-6<br>-0,078*Mes+2249,00<br>40<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018 |
| CC-17<br>-0,039*Mes+2235,31<br>42<br>Acuífero superior<br>Reemplaza<br>a SI-23C<br>Ord. N° 761 (30/11/2016) | CC-17<br>-0,039*Mes+2235,31<br>42<br>Acuífero superior<br>Reemplaza<br>a SI-23C<br>Ord. N° 761 (30/11/2016) | CC-17<br>-0,039*Mes+2235,31<br>42<br>Acuífero superior<br>Reemplaza<br>a SI-23C<br>Ord. N° 761 (30/11/2016) | CC-17<br>-0,039*Mes+2235,31<br>42<br>Acuífero superior<br>Reemplaza<br>a SI-23C<br>Ord. N° 761 (30/11/2016) | CC-17<br>-0,039*Mes+2235,31<br>42<br>Acuífero superior<br>Reemplaza<br>a SI-23C<br>Ord. N° 761 (30/11/2016) | CC-17<br>-0,039*Mes+2235,31<br>42<br>Acuífero superior<br>Reemplaza<br>a SI-23C<br>Ord. N° 761 (30/11/2016) |
| SI-23C<br>-0,036*Mes+2237,19<br>71<br>Acuífero superior<br>Reemplazado<br>por CC-17<br>Res. Ex. N°0002/2018 | SI-23C<br>-0,036*Mes+2237,19<br>71<br>Acuífero superior<br>Reemplazado<br>por CC-17<br>Res. Ex. N°0002/2018 | SI-23C<br>-0,036*Mes+2237,19<br>71<br>Acuífero superior<br>Reemplazado<br>por CC-17<br>Res. Ex. N°0002/2018 | SI-23C<br>-0,036*Mes+2237,19<br>71<br>Acuífero superior<br>Reemplazado<br>por CC-17<br>Res. Ex. N°0002/2018 | SI-23C<br>-0,036*Mes+2237,19<br>71<br>Acuífero superior<br>Reemplazado<br>por CC-17<br>Res. Ex. N°0002/2018 | SI-23C<br>-0,036*Mes+2237,19<br>71<br>Acuífero superior<br>Reemplazado<br>por CC-17<br>Res. Ex. N°0002/2018 |
| SI-24E | -0,054*Mes+2238,94 | 73 | Acuífero Inferior |  | Res. Ex. N°0002/2018 |

<!-- Estadísticas: 5 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: elaboración propia con información provista por Codelco La LNA establece en su considerando vii lo siguiente: _“Se entenderá que existe afectación sobre los_ _recursos hídricos, a causa del Proyecto, si el nivel medido (en msnm) en al menos uno de los pozos_ -->
<!-- FIN TABLA 5-1 -->


**LISTADO DE FIGURAS**

Figura 1-1: Dominio del modelo Arcadis (2020) ....................................................................................... 1

Figura 3-1: Perfil norte-sur subcuenca Calama - Chuquicamata. Sector rajo DMH ............................... 5

Figura 4-1: Dominio y malla _quadtree_ del modelo actualizado de Arcadis (2020) .................................. 7

Figura 4-2: Acercamiento grilla en zona de DMH - Nacientes del río San Salvador .............................. 8

Figura 4-3: Vista 3D del modelo de Arcadis (2020) ................................................................................. 8

Figura 4-4: Ubicación pozos de extracción de DMH y Minera El Tesoro en modelo de Arcadis (2020) . 9

Figura 4-5: Extracciones históricas pozos DMH 2010-2019 .................................................................... 9

Figura 4-6: Ubicación targets de nivel utilizadas para calibración de modelo numérico actualizado
(Arcadis, 2020) ....................................................................................................................................... 10

Figura 4-7: Comparación niveles simulados vs observados (Arcadis, 2020) ........................................ 11

Figura 4-8: Ubicación puntos seleccionados aguas abajo del rajo DMH............................................... 11

Figura 4-9: Hidrograma de calibración para pozo PBMM-4 (IL-V) ......................................................... 12

Figura 4-10: Hidrograma de calibración para pozo CC-18 (S) .............................................................. 12

2

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

Figura 4-11: Hidrograma de calibración para pozo CC-9 (S) ................................................................ 12

Figura 4-12: Hidrograma de calibración para pozo CC-16 (IC) ............................................................. 13

Figura 4-13: Hidrograma de calibración para pozo CC-10 (IC) ............................................................. 13

Figura 4-14: Hidrograma de calibración para pozo SI-8C (S) ................................................................ 13

Figura 4-15: Balance promedio período 2003 - 2019 modelo Arcadis (2020) ...................................... 14

Figura 4-16: Error de cierre balance de masas modelo Arcadis (2020) ................................................ 14

Figura 5-2: Ubicación pozos de línea de no afectación proyecto DMH ................................................. 15

Figura 5-3: Niveles simulados en pozo CC-3 ......................................................................................... 16

Figura 5-4: Niveles simulados en pozo CC-6 ......................................................................................... 17

Figura 5-5: Niveles simulados en pozo CC-17 ....................................................................................... 17

Figura 5-6: Niveles simulados en pozo SI-24E ...................................................................................... 18

Figura 5-7: Curvas de isodescenso adicional generadas por el Proyecto en evaluación, respecto del
Caso Actual ............................................................................................................................................ 18

Figura 5-8: Caudal simulado en nacientes río San Salvador ................................................................. 19

3

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**1** **INTRODUCCIÓN**

**1.1** **Aspectos generales**

El proceso de evaluación ambiental del proyecto MM (Mansa Misa) demandó la sistematización del
conocimiento hidrogeológico del sector Calama - Chuquicamata a través de la elaboración de un estudio
hidrogeológico del sector. El objetivo del estudio consideró la recolección de información de terreno tales
como estudios geofísicos, perforaciones, ensayos de bombeo, geología de superficie y de subsuperficie,
entre otros. El proceso de recolección de información tuvo como resultado la elaboración de un modelo
conceptual de flujo y un modelo numérico del sistema de agua subterránea de la zona (CPH, 2005). Dicho
modelo se utilizó en el proceso de evaluación ambiental para determinar el potencial de drenaje del rajo
MM (Mansa Mina).

Seguidamente, en base a una mayor cantidad de información, tanto el modelo conceptual como el modelo
numérico fueron actualizados, principalmente en la extensión de su dominio hacía el suroeste, para
incorporar el oasis de Calama. Este último modelo es descrito en el documento “Modelamiento hidráulico
Tranque Talabre y su relación con los acuíferos y cauces superficiales” (Knight Piésold, 2010) y entregado
a DGA quien se pronunció conforme en sus conclusiones y resultados en Ord, N° 330 del 2012.

Con posterioridad, en el proceso de revisión de la RCA 311 de acuerdo con Artículo 25 Quinquies de la
Ley 19.300 (25QQ), se entregó una actualización del modelo numérico (Anexo A del informe “Construcción
Modelo Numérico de Flujo - Efecto del Drenaje del Rajo DMH” (Hidromas, 2015)), donde se realizó la
extensión del dominio del modelo numérico hacia el sector suroeste. La modificación al dominio del modelo
obedeció principalmente a la necesidad de alejar las condiciones de borde numéricas de los objetivos de
evaluación.

Este último modelo fue actualizado y recalibrado por Arcadis (2020) para incorporar información medida
hasta noviembre de 2019. En particular se actualizaron los datos de monitoreo disponibles de la cuenca de
Calama y las extracciones históricas de drenaje del Rajo de la División Ministro Hales de Codelco (DMH).

Para evaluar el potencial efecto que tendrá el programa de desagüe futuro del rajo DMH sobre los sobre
los objetivos de interés ambiental, los cuales corresponden principalmente a la referida “la línea de no
afectación”, definida en la Resolución Exenta No 0002 de enero de 2018 y la tasa de descarga de agua
subterránea en la Naciente del río San Salvador, se han desarrollado una serie de escenarios de operación.
Estos se basan en los flujos que se estiman ingresarán al rajo mediante un modelo de detalle de éste,
desarrollado por ITASCA (2019). Estos escenarios se diseñaron para evalúan el efecto adicional que
generaría el Proyecto en evaluación respecto del Caso Actual vigente hasta el año 2026. El presente
documento reporta la evaluación de dichos escenarios.

La Figura 1-1 muestra el dominio del modelo Arcadis (2020).

**1.2** **Objetivos y alcances**

 - Simular el efecto de modificar el plan de explotación del yacimiento Mansa Mina (nuevo plan de
minado de 500 ktpd).

 - Construir una nueva simulación que incorpore el nuevo pan de desagüe que se estima para este
nuevo plan minero. Dicho plan de desagüe proviene del modelo de detalle del rajo.

 - Evaluar los efectos sobre el sistema de agua subterránea y los objetos de protección descritos en
Resolución Exenta No 0002/2018, representados por la tasa de descarga de agua subterránea en
la Naciente del Río San Salvador y los niveles de agua subterránea en los pozos de la denominada
“Línea de No Afectación” en el límite norte del oasis de Calama.

 - Comparar entre el Caso Actual y el Proyecto en evaluación, estimando el potencial descenso
adicional atribuible al Proyecto.

1

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**Figura 1-1: Dominio del modelo Arcadis (2020)**

Fuente: elaboración propia con datos desde Arcadis (2020)

1

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**2** **REFERENCIAS**

 - Ref. 1 CPH (2005). Modelo hidrogeológico integrado sector Calama Pampa Talabre. Preparado
en Julio 2005 para DCN.

 - Ref. 2 KnightPiésold. (2010). Modelamiento Hidráulico Tranque Talabre y su relación con los
Acuíferos y Cauces Superficiales.

 - Ref. 3 Hidromas. (2012). Servicio de Construcción y Validación de Modelamiento NuméricoModelación Hidrogeológica del Acuífero de Calama.

 - Ref. 4 Hidromas. (2015). Actualización Modelo de Flujo - Estudio Infiltración Tranque Talabre.

 - Ref. 5 KnightPiésold. (2014). Análisis Integrado Río Loa, Región de Antofagasta.

 - Ref. 6 Amphos21 (2019). Servicio Hidrogeológico Salar de Brinkerhoff. Modelo Conceptual
Hidrogeológico.

 - Ref. 7 Arcadis. (2020). Actualización Modelo Hidrogeológico 3D de Flujo Calama-Talabre. Informe
de Actualización y Recalibración a Noviembre 2019.

 - Ref. 8 Panday, S. y otros (2013). MODLFOW-USG Version 1: An Unstructured Grid Version of
MODFLOW for Simulating Groundwater Flow and Tightly Coupled Processes Using a Control
Volume Finite-Difference Formulation. US Geological Survey Techniques and Methods book 6,
chap. A45. 2013.

 - Ref. 9 Panday, S. (2019). Block-centered Transport (BCT) Process for MODFLOW-USG Version
1.4.0. Sorab Panday, GSI Environmental.

 - Ref. 10 ITASCA (2019). Simulaciones Plan Minero DIA. Actualización Modelo Hidrogeológico
Rajo DMH.

 Ref. 11 SEA (2012). GUÍA PARA EL USO DE MODELOS DE AGUAS SUBTERRÁNEAS EN EL
SEIA. Editor: Servicio de Evaluación Ambiental, SEA - ISBN: 978-956-9076-12-1.

1

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**3** **RESUMEN DE UNIDADES HIDROGEOLÓGICAS**

En términos generales la definición de unidades hidrogeológicas no sido modificada respecto de (Knight
Piésold, 2010), excepto por algunas modificaciones locales definidas por Amphos21 (2019), y además
cambios geométricos producto de la perforación de nuevos sondajes en la zona. A continuación, se
presenta un resumen de ellas.

**UH-1: Depósitos Aluvio-Evaporíticos Plio-Pleistocenos**

La unidad hidrogeológica Depósitos Aluvio-Evaporíticos Plio-Pleistocenos está compuesta por las unidades
geológicas reunidas en el grupo de los depósitos no consolidados, además de la Formación Chiu-Chiu. Por
lo tanto, incluye principalmente gravas, arenas, depósitos detrito-evaporíticos y depósitos limo-arenosos,
los que se separan en dos subunidades:

 - UH-1a: Depósitos aluviales de Permeabilidad Media-Alta
La subunidad UH-1a de “Depósitos aluviales de Permeabilidad Media-Alta” está principalmente
formada por gravas y arenas con matriz arenosa, en algunos casos limo arenosa. Su rango de
permeabilidad se estima en un rango amplio, entre 10-1 y 102 m/día.

 - UH-1b: Depósitos detrito-evaporíticos de permeabilidad Media-Baja
La subunidad 1b de “Depósitos detrito-evaporíticos de permeabilidad Media-Baja” está albergada
por la secuencia de la Formación Chiuchiu y rellenos clástico-salinos de salares. Se estima que la
permeabilidad de estos sedimentos se halla en un rango muy inferior a la primera subunidad, de
10-3 y 100 m/día.

**UH-2: Acuífero Cárstico-Detrítico El Loa (“Acuífero Superior”)**

La secuencia conformada por rocas carbonatadas y detríticas pertenecientes principalmente a la
Formación Opache, pero también a la parte superior de la Formación Jalquinche (UG-3c: Secuencia
Superior Calcárea), conforman un acuífero predominantemente de carácter freático y de permeabilidad
muy variable. Este acuífero comúnmente referido como “Superior” (“Unidad Hidrogeológica 1” de GP, 2008,
y “Segundo Acuífero” en DCN, 2005), en el sector noreste de la cuenca también se localiza en las
secuencias sedimentarias de la Formación Lasana. Esta formación engrana con los depósitos de la
Formación Jalquinche, la cual es la responsable principal de la generación del Acuitardo (unidad
hidrogeológica descrita a continuación).

La UH-2 ha sido separada en tres subunidades basado en sus condiciones geológicas, comportamiento
regional freático y rango de permeabilidades, similares en ambos dominios (Calcáreo y Arenoso):

 - UH-2a: Rocas cárstico-arenosas de Permeabilidad Media-Alta
La UH-2a, “Rocas cárstico-arenosas de Permeabilidad Media-Alta”, es el medio predominante de
la unidad, por lo tanto, considerada representativa de la condición típica del Acuífero Superior. La
permeabilidad de esta subunidad es estimada en el rango 10-2 a 101 m/día, basado en los valores
obtenidos mediante ensayos hidráulicos.

 - UH-2b: Depósitos limo-arcillosos de Permeabilidad Baja
Los “Depósitos limo-arcillosos de Permeabilidad Baja”, la UH-2b, tienen una presencia muy inferior
a la subunidad predominante (UH-2a) y corresponde a depósitos finos interceptados por pozos
situados en los sectores noreste y sureste del Tranque Talabre. Su permeabilidad es estimada en
el rango 10-4 a 10-1 m/día, sin la disponibilidad de datos empíricos específicos a esta subunidad.

 - UH-2c: Depósitos de arenas negras de Permeabilidad Alta
La subunidad de “Depósitos de arenas negras de Permeabilidad Alta” (UH-2c) corresponde a
depósitos detríticos, con una presencia importante en el Dominio Arenoso. La conductividad
hidráulica estimada para la UH-2c es de 10-2 a 100 m/día.

2

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**UH-3: Acuitardo Ignimbrítico**

El Acuitardo ignimbrítico está conformado por tobas consolidadas, con soldadas en grado variable, con un
comportamiento hidrogeológico de baja permeabilidad. Estas tobas han sido descritas por Nazca (2001)
en los pozos perforados por Aguas Yalqui; este autor correlacionó las tobas con la Ignimbrita Sifón
(Marinovic y Lahsen, 1984), debido a la presencia de esta unidad geológica en afloramientos cercanos al
campo de pozos de la mencionada empresa de desarrollo de recursos hídricos.

Esta unidad tendría una permeabilidad estimada en base a antecedentes bibliográficos de 10-6 m/día.
Genera confinamiento sobre el medio saturado infrayaciente.

**UH-4: Acuitardo El Loa (“Acuitardo”)**

El Acuitardo El Loa está conformado por una secuencia de muy baja permeabilidad, del orden de <5x10-3
m/día; está predominantemente compuesta por arcillas y limos pertenecientes a la parte inferior de la
Formación Jalquinche (Secuencia Inferior Limo-Arcillosa), corresponde a una unidad hidrogeológica con
un alto grado de homogeneidad.

Se han identificado tres tipos de depósitos diferentes asociados a la misma unidad:

 - UH-4a: Depósitos limo-arcillosos de Permeabilidad Baja

 - UH-4b: Depósitos arenosos de Permeabilidad Media-Alta

 - UH-4c: Lavas volcánicas de Permeabilidad Baja

**UH-5: Acuífero Gravas de Calama (“Acuífero Inferior”)**

El Acuífero Gravas de Calama está formado por la unidad geológica Formación Calama. Las gravas,
conglomerados y arenas gravosas, con matriz arenosa y limo-arenosa, que componen la sección
reconocida, a través de las muestras de sondajes y pozos, de esta formación (aproximadamente 150 m
superiores) se encuentran en su mayor parte saturadas. Se reconocen dos subunidades:

 - UH-5a: Depósitos de gravas
La subunidad UH-5a “Depósitos de gravas” representa el Acuífero Inferior en sus condiciones
típicas, con una conductividad hidráulica -calculada empíricamente- en el rango 5x10-2 a 101
m/día.

 - UH-5b: Depósitos limo-arcillosos
Para la subunidad UH-5b “Depósitos limo-arcillosos”, compuesta por intercalaciones limoarcillosas, se ha estimado una conductividad hidráulica de 10-5 a 10-3 m/día.

**UH-6: Acuicludo Rocas Pre-Terciarias (“Basamento Impermeable”)**

El Acuicludo Rocas Pre-Terciarias está conformado por la unidad geológica “UG-1: Basamento ÍgneoMetamórfico”. Esta unidad agrupa litologías muy diversas, sin embargo, predominan ampliamente las rocas
ígneas y metamórficas sobre las secuencias estratiformes compuestas por rocas volcánicas y
sedimentarias. El conjunto de estas rocas presenta una conductividad hidráulica muy baja, entre 10-9 y 105 m/día, excepto en sectores de roca muy fracturada, zonas de intenso fallamiento y localmente por efecto
de procesos de alteración.

Las unidades hidrogeológicas que mayoritariamente condicionan los flujos subterráneos en el sector de
estudio son las siguientes, ordenados estratigráficamente de menor a mayor profundidad: el Acuífero
Superior, el Acuitardo, el Acuífero Inferior y el Basamento Impermeable (DCN-KP, 2010).

En toda la parte central del área de estudio, en general el Acuífero Superior sobreyace al Acuitardo y éste
a su vez al Acuífero Inferior. En términos generales, la extensión lateral del Acuífero Superior y del Acuitardo
son similares; no obstante, analizado en mayor detalle se observa que en ciertos sectores el Acuífero
Superior se acerca más al borde impermeable; en una menor cantidad de puntos, el Acuitardo alcanza una
mayor cercanía al borde impermeable que el Acuífero Superior.

3

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

Debido a su continuidad hidráulica, el Acuífero Inferior se ha ampliado lateralmente mediante las gravas
Plio-Pleistocenas (UH-1) situadas en los bordes de la cuenca. El análisis de la geometría de las tres
unidades hidrogeológicas principales, vale decir el Acuífero Inferior, Acuitardo y Acuífero Superior. En las
siguientes figuras se muestra perfiles

Para efectos de la modelación hidrogeológica numérica dichas unidades han sido agrupadas de forma
macro para considerar 4 capas, representativas de los siguientes acuíferos:

 - Acuífero superior (calizas/sedimentos)

 - Acuitardo intermedio (depósitos limo-arcillosos)

 - Acuífero inferior (gravas)

 - Basamento hidrogeológico.

En la Figura 3-1 se presenta la geometría de las unidades hidrogeológicas construidas en Leapfrog, y se
comparan contra la malla del modelo numérico, focalizadas en la zona de Calama-Chuquicamata.

4

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**Figura 3-1: Perfil norte-sur subcuenca Calama - Chuquicamata. Sector rajo DMH**

Fuente: elaboración propia

5

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**4** **MODELO HIDROGEOLÓGICO NUMÉRICO**

**4.1** **Aspectos generales**

El modelo numérico utilizado es descrito en detalle en Arcadis (2020) (Ref. 7), por lo que en esta sección
se presenta un resumen de sus características principales.

La elaboración del modelo numérico incluyó la definición de los límites espaciales del modelo, su
discretización horizontal y vertical, la distribución espacial de parámetros hidrogeológicos y la asignación
de condiciones de borde, incluyendo las recargas y descargas de sistema de agua subterránea.

Para modelar el sistema de agua subterránea se ha usado el código numérico MODFLOW, publicado
por el Servicio Geológico de los Estados Unidos (USGS), el cual es uno de los códigos recomendados
por la guía del SEA (2012) para evaluaciones ambientales en Chile, razón por la cual es considerado
para el desarrollo de la herramienta numérica aquí descrita.

La actualización de Arcadis (2020) consideró el cambio del código de flujo de MOFLOW-2000 a
MODFLOW-USG (Ref. 8), en particular a su variante USG-Transport (Ref. 9) debido a que otorga
mejores prestaciones que las versiones previas de MODFLOW, dentro de las cuales se destacan:

 - El uso de mallas no estructuradas para refinar la malla en zonas de interés, permitiendo lograr
mayor precisión con menores tiempos de simulación.

 - Reduce los problemas de convergencia numérica asociados al secado y rehumectación de celdas
en acuíferos libres, producto de napas fluctuantes.

 - Permite introducir discontinuidades de unidades hidrogeológicas (acuñamientos), eliminando la
necesidad de tener capas numéricas continuas.

 - Permite trabajar sólo con celdas inactivas permitiendo tiempos de simulación menores.

 - Incorpora el uso del paquete CLN para simular pozos multicapa, incluyendo la opción de reducir
automáticamente las tasas de bombeo cuando el sistema acuífero no es capaz de sustentarlas.

Para operar el modelo numérico se consideró cambiar desde Visual MODFLOW a la plataforma de prey post- procesamiento Groundwater Vistas 7 de Environmental Simulations Inc, debido a que cuenta
con una mejor integración con MODFLOW-USG en términos de paquetes disponibles.

En la Figura 4-1 se muestra el dominio del modelo, la malla utilizada y la ubicación del río Loa junto a
las nacientes del río San Salvador, mientras que la Figura 4-2 muestra un zoom a la malla usada en
dicha zona. En la Figura 4-3 se muestra una vista 3D del modelo.

6

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**Figura 4-1: Dominio y malla** _**quadtree**_ **del modelo actualizado de Arcadis (2020)**

Celdas de no

flujo modelo

numérico

Fuente: elaboración propia

7

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**Figura 4-2: Acercamiento grilla en zona de DMH - Nacientes del río San Salvador**

Fuente: elaboración propia

**Figura 4-3: Vista 3D del modelo de Arcadis (2020)**

Fuente: elaboración propia

8

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

Los pozos de bombeo considerandos en el modelo se muestran en la Figura 4-4, mientras que las
extracciones históricas asociadas a la red desagüe del rajo DMH se presentan en la Figura 4-5.

**Figura 4-4: Ubicación pozos de extracción de DMH y Minera El Tesoro en modelo de Arcadis**

**(2020)**

Fuente: elaboración propia con datos de Arcadis (2020) (Ref. 7)

**Figura 4-5: Extracciones históricas pozos DMH 2010-2019**

Fuente: elaboración propia con datos provistos por Codelco

9

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**4.2** **Calibración del modelo numérico**

El modelo actualizado fue recalibrado para lograr concordancia entre los niveles de agua simulados y
observados, así como otros aspectos del modelo conceptual.

Para la calibración se consideraron un total de 248 puntos con información de niveles desde enero 2003
a noviembre 2019, la Figura 4-6 muestra la ubicación de estos puntos.

**Figura 4-6: Ubicación targets de nivel utilizadas para calibración de modelo numérico**

**actualizado (Arcadis, 2020)**

Fuente: elaboración propia

El proceso de calibración modificó los parámetros hidráulicos del modelo (Kx, Kz, Ss, Sy) y
conductancias de las condiciones de borde asociadas a lo río Loa y Nacientes del rio San Salvador. En
Figura 4-7 se comparan los niveles simulados vs observados para todos los puntos y para todos los
tiempos (32.244 datos). Se observa que existe buen grado de correlación entre ambas series. Además,
el error cuadrático medio normalizado (NRMS) es inferior al 5% recomendado por SEA (2012) (Ref. 11).

En la Figura 4-8 se muestra la ubicación de pozos seleccionados para presentar la calibración del
modelo en la zona de interés para el proyecto DMH y en Figura 4-9 a Figura 4-14 se presentan
hidrogramas de pozos seleccionados, el resto de los hidrogramas se presenta en el Anexo A de este
documento.

10

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**Figura 4-7: Comparación niveles simulados vs observados (Arcadis, 2020)**

Fuente: elaboración propia con resultados de Arcadis (2020)

**Figura 4-8: Ubicación puntos seleccionados aguas abajo del rajo DMH**

Fuente: elaboración propia

11

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**Figura 4-9: Hidrograma de calibración para pozo PBMM-4 (IL-V)**

Fuente: elaboración propia con resultados de Arcadis (2020)

**Figura 4-10: Hidrograma de calibración para pozo CC-18 (S)**

Fuente: elaboración propia con resultados de Arcadis (2020)

**Figura 4-11: Hidrograma de calibración para pozo CC-9 (S)**

Fuente: elaboración propia con resultados de Arcadis (2020)

12

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**Figura 4-12: Hidrograma de calibración para pozo CC-16 (IC)**

Fuente: elaboración propia con resultados de Arcadis (2020)

**Figura 4-13: Hidrograma de calibración para pozo CC-10 (IC)**

Fuente: elaboración propia con resultados de Arcadis (2020)

**Figura 4-14: Hidrograma de calibración para pozo SI-8C (S)**

Fuente: elaboración propia con resultados de Arcadis (2020)

13

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

El balance hídrico promedio para el periodo 2003 a 2019 es presentado en la Figura 4-15. Se observa
que las principales entradas y salidas corresponden a los flujos subterráneos a través de los límites del
área modelada. Por otra parte, en términos promedio el río Loa - río Salado genera una pequeña
recarga, en vista que los flujos de entrada son levemente mayores a los de salida. Finalmente, la Figura
4-16 presenta el error cierre del balance para toda la simulación. Los valores indican que nunca se
supera el umbral de 1% recomendado por SEA (2012) (Ref. 11).

**Figura 4-15: Balance promedio período 2003 - 2019 modelo Arcadis (2020)**

Fuente: elaboración propia con resultados de Arcadis (2020)

**Figura 4-16: Error de cierre balance de masas modelo Arcadis (2020)**

Fuente: elaboración propia con resultados de Arcadis (2020)

14

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**5** **ANÁLISIS DEL EFECTO FUTURO DEL DRENAJE DEL RAJO DMH**

**5.1** **Descripción de escenarios**

Tomando como base el modelo calibrado a noviembre 2019, se desarrollaron simulaciones predictivas
hasta el año 2028 para verificar los efectos del drenaje del rajo sobre los niveles de agua subterránea,
así como en los flujos en la cabecera del río San Salvador.

Los escenarios fueron implementados bajo las siguientes consideraciones:

 - Se actualizó la información de bombeo del rajo de DMH hasta marzo de 2020.

 - Se realizaron dos escenarios predictivos: el “caso actualmente aprobado y el escenario de
explotación modificado correspondiente al movimiento mina de magnitud 500 ktpd, denominado
“Proyecto en evaluación”.

 - El escenario Proyecto en evaluación toma una condición de drenaje futura (2020-2028) a partir
de los resultados del modelo de detalle del rajo de ITASCA (2019) (Ref.10), considerando
detener todos los flujos que ingresan al rajo mediante pozos de extracción.

**5.2** **Resultados**

**5.2.1 Niveles de agua**

Para evaluar el efecto del drenaje del Rajo DMH en los niveles de agua subterránea se analiza el
comportamiento simulado para los pozos CC-3, CC-6, CC-17 y SI-24E (Figura 5-1), el umbral definido
por la “Línea de No Afectación” vigente y los datos medidos hasta noviembre de 2019.

**Figura 5-1: Ubicación pozos de línea de no afectación proyecto DMH**

Celdas de no

flujo modelo

numérico

Fuente: elaboración propia

15

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

La Línea de No Afectación (LNA) sobre los recursos hídricos se encuentra aprobada en el proceso de
revisión de la RCA 311/2005 (25 quinquies), a través de la Resolución Exenta N°0002/2018 la cual
define los pozos y sus umbrales (Tabla 5-1). Cabe mencionar que el pozo SI-23C fue reemplazado por
el CC-17 a través del Ord. N° 761 (30/11/2016).

**Tabla 5-1: Umbrales para pozos en Línea de No Afectación**

|Mes inicial<br>Sistema de aguas<br>Pozo Umbral (m.snm) de Nota Fuente<br>subterráneas<br>aplicación|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|CC-3<br>-0,064*Mes+2237,76<br>42<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018|CC-3<br>-0,064*Mes+2237,76<br>42<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018|CC-3<br>-0,064*Mes+2237,76<br>42<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018|CC-3<br>-0,064*Mes+2237,76<br>42<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018|CC-3<br>-0,064*Mes+2237,76<br>42<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018|CC-3<br>-0,064*Mes+2237,76<br>42<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018|
|CC-6<br>-0,078*Mes+2249,00<br>40<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018|CC-6<br>-0,078*Mes+2249,00<br>40<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018|CC-6<br>-0,078*Mes+2249,00<br>40<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018|CC-6<br>-0,078*Mes+2249,00<br>40<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018|CC-6<br>-0,078*Mes+2249,00<br>40<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018|CC-6<br>-0,078*Mes+2249,00<br>40<br>Acuífero inferior<br> <br>Res. Ex. N°0002/2018|
|CC-17<br>-0,039*Mes+2235,31<br>42<br>Acuífero superior<br>Reemplaza<br>a SI-23C<br>Ord. N° 761 (30/11/2016)|CC-17<br>-0,039*Mes+2235,31<br>42<br>Acuífero superior<br>Reemplaza<br>a SI-23C<br>Ord. N° 761 (30/11/2016)|CC-17<br>-0,039*Mes+2235,31<br>42<br>Acuífero superior<br>Reemplaza<br>a SI-23C<br>Ord. N° 761 (30/11/2016)|CC-17<br>-0,039*Mes+2235,31<br>42<br>Acuífero superior<br>Reemplaza<br>a SI-23C<br>Ord. N° 761 (30/11/2016)|CC-17<br>-0,039*Mes+2235,31<br>42<br>Acuífero superior<br>Reemplaza<br>a SI-23C<br>Ord. N° 761 (30/11/2016)|CC-17<br>-0,039*Mes+2235,31<br>42<br>Acuífero superior<br>Reemplaza<br>a SI-23C<br>Ord. N° 761 (30/11/2016)|
|SI-23C<br>-0,036*Mes+2237,19<br>71<br>Acuífero superior<br>Reemplazado<br>por CC-17<br>Res. Ex. N°0002/2018|SI-23C<br>-0,036*Mes+2237,19<br>71<br>Acuífero superior<br>Reemplazado<br>por CC-17<br>Res. Ex. N°0002/2018|SI-23C<br>-0,036*Mes+2237,19<br>71<br>Acuífero superior<br>Reemplazado<br>por CC-17<br>Res. Ex. N°0002/2018|SI-23C<br>-0,036*Mes+2237,19<br>71<br>Acuífero superior<br>Reemplazado<br>por CC-17<br>Res. Ex. N°0002/2018|SI-23C<br>-0,036*Mes+2237,19<br>71<br>Acuífero superior<br>Reemplazado<br>por CC-17<br>Res. Ex. N°0002/2018|SI-23C<br>-0,036*Mes+2237,19<br>71<br>Acuífero superior<br>Reemplazado<br>por CC-17<br>Res. Ex. N°0002/2018|
|SI-24E|-0,054*Mes+2238,94|73|Acuífero Inferior||Res. Ex. N°0002/2018|

Fuente: elaboración propia con información provista por Codelco

La LNA establece en su considerando vii lo siguiente: _“Se entenderá que existe afectación sobre los_
_recursos hídricos, a causa del Proyecto, si el nivel medido (en msnm) en al menos uno de los pozos_
_indicados en la siguiente tabla, se encuentran por debajo del umbral en cualquier medición mensual. En_
_este caso, el titular deberá iniciar la medida de compensación propuesta y aceptada (reinyección al_
_acuífero). Los pozos que componen la “Línea de No Afección” está compuesta finalmente por los_
_siguientes pozos y sus respectivos umbrales:”_ .

En la Figura 5-2 a Figura 5-5 se presenta el nivel modelado de cada pozo, comparando ambos
escenarios desde el año 2010 a 2026, la línea de no afectación (LNA) y los datos medidos disponibles.
En primer lugar, se observa que la modificación del caudal de bombeo desde el Caso Actual al Proyecto
en evaluación no genera cambios en la predicción de niveles, por otra parte, tampoco generan un nivel
que supera en ningún instante los umbrales definidos.

**Figura 5-2: Niveles simulados en pozo CC-3**

Fuente: elaboración propia

16

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**Figura 5-3: Niveles simulados en pozo CC-6**

Fuente: elaboración propia

**Figura 5-4: Niveles simulados en pozo CC-17**

Fuente: elaboración propia

En la Figura 5-6 se muestra un mapa de isodescenso adicional, es decir aquel que aporta el Proyecto
en evaluación por sobre el Caso Actual. En ella se observa que la línea de isodescenso adicional igual
a 5 cm no alcanza al año 2026 ninguno de los cuatro pozos de la LNA.

17

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**Figura 5-5: Niveles simulados en pozo SI-24E**

Fuente: elaboración propia

**Figura 5-6: Curvas de isodescenso adicional generadas por el Proyecto en evaluación,**

**respecto del Caso Actual**

Fuente: elaboración propia

18

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**5.2.2 Caudal en punto de aforo (RSSN) para nacientes río San Salvador**

El caudal proyectado para el aforo del punto RSSN (Nacientes río San Salvador), parte del Plan de
Vigilancia Ambiental (PVA) de Codelco, se muestra en la Figura 5-7. En ella se comparan ambos
escenarios simulados, los datos medidos por Codelco y el promedio de la información disponible (2014
a 2019).

El comportamiento del caudal simulado para la cabecera de río San Salvador para la situación histórica
(mayo 2014 a noviembre 2019), se ajusta de forma razonable con el promedio de los datos históricos.
Se puede observar la alta variabilidad natural de los caudales medidos en la naciente del rio. Esta
variabilidad se manifiesta no solo a nivel diario, sino que también a escala mensual. Luego, es posible
constatar que las simulaciones caen dentro del rango de variación natural del rio.

Finalmente, se observa que los caudales simulados para RSSN en el período 2020 a 2026 son idénticos
para ambos escenarios proyectados, es decir, el Proyecto en evaluación no generaría una disminución
adicional respecto del caudal que se estima para el Caso Actual. Este hecho es concordante con las
curvas de isodescenso adicional presentadas en la Figura 5-6, donde el isodescenso de 5 cm no
alcanzaría al año 2026 el punto RSSN.

**Figura 5-7: Caudal simulado en nacientes río San Salvador**

Fuente: elaboración propia

19

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

**6** **CONCLUSIONES**

La actualización más reciente del modelo numérico mantiene, y en algunos casos mejora, los ajustes
presentados en procesos de actualizaciones anteriores (2012 - 2015 - 2017), y representa de manera
aceptable el comportamiento del acuífero.

Mediante el modelo numérico se evalúa que efectos del drenaje futuro a causa del Proyecto en
evaluación son prácticamente los mismos que el Caso Actual en desarrollo, tanto para niveles de aguas
subterráneas de los pozos de la LNA como para los caudales en las nacientes del San Salvador.

Según las simulaciones y su comparación con el comportamiento real del acuífero (mediciones de
niveles de aguas subterráneas en pozos), no se prevén la activación de umbrales a causa del drenaje
del rajo, tanto en el caso actual en desarrollo, como para el caso del proyecto en evaluación.

La disminución adicional de caudal en la cabecera del San Salvador a causa del proyecto en evaluación
es despreciable y de un orden de magnitud inferior a la variabilidad natural de los caudales medidos en
terreno.

La disminución adicional de caudal en la cabecera del San Salvador se mantiene en el rango declarado
en el proceso de revisión de la RCA N°311/2005.

20

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

### ANEXO A HIDROGRAMAS DE CALIBRACIÓN ADICIONALES

21

ACTUALIZACIÓN MODELO HIDROGEOLÓGICO NUMÉRICO 3D REGIONAL CALAMA-TALABRE

22

Arcadis

Av. Antonio Varas 621
Providencia, Santiago
T: +56 2 2381 6000

**arcadis.com**