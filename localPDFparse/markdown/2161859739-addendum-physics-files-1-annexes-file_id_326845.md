---
title: Sin título
author: SGA
date: D:20241015090434-03'00'
language: es
type: report
pages: 77
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MODELACIÓN DE EMISIONES ATMOSFÉRICAS
-->

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

# MODELACIÓN DE EMISIONES ATMOSFÉRICAS

## Octubre, 2024

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**ÍNDICE**

**1** **INTRODUCCIÓN .......................................................................................................................... 1**
**2** **RESUMEN DE ESTIMACIÓN DE EMISIONES ................................................................................. 3**
**3** **MODELACIÓN DE DISPERSIÓN DE CONTAMINANTES ................................................................. 7**

3.1 MARCO LEGAL .................................................................................................................... 7
3.2 LÍNEA DE BASE .................................................................................................................... 7
3.3 ANÁLISIS METEOROLÓGICO .............................................................................................. 12

3.3.1 Temperatura ................................................................................................................... 14
3.3.2 Humedad Relativa ........................................................................................................... 15

3.3.3 Velocidad y Dirección del Viento ..................................................................................... 16

3.4 BASE TEÓRICA DEL MODELO UTILIZADO ........................................................................... 18
3.5 ANÁLISIS DE INCERTIDUMBRE ........................................................................................... 20

3.5.1 Series Temporales ........................................................................................................... 20
3.5.2 Ciclos diarios ................................................................................................................... 23

3.5.3 Ciclos estacionales ........................................................................................................... 26

3.5.4 Rosas de Viento ............................................................................................................... 28

3.5.5 Ciclo diario de Temperatura (°C) ...................................................................................... 31
3.5.6 Ciclo estacional de Temperatura (°C) ............................................................................... 32

3.6 ANÁLISIS DE INCERTIDUMBRE EVALUACIÓN CUANTITATIVA DE LA MODELACIÓN
METEOROLÓGICA ............................................................................................................. 33
3.7 CONSTRUCCIÓN DE ESCENARIOS ...................................................................................... 35

_3.7.1_ Escenario de Emisiones ................................................................................................... 35

3.7.2 Escenario de Receptores ................................................................................................. 38
3.7.3 Escenario Meteorológico ................................................................................................. 39

3.7.4 Escenario Geofísico ......................................................................................................... 42

3.7.5 Escenario Uso de Suelo .................................................................................................... 43

3.7.6 Campos de Viento del Modelo Meteorlógico ................................................................... 44

3.8 RESULTADOS DE LA IMPLEMENTACIÓN DEL MODELO ....................................................... 49
3.9 ANÁLISIS DE CUMPLIMIENTO NORMATIVO VIGENTE DE CALIDAD DEL AIRE ...................... 49
3.10 ANÁLISIS DE IMPACTO SIGNIFICATIVO EN ZONA SATURADA ............................................. 55
3.11 ÁREA DE INFLUENCIA ........................................................................................................ 56

3.12 RESUMEN DE RESULTADOS Y CONCLUSIONES ................................................................... 59

3.13 ISOCONCENTRACIONES RESULTANTES .............................................................................. 60

**ÍNDICE DE TABLAS**

Tabla 1.Cronograma del Proyecto ....................................................................................................... 4
Tabla 2.Resumen Estimación de Emisiones ......................................................................................... 6

Tabla 3. Normas de Calidad del Aire Consideradas en el Estudio. ........................................................ 7

Tabla 4. Coordenadas de la Estación. .................................................................................................. 8

Tabla 5. Información de Datos Válidos. ............................................................................................... 8

Modelación de Emisiones Atmosféricas **i**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

Tabla 6. Resumen Línea de Base de Calidad del Aire. ......................................................................... 12

Tabla 7. Información Estación Meteorológica Mirasol. ...................................................................... 12
Tabla 8. Resumen de estadísticos para Temperatura (°C) .................................................................. 14
Tabla 9. Resumen de estadísticos para Humedad Relativa (%) ........................................................... 15
Tabla 10. Resumen de estadísticos para Velocidad del Viento (m/s) .................................................. 16
Tabla 11. Sesgo, Error Cuadrático Medio, y Coeficiente de Correlación Velocidad del Viento - Datos

Observados vs Modelo WRF 2021 ................................................................................... 34

Tabla 12. Tasa de Emisión Consideradas............................................................................................ 36

Tabla 13. Coordenadas de los receptores Primarios .......................................................................... 38

Tabla 14 Detalle Archivo WRF ........................................................................................................... 39

Tabla 15 Características del Suelo ..................................................................................................... 44
Tabla 16. Aporte del Proyecto Material Particulado Respirable μg/m [3] N (MP10 y MP2,5) .................. 50
Tabla 17. Aporte del Proyecto Dióxido de Nitrógeno μg/m [3] N (NO2) .................................................. 50
Tabla 18. Aporte del Proyecto Monóxido de Carbono μg/m [3] N (CO) ................................................... 51
Tabla 19. Aporte del Proyecto Dióxido de Azufre μg/m [3] N (SO2), Norma Primaria .............................. 51
Tabla 20. Aporte del Proyecto Dióxido de Azufre μg/m [3] N (SO2), Norma Secundaria .......................... 52
Tabla 21. Aporte del Proyecto Material Particulado Sedimentable mg/m [2] -día (MPS), Norma Secundaria

....................................................................................................................................... 52

Tabla 22. Análisis Normativo MP2,5 .................................................................................................. 53
Tabla 23. Coordenadas de los Puntos de Máximo Impacto (PMI) ....................................................... 54
Tabla 24. Aportes del proyecto y Nivel de Significancia MP2,5 Media Anual ...................................... 55
Tabla 25. Aportes del proyecto y Nivel de Significancia MP2,5 24 Horas ............................................ 55

**ÍNDICE DE FIGURAS**

Figura 1 Ubicación del Proyecto .......................................................................................................... 2
Figura 2 Ubicación de la Estación de Calidad del Aire .......................................................................... 9
Figura 3. Serie de Tiempo MP2,5, estación Mirasol. .......................................................................... 10
Figura 4. Serie de Tiempo MP2,5, estación Alerce. ............................................................................ 10
Figura 5. Promedios Mensuales de MP2,5 Estación Mirasol. ............................................................. 11
Figura 6. Promedios Mensuales de MP2,5 Alerce. ............................................................................. 11
Figura 7. Ubicación de Estación Meteorológica. ................................................................................ 13
Figura 8. Ciclo diario de temperatura (°C). ......................................................................................... 14
Figura 9. Ciclo diario de humedad relativa (%). .................................................................................. 15
Figura 10. Ciclo diario de velocidad del viento (m/s) .......................................................................... 16
Figura 11. Rosas de Viento según período ......................................................................................... 17
Figura 12. Representación Gráfica del Modelo Tipo Puff y de Pluma. ................................................ 19
Figura 13. Serie temporal para registros horarios de velocidad del viento observada y modelada para la

Estación Mirasol ............................................................................................................. 21

Figura 14. Serie temporal para registros horarios de velocidad del viento observada y modelada para la

Estación Mirasol, Año 2023 ............................................................................................. 22
Figura 15. Ciclos diarios de velocidad del viento observada y modelada, estación Mirasol Año 2023 . 24
Figura 16. Ciclos diarios de dirección del viento observada y modelada, Mirasol, Año 2023 .............. 25
Figura 17. Ciclo Estacional del Viento observado y modelado para Mirasol, Año 2023 ....................... 27
Figura 18. Rosas de viento observada, Estación Mirasol, Año 2023.................................................... 29

Modelación de Emisiones Atmosféricas **ii**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

Figura 19. Rosas de viento modelada, Estación Mirasol, Año 2023 .................................................... 30
Figura 20. Ciclos diarios de temperatura observada y modelada, estación El Mirasol, Año 2023 ........ 31
Figura 21. Ciclo estacional de la temperatura observado y modelado, Estación El Mirasol, Año 2023 32
Figura 22. Fuentes de emisión consideradas ..................................................................................... 37
Figura 23. Ubicación de Receptores Norma Primaria ......................................................................... 40
Figura 24. Dominio de Modelación .................................................................................................... 41
Figura 25. Topografía de la Zona. ...................................................................................................... 42
Figura 26. Uso de Suelo de la Zona. ................................................................................................... 43
Figura 27. Campo de viento día invierno ........................................................................................... 45
Figura 28. Campo de viento noche invierno....................................................................................... 46
Figura 29. Campo de viento día verano ............................................................................................. 47
Figura 30. Campo de viento noche verano ........................................................................................ 48
Figura 31. Área de Influencia de la Componente Calidad del Aire Receptores Primarios .................... 57
Figura 32. Área de Influencia de la Componente Calidad del Aire Receptores Secundarios ................ 58
Figura 33. Isoconcentración Promedio Anual MP10........................................................................... 61
Figura 34. Isoconcentración Percentil 98 24 Horas MP10. ................................................................. 62
Figura 35. Isoconcentración Promedio Anual MP2,5.......................................................................... 63
Figura 36. Isoconcentración Percentil 98 24 Horas MP2,5 ................................................................. 64
Figura 37. Isoconcentración Promedio Anual NO2. ............................................................................ 65
Figura 38. Isoconcentración Percentil 99 24 Horas NO2..................................................................... 66
Figura 39. Isoconcentración Percentil 99 1 Hora NO2. ....................................................................... 67
Figura 40. Isoconcentración Promedio Anual SO2. ............................................................................ 68
Figura 41. Isoconcentración Percentil 99 24 Horas SO2. .................................................................... 69
Figura 42. Isoconcentración Percentil 99 1 Hora SO2. ........................................................................ 70
Figura 43. Isoconcentración Percentil 99 1 Hora CO. ......................................................................... 71
Figura 44. Isoconcentración Percentil 99 8 Horas CO. ........................................................................ 72
Figura 45. Idepositación Promedio Anual MPS. ................................................................................. 73

Modelación de Emisiones Atmosféricas **iii**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**1** **INTRODUCCIÓN**

En este anexo se presenta la modelación de emisiones atmosféricas de los contaminantes: material
particulado respirable (MP10), material particulado fino (MP2.5) material particulado sedimentable
(MPS) y gases de combustión (NO x, CO y SO 2 ) para el Proyecto “Inmobiliario Puerta Norte”, en adelante
el “Proyecto”.

El Proyecto Inmobiliario “Puerta Norte”, se desarrollará en la comuna de Puerto Montt, provincia de
Llanquihue, región de Los Lagos.

Para el efecto, se dispone de un predio de 33,56 has, donde se proyecta la construcción de 1.619
viviendas distribuidas en 703 casas, 476 townhouses y 440 departamentos. A su vez, los townhouses
podrán ser del tipo de viviendas individuales o colectivas donde se consideran 5 unidades.

A su vez, el lugar específico de localización del proyecto inmobiliario “Puerta Norte”, corresponde a un
predio que ocupa actualmente la planta astilladora de “ _Eucaliptus globulus”_ perteneciente a Forestal
Los Lagos S. A. Esta planta, se encuentra en operación desde fines de los años 80 del siglo pasado y se
emplaza en un área netamente industrial, donde operan también otras empresas forestales, acuícolas,
áridos y otros rubros. Asimismo, en parte de la zona se ubica el humedal “Ruta 5”, cuyo nombre se
deriva de su proximidad a la ruta del mismo nombre.

La superficie de las viviendas se encuentra comprendida entre 52,8 m [2] y 63,52 m [2] . No obstante, y de
acuerdo a la cronología del Proyecto presentada en la Tabla 1 y las emisiones presentadas en la Tabla
2, el período de mayor emisión de material particulado corresponde al año 6 donde se desarrollan las
obras principalmente del Edificio Castellón, representando de esta manera el escenario mas
desfavorable en cuanto a la generación de emisiones.

Por otra parte, la Región de lo Lagos, específicamente Puerto Montt se encuentra declarada como zona
saturada por material particulado respirable fino MP2,5 como concentración de 24 horas, mediante
D.S. N° 24/2020 del Ministerio del Medio Ambiente.

En la siguiente Figura 1 se presenta la ubicación del Proyecto a escala local.

Modelación de Emisiones Atmosféricas **1**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 1 Ubicación del Proyecto**

Fuente: Estudio de Emisiones Atmosféricas de la presente Adenda

Modelación de Emisiones Atmosféricas **2**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**2** **RESUMEN DE ESTIMACIÓN DE EMISIONES**

La estimación de emisiones del Proyecto se realizó aplicando los factores de emisión y fórmulas
propuestas por la Agencia de Protección Ambiental de los EE.UU. en el documento “AP-42 5th Edición.

A continuación, en la Tabla 2 se muestra el resumen de las emisiones de material particulado respirable
(MP10), fino (MP2,5), sedimentable (MPS), óxidos de nitrógeno (NOx), monóxido de carbono (CO) y
óxidos de azufre (SOx).

Es importante señalar que para evaluar el impacto de las emisiones se ha el año de mayor emisión de
material particulado MP10 que corresponde al año 6 donde se desarrolla parte de la Fase de
Construcción y Operación.

Las emisiones mencionadas fueron presentadas en detalle en Actualización Estimación de Emisiones
Atmosféricas de la presente Adenda.

Modelación de Emisiones Atmosféricas **3**

**Tabla 1.Cronograma del Proyecto**

|Etapa|Actividad|1|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|2|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|3|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|Col38|4|Col40|Col41|Col42|Col43|Col44|Col45|Col46|Col47|Col48|Col49|Col50|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Etapa**|**Actividad**|**1 **|**2 **|**3 **|**4 **|**5 **|**6 **|**7 **|**8 **|**9 **|**10**|**11**|**12**|**13**|**14**|**15**|**16**|**17**|**18**|**19**|**20**|**21**|**22**|**23**|**24**|**25**|**26**|**27**|**28**|**29**|**30**|**31**|**32**|**33**|**34**|**35**|**36**|**37**|**38**|**39**|**40**|**41**|**42**|**43**|**44**|**45**|**46**|**47**|**48**|
|**ETAPA 1**|Instalación de<br>Faenas|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 1**|Movimientos de<br>tierra|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 1**|ALC-AP-ALL|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 1**|Pavimentación|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 1**|Construcción de<br>viviendas|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 1**|Áreas verdes|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 1**|Electricidad|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 1**|Levantamiento de<br>faenas|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 1**|Entrega a clientes|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 2**|Instalación de<br>faenas|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 2**|Movimientos de<br>tierra|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 2**|ALC-AP-ALL|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 2**|Pavimentación|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 2**|Construcción de<br>viviendas|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 2**|Áreas verdes|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 2**|Electricidad|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 2**|Levantamiento de<br>faenas|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 2**|Entrega a clientes|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 3**|Instalación de<br>faenas|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 3**|Movimientos de<br>tierra|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 3**|ALC-AP-ALL|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 3**|Pavimentación|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 3**|Construcción de<br>viviendas|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 3**|Áreas verdes|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 3**|Electricidad|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 3**|Levantamiento de<br>faenas|||||||||||||||||||||||||||||||||||||||||||||||||
|**ETAPA 3**|Entrega a clientes|||||||||||||||||||||||||||||||||||||||||||||||||

|Etapa|Actividad|3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|4|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|5|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|Col38|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Etapa**|**Actividad**|**25**|**26**|**27**|**28**|**29**|**30**|**31**|**32**|**33**|**34**|**35**|**36**|**37**|**38**|**39**|**40**|**41**|**42**|**43**|**44**|**45**|**46**|**47**|**48**|**49**|**50**|**51**|**52**|**53**|**54**|**55**|**56**|**57**|**58**|**59**|**60**|
|**ETAPA 4**|Instalación de Faenas|||||||||||||||||||||||||||||||||||||
|**ETAPA 4**|Movimientos de tierra|||||||||||||||||||||||||||||||||||||
|**ETAPA 4**|ALC-AP-ALL|||||||||||||||||||||||||||||||||||||

Modelación de Emisiones Atmosféricas **4**

|Etapa|Actividad|3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|4|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|5|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|Col38|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Etapa**|**Actividad**|**25**<br>|**26**<br>|**27**<br>|**28**<br>|**29**<br>|**30**<br>|**31**|**32**|**33**|**34**|**35**|**36**<br>|**37**<br>|**38**<br>|**39**<br>|**40**<br>|**41**<br>|**42**<br>|**43**<br>|**44**<br>|**45**<br>|**46**<br>|**47**<br>|**48**<br>|**49**<br>|**50**<br>|**51**<br>|**52**<br>|**53**<br>|**54**<br>|**55**<br>|**56**<br>|**57**<br>|**58**<br>|**59**<br>|**60**<br>|
|**Etapa**|Pavimentación|Pavimentación|Pavimentación|Pavimentación|Pavimentación|Pavimentación|Pavimentación|||||||||||||||||||||||||||||||
|**Etapa**|Construcción de viviendas|||||||||||||||||||||||||||||||||||||
|**Etapa**|Áreas verdes|||||||||||||||||||||||||||||||||||||
|**Etapa**|Electricidad|||||||||||||||||||||||||||||||||||||
|**Etapa**|Levantamiento de faenas|||||||||||||||||||||||||||||||||||||
|**Etapa**|Entrega a clientes|||||||||||||||||||||||||||||||||||||
|**ETAPA 5**|Instalación de Faenas|||||||||||||||||||||||||||||||||||||
|**ETAPA 5**|Movimientos de tierra|||||||||||||||||||||||||||||||||||||
|**ETAPA 5**|ALC-AP-ALL|||||||||||||||||||||||||||||||||||||
|**ETAPA 5**|Pavimentación|||||||||||||||||||||||||||||||||||||
|**ETAPA 5**|Construcción de viviendas|||||||||||||||||||||||||||||||||||||
|**ETAPA 5**|Áreas verdes|||||||||||||||||||||||||||||||||||||
|**ETAPA 5**|Electricidad|||||||||||||||||||||||||||||||||||||
|**ETAPA 5**|Levantamiento de faenas|||||||||||||||||||||||||||||||||||||
|**ETAPA 5**|Entrega a clientes|||||||||||||||||||||||||||||||||||||

|Etapa|Actividad|5|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|6|Col16|Col17|Col18|Col19|Col20|Col21|Col22|Col23|Col24|Col25|Col26|7|Col28|Col29|Col30|Col31|Col32|Col33|Col34|Col35|Col36|Col37|Col38|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Etapa**|**Actividad**|**49**|**50**|**51**|**52**|**53**|**54**|**55**|**56**|**57**|**58**|**59**|**60**|**61**|**62**|**63**|**64**|**65**|**66**|**67**|**68**|**69**|**70**|**71**|**72**|**73**|**74**|**75**|**76**|**77**|**78**|**79**|**80**|**81**|**82**|**83**|**84**|
|**ETAPA 6**|Instalación de Faenas|||||||||||||||||||||||||||||||||||||
|**ETAPA 6**|Movimientos de tierra|||||||||||||||||||||||||||||||||||||
|**ETAPA 6**|ALC-AP-ALL|||||||||||||||||||||||||||||||||||||
|**ETAPA 6**|Pavimentación|||||||||||||||||||||||||||||||||||||
|**ETAPA 6**|Construcción de viviendas|||||||||||||||||||||||||||||||||||||
|**ETAPA 6**|Áreas verdes|||||||||||||||||||||||||||||||||||||
|**ETAPA 6**|Electricidad|||||||||||||||||||||||||||||||||||||
|**ETAPA 6**|Levantamiento de faenas|||||||||||||||||||||||||||||||||||||
|**ETAPA 6**|Entrega a clientes|||||||||||||||||||||||||||||||||||||
|**ETAPA 7**|Instalación de Faenas|||||||||||||||||||||||||||||||||||||
|**ETAPA 7**|Movimientos de tierra|||||||||||||||||||||||||||||||||||||
|**ETAPA 7**|ALC-AP-ALL|||||||||||||||||||||||||||||||||||||
|**ETAPA 7**|Pavimentación|||||||||||||||||||||||||||||||||||||
|**ETAPA 7**|Construcción de viviendas|||||||||||||||||||||||||||||||||||||
|**ETAPA 7**|Áreas verdes|||||||||||||||||||||||||||||||||||||
|**ETAPA 7**|Electricidad|||||||||||||||||||||||||||||||||||||
|**ETAPA 7**|Levantamiento de faenas|||||||||||||||||||||||||||||||||||||
|**ETAPA 7**|Entrega a clientes|||||||||||||||||||||||||||||||||||||

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

Fuente: Estudio de Emisiones Atmosféricas de la presente Adenda

Modelación de Emisiones Atmosféricas **5**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Tabla 2.Resumen Estimación de Emisiones**

|Fase|Período|MP10|MP2,5|MPS|CO|NOx|SOx|
|---|---|---|---|---|---|---|---|
|Construcción|Año 1|1,88|1,02|6,56|1,85|7,59|0,46|
|Construcción|Año 2|1,49|0,80|5,13|1,79|7,54|0,46|
|Construcción|Año 3|1,27|0,42|5,65|0,35|0,61|0,00|
|Construcción|Año 4|1,28|0,38|5,43|0,49|0,89|0,00|
|Construcción|Año 5|1,42|0,46|6,25|1,02|1,02|0,00|
|Construcción|Año 6|1,43|0,50|6,54|0,45|0,78|0,00|
|Construcción|Año 7|0,92|0,27|4,41|0,35|0,35|0,00|
|Operación|Año 2|0,02|0,00|0,08|0,00|0,00|0,00|
|Operación|Año 3|0,21|0,05|1,09|0,00|0,00|0,05|
|Operación|Año 4|0,43|0,11|2,22|0,00|0,01|0,00|
|Operación|Año 5|0,69|0,17|3,54|0,00|0,00|0,01|
|Operación|Año 6|0,90|0,23|4,67|0,01|0,00|0,00|
|Operación|Año 7|1,15|0,29|5,93|0,06|0,00|0,00|
|Operación|Año 8|1,27|0,32|6,56|0,00|0,01|0,00|
|**Resumen **|**Resumen **|**Resumen **|**Resumen **|**Resumen **|**Resumen **|**Resumen **|**Resumen **|
|**Construcción **|**Año 1**|1,88|1,02|6,56|1,85|7,59|0,46|
|**Construcción +Operación **|**Año 2**|1,51|0,80|5,22|1,79|7,55|0,46|
|**Construcción +Operación **|**Año 3**|1,48|0,48|6,73|0,35|0,61|0,05|
|**Construcción +Operación **|**Año 4**|1,71|0,49|7,65|0,49|0,90|0,00|
|**Construcción +Operación **|**Año 5**|2,10|0,64|9,79|1,03|1,03|0,02|
|**Construcción +Operación **|**Año 6**|2,33|0,73|11,20|0,45|0,78|0,00|
|**Construcción +Operación **|**Año 7**|2,06|0,56|10,34|0,41|0,35|0,00|
|**Operación **|**Año 8**|1,29|0,32|6,64|0,00|0,01|0,00|

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **6**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3** **MODELACIÓN DE DISPERSIÓN DE CONTAMINANTES**

**3.1** **Marco Legal**

La siguiente modelación determinará el efecto en las cercanías del Proyecto, producto de las emisiones
de Material Particulado Respirable (MP10), Fino (MP2,5), material particulado sedimentable (MPS) y
los gases CO, NO 2 y SO 2, generados por las actividades asociadas al año 6.

En el contexto legal, existen normas primarias y secundarias asociadas a los contaminantes de las
emisiones atmosféricas generadas en el Proyecto. Los estadísticos a evaluar se presentan en la Tabla

3.

**Tabla 3. Normas de Calidad del Aire Consideradas en el Estudio.**

|Parámetro|Norma|Estadístico|Valor límite|Referencia|
|---|---|---|---|---|
|MP10|Primaria|Promedio Anual1|50g/m3N|D.S. N° 12/22 MMA|
|MP10|Primaria|Percentil 98 promedio diario|130g/m3N|130g/m3N|
|MP2,5|Primaria|Promedio Anual1|20g/m3N|D.S. N° 12/2011 del MMA|
|MP2,5|Primaria|Percentil 98 promedio diario|50g/m3N|50g/m3N|
|NO2|Primaria|Promedio Anual1|40g/m3N|D.S. N° 40/2023 del MMA|
|NO2|Primaria|Percentil 99 promedio diario|100g/m3N|100g/m3N|
|NO2|Primaria|Percentil 99 máx. 1 hora1|200g/m3N|200g/m3N|
|CO|Primaria|Percentil 99 1 hora1|30 mg/m3N|D.S. N° 115/2002 del<br>MINSEGPRES|
|CO|Primaria|Percentil 99 8 hora1|10 mg/m3N|10 mg/m3N|
|SO2|Primaria|Promedio Anual1|60 μg/m3N|D.S. N° 104/2018 del MMA|
|SO2|Primaria|Percentil 99 24 horas1|150 μg/m3N|150 μg/m3N|
|SO2|Primaria|Percentil 99 1 hora1|350 μg/m3N|350 μg/m3N|
|SO2|Secundaria|Promedio Anual|60 μg/m3N|D.S. N° 22/2010 del<br>MINSEGPRES|
|SO2|Secundaria|Percentil 99,7 diario|260 μg/m3N|260 μg/m3N|
|SO2|Secundaria|Percentil 99,73 1 hora|700 μg/m3N|700 μg/m3N|
|MPS|Secundaria|Promedio Anual|200 mg/m2-día|Ordenanza de la<br>Confederación Suiza|

Fuente: Elaboración propia

**3.2** **Línea de Base**

Para establecer la línea de base de calidad del aire del Proyecto, se deben considerar datos de
estaciones de calidad aire cercanas y situadas en una zona que sea representativa respecto a la
ubicación del Proyecto. Se realizó una recopilación de la información pública en especial del Sistema
de Información Nacional de Calidad del Aire, por lo que la estación más cercana se ubica a 2,6 km al
sureste (SE) del Proyecto, siendo representativa del lugar donde se sitúa el Proyecto y para lo cual se

1 Aplicable al promedio anual de tres años consecutivos.

Modelación de Emisiones Atmosféricas **7**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

ha considerado un período de datos de los años 2021-2022-2023. Además, se consideró la estación
Alerce ubicada a 8,8 km al noreste.

Los contaminantes que miden las estaciones y las coordenadas se presentan en la siguiente Tabla.

Es importante señalar que los registros para los contaminantes NO 2, CO y SO 2, corresponden a datos
preliminares, por lo cual deben ser considerados de manera referencial, mientras que los registros de
MP10 y MP2,5 tienen la categoría de validados.

**Tabla 4. Coordenadas de la Estación.**

|Estación|Período|Coordenadas Datum WGS 84<br>Huso 18H|Col4|Contaminante|Operador y Propietario|
|---|---|---|---|---|---|
|**Estación**|**Período**|**Este**|**Norte**|**Norte**|**Norte**|
|Mirasol|2021-2023|669.585|5.406.017|MP2,5|Ministerio del Medio<br>Ambiente|
|Alerce|2021-2023|675.585|5.414.803|MP2,5|Sub Secretaría del Medio<br>Ambiente|

Fuente: Elaboración propia

**Tabla 5. Información de Datos Válidos.**

|Estación|2021|Col3|2022|Col5|2023|Col7|
|---|---|---|---|---|---|---|
|**Estación**|**Datos válidos/**<br>**preliminares**|**% **|**Datos válidos/**<br>**preliminares**|**% **|**Datos válidos/**<br>**preliminares**|**% **|
|Mirasol|8.539|97%|8.460|97%|8.412|96%|
|Alerce|8.470|97%|8.501|97%|8.438|96%|

Fuente: Elaboración propia

Por otra parte, en la siguiente Figura se presenta la ubicación de las Estación Mirasol y Alerce.

Modelación de Emisiones Atmosféricas **8**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 2 Ubicación de la Estación de Calidad del Aire**

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **9**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

En las siguientes Figuras se presentan la serie de tiempo para el período completo 2021-2022-2023,
posteriormente se muestran los promedios mensuales para cada contaminante.

**Figura 3. Serie de Tiempo MP2,5, estación Mirasol.**

Fuente: SINCA

**Figura 4. Serie de Tiempo MP2,5, estación Alerce.**

Fuente: SINCA

Modelación de Emisiones Atmosféricas **10**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 5. Promedios Mensuales de MP2,5 Estación Mirasol.**

Fuente: Elaboración propia

**Figura 6. Promedios Mensuales de MP2,5 Alerce.**

Fuente: Elaboración propia

En las figuras anteriores se observa un aumento de las concentraciones entre los meses de abril a
septiembre, alza que se asocia al uso de la leña como combustible para calefaccionar los hogares, el
año 2022 presenta los mayores registros, luego el año 2023 se observa una notable disminución.

Modelación de Emisiones Atmosféricas **11**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Tabla 6. Resumen Línea de Base de Calidad del Aire.**

|Estación|Parámetro|Estadístico|Estación Mirasol - Registro monitoreado<br>(μg/m3N)|Col5|Col6|Col7|Norma|% Norma|
|---|---|---|---|---|---|---|---|---|
|**Estación**|**Parámetro**|**Estadístico**|**Año 2021**|**Año 2022**|**Año 2023**|**Promedio**<br>**trianual**|**Promedio**<br>**trianual**|**Promedio**<br>**trianual**|
|Mirasol|MP2,5|Promedio anual|23|28|20|24|20|119%|
|Mirasol|MP2,5|Percentil 98 diario|112|141|110|141|50|282%|
|Alerce|MP2,5|Promedio anual|25|27|22|25|20|123%|
|Alerce|MP2,5|Percentil 98 diario|110|136|88|136|50|272%|

Fuente: Elaboración propia

Como se observa en la Tabla anterior que en ambas estaciones el contaminante MP2,5 se encuentra
en niveles de saturación, tanto para la norma anual como la diaria.
Por lo tanto la zona donde se ubica el Proyecto se encuentra en niveles de saturación por MP2,5 lo que
va en línea con la declaración de zona saturada establecida en el D.S. N° 24/2020 del Ministerio del

Medio Ambiente.

**3.3** **Análisis Meteorológico**

Para este análisis meteorológico se han considerado los registros de las variables, temperatura,
humedad relativa, velocidad y dirección del viento de la estación Mirasol dependiente del Ministerio
de Medio Ambiente para el período 2021-2023, siendo la estación más cercana con registros
disponibles de manera pública y que se ubica a 2,5 km al sur-este del Proyecto, como se presenta en
la siguiente Figura. Importante señalar que la temperatura sólo presenta datos para el año 2023. Por
otra parte, en la Tabla 7 se presenta la información de la estación Mirasol.

**Tabla 7. Información Estación Meteorológica Mirasol.**

|Estación|Coordenada UTM WGS84 (Huso 18)|Col3|Variables meteorológicas|Periodo|Administrada por|
|---|---|---|---|---|---|
|**Estación**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Estación Mirasol|669.585|5.406.017|Velocidad y dirección del<br>viento, temperatura y<br>humedad relativa|2021-2023|Ministerio de<br>Medio Ambiente|

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **12**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 7. Ubicación de Estación Meteorológica.**

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **13**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.3.1** **Temperatura**

En la siguiente Tabla se presentan los valores mínimos, máximos y promedios mensuales de
temperatura para el año 2023. En ella se observa que entre los meses de mayo junio y julio se
presentan temperaturas bajo los 0°C, mientras que el promedio anual llega a 10,7°C. Por otra parte,
en la Figura 8 se presenta el comportamiento del ciclo diario donde las máximas promedio se observan
alrededor de las 14: 00 horas. Es importante mencionar que para la temperatura sólo se encuentra
disponible el año 2023.

**Tabla 8. Resumen de estadísticos para Temperatura (°C)**

|Mes|2023|Col3|Col4|
|---|---|---|---|
|**Mes**|**Mínima**|**Máxima**|**Media**|
|Enero|5,6|23,6|14,1|
|Febrero|7,2|23,4|14,9|
|Marzo|3,6|23,5|12,8|
|Abril|5,4|18,6|11,4|
|Mayo|-0,6|16,9|9,6|
|Junio|-0,3|13,8|8,3|
|Julio|-1,2|15,8|8,0|
|Agosto|0,2|13,6|7,5|
|Septiembre|0,3|16,7|7,9|
|Octubre|2,3|20,7|9,6|
|Noviembre|3,2|21,6|10,8|
|Diciembre|4,4|23,3|13,5|
|**Promedio**|**2,5**|**19,3**|**10,7**|

Fuente: Elaboración propia

**Figura 8. Ciclo diario de temperatura (°C).**

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **14**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.3.2** **Humedad Relativa**

En la Tabla 9 se presentan los valores mínimos, máximos y promedios mensuales de la humedad
relativa del aire. El promedio anual para los tres períodos se encuentra entre el 73% y el 74%. Por otra
parte, en la Figura 9 se presenta el comportamiento del ciclo diario donde los promedios horarios se
mantienen sobre el 60%.

**Tabla 9. Resumen de estadísticos para Humedad Relativa (%)**

|Mes|2021|Col3|Col4|2022|Col6|Col7|2023|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Mes**|**Mínima**|**Máxima**|**Media**|**Mínima**|**Máxima**|**Media**|**Mínima**|**Máxima**|**Media**|
|Enero|37|91|69|38|90|67|36|94|70|
|Febrero|38|94|69|30|89|68|26|94|69|
|Marzo|30|94|74|38|92|74|29|93|72|
|Abril|33|93|78|50|94|79|38|96|80|
|Mayo|47|94|80|39|93|77|43|96|79|
|Junio|38|94|77|27|91|76|40|94|78|
|Julio|52|93|81|35|91|78|46|91|77|
|Agosto|46|94|78|43|94|76|32|93|75|
|Septiembre|34|93|74|39|94|74|43|94|73|
|Octubre|24|94|71|42|93|72|42|93|71|
|Noviembre|40|90|70|36|94|72|29|93|71|
|Diciembre|32|94|70|36|90|67|32|90|67|
|**Promedio**|**38**|**93**|**74**|**38**|**92**|**73**|**36**|**93**|**74**|

Fuente: Elaboración propia

**Figura 9. Ciclo diario de humedad relativa (%).**

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **15**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.3.3** **Velocidad y Dirección del Viento**

En la Tabla 10 se presentan los valores mínimos, máximos y promedios mensuales de la velocidad del
viento. En ella se observa que la máxima velocidad alcanza los 9,9 m/s en el mes de junio del año 2021,
mientras que el promedio se encuentra entre los 1,6 y 2,3 m/s. Por otra parte, en la Figura 10 se
presenta el comportamiento del ciclo diario donde se observan intensidades homogéneas durante
todo el día para los tres períodos.

**Tabla 10. Resumen de estadísticos para Velocidad del Viento (m/s)**

|Mes|2021|Col3|Col4|2022|Col6|Col7|2023|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Mes**|**Mínima**|**Máxima**|**Media**|**Mínima**|**Máxima**|**Media**|**Mínima**|**Máxima**|**Media**|
|Enero|0,1|6,2|2,9|0,0|5,7|1,0|0,1|4,8|1,8|
|Febrero|0,1|7,4|3,0|0,0|6,4|0,9|0,0|5,1|2,0|
|Marzo|0,2|7,4|2,6|0,0|7,0|0,6|0,0|6,3|1,9|
|Abril|0,0|7,2|2,4|0,0|6,1|1,6|0,0|7,0|1,5|
|Mayo|0,0|7,3|2,7|0,0|4,8|1,7|0,0|7,7|1,7|
|Junio|0,1|9,9|2,8|0,0|5,7|1,6|0,0|6,3|2,1|
|Julio|0,1|6,7|2,6|0,0|6,6|2,0|0,0|6,5|2,0|
|Agosto|0,0|7,7|2,5|0,0|5,6|1,5|0,0|7,0|2,0|
|Septiembre|0,0|7,6|1,4|0,0|6,0|1,8|0,0|5,8|2,0|
|Octubre|0,0|6,7|1,5|0,1|5,4|2,0|0,1|6,2|2,1|
|Noviembre|0,0|6,1|1,2|0,1|5,4|2,0|0,1|6,0|2,0|
|Diciembre|0,0|6,4|1,5|0,0|6,1|2,1|0,1|5,3|2,2|
|Promedio|**0,1**|**7,2**|**2,3**|**0,0 **|**5,9**|**1,6**|**0,0**|**6,2**|**1,9**|

Fuente: Elaboración propia

**Figura 10. Ciclo diario de velocidad del viento (m/s)**

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **16**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

En cuanto a la dirección del viento, se presentaron rosas de viento para los dos períodos (2021-2023)
y en el cual se observa (Figura 11) que las componentes predominantes son norte, noroeste, además
de las componentes sur-sureste y sureste. Las intensidades son bajas durante todo el año no
sobrepasando el rango de los 5,7 - 8,0 m/s. En cuanto a los períodos de calma llegan a un máximo del
24% en el año 2022.

**Figura 11. Rosas de Viento según período**

|Año 2021|Año 2022|Col3|Col4|
|---|---|---|---|
|NORTH<br>SOUTH<br>WEST<br>EAST<br>2.4%<br>4.8%<br>7.2%<br>9.6%<br>12%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 16.35%|NORTH<br>SOUTH<br>WEST<br>EAST<br>2.4%<br>4.8%<br>7.2%<br>9.6%<br>12%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 24.42%|NORTH<br>SOUTH<br>WEST<br>EAST<br>2.4%<br>4.8%<br>7.2%<br>9.6%<br>12%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 24.42%|NORTH<br>SOUTH<br>WEST<br>EAST<br>2.4%<br>4.8%<br>7.2%<br>9.6%<br>12%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 24.42%|
|**Año 2023**|**Año 2023**|**Año 2023**|**Año 2023**|
|<br>NORTH<br>SOUTH<br>WEST<br>EAST<br>3.2%<br>6.4%<br>9.6%<br>12.8%<br>16%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 8.53%|<br>NORTH<br>SOUTH<br>WEST<br>EAST<br>3.2%<br>6.4%<br>9.6%<br>12.8%<br>16%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 8.53%|<br>NORTH<br>SOUTH<br>WEST<br>EAST<br>3.2%<br>6.4%<br>9.6%<br>12.8%<br>16%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 8.53%|<br>NORTH<br>SOUTH<br>WEST<br>EAST<br>3.2%<br>6.4%<br>9.6%<br>12.8%<br>16%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 8.53%|
|<br>NORTH<br>SOUTH<br>WEST<br>EAST<br>3.2%<br>6.4%<br>9.6%<br>12.8%<br>16%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 8.53%|<br>NORTH<br>SOUTH<br>WEST<br>EAST<br>3.2%<br>6.4%<br>9.6%<br>12.8%<br>16%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 8.53%|WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 8.53%|WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 8.53%|
|||||

|Col1|NORTH<br>16%<br>12.8%<br>9.6%<br>6.4%<br>3.2%|Col3|
|---|---|---|
|WEST|SOUTH<br>EAST|SOUTH<br>EAST|
|WEST|SOUTH<br>EAST||
|WEST|SOUTH<br>EAST||
|WEST|SOUTH<br>EAST||
|WEST|SOUTH<br>EAST||
|WEST|SOUTH<br>EAST||
|WEST|SOUTH<br>EAST||

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **17**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.4** **Base Teórica del Modelo Utilizado**

El modelo utilizado para determinar el efecto que tendrán las emisiones de Material Particulado
Respirable (MP-10), Fino (MP-2,5), material particulado sedimentable (MPS) y los gases (NO x, SO x y CO)
generadas en el año 6, corresponde al sistema de modelación “WRF-CALPUFF”.

El sistema de modelación incluye tres componentes principales: WRF, CALPUFF y CALPOST, además de
una larga selección de preprocesadores diseñados para incluir en el modelo datos meteorológicos y
geofísicos.

WRF es un sistema de predicción numérico de mesoescala no hidrostático (considera los movimientos
verticales), usado con fines de pronóstico operacional y en investigación de la atmósfera. Los
principales componentes de este modelo son las fuentes externas de datos, como son los datos de
entrada y la información geográfica, el sistema de pre-procesamiento, el modelo WRF-ARW y los
sistemas de post-procesamiento.

CALPUFF es un modelo tipo “puff” Lagrangiano Gaussiano no estacionario capaz de modelar el
transporte y dispersión de contaminantes sobre la base entregada por el Servicio Evaluación Ambiental
(SEA). Los modelos tipo “puff” representan una pluma de contaminantes continuo como un número
discreto de paquetes de material contaminante. El modelo evalúa la contribución de un “puff” en la
concentración atmosférica de un receptor en un instante determinado, para luego permitir que el puff
se mueva, evolucione en tamaño, fuerza, etc., hasta la próxima itineración. Luego, la concentración
total en un receptor resultará de la sumatoria de las contribuciones de todos los “puff”. La ecuación
básica del modelo se muestra a continuación:

Donde:

C: Concentración (g/m [3] )

Q: Masa del contaminante en el “puff” (g)

σx: Coeficiente de dispersión en dirección del viento (m)

σy: Coeficiente de dispersión en dirección perpendicular al viento (m)

σz: Coeficiente de dispersión vertical (m)

da: Distancia desde el centro del “puff” hacia el receptor en el eje de la dirección del viento
(m)

dc: Distancia desde el centro del “puff” hacia el receptor en el eje perpendicular a la dirección
del viento (m)

g: Altura de la ecuación gaussiana (m)

H: Altura efectiva del “puff” (m)

h: Altura de la capa de mezcla (m)

Modelación de Emisiones Atmosféricas **18**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

A diferencia de un modelo de pluma, los modelos de tipo “puff” consideran las emisiones (de los puff)
independientes de su fuente de emisión permitiendo que los “puff” respondan a la meteorología en la
que se encuentra inmerso en cada instante. Lo anterior se representa esquemáticamente en la
siguiente Figura 12.

**Figura 12. Representación Gráfica del Modelo Tipo Puff y de Pluma.**

Fuente: Lakes Environmental.

Finalmente, CALPOST procesa las salidas de CALPUFF creando los archivos con las tabulaciones
necesarias para la evaluación de los resultados según los estadísticos establecidos en las normas de
calidad del aire.

Es importante señalar que el archivo metrológico WRF considera el año 2023, el cual considera las
ultimas actualizaciones de parametrización del Modelo, además por disponibilidad de datos asociados
a la variable temperatura, que sólo existen registros para el año 2023 en la estación Mirasol.

Modelación de Emisiones Atmosféricas **19**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.5** **Análisis de Incertidumbre**

La meteorología considerada en la siguiente sección corresponde a la registrada durante el año 2023
en la Estación Mirasol perteneciente al Ministerio de Medio Ambiente. Las coordenadas de la Estación
son: 669.585 (m) Este y 5.406.017 (m) Norte. Cabe destacar que de acuerdo a los requerimientos del
Servicio de Evaluación Ambiental (SEA) en su “Guía para el uso de modelos de calidad del aire en el
SEIA”, la estación meteorológica cumple con el porcentaje mínimo de datos válidos de las variables
medidas, el cual corresponde como mínimo a un 75% de los registros.

A continuación, se presentan series temporales, ciclos diarios, ciclos estacionales y rosas de vientos a
partir de los registros correspondientes a la estación antes mencionadas, además de lo pronosticado
por el modelo WRF (Weather Research and Forecasting), con el fin de evaluar la capacidad predictiva
del modelo. El WRF, es un modelo dinámico de mesoescala de última generación que puede ser usado
tanto para la investigación como para pronóstico operativo.

**3.5.1** **Series Temporales**

A través de series temporales se pueden identificar periodos con datos faltantes, fallas de los equipos,
valores fuera de rango (outlier) y/o tendencias de la variable analizada. La Figura 13 presenta las series
temporales de velocidad del viento, tanto observadas como las arrojadas por la modelación WRF 2021
para la estación Mirasol. En tanto, la Figura 14 presenta las series temporales de la dirección del viento
horaria observada y modelada en la misma estación monitora.

En la Figura 13 se puede apreciar la continuidad de registros para el periodo de análisis. Se observa
que los datos modelados muestran velocidades con mayor intensidad que las observadas con máximos
sobre los 10 m/s.

Con respecto a la dirección del viento, la Figura 14 muestra una similitud entre los registros observados
y modelados, con un claro predominio, en ambos casos, de las direcciones con ángulo entre los 300° y

360°.

Modelación de Emisiones Atmosféricas **20**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 13. Serie temporal para registros horarios de velocidad del viento observada y modelada**

**para la Estación Mirasol**

Fuente: Elaboración propia a partir de los datos del Modelo WRF y observados.

Modelación de Emisiones Atmosféricas **21**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 14. Serie temporal para registros horarios de velocidad del viento observada y modelada**

**para la Estación Mirasol, Año 2023**

Fuente: Elaboración propia a partir de los datos del Modelo WRF y observados.

Modelación de Emisiones Atmosféricas **22**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.5.2** **Ciclos diarios**

A continuación, en la Figura 15 se presentan los ciclos diarios promedios junto con su variabilidad en
términos de los percentiles 5 y 95, tanto de la velocidad del viento observada como modelada,
correspondientes a la estación Mirasol para el año 2023. Estos gráficos muestran tanto la variación
típica de la velocidad del viento, como su variabilidad interdiaria. En tanto, la Figura 16 muestra en
términos porcentuales la frecuencia de las direcciones del viento durante el ciclo diario completo.

En la Figura 15 se puede apreciar que los ciclos de velocidad del viento, con velocidades observadas
promedios levemente más elevadas; con una velocidad promedio máxima entre las 13:00 y 15:00
horas, aunque los datos modelados muestran mínimas variaciones durante el día.

Respecto al ciclo diario de la dirección del viento, la Figura 16 muestra que el comportamiento de los
vientos observados tiene leves variaciones, por una parte las mayores frecuencias en el día, se
observan entre 60° y 120°, mientras que en los datos modelados se presentan entre los 60° y 180°.

Modelación de Emisiones Atmosféricas **23**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 15. Ciclos diarios de velocidad del viento observada y modelada, estación Mirasol Año 2023**

Fuente: Elaboración propia a partir de los datos del Modelo WRF y observados.

Modelación de Emisiones Atmosféricas **24**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 16. Ciclos diarios de dirección del viento observada y modelada, Mirasol, Año 2023**

Fuente: Elaboración propia a partir de los datos del Modelo WRF y observados.

Modelación de Emisiones Atmosféricas **25**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.5.3** **Ciclos estacionales**

En la Figura 17, se presenta la variación estacional de los ciclos diarios-anuales de las velocidades y
direcciones del viento, tanto observadas como modeladas, para la estación Mirasol en el Año 2021.
Los colores representan las distintas intensidades de la velocidad del viento durante el ciclo estacional,
mientras que la dirección del viento está representada por las flechas sobrepuestas que indican la
componente predominante.

En la Figura 17 se puede apreciar que los ciclos estacionales del viento observados muestran vientos
de mayor intensidad entre las 11:00 y las 18:00 horas, mientras que el modelado muestra una
constante de vientos mayores especialmente entre los meses de abril y septiembre.

Con respecto a la dirección del viento, las componentes predominantes durante el ciclo diario y
durante los distintos meses del año, están en concordancia con lo indicado en el análisis de las series
temporales y del ciclo diario, es decir, norte, noroeste, sur-sureste y sureste.

Modelación de Emisiones Atmosféricas **26**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 17. Ciclo Estacional del Viento observado y modelado para Mirasol, Año 2023**

Fuente: Elaboración propia a partir de los datos del Modelo WRF y observados.

Modelación de Emisiones Atmosféricas **27**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.5.4** **Rosas de Viento**

A continuación, la Figura 18 y la Figura 19 muestran las rosas de viento en la estación Mirasol, en el
año 2023, tanto para el caso observado como modelado, respectivamente. En cada una de estas
figuras se representan tanto la dirección del viento promedio anual (ciclo diario completo) así como
también el promedio del ciclo diurno (8:00 a 19:00 horas) y el ciclo nocturno (20:00 a 7:00 horas).

De acuerdo con estas rosas de vientos, se puede apreciar que, para el caso de los registros observados,
se presenta una componente predominante durante el ciclo diario, vientos provenientes del noroeste
y sureste, mientras que los modelados son del norte, nor-noroeste y sur. De la misma manera, en
período nocturno.

Se debe considerar que la mayoría de las actividades asociadas al Proyecto se realizan en período
diurno, donde los datos observados y modelados correlacionan en la componente nor-noroeste.

Modelación de Emisiones Atmosféricas **28**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 18. Rosas de viento observada, Estación Mirasol, Año 2023**

|Col1|3.2%|Col3|
|---|---|---|
|WEST|SOUTH<br>EAST|SOUTH<br>EAST|
|WEST|SOUTH<br>EAST||
|WEST|SOUTH<br>EAST||
|WEST|SOUTH<br>EAST||
|WEST|SOUTH<br>EAST||
|WEST|SOUTH<br>EAST||
|WEST|SOUTH<br>EAST||

|Ciclo Diurno|Ciclo Nocturno|
|---|---|
|<br>NORTH<br>SOUTH<br>WEST<br>EAST<br>3%<br>6%<br>9%<br>12%<br>15%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 5.09%|<br>NORTH<br>SOUTH<br>WEST<br>EAST<br>3.4%<br>6.8%<br>10.2%<br>13.6%<br>17%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 11.96%|
|**Ciclo Diario Completo**|**Ciclo Diario Completo**|
|<br>NORTH<br>SOUTH<br>WEST<br>EAST<br>3.2%<br>6.4%<br>9.6%<br>12.8%<br>16%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 8.53%|<br>NORTH<br>SOUTH<br>WEST<br>EAST<br>3.2%<br>6.4%<br>9.6%<br>12.8%<br>16%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 8.53%|

Fuente: Elaboración propia a partir de los datos del Modelo WRF y observados.

Modelación de Emisiones Atmosféricas **29**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 19. Rosas de viento modelada, Estación Mirasol, Año 2023**

|Col1|NORTH<br>27%<br>21.6%<br>16.2%<br>10.8%<br>5.4%|Col3|
|---|---|---|
|WEST|SOUTH<br>EAST|SOUTH<br>EAST|
|WEST|SOUTH<br>EAST||
|WEST|SOUTH<br>EAST||
|WEST|SOUTH<br>EAST||
|WEST|SOUTH<br>EAST||
|WEST|SOUTH<br>EAST||
|WEST|SOUTH<br>EAST||

|Ciclo Diurno|Ciclo Nocturno|
|---|---|
|<br>NORTH<br>SOUTH<br>WEST<br>EAST<br>5%<br>10%<br>15%<br>20%<br>25%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 1.78%|<br>NORTH<br>SOUTH<br>WEST<br>EAST<br>5.6%<br>11.2%<br>16.8%<br>22.4%<br>28%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 1.19%|
|**Ciclo Diario Completo**|**Ciclo Diario Completo**|
|<br>NORTH<br>SOUTH<br>WEST<br>EAST<br>5.4%<br>10.8%<br>16.2%<br>21.6%<br>27%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 1.48%|<br>NORTH<br>SOUTH<br>WEST<br>EAST<br>5.4%<br>10.8%<br>16.2%<br>21.6%<br>27%<br>WIND SPEED<br>(m/s)<br> >= 11.10<br> 8.80 - 11.10<br> 5.70 - 8.80<br> 3.60 - 5.70<br> 2.10 - 3.60<br> 0.50 - 2.10<br>Calms: 1.48%|

Fuente: Elaboración propia a partir de los datos del Modelo WRF y observados.

Modelación de Emisiones Atmosféricas **30**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.5.5** **Ciclo diario de Temperatura (°C)**

En el ciclo diario de la temperatura se observa que los datos observados muestran el máximo registro
entorno a las 14:00 horas, mientras que los datos modelados lo hacen a las 15:00 horas. Respecto a
las temperaturas promedios, los datos observados son levemente mayores.

**Figura 20. Ciclos diarios de temperatura observada y modelada, estación El Mirasol, Año 2023**

Fuente: Elaboración propia a partir de los datos del Modelo WRF y observados.

Modelación de Emisiones Atmosféricas **31**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.5.6** **Ciclo estacional de Temperatura (°C)**

El ciclo estacional de la temperatura muestra temperaturas similares en la estación El Mirasol, los
máximos registros tanto en los datos observados como modelados se presentan entre las 09:00 y 19:00
horas en períodos de primavera y verano.

**Figura 21. Ciclo estacional de la temperatura observado y modelado, Estación El Mirasol, Año 2023**

Fuente: Elaboración propia a partir de los datos del Modelo WRF y observados

Modelación de Emisiones Atmosféricas **32**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.6** **Análisis de Incertidumbre Evaluación cuantitativa de la modelación meteorológica**

Para evaluar la incertidumbre de la modelación WRF-2023 se comparan las velocidades de viento y
temperatura promedio modeladas con las velocidades registradas en la estación monitora Mirasol.

El análisis cuantitativo se debe realizar calculando como mínimo las métricas estadísticas del sesgo
(error medio o BIAS), la raíz del error cuadrático medio (RMSE) y coeficiente de correlación, cuyas
ecuaciones se presentan a continuación.

Sesgo (BIAS): Este indicador representa la tendencia del modelo WRF a sobreestimar o subestimar las
condiciones reales de la variable analizada. Si el valor es negativo, el modelo subestima el valor de
éstas y viceversa. La fórmula para el cálculo del sesgo es la siguiente:

Donde:

BIAS: Sesgo

n: Tamaño de la Muestra

Si: Valor Modelado

Oi: Valor Observado

Error Cuadrático Medio (RMSE): Este valor refleja la diferencia promedio entre los valores modelados
y observados. La fórmula para el cálculo del error cuadrático medio es la siguiente:

Donde:

ECM: Error Cuadrático Medio

N: Tamaño de la Muestra

Si: Valor Modelado

Oi: Valor Observado

Coeficiente de Correlación (r): Este estadístico mide la relación lineal entre la variable modelada y la
variable observada. El resultado de este coeficiente se encuentra en el intervalo [-1, 1]. El valor 1
representa una correlación positiva perfecta entre la variable modelada y observada, mientras que el
valor -1 muestra una correlación negativa perfecta. La fórmula para el cálculo del coeficiente de
correlación (r) es la siguiente:

Modelación de Emisiones Atmosféricas **33**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

N

[1] ̅̅̅̅(Oi−Oi̅̅̅)

N [ ∑] [(][Si−Si] σ [)] S σ O

r= [1]

i=1

Donde:

r: Coeficiente de Correlación

N: Tamaño de la Muestra

M: Valor Modelado

O: Valor Observado

σ: Desviación Estándar

La Tabla 11 muestra los resultados del cálculo de estos estadísticos aplicados a la velocidad del viento
y temperatura modelada y observada en la estación Mirasol. En ella se puede ver que las variables se
encuentran dentro de lo recomendado por la Guía de Modelos 2023.

**Tabla 11. Sesgo, Error Cuadrático Medio, y Coeficiente de Correlación Velocidad del Viento - Datos**

**Observados vs Modelo WRF 2021**

|Estadístico|Velocidad del<br>Viento (m/s)|Tolerancia|Temperatura (°C)|Tolerancia|
|---|---|---|---|---|
|BIAS|1,655|+/- 2,5 m/s|-1,013|+/- 4 °C|
|RMSE|2,185|<= 3,5 m/s|2,297|<= 4,5 °C|
|Coeficiente de<br>correlación|0,7|> 0,6|0,98|> 0,8|

Fuente: Elaboración propia

Los datos de los estadísticos mostrados en la Tabla anterior se observan que tanto para la velocidad
del viento como para la temperatura se cumplen los valores medios esperables para las métricas
evaluadas.

Por el análisis realizado podemos decir que los registros del modelo WRF se asemejan medianamente
en cuanto al comportamiento de los vientos, si levemente mayores en intensidad que los datos
modelados, la dirección de los vientos se representa de buena manera en el modelo con componentes
predominantes similares en la componente nor-noroeste.

Modelación de Emisiones Atmosféricas **34**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.7** **Construcción de Escenarios**

El desarrollo del modelo involucra la construcción de un escenario meteorológico, geofísico, de
emisiones y receptores sensibles sobre el dominio de la modelación. Para elaborar los escenarios a
modelar se requiere de datos de entrada mínimos los cuales fueron recopilados y procesados desde
estaciones de monitoreo e imágenes satelitales a través de una modelación de pronóstico mediante
WRF. El detalle de los datos recopilados para la confección de cada escenario se presenta a

continuación.

- Escenario de Emisiones y Receptores

- Ubicación y características de las fuentes emisoras, incluyendo la tasa de emisión

- Ubicación de los receptores sensibles en el área de influencia del Proyecto

- Escenario Meteorológico

- Información meteorológica del Modelo de Pronostico WRF:


Temperatura ambiente

 Velocidad del viento

 Dirección del viento

- Escenario Geofísico

- Topografía del área de modelación

A continuación, se presentan los escenarios construidos para la modelación.

_**3.7.1**_ **Escenario de Emisiones**

Se ha considerado para la modelación de dispersión de contaminantes el periodo Año 6, donde se
realizan las actividades de la Fase de Construcción y Fase de Operación, siendo este período donde
se genera mayor emisión según los resultados presentados en el Anexo Actualización Estimación de

Emisiones.

La tasa de emisión y características de cada una de las fuentes consideradas del Proyecto, se han
estimado a partir del desarrollo y resultados del cálculo de emisiones indicado en la siguiente Tabla.

El detalle de los datos ingresados al modelo se encuentra en los archivos de entrada como respaldo
digital al presente documento. A continuación, en la Tabla 12 se resumen las tasas de emisión
asociadas a las obras que consideran actividades como excavaciones, transferencia de material,
tránsito de vehículos por caminos pavimentados y no pavimentados, combustión generada por la
operación de la maquinaria, combustión de la operación de vehículos y grupo electrógeno. Es
importante señalar que en el Modelo Calpuff se ha considerado la transformación química de los
contaminantes SOx y NOx mediante la opción RIVAD por lo cual las emisiones de NOX se han dividido
en NO, NO 2, HNO 3 y NO 3, mientras que el SOx en SO 2 y SO 4 .

Modelación de Emisiones Atmosféricas **35**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Tabla 12. Tasa de Emisión Consideradas.**

|Tipo de<br>Fuente|ID|Descripción|Unidad|SO2|SO4|NO|NO2|HNO3|NO3|CO|MP10|MP2,5|MPS|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|ROAD|SRC_1|Salida Puerto Montt|Kg/m/h|1,77E-07|0,00E+00|1,07E-05|0,00E+00|0,00E+00|0,00E+00|1,82E-06|1,00E-04|2,51E-05|5,17E-04|
|ROAD|SRC_2|Acceso|Kg/m/h|1,97E-07|0,00E+00|1,19E-05|0,00E+00|0,00E+00|0,00E+00|2,01E-06|1,11E-04|2,79E-05|5,73E-04|
|AREA_POLY|SRC_3|Comp1_E1|t/año-m2|0,00E+00|0,00E+00|0,00E+00|0,00E+00|0,00E+00|0,00E+00|0,00E+00|1,22E-06|5,88E-07|5,74E-06|
|AREA_POLY|SRC_6|Escarpe|t/año-m2|0,00E+00|0,00E+00|0,00E+00|0,00E+00|0,00E+00|0,00E+00|0,00E+00|2,21E-06|3,31E-07|2,21E-06|
|ROAD|SRC_7|Tramo 2|Kg/m/h|7,29E-09|0,00E+00|2,86E-06|0,00E+00|0,00E+00|0,00E+00|3,43E-07|2,68E-05|6,58E-06|1,39E-04|
|ROAD|SRC_8|Tramo 3|Kg/m/h|7,31E-09|0,00E+00|2,86E-06|0,00E+00|0,00E+00|0,00E+00|3,43E-07|2,48E-05|6,09E-06|1,29E-04|
|ROAD|SRC_9|Tramo 4|Kg/m/h|1,04E-08|0,00E+00|4,06E-06|0,00E+00|0,00E+00|0,00E+00|4,87E-07|9,40E-06|2,40E-06|4,83E-05|
|ROAD|SRC_10|Tramo 8|Kg/m/h|1,82E-08|0,00E+00|7,13E-06|0,00E+00|0,00E+00|0,00E+00|8,55E-07|1,01E-04|1,03E-05|3,28E-04|
|AREA_POLY|SRC_11|Acopio Etapa 1|t/año-m2|0,00E+00|0,00E+00|0,00E+00|0,00E+00|0,00E+00|0,00E+00|0,00E+00|2,93E-10|4,49E-11|5,85E-10|
|POINT|SRC_12|Maq1|t/año|9,72E-04|0,00E+00|2,93E-01|0,00E+00|0,00E+00|0,00E+00|2,06E-01|2,20E-02|2,20E-02|2,20E-02|
|POINT|SRC_13|Maq2|t/año|9,72E-04|0,00E+00|2,93E-01|0,00E+00|0,00E+00|0,00E+00|2,06E-01|2,20E-02|2,20E-02|2,20E-02|
|POINT|SRC_15|Caldera|t/año|8,17E-05|0,00E+00|1,37E-02|0,00E+00|0,00E+00|0,00E+00|1,15E-02|1,04E-03|1,04E-03|1,04E-03|
|ROAD|SRC_16|Tramo 9|t/año|1,70E-08|0,00E+00|6,66E-06|0,00E+00|0,00E+00|0,00E+00|7,99E-07|3,36E-06|5,76E-07|1,04E-05|

Nota: Las fuentes tipo areales y lineal-areal se ingresan al modelo con una tasa en [t/año-m [2] ] distribuida en el área de la fuente considerada. Las fuentes puntuales se ingresan en

[t/año] y las fuentes Road en [kg/m/h].

Modelación de Emisiones Atmosféricas **36**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 22. Fuentes de emisión consideradas**

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **37**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.7.2** **Escenario de Receptores**

En el entorno del Proyecto se han identificado 16 receptores poblacionales identificados por el Titular
y la componente ruido, además de las dos estaciones de calidad del aire que son Mirasol y Alerce. Cabe
señalar que los anteriores receptores forman parte de la evaluación de las normas primarias de calidad
del aire. Como receptor secundario se identifican dos sectores en el Estero Lobos

A continuación, en la Tabla 13 se presentan las coordenadas de los receptores considerados en la
modelación primarios. Además, su ubicación se presenta en la Figura 23.

**Tabla 13. Coordenadas de los receptores Primarios**

|Nombre|ID del<br>Modelo|Descripción|Coordenadas UTM (Huso 18G.<br>Datum WGS84)|Col5|
|---|---|---|---|---|
|**Nombre**|**ID del**<br>**Modelo**|**Descripción**|**Este (m)**|**Norte (m)**|
|Estación<br>Alerce|R_1|Estación calidad del aire|675.585|5.414.803|
|Estación<br>Mirasol|R_2|Estación calidad del aire|669.585|5.406.017|
|R1|R_3|Inmueble casa habitación 1 piso ubicada en calle Diamante**No**<br>4940, aprox. 300m. al poniente del límite predial del Proyecto.|668.016|5.408.915|
|R2|R_4|Inmueble casa habitación 1 piso ubicada en calle Diamante**No**<br>5020, aprox. 20m. al sur poniente del límite predial del<br>Proyecto.|668.245|5.408.698|
|R3|R_5|Inmueble casa habitación 2 pisos ubicada en pasaje Aragonita<br>No 5707, aprox. 75m. al sur poniente del límite predial del<br>Provecto.|668.257|5.408.494|
|R4|R_6|Inmueble casa habitación 2 pisos ubicada encalle Ojos de<br>Tigre N° 5734, aprox. 35m. al sur del límite predial del<br>Provecto.|668.372|5.408.463|
|RF1|R_7|Avifauna y; Anfibios|668.867|5.408.704|
|RF2|R_8|Avifauna y; Anfibios|668.970|5.409.020|

Fuente: Elaboración propia

Además, para generar los mapas de isoconcentraciones se estableció una grilla de receptores que
abarca un área de 50 x 50 km, equiespaciados cada 1 km en donde se encuentra contenida el área del
Proyecto, el área de influencia directa del mismo y toda la información de interés.

Modelación de Emisiones Atmosféricas **38**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.7.3** **Escenario Meteorológico**

El escenario meteorológico se construyó a partir de la información meteorológica generada por el
modelo _WRF_ . La Tabla 14 muestra la configuración utilizada por el modelo meteorológico. El dominio
del área corresponde a una grilla de 50 km x 50 km, teniendo origen en las coordenadas presentadas
en la siguiente Tabla 14, mientras que la Figura 24 muestra el dominio de modelación.

**Tabla 14 Detalle Archivo WRF**

|Proyección Cartográfica|Cónica conforme de Lambert (LCC)|
|---|---|
|Período|1 Enero al 31 de Diciembre 2023|
|Origen|Latitude: 41.455 S - Longitude: 72.982 W|
|Datum|NWS-84|
|Grilla|1 km|

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **39**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 23. Ubicación de Receptores Norma Primaria**

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **40**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 24. Dominio de Modelación**

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **41**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.7.4** **Escenario Geofísico**

La topografía de la zona se obtuvo de datos de elevación recopilados por satélite con una resolución
de tres arcos-segundo, lo que significa 1/1.200aba parte de un grado de latitud/longitud o bien 90
metros. A continuación, la Figura 25 presenta gráficamente la topografía del área.

**Figura 25. Topografía de la Zona.**

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **42**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.7.5** **Escenario Uso de Suelo**

En el Cuadro siguiente se presentan las características del suelo del sector en términos de la
modelación.

**Figura 26. Uso de Suelo de la Zona.**

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **43**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Tabla 15 Características del Suelo**

|Tipo de Suelo|Descripción|Rugosidad<br>superficial (m)|Albedo|Razón de Bowen|
|---|---|---|---|---|
|10|Urbanización|1,0|0,18|1,5|
|20|Suelo agrícola sin riego|0,25|0,15|1,0|
|30|Pastizal|0,05|0,25|1,0|
|40|Bosque|1,0|0,10|1,0|
|51|Pequeña masa de agua|0,001|0,1|0,0|

Fuente: Elaboración propia

**3.7.6** **Campos de Viento del Modelo Meteorlógico**

Para los campos de vientos representativos se ha considerado la estacionalidad de invierno y verano,
seleccionando para el primer caso el día 21 de junio a las 02:00 AM y a las 15:00 PM, mientras que para
la segunda se consideró el día 21 de diciembre a las 02:00 AM y a las 15:00 PM.

Modelación de Emisiones Atmosféricas **44**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 27. Campo de viento día invierno**

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **45**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 28. Campo de viento noche invierno**

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **46**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 29. Campo de viento día verano**

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **47**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 30. Campo de viento noche verano**

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **48**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.8** **Resultados de la Implementación del Modelo**

A continuación, se presentan los resultados de la implementación del modelo WRF-CALPUFF.

**3.9** **Análisis de Cumplimiento Normativo vigente de Calidad del Aire**

Utilizando el modelo de dispersión WRF-CALPUFF, se modelaron las emisiones de MP10, MP2,5, MPS
y los gases SO 2, NO 2 y CO, sobre el dominio de modelación establecido por la extensión en superficie
del archivo WRF. La resolución con tamaño de grilla de los receptores fue de 1000 x 1000 metros.

Para la aplicación de este modelo se consideró la meteorología WRF para el período entre el 1 de enero
del 2023 al 31 de diciembre de 2023. Luego, se obtuvieron las concentraciones de los contaminantes
anteriormente mencionados y estimadas para cada una de las horas del periodo evaluado.

Finalmente se aplicó el módulo CALPOST para obtener los estadísticos establecidos en las normas de
calidad del aire presentadas en este documento. A continuación, se presentan los resultados como
aporte del Proyecto en los receptores discretos evaluados.

Es importante señalar que a partir de la Tabla 16 hasta la Tabla 21 se presentan las concentraciones
como aporte. Por otra parte, entre la Figura 33 y Figura 45 se presentan las concentraciones.

Modelación de Emisiones Atmosféricas **49**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Tabla 16. Aporte del Proyecto Material Particulado Respirable μg/m** **[3]** **N (MP10 y MP2,5)**

|Receptor|MP10|Col3|Col4|Col5|Col6|Col7|MP2,5|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Anual**|**Valor**<br>**Norma**<br>**Anual D.S.**<br>**No**<br>**12/2022**|**% de la**<br>**Norma**|**P98 24**<br>**hrs**|**Valor**<br>**Norma**<br>**Diaria D.S.**<br>**N°12/2022**|**% de la**<br>**Norma**|**Anual**|**Valor Anual**<br>**Norma D.S.**<br>**No 12/2012**|**% de la**<br>**Norma**|**P98 24 hrs**|**Valor Norma**<br>**Diaria D.S.**<br>**No 12/2012**|**% de la**<br>**Norma**|
|Estación Alerce|0,00|50|0,00%|0,01|130|0,00%|0,00|20|0,00%|0,00|50|0,00%|
|Estación Mirasol|0,02|0,02|0,03%|0,09|0,09|0,07%|0,00|0,00|0,02%|0,02|0,02|0,05%|
|R1|0,02|0,02|0,03%|0,16|0,16|0,13%|0,00|0,00|0,02%|0,04|0,04|0,08%|
|R2|0,03|0,03|0,07%|0,29|0,29|0,22%|0,01|0,01|0,04%|0,08|0,08|0,15%|
|R3|0,03|0,03|0,07%|0,26|0,26|0,20%|0,01|0,01|0,04%|0,07|0,07|0,13%|
|R4|0,05|0,05|0,10%|0,43|0,43|0,33%|0,01|0,01|0,06%|0,10|0,10|0,19%|

Fuente: Elaboración propia

**Tabla 17. Aporte del Proyecto Dióxido de Nitrógeno μg/m** **[3]** **N (NO** **2** **)**

|Receptor|NO2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Anual**|**Valor Norma**<br>**Anual D.S. No**<br>**40/2023**|**% de la Norma**|**P99 24 horas**|**Valor Norma**<br>**Horaria D.S. No**<br>**40/2023**|**% de la Norma**|**P99 1 hora**|**Valor Norma**<br>**Horaria D.S. No**<br>**40/2023**|**% de la Norma**|
|Estación Alerce|0,00|40|0,00%|0,00|100|0,00%|0,03|200|0,01%|
|Estación Mirasol|0,00|0,00|0,01%|0,03|0,03|0,03%|0,34|0,34|0,17%|
|R1|0,00|0,00|0,01%|0,07|0,07|0,07%|1,08|1,08|0,54%|
|R2|0,01|0,01|0,02%|0,11|0,11|0,11%|1,79|1,79|0,90%|
|R3|0,01|0,01|0,02%|0,10|0,10|0,10%|1,59|1,59|0,79%|
|R4|0,01|0,01|0,02%|0,13|0,13|0,13%|2,35|2,35|1,17%|

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **50**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Tabla 18. Aporte del Proyecto Monóxido de Carbono μg/m** **[3]** **N (CO)**

|Receptor|CO|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|**Receptor**|**P99 8 horas**|**Valor Norma 8 hrs**<br>**D.S. No 115/2002**|**% de la Norma**|**P99 1 hora**|**Valor Norma 1 hr**<br>**D.S. No 115/2002**|**% de la Norma**|
|Estación Alerce|0,00|10000|0,00%|0,01|30000|0,00%|
|Estación Mirasol|0,02|0,02|0,00%|0,13|0,13|0,00%|
|R1|0,10|0,10|0,00%|0,72|0,72|0,00%|
|R2|0,22|0,22|0,00%|1,29|1,29|0,00%|
|R3|0,18|0,18|0,00%|1,03|1,03|0,00%|
|R4|0,27|0,27|0,00%|1,52|1,52|0,01%|

Fuente: Elaboración propia

**Tabla 19. Aporte del Proyecto Dióxido de Azufre μg/m** **[3]** **N (SO** **2** **), Norma Primaria**

|Receptor|SO2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Anual**|**Valor Norma**<br>**D.S. No**<br>**104/2018**|**% de la**<br>**Norma**|**P99 24 hrs**|**Valor Norma**<br>**D.S. No**<br>**104/2018**|**% de la**<br>**Norma**|**P99 1 hr**|**Valor Norma**<br>**D.S. No**<br>**104/2018**|**% de la**<br>**Norma**|
|Estación Alerce|6,20E-07|60|0,00%|9,50E-06|150|0,00%|1,45E-05|350|0,00%|
|Estación Mirasol|2,39E-05|2,39E-05|0,00%|1,70E-04|1,70E-04|0,00%|4,77E-04|4,77E-04|0,00%|
|R1|2,43E-05|2,43E-05|0,00%|3,22E-04|3,22E-04|0,00%|5,73E-04|5,73E-04|0,00%|
|R2|5,49E-05|5,49E-05|0,00%|6,03E-04|6,03E-04|0,00%|1,25E-03|1,25E-03|0,00%|
|R3|5,54E-05|5,54E-05|0,00%|5,53E-04|5,53E-04|0,00%|1,21E-03|1,21E-03|0,00%|
|R4|8,87E-05|8,87E-05|0,00%|8,20E-04|8,20E-04|0,00%|1,93E-03|1,93E-03|0,00%|

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **51**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Tabla 20. Aporte del Proyecto Dióxido de Azufre μg/m** **[3]** **N (SO** **2** **), Norma Secundaria**

|Receptor|SO2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Anual**|**Valor Norma**<br>**D.S. No**<br>**22/2010**|**% de la**<br>**Norma**|**P99 24 hrs**|**Valor Norma**<br>**D.S. No 22/2010**|**% de la**<br>**Norma**|**P99 1 hr**|**Valor Norma**<br>**D.S. No**<br>**22/2010**|**% de la**<br>**Norma**|
|RF1|9,55E-04|60|0,00%|4,29E-03|260|0,00%|2,49E-02|700|0,00%|
|RF2|3,75E-04|60|0,00%|1,83E-03|260|0,00%|1,13E-02|700|0,00%|

Fuente: Elaboración propia

**Tabla 21. Aporte del Proyecto Material Particulado Sedimentable mg/m** **[2]** **-día (MPS), Norma Secundaria**

|Receptor|MPS|Col3|Col4|
|---|---|---|---|
|**Receptor**|**Promedio Anual**|**Valor Norma Suiza**|**% de la Norma**|
|RF1|5,87|200|2,9%|
|RF2|1,26|200|0,6%|

Fuente: Elaboración propia

En las Tablas anteriores se puede observar que las concentraciones, no sobrepasan los valores límites permisibles para cada contaminante. En
cuanto al análisis normativo a continuación se presenta el aporte del Proyecto más la línea de base, evaluación realizada considerando los registros
de la estación Mirasol.

Modelación de Emisiones Atmosféricas **52**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Tabla 22. Análisis Normativo MP2,5**

|Receptores|Concentraciones (μg/m3N)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Receptores**|**MP2,5**|**MP2,5**|**MP2,5**|**MP2,5**|**MP2,5**|**MP2,5**|**MP2,5**|**MP2,5**|
|**Receptores**|**Promedio Anual**|**Promedio Anual**|**Promedio Anual**|**Promedio Anual**|**Percentil 98 24 Horas**|**Percentil 98 24 Horas**|**Percentil 98 24 Horas**|**Percentil 98 24 Horas**|
|**Receptores**|**Aporte**<br>**Proyecto**<br>**(AP)**|**Línea de**<br>**Base (LB)**|**AP+LB**|**% de la**<br>**Norma**<br>**(20**<br>**μg/m3N)**|**Aporte**<br>**Proyecto**<br>**(AP)**|**Línea de**<br>**Base (LB)**|**AP+LB**|**% de la**<br>**Norma**|
|**Receptores**|**Aporte**<br>**Proyecto**<br>**(AP)**|**Línea de**<br>**Base (LB)**|**AP+LB**|**% de la**<br>**Norma**<br>**(20**<br>**μg/m3N)**|**Aporte**<br>**Proyecto**<br>**(AP)**|**Línea de**<br>**Base (LB)**|**AP+LB**|**(50**<br>**μg/m3N)**|
|Estación Alerce|0,00|25|25,0|125%|0,00|136|136,0|272%|
|Estación Mirasol|0,00|24|24,0|120%|0,02|141|141,0|282%|

Fuente: Elaboración propia

En la Tabla anterior es posible observar que las condiciones basales no presentan alteración toda vez
que los aportes del Proyectos no son significativos para todos los receptores evaluados.

A continuación, se presentan las coordenadas de los puntos de máximo impacto (PMI), en ella se
observa que los PMI de material particulado respirable, se registran a 566 metros al suroeste del
Proyecto en sector de carretera al igual que el SO2, mientras que para el NO2 y el CO el punto de
máximo impacto recae en el sector del estero Lobos específicamente en el receptor RF1.

Modelación de Emisiones Atmosféricas **53**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Tabla 23. Coordenadas de los Puntos de Máximo Impacto (PMI)**

|Parámetro|Norma|Estadístico|Concentración<br>(μg/m3)|Valor Norma|Coordenadas UTM WGS 84|Col7|Identificación|
|---|---|---|---|---|---|---|---|
|**Parámetro**|**Norma**|**Estadístico**|**Concentración**<br>**(μg/m3) **|**Valor Norma**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|MP10|Primaria|Promedio Anual|5,67|50g/m3N|669.069|5.408.234|566 metros al sureste|
|MP10|Primaria|Percentil 98 promedio diario|16,83|130g/m3N|669.069|5.408.234|566 metros al sureste|
|MP2,5|Primaria|Promedio Anual|1,42|20g/m3N|669.069|5.408.234|566 metros al sureste|
|MP2,5|Primaria|Percentil 98 promedio diario|4,23|50g/m3N|669.069|5.408.234|566 metros al sureste|
|NO2|Primaria|Promedio Anual|0,06|400g/m3N|668.867|5.408.704|RF1|
|NO2|Primaria|Percentil 99 máx. 24 horas|0,26|100g/m3N|668.867|5.408.704|RF1|
|NO2|Primaria|Percentil 99 máx. 1 hora|2,92|200g/m3N|668.867|5.408.704|RF1|
|CO|Primaria|Percentil 99 8 horas|1,93|10.000g/m3N|668.867|5.408.704|RF1|
|CO|Primaria|Percentil 99 1 hora|7,27|30.000g/m3N|668.867|5.408.704|RF1|
|SO2|Primaria|Promedio Anual|0,01|60 μg/m3N|669.069|5.408.234|566 metros al sureste|
|SO2|Primaria|Percentil 99 24 horas|0,03|150 μg/m3N|669.069|5.408.234|566 metros al sureste|
|SO2|Primaria|Percentil 99 1 hora|0,10|350 μg/m3N|669.069|5.408.234|566 metros al sureste|

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **54**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.10** **Análisis de Impacto Significativo en Zona Saturada**

La Región de Los Lagos se encuentra declarada como zona latente por material particulado respirable
fino MP2,5 mediante el D.S. N° 24/2020 del Ministerio del Medio Ambiente, debido a lo anterior es que
se debe evaluar el impacto de las emisiones para determinar si los impactos son significativos.

Para evaluar si los impactos son significativos se debe comparar con los criterios de significancia
presentados en el documento “Criterio de Evaluación en el SEIA: Impacto de Emisiones en Zonas
Saturadas por Material Particulado Respirable MP10 y Material Particulado Respirable Fino MP2,5
(2023)”. Según el documento de referencia y de acuerdo a los resultados de las emisiones basados en
el cronograma del Proyecto se debe utilizar la Tabla 1 del Criterio de Evaluación, toda vez que el
escenario evaluado contempla la Fase de Construcción más la Fase de Operación del Proyecto donde
esta última tiene una duración de más de 3 años.

En la siguiente Tabla se presentan los aportes del proyecto y el límite de significancia, donde se observa
que el impacto del Proyecto no es significativo para la zona de riesgo prexistente de la Región de los
Lagos.

**Tabla 24. Aportes del proyecto y Nivel de Significancia MP2,5 Media Anual**

|Receptor|Aporte del proyecto<br>(μg/m3)|Límite de<br>Significancia (μg/m3)|% respecto al límite de<br>significancia|
|---|---|---|---|
|Estación Alerce|0,00|0,33|0%|
|Estación Mirasol|0,02|0,33|6%|
|R1|0,03|0,33|9%|
|R2|0,08|0,33|24%|
|R3|0,03|0,33|9%|
|R4|0,01|0,33|4%|

Fuente: Elaboración propia

**Tabla 25. Aportes del proyecto y Nivel de Significancia MP2,5 24 Horas**

|Receptor|Aporte del proyecto<br>(μg/m3)|Límite de<br>Significancia (μg/m3)|% respecto al límite de<br>significancia|
|---|---|---|---|
|Estación Alerce|0,00|1,71|0%|
|Estación Mirasol|0,14|1,71|8%|
|R1|0,17|1,71|10%|
|R2|0,38|1,71|22%|
|R3|0,18|1,71|10%|
|R4|0,09|1,71|5%|

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **55**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.11** **Área de Influencia**

De acuerdo con el Reglamento del Sistema de Evaluación de Impacto Ambiental, el área de influencia
es “ _El área o espacio geográfico, cuyos atributos, elementos naturales o socioculturales deben ser_
_considerados con la finalidad de definir si el proyecto genera o presenta algunos de los efectos,_
_características o circunstancias del artículo 11 de la Ley, o bien para justificar la inexistencia de dichos_
_efectos características o circunstancias_ ”.

El Área de Influencia para este componente, se ha establecido con la finalidad de definir si el proyecto
o actividad genera o presenta alguno de los efectos características o circunstancias del artículo N°11 de
la Ley, o bien para justificar la inexistencia de dichos efectos, características o circunstancias”, tal y
como lo indica el artículo N°2, letra a) del “D.S. N° 40/2012”, así como la Guía sobre el Área de Influencia
en el SEIA, Resolución Exenta N°0423 de la Dirección Ejecutiva del SEA, de fecha 26 de abril de 2017.
La delimitación del Área de Influencia para el componente Calidad de Aire, se realizó a partir del área
definida por la dispersión de las emisiones atmosféricas asociadas al material particulado respirable
MP10 para los receptores primarios.

En particular, para definir el Área de Influencia de los receptores primarios se ha considerado la curva
de isoconcentración respecto al valor de la norma diaria de MP10 que equivale al 1,0% (1,3 μg/m [3] N)
del límite permisible. Es importante señalar que la concentración para los otros contaminantes al ser
muy bajas el porcentaje no se ve reflejado en las isoconcentraciones.

Por otra para los receptores secundarios se consideró la superficie conformada por la isodepositación
equivalente al 1,0% del valor de la norma anual de referencia, es decir 2,0 mg/m [2] -día, como se muestra

en la

Modelación de Emisiones Atmosféricas **56**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 31. Área de Influencia de la Componente Calidad del Aire Receptores Primarios**

Fuente: Elaboración propia

Modelación de Emisiones Atmosféricas **57**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 32. Área de Influencia de la Componente Calidad del Aire Receptores Secundarios**

Modelación de Emisiones Atmosféricas **58**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**3.12** **Resumen de Resultados y Conclusiones**

Según lo expuesto en el documento, se concluye que:

**Respecto a la descripción y justificación del modelo utilizado y los contaminantes modelados:**

El sistema de modelación utilizado corresponde al denominado “WRF-CALPUFF”, que considera
un modelo tipo “puff” Lagrangiano Gaussiano no estacionario y un modelo meteorológico de
predicción numérica a mesoescala no hidrostático. Este modelo sirve para representar la
dispersión de contaminantes en dominios de modelación cuyas fuentes de emisión se ubican a
más de 5 km de los receptores sensibles a analizar.

**Respecto de las características del dominio de modelación y su entorno:**

Se considera como dominio de modelación una grilla cuya superficie es de 28 km x 28 km,
inserta en el modelo meteorológico WRF cuyo dominio es de 50 km x 50 km con una resolución

de 1 km.

Para el escenario geofísico, se utilizó un archivo SRTM1 (Shuttle Radar Topography Mission)
con una resolución aproximada de 30 m. Este proporcionó altura para los puntos de interés
asociados al modelo meteorológico WRF.

Por otra parte, la configuración del modelo CALPUFF es presentada en el Apéndice del informe,
particularmente en el archivo denominado CALPUFF.INP, correspondiente al archivo de control
del modelo para cada escenario modelado.

**Respecto de los datos de entrada al modelo:**

Respecto de las fuentes de emisión, se consideran fuentes de tipo Road, Areal y Puntual,
Puntuales, para representar la emisión de las actividades asociadas al tránsito de vehículos en
caminos pavimentados y no pavimentados, así como al uso de maquinaria pesada,
carga/descarga de material.

Para efectos del presente análisis, para evaluar el escenario más desfavorable, se construyó el
modelo específico para la Fase Construcción más Fase de Operación, correspondiente al año 6.

**Respecto a la incertidumbre:**

Se realizó un análisis de incertidumbre del modelo meteorológico de tipo cualitativo y uno
cuantitativo. En el análisis cualitativo se observó que el modelo se acerca medianamente a la
realidad para las variables analizadas, correspondientes a velocidad, dirección del viento y

temperatura.

Respecto de la velocidad, el análisis cualitativo, se observó en un comportamiento que
sobrestima los valores altos mostrando una mayor intensidad en los vientos modelados,
generando una menor dispersión.

Modelación de Emisiones Atmosféricas **59**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Línea de base de calidad del aire**

Se consideró la línea de base de calidad del aire determinadas en el capítulo 3.2 del presente
documento, en donde se caracterizó la calidad del aire en base a los registros en la Estación
Mirasol y Alerce, siendo estos puntos los más cercanos de monitoreo respecto al Proyecto.

De acuerdo con los valores obtenidos para la línea de base de calidad de aire, todos los
contaminantes considerados en todos sus estadísticos considerados, se encuentran sobre el

valor máximo normado.

**Respecto de la implementación del modelo y el análisis normativo:**

Particularmente en cuanto a los aportes del Proyecto es posible indicar que:

 - El Proyecto genera un aumento de las concentraciones el escenario evaluado, para el

material particulado y los gases. El aporte máximo se genera principalmente en el

monóxido de carbono y dióxido de nitrogeno;

Por otra parte, al comparar los valores de Línea de Base de Calidad del Aire más los aportes del
Proyecto, es posible observar que:

 - Se supera los valores máximos de concentración de la normativa de calidad del aire chilena

producto de las condiciones basales;

Las condiciones basales no se modifican ya que el aporte no es significativo.

**3.13** **Isoconcentraciones Resultantes**

En la siguiente sección se presentan los aportes del Proyecto en su entorno mediante las
isoconcentraciones que muestra el modelo de dispersión, correspondiente a los estadísticos según la
normativa vigente de cada contaminante.

Modelación de Emisiones Atmosféricas **60**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 33. Isoconcentración Promedio Anual MP10.**

Modelación de Emisiones Atmosféricas **61**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 34. Isoconcentración Percentil 98 24 Horas MP10.**

Modelación de Emisiones Atmosféricas **62**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 35. Isoconcentración Promedio Anual MP2,5.**

Modelación de Emisiones Atmosféricas **63**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 36. Isoconcentración Percentil 98 24 Horas MP2,5**

Modelación de Emisiones Atmosféricas **64**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 37. Isoconcentración Promedio Anual NO2.**

Modelación de Emisiones Atmosféricas **65**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 38. Isoconcentración Percentil 99 24 Horas NO2.**

Modelación de Emisiones Atmosféricas **66**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 39. Isoconcentración Percentil 99 1 Hora NO2.**

Modelación de Emisiones Atmosféricas **67**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 40. Isoconcentración Promedio Anual SO2.**

Modelación de Emisiones Atmosféricas **68**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 41. Isoconcentración Percentil 99 24 Horas SO2.**

Modelación de Emisiones Atmosféricas **69**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 42. Isoconcentración Percentil 99 1 Hora SO2.**

Modelación de Emisiones Atmosféricas **70**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 43. Isoconcentración Percentil 99 1 Hora CO.**

Modelación de Emisiones Atmosféricas **71**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 44. Isoconcentración Percentil 99 8 Horas CO.**

Modelación de Emisiones Atmosféricas **72**

|ADENDA|Col2|
|---|---|
|PROYECTO INMOBILIARIO PUERTA NORTE|PROYECTO INMOBILIARIO PUERTA NORTE|

**Figura 45. Idepositación Promedio Anual MPS.**

Modelación de Emisiones Atmosféricas **73**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3.: Normas de Calidad del Aire Consideradas en el Estudio.****

| Parámetro | Norma | Estadístico | Valor límite | Referencia |
| --- | --- | --- | --- | --- |
| MP10 | Primaria | Promedio Anual1 | 50g/m3N | D.S. N° 12/22 MMA |
| MP10 | Primaria | Percentil 98 promedio diario | 130g/m3N | 130g/m3N |
| MP2,5 | Primaria | Promedio Anual1 | 20g/m3N | D.S. N° 12/2011 del MMA |
| MP2,5 | Primaria | Percentil 98 promedio diario | 50g/m3N | 50g/m3N |
| NO2 | Primaria | Promedio Anual1 | 40g/m3N | D.S. N° 40/2023 del MMA |
| NO2 | Primaria | Percentil 99 promedio diario | 100g/m3N | 100g/m3N |
| NO2 | Primaria | Percentil 99 máx. 1 hora1 | 200g/m3N | 200g/m3N |
| CO | Primaria | Percentil 99 1 hora1 | 30 mg/m3N | D.S. N° 115/2002 del<br>MINSEGPRES |
| CO | Primaria | Percentil 99 8 hora1 | 10 mg/m3N | 10 mg/m3N |
| SO2 | Primaria | Promedio Anual1 | 60 μg/m3N | D.S. N° 104/2018 del MMA |
| SO2 | Primaria | Percentil 99 24 horas1 | 150 μg/m3N | 150 μg/m3N |
| SO2 | Primaria | Percentil 99 1 hora1 | 350 μg/m3N | 350 μg/m3N |
| SO2 | Secundaria | Promedio Anual | 60 μg/m3N | D.S. N° 22/2010 del<br>MINSEGPRES |
| SO2 | Secundaria | Percentil 99,7 diario | 260 μg/m3N | 260 μg/m3N |
| SO2 | Secundaria | Percentil 99,73 1 hora | 700 μg/m3N | 700 μg/m3N |
| MPS | Secundaria | Promedio Anual | 200 mg/m2-día | Ordenanza de la<br>Confederación Suiza |

**Tabla 1.: Cronograma del Proyecto****

| Etapa | Actividad | 1 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 | 2 | Col16 | Col17 | Col18 | Col19 | Col20 | Col21 | Col22 | Col23 | Col24 | Col25 | Col26 | 3 | Col28 | Col29 | Col30 | Col31 | Col32 | Col33 | Col34 | Col35 | Col36 | Col37 | Col38 | 4 | Col40 | Col41 | Col42 | Col43 | Col44 | Col45 | Col46 | Col47 | Col48 | Col49 | Col50 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Etapa** | **Actividad** | **1 ** | **2 ** | **3 ** | **4 ** | **5 ** | **6 ** | **7 ** | **8 ** | **9 ** | **10** | **11** | **12** | **13** | **14** | **15** | **16** | **17** | **18** | **19** | **20** | **21** | **22** | **23** | **24** | **25** | **26** | **27** | **28** | **29** | **30** | **31** | **32** | **33** | **34** | **35** | **36** | **37** | **38** | **39** | **40** | **41** | **42** | **43** | **44** | **45** | **46** | **47** | **48** |
| **ETAPA 1** | Instalación de<br>Faenas |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 1** | Movimientos de<br>tierra |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 1** | ALC-AP-ALL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 1** | Pavimentación |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 1** | Construcción de<br>viviendas |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 1** | Áreas verdes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 1** | Electricidad |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 1** | Levantamiento de<br>faenas |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 1** | Entrega a clientes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 2** | Instalación de<br>faenas |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 2** | Movimientos de<br>tierra |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 2** | ALC-AP-ALL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 2** | Pavimentación |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 2** | Construcción de<br>viviendas |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 2** | Áreas verdes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 2** | Electricidad |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 2** | Levantamiento de<br>faenas |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 2** | Entrega a clientes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 3** | Instalación de<br>faenas |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 3** | Movimientos de<br>tierra |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 3** | ALC-AP-ALL |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 3** | Pavimentación |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 3** | Construcción de<br>viviendas |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 3** | Áreas verdes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 3** | Electricidad |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 3** | Levantamiento de<br>faenas |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **ETAPA 3** | Entrega a clientes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

**Tabla 2.: Resumen Estimación de Emisiones****

| Fase | Período | MP10 | MP2,5 | MPS | CO | NOx | SOx |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Construcción | Año 1 | 1,88 | 1,02 | 6,56 | 1,85 | 7,59 | 0,46 |
| Construcción | Año 2 | 1,49 | 0,80 | 5,13 | 1,79 | 7,54 | 0,46 |
| Construcción | Año 3 | 1,27 | 0,42 | 5,65 | 0,35 | 0,61 | 0,00 |
| Construcción | Año 4 | 1,28 | 0,38 | 5,43 | 0,49 | 0,89 | 0,00 |
| Construcción | Año 5 | 1,42 | 0,46 | 6,25 | 1,02 | 1,02 | 0,00 |
| Construcción | Año 6 | 1,43 | 0,50 | 6,54 | 0,45 | 0,78 | 0,00 |
| Construcción | Año 7 | 0,92 | 0,27 | 4,41 | 0,35 | 0,35 | 0,00 |
| Operación | Año 2 | 0,02 | 0,00 | 0,08 | 0,00 | 0,00 | 0,00 |
| Operación | Año 3 | 0,21 | 0,05 | 1,09 | 0,00 | 0,00 | 0,05 |
| Operación | Año 4 | 0,43 | 0,11 | 2,22 | 0,00 | 0,01 | 0,00 |
| Operación | Año 5 | 0,69 | 0,17 | 3,54 | 0,00 | 0,00 | 0,01 |
| Operación | Año 6 | 0,90 | 0,23 | 4,67 | 0,01 | 0,00 | 0,00 |
| Operación | Año 7 | 1,15 | 0,29 | 5,93 | 0,06 | 0,00 | 0,00 |
| Operación | Año 8 | 1,27 | 0,32 | 6,56 | 0,00 | 0,01 | 0,00 |
| **Resumen ** | **Resumen ** | **Resumen ** | **Resumen ** | **Resumen ** | **Resumen ** | **Resumen ** | **Resumen ** |
| **Construcción ** | **Año 1** | 1,88 | 1,02 | 6,56 | 1,85 | 7,59 | 0,46 |
| **Construcción +Operación ** | **Año 2** | 1,51 | 0,80 | 5,22 | 1,79 | 7,55 | 0,46 |
| **Construcción +Operación ** | **Año 3** | 1,48 | 0,48 | 6,73 | 0,35 | 0,61 | 0,05 |
| **Construcción +Operación ** | **Año 4** | 1,71 | 0,49 | 7,65 | 0,49 | 0,90 | 0,00 |
| **Construcción +Operación ** | **Año 5** | 2,10 | 0,64 | 9,79 | 1,03 | 1,03 | 0,02 |
| **Construcción +Operación ** | **Año 6** | 2,33 | 0,73 | 11,20 | 0,45 | 0,78 | 0,00 |
| **Construcción +Operación ** | **Año 7** | 2,06 | 0,56 | 10,34 | 0,41 | 0,35 | 0,00 |
| **Operación ** | **Año 8** | 1,29 | 0,32 | 6,64 | 0,00 | 0,01 | 0,00 |

**Tabla 4.: Coordenadas de la Estación.****

| Estación | Período | Coordenadas Datum WGS 84<br>Huso 18H | Col4 | Contaminante | Operador y Propietario |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Período** | **Este** | **Norte** | **Norte** | **Norte** |
| Mirasol | 2021-2023 | 669.585 | 5.406.017 | MP2,5 | Ministerio del Medio<br>Ambiente |
| Alerce | 2021-2023 | 675.585 | 5.414.803 | MP2,5 | Sub Secretaría del Medio<br>Ambiente |

**Tabla 5.: Información de Datos Válidos.****

| Estación | 2021 | Col3 | 2022 | Col5 | 2023 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Estación** | **Datos válidos/**<br>**preliminares** | **% ** | **Datos válidos/**<br>**preliminares** | **% ** | **Datos válidos/**<br>**preliminares** | **% ** |
| Mirasol | 8.539 | 97% | 8.460 | 97% | 8.412 | 96% |
| Alerce | 8.470 | 97% | 8.501 | 97% | 8.438 | 96% |

**Tabla 6.: Resumen Línea de Base de Calidad del Aire.****

| Estación | Parámetro | Estadístico | Estación Mirasol - Registro monitoreado<br>(μg/m3N) | Col5 | Col6 | Col7 | Norma | % Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Estación** | **Parámetro** | **Estadístico** | **Año 2021** | **Año 2022** | **Año 2023** | **Promedio**<br>**trianual** | **Promedio**<br>**trianual** | **Promedio**<br>**trianual** |
| Mirasol | MP2,5 | Promedio anual | 23 | 28 | 20 | 24 | 20 | 119% |
| Mirasol | MP2,5 | Percentil 98 diario | 112 | 141 | 110 | 141 | 50 | 282% |
| Alerce | MP2,5 | Promedio anual | 25 | 27 | 22 | 25 | 20 | 123% |
| Alerce | MP2,5 | Percentil 98 diario | 110 | 136 | 88 | 136 | 50 | 272% |

**Tabla 7.: Información Estación Meteorológica Mirasol.****

| Estación | Coordenada UTM WGS84 (Huso 18) | Col3 | Variables meteorológicas | Periodo | Administrada por |
| --- | --- | --- | --- | --- | --- |
| **Estación** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| Estación Mirasol | 669.585 | 5.406.017 | Velocidad y dirección del<br>viento, temperatura y<br>humedad relativa | 2021-2023 | Ministerio de<br>Medio Ambiente |

**Tabla 8.: Resumen de estadísticos para Temperatura (°C)****

| Mes | 2023 | Col3 | Col4 |
| --- | --- | --- | --- |
| **Mes** | **Mínima** | **Máxima** | **Media** |
| Enero | 5,6 | 23,6 | 14,1 |
| Febrero | 7,2 | 23,4 | 14,9 |
| Marzo | 3,6 | 23,5 | 12,8 |
| Abril | 5,4 | 18,6 | 11,4 |
| Mayo | -0,6 | 16,9 | 9,6 |
| Junio | -0,3 | 13,8 | 8,3 |
| Julio | -1,2 | 15,8 | 8,0 |
| Agosto | 0,2 | 13,6 | 7,5 |
| Septiembre | 0,3 | 16,7 | 7,9 |
| Octubre | 2,3 | 20,7 | 9,6 |
| Noviembre | 3,2 | 21,6 | 10,8 |
| Diciembre | 4,4 | 23,3 | 13,5 |
| **Promedio** | **2,5** | **19,3** | **10,7** |

**Tabla 9.: Resumen de estadísticos para Humedad Relativa (%)****

| Mes | 2021 | Col3 | Col4 | 2022 | Col6 | Col7 | 2023 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mes** | **Mínima** | **Máxima** | **Media** | **Mínima** | **Máxima** | **Media** | **Mínima** | **Máxima** | **Media** |
| Enero | 37 | 91 | 69 | 38 | 90 | 67 | 36 | 94 | 70 |
| Febrero | 38 | 94 | 69 | 30 | 89 | 68 | 26 | 94 | 69 |
| Marzo | 30 | 94 | 74 | 38 | 92 | 74 | 29 | 93 | 72 |
| Abril | 33 | 93 | 78 | 50 | 94 | 79 | 38 | 96 | 80 |
| Mayo | 47 | 94 | 80 | 39 | 93 | 77 | 43 | 96 | 79 |
| Junio | 38 | 94 | 77 | 27 | 91 | 76 | 40 | 94 | 78 |
| Julio | 52 | 93 | 81 | 35 | 91 | 78 | 46 | 91 | 77 |
| Agosto | 46 | 94 | 78 | 43 | 94 | 76 | 32 | 93 | 75 |
| Septiembre | 34 | 93 | 74 | 39 | 94 | 74 | 43 | 94 | 73 |
| Octubre | 24 | 94 | 71 | 42 | 93 | 72 | 42 | 93 | 71 |
| Noviembre | 40 | 90 | 70 | 36 | 94 | 72 | 29 | 93 | 71 |
| Diciembre | 32 | 94 | 70 | 36 | 90 | 67 | 32 | 90 | 67 |
| **Promedio** | **38** | **93** | **74** | **38** | **92** | **73** | **36** | **93** | **74** |

**Tabla 10.: Resumen de estadísticos para Velocidad del Viento (m/s)****

| Mes | 2021 | Col3 | Col4 | 2022 | Col6 | Col7 | 2023 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Mes** | **Mínima** | **Máxima** | **Media** | **Mínima** | **Máxima** | **Media** | **Mínima** | **Máxima** | **Media** |
| Enero | 0,1 | 6,2 | 2,9 | 0,0 | 5,7 | 1,0 | 0,1 | 4,8 | 1,8 |
| Febrero | 0,1 | 7,4 | 3,0 | 0,0 | 6,4 | 0,9 | 0,0 | 5,1 | 2,0 |
| Marzo | 0,2 | 7,4 | 2,6 | 0,0 | 7,0 | 0,6 | 0,0 | 6,3 | 1,9 |
| Abril | 0,0 | 7,2 | 2,4 | 0,0 | 6,1 | 1,6 | 0,0 | 7,0 | 1,5 |
| Mayo | 0,0 | 7,3 | 2,7 | 0,0 | 4,8 | 1,7 | 0,0 | 7,7 | 1,7 |
| Junio | 0,1 | 9,9 | 2,8 | 0,0 | 5,7 | 1,6 | 0,0 | 6,3 | 2,1 |
| Julio | 0,1 | 6,7 | 2,6 | 0,0 | 6,6 | 2,0 | 0,0 | 6,5 | 2,0 |
| Agosto | 0,0 | 7,7 | 2,5 | 0,0 | 5,6 | 1,5 | 0,0 | 7,0 | 2,0 |
| Septiembre | 0,0 | 7,6 | 1,4 | 0,0 | 6,0 | 1,8 | 0,0 | 5,8 | 2,0 |
| Octubre | 0,0 | 6,7 | 1,5 | 0,1 | 5,4 | 2,0 | 0,1 | 6,2 | 2,1 |
| Noviembre | 0,0 | 6,1 | 1,2 | 0,1 | 5,4 | 2,0 | 0,1 | 6,0 | 2,0 |
| Diciembre | 0,0 | 6,4 | 1,5 | 0,0 | 6,1 | 2,1 | 0,1 | 5,3 | 2,2 |
| Promedio | **0,1** | **7,2** | **2,3** | **0,0 ** | **5,9** | **1,6** | **0,0** | **6,2** | **1,9** |

**Tabla 11.: Sesgo, Error Cuadrático Medio, y Coeficiente de Correlación Velocidad del Viento - Datos****

| Estadístico | Velocidad del<br>Viento (m/s) | Tolerancia | Temperatura (°C) | Tolerancia |
| --- | --- | --- | --- | --- |
| BIAS | 1,655 | +/- 2,5 m/s | -1,013 | +/- 4 °C |
| RMSE | 2,185 | <= 3,5 m/s | 2,297 | <= 4,5 °C |
| Coeficiente de<br>correlación | 0,7 | > 0,6 | 0,98 | > 0,8 |

**Tabla 12.: Tasa de Emisión Consideradas.****

| Tipo de<br>Fuente | ID | Descripción | Unidad | SO2 | SO4 | NO | NO2 | HNO3 | NO3 | CO | MP10 | MP2,5 | MPS |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ROAD | SRC_1 | Salida Puerto Montt | Kg/m/h | 1,77E-07 | 0,00E+00 | 1,07E-05 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 1,82E-06 | 1,00E-04 | 2,51E-05 | 5,17E-04 |
| ROAD | SRC_2 | Acceso | Kg/m/h | 1,97E-07 | 0,00E+00 | 1,19E-05 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 2,01E-06 | 1,11E-04 | 2,79E-05 | 5,73E-04 |
| AREA_POLY | SRC_3 | Comp1_E1 | t/año-m2 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 1,22E-06 | 5,88E-07 | 5,74E-06 |
| AREA_POLY | SRC_6 | Escarpe | t/año-m2 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 2,21E-06 | 3,31E-07 | 2,21E-06 |
| ROAD | SRC_7 | Tramo 2 | Kg/m/h | 7,29E-09 | 0,00E+00 | 2,86E-06 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 3,43E-07 | 2,68E-05 | 6,58E-06 | 1,39E-04 |
| ROAD | SRC_8 | Tramo 3 | Kg/m/h | 7,31E-09 | 0,00E+00 | 2,86E-06 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 3,43E-07 | 2,48E-05 | 6,09E-06 | 1,29E-04 |
| ROAD | SRC_9 | Tramo 4 | Kg/m/h | 1,04E-08 | 0,00E+00 | 4,06E-06 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 4,87E-07 | 9,40E-06 | 2,40E-06 | 4,83E-05 |
| ROAD | SRC_10 | Tramo 8 | Kg/m/h | 1,82E-08 | 0,00E+00 | 7,13E-06 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 8,55E-07 | 1,01E-04 | 1,03E-05 | 3,28E-04 |
| AREA_POLY | SRC_11 | Acopio Etapa 1 | t/año-m2 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 2,93E-10 | 4,49E-11 | 5,85E-10 |
| POINT | SRC_12 | Maq1 | t/año | 9,72E-04 | 0,00E+00 | 2,93E-01 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 2,06E-01 | 2,20E-02 | 2,20E-02 | 2,20E-02 |
| POINT | SRC_13 | Maq2 | t/año | 9,72E-04 | 0,00E+00 | 2,93E-01 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 2,06E-01 | 2,20E-02 | 2,20E-02 | 2,20E-02 |
| POINT | SRC_15 | Caldera | t/año | 8,17E-05 | 0,00E+00 | 1,37E-02 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 1,15E-02 | 1,04E-03 | 1,04E-03 | 1,04E-03 |
| ROAD | SRC_16 | Tramo 9 | t/año | 1,70E-08 | 0,00E+00 | 6,66E-06 | 0,00E+00 | 0,00E+00 | 0,00E+00 | 7,99E-07 | 3,36E-06 | 5,76E-07 | 1,04E-05 |

**Tabla 13.: Coordenadas de los receptores Primarios****

| Nombre | ID del<br>Modelo | Descripción | Coordenadas UTM (Huso 18G.<br>Datum WGS84) | Col5 |
| --- | --- | --- | --- | --- |
| **Nombre** | **ID del**<br>**Modelo** | **Descripción** | **Este (m)** | **Norte (m)** |
| Estación<br>Alerce | R_1 | Estación calidad del aire | 675.585 | 5.414.803 |
| Estación<br>Mirasol | R_2 | Estación calidad del aire | 669.585 | 5.406.017 |
| R1 | R_3 | Inmueble casa habitación 1 piso ubicada en calle Diamante**No**<br>4940, aprox. 300m. al poniente del límite predial del Proyecto. | 668.016 | 5.408.915 |
| R2 | R_4 | Inmueble casa habitación 1 piso ubicada en calle Diamante**No**<br>5020, aprox. 20m. al sur poniente del límite predial del<br>Proyecto. | 668.245 | 5.408.698 |
| R3 | R_5 | Inmueble casa habitación 2 pisos ubicada en pasaje Aragonita<br>No 5707, aprox. 75m. al sur poniente del límite predial del<br>Provecto. | 668.257 | 5.408.494 |
| R4 | R_6 | Inmueble casa habitación 2 pisos ubicada encalle Ojos de<br>Tigre N° 5734, aprox. 35m. al sur del límite predial del<br>Provecto. | 668.372 | 5.408.463 |
| RF1 | R_7 | Avifauna y; Anfibios | 668.867 | 5.408.704 |
| RF2 | R_8 | Avifauna y; Anfibios | 668.970 | 5.409.020 |

**Tabla 14: Detalle Archivo WRF****

| Proyección Cartográfica | Cónica conforme de Lambert (LCC) |
| --- | --- |
| Período | 1 Enero al 31 de Diciembre 2023 |
| Origen | Latitude: 41.455 S - Longitude: 72.982 W |
| Datum | NWS-84 |
| Grilla | 1 km |

**Tabla 15: Características del Suelo****

| Tipo de Suelo | Descripción | Rugosidad<br>superficial (m) | Albedo | Razón de Bowen |
| --- | --- | --- | --- | --- |
| 10 | Urbanización | 1,0 | 0,18 | 1,5 |
| 20 | Suelo agrícola sin riego | 0,25 | 0,15 | 1,0 |
| 30 | Pastizal | 0,05 | 0,25 | 1,0 |
| 40 | Bosque | 1,0 | 0,10 | 1,0 |
| 51 | Pequeña masa de agua | 0,001 | 0,1 | 0,0 |

**Tabla 16.: Aporte del Proyecto Material Particulado Respirable μg/m** **[3]** **N (MP10 y MP2,5)****

| Receptor | MP10 | Col3 | Col4 | Col5 | Col6 | Col7 | MP2,5 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Anual** | **Valor**<br>**Norma**<br>**Anual D.S.**<br>**No**<br>**12/2022** | **% de la**<br>**Norma** | **P98 24**<br>**hrs** | **Valor**<br>**Norma**<br>**Diaria D.S.**<br>**N°12/2022** | **% de la**<br>**Norma** | **Anual** | **Valor Anual**<br>**Norma D.S.**<br>**No 12/2012** | **% de la**<br>**Norma** | **P98 24 hrs** | **Valor Norma**<br>**Diaria D.S.**<br>**No 12/2012** | **% de la**<br>**Norma** |
| Estación Alerce | 0,00 | 50 | 0,00% | 0,01 | 130 | 0,00% | 0,00 | 20 | 0,00% | 0,00 | 50 | 0,00% |
| Estación Mirasol | 0,02 | 0,02 | 0,03% | 0,09 | 0,09 | 0,07% | 0,00 | 0,00 | 0,02% | 0,02 | 0,02 | 0,05% |
| R1 | 0,02 | 0,02 | 0,03% | 0,16 | 0,16 | 0,13% | 0,00 | 0,00 | 0,02% | 0,04 | 0,04 | 0,08% |
| R2 | 0,03 | 0,03 | 0,07% | 0,29 | 0,29 | 0,22% | 0,01 | 0,01 | 0,04% | 0,08 | 0,08 | 0,15% |
| R3 | 0,03 | 0,03 | 0,07% | 0,26 | 0,26 | 0,20% | 0,01 | 0,01 | 0,04% | 0,07 | 0,07 | 0,13% |
| R4 | 0,05 | 0,05 | 0,10% | 0,43 | 0,43 | 0,33% | 0,01 | 0,01 | 0,06% | 0,10 | 0,10 | 0,19% |

**Tabla 17.: Aporte del Proyecto Dióxido de Nitrógeno μg/m** **[3]** **N (NO** **2** **)****

| Receptor | NO2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Anual** | **Valor Norma**<br>**Anual D.S. No**<br>**40/2023** | **% de la Norma** | **P99 24 horas** | **Valor Norma**<br>**Horaria D.S. No**<br>**40/2023** | **% de la Norma** | **P99 1 hora** | **Valor Norma**<br>**Horaria D.S. No**<br>**40/2023** | **% de la Norma** |
| Estación Alerce | 0,00 | 40 | 0,00% | 0,00 | 100 | 0,00% | 0,03 | 200 | 0,01% |
| Estación Mirasol | 0,00 | 0,00 | 0,01% | 0,03 | 0,03 | 0,03% | 0,34 | 0,34 | 0,17% |
| R1 | 0,00 | 0,00 | 0,01% | 0,07 | 0,07 | 0,07% | 1,08 | 1,08 | 0,54% |
| R2 | 0,01 | 0,01 | 0,02% | 0,11 | 0,11 | 0,11% | 1,79 | 1,79 | 0,90% |
| R3 | 0,01 | 0,01 | 0,02% | 0,10 | 0,10 | 0,10% | 1,59 | 1,59 | 0,79% |
| R4 | 0,01 | 0,01 | 0,02% | 0,13 | 0,13 | 0,13% | 2,35 | 2,35 | 1,17% |

**Tabla 18.: Aporte del Proyecto Monóxido de Carbono μg/m** **[3]** **N (CO)****

| Receptor | CO | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **P99 8 horas** | **Valor Norma 8 hrs**<br>**D.S. No 115/2002** | **% de la Norma** | **P99 1 hora** | **Valor Norma 1 hr**<br>**D.S. No 115/2002** | **% de la Norma** |
| Estación Alerce | 0,00 | 10000 | 0,00% | 0,01 | 30000 | 0,00% |
| Estación Mirasol | 0,02 | 0,02 | 0,00% | 0,13 | 0,13 | 0,00% |
| R1 | 0,10 | 0,10 | 0,00% | 0,72 | 0,72 | 0,00% |
| R2 | 0,22 | 0,22 | 0,00% | 1,29 | 1,29 | 0,00% |
| R3 | 0,18 | 0,18 | 0,00% | 1,03 | 1,03 | 0,00% |
| R4 | 0,27 | 0,27 | 0,00% | 1,52 | 1,52 | 0,01% |

**Tabla 19.: Aporte del Proyecto Dióxido de Azufre μg/m** **[3]** **N (SO** **2** **), Norma Primaria****

| Receptor | SO2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Anual** | **Valor Norma**<br>**D.S. No**<br>**104/2018** | **% de la**<br>**Norma** | **P99 24 hrs** | **Valor Norma**<br>**D.S. No**<br>**104/2018** | **% de la**<br>**Norma** | **P99 1 hr** | **Valor Norma**<br>**D.S. No**<br>**104/2018** | **% de la**<br>**Norma** |
| Estación Alerce | 6,20E-07 | 60 | 0,00% | 9,50E-06 | 150 | 0,00% | 1,45E-05 | 350 | 0,00% |
| Estación Mirasol | 2,39E-05 | 2,39E-05 | 0,00% | 1,70E-04 | 1,70E-04 | 0,00% | 4,77E-04 | 4,77E-04 | 0,00% |
| R1 | 2,43E-05 | 2,43E-05 | 0,00% | 3,22E-04 | 3,22E-04 | 0,00% | 5,73E-04 | 5,73E-04 | 0,00% |
| R2 | 5,49E-05 | 5,49E-05 | 0,00% | 6,03E-04 | 6,03E-04 | 0,00% | 1,25E-03 | 1,25E-03 | 0,00% |
| R3 | 5,54E-05 | 5,54E-05 | 0,00% | 5,53E-04 | 5,53E-04 | 0,00% | 1,21E-03 | 1,21E-03 | 0,00% |
| R4 | 8,87E-05 | 8,87E-05 | 0,00% | 8,20E-04 | 8,20E-04 | 0,00% | 1,93E-03 | 1,93E-03 | 0,00% |

**Tabla 20.: Aporte del Proyecto Dióxido de Azufre μg/m** **[3]** **N (SO** **2** **), Norma Secundaria****

| Receptor | SO2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Anual** | **Valor Norma**<br>**D.S. No**<br>**22/2010** | **% de la**<br>**Norma** | **P99 24 hrs** | **Valor Norma**<br>**D.S. No 22/2010** | **% de la**<br>**Norma** | **P99 1 hr** | **Valor Norma**<br>**D.S. No**<br>**22/2010** | **% de la**<br>**Norma** |
| RF1 | 9,55E-04 | 60 | 0,00% | 4,29E-03 | 260 | 0,00% | 2,49E-02 | 700 | 0,00% |
| RF2 | 3,75E-04 | 60 | 0,00% | 1,83E-03 | 260 | 0,00% | 1,13E-02 | 700 | 0,00% |

**Tabla 21.: Aporte del Proyecto Material Particulado Sedimentable mg/m** **[2]** **-día (MPS), Norma Secundaria****

| Receptor | MPS | Col3 | Col4 |
| --- | --- | --- | --- |
| **Receptor** | **Promedio Anual** | **Valor Norma Suiza** | **% de la Norma** |
| RF1 | 5,87 | 200 | 2,9% |
| RF2 | 1,26 | 200 | 0,6% |

**Tabla 22.: Análisis Normativo MP2,5****

| Receptores | Concentraciones (μg/m3N) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptores** | **MP2,5** | **MP2,5** | **MP2,5** | **MP2,5** | **MP2,5** | **MP2,5** | **MP2,5** | **MP2,5** |
| **Receptores** | **Promedio Anual** | **Promedio Anual** | **Promedio Anual** | **Promedio Anual** | **Percentil 98 24 Horas** | **Percentil 98 24 Horas** | **Percentil 98 24 Horas** | **Percentil 98 24 Horas** |
| **Receptores** | **Aporte**<br>**Proyecto**<br>**(AP)** | **Línea de**<br>**Base (LB)** | **AP+LB** | **% de la**<br>**Norma**<br>**(20**<br>**μg/m3N)** | **Aporte**<br>**Proyecto**<br>**(AP)** | **Línea de**<br>**Base (LB)** | **AP+LB** | **% de la**<br>**Norma** |
| **Receptores** | **Aporte**<br>**Proyecto**<br>**(AP)** | **Línea de**<br>**Base (LB)** | **AP+LB** | **% de la**<br>**Norma**<br>**(20**<br>**μg/m3N)** | **Aporte**<br>**Proyecto**<br>**(AP)** | **Línea de**<br>**Base (LB)** | **AP+LB** | **(50**<br>**μg/m3N)** |
| Estación Alerce | 0,00 | 25 | 25,0 | 125% | 0,00 | 136 | 136,0 | 272% |
| Estación Mirasol | 0,00 | 24 | 24,0 | 120% | 0,02 | 141 | 141,0 | 282% |

**Tabla 23.: Coordenadas de los Puntos de Máximo Impacto (PMI)****

| Parámetro | Norma | Estadístico | Concentración<br>(μg/m3) | Valor Norma | Coordenadas UTM WGS 84 | Col7 | Identificación |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Parámetro** | **Norma** | **Estadístico** | **Concentración**<br>**(μg/m3) ** | **Valor Norma** | **Este (m)** | **Norte (m)** | **Norte (m)** |
| MP10 | Primaria | Promedio Anual | 5,67 | 50g/m3N | 669.069 | 5.408.234 | 566 metros al sureste |
| MP10 | Primaria | Percentil 98 promedio diario | 16,83 | 130g/m3N | 669.069 | 5.408.234 | 566 metros al sureste |
| MP2,5 | Primaria | Promedio Anual | 1,42 | 20g/m3N | 669.069 | 5.408.234 | 566 metros al sureste |
| MP2,5 | Primaria | Percentil 98 promedio diario | 4,23 | 50g/m3N | 669.069 | 5.408.234 | 566 metros al sureste |
| NO2 | Primaria | Promedio Anual | 0,06 | 400g/m3N | 668.867 | 5.408.704 | RF1 |
| NO2 | Primaria | Percentil 99 máx. 24 horas | 0,26 | 100g/m3N | 668.867 | 5.408.704 | RF1 |
| NO2 | Primaria | Percentil 99 máx. 1 hora | 2,92 | 200g/m3N | 668.867 | 5.408.704 | RF1 |
| CO | Primaria | Percentil 99 8 horas | 1,93 | 10.000g/m3N | 668.867 | 5.408.704 | RF1 |
| CO | Primaria | Percentil 99 1 hora | 7,27 | 30.000g/m3N | 668.867 | 5.408.704 | RF1 |
| SO2 | Primaria | Promedio Anual | 0,01 | 60 μg/m3N | 669.069 | 5.408.234 | 566 metros al sureste |
| SO2 | Primaria | Percentil 99 24 horas | 0,03 | 150 μg/m3N | 669.069 | 5.408.234 | 566 metros al sureste |
| SO2 | Primaria | Percentil 99 1 hora | 0,10 | 350 μg/m3N | 669.069 | 5.408.234 | 566 metros al sureste |

**Tabla 24.: Aportes del proyecto y Nivel de Significancia MP2,5 Media Anual****

| Receptor | Aporte del proyecto<br>(μg/m3) | Límite de<br>Significancia (μg/m3) | % respecto al límite de<br>significancia |
| --- | --- | --- | --- |
| Estación Alerce | 0,00 | 0,33 | 0% |
| Estación Mirasol | 0,02 | 0,33 | 6% |
| R1 | 0,03 | 0,33 | 9% |
| R2 | 0,08 | 0,33 | 24% |
| R3 | 0,03 | 0,33 | 9% |
| R4 | 0,01 | 0,33 | 4% |

**Tabla 25.: Aportes del proyecto y Nivel de Significancia MP2,5 24 Horas****

| Receptor | Aporte del proyecto<br>(μg/m3) | Límite de<br>Significancia (μg/m3) | % respecto al límite de<br>significancia |
| --- | --- | --- | --- |
| Estación Alerce | 0,00 | 1,71 | 0% |
| Estación Mirasol | 0,14 | 1,71 | 8% |
| R1 | 0,17 | 1,71 | 10% |
| R2 | 0,38 | 1,71 | 22% |
| R3 | 0,18 | 1,71 | 10% |
| R4 | 0,09 | 1,71 | 5% |
