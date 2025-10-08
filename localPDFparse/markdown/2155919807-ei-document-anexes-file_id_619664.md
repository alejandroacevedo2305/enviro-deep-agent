---
title: Sin título
author: Reynaldo Payano
date: D:20210625170247-04'00'
language: es
type: report
pages: 70
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ESTUDIO DE LÍNEA BASE HIDROLÓGICA PROYECTO PARQUE FOTOVOLTAICO LEYDA
-->

# ESTUDIO DE LÍNEA BASE HIDROLÓGICA PROYECTO PARQUE FOTOVOLTAICO LEYDA

## REGIÓN DE VALPARAÍSO

### INFORME FINAL

Elaborado por:

INRHED SPA

|Tipo documento|Informe Técnico|Col3|Col4|Rev.|0|Col7|
|---|---|---|---|---|---|---|
|**Código SGI**|PR28_HidroPFVLeyda|PR28_HidroPFVLeyda|PR28_HidroPFVLeyda|PR28_HidroPFVLeyda|PR28_HidroPFVLeyda|PR28_HidroPFVLeyda|
|**Cronología documental **|**Cronología documental **|**Cronología documental **|**Cronología documental **|**Cronología documental **|**Cronología documental **|**Cronología documental **|
|**Revisión**|**Fecha**|**Emitido para**|**POR**|**REV.**|**VAL.**|**Para**|
|0|25-06-2021|ALTOYA-SOLEK|RP/ILV|RP|RP|SV/MC|
|D|24-02-2021|ALTOYA-SOLEK|RP/ILV|RP|RP|SV/MC|
|C|05-01-2021|ALTOYA-SOLEK|RP/ILV|RP|RP|SV/MC|
|B|30-12-2020|ALTOYA-SOLEK|RP/ILV|RP|RP|SV/MC|
|A|27-11-2020|Revisión interna|RP/ILV|RP|RP||

**Av. Nueva Providencia 1881,**
**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103**
**Of. 1620, Santiago de Chile**

##### TABLA DE CONTENIDO

1. INTRODUCIÓN ............................................................................................................................4

1.1. Objetivos y Alcances ...............................................................................................................6

2. ANTECEDENTES ..........................................................................................................................7

3. CARACTERIZACIÓN HIDROLÓGICA ..............................................................................................8

3.1. Red de drenaje .......................................................................................................................8

3.2. Temperaturas .......................................................................................................................10

3.3. Evaporación y evapotranspiración .......................................................................................11

3.4. Análisis de precipitaciones medias .......................................................................................12

3.5. Análisis de frecuencia de las precipitaciones máximas ........................................................14

3.6. Caracterización de las cuencas aportantes ...........................................................................18

3.7. Estimación de caudales de crecidas .....................................................................................24

_3.7.1._ _Generación de curvas IDF_ .................................................................................................24

_3.7.2._ _Estimación de crecidas_ .....................................................................................................29

4. CARACTERIZACIÓN HIDRÁULICA ..............................................................................................31

4.1. Alcance .................................................................................................................................31

4.2. Metodología de simulación hidráulica .................................................................................33

_4.2.1._ _Modelización bidimensional del flujo de agua_ ..................................................................33

_4.2.2._ _Fundamentos de cálculo del modelo bidimensional Iber_ ..................................................34

_4.2.3._ _Ecuaciones_ ........................................................................................................................35

_4.2.4._ _Esquemas numéricos y malla de cálculo_ ...........................................................................36

_4.2.5._ _Condiciones de contorno_ ..................................................................................................37

_4.2.6._ _Parámetros de entrada del modelo bidimensional de flujo_ ..............................................38

_4.2.6.1._ _Modelo Digital de Terreno_ ............................................................................................38

_4.2.6.2._ _Rugosidad del terreno_ ..................................................................................................38

_4.2.6.3._ _Malla de cálculo_ ............................................................................................................43

_4.2.6.4._ _Condiciones hidrodinámicas_ .........................................................................................44

_4.2.6.5._ _Condiciones iniciales_ .....................................................................................................45

_4.2.6.6._ _Opciones de cálculo hidráulico_ .....................................................................................45

4.3. Resultados del modelo hidráulico ........................................................................................46

_4.3.1._ _Situación sin proyecto en zona de emplazamiento del parque_ .........................................48

_4.3.2._ _Situación con proyecto en zona de emplazamiento del parque_ ........................................51

5. CONCLUSIONES ........................................................................................................................54

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 0
**Of. 1620, Santiago de Chile**

6. ANEXOS ....................................................................................................................................56

6.1. Anexo A. Modelación rotura del Embalse Cerrillos de Leyda ...............................................56

_6.1.1._ _Tipo de falla analizada (conceptual)_ .................................................................................56

_6.1.2._ _Tipo de falla modelada_ .....................................................................................................57

_6.1.3._ _Parámetros de la falla o brecha modelada_ .......................................................................58

_6.1.4._ _Resultados_ ........................................................................................................................59

6.2. Anexo B. Digital. Datos estaciones DGA ...............................................................................61

6.3. Anexo C. Topografía .............................................................................................................61

6.4. Anexo D. Resumen metodológico para la determinación de caudales de crecidas en cuencas

sin control fluviométrico ..................................................................................................................61

6.5. Anexo E. Solicitud de información DOH Valparaíso ..............................................................67

6.6. Anexo F. Registro fotográfico Leyda .....................................................................................68

##### ÍNDICE DE FIGURAS

Figura 1-1.Ubicación Parque Fotovoltaico Leyda ...............................................................................5

Figura 3-1. Red de drenaje de la zona de estudio. .............................................................................9

Figura 3-2. Red de drenaje de la zona de estudio: zoom ampliado ..................................................10

Figura 3-2. Temperaturas medias, máximas y mínimas mensuales estaciones DGA Melipilla y DCM

Santo Domingo: Elaboración a partir de datos DGA y DMC .............................................................11

Figura 3-3. Isotermas e Isolíneas de evaporación de tanque tipo A según Balance Hídrico de Chile

(1987). ..............................................................................................................................................12

Figura 3-4. Mapa de isoyetas actualizadas interpolado a partir de las estaciones meteorológicas más

próximas a las zona de estudio. .......................................................................................................13

Figura 3-5. Climograma de precipitación media mensual de las estaciones más cercanas a la zona de

estudio; temperatura media mensual de la estación DMC Santo Domingo y estaciones DGA Melipilla

y Laguna Aculeo. Elaboración a partir de datos DGA del BNA y DMC ..............................................14

Figura 3-6. Análisis de frecuencia Gumbel de la estación Cerrillos de Layda [1932 - 2020].............15

Figura 3-7. Análisis de frecuencia Gumbel de la estación Melipilla [1971 - 2020]. ..........................15

Figura 3-8. Análisis de frecuencia Gumbel de la estación Estero Puangue en Ruta 78 [1989 - 2020].

.........................................................................................................................................................16

Figura 3-9. Análisis de frecuencia Estaciones Meteorológicas [1930 - 2020]. .................................17

Figura 3-10. Cuencas aportantes a la zona de estudio .....................................................................19

Figura 3-11. Cuencas aportantes a la zona de estudio: Zoom ampliado ..........................................20

Figura 3-12. Curvas IDF Estación Cerrillos de Leyda (duración 24 horas) .........................................28

Figura 3-13. Curvas IDF Estación Cerrillos de Leyda (duraciones menores a 1 hora) .......................28

Figura 4-1. Alcance del estudio de inundabilidad en parque............................................................32
Figura 4-2. Interrelación entre módulos de cálculo en Iber. Fuente: https://www.iberaula.es/ ......34

Figura 4-3. Ejemplo de edición de nodos de una malla. ...................................................................36

Figura 4-4. MDT en parque. .............................................................................................................38

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 1
**Of. 1620, Santiago de Chile**

Figura 4-5. Ubicación Calicatas Puntos P1 y P9 realizadas en la zona de proyecto ..........................41

Figura 4-6. Calicatas y sus granulometrías asociadas. ......................................................................42

Figura 4-7. Malla no estructurada utilizada en Parque.....................................................................43

Figura 4-8. Localización de las condiciones de contorno de entrada para modelo Iber en parque. .44

Figura 4-9. Rangos de velocidades definidos para este Proyecto. ....................................................46

Figura 4-10. Hidrodinámica de sistema hidrológico. Se muestra la hidráulica de calado en

modelación bidimensional (Iber) para 4 pasos de tiempo (a = 270 s., b = 1.780 s., c = 33.340 s. y d

66.500 s.) ..........................................................................................................................................47

Figura 4-11. Lámina de inundación T = 100, Tirante de agua para situación sin proyecto en parque

.........................................................................................................................................................49

Figura 4-12. Lámina de inundación T = 100, Velocidad de flujo para situación sin proyecto en parque

.........................................................................................................................................................50

Figura 4-13. Lámina de inundación T = 100, Tirante de agua para situación con proyecto en parque

.........................................................................................................................................................52

Figura 4-14. Lámina de inundación T = 100, Velocidad de flujo para situación con proyecto en parque

.........................................................................................................................................................53

Figura 6-1. Tabla de síntesis de riesgos críticos en algunos embalses de San Antonio. ....................56

Figura 6-2. Conclusiones y recomendaciones asociadas a la ficha de Evaluación de Riesgo Total de la

Presa (Embalse Cerrillos de Leyda). ..................................................................................................57

Figura 6-3. Secuencia lógica conceptual del tipo de falla analizada. ................................................57

Figura 6-4. Tipo de falla o brecha trapezoidal modelada. ................................................................58

Figura 6-5. En color rojo está representado el eje longitudinal de rotura del muro de tierra de

Embalse Leyda. .................................................................................................................................58

Figura 6-6. Hidrodinámica de la rotura en Iber para 4 instantes (a segundo 70.000; b segundo 71.800;

y c segundo 80.000) .........................................................................................................................60

Figura 6-7. Hidrograma del caudal de salida tras rotura del embalse. .............................................61

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 2
**Of. 1620, Santiago de Chile**

##### ÍNDICE DE TABLAS

Tabla 1-1: Coordenadas referenciales del emplazamiento del Parque Fotovoltaico Parque Leyda ...4

Tabla 3-1: Conjunto de estaciones meteorológicas seleccionadas ...................................................13

Tabla 3-2: Resumen de resultados análisis de frecuencia [1930-2020] ............................................17

Tabla 3-3: Parámetros geomorfológicos de las cuencas aportantes: CAP-1 hasta CAP-7 .................21

Tabla 3-4: Parámetros geomorfológicos de las cuencas aportantes: CAP-E1 hasta CAP-E6 .............22

Tabla 3-5: Parámetros geomorfológicos de las cuencas aportantes: CAP-E7 hasta CAP-E12 ...........23

Tabla 3-6: Intensidades de lluvia para distintos períodos de retorno ..............................................24

Tabla 3-7: Coeficientes de duración para 10 años de período de retorno .......................................24

Tabla 3-8: Coeficientes de frecuencia ..............................................................................................24

Tabla 3-9: Tiempo de concentración de las subcuencas aportantes ................................................26

Tabla 3-10: Resumen de resultados de intensidades de diseño: zona de paneles ...........................27

Tabla 3-11: Coeficientes de escorrentía adoptados para las subcuencas aportantes ......................29

Tabla 3-12: Coeficientes de escorrentía adoptados para las subcuencas aportantes (continuación)

.........................................................................................................................................................29

Tabla 3-13: Coeficientes de escorrentía adoptados para las subcuencas aportantes (continuación)

.........................................................................................................................................................30

Tabla 3-14: Resumen de resultados de caudales líquidos máximos estimados para las cuencas

aportantes ........................................................................................................................................30

Tabla 4-1. Valores para el Cálculo del Coeficiente de Manning Mediante Método de Cowan. ........40

Tabla 4-2. Resumen coordenada y profundidad de las calicatas ......................................................41

Tabla 4-3. Coeficientes de Manning según fórmula de Cowan........................................................43

Tabla 4-4. Caudales y cuenca de captación asociada a cada entrada ...............................................45

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 3
**Of. 1620, Santiago de Chile**

PR28 - Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

#### 1. INTRODUCIÓN

El Parque Fotovoltaico Leyda, corresponde a una central generadora, que se emplazará en un terreno

de 120,4 ha y estará ubicado en la comuna de San Antonio, Provincia homónima, Región de

Valparaíso. Este proyecto consiste en un parque fotovoltaico (PFV) de 96 MW, el cual generará

electricidad a partir de energía solar mediante la instalación de 177.961 módulos fotovoltaicos, la que

será inyectada al Sistema Eléctrico Nacional (SEN) a través de un punto de conexión en 110 kV, que

empalmará directamente con la subestación eléctrica Leyda, a pocos metros del área del PFV.

El proyecto fue ingresado como una DIA (Declaración de Impacto Ambiental) al SEA (Servicio de

Evaluación Ambiental). En dicho contexto, a través del ICSARA N°91 con fecha del 05 de abril del año

2021, se han generado una serie de observaciones enfocadas a las aguas superficiales, las cuales

deben ser respondidas para la aprobación de la RCA (Resolución de Calificación Ambiental) del

proyecto.

Altoya & Solek le han encargado a INRHED SPA los estudios correspondientes para la realización de

una Línea Base Hidrológica del Parque Fotovoltaico (Figura 1-1).

En la Tabla 1-1, se presentan las coordenadas geográficas referenciales del polígono de

emplazamiento del Parque Fotovoltaico Leyda.

_Tabla 1-1: Coordenadas referenciales del emplazamiento del Parque Fotovoltaico Parque Leyda_

|Vértices|Coordenadas WGS84 H19S|Col3|
|---|---|---|
|**Vértices**|**UTM Este (m)**|**UTM Norte (m)**|
|V1|271.238|6.277.533|
|V2|268.958|6.278.391|
|V3|268.913|6.277.938|
|V4|269.331|6.277.360|
|V5|270.631|6.277.136|

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 4
**Of. 1620, Santiago de Chile**

PR28 - Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 1-1.Ubicación Parque Fotovoltaico Leyda_

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 5
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

##### 1.1. Objetivos y Alcances

El objetivo principal del presente proyecto es desarrollar un estudio hidrológico e hidráulico del

Proyecto Parque Fotovoltaico Leyda, enfocado a generar una línea base hidrológica, determinar las

zonas de inundación para un periodo de retorno T=100 años y diseñar obras hidráulicas de

protección (en caso necesario).

El alcance del proyecto incluye:

 - Visita a terreno para el levantamiento de información

 - Elaboración de estudio hidrológico enfocado a la interpretación del clima y precipitaciones

en la zona, análisis de precipitaciones máximas para diferentes periodos de retorno (T= 2 a

100 años), estudio de escorrentías superficiales (caudales líquidos), flujos aluvionales

(caudales detríticos) e interferencias de cauces naturales de carácter cíclico.

 - Modelación hidráulica que permita identificar zonas de inundación en el emplazamiento de

paneles y torres. Y de acuerdo a los resultados de la modelación hidráulica se propondrán

diseño de obras hidráulicas de protección en caso necesario

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 6
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

#### 2. ANTECEDENTES

Se han recopilado y analizado los antecedentes disponibles, los que incluyen trabajos técnicos

relacionados geomorfología, hidrología (precipitaciones, caudales, temperaturas,

evapotranspiración, etc.), obras civiles, ingeniería ambiental, estudios de recursos hídricos y otros.

Dicha información fue recopilada a partir de la información proporcionada por ALTOYA & SOLEK la

información disponible en servicios públicos tales como el Servicio Nacional de Geología y Minería

(SERNAGEOMIN), la Dirección General de Aguas (DGA), Servicio de Evaluación Ambiental (SEA),

Dirección Meteorológica de Chile (DMC), entre otros.

Los antecedentes recopilados fueron los siguientes:

 - INRHED & GEOMAG (2021). Levantamiento Topográfico Parque Fotovoltaico Leyda.

 - ALTOYA & SOLEK (2020). Archivo AutoCAD DWG “PR_CL_0733_DP_0603_rev05_Adenda”,

que contiene layout del parque y topografía existente.

 - ALTOYA & SOLEK (2020). Archivo KMZ “PR_CL_0733_DP_0603_rev05_Adenda”, que

contiene la ubicación, área y los límites del Parque Leyda.

 - INRHED (2020). Informe Línea Base Hidrológica Proyecto Parque Fotovoltaico Leyda.

 - INRHED (2020). Informe Línea Base Hidrogeológica Proyecto Parque Fotovoltaico Leyda.

 - DGA-BNA (2020). Estadísticas de precipitaciones, temperaturas y caudales en las estaciones

DGA próximas a la zona de estudio.

 - DGA-IPLA (1987). Balance Hídrico de Chile. Ministerio de Obras Públicas, Santiago, Chile.

 - DGA, U. Chile & PUC (2017). Actualización del Balance Hídrico Nacional, SIT N° 417.

Ministerio de Obras Públicas, Dirección General de Aguas, División de Estudios y

Planificación. Realizado por la Universidad de Chile & Pontificia Universidad Católica de

Chile.

 - Guía Metodológica para Presentación y Revisión Técnica de Proyectos de Modificación de

Cauces Naturales y Artificiales. DGA, 2016.

 - Guía de Permisos Ambientales sectoriales en el SEIA: Permiso para la construcción de ciertas

obras hidráulicas. Gobierno de Chile, DGA, SNGM.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 7
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

#### 3. CARACTERIZACIÓN HIDROLÓGICA

##### 3.1. Red de drenaje

En En términos hidrológicos, el área de estudio se encuentra inserta en la subsubcuenca DGA “Rio
Maipo Entre Estero Popeta y Desembocadura (413,56 km [2] ) perteneciente a la subcuenca DGA “Rio
Maipo Bajo (Entre Rio Mapocho y Desembocadura)- 3363,03 km [2] )” y esta a su vez perteneciente a
la gran cuenca DGA “Río Maipo (15273,14 km [2] )”, que actualmente presenta un régimen exorreico

bien activo. En la zona existe una red de drenaje bien definida, caracterizada por el escurrimiento

permanente del Estero Leyda que sigue una orientación EW en dirección al Embalse Leyda. Así

mismo, hacia el sur del proyecto se encuentra el embalse Cerrillos de Leyda o Embalse Leyda,

inventariado por la DGA & DOH en el año 2016 como un embalse para uso de riego construido el

año 1932 con una altura de muro de 19 m (Figura 3-1).

Los cauces o escurrimientos que se observan en la zona son cárcavas o socavones formados en la

roca intrusiva por la acción del agua. La roca sobre la cual se disponen las obras del proyecto, está

fuertemente meteorizada en superficie, lo que facilita la formación de cárcavas o socavones

producto de escurrimientos superficiales esporádicos asociados a precipitaciones, los que van

labrando la superficie rocosa. Sin embargo, durante la inspección en terreno, se constató que estos

rasgos que componen los cauces del sector, se encuentran completamente secos y que por ende

sólo canalizan el agua cuando hay precipitaciones suficientes para desarrollar escurrimiento

superficial.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 8
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 3-1. Red de drenaje de la zona de estudio._

De acuerdo a la revisión de la carta IGM escala 1:50.000 denominada “E063 Puangue” y en los

puntos indicados por la autoridad en la ICSARA como N: 6.277.833 m, E: 269.858 m (Pto 1, en Figura
3-2) / N: 6.277.755 m, E: 269.706 m (Pto 2, en Figura 3-2) el cauce se encuentra desplazado hacia el

sur entre 10 y 65 m según la realidad del trazado del cauce (Red actual en Figura 3-2) y la topografía

detalle presentada en el Anexo C. Además, para mayor entendimiento del sector se realizó un

recorrido por el cauce señalado por la autoridad (Red IGM) y se presenta un archivo kmz con las

fotos georreferenciadas donde se puede observar las fotos el cauce IGM vs el cauce principal actual

(Ver Anexo F). Por lo tanto, no se modifican los cauces naturales ni artificiales superficiales.

Respecto a los puntos N: 6.278.381 m, E: 268.976 m (Pto 3, en Figura 3-2) / N: 6.278.161 m, E:

268.926 m (Pto 4, en Figura 3-2) se aclara que al igual que lo mencionado anteriormente el cauce

IGM no estaría siendo modificado, ya que en la realidad (Red actual, en Figura 3-2) debido a que en

la zona dicho cauce no se proyectan obra de paneles ni otra obra que pudiera afectar el libre

escurrimiento. El cerco perimetral que se proyecta en el punto N: 6.278.161 m, E: 268.926 m será

un cerco vivo existente que se mantendrá durante las distintas etapas del proyecto. La modelación

de los puntos indicados y de todo el sistema hídrico se presentan en el Capítulo 4 del presente

documento.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 9
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 3-2. Red de drenaje de la zona de estudio: zoom ampliado_

##### 3.2. Temperaturas

El registro de información disponible de temperaturas en las zonas es muy escaso. La temperatura

media anual en la zona oscila entre 12°C y 14oC de acuerdo con las isotermas del Balance Hídrico de

Chile (DGA, 1987). Dichos valores son coherentes con el estimado en la estación meteorológica

Santo Domingo de la Dirección Meteorológica de Chile -DMC (1966-2020) y la estación DGA Melipilla

(1971-2013) del orden de 12,1°C y 14,81 oC, tal como se muestra en la Figura 3-3. La distribución

mensual de las temperaturas máximas, medias y mínimas de ambas estaciones se presentan en la

misma Figura 3-2. De acuerdo a la estación meteorológica vigente más cercana a la zona de estudio

(DMC Santo Domingo), las temperatura mínimas se registran en los meses de invierno,

particularmente entre junio y agosto con valores de 6,87°C y 7,17 °C y la máxima en los meses de

verano (principalmente en Enero) con valores entre 16,31°C y 18,08°C. Dichas temperaturas son

típicas de clima mediterráneo de lluvia invernal e influencia costera invernal Csb (i) según el sistema

Köppen-Geiger (Figura 3-4), cuyas condiciones climáticas en la zona se traduce en un efecto

modulador de las temperaturas, la presencia de humedad, neblinas matinales y una pluviometría
que supera los 100 mm anual (pudiendo llegar a valores de 900 mm/año), donde en el mes más frio

las temperaturas medias superan los 0°C y las temperaturas medias anuales en torno a los 12 °C.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 10
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 3-3. Temperaturas medias, máximas y mínimas mensuales estaciones DGA Melipilla y DCM Santo Domingo:_

_Elaboración a partir de datos DGA y DMC_

##### 3.3. Evaporación y evapotranspiración

Según el Balance Hídrico de Chile (1987), la evaporación potencial del área es del orden de 2500
mm/año (Figura 3-3). Utilizando el método de Turc, que indica que:

P
ETR (Turc) =

2

0,9 + [P]
~~√~~ L [2]

L [2]

Donde:

ETR = evaporación real en mm/año; P =precipitación en mm/año; _L=300+25t+0,005t_ _[3]_ (siendo t la

temperatura media anual en oC).

Se obtuvo un valor de evapotranspiración real (ETR) de 343,9 mm/año para la zona de estudio, que
es coherente con el valor de ETR estimado por la DGA (1987) de 300 mm/año.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 11
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 3-4. Isotermas e Isolíneas de evaporación de tanque tipo A según Balance Hídrico de Chile (1987)._

##### 3.4. Análisis de precipitaciones medias

Próximo a la zona de estudio existe la estación meteorológica DGA Cerrillos de Layda, ubicada a

unos 3,4 km al suroeste del predio, a una altitud de 182 msnm y dentro de la misma subcuenca

hidrográfica. Posee una longitud de datos representativos de 90 años desde el año 1932 hasta 2020.
Sus datos permiten caracterizar una precipitación media con un valor de 394,64 mm/año para el

área de estudio, valor muy coherente con el Balance Hídrico de Chile (DGA, 1987) y las isoyetas
interpoladas de INRHED (2020) que estimaron valores entre 300 y 400 mm/año (Figura 3-5).

Otras estaciones que están cerca de la zona (hacia el Este y Sur del proyecto) permiten caracterizar
una precipitación menor del orden de 164,48 mm/año (RIO MAIPO EN CABIMBAO); 264,45 mm/año
(ESTERO PUANGUE EN RUTA 78) y 353,51 mm/año (MELIPILLA).

En la Tabla 3-1 se presentan las características principales de todas las estaciones más cercanas a la

zona de estudio (nombre, código BNA, coordenadas UTM WGS84, altitud, fecha de inicio y final del

registro, longitud de la serie, distancia hasta la zona de estudio y precipitación media).

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 12
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Tabla 3-1: Conjunto de estaciones meteorológicas seleccionadas_

|N°|Nombre estación|Código BNA|UTM N [m]|UTM E [m]|Altura<br>[msnm]|Fecha<br>inicio|Fecha<br>final|Longitud<br>de la<br>serie<br>(años)|Distancia<br>a la zona<br>de<br>estudio<br>[Km]|Pp<br>med<br>[mm]|
|---|---|---|---|---|---|---|---|---|---|---|
|1|CERRILLOS DE<br>LEYDA|05748003-3|6275551|267151|182|mar-32|jul-20|90|3,4|**394,64**|
|2|ESTERO<br>PUANGUE EN<br>RUTA 78|05746001-6|6272931|283302|93|abr-89|jul-20|33|14,3|**263,45**|
|3|RIO MAIPO EN<br>CABIMBAO|05748001-7|6260738|265651|35|oct-09|jul-20|10|17,5|**164,48**|
|4|MELIPILLA|05740005-6|6271128|296069|168|ago-71|jul-20|47|27,2|**353,51**|
|5|FUNDO LAS DOS<br>PUERTAS|05800002-7|6250021|253643|24|jun-90|jul-20|32|32,1|**415,14**|
|6|CARMEN DE LAS<br>ROSAS|05740004-8|6262366|300173|165|nov-30|jul-20|91|34,1|**416,64**|
|7|LOS GUINDOS|05747001-1|6247706|293453|125|jul-89|jul-20|32|38,2|**436,90**|
|8|RAPEL|06056003-K|6240222|247305|16|jul-40|jul-20|80|43,7|**523,89**|
|9|BARRERA<br>LONCHA|06042004-1|6226976|297450|144|may-84|jul-20|38|57,8|**429,19**|
|10|VILLA ALHUE|06040001-6|6231976|306676|197|ene-79|jul-20|43|58,9|**442,09**|

Fuente: Elaboración propia a partir del BNA de la DGA.

_Figura 3-5. Mapa de isoyetas actualizadas interpolado a partir de las estaciones meteorológicas más próximas a las zona_

_de estudio._

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 13
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

En la Figura 3-6 se presenta la distribución de precipitaciones mensuales de las estaciones más

cercanas y representativas de la zona de estudio: Cerrillos De Leyda, Estero Pangue en Ruta 78,

Fundo Las Dos Puertas, Los Guindos, Rapel, Carmen De Las Rosas, Melipilla, Barrera Loncha, y Villa

Alhue. La variación mensual de la precipitación de la Estación Cerrillos de Leyda muestra que los

meses de mayo (72,8 mm), junio (98,74 mm), julio (91,21) y agosto (63,97 mm), son los más lluviosos

y coincide con las temperaturas más bajas. Además, se observa que las menores precipitaciones o

mes más secos se presentan entre octubre y marzo (específicamente en verano, entre diciembre y

febrero) que no alcanzan los 15,0 mm mensual y ocasionalmente se producen eventos esporádicos
extremos en septiembre, marzo y abril que pueden llegar superar los 20,0 mm/mensual.

_Figura 3-6. Climograma de precipitación media mensual de las estaciones más cercanas a la zona de estudio;_
_temperatura media mensual de la estación DMC Santo Domingo y estaciones DGA Melipilla y Laguna Aculeo._

_Elaboración a partir de datos DGA del BNA y DMC_

##### 3.5. Análisis de frecuencia de las precipitaciones máximas

De las diez (10) estaciones de monitoreo presentadas anteriormente en la Tabla 3-1, se han

seleccionado tres (3) estaciones meteorológicas (Cerrillos De Leyda, Estero Pangue en Ruta 78 y

Melipilla), que son las más representativa en cuanto al registro de datos y el contexto hidrológico

de la zona de estudio. Poseen un registro de más de 30 años de datos completos.

Para el cálculo de los caudales asociados a las cuencas aportantes del proyecto (ver siguiente ítem

3.6) se han analizado las precipitaciones máximas en 24 horas de las 3 estaciones meteorológicas

de la DGA comentadas anteriormente, cuyo registro de datos se presentan en el Anexo B.

Posteriormente, a la serie de datos de precipitaciones máximas se le realizó un análisis de frecuencia

ajustando las siguientes funciones de probabilidad: Normal, Log-Normal, Pearson, Log-Pearson y

Gumbel. En cada función se empleó el “ _test chi-cuadrado_ ” como indicador de descarte,

complementado en un análisis gráfico con la finalidad de determinar la probabilidad de frecuencia

que mejor se ajuste para cada una de las series analizadas.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 14
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

En base a los análisis realizados se determinó que la función que mejor se ajusta para las

precipitaciones máximas de las estaciones corresponde a la Gumbel. Los resultados obtenidos para

distintos periodos de retorno (T= 2 a 100 años) se presentan en la Tabla 3-2, mientras que los

resultados del ajuste gráfico se muestran en la Figura 3-7, Figura 3-8 y Figura 3-9, para las estaciones

analizadas.

_Figura 3-7. Análisis de frecuencia Gumbel de la estación Cerrillos de Layda [1932 - 2020]._

_Figura 3-8. Análisis de frecuencia Gumbel de la estación Melipilla [1971 - 2020]._

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 15
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 3-9. Análisis de frecuencia Gumbel de la estación Estero Puangue en Ruta 78 [1989 - 2020]._

En la Tabla 3-2 y Figura 3-8 se presenta un resumen de los resultados de análisis de frecuencia para

el periodo analizado (1930-2020) para las estaciones seleccionadas, los cuales son coherentes en
órdenes de magnitud con las estimaciones realizadas por DGA (1987) [1] y DGA (1989) [2] para un
periodo de retorno de 10 años entre 80 y 90 mm/día. Luego del análisis realizado de todas las

estaciones cercanas al proyecto (zona de paneles y línea eléctrica), se ha seleccionado la estación

Cerrillos de Leyda (siguiendo los criterios comentado en el punto 3.4) para el cálculo de los caudales

máximos de las cuencas aportantes y modelación hidráulica.

1 DGA (1987) Balance Hídrico de Chile. Departamento de Hidrología. Dirección General de Aguas. Ministerio
de Obras Públicas. Santiago, Chile.
2 DGA, 1989. Precipitaciones máximas en 1, 2 y 3 días. Dirección General de Aguas, Ministerio de Obras
Públicas. Santiago, Chile.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,**
**Of. 1620, Santiago de Chile**

16

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Tabla 3-2: Resumen de resultados análisis de frecuencia [1930-2020]_

|Período de Retorno<br>(años)|Precipitación Máxima Anual en 24 Horas (mm)|Col3|Col4|
|---|---|---|---|
|Período de Retorno<br>(años)|Cerrillos De Leyda<br>(1932-2020)|Estero Pangue en Ruta 78<br>(1989-2020)|Melipilla<br>(1971-2020)|
|2|54.9|42.5|49.2|
|5|80.1|64.7|69.6|
|10|96.7|79.4|83.1|
|20|112.7|93.5|96.1|
|25|117.8|97.9|100.2|
|50|133.4|111.7|112.9|
|100|148.9|125.4|125.5|
|**c2(calculado)=**|1.7|0.7|1.5|
|**c2(0,05)=**|6.0|6.0|6.0|
|**Test**|Aceptado|Aceptado|Aceptado|

_Figura 3-10. Análisis de frecuencia Estaciones Meteorológicas [1930 - 2020]._

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 17
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

A partir del análisis de frecuencia mostrado anteriormente se puede comentar lo siguiente:

 - La obtención de precipitaciones máximas para los periodos de retorno de interés es

coherente a lo esperado en la zona de estudio.

 - La función Gumbel fue la que presentó el mejor ajuste estadístico/gráfico para las

estaciones analizadas (Cerrillos De Leyda, Estero Pangue en Ruta 78 y Melipilla).

 - La estación meteorológica Cerrillos de Leyda es la más representativa de la hidrología del

proyecto (zona de paneles y líneas de transmisión), la cual cuenta con una longitud de datos

representativos de 90 años y se ubica a unos 3,4 km al Suroeste del proyecto, a una altitud

de 182 msnm y dentro de la misma subcuenca hidrográfica. Dicha estación reproduce

bastante bien los eventos extremos ocurridos en la zona de estudio. Por lo cual se

considerará la estadística de dicha estación para el cálculo de los caudales aportantes a la

zona de estudio.

 - Para un periodo de retorno de T= 10 años se obtuvo un valor de 96,7 mm, la cual es

coherente (en órdenes de magnitud un poco mayor) con la estimada por el Balance Hídrico

Nacional (DGA, 1987) alrededor de 90 mm.

 - Asimismo, para un periodo de retorno de T= 100 años se obtuvo un valor de 148,9 mm, cuyo

valor está por encima del mayor evento de precipitación registrado cercano a la zona (124

mm en 24 horas el día 12 de julio de 1940). Por lo tanto, se tomará el valor de T=100 años

calculado como la precipitación de diseño.

##### 3.6. Caracterización de las cuencas aportantes

Se ha realizado una caracterización morfológica de las cuencas aportantes a la zona de estudio para

lo cual se trazaron los límites de las cuencas y la red de drenaje. Esto se realizó a partir de la

topografía disponible (Anexo C) y usando herramientas de integración espacial en los Sistemas de

Información Geográfica (SIG) y manejo de algoritmos _Hydrology - watershed delimitation_

disponibles en los softwares GIS. Para esto se utilizó como apoyo las imágenes satelitales de Google

Earth y los modelos de elevación digital (DEM) de la NASA “ASTER Global Digital Elevation Model

(GDEM) Version 3 (ASTGTM)” con una resolución espacial de 30 x 30 m que permiten representar

la red de drenaje tanto de la DGA como del IGM.

En la Figura 3-11 y Figura 3-12 se presentan las cuencas aportantes a la zona de estudio: CAP-1 hasta

CAP-7 (que son cuencas internas que drenan hacia el sur del proyecto); CAP-E1 hasta CAP-E9

(cuencas aportantes que drenan hacia la zona del Embalse Leyda y que de forma indirecta influyen

en la modelación del sistema hídrico); CAP-E10, CAP-E11, CAP-E12 y CAP-E13 (cuencas internas que

drenan hacia el norte del proyecto); mientras que en la Tabla 3-3, Tabla 3-4 y Tabla 3-5 se reportan

los parámetros geomorfológicos de cada una de ellas.

Se aclara que los pequeños aportes de las cuencas del sector sur y norte están contenidas dentro

de la memoria de cálculo hidrológico de caudales, dado que en términos hidrológicos sólo una parte

de la cuenca CAP-1 constituiría un aporte directo al proyecto. Sin embargo, se han delimitado las

cuencas aportantes dentro del proyecto (CAP-1, CAP-2, CAP-3, CAP-4, CAP-5, CAP-6, CAP-7; CAP
E10; CAP-E11 y CAP-12) para poder realizar la modelación hidráulica de los escurrimientos dentro

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 18
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

del parque con el objetivo de no modificarlos. Las cuencas aportantes al exterior del proyecto (CAP
E1 hasta CAP-E9) no constituyen un aporte directo al proyecto sino al Embalse Leyda y al Estero

Leyda, que se han delimitado dichas cuencas para realizar la modelación hidráulica y simular el

crecimiento que tendría el embalse para un periodo de retorno de 100 años y su posible interacción

con el proyecto. Además, para responder lo solicitado por la autoridad en la adenda anterior en

referencia al “estudio de inundación para una crecida de periodo de retorno de 100 años, con una

extensión de al menos 100 m aguas arriba a las coordenadas UTM Datum WGS84 (huso 19) Norte:

6.276.963 m y Este: 270.591 y 100 m aguas abajo del muro del Embalse Leyda”.

_Figura 3-11. Cuencas aportantes a la zona de estudio_

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 19
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 3-12. Cuencas aportantes a la zona de estudio: Zoom ampliado_

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 20
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Tabla 3-3: Parámetros geomorfológicos de las cuencas aportantes: CAP-1 hasta CAP-7_

|PARÁMETROS MORFOMÉTRICOS GENERALES|Col2|SUBCUENCA<br>CAP-1|SUBCUENCA<br>CAP-2|SUBCUENCA<br>CAP-3|SUBCUENCA<br>CAP-4|SUBCUENCA<br>CAP-5|SUBCUENCA<br>CAP-6|SUBCUENCA<br>CAP-7|
|---|---|---|---|---|---|---|---|---|
|**Parámetro**|**Símbolo**|**Valor**|**Valor**|**Valor**|**Valor**|**Valor**|**Valor**|**Valor**|
|Perímetro (km)|P|1.77|1.83|1.77|1.90|1.51|1.77|1.46|
|Área (km2)|A|0.14|0.19|0.11|0.17|0.10|0.14|0.12|
|Longitud cauce principal (km)|LCP|0.36|0.63|0.38|0.56|0.45|0.34|0.38|
|Desnivel altitudinal (m)|DA|19.00|31.00|34.00|38.00|42.00||34.00|
|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|
|Cota máxima (msnm)|cmax|188.00|200.00|203.00|207.00|211.00|209.00|210.00|
|Cota mínima (msnm)|cmin|169.00|169.00|169.00|169.00|169.00|170.00|176.00|
|Altitud media (msnm)|Am|177.59|184.23|180.82|187.56|189.17|191.03|192.99|
|Pendiente promedio de la cuenca (%)|**Smed**|**6.03**|**6.76**|**6.19**|**7.39**|**8.53**|**8.78**|**8.57**|
|Altitud máx del cauce (msnm)|Amaxc|177.00|187.00|182.00|188.00|195.00|191.00|197.00|
|Altitud min del cauce (msnm)|Aminc|169.00|169.00|169.00|169.00|169.00|170.00|173.00|
|Altitud media del cauce (msnm)|Amedc|173.69|178.35|174.47|178.00|179.89|181.25|183.33|
|Pendiente promedio del cauce (%)|**Sc**|**4.10**|**5.15**|**4.45**|**5.22**|**6.48**|**7.31**|**6.46**|
|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|
|Longitud de la cuenca (km)|D|0.41|0.68|0.62|0.69|0.61|0.63|0.52|
|Factor de forma|FF|0.813|0.405|0.298|0.356|0.272|0.364|0.451|
|Coeficiente de compacidad|Kc|1.34|1.18|1.46|1.29|1.33|1.30|1.17|
|Coeficiente de circularidad<br>(redondez)|CC|0.97|1.94|2.63|2.21|2.89|2.16|1.74|

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 21
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Tabla 3-4: Parámetros geomorfológicos de las cuencas aportantes: CAP-E1 hasta CAP-E6_

|PARÁMETROS MORFOMÉTRICOS GENERALES|Col2|SUBCUENC<br>A CAP-E1|SUBCUENC<br>A CAP-E2|SUBCUENC<br>A CAP-E3|SUBCUENC<br>A CAP-E4|SUBCUENC<br>A CAP-E5|SUBCUENC<br>A CAP-E6|
|---|---|---|---|---|---|---|---|
|**Parámetro**|**Símbol**<br>**o **|**Valor**|**Valor**|**Valor**|**Valor**|**Valor**|**Valor**|
|Perímetro (km)|P|18.60|1.14|17.54|5.05|3.21|2.04|
|Área (km2)|A|12.88|0.08|9.23|0.68|0.53|0.20|
|Longitud cauce principal (km)|LCP|7.04|0.27|7.35|1.77|1.04|0.79|
|Desnivel altitudinal (m)|DA|415.00|10.00|409.00|92.00|72.00|69.00|
|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|
|Cota máxima (msnm)|cmax|585.00|179.00|578.00|261.00|241.00|238.00|
|Cota mínima (msnm)|cmin|170.00|169.00|169.00|169.00|169.00|169.00|
|Altitud media (msnm)|Am|249.45|172.11|258.22|195.41|190.48|194.19|
|Pendiente promedio de la cuenca<br>(%)|**Smed**|**16.30**|**3.76**|**16.54**|**9.21**|**9.64**|**10.57**|
|Altitud máx del cauce (msnm)|Amaxc|393.00|173.00|464.00|215.00|201.00|204.00|
|Altitud min del cauce (msnm)|Aminc|170.00|169.00|169.00|169.00|169.00|169.00|
|Altitud media del cauce (msnm)|Amedc|207.00|170.58|227.86|183.37|178.98|187.23|
|Pendiente promedio del cauce (%)|**Sc**|**6.94**|**2.22**|**9.04**|**4.83**|**6.11**|**6.91**|
|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|
|Longitud de la cuenca (km)|D|6.61|0.36|6.28|1.22|1.03|0.68|
|Factor de forma|FF|0.295|0.600|0.234|0.454|0.499|0.426|
|Coeficiente de compacidad|Kc|1.45|1.15|1.62|1.72|1.23|1.28|
|Coeficiente de circularidad<br>(redondez)|CC|2.66|1.31|3.36|1.73|1.57|1.85|

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 22
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Tabla 3-5: Parámetros geomorfológicos de las cuencas aportantes: CAP-E7 hasta CAP-E12_

|PARÁMETROS MORFOMÉTRICOS<br>GENERALES|Col2|SUBCUE<br>NCA<br>CAP-E7|SUBCUEN<br>CA CAP-E8|SUBCUEN<br>CA CAP-E9|SUBCUEN<br>CA CAP-<br>E10|SUBCUEN<br>CA CAP-<br>E11|SUBCUEN<br>CA CAP-<br>E12|SUBCUEN<br>CA CAP-<br>E13|
|---|---|---|---|---|---|---|---|---|
|**Parámetro**|**Valor**|**Símbolo**|**Valor**|**Valor**|**Valor**|**Valor**|**Valor**|**Valor**|
|Perímetro (km)|3.01|P|1.32|1.55|1.40|1.21|2.15|1.10|
|Área (km2)|0.51|A|0.10|0.15|0.11|0.07|0.20|0.07|
|Longitud cauce principal (km)|1.03|LCP|0.36|0.38|0.21|0.12|0.52|0.38|
|Desnivel altitudinal (m)|111.00|DA|62.00|61.00|29.00|24.00|36.00|21.00|
|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DEL RELIEVE**||
|Cota máxima (msnm)|280.00|cmax|231.00|230.00|196.00|212.00|220.00|185.00|
|Cota mínima (msnm)|169.00|cmin|169.00|169.00|167.00|188.00|184.00|164.00|
|Altitud media (msnm)|215.67|Am|201.54|192.24|178.94|197.80|194.21|174.12|
|Pendiente promedio de la<br>cuenca (%)|**18.70**|**Smed**|**20.17**|**14.63**|**6.94**|**8.41**|**8.45**|**8.17**|
|Altitud máx del cauce (msnm)|246.00|Amaxc|203.00|188.00|171.00|188.00|194.00|180.00|
|Altitud min del cauce (msnm)|169.00|Aminc|169.00|169.00|167.00|188.00|184.00|162.00|
|Altitud media del cauce (msnm)|195.93|Amedc|183.00|175.44|170.56|188.00|187.82|172.40|
|Pendiente promedio del cauce<br>(%)|**11.55**|**Sc**|**16.94**|**7.60**|**3.38**|**3.89**|**5.19**|**8.43**|
|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**|**PARÁMETROS MORFOMÉTRICOS ASOCIADOS A LA FORMA DE LA CUENCA**||
|Longitud de la cuenca (km)|0.96|D|0.49|0.56|0.33|0.30|0.68|0.410|
|Factor de forma|0.549|FF|0.414|0.487|1.012|0.830|0.434|0.426|
|Coeficiente de compacidad|1.18|Kc|1.17|1.11|1.18|1.24|1.35|1.15|
|Coeficiente de circularidad<br>(redondez)|1.43|CC|1.90|1.61|0.78|0.95|1.81|1.84|

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 23
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

##### 3.7. Estimación de caudales de crecidas

_3.7.1._ _Generación de curvas IDF_

Lo primero a considerar en el trazado de curvas IDF es la información pluviográfica disponible en las

cercanías de la zona en estudio. Para esto, se revisaron los antecedentes mencionados en el Capítulo

2 del presente informe.

La información relevante corresponde a las intensidades de lluvia (Tabla 3.702.402.A), coeficientes

de duración (Tabla 3.702.403.A) y de frecuencia (Tabla 3.702.403.B) del Manual de Carreteras (MOP,

2020) para la estación pluviográfica Melipilla, según se presenta a continuación.

_Tabla 3-6: Intensidades de lluvia para distintos períodos de retorno_

|Estación<br>Pluviométrica|T<br>[años]|Duración [horas]|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Estación**<br>**Pluviométrica**|**T **<br>**[años]**|**1 **|**2 **|**4 **|**6 **|**8 **|**10**|**12**|**14**|**18**|**24**|
|**Melipilla**|**10**|11,65|10,36|8,63|7,76|6,86|6,22|5,64|5,31|4,81|4,11|
|**Melipilla**|**25**|14,34|12,66|10,51|9,48|8,39|7,64|6,95|6,57|6,01|5,16|
|**Melipilla**|**50**|16,34|14,37|11,90|10,76|9,52|8,69|7,91|7,50|6,90|5,94|
|**Melipilla**|**100**|18,33|16,07|13,28|12,02|10,65|9,73|8,87|8,43|7,78|6,71|

_Fuente: Tabla 3.702.402.A del Manual de Carreteras (MOP, 2020)_

_Tabla 3-7: Coeficientes de duración para 10 años de período de retorno_

|Estación<br>Pluviométrica|Duración [horas]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Estación**<br>**Pluviométrica**|**1 **|**2 **|**4 **|**6 **|**8 **|**10**|**12**|**14**|**18**|**24**|
|Melipilla|0,12|0,21|0,35|0,47|0,55|0,63|0,68|0,75|<br>0,88|1,00|

_Fuente: Tabla 3.702.403.A del Manual de Carreteras (MOP, 2020)_

_Tabla 3-8: Coeficientes de frecuencia_

|Estación<br>Pluviométrica|Período de retorno [años]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Estación**<br>**Pluviométrica**|**2 **|**5 **|**10**|**20**|**25**|**50**|**100**|**200**|
|Melipilla|0,53|0,81|1,00|1,18|1,24|1,41|1,59|1,76|

_Fuente: Manual de Carreteras Tabla 3.702.403.B_

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 24
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

Con la siguiente ecuación se puede determinar la intensidad máxima de diseño para un período de

retorno de 10 años:

T

T = [P] [t]

I t

**Ecuación 3.1**
t

Donde:

T = K⋅CD t ⋅CF T ⋅P 2410

P t

10

24 **Ecuación 3.2**

I tT : Intensidad con período de retorno T y duración de t horas (mm/h).

P tT : Precipitación con período de retorno T y duración de t horas (mm).

t: Duración de la lluvia (hora).

CD t : Coeficiente de duración para t horas (Tabla 3-7).

CF T : Coeficiente de frecuencia para T años de período de retorno (Tabla 3-8).

P 2410 : Precipitación diaria (de 8 AM a 8 AM) con 10 años de período de retorno obtenida de la estación

pluviométrica (mm).

K: Coeficiente de correlación para la lluvia máxima P 2410 respecto a las 24 horas más lluviosas de la

tormenta (valor adoptado 1,1).

Por lo tanto, para la estación Cerrillos de Leyda se tiene P 2410 =112,5 (mm).

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 25
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

En la Tabla 3-9 se presenta el tiempo de concentración (Tc) adoptado para cada una de las cuencas

aportantes a la zona de estudio (ver Anexo D para las fórmulas aplicadas en cada método).

_Tabla 3-9: Tiempo de concentración de las subcuencas aportantes_

|Nombre|Área<br>[km2]|Hi<br>[m]*|Tc (Hr)|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Nombre**|**Área**<br>**[km2] **|**Hi**<br>**[m]***|**California**<br>**Culverts Practice**<br>**(1942)**|**Giandotti**|**Norma**<br>**Española**|**Kirpich**|**Adoptado**|
|SUBCUENCA CAP-1|0,14|177,59|0,09|0,86|0,23|0,10|0,86|
|SUBCUENCA CAP-2|0,19|184,23|0,15|0,86|0,35|0,14|0,86|
|SUBCUENCA CAP-3|0,11|180,82|0,08|0,70|0,24|0,10|0,70|
|SUBCUENCA CAP-4|0,17|187,56|0,12|0,72|0,32|0,13|0,72|
|SUBCUENCA CAP-5|0,10|189,17|0,09|0,54|0,26|0,10|0,54|
|SUBCUENCA CAP-6|0,14|191,03|0,07|0,55|0,21|0,00|0,55|
|SUBCUENCA CAP-7|0,12|192,99|34,0|0,08|0,59|0,23|0,09|
|SUBCUENCA CAP-E1|12,88|249,45|415,0|0,89|3,49|1,87|0,83|
|SUBCUENCA CAP-E2|0,08|172,11|10,0|0,09|1,08|0,21|0,10|
|SUBCUENCA CAP-E3|9,23|258,22|409,0|0,94|3,07|1,92|0,77|
|SUBCUENCA CAP-E4|0,68|195,41|92,0|0,32|1,45|0,73|0,33|
|SUBCUENCA CAP-E5|0,53|190,48|72,0|0,19|1,21|0,48|0,20|
|SUBCUENCA CAP-E6|0,20|194,19|0,14|0,74|0,38|0,15|0,74|
|SUBCUENCA CAP-E7|0,51|215,67|0,16|0,80|0,42|0,15|0,80|
|SUBCUENCA CAP-E8|0,10|201,54|0,06|0,40|0,19|0,06|0,40|
|SUBCUENCA CAP-E9|0,15|192,24|0,06|0,55|0,21|0,08|0,55|
|SUBCUENCA CAP-E10|0,11|178,94|0,04|0,59|0,15|0,07|0,59|
|SUBCUENCA CAP-E11|0,07|197,80|0,02|0,51|0,09|0,04|0,51|
|SUBCUENCA CAP-E12|0,20|194,21|0,11|1,01|0,29|0,13|1,01|
|SUBCUENCA CAP-E13|0,07|174,12|0,10|0,64|0,23|0,08|0,64|

- Hi: Altitud media de la cuenca aportante.

_Fuente: Elaboración propia a partir del Manual de Carreteras (MOP, 2020 -Tabla 3.702.501.A) y DGA (1995)._

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 26
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

En la Tabla 3-10 se presentan los resultados de intensidades de diseño (i) obtenidas para cada una

de las cuencas aportantes al proyecto.

_Tabla 3-10: Resumen de resultados de intensidades de diseño: zona de paneles_

|Nombre|Área [km2]|Hi [m]*|Tc (hr)<br>Adoptado|IT<br>24<br>[mm/hr]|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Nombre**|**Área [km2]**|**Hi [m]***|**Tc (hr)**<br>**Adoptado**|**T=2**|**T=5**|**T=10**|**T=20**|**T=50**|**T=100**|
|SUBCUENCA CAP-1|0,14|177,59|0,86|7,4|11,3|13,9|16,4|19,6|22,1|
|SUBCUENCA CAP-2|0,19|184,23|0,86|7,4|11,3|13,9|16,4|19,6|22,1|
|SUBCUENCA CAP-3|0,11|180,82|0,70|8,1|12,4|15,4|18,1|21,7|24,4|
|SUBCUENCA CAP-4|0,17|187,56|0,72|8,0|12,2|17,8|17,8|21,3|24,0|
|SUBCUENCA CAP-5|0,10|189,17|0,54|8,9|13,6|16,8|19,9|23,7|26,8|
|SUBCUENCA CAP-6|0,14|191,03|0,55|8,8|13,5|16,6|19,6|23,5|26,4|
|SUBCUENCA CAP-7|0,12|192,99|0,09|8,5|13,0|16,1|19,0|22,7|25,6|
|SUBCUENCA CAP-E1|12,88|249,45|0,83|5,2|7,9|9,8|11,5|13,8|15,5|
|SUBCUENCA CAP-E2|0,08|172,11|0,10|6,6|10,1|12,5|14,8|17,6|19,9|
|SUBCUENCA CAP-E3|9,23|258,22|0,77|5,3|8,1|11,8|11,8|14,2|16,0|
|SUBCUENCA CAP-E4|0,68|195,41|0,33|6,4|9,7|12,0|14,2|16,9|19,1|
|SUBCUENCA CAP-E5|0,53|190,48|0,20|6,5|9,9|12,3|14,5|17,3|19,5|
|SUBCUENCA CAP-E6|0,20|194,19|0,74|8,0|12,2|15,0|17,7|21,2|23,9|
|SUBCUENCA CAP-E7|0,51|215,67|0,80|7,7|11,8|14,6|17,2|20,6|23,2|
|SUBCUENCA CAP-E8|0,10|201,54|0,40|11,2|17,1|21,1|24,9|29,8|33,6|
|SUBCUENCA CAP-E9|0,15|192,24|0,55|8,8|13,5|19,6|19,6|23,5|26,4|
|SUBCUENCA CAP-E10|0,11|178,94|0,59|8,5|13,0|16,1|19,0|22,7|25,6|
|SUBCUENCA CAP-E11|0,07|197,80|0,51|9,4|14,3|17,7|20,8|24,9|28,1|
|SUBCUENCA CAP-E12|0,20|194,21|1,01|6,8|10,3|12,8|15,1|18,0|20,3|
|SUBCUENCA CAP-E13|0,07|174,12|0,64|8,1|12,3|15,2|18,0|21,5|24,2|

*Hi: Altitud media de la cuenca aportante.

**: Este evento es mayor que el T= 100 años.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 27
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

A partir de lo anterior se trazaron las curvas IDF, las cuales se presentan en la Figura 3-13 para una

duración de 24 horas y en la Figura 3-14 se presentan las curvas IDF para duraciones menores a 1

hora.

_Figura 3-13. Curvas IDF Estación Cerrillos de Leyda (duración 24 horas)_

_Figura 3-14. Curvas IDF Estación Cerrillos de Leyda (duraciones menores a 1 hora)_

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 28
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_3.7.2._ _Estimación de crecidas_

Dado que las cuencas aportantes al Proyecto Fotovoltaico Leyda se encuentran en cuencas sin

control fluviométrico, los caudales líquidos se han estimado tomando en cuenta la “precipitación e
intensidad de diseño” y la utilización del Método Racional aplicable a cuencas menores de 25 km [2] .

Dicho método se explica de forma detallada en el Anexo D y en el “Manual de Carreteras Vol. N°3

(MOP, 2020). Dicho método ha sido utilizado de acuerdo con las características de la cuenca (área,

pendiente, altitud, etc.) determinados en el punto 3.6. Además, para la obtención de los caudales

de diseño se han obtenido el tiempo de concentración (Tc) e intensidad de la precipitación de diseño

(i) sobre las cuencas de interés. En la Tabla 3-11, Tabla 3-12 y Tabla 3-13 se presentan los

coeficientes de escorrentías adoptados a partir de lo indicado en la metodología del Anexo D.

_Tabla 3-11: Coeficientes de escorrentía adoptados para las subcuencas aportantes_

|Parámetro|SUBCUENCA<br>CAP-1|SUBCUENCA<br>CAP-2|SUBCUENCA<br>CAP-3|SUBCUENCA<br>CAP-4|SUBCUENCA<br>CAP-5|SUBCUENCA<br>CAP-6|SUBCUENCA<br>CAP-7|
|---|---|---|---|---|---|---|---|
|Relieve|0,15|0,16|0,15|0,17|0,18|0,19|0,18|
|Infiltración|0,10|0,06|0,06|0,06|0,06|0,06|0,10|
|Cobertura vegetal|0,07|0,12|0,12|0,12|0,12|0,12|0,07|
|Almacenamiento superficial|0,10|0,08|0,08|0,08|0,08|0,08|0,10|
|**C (T= 10 años)**|**0,42**|**0,42**|**0,41**|**0,43**|**0,44**|**0,45**|**0,45**|
|C (T= 2 años)|0,35|0,35|0,34|0,35|0,36|0,37|0,37|
|C (T= 5 años)|0,39|0,39|0,38|0,40|0,41|0,42|0,42|
|C (T= 20 años)|0,45|0,45|0,44|0,43|0,44|0,49|0,49|
|C (T= 25 años)|0,46|0,46|0,45|0,46|0,48|0,50|0,50|
|C (T= 50 años)|0,50|0,50|0,49|0,47|0,48|0,54|0,54|
|C (T= 100 años)|0,53|0,53|0,51|0,52|0,53|0,56|0,56|

_Fuente: Elaboración propia a partir del Manual de Carreteras (MOP, 2020)._

_Tabla 3-12: Coeficientes de escorrentía adoptados para las subcuencas aportantes (continuación)_

|Parámetro|SUBCUENCA<br>CAP-E1|SUBCUENCA<br>CAP-E2|SUBCUENCA<br>CAP-E3|SUBCUENCA<br>CAP-E4|SUBCUENCA<br>CAP-E5|SUBCUENCA<br>CAP-E6|SUBCUENCA<br>CAP-E7|
|---|---|---|---|---|---|---|---|
|Relieve|0,23|0,13|0,23|0,19|0,20|0,20|0,23|
|Infiltración|0,06|0,06|0,06|0,06|0,06|0,10|0,06|
|Cobertura vegetal|0,12|0,12|0,12|0,12|0,12|0,07|0,12|
|Almacenamiento superficial|0,08|0,08|0,08|0,08|0,08|0,10|0,08|
|**C (T= 10 años)**|**0,49**|**0,39**|**0,49**|**0,45**|**0,46**|**0,47**|**0,49**|
|C (T= 2 años)|0,40|0,32|0,40|0,37|0,38|0,39|0,40|
|C (T= 5 años)|0,45|0,36|0,45|0,42|0,43|0,43|0,45|
|C (T= 20 años)|0,53|0,42|0,49|0,45|0,50|0,51|0,53|
|C (T= 25 años)|0,54|0,43|0,53|0,49|0,51|0,52|0,54|
|C (T= 50 años)|0,59|0,47|0,54|0,50|0,55|0,56|0,59|
|C (T= 100 años)|0,61|0,49|0,59|0,54|0,58|0,59|0,61|

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 29
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Tabla 3-13: Coeficientes de escorrentía adoptados para las subcuencas aportantes (continuación)_

|Parámetro|SUBCUENCA<br>CAP-E8|SUBCUENCA<br>CAP-E9|SUBCUENCA<br>CAP-E10|SUBCUENCA<br>CAP-E11|SUBCUENCA<br>CAP-E12|SUBCUENCA<br>CAP-E13|
|---|---|---|---|---|---|---|
|Relieve|0,24|0,22|0,16|0,18|0,18|0,18|
|Infiltración|0,06|0,06|0,06|0,10|0,06|0,10|
|Cobertura vegetal|0,12|0,12|0,12|0,07|0,12|0,07|
|Almacenamiento superficial|0,08|0,08|0,08|0,10|0,08|0,10|
|**C (T= 10 años)**|**0,50**|**0,48**|**0,42**|**0,45**|**0,44**|**0,45**|
|C (T= 2 años)|0,41|0,39|0,35|0,37|0,36|0,37|
|C (T= 5 años)|0,46|0,44|0,39|0,42|0,41|0,42|
|C (T= 20 años)|0,54|0,48|0,42|0,49|0,48|0,49|
|C (T= 25 años)|0,55|0,52|0,45|0,50|0,48|0,50|
|C (T= 50 años)|0,60|0,53|0,46|0,54|0,53|0,54|
|C (T= 100 años)|0,63|0,58|0,50|0,56|0,55|0,56|

En base a lo anterior, en la Tabla 3-14 se presentan los caudales máximos obtenidos para las cuencas

aportantes a la zona de estudio (zonas de panes y LAT) para distintos periodos de retorno, donde se

ha utilizado el Método Racional para el caso de las cuencas aportantes <25 km2.

_Tabla 3-14: Resumen de resultados de caudales líquidos máximos estimados para las cuencas aportantes_

|Nombre|Área [km2]|Altitud (m)|Método Racional|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Nombre**|**Área [km2]**|**Altitud (m)**|**T=2**|**T=5**|**T=10**|**T=20**|**T=50**|**T=100**|
|SUBCUENCA CAP-1|0,14|177,59|0,10|0,17|0,22|0,28|0,38|0,44|
|SUBCUENCA CAP-2|0,19|184,23|0,13|0,23|0,30|0,39|0,52|0,61|
|SUBCUENCA CAP-3|0,11|180,82|0,09|0,15|0,20|0,26|0,34|0,40|
|SUBCUENCA CAP-4|0,17|187,56|0,13|0,23|0,36|0,39|0,52|0,61|
|SUBCUENCA CAP-5|0,10|189,17|0,09|0,16|0,21|0,27|0,35|0,41|
|SUBCUENCA CAP-6|0,14|191,03|0,13|0,22|0,30|0,38|0,51|0,60|
|SUBCUENCA CAP-7|0,12|192,99|0,11|0,18|0,25|0,31|0,42|0,49|
|SUBCUENCA CAP-E1|12,88|249,45|7,46|12,82|17,12|21,81|28,96|34,02|
|SUBCUENCA CAP-E2|0,08|172,11|0,05|0,08|0,11|0,13|0,18|0,21|
|SUBCUENCA CAP-E3|9,23|258,22|5,49|9,44|14,88|16,07|21,34|25,06|
|SUBCUENCA CAP-E4|0,68|195,41|0,44|0,76|1,01|1,29|1,71|2,01|
|SUBCUENCA CAP-E5|0,53|190,48|0,36|0,62|0,83|1,06|1,41|1,65|
|SUBCUENCA CAP-E6|0,20|194,19|0,17|0,29|0,39|0,49|0,65|0,77|
|SUBCUENCA CAP-E7|0,51|215,67|0,44|0,75|1,00|1,28|1,70|1,99|
|SUBCUENCA CAP-E8|0,10|201,54|0,13|0,22|0,29|0,37|0,49|0,58|
|SUBCUENCA CAP-E9|0,15|192,24|0,15|0,25|0,40|0,43|0,57|0,67|
|SUBCUENCA CAP-E10|0,11|178,94|0,09|0,15|0,21|0,26|0,35|0,41|
|SUBCUENCA CAP-E11|0,07|197,80|0,07|0,12|0,16|0,21|0,28|0,33|
|SUBCUENCA CAP-E12|0,20|194,21|0,14|0,23|0,31|0,40|0,53|0,62|
|SUBCUENCA CAP-E13|0,07|174,12|0,06|0,10|0,14|0,17|0,23|0,27|

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 30
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

#### 4. CARACTERIZACIÓN HIDRÁULICA

Se realiza el presente estudio hidráulico dada la eventual existencia de cauces en que las crecidas

puedan afectar potencialmente el funcionamiento de las instalaciones del Parque Fotovoltaico

incorporando la crecida del Embalse Leyda. El objetivo de evaluar el riesgo de inundación

considerando un período de retorno de 100 años tomando especial atención a las instalaciones,

paneles, cruces con caminos y vallado.

Como existe una topografía de detalle en el parque se ha optado por una modelación bidimensional

para el análisis del comportamiento de los flujos de crecida. Dada la cantidad de entradas de agua

del terreno, este análisis bidimensional permitirá determinar la extensión de la inundabilidad con

más realismo que con un modelo unidimensional.

##### 4.1. Alcance

Se dispone de una topografía de detalle en el terreno donde será emplazado el parque fotovoltaico,

ampliada al menos 100 metros aguas arriba en el punto definido por la autoridad, 100 metros aguas

abajo del muro del embalse y en zonas de inundación. Para el presente estudio de inundabilidad se

construyó un Modelo Digital de Elevaciones (MDE), cuyos límites perimetrales (Figura 4-1) definen

el alcance de la modelización hidráulica.

La modelización de detalle del presente estudio se realiza tanto para la situación topográfica actual

de terreno como para la situación futura.

La modelación hidráulica (o estudio de inundación) se realizó para una crecida de periodo de retorno

de 100 años, con una extensión de al menos 100 m aguas arriba a las coordenadas UTM Datum

WGS84 (huso 19) Norte: 6.276.963 m y Este: 270.591 (PUNTO AUTORIDAD) y 100 m aguas abajo del

muro del Embalse Leyda.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 31
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 4-1. Alcance del estudio de inundabilidad en parque._

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 32
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

##### 4.2. Metodología de simulación hidráulica

_4.2.1._ _Modelización bidimensional del flujo de agua_

La modelización matemática bidimensional del flujo de agua consiste en predecir los valores que

toman las variables hidráulicas (velocidad, calado, caudal, etc.) a partir de la resolución mediante

métodos numéricos de ecuaciones considerando una serie de hipótesis.

La observación de que en la realidad se encuentran muchas situaciones donde el flujo parece ser

efectivamente bidimensional (es decir, predominan las dimensiones horizontales sobre la vertical)

o donde el fenómeno es complejo y es difícil definir a priori los cauces preferentes han llevado al

uso de ecuaciones y esquemas bidimensionales, aprovechando la creciente capacidad y velocidad

de los computadores modernos.

Existe una variedad de herramientas para la resolución del flujo de agua en lámina libre en 2

dimensiones. Algunas de las más consolidadas como Mike-21, Sobek o Tublow2D utilizan esquemas

en diferencias finitas, con sus limitaciones propias asociadas a la flexibilidad de la malla y en el

cálculo de soluciones con discontinuidades. Otros como Telemac2D, SMS y FLO-2D utilizan

elementos finitos que tiene mayor flexibilidad con arreglos de mallas no estructuradas.

En la actualidad la tendencia decanta hacia la metodología de los volúmenes finitos, aprovechando

importantes desarrollos que ha habido en las últimas décadas con este tipo de esquemas para las

ecuaciones de aguas someras. Algunas herramientas disponibles y que utilizan volúmenes finitos

son Infoworks, Guad2D, OpenFOAM, Iber, las últimas versiones de Mike-21 y HEC-RAS 2D.

En el presente estudio se ha utilizado la versión 2.6 del programa de modelización hidráulica

bidimensional Iber.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 33
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_4.2.2._ _Fundamentos de cálculo del modelo bidimensional Iber_

Iber es un modelo matemático bidimensional para la simulación de flujo en ríos y estuarios
desarrollado a partir de la colaboración del Grupo de Ingeniería del Agua y del Medio Ambiente,
GEAMA (Universidade da Coruña), Grupo de Ingeniería Matemática (Universidad Santiago de
Compostela), Instituto Flumen (Universitat Politècnica de Catalunya y Centro Internacional de
Métodos Numéricos en Ingeniería CIMNE), promovido por el Centro de Estudios Hidrográficos del
CEDEX y la Dirección General del Agua de España.

Este modelo numérico se desarrolló directamente desde la administración pública española en
colaboración con las universidades y centros de investigación mencionados, diseñado
especialmente para resolver las necesidades técnicas específicas en estudios hidrológicos e
hidráulicos. Algunas de las aplicaciones actuales de Iber son:

 Simulación del flujo en lámina libre en cauces naturales

 - Evaluación de zonas inundables

 - Cálculo hidráulico de canalizaciones

 - Cálculo hidráulico de redes de canales en lámina libre

 - Cálculo de corrientes en estuarios

 Proceso de erosión y sedimentación por transporte de material granular

 - Cálculo de modelos turbulentos

 Modelación distribuida hidrológica

 Eco-hidráulica y modelos de hábitat de peces

 Calidad de aguas y transporte de contaminantes

Iber se desarrolló a partir de 2 herramientas de modelación numérica bidimensional ya existentes:
Turbillón y CARPA, ambas con métodos de volúmenes finitos, que fueron integrados en un único
código ampliado con nuevas capacidades. Iber integra de diferentes módulos de cálculos acoplados
entre sí para resolver las aplicaciones mencionadas.

_[Figura 4-2. Interrelación entre módulos de cálculo en Iber. Fuente: https://www.iberaula.es/](https://www.iberaula.es/)_

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 34
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_4.2.3._ _Ecuaciones_

El módulo hidrodinámico de Iber resuelve las ecuaciones de St. Venant bidimensionales,

incorporando opcionalmente los efectos de la turbulencia y rozamiento superficial por el viento:

∂h

∂h

∂t [+ ∂hU] ∂x [x]

[x] + [∂hU] [y]

∂x

= 0
∂y

[∂]

∂x [(hU] [x2] [ + gh] 2 [2]

∂ [∂]
∂t [(hU] [x] [) +]

[2] [∂]

2 [) +]

[∂]

∂y [(hU] [x] [U] [y] [) = −gh∂Z] ∂x [b]

[b]

∂x [+ τ] [s,x]

[s,x]

ρ [−τ] [b,x] ρ

[x] [∂]

∂x ~~[)]~~ [ +]

[∂]

∂y [(v] [t] [h∂U] ∂y [x]

[x]

∂y [)]

[b,x] [∂]

ρ [+]

[∂]

∂x [(v] [t] [h∂U] ∂x [x]

[b]

∂y [+ τ] ρ [s,][y]

[s,][y]

ρ [−τ] [b,] ρ [y]

[2]

2 ~~[)]~~ [ = −gh∂Z] ∂y [b]

[∂]

∂y [(v] [t] [h∂U] ∂y [y]

[y]

∂y ~~[)]~~

∂ [∂]
∂t [(hU] [y] [) +] ∂x

[∂] [∂]

∂x [(hU] [x] [U] [y] [) +]

2

[∂]

∂y [(hU] [y]

2 + g [h] [2]

[y] [∂]

∂x ~~[)]~~ [ +]

[b,][y] [∂]

ρ [+] ∂x

[∂]

∂x [(v] [t] [h∂U] ∂x [y]

En donde h es el calado, U x, U y son las velocidades horizontales promediadas en profundidad, g es
la aceleración de gravedad, ρ es la densidad del agua, Z b es la cota de fondo, τ s es la fricción en la
superficie libre debida al rozamiento producido por el viento, τ b es la fricción debida al rozamiento
del fondo y v t es la viscosidad turbulenta. La fricción de fondo se evalúa mediante la fórmula de

Manning como:

τ b,x = ρhg [n] [2] [U] h [4/3][x] [|U|] [2]

τ b,y = ρhg [n] [2] [U] h [4/3][y] [|U|] [2]

Todas las funciones y parámetros que aparecen en las ecuaciones hidrodinámicas (incluyendo

coeficiente de Manning y velocidad del viento) pueden imponerse de forma variable, tanto espacial

como temporalmente. En este estudio no se ha considerado el efecto del viento ni la turbulencia en

el flujo de agua.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 35
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_4.2.4._ _Esquemas numéricos y malla de cálculo_

Las ecuaciones de aguas someras y las del modelo k-εse resuelven mediante el método de

volúmenes finitos para mallas bidimensionales no estructuradas. Los esquemas numéricos

utilizados en Iber son especialmente apropiados para la modelización de cambios de régimen y de

frentes seco-mojado (frentes de inundación). La discretización del dominio espacial se realiza con

volúmenes finitos en mallas no estructuradas, admitiéndose estas mixtas formadas por elementos

triangulares y cuadrangulares. El flujo convectivo se discretiza mediante esquemas descentrados de

tipo Godunov. El término que incluye la pendiente del fondo se discretiza de forma descentrada con

el fin de evitar oscilaciones espurias de la lámina libre cuando se trabaja con terrenos complejos. El

resto de los términos, incluidos los de difusión turbulenta, se discretizan con un esquema centrado.

Uno de los procesos que requieren mayor tiempo y esfuerzo a la hora de desarrollar un estudio de

simulación numérica del flujo en ríos es la generación de la malla de cálculo. Un río tiene una

geometría irregular y la construcción de una malla eficiente no es evidente. Es deseable que la malla

sea irregular, con el fin de minimizar el número de elementos con transiciones suaves. Para ello son

muy adecuados los métodos de mallado basados en el error cordal (máxima distancia entre el

terreno original y la malla). Por ello Iber incorpora capacidades de mallado como la creación de

mallas estructuradas y no estructuradas, de triángulos y de cuadriláteros, mediante el uso de

diversos algoritmos de mallado. Adicionalmente se han desarrollado herramientas de creación y

edición de mallas que se adaptan a las necesidades de los estudios de hidráulica fluvial.

_Figura 4-3. Ejemplo de edición de nodos de una malla._

_Fuente: E. Blandé et al. (2012)_

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 36
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_4.2.5._ _Condiciones de contorno_

Iber distingue entre contornos cerrados (tipo pared) y contornos abiertos por los cuales entra y sale

el agua del dominio de cálculo. En los contornos cerrados se puede imponer o una condición de

deslizamiento libre o una condición de fricción de pared. Con la condición de deslizamiento libre se

desprecia el rozamiento generado por los contornos sobre el fluido. Si se considera relevante el

efecto del rozamiento generado por el contorno se debe utilizar una condición de contorno tipo

fricción. La velocidad tangencial a la pared puede expresarse como una función de la velocidad de

fricción de pared (u*) y de la distancia a la pared como:

[u] [∗]

0,4 [Ln(Edu] v [∗]

|U| = [u] [∗]

v ~~[)]~~

Donde d es la distancia en perpendicular a la pared y E es un parámetro cuyo valor depende de las

características del flujo. Para el cálculo de E se consideran condiciones de flujo turbulento liso,

turbulento rugoso, y transición entre turbulento liso y rugoso.

Respecto a los contornos abiertos, se consideran diferentes alternativas en función del régimen

hidráulico en el contorno. En los contornos de entrada se fija el caudal de agua y se asume que la

dirección del flujo es perpendicular al contorno. En caso de que el flujo entre en régimen

supercrítico, se impone adicionalmente el calado. La distribución del caudal unitario a lo largo del

contorno se realiza de forma proporcional al calado en cada punto del mismo, según la expresión
q n = Ch [5/3], donde C es una constante que asegura que la integral del caudal unitario q n a lo largo
del contorno considerado es igual al caudal total de entrada. En los contornos de salida se impone

el nivel de la lámina de agua en caso de que se produzca un régimen subcrítico, mientras que no es

necesario imponer ninguna condición en el caso de que el régimen sea supercrítico. En los contornos

de salida se considera asimismo la posibilidad de introducir una relación de curva de gasto que

defina la relación entre la cota de la lámina de agua y el caudal específico desaguado en cada punto

del contorno.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 37
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_4.2.6._ _Parámetros de entrada del modelo bidimensional de flujo_

_4.2.6.1._ _Modelo Digital de Terreno_

A partir de la topografía de detalle disponible en la zona de estudio y aquella levantada por INRHED

& GEOMAG (2021) se ha generado un Modelo Digital de Terreno (MDT) de la situación topográfica

sobre la cual se trabajó (Figura 4-4), esta situación se ha ampliado, comprendiendo al menos 100

metros aguas arriba del punto definido por la autoridad, 100 metros aguas abajo del muro del

embalse y en áreas de inundación del embalse, permitiendo generar una correcta modelación

hidráulica. Con esto es posible construir la malla geométrica de cálculo del modelo hidráulico.

_Figura 4-4. MDT en parque._

_4.2.6.2._ _Rugosidad del terreno_

Para el análisis hidráulico, es necesario caracterizar la rugosidad de las superficies mediante el

coeficiente de Manning como antecedente para el modelo hidráulico, parámetro que representa la

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 38
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

resistencia que ejerce la superficie al escurrimiento del agua, y que se relaciona con el caudal, la

pendiente y geometría del cauce, según la Ecuación 4.1.

v= [Q]

[Q]

A [ = 1] n

n [ × R]

2 3⁄ × i

1 2⁄ **Ecuación 4.1**

Dónde:

v : velocidad media de la sección transversal de escurrimiento en el canal (m/s)

Q : caudal en el canal (m [3] /s)

A : área sección transversal de la corriente (m [2] )

n : coeficiente de rugosidad de Manning

R : radio hidráulico (área/perímetro mojado) (m)

i : pendiente en uno por uno (m/m)

El coeficiente de rugosidad de Manning del cauce natural se determinó utilizando la Tabla 3.705.1.A

del Manual de Carreteras (MOP, 2018), el libro “Hidráulica de Canales Abiertos”, Ven Te Chow

(1994); la fórmula de Cowan y también considerando las características morfológicas de los cauces

observadas en terreno.

Cowan (1956) desarrolló un procedimiento para estimar el valor del coeficiente de Manning, el cual

queda definido por la siguiente ecuación:

n= m∙(n 0 + n 1 + n 2 + n 3 + n 4 ) **Ecuación 4.2**

Dónde:

n : Coeficiente de rugosidad de Manning

n 0 : Rugosidad base para un canal recto, uniforme, prismático y con rugosidad homogénea

n 1 : Rugosidad adicional debida a irregularidades superficiales del perímetro mojado a lo largo del

tramo en estudio

n 2 : Rugosidad adicional equivalente debida a variación de forma y de dimensiones de las secciones

a lo largo del tramo en estudio

n 3 : Rugosidad adicional equivalente debida a obstrucciones existentes en el cauce

n 4 : Rugosidad adicional equivalente debida a la presencia de vegetación

m : Factor de corrección para incorporar efecto de sinuosidad del cauce o presencia de meandros

En la Tabla 4-1 se presentan los valores de los parámetros que intervienen en la fórmula de Cowan.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 39
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Tabla 4-1. Valores para el Cálculo del Coeficiente de Manning Mediante Método de Cowan._

|Condiciones del Canal|Col2|Valor|Col4|
|---|---|---|---|
|Material del Lecho|Tierra|n0|0,020|
|Material del Lecho|Roca Cortada|Roca Cortada|0,025|
|Material del Lecho|Grava Fina|Grava Fina|0,024|
|Material del Lecho|Grava Gruesa|Grava Gruesa|0,028|
|Grado de Irregularidad Perímetro<br>Mojado|Despreciable|n1|0,000|
|Grado de Irregularidad Perímetro<br>Mojado|Leve|Leve|0,005|
|Grado de Irregularidad Perímetro<br>Mojado|Moderado|Moderado|0,010|
|Grado de Irregularidad Perímetro<br>Mojado|Alto|Alto|0,020|
|Variaciones de las Secciones|Graduales|n2|0,000|
|Variaciones de las Secciones|Alternándose Ocasionalmente|Alternándose Ocasionalmente|0,005|
|Variaciones de las Secciones|Alternándose Frecuentemente|Alternándose Frecuentemente|0,010 - 0,015|
|Efecto<br>Relativo<br>de<br>las<br>Obstrucciones|Despreciable|n3|0,000|
|Efecto<br>Relativo<br>de<br>las<br>Obstrucciones|Leve|Leve|0,010 - 0,015|
|Efecto<br>Relativo<br>de<br>las<br>Obstrucciones|Apreciable|Apreciable|0,020 - 0,030|
|Efecto<br>Relativo<br>de<br>las<br>Obstrucciones|Alto|Alto|0,040 - 0,060|
|Densidad de Vegetación|Baja|n4|0,005 - 0,010|
|Densidad de Vegetación|Media|Media|0,010 - 0,025|
|Densidad de Vegetación|Alta|Alta|0,025 - 0,050|
|Densidad de Vegetación|Muy alta|Muy alta|0,050 - 0,100|
|Sinuosidad<br>y <br>Frecuencia<br>de<br>Meandros|Leve|m|1,000|
|Sinuosidad<br>y <br>Frecuencia<br>de<br>Meandros|Apreciable|Apreciable|1,150|
|Sinuosidad<br>y <br>Frecuencia<br>de<br>Meandros|Alto|Alto|1,300|

_Fuente: Manual de Carreteras (MOP, 2018)._

En cauces naturales constituidos por lechos pedregosos, donde el sedimento es caracterizable por

un diámetro medio o representativo, se emplea la fórmula de Strickler para estimar n 0, si el régimen

es hidrodinámicamente rugoso:

n 0 = 0.038 D [1/6] **Ecuación 4.3**

Dónde:

n 0 : Rugosidad base

D: Diámetro representativo de la rugosidad superficial (m)

En cauces naturales pedregosos, este diámetro representativo de la rugosidad se asimila al diámetro

D 65, D 90 o D 95 dependiendo de la tendencia al acorazamiento del lecho. En particular, cuando los

sedimentos son de granulometría gruesa y extendida, el diámetro medio de la coraza es cercano al

D 90 o D 95 obtenido de la curva granulométrica original del lecho.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 40
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

En la Figura 4-5 se presenta la ubicación de la calicata realizadas, cuyas coordenadas se presentan

en la Tabla 4-2.

_Figura 4-5. Ubicación Calicatas Puntos P1 y P9 realizadas en la zona de proyecto_

_Tabla 4-2. Resumen coordenada y profundidad de las calicatas_

|Calicata|Coordenadas UTM WGS 84|Col3|Profundiad<br>prospectada (m)|Fecha de<br>prospección|
|---|---|---|---|---|
|**Calicata**|**UTM E (m)**|**UTM N (m)**|**UTM N (m)**|**UTM N (m)**|
|C-1|270.244|6.227.098|3.0|7/12/2020|
|C-2|269.100|6.227.478|3.0|7/12/2020|
|C-3|268.953|6.227.547|3.0|7/12/2020|

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 41
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 4-6. Calicatas y sus granulometrías asociadas._

En la visita a terreno del día 7 de diciembre de 2020 a la zona de estudio se pudieron apreciar las

características de los lechos de los cauces principales y de las riberas o bordes. Además, se evidenció

que el terreno algunos cauces bien marcados y la clara influencia de los afluentes al Embalse Leyda.

Los resultados de laboratorio (ONEGEOTECNIA, 2020) muestran que los suelos corresponden

básicamente a estratos arcillosos y areno arcillosos. Según la clasificación USCS, C-1 corresponde a

una arena arcillosa (SC) mientras que C-2 y C-3 corresponden a arcilla de baja plasticidad (CL).

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 42
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

Basado en lo anterior, se obtienen los valores de coeficientes de la Tabla 4-3 que permitirán modelar

la situación del eje hidráulico.

_Tabla 4-3._ _Coeficientes de Manning según fórmula de Cowan_

|Variable|Cauces principales|Riberas|
|---|---|---|
|n0|0,021|0,010|
|n1|0,007|0,007|
|n2|0,003|0,003|
|n3|0,015|0,015|
|n4|0,002|0,007|
|m|1,0|1,0|
|n|**0,035**|**0,040**|

Realizando el cálculo, se obtiene un coeficiente de rugosidad de Manning (n) para los cauces

principales de 0,035 y para las riberas de 0,040.

_4.2.6.3._ _Malla de cálculo_

Se ha definido un mallado no estructurado de tipo triangular para el cálculo hidráulico utilizando las

herramientas disponibles en Iber 2.5 en conjunto con los MDT generados anteriormente. Se ha

realizado un mallado de 5 m para el área del parque. En la Figura 4-7 se muestra la malla de cálculo

no estructurada utilizada.

_Figura 4-7. Malla no estructurada utilizada en Parque._

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 43
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_4.2.6.4._ _Condiciones hidrodinámicas_

Como condición de contorno aguas arriba para ambas simulaciones, se ha aplicado en régimen
crítico/subcrítico para todos los cauces considerados un hidrograma constante, con caudales

máximos de crecida para T = 100 años obtenidos en el cálculo hidrológico. Esta consideración

aplicando un tiempo de simulación suficiente para que el flujo en el modelo se estabilice, es decir

que el caudal que entra es igual al que sale, quedando del lado de la seguridad en los resultados

obtenidos.

En el estudio hidrológico del presente proyecto se puede comprobar que el caudal total simulado
es de 72,15 m [3] /s . Este aporte se produce a través de 20 entradas (Ver Tabla 4-4) fluviales como se
muestra en la Figura 4-8.

_Figura 4-8. Localización de las condiciones de contorno de entrada para modelo Iber en parque._

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 44
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Tabla 4-4. Caudales y cuenca de captación asociada a cada entrada_

|Entrada|Caudal (m3/s)|CAP|
|---|---|---|
|INLET-1|0,77|CAP-E6|
|INLET-2|1,65|CAP-E5|
|INLET-3|2,01|CAP-E4|
|INLET-4|25,06|CAP-E3|
|INLET-5|0,21|CAP-E2|
|INLET-6|34,02|CAP-E1|
|INLET-7|0,62|CAP-E12|
|INLET-8|0,49|CAP-7|
|INLET-9|0,6|CAP-6|
|INLET-10|0,41|CAP-5|
|INLET-11|0,33|CAP-E11|
|INLET-12|0,61|CAP-4|
|INLET-13|0,4|CAP-3|
|INLET-14|0,61|CAP-2|
|INLET-15|0,41|CAP-E10|
|INLET-16|0,44|CAP-1|
|INLET-17|0,67|CAP-E9|
|INLET-18|0,58|CAP-E8|
|INLET-19|1,99|CAP-E7|
|INLET-20|0,27|CAP-E13|

En cuanto a las condiciones aguas abajo para ambas simulaciones, estas se han localizado en todos

los límites del MDT susceptibles de ser salida con una condición de régimen subcrítico para no

afectar el resultado final.

_4.2.6.5._ _Condiciones iniciales_

Se ha considerado que el flujo transcurre por un terreno inicialmente seco, asignando valor cero a

las condiciones iniciales 2D. Como límite seco-mojado se define el umbral para considerar

transferencia de caudal entre celdas adyacentes en 1 cm.

_4.2.6.6._ _Opciones de cálculo hidráulico_

Las opciones de cálculo establecidas en Iber para la modelación bidimensional han sido:

 Cálculo con esquema numérico de primer orden.

 Condición de discretización temporal CFL: 0,45

 Tiempo máximo de simulación: 80.000 s (22,22 horas)

 - Intervalo de resultados: 10 s

 Incremento de tiempo máximo: 1s (determinado automáticamente por Iber)

 Método de secado: por defecto

 Resultados a obtener: Calado, velocidad, caudal, cota y mapa de máximos de estos.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 45
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

##### 4.3. Resultados del modelo hidráulico

Se realiza un análisis hidrodinámico bidimensional del comportamiento del flujo de inundación para

T = 100 años en situación sin proyecto y situación con proyecto, tanto para el parque como para su

línea de alta tensión.

Se han definido rangos de velocidades acordes a las condiciones particulares del proyecto, tomando

en cuenta la granulometría, experiencia de este consultor y los criterios entregados por el Manual

de Carreteras V III, 3.705.2 Canales revestidos no erosionables, 3.705.3 Canales revestidos

erosionables y Tabla 3.705.301.A Velocidades y fuerzas tractices máximas permisibles. Estos rangos

consolidados se presentan en la Figura 4-9.

_Figura 4-9. Rangos de velocidades definidos para este Proyecto._

En la Figura 4-10 se presentan 4 capturas de la hidrodinámica modelada en el sistema hidrológico

asociado al Embalse Leyda para distintos instantes de tiempo:

 - En el instante _a_ han transcurrido 270 segundos (4 minutos 30 segundos) de modelado, es

decir en ese momento se está iniciando el funcionamiento del sistema hidrológico, con 19

entradas fluviales que comienzan a llegar a la zona del embalse.

 - En el instante _b_ han transcurrido 1780 segundos (casi 30 minutos) de modelado, en este

punto se han unido todas las entradas fluviales que drenan hacia el embalse, empezando a

trabajar de forma solidaria en el llenado de éste. Por otro lado, los flujos dentro del parque

comienzan a llegar a una condición de estabilidad hidráulica.

 - En el instante _c_ han transcurrido 33.340 segundos (un poco más de 9 horas), se puede ver

como en este momento todas las entradas fluviales hacia el embalse han llenado gran parte

de la capacidad de éste. En este momento el sistema se encuentra en un proceso de

aumento de cota, en particular notar el aumento del nivel en la zona cercana al

emplazamiento del parque. Con respecto a los flujos dentro del parque, estos ya han llegado

a una condición de estabilidad hidráulica.

 - En el instante _d_ han transcurrido 66.500 segundos (18 horas 30 minutos), ya se puede

observar el sobrepaso del muro del Embalse Leyda.

Se observa que exactamente en el segundo 65.220, es decir tras 18 horas de lluvia T = 100 constante

(caso muy conservador) existe sobrepaso en el muro, por lo tanto, se asumirá este instante para

obtener el área máxima de inundación con fines de diseño, luego de esto, el sistema de evacuación

del embalse comienza a trabajar y en consecuencia a liberar agua.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 46
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 4-10. Hidrodinámica de sistema hidrológico. Se muestra la hidráulica de calado en modelación bidimensional (Iber) para 4 pasos de tiempo (a = 270 s., b = 1.780 s., c =_

_33.340 s. y d 66.500 s.)_

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 47
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_4.3.1._ _Situación sin proyecto en zona de emplazamiento del parque_

En la Figura 4-11 y Figura 4-12 se puede observar la lámina de inundación para T = 100 años,

mostrando el tirante de agua y la velocidad de flujo respectivamente, se han incorporado las obras

de drenaje existentes (puentes y alcantarillas) fuera del terreno pero que drenan hacia dentro del

área de inundación del embalse.

Se observa que la mediana de las velocidades es aproximadamente 0,40 m/s, con máximos
superiores a los 2 m/s presentes de forma localizada. Por otro lado, las alturas de escurrimiento

presentan una mediana de aproximadamente 1,6 m dada la influencia del embalse, pero dentro del

parque estas alturas de escurrimiento no superan los 50 cm.

Finalmente, con respecto al cauce que la autoridad definió modelar (Punto Autoridad) se puede ver

que es uno de los principales afluentes de agua hacia el embalse en este sistema hidrológico, y que

casi su totalidad ingresa por el puente ubicado al Sur del parque, mientras que otra parte escurre

longitudinalmente a la Ruta G-904.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 48
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 4-11. Lámina de inundación T = 100, Tirante de agua para situación sin proyecto en parque_

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 49
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 4-12. Lámina de inundación T = 100, Velocidad de flujo para situación sin proyecto en parque_

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 50
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_4.3.2._ _Situación con proyecto en zona de emplazamiento del parque_

En la Figura 4-13 y la Figura 4-14 se puede observar la lámina de inundación para T = 100 años,

mostrando el tirante de agua y la velocidad de flujo respectivamente, se han incorporado ahora las

obras proyectadas (paneles, caminos, vallado perimetral, torres)

Se ha realizado un trabajo iterativo entre la hidráulica de este estudio y la ingeniería del proyecto

para realizar un correcto emplazamiento de todas las obras asociadas al parque. Como resultado se

tiene un _LAYOUT_ que evita por completo todas las áreas de inundación, considerando vallado

perimetral, caminos interiores, postes, paneles y estructuras. Esto trae como resultado el libre

escurrimiento del flujo en su estado natural, no modificando su hidrodinámica, ni tampoco la

cantidad y calidad del agua que fluye desde el interior del parque hacia el embalse, como desde el

embalse hacia cercanías del parque. Es por ello, que no existe modificación ni regularización de

cauce naturales o artificiales.

En consecuencia, se evita el área de inundación máxima del embalse, como también el área de

inundación ocurrida el año 2007 evitando riesgos de inundación dentro del parque. Notar la

similitud del área de inundación del 2007 con la modelación hidráulica, esto lleva a concluir que esa

área es la máxima en la zona.

Finalmente, en el Anexo A se presenta una modelación de la rotura del Embalse Cerrillos de Leyda

(al menos 100 m aguas abajo del muro de dicho embalse), a partir de los resultados obtenidos de

la modelación con proyecto.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 51
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 4-13. Lámina de inundación T = 100, Tirante de agua para situación con proyecto en parque_

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 52
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 4-14. Lámina de inundación T = 100, Velocidad de flujo para situación con proyecto en parque_

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 53
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

#### 5. CONCLUSIONES

 - Las cuencas aportantes al Proyecto PFV Leyda se encuentran en una zona sin control

fluviométrico (es decir, que no existen mediciones de caudales en cauces) por parte de la

Dirección General de Aguas.

 - Los cauces o escurrimientos que se observan en la zona son cárcavas o socavones formados

en la roca intrusiva por la acción del agua. La roca sobre la cual se disponen las obras del

proyecto, está fuertemente meteorizada en superficie, lo que facilita la formación de

cárcavas o socavones producto de escurrimientos superficiales esporádicos asociados a

precipitaciones, los que van labrando la superficie rocosa. Sin embargo, durante la

inspección en terreno, se constató que estos rasgos que componen los cauces del sector, se

encuentran completamente secos y que por ende sólo canalizan el agua cuando hay

precipitaciones suficientes para desarrollar escurrimiento superficial.

 - Se ha analizado la estadística de precipitaciones máximas en 24 horas de las estaciones

meteorológicas DGA próximas a la zona de estudio, ubicadas a distintas alturas geográficas.

 - La función Gumbel fue la que presentó el mejor ajuste estadístico/gráfico para las

estaciones analizadas (Cerrillos De Leyda, Estero Pangue en Ruta 78 y Melipilla).

 - La estación meteorológica Cerrillos de Leyda es la más representativa de la hidrología del

proyecto (zona de paneles y líneas de transmisión), la cual cuenta con una longitud de datos

representativos de 90 años y se ubica a unos 3,4 km al Suroeste del proyecto, a una altitud

de 182 msnm y dentro de la misma subcuenca hidrográfica. Dicha estación reproduce

bastante bien los eventos extremos ocurridos en la zona de estudio.

 - Para un periodo de retorno de T= 10 años se obtuvo un valor de 96,7 mm, la cual es

coherente (en órdenes de magnitud un poco mayor) con la estimada por el Balance Hídrico

Nacional (DGA, 1987) alrededor de 90 mm.

 - Asimismo, para un periodo de retorno de T= 100 años se obtuvo un valor de 148,9 mm, cuyo

valor está por encima del mayor evento de precipitación registrado cercano a la zona (124

mm en 24 horas el día 12 de julio de 1940). Por lo tanto, se tomará el valor de T=100 años

calculado como la precipitación de diseño.

 - Se ha realizado la caracterización geomorfológica de las cuencas aportantes a la zona de

estudio, así como el cálculo de los caudales máximos para distintos periodos de retorno (T=

2 hasta 100 años) utilizando el Método Racional del Manual de Carreteras del MOP, 2020.

 - La modelación hidráulica fue realizada en condiciones conservadoras, de caudal máximo

constante hasta el tiempo suficiente de llenado del embalse con sobrepaso (65.200

segundos, o 18,12 horas). Se considera esta área como el área máxima de inundación.

 - Se ha realizado un trabajo iterativo entre la hidráulica y la ingeniería del proyecto para lograr

un layout (caminos, paneles, postes, estructuras, vallado perimetral) que evite por completo

el área de inundación del embalse, como también la ocurrida el año 2007 optando por la

seguridad de estructuras y personas. Por lo tanto, no se afectará la red hidrográfica

delimitada por la DGA y por el IGM.

 - Igualmente, se evita toda el área de escurrimientos interiores del parque.

 - Las obras proyectadas no intervienen en ningún caso los escurrimientos, permitiendo su

libre tránsito y flujo.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 54
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

 - Las obras proyectadas no modifican en ninguna forma la cantidad o calidad del agua que va

desde el parque hacia el embalse o desde el embalse hacia cercanías del parque. Por lo

tanto, no se generan efectos sobre la permanencia de este preciado recurso agua tan

escaso, asociada a su disponibilidad, utilización y aprovechamiento racional futuro (no

afectación sobre el consumo humano del agua).

 - Finalmente, no se generarán impactos significativos sobre la cantidad y calidad de los

recursos hídricos ni efectos sobre la capacidad de generación o renovación del recurso, ya

que los escurrimientos ni red hidrográfica superficial (red DGA e IGM) no serán intervenidas.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 55
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

#### 6. ANEXOS

##### 6.1. Anexo A. Modelación rotura del Embalse Cerrillos de Leyda

_6.1.1._ _Tipo de falla analizada (conceptual)_

En el Informe ESTUDIO DE CATASTRO E INSPECCIÓN PRELIMINAR DE EMBALSES PRIMERA ETAPA
QUINTA REGIÓN de R.E.G Ingenieros Consultores y la Dirección General de Aguas (1994), se hace

una revisión de la seguridad de los embalses mayores en la región de Valparaíso basado en la

metodología HAZOP. Se definió que para el embalse Cerrillos de Leyda se presenta un riesgo Bajo y

que el evento crítico sería una falla por Piping.

_Figura 6-1. Tabla de síntesis de riesgos críticos en algunos embalses de San Antonio._

_Fuente: Estudio de Catastro e inspección preliminar de embalses primera etapa, quinta región, R.E.G. Ingenieros_

_Consultores y Dirección General de Aguas (1994)._

A pesar de que se cataloga como un riesgo bajo, en las “Conclusiones y Recomendaciones” se señala

que se presenta un riesgo por piping, y que ante rotura o vaciamiento la onda de crecida será muy

grande, con posible afectación al Embalse San Juan, que se encuentra 4 kilómetros aguas abajo del

Embalse Leyda.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 56
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 6-2. Conclusiones y recomendaciones asociadas a la ficha de Evaluación de Riesgo Total de la Presa (Embalse_

_Cerrillos de Leyda)._

_Fuente: Estudio de Catastro e inspección preliminar de embalses primera etapa, quinta región (1994), R.E.G._

_Ingenieros Consultores y Dirección General de Aguas_

Es por este motivo, que el objetivo de este Anexo es evaluar y cuantificar esta onda de crecida

generada tras la rotura del embalse a través de un hidrograma de caudal.

Inicialmente la falla por sobrepaso y piping (1) se podrían dar de forma simultánea, y si este es

el caso existe una probabilidad de que falle por deslizamiento de talud exterior (2, aguas abajo

del muro), luego, al liberarse un volumen inicial de agua, se genera una socavación local con

capacidad de socavar o generar deslizamiento del talud interior (3, aguas arriba del muro). La

secuencia lógica de falla analizada es la indicada en la Figura 6-3.

_Figura 6-3. Secuencia lógica conceptual del tipo de falla analizada._

_6.1.2._ _Tipo de falla modelada_

Para poder modelar la conceptualización antes realizada se realizará una serie de

simplificaciones del proceso físico:

 - Inicialmente **se modela el sobrepaso** (Y con esto se estima la capacidad máxima de

inundación del embalse, análisis expuesto en el informe) y;

 luego **formación de una brecha o falla trapezoidal**, que sería la simplificación de un

deslizamiento de talud exterior sumado al talud interior debido a la socavación inducida por

la liberación de caudal, generando un vaciamiento parcial del embalse.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 57
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 6-4. Tipo de falla o brecha trapezoidal modelada._

_6.1.3._ _Parámetros de la falla o brecha modelada_

**a)** **Eje longitudinal de Rotura:**

70 metros

_Figura 6-5. En color rojo está representado el eje longitudinal de rotura del muro de tierra de Embalse Leyda._

**b)** **Cota superior de la falla (elevación):**

173 m.

**c)** **Cota inferior de la falla (elevación):**

164 m.

**d)** **Altura de agua (** H **):**

Cota superior - Cota inferior **=** 9 m

**e)** **Ancho superior de falla (** b **):**

b= 3H (US Bureau of Reclamation, 1988) = 27 m

**f)** **Ancho inferior de falla:**

20 m

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 58
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

**g)** **Tiempo de formación de la rotura (** Tf **):**

Al ser una presa de tierra la falla no será tan frágil como lo podría ser en una presa de

hormigón, se utilizará el criterio de MacDonald y Langridge-Monopolis (1984):

Tf (horas) = 0,0179Ve [0,364]

Con Ve= 11250 m [3], Tf será aproximadamente 30 minutos.

_6.1.4._ _Resultados_

Inicialmente se modelan unos minutos del sobrepaso del muro, esto ocurre inicialmente en el

segundo 65.220 de modelación (18 horas aprox.) y luego al segundo 70.000 (19 horas y 30 minutos

aprox.) se modela el inicio de la rotura, que se extiende por 30 minutos. La rotura se forma en un

lapso de 30 minutos. En la Figura 6-6 de muestran 2 instantes de la modelación hidrodinámica 2D

en Iber.

 En el instante a, han transcurrido 70.000 segundos de modelación (es decir 19,44 horas). En

este instante comienza a formarse la falla en el muro, que se prolongará por 1800 segundos

(30 minutos) hasta completarse.

 En el instante b, han transcurrido 71.800 segundos (es decir 19,94 horas) de modelación. En

este instante la formación de la falla está completa, y se observa el máximo caudal saliente

del embalse.

 En el instante c, han transcurrido 80.000 segundos de modelación, marcando el final de

ésta.

Cabe mencionar que una vez ocurre el vaciamiento parcial del embalse, el área de inundación en

cercanías del parque como es lógico también disminuye.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 59
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Figura 6-6. Hidrodinámica de la rotura en Iber para 4 instantes (a segundo 70.000; b segundo 71.800; y c segundo_

_80.000)_

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 60
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

El caudal máximo que se observa en la simulación es de aproximadamente 800 m [3] /s y el flujo se
dirige aguas abajo del muro siguiendo la máxima pendiente identificada en el levantamiento

topográfico de detalle, es decir con dirección clara y directa hacia el Embalse San Juan. En la Figura

6-7 se muestra el hidrograma de vaciamiento parcial simulado.

_Figura 6-7. Hidrograma del caudal de salida tras rotura del embalse._

##### 6.2. Anexo B. Digital. Datos estaciones DGA 6.3. Anexo C. Topografía 6.4. Anexo D. Resumen metodológico para la determinación de caudales de crecidas en cuencas sin control fluviométrico

Para definir los caudales de crecidas en el caso de las cuencas sin control fluviométrico, se utilizaron

relaciones de precipitación-escorrentía, a partir de las precipitaciones máximas en 24 horas, de

acuerdo con la distribución espacial de las estaciones en la cuenca. Para ello se estimaron las

precipitaciones máximas en 24 horas para periodos de retorno de 2, 5, 10, 20, 25, 50, 100 y 200

años mediante análisis de frecuencia Log-Normal, Normal, Pearson, Log-Pearson y Gumbel.

Posteriormente, se aplicaron las metodologías definidas en el “Manual de cálculo de crecidas y

caudales mínimos en cuencas sin información fluviométrica” (DGA, 1995) y “Manual de Carreteras

Vol. N°3 (MOP, 2020), en los cuales se plantea básicamente la aplicación de cuatro fórmulas

empíricas para el cálculo de crecidas en cuencas pluviales a partir de la información pluviométrica y

las características morfológicas de cada cuenca, en que se aplican parámetros relativos a cada

región. Estos métodos son DGA-AC, Verni y King modificado y Método Racional. De estos métodos

se aplicó el Método Racional del Manual de Carreteras, ya que todas las cuencas aportantes tienen
un área menor a 25 km [2] . Cada uno de los métodos se detalla a continuación como una forma de

orientar al lector:

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 61
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

 - **D.1 Método DGA-AC**

El método DGA-AC para crecidas pluviales, corresponde a un análisis regional de crecidas de origen

pluvial, basado en series de máximos anuales generadas a partir de información de caudales medios

diarios máximos e instantáneos máximos del período pluvial, de 234 estaciones de control

fluviométrico. Este método, que abarca estaciones desde la III a la IX Región, es válido para cuencas

pluviales o pluvionivales sin información fluviométrica y con áreas comprendidas entre 20 y 10.000

[km [2] ]. Su uso está restringido a períodos de retorno inferiores a 100 años.

El método consiste básicamente en determinar una curva de frecuencia para el caudal instantáneo

máximo de la cuenca, en base al procedimiento esquematizado en el diagrama presentado en la

Ilustración Anexo D-1.

_Ilustración Anexo D-1: Diagrama método DGA-AC_

_Fuente: Manual de Cálculo y Crecidas y Caudales Mínimos en Cuencas sin información fluviométrica (DGA,_

_1995)._

Se definen las cuencas ubicadas entre las latitudes 25°S y 352S, pertenecientes a las cuencas

Copiapó, Huasco y Elqui como Ip. En la Ilustración Anexo D-2 se definen las zonas correspondientes.

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 62
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

_Ilustración Anexo D-2: Definición Zonas Homogéneas Pluviales, método DGA-AC_

_Fuente: Manual de Cálculo y Crecidas y Caudales Mínimos en Cuencas sin información fluviométrica (DGA,_

_1995)._

Una vez definidas las zonas homogéneas pluviales, se define la curva de frecuencia regional de

caudales medios diarios máximos para distintos periodos de retorno, según lo establecido en el

Manual de Cálculo de Crecidas y Caudales mínimos en Cuencas sin Información Fluviométrica (DGA,

1995).

_Cuadro Anexo D-1: Curva de Frecuencia Caudales Medios Máximos Diarios para cuencas homogéneas “Ip”_

|Curva de Frecuencia Caudales<br>Medios Máximos Diarios Ip|Q(T)/Q(10)|Col3|Col4|
|---|---|---|---|
|Periodo de Retorno T (años|Media|Máxima|Mínima|
|2|0,43|0,52|0,35|
|5|0,74|0,80|0,63|
|10|1|1|1|
|20|1,27|1,34|1,21|
|25|1,36|1,46|1,27|
|50|1,66|1,87|1,49|
|75|1,86|2,13|1,62|
|100|2,00|2,33|1,71|

Para la determinación de los caudales medios diarios de período de retorno de 10 años, se plantea

la siguiente relación, correspondiente a la III y IV Región:

Q 10 = 1,94 ∙10 [−7] ∙Ap [0,776] ∙(P 2410 ) 3,108 Ecuación 1

Donde:

Q 10 : Caudal medio diario máximo de periodo de retorno 10 años [m [3] /s]
Ap : Área pluvial de la cuenca [km [2] ]

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 63
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

P 2410 : Precipitación diaria máxima de periodo de retorno 10 años [mm]

Finalmente, a través de un factor de conversión asociado a las zonas homogéneas (para el caso de

la zona de estudio _Ip=1,25_ ), se estima el caudal instantáneo máximo a partir del caudal medio diario

máximo.

**D.2 Método Verni y King modificado**

Este método relaciona el caudal instantáneo máximo de una crecida con la precipitación diaria

máxima y el área pluvial a través de una relación de potencias. Esta fórmula se establece para

períodos de retorno mayores a 30 años. Tiene la siguiente forma:

Q= C(T) ∙0,00618 ∙Ap [0,88] ∙P 241,24 Ecuación 2

Donde:

Q : Caudal instantáneo máximo de periodo de retorno T años [m [3] /s]
C(T) : Coeficiente empírico de periodo de retorno T años
Ap : Área pluvial de la cuenca [km [2] ]
P 24 : Precipitación diaria máxima asociada al periodo de retorno T años [mm]

El coeficiente empírico para período de retorno de 10 años para la II Región es de 0,027. La curva

de frecuencia del coeficiente empírico para la III Región se presenta en el Cuadro Anexo D-2.

_Cuadro Anexo D-2: Curva de frecuencia de coeficiente empírico III Región para aplicación de Verni y King modificado_

|T<br>(años)|C(T) /C(T=10)|
|---|---|
|**2 **<br>**5 **<br>**10**<br>**20**<br>**25**<br>**50**<br>**100**|0,90<br>0,95<br>1,00<br>1,10<br>1,14<br>1,23<br>1,32|

_Fuente: Manual de Cálculo y Crecidas y Caudales Mínimos en Cuencas sin información fluviométrica (DGA,_

_1995)._

**D.3 Método de la Fórmula Racional**

La expresión para la determinación del caudal máximo instantáneo de período de retorno T es la

siguiente.

Q= [C∙i∙Ap] Ecuación 3

3,6

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 64
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

Donde:

Q : Caudal instantáneo máximo de periodo de retorno T años [m [3] /s]
C : Coeficiente de escorrentía asociado al periodo de retorno T años
Ap : Área pluvial de la cuenca [km [2] ]
i : Intensidad media de lluvia asociada al periodo de retorno T y a una duración igual al
tiempo de concentración de la cuenca pluvial [mm/hr]

Finalmente, se aplican 3 fórmulas para determinar el tiempo de concentración de la cuenca,

utilizando las características morfológicas de las cuencas, las cuales se indican a continuación.

_Cuadro Anexo D-3: Fórmulas para determinar el tiempo de concentración (Tc) de una cuenca_

|- California Culverts<br>Practice (1942)|L3 0,385<br>tc = 0,95 ⋅( )<br>H|Ecuación 4|
|---|---|---|
|- <br>Giandotti|tc=4 ⋅A0,5 + 1,5 ⋅L<br>0,8 ⋅√Hm<br>|Ecuación 5|
|- <br>Normas Españolas|tc= 0,72 ⋅L0,76<br>S0,19|Ecuación 6|
|- <br>Kirpich (SCS, 1975)|tc= 258,7 ⋅L0,8(~~(~~1000<br>CN) −9)0,7/1900 ∙S0,5 <br>También puede determinarse por:<br> tc= 0,066 ⋅( L<br>√S~~)~~<br>0,77<br>|<br>Ecuación 7|

_Fuente: Manual de Carreteras (MOP, 2020 - Tabla 3.702.501.A)_

Donde:

tc : Tiempo de concentración [h]
L : Longitud del cauce [km]
S : Pendiente media de la cuenca [%]
H : Diferencia de nivel entre las cotas extremas de la cuenca [m]

H m : Diferencia de nivel entre la cota media y la cota mínima de la cuenca [m]
A : Área de la cuenca [km [2] ]

CN : Curva Número

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 65
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

 - **Coeficiente de escorrentía asociado al periodo de retorno T años**

Los coeficientes de escurrimiento “C” dependen de las características del terreno, uso y manejo del

suelo, condiciones de infiltración, además de factores de relieve, cobertura vegetal y

almacenamiento y se necesita un criterio técnico adecuado y experiencia para seleccionar un valor

representativo. Para el cálculo de “C” se aplicará la Tabla 3.702.503.A y Tabla 3.702.503.B del

Manual de Carreteras (MOP, 2020), las cuales se presentan a continuación:

_Cuadro Anexo D-4: Fórmulas para determinar el coeficiente de escorrentía (C) de una cuenca_

_Fuente: Manual de Carreteras (MOP, 2020 - Tabla 3.702.503.B)_

Para el cálculo de los coeficientes de escorrentías para T<10 años y T>100 años se aplicarán los

coeficientes indicados a continuación:

|ión:|Col2|
|---|---|
|T|C (T=10 años)|
|2|C x 0,82*|
|5|C x 0,92*|
|10|C x 1,0|
|20|C x 1,08*|
|25|C x 1,10|
|50|C x 1,20|
|100|C x 1,25|

*Valor obtenido de la curva: C (T)= 0,112ln(T) + 0,7443

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 66
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

##### 6.5. Anexo E. Solicitud de información DOH Valparaíso

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 67
**Of. 1620, Santiago de Chile**

PR28- Línea Base Hidrológica Parque Fotovoltaico Leyda, San Antonio, Región de Valparaíso

##### 6.6. Anexo F. Registro fotográfico Leyda

**www.inrhedchile.com** **info@inrhedchile.com** **+56 2440 5103** **Av. Nueva Providencia 1881,** 68
**Of. 1620, Santiago de Chile**