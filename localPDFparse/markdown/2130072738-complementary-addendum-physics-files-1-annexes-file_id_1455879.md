---
title: Microsoft Word - Informe_dispersion.docx
author: Marcia Romero
date: D:20150310134813-03'00'
language: es
type: report
pages: 22
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Actualización simulación de la dispersión de contaminantes atmosféricos para el Proyecto “Mejoramiento Matriz de Sustentabilidad de Recursos Geológicos, Actualización Modelos Geometalurgicos y Geotécnicos ”
-->

_Ingeniería y Geofísica LTDA_

# Actualización simulación de la dispersión de contaminantes atmosféricos para el Proyecto “Mejoramiento Matriz de Sustentabilidad de Recursos Geológicos, Actualización Modelos Geometalurgicos y Geotécnicos ”

### Marzo de 2015

________________________________________________________________________ 1
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

### Contenido

1 Introducción ..................................................................................................................................... 3

2 Objetivo y características de la modelación ..................................................................................... 4

3 Meteorología .................................................................................................................................... 6

4 Simulaciones de dispersión ............................................................................................................ 14

4.1 Aportes .................................................................................................................................... 14

4.2 Isolíneas de concentración ...................................................................................................... 16

4.3 Análisis de incertidumbres ...................................................................................................... 21

5 Conclusiones ................................................................................................................................... 22

________________________________________________________________________ 2
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

### 1 Introducción

En el Proyecto “Mejoramiento Matriz de Sustentabilidad de Recursos Geológicos, Actualización Modelos
Geometalurgicos y Geotécnicos” se localiza al interior de las servidumbres mineras de la contempla el
uso de nueve máquinas de sondaje. El proyecto mismo se asocia a emisiones de contaminantes
atmosféricas, principalmente por el uso de las máquinas de sondaje. En este informe se evalúa el
impacto en calidad del aire por estas emisiones.

En el siguiente capítulo, se entregan el objetivo del informe y las características de la
modelación. El capítulo 3 resume las características meteorológicas más importantes de la zona. El
capítulo 4 entrega los resultados de la simulación de la dispersión de contaminantes. En los
capítulos 5 y 6 se entregan un análisis de incertidumbre y las conclusiones, respectivamente.

________________________________________________________________________ 3
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

### 2 Objetivo y características de la modelación

El objetivo de este informe es evaluar el impacto del proyecto a través de una modelación
de dispersión de contaminantes.

La modelación se hizo según los criterios de la _Guía_ usando el modelo meteorológico
_Weather Research and Forecasting Model_ (WRF) y el modelo de dispersión CALPUFF. Aparte de la
meteorología, CALPUFF requiere como información de entrada las emisiones en términos de su
magnitud y su ubicación.

Según anexo 16 “Informe Actualización de Estimaciones de Emisiones Atmosféricas por
Polvo Resuspendido”, el peor escenario de las emisiones del proyecto son para el año 2016 y tal

como se indica en la tabla 1.

|Actividad|Emisiones Proyecto<br>[ton/Proyecto]|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Actividad**|**PM10**|**PM2,5**|**CO**|**NOx**|**HC**|
|Escarpes|0,299|0,042||||
|Excavaciones|0,075|0,010||||
|Carga y descarga|0,009|0,001||||
|Resuspendido en Caminos|1,020|0,109||||
|Escapes maquinaria|20,046|20,046|54,677|261,650|24,605|
|Escapes camiones|0,002|0,002|0,032|0,093|0,005|
|**Total Actualización**|**21,451**|**20,211**|**54,709**|**261,742**|**24,610**|

**Tabla 1:** Emisiones de MP10, MP2,5, CO, NOx y HC en toneladas/año para cada una de las fuentes

relevantes del proyecto. Los valores son los que corresponden a las emisiones del año 2016.

La figura 1 muestra la ubicación de la zona del sondaje junto con el camino asociado que

se usará con respecto a las estaciones de monitoreo que se usan para evaluar el impacto. La tabla

2 entrega las coordenadas de estas estaciones.

**Estación** **Longitud** **Latitud**

**Chiu ‐ Chiu** ‐68.650 ‐22.3514

**Centro** ‐68.9284 ‐22.4618

**Servicio Médico Legal** ‐68.9477 ‐22.4605
**Hospital del Cobre** ‐68.9084 ‐22.4506
**Pedro Vergara Keller** ‐68.9331 ‐22.4425

**23 de marzo** ‐68.9377 ‐22.4602

**Tabla 2:** Coordenadas de las estaciones de monitoreo con representatividad poblacional en

longitud‐latitud

________________________________________________________________________ 4
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

**Figura 1:** Ubicación de la zona de sondaje y su camino asociado junto con las estaciones de monitoreo que se usan para evaluar el impacto.

________________________________________________________________________ _meteodata Ltda_
_Domeyko 1864, Santiago_

5

_Ingeniería y Geofísica LTDA_

### 3 Meteorología

Tal como se indica en la _Guía_ el fundamento para la modelación de la dispersión de los
contaminantes atmosféricos es la meteorología. En este capítulo se describen las características
más importantes de la meteorología junto con una evaluación de desempeño del modelo WRF.

Una evaluación detallada se encuentra en el anexo de este informe.

Tal como se mencionó anteriormente, la simulación de WRF representa el año 2012. Cabe
señalar que, según la _Guía_, siempre se debe simular un año y se supone que este año sea
representativo en términos meteorológicos. Es decir, no existe ninguna ventaja o desventaja de
usar un año en particular. En el caso de Radomiro Tomic, existe una base de datos WRF para el año
2012 evaluada lo que hace justamente eficiente cualquier simulación de dispersión dentro del SEIA
lo explica el uso de justamente este año.

La zona cuenta con una red de estaciones meteorológicas muy densa. La figura 2 indica las
ubicaciones de aquellas que se han usado en la evaluación.

**Figura 2:** Ubicación de las estaciones meteorológicas en la zona de interés.

________________________________________________________________________ 6
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

Un rasgo muy importante de la meteorología en la zona son los ciclos diarios. La figura 3
muestra modo del ejemplo de la estación Calama norte estos ciclos de la velocidad y la dirección
del viento; el panel superior entrega el ciclo diario promedio (línea azul) y el rango de 90% de los
datos (sombra celeste) y en el panel inferior, se muestran las frecuencias de las direcciones de

viento a nivel horario.

**Figura 3:** Ciclo diario del viento en estación Calama Norte. El panel superior el ciclo diario

promedio (líneaazul) y el rango de 90% de los datos (sombra celeste). En el panel inferior, se

muestran las frecuencias de las direcciones de viento a nivel horario.

En primer lugar, la figura demuestra de manera muy clara la presencia del ciclo diario en
ambas variables. Durante la noche, la velocidad de viento es baja con valores mínimos de
aproximadamente 5 m/s. Durante el día el viento es más fuerte, generalmente dos a tres veces
más intenso que durante la noche. En este caso, se alcanzan velocidades de aproximadamente 8
m/s. También en términos de la dirección del viento, se observa un ciclo diario muy marcado. Tal
como se describe más adelante, la variabilidad espacial de esta variable es muy alta. En el caso de
la estación Calama Norte, se observa un viento desde el este durante la noche y desde el sur‐oeste
durante el día. Considerando Calama como el punto más crítico en términos de impacto,
generalmente no se observa un flujo de aire con un origen directamente de la faenas de CODELCO.

________________________________________________________________________ 7
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

Mientras la figura 3 se usó a modo de ejemplo, las figuras 4 y 5 ponen en contexto los
ciclos diarios de viento de todas las estaciones a través de los campos de viento a las 05:00 y 17:00
hrs, respectivamente. Las flechas indican hacia donde sopla el viento y los puntos amarrillos la

ubicación de la estación.

Es evidente la diferencia entre los patrones de viento durante el día y la noche. Los vientos
son mucho más fuertes durante el día y, además no existen direcciones de viento que apuntan a
Calama. Generalmente, los vientos dirección suroeste‐oeste durante este periodo. Durante la
noche, los vientos son mucho más débiles y el patrón de viento es más complejo. En este caso sí
existen estaciones que muestran direcciones de viento hacia Calama como por ejemplo Quetena 1
y Pique 2. No obstante, se puede ver muy bien en la figura, que tanto en Quetena 2 y Calama
Norte, las direcciones indican que los flujos no llegan a la ciudad sino son desviadas antes por
parte de un flujo desde el este.

**Figura 4:** Patrón de viento día las 05:00 hrs según las observaciones. Las flechas indican hacia

donde sopla el viento y los puntos amarrillos la ubicación de la estación.

________________________________________________________________________ 8
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

**Figura 5:** Patrón de viento día las 17:00 hrs según las observaciones. Las flechas indican hacia

donde sopla el viento y los puntos amarrillos la ubicación de la estación.

Mientras las figuras 3 ‐ 5 se basan en la información más objetiva que son las
observaciones, no pueden entregar una información con una cobertura espacial completa. Con
fines de lograr esta cobertura, se usan los modelos numéricos, en este caso el modelo WRF. Con
respecto a estos datos, se debe, en primer lugar, compararlos con los datos observacionales.

Nuevamente, se usa la estación Calama Norte a modo de ejemplo para esta comparación.
La figura 6 compara el ciclo diario de la velocidad del viento observado con el de WRF (simulado)
para esta estación. Se puede observar que WRF sobre‐estima la velocidad máxima durante el día.
No obstante, durante la noche que representa el periodo más crítico de transporte de
contaminantes hacia la ciudad de Calama, el desempeño del modelo es muy bueno.

La figura 7 compara los ciclos diarios de la dirección del viento observados con los de WRF

(simulados) también para las estacione Calama Norte. También en este caso, se puede observar

que WRF reproduce muy bien el ciclo.

________________________________________________________________________ 9
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

Tal como indica el anexo a este informe, las características indicadas para la estación

Calama Norte en términos del desempeño de WRF son muy representativas para todas las otras

estaciones evaluadas.

**Figura 6:** Ciclo diario de la velocidad del viento en estación Calama Norte. El panel superior se

muestra el ciclo diario observado, en el panel inferior el simulado por WRF. El ciclo diario

promedio se indica a través de la línea azul y el rango de 90% a través de la sombra celeste.

________________________________________________________________________ 10
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

**Figura 7** : Ciclo diario de la dirección del viento según las observaciones (panel superior) y WRF

(panel inferior). Se muestran las frecuencias de las direcciones de viento a nivel horario.

Finalmente, se usan los datos de WRF para indicar los patrones de viento más importante
en la zona. Las figuras 8 y 9 muestran los patrones de viento según el modelo WRF a las 05:00 y las
17:00 hrs que se consideran horas representativas de los patrones durante la noche y el día,
respectivamente. Tal como en el caso de las observaciones, se puede observar también en este
caso que los vientos durante el día son más fuertes y muestran direcciones dominantes desde el
oeste y suroeste. A contrario a este patrón, los vientos durante la noche son más débiles y el
patrón es más complejo. Esta complejidad se debe a la presencia de vientos catabáticos que
siguen principalmente los rasgos de la topografía. Es así también que se explican los vientos del
este en la zona dentro de Calama y hacia el sur este, que actúan como un “escudo” para la ciudad

________________________________________________________________________ 11
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

en un sentido que previenen que los flujos desde el norte y, por lo tanto, desde el Distrito Norte
(que transportan contaminantes de esta zona hacia Calama) no entren a la ciudad.

**Figura 8** : Patrón de viento según WRF a las 05:00 hrs. Se observan vientos débiles y las direcciones

de viento en función de la pendiente hacia abajo local.

________________________________________________________________________ 12
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

**Figura 9** : Patrón de viento según WRF a las 17:00 hrs. Los vientos son más fuertes que durante la

noche y se muestran direcciones dominantes desde el oeste y suroeste

________________________________________________________________________ 13
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

### 4 Simulaciones de dispersión

El presente documento da cuenta de los resultados obtenidos al modelar la dispersión
atmosférica de las concentraciones de MP10, MP2,5 y NOx para el proyecto “Mejoramiento Matriz
de Sustentabilidad de Recursos Geológicos, Actualización Modelos Geometalurgicos y
Geotécnicos”. El proyecto consta de 3 etapas, construcción, operación y cierre. Como se mencionó
anteriormente, la modelación se realiza para el año 2016, es decir, para el escenario de operación
que constituye el peor escenario.

El área de modelación corresponde a una grilla de 72 x 72 km [2], con un espaciamiento de
1 km., en cuyo interior se encuentra ubicado el sitio de emplazamiento del Proyecto y puntos de
interés. La figura 1 presenta la zona de estudio.

La simulación de las concentraciones de material particulado y gases asociadas al
Proyecto, fueron modeladas según requerimiento de la “Guía para el Uso de Modelos de Calidad
del Aire en el SEIA, 2012” Servicio de Evaluación Ambiental, mediante la aplicación del sistema de
modelación atmosférica “WRF - CALPUFF” definido por la agencia EPA como sistema de referencia
para simular la dispersión de contaminantes provenientes de complejos industriales ubicados en
terreno complejo.

La meteorología utilizada en la modelación, corresponde a la obtenida por medio del
modelo meteorológico de pronóstico Weather Research and Forecasting Model (WRF), la cual será
utilizada como entrada para el modelo de dispersión CALPUFF. Dicha información es referente al
entorno del proyecto y corresponde al periodo comprendido entre el 1 de enero y el 31 de

diciembre del año 2012.

#### 4.1 Aportes

Mediante la aplicación del modelo CALPUFF fue posible obtener las concentraciones de
material particulado, basándose en los campos de vientos generados por la modelación
meteorológica realizada con WRF.

Las tablas 3 a la 5 presentan el resumen de las concentraciones resultantes de la
modelación en los puntos de interés.

De manera general, se observa que los aportes son muy bajos en todas las estaciones.
Siendo siempre máximos en estación PVK y mínimos en Chiu‐Chiu. Para MP10 y MP2,5 las
concentraciones alcanzan valores siempre inferiores a 0.01 μg/m [3] N en promedio e inferiores a
0.03 μg/m [3] N para el percentil 98. Con respecto al NOx, este es el contaminante que muestra
mayores concentraciones, aproximadamente un orden de magnitud mayor al material particulado.
No obstante, las concentraciones siguen siendo muy bajas, manteniéndose bajo 0.13 μg/m [3] N en
promedio y bajo 1.3 μg/m [3] N para percentil 99 horario.

________________________________________________________________________ 14
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

|Estaciones|Concentraciones promedio de<br>MP10 (μg/m3N)|Percentil 98 de las concentraciones<br>de MP10 (μg/m3N)|
|---|---|---|
|**Centro**|0.0081|0.0225|
|**Chiu ‐ Chiu**|0.0035|0.0177|
|**Hospital del Cobre**|0.0087|0.0240|
|**23 de marzo**|0.0086|0.0243|
|**PVK**|0.0112|0.0335|
|**SML**|0.0089|0.0256|

**Tabla 3** : Concentraciones promedio y los percentiles 98 de las concentraciones de MP10 para cada

estación de monitoreo con representatividad poblacional en la zona.

|Estaciones|Concentraciones promedio de<br>MP2,5 (μg/m3N)|Percentil 98 de las concentraciones<br>de MP2,5 (μg/m3N)|
|---|---|---|
|**Centro**|0.0074|0.0208|
|**Chiu ‐ Chiu**|0.0033|0.0165|
|**Hospital del Cobre**|0.0079|0.0223|
|**23 de marzo**|0.0079|0.0224|
|**PVK**|0.0103|0.0312|
|**SML**|0.0082|0.0239|

**Tabla 4** : Concentraciones promedio y los percentiles 98 de las concentraciones de MP2,5 para

cada estación de monitoreo con representatividad poblacional en la zona.

|Estaciones|Concentraciones promedio de<br>NOx (μg/m3N)|Percentil 99 de las concentraciones<br>de NOx (μg/m3N)|
|---|---|---|
|**Centro**|0.0950|0.9485|
|**Chiu ‐ Chiu**|0.0421|0.6993|
|**Hospital del Cobre**|0.1024|1.0514|
|**23 de marzo**|0.1020|0.9944|
|**PVK**|0.1330|1.3052|
|**SML**|0.1056|1.0179|

**Tabla 5** : Concentraciones promedio y los percentiles 99 de las concentraciones de NOx para cada

estación de monitoreo con representatividad poblacional en la zona.

________________________________________________________________________ 15
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

#### 4.2 Isolíneas de concentración

A continuación se presentan las isoconcentraciones obtenidas en la modelación para
MP10, MP2,5 y NOx. Se puede observar que desde la zona de sondaje existe una “bifurcación” del
transporte de los contaminantes la que se puede observar mejor en los 2 contornos más bajos de
todas las figuras promedio: una dirección del flujo es desde la zona del sondaje hacia el sur, la
segunda hacia el este‐sureste. El flujo hacia el sur es desde la zona del sondaje hacia la ciudad de
Calama y el flujo hacia el este‐sureste es hacia Chiu Chiu. No obstante, en el caso de Chiu Chiu
existe un viento con una dirección noreste en la ciudad misma que inhibe el ingreso de los
contaminantes a la ciudad (ver figuras 8). Algo similar ocurre en Calama donde los vientos cerca de
la ciudad desde el este desvían los contaminantes y inhiben su ingreso a las zonas pobladas (ver
figuras 8). A pesar de lo anterior, se puede observar que en promedio las concentraciones en
Calama son bajas (alrededor de 0.01 μg/m [3] N para MP10) y en Chiu Chiu menos de 0.004 μg/m [3] N.

**Escenario de Operación (2015)**

**Figura 10** : Patrón espacial promedio de MP10.

________________________________________________________________________ 16
_meteodata Ltda_
_Domeyko 1864, Santiago_

**Figura 11** : Patrón espacial del percentil 98 de MP10.

_Ingeniería y Geofísica LTDA_

17

________________________________________________________________________
_meteodata Ltda_
_Domeyko 1864, Santiago_

**Figura 12** : Patrón espacial promedio de MP2,5.

_Ingeniería y Geofísica LTDA_

18

________________________________________________________________________
_meteodata Ltda_
_Domeyko 1864, Santiago_

**Figura 13** : Patrón espacial del percentil 98 de MP2,5.

_Ingeniería y Geofísica LTDA_

19

________________________________________________________________________
_meteodata Ltda_
_Domeyko 1864, Santiago_

**Figura 14** : Patrón espacial del promedio de NOx.

_Ingeniería y Geofísica LTDA_

20

________________________________________________________________________
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

**Figura 15** : Patrón espacial del percentil 99 de NOx.

#### 4.3 Análisis de incertidumbres

El objetivo de un análisis de incertidumbre es poner en contexto los resultados de las
simulaciones de dispersión con los errores del modelo meteorológico. De esta manera, se apunta
a evaluar posibles sobre‐ o subestimaciones del modelo de dispersión. En este sentido se observa
que el modelo WRF representa muy bien la meteorología predominante del sector, ya sea para
velocidad de viento o dirección de viento. Debido a lo anterior, se concluye que no existen
antecedentes necesarios para considerar incertidumbres significativas en las concentraciones
presentadas anteriormente, ya sea en las magnitudes o en la dirección de la pluma.

________________________________________________________________________ 21
_meteodata Ltda_
_Domeyko 1864, Santiago_

_Ingeniería y Geofísica LTDA_

### 5 Conclusiones

Según la estimación de emisiones estimadas para este proyecto, las emisiones de material
particulado son al menos tres órdenes de magnitud menores que las emisiones totales en la zona.
Estas bajas emisiones explican el impacto despreciable que tiene el proyecto. En términos de
impacto por material particulado (MP10 y MP2,5) no existe ninguna evidencia que el proyecto
tendrá algún impacto “medible “en las ciudades de Calama y Chiu Chiu en el sentido que el error
de sensibilidad de los sensores para material particulado son mayores que el impacto estimado
por la modelación.

En el caso de NOx, las emisiones son un orden de magnitud mayor que las de material particulado.
Aún así, también en este caso los impactos promedio son menores que 0.1 μg/m [3] N, esto equivale
a un 0.1% de norma para NO 2 (considerando todo el NOx como NO 2 ), por lo que deben ser
considerados despreciables.

________________________________________________________________________ 22
_meteodata Ltda_
_Domeyko 1864, Santiago_

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3: ** : Concentraciones promedio y los percentiles 98 de las concentraciones de MP10 para cada**

| Estaciones | Concentraciones promedio de<br>MP2,5 (μg/m3N) | Percentil 98 de las concentraciones<br>de MP2,5 (μg/m3N) |
| --- | --- | --- |
| **Centro** | 0.0074 | 0.0208 |
| **Chiu ‐ Chiu** | 0.0033 | 0.0165 |
| **Hospital del Cobre** | 0.0079 | 0.0223 |
| **23 de marzo** | 0.0079 | 0.0224 |
| **PVK** | 0.0103 | 0.0312 |
| **SML** | 0.0082 | 0.0239 |

**Tabla 4: ** : Concentraciones promedio y los percentiles 98 de las concentraciones de MP2,5 para**

| Estaciones | Concentraciones promedio de<br>NOx (μg/m3N) | Percentil 99 de las concentraciones<br>de NOx (μg/m3N) |
| --- | --- | --- |
| **Centro** | 0.0950 | 0.9485 |
| **Chiu ‐ Chiu** | 0.0421 | 0.6993 |
| **Hospital del Cobre** | 0.1024 | 1.0514 |
| **23 de marzo** | 0.1020 | 0.9944 |
| **PVK** | 0.1330 | 1.3052 |
| **SML** | 0.1056 | 1.0179 |
