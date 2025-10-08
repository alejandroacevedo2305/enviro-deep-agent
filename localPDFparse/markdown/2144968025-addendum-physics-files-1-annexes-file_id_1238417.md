---
title: Sin título
author: GSAE
date: D:20191118105613
language: es
type: report
pages: 52
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Informe de modelación de dispersión "Ajustes operacionales para Mina Chuquicamata Subterránea"
-->

# Informe de modelación de dispersión "Ajustes operacionales para Mina Chuquicamata Subterránea"

Preparado para:

CODELCO División Chuquicamata

Preparado por:

Ingeniería y Geofísica Limitada.

Noviembre de 2019

## Contenidos

1 Introducción 2

2 Metodología 4

2.1 Sistema de modelación WRF - CALPUFF . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2.2 Resumen de emisiones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

3 Resultados 8

3.1 Aportes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

3.2 Comparación con la norma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

3.3 Isolíneas de concentración . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

3.3.1 Fase de Construcción. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14

3.3.2 Fase de Operación. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32

3.4 Análisis de Incertidumbre . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50

4 Conclusiones 51

1 INTRODUCCIÓN

## 1 Introducción

En la actualidad, la Mina Chuquicamata Subterránea (en adelante MCHS) se encuentra iniciando su fase

de operación y requiere realizar modificaciones a su proyecto autorizado por lo cual, mediante la presente

Declaración de Impacto Ambiental proyecto "Ajustes operacionales para Mina Chuquicamata Subterránea" (en

adelante el Proyecto), se somete al Sistema de Evaluación de Impacto Ambiental (en adelante SEIA) según lo

disponen los Artículos N [o] 8 y siguientes de la LBGMA, expresando, bajo juramento, que este Proyecto cumple

con la legislación ambiental vigente, de conformidad con lo exigido en el Artículo N [o] 19 del Decreto Supremo

N [o] 40/2012, que aprueba el Reglamento del SEIA.

El presente Proyecto considera modificar el proyecto original "Mina Chuquicamata Subterránea", el cual fue

autorizado mediante la Resolución Exenta N [o] 288/2010 de la Comisión Regional del Medio Ambiente de la

Región de Antofagasta; el proyecto "Optimización de Infraestructura PMCHS”, calificado favorablemente mediante

la Resolución Exenta N [o] 271/2016; y el Proyecto "Adecuaciones Constructivas y Operacionales del PMCHS"

aprobado ambientalmente mediante Resolución Exenta N [o] 473/2017. Adicionalmente, modifica lo presentado en

la Consulta de Pertinencia resuelta mediante Resolución Exenta N [o] 0519/2015 proyecto "Actualización de Área

de Instalaciones de Faena de Construcción PMCHS".

Actualmente, la MCHS se encuentra iniciando su fase de operación, específicamente está dando comienzo al

periodo de _rump up_, el que se extenderá por siete años, tiempo que será necesario para lograr el régimen

productivo de 140 ktpd. Es importante indicar que durante esta fase, además de la extracción de mineral, se

continuarán realizando actividades relacionadas con el desarrollo y habilitación de los restantes macro blo

ques, así como también la habilitación de infraestructura de los siguientes niveles de producción. Lo anterior

configura una condición de simultaneidad de la extracción de mineral con el desarrollo de la infraestructura

minera, tal como se señalara en el proyecto original. A mayor abundamiento en esa instancia se indicó que

"se debe tener en cuenta que debido a las características del método de explotación subterráneo, existirá una

permanente necesidad de habilitar de forma paulatina los posteriores niveles de explotación de la mina, por lo

cual se continuará con actividades de construcción".

Las modificaciones a la fase de operación de la MCHS que se someten a evaluación a través de esta DIA son

las siguientes:

_•_ Ampliación planta de tratamiento de aguas servidas.

_•_ Modificación al sistema de ventilación de la mina.

_•_ Modificación de la infraestructura de servicios en superficie.

_•_ Extensión de la vida útil de las instalaciones de faenas para empresas contratistas.

_•_ Complementación de la infraestructura de servicios en interior mina.

_•_ Optimización del _layout_ del área de explotación de la mina subterránea.

_•_ Modificación de la mano de obra para la operación de la MCHS.

2 _Domeyko 1864, Santiago_

1 INTRODUCCIÓN

Cabe indicar que la MCHS mantendrá sin variación su vida útil, el área y los volúmenes de extracción autorizados.

Con el objetivo de dar cumplimiento a los requerimientos del Sistema de Evaluación de Impacto Ambiental

(SEIA), se presentan en este documento los aportes a las concentraciones obtenidos en la modelación de dis

persión atmosférica de MP10, MP2,5, gases y tasa de depositación de MPS para el presente Proyecto en los

receptores con representatividad poblacional de la comuna de Calama.

La estructura del informe tiene el siguiente orden: en el capítulo 2 se presenta la metodología utilizada para

la modelación de dispersión; en el capítulo 3 se presentan los aportes a las concentraciones de los distintos

contaminantes que son generadas por el Proyecto; finalmente, en el capítulo 4, se presentan las conclusiones.

3 _Domeyko 1864, Santiago_

2 METODOLOGÍA

## 2 Metodología

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

del año 2018. Se utiliza este año ya que la modelación meteorológica de este periodo representa muy bien el

clima de la zona evaluada.

El Proyecto consta de dos fases, una de Construcción y una de Operación. Para el caso de la Fase de Cons

trucción, se modela el año 2021 que constituye el peor escenario en términos de las emisiones para esta etapa

del Proyecto. Para el caso de la Fase de Operación, se modela el año 2026 por la misma razón.

El área de modelación corresponde a una grilla de 62 x 62 km, con un espaciamiento de 1 km, en cuyo interior

se encuentra ubicado el sitio de emplazamiento del Proyecto y puntos de interés. Las Figuras 1 y 2 muestran el

área de estudio, los receptores en que se evaluarán las concentraciones y la ubicación de las fuentes de emisión

asociadas al Proyecto.

4 _Domeyko 1864, Santiago_

2.1 Sistema de modelación WRF - CALPUFF 2 METODOLOGÍA

Figura 1. Contexto geográfico del proyecto para la Fase de Construcción.

5 _Domeyko 1864, Santiago_

2.1 Sistema de modelación WRF - CALPUFF 2 METODOLOGÍA

Figura 2. Contexto geográfico del proyecto para la Fase de Operación.

6 _Domeyko 1864, Santiago_

2.2 Resumen de emisiones 2 METODOLOGÍA

2.2 Resumen de emisiones

Las emisiones utilizadas como datos de entrada en el sistema de mododelación WRF-CALPUFF fueron obtenidas

del informe Inventario de Emisiones "Ajustes operacionales para Mina Chuquicamata Subterránea". A contin

uación, en las Tablas 1 y 2, se presenta un resumen de estas por cada fuente para la Fase de Construcción y la

Fase de Operación. Cabe destacar que las emisiones de NO _x_ fueron consideradas en su totalidad como NO 2,

esto constituye el escenario más conservador desde el punto de vista de los gases.

|Fuente|CO|HC|MP10|MP2,5|MPS|NO<br>2|SO<br>2|
|---|---|---|---|---|---|---|---|
|Botadero J1 P|0,0000|0,0000|0,1412|0,0214|0,2985|0,0000|0,0000|
|Botadero J1 T|0,0000|0,0000|0,8860|0,1342|1,8733|0,0000|0,0000|
|Pique|5,1767|0,9463|0,8161|0,6963|0,2985|20,9939|0,1020|
|Ruta pique a botadero J1 p|0,0429|0,0100|2,4910|0,2523|8,7044|0,1334|0,0241|
|Ruta planta hormigón a túnel|0,0043|0,0010|0,1540|0,0157|0,5374|0,0135|0,0024|
|Ruta polvorín superficial a pique|0,0057|0,0009|0,6284|0,0648|2,1907|0,0131|0,0042|
|Ruta polvorín superficial a túnel|0,0012|0,0002|0,1360|0,0140|0,4741|0,0028|0,0009|
|Ruta túnel a botadero J1 t|0,1120|0,0261|6,4986|0,6582|22,7088|0,3480|0,0628|
|Túnel|2,9999|0,8485|1,4377|0,6859|1,8733|11,2567|0,0799|
|Total|8,3428|1,8331|13,1889|2,5429|38,9589|32,7614|0,2764|

Tabla 1. Emisiones por fuente del proyecto, en toneladas por año, para la Fase de Construcción.

|Fuente|CO|HC|MP10|MP2,5|MPS|NO<br>2|SO<br>2|
|---|---|---|---|---|---|---|---|
|Ruta CVPZN a instalaciones MCHS Codelco|0,2522|0,0537|11,8453|1,2040|41,3747|1,1525|0,0736|
|Ruta CVPZN a instalaciones MCHS Contratistas|1,9335|0,4117|178,5140|18,0004|624,1477|8,8359|0,5641|
|Ruta CVPZN a relleno sanitario RT|0,0001|0,0000|0,0046|0,0005|0,0160|0,0004|0,0000|
|Ruta Calama a instalaciones MCHS Codelco|0,3753|0,0799|0,2235|0,0780|0,9806|1,7151|0,1095|
|Ruta Calama a instalaciones MCHS Contratistas|0,1876|0,0400|0,4541|0,1218|2,2737|0,8575|0,0547|
|Ruta PAT casino VP a puerta 4|0,0001|0,0000|0,0001|0,0000|0,0004|0,0005|0,0000|
|Ruta PAT centro acopio a puerta 4|0,0001|0,0000|0,0000|0,0000|0,0002|0,0003|0,0000|
|Ruta PTAS a garita acceso norte|0,0001|0,0000|0,0001|0,0000|0,0004|0,0005|0,0000|
|Ruta garita acceso norte a CVPZN|0,0013|0,0003|0,0575|0,0058|0,2009|0,0054|0,0003|
|Total|2,7503|0,5856|191,0993|19,4105|668,9947|12,5683|0,8023|

Tabla 2. Emisiones por fuente del proyecto, en toneladas por año, para la Fase de Operación.

7 _Domeyko 1864, Santiago_

3 RESULTADOS

## 3 Resultados

En esta sección, se presentan los resultados de la modelación de dispersión para Proyecto obtenidos mediante

el sistema de modelación WRF-CALPUFF.

3.1 Aportes

En las Tablas 5 y 6, se presentan los aportes a las concentraciones de MP10, MP2,5, gases y tasa de de

positación de MPS para la Fase de Construcción y para la Fase de Operación, respectivamente. Las coordenadas

del punto de máximo impacto (PMI) para ambas fases del Proyecto, se muestran en las Tablas 3 y 4.

Para la Fase de Construcción, los gases evaluados presentan aportes bajos que cumplen con la normativa vigente.

En el caso del CO, HC y SO 2, los aportes no superan los 0,13 _μ_ g/m [3] N como valor máximo. Este valor se presenta

en el receptor PVK para CO como concentración horaria (percentil 99). En el caso del NO 2, los aportes alcanzan

0,51 _μ_ g/m [3] N en el mismo receptor mencionado anteriormente, también como concentración horaria (percentil

99). Para los contaminantes de tipo material particulado, se observa una concentración máxima en PVK para

MP10 de 0,03 _μ_ g/m [3] N como promedio anual y de 0,06 _μ_ g/m [3] N como concentración diaria (percentil 98).

Para la Fase de Operación, la situación es similar en términos de cumplimiento de la normativa vigente. Sin

embargo, los aportes de material particulado son más altos a los observados durante la Fase de Construcción.

De la Tabla 6, se puede observar una concentración máxima en PVK para MP10 de 0,4 _μ_ g/m [3] N como promedio

anual y de 0,7 _μ_ g/m [3] N como concentración diaria (percentil 98). Respecto de los gases, se puede apreciar que

los aportes a las concentraciones para estos contaminantes son más bajas en comparación observadas durante

la Fase de Construcción.

8 _Domeyko 1864, Santiago_

3.1 Aportes 3 RESULTADOS

|Contaminante|Estadístico|Coordenadas|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Contaminante|Estadístico|Lon|Este|Lat|Norte|Fecha|
|CO|P99 8hr|-68,8445|516.013|-22,2923|7.534.811|24-Mar-2018 08:00:00|
|CO|P99 hr|-68,8445|516.013|-22,2923|7.534.811|11-Jan-2018 07:00:00|
|HC|~~_x_ ~~Anual|-68,8445|516.013|-22,2923|7.534.811|-|
|HC|P98 diario|-68,8445|516.013|-22,2923|7.534.811|19-May-2018|
|MP10|~~_x_ ~~Anual|-68,8445|516.013|-22,2923|7.534.811|-|
|MP10|P98 diario|-68,8445|516.013|-22,2923|7.534.811|01-May-2018|
|MP2,5|~~_x_ ~~Anual|-68,8445|516.013|-22,2923|7.534.811|-|
|MP2,5|P98 diario|-68,8445|516.013|-22,2923|7.534.811|15-Oct-2018|
|MPS|~~_x_ ~~Anual|-68,8445|516.013|-22,2923|7.534.811|-|
|MPS|~~_x_ ~~Mensual|-68,8445|516.013|-22,2923|7.534.811|May-2018|
|NO2|~~_x_ ~~Anual|-68,8445|516.013|-22,2923|7.534.811|-|
|NO2|P99 hr|-68,8445|516.013|-22,2923|7.534.811|13-Dec-2018 05:00:00|
|SO_p_<br>2|~~_x_ ~~Anual|-68,8445|516.013|-22,2923|7.534.811|-|
|SO_p_<br>2|P99 diario|-68,8445|516.013|-22,2923|7.534.811|27-May-2018|
|SO_p_<br>2|P98,5 hr|-68,8445|516.013|-22,2923|7.534.811|28-Feb-2018 05:00:00|
|SO_s_<br>2|~~_x_ ~~Anual|-68,8445|516.013|-22,2923|7.534.811|-|
|SO_s_<br>2|P99,7 diario|-68,8445|516.013|-22,2923|7.534.811|20-May-2018|
|SO_s_<br>2|P99,73 hr|-68,8445|516.013|-22,2923|7.534.811|21-Mar-2018 06:00:00|

Tabla 3. Coordenadas del punto de máximo impacto (PMI) para la Fase de Construcción.

|Contaminante|Estadístico|Coordenadas|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Contaminante|Estadístico|Lon|Este|Lat|Norte|Fecha|
|CO|P99 8hr|-68,8346|517.026|-22,3378|7.529.768|14-Feb-2018 16:00:00|
|CO|P99 hr|-68,8346|517.026|-22,3378|7.529.768|06-Jan-2018 14:00:00|
|HC|~~_x_ ~~Anual|-68,8346|517.026|-22,3378|7.529.768|-|
|HC|P98 diario|-68,8346|517.026|-22,3378|7.529.768|29-Jun-2018|
|MP10|~~_x_ ~~Anual|-68,8346|517.026|-22,3378|7.529.768|-|
|MP10|P98 diario|-68,8346|517.026|-22,3378|7.529.768|29-Jun-2018|
|MP2,5|~~_x_ ~~Anual|-68,8346|517.026|-22,3378|7.529.768|-|
|MP2,5|P98 diario|-68,8346|517.026|-22,3378|7.529.768|29-Jun-2018|
|MPS|~~_x_ ~~Anual|-68,8346|517.026|-22,3378|7.529.768|-|
|MPS|~~_x_ ~~Mensual|-68,8346|517.026|-22,3378|7.529.768|May-2018|
|NO2|~~_x_ ~~Anual|-68,8346|517.026|-22,3378|7.529.768|-|
|NO2|P99 hr|-68,8346|523.139|-22,3378|7.540.849|30-Jun-2018 04:00:00|
|SO_p_<br>2|~~_x_ ~~Anual|-68,8346|517.026|-22,3378|7.529.768|-|
|SO_p_<br>2|P99 diario|-68,8346|517.026|-22,3378|7.529.768|05-Jul-2018|
|SO_p_<br>2|P98,5 hr|-68,8346|523.139|-22,3378|7.540.849|17-Oct-2018 05:00:00|
|SO_s_<br>2|~~_x_ ~~Anual|-68,8346|517.026|-22,3378|7.529.768|-|
|SO_s_<br>2|P99,7 diario|-68,8346|517.026|-22,3378|7.529.768|01-Jul-2018|
|SO_s_<br>2|P99,73 hr|-68,8346|523.139|-22,3378|7.540.849|30-Sep-2018 03:00:00|

Tabla 4. Coordenadas del punto de máximo impacto (PMI) para la Fase de Operación.

9 _Domeyko 1864, Santiago_

3.1 Aportes 3 RESULTADOS

|SOs [μg/m3N] 2|P99,73 1hr|0,0115|0,0059|0,0190|0,0119|0,0165|0,1692|
|---|---|---|---|---|---|---|---|
|SO_s_<br>2 [_μ_g/m3N]|P99,7<br>día|0,0027|0,0015|0,0038|0,0029|0,0049|0,0486|
|SO_s_<br>2 [_μ_g/m3N]|_x_<br>Año|0,0011|0,0003|0,0017|0,0012|0,0021|0,0230|
|SO_p_<br>2 [_μ_g/m3N]|P98.5<br>1hr|0,0077|0,0028|0,0120|0,0081|0,0120|0,1247|
|SO_p_<br>2 [_μ_g/m3N]|P99<br>día|0,0022|0,0013|0,0036|0,0025|0,0042|0,0451|
|SO_p_<br>2 [_μ_g/m3N]|_x_<br>Año|0,0011|0,0003|0,0017|0,0012|0,0021|0,0230|
|NO2 [_μ_g/m3N]|P99<br>1hr|0,1366|0,0526|0,2163|0,1402|0,2064|2,1588|
|NO2 [_μ_g/m3N]|_x_<br>Año|0,0181|0,0040|0,0281|0,0200|0,0332|0,3604|
|MPS [mg/m2-día]|_x_<br>Mes|0,0344|0,0123|0,0576|0,0375|0,0655|59,3808|
|MPS [mg/m2-día]|_x_<br>Año|0,0345|0,0216|0,0563|0,0371|0,0625|48,5856|
|MP2,5 [_μ_g/m3N]|P98<br>día|0,0430|0,0296|0,0531|0,0465|0,0722|1,2110|
|MP2,5 [_μ_g/m3N]|_x_<br>Año|0,0220|0,0066|0,0273|0,0239|0,0371|0,6809|
|MP10 [_μ_g/m3N]|P98<br>día|0,4212|0,2931|0,5171|0,4557|0,7043|12,0012|
|MP10 [_μ_g/m3N]|_x_<br>Año|0,2141|0,0654|0,2630|0,2327|0,3599|6,7460|
|HC [_μ_g/m3N]|P98<br>día|0,0016|0,0008|0,0025|0,0018|0,0028|0,0296|
|HC [_μ_g/m3N]|_x_<br>Año|0,0008|0,0002|0,0013|0,0009|0,0015|0,0168|
|CO [_μ_g/m3N]|P99<br>1hr|0,0296|0,0115|0,0466|0,0303|0,0444|0,4724|
|CO [_μ_g/m3N]|P99<br>8hr|0,0201|0,0143|0,0321|0,0211|0,0347|0,3484|
|Receptor|Receptor|Centro|Chiu Chiu|H. del Cobre|Marzo 23|PVK|PMI|

10 _Domeyko 1864, Santiago_

|SOs [μg/m3N] 2|P99,73 1hr|0,0035|0,0021|0,0045|0,0037|0,0054|0,8673|
|---|---|---|---|---|---|---|---|
|SO_s_<br>2 [_μ_g/m3N]|P99,7<br>día|0,0008|0,0007|0,0010|0,0009|0,0015|0,2350|
|SO_s_<br>2 [_μ_g/m3N]|_x_<br>Año|0,0003|0,0001|0,0003|0,0003|0,0005|0,0843|
|SO_p_<br>2 [_μ_g/m3N]|P98.5<br>1hr|0,0023|0,0007|0,0029|0,0025|0,0039|0,7238|
|SO_p_<br>2 [_μ_g/m3N]|P99<br>día|0,0007|0,0005|0,0009|0,0008|0,0013|0,2014|
|SO_p_<br>2 [_μ_g/m3N]|_x_<br>Año|0,0003|0,0001|0,0003|0,0003|0,0005|0,0843|
|NO2 [_μ_g/m3N]|P99<br>1hr|0,2985|0,1083|0,3659|0,3217|0,5102|99,7427|
|NO2 [_μ_g/m3N]|_x_<br>Año|0,0327|0,0068|0,0386|0,0368|0,0607|9,7690|
|MPS [mg/m2-día]|_x_<br>Mes|0,0016|0,0008|0,0019|0,0017|0,0028|22,7594|
|MPS [mg/m2-día]|_x_<br>Año|0,0015|0,0012|0,0019|0,0017|0,0029|18,2190|
|MP2,5 [_μ_g/m3N]|P98<br>día|0,0062|0,0031|0,0075|0,0067|0,0107|1,6182|
|MP2,5 [_μ_g/m3N]|_x_<br>Año|0,0028|0,0006|0,0033|0,0031|0,0050|0,7595|
|MP10 [_μ_g/m3N]|P98<br>día|0,0323|0,0164|0,0399|0,0349|0,0556|5,3620|
|MP10 [_μ_g/m3N]|_x_<br>Año|0,0149|0,0032|0,0180|0,0165|0,0268|2,9211|
|HC [_μ_g/m3N]|P98<br>día|0,0043|0,0021|0,0052|0,0047|0,0076|1,8247|
|HC [_μ_g/m3N]|_x_<br>Año|0,0019|0,0004|0,0023|0,0021|0,0035|0,7265|
|CO [_μ_g/m3N]|P99<br>1hr|0,0753|0,0275|0,0905|0,0812|0,1291|26,5847|
|CO [_μ_g/m3N]|P99<br>8hr|0,0577|0,0579|0,0680|0,0610|0,0957|17,4677|
|Receptor|Receptor|Centro|Chiu Chiu|H. del Cobre|Marzo 23|PVK|PMI|

3.2 Comparación con la norma 3 RESULTADOS

3.2 Comparación con la norma

Las normas chilenas de calidad ambiental, cada una dictada por medio de un Decreto Supremo, establecen los

valores de las concentraciones y períodos, máximos o mínimos permisibles de los contaminantes. En la Tabla

7 se muestra las concentraciones máximas permitidas según la normativa Chilena vigente, el tipo de norma a

la cual corresponde y el decreto que establece estos límites. Cabe destacar que una norma de tipo primaria

es aquella que establece los valores de las concentraciones y períodos, máximos y mínimos permisibles cuya

presencia en el ambiente pueda constituir un riesgo para la vida o la salud de la población. Análogamente, las

de tipo secundaria norman aquellos contaminantes cuya presencia en el ambiente pueda constituir un riesgo

para la protección o conservación del medio ambiente, o la preservación de la naturaleza. (Fuente: Ley 19.300

de Bases del Medio Ambiente).

|Contaminante|Tipo de Norma|Estadístico|Valor|Referencia|
|---|---|---|---|---|
|MPS|Secundaria|Promedio del Periodo|100 mg/m2-día|D.S. 04/92 MINAGRI|
|MPS|Secundaria|Promedio Mensual|150 mg/m2-día|D.S. 04/92 MINAGRI|
|MP10|Primaria|Promedio del Periodo|50_ μ_g/m3N|D.S. 45/02 MINSEGPRES|
|MP10|Primaria|Percentil 98 diario|150_ μ_g/m3N|D.S. 59/13 MMA|
|MP2.5|Primaria|Promedio del Periodo|20_ μ_g/m3N|D.S. 12/11 MMA|
|MP2.5|Primaria|Percentil 98 diario|50_ μ_g/m3N|D.S. 12/11 MMA|
|SO2|Primaria|Promedio del Periodo|60_ μ_g/m3N|D.S. 104/19 MINSEGPRES|
|SO2|Primaria|Percentil 99 diario<br>Percentil 98,5 horario|150_ μ_g/m3N<br>350_ μ_g/m3N|D.S. 104/19 MINSEGPRES<br>D.S. 104/19 MINSEGPRES|
|SO2|Secundaria|Promedio del Periodo|80_ μ_g/m3N|D.S. 22/10 MINSEGPRES|
|SO2|Secundaria|Percentil 99,7 diario|365_ μ_g/m3N|D.S. 22/10 MINSEGPRES|
|SO2|Secundaria|Percentil 99,73 horario|1.000_ μ_g/m3N|D.S. 22/10 MINSEGPRES|
|NO2|Primaria|Promedio del Periodo|100_ μ_g/m3N|D.S. 114/02 MINSEGPRES|
|NO2|Primaria|Percentil 99 horario|400_ μ_g/m3N|D.S. 114/02 MINSEGPRES|
|CO|Primaria|Percentil 99 8 horas|10.000_ μ_g/m3N|D.S. 115/02 MINSEGPRES|
|CO|Primaria|Percentil 99 horario|30.000_ μ_g/m3N|D.S. 115/02 MINSEGPRES|
|O3|Primaria|Percentil 99 8 horas|120_ μ_g/m3N|D.S. 112/02 MINSEGPRES|

Tabla 7. Valores límites de referencia según la normativa vigente para cada contaminante.

En las Tablas 8 y 9, se presenta una comparación porcentual entre los límites establecidos por la normativa

vigente y los aportes obtenidos en la modelación para la Fase de Construcción y para la Fase de Operación,

respectivamente. En ellas, se puede observar que la totalidad de los contaminantes observados cumplen con la

normativa vigente correspondiente. Por una parte, en la Fase de Construcción, se presentan porcentajes nulos

(<0,05%) en todos los contaminantes y estadísticos evaluados, salvo para NO 2 que alcanza un 0,1% de norma

anual y horaria. Por otra parte, en la Fase de Operación, se presentan también aportes nulos para gases, pero

no para material marticulado. En este sentido, el contaminante con mayor aporte es el MP10 (por sobre MP2,5

y MPS) que alcanza un máximo de 0,7% de la norma anual y un 0,5% de la norma diaria en PVK.

11 _Domeyko 1864, Santiago_

3.2 Comparación con la norma 3 RESULTADOS

|SOs [μg/m3N] 2|P99,73 1hr|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|---|---|---|---|---|---|---|---|
|SO_s_<br>2 [_μ_g/m3N]|P99,7<br>día|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|SO_s_<br>2 [_μ_g/m3N]|_x_<br>Año|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|SO_p_<br>2 [_μ_g/m3N]|P98.5<br>1hr|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|SO_p_<br>2 [_μ_g/m3N]|P99<br>día|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|SO_p_<br>2 [_μ_g/m3N]|_x_<br>Año|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|NO2 [_μ_g/m3N]|P99<br>1hr|0,0%|0,0%|0,1%|0,0%|0,1%|0,5%|
|NO2 [_μ_g/m3N]|_x_<br>Año|0,0%|0,0%|0,0%|0,0%|0,0%|0,4%|
|MPS [mg/m2-día]|_x_<br>Mes|0,0%|0,0%|0,0%|0,0%|0,0%|39,6%|
|MPS [mg/m2-día]|_x_<br>Año|0,0%|0,0%|0,1%|0,0%|0,1%|48,6%|
|MP2,5 [_μ_g/m3N]|P98<br>día|0,1%|0,1%|0,1%|0,1%|0,1%|2,4%|
|MP2,5 [_μ_g/m3N]|_x_<br>Año|0,1%|0,0%|0,1%|0,1%|0,2%|3,4%|
|MP10 [_μ_g/m3N]|P98<br>día|0,3%|0,2%|0,3%|0,3%|0,5%|8,0%|
|MP10 [_μ_g/m3N]|_x_<br>Año|0,4%|0,1%|0,5%|0,5%|0,7%|13,5%|
|HC [_μ_g/m3N]|P98<br>día|-|-|-|-|-|-|
|HC [_μ_g/m3N]|_x_<br>Año|-|-|-|-|-|-|
|CO [_μ_g/m3N]|P99<br>1hr|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|CO [_μ_g/m3N]|P99<br>8hr|0,0%|0,0%|0,0%|0,0%|0,0%|0,0%|
|Receptor|Receptor|Centro|Chiu Chiu|H. del Cobre|Marzo 23|PVK|PMI|

12 _Domeyko 1864, Santiago_

|SOs [μg/m3N] 2|P99,73 1hr|0,0%|0,0%|0,0%|0,0%|0,0%|0,1%|
|---|---|---|---|---|---|---|---|
|SO_s_<br>2 [_μ_g/m3N]|P99,7<br>día|0,0%|0,0%|0,0%|0,0%|0,0%|0,1%|
|SO_s_<br>2 [_μ_g/m3N]|_x_<br>Año|0,0%|0,0%|0,0%|0,0%|0,0%|0,1%|
|SO_p_<br>2 [_μ_g/m3N]|P98.5<br>1hr|0,0%|0,0%|0,0%|0,0%|0,0%|0,2%|
|SO_p_<br>2 [_μ_g/m3N]|P99<br>día|0,0%|0,0%|0,0%|0,0%|0,0%|0,1%|
|SO_p_<br>2 [_μ_g/m3N]|_x_<br>Año|0,0%|0,0%|0,0%|0,0%|0,0%|0,1%|
|NO2 [_μ_g/m3N]|P99<br>1hr|0,1%|0,0%|0,1%|0,1%|0,1%|24,9%|
|NO2 [_μ_g/m3N]|_x_<br>Año|0,0%|0,0%|0,0%|0,0%|0,1%|9,8%|
|MPS [mg/m2-día]|_x_<br>Mes|0,0%|0,0%|0,0%|0,0%|0,0%|15,2%|
|MPS [mg/m2-día]|_x_<br>Año|0,0%|0,0%|0,0%|0,0%|0,0%|18,2%|
|MP2,5 [_μ_g/m3N]|P98<br>día|0,0%|0,0%|0,0%|0,0%|0,0%|3,2%|
|MP2,5 [_μ_g/m3N]|_x_<br>Año|0,0%|0,0%|0,0%|0,0%|0,0%|3,8%|
|MP10 [_μ_g/m3N]|P98<br>día|0,0%|0,0%|0,0%|0,0%|0,0%|3,6%|
|MP10 [_μ_g/m3N]|_x_<br>Año|0,0%|0,0%|0,0%|0,0%|0,1%|5,8%|
|HC [_μ_g/m3N]|P98<br>día|-|-|-|-|-|-|
|HC [_μ_g/m3N]|_x_<br>Año|-|-|-|-|-|-|
|CO [_μ_g/m3N]|P99<br>1hr|0,0%|0,0%|0,0%|0,0%|0,0%|0,1%|
|CO [_μ_g/m3N]|P99<br>8hr|0,0%|0,0%|0,0%|0,0%|0,0%|0,2%|
|Receptor|Receptor|Centro|Chiu Chiu|H. del Cobre|Marzo 23|PVK|PMI|

3.3 Isolíneas de concentración 3 RESULTADOS

3.3 Isolíneas de concentración

Las isolíneas de concentración tienen por objetivo presentar el impacto espacial del Proyecto. Es por esto que

los niveles de concentración se presentan en un mapa que pone en contexto las concentraciones y los receptores

en que se evalúan los aportes. En las Figuras 3 a la 37, se muestran las isolíneas de concentración para MP10,

MP2 _,_ 5, gases y de tasa de depositación de MPS.

En general las isolíneas de concentración siguen el patrón de los vientos predominantes en la zona durante

el periodo menos favorable en el sentido de la calidad del aire. En este caso, ese periodo ocurre durante la

noche ya los vientos son de menor magnitud que los observados durante el día impidiendo la dispersión de los

contaminantes. En este caso, se observa lo descrito previamente, donde los vientos desplazan los contaminantes

hacia el oeste y, levemente, al suroeste de la zona donde se ubican las fuentes emisoras. Esta forma de los

vientos permite que la concentraciones que llegan a Calama y Chiu Chiu sean menores a las observadas en la

zona minera. En el caso del MPS, la situación es similar, sin embargo, al tratarse de una tasa de depositación, y

no de una concentración atmosférica, los valores de este contaminante caen rápidamente con la distancia desde

la fuente emisora. Esto provoca que los aportes de MPS sean aún más bajos en las zonas pobladas aledañas

a la DCH.

13 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

3.3.1 Fase de Construcción.

Figura 3. Percentil 99 8 horas de CO para la Fase de Construcción.

14 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 4. Percentil 99 horario de CO para la Fase de Construcción.

15 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 5. Promedio anual de HC para la Fase de Construcción.

16 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 6. Percentil 98 diario de HC para la Fase de Construcción.

17 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 7. Promedio anual de MP10 para la Fase de Construcción.

18 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 8. Percentil 98 diario de MP10 para la Fase de Construcción.

19 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 9. Promedio anual de MP2 _,_ 5 para la Fase de Construcción.

20 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 10. Percentil 98 diario de MP2 _,_ 5 para la Fase de Construcción.

21 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 11. Promedio anual de MPS para la Fase de Construcción.

22 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 12. Promedio mensual de MPS para la Fase de Construcción.

23 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 13. Promedio anual de NO 2 para la Fase de Construcción.

24 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 14. Percentil 99 horario de NO 2 para la Fase de Construcción.

25 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 15. Promedio anual de SO 2 para la Fase de Construcción.

26 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 16. Percentil 99 diario de SO 2 para la Fase de Construcción.

27 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 17. Percentil 98,5 horario de SO 2 para la Fase de Construcción.

28 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 18. Promedio anual de SO 2 para la Fase de Construcción.

29 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 19. Percentil 99,7 diario de SO 2 para la Fase de Construcción.

30 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 20. Percentil 99,73 horario de SO 2 para la Fase de Construcción.

31 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

3.3.2 Fase de Operación.

Figura 21. Percentil 99 8 horas de CO para la Fase de Operación.

32 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 22. Percentil 99 horario de CO para la Fase de Operación.

33 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 23. Promedio anual de HC para la Fase de Operación.

34 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 24. Percentil 98 diario de HC para la Fase de Operación.

35 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 25. Promedio anual de MP10 para la Fase de Operación.

36 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 26. Percentil 98 diario de MP10 para la Fase de Operación.

37 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 27. Promedio anual de MP2 _,_ 5 para la Fase de Operación.

38 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 28. Percentil 98 diario de MP2 _,_ 5 para la Fase de Operación.

39 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 29. Promedio anual de MPS para la Fase de Operación.

40 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 30. Promedio mensual de MPS para la Fase de Operación.

41 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 31. Promedio anual de NO 2 para la Fase de Operación.

42 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 32. Percentil 99 horario de NO 2 para la Fase de Operación.

43 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 33. Promedio anual de SO 2 para la Fase de Operación.

44 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 34. Percentil 99 diario de SO 2 para la Fase de Operación.

45 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 35. Percentil 98,5 horario de SO 2 para la Fase de Operación.

46 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 36. Promedio anual de SO 2 para la Fase de Operación.

47 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 37. Percentil 99,7 diario de SO 2 para la Fase de Operación.

48 _Domeyko 1864, Santiago_

3.3 Isolíneas de concentración 3 RESULTADOS

Figura 38. Percentil 99,73 horario de SO 2 para la Fase de Operación.

49 _Domeyko 1864, Santiago_

3.4 Análisis de Incertidumbre 3 RESULTADOS

3.4 Análisis de Incertidumbre

El objetivo de un análisis de incertidumbre es poner en contexto los resultados de las simulaciones de dispersión

con los errores del modelo meteorológico. De esta manera, se apunta a evaluar posibles sobre- o subestima

ciones del modelo de dispersión. En este sentido, se observa que el modelo WRF representa muy bien la

meteorología predominante del sector, ya sea para velocidad de viento o dirección de de viento (ver documento

"Informe de observaciones y modelación meteorológica Distrito Norte"). Debido a lo anterior, se concluye que no

existen antecedentes necesarios para considerar incertidumbres significativas en las concentraciones presentadas

anteriormente, ya sea en las magnitudes o en la dirección de la pluma.

50 _Domeyko 1864, Santiago_

4 CONCLUSIONES

## 4 Conclusiones

En este documento se presentan de los resultados obtenidos al modelar la dispersión atmosférica de las con

centraciones de MP10, MP2 _,_ 5, gases y tasa de depositación de MPS para el proyecto "Ajustes operacionales

para Mina Chuquicamata Subterránea" de CODELCO DCH que se desarrolla en la Comuna de Calama en la

Región de Antofagasta, Chile.

El Proyecto consta de dos fases, una de Construcción y una de Operación. Para el caso de la Fase de Cons

trucción, se modela el año 2021 que constituye el peor escenario en términos de las emisiones para esta etapa

del Proyecto. Para el caso de la Fase de Operación, se modela el año 2026 por la misma razón.

Respecto a los aportes del Proyecto, se puede observar que la totalidad de los contaminantes analizados cumplen

con la normativa vigente correspondiente. Por una parte, en la Fase de Construcción, se presentan porcentajes

nulos (<0,05%) en todos los contaminantes y estadísticos evaluados, salvo para NO 2 que alcanza un 0,1% de

norma anual y horaria. Por otra parte, en la Fase de Operación, se presentan también aportes nulos para gases,

pero no para material marticulado. En este sentido, el contaminante con mayor aporte es el MP10 (por sobre

MP2,5 y MPS) que alcanza un máximo de 0,7% de la norma anual y un 0,5% de la norma diaria en PVK.

Respecto de las isolíneas de concentración, se puede observar que estas siguen el patrón de los vientos pre

dominantes en la zona (ver documento "Informe de observaciones y modelación meteorológica Distrito Norte"),

desplazándose hacia el oeste y, levente, hacia el suroeste. Esta forma de los vientos permite que la concen

traciones que llegan a Calama y Chiu Chiu sean menores a las observadas en la zona minera. En el caso del

MPS, la situación es similar, sin embargo, al tratarse de una tasa de depositación, y no de una concentración

atmosférica, los valores de este contaminante caen rápidamente con la distancia desde la fuente emisora. Esto

provoca que los aportes de MPS sean aún más bajos en las zonas pobladas aledañas a la DCH.

51 _Domeyko 1864, Santiago_

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Emisiones por fuente del proyecto, en toneladas por año, para la Fase de Construcción.**

| Fuente | CO | HC | MP10 | MP2,5 | MPS | NO<br>2 | SO<br>2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ruta CVPZN a instalaciones MCHS Codelco | 0,2522 | 0,0537 | 11,8453 | 1,2040 | 41,3747 | 1,1525 | 0,0736 |
| Ruta CVPZN a instalaciones MCHS Contratistas | 1,9335 | 0,4117 | 178,5140 | 18,0004 | 624,1477 | 8,8359 | 0,5641 |
| Ruta CVPZN a relleno sanitario RT | 0,0001 | 0,0000 | 0,0046 | 0,0005 | 0,0160 | 0,0004 | 0,0000 |
| Ruta Calama a instalaciones MCHS Codelco | 0,3753 | 0,0799 | 0,2235 | 0,0780 | 0,9806 | 1,7151 | 0,1095 |
| Ruta Calama a instalaciones MCHS Contratistas | 0,1876 | 0,0400 | 0,4541 | 0,1218 | 2,2737 | 0,8575 | 0,0547 |
| Ruta PAT casino VP a puerta 4 | 0,0001 | 0,0000 | 0,0001 | 0,0000 | 0,0004 | 0,0005 | 0,0000 |
| Ruta PAT centro acopio a puerta 4 | 0,0001 | 0,0000 | 0,0000 | 0,0000 | 0,0002 | 0,0003 | 0,0000 |
| Ruta PTAS a garita acceso norte | 0,0001 | 0,0000 | 0,0001 | 0,0000 | 0,0004 | 0,0005 | 0,0000 |
| Ruta garita acceso norte a CVPZN | 0,0013 | 0,0003 | 0,0575 | 0,0058 | 0,2009 | 0,0054 | 0,0003 |
| Total | 2,7503 | 0,5856 | 191,0993 | 19,4105 | 668,9947 | 12,5683 | 0,8023 |

**Tabla 3.: Coordenadas del punto de máximo impacto (PMI) para la Fase de Construcción.**

| Contaminante | Estadístico | Coordenadas | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Contaminante | Estadístico | Lon | Este | Lat | Norte | Fecha |
| CO | P99 8hr | -68,8346 | 517.026 | -22,3378 | 7.529.768 | 14-Feb-2018 16:00:00 |
| CO | P99 hr | -68,8346 | 517.026 | -22,3378 | 7.529.768 | 06-Jan-2018 14:00:00 |
| HC | ~~_x_ ~~Anual | -68,8346 | 517.026 | -22,3378 | 7.529.768 | - |
| HC | P98 diario | -68,8346 | 517.026 | -22,3378 | 7.529.768 | 29-Jun-2018 |
| MP10 | ~~_x_ ~~Anual | -68,8346 | 517.026 | -22,3378 | 7.529.768 | - |
| MP10 | P98 diario | -68,8346 | 517.026 | -22,3378 | 7.529.768 | 29-Jun-2018 |
| MP2,5 | ~~_x_ ~~Anual | -68,8346 | 517.026 | -22,3378 | 7.529.768 | - |
| MP2,5 | P98 diario | -68,8346 | 517.026 | -22,3378 | 7.529.768 | 29-Jun-2018 |
| MPS | ~~_x_ ~~Anual | -68,8346 | 517.026 | -22,3378 | 7.529.768 | - |
| MPS | ~~_x_ ~~Mensual | -68,8346 | 517.026 | -22,3378 | 7.529.768 | May-2018 |
| NO2 | ~~_x_ ~~Anual | -68,8346 | 517.026 | -22,3378 | 7.529.768 | - |
| NO2 | P99 hr | -68,8346 | 523.139 | -22,3378 | 7.540.849 | 30-Jun-2018 04:00:00 |
| SO_p_<br>2 | ~~_x_ ~~Anual | -68,8346 | 517.026 | -22,3378 | 7.529.768 | - |
| SO_p_<br>2 | P99 diario | -68,8346 | 517.026 | -22,3378 | 7.529.768 | 05-Jul-2018 |
| SO_p_<br>2 | P98,5 hr | -68,8346 | 523.139 | -22,3378 | 7.540.849 | 17-Oct-2018 05:00:00 |
| SO_s_<br>2 | ~~_x_ ~~Anual | -68,8346 | 517.026 | -22,3378 | 7.529.768 | - |
| SO_s_<br>2 | P99,7 diario | -68,8346 | 517.026 | -22,3378 | 7.529.768 | 01-Jul-2018 |
| SO_s_<br>2 | P99,73 hr | -68,8346 | 523.139 | -22,3378 | 7.540.849 | 30-Sep-2018 03:00:00 |

**Tabla 4.: Coordenadas del punto de máximo impacto (PMI) para la Fase de Operación.**

| SOs [μg/m3N] 2 | P99,73 1hr | 0,0115 | 0,0059 | 0,0190 | 0,0119 | 0,0165 | 0,1692 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SO_s_<br>2 [_μ_g/m3N] | P99,7<br>día | 0,0027 | 0,0015 | 0,0038 | 0,0029 | 0,0049 | 0,0486 |
| SO_s_<br>2 [_μ_g/m3N] | _x_<br>Año | 0,0011 | 0,0003 | 0,0017 | 0,0012 | 0,0021 | 0,0230 |
| SO_p_<br>2 [_μ_g/m3N] | P98.5<br>1hr | 0,0077 | 0,0028 | 0,0120 | 0,0081 | 0,0120 | 0,1247 |
| SO_p_<br>2 [_μ_g/m3N] | P99<br>día | 0,0022 | 0,0013 | 0,0036 | 0,0025 | 0,0042 | 0,0451 |
| SO_p_<br>2 [_μ_g/m3N] | _x_<br>Año | 0,0011 | 0,0003 | 0,0017 | 0,0012 | 0,0021 | 0,0230 |
| NO2 [_μ_g/m3N] | P99<br>1hr | 0,1366 | 0,0526 | 0,2163 | 0,1402 | 0,2064 | 2,1588 |
| NO2 [_μ_g/m3N] | _x_<br>Año | 0,0181 | 0,0040 | 0,0281 | 0,0200 | 0,0332 | 0,3604 |
| MPS [mg/m2-día] | _x_<br>Mes | 0,0344 | 0,0123 | 0,0576 | 0,0375 | 0,0655 | 59,3808 |
| MPS [mg/m2-día] | _x_<br>Año | 0,0345 | 0,0216 | 0,0563 | 0,0371 | 0,0625 | 48,5856 |
| MP2,5 [_μ_g/m3N] | P98<br>día | 0,0430 | 0,0296 | 0,0531 | 0,0465 | 0,0722 | 1,2110 |
| MP2,5 [_μ_g/m3N] | _x_<br>Año | 0,0220 | 0,0066 | 0,0273 | 0,0239 | 0,0371 | 0,6809 |
| MP10 [_μ_g/m3N] | P98<br>día | 0,4212 | 0,2931 | 0,5171 | 0,4557 | 0,7043 | 12,0012 |
| MP10 [_μ_g/m3N] | _x_<br>Año | 0,2141 | 0,0654 | 0,2630 | 0,2327 | 0,3599 | 6,7460 |
| HC [_μ_g/m3N] | P98<br>día | 0,0016 | 0,0008 | 0,0025 | 0,0018 | 0,0028 | 0,0296 |
| HC [_μ_g/m3N] | _x_<br>Año | 0,0008 | 0,0002 | 0,0013 | 0,0009 | 0,0015 | 0,0168 |
| CO [_μ_g/m3N] | P99<br>1hr | 0,0296 | 0,0115 | 0,0466 | 0,0303 | 0,0444 | 0,4724 |
| CO [_μ_g/m3N] | P99<br>8hr | 0,0201 | 0,0143 | 0,0321 | 0,0211 | 0,0347 | 0,3484 |
| Receptor | Receptor | Centro | Chiu Chiu | H. del Cobre | Marzo 23 | PVK | PMI |
