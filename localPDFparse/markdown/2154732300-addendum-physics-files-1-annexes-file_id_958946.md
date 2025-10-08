---
title: Sin título
author: pschnettler
date: D:20221014213834-03'00'
language: es
type: report
pages: 27
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME TÉCNICO MODELACIÓN ADENDA No 1 “AMPLIACIÓN DE BIOMASA, CENTRO DE ENGORDA RÍO REÑIHUE, COMUNA DE CHAITÉN, REGIÓN DE LOS LAGOS” GLACIARES DOS S.A.
-->

# INFORME TÉCNICO MODELACIÓN ADENDA No 1 “AMPLIACIÓN DE BIOMASA, CENTRO DE ENGORDA RÍO REÑIHUE, COMUNA DE CHAITÉN, REGIÓN DE LOS LAGOS” GLACIARES DOS S.A.

ELABORADO POR:

BUIN 367 - PUERTO MONTT

+56-65-2752179/+56-65-2714278

[www.ecosistema.cl](http://www.ecosistema.cl/)

[info@ecosistema.cl](mailto:info@ecosistema.cl)

**Puerto Montt, octubre 2022**

**ÍNDICE**

**1.** **ANTECEDENTES GENERALES ................................................................................................................. 4**

**2.** **OBJETIVOS ............................................................................................................................................ 6**

**3.** **METODOLOGÍA ..................................................................................................................................... 7**

**4.** **DATOS DE ENTRADA. ............................................................................................................................ 9**

**5.** **RESULTADOS ...................................................................................................................................... 13**

5.1 C ICLO C OMPLETO DE C ORRIENTES ........................................................................................................... 13

5.2 C ICLO C UADRATURA ............................................................................................................................. 14

5.3 C ICLO S ICIGIA ...................................................................................................................................... 16

**6.** **COMENTARIOS FINALES ...................................................................................................................... 18**

**7.** **ANEXOS .............................................................................................................................................. 19**

**7.1** **ANEXO 1_DATOS CRUDOS BATIMETRIA ......................................................................................... 20**

**7.2** **ANEXO 2_DATOS CRUDOS ADCP .................................................................................................... 21**

**7.3** **ANEXO 3_PLANOS Y FIGURAS ........................................................................................................ 22**

**7.4** **ANEXO 4_ARCHIVOS INPUTS .......................................................................................................... 23**

**7.5** **ANEXO 5_ARCHIVOS SALIDA .......................................................................................................... 24**

**7.6** **ANEXO 6_RESULTADOS .................................................................................................................. 25**

**7.7** **ANEXO 7_FT ALIMENTO ................................................................................................................. 26**

**ÍNDICE DE TABLAS**

Tabla 1. Modelaciones realizadas para centro Reñihue ........................................................................................ 8
Tabla 2. Profundidad promedio por configuración. .............................................................................................. 9
Tabla 3. Capas de corrientes utilizadas en la modelación .................................................................................. 10
Tabla 4. Datos corrientes .................................................................................................................................... 10

Tabla 5. Datos de entrada ................................................................................................................................... 11
Tabla 6. Características del alimento según ficha técnica y certificado ............................................................. 11
Tabla 7. Características del alimento mayor tamaño según ficha técnica y certificado ...................................... 12
Tabla 8. Superficie tasa de depositación carbono orgánico durante un ciclo de 30 días de medición. ............... 13
Tabla 9. Superficie tasa de depositación carbono orgánico durante un ciclo de cuadratura. .............................. 14
Tabla 10. Superficie tasa de depositación carbono orgánico durante un ciclo de sicigia. .................................. 16
Tabla 11. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de sicigia y serie de

alimento ...................................................................................................................................................... 17

**ÍNDICE DE FIGURAS**

Figura N° 1. Ubicación geográfica de la zona de emplazamiento del proyecto. .................................................. 7
Figura N° 2. Ubicación módulo para modelación. ............................................................................................... 9
Figura N° 3. Dispersión y concentración de carbono. Ciclo completo de medición de corrientes. .................... 13
Figura N° 4. Frecuencias de ocurrencias de tasas de depositación. Ciclo Completo de Corrientes. .................. 14
Figura N° 5. Dispersión y concentración de carbono. Período cuadratura. ........................................................ 15
Figura N° 6. Frecuencias de ocurrencias de tasas de depositación. Corrientes de cuadratura. ........................... 15
Figura N° 7. Dispersión y concentración de carbono. Período Sicigia. .............................................................. 16
Figura N° 8. Frecuencias de ocurrencias de tasas de depositación. Corrientes de sicigia. ................................. 17

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

Actualmente, en Chile aún se sigue modelando con el software DEPOMOD, desarrollado por Cromey
_et al_, (2002) que permite estimar a escala local la tasa de depositación de biosólidos producto del
porcentaje de alimento no consumido y fecas; para ello considera variables productivas, tales como
cantidad de alimento vertido en un ciclo de producción, características del alimento, datos
oceanográficos del sector y con ello poder simular el flujo y cantidad de desechos desde las balsas de

cultivo al fondo marino.

Este modelo está estructurado en cuatro módulos que se acoplan para estimar las concentraciones
de Carbono Orgánico Total (COT) en el fondo. Estos son: a) generación de la grilla (GRIDGEN), b)
trayectoria de partículas (PARTRACK) y c) re-suspensión y módulo de respuesta bentónica (RESUS).
El cuarto módulo (BENTHIC) conecta los tres primeros, cuantificando la dispersión de los residuos
liberados por los centros de cultivo para la estimación de la concentración de carbono orgánico total
(COT) en el bentos. (IFOP, 2013 [6] ).

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

6 Instituto fomento Pesquero IFOP. Informe final Experiencia Internacional en el uso de DEPOMOD para la Acuicultura.

Se presenta nuevamente el informe de modelación, dado que dentro del marco de evaluación de la
DIA en el Informe Consolidado de Solicitud de Aclaraciones, Rectificaciones y/o Ampliaciones a la
Declaración de Impacto Ambiental del Proyecto se realizan las siguientes observaciones:

_“1.21 En la DIA en el punto 3 metodología se indica que, (...) “En términos generales los datos de entrada_
_utilizados en la presente modelación son aquellos por defecto del software DEPOMOD V2 en cuanto a porcentaje_
_de humedad, ANC, en tanto la digestibilidad utilizada corresponde a la entregada por la empresa Salmofood_
_(se adjunta certificado en anexo xxx) (...)” Al respecto, se solicita rectificar esta información y adjuntar ficha_
_técnica de la serie de alimentos con los que se alimentará al cultivo de salmones donde indica, porcentaje de_
_nutrientes, % de digestibilidad, de humedad, diámetro del alimento y las especificaciones en detalle todos los_
_alimentos que se consideraron en la modelación de corrientes en la serie de alimentos”._

_“1.29 En relación al documento “Anexo_13_informe_modelacion”, se solicita al titular:_

 - _Indicar en base al análisis de las corrientes, cual fue el criterio de selección para las capas que_
_serán utilizadas en la Modelación Depomod._

 - _Dado que la modificación del proyecto técnico indica como especie de cultivo Salmónidos, lo cual hace_
_referencia que se cultivaran más de una especie con diferentes ciclos productivos, se solicita realizar_
_modelaciones que consideren el ciclo productivo más largo y el ciclo productivo más corto según la_
_especie a cultivar, indicando la biomasa total de producción en toneladas, el ciclo productivo en días,_
_y según especie_

 - _Para la nueva modelación, se debe considerar, el tamaño máximo de alimento suministrado e_
_incorporar todos los archivos utilizados en la modelación, los archivos utilizados como inputs y los_
_generados después de su ejecución.”_

Por tanto, y de acuerdo a lo observado, el titular aclara y declara que se corrige la producción máxima
esperada para el centro de cultivo, para una biomasa de sólo 4.000 toneladas de salmónidos,
correspondiente a un único ciclo de cultivo de 13 meses de duración e independiente de la especie
de que se trate, por lo que se presenta una nueva modelación considerando lo anteriormente
indicado sólo para el alimento de mayor diámetro, dado que es el escenario más desfavorable y
porque fue solicitada en el adenda (observación 4.5.2.).

**2.** **OBJETIVOS**

a. Establecer la tasa de depositación y dispersión de Carbono generado anualmente por el

proyecto.
b. Determinar el área de depositación de Carbono.

**3.** **METODOLOGÍA**

Se realizan las modelaciones de los distintos escenarios utilizando el modelo DEPOMOD V2 sin activar

el modo de resuspensión consideración que fue acordada en el taller organizado por el Servicio de
Evaluación Ambiental de la Región de Magallanes y Antártica Chilena en noviembre del año 2019.

Se realizaron modelaciones en tres escenarios de corrientes, ciclo completo con mediciones de 30
días, corrientes de sicigia y corrientes de cuadratura un solo ciclo de cultivo independiente de la
especie a cultivar:

a) Ciclo de cultivo: producción de 4.000 ton considerando un módulo de cultivo de 28 balsas de

40x40x20m.

La solicitud de concesión se ubica en estero Reñihue, desembocadura río Reñihue, comuna de
Chaitén, región de Los Lagos. ( **Figura 1** ).

Figura N° 1. Ubicación geográfica de la zona de emplazamiento del proyecto.

Tal como ya se indicó, se realizaron 3 modelaciones, para la máxima biomasa de 4.000 ton (ciclo
largo), en período de cuadratura, sicigia y ciclo completo de corrientes utilizando el alimento de
mayor diámetro.

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

El estudio de corrientes utilizado y el perfil batimétrico del área solicitada fueron levantados por la
empresa SELK’ y cumplen con lo dispuesto por la Res. No 3612/2009 y sus modificaciones.
La siguiente **tabla 1** muestra el detalle de las modelaciones realizadas para ambos ciclos de cultivo.

Tabla 1. Modelaciones realizadas para centro Reñihue

|Escenario|Configuración|Estructuras|Biomasa|Corrientes|
|---|---|---|---|---|
|Alimento Mayor<br>Diámetro|1 módulo|28 balsas (40x40x20m)|4.000 toneladas|Ciclo completo: 30 días|
|Alimento Mayor<br>Diámetro|1 módulo|28 balsas (40x40x20m)|4.000 toneladas|Período de cuadratura|
|Alimento Mayor<br>Diámetro|1 módulo|28 balsas (40x40x20m)|4.000 toneladas|Período de sicigia|

**4.** **DATOS DE ENTRADA.**

A continuación se detallan los datos de entrada a utilizar en el modelo.

4.1 Módulo de cultivo

La siguiente figura muestra la posición del módulo de cultivo para las modelaciones realizadas.

Figura N° 2. Ubicación módulo para modelación.

4.2 Datos Oceanográficos

4.2.1 Profundidad media del sector

La **Tabla 2** muestra la profundidad promedio de la zona de emplazamiento de cada módulo de cultivo.

Tabla 2. Profundidad promedio por configuración.

|Configuración|Profundidad media<br>zona ubicación módulos (m)|
|---|---|
|28 balsas (40x40x20m)|112|

4.2.2 Selección de capas de corrientes

Se seleccionaron 5 capas de magnitudes y dirección de corrientes, el criterio de selección de las 5
capas de corrientes utilizadas en la modelación Depomod parte en primer término a partir de la capa
correspondiente a la profundidad de la red pecera, a partir de la cual comienza o se estima que
comienza el proceso de depositación de alimento no consumido y fecas de los peces, atendiendo a
que por lo general se estima que su capa natatoria está en torno a los 15 metros de profundidad.

A partir de esta celda, y teniendo presente por una parte intentar dividir la columna de agua en
intervalos lo más regular posible y por la otra seleccionar celdas que en general muestren una
condición asociada a los menores valores de magnitud para no subestimar la depositación, por lo que
la segunda capa seleccionada corresponde a la celda 21 correspondiente a 42 metros de profundidad,
a partir de lo cual la columna de agua comienza a decrecer en valores promedio y máximos.

Según lo antes indicado, a partir de los 40 metros aproximadamente y hasta los 110 metros, los
valores medios y máximos comienzan a decrecer por lo que se dividió la columna restante en 2 celdas
separadas cada 24 metros aproximadamente (capa 33 correspondiente a 66 metros y capa 45
correspondiente a 90 metros), cada una de las cuales con valores medios y máximos más bajos que
la anterior hasta la selección de la última celda correspondiente a los 110 metros de profundidad y
que corresponde a la celda más cercana al fondo.

La **Tabla 3** muestra las capas de corrientes utilizadas en la modelación. Para mayor información
revisar estudio de corrientes adjunto en el anexo 13 del adenda. En tanto la **Tabla 4** muestra el detalle
de velocidad, cantidad de datos, tiempos de medición y altura de marea para los períodos de ciclo
completo de mediciones de corrientes, ciclo cuadratura y sicigia.

Tabla 3. Capas de corrientes utilizadas en la modelación

|Capas|Profundidad (m)|Distancia de la capa al fondo marino (m)|
|---|---|---|
|10|20|92|
|21|42|70|
|33|66|46|
|45|90|22|
|55|110|2|

Tabla 4. Datos corrientes

|Período Lunar|No datos|Tiempo de medición<br>(s)|Velocidad media<br>ultima capa (cm/s)|
|---|---|---|---|
|Ciclo Completo|4.343|600|3,97|
|Cuadratura|1.152|600|4,09|
|Sicigia|1.264|600|3,67|

4.3 Datos de entrada Productivos

4.3.1 Ciclo Largo

La siguiente **Tabla 5** detalla los datos de entrada utilizados para la modelación de ciclo largo.

Tabla 5. Datos de entrada

|Ítem|Dato|Unidades|Fuente|
|---|---|---|---|
|Biomasa|4.000.000|Kilos|Titular|
|Ciclo|395|Días|Titular (13 meses)|
|Balsas|28|Número|Titular|
|Dimensiones|40*40*20|Metros|Titular|
|**Alimento**|**364**|**Kilos/balsa/día**|**Titular**|
|Humedad|10|%|Ficha técnica|
|ANC|2|%|Micro raciones|
|**Digestibilidad**|**86.8 = 87**|**% **|**Ficha técnica**|
|Peso inicial|0,15|Kilos|Titular|
|Peso final|4,0|Kilos|Titular|
|FCR|1,05||Titular|

La siguiente **Tabla 6** detalla las características del alimento a utilizar para el centro Reñihue según
ficha técnica adjunta en **anexo 6** .

Tabla 6. Características del alimento según ficha técnica y certificado

|CARACTERÍSTICAS ALIMENTO|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Tipo alimento**|**Tamaño**|**% **<br>**Digestibilidad**|**% **<br>**Humedad**|**Velocidad Sedimentación**<br>**(cm/s)**|**Porcentaje uso (%)**|
|**WEL 100**|**3000**|85,4|10|7,8|0,03|
|**WEL 250**|**4000**|85,9|10|7,8|0,1|
|**XG 250**|**4000**|85,9|10|7,8|0,18|
|**XG 500**|**6000**|86,7|10|10|0,18|
|**XG 1000**|**9000**|86,8|10|10,6|0,51|

De acuerdo a los datos de la tabla anterior, se aclara que el porcentaje de uso del alimento en el ciclo
de cultivo fue entregado por el Titular; en tanto la digestibilidad y las velocidades de hundimiento
fue entregado por el proveedor del alimento (ver certificado en **anexo 6** ), finalmente el porcentaje
de humedad fue entregado en la ficha técnica ( **Anexo 6** ).

La siguiente **tabla 7** detalla la característica del alimento de mayor tamaño.

Tabla 7. Características del alimento mayor tamaño según ficha técnica y certificado

|CARACTERISTICAS ALIMENTO|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Tipo alimento**|**Tamaño**|**% **<br>**Digestibilidad**|**% **<br>**Humedad**|**Velocidad Sedimentación**<br>**(cm/s)**|**Porcentaje uso**<br>**(%)**|
|**XG 1000**|**9000**|86,8|10|10,6|100|

**Coeficientes de dispersión:**
Se utilizan los dados por defecto por el software DEPOMOD:
Dispersión horizontal (x): 0.1 m [2] s [-1]
Dispersión vertical (y): 0.1 m [2] s [-1]
Dirección vertical (z): 0.01 m [2] s [-1 ]

**Modo trayectoria de partículas:**
Número de partículas: 10 (por defecto entregado por el software DEPOMOD)
Exactitud de la evaluación de la trayectoria: Alto (60 s), dado por defecto por el Software DEPOMOD.

**Datos de entrada oceanográficos:**

1. **Matriz batimétrica**, datos crudos presentados en CPS, planilla Excel con coordenadas UTM y

profundidades corregidas al NRS. Realizado por SELK’

2. **Profundidad media del sector de emplazamiento de los módulos de cultivo** : **112m** de

acuerdo a resultados de la batimetría.

3. **Plano base**, posición de los módulos propuesta por el Titular

**5.** **RESULTADOS**

A continuación, se presentan los resultados de las modelaciones realizadas para los tres escenarios,
el primero utilizando toda la batería de datos de corrientes “Ciclo Completo”, es decir, se utilizaron
todos los datos colectados durante los 30 días de medición, el segundo utilizando las corrientes en
período de cuadratura y el tercero en período de sicigia.

En **anexo 4** se adjuntan las salidas del software y en tanto en **anexo 5** se adjuntan planillas Excel con
el resultado de las tasas de depositación de carbono (archivo.sur) y **Anexo 6**, certificado de
Salmofood y ficha técnica de alimento

Dado que todos los resultados dieron tasas cercanas a los 1,8kgC/m2/año, las figuras de depositación
muestran la misma escala, sin embargo, las diferencias en las tasas máximas se detallarán en la **tabla**
**19** y en **anexo 5** antes indicado.

**5.1** **Ciclo Completo de Corrientes**

El resultado de la modelación se presenta en la **Tabla 8** y **Figura 3** . Del total del área de
sedimentación, se tiene lo siguiente:

Tabla 8. Superficie tasa de depositación carbono orgánico durante un ciclo de 30 días de medición.

|Tasa depositación (grC/m/día)|Superficie (m2)|Porcentaje (%)|
|---|---|---|
|1.0 -2.0|48.731|38,72%|
|2.0 - 3.0|29.298|23,28%|
|3.0 - 4.0|29.665|23,57%|
|4.0 - 4.7|18.151|14,42%|
|**TOTAL**|**125.845**|**100%**|

Figura N° 3. Dispersión y concentración de carbono. Ciclo completo de medición de corrientes.

De acuerdo con los resultados obtenidos en las modelaciones se tiene que las tasas de depositaciones
varían entre 1,0 y 4,7 grC/m [2] /día (ver serie depositación, **anexo 5** archivos resus), el área de
depositación total es de 125.845 m [2], la máxima tasa de depositación de 4,7grC/m [2] /día se deposita
íntegramente dentro del polígono. La siguiente **Figura 4** muestra la frecuencia de ocurrencia de las
tasas de depositación, en donde se puede observar el porcentaje de participación de cada tasa de
depositación.

Figura N° 4. Frecuencias de ocurrencias de tasas de depositación. Ciclo Completo de Corrientes.

**5.2** **Ciclo Cuadratura**

El resultado de la modelación se presenta en la **Tabla 9** y **Figura 5** . Del total del área de
sedimentación, se tiene lo siguiente:

Tabla 9. Superficie tasa de depositación carbono orgánico durante un ciclo de cuadratura.

|Tasa depositación (kg C/m/año)|Superficie (m2)|Porcentaje (%)|
|---|---|---|
|1.0 -2.0|51.030|40,21%|
|2.0 - 3.0|29.748|23,44%|
|3.0 - 4.0|30.905|24,35%|
|4.0 - 4.6|15.213|11,99%|
|**TOTAL**|**126.896**|**100%**|

Figura N° 5. Dispersión y concentración de carbono. Período cuadratura.

De acuerdo con los resultados obtenidos en las modelaciones se tiene que las tasas de depositaciones
varían entre 1,0 y 4,6 gC/m [2] /día (ver serie depositación, **anexo 5** archivos resus), el área de
depositación total es de 126.896m [2], la máxima tasa de depositación de 4,6 g/m [2] /día se deposita
íntegramente dentro del polígono. La siguiente **Figura 6** muestra la frecuencia de ocurrencia de las
tasas de depositación.

Figura N° 6. Frecuencias de ocurrencias de tasas de depositación. Corrientes de cuadratura.

**5.3** **Ciclo Sicigia**

El resultado de la modelación se presenta en la **Tabla 10** y **Figura 7** . Del total del área de
sedimentación, se tiene lo siguiente:

Tabla 10. Superficie tasa de depositación carbono orgánico durante un ciclo de sicigia.

|Tasa depositación (g C/m2/día)|Superficie (m2)|Porcentaje (%)|
|---|---|---|
|1.0 -2.0|45.312|36,88%|
|2.0 - 3.0|26.507|21,57%|
|3.0 - 4.0|24.901|20,27%|
|4.0 - 5.0|26.133|21,27%|
|5.0 - 5.06|7|0,01%|
|**TOTAL**|**122.860**|**100%**|

Figura N° 7. Dispersión y concentración de carbono. Período Sicigia.

De acuerdo con los resultados obtenidos en las modelaciones se tiene que las tasas de depositaciones
varían entre 1,0 y 5,06 gC/m [2] /día (ver serie depositación, **anexo 5** archivos resus), el área de
depositación total es de 118.936 m [2], la máxima tasa de depositación de 5,0 a 5,06 grC/m [2] /día
representa el 0,01% de la superficie total de la pluma y se deposita íntegramente dentro del polígono.
( **Figura 7** ). La **Figura 8** muestra la frecuencia de ocurrencia de las tasas de depositación

Figura N° 8. Frecuencias de ocurrencias de tasas de depositación. Corrientes de sicigia.

La siguiente **Tabla 11** muestra la frecuencia de ocurrencia de las tasas de depositación, en donde se
puede observar el porcentaje de participación de cada tasa de depositación, tomando como punto
de inflexión la tasa de 5,0 gC/m [2] /día.

Tabla 11. Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de sicigia y serie de alimento

|Tasa Depositación (gC/m2/día)|N° Datos|Porcentaje|
|---|---|---|
|0 - 5,0|8.721|99,99|
|5,0 - 5,06|1|0,01|
|**Total**|**8.722**|**100%**|

Fuente: archivo Excel adjunto en **anexo 5**

**6.** **COMENTARIOS FINALES**

- El centro de cultivo Reñihue presenta un solo ciclo de cultivo, independiente de la especie a
cultivar, el ciclo es de 13 meses para una biomasa de 4000 toneladas. Se realizaron 3
modelaciones, correspondientes a los tres escenarios de corrientes, ciclo completo, corrientes
de cuadratura y corrientes de sicigia, para el “alimento de mayor diámetro” que hace referencia
a modelar solo con el alimento de mayor tamaño suministrado en el centro.

- Se consideran 5 tipos de alimento, siendo el de mayor diámetro el correspondiente a pellet de
9mm, que de acuerdo a certificados y ficha técnica tiene una humedad de 10%, digestibilidad
de 86,8% y velocidad de hundimiento de 10,6cm/s.

- Los resultados de las modelaciones indican que para el escenario de ciclo completo de corrientes
presentó una tasa máxima de depositación de 4,7 grC/m [2] /día; para el escenario de cuadratura
la tasa mayor fue de 4,6 grC/m [2] /día; en tanto, para ciclo de Sicigia la tasa máxima es de
5,06grC/m [2] /día, si bien para esta fase el resultado se encuentra por sobre los 5 gramos, en
estricto rigor del total de datos obtenidos en la matriz de depositación solo 1 dato está por sobre
el límite, es decir, 0,01%; por tanto, se infiere que estas tasas no generan efectos adversos
significativos, considerando además la profundidad del sector y las magnitudes de corrientes
que reflejan una condición de mediana energía, hecho que finalmente se corrobora con los
resultados de las INFAs, que en el tiempo han sido todas aeróbicas.

- Respecto de la superficie de depositación, en todas las modelaciones las superficies estuvieron
por sobre los 120 mil metros cuadrados. La menor superficie fue para corrientes de sicigia con
122.860m [2], seguido por el ciclo de 30 días de corrientes con una superficie de 125.845m [2] y la
mayor corresponde a la modelación de corrientes de cuadratura con 126.896 m [2] .

- Si bien, la mayor superficie se obtuvo en cuadratura, contrario a lo que teóricamente se pudiese
esperar, lo cierto es que en cuadratura se tiene la mayor velocidad media de la última capa, lo
que podría en parte explicar el resultado. Sin perjuicio de lo anterior, las superficies son similares
y las diferencias no son significativas.

- De acuerdo a lo anteriormente expuesto, los resultados de las modelaciones muestran que, en
términos de tasa de depositación, superficie de sedimentación permite inferir que el centro es
capaz de soportar de manera sustentable la producción de 4.000 toneladas; más aún cuando los
resultados del modelo representan lo que sería el escenario a máxima biomasa y con la mayor
carga de material particulado, sin embargo, el proceso de engorda es un proceso paulatino que
se inicia con la siembra de peces, lo que podría demorar alrededor de 2 meses con una muy baja
biomasa si se considera el ingreso de peces de una talla muy pequeña por lo que en definitiva,
la máxima biomasa que pretende el proyecto corresponde a la suma de las cosechas que se
realizan al término del ciclo productivo en donde se extraen aquellos ejemplares mejor dotados
acorde a procesos de selección natural que han alcanzado la talla de cosecha.

**7.** **ANEXOS**

**7.1** **ANEXO 1_DATOS CRUDOS BATIMETRIA**

**7.2** **ANEXO 2_DATOS CRUDOS ADCP**

**7.3** **ANEXO 3_PLANOS Y FIGURAS**

**7.4** **ANEXO 4_ARCHIVOS INPUTS**

**7.5** **ANEXO 5_ARCHIVOS SALIDA**

**7.6** **ANEXO 6_RESULTADOS**

**7.7** **ANEXO 7_FT ALIMENTO**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Modelaciones realizadas para centro Reñihue**

| Escenario | Configuración | Estructuras | Biomasa | Corrientes |
| --- | --- | --- | --- | --- |
| Alimento Mayor<br>Diámetro | 1 módulo | 28 balsas (40x40x20m) | 4.000 toneladas | Ciclo completo: 30 días |
| Alimento Mayor<br>Diámetro | 1 módulo | 28 balsas (40x40x20m) | 4.000 toneladas | Período de cuadratura |
| Alimento Mayor<br>Diámetro | 1 módulo | 28 balsas (40x40x20m) | 4.000 toneladas | Período de sicigia |

**Tabla 2.: Profundidad promedio por configuración.**

| Configuración | Profundidad media<br>zona ubicación módulos (m) |
| --- | --- |
| 28 balsas (40x40x20m) | 112 |

**Tabla 3.: Capas de corrientes utilizadas en la modelación**

| Capas | Profundidad (m) | Distancia de la capa al fondo marino (m) |
| --- | --- | --- |
| 10 | 20 | 92 |
| 21 | 42 | 70 |
| 33 | 66 | 46 |
| 45 | 90 | 22 |
| 55 | 110 | 2 |

**Tabla 4.: Datos corrientes**

| Período Lunar | No datos | Tiempo de medición<br>(s) | Velocidad media<br>ultima capa (cm/s) |
| --- | --- | --- | --- |
| Ciclo Completo | 4.343 | 600 | 3,97 |
| Cuadratura | 1.152 | 600 | 4,09 |
| Sicigia | 1.264 | 600 | 3,67 |

**Tabla 5.: Datos de entrada**

| Ítem | Dato | Unidades | Fuente |
| --- | --- | --- | --- |
| Biomasa | 4.000.000 | Kilos | Titular |
| Ciclo | 395 | Días | Titular (13 meses) |
| Balsas | 28 | Número | Titular |
| Dimensiones | 40*40*20 | Metros | Titular |
| **Alimento** | **364** | **Kilos/balsa/día** | **Titular** |
| Humedad | 10 | % | Ficha técnica |
| ANC | 2 | % | Micro raciones |
| **Digestibilidad** | **86.8 = 87** | **% ** | **Ficha técnica** |
| Peso inicial | 0,15 | Kilos | Titular |
| Peso final | 4,0 | Kilos | Titular |
| FCR | 1,05 |  | Titular |

**Tabla 6.: Características del alimento según ficha técnica y certificado**

| CARACTERÍSTICAS ALIMENTO | Col2 | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Tipo alimento** | **Tamaño** | **% **<br>**Digestibilidad** | **% **<br>**Humedad** | **Velocidad Sedimentación**<br>**(cm/s)** | **Porcentaje uso (%)** |
| **WEL 100** | **3000** | 85,4 | 10 | 7,8 | 0,03 |
| **WEL 250** | **4000** | 85,9 | 10 | 7,8 | 0,1 |
| **XG 250** | **4000** | 85,9 | 10 | 7,8 | 0,18 |
| **XG 500** | **6000** | 86,7 | 10 | 10 | 0,18 |
| **XG 1000** | **9000** | 86,8 | 10 | 10,6 | 0,51 |

**Tabla 7.: Características del alimento mayor tamaño según ficha técnica y certificado**

| CARACTERISTICAS ALIMENTO | Col2 | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Tipo alimento** | **Tamaño** | **% **<br>**Digestibilidad** | **% **<br>**Humedad** | **Velocidad Sedimentación**<br>**(cm/s)** | **Porcentaje uso**<br>**(%)** |
| **XG 1000** | **9000** | 86,8 | 10 | 10,6 | 100 |

**Tabla 8.: Superficie tasa de depositación carbono orgánico durante un ciclo de 30 días de medición.**

| Tasa depositación (grC/m/día) | Superficie (m2) | Porcentaje (%) |
| --- | --- | --- |
| 1.0 -2.0 | 48.731 | 38,72% |
| 2.0 - 3.0 | 29.298 | 23,28% |
| 3.0 - 4.0 | 29.665 | 23,57% |
| 4.0 - 4.7 | 18.151 | 14,42% |
| **TOTAL** | **125.845** | **100%** |

**Tabla 9.: Superficie tasa de depositación carbono orgánico durante un ciclo de cuadratura.**

| Tasa depositación (kg C/m/año) | Superficie (m2) | Porcentaje (%) |
| --- | --- | --- |
| 1.0 -2.0 | 51.030 | 40,21% |
| 2.0 - 3.0 | 29.748 | 23,44% |
| 3.0 - 4.0 | 30.905 | 24,35% |
| 4.0 - 4.6 | 15.213 | 11,99% |
| **TOTAL** | **126.896** | **100%** |

**Tabla 10.: Superficie tasa de depositación carbono orgánico durante un ciclo de sicigia.**

| Tasa depositación (g C/m2/día) | Superficie (m2) | Porcentaje (%) |
| --- | --- | --- |
| 1.0 -2.0 | 45.312 | 36,88% |
| 2.0 - 3.0 | 26.507 | 21,57% |
| 3.0 - 4.0 | 24.901 | 20,27% |
| 4.0 - 5.0 | 26.133 | 21,27% |
| 5.0 - 5.06 | 7 | 0,01% |
| **TOTAL** | **122.860** | **100%** |

**Tabla 11.: Frecuencias de ocurrencia tasa de depositación carbono orgánico. Corrientes de sicigia y serie de alimento**

| Tasa Depositación (gC/m2/día) | N° Datos | Porcentaje |
| --- | --- | --- |
| 0 - 5,0 | 8.721 | 99,99 |
| 5,0 - 5,06 | 1 | 0,01 |
| **Total** | **8.722** | **100%** |
