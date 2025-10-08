---
title: Sin título
author: EMwalnut@outlook.com
date: D:20200901205038-04'00'
language: es
type: report
pages: 45
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - CAPÍTULO A1: INTRODUCCIÓN
  - CAPÍTULO A2: ANÁLISIS DE LA INFORMACIÓN METEOROLÓGICA DE LA ZONA DEL PROYECTO
  - CAPÍTULO A3: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO METEOROLÓGICO WRF
  - CAPÍTULO 4: ANÁLISIS DE INCERTIDUMBRE DE LOS RESULTADOS DEL MODELO WRF RESPECTO DE LOS DATOS OBSERVADOS DURANTE EL AÑO 2019
  - CAPÍTULO A5: CONCLUSIONES
  - CAPÍTULO A6: BIBLIOGRAFIA
-->

## ESTUDIO EM2020/200-16: “Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo Santo”.

Empresa Eléctrica Guindo Santo SpA.

Agosto 2020

CAPÍTULO A1: INTRODUCCIÓN .................................................................................. 1

CAPÍTULO A2: ANÁLISIS DE LA INFORMACIÓN METEOROLÓGICA DE LA ZONA DEL

PROYECTO .................................................................................................................. 2

2.1 Introducción ........................................................................................................................ 2

2.2 Descripción de la Red de Monitoreo ................................................................................. 2

2.3 Series de Tiempo ................................................................................................................ 5

2.3.1 Temperatura..................................................................................................................................... 5

2.3.2 Velocidad de Viento ......................................................................................................................... 6

2.4 Ciclos Diarios de Temperatura, Velocidades y Direcciones de Viento .......................... 7

2.5 Ciclos Estacionales de Variables Meteorológicas ........................................................ 11

CAPÍTULO A3: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO
METEOROLÓGICO WRF ............................................................................................. 14

3.1 Introducción ...................................................................................................................... 14

3.2 Implementación Modelo WRF ......................................................................................... 15

3.3 Resultados del Modelo WRF ........................................................................................... 18

CAPÍTULO 4: ANÁLISIS DE INCERTIDUMBRE DE LOS RESULTADOS DEL MODELO
WRF RESPECTO DE LOS DATOS OBSERVADOS DURANTE EL AÑO 2019................. 21

4.1 Introducción ...................................................................................................................... 21

4.2 Diagnóstico en Base a Datos Observados Durante el Año 2019 ................................. 22

4.2.1 Comparación Entre la Meteorología Modelada por WRF, Respecto de los Datos Observados
Durante el Año 2019 ................................................................................................................................... 23

4.2.2 Resultados del Análisis Estadístico de los Datos Modelados con WRF, Respecto de los Datos
Observados Durante el Año 2019 .............................................................................................................. 35

4.3 Factor de Corrección ........................................................................................................ 36

i

CAPÍTULO A5: CONCLUSIONES ................................................................................ 37

CAPÍTULO A6: BIBLIOGRAFIA ................................................................................... 38

ii

Tabla A-1: Características de la estación meteorológica de superficie utilizada en el estudio. ......... 4

Tabla A-2: Porcentaje de datos válidos de la estación meteorológica de superficie utilizada en el

estudio. ..................................................................................................................................... 4

Tabla A-3: Configuración de las grillas en las corridas del modelo WRF. ........................................... 16

Tabla A-4: Estadísticos utilizados Análisis de Incertidumbre y Rangos. ............................................ 23

Tabla A-5: Resultados Estadísticos........................................................................................................ 35

iii

Figura A-1: Ubicación de la estación meteorológica ubicada dentro de la zona de estudio. ............... 3

Figura A-2: Serie de tiempo de temperatura observada en estación Termas de Chillán durante el año

2019. ......................................................................................................................................... 6

Figura A-3: Serie de tiempo de velocidad de viento observada en estación Termas de Chillán durante

el año 2019. .............................................................................................................................. 7

Figura A-4: Ciclo Diario de temperatura observada en estación Termas de Chillán durante el año

2019. ......................................................................................................................................... 8

Figura A-5: Ciclos diarios de velocidad y dirección de viento en estación Termas de Chillán, periodo

enero - diciembre del 2019. a) Ciclo diario promedio de velocidades de viento. b) Ciclo
diario promedio de frecuencia direcciones de viento. .......................................................... 9

Figura A-6: Rosas de Viento promedio anuales observadas durante el periodo enero - diciembre del

2019 en la estación Termas de Chillán. a) Periodo 01:00 a 06:00 horas. b) Periodo 07:00
a 14:00 horas. c) Periodo 15:00 a 24:00 horas. d) Periodo 01:00 a 24:00 horas (diario). 10

Figura A-7: Ciclos diario y anual de temperatura observados en estación Termas de Chillán, periodo

enero - diciembre del 2019. ................................................................................................. 12

Figura A-8: Ciclos diario y anual velocidad y dirección de viento observados en estación Termas de

Chillán, periodo enero - diciembre del 2019. ...................................................................... 13

Figura A-9: Diagrama de operación del modelo meteorológico WRF. .................................................. 15

Figura A-10: Ilustración del dominio y topografía del área de estudio. .................................................. 17

Figura A-11: Comparación entre campos de viento de verano v/s invierno a las 00:00 horas. a) Verano:

02-01-2019, 00:00 horas. b) Invierno: 02-07-2019, 00:00 horas. ..................................... 19

Figura A-12: Comparación entre campos de viento de verano v/s invierno a las 12:00 horas. a) Verano:

02-01-2019, 12:00 horas. b) Invierno: 02-07-2019, 12:00 horas. ..................................... 20

Figura A-13: Series de tiempo de temperatura de estación Termas de Chillán, año 2019. a) Datos

observados, b) Datos modelados con WRF. ........................................................................ 24

Figura A-14: Series de tiempo de velocidad de viento de estación Termas de Chillán, año 2019. a) Datos

observados, b) Datos modelados con WRF. ........................................................................ 25

Figura A-15: Ciclos Diarios de temperatura de estación Termas de Chillán, año 2019. a) Temperatura

datos observados, b) Temperatura datos modelados con WRF. ....................................... 27

Figura A-16: Ciclos Diarios de velocidad y dirección de viento de estación Termas de Chillán, año 2019.

a) Velocidad datos observados, b) Velocidad datos modelados con WRF, c) Dirección
datos observados, d) Dirección datos modelados. ............................................................ 28

iv

Figura A-17: Ciclos Diarios y Anuales de Temperatura de estación Termas de Chillán, año 2019. a)

Datos Observados, b) Datos Modelados con WRF. ............................................................ 30

Figura A-18: Ciclos Diarios y Anuales de Velocidad y Dirección de Viento de estación Termas de

Chillán, año 2019. a) Datos Observados, b) Datos Modelados con WRF. ......................... 31

Figura A-19: Rosas de Viento Madrugada y Mañana de estación Termas de Chillán, año 2019. a) Datos

observados 01:00-06:00 horas, b) Datos modelados con WRF 01:00-06:00 horas, c) Datos
observados 07:00-14:00 horas, d) Datos modelados 07:00-14:00 horas. ....................... 33

Figura A-20: Rosas de Viento Tarde y todo el día de estación Termas de Chillán, año 2019. a) Datos

observados 15:00-00:00 horas, b) Datos modelados con WRF 15:00-00:00 horas, c) Datos
Observados 01:00-24:00 horas, d) datos Modelados con WRF 01:00-24:00 horas. ....... 34

v

# CAPÍTULO A1: INTRODUCCIÓN

En este documento EnviroModeling Spa. presenta el Anexo A del Informe Final
correspondiente al estudio: “Inventario de Emisiones y Modelación de Calidad de Aire
para el Proyecto Parque Solar Guindo Santo”, en el marco de la Adenda N° 1 del Proyecto
Parque Solar Guindo Santo.

El objetivo de este estudio consiste en evaluar el impacto en la calidad del aire en el área
de influencia del Proyecto Parque Solar Guindo Santo.

Para el logro de este objetivo, se realizó la actividad de análisis y modelación de la
meteorología del año 2019.

En este Anexo se presenta la descripción de la información meteorológica de la estación
Termas de Chillán de la Dirección Meteorológica de Chile (DMC), la implementación,
aplicación y resultados del modelo meteorológico WRF y la comparación de los

resultados de WRF con los datos observados en la estación Termas de Chillán.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 1
Santo”

Anexo A

# CAPÍTULO A2: ANÁLISIS DE LA INFORMACIÓN METEOROLÓGICA DE LA ZONA DEL PROYECTO

### 2.1 Introducción

A continuación, se presenta el análisis de la información meteorológica registrada por
la estación Termas de Chillán durante el periodo de enero - diciembre del 2019,
perteneciente a la red de monitoreo de la Dirección Meteorológica de Chile (DMC). Ésta
es una estación meteorológica que se ubica en un sector precordillerano de condiciones
extremas, que se diferencia de la zona donde se emplaza el Proyecto. Sin embargo, se
realizó su análisis debido a que es la más cercana que cumple con los estándares
meteorológicos descritos en la World Meteorological Organization (WMO).

### 2.2 Descripción de la Red de Monitoreo

La estación Termas de Chillán se encuentra emplazada en la comuna de Pinto, Región
de Ñuble, a 82 km al oriente de la ciudad de Chillán (ver Figura A-1 ubicación).

Esta estación registra datos de velocidad y dirección de viento, temperatura, radiación
solar global, humedad relativa, presión y precipitación. En el presente texto solo fueron
analizadas las variables temperatura y velocidad de viento.

En Figura A-1 se presenta la ubicación de la estación, la cual se encuentra emplazada
en plena cordillera. En Tabla A-1 se presenta información acerca de la
georreferenciación de la estación de monitoreo mencionada, durante el periodo enero diciembre del año 2019. En Tabla A-2 se presenta el porcentaje de datos válidos para
las variables descritas.

En las siguientes secciones se presenta el análisis de la información meteorológica de
superficie registrada por la estación Termas de Chillán.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 2
Santo”

Anexo A

Figura A-1: Ubicación de la estación meteorológica ubicada dentro de la zona de

estudio.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 3
Santo”

Anexo A

Tabla A-1: Características de la estación meteorológica de superficie utilizada en el estudio.

|Estación|Col2|Coordenadas Datum WGS 84|Col4|Variables|Col6|Col7|
|---|---|---|---|---|---|---|
|Abreviación|Nombre|UTM-E (m)|UTM-N (m)|VV|DV|T|
|TCH|Termas de Chillán|285.279,49|5.913.107,85|X|X|X|

VV: Velocidad de viento, m/s. DV: Dirección de viento, grados. T: Temperatura

Tabla A-2: Porcentaje de datos válidos de la estación meteorológica de superficie utilizada en el estudio.

|Estación|Col2|Coordenadas Datum WGS 84|Col4|% de Datos válidos por variable|Col6|Col7|
|---|---|---|---|---|---|---|
|Abreviación|Nombre|UTM-E (m)|UTM-N (m)|VV|DV|T|
|TCH|Termas de Chillán|285.279,49|5.913.107,85|85,43|86,11|87,46|

VV: Velocidad de viento, m/s. DV: Dirección de viento, grados. T: Temperatura, oC.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo Santo” 4

Anexo A

### 2.3 Series de Tiempo

En esta sección se presentan las series de tiempo de velocidad de viento horarias
observadas durante el periodo enero - diciembre del 2019 en la estación presentada en
Tabla A-1 y Tabla A-2. Los gráficos de series de tiempo presentados a continuación
fueron realizados con el Software Matlab. Estas series de tiempo permiten un análisis
cualitativo de los datos en términos de completitud de la serie y periodos con datos
faltantes, valores fuera de rango y problemas de equipo (datos constantes, tendencias,
entre otras).

Las series de tiempo se presentan para las siguientes variables:

Temperatura

- Velocidad del viento

2.3.1 Temperatura

Las series de tiempo de temperatura se presentan en Figura A-2. Desde el punto de vista
de la integridad de los datos, es posible observar falta de éstos en el mes de mayo y los
primeros días de junio, posiblemente debido a nevazones que impiden realizar la
correcta operación de la estación. A pesar de lo anterior, el porcentaje de datos válidos
es bastante alto, lo que permite analizar de buena forma la variabilidad temporal y el
comportamiento diario y estacional en el año (datos sobre el 80%, ver Tabla A-2).

Desde el punto de vista cuantitativo, se observan mayores temperaturas en el periodo
estival y los valores mínimos en el periodo de invierno, bajo los cero grados (Figura A2). Esto es en concordancia con el clima típico de esta zona, el cual corresponde a un
clima frío de altura con abundantes precipitaciones (Inzunza, 2000).

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 5
Santo”

Anexo A

Figura A-2: Serie de tiempo de temperatura observada en estación Termas de Chillán

durante el año 2019.

2.3.2 Velocidad de Viento

Las series de tiempo de la velocidad de viento se presentan en Figura A-3. Al igual que
la temperatura el porcentaje de datos válidos es sobre el 80%, pudiendo analizar de
buena forma la variabilidad temporal y el comportamiento diario y estacional (ver Tabla
A-2).

Desde el punto de vista de la intensidad, se observan mayores magnitudes en el periodo
de invierno, posiblemente asociado al paso de frentes fríos característicos en el periodo
invernal en Chile Central y Sur, trayendo como consecuencia inestabilidad atmosférica,
fuertes movimientos verticales y advección de masas de aire en la zona estudiada
(Garreaud, 1995).

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 6
Santo”

Anexo A

Figura A-3: Serie de tiempo de velocidad de viento observada en estación Termas de

Chillán durante el año 2019.

### 2.4 Ciclos Diarios de Temperatura, Velocidades y Direcciones de Viento

En esta sección se presenta un análisis de las temperaturas, velocidades y direcciones
de los vientos promedio anuales, mediante ciclos diarios y rosas de viento observados
durante el año 2019.

Los ciclos diarios entregan información del comportamiento promedio de la variable
meteorológica analizada durante las horas del día. Mientras que las rosas de viento
entregan información asociada a la distribución de velocidades y la frecuencia de
ocurrencia de las diferentes direcciones de viento.

El ciclo diario de temperatura se presenta en Figura A-4, el que muestra un
comportamiento típico de la zona Centro-Sur de Chile. Se visualizan máximos en el día
y mínimas en la noche. La variabilidad mostrada mediante los percentiles 5 y 95 indican
máximos cercanos a 22 °C y mínimas levemente bajo cero, mostrando una amplitud
térmica significativa.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 7
Santo”

Anexo A

Figura A-4: Ciclo Diario de temperatura observada en estación Termas de Chillán

durante el año 2019.

Respecto al comportamiento de la velocidad de viento (Figura A-5, Panel a) se visualiza
velocidades promedios en torno a los 7 m/s en el periodo nocturno, mientras que en la
tarde éstas suben en torno a los 10 m/s. Esto es comportamiento típico observado en
estas latitudes y de clima de montaña, debido al aumento de la turbulencia atmosférica,
producto de la insolación causada por la radiación de onda corta proveniente del sol
(Stull, 2012).

La dirección de viento observada en el ciclo (Figura A-5, Panel b), es característica de
cordillera, debido al cambio en la dirección de viento producto de las diferencias de
temperatura, entre ladera y valle (vientos catabáticos) que hacen que los flujos tomen
direcciones distintas. La imagen muestra la frecuencia de las direcciones de viento
observado cada 22,5o de ángulo de dirección de viento en porcentaje. En horas de
madrugada se observa una mayor frecuencia de vientos con predominancia Noreste
(entre 0o y 90o), pasando el 50%, cambiando en horas de la tarde, a partir de las 10:00
horas para pasar a una predominancia Suroeste cercano a un 40%.

Lo anterior es reforzado por la Figura A-6, panel a) y b), donde se muestran frecuencias
cercanas al 24% de componente Noreste en el periodo nocturno, en comparación con el
periodo de tarde, panel c), donde la frecuencia disminuye a un 16% y aparece una
componente Suroeste con un 4%.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 8
Santo”

Anexo A

Figura A-5: Ciclos diarios de velocidad y dirección de viento en estación Termas de

Chillán, periodo enero - diciembre del 2019. a) Ciclo diario promedio de
velocidades de viento. b) Ciclo diario promedio de frecuencia direcciones
de viento.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 9
Santo”

Anexo A

|a)|b)|
|---|---|
|c)|d)|

Figura A-6: Rosas de Viento promedio anuales observadas durante el periodo enerodiciembre del 2019 en la estación Termas de Chillán. a) Periodo 01:00 a
06:00 horas. b) Periodo 07:00 a 14:00 horas. c) Periodo 15:00 a 24:00
horas. d) Periodo 01:00 a 24:00 horas (diario).

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 10
Santo”

Anexo A

### 2.5 Ciclos Estacionales de Variables Meteorológicas

Los ciclos estacionales son presentados para analizar el comportamiento de una
variable meteorológica de interés desde el punto de vista de ciclo anual y ciclo diario en
promedio.

Los ciclos estacionales corresponden a gráficos en cuyo eje “x” muestran las horas del
día para la obtención del ciclo diario y en el eje “y” los meses del año para mostrar el
ciclo anual, con cálculos obtenidos mediante promedios horas del año 2019 de la
meteorología observada. Los colores representan la magnitud de la variable con una
barra de color tipo “jet” de la librería de color del software utilizado para graficar, donde
los colores rojos representan mayores magnitudes y los colores azules menores. Las
variables a presentar son temperaturas, velocidades y direcciones de los vientos para
la estación Termas de Chillán.

En Figura A-7 se muestra el ciclo estacional de la temperatura, donde se visualizan
magnitudes sobre los 20 °C en el periodo estival y tarde. En el periodo nocturno el
descenso no es brusco, visualizándose temperaturas promedio entre 10 °C y 15 °C.

Contrario a la descripción anterior, en el periodo invernal el gráfico muestra
temperaturas menores a 0 °C en promedio, siendo constante en periodo nocturno y
diurno. A medida que se acerca al periodo de primavera y con el aumento de la radiación
solar en el hemisferio Sur, el cambio en la temperatura acusa un aumento paulatino de
la temperatura visto desde agosto y en horas del día.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 11
Santo”

Anexo A

Figura A-7: Ciclos diario y anual de temperatura observados en estación Termas de

Chillán, periodo enero - diciembre del 2019. [1]

En Figura A-8 se muestra el ciclo diario y anual de la velocidad y dirección de viento.
Como se describió con anterioridad, los colores muestran la magnitud de la velocidad
del viento y los vectores de viento representan la dirección predominante en la misma
temporalidad.

El ciclo estacional y diario de velocidad muestra un comportamiento similar respecto a
la temperatura, en proporción al crecimiento y disminución de la magnitud en los ciclos
anual y diario.

Las observaciones muestran un aumento en la velocidad de viento en horas de la tarde
en los meses de verano. Lo contrario ocurre en la temporada de invierno, donde se
visualizan magnitudes de viento mayores en el periodo nocturno y madrugada.
Respecto a la dirección de viento, ésta muestra un comportamiento en correspondencia

1 Sección en blanco corresponde a periodo sin datos.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 12
Santo”

Anexo A

con el tipo brisa valle - montaña o vientos catabáticos, donde en temporada de verano
se visualizan vientos de componente Noreste en el periodo nocturno para pasar en
horas de la tarde a componente Sur. En los meses de invierno no se observa esta
tendencia.

Figura A-8: Ciclos diario y anual velocidad y dirección de viento observados en

estación Termas de Chillán, periodo enero - diciembre del 2019. [ 2]

2 Sección en blanco corresponde a periodo sin datos.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 13
Santo”

Anexo A

# CAPÍTULO A3: IMPLEMENTACIÓN, APLICACIÓN Y RESULTADOS DEL MODELO METEOROLÓGICO WRF

### 3.1 Introducción

En este Capítulo se presenta la implementación y aplicación del modelo meteorológico
WRF v4.1.5 (Weather Research and Forecasting Model). WRF es uno de los modelos
meteorológicos de pronóstico más avanzados y completos. El modelo ofrece una
amplia gama de aplicaciones meteorológicas a través de escalas de decenas de metros
a miles de kilómetros.

WRF ofrece pronósticos operativos mediante una plataforma flexible y
computacionalmente eficiente, al tiempo que proporciona los últimos avances en la
física, numéricos y de asimilación de datos aportados por los desarrolladores a través
de una amplia comunidad de investigación.

El modelo obtiene sus condiciones de borde de datos históricos globales del clima que
son mantenidos por centros operacionales de pronóstico del tiempo. Estos datos
globales representan el estado completo de la atmósfera en todo el planeta y son
resultado de análisis informáticos sofisticados de datos superficiales disponibles y de
observaciones a niveles más altos. Cada período de análisis combina decenas de miles
de mediciones individuales tomadas en todo el globo terrestre.

Para poder incorporar la gama completa de fenómenos meteorológicos que ocurren en
la atmósfera real el modelo utiliza una configuración de grillas anidadas. El alcance de
la grilla más gruesa es seleccionado para capturar el efecto de los fenómenos de la
escala sinóptica dentro de la región de interés, mientras que la grilla más fina permite
que el modelo desarrolle circulaciones regionales relacionadas con la interacción de la
atmósfera con la topografía.

En Figura A-9 se presenta un diagrama de operación del modelo WRF. Como se observa
en esta figura, este sistema considera como información de entrada meteorología del
sistema GFS y/o datos de estaciones meteorológicas locales, además de topografía y
uso de suelos. Con los archivos de salida del modelo se puede obtener un archivo
formato tipo CALMET, el cual sirve de entrada para el modelo CALPUFF.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 14
Santo”

Anexo A

Figura A-9: Diagrama de operación del modelo meteorológico WRF.

### 3.2 Implementación Modelo WRF

Para la implementación del modelo WRF fue considerada la meteorología de los datos
históricos del año 2019 proporcionados por el Sistema Global Forecast System (GFS),
de la NOAA (National Oceanic and Atmospheric Administration), de USA, con una
resolución temporal de 3 horas y resolución espacial de 0,5 grados. El uso de suelos
correspondió a la información satelital de MODIS de la NASA, con una resolución de 15
segundos de grado. Respecto a la topografía (Figura A-10), ésta fue obtenida a partir de
la información topográfica del SRTM (misión de radar topográfico del Transbordador
Espacial de la NASA) con resolución de 3 segundos de grado, es decir 90 metros
aproximadamente. Con toda esta información se corrió el modelo WRF v4.1.5 para
generar la meteorología requerida por el modelo CALPUFF.

Finalmente, los archivos de salida de WRF en formato netCDF para el año 2019 fueron
procesados mediante MMIF v3.4.1, obteniendo un archivo en formato .met (CALPUFFREADY) listo para ser ingresado al modelo de dispersión de contaminantes CALPUFF.
Esto, a partir de los resultados del modelo WRF con una resolución de 1 kilómetro en su
grilla más fina, de acuerdo a los estándares establecidos en la “Guía Para el Uso de
Modelos de Calidad de Aire en el SEIA, año 2012” (Guía SEA), elaborada por el Servicio
de Evaluación Ambiental (SEA).

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 15
Santo”

Anexo A

Las características del dominio de más alta resolución se muestran en la Tabla A-3.

El dominio de modelación del proyecto se diseñó considerando la grilla de más alta
resolución de WRF (Tabla A-3), por ser la que mejor representa la zona de estudio,
debido a que considera una resolución con tamaño de grilla de 1,0 x 1,0 km para definir
la topografía y uso de suelos. Tiene dimensiones de 80 km en la dirección Este-Oeste y
70 km en la dirección Norte-Sur, a partir de su origen ubicado en los 37,078 latitud Sur
y 71,735 longitud Oeste. Las características generales de la proyección Lambert de esta
grilla se presentan en Tabla A-3 y este dominio se presenta en Figura A-10.

Tabla A-3: Configuración de las grillas en las corridas del modelo WRF.

|Características|Configuración|
|---|---|
|Tipo de Proyección|Lambert Conformal Conic|
|N° celdas en dirección E-W|80|
|N° celdas en dirección N-S|70|
|Resolución en dirección E-W|1 km|
|Resolución en dirección N-S|1 km|
|ref_lat|-37,078|
|ref_lon|-71,735|
|truelat1|-36,818|
|truelat2|-37,338|
|stand_lon|-71,735|

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 16
Santo”

Anexo A

|Col1|PROYECTO<br>PARQUE SOLAR GUINDO SANTO<br>Región de Ñuble<br>Provincia de Diguillín|
|---|---|
||Situación<br>Regional <br>Situación<br>Nacional <br>i <br>ii|
||LEYENDA:<br>: Proyecto<br>Curvas de nivel (m.s.n.m):<br>|
||ESCALA:<br>Escala Gráfica:<br>Escala Numérica 1 : 556.000<br>0 5 10 km|
|||

Figura A-10: Ilustración del dominio y topografía del área de estudio.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo Santo” 17

Anexo A

### 3.3 Resultados del Modelo WRF

En esta sección se presentan los resultados del modelo meteorológico WRF. Estos
resultados son proporcionados al modelo de dispersión CALPUFF para relacionar las
condiciones meteorológicas con las emisiones de contaminantes atmosféricos y su
distribución en el área de estudio.

Los resultados de WRF se presentan los resultados del modelo meteorológico WRF.
Estos resultados se presentan en Figura A-11 y Figura A-12, mediante ejemplos de
campos de vientos modelados para el dominio de modelación, durante horas de noche
y día, de los días 02 de enero y 02 julio del 2019 (verano e invierno) para las 00:00 y 12:00
horas.

Según lo visualizado en la Figura A-11, el modelo presenta diferencias en las direcciones
de viento en todo el dominio. Siendo más marcado en sectores de valle (topografía más
baja en verde). Predomina una componente típica de viento Sur en el panel a), mientras
que en el panel b) el viento es más bien de componente Noreste. Esto último podría
implicar que el modelo logra capturar los sistemas frontales que son parte del sistema
sinóptico de Chile Centro-Sur. La otra diferencia notable corresponde a los vientos en
topografía alta (cordillera) donde en temporada de verano presenta pocas intensidades
de viento, mientras que en invierno se presentan altas intensidades sobre las cumbres,
en tanto que en quebradas se muestra una cierta turbulencia atmosférica, sin una
dirección clara, debido a la topografía compleja existente.

Lo visualizado en la Figura A-12, es parecido a lo mostrado en la Figura A-11. El modelo
presenta diferencias marcadas en las direcciones de viento en todo el dominio, entre
ambas estacionalidades. Es altamente probable que el modelo haya capturado una alta
estabilidad atmosférica típica de verano, con un viento de componente Sur y poca
intensidad en cordillera, mientras que en invierno, el modelo esté mostrando viento de
componente Norte, probablemente asociado a un sistema de bajas presiones (ciclones
atmosféricos) y alta intensidad de vientos marcado en cordillera.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 18
Santo”

Anexo A

Figura A-11: Comparación entre campos de viento de verano v/s invierno a las 00:00 horas. a) Verano: 02-01-2019,

00:00 horas. b) Invierno: 02-07-2019, 00:00 horas.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo Santo” 19

Anexo A

Figura A-12: Comparación entre campos de viento de verano v/s invierno a las 12:00 horas. a) Verano: 02-01-2019,

12:00 horas. b) Invierno: 02-07-2019, 12:00 horas.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo Santo” 20

Anexo A

# CAPÍTULO 4: ANÁLISIS DE INCERTIDUMBRE DE LOS RESULTADOS DEL MODELO WRF RESPECTO DE LOS DATOS OBSERVADOS DURANTE EL AÑO 2019

### 4.1 Introducción

En el presente capítulo se realizará el análisis de incertidumbre del modelo WRF, el cual
es solicitado en la Guía SEA.

Las variables analizadas cualitativamente correspondieron a la temperatura, velocidad
y dirección de viento, mientras que desde el punto de vista estadístico solo fueron
temperatura y velocidad de viento, medidas en la estación Termas de Chillán, región de
Ñuble, Chile.

Es necesario aclarar que los datos observados fueron validados siguiendo los criterios
de la Agencia de Protección Ambiental de los EE.UU (EPA, 2000). Los criterios de
validación fueron los siguientes:

 Temperatura

 Datos menores a -21°C y máximos a 45°C.

 - Cuando su variación no es más de 10° durante 18 horas consecutivas.

 El cambio es mayor que 5 °C que la hora anterior.

 No varía más de 0,5 °C por 12 horas consecutivas.

 - Velocidad de Viento

 - Datos menores a 0 m/s y mayores a 30 m/s.

 Datos sin variación de más de 0,1 m/s en 3 horas o 0,5 m/s en 12 horas.

 - Dirección de Viento

 - Datos menores a 0° y mayores a 360°.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 21
Santo”

Anexo A

 Datos sin variación menor a 0° ó mayor por más de 3 horas consecutivas.

 Datos sin variación de más de 10° por 18 horas consecutivas.

Es necesario aclarar que la comparación entre el modelo meteorológico y las
observaciones es más bien referencial, con el objetivo de cumplir con los lineamientos
de la Guía SEA.

La estación Termas de Chillán y la única presente en el dominio de modelación, se
encuentra emplazada en plena Cordillera de los Andes, caracterizada por topografía
compleja a 1.721 m.s.n.m. Esto hace muy complejo que un modelo pueda reproducir
con un buen desempeño las variables meteorológicas. Sin perjuicio de lo anterior, el
proyecto se encuentra localizado en Valle, cerca de la localidad de Yungay, por lo tanto
este análisis no necesariamente impacta en el desempeño del modelo en la ubicación
del proyecto.

### 4.2 Diagnóstico en Base a Datos Observados Durante el Año 2019

Para analizar el desempeño del modelo, éste se hace mediante la comparación
cualitativa y cuantitativa de las salidas numéricas del modelo con respecto a las
observaciones de la estación Termas de Chillán, para las variables temperatura,
velocidad y dirección del viento. Se presentan gráficos comparativos entre
observaciones y modelo, solicitados por la Guía SEA, y finalmente se muestra el análisis
cuantitativo aplicando los siguientes estadísticos matemáticos:

Error Cuadrático Medio (RMSE): entrega el grado de precisión entre los datos
pronosticados y observado.

Sesgo normalizado (BIASN): entrega el sesgo entre las series modeladas y
observadas.

Coeficiente de Correlación (R): entrega el grado de relación lineal entre los datos
observados y modelados.

En Tabla A-4 se presentan la ecuación y el Rango de estos estadísticos.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 22
Santo”

Anexo A

Tabla A-4: Estadísticos utilizados Análisis de Incertidumbre y Rangos.

|Estadístico|Ecuación|Rango|
|---|---|---|
|RMSE|√∑(Mi−Oi)2<br>n<br>n<br>i=1<br>|(0, ∞)|
|BIASN|∑<br>Mi−Oi<br>n<br>i=1<br>∑<br>Oi<br>n<br>i=1<br>|(-∞,∞)|
|R|1<br>(1 −n)∑(Mi−M)<br>̅̅̅̅<br>σM<br>N<br>i=1<br>(Oi−O)<br>̅̅̅̅<br>σo<br>|[-1,1]|

4.2.1 Comparación Entre la Meteorología Modelada por WRF, Respecto de los Datos

Observados Durante el Año 2019

La comparación entre series de tiempo observadas y modeladas de temperatura y
velocidad de viento del año 2019, para la estación Termas de Chillán se presentan en
Figura A-13 y Figura A-14.

En general es posible apreciar una subestimación de los resultados del modelo respecto
a las observaciones, tanto en la temperatura como en la velocidad de viento. En ambas
variables se aprecia una subestimación de las máximas magnitudes, sin embargo, los
mínimos son bien representados. Los máximos de temperatura observados llegan cerca
de los 30 °C, en cambio el modelo muestra temperaturas que apenas sobrepasan los 20
°C.

Respecto a la velocidad de viento, pasa lo mismo, las observaciones muestran
magnitudes de viento cercanas a los 30 m/s, mientras que el modelo se aproxima a los
25 m/s como máximo, subestimando claramente. Adicionalmente las observaciones
muestran un comportamiento más bien homogéneo de los datos, a diferencia del
modelo que muestra datos más heterogéneos, aparentemente diferenciando la cantidad
de calmas que podría haber.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 23
Santo”

Anexo A

Figura A-13: Series de tiempo de temperatura de estación Termas de Chillán, año 2019.

a) Datos observados, b) Datos modelados con WRF.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 24
Santo”

Anexo A

Figura A-14: Series de tiempo de velocidad de viento de estación Termas de Chillán, año

2019. a) Datos observados, b) Datos modelados con WRF.

La comparación entre los ciclos diarios de temperatura observados y modelados se
muestran en la Figura A-15. Las observaciones y el modelo muestran el típico ciclo de
temperatura diaria con aumento en el día de su magnitud y una disminución en el
periodo nocturno. Sin embargo, la diferencia se presenta en la subestimación de los
índices mostrados en el gráfico por parte del modelo (Figura A-15 panel b). Esto se ve

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 25
Santo”

Anexo A

reflejado en los percentiles 95 y en el promedio, salvo el percentil 5, para el cual el
modelo da un buen acercamiento de los mínimos de las observaciones. Lo anterior da
como resultado una amplitud térmica menor en el modelo y adicionalmente da cuenta
que se subestiman los valores altos de temperatura.

La comparación entre los ciclos diarios de velocidad de viento observados y modelados
se muestran en la Figura A-16, panel a) y b). Las observaciones muestran el típico ciclo
de velocidad de viento diario con un aumento en el día de la intensidad y una
disminución en el periodo nocturno. La variabilidad es importante, mostrando
velocidades de 2 m/s como percentil 5 y alrededor de 16 m/s como percentil 95 en
promedio para ambos índices. Respecto al modelo, este no logra reproducir el ciclo de
velocidad de viento subestimando la media y los extremos del 90% del rango observado.
Esto en cordillera podría llevar a sobrestimar la dispersión de contaminantes, sin
embargo, el proyecto se encuentra emplazado en valle con influencia cordillerana.

En la Figura A-16 paneles c) y d) se muestra el ciclo diario de las direcciones de viento,
visualizando las frecuencias de esta variable cada 22,5° entre observaciones y las
salidas del modelo en las horas del día. Las observaciones muestran vientos
predominantes Noreste sobre un 50% en el periodo nocturno, para pasar a partir de las
12:00 horas hasta el resto del día un 50% de predominancia Suroeste.

Respecto a lo modelado, reproduce de forma parcial las observaciones, pero
subestimando la frecuencia en el periodo nocturno con un 20% de las frecuencias de
componente Noreste, mientras que en la tarde presenta más bien una frecuencia
compartida de predominancia de direcciones de viento entre componentes Suroeste a
Norte, 35% y 20% respectivamente.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 26
Santo”

Anexo A

Figura A-15: Ciclos Diarios de temperatura de estación Termas de Chillán, año 2019. a) Temperatura datos

observados, b) Temperatura datos modelados con WRF.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo Santo” 27

Anexo A

|a)|b)|
|---|---|
|c)|d)<br>|

Figura A-16: Ciclos Diarios de velocidad y dirección de viento de estación Termas de Chillán, año 2019. a) Velocidad

datos observados, b) Velocidad datos modelados con WRF, c) Dirección datos observados, d) Dirección
datos modelados.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo Santo” 28

Anexo A

Respecto al desempeño del modelo en la representación estacional, en Figura A-17 y
Figura A-18 se presentan los ciclos estacionales de temperatura y velocidad y dirección
de vientos.

En Figura A-17 se observa que el modelo simula notablemente el aumento de la
temperatura, en los meses de verano y en el periodo diurno y viceversa, es decir
disminución en periodo invernal y nocturno.

En la Figura A-18 se muestran los ciclos diarios y anuales en una misma figura entre
observaciones y modelado de las variables velocidad y dirección de viento. Es
importante notar que la sección blanca del panel a) corresponde a la falta de datos de
las observaciones, probablemente debido a la falta de acceso a la estación por
nevazones. Sin embargo, esto es una suposición de la causa.

Parte de las similitudes entre ambas imágenes, muestran la mayor intensidad presente
en el periodo invernal, además de compartir cierta similitud en la dirección de los
vientos, Noreste las observaciones y Suroeste levemente lo modelado.

Las observaciones muestran el aumento de velocidad de viento en el periodo diurno y
estival y el cambio en la dirección de viento, debido a los cambios de temperatura
producidos por la insolación solar en ladera (Figura A-17). Sin embargo, el modelo
subestima este comportamiento. Es importante destacar que, a modo de ciclo anual, el
modelo logra reproducir parcialmente la dirección de los vientos.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 29
Santo”

Anexo A

Figura A-17: Ciclos Diarios y Anuales de Temperatura de estación Termas de Chillán, año 2019. a) Datos Observados,

b) Datos Modelados con WRF.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo Santo” 30

Anexo A

Figura A-18: Ciclos Diarios y Anuales de Velocidad y Dirección de Viento de estación Termas de Chillán, año 2019. a)

Datos Observados, b) Datos Modelados con WRF.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo Santo” 31

Anexo A

Finalmente, en Figura A-19 y Figura A-20 se muestran las rosas de viento observadas y
modeladas de estación Termas de Chillán, con la idea de mostrar distintos periodos,
entre madrugada, mañana y tarde, entre ambos casos. Estas figuras refuerzan el
análisis anterior de vientos predominantes y velocidades de viento, indicando que el
modelo logra representar parcialmente la dirección de viento, donde las observaciones
muestran una tendencia Noreste en la mañana (Figura A-19) y en todo el periodo en
promedio (Figura A-20, paneles c y d). No obstante, la velocidad es subestimada pero
tiene una mayor aproximación a los ciclos mostrados en las observaciones.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 32
Santo”

Anexo A

|a)|b)|
|---|---|
|c)|d)|

Figura A-19: Rosas de Viento Madrugada y Mañana de estación Termas de Chillán, año

2019. a) Datos observados 01:00-06:00 horas, b) Datos modelados con
WRF 01:00-06:00 horas, c) Datos observados 07:00-14:00 horas, d) Datos
modelados 07:00-14:00 horas.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 33
Santo”

Anexo A

|a)|b)|
|---|---|
|c)<br>|d)<br>|

Figura A-20: Rosas de Viento Tarde y todo el día de estación Termas de Chillán, año

2019. a) Datos observados 15:00-00:00 horas, b) Datos modelados con
WRF 15:00-00:00 horas, c) Datos Observados 01:00-24:00 horas, d) datos
Modelados con WRF 01:00-24:00 horas.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 34
Santo”

Anexo A

4.2.2 Resultados del Análisis Estadístico de los Datos Modelados con WRF, Respecto

de los Datos Observados Durante el Año 2019

Los resultados estadísticos matemáticos obtenidos entre los datos observados y
modelados para la estación Termas de Chillán se presentan en Tabla A-5. Estos
resultados dan una muestra del desempeño del modelo en el punto geográfico
analizado. Estos resultados indican que en la estación de estudio, respecto a la
velocidad de viento, el modelo no fue tan preciso, reflejado en el estadístico RMSE,
subestimando levemente las observaciones, indicado en el BIASN y la relación con los
datos fue más bien baja respecto a las observaciones mostrado en el coeficiente de
correlación R. Cabe destacar que esto puede deberse a la topografía compleja presente
en el lugar, lo cual es aún un sesgo importante en los modelos numéricos
meteorológicos.

En cambio, para la temperatura el modelo mostró una gran relación con los datos,
reflejado en el coeficiente de correlación de 0,84, no obstante, la precisión y la
subestimación se mantuvo igual que la velocidad de viento.

Tabla A-5: Resultados Estadísticos.

|Estadístico|Valor|Variable|
|---|---|---|
|RMSE (m/s)|5,86|VV|
|BIASN (m/s)|-0,31|VV|
|R|0,20|VV|
|Promedio Observaciones (m/s)|7,85|VV|
|Promedio Modelado (m/s)|5,82|VV|
|RMSE (°C)|3,88|T|
|BIASN (°C)|-0,22|T|
|R|0,84|T|
|Promedio Observaciones (°C)|9,36|T|
|Promedio Modelado (°C)|6,86|T|

RMSE: Error Cuadrático Medio, BIASN: Sesgo normalizado, R: Coeficiente de Correlación

VV: Velocidad de viento, T: Temperatura.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 35
Santo”

Anexo A

### 4.3 Factor de Corrección

Según los resultados obtenidos en el análisis de incertidumbre, la información de WRF
entregada al modelo CALPUFF podría implicar que el modelo sobrestime la dispersión
de contaminantes. Por lo tanto, no es necesario aplicar un factor de corrección y se
considera como el peor escenario posible de dispersión en la zona de estudio.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 36
Santo”

Anexo A

# CAPÍTULO A5: CONCLUSIONES

En este Capítulo se presentan las conclusiones correspondientes al Anexo A del Informe
Final del estudio “Inventario de Emisiones y Modelación de Calidad de Aire para el
Proyecto Parque Solar Guindo Santo”, ubicado en el área rural de la comuna de Yungay,
Región de Ñuble.

En este estudio se elaboró el inventario de emisiones de contaminantes atmosféricos
actualizado de las etapas de construcción, operación y cierre del Proyecto.

La ejecución del estudio de calidad de aire del Proyecto consideró la meteorología del
año 2019 generada por el modelo meteorológico de mesoescala WRF, de acuerdo a los
requerimientos del SEA. La meteorología generada por WRF fue validada a través de un
análisis de incertidumbre considerando la meteorología de la estación Termas de
Chillán.

De los resultados obtenidos del análisis meteorológico de la información de la estación
Termas de Chillán en comparación con los datos meteorológicos entregados por el
modelo WRF se observa que hay diferencias, las que pueden provocar una
sobreestimación de la concentración de los contaminantes atmosféricos en la zona al
modelar con CALPUFF. Por lo tanto, no es necesario aplicar un factor de corrección ya
que se está considerando el peor escenario posible de dispersión atmosférica en la zona
de estudio.

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 37
Santo”

Anexo A

# CAPÍTULO A6: BIBLIOGRAFIA

Garreaud, R. (1995). “Configuraciones Atmosféricas Durante Tormentas Pluviales
en Chile Central”. Meteorológica (Argentina), 19, 73-81.

Inzunza, J. (2000). “Meteorología Descriptiva y Aplicaciones en Chile”. Universidad
de Concepción, Concepción. Chile http://www. udec. cl/~ jinzunza/meteo/cap1.
pdf.

Stull, R. B. (2012). “An introduction to Boundary Layer Meteorology” (Vol. 13).
Springer Science & Business Media.

i De derivative work: Janitoalevic - Este archivo deriva de: Provincia de Ñuble.svg de B1mbo, CC BY-SA
4.0, https://commons.wikimedia.org/w/index.php?curid=50211914

ii De derivative work: Janitoalevic - Este archivo deriva de: Mapa loc Biobío.svg de B1mbo, CC BY-SA 4.0,
[https://commons.wikimedia.org/w/index.php?curid=50212397](https://commons.wikimedia.org/w/index.php?curid=50212397)

Propuesta EM2020/200-16 | AAKTEI

“Inventario de Emisiones y Modelación de Calidad de Aire para el Proyecto Parque Solar Guindo 38
Santo”

Anexo A