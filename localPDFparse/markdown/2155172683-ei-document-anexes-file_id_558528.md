---
title: iembre 30 de 2011
author: Valeria P. Campos Bravo
date: D:20220216184520-03'00'
language: es
type: report
pages: 49
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 
  - 
-->

###### INFORME DE INVENTARIO Y MODELACIÓN DE OLORES PROYECTO: “ACTUALIZACIÓN SISTEMA DE TRATAMIENTO DE RESIDUOS LÍQUIDOS INDUSTRIALES DE PLANTA SANTA MARÍA”

_Preparado por:_

_Para:_

Febrero, 2022

###### INFORME DE RESULTADOS ATM 077-22 INFORME DE INVENTARIO Y MODELACIÓN DE OLORES “ACTUALIZACIÓN SISTEMA DE TRATAMIENTO DE RESIDUOS LÍQUIDOS INDUSTRIALES DE PLANTA SANTA MARÍA”

_Preparado para:_

|Versión del Documento|Col2|Col3|Col4|1|Col6|
|---|---|---|---|---|---|
|**_Responsable Elaboración_**|**_Responsable Elaboración_**|**_Responsable Revisión_**|**_Responsable Revisión_**|**_Responsable Aprobación_**|**_Responsable Aprobación_**|
|Nombre:|Sebastián Díaz.|Nombre:|Matías de la Parra|Nombre:|Sebastián Díaz.|
|Cargo:|Gerente Técnico|Cargo|Jefe de Área|Cargo:|Gerente Técnico|
|Fecha:|11-02-2022|Fecha:|11-02-2022|Fecha:|11-02-2022|
|Firma:||Firma:||Firma:||

Febrero, 2022

**ÍNDICE DE CONTENIDOS**

1 Introducción ....................................................................................... 1

1.1 Alcances ............................................................................................ 3
2 Marco Legal ....................................................................................... 5
3 Meteorología de la Zona de Estudio ....................................................... 6
3.1 Series de Tiempo ................................................................................ 7
3.2 Rosas de Viento .................................................................................. 8

3.3 Ciclo Estacional.................................................................................. 11

3.4 Ciclo Diario Velocidad del Viento .......................................................... 12
3.5 Análisis de Incertidumbre ................................................................... 14
3.6 Descripción de Parámetros Estadísticos................................................. 14
3.6.1 Media ............................................................................................... 14

3.6.2 Moda ............................................................................................... 15

3.6.3 Mediana ............................................................................................ 15
3.6.4 Desviación Estándar ........................................................................... 15
3.6.5 Raíz del Error Cuadrático Medio ........................................................... 15
3.6.6 Error Medio Cuadrático ....................................................................... 16
3.6.7 Sesgo ............................................................................................... 16
3.6.8 Coeficiente de correlación ................................................................... 16
3.7 Análisis cuantitativo ........................................................................... 17
4 Estimación de Emisiones del Proyecto ................................................... 19
4.1 Fuentes Emisoras ............................................................................... 19
4.2 Factores de Emisión ........................................................................... 20
4.3 Tasas de Emisión ............................................................................... 23
5 Modelación de Dispersión de Contaminantes ......................................... 24
5.1.1 Base Teórica ..................................................................................... 24
5.1.2 Sistema de Modelación WRF - CALPUFF ................................................ 24
5.2 Variables de Entrada ingresados al Sistema de Modelación ...................... 26
6 Resultados Modelación ....................................................................... 31
6.1 Campos de Viento .............................................................................. 31
6.2 Aportes Obtenidos de la Modelación ..................................................... 36
6.2.1 Aporte en Puntos de Interés ................................................................ 36
6.2.2 Ajustes de Resultados de la Modelación por Incertidumbre ...................... 38
6.3 Mapas de Isoconcentraciones .............................................................. 40
7 Área de Influencia .............................................................................. 43

8 Conclusiones ..................................................................................... 44
9 Bibliografía ........................................................................................ 45

_**Inventario y modelación de Olores ATM077-22**_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**ÍNDICE DE FIGURAS**

Figura N° 1 Ubicación del Proyecto y Área de Modelación ............................................ 4
Figura N° 2 Serie temporal horaria velocidad del viento - Estación Los Andes Periodo
enero a diciembre 2021 .......................................................................................... 7
Figura N° 3 Frecuencia de ocurrencia dirección del viento - Estación Los Andes Periodo
enero a diciembre 2021 .......................................................................................... 8
Figura N° 4 Rosa de Viento Ciclo Completo Estación Los Andes Periodo enero a diciembre
2021 ................................................................................................ 9
Figura N° 5 Variabilidad temporal del viento - Estación Los Andes Periodo enero a
diciembre 2021 ............................................................................................... 10
Figura N° 6 Variabilidad estacional del viento - Estación Los Andes Periodo 01 enero 2021
- 31 diciembre 2021 ............................................................................................. 11
Figura N° 7 Ciclos Diarios de Velocidad (m/s) y Dirección del Viento (°) Estación Los
Andes (Observado v/s Modelado) Periodo enero a diciembre 2021 .............................. 13
Figura N° 8 Ventajas de la Tecnología de Vermifiltración (Extracto) ............................ 20
Figura N° 9 Ubicación de las Fuentes de Emisión Actual y con Proyecto ....................... 22
Figura N° 10 Uso de Suelo ..................................................................................... 27
Figura N° 11 Topografía Área de Modelación ............................................................ 28
Figura N° 12 Ubicación Puntos de Interés ................................................................ 30
Figura N° 13 Campos de Viento a las 00:00 horas. ................................................... 32
Figura N° 14 Campos de Viento a las 06:00 horas .................................................... 33
Figura N° 15 Campos de Viento a las 12:00 horas .................................................... 34
Figura N° 16 Campos de Viento a las 18:00 horas. ................................................... 35
Figura N° 17 Percentil 98 de 1 Hora Escenario Actual ................................................ 41
Figura N° 18 Percentil 98 de 1 Hora Escenario con Proyecto ....................................... 42
Figura N° 19 Área de Influencia .............................................................................. 43

**ÍNDICE DE TABLAS**

Tabla N° 1 Coordenadas de los Vértices del Área de Modelación .................................. 2

Tabla N° 2 Normas de Calidad del Aire Consideradas en el Estudio .............................. 5
Tabla N° 3 Localización de Referencia y Variables Meteorológicas Monitoreadas............. 6
Tabla N° 4 Estadísticas de Datos Meteorológicos Monitoreados .................................... 7
Tabla N° 5 Velocidad Promedio del Viento en m/s ..................................................... 14
Tabla N° 6 Valores de los indicadores estadísticos observados y modelados ................. 17
Tabla N° 7 Estadígrafos de evaluación de desempeño del modelo Velocidad del Viento .. 17
Tabla N° 8 Fuentes Emisoras de Olor Actual y con Proyecto ....................................... 19
Tabla N° 9 Tasas de Emisión Biofiltro Jucosol ........................................................... 23
Tabla N° 10 Características del Uso de Suelo ........................................................... 26
Tabla N° 11 Localización Puntos Discretos ............................................................... 29
Tabla N° 12 Aporte Planta Jucosol Escenario Actual .................................................. 36
Tabla N° 13 Aporte Planta Jucosol Quilicura Escenario Proyecto .................................. 37
Tabla N° 14 Aporte Planta Jucosol con Incertidumbre Escenario Actual ........................ 39
Tabla N° 15 Aporte Planta Jucosol con Incertidumbre Escenario con Proyecto .............. 39

_**Inventario y modelación de Olores ATM077-22**_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**1** **Introducción**

La empresa Jucosol ubicada en San Felipe en la Región de Valparaíso, se dedica a
la producción de jugo concentrado de uva desde 1975, también conocido como
mosto.

Actualmente la empresa Jucosol opera un biofiltro de lombrices para el
tratamiento de sus aguas de proceso, sin embargo, pretenden ampliar su
capacidad de tratamiento de agua adicionando 4 unidades de biofiltros que
poseen las mismas características del que ya está instalado, obteniendo así 5
unidades de biofiltros operativos.

A solicitud de DAES, Algoritmos y Mediciones Ambientales SpA, realizó el Servicio
de Predicción de Impacto por Olores para proyecto “Actualización Sistema de
Tratamiento de Residuos Líquidos Industriales de Planta Santa María”. Para
realizar la predicción de impactos, primero se realizó la búsqueda de los factores
de emisión de olores para los biofiltros. La segunda parte corresponde a la
modelación de los impactos de olor a través del sistema WRF-CALPUFF, donde se
modeló el escenario actual y el escenario con proyecto.

El área de modelación corresponde a una grilla de 12 km x 13 km, un
espaciamiento de 1 km y en cuyo interior se encuentra ubicado el sitio de
emplazamiento de la planta y los puntos de interés.

La siguiente tabla muestra las coordenadas de los vértices del área de
modelación.

_**Inventario y modelación de Olores ATM077-22**_ _1/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

_**Tabla N° 1**_
_**Coordenadas de los Vértices del Área de Modelación**_ _**[a]**_

|Vértice|Coordenadas UTMa|Col3|
|---|---|---|
|**Vértice**|**Este (m)**|**Norte (m)**|
|Noreste|352.440|6.376.880|
|Noroeste|340.418|6.376.696|
|Sureste|352.641|6.363.916|
|Suroeste|340.617|6.363.728|

Fuente: Algoritmos SpA, 2022.

Las directrices para la predicción de impactos del presente documento provienen
de la “Guía para la Predicción y Evaluación de Impactos por Olor en el SEIA. La
modelación para la predicción de impactos se desarrolló en base a la “Guía para
el Uso de Modelos de Calidad del Aire en el SEIA, 2012” del Servicio de
Evaluación Ambiental. Esta Guía indica como opción la aplicación del sistema de
modelación atmosférica “WRF - CALPUFF”, sistema de modelación que a su vez
está definido por la agencia EPA como sistema de referencia para simular la
dispersión de contaminantes provenientes de centros industriales ubicados en
terreno complejo.

La meteorología utilizada en el sistema de modelación se obtuvo por medio del
modelo meteorológico de pronóstico Weather Research and Forecasting Model
(WRF), con todos los parámetros indicados en la “Guía para el Uso de Modelos de
Calidad del Aire en el SEIA, 2012”. Dicha información es referente al entorno del
proyecto y corresponde al periodo comprendido entre el 1 de enero 2021 hasta el
31 de diciembre 2021.

En la Figura N° 1 se presenta el mapa con la ubicación del proyecto y el área de
modelación.

a Coordenadas tomadas según Datum WGS-84

_**Inventario y modelación de Olores ATM077-22**_ _2/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**1.1** **Alcances**

 Obtener las emisiones de los biofiltros para agregar al modelo para el
escenario con proyecto.

 Realizar el modelo meteorológico WRF y validarlo mediante la comparación
con datos monitoreados.

 Obtener aportes en concentración e isoconcentraciones de olor con el
sistema de modelación WRF-CALPUFF, en cada punto de interés ingresado
al modelo y para cada escenario.

_**Inventario y modelación de Olores ATM077-22**_ _3/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

_**Figura N° 1**_
_**Ubicación del Proyecto y Área de Modelación**_

Fuente: Algoritmos SpA, 2022.

_**Inventario y modelación de Olores ATM077-22**_ _4/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**2** **Marco Legal**

Debido que la legislación chilena hoy en día no cuenta con límites normativos
para concentraciones de olor como inmisión, se decidió buscar dentro de la
legislación internacional límites de olor para evaluar los resultados del modelo de
dispersión. Dentro de las normas consultadas se seleccionó la de los Países Bajos
con el estadístico percentil 98 de 1 hora. La siguiente tabla tiene el valor límite de
la norma:

_**Tabla N° 2**_

_**Normas de Calidad del Aire Consideradas en el Estudio**_

|País|Estadístico|Límite de<br>concentración de<br>olor (OUE/m3)|Referencia|
|---|---|---|---|
|Países Bajos|Percentil 98<br>horario|0,5|Brancher et al, 2016|

Fuente: Algoritmos SpA 2022.

_**Inventario y modelación de Olores ATM077-22**_ _5/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**3** **Meteorología de la Zona de Estudio**

Las variables meteorológicas de mayor incidencia en la dispersión de las
emisiones atmosféricas generadas por el Proyecto fueron obtenidas por medio del
modelo meteorológico de pronóstico Weather Research and Forecasting Model
(WRF).

Este modelo es recomendado por la “Guía para el uso de modelos de calidad del
aire en el SEIA”, para la generación de datos meteorológicos, ya que, según
indica, es uno de los modelos meteorológicos de pronóstico más avanzados y
completos, siendo empleado en la mayoría de los proyectos relacionados con
modelación atmosférica encargados por organismos estatales como el Ministerio
del Medio Ambiente (MMA) y la ex Comisión Nacional de Energía (CNE) (ahora
Ministerio de Energía).

El WRF es un sistema de predicción numérico de mesoescala no hidrostático
(considera los movimientos verticales), usado con fines de pronóstico operacional
y en investigación de la atmósfera. Los principales componentes de este modelo
son las fuentes externas de datos, como son los datos de entrada y la
información geográfica, el sistema de pre-procesamiento, el modelo WRF-ARW y
los sistemas de post-procesamiento.

Las fuentes externas de datos contienen información necesaria para inicializar
WRF. Éstos corresponden a las observaciones convencionales o satélites de la
atmósfera. De estos datos se obtienen las condiciones iniciales y de borde para
las simulaciones del WRF. También es necesario entregarle datos sobre el terreno
que contengan información sobre la orografía, uso de suelo, relieve y vegetación,
entre otros.

Los modelos meteorológicos al representar una aproximación de la realidad
tienen asociados errores e incertidumbres, es por este motivo que los resultados
obtenidos mediante la modelación con WRF serán comparados con las variables
meteorológicas registradas por la estación Los Andes con el fin de evaluar la
capacidad predictiva del modelo.

La Tabla N° 3 presenta las coordenadas de localización y las variables
meteorológicas monitoreadas en la estación antes mencionada

_**Tabla N° 3**_
_**Localización de Referencia y Variables Meteorológicas Monitoreadas**_

|Estación|Coordenadas UTM|Col3|Variables|Periodo|
|---|---|---|---|---|
|**Estación**|**Norte (m)**|**Este (m)**|**Este (m)**|**Este (m)**|
|Los Andes|351.534|6.364.623|Velocidad del viento<br>Dirección del viento|01 de enero al 31 de<br>diciembre 2021|

Fuente: Información obtenida de Sistema de Información Nacional de Calidad del Aire (SINCA).

_**Inventario y modelación de Olores ATM077-22**_ _6/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

En las siguientes secciones se realiza un análisis comparativo entre la data
meteorológica registrada por la estación de monitoreo y lo simulado con WRF
para el periodo de registro (ver Tabla N° 3), con resolución horaria para las
variables meteorológicas de velocidad y dirección de viento, ya que estos
parámetros influyen directamente en el fenómeno de dispersión de
contaminantes.

**3.1** **Series de Tiempo**

La Tabla N° 4 muestra los porcentajes de datos válidos y de calmas monitoreados
por la Estación Los Andes. Respecto a la velocidad del viento se consideró como
calma los registros menores a 0,5 (m/s).

_**Tabla N° 4**_
_**Estadísticas de Datos Meteorológicos Monitoreados**_

|Estación|Datos<br>Totales|Porcentaje de Calma (%)|Col4|Porcentaje Datos<br>Válidos (%)|
|---|---|---|---|---|
|**Estación**|**Datos**<br>**Totales**|**Periodo**<br>**Diurno**|**Periodo**<br>**Nocturno**|**Periodo**<br>**Nocturno**|
|Los Andes|8.704|11%|38%|100|

Fuente: Algoritmos SpA, 2022.

La serie temporal de la velocidad del viento registrada por la Estación Los Andes,
permiten un análisis cualitativo de los datos en términos de variabilidad, amplitud
de rango y frecuencia de los datos con que se cuenta. No se presentan las series
temporales generadas por el modelo WRF, ya que la información de pronóstico
dispone de la totalidad de los datos.

_**Figura N° 2**_
_**Serie temporal horaria velocidad del viento - Estación Los Andes**_

_**Periodo enero a diciembre 2021**_

Fuente: Algoritmos SpA, 2022.

_**Inventario y modelación de Olores ATM077-22**_ _7/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

La serie temporal de la velocidad del viento registrada por la estación Los Andes
muestra un leve ciclo anual, con las máximas velocidades registradas entre
septiembre y marzo, correspondiendo a los meses de primavera y verano, y las
mínimas velocidades entre abril y agosto, centradas en el periodo de otoño
invierno.

Con respecto a la dirección del viento, se identifican dos patrones dominantes. El
primero de ellos corresponde a vientos preferentemente desde el Norte Noreste
(NNE) correspondiente a la línea centrada entre 0 y 60°. El segundo corresponde
a vientos desde el Oeste Suroeste (OSO), correspondiente s la línea centrada en
240°.

_**Figura N° 3**_
_**Frecuencia de ocurrencia dirección del viento - Estación Los Andes**_

_**Periodo enero a diciembre 2021**_

Fuente: Algoritmos SpA, 2022.

**3.2** **Rosas de Viento**

A continuación, se muestran los campos de viento anual y para diferentes
periodos del día, los que muestran la variabilidad temporal del viento durante el
periodo desde enero a diciembre del 2021 para la Estación Los Andes y la
modelación generada con WRF para dicha estación.

_**Inventario y modelación de Olores ATM077-22**_ _8/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

_**Figura N° 4**_
_**Rosa de Viento Ciclo Completo Estación Los Andes**_

_**Periodo enero a diciembre 2021**_

|Observado|Modelado|
|---|---|
|||

Fuente: Algoritmos SpA, 2022.

La rosa de viento del lado izquierdo de la Figura N° 4, corresponde a los registros
de la Estación Los Andes en la cual se puede observar que prevalecen con mayor
frecuencia vientos desde Norte Noreste (NNE) y Noreste (NE) explicando en
conjunto un 59% de la frecuencia total. En menor medida se observan vientos
desde el Oeste Suroeste (OSO), explicando el 10% de la frecuencia total.

Con respecto a lo modelado con WRF (lado derecho de la Figura N° 4) se obtiene
el mismo patrón de vientos observados, sin embargo se subestima la frecuencia
de ocurrencia de los vientos desde el Norte Noreste (NNE) y sobrestima los
vientos desde el Este Noreste (ENE), sin embargo, ambos provienen desde el
mismo cuadrante.

_**Inventario y modelación de Olores ATM077-22**_ _9/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

_**Figura N° 5**_
_**Variabilidad temporal del viento - Estación Los Andes**_

_**Periodo enero a diciembre 2021**_

|Col1|00:00 - 05:00 horas|06:00 - 11:00 horas|12:00 - 17:00 horas|18:00 - 23:00 horas|
|---|---|---|---|---|
|**_Observado_**|||||
|**_Modelado_**||<br>|||

Fuente: Algoritmos SpA, 2022.

_**Inventario y modelación de Olores ATM077-22**_ _10/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

Al observar el comportamiento espacial de los vientos en los diferentes periodos
del día para la Estación Los Andes (parte superior de la Figura N° 5) se puede
apreciar que, principalmente a lo largo del todo el día se registran vientos desde
el Norte Noreste (NNE), excepto en el periodo desde las 12:00 y 17:00 donde el
viento preferentemente proviene desde el Oeste Suroeste (OSO).

**3.3** **Ciclo Estacional**

La Figura N° 6 muestra la evolución estacional y diaria de la velocidad y dirección
del viento, presentando en el eje “x” las horas del día y en el eje “y” los meses
del año. Es posible observar un patrón diario representativo, correspondiendo a
vientos débiles en horas de la noche y madrugada, con valores que varían entre
0,5 y 1 m/s a lo largo de todo el año. Para el horario diurno, se observan los
máximos valores entre 14:00 y 17:00 horas, siendo levemente más intensas las
velocidades en primavera verano con valores que alcanzan los 3 m/s a diferencia
del periodo invernal donde las velocidades no sobrepasan los 2 m/s.

En cuanto a la dirección del viento observado por la estación Los Andes, se
obtienen vientos desde el Norte Noreste (NNE) principalmente entre las 00:00 y
08:00 horas a lo largo de todo el año. Mientras que en las horas del prevalecen
vientos desde el Oeste Suroeste (OSO).

_**Figura N° 6**_
_**Variabilidad estacional del viento - Estación Los Andes**_

_**Periodo 01 enero 2021 - 31 diciembre 2021**_

|Observado|Modelado|
|---|---|
|||

Fuente: Algoritmos SpA, 2022.

_**Inventario y modelación de Olores ATM077-22**_ _11/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**3.4** **Ciclo Diario Velocidad del Viento**

A continuación, se presentan los ciclos diarios promedio de la velocidad y
dirección del viento monitoreada por la Estación Los Andes y lo modelado con
WRF para dicha estación.

Al apreciar la curva de velocidad promedio para la Estación Los Andes (lado
izquierdo superior de la Figura N° 7), esta presenta una condición homogénea a
lo largo de la madrugada, con una velocidades menores a 1 m/s, aumentando a
partir de las 10:00 horas hasta alcanzar el máximo alrededor de las 16:00 horas
alcanzando un valor de 2,1 m/s. De los datos modelados se obtiene un ciclo
similar, con un máximo igual a 2,5 m/s.

Respecto de la dirección del viento (parte inferior izquierda de la Figura N° 7) se
observa un marcado ciclo diario con vientos desde el Norte Noreste (NNE) entre
las 00:00- 09:00 y 18:00 y 00:00 horas. Por otro lado, durante las horas de
máxima velocidad, el viento viene preferentemente desde el Oeste Suroeste
(OSO).

_**Inventario y modelación de Olores ATM077-22**_ _12/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

_**Figura N° 7**_
_**Ciclos Diarios de Velocidad (m/s) y Dirección del Viento (°)**_

_**Estación Los Andes (Observado v/s Modelado)**_

_**Periodo enero a diciembre 2021**_

|Observado|Modelado|
|---|---|
|||

Fuente: Algoritmos SpA, 2022.

_**Inventario y modelación de Olores ATM077-22**_ _13/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**3.5** **Análisis de Incertidumbre**

La Tabla N° 5 presenta las diferencias entre las observaciones y los pronósticos
de los valores promedios de velocidad de viento para el periodo diurno y nocturno
para la Estación Los Andes.

_**Tabla N° 5**_
_**Velocidad Promedio del Viento en m/s**_

|Estación|Periodo|Promedio<br>Observación|Promedio<br>Pronóstico WRF|%<br>Sobrestimado<br>por pronóstico|
|---|---|---|---|---|
|Los Andes|Diurno|1,25|1,40|11%|
|Los Andes|Nocturno|0,95|1,52|38%|

Fuente: Algoritmos SpA, 2022.

Al comparar los ciclos diarios promedios observados y de pronóstico para la
Estación Los Andes, se evidencia que el modelo reproduce correctamente la
trayectoria del viento, presentando la mayor diferencia en el horario nocturno,
sobrestimando en 38% los valores modelados situación que genera condiciones
favorables con respecto a la ventilación en el área de interés, ya que la
meteorología generada por el modelo WRF al ser utilizada como dato de entrada
para el modelo de dispersión CALPUFF. Este último sobrestimaría el valor de la
concentración de los contaminantes.

**3.6** **Descripción de Parámetros Estadísticos**

**3.6.1** **Media**

Valor característico de una serie de datos cuantitativos, se obtiene a partir de la
suma de todos sus valores dividida entre el número de sumandos. Cuando el
[conjunto es una muestra aleatoria recibe el nombre de media muestral siendo](https://es.wikipedia.org/wiki/Muestra_aleatoria)
[uno de los principales estadísticos muestrales.](https://es.wikipedia.org/wiki/Estad%C3%ADstico)

###### 1

# 

_n_

###### x = _[x] i_ _n_

###### = n =

_i_

1

_**Inventario y modelación de Olores ATM077-22**_ _14/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**3.6.2** **Moda**

Corresponde al valor que cuenta con una mayor frecuencia en una distribución de
datos, es decir, el número más repetido.

**3.6.3** **Mediana**

La mediana es la medida más robusta, resistente y más común de la tendencia
central de la distribución de datos. A diferencia de la media no se ve afectada por
valores extremos que pudieran ser anómalos.

**3.6.4** **Desviación Estándar**

Corresponde a la raíz cuadrada de la diferencia media cuadrática entre el error de
pronóstico y el error de pronóstico promedio (E). Se utiliza para medir la cantidad
de variabilidad en el pronóstico de variables meteorológicas. Cuanto mayor sea el
valor de la SD, mayor será la variabilidad del pronóstico

Para realizar la validación de los datos registrados por la estación Camanchaca,
se calculan diferentes estadísticos clásicos tales como:

**3.6.5** **Raíz del Error Cuadrático Medio**

Corresponde al cálculo de la raíz cuadrada del promedio de las diferencias
cuadradas de cada una de los valores del pronóstico y la observación. Este
cálculo permite ponderar los errores positivos y negativos, por lo cual en él están
incluidos los errores sistemáticos y aleatorios de los modelos.

Dónde:

X 1i : es el valor de la serie No 1

_**Inventario y modelación de Olores ATM077-22**_ _15/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

x 2i : es el valor de la serie No2

N: es el número de valores analizado

**3.6.6** **Error Medio Cuadrático**

El error medio cuadrático entrega las medidas de las diferencias en promedio
entre los valores modelados y los observados. Está definido como:

**3.6.7** **Sesgo**

Proporciona información sobre la tendencia del modelo a sobreestimar o
subestimar una variable, cuantificando el error sistemático del modelo.

##### N ( x 1 i − x 2 i BIAS =

##### ( x 1 i − x 2 i )

##### 1 i − =
# 

##### _N_

_i_

= 1

**3.6.8** **Coeficiente de correlación**

Nos permite establecer la relación lineal entre los modelos utilizados y la
observación y está acotada entre -1 y 1.

_N_

##  ( x 1 i − x 1 () x 2 i −

_i_ = 1
###### =

###### ( x 1 − x 1 () x 2 − x 2 )

###### x − x x − x

1 _i_ 1 2 _i_

_i_ = 1
###### Corr =

1 _i_ 1

_i_

_i_

_i_

1 _i_ 1 2 _i_ 2

1

=

###### − ( N )1

1 2

###### − N )1 S S

###### −

Si Corr < 0 significa que las dos variables se correlacionan en sentido inverso. A
valores altos de una de ellas le suelen corresponder valor bajos de la otra y
viceversa. Si Corr > 0 las dos variables se correlacionan en sentido directo.A
valores altos de una le corresponden valores altos de la otra. Si corr = 0 se dice
que las variables están incorrelacionadas por lo tanto no puede establecerse
ningún sentido de covariación.

_**Inventario y modelación de Olores ATM077-22**_ _16/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**3.7** **Análisis cuantitativo**

Tanto la velocidad como la dirección del viento son variables meteorológicas
relevantes para el análisis de los datos de entrada del modelo y a objeto de
observar la dirección de las masas de aire. Debido a lo anterior, a continuación,
se presenta en la Tabla N° 6 los resultados obtenidos al aplicar los estadísticos a
los datos observados y modelados para la velocidad del viento en cada estación
evaluada.

_**Tabla N° 6**_
_**Valores de los indicadores estadísticos observados y modelados**_

|Estadísticos|Unidad|Los Andes|Col4|
|---|---|---|---|
|**Estadísticos**|**Unidad**|**observado**|**modelado**|
|Media|m/s|1,11|1,46|
|Máximo|m/s|6,36|10,32|
|Mínimo|m/s|0,00|0,01|
|Moda|m/s|0,15|1,05|
|Mediana|m/s|0,93|1,27|
|Desviación estándar|--|0,85|0,86|

Fuente: Algoritmos SpA, 2022

Para complementar el análisis cualitativo, se presenta en la Tabla N° 7 un análisis
cuantitativo de las variables velocidad del viento que compara los valores
observados y modelados por medio de la utilización de tres estadígrafos
comúnmente utilizados para la evaluación del desempeño de modelos; Sesgo,
Error Cuadrático Medio y el coeficiente de correlación (r).

A continuación, se los estadígrafos de evaluación de desempeño del modelo WRF
respecto a los datos monitoreados por la estación Los Andes.

_**Tabla N° 7**_
_**Estadígrafos de evaluación de desempeño del modelo**_

_**Velocidad del Viento**_

|Estación|Serie de datos|Medida de Error|Col4|Col5|
|---|---|---|---|---|
|**Estación**|**Serie de datos**|**Sesgo**|**RMSE**|**Corr**|
|Los Andes|Serie de Tiempo|0,35|0,92|0,50|
|Los Andes|Ciclo Diario|0,35|0,48|0,77|

Fuente: Algoritmos SpA, 2022.

_**Inventario y modelación de Olores ATM077-22**_ _17/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

En base a lo anteriormente expuesto respecto de la meteorología, es posible
concluir que el modelo representa de manera satisfactoria la dinámica del viento
observado ya que este reproduce un ciclo anual de la velocidad junto a los
patrones en la dirección, sin embargo este sobrestima los valores nocturnos. En
relación a los estadísticos evaluados, se obtiene un bajo sesgo, con un valor de
error igual a 0,35 m/s para el ciclo diario. Finalmente al evaluar la correlación,
obtenemos un valor superior a 0,57 tanto en la serie temporal anual como en el
ciclo diario.

_**Inventario y modelación de Olores ATM077-22**_ _18/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**4** **Estimación de Emisiones del Proyecto**

En esta sección se describirán las actividades que emiten olor en la planta de
Jucosol, además se obtendrán las emisiones de estas fuentes que serán
ingresadas al modelo con el fin de predecir el impacto de los olores en los
receptores cercanos.

**4.1** **Fuentes Emisoras**

La Tabla N° 8 presenta las fuentes emisoras de olor de la planta Jucosol.

_**Tabla N° 8**_
_**Fuentes Emisoras de Olor Actual y con Proyecto**_

|Escenario|Tipo de Fuente|Fuentes Emisoras|
|---|---|---|
|Actual|Areales|• <br>1 Biofiltro|
|Proyecto|Proyecto|• <br>5 Biofiltros|

Fuente: Algoritmos SpA, 2022

Para el escenario actual se considera 1 fuente que consiste en un Biofiltro de
lombrices que trata el agua de proceso, para el escenario con proyecto se
considera el biofiltro actual más 4 unidades nuevas. Cada biofiltro considera una
superficie de 200 m [2], son equipos techados con paredes de alto de 1,2 metros
donde el resto de la pared es una malla metálica.

Los biofiltros de lombrices usan la técnica de vermifiltración que emplea
lombrices de tierra en un lecho filtrante. La integración de lombrices de tierra en
el proceso de filtración de aguas residuales ha evolucionado como una alternativa
ecológica y económica al proceso convencional de aguas residuales (Bhavini,
Kanaujia, Trivedi, & Hait, 2020). La vermifiltración no necesita energía externa
(excepto el bombeo), es de bajo costo y no produce lodos.

En la vermifiltración el cuerpo de la lombriz funciona como un biofiltro y prolonga
el metabolismo microbiano aumentando su población. El efluente resultante se
vuelve altamente nutritivo y puede reutilizarse con fines de riego. Las lombrices
de tierra son devoradores de desechos y descomponedores versátiles. Promueven
el crecimiento de bacterias de descomposición beneficiosas en aguas residuales
domésticas y actúan como aireador, triturador, degradador químico y estimulador
biológico. Los dos procesos, proceso microbiano y proceso vermi, funcionan
simultáneamente en el tratamiento de aguas residuales utilizando lombrices de
tierra. Las lombrices de tierra estimulan y aceleran aún más la actividad
microbiana al aumentar la población de microorganismos del suelo y también a
través de una mejor aireación (Kumar, Rajpal, Bhargava, & Prasad, 2013).

_**Inventario y modelación de Olores ATM077-22**_ _19/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**4.2** **Factores de Emisión**

Respecto a los factores de emisión de olor para biofiltros de lombrices o
vermifiltros no se encontró información sobre ellos, no obstante, esto se debe a
que variados estudios indican que los vermifiltros no producen olor. A
continuación se muestran los estudios que abalan esta indicación.

Las ventajas de la tecnología de vermifiltración incluyen la rentabilidad, la
tecnología socialmente aceptable y sin olores con una eficacia de alto rendimiento
(Arora & Saraswat, 2021). Para los vermifiltros tampoco hay problema de malos
olores durante el procesamiento (Kumar, Rajpal, Bhargava, & Prasad, 2013). En
la siguiente imagen se observa un diagrama de las ventajas de la tecnología de
vermifiltración de aguas la cual indica: _“No se produce olor durante el_
_tratamiento ya que es una tecnología aeróbica y no se produce formación de_
_lodos. Por lo tanto esto no genera la necesidad de tratamiento de lodos_
_excedentes y su costo de disposición”_

_**Figura N° 8**_
_**Ventajas de la Tecnología de Vermifiltración (Extracto)**_

Fuente: (Arora & Saraswat, 2021)

En un estudio sobre la reutilización de las aguas residuales y la recolección de las
excretas porcinas, se indica que la concentración de contaminante en el agua del
tanque después del vermifiltrado al final del experimento se mantuvo menor que
la del líquido después del tamizado, el amoníaco se eliminó del líquido mediante
una rápida adsorción sobre la materia orgánica después de la aspersión y una
organización progresiva por parte de la biomasa. Esta eliminación de amoníaco
fue sin duda la causa de la importante disminución (en torno al 50%) de las
emisiones de amoníaco del edificio. El olor del efluente se eliminó al pasar por el
vermifiltro (Li, y otros, 2007). El pH en las aguas residuales puede ser casi
neutralizado por las lombrices de tierra y hay muy poco o ningún problema de
malos olores durante el procesamiento. (Kumar, Rajpal, Bhargava, & Prasad,
2013).

En otra investigación se estudia un modelo de vermifiltro a escala de laboratorio
para tratar las aguas grises, donde se utilizó un sistema de suministro por lotes
en el diseño experimental para investigar las condiciones necesarias para el
correcto funcionamiento del sistema de vermifiltración para áreas de clima cálido.

_**Inventario y modelación de Olores ATM077-22**_ _20/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

Donde se encontró que los vermifiltros tenían materia orgánica potencial libre de
olores y los lodos de las lombrices se pueden recolectar cada 6-8 meses para
usarlos como fertilizante para la agricultura y la alimentación de aves,
respectivamente. En lo que respecta al olor, no hubo problemas de olores en el
vermifiltro en comparación con la unidad de control. La lombriz Eudrilus eugeniae
predominantemente disponible toleró temperaturas superiores a 40 °C dentro del
filtro e hizo que el vermifiltro no tuviera olor (Tiruneh, 2016).

La ausencia de olor puede ser explicado ya que las lombrices de tierra liberan sus
fluidos celómicos 'antipatógenos' en la biomasa de desechos en descomposición
que matan a los patógenos haciendo que el proceso sea completamente 'libre de
olores', por lo cual, la vermifiltración es un sistema de 'baja energía' 'sin olor' y
no hay formación de 'lodos' ya que las lombrices comen los sólidos en las aguas
residuales simultáneamente y los excretan como su detrito de lombriz. (Singh &
Kumar, 2019)

Finalmente, otro estudio informa que la vermifiltración produce poco o ningún
mal olor. La vermifiltración también posee la capacidad de estimular y mejorar la
flora bacteriana para reducir enormemente los patógenos presentes en el
sistema. (Singh, Bhunia, & Rajesh, 2017)

Ya que se indica que esta clase de tecnología no produce olor no existen factores
para esta clase de fuente, sin embargo, para evaluar alguna clase de impacto se
utilizará el factor de emisión de una planta de agua residual específicamente en
un reactor aerobio que no considera producción de lodos y además con la más
baja carga de finos, ya que sería lo más cercano a esta clase de fuente. El valor
referencial a utilizar es de **0,2 ou** **E** **/s-m** **[2]** como factor de emisión, que proviene
del capítulo 3.G3 del documento “Netherlands Emission Guidelines for Air”.

En la Figura N° 9 se muestra la ubicación de las fuentes de emisión del escenario
actual y con proyecto.

_**Inventario y modelación de Olores ATM077-22**_ _21/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

_**Figura N° 9**_
_**Ubicación de las Fuentes de Emisión Actual y con Proyecto**_

Fuente: Algoritmos SpA, 2022

_**Inventario y modelación de Olores ATM077-22**_ _22/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**4.3** **Tasas de Emisión**

A continuación, se encuentra el resumen de las emisiones de las fuentes areales.
La Tabla N° 9 muestra los resultados de las emisiones de los biofiltros de la
planta.

_**Tabla N° 9**_
_**Tasas de Emisión Biofiltro Jucosol**_

|Fuente|OER OUE/s|
|---|---|
|Biofiltro 1<br>|40|

Fuente: Algoritmos SpA, 2022

_**Inventario y modelación de Olores ATM077-22**_ _23/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**5** **Modelación de Dispersión de Contaminantes**

Con el fin de evaluar el impacto de las fuentes odorantes se realizó una
modelación de dispersión con el sistema WRF-CALPUFF. Para esta modelación se
utilizó el factor de emisión como referencia para biofiltro, además se consideró
como todas las fuentes emitiendo de forma permanente, es decir, las 24 horas
del día los 365 días del año, lo anterior tiene un fin de obtener predecir el
impacto bajo la consideración de la peor condición operativa.

**5.1.1** **Base Teórica**

La aplicación de modelos de dispersión atmosférica permite determinar el aporte
de las emisiones provenientes de fuentes emisoras, en localidades y sectores
aledaños a las instalaciones de un determinado proyecto, permitiendo de este
modo, asignar las cuotas de responsabilidad en los niveles de calidad del aire
medidos en su entorno.

Los modelos lagrangianos se caracterizan por hacer uso de un sistema de
referencia que se ajusta al movimiento atmosférico. Es decir, las emisiones,
reacciones, deposición y mezclado de los contaminantes se analizan para un
volumen de aire que va cambiando su posición, de acuerdo con la velocidad y
dirección del viento. Bajo este esquema general, los modelos lagrangianos se
pueden clasificar como modelos de trayectoria y modelos gaussianos, de acuerdo
con la geometría del sistema de modelación. Los modelos de trayectoria pueden
simular los procesos para una columna hipotética de aire, en cambio, cuando la
simulación se hace para una pluma de emisión, continua o discreta, se trata de
modelos gaussianos.

Los modelos gaussianos describen el transporte y mezcla de los contaminantes,
asumiendo que las emisiones presentan, en las direcciones horizontal y vertical,
una distribución normal o de curva gaussiana con una concentración máxima en
el centro de la pluma. Generalmente estos modelos se aplican para evaluar la
dispersión de contaminantes provenientes de fuentes puntuales, aunque también
se aplican para simular emisiones de fuentes de área y de línea. Otra
característica de este tipo de modelos es que normalmente son aplicados para
evaluar la dispersión de contaminantes primarios no reactivos, aunque existen
versiones que incluyen en su formulación consideraciones especiales para poder
simular procesos de deposición y transformación química.

**5.1.2** **Sistema de Modelación WRF - CALPUFF**

Para determinar el efecto que tendrán las emisiones de material particulado y
gases provenientes de la operación del Proyecto, se utiliza un sistema acoplado
de dos modelos: El modelo atmosférico Weather Research and Forecasting
(WRF), y el modelo CALPUFF, simulador de la dispersión de contaminantes en la
atmósfera. Ambos conforman el sistema de modelación WRF-CALPUFF.

_**Inventario y modelación de Olores ATM077-22**_ _24/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

 - **WRF**

WRF es un modelo numérico de pronóstico e investigación atmosférica,
[desarrollado por las el Centro Nacional para la investigación Atmosférica (NCAR)](https://es.wikipedia.org/wiki/Centro_Nacional_de_Investigaci%C3%B3n_Atmosf%C3%A9rica)
y los Centros Nacionales para la Predicción Medioambiental (NCEP), ambas
entidades norteamericanas. Destaca sobre otros modelos porque considera los
efectos de la superficie terrestre, lo que permite resolver o pronosticar los
fenómenos meteorológicos inducidos o influenciados por esa estructura. Su uso
está aceptado por el Servicio de Evaluación Ambiental en Chile, para ser aplicado
dentro del Sistema de Evaluación de Impacto Ambiental, ya que permite cubrir la
necesidad de ampliar la resolución espacial que poseen las estaciones de
monitoreo.

La forma de trabajo de WRF comprende la resolución de las ecuaciones primitivas
de la atmósfera, utilizando una descripción euleriana. Además, es un modelo no
hidrostático, es decir, incluye la variación de presión en el eje vertical de la
atmósfera dentro de sus ecuaciones. Su manejo comprende dos componentes
importantes, el primero de ellos corresponde al WRF Pre-processing System
(WPS) donde se preparan los archivos de entrada para las simulaciones y el WRF
Model (núcleo dinámico) donde se integran las ecuaciones dinámicas y
termodinámicas, modelos de nubes, superficie, radiación, microfísica, entre otros.

Las variables meteorológicas más importantes que inciden en la dispersión de las
emisiones atmosféricas corresponden a la temperatura, velocidad del viento y
estabilidad atmosférica de la localidad sometida a evaluación. Estas variables son
utilizadas como entradas en los modelos de dispersión de contaminantes,
necesarios para predecir y evaluar los impactos ambientales actuales o de futuros
proyectos. Es por esta razón que es necesario introducir los resultados obtenidos
del modelo WRF al modelo CALPUFF.

 - **CALPUFF**

El modelo CALPUFF es un sistema avanzado de modelación meteorológica y de
calidad el aire, no estacionario, desarrollado por Sigma Research Corporation
(SRC) a fines de la década de 1980 (url: http://www.src.com). La versión
número cinco del modelo está aprobada por la Agencia de Protección Ambiental
de los Estados Unidos (EPA), lo que convierte a este modelo en una herramienta
ampliamente utilizada a nivel mundial. De forma particular, al igual que WRF, el
modelo CALPUFF está aprobado por el Servicio de Evaluación Ambiental en Chile,
para poder emplearlo dentro del Sistema de Evaluación de Impacto Ambiental.

CALPUFF modela el transporte y dispersión de contaminantes emitidos por las
fuentes emisoras en forma de paquetes o _puff_ de material, procesándolos a
través del dominio de modelación. Este modelo incluye tres componentes
principales: WRF, CALPUFF y CALPOST, además de una larga selección de
preprocesadores, diseñados para incluir datos meteorológicos y geofísicos en el
modelo. WRF simula campos de viento y temperatura en un dominio de
modelación engrillado y tridimensional. CALPUFF modela la dispersión de

_**Inventario y modelación de Olores ATM077-22**_ _25/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

contaminantes y CALPOST procesa las salidas de CALPUFF creando archivos con
las tabulaciones necesarias que permitan la evaluación de resultados.

**5.2** **Variables de Entrada ingresados al Sistema de Modelación**

El sistema de modelación WRF-CALPUFF requiere de la siguiente información de
entrada:

 **Archivos NCEP-FNL (Final):** Información de entrada para el modelo
WRF, con una resolución espacial de 1km x 1km (url:
https://rda.ucar.edu/datasets/ds083.2/).

 - **Uso de Suelo** **[b]** **:** Esta información permite definir los coeficientes de
rugosidad superficial, razón de Bowen y albedo. Los usos de suelo
presentes en el área de estudio se encuentran en la siguiente tabla.

_**Tabla N° 10**_
_**Características del Uso de Suelo**_

|Uso de Suelo|Albedoc|Col3|Razón de Bowend|Col5|Rugosidad<br>Superficial (cm)|Col7|
|---|---|---|---|---|---|---|
|**Uso de Suelo**|**Verano**|**Invierno**|**Verano**|**Invierno**|**Verano**|**Invierno**|
|Bosque hoja<br>caduca|0,16|0,17|1|1|50|50|
|Bosque Mixto|0,13|0,14|0,5|0,5|50|50|
|Matorral|0,22|0,25|1|1|10|10|
|Mezcla de hierbas|0,20|0,24|1|1|11|10|
|Pradera|0,19|0,23|1|1|12|10|
|Pastos de cultivos<br>mixtos|0,18|0,23|1|1|15|5|
|Urbano|0,18|0,18|1,5|1,5|50|50|
|Mosaico de<br>bosques de<br>cultivo|0,16|0,20|1|1|20|20|

Fuente: Algoritmos SpA, 2022

La siguiente figura presenta los usos de suelo presentes en el área de estudio,
indicados en la tabla anterior.

b Información obtenida a partir de preprocesador CTGPROC
c Albedo: reflectividad a la luz solar del suelo (expresada como fracción respecto a la unidad)
d Razón de Bowen: definida como la razón entre flujos sensibles y latentes, a nivel de superficie.

_**Inventario y modelación de Olores ATM077-22**_ _26/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

_**Figura N° 10**_
_**Uso de Suelo**_

Fuente: Algoritmos SpA, 2022

_**Inventario y modelación de Olores ATM077-22**_ _27/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

 - **Data de emisiones**, Corresponde al valor emitido por cada fuente
considerada en la fase de operación. (Ver capítulo 4)

 - **Topografía del área de modelación:** Esta información es obtenida de
datos satelitales para la zona de estudio. En la Figura N° 11 se muestra la
topografía del área de la planta.

 **Ubicación de puntos de interés**, Esto permite la evaluación de los
resultados en comparación con la normativa aplicable. La ubicación de los
puntos de interés considerados se encuentra en la Tabla N° 11. En la
Figura N° 12, se muestra la ubicación de dicho punto.

_**Figura N° 11**_
_**Topografía Área de Modelación**_

Fuente: Algoritmos SpA, 2022

_**Inventario y modelación de Olores ATM077-22**_ _28/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

_**Tabla N° 11**_
_**Localización Puntos Discretos**_ _**[e]**_

|Punto de Interés|Coordenadas UTM|Col3|
|---|---|---|
|**Punto de Interés**|**Este (m)**|**Norte (m)**|
|R1|346.589|6.370.985|
|R2|346.714|6.370.645|
|R3|346.904|6.370.732|
|R4|346.413|6.370.610|
|R5|346.973|6.370.901|
|R6|346.395|6.370.990|

Fuente: Algoritmos SpA, 2022

e Datum WGS84, coordenadas UTM.

_**Inventario y modelación de Olores ATM077-22**_ _29/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

_**Figura N° 12**_
_**Ubicación Puntos de Interés**_

Fuente: Algoritmos SpA, 2022

_**Inventario y modelación de Olores ATM077-22**_ _30/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**6** **Resultados Modelación**

Se presentan los resultados obtenidos de la modelación atmosférica para el
escenario de operación de la planta con el fin de evaluar el aporte de unidades de
olor en los diferentes receptores considerados en el estudio.

**6.1** **Campos de Viento**

Mediante la aplicación del modelo WRF se simuló el comportamiento de los
campos de vientos sobre el área del Proyecto, para cada una de las horas
consideradas en la modelación. Dichos campos de vientos permitirán determinar
posteriormente la dispersión de los contaminantes, a través de la aplicación del
modelo CALPUFF.

A modo de ejemplo se seleccionó el día 15 de febrero del año 2021
correspondiente al máximo valor horario del escenario con proyecto, para
representar el comportamiento de los vientos superficiales en horas
representativas del día, en la madrugada (06:00 hrs.), a medio día (12:00 hrs.),
durante la tarde (18:00 hrs.) y en la noche (00:00 hrs.).

_**Inventario y modelación de Olores ATM077-22**_ _31/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

_**Figura N° 13**_
_**Campos de Viento a las 00:00 horas.**_

Fuente: Algoritmos SpA, 2022

_**Inventario y modelación de Olores ATM077-22**_ _32/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_
_Febrero, 2022_

_**Figura N° 14**_
_**Campos de Viento a las 06:00 horas**_

Fuente: Algoritmos SpA, 2022

_**Inventario y modelación de Olores ATM077-22**_ _33/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_
_Febrero, 2022_

_**Figura N° 15**_
_**Campos de Viento a las 12:00 horas**_

Fuente: Algoritmos SpA, 2022

_**Inventario y modelación de Olores ATM077-22**_ _34/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_
_Febrero, 2022_

_**Figura N° 16**_
_**Campos de Viento a las 18:00 horas.**_

Fuente: Algoritmos SpA, 2022

_**Inventario y modelación de Olores ATM077-22**_ _35/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_
_Febrero, 2022_

**6.2** **Aportes Obtenidos de la Modelación**

Mediante la aplicación del modelo WRF-CALPUFF fue posible obtener los aportes
de unidades de olor de la planta Jucosol en el escenario de operación, basándose
en los campos de vientos generados por la modelación meteorológica realizada
con WRF.

Los aportes de la planta fueron evaluados en los sectores de su entorno, y fueron
comparados con el límite normativo de los Países Bajos de manera de cuantificar
si se generarán efectos adversos significativos sobre la población.

**6.2.1** **Aporte en Puntos de Interés**

En la siguiente tabla se presenta los aportes obtenidos por la modelación del
escenario de operación de la planta en los puntos de interés en el escenario
actual.

_**Tabla N° 12**_
_**Aporte Planta Jucosol Escenario Actual**_

|Puntos de Interés|Norma Países Bajos<br>Percentil 98 Horario (Unidades de Olor)|Col3|Aporte/Límite<br>Norma|
|---|---|---|---|
|**Puntos de Interés**|**Aporte**|**Límite Norma**|**Límite Norma**|
|R1|0,0035|0,5|0,69%|
|R2|0,0040|0,5|0,80%|
|R3|0,0018|0,5|0,36%|
|R4|0,0290|0,5|5,80%|
|R5|0,0013|0,5|0,26%|
|R6|0,0032|0,5|0,64%|

Fuente: Algoritmos SpA, 2022

_**Inventario y modelación de Olores ATM077-22**_ _36/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

_**Tabla N° 13**_
_**Aporte Planta Jucosol Quilicura Escenario Proyecto**_

|Puntos de Interés|Norma Países Bajos<br>Percentil 98 Horario (Unidades de Olor)|Col3|Aporte/Límite<br>Norma|
|---|---|---|---|
|**Puntos de Interés**|**Aporte**|**Límite Norma**|**Límite Norma**|
|R1|0,0133|0,5|2,66%|
|R2|0,0221|0,5|4,41%|
|R3|0,0070|0,5|1,40%|
|R4|0,1342|0,5|26,85%|
|R5|0,0051|0,5|1,02%|
|R6|0,0139|0,5|2,77%|

Fuente: Algoritmos SpA, 2022

_**Inventario y modelación de Olores ATM077-22**_ _37/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**6.2.2** **Ajustes de Resultados de la Modelación por Incertidumbre**

Acorde al análisis de incertidumbre de la modelación WRF presentado en el
capítulo 3 del presente informe, en la evaluación cuantitativa (sección 3.5), se
procede a integrar a los resultados de la modelación la incertidumbre generada,
para esto se escogió el máximo porcentaje de incertidumbre alcanzado (38 %) y
fue aplicado de acuerdo con la siguiente ecuación.

RM [′] = RM+ % de incertidumbre∗RM (IV)

Dónde:

RM’ : Resultados de la modelación WRF-CALPUFF corregidos por incertidumbre
RM : Resultados modelación WRF-CALPUFF (concentraciones contaminantes)

_% de incertidumbre_ : 38%, mayor porcentaje de incertidumbre alcanzado en la
evaluación cuantitativa del WRF (sección 3.5 del presente
informe).

_**Inventario y modelación de Olores ATM077-22**_ _38/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

En la siguiente tabla se presenta los resultados de la modelación con el ajuste de
incertidumbre.

_**Tabla N° 14**_
_**Aporte Planta Jucosol con Incertidumbre Escenario Actual**_

|Puntos de Interés|Norma Países Bajos<br>Percentil 98 Horario (Unidades de Olor)|Col3|Aporte/Límite<br>Norma|
|---|---|---|---|
|**Puntos de Interés**|**Aporte**|**Límite Norma**|**Límite Norma**|
|R1|0,0048|0,5|0,96%|
|R2|0,0055|0,5|1,11%|
|R3|0,0025|0,5|0,50%|
|R4|0,0401|0,5|8,01%|
|R5|0,0018|0,5|0,36%|
|R6|0,0044|0,5|0,88%|

Fuente: Algoritmos SpA, 2022

_**Tabla N° 15**_
_**Aporte Planta Jucosol con Incertidumbre Escenario con Proyecto**_

|Puntos de Interés|Norma Países Bajos<br>Percentil 98 Horario (Unidades de Olor)|Col3|Aporte/Límite<br>Norma|
|---|---|---|---|
|**Puntos de Interés**|**Aporte**|**Límite Norma**|**Límite Norma**|
|R1|0,0183|0,5|3,66%|
|R2|0,0304|0,5|6,09%|
|R3|0,0097|0,5|1,94%|
|R4|0,1853|0,5|37,05%|
|R5|0,0070|0,5|1,40%|
|R6|0,0191|0,5|3,83%|

Fuente: Algoritmos SpA, 2022

_**Inventario y modelación de Olores ATM077-22**_ _39/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**6.3** **Mapas de Isoconcentraciones**

A continuación, se presentan las isolíneas de concentración para el percentil 98
de 1 hora.

_**Inventario y modelación de Olores ATM077-22**_ _40/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

_**Figura N° 17**_
_**Percentil 98 de 1 Hora Escenario Actual**_

Fuente: Algoritmos SpA, 2022

_**Inventario y modelación de Olores ATM077-22**_ _41/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

_**Figura N° 18**_
_**Percentil 98 de 1 Hora Escenario con Proyecto**_

Fuente: Algoritmos SpA, 2022

_**Inventario y modelación de Olores ATM077-22**_ _42/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**7** **Área de Influencia**

Respecto al área de influencia (AI) de la planta, la “Guía para la Predicción y
Evaluación de Impactos por Olor en el SEIA”, indica que es usual circunscribir el
AI al espacio contenido por la isodora de 1 unidad de olor, no obstante, también
se incluyó las instalaciones del proyecto. Se destaca que el modelo no género una
isodora de 1 unidad de olor para el máximo valor horario obtenido del modelo,
por lo cual, se dejó como área de influencia el lugar de ubicación de los biofiltros.
A continuación, se muestra el área de influencia de la planta.

_**Figura N° 19**_
_**Área de Influencia**_

Fuente: Algoritmos SpA, 2022

_**Inventario y modelación de Olores ATM077-22**_ _43/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**8** **Conclusiones**

Del presente informe podemos extraer las siguientes conclusiones:

 Respecto a los resultados de la modelación, se evaluaron 6 receptores que
se encuentran alrededor de la planta, de los cuales los aporte obtenidos no
superan la norma de los Países Bajos tanto para el escenario actual y el

con proyecto

 El receptor de mayor concentración en unidades de olor es el número 4, no
obstante, este receptor solo representa un 26,9% y un 37,1% de la norma
para el escenario actual y con proyecto respectivamente.

 En la isoconcentraciones obtenidas bajo la modelación se puede observar
que estas tienen una dispersión local y se encuentra bajo la unidad de olor
para ambos escenarios.

 Finalmente, se destaca que no se generó una isodora de 1 unidad de olor,
siendo que se utilizó el máximo valor horario de olor que entregó el

proyecto.

_**Inventario y modelación de Olores ATM077-22**_ _44/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_

**9** **Bibliografía**

Arora, S., & Saraswat, S. (2021). Vermifiltration as a natural, sustainable and green

technology for environmental remediation: A new paradigm for wastewater
treatment process. _Vermifiltration as a natural, sustainable and green technology_
_for environmental remediation: A new paradigm for wastewater treatment_
_process_ . Malviya Nagar, Jaipur, Taiwan: Elseiver.

Bhavini, Kanaujia, Trivedi, & Hait. (2020). Applicability of Vermifiltration for Wastewater

Treatment and Recycling. _Applicability of Vermifiltration for Wastewater Treatment_
_and Recycling_ . Bihar, India: Springer Nature Singapore Pte Ltd. 2020.

Kumar, T., Rajpal, A., Bhargava, R., & Prasad, K. (2013). Performance evaluation of

vermifilter at different hydraulic loading. _Performance evaluation of vermifilter at_
_different hydraulic loading_ . Roorkee, Roorkee, India: Elseiver.

Li, Y., Cluzeau, Bouch ́e, Qiu, Laplanche, Hassouna, . . . Callarec. (2007). Vermifiltration

as a stage in reuse of swine wastewater: Monitoring methodology on an
experimental farm. _Vermifiltration as a stage in reuse of swine wastewater:_
_Monitoring methodology on an experimental farm_ . Rennes, Bretaña, Francia:
Elseiver.

Singh, R., Bhunia, P., & Rajesh, D. (2017). A mechanistic review on vermifiltration of

wastewater: Design, operation and performance. Odisha, India: Elseiver.

Singh, S., & Kumar, R. (2019). WASTEWATER VERMIFILTRATION (DETOXIFICATION &

DISINFECTION) BY EARTHWORMS FOR REUSE OF CLEAN, NUTRITIVE WATER IN
FARM IRRIGATION GIVING HIGHER FOOD PRODUCTIVITY, WHILE SAVING
FERTILIZERS & HUGE FRESHWATER OF EARTH. _VERMI_, 114-121.

Tiruneh, A. (2016). _Concentrated Greywater Treatment by Vermifiltration for Sub-_

_Saharan Urban Poor._ Mississippi: INTERNATIONAL INSTITUTE FOR WATER AND
ENVIRONMNETAL ENGINEERING.

_**Inventario y modelación de Olores ATM077-22**_ _45/45_
_Estudio Olores Biofiltro Jucosol_
_Versión 1_

_Febrero, 2022_