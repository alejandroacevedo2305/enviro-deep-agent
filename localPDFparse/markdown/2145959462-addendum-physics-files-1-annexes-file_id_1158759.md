---
title: Tipo de Informe o Capítulo
author: Rodrigo Palacios
date: D:20210107120408-03'00'
language: es
type: report
pages: 45
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Sol del Sur 8 SpA Anexo 16 Actualización de estimación de emisiones atmosféricas
-->

# Sol del Sur 8 SpA Anexo 16 Actualización de estimación de emisiones atmosféricas

## Adenda DIA Parque Fotovoltaico Parronal

### Región de la Araucanía

Enero, 2021

Elaborado por:

**Gestión Ambiental Consultores S.A.**

General del Canto 421, Piso 6, Providencia,

Santiago, Chile - Fono: +56 2 2719 5600

www.gac.cl

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**INDICE GENERAL**

**1.** **Introducción ............................................................................................................................... 1**

**2.** **Objetivos .................................................................................................................................... 1**

**3.** **Estimación de emisiones ............................................................................................................. 2**

3.1. Actividades emisoras ..................................................................................................................... 2

3.2. Metodología de estimación de emisiones .................................................................................... 3

3.3. Factores de emisión ...................................................................................................................... 4

3.3.1 Factores de emisión para material particulado resuspendido .............................................. 4

3.3.2 Factores de emisión para la estimación de emisiones de gases y material particulado ....... 6

3.4. Niveles de actividad ..................................................................................................................... 14

3.4.1 Niveles de actividad de maquinarias ................................................................................... 14

3.4.2 Niveles de actividad de vehículos ........................................................................................ 15

3.4.3 Generadores eléctricos ....................................................................................................... 18

3.4.4 Movimiento de material ...................................................................................................... 19

3.5. Medidas de control y abatimiento de emisiones ........................................................................ 19

3.6. Emisiones ..................................................................................................................................... 21

3.6.1 Emisiones en fase de construcción ..................................................................................... 21

3.6.2 Emisiones en fase de operación .......................................................................................... 28

3.6.3 Emisiones en fase de cierre ................................................................................................. 30

3.6.4 Resumen de emisiones ........................................................................................................ 33

**4.** **Modelo de calidad del aire ........................................................................................................ 35**

4.1. Justificación del modelo de calidad del aire ................................................................................ 35

4.2. Descripción del modelo de calidad del aire ................................................................................ 35

4.2.1 Modelo SCREEN3 ................................................................................................................. 35

4.2.2 Fuentes emisoras y receptores asociados ........................................................................... 36

4.3. Resultados de modelación .......................................................................................................... 39

**5.** **Conclusiones ............................................................................................................................. 40**

i

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**INDICE DE TABLAS**

Tabla 3-1. Cronograma de actividades fase de construcción. ....................................................................... 2

Tabla 3-2. Actividades generadoras de emisiones por fase del Proyecto ..................................................... 3

Tabla 3-3. Factor de emisión para nivelación ................................................................................................ 4

Tabla 3-4. Factor de emisión para excavaciones ........................................................................................... 5

Tabla 3-5: Factor de emisión para transferencia de material (carguío y volteo de camiones) ..................... 5

<!-- INICIO TABLA 3-5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Parámetros|k: factor según tamaño de partícula<br>MP2,5 = 0,105<br>MP10 = 0,75<br>MPS = 1<br>s: % de finos del suelo [8,5 valor por defecto]<br>M: % humedad del material [6,5 valor por defecto]| |Fuente|Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition: Chapter 11,<br>Section 11.9 “Western Surface Coal Mining, 1998”, Table 11.9-2.| |Descripción|Corresponde al factor de emisión de despeje de material (bulldozing/overburden)<br>escalado por 0,75 para ser aplicado a MP10. La unidad de este factor<br>corresponde a kilógramos emitidos por hora excavada| |Nota|El nivel de actividad se determina a través del rendimiento de la maquinaria y el<br>volumen a excavar. Por defecto se considerará para una retroexcavadora con<br>capacidad de palada de 1 m3 un rendimiento igual a 30 m3/h.| -->

**Tabla 3-5: Factor de emisión para transferencia de material (carguío y volteo de camiones)****

| Factor de Emisión (fe) | fe = 0,0016*k*(U/2,2)^1,3/(M/2)^1,4 |
| --- | --- |
| Unidades | kg/t |
| Parámetros | k: factor según tamaño de partícula<br>MP2,5 = 0,053<br>MP10 = 0,35<br>MPS = 0,74<br>U: Velocidad del viento (m/s) [5 m/s valor por defecto]<br>M: Humedad del material [6,5 valor por defecto] |
| Fuente | Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.4<br>“Aggregate Handling and Storage Piles, 2006”. |
| Descripción | Corresponde al factor de emisión de transferencia discreta de material utilizado<br>directamente. La unidad de este factor corresponde a kilogramos emitidos por<br>cada tonelada de material cargado o descargado. |

<!-- Estadísticas: 4 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 3-6. Factores de emisión por resuspensión de MP por circulación de vehículos en caminos pavimentados** 5 -->
<!-- FIN TABLA 3-5 -->


Tabla 3-6. Factores de emisión por resuspensión de MP por circulación de vehículos en caminos

pavimentados ................................................................................................................................................ 5

Tabla 3-7. Factor de emisión por resuspensión de MP por circulación de vehículos pesados en caminos no

pavimentados ................................................................................................................................................ 6

Tabla 3-8. Factores de emisión de gases y MP de maquinarias .................................................................... 7

Tabla 3-9. Factores de emisión en estado estacionario de MP10 y gases para combustión de maquinaria 9

Tabla 3-10. Factores de ajuste transiente y consumo de combustible de maquinarias ............................... 9

Tabla 3-11. Factor de carga, vida media, horas de funcionamiento, edad promedio y factor de edad para

cada tipo de maquinaria ................................................................................................................................ 9

Tabla 3-12. Valor del factor A necesario para determinar el factor de deterioro por tipo de contaminante

..................................................................................................................................................................... 10

Tabla 3-13. Factor de deterioro por tipo de maquinaria y contaminante .................................................. 10

Tabla 3-14. Factor de ajuste de emisión de material particulado dado el contenido de azufre en el

combustible ................................................................................................................................................. 11

Tabla 3-15. Factores de emisión ajustados de MP10 y gases para combustión de maquinaria ................. 11

Tabla 3-16. Factor de Emisión Para Gases y MP de Vehículos .................................................................... 11

Tabla 3-17. Factores de emisión de MP y gases para grupos electrógenos equipo nuevo y consumo de

combustible ................................................................................................................................................. 13

Tabla 3-18. Factor de carga, vida media, horas de funcionamiento, edad promedio y factor de edad para

grupos electrógenos .................................................................................................................................... 13

Tabla 3-19. Valor del factor A necesario para determinar el factor de deterioro por tipo de contaminante

para grupos electrógenos ............................................................................................................................ 13

Tabla 3-20. Factor de deterioro por tipo de contaminante para grupos electrógenos .............................. 13

Tabla 3-21. Factor de ajuste de emisión de material particulado dado el contenido de azufre en el

combustible para grupos electrógenos ....................................................................................................... 13

Tabla 3-22. Factores de emisión ajustados de MP y gases para grupos electrógenos ............................... 14

Tabla 3-23. Niveles de actividad de maquinaria en fases de construcción y operación ............................. 14

Tabla 3-24. Vehículos utilizados en fase de construcción ........................................................................... 15

Tabla 3-25. Vehículos utilizados en fase de operación ............................................................................... 16

Tabla 3-26. Vehículos utilizados en fase de cierre ...................................................................................... 17

Tabla 3-27. Rutas utilizadas ......................................................................................................................... 17

Tabla 3-28. Horas de operación de generadores eléctricos. ....................................................................... 18

Tabla 3-29. Nivel de actividad asociado a nivelación .................................................................................. 19

Tabla 3-30. Nivel de actividad asociado a excavaciones ............................................................................. 19

ii

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

Tabla 3-31. Nivel de actividad asociado a transferencia de material ......................................................... 19

Tabla 3-32. Variables y valores utilizados para eficiencia en humectación. ............................................... 20

Tabla 3-33. Cálculo de agua para humectación de caminos ....................................................................... 21

Tabla 3-34. Emisiones por tránsito de vehículos en caminos pavimentados en fase de construcción ...... 22

Tabla 3-35. Contenido de silt (sL) de caminos pavimentados del Proyecto................................................ 23

Tabla 3-36. Emisiones por tránsito de vehículos en caminos no pavimentados en fase de construcción . 23

Tabla 3-37. Emisiones por tránsito de vehículos en caminos no pavimentados en fase de construcción . 23

Tabla 3-38. Emisiones por nivelación en fase de construcción ................................................................... 24

Tabla 3-39. Emisiones por excavaciones en fase de construcción .............................................................. 24

Tabla 3-40. Emisiones por transferencia de material en fase de construcción .......................................... 24

Tabla 3-41. Emisiones por motores de maquinaria en fase de construcción ............................................. 25

Tabla 3-42. Emisiones por operación de generadores en fase de construcción ......................................... 25

Tabla 3-43. Emisiones por combustión de motores de vehículos fase de construcción ............................ 26

Tabla 3-44. Emisiones por tránsito de vehículos en caminos pavimentados en fase de operación ........... 28

Tabla 3-45. Emisiones por tránsito de vehículos en caminos no pavimentados en fase de operación ...... 28

Tabla 3-46. Emisiones por tránsito de vehículos en caminos no pavimentados en fase de operación ...... 28

Tabla 3-47. Emisiones por combustión de motores de vehículos en fase de operación ............................ 29

Tabla 3-48. Emisiones por motores de maquinaria en fase de operación .................................................. 29

Tabla 3-49. Emisiones por tránsito de vehículos en caminos pavimentados en fase de cierre .................. 30

Tabla 3-50. Emisiones por tránsito de vehículos en caminos no pavimentados en fase de cierre ............. 30

Tabla 3-51. Emisiones por tránsito de vehículos en caminos no pavimentados en fase de cierre ............. 31

Tabla 3-52. Emisiones por operación de generadores en fase de cierre .................................................... 31

Tabla 3-53. Emisiones por combustión de motores de vehículos en fase de cierre ................................... 32

Tabla 3-54. Emisiones totales en fase de construcción............................................................................... 33

Tabla 3-55. Emisiones totales en fase de operación ................................................................................... 33

Tabla 3-56. Emisiones totales en fase de cierre .......................................................................................... 34

Tabla 4-1. Factor de corrección para concentraciones de SCREEN3 ........................................................... 36

Tabla 4-2. Características y emisiones de la fuente emisora Parque Fotovoltaico y caminos internos ..... 36

Tabla 4-3. Características y emisiones de la fuente emisora Ruta S/R ....................................................... 37

Tabla 4-4. Receptores en área de influencia de la Planta Fotovoltaica ...................................................... 38

Tabla 4-5. Clases de estabilidad .................................................................................................................. 39

Tabla 4-6. Resultados de modelación de MP10 .......................................................................................... 39

iii

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**INDICE DE FIGURAS**

Figura 4-1. Ubicación de receptores en área de influencia del Parque Fotovoltaico ................................. 38

iv

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

##### 1. INTRODUCCIÓN

El presente informe contiene los resultados de la actualización de la estimación de emisiones atmosféricas,

para material particulado (MPS, MP10 y MP2,5), dióxido de nitrógeno (NO 2 ), monóxido de carbono (CO) y

anhídrido sulfuroso (SO 2 ) asociadas a las actividades de construcción, operación y cierre del proyecto

Parque Fotovoltaico Parronal (en adelante, el Proyecto), ubicado en la comuna de Renaico, Región de la

Araucanía.

El Parque contará con una potencia nominal instalada de 9 MWac, compuesto de un máximo de 32.400

módulos fotovoltaicos, y un tendido eléctrico aéreo de 23 kV de conexión a la red de distribución.

El Proyecto, además, comprende la construcción y operación de obras menores tales como caminos de

acceso, sala de control y centros de transformación, todas obras de carácter permanente, además de la

instalación de faena, que corresponde a una instalación temporal durante la fase de construcción del

Proyecto.

Debido al tipo de Proyecto, se espera que las emisiones que se producirán en la fase de construcción (que

corresponde a la fase de mayores emisiones), sean de poca relevancia, además de producirse durante un

periodo acotado. La fase de operación del Proyecto contempla, como actividades susceptibles de producir

emisiones atmosféricas, el tránsito de vehículos para transporte de personal, residuos e insumos.

##### 2. OBJETIVOS

 - Estimar las emisiones atmosféricas producto de las actividades a desarrollar durante la fase de

construcción del Proyecto.

 - Estimar las emisiones atmosféricas producto de las actividades a desarrollar durante la fase de

operación del Proyecto.

 - Estimar las emisiones atmosféricas producto de las actividades a desarrollar durante la fase de

cierre del Proyecto.

1

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

##### 3. ESTIMACIÓN DE EMISIONES

A continuación, se describen las actividades identificadas como generadoras de emisiones atmosféricas

durante las fases de construcción, operación y cierre del Proyecto, la metodología utilizada para la

estimación de emisiones y las emisiones estimadas para cada una de las actividades identificadas.

##### 3.1. Actividades emisoras

Las emisiones a la atmósfera que generará el Proyecto, en sus fases de construcción, operación y cierre,

corresponderán a emisiones fugitivas de material particulado respirable MP10, MP2.5, material

particulado sedimentable (MPS), gases de combustión de vehículos y maquinarias, y gases de equipos

generadores, que serán utilizados en las distintas fases que comprende este proyecto.

La fase de construcción tendrá una duración de 6 meses, la fase de operación tendrá una duración de 25

años (aunque debido a las características de este tipo de instalaciones, se espera que el período de

funcionamiento de estas unidades se extienda en el tiempo) y la fase de cierre durará 3 meses. En la Tabla

3-1 se presenta el cronograma de actividades para la fase de construcción del Proyecto y en la Tabla 3-2

se presenta las actividades del proyecto generadoras de emisiones atmosféricas.

**Tabla 3-1. Cronograma de actividades fase de construcción.**

|Actividades|Mes 1|Mes 2|Mes 3|Mes 4|Mes 5|Mes 6|
|---|---|---|---|---|---|---|
|Cercado del parque solar|||||||
|Habilitación faena para obras temporales y permanentes|||||||
|Habilitación de terrenos y de caminos interiores|||||||
|Hincado de estructuras|||||||
|Montaje de paneles|||||||
|Conexiones eléctricas|||||||
|Obras de drenaje de aguas lluvias|||||||
|Pruebas eléctricas y puesta en marcha|||||||
|Desmantelamiento de obras temporales|||||||
|Energización|||||||
|Interconexión|||||||

Fuente: GAC

2

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 3-2. Actividades generadoras de emisiones por fase del Proyecto**

|Fase del<br>Proyecto|Actividad Generadora de Emisiones|Contaminante|
|---|---|---|
|Construcción|Nivelación de superficies|MP10, MP2,5 y MPS|
|Construcción|Excavaciones|Excavaciones|
|Construcción|Transferencias de material excavado|Transferencias de material excavado|
|Construcción|Tránsito de vehículos por caminos pavimentados|Tránsito de vehículos por caminos pavimentados|
|Construcción|Tránsito de vehículos por caminos no pavimentados|Tránsito de vehículos por caminos no pavimentados|
|Construcción|Motores de maquinaria|MP10, MP2,5, MPS,<br>NOx, CO, SO2 y COV|
|Construcción|Motores de vehículos de transporte|Motores de vehículos de transporte|
|Construcción|Equipo generador de electricidad|Equipo generador de electricidad|
|Operación|Tránsito de vehículos por caminos pavimentados|MP10, MP2,5 y MPS|
|Operación|Tránsito de vehículos por caminos no pavimentados|Tránsito de vehículos por caminos no pavimentados|
|Operación|Motores de vehículos de transporte|MP10, MP2,5, MPS,<br>NOx, CO, SO2 y COV|
|Operación|Motores de maquinaria|Motores de maquinaria|
|Cierre|Tránsito de vehículos por caminos pavimentados|MP10, MP2,5 y MPS|
|Cierre|Tránsito de vehículos por caminos no pavimentados|Tránsito de vehículos por caminos no pavimentados|
|Cierre|Motores de vehículos de transporte|MP10, MP2,5, MPS,<br>NOx, CO, SO2 y COV|
|Cierre|Equipos generadores de electricidad|Equipos generadores de electricidad|

Fuente: GAC

##### 3.2. Metodología de estimación de emisiones

Para estimar las emisiones generadas por las distintas fases del Proyecto se han utilizado factores de

emisión para cada actividad. La ecuación general para estimar las emisiones de cualquier actividad es la

siguiente:

Donde:

E: Emisión (t/año)

fe : Factor de emisión
##### E= fe∗Na∗(1 − 100 [Ea] [)] Na : Nivel de la actividad

Ea : Eficiencia de abatimiento

Las emisiones de material particulado (MP10, MP2,5 y MPS) y gases (CO, NO X, COV y SO 2 ), generadas por

las actividades del proyecto, en cada una de sus fases, se han estimado utilizando los documentos “Informe

Final Servicio de Recopilación y Sistematización de Factores de Emisión al Aire para el Servicio de

Evaluación Ambiental” (2015), la “Guía para la estimación de emisiones atmosféricas de proyectos

inmobiliarios para la Región Metropolitana del Ministerio del Medio Ambiente” (2012) y los factores de

emisión del documento AP 42 de la EPA (Fifth Edition, Compilation of Air Pollutant Emission Factors,

Volume 1: Stationary Point and Area Sources, United States - Environmental Protection Agency).

Para el cálculo de los factores de emisiones, se han utilizado valores de parámetros locales, y cuando no

se cuenta con ellos, fueron utilizados los valores por defecto que establece la “Guía para la estimación de

##### E= fe∗Na∗(1 − 100 [Ea]

##### 100 [)]

3

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

emisiones atmosféricas de proyectos inmobiliarios para la Región Metropolitana” del Ministerio del Medio

Ambiente, enero 2012, y el documento “Informe Final Servicio de Recopilación y Sistematización de

Factores de Emisión al Aire para el Servicio de Evaluación Ambiental” (2015).

##### 3.3. Factores de emisión

Los factores de emisión (fe) corresponden a ecuaciones o expresiones matemáticas que permiten estimar

tasas unitarias de emisiones atmosféricas. Para el caso específico de las operaciones relacionadas con este

proyecto, en cada una de sus fases, se utilizaron los modelos matemáticos para factores de emisión,

propuestos en los documentos citados en el punto anterior.

Estos factores de emisión proporcionan una tasa representativa de la cantidad de agentes contaminantes

por unidad de peso, volumen, distancia o duración de la actividad. En muchos casos, los factores de

emisión representan la media de un conjunto de datos disponibles y, por lo general, se asume como

representativo de períodos de largo plazo.

A continuación, se presentan los factores de emisión utilizados para estimar las emisiones del proyecto.

En primer lugar, se presentan los factores de emisión de material particulado resuspendido y

posteriormente los factores de emisión de material particulado y gases asociados a procesos de

combustión.

###### 3.3.1 Factores de emisión para material particulado resuspendido

Las expresiones de factores de emisión para la estimación de emisiones de material particulado
resuspendido, se presentan a continuación [1] .

**Tabla 3-3. Factor de emisión para nivelación**

|Factor de Emisión (fe)|fe = k*0,0056*(S)^2,0 [Para MP10]<br>fe = k*0,0034*(S)^2,5 [Para MPS y MP2,5]|
|---|---|
|Unidades|kg/veh-km|
|Parámetros|k: factor según tamaño de partícula<br>MP2,5 = 0,0,031<br>M910 = 0,60<br>MPS = 1<br>S: Velocidad del vehículo nivelador (km/h) [11,4 nivel de referencia]|
|Fuente|Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition: Chapter 13,<br>Section 11.9“Western Surface Coal Mining, 1998” (Grading)|
|Descripción|Corresponde al factor de emisión de nivelación de terrenos (grading). La unidad<br>de este factor corresponde a kilógramos emitidos por kilómetro recorrido por<br>el vehículo nivelador en el proceso.|
|Nivel de actividad|El nivel de actividad se determina según la distancia que recorre el vehículo|

1 Fuentes de información: “Guía para la estimación de emisiones atmosféricas de proyectos inmobiliarios para la Región
Metropolitana” del Ministerio del Medio Ambiente, enero 2012, y el documento “Informe Final Servicio de Recopilación y
Sistematización de Factores de Emisión al Aire para el Servicio de Evaluación Ambiental” (2015).

4

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

|Factor de Emisión (fe)|fe = k*0,0056*(S)^2,0 [Para MP10]<br>fe = k*0,0034*(S)^2,5 [Para MPS y MP2,5]|
|---|---|
||nivelador por el área a nivelar.|

**Tabla 3-4. Factor de emisión para excavaciones**

|Factor de Emisión (fe)|fe = 0,45*k*(s^1,5/M^1,4) [Para PM10]<br>fe = 2,6*k*(s^1,2/M^1,3) [Para MPS y MP2,5]|
|---|---|
|Unidades|kg/h|
|Parámetros|k: factor según tamaño de partícula<br>MP2,5 = 0,105<br>MP10 = 0,75<br>MPS = 1<br>s: % de finos del suelo [8,5 valor por defecto]<br>M: % humedad del material [6,5 valor por defecto]|
|Fuente|Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition: Chapter 11,<br>Section 11.9 “Western Surface Coal Mining, 1998”, Table 11.9-2.|
|Descripción|Corresponde al factor de emisión de despeje de material (bulldozing/overburden)<br>escalado por 0,75 para ser aplicado a MP10. La unidad de este factor<br>corresponde a kilógramos emitidos por hora excavada|
|Nota|El nivel de actividad se determina a través del rendimiento de la maquinaria y el<br>volumen a excavar. Por defecto se considerará para una retroexcavadora con<br>capacidad de palada de 1 m3 un rendimiento igual a 30 m3/h.|

**Tabla 3-5: Factor de emisión para transferencia de material (carguío y volteo de camiones)**

|Factor de Emisión (fe)|fe = 0,0016*k*(U/2,2)^1,3/(M/2)^1,4|
|---|---|
|Unidades|kg/t|
|Parámetros|k: factor según tamaño de partícula<br>MP2,5 = 0,053<br>MP10 = 0,35<br>MPS = 0,74<br>U: Velocidad del viento (m/s) [5 m/s valor por defecto]<br>M: Humedad del material [6,5 valor por defecto]|
|Fuente|Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.4<br>“Aggregate Handling and Storage Piles, 2006”.|
|Descripción|Corresponde al factor de emisión de transferencia discreta de material utilizado<br>directamente. La unidad de este factor corresponde a kilogramos emitidos por<br>cada tonelada de material cargado o descargado.|

**Tabla 3-6. Factores de emisión por resuspensión de MP por circulación de vehículos en caminos pavimentados**

5

|Factor de Emisión (fe)|fe = k*(sL)^0,91*W^1,02*(1-P/4N)|
|---|---|
|Unidades|g/km|
|Parámetros|k: factor según tamaño de partícula<br>MP2,5 = 0,15|

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

|Factor de Emisión (fe)|fe = k*(sL)^0,91*W^1,02*(1-P/4N)|
|---|---|
||MP10 = 0,62<br>MPS = 3,23<br>sL: Carga de fino de la superficie, (g/m2)<br>W: Peso promedio ponderado de la flota que circula por las vías (t)<br>P: número de días con al menos 0,254 mm de precipitación durante el período<br>considerado<br>N: número de días del periodo considerado|
|Fuente|Compilation of Air Pollutant Emission Factors, AP-42: Chapter 13, Section 13.2.1<br>“Paved Roads, 2011”.|
|Descripción|Corresponde al factor de emisión de material particulado resuspendido por<br>tránsito de vehículos por caminos pavimentados. La unidad de este factor de<br>emisión es gramos de MP emitidos por kilómetro recorrido.|

**Tabla 3-7. Factor de emisión por resuspensión de MP por circulación de vehículos pesados en caminos no**

**pavimentados**

|Factor de Emisión (fe)|fe = 281,9*k*(s/12)^0,9*(W/2,7)^0,45*(1-P/365) [Para MP10 y MP2,5]<br>fe = 281,9*k*(s/12)^0,7*(W/2,7)^0,45*(1-P/365) [Para MPS]|
|---|---|
|Unidades|g/km|
|Parámetros|k: factor según tamaño de partícula<br>MP2,5 = 0,15<br>MP10 = 1,5<br>MPS = 4,9<br>s: % de finos del suelo [8,5 valor por defecto]<br>W: Peso promedio de la flota que circula por las vías (t)<br>P: número de días en un año con al menos 0,254 mm de precipitación|
|Fuente|Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.2<br>“Unpaved Roads” e Informe Final Servicio de Recopilación y Sistematización de<br>Factores de Emisión al Aire para el Servicio de Evaluación Ambiental|
|Descripción|Corresponde al factor de emisión de tránsito por caminos no pavimentados<br>determinado para sitios industriales. La unidad de este factor de emisión es<br>gramos de MP emitidos por kilómetro recorrido.|
|Nota|Dadas las características de la flota utilizada en la determinación de este factor<br>de emisión, su aplicación se reconoce válida para una flota de vehículos<br>pesados, es decir, cuyo peso promedio exceda las 2,7 toneladas métricas.|

###### 3.3.2 Factores de emisión para la estimación de emisiones de gases y material particulado

Los factores de emisión de gases y material particulado de combustión, asociados a la operación de la

maquinaria, vehículos y generadores durante las distintas fases del proyecto, se presentan en las tablas

siguientes.

6

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 3-8. Factores de emisión de gases y MP de maquinarias**

|Factor de Emisión (fe)|E = (FP × t × C × P)|
|---|---|
|Unidades|g/día|
|Parámetros|FP: factor según potencia<br>t: tiempo de operación diaria (h)<br>C: Porcentaje de carga<br>P: Potencia Nominal (kw)|
|Fuente|Guía para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios para<br>la Región Metropolitana, Tabla 4.9|
|Descripción|Corresponde al factor de emisión de combustión de los motores de la maquinaria<br>fuera de ruta.|

Con respecto a los factores de emisión para la maquinaria, los mismos fueron calculados a partir de la

metodología propuesta por USEPA, recogida en el documento “Exhaust and Crankcase Emission Factors

for Nonroad Engine Modeling - Compression-Ignition (USEPA)” [2] .

La metodología, similar, pero no idéntica entre gases y material particulado considera que:

FE (HC, CO, NOx) = FE ss × FAT× FD

Donde:

 - FE: Factor de emisión resultante luego de considerar ajustes para dar cuenta del estado transiente

y el deterioro de la maquinaria (g/hp-h)

 - FE ss : Factor de emisión en estado estacionario (g/hp-h)

 - FAT: Factor de ajuste transiente (adimensional)

 - FD: Factor de deterioro (adimensional), que a su vez se calcula como:

FD= 1 + A× (Factor de edad) [b] ; si Factor de edad ≥1

FD= 1 + A ; si Factor de edad< 1

Donde:

A, b: Constantes que dependen del contaminante/tecnología con b = 1

Factor de edad= fracción de la vida media gastada

= [Horas acumuladas× Factor de carga]

Vida media a plena carga (horas)

En el caso del material particulado:

2 [Disponible en su versión más actual a la fecha (julio 2010) en: https://nepis.epa.gov/Exe/ZyPDF.cgi?Dockey=P10081UI.pdf](https://nepis.epa.gov/Exe/ZyPDF.cgi?Dockey=P10081UI.pdf)

7

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

FE (MP) = FE ss × FAT× FD× S MPaj

Donde a las variables consideradas en el caso de los gases se adiciona un factor de ajuste por el contenido

de azufre en el combustible, el cual se determina a través de la siguiente ecuación:

S MPaj = BSFC× 453,6 × 7,0 × soxcnv× 0,01 × (soxbas−soxdsl)

Donde:

 - S MPaj : Factor de ajuste material particulado por contenido de azufre (g/hp-h)

 - BSFC: Consumo de combustible ajustado (lb/hp-h)

 - 453,6: Factor de conversión de libras a gramos

 - 7,0: gramos de sulfato por gramos de azufre

 - soxcnv: Fracción de azufre que se convierte en material particulado (0,02247 por defecto)

 - 0,01: Factor de conversión desde porcentaje en peso a fracción.

 - soxbas: Contenido de azufre por defecto en combustible (0,33%)

 - soxdsl: Porcentaje en peso de azufre en el combustible (50 ppm = 0,005% en el caso de Chile,

excepto en región Metropolitana)

Finalmente, el factor de emisión de SO 2 se calcula de la siguiente manera:

FE SO 2 = (BSFC× 453,6 × (1 −soxcnv) −FE HC ) × 0,01 × soxdsl× 2

Donde:

 - FE SO2 : Factor de emisión de SO 2 (g/hp-h)

 - BSFC: Consumo de combustible ajustado (lb/hp-h)

 - 453,6: Factor de conversión de libras a gramos

 - soxcnv: Fracción de azufre que se convierte en material particulado (0,02247 por defecto)

 - FE HC : Factor de emisión de hidrocarburo calculado.

 - 0,01: Factor de conversión desde porcentaje en peso a fracción.

 - soxdsl: Porcentaje en peso de azufre en el combustible (50 ppm = 0,005% en el caso de Chile,

excepto en región Metropolitana)

Las variables utilizadas en el cálculo, excepto aquellas cuyo valor ya ha sido indicado, se encuentran

tabuladas en el documento mencionado como fuente y, complementariamente, en el documento

“Median Life, Annual Activity, and Load Factor Values for Nonroad Engine Emissions Modeling” [3] . Estos

valores dependen del tipo y potencia de la maquinaria de acuerdo al siguiente detalle.

3 Disponible en su versión más actual a la fecha (julio 2010) en: https://nepis.epa.gov/Exe/ZyPDF.cgi?Dockey=P10081RV.pdf

8

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 3-9. Factores de emisión en estado estacionario de MP10 y gases para combustión de maquinaria**

|Fase|Equipo|Potencia<br>(kW)|Potencia<br>(hp)|FE en caliente (g/hp-h)|Col6|Col7|Col8|Estándar<br>de<br>emisión|
|---|---|---|---|---|---|---|---|---|
|**Fase**|**Equipo**|**Potencia**<br>**(kW)**|**Potencia**<br>**(hp)**|**HC**|**CO**|**NOx**|**PM**|**PM**|
|Construcción|Grúa|30|40|0,2789|1,5323|4,7279|0,3389|Tier 2|
|Construcción|Toro/Manitou|30|40|0,2789|1,5323|4,7279|0,3389|Tier 2|
|Construcción|Excavadora|70|94|0,1836|2,3655|3,0|0,30|Tier 3|
|Construcción|Retroexcavadora|70|94|0,1836|2,3655|3,0|0,30|Tier 3|
|Construcción|Bulldozer|300|402|0,1669|0,8425|2,5|0,15|Tier 3|
|Construcción|Cargadora frontal|180|241|0,1836|0,7475|2,5|0,15|Tier 3|
|Construcción|Hincadora/Perforadora|40|54|0,1836|2,3655|3,0|0,30|Tier 3|
|Construcción|Motoniveladora|110|148|0,1836|0,8667|2,5|0,22|Tier 3|
|Construcción|Rodillo|20|27|0,2789|1,5323|4,7279|0,3389|Tier 2|
|Operación|Tractor|14|19|0,4380|2,1610|4,4399|0,2665|Tier 2|

Fuente: Factores provienen de Tablas 4, 5, 6 y 7 del documento Exhaust and Crankcase Emission Factors for Nonroad Engine

Modeling - Compression-Ignition (USEPA).

**Tabla 3-10. Factores de ajuste transiente y consumo de combustible de maquinarias**

|Fase|Equipo|Potencia<br>(hp)|Factor de ajuste transiente|Col5|Col6|Col7|BSFC ss<br>(lb/hp-<br>hr)|BSFC<br>TAF|
|---|---|---|---|---|---|---|---|---|
|**Fase**|**Equipo**|**Potencia**<br>**(hp)**|**HC**|**CO**|**NOx**|**PM**|**PM**|**PM**|
|Construcción|Grúa|40|1,00|1,00|1,00|1,00|0,408|1,00|
|Construcción|Toro/Manitou|40|1,05|1,53|0,95|1,23|0,408|1,01|
|Construcción|Excavadora|94|1,05|1,53|1,04|1,47|0,408|1,01|
|Construcción|Retroexcavadora|94|2,29|2,57|1,21|2,37|0,408|1,18|
|Construcción|Bulldozer|402|1,05|1,53|1,04|1,47|0,367|1,01|
|Construcción|Cargadora frontal|241|1,05|1,53|1,04|1,47|0,367|1,01|
|Construcción|Hincadora/Perforadora|54|1,05|1,53|1,04|1,47|0,408|1,01|
|Construcción|Motoniveladora|148|1,05|1,53|1,04|1,47|0,367|1,01|
|Construcción|Rodillo|27|1,05|1,53|1,04|1,47|0,408|1,01|
|Operación|Tractor|19|1,00|1,00|1,00|1,00|0,408|1,00|

Fuente: Factores provienen de Tablas A4 y A5 del documento Exhaust and Crankcase Emission Factors for Nonroad Engine

Modeling - Compression-Ignition (USEPA).

**Tabla 3-11. Factor de carga, vida media, horas de funcionamiento, edad promedio y factor de edad para cada**

**tipo de maquinaria**

|Fase|Equipo|Potencia<br>(hp)|Factor de<br>Carga|Vida<br>Media<br>(horas)|Actividad<br>(horas/año)|Edad<br>promedio<br>(años|Factor<br>de edad|
|---|---|---|---|---|---|---|---|
|Construcción|Grúa|40|0,47|2500|415|3|0,234|
|Construcción|Toro/Manitou|40|0,63|2500|413|3|0,312|
|Construcción|Excavadora|94|0,53|4667|378|3|0,129|

9

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

|Fase|Equipo|Potencia<br>(hp)|Factor de<br>Carga|Vida<br>Media<br>(horas)|Actividad<br>(horas/año)|Edad<br>promedio<br>(años|Factor<br>de edad|
|---|---|---|---|---|---|---|---|
||Retroexcavadora|94|0,48|4667|870|3|0,268|
||Bulldozer|402|0,80|7000|700|3|0,240|
||Cargadora frontal|241|0,71|4667|512|3|0,234|
||Hincadora/Perforadora|54|0,48|4667|371|3|0,114|
||Motoniveladora|148|0,64|4667|504|3|0,207|
||Rodillo|27|0,49|2500|488|3|0,287|
|Operación|Tractor|19|0,44|2500|721|3|0,381|

Fuente: Factores de carga y horas de actividad provienen del Appendix A, y la vida media de las tablas 1 y 2 del documento

“Median Life, Annual Activity, and Load Factor Values for Nonroad Engine Emissions Modeling”. Por su parte, el factor de edad

fue calculado según la ecuación correspondiente, indicada previamente en el presente informe.

**Tabla 3-12. Valor del factor A necesario para determinar el factor de deterioro por tipo de contaminante**

|Factor de deterioro relativo (A)|Col2|Col3|Col4|Estándar|
|---|---|---|---|---|
|**HC**|**CO**|**NOx**|**MP**|**MP**|
|0,036|0,101|0,024|0,473|Tier 1|
|0,034|0,101|0,009|0,473|Tier 2|
|0,027|0,151|0,008|0,473|Tier 3+|

Fuente: Tabla A6 del documento Exhaust and Crankcase Emission Factors for Nonroad Engine Modeling - Compression-Ignition.

**Tabla 3-13. Factor de deterioro por tipo de maquinaria y contaminante**

|Fase|Equipo|Potencia<br>(hp)|Factor de deterioro|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Fase**|**Equipo**|**Potencia**<br>**(hp)**|**HC**|**CO**|**NOx**|**PM**|
|Construcción|Grúa|40|1,008|1,024|1,002|1,111|
|Construcción|Toro/Manitou|40|1,011|1,032|1,003|1,148|
|Construcción|Excavadora|94|1,003|1,019|1,001|1,061|
|Construcción|Retroexcavadora|94|1,007|1,041|1,002|1,127|
|Construcción|Bulldozer|402|1,006|1,036|1,002|1,114|
|Construcción|Cargadora frontal|241|1,006|1,035|1,002|1,111|
|Construcción|Hincadora/Perforadora|54|1,003|1,017|1,001|1,054|
|Construcción|Motoniveladora|148|1,006|1,031|1,002|1,098|
|Construcción|Rodillo|27|1,010|1,029|1,003|1,136|
|Operación|Tractor|19|1,013|1,038|1,003|1,180|

10

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 3-14. Factor de ajuste de emisión de material particulado dado el contenido de azufre en el combustible**

|Fase|Equipo|Potencia<br>(hp)|BSFC|soxcnv|soxbas|soxdsl|S<br>PMadj|
|---|---|---|---|---|---|---|---|
|Construcción|Grúa|40|0,4080|0,02247|0,33|0,005|0,0946|
|Construcción|Toro/Manitou|40|0,4121|0,02247|0,33|0,005|0,0956|
|Construcción|Excavadora|94|0,4121|0,02247|0,33|0,005|0,0956|
|Construcción|Retroexcavadora|94|0,4814|0,02247|0,33|0,005|0,1116|
|Construcción|Bulldozer|402|0,3707|0,02247|0,33|0,005|0,0859|
|Construcción|Cargadora frontal|241|0,3707|0,02247|0,33|0,005|0,0859|
|Construcción|Hincadora/Perforadora|54|0,4121|0,02247|0,33|0,005|0,0956|
|Construcción|Motoniveladora|148|0,3707|0,02247|0,33|0,005|0,0859|
|Construcción|Rodillo|27|0,4121|0,02247|0,33|0,005|0,0956|
|Operación|Tractor|19|0,4080|0,02247|0,33|0,005|0,0946|

**Tabla 3-15. Factores de emisión ajustados de MP10 y gases para combustión de maquinaria**

|Fase|Equipo|Potencia<br>(hp)|Factor de emisión (g/hp-h)|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Fase**|**Equipo**|**Potencia**<br>**(hp)**|**HC**|**CO**|**NOx**|**MP10**|**SO2 **|
|Construcción|Grúa|40|0,281|1,569|4,738|0,376|0,018|
|Construcción|Toro/Manitou|40|0,296|2,418|4,504|0,478|0,018|
|Construcción|Excavadora|94|0,193|3,690|3,123|0,468|0,018|
|Construcción|Retroexcavadora|94|0,423|6,326|3,638|0,801|0,021|
|Construcción|Bulldozer|402|0,176|1,336|2,605|0,246|0,016|
|Construcción|Cargadora frontal|241|0,194|1,184|2,605|0,245|0,016|
|Construcción|Hincadora/Perforadora|54|0,193|3,682|3,123|0,465|0,018|
|Construcción|Motoniveladora|148|0,194|1,368|2,604|0,355|0,016|
|Construcción|Rodillo|27|0,296|2,412|4,930|0,566|0,018|
|Operación|Tractor|19|0,444|2,244|4,455|0,314|0,018|

Fuente: Estimación propia a partir de la metodología propuesta en el documento Exhaust and Crankcase Emission Factors for

Nonroad Engine Modeling - Compression-Ignition (USEPA).

A continuación, se presenta el cálculo de los factores de emisión de material particulado y gases producto

de la combustión de motores de los vehículos que se utilizarán en el Proyecto.

**Tabla 3-16. Factor de Emisión Para Gases y MP de Vehículos**

|Categoría|Contaminante|Factor de emisión (g/km)|
|---|---|---|
|Camiones Pesados<br>Diésel Tipo 3|CO|(1,24588358438859+(103,700537481749/(1+exp((((-1)*-<br>1,3906312471446)+(0,543451750078654*ln(V)))+(0,0390066425998189* V)))))|
|Camiones Pesados<br>Diésel Tipo 3|HC|((0,135938586321894+(0,71588074810547*exp(((-<br>1)*0,0234666513590177)*V)))+(2,79878282504916*exp(((-<br>1)*0,123459782380517)*V)))|
|Camiones Pesados<br>Diésel Tipo 3|NOx|((5,58300975720938+(14,5724996214701*exp(((-<br>1)*0,0510403515051286)*V)))+(45,651882800859*exp(((-|

11

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

|Categoría|Contaminante|Factor de emisión (g/km)|
|---|---|---|
|||1)*0,309240087785118)*V)))|
||MP|((0,100820480611018+(0,424449762706025*exp(((-<br>1)*0,0416436785215947)*V)))+(0,864328026775096*exp(((-<br>1)*0,159945936589218)*V)))|
|Buses Particulares|CO|((1,08632604031267+(6,46823166382744*exp(((-<br>1)*0,0457909676088093)*V)))+(15,0010348169023*exp(((-<br>1)*0,221904651804259)*V)))|
|Buses Particulares|HC|(0,227231246172132+(15,6623993601925/(1+exp((((-1)*-<br>0,530825258433305)+(0,64893877880533*ln(V)))+(0,0270342446309713*V)))))|
|Buses Particulares|NOx|((5,30542698745506+(21,8812199241423*exp(((-<br>1)*0,0529967144180243)*V)))+(90,0551365078442*exp(((-<br>1)*0,247649925809256)*V)))|
|Buses Particulares|MP*|(0,0824673698756213+(1,06820321325441/(1+exp((((-<br>1)*2,35097203495455)+(1,08187915615308*ln(V)))+(0,0118433684419714*V)))))|
|Vehículos<br>Comerciales Diésel<br>Tipo 2|CO|0,82*(0,000223*V^2-0,026*k18+1,076)|
|Vehículos<br>Comerciales Diésel<br>Tipo 2|HC|0,62*(0,0000175*V^2-0,00284*V+0,2162)|
|Vehículos<br>Comerciales Diésel<br>Tipo 2|NOx|0,84*(0,000241*V^2-0,03181*V+2,0247)|
|Vehículos<br>Comerciales Diésel<br>Tipo 2|MP*|0,67*(0,000045*V^2-0,004885*V+0,1932)|

(*) Se considera que todo el material particulado emitido corresponde a MP2,5

Fuente: Anexo 2 de la Guía para la estimación de emisiones atmosféricas de proyectos inmobiliarios para la Región Metropolitana,

2012.

Respecto de los grupos generadores se ha considerado la “Minuta estimación de emisiones de Grupos

Electrógenos” del Ministerio del Medio Ambiente, 2017, basada en la metodología EPA para motores fuera

de ruta, misma metodología utilizada para obtener los factores de emisión de la maquinaria descrita más

arriba en el presente informe.

12

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 3-17. Factores de emisión de MP y gases para grupos electrógenos equipo nuevo y consumo de**

**combustible**

|Fase|Combustible|Potencia<br>(kW)|Estándar<br>de<br>emisión|Factor de emisión equipo nuevo (g/kW-h)|Col6|Col7|Col8|BSFC|
|---|---|---|---|---|---|---|---|---|
|**Fase**|**Combustible**|**Potencia**<br>**(kW)**|**Estándar**<br>**de**<br>**emisión**|**MP**|**NOx**|**CO**|**HC**|**HC**|
|Construcción|Diesel|40|Tier 2|0,322|6,303|3,172|0,492|248|
|Cierre|Diesel|40|Tier 2|0,322|6,303|3,172|0,492|248|

**Tabla 3-18. Factor de carga, vida media, horas de funcionamiento, edad promedio y factor de edad para grupos**

**electrógenos**

|Fase|Horas de<br>operación (h)|Factor de<br>carga|Vida media<br>(h)|Vida útil<br>(años)|Edad<br>promedio<br>(años)|Factor de<br>edad|
|---|---|---|---|---|---|---|
|Construcción|960|0,7|4667|7|2|0,346|
|Cierre|576|0,7|4667|12|2|0,173|

**Tabla 3-19. Valor del factor A necesario para determinar el factor de deterioro por tipo de contaminante para**

**grupos electrógenos**

|Estándar de emisión|Factor de deterioro relativo (A)|Col3|Col4|Col5|
|---|---|---|---|---|
|**Estándar de emisión**|**MP**|**NOx**|**CO**|**HC**|
|Tier 2|0,473|0,009|0,101|0,034|

**Tabla 3-20. Factor de deterioro por tipo de contaminante para grupos electrógenos**

|Fase|Combustible|Potencia<br>(kW)|Estándar de<br>emisión|Factor de deterioro|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Fase**|**Combustible**|**Potencia**<br>**(kW)**|**Estándar de**<br>**emisión**|**MP**|**NOx**|**CO**|**HC**|
|Construcción|Diesel|40|Tier 2|1,136|1,003|1,029|1,010|
|Cierre|Diesel|40|Tier 2|1,082|1,002|1,017|1,006|

**Tabla 3-21. Factor de ajuste de emisión de material particulado dado el contenido de azufre en el combustible**

**para grupos electrógenos**

|Fase|Combustible|Potencia<br>(kW)|Estándar<br>de<br>emisión|BSFC|TAF|soxcnv|soxbas|soxdsl|S<br>PMadj|
|---|---|---|---|---|---|---|---|---|---|
|Construcción|Diesel|40|Tier 2|248|1|0,02247|0,2|0,005|0,0761|
|Cierre|Diesel|40|Tier 2|248|1|0,02247|0,2|0,005|0,0761|

13

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 3-22. Factores de emisión ajustados de MP y gases para grupos electrógenos**

|Fase|Combustible|Potencia<br>(kW)|Estándar<br>de<br>emisión|Factor de emisión (g/kW-h)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Fase**|**Combustible**|**Potencia**<br>**(kW)**|**Estándar**<br>**de**<br>**emisión**|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|
|Construcción|Diesel|40|Tier 2|0,290|0,281|6,319|3,264|0,497|0,024|
|Cierre|Diesel|40|Tier 2|0,272|0,264|6,313|3,227|0,495|0,024|

##### 3.4. Niveles de actividad

A continuación, se reportan los niveles de actividad considerados para las actividades emisoras en cada

fase del Proyecto.

La fase de construcción tendrá una duración de 6 meses, y los niveles de actividad son reportados como

totales para esta fase. La fase de operación corresponde a la vida útil del proyecto, que se estima en 25

años, por lo tanto, los niveles de actividad son reportados para un año de operación. Finalmente, la fase

de cierre del Proyecto tendrá una duración de 3 meses.

El nivel de actividad (Na) utilizado para calcular las emisiones de cada actividad, en cada una de las fases

del proyecto, se presenta en las tablas siguientes.

###### 3.4.1 Niveles de actividad de maquinarias

El nivel de actividad de la maquinaria, durante cada una de las fases del proyecto, corresponde a las horas

de operación, cantidad de equipos y potencia de cada una de ellas. A continuación, la Tabla 3-23 indica los

niveles de actividad para maquinaria en las fases de construcción y operación.

**Tabla 3-23. Niveles de actividad de maquinaria en fases de construcción y operación**

|Fase|Equipo|Cantidad de<br>equipos|Horas de<br>operación<br>anuales|Potencia (kW)|
|---|---|---|---|---|
|Construcción|Grúa|1|768|30|
|Construcción|Toro/Manitou|2|1536|30|
|Construcción|Excavadora|1|384|70|
|Construcción|Retroexcavadora|2|1536|70|
|Construcción|Bulldozer|1|96|300|
|Construcción|Cargadora frontal|1|96|180|
|Construcción|Hincadora/Perforadora|1|384|40|
|Construcción|Motoniveladora|1|192|110|
|Construcción|Rodillo|1|192|20|
|Operación|Tractor|2|1152|14|

14

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

###### 3.4.2 Niveles de actividad de vehículos

El nivel de actividad para la estimación de emisiones por tránsito vehicular (por combustión del motor o

resuspensión de material particulado), corresponde a la distancia recorrida, velocidad de circulación y

peso promedio de los vehículos. Las categorías de los vehículos que conforman la flota de vehículos del

proyecto, es la siguiente:

Camiones Pesados Diesel Tipo 3: Corresponden a camiones pesados con peso bruto superior a 16

toneladas cuya fecha de inscripción en el Registro Nacional de Vehículos Motorizados sea posterior a

septiembre del año 2003. Estos buses deben cumplir con la normativa EPA 98 o Euro III.

Buses Particulares: Corresponden a buses destinados al transporte privado de pasajeros dentro de la

ciudad (buses de servicio urbano) que no caen dentro de las alternativas anteriores. Se trata de buses

institucionales o privados que no tienen recorrido definido ni son licitados por la autoridad.

Vehículos Comerciales Diesel Tipo 2: Corresponden a los vehículos livianos de pasajeros o carga liviana,

privados o comerciales y que funcionan con combustible diésel, principalmente del tipo jeep, camioneta

o furgón cuya fecha de inscripción en el registro Nacional de Vehículos Motorizados sea posterior a

septiembre del año 2003 cumpliendo con la normativa EPA 94 federal o la Euro III.

A continuación, en la Tabla 3-24, Tabla 3-25 y Tabla 3-26, se reportan los niveles de actividad y

características de los vehículos a utilizar en las fases de construcción, operación y cierre, respectivamente.

**Tabla 3-24. Vehículos utilizados en fase de construcción**

|Tipo de vehículo|Carga|Origen|Destino|Peso vehículo (t)|Col6|Viajes<br>mensuales<br>(ida)|Distancia (km) - Tipo de<br>carpeta|Col9|
|---|---|---|---|---|---|---|---|---|
|**Tipo de vehículo**|**Carga**|**Origen**|**Destino**|**Vacío**|**Cargado**|**Cargado**|**Pavimentado**|**No**<br>**pavimentado**|
|Camioneta 4x4 y<br>furgoneta|Personal|Los Ángeles|Faena|1,9|3,0|240|42,3|5,6|
|Bus|Personal|Los Ángeles|Faena|(*)|19,0|48|42,3|5,6|
|Camión tanque|Combustible|Los Ángeles|Faena|7,8|36,9|2|42,3|5,6|
|Camión aljibe<br>20.000L o similar|Agua|Caminos internos y acceso<br>por Ruta S/R|Caminos internos y acceso<br>por Ruta S/R|10,5|30,5|48|-|5,6|
|Camión aljibe<br>20.000L o similar|Agua potable|Los Ángeles|Faena|10,5|30,5|2|42,3|5,6|
|Camión<br>Hormigonero 6 m3|Hormigón|Planta de<br>hormigón<br>(Los Ángeles)|<br>Faena|11,6|32,2|8|45,3|5,6|
|Camión grúa|Carga en<br>General|Los Ángeles|Faena|7,3|27,0|8|42,3|5,6|
|Camión 20 t o<br>similar|Perfiles de<br>acero|Los Ángeles|Faena|10,3|32,0|6|42,3|5,6|
|Camión 30 t o<br>similar|Módulos<br>Fotovoltaicos|Talcahuano|Faena|9,7|40,0|12|143,2|5,6|

15

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

|Tipo de vehículo|Carga|Origen|Destino|Peso vehículo (t)|Col6|Viajes<br>mensuales<br>(ida)|Distancia (km) - Tipo de<br>carpeta|Col9|
|---|---|---|---|---|---|---|---|---|
|**Tipo de vehículo**|**Carga**|**Origen**|**Destino**|**Vacío**|**Cargado**|**Cargado**|**Pavimentado**|**No**<br>**pavimentado**|
|Camión 30 t o<br>similar|Seguidores<br>Solares|Talcahuano|Faena|9,7|40,0|12|143,2|5,6|
|Camión 30 t o<br>similar|Equipos SE<br>Salas<br>Eléctricas<br>Inversores<br>Cables<br>Cuadros CN1|Los Ángeles|Faena|9,7|40,0|2|42,3|5,6|
|Camión habilitado|Residuos<br>peligrosos|Faena|Hidronor<br>(Talcahuano)|5,6|17,1|1|137,6|5,6|
|Camión habilitado|Residuos no<br>peligrosos|Faena|Relleno<br>sanitario de<br>Los Ángeles|5,6|17,1|2|59,7|7,2|
|Camión tolva|Suelo de<br>excavación|Interior de la faena|Interior de la faena|9,3|33,5|32|-|2,6|
|Camión tolva|Áridos|Planta de<br>áridos|Faena|9,3|33,5|14|22,3|9,6|

(*) Se ha considerado que los buses nunca viajan vacíos.

**Tabla 3-25. Vehículos utilizados en fase de operación**

|Tipo de vehículo|Carga|Origen|Destino|Peso vehículo (t)|Col6|Viajes<br>anuales<br>(ida)|Distancia (km) - Tipo de<br>carpeta|Col9|
|---|---|---|---|---|---|---|---|---|
|**Tipo de vehículo**|**Carga**|**Origen**|**Destino**|**Vacío**|**Cargado**|**Cargado**|**Pavimento**|**No**<br>**pavimentado**|
|Camioneta 4x4 y<br>furgoneta|Personal|Los Ángeles|Planta|1,9|3,0|144|42,3|5,6|
|Camión|Equipos y<br>maquinaria|Los Ángeles|Planta|9,7|40,0|2|42,3|5,6|
|Camión aljibe<br>30.000L o similar|Agua<br>limpieza<br>paneles|Los Ángeles|Planta|14,0|44,0|4|42,3|5,6|
|Camión aljibe<br>20.000L o similar|Agua potable|Los Ángeles|Planta|10,5|30,5|4|42,3|5,6|
|Camión tanque|Combustible|Los Ángeles|Planta|7,8|36,9|2|42,3|5,6|
|Camión<br>Habilitado|Residuos|Planta|Relleno<br>sanitario<br>de Los<br>Ángeles|5,6|17,1|4|59,7|7,2|

16

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 3-26. Vehículos utilizados en fase de cierre**

|Tipo de vehículo|Carga|Origen|Destino|Peso vehículo (t)|Col6|Viajes<br>mensuales<br>(ida)|Distancia (km) - Tipo de<br>carpeta|Col9|
|---|---|---|---|---|---|---|---|---|
|**Tipo de vehículo**|**Carga**|**Origen**|**Destino**|**Vacío**|**Cargado**|**Cargado**|**Pavimento**|**No**<br>**pavimentado**|
|Camioneta 4x4|Personal|Los Ángeles|Planta|1,9|3,0|30|42,3|5,6|
|Bus|Personal|Los Ángeles|Planta|(*)|19,0|15|42,3|5,6|
|Camión|Equipos y<br>maquinaria|Planta|Los Ángeles|10,3|32,0|15|42,3|5,6|
|Camión<br>aljibe<br>20.000L o similar|Agua<br>industrial|Caminos internos y acceso<br>por Ruta S/R|Caminos internos y acceso<br>por Ruta S/R|10,5|30,5|30|-|5,6|
|Camión<br>Aljibe<br>20.000L o similar|Agua<br>industrial|Los Ángeles|Planta|10,5|30,5|1|42,3|5,6|
|Camión<br>aljibe<br>20.000L o similar|Agua potable|Los Ángeles|Planta|10,5|30,5|1|42,3|5,6|
|Camión tanque|Combustible|Los Ángeles|Planta|7,8|36,9|1|42,3|5,6|
|Camión 15 t|Módulos|Planta|Zona de<br>reciclaje<br>habilitada<br>(Hidronor)|6,8|24,1|12|137,6|5,6|
|Camión<br>habilitado|Residuos|Planta|Relleno<br>sanitario de<br>Los Ángeles|5,6|17,1|6|59,7|7,2|

(*) Se ha considerado que los buses nunca viajan vacíos.

Las rutas pavimentadas y no pavimentadas, asociadas a las distancias recorridas anteriormente

presentadas, corresponden a las siguientes:

**Tabla 3-27. Rutas utilizadas**

|Tramo|Col2|Ruta|Detalle ruta|Longitud<br>subtramo<br>(km)|Tipo de camino|Longitud<br>no pav<br>(km)|Longitud<br>pav<br>(km)|
|---|---|---|---|---|---|---|---|
|1|Proyecto - Los<br>Ángeles|Ruta S/R - Ruta 180 - Vicuña<br>Mackenna - San Martín|Ruta S/R|3,0|No pavimentado|3,0|42,3|
|1|Proyecto - Los<br>Ángeles|Ruta S/R - Ruta 180 - Vicuña<br>Mackenna - San Martín|Ruta 180|37,1|Pavimentado|Pavimentado|Pavimentado|
|1|Proyecto - Los<br>Ángeles|Ruta S/R - Ruta 180 - Vicuña<br>Mackenna - San Martín|Interior Los<br>Ángeles|5,2|Pavimentado|Pavimentado|Pavimentado|
|2|Proyecto -<br>Talcahuano|Ruta S/R - Ruta 180 - Ruta 156 -<br>Puente Chacabuco - Nueva<br>Costanera - Gran Bretaña -<br>Juan Antonio Ríos - La Marina|Ruta S/R|3,0|No pavimentado|3,0|143,2|
|2|Proyecto -<br>Talcahuano|Ruta S/R - Ruta 180 - Ruta 156 -<br>Puente Chacabuco - Nueva<br>Costanera - Gran Bretaña -<br>Juan Antonio Ríos - La Marina|Ruta 180|17,2|Pavimentado|Pavimentado|Pavimentado|
|2|Proyecto -<br>Talcahuano|Ruta S/R - Ruta 180 - Ruta 156 -<br>Puente Chacabuco - Nueva<br>Costanera - Gran Bretaña -<br>Juan Antonio Ríos - La Marina|Ruta 156|109,0|Pavimentado|Pavimentado|Pavimentado|
|2|Proyecto -<br>Talcahuano|Ruta S/R - Ruta 180 - Ruta 156 -<br>Puente Chacabuco - Nueva<br>Costanera - Gran Bretaña -<br>Juan Antonio Ríos - La Marina|Interior<br>Talcahuano|17,0|Pavimentado|Pavimentado|Pavimentado|
|3|Proyecto -<br>Planta de áridos|Ruta S/R - Ruta 180 - Ruta Q-<br>530|Ruta S/R|3,0|No pavimentado|7,0|22,3|
|3|Proyecto -<br>Planta de áridos|Ruta S/R - Ruta 180 - Ruta Q-<br>530|Ruta 180|22,3|Pavimentado|Pavimentado|Pavimentado|
|3|Proyecto -<br>Planta de áridos|Ruta S/R - Ruta 180 - Ruta Q-<br>530|Ruta Q-530|4,0|No pavimentado|No pavimentado|No pavimentado|

17

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

|Tramo|Col2|Ruta|Detalle ruta|Longitud<br>subtramo<br>(km)|Tipo de camino|Longitud<br>no pav<br>(km)|Longitud<br>pav<br>(km)|
|---|---|---|---|---|---|---|---|
|4|Proyecto -<br>Planta de<br>hormigón|Ruta S/R - Ruta 180 - Vicuña<br>Mackenna - Los Carrera -<br>Gabriela Mistral - Las Industrias|Ruta S/R|3,0|No pavimentado|3,0|45,3|
|4|Proyecto -<br>Planta de<br>hormigón|Ruta S/R - Ruta 180 - Vicuña<br>Mackenna - Los Carrera -<br>Gabriela Mistral - Las Industrias|Ruta 180|37,1|Pavimentado|Pavimentado|Pavimentado|
|4|Proyecto -<br>Planta de<br>hormigón|Ruta S/R - Ruta 180 - Vicuña<br>Mackenna - Los Carrera -<br>Gabriela Mistral - Las Industrias|Interior Los<br>Ángeles|8,2|Pavimentado|Pavimentado|Pavimentado|
|5|Proyecto -<br>Relleno sanitario<br>de Los Ángeles|Ruta S/R - Ruta 180 - Ruta 5 -<br>acceso a relleno sanitario|Ruta S/R|3,0|No pavimentado|4,6|59,7|
|5|Proyecto -<br>Relleno sanitario<br>de Los Ángeles|Ruta S/R - Ruta 180 - Ruta 5 -<br>acceso a relleno sanitario|Ruta 180|37,1|Pavimentado|Pavimentado|Pavimentado|
|5|Proyecto -<br>Relleno sanitario<br>de Los Ángeles|Ruta S/R - Ruta 180 - Ruta 5 -<br>acceso a relleno sanitario|Ruta 5|22,6|Pavimentado|Pavimentado|Pavimentado|
|5|Proyecto -<br>Relleno sanitario<br>de Los Ángeles|Ruta S/R - Ruta 180 - Ruta 5 -<br>acceso a relleno sanitario|Acceso a<br>relleno<br>sanitario|1,6|No pavimentado|No pavimentado|No pavimentado|
|6|Proyecto -<br>Hidronor|Ruta S/R - Ruta 180 - Ruta 156 -<br>Puente Chacabuco - Nueva<br>Costanera - Gran Bretaña - E,<br>Torriceli - S, Watt|Ruta S/R|3,0|No pavimentado|3,0|137,6|
|6|Proyecto -<br>Hidronor|Ruta S/R - Ruta 180 - Ruta 156 -<br>Puente Chacabuco - Nueva<br>Costanera - Gran Bretaña - E,<br>Torriceli - S, Watt|Ruta 180|17,2|Pavimentado|Pavimentado|Pavimentado|
|6|Proyecto -<br>Hidronor|Ruta S/R - Ruta 180 - Ruta 156 -<br>Puente Chacabuco - Nueva<br>Costanera - Gran Bretaña - E,<br>Torriceli - S, Watt|Ruta 156|109,0|Pavimentado|Pavimentado|Pavimentado|
|6|Proyecto -<br>Hidronor|Ruta S/R - Ruta 180 - Ruta 156 -<br>Puente Chacabuco - Nueva<br>Costanera - Gran Bretaña - E,<br>Torriceli - S, Watt|Interior<br>Talcahuano|11,4|Pavimentado|Pavimentado|Pavimentado|
|7|Interior Proyecto|Interior Proyecto|Caminos<br>internos|2,6|No pavimentado|2,6|0,0|

Considerando el peso de los vehículos indicados en la Tabla 3-24, Tabla 3-25 y Tabla 3-26, se estima un

peso promedio ponderado para la flota de vehículos que circulará por caminos no pavimentados, de 10,7

toneladas al interior de la faena y 9,9 toneladas en la Ruta S/R de acceso al Proyecto, durante la fase de

construcción; 4,3 toneladas en fase de operación, y de 14,5 toneladas al interior de la faena y en la Ruta

S/R de acceso al Proyecto para la fase de cierre. Para caminos pavimentados se consideró el peso promedio

por defecto indicado en la “Guía para la estimación de emisiones atmosféricas de proyectos inmobiliarios

para la Región Metropolitana del Ministerio del Medio Ambiente”, que es de 8 toneladas.

Se considera que los vehículos livianos circulan a una velocidad de 60 km/h en caminos pavimentados, y a

una velocidad de 40 km/h en caminos no pavimentados, mientras que buses y camiones lo hacen a 50

km/h en caminos pavimentados y 30 km/h en caminos no pavimentados.

###### 3.4.3 Generadores eléctricos

El nivel de actividad para generadores eléctricos corresponde al número de horas de operación y a la

potencia de estos. Durante las fases de construcción y cierre se utilizará un equipo de 50 KVA, mientras

que durante la fase de operación no se considera la utilización de generadores diésel de energía eléctrica.

A continuación, la Tabla 3-28 indica las características y horas de operación de los equipos generadores

para las fases de construcción y cierre del Proyecto.

**Tabla 3-28. Horas de operación de generadores eléctricos.**

|Fase|Cantidad de equipos|Potencia (kw)|Horas totales|
|---|---|---|---|
|Construcción|1|40|960|
|Cierre|1|40|576|

18

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

###### 3.4.4 Movimiento de material

La fase de construcción del Proyecto considera actividades de nivelación, excavación, relleno y

transferencias del material excavado. En las siguientes tablas se presentan los niveles de actividad

asociados a dichas actividades.

**Tabla 3-29. Nivel de actividad asociado a nivelación**

|Actividad|Nivel de Actividad|Col3|Col4|
|---|---|---|---|
|**Actividad**|**Ancho de la hoja de la**<br>**motoniveladora (m)**|**Superficie a nivelar (m2) **|**Recorrido de la motoniveladora**<br>**(km)**|
|Nivelación|3,66|227520|62,20|

**Tabla 3-30. Nivel de actividad asociado a excavaciones**

|Actividad|Obra|Nivel de Actividad|Col4|Col5|
|---|---|---|---|---|
|**Actividad**|**Obra**|**Cantidad de**<br>**material a**<br>**excavar (m3) **|**Rendimiento de**<br>**la pala (m3/h)**|**Horas de**<br>**excavación (h)**|
|Excavaciones|Terreno de Planta FV (Movimiento de<br>Tierras incluyendo terrazas de<br>subcampos y caminos interiores)|2000|30|**67**|
|Excavaciones|Otros (instalación de trackers, zanjas<br>BT/MT, vallado, edificaciones, casetas,<br>instalación de faena, acceso y<br>subestación)|500|30|**17**|

**Tabla 3-31. Nivel de actividad asociado a transferencia de material**

|Actividad|Sub-actividad|Nivel de Actividad|Col4|Col5|
|---|---|---|---|---|
|**Actividad**|**Sub-actividad**|**Material a**<br>**transferir (m3) **|**Densidad del**<br>**material (t/m3) **|**Material a**<br>**descargar (t)**|
|Transferencia de<br>material|Carga de material en camiones|2500|1,8|**4500**|
|Transferencia de<br>material|Descarga de material excavado como<br>relleno|2500|1,8|**4500**|
|Transferencia de<br>material|Descarga de áridos|1100|1,8|**1980**|

Se considera una humedad de 6,5% y un contenido de finos de 8,5%, para el material excavado durante la
fase de construcción, valores por defecto de acuerdo a la referencia [4] .

##### 3.5. Medidas de control y abatimiento de emisiones

Como medida de control, el Proyecto considera las siguientes actividades y /o acciones a implementar

durante las fases de construcción y cierre:

4 “Guía para la estimación de emisiones atmosféricas de proyectos inmobiliarios para la Región Metropolitana” del Ministerio del
Medio Ambiente, enero 2012

19

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

 - La actividad de habilitación de los terrenos se iniciará con la humectación del frente de trabajo,

definiendo un área de hasta 100 m [2] de superficie a humectar (siempre antes de comenzar con los

movimientos de tierra);

 - Los vehículos poseerán las revisiones técnicas al día. La mantención de la maquinaria se realizará

de acuerdo a las especificaciones del fabricante, en talleres mecánicos autorizados.

 - Los caminos internos del Parque Fotovoltaico (2,6 km), así como también el acceso al Proyecto por

la Ruta S/R (3,0 km) serán humectados dos veces durante el día, con la finalidad de controlar las

emisiones de material particulado, producidas por el tránsito de vehículos. La eficiencia de esta

medida fue estimada en un 75%, y se detalla a continuación.

La eficiencia indicada para la medida de humectación, durante las fases de construcción y cierre del

Proyecto, fue estimada con la metodología indicada en el “Emissions Inventory Guidance: Mineral

Handling and Processing Industries Handling” del Mojave Desert Air Quality Management District
(MDAQMD) [5], citado por la USEPA.

La eficiencia de la medida se estima mediante la siguiente ecuación.

En donde:

C _f_ : Eficiencia de control de la humectación, en porcentaje.

A: Evaporación anual, en pulgadas.

D: Tasa de tráfico horario promedio, en vehículos por hora.

T: Tiempo entre aplicación de agua, en horas.

I: Intensidad de aplicación de agua en galones por yarda cuadrada.

Considerando que para la fase de construcción se estima un flujo de 437 vehículos mensuales al interior

del proyecto y de 405 vehículos mensuales por la Ruta S/R, se evalúa flujos de 4,6 vehículos/hora y 4,2

vehículos/hora (ida y vuelta) respectivamente, considerando una jornada de 8 horas. La siguiente tabla

presenta el valor de las variables utilizadas para el cálculo.

**Tabla 3-32. Variables y valores utilizados para eficiencia en humectación.**

|Variable|Caminos internos|Acceso por Ruta S/R|
|---|---|---|
|A” (*)|44,33|44,33|
|D (veh/hora)|4,6|4,2|
|T (h)|4|4|
|I (gal/yd2)|0,039|0,036|
|I (L/m2)|0,18|0,16|

5 Disponible en: http://www.mdaqmd.ca.gov/modules/showdocument.aspx?documentid=401

20

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

|Variable|Caminos internos|Acceso por Ruta S/R|
|---|---|---|
|Cf|75%|75%|

(*) Fuente: Calculo y cartografía de la evapotranspiración potencial en chile - CIREN - El Vergel (Angol)

Con la información presentada, a continuación, la Tabla 3-33 indica el volumen de agua requerido

diariamente para obtener una eficiencia no inferior al 75% en la reducción de emisiones.

**Tabla 3-33. Cálculo de agua para humectación de caminos**

|Variable|Caminos internos|Acceso por Ruta S/R|
|---|---|---|
|Camino (m)|2600|3000|
|Ancho (m)|6|6|
|Superficie (m2)|15600|18000|
|Total (m3/pasada)|2,7|2,9|
|Total (m3/día)|5,5|5,9|

Por lo tanto, se considera la humectación con 0,039 (gal/yd2), lo que equivale a 0,18 (l/m2) cada 4 horas
en los caminos internos del PFV, y del acceso por la Ruta S/R con 0,16 (l/m [2] ) para obtener una eficiencia

no inferior al 75% en la reducción de emisiones de material particulado, debido al tránsito vehicular en

estos caminos. Esta aplicación implica humectar los caminos una vez al inicio de la jornada, y nuevamente
a mitad de la jornada, lo que requiere un consumo de agua de 11,3 m [3] /día.

##### 3.6. Emisiones

A continuación, se entregan las emisiones obtenidas para las actividades del proyecto, considerando las

metodologías y los niveles de actividad presentados precedentemente, para las fases de construcción,

operación y cierre del Proyecto.

###### 3.6.1 Emisiones en fase de construcción

A continuación, se reportan las emisiones estimadas para las fuentes identificadas en la fase de

construcción del Proyecto. Las emisiones que se presentan en las siguientes tablas, corresponden a las que

se generarían durante los 6 meses que duraría esta fase.

21

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 3-34. Emisiones por tránsito de vehículos en caminos pavimentados en fase de construcción**

|Actividad|Tramo|Sub-tramo|Factor de Emisión (g/km-veh)|Col5|Col6|Nivel de<br>Actividad<br>(km-<br>veh/mes)|Duración<br>de la<br>actividad<br>(mes)|Medida de<br>control<br>(%)|Emisión (t)|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Tramo**|**Sub-tramo**|**MP30**|**MP10**|**MP2,5**|**MP2,5**|**MP2,5**|**MP2,5**|**MP30**|**MP10**|**MP2,5**|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Los Ángeles|Ruta 180|2,0|0,4|0,1|22854|6|0|0,27|0,05|0,01|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Los Ángeles|interior Los Ángeles|2,0|0,4|0,1|3203|6|0|0,04|0,01|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Talcahuano|Ruta 180|2,0|0,4|0,1|826|6|0|0,01|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Talcahuano|Ruta 156|5,9|1,1|0,3|5232|6|0|0,19|0,04|0,01|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Talcahuano|Interior Talcahuano|1,1|0,2|0,0|816|6|0|0,01|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Planta de<br>áridos|Ruta 180|2,0|0,4|0,1|624|6|0|0,01|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Planta de<br>hormigón|Ruta 180|2,0|0,4|0,1|594|6|0|0,01|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Planta de<br>hormigón|interior Los Ángeles|2,0|0,4|0,1|131|6|0|0,00|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Relleno<br>sanitario|Ruta 180|2,0|0,4|0,1|148|6|0|0,00|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Relleno<br>sanitario|Ruta 5|1,1|0,2|0,0|90|6|0|0,00|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Hidronor|Ruta 180|2,0|0,4|0,1|34|6|0|0,00|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Hidronor|Ruta 156|5,9|1,1|0,3|218|6|0|0,01|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Hidronor|Interior Talcahuano|1,1|0,2|0,0|23|6|0|0,00|0,00|0,00|
|<br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br>|**0,54**|**0,10**|**0,02**|

22

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

Se considera un peso promedio de los vehículos (W) de 8 toneladas, y un contenido de silt (sL) de acuerdo

a la siguiente tabla.

**Tabla 3-35. Contenido de silt (sL) de caminos pavimentados del Proyecto**

|Calle/Ruta|Tipo de flujo|sL (g/m2)|
|---|---|---|
|Ruta 156|500-5000 veh/d|0,2|
|Ruta 180|5000-10000 veh/d|0,06|
|Interior Los Ángeles|Interior Los Ángeles|Interior Los Ángeles|
|Interior Talcahuano|>10000 veh/d|0,03|
|Ruta 5|Ruta 5|Ruta 5|

(*) Contenido de silt (sL) de acuerdo con “Informe Final Servicio de Recopilación y Sistematización de Factores de Emisión al Aire

para el Servicio de Evaluación Ambiental” (2015).

Se consideró además una cantidad de 70 días al año con al menos 0,254 mm de precipitación, de acuerdo
con datos del año 2019 de la Estación DGA Angol (La Mona) [6] .

**Tabla 3-36. Emisiones por tránsito de vehículos en caminos no pavimentados en fase de construcción**

|Actividad|Tramo|Factor de Emisión (g/km-<br>veh)|Col4|Col5|Nivel de<br>Actividad<br>(km-<br>veh/mes)|Duración<br>de la<br>actividad<br>(mes)|Medida<br>de<br>control<br>(%)|Emisión (t)|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Tramo**|**MPS**|**MP10**|**MP2,5**|**MP2,5**|**MP2,5**|**MP2,5**|**MPS**|**MP10**|**MP2,5**|
|Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados|Interior del<br>proyecto|1630|466|47|2272|6|75|5,55|1,59|0,16|
|Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados|Ruta S/R|1570|449|45|2430|6|75|5,72|1,64|0,16|
|Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados|Ruta Q-530<br>(acceso a planta<br>de áridos)|2226|636|64|112|6||1,50|0,43|0,04|
|Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados|Acceso a relleno<br>sanitario|1674|478|48|6|6||0,06|0,02|0,00|
|<br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br>|**12,84**|**3,67**|**0,37**|

Para la estimación de emisiones por tránsito vehicular en caminos no pavimentados, se consideraron los
pesos promedios de flotas que se muestran en la siguiente tabla, y un contenido de silt de 8,5% [7] .

**Tabla 3-37. Emisiones por tránsito de vehículos en caminos no pavimentados en fase de construcción**

|Peso flota|Col2|
|---|---|
|W: Peso de la flota interior Proyecto (t)|10,7|
|W: Peso de la flota Ruta S/R (acceso al Proyecto) (t)|9,9|
|W: Peso de la flota Ruta Q-530 (acceso a planta de áridos) (t)|21,4|
|W: Peso de la flota acceso a relleno sanitario (t)|11,4|

6 [Información disponible en http://explorador.cr2.cl/](http://explorador.cr2.cl/)
7 Valor para rutas de scraper en sitios de construcción en “Informe Final Servicio de Recopilación y Sistematización de Factores de
Emisión al Aire para el Servicio de Evaluación Ambiental” (2015), Tabla 4

23

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 3-38. Emisiones por nivelación en fase de construcción**

|Actividad|Factor de Emisión (kg/veh-km)|Col3|Col4|Nivel de<br>Actividad<br>(km)|Emisión (t)|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Actividad**|**MPS**|**MP10**|**MP2,5**|**MP2,5**|**MPS**|**MP10**|**MP2,5**|
|Nivelación|1,49|0,44|0,05|62,20|0,09|0,03|0,00|

**Tabla 3-39. Emisiones por excavaciones en fase de construcción**

|Actividad|Obra|Factor de Emisión (kg/h)|Col4|Col5|Nivel de<br>Actividad<br>(h)|Emisión (t)|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Obra**|**MPS**|**MP10**|**MP2,5**|**MP2,5**|**MPS**|**MP10**|**MP2,5**|
|Excavaciones|Terreno de Planta FV|2,98|0,61|0,31|67|0,198|0,041|0,021|
|Excavaciones|Otros|2,98|0,61|0,31|17|0,050|0,010|0,005|
|||||||**0,248**|**0,051**|**0,026**|

**Tabla 3-40. Emisiones por transferencia de material en fase de construcción**

|Actividad|Obra|Factor de Emisión (kg/t)|Col4|Col5|Nivel de<br>Actividad<br>(t)|Emisión (t)|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Obra**|**MPS**|**MP10**|**MP2,5**|**MP2,5**|**MPS**|**MP10**|**MP2,5**|
|Transferencia<br>de material<br>|Carga de material en<br>camiones|0,00054|0,00026|0,00004|4500|0,00245|0,00116|0,00018|
|Transferencia<br>de material<br>|Descarga de material<br>excavado como<br>relleno|0,00054|0,00026|0,00004|4500|0,00245|0,00116|0,00018|
|Transferencia<br>de material<br>|Descarga de áridos<br>|0,00054<br>|0,00026<br>|0,00004<br>|1980<br>|0,00108|0,00051|0,00008|
|<br> <br> <br> <br> <br>|<br> <br> <br> <br> <br>|<br> <br> <br> <br> <br>|<br> <br> <br> <br> <br>|<br> <br> <br> <br> <br>|<br> <br> <br> <br> <br>|**0,00597**|**0,00282**|**0,00043**|

Para transferencia de material se considera una velocidad promedio del viento de 4,3 (m/s), obtenida del
informe eólico a 5 m de altura en el sitio del proyecto [8] y una humedad del material de 6,5%, valor por

defecto de acuerdo a la referencia [9] .

8
Informe eólico a 5 m de altura en el sitio del proyecto disponible en
[http://walker.dgf.uchile.cl/Explorador/Eolico2/Reportes//minenergia_eolico_5e65eacf8a70a/informe_eolico.pdf](http://walker.dgf.uchile.cl/Explorador/Eolico2/Reportes/minenergia_eolico_5e65eacf8a70a/informe_eolico.pdf)
9 “Guía para la estimación de emisiones atmosféricas de proyectos inmobiliarios para la Región Metropolitana” del Ministerio del
Medio Ambiente, enero 2012

24

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 3-41. Emisiones por motores de maquinaria en fase de construcción**

|Equipo|Factor de emisión (g/hp-h)|Col3|Col4|Col5|Col6|Col7|Potencia<br>(hp)|Factor de<br>carga|Horas de<br>actividad<br>(h)|Cantidad<br>de<br>equipos|Emisión (t)|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Equipo**|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|**SO2 **|**SO2 **|**SO2 **|**SO2 **|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|
|Grúa|0,376|0,365|4,738|1,569|0,281|0,018|40|0,47|768|1|0,005|0,005|0,069|0,023|0,004|0,000|
|Toro/Manitou|0,478|0,464|4,504|2,418|0,296|0,018|40|0,63|1536|2|0,037|0,036|0,351|0,188|0,023|0,001|
|Excavadora|0,468|0,454|3,123|3,690|0,193|0,018|94|0,53|384|1|0,009|0,009|0,060|0,070|0,004|0,000|
|Retroexcavadora|0,801|0,777|3,638|6,326|0,423|0,021|94|0,48|1536|2|0,111|0,108|0,504|0,876|0,059|0,003|
|Bulldozer|0,246|0,238|2,605|1,336|0,176|0,016|402|0,80|96|1|0,008|0,007|0,080|0,041|0,005|0,001|
|Cargadora frontal|0,245|0,238|2,605|1,184|0,194|0,016|241|0,71|96|1|0,004|0,004|0,043|0,019|0,003|0,000|
|Hincadora/Perforadora|0,465|0,451|3,123|3,682|0,193|0,018|54|0,48|384|1|0,005|0,004|0,031|0,036|0,002|0,000|
|Motoniveladora|0,355|0,344|2,604|1,368|0,194|0,016|148|0,64|192|1|0,006|0,006|0,047|0,025|0,004|0,000|
|Rodillo|0,566|0,549|4,930|2,412|0,296|0,018|27|0,49|192|1|0,001|0,001|0,012|0,006|0,001|0,000|
|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|**0,187**|**0,181**|**1,197**|**1,285**|**0,104**|**0,006**|

**Tabla 3-42. Emisiones por operación de generadores en fase de construcción**

|Potencia<br>(kW)|Cantidad de<br>equipos|Horas de<br>operación (h)|Factor de<br>carga|Emisión (t)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Potencia**<br>**(kW)**|**Cantidad de**<br>**equipos**|**Horas de**<br>**operación (h)**|**Factor de**<br>**carga**|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|
|40|1|960|0,7|0,008|0,008|0,170|0,088|0,013|0,001|

25

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 3-43. Emisiones por combustión de motores de vehículos fase de construcción**

|Tipo de<br>Vehículo|Tipo de<br>superficie|Tramo|Factor de Emisión (g/km-veh)|Col5|Col6|Col7|Col8|Col9|Nivel de<br>Actividad<br>(km-<br>veh/mes)|meses/año|Emisión (t/año)|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo de**<br>**Vehículo**|**Tipo de**<br>**superficie**|**Tramo**|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|**SO2 **|**SO2 **|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|
|Vehículos<br>Comerciales<br>Diesel Tipo 2|Pavimentada|Proyecto - Los<br>Ángeles|0,042|0,040|0,826|0,261|0,067|0,002|20304|6|0,005|0,005|0,101|0,032|0,008|0,000|
|Vehículos<br>Comerciales<br>Diesel Tipo 2|Sin pavimentar|Ruta S/R<br>(acceso a<br>Proyecto)|0,047|0,045|0,956|0,322|0,081|0,002|1440|6|0,000|0,000|0,008|0,003|0,001|0,000|
|Vehículos<br>Comerciales<br>Diesel Tipo 2|Sin pavimentar|Interior<br>Proyecto|0,047|0,045|0,956|0,322|0,081|0,002|1248|6|0,000|0,000|0,007|0,002|0,001|0,000|
|Buses<br>Interurbanos<br>Diesel Tipo 3|Pavimentada|Proyecto - Los<br>Ángeles|0,166|0,161|6,852|1,742|0,413|0,007|4061|6|0,004|0,004|0,167|0,042|0,010|0,000|
|Buses<br>Interurbanos<br>Diesel Tipo 3|Sin pavimentar|Ruta S/R<br>(acceso a<br>Proyecto)|0,250|0,242|9,821|2,743|0,665|0,010|288|6|0,000|0,000|0,017|0,005|0,001|0,000|
|Buses<br>Interurbanos<br>Diesel Tipo 3|Sin pavimentar|Interior<br>Proyecto|0,250|0,242|9,821|2,743|0,665|0,010|250|6|0,000|0,000|0,015|0,004|0,001|0,000|
|Camiones<br>Pesados<br>Diesel Tipo 3|Pavimentada|Proyecto - Los<br>Ángeles|0,154|0,154|6,719|1,682|0,363|0,007|1692|6|0,002|0,002|0,068|0,017|0,004|0,000|
|Camiones<br>Pesados<br>Diesel Tipo 3|Pavimentada|Proyecto -<br>Talcahuano|0,154|0,154|6,719|1,682|0,363|0,007|6874|6|0,006|0,006|0,277|0,069|0,015|0,000|
|Camiones<br>Pesados<br>Diesel Tipo 3|Pavimentada|Proyecto -<br>Planta de<br>áridos|0,154|0,154|6,719|1,682|0,363|0,007|624|6|0,001|0,001|0,025|0,006|0,001|0,000|
|Camiones<br>Pesados<br>Diesel Tipo 3|Pavimentada|Proyecto -<br>Planta de<br>hormigón|0,154|0,154|6,719|1,682|0,363|0,007|725|6|0,001|0,001|0,029|0,007|0,002|0,000|
|Camiones<br>Pesados<br>Diesel Tipo 3|Pavimentada|Proyecto -<br>Relleno<br>sanitario|0,154|0,154|6,719|1,682|0,363|0,007|239|6|0,000|0,000|0,010|0,002|0,001|0,000|
|Camiones<br>Pesados<br>Diesel Tipo 3|Pavimentada|Proyecto -<br>Hidronor|0,154|0,154|6,719|1,682|0,363|0,007|275|6|0,000|0,000|0,011|0,003|0,001|0,000|
|Camiones<br>Pesados<br>Diesel Tipo 3|Sin pavimentar|Ruta S/R<br>(acceso a<br>Proyecto)|0,230|0,230|8,739|2,492|0,559|0,010|2430|6|0,003|0,003|0,127|0,036|0,008|0,000|

26

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

|Tipo de<br>Vehículo|Tipo de<br>superficie|Tramo|Factor de Emisión (g/km-veh)|Col5|Col6|Col7|Col8|Col9|Nivel de<br>Actividad<br>(km-<br>veh/mes)|meses/año|Emisión (t/año)|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo de**<br>**Vehículo**|**Tipo de**<br>**superficie**|**Tramo**|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|**SO2 **|**SO2 **|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|
|**Tipo de**<br>**Vehículo**|Sin pavimentar|Acceso a<br>planta de<br>áridos (Ruta<br>Q-530)|0,230|0,230|8,739|2,492|0,559|0,010|112|6|0,000|0,000|0,006|0,002|0,000|0,000|
|**Tipo de**<br>**Vehículo**|Sin pavimentar|Acceso a<br>relleno<br>sanitario|0,230|0,230|8,739|2,492|0,559|0,010|6|6|0,000|0,000|0,000|0,000|0,000|0,000|
|**Tipo de**<br>**Vehículo**|Sin pavimentar|Interior<br>Proyecto|0,230|0,230|8,739|2,492|0,559|0,010|2272|6|0,003|0,003|0,119|0,034|0,008|0,000|
|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|**0,027**|**0,026**|**0,988**|**0,266**|**0,061**|**0,001**|

27

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

###### 3.6.2 Emisiones en fase de operación

A continuación, se reportan las emisiones estimadas para las fuentes emisoras identificadas para la fase

de operación del Proyecto. Las emisiones reportadas corresponden a las generadas producto de un año

de operación del Proyecto.

**Tabla 3-44. Emisiones por tránsito de vehículos en caminos pavimentados en fase de operación**

|Actividad|Tramo|Sub-tramo|Factor de Emisión<br>(g/km-veh)|Col5|Col6|Nivel de<br>Actividad<br>(km-<br>veh/año)|Emisión (t/año)|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Tramo**|**Sub-tramo**|**MPS**|**MP10**|**MP2,5**|**MP2,5**|**MPS**|**MP10**|**MP2,5**|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados<br>|Proyecto<br>- Los<br>Ángeles|Ruta 180|2,0|0,4|0,1|11575|0,02|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados<br>|Proyecto<br>- Los<br>Ángeles|interior Los Ángeles|2,0|0,4|0,1|1622|0,00|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados<br>|Proyecto<br>- Relleno<br>sanitario<br>|Ruta 180|2,0|0,4|0,1|297|0,00|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados<br>|Proyecto<br>- Relleno<br>sanitario<br>|Ruta 5<br>|1,1<br>|0,2<br>|0,0<br>|181<br>|0,00|0,00|0,00|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**0,03**|**0,01**|**0,00**|

**Tabla 3-45. Emisiones por tránsito de vehículos en caminos no pavimentados en fase de operación**

|Actividad|Tramo|Factor de Emisión (g/km-veh)|Col4|Col5|Nivel de<br>Actividad<br>(km-<br>veh/año)|Medida<br>de<br>control<br>(%)|Emisión (t/año)|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Tramo**|**MPS**|**MP10**|**MP2,5**|**MP2,5**|**MP2,5**|**MPS**|**MP10**|**MP2,5**|
|Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados<br>|Interior del<br>proyecto|1084|310|31|832|0|0,90|0,26|0,03|
|Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados<br>|Ruta S/R|1084|310|31|960|0|1,04|0,30|0,03|
|Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados<br>|Acceso a<br>relleno<br>sanitario<br>|1674<br>|478<br>|48<br>|13<br>|0 <br>|0,02|0,01|0,00|
|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|**1,96**|**0,56**|**0,06**|

Para la estimación de emisiones por tránsito vehicular en caminos no pavimentados, se consideraron los
pesos promedios de flotas que se muestran en la siguiente tabla, y un contenido de silt de 8,5% [10] .

**Tabla 3-46. Emisiones por tránsito de vehículos en caminos no pavimentados en fase de operación**

|Peso flota|Col2|
|---|---|
|W: Peso de la flota interior Proyecto (t)|4,3|
|W: Peso de la flota Ruta S/R (acceso al Proyecto) (t)|4,3|
|W: Peso de la flota acceso a relleno sanitario (t)|11,4|

10 Valor para rutas de scraper en sitios de construcción en “Informe Final Servicio de Recopilación y Sistematización de Factores
de Emisión al Aire para el Servicio de Evaluación Ambiental” (2015), Tabla 4

28

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 3-47. Emisiones por combustión de motores de vehículos en fase de operación**

|Tipo de<br>Vehículo|Tipo de<br>superficie|Tramo|Factor de Emisión (g/km-veh)|Col5|Col6|Col7|Col8|Col9|Nivel de<br>Actividad<br>(km-<br>veh/año)|Emisión (t/año)|Col12|Col13|Col14|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo de**<br>**Vehículo**|**Tipo de**<br>**superficie**|**Tramo**|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2**|**SO2**|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2**|
|Vehículos<br>Comerciales<br>Diesel Tipo<br>2|Pavimentada|Proyecto -<br>Los Ángeles|0,042|0,040|0,826|0,261|0,067|0,002|12182|0,0005|0,0005|0,0101|0,0032|0,0008|0,0000|
|Vehículos<br>Comerciales<br>Diesel Tipo<br>2|Sin<br>pavimentar|Ruta S/R<br>(acceso a<br>Proyecto)|0,047|0,045|0,956|0,322|0,081|0,002|864|0,0000|0,0000|0,0008|0,0003|0,0001|0,0000|
|Vehículos<br>Comerciales<br>Diesel Tipo<br>2|Sin<br>pavimentar|Interior<br>Proyecto|0,047|0,045|0,956|0,322|0,081|0,002|749|0,0000|0,0000|0,0007|0,0002|0,0001|0,0000|
|Camiones<br>Pesados<br>Diesel Tipo<br>3|Pavimentada|Proyecto -<br>Los Ángeles|0,154|0,154|6,719|1,682|0,363|0,007|1015|0,0002|0,0002|0,0068|0,0017|0,0004|0,0000|
|Camiones<br>Pesados<br>Diesel Tipo<br>3|Pavimentada|Proyecto -<br>Relleno<br>sanitario|0,154|0,154|6,719|1,682|0,363|0,007|478|0,0001|0,0001|0,0032|0,0008|0,0002|0,0000|
|Camiones<br>Pesados<br>Diesel Tipo<br>3|Sin<br>pavimentar|Ruta S/R<br>(acceso a<br>Proyecto)|0,230|0,230|8,739|2,492|0,559|0,010|960|0,0002|0,0002|0,0084|0,0024|0,0005|0,0000|
|Camiones<br>Pesados<br>Diesel Tipo<br>3|Sin<br>pavimentar|Acceso a<br>relleno<br>sanitario|0,230|0,230|8,739|2,492|0,559|0,010|13|0,0000|0,0000|0,0001|0,0000|0,0000|0,0000|
|Camiones<br>Pesados<br>Diesel Tipo<br>3|Sin<br>pavimentar|Interior<br>Proyecto|0,230|0,230|8,739|2,492|0,559|0,010|832|0,0002|0,0002|0,0073|0,0021|0,0005|0,0000|
|<br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br>|**0,0012**|**0,0012**|**0,0374**|**0,0107**|**0,0025**|**0,0001**|

**Tabla 3-48. Emisiones por motores de maquinaria en fase de operación**

|Equipo|Factor de emisión (g/hp-h)|Col3|Col4|Col5|Col6|Col7|Potencia<br>(hp)|Factor de<br>carga|Horas de<br>actividad<br>(h/año)|Cantidad<br>de equipos|Emisión (t/año)|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Equipo**|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|**SO2 **|**SO2 **|**SO2 **|**SO2 **|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|
|Tractor|0,314|0,305|4,455|2,244|0,444|0,018|19|0,44|1152|2|0,024|0,023|0,350|0,109|0,026|0,002|

29

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

###### 3.6.3 Emisiones en fase de cierre

A continuación, se reportan las emisiones estimadas para las fuentes identificadas en la fase de cierre del

Proyecto. Las emisiones que se presentan en las siguientes tablas, corresponden a las que se generarían

durante los 3 meses que duraría esta fase.

**Tabla 3-49. Emisiones por tránsito de vehículos en caminos pavimentados en fase de cierre**

|Actividad|Tramo|Sub-tramo|Factor de Emisión<br>(g/km-veh)|Col5|Col6|Nivel de<br>Actividad<br>(km-<br>veh/mes)|Duración<br>de la<br>actividad<br>(mes)|Emisión (t)|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Tramo**|**Sub-tramo**|**MPS**|**MP10**|**MP2,5**|**MP2,5**|**MP2,5**|**MPS**|**MP10**|**MP2,5**|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Los Ángeles|Ruta 180|2,0|0,4|0,1|4675|3|0,03|0,01|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Los Ángeles|interior Los<br>Ángeles|2,0|0,4|0,1|655|3|0,00|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Relleno<br>sanitario|Ruta 180|2,0|0,4|0,1|445|3|0,00|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Relleno<br>sanitario|Ruta 5|1,1|0,2|0,0|271|3|0,00|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Hidronor|Ruta 180|2,0|0,4|0,1|413|3|0,00|0,00|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Hidronor|Ruta 156|5,9|1,1|0,3|2616|3|0,05|0,01|0,00|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|Proyecto -<br>Hidronor|Interior<br>Talcahuano|1,1|0,2|0,0|274|3|0,00|0,00|0,00|
|||||||||**0,09**|**0,02**|**0,00**|

**Tabla 3-50. Emisiones por tránsito de vehículos en caminos no pavimentados en fase de cierre**

|Actividad|Tramo|Factor de Emisión (g/km-<br>veh)|Col4|Col5|Nivel de<br>Actividad<br>(km-<br>veh/mes)|Duración<br>de la<br>actividad<br>(mes)|Medida<br>de<br>control<br>(%)|Emisión (t)|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Actividad**|**Tramo**|**MPS**|**MP10**|**MP2,5**|**MP2,5**|**MP2,5**|**MP2,5**|**MPS**|**MP10**|**MP2,5**|
|Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados<br>|Interior<br>del<br>proyecto|1868|534|53|577|3|75|0,81|0,23|0,02|
|Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados<br>|Ruta S/R|1868|534|53|666|3|75|0,93|0,27|0,03|
|Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados<br>|Acceso a<br>relleno<br>sanitario<br>|1674|478|48|19|3||0,10|0,03|0,00|
|<br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br>|**1,84**|**0,53**|**0,05**|

Para la estimación de emisiones por tránsito vehicular en caminos no pavimentados, se consideraron los
pesos promedios de flotas que se muestran en la siguiente tabla, y un contenido de silt de 8,5% [11] .

11 Valor para rutas de scraper en sitios de construcción en “Informe Final Servicio de Recopilación y Sistematización de Factores
de Emisión al Aire para el Servicio de Evaluación Ambiental” (2015), Tabla 4

30

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 3-51. Emisiones por tránsito de vehículos en caminos no pavimentados en fase de cierre**

|Peso flota|Col2|
|---|---|
|W: Peso de la flota interior Proyecto (t)|14,5|
|W: Peso de la flota Ruta S/R (acceso al Proyecto) (t)|8,9|
|W: Peso de la flota acceso a relleno sanitario (t)|11,4|

**Tabla 3-52. Emisiones por operación de generadores en fase de cierre**

|Potencia<br>(kW)|Cantidad<br>de<br>equipos|Horas de<br>operación<br>(h)|Factor de<br>carga|Emisión (t)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Potencia**<br>**(kW)**|**Cantidad**<br>**de**<br>**equipos**|**Horas de**<br>**operación**<br>**(h)**|**Factor de**<br>**carga**|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|
|40|1|576|0,7|0,004|0,004|0,102|0,052|0,008|0,000|

31

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 3-53. Emisiones por combustión de motores de vehículos en fase de cierre**

|Tipo de<br>Vehículo|Tipo de<br>superficie|Tramo|Factor de Emisión (g/km-veh)|Col5|Col6|Col7|Col8|Col9|Nivel de<br>Actividad<br>(km-<br>veh/mes)|meses/año|Emisión (t/año)|Col13|Col14|Col15|Col16|Col17|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Tipo de**<br>**Vehículo**|**Tipo de**<br>**superficie**|**Tramo**|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|**SO2 **|**SO2 **|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|
|Vehículos<br>Comerciales<br>Diesel Tipo 2|Pavimentada|Proyecto -<br>Los<br>Ángeles|0,042|0,040|0,826|0,261|0,067|0,002|2538|3|0,000|0,000|0,006|0,002|0,001|0,000|
|Vehículos<br>Comerciales<br>Diesel Tipo 2|Sin<br>pavimentar|Ruta S/R<br>(acceso a<br>Proyecto)|0,047|0,045|0,956|0,322|0,081|0,002|180|3|0,000|0,000|0,001|0,000|0,000|0,000|
|Vehículos<br>Comerciales<br>Diesel Tipo 2|Sin<br>pavimentar|Interior<br>Proyecto|0,047|0,045|0,956|0,322|0,081|0,002|156|3|0,000|0,000|0,000|0,000|0,000|0,000|
|Buses<br>Interurbanos<br>Diesel Tipo 3|Pavimentada|Proyecto -<br>Los<br>Ángeles|0,166|0,161|6,852|1,742|0,413|0,007|1269|3|0,001|0,001|0,026|0,007|0,002|0,000|
|Buses<br>Interurbanos<br>Diesel Tipo 3|Sin<br>pavimentar|Ruta S/R<br>(acceso a<br>Proyecto)|0,250|0,242|9,821|2,743|0,665|0,010|90|3|0,000|0,000|0,003|0,001|0,000|0,000|
|Buses<br>Interurbanos<br>Diesel Tipo 3|Sin<br>pavimentar|Interior<br>Proyecto|0,250|0,242|9,821|2,743|0,665|0,010|78|3|0,000|0,000|0,002|0,001|0,000|0,000|
|Camiones<br>Pesados<br>Diesel Tipo 3|Pavimentada|Proyecto -<br>Los<br>Ángeles|0,154|0,154|6,719|1,682|0,363|0,007|1523|3|0,001|0,001|0,031|0,008|0,002|0,000|
|Camiones<br>Pesados<br>Diesel Tipo 3|Pavimentada|Proyecto -<br>Relleno<br>sanitario|0,154|0,154|6,719|1,682|0,363|0,007|716|3|0,000|0,000|0,014|0,004|0,001|0,000|
|Camiones<br>Pesados<br>Diesel Tipo 3|Pavimentada|Proyecto -<br>Hidronor|0,154|0,154|6,719|1,682|0,363|0,007|3302|3|0,002|0,002|0,067|0,017|0,004|0,000|
|Camiones<br>Pesados<br>Diesel Tipo 3|Sin<br>pavimentar|Ruta S/R<br>(acceso a<br>Proyecto)|0,230|0,230|8,739|2,492|0,559|0,010|666|3|0,000|0,000|0,017|0,005|0,001|0,000|
|Camiones<br>Pesados<br>Diesel Tipo 3|Sin<br>pavimentar|Acceso a<br>relleno<br>sanitario|0,230|0,230|8,739|2,492|0,559|0,010|19|3|0,000|0,000|0,001|0,000|0,000|0,000|
|Camiones<br>Pesados<br>Diesel Tipo 3|Sin<br>pavimentar|Interior<br>Proyecto|0,230|0,230|8,739|2,492|0,559|0,010|577|3|0,000|0,000|0,015|0,004|0,001|0,000|
|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>|**0,005**|**0,005**|**0,183**|**0,048**|**0,011**|**0,000**|

32

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

###### 3.6.4 Resumen de emisiones

A continuación, se presenta el resumen de las emisiones de cada fase del Proyecto.

**Tabla 3-54. Emisiones totales en fase de construcción**

|11|Emisión (t)|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**11**|**MPS**|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|
|Nivelación|0,09|0,03|0,00|-|-|-|-|
|Excavaciones|0,25|0,05|0,03|-|-|-|-|
|Transferencia de<br>material|0,01|0,00|0,00|-|-|-|-|
|Tránsito de<br>vehículos pesados<br>por caminos no<br>pavimentados|12,84|3,67|0,37|-|-|-|-|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|0,54|0,10|0,02|-|-|-|-|
|Combustión de<br>motores de<br>vehículos|0,03|0,03|0,03|0,99|0,27|0,06|0,00|
|Maquinaria|0,19|0,19|0,18|1,20|1,29|0,10|0,01|
|Generadores|0,01|0,01|0,01|0,17|0,09|0,01|0,00|
|**TOTAL**|**13,94**|**4,07**|**0,64**|**2,35**|**1,64**|**0,18**|**0,01**|

**Tabla 3-55. Emisiones totales en fase de operación**

|Actividad|Emisión (t)|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Actividad**|**MPS**|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|
|Tránsito de<br>vehículos pesados<br>por caminos no<br>pavimentados|1,96|0,56|0,06|-|-|-|-|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|0,03|0,01|0,00|-|-|-|-|
|Combustión de<br>motores de<br>vehículos|0,00|0,00|0,00|0,04|0,01|0,00|0,00|
|Maquinaria|0,02|0,02|0,02|0,35|0,11|0,03|0,00|
|**TOTAL**|**2,02**|**0,59**|**0,08**|**0,39**|**0,12**|**0,03**|**0,00**|

33

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 3-56. Emisiones totales en fase de cierre**

|Actividad|Emisión (t)|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Actividad**|**MPS**|**MP10**|**MP2,5**|**NOx**|**CO**|**HC**|**SO2 **|
|Tránsito de<br>vehículos pesados<br>por caminos no<br>pavimentados|1,84|0,53|0,05|-|-|-|-|
|Tránsito de<br>vehículos por<br>caminos<br>pavimentados|0,09|0,02|0,00|-|-|-|-|
|Combustión de<br>motores de<br>vehículos|0,00|0,00|0,00|0,18|0,05|0,01|0,00|
|Generadores|0,00|0,00|0,00|0,10|0,05|0,01|0,00|
|**TOTAL**|**1,93**|**0,55**|**0,07**|**0,28**|**0,10**|**0,02**|**0,00**|

Se observa que la fase en donde se producirán las mayores emisiones corresponde a la fase de

construcción del Proyecto, en donde la actividad de tránsito vehicular por caminos no pavimentados,

genera los aportes más importantes en emisiones de material particulado. Las emisiones de gases son

aportadas principalmente por la combustión de los motores de maquinaria.

34

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

##### 4. MODELO DE CALIDAD DEL AIRE 4.1. Justificación del modelo de calidad del aire

Según lo establecido por la “Guía para el uso de Modelos de Calidad del Aire en el SEIA”, la selección del

modelo de Calidad del Aire utilizado en el presente estudio se realizó a partir de determinar la necesidad

de usar un modelo refinado mediante la técnica de “screening”. Este tipo de modelos sólo se utiliza para

decidir si se debe hacer una estimación de impactos a través de modelación. Por lo anterior, el modelo

SCREEN3 fue usado para determinar la necesidad de un modelo de mayor precisión.

##### 4.2. Descripción del modelo de calidad del aire

###### 4.2.1 Modelo SCREEN3

La evaluación del aporte a las concentraciones de contaminantes se realizó utilizando la metodología

screening recomendada por la US EPA en su documento Apéndice W parte 51-40 CFR Directrices para
Modelos de Calidad del Aire (Guideline on Air Quality Models) [12] .

En dicho documento se distinguen dos niveles de sofisticación en modelos de dispersión, el primer nivel

consiste de una técnica simple de estimación, que generalmente considera el peor caso de condiciones

meteorológicas, de modo de proveer estimaciones conservadoras sobre el impacto en la calidad del aire

de una fuente específica o una categoría de fuentes. El segundo nivel corresponde a un análisis más

refinado, que se debe llevar a cabo cuando las técnicas de screening indican que la concentración

contribuida por la fuente excede o cumple de manera ajustada las normas de calidad del aire.

Para la modelacion screening se utilizó SCREEN3 de la EPA, que es un modelo de dispersión gaussiano y

que realiza cálculos de corto plazo (horarios), incluyendo la estimación de las concentraciones máximas a

nivel del suelo, a distintas distancias viento abajo de la fuente. Es capaz de examinar un conjunto de clases

de estabilidad atmosférica y de velocidades de viento, con el objetivo de identificar las condiciones

meteorológicas más desfavorables para la dispersión de los contaminantes, es decir, identifica la

combinación de velocidad del viento y estabilidad atmosférica que resulta en el máximo nivel de

concentración del contaminante.

Dependiendo del tipo de fuente considerada (puntual o de área), el modelo usa distintos datos de entrada.

Los datos de entrada corresponden a las características de la fuente y de las emisiones (tasa de emisión,

dimensiones de la fuente, entre otros), entregando como resultado, un listado con las concentraciones a

nivel del suelo a diferentes distancias viento abajo de la fuente emisora.

12 http://www.epa.gov/scram001/guidance/guide/appw_05.pdf

35

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

Las concentraciones estimadas por el modelo SCREEN3 representan promedios horarios, por lo tanto,

cuando se requieren resultados para diferentes periodos, es necesario aplicar un factor de corrección. Los
factores de correccion según la EPA [13] son:

**Tabla 4-1. Factor de corrección para concentraciones de SCREEN3**

|Periodo|Factor de Corrección|
|---|---|
|24 horas|0,4|
|Anual|0,08|

###### 4.2.2 Fuentes emisoras y receptores asociados

Se realizaron modelaciones SCREEN de las emisiones de MP10 y MP2,5 generadas durante el primer año

del Proyecto, esto es, la fase de construcción, de 6 meses de duración, y los primeros 6 meses de la fase

de operación.

Se han considerado dos fuentes emisoras. La primera se trata de un área de 22,8 hectáreas

correspondiente al Parque Fotovoltaico y sus caminos internos. La segunda fuente emisora corresponde a

un tramo de 1300 m de longitud de la Ruta S/R por donde se accede al Proyecto. El detalle de las fuentes

emisoras ingresadas al modelo SCREEN3 se presentan a continuación.

**Tabla 4-2. Características y emisiones de la fuente emisora Parque Fotovoltaico y caminos internos**

|Características de la fuente|Col2|Col3|
|---|---|---|
|Ancho|340|m|
|Largo|670|m|
|Superficie|227800|m2|
|**Fase de construcción**|**Fase de construcción**|**Fase de construcción**|
|Duración fase|6|meses|
|Emisión MP10|1,87|t|
|Emisión MP2,5|0,38|t|
|**Fase de operación**|**Fase de operación**|**Fase de operación**|
|Duración fase en Año 1|6|meses|
|Emisión MP10|0,28|t|
|Emisión MP2,5|0,06|t|
|**Total Año 1**|**Total Año 1**|**Total Año 1**|
|Duración Año 1|12|meses/año|
|Duración Año 1|24|d/mes|
|Duración Año 1|8|h/d|
|Duración Año 1|2304|h/año|
|Emisión MP10|2,1|t/año|
|Emisión MP10|0,26|g/s|
|Emisión MP10|**1,14E-06**|g/s/m2|

13 Recommended Factors to Convert Maximum 1-hour Avg. Concentrations to Other Averaging Periods (U.S. EPA, 2011, 1995a;
ARB, 1994).

36

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

|Emisión MP2,5|0,4|t/año|
|---|---|---|
|Emisión MP2,5|0,05|g/s|
|Emisión MP2,5|**2,32E-07**|g/s/m2|

**Tabla 4-3. Características y emisiones de la fuente emisora Ruta S/R**

|Características de la fuente|Col2|Col3|
|---|---|---|
|Ancho|130|m|
|Largo|1300|m|
|Superficie|169000|m2|

|Duración fase|6|meses|
|---|---|---|
|Emisión MP10 en long total|1,64|t|
|Emisión MP2,5 en long total|0,17|t|
|Longitud total|3000|m|
|Emisión MP10 en tramo|0,71|t|
|Emisión MP2,5 en tramo|0,07|t|

|Duración fase en Año 1|6|meses|
|---|---|---|
|Emisión MP10 en long total|0,30|t|
|Emisión MP2,5 en long total|0,04|t|
|Longitud total|3000|m|
|Emisión MP10 en tramo|0,13|t|
|Emisión MP2,5 en tramo|0,02|t|
|**Total Año 1**|**Total Año 1**|**Total Año 1**|
|Duración Año 1|12|meses/año|
|Duración Año 1|24|d/mes|
|Duración Año 1|8|h/d|
|Duración Año 1|2304|h/año|
|Emisión MP10|0,84|t/año|
|Emisión MP10|0,10|g/s|
|Emisión MP10|**5,99E-07**|g/s/m2|
|Emisión MP2,5|0,09|t/año|
|Emisión MP2,5|0,01|g/s|
|Emisión MP2,5|**6,39E-08**|g/s/m2|

Se han identificado los receptores descritos en la Tabla 4-4, en las cercanías del Parque Fotovoltaico.

37

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

**Tabla 4-4. Receptores en área de influencia de la Planta Fotovoltaica**

|Punto|Descripción|Coordenadas UTM|Col4|
|---|---|---|---|
|**Punto**|**Descripción**|**Datum WGS 84 Huso 19H**|**Datum WGS 84 Huso 19H**|
|**Punto**|**Descripción**|**Este**|**Norte**|
|1|Vivienda de 2 pisos ubicada a un costado de Ruta 172,<br>parcela 18. Sector Parronal.|714.075|5.824.604|
|2|Vivienda de 1 piso ubicada a un costado de Ruta 172,<br>parcela 17, lote 3. Sector Parronal.|713.861|5.824.572|
|3|Vivienda de 1 piso ubicada a un costado de Ruta 172.<br>Sector Parronal.|713.675|5.824.556|
|4|Vivienda de 1 piso ubicada a un costado de Ruta 172,<br>parcela 17, lote 1. Sector Parronal.|713.668|5.824.628|
|5|Vivienda de 1 piso ubicada a un costado de Ruta 172.<br>Sector Parronal.|713.391|5.823.995|
|6|Vivienda de 1 piso ubicada a un costado de Ruta 172.<br>Sector Parronal.|713.338|5.824.262|

(*) Identificación de receptores de acuerdo a la modelación de ruido.

**Figura 4-1. Ubicación de receptores en área de influencia del Parque Fotovoltaico**

Fuente: GAC

38

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

Finalmente, considerando las velocidades del viento de 4,3 m/s en promedio y que las obras se

desarrollarán durante el día, se define la clase de estabilidad Clase B - inestable de acuerdo con lo

presentado en la Tabla 4-5, a continuación.

**Tabla 4-5. Clases de estabilidad**

Fuente: “Screening Procedures for Estimating the Air Quality Impact of Stationary Sources Revised”, USEPA (1992). Table 3-2. Key

<!-- INICIO TABLA 3-2. -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- #### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16 Adenda DIA Parque Fotovoltaico Parronal -->

**Tabla 3-2.: Actividades generadoras de emisiones por fase del Proyecto****

| Fase del<br>Proyecto | Actividad Generadora de Emisiones | Contaminante |
| --- | --- | --- |
| Construcción | Nivelación de superficies | MP10, MP2,5 y MPS |
| Construcción | Excavaciones | Excavaciones |
| Construcción | Transferencias de material excavado | Transferencias de material excavado |
| Construcción | Tránsito de vehículos por caminos pavimentados | Tránsito de vehículos por caminos pavimentados |
| Construcción | Tránsito de vehículos por caminos no pavimentados | Tránsito de vehículos por caminos no pavimentados |
| Construcción | Motores de maquinaria | MP10, MP2,5, MPS,<br>NOx, CO, SO2 y COV |
| Construcción | Motores de vehículos de transporte | Motores de vehículos de transporte |
| Construcción | Equipo generador de electricidad | Equipo generador de electricidad |
| Operación | Tránsito de vehículos por caminos pavimentados | MP10, MP2,5 y MPS |
| Operación | Tránsito de vehículos por caminos no pavimentados | Tránsito de vehículos por caminos no pavimentados |
| Operación | Motores de vehículos de transporte | MP10, MP2,5, MPS,<br>NOx, CO, SO2 y COV |
| Operación | Motores de maquinaria | Motores de maquinaria |
| Cierre | Tránsito de vehículos por caminos pavimentados | MP10, MP2,5 y MPS |
| Cierre | Tránsito de vehículos por caminos no pavimentados | Tránsito de vehículos por caminos no pavimentados |
| Cierre | Motores de vehículos de transporte | MP10, MP2,5, MPS,<br>NOx, CO, SO2 y COV |
| Cierre | Equipos generadores de electricidad | Equipos generadores de electricidad |

<!-- Estadísticas: 16 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: GAC ##### 3.2. Metodología de estimación de emisiones -->
<!-- FIN TABLA 3-2. -->


to Stability Categories

##### 4.3. Resultados de modelación

A continuación, se presentan los resultados de las modelaciones con SCREEN3 de las emisiones de MP10

generadas por el Proyecto durante el primer año del Proyecto. Estos resultados provienen originalmente

en resolución temporal horaria y son corregidos según los factores de la Tabla 4-1.

**Tabla 4-6. Resultados de modelación de MP10**

|Receptor|Aporte del Proyecto MP10 (μg/m3)|Col3|Aporte del Proyecto MP2,5 (μg/m3)|Col5|
|---|---|---|---|---|
|**Receptor**|**Max 24h**|**Anual**|**Max 24h**|**Anual**|
|1|1,8|0,4|0,4|0,1|
|2|2,0|0,4|0,4|0,1|
|3|1,4|0,3|0,3|0,1|
|4|1,2|0,2|0,2|0,0|
|5|1,1|0,2|0,2|0,0|
|6|1,0|0,2|0,2|0,0|
|**Norma primaria**|**150**|**50**|**50**|**20**|

39

#### Sol del Sur 8 SpA Actualización de estimación de emisiones atmosféricas Anexo 16

Adenda DIA Parque Fotovoltaico Parronal

De acuerdo a los resultados de la modelación con SCREEN3, los aportes del Proyecto en términos de

concentraciones de MP10 son menores al 1,3% de la norma primaria de MP10, mientras que las

concentraciones de MP2,5 no superan el 0,8% de la norma respectiva.

##### 5. CONCLUSIONES

 - Las mayores emisiones serán producidas durante la fase de construcción del Proyecto, que tendrá

una duración de 6 meses.

 - En la fase de construcción del Proyecto, las emisiones de material particulado son generadas

principalmente por la actividad de tránsito vehicular por caminos no pavimentados, alcanzando

un total de 4,07 toneladas de MP10 y 0,64 toneladas de MP2,5.

 - En la fase de construcción del Proyecto, las emisiones de gases son generadas principalmente por

la combustión de motores de maquinaria, estimándose totales de 0,18 toneladas de HC, 2,35

toneladas de NO x, 1,64 toneladas de CO y 0,01 toneladas de SO 2 .

 - En la fase de operación del Proyecto, se generarán emisiones muy menores debido al transporte

de personal, insumos y residuos y a la operación de tractores de baja potencia para actividades de

mantención.

 - En la fase de cierre del Proyecto, se generarán emisiones menores debido al transporte de

personal, insumos, módulos y residuos, además del funcionamiento de los equipos generadores.

 - Los aportes del Proyecto en términos de concentraciones de MP10 y MP2,5, obtenidos a través

de la modelación con SCREEN3, son menores al 1,3% de las normas primarias respectivas.

 - Dado que los aportes del Proyecto están muy por debajo de los límites establecidos en las normas

de calidad del aire, se concluye que no se requiere un modelo más refinado para la determinación

de impactos.

40

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3-1.: Cronograma de actividades fase de construcción.****

| Actividades | Mes 1 | Mes 2 | Mes 3 | Mes 4 | Mes 5 | Mes 6 |
| --- | --- | --- | --- | --- | --- | --- |
| Cercado del parque solar |  |  |  |  |  |  |
| Habilitación faena para obras temporales y permanentes |  |  |  |  |  |  |
| Habilitación de terrenos y de caminos interiores |  |  |  |  |  |  |
| Hincado de estructuras |  |  |  |  |  |  |
| Montaje de paneles |  |  |  |  |  |  |
| Conexiones eléctricas |  |  |  |  |  |  |
| Obras de drenaje de aguas lluvias |  |  |  |  |  |  |
| Pruebas eléctricas y puesta en marcha |  |  |  |  |  |  |
| Desmantelamiento de obras temporales |  |  |  |  |  |  |
| Energización |  |  |  |  |  |  |
| Interconexión |  |  |  |  |  |  |

**Tabla 3-3.: Factor de emisión para nivelación****

| Factor de Emisión (fe) | fe = k*0,0056*(S)^2,0 [Para MP10]<br>fe = k*0,0034*(S)^2,5 [Para MPS y MP2,5] |
| --- | --- |
| Unidades | kg/veh-km |
| Parámetros | k: factor según tamaño de partícula<br>MP2,5 = 0,0,031<br>M910 = 0,60<br>MPS = 1<br>S: Velocidad del vehículo nivelador (km/h) [11,4 nivel de referencia] |
| Fuente | Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition: Chapter 13,<br>Section 11.9“Western Surface Coal Mining, 1998” (Grading) |
| Descripción | Corresponde al factor de emisión de nivelación de terrenos (grading). La unidad<br>de este factor corresponde a kilógramos emitidos por kilómetro recorrido por<br>el vehículo nivelador en el proceso. |
| Nivel de actividad | El nivel de actividad se determina según la distancia que recorre el vehículo |

**Tabla 3-4.: Factor de emisión para excavaciones****

| Factor de Emisión (fe) | fe = 0,45*k*(s^1,5/M^1,4) [Para PM10]<br>fe = 2,6*k*(s^1,2/M^1,3) [Para MPS y MP2,5] |
| --- | --- |
| Unidades | kg/h |
| Parámetros | k: factor según tamaño de partícula<br>MP2,5 = 0,105<br>MP10 = 0,75<br>MPS = 1<br>s: % de finos del suelo [8,5 valor por defecto]<br>M: % humedad del material [6,5 valor por defecto] |
| Fuente | Compilation of Air Pollutant Emission Factors, AP 42, 5th Edition: Chapter 11,<br>Section 11.9 “Western Surface Coal Mining, 1998”, Table 11.9-2. |
| Descripción | Corresponde al factor de emisión de despeje de material (bulldozing/overburden)<br>escalado por 0,75 para ser aplicado a MP10. La unidad de este factor<br>corresponde a kilógramos emitidos por hora excavada |
| Nota | El nivel de actividad se determina a través del rendimiento de la maquinaria y el<br>volumen a excavar. Por defecto se considerará para una retroexcavadora con<br>capacidad de palada de 1 m3 un rendimiento igual a 30 m3/h. |

**Tabla 3-6.: Factores de emisión por resuspensión de MP por circulación de vehículos en caminos pavimentados****

| Factor de Emisión (fe) | fe = k*(sL)^0,91*W^1,02*(1-P/4N) |
| --- | --- |
| Unidades | g/km |
| Parámetros | k: factor según tamaño de partícula<br>MP2,5 = 0,15 |

**Tabla 3-7.: Factor de emisión por resuspensión de MP por circulación de vehículos pesados en caminos no****

| Factor de Emisión (fe) | fe = 281,9*k*(s/12)^0,9*(W/2,7)^0,45*(1-P/365) [Para MP10 y MP2,5]<br>fe = 281,9*k*(s/12)^0,7*(W/2,7)^0,45*(1-P/365) [Para MPS] |
| --- | --- |
| Unidades | g/km |
| Parámetros | k: factor según tamaño de partícula<br>MP2,5 = 0,15<br>MP10 = 1,5<br>MPS = 4,9<br>s: % de finos del suelo [8,5 valor por defecto]<br>W: Peso promedio de la flota que circula por las vías (t)<br>P: número de días en un año con al menos 0,254 mm de precipitación |
| Fuente | Compilation of Air Pollutant Emission Factors, AP 42: Chapter 13, Section 13.2.2<br>“Unpaved Roads” e Informe Final Servicio de Recopilación y Sistematización de<br>Factores de Emisión al Aire para el Servicio de Evaluación Ambiental |
| Descripción | Corresponde al factor de emisión de tránsito por caminos no pavimentados<br>determinado para sitios industriales. La unidad de este factor de emisión es<br>gramos de MP emitidos por kilómetro recorrido. |
| Nota | Dadas las características de la flota utilizada en la determinación de este factor<br>de emisión, su aplicación se reconoce válida para una flota de vehículos<br>pesados, es decir, cuyo peso promedio exceda las 2,7 toneladas métricas. |

**Tabla 3-8.: Factores de emisión de gases y MP de maquinarias****

| Factor de Emisión (fe) | E = (FP × t × C × P) |
| --- | --- |
| Unidades | g/día |
| Parámetros | FP: factor según potencia<br>t: tiempo de operación diaria (h)<br>C: Porcentaje de carga<br>P: Potencia Nominal (kw) |
| Fuente | Guía para la Estimación de Emisiones Atmosféricas de Proyectos Inmobiliarios para<br>la Región Metropolitana, Tabla 4.9 |
| Descripción | Corresponde al factor de emisión de combustión de los motores de la maquinaria<br>fuera de ruta. |

**Tabla 3-9.: Factores de emisión en estado estacionario de MP10 y gases para combustión de maquinaria****

| Fase | Equipo | Potencia<br>(kW) | Potencia<br>(hp) | FE en caliente (g/hp-h) | Col6 | Col7 | Col8 | Estándar<br>de<br>emisión |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **Equipo** | **Potencia**<br>**(kW)** | **Potencia**<br>**(hp)** | **HC** | **CO** | **NOx** | **PM** | **PM** |
| Construcción | Grúa | 30 | 40 | 0,2789 | 1,5323 | 4,7279 | 0,3389 | Tier 2 |
| Construcción | Toro/Manitou | 30 | 40 | 0,2789 | 1,5323 | 4,7279 | 0,3389 | Tier 2 |
| Construcción | Excavadora | 70 | 94 | 0,1836 | 2,3655 | 3,0 | 0,30 | Tier 3 |
| Construcción | Retroexcavadora | 70 | 94 | 0,1836 | 2,3655 | 3,0 | 0,30 | Tier 3 |
| Construcción | Bulldozer | 300 | 402 | 0,1669 | 0,8425 | 2,5 | 0,15 | Tier 3 |
| Construcción | Cargadora frontal | 180 | 241 | 0,1836 | 0,7475 | 2,5 | 0,15 | Tier 3 |
| Construcción | Hincadora/Perforadora | 40 | 54 | 0,1836 | 2,3655 | 3,0 | 0,30 | Tier 3 |
| Construcción | Motoniveladora | 110 | 148 | 0,1836 | 0,8667 | 2,5 | 0,22 | Tier 3 |
| Construcción | Rodillo | 20 | 27 | 0,2789 | 1,5323 | 4,7279 | 0,3389 | Tier 2 |
| Operación | Tractor | 14 | 19 | 0,4380 | 2,1610 | 4,4399 | 0,2665 | Tier 2 |

**Tabla 3-10.: Factores de ajuste transiente y consumo de combustible de maquinarias****

| Fase | Equipo | Potencia<br>(hp) | Factor de ajuste transiente | Col5 | Col6 | Col7 | BSFC ss<br>(lb/hp-<br>hr) | BSFC<br>TAF |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **Equipo** | **Potencia**<br>**(hp)** | **HC** | **CO** | **NOx** | **PM** | **PM** | **PM** |
| Construcción | Grúa | 40 | 1,00 | 1,00 | 1,00 | 1,00 | 0,408 | 1,00 |
| Construcción | Toro/Manitou | 40 | 1,05 | 1,53 | 0,95 | 1,23 | 0,408 | 1,01 |
| Construcción | Excavadora | 94 | 1,05 | 1,53 | 1,04 | 1,47 | 0,408 | 1,01 |
| Construcción | Retroexcavadora | 94 | 2,29 | 2,57 | 1,21 | 2,37 | 0,408 | 1,18 |
| Construcción | Bulldozer | 402 | 1,05 | 1,53 | 1,04 | 1,47 | 0,367 | 1,01 |
| Construcción | Cargadora frontal | 241 | 1,05 | 1,53 | 1,04 | 1,47 | 0,367 | 1,01 |
| Construcción | Hincadora/Perforadora | 54 | 1,05 | 1,53 | 1,04 | 1,47 | 0,408 | 1,01 |
| Construcción | Motoniveladora | 148 | 1,05 | 1,53 | 1,04 | 1,47 | 0,367 | 1,01 |
| Construcción | Rodillo | 27 | 1,05 | 1,53 | 1,04 | 1,47 | 0,408 | 1,01 |
| Operación | Tractor | 19 | 1,00 | 1,00 | 1,00 | 1,00 | 0,408 | 1,00 |

**Tabla 3-11.: Factor de carga, vida media, horas de funcionamiento, edad promedio y factor de edad para cada****

| Fase | Equipo | Potencia<br>(hp) | Factor de<br>Carga | Vida<br>Media<br>(horas) | Actividad<br>(horas/año) | Edad<br>promedio<br>(años | Factor<br>de edad |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Construcción | Grúa | 40 | 0,47 | 2500 | 415 | 3 | 0,234 |
| Construcción | Toro/Manitou | 40 | 0,63 | 2500 | 413 | 3 | 0,312 |
| Construcción | Excavadora | 94 | 0,53 | 4667 | 378 | 3 | 0,129 |

**Tabla 3-12.: Valor del factor A necesario para determinar el factor de deterioro por tipo de contaminante****

| Factor de deterioro relativo (A) | Col2 | Col3 | Col4 | Estándar |
| --- | --- | --- | --- | --- |
| **HC** | **CO** | **NOx** | **MP** | **MP** |
| 0,036 | 0,101 | 0,024 | 0,473 | Tier 1 |
| 0,034 | 0,101 | 0,009 | 0,473 | Tier 2 |
| 0,027 | 0,151 | 0,008 | 0,473 | Tier 3+ |

**Tabla 3-13.: Factor de deterioro por tipo de maquinaria y contaminante****

| Fase | Equipo | Potencia<br>(hp) | Factor de deterioro | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **Equipo** | **Potencia**<br>**(hp)** | **HC** | **CO** | **NOx** | **PM** |
| Construcción | Grúa | 40 | 1,008 | 1,024 | 1,002 | 1,111 |
| Construcción | Toro/Manitou | 40 | 1,011 | 1,032 | 1,003 | 1,148 |
| Construcción | Excavadora | 94 | 1,003 | 1,019 | 1,001 | 1,061 |
| Construcción | Retroexcavadora | 94 | 1,007 | 1,041 | 1,002 | 1,127 |
| Construcción | Bulldozer | 402 | 1,006 | 1,036 | 1,002 | 1,114 |
| Construcción | Cargadora frontal | 241 | 1,006 | 1,035 | 1,002 | 1,111 |
| Construcción | Hincadora/Perforadora | 54 | 1,003 | 1,017 | 1,001 | 1,054 |
| Construcción | Motoniveladora | 148 | 1,006 | 1,031 | 1,002 | 1,098 |
| Construcción | Rodillo | 27 | 1,010 | 1,029 | 1,003 | 1,136 |
| Operación | Tractor | 19 | 1,013 | 1,038 | 1,003 | 1,180 |

**Tabla 3-14.: Factor de ajuste de emisión de material particulado dado el contenido de azufre en el combustible****

| Fase | Equipo | Potencia<br>(hp) | BSFC | soxcnv | soxbas | soxdsl | S<br>PMadj |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Construcción | Grúa | 40 | 0,4080 | 0,02247 | 0,33 | 0,005 | 0,0946 |
| Construcción | Toro/Manitou | 40 | 0,4121 | 0,02247 | 0,33 | 0,005 | 0,0956 |
| Construcción | Excavadora | 94 | 0,4121 | 0,02247 | 0,33 | 0,005 | 0,0956 |
| Construcción | Retroexcavadora | 94 | 0,4814 | 0,02247 | 0,33 | 0,005 | 0,1116 |
| Construcción | Bulldozer | 402 | 0,3707 | 0,02247 | 0,33 | 0,005 | 0,0859 |
| Construcción | Cargadora frontal | 241 | 0,3707 | 0,02247 | 0,33 | 0,005 | 0,0859 |
| Construcción | Hincadora/Perforadora | 54 | 0,4121 | 0,02247 | 0,33 | 0,005 | 0,0956 |
| Construcción | Motoniveladora | 148 | 0,3707 | 0,02247 | 0,33 | 0,005 | 0,0859 |
| Construcción | Rodillo | 27 | 0,4121 | 0,02247 | 0,33 | 0,005 | 0,0956 |
| Operación | Tractor | 19 | 0,4080 | 0,02247 | 0,33 | 0,005 | 0,0946 |

**Tabla 3-15.: Factores de emisión ajustados de MP10 y gases para combustión de maquinaria****

| Fase | Equipo | Potencia<br>(hp) | Factor de emisión (g/hp-h) | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **Equipo** | **Potencia**<br>**(hp)** | **HC** | **CO** | **NOx** | **MP10** | **SO2 ** |
| Construcción | Grúa | 40 | 0,281 | 1,569 | 4,738 | 0,376 | 0,018 |
| Construcción | Toro/Manitou | 40 | 0,296 | 2,418 | 4,504 | 0,478 | 0,018 |
| Construcción | Excavadora | 94 | 0,193 | 3,690 | 3,123 | 0,468 | 0,018 |
| Construcción | Retroexcavadora | 94 | 0,423 | 6,326 | 3,638 | 0,801 | 0,021 |
| Construcción | Bulldozer | 402 | 0,176 | 1,336 | 2,605 | 0,246 | 0,016 |
| Construcción | Cargadora frontal | 241 | 0,194 | 1,184 | 2,605 | 0,245 | 0,016 |
| Construcción | Hincadora/Perforadora | 54 | 0,193 | 3,682 | 3,123 | 0,465 | 0,018 |
| Construcción | Motoniveladora | 148 | 0,194 | 1,368 | 2,604 | 0,355 | 0,016 |
| Construcción | Rodillo | 27 | 0,296 | 2,412 | 4,930 | 0,566 | 0,018 |
| Operación | Tractor | 19 | 0,444 | 2,244 | 4,455 | 0,314 | 0,018 |

**Tabla 3-16.: Factor de Emisión Para Gases y MP de Vehículos****

| Categoría | Contaminante | Factor de emisión (g/km) |
| --- | --- | --- |
| Camiones Pesados<br>Diésel Tipo 3 | CO | (1,24588358438859+(103,700537481749/(1+exp((((-1)*-<br>1,3906312471446)+(0,543451750078654*ln(V)))+(0,0390066425998189* V))))) |
| Camiones Pesados<br>Diésel Tipo 3 | HC | ((0,135938586321894+(0,71588074810547*exp(((-<br>1)*0,0234666513590177)*V)))+(2,79878282504916*exp(((-<br>1)*0,123459782380517)*V))) |
| Camiones Pesados<br>Diésel Tipo 3 | NOx | ((5,58300975720938+(14,5724996214701*exp(((-<br>1)*0,0510403515051286)*V)))+(45,651882800859*exp(((- |

**Tabla 3-17.: Factores de emisión de MP y gases para grupos electrógenos equipo nuevo y consumo de****

| Fase | Combustible | Potencia<br>(kW) | Estándar<br>de<br>emisión | Factor de emisión equipo nuevo (g/kW-h) | Col6 | Col7 | Col8 | BSFC |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **Combustible** | **Potencia**<br>**(kW)** | **Estándar**<br>**de**<br>**emisión** | **MP** | **NOx** | **CO** | **HC** | **HC** |
| Construcción | Diesel | 40 | Tier 2 | 0,322 | 6,303 | 3,172 | 0,492 | 248 |
| Cierre | Diesel | 40 | Tier 2 | 0,322 | 6,303 | 3,172 | 0,492 | 248 |

**Tabla 3-18.: Factor de carga, vida media, horas de funcionamiento, edad promedio y factor de edad para grupos****

| Fase | Horas de<br>operación (h) | Factor de<br>carga | Vida media<br>(h) | Vida útil<br>(años) | Edad<br>promedio<br>(años) | Factor de<br>edad |
| --- | --- | --- | --- | --- | --- | --- |
| Construcción | 960 | 0,7 | 4667 | 7 | 2 | 0,346 |
| Cierre | 576 | 0,7 | 4667 | 12 | 2 | 0,173 |

**Tabla 3-19.: Valor del factor A necesario para determinar el factor de deterioro por tipo de contaminante para****

| Estándar de emisión | Factor de deterioro relativo (A) | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Estándar de emisión** | **MP** | **NOx** | **CO** | **HC** |
| Tier 2 | 0,473 | 0,009 | 0,101 | 0,034 |

**Tabla 3-20.: Factor de deterioro por tipo de contaminante para grupos electrógenos****

| Fase | Combustible | Potencia<br>(kW) | Estándar de<br>emisión | Factor de deterioro | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **Combustible** | **Potencia**<br>**(kW)** | **Estándar de**<br>**emisión** | **MP** | **NOx** | **CO** | **HC** |
| Construcción | Diesel | 40 | Tier 2 | 1,136 | 1,003 | 1,029 | 1,010 |
| Cierre | Diesel | 40 | Tier 2 | 1,082 | 1,002 | 1,017 | 1,006 |

**Tabla 3-21.: Factor de ajuste de emisión de material particulado dado el contenido de azufre en el combustible****

| Fase | Combustible | Potencia<br>(kW) | Estándar<br>de<br>emisión | BSFC | TAF | soxcnv | soxbas | soxdsl | S<br>PMadj |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Construcción | Diesel | 40 | Tier 2 | 248 | 1 | 0,02247 | 0,2 | 0,005 | 0,0761 |
| Cierre | Diesel | 40 | Tier 2 | 248 | 1 | 0,02247 | 0,2 | 0,005 | 0,0761 |

**Tabla 3-22.: Factores de emisión ajustados de MP y gases para grupos electrógenos****

| Fase | Combustible | Potencia<br>(kW) | Estándar<br>de<br>emisión | Factor de emisión (g/kW-h) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **Combustible** | **Potencia**<br>**(kW)** | **Estándar**<br>**de**<br>**emisión** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2 ** |
| Construcción | Diesel | 40 | Tier 2 | 0,290 | 0,281 | 6,319 | 3,264 | 0,497 | 0,024 |
| Cierre | Diesel | 40 | Tier 2 | 0,272 | 0,264 | 6,313 | 3,227 | 0,495 | 0,024 |

**Tabla 3-23.: Niveles de actividad de maquinaria en fases de construcción y operación****

| Fase | Equipo | Cantidad de<br>equipos | Horas de<br>operación<br>anuales | Potencia (kW) |
| --- | --- | --- | --- | --- |
| Construcción | Grúa | 1 | 768 | 30 |
| Construcción | Toro/Manitou | 2 | 1536 | 30 |
| Construcción | Excavadora | 1 | 384 | 70 |
| Construcción | Retroexcavadora | 2 | 1536 | 70 |
| Construcción | Bulldozer | 1 | 96 | 300 |
| Construcción | Cargadora frontal | 1 | 96 | 180 |
| Construcción | Hincadora/Perforadora | 1 | 384 | 40 |
| Construcción | Motoniveladora | 1 | 192 | 110 |
| Construcción | Rodillo | 1 | 192 | 20 |
| Operación | Tractor | 2 | 1152 | 14 |

**Tabla 3-24.: Vehículos utilizados en fase de construcción****

| Tipo de vehículo | Carga | Origen | Destino | Peso vehículo (t) | Col6 | Viajes<br>mensuales<br>(ida) | Distancia (km) - Tipo de<br>carpeta | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo de vehículo** | **Carga** | **Origen** | **Destino** | **Vacío** | **Cargado** | **Cargado** | **Pavimentado** | **No**<br>**pavimentado** |
| Camioneta 4x4 y<br>furgoneta | Personal | Los Ángeles | Faena | 1,9 | 3,0 | 240 | 42,3 | 5,6 |
| Bus | Personal | Los Ángeles | Faena | (*) | 19,0 | 48 | 42,3 | 5,6 |
| Camión tanque | Combustible | Los Ángeles | Faena | 7,8 | 36,9 | 2 | 42,3 | 5,6 |
| Camión aljibe<br>20.000L o similar | Agua | Caminos internos y acceso<br>por Ruta S/R | Caminos internos y acceso<br>por Ruta S/R | 10,5 | 30,5 | 48 | - | 5,6 |
| Camión aljibe<br>20.000L o similar | Agua potable | Los Ángeles | Faena | 10,5 | 30,5 | 2 | 42,3 | 5,6 |
| Camión<br>Hormigonero 6 m3 | Hormigón | Planta de<br>hormigón<br>(Los Ángeles) | <br>Faena | 11,6 | 32,2 | 8 | 45,3 | 5,6 |
| Camión grúa | Carga en<br>General | Los Ángeles | Faena | 7,3 | 27,0 | 8 | 42,3 | 5,6 |
| Camión 20 t o<br>similar | Perfiles de<br>acero | Los Ángeles | Faena | 10,3 | 32,0 | 6 | 42,3 | 5,6 |
| Camión 30 t o<br>similar | Módulos<br>Fotovoltaicos | Talcahuano | Faena | 9,7 | 40,0 | 12 | 143,2 | 5,6 |

**Tabla 3-25.: Vehículos utilizados en fase de operación****

| Tipo de vehículo | Carga | Origen | Destino | Peso vehículo (t) | Col6 | Viajes<br>anuales<br>(ida) | Distancia (km) - Tipo de<br>carpeta | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo de vehículo** | **Carga** | **Origen** | **Destino** | **Vacío** | **Cargado** | **Cargado** | **Pavimento** | **No**<br>**pavimentado** |
| Camioneta 4x4 y<br>furgoneta | Personal | Los Ángeles | Planta | 1,9 | 3,0 | 144 | 42,3 | 5,6 |
| Camión | Equipos y<br>maquinaria | Los Ángeles | Planta | 9,7 | 40,0 | 2 | 42,3 | 5,6 |
| Camión aljibe<br>30.000L o similar | Agua<br>limpieza<br>paneles | Los Ángeles | Planta | 14,0 | 44,0 | 4 | 42,3 | 5,6 |
| Camión aljibe<br>20.000L o similar | Agua potable | Los Ángeles | Planta | 10,5 | 30,5 | 4 | 42,3 | 5,6 |
| Camión tanque | Combustible | Los Ángeles | Planta | 7,8 | 36,9 | 2 | 42,3 | 5,6 |
| Camión<br>Habilitado | Residuos | Planta | Relleno<br>sanitario<br>de Los<br>Ángeles | 5,6 | 17,1 | 4 | 59,7 | 7,2 |

**Tabla 3-26.: Vehículos utilizados en fase de cierre****

| Tipo de vehículo | Carga | Origen | Destino | Peso vehículo (t) | Col6 | Viajes<br>mensuales<br>(ida) | Distancia (km) - Tipo de<br>carpeta | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo de vehículo** | **Carga** | **Origen** | **Destino** | **Vacío** | **Cargado** | **Cargado** | **Pavimento** | **No**<br>**pavimentado** |
| Camioneta 4x4 | Personal | Los Ángeles | Planta | 1,9 | 3,0 | 30 | 42,3 | 5,6 |
| Bus | Personal | Los Ángeles | Planta | (*) | 19,0 | 15 | 42,3 | 5,6 |
| Camión | Equipos y<br>maquinaria | Planta | Los Ángeles | 10,3 | 32,0 | 15 | 42,3 | 5,6 |
| Camión<br>aljibe<br>20.000L o similar | Agua<br>industrial | Caminos internos y acceso<br>por Ruta S/R | Caminos internos y acceso<br>por Ruta S/R | 10,5 | 30,5 | 30 | - | 5,6 |
| Camión<br>Aljibe<br>20.000L o similar | Agua<br>industrial | Los Ángeles | Planta | 10,5 | 30,5 | 1 | 42,3 | 5,6 |
| Camión<br>aljibe<br>20.000L o similar | Agua potable | Los Ángeles | Planta | 10,5 | 30,5 | 1 | 42,3 | 5,6 |
| Camión tanque | Combustible | Los Ángeles | Planta | 7,8 | 36,9 | 1 | 42,3 | 5,6 |
| Camión 15 t | Módulos | Planta | Zona de<br>reciclaje<br>habilitada<br>(Hidronor) | 6,8 | 24,1 | 12 | 137,6 | 5,6 |
| Camión<br>habilitado | Residuos | Planta | Relleno<br>sanitario de<br>Los Ángeles | 5,6 | 17,1 | 6 | 59,7 | 7,2 |

**Tabla 3-27.: Rutas utilizadas****

| Tramo | Col2 | Ruta | Detalle ruta | Longitud<br>subtramo<br>(km) | Tipo de camino | Longitud<br>no pav<br>(km) | Longitud<br>pav<br>(km) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Proyecto - Los<br>Ángeles | Ruta S/R - Ruta 180 - Vicuña<br>Mackenna - San Martín | Ruta S/R | 3,0 | No pavimentado | 3,0 | 42,3 |
| 1 | Proyecto - Los<br>Ángeles | Ruta S/R - Ruta 180 - Vicuña<br>Mackenna - San Martín | Ruta 180 | 37,1 | Pavimentado | Pavimentado | Pavimentado |
| 1 | Proyecto - Los<br>Ángeles | Ruta S/R - Ruta 180 - Vicuña<br>Mackenna - San Martín | Interior Los<br>Ángeles | 5,2 | Pavimentado | Pavimentado | Pavimentado |
| 2 | Proyecto -<br>Talcahuano | Ruta S/R - Ruta 180 - Ruta 156 -<br>Puente Chacabuco - Nueva<br>Costanera - Gran Bretaña -<br>Juan Antonio Ríos - La Marina | Ruta S/R | 3,0 | No pavimentado | 3,0 | 143,2 |
| 2 | Proyecto -<br>Talcahuano | Ruta S/R - Ruta 180 - Ruta 156 -<br>Puente Chacabuco - Nueva<br>Costanera - Gran Bretaña -<br>Juan Antonio Ríos - La Marina | Ruta 180 | 17,2 | Pavimentado | Pavimentado | Pavimentado |
| 2 | Proyecto -<br>Talcahuano | Ruta S/R - Ruta 180 - Ruta 156 -<br>Puente Chacabuco - Nueva<br>Costanera - Gran Bretaña -<br>Juan Antonio Ríos - La Marina | Ruta 156 | 109,0 | Pavimentado | Pavimentado | Pavimentado |
| 2 | Proyecto -<br>Talcahuano | Ruta S/R - Ruta 180 - Ruta 156 -<br>Puente Chacabuco - Nueva<br>Costanera - Gran Bretaña -<br>Juan Antonio Ríos - La Marina | Interior<br>Talcahuano | 17,0 | Pavimentado | Pavimentado | Pavimentado |
| 3 | Proyecto -<br>Planta de áridos | Ruta S/R - Ruta 180 - Ruta Q-<br>530 | Ruta S/R | 3,0 | No pavimentado | 7,0 | 22,3 |
| 3 | Proyecto -<br>Planta de áridos | Ruta S/R - Ruta 180 - Ruta Q-<br>530 | Ruta 180 | 22,3 | Pavimentado | Pavimentado | Pavimentado |
| 3 | Proyecto -<br>Planta de áridos | Ruta S/R - Ruta 180 - Ruta Q-<br>530 | Ruta Q-530 | 4,0 | No pavimentado | No pavimentado | No pavimentado |

**Tabla 3-28.: Horas de operación de generadores eléctricos.****

| Fase | Cantidad de equipos | Potencia (kw) | Horas totales |
| --- | --- | --- | --- |
| Construcción | 1 | 40 | 960 |
| Cierre | 1 | 40 | 576 |

**Tabla 3-29.: Nivel de actividad asociado a nivelación****

| Actividad | Obra | Nivel de Actividad | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Actividad** | **Obra** | **Cantidad de**<br>**material a**<br>**excavar (m3) ** | **Rendimiento de**<br>**la pala (m3/h)** | **Horas de**<br>**excavación (h)** |
| Excavaciones | Terreno de Planta FV (Movimiento de<br>Tierras incluyendo terrazas de<br>subcampos y caminos interiores) | 2000 | 30 | **67** |
| Excavaciones | Otros (instalación de trackers, zanjas<br>BT/MT, vallado, edificaciones, casetas,<br>instalación de faena, acceso y<br>subestación) | 500 | 30 | **17** |

**Tabla 3-31.: Nivel de actividad asociado a transferencia de material****

| Actividad | Sub-actividad | Nivel de Actividad | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Actividad** | **Sub-actividad** | **Material a**<br>**transferir (m3) ** | **Densidad del**<br>**material (t/m3) ** | **Material a**<br>**descargar (t)** |
| Transferencia de<br>material | Carga de material en camiones | 2500 | 1,8 | **4500** |
| Transferencia de<br>material | Descarga de material excavado como<br>relleno | 2500 | 1,8 | **4500** |
| Transferencia de<br>material | Descarga de áridos | 1100 | 1,8 | **1980** |

**Tabla 3-32.: Variables y valores utilizados para eficiencia en humectación.****

| Variable | Caminos internos | Acceso por Ruta S/R |
| --- | --- | --- |
| A” (*) | 44,33 | 44,33 |
| D (veh/hora) | 4,6 | 4,2 |
| T (h) | 4 | 4 |
| I (gal/yd2) | 0,039 | 0,036 |
| I (L/m2) | 0,18 | 0,16 |

**Tabla 3-33.: Cálculo de agua para humectación de caminos****

| Variable | Caminos internos | Acceso por Ruta S/R |
| --- | --- | --- |
| Camino (m) | 2600 | 3000 |
| Ancho (m) | 6 | 6 |
| Superficie (m2) | 15600 | 18000 |
| Total (m3/pasada) | 2,7 | 2,9 |
| Total (m3/día) | 5,5 | 5,9 |

**Tabla 3-34.: Emisiones por tránsito de vehículos en caminos pavimentados en fase de construcción****

| Actividad | Tramo | Sub-tramo | Factor de Emisión (g/km-veh) | Col5 | Col6 | Nivel de<br>Actividad<br>(km-<br>veh/mes) | Duración<br>de la<br>actividad<br>(mes) | Medida de<br>control<br>(%) | Emisión (t) | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Tramo** | **Sub-tramo** | **MP30** | **MP10** | **MP2,5** | **MP2,5** | **MP2,5** | **MP2,5** | **MP30** | **MP10** | **MP2,5** |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Los Ángeles | Ruta 180 | 2,0 | 0,4 | 0,1 | 22854 | 6 | 0 | 0,27 | 0,05 | 0,01 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Los Ángeles | interior Los Ángeles | 2,0 | 0,4 | 0,1 | 3203 | 6 | 0 | 0,04 | 0,01 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Talcahuano | Ruta 180 | 2,0 | 0,4 | 0,1 | 826 | 6 | 0 | 0,01 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Talcahuano | Ruta 156 | 5,9 | 1,1 | 0,3 | 5232 | 6 | 0 | 0,19 | 0,04 | 0,01 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Talcahuano | Interior Talcahuano | 1,1 | 0,2 | 0,0 | 816 | 6 | 0 | 0,01 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Planta de<br>áridos | Ruta 180 | 2,0 | 0,4 | 0,1 | 624 | 6 | 0 | 0,01 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Planta de<br>hormigón | Ruta 180 | 2,0 | 0,4 | 0,1 | 594 | 6 | 0 | 0,01 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Planta de<br>hormigón | interior Los Ángeles | 2,0 | 0,4 | 0,1 | 131 | 6 | 0 | 0,00 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Relleno<br>sanitario | Ruta 180 | 2,0 | 0,4 | 0,1 | 148 | 6 | 0 | 0,00 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Relleno<br>sanitario | Ruta 5 | 1,1 | 0,2 | 0,0 | 90 | 6 | 0 | 0,00 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Hidronor | Ruta 180 | 2,0 | 0,4 | 0,1 | 34 | 6 | 0 | 0,00 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Hidronor | Ruta 156 | 5,9 | 1,1 | 0,3 | 218 | 6 | 0 | 0,01 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Hidronor | Interior Talcahuano | 1,1 | 0,2 | 0,0 | 23 | 6 | 0 | 0,00 | 0,00 | 0,00 |
| <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> | **0,54** | **0,10** | **0,02** |

**Tabla 3-35.: Contenido de silt (sL) de caminos pavimentados del Proyecto****

| Calle/Ruta | Tipo de flujo | sL (g/m2) |
| --- | --- | --- |
| Ruta 156 | 500-5000 veh/d | 0,2 |
| Ruta 180 | 5000-10000 veh/d | 0,06 |
| Interior Los Ángeles | Interior Los Ángeles | Interior Los Ángeles |
| Interior Talcahuano | >10000 veh/d | 0,03 |
| Ruta 5 | Ruta 5 | Ruta 5 |

**Tabla 3-36.: Emisiones por tránsito de vehículos en caminos no pavimentados en fase de construcción****

| Actividad | Tramo | Factor de Emisión (g/km-<br>veh) | Col4 | Col5 | Nivel de<br>Actividad<br>(km-<br>veh/mes) | Duración<br>de la<br>actividad<br>(mes) | Medida<br>de<br>control<br>(%) | Emisión (t) | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Tramo** | **MPS** | **MP10** | **MP2,5** | **MP2,5** | **MP2,5** | **MP2,5** | **MPS** | **MP10** | **MP2,5** |
| Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados | Interior del<br>proyecto | 1630 | 466 | 47 | 2272 | 6 | 75 | 5,55 | 1,59 | 0,16 |
| Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados | Ruta S/R | 1570 | 449 | 45 | 2430 | 6 | 75 | 5,72 | 1,64 | 0,16 |
| Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados | Ruta Q-530<br>(acceso a planta<br>de áridos) | 2226 | 636 | 64 | 112 | 6 |  | 1,50 | 0,43 | 0,04 |
| Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados | Acceso a relleno<br>sanitario | 1674 | 478 | 48 | 6 | 6 |  | 0,06 | 0,02 | 0,00 |
| <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> | **12,84** | **3,67** | **0,37** |

**Tabla 3-37.: Emisiones por tránsito de vehículos en caminos no pavimentados en fase de construcción****

| Peso flota | Col2 |
| --- | --- |
| W: Peso de la flota interior Proyecto (t) | 10,7 |
| W: Peso de la flota Ruta S/R (acceso al Proyecto) (t) | 9,9 |
| W: Peso de la flota Ruta Q-530 (acceso a planta de áridos) (t) | 21,4 |
| W: Peso de la flota acceso a relleno sanitario (t) | 11,4 |

**Tabla 3-38.: Emisiones por nivelación en fase de construcción****

| Actividad | Obra | Factor de Emisión (kg/h) | Col4 | Col5 | Nivel de<br>Actividad<br>(h) | Emisión (t) | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Obra** | **MPS** | **MP10** | **MP2,5** | **MP2,5** | **MPS** | **MP10** | **MP2,5** |
| Excavaciones | Terreno de Planta FV | 2,98 | 0,61 | 0,31 | 67 | 0,198 | 0,041 | 0,021 |
| Excavaciones | Otros | 2,98 | 0,61 | 0,31 | 17 | 0,050 | 0,010 | 0,005 |
|  |  |  |  |  |  | **0,248** | **0,051** | **0,026** |

**Tabla 3-40.: Emisiones por transferencia de material en fase de construcción****

| Actividad | Obra | Factor de Emisión (kg/t) | Col4 | Col5 | Nivel de<br>Actividad<br>(t) | Emisión (t) | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Obra** | **MPS** | **MP10** | **MP2,5** | **MP2,5** | **MPS** | **MP10** | **MP2,5** |
| Transferencia<br>de material<br> | Carga de material en<br>camiones | 0,00054 | 0,00026 | 0,00004 | 4500 | 0,00245 | 0,00116 | 0,00018 |
| Transferencia<br>de material<br> | Descarga de material<br>excavado como<br>relleno | 0,00054 | 0,00026 | 0,00004 | 4500 | 0,00245 | 0,00116 | 0,00018 |
| Transferencia<br>de material<br> | Descarga de áridos<br> | 0,00054<br> | 0,00026<br> | 0,00004<br> | 1980<br> | 0,00108 | 0,00051 | 0,00008 |
| <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> | **0,00597** | **0,00282** | **0,00043** |

**Tabla 3-41.: Emisiones por motores de maquinaria en fase de construcción****

| Equipo | Factor de emisión (g/hp-h) | Col3 | Col4 | Col5 | Col6 | Col7 | Potencia<br>(hp) | Factor de<br>carga | Horas de<br>actividad<br>(h) | Cantidad<br>de<br>equipos | Emisión (t) | Col13 | Col14 | Col15 | Col16 | Col17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Equipo** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2 ** | **SO2 ** | **SO2 ** | **SO2 ** | **SO2 ** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2 ** |
| Grúa | 0,376 | 0,365 | 4,738 | 1,569 | 0,281 | 0,018 | 40 | 0,47 | 768 | 1 | 0,005 | 0,005 | 0,069 | 0,023 | 0,004 | 0,000 |
| Toro/Manitou | 0,478 | 0,464 | 4,504 | 2,418 | 0,296 | 0,018 | 40 | 0,63 | 1536 | 2 | 0,037 | 0,036 | 0,351 | 0,188 | 0,023 | 0,001 |
| Excavadora | 0,468 | 0,454 | 3,123 | 3,690 | 0,193 | 0,018 | 94 | 0,53 | 384 | 1 | 0,009 | 0,009 | 0,060 | 0,070 | 0,004 | 0,000 |
| Retroexcavadora | 0,801 | 0,777 | 3,638 | 6,326 | 0,423 | 0,021 | 94 | 0,48 | 1536 | 2 | 0,111 | 0,108 | 0,504 | 0,876 | 0,059 | 0,003 |
| Bulldozer | 0,246 | 0,238 | 2,605 | 1,336 | 0,176 | 0,016 | 402 | 0,80 | 96 | 1 | 0,008 | 0,007 | 0,080 | 0,041 | 0,005 | 0,001 |
| Cargadora frontal | 0,245 | 0,238 | 2,605 | 1,184 | 0,194 | 0,016 | 241 | 0,71 | 96 | 1 | 0,004 | 0,004 | 0,043 | 0,019 | 0,003 | 0,000 |
| Hincadora/Perforadora | 0,465 | 0,451 | 3,123 | 3,682 | 0,193 | 0,018 | 54 | 0,48 | 384 | 1 | 0,005 | 0,004 | 0,031 | 0,036 | 0,002 | 0,000 |
| Motoniveladora | 0,355 | 0,344 | 2,604 | 1,368 | 0,194 | 0,016 | 148 | 0,64 | 192 | 1 | 0,006 | 0,006 | 0,047 | 0,025 | 0,004 | 0,000 |
| Rodillo | 0,566 | 0,549 | 4,930 | 2,412 | 0,296 | 0,018 | 27 | 0,49 | 192 | 1 | 0,001 | 0,001 | 0,012 | 0,006 | 0,001 | 0,000 |
| <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | **0,187** | **0,181** | **1,197** | **1,285** | **0,104** | **0,006** |

**Tabla 3-42.: Emisiones por operación de generadores en fase de construcción****

| Potencia<br>(kW) | Cantidad de<br>equipos | Horas de<br>operación (h) | Factor de<br>carga | Emisión (t) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Potencia**<br>**(kW)** | **Cantidad de**<br>**equipos** | **Horas de**<br>**operación (h)** | **Factor de**<br>**carga** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2 ** |
| 40 | 1 | 960 | 0,7 | 0,008 | 0,008 | 0,170 | 0,088 | 0,013 | 0,001 |

**Tabla 3-43.: Emisiones por combustión de motores de vehículos fase de construcción****

| Tipo de<br>Vehículo | Tipo de<br>superficie | Tramo | Factor de Emisión (g/km-veh) | Col5 | Col6 | Col7 | Col8 | Col9 | Nivel de<br>Actividad<br>(km-<br>veh/mes) | meses/año | Emisión (t/año) | Col13 | Col14 | Col15 | Col16 | Col17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo de**<br>**Vehículo** | **Tipo de**<br>**superficie** | **Tramo** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2 ** | **SO2 ** | **SO2 ** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2 ** |
| Vehículos<br>Comerciales<br>Diesel Tipo 2 | Pavimentada | Proyecto - Los<br>Ángeles | 0,042 | 0,040 | 0,826 | 0,261 | 0,067 | 0,002 | 20304 | 6 | 0,005 | 0,005 | 0,101 | 0,032 | 0,008 | 0,000 |
| Vehículos<br>Comerciales<br>Diesel Tipo 2 | Sin pavimentar | Ruta S/R<br>(acceso a<br>Proyecto) | 0,047 | 0,045 | 0,956 | 0,322 | 0,081 | 0,002 | 1440 | 6 | 0,000 | 0,000 | 0,008 | 0,003 | 0,001 | 0,000 |
| Vehículos<br>Comerciales<br>Diesel Tipo 2 | Sin pavimentar | Interior<br>Proyecto | 0,047 | 0,045 | 0,956 | 0,322 | 0,081 | 0,002 | 1248 | 6 | 0,000 | 0,000 | 0,007 | 0,002 | 0,001 | 0,000 |
| Buses<br>Interurbanos<br>Diesel Tipo 3 | Pavimentada | Proyecto - Los<br>Ángeles | 0,166 | 0,161 | 6,852 | 1,742 | 0,413 | 0,007 | 4061 | 6 | 0,004 | 0,004 | 0,167 | 0,042 | 0,010 | 0,000 |
| Buses<br>Interurbanos<br>Diesel Tipo 3 | Sin pavimentar | Ruta S/R<br>(acceso a<br>Proyecto) | 0,250 | 0,242 | 9,821 | 2,743 | 0,665 | 0,010 | 288 | 6 | 0,000 | 0,000 | 0,017 | 0,005 | 0,001 | 0,000 |
| Buses<br>Interurbanos<br>Diesel Tipo 3 | Sin pavimentar | Interior<br>Proyecto | 0,250 | 0,242 | 9,821 | 2,743 | 0,665 | 0,010 | 250 | 6 | 0,000 | 0,000 | 0,015 | 0,004 | 0,001 | 0,000 |
| Camiones<br>Pesados<br>Diesel Tipo 3 | Pavimentada | Proyecto - Los<br>Ángeles | 0,154 | 0,154 | 6,719 | 1,682 | 0,363 | 0,007 | 1692 | 6 | 0,002 | 0,002 | 0,068 | 0,017 | 0,004 | 0,000 |
| Camiones<br>Pesados<br>Diesel Tipo 3 | Pavimentada | Proyecto -<br>Talcahuano | 0,154 | 0,154 | 6,719 | 1,682 | 0,363 | 0,007 | 6874 | 6 | 0,006 | 0,006 | 0,277 | 0,069 | 0,015 | 0,000 |
| Camiones<br>Pesados<br>Diesel Tipo 3 | Pavimentada | Proyecto -<br>Planta de<br>áridos | 0,154 | 0,154 | 6,719 | 1,682 | 0,363 | 0,007 | 624 | 6 | 0,001 | 0,001 | 0,025 | 0,006 | 0,001 | 0,000 |
| Camiones<br>Pesados<br>Diesel Tipo 3 | Pavimentada | Proyecto -<br>Planta de<br>hormigón | 0,154 | 0,154 | 6,719 | 1,682 | 0,363 | 0,007 | 725 | 6 | 0,001 | 0,001 | 0,029 | 0,007 | 0,002 | 0,000 |
| Camiones<br>Pesados<br>Diesel Tipo 3 | Pavimentada | Proyecto -<br>Relleno<br>sanitario | 0,154 | 0,154 | 6,719 | 1,682 | 0,363 | 0,007 | 239 | 6 | 0,000 | 0,000 | 0,010 | 0,002 | 0,001 | 0,000 |
| Camiones<br>Pesados<br>Diesel Tipo 3 | Pavimentada | Proyecto -<br>Hidronor | 0,154 | 0,154 | 6,719 | 1,682 | 0,363 | 0,007 | 275 | 6 | 0,000 | 0,000 | 0,011 | 0,003 | 0,001 | 0,000 |
| Camiones<br>Pesados<br>Diesel Tipo 3 | Sin pavimentar | Ruta S/R<br>(acceso a<br>Proyecto) | 0,230 | 0,230 | 8,739 | 2,492 | 0,559 | 0,010 | 2430 | 6 | 0,003 | 0,003 | 0,127 | 0,036 | 0,008 | 0,000 |

**Tabla 3-44.: Emisiones por tránsito de vehículos en caminos pavimentados en fase de operación****

| Actividad | Tramo | Sub-tramo | Factor de Emisión<br>(g/km-veh) | Col5 | Col6 | Nivel de<br>Actividad<br>(km-<br>veh/año) | Emisión (t/año) | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Tramo** | **Sub-tramo** | **MPS** | **MP10** | **MP2,5** | **MP2,5** | **MPS** | **MP10** | **MP2,5** |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados<br> | Proyecto<br>- Los<br>Ángeles | Ruta 180 | 2,0 | 0,4 | 0,1 | 11575 | 0,02 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados<br> | Proyecto<br>- Los<br>Ángeles | interior Los Ángeles | 2,0 | 0,4 | 0,1 | 1622 | 0,00 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados<br> | Proyecto<br>- Relleno<br>sanitario<br> | Ruta 180 | 2,0 | 0,4 | 0,1 | 297 | 0,00 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados<br> | Proyecto<br>- Relleno<br>sanitario<br> | Ruta 5<br> | 1,1<br> | 0,2<br> | 0,0<br> | 181<br> | 0,00 | 0,00 | 0,00 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **0,03** | **0,01** | **0,00** |

**Tabla 3-45.: Emisiones por tránsito de vehículos en caminos no pavimentados en fase de operación****

| Actividad | Tramo | Factor de Emisión (g/km-veh) | Col4 | Col5 | Nivel de<br>Actividad<br>(km-<br>veh/año) | Medida<br>de<br>control<br>(%) | Emisión (t/año) | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Tramo** | **MPS** | **MP10** | **MP2,5** | **MP2,5** | **MP2,5** | **MPS** | **MP10** | **MP2,5** |
| Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados<br> | Interior del<br>proyecto | 1084 | 310 | 31 | 832 | 0 | 0,90 | 0,26 | 0,03 |
| Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados<br> | Ruta S/R | 1084 | 310 | 31 | 960 | 0 | 1,04 | 0,30 | 0,03 |
| Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados<br> | Acceso a<br>relleno<br>sanitario<br> | 1674<br> | 478<br> | 48<br> | 13<br> | 0 <br> | 0,02 | 0,01 | 0,00 |
| <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> | **1,96** | **0,56** | **0,06** |

**Tabla 3-46.: Emisiones por tránsito de vehículos en caminos no pavimentados en fase de operación****

| Peso flota | Col2 |
| --- | --- |
| W: Peso de la flota interior Proyecto (t) | 4,3 |
| W: Peso de la flota Ruta S/R (acceso al Proyecto) (t) | 4,3 |
| W: Peso de la flota acceso a relleno sanitario (t) | 11,4 |

**Tabla 3-47.: Emisiones por combustión de motores de vehículos en fase de operación****

| Tipo de<br>Vehículo | Tipo de<br>superficie | Tramo | Factor de Emisión (g/km-veh) | Col5 | Col6 | Col7 | Col8 | Col9 | Nivel de<br>Actividad<br>(km-<br>veh/año) | Emisión (t/año) | Col12 | Col13 | Col14 | Col15 | Col16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo de**<br>**Vehículo** | **Tipo de**<br>**superficie** | **Tramo** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2** | **SO2** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2** |
| Vehículos<br>Comerciales<br>Diesel Tipo<br>2 | Pavimentada | Proyecto -<br>Los Ángeles | 0,042 | 0,040 | 0,826 | 0,261 | 0,067 | 0,002 | 12182 | 0,0005 | 0,0005 | 0,0101 | 0,0032 | 0,0008 | 0,0000 |
| Vehículos<br>Comerciales<br>Diesel Tipo<br>2 | Sin<br>pavimentar | Ruta S/R<br>(acceso a<br>Proyecto) | 0,047 | 0,045 | 0,956 | 0,322 | 0,081 | 0,002 | 864 | 0,0000 | 0,0000 | 0,0008 | 0,0003 | 0,0001 | 0,0000 |
| Vehículos<br>Comerciales<br>Diesel Tipo<br>2 | Sin<br>pavimentar | Interior<br>Proyecto | 0,047 | 0,045 | 0,956 | 0,322 | 0,081 | 0,002 | 749 | 0,0000 | 0,0000 | 0,0007 | 0,0002 | 0,0001 | 0,0000 |
| Camiones<br>Pesados<br>Diesel Tipo<br>3 | Pavimentada | Proyecto -<br>Los Ángeles | 0,154 | 0,154 | 6,719 | 1,682 | 0,363 | 0,007 | 1015 | 0,0002 | 0,0002 | 0,0068 | 0,0017 | 0,0004 | 0,0000 |
| Camiones<br>Pesados<br>Diesel Tipo<br>3 | Pavimentada | Proyecto -<br>Relleno<br>sanitario | 0,154 | 0,154 | 6,719 | 1,682 | 0,363 | 0,007 | 478 | 0,0001 | 0,0001 | 0,0032 | 0,0008 | 0,0002 | 0,0000 |
| Camiones<br>Pesados<br>Diesel Tipo<br>3 | Sin<br>pavimentar | Ruta S/R<br>(acceso a<br>Proyecto) | 0,230 | 0,230 | 8,739 | 2,492 | 0,559 | 0,010 | 960 | 0,0002 | 0,0002 | 0,0084 | 0,0024 | 0,0005 | 0,0000 |
| Camiones<br>Pesados<br>Diesel Tipo<br>3 | Sin<br>pavimentar | Acceso a<br>relleno<br>sanitario | 0,230 | 0,230 | 8,739 | 2,492 | 0,559 | 0,010 | 13 | 0,0000 | 0,0000 | 0,0001 | 0,0000 | 0,0000 | 0,0000 |
| Camiones<br>Pesados<br>Diesel Tipo<br>3 | Sin<br>pavimentar | Interior<br>Proyecto | 0,230 | 0,230 | 8,739 | 2,492 | 0,559 | 0,010 | 832 | 0,0002 | 0,0002 | 0,0073 | 0,0021 | 0,0005 | 0,0000 |
| <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> | **0,0012** | **0,0012** | **0,0374** | **0,0107** | **0,0025** | **0,0001** |

**Tabla 3-48.: Emisiones por motores de maquinaria en fase de operación****

| Equipo | Factor de emisión (g/hp-h) | Col3 | Col4 | Col5 | Col6 | Col7 | Potencia<br>(hp) | Factor de<br>carga | Horas de<br>actividad<br>(h/año) | Cantidad<br>de equipos | Emisión (t/año) | Col13 | Col14 | Col15 | Col16 | Col17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Equipo** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2 ** | **SO2 ** | **SO2 ** | **SO2 ** | **SO2 ** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2 ** |
| Tractor | 0,314 | 0,305 | 4,455 | 2,244 | 0,444 | 0,018 | 19 | 0,44 | 1152 | 2 | 0,024 | 0,023 | 0,350 | 0,109 | 0,026 | 0,002 |

**Tabla 3-49.: Emisiones por tránsito de vehículos en caminos pavimentados en fase de cierre****

| Actividad | Tramo | Sub-tramo | Factor de Emisión<br>(g/km-veh) | Col5 | Col6 | Nivel de<br>Actividad<br>(km-<br>veh/mes) | Duración<br>de la<br>actividad<br>(mes) | Emisión (t) | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Tramo** | **Sub-tramo** | **MPS** | **MP10** | **MP2,5** | **MP2,5** | **MP2,5** | **MPS** | **MP10** | **MP2,5** |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Los Ángeles | Ruta 180 | 2,0 | 0,4 | 0,1 | 4675 | 3 | 0,03 | 0,01 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Los Ángeles | interior Los<br>Ángeles | 2,0 | 0,4 | 0,1 | 655 | 3 | 0,00 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Relleno<br>sanitario | Ruta 180 | 2,0 | 0,4 | 0,1 | 445 | 3 | 0,00 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Relleno<br>sanitario | Ruta 5 | 1,1 | 0,2 | 0,0 | 271 | 3 | 0,00 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Hidronor | Ruta 180 | 2,0 | 0,4 | 0,1 | 413 | 3 | 0,00 | 0,00 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Hidronor | Ruta 156 | 5,9 | 1,1 | 0,3 | 2616 | 3 | 0,05 | 0,01 | 0,00 |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | Proyecto -<br>Hidronor | Interior<br>Talcahuano | 1,1 | 0,2 | 0,0 | 274 | 3 | 0,00 | 0,00 | 0,00 |
|  |  |  |  |  |  |  |  | **0,09** | **0,02** | **0,00** |

**Tabla 3-50.: Emisiones por tránsito de vehículos en caminos no pavimentados en fase de cierre****

| Actividad | Tramo | Factor de Emisión (g/km-<br>veh) | Col4 | Col5 | Nivel de<br>Actividad<br>(km-<br>veh/mes) | Duración<br>de la<br>actividad<br>(mes) | Medida<br>de<br>control<br>(%) | Emisión (t) | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **Tramo** | **MPS** | **MP10** | **MP2,5** | **MP2,5** | **MP2,5** | **MP2,5** | **MPS** | **MP10** | **MP2,5** |
| Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados<br> | Interior<br>del<br>proyecto | 1868 | 534 | 53 | 577 | 3 | 75 | 0,81 | 0,23 | 0,02 |
| Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados<br> | Ruta S/R | 1868 | 534 | 53 | 666 | 3 | 75 | 0,93 | 0,27 | 0,03 |
| Tránsito de<br>vehículos<br>pesados por<br>caminos no<br>pavimentados<br> | Acceso a<br>relleno<br>sanitario<br> | 1674 | 478 | 48 | 19 | 3 |  | 0,10 | 0,03 | 0,00 |
| <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> | **1,84** | **0,53** | **0,05** |

**Tabla 3-51.: Emisiones por tránsito de vehículos en caminos no pavimentados en fase de cierre****

| Peso flota | Col2 |
| --- | --- |
| W: Peso de la flota interior Proyecto (t) | 14,5 |
| W: Peso de la flota Ruta S/R (acceso al Proyecto) (t) | 8,9 |
| W: Peso de la flota acceso a relleno sanitario (t) | 11,4 |

**Tabla 3-52.: Emisiones por operación de generadores en fase de cierre****

| Potencia<br>(kW) | Cantidad<br>de<br>equipos | Horas de<br>operación<br>(h) | Factor de<br>carga | Emisión (t) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Potencia**<br>**(kW)** | **Cantidad**<br>**de**<br>**equipos** | **Horas de**<br>**operación**<br>**(h)** | **Factor de**<br>**carga** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2 ** |
| 40 | 1 | 576 | 0,7 | 0,004 | 0,004 | 0,102 | 0,052 | 0,008 | 0,000 |

**Tabla 3-53.: Emisiones por combustión de motores de vehículos en fase de cierre****

| Tipo de<br>Vehículo | Tipo de<br>superficie | Tramo | Factor de Emisión (g/km-veh) | Col5 | Col6 | Col7 | Col8 | Col9 | Nivel de<br>Actividad<br>(km-<br>veh/mes) | meses/año | Emisión (t/año) | Col13 | Col14 | Col15 | Col16 | Col17 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Tipo de**<br>**Vehículo** | **Tipo de**<br>**superficie** | **Tramo** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2 ** | **SO2 ** | **SO2 ** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2 ** |
| Vehículos<br>Comerciales<br>Diesel Tipo 2 | Pavimentada | Proyecto -<br>Los<br>Ángeles | 0,042 | 0,040 | 0,826 | 0,261 | 0,067 | 0,002 | 2538 | 3 | 0,000 | 0,000 | 0,006 | 0,002 | 0,001 | 0,000 |
| Vehículos<br>Comerciales<br>Diesel Tipo 2 | Sin<br>pavimentar | Ruta S/R<br>(acceso a<br>Proyecto) | 0,047 | 0,045 | 0,956 | 0,322 | 0,081 | 0,002 | 180 | 3 | 0,000 | 0,000 | 0,001 | 0,000 | 0,000 | 0,000 |
| Vehículos<br>Comerciales<br>Diesel Tipo 2 | Sin<br>pavimentar | Interior<br>Proyecto | 0,047 | 0,045 | 0,956 | 0,322 | 0,081 | 0,002 | 156 | 3 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| Buses<br>Interurbanos<br>Diesel Tipo 3 | Pavimentada | Proyecto -<br>Los<br>Ángeles | 0,166 | 0,161 | 6,852 | 1,742 | 0,413 | 0,007 | 1269 | 3 | 0,001 | 0,001 | 0,026 | 0,007 | 0,002 | 0,000 |
| Buses<br>Interurbanos<br>Diesel Tipo 3 | Sin<br>pavimentar | Ruta S/R<br>(acceso a<br>Proyecto) | 0,250 | 0,242 | 9,821 | 2,743 | 0,665 | 0,010 | 90 | 3 | 0,000 | 0,000 | 0,003 | 0,001 | 0,000 | 0,000 |
| Buses<br>Interurbanos<br>Diesel Tipo 3 | Sin<br>pavimentar | Interior<br>Proyecto | 0,250 | 0,242 | 9,821 | 2,743 | 0,665 | 0,010 | 78 | 3 | 0,000 | 0,000 | 0,002 | 0,001 | 0,000 | 0,000 |
| Camiones<br>Pesados<br>Diesel Tipo 3 | Pavimentada | Proyecto -<br>Los<br>Ángeles | 0,154 | 0,154 | 6,719 | 1,682 | 0,363 | 0,007 | 1523 | 3 | 0,001 | 0,001 | 0,031 | 0,008 | 0,002 | 0,000 |
| Camiones<br>Pesados<br>Diesel Tipo 3 | Pavimentada | Proyecto -<br>Relleno<br>sanitario | 0,154 | 0,154 | 6,719 | 1,682 | 0,363 | 0,007 | 716 | 3 | 0,000 | 0,000 | 0,014 | 0,004 | 0,001 | 0,000 |
| Camiones<br>Pesados<br>Diesel Tipo 3 | Pavimentada | Proyecto -<br>Hidronor | 0,154 | 0,154 | 6,719 | 1,682 | 0,363 | 0,007 | 3302 | 3 | 0,002 | 0,002 | 0,067 | 0,017 | 0,004 | 0,000 |
| Camiones<br>Pesados<br>Diesel Tipo 3 | Sin<br>pavimentar | Ruta S/R<br>(acceso a<br>Proyecto) | 0,230 | 0,230 | 8,739 | 2,492 | 0,559 | 0,010 | 666 | 3 | 0,000 | 0,000 | 0,017 | 0,005 | 0,001 | 0,000 |
| Camiones<br>Pesados<br>Diesel Tipo 3 | Sin<br>pavimentar | Acceso a<br>relleno<br>sanitario | 0,230 | 0,230 | 8,739 | 2,492 | 0,559 | 0,010 | 19 | 3 | 0,000 | 0,000 | 0,001 | 0,000 | 0,000 | 0,000 |
| Camiones<br>Pesados<br>Diesel Tipo 3 | Sin<br>pavimentar | Interior<br>Proyecto | 0,230 | 0,230 | 8,739 | 2,492 | 0,559 | 0,010 | 577 | 3 | 0,000 | 0,000 | 0,015 | 0,004 | 0,001 | 0,000 |
| <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | **0,005** | **0,005** | **0,183** | **0,048** | **0,011** | **0,000** |

**Tabla 3-54.: Emisiones totales en fase de construcción****

| 11 | Emisión (t) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **11** | **MPS** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2 ** |
| Nivelación | 0,09 | 0,03 | 0,00 | - | - | - | - |
| Excavaciones | 0,25 | 0,05 | 0,03 | - | - | - | - |
| Transferencia de<br>material | 0,01 | 0,00 | 0,00 | - | - | - | - |
| Tránsito de<br>vehículos pesados<br>por caminos no<br>pavimentados | 12,84 | 3,67 | 0,37 | - | - | - | - |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | 0,54 | 0,10 | 0,02 | - | - | - | - |
| Combustión de<br>motores de<br>vehículos | 0,03 | 0,03 | 0,03 | 0,99 | 0,27 | 0,06 | 0,00 |
| Maquinaria | 0,19 | 0,19 | 0,18 | 1,20 | 1,29 | 0,10 | 0,01 |
| Generadores | 0,01 | 0,01 | 0,01 | 0,17 | 0,09 | 0,01 | 0,00 |
| **TOTAL** | **13,94** | **4,07** | **0,64** | **2,35** | **1,64** | **0,18** | **0,01** |

**Tabla 3-55.: Emisiones totales en fase de operación****

| Actividad | Emisión (t) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **MPS** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2 ** |
| Tránsito de<br>vehículos pesados<br>por caminos no<br>pavimentados | 1,96 | 0,56 | 0,06 | - | - | - | - |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | 0,03 | 0,01 | 0,00 | - | - | - | - |
| Combustión de<br>motores de<br>vehículos | 0,00 | 0,00 | 0,00 | 0,04 | 0,01 | 0,00 | 0,00 |
| Maquinaria | 0,02 | 0,02 | 0,02 | 0,35 | 0,11 | 0,03 | 0,00 |
| **TOTAL** | **2,02** | **0,59** | **0,08** | **0,39** | **0,12** | **0,03** | **0,00** |

**Tabla 3-56.: Emisiones totales en fase de cierre****

| Actividad | Emisión (t) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **MPS** | **MP10** | **MP2,5** | **NOx** | **CO** | **HC** | **SO2 ** |
| Tránsito de<br>vehículos pesados<br>por caminos no<br>pavimentados | 1,84 | 0,53 | 0,05 | - | - | - | - |
| Tránsito de<br>vehículos por<br>caminos<br>pavimentados | 0,09 | 0,02 | 0,00 | - | - | - | - |
| Combustión de<br>motores de<br>vehículos | 0,00 | 0,00 | 0,00 | 0,18 | 0,05 | 0,01 | 0,00 |
| Generadores | 0,00 | 0,00 | 0,00 | 0,10 | 0,05 | 0,01 | 0,00 |
| **TOTAL** | **1,93** | **0,55** | **0,07** | **0,28** | **0,10** | **0,02** | **0,00** |

**Tabla 4-1.: Factor de corrección para concentraciones de SCREEN3****

| Periodo | Factor de Corrección |
| --- | --- |
| 24 horas | 0,4 |
| Anual | 0,08 |

**Tabla 4-2.: Características y emisiones de la fuente emisora Parque Fotovoltaico y caminos internos****

| Características de la fuente | Col2 | Col3 |
| --- | --- | --- |
| Ancho | 340 | m |
| Largo | 670 | m |
| Superficie | 227800 | m2 |
| **Fase de construcción** | **Fase de construcción** | **Fase de construcción** |
| Duración fase | 6 | meses |
| Emisión MP10 | 1,87 | t |
| Emisión MP2,5 | 0,38 | t |
| **Fase de operación** | **Fase de operación** | **Fase de operación** |
| Duración fase en Año 1 | 6 | meses |
| Emisión MP10 | 0,28 | t |
| Emisión MP2,5 | 0,06 | t |
| **Total Año 1** | **Total Año 1** | **Total Año 1** |
| Duración Año 1 | 12 | meses/año |
| Duración Año 1 | 24 | d/mes |
| Duración Año 1 | 8 | h/d |
| Duración Año 1 | 2304 | h/año |
| Emisión MP10 | 2,1 | t/año |
| Emisión MP10 | 0,26 | g/s |
| Emisión MP10 | **1,14E-06** | g/s/m2 |

**Tabla 4-3.: Características y emisiones de la fuente emisora Ruta S/R****

| Duración fase | 6 | meses |
| --- | --- | --- |
| Emisión MP10 en long total | 1,64 | t |
| Emisión MP2,5 en long total | 0,17 | t |
| Longitud total | 3000 | m |
| Emisión MP10 en tramo | 0,71 | t |
| Emisión MP2,5 en tramo | 0,07 | t |

**Tabla 4-4.: Receptores en área de influencia de la Planta Fotovoltaica****

| Punto | Descripción | Coordenadas UTM | Col4 |
| --- | --- | --- | --- |
| **Punto** | **Descripción** | **Datum WGS 84 Huso 19H** | **Datum WGS 84 Huso 19H** |
| **Punto** | **Descripción** | **Este** | **Norte** |
| 1 | Vivienda de 2 pisos ubicada a un costado de Ruta 172,<br>parcela 18. Sector Parronal. | 714.075 | 5.824.604 |
| 2 | Vivienda de 1 piso ubicada a un costado de Ruta 172,<br>parcela 17, lote 3. Sector Parronal. | 713.861 | 5.824.572 |
| 3 | Vivienda de 1 piso ubicada a un costado de Ruta 172.<br>Sector Parronal. | 713.675 | 5.824.556 |
| 4 | Vivienda de 1 piso ubicada a un costado de Ruta 172,<br>parcela 17, lote 1. Sector Parronal. | 713.668 | 5.824.628 |
| 5 | Vivienda de 1 piso ubicada a un costado de Ruta 172.<br>Sector Parronal. | 713.391 | 5.823.995 |
| 6 | Vivienda de 1 piso ubicada a un costado de Ruta 172.<br>Sector Parronal. | 713.338 | 5.824.262 |

**Tabla 4-6.: Resultados de modelación de MP10****

| Receptor | Aporte del Proyecto MP10 (μg/m3) | Col3 | Aporte del Proyecto MP2,5 (μg/m3) | Col5 |
| --- | --- | --- | --- | --- |
| **Receptor** | **Max 24h** | **Anual** | **Max 24h** | **Anual** |
| 1 | 1,8 | 0,4 | 0,4 | 0,1 |
| 2 | 2,0 | 0,4 | 0,4 | 0,1 |
| 3 | 1,4 | 0,3 | 0,3 | 0,1 |
| 4 | 1,2 | 0,2 | 0,2 | 0,0 |
| 5 | 1,1 | 0,2 | 0,2 | 0,0 |
| 6 | 1,0 | 0,2 | 0,2 | 0,0 |
| **Norma primaria** | **150** | **50** | **50** | **20** |
