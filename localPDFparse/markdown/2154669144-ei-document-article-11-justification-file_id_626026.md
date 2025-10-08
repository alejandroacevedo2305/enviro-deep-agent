---
title: F0101S23
author: wood
date: D:20211117115909-03'00'
language: es
type: report
pages: 34
has_toc: True
has_tables: True
extraction_quality: high
---

**DECLARACIÓN DE IMPACTO AMBIENTAL**

**“AJUSTES CONSTRUCTIVOS A INSTALACIONES DE RELAVES**

**ESPESADOS”**

**CAPÍTULO 2**

**ANEXO 2-3 MODELACIÓN EMISIONES ATMOSFÉRICAS**

**Noviembre de 2021**

Informe de modelación de dispersión

_"Ajustes constructivos a Instalaciones de Relaves Espesados"_

noviembre de 2021

preparado para:

especialistas en meteorología y calidad del aire

Contenidos

1 Introducción 2

2 Metodología 3

2.1 Sistema de modelación WRF - CALPUFF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3

2.2 Resumen de emisiones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

3 Resultados 8

3.1 Aportes del Proyecto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

3.2 Comparación con la norma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

3.3 Isolíneas de concentración . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12

3.4 Análisis de Incertidumbre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31

4 Conclusiones 32

1 INTRODUCCIÓN

1 Introducción

En este documento se presentan de los resultados obtenidos al modelar la dispersión atmosférica de las con

centraciones de MP10, MP2 _,_ 5, gases y tasa de depositación de MPS para el proyecto "Ajustes constructivos

a Instalaciones de Relaves Espesados” (en adelante el Proyecto) de CODELCO División Chuquicamata que se

desarrolla en la Comuna de Calama en la Región de Antofagasta, Chile.

Las obras e instalaciones asociadas al Proyecto, se localizan al interior de la División Chuquicamata y fueron

sometidas originalmente al SEIA mediante el Estudio de Impacto Ambiental (EIA) del Proyecto RT Sulfuros, cuyo

Titular es Codelco División Radomiro Tomic, aprobado ambientalmente mediante Resolución Exenta N [o] 0022 del

20 de enero de 2016 de la Comisión de Evaluación Ambiental de la Región de Antofagasta, en adelante RCA

N [o] 0022/2016. El alcance del Proyecto RT Sulfuros contemplaba, entre otras obras, una Planta de Espesadores

de Relaves de Alta Densidad (PEAD) en el sector de relaves espesados del tranque Talabre, la cual permitiría el

funcionamiento del tranque con tecnología de relaves espesados, para todos los usuarios de la Corporación que

conforman el denominado Distrito Norte, correspondientes a la División Chuquicamata (DCH), División Ministro

Hales (DMH), y División Radomiro Tomic (DRT), logrando una depositación nominal de hasta 421 mil toneladas

por día (ktpd).

Actualmente, basado en la capacidad disponible de almacenamiento de relave convencional de la VIII y IX Etapa

del tranque Talabre, en la tasa de procesamiento de mineral actualmente proyectado en el Plan de Negocios de

Codelco (421 ktpd), en las mejores prácticas recogidas en el mercado y la industria en cuanto al espesamiento

de relaves y en materia de seguridad de las obras, es que surge la necesidad de incorporar adecuaciones

constructivas a las obras que formaron parte del área de la planta relaves espesados e infraestructura anexas,

aprobadas en el Proyecto RT Sulfuros.

Con el objetivo de dar cumplimiento a los requerimientos del Sistema de Evaluación de Impacto Ambiental

(SEIA), se presentan en este documento los aportes a las concentraciones obtenidos en la modelación de dis

persión atmosférica de MP10, MP2,5, gases y tasa de depositación de MPS para el presente Proyecto en los

receptores con representatividad poblacional de la comuna de Calama.

La estructura del informe tiene el siguiente orden: en el capítulo 2 se presenta la metodología utilizada para

la modelación de dispersión; en el capítulo 3 se presentan los aportes a las concentraciones de los distintos

contaminantes que son generadas por el Proyecto; finalmente, en el capítulo 4, se presentan las conclusiones.

2

2 METODOLOGÍA

2 Metodología

2.1 Sistema de modelación WRF - CALPUFF

La simulación de las concentraciones de material particulado asociadas al Proyecto, fueron modeladas según

requerimiento de la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA” del Servicio de Evaluación

Ambiental (SEA), mediante la aplicación del sistema de modelación atmosférica “WRF - CALPUFF” definido

por la _Environmental Protection Agency_ (EPA) como sistema de referencia para simular la dispersión de con

taminantes provenientes de complejos industriales ubicados en terreno complejo.

Por una parte, _Weather Research and Forecasting Model_ (WRF) es un modelo de pronóstico meteorológico que

simula diversas variables atmosféricas en un dominio de modelación grillado y tridimensional. Por otra parte,

CALPUFF es un modelo que trata las emisiones como “puffs” las que se van desplazando a través de un campo

meteorológico tridimensional (proporcionado por el modelo WRF). Este sistema, tiene como objetivo modelar

el transporte y dispersión de contaminantes emitidos por las fuentes emisoras de un proyecto y las salidas

contienen concentraciones y/o tasas de depositación.

Tal como se mencionó anteriormente, la meteorología utilizada en la modelación se obtiene del modelo meteo

rológico WRF que será utilizada como entrada para el modelo de dispersión CALPUFF. Dicha información es

referente al entorno del Proyecto y corresponde al periodo comprendido entre el 1 de enero y el 31 de diciembre

del año 2020. Se utiliza este año ya que la modelación meteorológica de este periodo representa muy bien el

clima de la zona evaluada.

El Proyecto cuenta con una fase, la cual corresponde a Construcción. Sin embargo, esta, durante sus obras,

requiere de modificaciones a un proyecto anterior, que fue aprobado ambientalmente en la RCA N [o] 0022/2016,

ya que se trata de una adecuación constructiva. Debido a lo anterior, los aportes a las concentraciones de la

Fase de Construcción del Proyecto deben ser evaluados en términos de la diferencia de los resultados obtenidos

en los escenarios de Construcción Futura (el Proyecto) y Construcción Actual o Caso Base (proyecto aprobado

en la RCA N [o] 0022/2016). Para obtener esta diferencia, se obtienen los datos (grilla y discretos) promedio y

percentil correspondientes a cada contaminante y a cada escenario. Luego, se hace la diferencia de los resul

tados (Construcción Futura menos Construcción Actual) para cada contaminante y estadístico evaluado en el

Proyecto. En el caso del Escenario de Construcción Futura, se modela el año 2025 que es el año que constituye

el peor escenario en términos de las emisiones durante esta etapa del Proyecto y para el caso del Escenario

de Construcción Actual, se modela el año 2023 debido a la misma razón anterior.

El área de modelación corresponde a una grilla de 62 x 62 km, con un espaciamiento de 1 km, en cuyo interior

se encuentra ubicado el sitio de emplazamiento del Proyecto y puntos de interés. La Figuras 1 y 2 muestran el

área de estudio, los receptores en que se evaluarán las concentraciones y la ubicación de las fuentes de emisión

asociadas al Proyecto.

3

2.1 Sistema de modelación WRF - CALPUFF 2 METODOLOGÍA

Figura 1. Contexto geográfico del proyecto para el escenario de Construcción Actual.

4

2.1 Sistema de modelación WRF - CALPUFF 2 METODOLOGÍA

Figura 2. Contexto geográfico del proyecto para el escenario de Construcción Futura.

5

2.2 Resumen de emisiones 2 METODOLOGÍA

2.2 Resumen de emisiones

Las emisiones utilizadas como datos de entrada en el sistema de mododelación WRF-CALPUFF fueron obtenidas

del informe Inventario de Emisiones "Ajustes constructivos a Instalaciones de Relaves Espesados". A continuación,

en las Tablas 1 y 2, se presenta un resumen de estas por cada fuente para el Escenario de Construcción Actual y

el Escenario Construcción Futura. Cabe destacar que las emisiones de NO _x_ fueron consideradas en su totalidad

como NO 2, esto constituye el escenario más conservador desde el punto de vista de los gases, y que para la

modelación de Material Particulado Sedimentable (MPS) se consideraron las emisiones de MP30.

|Contaminante|CO|HC|MP10|MP2,5|MPS|NO2|SO2|
|---|---|---|---|---|---|---|---|
|Fuente|[ton/año]|[ton/año]|[ton/año]|[ton/año]|[ton/año]|[ton/año]|[ton/año]|
|Botadero 57|0,0000|0,0000|2,2286|0,3375|4,7120|0,0000|0,0000|
|Muro norte|0,0000|0,0000|0,3277|0,0635|0,7946|0,0000|0,0000|
|Muro oeste|0,0000|0,0000|0,6549|0,1269|1,5884|0,0000|0,0000|
|Muro sur|0,0000|0,0000|1,2376|0,2859|3,3388|0,0000|0,0000|
|PEAD|57,3191|7,3146|6,6752|6,1882|1,7293|109,5980|0,1666|
|Ruta 50 PEAD|1,6689|0,4261|82,9285|8,4906|289,4739|7,7390|0,0075|
|Total|58,9880|7,7407|94,0526|15,4926|301,6369|117,3370|0,1741|

Tabla 1. Emisiones por fuente del proyecto, en toneladas por año, para la Fase de Construcción Actual.

6

|Contaminante|CO|HC|MP10|MP2,5|MPS|NO2|SO2|
|---|---|---|---|---|---|---|---|
|Fuente|[ton/año]|[ton/año]|[ton/año]|[ton/año]|[ton/año]|[ton/año]|[ton/año]|
|Acopio Temp 1|5,0551|0,6516|20,1025|3,3736|40,2440|9,9719|0,0150|
|Acopio Temp 2|0,1927|0,0248|3,8086|0,5952|7,5658|0,3801|0,0006|
|Acopio Temp 3|0,1927|0,0248|5,0048|0,7784|9,9506|0,3801|0,0006|
|Botadero 57|8,2469|1,0630|4,2726|1,1488|7,7833|16,2681|0,0245|
|Botadero A4|0,0000|0,0000|0,0997|0,0151|0,2108|0,0000|0,0000|
|Botadero A5|0,0000|0,0000|0,0997|0,0151|0,2108|0,0000|0,0000|
|Cajon RT|1,3715|0,1861|0,3670|0,2542|0,4859|2,4655|0,0037|
|Camino Acceso PRET|0,0741|0,0096|0,0053|0,0053|0,0000|0,1462|0,0002|
|Camino Acopio Temp 1 a Cajon RT no-pav1|0,2172|0,0456|13,7895|1,4009|48,1767|1,2448|0,0010|
|Camino Acopio Temp 1 a Cajon RT no-pav2|0,0139|0,0029|0,8828|0,0897|3,0843|0,0797|0,0001|
|Camino Acopio Temp 1 a Cajon RT pav1|0,3665|0,0770|3,8320|0,9583|17,8815|2,1006|0,0017|
|Camino Acopio Temp 1 a Cajon RT pav2|0,6368|0,1338|6,7975|1,6988|31,7265|3,6498|0,0029|
|Camino Acopio Temp 1 a Muro norte pav|0,8326|0,1750|8,8894|2,2216|41,4901|4,7725|0,0038|
|Camino Acopio Temp 1 a PEAD no-pav|0,0998|0,0210|6,3386|0,6440|22,1454|0,5722|0,0005|
|Camino Acopio Temp 1 a Rel CH MH no-pav|0,0006|0,0001|0,0358|0,0036|0,1250|0,0032|0,0000|
|Camino Acopio Temp 1 a Rel CH MH pav|0,0025|0,0005|0,0270|0,0068|0,1261|0,0145|0,0000|
|Camino Acopio Temp 1 a SE PRET no-pav|0,0001|0,0000|0,0079|0,0008|0,0274|0,0007|0,0000|
|Camino Acopio Temp 1 a Sentina RT no-pav|0,0222|0,0047|1,4090|0,1431|4,9226|0,1272|0,0001|

2.2 Resumen de emisiones 2 METODOLOGÍA

|Contaminante|CO|HC|MP10|MP2,5|MPS|NO2|SO2|
|---|---|---|---|---|---|---|---|
|Fuente|[ton/año]|[ton/año]|[ton/año]|[ton/año]|[ton/año]|[ton/año]|[ton/año]|
|Camino Botadero 57 a Acopio Temp 1 no-pav|0,1549|0,0299|15,2553|1,5415|53,3301|0,8579|0,0007|
|Camino Cajón RT a Botadero A4 no-pav|0,0045|0,0009|0,2831|0,0288|0,9889|0,0256|0,0000|
|Camino Cajón RT a Botadero A4 pav|0,0016|0,0003|0,0168|0,0042|0,0783|0,0090|0,0000|
|Camino Cajón RT a Botadero A5 no-pav|0,0028|0,0006|0,1785|0,0181|0,6236|0,0161|0,0000|
|Camino Cajón RT a Botadero A5 pav|0,0063|0,0013|0,0669|0,0167|0,3120|0,0359|0,0000|
|Camino Calama a Barrio cívico cnp|0,0270|0,0066|1,3927|0,1419|4,8641|0,1580|0,0001|
|Camino Calama a Barrio cívico cp1 T1|0,4135|0,0948|2,4102|0,6192|11,1440|2,5195|0,0022|
|Camino Calama a Barrio cívico cp1 T2|0,3997|0,0916|2,3299|0,5986|10,7726|2,4356|0,0021|
|Camino Calama a Barrio cívico cp1 T3|0,5652|0,1296|3,2939|0,8463|15,2302|3,4434|0,0029|
|Camino Calama a Campamento RT cp3 T1|0,3429|0,0891|1,5987|0,4136|7,3741|1,9179|0,0016|
|Camino Calama a Campamento RT cp3 T2|0,3287|0,0855|1,5325|0,3965|7,0689|1,8386|0,0015|
|Camino Calama a Campamento RT cp3 T3|0,3248|0,0845|1,5146|0,3918|6,9864|1,8171|0,0015|
|Camino Calama a Campamento RT cp3 T4|0,3160|0,0822|1,4735|0,3812|6,7967|1,7678|0,0015|
|Camino Calama a Campamento RT cp3 T5|0,3041|0,0791|1,4181|0,3669|6,5410|1,7013|0,0014|
|Camino Campamento RT a Barrio cívico cp2 T1|0,2974|0,0773|1,3865|0,3587|6,3953|1,6634|0,0014|
|Camino Campamento RT a Barrio cívico cp2 T2|0,3127|0,0813|1,4578|0,3771|6,7244|1,7490|0,0014|
|Camino Campamento RT a Barrio cívico cp2 T3|0,2554|0,0664|1,1908|0,3081|5,4926|1,4286|0,0012|
|Camino Campamento RT a Barrio cívico cp2 T4|0,1816|0,0472|0,8469|0,2191|3,9064|1,0160|0,0008|
|Camino PEAD a Botadero A4 pav|0,0228|0,0048|0,2439|0,0610|1,1384|0,1309|0,0001|
|Camino Pta Hormigón a Cajón RT no-pav|0,0003|0,0001|0,0165|0,0017|0,0575|0,0016|0,0000|
|Camino Pta Hormigón a EBR no-pav1|0,0007|0,0001|0,0393|0,0040|0,1374|0,0038|0,0000|
|Camino Pta Hormigón a EBR no-pav2|0,0002|0,0000|0,0111|0,0011|0,0388|0,0011|0,0000|
|Camino Pta Hormigón a EBR pav|0,0045|0,0009|0,0408|0,0103|0,1901|0,0257|0,0000|
|Camino Pta Hormigón a LAT 220 no-pav|0,0002|0,0000|0,0098|0,0010|0,0341|0,0009|0,0000|
|Camino Pta Hormigón a LAT 220 pav|0,0000|0,0000|0,0003|0,0001|0,0013|0,0002|0,0000|
|Camino Pta Hormigón a PEAD no-pav|0,0147|0,0031|0,8724|0,0887|3,0476|0,0845|0,0001|
|Camino Pta Hormigón a Rel RT no-pav|0,0004|0,0001|0,0241|0,0025|0,0843|0,0023|0,0000|
|Camino Pta Hormigón a SE PRET no-pav|0,0009|0,0002|0,0544|0,0055|0,1901|0,0053|0,0000|
|Camino Pta Hormigón a Sentina RT no-pav|0,0055|0,0012|0,3245|0,0330|1,1336|0,0314|0,0000|
|EBR|0,6515|0,0840|0,0934|0,0934|0,0000|1,2851|0,0020|
|GE Cajón RT|1,3269|0,5029|0,4330|0,4330|0,0000|6,1598|0,4051|
|GE EBR|1,5417|0,5843|0,5031|0,5031|0,0000|7,1569|0,4706|
|GE LAT 220|0,7709|0,2922|0,2515|0,2515|0,0000|3,5784|0,2353|
|GE LMT 34 5|0,6424|0,2435|0,2096|0,2096|0,0000|2,9820|0,1961|
|GE PEAD|7,5512|2,8620|2,4641|2,4641|0,0000|35,0540|2,3051|
|GE Rel CH MH|1,1563|0,4383|0,3773|0,3773|0,0000|5,3676|0,3530|
|GE Rel RT|1,0278|0,3896|0,3354|0,3354|0,0000|4,7712|0,3138|
|GE Sentina RT|0,5781|0,2191|0,1887|0,1887|0,0000|2,6838|0,1765|
|GE Sist Resp Elec|0,7709|0,2922|0,2515|0,2515|0,0000|3,5784|0,2353|
|LAT 220|2,5755|0,3096|0,4470|0,3535|0,6401|4,0295|0,0060|
|LAT 34 5|0,6519|0,0840|0,1113|0,0973|0,0157|1,2860|0,0020|
|Muro norte con2|0,4520|0,0583|3,8388|1,2290|4,4277|0,8917|0,0013|
|PEAD con2|6,2123|0,8713|5,1795|2,2660|15,9783|9,9656|0,0148|
|Rel CH MH|10,4329|1,3960|1,8740|1,3602|3,6314|19,1051|0,0287|
|Rel RT|10,4010|1,3919|1,4479|1,1716|1,8644|19,0420|0,0286|
|SE PRET|0,0000|0,0000|0,0030|0,0005|0,0064|0,0000|0,0000|
|Sentina RT|1,6297|0,2194|3,6766|1,7618|14,5843|2,9750|0,0045|
|Sist Resp Elec|0,6744|0,0869|0,3850|0,2263|1,2331|1,3303|0,0021|
|Total|70,6615|13,8046|137,1242|34,1641|439,2211|198,1075|4,8558|

Tabla 2. Emisiones por fuente del proyecto, en toneladas por año, para la Fase de Construcción Futura.

7

3 RESULTADOS

3 Resultados

En esta sección, se presentan los resultados de la modelación de dispersión para Proyecto obtenidos mediante

el sistema de modelación WRF-CALPUFF.

3.1 Aportes del Proyecto

En la Tabla 3, se presentan los aportes a las concentraciones de MP10, MP2,5, gases y tasa de depositación

de MPS para la Fase de Construcción. Las coordenadas del punto de máximo impacto (PMI) del Proyecto, se

muestran en la Tabla 4.

Para la Fase de Construcción (Futura - Actual), se observan aportes bajos y que cumplen con la normativa

vigente en en todos los contaminantes y estadísticos evaluados. Estos resultados, se deben principalmente a

que esta fase se evalúa en términos de la diferencia de dos escenarios (Construcción Actual y Construcción

Futura). En este sentido, los valores de los aportes a las concentraciones dependen del cambio del nivel de

actividad de las fuentes emisoras y del cambio de ubicación de éstas en ambos escenarios. Para este caso,

el total de las emisiones del Escenario de Construcción Futura es levemente mayor a las del Escenario de

Construcción Actual lo que se refleja en aportes menores 0,5 _μ_ g/m [3] para todos los receptores y estadísticos

evaluados. Cabe señalar que los resultados de la modelación se muestran aproximados al entero más cercano.

8

3.1 Aportes del Proyecto 3 RESULTADOS

|SOs [μg/m3N] 2|P99,73 1hr|0|0|0|0|0|0|12|
|---|---|---|---|---|---|---|---|---|
|SO_s_<br>2 [_μ_g/m3N]|P99,7<br>día|0|0|0|0|0|0|2|
|SO_s_<br>2 [_μ_g/m3N]|_x_<br>Año|0|0|0|0|0|0|1|
|SO_p_<br>2 [_μ_g/m3N]|P98.5<br>1hr|0|0|0|0|0|0|10|
|SO_p_<br>2 [_μ_g/m3N]|P99<br>día|0|0|0|0|0|0|2|
|SO_p_<br>2 [_μ_g/m3N]|_x_<br>Año|0|0|0|0|0|0|1|
|NO2 [_μ_g/m3N]|P99<br>1hr|1|0|1|1|1|0|169|
|NO2 [_μ_g/m3N]|_x_<br>Año|0|0|0|0|0|0|14|
|MPS [mg/m2-día]|_x_<br>Mes|0|0|0|0|0|0|47|
|MPS [mg/m2-día]|_x_<br>Año|0|0|0|0|0|0|44|
|MP2,5 [_μ_g/m3N]|P98<br>día|0|0|0|0|0|0|3|
|MP2,5 [_μ_g/m3N]|_x_<br>Año|0|0|0|0|0|0|1|
|MP10 [_μ_g/m3N]|P98<br>día|0|0|0|0|0|0|17|
|MP10 [_μ_g/m3N]|_x_<br>Año|0|0|0|0|0|0|7|
|HC [_μ_g/m3N]|P98<br>día|0|0|0|0|0|0|2|
|HC [_μ_g/m3N]|_x_<br>Año|0|0|0|0|0|0|1|
|CO [_μ_g/m3N]|P99<br>1hr|0|0|0|0|0|0|38|
|CO [_μ_g/m3N]|P99<br>8hr|0|0|0|0|0|0|20|
|Contaminante|Estadístico<br>Receptor|Centro|Chiu Chiu|H. del Cobre|Marzo 23|PVK|Lasana|PMI|

9

|SOs [μg/m3N] 2|P99,73 1hr|-68,80|-22,32|
|---|---|---|---|
|SO_s_<br>2 [_μ_g/m3N]|P99,7<br>día|-68,80|-22,32|
|SO_s_<br>2 [_μ_g/m3N]|_x_<br>Año|-68,80|-22,32|
|SO_p_<br>2 [_μ_g/m3N]|P98.5<br>1hr|-68,80|-22,32|
|SO_p_<br>2 [_μ_g/m3N]|P99<br>día|-68,80|-22,32|
|SO_p_<br>2 [_μ_g/m3N]|_x_<br>Año|-68,80|-22,32|
|NO2 [_μ_g/m3N]|P99<br>1hr|-68,80|-22,32|
|NO2 [_μ_g/m3N]|_x_<br>Año|-68,80|-22,32|
|MPS [mg/m2-día]|_x_<br>Mes|-68,85|-22,31|
|MPS [mg/m2-día]|_x_<br>Año|-68,85|-22,31|
|MP2,5 [_μ_g/m3N]|P98<br>día|-68,84|-22,31|
|MP2,5 [_μ_g/m3N]|_x_<br>Año|-68,84|-22,32|
|MP10 [_μ_g/m3N]|P98<br>día|-68,84|-22,31|
|MP10 [_μ_g/m3N]|_x_<br>Año|-68,84|-22,32|
|HC [_μ_g/m3N]|P98<br>día|-68,80|-22,32|
|HC [_μ_g/m3N]|_x_<br>Año|-68,80|-22,32|
|CO [_μ_g/m3N]|P99<br>1hr|-68,80|-22,32|
|CO [_μ_g/m3N]|P99<br>8hr|-68,80|-22,32|
|Contaminante|Estadístico<br>Receptor|Longitud|Latitud|

3.2 Comparación con la norma 3 RESULTADOS

3.2 Comparación con la norma

Las normas chilenas de calidad ambiental, cada una dictada por medio de un Decreto Supremo, establecen los

valores de las concentraciones y períodos, máximos o mínimos permisibles de los contaminantes. En la Tabla

5 se muestra las concentraciones máximas permitidas según la normativa Chilena vigente, el tipo de norma a

la cual corresponde y el decreto que establece estos límites. Cabe destacar que una norma de tipo primaria

es aquella que establece los valores de las concentraciones y períodos, máximos y mínimos permisibles cuya

presencia en el ambiente pueda constituir un riesgo para la vida o la salud de la población. Análogamente, las

de tipo secundaria norman aquellos contaminantes cuya presencia en el ambiente pueda constituir un riesgo

para la protección o conservación del medio ambiente, o la preservación de la naturaleza. (Fuente: Ley 19.300

de Bases del Medio Ambiente).

|Contaminante|Tipo de Norma|Estadístico|Valor|Referencia|
|---|---|---|---|---|
|MP10|Primaria|Promedio del periodo|50_ μ_g/m3N|D.S. 45/02 MINSEGPRES|
|MP10|Primaria|Percentil 98 diario|150_ μ_g/m3N|D.S. 59/13 MMA|
|MP2,5|Primaria|Promedio del periodo|20_ μ_g/m3N|D.S. 12/11 MMA|
|MP2,5|Primaria|Percentil 98 diario|50_ μ_g/m3N|D.S. 12/11 MMA|
|MPS|Secundaria|Promedio del periodo|100 mg/m2-día|D.S. 04/92 MINAGRI|
|MPS|Secundaria|Percentil 98 diario|150 mg/m2-día|D.S. 04/92 MINAGRI|
|SO2|Primaria|Promedio del periodo|60_ μ_g/m3N|D.S. 104/19 MMA|
|SO2|Primaria|Percentil 99 diario|150_ μ_g/m3N|D.S. 104/19 MMA|
|SO2|Primaria|Percentil 98,5 horario|350_ μ_g/m3N|D.S. 104/19 MMA|
|SO2|Secundaria|Promedio del periodo|80_ μ_g/m3N|D.S. 22/10 MINSEGPRES|
|SO2|Secundaria|Percentil 99,7 diario|365_ μ_g/m3N|D.S. 22/10 MINSEGPRES|
|SO2|Secundaria|Percentil 99,73 horario|1.000_ μ_g/m3N|D.S. 22/10 MINSEGPRES|
|NO2|Primaria|Promedio del periodo|100_ μ_g/m3N|D.S. 114/02 MINSEGPRES|
|NO2|Primaria|Percentil 99 horario|400_ μ_g/m3N|D.S. 114/13 MINSEGPRES|
|CO|Primaria|Percentil 99 8 horas|10.000_ μ_g/m3N|D.S. 115/02 MINSEGPRES|
|CO|Primaria|Percentil 99 horario|30.000_ μ_g/m3N|D.S. 115/13 MINSEGPRES|
|O3|Primaria|Percentil 99 8 horas|120_ μ_g/m3N|D.S. 112/02 MINSEGPRES|

Tabla 5. Valores límites de referencia según la normativa vigente para cada contaminante.

En la Tabla 6, se presenta una comparación porcentual entre los límites establecidos por la normativa vigente

y los aportes obtenidos en la modelación para la Fase de Construcción. En ella, se puede observar que todos

los receptores cumplen con la normativa establecida para cada receptor y contaminante evaluado. Cabe señalar

que los resultados expuestos en la tabla fueron aproximados al entero más cercano, por lo que todos los valores

presentados son menores a 0,5% de la norma establecida para cada contaminante.

10

3.2 Comparación con la norma 3 RESULTADOS

|SOs [μg/m3N] 2|P99,73 1hr|0%|0%|0%|0%|0%|0%|1%|
|---|---|---|---|---|---|---|---|---|
|SO_s_<br>2 [_μ_g/m3N]|P99,7<br>día|0%|0%|0%|0%|0%|0%|1%|
|SO_s_<br>2 [_μ_g/m3N]|_x_<br>Año|0%|0%|0%|0%|0%|0%|1%|
|SO_p_<br>2 [_μ_g/m3N]|P98.5<br>1hr|0%|0%|0%|0%|0%|0%|3%|
|SO_p_<br>2 [_μ_g/m3N]|P99<br>día|0%|0%|0%|0%|0%|0%|1%|
|SO_p_<br>2 [_μ_g/m3N]|_x_<br>Año|0%|0%|0%|0%|0%|0%|2%|
|NO2 [_μ_g/m3N]|P99<br>1hr|0%|0%|0%|0%|0%|0%|42%|
|NO2 [_μ_g/m3N]|_x_<br>Año|0%|0%|0%|0%|0%|0%|14%|
|MPS [mg/m2-día]|_x_<br>Mes|0%|0%|0%|0%|0%|0%|31%|
|MPS [mg/m2-día]|_x_<br>Año|0%|0%|0%|0%|0%|0%|44%|
|MP2,5 [_μ_g/m3N]|P98<br>día|0%|0%|0%|0%|0%|0%|6%|
|MP2,5 [_μ_g/m3N]|_x_<br>Año|0%|0%|0%|0%|0%|0%|5%|
|MP10 [_μ_g/m3N]|P98<br>día|0%|0%|0%|0%|0%|0%|11%|
|MP10 [_μ_g/m3N]|_x_<br>Año|0%|0%|0%|0%|0%|0%|14%|
|HC [_μ_g/m3N]|P98<br>día|-|-|-|-|-|-|-|
|HC [_μ_g/m3N]|_x_<br>Año|-|-|-|-|-|-|-|
|CO [_μ_g/m3N]|P99<br>1hr|0%|0%|0%|0%|0%|0%|0%|
|CO [_μ_g/m3N]|P99<br>8hr|0%|0%|0%|0%|0%|0%|0%|
|Contaminante|Estadístico<br>Receptor|Centro|Chiu Chiu|H. del Cobre|Marzo 23|PVK|Lasana|PMI|

11

3.3 Isolíneas de concentración 3 RESULTADOS

3.3 Isolíneas de concentración

Las isolíneas de concentración tienen por objetivo presentar el impacto espacial del Proyecto. Es por esto que

los niveles de concentración se presentan en un mapa que pone en contexto las concentraciones y los receptores

en que se evalúan los aportes. En las Figuras 3 a la 19, se muestran las isolíneas de concentración para MP10,

MP2 _,_ 5, gases y de tasa de depositación de MPS.

En general, las isolíneas de concentración siguen el patrón de los vientos predominantes en la zona durante

el periodo menos favorable en el sentido de la calidad del aire. En este caso, ese periodo ocurre durante la

noche ya los vientos son de menor magnitud que los observados durante el día impidiendo la dispersión de los

contaminantes (ver documento "Informe de observaciones y modelación meteorológica Distrito Norte"). Esto se

observa en las isolíneas de Construcción Actual y Construcción Futura (no mostrado). Sin embargo, los patrones

observados en la Fase de Construcción (Futura - Actual) son distintos ya que lo que refleja los aportes del

Proyecto, en este caso, es la diferencia de dos escenarios (Construcción Futura - Construcción Actual). En

términos simples, las isolíneas que se muestran para la Fase de Construcción (Futura - Actual) responden a la

diferencia de los campos promedio y percentil que corresponda a cada contaminante. Debido a lo anterior, las

isolíneas pueden tener diversas formas, variando de un contaminante a otro.

Cabe señalar que para este Proyecto se ha establecido, según el capítulo 2 de la DIA, el valor de 0,5 _μ_ g/m [3] N

para MP10 promedio anual (Fase de Construcción), como Área de Influencia (AI), que corresponde al 1% de la

norma para este contaminante.

12

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 3. Percentil 99 8 horas de CO para la Fase de Construcción (Futura - Actual).

13

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 4. Percentil 99 horario de CO para la Fase de Construcción (Futura - Actual).

14

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 5. Promedio anual de HC para la Fase de Construcción (Futura - Actual).

15

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 6. Percentil 98 diario de HC para la Fase de Construcción (Futura - Actual).

16

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 7. Promedio anual de MP10 para la Fase de Construcción (Futura - Actual).

17

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 8. Percentil 98 diario de MP10 para la Fase de Construcción (Futura - Actual).

18

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 9. Promedio anual de MP2 _,_ 5 para la Fase de Construcción (Futura - Actual).

19

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 10. Percentil 98 diario de MP2 _,_ 5 para la Fase de Construcción (Futura - Actual).

20

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 11. Promedio anual de MPS para la Fase de Construcción (Futura - Actual).

21

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 12. Promedio mensual de MPS para la Fase de Construcción (Futura - Actual).

22

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 13. Promedio anual de NO 2 para la Fase de Construcción (Futura - Actual).

23

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 14. Percentil 99 horario de NO 2 para la Fase de Construcción (Futura - Actual).

24

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 15. Promedio anual de SO 2 para la Fase de Construcción (Futura - Actual).

25

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 16. Percentil 99 diario de SO 2 para la Fase de Construcción (Futura - Actual).

26

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 17. Percentil 98,5 horario de SO 2 para la Fase de Construcción (Futura - Actual).

27

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 18. Promedio anual de SO 2 para la Fase de Construcción (Futura - Actual).

28

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 19. Percentil 99,7 diario de SO 2 para la Fase de Construcción (Futura - Actual).

29

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 20. Percentil 99,73 horario de SO 2 para la Fase de Construcción (Futura - Actual).

30

3.4 Análisis de Incertidumbre 3 RESULTADOS

3.4 Análisis de Incertidumbre

El objetivo de un análisis de incertidumbre es poner en contexto los resultados de las simulaciones de dispersión

con los errores del modelo meteorológico. De esta manera, se apunta a evaluar posibles sobre- o subestimaciones

del modelo de dispersión. En este sentido, se observa que el modelo WRF representa muy bien la meteorología

predominante del sector, ya sea para velocidad de viento o dirección de de viento (ver documento "Informe de

observaciones y modelación meteorológica Distrito Norte"). Debido a lo anterior, se concluye que no existen

antecedentes para considerar incertidumbres significativas en las concentraciones presentadas anteriormente,

ya sea en las magnitudes o en la dirección de la pluma.

31

4 CONCLUSIONES

4 Conclusiones

En este documento se presentan de los resultados obtenidos al modelar la dispersión atmosférica de las con

centraciones de MP10, MP2 _,_ 5, gases y tasa de depositación de MPS para el proyecto “Ajustes constructivos

a Instalaciones de Relaves Espesados” de CODELCO DCH que se desarrolla en la Comuna de Calama en la

Región de Antofagasta, Chile.

El Proyecto cuenta con una fase, la cual corresponde a Construcción. Sin embargo, esta, durante sus obras,

requiere de modificaciones a un proyecto anterior, que aprobado ambientalmente en la RCA N [o] 0022/2016, ya

que se trata de una adecuación constructiva. Debido a lo anterior, los aportes a las concentraciones de la Fase

de Construcción del Proyecto deben ser evaluados en términos de la diferencia de los resultados obtenidos

en los escenarios de Construcción Futura (el Proyecto) y Construcción Actual o Caso Base (proyecto aprobado

en la RCA N [o] 0022/2016). Para obtener esta diferencia, se obtienen los datos (grilla y discretos) promedio y

percentil correspondientes a cada contaminante y a cada escenario. Luego, se hace la diferencia de los resul

tados (Construcción Futura menos Construcción Actual) para cada contaminante y estadístico evaluado en el

Proyecto. En el caso del Escenario de Construcción Futura se modela el año 2025 que es el año que constituye

el peor escenario en términos de las emisiones durante esta etapa del Proyecto y para el caso del Escenario

de Construcción Actual se modela el año 2023 debido a la misma razón anterior.

Respecto a los aportes del proyecto, durante la Fase de Construcción (Futura - Actual), se observa que todos

los contaminantes y estadísticos evaluados cumplen con la norma establecida.

Respecto de las isolíneas de concentración, se puede observar que los patrones observados en la Fase de

Operación son complejos, ya que lo que refleja los aportes del Proyecto, en este caso, es la diferencia de los

resultados ente los escenarios de Construcción Futura y Construcción Actual. En términos simples, las isolíneas

que se muestran para la Fase de Construcción (Futura - Actual) responden a la diferencia de los campos prome

dio y percentil que corresponda a cada contaminante. Debido a esto, las isolíneas de concentración pueden

tener diversas formas, variando de un contaminante a otro.

Finalmente, cabe señalar que para este Proyecto se ha establecido, según el capítulo 2 de la DIA, el valor de

0,5 _μ_ g/m [3] N para MP10 promedio anual (Fase de Construcción), como Área de Influencia (AI), que corresponde

al 1% de la norma para este contaminante.

32

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Emisiones por fuente del proyecto, en toneladas por año, para la Fase de Construcción Actual.**

| Contaminante | CO | HC | MP10 | MP2,5 | MPS | NO2 | SO2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Fuente | [ton/año] | [ton/año] | [ton/año] | [ton/año] | [ton/año] | [ton/año] | [ton/año] |
| Acopio Temp 1 | 5,0551 | 0,6516 | 20,1025 | 3,3736 | 40,2440 | 9,9719 | 0,0150 |
| Acopio Temp 2 | 0,1927 | 0,0248 | 3,8086 | 0,5952 | 7,5658 | 0,3801 | 0,0006 |
| Acopio Temp 3 | 0,1927 | 0,0248 | 5,0048 | 0,7784 | 9,9506 | 0,3801 | 0,0006 |
| Botadero 57 | 8,2469 | 1,0630 | 4,2726 | 1,1488 | 7,7833 | 16,2681 | 0,0245 |
| Botadero A4 | 0,0000 | 0,0000 | 0,0997 | 0,0151 | 0,2108 | 0,0000 | 0,0000 |
| Botadero A5 | 0,0000 | 0,0000 | 0,0997 | 0,0151 | 0,2108 | 0,0000 | 0,0000 |
| Cajon RT | 1,3715 | 0,1861 | 0,3670 | 0,2542 | 0,4859 | 2,4655 | 0,0037 |
| Camino Acceso PRET | 0,0741 | 0,0096 | 0,0053 | 0,0053 | 0,0000 | 0,1462 | 0,0002 |
| Camino Acopio Temp 1 a Cajon RT no-pav1 | 0,2172 | 0,0456 | 13,7895 | 1,4009 | 48,1767 | 1,2448 | 0,0010 |
| Camino Acopio Temp 1 a Cajon RT no-pav2 | 0,0139 | 0,0029 | 0,8828 | 0,0897 | 3,0843 | 0,0797 | 0,0001 |
| Camino Acopio Temp 1 a Cajon RT pav1 | 0,3665 | 0,0770 | 3,8320 | 0,9583 | 17,8815 | 2,1006 | 0,0017 |
| Camino Acopio Temp 1 a Cajon RT pav2 | 0,6368 | 0,1338 | 6,7975 | 1,6988 | 31,7265 | 3,6498 | 0,0029 |
| Camino Acopio Temp 1 a Muro norte pav | 0,8326 | 0,1750 | 8,8894 | 2,2216 | 41,4901 | 4,7725 | 0,0038 |
| Camino Acopio Temp 1 a PEAD no-pav | 0,0998 | 0,0210 | 6,3386 | 0,6440 | 22,1454 | 0,5722 | 0,0005 |
| Camino Acopio Temp 1 a Rel CH MH no-pav | 0,0006 | 0,0001 | 0,0358 | 0,0036 | 0,1250 | 0,0032 | 0,0000 |
| Camino Acopio Temp 1 a Rel CH MH pav | 0,0025 | 0,0005 | 0,0270 | 0,0068 | 0,1261 | 0,0145 | 0,0000 |
| Camino Acopio Temp 1 a SE PRET no-pav | 0,0001 | 0,0000 | 0,0079 | 0,0008 | 0,0274 | 0,0007 | 0,0000 |
| Camino Acopio Temp 1 a Sentina RT no-pav | 0,0222 | 0,0047 | 1,4090 | 0,1431 | 4,9226 | 0,1272 | 0,0001 |
