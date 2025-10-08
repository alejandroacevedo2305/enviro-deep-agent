---
title: Sin título
author: usuario
date: D:20140728145428-04'00'
language: es
type: report
pages: 70
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MODELACION ATMOSFÉRICA. DECLARACIÓN DE IMPACTO AMBIENTAL “REGULARIZACIÓN Y CONTINUIDAD PLANTA DE ASFALTO E IMPLEMENTACIÓN DE EXTRACCIÓN Y PROCESAMIENTO DE ÁRIDOS”
-->

# MODELACION ATMOSFÉRICA. DECLARACIÓN DE IMPACTO AMBIENTAL “REGULARIZACIÓN Y CONTINUIDAD PLANTA DE ASFALTO E IMPLEMENTACIÓN DE EXTRACCIÓN Y PROCESAMIENTO DE ÁRIDOS”

**JULIO 2014**

**ÍNDICE GENERAL**

**1.** **Introducción ............................................................................................................ 7**

**2.** **Modelo Calpuff ........................................................................................................ 7**

**3.** **Metodología ............................................................................................................. 9**

**3.1** **Recopilación y procesamiento de datos meteorológicos y de uso de**
**suelo del área de estudio para año base 2012 .................................................... 9**

**3.1.1** **Área de Estudio ........................................................................................ 9**

**3.1.2** **Información meteorológica y geofísica ............................................ 10**

**3.1.3** **Procesamiento de datos en CALMET ................................................. 11**

**3.2** **Recopilación y procesamiento del escenario de emisión propuesto**
**para la modelación en CALPUFF ........................................................................... 12**

**3.2.1.** **Fuentes de área ...................................................................................... 13**

**3.2.2.** **Fuentes puntuales ................................................................................. 14**

**3.3.** **Análisis de los resultados ............................................................................ 18**

**3.3.1.** **Marco Legal Aplicable ........................................................................... 18**

**4.** **Resultados. ............................................................................................................ 19**

**4.1.** **Caracterización Geofísica ............................................................................ 19**

**4.1.1.** **Topografía ............................................................................................... 19**

**4.2.** **Caracterización Meteorológica ................................................................... 20**

**4.2.1.** **Viento ....................................................................................................... 20**

**4.1.1.** **Temperatura y humedad relativa del aire ........................................ 38**

**4.3.** **Concentración de contaminantes atmosféricos ..................................... 40**

**4.3.1.** **Curvas de iso-concentración Escenario No1 .................................... 42**

**4.4.** **Evaluación discreta de las emisiones de la futura planta de Asfalto . 56**

**5.** **Conclusión .............................................................................................................. 69**

Página **2** de **70**

**Índice de Tablas**

**Tabla 1.** Coordenadas UTM del área de estudio. Datum WGS-84, Huso 18 Sur. ........ 10

**Tabla 2.** Datos meteorológicos y geofísicos considerados en la modelación. ............. 11

**Tabla 3.** Principales emisiones atmosféricas areales generadas en el proyecto.......... 13

**Tabla 4.** Emisiones atmosféricas puntuales generadas en la producción de asfalto. ... 14

**Tabla 5.** Coordenadas de fuentes puntuales. ......................................................... 16

**Tabla 6.** Coordenadas y superficies de fuentes de área. ......................................... 16

**Tabla 7.** Emisiones atmosféricas areales usadas en la modelación CALPUFF. ............ 17

**Tabla 8.** Emisiones atmosféricas areales usadas en la modelación CALPUFF. ............ 17

**Tabla 9.** Normas de calidad aplicables al proyecto ................................................ 18

**Tabla 10.** Dirección y velocidad de viento estacional, estación Museo Ferroviario. .... 27

**Tabla 11.** Dirección y velocidad de viento estacional, medidas en la estación
meteorológica Las Encinas. ................................................................................... 29

**Tabla 12.** Coordenadas Receptores discretos evaluados en la modelación ............... 56

**Tabla 13.** Concentraciones de MP10 (Percentiles 98, promedio 24 horas) modeladas
en receptores discretos en la comuna de Temuco. .................................................. 58

**Tabla 14.** Concentraciones de MP10 (Percentiles 98, promedio 24 horas) modeladas
en las estaciones de monitoreo Museo Ferroviario y Las Encinas. ............................. 58

**Tabla 15.** Concentraciones de MP10 (anual) modeladas en receptores discretos en la

comuna de Temuco. ............................................................................................. 59

**Tabla 16.** Concentraciones de MP10 (anual) modeladas en las estaciones de
monitoreo Museo Ferroviario y Las Encinas. ........................................................... 59

**Tabla 17** . Concentraciones de MP2,5 (Percentiles 98, promedio 24 horas) modeladas
en receptores discretos en la comuna de Temuco. .................................................. 60

**Tabla 18.** Concentraciones de MP2,5 (Percentiles 98, promedio 24 horas) modeladas
en las estaciones de monitoreo Museo Ferroviario y Las Encinas. ............................. 60

**Tabla 19.** Concentraciones de MP2,5 (anual) modeladas en receptores discretos en la

comuna de Temuco. ............................................................................................. 61

Página **3** de **70**

**Tabla 20.** Concentraciones de MP2,5 (anual) modeladas en las estaciones de
monitoreo Museo Ferroviario y Las Encinas. ........................................................... 61

**Tabla 21.** Concentraciones de NOx (Percentiles 99, promedio horario) modeladas en
receptores discretos en la comuna de Temuco. ....................................................... 63

**Tabla 22.** Concentraciones de NOx (Percentiles 99, promedio horario) modeladas en
las estaciones de monitoreo Museo Ferroviario y Las Encinas. .................................. 63

**Tabla 23.** Concentraciones de NOx (anual) modeladas en receptores discretos en la

comuna de Temuco. ............................................................................................. 64

**Tabla 24.** Concentraciones de NOx (anual) modeladas en las estaciones de monitoreo
Museo Ferroviario y Las Encinas. ........................................................................... 64

**Tabla 25.** Concentraciones de SO 2 (Percentiles 99, promedio diario) modeladas en
receptores discretos en la comuna de Temuco. ....................................................... 65

**Tabla 26.** Concentraciones de SO 2 (Percentiles 99, promedio diario) modeladas en las
estaciones de monitoreo Museo Ferroviario y Las Encinas. ....................................... 65

**Tabla 27.** Concentraciones de SO 2 (anual) modeladas en receptores discretos en la

comuna de Temuco. ............................................................................................. 66

**Tabla 28.** Concentraciones de SO 2 (anual) modeladas en las estaciones de monitoreo
Museo Ferroviario y Las Encinas. ........................................................................... 66

**Tabla 29.** Concentraciones de SO 2 (Percentiles 99,73, promedio horario) modeladas
en receptores discretos en la comuna de Temuco. .................................................. 67

**Tabla 30.** Concentraciones de SO 2 (Percentiles 99,73, promedio horario) modeladas
en las estaciones de monitoreo Museo Ferroviario y Las Encinas. ............................. 67

**Tabla 31.** Concentraciones de CO (Percentiles 99, promedio 8 horas) modeladas en
receptores discretos en la comuna de Temuco. ....................................................... 68

**Tabla 32.** Concentraciones de CO (Percentiles 99, promedio 8 horas) modeladas en
las estaciones de monitoreo Museo Ferroviario y Las Encinas. .................................. 68

Página **4** de **70**

**Índice de Figuras**

**Figura 1.** Área de estudio utilizada para la modelación de contaminantes atmosféricos.

.......................................................................................................................... 10

**Figura 2.** Esquema de la recopilación y procesamiento de datos CALMET. ............... 12

**Figura 3.** Principales Fuentes de Emisión de Extracción, procesamiento y producción

de asfalto. ........................................................................................................... 15

**Figura 4.** Elevación de terreno del área de estudio ................................................ 19

**Figura 5.** Rosa de viento anual Estación Museo Ferroviario ..................................... 21

**Figura 6.** Viento anual en estación Museo Ferroviario............................................. 22

**Figura 7.** Rosa de viento anual Estación Las Encinas .............................................. 23

**Figura 8.** Viento anual en estación Las Encinas. .................................................... 24

**Figura 9.** Rosas de viento de estaciones Museo Ferroviario y Las encinas. ............... 25

**Figura 10.** Rosas de viento según estación del año, Museo Ferroviario. ................... 26

**Figura 11.** Velocidad del viento estacional en estación Museo Ferroviario. ............... 27

**Figura 12.** Rosas de viento según estación del año, Las Encinas. ............................ 28

**Figura 13.** Velocidad de viento Estación Las Encinas. ............................................. 30

**Figura 14.** Rosas de viento según horas del día en verano, Museo Ferroviario. ........ 31

**Figura 15.** Rosas de viento según horas del día en otoño, Museo Ferroviario. .......... 32

**Figura 16.** Rosas de viento según horas del día en invierno, Museo Ferroviario. ....... 33

**Figura 17.** Rosas de viento según horas del día en primavera, Museo Ferroviario. .... 34

**Figura 18.** Rosas de viento según horas del día en verano, Las Encinas. ................. 35

**Figura 19.** Rosas de viento según horas del día en otoño, Las Encinas. ................... 36

**Figura 20.** Rosas de viento según horas del día en invierno, Las Encinas. ................ 37

**Figura 21.** Rosas de viento según horas del día en invierno, Las Encinas. ................ 38

**Figura 22.** Temperatura y humedad relativa según hora del día en estación Museo
Ferroviario - Temuco, año 2012. ............................................................................ 39

Página **5** de **70**

**Figura 22.** Temperatura del aire según hora del día en estación Museo Ferroviario Temuco, año 2012. .............................................................................................. 40

**Figura 23.** Fuente areales y fijas de emisión del proyecto. ..................................... 41

**Figura 24.** Curvas de iso-concentración diaria (μg/m [3] ) para el MP10. ...................... 42

**Figura 25.** Curvas de iso-concentración anual (μg/m [3] ) para el MP10. ...................... 43

**Figura 26.** Curvas de iso-concentración diaria (μg/m [3] ) para el MP2,5. ..................... 45

**Figura 27.** Curvas de iso-concentración anual (μg/m [3] ) para el MP2,5. ..................... 46

**Figura 28.** Curvas de iso-concentración horaria (μg/m [3] ) para el NOx. ..................... 48

**Figura 29.** Curvas de iso-concentración anual (μg/m [3] ) para NOx. ........................... 49

**Figura 30.** Curvas de iso-concentración horaria (μg/m [3] ) para el SO 2 . ...................... 51

**Figura 31.** Curvas de iso-concentración diaria (μg/m [3] ) para el SO 2 .......................... 52

**Figura 32.** Curvas de iso-concentración anual (μg/m [3] ) para el SO 2 . ......................... 54

**Figura 33.** Curvas de iso-concentración para 8 horas (mg/m [3] ) para el CO. .............. 55

**Figura 34.** Receptores discretos utilizados en la modelación atmosférica (cercanos a la
planta). ............................................................................................................... 56

**Figura 35** . Receptores discretos utilizados en la modelación atmosférica. (Estaciones
de Monitoreo con representatividad Poblacional) ..................................................... 57

Página **6** de **70**

**1.** **Introducción**

El proyecto corresponde a la extracción de áridos sobre los 74.667 m [3] en un tramo del
río Cautín, el procesamiento de los mismos y la producción de mezclas asfálticas, con
la finalidad de satisfacer la demanda de este producto destinado a la pavimentación de
caminos. La planta de asfalto se encuentra instalada de acuerdo a la Resolución de
Calificación Ambiental favorable RCA N°212 del 12 de Diciembre de 2007, con una vida
útil de 5 años, la cual ha cumplido su período de operación, es por ello la necesidad de
ampliar su vida útil.

El predio donde se proyecta la extracción de áridos y se encuentra instalada la planta
de asfalto se ubica en el Camino Viejo a Cajón km 5 sector Feria Los Camiones,
aproximadamente a 5 Km al Norte de la ciudad de Temuco, entre las comunas de
Temuco y Padre las Casas, novena región de la Araucanía. La zona de extracción
corresponde a un tramo de 1500 m de longitud aproximadamente, ubicado a 3 km
aguas abajo del puente Cautín (Ruta 5 Sur). Por otro lado la planta de asfalto ya se
encuentra instalada y se ubica a 0,2 km al interior del predio desde el Camino Viejo a
Cajón.

Para evaluar el efecto de las emisiones futuras de se utilizó un modelo de dispersión
tipo puff, llamado CALPUFF, recomendado por el Ministerio de Medio Ambiente en la
Guía para el uso de modelos de calidad del aire en el SEIA, publicada el año 2012.

CALPUFF es un modelo de dispersión utilizado en todo el mundo para simulaciones de
concentraciones ambientales de las emisiones de operaciones normales. CAPUFF se
utilizan para establecer, desarrollar y analizar escenarios de emisión y regulación.

**2.** **Modelo Calpuff**

De acuerdo a la “Guía para el uso de modelos de calidad del aire en el SEIA” Los
modelos existentes se pueden clasificar en Gaussianos, Eulerianos, Lagrangeanos y
tipo “Puff”.

La modelación de la dispersión atmosférica de los contaminantes provenientes del
proyecto que se somete a evaluación ambiental, se realizó con un modelo tipo “Puff”,
específicamente el modelo CALPUFF.

Los modelos tipo “puff” son una combinación entre los modelos Gaussianos y los
modelos Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de
contaminantes provenientes de una emisión instantánea, llamada “puff”, a lo largo de
una trayectoria. Su aproximación matemática consiste en estimar la dispersión en
forma Gaussiana en cada punto de una trayectoria; es decir, los modelos tipo “puff”
sólo requieren una trayectoria por “puff”, lo que hace su cálculo mucho más rápido. En
el caso de emisiones continuas, se simulan las trayectorias y la dispersión Gaussiana
de muchos “puffs”.

Página **7** de **70**

Considerando las características del terreno, las distintas unidades geomorfológicas del
área de influencia del proyecto y el dominio de la modelación se consideró utilizar el
modelo CALPUFF para simular la dispersión de los contaminantes generados en por la
operación actual y futura del proyecto.

CALPUFF, es un modelo no estacionario desarrollado por “TRC Scientists”, ha sido
usado en una amplia variedad de estudios de modelación de calidad del aire,
incluyendo: deposición de contaminantes tóxicos, impactos de incendios forestales,
evaluaciones de visibilidad y un largo rango de estudios de transporte.

CALPUFF es un modelo completo que incorpora herramientas para procesar datos
meteorológicos y geofísicos, modelos de dispersión y pos procesamiento. Dicho modelo
es recomendado por la agencia de protección ambiental (EPA) para modelar transporte
a larga distancia de contaminantes.

CALPUFF se compone de tres módulos

 CALMET: Es un modelo meteorológico que desarrolla campos horarios de viento
y temperatura en una grilla de tres dimensiones. También asocia campos en
dos dimensiones de altura y usos de suelo.

 CALPUFF: Es un modelo de transporte y dispersión emitido desde fuentes
modeladas, simulando procesos de dispersión y transformación. CALPUFF utiliza
los datos generados por CALMET. Los archivos de salida de CALPUFF contienen
las concentraciones horarias o deposición por hora de flujos evaluados en
receptores seleccionados.

 CALPOST: Es usado para procesar esos archivos generados por CALMET y
CALPUFF, produciendo tabulaciones que resumen los resultados de la
simulación, identificando por ejemplo, la concentración promedio de 24 horas
para cada receptor.

Ecuación del modelo CALPUFF

La ecuación básica que utiliza el modelo para realizar la modelaciones es la siguiente:

~~[~~

[] ] ~~[[]~~

[]]

]

⁄

∑

~~[~~

Página **8** de **70**

Dónde:

**C** : concentración a nivel del suelo (g/m [3] ),

**Q:** masa de contaminantes (g) en la nube.

**σ** **x** : desviación estándar (m) de la distribución de Gauss en el viento a lo largo de la
dirección.

**σ** **y** **:** desviación estándar (m) de la distribución de Gauss en el viento de costado

**σ** **z** **:** desviación estándar (m) de la distribución de Gauss en la dirección vertical.

**d** **a** **:** distancia (m) del centro de la nube al receptor en la dirección del viento a lo
largo.

**d** **c** **:** distancia (m) del centro de la nube al receptor en la dirección de viento cruzado.

**3.** **Metodología**

La modelación de las dispersión de contaminantes atmosféricos se realizó de acuerdo a
la siguiente metodología.

**3.1** **Recopilación y procesamiento de datos meteorológicos y de uso de**
**suelo del área de estudio para año base 2012**

3.1.1 Área de Estudio

Para la realización de esta etapa se utilizó el modelo CALMET, el cual desarrolla e
integra datos meteorológicos, análisis de alturas y uso de suelo. Generando grillas de
dos y tres dimensiones que posteriormente se utilizaron para la modelación de
dispersión de contaminantes.

El primer paso realizado fue seleccionar el área de estudio considerada para la
modelación en CALMET, la cual incluyo el área de extracción y procesamiento de áridos
y producción de asfalto de la empresa Bitumix CVV Ltda.

Para el estudio de la dispersión de emisiones se consideró una grilla de 20 x 20 km [2], la
cual se dividió en 75 celdas de 0,27 x 0,27 km [2 ] cada una.

En la Figura 1 se puede observar el área de estudio considerada y en la Tabla 1 se
presentan las coordenadas UTM de dicha área.

Página **9** de **70**

**Figura 1.** Área de estudio utilizada para la modelación de contaminantes atmosférico.

**Tabla 1.** Coordenadas UTM del área de estudio. Datum WGS-84, Huso 18 Sur.

|Punto|Este (m)|Norte (m)|
|---|---|---|
|A|701.375|5.702.888|
|B|701.375|5.722.888|
|C|721.375|5.722.888|
|D|721.375|5.702.888|

3.1.2 Información meteorológica y geofísica

El segundo paso fue la recopilación de datos de las distintas fuentes de información,
como por ejemplo, estaciones meteorológicas de altura y de superficie de la comuna
de Temuco, provenientes de sondeos y modelos meteorológicos, además de la
obtención de modelos de elevación digital (DEM) con sus respectivos usos de suelo.

Página **10** de **70**

Para la recopilación de datos meteorológicos se consideró el 2012 como año base,
debido a que dicho año presenta una mayor disponibilidad de datos meteorológicos y

de calidad de aire.

En la Tabla 2, se presentan las categorías y el tipo de datos con las respectivas fuentes
de información.

**Tabla 2.** Datos meteorológicos y geofísicos considerados en la modelación.

|Categoría de datos|Parámetro|Fuente|
|---|---|---|
|Meteorología de altura|Temperatura|National<br>Oceanic<br>and<br>Atmospheric Administration<br>(NOAA)|
|Meteorología de altura|Presión|Presión|
|Meteorología de altura|Velocidad de viento|Velocidad de viento|
|Meteorología de altura|Dirección de viento|Dirección de viento|
|Meteorología de Superficie|Temperatura|Estación Museo Ferroviario<br>Estación Las Encinas|
|Meteorología de Superficie|Presión|Estación Museo Ferroviario<br>Estación Las Encinas|
|Meteorología de Superficie|Velocidad de viento|Estación Museo Ferroviario<br>Estación Las Encinas|
|Meteorología de Superficie|Dirección de viento|Estación Museo Ferroviario<br>Estación Las Encinas|
|Meteorología de Superficie|Humedad relativa|Estación Museo Ferroviario<br>Estación Las Encinas|
|Geofísicos|Elevación de Terreno|United<br>Stated<br>Geological<br>Survey (USGS)|
|Geofísicos|Uso de Suelo|Uso de Suelo|

3.1.3 Procesamiento de datos en CALMET

El tercer paso, fue procesamiento de los datos en el modelo meteorológico CALMET.
Como ya se mencionó CALMET integra datos, los cuales son ingresados en tres preprocesadores dentro del modelo meteorológico, estos son:

Pre-procesador de datos de altura (READ62): se ingresan datos de temperatura,
presión, dirección del viento, velocidad de viento.

Página **11** de **70**

Pre-procesador de datos superficiales (SMERGE): se ingresan datos superficiales
como por ejemplo: humedad relativa, temperatura, presión superficial, dirección
del viento y velocidad de viento.

Pre-procesador de datos Geofísicos (MAKEGEO): se ingresan datos de elevación del
terreno y de usos de suelo.

En la Figura 2 se observa un esquema con los datos ingresados a los pre-procesadores
y los archivos generados (.DAT) que procesa CALMET.

**Figura 2.** Esquema de la recopilación y procesamiento de datos CALMET.

**3.2** **Recopilación y procesamiento del escenario de emisión propuesto**
**para la modelación en CALPUFF**

Para evaluar la dispersión de los contaminantes atmosféricos proveniente de la
operación de la planta, se utilizó la información presente en la Declaración de impacto
ambiental, específicamente las estimaciones de emisiones y Descripción de proyecto.
Para la modelación se consideró la emisión de contaminantes atmosféricos proveniente
de las principales actividades involucradas en el proceso de operación de la planta de

Página **12** de **70**

extracción áridos y producción de asfalto. A continuación se presentan las emisiones de
los procesos productivos en la etapa de operación.

**3.2.1.** **Fuentes de área**

En la Tabla 3 se presentan las emisiones areales que genera el proyecto sujeto a
evaluación ambiental, para ser consideradas en la modelación.

**Tabla 3.** Principales emisiones atmosféricas areales generadas en el proyecto.

|Emisiones de área de extracción y procesamiento de áridos (ton/año)|Col2|Col3|
|---|---|---|
|**Actividad**|**MP10**|**MP2.5**|
|Transferencia de material, carguío y volteo|0,0214|0,00325|
|Erosión de material en pilas|0,00011|-|
|Planta chancadora (chancadores, harnero,<br>cintas<br>transportadoras,<br>transferencia<br>de<br>material y descarga en buzón)|0,1831|0,0246|
|Transferencia de material, carguío y volteo|0,0566|0,00857|
|Tránsito<br>de<br>camiones<br>en<br>caminos<br>no<br>pavimentados|0,20034|0,02003|
|Tránsito de cargador frontal en caminos no<br>pavimentados|1,93436|0,19343|
|**Emisiones parciales**|**2,396**|**0,250**|
|**Emisiones de área producción de asfalto (ton/año)**|**Emisiones de área producción de asfalto (ton/año)**|**Emisiones de área producción de asfalto (ton/año)**|
|**Actividad**|**MP10**|**MP2.5**|
|Transferencia de material|0,034409|0,005210|
|Erosión material en pilas (área planta de<br>asfalto)|0,00483|-|
|Tránsito<br>de<br>camiones<br>por<br>caminos<br>no<br>pavimentados|1,10249|0,11025|
|**Emisiones parciales**|**1,14172**|**0,11546**|
|**Emisiones Totales**|**3,538**|**0,365**|

Página **13** de **70**

**3.2.2.** **Fuentes puntuales**

En la Tabla 4 se presentan las emisiones puntuales que genera el proyecto sujeto a
evaluación ambiental, para ser consideradas en la modelación.

**Tabla 4.** Emisiones atmosféricas puntuales generadas en la producción de asfalto.

|Actividad|Emisiones Puntuales (ton/año)|Col3|Col4|Col5|
|---|---|---|---|---|
|**Actividad**|**MP10**|**CO**|**NOx**|**SO2 **|
|Calentador Vertical|0,0122|-|-|-|
|Secador de Asfalto|0,6335|3,5810|1,5149|0,3030|
|Equipo Electrógeno|0,4256|3,3440|7,9040|4,9187|

Las fuentes de área se refieren a una serie de fuentes pequeñas, numerosas y
dispersas, que no pueden ser incluidas de manera eficiente en un inventario de fuentes
puntuales, pero que en conjunto pueden afectar la calidad del aire. Por otro lado las
fuentes puntuales son aquellas que se emiten a través de un ducto o chimenea.

Es importante mencionar que en las emisiones utilizadas para la modelación, no se
consideraron las emisiones generadas por la combustión interna de maquinaria y
camiones al interior del proyecto, para ambos procesos. Lo anterior debido a que
dichas emisiones son provenientes de fuentes móviles y son despreciables en
comparación a las emisiones de fuentes areales y puntuales. En la Figura 3 se
presentan las ubicaciones de las fuentes puntuales y de área utilizadas para realizar la
modelación.

Página **14** de **70**

**Figura 3.** Principales Fuentes de Emisión de Extracción, procesamiento y producción

de asfalto.

Tal como se aprecia en la figura anterior, para la modelación de emisiones
atmosféricas, se consideraron fuentes de área y fuentes puntuales. Para efectos de
cálculo, las fuentes de áreas se agruparon en cinco superficies: E1, E2 y E3,
correspondientes a la extracción y procesamiento de áridos y A1 y A2,
correspondientes a la producción de asfalto.

A continuación se detalla cada superficie:

 - **Área E1:** En color rojo en la figura 3, corresponde a emisión areal del proyecto
de extracción y procesamiento de áridos y contiene las siguientes fuentes:
trasferencia de material, carguío y volteo, erosión de pila de acopio, tránsito de
cargador frontal por caminos no pavimentados, tránsito de camiones por
caminos no pavimentados.

 - **Área E2:** En color rojo en la figura 3, corresponde a emisión areal del proyecto
de extracción y procesamiento de áridos y contiene las siguientes fuentes:
planta chancadora (chancadores, harnero, cinta transportadora, transferencia
de material (carga) y descarga en buzón).

 - **Área E3:** En color rojo en la figura 3, corresponde a las emisiones areales del
proyecto de extracción de áridos y contiene las siguientes fuentes:
transferencia de material, erosión de material en pilas de acopio. Sin embargo,

Página **15** de **70**

como tasa de emisión sólo se considerará transferencia de material, ya que
toda la erosión de pilas de acopio para extracción y procesamiento de áridos se
incluyó en E1.

 - **Área A1:** En color azul en la figura 3, corresponde a las emisiones areales del
proyecto de producción de asfalto y contiene las siguientes fuentes:
Transferencia de material, erosión de material en pilas y tránsito de camiones
en caminos no pavimentados.

Con respecto a las fuentes puntuales, se consideraron tres: la chimenea del secador de
asfalto, chimenea del calentador vertical y el escape del equipo electrógeno. A
continuación se presenta las coordenadas y superficies de las fuentes puntuales y de
área consideradas en la modelación.

**Tabla 5.** Coordenadas de fuentes puntuales.

|Fuente|UTM, WGS-84, Huso 18 S|Col3|
|---|---|---|
|**Fuente**|**Este (m)**|**Norte (m)**|
|Calentador vertical|715.069|5.713.887|
|Secador de Asfalto|715.058|5.713.895|
|Equipo Electrógeno|715.163|5.713.736|

**Tabla 6.** Coordenadas y superficies de fuentes de área.

|Zona|Superficie (m2)|Vertices (UTM, WGS-84, Huso 18 S)|Col4|
|---|---|---|---|
|**Zona**|**Superficie (m2) **|**Este (m)**|**Norte (m)**|
|E1|5.818|715.195|5.713.782|
|E1|5.818|715.194|5.713.724|
|E1|5.818|715.296|5.713.776|
|E1|5.818|715.296|5.713.720|
|E2|2.722|715.118|5.713.758|
|E2|2.722|715.142|5.713.710|
|E2|2.722|715.164|5.713.779|
|E2|2.722|715.188|5.713.733|
|E3|3.318|715.048|5.713.773|
|E3|3.318|715.073|5.713.708|
|E3|3.318|715.091|5.713.789|
|E3|3.318|715.117|5.713.723|
|A1|2.740|715.082|5.713.852|
|A1|2.740|715.103|5.713.793|
|A1|2.740|715.123|5.713.865|
|A1|2.740|715.145|5.713.806|

Página **16** de **70**

Las áreas de las zonas de alimentación y acopio se calcularon a través del software
Google Earth Pro. Finalmente en las siguientes tablas se detallan las emisiones
(ton/año/m [2] ) ingresadas al modelo CALPUFF, para calcular la dispersión atmosférica.

**Tabla 7.** Emisiones atmosféricas areales usadas en la modelación CALPUFF.

|Zona|Emisión MP10<br>(ton/año)|Área (m2)|Emisión MP10<br>(ton/año/m2)|
|---|---|---|---|
|E1|2,156|5.818|0,000371|
|E2|0,183|2.722|0,0000673|
|E3|0,057|3.318|0,0000171|
|A1|1,142|2.740|0,000417|

**Tabla 8.** Emisiones atmosféricas areales usadas en la modelación CALPUFF.

|Zona|Emisión MP10<br>(ton/año)|Área (m2)|Emisión MP10<br>(ton/año/m2)|
|---|---|---|---|
|E1|0,217|5.818|0,0000372|
|E2|0,025|2.722|0,00000904|
|E3|0,009|3.318|0,00000258|
|A1|0,115|2.740|0,0000421|

Página **17** de **70**

**3.3.** **Análisis de los resultados**

Para analizar los resultados de la modelación de dispersión de contaminantes
atmosféricos, se realizaron mapas de iso-concentración de las emisiones generadas por
el proyecto. Dichos mapas permitieron evaluar los niveles de concentración, de los
diferentes contaminantes, en toda el área de estudio. Por otro lado, con el fin de
analizar el impacto en la calidad del aire en los poblados más cercanos, se realizó una
modelación discreta, en receptores específicos, para obtener la concentración en el
aire de la comuna de Temuco. Dichos valores fueron comparados con la normativa
respectiva y la 2 estaciones de monitoreo presentes en la comuna de Temuco.

**3.3.1.** **Marco Legal Aplicable**

Con el fin de determinar el cumplimiento de la normativa ambiental aplicable, se
consideraron las normas de calidad primaria y secundaria de aire para los
contaminantes asociados a la Producción de Asfalto. En la siguiente tabla se presenta
un resumen con los valores máximos considerados para los diferentes contaminantes
asociados a la operación del proyecto.

**Tabla 9.** Normas de calidad aplicables al proyecto

|Normativa de calidad del aire primaria|Col2|Col3|Col4|
|---|---|---|---|
|**Contaminante**|**Límite Norma**|**Concentración**|**Decreto**|
|Material Particulado<br>(MP10)|150 μg/m~~3~~N|Máxima Diaria|N° 20/2013<br>MMA|
|Material Particulado<br>(MP10)|50 μg/m3N <br>|Media anual**1**|Media anual**1**|
|Material Particulado<br>(MP2,5)|50 μg/m~~3~~N|Máxima Diaria|N° 12/2011<br>MMA|
|Material Particulado<br>(MP2,5)|20 μg/m3N <br>|Media anual|Media anual|
|Dióxido de azufre (SO2)|80 μg/m~~3~~N <br>|Media anual|N° 113/2002<br>MINSEGPRES|
|Dióxido de azufre (SO2)|250 μg/m~~3~~N|Máxima diaria|Máxima diaria|
|Dióxido de Nitrógeno<br>(NO2)|400 μg/m3N|1 hora|N° 114/2002<br>MNSEGPRES|
|Dióxido de Nitrógeno<br>(NO2)|100 μg/m3N|Media anual|Media anual|
|Monóxido de Carbono<br>(CO)|10 mg/m3N|8 horas|N° 115/2002<br>MINSEGPRES|
|**Normativa de calidad del aire secundaria**|**Normativa de calidad del aire secundaria**|**Normativa de calidad del aire secundaria**|**Normativa de calidad del aire secundaria**|
|**Contaminante**|**Límite Norma**|**Concentración**|**Decreto**|
|Dióxido de azufre SO2|700 μg/m3N|1 hora|N° 22/2010<br>MINSEGPRES|
|Dióxido de azufre SO2|260 μg/m3N|Máxima Diaria|Máxima Diaria|
|Dióxido de azufre SO2|60 μg/m3N|Media Anual|Media Anual|

**1** Vigente sólo hasta el 2017.

Página **18** de **70**

**4.** **Resultados.**

A continuación se presentan los principales resultados de la modelación de emisiones
atmosféricas. Dichos resultados incluyen los datos generados por los procesadores
CALMET, CALPUFF Y CALPOST.

Se procesaron los datos geofísicos y meteorológicos (altura y superficie), los resultados
obtenidos con el procesador CALMET se presentan a continuación.

**4.1.** **Caracterización Geofísica**

**4.1.1.** **Topografía**

**Figura 4.** Elevación de terreno del área de estudio.

En la figura anterior se observa que Temuco está rodeado por 2 relieves montañosos
que se encuentran al norte y al sur de la ciudad, siendo el más prominente, el del
norte. Esta topografía influirá tanto en las velocidades de vientos como en la dirección,
así como en la dispersión de contaminantes.

Página **19** de **70**

**4.2.** **Caracterización Meteorológica**

**4.2.1.** **Viento**

A continuación, se presentan los resultados de las estaciones meteorológicas más
cercanas al proyecto, correspondiente a estación Meteorológica Museo Ferroviario y la
estación Las Encinas.

 **Dirección y velocidad de vientos anuales**

A continuación se presentan las rosas de viento anual para las estaciones
meteorológicas, el cual es un método gráfico que consiste en representar
conjuntamente las distribuciones de frecuencias de la dirección y la velocidad del
viento. Las direcciones se agruparon en 16 clases representando la dirección desde
donde sopla el viento (N, NNE, NE, ENE, E, ESE, SE, SSE, S, SSO, SO, OSO, O, ONO,
NO, NNO), y las velocidades se discriminaron en intervalos. Se consideró como calma
(velocidad del viento muy baja o la) valores menores a 0,5 [m/s]. Las barras del
gráfico estas divididas en segmentos de diferentes tamaño y color. Cada segmento de
color representa un rango específico de velocidad del viento en unidades de [m/s]. El
tamaño o largo de cada segmento dentro de cada barra es proporcional a la
frecuencia de los vientos que soplan en ese rango. La frecuencia se representa
porcentualmente en los diferentes círculos concéntricos del gráfico.

Además, se presentan gráficos de barra para demostrar la dominancia de la velocidad

de los vientos.

Página **20** de **70**

a) Estación meteorológica Museo Ferroviario

**Figura 5.** Rosa de viento anual Estación Museo Ferroviario.

Página **21** de **70**

**Figura 6.** Viento anual en estación Museo Ferroviario.

De acuerdo a la dirección de vientos registrados el año 2012 en la estación Museo
Ferroviario, se puede apreciar que según el vector resultante, los vientos
predominantes provienen de la dirección sur (S) con un 45% de frecuencia.

Con respecto a las velocidades de viento, se puede apreciar que predominan las
velocidades entre 0,5-2,1 [m/s] con un 60% de frecuencia, luego siguen las
velocidades entre 2,1 - 3,6 [m/s] con 17,9% y las velocidades calmas (cercanas a 0

[m/s]) con un 16,8% de frecuencia. Se observa que los vientos son mayoritariamente
lentos y que existe un gran porcentaje de calmas, dificultando la dispersión de

contaminantes.

Página **22** de **70**

b) Estación Meteorológica Las Encinas

**Figura 7.** Rosa de viento anual Estación Las Encinas.

Página **23** de **70**

**Figura 8.** Viento anual en estación Las Encinas.

De acuerdo a la dirección de vientos registrados en el año 2012 en estación Las
Encinas, se puede apreciar que según el vector resultante, los vientos predominantes
provienen de la dirección oeste suroeste (OSO) con un 23% de frecuencia.

Con respecto a las velocidades de viento, se puede apreciar que predominan las
velocidades entre 0,5 - 2,1 [m/s] con un 60,8% de frecuencia y las velocidades entre
2,1-3,6 [m/s] con un 19,2% de frecuencia. Las calmas alcanzan un 12,1% de
frecuencia. En esta estación se puede observar que las velocidades aumentan
levemente, dado por la posición geográfica de la estación, sin embargo siguen siendo
velocidades bajas y un porcentaje considerable de calmas, por lo que se concluye que
no existen vientos favorables para una

Adicionalmente, en la Figura 9, se puede observar las rosas de vientos de ambas
estaciones con sus respectivas ubicaciones dentro del área de estudio.

Página **24** de **70**

**Figura 9.** Rosas de viento de estaciones Museo Ferroviario y Las Encinas.

En la figura se puede observar la influencia de la topografía en el patrón de vientos,
apreciándose la acción de los cerros que desvía los vientos provocando la rosa
observada en Museo Ferroviario, recordando que Temuco se encuentra entre 2 cerros,
uno ubicado al norte y otro al sur del centro de la ciudad.

Página **25** de **70**

**Dirección y velocidad de viento estacional**

a) Estación meteorológica Museo Ferroviario:

**Figura 10.** Rosas de viento según estación del año, Museo Ferroviario.

En las rosas de vientos estacionales medidos en Museo Ferroviario se puede observar
que durante todo el año los vientos vienen principalmente del sur, existiendo una
variación de vientos predominantes que fluctúa entre direcciones oeste suroeste (OSO)
y sureste (SE), salvo en algunos meses de primavera donde existen vientos que soplan
desde el este (E) y este noreste (ENE).

En la Tabla 10, se observan las frecuencias según rango de velocidades.

Página **26** de **70**

**Tabla 10.** Dirección y velocidad de viento estacional, estación Museo Ferroviario.

|Estaciones|Dirección de Vector<br>Resultante|Velocidades<br>Predominantes y Calmas<br>(m/s)|Frecuencia<br>%|
|---|---|---|---|
|Verano|OSO (53%)|0,5-2,1|68,3|
|Verano|OSO (53%)|2,1-3,6|16,6|
|Verano|OSO (53%)|3,6-5,7|6,5|
|Verano|OSO (53%)|Calma|8,6|
|Otoño|S (54%)|0,5-2,1|60,9|
|Otoño|S (54%)|2,1-3,6|14,5|
|Otoño|S (54%)|3,6-5,7|3,6|
|Otoño|S (54%)|Calmas|20,3|
|Invierno|SSE (78 %)|0,5-2,1|58,1|
|Invierno|SSE (78 %)|2,1-3,6|15,7|
|Invierno|SSE (78 %)|3,6-5,7|3,2|
|Invierno|SSE (78 %)|Calmas|21,8|
|Primavera|SE (44 %)|0,5-2,1|55,7|
|Primavera|SE (44 %)|2,1-3,6|22,3|
|Primavera|SE (44 %)|3,6-5,7|5,1|
|Primavera|SE (44 %)|Calmas|16,9|

A continuación se presenta gráficamente la velocidad de los vientos en estación Museo
Ferroviario para cada estación del año.

**Figura 11.** Velocidad del viento estacional en estación Museo Ferroviario.

Página **27** de **70**

En la tabla y gráfico anterior se puede apreciar que los vientos no favorecen la
dispersión de contaminantes, debido a una considerable presencia de velocidades
calma (>16 %), salvo en los meses de verano donde las calmas disminuyen a 8,6%.

La estación de verano es la que presenta las condiciones más favorables para la
dispersión de los contaminantes, debido a que presenta la mayor frecuencia de rangos
de altas velocidades entre 3,6-5,7 [m/s] (6,5%) y la menor frecuencia de calmas
(8,6%). Por otro lado la estación más desfavorable es invierno, ya que posee la
frecuencia más baja de altas velocidades (3,2%) y la mayor frecuencia de calmas
(21,8%).

b) Estación meteorológica Las Encinas:

**Figura 12.** Rosas de viento según estación del año, Las Encinas.

Con respecto a Estación Las encinas se observa que durante todas las estaciones del
año los vientos vienen principalmente desde el oeste, existiendo una variación que
fluctúa entre oeste suroeste (OSO) y oeste noroeste (ONO). Sin embargo, existen

Página **28** de **70**

algunos episodios ocurridos durante otoño e invierno donde aparecen fuertes
componentes noreste (NE) que se asocian a frentes de mal tiempo.

**Tabla 11.** Dirección y velocidad de viento estacional, medidas en la estación

meteorológica Las Encinas.

|Estaciones|Dirección de Vector<br>Resultante|Col3|Velocidades<br>Predominantes y Calmas<br>(m/s)|Col5|Frecuencia<br>%|
|---|---|---|---|---|---|
|Verano|Verano|OSO (50 %)|0,5-2,1|54,5|54,5|
|Verano|Verano|OSO (50 %)|2,1-3,6|23,1|23,1|
|Verano|Verano|OSO (50 %)|3,6-5,7|10,0|10,0|
|Verano|Verano|OSO (50 %)|Calma|12,1|12,1|
|Otoño|Otoño|O (12 %)|0,5-2,1|63,7|63,7|
|Otoño|Otoño|O (12 %)|2,1-3,6|16,2|16,2|
|Otoño|Otoño|O (12 %)|3,6-5,7|5,8|5,8|
|Otoño|Otoño|O (12 %)|Calmas|13,4|13,4|
|Invierno|Invierno|ONO (8 %)|0,5-2,1|62,5|62,5|
|Invierno|Invierno|ONO (8 %)|2,1-3,6|17,5|17,5|
|Invierno|Invierno|ONO (8 %)|3,6-5,7|6,1|6,1|
|Invierno|Invierno|ONO (8 %)|Calmas|12,6|12,6|
|Primavera|Primavera|OSO (39 %)|0,5-2,1|66,8|66,8|
|Primavera|Primavera|OSO (39 %)|2,1-3,6|22,4|22,4|
|Primavera|Primavera|OSO (39 %)|3,6-5,7|5,4|5,4|
|Primavera|Primavera|OSO (39 %)|Calmas|5,4|5,4|

Página **29** de **70**

**Figura 13.** Velocidad de viento Estación Las Encinas.

Con respecto a las velocidades, al igual que la estación Museo Ferroviario, los datos
registrados en la estación Las Encinas, permiten concluir que en al área de estudio no
se presentan una buena dispersión de contaminantes, debido a que existe un alto
porcentaje de calmas ( >12%) la mayor parte del año, a excepción de los meses de
primavera donde las calmas disminuyen a 5,4%, pero también existe una baja
frecuencia de velocidades altas (3,6 - 5,7 [m/s]) que apenas alcanza 5,4%.

La estación del año que presenta las mejores condiciones de dispersión es verano,
debido a que posee la mayor frecuencia de velocidades altas, mientras que la estación
de otoño es la que tiene menores condiciones de dispersión producto de su gran
cantidad de velocidades calmas y baja cantidad de altas velocidades.

Página **30** de **70**

**Dirección y velocidad de viento en ciclos diarios**

a) Estación meteorológica Museo Ferroviario:

**Figura 14.** Rosas de viento según horas del día en verano, Museo Ferroviario.

Página **31** de **70**

**Figura 15.** Rosas de viento según horas del día en otoño, Museo Ferroviario.

Página **32** de **70**

**Figura 16.** Rosas de viento según horas del día en invierno, Museo Ferroviario.

Página **33** de **70**

**Figura 17.** Rosas de viento según horas del día en primavera, Museo Ferroviario.

En los ciclos diarios de rosas de vientos para la estación Museo Ferroviario, se observa
que para todas las estaciones del año existe un componente oeste y sur oeste que se
acentúa llegada la tarde. Además se observa que las velocidades más altas se alcanzan
entre la tarde y noche, siendo más visible durante las estaciones de primavera y
verano. Por otro lado se observó que generalmente no existen cambios drásticos entre
distintas horas del día, salvo durante los meses de primavera que se observó una
inestabilidad notable entre la mañana y tarde, sin embargo esto no afecta de gran
manera al vector resultante. Algo similar se observó durante los meses de otoño, pero
en menor magnitud.

Página **34** de **70**

b) Estación meteorológica Las Encinas:

**Figura 18.** Rosas de viento según horas del día en verano, Las Encinas.

Página **35** de **70**

**Figura 19.** Rosas de viento según horas del día en otoño, Las Encinas.

Página **36** de **70**

**Figura 20.** Rosas de viento según horas del día en invierno, Las Encinas.

Página **37** de **70**

**Figura 21.** Rosas de viento según horas del día en primavera, Las Encinas.

En los ciclos diarios de rosas de vientos para la estación Las Encinas, se observa que
para todas las estaciones del año existe un aumento de las velocidades de durante las
tardes. También se observa un componente noreste que se hace notar en las
madrugadas y mañanas de Otoño-Invierno, sin embargo las velocidades que se
alcanzan son relativamente bajas (0,5 -2,1 m/s).

En general se observan componentes que varían de madrugada a noche entre
direcciones noroeste y suroeste.

**4.1.1.** **Temperatura y humedad relativa del aire**

En el gráfico que se presenta a continuación se muestran las temperaturas y
humedades relativas promedios como ciclo diario medidas en la estación museo
ferroviario de Temuco en el año base 2012.

Página **38** de **70**

**Figura 22.** Temperatura y humedad relativa según hora del día en estación Museo

Ferroviario - Temuco, año 2012.

En el gráfico anterior se observa la relación inversa entre temperatura del aire y
humedad relativa del aire, donde los niveles más altos de temperatura que se alcanzan
entre las 14 y 17 horas, coinciden con los niveles más bajos de humedad. Por otro lado
las temperaturas más bajas se alcanzan entre las 06 y 08 horas, coincidiendo con los
niveles más altos de humedad.

Para el caso de la temperatura, el máximo promedio alcanzado en la hora 16 fue de
17,47 °C, mientras que la temperatura promedio mínima se alcanzó a la hora 7 y fue
de 8,27°C.

Con respecto a la humedad relativa, el máximo promedio alcanzado en la hora 7 fue de
95,86%, mientras que el promedio mínimo se alcanzó a la hora 16 y fue de 78,1%.

También se presenta el siguiente gráfico de temperaturas indicando las máximas y
mínimas del año 2012.

Página **39** de **70**

**Figura 23.** Temperatura del aire según hora del día en estación Museo Ferroviario
Temuco, año 2012.

En el gráfico anterior se observa que existe una gran variabilidad de temperaturas a lo
largo del año y del día, esto es típico de ciudades ubicadas en la depresión intermedia
o valle longitudinal de Chile. Se observa la presencia de temperaturas extremas, con
mínimas bajo cero que llegan a los -2,7 °C y máximas que llegan a los 35,1 °C.

Es importante destacar que este tipo de comportamiento en las temperaturas da a
origen a eventos de inversión térmica que produce un aumento en la concentración
ambiental de contaminantes atmosféricos, esto se acentúa mucho más en las noches
frías de invierno, donde el aire superficial se enfría de gran manera, más rápido que el
aire superior, produciendo que los contaminantes no se escapen hacia zonas más altas.

**4.3.** **Concentración de contaminantes atmosféricos**

Tal como se menciona en la metodología del presente informe, para analizar el efecto
en la calidad del aire debido al funcionamiento de la planta de extracción de áridos,
procesamiento y producción de asfalto, se definió un escenario de emisión el cual
simula la dispersión de contaminantes provenientes de las zonas A1, E1, E2, E3,
calentador vertical y secado de asfalto, durante todo el año 2012.

La siguiente figura presenta la ubicación espacial de las fuentes de emisión del
Proyecto.

Página **40** de **70**

**Figura 24.** Fuente areales y fijas de emisión del proyecto.

Página **41** de **70**

**4.3.1.** **Curvas de iso-concentración Escenario No1**

**Material Particulado (MP10)**

A continuación se presentan las curvas de iso-concentración del Material Particulado
Respirable (MP10) en μg/m [3], como concentración diaria (24 horas).

**Figura 25.** Curvas de iso-concentración diaria (μg/m [3] ) para el MP10.

En la figura anterior se aprecia el área de estudio (20 x 20 km [2] ), la ubicación de la
planta dentro del área de estudio, y las curvas de iso-concentración para el MP10.

Es importante mencionar que la norma de MP10, establece un valor máximo de 150
μg/m [3], como promedio diario (D.S 20 /2013).

Los resultados de la modelación permiten concluir que las emisiones de material
particulado respirable (MP10) generadas en la futura operación del proyecto no

Página **42** de **70**

generan un aporte significativo, considerando que el máximo valor de percentil 98
modelado tiene un valor de 17 μg/m [3] .

En la figura anterior se puede apreciar que el efecto de MP10 es local, en donde las
concentraciones superiores a 8 μg/m [3] se ubican en un área de 0,26 km [2], la cual
equivale a un 0,065 % del área de estudio. (Áreas calculadas mediante el programa
Google Earth Pro)

A continuación se presentan las curvas de iso-concentración del Material Particulado
(MP10) en μg/m [3], como concentración anual.

**Figura 26.** Curvas de iso-concentración anual (μg/m [3] ) para el MP10.

En la figura anterior se aprecia el área de estudio (20 x 20 km [2] ), la ubicación de la
planta dentro del área de estudio, y la curva de iso-concentración para MP10 como
concentración promedio anual.

Página **43** de **70**

Es importante mencionar que la norma de MP10, establece un valor máximo de 50
μg/m [3], como promedio anual (D.S 20 /2013).

El máximo valor registrado en la modelación fue de 8,7 μg/m [3], dicho valor permite
concluir que las emisiones generadas por el futuro proyecto no generaran emisiones
capaces de alterar la calidad del aíre.

Mediante Google Earth Pro se calculó el área cuya concentración es mayor a 3,1
μg/m [3], el valor de esta superficie tiene un valor de 0,19 km [2] . Esto último permite
concluir que el efecto de las emisiones atmosféricas de la futura planta será de
carácter local y no afectará la zona más poblada de la ciudad de Temuco.

Finalmente se puede concluir que las futuras concentraciones, tanto diarias como
anuales de MP10, serán de carácter local y de baja magnitud.

Las pluma de dispersión indica que las mayores concentraciones serán direccionadas
hacia el norte de la ubicación del proyecto, esto producto de los vientos predominantes

en la zona.

Página **44** de **70**

**Material Particulado (MP2,5)**

A continuación se presentan las curvas de iso-concentración del Material Particulado
Fino (MP2,5) en μg/m [3], como concentración diaria (24 horas).

**Figura 27.** Curvas de iso-concentración diaria (μg/m [3] ) para el MP2,5.

En la figura anterior se aprecia el área de estudio (20 x 20 km [2] ), la ubicación de la
planta dentro del área de estudio, y la curva de iso-concentración para el MP2,5. Es
importante mencionar que la norma de MP2,5, establece un valor máximo de 50
μg/m [3], como promedio diario (D.S 12 /2011).

Mediante el modelo CALPUFF se calculó el máximo valor registrado en el área de
estudio, dicho valor es de 1,68 μg/m [3], equivalente al percentil 98 de la concentración
diaria de MP2,5.

Página **45** de **70**

Como se puede apreciar en la figura anterior, las emisiones de MP2,5 se direccionan,
producto de los vientos, al sector norte de la planta. Además en la figura se observa
que las concentraciones más altas tiene tienen un carácter local y no afectan a la zona
más urbanizada de la comuna de Temuco.

Finalmente, a través de Google Earth Pro, se calculó la superficie con concentraciones
superiores a 0,6 μg/m [3], dicha área presenta una superficie de 0,6 km [2] .

A continuación se presentan las curvas de iso-concentración del Material Particulado
Fino (MP2,5) en μg/m [3], como concentración anual.

**Figura 28.** Curvas de iso-concentración anual (μg/m [3] ) para el MP2,5.

En la figura anterior se aprecia el área de estudio (20x 20 km [2] ), la ubicación de la
planta dentro del área de estudio, y la curva de iso-concentración para el MP2,5.

Es importante mencionar que la norma de MP2,5, establece un valor máximo de 20
μg/m [3], como promedio anual (D.S 12 /2011).

Página **46** de **70**

El máximo valor registrado en la modelación fue de 0,85 μg/m [3], dicho valor permite
concluir que las emisiones generadas por el futuro proyecto no generaran emisiones
capaces de alterar la calidad del aíre.

Mediante Google Earth Pro se calculó el área cuya concentración es mayor a 0,2
μg/m [3], el valor de esta superficie tiene un valor de 0,68 km [2] . Esto último permite
concluir que el efecto de las emisiones atmosféricas de la futura planta será de
carácter local y no afectará la zona más poblada de la ciudad de Temuco.

Finalmente se puede concluir que las futuras concentraciones, tanto diarias como
anuales de MP2,5, serán de carácter local y de baja magnitud.

Las pluma de dispersión indica que las concentraciones serán direccionadas hacia el
noreste del área de estudio, esto producto a los vientos predominantes en la zona.

Página **47** de **70**

**Óxido de Nitrógeno**

A continuación se presentan las curvas de iso-concentración de Óxidos de Nitrógeno
(NOx) en μg/m [3], como concentración horaria.

**Figura 29.** Curvas de iso-concentración horaria (μg/m [3] ) para el NOx.

En la figura anterior se aprecia el área de estudio (20 x 20 km [2] ), la ubicación de la
planta dentro del área de estudio y las curvas de iso-concentración para el NOx.

La norma primaria de calidad del NO 2, establece un valor máximo de 400 μg/m [3], como
promedio horario (D.S 114/2002).

De acuerdo a los resultados de la modelación se registró un valor máximo 124 μg/m [3] .

Mediante Google Earth Pro se calculó el área cuya concentración es mayor a 22 μg/m [3],
esta superficie tiene un valor de 1,37 km [2] lo que equivale a un 0,34% del área estudio.
Esto último permite concluir que el efecto de las emisiones atmosféricas de la futura

Página **48** de **70**

planta será de carácter local y no afectará la zona más poblada de la ciudad de

Temuco.

A continuación se presentan las curvas de iso-concentración de Óxidos de Nitrógeno
(NOx) en μg/m [3], como concentración anual.

**Figura 30.** Curvas de iso-concentración anual (μg/m [3] ) para NOx.

En la figura anterior se aprecia el área de estudio (20 x 20 km [2] ), la ubicación de la
planta dentro del área de estudio y las curvas de iso-concentración para NOx.

La norma primaria de calidad del NO 2, establece un valor máximo de 100 μg/m [3], como
promedio anual (D.S 114/2002).

De acuerdo a los resultados de la modelación se registró un valor máximo de 5,54
μg/m [3] .

Página **49** de **70**

Mediante Google Earth Pro se calculó el área cuya concentración es mayor a 0,9
μg/m [3], el valor de esta superficie tiene un valor de 0,85 km [2] . Esto último permite
concluir que el efecto de las emisiones atmosféricas de la futura planta será de
carácter local y no afectará la zona más poblada de la ciudad de Temuco.

Finalmente, se puede concluir que las máximas concentraciones de NOx, tanto horaria
o anual, no son significativas, si se comparan con la normativa establecidas en el D.S
114/2002.

La pluma de dispersión de emisiones del NOx se direcciona hacia el noreste del área de
estudio, esto debido a la dirección predominante de vientos.

Página **50** de **70**

**Dióxido de Azufre (SO** **2** **)**

A continuación se presentan las curvas de iso-concentración del Dióxido de Azufre
(SO 2 ) en μg/m [3], como concentración horaria.

**Figura 31.** Curvas de iso-concentración horaria (μg/m [3] ) para el SO 2 .

La norma secundaria de calidad del SO 2, establece un valor máximo de 700 μg/m [3],
como promedio horario (D.S 22/2010).

De acuerdo a los resultados de la modelación se registró un valor máximo de 81,6
μg/m [3] .

Mediante Google Earth Pro se calculó el área cuya concentración es mayor a 17 μg/m [3],
el valor de esta superficie corresponde a 1,25 km [2] la que equivale a un 0,31% del área

total de estudio.

Página **51** de **70**

Esto último permite concluir que el efecto de las emisiones atmosféricas de la futura
planta será de carácter local y no afectará a zonas circundantes con uso de suelo
agrícola.

Los efectos del SO 2 sobre la vegetación y la agricultura dependen de diversos factores
entre ellos, el tiempo de exposición, la concentración del contaminante, factores
ambientales, la duración de los periodos a bajas concentraciones y las características
morfológicas de las plantas.

Si se considera que una concentración de 260 μg/m [3 ] y 520 μg/m [3] la tasa fotosintética
disminuía considerablemente respecto a una menor exposición a SO 2 (Keller, 1977), la
concentración generada por el modelo no afectará los la vegetación cercana a la
planta.

A continuación se presentan las curvas de iso-concentración del Dióxido de Azufre
(SO 2 ) en μg/m [3], como concentración diaria.

**Figura 32.** Curvas de iso-concentración diaria (μg/m [3] ) para el SO 2 .

Página **52** de **70**

En la figura anterior se aprecia el área de estudio (20 x 20 km [2] ), la ubicación de la
planta dentro del área de estudio y las curvas de iso-concentración para el SO 2 .

Es importante mencionar que la norma primaria de calidad del SO 2, establece un valor
máximo de 250 μg/m [3], como promedio diario (D.S 113/2002).

De acuerdo a los resultados de la modelación se registró un valor máximo 10,7 μg/m [3] .

Mediante Google Earth Pro se calculó el área cuya concentración es mayor a 3 μg/m [3],
el valor de esta superficie corresponde a 0,73 km [2], la que equivale a un 0,18% del
área de estudio total.

Esto último permite concluir que el efecto de las emisiones atmosféricas de la futura
planta será de carácter local y no afectará la zona más poblada de la ciudad de

Temuco.

A continuación se presentan las curvas de iso-concentración del Dióxido de Azufre
(SO 2 ) en μg/m [3], como concentración anual.

Página **53** de **70**

**Figura 33.** Curvas de iso-concentración anual (μg/m [3] ) para el SO 2 .

La norma primaria de calidad del SO 2, establece un valor máximo de 80 μg/m [3], como
promedio anual (D.S 113/2002).

De acuerdo a los resultados de la modelación se registró un valor máximo 3,51 μg/m [3] .

Mediante Google Earth Pro se calculó el área cuya concentración es mayor a 0,5
μg/m [3], el valor de esta superficie corresponde a 1,47 km [2] .

La norma secundaria de calidad del SO 2, establece un valor máximo de 60 μg/m [3],
como promedio diario (D.S 22/2010). Por lo tanto, se puede concluir que el valor
máximo registrado equivale al 5,85% de la normativa secundaria anual para el SO 2 .

Esto último permite concluir que el efecto de las emisiones atmosféricas de la futura
planta será de carácter local y no afectará la zona más poblada de la ciudad de

Temuco.

Página **54** de **70**

**Monóxido de Carbono (CO)**

A continuación se presentan las curvas de iso-concentración para el Monóxido de
Carbono en su concentración de 8 horas.

**Figura 34.** Curvas de iso-concentración para 8 horas (mg/m [3] ) para el CO.

En la figura anterior se aprecia el área de estudio (20 x 20 km [2] ), la ubicación de la
planta dentro del área de estudio, y la curva de iso-concentración 8 horas para el CO.

Es importante mencionar que la norma de CO, establece un valor máximo de 10
mg/m [3], como promedio de 8 horas (D.S 115 /2002).

De acuerdo a los resultados de la modelación se registró un valor máximo 0,015
mg/m [3] .

Mediante Google Earth Pro se calculó el área cuya concentración es mayor a 0,004
mg/m [3], el valor de esta superficie tiene un valor de 1,36 km [2] .

Página **55** de **70**

Esto último permite concluir que el efecto de las emisiones atmosféricas de la futura
planta será de carácter local y no afectará la zona más poblada de la ciudad de

Temuco.

**4.4.** **Evaluación discreta de las emisiones de la futura planta de Asfalto**

Para realizar la evaluación discreta se utilizaron 8 puntos, de los cuales 6 de ellos se
ubicaron en los sectores más cercanos a la planta y para los dos restantes se utilizaron
las estaciones de monitoreo con representatividad poblacional (Estación Museo
Ferroviario y Estación Las Encinas).

En la siguiente tabla se presentan las coordenadas UTM de los puntos, las cuales se
encuentran en WGS-84, Huso 18 Sur.

**Tabla 12.** Coordenadas Receptores discretos evaluados en la modelación

|Punto|Este (m)|Norte (m)|
|---|---|---|
|1|714.946|5714.183|
|2|715.244|5714.366|
|3|714.245|5713.813|
|4|714.465|5714.975|
|5|715.840|5714.798|
|6|716.963|5715.509|
|Estación Museo ferroviario|711.179|5710.900|
|Estación Las Encinas|706.761|5708.427|

En las siguientes figuras se visualizan los receptores discretos utilizados en la
modelación.

**Figura 35.** Receptores discretos utilizados en la modelación atmosférica (cercanos a la

planta).

Página **56** de **70**

**Figura 36** . Receptores discretos utilizados en la modelación atmosférica. (Estaciones

de Monitoreo con representatividad Poblacional)

El objetivo de esta evaluación es conocer, mediante el modelo CALPUFF, las
concentraciones de MP10, MP2,5, NOx, SO 2 y CO, que puedan experimentar los puntos
y medir las estaciones de monitoreo. Además, en el caso de ser posible, evaluar el
aporte (en porcentaje de contribución) del proyecto sobre las estaciones.

Página **57** de **70**

**Concentración de Material Particulado (MP10)**

La siguiente tabla permite evaluar el aporte de las emisiones de material particulado
respirable (MP10) generadas en la operación del futuro proyecto de extracción de
áridos, procesamiento y producción de asfaltos.

Para esto se calculó en ocho puntos específicos la concentración diaria de MP10, para
luego ver el aporte de dichas concentraciones en los respectivos puntos.

A continuación se presentan las concentraciones modeladas en los 8 receptores
discretos presentes en el área de estudio.

Concentración Diaria

**Tabla 13.** Concentraciones de MP10 (Percentiles 98, promedio 24 horas) modeladas

en receptores discretos en la comuna de Temuco.

|Punto|Valor Norma<br>(μg/m3N)|Valor Modelado<br>(μg/m3N)|
|---|---|---|
|1|150|8,97|
|2|150|6,17|
|3|150|1,67|
|4|150|0,88|
|5|150|1,20|
|6|150|0,44|

En la tabla anterior se presentan las concentraciones modeladas en los seis puntos o
receptores discretos ubicados alrededor de la planta. Tal como se puede apreciar el
punto No1 presenta los niveles más altos de MP10, sin embargo dichos niveles son
bajos si se considera que la norma establece como límite máximo 150 μg/m [3] .

**Tabla 14.** Concentraciones de MP10 (Percentiles 98, promedio 24 horas) modeladas
en las estaciones de monitoreo Museo Ferroviario y Las Encinas.

|Estación de<br>Monitoreo|Valor Norma<br>(μg/m3N)|Valor<br>Modelado<br>(μg/m3N)|Valor<br>observado en<br>estación año<br>2013<br>(μg/m3N)|Aporte del<br>proyecto (%)|
|---|---|---|---|---|
|Museo Ferroviario|<br>150|0,144|183,4|0,078 %|
|Las Encinas|150|0,033|190,2|0,017 %|

Tal como se puede apreciar en la tabla anterior, el aporte de MP10 que generará el
futuro proyecto en la ciudad de Temuco es relativamente bajo, alcanzando un 0,065%
en Estación Museo Ferroviario y un 0,013% en Las Encinas. Sin embargo, las
concentraciones del área de estudio actualmente se encuentran superando la
normativa de calidad de aire (D.S 20/13).

Página **58** de **70**

No obstante lo anterior, de acuerdo a las modelación realizada, se puede apreciar que
el aporte, en la concentración de MP10, del futuro proyecto es prácticamente
insignificante.

Concentraciones Anuales de MP10

**Tabla 15.** Concentraciones de MP10 (anual) modeladas en receptores discretos en la

comuna de Temuco.

|Punto|Valor Norma<br>(μg/m3N)|Valor Modelado (μg/m3N)|
|---|---|---|
|1|50|2,88|
|2|50|2,11|
|3|50|0,63|
|4|50|0,28|
|5|50|0,38|
|6|50|0,15|

En la tabla anterior se presentan las concentraciones modeladas en los seis puntos o
receptores discretos ubicados alrededor de la planta. Tal como se puede apreciar el
punto No1 presenta los niveles más altos de MP10, sin embargo dichos niveles son
bajos si se considera que la norma establece 50 μg/m [3] como límite de promedio anual.

**Tabla 16.** Concentraciones de MP10 (anual) modeladas en las estaciones de

monitoreo Museo Ferroviario y Las Encinas.

|Estación de<br>Monitoreo|Valor Norma<br>(μg/m3N)|Col3|Valor<br>Modelado<br>(μg/m3N)|Valor<br>observado en<br>estación año<br>2013<br>(μg/m3N)|Aporte del<br>proyecto (%)|
|---|---|---|---|---|---|
|Museo Ferroviario|Museo Ferroviario|50|0,038|55,34|0,069%|
|Las Encinas|Las Encinas|50|0,008|55,95|0,014%|

Tal como se puede apreciar en la tabla anterior, las concentraciones de MP10 que
generará el futuro proyecto bajas, sin embargo las concentraciones del área de estudio
actualmente se encuentran superando la normativa de calidad de aire (D.S 20/13).

No obstante lo anterior, de acuerdo a las modelación realizada, se puede apreciar que
el aporte, en la concentración de MP10, de la futura planta de Asfalto no es
significativo lo que se traduce en un aumento inferior al 0,07% de la condición actual
en el área de estudio.

Página **59** de **70**

**Concentración de Material Particulado (MP2,5)**

La siguiente tabla permite evaluar el aporte de las emisiones de material particulado
fino (MP2,5) generadas en la operación del futuro proyecto de extracción de áridos,
procesamiento y producción de asfaltos.

Para esto se calculó en ocho puntos específicos la concentración diaria de MP2,5, para
luego ver el aporte de dichas concentraciones en los respectivos puntos.

A continuación se presentan las concentraciones modeladas en los 8 receptores
discretos presentes en el área de estudio.

Concentración Diaria

**Tabla 17.** Concentraciones de MP2,5 (Percentiles 98, promedio 24 horas) modeladas

en receptores discretos en la comuna de Temuco.

|Punto|Valor Norma<br>(μg/m3N)|Valor Modelado (μg/m3N)|
|---|---|---|
|1|50|0,89|
|2|50|0,61|
|3|50|0,16|
|4|50|0,08|
|5|50|0,11|
|6|50|0,04|

En la tabla anterior se presentan las concentraciones modeladas en los seis puntos o
receptores discretos ubicados alrededor de la planta. Tal como se puede apreciar el
punto No1 presenta los niveles más altos de MP2,5, sin embargo dichos niveles son
bastante bajos si se considera que la norma permite un máximo de 50 μg/m [3] como
concentración promedio 24 hrs.

**Tabla 18.** Concentraciones de MP2,5 (Percentiles 98, promedio 24 horas) modeladas

en las estaciones de monitoreo Museo Ferroviario y Las Encinas.

|Estación de<br>Monitoreo|Valor Norma<br>(μg/m3N)|Col3|Valor<br>Modelado<br>(μg/m3N)|Col5|Valor<br>observado en<br>estación año<br>2013<br>(μg/m3N)|Col7|Aporte del<br>proyecto (%)|Col9|
|---|---|---|---|---|---|---|---|---|
|Estación Museo<br>ferroviario|Estación Museo<br>ferroviario|50|50|0,012|0,012|157,4|157,4|0,008 %|
|Estación Las Encinas|Estación Las Encinas|50|50|0,003|0,003|159,2|159,2|0,002 %|

Tal como se puede apreciar en la tabla anterior, las concentraciones de MP2,5 que
generará el futuro proyecto son bastante bajas, sin embargo las concentraciones

Página **60** de **70**

observadas en el área de estudio actualmente se encuentran superando la normativa
de calidad de aire (D.S 12/11).

No obstante lo anterior, de acuerdo a las modelación realizada, se puede apreciar que
el aporte, en la concentración ambiental de MP2,5, del futuro proyecto es
relativamente bajo alcanzándose un aumento inferior al 0,008% de la condición actual
registrada en las dos estaciones de monitoreo consideradas en el presente estudio.

Concentraciones Anuales de MP2,5

**Tabla 19.** Concentraciones de MP2,5 (anual) modeladas en receptores discretos en la

comuna de Temuco.

|Punto|Valor Norma<br>(μg/m3N)|Valor Modelado<br>(μg/m3N)|
|---|---|---|
|1|20|0,28|
|2|20|0,21|
|3|20|0,06|
|4|20|0,02|
|5|20|0,04|
|6|20|0,01|

En la tabla anterior se presentan las concentraciones modelada en los seis puntos o
receptores discretos ubicados alrededor de la planta. Tal como se puede apreciar el
punto No1 presenta los niveles más altos de MP2,5, sin embargo dichos niveles son
bajos si se considera que la norma permite 20 μg/m [3] .

**Tabla 20.** Concentraciones de MP2,5 (anual) modeladas en las estaciones de

monitoreo Museo Ferroviario y Las Encinas.

|Estación de<br>Monitoreo|Valor Norma<br>(μg/m3N)|Col3|Valor<br>Modelado<br>(μg/m3N)|Col5|Valor<br>observado en<br>estación año<br>2013<br>(μg/m3N)|Aporte del<br>proyecto (%)|
|---|---|---|---|---|---|---|
|Museo ferroviario|20|0,0034|0,0034|39,3|39,3|0,009%|
|Las Encinas|20|0,0006|0,0006|38,7|38,7|0,002%|

Tal como se puede apreciar en la tabla anterior, las concentraciones de MP2,5 que
generará el futuro proyecto son bajas, sin embargo las concentraciones del área de
estudio actualmente se encuentran superando la normativa de calidad de aire (D.S
12/11).

No obstante lo anterior, de acuerdo a las modelación realizada, se puede apreciar que
el aporte, en la concentración de MP2,5, de la futura planta es bastante bajo, tomando

Página **61** de **70**

en cuenta que se consigue un aumento inferior al 0,02% de la condición actual en el
área de estudio.

Página **62** de **70**

**Óxidos de Nitrógeno (NOx)**

La siguiente tabla permite evaluar el aporte de las emisiones de óxidos de nitrógeno
(NOx) generadas en la operación del futuro proyecto de extracción de áridos,
procesamiento y producción de asfaltos.

Para esto se calculó en ocho puntos específicos la concentración horaria de NOx, para
luego ver el aporte de dichas concentraciones en los respectivos puntos.

A continuación se presentan las concentraciones modeladas en los 8 receptores
discretos presentes en el área de estudio.

Concentración horaria

**Tabla 21.** Concentraciones de NOx (Percentiles 99, promedio horario) modeladas en

receptores discretos en la comuna de Temuco.

|Punto|Valor Norma<br>(μg/m3N)|Valor Modelado<br>(μg/m3N)|
|---|---|---|
|1|400|46,8|
|2|400|29,5|
|3|400|12,8|
|4|400|4,63|
|5|400|6,66|
|6|400|2,48|

En la tabla anterior se presentan las concentraciones modelada en los seis puntos o
receptores discretos ubicados alrededor de la planta. Tal como se puede apreciar el
punto No1 presenta los niveles más altos de NOx, sin embargo dichos niveles son
relativamente bajos si se considera que la norma permite 400 μg/m [3] .

**Tabla 22.** Concentraciones de NOx (Percentiles 99, promedio horario) modeladas en

las estaciones de monitoreo Museo Ferroviario y Las Encinas.

|Estación de monitoreo|Valor Norma<br>(μg/m3N)|Valor Modelado<br>(μg/m3N)|Valor Estación<br>(μg/m3N)|
|---|---|---|---|
|Museo ferroviario|400|1,58|sin datos|
|Las Encinas|400|0,42|sin datos|

Tal como se puede apreciar en la tabla anterior, las concentraciones modeladas en
ambas estaciones son bastante bajas si se comparan con los valores establecidos en el
D.S 114/2002.

Es importante mencionar que los registros de NOx en las dos estaciones actualmente
no se encuentran actualizados para el año 2013. Por lo tanto no existe información
para poder comparar el aporte de NOx generado por el futuro proyecto.

Página **63** de **70**

Concentraciones Anuales de NOx

**Tabla 23.** Concentraciones de NOx (anual) modeladas en receptores discretos en la

comuna de Temuco.

|Punto|Valor Norma<br>(μg/m3N)|Valor Modelado<br>(μg/m3N)|
|---|---|---|
|1|100|1,00|
|2|100|0,62|
|3|100|0,36|
|4|100|0,17|
|5|100|0,18|
|6|100|0,10|

En la tabla anterior se presentan las concentraciones modeladas en los seis puntos o
receptores discretos ubicados alrededor de la planta. Tal como se puede apreciar el
punto No1 presenta los niveles más altos de NOx, sin embargo dichos niveles son
bastante bajos si se considera que la norma permite 100 μg/m [3] .

**Tabla 24.** Concentraciones de NOx (anual) modeladas en las estaciones de monitoreo

Museo Ferroviario y Las Encinas.

|Estación de monitoreo|Valor Norma<br>(μg/m3N)|Valor Modelado<br>(μg/m3N)|Valor Estación<br>(μg/m3N)|
|---|---|---|---|
|Museo ferroviario|100|0,035|sin datos|
|Las Encinas|100|0,007|sin datos|

Tal como se puede apreciar en la tabla anterior, las concentraciones modeladas en
ambas estaciones son bajas si se comparan con los valores establecidos en el D.S
114/2002.

Es importante mencionar que los registros de NOx en las dos estaciones actualmente
no poseen datos, por lo tanto no existe información para poder determinar el aporte
de NOx generado por el futuro proyecto, sin embargo está muy por debajo de la

norma.

Página **64** de **70**

**Dióxido de Azufre (SO** **2** **)**

La siguiente tabla permite evaluar el aporte de las emisiones de Dióxido de Azufre
(SO 2 ) generadas en la operación del futuro proyecto.

A continuación se presentan las concentraciones modeladas en los 8 receptores
discretos presentes en el área de estudio.

Concentración Diaria

**Tabla 25.** Concentraciones de SO 2 (Percentiles 99, promedio diario) modeladas en

receptores discretos en la comuna de Temuco.

|Punto|Valor Norma<br>Primaria<br>(μg/m3N)|Valor Norma<br>Secundaria<br>(μg/m3N)|Valor Modelado<br>(μg/m3N)|
|---|---|---|---|
|1|250|260|3,30|
|2|250|260|1,76|
|3|250|260|1,01|
|4|250|260|0,63|
|5|250|260|0,54|
|6|250|260|0,30|

En la tabla anterior se presentan las concentraciones modeladas en los seis puntos o
receptores discretos ubicados alrededor de la planta. Tal como se puede apreciar el
punto No1 presenta los niveles más altos de SO 2, sin embargo dichos niveles son
bastante bajos si se considera que las normas primarias y secundarias permiten 250
μg/m [3] y 260 μg/m [3] respectivamente.

**Tabla 26.** Concentraciones de SO 2 (Percentiles 99, promedio diario) modeladas en las

estaciones de monitoreo Museo Ferroviario y Las Encinas.

|Estación de<br>monitoreo|Valor Norma<br>Primaria<br>(μg/m3N)|Valor Norma<br>Secundaria<br>(μg/m3N)|Valor<br>Modelado<br>(μg/m3N)|Valor<br>Estación<br>(μg/m3N)|
|---|---|---|---|---|
|Museo ferroviario|250|260|0,15|sin datos|
|Las Encinas|250|260|0,03|sin datos|

Tal como se puede apreciar en la tabla anterior, las concentraciones modeladas en
ambas estaciones son bastante bajas si se comparan con los valores establecidos en el
D.S 113/2002 y D.S 22/2010.

Es importante mencionar que los registros de SO 2 en las dos estaciones actualmente
no poseen datos. Por lo tanto no existe información para poder comparar el aporte de
SO 2 generado por el futuro proyecto.

Página **65** de **70**

Concentraciones Anuales de SO 2

**Tabla 27.** Concentraciones de SO 2 (anual) modeladas en receptores discretos en la

comuna de Temuco.

|Punto|Valor Norma<br>Primaria<br>(μg/m3N)|Valor Norma<br>Secundaria<br>(μg/m3N)|Valor Modelado<br>(μg/m3N)|
|---|---|---|---|
|1|80|60|0,63|
|2|80|60|0,41|
|3|80|60|0,24|
|4|80|60|0,12|
|5|80|60|0,14|
|6|80|60|0,08|

En la tabla anterior se presentan las concentraciones modelada en los seis puntos o
receptores discretos ubicados alrededor de la planta. Tal como se puede apreciar el
punto No1 presenta los niveles más altos de SO 2, sin embargo dichos niveles son
relativamente bajos si se considera que las normas primarias y secundarias permiten
80 μg/m [3] y 60 μg/m [3] respectivamente.

**Tabla 28.** Concentraciones de SO 2 (anual) modeladas en las estaciones de monitoreo

Museo Ferroviario y Las Encinas.

|Estación de<br>monitoreo|Valor Norma<br>Primaria<br>(μg/m3N)|Valor Norma<br>Secundaria<br>(μg/m3N)|Valor<br>Modelado<br>(μg/m3N)|Valor Estación<br>(μg/m3N)|
|---|---|---|---|---|
|Museo<br>ferroviario|80|60|0,025|sin datos|
|Las Encinas|80|60|0,006|sin datos|

Tal como se puede apreciar en la tabla anterior, las concentraciones modeladas en
ambas estaciones son bastante bajas si se comparan con los valores establecidos en el
D.S 113/2002 y D.S 22/2010.

Es importante mencionar que los registros de SO 2 en las dos estaciones actualmente
no se encuentran actualizados. Por lo tanto no existe información para poder comparar
el aporte de SO 2 generado por el futuro proyecto.

Página **66** de **70**

Concentraciones horarias de SO 2

**Tabla 29.** Concentraciones de SO 2 (Percentiles 99,73, promedio horario) modeladas

en receptores discretos en la comuna de Temuco.

|Punto|Valor Norma<br>Secundaria<br>(μg/m3N)|Valor Modelado<br>(μg/m3N)|
|---|---|---|
|1|700|31,6|
|2|700|31,9|
|3|700|9,56|
|4|700|3,54|
|5|700|6,32|
|6|700|2,19|

En la tabla anterior se presentan las concentraciones modelada en los seis puntos o
receptores discretos ubicados alrededor de la planta. Tal como se puede apreciar el
punto No2 presenta los niveles más altos de SO 2, sin embargo dichos niveles son bajos
si se considera que la norma establece como límite 700 μg/m [3] .

**Tabla 30.** Concentraciones de SO 2 (Percentiles 99,73, promedio horario) modeladas

en las estaciones de monitoreo Museo Ferroviario y Las Encinas.

|Punto|Valor Norma<br>Secundaria<br>(μg/m3N)|Valor Modelado<br>(μg/m3N)|Valor Estación<br>(μg/m3N)|
|---|---|---|---|
|Estación Museo Ferroviario|700|1,19|Sin Datos|
|Estación Las Encinas|700|0,30|Sin Datos|

Tal como se puede apreciar en la tabla anterior, las concentraciones modeladas en
ambas estaciones son bastante bajas si se comparan con los valores establecidos en el
D.S 22/2010.

Es importante mencionar que los registros de SO 2 en las dos estaciones actualmente
no se encuentran actualizados. Por lo tanto no existe información para poder comparar
el aporte de SO 2 generado por el futuro proyecto.

Página **67** de **70**

**Monóxido de Carbono (CO)**

La siguiente tabla permite evaluar el aporte de las emisiones de Monóxido de Carbono
(CO) generadas en la operación del futuro proyecto.

A continuación se presentan las concentraciones modeladas en los 8 receptores
discretos presentes en el área de estudio.

Concentración 8 horas

**Tabla 31.** Concentraciones de CO (Percentiles 99, promedio 8 horas) modeladas en

receptores discretos en la comuna de Temuco.

|Punto|Valor Norma<br>Primaria<br>(mg/m3N)|Valor Modelado<br>(mg/m3N)|
|---|---|---|
|1|10|0,0084|
|2|10|0,0048|
|3|10|0,0024|
|4|10|0,0013|
|5|10|0,0015|
|6|10|0,0008|

En la tabla anterior se presentan las concentraciones modelada en los seis puntos o
receptores discretos ubicados alrededor de la planta. Tal como se puede apreciar el
punto No1 presenta los niveles más altos de CO, sin embargo dichos niveles son
bastante bajos si se considera que las norma primaria permite 10 mg/m [3] .

**Tabla 32.** Concentraciones de CO (Percentiles 99, promedio 8 horas) modeladas en

las estaciones de monitoreo Museo Ferroviario y Las Encinas.

|Estación de<br>monitoreo|Valor Norma<br>Primaria<br>(mg/m3N)|Valor Modelado<br>(mg/m3N)|Valor Estación<br>(mg/m3N)|
|---|---|---|---|
|Museo Ferroviario|10|0,0004|Sin Datos|
|Las Encinas|10|0,0001|Sin Datos|

Tal como se puede apreciar en la tabla anterior, las concentraciones de CO que
generará el futuro proyecto son bastante bajas, comparándolas con el límite de la
norma que es 10 mg/m [3] .

Es importante mencionar que los registros de CO en las dos estaciones actualmente
presentan datos. Por lo tanto no existe información para poder comparar el aporte de
CO generado por el futuro proyecto.

Página **68** de **70**

**5.** **Conclusión**

El objetivo del proyecto es ampliar la vida útil de la planta de asfalto - Temuco, la cual
produce mezclas asfálticas, necesarias para obras asociadas a la pavimentación de
caminos, además el proyecto incluyó la extracción y procesamiento de áridos de un
tramo del río Cautín.

Para conocer el efecto que tendrá el proyecto, una vez que comience a operar
nuevamente, se calcularon las emisiones atmosféricas de los principales proceso
generadores de emisiones atmosféricas. Dichas emisiones corresponden a dos fuentes
fijas y cuatro fuentes de área (Anexo 14.1).

Se evaluó el efecto de las futuras emisiones atmosféricas, para ello se utilizó el modelo
CALPUFF, el cual permitió simular la dispersión y concentraciones de los distintos
contaminantes generados en un área de estudio de 20 x 20 km [2] .

De acuerdo a los resultados obtenidos en la modelación se puede concluir que:

Debido a la predominancia de vientos Sur y Sur Oeste, los contaminantes se
dispersan hacia la zona noreste del área de estudio.

De acuerdo a los rangos de velocidad de viento, registrados en dos estaciones
meteorológicas, se puede inferir que en el área de estudio no existe una buena
dispersión de contaminantes, debido a un porcentaje considerable de velocidades
calmas (0 m/s) y vientos lentos.

Se evaluó mediante mapas de iso-concentración los aportes de contaminantes que
generará el futuro proyecto. En todos los caso se evidencio un efecto local, ya que
las mayores concentraciones de cada contaminante abarcan superficies que no
alcanzan el 1% del área de estudio.

Para evaluar el efecto en los poblados cercanos a la planta, se realizó una
modelación en fuentes discretas. Para esto se definieron ocho receptores, seis de
estos correspondieron a puntos cercanos a la planta y dos correspondieron a las
estaciones de monitoreo Museo Ferroviario y Las Encinas.

Las concentraciones modeladas, para cada contaminante, en los seis puntos
cercanos a la planta, permiten concluir que en ningún caso las emisiones
generadas por el futuro proyecto superaran las respectivas normas de calidad
vigente en nuestro país e incluso se encuentran por muy debajo de éstas.

Se modelo la concentración, de cada contaminante, en dos estaciones de
monitoreo. Los resultados de dicha modelación permitió evaluar el aumento (o
aporte) que generaran las emisiones sobre la calidad de aire de la ciudad de

Temuco.

Página **69** de **70**

Considerando los resultados obtenidos en las estaciones de monitoreo, se puede
concluir que, los aportes a las concentración ambiental que generaran las futuras
emisiones atmosféricas de la planta no superará el 0,1% de la concentración que
actualmente registran las estaciones de monitoreo Museo Ferroviario y Las Encinas,
para los contaminantes MP10 y MP2,5.

Por lo tanto, considerando todo lo mencionado, se puede concluir que las futuras
emisiones atmosféricas de MP10, MP2,5, NOx, SO 2 y CO, no afectaran de manera
considerable la calidad del aire de la ciudad de Temuco. Si se considera que el
aumento de las concentraciones de MP10 y MP2,5, no supera el 0,1% de la condición
actual, registrada en las estaciones de monitoreo Museo Ferroviario y Las Encinas,
además que en ningún caso se ven superados los límites establecidos por la normativa
vigente, al contrario, se obtuvieron valores muy por debajo de éstos.

Página **70** de **70**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: ** Coordenadas UTM del área de estudio. Datum WGS-84, Huso 18 Sur.**

| Punto | Este (m) | Norte (m) |
| --- | --- | --- |
| A | 701.375 | 5.702.888 |
| B | 701.375 | 5.722.888 |
| C | 721.375 | 5.722.888 |
| D | 721.375 | 5.702.888 |

**Tabla 2.: ** Datos meteorológicos y geofísicos considerados en la modelación.**

| Categoría de datos | Parámetro | Fuente |
| --- | --- | --- |
| Meteorología de altura | Temperatura | National<br>Oceanic<br>and<br>Atmospheric Administration<br>(NOAA) |
| Meteorología de altura | Presión | Presión |
| Meteorología de altura | Velocidad de viento | Velocidad de viento |
| Meteorología de altura | Dirección de viento | Dirección de viento |
| Meteorología de Superficie | Temperatura | Estación Museo Ferroviario<br>Estación Las Encinas |
| Meteorología de Superficie | Presión | Estación Museo Ferroviario<br>Estación Las Encinas |
| Meteorología de Superficie | Velocidad de viento | Estación Museo Ferroviario<br>Estación Las Encinas |
| Meteorología de Superficie | Dirección de viento | Estación Museo Ferroviario<br>Estación Las Encinas |
| Meteorología de Superficie | Humedad relativa | Estación Museo Ferroviario<br>Estación Las Encinas |
| Geofísicos | Elevación de Terreno | United<br>Stated<br>Geological<br>Survey (USGS) |
| Geofísicos | Uso de Suelo | Uso de Suelo |

**Tabla 3.: ** Principales emisiones atmosféricas areales generadas en el proyecto.**

| Emisiones de área de extracción y procesamiento de áridos (ton/año) | Col2 | Col3 |
| --- | --- | --- |
| **Actividad** | **MP10** | **MP2.5** |
| Transferencia de material, carguío y volteo | 0,0214 | 0,00325 |
| Erosión de material en pilas | 0,00011 | - |
| Planta chancadora (chancadores, harnero,<br>cintas<br>transportadoras,<br>transferencia<br>de<br>material y descarga en buzón) | 0,1831 | 0,0246 |
| Transferencia de material, carguío y volteo | 0,0566 | 0,00857 |
| Tránsito<br>de<br>camiones<br>en<br>caminos<br>no<br>pavimentados | 0,20034 | 0,02003 |
| Tránsito de cargador frontal en caminos no<br>pavimentados | 1,93436 | 0,19343 |
| **Emisiones parciales** | **2,396** | **0,250** |
| **Emisiones de área producción de asfalto (ton/año)** | **Emisiones de área producción de asfalto (ton/año)** | **Emisiones de área producción de asfalto (ton/año)** |
| **Actividad** | **MP10** | **MP2.5** |
| Transferencia de material | 0,034409 | 0,005210 |
| Erosión material en pilas (área planta de<br>asfalto) | 0,00483 | - |
| Tránsito<br>de<br>camiones<br>por<br>caminos<br>no<br>pavimentados | 1,10249 | 0,11025 |
| **Emisiones parciales** | **1,14172** | **0,11546** |
| **Emisiones Totales** | **3,538** | **0,365** |

**Tabla 4.: ** Emisiones atmosféricas puntuales generadas en la producción de asfalto.**

| Actividad | Emisiones Puntuales (ton/año) | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Actividad** | **MP10** | **CO** | **NOx** | **SO2 ** |
| Calentador Vertical | 0,0122 | - | - | - |
| Secador de Asfalto | 0,6335 | 3,5810 | 1,5149 | 0,3030 |
| Equipo Electrógeno | 0,4256 | 3,3440 | 7,9040 | 4,9187 |

**Tabla 5.: ** Coordenadas de fuentes puntuales.**

| Fuente | UTM, WGS-84, Huso 18 S | Col3 |
| --- | --- | --- |
| **Fuente** | **Este (m)** | **Norte (m)** |
| Calentador vertical | 715.069 | 5.713.887 |
| Secador de Asfalto | 715.058 | 5.713.895 |
| Equipo Electrógeno | 715.163 | 5.713.736 |

**Tabla 6.: ** Coordenadas y superficies de fuentes de área.**

| Zona | Superficie (m2) | Vertices (UTM, WGS-84, Huso 18 S) | Col4 |
| --- | --- | --- | --- |
| **Zona** | **Superficie (m2) ** | **Este (m)** | **Norte (m)** |
| E1 | 5.818 | 715.195 | 5.713.782 |
| E1 | 5.818 | 715.194 | 5.713.724 |
| E1 | 5.818 | 715.296 | 5.713.776 |
| E1 | 5.818 | 715.296 | 5.713.720 |
| E2 | 2.722 | 715.118 | 5.713.758 |
| E2 | 2.722 | 715.142 | 5.713.710 |
| E2 | 2.722 | 715.164 | 5.713.779 |
| E2 | 2.722 | 715.188 | 5.713.733 |
| E3 | 3.318 | 715.048 | 5.713.773 |
| E3 | 3.318 | 715.073 | 5.713.708 |
| E3 | 3.318 | 715.091 | 5.713.789 |
| E3 | 3.318 | 715.117 | 5.713.723 |
| A1 | 2.740 | 715.082 | 5.713.852 |
| A1 | 2.740 | 715.103 | 5.713.793 |
| A1 | 2.740 | 715.123 | 5.713.865 |
| A1 | 2.740 | 715.145 | 5.713.806 |

**Tabla 7.: ** Emisiones atmosféricas areales usadas en la modelación CALPUFF.**

| Zona | Emisión MP10<br>(ton/año) | Área (m2) | Emisión MP10<br>(ton/año/m2) |
| --- | --- | --- | --- |
| E1 | 2,156 | 5.818 | 0,000371 |
| E2 | 0,183 | 2.722 | 0,0000673 |
| E3 | 0,057 | 3.318 | 0,0000171 |
| A1 | 1,142 | 2.740 | 0,000417 |

**Tabla 8.: ** Emisiones atmosféricas areales usadas en la modelación CALPUFF.**

| Zona | Emisión MP10<br>(ton/año) | Área (m2) | Emisión MP10<br>(ton/año/m2) |
| --- | --- | --- | --- |
| E1 | 0,217 | 5.818 | 0,0000372 |
| E2 | 0,025 | 2.722 | 0,00000904 |
| E3 | 0,009 | 3.318 | 0,00000258 |
| A1 | 0,115 | 2.740 | 0,0000421 |

**Tabla 9.: ** Normas de calidad aplicables al proyecto**

| Normativa de calidad del aire primaria | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| **Contaminante** | **Límite Norma** | **Concentración** | **Decreto** |
| Material Particulado<br>(MP10) | 150 μg/m~~3~~N | Máxima Diaria | N° 20/2013<br>MMA |
| Material Particulado<br>(MP10) | 50 μg/m3N <br> | Media anual**1** | Media anual**1** |
| Material Particulado<br>(MP2,5) | 50 μg/m~~3~~N | Máxima Diaria | N° 12/2011<br>MMA |
| Material Particulado<br>(MP2,5) | 20 μg/m3N <br> | Media anual | Media anual |
| Dióxido de azufre (SO2) | 80 μg/m~~3~~N <br> | Media anual | N° 113/2002<br>MINSEGPRES |
| Dióxido de azufre (SO2) | 250 μg/m~~3~~N | Máxima diaria | Máxima diaria |
| Dióxido de Nitrógeno<br>(NO2) | 400 μg/m3N | 1 hora | N° 114/2002<br>MNSEGPRES |
| Dióxido de Nitrógeno<br>(NO2) | 100 μg/m3N | Media anual | Media anual |
| Monóxido de Carbono<br>(CO) | 10 mg/m3N | 8 horas | N° 115/2002<br>MINSEGPRES |
| **Normativa de calidad del aire secundaria** | **Normativa de calidad del aire secundaria** | **Normativa de calidad del aire secundaria** | **Normativa de calidad del aire secundaria** |
| **Contaminante** | **Límite Norma** | **Concentración** | **Decreto** |
| Dióxido de azufre SO2 | 700 μg/m3N | 1 hora | N° 22/2010<br>MINSEGPRES |
| Dióxido de azufre SO2 | 260 μg/m3N | Máxima Diaria | Máxima Diaria |
| Dióxido de azufre SO2 | 60 μg/m3N | Media Anual | Media Anual |

**Tabla 10.: ** Dirección y velocidad de viento estacional, estación Museo Ferroviario.**

| Estaciones | Dirección de Vector<br>Resultante | Velocidades<br>Predominantes y Calmas<br>(m/s) | Frecuencia<br>% |
| --- | --- | --- | --- |
| Verano | OSO (53%) | 0,5-2,1 | 68,3 |
| Verano | OSO (53%) | 2,1-3,6 | 16,6 |
| Verano | OSO (53%) | 3,6-5,7 | 6,5 |
| Verano | OSO (53%) | Calma | 8,6 |
| Otoño | S (54%) | 0,5-2,1 | 60,9 |
| Otoño | S (54%) | 2,1-3,6 | 14,5 |
| Otoño | S (54%) | 3,6-5,7 | 3,6 |
| Otoño | S (54%) | Calmas | 20,3 |
| Invierno | SSE (78 %) | 0,5-2,1 | 58,1 |
| Invierno | SSE (78 %) | 2,1-3,6 | 15,7 |
| Invierno | SSE (78 %) | 3,6-5,7 | 3,2 |
| Invierno | SSE (78 %) | Calmas | 21,8 |
| Primavera | SE (44 %) | 0,5-2,1 | 55,7 |
| Primavera | SE (44 %) | 2,1-3,6 | 22,3 |
| Primavera | SE (44 %) | 3,6-5,7 | 5,1 |
| Primavera | SE (44 %) | Calmas | 16,9 |

**Tabla 11.: ** Dirección y velocidad de viento estacional, medidas en la estación**

| Estaciones | Dirección de Vector<br>Resultante | Col3 | Velocidades<br>Predominantes y Calmas<br>(m/s) | Col5 | Frecuencia<br>% |
| --- | --- | --- | --- | --- | --- |
| Verano | Verano | OSO (50 %) | 0,5-2,1 | 54,5 | 54,5 |
| Verano | Verano | OSO (50 %) | 2,1-3,6 | 23,1 | 23,1 |
| Verano | Verano | OSO (50 %) | 3,6-5,7 | 10,0 | 10,0 |
| Verano | Verano | OSO (50 %) | Calma | 12,1 | 12,1 |
| Otoño | Otoño | O (12 %) | 0,5-2,1 | 63,7 | 63,7 |
| Otoño | Otoño | O (12 %) | 2,1-3,6 | 16,2 | 16,2 |
| Otoño | Otoño | O (12 %) | 3,6-5,7 | 5,8 | 5,8 |
| Otoño | Otoño | O (12 %) | Calmas | 13,4 | 13,4 |
| Invierno | Invierno | ONO (8 %) | 0,5-2,1 | 62,5 | 62,5 |
| Invierno | Invierno | ONO (8 %) | 2,1-3,6 | 17,5 | 17,5 |
| Invierno | Invierno | ONO (8 %) | 3,6-5,7 | 6,1 | 6,1 |
| Invierno | Invierno | ONO (8 %) | Calmas | 12,6 | 12,6 |
| Primavera | Primavera | OSO (39 %) | 0,5-2,1 | 66,8 | 66,8 |
| Primavera | Primavera | OSO (39 %) | 2,1-3,6 | 22,4 | 22,4 |
| Primavera | Primavera | OSO (39 %) | 3,6-5,7 | 5,4 | 5,4 |
| Primavera | Primavera | OSO (39 %) | Calmas | 5,4 | 5,4 |

**Tabla 12.: ** Coordenadas Receptores discretos evaluados en la modelación**

| Punto | Este (m) | Norte (m) |
| --- | --- | --- |
| 1 | 714.946 | 5714.183 |
| 2 | 715.244 | 5714.366 |
| 3 | 714.245 | 5713.813 |
| 4 | 714.465 | 5714.975 |
| 5 | 715.840 | 5714.798 |
| 6 | 716.963 | 5715.509 |
| Estación Museo ferroviario | 711.179 | 5710.900 |
| Estación Las Encinas | 706.761 | 5708.427 |

**Tabla 13.: ** Concentraciones de MP10 (Percentiles 98, promedio 24 horas) modeladas**

| Punto | Valor Norma<br>(μg/m3N) | Valor Modelado<br>(μg/m3N) |
| --- | --- | --- |
| 1 | 150 | 8,97 |
| 2 | 150 | 6,17 |
| 3 | 150 | 1,67 |
| 4 | 150 | 0,88 |
| 5 | 150 | 1,20 |
| 6 | 150 | 0,44 |

**Tabla 14.: ** Concentraciones de MP10 (Percentiles 98, promedio 24 horas) modeladas**

| Estación de<br>Monitoreo | Valor Norma<br>(μg/m3N) | Valor<br>Modelado<br>(μg/m3N) | Valor<br>observado en<br>estación año<br>2013<br>(μg/m3N) | Aporte del<br>proyecto (%) |
| --- | --- | --- | --- | --- |
| Museo Ferroviario | <br>150 | 0,144 | 183,4 | 0,078 % |
| Las Encinas | 150 | 0,033 | 190,2 | 0,017 % |

**Tabla 15.: ** Concentraciones de MP10 (anual) modeladas en receptores discretos en la**

| Punto | Valor Norma<br>(μg/m3N) | Valor Modelado (μg/m3N) |
| --- | --- | --- |
| 1 | 50 | 2,88 |
| 2 | 50 | 2,11 |
| 3 | 50 | 0,63 |
| 4 | 50 | 0,28 |
| 5 | 50 | 0,38 |
| 6 | 50 | 0,15 |

**Tabla 16.: ** Concentraciones de MP10 (anual) modeladas en las estaciones de**

| Estación de<br>Monitoreo | Valor Norma<br>(μg/m3N) | Col3 | Valor<br>Modelado<br>(μg/m3N) | Valor<br>observado en<br>estación año<br>2013<br>(μg/m3N) | Aporte del<br>proyecto (%) |
| --- | --- | --- | --- | --- | --- |
| Museo Ferroviario | Museo Ferroviario | 50 | 0,038 | 55,34 | 0,069% |
| Las Encinas | Las Encinas | 50 | 0,008 | 55,95 | 0,014% |

**Tabla 17.: ** Concentraciones de MP2,5 (Percentiles 98, promedio 24 horas) modeladas**

| Punto | Valor Norma<br>(μg/m3N) | Valor Modelado (μg/m3N) |
| --- | --- | --- |
| 1 | 50 | 0,89 |
| 2 | 50 | 0,61 |
| 3 | 50 | 0,16 |
| 4 | 50 | 0,08 |
| 5 | 50 | 0,11 |
| 6 | 50 | 0,04 |

**Tabla 18.: ** Concentraciones de MP2,5 (Percentiles 98, promedio 24 horas) modeladas**

| Estación de<br>Monitoreo | Valor Norma<br>(μg/m3N) | Col3 | Valor<br>Modelado<br>(μg/m3N) | Col5 | Valor<br>observado en<br>estación año<br>2013<br>(μg/m3N) | Col7 | Aporte del<br>proyecto (%) | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Estación Museo<br>ferroviario | Estación Museo<br>ferroviario | 50 | 50 | 0,012 | 0,012 | 157,4 | 157,4 | 0,008 % |
| Estación Las Encinas | Estación Las Encinas | 50 | 50 | 0,003 | 0,003 | 159,2 | 159,2 | 0,002 % |

**Tabla 19.: ** Concentraciones de MP2,5 (anual) modeladas en receptores discretos en la**

| Punto | Valor Norma<br>(μg/m3N) | Valor Modelado<br>(μg/m3N) |
| --- | --- | --- |
| 1 | 20 | 0,28 |
| 2 | 20 | 0,21 |
| 3 | 20 | 0,06 |
| 4 | 20 | 0,02 |
| 5 | 20 | 0,04 |
| 6 | 20 | 0,01 |

**Tabla 20.: ** Concentraciones de MP2,5 (anual) modeladas en las estaciones de**

| Estación de<br>Monitoreo | Valor Norma<br>(μg/m3N) | Col3 | Valor<br>Modelado<br>(μg/m3N) | Col5 | Valor<br>observado en<br>estación año<br>2013<br>(μg/m3N) | Aporte del<br>proyecto (%) |
| --- | --- | --- | --- | --- | --- | --- |
| Museo ferroviario | 20 | 0,0034 | 0,0034 | 39,3 | 39,3 | 0,009% |
| Las Encinas | 20 | 0,0006 | 0,0006 | 38,7 | 38,7 | 0,002% |

**Tabla 21.: ** Concentraciones de NOx (Percentiles 99, promedio horario) modeladas en**

| Punto | Valor Norma<br>(μg/m3N) | Valor Modelado<br>(μg/m3N) |
| --- | --- | --- |
| 1 | 400 | 46,8 |
| 2 | 400 | 29,5 |
| 3 | 400 | 12,8 |
| 4 | 400 | 4,63 |
| 5 | 400 | 6,66 |
| 6 | 400 | 2,48 |

**Tabla 22.: ** Concentraciones de NOx (Percentiles 99, promedio horario) modeladas en**

| Estación de monitoreo | Valor Norma<br>(μg/m3N) | Valor Modelado<br>(μg/m3N) | Valor Estación<br>(μg/m3N) |
| --- | --- | --- | --- |
| Museo ferroviario | 400 | 1,58 | sin datos |
| Las Encinas | 400 | 0,42 | sin datos |

**Tabla 23.: ** Concentraciones de NOx (anual) modeladas en receptores discretos en la**

| Punto | Valor Norma<br>(μg/m3N) | Valor Modelado<br>(μg/m3N) |
| --- | --- | --- |
| 1 | 100 | 1,00 |
| 2 | 100 | 0,62 |
| 3 | 100 | 0,36 |
| 4 | 100 | 0,17 |
| 5 | 100 | 0,18 |
| 6 | 100 | 0,10 |

**Tabla 24.: ** Concentraciones de NOx (anual) modeladas en las estaciones de monitoreo**

| Estación de monitoreo | Valor Norma<br>(μg/m3N) | Valor Modelado<br>(μg/m3N) | Valor Estación<br>(μg/m3N) |
| --- | --- | --- | --- |
| Museo ferroviario | 100 | 0,035 | sin datos |
| Las Encinas | 100 | 0,007 | sin datos |

**Tabla 25.: ** Concentraciones de SO 2 (Percentiles 99, promedio diario) modeladas en**

| Punto | Valor Norma<br>Primaria<br>(μg/m3N) | Valor Norma<br>Secundaria<br>(μg/m3N) | Valor Modelado<br>(μg/m3N) |
| --- | --- | --- | --- |
| 1 | 250 | 260 | 3,30 |
| 2 | 250 | 260 | 1,76 |
| 3 | 250 | 260 | 1,01 |
| 4 | 250 | 260 | 0,63 |
| 5 | 250 | 260 | 0,54 |
| 6 | 250 | 260 | 0,30 |

**Tabla 26.: ** Concentraciones de SO 2 (Percentiles 99, promedio diario) modeladas en las**

| Estación de<br>monitoreo | Valor Norma<br>Primaria<br>(μg/m3N) | Valor Norma<br>Secundaria<br>(μg/m3N) | Valor<br>Modelado<br>(μg/m3N) | Valor<br>Estación<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| Museo ferroviario | 250 | 260 | 0,15 | sin datos |
| Las Encinas | 250 | 260 | 0,03 | sin datos |

**Tabla 27.: ** Concentraciones de SO 2 (anual) modeladas en receptores discretos en la**

| Punto | Valor Norma<br>Primaria<br>(μg/m3N) | Valor Norma<br>Secundaria<br>(μg/m3N) | Valor Modelado<br>(μg/m3N) |
| --- | --- | --- | --- |
| 1 | 80 | 60 | 0,63 |
| 2 | 80 | 60 | 0,41 |
| 3 | 80 | 60 | 0,24 |
| 4 | 80 | 60 | 0,12 |
| 5 | 80 | 60 | 0,14 |
| 6 | 80 | 60 | 0,08 |

**Tabla 28.: ** Concentraciones de SO 2 (anual) modeladas en las estaciones de monitoreo**

| Estación de<br>monitoreo | Valor Norma<br>Primaria<br>(μg/m3N) | Valor Norma<br>Secundaria<br>(μg/m3N) | Valor<br>Modelado<br>(μg/m3N) | Valor Estación<br>(μg/m3N) |
| --- | --- | --- | --- | --- |
| Museo<br>ferroviario | 80 | 60 | 0,025 | sin datos |
| Las Encinas | 80 | 60 | 0,006 | sin datos |

**Tabla 29.: ** Concentraciones de SO 2 (Percentiles 99,73, promedio horario) modeladas**

| Punto | Valor Norma<br>Secundaria<br>(μg/m3N) | Valor Modelado<br>(μg/m3N) |
| --- | --- | --- |
| 1 | 700 | 31,6 |
| 2 | 700 | 31,9 |
| 3 | 700 | 9,56 |
| 4 | 700 | 3,54 |
| 5 | 700 | 6,32 |
| 6 | 700 | 2,19 |

**Tabla 30.: ** Concentraciones de SO 2 (Percentiles 99,73, promedio horario) modeladas**

| Punto | Valor Norma<br>Secundaria<br>(μg/m3N) | Valor Modelado<br>(μg/m3N) | Valor Estación<br>(μg/m3N) |
| --- | --- | --- | --- |
| Estación Museo Ferroviario | 700 | 1,19 | Sin Datos |
| Estación Las Encinas | 700 | 0,30 | Sin Datos |

**Tabla 31.: ** Concentraciones de CO (Percentiles 99, promedio 8 horas) modeladas en**

| Punto | Valor Norma<br>Primaria<br>(mg/m3N) | Valor Modelado<br>(mg/m3N) |
| --- | --- | --- |
| 1 | 10 | 0,0084 |
| 2 | 10 | 0,0048 |
| 3 | 10 | 0,0024 |
| 4 | 10 | 0,0013 |
| 5 | 10 | 0,0015 |
| 6 | 10 | 0,0008 |

**Tabla 32.: ** Concentraciones de CO (Percentiles 99, promedio 8 horas) modeladas en**

| Estación de<br>monitoreo | Valor Norma<br>Primaria<br>(mg/m3N) | Valor Modelado<br>(mg/m3N) | Valor Estación<br>(mg/m3N) |
| --- | --- | --- | --- |
| Museo Ferroviario | 10 | 0,0004 | Sin Datos |
| Las Encinas | 10 | 0,0001 | Sin Datos |
