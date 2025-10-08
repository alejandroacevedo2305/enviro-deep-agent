---
title: Sin título
author: Hermes
date: D:20230629163737-04'00'
language: es
type: report
pages: 138
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Parque Fotovoltaico Parina Solar
-->

**ANEXO 19**

**MODELACION DE CALIDAD DEL AIRE ACTUALIZADO**

## Anexo 19 Modelación de Calidad del Aire Actualizado

# Parque Fotovoltaico Parina Solar

## Junio 2023

**Preparado para:**

|REVISIONES|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|No REV.|ELABORADO POR|REVISADO POR|FECHA|FIRMA RESPONSABLE|
|V2|Carlos Ross A.|María José Meneses V.|30-05-2023||
|V2|Ingeniero Ambiental,<br>UNAB|Ingeniero Civil de<br>Industrias con Mención<br>en Ingeniería Química,<br>PUC.|Ingeniero Civil de<br>Industrias con Mención<br>en Ingeniería Química,<br>PUC.|Ingeniero Civil de<br>Industrias con Mención<br>en Ingeniería Química,<br>PUC.|
|V2|Ingeniero Ambiental,<br>UNAB|Ingeniero Civil de<br>Industrias con Mención<br>en Ingeniería Química,<br>PUC.|Ingeniero Civil de<br>Industrias con Mención<br>en Ingeniería Química,<br>PUC.|María José Meneses V.|

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

INDICE

**1.** **INTRODUCCIÓN ................................................................................................................ 1**

**2.** **RESUMEN DE INVENTARIO DE EMISIONES ATMOSFÉRICAS ................................................ 2**

**3.** **MODELO DE CALIDAD DEL AIRE ......................................................................................... 3**

**3.1.** **Tipo de Modelo de Calidad del Aire Seleccionado .............................................................. 3**

**3.2.** **Descripción del Modelo de Calidad del Aire Seleccionado - CALPUFF .................................. 3**

**3.3.** **Características del Modelo de Dispersión de Contaminantes .............................................. 4**

3.3.1. Dominio de Modelación .................................................................................................................. 4

3.3.2. Topografía del Sector ...................................................................................................................... 7

**3.4.** **Descripción del Modelo Meteorológico - WRF .................................................................. 9**

**3.5.** **Caracterización de Clima del Área del Proyecto ............................................................... 11**

**3.6.** **Caracterización Meteorológica del Área del Proyecto ...................................................... 17**

3.6.1. Meteorología de Superficie - Valores Observados ....................................................................... 17

3.6.2. Meteorología de Superficie - Valores Modelados ........................................................................ 42

3.6.3. Meteorología de Altura - Valores Observados ............................................................................. 53

3.6.4. Meteorología de Altura - Valores Modelados .............................................................................. 53

**3.7.** **Análisis de Incertidumbre ............................................................................................... 57**

3.7.1. Comparación Cualitativa ............................................................................................................... 57

3.7.2. Comparación Cuantitativa ............................................................................................................. 61

**3.8.** **Evolución Cambio Climático en el Área del Proyecto ........................................................ 62**

**3.9.** **Normas de Calidad del Aire ............................................................................................. 69**

**3.10.** **Línea Base de Calidad del Aire ......................................................................................... 70**

3.10.1. Estación Centro ......................................................................................................................... 72

3.10.2. Club Deportivo 23 de marzo ..................................................................................................... 82

3.10.3. Colegio Pedro Vergara Keller .................................................................................................... 88

3.10.4. Resumen de Línea de Base de Calidad del Aire ........................................................................ 92

www.dfmconsultores.cl

**info@dfmconsultores.cl**

i

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.11.** **Escenario Modelado ....................................................................................................... 94**

3.11.1. Fuentes Emisoras Fase de Construcción ................................................................................... 94

**3.12.** **Receptores de Interés ..................................................................................................... 96**

**3.13.** **Resultados de la Modelación Fase de Construcción ......................................................... 98**

**3.14.** **Concentración Total Esperada ....................................................................................... 117**

**4.** **DETERMINACIÓN DEL ÁREA DE INFLUENCIA DEL PROYECTO .......................................... 124**

**5.** **CONCLUSIONES ............................................................................................................ 126**

www.dfmconsultores.cl

**info@dfmconsultores.cl**

ii

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

INDICE TABLAS

Tabla 2-1 - Resumen de emisiones atmosféricas. Fase de Construcción. .......................................... 2

Tabla 3-1. Configuración parámetros principales WRF. .................................................................... 10

Tabla 3-2 - Estación de Monitoreo Meteorológico. ......................................................................... 17

Tabla 3-3- Resumen de información Velocidad del Viento observada. Estación El Cobre. .............. 19

Tabla 3-4 - Frecuencia de distribución, velocidad y dirección del viento. Estación Hospital del Cobre.

........................................................................................................................................................... 22

Tabla 3-5 - Resumen de información Temperatura observada. Estación El Cobre........................... 26

Tabla 3-6 - Resumen de información Humedad Relativa observada. Estación El Cobre. ................. 30

Tabla 3-7- Resumen de información Presión Atmosférica observada. Estación El Cobre. ............... 34

Tabla 3-8- Resumen de información Radiación Solar observada. Estación El Cobre. ....................... 38

Tabla 3-9- Resumen de Información Velocidad del Viento año 2019. Estación Hospital El Cobre. . 42

Tabla 3-10 - Frecuencia de distribución de velocidad y dirección del viento modelados en Estación

Hospital del Cobre, año 2019. ........................................................................................................... 45

Tabla 3-11 - Resumen de Información Temperatura modelada en Hospital El Cobre, año 2019. ... 49

Tabla 3-12 - Resumen de Información Altura de Capa de Mezcla modelada en Estación Hospital El

Cobre, año 2019. ............................................................................................................................... 53

Tabla 3-13 - Estadígrafos de Dispersión para Velocidad del Viento y Temperatura. ....................... 61

Tabla 3-14. Principales índices evaluación cambio climático. Región de Antofagasta, provincia El Loa,

comuna de Calama. ........................................................................................................................... 62

Tabla 3-15 - Normas de calidad del aire. .......................................................................................... 69

Tabla 3-16 - Caracterización de estación de monitoreo de calidad del aire. ................................... 70

Tabla 3-17. Resultados Monitoreo de MP2.5. Estación Centro. ....................................................... 72

Tabla 3-18. Comparación de Monitoreo de MP2.5 con Normativa. Estación Centro. ..................... 72

Tabla 3-19. Resultados Monitoreo de MP10. Estación Centro. ........................................................ 74

Tabla 3-20. Comparación de Monitoreo de MP10 con Normativa. Estación Centro. ...................... 74

Tabla 3-21. Resultados Monitoreo de CO. Estación Centro. ............................................................. 76

Tabla 3-22. Comparación de Monitoreo de CO con normativa. Estación Centro. ............................ 76

www.dfmconsultores.cl

**info@dfmconsultores.cl**

iii

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Tabla 3-23. Resultados Monitoreo de NO 2 . Estación Centro. ........................................................... 78

Tabla 3-24. Comparación con normativa de dióxido de nitrógeno (NO 2 ). Estación Centro. ............ 78

Tabla 3-25. Resultados Monitoreo de SO 2 . Estación Centro. ............................................................ 80

Tabla 3-26. Comparación de Monitoreo de SO 2 con Normativa. Estación Centro. .......................... 80

Tabla 3-27. Resultados Monitoreo de MP2.5. Estación Club Deportivo 23 de marzo. ..................... 82

Tabla 3-28. Comparación de Monitoreo con Normativa. Estación Club Deportivo 23 de marzo. .... 82

Tabla 3-29. Resultados Monitoreo de MP10. Estación Club Deportivo 23 de marzo. ...................... 84

Tabla 3-30. Comparación de Monitoreo de MP10 con Normativa. Estación Club Deportivo 23 de

marzo................................................................................................................................................. 84

Tabla 3-31. Resultados Monitoreo de SO 2 . Estación Club Deportivo 23 de marzo. ......................... 86

Tabla 3-32. Comparación de Monitoreo de SO 2 con Normativa. Estación Club Deportivo 23 de marzo.

........................................................................................................................................................... 86

Tabla 3-33. Resultados Monitoreo de MP2.5. Estación Colegio Pedro Vergara Keller. .................... 88

Tabla 3-34. Comparación de Monitoreo con Normativa de MP2,5. Estación Colegio Pedro Vergara

Keller. ................................................................................................................................................ 88

Tabla 3-35. Resultados Monitoreo de MP10. Estación Colegio Pedro Vergara Keller. .................... 90

Tabla 3-36. Comparación de Monitoreo con Normativa de MP10. Estación Colegio Pedro Vergara

Keller. ................................................................................................................................................ 90

Tabla 3-37 - Resumen Línea Base de Calidad del Aire, Estación Centro. ......................................... 92

Tabla 3-38 - Resumen Línea Base de Calidad del Aire, Estación Club Deportivo 23 de marzo. ....... 93

Tabla 3-39 - Resumen Línea Base de Calidad del Aire, Estación Colegio Pedro Vergara Keller. ...... 93

Tabla 3-40. Fuentes Emisoras Fase de Construcción. ....................................................................... 94

Tabla 3-41- Receptores de Interés. .................................................................................................. 96

Tabla 3-42 - Resultados de modelo de dispersión de MP2.5. Fase de Construcción. ...................... 98

Tabla 3-43 - Resultados de modelo de dispersión de MP10. Fase de Construcción. ....................... 99

Tabla 3-44 - Resultados de modelo de dispersión de MPS. Fase de Construcción. ....................... 100

Tabla 3-45 - Resultados de modelo de dispersión de CO. Fase de Construcción. ......................... 101

Tabla 3-46 - Resultados de modelo de dispersión de NO 2 . Fase de Construcción. ........................ 102

www.dfmconsultores.cl

**info@dfmconsultores.cl**

iv

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Tabla 3-47 - Resultados de modelo de dispersión de SO 2 . Fase de Construcción. ........................ 103

Tabla 3-48 - Concentración total esperada, estación Centro. Fase de Construcción. ................... 117

Tabla 3-49 - Aporte otros proyectos, Estación Centro. .................................................................. 118

Tabla 3-50 - Aporte otros proyectos, Estación Club Deportivo 23 de marzo. ................................ 119

Tabla 3-51 - Aporte otros proyectos, estación Colegio Pedro Vergara Keller. ............................... 120

Tabla 3-52 - Concentración total esperada, estación Centro. Fase de Construcción. ................... 121

Tabla 3-53 - Concentración total esperada, estación Club Deportivo 23 de marzo. Fase de

Construcción.................................................................................................................................... 122

Tabla 3-54 - Concentración total esperada, estación Colegio Pedro Vergara Keller. Fase de

Construcción.................................................................................................................................... 122

Tabla 5-1. Archivos de modelación entregados. ............................................................................. 127

www.dfmconsultores.cl

**info@dfmconsultores.cl**

v

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

ÍNDICE FIGURAS

Figura 3-1 - Dominio de Modelación. ................................................................................................. 5

Figura 3-2 - Ubicación Grilla de Receptores. ...................................................................................... 6

Figura 3-3 - Topografía del Dominio de Modelación. ......................................................................... 8

Figura 3-4 - Campo de Isotermas. Región de Antofagasta. .............................................................. 12

Figura 3-5 - Campo de Isoyetas. Región de Antofagasta. ................................................................. 13

Figura 3-6 - Climograma de Antofagasta. ......................................................................................... 14

Figura 3-7 - Clasificación climática según Köppen. Región de Antofagasta. .................................... 16

Figura 3-8 - Ubicación Referencial estación de monitoreo meteorológico. .................................... 18

Figura 3-9 - Serie de tiempo para velocidad del viento. Estación Hospital del Cobre. .................... 20

Figura 3-10 - Serie de tiempo para dirección del viento. Estación Hospital del Cobre. ................... 21

Figura 3-11 - Ciclo diario de velocidad del viento. Estación Hospital del Cobre. ............................. 23

Figura 3-12 - Ciclo diario dirección del viento. Estación Hospital del Cobre. ................................... 24

Figura 3-13 - Ciclo estacional de vientos. Estación Hospital del Cobre. ........................................... 25

Figura 3-14 - Serie de tiempo para la temperatura. Estación Hospital del Cobre............................ 27

Figura 3-15 - Ciclo diario de temperatura. Estación Hospital del Cobre. ......................................... 28

Figura 3-16 - Ciclo estacional de temperatura. Estación Hospital del Cobre. .................................. 29

Figura 3-17 - Serie de tiempo para la Humedad Relativa. Estación Hospital del Cobre. ................. 31

Figura 3-18 - Ciclo diario de Humedad Relativa. Estación Hospital del Cobre. ................................ 32

Figura 3-19 - Ciclo estacional de Humedad Relativa. Estación Hospital del Cobre. ......................... 33

Figura 3-20 - Serie de tiempo para la Presión Atmosférica. Estación Hospital del Cobre. ............... 35

Figura 3-21 - Ciclo estacional de Presión Atmosférica. Estación Hospital del Cobre. ...................... 36

Figura 3-22. Serie de tiempo para la Precipitación. Estación Hospital del Cobre. ............................ 37

Figura 3-23 - Serie de tiempo para la Radiación Solar. Estación Hospital del Cobre. ...................... 39

Figura 3-24 - Ciclo diario de Radiación Solar. Estación Hospital del Cobre. ..................................... 40

Figura 3-25 - Ciclo estacional de Radiación Solar. Estación Hospital del Cobre. .............................. 41

www.dfmconsultores.cl

**info@dfmconsultores.cl**

vi

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Figura 3-26 - Serie de tiempo de velocidad del viento modelado en Estación Hospital del Cobre, año

2019. .................................................................................................................................................. 43

Figura 3-27 - Serie de tiempo de dirección del viento modelado en Estación Hospital del Cobre, año

2019. .................................................................................................................................................. 44

Figura 3-28 - Ciclo Diario de Velocidad del Viento modelado en Estación Hospital del Cobre, año

2019. .................................................................................................................................................. 46

Figura 3-29 - Ciclo Diario de Dirección de Viento modelado en Estación Hospital del Cobre, año 2019.

........................................................................................................................................................... 47

Figura 3-30 - Ciclo Estacional de Vientos modelado en Estación Hospital del Cobre, año 2019. ..... 48

Figura 3-31 - Serie de Tiempo Temperatura modelada en Hospital El Cobre, año 2019. ................ 50

Figura 3-32 - Ciclo Diario Temperatura modelada en Hospital El Cobre, año 2019. ........................ 51

Figura 3-33 - Ciclo Estacional de Temperatura modelada en Hospital El Cobre, año 2019. ............ 52

Figura 3-34 - Serie de Tiempo Altura de Capa de Mezcla. ................................................................ 54

Figura 3-35 - Ciclo Diario Altura de Capa de Mezcla. ........................................................................ 55

Figura 3-36 - Ciclo Estacional Altura de Capa de Mezcla. ................................................................. 56

Figura 3-37 - Comparación de Ciclos Diarios de Dirección del Viento, Estación Hospital del Cobre. 57

Figura 3-38 - Comparación del Ciclo Diario de la Velocidad del Viento, Estación Hospital del Cobre.

........................................................................................................................................................... 58

Figura 3-39 - Comparación del Ciclo Estacional de la Velocidad y Dirección del Viento, Estación

Hospital del Cobre. ............................................................................................................................ 58

Figura 3-40 - Comparación del Ciclo Diario de la Temperatura, Estación Hospital del Cobre. ........ 59

Figura 3-41 - Comparación del Ciclo Estacional de Temperatura, Estación Hospital del Cobre. ..... 60

Figura 3-42. Comparación Temperatura Media Anual entre situación actual y futura. Región de

Antofagasta. ...................................................................................................................................... 64

Figura 3-43. Comparación Precipitación Acumulada Anual entre situación actual y futura. Región de

Antofagasta. ...................................................................................................................................... 65

Figura 3-44. Comparación Velocidad Media Anual Viento entre situación actual y futura. Región de

Antofagasta. ...................................................................................................................................... 66

Figura 3-45. Evolución Precipitación Acumulada Anual. Región de Antofagasta. ............................ 67

www.dfmconsultores.cl

**info@dfmconsultores.cl**

vii

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Figura 3-46. Evolución Velocidad Media Anual Viento. Región de Antofagasta. .............................. 68

Figura 3-47. Ubicación Estaciones de Monitoreo de Calidad del Aire. ............................................. 71

Figura 3-48. Serie de tiempo Material Particulado Fino (MP2,5). Estación Centro. ......................... 73

Figura 3-49. Serie de tiempo Material Particulado Respirable (MP10). Estación Centro. ................ 75

Figura 3-50. Serie de tiempo Monóxido de Carbono (CO). Estación Centro. ................................... 77

Figura 3-51. Serie de tiempo Dióxido de Nitrógeno (NO 2 ). Estación Centro. ................................... 79

Figura 3-52. Serie de tiempo Dióxido de Azufre (SO2). Estación Centro. ......................................... 81

Figura 3-53. Serie de tiempo Material Particulado Fino (MP2,5). Estación Club Deportivo 23 de

marzo................................................................................................................................................. 83

Figura 3-54. Serie de tiempo Material Particulado Respirable (MP10). Estación Club Deportivo 23 de

marzo................................................................................................................................................. 85

Figura 3-55. Serie de tiempo Dióxido de Azufre (SO2). Estación Club Deportivo 23 de marzo. ....... 87

Figura 3-56. Serie de tiempo Material Particulado Fino (MP2,5). Estación Colegio Pedro Vergara

Keller. ................................................................................................................................................ 89

Figura 3-57. Serie de tiempo Material Particulado Respirable (MP10). Estación Colegio Pedro

Vergara Keller. ................................................................................................................................... 91

Figura 3-58 - Ubicación Fuentes Emisoras Fase de Construcción. ................................................... 95

Figura 3-59 - Ubicación de Receptores de Interés. .......................................................................... 97

Figura 3-60. Curva de Isoconcentración para Percentil 98 período 24 horas MP2,5 (μg/m [3] ). Fase de

Construcción.................................................................................................................................... 104

Figura 3-61. Curva de Isoconcentración para período anual MP2,5 (μg/m [3] ). Fase de Construcción.

......................................................................................................................................................... 105

Figura 3-62. Curva de Isoconcentración para Percentil 98 período 24 horas MP10 (μg/m [3] ). Fase de

Construcción.................................................................................................................................... 106

Figura 3-63. Curva de Isoconcentración para período anual MP10 (μg/m [3] ). Fase de Construcción.

......................................................................................................................................................... 107

Figura 3-64. Curva de Isodepositación para período mensual MPS (mg/m [2] /día). Fase de

Construcción.................................................................................................................................... 108

www.dfmconsultores.cl

**info@dfmconsultores.cl**

viii

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Figura 3-65. Curva de Isodepositación para período anual MPS (mg/m [2] /día). Fase de Construcción.

......................................................................................................................................................... 109

Figura 3-66. Curva de Isoconcentración para Percentil 99 periodo 1 hora CO (mg/m [3] ). Fase de

Construcción.................................................................................................................................... 110

Figura 3-67. Curva de Isoconcentración para Percentil 99 período 8 horas CO (mg/m [3] ). Fase de

Construcción.................................................................................................................................... 111

Figura 3-68. Curva de Isoconcentración para periodo anual NO 2 (μg/m [3] ). Fase de Construcción. 112

Figura 3-69. Curva de Isoconcentración para Percentil 99 periodo 1 hora NO 2 (μg/m [3] ). Fase de

Construcción.................................................................................................................................... 113

Figura 3-70. Curva de Isoconcentración para período anual SO 2 (μg/m [3] ). Fase de Construcción. . 114

Figura 3-71. Curva de Isoconcentración para Percentil 99 periodo 24 horas SO 2 (μg/m [3] ). Fase de

Construcción.................................................................................................................................... 115

Figura 3-72. Curva de Isoconcentración para Percentil 99 periodo 1 hora SO 2 (μg/m [3] ). Fase de

Construcción.................................................................................................................................... 116

Figura 4-1 - Área de influencia del Proyecto - Componente Aire. ................................................. 125

www.dfmconsultores.cl

**info@dfmconsultores.cl**

ix

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

### 1. INTRODUCCIÓN

El presente informe contiene la modelación de dispersión de contaminantes atmosféricos del

Proyecto “Parque Fotovoltaico Parina Solar”, de ahora en adelante mencionado como el Proyecto,

el cual corresponde a una nueva Central Solar Fotovoltaica destinada a la generación de energía

eléctrica a partir de tecnología solar, ubicada en la comuna de Calama, Provincia de El Loa, Región

de Antofagasta. La energía generada por el Proyecto será inyectada al Sistema Eléctrico Nacional, a

través de una línea de transmisión eléctrica (LTE) de 220 kV, para la que se considera una línea de

una extensión de 22,9 km hasta la S/E Calama, ubicada al noroeste del Proyecto.

A partir de las emisiones de contaminantes presentadas en el “Inventario de Emisiones Atmosféricas

Actualizado” (Anexo 7 de la presente Adenda) en conjunto con la información meteorológica y

topográfica disponible, se procedió a estimar la depositación de Material Particulado Sedimentable

(MPS) aportado por el Proyecto, así como también la concentración ambiental de Material

Particulado Respirable (MP10) y Material Particulado Respirable Fino (MP2,5). Además, se realizó la

estimación del aporte a la calidad del aire de los gases Monóxido de Carbono (CO), Dióxido de Azufre

(SO 2 ) y Dióxido de Nitrógeno (NO 2 ) en los receptores sensibles localizados en el entorno del

Proyecto.

A continuación, se presentan las características utilizadas en el modelo de dispersión y la

información meteorológica de entrada de dicho modelo con su análisis de incertidumbre respectivo,

además de la línea de base proyectada. Luego, se presentan los parámetros utilizados en la

modelación, los resultados obtenidos a partir de ella, y finalmente, las conclusiones relevantes del

estudio realizado.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

1

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

### 2. RESUMEN DE INVENTARIO DE EMISIONES ATMOSFÉRICAS

Conforme a lo señalado anteriormente, en la siguiente tabla se presentan las emisiones modeladas

correspondientes a aquellas generadas por la ejecución de la Fase de Construcción indicado en la

descripción del Proyecto, relacionadas al primer año de actividades descrito en el cronograma

establecido.

**Tabla 2-1 - Resumen de emisiones atmosféricas. Fase de Construcción.**

|ACTIVIDAD|EMISIONES [t/Año 1 Construcción]|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**ACTIVIDAD**|**MP2,5 **|**MP10 **|**MPS**|**CO**|**HC**|**SOx**|**NOx**|
|Movimiento de tierra|1,39|3,07|13,48|||||
|Tránsito por caminos no<br>pavimentados|0,35|3,51|12,34|||||
|Tránsito por caminos<br>pavimentados|0,38|1,68|8,75|||||
|Combustión vehículos<br>(Caminos No Pavimentados)|0,00|0,00|0,00|0,01|0,00|0,00|0,12|
|Combustión vehículos<br>(Caminos Pavimentados)|0,02|0,02|0,02|0,05|0,01|0,00|1,87|
|Combustión maquinarias|0,04|0,05|0,05|7,65|1,10|3,15|15,45|
|Grupo Electrógeno|0,22|0,22|0,22|0,68|0,26|0,21|3,18|
|**TOTAL**|**2,41**|**8,54**|**34,86**|**8,39**|**1,37**|**3,36**|**20,61**|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

2

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

### 3. MODELO DE CALIDAD DEL AIRE

En la siguiente sección, se presenta la información relevante respecto al modelo de calidad del aire

utilizado.

#### 3.1. Tipo de Modelo de Calidad del Aire Seleccionado

Los principales factores por considerar para la selección de un modelo de calidad del aire

corresponden al tipo de terreno presente en el área del proyecto, es decir, si es plano o complejo,

y el tipo de contaminante a emitir, si es primario o secundario. De acuerdo con lo recomendado en

la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, en el área de emplazamiento del

proyecto existen factores que podrían perturbar el carácter lineal de los vientos, por lo que es

necesario utilizar un modelo que permita simular una meteorología heterogénea. En consecuencia,

se ha seleccionado un modelo tipo _puff_ para la ejecución de la modelación de calidad del aire, el

cual se presentará en detalle en las siguientes secciones.

#### 3.2. Descripción del Modelo de Calidad del Aire Seleccionado - CALPUFF

Como se indicó anteriormente, en las áreas cercanas al emplazamiento del Proyecto se presentan

topografías complejas, las cuales podrían interferir en el carácter lineal de los vientos, por lo que se

ha seleccionado un modelo de calidad del aire del tipo _puff_, específicamente CALPUFF. Este consiste

en un modelo de libre disposición, el cual fue desarrollado por Research Corporation, siendo

Exponent [1] la empresa de soporte técnico actual.

CALPUFF es un modelo de dispersión de contaminantes, no estacionario y de multi-capa, capaz de

modelar múltiples especies. Puede simular los efectos del tiempo - y en el espacio - en diversas

condiciones meteorológicas en el transporte de contaminantes, y corresponde a un modelo

Lagrangiano-Gaussiano de transporte y dispersión de _puff_ emitidos por las fuentes emisoras

consideradas. Dentro de las capacidades del Modelo de Calidad del Aire, es posible destacar los

siguientes aspectos:

 - Simulación de procesos complejos: fumigación, estancamiento y recirculación.

 - Modelación de transporte de contaminantes de largo alcance.

 - Incorporación de efectos de terreno complejo en la dispersión de contaminantes.

1 [www.src.com/calpuff/calpuff1.htm](http://www.src.com/calpuff/calpuff1.htm)

www.dfmconsultores.cl

**info@dfmconsultores.cl**

3

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

 - Modelación de procesos de transformaciones químicas.

Asimismo, posee un módulo para realizar el post-procesamiento de datos, denominado CALPOST,

el cual calcula las concentraciones en los receptores de interés, permitiendo gestionar los datos para

cada contaminante según el período de tiempo requerido para el análisis.

#### 3.3. Características del Modelo de Dispersión de Contaminantes

**3.3.1.** **Dominio de Modelación**

En la Figura 3-1 se presenta el dominio de modelación, el cual corresponde a un área de 38 × 35

kilómetros, con celdas de 1.000 × 1.000 m.

Cabe señalar que, de forma adicional, se definió una grilla de receptores de acuerdo a lo

recomendado en la Guía para el Uso de Modelos de Calidad del Aire en el SEIA [(2)] . Para esto se

utilizaron 5 niveles de resolución:

 - Nivel 1: Espaciado de 20 metros en el perímetro del Parque Fotovoltaico, hasta una distancia

de 100 metros desde el centro de éste.

 - Nivel 2: Espaciado de 50 metros para los primeros 500 metros desde el centro del Parque

Fotovoltaico.

 - Nivel 3: Espaciado de 250 metros entre los 500 metros y 2 kilómetros desde el centro del

Parque Fotovoltaico.

 - Nivel 4: Espaciado de 500 metros entre los 2 kilómetros y los 5 kilómetros desde el centro

del Parque Fotovoltaico.

 - Nivel 5: Espaciado de 1.000 metros entre los 5 kilómetros y los 25 kilómetros desde el centro

del Parque Fotovoltaico.

Así, en la Figura 3-2 se presenta la ubicación de la grilla con respecto al Parque Fotovoltaico.

2 Guía para el Uso de Modelos de Calidad del Aire en el SEIA, SEA, 2023. Enlace web:
[https://sea.gob.cl/sites/default/files/imce/archivos/2023/02.FEB/28/Guia-Calidad-del-aire_V.4-final.pdf](https://sea.gob.cl/sites/default/files/imce/archivos/2023/02.FEB/28/Guia-Calidad-del-aire_V.4-final.pdf)

www.dfmconsultores.cl

**info@dfmconsultores.cl**

4

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-1 - Dominio de Modelación.**

Fuente: Elaboración propia.

5

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-2 - Ubicación Grilla de Receptores.**

Fuente: Elaboración propia.

6

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.3.2.** **Topografía del Sector**

La topografía del sector se ha extraído de Shuttle Radar Topography Mission, SRTM1, cuya

resolución es aproximadamente de 30 m. El archivo SRTM1 ha sido incorporado al modelo con el

objetivo de proporcionar la altura de los puntos de interés, lo cual se muestra en la Figura 3-3 con

la información utilizada.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

7

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-3 - Topografía del Dominio de Modelación.**

Fuente: Elaboración propia.

8

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

#### 3.4. Descripción del Modelo Meteorológico - WRF

Weather Research and Forecasting Model o WRF por sus siglas en inglés, es un sistema de

modelación atmosférico de mesoescala ampliamente usado a nivel mundial en contextos de

investigación y de pronósticos operacionales. En Chile, es el modelo numérico recomendado para

la generación de datos meteorológicos en la Guía para el Uso de Modelos de Calidad del Aire en el

SEIA (SEA, 2023).

El modelo utiliza una grilla tridimensional para representar la atmósfera y sus procesos (radiación

atmosférica, capa superficial y capa límite y procesos de formación de nubes y de precipitación,

entre otros) en distintas escalas espaciales, las cuales pueden variar desde las decenas de metros

hasta miles de kilómetros. Utiliza información de topografía y uso de suelo y de meteorología

observada o modelada proveniente de modelos meteorológicos globales para definir las

condiciones iniciales y de borde para la simulación de pronósticos meteorológicos.

A continuación, se describen las fuentes de la información suministrada y su tratamiento:

Topografía del dominio de modelación: Se ha utilizado información topográfica de alta resolución

proveniente del modelo Shuttle Radar Topography Mission, SRTM1, cuya resolución es

aproximadamente 30 m.

Uso de suelo: Se ha utilizado información de uso de suelos de alta resolución proveniente del

modelo Copernicus Global Land Service: Land Cover 100m con una resolución de 100 metros.

Meteorología proveniente de un modelo meteorológico global: Se han utilizado los resultados del

modelo ERA 5, año 2021. Este modelo corresponde a estimaciones horarias de una gran cantidad

de variables climáticas atmosféricas, terrestres y oceánicas. Los datos cubren la Tierra en una grilla

de aproximadamente 30 km de resolución y resuelven la atmósfera hasta una altura de 80 km

Los principales parámetros utilizados para la configuración del modelo meteorológico se presentan

a continuación en la Tabla 3-1, estos fueron seleccionados por su capacidad de adaptación a la

topografía compleja y a modelos de alta resolución (< 3 km). La configuración del modelo se

presenta en el Anexo 1. Archivos Digitales de Modelación (Sección 6 del presente Informe).

www.dfmconsultores.cl

**info@dfmconsultores.cl**

9

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Tabla 3-1. Configuración parámetros principales WRF.**

|Parámetro|Valor|
|---|---|
|**Dominio**|**Dominio**|
|Resolución horizontal|1 km|
|Proyección|Lambert|
|Número de niveles verticales|44|
|Niveles verticales (eta)|0.000000, 0.051578, 0.101822, 0.150735, 0.198315, 0.244562, 0.289477,<br>0.333059,0.375309,0.416226,0.455810,<br>0.494062,<br>0.530982,<br>0.566569,<br>0.600823, 0.633745, 0.665334, 0.695591, 0.724515, 0.752107, 0.778366,<br>0.803292, 0.826886, 0.849148, 0.870076, 0.889673, 0.907937, 0.923302,<br>0.937101, 0.949333, 0.960000, 0.969101, 0.976635, 0.982603, 0.987005,<br>0.989841, 0.991111, 0.992381, 0.993651, 0.994921, 0.996190, 0.997460,<br>0.998730, 1.000000,|
|**Física**|**Física**|
|Esquema de radiación|RRTMG-fast (Onda corta y larga)|
|Modelo de suelo|Modelo Noah Land Surface|
|Tratamiento de capa superficial|Revised MM5 surface layer|
|Parametrización de capa límite|Yonsei University|
|Esquema de convección|Kain-Fritsch|
|Microfísica de nubes y precipitación|WSM 3-class|
|**Dinámica**|**Dinámica**|
|Parametrización de turbulencia|Smagorinsky|
|Núcleo dinámico|EM (Advanced Mass) y No hidroestático|
|Advección|positiva-definitiva|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

10

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

#### 3.5. Caracterización de Clima del Área del Proyecto

La zona donde se emplazará el Proyecto se encuentra dentro de la comuna de Calama, Región de

Antofagasta, por ende, la descripción climática se circunscribe a esta zona.

Conforme con el documento “Climatología Regional” de la Dirección Meteorológica de Chile (DMC,

2001), en la faja costera de la región impera un clima desértico con nublados abundantes, siendo

los elementos climáticos sobresalientes la ausencia de precipitaciones, un alto porcentaje de días

con nublados matinales, humedad relativa elevada y temperaturas que presentan poca variación

diurna y estacional. Esta uniformidad se debe a la cercanía del océano, a la influencia moderadora

de la corriente de Humboldt y a la presencia del anticiclón semipermanente del Pacífico sur, que

genera estabilidad atmosférica.

Hacia el interior de la Región, donde está ubicada la ciudad de Calama, el clima se clasifica como

desértico marginal de altura y se caracteriza por una aridez extrema durante todo el año (las

precipitaciones no muestran un régimen marcado), ausencia de humedad y una carencia casi

absoluta de nubosidad, lo que deja vía libre a la radiación solar durante el día y a la emisión durante

la noche, las temperaturas en consecuencia presentan un ciclo diario con una significativa amplitud,

que bordea los 20°C en verano e invierno. En cuanto al ciclo anual, la amplitud térmica es cercana a

los 7°C.

La configuración térmica continúa manteniendo una marcada orientación longitudinal (ver Figura

3-4), aunque destacan algunos rasgos notables, como la cuenca del Salar de Atacama (al sureste de

Calama) que se presenta como una zona muy isotermal y la cordillera Domeyko, sobre los 69°W,

que se observa como una región de intenso gradiente zonal de temperatura, superior a los 7°C,

registrándose en el sector cordillerano andino los valores más bajos de la temperatura media anual;

la zona de los valles intermedios registros entre 8 y 16°C y en el sector ubicado en el litoral valores

entre los 16 y 18°C.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

11

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-4 - Campo de Isotermas. Región de Antofagasta.**

Fuente: Elaboración propia a partir de información digital obtenida de la web de Infraestructura de Datos

Geoespaciales de Chile (IDE CHILE, 2018).

www.dfmconsultores.cl

**info@dfmconsultores.cl**

12

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Respecto al espacio geográfico en el cual se emplaza el proyecto, el cual se encuentra a

aproximadamente 13 km al sureste del límite urbano de Calama, presenta temperaturas alrededor

de los 12°C.

**Figura 3-5 - Campo de Isoyetas. Región de Antofagasta.**

Fuente: Elaboración propia a partir de información digital obtenida de la web de Infraestructura de Datos

Geoespaciales de Chile (IDE CHILE, 2018).

www.dfmconsultores.cl

**info@dfmconsultores.cl**

13

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Respecto al espacio geográfico en el cual se emplaza el proyecto, el cual se encuentra ubicado hacia

el sureste de Calama, a 13 km con respecto al límite urbano de esa ciudad, presenta precipitaciones

que rondan los 10 mm.

Por otro lado, para visualizar la variación de las temperaturas y las precipitaciones a lo largo del año,

en la siguiente figura se presenta a modo referencial el climograma de Antofagasta, en donde se

aprecia que los meses de mayor pluviometría corresponden a julio, agosto y septiembre, los cuales

coinciden con los meses en donde se presentan las menores temperaturas a lo largo del año.

**Figura 3-6 - Climograma de Antofagasta.**

Fuente: “Climatología Regional” (DMC, 2001).

www.dfmconsultores.cl

**info@dfmconsultores.cl**

14

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Con respecto al clima, de acuerdo con la clasificación de Köppen, la Región de Antofagasta presenta

los siguientes subtipos climáticos:

 - ET: Clima de tundra.

 - ET (w): Clima de tundra de lluvia estival.

 - Bwh: Clima desértico cálido.

 - Bwh (s): Clima desértico cálido de lluvia invernal.

 - Bwk: Clima desértico frío.

 - Bwk (w): Clima desértico frío de lluvia estival.

 - Bwk (s): Clima desértico frío de lluvia invernal.

 - EF: Clima glacial.

 - EF (w): Clima glacial de lluvia estival.

 - Bsk: Clima semiárido.

 - Bsk (w): Clima semiárido de lluvia estival.

 - Bsk (s): Clima semiárido de lluvia invernal.

De esta forma, en la Figura 3-7 se presenta la clasificación climática para la Región de Antofagasta

conforme a los subtipos climáticos mencionados anteriormente. En dicha figura se puede apreciar

que el clima correspondiente a la zona en donde se emplaza el proyecto corresponde a un clima del

tipo desértico frío de lluvia estival, el cual se caracteriza por tener inviernos muy fríos y los veranos

templados o cálidos. Adicionalmente, las precipitaciones suelen ser escasas e irregulares.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

15

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-7 - Clasificación climática según Köppen. Región de Antofagasta.**

Fuente: Elaboración propia a partir de información digital obtenida de la web de Infraestructura de Datos

Geoespaciales de Chile (IDE CHILE, 2018).

www.dfmconsultores.cl

**info@dfmconsultores.cl**

16

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

#### 3.6. Caracterización Meteorológica del Área del Proyecto

En este inciso se presenta la caracterización de la meteorología observada y modelada para la

estación meteorológica relevante en este estudio.

**3.6.1.** **Meteorología de Superficie - Valores Observados**

La meteorología de superficie utilizada para caracterizar el área del Proyecto corresponde a los

registros horarios de temperatura, velocidad y dirección del viento, humedad relativa, presión

atmosférica, precipitación y radiación solar, entregados por la Estación Meteorológica Hospital El

Cobre, ubicada en la ciudad de Calama. En la Tabla 3-2 se resume la caracterización de las variables

mencionadas de dicha estación.

**Tabla 3-2 - Estación de Monitoreo Meteorológico.**

|Nombre Estación|Ubicación<br>(Comuna)|Coordenadas UTM<br>(Datum WGS 84<br>Huso 19)|Col4|Variables|Período|
|---|---|---|---|---|---|
|**Nombre Estación**|**Ubicación**<br>**(Comuna)**|**Este [m]**|**Norte [m]**|**Norte [m]**|**Norte [m]**|
|Hospital el Cobre|Calama|509.427|7.517.292|Temperatura|2017-2019|
|Hospital el Cobre|Calama|509.427|7.517.292|Dirección del Viento|2017-2019|
|Hospital el Cobre|Calama|509.427|7.517.292|Velocidad del Viento|2017-2019|
|Hospital el Cobre|Calama|509.427|7.517.292|Humedad Relativa|2017-2019|
|Hospital el Cobre|Calama|509.427|7.517.292|Presión Atmosférica|2017-2019|
|Hospital el Cobre|Calama|509.427|7.517.292|Precipitación|2017-2019|
|Hospital el Cobre|Calama|509.427|7.517.292|Radiación Solar|2017-2019|

Fuente: Elaboración propia.

Seguidamente, en la Figura 3-8 es posible observar la ubicación referencial de la estación de

monitoreo meteorológico Estación Hospital El Cobre con respecto a la zona de emplazamiento del

proyecto.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

17

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-8 - Ubicación Referencial estación de monitoreo meteorológico.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

18

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.6.1.1.** **Estación Hospital del Cobre**

_**3.6.1.1.1.**_ _**Velocidad y Dirección del Viento**_

A continuación, en la Tabla 3-3 se presenta el resumen de información para la variable Velocidad de

Viento, específicamente los promedios, máximos y mínimos anuales, además del porcentaje de

calmas correspondiente al porcentaje de tiempo en que la velocidad del viento es menor a 0,5 m/s,

para los años 2018 a 2020. Conforme a lo señalado en la “Guía para el Uso de Modelos de Calidad

del Aire en el SEIA”, las series de datos meteorológicos deben contener un 75% de datos válidos, lo

cual se cumple para el periodo en estudio.

**Tabla 3-3- Resumen de información Velocidad del Viento observada. Estación El Cobre.**

|Parámetro|Variable|Año|Col4|Col5|Trienio|
|---|---|---|---|---|---|
|**Parámetro**|**Variable**|**2018**|**2019**|**2020**|**2020**|
|Velocidad de<br>Viento (m/s)|Promedio|4,1|4,1|4,1|4,1|
|Velocidad de<br>Viento (m/s)|Máximo|8,8|10,4|10,6|8,8|
|Velocidad de<br>Viento (m/s)|Mínimo|0,1|0,1|0,1|0,1|
|Porcentaje de Calmas (%)|Porcentaje de Calmas (%)|1,1|1,0|1,3|1,1|
|Datos Válidos (%)|Datos Válidos (%)|99,9%|100,0%|99,8%|99,9%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

19

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_a._ _Series de Tiempo_

Para una visualización gráfica de los datos disponibles, en la Figura 3-9 se presenta la serie de tiempo

para la variable Velocidad del Viento durante el periodo comprendido entre enero de 2018 y

diciembre de 2020. En él es posible identificar que la mayoría de los valores se concentran entre los

0 m/s y 8 m/s, con valores excepcionales que alcanzan por sobre los 10 m/s.

**Figura 3-9 - Serie de tiempo para velocidad del viento. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

20

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

De igual manera, para una visualización gráfica de los datos disponibles, en la Figura 3-10 se

presenta la serie de tiempo para la variable dirección del viento, en la cual se observan mayores

concentraciones de los datos entre los 50° y 120°, como también entre los 250° y 270°.

**Figura 3-10 - Serie de tiempo para dirección del viento. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

21

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Para caracterizar la información anual registrada de las variables analizadas, en la Tabla 3-4, se

presenta la frecuencia de distribución para la velocidad y dirección del viento observada en las

figuras anteriores.

**Tabla 3-4 - Frecuencia de distribución, velocidad y dirección del viento. Estación Hospital del Cobre.**

|Dirección|Col2|Distribución Porcentual de Velocidad del Viento (m/s)|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Dirección**|**Dirección**|**0,50 - 2,10**|**2,10 - 3,60**|**3,60 - 5,70**|**5,70 - 8,80**|**8,80 - 11,10**|**>= 11,10**|**Total (%)**|
|348,75 - 11,25|N|0,50%|0,03%|0,01%|0,00%|0,00%|0,00%|0,62%|
|11,25 - 33,75|NNE|0,63%|0,11%|0,01%|0,00%|0,00%|0,00%|0,82%|
|33,75 - 56,25|NE|1,21%|1,11%|0,20%|0,01%|0,00%|0,00%|2,60%|
|56,25 - 78,75|ENE|2,18%|7,10%|4,03%|0,12%|0,00%|0,00%|13,50%|
|78,75 - 101,25|E|2,00%|8,07%|14,34%|3,97%|0,00%|0,00%|28,43%|
|101,25 - 123,75|ESE|1,07%|1,44%|1,32%|0,09%|0,00%|0,00%|3,99%|
|123,75 - 146,25|SE|0,83%|0,13%|0,00%|0,00%|0,00%|0,00%|1,06%|
|146,25 - 168,75|SSE|0,79%|0,07%|0,00%|0,00%|0,00%|0,00%|0,92%|
|168,75 - 191,25|S|0,80%|0,09%|0,00%|0,00%|0,00%|0,00%|0,95%|
|191,25 - 213,75|SSW|0,89%|0,33%|0,02%|0,00%|0,00%|0,00%|1,32%|
|213,75 - 236,25|SW|1,15%|1,06%|0,52%|0,11%|0,00%|0,00%|2,91%|
|236,25 - 258,75|WSW|1,28%|2,82%|6,94%|8,02%|0,01%|0,00%|19,15%|
|258,75 - 281,25|W|0,98%|2,52%|6,08%|8,89%|0,01%|0,00%|18,56%|
|281,25 - 303,75|WNW|0,72%|0,56%|0,98%|0,96%|0,01%|0,00%|3,30%|
|303,75 - 326,25|NW|0,43%|0,11%|0,16%|0,51%|0,04%|0,00%|1,30%|
|326,25 - 348,75|NNW|0,37%|0,05%|0,03%|0,02%|0,01%|0,00%|0,56%|
|Sub-Total|Sub-Total|15,83%|25,60%|34,66%|22,71%|0,09%|0,00%|98,89%|
|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|1,11%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

22

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_b._ _Ciclos Diarios_

En la Figura 3-11 se presenta el ciclo diario para la variable Velocidad del Viento, en donde se puede

observar que el valor mínimo de velocidad del viento se presenta a las 11:00 horas con un valor

promedio en torno a 2,3 m/s, posteriormente, la velocidad comienza a incrementar

sostenidamente, alcanzando las mayores intensidades de viento entre las 15:00 y las 16:00 horas,

con un promedio máximo aproximado de 6,3 m/s. Luego disminuye paulatinamente hasta alcanzar

un valor mínimo local entre las 22:00 y 23:00 horas de unos 2,5 m/s, y a partir de entonces la

velocidad aumenta gradualmente hasta alcanzar un máximo local a las 8:00 horas, para luego volver

a descender al mínimo del ciclo descrito inicialmente.

**Figura 3-11 - Ciclo diario de velocidad del viento. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

23

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

En la Figura 3-12 se presenta el ciclo diario de Dirección del Viento, en donde es posible observar

que durante la noche y la madrugada existe predominancia de vientos E y menores frecuencias de

vientos ENE y ESE. Por otro lado, a las 11:00 horas se presenta un cambio en la dirección del viento,

por lo que a partir de las 12:00 hasta las 21:00 horas la dirección del viento predominante es OSO y

O. Luego, a las 22:00 horas se observa nuevamente un cambio en las direcciones del viento

correspondientes a las indicadas para el período nocturno.

**Figura 3-12 - Ciclo diario dirección del viento. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

24

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_c._ _Ciclo Estacional_

En la Figura 3-13 se presenta el ciclo estacional de vientos observado, en el cual se puede apreciar

que las mayores intensidades de viento se producen entre los meses de octubre y febrero durante

el periodo diurno, específicamente entre las 14:00 y las 18:00 horas. Por el contrario, las menores

intensidades de viento se registran en los momentos de cambio de dirección dominante, es decir, a

las 11:00 horas y entre las 22:00 y 23:00 horas.

**Figura 3-13 - Ciclo estacional de vientos. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

25

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_**3.6.1.1.2.**_ _**Temperatura**_

En la siguiente sección, se presenta en resumen de la información registrada para la variable

meteorológica Temperatura en la estación Hospital del Cobre, así como su respectiva serie de

tiempo, ciclo diario y ciclo estacional observado. De esta forma, en la Tabla 3-5 se muestra la síntesis

de los datos de temperatura, tales como promedio, máximo y mínimo anual para el periodo en

estudio. De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA”, las series de datos meteorológicos deben contener un 75% de datos válidos, lo cual se cumple

para los años 2018, 2019 y 2020.

**Tabla 3-5 - Resumen de información Temperatura observada. Estación El Cobre.**

|Parámetro|Variable|Año|Col4|Col5|Trienio|
|---|---|---|---|---|---|
|**Parámetro**|**Variable**|**2018**|**2019**|**2020**|**2020**|
|Temperatura<br>(°C)|Promedio|14,9|15,3|15,2|15,14|
|Temperatura<br>(°C)|Máximo|29,0|29,2|28,5|29,18|
|Temperatura<br>(°C)|Mínimo|0,0|-3,8|-1,6|-3,75|
|Datos Válidos (%)|Datos Válidos (%)|99,9%|100,0%|99,9%|99,9%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia.

26

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_a._ _Serie de Tiempo_

A modo de verificación de la completitud de los datos, en la Figura 3-14 se presenta la serie de

tiempo para la variable meteorológica Temperatura correspondiente a los registros obtenidos

durante los meses de enero 2018 hasta diciembre de 2020. En ella es posible notar que los valores

se concentran entre los 5°C y los 25°C.

**Figura 3-14 - Serie de tiempo para la temperatura. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

27

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_b._ _Ciclo Diario_

En la Figura 3-15 se presenta el ciclo diario para la variable Temperatura, el cual muestra que las

menores temperaturas se registran durante el período nocturno y de madrugada, alcanzando

valores mínimos promedio aproximados a 7,5°C entre las 6:00 horas y las 7:00 horas. A partir de

esta última hora, la temperatura comienza a aumentar paulatinamente durante la mañana y horas

de la tarde hasta alcanzar un máximo promedio aproximado de 22°C entre las 14:00 y las 16:00

horas, para posteriormente descender en forma gradual hasta llegar a los valores nocturnos y de

madrugada descritos inicialmente.

**Figura 3-15 - Ciclo diario de temperatura. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

28

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

### _c. Ciclo Estacional_

En la Figura 3-16 se presenta el ciclo estacional de la Temperatura observada, en donde es posible

apreciar que las mayores temperaturas se presentan durante los meses comprendidos entre

octubre y marzo, específicamente en el periodo diurno, alcanzando los máximos valores entre las

de 14:00 y las 18:00 horas. Por otro lado, las menores temperaturas registradas se presentan

durante los meses de invierno, en particular, en las madrugadas de los meses de julio y agosto entre

las 05:00 a las 8:00 horas.

**Figura 3-16 - Ciclo estacional de temperatura. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

29

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_**3.6.1.1.3.**_ _**Humedad Relativa**_

A continuación, se presenta un resumen de la información registrada para la variable meteorológica

Humedad Relativa en la Estación Hospital del Cobre, como también su respectiva serie de tiempo,

ciclo diario y ciclo estacional observado. De esta forma, en la Tabla 3-6 se muestra la síntesis de los

datos utilizados para dicha variable, especificando promedios, máximos y mínimos anuales. De

acuerdo con lo establecido en la Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, las

series de datos meteorológicos deben contener un 75% de datos válidos, lo cual se cumple para el

periodo en estudio.

**Tabla 3-6 - Resumen de información Humedad Relativa observada. Estación El Cobre.**

|Parámetro|Variable|Año|Col4|Col5|Trienio|
|---|---|---|---|---|---|
|**Parámetro**|**Variable**|**2018**|**2019**|**2020**|**2020**|
|Humedad<br>Relativa (%)|Promedio|25,66|25,25|26,22|25,71|
|Humedad<br>Relativa (%)|Máximo|89,69|98,87|100,00|100,00|
|Humedad<br>Relativa (%)|Mínimo|0,39|0,41|0,41|0,39|
|% Datos Válidos|% Datos Válidos|99,8%|99,9%|99,9%|99,9%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

30

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_a._ _Serie de Tiempo_

A modo de verificación de la completitud de los datos, en la Figura 3-17 se presenta la serie de

tiempo para la variable meteorológica Humedad Relativa, que los valores más altos se registran en

los meses de verano, mientras que los valores menores se perciben durante los meses de invierno.

**Figura 3-17 - Serie de tiempo para la Humedad Relativa. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

31

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_b._ _Ciclo Diario_

En la Figura 3-18 se presenta el ciclo diario para la variable Humedad Relativa, en donde es posible

notar que los valores mínimos se registran durante el período diurno, alcanzando el punto más bajo

entre las 16:00 y las 17:00 horas, con un valor promedio de 15%. Posteriormente, la humedad

relativa comienza a aumentar de forma paulatina durante la tarde y noche hasta alcanzar un

máximo promedio aproximado de 38% a las 06:00 horas. Luego, la humedad relativa comienza a

descender de manera gradual hasta llegar a los valores diurnos descritos de manera inicial.

**Figura 3-18 - Ciclo diario de Humedad Relativa. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

32

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

### _c. Ciclo Estacional_

En la Figura 3-19 se presenta el ciclo estacional de la Humedad Relativa observada, en donde es

posible apreciar que los valores más bajos se presentan durante los meses de invierno, en particular

entre los meses de agosto y septiembre, alcanzando cifras mínimas entre las de 12:00 y las 17:00

horas. Por otro lado, los valores máximos de humedad relativa se obtienen en los meses de verano

en las horas de la madrugada, específicamente en el mes de febrero.

**Figura 3-19 - Ciclo estacional de Humedad Relativa. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

33

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_**3.6.1.1.4.**_ _**Presión Atmosférica**_

En el siguiente apartado, se presenta en resumen la información registrada para la variable

meteorológica Presión Atmosférica en la estación Hospital del Cobre, así como también su

respectiva serie de tiempo y ciclo estacional observado. De esta forma, en la Tabla 3-7 se muestra

la síntesis de los datos utilizados durante el estudio, estableciendo los promedios, valores máximos

y mínimos anuales para los años 2018, 2019 y 2020. Al igual que las variables anteriores, la serie de

datos meteorológicos para esta variable cumple con lo establecido por el SEIA para todos los años

mencionados.

**Tabla 3-7- Resumen de información Presión Atmosférica observada. Estación El Cobre.**

|Parámetro|Variable|Año|Col4|Col5|Trienio|
|---|---|---|---|---|---|
|**Parámetro**|**Variable**|**2018**|**2019**|**2020**|**2020**|
|Presión<br>Atmosférica<br>(hPa)|Promedio|775,3|775,3|775,5|775,4|
|Presión<br>Atmosférica<br>(hPa)|Máximo|780,6|779,4|780,6|780,6|
|Presión<br>Atmosférica<br>(hPa)|Mínimo|768,8|771,0|770,8|768,8|
|% Datos Válidos|% Datos Válidos|99,9%|100,0%|99,8%|99,9%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia.

34

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_a._ _Serie de Tiempo_

A modo de verificación de la completitud de los datos, en la Figura 3-20 se presenta la serie de

tiempo para la variable meteorológica Presión Atmosférica a partir de los datos registrados entre

enero de 2018 y diciembre de 2020. En ella se puede identificar que la mayoría de los valores se

concentran entre los 772 mmHg y los 778 mmHg, con algunas excepciones durante los meses de

invierno que superan los 780 mmHg.

**Figura 3-20 - Serie de tiempo para la Presión Atmosférica. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

35

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_b._ _Ciclo Estacional_

En la Figura 3-21 se presenta el ciclo estacional de la Presión Atmosférica observada, en donde se

aprecia la variabilidad de este parámetro durante el día y el año. En general, es posible identificar

que los valores mínimos se registran durante el transcurso del día en los meses de verano entre las

16:00 y 18:00 horas, mientras que los valores máximos se presentan en los meses de invierno

durante las 22:00 a 01:00 horas y las 9:00 a 12:00 horas.

**Figura 3-21 - Ciclo estacional de Presión Atmosférica. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

36

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_**3.6.1.1.5.**_ _**Precipitación**_

A continuación, se presenta en resumen de la información registrada para la variable meteorológica

Precipitación en la Estación Hospital del Cobre, correspondiente a la serie de tiempo de los valores

mensuales.

_a._ _Serie de Tiempo_

En la Figura 3-22 se presenta la serie para la variable meteorológica Precipitación, en donde se

observa que los meses de precipitación son variados, pero principalmente se registran valores más

altos durante los meses de verano, específicamente entre los meses de enero y febrero. Sin

embargo, existen algunas cifras destacables durante el periodo de invierno de los años 2019 y 2020.

**Figura 3-22. Serie de tiempo para la Precipitación. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

37

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_**3.6.1.1.6.**_ _**Radiación Solar**_

A continuación, se presenta en resumen la información registrada para la variable meteorológica

Radiación Solar en la Estación Hospital del Cobre, como también su respectiva serie de tiempo, ciclo

diario y ciclo estacional observado. De esta manera, en la Tabla 3-8 se muestra la síntesis de los

datos utilizados para el estudio, específicamente los valores promedios, máximos y mínimos

registrados para los años en evaluación. Por otro lado, al igual que las variables meteorológicas

anteriores, se cumple con el porcentaje de datos válidos para los años 2018, 2019 y 2020 conforme

a lo establecido por el SEIA.

**Tabla 3-8- Resumen de información Radiación Solar observada. Estación El Cobre.**

|Parámetro|Variable|Año|Col4|Col5|Trienio|
|---|---|---|---|---|---|
|**Parámetro**|**Variable**|**2018**|**2019**|**2020**|**2020**|
|Radiación Solar<br>(W/m2)|Promedio|284,7|281,7|280,7|282,3|
|Radiación Solar<br>(W/m2)|Máximo|1.143,0|1.153,6|1.129,0|1.153,6|
|Radiación Solar<br>(W/m2)|Mínimo|0,0|0,0|0,0|0,0|
|% Datos Válidos|% Datos Válidos|99,7%|99,9%|99,9%|99,8%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia.

38

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_a._ _Serie de Tiempo_

A modo de verificación de la completitud de los datos, en la

Figura 3-23 se presenta la serie de tiempo para la variable meteorológica Radiación Solar, en donde

se puede identificar una clara periodicidad de los valores para cada año, situación propia de la

radiación solar.

**Figura 3-23 - Serie de tiempo para la Radiación Solar. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

39

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_b._ _Ciclo Diario_

En la Figura 3-24 se presenta el ciclo diario para la variable Radiación Solar, en donde se pueden

visualizar los valores registrados durante horas de la madrugada hasta inicios del periodo nocturno.

En este intervalo la radiación solar aumenta de manera gradual hasta alcanzar su máximo valor

promedio de 920 [W/m2] a las 13:00 horas, para luego disminuir hacia valores nulos que se

mantienen hasta las 6:00, hora en la cual comienza nuevamente el ciclo descrito.

**Figura 3-24 - Ciclo diario de Radiación Solar. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

40

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

### _c. Ciclo Estacional_

En la Figura 3-25 se presenta el ciclo estacional de la Radiación Solar observada, en donde es posible

apreciar que las mayores radiaciones se presentan durante los meses de verano en el periodo

diurno, alcanzando valores máximos entre las de 12:00 y las 14:00 horas. Por otro lado, la mayor

extensión de los valores nulos de Radiación Solar se presenta durante los meses de invierno, en

particular en el mes de junio, en donde el periodo se extiende entre las 19:00 y 8:00 horas.

**Figura 3-25 - Ciclo estacional de Radiación Solar. Estación Hospital del Cobre.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

41

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.6.2.** **Meteorología de Superficie - Valores Modelados**

En el siguiente apartado se presenta el análisis de las variables meteorológicas modeladas

mencionadas anteriormente. Los datos corresponden a los valores extraídos del modelo

meteorológico WRF (Weather Research and Forecasting) desarrollado para el año 2019 y la

meteorología de superficie utilizada para caracterizar el área del Proyecto corresponde a los valores

horarios de temperatura, velocidad y dirección del viento, en la ubicación de la Estación

Meteorológica Hospital del Cobre.

**3.6.2.1.** **Estación Hospital del Cobre**

_**3.6.2.1.1.**_ _**Velocidad y Dirección del Viento**_

En la Tabla 3-9 se presenta el resumen de información para la variable velocidad viento; promedio,

máximo y mínimo además del porcentaje de calmas, el cual se define como el porcentaje del tiempo

en que la velocidad del viento es menor 0,5 m/s para el período en estudio. Dado que los datos son

provenientes de un Modelo Meteorológico se cuenta con la totalidad de los valores de la serie.

**Tabla 3-9- Resumen de Información Velocidad del Viento año 2019. Estación Hospital El Cobre.**

|Parámetro|Variable|Valor|
|---|---|---|
|Velocidad de Viento<br>[m/s]|Promedio|3,35|
|Velocidad de Viento<br>[m/s]|Máximo|15,98|
|Velocidad de Viento<br>[m/s]|Mínimo|0,04|

Fuente: Elaboración propia.

A continuación, se presentan las series de tiempo, ciclos diarios y ciclo estacional modelados para

las variables meteorológicas Velocidad y Dirección del Viento.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

42

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_a._ _Series de Tiempo_

Para una visualización gráfica de los datos disponibles, en las siguientes figuras se presentan las

series de tiempo para las variables Velocidad y Dirección del Viento modelados en la Estación

Hospital del Cobre el año 2019. En ellas, es posible identificar que la mayoría de los valores se

concentran entre los 0 m/s y 8 m/s.

**Figura 3-26 - Serie de tiempo de velocidad del viento modelado en Estación Hospital del Cobre, año 2019.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

43

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-27 - Serie de tiempo de dirección del viento modelado en Estación Hospital del Cobre, año 2019.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

44

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

De esta forma, para caracterizar la información anual modelada de ambas variables, en la Tabla

3-10se presenta la frecuencia de distribución para la Velocidad y Dirección del Viento modelada.

**Tabla 3-10 - Frecuencia de distribución de velocidad y dirección del viento modelados en Estación Hospital**

**del Cobre, año 2019.**

|Dirección|Col2|Distribución Porcentual de Velocidad del Viento (m/s)|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Dirección**|**Dirección**|**0,50 - 2,10**|**2,10 - 3,60**|**3,60 - 5,70**|**5,70 - 8,80**|**8,80 - 11,10**|**>= 11,10**|**Total (%)**|
|348,75 - 11,25|N|0,47%|0,01%|0,00%|0,00%|0,00%|0,00%|0,48%|
|11,25 - 33,75|NNE|0,81%|0,07%|0,01%|0,01%|0,00%|0,00%|0,90%|
|33,75 - 56,25|NE|2,26%|0,71%|0,03%|0,00%|0,00%|0,00%|3,00%|
|56,25 - 78,75|ENE|7,85%|4,70%|0,26%|0,00%|0,00%|0,00%|12,82%|
|78,75 - 101,25|E|6,70%|10,67%|6,26%|0,11%|0,00%|0,00%|23,74%|
|101,25 - 123,75|ESE|1,23%|0,27%|0,30%|0,01%|0,00%|0,00%|1,82%|
|123,75 - 146,25|SE|0,81%|0,02%|0,00%|0,00%|0,00%|0,00%|0,83%|
|146,25 - 168,75|SSE|0,78%|0,05%|0,00%|0,00%|0,00%|0,00%|0,82%|
|168,75 - 191,25|S|0,95%|0,07%|0,00%|0,01%|0,00%|0,00%|1,03%|
|191,25 - 213,75|SSW|1,47%|0,18%|0,05%|0,00%|0,00%|0,00%|1,70%|
|213,75 - 236,25|SW|2,01%|0,89%|0,22%|0,06%|0,00%|0,00%|3,17%|
|236,25 - 258,75|WSW|2,82%|3,18%|13,14%|7,44%|0,03%|0,00%|26,62%|
|258,75 - 281,25|W|1,97%|1,97%|5,09%|6,05%|0,03%|0,00%|15,13%|
|281,25 - 303,75|WNW|1,20%|0,62%|1,18%|1,16%|0,06%|0,01%|4,22%|
|303,75 - 326,25|NW|0,49%|0,09%|0,06%|0,18%|0,08%|0,06%|0,96%|
|326,25 - 348,75|NNW|0,31%|0,01%|0,01%|0,00%|0,00%|0,00%|0,33%|
|Sub-Total|Sub-Total|32,13%|23,53%|26,60%|15,05%|0,21%|0,07%|97,58%|
|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|2,42%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

45

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_b._ _Ciclos Diarios_

En la siguiente figura se presenta el ciclo diario para la variable Velocidad del Viento, donde se puede

observar que el valor mínimo de velocidad del viento se presenta a las 11:00 horas con un valor

promedio en torno a 2,3 m/s, posteriormente, la velocidad comienza a incrementar

sostenidamente, alcanzando las mayores intensidades de viento entre las 15:00 y las 16:00 horas,

con un promedio máximo aproximado de 6,3 m/s. Luego, la intensidad disminuye paulatinamente

hasta alcanzar un valor mínimo local a las 22:00 horas de unos 2,5 m/s, y a partir de entonces, la

velocidad aumenta gradualmente hasta alcanzar un máximo local entre las 7:00 y las 8:00 horas,

para luego volver a descender al mínimo del ciclo descrito inicialmente.

**Figura 3-28 - Ciclo Diario de Velocidad del Viento modelado en Estación Hospital del Cobre, año 2019.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

46

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

En la siguiente figura se presenta el ciclo diario para la variable Dirección del Viento, en la cual se

puede observar que durante la noche y la madrugada existe predominancia de vientos E. Por otro

lado, a las 10:00 horas se presenta un cambio en la dirección del viento, el cual se prolonga hasta

las 21:00 horas con vientos de direcciones predominantes OSO y O. Luego, a las 22:00 horas se

observa nuevamente un cambio en las direcciones de viento correspondiente a las indicadas para

el periodo nocturno.

**Figura 3-29 - Ciclo Diario de Dirección de Viento modelado en Estación Hospital del Cobre, año 2019.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

47

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_c._ _Ciclo Estacional_

En la siguiente figura se presenta el ciclo estacional de vientos modelado, en donde es posible

apreciar que el modelo estima las mayores intensidades de viento en los meses de octubre a febrero

durante el periodo diurno, específicamente entre las 14:00 y las 19:00 horas. Por el contrario, las

menores intensidades de viento son calculadas para el período nocturno durante los meses cálidos.

**Figura 3-30 - Ciclo Estacional de Vientos modelado en Estación Hospital del Cobre, año 2019.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

48

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_**3.6.2.1.2.**_ _**Temperatura**_

En la Tabla 3-11 se presenta el resumen de información para la variable Temperatura; promedio,

máximo y mínimo. Dado que los datos son provenientes de un Modelo Meteorológico, se cuenta

con la totalidad de los valores de la serie.

**Tabla 3-11 - Resumen de Información Temperatura modelada en Hospital El Cobre, año 2019.**

|Parámetro|Variable|Valor|
|---|---|---|
|Temperatura [°C]|Promedio|14,79|
|Temperatura [°C]|Máximo|26,360|
|Temperatura [°C]|Mínimo|-1,630|

Fuente: Elaboración propia.

A continuación, se presentan la serie de tiempo, ciclo diario y ciclo estacional modelados para la

variable meteorológica temperatura.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

49

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_a._ _Series de Tiempo_

Para una visualización gráfica de los datos disponibles, en la siguiente figura se presenta la serie de

tiempo para la variable meteorológica Temperatura modelada en Hospital El Cobre para el año

2019. En ella es posible observar que la mayoría de los valores calculados por el modelo se

concentran entre los 5°C y los 25°C.

**Figura 3-31 - Serie de Tiempo Temperatura modelada en Hospital El Cobre, año 2019.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

50

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_b._ _Ciclo Diario_

En la siguiente figura se presenta el ciclo diario para la variable Temperatura, modelada en Hospital

El Cobre para el año 2019. Como se puede apreciar, el modelo determina que las temperaturas más

bajas ocurren durante el período nocturno y de madrugada, estimando un valor mínimo promedio

aproximado de 7 °C a las 6:00 horas. Posteriormente, el modelo calcula un aumento de temperatura

hasta alcanzar un máximo promedio aproximado de 22°C entre las 14:00 y las 16:00 horas, para

posteriormente descender en forma gradual hasta llegar a los valores nocturnos y de madrugada

descritos inicialmente.

**Figura 3-32 - Ciclo Diario Temperatura modelada en Hospital El Cobre, año 2019.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

51

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_c._ _Ciclo Estacional_

En la Figura3-28 se presenta el ciclo estacional de la temperatura modelada en Hospital El Cobre

para el año 2019, en la cual se observa que las mayores temperaturas son calculadas durante los

meses de verano en el periodo diurno, alcanzando los valores máximos entre las 14:00 y 18:00

horas. Por otro lado, las menores temperaturas se obtienen en los meses de invierno, en particular,

en la madrugada y horas de la mañana en el mes de julio entre las 04:00 y las 07:00 horas.

**Figura 3-33 - Ciclo Estacional de Temperatura modelada en Hospital El Cobre, año 2019.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

52

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.6.3.** **Meteorología de Altura - Valores Observados**

Con relación a la meteorología de altura, no existen registros de mediciones disponibles en la

estación meteorológica utilizada, pues en ella no se realizan radiosondeos.

**3.6.4.** **Meteorología de Altura - Valores Modelados**

La altura de capa de mezcla corresponde a la altura medida desde la superficie en la que la

inestabilidad favorece la dispersión vertical de contaminantes. En consecuencia, se ha caracterizado

la variable altura de la capa de mezcla, la cual corresponde a un parámetro obtenido del

procesamiento de los resultados de modelo meteorológico WRF.

Para lo anterior, se han tomado los datos entregados por el modelo meteorológico WRF en la

ubicación de la estación meteorológica mencionada. A continuación, se presentan los valores

entregados por el modelo.

**3.6.4.1.** **Altura de Capa de Mezcla**

En la Tabla 3-12 se presenta el resumen de información para la variable altura de capa de mezcla

con el promedio, máximo y mínimo para el periodo en estudio. Dado que los datos son provenientes

de un Modelo Meteorológico se cuenta con la totalidad de los valores de la serie.

**Tabla 3-12 - Resumen de Información Altura de Capa de Mezcla modelada en Estación Hospital El Cobre,**

**año 2019.**

|Parámetro|Variable|Valor|
|---|---|---|
|Altura de Capa de Mezcla [m]|Promedio|539|
|Altura de Capa de Mezcla [m]|Máxima|3298|
|Altura de Capa de Mezcla [m]|Mínima|10|

Fuente: Elaboración propia

De igual manera, se presentan las series de tiempo, ciclo diario y ciclo estacional modelados para la

variable meteorológica altura de capa de mezcla.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

53

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

#### _3.6.4.1.1. Series de Tiempo_

Para una visualización gráfica de los datos disponibles, en la Figura 3-34 se presenta la serie de

tiempo para la variable altura de capa de mezcla.

**Figura 3-34 - Serie de Tiempo Altura de Capa de Mezcla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

54

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_**3.6.4.1.2.**_ _**Ciclo Diario**_

En la Figura 3-35 se muestra el ciclo diario para la variable altura de capa de mezcla modelada en la

Estación Hospital El Cobre. En él es posible distinguir que el modelo calcula los valores más bajos

durante el periodo nocturno y de madrugada. Así, a partir de las 06:00 horas la magnitud de la altura

de capa de mezcla comienza a aumentar sostenidamente hasta alcanzar un máximo promedio

aproximado de 1.450 metros a las 16:00 horas. Posteriormente, esta comienza a descender hasta

alcanzar los valores nocturnos mencionados inicialmente.

**Figura 3-35 - Ciclo Diario Altura de Capa de Mezcla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

55

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

_**3.6.4.1.3.**_ _**Ciclo Estacional**_

En la Figura 3-36 se presenta el ciclo estacional para la variable altura de capa de mezcla, donde se

puede observar que durante el periodo nocturno y de madrugada se presentan los menores valores

de esta variable durante todo el año. Por el contrario, los valores máximos se presentan durante los

meses de verano, particularmente en horas de la tarde.

**Figura 3-36 - Ciclo Estacional Altura de Capa de Mezcla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

56

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

#### 3.7. Análisis de Incertidumbre

En las siguientes secciones se presenta la comparación cualitativa y cuantitativa entre los datos

observados y los resultados del modelo meteorológico, esto con el fin de determinar la

incertidumbre de este último. De esta forma, en vista de que la meteorología de superficie es un

factor relevante en la dispersión de los contaminantes, en el presente inciso se busca validar en

forma cualitativa el modelo WRF que será utilizado como información base de entrada al modelo

de dispersión CALPUFF.

**3.7.1.** **Comparación Cualitativa**

**3.7.1.1.** **Velocidad y Dirección del Viento**

En las siguientes figuras, se presenta una comparación cualitativa de las variables meteorológicas

velocidad y dirección del viento, observadas y modeladas.

En la Figura 3-37 se observa la comparación de los ciclos diarios de dirección del viento para el

periodo en estudio, en donde se puede apreciar la gran similitud en las direcciones de viento y en

su frecuencia, coincidiendo en sus componentes, como son las direcciones OSO y O durante el día,

como también en las direcciones que se presentan en el periodo nocturno, particularmente las

direcciones E y ENE.

**Figura 3-37 - Comparación de Ciclos Diarios de Dirección del Viento, Estación Hospital del Cobre.**

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia

En la Figura 3-38 se muestra la comparativa de los ciclos diarios de velocidad del viento para el

periodo en estudio, la cual grafica la similitud que existe entre ambos ciclos, observándose una

coincidencia en la intensidad y en las horas en que se presentan los valores máximos ocurridos en

www.dfmconsultores.cl

**info@dfmconsultores.cl**

57

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

las primeras horas de la tarde. Sin embargo, es posible notar algunas diferencias durante el periodo

nocturno dado que existe una cierta subestimación de la intensidad del viento.

**Figura 3-38 - Comparación del Ciclo Diario de la Velocidad del Viento, Estación Hospital del Cobre.**

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia.

En la Figura 3-39 se expone la comparativa de los Ciclos Estacionales de Viento, en donde es posible

apreciar bastante similitud entre las intensidades de viento, así como también en las direcciones de

viento a lo largo del año y en las distintas horas del día. Sin embargo, se puede notar que el modelo

tiende a subestimar los valores máximos tanto en el periodo diurno como nocturno.

**Figura 3-39 - Comparación del Ciclo Estacional de la Velocidad y Dirección del Viento, Estación Hospital**

**del Cobre.**

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia

www.dfmconsultores.cl

**info@dfmconsultores.cl**

58

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.7.1.2.** **Temperatura**

En la Figura 3-40 se presenta la comparación de los ciclos diarios de temperatura atmosférica para

el periodo en estudio, en la cual se muestra un muy buen acuerdo en términos tanto de la fase como

de la amplitud entre ambos ciclos, observándose que los momentos de mínima y máxima son

coincidentes.

**Figura 3-40 - Comparación del Ciclo Diario de la Temperatura, Estación Hospital del Cobre.**

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

59

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Por su parte, en la Figura 3-41 se presenta la comparación del Ciclo Estacional de Temperatura para

el periodo en estudio, en la cual se puede apreciar que el modelo representa de muy buena manera

la fase de cada ciclo, tanto diario como anual, con sus respectivos mínimos y máximos. Sin embargo,

el modelo presenta una leve subestimación de los valores máximos que se presentan durante el día,

y en particular en los meses de verano.

**Figura 3-41 - Comparación del Ciclo Estacional de Temperatura, Estación Hospital del Cobre.**

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia

www.dfmconsultores.cl

**info@dfmconsultores.cl**

60

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.7.2.** **Comparación Cuantitativa**

Para realizar la comparación cuantitativa se han utilizado tres estadígrafos comúnmente empleados

para la evaluación del desempeño de modelos: sesgo, error cuadrático medio (ECM) y el coeficiente

de correlación (r). Dichos estadígrafos fueron calculados para los ciclos diarios, de tal manera de

poder cuantificar el desempeño del modelo para el conjunto de datos del periodo. A continuación,

en la Tabla 3-13 se presenta el valor obtenido de los estadígrafos.

**Tabla 3-13 - Estadígrafos de Dispersión para Velocidad del Viento y Temperatura.**

|Medida de Error|Estación Hospital del Cobre|Col3|
|---|---|---|
|**Medida de Error**|**Velocidad del Viento**|**Temperatura**|
|Sesgo|-0,73 m/s|-0,55 °C|
|ECM|1,06 m/s|1,10 °C|
|r|0,85|0,99|

Fuente: Elaboración propia.

Respecto a las medidas de dispersión presentadas en la tabla anterior, se muestra que el modelo

representa de manera satisfactoria las variables velocidad del viento y temperatura. En el primer

caso, el sesgo y el error cuadrático medio indican una subestimación por parte del modelo de 1,06

m/s en promedio, mientras que el coeficiente de correlación es de un 85%. En el caso de la

temperatura, se observa un error cuadrático cercano a un grado, con un sesgo que indica una leve

subestimación de la variable, mientras que al mismo tiempo se observan altos valores para el

coeficiente de correlación (99%).

Dados los valores de estadígrafos de dispersión para velocidad del viento y temperatura, los cuales

manifiestan un buen desempeño del modelo meteorológico WRF, no se considera pertinente

realizar correcciones a los resultados obtenidos a través del modelo CALPUFF.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

61

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

#### 3.8. Evolución Cambio Climático en el Área del Proyecto

De acuerdo a la Ley N°21.455 o Ley Marco de Cambio Climático [(3)], publicada el 13 de junio de 2022,

y conforme a la “Guía Metodológica para la consideración del cambio climático en el SEIA” [(3)],

publicada el 16 de enero de 2023, surge la necesidad de considerar la variable de cambio climático

en los componentes del medio ambiente que resulten pertinentes en el marco del Sistema de

Evaluación de Impacto Ambiental (SEIA).

De este modo, para evaluar la variación del cambio climático en la zona donde se emplazará el

proyecto, se ha utilizado la información disponible en el Explorador de Amenazas Climáticas,
específicamente la herramienta ARClim [(4)], con el fin de visualizar y analizar los principales índices

climáticos actuales y futuros (considerando un plazo de 12 a 42 años), estableciendo la diferencia

entre ellos.

A continuación, en la Tabla 3-14, se presentan los índices de temperatura media anual, precipitación

acumulada anual y velocidad viento promedio anual, analizados para la comuna de Calama.

**Tabla 3-14. Principales índices evaluación cambio climático. Región de Antofagasta, provincia El Loa,**

**comuna de Calama.**

|Índice|Periodo|Valor|
|---|---|---|
|Temperatura media anual (°C)|Presente|8,32|
|Temperatura media anual (°C)|Futuro|10,47|
|Temperatura media anual (°C)|Cambio (Futuro - Presente)|2,15|
|Precipitación acumulada anual (mm)|Presente|83,84|
|Precipitación acumulada anual (mm)|Futuro|88,30|
|Precipitación acumulada anual (mm)|Cambio (Futuro - Presente)|4,45|
|Velocidad viento promedio anual (m/s)|Presente|4,75|
|Velocidad viento promedio anual (m/s)|Futuro|4,79|
|Velocidad viento promedio anual (m/s)|Cambio (Futuro - Presente)|0,03|

Fuente: Elaboración propia, en base a datos climáticos anuales por comuna [(4)] .

3 [Link web Ley Marco de Cambio Climático: https://www.bcn.cl/leychile/navegar?idNorma=1177286](https://www.bcn.cl/leychile/navegar?idNorma=1177286)
4 [ARClim, herramienta “Explorador de Amenazas Climáticas”. Acceso desde: https://arclim.mma.gob.cl/amenazas/](https://arclim.mma.gob.cl/amenazas/)

www.dfmconsultores.cl

**info@dfmconsultores.cl**

62

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Así, de la tabla precedente se puede observar que, en la comuna de Calama, que es donde se

localizará el proyecto en estudio, se identifica una diferencia de temperatura media anual entre los

valores futuros con respecto a los valores actuales de 2,15 °C, lo cual corresponde a un aumento del

25,84% de las temperaturas, dentro de los próximos 12 a 42 años.

Por su parte, con respecto a las precipitaciones acumuladas anuales, es posible observar una

diferencia de 4,45 mm, lo que corresponde a un incremento del 5,31% de los registros anuales de

precipitación futuros, con respecto a los valores actuales.

Por último, en cuanto a la velocidad media anual del viento, se observa que presentará una variación

de 0,03 m/s, lo que corresponde a un aumento del 0,70% del valor actual registrado.

A continuación, de forma complementaria e ilustrativa, en las Figura 3-42, Figura 3-43 y Figura 3-44

se presenta la comparación entre la situación actual y futura de las variables de temperatura media

anual, precipitaciones acumuladas anuales y velocidad del viento promedio anual, respectivamente,

correspondientes a la Región de Antofagasta.

Cabe señalar que, dado que en las Figura 3-43 y Figura 3-44 las variaciones de precipitación

acumulada anual y de velocidad media anual del viento, respectivamente, son leves e incluso

prácticamente imperceptibles para los rangos establecidos, se presetnan las Figura 3-45 y Figura

3-46, donde se observa ilustrativamente las evoluciones, en porcentaje, entre la situación actual y

futura de estas variables.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

63

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-42. Comparación Temperatura Media Anual entre situación actual y futura. Región de**

**Antofagasta.**

Fuente: Elaboración Propia a partir de información digital obtenida de la web de ARClim, “Explorador de

Amenazas Climáticas” [(4)] .

www.dfmconsultores.cl

**info@dfmconsultores.cl**

64

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-43. Comparación Precipitación Acumulada Anual entre situación actual y futura. Región de**

**Antofagasta.**

Fuente: Elaboración Propia a partir de información digital obtenida de la web de ARClim, “Explorador de

Amenazas Climáticas” [(4)] .

www.dfmconsultores.cl

**info@dfmconsultores.cl**

65

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-44. Comparación Velocidad Media Anual Viento entre situación actual y futura. Región de**

**Antofagasta.**

Fuente: Elaboración Propia a partir de información digital obtenida de la web de ARClim, “Explorador de

Amenazas Climáticas” [(4)] .

www.dfmconsultores.cl

**info@dfmconsultores.cl**

66

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-45. Evolución Precipitación Acumulada Anual. Región de Antofagasta.**

Fuente: Elaboración Propia a partir de información digital obtenida de la web de ARClim, “Explorador de

Amenazas Climáticas” [(4)] .

www.dfmconsultores.cl

**info@dfmconsultores.cl**

67

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-46. Evolución Velocidad Media Anual Viento. Región de Antofagasta.**

Fuente: Elaboración Propia a partir de información digital obtenida de la web de ARClim, “Explorador de

Amenazas Climáticas” [(4)] .

www.dfmconsultores.cl

**info@dfmconsultores.cl**

68

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

#### 3.9. Normas de Calidad del Aire

En la Tabla 3-15 se presentan las normativas de calidad del aire de los contaminantes de interés

para el proyecto: Material Particulado Respirable Fino (MP2,5), Material Particulado Respirable

(MP10), Material Particulado Sedimentable (MPS), Monóxido de Carbono (CO), Dióxido de

Nitrógeno (NO 2 ) y Dióxido de Azufre (SO 2 ).

**Tabla 3-15 - Normas de calidad del aire.**

|Contaminante|Decreto<br>Aplicable|Norma|Col4|Periodo de Evaluación de Cumplimiento de<br>Norma|
|---|---|---|---|---|
|**Contaminante**|**Decreto**<br>**Aplicable**|**Valor**|**Unidad**|**Unidad**|
|Material Particulado<br>Respirable Fino<br>(MP2,5)|Decreto Supremo<br>N°12/2011|50|μg/m3|Percentil 98 de la media aritmética diaria durante<br>un año.|
|Material Particulado<br>Respirable Fino<br>(MP2,5)|Decreto Supremo<br>N°12/2011|20|20|Media aritmética trianual|
|Material Particulado<br>Respirable (MP10)|Decreto Supremo<br>N°12/2021|130|μg/m3N|Percentil 98 de la media aritmética diaria durante<br>un año.|
|Material Particulado<br>Respirable (MP10)|Decreto Supremo<br>N°12/2021|50|50|Media aritmética trianual.|
|Dióxido de<br>nitrógeno (NO2)|Decreto Supremo<br>No114/2002|400|μg/m3N|Percentil 99 de la media aritmética horaria<br>durante un año.|
|Dióxido de<br>nitrógeno (NO2)|Decreto Supremo<br>No114/2002|100|100|Media aritmética trianual.|
|Dióxido de azufre<br>(SO2)|Decreto Supremo<br>N°104/2019|350|μg/m3N|Percentil 99 de las concentraciones de 1 hora.|
|Dióxido de azufre<br>(SO2)|Decreto Supremo<br>N°104/2019|150|150|Percentil 99 de las concentraciones de 24 horas|
|Dióxido de azufre<br>(SO2)|Decreto Supremo<br>N°104/2019|60|60|Concentración anual|
|Monóxido de<br>Carbono (CO)|Decreto Supremo<br>N°115/2002|30|mg/m3N|Percentil 99 de la media aritmética horaria<br>durante un año.|
|Monóxido de<br>Carbono (CO)|Decreto Supremo<br>N°115/2002|10|10|Percentil 99 de la media aritmética de 8 horas<br>durante un año.|
|Material Particulado<br>Sedimentable (MPS)|Norma de<br>Referencia<br>Decreto Supremo<br>N°04/1992|150|mg/m2/día|Media aritmética mensual|
|Material Particulado<br>Sedimentable (MPS)|Norma de<br>Referencia<br>Decreto Supremo<br>N°04/1992|100|100|Media aritmética anual|

Fuente: Elaboración propia.

Cabe destacar que, ante la ausencia de una norma de calidad nacional aplicable para el caso de

Material Particulado Sedimentable, se evaluará el cumplimiento de las concentraciones de este

contaminante a través de la utilización de una norma de referencia, de acuerdo con lo establecido

en el Reglamento de Evaluación Ambiental.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

69

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

#### 3.10. Línea Base de Calidad del Aire

A continuación, se describe la línea base de calidad del aire para el presente Proyecto en evaluación.

Para evitar sesgos estacionales, para la descripción del área de influencia se debe considerar un

periodo de registro de un año de mediciones, con una proporción de datos válidos igual o mayor al

75% en el caso de mediciones continuas, de acuerdo con los lineamientos establecidos en la Guía
para la Descripción del Área de Influencia - Calidad del Aire en el Área de Influencia de Proyectos

que Ingresan al SEIA [ (5)] .

Previo al análisis de los datos de calidad del aire, se considera la revisión de la completitud de éstos.

En los siguientes apartados se presentan los periodos de datos, junto con la completitud de éstos,

para las estaciones de monitoreo de calidad del aire consideradas.

Las estaciones de monitoreo de calidad del aire utilizadas para la elaboración de esta línea de base

de calidad del aire corresponden a las Estaciones Centro, Colegio Pedro Vergara Keller y Club

Deportivo 23 de marzo. En la siguiente tabla se presentan las coordenadas geográficas y periodo de

datos de medición considerados para las estaciones de monitoreo mencionadas, utilizados para la

elaboración de la Línea de Base de Calidad del Aire

**Tabla 3-16 - Caracterización de estación de monitoreo de calidad del aire.**

|Estación|Coordenadas UTM 18S WGS 84|Col3|Contaminantes<br>Medidos|Periodo de<br>Análisis|
|---|---|---|---|---|
|**Estación**|**Este**|**Norte**|**Norte**|**Norte**|
|Estación Centro|507.389|7.516.053|MP2,5, MP10, CO,<br>NO2, SO2|2020 - 2022|
|Colegio Pedro<br>Vergara Keller|506.893|7.518.227|MP2,5, MP10|2020 - 2022|
|Club Deportivo 23<br>de marzo|506.399|7.516.241|MP2,5, MP10, SO2|2020 - 2022|

Fuente: Elaboración propia.

En la Figura 3-47 se muestra la ubicación de las estaciones de monitoreo de Calidad del Aire

mencionadas en la tabla anterior, con respecto a la zona de emplazamiento del Proyecto.

5 Guía para la Descripción de la Calidad del Aire en el Área de influencia de Proyectos que Ingresan al SEIA, SEA 2015.
[Enlace web: https://sea.gob.cl/sites/default/files/imce/archivos/2016/01/20/guia_calidad_del_aire.pdf](https://sea.gob.cl/sites/default/files/imce/archivos/2016/01/20/guia_calidad_del_aire.pdf)

www.dfmconsultores.cl

**info@dfmconsultores.cl**

70

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-47. Ubicación Estaciones de Monitoreo de Calidad del Aire.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

71

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.10.1.** **Estación Centro**

A continuación, se muestran la completitud y las series de datos del último trienio para los

contaminantes monitoreados en la Estación Centro. Tales contaminantes corresponden a Material

Particulado Fino (MP2.5), Material Particulado Respirable (MP10), Dióxido de Azufre (SO 2 ), Dióxido

de Nitrógeno (NO 2 ) y Monóxido de Carbono (CO).

**3.10.1.1.** **Material Particulado Fino (MP2,5)**

Resultados Monitoreo

En la Tabla 3-17 se presenta los los resultados del monitoreo de material particulado fino (MP2.5)

en la Estación Centro durante el periodo comprendido entre el 01 de enero de 2020 al 31 de

diciembre de 2022.

**Tabla 3-17. Resultados Monitoreo de MP2.5. Estación Centro.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2020**|**2021**|**2022**|
|MP2,5 (μg/m3)|Número de datos medidos|366|365|365|
|MP2,5 (μg/m3)|Número de datos válidos|341|346|349|
|MP2,5 (μg/m3)|Porcentaje de datos válidos|93%|95%|96%|
|MP2,5 (μg/m3)|Mínimo diario|0,0|0,0|2,0|
|MP2,5 (μg/m3)|Máximo diario|14,0|10,0|23,0|
|MP2,5 (μg/m3)|Percentil 98 diario|10,0|7,0|13,0|
|MP2,5 (μg/m3)|Media anual|5,2|4,4|5,3|
|MP2,5 (μg/m3)|Media trianual|5,0|5,0|5,0|

Fuente: Elaboración propia, a partir de datos del SINCA.

Comparación con Normativa

En la Tabla 3-18 se exhibe la comparación de los resultados del monitoreo de material particulado

fino (MP2.5) en la Centro con la normativa primaria de calidad del aire durante el periodo en

estudio.

**Tabla 3-18. Comparación de Monitoreo de MP2.5 con Normativa. Estación Centro.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de la<br>Norma|
|---|---|---|---|---|---|---|
|MP2,5|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 98 de la<br>concentración media diaria|13,0|50|μg/m3|26,0%|
|MP2,5|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media<br>trianual|5,0|20|μg/m3|25,0%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia, a partir de datos del SINCA.

72

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

De la tabla anterior, es posible establecer, de manera cuantitativa, que la estación de monitoreo

Centro ha registrado concentraciones de MP2.5 por debajo de los valores límites de la normativa de

percentil 98 de 24 horas y de periodo trianual para el periodo en estudio.

Serie de Tiempo

A continuación, en la Figura 3-48 se muestran las series de datos de material particulado respirable

fino (MP2.5) monitoreados por la Estación Centro durante el periodo comprendido entre 01 de

enero de 2020 al 31 de diciembre de 2022

**Figura 3-48. Serie de tiempo Material Particulado Fino (MP2,5). Estación Centro.**

Fuente: Elaboración propia, a partir de datos del SINCA.

A partir de la figura anterior, es posible concluir de manera cualitativa que la concentración

observada en la Estación Centro en el último trienio, para el contaminante Material Particulado Fino

(MP2,5), se encuentra por debajo de los límites establecidos por las normativas de percentil 98 de

concentraciones medias diarias y de concentración media anual.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

73

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.10.1.2.** **Material Particulado Respirable (MP10)**

Resultados Monitoreo

En la Tabla 3-19 se presentan los resultados del monitoreo de material particulado respirable

(MP10) en la Estación Centro durante el periodo comprendido entre el 01 de enero de 2020 al 31

de diciembre de 2022.

**Tabla 3-19. Resultados Monitoreo de MP10. Estación Centro.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2020**|**2021**|**2022**|
|MP10 (μg/m3N)|Número de datos medidos|366|365|365|
|MP10 (μg/m3N)|Número de datos válidos|336|345|349|
|MP10 (μg/m3N)|Porcentaje de datos válidos|92%|95%|96%|
|MP10 (μg/m3N)|Mínimo diario|14,0|6,0|12,0|
|MP10 (μg/m3N)|Máximo diario|104,0|66,0|50,0|
|MP10 (μg/m3N)|Percentil 98 diario|48,0|37,0|42,0|
|MP10 (μg/m3N)|Media anual|29,7|21,0|26,3|
|MP10 (μg/m3N)|Media trianual|25,7|25,7|25,7|

Fuente: Elaboración propia, a partir de datos del SINCA.

Comparación con Normativa

En la Tabla 3-20 se exhibe la comparación de los resultados del monitoreo de material particulado

respirable (MP10) en la Estación Centro con la normativa primaria de calidad del aire durante el

periodo en estudio.

**Tabla 3-20. Comparación de Monitoreo de MP10 con Normativa. Estación Centro.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|MP10|1 de enero de 2020 - 31 de<br>diciembre de 2022|Percentil 98 de la<br>concentración media diaria|26,3|130|μg/m3N|20,3%|
|MP10|1 de enero de 2020 - 31 de<br>diciembre de 2022|Concentración media<br>trianual|25,7|50|μg/m3N|51,4%|

Fuente: Elaboración propia, a partir de datos del SINCA.

De la tabla anterior, es posible establecer de manera cuantitativa que la estación de monitoreo

Centro ha registrado concentraciones de MP10 por debajo de los límites normativos, tanto para el

periodo diario como trianual, del periodo en estudio.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

74

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Serie de Tiempo

A continuación, en la Figura 3-49 se muestran las series de datos de material particulado respirable

(MP10) monitoreados por la Estación Centro durante el periodo en estudio.

**Figura 3-49. Serie de tiempo Material Particulado Respirable (MP10). Estación Centro.**

Fuente: Elaboración propia, a partir de datos del SINCA.

De la figura anterior se puede concluir de manera cualitativa que, para el contaminante Material

Particulado Respirable (MP10), la concentración observada en la Estación Centro en el último trienio

se encuentra por debajo de los límites establecidos por las normativas de percentil 98 de

concentraciones medias diarias y de concentración media anual.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

75

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.10.1.3.** **Monóxido de carbono (CO)**

Resultados Monitoreo

En la Tabla 3-21 se presentan los resultados del monitoreo de dióxido de carbono (CO) en la Estación

Centro durante el periodo comprendido entre el 01 de enero de 2020 al 31 de diciembre de 2022.

**Tabla 3-21. Resultados Monitoreo de CO. Estación Centro.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2020**|**2021**|**2022**|
|CO (mg/m3N)|Número de datos medidos|8.784|8.760|8.760|
|CO (mg/m3N)|Número de datos válidos|8.682|8.676|8.441|
|CO (mg/m3N)|Porcentaje de datos válidos|99%|99%|96%|
|CO (mg/m3N)|Mínimo horario|0,0|0,0|0,0|
|CO (mg/m3N)|Máximo horario|1,4|1,8|2,4|
|CO (mg/m3N)|Percentil 99 de los máximos diarios de concentración<br>horaria|1,1|1,4|1,9|
|CO (mg/m3N)|Promedio trianual percentil 99 de los máximos diarios<br>de concentración horaria|1,5|1,5|1,5|
|CO (mg/m3N)|Percentil 99 de los máximos diarios de concentración<br>media móvil de 8 horas|0,6|0,9|1,0|
|CO (mg/m3N)|Promedio trianual percentil 99 de los máximos diarios<br>de concentración media móvil de 8 horas|0,8|0,8|0,8|

Fuente: Elaboración propia, a partir de datos del SINCA.

Comparación con Normativa

En la Tabla 3-22 se exhibe la comparación de los resultados del monitoreo de dióxido de carbono

(CO) en la Estación Centro con la normativa primaria de calidad del aire durante el periodo en

estudio.

**Tabla 3-22. Comparación de Monitoreo de CO con normativa. Estación Centro.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|CO|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora|1,5|30|mg/m3N|5,0%|
|CO|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 99 de los<br>máximos diarios de<br>concentración de 8 horas|0,8|10|mg/m3N|8,0%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia, a partir de datos del SINCA

76

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

De la tabla anterior, es posible establecer, de manera cuantitativa, que la estación de monitoreo

Centro ha registrado concentraciones de CO bajo las normas de percentil 99 para periodo de 1 hora

y 8 horas.

Serie de Tiempo

A continuación, en la Figura 3-40, se muestran las series de datos de dióxido de carbono (CO)

monitoreados por la Estación Centro durante el periodo en estudio.

**Figura 3-50. Serie de tiempo Monóxido de Carbono (CO). Estación Centro.**

Fuente: Elaboración propia, a partir de datos del SINCA.

Conforme a la figura anterior, es posible concluir, de manera cualitativa, que la concentración

observada para el contaminante Monóxido de Carbono (CO) en la Estación Centro se encuentra por

debajo de los límites establecidos, tanto por la normativa de percentil 99 de 1 hora, así como

también para la norma de percentil 99 de 8 horas, para el periodo en estudio.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

77

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.10.1.4.** **Dióxido de nitrógeno (NO** **2** **)**

Resultados Monitoreo

En la Tabla 3-23 se presentan los resultados del monitoreo de dióxido de nitrógeno (NO 2 ) en la

Estación Centro durante el periodo comprendido entre el 01 de enero de 2020 al 31 de diciembre

de 2022.

**Tabla 3-23. Resultados Monitoreo de NO** **2** **. Estación Centro.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2020**|**2021**|**2022**|
|NO2 (μg/m3N)|Número de datos medidos|8.784|8.760|8.760|
|NO2 (μg/m3N)|Número de datos válidos|8.520|8.319|8.600|
|NO2 (μg/m3N)|Porcentaje de datos válidos|97%|95%|98%|
|NO2 (μg/m3N)|Mínimo horario|0,5|0,0|2,5|
|NO2 (μg/m3N)|Máximo horario|91,2|95,5|103,7|
|NO2 (μg/m3N)|Percentil 99 de los máximos diarios de<br>concentración horaria|79,6|85,7|95,4|
|NO2 (μg/m3N)|Promedio trianual percentil 99 de los máximos<br>diarios de concentración horaria|86,9|86,9|86,9|
|NO2 (μg/m3N)|Media anual|12,9|18,3|21,2|
|NO2 (μg/m3N)|Media trianual|17,5|17,5|17,5|

Fuente: Elaboración propia, a partir de datos del SINCA.

Comparación con Normativa

En la Tabla 3-24 se exhibe la comparación de los resultados del monitoreo de dióxido de nitrógeno

(NO 2 ) en la Estación Centro con la normativa primaria de calidad del aire durante el periodo en

estudio.

**Tabla 3-24. Comparación con normativa de dióxido de nitrógeno (NO** **2** **). Estación Centro.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|NO2|1 de enero de 2020<br>- 31 de diciembre<br>de 2022|Percentil 99 de los máximos<br>diarios de concentración de 1 hora|86,9|400|μg/m3N|21,7%|
|NO2|1 de enero de 2020<br>- 31 de diciembre<br>de 2022|Concentración media trianual|17,5|100|μg/m3N|17,5%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia, a partir de datos del SINCA.

78

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

De la tabla anterior, es posible establecer, de manera cuantitativa, que la estación de monitoreo

Centro ha registrado concentraciones de NO 2 bajo la norma de percentil 99 de 1 hora, como también

bajo la norma de periodo trianual.

Serie de Tiempo

A continuación, en la Figura 3-51 se muestran las series de datos de dióxido de nitrógeno (NO 2 )

monitoreados por la Estación Centro durante el periodo en estudio.

**Figura 3-51. Serie de tiempo Dióxido de Nitrógeno (NO** **2** **). Estación Centro.**

Fuente: Elaboración propia, a partir de datos del SINCA.

Respecto a la figura anterior se puede concluir, de manera cualitativa, que la concentración

observada para el contaminante dióxido de nitrógeno (NO 2 ) en la Estación Centro en el último

trienio se encuentra por debajo de los límites establecidos por la normativa primaria de calidad del

aire del NO 2, tanto para el periodo horario, como para el periodo anual.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

79

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.10.1.5.** **Dióxido de azufre (SO** **2** **)**

Resultados Monitoreo

En la Tabla 3-25 se presentan los resultados del monitoreo de dióxido de azufre (SO 2 ) en la Estación

Centro durante el periodo comprendido entre el 01 de enero de 2020 al 31 de diciembre de 2022.

**Tabla 3-25. Resultados Monitoreo de SO** **2** **. Estación Centro.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2020**|**2021**|**2022**|
|SO2 (μg/m3N)|Número de datos medidos|8.784|8.760|8.760|
|SO2 (μg/m3N)|Número de datos válidos|8.682|8.529|8.614|
|SO2 (μg/m3N)|Porcentaje de datos válidos|99%|97%|98%|
|SO2 (μg/m3N)|Mínimo horario|0,8|0,1|0,1|
|SO2 (μg/m3N)|Máximo horario|137,8|74,2|155,3|
|SO2 (μg/m3N)|Percentil 99 de concentración horaria|13,7|7,3|13,3|
|SO2 (μg/m3N)|Promedio trianual percentil 99 de concentración horaria|11,4|11,4|11,4|
|SO2 (μg/m3N)|Percentil 99 de concentración diaria|6,2|4,4|6,8|
|SO2 (μg/m3N)|Promedio trianual percentil 99 de concentración diaria|5,8|5,8|5,8|
|SO2 (μg/m3N)|Media anual|2,7|2,2|2,7|
|SO2 (μg/m3N)|Media trianual|2,5|2,5|2,5|

Fuente: Elaboración propia, a partir de datos del SINCA.

Comparación con Normativa

En la Tabla 3-26 se exhibe la comparación de los resultados del monitoreo de dióxido de azufre (SO 2 )

en la Estación Centro con la normativa primaria de calidad del aire durante el periodo en estudio.

**Tabla 3-26. Comparación de Monitoreo de SO** **2** **con Normativa. Estación Centro.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|SO2|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 99 de<br>concentración horaria|11,4|350|μg/m3N|3,3%|
|SO2|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 99 de la<br>concentración media diaria|5,8|150|μg/m3N|3,9%|
|SO2|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media<br>trianual|2,5|60|μg/m3N|4,2%|

Fuente: Elaboración propia, a partir de datos del SINCA.

De la tabla anterior, es posible establecer, de manera cuantitativa, que la estación de monitoreo

Centro ha registrado concentraciones de SO 2 bajo los límites normativos establecidos para: el

percentil 99 de 1 hora, el percentil 99 de 24 horas, y también el periodo anual.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

80

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Series de Tiempo

A continuación, en la Figura 3-52 se muestran las series de datos dióxido de azufre (SO 2 )

monitoreados por la Estación Centro durante el periodo en estudio.

**Figura 3-52. Serie de tiempo Dióxido de Azufre (SO2). Estación Centro.**

Fuente: Elaboración propia, a partir de datos del SINCA.

Con respecto a la figura anterior, es posible establecer, de manera cualitativa, que las

concentraciones observadas para el contaminante Dióxido de Azufre (SO 2 ) en la Estación Centro se

encuentran por bajo las normas de percentil 99 de 1 hora, percentil 99 de 24 horas, y también el

periodo anual, para todo el periodo en estudio.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

81

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.10.2.** **Club Deportivo 23 de marzo**

**3.10.2.1.** **Material Particulado Fino (MP2,5)**

Resultados Monitoreo

En la Tabla 3-27 se presentan los resultados del monitoreo de material particulado fino (MP2.5) en

la Estación Club Deportivo 23 de marzo durante el periodo comprendido entre el 01 de enero de

2020 al 31 de diciembre de 2022.

**Tabla 3-27. Resultados Monitoreo de MP2.5. Estación Club Deportivo 23 de marzo.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2020**|**2021**|**2022**|
|MP2,5 (μg/m3)|Número de datos medidos|366|365|365|
|MP2,5 (μg/m3)|Número de datos válidos|354|345|347|
|MP2,5 (μg/m3)|Porcentaje de datos válidos|97%|95%|95%|
|MP2,5 (μg/m3)|Mínimo diario|2,0|3,0|3,0|
|MP2,5 (μg/m3)|Máximo diario|36,0|19,0|32,0|
|MP2,5 (μg/m3)|Percentil 98 diario|16,0|12,0|11,0|
|MP2,5 (μg/m3)|Media anual|7,4|6,9|6,6|
|MP2,5 (μg/m3)|Media trianual|7,0|7,0|7,0|

Fuente: Elaboración propia, a partir de datos del SINCA.

Comparación con Normativa

En la Tabla 3-28 se exhibe la comparación de los resultados del monitoreo de material particulado

fino (MP2.5) en la Estación Club Deportivo 23 de marzo con la normativa primaria de calidad del aire

durante el periodo en estudio.

**Tabla 3-28. Comparación de Monitoreo con Normativa. Estación Club Deportivo 23 de marzo.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de la<br>Norma|
|---|---|---|---|---|---|---|
|MP2,5|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 98 de la<br>concentración media diaria|11,0|50|μg/m3|22,0%|
|MP2,5|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media<br>trianual|7,0|20|μg/m3|35,0%|

Fuente: Elaboración propia, a partir de datos del SINCA.

De la tabla anterior, es posible establecer, de manera cuantitativa, que la estación de monitoreo

Club Deportivo 23 de marzo ha registrado concentraciones de MP2.5 por bajo la normativa de

percentil 98 de 24 horas y de periodo trianual para el periodo en estudio.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

82

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Serie de Tiempo

En la Figura 3-53 se muestra la serie de datos del contaminante Material Particulado Fino (MP2,5)

monitoreado en la Estación Club Deportivo 23 de marzo durante el periodo comprendido entre 01

de enero de 2020 al 31 de diciembre de 2022.

**Figura 3-53. Serie de tiempo Material Particulado Fino (MP2,5). Estación Club Deportivo 23 de marzo.**

Fuente: Elaboración propia, a partir de datos del SINCA.

Conforme a la figura anterior, se puede concluir, de manera cualitativa, que la concentración

observada para el contaminante Material Particulado Fino (MP2,5) en la Estación Club Deportivo 23

de marzo se encuentra por debajo de los límites establecidos por las normativas de percentil 98 de

concentraciones medias diarias y de concentración media anual, para el periodo en estudio.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

83

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.10.2.2.** **Material Particulado Respirable (MP10)**

Resultados Monitoreo

En la Tabla 3-29 se presentan los resultados del monitoreo de material particulado respirable

(MP10) en la Estación Club Deportivo 23 de marzo durante el periodo comprendido entre el 01 de

enero de 2020 al 31 de diciembre de 2022.

**Tabla 3-29. Resultados Monitoreo de MP10. Estación Club Deportivo 23 de marzo.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2020**|**2021**|**2022**|
|MP10 (μg/m3N)|Número de datos medidos|366|365|365|
|MP10 (μg/m3N)|Número de datos válidos|354|345|347|
|MP10 (μg/m3N)|Porcentaje de datos válidos|97%|95%|95%|
|MP10 (μg/m3N)|Mínimo diario|12,0|24,0|23,0|
|MP10 (μg/m3N)|Máximo diario|109,0|142,0|77,0|
|MP10 (μg/m3N)|Percentil 98 diario|60,0|77,0|68,0|
|MP10 (μg/m3N)|Media anual|39,0|45,5|43,8|
|MP10 (μg/m3N)|Media trianual|42,8|42,8|42,8|

Fuente: Elaboración propia, a partir de datos del SINCA.

Comparación con Normativa

En la Tabla 3-30 se exhibe la comparación de los resultados del monitoreo de material particulado

respirable (MP10) en la Estación Club Deportivo 23 de marzo con la normativa primaria de calidad

del aire durante el periodo en estudio.

**Tabla 3-30. Comparación de Monitoreo de MP10 con Normativa. Estación Club Deportivo 23 de marzo.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|MP10|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 98 de la<br>concentración media diaria|68,0|130|μg/m3N|52,3%|
|MP10|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media<br>trianual|42,8|50|μg/m3N|85,6%|

Fuente: Elaboración propia, a partir de datos del SINCA.

De la tabla anterior, es posible establecer de manera cuantitativa que la estación de monitoreo Club

Deportivo 23 de marzo ha registrado concentraciones de MP10 por bajo los límites normativos,

tanto para el periodo diario como trianual del periodo en estudio. No obstante, considerando los

registros en la estación Club Deportivo 23 de marzo, el valor del estadígrafo de concentración media

trianual de MP10, se encuentra dentro del rango de condición de latencia, dado que la

www.dfmconsultores.cl

**info@dfmconsultores.cl**

84

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

concentración equivale a un 85,6% de la norma, superando 80%, de acuerdo con la normativa

primaria de calidad del aire.

Serie de Tiempo

A continuación, en la Figura 3-54 se muestran las series de datos de material particulado respirable

(MP10) monitoreados por la Estación Estación Club Deportivo 23 de marzo durante el periodo en

estudio.

**Figura 3-54. Serie de tiempo Material Particulado Respirable (MP10). Estación Club Deportivo 23 de**

**marzo.**

Fuente: Elaboración propia, a partir de datos del SINCA.

Con respecto a la figura anterior, es posible concluir de manera cualitativa que, para la Estación Club

Deportivo 23 de marzo, los valores diarios de concentración de MP10 no superan el límite conforme

a la norma de percentil 98 diario, para el periodo en estudio.

Para el caso de la serie de tiempo de valores mensuales, donde a través de la línea verde se observa

la concentración media trianual de MP10, se aprecia que los valores de este estadígrafo, en la

www.dfmconsultores.cl

**info@dfmconsultores.cl**

85

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Estación Club Deportivo 23 de marzo, se encuentran dentro del rango de condición de latencia, dado

que se supera el 80%, es decir se sobrepasa los 40 μg/m [3] N, de la norma respectiva.

**3.10.2.3.** **Dióxido de azufre (SO** **2** **)**

Resultados Monitoreo

En la Tabla 3-31 se presentan los resultados del monitoreo de dióxido de azufre (SO 2 ) en la Estación

Estación Club Deportivo 23 de marzo durante el periodo comprendido entre el 01 de enero de 2020

al 31 de diciembre de 2022.

**Tabla 3-31. Resultados Monitoreo de SO** **2** **. Estación Club Deportivo 23 de marzo.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2020**|**2021**|**2022**|
|SO2 (μg/m3N)|Número de datos medidos|8.784|8.760|8.760|
|SO2 (μg/m3N)|Número de datos válidos|8.545|8.520|8.607|
|SO2 (μg/m3N)|Porcentaje de datos válidos|97%|97%|98%|
|SO2 (μg/m3N)|Mínimo horario|0,0|0,1|0,4|
|SO2 (μg/m3N)|Máximo horario|151,0|176,0|170,8|
|SO2 (μg/m3N)|Percentil 99 de concentración horaria|12,6|11,9|20,5|
|SO2 (μg/m3N)|Promedio trianual percentil 99 de concentración horaria|15,0|15,0|15,0|
|SO2 (μg/m3N)|Percentil 99 de concentración diaria|6,8|5,3|10,2|
|SO2 (μg/m3N)|Promedio trianual percentil 99 de concentración diaria|7,5|7,5|7,5|
|SO2 (μg/m3N)|Media anual|1,6|2,2|2,9|
|SO2 (μg/m3N)|Media trianual|2,3|2,3|2,3|

Fuente: Elaboración propia, a partir de datos del SINCA.

Comparación con Normativa

En la Tabla 3-32 se exhibe la comparación de los resultados del monitoreo de dióxido de azufre (SO 2 )

en la Estación Club Deportivo 23 de marzo con la normativa primaria de calidad del aire durante el

periodo en estudio.

**Tabla 3-32. Comparación de Monitoreo de SO** **2** **con Normativa. Estación Club Deportivo 23 de marzo.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|SO2|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 99 de<br>concentración horaria|15,0|350|μg/m3N|4,3%|
|SO2|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 99 de la<br>concentración media diaria|7,5|150|μg/m3N|5,0%|
|SO2|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media<br>trianual|2,3|60|μg/m3N|3,8%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia, a partir de datos del SINCA.

86

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

De la tabla anterior, es posible establecer, de manera cuantitativa, que la estación de monitoreo

Club Deportivo 23 de marzo ha registrado concentraciones de SO 2 bajo los límites normativos

establecidos para: el percentil 99 de 1 hora, el percentil 99 de 24 horas, y también el periodo anual.

Series de Tiempo

A continuación, en la Figura 3-55 se muestran las series de datos dióxido de azufre (SO 2 )

monitoreados por la Estación Club Deportivo 23 de marzo durante el periodo en estudio.

**Figura 3-55. Serie de tiempo Dióxido de Azufre (SO2). Estación Club Deportivo 23 de marzo.**

Fuente: Elaboración propia, a partir de datos del SINCA.

Con respecto a la figura anterior, es posible establecer, de manera cualitativa, que las

concentraciones observadas para el contaminante Dióxido de Azufre (SO 2 ) en la Estación Club

Deportivo 23 de marzo se encuentran por bajo las normas de percentil 99 de 1 hora, percentil 99 de

24 horas, y también el periodo anual, para todo el periodo en estudio.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

87

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.10.3.** **Colegio Pedro Vergara Keller**

**3.10.3.1.** **Material Particulado Fino (MP2,5)**

Resultados Monitoreo

En la Tabla 3-33 se presentan los resultados del monitoreo de material particulado fino (MP2.5) en

la Estación Colegio Pedro Vergara Keller durante el periodo comprendido entre el 01 de enero de

2020 al 31 de diciembre de 2022.

**Tabla 3-33. Resultados Monitoreo de MP2.5. Estación Colegio Pedro Vergara Keller.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2020**|**2021**|**2022**|
|MP2,5 (μg/m3)|Número de datos medidos|366|365|365|
|MP2,5 (μg/m3)|Número de datos válidos|342|350|335|
|MP2,5 (μg/m3)|Porcentaje de datos válidos|93%|96%|92%|
|MP2,5 (μg/m3)|Mínimo diario|4,0|3,0|3,0|
|MP2,5 (μg/m3)|Máximo diario|50,0|45,0|51,0|
|MP2,5 (μg/m3)|Percentil 98 diario|17,0|21,0|15,0|
|MP2,5 (μg/m3)|Media anual|8,5|10,9|9,5|
|MP2,5 (μg/m3)|Media trianual|9,6|9,6|9,6|

Fuente: Elaboración propia, a partir de datos del SINCA.

Comparación con Normativa

En la Tabla 3-34 se exhibe la comparación de los resultados del monitoreo de material particulado

fino (MP2.5) en la Estación Colegio Pedro Vergara Keller con la normativa primaria de calidad del

aire, durante el periodo en estudio.

**Tabla 3-34. Comparación de Monitoreo con Normativa de MP2,5. Estación Colegio Pedro Vergara Keller.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|MP2,5|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 98 de la<br>concentración media diaria|15,0|50|μg/m3|30,0%|
|MP2,5|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media<br>trianual|9,6|20|μg/m3|48,0%|

Fuente: Elaboración propia, a partir de datos del SINCA.

De la tabla anterior, es posible establecer, de manera cuantitativa, que la estación de monitoreo

Colegio Pedro Vergara Keller ha registrado concentraciones de MP2.5 por bajo la normativa de

percentil 98 de 24 horas y de periodo trianual, para el periodo en estudio.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

88

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Serie de Tiempo

A continuación, en la Figura 3-56, se muestra la serie de datos del contaminante Material

Particulado Fino (MP2,5) monitoreado en la Estación Colegio Pedro Vergara Keller durante el

periodo comprendido entre 01 de enero de 2020 al 31 de diciembre de 2022.

**Figura 3-56. Serie de tiempo Material Particulado Fino (MP2,5). Estación Colegio Pedro Vergara Keller.**

Fuente: Elaboración propia, a partir de datos del SINCA.

Conforme a lo expuesto en la figura anterior, es posible concluir que la concentración observada

para el contaminante Material Particulado Fino (MP2,5) en la Estación Colegio Pedro Vergara Keller

se encuentra por debajo de los límites establecidos por las normativas de percentil 98 de

concentraciones medias diarias y de concentración media anual, para todo el periodo en estudio.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

89

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**3.10.3.2.** **Material Particulado Respirable (MP10)**

Resultados Monitoreo

En la Tabla 3-35 se presentan los resultados del monitoreo de material particulado respirable

(MP10) en la Estación Colegio Pedro Vergara Keller durante el periodo comprendido entre el 01 de

enero de 2020 al 31 de diciembre de 2022.

**Tabla 3-35. Resultados Monitoreo de MP10. Estación Colegio Pedro Vergara Keller.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2020**|**2021**|**2022**|
|MP10 (μg/m3N)|Número de datos medidos|366|365|365|
|MP10 (μg/m3N)|Número de datos válidos|342|349|335|
|MP10 (μg/m3N)|Porcentaje de datos válidos|93%|96%|92%|
|MP10 (μg/m3N)|Mínimo diario|16,0|18,0|21,0|
|MP10 (μg/m3N)|Máximo diario|233,0|113,0|118,0|
|MP10 (μg/m3N)|Percentil 98 diario|72,0|75,0|83,0|
|MP10 (μg/m3N)|Media anual|44,3|46,4|49,5|
|MP10 (μg/m3N)|Media trianual|46,7|46,7|46,7|

Fuente: Elaboración propia, a partir de datos del SINCA.

Comparación con Normativa

En la Tabla 3-36 se exhibe la comparación de los resultados del monitoreo de material particulado

respirable (MP10) en la Estación Colegio Pedro Vergara Keller con la normativa primaria de calidad

del aire, durante el periodo en estudio.

**Tabla 3-36. Comparación de Monitoreo con Normativa de MP10. Estación Colegio Pedro Vergara Keller.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|MP10|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 98 de la<br>concentración media diaria|83,0|130|μg/m3N|63,8%|
|MP10|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media<br>trianual|46,7|50|μg/m3N|93,4%|

Fuente: Elaboración propia, a partir de datos del SINCA.

De la tabla anterior, es posible establecer de manera cuantitativa que la estación de monitoreo

Colegio Pedro Vergara Keller ha registrado concentraciones de MP10 por bajo los límites

normativos, tanto para el periodo diario como trianual del periodo en estudio. No obstante,

considerando los registros en la estación Colegio Pedro Vergara Keller, el valor del estadígrafo de

concentración media trianual de MP10 se encuentra dentro el rango de condición de latencia, dado

www.dfmconsultores.cl

**info@dfmconsultores.cl**

90

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

que la concentración equivale a un 93,4% de la norma, superando 80%, de acuerdo con la normativa

primaria de calidad del aire.

Serie de Tiempo

A continuación, en la Figura 3-57 se muestran las series de datos del contaminante Material

Particulado Respirable (MP10) monitoreado en la Estación Colegio Pedro Vergara Keller, durante el

periodo en estudio.

**Figura 3-57. Serie de tiempo Material Particulado Respirable (MP10). Estación Colegio Pedro Vergara**

**Keller.**

Fuente: Elaboración propia, a partir de datos del SINCA.

Con respecto a la figura anterior, es posible concluir de manera cualitativa que, para la Estación

Colegio Pedro Vergara Keller, los valores diarios de concentración de MP10 no superan el límite

conforme a la norma de percentil 98 diario, para el periodo en estudio.

Para el caso de la serie de tiempo de valores mensuales, donde a través de la línea verde se observa

la concentración media trianual de MP10, se aprecia que los valores de este estadígrafo, en la

www.dfmconsultores.cl

**info@dfmconsultores.cl**

91

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

Estación Colegio Pedro Vergara Keller, se encuentran dentro del rango de condición de latencia,

dado que se supera el 80%, es decir, se sobrepasan los 40 μg/m [3] N, de la norma respectiva.

**3.10.4.** **Resumen de Línea de Base de Calidad del Aire**

En la Tabla 3-37 se presenta un resumen de la Línea Base de Calidad del Aire analizada para la

Estación Centro, mientras que en la Tabla 3-38 y Tabla 3-39 se expone un resumen de las Estaciones

Club Deportivo 23 de marzo y Colegio Pedro Vergara Keller respectivamente.

**Tabla 3-37 - Resumen Línea Base de Calidad del Aire, Estación Centro.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje<br>de la Norma|
|---|---|---|---|---|---|---|
|MP2,5|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 98 de la<br>concentración media diaria|13,0|50|μg/m3|26,0%|
|MP2,5|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media trianual|5,0|20|μg/m3|25,0%|
|MP10|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 98 de la<br>concentración media diaria|26,3|130|μg/m3N|20,3%|
|MP10|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media trianual|25,7|50|μg/m3N|51,4%|
|CO|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 99 de los máximos<br>diarios de concentración de 1<br>hora|1,5|30|mg/m3N|5,0%|
|CO|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 99 de los máximos<br>diarios de concentración de 8<br>horas|0,8|10|mg/m3N|8,0%|
|NO2|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 99 de los máximos<br>diarios de concentración de 1<br>hora|86,9|400|μg/m3N|21,7%|
|NO2|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media trianual|17,5|100|μg/m3N|17,5%|
|SO2|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 99 de concentración<br>horaria|11,4|350|μg/m3N|3,3%|
|SO2|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 99 de la<br>concentración media diaria|5,8|150|μg/m3N|3,9%|
|SO2|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media trianual|2,5|60|μg/m3N|4,2%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

92

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Tabla 3-38 - Resumen Línea Base de Calidad del Aire, Estación Club Deportivo 23 de marzo.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|MP2,5|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 98 de la<br>concentración media diaria|11,0|50|μg/m3|22,0%|
|MP2,5|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media<br>trianual|7,0|20|μg/m3|35,0%|
|MP10|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 98 de la<br>concentración media diaria|68,0|130|μg/m3N|52,3%|
|MP10|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media<br>trianual|42,8|50|μg/m3N|85,6%|
|SO2|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 99 de<br>concentración horaria|15,0|350|μg/m3N|4,3%|
|SO2|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 99 de la<br>concentración media diaria|7,5|150|μg/m3N|5,0%|
|SO2|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media<br>trianual|2,3|60|μg/m3N|3,8%|

Fuente: Elaboración propia.

**Tabla 3-39 - Resumen Línea Base de Calidad del Aire, Estación Colegio Pedro Vergara Keller.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|MP2,5|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 98 de la<br>concentración media diaria|15,0|50|μg/m3|30,0%|
|MP2,5|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media<br>trianual|9,6|20|μg/m3|48,0%|
|MP10|1 de enero de 2020 - 31<br>de diciembre de 2022|Percentil 98 de la<br>concentración media diaria|83,0|130|μg/m3N|63,8%|
|MP10|1 de enero de 2020 - 31<br>de diciembre de 2022|Concentración media<br>trianual|46,7|50|μg/m3N|93,4%|

Fuente: Elaboración propia.

93

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

#### 3.11. Escenario Modelado

Para la modelación de dispersión de contaminantes se ha considerado el periodo de la fase de

construcción correspondiente a los primeros 12 meses, pues en él se presentan las mayores

emisiones. En consecuencia, a continuación, se procede a describir las fuentes emisoras ingresadas

al modelo de dispersión de contaminantes.

**3.11.1.** **Fuentes Emisoras Fase de Construcción**

Las fuentes de la fase de Construcción fueron georreferenciadas de acuerdo con la información

proporcionada por ingeniería, para posteriormente ser ingresadas al modelo. En la Figura 3-58 se

presenta la ubicación espacial de las fuentes emisoras, mientras que en la Tabla 3-40 se presenta el

detalle de las características de las fuentes y las tasas de emisión utilizadas. Cabe señalar que para

las emisiones asociadas a la fase de construcción del Proyecto se consideró una operación diaria de

8 horas para lunes a viernes y de 6 horas para el sábado.

**Tabla 3-40. Fuentes Emisoras Fase de Construcción.**

|ID|Descripción|Tipo de<br>fuente|Tasas de emisión|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Descripción**|**Tipo de**<br>**fuente**|**MP2.5**|**MP10**|**MPS**|**CO**|**NO2 **|**SO2 **|**Unidad**|
|SRC_1|Área proyecto|Areal|7,04E-08|1,39E-07|5,65E-07|4,12E-07|9,24E-07|1,67E-07|g/s/m2|
|SRC_2|Acceso|Camino|1,70E-05|1,70E-04|5,96E-04|1,21E-07|3,77E-06|6,20E-09|g/s/m|
|SRC_3|Tramo A|Camino|6,54E-07|2,75E-06|1,41E-05|9,48E-08|2,95E-06|4,86E-09|g/s/m|
|SRC_4|Tramo B|Camino|1,98E-06|1,98E-05|6,97E-05|2,74E-09|1,00E-07|1,64E-10|g/s/m|
|SRC_5|Tramo C|Camino|6,27E-07|2,64E-06|1,35E-05|9,21E-08|2,86E-06|4,70E-09|g/s/m|
|SRC_6|Tramo D|Camino|4,73E-07|1,96E-06|1,00E-05|7,25E-08|2,11E-06|3,48E-09|g/s/m|
|SRC_7|Tramo E|Camino|1,57E-07|6,86E-07|3,56E-06|2,00E-08|7,61E-07|1,24E-09|g/s/m|
|SRC_8|Camino interno|Camino|4,02E-06|4,00E-05|1,41E-04|1,84E-07|4,09E-07|1,18E-09|g/s/m|
|SRC_9|LTE|Lineal-areal|2,95E-08|6,51E-08|2,85E-07|8,50E-09|1,07E-08|1,09E-09|g/s/m2|

Fuente: Elaboración propia

www.dfmconsultores.cl

**info@dfmconsultores.cl**

94

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-58 - Ubicación Fuentes Emisoras Fase de Construcción.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

95

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

#### 3.12. Receptores de Interés

Tras definir una grilla de receptores con 5 niveles de resolución, tal cual se describió en la sección

3.3.1 del presente informe, se consideraron 15 receptores discretos, de los cuales doce (12)

corresponden a receptores que son parte del estudio de ruido, mientras que los tres (3) restantes

corresponden a las estaciones de monitoreo de calidad del aire considerados para la línea de base.

En la Tabla 3-41 se presenta el detalle de los receptores discretos, las coordenadas de ubicación de

cada receptor, su altura y descripción.

**Tabla 3-41- Receptores de Interés.**

|Receptor|Descripción|Coordenadas de Ubicación<br>Datum WGS 84|Col4|Altitud<br>(m.s.n.m.)|
|---|---|---|---|---|
|**Receptor**|**Descripción**|**Este [m]**|**Norte [m]**|**Norte [m]**|
|R_1|R01 Ruido|508.146|7.519.542|2279,2|
|R_2|R02 Ruido|508.855|7.519.417|2288,2|
|R_3|R03 Ruido|509.284|7.519.382|2297,1|
|R_4|R04 Ruido|510.263|7.519.143|2313,1|
|R_5|R05 Ruido|513.147|7.519.045|2357,6|
|R_6|R06 Ruido|513.721|7.518.530|2373,9|
|R_7|R07 Ruido|513.958|7.518.635|2376,5|
|R_8|R08 Ruido|513.226|7.517.661|2364,4|
|R_9|R09 Ruido|514.502|7.516.108|2380,3|
|R_10|R10 Ruido|519.188|7.513.097|2445,1|
|R_11|R11 Ruido|519.867|7.513.436|2450,8|
|R_12|R12 Ruido|523.573|7.510.935|2465,9|
|R_13|Estación Centro|507.371|7.516.056|2265,3|
|R_14|Colegio Pedro Vergara Keller|506.895|7.518.221|2260,8|
|R_15|Club Deportivo 23 de marzo|506.403|7.516.233|2253,2|

Fuente: Elaboración propia.

En la Figura 3-59 se muestra una imagen referencial de la ubicación de los receptores discretos

utilizados en la modelación.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

96

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-59 - Ubicación de Receptores de Interés.**

Fuente: Elaboración propia.

97

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

#### 3.13. Resultados de la Modelación Fase de Construcción

En este inciso se presentan los resultados de la modelación de dispersión de contaminantes realizada para la fase de construcción del proyecto.

De esta forma, en las siguientes tablas se exhiben las concentraciones aportadas por el proyecto para los distintos contaminantes considerados

sobre los receptores de interés.

**Tabla 3-42 - Resultados de modelo de dispersión de MP2.5. Fase de Construcción.**

|Receptor|Descripción|Material Particulado Respirable Fino (MP2,5)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3] **|**Concentración [μg/m3] **|**Norma de Calidad**|**Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Percentil 98**<br>**24 horas**|**Período Anual**|**Percentil 98**<br>**24 horas**|**Período Anual**|**Percentil 98**<br>**24 horas**|**Período Anual**|
|R_1|R01|0,01|0,00|50|20|0,01%|0,01%|
|R_2|R02|0,01|0,00|0,00|0,00|0,02%|0,01%|
|R_3|R03|0,01|0,00|0,00|0,00|0,02%|0,01%|
|R_4|R04|0,01|0,00|0,00|0,00|0,01%|0,01%|
|R_5|R05|0,00|0,00|0,00|0,00|0,01%|0,01%|
|R_6|R06|0,01|0,00|0,00|0,00|0,02%|0,02%|
|R_7|R07|0,03|0,01|0,01|0,01|0,06%|0,06%|
|R_8|R08|0,00|0,00|0,00|0,00|0,01%|0,00%|
|R_9|R09|0,01|0,00|0,00|0,00|0,01%|0,00%|
|R_10|R10|0,02|0,00|0,00|0,00|0,03%|0,02%|
|R_11|R11|0,01|0,00|0,00|0,00|0,02%|0,01%|
|R_12|R12|0,05|0,01|0,01|0,01|0,10%|0,04%|
|R_13|Estación Centro|0,01|0,00|0,00|0,00|0,01%|0,00%|
|R_14|Colegio Pedro Vergara Keller|0,00|0,00|0,00|0,00|0,01%|0,00%|
|R_15|Club Deportivo 23 de Marzo|0,00|0,00|0,00|0,00|0,01%|0,00%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

98

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Tabla 3-43 - Resultados de modelo de dispersión de MP10. Fase de Construcción.**

|Receptor|Descripción|Material Particulado Respirable (MP10)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3] **|**Concentración [μg/m3] **|**Norma de Calidad**|**Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Percentil 98**<br>**24 horas**|**Período Anual**|**Percentil 98**<br>**24 horas**|**Período Anual**|**Percentil 98**<br>**24 horas**|**Período Anual**|
|R_1|R01|0,01|0,00|130|50|0,01%|0,01%|
|R_2|R02|0,02|0,00|0,00|0,00|0,01%|0,01%|
|R_3|R03|0,02|0,00|0,00|0,00|0,02%|0,01%|
|R_4|R04|0,01|0,00|0,00|0,00|0,01%|0,01%|
|R_5|R05|0,01|0,00|0,00|0,00|0,01%|0,00%|
|R_6|R06|0,02|0,01|0,01|0,01|0,02%|0,02%|
|R_7|R07|0,07|0,03|0,03|0,03|0,05%|0,05%|
|R_8|R08|0,01|0,00|0,00|0,00|0,01%|0,00%|
|R_9|R09|0,02|0,00|0,00|0,00|0,01%|0,01%|
|R_10|R10|0,05|0,01|0,01|0,01|0,04%|0,02%|
|R_11|R11|0,04|0,01|0,01|0,01|0,03%|0,01%|
|R_12|R12|0,15|0,02|0,02|0,02|0,11%|0,04%|
|R_13|Estación Centro|0,02|0,00|0,00|0,00|0,01%|0,00%|
|R_14|Colegio Pedro Vergara Keller|0,01|0,00|0,00|0,00|0,01%|0,00%|
|R_15|Club Deportivo 23 de Marzo|0,01|0,00|0,00|0,00|0,01%|0,00%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

99

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Tabla 3-44 - Resultados de modelo de dispersión de MPS. Fase de Construcción.**

|Receptor|Descripción|Material Particulado Respirable (MP10)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Tasa de depositación [mg/m2-día]**|**Tasa de depositación [mg/m2-día]**|**Norma de referencia**|**Norma de referencia**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Periodo Mensual**|**Período Anual**|**Periodo Mensual**|**Período Anual**|**Periodo Mensual**|**Período Anual**|
|R_1|R01|0,02|0,01|150|100|0,01%|0,01%|
|R_2|R02|0,04|0,02|0,02|0,02|0,03%|0,02%|
|R_3|R03|0,05|0,02|0,02|0,02|0,03%|0,02%|
|R_4|R04|0,02|0,01|0,01|0,01|0,02%|0,01%|
|R_5|R05|0,02|0,01|0,01|0,01|0,01%|0,01%|
|R_6|R06|0,14|0,12|0,12|0,12|0,09%|0,12%|
|R_7|R07|0,28|0,25|0,25|0,25|0,19%|0,25%|
|R_8|R08|0,01|0,01|0,01|0,01|0,01%|0,01%|
|R_9|R09|0,01|0,01|0,01|0,01|0,01%|0,01%|
|R_10|R10|0,07|0,03|0,03|0,03|0,04%|0,03%|
|R_11|R11|0,05|0,03|0,03|0,03|0,03%|0,03%|
|R_12|R12|0,12|0,04|0,04|0,04|0,08%|0,04%|
|R_13|Estación Centro|0,02|0,01|0,01|0,01|0,01%|0,01%|
|R_14|Colegio Pedro Vergara Keller|0,01|0,01|0,01|0,01|0,01%|0,01%|
|R_15|Club Deportivo 23 de Marzo|0,01|0,01|0,01|0,01|0,01%|0,01%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

100

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Tabla 3-45 - Resultados de modelo de dispersión de CO. Fase de Construcción.**

|Receptor|Descripción|Monóxido de Carbono (CO)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [mg/m3] **|**Concentración [mg/m3] **|**Norma de Calidad**|**Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Percentil 99**<br>**1 hora**|**Percentil 99**<br>**8 horas**|**Percentil 99**<br>**1 hora**|**Percentil 99**<br>**8 horas**|**Percentil 99**<br>**1 hora**|**Percentil 99**<br>**8 horas**|
|R_1|R01|0,00|0,00|30|10|0,00%|0,00%|
|R_2|R02|0,00|0,00|0,00|0,00|0,00%|0,00%|
|R_3|R03|0,00|0,00|0,00|0,00|0,00%|0,00%|
|R_4|R04|0,00|0,00|0,00|0,00|0,00%|0,00%|
|R_5|R05|0,00|0,00|0,00|0,00|0,00%|0,00%|
|R_6|R06|0,00|0,00|0,00|0,00|0,00%|0,00%|
|R_7|R07|0,00|0,00|0,00|0,00|0,00%|0,00%|
|R_8|R08|0,00|0,00|0,00|0,00|0,00%|0,00%|
|R_9|R09|0,00|0,00|0,00|0,00|0,00%|0,00%|
|R_10|R10|0,00|0,00|0,00|0,00|0,00%|0,00%|
|R_11|R11|0,00|0,00|0,00|0,00|0,00%|0,00%|
|R_12|R12|0,00|0,00|0,00|0,00|0,01%|0,01%|
|R_13|Estación Centro|0,00|0,00|0,00|0,00|0,00%|0,00%|
|R_14|Colegio Pedro Vergara Keller|0,00|0,00|0,00|0,00|0,00%|0,00%|
|R_15|Club Deportivo 23 de Marzo|0,00|0,00|0,00|0,00|0,00%|0,00%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

101

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Tabla 3-46 - Resultados de modelo de dispersión de NO** **2** **. Fase de Construcción.**

|Receptor|Descripción|Dióxido de Nitrógeno (NO )<br>2|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Norma de Calidad**|**Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Percentil 99**<br>**1 hora**|**Período Anual**|**Percentil 99**<br>**1 hora**|**Período Anual**|**Percentil 99**<br>** 1 hora**|**Período Anual**|
|R_1|R01|0,11|0,00|400|100|0,03%|0,00%|
|R_2|R02|0,12|0,00|0,00|0,00|0,03%|0,00%|
|R_3|R03|0,13|0,00|0,00|0,00|0,03%|0,00%|
|R_4|R04|0,17|0,00|0,00|0,00|0,04%|0,00%|
|R_5|R05|0,19|0,00|0,00|0,00|0,05%|0,00%|
|R_6|R06|0,30|0,00|0,00|0,00|0,07%|0,00%|
|R_7|R07|0,25|0,00|0,00|0,00|0,06%|0,00%|
|R_8|R08|0,31|0,00|0,00|0,00|0,08%|0,00%|
|R_9|R09|0,68|0,00|0,00|0,00|0,17%|0,00%|
|R_10|R10|2,51|0,02|0,02|0,02|0,63%|0,02%|
|R_11|R11|2,03|0,01|0,01|0,01|0,51%|0,01%|
|R_12|R12|8,48|0,08|0,08|0,08|2,12%|0,08%|
|R_13|Estación Centro|0,50|0,00|0,00|0,00|0,12%|0,00%|
|R_14|Colegio Pedro Vergara Keller|0,15|0,00|0,00|0,00|0,04%|0,00%|
|R_15|Club Deportivo 23 de Marzo|0,36|0,00|0,00|0,00|0,09%|0,00%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

102

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Tabla 3-47 - Resultados de modelo de dispersión de SO** **2** **. Fase de Construcción.**

|Receptor|Descripción|Dióxido de Azufre (SO )<br>2|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Norma de Calidad**|**Norma de Calidad**|**Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Percentil 99**<br>**1 hora**|**Percentil 99**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 99**<br>** 1 hora**|**Percentil 99**<br>** 24 horas**|**Período**<br>**Anual**|**Percentil 99**<br>** 1 hora**|**Percentil 99**<br>**24 horas**|**Período**<br>**Anual**|
|R_1|R01|0,00|0,00|0,00|350|150|60|0,00%|0,00%|0,00%|
|R_2|R02|0,00|0,00|0,00|0,00|0,00|0,00|0,00%|0,00%|0,00%|
|R_3|R03|0,00|0,00|0,00|0,00|0,00|0,00|0,00%|0,00%|0,00%|
|R_4|R04|0,00|0,00|0,00|0,00|0,00|0,00|0,00%|0,00%|0,00%|
|R_5|R05|0,00|0,00|0,00|0,00|0,00|0,00|0,00%|0,00%|0,00%|
|R_6|R06|0,00|0,00|0,00|0,00|0,00|0,00|0,00%|0,00%|0,00%|
|R_7|R07|0,01|0,00|0,00|0,00|0,00|0,00|0,00%|0,00%|0,00%|
|R_8|R08|0,00|0,00|0,00|0,00|0,00|0,00|0,00%|0,00%|0,00%|
|R_9|R09|0,01|0,01|0,00|0,00|0,00|0,00|0,00%|0,01%|0,00%|
|R_10|R10|0,07|0,03|0,00|0,00|0,00|0,00|0,02%|0,02%|0,00%|
|R_11|R11|0,05|0,02|0,00|0,00|0,00|0,00|0,01%|0,01%|0,00%|
|R_12|R12|0,51|0,12|0,01|0,01|0,01|0,01|0,15%|0,08%|0,02%|
|R_13|Estación Centro|0,01|0,01|0,00|0,00|0,00|0,00|0,00%|0,00%|0,00%|
|R_14|Colegio Pedro<br>Vergara Keller|0,00|0,00|0,00|0,00|0,00|0,00|0,00%|0,00%|0,00%|
|R_15|Club Deportivo 23<br>de Marzo|0,01|0,00|0,00|0,00|0,00|0,00|0,00%|0,00%|0,00%|

Fuente: Elaboración propia.

Por otro lado, en las siguientes figuras se presentan las curvas de isoconcentración e isodepositación del aporte generado por el proyecto en la

fase de construcción.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

103

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-60. Curva de Isoconcentración para Percentil 98 período 24 horas MP2,5 (μg/m** **[3]** **). Fase de**

**Construcción.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

104

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-61. Curva de Isoconcentración para período anual MP2,5 (μg/m** **[3]** **). Fase de Construcción.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

105

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-62. Curva de Isoconcentración para Percentil 98 período 24 horas MP10 (μg/m** **[3]** **). Fase de**

**Construcción.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

106

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-63. Curva de Isoconcentración para período anual MP10 (μg/m** **[3]** **). Fase de Construcción.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

107

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-64. Curva de Isodepositación para período mensual MPS (mg/m** **[2]** **/día). Fase de Construcción.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

108

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-65. Curva de Isodepositación para período anual MPS (mg/m** **[2]** **/día). Fase de Construcción.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

109

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-66. Curva de Isoconcentración para Percentil 99 periodo 1 hora CO (mg/m** **[3]** **). Fase de**

**Construcción.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

110

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-67. Curva de Isoconcentración para Percentil 99 período 8 horas CO (mg/m** **[3]** **). Fase de**

**Construcción.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

111

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-68. Curva de Isoconcentración para periodo anual NO** **2** **(μg/m** **[3]** **). Fase de Construcción.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

112

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-69. Curva de Isoconcentración para Percentil 99 periodo 1 hora NO** **2** **(μg/m** **[3]** **). Fase de**

**Construcción.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

113

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-70. Curva de Isoconcentración para período anual SO** **2** **(μg/m** **[3]** **). Fase de Construcción.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

114

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-71. Curva de Isoconcentración para Percentil 99 periodo 24 horas SO** **2** **(μg/m** **[3]** **). Fase de**

**Construcción.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

115

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 3-72. Curva de Isoconcentración para Percentil 99 periodo 1 hora SO** **2** **(μg/m** **[3]** **). Fase de**

**Construcción.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

116

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

#### 3.14. Concentración Total Esperada

A continuación, se presentan las concentraciones totales esperadas en aquellos puntos en los que se cuenta con registro de datos de monitoreo

de calidad del aire, sumando el valor de la línea base más el aporte de proyectos aprobados y no ejecutados que hayan declarado aportes en las

estaciones evaluadas, más el aporte del proyecto en la fase de construcción, incluyendo además la comparación con la norma de calidad respectiva.

En la Tabla 3-48 se presentan los proyectos considerados, que hayan declarado aportes en las estaciones evaluadas, estén aprobados y no se hayan

ejecutado:

**Tabla 3-48 - Concentración total esperada, estación Centro. Fase de Construcción.**

|id|Nombre del Proyecto|Fuente|
|---|---|---|
|P1|Proyecto Inmobiliario Lotes B y C|https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2151471662|
|P2|Delimitación de nuevos recursos,<br>Proyecto Quetena|https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2152572499|
|P3|Proyecto Ampliación y Mejoramiento<br>Aeropuerto El Loa de Calama|https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2151727454|
|P4|Parque Fotovoltaico Latorre Sunlight|https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2151793001|
|P5|Proyecto Extracción de Áridos Pozo<br>E10 (km 100)|https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2145347109|
|P6|Ajustes Constructivos a Instalaciones<br>de Relaves Espesados|https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2154669144|
|P7|Parque Eólico Vientos del Loa|https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2147975096|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

117

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

A continuación, se presenta el aporte informado por los proyectos considerados en la tabla anterior:

**Tabla 3-49 - Aporte otros proyectos, Estación Centro.**

|Contaminante|Período|Unidad|Normativa<br>vigente|Aporte de otros proyectos|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Período**|**Unidad**|**Normativa**<br>**vigente**|**P1**|**P2**|**P3**|**P4**|**P5**|**P6**|**P7**|**Total**|**Porcentaje**<br>**de la**<br>**norma**|
|Material<br>Particulado<br>Respirable<br>Fino (MP2,5)|P98 24h|μg/m3|50|0,001|0,004|0,007|0,000|0,000|0,092|0,000|0,104|0,21%|
|Material<br>Particulado<br>Respirable<br>Fino (MP2,5)|Anual|μg/m3|20|0,000|0,001|0,002|0,000|0,000|0,050|0,000|0,053|0,26%|
|Material<br>Particulado<br>Respirable<br>(MP10)|P98 24h|μg/m3N|130|0,001|0,009|0,026|0,010|0,010|0,371|0,000|0,427|0,33%|
|Material<br>Particulado<br>Respirable<br>(MP10)|Anual|μg/m3N|50|0,000|0,002|0,006|0,000|0,000|0,199|0,000|0,207|0,41%|
|Monóxido de<br>Carbono (CO)|P99 máx. 1h|mg/m3N|30|n/i|0,0359|0,140|0,050|n/i|0,667|0,000|0,893|0,00%|
|Monóxido de<br>Carbono (CO)|P99 máx. 8h|mg/m3N|10|n/i|0,0511|0,041|0,030|n/i|0,462|0,000|0,584|0,01%|
|Dióxido de<br>Nitrógeno<br>(NO2)|P99 máx. 1h|μg/m3N|400|n/i|0,1654|0,533|0,160|n/i|1,952|2,000|4,810|1,20%|
|Dióxido de<br>Nitrógeno<br>(NO2)|Anual|μg/m3N|100|n/i|0,0006|0,015|0,010|n/i|0,284|2,000|2,309|2,31%|
|Dióxido de<br>Azufre (SO2)|P99 1h|μg/m3N|350|n/i|0,0064|0,000|0,000|n/i|0,048|0,000|0,054|0,02%|
|Dióxido de<br>Azufre (SO2)|P99 24h|μg/m3N|150|n/i|0,0053|0,000|0,000|n/i|0,013|0,000|0,018|0,01%|
|Dióxido de<br>Azufre (SO2)|Anual|μg/m3N|60|n/i|0,0006|0,000|0,000|n/i|0,007|0,000|0,007|0,01%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

118

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Tabla 3-50 - Aporte otros proyectos, Estación Club Deportivo 23 de marzo.**

|Contaminante|Período|Unidad|Normativa<br>vigente|Aporte de otros proyectos|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Período**|**Unidad**|**Normativa**<br>**vigente**|**P1**|**P2**|**P3**|**P4**|**P5**|**P6**|**P7**|**Total**|**Porcentaje**<br>**de la**<br>**norma**|
|Material<br>Particulado<br>Respirable<br>Fino (MP2,5)|P98 24h|μg/m3|50|0,001|0,006|0,004|0,000|0,000|0,099|0,000|0,111|0,22%|
|Material<br>Particulado<br>Respirable<br>Fino (MP2,5)|Anual|μg/m3|20|0,000|0,001|0,001|0,000|0,000|0,056|0,000|0,058|0,29%|
|Material<br>Particulado<br>Respirable<br>(MP10)|P98 24h|μg/m3N|130|0,002|0,011|0,017|0,010|0,010|0,390|0,000|0,440|0,34%|
|Material<br>Particulado<br>Respirable<br>(MP10)|Anual|μg/m3N|50|0,000|0,002|0,004|0,000|0,000|0,223|0,000|0,229|0,46%|
|Dióxido de<br>Azufre (SO2)|P99 1h|μg/m3N|350|n/i|0,009|0,000|0,000|n/i|0,049|0,000|0,058|0,02%|
|Dióxido de<br>Azufre (SO2)|P99 24h|μg/m3N|150|n/i|0,006|0,000|0,000|n/i|0,015|0,000|0,020|0,01%|
|Dióxido de<br>Azufre (SO2)|Anual|μg/m3N|60|n/i|0,001|0,000|0,000|n/i|0,007|0,000|0,008|0,01%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

119

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Tabla 3-51 - Aporte otros proyectos, estación Colegio Pedro Vergara Keller.**

|Contaminante|Período|Unidad|Normativa<br>vigente|Aporte de otros proyectos|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Período**|**Unidad**|**Normativa**<br>**vigente**|**P1**|**P2**|**P3**|**P4**|**P5**|**P6**|**P7**|**Valor**|**Porcentaje**<br>**de la**<br>**norma**|
|Material<br>Particulado<br>Respirable<br>Fino (MP2,5)|P98 24h|μg/m3|50|0,006|0,015|0,002|0,000|0,000|0,155|0,000|0,178|0,36%|
|Material<br>Particulado<br>Respirable<br>Fino (MP2,5)|Anual|μg/m3|20|0,001|0,002|0,000|0,000|0,000|0,090|0,000|0,094|0,47%|
|Material<br>Particulado<br>Respirable<br>(MP10)|P98 24h|μg/m3N|130|0,011|0,032|0,007|0,010|0,000|0,633|0,000|0,693|0,53%|
|Material<br>Particulado<br>Respirable<br>(MP10)|Anual|μg/m3N|50|0,002|0,008|0,001|0,000|0,000|0,369|0,000|0,380|0,76%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

120

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

A continuación, se presenta la concentración total esperada, calculada de acuerdo a las siguientes formulas:

**Línea de base proyectada: [Valor medido] + [Aporte de otros proyectos]**

**Concentración total esperada: [Línea de base proyectada] + [Aporte del proyecto]**

**Tabla 3-52 - Concentración total esperada, estación Centro. Fase de Construcción.**

|Contaminante|Período|Unidad|Normativa<br>vigente|Línea de Base Proyectada|Col6|Col7|Col8|Aporte del proyecto|Col10|Concentración Total|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Período**|**Unidad**|**Normativa**<br>**vigente**|**Valor**<br>**Medido**|**Aporte**<br>**otros**<br>**proyectos**|**Total**|**Porcentaje**<br>**de la**<br>**norma**|**Valor**|**Porcentaje**<br>**de la**<br>**norma**|**Valor**|**Porcentaje**<br>**de la**<br>**norma**|
|Material<br>Particulado<br>Respirable<br>Fino (MP2,5)|P98 24h|μg/m3|50|13,00|0,10|13,10|26,2%|0,01|0,01%|13,11|26,22%|
|Material<br>Particulado<br>Respirable<br>Fino (MP2,5)|Anual|μg/m3|20|5,00|0,05|5,05|25,3%|0,00|0,00%|5,05|25,27%|
|Material<br>Particulado<br>Respirable<br>(MP10)|P98 24h|μg/m3N|130|26,34|0,43|26,76|20,6%|0,02|0,01%|26,78|20,60%|
|Material<br>Particulado<br>Respirable<br>(MP10)|Anual|μg/m3N|50|25,70|0,21|25,91|51,8%|0,00|0,00%|25,91|51,82%|
|Monóxido de<br>Carbono (CO)|P99 máx. 1h|mg/m3N|30|1,50|0,00|1,50|5,0%|0,00|0,00%|1,50|5,00%|
|Monóxido de<br>Carbono (CO)|P99 máx. 8h|mg/m3N|10|0,80|0,00|0,80|8,0%|0,00|0,00%|0,80|8,01%|
|Dióxido de<br>Nitrógeno<br>(NO2)|P99 máx. 1h|μg/m3N|400|86,90|4,81|91,71|22,9%|0,50|0,12%|92,21|23,05%|
|Dióxido de<br>Nitrógeno<br>(NO2)|Anual|μg/m3N|100|17,50|2,31|19,81|19,8%|0,00|0,00%|19,81|19,81%|
|Dióxido de<br>Azufre (SO2)|P99 1h|μg/m3N|350|11,40|0,05|11,45|3,3%|0,01|0,00%|11,46|3,28%|
|Dióxido de<br>Azufre (SO2)|P99 24h|μg/m3N|150|5,80|0,02|5,82|3,9%|0,01|0,00%|5,82|3,88%|
|Dióxido de<br>Azufre (SO2)|Anual|μg/m3N|60|2,50|0,01|2,51|4,2%|0,00|0,00%|2,51|4,18%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

121

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Tabla 3-53 - Concentración total esperada, estación Club Deportivo 23 de marzo. Fase de Construcción.**

|Contaminante|Período|Unidad|Normativa<br>vigente|Línea de Base|Col6|Col7|Col8|Aporte del proyecto|Col10|Concentración Total|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Período**|**Unidad**|**Normativa**<br>**vigente**|**Valor**|**Aporte**<br>**otros**<br>**proyectos**|**Total**|**Porcentaje**<br>**de la**<br>**norma**|**Valor**|**Porcentaje**<br>**de la**<br>**norma**|**Valor**|**Porcentaje**<br>**de la**<br>**norma**|
|Material<br>Particulado<br>Respirable<br>Fino (MP2,5)|P98 24h|μg/m3|50|11,00|0,11|11,11|22,00%|0,00|0,01%|11,12|22,23%|
|Material<br>Particulado<br>Respirable<br>Fino (MP2,5)|Anual|μg/m3|20|7,00|0,06|7,06|35,00%|0,00|0,00%|7,06|35,29%|
|Material<br>Particulado<br>Respirable<br>(MP10)|P98 24h|μg/m3N|130|68,00|0,44|68,44|52,31%|0,01|0,01%|68,45|52,66%|
|Material<br>Particulado<br>Respirable<br>(MP10)|Anual|μg/m3N|50|42,80|0,23|43,03|85,60%|0,00|0,00%|43,03|86,06%|
|Dióxido de<br>Azufre (SO2)|P99 1h|μg/m3N|350|15,00|0,06|15,06|4,29%|0,01|0,00%|15,06|4,30%|
|Dióxido de<br>Azufre (SO2)|P99 24h|μg/m3N|150|7,50|0,02|7,52|5,00%|0,00|0,00%|7,52|5,02%|
|Dióxido de<br>Azufre (SO2)|Anual|μg/m3N|60|2,30|0,01|2,31|3,83%|0,00|0,00%|2,31|3,85%|

Fuente: Elaboración propia.

**Tabla 3-54 - Concentración total esperada, estación Colegio Pedro Vergara Keller. Fase de Construcción.**

|Contaminante|Período|Unidad|Normativa<br>vigente|Línea de Base|Col6|Col7|Col8|Aporte del proyecto|Col10|Concentración Total|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Período**|**Unidad**|**Normativa**<br>**vigente**|**Valor**|**Aporte**<br>**otros**<br>**proyectos**|**Total**|**Porcentaje**<br>**de la**<br>**norma**|**Valor**|**Porcentaje**<br>**de la**<br>**norma**|**Valor**|**Porcentaje**<br>**de la**<br>**norma**|
|Material<br>Particulado<br>Respirable<br>Fino (MP2,5)|P98 24h|μg/m3|50|15|0,18|15,18|30,00%|0,00|0,01%|15,18|30,36%|
|Material<br>Particulado<br>Respirable<br>Fino (MP2,5)|Anual|μg/m3|20|9,6|0,09|9,69|48,00%|0,00|0,00%|9,69|48,47%|
|Material<br>Particulado<br>Respirable<br>(MP10)|P98 24h|μg/m3N|130|83|0,69|83,69|63,85%|0,01|0,01%|83,70|64,39%|
|Material<br>Particulado<br>Respirable<br>(MP10)|Anual|μg/m3N|50|46,7|0,38|47,08|93,40%|0,00|0,00%|47,08|94,16%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

122

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

De los resultados anteriormente presentados, es posible observar que los aportes del Proyecto en

los puntos de ubicación de las Estaciones Centro, Colegio Pedro Vergara Keller y Club Deportivo 23

de marzo son bajos o, incluso nulos, ya que, para todos los estadígrafos de los contaminantes

analizados, los aportes del proyecto no superan el 0,12% de las normas respectivas, por lo que no

modifican los valores basales de calidad del aire de la ciudad de Calama.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

123

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

### 4. DETERMINACIÓN DEL ÁREA DE INFLUENCIA DEL PROYECTO

Para el estudio de los impactos o efectos potencialmente significativos en la calidad del aire

producidos por el Proyecto, el área de estudio debe comprender el espacio de donde se ubican las

fuentes de emisión, receptores sensibles y el que comprende la dispersión de los contaminantes

emitidos. De esta forma, para predecir y evaluar el potencial riesgo para la salud de la población

dicha área debe comprender el espacio con presencia de población expuesta a los contaminantes

emitidos por el proyecto [6] .

En el caso específico del presente estudio, el contaminante de mayor relevancia corresponde al

MP10. Esto, considerando la naturaleza de las emisiones generadas por el proyecto y la cercanía de

la ciudad de Calama, la cual corresponde a una zona saturada por el contaminante MP10 mediante

Decreto 57/2009 del MINSEGPRES “Declara Zona Saturada por Material Particulado Respirable

MP10, a la ciudad de Calama y su área circundante”, que establece un área en la que se encuentra

inserta el Proyecto en evaluación. Es relevante indicar que la zona declarada como saturada contará

con un Plan de Descontaminación Atmosférica (PDA) en el corto plazo.

En base a lo anterior, el área de influencia se determinó utilizando las curvas de isoconcentración

de dicho contaminante, para lo cual se ha establecido como límite aquella concentración que es

significativa numéricamente, es decir, a partir de la curva para el Percentil 98 de los promedios

diarios de MP10, se ha considerado un valor de 0,5 [μg/m3N]. Este valor se justifica en la

aproximación de los resultados obtenidos al entero próximo, de acuerdo con el procedimiento

establecido en la norma primaria de calidad del aire del contaminante en cuestión (DS N°59/1998,

modificado por el DS N°45/2001, MINSEGPRES). En la Figura 4-1 se presenta el área de influencia en

base a este componente.

6 Guía para la Descripción del Área de Influencia del SEA (SEA, 2017).

www.dfmconsultores.cl

**info@dfmconsultores.cl**

124

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**Figura 4-1 - Área de influencia del Proyecto - Componente Aire.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

125

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

### 5. CONCLUSIONES

La modelación de la fase de construcción corresponde al periodo en que se presentan las mayores

emisiones, comprendiendo los primeros 12 meses desde iniciada las actividades de construcción del

Proyecto.

De acuerdo con los resultados obtenidos se pueden mencionar las siguientes conclusiones:

 - Conforme con el análisis de incertidumbre realizado, se concluye que el modelo representa

de manera aceptable las variables velocidad del viento y temperatura, dados los valores de

estadígrafos de dispersión para velocidad del viento y temperatura, que manifiestan un

buen desempeño del modelo meteorológico WRF. Por ello, no se considera pertinente

realizar correcciones a los resultados obtenidos con el modelo CALPUFF.

 - Respecto a los aportes del proyecto de la Fase de Construcción a las concentraciones de los

contaminantes MP2.5, MP10, MPS, CO, NO 2 y SO 2 en los receptores de interés, es posible

establecer que estos son bajos o nulos, con excepción del aporte en el valor horario de NO 2

en el receptor R_12, el cual corresponde a una faena de extracción de lodos, en donde el

aporte del proyecto se cuantifica en un 2,12% de la normativa. No obstante, es importante

señalar que estos aportes son temporales y solo se presentarán en un período de tiempo

acotado, mientras se realice la construcción del Proyecto.

 - En cuanto a la concentración total esperada para las fases de construcción y cierre, se

observa que los aportes del proyecto en los puntos de ubicación de las Estaciones Centro,

Colegio Pedro Vergara Keller y Club Deportivo 23 de marzo son bajos o nulos (menores al

0,12% de la normativa respectiva, para cada contaminante y estadígrafo evaluados) y no

modifican la condición basal de calidad del aire.

Por tanto, a modo general y en vista de los resultados obtenidos, el Proyecto no generaría

impactos significativos en la calidad del aire en ninguno de los receptores de interés, como

tampoco sobre el área circundante relacionada a las fuentes emisoras del Proyecto, lo cual

implica que, con su ejecución, no existe riesgo a la salud.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

126

Modelación de Calidad del Aire Actualizado

**Parque Fotovoltaico Parina Solar**

Junio 2023

**ANEXO 1: ARCHIVOS DIGITALES MODELACIÓN**

En la siguiente tabla se detallan los archivos de entrada y salida de la modelación de calidad del aire

presentada en este estudio. Los archivos se listan según lo indicado en la “Guía para el uso de

modelos de calidad del aire en el SEIA”, considerando los archivos de entrada y salida de los módulos

CALMET, CALPUFF y CALPOST.

**Tabla 5-1. Archivos de modelación entregados.**

|Archivos|Entregado|Observación|
|---|---|---|
|**Archivos CALPUFF:**|**Archivos CALPUFF:**|**Archivos CALPUFF:**|
|- CALPUFF.DAT|NO|Corresponde al archivo CONC.DAT|
|- CALPUFF.LST|SI|-|
|- CALPUFF.INP|SI|-|
|- CONC.DAT|SI|-|
|- DFLX.DAT|SI|-|
|- WFLX.DAT|SI|-|
|**Archivos Meteorológicos:**|**Archivos Meteorológicos:**|**Archivos Meteorológicos:**|
|- CALMET.DAT|SI|Corresponde al archivo: calmetv6_Parina.dat|
|- GEO.DAT|SI|-|
|- SURF.DAT|NO|No fueron utilizados debido a que se usó, directamente en<br>CALPUFF, la meteorología proveniente del modelo<br>meteorológico WRF.|
|- UP.DAT|NO|NO|
|- CALMET.LST|NO|NO|
|- CALMET.INP|NO|NO|
|namelist.wps|SI|Archivo de configuración de preproceso de WRF (WPS)|
|namelist.input|SI|Archivo de configuración de WRF|
|**Archivos CALPOST:**|**Archivos CALPOST:**|**Archivos CALPOST:**|
|- CALPOST.DAT|SI|Los archivos se presentan en forma separada según<br>contaminantes y periodo.|
|- CALPOST.LST|SI|SI|
|- CALPOST.INP|SI|SI|
|**Archivos Complementarios:**|**Archivos Complementarios:**|**Archivos Complementarios:**|
|- Coastline Data File, Dry Flux Data File, Wet Flux<br>Data File, Ozone Data File, Chem Data File.|NO|No se incluyen, debido a que corresponden a datos que<br>no fueron modelados.|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

127

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2-1: - Resumen de emisiones atmosféricas. Fase de Construcción.****

| ACTIVIDAD | EMISIONES [t/Año 1 Construcción] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **ACTIVIDAD** | **MP2,5 ** | **MP10 ** | **MPS** | **CO** | **HC** | **SOx** | **NOx** |
| Movimiento de tierra | 1,39 | 3,07 | 13,48 |  |  |  |  |
| Tránsito por caminos no<br>pavimentados | 0,35 | 3,51 | 12,34 |  |  |  |  |
| Tránsito por caminos<br>pavimentados | 0,38 | 1,68 | 8,75 |  |  |  |  |
| Combustión vehículos<br>(Caminos No Pavimentados) | 0,00 | 0,00 | 0,00 | 0,01 | 0,00 | 0,00 | 0,12 |
| Combustión vehículos<br>(Caminos Pavimentados) | 0,02 | 0,02 | 0,02 | 0,05 | 0,01 | 0,00 | 1,87 |
| Combustión maquinarias | 0,04 | 0,05 | 0,05 | 7,65 | 1,10 | 3,15 | 15,45 |
| Grupo Electrógeno | 0,22 | 0,22 | 0,22 | 0,68 | 0,26 | 0,21 | 3,18 |
| **TOTAL** | **2,41** | **8,54** | **34,86** | **8,39** | **1,37** | **3,36** | **20,61** |

**Tabla 3-1.: Configuración parámetros principales WRF.****

| Parámetro | Valor |
| --- | --- |
| **Dominio** | **Dominio** |
| Resolución horizontal | 1 km |
| Proyección | Lambert |
| Número de niveles verticales | 44 |
| Niveles verticales (eta) | 0.000000, 0.051578, 0.101822, 0.150735, 0.198315, 0.244562, 0.289477,<br>0.333059,0.375309,0.416226,0.455810,<br>0.494062,<br>0.530982,<br>0.566569,<br>0.600823, 0.633745, 0.665334, 0.695591, 0.724515, 0.752107, 0.778366,<br>0.803292, 0.826886, 0.849148, 0.870076, 0.889673, 0.907937, 0.923302,<br>0.937101, 0.949333, 0.960000, 0.969101, 0.976635, 0.982603, 0.987005,<br>0.989841, 0.991111, 0.992381, 0.993651, 0.994921, 0.996190, 0.997460,<br>0.998730, 1.000000, |
| **Física** | **Física** |
| Esquema de radiación | RRTMG-fast (Onda corta y larga) |
| Modelo de suelo | Modelo Noah Land Surface |
| Tratamiento de capa superficial | Revised MM5 surface layer |
| Parametrización de capa límite | Yonsei University |
| Esquema de convección | Kain-Fritsch |
| Microfísica de nubes y precipitación | WSM 3-class |
| **Dinámica** | **Dinámica** |
| Parametrización de turbulencia | Smagorinsky |
| Núcleo dinámico | EM (Advanced Mass) y No hidroestático |
| Advección | positiva-definitiva |

**Tabla 3-2: - Estación de Monitoreo Meteorológico.****

| Nombre Estación | Ubicación<br>(Comuna) | Coordenadas UTM<br>(Datum WGS 84<br>Huso 19) | Col4 | Variables | Período |
| --- | --- | --- | --- | --- | --- |
| **Nombre Estación** | **Ubicación**<br>**(Comuna)** | **Este [m]** | **Norte [m]** | **Norte [m]** | **Norte [m]** |
| Hospital el Cobre | Calama | 509.427 | 7.517.292 | Temperatura | 2017-2019 |
| Hospital el Cobre | Calama | 509.427 | 7.517.292 | Dirección del Viento | 2017-2019 |
| Hospital el Cobre | Calama | 509.427 | 7.517.292 | Velocidad del Viento | 2017-2019 |
| Hospital el Cobre | Calama | 509.427 | 7.517.292 | Humedad Relativa | 2017-2019 |
| Hospital el Cobre | Calama | 509.427 | 7.517.292 | Presión Atmosférica | 2017-2019 |
| Hospital el Cobre | Calama | 509.427 | 7.517.292 | Precipitación | 2017-2019 |
| Hospital el Cobre | Calama | 509.427 | 7.517.292 | Radiación Solar | 2017-2019 |

**Tabla 3-3-: Resumen de información Velocidad del Viento observada. Estación El Cobre.****

| Parámetro | Variable | Año | Col4 | Col5 | Trienio |
| --- | --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2018** | **2019** | **2020** | **2020** |
| Velocidad de<br>Viento (m/s) | Promedio | 4,1 | 4,1 | 4,1 | 4,1 |
| Velocidad de<br>Viento (m/s) | Máximo | 8,8 | 10,4 | 10,6 | 8,8 |
| Velocidad de<br>Viento (m/s) | Mínimo | 0,1 | 0,1 | 0,1 | 0,1 |
| Porcentaje de Calmas (%) | Porcentaje de Calmas (%) | 1,1 | 1,0 | 1,3 | 1,1 |
| Datos Válidos (%) | Datos Válidos (%) | 99,9% | 100,0% | 99,8% | 99,9% |

**Tabla 3-4: - Frecuencia de distribución, velocidad y dirección del viento. Estación Hospital del Cobre.****

| Dirección | Col2 | Distribución Porcentual de Velocidad del Viento (m/s) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección** | **Dirección** | **0,50 - 2,10** | **2,10 - 3,60** | **3,60 - 5,70** | **5,70 - 8,80** | **8,80 - 11,10** | **>= 11,10** | **Total (%)** |
| 348,75 - 11,25 | N | 0,50% | 0,03% | 0,01% | 0,00% | 0,00% | 0,00% | 0,62% |
| 11,25 - 33,75 | NNE | 0,63% | 0,11% | 0,01% | 0,00% | 0,00% | 0,00% | 0,82% |
| 33,75 - 56,25 | NE | 1,21% | 1,11% | 0,20% | 0,01% | 0,00% | 0,00% | 2,60% |
| 56,25 - 78,75 | ENE | 2,18% | 7,10% | 4,03% | 0,12% | 0,00% | 0,00% | 13,50% |
| 78,75 - 101,25 | E | 2,00% | 8,07% | 14,34% | 3,97% | 0,00% | 0,00% | 28,43% |
| 101,25 - 123,75 | ESE | 1,07% | 1,44% | 1,32% | 0,09% | 0,00% | 0,00% | 3,99% |
| 123,75 - 146,25 | SE | 0,83% | 0,13% | 0,00% | 0,00% | 0,00% | 0,00% | 1,06% |
| 146,25 - 168,75 | SSE | 0,79% | 0,07% | 0,00% | 0,00% | 0,00% | 0,00% | 0,92% |
| 168,75 - 191,25 | S | 0,80% | 0,09% | 0,00% | 0,00% | 0,00% | 0,00% | 0,95% |
| 191,25 - 213,75 | SSW | 0,89% | 0,33% | 0,02% | 0,00% | 0,00% | 0,00% | 1,32% |
| 213,75 - 236,25 | SW | 1,15% | 1,06% | 0,52% | 0,11% | 0,00% | 0,00% | 2,91% |
| 236,25 - 258,75 | WSW | 1,28% | 2,82% | 6,94% | 8,02% | 0,01% | 0,00% | 19,15% |
| 258,75 - 281,25 | W | 0,98% | 2,52% | 6,08% | 8,89% | 0,01% | 0,00% | 18,56% |
| 281,25 - 303,75 | WNW | 0,72% | 0,56% | 0,98% | 0,96% | 0,01% | 0,00% | 3,30% |
| 303,75 - 326,25 | NW | 0,43% | 0,11% | 0,16% | 0,51% | 0,04% | 0,00% | 1,30% |
| 326,25 - 348,75 | NNW | 0,37% | 0,05% | 0,03% | 0,02% | 0,01% | 0,00% | 0,56% |
| Sub-Total | Sub-Total | 15,83% | 25,60% | 34,66% | 22,71% | 0,09% | 0,00% | 98,89% |
| Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | 1,11% |

**Tabla 3-5: - Resumen de información Temperatura observada. Estación El Cobre.****

| Parámetro | Variable | Año | Col4 | Col5 | Trienio |
| --- | --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2018** | **2019** | **2020** | **2020** |
| Temperatura<br>(°C) | Promedio | 14,9 | 15,3 | 15,2 | 15,14 |
| Temperatura<br>(°C) | Máximo | 29,0 | 29,2 | 28,5 | 29,18 |
| Temperatura<br>(°C) | Mínimo | 0,0 | -3,8 | -1,6 | -3,75 |
| Datos Válidos (%) | Datos Válidos (%) | 99,9% | 100,0% | 99,9% | 99,9% |

**Tabla 3-6: - Resumen de información Humedad Relativa observada. Estación El Cobre.****

| Parámetro | Variable | Año | Col4 | Col5 | Trienio |
| --- | --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2018** | **2019** | **2020** | **2020** |
| Humedad<br>Relativa (%) | Promedio | 25,66 | 25,25 | 26,22 | 25,71 |
| Humedad<br>Relativa (%) | Máximo | 89,69 | 98,87 | 100,00 | 100,00 |
| Humedad<br>Relativa (%) | Mínimo | 0,39 | 0,41 | 0,41 | 0,39 |
| % Datos Válidos | % Datos Válidos | 99,8% | 99,9% | 99,9% | 99,9% |

**Tabla 3-7-: Resumen de información Presión Atmosférica observada. Estación El Cobre.****

| Parámetro | Variable | Año | Col4 | Col5 | Trienio |
| --- | --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2018** | **2019** | **2020** | **2020** |
| Presión<br>Atmosférica<br>(hPa) | Promedio | 775,3 | 775,3 | 775,5 | 775,4 |
| Presión<br>Atmosférica<br>(hPa) | Máximo | 780,6 | 779,4 | 780,6 | 780,6 |
| Presión<br>Atmosférica<br>(hPa) | Mínimo | 768,8 | 771,0 | 770,8 | 768,8 |
| % Datos Válidos | % Datos Válidos | 99,9% | 100,0% | 99,8% | 99,9% |

**Tabla 3-8-: Resumen de información Radiación Solar observada. Estación El Cobre.****

| Parámetro | Variable | Año | Col4 | Col5 | Trienio |
| --- | --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2018** | **2019** | **2020** | **2020** |
| Radiación Solar<br>(W/m2) | Promedio | 284,7 | 281,7 | 280,7 | 282,3 |
| Radiación Solar<br>(W/m2) | Máximo | 1.143,0 | 1.153,6 | 1.129,0 | 1.153,6 |
| Radiación Solar<br>(W/m2) | Mínimo | 0,0 | 0,0 | 0,0 | 0,0 |
| % Datos Válidos | % Datos Válidos | 99,7% | 99,9% | 99,9% | 99,8% |

**Tabla 3-9-: Resumen de Información Velocidad del Viento año 2019. Estación Hospital El Cobre.****

| Parámetro | Variable | Valor |
| --- | --- | --- |
| Velocidad de Viento<br>[m/s] | Promedio | 3,35 |
| Velocidad de Viento<br>[m/s] | Máximo | 15,98 |
| Velocidad de Viento<br>[m/s] | Mínimo | 0,04 |

**Tabla 3-10: - Frecuencia de distribución de velocidad y dirección del viento modelados en Estación Hospital****

| Dirección | Col2 | Distribución Porcentual de Velocidad del Viento (m/s) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección** | **Dirección** | **0,50 - 2,10** | **2,10 - 3,60** | **3,60 - 5,70** | **5,70 - 8,80** | **8,80 - 11,10** | **>= 11,10** | **Total (%)** |
| 348,75 - 11,25 | N | 0,47% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% | 0,48% |
| 11,25 - 33,75 | NNE | 0,81% | 0,07% | 0,01% | 0,01% | 0,00% | 0,00% | 0,90% |
| 33,75 - 56,25 | NE | 2,26% | 0,71% | 0,03% | 0,00% | 0,00% | 0,00% | 3,00% |
| 56,25 - 78,75 | ENE | 7,85% | 4,70% | 0,26% | 0,00% | 0,00% | 0,00% | 12,82% |
| 78,75 - 101,25 | E | 6,70% | 10,67% | 6,26% | 0,11% | 0,00% | 0,00% | 23,74% |
| 101,25 - 123,75 | ESE | 1,23% | 0,27% | 0,30% | 0,01% | 0,00% | 0,00% | 1,82% |
| 123,75 - 146,25 | SE | 0,81% | 0,02% | 0,00% | 0,00% | 0,00% | 0,00% | 0,83% |
| 146,25 - 168,75 | SSE | 0,78% | 0,05% | 0,00% | 0,00% | 0,00% | 0,00% | 0,82% |
| 168,75 - 191,25 | S | 0,95% | 0,07% | 0,00% | 0,01% | 0,00% | 0,00% | 1,03% |
| 191,25 - 213,75 | SSW | 1,47% | 0,18% | 0,05% | 0,00% | 0,00% | 0,00% | 1,70% |
| 213,75 - 236,25 | SW | 2,01% | 0,89% | 0,22% | 0,06% | 0,00% | 0,00% | 3,17% |
| 236,25 - 258,75 | WSW | 2,82% | 3,18% | 13,14% | 7,44% | 0,03% | 0,00% | 26,62% |
| 258,75 - 281,25 | W | 1,97% | 1,97% | 5,09% | 6,05% | 0,03% | 0,00% | 15,13% |
| 281,25 - 303,75 | WNW | 1,20% | 0,62% | 1,18% | 1,16% | 0,06% | 0,01% | 4,22% |
| 303,75 - 326,25 | NW | 0,49% | 0,09% | 0,06% | 0,18% | 0,08% | 0,06% | 0,96% |
| 326,25 - 348,75 | NNW | 0,31% | 0,01% | 0,01% | 0,00% | 0,00% | 0,00% | 0,33% |
| Sub-Total | Sub-Total | 32,13% | 23,53% | 26,60% | 15,05% | 0,21% | 0,07% | 97,58% |
| Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | 2,42% |

**Tabla 3-11: - Resumen de Información Temperatura modelada en Hospital El Cobre, año 2019.****

| Parámetro | Variable | Valor |
| --- | --- | --- |
| Temperatura [°C] | Promedio | 14,79 |
| Temperatura [°C] | Máximo | 26,360 |
| Temperatura [°C] | Mínimo | -1,630 |

**Tabla 3-12: - Resumen de Información Altura de Capa de Mezcla modelada en Estación Hospital El Cobre,****

| Parámetro | Variable | Valor |
| --- | --- | --- |
| Altura de Capa de Mezcla [m] | Promedio | 539 |
| Altura de Capa de Mezcla [m] | Máxima | 3298 |
| Altura de Capa de Mezcla [m] | Mínima | 10 |

**Tabla 3-13: - Estadígrafos de Dispersión para Velocidad del Viento y Temperatura.****

| Medida de Error | Estación Hospital del Cobre | Col3 |
| --- | --- | --- |
| **Medida de Error** | **Velocidad del Viento** | **Temperatura** |
| Sesgo | -0,73 m/s | -0,55 °C |
| ECM | 1,06 m/s | 1,10 °C |
| r | 0,85 | 0,99 |

**Tabla 3-14.: Principales índices evaluación cambio climático. Región de Antofagasta, provincia El Loa,****

| Índice | Periodo | Valor |
| --- | --- | --- |
| Temperatura media anual (°C) | Presente | 8,32 |
| Temperatura media anual (°C) | Futuro | 10,47 |
| Temperatura media anual (°C) | Cambio (Futuro - Presente) | 2,15 |
| Precipitación acumulada anual (mm) | Presente | 83,84 |
| Precipitación acumulada anual (mm) | Futuro | 88,30 |
| Precipitación acumulada anual (mm) | Cambio (Futuro - Presente) | 4,45 |
| Velocidad viento promedio anual (m/s) | Presente | 4,75 |
| Velocidad viento promedio anual (m/s) | Futuro | 4,79 |
| Velocidad viento promedio anual (m/s) | Cambio (Futuro - Presente) | 0,03 |

**Tabla 3-15: - Normas de calidad del aire.****

| Contaminante | Decreto<br>Aplicable | Norma | Col4 | Periodo de Evaluación de Cumplimiento de<br>Norma |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Decreto**<br>**Aplicable** | **Valor** | **Unidad** | **Unidad** |
| Material Particulado<br>Respirable Fino<br>(MP2,5) | Decreto Supremo<br>N°12/2011 | 50 | μg/m3 | Percentil 98 de la media aritmética diaria durante<br>un año. |
| Material Particulado<br>Respirable Fino<br>(MP2,5) | Decreto Supremo<br>N°12/2011 | 20 | 20 | Media aritmética trianual |
| Material Particulado<br>Respirable (MP10) | Decreto Supremo<br>N°12/2021 | 130 | μg/m3N | Percentil 98 de la media aritmética diaria durante<br>un año. |
| Material Particulado<br>Respirable (MP10) | Decreto Supremo<br>N°12/2021 | 50 | 50 | Media aritmética trianual. |
| Dióxido de<br>nitrógeno (NO2) | Decreto Supremo<br>No114/2002 | 400 | μg/m3N | Percentil 99 de la media aritmética horaria<br>durante un año. |
| Dióxido de<br>nitrógeno (NO2) | Decreto Supremo<br>No114/2002 | 100 | 100 | Media aritmética trianual. |
| Dióxido de azufre<br>(SO2) | Decreto Supremo<br>N°104/2019 | 350 | μg/m3N | Percentil 99 de las concentraciones de 1 hora. |
| Dióxido de azufre<br>(SO2) | Decreto Supremo<br>N°104/2019 | 150 | 150 | Percentil 99 de las concentraciones de 24 horas |
| Dióxido de azufre<br>(SO2) | Decreto Supremo<br>N°104/2019 | 60 | 60 | Concentración anual |
| Monóxido de<br>Carbono (CO) | Decreto Supremo<br>N°115/2002 | 30 | mg/m3N | Percentil 99 de la media aritmética horaria<br>durante un año. |
| Monóxido de<br>Carbono (CO) | Decreto Supremo<br>N°115/2002 | 10 | 10 | Percentil 99 de la media aritmética de 8 horas<br>durante un año. |
| Material Particulado<br>Sedimentable (MPS) | Norma de<br>Referencia<br>Decreto Supremo<br>N°04/1992 | 150 | mg/m2/día | Media aritmética mensual |
| Material Particulado<br>Sedimentable (MPS) | Norma de<br>Referencia<br>Decreto Supremo<br>N°04/1992 | 100 | 100 | Media aritmética anual |

**Tabla 3-16: - Caracterización de estación de monitoreo de calidad del aire.****

| Estación | Coordenadas UTM 18S WGS 84 | Col3 | Contaminantes<br>Medidos | Periodo de<br>Análisis |
| --- | --- | --- | --- | --- |
| **Estación** | **Este** | **Norte** | **Norte** | **Norte** |
| Estación Centro | 507.389 | 7.516.053 | MP2,5, MP10, CO,<br>NO2, SO2 | 2020 - 2022 |
| Colegio Pedro<br>Vergara Keller | 506.893 | 7.518.227 | MP2,5, MP10 | 2020 - 2022 |
| Club Deportivo 23<br>de marzo | 506.399 | 7.516.241 | MP2,5, MP10, SO2 | 2020 - 2022 |

**Tabla 3-17.: Resultados Monitoreo de MP2.5. Estación Centro.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2020** | **2021** | **2022** |
| MP2,5 (μg/m3) | Número de datos medidos | 366 | 365 | 365 |
| MP2,5 (μg/m3) | Número de datos válidos | 341 | 346 | 349 |
| MP2,5 (μg/m3) | Porcentaje de datos válidos | 93% | 95% | 96% |
| MP2,5 (μg/m3) | Mínimo diario | 0,0 | 0,0 | 2,0 |
| MP2,5 (μg/m3) | Máximo diario | 14,0 | 10,0 | 23,0 |
| MP2,5 (μg/m3) | Percentil 98 diario | 10,0 | 7,0 | 13,0 |
| MP2,5 (μg/m3) | Media anual | 5,2 | 4,4 | 5,3 |
| MP2,5 (μg/m3) | Media trianual | 5,0 | 5,0 | 5,0 |

**Tabla 3-18.: Comparación de Monitoreo de MP2.5 con Normativa. Estación Centro.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP2,5 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 98 de la<br>concentración media diaria | 13,0 | 50 | μg/m3 | 26,0% |
| MP2,5 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media<br>trianual | 5,0 | 20 | μg/m3 | 25,0% |

**Tabla 3-19.: Resultados Monitoreo de MP10. Estación Centro.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2020** | **2021** | **2022** |
| MP10 (μg/m3N) | Número de datos medidos | 366 | 365 | 365 |
| MP10 (μg/m3N) | Número de datos válidos | 336 | 345 | 349 |
| MP10 (μg/m3N) | Porcentaje de datos válidos | 92% | 95% | 96% |
| MP10 (μg/m3N) | Mínimo diario | 14,0 | 6,0 | 12,0 |
| MP10 (μg/m3N) | Máximo diario | 104,0 | 66,0 | 50,0 |
| MP10 (μg/m3N) | Percentil 98 diario | 48,0 | 37,0 | 42,0 |
| MP10 (μg/m3N) | Media anual | 29,7 | 21,0 | 26,3 |
| MP10 (μg/m3N) | Media trianual | 25,7 | 25,7 | 25,7 |

**Tabla 3-20.: Comparación de Monitoreo de MP10 con Normativa. Estación Centro.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | 1 de enero de 2020 - 31 de<br>diciembre de 2022 | Percentil 98 de la<br>concentración media diaria | 26,3 | 130 | μg/m3N | 20,3% |
| MP10 | 1 de enero de 2020 - 31 de<br>diciembre de 2022 | Concentración media<br>trianual | 25,7 | 50 | μg/m3N | 51,4% |

**Tabla 3-21.: Resultados Monitoreo de CO. Estación Centro.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2020** | **2021** | **2022** |
| CO (mg/m3N) | Número de datos medidos | 8.784 | 8.760 | 8.760 |
| CO (mg/m3N) | Número de datos válidos | 8.682 | 8.676 | 8.441 |
| CO (mg/m3N) | Porcentaje de datos válidos | 99% | 99% | 96% |
| CO (mg/m3N) | Mínimo horario | 0,0 | 0,0 | 0,0 |
| CO (mg/m3N) | Máximo horario | 1,4 | 1,8 | 2,4 |
| CO (mg/m3N) | Percentil 99 de los máximos diarios de concentración<br>horaria | 1,1 | 1,4 | 1,9 |
| CO (mg/m3N) | Promedio trianual percentil 99 de los máximos diarios<br>de concentración horaria | 1,5 | 1,5 | 1,5 |
| CO (mg/m3N) | Percentil 99 de los máximos diarios de concentración<br>media móvil de 8 horas | 0,6 | 0,9 | 1,0 |
| CO (mg/m3N) | Promedio trianual percentil 99 de los máximos diarios<br>de concentración media móvil de 8 horas | 0,8 | 0,8 | 0,8 |

**Tabla 3-22.: Comparación de Monitoreo de CO con normativa. Estación Centro.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| CO | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora | 1,5 | 30 | mg/m3N | 5,0% |
| CO | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 99 de los<br>máximos diarios de<br>concentración de 8 horas | 0,8 | 10 | mg/m3N | 8,0% |

**Tabla 3-23.: Resultados Monitoreo de NO** **2** **. Estación Centro.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2020** | **2021** | **2022** |
| NO2 (μg/m3N) | Número de datos medidos | 8.784 | 8.760 | 8.760 |
| NO2 (μg/m3N) | Número de datos válidos | 8.520 | 8.319 | 8.600 |
| NO2 (μg/m3N) | Porcentaje de datos válidos | 97% | 95% | 98% |
| NO2 (μg/m3N) | Mínimo horario | 0,5 | 0,0 | 2,5 |
| NO2 (μg/m3N) | Máximo horario | 91,2 | 95,5 | 103,7 |
| NO2 (μg/m3N) | Percentil 99 de los máximos diarios de<br>concentración horaria | 79,6 | 85,7 | 95,4 |
| NO2 (μg/m3N) | Promedio trianual percentil 99 de los máximos<br>diarios de concentración horaria | 86,9 | 86,9 | 86,9 |
| NO2 (μg/m3N) | Media anual | 12,9 | 18,3 | 21,2 |
| NO2 (μg/m3N) | Media trianual | 17,5 | 17,5 | 17,5 |

**Tabla 3-24.: Comparación con normativa de dióxido de nitrógeno (NO** **2** **). Estación Centro.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| NO2 | 1 de enero de 2020<br>- 31 de diciembre<br>de 2022 | Percentil 99 de los máximos<br>diarios de concentración de 1 hora | 86,9 | 400 | μg/m3N | 21,7% |
| NO2 | 1 de enero de 2020<br>- 31 de diciembre<br>de 2022 | Concentración media trianual | 17,5 | 100 | μg/m3N | 17,5% |

**Tabla 3-25.: Resultados Monitoreo de SO** **2** **. Estación Centro.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2020** | **2021** | **2022** |
| SO2 (μg/m3N) | Número de datos medidos | 8.784 | 8.760 | 8.760 |
| SO2 (μg/m3N) | Número de datos válidos | 8.682 | 8.529 | 8.614 |
| SO2 (μg/m3N) | Porcentaje de datos válidos | 99% | 97% | 98% |
| SO2 (μg/m3N) | Mínimo horario | 0,8 | 0,1 | 0,1 |
| SO2 (μg/m3N) | Máximo horario | 137,8 | 74,2 | 155,3 |
| SO2 (μg/m3N) | Percentil 99 de concentración horaria | 13,7 | 7,3 | 13,3 |
| SO2 (μg/m3N) | Promedio trianual percentil 99 de concentración horaria | 11,4 | 11,4 | 11,4 |
| SO2 (μg/m3N) | Percentil 99 de concentración diaria | 6,2 | 4,4 | 6,8 |
| SO2 (μg/m3N) | Promedio trianual percentil 99 de concentración diaria | 5,8 | 5,8 | 5,8 |
| SO2 (μg/m3N) | Media anual | 2,7 | 2,2 | 2,7 |
| SO2 (μg/m3N) | Media trianual | 2,5 | 2,5 | 2,5 |

**Tabla 3-26.: Comparación de Monitoreo de SO** **2** **con Normativa. Estación Centro.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| SO2 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 99 de<br>concentración horaria | 11,4 | 350 | μg/m3N | 3,3% |
| SO2 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 99 de la<br>concentración media diaria | 5,8 | 150 | μg/m3N | 3,9% |
| SO2 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media<br>trianual | 2,5 | 60 | μg/m3N | 4,2% |

**Tabla 3-27.: Resultados Monitoreo de MP2.5. Estación Club Deportivo 23 de marzo.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2020** | **2021** | **2022** |
| MP2,5 (μg/m3) | Número de datos medidos | 366 | 365 | 365 |
| MP2,5 (μg/m3) | Número de datos válidos | 354 | 345 | 347 |
| MP2,5 (μg/m3) | Porcentaje de datos válidos | 97% | 95% | 95% |
| MP2,5 (μg/m3) | Mínimo diario | 2,0 | 3,0 | 3,0 |
| MP2,5 (μg/m3) | Máximo diario | 36,0 | 19,0 | 32,0 |
| MP2,5 (μg/m3) | Percentil 98 diario | 16,0 | 12,0 | 11,0 |
| MP2,5 (μg/m3) | Media anual | 7,4 | 6,9 | 6,6 |
| MP2,5 (μg/m3) | Media trianual | 7,0 | 7,0 | 7,0 |

**Tabla 3-28.: Comparación de Monitoreo con Normativa. Estación Club Deportivo 23 de marzo.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP2,5 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 98 de la<br>concentración media diaria | 11,0 | 50 | μg/m3 | 22,0% |
| MP2,5 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media<br>trianual | 7,0 | 20 | μg/m3 | 35,0% |

**Tabla 3-29.: Resultados Monitoreo de MP10. Estación Club Deportivo 23 de marzo.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2020** | **2021** | **2022** |
| MP10 (μg/m3N) | Número de datos medidos | 366 | 365 | 365 |
| MP10 (μg/m3N) | Número de datos válidos | 354 | 345 | 347 |
| MP10 (μg/m3N) | Porcentaje de datos válidos | 97% | 95% | 95% |
| MP10 (μg/m3N) | Mínimo diario | 12,0 | 24,0 | 23,0 |
| MP10 (μg/m3N) | Máximo diario | 109,0 | 142,0 | 77,0 |
| MP10 (μg/m3N) | Percentil 98 diario | 60,0 | 77,0 | 68,0 |
| MP10 (μg/m3N) | Media anual | 39,0 | 45,5 | 43,8 |
| MP10 (μg/m3N) | Media trianual | 42,8 | 42,8 | 42,8 |

**Tabla 3-30.: Comparación de Monitoreo de MP10 con Normativa. Estación Club Deportivo 23 de marzo.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 98 de la<br>concentración media diaria | 68,0 | 130 | μg/m3N | 52,3% |
| MP10 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media<br>trianual | 42,8 | 50 | μg/m3N | 85,6% |

**Tabla 3-31.: Resultados Monitoreo de SO** **2** **. Estación Club Deportivo 23 de marzo.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2020** | **2021** | **2022** |
| SO2 (μg/m3N) | Número de datos medidos | 8.784 | 8.760 | 8.760 |
| SO2 (μg/m3N) | Número de datos válidos | 8.545 | 8.520 | 8.607 |
| SO2 (μg/m3N) | Porcentaje de datos válidos | 97% | 97% | 98% |
| SO2 (μg/m3N) | Mínimo horario | 0,0 | 0,1 | 0,4 |
| SO2 (μg/m3N) | Máximo horario | 151,0 | 176,0 | 170,8 |
| SO2 (μg/m3N) | Percentil 99 de concentración horaria | 12,6 | 11,9 | 20,5 |
| SO2 (μg/m3N) | Promedio trianual percentil 99 de concentración horaria | 15,0 | 15,0 | 15,0 |
| SO2 (μg/m3N) | Percentil 99 de concentración diaria | 6,8 | 5,3 | 10,2 |
| SO2 (μg/m3N) | Promedio trianual percentil 99 de concentración diaria | 7,5 | 7,5 | 7,5 |
| SO2 (μg/m3N) | Media anual | 1,6 | 2,2 | 2,9 |
| SO2 (μg/m3N) | Media trianual | 2,3 | 2,3 | 2,3 |

**Tabla 3-32.: Comparación de Monitoreo de SO** **2** **con Normativa. Estación Club Deportivo 23 de marzo.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| SO2 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 99 de<br>concentración horaria | 15,0 | 350 | μg/m3N | 4,3% |
| SO2 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 99 de la<br>concentración media diaria | 7,5 | 150 | μg/m3N | 5,0% |
| SO2 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media<br>trianual | 2,3 | 60 | μg/m3N | 3,8% |

**Tabla 3-33.: Resultados Monitoreo de MP2.5. Estación Colegio Pedro Vergara Keller.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2020** | **2021** | **2022** |
| MP2,5 (μg/m3) | Número de datos medidos | 366 | 365 | 365 |
| MP2,5 (μg/m3) | Número de datos válidos | 342 | 350 | 335 |
| MP2,5 (μg/m3) | Porcentaje de datos válidos | 93% | 96% | 92% |
| MP2,5 (μg/m3) | Mínimo diario | 4,0 | 3,0 | 3,0 |
| MP2,5 (μg/m3) | Máximo diario | 50,0 | 45,0 | 51,0 |
| MP2,5 (μg/m3) | Percentil 98 diario | 17,0 | 21,0 | 15,0 |
| MP2,5 (μg/m3) | Media anual | 8,5 | 10,9 | 9,5 |
| MP2,5 (μg/m3) | Media trianual | 9,6 | 9,6 | 9,6 |

**Tabla 3-34.: Comparación de Monitoreo con Normativa de MP2,5. Estación Colegio Pedro Vergara Keller.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP2,5 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 98 de la<br>concentración media diaria | 15,0 | 50 | μg/m3 | 30,0% |
| MP2,5 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media<br>trianual | 9,6 | 20 | μg/m3 | 48,0% |

**Tabla 3-35.: Resultados Monitoreo de MP10. Estación Colegio Pedro Vergara Keller.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2020** | **2021** | **2022** |
| MP10 (μg/m3N) | Número de datos medidos | 366 | 365 | 365 |
| MP10 (μg/m3N) | Número de datos válidos | 342 | 349 | 335 |
| MP10 (μg/m3N) | Porcentaje de datos válidos | 93% | 96% | 92% |
| MP10 (μg/m3N) | Mínimo diario | 16,0 | 18,0 | 21,0 |
| MP10 (μg/m3N) | Máximo diario | 233,0 | 113,0 | 118,0 |
| MP10 (μg/m3N) | Percentil 98 diario | 72,0 | 75,0 | 83,0 |
| MP10 (μg/m3N) | Media anual | 44,3 | 46,4 | 49,5 |
| MP10 (μg/m3N) | Media trianual | 46,7 | 46,7 | 46,7 |

**Tabla 3-36.: Comparación de Monitoreo con Normativa de MP10. Estación Colegio Pedro Vergara Keller.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 98 de la<br>concentración media diaria | 83,0 | 130 | μg/m3N | 63,8% |
| MP10 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media<br>trianual | 46,7 | 50 | μg/m3N | 93,4% |

**Tabla 3-37: - Resumen Línea Base de Calidad del Aire, Estación Centro.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje<br>de la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP2,5 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 98 de la<br>concentración media diaria | 13,0 | 50 | μg/m3 | 26,0% |
| MP2,5 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media trianual | 5,0 | 20 | μg/m3 | 25,0% |
| MP10 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 98 de la<br>concentración media diaria | 26,3 | 130 | μg/m3N | 20,3% |
| MP10 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media trianual | 25,7 | 50 | μg/m3N | 51,4% |
| CO | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 99 de los máximos<br>diarios de concentración de 1<br>hora | 1,5 | 30 | mg/m3N | 5,0% |
| CO | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 99 de los máximos<br>diarios de concentración de 8<br>horas | 0,8 | 10 | mg/m3N | 8,0% |
| NO2 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 99 de los máximos<br>diarios de concentración de 1<br>hora | 86,9 | 400 | μg/m3N | 21,7% |
| NO2 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media trianual | 17,5 | 100 | μg/m3N | 17,5% |
| SO2 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 99 de concentración<br>horaria | 11,4 | 350 | μg/m3N | 3,3% |
| SO2 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 99 de la<br>concentración media diaria | 5,8 | 150 | μg/m3N | 3,9% |
| SO2 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media trianual | 2,5 | 60 | μg/m3N | 4,2% |

**Tabla 3-38: - Resumen Línea Base de Calidad del Aire, Estación Club Deportivo 23 de marzo.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP2,5 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 98 de la<br>concentración media diaria | 11,0 | 50 | μg/m3 | 22,0% |
| MP2,5 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media<br>trianual | 7,0 | 20 | μg/m3 | 35,0% |
| MP10 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 98 de la<br>concentración media diaria | 68,0 | 130 | μg/m3N | 52,3% |
| MP10 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media<br>trianual | 42,8 | 50 | μg/m3N | 85,6% |
| SO2 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 99 de<br>concentración horaria | 15,0 | 350 | μg/m3N | 4,3% |
| SO2 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 99 de la<br>concentración media diaria | 7,5 | 150 | μg/m3N | 5,0% |
| SO2 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media<br>trianual | 2,3 | 60 | μg/m3N | 3,8% |

**Tabla 3-39: - Resumen Línea Base de Calidad del Aire, Estación Colegio Pedro Vergara Keller.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP2,5 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 98 de la<br>concentración media diaria | 15,0 | 50 | μg/m3 | 30,0% |
| MP2,5 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media<br>trianual | 9,6 | 20 | μg/m3 | 48,0% |
| MP10 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Percentil 98 de la<br>concentración media diaria | 83,0 | 130 | μg/m3N | 63,8% |
| MP10 | 1 de enero de 2020 - 31<br>de diciembre de 2022 | Concentración media<br>trianual | 46,7 | 50 | μg/m3N | 93,4% |

**Tabla 3-40.: Fuentes Emisoras Fase de Construcción.****

| ID | Descripción | Tipo de<br>fuente | Tasas de emisión | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **Descripción** | **Tipo de**<br>**fuente** | **MP2.5** | **MP10** | **MPS** | **CO** | **NO2 ** | **SO2 ** | **Unidad** |
| SRC_1 | Área proyecto | Areal | 7,04E-08 | 1,39E-07 | 5,65E-07 | 4,12E-07 | 9,24E-07 | 1,67E-07 | g/s/m2 |
| SRC_2 | Acceso | Camino | 1,70E-05 | 1,70E-04 | 5,96E-04 | 1,21E-07 | 3,77E-06 | 6,20E-09 | g/s/m |
| SRC_3 | Tramo A | Camino | 6,54E-07 | 2,75E-06 | 1,41E-05 | 9,48E-08 | 2,95E-06 | 4,86E-09 | g/s/m |
| SRC_4 | Tramo B | Camino | 1,98E-06 | 1,98E-05 | 6,97E-05 | 2,74E-09 | 1,00E-07 | 1,64E-10 | g/s/m |
| SRC_5 | Tramo C | Camino | 6,27E-07 | 2,64E-06 | 1,35E-05 | 9,21E-08 | 2,86E-06 | 4,70E-09 | g/s/m |
| SRC_6 | Tramo D | Camino | 4,73E-07 | 1,96E-06 | 1,00E-05 | 7,25E-08 | 2,11E-06 | 3,48E-09 | g/s/m |
| SRC_7 | Tramo E | Camino | 1,57E-07 | 6,86E-07 | 3,56E-06 | 2,00E-08 | 7,61E-07 | 1,24E-09 | g/s/m |
| SRC_8 | Camino interno | Camino | 4,02E-06 | 4,00E-05 | 1,41E-04 | 1,84E-07 | 4,09E-07 | 1,18E-09 | g/s/m |
| SRC_9 | LTE | Lineal-areal | 2,95E-08 | 6,51E-08 | 2,85E-07 | 8,50E-09 | 1,07E-08 | 1,09E-09 | g/s/m2 |

**Tabla 3-41-: Receptores de Interés.****

| Receptor | Descripción | Coordenadas de Ubicación<br>Datum WGS 84 | Col4 | Altitud<br>(m.s.n.m.) |
| --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Este [m]** | **Norte [m]** | **Norte [m]** |
| R_1 | R01 Ruido | 508.146 | 7.519.542 | 2279,2 |
| R_2 | R02 Ruido | 508.855 | 7.519.417 | 2288,2 |
| R_3 | R03 Ruido | 509.284 | 7.519.382 | 2297,1 |
| R_4 | R04 Ruido | 510.263 | 7.519.143 | 2313,1 |
| R_5 | R05 Ruido | 513.147 | 7.519.045 | 2357,6 |
| R_6 | R06 Ruido | 513.721 | 7.518.530 | 2373,9 |
| R_7 | R07 Ruido | 513.958 | 7.518.635 | 2376,5 |
| R_8 | R08 Ruido | 513.226 | 7.517.661 | 2364,4 |
| R_9 | R09 Ruido | 514.502 | 7.516.108 | 2380,3 |
| R_10 | R10 Ruido | 519.188 | 7.513.097 | 2445,1 |
| R_11 | R11 Ruido | 519.867 | 7.513.436 | 2450,8 |
| R_12 | R12 Ruido | 523.573 | 7.510.935 | 2465,9 |
| R_13 | Estación Centro | 507.371 | 7.516.056 | 2265,3 |
| R_14 | Colegio Pedro Vergara Keller | 506.895 | 7.518.221 | 2260,8 |
| R_15 | Club Deportivo 23 de marzo | 506.403 | 7.516.233 | 2253,2 |

**Tabla 3-42: - Resultados de modelo de dispersión de MP2.5. Fase de Construcción.****

| Receptor | Descripción | Material Particulado Respirable Fino (MP2,5) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [μg/m3] ** | **Concentración [μg/m3] ** | **Norma de Calidad** | **Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Percentil 98**<br>**24 horas** | **Período Anual** | **Percentil 98**<br>**24 horas** | **Período Anual** | **Percentil 98**<br>**24 horas** | **Período Anual** |
| R_1 | R01 | 0,01 | 0,00 | 50 | 20 | 0,01% | 0,01% |
| R_2 | R02 | 0,01 | 0,00 | 0,00 | 0,00 | 0,02% | 0,01% |
| R_3 | R03 | 0,01 | 0,00 | 0,00 | 0,00 | 0,02% | 0,01% |
| R_4 | R04 | 0,01 | 0,00 | 0,00 | 0,00 | 0,01% | 0,01% |
| R_5 | R05 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01% | 0,01% |
| R_6 | R06 | 0,01 | 0,00 | 0,00 | 0,00 | 0,02% | 0,02% |
| R_7 | R07 | 0,03 | 0,01 | 0,01 | 0,01 | 0,06% | 0,06% |
| R_8 | R08 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01% | 0,00% |
| R_9 | R09 | 0,01 | 0,00 | 0,00 | 0,00 | 0,01% | 0,00% |
| R_10 | R10 | 0,02 | 0,00 | 0,00 | 0,00 | 0,03% | 0,02% |
| R_11 | R11 | 0,01 | 0,00 | 0,00 | 0,00 | 0,02% | 0,01% |
| R_12 | R12 | 0,05 | 0,01 | 0,01 | 0,01 | 0,10% | 0,04% |
| R_13 | Estación Centro | 0,01 | 0,00 | 0,00 | 0,00 | 0,01% | 0,00% |
| R_14 | Colegio Pedro Vergara Keller | 0,00 | 0,00 | 0,00 | 0,00 | 0,01% | 0,00% |
| R_15 | Club Deportivo 23 de Marzo | 0,00 | 0,00 | 0,00 | 0,00 | 0,01% | 0,00% |

**Tabla 3-43: - Resultados de modelo de dispersión de MP10. Fase de Construcción.****

| Receptor | Descripción | Material Particulado Respirable (MP10) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [μg/m3] ** | **Concentración [μg/m3] ** | **Norma de Calidad** | **Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Percentil 98**<br>**24 horas** | **Período Anual** | **Percentil 98**<br>**24 horas** | **Período Anual** | **Percentil 98**<br>**24 horas** | **Período Anual** |
| R_1 | R01 | 0,01 | 0,00 | 130 | 50 | 0,01% | 0,01% |
| R_2 | R02 | 0,02 | 0,00 | 0,00 | 0,00 | 0,01% | 0,01% |
| R_3 | R03 | 0,02 | 0,00 | 0,00 | 0,00 | 0,02% | 0,01% |
| R_4 | R04 | 0,01 | 0,00 | 0,00 | 0,00 | 0,01% | 0,01% |
| R_5 | R05 | 0,01 | 0,00 | 0,00 | 0,00 | 0,01% | 0,00% |
| R_6 | R06 | 0,02 | 0,01 | 0,01 | 0,01 | 0,02% | 0,02% |
| R_7 | R07 | 0,07 | 0,03 | 0,03 | 0,03 | 0,05% | 0,05% |
| R_8 | R08 | 0,01 | 0,00 | 0,00 | 0,00 | 0,01% | 0,00% |
| R_9 | R09 | 0,02 | 0,00 | 0,00 | 0,00 | 0,01% | 0,01% |
| R_10 | R10 | 0,05 | 0,01 | 0,01 | 0,01 | 0,04% | 0,02% |
| R_11 | R11 | 0,04 | 0,01 | 0,01 | 0,01 | 0,03% | 0,01% |
| R_12 | R12 | 0,15 | 0,02 | 0,02 | 0,02 | 0,11% | 0,04% |
| R_13 | Estación Centro | 0,02 | 0,00 | 0,00 | 0,00 | 0,01% | 0,00% |
| R_14 | Colegio Pedro Vergara Keller | 0,01 | 0,00 | 0,00 | 0,00 | 0,01% | 0,00% |
| R_15 | Club Deportivo 23 de Marzo | 0,01 | 0,00 | 0,00 | 0,00 | 0,01% | 0,00% |

**Tabla 3-44: - Resultados de modelo de dispersión de MPS. Fase de Construcción.****

| Receptor | Descripción | Material Particulado Respirable (MP10) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Tasa de depositación [mg/m2-día]** | **Tasa de depositación [mg/m2-día]** | **Norma de referencia** | **Norma de referencia** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Periodo Mensual** | **Período Anual** | **Periodo Mensual** | **Período Anual** | **Periodo Mensual** | **Período Anual** |
| R_1 | R01 | 0,02 | 0,01 | 150 | 100 | 0,01% | 0,01% |
| R_2 | R02 | 0,04 | 0,02 | 0,02 | 0,02 | 0,03% | 0,02% |
| R_3 | R03 | 0,05 | 0,02 | 0,02 | 0,02 | 0,03% | 0,02% |
| R_4 | R04 | 0,02 | 0,01 | 0,01 | 0,01 | 0,02% | 0,01% |
| R_5 | R05 | 0,02 | 0,01 | 0,01 | 0,01 | 0,01% | 0,01% |
| R_6 | R06 | 0,14 | 0,12 | 0,12 | 0,12 | 0,09% | 0,12% |
| R_7 | R07 | 0,28 | 0,25 | 0,25 | 0,25 | 0,19% | 0,25% |
| R_8 | R08 | 0,01 | 0,01 | 0,01 | 0,01 | 0,01% | 0,01% |
| R_9 | R09 | 0,01 | 0,01 | 0,01 | 0,01 | 0,01% | 0,01% |
| R_10 | R10 | 0,07 | 0,03 | 0,03 | 0,03 | 0,04% | 0,03% |
| R_11 | R11 | 0,05 | 0,03 | 0,03 | 0,03 | 0,03% | 0,03% |
| R_12 | R12 | 0,12 | 0,04 | 0,04 | 0,04 | 0,08% | 0,04% |
| R_13 | Estación Centro | 0,02 | 0,01 | 0,01 | 0,01 | 0,01% | 0,01% |
| R_14 | Colegio Pedro Vergara Keller | 0,01 | 0,01 | 0,01 | 0,01 | 0,01% | 0,01% |
| R_15 | Club Deportivo 23 de Marzo | 0,01 | 0,01 | 0,01 | 0,01 | 0,01% | 0,01% |

**Tabla 3-45: - Resultados de modelo de dispersión de CO. Fase de Construcción.****

| Receptor | Descripción | Monóxido de Carbono (CO) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [mg/m3] ** | **Concentración [mg/m3] ** | **Norma de Calidad** | **Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Percentil 99**<br>**1 hora** | **Percentil 99**<br>**8 horas** | **Percentil 99**<br>**1 hora** | **Percentil 99**<br>**8 horas** | **Percentil 99**<br>**1 hora** | **Percentil 99**<br>**8 horas** |
| R_1 | R01 | 0,00 | 0,00 | 30 | 10 | 0,00% | 0,00% |
| R_2 | R02 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% |
| R_3 | R03 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% |
| R_4 | R04 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% |
| R_5 | R05 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% |
| R_6 | R06 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% |
| R_7 | R07 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% |
| R_8 | R08 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% |
| R_9 | R09 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% |
| R_10 | R10 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% |
| R_11 | R11 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% |
| R_12 | R12 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01% | 0,01% |
| R_13 | Estación Centro | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% |
| R_14 | Colegio Pedro Vergara Keller | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% |
| R_15 | Club Deportivo 23 de Marzo | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% |

**Tabla 3-46: - Resultados de modelo de dispersión de NO** **2** **. Fase de Construcción.****

| Receptor | Descripción | Dióxido de Nitrógeno (NO )<br>2 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Norma de Calidad** | **Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Percentil 99**<br>**1 hora** | **Período Anual** | **Percentil 99**<br>**1 hora** | **Período Anual** | **Percentil 99**<br>** 1 hora** | **Período Anual** |
| R_1 | R01 | 0,11 | 0,00 | 400 | 100 | 0,03% | 0,00% |
| R_2 | R02 | 0,12 | 0,00 | 0,00 | 0,00 | 0,03% | 0,00% |
| R_3 | R03 | 0,13 | 0,00 | 0,00 | 0,00 | 0,03% | 0,00% |
| R_4 | R04 | 0,17 | 0,00 | 0,00 | 0,00 | 0,04% | 0,00% |
| R_5 | R05 | 0,19 | 0,00 | 0,00 | 0,00 | 0,05% | 0,00% |
| R_6 | R06 | 0,30 | 0,00 | 0,00 | 0,00 | 0,07% | 0,00% |
| R_7 | R07 | 0,25 | 0,00 | 0,00 | 0,00 | 0,06% | 0,00% |
| R_8 | R08 | 0,31 | 0,00 | 0,00 | 0,00 | 0,08% | 0,00% |
| R_9 | R09 | 0,68 | 0,00 | 0,00 | 0,00 | 0,17% | 0,00% |
| R_10 | R10 | 2,51 | 0,02 | 0,02 | 0,02 | 0,63% | 0,02% |
| R_11 | R11 | 2,03 | 0,01 | 0,01 | 0,01 | 0,51% | 0,01% |
| R_12 | R12 | 8,48 | 0,08 | 0,08 | 0,08 | 2,12% | 0,08% |
| R_13 | Estación Centro | 0,50 | 0,00 | 0,00 | 0,00 | 0,12% | 0,00% |
| R_14 | Colegio Pedro Vergara Keller | 0,15 | 0,00 | 0,00 | 0,00 | 0,04% | 0,00% |
| R_15 | Club Deportivo 23 de Marzo | 0,36 | 0,00 | 0,00 | 0,00 | 0,09% | 0,00% |

**Tabla 3-47: - Resultados de modelo de dispersión de SO** **2** **. Fase de Construcción.****

| Receptor | Descripción | Dióxido de Azufre (SO )<br>2 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Norma de Calidad** | **Norma de Calidad** | **Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Percentil 99**<br>**1 hora** | **Percentil 99**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 99**<br>** 1 hora** | **Percentil 99**<br>** 24 horas** | **Período**<br>**Anual** | **Percentil 99**<br>** 1 hora** | **Percentil 99**<br>**24 horas** | **Período**<br>**Anual** |
| R_1 | R01 | 0,00 | 0,00 | 0,00 | 350 | 150 | 60 | 0,00% | 0,00% | 0,00% |
| R_2 | R02 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% | 0,00% |
| R_3 | R03 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% | 0,00% |
| R_4 | R04 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% | 0,00% |
| R_5 | R05 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% | 0,00% |
| R_6 | R06 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% | 0,00% |
| R_7 | R07 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% | 0,00% |
| R_8 | R08 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% | 0,00% |
| R_9 | R09 | 0,01 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,01% | 0,00% |
| R_10 | R10 | 0,07 | 0,03 | 0,00 | 0,00 | 0,00 | 0,00 | 0,02% | 0,02% | 0,00% |
| R_11 | R11 | 0,05 | 0,02 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01% | 0,01% | 0,00% |
| R_12 | R12 | 0,51 | 0,12 | 0,01 | 0,01 | 0,01 | 0,01 | 0,15% | 0,08% | 0,02% |
| R_13 | Estación Centro | 0,01 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% | 0,00% |
| R_14 | Colegio Pedro<br>Vergara Keller | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% | 0,00% |
| R_15 | Club Deportivo 23<br>de Marzo | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00% | 0,00% | 0,00% |

**Tabla 3-48: - Concentración total esperada, estación Centro. Fase de Construcción.****

| id | Nombre del Proyecto | Fuente |
| --- | --- | --- |
| P1 | Proyecto Inmobiliario Lotes B y C | https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2151471662 |
| P2 | Delimitación de nuevos recursos,<br>Proyecto Quetena | https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2152572499 |
| P3 | Proyecto Ampliación y Mejoramiento<br>Aeropuerto El Loa de Calama | https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2151727454 |
| P4 | Parque Fotovoltaico Latorre Sunlight | https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2151793001 |
| P5 | Proyecto Extracción de Áridos Pozo<br>E10 (km 100) | https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2145347109 |
| P6 | Ajustes Constructivos a Instalaciones<br>de Relaves Espesados | https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2154669144 |
| P7 | Parque Eólico Vientos del Loa | https://seia.sea.gob.cl/expediente/expedientesEvaluacion.php?modo=ficha&id_expediente=2147975096 |

**Tabla 3-49: - Aporte otros proyectos, Estación Centro.****

| Contaminante | Período | Unidad | Normativa<br>vigente | Aporte de otros proyectos | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Período** | **Unidad** | **Normativa**<br>**vigente** | **P1** | **P2** | **P3** | **P4** | **P5** | **P6** | **P7** | **Total** | **Porcentaje**<br>**de la**<br>**norma** |
| Material<br>Particulado<br>Respirable<br>Fino (MP2,5) | P98 24h | μg/m3 | 50 | 0,001 | 0,004 | 0,007 | 0,000 | 0,000 | 0,092 | 0,000 | 0,104 | 0,21% |
| Material<br>Particulado<br>Respirable<br>Fino (MP2,5) | Anual | μg/m3 | 20 | 0,000 | 0,001 | 0,002 | 0,000 | 0,000 | 0,050 | 0,000 | 0,053 | 0,26% |
| Material<br>Particulado<br>Respirable<br>(MP10) | P98 24h | μg/m3N | 130 | 0,001 | 0,009 | 0,026 | 0,010 | 0,010 | 0,371 | 0,000 | 0,427 | 0,33% |
| Material<br>Particulado<br>Respirable<br>(MP10) | Anual | μg/m3N | 50 | 0,000 | 0,002 | 0,006 | 0,000 | 0,000 | 0,199 | 0,000 | 0,207 | 0,41% |
| Monóxido de<br>Carbono (CO) | P99 máx. 1h | mg/m3N | 30 | n/i | 0,0359 | 0,140 | 0,050 | n/i | 0,667 | 0,000 | 0,893 | 0,00% |
| Monóxido de<br>Carbono (CO) | P99 máx. 8h | mg/m3N | 10 | n/i | 0,0511 | 0,041 | 0,030 | n/i | 0,462 | 0,000 | 0,584 | 0,01% |
| Dióxido de<br>Nitrógeno<br>(NO2) | P99 máx. 1h | μg/m3N | 400 | n/i | 0,1654 | 0,533 | 0,160 | n/i | 1,952 | 2,000 | 4,810 | 1,20% |
| Dióxido de<br>Nitrógeno<br>(NO2) | Anual | μg/m3N | 100 | n/i | 0,0006 | 0,015 | 0,010 | n/i | 0,284 | 2,000 | 2,309 | 2,31% |
| Dióxido de<br>Azufre (SO2) | P99 1h | μg/m3N | 350 | n/i | 0,0064 | 0,000 | 0,000 | n/i | 0,048 | 0,000 | 0,054 | 0,02% |
| Dióxido de<br>Azufre (SO2) | P99 24h | μg/m3N | 150 | n/i | 0,0053 | 0,000 | 0,000 | n/i | 0,013 | 0,000 | 0,018 | 0,01% |
| Dióxido de<br>Azufre (SO2) | Anual | μg/m3N | 60 | n/i | 0,0006 | 0,000 | 0,000 | n/i | 0,007 | 0,000 | 0,007 | 0,01% |

**Tabla 3-50: - Aporte otros proyectos, Estación Club Deportivo 23 de marzo.****

| Contaminante | Período | Unidad | Normativa<br>vigente | Aporte de otros proyectos | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Período** | **Unidad** | **Normativa**<br>**vigente** | **P1** | **P2** | **P3** | **P4** | **P5** | **P6** | **P7** | **Total** | **Porcentaje**<br>**de la**<br>**norma** |
| Material<br>Particulado<br>Respirable<br>Fino (MP2,5) | P98 24h | μg/m3 | 50 | 0,001 | 0,006 | 0,004 | 0,000 | 0,000 | 0,099 | 0,000 | 0,111 | 0,22% |
| Material<br>Particulado<br>Respirable<br>Fino (MP2,5) | Anual | μg/m3 | 20 | 0,000 | 0,001 | 0,001 | 0,000 | 0,000 | 0,056 | 0,000 | 0,058 | 0,29% |
| Material<br>Particulado<br>Respirable<br>(MP10) | P98 24h | μg/m3N | 130 | 0,002 | 0,011 | 0,017 | 0,010 | 0,010 | 0,390 | 0,000 | 0,440 | 0,34% |
| Material<br>Particulado<br>Respirable<br>(MP10) | Anual | μg/m3N | 50 | 0,000 | 0,002 | 0,004 | 0,000 | 0,000 | 0,223 | 0,000 | 0,229 | 0,46% |
| Dióxido de<br>Azufre (SO2) | P99 1h | μg/m3N | 350 | n/i | 0,009 | 0,000 | 0,000 | n/i | 0,049 | 0,000 | 0,058 | 0,02% |
| Dióxido de<br>Azufre (SO2) | P99 24h | μg/m3N | 150 | n/i | 0,006 | 0,000 | 0,000 | n/i | 0,015 | 0,000 | 0,020 | 0,01% |
| Dióxido de<br>Azufre (SO2) | Anual | μg/m3N | 60 | n/i | 0,001 | 0,000 | 0,000 | n/i | 0,007 | 0,000 | 0,008 | 0,01% |

**Tabla 3-51: - Aporte otros proyectos, estación Colegio Pedro Vergara Keller.****

| Contaminante | Período | Unidad | Normativa<br>vigente | Aporte de otros proyectos | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Período** | **Unidad** | **Normativa**<br>**vigente** | **P1** | **P2** | **P3** | **P4** | **P5** | **P6** | **P7** | **Valor** | **Porcentaje**<br>**de la**<br>**norma** |
| Material<br>Particulado<br>Respirable<br>Fino (MP2,5) | P98 24h | μg/m3 | 50 | 0,006 | 0,015 | 0,002 | 0,000 | 0,000 | 0,155 | 0,000 | 0,178 | 0,36% |
| Material<br>Particulado<br>Respirable<br>Fino (MP2,5) | Anual | μg/m3 | 20 | 0,001 | 0,002 | 0,000 | 0,000 | 0,000 | 0,090 | 0,000 | 0,094 | 0,47% |
| Material<br>Particulado<br>Respirable<br>(MP10) | P98 24h | μg/m3N | 130 | 0,011 | 0,032 | 0,007 | 0,010 | 0,000 | 0,633 | 0,000 | 0,693 | 0,53% |
| Material<br>Particulado<br>Respirable<br>(MP10) | Anual | μg/m3N | 50 | 0,002 | 0,008 | 0,001 | 0,000 | 0,000 | 0,369 | 0,000 | 0,380 | 0,76% |

**Tabla 3-52: - Concentración total esperada, estación Centro. Fase de Construcción.****

| Contaminante | Período | Unidad | Normativa<br>vigente | Línea de Base Proyectada | Col6 | Col7 | Col8 | Aporte del proyecto | Col10 | Concentración Total | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Período** | **Unidad** | **Normativa**<br>**vigente** | **Valor**<br>**Medido** | **Aporte**<br>**otros**<br>**proyectos** | **Total** | **Porcentaje**<br>**de la**<br>**norma** | **Valor** | **Porcentaje**<br>**de la**<br>**norma** | **Valor** | **Porcentaje**<br>**de la**<br>**norma** |
| Material<br>Particulado<br>Respirable<br>Fino (MP2,5) | P98 24h | μg/m3 | 50 | 13,00 | 0,10 | 13,10 | 26,2% | 0,01 | 0,01% | 13,11 | 26,22% |
| Material<br>Particulado<br>Respirable<br>Fino (MP2,5) | Anual | μg/m3 | 20 | 5,00 | 0,05 | 5,05 | 25,3% | 0,00 | 0,00% | 5,05 | 25,27% |
| Material<br>Particulado<br>Respirable<br>(MP10) | P98 24h | μg/m3N | 130 | 26,34 | 0,43 | 26,76 | 20,6% | 0,02 | 0,01% | 26,78 | 20,60% |
| Material<br>Particulado<br>Respirable<br>(MP10) | Anual | μg/m3N | 50 | 25,70 | 0,21 | 25,91 | 51,8% | 0,00 | 0,00% | 25,91 | 51,82% |
| Monóxido de<br>Carbono (CO) | P99 máx. 1h | mg/m3N | 30 | 1,50 | 0,00 | 1,50 | 5,0% | 0,00 | 0,00% | 1,50 | 5,00% |
| Monóxido de<br>Carbono (CO) | P99 máx. 8h | mg/m3N | 10 | 0,80 | 0,00 | 0,80 | 8,0% | 0,00 | 0,00% | 0,80 | 8,01% |
| Dióxido de<br>Nitrógeno<br>(NO2) | P99 máx. 1h | μg/m3N | 400 | 86,90 | 4,81 | 91,71 | 22,9% | 0,50 | 0,12% | 92,21 | 23,05% |
| Dióxido de<br>Nitrógeno<br>(NO2) | Anual | μg/m3N | 100 | 17,50 | 2,31 | 19,81 | 19,8% | 0,00 | 0,00% | 19,81 | 19,81% |
| Dióxido de<br>Azufre (SO2) | P99 1h | μg/m3N | 350 | 11,40 | 0,05 | 11,45 | 3,3% | 0,01 | 0,00% | 11,46 | 3,28% |
| Dióxido de<br>Azufre (SO2) | P99 24h | μg/m3N | 150 | 5,80 | 0,02 | 5,82 | 3,9% | 0,01 | 0,00% | 5,82 | 3,88% |
| Dióxido de<br>Azufre (SO2) | Anual | μg/m3N | 60 | 2,50 | 0,01 | 2,51 | 4,2% | 0,00 | 0,00% | 2,51 | 4,18% |

**Tabla 3-53: - Concentración total esperada, estación Club Deportivo 23 de marzo. Fase de Construcción.****

| Contaminante | Período | Unidad | Normativa<br>vigente | Línea de Base | Col6 | Col7 | Col8 | Aporte del proyecto | Col10 | Concentración Total | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Período** | **Unidad** | **Normativa**<br>**vigente** | **Valor** | **Aporte**<br>**otros**<br>**proyectos** | **Total** | **Porcentaje**<br>**de la**<br>**norma** | **Valor** | **Porcentaje**<br>**de la**<br>**norma** | **Valor** | **Porcentaje**<br>**de la**<br>**norma** |
| Material<br>Particulado<br>Respirable<br>Fino (MP2,5) | P98 24h | μg/m3 | 50 | 11,00 | 0,11 | 11,11 | 22,00% | 0,00 | 0,01% | 11,12 | 22,23% |
| Material<br>Particulado<br>Respirable<br>Fino (MP2,5) | Anual | μg/m3 | 20 | 7,00 | 0,06 | 7,06 | 35,00% | 0,00 | 0,00% | 7,06 | 35,29% |
| Material<br>Particulado<br>Respirable<br>(MP10) | P98 24h | μg/m3N | 130 | 68,00 | 0,44 | 68,44 | 52,31% | 0,01 | 0,01% | 68,45 | 52,66% |
| Material<br>Particulado<br>Respirable<br>(MP10) | Anual | μg/m3N | 50 | 42,80 | 0,23 | 43,03 | 85,60% | 0,00 | 0,00% | 43,03 | 86,06% |
| Dióxido de<br>Azufre (SO2) | P99 1h | μg/m3N | 350 | 15,00 | 0,06 | 15,06 | 4,29% | 0,01 | 0,00% | 15,06 | 4,30% |
| Dióxido de<br>Azufre (SO2) | P99 24h | μg/m3N | 150 | 7,50 | 0,02 | 7,52 | 5,00% | 0,00 | 0,00% | 7,52 | 5,02% |
| Dióxido de<br>Azufre (SO2) | Anual | μg/m3N | 60 | 2,30 | 0,01 | 2,31 | 3,83% | 0,00 | 0,00% | 2,31 | 3,85% |

**Tabla 3-54: - Concentración total esperada, estación Colegio Pedro Vergara Keller. Fase de Construcción.****

| Contaminante | Período | Unidad | Normativa<br>vigente | Línea de Base | Col6 | Col7 | Col8 | Aporte del proyecto | Col10 | Concentración Total | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Período** | **Unidad** | **Normativa**<br>**vigente** | **Valor** | **Aporte**<br>**otros**<br>**proyectos** | **Total** | **Porcentaje**<br>**de la**<br>**norma** | **Valor** | **Porcentaje**<br>**de la**<br>**norma** | **Valor** | **Porcentaje**<br>**de la**<br>**norma** |
| Material<br>Particulado<br>Respirable<br>Fino (MP2,5) | P98 24h | μg/m3 | 50 | 15 | 0,18 | 15,18 | 30,00% | 0,00 | 0,01% | 15,18 | 30,36% |
| Material<br>Particulado<br>Respirable<br>Fino (MP2,5) | Anual | μg/m3 | 20 | 9,6 | 0,09 | 9,69 | 48,00% | 0,00 | 0,00% | 9,69 | 48,47% |
| Material<br>Particulado<br>Respirable<br>(MP10) | P98 24h | μg/m3N | 130 | 83 | 0,69 | 83,69 | 63,85% | 0,01 | 0,01% | 83,70 | 64,39% |
| Material<br>Particulado<br>Respirable<br>(MP10) | Anual | μg/m3N | 50 | 46,7 | 0,38 | 47,08 | 93,40% | 0,00 | 0,00% | 47,08 | 94,16% |

**Tabla 5-1.: Archivos de modelación entregados.****

| Archivos | Entregado | Observación |
| --- | --- | --- |
| **Archivos CALPUFF:** | **Archivos CALPUFF:** | **Archivos CALPUFF:** |
| - CALPUFF.DAT | NO | Corresponde al archivo CONC.DAT |
| - CALPUFF.LST | SI | - |
| - CALPUFF.INP | SI | - |
| - CONC.DAT | SI | - |
| - DFLX.DAT | SI | - |
| - WFLX.DAT | SI | - |
| **Archivos Meteorológicos:** | **Archivos Meteorológicos:** | **Archivos Meteorológicos:** |
| - CALMET.DAT | SI | Corresponde al archivo: calmetv6_Parina.dat |
| - GEO.DAT | SI | - |
| - SURF.DAT | NO | No fueron utilizados debido a que se usó, directamente en<br>CALPUFF, la meteorología proveniente del modelo<br>meteorológico WRF. |
| - UP.DAT | NO | NO |
| - CALMET.LST | NO | NO |
| - CALMET.INP | NO | NO |
| namelist.wps | SI | Archivo de configuración de preproceso de WRF (WPS) |
| namelist.input | SI | Archivo de configuración de WRF |
| **Archivos CALPOST:** | **Archivos CALPOST:** | **Archivos CALPOST:** |
| - CALPOST.DAT | SI | Los archivos se presentan en forma separada según<br>contaminantes y periodo. |
| - CALPOST.LST | SI | SI |
| - CALPOST.INP | SI | SI |
| **Archivos Complementarios:** | **Archivos Complementarios:** | **Archivos Complementarios:** |
| - Coastline Data File, Dry Flux Data File, Wet Flux<br>Data File, Ozone Data File, Chem Data File. | NO | No se incluyen, debido a que corresponden a datos que<br>no fueron modelados. |
