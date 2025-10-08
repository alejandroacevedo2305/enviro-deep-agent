---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: report
pages: 151
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Declaración de Impacto Ambiental Proyecto “Parque Solar Fotovoltaico Acuyo”
  - Proyecto “Parque Solar Fotovoltaico Acuyo”
-->

2024

# Declaración de Impacto Ambiental Proyecto “Parque Solar Fotovoltaico Acuyo”

## Anexo 2.1.B. Modelación de Dispersión de Contaminantes Atmosféricos

##### Región de Valparaíso, Chile

Desarrollado por:

### Modelación de Dispersión de Contaminantes Atmosféricos

# Proyecto “Parque Solar Fotovoltaico Acuyo”

#### Diciembre 2023

**PREPARADO PARA**

AMBEC S.A.

|REVISIONES|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|No REV.|ELABORADO POR|REVISADO POR|FECHA|FIRMA RESPONSABLE|
|Rev.0|Ernesto Sáez|María José Meneses|12-12-2023||
|Rev.0|Ingeniero Civil Químico<br>(UTFSM)|Ingeniero Civil de<br>Industrias con Mención<br>en Ing. Química (PUC)|Ingeniero Civil de<br>Industrias con Mención<br>en Ing. Química (PUC)|Ingeniero Civil de<br>Industrias con Mención<br>en Ing. Química (PUC)|
|Rev.0|Ingeniero Civil Químico<br>(UTFSM)|Ingeniero Civil de<br>Industrias con Mención<br>en Ing. Química (PUC)|Ingeniero Civil de<br>Industrias con Mención<br>en Ing. Química (PUC)|María José Meneses|

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

ÍNDICE

**1** **INTRODUCCIÓN ................................................................................................................. 1**

**2** **OBJETIVOS ........................................................................................................................ 4**

2.1 Objetivo General ......................................................................................................................... 4

2.2 Objetivos Específicos .................................................................................................................. 4

**3** **METODOLOGÍA ................................................................................................................. 5**

**4** **RESUMEN DE LA ESTIMACIÓN DE EMISIONES ATMOSFÉRICAS ............................................ 7**

**5** **MODELO DE CALIDAD DEL AIRE .......................................................................................... 8**

5.1 Tipo de Modelo de Calidad del Aire Seleccionado ..................................................................... 8

5.2 Descripción del Modelo de Calidad del Aire Seleccionado - CALPUFF ....................................... 8

5.3 Características del Modelo de Dispersión de Contaminantes .................................................. 10

5.3.1 Dominio de la Modelación .................................................................................................. 10

5.3.2 Topografía del Sector .......................................................................................................... 11

5.3.3 Uso de Suelos ...................................................................................................................... 12

5.4 Descripción del Modelo Meteorológico Seleccionado - WRF .................................................. 13

5.4.1.1 Selección año de modelación ........................................................................................ 15

5.5 Caracterización de Clima en el Área del Proyecto .................................................................... 16

5.5.1 Evolución del Clima producto del Cambio Climático en el Área del Proyecto .................... 22

5.6 Caracterización Meteorológica del Área del Proyecto ............................................................. 28

5.6.1 Meteorología de Superficie - Valores Observados ............................................................. 28

5.6.1.1 Estación Casablanca ...................................................................................................... 31

5.6.2 Meteorología de Superficie - Valores Modelados .............................................................. 57

5.6.2.1 Estación Meteorológica Casablanca .............................................................................. 57

5.6.3 Meteorología de Altura - Valores Observados ................................................................... 69

5.6.4 Meteorología de Altura - Valores Modelados .................................................................... 69

5.6.4.1 Estación Meteorológica Casablanca .............................................................................. 69

5.7 Análisis de Incertidumbre ......................................................................................................... 73

www.dfmconsultores.cl

i
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.7.1 Estación Casablanca ............................................................................................................ 74

5.7.1.1 Comparación Cuantitativa ............................................................................................. 74

5.7.1.2 Comparación Cualitativa ............................................................................................... 75

5.7.1.3 Velocidad y Dirección del Viento ................................................................................... 75

5.7.1.4 Temperatura .................................................................................................................. 80

5.8 Normas de Calidad del Aire ...................................................................................................... 84

5.9 Línea Base de Calidad del Aire .................................................................................................. 85

5.9.1 Estaciones de monitoreo .................................................................................................... 85

5.9.1.1 Estación Casablanca ...................................................................................................... 88

5.9.2 Resumen Línea de Base de Calidad de Aire ........................................................................ 92

5.10 Escenario de Modelación ....................................................................................................... 93

5.10.1 Fuentes Emisoras .............................................................................................................. 93

5.10.2 Receptores de Interés ..................................................................................................... 100

5.11 Resultados de la Modelación ................................................................................................ 104

5.11.1 Material Particulado Fino Respirable (MP2.5) ................................................................ 105

5.11.2 Material Particulado Respirable (MP10) ......................................................................... 109

5.11.3 Material Particulado Sedimentable (MPS) ...................................................................... 113

5.11.4 Monóxido de Carbono (CO) ............................................................................................ 116

5.11.5 Dióxido de Nitrógeno (NO 2 ) ............................................................................................ 118

5.11.6 Dióxido de Azufre (SO 2 ). Normas primarias .................................................................... 122

5.11.7 Dióxido de Azufre (SO 2 ). Normas secundarias. ............................................................... 127

5.12 Concentración total esperada .............................................................................................. 131

5.13 Área de Influencia ................................................................................................................. 132

**6** **CONCLUSIONES ............................................................................................................. 136**

6.1 Modelación de Dispersión de Contaminantes........................................................................ 136

6.2 Concentración total esperada ................................................................................................ 137

**7** **ANEXO 1: ARCHIVOS DIGITALES MODELACIÓN ............................................................... 138**

www.dfmconsultores.cl

ii
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

ÍNDICE TABLAS

Tabla 4-1. Resumen de emisiones. Año 1 de la Fase de Construcción del Proyecto. ......................... 7

Tabla 5-1. Configuración parámetros principales WRF. .................................................................... 14

Tabla 5-2. Concentración media anual de MP10 en años 2020 - 2022, estación de monitoreo

Casablanca. ........................................................................................................................................ 15

Tabla 5-3. Principales índices evaluación cambio climático. Región de Valparaíso, provincia de

Valparaíso, comuna Casablanca. ....................................................................................................... 22

Tabla 5-4. Coordenadas de Ubicación, Estación de Monitoreo Casablanca. .................................... 28

Tabla 5-5. Equipos y principios de operación registro de variables meteorológicas. ....................... 29

Tabla 5-6. Resumen de información Velocidad del Viento. Estación Casablanca............................. 31

Tabla 5-7. Frecuencia de distribución Velocidad y Dirección del Viento. Enero 2020 a diciembre de

2022. Estación Casablanca. ............................................................................................................... 34

Tabla 5-8. Resumen de información Temperatura Observada. Estación Casablanca. ..................... 39

Tabla 5-9. Resumen de información Humedad Relativa Observada. Estación Casablanca. ............. 43

Tabla 5-10. Resumen de información Precipitación acumulada Observada. Estación Casablanca. . 47

Tabla 5-11. Resumen de información Presión atmosférica Observada. Estación Casablanca. ........ 50

Tabla 5-12. Resumen de información Radiación solar Observada. Estación Casablanca. ................ 53

Tabla 5-13. Resumen de información Velocidad del Viento Modelado. Estación Casablanca. ........ 57

Tabla 5-14. Frecuencia de distribución Velocidad y Dirección del Viento Modelada. Enero a

diciembre de 2020. Estación Casablanca. ......................................................................................... 60

Tabla 5-15. Resumen de información Temperatura Modelada. Estación Casablanca. .................... 65

Tabla 5-16. Resumen de Información Altura de Capa de Mezcla Modelada. Estación Casablanca. 69

Tabla 5-17. Métricas estadísticas recomendables en el Análisis de Incertidumbre para las variables

meteorológicas medias. .................................................................................................................... 73

Tabla 5-18. Estadígrafos de Dispersión para Velocidad del Viento y Temperatura. Estación

Casablanca. ........................................................................................................................................ 74

Tabla 5-19. Normas primarias de calidad del aire. ............................................................................ 84

Tabla 5-20. Normas secundarias de calidad del aire. ........................................................................ 84

Tabla 5-21. Inventario de Equipos y Técnicas de Medición. ............................................................. 85

Tabla 5-22. Caracterización de Estación de Monitoreo de Calidad del Aire. .................................... 86

Tabla 5-23. Resultados Monitoreo de MP10. Estación Casablanca [()] . .............................................. 88

www.dfmconsultores.cl

iii
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Tabla 5-24. Comparación de Monitoreo de MP10 con Normativa. Estación Casablanca. ............... 88

Tabla 5-25. Resultados Monitoreo de CO. Estación Casablanca [()] . ................................................... 89

Tabla 5-26. Comparación de Monitoreo de CO con Normativa. Estación Casablanca. .................... 89

Tabla 5-27. Resultados Monitoreo de NO 2 . Estación Casablanca. .................................................... 90

Tabla 5-28. Comparación de Monitoreo de NO 2 con Normativa. Estación Casablanca. .................. 90

Tabla 5-29. Resultados Monitoreo de SO 2 . Estación Casablanca [()] . .................................................. 91

Tabla 5-30. Comparación de Monitoreo de SO 2 con Normativa. Estación Casablanca. ................... 91

Tabla 5-31. Resumen Línea de Base de Calidad del Aire. .................................................................. 92

Tabla 5-32. Características Fuentes Emisoras de contaminantes atmosféricos. .............................. 97

Tabla 5-33. Características Fuentes Emisoras Puntuales. ................................................................ 99

Tabla 5-34. Receptores de Interés. ................................................................................................. 100

Tabla 5-35. Resultados de modelo de dispersión de MP2.5. .......................................................... 105

Tabla 5-36. Resultados de modelo de dispersión de MP10. ........................................................... 109

Tabla 5-37. Resultados de modelo de dispersión de MPS. ............................................................. 113

Tabla 5-38. Resultados de modelo de dispersión de CO. ................................................................ 116

Tabla 5-39. Resultados de modelo de dispersión de NO 2 . .............................................................. 118

Tabla 5-40. Resultados de modelo de dispersión de SO 2 . Normas primarias de calidad del aire. . 122

Tabla 5-41. Resultados de modelo de dispersión de SO 2 . Normas secundarias de calidad del aire.

......................................................................................................................................................... 127

Tabla 5-42. Concentración total esperada. Estación Casablanca.................................................... 131

Tabla 5-43. Criterios recomendados de incremento significativo en la concentración de

contaminantes atmosféricos en zonas saturadas. .......................................................................... 133

Tabla 7-1. Archivos de modelación entregados. ............................................................................. 138

www.dfmconsultores.cl

iv
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

ÍNDICE FIGURAS

Figura 3-1. Diagrama Metodología de Trabajo. .................................................................................. 6

Figura 5-1. Dominio de Modelación. ................................................................................................. 10

Figura 5-2. Topografía del Dominio de Modelación. ........................................................................ 11

Figura 5-3. Uso de Suelos del Dominio de Modelación. ................................................................... 12

Figura 5-4. Campo de Isotermas. Región de Valparaíso. .................................................................. 17

Figura 5-5. Campo de Isoyetas. Región de Valparaíso. ..................................................................... 18

Figura 5-6. Climograma de la Región de Valparaíso.......................................................................... 19

Figura 5-7. Clasificación climática según Köppen. Región de Valparaíso. ......................................... 21

Figura 5-8. Comparación Temperatura Media Anual entre situación actual y futura. Región de

Valparaíso. ......................................................................................................................................... 24

Figura 5-9. Comparación Precipitación Acumulada Anual entre situación actual y futura. Región de

Valparaíso. ......................................................................................................................................... 25

Figura 5-10. Comparación Velocidad Media Anual Viento entre situación actual y futura. Región de

Valparaíso. ......................................................................................................................................... 26

Figura 5-11. Evolución Velocidad Media Anual Viento. Región de Valparaíso. ................................ 27

Figura 5-12. Ubicación Referencial Estación de Monitoreo Meteorológico. .................................... 30

Figura 5-13. Serie de Tiempo Velocidad del Viento Observado. Enero 2020 a diciembre de 2022.

Estación Casablanca. ......................................................................................................................... 32

Figura 5-14. Serie de Tiempo Dirección del Viento Observado. Enero 2020 a diciembre de 2022.

Estación Casablanca. ......................................................................................................................... 33

Figura 5-15. Ciclo Diario Velocidad del Viento Observado. Enero 2020 a diciembre de 2022. Estación

Casablanca. ........................................................................................................................................ 35

Figura 5-16. Ciclo Diario Dirección del Viento Observado. Enero 2020 a diciembre de 2022. Estación

Casablanca. ........................................................................................................................................ 36

Figura 5-17. Ciclo Estacional de Velocidad y Dirección del Viento Observado. Enero 2020 a Diciembre

2022. Estación Casablanca. ............................................................................................................... 38

Figura 5-18. Serie de Tiempo Temperatura Observada. Enero 2020 a diciembre de 2022. Estación

Casablanca. ........................................................................................................................................ 40

Figura 5-19. Ciclo Diario Temperatura Observada. Enero 2020 a diciembre de 2022. Estación

Casablanca. ........................................................................................................................................ 41

www.dfmconsultores.cl

**info@dfmconsultores.cl** v

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Figura 5-20. Ciclo Estacional Temperatura Observada. Enero 2020 a diciembre de 2022. Estación

Casablanca. ........................................................................................................................................ 42

Figura 5-21. Serie de Tiempo Humedad Relativa Observada. Enero 2020 a diciembre de 2022.

Estación Casablanca. ......................................................................................................................... 44

Figura 5-22. Ciclo Diario Humedad Relativa Observada. Enero 2020 a diciembre de 2022. Estación

Casablanca. ........................................................................................................................................ 45

Figura 5-23. Ciclo Estacional Humedad Relativa Observada. Enero 2020 a diciembre de 2022.

Estación Casablanca. ......................................................................................................................... 46

Figura 5-24. Serie de Tiempo Precipitación Diaria Acumulada. Enero 2020 a diciembre de 2022.

Estación Casablanca. ......................................................................................................................... 48

Figura 5-25. Serie de Tiempo Precipitación Mensual Acumulada. Enero 2020 a diciembre de 2022.

Estación Casablanca. ......................................................................................................................... 49

Figura 5-26. Serie de Tiempo Presión atmosférica Observada. Enero 2020 a diciembre de 2022.

Estación Casablanca. ......................................................................................................................... 51

Figura 5-27. Ciclo Anual Presión atmosférica Observada. Enero 2020 a diciembre de 2022. Estación

Casablanca. ........................................................................................................................................ 52

Figura 5-28. Serie de Tiempo Radiación Solar Observada. Enero 2020 a diciembre de 2022. Estación

Casablanca. ........................................................................................................................................ 54

Figura 5-29. Ciclo Diario Radiación Solar Observada. Enero 2020 a diciembre de 2022. Estación

Casablanca. ........................................................................................................................................ 55

Figura 5-30. Ciclo Estacional Radiación Solar Observada. Enero 2020 a diciembre de 2022. Estación

Casablanca. ........................................................................................................................................ 56

Figura 5-31. Serie de Tiempo Velocidad del Viento Modelada. Enero a diciembre de 2020. Estación

Casablanca. ........................................................................................................................................ 58

Figura 5-32. Serie de Tiempo Dirección del Viento Modelada. Enero a diciembre de 2020. Estación

Casablanca. ........................................................................................................................................ 59

Figura 5-33. Ciclo Diario Velocidad del Viento Modelada. Enero a diciembre de 2020. Estación

Casablanca. ........................................................................................................................................ 61

Figura 5-34. Ciclo Diario Dirección del Viento Modelada. Enero a diciembre de 2020. Estación

Casablanca. ........................................................................................................................................ 62

Figura 5-35. Ciclo Estacional de Velocidad y Dirección del Viento Modelado. Año 2020. Estación

Casablanca. ........................................................................................................................................ 64

www.dfmconsultores.cl

vi
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Figura 5-36. Serie de Tiempo Temperatura Modelada. Enero a diciembre de 2020. Estación

Casablanca. ........................................................................................................................................ 66

Figura 5-37. Ciclo Diario Temperatura Modelada. Enero a diciembre de 2020. Estación Casablanca.

........................................................................................................................................................... 67

Figura 5-38. Ciclo Estacional Temperatura Modelada. Enero a diciembre de 2020. Estación

Casablanca. ........................................................................................................................................ 68

Figura 5-39. Serie de tiempo para Altura de Capa de Mezcla Modelada. Enero a diciembre de 2020.

Estación Casablanca. ......................................................................................................................... 70

Figura 5-40. Ciclo Diario Altura de Capa de Mezcla Modelada. Enero a diciembre de 2020. Estación

Casablanca. ........................................................................................................................................ 71

Figura 5-41. Ciclo Estacional Altura Capa de Mezcla Modelada. Enero a diciembre de 2020. Estación

Casablanca. ........................................................................................................................................ 72

Figura 5-42. Comparación del Ciclo Diario de la Velocidad del Viento. Estación Casablanca. ......... 76

Figura 5-43. Comparación de Histogramas de Dirección. Estación Casablanca. .............................. 77

Figura 5-44. Comparación de Ciclo Estacional de Velocidad y Dirección del Viento. Estación

Casablanca. ........................................................................................................................................ 79

Figura 5-45. Comparación del Ciclo Diario de la Temperatura. Estación Casablanca. ...................... 81

Figura 5-46. Comparación del Ciclo Estacional de Temperatura. Estación Casablanca. ................... 83

Figura 5-47. Ubicación Referencial Estación de Monitoreo de Calidad del Aire............................... 87

Figura 5-48. Ubicación Fuentes Emisoras de área y puntuales. ........................................................ 94

Figura 5-49. Ubicación Fuentes Emisoras de camino. ....................................................................... 95

Figura 5-50. Ubicación Fuentes Emisoras lineales-areales. .............................................................. 96

Figura 5-51. Ubicación de Receptores de Interés. .......................................................................... 101

Figura 5-52. Ubicación de Grilla de Receptores. ............................................................................ 103

Figura 5-53. Curva de Isoconcentración para Percentil 98 período 24 horas MP2.5 (μg/m [3] ). ....... 107

Figura 5-54. Curva de Isoconcentración para período anual MP2.5 (μg/m [3] ). ................................ 108

Figura 5-55. Curva de Isoconcentración para Percentil 98 período 24 horas MP10 (μg/m [3] ). ........ 111

Figura 5-56. Curva de Isoconcentración para período anual MP10 (μg/m [3] ). ................................. 112

Figura 5-57. Curva de Isodepositación para periodo Mensual de MPS (mg/m [2] -día). ..................... 114

Figura 5-58. Curva de Isodepositación para periodo Anual de MPS (mg/m [2] -día). ......................... 115

Figura 5-59. Curva de Isoconcentración para Percentil 99 periodo 1 hora NO 2 (μg/m [3] ). ............... 120

www.dfmconsultores.cl

vii
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Figura 5-60. Curva de Isoconcentración para periodo anual NO 2 (μg/m [3] ). .................................... 121

Figura 5-61. Curva de Isoconcentración para Percentil 99 período 1 hora SO 2 (μg/m [3] ). Norma

primaria de calidad del aire. ............................................................................................................ 124

Figura 5-62. Curva de Isoconcentración para Percentil 99 período 24 horas SO 2 (μg/m [3] ). Norma

primaria de calidad del aire. ............................................................................................................ 125

Figura 5-63. Curva de Isoconcentración para periodo Anual SO 2 (μg/m [3] ). Norma primaria de calidad

del aire. ............................................................................................................................................ 126

Figura 5-64. Curva de Isoconcentración para Percentil 99,73 período 1 hora SO 2 (μg/m [3] ). Norma

secundaria de calidad del aire. ........................................................................................................ 128

Figura 5-65. Curva de Isoconcentración para Percentil 99,7 período 24 horas SO 2 (μg/m [3] ). Norma

secundaria de calidad del aire. ........................................................................................................ 129

Figura 5-66. Curva de Isoconcentración para periodo Anual SO 2 (μg/m [3] ). Norma secundaria de

calidad del aire. ............................................................................................................................... 130

Figura 5-67. Área de Influencia Proyecto para Normas Primarias de Calidad de Aire. ................... 134

Figura 5-68. Área de Influencia Proyecto para Normas Secundarias de Calidad de Aire. .............. 135

www.dfmconsultores.cl

viii
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

##### 1 INTRODUCCIÓN

El presente informe contiene la modelación de dispersión de contaminantes del Proyecto “Parque

Solar Fotovoltaico Acuyo”, en adelante denominado también como “el Proyecto”.

El Proyecto consiste en la construcción y operación de un Parque Fotovoltaico (PFV), para la

captación de energía solar y generación de energía eléctrica, enmarcado dentro de las ERNC. El

Proyecto se ubicará en la localidad de Casablanca, comuna de Casablanca, Región de Valparaíso.

El desarrollo de este considera la producción de energía limpia, para lo cual, se construirá un Parque

Solar Fotovoltaico de 81,81 MW (ac) de potencia. La energía generada será transmitida mediante

una Línea Eléctrica de Alta Tensión (en adelante LAT) de 66 kV. La obra principal del Proyecto

corresponde a la implementación de módulos o paneles fotovoltaicos (en adelante “Módulos” o

“Paneles”).

Los Módulos están compuestos de una serie de celdas fotoeléctricas, que es el elemento base del

proceso de transformación de la radiación solar en energía eléctrica. Los Paneles estarán montados

sobre estructuras metálicas de soporte con seguimiento solar en un eje. Los Módulos serán

conectados a los Centros de Transformación (elementos prefabricados en container), que preparan

la energía para ser transmitida. Desde uno de los catorce Centros de Transformación se conectará

el Parque a su LAT de 66 kV.

Durante la fase de construcción se requerirá de dos instalaciones de faenas de uso temporal, las

cuales proveerá los servicios necesarios a los trabajadores que construyan el Proyecto. Contará,

además, con los espacios e instalaciones necesarias para almacenar los insumos y materiales de

construcción requeridos para el PFV y la LAT. Las instalaciones temporales serán desmanteladas una

vez concluida la construcción de las obras.

A partir de los resultados de la estimación de emisiones de contaminantes atmosféricos para cada

situación o caso mencionado anteriormente, los cuales se presentaron en el Anexo 2-1: “Estimación

de Emisiones” de la presente DIA, y con el objetivo de estimar el aporte del proyecto en la

concentración de contaminantes atmosféricos sobre la zona de emplazamiento, se presenta un

modelo de calidad del aire CALPUFF siguiendo los lineamientos de la “Guía para el Uso de Modelos

de Calidad del Aire en el SEIA (2023)”.

En primer lugar, se describe el tipo de modelo de calidad del aire seleccionado y su justificación para

la aplicación en este estudio. Luego se presentan las características del modelo de dispersión de

contaminantes; dominio de modelación, topografía del sector y uso de suelos. Posteriormente, se

presenta una caracterización meteorológica del área del proyecto donde se muestran datos de

meteorología de superficie observada en la estación de monitoreo Casablanca, la cual es de

propiedad de TRESMONTES S.A. Esta caracterización será citada desde el “Anexo 03.2 Modelación

www.dfmconsultores.cl

1
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [1]

“Ampliación Línea Snacks” de TRESMONTES S.A.

A su vez, se presentan datos de meteorología de superficie y altura modelada con el modelo

meteorológico WRF para los mismos puntos, los cuales, posteriormente, son utilizados como datos

de entrada para el modelo de dispersión de contaminantes CALPUFF.

Con el objetivo de validar la capacidad del modelo meteorológico WRF (Weather Research and

Forecasting) de representar la meteorología local, se presenta un análisis de incertidumbre en el

cual se comparan, en forma cualitativa, datos observados y modelados a nivel de ciclo diario y anual,

y en forma cuantitativa con el cálculo de estadígrafos útiles para determinar la capacidad del modelo

de representar datos observados.

Para establecer un punto de comparación de los resultados del modelo de calidad del aire, se

presentan las normas de calidad del aire aplicables al proyecto. Luego, se presentan los escenarios

de modelación anteriormente mencionados. Se describen y presentan las fuentes de emisión junto

con la caracterización de estas; tipo de fuente, dimensión característica y tasas de emisión.

Con el fin de evaluar el aporte del proyecto en la concentración de contaminantes atmosféricos en

la zona, establece una grilla de modelación y un total de 21 receptores discretos ubicados en las

cercanías del proyecto, sobre los cuales se evalúa el aporte del proyecto. Estos receptores

consideran: la estación de monitoreo Casablanca, receptores de medio humano y receptores de

fauna, descritos como puntos de medición para caracterizar fauna.

Se presentan los resultados cualitativos y cuantitativos de la modelación de dispersión de los

siguientes contaminantes atmosféricos: material particulado fino respirable (MP2.5), material

particulado respirable (MP10), material particulado sedimentable (MPS), monóxido de carbono

(CO), dióxido de nitrógeno (NO 2 ) y dióxido de azufre (SO 2 ). Lo anterior se realiza para cada

contaminante en forma cuantitativa a través de tablas, donde se compara el aporte del proyecto

sobre cada receptor y su respectiva comparación con la norma de calidad del aire aplicable y en

forma cualitativa con la presentación de curvas de isoconcentración, las que permiten visualizar a

modo global la dispersión de contaminantes dentro del dominio de modelación considerando

también a los receptores discretos seleccionados. Luego, se presenta la concentración total (línea

de base y aportes del proyecto) en la estación de calidad del aire Casablanca, propiedad de

TRESMONTES S.A. cuya información fue recuperada del Anexo 03.2 Modelación de emisiones

1 Anexo 03.2 Modelación de emisiones atmosféricas recuperado desde el expediente electrónico de la
pertinencia de ingreso al SEIA, e-Pertinencia (2023). Enlace:
[https://pertinencia.sea.gob.cl/api/public/expediente/PERTI-2023-11516](https://pertinencia.sea.gob.cl/api/public/expediente/PERTI-2023-11516)

www.dfmconsultores.cl

2
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)] “Ampliación Línea

Snacks” de TRESMONTES S.A., comparándola con la norma de referencia de calidad del aire.

Finalmente, se presentan las principales conclusiones del estudio.

www.dfmconsultores.cl

3
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

##### 2 OBJETIVOS

###### 2.1 Objetivo General

Evaluar el efecto que tendrán las emisiones atmosféricas asociadas a la ejecución del Proyecto sobre

la calidad del aire en los receptores de interés para así cumplir con los requerimientos indicados en

la Ley N° 19.300 de Bases Generales de Medio Ambiente, sus modificaciones a través de la Ley N°

20.417 y el Reglamento del SEIA D.S. N° 40/2013 en relación con los requisitos mínimos y criterios

para realizar una Declaración de Impacto Ambiental (DIA) de Ingreso al Sistema de Evaluación de

Impacto Ambiental (SEIA).

###### 2.2 Objetivos Específicos

Los objetivos específicos del presente informe se listan a continuación:

 Definir un dominio de modelación coherente con la magnitud del Proyecto y la capacidad

potencial que tengan los contaminantes a dispersar en la atmósfera, asimismo incluyendo

a los receptores discretos de interés.

 Presentar la caracterización de clima, meteorología y calidad del aire de la zona de

emplazamiento del Proyecto a partir de los datos registrados en la estación de monitoreo

Casablanca, para el periodo comprendido entre enero 2020 y diciembre 2022.

 Presentar la caracterización de meteorología de la zona de emplazamiento del Proyecto a

partir del modelo meteorológico WRF, y utilizar este último como dato de entrada en la

modelación de dispersión de contaminantes en el software CALPUFF.

 Identificar las principales fuentes de emisión asociadas al Proyecto y georreferenciarlas

dentro del dominio de modelación.

 Modelar la dispersión de los contaminantes atmosféricos mediante el software CALPUFF

para el escenario en estudio.

 Establecer el aporte total de la concentración de contaminantes atmosféricos en cada

receptor de interés y presentar las concentraciones esperadas dentro del dominio de

modelación mediante curvas de isoconcentración e isodepositación para cada

contaminante, según corresponda.

www.dfmconsultores.cl

4
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

##### 3 METODOLOGÍA

En el siguiente apartado, se describen los pasos que definen la metodología utilizada para la

elaboración de la modelación de dispersión de contaminantes del Proyecto.

 - _Estimación de emisiones y fuentes de emisión:_ a partir de los resultados del inventario de

emisiones (Anexo 2-1: Estimación de Emisiones), se definen las fuentes de emisión y

emisiones asociadas a cada una de ellas, las cuales son georreferenciadas dentro del

dominio de modelación.

 - _Receptores discretos:_ se definen los receptores de interés dentro del dominio de

modelación con el fin de evaluar el aporte de la concentración de contaminantes

atmosféricos sobre cada uno de estos, tales como estaciones de monitoreo, viviendas, etc.

 - _Modelo meteorológico Weather Research and Forecasting (WRF):_ se modela la

meteorología de un año calendario, para posteriormente utilizar dicho modelo en la

modelación de dispersión de contaminantes atmosféricos.

 - _Caracterización meteorológica:_ se realiza una caracterización de las variables

meteorológicas relevantes a partir de coordenadas dentro del dominio del modelo

meteorológico WRF.

 - _Topografía:_ se obtienen los datos de topografía del dominio de modelación a partir de

Shuttle Radar Topography (SRTM1), cuya resolución es aproximadamente de 30 metros.

Estos datos son parámetros relevantes de entrada en cuanto al relieve del dominio de

modelación.

 - _Uso de suelos:_ se obtienen los datos de uso de suelos de la zona a partir de los archivos

Global Land Cover Characterization (GLCC) publicados por el US Geological Survey (USGS).

Estos datos son parámetros relevantes de entrada para que el modelo posea la información

acerca de los diversos tipos de uso de suelos presente dentro del dominio de modelación.

 - _Modelación de dispersión de contaminantes atmosféricos (CALPUFF):_ a partir de los

principales datos de entrada del modelo, tales como fuentes de emisión, receptores

discretos, datos meteorológicos, topografía y uso de suelos, se realiza la modelación de

dispersión de contaminantes utilizando el software CALPUFF, a modo de determinar la

dispersión de los siguientes contaminantes: material particulado respirable fino (MP2.5),

material particulado respirable (MP10), material particulado sedimentable (MPS), dióxido

de nitrógeno (NO 2 ), dióxido de azufre (SO 2 ) y monóxido de carbono (CO). Se ha incorporado

www.dfmconsultores.cl

5
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

el módulo de transformación química (RIVAD/ISORROPIA) para la cuantificación del material

particulado secundario, en particular, la transformación de SO 2 a SO 4, y NO/NO 2 en HNO 3 y

NO 3 .

 - _Análisis de resultados:_ a partir de los resultados de la modelación, se presentan los aportes

del Proyecto en cuanto a la concentración de los contaminantes modelados para cada uno

de los receptores discretos identificados. Además, se presentan las curvas de

isoconcentración e isodepositación dentro del dominio de modelación.

 - _Conclusiones:_ se presentan las principales conclusiones del estudio realizado.

De esta manera, conforme a los pasos señalados anteriormente, en la siguiente figura se muestra

un mapa conceptual con los principales ejes de la metodología de trabajo descrita.

**Figura 3-1. Diagrama Metodología de Trabajo.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

6
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

##### 4 RESUMEN DE LA ESTIMACIÓN DE EMISIONES ATMOSFÉRICAS

A continuación, en la Tabla 4-1 se presenta un resumen de las emisiones de contaminantes

atmosféricos estimadas para el Año 1 de la Fase de Construcción del Proyecto (Año de máxima

emisión).

**Tabla 4-1. Resumen de emisiones. Año 1 de la Fase de Construcción del Proyecto.**

|Actividad|Emisión (t/año)|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Actividad**|**MP2.5**|**MP10**|**MPS**|**CO**|**NOx**|**COVs**|**SO2 **|**NH3 **|
|Movimiento de Tierra|1,050|4,516|11,912||||||
|Maquinaria|0,811|0,811|0,811|6,273|8,358|0,887|0,014|0,004|
|Grupos electrógenos|0,368|0,368|0,368|1,127|5,230|0,427|0,344||
|Resuspensión de polvo por<br>transporte|1,277|11,349|41,432||||||
|Combustión por transporte|0,051|0,051|0,051|0,590|2,498|0,105|0,003|0,001|
|**Total**|**3,556**|**17,094**|**54,573**|**7,990**|**16,086**|**1,419**|**0,360**|**0,005**|

Fuente: Elaboración propia en base a Anexo 2-1: Estimación de Emisiones, componente de la presente DIA.

Para efectos del siguiente informe, las emisiones por modelar, para cada caso, están acotadas a

aquellas cuyas fuentes de emisión están contenidas dentro del dominio de modelación.

www.dfmconsultores.cl

7
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

##### 5 MODELO DE CALIDAD DEL AIRE

A continuación, se presenta la información relevante respecto del modelo de calidad del aire

utilizado.

###### 5.1 Tipo de Modelo de Calidad del Aire Seleccionado

Los principales factores por considerar para la selección de un modelo corresponden al tipo de

terreno presente en el área del proyecto, es decir, si es plano o complejo, y el tipo de contaminante

a emitir, si es primario o secundario. De acuerdo con lo recomendado en la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA”, en el área de emplazamiento del proyecto existen factores

que podrían perturbar el carácter lineal de los vientos, por lo anterior, es necesario utilizar un

modelo que permita simular meteorología heterogénea. Debido a lo anterior, se ha seleccionado

un modelo tipo “puff” para la ejecución de la modelación de calidad del aire.

A continuación, se presenta el detalle del modelo tipo “puff” a utilizar.

###### 5.2 Descripción del Modelo de Calidad del Aire Seleccionado - CALPUFF

Como se indicó anteriormente, el entorno del área del proyecto presenta sectores de topografía

compleja, que podrían interferir en el carácter lineal de los vientos, se seleccionó como modelo de

calidad del aire, CALPUFF. La descripción del mencionado modelo se presenta a continuación.

CALPUFF, es un modelo de libre disposición, que fue desarrollado por Research Corporation, siendo

Atmospheric Studies Group de Exponent [(2)], empresa que es su soporte técnico actual.

Es un modelo de dispersión de contaminantes, no estacionario, multi-capa, que es capaz de modelar

múltiples especies. Puede simular los efectos del tiempo - y en el espacio - las diversas condiciones

meteorológicas en el transporte de contaminantes. Corresponde a un modelo Lagrangiano
Gaussiano de transporte y dispersión de “puff” emitidos por las fuentes emisoras consideradas.

Dentro de las capacidades del Modelo de Calidad del Aire, se puede destacar lo siguiente:

 - Simulación de procesos complejos: fumigación, estancamiento y recirculación.

 - Modelación de transporte de contaminantes de largo alcance.

 - Incorporación de efectos de terreno complejo en la dispersión de contaminantes.

 - Modelación de procesos de transformaciones químicas.

2 [www.src.com/calpuff/calpuff1.htm](http://www.src.com/calpuff/calpuff1.htm)

www.dfmconsultores.cl

8
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Se ha incorporado el módulo de transformación química (RIVAD/ISORROPIA) para la cuantificación

del material particulado secundario, en particular, la transformación de SO 2 a SO 4, y NO/NO 2 en

HNO 3 y NO 3 .

Posee un módulo para realizar el post-procesamiento de datos, denominado CALPOST, el cual

calcula las concentraciones en los receptores de interés, permitiendo gestionar los datos para cada

contaminante según el período de tiempo requerido para el análisis.

www.dfmconsultores.cl

9
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

###### 5.3 Características del Modelo de Dispersión de Contaminantes

5.3.1 Dominio de la Modelación

En la Figura 5-1 se presenta el dominio de modelación, el cual corresponde a un área de 18 x 18

kilómetros con 324 celdas, de 1.000 × 1.000 m cada una.

**Figura 5-1. Dominio de Modelación.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

10
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.3.2 Topografía del Sector

La topografía del sector se ha extraído de Shuttle Radar Topography Mission, SRTM1, cuya

resolución es aproximadamente 30 m.

El archivo SRTM1 ha sido incorporado al modelo con el objetivo de proporcionar la altura de los

puntos de interés. En la Figura 5-2 se presenta una imagen de la información utilizada.

**Figura 5-2. Topografía del Dominio de Modelación.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

11
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.3.3 Uso de Suelos

De acuerdo con el dominio de modelación y con la información relacionada al uso de suelo de la

zona, obtenida a través de los archivos Global Land Cover Characterization (GLCC) publicados por el

U.S. Geological Survey (USGS), en la Figura 5-3 se presentan los principales usos de suelos dentro

del dominio señalado, en donde se puede apreciar que predominan los suelos del tipo agrícola, con

cierta presencia de áreas como bosques y acuíferos.

**Figura 5-3. Uso de Suelos del Dominio de Modelación.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

12
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

###### 5.4 Descripción del Modelo Meteorológico Seleccionado - WRF

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

a continuación en la Tabla 5-1, estos fueron seleccionados por su capacidad de adaptación a la

topografía compleja y a modelos de alta resolución (< 3 km). La configuración del modelo se

presenta en el Apéndice 1: Archivos Digitales Modelación (sección 7 del presente informe).

www.dfmconsultores.cl

13
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Tabla 5-1. Configuración parámetros principales WRF.**

|Parámetro|Valor|
|---|---|
|**Dominio**|**Dominio**|
|Resolución horizontal|1 km|
|Proyección|Lambert|
|Dimensión|67x67x44|
|Número de niveles verticales|44|
|Niveles verticales (eta)|0.000000, 0.051578, 0.101822, 0.150735, 0.198315, 0.244562, 0.289477,<br>0.333059,<br>0.375309,<br>0.416226,<br>0.455810, 0.494062, 0.530982, 0.566569, 0.600823, 0.633745, 0.665334,<br>0.695591, 0.724515, 0.752107, 0.778366, 0.803292, 0.826886, 0.849148,<br>0.870076, 0.889673, 0.907937, 0.923302, 0.937101, 0.949333, 0.960000,<br>0.969101, 0.976635, 0.982603, 0.987005, 0.989841, 0.991111, 0.992381,<br>0.993651, 0.994921, 0.996190, 0.997460, 0.998730, 1.000000|
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

Fuente: Elaboración Propia.

www.dfmconsultores.cl

14
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.4.1.1 _Selección año de modelación_

Para seleccionar el año de modelación se consideraron los datos de las concentraciones de

contaminantes atmosféricos, particularmente los de material particulado respirable (MP10), en la

estación de monitoreo Casablanca. Específicamente, se evaluó el valor del estadígrafo de

concentración media anual del último trienio, el cual se obtuvo de los resultados presentados en los

informes de monitoreo. De esta manera, se consideraron las medias anuales de los años 2020, 2021

y 2022, los cuales se presentan en la Tabla 5-2.

**Tabla 5-2. Concentración media anual de MP10 en años 2020 - 2022, estación de monitoreo Casablanca.**

|Estación|Año|Concentración Media Anual MP10<br>(μg/m3N)|
|---|---|---|
|Casablanca|2020|34|
|Casablanca|2021|32|
|Casablanca|2022|30|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

De la tabla precedente, es posible observar que la concentración media anual más alta de MP10 se

obtiene en el año 2020 para la estación de monitoreo Casablanca, por lo que este año corresponde

al año más desfavorable.

Así, de acuerdo con la información obtenida, se definió el año 2020 como año de modelación,

considerando que es el año más conservador, en cuanto a la calidad del aire de material particulado

respirable en la zona donde se emplazará el proyecto.

www.dfmconsultores.cl

15
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

###### 5.5 Caracterización de Clima en el Área del Proyecto

La zona donde se emplazará el Proyecto se encuentra dentro de la comuna de Casablanca, provincia

de Valparaíso, en la Región de Valparaíso, por ende, la descripción climática se circunscribe a esta

zona.

Conforme con el documento “Climatología Regional” de la Dirección Meteorológica de Chile (DMC,

2001), el clima de la región se define como templado cálido con lluvias invernales, estación seca

prolongada y gran nubosidad, que se caracteriza porque los contrastes diarios de temperatura se

atenúan por el efecto oceánico y son poco acentuados durante el año; así, presenta, de manera

generalizada a lo largo del año, una amplia cobertura de nubosidad baja matinal y humedad relativa

elevada.

El régimen térmico anual de esta región (ver Figura 5-4), marcado en su parte central, por el valle

transversal del río Aconcagua, deja ver claramente su influencia con un gradiente térmico de 2°C

entre Los Andes y Concón. En tanto, el sector cordillerano presenta una disminución de hasta 4°C

en sus valores de temperatura media anual, en relación con aquellas zonas ubicadas más hacia el

oeste de la región.

Respecto al espacio geográfico en el cual se emplaza el proyecto, el cual se encuentra en el sector

suroeste de la región, donde, al norte limita con las urbes de Valparaíso y Quilpué, al sur y este con

la Región Metropolitana y al oeste con Algarrobo y con el Mar Chileno, se presentan temperaturas

medias anuales de 14°C, aproximadamente.

www.dfmconsultores.cl

16
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-4. Campo de Isotermas. Región de Valparaíso.**

Fuente: Elaboración Propia a partir de información digital obtenida de la web de Infraestructura de Datos Geoespaciales de Chile (IDE

CHILE, 2017).

Por su parte, el régimen de lluvias anuales en la región (ver Figura 5-5) presenta valores significativos

en el sector costero, los que aumentan a medida que se incrementa la latitud, alcanzando hasta más

www.dfmconsultores.cl

17
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

allá de los 400 mm anuales. En tanto, la zona intermedia registra valores que, aunque más bajos que

en la parte costera sur de la región, no dejan de ser significativos, superando los 300 mm. Por último,

en su parte cordillerana, la precipitación se incrementa más allá de los 600 mm anuales.

**Figura 5-5. Campo de Isoyetas. Región de Valparaíso.**

Fuente: Elaboración Propia a partir de información digital obtenida de la web de Infraestructura de Datos Geoespaciales de Chile (IDE

CHILE, 2019).

www.dfmconsultores.cl

18
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Respecto al espacio geográfico en el cual se emplaza el proyecto, presenta precipitaciones alrededor

de los 500 mm.

Por otro lado, para visualizar la variación de las temperaturas y las precipitaciones a lo largo del año,

en la siguiente figura se presenta a modo referencial el climograma de Valparaíso, en donde se

aprecia que los meses de mayor pluviometría corresponden a junio y julio, los cuales coinciden con

los meses en donde se presentan las menores temperaturas a lo largo del año.

**Figura 5-6. Climograma de la Región de Valparaíso.**

Fuente: “Climatología Regional” (DMC, 2001).

www.dfmconsultores.cl

19
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Con respecto al clima, de acuerdo con la clasificación de Köppen, la Región de Valparaíso

presenta los siguientes subtipos climáticos:

 - BSk: Clima semiárido.

 - BSk (s): Clima semiárido de lluvia invernal.

 - BSk (s) (i): Clima semiárido de lluvia invernal e influencia costera.

 - Csb: Clima mediterráneo de lluvia invernal.

 - Csb (h): Clima mediterráneo de lluvia invernal de altura.

 - Csb (i): Clima mediterráneo de lluvia invernal e influencia costera.

 - Csc: Clima mediterráneo frío de lluvia invernal.

 - ET: Clima de tundra.

 - ET (s): Clima de tundra de lluvia invernal.

De esta forma, en la Figura 5-7 se presenta la clasificación climática para la Región de Valparaíso

conforme a los subtipos climáticos mencionados anteriormente.

Así, en dicha figura, se puede observar que el clima correspondiente a la zona en donde se emplaza

el proyecto corresponde a un clima del tipo mediterráneo de lluvia invernal, el cual se caracteriza

por presentar, usualmente, promedio termal anual igual o mayor a 10°C, siendo el promedio del

mes más cálido menor a 22°C, aproximadamente. De esta manera, los inviernos suelen ser

templados, mientras que los veranos son secos y cálidos. A su vez, la mayor parte de las lluvias caen

en invierno o en estaciones intermedias.

www.dfmconsultores.cl

20
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-7. Clasificación climática según Köppen. Región de Valparaíso.**

Fuente: Elaboración Propia a partir de información digital obtenida de la web de Infraestructura de Datos Geoespaciales de Chile (IDE

CHILE, 2018).

www.dfmconsultores.cl

21
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.5.1 Evolución del Clima producto del Cambio Climático en el Área del

Proyecto

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

A continuación, en la Tabla 5-3, se presentan los índices de velocidad de temperatura media anual,

precipitación acumulada anual y viento promedio anual, analizados para la comuna de Casablanca,

provincia de Valparaíso.

**Tabla 5-3. Principales índices evaluación cambio climático. Región de Valparaíso, provincia de Valparaíso,**

**comuna Casablanca.**

|Índice|Periodo|Valor|
|---|---|---|
|Temperatura media anual (°C)|Presente|13,80|
|Temperatura media anual (°C)|Futuro|14,89|
|Temperatura media anual (°C)|Cambio (Futuro - Presente)|1,09|
|Precipitación acumulada anual (mm)|Presente|474,43|
|Precipitación acumulada anual (mm)|Futuro|386,64|
|Precipitación acumulada anual (mm)|Cambio (Futuro - Presente)|-87,78|
|Velocidad viento promedio anual<br>(m/s)|Presente|2,33|
|Velocidad viento promedio anual<br>(m/s)|Futuro|2,30|
|Velocidad viento promedio anual<br>(m/s)|Cambio (Futuro - Presente)|-0,03|

Fuente: Elaboración propia, en base a datos climáticos anuales por comuna [(4)] .

Así, de la tabla precedente se puede observar que, en la comuna de Casablanca, que es donde se

localizará el proyecto en estudio, se identifica un aumento de la temperatura media anual en los

próximos 12 a 42 años de 1,09 °C.

3 [Link web Ley Marco de Cambio Climático: https://www.bcn.cl/leychile/navegar?idNorma=1177286](https://www.bcn.cl/leychile/navegar?idNorma=1177286)
4 [ARClim, herramienta “Explorador de Amenazas Climáticas”. Acceso desde: https://arclim.mma.gob.cl/amenazas/](https://arclim.mma.gob.cl/amenazas/)

www.dfmconsultores.cl

22
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Por su parte, con respecto a las precipitaciones acumuladas anuales, es posible observar una

diferencia de -87,78 mm, lo que corresponde a una disminución del 18,50% de los registros anuales

de precipitación futuros, con respecto a los valores actuales.

Por último, en cuanto a la velocidad media anual del viento, se observa que presentará una variación

de -0,03 m/s, lo que corresponde a una disminución del 1,33% del valor actual registrado.

A continuación, de forma complementaria e ilustrativa, en las Figura 5-8, Figura 5-9 y Figura 5-10 se

presenta la comparación entre la situación actual y futura de las variables de temperatura media

anual, precipitaciones acumuladas anuales y velocidad del viento promedio anual, respectivamente,

correspondientes a la Región de Valparaíso.

Cabe señalar que, dado que en la Figura 5-10 la variación de la velocidad promedio anual del viento

es leve, e incluso prácticamente imperceptible para los rangos establecidos, se presenta la Figura

5-11, donde se observa ilustrativamente la evolución, en porcentaje, entre la situación actual y

futura de esta variable.

www.dfmconsultores.cl

23
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-8. Comparación Temperatura Media Anual entre situación actual y futura. Región de Valparaíso.**

Fuente: Elaboración Propia a partir de información digital obtenida de la web de ARClim, “Explorador de Amenazas Climáticas” [ (4)] .

www.dfmconsultores.cl

24
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-9. Comparación Precipitación Acumulada Anual entre situación actual y futura. Región de**

**Valparaíso.**

Fuente: Elaboración Propia a partir de información digital obtenida de la web de ARClim, “Explorador de Amenazas Climáticas” [ (4)] .

www.dfmconsultores.cl

25
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-10. Comparación Velocidad Media Anual Viento entre situación actual y futura. Región de**

**Valparaíso.**

Fuente: Elaboración Propia a partir de información digital obtenida de la web de ARClim, “Explorador de Amenazas Climáticas” [ (4)] .

www.dfmconsultores.cl

26
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-11. Evolución Velocidad Media Anual Viento. Región de Valparaíso.**

Fuente: Elaboración Propia a partir de información digital obtenida de la web de ARClim, “Explorador de Amenazas Climáticas” [ (4)] .

www.dfmconsultores.cl

27
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

###### 5.6 Caracterización Meteorológica del Área del Proyecto

En este inciso se presenta la caracterización de la meteorología observada y modelada para el sector

del proyecto.

5.6.1 Meteorología de Superficie - Valores Observados

Para caracterizar la meteorología del área del Proyecto se utilizan los registros horarios de velocidad

del viento, dirección del viento, temperatura, humedad relativa, presión atmosférica y radiación

solar, pertenecientes a la estación de monitoreo Casablanca, de propiedad de la empresa

TRESMONTES S.A., cuyos principales resultados fueron recuperados desde “Anexo 03.2 Modelación
de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

Las coordenadas UTM de la estación de monitoreo indicada se presentan en la Tabla 5-4, junto con

las variables que miden y el periodo de monitoreo respectivo.

**Tabla 5-4. Coordenadas de Ubicación, Estación de Monitoreo Casablanca.**

|Nombre|Variables Meteorológicas<br>Registradas|Periodo monitoreado<br>considerado para este<br>estudio|Coordenadas (Datum WGS84)|Col5|
|---|---|---|---|---|
|**Nombre**|**Variables Meteorológicas**<br>**Registradas**|**Periodo monitoreado**<br>**considerado para este**<br>**estudio**|**Este (m)**|**Norte (m)**|
|Casablanca|Velocidad del Viento (m/s)|Enero 2020 a<br>Diciembre 2022|278.002|6.309.012|
|Casablanca|Dirección del Viento (°)|Dirección del Viento (°)|Dirección del Viento (°)|Dirección del Viento (°)|
|Casablanca|Temperatura del Aire (°C)|Temperatura del Aire (°C)|Temperatura del Aire (°C)|Temperatura del Aire (°C)|
|Casablanca|Humedad Relativa (%)|Humedad Relativa (%)|Humedad Relativa (%)|Humedad Relativa (%)|
|Casablanca|Precipitación Acumulada (mm)|Precipitación Acumulada (mm)|Precipitación Acumulada (mm)|Precipitación Acumulada (mm)|
|Casablanca|Presión Atmosférica (mmHg)|Presión Atmosférica (mmHg)|Presión Atmosférica (mmHg)|Presión Atmosférica (mmHg)|
|Casablanca|Radiación Solar (W/m2)|Radiación Solar (W/m2)|Radiación Solar (W/m2)|Radiación Solar (W/m2)|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

A modo de complemento, en la Tabla 5-21, se presenta el detalle de las técnicas de medición y los

equipos utilizados para medir las variables meteorológicas registradas para las estaciones de

monitoreo mencionadas.

www.dfmconsultores.cl

28
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Tabla 5-5. Equipos y principios de operación registro de variables meteorológicas.**

|Nombre Estación|Parámetro|Unidad|Equipo - Serie|Principio de Operación|
|---|---|---|---|---|
|Casablanca|Velocidad del<br>Viento|m/s|Young std 5103 - 57026|Generación de pulso /<br>potenciómetro|
|Casablanca|Dirección del<br>Viento|°|Young std 5103 - 57026|Generación de pulso /<br>potenciómetro|
|Casablanca|Temperatura|°C|Vaisala, HMP155 - E4010123|Sensor polinomial|
|Casablanca|Humedad Relativa|%|Vaisala, HMP155 - E4010123|Sensor polinomial|
|Casablanca|Precipitación|mm|Texas TR525M - 47611-511|Tipping Bucket|
|Casablanca|Presión<br>Atmosférica|mmHg|Vaisala, PTB110 - F4540027|Sensor capacitivo|
|Casablanca|Radiación Solar|W/m2|Licor Li200R - PY77315|Detector fotovoltaico|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

En la Figura 5-12 se puede observar la ubicación referencial de las estaciones de monitoreo

meteorológico, respecto a la zona de emplazamiento del proyecto.

www.dfmconsultores.cl

29
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-12. Ubicación Referencial Estación de Monitoreo Meteorológico.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

30
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

A continuación, en los siguientes acápites, desarrollan el análisis de las variables meteorológicas

indicadas anteriormente para la estación de monitoreo respectiva.

5.6.1.1 _Estación Casablanca_

a) Velocidad y Dirección del Viento

En la Tabla 5-6 se presenta el resumen de información para la variable velocidad del viento,

específicamente el promedio, máximo y mínimo del año en estudio, además del porcentaje de

calmas, el cual se define como el porcentaje del tiempo en que la velocidad del viento es menor a

0,5 m/s.

De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”,

las series de datos meteorológicos deben contener un 75% de datos válidos, lo cual se cumple para

el periodo en estudio. En consecuencia, el periodo mencionado será utilizado para los siguientes

análisis.

**Tabla 5-6. Resumen de información Velocidad del Viento. Estación Casablanca.**

|Parámetro|Variable|Año|Col4|Col5|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2020**|**2021**|**2022**|
|Velocidad de Viento (m/s)|Promedio|1,8|1,9|1,8|
|Velocidad de Viento (m/s)|Máximo|9,8|8,9|9,0|
|Velocidad de Viento (m/s)|Mínimo|0,0|0,0|0,0|
|Porcentaje de Calmas (%)|Porcentaje de Calmas (%)|12,2|11,7|12,8|
|Datos Válidos (%)|Datos Válidos (%)|98,6%|100,0%|100,0%|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

A continuación, se muestran las series de tiempo, ciclos diarios y ciclo estacional para las variables

meteorológicas observadas velocidad y dirección del viento.

www.dfmconsultores.cl

31
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Series de Tiempo

De tal manera de verificar la completitud de los datos, en la Figura 5-13 y Figura 5-14 se presentan

las series de tiempo para la variable velocidad y dirección del viento respectivamente, donde se

puede comprobar que se cumple con que la proporción de datos válidos es igual o superior al 75%

para el periodo en estudio.

Además, se puede identificar que las velocidades de viento se encuentran mayormente entre los 0

y 6,0 m/s, exceptuando ciertos valores que sobrepasan este intervalo, alcanzando registros cercanos

a los 10,0 m/s.

**Figura 5-13. Serie de Tiempo Velocidad del Viento Observado. Enero 2020 a diciembre de 2022. Estación**

**Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

32
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

En cuanto a la dirección del viento, se puede identificar una mayor concentración de datos entre los

250 y 360°, así como también valores que rondan los 100°.

**Figura 5-14. Serie de Tiempo Dirección del Viento Observado. Enero 2020 a diciembre de 2022. Estación**

**Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

Por otro lado, para caracterizar la información anual registrada, tanto para la velocidad como para

la dirección del viento, en la Tabla 5-7 se presenta la frecuencia de distribución para la velocidad y

dirección del viento observada.

www.dfmconsultores.cl

33
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Tabla 5-7. Frecuencia de distribución Velocidad y Dirección del Viento. Enero 2020 a diciembre de 2022. Estación Casablanca.**

|Dirección|Col2|Distribución Porcentual de Velocidad del Viento (m/s)|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Dirección**|**Dirección**|**0,50 - 2,10**|**2,10 - 3,60**|**3,60 - 5,70**|**5,70 - 8,80**|**8,80 - 11,10**|**>= 11,10**|**Total (%)**|
|348,75 - 11,25|N|2,67%|1,09%|0,70%|0,14%|0,01%|0,00%|4,61%|
|11,25 - 33,75|NNE|1,79%|0,72%|0,49%|0,06%|0,00%|0,00%|3,06%|
|33,75 - 56,25|NE|1,87%|0,23%|0,06%|0,00%|0,00%|0,00%|2,15%|
|56,25 - 78,75|ENE|2,86%|0,12%|0,01%|0,00%|0,00%|0,00%|3,00%|
|78,75 - 101,25|E|5,02%|0,12%|0,01%|0,00%|0,00%|0,00%|5,15%|
|101,25 - 123,75|ESE|5,52%|0,13%|0,02%|0,00%|0,00%|0,00%|5,66%|
|123,75 - 146,25|SE|4,12%|0,10%|0,01%|0,00%|0,00%|0,00%|4,22%|
|146,25 - 168,75|SSE|2,68%|0,27%|0,03%|0,00%|0,00%|0,00%|2,98%|
|168,75 - 191,25|S|2,22%|0,63%|0,15%|0,00%|0,00%|0,00%|2,99%|
|191,25 - 213,75|SSW|2,39%|1,11%|0,83%|0,18%|0,00%|0,00%|4,51%|
|213,75 - 236,25|SW|2,10%|2,10%|2,30%|0,47%|0,00%|0,00%|6,96%|
|236,25 - 258,75|WSW|2,22%|2,61%|3,80%|0,61%|0,00%|0,00%|9,24%|
|258,75 - 281,25|W|3,27%|2,15%|1,60%|0,03%|0,00%|0,00%|7,05%|
|281,25 - 303,75|WNW|5,35%|2,21%|1,62%|0,05%|0,00%|0,00%|9,23%|
|303,75 - 326,25|NW|6,80%|2,13%|0,94%|0,11%|0,00%|0,00%|9,97%|
|326,25 - 348,75|NNW|4,58%|1,68%|0,61%|0,10%|0,00%|0,00%|6,97%|
|Sub-Total|Sub-Total|55,45%|17,39%|13,17%|1,74%|0,02%|0,00%|87,76%|
|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|12,24%|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)] “Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

34
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Ciclos Diarios

En la Figura 5-15 se presenta el ciclo diario para la variable velocidad del viento observada, en donde

se puede observar que las menores velocidades ocurren durante el periodo nocturno y de

madrugada, específicamente entre las 23:00 y 07:00 horas, en donde se alcanza un mínimo

promedio de velocidad de viento de aproximadamente 0,9 m/s. Luego, la velocidad comienza a

incrementar sostenidamente alcanzando las mayores intensidades de viento a las 14:00 horas,

adoptando valores máximos promedios que alcanzan los 4 m/s. Posteriormente, la velocidad

desciende hasta alcanzar los valores nocturnos, iniciando nuevamente el ciclo. Cabe mencionar que

el rango de oscilación del 90% de los datos posee una diferencia de 5,0 m/s al momento de máxima

velocidad y de 1,8 m/s al momento de mínima velocidad.

**Figura 5-15. Ciclo Diario Velocidad del Viento Observado. Enero 2020 a diciembre de 2022. Estación**

**Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

35
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

En la Figura 5-16 se presenta el ciclo diario de la variable meteorológica dirección del viento. En ella

se puede observar que, durante la noche y madrugada, específicamente entre las 20:00 y 08:00

horas, los vientos presentan dirección este sureste (ESE), alcanzando máxima frecuencia a las 22:00

horas. Por el contrario, durante la mañana, específicamente entre las 07:00 y las 11:00 horas, los

vientos presentan dirección noroeste (NO), alcanzando la frecuencia más alta a las 10:00 horas. Por

último, durante la tarde, específicamente entre las 12:00 y las 19:00 horas, los vientos presentan

dirección oeste suroeste (OSO), principalmente, alcanzando máxima frecuencia a las 15:00 horas.

**Figura 5-16. Ciclo Diario Dirección del Viento Observado. Enero 2020 a diciembre de 2022. Estación**

**Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

36
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Ciclo Estacional

En la Figura 5-17 se presenta el ciclo estacional de vientos observados, en donde es posible apreciar

que las mayores intensidades de viento se producen en los meses de octubre y enero durante la

tarde, específicamente a las 12:00 y las 16:00 horas; mientras que las menores intensidades se

presentan durante la noche, la madrugada y la mañana, entre las 22:00 y las 09:00 horas, durante

prácticamente todo el año.

Por otro lado, en cuanto a la dirección del viento, es posible observar una marcada predominancia

de vientos norte (N), nornoreste (NNE) y nornoroeste (NNO) durante todos los meses del año,

principalmente en el rango horario entre las 00:00 y las 10:00 horas.

Luego, durante todos los meses del periodo analizado, en el horario comprendido entre las 12:00 y

19:00 horas, se observa que la dirección del viento es principalmente oeste (O) y, en algunos meses,

específicamente en mayo y julio, también se observan vientos oeste noroeste (ONO).

Por último, entre los meses de noviembre a marzo, en el horario comprendido entre las 20:00 y las

23:00 horas, se observa que la dirección del viento es oeste (O) y oeste noroeste (ONO). Por su

parte, para los meses entre abril y septiembre, en el mismo rango horario mencionado, se observa

predominancia de vientos este (E), este noreste (ENE) y noreste (NE).

www.dfmconsultores.cl

37
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-17. Ciclo Estacional de Velocidad y Dirección del Viento Observado. Enero 2020 a Diciembre 2022.**

**Estación Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

38
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

b) Temperatura

A continuación, en la Tabla 5-8 se muestra el resumen de información para la variable temperatura,

especificando promedio, máximo y mínimo anual para el periodo comprendido entre enero 2020 y

diciembre 2022. De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del

Aire en el SEIA”, las series de datos meteorológicos deben contar con un 75% de datos válidos, lo

cual se cumple para el periodo en estudio. En consecuencia, el periodo mencionado será utilizado

para los siguientes análisis.

**Tabla 5-8. Resumen de información Temperatura Observada. Estación Casablanca.**

|Parámetro|Variable|Año|Col4|Col5|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2020**|**2021**|**2022**|
|Temperatura (°C)|Promedio|14,2|13,0|12,9|
|Temperatura (°C)|Máximo|35,7|33,4|33,3|
|Temperatura (°C)|Mínimo|-1,8|-5,4|-5,1|
|Datos Válidos (%)|Datos Válidos (%)|98,6%|100,0%|100,0%|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

A continuación, en los siguientes apartados se presenta la serie de tiempo, ciclo diario y ciclo

estacional observados para la variable meteorológica temperatura.

www.dfmconsultores.cl

39
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Serie de Tiempo

A modo de verificación de la completitud de los datos obtenidos mediante la estación de monitoreo

meteorológico Casablanca, en la Figura 5-18 se presenta la serie de tiempo para la variable

temperatura observada. En ésta es posible comprobar que se cumple con que la proporción de

datos válidos es igual o superior al 75% para el periodo en estudio.

Adicionalmente, se puede identificar que las temperaturas registradas se encuentran

principalmente entre los 0 y 30°C aproximadamente, con algunas excepciones durante los meses de

julio de 2021 y junio de 2022, donde se observan temperaturas que alcanzan los -5°C.

**Figura 5-18. Serie de Tiempo Temperatura Observada. Enero 2020 a diciembre de 2022. Estación**

**Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

40
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Ciclo Diario

En la Figura 5-19 se expone el ciclo diario para la variable temperatura observada, en donde es

posible observar que las menores temperaturas ocurren durante la madrugada, específicamente

entre las 01:00 y 07:00 horas, aproximadamente, alcanzando un mínimo promedio aproximado de

temperatura de 7,5°C a las 06:00 horas. Desde las 07:00 horas en adelante, la temperatura comienza

a aumentar paulatinamente hasta alcanzar un máximo promedio aproximado de 21,5°C entre las

13:00 y las 14:00 horas, para luego comenzar a disminuir de manera gradual hasta alcanzar los

valores de temperatura nocturnas, por bajo los 10 °C aproximadamente, para luego dar comienzo

nuevamente al ciclo. Cabe mencionar que el rango de oscilación del 90% de los datos posee una

diferencia de 15,5°C al momento de máxima temperatura y de 11°C al momento de mínima

temperatura, aproximadamente.

**Figura 5-19. Ciclo Diario Temperatura Observada. Enero 2020 a diciembre de 2022. Estación Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

41
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Ciclo Estacional

En la Figura 5-20 se presenta el ciclo estacional de la temperatura observada, en donde es posible

notar que las mayores temperaturas se registran durante los meses de verano, específicamente

entre noviembre y marzo, en el periodo de la tarde, alcanzando valores alrededor de los 25°C entre

las 11:00 y 16:00 horas. Por otro lado, las menores temperaturas se registran durante los meses

entre mayo y septiembre, principalmente, en donde se presentan temperaturas entre los 0°C y 5°C,

en el horario de madrugada y durante primeras horas de la mañana, específicamente entre las 01:00

y 09:00 horas.

**Figura 5-20. Ciclo Estacional Temperatura Observada. Enero 2020 a diciembre de 2022. Estación**

**Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

42
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

c) Humedad Relativa

A continuación, en la Tabla 5-9 se presenta el resumen de información para la variable humedad

relativa, detallando los valores promedio, máximos y mínimos anuales para los años 2020, 2021 y

2022. De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA”, las series de datos meteorológicos deben contener un 75% de datos válidos, condición la cual

se cumple para el periodo en estudio. En consecuencia, el periodo mencionado será utilizado para

los siguientes análisis.

**Tabla 5-9. Resumen de información Humedad Relativa Observada. Estación Casablanca.**

|Parámetro|Variable|Año|Col4|Col5|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2020**|**2021**|**2022**|
|Humedad Relativa (%)|Promedio|72,1|76,0|78,0|
|Humedad Relativa (%)|Máximo|100,0|100,0|100,0|
|Humedad Relativa (%)|Mínimo|10,0|12,3|13,7|
|% Datos Válidos|% Datos Válidos|97,7%|100,0%|100,0%|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

De esta forma, a continuación, se presentan la serie de tiempo, ciclo diario y ciclo estacional

observados para la variable meteorológica humedad relativa.

www.dfmconsultores.cl

43
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Serie de Tiempo

A modo de verificación de completitud de datos, en la Figura 5-21 se presenta la serie de tiempo

para la variable meteorológica humedad relativa, en la cual se puede comprobar que se cumple con

que la proporción de datos válidos es igual o superior al 75% para el periodo en estudio

A su vez, se observa que los valores se encuentran entre el 0% y 100%. Para el periodo en estudio,

la predominancia de registros se encuentra entre el 20% y 100% de humedad relativa,

aproximadamente.

**Figura 5-21. Serie de Tiempo Humedad Relativa Observada. Enero 2020 a diciembre de 2022. Estación**

**Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

44
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Ciclo Diario

En la Figura 5-22 se presenta el ciclo diario para la variable humedad relativa para el periodo en

estudio, en donde es posible apreciar que, durante el periodo nocturno y de madrugada, es decir,

entre las 00:00 y 07:00 horas, se presentan los máximos valores de humedad, alcanzando un registro

máximo aproximado de 93% a las 05:00 horas. Posteriormente, los valores comienzan a descender

a lo largo del día alcanzando un mínimo promedio aproximado de 50% a las 14:00 horas, para luego

aumentar de manera paulatina, hasta adoptar los valores nocturnos, dando inicio nuevamente al

ciclo. Cabe mencionar que el rango de oscilación del 90% de los datos posee una diferencia de 56%

al momento de mínima humedad y de 30% al momento de máxima humedad relativa.

**Figura 5-22. Ciclo Diario Humedad Relativa Observada. Enero 2020 a diciembre de 2022. Estación**

**Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

45
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Ciclo Estacional

En la Figura 5-23 se presenta el ciclo estacional de la humedad relativa para el periodo en estudio,

en donde se puede apreciar que los mayores porcentajes de humedad se registran durante los

meses entre junio y octubre, durante horas de la madrugada y la mañana, entre las 00:00 y 08:00

horas, con valores cercanos al 95% de humedad relativa.

A su vez, los menores porcentajes se presentan en noviembre y abril, entre las 11:00 y 16:00 horas,

registrando valores cercanos al 40% de humedad.

**Figura 5-23. Ciclo Estacional Humedad Relativa Observada. Enero 2020 a diciembre de 2022. Estación**

**Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

46
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

d) Precipitación Acumulada

A continuación, en la Tabla 5-10 se presenta el resumen de información para la variable

precipitación acumulada registrada en la estación de monitoreo Casablanca. De acuerdo con lo

establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, las series de datos

meteorológicos deben contener un 75% de datos válidos, condición la cual se cumple para el

periodo en estudio. En consecuencia, el periodo mencionado será utilizado para los siguientes

análisis.

**Tabla 5-10. Resumen de información Precipitación acumulada Observada. Estación Casablanca.**

|Parámetro|Variable|Año|Col4|Col5|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2020**|**2021**|**2022**|
|Precipitación Acumulada (mm)|Máximo acumulado diario|49,0|36,7|35,5|
|Precipitación Acumulada (mm)|Mínimo acumulado mensual|0,0|0,0|0,0|
|Precipitación Acumulada (mm)|Máximo acumulado mensual|140,9|43,7|122,1|
|Precipitación Acumulada (mm)|Acumulado anual|243,1|145,5|266,0|
|% Datos Válidos|% Datos Válidos|98,6%|100,0%|100,0%|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

De esta forma, a continuación, se presenta el análisis de las series para la variable meteorológica

precipitación acumulada.

www.dfmconsultores.cl

47
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Serie de Tiempo

En las Figura 5-24 y Figura 5-25 se presentan las series de tiempo de la variable meteorológica

precipitación acumulada, tanto para periodo diario como mensual, con el objetivo de verificar la

completitud de los datos. En ellas se puede observar que se registran mayores precipitaciones

durante el periodo invernal de los años 2021 y 2022, específicamente durante el mes de junio, para

los años 2020 y 2022, y mes de agosto para el año 2021, alcanzando valores por sobre los 30 mm de

agua caída diaria acumulada.

Asimismo, con respecto a las precipitaciones acumuladas mensuales, el año de mayor registro

pluviométrico corresponde al 2020, específicamente al mes de junio, sobrepasando levemente los

140 mm.

**Figura 5-24. Serie de Tiempo Precipitación Diaria Acumulada. Enero 2020 a diciembre de 2022. Estación**

**Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

48
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-25. Serie de Tiempo Precipitación Mensual Acumulada. Enero 2020 a diciembre de 2022. Estación**

**Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

49
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

e) Presión Atmosférica

A continuación, en la Tabla 5-11 se presenta el resumen de información para la variable presión

atmosférica en la estación de monitoreo Casablanca, detallando los valores promedio, máximos y

mínimos anuales para los años 2020, 2021 y 2022. De acuerdo con lo establecido en la “Guía para

el Uso de Modelos de Calidad del Aire en el SEIA”, las series de datos meteorológicos deben

contener un 75% de datos válidos, condición la cual se cumple para el periodo en estudio. En

consecuencia, el periodo mencionado será utilizado para los siguientes análisis.

**Tabla 5-11. Resumen de información Presión atmosférica Observada. Estación Casablanca.**

|Parámetro|Variable|Año|Col4|Col5|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2020**|**2021**|**2022**|
|Presión Atmosférica (mmHg)|Promedio|739,6|739,5|739,6|
|Presión Atmosférica (mmHg)|Máximo|748,0|747,8|748,3|
|Presión Atmosférica (mmHg)|Mínimo|734,0|734,0|733,0|
|% Datos Válidos|% Datos Válidos|98,6%|100,0%|99,4%|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

De esta forma, a continuación, se presentan la serie de tiempo y ciclo anual observados para la

variable meteorológica presión atmosférica.

www.dfmconsultores.cl

50
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Serie de Tiempo

A modo de verificación de completitud de datos, en la Figura 5-26 se presenta la serie de tiempo

para la variable meteorológica presión atmosférica, en la cual se puede comprobar que se cumple

con que la proporción de datos válidos es igual o superior al 75% para el periodo en estudio

A su vez, se observa que los valores, principalmente, se encuentran entre los 736 y los 746 mmHg.

**Figura 5-26. Serie de Tiempo Presión atmosférica Observada. Enero 2020 a diciembre de 2022. Estación**

**Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

51
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Ciclo Anual

En la Figura 5-27 se presenta el ciclo anual de presión atmosférica registrada por la estación

Casablanca para el periodo en estudio, en donde se puede apreciar que los mayores valores de

presión atmosférica se registran durante el invierno y principios de la primavera, específicamente

entre los meses de julio y septiembre, con valores máximos que sobrepasan levemente los 741

mmHg. Por el contrario, los menores valores de presión atmosférica se registran durante los meses

de verano, particularmente entre diciembre y febrero, con valores mínimos de 738 mmHg.

**Figura 5-27. Ciclo Anual Presión atmosférica Observada. Enero 2020 a diciembre de 2022. Estación**

**Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

52
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

f) Radiación Solar

A continuación, en la Tabla 5-12 se presenta el resumen de información para la variable radiación

solar, detallando los valores promedio, máximos y mínimos anuales para los años 2020, 2021 y 2022.

De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”,

las series de datos meteorológicos deben contener un 75% de datos válidos, lo cual se cumple para

el periodo en estudio. En consecuencia, el periodo mencionado será utilizado para los siguientes

análisis.

**Tabla 5-12. Resumen de información Radiación solar Observada. Estación Casablanca.**

|Parámetro|Variable|Año|Col4|Col5|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2020**|**2021**|**2022**|
|Radiación Solar (W/m2)|Promedio|189,5|185,6|179,6|
|Radiación Solar (W/m2)|Máximo|970,8|950,9|987,5|
|Radiación Solar (W/m2)|Mínimo|0,0|0,0|0,0|
|% Datos Válidos|% Datos Válidos|98,6%|99,9%|100,0%|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

De esta forma, a continuación, se presentan la serie de tiempo, ciclo diario y ciclo estacional

observados para la variable meteorológica radiación solar.

www.dfmconsultores.cl

53
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Serie de Tiempo

A modo de verificación de completitud de datos, en la Figura 5-28 se presenta la serie de tiempo

para la variable meteorológica radiación solar, en la cual es posible comprobar que se cumple con

que la proporción de datos válidos es igual o superior al 75% para el periodo en estudio.

A su vez, se observa que los valores de radiación solar se encuentran, principalmente, entre los 0 y

950 (W/m [2] ).

**Figura 5-28. Serie de Tiempo Radiación Solar Observada. Enero 2020 a diciembre de 2022. Estación**

**Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

54
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Ciclo Diario

En la Figura 5-29 se presenta el ciclo diario para la variable meteorológica radiación solar para el

periodo en estudio. En ésta es posible apreciar que, durante el periodo nocturno y de madrugada,

específicamente entre las 20:00 y 05:00 horas, no se perciben registros para esta variable. A partir

de esta última hora, los valores de radiación incrementan de manera paulatina, alcanzando valores

máximos promedio aproximados de 610 (W/m [2] ) a las 12:00 horas. Luego, las radiaciones

disminuyen hasta alcanzar valores nulos para esta variable, dando inicio nuevamente al ciclo

**Figura 5-29. Ciclo Diario Radiación Solar Observada. Enero 2020 a diciembre de 2022. Estación Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

55
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Ciclo Estacional

En la Figura 5-30 se presenta el ciclo estacional de la radiación solar, registrada por la estación

Casablanca, para el periodo en estudio; donde se puede observar que los mayores valores de

radiación solar se registran durante el periodo de verano, principalmente entre los meses de

octubre y febrero, específicamente entre las 11:00 y 14:00 horas, registrando valores alrededor de

los 850 (W/m [2] ). Por el contrario, los menores valores de radiación solar se registran durante todo el

año durante la noche y madrugada, entre 19:00 y 06:00 horas.

**Figura 5-30. Ciclo Estacional Radiación Solar Observada. Enero 2020 a diciembre de 2022. Estación**

**Casablanca.**

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

56
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.6.2 Meteorología de Superficie - Valores Modelados

5.6.2.1 _Estación Meteorológica Casablanca_

a) Velocidad y Dirección del Viento

En la Tabla 5-13 se presenta el resumen de información para la variable velocidad del viento

modelada, específicamente el promedio, máximo y mínimo del año en estudio, además del

porcentaje de calmas, el cual se define como el porcentaje del tiempo en que la velocidad del viento

es menor a 0,5 m/s.

De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”,

las series de datos meteorológicos deben contener un 75% de datos válidos, lo cual se cumple para

el año 2020 debido a que se cuenta con la completitud de los datos a partir del modelo WRF.

**Tabla 5-13. Resumen de información Velocidad del Viento Modelado. Estación Casablanca.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2020**|
|Velocidad de Viento (m/s)|Promedio|2,51|
|Velocidad de Viento (m/s)|Mínimo|0,01|
|Velocidad de Viento (m/s)|Máximo|11,84|
|Velocidad de Viento (m/s)|Porcentaje de Calmas (%)|7,2%|
|Velocidad de Viento (m/s)|Datos Válidos (%)|100%|

Fuente: Elaboración Propia en base a los resultados del modelo WRF.

A continuación, se muestran las series de tiempo, ciclos diarios y ciclo estacional para las variables

meteorológicas modeladas velocidad y dirección del viento.

www.dfmconsultores.cl

57
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Series de Tiempo

De tal manera de verificar la completitud de los datos, en la Figura 5-31 y Figura 5-32 se presentan

las series de tiempo para la variable velocidad y dirección del viento modeladas respectivamente,

en donde es posible observar que se cuenta con el 100% de los registros para ambas variables.

Además, se puede identificar que las velocidades de viento se encuentran mayormente entre los 0

y 8 m/s, exceptuando ciertos valores que sobrepasan este intervalo, alcanzando registros que

prácticamente alcanzan los 12 m/s.

**Figura 5-31. Serie de Tiempo Velocidad del Viento Modelada. Enero a diciembre de 2020. Estación**

**Casablanca.**

Fuente: Elaboración Propia en base a los resultados del modelo WRF.

www.dfmconsultores.cl

58
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

En cuanto a la dirección del viento, se puede identificar una mayor concentración de datos en los

200 y 250°; así como también entre los 300 y los 360°; no obstante, se puede observar cierta

dispersión de datos a lo largo del periodo en estudio.

**Figura 5-32. Serie de Tiempo Dirección del Viento Modelada. Enero a diciembre de 2020. Estación**

**Casablanca.**

Fuente: Elaboración Propia en base a los resultados del modelo WRF.

Por otro lado, para caracterizar la información anual registrada tanto para la velocidad como para

la dirección del viento, en la Tabla 5-14 se presenta la frecuencia de distribución para la velocidad y

dirección del viento modelada.

www.dfmconsultores.cl

59
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Tabla 5-14. Frecuencia de distribución Velocidad y Dirección del Viento Modelada. Enero a diciembre de 2020. Estación Casablanca.**

|Dirección|Col2|Distribución Porcentual de Velocidad del Viento (m/s)|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Dirección**|**Dirección**|**0,50 - 2,10**|**2,10 - 3,60**|**3,60 - 5,70**|**5,70 - 8,80**|**8,80 - 11,10**|**>= 11,10**|**Total (%)**|
|348,75 - 11,25|N|3,7%|1,2%|0,5%|0,3%|0,1%|0,0%|5,7%|
|11,25 - 33,75|NNE|4,2%|0,8%|0,2%|0,0%|0,0%|0,0%|5,2%|
|33,75 - 56,25|NE|4,6%|0,2%|0,0%|0,0%|0,0%|0,0%|4,8%|
|56,25 - 78,75|ENE|5,4%|0,3%|0,0%|0,0%|0,0%|0,0%|5,7%|
|78,75 - 101,25|E|4,1%|0,4%|0,1%|0,0%|0,0%|0,0%|4,5%|
|101,25 - 123,75|ESE|1,8%|0,3%|0,2%|0,1%|0,0%|0,0%|2,3%|
|123,75 - 146,25|SE|1,1%|0,2%|0,1%|0,0%|0,0%|0,0%|1,4%|
|146,25 - 168,75|SSE|0,9%|0,3%|0,0%|0,0%|0,0%|0,0%|1,3%|
|168,75 - 191,25|S|1,0%|0,8%|0,4%|0,5%|0,0%|0,0%|2,8%|
|191,25 - 213,75|SSW|1,4%|1,8%|3,3%|3,0%|0,1%|0,0%|9,6%|
|213,75 - 236,25|SW|0,8%|1,6%|4,5%|3,7%|0,3%|0,0%|10,9%|
|236,25 - 258,75|WSW|1,0%|1,7%|5,1%|0,4%|0,0%|0,0%|8,2%|
|258,75 - 281,25|W|3,1%|1,7%|0,7%|0,0%|0,0%|0,0%|5,5%|
|281,25 - 303,75|WNW|6,6%|1,3%|0,5%|0,1%|0,0%|0,0%|8,4%|
|303,75 - 326,25|NW|7,0%|1,3%|0,9%|0,1%|0,0%|0,0%|9,3%|
|326,25 - 348,75|NNW|4,6%|0,9%|1,3%|0,3%|0,0%|0,0%|7,1%|
|Sub-Total|Sub-Total|51,3%|14,8%|17,8%|8,4%|0,5%|0,1%|92,8%|
|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|7,2%|

Fuente: Elaboración Propia en base a los resultados del modelo WRF.

www.dfmconsultores.cl

60
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Ciclos Diarios

En la Figura 5-33 se presenta el ciclo diario para la variable velocidad del viento modelada, en donde

se puede observar que las menores velocidades ocurren durante el periodo nocturno, de

madrugada y primeras horas de la mañana, específicamente entre las 23:00 y 08:00 horas, en donde

se alcanza un mínimo promedio de velocidad de viento de aproximadamente 1,2 m/s a las 07:00

horas. Luego, la velocidad comienza a incrementar sostenidamente alcanzando las mayores

intensidades de viento entre las 13:00 y 16:00 horas, aproximadamente, adoptando valores

máximos promedios de aproximadamente 5,5 m/s a las 15:00 horas. Posteriormente, la velocidad

desciende hasta alcanzar los valores nocturnos, iniciando nuevamente el ciclo. Cabe mencionar que

el rango de oscilación del 90% de los datos posee una diferencia de 5,8 m/s al momento de máxima

velocidad y de 1,9 m/s al momento de mínima velocidad.

**Figura 5-33. Ciclo Diario Velocidad del Viento Modelada. Enero a diciembre de 2020. Estación Casablanca.**

Fuente: Elaboración Propia en base a los resultados del modelo WRF.

www.dfmconsultores.cl

61
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Por otro lado, en la Figura 5-34 se presenta el ciclo diario de dirección del viento modelado. En ella

se puede observar que, durante la noche y madrugada, específicamente entre las 18:00 y 07:00

horas, los vientos presentan dirección este noreste (ENE), alcanzando máxima frecuencia a las 01:00

horas. Por el contrario, durante la mañana, específicamente entre las 07:00 y las 11:00 horas, los

vientos presentan direcciones oeste noroeste (ONO) y sur suroeste (SSO), alcanzando la frecuencia

más alta a las 11:00 horas. Por último, durante la tarde, específicamente entre las 12:00 y las 19:00

horas, los vientos presentan dirección suroeste (SO), principalmente, alcanzando máxima frecuencia

entre las 16:00 y las 17:00 horas.

**Figura 5-34. Ciclo Diario Dirección del Viento Modelada. Enero a diciembre de 2020. Estación Casablanca.**

Fuente: Elaboración Propia en base a los resultados del modelo WRF.

www.dfmconsultores.cl

62
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Ciclo Estacional

En la Figura 5-35 se presenta el ciclo estacional de vientos modelados, en donde es posible apreciar

que las mayores intensidades de viento se producen en los meses de diciembre y principios de enero

durante la tarde, específicamente entre las 14:00 y las 16:00 horas; mientras que las menores

intensidades se presentan durante dos periodos: el periodo nocturno, entre las 21:00 y las 00:00

para los meses de octubre y noviembre, así como también entre enero y abril; y el periodo de

madrugada y primeras horas de la mañana, es decir, entre las 01:00 y 09:00 horas, para los meses

desde agosto a mayo.

Por otro lado, en cuanto a la dirección del viento, durante todo el año es posible observar una

marcada predominancia de vientos norte (N) y nornoreste (NNE), específicamente durante el

periodo nocturno, de madrugada y primeras horas de la mañana, entre las 21:00 y las 08:00 horas.

Por su parte, entre las 09:00 y las 19:00 horas, se observa predominancia de vientos con dirección

suroeste (SO), durante prácticamente todo el año.

www.dfmconsultores.cl

63
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-35. Ciclo Estacional de Velocidad y Dirección del Viento Modelado. Año 2020. Estación**

**Casablanca.**

Fuente: Elaboración Propia en base a los resultados del modelo WRF.

www.dfmconsultores.cl

64
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

b) Temperatura

A continuación, en la Tabla 5-15 se muestra el resumen de información para la variable temperatura

modelada, especificando promedio, máximo y mínimo anual para el año en estudio.

De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”,

las series de datos meteorológicos deben contar con un 75% de datos válidos, lo cual se cumple para

el año 2020 debido a que se cuenta con la completitud de los datos a partir del modelo WRF.

**Tabla 5-15. Resumen de información Temperatura Modelada. Estación Casablanca.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2020**|
|Temperatura (°C)|Promedio|15,52|
|Temperatura (°C)|Mínimo|2,78|
|Temperatura (°C)|Máximo|33,49|
|Temperatura (°C)|Datos Válidos (%)|100%|

Fuente: Elaboración Propia en base a los resultados del modelo WRF.

A continuación, en los siguientes apartados se presenta la serie de tiempo, ciclo diario y ciclo

estacional modelados para la variable meteorológica temperatura.

www.dfmconsultores.cl

65
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Serie de Tiempo

A modo de verificación de la completitud de los datos, en la Figura 5-36 se presenta la serie de

tiempo para la variable temperatura modelada, en donde es posible observar que se cuenta con el

100% de los registros para dicha variable en concordancia con el uso de los registros entregados por

el modelo meteorológico WRF.

Por otro lado, se puede identificar que las temperaturas registradas se encuentran principalmente

entre los 5 y 30°C aproximadamente, con excepciones durante los meses de julio a octubre, en

donde se observan temperaturas inferiores a los 5°C, y durante los meses entre enero y mediados

de mayo, aproximadamente, donde se observan temperaturas superiores a los 30°C.

**Figura 5-36. Serie de Tiempo Temperatura Modelada. Enero a diciembre de 2020. Estación Casablanca.**

Fuente: Elaboración Propia en base a los resultados del modelo WRF.

www.dfmconsultores.cl

66
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Ciclo Diario

En la Figura 5-37 se expone el ciclo diario para la variable temperatura modelada, en donde es

posible observar que las menores temperaturas ocurren durante el periodo nocturno, de

madrugada y primeras horas de la mañana, específicamente entre las 22:00 y 07:00 horas,

alcanzando un mínimo promedio de temperatura de aproximadamente 12°C a las 06:00 horas.

Luego, la temperatura comienza a aumentar paulatinamente hasta alcanzar un máximo promedio

aproximado de 21°C a las 13:00 horas, para luego comenzar a disminuir de manera gradual hasta

alcanzar los valores de temperatura nocturnas, por bajo los 15 °C, para luego dar comienzo

nuevamente al ciclo. Cabe mencionar que el rango de oscilación del 90% de los datos posee una

diferencia de 10°C al momento de máxima temperatura y de 11°C, aproximadamente, al momento

de mínima temperatura.

**Figura 5-37. Ciclo Diario Temperatura Modelada. Enero a diciembre de 2020. Estación Casablanca.**

Fuente: Elaboración Propia en base a los resultados del modelo WRF.

www.dfmconsultores.cl

67
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Ciclo Estacional

En la Figura 5-38 se presenta el ciclo estacional de la temperatura modelada, en donde es posible

notar que las mayores temperaturas se registran durante los meses de verano, específicamente

entre diciembre y marzo, en el periodo diurno, alcanzando valores sobrepasan levemente los 25°C,

aproximadamente, entre las 11:00 y 15:00 horas. Por otro lado, las menores temperaturas se

registran durante los meses entre julio y octubre, en donde se presentan temperaturas mínimas

promedio aproximadas de 9°C entre las 21:00 y 09:00 horas.

**Figura 5-38. Ciclo Estacional Temperatura Modelada. Enero a diciembre de 2020. Estación Casablanca.**

Fuente: Elaboración Propia en base a los resultados del modelo WRF.

www.dfmconsultores.cl

68
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.6.3 Meteorología de Altura - Valores Observados

Con respecto a la meteorología de altura, no existen registros de mediciones disponibles en las

estaciones utilizadas que puedan ser incorporadas en este estudio.

5.6.4 Meteorología de Altura - Valores Modelados

5.6.4.1 _Estación Meteorológica Casablanca_

a) Altura Capa de Mezcla

La altura de capa de mezcla es un parámetro obtenido tras el procesamiento de los resultados del

modelo meteorológico WRF, el cual representa la altura medida desde la superficie en donde la

inestabilidad favorece la dispersión vertical de contaminantes.

A continuación, se presenta la caracterización de la variable meteorológica altura de capa de mezcla,

considerado los datos entregados por el modelo meteorológico WRF correspondiente al año 2020

para el sector cercano al Proyecto, específicamente en la localización de la estación Casablanca,

identificando los valores promedio, máximo y mínimo para esta variable, tal como se muestra en la

Tabla 5-16.

**Tabla 5-16. Resumen de Información Altura de Capa de Mezcla Modelada. Estación Casablanca.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2020**|
|Altura Capa de Mezcla (m)|Promedio|261,35|
|Altura Capa de Mezcla (m)|Mínimo|10,00|
|Altura Capa de Mezcla (m)|Máximo|1.840,15|
|Altura Capa de Mezcla (m)|% Datos Válidos|100%|

Fuente: Elaboración Propia en base a los resultados del modelo WRF.

A continuación, se presenta la serie de tiempo, ciclo diario y ciclo estacional modelados para la

variable meteorológica altura de capa de mezcla.

www.dfmconsultores.cl

69
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Serie de Tiempo

En la Figura 5-39 se presenta la serie de tiempo para la variable altura de capa de mezcla modelada,

en donde es posible observar una completitud de los datos, esto ya que el parámetro ha sido

calculado conforme a los resultados del modelo meteorológico WRF. En ella se puede identificar

que, los valores modelados se concentran mayormente entre los 0 y 1.200 metros, durante todos

los meses del año. No obstante, existen valores que sobrepasan los 1.800 metros de altura de capa

de mezcla, lo cual ocurre particularmente durante el mes de abril.

**Figura 5-39. Serie de tiempo para Altura de Capa de Mezcla Modelada. Enero a diciembre de 2020.**

**Estación Casablanca.**

Fuente: Elaboración Propia en base a los resultados del modelo WRF.

www.dfmconsultores.cl

70
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Ciclo Diario

En la Figura 5-40 se presenta el ciclo diario para la variable altura de capa de mezcla modelada, en

donde se puede observar que los menores valores se presentan durante el periodo nocturno y de

madrugada, presentándose una estabilidad a los 50 metros aproximadamente. A partir de las 06:00

horas, los valores incrementan de manera sostenida, conforme a la incidencia de la radiación solar,

alcanzando un valor máximo promedio aproximado de 750 metros a las 13:00 horas. Posterior a

ello, la altura de la capa de mezcla comienza a disminuir en magnitud hasta alcanzar los valores

nocturnos, dando inicio nuevamente al ciclo. Cabe mencionar que, el rango de oscilación del 90%

de los datos de esta variable es de aproximadamente 900 metros al momento de máxima altura.

**Figura 5-40. Ciclo Diario Altura de Capa de Mezcla Modelada. Enero a diciembre de 2020. Estación**

**Casablanca.**

Fuente: Elaboración Propia en base a los resultados del modelo WRF.

www.dfmconsultores.cl

71
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Ciclo Estacional

En la Figura 5-41 se presenta el ciclo estacional de la altura de capa de mezcla modelada, en donde

es posible notar que las mayores alturas se registran durante los meses de septiembre y abril, en

donde se registran alturas de capa de mezcla que sobrepasan los 800 metros, específicamente entre

las 11:00 y las 14:00 horas. Por el contrario, las menores alturas se presentan a lo largo del periodo

anual, entre las 20:00 y 09:00 horas, registrando valores cercanos a los 0 metros de altura.

**Figura 5-41. Ciclo Estacional Altura Capa de Mezcla Modelada. Enero a diciembre de 2020. Estación**

**Casablanca.**

Fuente: Elaboración Propia en base a los resultados del modelo WRF.

www.dfmconsultores.cl

72
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

###### 5.7 Análisis de Incertidumbre

En las siguientes secciones se presentan la comparación cuantitativa y cualitativa entre los

resultados del modelo meteorológico y los datos observados, con el fin de determinar la

incertidumbre entre ambos. El análisis se presenta para el año 2020 en la misma ubicación de

comparación, correspondiente a la estación de monitoreo Casablanca.

Es necesario señalar que, para el análisis de la comparación cuantitativa entre los valores modelados

y observados, se consideran tres estadígrafos que comúnmente se utilizan para la evaluación del

_performance_ de modelos: Sesgo, snacks Cuadrático Medio (ECM) y el coeficiente de correlación (r),

los cuales fueron calculados para las series de tiempo y los ciclos diarios de las variables velocidad

de viento y temperatura. De esta manera, para realizar dicho análisis se realiza una comparativa con
los valores recomendados en la Guía para el uso de Modelos de Calidad del Aire en el SEIA [(5)], los

cuales se presentan en la Tabla 5-17.

**Tabla 5-17. Métricas estadísticas recomendables en el Análisis de Incertidumbre para las variables**

**meteorológicas medias.**

|Estadístico o Medida de Error|Velocidad Viento|Temperatura|
|---|---|---|
|Sesgo|[-2,5; 2,5] m/s|[-4,0; 4,0] °C|
|Error cuadrático medio (ECM)|≤ 3,5 m/s|≤ 4,5 °C|
|r|> 0,6|> 0,8|

Fuente: Guía para el uso de Modelos de Calidad del Aire en el SEIA [(5)] .

5 Guía para el uso de Modelos de Calidad del Aire en el SEIA, SEA, 2023. Link web:
[https://sea.gob.cl/sites/default/files/imce/archivos/2023/02.FEB/28/Guia-Calidad-del-aire_V.4-final.pdf](https://sea.gob.cl/sites/default/files/imce/archivos/2023/02.FEB/28/Guia-Calidad-del-aire_V.4-final.pdf)

www.dfmconsultores.cl

73
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.7.1 Estación Casablanca

5.7.1.1 _Comparación Cuantitativa_

A continuación, en la siguiente tabla, se presentan los estadígrafos: Sesgo, Error Cuadrático Medio

(ECM) y el coeficiente de correlación (r) obtenidos para los datos de la estación Casablanca.

**Tabla 5-18. Estadígrafos de Dispersión para Velocidad del Viento y Temperatura. Estación Casablanca.**

|Medida de Error|Estación Casablanca|Col3|Col4|Col5|
|---|---|---|---|---|
|**Medida de Error**|**Velocidad Viento**|**Velocidad Viento**|**Temperatura**|**Temperatura**|
|**Medida de Error**|**Serie de Tiempo**|**Ciclo Diario**|**Serie de Tiempo**|**Ciclo Diario**|
|Sesgo|0,68|0,69|1,28|1,29|
|ECM|1,46|0,85|4,19|2,26|
|r|0,77|0,99|0,80|0,98|

Fuente: Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

A partir de la tabla anterior, con respecto a la variable de velocidad de viento, se aprecia que los

coeficientes de correlación son altos, de 77% y 99% para la serie de tiempo y ciclo diario,

respectivamente, los cuales son superiores al valor establecido en la Guía para el uso de Modelos

de Calidad del Aire en el SEIA, según lo presentado en la Tabla 5-17. Por su parte, el error cuadrático

medio es de 1,46 y 0,85 m/s para la serie de tiempo y ciclo diario, respectivamente, los cuales se

encuentran dentro del rango recomendado por la Guía. Por último, los valores de sesgo son iguales

a 0,68 y 0,69 m/s para la serie de tiempo y ciclo diario, los cuales también se encuentran del rango

recomendado, según la Tabla 5-17.

Por otro lado, con respecto a la temperatura, se observa que los coeficientes de correlación son

altos, de 80% y 98%, para la serie de tiempo y ciclo diario, respectivamente, los cuales son

notoriamente mayores al valor mínimo establecido en la Guía para el uso de Modelos de Calidad

del Aire en el SEIA (Tabla 5-17). Luego, los valores de error cuadrático medio también se encuentran

dentro del rango establecido por la Guía, dado que, tanto para la serie de tiempo como para el ciclo

diario, se obtienen valores inferiores a 4,5 °C. Por último, se observa que los valores de sesgo de

serie de tiempo y ciclo diario, iguales a 1,28°C y 1,29°C, respectivamente, cumplen con el rango

recomendado en la Guía.

Finalmente, dadas las medidas de dispersión presentadas, se establece en forma cuantitativa que

el modelo tiende a sobrestimar levemente la velocidad del viento y la temperatura, no obstante,

logra representar de manera correcta los valores medidos, sin diferencias significativas.

www.dfmconsultores.cl

74
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.7.1.2 _Comparación Cualitativa_

Debido a que la meteorología de superficie es un factor relevante en la dispersión de los

contaminantes, en el presente inciso se busca validar en forma cualitativa el modelo WRF que será

utilizado como información base de entrada al modelo de dispersión CALPUFF.

Para llevar a cabo lo anterior, se presenta una comparación de los datos observados en la estación

Casablanca para el periodo comprendido entre el enero y diciembre del año 2020, mismo periodo

para el que se realizó el modelo meteorológico WRF. Así, se comparan ciclos diarios y estacionales

para las variables meteorológicas velocidad del viento, dirección del viento y temperatura.

5.7.1.3 _Velocidad y Dirección del Viento_

a) Ciclo Diario

En la Figura 5-42 se observa la comparativa de los ciclos diarios de velocidad del viento para el

período en estudio, para la estación de monitoreo Casablanca. En ésta se observa un buen acuerdo

en términos de la fase entre ambos ciclos, observándose una cercanía en las horas en que se

presentan los mínimos y máximos, sin embargo, el modelo tiende a sobrestimar levemente la

magnitud del viento durante todo el día, tanto para las velocidades máximas como las mínimas

registradas.

Por su parte, en la Figura 5-43 se observa la comparativa de los ciclos diarios, o histogramas, de

dirección del viento para el período en estudio, para la estación de monitoreo Casablanca. En ésta

se puede apreciar que, si bien las frecuencias de viento están levemente sobrestimadas por el

modelo, se logra predecir la dirección de viento predominante, lo cual se aprecia notoriamente

durante la tarde. Tal como se puede apreciar, para el período diurno, se observan, principalmente,

vientos noroeste (NO) y nornoroeste (NNO), donde se puede apreciar que el modelo representa

adecuadamente los registros observados. Por su parte, durante la tarde y noche se observan vientos

en direcciones suroeste (SO) y oeste suroeste (OSO), donde existen pequeñas diferencias con los

valores modelados, además de que el modelo tiende a sobrestimar levemente las frecuencias de

viento.

www.dfmconsultores.cl

75
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-42. Comparación del Ciclo Diario de la Velocidad del Viento. Estación Casablanca.**

|Observado|Modelado|
|---|---|
|||

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)] “Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

76
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-43. Comparación de Histogramas de Dirección. Estación Casablanca.**

|Observado|Modelado|
|---|---|
|||

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)] “Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

77
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

b) Ciclo Estacional

A continuación, en la Figura 5-44 se presenta el ciclo estacional de velocidad y dirección de viento

para el periodo de estudio, en la estación de monitoreo Casablanca. En cuanto a la dirección de

viento en ésta se logra apreciar que, para el periodo de madrugada y durante las primeras horas de

la mañana, el modelo tiende a representar la tendencia de los datos observados; no obstante, para

el resto del día, lo modelado presenta ciertas diferencias respecto a lo observado. Por su parte, se

aprecia que el modelo tiende a sobrestimar la intensidad de viento durante todo el periodo en

estudio, lo cual se puede apreciar más notoriamente en los meses de verano, los cuales

corresponden al periodo de mayor velocidad de viento.

www.dfmconsultores.cl

78
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-44. Comparación de Ciclo Estacional de Velocidad y Dirección del Viento. Estación Casablanca.**

|Observado|Modelado|
|---|---|
|||

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)] “Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

79
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.7.1.4 _Temperatura_

a) Ciclo Diario

En la Figura 5-45 se presenta la comparativa de los ciclos diarios de temperatura atmosférica para

el período en estudio, para la estación de monitoreo Casablanca. En ella se observa un muy buen

acuerdo en términos de la fase entre ambos ciclos, pues tanto las horas de mínimos como de

máximos son coincidentes; no obstante, se observan leves diferencias en términos de amplitud de

ambos ciclos. Adicionalmente, se observa que el modelo subestima levemente las temperaturas

máximas diarias, mientras que las temperaturas mínimas diarias las tiende a sobrestimar.

www.dfmconsultores.cl

80
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-45. Comparación del Ciclo Diario de la Temperatura. Estación Casablanca.**

|Observado|Modelado|
|---|---|
|||

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)] “Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

81
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

b) Ciclo Estacional

En la Figura 5-46 se presenta la comparativa del ciclo estacional de temperaturas observadas y

modeladas para el período en estudio, para la estación de monitoreo Casablanca. En ella se puede

distinguir que el modelo representa la fase de cada ciclo, tanto diario como anual, con sus

respectivos mínimos y máximos. Sin embargo, se observa que el modelo tiende a sobrestimar los

valores mínimos de temperatura, lo cual se aprecia en los meses de invierno-primavera, en periodo

nocturno, de madrugada y durante las primeras horas de la mañana, principalmente.

Adicionalmente, con respecto a las temperaturas máximas, el modelo tiende a subestimarlas

levemente, lo cual se observa durante los meses de verano, en horas de la tarde, principalmente.

www.dfmconsultores.cl

82
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-46. Comparación del Ciclo Estacional de Temperatura. Estación Casablanca.**

|Observado|Modelado|
|---|---|
|||

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)] “Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

83
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

###### 5.8 Normas de Calidad del Aire

En la Tabla 5-19 se presenta la normativa de calidad del aire de los contaminantes de interés para

el Proyecto, los cuales corresponden a: material particulado respirable fino (MP2.5), material

particulado respirable (MP10), dióxido de nitrógeno (NO 2 ), monóxido de carbono (CO) y dióxido de

azufre (SO 2 ) en su norma primaria de calidad del aire.

**Tabla 5-19. Normas primarias de calidad del aire.**

|Contaminante|Decreto Aplicable|Norma|Col4|Periodo de Evaluación de Cumplimiento de<br>Norma|
|---|---|---|---|---|
|**Contaminante**|**Decreto Aplicable**|**Valor**|**Unidad**|**Unidad**|
|Material Particulado<br>Respirable Fino (MP2.5)|Decreto Supremo<br>N°12/2011|50|μg/m3|Percentil 98 de las concentraciones de 24<br>horas|
|Material Particulado<br>Respirable Fino (MP2.5)|Decreto Supremo<br>N°12/2011|20|20|Concentración anual|
|Material Particulado<br>Respirable (MP10)|Decreto Supremo<br>N°12/2022|130|μg/m3N|Percentil 98 de las concentraciones de 24<br>horas|
|Material Particulado<br>Respirable (MP10)|Decreto Supremo<br>N°12/2022|50|50|Concentración anual|
|Monóxido de Carbono<br>(CO)|Decreto Supremo<br>N°115/2002|30|mg/m3N|Percentil 99 de los máximos diarios de<br>concentración de 1 hora|
|Monóxido de Carbono<br>(CO)|Decreto Supremo<br>N°115/2002|10|10|Percentil 99 de los máximos diarios de<br>concentración de 8 horas|
|Dióxido de Nitrógeno<br>(NO2)|Decreto Supremo<br>N°114/2002|400|μg/m3N|Percentil 99 de los máximos diarios de<br>concentración de 1 hora|
|Dióxido de Nitrógeno<br>(NO2)|Decreto Supremo<br>N°114/2002|100|100|Concentración anual|
|Dióxido de Azufre (SO2) <br>(Norma primaria de<br>calidad del aire)|Decreto Supremo<br>N°104/2019|350|μg/m3N|Percentil 99 de las concentraciones de 1 hora.|
|Dióxido de Azufre (SO2) <br>(Norma primaria de<br>calidad del aire)|Decreto Supremo<br>N°104/2019|150|150|Percentil 99 de las concentraciones de 24<br>horas|
|Dióxido de Azufre (SO2) <br>(Norma primaria de<br>calidad del aire)|Decreto Supremo<br>N°104/2019|60|60|Concentración anual|

Fuente: Elaboración Propia.

De forma complementaria, se presenta en la Tabla 5-20 la normativa de calidad del aire secundaria

de los contaminantes de interés para el Proyecto, los cuales corresponden a: material particulado

sedimentable (MPS) y dióxido de azufre (SO 2 ).

**Tabla 5-20. Normas secundarias de calidad del aire.**

|Contaminante|Decreto Aplicable|Norma|Col4|Periodo de Evaluación de Cumplimiento de<br>Norma|
|---|---|---|---|---|
|**Contaminante**|**Decreto Aplicable**|**Valor**|**Unidad**|**Unidad**|
|Material Particulado<br>Sedimentable (MPS)|Confederación Suiza,<br>Recursos Naturales|200|mg/m2-día|Media aritmética anual|
|Material Particulado<br>Sedimentable (MPS)|República de Argentina|333|mg/m2-día|Media aritmética mensual|
|Dióxido de Azufre (SO2) <br>(Norma secundaria de<br>calidad del aire)|Decreto Supremo<br>N°22/2010|700|μg/m3N|Percentil 99,73 de las concentraciones de 1<br>hora. Zona Sur.|
|Dióxido de Azufre (SO2) <br>(Norma secundaria de<br>calidad del aire)|Decreto Supremo<br>N°22/2010|260|260|Percentil 99,7 de las concentraciones de 24<br>horas. Zona Sur.|
|Dióxido de Azufre (SO2) <br>(Norma secundaria de<br>calidad del aire)|Decreto Supremo<br>N°22/2010|60|60|Concentración anual. Zona Sur.|

Fuente: Elaboración Propia.

Para el caso del material particulado sedimentable, ante la ausencia de una norma de calidad

nacional aplicable para la zona del Proyecto, se evaluará el cumplimiento de los valores obtenidos

www.dfmconsultores.cl

84
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

a través de la utilización de una norma de referencia, de acuerdo con lo establecido en el Artículo

11 del Reglamento de Evaluación Ambiental (RSEIA). En consecuencia, se considerará la norma de

referencia de la Confederación Suiza y de la República de Argentina para el análisis de este

contaminante.

###### 5.9 Línea Base de Calidad del Aire

A continuación, se describe la línea base de calidad del aire para el presente Proyecto en evaluación.

Para evitar sesgos estacionales, para la descripción del área de influencia se debe considerar un

periodo de registro de un año de mediciones, con una proporción de datos válidos igual o mayor al

75% en el caso de mediciones continuas, de acuerdo con los lineamientos establecidos en la Guía
para la descripción del Área de Influencia, Calidad del Aire en el Área de Influencia de proyectos que

ingresan al SEIA.

Previo al análisis de los datos de calidad del aire, se considera la revisión de la completitud de éstos.

En los siguientes apartados se presentan los periodos de datos, junto con la completitud de éstos,

para la estación de monitoreo de calidad del aire considerada.

5.9.1 Estaciones de monitoreo

La estación de monitoreo que se encuentra más cercana a la localización del proyecto, y con la que

se cuenta con información disponible, corresponde a la estación Casablanca, de propiedad de la

empresa TRESMONTES S.A., cuyos principales resultados fueron recuperados desde “Anexo 03.2

Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al

SEIA [(1)] “Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

A modo de complemento, en la Tabla 5-21, se presenta el detalle de los equipos utilizados y los

principios de operación para medir los parámetros registrados para la estación de monitoreo

indicada en el párrafo anterior.

**Tabla 5-21. Inventario de Equipos y Técnicas de Medición.**

|Nombre<br>Estación|Parámetro|Unidad|Equipo - Serie|Principio de Operación|
|---|---|---|---|---|
|Casablanca|Material Particulado<br>Respirable (MP10)|μg/m3N|Tisch Enviromental -<br>P3829X|Gravimetría de Alto<br>Volumen (Hi Vol)|
|Casablanca|Monóxido de Carbono (CO)|ppm|Teledyne 300E - 1308|IRND con Filtro gaseoso de<br>correlación|
|Casablanca|Dióxido de Nitrógeno (NO2)|ppb|Teledyne T200 - 155|Luminescencia Química|
|Casablanca|Dióxido de Azufre (SO2)|ppb|Teledyne 100E - 266|Fluorescencia de pulso UV|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

85
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

A continuación, en la Tabla 5-22 se presentan las coordenadas geográficas y periodo de datos de

medición considerados para la estación de monitoreo mencionada, utilizados para la elaboración

de la Línea de Base de Calidad del Aire del proyecto.

**Tabla 5-22. Caracterización de Estación de Monitoreo de Calidad del Aire.**

|Nombre|Parámetros de Calidad del Aire<br>Registrados|Periodo monitoreado<br>considerado para este<br>estudio|Coordenadas (Datum<br>WGS84)|Col5|
|---|---|---|---|---|
|**Nombre**|**Parámetros de Calidad del Aire**<br>**Registrados**|**Periodo monitoreado**<br>**considerado para este**<br>**estudio**|**Este (m)**|**Norte (m)**|
|Casablanca|Material Particulado Respirable<br>(MP10)|Enero 2020 a Diciembre<br>2022|278.002|6.309.012|
|Casablanca|Monóxido de Carbono (CO)|Monóxido de Carbono (CO)|Monóxido de Carbono (CO)|Monóxido de Carbono (CO)|
|Casablanca|Dióxido de Nitrógeno (NO2)|Dióxido de Nitrógeno (NO2)|Dióxido de Nitrógeno (NO2)|Dióxido de Nitrógeno (NO2)|
|Casablanca|Dióxido de Azufre (SO2)|Dióxido de Azufre (SO2)|Dióxido de Azufre (SO2)|Dióxido de Azufre (SO2)|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

Asimismo, en la Figura 5-47 se muestra la ubicación de la estación de monitoreo con respecto a la

zona de emplazamiento del Proyecto.

www.dfmconsultores.cl

86
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-47. Ubicación Referencial Estación de Monitoreo de Calidad del Aire.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

87
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.9.1.1 _Estación Casablanca_

a) Material Particulado Respirable (MP10)

Resultados Monitoreo

En la Tabla 5-23 se presentan los resultados del monitoreo de material particulado respirable

(MP10) en la Estación Casablanca durante el periodo comprendido entre el 01 de enero de 2020 al

31 de diciembre de 2022.

**Tabla 5-23. Resultados Monitoreo de MP10. Estación Casablanca** **[(6)]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2020**|**2021**|**2022**|
|MP10 (μg/m3N)|Percentil 98 diario|74|80|86|
|MP10 (μg/m3N)|Media anual|34|32|30|
|MP10 (μg/m3N)|Media trianual|32|32|32|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

Comparación con Normativa

En la Tabla 5-24 se exhibe la comparación de los resultados del monitoreo de material particulado

respirable (MP10) en la Estación Casablanca con la normativa primaria de calidad del aire durante

el periodo en estudio.

**Tabla 5-24. Comparación de Monitoreo de MP10 con Normativa. Estación Casablanca.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|MP10|1 de enero de 2022 - 31<br>diciembre 2022|Percentil 98 de la<br>concentración media diaria|86|130|μg/m3N|66,2%|
|MP10|1 de enero de 2020 - 31<br>diciembre 2022|Concentración media trianual|32|50|μg/m3N|64,0%|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

De la tabla anterior, es posible establecer de manera cuantitativa que la estación de monitoreo

Casablanca ha registrado concentraciones de MP10 por bajo los límites normativos, tanto para el

periodo diario como anual, del periodo en estudio.

6 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado en los Informes de Monitoreo, por el titular propietario de la estación.

www.dfmconsultores.cl

88
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

b) Monóxido de Carbono (CO)

Resultados Monitoreo

En la Tabla 5-25 se presentan los resultados del monitoreo de dióxido de carbono (CO) en la Estación

Casablanca durante el periodo comprendido entre el 01 de enero de 2020 al 31 de diciembre de

2022.

**Tabla 5-25. Resultados Monitoreo de CO. Estación Casablanca** **[(7)]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2020**|**2021**|**2022**|
|CO (mg/m3N)|Percentil 99 de los máximos diarios de<br>concentración horaria|1,3|1,3|1,2|
|CO (mg/m3N)|Promedio trianual percentil 99 de los máximos<br>diarios de concentración horaria|1,3|1,3|1,3|
|CO (mg/m3N)|Percentil 99 de los máximos diarios de<br>concentración de 8 horas|0,8|1,0|0,8|
|CO (mg/m3N)|Promedio trianual percentil 99 de los máximos<br>diarios de concentración de 8 horas|0,9|0,9|0,9|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

Comparación con Normativa

En la Tabla 5-26 se exhibe la comparación de los resultados del monitoreo de dióxido de carbono

(CO) en la Estación Casablanca con la normativa primaria de calidad del aire durante el periodo en

estudio.

**Tabla 5-26. Comparación de Monitoreo de CO con Normativa. Estación Casablanca.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|CO|1 de enero de 2020 -<br>31 diciembre 2022|Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora|1,3|30|mg/m3N|4,4%|
|CO|1 de enero de 2020 -<br>31 diciembre 2022|Percentil 99 de los<br>máximos diarios de<br>concentración de 8 horas|0,9|10|mg/m3N|8,9%|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

De la tabla anterior, es posible establecer, de manera cuantitativa, que la estación de monitoreo

Casablanca ha registrado concentraciones de CO bajo las normas de percentil 99 para periodo de 1

hora y 8 horas.

7 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado en los Informes de Monitoreo, por el titular propietario de la estación.

www.dfmconsultores.cl

89
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

c) Dióxido de Nitrógeno (NO 2 )

Resultados Monitoreo

En la Tabla 5-27 se presentan los resultados del monitoreo de dióxido de nitrógeno (NO 2 ) en la

Estación Casablanca durante el periodo comprendido entre el 01 de enero de 2020 al 31 de

diciembre de 2022.

**Tabla 5-27. Resultados Monitoreo de NO** **2** **. Estación Casablanca.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2020**|**2021**|**2022**|
|NO2 (μg/m3N)|Percentil 99 de los máximos diarios de concentración<br>horaria|45,1|60,1|50,7|
|NO2 (μg/m3N)|Promedio trianual percentil 99 de los máximos diarios de<br>concentración horaria|52,6|52,6|52,6|
|NO2 (μg/m3N)|Media anual|9,4|11,3|11,3|
|NO2 (μg/m3N)|Media trianual|11,3|11,3|11,3|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

Comparación con Normativa

En la Tabla 5-28 se exhibe la comparación de los resultados del monitoreo de dióxido de nitrógeno

(NO 2 ) en la Estación Casablanca con la normativa primaria de calidad del aire durante el periodo en

estudio.

**Tabla 5-28. Comparación de Monitoreo de NO** **2** **con Normativa. Estación Casablanca.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de la<br>Norma|
|---|---|---|---|---|---|---|
|NO2|1 de enero de 2020 - 31<br>diciembre 2022|Percentil 99 de los máximos<br>diarios de concentración de<br>1 hora|52,6|400|μg/m3N|13,1%|
|NO2|1 de enero de 2020 - 31<br>diciembre 2022|Concentración media<br>trianual|11,3|100|μg/m3N|11,3%|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

De la tabla anterior, es posible establecer, de manera cuantitativa, que la estación de monitoreo

Casablanca ha registrado concentraciones de NO 2 bajo la norma de percentil 99 de 1 hora, como

también bajo la norma de periodo anual, para el periodo en estudio.

www.dfmconsultores.cl

90
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

d) Dióxido de Azufre (SO 2 )

Resultados Monitoreo

En la Tabla 5-29 se presentan los resultados del monitoreo de dióxido de azufre (SO 2 ) en la Estación

Casablanca durante el periodo comprendido entre el 01 de enero de 2020 al 31 de diciembre de

2022.

**Tabla 5-29. Resultados Monitoreo de SO** **2** **. Estación Casablanca** **[(8)]** **.**

|Contaminante|Parámetro|Año|Col4|Col5|
|---|---|---|---|---|
|**Contaminante**|**Parámetro**|**2020**|**2021**|**2022**|
|SO2 (μg/m3N)|Percentil 99 de concentración horaria|15,6|18,2|5,2|
|SO2 (μg/m3N)|Promedio trianual percentil 99 de concentración horaria|13,0|13,0|13,0|
|SO2 (μg/m3N)|Percentil 99 de concentración diaria|2,6|2,6|2,6|
|SO2 (μg/m3N)|Promedio trianual percentil 99 de concentración diaria|2,6|2,6|2,6|
|SO2 (μg/m3N)|Media anual|0,0|2,6|2,6|
|SO2 (μg/m3N)|Media trianual|1,3|1,3|1,3|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

Comparación con Normativa

En la Tabla 5-30 se exhibe la comparación de los resultados del monitoreo de dióxido de azufre (SO 2 )

en la Estación Casablanca con la normativa primaria de calidad del aire durante el periodo en

estudio.

**Tabla 5-30. Comparación de Monitoreo de SO** **2** **con Normativa. Estación Casablanca.**

|Contaminante|Periodo|Estadígrafo|Valor|Norma|Unidad|Porcentaje de<br>la Norma|
|---|---|---|---|---|---|---|
|SO2|1 de enero de 2020 - 31<br>diciembre 2022|Percentil 99 de concentración<br>horaria|13,0|350|μg/m3N|3,7%|
|SO2|1 de enero de 2020 - 31<br>diciembre 2022|Percentil 99 de la concentración<br>media diaria|2,6|150|μg/m3N|1,7%|
|SO2|1 de enero de 2020 - 31<br>diciembre 2022|Concentración media trianual|1,3|60|μg/m3N|2,2%|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

De la tabla anterior, es posible establecer de manera cuantitativa que la estación de monitoreo

Casablanca ha registrado concentraciones de SO 2 bajo los límites normativos establecidos para: el

percentil 99 de 1 hora, el percentil 99 de 24 horas, y también el periodo anual.

8 Ante la no disponibilidad de datos para este contaminante en esta estación, se presenta el resumen de
resultados del monitoreo presentado en los Informes de Monitoreo, por el titular propietario de la estación.

www.dfmconsultores.cl

91
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.9.2 Resumen Línea de Base de Calidad de Aire

A continuación, en la Tabla 5-31 se presenta el resumen de la línea de base de calidad del aire de la

estación de monitoreo Casablanca para el periodo comprendido entre el 01 de enero de 2020 al 31

de diciembre de 2022. En ésta es posible apreciar que, de acuerdo con la información disponible

para la estación de monitoreo Casablanca, las concentraciones de los contaminantes: material

particulado respirable (MP10), monóxido de carbono (CO), dióxido de nitrógeno (NO 2 ) y dióxido de

azufre (SO 2 ), se encuentran por bajo el umbral establecido por las normas respectivas.

**Tabla 5-31. Resumen Línea de Base de Calidad del Aire.**

|Contaminante|Estadígrafo|Norma|Unidad|Estación Casablanca|Col6|
|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Norma**|**Unidad**|**Valor**|**Porcentaje de la Norma**|
|MP10|P 98 - 24 horas|130|μg/m3N|86|66,2%|
|MP10|Media Trianual|50|μg/m3N|32|64,0%|
|CO|P 99 - 1 hora|30|mg/m3N|1,3|4,4%|
|CO|P 99 - 8 horas|10|mg/m3N|0,9|8,9%|
|NO2|P 99 - 1 hora|400|μg/m3N|52,6|13,1%|
|NO2|Media Trianual|100|μg/m3N|11,3|11,3%|
|SO2|P 99 - 1 hora|350|μg/m3N|13,0|3,7%|
|SO2|P 99 - 24 horas|150|μg/m3N|2,6|1,7%|
|SO2|Media Anual|60|μg/m3N|1,3|2,2%|

Fuente: “Anexo 03.2 Modelación de emisiones atmosféricas”, componente de la Consulta de Pertinencia de ingreso al SEIA [(1)]

“Ampliación Línea Snacks” de presentada por TRESMONTES S.A.

www.dfmconsultores.cl

92
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

###### 5.10 Escenario de Modelación

Para la modelación de dispersión de contaminantes, específicamente de MP2.5, MP10, MPS, CO,

NO 2 y SO 2, se han considerado las emisiones correspondientes a la fase de construcción, en

particular, el año 1 por ser aquel año con mayor magnitud de emisiones. Dichas emisiones se

presentan de manera detallada en el Anexo 2-1: “Estimación de Emisiones Atmosféricas”

componente de la presente DIA y de forma resumida en la Tabla 4-1.

5.10.1 Fuentes Emisoras

Las fuentes emisoras han sido georreferenciadas de acuerdo con la información proporcionada por

la ingeniería del Proyecto, para posteriormente ser ingresadas al modelo de dispersión de

contaminantes.

En consecuencia, en las Figura 5-48, Figura 5-49 y Figura 5-50 se presentan las ubicaciones de las

distintas fuentes emisoras, mientras que en la Tabla 5-32 se muestra el detalle de las características

de las fuentes y las tasas de emisión asociadas a cada una.

www.dfmconsultores.cl

93
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-48. Ubicación Fuentes Emisoras de área y puntuales.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

94
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-49. Ubicación Fuentes Emisoras de camino.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

95
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-50. Ubicación Fuentes Emisoras lineales-areales.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

96
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

De esta manera, a continuación, en la Tabla 5-32 se presentan las dimensiones de cada fuente y su respectiva tasa de emisión, calculadas para el

escenario de modelación.

**Tabla 5-32. Características Fuentes Emisoras de contaminantes atmosféricos.**

|ID Fuente|Descripción|Tipo de Fuente|Dimensión<br>característica9|Col5|Tasa de emisión Año 1|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID Fuente**|**Descripción**|**Tipo de Fuente**|**- **|**Unidad**|**MP2.5**|**MP10**|**MPS**|**CO**|**NO**|**NO2 **|**SO2 **|**Unidad**|
|PFV_1_1|Parque Fotovoltaico 1_1|AREAL|138.359|m2|1,672E-07|5,207E-07|1,213E-06|4,980E-07|4,152E-07|7,073E-08|1,115E-09|g/s-m2|
|PFV_1_2|Parque Fotovoltaico 1_2|AREAL|53.127|m2|1,672E-07|5,207E-07|1,213E-06|4,980E-07|4,152E-07|7,073E-08|1,115E-09|g/s-m2|
|PFV_1_3|Parque Fotovoltaico 1_3|AREAL|9.084|m2|1,672E-07|5,207E-07|1,213E-06|4,980E-07|4,152E-07|7,073E-08|1,115E-09|g/s-m2|
|PFV_1_4|Parque Fotovoltaico 1_4|AREAL|43.540|m2|1,672E-07|5,207E-07|1,213E-06|4,980E-07|4,152E-07|7,073E-08|1,115E-09|g/s-m2|
|PFV_2|Parque Fotovoltaico 2|AREAL|376.863|m2|1,672E-07|5,207E-07|1,213E-06|4,980E-07|4,152E-07|7,073E-08|1,115E-09|g/s-m2|
|PFV_3_1|Parque Fotovoltaico 3_1|AREAL|99.648|m2|1,672E-07|5,207E-07|1,213E-06|4,980E-07|4,152E-07|7,073E-08|1,115E-09|g/s-m2|
|PFV_3_2|Parque Fotovoltaico 3_1|AREAL|22.607|m2|1,672E-07|5,207E-07|1,213E-06|4,980E-07|4,152E-07|7,073E-08|1,115E-09|g/s-m2|
|PFV_4|Parque Fotovoltaico 4|AREAL|157.077|m2|1,672E-07|5,207E-07|1,213E-06|4,980E-07|4,152E-07|7,073E-08|1,115E-09|g/s-m2|
|LAT_1|Línea eléctrica soterrada 1|LINEAL-AREAL|12.321|m2|4,081E-06|5,744E-06|1,805E-05|2,312E-05|1,443E-05|2,459E-06|4,755E-08|g/s-m2|
|LAT_2|Línea eléctrica soterrada 2|LINEAL-AREAL|286|m2|4,081E-06|5,744E-06|1,805E-05|2,312E-05|1,443E-05|2,459E-06|4,755E-08|g/s-m2|
|LAT_3|Línea eléctrica soterrada 3|LINEAL-AREAL|1.389|m2|4,081E-06|5,744E-06|1,805E-05|2,312E-05|1,443E-05|2,459E-06|4,755E-08|g/s-m2|
|LAT_4|Línea eléctrica soterrada 4|LINEAL-AREAL|148|m2|4,081E-06|5,744E-06|1,805E-05|2,312E-05|1,443E-05|2,459E-06|4,755E-08|g/s-m2|
|LAT_5|Línea eléctrica soterrada 5|LINEAL-AREAL|3.141|m2|4,081E-06|5,744E-06|1,805E-05|2,312E-05|1,443E-05|2,459E-06|4,755E-08|g/s-m2|
|LAT|Línea de alta tensión|LINEAL-AREAL|121|m2|1,720E-05|2,422E-05|7,609E-05|9,746E-05|6,085E-05|1,037E-05|2,005E-07|g/s-m2|
|BESS_1_2|BESS 1 y 2|AREAL|7.780|m2|3,237E-06|4,557E-06|1,432E-05|1,834E-05|1,145E-05|1,951E-06|3,772E-08|g/s-m2|
|BESS_3|BESS 3|AREAL|1.100|m2|3,237E-06|4,557E-06|1,432E-05|1,834E-05|1,145E-05|1,951E-06|3,772E-08|g/s-m2|
|BESS_4|BESS 4|AREAL|531|m2|3,237E-06|4,557E-06|1,432E-05|1,834E-05|1,145E-05|1,951E-06|3,772E-08|g/s-m2|
|GE_1|Grupo Electrógeno (IF 1)|PUNTUAL|-|-|6,975E-03|6,975E-03|6,975E-03|2,138E-02|5,824E-02|9,923E-03|6,525E-03|g/s|
|GE_2|Grupo Electrógeno (Subestación Acuyo)|PUNTUAL|-|-|6,975E-03|6,975E-03|6,975E-03|2,138E-02|5,824E-02|9,923E-03|6,525E-03|g/s|

9 La dimensión característica considera para las fuentes de camino ( _ROAD_ ) el largo de este, para fuentes poligonales (AREA o LINE-AREA) considera el área de
estas y para fuentes puntuales (POINT) esta dimensión no es considerada y está incluida por defecto en el modelo.

www.dfmconsultores.cl

97
**info@dfmconsultores.cl**

|Proyecto “Parque Solar Fotovoltaico Acuyo” Modelación de Dispersión de Contaminantes Atmosféricos Diciembre 2023|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
||||||||||||||
|**ID Fuente**|**Descripción**|**Tipo de Fuente**|**Dimensión**<br>**característica9 **|**Dimensión**<br>**característica9 **|**Tasa de emisión Año 1**|**Tasa de emisión Año 1**|**Tasa de emisión Año 1**|**Tasa de emisión Año 1**|**Tasa de emisión Año 1**|**Tasa de emisión Año 1**|**Tasa de emisión Año 1**|**Tasa de emisión Año 1**|
|**ID Fuente**|**Descripción**|**Tipo de Fuente**|**- **|**Unidad**|**MP2.5**|**MP10**|**MPS**|**CO**|**NO**|**NO2 **|**SO2 **|**Unidad**|
|GE_3|Grupo Electrógeno (IF 2)|PUNTUAL|-|-|6,975E-03|6,975E-03|6,975E-03|2,138E-02|5,824E-02|9,923E-03|6,525E-03|g/s|
|GE_4|Grupo Electrógeno (PFV 3)|PUNTUAL|-|-|6,975E-03|6,975E-03|6,975E-03|2,138E-02|5,824E-02|9,923E-03|6,525E-03|g/s|
|GE_5|Grupo Electrógeno (PFV 4)|PUNTUAL|-|-|6,975E-03|6,975E-03|6,975E-03|2,138E-02|5,824E-02|9,923E-03|6,525E-03|g/s|
|TRA_4|Tramo 4|CAMINO|6.223|m|9,004E-07|3,229E-06|1,616E-05|1,780E-06|4,460E-06|7,598E-07|8,004E-09|g/s-m|
|TRA_5|Tramo 5|CAMINO|983|m|1,770E-06|6,823E-06|3,488E-05|1,787E-06|4,476E-06|7,625E-07|8,032E-09|g/s-m|
|TRA_6|Tramo 6|CAMINO|2.086|m|1,938E-06|7,471E-06|3,819E-05|1,949E-06|4,889E-06|8,329E-07|8,773E-09|g/s-m|
|TRA_7|Tramo 7|CAMINO|1.307|m|1,627E-05|1,622E-04|5,675E-04|6,223E-07|1,557E-06|2,652E-07|2,783E-09|g/s-m|
|TRA_8|Tramo 8|CAMINO|60|m|1,793E-06|1,787E-05|6,251E-05|8,377E-08|2,041E-07|3,477E-08|3,510E-10|g/s-m|
|TRA_9|Tramo 9|CAMINO|75|m|3,635E-07|3,622E-06|1,267E-05|1,698E-08|4,137E-08|7,049E-09|7,115E-11|g/s-m|
|TRA_10|Tramo 10|CAMINO|196|m|1,472E-06|1,466E-05|5,131E-05|6,876E-08|1,675E-07|2,854E-08|2,881E-10|g/s-m|
|TRA_11|Tramo 11|CAMINO|1.630|m|3,483E-05|3,472E-04|1,215E-03|1,303E-06|3,272E-06|5,574E-07|5,883E-09|g/s-m|
|TRA_12_1|Tramo 12_1|CAMINO|358|m|8,756E-07|8,730E-06|3,055E-05|3,317E-08|8,254E-08|1,406E-08|1,469E-10|g/s-m|
|TRA_12_2|Tramo 12_2|CAMINO|1.573|m|8,756E-07|8,730E-06|3,055E-05|3,317E-08|8,254E-08|1,406E-08|1,469E-10|g/s-m|
|TRA_12_3|Tramo 12_3|CAMINO|900|m|8,756E-07|8,730E-06|3,055E-05|3,317E-08|8,254E-08|1,406E-08|1,469E-10|g/s-m|
|TRA_12_4|Tramo 12_4|CAMINO|931|m|8,756E-07|8,730E-06|3,055E-05|3,317E-08|8,254E-08|1,406E-08|1,469E-10|g/s-m|
|TRA_13_1|Tramo 13_1|CAMINO|1.410|m|2,607E-06|2,600E-05|9,096E-05|9,876E-08|2,458E-07|4,187E-08|4,373E-10|g/s-m|
|TRA_13_2|Tramo 13_2|CAMINO|1.061|m|2,607E-06|2,600E-05|9,096E-05|9,876E-08|2,458E-07|4,187E-08|4,373E-10|g/s-m|
|TRA_13_3|Tramo 13_3|CAMINO|764|m|2,607E-06|2,600E-05|9,096E-05|9,876E-08|2,458E-07|4,187E-08|4,373E-10|g/s-m|
|TRA_13_4|Tramo 13_4|CAMINO|520|m|2,607E-06|2,600E-05|9,096E-05|9,876E-08|2,458E-07|4,187E-08|4,373E-10|g/s-m|
|TRA_14_1|Tramo 14_1|CAMINO|1.163|m|1,150E-06|1,146E-05|4,011E-05|4,358E-08|1,084E-07|1,847E-08|1,929E-10|g/s-m|
|TRA_14_2|Tramo 14_2|CAMINO|461|m|1,150E-06|1,146E-05|4,011E-05|4,358E-08|1,084E-07|1,847E-08|1,929E-10|g/s-m|
|TRA_14_3|Tramo 14_3|CAMINO|1.548|m|1,150E-06|1,146E-05|4,011E-05|4,358E-08|1,084E-07|1,847E-08|1,929E-10|g/s-m|
|TRA_15_1|Tramo 15_1|CAMINO|2.573|m|9,735E-07|9,706E-06|3,396E-05|3,678E-08|9,156E-08|1,560E-08|1,630E-10|g/s-m|
|TRA_15_2|Tramo 15_2|CAMINO|670|m|9,735E-07|9,706E-06|3,396E-05|3,678E-08|9,156E-08|1,560E-08|1,630E-10|g/s-m|
|TRA_15_3|Tramo 15_3|CAMINO|141|m|9,735E-07|9,706E-06|3,396E-05|3,678E-08|9,156E-08|1,560E-08|1,630E-10|g/s-m|

Fuente: Elaboración Propia.

www.dfmconsultores.cl

98
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

De forma complementaria, en la Tabla 5-33 se presentan las características principales de las fuentes puntuales, las cuales también fueron

ingresadas como parámetros de entrada al modelo y corresponden a: altura y diámetro de chimenea, y velocidad y temperatura de salida de los

gases.

**Tabla 5-33. Características Fuentes Emisoras Puntuales.**

|Fuente|ID CALPUFF|Altura chimenea<br>(m)|Temperatura salida de los gases<br>(K)|Diámetro interno chimenea<br>(m)|Velocidad de salida de los gases<br>(m/s)|
|---|---|---|---|---|---|
|Grupo Electrógeno (IF 1)|GE_1|1,391|673,15|0,05|22,40|
|Grupo Electrógeno<br>(Subestación Acuyo)|GE_2|1,391|673,15|0,05|22,40|
|Grupo Electrógeno (IF 2)|GE_3|1,391|673,15|0,05|22,40|
|Grupo Electrógeno (PFV 3)|GE_4|1,391|673,15|0,05|22,40|
|Grupo Electrógeno (PFV 4)|GE_5|1,391|673,15|0,05|22,40|

Fuente: Elaboración Propia.

www.dfmconsultores.cl

99
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.10.2 Receptores de Interés

Se definieron 21 receptores, correspondientes a: la estación de monitoreo Casablanca, receptores

de medio humano y receptores de fauna. En la siguiente tabla se presentan las coordenadas de

ubicación, junto con su respectiva elevación, de cada receptor a considerar.

**Tabla 5-34. Receptores de Interés.**

|ID Receptor|Descripción|Coordenadas de Ubicación|Col4|Elevación (m.s.n.m)|
|---|---|---|---|---|
|**ID Receptor**|**Descripción**|**(Datum WGS84)**|**(Datum WGS84)**|**(Datum WGS84)**|
|**ID Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|E_1|Estación Casablanca|278.002|6.309.012|274,95|
|R_1|Receptor de medio humano R1|274.179|6.311.974|269,44|
|R_2|Receptor de medio humano R2|274.662|6.311.643|262,31|
|R_3|Receptor de medio humano R3|274.756|6.311.286|262,63|
|R_4|Receptor de medio humano R4|273.779|6.311.341|263,93|
|R_5|Receptor de medio humano R5|273.945|6.310.943|265,61|
|R_6|Receptor de medio humano R6|274.286|6.310.949|263,46|
|R_7|Receptor de medio humano R7|274.172|6.310.445|266,25|
|R_8|Receptor de medio humano R8|274.434|6.310.332|266,06|
|R_9|Receptor de medio humano R9|273.601|6.310.276|267,81|
|R_10|Receptor de medio humano R10|273.544|6.309.744|286,25|
|R_11|Receptor de medio humano R11|274.360|6.309.617|277,11|
|R_12|Receptor de medio humano R12|274.118|6.309.269|288,31|
|R_13|Receptor de medio humano R13|273.365|6.308.856|308,61|
|R_14|Receptor de medio humano R14|274.199|6.308.835|307,22|
|R_15|Receptor de medio humano R15|275.023|6.308.983|291,32|
|RF_1|Receptor de fauna RF1|274.370|6.311.822|266,07|
|RF_2|Receptor de fauna RF2|274.604|6.311.084|262,66|
|RF_3|Receptor de fauna RF3|274.182|6.310.058|271,26|
|RF_4|Receptor de fauna RF4|273.905|6.308.660|309,52|
|RF_5|Receptor de fauna RF5|274.651|6.308.709|318,83|

Fuente: Elaboración Propia.

Así, en la siguiente figura se presentan, de manera georreferenciada, la ubicación de los receptores

discretos utilizados en la modelación.

www.dfmconsultores.cl

100
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-51. Ubicación de Receptores de Interés.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

101
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

Adicionalmente, se definió una grilla de receptores de acuerdo a lo recomendado en la Guía para el

Uso de Modelos de Calidad del Aire en el SEIA (SEA, 2023). Para esto se utilizaron 5 niveles de

resolución:

 - Nivel 1: Espaciado de 20 metros para el perímetro de las subunidades del parque

fotovoltaico.

 - Nivel 2: Espaciado de 50 metros hasta una distancia de 500 metros desde el centro de las

subunidades del parque fotovoltaico.

 - Nivel 3: Espaciado de 250 metros hasta una distancia de 2.500 metros desde el centro de

las subunidades del parque fotovoltaico.

 - Nivel 4: Espaciado de 500 metros hasta una distancia de 5.000 metros desde el centro de

las subunidades del parque fotovoltaico.

 - Nivel 5: Espaciado de 1.000 metros por todo el dominio de modelación

A continuación, en la Figura 5-52 se presenta la ubicación de la grilla con respecto a la ubicación del

proyecto.

www.dfmconsultores.cl

102
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-52. Ubicación de Grilla de Receptores.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

103
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

###### 5.11 Resultados de la Modelación

En este inciso se presentan los resultados del escenario de modelación descrito anteriormente en

el inciso 5.10. Se presentan tablas donde se cuantifica el aporte de cada contaminante evaluado del

proyecto para cada receptor de interés, luego se realiza una comparación con la normativa de

calidad de aire respectiva, para así establecer el porcentaje del aporte del proyecto respecto a la

norma de cada contaminante.

Además del análisis cuantitativo, se presentan las curvas de isoconcentración e isodepositación para

todos los escenarios y para todos los contaminantes, esto es útil para cuantificar el impacto del

proyecto en todo el dominio de modelación y poder estimar el impacto que tendrá el proyecto en

otras zonas que no necesariamente son las de los receptores de interés.

www.dfmconsultores.cl

104
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.11.1 Material Particulado Fino Respirable (MP2.5)

En la Tabla 5-35 se presentan las concentraciones de Material Particulado Fino Respirable (MP2.5) aportadas por proyecto en los receptores de

interés para el escenario de modelación en estudio.

**Tabla 5-35. Resultados de modelo de dispersión de MP2.5.**

|ID<br>Receptor|Descripción|Coordenadas de Ubicación<br>(Datum WGS84)|Col4|Material Particulado Respirable (MP2.5)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Concentración (μg/m3) - Aporte del**<br>**Proyecto**|**Concentración (μg/m3) - Aporte del**<br>**Proyecto**|**Concentración (μg/m3) - Norma de**<br>**Calidad**|**Concentración (μg/m3) - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil 98 24**<br>**horas**|**Período Anual**|**Percentil 98 24**<br>**horas**|**Período Anual**|**Percentil 98 24**<br>**horas**|**Período Anual**|
|E_1|Estación Casablanca|278.002|6.309.012|0,13|0,02|50|20|0,26%|0,12%|
|R_1|Receptor de medio humano R1|274.179|6.311.974|2,19|0,40|50|20|4,37%|2,00%|
|R_2|Receptor de medio humano R2|274.662|6.311.643|1,62|0,32|50|20|3,25%|1,60%|
|R_3|Receptor de medio humano R3|274.756|6.311.286|1,61|0,35|50|20|3,22%|1,73%|
|R_4|Receptor de medio humano R4|273.779|6.311.341|3,00|0,50|50|20|6,00%|2,52%|
|R_5|Receptor de medio humano R5|273.945|6.310.943|2,21|0,34|50|20|4,42%|1,72%|
|R_6|Receptor de medio humano R6|274.286|6.310.949|4,55|1,42|50|20|9,10%|7,12%|
|R_7|Receptor de medio humano R7|274.172|6.310.445|3,76|1,13|50|20|7,52%|5,65%|
|R_8|Receptor de medio humano R8|274.434|6.310.332|2,22|0,71|50|20|4,44%|3,55%|
|R_9|Receptor de medio humano R9|273.601|6.310.276|1,49|0,24|50|20|2,98%|1,20%|
|R_10|Receptor de medio humano R10|273.544|6.309.744|2,07|0,27|50|20|4,14%|1,34%|
|R_11|Receptor de medio humano R11|274.360|6.309.617|2,83|0,62|50|20|5,67%|3,09%|
|R_12|Receptor de medio humano R12|274.118|6.309.269|2,01|0,36|50|20|4,02%|1,82%|
|R_13|Receptor de medio humano R13|273.365|6.308.856|0,45|0,05|50|20|0,91%|0,25%|
|R_14|Receptor de medio humano R14|274.199|6.308.835|1,02|0,21|50|20|2,04%|1,03%|
|R_15|Receptor de medio humano R15|275.023|6.308.983|0,96|0,16|50|20|1,92%|0,82%|

Fuente: Elaboración Propia.

www.dfmconsultores.cl

105
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

De los resultados presentados en la tabla anterior, se observa que los aportes del del proyecto sobre los receptores de interés no superan el 9,1%

de la norma de este contaminante en periodo diario en el receptor de medio humano “R_6”, mientras que, para periodo anual, los valores no

sobrepasan el 7,1% de la normativa respectiva en el mismo receptor de medio humano.

En la Figura 5-53 y la Figura 5-54 se presentan las curvas de isoconcentración de Material Particulado Fino Respirable (MP2.5) para la norma de

percentil 98 de 24 horas y la norma periodo anual respectivamente.

www.dfmconsultores.cl

106
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-53. Curva de Isoconcentración para Percentil 98 período 24 horas MP2.5 (μg/m** **[3]** **).**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

107
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-54. Curva de Isoconcentración para período anual MP2.5 (μg/m** **[3]** **).**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

108
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.11.2 Material Particulado Respirable (MP10)

En la Tabla 5-36 se presentan las concentraciones de Material Particulado Respirable (MP10) aportadas por el proyecto en los receptores de interés

para el escenario de modelación en estudio.

**Tabla 5-36. Resultados de modelo de dispersión de MP10.**

|ID<br>Receptor|Descripción|Coordenadas de Ubicación<br>(Datum WGS84)|Col4|Material Particulado Respirable (MP10)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Concentración (μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración (μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración (μg/m3N) - Norma de**<br>**Calidad**|**Concentración (μg/m3N) - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil 98 24**<br>**horas**|**Período Anual**|**Percentil 98 24**<br>**horas**|**Período Anual**|**Percentil 98 24**<br>**horas**|**Período Anual**|
|E_1|Estación Casablanca|278.002|6.309.012|0,71|0,11|130|50|0,54%|0,22%|
|R_1|Receptor de medio humano R1|274.179|6.311.974|6,51|1,34|130|50|5,01%|2,68%|
|R_2|Receptor de medio humano R2|274.662|6.311.643|5,69|1,27|130|50|4,37%|2,53%|
|R_3|Receptor de medio humano R3|274.756|6.311.286|6,37|1,58|130|50|4,90%|3,16%|
|R_4|Receptor de medio humano R4|273.779|6.311.341|18,68|3,08|130|50|14,37%|6,17%|
|R_5|Receptor de medio humano R5|273.945|6.310.943|11,17|1,84|130|50|8,59%|3,67%|
|R_6|Receptor de medio humano R6|274.286|6.310.949|28,99|11,12|130|50|22,30%|22,25%|
|R_7|Receptor de medio humano R7|274.172|6.310.445|28,12|8,22|130|50|21,63%|16,45%|
|R_8|Receptor de medio humano R8|274.434|6.310.332|14,31|4,21|130|50|11,01%|8,43%|
|R_9|Receptor de medio humano R9|273.601|6.310.276|9,96|1,44|130|50|7,67%|2,87%|
|R_10|Receptor de medio humano R10|273.544|6.309.744|10,93|1,43|130|50|8,41%|2,86%|
|R_11|Receptor de medio humano R11|274.360|6.309.617|12,97|2,77|130|50|9,97%|5,54%|
|R_12|Receptor de medio humano R12|274.118|6.309.269|7,95|1,49|130|50|6,12%|2,98%|
|R_13|Receptor de medio humano R13|273.365|6.308.856|1,80|0,22|130|50|1,38%|0,43%|
|R_14|Receptor de medio humano R14|274.199|6.308.835|4,17|0,76|130|50|3,21%|1,51%|
|R_15|Receptor de medio humano R15|275.023|6.308.983|3,20|0,64|130|50|2,46%|1,28%|

Fuente: Elaboración Propia.

www.dfmconsultores.cl

109
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

De los resultados presentados en la tabla anterior, se observa que los aportes del del proyecto sobre los receptores de interés no superan el 22,3%

de la norma de este contaminante en periodo diario en el receptor de medio humano “R_6”, mientras que, para periodo anual, los valores no

sobrepasan el 22,3% de la normativa respectiva en el mismo receptor de medio humano.

En la Figura 5-55 y la Figura 5-56 se presentan las curvas de isoconcentración de Material Particulado Respirable (MP10) para la norma de percentil

98 de 24 horas y la norma periodo anual, respectivamente.

www.dfmconsultores.cl

110
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-55. Curva de Isoconcentración para Percentil 98 período 24 horas MP10 (μg/m** **[3]** **).**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

111
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-56. Curva de Isoconcentración para período anual MP10 (μg/m** **[3]** **).**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

112
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.11.3 Material Particulado Sedimentable (MPS)

En la Tabla 5-37 se presentan las concentraciones de Material Particulado Sedimentable (MPS) aportadas por el proyecto en los receptores de flora

de interés para el escenario de modelación en estudio.

**Tabla 5-37. Resultados de modelo de dispersión de MPS.**

|ID<br>Receptor|Descripción|Coordenadas de Ubicación<br>(Datum WGS84)|Col4|Material Particulado Sedimentable (MPS)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Tasa de depositación (mg/m2-dia)**|**Tasa de depositación (mg/m2-dia)**|**Norma (mg/m2-dia)**|**Norma (mg/m2-dia)**|**Porcentaje de la Norma**|**Porcentaje de la Norma**|
|**ID**<br>**Receptor**|**Descripción**|**Este**|**Norte**|**Período Mensual**|**Período Anual**|**Período Mensual**|**Período Anual**|**Período Mensual**|**Período Anual**|
|RF_1|Receptor de fauna RF1|274.370|6.311.822|13,92|7,28|333|200|4,18%|3,64%|
|RF_2|Receptor de fauna RF2|274.604|6.311.084|14,47|9,35|333|200|4,35%|4,68%|
|RF_3|Receptor de fauna RF3|274.182|6.310.058|63,06|35,05|333|200|18,94%|17,52%|
|RF_4|Receptor de fauna RF4|273.905|6.308.660|2,84|1,46|333|200|0,85%|0,73%|
|RF_5|Receptor de fauna RF5|274.651|6.308.709|3,42|1,51|333|200|1,03%|0,75%|

Fuente: Elaboración Propia.

De los resultados presentados en la tabla anterior, se observa que los aportes del del proyecto sobre los receptores de interés no superan el 18,9%

de la norma de este contaminante en periodo mensual en el receptor de fauna “RF_3”, mientras que, para periodo anual, los valores no sobrepasan

el 17,5% de la normativa respectiva en el mismo receptor de fauna.

www.dfmconsultores.cl

113
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-57. Curva de Isodepositación para periodo Mensual de MPS (mg/m** **[2]** **-día).**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

114
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-58. Curva de Isodepositación para periodo Anual de MPS (mg/m** **[2]** **-día).**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

115
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.11.4 Monóxido de Carbono (CO)

En la Tabla 5-38 se presentan las concentraciones de Monóxido de Carbono (CO) aportadas por el proyecto en los receptores de interés para el

escenario de modelación en estudio.

**Tabla 5-38. Resultados de modelo de dispersión de CO.**

|ID<br>Receptor|Descripción|Coordenadas de Ubicación<br>(Datum WGS84)|Col4|Monóxido de Carbono (CO)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Coordenadas de Ubicación**<br>** (Datum WGS84)**|**Concentración (mg/m3N) - Aporte del**<br>**Proyecto**|**Concentración (mg/m3N) - Aporte del**<br>**Proyecto**|**Concentración (mg/m3N) - Norma de**<br>**Calidad**|**Concentración (mg/m3N) - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil 99 1 hora**|**Percentil 99 8**<br>**horas**|**Percentil 99 1 hora**|**Percentil 99 8**<br>**horas**|**Percentil 99 1 hora**|**Percentil 99 8**<br>**horas**|
|E_1|Estación Casablanca|278.002|6.309.012|0,00|0,00|30|10|0,01%|0,01%|
|R_1|Receptor de medio humano R1|274.179|6.311.974|0,16|0,02|30|10|0,54%|0,22%|
|R_2|Receptor de medio humano R2|274.662|6.311.643|0,12|0,02|30|10|0,41%|0,19%|
|R_3|Receptor de medio humano R3|274.756|6.311.286|0,10|0,01|30|10|0,35%|0,13%|
|R_4|Receptor de medio humano R4|273.779|6.311.341|0,15|0,02|30|10|0,51%|0,24%|
|R_5|Receptor de medio humano R5|273.945|6.310.943|0,14|0,02|30|10|0,46%|0,18%|
|R_6|Receptor de medio humano R6|274.286|6.310.949|0,14|0,02|30|10|0,48%|0,24%|
|R_7|Receptor de medio humano R7|274.172|6.310.445|0,09|0,01|30|10|0,30%|0,14%|
|R_8|Receptor de medio humano R8|274.434|6.310.332|0,06|0,01|30|10|0,19%|0,11%|
|R_9|Receptor de medio humano R9|273.601|6.310.276|0,07|0,01|30|10|0,22%|0,09%|
|R_10|Receptor de medio humano R10|273.544|6.309.744|0,09|0,01|30|10|0,31%|0,12%|
|R_11|Receptor de medio humano R11|274.360|6.309.617|0,10|0,02|30|10|0,34%|0,15%|
|R_12|Receptor de medio humano R12|274.118|6.309.269|0,11|0,02|30|10|0,36%|0,17%|
|R_13|Receptor de medio humano R13|273.365|6.308.856|0,02|0,00|30|10|0,05%|0,02%|
|R_14|Receptor de medio humano R14|274.199|6.308.835|0,05|0,01|30|10|0,18%|0,09%|
|R_15|Receptor de medio humano R15|275.023|6.308.983|0,06|0,01|30|10|0,19%|0,09%|

Fuente: Elaboración Propia.

www.dfmconsultores.cl

116
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

De los resultados presentados en la tabla anterior, se observa que los aportes del del proyecto sobre los receptores de interés no superan el 0,54%

de la norma de este contaminante en periodo horario en el receptor de medio humano “R_1”, mientras que, para periodo de 8 horas, los valores

no sobrepasan el 0,24% de la normativa respectiva en el mismo receptor de medio humano “R_6”.

Cabe señalar que, debido a los bajos valores obtenidos, no se presentan curvas de isoconcentración, ya que se encuentran por debajo de 1 mg/m [3] N.

www.dfmconsultores.cl

117
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.11.5 Dióxido de Nitrógeno (NO 2 )

En la Tabla 5-39 se presentan las concentraciones de Dióxido de Nitrógeno (NO 2 ) aportadas por el proyecto en los receptores de interés para el

escenario de modelación en estudio.

**Tabla 5-39. Resultados de modelo de dispersión de NO** **2** **.**

|ID<br>Receptor|Descripción|Coordenadas de Ubicación|Col4|Dióxido de Nitrógeno (NO2)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de Ubicación**|**Coordenadas de Ubicación**|**Concentración (μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración (μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración (μg/m3N) - Norma de**<br>**Calidad**|**Concentración (μg/m3N) - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil 99 1 hora**|**Período Anual**|**Percentil 99 1 hora**|**Período Anual**|**Percentil 99 1 hora**|**Período Anual**|
|E_1|Estación Casablanca|278.002|6.309.012|5,88|0,06|400|100|1,47%|0,06%|
|R_1|Receptor de medio humano R1|274.179|6.311.974|84,78|0,71|400|100|21,19%|0,71%|
|R_2|Receptor de medio humano R2|274.662|6.311.643|61,27|0,70|400|100|15,32%|0,70%|
|R_3|Receptor de medio humano R3|274.756|6.311.286|65,14|0,76|400|100|16,28%|0,76%|
|R_4|Receptor de medio humano R4|273.779|6.311.341|73,31|0,60|400|100|18,33%|0,60%|
|R_5|Receptor de medio humano R5|273.945|6.310.943|79,13|0,64|400|100|19,78%|0,64%|
|R_6|Receptor de medio humano R6|274.286|6.310.949|71,59|0,84|400|100|17,90%|0,84%|
|R_7|Receptor de medio humano R7|274.172|6.310.445|49,76|0,80|400|100|12,44%|0,80%|
|R_8|Receptor de medio humano R8|274.434|6.310.332|44,85|0,77|400|100|11,21%|0,77%|
|R_9|Receptor de medio humano R9|273.601|6.310.276|53,03|0,41|400|100|13,26%|0,41%|
|R_10|Receptor de medio humano R10|273.544|6.309.744|60,47|0,45|400|100|15,12%|0,45%|
|R_11|Receptor de medio humano R11|274.360|6.309.617|75,07|0,92|400|100|18,77%|0,92%|
|R_12|Receptor de medio humano R12|274.118|6.309.269|76,05|0,67|400|100|19,01%|0,67%|
|R_13|Receptor de medio humano R13|273.365|6.308.856|17,60|0,13|400|100|4,40%|0,13%|
|R_14|Receptor de medio humano R14|274.199|6.308.835|39,54|0,42|400|100|9,89%|0,42%|
|R_15|Receptor de medio humano R15|275.023|6.308.983|36,51|0,33|400|100|9,13%|0,33%|

Fuente: Elaboración Propia.

www.dfmconsultores.cl

118
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

De los resultados presentados en la tabla anterior, se observa que los aportes del del proyecto sobre los receptores de interés no superan el 21,2%

de la norma de este contaminante en periodo horario en el receptor de medio humano “R_1”, mientras que, para periodo de 8 horas, los valores

no sobrepasan el 0,92% de la normativa respectiva en el mismo receptor de medio humano “R_11”.

En la Figura 5-59 y la Figura 5-60 se presentan las curvas de isoconcentración de dióxido de nitrógeno (NO 2 ) para la norma de percentil 99 de 1

hora y la norma de periodo anual, respectivamente.

www.dfmconsultores.cl

119
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-59. Curva de Isoconcentración para Percentil 99 periodo 1 hora NO** **2** **(μg/m** **[3]** **).**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

120
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-60. Curva de Isoconcentración para periodo anual NO** **2** **(μg/m** **[3]** **).**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

121
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.11.6 Dióxido de Azufre (SO 2 ). Normas primarias

En la Tabla 5-40 se presentan las concentraciones de Dióxido de Azufre (SO 2 ) aportadas por el proyecto en los receptores de interés para el

escenario de modelación en estudio.

**Tabla 5-40. Resultados de modelo de dispersión de SO** **2** **. Normas primarias de calidad del aire.**

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación|Col4|Dióxido de Azufre (SO2)|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**|**Coordenadas de**<br>**Ubicación**|**Concentración (μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración (μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración (μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración (μg/m3N) - Norma de**<br>**Calidad**|**Concentración (μg/m3N) - Norma de**<br>**Calidad**|**Concentración (μg/m3N) - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil 99**<br>**1 hora**|**Percentil 99**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 99**<br>**1 hora**|**Percentil 99**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 99**<br>**1 hora**|**Percentil 99**<br>**24 horas**|**Período**<br>**Anual**|
|E_1|Estación Casablanca|278.002|6.309.012|0,03|0,01|0,00|350|150|60|0,01%|0,01%|0,00%|
|R_1|Receptor de medio humano R1|274.179|6.311.974|0,44|0,14|0,03|350|150|60|0,12%|0,09%|0,05%|
|R_2|Receptor de medio humano R2|274.662|6.311.643|0,37|0,08|0,02|350|150|60|0,11%|0,05%|0,03%|
|R_3|Receptor de medio humano R3|274.756|6.311.286|0,42|0,12|0,02|350|150|60|0,12%|0,08%|0,04%|
|R_4|Receptor de medio humano R4|273.779|6.311.341|0,44|0,16|0,02|350|150|60|0,13%|0,11%|0,03%|
|R_5|Receptor de medio humano R5|273.945|6.310.943|0,35|0,11|0,01|350|150|60|0,10%|0,07%|0,02%|
|R_6|Receptor de medio humano R6|274.286|6.310.949|0,37|0,14|0,02|350|150|60|0,10%|0,09%|0,03%|
|R_7|Receptor de medio humano R7|274.172|6.310.445|0,23|0,08|0,01|350|150|60|0,07%|0,05%|0,02%|
|R_8|Receptor de medio humano R8|274.434|6.310.332|0,19|0,05|0,02|350|150|60|0,05%|0,04%|0,03%|
|R_9|Receptor de medio humano R9|273.601|6.310.276|0,18|0,05|0,01|350|150|60|0,05%|0,03%|0,01%|
|R_10|Receptor de medio humano R10|273.544|6.309.744|0,24|0,15|0,01|350|150|60|0,07%|0,10%|0,02%|
|R_11|Receptor de medio humano R11|274.360|6.309.617|0,32|0,10|0,02|350|150|60|0,09%|0,07%|0,03%|
|R_12|Receptor de medio humano R12|274.118|6.309.269|0,34|0,10|0,02|350|150|60|0,10%|0,07%|0,03%|
|R_13|Receptor de medio humano R13|273.365|6.308.856|0,08|0,02|0,00|350|150|60|0,02%|0,02%|0,00%|
|R_14|Receptor de medio humano R14|274.199|6.308.835|0,33|0,09|0,02|350|150|60|0,09%|0,06%|0,03%|
|R_15|Receptor de medio humano R15|275.023|6.308.983|0,25|0,10|0,01|350|150|60|0,07%|0,07%|0,02%|

Fuente: Elaboración Propia.

De los resultados presentados en la tabla anterior, se observa que los aportes del del proyecto sobre los receptores de interés no superan el 0,13%

de la norma de este contaminante en periodo horario en el receptor de medio humano “R_4”, mientras que, para periodo de 24 horas, los valores

no sobrepasan el 0,11% de la normativa respectiva en el mismo receptor de medio humano “R_6”. Para el periodo anual, los valores no sobrepasan

el 0,05% de la normativa respectiva en el mismo receptor de medio humano “R_2”.

www.dfmconsultores.cl

122
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

En la Figura 5-61, Figura 5-62 y Figura 5-63 se presentan las curvas de isoconcentración de dióxido de azufre (SO 2 ) para la norma de percentil 99

de 1 hora, percentil 99 de 24 horas, y de periodo anual, respectivamente.

www.dfmconsultores.cl

123
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-61. Curva de Isoconcentración para Percentil 99 período 1 hora SO** **2** **(μg/m** **[3]** **). Norma primaria de**

**calidad del aire.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

124
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-62. Curva de Isoconcentración para Percentil 99 período 24 horas SO** **2** **(μg/m** **[3]** **). Norma primaria de**

**calidad del aire.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

125
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-63. Curva de Isoconcentración para periodo Anual SO** **2** **(μg/m** **[3]** **). Norma primaria de calidad del**

**aire.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

126
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

5.11.7 Dióxido de Azufre (SO 2 ). Normas secundarias.

En la Tabla 5-41 se presentan los aportes de Dióxido de Azufre (SO 2 ) del proyecto en los receptores de interés para el escenario de modelación en

estudio.

**Tabla 5-41. Resultados de modelo de dispersión de SO** **2** **. Normas secundarias de calidad del aire.**

|ID<br>Receptor|Descripción|Coordenadas de Ubicación|Col4|Dióxido de Azufre (SO2)|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de Ubicación**|**Coordenadas de Ubicación**|**Concentración (μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración (μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración (μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración (μg/m3N) - Norma de**<br>**Calidad**|**Concentración (μg/m3N) - Norma de**<br>**Calidad**|**Concentración (μg/m3N) - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil**<br>**99,73 1 hora**|**Percentil**<br>**99,7 24 horas**|**Período**<br>**Anual**|**Percentil**<br>**99,73 1 hora**|**Percentil**<br>**99,7 24 horas**|**Período**<br>**Anual**|**Percentil**<br>**99,73 1 hora**|**Percentil**<br>**99,7 24 horas**|**Período**<br>**Anual**|
|RF_1|Receptor de fauna RF1|274.370|6.311.822|0,94|0,21|0,04|700|260|60|0,13%|0,08%|0,07%|
|RF_2|Receptor de fauna RF2|274.604|6.311.084|0,82|0,17|0,02|700|260|60|0,12%|0,07%|0,03%|
|RF_3|Receptor de fauna RF3|274.182|6.310.058|0,55|0,13|0,03|700|260|60|0,08%|0,05%|0,05%|
|RF_4|Receptor de fauna RF4|273.905|6.308.660|0,39|0,06|0,01|700|260|60|0,06%|0,02%|0,01%|
|RF_5|Receptor de fauna RF5|274.651|6.308.709|0,53|0,14|0,02|700|260|60|0,08%|0,05%|0,03%|

Fuente: Elaboración Propia.

De los resultados presentados en la tabla anterior, se observa que los aportes del del proyecto sobre los receptores de interés no superan el 0,13%

de la norma de este contaminante en periodo horario en el receptor de fauna “RF_1”, mientras que, para periodo de 24 horas, los valores no

sobrepasan el 0,08% de la normativa respectiva en el mismo receptor. Para el periodo anual, los valores no sobrepasan el 0,07% de la normativa

respectiva en el mismo receptor.

En la Figura 5-64, Figura 5-65 y Figura 5-66 se presentan las curvas de isoconcentración de dióxido de azufre (SO 2 ) para las normas secundarias de

percentil 99,73 de 1 hora, percentil 99,7 de 24 horas, y de periodo anual, respectivamente.

www.dfmconsultores.cl

127
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-64. Curva de Isoconcentración para Percentil 99,73 período 1 hora SO** **2** **(μg/m** **[3]** **). Norma**

**secundaria de calidad del aire.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

128
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-65. Curva de Isoconcentración para Percentil 99,7 período 24 horas SO** **2** **(μg/m** **[3]** **). Norma**

**secundaria de calidad del aire.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

129
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-66. Curva de Isoconcentración para periodo Anual SO** **2** **(μg/m** **[3]** **). Norma secundaria de calidad del**

**aire.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

130
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

###### 5.12 Concentración total esperada

Con el fin de cuantificar el impacto que tendrá la ejecución del proyecto en todos aquellos

receptores de interés con los que se cuenta información monitoreada de la línea de base, se

presenta en este inciso la concentración total esperada de cada uno, la que se obtiene sumando los

valores de la línea de base, presentados en el inciso 5.9, a los aportes del proyecto, presentados en

el inciso 5.11.

En la Tabla 5-42 se presenta la concentración total esperada en la estación de monitoreo

Casablanca.

**Tabla 5-42. Concentración total esperada. Estación Casablanca.**

|Contaminante|Estadígrafo|Norma|Unidad|Línea de base|Col6|Aporte Proyecto|Col8|Concentración total|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Norma**|**Unidad**|**Valor**|**% Norma**|**Valor**|**% Norma**|**Valor**|**% Norma**|
|MP10|P 98 - 24<br>horas|130|μg/m3N|86,0|66,15%|0,71|0,54%|86,71|66,70%|
|MP10|Media<br>Trianual|50|μg/m3N|32,0|64,00%|0,11|0,22%|32,11|64,22%|
|CO|P 99 - 1<br>hora|30|mg/m3N|1,3|4,33%|0,00|0,01%|1,30|4,35%|
|CO|P 99 - 8<br>horas|10|mg/m3N|0,9|9,00%|0,00|0,01%|0,90|9,01%|
|NO2|P 99 - 1<br>hora|400|μg/m3N|52,6|13,15%|5,88|1,47%|58,48|14,62%|
|NO2|Media<br>Trianual|100|μg/m3N|11,3|11,30%|0,06|0,06%|11,36|11,36%|
|SO2|P 99 - 1<br>hora|350|μg/m3N|13,0|3,71%|0,03|0,01%|13,03|3,72%|
|SO2|P 99 - 24<br>horas|150|μg/m3N|2,6|1,73%|0,01|0,01%|2,61|1,74%|
|SO2|Media<br>Anual|60|μg/m3N|1,3|2,17%|0,00|0,00%|1,30|2,17%|

Fuente: Elaboración Propia.

Como se puede apreciar en la tabla precedente, los aportes del Proyecto a la concentración

ambiental en la estación Casablanca, son menores que los valores establecidos para los SILs (Niveles

de Impacto Significativo) para los contaminantes de: Material Particulado Respirable (MP10),

Monóxido de Carbono (CO), Dióxido de Nitrógeno (NO 2 ) y Dióxido de Azufre (SO 2 ).

En consecuencia, los aportes del proyecto determinados bajo un escenario conservador de

modelación no tendrán efectos significativos en la calidad del aire en Casablanca.

www.dfmconsultores.cl

131
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

###### 5.13 Área de Influencia

Tomando en consideración lo señalado en los artículos 5 y 6 del RSEIA así como lo estipulado en la
“Guía Calidad del Aire en el Área de Influencia de Proyectos que ingresan al SEIA” (SEA, 2015), para

la definición del área de influencia, y en función de evaluar el “riesgo a la salud de la población” y la

afectación de los recursos naturales renovables debido a la calidad del aire, se han considerado

criterios sobre la base de los receptores sensibles en los cuales existe un objeto de protección, con

norma primaria o secundaria vigente en Chile, o alguna norma de referencia. Lo anterior en función

a que se busca establecer si, con el aporte del Proyecto (obras, partes y acciones), se superan o no

los límites normados de las concentraciones ambientales de los distintos parámetros.

De esta manera, considerando los receptores sensibles identificados, el área de influencia se define

en este caso, para la normativa primaria de calidad del aire de material particulado respirable fino

(MP2.5) y material particulado respirable (MP10), en base a los SILs (Niveles de Impacto

Significativo), los cuales corresponden a las variaciones en las concentraciones definidas de

contaminantes criterio en el aire ambiental que se consideran intrascendentes en comparación con
los NAAQS [(10)] (Estándares Nacionales de Calidad del Aire) y a la variabilidad propia de las

concentraciones del respectivo contaminante en las mediciones realizadas por redes de monitoreo,

las que de acuerdo al Documento “Evaluación Significancia del Impacto de las Emisiones de un

Proyecto o Actividad en Zonas Saturadas en el Marco del SEIA”, elaborado por el DICTUC para el

Servicio de Evaluación Ambiental (2022), corresponden a los presentados en la Tabla 5-43 del

mencionado informe, tabla que se presenta a continuación.

10 NAAQS: National Ambient Air Quality Standards.

www.dfmconsultores.cl

132
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Tabla 5-43. Criterios recomendados de incremento significativo en la concentración de contaminantes**

**atmosféricos en zonas saturadas.**

|Contaminante|Período|SIL Porcentual USEPA|Incremento Significativo en la Concentración<br>(ug/m3)|
|---|---|---|---|
|MP2.5|24 horas|3,4%|1,7|
|MP2.5|Anual|1,7%|0,3|
|MP10|24 horas|3,3%|5,0|
|MP10|Anual|2,0%|1,0|
|O3|8 horas|1,4%|1,7|
|NO2|1 hora|4,0%|16,0|
|NO2|Anual|1,0%|1,0|
|CO|1 hora|5,0%|1.500,0|
|CO|8 horas|4,9%|488,9|
|SO2|1 hora|4,0%|14,0|
|SO2|24 horas|1,4%|2,0|
|SO2|Anual|2,0%|1,2|

Fuente: Tabla 7-5 Criterios recomendados de incremento significativo en la concentración de contaminantes atmosféricos en zonas

saturadas. Documento “Evaluación Significancia del Impacto de las Emisiones de un Proyecto o Actividad en Zonas Saturadas en el

Marco del SEIA”, elaborado por el DICTUC para el Servicio de Evaluación Ambiental (2022).

Es necesario indicar que aquellas variaciones de concentración por debajo de los valores indicados

en la tabla precedente son considerados estadísticamente no significativos, toda vez que desde un

punto de vista estadístico no se pueden diferenciar de la variabilidad observada en las mediciones.

Es por ello que se han considerado dichos valores para la determinación del área de influencia del

Proyecto.

De esta manera, para el escenario modelado y considerando aquellos contaminantes que presenten

las mayores extensiones geográficas para el área de influencia, considerando los contaminantes de:

material particulado (MP2.5 y MP10) y gaseosos (CO, NO 2 y SO 2 ), se obtienen para los estadígrafos

de periodo horario de NO 2 . De esta manera, en la siguiente figura, se presenta el área de influencia

considerada para el proyecto, conforme a lo indicado anteriormente.

www.dfmconsultores.cl

133
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-67. Área de Influencia Proyecto para Normas Primarias de Calidad de Aire.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

134
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

**Figura 5-68. Área de Influencia Proyecto para Normas Secundarias de Calidad de Aire.**

Fuente: Elaboración propia.

Respecto a la normativa secundaria, aplicable en este caso para el material particulado

sedimentable (MPS), se ha considerado de manera conservadora el 2% del valor de la norma

mensual de referencia utilizada (Norma de Provincia de Buenos Aires).

www.dfmconsultores.cl

135
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

##### 6 CONCLUSIONES

###### 6.1 Modelación de Dispersión de Contaminantes

De los resultados obtenidos se concluye que, de forma general, los aportes netos del proyecto sobre

los receptores de interés no generan impactos significativos en las normas primarias de calidad del

aire al no superar sus valores normativos.

 - Para el Material Particulado fino respirable (MP2.5), se observa que los aportes del del

proyecto sobre los receptores de interés no superan el 9,1% de la norma de este

contaminante en periodo diario en el receptor de medio humano “R_6”, mientras que, para

periodo anual, los valores no sobrepasan el 7,1% de la normativa respectiva en el mismo

receptor de medio humano.

 - Para el Material Particulado respirable (MP10), se observa que los aportes del del proyecto

sobre los receptores de interés no superan el 22,3% de la norma de este contaminante en

periodo diario en el receptor de medio humano “R_6”, mientras que, para periodo anual,

los valores no sobrepasan el 22,3% de la normativa respectiva en el mismo receptor de

medio humano.

 - Para el Material Particulado Sedimentable (MPS), se observa que los aportes del del

proyecto sobre los receptores de interés no superan el 18,9% de la norma de este

contaminante en periodo mensual en el receptor de fauna “RF_3”, mientras que, para

periodo anual, los valores no sobrepasan el 17,5% de la normativa respectiva en el mismo

receptor de fauna.

 - Para el Monóxido de Carbono (CO), se observa que los aportes del del proyecto sobre los

receptores de interés no superan el 0,54% de la norma de este contaminante en periodo

horario en el receptor de medio humano “R_1”, mientras que, para periodo de 8 horas, los

valores no sobrepasan el 0,24% de la normativa respectiva en el mismo receptor de medio

humano “R_6”.

 - Para el Dióxido de Nitrógeno (NO 2 ) se observa que los aportes del del proyecto sobre los

receptores de interés no superan el 21,2% de la norma de este contaminante en periodo

horario en el receptor de medio humano “R_1”, mientras que, para periodo de 8 horas, los

valores no sobrepasan el 0,92% de la normativa respectiva en el mismo receptor de medio

humano “R_11”.

www.dfmconsultores.cl

136
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

 - Para el Dióxido de Azufre (SO 2 ) en su norma primaria, se observa que los aportes del del

proyecto sobre los receptores de interés no superan el 0,13% de la norma de este

contaminante en periodo horario en el receptor de medio humano “R_4”, mientras que,

para periodo de 24 horas, los valores no sobrepasan el 0,11% de la normativa respectiva en

el mismo receptor de medio humano “R_6”. Para el periodo anual, los valores no

sobrepasan el 0,05% de la normativa respectiva en el mismo receptor de medio humano

“R_2”. Por otra parte, en su norma secundaria, se observa que los aportes del proyecto

sobre los receptores de interés no superan el 0,13% de la norma de este contaminante en

periodo horario, mientras que, para periodo de 24 horas, los valores no sobrepasan el 0,08%

de la normativa respectiva. Para el periodo anual, los valores no sobrepasan el 0,07% de la

normativa, todos evaluados en el receptor de fauna “RF_1”.

Se debe considerar que todos los aportes descritos están acotados únicamente a un periodo de 12

meses asociado a la Fase de Construcción del Proyecto, disminuyendo sus valores durante los 30

años de la Fase de Operación, para la cual están considerados únicamente actividades de

mantenimiento.

###### 6.2 Concentración total esperada

Luego, en cuanto a la concentración total esperada, donde se analiza y cuantifica el impacto de la

implementación y ejecución del proyecto en la estación de monitoreo Casablanca, se concluye que

los aportes del caso proyectado a la concentración ambiental, para los contaminantes de material

particulado respirable (MP10), monóxido de carbono (CO), dióxido de Nitrógeno (NO 2 ) y dióxido de

azufre (SO 2 ), son menores que los valores establecidos para los SILs (Niveles de Impacto

Significativo).

En consecuencia, los aportes del proyecto determinados bajo un escenario conservador de

modelación no tendrán efectos significativos en la calidad del aire en Casablanca.

www.dfmconsultores.cl

137
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

##### 7 APÉNDICE 1: ARCHIVOS DIGITALES MODELACIÓN

En la siguiente tabla se detallan los archivos de entrada y salida de la modelación de calidad del aire

presentada en este estudio. Los archivos se listan según lo indicado en la “Guía para el uso de

modelos de calidad del aire en el SEIA”, considerando los archivos de entrada y salida de los módulos

CALMET, CALPUFF y CALPOST.

**Tabla 7-1. Archivos de modelación entregados.**

|Archivos|Entregado|Observación|
|---|---|---|
|**Archivos CALPUFF:**|**Archivos CALPUFF:**|**Archivos CALPUFF:**|
|- CALPUFF.DAT|NO|Corresponde al archivo CONC.DAT|
|- CALPUFF.LST|SI|-|
|- CALPUFF.INP|SI|-|
|- CONC.DAT|SI|-|
|- DFLX.DAT|SI|-|
|- WFLX.DAT|NO|-|
|- POSTUTCN.INP|SI|-|
|- POSTUTCN.LST|SI|-|
|- PUCONC.DAT|SI|-|
|**Archivos Meteorológicos:**|**Archivos Meteorológicos:**|**Archivos Meteorológicos:**|
|- CALMET.DAT|SI|-Corresponde al archivo:<br>calmetv6_Casablanca_2020.dat|
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

Fuente: Elaboración Propia.

www.dfmconsultores.cl

138
**info@dfmconsultores.cl**

**Proyecto “Parque Solar Fotovoltaico Acuyo”**

Modelación de Dispersión de Contaminantes Atmosféricos

Diciembre 2023

De acuerdo a lo señalado en el artículo 14 bis de la Ley N°19.300 sobre Bases Generales del Medio

Ambiente y en los artículos 21 inciso 3° y 29 inciso 1° del Decreto Supremo N°40 de 2012, Ministerio

del Medio Ambiente, Reglamento del Sistema de Evaluación de Impacto Ambiental, se informa que

dada la naturaleza de los documentos los archivos digitales del Modelo Calpuff y Modelo

Meteorológico WRF, no es posible agregarlos al expediente electrónico, motivo por el cual dicha

información se encuentra disponible para el público en general en las oficinas del Servicio de

Evaluación Ambiental de Valparaíso, ubicada en calle Prat 827, Oficina 301, Valparaíso. Los

interesados en obtener dicha documentación deben comunicarse con Oficina de Información y

Atención Ciudadana del SEA, ingresando su requerimiento a través del siguiente link:

[www.sea.gob.cl](http://www.sea.gob.cl/)

www.dfmconsultores.cl

139
**info@dfmconsultores.cl**

Acuse de recibo para entrega de archivos de gran tamaño.

Estimado Sr. José Gabriel Arosa Gómez, representante legal de FONTUS SCL III SpA

Mediante el presente acusamos recibo, en la fecha y hora de este correo, de los documentos que se
detallan a continuación, los cuales cumplen con las condiciones necesarias para la entrega de
documentos de gran tamaño al SEA:

✓ Antecedentes del proyecto:

 - Nombre del proyecto: Proyecto Solar Fotovoltaico Acuyo.

 - Modalidad de ingreso (EIA, DIA, Adenda): DIA.

Antecedentes de los archivos de gran tamaño recibidos:

|N°|Antecedentes de los archivos<br>de gran tamaño recibidos.|Nombre y Extensión del Archivo.|Tamaño del<br>Archivo<br>(>100 Mb)|
|---|---|---|---|
|1|Carpeta comprimida|2161081212 - Parque Solar Fotovoltaico<br>Acuyo.|7,17 GB|

El detalle de los archivos contenidos en la respectiva carpeta comprimida, que se mencionan antes, se
detalla a continuación:

|Nivel 1|Nivel 2|Nivel 3|
|---|---|---|
|2161081212 - Parque Solar<br>Fotovoltaico Acuyo.|01 CALMET|calmetv6_Casablanca_2020.dat|
|2161081212 - Parque Solar<br>Fotovoltaico Acuyo.|01 CALMET|GEO.DAT|
|2161081212 - Parque Solar<br>Fotovoltaico Acuyo.|01 CALMET|namelist.input|
|2161081212 - Parque Solar<br>Fotovoltaico Acuyo.|01 CALMET|namelist.wps|
|2161081212 - Parque Solar<br>Fotovoltaico Acuyo.|02 CALPUFF|CALPUFF.INP|
|2161081212 - Parque Solar<br>Fotovoltaico Acuyo.|02 CALPUFF|CALPUFF.LST|
|2161081212 - Parque Solar<br>Fotovoltaico Acuyo.|02 CALPUFF|CONC.DAT|
|2161081212 - Parque Solar<br>Fotovoltaico Acuyo.|02 CALPUFF|DFLX.DAT|
|2161081212 - Parque Solar<br>Fotovoltaico Acuyo.|02 CALPUFF|POSTUTCN.INP|
|2161081212 - Parque Solar<br>Fotovoltaico Acuyo.|02 CALPUFF|POSTUTCN.LST|
|2161081212 - Parque Solar<br>Fotovoltaico Acuyo.|02 CALPUFF|PUCONC.DAT|
|2161081212 - Parque Solar<br>Fotovoltaico Acuyo.|02 CALPUFF|WFLX.DAT|

Saluda cordialmente a Ud.,

Rossana Chávez Zuñiga
Oficial de Partes

SEA Región de Valparaíso

Página **1** de **1**

**Envío acuse de recibo para carga de archivos de gran tamaño del Proyecto "Parque**
**Solar Fotovoltaico Acuyo"**

Oficina Partes SEA Valparaíso <oficinapartes.sea.valparaiso@sea.gob.cl>

Mié 17/01/2024 11:36

Para:jose.arosa@prime-energia.com <jose.arosa@prime-energia.com>;framirez@ambec.cl <framirez@ambec.cl>
CC:mastudillo@ambec.cl <mastudillo@ambec.cl>;hvasquez@ambec.cl <hvasquez@ambec.cl>;Sandra Fuentes Troncoso
<sfuentes.5@sea.gob.cl>;Fanny Soledad Arias Lira <fanny.arias@sea.gob.cl>;Rossana Chavez Zuñiga
<rossana.chavez@sea.gob.cl>

1 archivos adjuntos (102 KB)

Acuse recibo archivos 200MB PSF Acuyo v(A) SFT 20240117.pdf;

Señor

José Gabriel Arosa

Representante Legal

FONTUS SCL III SpA

Presente.

De mi consideración:

Mediante el presente acusamos recibo, en la fecha y hora de este correo, de los documentos que se
detallan en el archivo adjunto, los cuales cumplen con las condiciones necesarias para la entrega
de documentos de gran tamaño al SEA, DIA Proyecto "Parque Solar Fotovoltaico Acuyo".

Saluda atentamente,

_"Esta cuenta no está habilitada para recibir documentos o mensajes, por lo que se solicita que para "Acuso_
_recibo", responda a "todos"; y para consultas de cualquier tipo se dirija a contacto.sea.gob.cl"_

**Oficina de Partes**

Dirección Regional de Valparaíso

+5632 2219928 Anexo 201

**Servicio de Evaluación Ambiental**

**Gobierno de Chile**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4-1.: Resumen de emisiones. Año 1 de la Fase de Construcción del Proyecto.****

| Actividad | Emisión (t/año) | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **MP2.5** | **MP10** | **MPS** | **CO** | **NOx** | **COVs** | **SO2 ** | **NH3 ** |
| Movimiento de Tierra | 1,050 | 4,516 | 11,912 |  |  |  |  |  |
| Maquinaria | 0,811 | 0,811 | 0,811 | 6,273 | 8,358 | 0,887 | 0,014 | 0,004 |
| Grupos electrógenos | 0,368 | 0,368 | 0,368 | 1,127 | 5,230 | 0,427 | 0,344 |  |
| Resuspensión de polvo por<br>transporte | 1,277 | 11,349 | 41,432 |  |  |  |  |  |
| Combustión por transporte | 0,051 | 0,051 | 0,051 | 0,590 | 2,498 | 0,105 | 0,003 | 0,001 |
| **Total** | **3,556** | **17,094** | **54,573** | **7,990** | **16,086** | **1,419** | **0,360** | **0,005** |

**Tabla 5-1.: Configuración parámetros principales WRF.****

| Parámetro | Valor |
| --- | --- |
| **Dominio** | **Dominio** |
| Resolución horizontal | 1 km |
| Proyección | Lambert |
| Dimensión | 67x67x44 |
| Número de niveles verticales | 44 |
| Niveles verticales (eta) | 0.000000, 0.051578, 0.101822, 0.150735, 0.198315, 0.244562, 0.289477,<br>0.333059,<br>0.375309,<br>0.416226,<br>0.455810, 0.494062, 0.530982, 0.566569, 0.600823, 0.633745, 0.665334,<br>0.695591, 0.724515, 0.752107, 0.778366, 0.803292, 0.826886, 0.849148,<br>0.870076, 0.889673, 0.907937, 0.923302, 0.937101, 0.949333, 0.960000,<br>0.969101, 0.976635, 0.982603, 0.987005, 0.989841, 0.991111, 0.992381,<br>0.993651, 0.994921, 0.996190, 0.997460, 0.998730, 1.000000 |
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

**Tabla 5-2.: Concentración media anual de MP10 en años 2020 - 2022, estación de monitoreo Casablanca.****

| Estación | Año | Concentración Media Anual MP10<br>(μg/m3N) |
| --- | --- | --- |
| Casablanca | 2020 | 34 |
| Casablanca | 2021 | 32 |
| Casablanca | 2022 | 30 |

**Tabla 5-3.: Principales índices evaluación cambio climático. Región de Valparaíso, provincia de Valparaíso,****

| Índice | Periodo | Valor |
| --- | --- | --- |
| Temperatura media anual (°C) | Presente | 13,80 |
| Temperatura media anual (°C) | Futuro | 14,89 |
| Temperatura media anual (°C) | Cambio (Futuro - Presente) | 1,09 |
| Precipitación acumulada anual (mm) | Presente | 474,43 |
| Precipitación acumulada anual (mm) | Futuro | 386,64 |
| Precipitación acumulada anual (mm) | Cambio (Futuro - Presente) | -87,78 |
| Velocidad viento promedio anual<br>(m/s) | Presente | 2,33 |
| Velocidad viento promedio anual<br>(m/s) | Futuro | 2,30 |
| Velocidad viento promedio anual<br>(m/s) | Cambio (Futuro - Presente) | -0,03 |

**Tabla 5-4.: Coordenadas de Ubicación, Estación de Monitoreo Casablanca.****

| Nombre | Variables Meteorológicas<br>Registradas | Periodo monitoreado<br>considerado para este<br>estudio | Coordenadas (Datum WGS84) | Col5 |
| --- | --- | --- | --- | --- |
| **Nombre** | **Variables Meteorológicas**<br>**Registradas** | **Periodo monitoreado**<br>**considerado para este**<br>**estudio** | **Este (m)** | **Norte (m)** |
| Casablanca | Velocidad del Viento (m/s) | Enero 2020 a<br>Diciembre 2022 | 278.002 | 6.309.012 |
| Casablanca | Dirección del Viento (°) | Dirección del Viento (°) | Dirección del Viento (°) | Dirección del Viento (°) |
| Casablanca | Temperatura del Aire (°C) | Temperatura del Aire (°C) | Temperatura del Aire (°C) | Temperatura del Aire (°C) |
| Casablanca | Humedad Relativa (%) | Humedad Relativa (%) | Humedad Relativa (%) | Humedad Relativa (%) |
| Casablanca | Precipitación Acumulada (mm) | Precipitación Acumulada (mm) | Precipitación Acumulada (mm) | Precipitación Acumulada (mm) |
| Casablanca | Presión Atmosférica (mmHg) | Presión Atmosférica (mmHg) | Presión Atmosférica (mmHg) | Presión Atmosférica (mmHg) |
| Casablanca | Radiación Solar (W/m2) | Radiación Solar (W/m2) | Radiación Solar (W/m2) | Radiación Solar (W/m2) |

**Tabla 5-5.: Equipos y principios de operación registro de variables meteorológicas.****

| Nombre Estación | Parámetro | Unidad | Equipo - Serie | Principio de Operación |
| --- | --- | --- | --- | --- |
| Casablanca | Velocidad del<br>Viento | m/s | Young std 5103 - 57026 | Generación de pulso /<br>potenciómetro |
| Casablanca | Dirección del<br>Viento | ° | Young std 5103 - 57026 | Generación de pulso /<br>potenciómetro |
| Casablanca | Temperatura | °C | Vaisala, HMP155 - E4010123 | Sensor polinomial |
| Casablanca | Humedad Relativa | % | Vaisala, HMP155 - E4010123 | Sensor polinomial |
| Casablanca | Precipitación | mm | Texas TR525M - 47611-511 | Tipping Bucket |
| Casablanca | Presión<br>Atmosférica | mmHg | Vaisala, PTB110 - F4540027 | Sensor capacitivo |
| Casablanca | Radiación Solar | W/m2 | Licor Li200R - PY77315 | Detector fotovoltaico |

**Tabla 5-6.: Resumen de información Velocidad del Viento. Estación Casablanca.****

| Parámetro | Variable | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2020** | **2021** | **2022** |
| Velocidad de Viento (m/s) | Promedio | 1,8 | 1,9 | 1,8 |
| Velocidad de Viento (m/s) | Máximo | 9,8 | 8,9 | 9,0 |
| Velocidad de Viento (m/s) | Mínimo | 0,0 | 0,0 | 0,0 |
| Porcentaje de Calmas (%) | Porcentaje de Calmas (%) | 12,2 | 11,7 | 12,8 |
| Datos Válidos (%) | Datos Válidos (%) | 98,6% | 100,0% | 100,0% |

**Tabla 5-7.: Frecuencia de distribución Velocidad y Dirección del Viento. Enero 2020 a diciembre de 2022. Estación Casablanca.****

| Dirección | Col2 | Distribución Porcentual de Velocidad del Viento (m/s) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección** | **Dirección** | **0,50 - 2,10** | **2,10 - 3,60** | **3,60 - 5,70** | **5,70 - 8,80** | **8,80 - 11,10** | **>= 11,10** | **Total (%)** |
| 348,75 - 11,25 | N | 2,67% | 1,09% | 0,70% | 0,14% | 0,01% | 0,00% | 4,61% |
| 11,25 - 33,75 | NNE | 1,79% | 0,72% | 0,49% | 0,06% | 0,00% | 0,00% | 3,06% |
| 33,75 - 56,25 | NE | 1,87% | 0,23% | 0,06% | 0,00% | 0,00% | 0,00% | 2,15% |
| 56,25 - 78,75 | ENE | 2,86% | 0,12% | 0,01% | 0,00% | 0,00% | 0,00% | 3,00% |
| 78,75 - 101,25 | E | 5,02% | 0,12% | 0,01% | 0,00% | 0,00% | 0,00% | 5,15% |
| 101,25 - 123,75 | ESE | 5,52% | 0,13% | 0,02% | 0,00% | 0,00% | 0,00% | 5,66% |
| 123,75 - 146,25 | SE | 4,12% | 0,10% | 0,01% | 0,00% | 0,00% | 0,00% | 4,22% |
| 146,25 - 168,75 | SSE | 2,68% | 0,27% | 0,03% | 0,00% | 0,00% | 0,00% | 2,98% |
| 168,75 - 191,25 | S | 2,22% | 0,63% | 0,15% | 0,00% | 0,00% | 0,00% | 2,99% |
| 191,25 - 213,75 | SSW | 2,39% | 1,11% | 0,83% | 0,18% | 0,00% | 0,00% | 4,51% |
| 213,75 - 236,25 | SW | 2,10% | 2,10% | 2,30% | 0,47% | 0,00% | 0,00% | 6,96% |
| 236,25 - 258,75 | WSW | 2,22% | 2,61% | 3,80% | 0,61% | 0,00% | 0,00% | 9,24% |
| 258,75 - 281,25 | W | 3,27% | 2,15% | 1,60% | 0,03% | 0,00% | 0,00% | 7,05% |
| 281,25 - 303,75 | WNW | 5,35% | 2,21% | 1,62% | 0,05% | 0,00% | 0,00% | 9,23% |
| 303,75 - 326,25 | NW | 6,80% | 2,13% | 0,94% | 0,11% | 0,00% | 0,00% | 9,97% |
| 326,25 - 348,75 | NNW | 4,58% | 1,68% | 0,61% | 0,10% | 0,00% | 0,00% | 6,97% |
| Sub-Total | Sub-Total | 55,45% | 17,39% | 13,17% | 1,74% | 0,02% | 0,00% | 87,76% |
| Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | 12,24% |

**Tabla 5-8.: Resumen de información Temperatura Observada. Estación Casablanca.****

| Parámetro | Variable | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2020** | **2021** | **2022** |
| Temperatura (°C) | Promedio | 14,2 | 13,0 | 12,9 |
| Temperatura (°C) | Máximo | 35,7 | 33,4 | 33,3 |
| Temperatura (°C) | Mínimo | -1,8 | -5,4 | -5,1 |
| Datos Válidos (%) | Datos Válidos (%) | 98,6% | 100,0% | 100,0% |

**Tabla 5-9.: Resumen de información Humedad Relativa Observada. Estación Casablanca.****

| Parámetro | Variable | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2020** | **2021** | **2022** |
| Humedad Relativa (%) | Promedio | 72,1 | 76,0 | 78,0 |
| Humedad Relativa (%) | Máximo | 100,0 | 100,0 | 100,0 |
| Humedad Relativa (%) | Mínimo | 10,0 | 12,3 | 13,7 |
| % Datos Válidos | % Datos Válidos | 97,7% | 100,0% | 100,0% |

**Tabla 5-10.: Resumen de información Precipitación acumulada Observada. Estación Casablanca.****

| Parámetro | Variable | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2020** | **2021** | **2022** |
| Precipitación Acumulada (mm) | Máximo acumulado diario | 49,0 | 36,7 | 35,5 |
| Precipitación Acumulada (mm) | Mínimo acumulado mensual | 0,0 | 0,0 | 0,0 |
| Precipitación Acumulada (mm) | Máximo acumulado mensual | 140,9 | 43,7 | 122,1 |
| Precipitación Acumulada (mm) | Acumulado anual | 243,1 | 145,5 | 266,0 |
| % Datos Válidos | % Datos Válidos | 98,6% | 100,0% | 100,0% |

**Tabla 5-11.: Resumen de información Presión atmosférica Observada. Estación Casablanca.****

| Parámetro | Variable | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2020** | **2021** | **2022** |
| Presión Atmosférica (mmHg) | Promedio | 739,6 | 739,5 | 739,6 |
| Presión Atmosférica (mmHg) | Máximo | 748,0 | 747,8 | 748,3 |
| Presión Atmosférica (mmHg) | Mínimo | 734,0 | 734,0 | 733,0 |
| % Datos Válidos | % Datos Válidos | 98,6% | 100,0% | 99,4% |

**Tabla 5-12.: Resumen de información Radiación solar Observada. Estación Casablanca.****

| Parámetro | Variable | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2020** | **2021** | **2022** |
| Radiación Solar (W/m2) | Promedio | 189,5 | 185,6 | 179,6 |
| Radiación Solar (W/m2) | Máximo | 970,8 | 950,9 | 987,5 |
| Radiación Solar (W/m2) | Mínimo | 0,0 | 0,0 | 0,0 |
| % Datos Válidos | % Datos Válidos | 98,6% | 99,9% | 100,0% |

**Tabla 5-13.: Resumen de información Velocidad del Viento Modelado. Estación Casablanca.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2020** |
| Velocidad de Viento (m/s) | Promedio | 2,51 |
| Velocidad de Viento (m/s) | Mínimo | 0,01 |
| Velocidad de Viento (m/s) | Máximo | 11,84 |
| Velocidad de Viento (m/s) | Porcentaje de Calmas (%) | 7,2% |
| Velocidad de Viento (m/s) | Datos Válidos (%) | 100% |

**Tabla 5-14.: Frecuencia de distribución Velocidad y Dirección del Viento Modelada. Enero a diciembre de 2020. Estación Casablanca.****

| Dirección | Col2 | Distribución Porcentual de Velocidad del Viento (m/s) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección** | **Dirección** | **0,50 - 2,10** | **2,10 - 3,60** | **3,60 - 5,70** | **5,70 - 8,80** | **8,80 - 11,10** | **>= 11,10** | **Total (%)** |
| 348,75 - 11,25 | N | 3,7% | 1,2% | 0,5% | 0,3% | 0,1% | 0,0% | 5,7% |
| 11,25 - 33,75 | NNE | 4,2% | 0,8% | 0,2% | 0,0% | 0,0% | 0,0% | 5,2% |
| 33,75 - 56,25 | NE | 4,6% | 0,2% | 0,0% | 0,0% | 0,0% | 0,0% | 4,8% |
| 56,25 - 78,75 | ENE | 5,4% | 0,3% | 0,0% | 0,0% | 0,0% | 0,0% | 5,7% |
| 78,75 - 101,25 | E | 4,1% | 0,4% | 0,1% | 0,0% | 0,0% | 0,0% | 4,5% |
| 101,25 - 123,75 | ESE | 1,8% | 0,3% | 0,2% | 0,1% | 0,0% | 0,0% | 2,3% |
| 123,75 - 146,25 | SE | 1,1% | 0,2% | 0,1% | 0,0% | 0,0% | 0,0% | 1,4% |
| 146,25 - 168,75 | SSE | 0,9% | 0,3% | 0,0% | 0,0% | 0,0% | 0,0% | 1,3% |
| 168,75 - 191,25 | S | 1,0% | 0,8% | 0,4% | 0,5% | 0,0% | 0,0% | 2,8% |
| 191,25 - 213,75 | SSW | 1,4% | 1,8% | 3,3% | 3,0% | 0,1% | 0,0% | 9,6% |
| 213,75 - 236,25 | SW | 0,8% | 1,6% | 4,5% | 3,7% | 0,3% | 0,0% | 10,9% |
| 236,25 - 258,75 | WSW | 1,0% | 1,7% | 5,1% | 0,4% | 0,0% | 0,0% | 8,2% |
| 258,75 - 281,25 | W | 3,1% | 1,7% | 0,7% | 0,0% | 0,0% | 0,0% | 5,5% |
| 281,25 - 303,75 | WNW | 6,6% | 1,3% | 0,5% | 0,1% | 0,0% | 0,0% | 8,4% |
| 303,75 - 326,25 | NW | 7,0% | 1,3% | 0,9% | 0,1% | 0,0% | 0,0% | 9,3% |
| 326,25 - 348,75 | NNW | 4,6% | 0,9% | 1,3% | 0,3% | 0,0% | 0,0% | 7,1% |
| Sub-Total | Sub-Total | 51,3% | 14,8% | 17,8% | 8,4% | 0,5% | 0,1% | 92,8% |
| Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | 7,2% |

**Tabla 5-15.: Resumen de información Temperatura Modelada. Estación Casablanca.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2020** |
| Temperatura (°C) | Promedio | 15,52 |
| Temperatura (°C) | Mínimo | 2,78 |
| Temperatura (°C) | Máximo | 33,49 |
| Temperatura (°C) | Datos Válidos (%) | 100% |

**Tabla 5-16.**

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2020** |
| Altura Capa de Mezcla (m) | Promedio | 261,35 |
| Altura Capa de Mezcla (m) | Mínimo | 10,00 |
| Altura Capa de Mezcla (m) | Máximo | 1.840,15 |
| Altura Capa de Mezcla (m) | % Datos Válidos | 100% |

**Tabla 5-17.: Métricas estadísticas recomendables en el Análisis de Incertidumbre para las variables****

| Estadístico o Medida de Error | Velocidad Viento | Temperatura |
| --- | --- | --- |
| Sesgo | [-2,5; 2,5] m/s | [-4,0; 4,0] °C |
| Error cuadrático medio (ECM) | ≤ 3,5 m/s | ≤ 4,5 °C |
| r | > 0,6 | > 0,8 |

**Tabla 5-18.: Estadígrafos de Dispersión para Velocidad del Viento y Temperatura. Estación Casablanca.****

| Medida de Error | Estación Casablanca | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Medida de Error** | **Velocidad Viento** | **Velocidad Viento** | **Temperatura** | **Temperatura** |
| **Medida de Error** | **Serie de Tiempo** | **Ciclo Diario** | **Serie de Tiempo** | **Ciclo Diario** |
| Sesgo | 0,68 | 0,69 | 1,28 | 1,29 |
| ECM | 1,46 | 0,85 | 4,19 | 2,26 |
| r | 0,77 | 0,99 | 0,80 | 0,98 |

**Tabla 5-19.: Normas primarias de calidad del aire.****

| Contaminante | Decreto Aplicable | Norma | Col4 | Periodo de Evaluación de Cumplimiento de<br>Norma |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Decreto Aplicable** | **Valor** | **Unidad** | **Unidad** |
| Material Particulado<br>Respirable Fino (MP2.5) | Decreto Supremo<br>N°12/2011 | 50 | μg/m3 | Percentil 98 de las concentraciones de 24<br>horas |
| Material Particulado<br>Respirable Fino (MP2.5) | Decreto Supremo<br>N°12/2011 | 20 | 20 | Concentración anual |
| Material Particulado<br>Respirable (MP10) | Decreto Supremo<br>N°12/2022 | 130 | μg/m3N | Percentil 98 de las concentraciones de 24<br>horas |
| Material Particulado<br>Respirable (MP10) | Decreto Supremo<br>N°12/2022 | 50 | 50 | Concentración anual |
| Monóxido de Carbono<br>(CO) | Decreto Supremo<br>N°115/2002 | 30 | mg/m3N | Percentil 99 de los máximos diarios de<br>concentración de 1 hora |
| Monóxido de Carbono<br>(CO) | Decreto Supremo<br>N°115/2002 | 10 | 10 | Percentil 99 de los máximos diarios de<br>concentración de 8 horas |
| Dióxido de Nitrógeno<br>(NO2) | Decreto Supremo<br>N°114/2002 | 400 | μg/m3N | Percentil 99 de los máximos diarios de<br>concentración de 1 hora |
| Dióxido de Nitrógeno<br>(NO2) | Decreto Supremo<br>N°114/2002 | 100 | 100 | Concentración anual |
| Dióxido de Azufre (SO2) <br>(Norma primaria de<br>calidad del aire) | Decreto Supremo<br>N°104/2019 | 350 | μg/m3N | Percentil 99 de las concentraciones de 1 hora. |
| Dióxido de Azufre (SO2) <br>(Norma primaria de<br>calidad del aire) | Decreto Supremo<br>N°104/2019 | 150 | 150 | Percentil 99 de las concentraciones de 24<br>horas |
| Dióxido de Azufre (SO2) <br>(Norma primaria de<br>calidad del aire) | Decreto Supremo<br>N°104/2019 | 60 | 60 | Concentración anual |

**Tabla 5-20.: Normas secundarias de calidad del aire.****

| Contaminante | Decreto Aplicable | Norma | Col4 | Periodo de Evaluación de Cumplimiento de<br>Norma |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Decreto Aplicable** | **Valor** | **Unidad** | **Unidad** |
| Material Particulado<br>Sedimentable (MPS) | Confederación Suiza,<br>Recursos Naturales | 200 | mg/m2-día | Media aritmética anual |
| Material Particulado<br>Sedimentable (MPS) | República de Argentina | 333 | mg/m2-día | Media aritmética mensual |
| Dióxido de Azufre (SO2) <br>(Norma secundaria de<br>calidad del aire) | Decreto Supremo<br>N°22/2010 | 700 | μg/m3N | Percentil 99,73 de las concentraciones de 1<br>hora. Zona Sur. |
| Dióxido de Azufre (SO2) <br>(Norma secundaria de<br>calidad del aire) | Decreto Supremo<br>N°22/2010 | 260 | 260 | Percentil 99,7 de las concentraciones de 24<br>horas. Zona Sur. |
| Dióxido de Azufre (SO2) <br>(Norma secundaria de<br>calidad del aire) | Decreto Supremo<br>N°22/2010 | 60 | 60 | Concentración anual. Zona Sur. |

**Tabla 5-21.: Inventario de Equipos y Técnicas de Medición.****

| Nombre<br>Estación | Parámetro | Unidad | Equipo - Serie | Principio de Operación |
| --- | --- | --- | --- | --- |
| Casablanca | Material Particulado<br>Respirable (MP10) | μg/m3N | Tisch Enviromental -<br>P3829X | Gravimetría de Alto<br>Volumen (Hi Vol) |
| Casablanca | Monóxido de Carbono (CO) | ppm | Teledyne 300E - 1308 | IRND con Filtro gaseoso de<br>correlación |
| Casablanca | Dióxido de Nitrógeno (NO2) | ppb | Teledyne T200 - 155 | Luminescencia Química |
| Casablanca | Dióxido de Azufre (SO2) | ppb | Teledyne 100E - 266 | Fluorescencia de pulso UV |

**Tabla 5-22.: Caracterización de Estación de Monitoreo de Calidad del Aire.****

| Nombre | Parámetros de Calidad del Aire<br>Registrados | Periodo monitoreado<br>considerado para este<br>estudio | Coordenadas (Datum<br>WGS84) | Col5 |
| --- | --- | --- | --- | --- |
| **Nombre** | **Parámetros de Calidad del Aire**<br>**Registrados** | **Periodo monitoreado**<br>**considerado para este**<br>**estudio** | **Este (m)** | **Norte (m)** |
| Casablanca | Material Particulado Respirable<br>(MP10) | Enero 2020 a Diciembre<br>2022 | 278.002 | 6.309.012 |
| Casablanca | Monóxido de Carbono (CO) | Monóxido de Carbono (CO) | Monóxido de Carbono (CO) | Monóxido de Carbono (CO) |
| Casablanca | Dióxido de Nitrógeno (NO2) | Dióxido de Nitrógeno (NO2) | Dióxido de Nitrógeno (NO2) | Dióxido de Nitrógeno (NO2) |
| Casablanca | Dióxido de Azufre (SO2) | Dióxido de Azufre (SO2) | Dióxido de Azufre (SO2) | Dióxido de Azufre (SO2) |

**Tabla 5-23.: Resultados Monitoreo de MP10. Estación Casablanca** **[(6)]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2020** | **2021** | **2022** |
| MP10 (μg/m3N) | Percentil 98 diario | 74 | 80 | 86 |
| MP10 (μg/m3N) | Media anual | 34 | 32 | 30 |
| MP10 (μg/m3N) | Media trianual | 32 | 32 | 32 |

**Tabla 5-24.: Comparación de Monitoreo de MP10 con Normativa. Estación Casablanca.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP10 | 1 de enero de 2022 - 31<br>diciembre 2022 | Percentil 98 de la<br>concentración media diaria | 86 | 130 | μg/m3N | 66,2% |
| MP10 | 1 de enero de 2020 - 31<br>diciembre 2022 | Concentración media trianual | 32 | 50 | μg/m3N | 64,0% |

**Tabla 5-25.: Resultados Monitoreo de CO. Estación Casablanca** **[(7)]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2020** | **2021** | **2022** |
| CO (mg/m3N) | Percentil 99 de los máximos diarios de<br>concentración horaria | 1,3 | 1,3 | 1,2 |
| CO (mg/m3N) | Promedio trianual percentil 99 de los máximos<br>diarios de concentración horaria | 1,3 | 1,3 | 1,3 |
| CO (mg/m3N) | Percentil 99 de los máximos diarios de<br>concentración de 8 horas | 0,8 | 1,0 | 0,8 |
| CO (mg/m3N) | Promedio trianual percentil 99 de los máximos<br>diarios de concentración de 8 horas | 0,9 | 0,9 | 0,9 |

**Tabla 5-26.: Comparación de Monitoreo de CO con Normativa. Estación Casablanca.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| CO | 1 de enero de 2020 -<br>31 diciembre 2022 | Percentil 99 de los<br>máximos diarios de<br>concentración de 1 hora | 1,3 | 30 | mg/m3N | 4,4% |
| CO | 1 de enero de 2020 -<br>31 diciembre 2022 | Percentil 99 de los<br>máximos diarios de<br>concentración de 8 horas | 0,9 | 10 | mg/m3N | 8,9% |

**Tabla 5-27.: Resultados Monitoreo de NO** **2** **. Estación Casablanca.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2020** | **2021** | **2022** |
| NO2 (μg/m3N) | Percentil 99 de los máximos diarios de concentración<br>horaria | 45,1 | 60,1 | 50,7 |
| NO2 (μg/m3N) | Promedio trianual percentil 99 de los máximos diarios de<br>concentración horaria | 52,6 | 52,6 | 52,6 |
| NO2 (μg/m3N) | Media anual | 9,4 | 11,3 | 11,3 |
| NO2 (μg/m3N) | Media trianual | 11,3 | 11,3 | 11,3 |

**Tabla 5-28.: Comparación de Monitoreo de NO** **2** **con Normativa. Estación Casablanca.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- |
| NO2 | 1 de enero de 2020 - 31<br>diciembre 2022 | Percentil 99 de los máximos<br>diarios de concentración de<br>1 hora | 52,6 | 400 | μg/m3N | 13,1% |
| NO2 | 1 de enero de 2020 - 31<br>diciembre 2022 | Concentración media<br>trianual | 11,3 | 100 | μg/m3N | 11,3% |

**Tabla 5-29.: Resultados Monitoreo de SO** **2** **. Estación Casablanca** **[(8)]** **.****

| Contaminante | Parámetro | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Parámetro** | **2020** | **2021** | **2022** |
| SO2 (μg/m3N) | Percentil 99 de concentración horaria | 15,6 | 18,2 | 5,2 |
| SO2 (μg/m3N) | Promedio trianual percentil 99 de concentración horaria | 13,0 | 13,0 | 13,0 |
| SO2 (μg/m3N) | Percentil 99 de concentración diaria | 2,6 | 2,6 | 2,6 |
| SO2 (μg/m3N) | Promedio trianual percentil 99 de concentración diaria | 2,6 | 2,6 | 2,6 |
| SO2 (μg/m3N) | Media anual | 0,0 | 2,6 | 2,6 |
| SO2 (μg/m3N) | Media trianual | 1,3 | 1,3 | 1,3 |

**Tabla 5-30.: Comparación de Monitoreo de SO** **2** **con Normativa. Estación Casablanca.****

| Contaminante | Periodo | Estadígrafo | Valor | Norma | Unidad | Porcentaje de<br>la Norma |
| --- | --- | --- | --- | --- | --- | --- |
| SO2 | 1 de enero de 2020 - 31<br>diciembre 2022 | Percentil 99 de concentración<br>horaria | 13,0 | 350 | μg/m3N | 3,7% |
| SO2 | 1 de enero de 2020 - 31<br>diciembre 2022 | Percentil 99 de la concentración<br>media diaria | 2,6 | 150 | μg/m3N | 1,7% |
| SO2 | 1 de enero de 2020 - 31<br>diciembre 2022 | Concentración media trianual | 1,3 | 60 | μg/m3N | 2,2% |

**Tabla 5-31.: Resumen Línea de Base de Calidad del Aire.****

| Contaminante | Estadígrafo | Norma | Unidad | Estación Casablanca | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Estadígrafo** | **Norma** | **Unidad** | **Valor** | **Porcentaje de la Norma** |
| MP10 | P 98 - 24 horas | 130 | μg/m3N | 86 | 66,2% |
| MP10 | Media Trianual | 50 | μg/m3N | 32 | 64,0% |
| CO | P 99 - 1 hora | 30 | mg/m3N | 1,3 | 4,4% |
| CO | P 99 - 8 horas | 10 | mg/m3N | 0,9 | 8,9% |
| NO2 | P 99 - 1 hora | 400 | μg/m3N | 52,6 | 13,1% |
| NO2 | Media Trianual | 100 | μg/m3N | 11,3 | 11,3% |
| SO2 | P 99 - 1 hora | 350 | μg/m3N | 13,0 | 3,7% |
| SO2 | P 99 - 24 horas | 150 | μg/m3N | 2,6 | 1,7% |
| SO2 | Media Anual | 60 | μg/m3N | 1,3 | 2,2% |

**Tabla 5-32.: Características Fuentes Emisoras de contaminantes atmosféricos.****

| ID Fuente | Descripción | Tipo de Fuente | Dimensión<br>característica9 | Col5 | Tasa de emisión Año 1 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID Fuente** | **Descripción** | **Tipo de Fuente** | **- ** | **Unidad** | **MP2.5** | **MP10** | **MPS** | **CO** | **NO** | **NO2 ** | **SO2 ** | **Unidad** |
| PFV_1_1 | Parque Fotovoltaico 1_1 | AREAL | 138.359 | m2 | 1,672E-07 | 5,207E-07 | 1,213E-06 | 4,980E-07 | 4,152E-07 | 7,073E-08 | 1,115E-09 | g/s-m2 |
| PFV_1_2 | Parque Fotovoltaico 1_2 | AREAL | 53.127 | m2 | 1,672E-07 | 5,207E-07 | 1,213E-06 | 4,980E-07 | 4,152E-07 | 7,073E-08 | 1,115E-09 | g/s-m2 |
| PFV_1_3 | Parque Fotovoltaico 1_3 | AREAL | 9.084 | m2 | 1,672E-07 | 5,207E-07 | 1,213E-06 | 4,980E-07 | 4,152E-07 | 7,073E-08 | 1,115E-09 | g/s-m2 |
| PFV_1_4 | Parque Fotovoltaico 1_4 | AREAL | 43.540 | m2 | 1,672E-07 | 5,207E-07 | 1,213E-06 | 4,980E-07 | 4,152E-07 | 7,073E-08 | 1,115E-09 | g/s-m2 |
| PFV_2 | Parque Fotovoltaico 2 | AREAL | 376.863 | m2 | 1,672E-07 | 5,207E-07 | 1,213E-06 | 4,980E-07 | 4,152E-07 | 7,073E-08 | 1,115E-09 | g/s-m2 |
| PFV_3_1 | Parque Fotovoltaico 3_1 | AREAL | 99.648 | m2 | 1,672E-07 | 5,207E-07 | 1,213E-06 | 4,980E-07 | 4,152E-07 | 7,073E-08 | 1,115E-09 | g/s-m2 |
| PFV_3_2 | Parque Fotovoltaico 3_1 | AREAL | 22.607 | m2 | 1,672E-07 | 5,207E-07 | 1,213E-06 | 4,980E-07 | 4,152E-07 | 7,073E-08 | 1,115E-09 | g/s-m2 |
| PFV_4 | Parque Fotovoltaico 4 | AREAL | 157.077 | m2 | 1,672E-07 | 5,207E-07 | 1,213E-06 | 4,980E-07 | 4,152E-07 | 7,073E-08 | 1,115E-09 | g/s-m2 |
| LAT_1 | Línea eléctrica soterrada 1 | LINEAL-AREAL | 12.321 | m2 | 4,081E-06 | 5,744E-06 | 1,805E-05 | 2,312E-05 | 1,443E-05 | 2,459E-06 | 4,755E-08 | g/s-m2 |
| LAT_2 | Línea eléctrica soterrada 2 | LINEAL-AREAL | 286 | m2 | 4,081E-06 | 5,744E-06 | 1,805E-05 | 2,312E-05 | 1,443E-05 | 2,459E-06 | 4,755E-08 | g/s-m2 |
| LAT_3 | Línea eléctrica soterrada 3 | LINEAL-AREAL | 1.389 | m2 | 4,081E-06 | 5,744E-06 | 1,805E-05 | 2,312E-05 | 1,443E-05 | 2,459E-06 | 4,755E-08 | g/s-m2 |
| LAT_4 | Línea eléctrica soterrada 4 | LINEAL-AREAL | 148 | m2 | 4,081E-06 | 5,744E-06 | 1,805E-05 | 2,312E-05 | 1,443E-05 | 2,459E-06 | 4,755E-08 | g/s-m2 |
| LAT_5 | Línea eléctrica soterrada 5 | LINEAL-AREAL | 3.141 | m2 | 4,081E-06 | 5,744E-06 | 1,805E-05 | 2,312E-05 | 1,443E-05 | 2,459E-06 | 4,755E-08 | g/s-m2 |
| LAT | Línea de alta tensión | LINEAL-AREAL | 121 | m2 | 1,720E-05 | 2,422E-05 | 7,609E-05 | 9,746E-05 | 6,085E-05 | 1,037E-05 | 2,005E-07 | g/s-m2 |
| BESS_1_2 | BESS 1 y 2 | AREAL | 7.780 | m2 | 3,237E-06 | 4,557E-06 | 1,432E-05 | 1,834E-05 | 1,145E-05 | 1,951E-06 | 3,772E-08 | g/s-m2 |
| BESS_3 | BESS 3 | AREAL | 1.100 | m2 | 3,237E-06 | 4,557E-06 | 1,432E-05 | 1,834E-05 | 1,145E-05 | 1,951E-06 | 3,772E-08 | g/s-m2 |
| BESS_4 | BESS 4 | AREAL | 531 | m2 | 3,237E-06 | 4,557E-06 | 1,432E-05 | 1,834E-05 | 1,145E-05 | 1,951E-06 | 3,772E-08 | g/s-m2 |
| GE_1 | Grupo Electrógeno (IF 1) | PUNTUAL | - | - | 6,975E-03 | 6,975E-03 | 6,975E-03 | 2,138E-02 | 5,824E-02 | 9,923E-03 | 6,525E-03 | g/s |
| GE_2 | Grupo Electrógeno (Subestación Acuyo) | PUNTUAL | - | - | 6,975E-03 | 6,975E-03 | 6,975E-03 | 2,138E-02 | 5,824E-02 | 9,923E-03 | 6,525E-03 | g/s |

**Tabla 5-33.: Características Fuentes Emisoras Puntuales.****

| Fuente | ID CALPUFF | Altura chimenea<br>(m) | Temperatura salida de los gases<br>(K) | Diámetro interno chimenea<br>(m) | Velocidad de salida de los gases<br>(m/s) |
| --- | --- | --- | --- | --- | --- |
| Grupo Electrógeno (IF 1) | GE_1 | 1,391 | 673,15 | 0,05 | 22,40 |
| Grupo Electrógeno<br>(Subestación Acuyo) | GE_2 | 1,391 | 673,15 | 0,05 | 22,40 |
| Grupo Electrógeno (IF 2) | GE_3 | 1,391 | 673,15 | 0,05 | 22,40 |
| Grupo Electrógeno (PFV 3) | GE_4 | 1,391 | 673,15 | 0,05 | 22,40 |
| Grupo Electrógeno (PFV 4) | GE_5 | 1,391 | 673,15 | 0,05 | 22,40 |

**Tabla 5-34.: Receptores de Interés.****

| ID Receptor | Descripción | Coordenadas de Ubicación | Col4 | Elevación (m.s.n.m) |
| --- | --- | --- | --- | --- |
| **ID Receptor** | **Descripción** | **(Datum WGS84)** | **(Datum WGS84)** | **(Datum WGS84)** |
| **ID Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Norte (m)** |
| E_1 | Estación Casablanca | 278.002 | 6.309.012 | 274,95 |
| R_1 | Receptor de medio humano R1 | 274.179 | 6.311.974 | 269,44 |
| R_2 | Receptor de medio humano R2 | 274.662 | 6.311.643 | 262,31 |
| R_3 | Receptor de medio humano R3 | 274.756 | 6.311.286 | 262,63 |
| R_4 | Receptor de medio humano R4 | 273.779 | 6.311.341 | 263,93 |
| R_5 | Receptor de medio humano R5 | 273.945 | 6.310.943 | 265,61 |
| R_6 | Receptor de medio humano R6 | 274.286 | 6.310.949 | 263,46 |
| R_7 | Receptor de medio humano R7 | 274.172 | 6.310.445 | 266,25 |
| R_8 | Receptor de medio humano R8 | 274.434 | 6.310.332 | 266,06 |
| R_9 | Receptor de medio humano R9 | 273.601 | 6.310.276 | 267,81 |
| R_10 | Receptor de medio humano R10 | 273.544 | 6.309.744 | 286,25 |
| R_11 | Receptor de medio humano R11 | 274.360 | 6.309.617 | 277,11 |
| R_12 | Receptor de medio humano R12 | 274.118 | 6.309.269 | 288,31 |
| R_13 | Receptor de medio humano R13 | 273.365 | 6.308.856 | 308,61 |
| R_14 | Receptor de medio humano R14 | 274.199 | 6.308.835 | 307,22 |
| R_15 | Receptor de medio humano R15 | 275.023 | 6.308.983 | 291,32 |
| RF_1 | Receptor de fauna RF1 | 274.370 | 6.311.822 | 266,07 |
| RF_2 | Receptor de fauna RF2 | 274.604 | 6.311.084 | 262,66 |
| RF_3 | Receptor de fauna RF3 | 274.182 | 6.310.058 | 271,26 |
| RF_4 | Receptor de fauna RF4 | 273.905 | 6.308.660 | 309,52 |
| RF_5 | Receptor de fauna RF5 | 274.651 | 6.308.709 | 318,83 |

**Tabla 5-35.: Resultados de modelo de dispersión de MP2.5.****

| ID<br>Receptor | Descripción | Coordenadas de Ubicación<br>(Datum WGS84) | Col4 | Material Particulado Respirable (MP2.5) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Concentración (μg/m3) - Aporte del**<br>**Proyecto** | **Concentración (μg/m3) - Aporte del**<br>**Proyecto** | **Concentración (μg/m3) - Norma de**<br>**Calidad** | **Concentración (μg/m3) - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil 98 24**<br>**horas** | **Período Anual** | **Percentil 98 24**<br>**horas** | **Período Anual** | **Percentil 98 24**<br>**horas** | **Período Anual** |
| E_1 | Estación Casablanca | 278.002 | 6.309.012 | 0,13 | 0,02 | 50 | 20 | 0,26% | 0,12% |
| R_1 | Receptor de medio humano R1 | 274.179 | 6.311.974 | 2,19 | 0,40 | 50 | 20 | 4,37% | 2,00% |
| R_2 | Receptor de medio humano R2 | 274.662 | 6.311.643 | 1,62 | 0,32 | 50 | 20 | 3,25% | 1,60% |
| R_3 | Receptor de medio humano R3 | 274.756 | 6.311.286 | 1,61 | 0,35 | 50 | 20 | 3,22% | 1,73% |
| R_4 | Receptor de medio humano R4 | 273.779 | 6.311.341 | 3,00 | 0,50 | 50 | 20 | 6,00% | 2,52% |
| R_5 | Receptor de medio humano R5 | 273.945 | 6.310.943 | 2,21 | 0,34 | 50 | 20 | 4,42% | 1,72% |
| R_6 | Receptor de medio humano R6 | 274.286 | 6.310.949 | 4,55 | 1,42 | 50 | 20 | 9,10% | 7,12% |
| R_7 | Receptor de medio humano R7 | 274.172 | 6.310.445 | 3,76 | 1,13 | 50 | 20 | 7,52% | 5,65% |
| R_8 | Receptor de medio humano R8 | 274.434 | 6.310.332 | 2,22 | 0,71 | 50 | 20 | 4,44% | 3,55% |
| R_9 | Receptor de medio humano R9 | 273.601 | 6.310.276 | 1,49 | 0,24 | 50 | 20 | 2,98% | 1,20% |
| R_10 | Receptor de medio humano R10 | 273.544 | 6.309.744 | 2,07 | 0,27 | 50 | 20 | 4,14% | 1,34% |
| R_11 | Receptor de medio humano R11 | 274.360 | 6.309.617 | 2,83 | 0,62 | 50 | 20 | 5,67% | 3,09% |
| R_12 | Receptor de medio humano R12 | 274.118 | 6.309.269 | 2,01 | 0,36 | 50 | 20 | 4,02% | 1,82% |
| R_13 | Receptor de medio humano R13 | 273.365 | 6.308.856 | 0,45 | 0,05 | 50 | 20 | 0,91% | 0,25% |
| R_14 | Receptor de medio humano R14 | 274.199 | 6.308.835 | 1,02 | 0,21 | 50 | 20 | 2,04% | 1,03% |
| R_15 | Receptor de medio humano R15 | 275.023 | 6.308.983 | 0,96 | 0,16 | 50 | 20 | 1,92% | 0,82% |

**Tabla 5-36.: Resultados de modelo de dispersión de MP10.****

| ID<br>Receptor | Descripción | Coordenadas de Ubicación<br>(Datum WGS84) | Col4 | Material Particulado Respirable (MP10) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Concentración (μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración (μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración (μg/m3N) - Norma de**<br>**Calidad** | **Concentración (μg/m3N) - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil 98 24**<br>**horas** | **Período Anual** | **Percentil 98 24**<br>**horas** | **Período Anual** | **Percentil 98 24**<br>**horas** | **Período Anual** |
| E_1 | Estación Casablanca | 278.002 | 6.309.012 | 0,71 | 0,11 | 130 | 50 | 0,54% | 0,22% |
| R_1 | Receptor de medio humano R1 | 274.179 | 6.311.974 | 6,51 | 1,34 | 130 | 50 | 5,01% | 2,68% |
| R_2 | Receptor de medio humano R2 | 274.662 | 6.311.643 | 5,69 | 1,27 | 130 | 50 | 4,37% | 2,53% |
| R_3 | Receptor de medio humano R3 | 274.756 | 6.311.286 | 6,37 | 1,58 | 130 | 50 | 4,90% | 3,16% |
| R_4 | Receptor de medio humano R4 | 273.779 | 6.311.341 | 18,68 | 3,08 | 130 | 50 | 14,37% | 6,17% |
| R_5 | Receptor de medio humano R5 | 273.945 | 6.310.943 | 11,17 | 1,84 | 130 | 50 | 8,59% | 3,67% |
| R_6 | Receptor de medio humano R6 | 274.286 | 6.310.949 | 28,99 | 11,12 | 130 | 50 | 22,30% | 22,25% |
| R_7 | Receptor de medio humano R7 | 274.172 | 6.310.445 | 28,12 | 8,22 | 130 | 50 | 21,63% | 16,45% |
| R_8 | Receptor de medio humano R8 | 274.434 | 6.310.332 | 14,31 | 4,21 | 130 | 50 | 11,01% | 8,43% |
| R_9 | Receptor de medio humano R9 | 273.601 | 6.310.276 | 9,96 | 1,44 | 130 | 50 | 7,67% | 2,87% |
| R_10 | Receptor de medio humano R10 | 273.544 | 6.309.744 | 10,93 | 1,43 | 130 | 50 | 8,41% | 2,86% |
| R_11 | Receptor de medio humano R11 | 274.360 | 6.309.617 | 12,97 | 2,77 | 130 | 50 | 9,97% | 5,54% |
| R_12 | Receptor de medio humano R12 | 274.118 | 6.309.269 | 7,95 | 1,49 | 130 | 50 | 6,12% | 2,98% |
| R_13 | Receptor de medio humano R13 | 273.365 | 6.308.856 | 1,80 | 0,22 | 130 | 50 | 1,38% | 0,43% |
| R_14 | Receptor de medio humano R14 | 274.199 | 6.308.835 | 4,17 | 0,76 | 130 | 50 | 3,21% | 1,51% |
| R_15 | Receptor de medio humano R15 | 275.023 | 6.308.983 | 3,20 | 0,64 | 130 | 50 | 2,46% | 1,28% |

**Tabla 5-37.: Resultados de modelo de dispersión de MPS.****

| ID<br>Receptor | Descripción | Coordenadas de Ubicación<br>(Datum WGS84) | Col4 | Material Particulado Sedimentable (MPS) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Tasa de depositación (mg/m2-dia)** | **Tasa de depositación (mg/m2-dia)** | **Norma (mg/m2-dia)** | **Norma (mg/m2-dia)** | **Porcentaje de la Norma** | **Porcentaje de la Norma** |
| **ID**<br>**Receptor** | **Descripción** | **Este** | **Norte** | **Período Mensual** | **Período Anual** | **Período Mensual** | **Período Anual** | **Período Mensual** | **Período Anual** |
| RF_1 | Receptor de fauna RF1 | 274.370 | 6.311.822 | 13,92 | 7,28 | 333 | 200 | 4,18% | 3,64% |
| RF_2 | Receptor de fauna RF2 | 274.604 | 6.311.084 | 14,47 | 9,35 | 333 | 200 | 4,35% | 4,68% |
| RF_3 | Receptor de fauna RF3 | 274.182 | 6.310.058 | 63,06 | 35,05 | 333 | 200 | 18,94% | 17,52% |
| RF_4 | Receptor de fauna RF4 | 273.905 | 6.308.660 | 2,84 | 1,46 | 333 | 200 | 0,85% | 0,73% |
| RF_5 | Receptor de fauna RF5 | 274.651 | 6.308.709 | 3,42 | 1,51 | 333 | 200 | 1,03% | 0,75% |

**Tabla 5-38.: Resultados de modelo de dispersión de CO.****

| ID<br>Receptor | Descripción | Coordenadas de Ubicación<br>(Datum WGS84) | Col4 | Monóxido de Carbono (CO) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Coordenadas de Ubicación**<br>** (Datum WGS84)** | **Concentración (mg/m3N) - Aporte del**<br>**Proyecto** | **Concentración (mg/m3N) - Aporte del**<br>**Proyecto** | **Concentración (mg/m3N) - Norma de**<br>**Calidad** | **Concentración (mg/m3N) - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil 99 1 hora** | **Percentil 99 8**<br>**horas** | **Percentil 99 1 hora** | **Percentil 99 8**<br>**horas** | **Percentil 99 1 hora** | **Percentil 99 8**<br>**horas** |
| E_1 | Estación Casablanca | 278.002 | 6.309.012 | 0,00 | 0,00 | 30 | 10 | 0,01% | 0,01% |
| R_1 | Receptor de medio humano R1 | 274.179 | 6.311.974 | 0,16 | 0,02 | 30 | 10 | 0,54% | 0,22% |
| R_2 | Receptor de medio humano R2 | 274.662 | 6.311.643 | 0,12 | 0,02 | 30 | 10 | 0,41% | 0,19% |
| R_3 | Receptor de medio humano R3 | 274.756 | 6.311.286 | 0,10 | 0,01 | 30 | 10 | 0,35% | 0,13% |
| R_4 | Receptor de medio humano R4 | 273.779 | 6.311.341 | 0,15 | 0,02 | 30 | 10 | 0,51% | 0,24% |
| R_5 | Receptor de medio humano R5 | 273.945 | 6.310.943 | 0,14 | 0,02 | 30 | 10 | 0,46% | 0,18% |
| R_6 | Receptor de medio humano R6 | 274.286 | 6.310.949 | 0,14 | 0,02 | 30 | 10 | 0,48% | 0,24% |
| R_7 | Receptor de medio humano R7 | 274.172 | 6.310.445 | 0,09 | 0,01 | 30 | 10 | 0,30% | 0,14% |
| R_8 | Receptor de medio humano R8 | 274.434 | 6.310.332 | 0,06 | 0,01 | 30 | 10 | 0,19% | 0,11% |
| R_9 | Receptor de medio humano R9 | 273.601 | 6.310.276 | 0,07 | 0,01 | 30 | 10 | 0,22% | 0,09% |
| R_10 | Receptor de medio humano R10 | 273.544 | 6.309.744 | 0,09 | 0,01 | 30 | 10 | 0,31% | 0,12% |
| R_11 | Receptor de medio humano R11 | 274.360 | 6.309.617 | 0,10 | 0,02 | 30 | 10 | 0,34% | 0,15% |
| R_12 | Receptor de medio humano R12 | 274.118 | 6.309.269 | 0,11 | 0,02 | 30 | 10 | 0,36% | 0,17% |
| R_13 | Receptor de medio humano R13 | 273.365 | 6.308.856 | 0,02 | 0,00 | 30 | 10 | 0,05% | 0,02% |
| R_14 | Receptor de medio humano R14 | 274.199 | 6.308.835 | 0,05 | 0,01 | 30 | 10 | 0,18% | 0,09% |
| R_15 | Receptor de medio humano R15 | 275.023 | 6.308.983 | 0,06 | 0,01 | 30 | 10 | 0,19% | 0,09% |

**Tabla 5-39.: Resultados de modelo de dispersión de NO** **2** **.****

| ID<br>Receptor | Descripción | Coordenadas de Ubicación | Col4 | Dióxido de Nitrógeno (NO2) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de Ubicación** | **Coordenadas de Ubicación** | **Concentración (μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración (μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración (μg/m3N) - Norma de**<br>**Calidad** | **Concentración (μg/m3N) - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil 99 1 hora** | **Período Anual** | **Percentil 99 1 hora** | **Período Anual** | **Percentil 99 1 hora** | **Período Anual** |
| E_1 | Estación Casablanca | 278.002 | 6.309.012 | 5,88 | 0,06 | 400 | 100 | 1,47% | 0,06% |
| R_1 | Receptor de medio humano R1 | 274.179 | 6.311.974 | 84,78 | 0,71 | 400 | 100 | 21,19% | 0,71% |
| R_2 | Receptor de medio humano R2 | 274.662 | 6.311.643 | 61,27 | 0,70 | 400 | 100 | 15,32% | 0,70% |
| R_3 | Receptor de medio humano R3 | 274.756 | 6.311.286 | 65,14 | 0,76 | 400 | 100 | 16,28% | 0,76% |
| R_4 | Receptor de medio humano R4 | 273.779 | 6.311.341 | 73,31 | 0,60 | 400 | 100 | 18,33% | 0,60% |
| R_5 | Receptor de medio humano R5 | 273.945 | 6.310.943 | 79,13 | 0,64 | 400 | 100 | 19,78% | 0,64% |
| R_6 | Receptor de medio humano R6 | 274.286 | 6.310.949 | 71,59 | 0,84 | 400 | 100 | 17,90% | 0,84% |
| R_7 | Receptor de medio humano R7 | 274.172 | 6.310.445 | 49,76 | 0,80 | 400 | 100 | 12,44% | 0,80% |
| R_8 | Receptor de medio humano R8 | 274.434 | 6.310.332 | 44,85 | 0,77 | 400 | 100 | 11,21% | 0,77% |
| R_9 | Receptor de medio humano R9 | 273.601 | 6.310.276 | 53,03 | 0,41 | 400 | 100 | 13,26% | 0,41% |
| R_10 | Receptor de medio humano R10 | 273.544 | 6.309.744 | 60,47 | 0,45 | 400 | 100 | 15,12% | 0,45% |
| R_11 | Receptor de medio humano R11 | 274.360 | 6.309.617 | 75,07 | 0,92 | 400 | 100 | 18,77% | 0,92% |
| R_12 | Receptor de medio humano R12 | 274.118 | 6.309.269 | 76,05 | 0,67 | 400 | 100 | 19,01% | 0,67% |
| R_13 | Receptor de medio humano R13 | 273.365 | 6.308.856 | 17,60 | 0,13 | 400 | 100 | 4,40% | 0,13% |
| R_14 | Receptor de medio humano R14 | 274.199 | 6.308.835 | 39,54 | 0,42 | 400 | 100 | 9,89% | 0,42% |
| R_15 | Receptor de medio humano R15 | 275.023 | 6.308.983 | 36,51 | 0,33 | 400 | 100 | 9,13% | 0,33% |

**Tabla 5-40.: Resultados de modelo de dispersión de SO** **2** **. Normas primarias de calidad del aire.****

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación | Col4 | Dióxido de Azufre (SO2) | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación** | **Coordenadas de**<br>**Ubicación** | **Concentración (μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración (μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración (μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración (μg/m3N) - Norma de**<br>**Calidad** | **Concentración (μg/m3N) - Norma de**<br>**Calidad** | **Concentración (μg/m3N) - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil 99**<br>**1 hora** | **Percentil 99**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 99**<br>**1 hora** | **Percentil 99**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 99**<br>**1 hora** | **Percentil 99**<br>**24 horas** | **Período**<br>**Anual** |
| E_1 | Estación Casablanca | 278.002 | 6.309.012 | 0,03 | 0,01 | 0,00 | 350 | 150 | 60 | 0,01% | 0,01% | 0,00% |
| R_1 | Receptor de medio humano R1 | 274.179 | 6.311.974 | 0,44 | 0,14 | 0,03 | 350 | 150 | 60 | 0,12% | 0,09% | 0,05% |
| R_2 | Receptor de medio humano R2 | 274.662 | 6.311.643 | 0,37 | 0,08 | 0,02 | 350 | 150 | 60 | 0,11% | 0,05% | 0,03% |
| R_3 | Receptor de medio humano R3 | 274.756 | 6.311.286 | 0,42 | 0,12 | 0,02 | 350 | 150 | 60 | 0,12% | 0,08% | 0,04% |
| R_4 | Receptor de medio humano R4 | 273.779 | 6.311.341 | 0,44 | 0,16 | 0,02 | 350 | 150 | 60 | 0,13% | 0,11% | 0,03% |
| R_5 | Receptor de medio humano R5 | 273.945 | 6.310.943 | 0,35 | 0,11 | 0,01 | 350 | 150 | 60 | 0,10% | 0,07% | 0,02% |
| R_6 | Receptor de medio humano R6 | 274.286 | 6.310.949 | 0,37 | 0,14 | 0,02 | 350 | 150 | 60 | 0,10% | 0,09% | 0,03% |
| R_7 | Receptor de medio humano R7 | 274.172 | 6.310.445 | 0,23 | 0,08 | 0,01 | 350 | 150 | 60 | 0,07% | 0,05% | 0,02% |
| R_8 | Receptor de medio humano R8 | 274.434 | 6.310.332 | 0,19 | 0,05 | 0,02 | 350 | 150 | 60 | 0,05% | 0,04% | 0,03% |
| R_9 | Receptor de medio humano R9 | 273.601 | 6.310.276 | 0,18 | 0,05 | 0,01 | 350 | 150 | 60 | 0,05% | 0,03% | 0,01% |
| R_10 | Receptor de medio humano R10 | 273.544 | 6.309.744 | 0,24 | 0,15 | 0,01 | 350 | 150 | 60 | 0,07% | 0,10% | 0,02% |
| R_11 | Receptor de medio humano R11 | 274.360 | 6.309.617 | 0,32 | 0,10 | 0,02 | 350 | 150 | 60 | 0,09% | 0,07% | 0,03% |
| R_12 | Receptor de medio humano R12 | 274.118 | 6.309.269 | 0,34 | 0,10 | 0,02 | 350 | 150 | 60 | 0,10% | 0,07% | 0,03% |
| R_13 | Receptor de medio humano R13 | 273.365 | 6.308.856 | 0,08 | 0,02 | 0,00 | 350 | 150 | 60 | 0,02% | 0,02% | 0,00% |
| R_14 | Receptor de medio humano R14 | 274.199 | 6.308.835 | 0,33 | 0,09 | 0,02 | 350 | 150 | 60 | 0,09% | 0,06% | 0,03% |
| R_15 | Receptor de medio humano R15 | 275.023 | 6.308.983 | 0,25 | 0,10 | 0,01 | 350 | 150 | 60 | 0,07% | 0,07% | 0,02% |

**Tabla 5-41.: Resultados de modelo de dispersión de SO** **2** **. Normas secundarias de calidad del aire.****

| ID<br>Receptor | Descripción | Coordenadas de Ubicación | Col4 | Dióxido de Azufre (SO2) | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de Ubicación** | **Coordenadas de Ubicación** | **Concentración (μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración (μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración (μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración (μg/m3N) - Norma de**<br>**Calidad** | **Concentración (μg/m3N) - Norma de**<br>**Calidad** | **Concentración (μg/m3N) - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil**<br>**99,73 1 hora** | **Percentil**<br>**99,7 24 horas** | **Período**<br>**Anual** | **Percentil**<br>**99,73 1 hora** | **Percentil**<br>**99,7 24 horas** | **Período**<br>**Anual** | **Percentil**<br>**99,73 1 hora** | **Percentil**<br>**99,7 24 horas** | **Período**<br>**Anual** |
| RF_1 | Receptor de fauna RF1 | 274.370 | 6.311.822 | 0,94 | 0,21 | 0,04 | 700 | 260 | 60 | 0,13% | 0,08% | 0,07% |
| RF_2 | Receptor de fauna RF2 | 274.604 | 6.311.084 | 0,82 | 0,17 | 0,02 | 700 | 260 | 60 | 0,12% | 0,07% | 0,03% |
| RF_3 | Receptor de fauna RF3 | 274.182 | 6.310.058 | 0,55 | 0,13 | 0,03 | 700 | 260 | 60 | 0,08% | 0,05% | 0,05% |
| RF_4 | Receptor de fauna RF4 | 273.905 | 6.308.660 | 0,39 | 0,06 | 0,01 | 700 | 260 | 60 | 0,06% | 0,02% | 0,01% |
| RF_5 | Receptor de fauna RF5 | 274.651 | 6.308.709 | 0,53 | 0,14 | 0,02 | 700 | 260 | 60 | 0,08% | 0,05% | 0,03% |

**Tabla 5-42.: Concentración total esperada. Estación Casablanca.****

| Contaminante | Estadígrafo | Norma | Unidad | Línea de base | Col6 | Aporte Proyecto | Col8 | Concentración total | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Estadígrafo** | **Norma** | **Unidad** | **Valor** | **% Norma** | **Valor** | **% Norma** | **Valor** | **% Norma** |
| MP10 | P 98 - 24<br>horas | 130 | μg/m3N | 86,0 | 66,15% | 0,71 | 0,54% | 86,71 | 66,70% |
| MP10 | Media<br>Trianual | 50 | μg/m3N | 32,0 | 64,00% | 0,11 | 0,22% | 32,11 | 64,22% |
| CO | P 99 - 1<br>hora | 30 | mg/m3N | 1,3 | 4,33% | 0,00 | 0,01% | 1,30 | 4,35% |
| CO | P 99 - 8<br>horas | 10 | mg/m3N | 0,9 | 9,00% | 0,00 | 0,01% | 0,90 | 9,01% |
| NO2 | P 99 - 1<br>hora | 400 | μg/m3N | 52,6 | 13,15% | 5,88 | 1,47% | 58,48 | 14,62% |
| NO2 | Media<br>Trianual | 100 | μg/m3N | 11,3 | 11,30% | 0,06 | 0,06% | 11,36 | 11,36% |
| SO2 | P 99 - 1<br>hora | 350 | μg/m3N | 13,0 | 3,71% | 0,03 | 0,01% | 13,03 | 3,72% |
| SO2 | P 99 - 24<br>horas | 150 | μg/m3N | 2,6 | 1,73% | 0,01 | 0,01% | 2,61 | 1,74% |
| SO2 | Media<br>Anual | 60 | μg/m3N | 1,3 | 2,17% | 0,00 | 0,00% | 1,30 | 2,17% |

**Tabla 5-43.: Criterios recomendados de incremento significativo en la concentración de contaminantes****

| Contaminante | Período | SIL Porcentual USEPA | Incremento Significativo en la Concentración<br>(ug/m3) |
| --- | --- | --- | --- |
| MP2.5 | 24 horas | 3,4% | 1,7 |
| MP2.5 | Anual | 1,7% | 0,3 |
| MP10 | 24 horas | 3,3% | 5,0 |
| MP10 | Anual | 2,0% | 1,0 |
| O3 | 8 horas | 1,4% | 1,7 |
| NO2 | 1 hora | 4,0% | 16,0 |
| NO2 | Anual | 1,0% | 1,0 |
| CO | 1 hora | 5,0% | 1.500,0 |
| CO | 8 horas | 4,9% | 488,9 |
| SO2 | 1 hora | 4,0% | 14,0 |
| SO2 | 24 horas | 1,4% | 2,0 |
| SO2 | Anual | 2,0% | 1,2 |

**Tabla 7-1.: Archivos de modelación entregados.****

| Archivos | Entregado | Observación |
| --- | --- | --- |
| **Archivos CALPUFF:** | **Archivos CALPUFF:** | **Archivos CALPUFF:** |
| - CALPUFF.DAT | NO | Corresponde al archivo CONC.DAT |
| - CALPUFF.LST | SI | - |
| - CALPUFF.INP | SI | - |
| - CONC.DAT | SI | - |
| - DFLX.DAT | SI | - |
| - WFLX.DAT | NO | - |
| - POSTUTCN.INP | SI | - |
| - POSTUTCN.LST | SI | - |
| - PUCONC.DAT | SI | - |
| **Archivos Meteorológicos:** | **Archivos Meteorológicos:** | **Archivos Meteorológicos:** |
| - CALMET.DAT | SI | -Corresponde al archivo:<br>calmetv6_Casablanca_2020.dat |
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
