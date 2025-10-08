---
title: Proyecto Captacion de agua canal La Higuera
author: Eduardo Rojas
date: D:20210514140535-04'00'
language: es
type: report
pages: 82
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 3.3 ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS
-->

# ANEXO 3.3 ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS

PROYECTO: “EXTENSIÓN VIDA ÚTIL PLANTA CHANCADO MÓVIL, TALTAL”

FEBRERO 2021

MASMINING
Avenida Balmaceda 417, Oficina 32, La Serena - Chile

Fono Celular +56 9 71396155 | Fijo +51 2 590140

erojas@masmining.com | [www.masmining.com](http://www.masmining.com/)

1

INCONSULT

**1463/OT11**

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**ÍNDICE**

**1** **INTRODUCCIÓN ............................................................................................ 5**

**2** **NORMATIVA .................................................................................................. 7**

**3** **METEOROLOGÍA Y CALIDAD DEL AIRE .......................................................... 7**

3.1 C LIMA ....................................................................................................... 11

3.2 M ETEOROLOGÍA ............................................................................................ 14

_3.2.1_ _Velocidad del viento ............................................................................. 14_

_3.2.2_ _Dirección del viento .............................................................................. 16_

3.3 C ALIDAD DEL AIRE ......................................................................................... 19

3.4 A NÁLISIS DE I NCERTIDUMBRE ............................................................................ 24

**4** **ESTIMACIÓN DE EMISIONES ....................................................................... 25**

4.1 M ETODOLOGÍA ............................................................................................. 26

4.2 R ESUSPENSIÓN DE MATERIAL POR TRÁNSITO EN CAMINO NO PAVIMENTADO ....................... 28

_4.2.1_ _Nivel de Actividad ................................................................................ 28_

_4.2.2_ _Factores de Emisión ............................................................................. 30_

_4.2.3_ _Emisiones ........................................................................................... 31_

4.3 T RANSFERENCIA DE M ATERIAL ........................................................................... 32

_4.3.1_ _Nivel de Actividad ................................................................................ 32_

_4.3.2_ _Factores de emisión ............................................................................. 32_

_4.3.3_ _Emisiones ........................................................................................... 34_

4.4 P ROCESAMIENTO DE M ATERIAL .......................................................................... 34

_4.4.1_ _Nivel de Actividad ................................................................................ 34_

_4.4.2_ _Factores de Emisión ............................................................................. 35_

_4.4.3_ _Emisiones ........................................................................................... 35_

4.5 C OMBUSTIÓN INTERNA DE MAQUINARIA ................................................................ 36

_4.5.1_ _Nivel de Actividad ................................................................................ 36_

_4.5.2_ _Factores de Emisión ............................................................................. 37_

_4.5.3_ _Emisiones ........................................................................................... 37_

4.6 C OMBUSTIÓN INTERNA DE VEHÍCULOS .................................................................. 37

_4.6.1_ _Nivel de Actividad ................................................................................ 37_

_4.6.2_ _Factores de emisión ............................................................................. 38_

_4.6.3_ _Emisiones ........................................................................................... 38_

4.7 E ROSIÓN DE MATERIAL EN PILA .......................................................................... 39

_4.7.1_ _Nivel de Actividad ................................................................................ 39_

_4.7.2_ _Factores de emisión ............................................................................. 39_

_4.7.3_ _Emisiones ........................................................................................... 40_

4.8 R ESUMEN DE E MISIONES ................................................................................. 41

**5** **MODELACIÓN ATMOSFÉRICA ...................................................................... 41**

1

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

5.1 C ARACTERÍSTICAS DEL M ODELO ......................................................................... 41

5.2 V ARIABLES DE ENTRADA AL SISTEMA DE MODELACIÓN ................................................ 44

5.3 R ESULTADOS DE LA M ODELACIÓN ....................................................................... 48

_5.3.1_ _Modelación WRF .................................................................................. 48_

_5.3.2_ _Aportes obtenidos en la Modelación ........................................................ 52_
5.4 U BICACIÓN P UNTO DE MÁXIMA CONCENTRACIÓN ...................................................... 54

**6** **APORTE DE OTROS PROYECTOS - EVALUACIÓN DEL EFECTO SINÉRGICO ... 58**

**7** **ANÁLISIS DE CUMPLIMIENTO DE NORMATIVA AMBIETNAL ........................ 58**

**8** **MAPAS DE ISOCONCENTRACIONES ............................................................. 62**

**9** **CONCLUSIONES .......................................................................................... 79**

**FIGURAS**

Figura 1.1. Localización del proyecto y principales receptores ....................................... 6
Figura 3.1. Data meteorológica y de calidad del aire de la Estación Taltal, años 2019 y

2020. .................................................................................................................. 10
Figura 3.2. Clasificación de Köppen para el Área de estudio del Proyecto ..................... 12
Figura 3.3. Temperatura promedio [°C] y Precipitación acumulada [mm/año] .............. 13
Figura 3.4. Ciclo estacional de la Velocidad del viento [m/s], años 2019 y 2020. .......... 15
Figura 3.5. Ciclo diario y mensual de la velocidad del viento [m/s], promedio 2019 y 2020.

.......................................................................................................................... 16

Figura 3.6. Rosa de los vientos anual [m/s], promedio 2019 y 2020. .......................... 17
Figura 3.7. Rosa de vientos horarias [m/s], promedio 2019 y 2020. ........................... 18
Figura 3.8. Evolución del PM 10 en sus valores horarios y promedios diarios, años 2019 y

2020. .................................................................................................................. 20

Figura 3.9. Variaciones en diferentes escalas temporales del PM 10 [μg/m [3] ], promedio 2019
y 2020. ............................................................................................................... 22
Figura 3.10. Concentración promedio diario del PM 10 [μg/m [3] ], años 2019 y 2020. ........ 23
Figura 3.11. Direcciones de origen de las concentraciones de PM 10, en base de VV y DV.

.......................................................................................................................... 24

Figura 3.12. Velocidad promedio del viento en m/s. .................................................. 25
Figura 4.1. Ubicación referencial de los caminos utilizados por el Proyecto. .................. 29
Figura 5.1. Imagen referencia tridimensional del terreno. .......................................... 45
Figura 5.2. Usos del suelo ...................................................................................... 46
Figura 5.3. Fuentes de Emisión............................................................................... 47
Figura 5.4. Campos de viento a las 06:00 horas ....................................................... 49
Figura 5.5. Campos de viento a las 12:00 horas ....................................................... 50
Figura 5.6. Campos de viento a las 18:00 horas ....................................................... 51
Figura 5.7. Campos de viento a las 00:00 horas ....................................................... 52
Figura 5.8. Ubicación puntos de máxima concentración "Fase de Operación Planta de

Chancado" ........................................................................................................... 57

2

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

Figura 8.1. "Fase de Operación Planta de Chancado" Promedio anual de MP 10 - PMC ..... 63
Figura 8.2. "Fase de Operación Planta de Chancado" Percentil 98 diario de MP 10 - PMC .. 65
Figura 8.3. "Fase de Operación Planta de Chancado" Promedio anual de MP 2,5 - PMC ..... 66
Figura 8.4. "Fase de Operación Planta de Chancado" Percentil 98 diario de MP 2,5 - PMC . 67
Figura 8.5. "Fase de Operación Planta de Chancado" Promedio anual de MPS - PMC ...... 68
Figura 8.6. "Fase de Operación Planta de Chancado" Promedio mensual de MPS - PMC .. 69
Figura 8.7. "Fase de Operación Planta de Chancado" Promedio anual SO 2 - PMC ........... 70
Figura 8.8. "Fase de Operación Planta de Chancado" Percentil 99 diario SO 2 - PMC ....... 71
Figura 8.9. "Fase de Operación Planta de Chancado" Percentil 99,7 diario SO 2 - PMC .... 72
Figura 8.10. "Fase de Operación Planta de Chancado" Percentil 99,73 horario SO 2 - PMC

.......................................................................................................................... 73

Figura 8.11. "Fase de Operación Planta de Chancado" Percentil 98,5 horario SO 2 - PMC 74
Figura 8.12. "Fase de Operación Planta de Chancado" Promedio anual NO 2 - PMC ......... 75
Figura 8.13. "Fase de Operación Planta de Chancado" Percentil 99 horario NO 2 - PMC ... 76
Figura 8.14. "Fase de Operación Planta de Chancado" Percentil 99 horario CO - PMC .... 77
Figura 8.15. "Fase de Operación Planta de Chancado" Percentil 99 8 horas CO - PMC .... 78

**TABLAS**

Tabla 2.1. Normas de calidad del aire consideradas en el estudio .................................. 7

Tabla 3.1. Estación de monitoreo - Localización y Variables Monitoreadas ..................... 9
Tabla 3.2. Porcentaje de data válida para las variables monitoreadas .......................... 11
Tabla 3.3. Resumen de Información de velocidad del viento, Años 2019 y 2020 ........... 14
Tabla 3.4. Normativa primaria de calidad del aire para MP 10 ....................................... 19
Tabla 3.5. Monitoreo material particulado MP 10 y comparación con norma .................... 19
Tabla 4.1. Actividades emisoras MP 10, MP 2,5, MPS y gases SO 2, NOx y CO .................... 26
Tabla 4.2. Nivel de actividad - Tránsito por camino no pavimentado ........................... 29
Tabla 4.3. Factor de emisión - Tránsito por camino no pavimentado industrial ............. 31
Tabla 4.4. Emisiones resultantes -Resuspención por tránsito en camino no pavimentado

.......................................................................................................................... 32

Tabla 4.5. Nivel de actividad - Transferencia de material ........................................... 32

Tabla 4.6. Factor de emisión - Transferencia de material ........................................... 34

Tabla 4.7. Emisiones resultantes - Transferencia de material ..................................... 34

Tabla 4.8. Nivel de actividad - Procesamiento de Material ......................................... 35

Tabla 4.9. Factor de Emisión - Procesamiento de Material ......................................... 35

Tabla 4.10. Emisiones resultantes - Procesamiento de material .................................. 36

Tabla 4.11. Nivel de actividad - combustión interna de maquinaria ............................. 36
Tabla 4.12. Factor de emisión - Combustión interna de maquinaria ............................ 37
Tabla 4.13. Emisiones Resultantes - Combustión interna de maquinaria ...................... 37
Tabla 4.14. Nivel de actividad - Combustión interna de vehículos ............................... 38

Tabla 4.15. Factor de emisión - Combustión interna de vehículos [g/km] .................... 38
Tabla 4.16. Emisiones resultantes - Combustión interna de vehículos ......................... 39

Tabla 4.17. Nivel de actividad - Erosión de material en pila ....................................... 39
Tabla 4.18. Factor de emisión - Erosión de material en pila ....................................... 40

3

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

Tabla 4.19. Emisiones resultantes - Erosión de material en pila ................................. 41

Tabla 4.20. Emisiones resultantes ........................................................................... 41

Tabla 5.1. Características del uso de suelo ............................................................... 44

Tabla 5.2. Localización puntos discretos .................................................................. 48
Tabla 5.3. Aportes del Proyecto en puntos de interés y puntos de máxima concentración
(PMC) “Fase de Operación Planta de Chancado [μg/m [3] ]” Sin Factor de Corrección ........ 54
Tabla 5.4. Aportes del Proyecto de MPS y SO 2 (Norma Secundaria) en puntos de interés y
punto de máxima concentración (PMC) “Fase de Operación Planta de Chancado” Sin Factor
de Corrección ....................................................................................................... 54

Tabla 5.5. Aportes del Proyecto en puntos de interés y puntos de máxima concentración
(PMC) “Fase de Operación Planta de Chancado [μg/m [3] ]” Con Factor de Corrección ....... 55
Tabla 5.6. Aportes del Proyecto de MPS y SO 2 (Norma Secundaria) en puntos de interés y
punto de máxima concentración (PMC) “Fase de Operación Planta de Chancado” Con Factor
de Corrección ....................................................................................................... 55

Tabla 5.7. Coordenadas de localización punto de máxima concentración (PMC) "Fase de
Operación Planta de Chancado" .............................................................................. 56
Tabla 7.1. Análisis de cumplimiento de normativa vigente para MP 10 “Fase de Operación
Planta de Chancado” [μg/m [3] ] ................................................................................. 58
Tabla 7.2. Análisis de cumplimiento de normativa vigente para MP 2,5 “Fase de Operación
Planta de Chancado” [μg/m [3] ] ................................................................................. 59
Tabla 7.3. Análisis de cumplimiento de normativa vigente para MPS “Fase de Operación
Planta de Chancado” [μg/m [3] ] ................................................................................. 59
Tabla 7.4. Análisis de cumplimiento de normativa vigente para CO “Fase de Operación
Planta de Chancado” [μg/m [3] ] ................................................................................. 60
Tabla 7.5. Análisis de cumplimiento de normativa vigente para NO 2 “Fase de Operación
Planta de Chancado” [μg/m [3] ] ................................................................................. 60
Tabla 7.6. Análisis de cumplimiento de normativa vigente para SO 2 “Fase de Operación
Planta de Chancado” [μg/m [3] ] ................................................................................. 60

4

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**1** **INTRODUCCIÓN**

El presente documento da cuenta de los resultados obtenidos de la estimación
y modelación de la dispersión de las emisiones atmosféricas del Proyecto
Minero “Extensión vida útil planta de chancado móvil, Taltal”, en el marco de
la presentación de una Evaluación Ambiental.

Cabe señalar que el Proyecto se localiza en la Región de Antofagasta, a
aproximadamente 3,5 km al noreste de la ciudad de Taltal, en el sector de
Lixiviación Secundaria de la Planta Taltal.

Cabe destacar que la extensión busca ampliar la vida útil del proyecto
“Modificación de Emplazamiento de Planta de Chancado Móvil”, aprobado
ambientalmente mediante la Resolución de Calificación Ambiental No100, del
6 de abril del año 2010. La Planta de Chancado Móvil aprobada por la
Resolución No100/2010 alcanza una capacidad nominal de 15.200 [t/mes] con

un sistema de muestreo.

De acuerdo con las características del Proyecto, se ha establecido un escenario
para estimar las emisiones, y posterior modelación, correspondiente a un
escenario de operación que considera una producción anual de material de
260.000 [t/año].

Conforme a lo anterior, y de acuerdo con las características del Proyecto, en
el presente documento se estiman las emisiones atmosféricas de los
contaminantes material particulado respirable (MP 10 ), material particulado
respirable fino (MP 2,5 ), material particulado sedimentable (MPS), dióxido de
azufre (SO 2 ), dióxido de nitrógeno (NO 2 ) y monóxido de carbono (CO).

Posteriormente, con el fin de determinar el impacto asociado a la ejecución
del Proyecto, las emisiones estimadas para cada uno de los contaminantes
serán modeladas con el fin de obtener las concentraciones resultantes en el

área de estudio. Lo anterior en consideración de los requerimientos de la “Guía
para el Uso de Modelos de Calidad del Aire en el SEIA, 2012” del Servicio de
Evaluación Ambiental. Respecto a esto, el sistema de modelación atmosférica
utilizado corresponde al “WRF - CALPUFF”, definido por la agencia EPA como
sistema de referencia para simular la dispersión de contaminantes
provenientes de instalaciones industriales ubicadas en terreno complejo.

5

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

En cuanto a la meteorología base utilizada en la modelación, se seleccionó el
modelo de pronóstico Weather Research and Forecasting (WRF), el cual
proveerá los datos de entrada para el modelo de dispersión CALPUFF.

El dominio del modelo de dispersión atmosférica corresponde a una grilla de
20 x 25 km, con un espaciamiento de 1 km, en cuyo interior se encuentra el
área de emplazamiento del Proyecto y los puntos de interés, asociados a
receptores cercanos (viviendas ubicadas en las inmediaciones del área del
Proyecto), un receptor en la playa más cercana y la estación de monitoreo de
calidad del aire “Estación Taltal” de titularidad ENAMI.

La siguiente figura muestra la ubicación de las principales partes y receptores
del proyecto.

**Figura 1.1. Localización del proyecto y principales receptores**

Fuente: Elaboración propia, 2021.

6

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**2** **NORMATIVA**

Para evaluar el nivel de cumplimiento de la normativa, se consideraron las
normas primarias y secundarias de calidad del aire definidas en la legislación
chilena. La siguiente tabla presenta los valores límites de referencia para el
análisis del presente documento.

**Tabla 2.1. Normas de calidad del aire consideradas en el estudio**

|Parámetro|Tipo de<br>Norma|Estadístico|Valor|Referencia|
|---|---|---|---|---|
|**MP10**|Primaria|Promedio del periodo|50 mg/m3N|D.S. 45/02 MINSEGPRES|
|**MP10**|Primaria|Percentil 98 diario|150 mg/m3N|D.S. 59/98 MINSEGPRES|
|**MP2,5 **|Primaria|Promedio del periodo|20 mg/m3|D.S. 12/11 MMA|
|**MP2,5 **|Primaria|Percentil 98 diario|50 mg/m3|D.S. 12/11 MMA|
|**MPS**|Secundaria|Promedio Anual|100 mg/m2-día|D.S. 04/92 MINAGRI|
|**MPS**|Secundaria|Promedio Mensual|150 mg/m2-día|D.S. 04/92 MINAGRI|
|**SO2 **|Primaria|Promedio del periodo|60 mg/m3N|D.S. 104/19<br>MINSEGPRES|
|**SO2 **|Primaria|Percentil 99 diario|150 mg/m3N|D.S. 104/19<br>MINSEGPRES|
|**SO2 **|Primaria|Percentil 98,5 horario|350 mg/m3N|D.S. 104/19<br>MINSEGPRES|
|**SO2 **|Secundaria|Promedio del periodo|80 mg/m3N|D.S. 22/10 MINSEGPRES|
|**SO2 **|Secundaria|Percentil 99,7 diario|365 mg/m3N|D.S. 22/10 MINSEGPRES|
|**SO2 **|Secundaria|Percentil 99,73<br>horario|1.000 mg/m3N|D.S. 22/10 MINSEGPRES|
|**NO2 **|Primaria|Promedio del periodo|100 mg/m3N|D.S. 114/02<br>MINSEGPRES|
|**NO2 **|Primaria|Percentil 99 horario|400 mg/m3N|D.S. 114/02<br>MINSEGPRES|
|**CO**|Primaria|Percentil 99 (8 horas)|10.000 mg/m3N|D.S. 115/02<br>MINSEGPRES|
|**CO**|Primaria|Percentil 99 horario|30.000 mg/m3N|D.S. 115/02<br>MINSEGPRES|

Fuente: Biblioteca del Congreso Nacional de Chile

**3** **METEOROLOGÍA Y CALIDAD DEL AIRE**

En este apartado se presenta una descripción general de las características
climáticas, meteorológicas y de calidad del aire de la zona donde se emplaza
el proyecto, en base a los siguientes objetivos:

 - Caracterizar el clima en el cual se inserta el Proyecto.

7

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

 Caracterizar los parámetros meteorológicos representativos del área de

desarrollo del Proyecto, en particular los permiten evaluar el
comportamiento del modelo meteorológico WRF considerado.

 - Caracterizar la calidad del aire presente en el sector, particularmente

para la estación meteorológica con la que cuenta el proyecto, la cual
mide continuamente PM 10 en los años 2019 y 2020. Además de
compararla con la normativa primaria vigente de calidad del aire.

 Realizar una proyección de la calidad del aire en base a los proyectos

cercanos.

 Desarrollar un análisis de incertidumbre del modelo meteorológico

utilizado en la modelación.

Para describir las variaciones de climas que existen en el área del Proyecto,
se utiliza la clasificación de Köppen, la cual se basa en que la vegetación
natural tiene una clara relación con el clima, por lo que los límites entre un
clima y otro se establecen teniendo en cuenta la distribución vegetaestacional. Los parámetros para determinar el clima de un lugar son las
temperaturas y precipitaciones medias, anuales y mensuales, además de la
estacionalidad de la precipitación.

Respecto a la data para el desarrollo de la caracterización meteorológica y de
calidad del aire, se realiza una revisión de la información disponible en el
Sistema de Información de Calidad del Aire (SINCA), sin embargo, en esta red
de monitoreo ninguna estación se encuentra localizada en el área considerada
para la evaluación del proyecto. En la comuna de Taltal el SINCA cuenta con
data de dos estaciones de meteorología y calidad del aire: “Paposo” y “Punto
de Máximo Impacto”, las cuales se descartan para la caracterización, dado que
se encuentran fuera del área de estudio, a una distancia mayor de 40
kilómetros en línea recta, y contienen información del año 2009.

Debido a lo anterior, la caracterización meteorológica y de calidad del aire del
presente proyecto se elabora a partir del monitoreo continuo realizado por del
titular para los años 2019 y 2020 en la denominada Estación Taltal.

Las coordenadas UTM de la Estación Taltal, junto a las variables monitoreadas
que se consideraron en este informe, se muestran en la siguiente tabla y su

8

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

localización se detalla en la cartografía presentada en la Figura 1.1,
presentada anteriormente.

**Tabla 3.1. Estación de monitoreo - Localización y Variables Monitoreadas**

|Estación|Parámetro|Coordenadas UTM,<br>WGS84 [m]|Col4|Variable<br>monitoreada|Periodo considerado|Col7|
|---|---|---|---|---|---|---|
|**Estación**|**Parámetro**|Este|Norte|Norte|Inicio|Término|
|**Estación**<br>**Taltal**|Meteorología|351.932|7.190.064|Velocidad del viento|01-01-2019|31-12-2020|
|**Estación**<br>**Taltal**|Meteorología|351.932|7.190.064|Dirección del viento|01-01-2019|31-12-2020|
|**Estación**<br>**Taltal**|Calidad del<br>Aire|Calidad del<br>Aire|Calidad del<br>Aire|Material Particulado<br>PM10|01-01-2019|31-12-2020|

Fuente: Elaboración propia, 2021.

A continuación, se presenta un resumen general de la data analizada para la
meteorología y calidad del aire, en donde, a la izquierda se presenta la
distribución general de las monitoreadas, mientras que a la derecha los
histogramas, en conjunto con una serie de parámetros como las series de
tiempo, los valores mínimos, valores máximos, promedios, estadístico
percentil 95, y datos faltantes o no válidos.

9

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 3.1. Data meteorológica y de calidad del aire de la Estación Taltal, años 2019 y**

**2020.**

Fuente: Elaboración propia, 2021.

Para un análisis adecuado de las variables meteorológicas y de calidad, la serie
de datos debe contener al menos un 75% de datos válidos, lo que en el caso
de estudio se cumple para los periodos de estudio, ya que el registro con el
que se cuenta alcanza un 96%, para todas las variables monitoreadas, tal
como se puede ver en la siguiente tabla:

10

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Tabla 3.2. Porcentaje de data válida para las variables monitoreadas**

|Variable|Col2|Data válida|
|---|---|---|
|**PM10**|2019|96,8|
|**PM10**|2020|99,8|
|**Dirección del**<br>**viento**|2020|99,6|
|**Dirección del**<br>**viento**|2020|99,9|
|**Velocidad del**<br>**viento**|2019|99,6|
|**Velocidad del**<br>**viento**|2020|99,9|

Fuente: Elaboración propia, 2021.

**3.1** **Clima**

El proyecto se encuentra localizado en la zona costera de Taltal, al sur de la
región de Antofagasta. Según se puede observar en la siguiente figura, el área
del proyecto se posiciona sobre una zona climática tipo Desértica con
diferentes matices, pasando por los Climas desérticos cálidos, cálidos de lluvia
invernal, frio y frio de lluvia invernal. Las obras particulares del proyecto, y la
estación de monitoreo con la que cuenta, se posicionan específicamente sobre
el Clima desértico Cálido de Lluvia Invernal (BWh [s]), según la clasificación
de Köppen, el cual se presenta también, por toda la costa del área de estudio.

El Clima desértico con fuerte influencia costera se localiza a lo largo de la costa
de la Región de Antofagasta y gran parte de la Región de Atacama, sus efectos
se manifiestan hasta 20 kilómetros hacia el interior, donde la sequedad
atmosférica es mayor, debido a que, por causas del relieve, la influencia
marítima es retenida en los cerros de la Cordillera de la Costa. Las

características principales de este subtipo climático se traducen en un efecto
modelador de las temperaturas produciendo por la corriente fría de Humboldt,
la presencia de abundante humedad, neblinas matinales y la ausencia de
precipitaciones.

11

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 3.2. Clasificación de Köppen para el Área de estudio del Proyecto**

Fuente: Elaboración propia, 2021.

Las características principales de esta clasificación se resumen en una
precipitación acumulada anual de aproximadamente 25 mm/año, una
temperatura media de 18,5 ° C, con directa influencia del pacífico, ya que se
presenta desde los 0 metros sobre el mar hasta cerca de los 500 metros. En
particular, para el área de estudio se observan temperaturas medias que van
desde los 17,78 °C en las zonas interiores hasta los 18,4 °C en las zonas
costeras, mientras que, respecto de las precipitaciones, se observan
precipitaciones que aumentan desde las zonas interiores hacia la costa, desde
los 16 mm de agua acumulada hasta los 22 mm, justamente en donde se
localiza el Proyecto. Ahora bien, estos valores muestran el escaso aporte de

12

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

las lluvias, con valores poco significativos, más bien denotando las
características secas de la zona.

**Figura 3.3. Temperatura promedio [°C] y Precipitación acumulada [mm/año]**

Fuente: Elaboración propia, 2021.

13

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**3.2** **Meteorología**

Tal como se detalló en apartados anteriores, la caracterización meteorológica
del proyecto se elabora a partir del monitoreo continuo realizado por del titular
para los años 2019 y 2020, en la denominada Estación Taltal, la cual cuenta
con variables meteorológicas de dirección y velocidad del viento.

**3.2.1** **Velocidad del viento**

Tanto la velocidad como la dirección del viento son variables meteorológicas
relevantes para el análisis de la dispersión mecánica de los contaminantes en
el área de estudio. Debido a lo anterior, a continuación, se presenta un
resumen de la información registrada para ambas variables, con sus
respectivas series de tiempo, ciclos diarios, mensuales o estacional y un
resumen de los valores promedio y máximo de la velocidad del viento.

**Tabla 3.3. Resumen de Información de velocidad del viento, Años 2019 y 2020**

|Estadístico|2019|2020|
|---|---|---|
|**Promedio (m/s)**|1,80|1,79|
|**Máximo (m/s)**|5,20|5,50|

Fuente: Elaboración propia, 2021.

A continuación, se presenta el ciclo estacional de la velocidad del viento. En la
figura se puede observar que se producen las máximas velocidades de los
vientos entre las 14 y las 15 horas en los meses de diciembre y enero. Por
otra parte, los meses entre mayo y julio presentan mayor estabilidad y menor
variación de las velocidades de los vientos.

14

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 3.4. Ciclo estacional de la Velocidad del viento [m/s], años 2019 y 2020.**

Fuente: Elaboración propia, 2021.

Por otra parte, al observar el ciclo diario es posible indicar que los vientos
menores se presentan en horas de la mañana, a eso de las 6:00 AM, donde
comienzan a incrementar hasta alcanzar la máxima a las 14 horas

aproximadamente, para comenzar a bajar paulatinamente hasta llegar
nuevamente a la menor velocidad. En cuanto al ciclo mensual, los vientos más
bajo se presentan en los meses de invierno, particularmente en el mes de
mayo y lo mayores vientos se presentan en los meses de octubre a marzo. En
las siguientes figuras se presentan los ciclos diarios y mensuales de la
velocidad del viento, en donde, además de periodo, se agregan los percentiles
que permiten entender donde se encuentra el 50% de datos y donde se

encuentra el 90% de los datos.

15

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 3.5. Ciclo diario y mensual de la velocidad del viento [m/s], promedio 2019 y 2020.**

Fuente: Elaboración propia, 2021.

**3.2.2** **Dirección del viento**

Para la descripción de la dirección de los vientos se presentan tres análisis de
la rosa de los vientos: El primero muestra una rosa general, la que permite

16

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

comprender como se comportan en promedio los vientos del área de estudio;
El segundo muestra la variación en diferentes horas de la rosa de los vientos,
y finalmente; El tercero que muestra un análisis estacional de la variación de

los vientos del sector.

En la rosa de los vientos anuales es posible observar que los vientos
predominantes de mayor intensidad se concentran y vienen principalmente
desde entre el oeste (W) y el norte (N). Lo anterior tiene directa explicación
con la localización de la estación, la que se enfrenta a la costa y se encuentra
bajo la influencia de la topografía que genera el cerro localizado hacia el noreste de la estación.

**Figura 3.6. Rosa de los vientos anual [m/s], promedio 2019 y 2020.**

Fuente: Elaboración propia, 2021.

Las figuras horarias permiten complementar lo indicado anteriormente, ya que
representan la variación clásica que se observa en las rosas de los vientos

17

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

costera, en donde un cambio de dirección entre el día y la noche, de este a
oeste, pero con la variación o influencia que genera el cerro posicionado al
noreste de la estación, que genera una corriente de norte a sur.

**Figura 3.7. Rosa de vientos horarias [m/s], promedio 2019 y 2020.**

Fuente: Elaboración propia, 2021.

El comportamiento de los vientos, dada la influencia de la costa y la topografía
del sector, permite indicar una baja probabilidad de influencia de las emisiones
desde el muro del tranque hacia la estación meteorológica, en particular, dado

18

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

que las actividades se generan durante el día.

**3.3** **Calidad del aire**

En el presente apartado se da cuenta la caracterización de la Calidad del Aire
realizada a partir de los resultados de los monitoreos obtenidos de la Estación
Taltal para el Material Particulado respirable MP 10 .

Como marco normativo, en la siguiente tabla se presenta la normativa
primaria de calidad del aire vigente para el material particulado respirable

MP 10 .

**Tabla 3.4. Normativa primaria de calidad del aire para MP** **10**

|Decreto Aplicable|Norma|Col3|Periodo de Evaluación de Cumplimiento<br>de Norma|
|---|---|---|---|
|**Decreto Aplicable**|**Valor**|**Unidad**|**Unidad**|
|**Decreto Supremo**<br>**N°59/1998**|150|μg/m3N|Percentil 98 de las concentraciones de 24<br>horas registradas durante un periodo anual|
|**Decreto Supremo**<br>**N°45/2002**|50|50|Concentración promedio anual|

Fuente: Biblioteca del Congreso Nacional de Chile.

A continuación, se presenta el porcentaje de datos válidos, junto al resumen
de los monitoreos y la comparación con la normativa primaria de calidad del
aire para este contaminante.

**Tabla 3.5. Monitoreo material particulado MP** **10** **y comparación con norma**

|Año|Estadístico|Datos<br>Válidos|Valor<br>[ug/m3N]|Límite de la<br>Norma<br>[ug/m3N]|% de<br>la<br>Norma|
|---|---|---|---|---|---|
|**2019**|Promedio del período|96,8%|16,8|50|34%|
|**2019**|Percentil 98 Diario|Percentil 98 Diario|30,4|150|20%|
|**2020**|Promedio del período|96,8%|15,7|50|31%|
|**2020**|Percentil 98 Diario|Percentil 98 Diario|26,7|150|18%|
|**Promedio**<br>**bi-anual**|Promedio del período|96,8%|16,3|50|33%|
|**Promedio**<br>**bi-anual**|Percentil 98 Diario|Percentil 98 Diario|28,6|150|19%|

Fuente: Elaboración propia, 2021.

De la tabla anterior, se observa que la Estación Taltal ha registrado valores
que permiten indicar que las concentraciones se encuentran muy por debajo
de los umbrales saturación y latencia de la norma de calidad de aire de
material particulado respirable (MP 10 ) tanto para su estadígrafo de percentil

19

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

98 de concentración media diaria como en la media anual. En la siguiente
figura se muestra la serie de tiempo horario y los promedios diarios, que
grafican lo detallado:

**Figura 3.8. Evolución del PM** **10** **en sus valores horarios y promedios diarios, años 2019 y**

**2020.**

20

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

Fuente: Elaboración propia, 2021.

Para mayor abundamiento, a continuación, se presenta una figura que grafica,
en sus variaciones temporales horaria, diarias, semanal y por mes, las
concentraciones de material particulado PM 10 . Además, incluye una
representación de los percentiles 25-75 y 5-95, que permiten observar donde
se concentra el 50%, y el 70% respectivamente, de los datos medidos por
unidad de tiempo graficada.

21

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 3.9. Variaciones en diferentes escalas temporales del PM** **10** **[μg/m** **[3]** **], promedio 2019**

**y 2020.**

Fuente: Elaboración propia, 2021.

De la gráfica resultante es posible indicar lo siguiente:

 Se observa una leve disminución de los promedios de material

particulado en los días sábado y domingo.

 En las horas del día, las mayores concentraciones se observan entre las

12 y las 16 horas.

 Respecto a la variación mensual las mayores concentraciones se

observan en los meses de invierno, junio, julio y agosto, observándose
una baja abrupta en septiembre, cuando las velocidades del viento
comienzan a aumentar, en conjunto con el aumento de la temperatura,
que incide en la altura de mezcla.

Respecto a los datos capturados, se presenta la siguiente figura, la cual
muestra los valores diarios obtenidos por la estación de monitoreo de MP 10 .

22

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 3.10. Concentración promedio diario del PM** **10** **[μg/m** **[3]** **], años 2019 y 2020.**

Fuente: Elaboración propia, 2021.

De la figura anterior es posible indicar que los valores diarios se encuentran
muy por debajo de la normativa establecida para ese estadístico (150 μg/m3),

23

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

alcanzando en sus valores más altos aproximadamente 45 μg/m3, como valor
promedio día.

**Figura 3.11. Direcciones de origen de las concentraciones de PM** **10** **, en base de VV y DV.**

Fuente: Elaboración propia, 2021.

**3.4** **Análisis de Incertidumbre**

Con el fin de validar la modelación meteorológica se realizó un análisis de

24

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

incertidumbre desde la comparación de los datos de dirección del viento
observados y los modelados, lo cual se presenta en la siguiente figura.

**Figura 3.12. Velocidad promedio del viento en m/s.**

Fuente: Elaboración propia, 2021.

En el grafico anterior es posible observar que las direcciones se subestiman
como máximo, en la modelación en un 12%. Dado lo anterior, se considera
utilizar un factor de corrección correspondiente a la amplificación de las
concentraciones resultantes de la modelación por 1,12.

**4** **ESTIMACIÓN DE EMISIONES**

El presente capítulo se da cuenta de la estimación de emisiones atmosféricas
de material particulado y gases, que generan las actividades asociadas a la
extensión de la vida útil del Proyecto.

La siguiente tabla resume las actividades, y los contaminantes estimados, para
las fuentes que generan emisiones atmosféricas en el Proyecto.

25

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Tabla 4.1. Actividades emisoras MP** **10** **, MP** **2,5** **, MPS y gases SO** **2** **, NOx y CO**

|Actividad|Contaminante|
|---|---|
|− Trasferencia de material tipo carga y descarga<br>− Tránsito en camino industrial no pavimentado<br>− Chancado de material, primario y secundario<br>− Selección de material, tamizado fino y grueso<br>− Puntos de transferencia en correas<br>transportadoras<br>− Erosión Eólica<br>|MP10, MP2,5y MPS|
|− Motor de vehículos<br>− Motor maquinarias<br>|MP10, MP2,5,MPS y gases<br>(CO, NOx y SO2)|

Fuente: Elaboración propia, 2021.

En los siguientes apartados se presenta: primero, la metodología para la
estimación de las emisiones atmosféricas; luego se presenta la estimación de
emisiones atmosféricas para cada una de las fuentes, en donde se detalla el
nivel de actividad, el factor de emisión determinado o utilizado y la emisión
resultante, y; finalmente se adjunta un resumen de las emisiones resultantes.

**4.1** **Metodología**

La metodología considera utilizar los factores de emisión y fórmulas
propuestas por : a) La Agencia de Protección Ambiental de los EE.UU. en el
documento “AP-42 5th Edition” y la Agencia Medioambiental Europea en el
documento “EEA Report N°21/2016”; b) La información indicada por el
SEREMI de Medio Ambiente Región Metropolitana mediante el documento
“Guía para la Estimación de Emisiones Atmosféricas de Proyectos
Inmobiliarios” de enero del 2012 (en adelante Guía RM 2012); c) El “Informe
Final Servicio de Recopilación y Sistematización de Factores de Emisión para
Aire para el Servicio de Evaluación Ambiental (SEA)” (mayo, 2015); d) La
“Guía Metodológica, Inventario de Emisiones Atmosféricas - Metodología
SINCA” de octubre del 2011 (en adelante Guía SINCA), y; e) La “Guía para la
Estimación de Emisiones Atmosféricas en la Región Metropolitana” de junio de
2020 (en adelante Guía RM 2020).

Según la metodología de cálculo recomendada por la EPA, la ecuación general
para determinar las emisiones de material particulado de gran parte de las

26

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

actividades corresponde a la siguiente:

E=Fe*Na*(1-Ea/100)

Donde:

E: Emisión

Fe: Factor de emisión

Na: Nivel de actividad

Ea: Eficiencia de abatimiento (%) de las medidas de mitigación
contempladas por el Proyecto.

Específicamente para la generación de emisiones por maquinaria, la ecuación
utilizada corresponde a:

E=FP*t*C*P

Donde:

E: Emisión

FP: Factor de emisión según potencia

t: Tiempo de operación

C: Porcentaje de carga

P: Potencia nominal

En cuanto a la generación de emisiones por combustión de vehículos la
ecuación utilizada para su estimación corresponde a:

E=FE*D

Donde:

E: Emisión

FE: Factor de emisión según categoría del vehículo

27

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

D: Distancia recorrida

Los valores de nivel de actividad (NA) son deducidos de la descripción del
Proyecto y de las respectivas actividades que éste involucra durante su
desarrollo. Para efectos del cálculo de emisiones, los factores o niveles de
actividad corresponden a parámetros que indican el grado o intensidad de
ejecución del Proyecto en el tiempo. Los factores de emisión (Fe)
corresponden a ecuaciones o expresiones matemáticas que permiten estimar
tasas unitarias de emisiones atmosféricas. Los factores de emisión, que
permiten estimar las emisiones particulares del Proyecto, son detallados en
los siguientes numerales.

A continuación, se presenta el detalle de cada nivel de actividad considerado,
el factor de emisión utilizado y las emisiones resultantes para la extensión de
la vida útil de la operación del proyecto.

**4.2** **Resuspensión de material por tránsito en camino no pavimentado**

**4.2.1** **Nivel de Actividad**

El tránsito de camiones por camino no pavimentado considera el transporte
de material desde la Cancha de Mineral al Área de Chancado y desde el Área
de Chancado al Área de Aglomerado.

Para realizar el traslado de material se requieren de camiones de capacidad
de 20 toneladas efectivas, por lo que la cantidad de viajes necesario para
transportar las 260.000 t/año de material considerado corresponden a 13.000
viajes al año.

Por otra parte, se considera la operación de camiones aljibes, los cuales
transitarán por caminos no pavimentados haciendo 5 viajes diarios.

Los caminos por recorrer consideran una distancia de aproximada 0,77
kilómetros de camino no pavimentado para el ingreso del material al Área de
Chancado y de 0,18 kilómetros para el transporte al Área de Aglomerado, en
cada viaje realizado, tanto para la ida como para la vuelta. A continuación, en
la siguiente imagen se presentan los tramos de los caminos considerados.

28

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 4.1. Ubicación referencial de los caminos utilizados por el Proyecto.**

Fuente: Elaboración propia, 2021.

En base a lo anterior, a continuación, se presenta el nivel de actividad del
Tránsito por Camino no Pavimentado.

**Tabla 4.2. Nivel de actividad - Tránsito por camino no pavimentado**

|Actividad|Tramo|Material<br>[t/año]|Capacidad<br>del<br>camión<br>[t]|Viajes<br>anuales<br>(ida)|Largo<br>[km]|Nivel del<br>Actividad<br>ida y<br>vuelta<br>[km/año]|
|---|---|---|---|---|---|---|
|**Riego de**<br>**caminos**|Tramo 1|-|-|1.825|0,8|2.811|
|**Riego de**<br>**caminos**|Tramo 2|-|-|1.825|0,2|657|
|**Transporte**<br>**de mineral**|Tramo 1|260.000|20|13.000|0,8|20.020|
|**Transporte**<br>**de mineral**|Tramo 2|Tramo 2|Tramo 2|13.000|0,2|4.680|
|**Total**|**Tramo 1**|**260.000**|**20**|**14.825**|**0,8**|**22.831**|
|**Total**|**Tramo 2**|**Tramo 2**|**Tramo 2**|**14.825**|**0,2**|**5.337**|

Fuente: Elaboración propia, 2021.

29

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**4.2.2** **Factores de Emisión**

La emisión por este concepto se refiere a la resuspensión de material
particulado debido al tránsito de vehículos en caminos industriales no
pavimentados. Para esta actividad, de acuerdo con lo que se detalla en la
Reporte AP-42 Actualización de noviembre 2006, Capítulo 13, Sección 13.2.2,
página 13.2.2-4, se pueden distinguir dos factores de emisión, dependiendo
si se transita por un camino industrial, dominado por vehículos pesados, o uno
público, dominado por vehículos livianos. Para efectos de este proyecto, dadas
las rutas por utilizar, solo se considera la metodología para caminos
industriales, la que corresponde a la siguiente:

[ [g]

km ~~[]]~~

0,45

∗
~~(~~ [W]

2,72 ~~[)]~~

FE= k∗281,9 ∗ (12 [s] ~~[)]~~

a

Donde:

F.E: Factor de emisión [g/km]

k: Factor de escala según tamaño de partícula [adimensional], donde:

k MPS : 4,90

k MP10 : 1,50

k MP2,5 : 0,15

s: Contenido de finos en la superficie del camino [%]. Se considera un
10% [i] .

a: Constante adimensional que corresponde a 0,9 para el MP 10 y MP 2,5 y
0,7 para MPS

W: Peso promedio de la flota de 18 toneladas. Dado que el camino de ida
es el mismo para los viajes de vuelta, y dado que solo se considera un tipo de
vehículo predominante, se considera como peso promedio el promedio directo
entre el peso del camión vacío, es decir 8 [t], y el peso del camión lleno, es

i
RCA N°150/2011, Adenda 1, Anexo Estimación de Emisiones de MP 10 y Modelación de Calidad del
Aire Proyecto “Optimización de Disposición de Ripios de Lixiviación, Planta Taltal”, página 19.

30

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

decir 28 [t], con lo que resulta un peso promedio de la flota (W) de 18 [t].

En base a las fórmulas y los parámetros antes presentados, los factores de
emisión, para las distintas fracciones de material particulado, de la actividad
de tránsito por camino industrial no pavimentado, corresponden a los que se
presentan a continuación:

**Tabla 4.3. Factor de emisión - Tránsito por camino no pavimentado industrial**

|Material Particulado|Factor de emisión [kg/km]|
|---|---|
|MPS|2,723|
|MP10|0,804|
|MP2,5|0,080|

Fuente: Elaboración propia, 2021.

**4.2.3** **Emisiones**

Respecto a la mitigación, de acuerdo con el Reporte AP-42, Chapter 13,
Section 13.2.2 “Unpaved Roads”, la eficiencia global de control de polvo,
mediante humectación es posible una reducción entre 75 a 90% de las
emisiones de Material Particulado, dependiendo de las condiciones de
humedad del suelo. En este caso, dada la localización del proyecto, y dado el
número de veces que se humectara al suelo diariamente, las emisiones
asociadas a la circulación de un camión por caminos industriales no
pavimentados se estiman con un rango de eficiencia de la humectación de un
80%, tal cual se presentaron en el proyecto aprobado con la RCA No 150/2011.

Para lograr esta humectación se considera la humectación de caminos no
pavimentados mediante un camión aljibe con agua de mar, considerando una
frecuencia de 5 veces por día, con lo que se estima un consumo de 50 [m3/día]
de agua de mar.

En base a los factores de emisiones antes presentados, y en base al nivel del
proyecto, a continuación, se presentan las emisiones resultantes para la
fuente de resuspención de material particulado producto de la circulación por
caminos no pavimentados:

31

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Tabla 4.4. Emisiones resultantes -Resuspención por tránsito en camino no pavimentado**

|Tramo|Nivel de<br>actividad<br>[km/año]|Mitigación<br>[%]|Factor de Emisión<br>[kg/km]|Col5|Col6|Emisiones [t/año]|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Tramo**|**Nivel de**<br>**actividad**<br>**[km/año]**|**Mitigación**<br>**[%]**|**MPS**|**MP10**|**MP2,5**|**MPS**|**MP10**|**MP2,5**|
|**Tramo 1**|22.831|80|2,723|0,804|0,080|12,43|3,67|0,37|
|**Tramo 2**|5.337|80|2,723|0,804|0,080|2,91|0,86|0,09|
|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**15,34**|**4,53**|**0,45**|

Fuente: Elaboración propia, 2021.

**4.3** **Transferencia de Material**

**4.3.1** **Nivel de Actividad**

Las cargas y descargas proyectadas de material, dado el material que se
requiere transportar, corresponde 260.000 toneladas en diferentes zonas de
operación. En la siguiente tabla se presenta el nivel de actividad
correspondiente a las toneladas anuales a cargar y descargar por zona:

**Tabla 4.5. Nivel de actividad - Transferencia de material**

|Actividad|Fuente|Zona|Material<br>Anual<br>[t/año]|
|---|---|---|---|
|**Transferencias de**<br>**mineral**|Carga de Material|Cancha de mineral|260.000|
|**Transferencias de**<br>**mineral**|Descarga de Material|Área de chancado|260.000|
|**Transferencias de**<br>**mineral**|Carga de Material|Stock Pile|260.000|
|**Transferencias de**<br>**mineral**|Descarga de Material|Área de aglomerado|260.000|
|**Total**|**Total**|**Total**|1.040.000|

Fuente: Elaboración propia, 2021.

**4.3.2** **Factores de emisión**

La emisión por este concepto se refiere a la emisión de material particulado
debido a las actividades de carga y descarga de material. Su fórmula se
obtiene de la EPA (Environmental Protection Agency USA), Reporte AP-42
Actualización de noviembre 2006, Capítulo 13, Sección 13.2.4, página 13.2.44. Se expresa en unidades de kilogramos emitidos por toneladas de material
transferido [kg/t], ya sea mediante una carga o una descarga, tal como se

32

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

muestra en la siguiente formula:

1,3

FE=

k∗0,0016 [U]
(2

2,2 ~~[)]~~

( [M] 2

1,4, [kg/t]

2 ~~[)]~~

Donde:

FE: Factor de emisión, en kilogramos emitidos por cada tonelada de
material [kg/t]

k: Factor de escala según tamaño de partícula [adimensional], donde:

MPS: 0,740

MP 10 : 0,350

MP 2,5 : 0,053

U: Velocidad del viento promedio [m/s]. Utilizando las consideraciones
meteorológicas descritas en el informe “Servicio de monitoreo de
meteorología” Enami - Planta José Antonio Moreno, Tal- Tal”, presentada en
la RCA No 150/2011, la velocidad media del viento en la zona presenta un
valor de 2,2 [m/s].

M: Porcentaje de humedad del material 4 [%] [ii]

En base a las fórmulas y los parámetros antes presentados, los factores de
emisión para las distintas fracciones de material particulado, de la actividad
transferencia de material corresponden a los que se presentan a continuación:

ii
RCA N°150/2011, Adenda 1, Anexo Estimación de Emisiones MP 10 y Modelación de Calidad del Aire
Proyecto “Optimización de Disposición de Ripios de Lixiviación, Planta Taltal”, página 22.

33

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Tabla 4.6. Factor de emisión - Transferencia de material**

|Material Particulado|Factor de emisión [kg/t]|
|---|---|
|MPS|4,5E-04|
|MP10|2,1E-04|
|MP2,5|3,2E-05|

Fuente: Elaboración propia, 2021.

**4.3.3** **Emisiones**

En base a los factores de emisiones antes presentados, y en base al nivel de
actividad del proyecto, a continuación, se presentan las emisiones resultantes
para la fuente de transferencia de material particulado producto de las cargas
y descargas de material:

**Tabla 4.7. Emisiones resultantes - Transferencia de material**

|Fuente|Zona|Material<br>Anual<br>[t/año]|Factor de Emisión [kg/t]|Col5|Col6|Emisiones [t/año]|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Fuente**|**Zona**|**Material**<br>**Anual**<br>**[t/año]**|**MPS**|**MP10**|**MP2,5**|**MPS**|**MP10 **|**MP2,5 **|
|**Carga de**<br>**Material**|Cancha de<br>mineral|260.000|4,5E-04|2,1E-04|3,2E-05|0,12|0,06|0,01|
|**Descarga**<br>**de Material**|Área de<br>chancado|260.000|4,5E-04|2,1E-04|3,2E-05|0,12|0,06|0,01|
|**Carga de**<br>**Material**|Stock Pile|260.000|4,5E-04|2,1E-04|3,2E-05|0,12|0,06|0,01|
|**Descarga**<br>**de Material**|Área de<br>aglomerado|260.000|4,5E04|2,1E-04|3,2E-05|0,12|0,06|0,01|
|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**0,47**|**0,22**|**0,03**|

Fuente: Elaboración propia, 2021.

**4.4** **Procesamiento de Material**

**4.4.1** **Nivel de Actividad**

Se consideran actividades de procesamiento de material a las que
corresponden a las de chancado primario, chancado secundario, clasificación
(tamizado) y transferencia en correas transportadoras.

El procesamiento proyectado de material corresponde 260.000 toneladas para
cada uno de los procesos, con excepción de la transferencia en correas
transportadoras, que se multiplica por el número de puntos de traspasos entre

34

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

correas. En la siguiente tabla se presenta el nivel de actividad
correspondiente:

**Tabla 4.8. Nivel de actividad - Procesamiento de Material**

|Actividad|Fuente|Zona|Material Anual<br>[t/año]|
|---|---|---|---|
|**Procesamiento**<br>**de material**|Chancado Primario|Zona de<br>Chancado|260.000|
|**Procesamiento**<br>**de material**|Chancado Secundario|Chancado Secundario|260.000|
|**Procesamiento**<br>**de material**|Clasificación de material<br>(tamizado grueso)|Clasificación de material<br>(tamizado grueso)|260.000|
|**Procesamiento**<br>**de material**|Clasificación de material<br>(tamizado fino)|Clasificación de material<br>(tamizado fino)|260.000|
|**Procesamiento**<br>**de material**|Transferencia entre correas<br>transportadoras|Transferencia entre correas<br>transportadoras|1.300.000|

Fuente: Elaboración propia, 2021.

**4.4.2** **Factores de Emisión**

La emisión por este concepto se refiere a la emisión de material particulado
debido a las actividades de procesamiento de material. Su fórmula se obtiene
de la EPA (Environmental Protection Agency USA), Reporte AP-42
Actualización de noviembre 2006, Capítulo 11, Sección 11.19.2, tabla 11.19.21 Emission Factors For Crushed Stone Processing Operations y en base a la
Guía RM 2020. Los factores considerados para los distintos procesos se
presentan en la siguiente tabla:

**Tabla 4.9. Factor de Emisión - Procesamiento de Material**

|Actividad|Factor de Emisión<br>[kg/t]|Col3|Col4|
|---|---|---|---|
|**Actividad**|**MPS**|**MP10**|**MP2,5**|
|Chancado primario (con supresión húmeda)|0,0006|0,0003|0,0001|
|Chancado secundario (con supresión húmeda)|0,0006|0,0003|0,0001|
|Tamizado grueso (con supresión húmeda)|0,0011|0,0004|0,0000|
|Tamizado fino (con supresión húmeda)|0,0018|0,0011|0,0002|
|Punto de transferencia entre correas|0,0015|0,0006|0,0002|

Fuente: Elaboración propia, 2021.

**4.4.3** **Emisiones**

En base a los factores de emisiones antes presentados, y en base al nivel de

35

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

actividad del proyecto, a continuación, se presentan las emisiones resultantes
para la fuente de procesamiento de material:

**Tabla 4.10. Emisiones resultantes - Procesamiento de material**

|Actividad|Fuente|Zona|Material<br>Anual<br>[t/año]|Factor de Emisión [kg/t]|Col6|Col7|Emisiones [t/año]|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Fuente**|**Zona**|**Material**<br>**Anual**<br>**[t/año]**|**MPS**|**MP10**|**MP2,5**|**MPS**|**MP10 **|**MP2,5 **|
|**Procesamiento de material**|Chancado<br>Primario|Zona<br>de chancado|260.000|0,0006|0,0003|0,0001|0,156|0,070|0,013|
|**Procesamiento de material**|Chancado<br>Secundario|Chancado<br>Secundario|260.000|0,0006|0,0003|0,0001|0,156|0,070|0,013|
|**Procesamiento de material**|Clasificación de<br>material<br>(tamizado<br>grueso)|Clasificación de<br>material<br>(tamizado<br>grueso)|260.000|0,0011|0,0004|0,0000|0,286|0,096|0,007|
|**Procesamiento de material**|Clasificación de<br>material<br>(tamizado fino)|Clasificación de<br>material<br>(tamizado fino)|260.000|0,0018|0,0011|0,0002|0,468|0,286|0,043|
|**Procesamiento de material**|Transferencia<br>entre correas<br>transportadoras|Transferencia<br>entre correas<br>transportadoras|260.000|0,0015|0,0006|0,0002|1,950|0,715|0,202|
|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**3,02**|**0,24**|**0,03**|

Fuente: Elaboración propia, 2021.

**4.5** **Combustión interna de maquinaria**

**4.5.1** **Nivel de Actividad**

Para la estimación de las emisiones de gases y material particulado se
consideró la operación de maquinarias correspondiente a cargadores frontales
(2), los cuales cargarán el material en la Cancha de Material, que será llevado
al Área de Chancado, mientras que el segundo cargará el material en el Stock
Pile, que posteriormente será llevado al Área de Aglomerado. Esta maquinaria
considera una operación diaria de 12 horas, como escenario conservador. El
nivel de actividad resultante se presenta en la siguiente tabla:

**Tabla 4.11. Nivel de actividad - combustión interna de maquinaria**

|Actividad|Maquinaria|N° de<br>maquinarias|Horas<br>diarias|Días a<br>mes|Meses<br>al año|Potencia<br>[kw]|Nivel de<br>actividad<br>[h-kw/año]|
|---|---|---|---|---|---|---|---|
|**Carga de**<br>**Material**|Cargador<br>Frontal|2|12|25|12|138|993.600|

Fuente: Elaboración propia, 2021.

36

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**4.5.2** **Factores de Emisión**

Como los factores de emisión de los motores de maquinaria están en función
de la potencia, se utilizará para su estimación la tabla “Factor de emisión en
función de la potencia” contenida en la Guía para la Estimación de Emisiones
Atmosféricas de la RM. El factor utilizado corresponde al siguiente:

**Tabla 4.12. Factor de emisión - Combustión interna de maquinaria**

|Actividad|Factor de Emisión [kg/kw-h]|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Actividad**|**MPS**|**MP10**|**MP2,5**|**NOX **|**SO2 **|**CO**|**HC**|
|Cargador Frontal|0,0011|0,0011|0,0011|0,0144|0,00002|0,0030|0,0014|

Fuente: Elaboración propia, 2021.

Cabe destacar que, el factor de carga considerado corresponde al 100%, como
escenario más desfavorable.

**4.5.3** **Emisiones**

En base a los factores de emisiones antes presentados, y en base al nivel de
actividad del proyecto, a continuación, se presentan las emisiones resultantes
para la fuente de combustión de maquinaria:

**Tabla 4.13. Emisiones Resultantes - Combustión interna de maquinaria**

|Actividad|Nivel de<br>Actividad<br>[h-kw/año]|Emisiones [t/año]|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Nivel de**<br>**Actividad**<br>**[h-kw/año]**|**MPS**|**MP10**|**MP2,5**|**NOX **|**SO2 **|**CO**|**HC**|
|Cargador<br>Frontal|993.600|1,09|1,09|1,09|14,27|0,02|2,98|1,34|

Fuente: Elaboración propia, 2021.

**4.6** **Combustión interna de vehículos**

**4.6.1** **Nivel de Actividad**

Para la estimación de las emisiones de gases y material particulado de los
vehículos del proyecto se consideró la misma operación considerada en
tránsito por camino no pavimentado. El nivel de actividad resultante para la
operación se presenta en la siguiente tabla:

37

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Tabla 4.14. Nivel de actividad - Combustión interna de vehículos**

|Actividad|Tramo|Material<br>[t/año]|Capacidad<br>del<br>camión<br>[t]|Viajes<br>anuales<br>(ida)|Largo<br>[km]|Nivel del<br>Actividad<br>ida y<br>vuelta<br>[km/año]|
|---|---|---|---|---|---|---|
|**Riego de**<br>**caminos**|Tramo 1|-|-|1.825|0,8|2.811|
|**Riego de**<br>**caminos**|Tramo 2|-|-|1.825|0,2|657|
|**Transporte**<br>**de mineral**|Tramo 1|260.000|20|13.000|0,8|20.020|
|**Transporte**<br>**de mineral**|Tramo 2|Tramo 2|Tramo 2|13.000|0,2|4.680|
|**Total**|**Tramo 1**|**260.000**|**20**|**14.825**|**0,8**|**22.831**|
|**Total**|**Tramo 2**|**Tramo 2**|**Tramo 2**|**14.825**|**0,2**|**5.337**|

Fuente: Elaboración propia, 2021.

**4.6.2** **Factores de emisión**

La estimación de las emisiones atmosféricas producto de la combustión interna
de los vehículos depende de la categoría vehicular, del tipo de combustible y
cilindrada, y de la normativa de emisiones o tecnología considerada por el
fabricante y considerada por el proyecto. Dado lo anterior, a continuación, se
presentan los factores de emisión considerados por el proyecto:

**Tabla 4.15. Factor de emisión - Combustión interna de vehículos [g/km]**

|Tipo de<br>vehículo|Factor de Emisión [g/km]|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Tipo de**<br>**vehículo**|**MPS**|**MP10**|**MP2,5**|**NOX **|**SO2 **|**CO**|**COV**|
|Pesados - Diésel<br>16 - 32 [t] - Euro<br>IV - 2005|0,13|0,13|0,13|6,27|0,0063|0,149|0,278|

Fuente: Guía para la Estimación de Emisiones Atmosféricas de la Región Metropolitana (2020,

SEA).

Para estimar el MPS se ha asumido de forma conservadora su factor de

emisión es igual al del MP 10 y al MP 2,5, entregados por la Guía para la
Estimación de Emisiones Atmosféricas de la Región Metropolitana (2020,
SEA).

**4.6.3** **Emisiones**

En base a los factores de emisiones antes presentados, y en base al nivel de
actividad de proyecto, a continuación, se presentan las emisiones resultantes

38

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

para la fuente de combustión interna de vehículos:

**Tabla 4.16. Emisiones resultantes - Combustión interna de vehículos**

|Camino|Nivel de<br>Actividad<br>[km/año]|Emisiones [t/año]|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Camino**|**Nivel de**<br>**Actividad**<br>**[km/año]**|**MPS**|**MP10**|**MP2,5**|**NOX **|**SO2 **|**CO**|**HC**|
|Tramo 1|43.882|0,0030|0,0030|0,0030|0,1431|0,0001|0,0034|0,0063|
|Tramo 2|35.616|0,0007|0,0007|0,0007|0,0335|0,0000|0,0008|0,0015|
|**Total**|**Total**|**0,004**|**0,004**|**0,004**|**0,177**|**0,000**|**0,004**|**0,008**|

Fuente: Elaboración propia, 2021.

**4.7** **Erosión de material en pila**

**4.7.1** **Nivel de Actividad**

Se considera un proceso de erosión eólica en pila de acopio en la Cancha de
Material, que está a la espera de ser llevado al Área de Chancado, mientras
que, también se considera un proceso de erosión eólica en pila de acopio, una
vez se haya chancado el material, el que está a la espera de ser llevado al
Área de Aglomeración. Las áreas de acopio y niveles de actividad resultantes
se presentan en la siguiente tabla:

**Tabla 4.17. Nivel de actividad - Erosión de material en pila**

|Zona|Superficie|Col3|Días de exposición al año|Nivel de actividad[ha-<br>días/año]|
|---|---|---|---|---|
|**Zona**|**[m2] **|**[ha]**|**[ha]**|**[ha]**|
|**Stock Pile**|1.200|0,12|365|43,8|
|**Cancha de mineral**|2.000|0,20|365|73,0|

Fuente: Elaboración propia, 2021.

**4.7.2** **Factores de emisión**

La emisión por este concepto se refiere a la emisión de material particulado
debido a las actividades de erosión de material en pila por la acción del viento.
La fuente de esta fórmula, y los parámetros asociados, corresponde a la Guía
para la Estimación de Emisiones Atmosféricas de la Región Metropolitana,
SEREMI de Medio Ambiente de la Región Metropolitana, la que se basa en el
documento WRAP (Western Regional Air Partnership) “Storage Pile Wind
Erosion” y corresponde a la que se presenta a continuación:

39

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

1,5 [s] [) ∗] ~~[( ]~~ [f]

FE= k∗
~~(~~ [s]

kg
15 [f] [) ∗ [] ha −día ~~[]]~~

Donde:

FE: Factor de emisión, en kilogramos emitidos por hectárea día expuesta
al año

k: Factor de escala según tamaño de partícula [adimensional], donde:

MPS: 1,90

MP 10 : 0,95

MP 2,5 : 0,14

s: Contenido de finos del material expuesto es de 10 [%].

f: Porcentaje [%] del tiempo en que el viento excede los 5,4 [m/s]. Cabe
destacar que, de acuerdo con los datos de la estación meteorológica, el tiempo
donde los vientos superan los 5,4 m/s es cercano a 0 [%], pero como
escenario más conservador se considera 5 [%].

En base a las fórmulas y los parámetros antes presentados, los factores de
emisión para las distintas fracciones de material particulado, de la actividad
transferencia de material corresponden a los que se presentan a continuación:

**Tabla 4.18. Factor de emisión - Erosión de material en pila**

|Material Particulado|Factor de emisión [kg/ha]|
|---|---|
|MPS|4,22|
|MP10|2,11|
|MP2,5<br>|0,31<br>|

Fuente: Elaboración propia, 2021.

**4.7.3** **Emisiones**

En base a los factores de emisiones antes presentados, y en base al nivel de
actividad del proyecto, a continuación, se presentan las emisiones resultantes
para la fuente de erosión de material en pila, producto del acopio de material:

40

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Tabla 4.19. Emisiones resultantes - Erosión de material en pila**

|Fuente|Zona|Superficie<br>expuesta al<br>año[ha-<br>día/año]|Factor de Emisión [kg/ha-<br>día]|Col5|Col6|Emisiones [t/año]|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Fuente**|**Zona**|**Superficie**<br>**expuesta al**<br>**año[ha-**<br>**día/año]**|**MPS**|**MP10**|**MP2,5**|**MPS**|**MP10 **|**MP2,5 **|
|**Erosión**<br>**de**<br>**material**<br>**en pila**|**Stock**<br>**Pile**|43,8|4,22|2,11|0,31|0,18|0,09|0,01|
|**Erosión**<br>**de**<br>**material**<br>**en pila**|**Cancha de**<br>**mineral**|73,0|4,22|2,11|0,31|0,31|0,15|0,02|
|**Total**|**Total**|**Total**|**Total**|**Total**|**Total**|**0,39**|**0,19**|**0,03**|

Fuente: Elaboración propia, 2021.

**4.8** **Resumen de Emisiones**

En base a los factores de emisiones antes presentados, el nivel de actividad
del proyecto, a continuación, se presenta un resumen de las emisiones
resultantes por actividad:

**Tabla 4.20. Emisiones resultantes**

|Actividad|Emisiones [t/año]|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Actividad**|**MPS**|**MP10**|**MP2,5**|**NOX **|**SO2 **|**CO**|**HC/C**<br>**OV**|
|Vehículos en caminos<br>industriales NO<br>pavimentados|15,34|4,53|0,45|0,00|0,00|0,00|0,00|
|Transferencia de material|0,47|0,22|0,03|0,00|0,00|0,00|0,00|
|Procesamiento de<br>material|3,02|1,33|0,36|0,00|0,00|0,00|0,00|
|Motor maquinaria|1,09|1,09|1,09|14,27|0,02|2,98|1,34|
|Motor vehículos pesados|0,00|0,00|0,00|0,18|0,00|0,00|0,01|
|Erosión de material en<br>pila|0,49|0,25|0,04|0,00|0,00|0,00|0,00|
|**Total**|**20,41**|**7,42**|**1,98**|**14,44**|**0,02**|**2,98**|**1,35**|

Fuente: Elaboración propia, 2021.

**5** **MODELACIÓN ATMOSFÉRICA**

**5.1** **Características del Modelo**

La modelación atmosférica permitirá evaluar el aporte de material particulado
respirable (MP 10 ), material particulado respirable fino (MP 2,5 ), material
particulado sedimentable (MPS), dióxido de azufre (SO 2 ), dióxido de nitrógeno
(NO 2 ) y monóxido de carbono (CO).

41

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

Los aportes de las fuentes de emisión de un Proyecto específico sobre la
población son inherentes a la responsabilidad que cada Proyecto tiene sobre
su entorno. Por ello, es determinante evidenciar los niveles de calidad del aire
a partir de la aplicación de modelos de dispersión atmosférica que posibiliten
identificar el aporte de las emisiones provenientes de distintos tipos de fuentes
emisoras, sean estas: puntuales, areales, lineales y/o volumétricas.

Los modelos lagrangeanos, se caracterizan por hacer uso de un sistema de
referencia que se ajusta al movimiento atmosférico. Es decir, las emisiones,
reacciones, deposición y mezclado de los contaminantes se analizan para un
volumen de aire que va cambiando su posición de acuerdo con la velocidad y
dirección del viento. Bajo este esquema general, los modelos lagrangeanos se
pueden clasificar como modelos de trayectoria que simulan los procesos para
una columna hipotética de aire.

Los modelos gaussianos describen el transporte y mezcla de los contaminantes
asumiendo que las emisiones presentan, en las direcciones horizontal y
vertical, una distribución normal o de curva gaussiana con una concentración
máxima en el centro de la pluma. Generalmente estos modelos se aplican para
evaluar la dispersión de contaminantes provenientes de fuentes puntuales,
aunque también se aplican para simular emisiones de fuentes de área y de
línea. Otra característica de este tipo de modelos es que normalmente son
aplicados para evaluar la dispersión de contaminantes primarios no reactivos,
aunque existen versiones que incluyen en su formulación consideraciones
especiales para poder simular procesos de deposición y transformación
química.

Los modelos tipo puff, se comportan como una mezcla entre los modelos
lagrangeanos y gaussianos, debido a que completa ambas metodologías a
través de un “puff” variable en el tiempo (no estacionario); un ejemplo de ello
es el sistema de modelación Calpuff.

El modelo utilizado para determinar el efecto que tendrán las emisiones de
material particulado y gases provenientes de la Fases de operación de la Planta
de Chancado del Proyecto, corresponde al sistema de modelación “CALPUFF”
desarrollado por EarthTech, con los datos provenientes de WRF utilizados

directamente en CALPUFF.

En este modelo las emisiones se tratan como “puffs”, que se van desplazando

42

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

a través de un campo meteorológico tridimensional.

El sistema de modelación CALPUFF es utilizado en el presente Proyecto
incluyendo los siguientes componentes: WRF, CALPUFF y CALPOST.

WRF es un modelo de pronóstico meteorológico que simula campos de viento
y temperatura en un dominio de modelación engrillado y tridimensional,
produce campos en dos-dimensiones como altura de mezcla, características
de superficie y propiedades de dispersión.

CALPUFF modela el transporte y dispersión de contaminantes emitidos por las
fuentes emisoras en forma de paquetes o “PUFF” de material procesándolos a
través del dominio de modelación. La salida primaria de este modelo contiene
cada hora de concentración o flujo de deposición evaluados en receptores
determinados, además el modelo CALPUFF, ha sido recomendado por EPA y
por la “Guía para el uso de modelos de calidad del aire en el SEIA” del año
2012, aplicable a terrenos complejos y a múltiples tipos de fuentes emisoras
(puntuales, areales y volumétricas), que realiza sus cálculos tomando los
datos meteorológicos superficiales y de la capa superior atmosférica (WRF),
incluyendo la opción de simular la dispersión de contaminantes tanto primarios

como secundarios.

Cabe señalar que el modelo CALPUFF, modela un conjunto de fuentes
emisoras, entregando como resultados concentraciones de cada parámetro
considerado, en cada punto de grilla, como en cada receptor puntual que sea
evaluado, no permitiendo determinar el aporte de cada fuente sobre cada
receptor, debido a que la base del modelo se enfoca en los aportes de un
conjunto de fuentes emisoras, en forma sistémica sobre campos de viento
dinámicos que logran representar la recirculación de la meteorología local.

CALPOST procesa las salidas de CALPUFF creando los archivos con las
tabulaciones necesarias para la evaluación de resultados.

Es preciso señalar que, para mayor detalle, se presenta en Apéndice 1 del
presente informe los archivos digitales de Modelación, entre los cuales se
presenta el modelo meteorológico WRF, los archivos de entrada y salida de
dispersión “CALPUFF” y los archivos de resultados de cada parámetro

analizado “CALPOST”.

43

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**5.2** **Variables de entrada al sistema de modelación**

El sistema de modelación WRF-CALPUFF requiere de la siguiente data de

entrada:

 Archivos FNL. Datos de entrada para el modelo de dispersión WRF.

 - Uso de Suelo. A partir de estos datos de definen los coeficientes de

rugosidad superficial, razón de Bowen y albedo. En la Tabla 5.1 se
presentan las características de suelo. En la Figura 5.2 se observan los
distintos tipos de uso de suelo presentes en el área del Proyecto.

**Tabla 5.1. Características del uso de suelo**

|Parámetro|Uso de Suelo|Col3|Col4|
|---|---|---|---|
|**Parámetro**|**Pastizales**|**Tierra Estéril**|**Mar**|
|Rugosidad Superficial|0,05|0,05|0,001|
|Albedoiii|0,25|0,30|0,10|
|Razón de Boweniv|1,0|1,0|0,0|

Fuente: Elaboración Propia 2020, en base a Tabla 4-45, Guía de usuario CALMET, Uso de Suelo y

Parámetros Geofísicos.

 Emisiones Atmosféricas corresponden a las emisiones máximas anuales

por fuente emisora y contaminante. En la Figura 5.3 se presentan las
fuentes de emisión

 Ubicación de puntos de interés. La Tabla 5.2 presenta las coordenadas

de localización de los puntos de interés considerados en el presente
informe. En la Figura 1.1 se presenta la ubicación de los puntos de
interés.

iii Albedo: reflectividad a la luz solar del suelo (expresada como fracción respecto a la unidad)

iv Razón de Bowen: definida como la razón entre flujos sensibles y latentes, a nivel de superficie.

44

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 5.1. Imagen referencia tridimensional del terreno.**

Fuente: Elaboración propia, 2021.

45

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 5.2. Usos del suelo**

Fuente: Elaboración propia, 2021.

46

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 5.3. Fuentes de Emisión**

Fuente: Elaboración propia, 2021.

47

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

 Ubicación de puntos de interés. La siguiente Tabla presenta las

coordenadas de localización de los puntos de interés considerados en el
presente informe, donde se presentan los primeros 3 receptores para
normativa primaria (R1 al R3) y los siguientes 7 receptores (R4 al R10),
para efecto de análisis de normativa secundaria, específicamente para
MPS y SO 2 .

**Tabla 5.2.** **Localización puntos discretos** **[v]**

|ID|Punto de Interés|Distancia de Área<br>de Proyecto (km)|Este (m)|Norte (m)|
|---|---|---|---|---|
|R1|Estación Taltal (Población Eduardo Vigil)|1,53|351.932|7.190.064|
|R2|Escuela Alondra Rojas|1,92|351.604|7.189.859|
|R3|Playa Muelle de Piedra|0,27|353.262|7.191.602|
|R4|Olivicultores 1 (MPS_1)|1,82|353.705|7.189.037|
|R5|Olivicultores 2 (MPS_2)|1,88|353.660|7.188.965|
|R6|Olivicultores 3 (MPS_3)|1,85|353.748|7.189.019|
|R7|Olivicultores 4 (MPS_4)|1,94|353.697|7.188.917|
|R8|Olivicultores 5 (MPS_5)|1,91|353.744|7.188.960|
|R9|Olivicultores 6 (MPS_6)|1,98|353.718|7.188.881|
|R10|Olivicultores 7 (MPS_7)|1,93|353.795|7.188.947|

Fuente: Elaboración Propia en base a información entregada por el Titular.

**5.3** **Resultados de la Modelación**

**5.3.1** **Modelación WRF**

Mediante la aplicación del modelo WRF fue posible simular el comportamiento
de los campos de vientos sobre el área de influencia del Proyecto, para cada
una de las horas consideradas en la modelación. Dichos campos de vientos
permitirán determinar posteriormente la dispersión de los contaminantes, a
través de la aplicación del modelo CALPUFF.

A modo de ejemplo, se seleccionó el día 7 de diciembre de 2019, donde se
produce el percentil 98 de MP10 para la Fase de Operación de la Planta de

v Datum WGS84, coordenadas UTM.

48

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

Chancado; para representar el comportamiento de los vientos superficiales en
horas representativas del día, en la madrugada (06:00 horas), a medio día
(12:00 horas), durante la tarde (18:00 horas) y en la noche (00:00 horas).

**Figura 5.4. Campos de viento a las 06:00 horas**

Fuente: Elaboración propia, 2021.

49

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 5.5. Campos de viento a las 12:00 horas**

Fuente: Elaboración propia, 2021.

50

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 5.6. Campos de viento a las 18:00 horas**

Fuente: Elaboración propia, 2021.

51

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 5.7. Campos de viento a las 00:00 horas**

Fuente: Elaboración propia, 2021.

**5.3.2** **Aportes obtenidos en la Modelación**

Mediante la aplicación del modelo CALPUFF, fue posible obtener las
concentraciones de material particulado y gases que aportará el Proyecto en
su Fase de Operación de la Planta de Chancado, basándose en los campos de

52

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

vientos generados por la modelación meteorológica realizada con WRF.

Las siguientes Tablas presentan el resumen de las concentraciones resultantes
de la modelación en los puntos de interés, en las estaciones de monitoreo y
en el punto de máximo impacto (punto dentro del área de modelación donde
se producen las máximas concentraciones de cada contaminante), para el

escenario evaluado.

Cabe señalar que los aportes han sido presentados para ambos escenarios
tanto en su condición inicial, como corregidos por su factor de corrección, el
cual fue presentado en el acápite 3.4 “Análisis de Incertidumbre” del presente

documento.

A continuación, son presentados los puntos de interés evaluados:

Receptores de material particulado respirable (MP 10 y MP 2,5 ), material
particulado sedimentable (MPS) y gases (SO 2, NO X y CO):

 R1; Estación Taltal (estación de monitoreo calidad del aire, Población

Eduardo Vigil)

 R2; Escuela Alondra Rojas (receptor cercano a población)

 R3; Playa Muelle de Piedra (receptor cercano a población)

 R4; Olivicultores 1 (MPS_1) (receptor de norma secundaria)

 R5; Olivicultores 2 (MPS_2) (receptor de norma secundaria)

 R6; Olivicultores 3 (MPS_3) (receptor de norma secundaria)

 R7; Olivicultores 4 (MPS_4) (receptor de norma secundaria)

 R8; Olivicultores 5 (MPS_5) (receptor de norma secundaria)

 R9; Olivicultores 6 (MPS_6) (receptor de norma secundaria)

 R10; Olivicultores 7 (MPS_7) (receptor de norma secundaria)

 Punto de Máxima Concentración, en adelante PMC.

53

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Tabla 5.3. Aportes del Proyecto en puntos de interés y puntos de máxima concentración (PMC) “Fase de Operación Planta**

**de Chancado [μg/m** **[3]** **]” Sin Factor de Corrección**

|Receptores|MP<br>10|Col3|MP<br>2,5|Col5|CO|Col7|NO<br>2|Col9|SO<br>2|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptores**|**Norma Primaria**|**Norma Primaria**|**Norma Primaria**|**Norma Primaria**|**Norma**<br>**Primaria**|**Norma**<br>**Primaria**|**Norma Primaria**|**Norma Primaria**|**Norma Primaria**|**Norma Primaria**|**Norma Primaria**|
|**Receptores**|**Promedio**<br>**Anual**|**P98**<br>**diario**|**Promedio**<br>**Anual**|**P98**<br>**diario**|**P99**<br>**horario**|**P99**<br>**8 **<br>**horas**|**Promedio**<br>**Anual**|**P99**<br>**horario**|**Promedio**<br>**Anual**|**P99**<br>**diario**|**P98,5**<br>**horario**|
|R1|0,04|0,13|0,01|0,04|0,36|0,13|0,09|2,61|0,0001|0,0003|0,0007|
|R2|0,03|0,12|0,01|0,04|0,30|0,11|0,08|1,95|0,0001|0,0003|0,0006|
|R3|0,10|0,38|0,03|0,12|2,00|0,49|0,26|10,47|0,0003|0,0011|0,0029|
|PMC|0,83|5,11|0,27|1,06|12,24|3,73|1,48|55,26|0,0019|0,0077|0,0321|

Fuente: Elaboración propia, 2021.

**Tabla 5.4. Aportes del Proyecto de MPS y SO** **2** **(Norma Secundaria) en puntos de interés y punto de máxima concentración**

**(PMC) “Fase de Operación Planta de Chancado” Sin Factor de Corrección**

|Receptores|MPS (Norma Secundaria)<br>[mg/m2-día]|Col3|SO (Norma Secundaria)<br>2<br>[ug/m3]|Col5|Col6|
|---|---|---|---|---|---|
|**Receptores**|**Promedio**<br>**Anual**|**Promedio**<br>**Mensual**|**Promedio**<br>**Anual**|**P99,7**<br>**diario**|**P99,73**<br>**horario**|
|R4|0,0012|0,0027|0,0002|0,0009|0,0025|
|R5|0,0012|0,0025|0,0002|0,0009|0,0024|
|R6|0,0012|0,0026|0,0002|0,0008|0,0023|
|R7|0,0011|0,0023|0,0001|0,0008|0,0022|
|R8|0,0011|0,0024|0,0001|0,0008|0,0022|
|R9|0,0010|0,0022|0,0001|0,0008|0,0020|
|R10|0,0011|0,0023|0,0001|0,0008|0,0021|
|PMC|0,0096|0,0163|0,0019|0,0091|0,0569|

Fuente: Elaboración propia, 2021.

54

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Tabla 5.5. Aportes del Proyecto en puntos de interés y puntos de máxima concentración (PMC) “Fase de Operación Planta**

**de Chancado [μg/m** **[3]** **]” Con Factor de Corrección**

|Receptores|MP<br>10|Col3|MP<br>2,5|Col5|CO|Col7|NO<br>2|Col9|SO<br>2|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptores**|**Norma Primaria**|**Norma Primaria**|**Norma Primaria**|**Norma Primaria**|**Norma**<br>**Primaria**|**Norma**<br>**Primaria**|**Norma Primaria**|**Norma Primaria**|**Norma Primaria**|**Norma Primaria**|**Norma Primaria**|
|**Receptores**|**Promedio**<br>**Anual**|**P98**<br>**diario**|**Promedio**<br>**Anual**|**P98**<br>**diario**|**P99**<br>**horario**|**P99**<br>**8 **<br>**horas**|**Promedio**<br>**Anual**|**P99**<br>**horario**|**Promedio**<br>**Anual**|**P99**<br>**diario**|**P98,5**<br>**horario**|
|R1|0,04|0,15|0,01|0,05|0,41|0,14|0,10|2,92|0,0001|0,0004|0,0008|
|R2|0,03|0,13|0,01|0,04|0,33|0,12|0,09|2,19|0,0001|0,0003|0,0007|
|R3|0,11|0,43|0,03|0,13|2,24|0,55|0,29|11,73|0,0003|0,0012|0,0033|
|PMC|0,93|5,72|0,30|1,19|13,71|4,18|1,65|61,89|0,0022|0,0086|0,0360|

Fuente: Elaboración propia, 2021.

**Tabla 5.6. Aportes del Proyecto de MPS y SO** **2** **(Norma Secundaria) en puntos de interés y punto de máxima concentración**

**(PMC) “Fase de Operación Planta de Chancado” Con Factor de Corrección**

|Receptores|MPS (Norma Secundaria)<br>[mg/m2-día]|Col3|SO (Norma Secundaria)<br>2<br>[ug/m3]|Col5|Col6|
|---|---|---|---|---|---|
|**Receptores**|**Promedio**<br>**Anual**|**Promedio**<br>**Mensual**|**Promedio**<br>**Anual**|**P99,7**<br>**diario**|**P99,73**<br>**horario**|
|R4|0,0014|0,0030|0,0002|0,0010|0,0028|
|R5|0,0013|0,0028|0,0002|0,0010|0,0027|
|R6|0,0013|0,0029|0,0002|0,0009|0,0026|
|R7|0,0012|0,0026|0,0002|0,0009|0,0024|
|R8|0,0012|0,0027|0,0002|0,0009|0,0024|
|R9|0,0012|0,0025|0,0002|0,0009|0,0022|
|R10|0,0012|0,0026|0,0002|0,0008|0,0023|
|PMC|0,0107|0,0182|0,0022|0,0102|0,0638|

Fuente: Elaboración propia, 2021.

55

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**5.4** **Ubicación Punto de máxima concentración**

La siguiente Tabla presenta la ubicación del Punto de Máxima Concentración
(PMC), tanto para el material particulado como para los gases, para el

escenario analizado.

Cabe señalar que las coordenadas se presentan en Proyección UTM Datum
WGS 84, Huso 19S.

**Tabla 5.7. Coordenadas de localización punto de máxima concentración (PMC) "Fase de**

**Operación Planta de Chancado"**

|Parámetro|Tipo de<br>Norma|Estadístico|Este (m)|Norte (m)|ID|
|---|---|---|---|---|---|
|MP10|Primaria|Promedio Anual|354.038|7.190.687|PMC1|
|MP10|Primaria|Percentil 98 Diario|354.038|7.190.687|PMC1|
|MP2,5|Primaria|Promedio Anual|354.038|7.190.687|PMC1|
|MP2,5|Primaria|Percentil 98 Diario|354.038|7.190.687|PMC1|
|MPS|Secundaria|Promedio Anual|354.038|7.190.687|PMC1|
|MPS|Secundaria|Promedio Mensual|354.038|7.190.687|PMC1|
|CO|Primaria|Percentil 99 Horario|354.038|7.190.687|PMC1|
|CO|Primaria|Percentil 99 8 horas.|354.038|7.190.687|PMC1|
|NO2|Primaria|Promedio del Anual|354.038|7.190.687|PMC1|
|NO2|Primaria|Percentil 99 Horario|354.038|7.190.687|PMC1|
|SO2|Primaria|Promedio del Anual|354.038|7.190.687|PMC1|
|SO2|Primaria|Percentil 99 Diario|354.038|7.190.687|PMC1|
|SO2|Primaria|Percentil 98,5 horario|354.038|7.190.687|PMC1|
|SO2|Secundaria|Promedio del Anual|354.038|7.190.687|PMC1|
|SO2|Secundaria|Percentil 99,7 Diario|354.038|7.190.687|PMC1|
|SO2|Secundaria|Percentil 99,73 Horario|354.038|7.190.687|PMC1|

Fuente: Elaboración propia, 2021.

En la siguiente imagen se observa la ubicación espacial del punto de máxima
concentración (PMC) en el área de modelación.

56

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 5.8. Ubicación puntos de máxima concentración "Fase de Operación Planta de Chancado"**

Fuente: Elaboración propia, 2021.

57

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**6** **APORTE DE OTROS PROYECTOS - EVALUACIÓN DEL EFECTO**
**SINÉRGICO**

La evaluación del efecto sinérgico no ha sido factible dado que se ha
establecido que en las inmediaciones del presente Proyecto no existen aportes
adicionales, a las emisiones generadas por el Proyecto, dado que no hay
proyectos que se encuentren aprobados y que no se estén ejecutando
actualmente, por lo que no se consideran aportes de terceros para el análisis
del cumplimiento normativo.

**7** **ANÁLISIS DE CUMPLIMIENTO DE NORMATIVA AMBIETNAL**

Para establecer el cumplimiento de la normativa ambiental vigente de calidad
del aire, bajo un escenario conservador, se sumarán los aportes modelados
sobre los receptores cercanos, a los valores monitoreados por la Estación
Taltal durante el periodo correspondiente a los años 2019 - 2020.

**Tabla 7.1. Análisis de cumplimiento de normativa vigente para MP** **10** **“Fase de Operación**

**Planta de Chancado” [μg/m** **[3]** **]**

|Parámetro|Tipo de<br>Norma|Estadístico|Receptores|Norma|(LB)|%<br>(LB)<br>c/r<br>Norma|(AP)|(AP+LB)|(AP+LB)<br>c/r a<br>(LB)|
|---|---|---|---|---|---|---|---|---|---|
|MP10|Primaria|Promedio<br>Anual|R1|50|16,3|33%|0,04|16,29|33%|
|MP10|Primaria|Promedio<br>Anual|R2|50|16,3|33%|0,03|16,28|33%|
|MP10|Primaria|Promedio<br>Anual|R3|50|16,3|33%|0,11|16,36|33%|
|MP10|Primaria|P98 diario|R1|150|28,6|19%|0,15|28,70|19%|
|MP10|Primaria|P98 diario|R2|150|28,6|19%|0,13|28,68|19%|
|MP10|Primaria|P98 diario|R3|150|28,6|19%|0,43|28,98|19%|

Fuente: Elaboración propia, 2021.

De acuerdo con lo presentado en la tabla anterior, se tiene que los aportes del
Proyecto no modifican la situación actual de calidad del aire del entorno del
proyecto, para el material particulado MP10, tanto en su estadístico diario

como anual.

Cabe señalar que la línea de base disponible corresponde sólo a material
particulado MP10, por lo que para los demás parámetros, a continuación se

58

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

presenta el aporte del proyecto con respecto a la normativa vigente, tanto
para las normas primarias como secundarias.

**Tabla 7.2. Análisis de cumplimiento de normativa vigente para MP** **2,5** **“Fase de Operación**

**Planta de Chancado” [μg/m** **[3]** **]**

|Parámetro|Tipo de<br>Norma|Estadístico|Receptores|Norma|(AP)|% (AP)<br>c/r Norma|
|---|---|---|---|---|---|---|
|MP2,5|Primaria|Promedio<br>Anual|R1|20|0,01|0%|
|MP2,5|Primaria|Promedio<br>Anual|R2|20|0,01|0%|
|MP2,5|Primaria|Promedio<br>Anual|R3|20|0,03|0%|
|MP2,5|Primaria|P98 diario|R1|50|0,05|0%|
|MP2,5|Primaria|P98 diario|R2|50|0,04|0%|
|MP2,5|Primaria|P98 diario|R3|50|0,13|0%|

Fuente: Elaboración propia, 2021.

**Tabla 7.3. Análisis de cumplimiento de normativa vigente para MPS “Fase de Operación**

**Planta de Chancado” [μg/m** **[3]** **]**

|Parámetro|Tipo de<br>Norma|Estadístico|Receptores|Norma|(AP)|% (AP)<br>c/r<br>Norma|
|---|---|---|---|---|---|---|
|MPS|Secundaria|Promedio<br>Anual|R4|100|0,0014|0%|
|MPS|Secundaria|Promedio<br>Anual|R5|100|0,0013|0%|
|MPS|Secundaria|Promedio<br>Anual|R6|100|0,0013|0%|
|MPS|Secundaria|Promedio<br>Anual|R7|100|0,0012|0%|
|MPS|Secundaria|Promedio<br>Anual|R8|100|0,0012|0%|
|MPS|Secundaria|Promedio<br>Anual|R9|100|0,0012|0%|
|MPS|Secundaria|Promedio<br>Anual|R10|100|0,0012|0%|
|MPS|Secundaria|Promedio<br>Mensual|R4|150|0,0030|0%|
|MPS|Secundaria|Promedio<br>Mensual|R5|150|0,0028|0%|
|MPS|Secundaria|Promedio<br>Mensual|R6|150|0,0029|0%|
|MPS|Secundaria|Promedio<br>Mensual|R7|150|0,0026|0%|
|MPS|Secundaria|Promedio<br>Mensual|R8|150|0,0027|0%|
|MPS|Secundaria|Promedio<br>Mensual|R9|150|0,0025|0%|
|MPS|Secundaria|Promedio<br>Mensual|R10|150|0,0026|0%|

Fuente: Elaboración propia, 2021.

59

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Tabla 7.4. Análisis de cumplimiento de normativa vigente para CO “Fase de Operación**

**Planta de Chancado” [μg/m** **[3]** **]**

|Parámetro|Tipo de<br>Norma|Estadístico|Receptores|Norma|(AP)|% (AP)<br>c/r Norma|
|---|---|---|---|---|---|---|
|CO|Primaria|P99 horario|R1|30.000|0,41|0%|
|CO|Primaria|P99 horario|R2|30.000|0,33|0%|
|CO|Primaria|P99 horario|R3|30.000|2,24|0%|
|CO|Primaria|P99 8 horas|R1|10.000|0,14|0%|
|CO|Primaria|P99 8 horas|R2|10.000|0,12|0%|
|CO|Primaria|P99 8 horas|R3|10.000|0,55|0%|

Fuente: Elaboración propia, 2021.

**Tabla 7.5. Análisis de cumplimiento de normativa vigente para NO** **2** **“Fase de Operación**

**Planta de Chancado” [μg/m** **[3]** **]**

|Parámetro|Tipo de<br>Norma|Estadístico|Receptores|Norma|(AP)|% (AP)<br>c/r Norma|
|---|---|---|---|---|---|---|
|NO2|Primaria|Promedio<br>Anual|R1|100|0,10|0%|
|NO2|Primaria|Promedio<br>Anual|R2|100|0,09|0%|
|NO2|Primaria|Promedio<br>Anual|R3|100|0,29|0%|
|NO2|Primaria|P99 diario|R1|400|2,92|1%|
|NO2|Primaria|P99 diario|R2|400|2,19|1%|
|NO2|Primaria|P99 diario|R3|400|11,73|3%|

Fuente: Elaboración propia, 2021.

**Tabla 7.6.** **Análisis de cumplimiento de normativa vigente para SO** **2** **“Fase de**

**Operación Planta de Chancado” [μg/m** **[3]** **]**

|Parámetro|Tipo de<br>Norma|Estadístico|Receptores|Norma|(AP)|% (AP)<br>c/r<br>Norma|
|---|---|---|---|---|---|---|
|SO2|Primaria|Promedio<br>Anual|R1|60|0,0001|0%|
|SO2|Primaria|Promedio<br>Anual|R2|60|0,0001|0%|
|SO2|Primaria|Promedio<br>Anual|R3|60|0,0003|0%|
|SO2|Primaria|P99 diario|R1|150|0,0004|0%|
|SO2|Primaria|P99 diario|R2|150|0,0003|0%|
|SO2|Primaria|P99 diario|R3|150|0,0012|0%|
|SO2|Primaria|P98,5<br>horario|R1|350|0,0008|0%|
|SO2|Primaria|P98,5<br>horario|R2|350|0,0007|0%|
|SO2|Primaria|P98,5<br>horario|R3|350|0,0033|0%|

60

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

|Parámetro|Tipo de<br>Norma|Estadístico|Receptores|Norma|(AP)|% (AP)<br>c/r<br>Norma|
|---|---|---|---|---|---|---|
||Secundaria|Promedio<br>Anual|R4|80|0,0002|0%|
||Secundaria|Promedio<br>Anual|R5|80|0,0002|0%|
||Secundaria|Promedio<br>Anual|R6|80|0,0002|0%|
||Secundaria|Promedio<br>Anual|R7|80|0,0002|0%|
||Secundaria|Promedio<br>Anual|R8|80|0,0002|0%|
||Secundaria|Promedio<br>Anual|R9|80|0,0002|0%|
||Secundaria|Promedio<br>Anual|R10|80|0,0002|0%|
||Secundaria|P99,7 diario|R4|365|0,0010|0%|
||Secundaria|P99,7 diario|R5|365|0,0010|0%|
||Secundaria|P99,7 diario|R6|365|0,0009|0%|
||Secundaria|P99,7 diario|R7|365|0,0009|0%|
||Secundaria|P99,7 diario|R8|365|0,0009|0%|
||Secundaria|P99,7 diario|R9|365|0,0009|0%|
||Secundaria|P99,7 diario|R10|365|0,0008|0%|
||Secundaria|P99,73<br>horario|R4|1000|0,0028|0%|
||Secundaria|P99,73<br>horario|R5|1000|0,0027|0%|
||Secundaria|P99,73<br>horario|R6|1000|0,0026|0%|
||Secundaria|P99,73<br>horario|R7|1000|0,0024|0%|
||Secundaria|P99,73<br>horario|R8|1000|0,0024|0%|
||Secundaria|P99,73<br>horario|R9|1000|0,0022|0%|
||Secundaria|P99,73<br>horario|R10|1000|0,0023|0%|

Fuente: Elaboración propia, 2021.

De acuerdo con lo presentado en las tablas anteriores, es preciso señalar que
la operación de la Planta de Chancado no genera aportes significativos sobre
los receptores evaluados, tanto en norma primaria, como secundaria, para
material particulado fino (MP 2,5 ), material particulado sedimentable (MPS) ni
gases (SO 2, CO y NO 2 ), alcanzando aportes máximos del 3% con respecto a
la normativa ambiental vigente para el NO 2 en su estadístico horario.

61

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**8** **MAPAS DE ISOCONCENTRACIONES**

A continuación, se presentan las iso-líneas de concentración para material
particulado respirable (MP 10 ), material particulado respirable fino (MP 2,5 ),
material particulado sedimentable (MPS) y para gases; dióxido de nitrógeno
(NO 2 ), dióxido de azufre (SO 2 ) y monóxido de carbono (CO), para la Operación
de la Planta de Chancado del Proyecto.

62

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 8.1. "Fase de Operación Planta de Chancado" Promedio anual de MP** **10** **- PMC**

63

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

Fuente: Elaboración propia, 2021.

64

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 8.2. "Fase de Operación Planta de Chancado" Percentil 98 diario de MP** **10** **- PMC**

Fuente: Elaboración propia, 2021.

65

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 8.3. "Fase de Operación Planta de Chancado" Promedio anual de MP** **2,5** **- PMC**

Fuente: Elaboración propia, 2021.

66

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 8.4. "Fase de Operación Planta de Chancado" Percentil 98 diario de MP** **2,5** **- PMC**

Fuente: Elaboración propia, 2021.

67

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 8.5. "Fase de Operación Planta de Chancado" Promedio anual de MPS - PMC**

Fuente: Elaboración propia, 2021.

68

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 8.6. "Fase de Operación Planta de Chancado" Promedio mensual de MPS - PMC**

Fuente: Elaboración propia, 2021.

69

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 8.7. "Fase de Operación Planta de Chancado" Promedio anual SO** **2** **- PMC**

Fuente: Elaboración propia, 2021.

70

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 8.8. "Fase de Operación Planta de Chancado" Percentil 99 diario SO** **2** **- PMC**

Fuente: Elaboración propia, 2021.

71

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 8.9. "Fase de Operación Planta de Chancado" Percentil 99,7 diario SO** **2** **- PMC**

Fuente: Elaboración propia, 2021.

72

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 8.10. "Fase de Operación Planta de Chancado" Percentil 99,73 horario SO** **2** **- PMC**

Fuente: Elaboración propia, 2021.

73

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 8.11. "Fase de Operación Planta de Chancado" Percentil 98,5 horario SO** **2** **- PMC**

Fuente: Elaboración propia, 2021.

74

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 8.12. "Fase de Operación Planta de Chancado" Promedio anual NO** **2** **- PMC**

Fuente: Elaboración propia, 2021.

75

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 8.13. "Fase de Operación Planta de Chancado" Percentil 99 horario NO** **2** **- PMC**

Fuente: Elaboración propia, 2021.

76

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 8.14. "Fase de Operación Planta de Chancado" Percentil 99 horario CO - PMC**

Fuente: Elaboración propia, 2021.

77

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**Figura 8.15. "Fase de Operación Planta de Chancado" Percentil 99 8 horas CO - PMC**

Fuente: Elaboración propia, 2021.

78

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

**9** **CONCLUSIONES**

En virtud de lo expuesto en las secciones anteriores, se concluye que el
Proyecto no provocará efectos adversos significativos sobre la salud de la
población, para mayor abundamiento se detalla lo siguiente:

Los niveles de línea de base monitoreados para el Material Particulado
Respirable (MP 10 ) no superan los límites ambientales vigentes para la Estación
de Taltal, de propiedad del titular, con porcentajes de norma de un 19% para
el P98 diario y de un 33% en relación con el promedio anual.

Con respecto a los cálculos de emisiones para las fuentes fugitivas, se
obtuvieron emisiones para un año de operación de la Planta de Chancado, en
donde se pudo observar que las máximas emisiones se generan en la actividad
de tránsito por camino no pavimentado para el material particulado en todas
sus fracciones (MP 10, MP 2,5 y MPS), mientras que para los gases se generan
producto de la actividad de operación de maquinarias.

De acuerdo con la modelación es posible indicar que, los aportes del Proyecto,
con respecto a la línea de base monitoreada en la Estación Taltal, no modifican
la situación actual de calidad del aire del área de influencia del Proyecto, dado
que no se alteran los porcentajes con respecto a la normativa ambiental
vigente, en ninguno de sus estadísticos normados, manteniéndose los
porcentajes en un 33% para el promedio anual y un 19 % para el estadístico

diario.

Cabe señalar que la línea de base monitoreada corresponde a material
particulado respirable MP 10, por lo que, para la evaluación de los demás
parámetros analizados se presentaron los aportes del Proyecto sobre los
receptores considerados tanto para la normativa primaria como secundaria,
con su respectivo porcentaje con respecto a cada estadístico normado.
Respecto a los otros parámetros, es preciso señalar que, el proyecto en su
fase de operación de la planta de chancado no genera aportes significativos
sobre los receptores evaluados, tanto en norma primaria, como secundaria,
para material particulado fino (MP 2,5 ), material particulado sedimentable
(MPS) ni gases (SO 2, CO y NO 2 ), alcanzando aportes máximos del 3 % con
respecto a la normativa ambiental vigente para el NO 2 en su estadístico
horario. Por lo que no modifica la condición actual de calidad del aire del área

79

ESTIMACIÓN Y MODELACIÓN DE EMISIONES ATMOSFÉRICAS, PROYECTO
“EXTENSIÓN VIDA ÚTIL PLANTA DE CHANCADO MÓVIL, TALTAL”

de influencia del Proyecto.

En cuanto al punto de máxima concentración, cabe destacar que, se encuentra
alejado de los receptores sensibles, en una zona no poblada (ladera de cerro),
y presenta valores de concentración muy por debajo de los límites normados
para todos los parámetros analizados (material particulado y gases).

Finalmente, y según los análisis presentados, se concluye que la extensión de
la vida útil del Proyecto, que permite la continuidad operacional de la planta
de chancado móvil de Taltal, no generará aportes que modifiquen
significativamente la calidad del aire de su área de influencia, ni generarán
superación de la normativa ambiental vigente para ninguno de sus parámetros
presentados y evaluados, con respecto a la estación de monitoreo de calidad
del aire presente en el entorno del Proyecto, ni tampoco para los receptores
considerados como sensibles, tanto para las normas primarias como

secundarias analizadas.

80

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2.1.: Normas de calidad del aire consideradas en el estudio****

| Parámetro | Tipo de<br>Norma | Estadístico | Valor | Referencia |
| --- | --- | --- | --- | --- |
| **MP10** | Primaria | Promedio del periodo | 50 mg/m3N | D.S. 45/02 MINSEGPRES |
| **MP10** | Primaria | Percentil 98 diario | 150 mg/m3N | D.S. 59/98 MINSEGPRES |
| **MP2,5 ** | Primaria | Promedio del periodo | 20 mg/m3 | D.S. 12/11 MMA |
| **MP2,5 ** | Primaria | Percentil 98 diario | 50 mg/m3 | D.S. 12/11 MMA |
| **MPS** | Secundaria | Promedio Anual | 100 mg/m2-día | D.S. 04/92 MINAGRI |
| **MPS** | Secundaria | Promedio Mensual | 150 mg/m2-día | D.S. 04/92 MINAGRI |
| **SO2 ** | Primaria | Promedio del periodo | 60 mg/m3N | D.S. 104/19<br>MINSEGPRES |
| **SO2 ** | Primaria | Percentil 99 diario | 150 mg/m3N | D.S. 104/19<br>MINSEGPRES |
| **SO2 ** | Primaria | Percentil 98,5 horario | 350 mg/m3N | D.S. 104/19<br>MINSEGPRES |
| **SO2 ** | Secundaria | Promedio del periodo | 80 mg/m3N | D.S. 22/10 MINSEGPRES |
| **SO2 ** | Secundaria | Percentil 99,7 diario | 365 mg/m3N | D.S. 22/10 MINSEGPRES |
| **SO2 ** | Secundaria | Percentil 99,73<br>horario | 1.000 mg/m3N | D.S. 22/10 MINSEGPRES |
| **NO2 ** | Primaria | Promedio del periodo | 100 mg/m3N | D.S. 114/02<br>MINSEGPRES |
| **NO2 ** | Primaria | Percentil 99 horario | 400 mg/m3N | D.S. 114/02<br>MINSEGPRES |
| **CO** | Primaria | Percentil 99 (8 horas) | 10.000 mg/m3N | D.S. 115/02<br>MINSEGPRES |
| **CO** | Primaria | Percentil 99 horario | 30.000 mg/m3N | D.S. 115/02<br>MINSEGPRES |

**Tabla 3.1.: Estación de monitoreo - Localización y Variables Monitoreadas****

| Estación | Parámetro | Coordenadas UTM,<br>WGS84 [m] | Col4 | Variable<br>monitoreada | Periodo considerado | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Estación** | **Parámetro** | Este | Norte | Norte | Inicio | Término |
| **Estación**<br>**Taltal** | Meteorología | 351.932 | 7.190.064 | Velocidad del viento | 01-01-2019 | 31-12-2020 |
| **Estación**<br>**Taltal** | Meteorología | 351.932 | 7.190.064 | Dirección del viento | 01-01-2019 | 31-12-2020 |
| **Estación**<br>**Taltal** | Calidad del<br>Aire | Calidad del<br>Aire | Calidad del<br>Aire | Material Particulado<br>PM10 | 01-01-2019 | 31-12-2020 |

**Tabla 3.2.: Porcentaje de data válida para las variables monitoreadas****

| Variable | Col2 | Data válida |
| --- | --- | --- |
| **PM10** | 2019 | 96,8 |
| **PM10** | 2020 | 99,8 |
| **Dirección del**<br>**viento** | 2020 | 99,6 |
| **Dirección del**<br>**viento** | 2020 | 99,9 |
| **Velocidad del**<br>**viento** | 2019 | 99,6 |
| **Velocidad del**<br>**viento** | 2020 | 99,9 |

**Tabla 3.3.: Resumen de Información de velocidad del viento, Años 2019 y 2020****

| Estadístico | 2019 | 2020 |
| --- | --- | --- |
| **Promedio (m/s)** | 1,80 | 1,79 |
| **Máximo (m/s)** | 5,20 | 5,50 |

**Tabla 3.4.: Normativa primaria de calidad del aire para MP** **10****

| Decreto Aplicable | Norma | Col3 | Periodo de Evaluación de Cumplimiento<br>de Norma |
| --- | --- | --- | --- |
| **Decreto Aplicable** | **Valor** | **Unidad** | **Unidad** |
| **Decreto Supremo**<br>**N°59/1998** | 150 | μg/m3N | Percentil 98 de las concentraciones de 24<br>horas registradas durante un periodo anual |
| **Decreto Supremo**<br>**N°45/2002** | 50 | 50 | Concentración promedio anual |

**Tabla 3.5.: Monitoreo material particulado MP** **10** **y comparación con norma****

| Año | Estadístico | Datos<br>Válidos | Valor<br>[ug/m3N] | Límite de la<br>Norma<br>[ug/m3N] | % de<br>la<br>Norma |
| --- | --- | --- | --- | --- | --- |
| **2019** | Promedio del período | 96,8% | 16,8 | 50 | 34% |
| **2019** | Percentil 98 Diario | Percentil 98 Diario | 30,4 | 150 | 20% |
| **2020** | Promedio del período | 96,8% | 15,7 | 50 | 31% |
| **2020** | Percentil 98 Diario | Percentil 98 Diario | 26,7 | 150 | 18% |
| **Promedio**<br>**bi-anual** | Promedio del período | 96,8% | 16,3 | 50 | 33% |
| **Promedio**<br>**bi-anual** | Percentil 98 Diario | Percentil 98 Diario | 28,6 | 150 | 19% |

**Tabla 4.1.: Actividades emisoras MP** **10** **, MP** **2,5** **, MPS y gases SO** **2** **, NOx y CO****

| Actividad | Contaminante |
| --- | --- |
| − Trasferencia de material tipo carga y descarga<br>− Tránsito en camino industrial no pavimentado<br>− Chancado de material, primario y secundario<br>− Selección de material, tamizado fino y grueso<br>− Puntos de transferencia en correas<br>transportadoras<br>− Erosión Eólica<br> | MP10, MP2,5y MPS |
| − Motor de vehículos<br>− Motor maquinarias<br> | MP10, MP2,5,MPS y gases<br>(CO, NOx y SO2) |

**Tabla 4.2.: Nivel de actividad - Tránsito por camino no pavimentado****

| Actividad | Tramo | Material<br>[t/año] | Capacidad<br>del<br>camión<br>[t] | Viajes<br>anuales<br>(ida) | Largo<br>[km] | Nivel del<br>Actividad<br>ida y<br>vuelta<br>[km/año] |
| --- | --- | --- | --- | --- | --- | --- |
| **Riego de**<br>**caminos** | Tramo 1 | - | - | 1.825 | 0,8 | 2.811 |
| **Riego de**<br>**caminos** | Tramo 2 | - | - | 1.825 | 0,2 | 657 |
| **Transporte**<br>**de mineral** | Tramo 1 | 260.000 | 20 | 13.000 | 0,8 | 20.020 |
| **Transporte**<br>**de mineral** | Tramo 2 | Tramo 2 | Tramo 2 | 13.000 | 0,2 | 4.680 |
| **Total** | **Tramo 1** | **260.000** | **20** | **14.825** | **0,8** | **22.831** |
| **Total** | **Tramo 2** | **Tramo 2** | **Tramo 2** | **14.825** | **0,2** | **5.337** |

**Tabla 4.3.: Factor de emisión - Tránsito por camino no pavimentado industrial****

| Material Particulado | Factor de emisión [kg/km] |
| --- | --- |
| MPS | 2,723 |
| MP10 | 0,804 |
| MP2,5 | 0,080 |

**Tabla 4.4.: Emisiones resultantes -Resuspención por tránsito en camino no pavimentado****

| Tramo | Nivel de<br>actividad<br>[km/año] | Mitigación<br>[%] | Factor de Emisión<br>[kg/km] | Col5 | Col6 | Emisiones [t/año] | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tramo** | **Nivel de**<br>**actividad**<br>**[km/año]** | **Mitigación**<br>**[%]** | **MPS** | **MP10** | **MP2,5** | **MPS** | **MP10** | **MP2,5** |
| **Tramo 1** | 22.831 | 80 | 2,723 | 0,804 | 0,080 | 12,43 | 3,67 | 0,37 |
| **Tramo 2** | 5.337 | 80 | 2,723 | 0,804 | 0,080 | 2,91 | 0,86 | 0,09 |
| **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **15,34** | **4,53** | **0,45** |

**Tabla 4.5.: Nivel de actividad - Transferencia de material****

| Actividad | Fuente | Zona | Material<br>Anual<br>[t/año] |
| --- | --- | --- | --- |
| **Transferencias de**<br>**mineral** | Carga de Material | Cancha de mineral | 260.000 |
| **Transferencias de**<br>**mineral** | Descarga de Material | Área de chancado | 260.000 |
| **Transferencias de**<br>**mineral** | Carga de Material | Stock Pile | 260.000 |
| **Transferencias de**<br>**mineral** | Descarga de Material | Área de aglomerado | 260.000 |
| **Total** | **Total** | **Total** | 1.040.000 |

**Tabla 4.6.: Factor de emisión - Transferencia de material****

| Material Particulado | Factor de emisión [kg/t] |
| --- | --- |
| MPS | 4,5E-04 |
| MP10 | 2,1E-04 |
| MP2,5 | 3,2E-05 |

**Tabla 4.7.: Emisiones resultantes - Transferencia de material****

| Fuente | Zona | Material<br>Anual<br>[t/año] | Factor de Emisión [kg/t] | Col5 | Col6 | Emisiones [t/año] | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente** | **Zona** | **Material**<br>**Anual**<br>**[t/año]** | **MPS** | **MP10** | **MP2,5** | **MPS** | **MP10 ** | **MP2,5 ** |
| **Carga de**<br>**Material** | Cancha de<br>mineral | 260.000 | 4,5E-04 | 2,1E-04 | 3,2E-05 | 0,12 | 0,06 | 0,01 |
| **Descarga**<br>**de Material** | Área de<br>chancado | 260.000 | 4,5E-04 | 2,1E-04 | 3,2E-05 | 0,12 | 0,06 | 0,01 |
| **Carga de**<br>**Material** | Stock Pile | 260.000 | 4,5E-04 | 2,1E-04 | 3,2E-05 | 0,12 | 0,06 | 0,01 |
| **Descarga**<br>**de Material** | Área de<br>aglomerado | 260.000 | 4,5E04 | 2,1E-04 | 3,2E-05 | 0,12 | 0,06 | 0,01 |
| **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **0,47** | **0,22** | **0,03** |

**Tabla 4.8.: Nivel de actividad - Procesamiento de Material****

| Actividad | Fuente | Zona | Material Anual<br>[t/año] |
| --- | --- | --- | --- |
| **Procesamiento**<br>**de material** | Chancado Primario | Zona de<br>Chancado | 260.000 |
| **Procesamiento**<br>**de material** | Chancado Secundario | Chancado Secundario | 260.000 |
| **Procesamiento**<br>**de material** | Clasificación de material<br>(tamizado grueso) | Clasificación de material<br>(tamizado grueso) | 260.000 |
| **Procesamiento**<br>**de material** | Clasificación de material<br>(tamizado fino) | Clasificación de material<br>(tamizado fino) | 260.000 |
| **Procesamiento**<br>**de material** | Transferencia entre correas<br>transportadoras | Transferencia entre correas<br>transportadoras | 1.300.000 |

**Tabla 4.9.: Factor de Emisión - Procesamiento de Material****

| Actividad | Factor de Emisión<br>[kg/t] | Col3 | Col4 |
| --- | --- | --- | --- |
| **Actividad** | **MPS** | **MP10** | **MP2,5** |
| Chancado primario (con supresión húmeda) | 0,0006 | 0,0003 | 0,0001 |
| Chancado secundario (con supresión húmeda) | 0,0006 | 0,0003 | 0,0001 |
| Tamizado grueso (con supresión húmeda) | 0,0011 | 0,0004 | 0,0000 |
| Tamizado fino (con supresión húmeda) | 0,0018 | 0,0011 | 0,0002 |
| Punto de transferencia entre correas | 0,0015 | 0,0006 | 0,0002 |

**Tabla 4.10.: Emisiones resultantes - Procesamiento de material****

| Actividad | Fuente | Zona | Material<br>Anual<br>[t/año] | Factor de Emisión [kg/t] | Col6 | Col7 | Emisiones [t/año] | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Fuente** | **Zona** | **Material**<br>**Anual**<br>**[t/año]** | **MPS** | **MP10** | **MP2,5** | **MPS** | **MP10 ** | **MP2,5 ** |
| **Procesamiento de material** | Chancado<br>Primario | Zona<br>de chancado | 260.000 | 0,0006 | 0,0003 | 0,0001 | 0,156 | 0,070 | 0,013 |
| **Procesamiento de material** | Chancado<br>Secundario | Chancado<br>Secundario | 260.000 | 0,0006 | 0,0003 | 0,0001 | 0,156 | 0,070 | 0,013 |
| **Procesamiento de material** | Clasificación de<br>material<br>(tamizado<br>grueso) | Clasificación de<br>material<br>(tamizado<br>grueso) | 260.000 | 0,0011 | 0,0004 | 0,0000 | 0,286 | 0,096 | 0,007 |
| **Procesamiento de material** | Clasificación de<br>material<br>(tamizado fino) | Clasificación de<br>material<br>(tamizado fino) | 260.000 | 0,0018 | 0,0011 | 0,0002 | 0,468 | 0,286 | 0,043 |
| **Procesamiento de material** | Transferencia<br>entre correas<br>transportadoras | Transferencia<br>entre correas<br>transportadoras | 260.000 | 0,0015 | 0,0006 | 0,0002 | 1,950 | 0,715 | 0,202 |
| **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **3,02** | **0,24** | **0,03** |

**Tabla 4.11.: Nivel de actividad - combustión interna de maquinaria****

| Actividad | Maquinaria | N° de<br>maquinarias | Horas<br>diarias | Días a<br>mes | Meses<br>al año | Potencia<br>[kw] | Nivel de<br>actividad<br>[h-kw/año] |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Carga de**<br>**Material** | Cargador<br>Frontal | 2 | 12 | 25 | 12 | 138 | 993.600 |

**Tabla 4.12.: Factor de emisión - Combustión interna de maquinaria****

| Actividad | Factor de Emisión [kg/kw-h] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **MPS** | **MP10** | **MP2,5** | **NOX ** | **SO2 ** | **CO** | **HC** |
| Cargador Frontal | 0,0011 | 0,0011 | 0,0011 | 0,0144 | 0,00002 | 0,0030 | 0,0014 |

**Tabla 4.13.: Emisiones Resultantes - Combustión interna de maquinaria****

| Actividad | Nivel de<br>Actividad<br>[h-kw/año] | Emisiones [t/año] | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Nivel de**<br>**Actividad**<br>**[h-kw/año]** | **MPS** | **MP10** | **MP2,5** | **NOX ** | **SO2 ** | **CO** | **HC** |
| Cargador<br>Frontal | 993.600 | 1,09 | 1,09 | 1,09 | 14,27 | 0,02 | 2,98 | 1,34 |

**Tabla 4.14.: Nivel de actividad - Combustión interna de vehículos****

| Actividad | Tramo | Material<br>[t/año] | Capacidad<br>del<br>camión<br>[t] | Viajes<br>anuales<br>(ida) | Largo<br>[km] | Nivel del<br>Actividad<br>ida y<br>vuelta<br>[km/año] |
| --- | --- | --- | --- | --- | --- | --- |
| **Riego de**<br>**caminos** | Tramo 1 | - | - | 1.825 | 0,8 | 2.811 |
| **Riego de**<br>**caminos** | Tramo 2 | - | - | 1.825 | 0,2 | 657 |
| **Transporte**<br>**de mineral** | Tramo 1 | 260.000 | 20 | 13.000 | 0,8 | 20.020 |
| **Transporte**<br>**de mineral** | Tramo 2 | Tramo 2 | Tramo 2 | 13.000 | 0,2 | 4.680 |
| **Total** | **Tramo 1** | **260.000** | **20** | **14.825** | **0,8** | **22.831** |
| **Total** | **Tramo 2** | **Tramo 2** | **Tramo 2** | **14.825** | **0,2** | **5.337** |

**Tabla 4.15.: Factor de emisión - Combustión interna de vehículos [g/km]****

| Tipo de<br>vehículo | Factor de Emisión [g/km] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo de**<br>**vehículo** | **MPS** | **MP10** | **MP2,5** | **NOX ** | **SO2 ** | **CO** | **COV** |
| Pesados - Diésel<br>16 - 32 [t] - Euro<br>IV - 2005 | 0,13 | 0,13 | 0,13 | 6,27 | 0,0063 | 0,149 | 0,278 |

**Tabla 4.16.: Emisiones resultantes - Combustión interna de vehículos****

| Camino | Nivel de<br>Actividad<br>[km/año] | Emisiones [t/año] | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Camino** | **Nivel de**<br>**Actividad**<br>**[km/año]** | **MPS** | **MP10** | **MP2,5** | **NOX ** | **SO2 ** | **CO** | **HC** |
| Tramo 1 | 43.882 | 0,0030 | 0,0030 | 0,0030 | 0,1431 | 0,0001 | 0,0034 | 0,0063 |
| Tramo 2 | 35.616 | 0,0007 | 0,0007 | 0,0007 | 0,0335 | 0,0000 | 0,0008 | 0,0015 |
| **Total** | **Total** | **0,004** | **0,004** | **0,004** | **0,177** | **0,000** | **0,004** | **0,008** |

**Tabla 4.17.: Nivel de actividad - Erosión de material en pila****

| Zona | Superficie | Col3 | Días de exposición al año | Nivel de actividad[ha-<br>días/año] |
| --- | --- | --- | --- | --- |
| **Zona** | **[m2] ** | **[ha]** | **[ha]** | **[ha]** |
| **Stock Pile** | 1.200 | 0,12 | 365 | 43,8 |
| **Cancha de mineral** | 2.000 | 0,20 | 365 | 73,0 |

**Tabla 4.18.: Factor de emisión - Erosión de material en pila****

| Material Particulado | Factor de emisión [kg/ha] |
| --- | --- |
| MPS | 4,22 |
| MP10 | 2,11 |
| MP2,5<br> | 0,31<br> |

**Tabla 4.19.: Emisiones resultantes - Erosión de material en pila****

| Fuente | Zona | Superficie<br>expuesta al<br>año[ha-<br>día/año] | Factor de Emisión [kg/ha-<br>día] | Col5 | Col6 | Emisiones [t/año] | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fuente** | **Zona** | **Superficie**<br>**expuesta al**<br>**año[ha-**<br>**día/año]** | **MPS** | **MP10** | **MP2,5** | **MPS** | **MP10 ** | **MP2,5 ** |
| **Erosión**<br>**de**<br>**material**<br>**en pila** | **Stock**<br>**Pile** | 43,8 | 4,22 | 2,11 | 0,31 | 0,18 | 0,09 | 0,01 |
| **Erosión**<br>**de**<br>**material**<br>**en pila** | **Cancha de**<br>**mineral** | 73,0 | 4,22 | 2,11 | 0,31 | 0,31 | 0,15 | 0,02 |
| **Total** | **Total** | **Total** | **Total** | **Total** | **Total** | **0,39** | **0,19** | **0,03** |

**Tabla 4.20.: Emisiones resultantes****

| Actividad | Emisiones [t/año] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **MPS** | **MP10** | **MP2,5** | **NOX ** | **SO2 ** | **CO** | **HC/C**<br>**OV** |
| Vehículos en caminos<br>industriales NO<br>pavimentados | 15,34 | 4,53 | 0,45 | 0,00 | 0,00 | 0,00 | 0,00 |
| Transferencia de material | 0,47 | 0,22 | 0,03 | 0,00 | 0,00 | 0,00 | 0,00 |
| Procesamiento de<br>material | 3,02 | 1,33 | 0,36 | 0,00 | 0,00 | 0,00 | 0,00 |
| Motor maquinaria | 1,09 | 1,09 | 1,09 | 14,27 | 0,02 | 2,98 | 1,34 |
| Motor vehículos pesados | 0,00 | 0,00 | 0,00 | 0,18 | 0,00 | 0,00 | 0,01 |
| Erosión de material en<br>pila | 0,49 | 0,25 | 0,04 | 0,00 | 0,00 | 0,00 | 0,00 |
| **Total** | **20,41** | **7,42** | **1,98** | **14,44** | **0,02** | **2,98** | **1,35** |

**Tabla 5.1.: Características del uso de suelo****

| Parámetro | Uso de Suelo | Col3 | Col4 |
| --- | --- | --- | --- |
| **Parámetro** | **Pastizales** | **Tierra Estéril** | **Mar** |
| Rugosidad Superficial | 0,05 | 0,05 | 0,001 |
| Albedoiii | 0,25 | 0,30 | 0,10 |
| Razón de Boweniv | 1,0 | 1,0 | 0,0 |

**Tabla 5.2.: ** **Localización puntos discretos** **[v]****

| ID | Punto de Interés | Distancia de Área<br>de Proyecto (km) | Este (m) | Norte (m) |
| --- | --- | --- | --- | --- |
| R1 | Estación Taltal (Población Eduardo Vigil) | 1,53 | 351.932 | 7.190.064 |
| R2 | Escuela Alondra Rojas | 1,92 | 351.604 | 7.189.859 |
| R3 | Playa Muelle de Piedra | 0,27 | 353.262 | 7.191.602 |
| R4 | Olivicultores 1 (MPS_1) | 1,82 | 353.705 | 7.189.037 |
| R5 | Olivicultores 2 (MPS_2) | 1,88 | 353.660 | 7.188.965 |
| R6 | Olivicultores 3 (MPS_3) | 1,85 | 353.748 | 7.189.019 |
| R7 | Olivicultores 4 (MPS_4) | 1,94 | 353.697 | 7.188.917 |
| R8 | Olivicultores 5 (MPS_5) | 1,91 | 353.744 | 7.188.960 |
| R9 | Olivicultores 6 (MPS_6) | 1,98 | 353.718 | 7.188.881 |
| R10 | Olivicultores 7 (MPS_7) | 1,93 | 353.795 | 7.188.947 |

**Tabla 5.3.: Aportes del Proyecto en puntos de interés y puntos de máxima concentración (PMC) “Fase de Operación Planta****

| Receptores | MP<br>10 | Col3 | MP<br>2,5 | Col5 | CO | Col7 | NO<br>2 | Col9 | SO<br>2 | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptores** | **Norma Primaria** | **Norma Primaria** | **Norma Primaria** | **Norma Primaria** | **Norma**<br>**Primaria** | **Norma**<br>**Primaria** | **Norma Primaria** | **Norma Primaria** | **Norma Primaria** | **Norma Primaria** | **Norma Primaria** |
| **Receptores** | **Promedio**<br>**Anual** | **P98**<br>**diario** | **Promedio**<br>**Anual** | **P98**<br>**diario** | **P99**<br>**horario** | **P99**<br>**8 **<br>**horas** | **Promedio**<br>**Anual** | **P99**<br>**horario** | **Promedio**<br>**Anual** | **P99**<br>**diario** | **P98,5**<br>**horario** |
| R1 | 0,04 | 0,13 | 0,01 | 0,04 | 0,36 | 0,13 | 0,09 | 2,61 | 0,0001 | 0,0003 | 0,0007 |
| R2 | 0,03 | 0,12 | 0,01 | 0,04 | 0,30 | 0,11 | 0,08 | 1,95 | 0,0001 | 0,0003 | 0,0006 |
| R3 | 0,10 | 0,38 | 0,03 | 0,12 | 2,00 | 0,49 | 0,26 | 10,47 | 0,0003 | 0,0011 | 0,0029 |
| PMC | 0,83 | 5,11 | 0,27 | 1,06 | 12,24 | 3,73 | 1,48 | 55,26 | 0,0019 | 0,0077 | 0,0321 |

**Tabla 5.4.: Aportes del Proyecto de MPS y SO** **2** **(Norma Secundaria) en puntos de interés y punto de máxima concentración****

| Receptores | MPS (Norma Secundaria)<br>[mg/m2-día] | Col3 | SO (Norma Secundaria)<br>2<br>[ug/m3] | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Receptores** | **Promedio**<br>**Anual** | **Promedio**<br>**Mensual** | **Promedio**<br>**Anual** | **P99,7**<br>**diario** | **P99,73**<br>**horario** |
| R4 | 0,0012 | 0,0027 | 0,0002 | 0,0009 | 0,0025 |
| R5 | 0,0012 | 0,0025 | 0,0002 | 0,0009 | 0,0024 |
| R6 | 0,0012 | 0,0026 | 0,0002 | 0,0008 | 0,0023 |
| R7 | 0,0011 | 0,0023 | 0,0001 | 0,0008 | 0,0022 |
| R8 | 0,0011 | 0,0024 | 0,0001 | 0,0008 | 0,0022 |
| R9 | 0,0010 | 0,0022 | 0,0001 | 0,0008 | 0,0020 |
| R10 | 0,0011 | 0,0023 | 0,0001 | 0,0008 | 0,0021 |
| PMC | 0,0096 | 0,0163 | 0,0019 | 0,0091 | 0,0569 |

**Tabla 5.5.: Aportes del Proyecto en puntos de interés y puntos de máxima concentración (PMC) “Fase de Operación Planta****

| Receptores | MP<br>10 | Col3 | MP<br>2,5 | Col5 | CO | Col7 | NO<br>2 | Col9 | SO<br>2 | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptores** | **Norma Primaria** | **Norma Primaria** | **Norma Primaria** | **Norma Primaria** | **Norma**<br>**Primaria** | **Norma**<br>**Primaria** | **Norma Primaria** | **Norma Primaria** | **Norma Primaria** | **Norma Primaria** | **Norma Primaria** |
| **Receptores** | **Promedio**<br>**Anual** | **P98**<br>**diario** | **Promedio**<br>**Anual** | **P98**<br>**diario** | **P99**<br>**horario** | **P99**<br>**8 **<br>**horas** | **Promedio**<br>**Anual** | **P99**<br>**horario** | **Promedio**<br>**Anual** | **P99**<br>**diario** | **P98,5**<br>**horario** |
| R1 | 0,04 | 0,15 | 0,01 | 0,05 | 0,41 | 0,14 | 0,10 | 2,92 | 0,0001 | 0,0004 | 0,0008 |
| R2 | 0,03 | 0,13 | 0,01 | 0,04 | 0,33 | 0,12 | 0,09 | 2,19 | 0,0001 | 0,0003 | 0,0007 |
| R3 | 0,11 | 0,43 | 0,03 | 0,13 | 2,24 | 0,55 | 0,29 | 11,73 | 0,0003 | 0,0012 | 0,0033 |
| PMC | 0,93 | 5,72 | 0,30 | 1,19 | 13,71 | 4,18 | 1,65 | 61,89 | 0,0022 | 0,0086 | 0,0360 |

**Tabla 5.6.: Aportes del Proyecto de MPS y SO** **2** **(Norma Secundaria) en puntos de interés y punto de máxima concentración****

| Receptores | MPS (Norma Secundaria)<br>[mg/m2-día] | Col3 | SO (Norma Secundaria)<br>2<br>[ug/m3] | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Receptores** | **Promedio**<br>**Anual** | **Promedio**<br>**Mensual** | **Promedio**<br>**Anual** | **P99,7**<br>**diario** | **P99,73**<br>**horario** |
| R4 | 0,0014 | 0,0030 | 0,0002 | 0,0010 | 0,0028 |
| R5 | 0,0013 | 0,0028 | 0,0002 | 0,0010 | 0,0027 |
| R6 | 0,0013 | 0,0029 | 0,0002 | 0,0009 | 0,0026 |
| R7 | 0,0012 | 0,0026 | 0,0002 | 0,0009 | 0,0024 |
| R8 | 0,0012 | 0,0027 | 0,0002 | 0,0009 | 0,0024 |
| R9 | 0,0012 | 0,0025 | 0,0002 | 0,0009 | 0,0022 |
| R10 | 0,0012 | 0,0026 | 0,0002 | 0,0008 | 0,0023 |
| PMC | 0,0107 | 0,0182 | 0,0022 | 0,0102 | 0,0638 |

**Tabla 5.7.: Coordenadas de localización punto de máxima concentración (PMC) "Fase de****

| Parámetro | Tipo de<br>Norma | Estadístico | Este (m) | Norte (m) | ID |
| --- | --- | --- | --- | --- | --- |
| MP10 | Primaria | Promedio Anual | 354.038 | 7.190.687 | PMC1 |
| MP10 | Primaria | Percentil 98 Diario | 354.038 | 7.190.687 | PMC1 |
| MP2,5 | Primaria | Promedio Anual | 354.038 | 7.190.687 | PMC1 |
| MP2,5 | Primaria | Percentil 98 Diario | 354.038 | 7.190.687 | PMC1 |
| MPS | Secundaria | Promedio Anual | 354.038 | 7.190.687 | PMC1 |
| MPS | Secundaria | Promedio Mensual | 354.038 | 7.190.687 | PMC1 |
| CO | Primaria | Percentil 99 Horario | 354.038 | 7.190.687 | PMC1 |
| CO | Primaria | Percentil 99 8 horas. | 354.038 | 7.190.687 | PMC1 |
| NO2 | Primaria | Promedio del Anual | 354.038 | 7.190.687 | PMC1 |
| NO2 | Primaria | Percentil 99 Horario | 354.038 | 7.190.687 | PMC1 |
| SO2 | Primaria | Promedio del Anual | 354.038 | 7.190.687 | PMC1 |
| SO2 | Primaria | Percentil 99 Diario | 354.038 | 7.190.687 | PMC1 |
| SO2 | Primaria | Percentil 98,5 horario | 354.038 | 7.190.687 | PMC1 |
| SO2 | Secundaria | Promedio del Anual | 354.038 | 7.190.687 | PMC1 |
| SO2 | Secundaria | Percentil 99,7 Diario | 354.038 | 7.190.687 | PMC1 |
| SO2 | Secundaria | Percentil 99,73 Horario | 354.038 | 7.190.687 | PMC1 |

**Tabla 7.1.: Análisis de cumplimiento de normativa vigente para MP** **10** **“Fase de Operación****

| Parámetro | Tipo de<br>Norma | Estadístico | Receptores | Norma | (LB) | %<br>(LB)<br>c/r<br>Norma | (AP) | (AP+LB) | (AP+LB)<br>c/r a<br>(LB) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MP10 | Primaria | Promedio<br>Anual | R1 | 50 | 16,3 | 33% | 0,04 | 16,29 | 33% |
| MP10 | Primaria | Promedio<br>Anual | R2 | 50 | 16,3 | 33% | 0,03 | 16,28 | 33% |
| MP10 | Primaria | Promedio<br>Anual | R3 | 50 | 16,3 | 33% | 0,11 | 16,36 | 33% |
| MP10 | Primaria | P98 diario | R1 | 150 | 28,6 | 19% | 0,15 | 28,70 | 19% |
| MP10 | Primaria | P98 diario | R2 | 150 | 28,6 | 19% | 0,13 | 28,68 | 19% |
| MP10 | Primaria | P98 diario | R3 | 150 | 28,6 | 19% | 0,43 | 28,98 | 19% |

**Tabla 7.2.: Análisis de cumplimiento de normativa vigente para MP** **2,5** **“Fase de Operación****

| Parámetro | Tipo de<br>Norma | Estadístico | Receptores | Norma | (AP) | % (AP)<br>c/r Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP2,5 | Primaria | Promedio<br>Anual | R1 | 20 | 0,01 | 0% |
| MP2,5 | Primaria | Promedio<br>Anual | R2 | 20 | 0,01 | 0% |
| MP2,5 | Primaria | Promedio<br>Anual | R3 | 20 | 0,03 | 0% |
| MP2,5 | Primaria | P98 diario | R1 | 50 | 0,05 | 0% |
| MP2,5 | Primaria | P98 diario | R2 | 50 | 0,04 | 0% |
| MP2,5 | Primaria | P98 diario | R3 | 50 | 0,13 | 0% |

**Tabla 7.3.: Análisis de cumplimiento de normativa vigente para MPS “Fase de Operación****

| Parámetro | Tipo de<br>Norma | Estadístico | Receptores | Norma | (AP) | % (AP)<br>c/r<br>Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MPS | Secundaria | Promedio<br>Anual | R4 | 100 | 0,0014 | 0% |
| MPS | Secundaria | Promedio<br>Anual | R5 | 100 | 0,0013 | 0% |
| MPS | Secundaria | Promedio<br>Anual | R6 | 100 | 0,0013 | 0% |
| MPS | Secundaria | Promedio<br>Anual | R7 | 100 | 0,0012 | 0% |
| MPS | Secundaria | Promedio<br>Anual | R8 | 100 | 0,0012 | 0% |
| MPS | Secundaria | Promedio<br>Anual | R9 | 100 | 0,0012 | 0% |
| MPS | Secundaria | Promedio<br>Anual | R10 | 100 | 0,0012 | 0% |
| MPS | Secundaria | Promedio<br>Mensual | R4 | 150 | 0,0030 | 0% |
| MPS | Secundaria | Promedio<br>Mensual | R5 | 150 | 0,0028 | 0% |
| MPS | Secundaria | Promedio<br>Mensual | R6 | 150 | 0,0029 | 0% |
| MPS | Secundaria | Promedio<br>Mensual | R7 | 150 | 0,0026 | 0% |
| MPS | Secundaria | Promedio<br>Mensual | R8 | 150 | 0,0027 | 0% |
| MPS | Secundaria | Promedio<br>Mensual | R9 | 150 | 0,0025 | 0% |
| MPS | Secundaria | Promedio<br>Mensual | R10 | 150 | 0,0026 | 0% |

**Tabla 7.4.: Análisis de cumplimiento de normativa vigente para CO “Fase de Operación****

| Parámetro | Tipo de<br>Norma | Estadístico | Receptores | Norma | (AP) | % (AP)<br>c/r Norma |
| --- | --- | --- | --- | --- | --- | --- |
| CO | Primaria | P99 horario | R1 | 30.000 | 0,41 | 0% |
| CO | Primaria | P99 horario | R2 | 30.000 | 0,33 | 0% |
| CO | Primaria | P99 horario | R3 | 30.000 | 2,24 | 0% |
| CO | Primaria | P99 8 horas | R1 | 10.000 | 0,14 | 0% |
| CO | Primaria | P99 8 horas | R2 | 10.000 | 0,12 | 0% |
| CO | Primaria | P99 8 horas | R3 | 10.000 | 0,55 | 0% |

**Tabla 7.5.: Análisis de cumplimiento de normativa vigente para NO** **2** **“Fase de Operación****

| Parámetro | Tipo de<br>Norma | Estadístico | Receptores | Norma | (AP) | % (AP)<br>c/r Norma |
| --- | --- | --- | --- | --- | --- | --- |
| NO2 | Primaria | Promedio<br>Anual | R1 | 100 | 0,10 | 0% |
| NO2 | Primaria | Promedio<br>Anual | R2 | 100 | 0,09 | 0% |
| NO2 | Primaria | Promedio<br>Anual | R3 | 100 | 0,29 | 0% |
| NO2 | Primaria | P99 diario | R1 | 400 | 2,92 | 1% |
| NO2 | Primaria | P99 diario | R2 | 400 | 2,19 | 1% |
| NO2 | Primaria | P99 diario | R3 | 400 | 11,73 | 3% |

**Tabla 7.6.: ** **Análisis de cumplimiento de normativa vigente para SO** **2** **“Fase de****

| Parámetro | Tipo de<br>Norma | Estadístico | Receptores | Norma | (AP) | % (AP)<br>c/r<br>Norma |
| --- | --- | --- | --- | --- | --- | --- |
| SO2 | Primaria | Promedio<br>Anual | R1 | 60 | 0,0001 | 0% |
| SO2 | Primaria | Promedio<br>Anual | R2 | 60 | 0,0001 | 0% |
| SO2 | Primaria | Promedio<br>Anual | R3 | 60 | 0,0003 | 0% |
| SO2 | Primaria | P99 diario | R1 | 150 | 0,0004 | 0% |
| SO2 | Primaria | P99 diario | R2 | 150 | 0,0003 | 0% |
| SO2 | Primaria | P99 diario | R3 | 150 | 0,0012 | 0% |
| SO2 | Primaria | P98,5<br>horario | R1 | 350 | 0,0008 | 0% |
| SO2 | Primaria | P98,5<br>horario | R2 | 350 | 0,0007 | 0% |
| SO2 | Primaria | P98,5<br>horario | R3 | 350 | 0,0033 | 0% |
