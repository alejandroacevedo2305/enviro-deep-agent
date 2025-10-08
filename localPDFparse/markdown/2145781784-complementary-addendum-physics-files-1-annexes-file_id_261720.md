---
title: Sin título
author: pschnettler
date: D:20211031220501-03'00'
language: es
type: report
pages: 35
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME TÉCNICO MODELACIÓN “CENTRO DE ENGORDA DE SALMONÍDEOS, CANAL BERTRAND, AL NORTE DE ISLA RIESCO, COMUNA DE RÍO VERDE, REGIÓN DE MAGALLANES Y ANTÁRTICA CHILENA, No PERT 213121034” CULTIVOS OTWAY S.A.
-->

# INFORME TÉCNICO MODELACIÓN “CENTRO DE ENGORDA DE SALMONÍDEOS, CANAL BERTRAND, AL NORTE DE ISLA RIESCO, COMUNA DE RÍO VERDE, REGIÓN DE MAGALLANES Y ANTÁRTICA CHILENA, No PERT 213121034” CULTIVOS OTWAY S.A.

ELABORADO POR

BUIN 367 - PUERTO MONTT

+56-652752179

[info@ecosistema.cl](mailto:info@ecosistema.cl)

[www.ecosistema.cl](http://www.ecosistema.cl/)

Puerto Montt, octubre 2021

**ÍNDICE**

**1.** **ANTECEDENTES GENERALES ................................................................................................................. 4**

**2.** **OBJETIVOS ............................................................................................................................................ 6**

**3.** **METODOLOGÍA ..................................................................................................................................... 7**

**4.** **DATOS DE ENTRADA. .......................................................................................................................... 10**

**5.** **RESULTADOS ...................................................................................................................................... 14**

5.1 S ERIE DE A LIMENTO .............................................................................................................................. 14

5.1.1 C ICLO C OMPLETO ................................................................................................................................. 14

5.1.2 C ICLO C UADRATURA ............................................................................................................................. 17

5.1.3 C ICLO S ICIGIA ...................................................................................................................................... 19

5.2 A LIMENTO DE M AYOR D IÁMETRO ........................................................................................................... 21

5.2.1 C ICLO C OMPLETO ................................................................................................................................. 21

5.2.2 C ICLO C UADRATURA ............................................................................................................................. 23

5.2.3 C ICLO S ICIGIA ...................................................................................................................................... 25

5.3 C OMPARACIÓN T ASAS DE D EPOSITACIÓN .................................................................................................. 27

**6.** **COMENTARIOS FINALES ...................................................................................................................... 29**

**7.** **ANEXOS .............................................................................................................................................. 30**

**ÍNDICE DE TABLAS**

Tabla 1. Modelaciones realizadas para centro Canal Bertrand ........................................................................... 10
Tabla 2. Datos de producción, características de alimento utilizados para el modelo DEPOMOD ................... 11
Tabla 3. Especificación del alimento utilizado para el modelo DEPOMOD ...................................................... 12
Tabla 4. Profundidad promedio por configuración. ............................................................................................ 12
Tabla 5. Capas de corrientes utilizadas en la modelación .................................................................................. 12
Tabla 6. Capas de corrientes utilizadas en la modelación .................................................................................. 12
Tabla 7. Superficie tasa de depositación carbono orgánico durante un ciclo de 30 días de medición. Serie de

alimento ...................................................................................................................................................... 14

Tabla 8. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Ciclo completo de corrientes y serie

de alimento ................................................................................................................................................. 15
Tabla 9. Superficie tasa de depositación carbono orgánico de acuerdo con modelación depomod por tasa de

depositación durante un ciclo de cuadratura. .............................................................................................. 17
Tabla 10. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de cuadratura y serie de

alimento ...................................................................................................................................................... 18

Tabla 11. Superficie tasa de depositación carbono orgánico durante un ciclo de sicigia. Serie alimento .......... 19
Tabla 12. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de sicigia y serie de

alimento ...................................................................................................................................................... 20

Tabla 13. Superficie tasa de depositación carbono orgánico durante un ciclo de 30 días de medición. Alimento

mayor diámetro ........................................................................................................................................... 21
Tabla 14. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Ciclo Completo de Corrientes y

alimento de mayor diámetro. ...................................................................................................................... 22
Tabla 15. Superficie por tasa de depositación durante un ciclo de cuadratura. Alimento mayor diámetro ........ 23
Tabla 16. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de Cuadratura y

alimento de mayor diámetro. ...................................................................................................................... 24
Tabla 17. Superficie tasa de depositación carbono orgánico durante corrientes de sicigia. Alimento mayor

diámetro ...................................................................................................................................................... 25

Tabla 18. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de sicigia y alimento de

mayor diámetro. .......................................................................................................................................... 26
Tabla 19. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de sicigia y alimento de

mayor diámetro. .......................................................................................................................................... 27

**ÍNDICE DE FIGURAS**

Figura N° 1. Ubicación geográfica de la zona de emplazamiento del proyecto. .................................................. 8
Figura N° 2. Ubicación módulos para modelación. ............................................................................................ 11
Figura N° 3. Dispersión y concentración de carbono. Ciclo completo de medición de corrientes. Serie alimento

.................................................................................................................................................................... 15

Figura N° 4. Frecuencias de ocurrencias de tasas de depositación. Ciclo completo de medición de corrientes.

Serie Alimento ............................................................................................................................................ 16

Figura N° 5. Dispersión y concentración de carbono. Período cuadratura. Serie Alimento ............................... 17
Figura N° 6. Frecuencias de ocurrencias de tasas de depositación. Corrientes de cuadratura. Serie Alimento .. 18
Figura N° 7. Dispersión y concentración de carbono. Período Sicigia. Serie Alimento ..................................... 19
Figura N° 8. Frecuencias de ocurrencias de tasas de depositación. Corrientes de sicigia. Serie Alimento ........ 20
Figura N° 9. Dispersión y concentración de carbono. Ciclo completo mediciones de corrientes. Alimento

mayor diámetro ........................................................................................................................................... 21
Figura N° 10. Frecuencias de ocurrencias de tasas de depositación. Ciclo Completo de Corrientes. Alimento

Mayor Diámetro ......................................................................................................................................... 22
Figura N° 11. Dispersión y concentración de carbono. Período Cuadratura. Alimento mayor diámetro ........... 23
Figura N° 12. Frecuencias de ocurrencias de tasas de depositación. Corrientes de Cuadratura. Alimento Mayor

Diámetro ..................................................................................................................................................... 24

Figura N° 13. Dispersión y concentración de carbono. Corrientes de sicigia. Alimento mayor diámetro ......... 25
Figura N° 14. Frecuencias de tasas de depositación. Período Sicigia. Alimento mayor diámetro ..................... 26
Figura N° 15. Frecuencias de tasas de depositación. Período ciclo completo de corrientes. .............................. 27
Figura N° 16. Frecuencias de tasas de depositación. Período cuadratura. .......................................................... 28
Figura N° 17. Frecuencias de tasas de depositación. Período sicigia. ................................................................ 28

**1.** **ANTECEDENTES GENERALES**

Al igual que en Chile, en todos los países desarrollados que cultivan salmones, el elemento central de
los planes de manejo de los centros de cultivo es minimizar los impactos sobre el bentos.
Generalmente, esto se realiza monitoreando algunos parámetros físicos y químicos del fondo marino,
así como también la estructura poblacional del bentos en sectores aledaños a los centros de cultivo
a intervalos regulares o en momentos específicos durante el ciclo de producción.

Los datos obtenidos son usados para determinar la escala y la extensión de los impactos; sin
embargo, este procedimiento tiene la desventaja que las mediciones puntuales (espaciales y
temporales) no pueden entregar una imagen global de la situación y el inconveniente es que, en la
mayoría de los casos, las mediciones de campo tienen un costo relativamente alto y consumen una
gran cantidad de tiempo.

En tales condiciones, los modelos computacionales, junto con algunas medidas de campo,
representan una poderosa herramienta para investigar, evaluar y manejar los impactos de los centros
de cultivo sobre el medio acuático. Es por ello que la modelación numérica de la deposición y de los
impactos bénticos de los residuos provenientes de centros de cultivo está siendo reconocida cada
vez más como una de las componentes importantes de los procesos de manejo de la acuicultura
(Ervik et al., 1997 [1] ; Henderson et al., 2001 [2] ; Cromey et al., 2002 [3] ; Pérez et al., 2002 [4] ; SEPA, 2003 [5] ).

En los últimos años varios países han desarrollado modelos para estimar la capacidad de carga de los
cuerpos de agua dedicados a los cultivos, entre los cuales se encuentran: DEPOMOD, modelo de
dispersión (Escocia), SUMSED, modelo de dispersión y sedimentación (Chile, España), MOM, modelo
de dispersión e impacto en el fondo, FJIORDENV, modelo de calidad de agua (Suecia, Noruega), LESV
IMPUT, modelo de nutrientes y calidad de agua, OPENSED y OPENDISP, modelos que predicen la tasa
de deposición de carbono en el sedimento bajo las jaulas y la dispersión de desechos solubles y
particulado proveniente de ellas, respectivamente (Escocia), y RTM, modelo que describe el impacto
del enriquecimiento orgánico en la dinámica Potencial Redox de los sedimentos (Escocia).

Actualmente en Chile el modelo deposicional más utilizado es el modelo DEPOMOD, desarrollado
por Cromey _et al_, (2002). Este modelo permite estimar a escala local la tasa de depositación de
biosólidos producto del porcentaje de alimento no consumido y fecas; para ello considera variables
productivas, tales como cantidad de alimento vertido en un ciclo de producción, características del
alimento, datos oceanográficos del sector y con ello poder simular el flujo y cantidad de desechos

desde las balsas de cultivo al fondo marino.

1 Ervik A, Kupka P, Aure J, Stigebrandt A, Johannessen P & Jahnsen T. (1997) Regulating the local environmental impact of intensive marine
fish farming I. The concept of the MOM system (Modelling-Ongrowing fish farms-Monitoring) Aquaculture 158 (1997) 85-94
2 Henderson A, Gamito S., Karakassis, P. Pederson I y Smaal A. Use of hydrodynamic and benthic models for managing environmental
impacts of marine aquaculture. J. Appl. Ichthyol. 17 (2001), 163-172.

3 Cromey Ch, Nickell TD & Black, DEPOMOD--modelling the deposition and biological effects of waste solids from marine cage farms.
Aquaculture 214: 211 -239
4 Peréz OM, Telfer TC, Beveridge MCM & Ross LG (2002) Geographical Information Systems (GIS) as a Simple Tool to Aid Modelling of
Particulate Waste Distribution at Marine Fish Cage Sites. Estuarine, Coastal and Shelf Science 54, 761-768.
5 SEPA (2003) Regulation and Monitoring of Marine Cage Fish Farming in Scotland Methods for Modelling In-feed Anti-parasitics and

Benthic effects

Este modelo está estructurado en cuatro módulos que se acoplan para estimar las concentraciones
de Carbono Orgánico Total (COT) en el fondo. Estos son: a) generación de la grilla (GRIDGEN), b)
trayectoria de partículas (PARTRACK) y c) re-suspensión y módulo de respuesta bentónica (RESUS).
El cuarto módulo (BENTHIC) conecta los tres primeros, cuantificando la dispersión de los residuos
liberados por los centros de cultivo para la estimación de la concentración de carbono orgánico total
(COT) en el bentos. (IFOP, 2013 [6] ).

El presente informe presenta los resultados de la modelación con el programa DEPOMOD, para dar
respuestas a las observaciones realizadas al informe entregado en adenda para la solicitud de
concesión Canal Bertrand de la empresa Cultivos Otway S.A., ubicado en canal Bertrand al norte de
isla Riesco en la comuna de Rio Verde de la Región de Magallanes y Antártica Chilena.

La modelación fue realizada sobre la base de datos de producción entregados por el mandante; en
tanto, los datos oceanográficos utilizados son aquellos levantados en el marco de desarrollo de la
Caracterización Preliminar de Sitio, como requisito normativo para el otorgamiento del PAS 116 del
D.S. No 40/2012.

6 Instituto fomento Pesquero IFOP. Informe final Experiencia Internacional en el uso de DEPOMOD para la Acuicultura.

**2.** **OBJETIVOS**

a. Establecer la tasa de depositación y dispersión de Carbono generado anualmente por el

proyecto.
b. Determinar el área de depositación de Carbono.

**3.** **METODOLOGÍA**

Dado que el informe de modelación presentado en adenda del proyecto DIA “CENTRO DE ENGORDA
DE SALMONÍDEOS, CANAL BERTRAND AL NORTE DE ISLA RIESCO, COMUNA DE RÍO VERDE, REGIÓN
DE MAGALLANES Y ANTÁRTICA CHILENA, No PERT 213121034” tuvo observaciones, el presente
documento presenta una nueva modelación para dar respuestas a dichas observaciones, en lo
particular a aquella que solicita modelar con los datos de entrada que el software DEPOMOD V2 tiene
por defecto, respecto lo cual, si bien se modela nuevamente no se utilizan los datos por defecto,
dado que dichos datos corresponde a publicaciones del año 2002; a la fecha la industria alimenticia
y la tecnología de alimentación ha ido evolucionando y tecnificándose con el propósito de generar
alimentos altamente energéticos y con mejores porcentajes de digestibilidad y al mismo tiempo las
tecnologías de alimentación apuntan a disminuir la pérdida de alimento no consumido, motivo por
el cual la presente modelación se realiza con datos bibliográficos entregados por Chang _et al_ en el
año 2014 [7] .

De la misma manera se aclara que las modelaciones se realizan sin activar el modo de resuspensión
consideración que fue acordada en el taller organizado por el Servicio de Evaluación Ambiental de la
Región de Magallanes y Antártica Chilena en noviembre del año 2019.

Dado que se utilizaron como datos de entrada aquello entregados por Chang _et al_ (2014), y que
difieren de los datos de entrada presentados en el informe adjunto en adenda, el titular decide
disminuir la producción a 5.000 toneladas utilizando una sola configuración de 28 balsas jaulas de
30x30x20m distribuidas en 2 módulos, dicho lo anterior, se describe a continuación la metodología
de trabajo:
Se realizó una modelación matemática de la tasa de depositación de carbono orgánico total que
aportaría la operación del centro Canal Bertrand considerando una producción de 5.000 toneladas
considerando una de 28 balsas de 30x30x20m, distribuidas en dos módulos de 14 unidades cada una.

La solicitud de concesión se ubica en el canal Bertrand al norte de isla Riesco, comuna de Río Verde,
Región de Magallanes y Antártica Chilena. ( **Figura 1** ).

7 B. D. Chang*, F. H. Page, R. J. Losier, E. P. McCurdy† (2014). Organic enrichment at salmon farms in the Bay of Fundy, Canada: DEPOMOD
predictions versus observed sediment sulfide concentrations. AQUACULTURE ENVIRONMENT INTERACTIONS. Vol. 5: 185-208, 2014

Figura N° 1. Ubicación geográfica de la zona de emplazamiento del proyecto.

Se realizan 6 modelaciones, todas ellas con la máxima biomasa de 5.000 ton, en período de
cuadratura, sicigia y ciclo completo de corrientes utilizando la serie de alimento indicado en la **Tabla**
**1** del presente documento y los mismos escenarios antes indicados, pero utilizando sólo el alimento
de mayor tamaño, todo ello para la configuración de 28 balsas de 30x30x20m, distribuidos en dos

módulos de 14 unidades cada uno.

Tal como ya se indicó las modelaciones se realizan con el modo de resuspensión desactivado.

El trabajo se ha realizado de la siguiente manera:

1. Recopilación de antecedentes

Se recopilan los antecedentes productivos y oceanográficos, en esta etapa se revisan y analizan los
antecedentes entregados por el mandante en relación al ciclo de producción (biomasa a cultivar,
estimación del alimento vertido acumulado, características del alimento a verter, tiempo de cultivo,
tipo y dimensiones de las balsas jaulas, fracción no consumida, porcentaje de digestibilidad y de
humedad del alimento), y datos oceanográficos, como plano de ubicación del centro y de las
unidades de cultivo, batimetría del sector y estudio de corrientes. Toda esta información se ordena
para posteriormente ser utilizada como datos de entrada del software ( **Tabla 1 y 2** ).

2. Trabajo de gabinete:

a. Modelación con DEPOMOD, utilizando los módulos correspondientes a Grilla (Gridgen),

trayectoria de partículas (Partrack) y resuspensión (RESUS) **sin activar el modo de**
**resuspensión** .
b. El resultado obtenido del DEPOMOD, se procesa mediante el software Surfer 13.
c. Para la determinación del área de sedimentación del carbono orgánico total se utiliza el

software Autocad, versión 2021.

El estudio de corrientes utilizado y el perfil batimétrico del área solicitada en concesión son aquellos
levantados en el marco de desarrollo de la Caracterización Preliminar de Sitio, como requisito
normativo para el otorgamiento del PAS 116 del D.S. No 40/2012.

En tanto los datos productivos utilizados tales como, biomasa a cultivar, estimación del alimento
vertido acumulado, características del alimento a verter, tiempo de cultivo, tipo y dimensiones de las
balsas jaulas, fueron entregados por el titular del proyecto; en tanto la fracción no consumida,
porcentaje de digestibilidad, humedad del alimento, porcentaje de carbono en el alimento y en el
pellet son datos bibliográficos aportados por Chang _et al_ (2014) [7]

**4.** **DATOS DE ENTRADA.**

La siguiente **tabla 1** muestra el detalle de las modelaciones realizadas.

Tabla 1. Modelaciones realizadas para centro Canal Bertrand

|Escenario|Configuración|Estructuras|Biomasa|Corrientes|
|---|---|---|---|---|
|Serie Alimento|2 módulos|28 balsas<br>(30x30x20m)|5.000<br>toneladas|Ciclo<br>completo: 30<br>días|
|Serie Alimento|2 módulos|28 balsas<br>(30x30x20m)|5.000<br>toneladas|Período de<br>cuadratura|
|Serie Alimento|2 módulos|28 balsas<br>(30x30x20m)|5.000<br>toneladas|Período de<br>sicigia|
|Alimento Mayor<br>Diámetro|2 módulos|28<br>balsas<br>(30x30x20m)|5.000<br>toneladas|Ciclo<br>completo: 30<br>días|
|Alimento Mayor<br>Diámetro|2 módulos|28<br>balsas<br>(30x30x20m)|5.000<br>toneladas|Período de<br>cuadratura|
|Alimento Mayor<br>Diámetro|2 módulos|28<br>balsas<br>(30x30x20m)|5.000<br>toneladas|Período de<br>sicigia|

Para la modelación se realizó un estudio de corrientes por 30 días, desde el 13 de agosto hasta el 14
de septiembre de 2019, con datos colectados cada 10 minutos (600 segundos), midiendo una
columna total de 120m. De este estudio se seleccionaron 5 capas distribuidas dentro de toda la
columna de agua a partir de los 20m de profundidad, correspondiente a la profundidad de la red
pecera. Entre los 20 y los 35 metros si bien se observó mayor dispersión en las direcciones de la
corriente y si bien ésta se mantiene hacia los estratos más profundos, desde los 35 metros tiende a
observarse una tendencia bimodal en el resto de la columna de agua por lo que el criterio de
selección de capas se basó en el comportamiento bastante homogéneo de la columna tanto en el
primer rango de profundidad antes mencionado así como hacia los estratos más profundos, en
cuanto a direcciones y en un comportamiento también esperable en cuanto a magnitudes, las que
van disminuyendo a medida que aumentaba la profundidad.
Sin perjuicio de lo anterior, en virtud de la **observación 7** **letra b del título III del adenda**
**complementaria** que indica “ _La tabla 5 ..._ _En base a lo anterior, es importante mencionar que, para_
_obtener una modelación representativa, se deben eliminar las capas que contengan interferencia_
_tanto en superficie como en el fondo. Para ello, comúnmente se eliminan las capas superiores y de_
_fondo_ ”, las modelaciones realizadas en el presente informe utilizan como capa profunda la
correspondiente a los 116 m, con ello se da cumplimiento a lo observado, no considerando las dos
últimas capas del estudio de corrientes y mantiene el uso de la capa de los 20m, como la primera
capa de corrientes.

La **Figura 2** muestra la ubicación de los módulos.

Figura N° 2. Ubicación módulos para modelación.

La **Tabla 2** indica los datos generales utilizados para la modelación, en tanto la **Tabla 3** muestra el
detalle del tipo de alimento utilizado para la modelación.

Tabla 2. Datos de producción, características de alimento utilizados para el modelo DEPOMOD

|Variable|Unidades|Configuración|
|---|---|---|
|Producción|Kilos|5.000.000|
|Ciclo de cultivo|Días|549|
|Balsa jaulas|Número|28|
|Dimensiones|Metros|30x30x20|
|Peso ingreso|Kilos|0.15|
|Peso cosecha|Kilos|5|
|Alimento acumulado|Kilos|5.558.108|
|Suministro alimento|Kilos/Balsa/día|361,6|
|ANC|%|38|
|Digestibilidad|%|908|
|Humedad alimento|%|108|
|Carbono alimento|%|578|
|Carbono fecas|%|338|

8 B. D. Chang*, F. H. Page, R. J. Losier, E. P. McCurdy† (2014). Organic enrichment at salmon farms in the Bay of Fundy, Canada: DEPOMOD
predictions versus observed sediment sulfide concentrations. AQUACULTURE ENVIRONMENT INTERACTIONS. Vol. 5: 185-208, 2014

Tabla 3. Especificación del alimento utilizado para el modelo DEPOMOD

|Especificación Alimento|Col2|Col3|
|---|---|---|
|Diámetro (um)|Velocidad sedimentación (m/s)|%Mass9|
|4000|0,082|5|
|6000|0,096|20|
|9000|0,122|75|

La **Tabla 4** muestra la profundidad promedio de la zona de emplazamiento de cada módulo de cultivo.

Tabla 4. Profundidad promedio por configuración.

|Configuración|Profundidad media<br>zona ubicación módulos (m)|
|---|---|
|2 módulos de 14 balsas: 28 balsas (30x30x20m)|122|

La **Tabla 5** muestra las capas de corrientes utilizadas en la modelación. Para mayor información
revisar estudio de corrientes adjunto en el anexo 5 de la DIA. En tanto la **Tabla 6** muestra el detalle
de velocidad, cantidad de datos, tiempos de medición y altura de marea para los períodos de ciclo
completo de mediciones de corrientes, ciclo cuadratura y sicigia.

Tabla 5. Capas de corrientes utilizadas en la modelación

|Capas|Profundidad (m)|Distancia de la capa al fondo marino<br>(m)|
|---|---|---|
|10|20|102|
|25|50|72|
|38|76|46|
|48|96|26|
|58|116|6|

Tabla 6. Capas de corrientes utilizadas en la modelación

|Período Lunar|No datos|Tiempo de medición<br>(s)|Velocidad media<br>ultima capa (cm/s)|Altura Marea<br>(m)|
|---|---|---|---|---|
|Ciclo Completo|4.579|600|2.17|0,6|
|Cuadratura|1.154|600|1.79|0,4|
|Sicigia|1.461|600|2.32|0,5|

**Coeficientes de dispersión:**
Se utilizan los dados por defecto por el software DEPOMOD:
Dispersión horizontal (x): 0.1 m [2] s [-1]
Dispersión vertical (y): 0.1 m [2] s [-1]
Dirección vertical (z): 0.01 m [2] s [-1 ]

9 Corresponde al porcentaje de tiempo en que se suministra cada tipo de alimento especificado en la tabla durante el ciclo productivo

**Modo trayectoria de partículas:**
Número de partículas: 10 (por defecto entregado por el software DEPOMOD)
Exactitud de la evaluación de la trayectoria: Alto (60 s), dado por defecto por el Software DEPOMOD.

**Datos de entrada oceanográficos:**

1. **Matriz batimétrica**, datos crudos presentados en CPS, planilla Excel con coordenadas UTM y

profundidades corregidas al NRS.

2. **Profundidad media del sector de emplazamiento de los módulos de cultivo** : **122m** de

acuerdo a resultados de la batimetría.

3. **Plano base**, posición de los módulos propuesta por el Titular

**5.** **RESULTADOS**

A continuación, se presentan los resultados de las modelaciones realizadas para los tres escenarios,
el primero utilizando toda la batería de datos de corrientes “Ciclo Completo”, es decir, se utilizaron
todos los datos colectados durante los 30 días de medición, el segundo utilizando las corrientes en
período de cuadratura y el tercero en período de sicigia.

En **anexo 4** se adjuntan las salidas del software y en tanto en **anexo 5** se adjuntan planillas Excel con
el resultado de las tasas de depositación de carbono (archivo.sur)

Dado que todos los resultados dieron tasas cercanas a los 1,8kgC/m2/año, las figuras de depositación
muestran la misma escala, sin embrago las diferencias en las tasas máximas se detallarán en la **tabla**
**19** y en **anexo 5** antes indicado.

**5.1** **Serie de Alimento**

**5.1.1** **Ciclo Completo**

El resultado de la modelación se presenta en la **Tabla 7** y **Figura 3** . Del total del área de
sedimentación, se tiene lo siguiente:

Tabla 7. Superficie tasa de depositación carbono orgánico durante un ciclo de 30 días de medición. Serie de alimento

|Tasa depositación (kg C/m/año)|Superficie (m2)|Porcentaje (%)|
|---|---|---|
|1.0 - 1.2|13.237|27,6%|
|1.2 - 1.4|15.401|32,1%|
|1.4 - 1.6|19.224|40,1%|
|1.6 - 1.8|124|0,26%|
|**TOTAL**|**47.986**|**100%**|

Figura N° 3. Dispersión y concentración de carbono. Ciclo completo de medición de corrientes. Serie alimento

De acuerdo con los resultados obtenidos en las modelaciones se tiene que las tasas de depositaciones
varían entre 1,0 y 1,791 KgC/m [2] /año (ver serie depositación, **anexo 5** archivos resus), el área de
depositación total es de 47.986m [2], la máxima tasa de depositación de 1,791kg/m [2] /año, equivalente
a 4,91grC/m [2] /día representa el 0,03% de la superficie total de la pluma y se deposita íntegramente
dentro del polígono.

La siguiente **tabla 8** y **figura 4** muestra la frecuencia de ocurrencia de las tasas de depositación, en
donde se puede observar el porcentaje de participación de cada tasa de depositación.

Tabla 8. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Ciclo completo de corrientes y serie de alimento

|Tasa Depositación (kgC/m2/año)|N° Datos|Porcentaje|
|---|---|---|
|0.0-0.999|6949|93,30%|
|1.0-1.2099|146|1,96%|
|1.21-1.4099|164|2,20%|
|1.41-1.6099|187|2,51%|
|1.61-1.791|2|0,03%|
|**Total**|**7448**|**100%**|

Fuente: archivo Excel adjunto en **anexo 5**

Figura N° 4. Frecuencias de ocurrencias de tasas de depositación. Ciclo completo de medición de corrientes. Serie Alimento

**5.1.2** **Ciclo Cuadratura**

El resultado de la modelación se presenta en la **Tabla 9** y **Figura 5** . Del total del área de
sedimentación, se tiene lo siguiente:

Tabla 9. Superficie tasa de depositación carbono orgánico de acuerdo con modelación depomod por tasa de depositación durante un

ciclo de cuadratura.

|Tasa depositación (kg C/m/año)|Superficie (m2)|Porcentaje (%)|
|---|---|---|
|1.0 - 1.2|12.051|25.0%|
|1.2 - 1.4|15.463|32.1%|
|1.4 - 1.6|19.787|41.0%|
|1.6 - 1.8|943|1.95%|
|**TOTAL**|**48.244**|**100%**|

Figura N° 5. Dispersión y concentración de carbono. Período cuadratura. Serie Alimento

De acuerdo con los resultados obtenidos en las modelaciones se tiene que las tasas de depositaciones
varían entre 1,0 y 1,736 kgC/m [2] /año (ver serie depositación, **anexo 5** archivos resus), el área de
depositación total es de 48.244m [2], la máxima tasa de depositación de 1,736 kg/m [2] /año, equivalente
a 4,76 grC/m [2] /día representa el 1,95% de la superficie total de la pluma y se deposita íntegramente
dentro del polígono.

La siguiente **tabla 10** y **figura 6** muestra la frecuencia de ocurrencia de las tasas de depositación, en
donde se puede observar el porcentaje de participación de cada tasa de depositación.

Tabla 10. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de cuadratura y serie de alimento

|Tasa Depositación (kgC/m2/año)|N° Datos|Porcentaje|
|---|---|---|
|0.0-0.999|6947|93,27%|
|1.0-1.2099|142|1,91%|
|1.21-1.4099|182|2,44%|
|1.41-1.6099|161|2,16%|
|1.61-1.736|16|0,21%|
|**Total**|**7448**|**100%**|

Fuente: archivo Excel adjunto en **anexo 5**

Figura N° 6. Frecuencias de ocurrencias de tasas de depositación. Corrientes de cuadratura. Serie Alimento

**5.1.3** **Ciclo Sicigia**

El resultado de la modelación se presenta en la **Tabla 11** y **Figura 7** . Del total del área de
sedimentación, se tiene lo siguiente:

Tabla 11. Superficie tasa de depositación carbono orgánico durante un ciclo de sicigia. Serie alimento

|Tasa depositación (kg C/m/año)|Superficie (m2)|Porcentaje (%)|
|---|---|---|
|1.0 - 1.2|13.149|27,8%|
|1.2 - 1.4|15.796|33,4%|
|1.4 - 1.6|18.108|38,3%|
|1.6 - 1.8|225|0,48%|
|**TOTAL**|**47.278**|**100%**|

Figura N° 7. Dispersión y concentración de carbono. Período Sicigia. Serie Alimento

De acuerdo con los resultados obtenidos en las modelaciones se tiene que las tasas de depositaciones
varían entre 1,0 y 1,768 KgC/m [2] /año (ver serie depositación, **anexo 5** archivos resus), el área de
depositación total es de 47.278 m [2], la máxima tasa de depositación de 1,768 kg/m [2] /año, equivalente
a 4,84 grC/m [2] /día representa el 0,08% de la superficie total de la pluma y se deposita íntegramente
dentro del polígono.

La siguiente **tabla 12** y **figura 8** muestra la frecuencia de ocurrencia de las tasas de depositación, en
donde se puede observar el porcentaje de participación de cada tasa de depositación.

Tabla 12. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de sicigia y serie de alimento

|Tasa Depositación (kgC/m2/año)|N° Datos|Porcentaje|
|---|---|---|
|0.0-0.999|6964|93,50%|
|1.0-1.2099|145|1,95%|
|1.21-1.4099|170|2,28%|
|1.41-1.6099|163|2,19%|
|1.61-1.768|6|0,08%|
|**Total**|**7448**|**100%**|

Fuente: archivo Excel adjunto en **anexo 5**

Figura N° 8. Frecuencias de ocurrencias de tasas de depositación. Corrientes de sicigia. Serie Alimento

**5.2** **Alimento de Mayor Diámetro**

**5.2.1** **Ciclo Completo**

El resultado de la modelación se presenta en la **Tabla 13** y **Figura 9** . Del total del área de
sedimentación, se tiene lo siguiente:

Tabla 13. Superficie tasa de depositación carbono orgánico durante un ciclo de 30 días de medición. Alimento mayor diámetro

|Tasa depositación (kg C/m/año)|Superficie (m2)|Porcentaje (%)|
|---|---|---|
|1.0 - 1.2|13.260|27,2%|
|1.2 - 1.4|13.797|28,4%|
|1.4 - 1.6|20.635|42,4%|
|1.6 - 1.8|973|2,00%|
|**TOTAL**|**48.665**|**100%**|

Figura N° 9. Dispersión y concentración de carbono. Ciclo completo mediciones de corrientes. Alimento mayor diámetro

De acuerdo con los resultados obtenidos en las modelaciones se tiene que las tasas de depositaciones
varían entre 1,0 y 1,752 KgC/m [2] /año (ver serie depositación, **anexo 5** archivos resus), el área de
depositación total es de 48.665 m [2], la máxima tasa de depositación de 1,752 kg/m [2] /año, equivalente
a 4,8grC/m [2] /día representa el 0,13% de la superficie total de la pluma y se deposita íntegramente
dentro del polígono.
La siguiente **tabla 14** y **figura 10** muestra la frecuencia de ocurrencia de las tasas de depositación, en
donde se puede observar el porcentaje de participación de cada tasa de depositación.

Tabla 14. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Ciclo Completo de Corrientes y alimento de mayor diámetro.

|Tasa Depositación (kgC/m2/año)|N° Datos|Porcentaje|
|---|---|---|
|0.0-0.9999|6945|93,25%|
|1.0-1.2099|141|1,89%|
|1.21-1.4099|144|1,93%|
|1.41-1.6099|208|2,79%|
|1.61-1.752|10|0,13%|
|**Total**|**7448**|**100%**|

Fuente: archivo Excel adjunto en **anexo 5**

Figura N° 10. Frecuencias de ocurrencias de tasas de depositación. Ciclo Completo de Corrientes. Alimento Mayor Diámetro

**5.2.2** **Ciclo Cuadratura**

El resultado de la modelación se presenta en la **Tabla 15** y **Figura 11** . Del total del área de
sedimentación, se tiene lo siguiente:

Tabla 15. Superficie por tasa de depositación durante un ciclo de cuadratura. Alimento mayor diámetro

|Tasa depositación (kg C/m/año)|Superficie (m2)|Porcentaje (%)|
|---|---|---|
|1.0 - 1.2|10.863|22,5%|
|1.2 - 1.4|15.533|32,2%|
|1.4 - 1.6|19.604|40,6%|
|1.6 - 1.8|2.284|4,7%|
|**TOTAL**|**48.284**|**100%**|

Figura N° 11. Dispersión y concentración de carbono. Período Cuadratura. Alimento mayor diámetro

De acuerdo con los resultados obtenidos en las modelaciones se tiene que las tasas de depositaciones
varían entre 1,0 y 1,745 KgC/m [2] /año (ver serie depositación, **anexo 5** archivos resus), el área de
depositación total es de 48.284m [2], la máxima tasa de depositación de 1,745 kg/m [2] /año, equivalente
a 4,78 **grC/m** **[2]** **/día** representa el 4,7% de la superficie total de la pluma y se deposita íntegramente
dentro del polígono.

La siguiente **tabla 16** y **figura 12** muestra la frecuencia de ocurrencia de las tasas de depositación, en
donde se puede observar el porcentaje de participación de cada tasa de depositación.

Tabla 16. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de Cuadratura y alimento de mayor diámetro.

|Tasa Depositación (kgC/m2/año)|N° Datos|Porcentaje|
|---|---|---|
|0.0-0.999|6938|93,15%|
|1.0-1.2099|141|1,89%|
|1.21-1.4099|170|2,28%|
|1.41-1.6099|171|2,30%|
|1.61-1.745|28|0,38%|
|**Total**|**7448**|**100%**|

Fuente: archivo Excel adjunto en **anexo 5**

Figura N° 12. Frecuencias de ocurrencias de tasas de depositación. Corrientes de Cuadratura. Alimento Mayor Diámetro

**5.2.3** **Ciclo Sicigia**

El resultado de la modelación se presenta en la **Tabla 17** y **Figura 13** . Del total del área de
sedimentación, se tiene lo siguiente:

Tabla 17. Superficie tasa de depositación carbono orgánico durante corrientes de sicigia. Alimento mayor diámetro

|Tasa depositación (kg C/m/año)|Superficie (m2)|Porcentaje (%)|
|---|---|---|
|1.0 - 1.2|12.891|26,8%|
|1.2 - 1.4|14.909|31,0%|
|1.4 - 1.6|19.335|40,2%|
|1.6 - 1.8|907|1,9%|
|**TOTAL**|**48.042**|**100%**|

Figura N° 13. Dispersión y concentración de carbono. Corrientes de sicigia. Alimento mayor diámetro

De acuerdo con los resultados obtenidos en las modelaciones se tiene que las tasas de depositaciones
varían entre 1,0 y 1,748 KgC/m [2] /año (ver serie depositación, **anexo 5** archivos resus), el área de
depositación total es de 48.130m [2], la máxima tasa de depositación de 1,748 kg/m [2] /año, equivalente
a 4,79 grC/m [2] /día representa el 0,16% de la superficie total de la pluma y se deposita íntegramente
dentro del polígono.
La siguiente **tabla 18** y **figura 14** muestra la frecuencia de ocurrencia de las tasas de depositación, en
donde se puede observar el porcentaje de participación de cada tasa de depositación.

Tabla 18. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de sicigia y alimento de mayor diámetro.

|Tasa Depositación (kgC/m2/año)|N° Datos|Porcentaje|
|---|---|---|
|0.0-0.999|6953|93,35%|
|1.0-1.2099|137|1,84%|
|1.21-1.4099|165|2,22%|
|1.41-1.6099|181|2,43%|
|1.61-1.748|12|0,16%|
|**Total**|**7448**|**100%**|

Fuente: archivo Excel adjunto en **anexo 5**

Figura N° 14. Frecuencias de tasas de depositación. Período Sicigia. Alimento mayor diámetro

La siguiente **tabla 19** detalla las máximas tasas de depositación por cada ciclo mareal para ambos
escenarios de tipo de alimento.

Tabla 19. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de sicigia y alimento de mayor diámetro.

|Ciclo de Corrientes|Tasa Máxima depositación (kgC/m2/año)|Col3|
|---|---|---|
|**Ciclo de Corrientes**|**Serie alimento**|**Alimento mayor diámetro**|
|Ciclo Completo|1,791|1,752|
|Cuadratura|1,736|1,745|
|Sicigia|1,768|1,748|

Fuente: Salidas del módulo resus, adjunto en **anexo 5** .

Del resultado de las modelaciones, se puede observar que en todas las modelaciones la disposición
de la pluma es en sentido norte-sur, lo que va de la mano con la disposición de los módulos de cultivo,
sumado además a que al analizar las capas del estudio de corrientes todas ellas, habida consideración
en diferencias en las magnitudes, presentaron un comportamiento relativamente similar en toda la
columna de agua.

**5.3** **Comparación Tasas de Depositación**

Las siguientes figuras comparan las tasas de depositación obtenidas entre serie de alimento y
alimento de mayor diámetro para cada configuración.

Las siguientes figuras muestran gráficamente las tasas de depositación de carbono comparando los
resultados obtenidos utilizando la serie de alimento y el alimento de mayor diámetro, al respecto se
observa que en todos los ciclos de corrientes se observan las mismas tasas de depositación y la
diferencia se encuentra en el porcentaje de participación de estas, con porcentajes de participación
similares con una tendencia a que la mayor tasa de depositación tiene una mayor participación en el
alimento de mayor diámetro. ( **Figuras 15, 16 y 17** ).

Figura N° 15. Frecuencias de tasas de depositación. Período ciclo completo de corrientes.

Figura N° 16. Frecuencias de tasas de depositación. Período cuadratura.

Figura N° 17. Frecuencias de tasas de depositación. Período sicigia.

**6.** **COMENTARIOS FINALES**

- Se realizaron 6 modelaciones, correspondientes a los tres escenarios de corrientes, ciclo
completo, corrientes de cuadratura y corrientes de sicigia, para cada tipo de alimento, “serie
de alimento” hace referencia a la matriz de alimento del proyecto y “alimento de mayor
diámetro” que hace referencia a modelar solo con el alimento de mayor tamaño
suministrado en el centro, que en este caso particular corresponde al pellet de 9mm.

- Respecto de las modelaciones realizadas, todas mostraron tasas de depositación similares;
en todos los casos tanto “serie de alimento” como “alimento de mayor diámetro” presentan
tasas en torno al 1,7 kgC/m [2] /año, y cercanas al 1,8 kgC/m [2] /año; motivo por el cual las escalas
gráficas de todas las figuras muestran una tasa máxima de 1,8 kgC/m [2] /año.

- La máxima tasa de depositación se observó en serie de alimento con ciclo completo de
corrientes con una tasa de 1,791 kgc/m [2] /año y la menor fue para el escenario de cuadratura,
serie de alimento con una tasa de 1,736 kgC/m [2] /año. Sin perjuicio de lo anterior, todas las
tasas estuvieron en torno a esos valores, esto podría atribuirse a que las magnitudes de
corrientes son similares en toda la columna de agua considerada para la modelación, es decir,
entre los 20 a 116m. (ver **anexo 5** )

- Respecto de la superficie de depositación, en todas las modelaciones para serie de alimento
la superficie fue en torno a los 47-48 mil metros cuadrados; en el caso del ciclo completo de
corrientes la superficie es de 47.986m [2] ; 48.244m [2] en el caso de corrientes de cuadratura y
para corrientes de sicigia la superficie es de 47.278m [2] . En tanto para las modelaciones de
alimento de mayor diámetro, las superficies de depositación fluctuaron en torno a los 48 mil
metros cuadrados; en el caso del ciclo completo de corrientes la superficie fue de 48.665m [2],
para corrientes de cuadratura la superficie fue de 48.284m [2], en tanto para corrientes de
sicigia la superficie fue de 48.042m [2] .

- Cabe destacar que no hubo mayores diferencias entre los resultados obtenidos utilizando la
serie de alimento y el alimento de mayor diámetro, los resultados, en términos generales
fueron muy similares tanto en tasa como en superficie y en todos los escenarios modelados
la pluma de sedimentación se deposita íntegramente dentro del polígono solicitado en

concesión.

- Una posible explicación a la similitud de los resultados puede deberse a la homogeneidad de
las magnitudes de corrientes, donde las velocidades promedio de la última capa utilizada
(116m) son similares entre los diferentes ciclos de corrientes.

- De acuerdo a lo anteriormente expuesto, los resultados de las modelaciones muestran que,
en términos de tasa de depositación, superficie de sedimentación permite inferir que el
centro es capaz de soportar de manera sustentable la producción de 5.000 toneladas; más
aún cuando los resultados del modelo representan lo que sería el escenario a máxima
biomasa y con la mayor carga de material particulado, sin embargo, el proceso de engorda
es un proceso paulatino que se inicia con la siembra de peces, lo que podría demorar
alrededor de 2 meses con una muy baja biomasa si se considera el ingreso de peces de una
talla muy pequeña por lo que en definitiva, la máxima biomasa que pretende el proyecto
corresponde a la suma de las cosechas que se realizan al término del ciclo productivo en
donde se extraen aquellos ejemplares mejor dotados acorde a procesos de selección natural
que han alcanzado la talla de cosecha.

**7.** **ANEXOS**

**ANEXO 1**

**Datos crudos Corrientes Eulerianas**

**ANEXO 2**

**Datos crudo batimetría**

**ANEXO 3**

**Plano base**

**Imágenes Modelaciones**

**ANEXO 4**

**Archivos de salida**

**ANEXO 5**

**Planillas Excel archivo Resus. sur**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Modelaciones realizadas para centro Canal Bertrand**

| Escenario | Configuración | Estructuras | Biomasa | Corrientes |
| --- | --- | --- | --- | --- |
| Serie Alimento | 2 módulos | 28 balsas<br>(30x30x20m) | 5.000<br>toneladas | Ciclo<br>completo: 30<br>días |
| Serie Alimento | 2 módulos | 28 balsas<br>(30x30x20m) | 5.000<br>toneladas | Período de<br>cuadratura |
| Serie Alimento | 2 módulos | 28 balsas<br>(30x30x20m) | 5.000<br>toneladas | Período de<br>sicigia |
| Alimento Mayor<br>Diámetro | 2 módulos | 28<br>balsas<br>(30x30x20m) | 5.000<br>toneladas | Ciclo<br>completo: 30<br>días |
| Alimento Mayor<br>Diámetro | 2 módulos | 28<br>balsas<br>(30x30x20m) | 5.000<br>toneladas | Período de<br>cuadratura |
| Alimento Mayor<br>Diámetro | 2 módulos | 28<br>balsas<br>(30x30x20m) | 5.000<br>toneladas | Período de<br>sicigia |

**Tabla 2.: Datos de producción, características de alimento utilizados para el modelo DEPOMOD**

| Variable | Unidades | Configuración |
| --- | --- | --- |
| Producción | Kilos | 5.000.000 |
| Ciclo de cultivo | Días | 549 |
| Balsa jaulas | Número | 28 |
| Dimensiones | Metros | 30x30x20 |
| Peso ingreso | Kilos | 0.15 |
| Peso cosecha | Kilos | 5 |
| Alimento acumulado | Kilos | 5.558.108 |
| Suministro alimento | Kilos/Balsa/día | 361,6 |
| ANC | % | 38 |
| Digestibilidad | % | 908 |
| Humedad alimento | % | 108 |
| Carbono alimento | % | 578 |
| Carbono fecas | % | 338 |

**Tabla 3.: Especificación del alimento utilizado para el modelo DEPOMOD**

| Especificación Alimento | Col2 | Col3 |
| --- | --- | --- |
| Diámetro (um) | Velocidad sedimentación (m/s) | %Mass9 |
| 4000 | 0,082 | 5 |
| 6000 | 0,096 | 20 |
| 9000 | 0,122 | 75 |

**Tabla 4.: Profundidad promedio por configuración.**

| Configuración | Profundidad media<br>zona ubicación módulos (m) |
| --- | --- |
| 2 módulos de 14 balsas: 28 balsas (30x30x20m) | 122 |

**Tabla 5.: Capas de corrientes utilizadas en la modelación**

| Capas | Profundidad (m) | Distancia de la capa al fondo marino<br>(m) |
| --- | --- | --- |
| 10 | 20 | 102 |
| 25 | 50 | 72 |
| 38 | 76 | 46 |
| 48 | 96 | 26 |
| 58 | 116 | 6 |

**Tabla 6.: Capas de corrientes utilizadas en la modelación**

| Período Lunar | No datos | Tiempo de medición<br>(s) | Velocidad media<br>ultima capa (cm/s) | Altura Marea<br>(m) |
| --- | --- | --- | --- | --- |
| Ciclo Completo | 4.579 | 600 | 2.17 | 0,6 |
| Cuadratura | 1.154 | 600 | 1.79 | 0,4 |
| Sicigia | 1.461 | 600 | 2.32 | 0,5 |

**Tabla 7.: Superficie tasa de depositación carbono orgánico durante un ciclo de 30 días de medición. Serie de alimento**

| Tasa depositación (kg C/m/año) | Superficie (m2) | Porcentaje (%) |
| --- | --- | --- |
| 1.0 - 1.2 | 13.237 | 27,6% |
| 1.2 - 1.4 | 15.401 | 32,1% |
| 1.4 - 1.6 | 19.224 | 40,1% |
| 1.6 - 1.8 | 124 | 0,26% |
| **TOTAL** | **47.986** | **100%** |

**Tabla 8.: Frecuencias de ocurrencia tasa de depositación carbono orgánico. Ciclo completo de corrientes y serie de alimento**

| Tasa Depositación (kgC/m2/año) | N° Datos | Porcentaje |
| --- | --- | --- |
| 0.0-0.999 | 6949 | 93,30% |
| 1.0-1.2099 | 146 | 1,96% |
| 1.21-1.4099 | 164 | 2,20% |
| 1.41-1.6099 | 187 | 2,51% |
| 1.61-1.791 | 2 | 0,03% |
| **Total** | **7448** | **100%** |

**Tabla 9.: Superficie tasa de depositación carbono orgánico de acuerdo con modelación depomod por tasa de depositación durante un**

| Tasa depositación (kg C/m/año) | Superficie (m2) | Porcentaje (%) |
| --- | --- | --- |
| 1.0 - 1.2 | 12.051 | 25.0% |
| 1.2 - 1.4 | 15.463 | 32.1% |
| 1.4 - 1.6 | 19.787 | 41.0% |
| 1.6 - 1.8 | 943 | 1.95% |
| **TOTAL** | **48.244** | **100%** |

**Tabla 10.: Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de cuadratura y serie de alimento**

| Tasa Depositación (kgC/m2/año) | N° Datos | Porcentaje |
| --- | --- | --- |
| 0.0-0.999 | 6947 | 93,27% |
| 1.0-1.2099 | 142 | 1,91% |
| 1.21-1.4099 | 182 | 2,44% |
| 1.41-1.6099 | 161 | 2,16% |
| 1.61-1.736 | 16 | 0,21% |
| **Total** | **7448** | **100%** |

**Tabla 11.: Superficie tasa de depositación carbono orgánico durante un ciclo de sicigia. Serie alimento**

| Tasa depositación (kg C/m/año) | Superficie (m2) | Porcentaje (%) |
| --- | --- | --- |
| 1.0 - 1.2 | 13.149 | 27,8% |
| 1.2 - 1.4 | 15.796 | 33,4% |
| 1.4 - 1.6 | 18.108 | 38,3% |
| 1.6 - 1.8 | 225 | 0,48% |
| **TOTAL** | **47.278** | **100%** |

**Tabla 12.: Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de sicigia y serie de alimento**

| Tasa Depositación (kgC/m2/año) | N° Datos | Porcentaje |
| --- | --- | --- |
| 0.0-0.999 | 6964 | 93,50% |
| 1.0-1.2099 | 145 | 1,95% |
| 1.21-1.4099 | 170 | 2,28% |
| 1.41-1.6099 | 163 | 2,19% |
| 1.61-1.768 | 6 | 0,08% |
| **Total** | **7448** | **100%** |

**Tabla 13.: Superficie tasa de depositación carbono orgánico durante un ciclo de 30 días de medición. Alimento mayor diámetro**

| Tasa depositación (kg C/m/año) | Superficie (m2) | Porcentaje (%) |
| --- | --- | --- |
| 1.0 - 1.2 | 13.260 | 27,2% |
| 1.2 - 1.4 | 13.797 | 28,4% |
| 1.4 - 1.6 | 20.635 | 42,4% |
| 1.6 - 1.8 | 973 | 2,00% |
| **TOTAL** | **48.665** | **100%** |

**Tabla 14.: Frecuencias de ocurrencia tasa de depositación carbono orgánico. Ciclo Completo de Corrientes y alimento de mayor diámetro.**

| Tasa Depositación (kgC/m2/año) | N° Datos | Porcentaje |
| --- | --- | --- |
| 0.0-0.9999 | 6945 | 93,25% |
| 1.0-1.2099 | 141 | 1,89% |
| 1.21-1.4099 | 144 | 1,93% |
| 1.41-1.6099 | 208 | 2,79% |
| 1.61-1.752 | 10 | 0,13% |
| **Total** | **7448** | **100%** |

**Tabla 15.: Superficie por tasa de depositación durante un ciclo de cuadratura. Alimento mayor diámetro**

| Tasa depositación (kg C/m/año) | Superficie (m2) | Porcentaje (%) |
| --- | --- | --- |
| 1.0 - 1.2 | 10.863 | 22,5% |
| 1.2 - 1.4 | 15.533 | 32,2% |
| 1.4 - 1.6 | 19.604 | 40,6% |
| 1.6 - 1.8 | 2.284 | 4,7% |
| **TOTAL** | **48.284** | **100%** |

**Tabla 16.: Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de Cuadratura y alimento de mayor diámetro.**

| Tasa Depositación (kgC/m2/año) | N° Datos | Porcentaje |
| --- | --- | --- |
| 0.0-0.999 | 6938 | 93,15% |
| 1.0-1.2099 | 141 | 1,89% |
| 1.21-1.4099 | 170 | 2,28% |
| 1.41-1.6099 | 171 | 2,30% |
| 1.61-1.745 | 28 | 0,38% |
| **Total** | **7448** | **100%** |

**Tabla 17.: Superficie tasa de depositación carbono orgánico durante corrientes de sicigia. Alimento mayor diámetro**

| Tasa depositación (kg C/m/año) | Superficie (m2) | Porcentaje (%) |
| --- | --- | --- |
| 1.0 - 1.2 | 12.891 | 26,8% |
| 1.2 - 1.4 | 14.909 | 31,0% |
| 1.4 - 1.6 | 19.335 | 40,2% |
| 1.6 - 1.8 | 907 | 1,9% |
| **TOTAL** | **48.042** | **100%** |

**Tabla 18.: Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de sicigia y alimento de mayor diámetro.**

| Tasa Depositación (kgC/m2/año) | N° Datos | Porcentaje |
| --- | --- | --- |
| 0.0-0.999 | 6953 | 93,35% |
| 1.0-1.2099 | 137 | 1,84% |
| 1.21-1.4099 | 165 | 2,22% |
| 1.41-1.6099 | 181 | 2,43% |
| 1.61-1.748 | 12 | 0,16% |
| **Total** | **7448** | **100%** |

**Tabla 19.: Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de sicigia y alimento de mayor diámetro.**

| Ciclo de Corrientes | Tasa Máxima depositación (kgC/m2/año) | Col3 |
| --- | --- | --- |
| **Ciclo de Corrientes** | **Serie alimento** | **Alimento mayor diámetro** |
| Ciclo Completo | 1,791 | 1,752 |
| Cuadratura | 1,736 | 1,745 |
| Sicigia | 1,768 | 1,748 |
