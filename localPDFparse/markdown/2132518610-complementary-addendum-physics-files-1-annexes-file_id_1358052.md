---
title: Sin título
author: Asesorías del Favero y Meneses
date: D:20180405082623-03'00'
language: es
type: report
pages: 177
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Proyecto “Actualización y Desarrollo Planta Faenadora de Aves Lo Miranda”
-->

## Modelación de Dispersión de Contaminantes Atmosféricos

# Proyecto “Actualización y Desarrollo Planta Faenadora de Aves Lo Miranda”

### Abril 2018

|REVISIONES|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|No REV.|ELABORADO POR|REVISADO POR|FECHA|DETALLES|
|0|Hermes Moraga S.|Benjamín Del Favero T.|03-04-18||

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

ÍNDICE

**1** **INTRODUCCIÓN ..................................................................................................... 1**

**2** **MODELO DE CALIDAD DEL AIRE .............................................................................. 3**

**2.1** **Tipo de Modelo de Calidad del Aire Seleccionado............................................................................... 3**

**2.2** **Descripción del Modelo de Calidad del Aire Seleccionado - CALPUFF ................................................. 3**

**2.3** **Características del Modelo de Dispersión de Contaminantes .............................................................. 5**

2.3.1 Dominio de la Modelación ..................................................................................... 5

2.3.2 Topografía del Sector ............................................................................................. 6

**2.4** **Caracterización Meteorológica del Área del Proyecto ......................................................................... 7**

2.4.1 Meteorología de Superficie - Valores Observados ................................................. 7

2.4.2 Meteorología de Superficie - Valores Modelados ............................................... 47

2.4.3 Meteorología de Altura - Valores Observados .................................................... 69

2.4.4 Meteorología de Altura - Valores Modelados ..................................................... 69

**2.5** **Análisis de Incertidumbre - Comparación Cualitativa ....................................................................... 75**

2.5.1 Velocidad y Dirección del Viento .......................................................................... 75

2.5.2 Temperatura ......................................................................................................... 80

**2.6** **Análisis de Incertidumbre - Comparación Cuantitativa .................................................................... 84**

**2.7** **Normas de Calidad del Aire .............................................................................................................. 86**

**2.8** **Calidad del Aire ................................................................................................................................ 87**

**2.9** **Escenarios Modelados ...................................................................................................................... 91**

2.9.1 Escenario 1: Construcción Etapa 2 y Operación Proyectada................................ 91

2.9.2 Escenario 2: Operación Proyectada ..................................................................... 97

**2.10** **Receptores de Interés ............................................................................................................ 102**

**2.11** **Resultados de la Modelación ................................................................................................. 104**

www.dfmconsultores.cl

**info@dfmconsultores.cl**

i

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

2.11.1 Escenario 1: Construcción Etapa 2 y Operación Proyectada.......................... 105

2.11.2 Escenario 2: Operación Proyectada ............................................................... 130

**2.12** **Concentración Total Esperada ............................................................................................... 155**

2.12.1 Escenario 1: Construcción Etapa 2 y Operación Proyectada.......................... 155

2.12.2 Escenario 2: Operación Proyectada ............................................................... 158

**3** **CONCLUSIONES .................................................................................................. 161**

**3.1** **Conclusiones Respecto a la Modelación de Dispersión de Contaminantes en la Atmósfera ........** ¡Error!

Marcador no definido.

3.1.1 Conclusiones Modelación Escenario 1 ............................................................... 161

www.dfmconsultores.cl

**info@dfmconsultores.cl**

ii

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

ÍNDICE TABLAS

Tabla 2-1 - Coordenadas de Ubicación Estaciones de Monitoreo Meteorológico. ............... 7

Tabla 2-2. Resumen de Información Velocidad del Viento Observada. Estación Rancagua I.

................................................................................................................................................ 9

Tabla 2-3 - Frecuencia de Distribución, Velocidad y Dirección del Viento. Periodo enero

2015 a diciembre 2017. Observado en Estación Rancagua I. .............................................. 12

Tabla 2-4 - Resumen de Información Temperatura Observada en Estación Rancagua I. .... 16

Tabla 2-5. Resumen de Información Humedad Relativa Observada en Estación Rancagua I.

.............................................................................................................................................. 20

Tabla 2-6. Resumen de Información Radiación Solar Observada en Estación Rancagua I. . 24

Tabla 2-7. Resumen de Información Velocidad del Viento Observada. Estación Rancagua II.

.............................................................................................................................................. 28

Tabla 2-8 - Frecuencia de Distribución, Velocidad y Dirección del Viento. Periodo enero

2015 a diciembre 2017. Observado en Estación Rancagua II. ............................................. 31

Tabla 2-9 - Resumen de Información Temperatura Observada en Estación Rancagua II. ... 35

Tabla 2-10. Resumen de Información Humedad Relativa Observada en Estación Rancagua

II. ........................................................................................................................................... 39

Tabla 2-11. Resumen de Información Radiación Solar Observada en Estación Rancagua II.

.............................................................................................................................................. 43

Tabla 2-12. Resumen de Información Velocidad del Viento Modelada. Estación Rancagua I.

.............................................................................................................................................. 47

Tabla 2-13 - Frecuencia de Distribución, Velocidad y Dirección del Viento. Período enero a

diciembre 2016. Modelado en Estación Rancagua I. ........................................................... 50

Tabla 2-14 - Resumen de Información Temperatura Modelada en Estación Rancagua I. ... 54

Tabla 2-15. Resumen de Información Velocidad del Viento Modelada. Estación Rancagua

II. ........................................................................................................................................... 58

www.dfmconsultores.cl

**info@dfmconsultores.cl**

iii

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Tabla 2-16 - Frecuencia de Distribución, Velocidad y Dirección del Viento. Período enero a

diciembre 2016. Modelado en Estación Rancagua II. .......................................................... 61

Tabla 2-17 - Resumen de Información Temperatura Modelada en Estación Rancagua II. .. 65

Tabla 2-18 - Resumen de Información Altura de Capa de Mezcla Modelada en Estación

Rancagua I............................................................................................................................. 69

Tabla 2-19 - Resumen de Información Altura de Capa de Mezcla Modelada en Estación

Rancagua II............................................................................................................................ 72

Tabla 2-20. Comparación Resultados Observados y Modelados de Velocidad del Viento y

Dirección del Viento. Periodo enero a diciembre 2016. Estación Rancagua I. .................... 75

Tabla 2-21. Comparación Resultados Observados y Modelados de Velocidad del Viento y

Dirección del Viento. Periodo enero a diciembre 2016. Estación Rancagua II. ................... 78

Tabla 2-22. Comparación Resultados Observados y Modelados de Temperatura. Periodo

enero a diciembre 2016. Estación Rancagua I. .................................................................... 80

Tabla 2-23. Comparación Resultados Observados y Modelados de Temperatura. Periodo

enero a diciembre 2016. Estación Rancagua I. .................................................................... 82

Tabla 2-24. Estadígrafos de Dispersión para Velocidad del Viento y Temperatura. ............ 84

Tabla 2-25 - Normas de calidad del aire. ............................................................................. 86

Tabla 2-26 - Estaciones monitoras de calidad del aire. ....................................................... 87

Tabla 2-27 -Calidad del Aire Estación Rancagua I. ............................................................... 89

Tabla 2-28 -Calidad del Aire Estación Rancagua II. .............................................................. 90

Tabla 2-29. Características y Tasas de Emisión de Fuentes Puntuales. Escenario 1. ........... 94

Tabla 2-30. Características y Tasas de Emisión de Fuentes Lineales. Escenario 1. .............. 95

Tabla 2-31. Características y Tasas de Emisión de Fuentes Areales. Escenario 1. ............... 96

Tabla 2-32. Características y Tasas de Emisión de Fuentes Puntuales. Escenario 2. ......... 100

Tabla 2-33. Características y Tasas de Emisión de Fuentes Lineales. Escenario 2. ............ 101

Tabla 2-34- Receptores de Interés. .................................................................................... 102

www.dfmconsultores.cl

**info@dfmconsultores.cl**

iv

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Tabla 2-35 - Resultados de modelo de dispersión de MP2.5. Escenario 1. ....................... 105

Tabla 2-36 - Resultados de modelo de dispersión de MP10. Escenario 1. ........................ 110

Tabla 2-37 - Resultados de modelo de dispersión de CO. Escenario 1. ............................ 115

Tabla 2-38 - Resultados de modelo de dispersión de NO 2 . Escenario 1. ........................... 120

Tabla 2-39 - Resultados de modelo de dispersión de SO 2 . Escenario 1. ........................... 125

Tabla 2-40 - Resultados de modelo de dispersión de MP2.5. Escenario 2. ....................... 130

Tabla 2-41 - Resultados de modelo de dispersión de MP10. Escenario 2. ........................ 135

Tabla 2-42 - Resultados de modelo de dispersión de CO. Escenario 2. ............................ 140

Tabla 2-43 - Resultados de modelo de dispersión de NO 2 . Escenario 2. ........................... 145

Tabla 2-44 - Resultados de modelo de dispersión de SO 2 . Escenario 2. ........................... 150

Tabla 2-45. Concentración total esperada. Material Particulado Respirable Fino (MP2.5).

Escenario 1. ......................................................................................................................... 155

Tabla 2-46. Concentración total esperada. Material Particulado Respirable (MP10).

Escenario 1. ......................................................................................................................... 156

Tabla 2-47. Concentración total esperada. Monóxido de Carbono (CO). Escenario 1. ..... 156

Tabla 2-48. Concentración total esperada. Dióxido de Azufre (SO 2 ). Escenario 1. ............ 157

Tabla 2-49. Concentración total esperada. Material Particulado Respirable Fino (MP2.5).

Escenario 2. ......................................................................................................................... 158

Tabla 2-50. Concentración total esperada. Material Particulado Respirable (MP10).

Escenario 2. ......................................................................................................................... 159

Tabla 2-51. Concentración total esperada. Monóxido de Carbono (CO). Escenario 2. ..... 159

Tabla 2-52. Concentración total esperada. Dióxido de Azufre (SO 2 ). Escenario 2. ............ 160

www.dfmconsultores.cl

**info@dfmconsultores.cl**

v

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

ÍNDICE FIGURAS

Figura 2-1 - Dominio de Modelación. .................................................................................... 5

Figura 2-2 - Topografía del Dominio de Modelación. ............................................................ 6

Figura 2-3 - Ubicación Referencial Estaciones de Monitoreo Meteorológico. ...................... 8

Figura 2-4. Serie de Tiempo para Velocidad del Viento. Período enero 2015 a diciembre

2017. Observado en Estación Rancagua I. ........................................................................... 10

Figura 2-5. Serie de Tiempo para Dirección del Viento. Período enero 2015 a diciembre

2017 - Observado en Estación Rancagua I. .......................................................................... 11

Figura 2-6 Ciclo Diario de Velocidad del Viento. Periodo enero 2015 a diciembre 2017Observado en Estación Rancagua I....................................................................................... 13

Figura 2-7 Ciclo Diario dirección del Viento. Periodo enero 2015 a diciembre 2017Observado en Estación Rancagua I....................................................................................... 14

Figura 2-8 - Ciclo Diario Anual Vientos. Período enero 2015 a diciembre 2017. Observado

en Estación Rancagua I. ........................................................................................................ 15

Figura 2-9 - Serie de Tiempo para la Temperatura. Período enero 2015 a diciembre 2017.

Observado en Estación Rancagua I....................................................................................... 17

Figura 2-10 - Ciclo Diario Temperatura. Período enero 2015 a diciembre 2017. Observado

en Estación Rancagua I. ........................................................................................................ 18

Figura 2-11 - Ciclo Diario Anual de Temperatura. Período enero 2015 a diciembre 2017.

Observado en Estación Rancagua I....................................................................................... 19

Figura 2-12. Serie de Tiempo Humedad Relativa. Periodo enero 2015 a diciembre 2017.

Observado en Estación Rancagua I....................................................................................... 21

Figura 2-13. Ciclo Diario de Humedad Relativa. Período enero 2015 a diciembre 2017.

Observado en Estación Rancagua I....................................................................................... 22

Figura 2-14 Ciclo Diario Anual de Humedad Relativa. Período enero 2015 a diciembre

2017. Observado en Estación Rancagua I. ........................................................................... 23

www.dfmconsultores.cl

**info@dfmconsultores.cl**

vi

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Figura 2-15. Serie de Tiempo Radiación Solar. Periodo enero 2015 a diciembre 2017.

Observado en Estación Rancagua I....................................................................................... 25

Figura 2-16. Ciclo Diario de Radiación Solar. Período enero 2015 a diciembre 2017.

Observado en Estación Rancagua I....................................................................................... 26

Figura 2-17 Ciclo Diario Anual de Radiación Solar. Período enero 2015 a diciembre 2017.

Observado en Estación Rancagua I....................................................................................... 27

Figura 2-18. Serie de Tiempo para Velocidad del Viento. Período enero 2015 a diciembre

2017. Observado en Estación Rancagua II. .......................................................................... 29

Figura 2-19. Serie de Tiempo para Dirección del Viento. Período enero 2015 a diciembre

2017 - Observado en Estación Rancagua II. ......................................................................... 30

Figura 2-20 Ciclo Diario de Velocidad del Viento. Periodo enero 2015 a diciembre 2017Observado en Estación Rancagua II...................................................................................... 32

Figura 2-21 Ciclo Diario dirección del Viento. Periodo enero 2015 a diciembre 2017Observado en Estación Rancagua II...................................................................................... 33

Figura 2-22 - Ciclo Diario Anual Vientos. Período enero 2015 a diciembre 2017. Observado

en Estación Rancagua II. ....................................................................................................... 34

Figura 2-23 - Serie de Tiempo para la Temperatura. Período enero 2015 a diciembre 2017.

Observado en Estación Rancagua II...................................................................................... 36

Figura 2-24 - Ciclo Diario Temperatura. Período enero 2015 a diciembre 2017. Observado

en Estación Rancagua II. ....................................................................................................... 37

Figura 2-25 - Ciclo Diario Anual de Temperatura. Período enero 2015 a diciembre 2017.

Observado en Estación Rancagua II...................................................................................... 38

Figura 2-26. Serie de Tiempo Humedad Relativa. Periodo enero 2015 a diciembre 2017.

Observado en Estación Rancagua II...................................................................................... 40

Figura 2-27. Ciclo Diario de Humedad Relativa. Período enero 2015 a diciembre 2017.

Observado en Estación Rancagua II...................................................................................... 41

www.dfmconsultores.cl

**info@dfmconsultores.cl**

vii

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Figura 2-28 Ciclo Diario Anual de Humedad Relativa. Período enero 2015 a diciembre

2017. Observado en Estación Rancagua II. .......................................................................... 42

Figura 2-29. Serie de Tiempo Radiación Solar. Periodo enero 2015 a diciembre 2017.

Observado en Estación Rancagua II...................................................................................... 44

Figura 2-30. Ciclo Diario de Radiación Solar. Período enero 2015 a diciembre 2017.

Observado en Estación Rancagua II...................................................................................... 45

Figura 2-31 Ciclo Diario Anual de Radiación Solar. Período enero 2015 a diciembre 2017.

Observado en Estación Rancagua II...................................................................................... 46

Figura 2-32. Serie de Tiempo para Velocidad del Viento. Período enero a diciembre 2016.

Modelado en Estación Rancagua I. ...................................................................................... 48

Figura 2-33. Serie de Tiempo para Dirección del Viento. Período enero a diciembre 2016.

Modelado en Estación Rancagua I. ...................................................................................... 49

Figura 2-34 Ciclo Diario de Velocidad del Viento. Período enero a diciembre 2016.

Modelado en Estación Rancagua I. ...................................................................................... 51

Figura 2-35 Ciclo Diario dirección del Viento. Período enero a diciembre 2016. Modelado

en Estación Rancagua I. ........................................................................................................ 52

Figura 2-36 - Ciclo Diario Anual Vientos. Período enero a diciembre 2016. Modelado en

Estación Rancagua I. ............................................................................................................. 53

Figura 2-37 - Serie de Tiempo para la Temperatura. Período enero a diciembre 2016.

Modelado en Estación Rancagua I. ...................................................................................... 55

Figura 2-38 - Ciclo Diario Temperatura. Período enero a diciembre 2016. Modelado en

Estación Rancagua I. ............................................................................................................. 56

Figura 2-39 - Ciclo Diario Anual de Temperatura. Período enero a diciembre 2016.

Modelado en Estación Rancagua I. ...................................................................................... 57

Figura 2-40. Serie de Tiempo para Velocidad del Viento. Período enero a diciembre 2016.

Modelado en Estación Rancagua II. ..................................................................................... 59

www.dfmconsultores.cl

**info@dfmconsultores.cl**

viii

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Figura 2-41. Serie de Tiempo para Dirección del Viento. Período enero a diciembre 2016.

Modelado en Estación Rancagua II. ..................................................................................... 60

Figura 2-42 Ciclo Diario de Velocidad del Viento. Período enero a diciembre 2016.

Modelado en Estación Rancagua II. ..................................................................................... 62

Figura 2-43 Ciclo Diario dirección del Viento. Período enero a diciembre 2016. Modelado

en Estación Rancagua II. ....................................................................................................... 63

Figura 2-44 - Ciclo Diario Anual Vientos. Período enero a diciembre 2016. Modelado en

Estación Rancagua II. ............................................................................................................ 64

Figura 2-45 - Serie de Tiempo para la Temperatura. Período enero a diciembre 2016.

Modelado en Estación Rancagua II. ..................................................................................... 66

Figura 2-46 - Ciclo Diario Temperatura. Período enero a diciembre 2016. Modelado en

Estación Rancagua II. ............................................................................................................ 67

Figura 2-47 - Ciclo Diario Anual de Temperatura. Período enero a diciembre 2016.

Modelado en Estación Rancagua II. ..................................................................................... 68

Figura 2-48 - Serie de Tiempo para Altura de Capa de Mezcla. Período enero a diciembre

2016. Modelado en Estación Rancagua I. ............................................................................ 70

Figura 2-49 - Ciclo Diario de Altura de Capa de Mezcla. Período enero a diciembre 2016.

Modelado en Estación Rancagua I. ...................................................................................... 71

Figura 2-50 - Serie de Tiempo para Altura de Capa de Mezcla. Período enero a diciembre

2016. Modelado en Estación Rancagua II. ........................................................................... 73

Figura 2-51 - Ciclo Diario de Altura de Capa de Mezcla. Período enero a diciembre 2016.

Modelado en Estación Rancagua II. ..................................................................................... 74

Figura 2-52. Ubicación Referencial Estaciones monitoras de Calidad del Aire. ................... 88

Figura 2-53. Ubicación Fuentes Emisoras. Vista General. Escenario 1. ............................... 92

Figura 2-54 - Ubicación Fuentes Emisoras. Zoom Sector Proyecto. Escenario 1. .............. 93

Figura 2-55. Ubicación Fuentes Emisoras. Vista General. Escenario 2. ............................... 98

Figura 2-56 - Ubicación Fuentes Emisoras. Zoom Sector Proyecto. Escenario 2. .............. 99

www.dfmconsultores.cl

**info@dfmconsultores.cl**

ix

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Figura 2-57 - Ubicación de Receptores de Interés. ........................................................... 103

Figura 2-58. Curva de Isoconcentración para Percentil 98 período 24 horas MP2,5
(μg/m [3] N). Vista General. Escenario 1. ................................................................................ 106

Figura 2-59. Curva de Isoconcentración para Percentil 98 período 24 horas MP2,5
(μg/m [3] N). Zoom Sector Proyecto. Escenario 1. .................................................................. 107

Figura 2-60. Curva de Isoconcentración para período anual MP2,5 (μg/m [3] N). Vista General.

Escenario 1. ......................................................................................................................... 108

Figura 2-61. Curva de Isoconcentración para período anual MP2,5 (μg/m [3] N). Zoom Sector

Proyecto. Escenario 1. ........................................................................................................ 109

Figura 2-62. Curva de Isoconcentración para Percentil 98 período 24 horas MP10
(μg/m [3] N). Vista General. Escenario 1. ................................................................................ 111

Figura 2-63. Curva de Isoconcentración para Percentil 98 período 24 horas MP10
(μg/m [3] N). Zoom Sector Proyecto. Escenario 1. .................................................................. 112

Figura 2-64. Curva de Isoconcentración para período anual MP10 (μg/m [3] N). Vista General.

Escenario 1. ......................................................................................................................... 113

Figura 2-65. Curva de Isoconcentración para período anual MP10 (μg/m [3] N). Zoom Sector

Proyecto. Escenario 1. ........................................................................................................ 114

Figura 2-66. Curva de Isoconcentración para Percentil 99 período 8 horas CO (mg/m [3] N).

Vista General. Escenario 1. ................................................................................................. 116

Figura 2-67. Curva de Isoconcentración para Percentil 99 período 8 horas CO (mg/m [3] N).

Zoom Sector Proyecto. Escenario 1. ................................................................................... 117

Figura 2-68. Curva de Isoconcentración para Percentil 99 periodo 1 hora CO (mg/m [3] N).

Vista General. Escenario 1. ................................................................................................. 118

Figura 2-69. Curva de Isoconcentración para Percentil 99 periodo 1 hora CO (mg/m [3] N).

Zoom Sector Proyecto. Escenario 1. ................................................................................... 119

Figura 2-70. Curva de Isoconcentración para periodo anual NO 2 (μg/m [3] N). Vista General.

Escenario 1. ......................................................................................................................... 121

www.dfmconsultores.cl

**info@dfmconsultores.cl**

x

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Figura 2-71. Curva de Isoconcentración para periodo anual NO 2 (μg/m [3] N). Zoom Sector

Proyecto. Escenario 1. ........................................................................................................ 122

Figura 2-72. Curva de Isoconcentración para Percentil 99 periodo 1 hora NO 2 (μg/m [3] N).

Vista General. Escenario 1. ................................................................................................. 123

Figura 2-73. Curva de Isoconcentración para Percentil 99 periodo 1 hora NO 2 (μg/m [3] N).

Zoom Sector Proyecto. Escenario 1. ................................................................................... 124

Figura 2-74. Curva de Isoconcentración para período anual SO 2 (μg/m [3] N). Vista General.

Escenario 1. ......................................................................................................................... 126

Figura 2-75. Curva de Isoconcentración para período anual SO 2 (μg/m [3] N). Zoom Sector

Proyecto. Escenario 1. ........................................................................................................ 127

Figura 2-76. Curva de Isoconcentración para Percentil 99 periodo 24 horas SO 2 (μg/m [3] N).

Vista General. Escenario 1. ................................................................................................. 128

Figura 2-77. Curva de Isoconcentración para Percentil 99 periodo 24 horas SO 2 (μg/m [3] N).

Zoom Sector Proyecto. Escenario 1. ................................................................................... 129

Figura 2-78. Curva de Isoconcentración para Percentil 98 período 24 horas MP2,5
(μg/m [3] N). Vista General. Escenario 2. ................................................................................ 131

Figura 2-79. Curva de Isoconcentración para Percentil 98 período 24 horas MP2,5
(μg/m [3] N). Zoom Sector Proyecto. Escenario 2. .................................................................. 132

Figura 2-80. Curva de Isoconcentración para período anual MP2,5 (μg/m [3] N). Vista General.

Escenario 2. ......................................................................................................................... 133

Figura 2-81. Curva de Isoconcentración para período anual MP2,5 (μg/m [3] N). Zoom Sector

Proyecto. Escenario 2. ........................................................................................................ 134

Figura 2-82. Curva de Isoconcentración para Percentil 98 período 24 horas MP10
(μg/m [3] N). Vista General. Escenario 2. ................................................................................ 136

Figura 2-83. Curva de Isoconcentración para Percentil 98 período 24 horas MP10
(μg/m [3] N). Zoom Sector Proyecto. Escenario 2. .................................................................. 137

www.dfmconsultores.cl

**info@dfmconsultores.cl**

xi

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Figura 2-84. Curva de Isoconcentración para período anual MP10 (μg/m [3] N). Vista General.

Escenario 2. ......................................................................................................................... 138

Figura 2-85. Curva de Isoconcentración para período anual MP10 (μg/m [3] N). Zoom Sector

Proyecto. Escenario 2. ........................................................................................................ 139

Figura 2-86. Curva de Isoconcentración para Percentil 99 período 8 horas CO (mg/m [3] N).

Vista General. Escenario 2. ................................................................................................. 141

Figura 2-87. Curva de Isoconcentración para Percentil 99 período 8 horas CO (mg/m [3] N).

Zoom Sector Proyecto. Escenario 2. ................................................................................... 142

Figura 2-88. Curva de Isoconcentración para Percentil 99 periodo 1 hora CO (mg/m [3] N).

Vista General. Escenario 2. ................................................................................................. 143

Figura 2-89. Curva de Isoconcentración para Percentil 99 periodo 1 hora CO (mg/m [3] N).

Zoom Sector Proyecto. Escenario 2. ................................................................................... 144

Figura 2-90. Curva de Isoconcentración para periodo anual NO 2 (μg/m [3] N). Vista General.

Escenario 2. ......................................................................................................................... 146

Figura 2-91. Curva de Isoconcentración para periodo anual NO 2 (μg/m [3] N). Zoom Sector

Proyecto. Escenario 2. ........................................................................................................ 147

Figura 2-92. Curva de Isoconcentración para Percentil 99 periodo 1 hora NO 2 (μg/m [3] N).

Vista General. Escenario 2. ................................................................................................. 148

Figura 2-93. Curva de Isoconcentración para Percentil 99 periodo 1 hora NO 2 (μg/m [3] N).

Zoom Sector Proyecto. Escenario 2. ................................................................................... 149

Figura 2-94. Curva de Isoconcentración para período anual SO 2 (μg/m [3] N). Vista General.

Escenario 2. ......................................................................................................................... 151

Figura 2-95. Curva de Isoconcentración para período anual SO 2 (μg/m [3] N). Zoom Sector

Proyecto. Escenario 2. ........................................................................................................ 152

Figura 2-96. Curva de Isoconcentración para Percentil 99 periodo 24 horas SO 2 (μg/m [3] N).

Vista General. Escenario 2. ................................................................................................. 153

www.dfmconsultores.cl

**info@dfmconsultores.cl**

xii

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Figura 2-97. Curva de Isoconcentración para Percentil 99 periodo 24 horas SO 2 (μg/m [3] N).

Vista General. Escenario 2. ................................................................................................. 154

www.dfmconsultores.cl

**info@dfmconsultores.cl**

xiii

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

#### 1 INTRODUCCIÓN

El presente informe contiene la Modelación de Calidad del Aire del Proyecto

“Actualización y Desarrollo Planta Faenadora de Aves Lo Miranda”, el cual se encuentra

ubicado en el Sector Lo Miranda de la Comuna de Doñihue, provincia de Cachapoal,

Región del Libertador General Bernardo O'Higgins. La planta tiene como objetivo la

faenación de aves y cerdos, elaboración de productos y subproductos alimenticios

provenientes de carnes de cerdo y aves y zona de frigorífico.

Para la modelación dispersión de contaminantes atmosféricos se observó lo señalado por

la “Guía para el uso de modelos de calidad de aire en el SEIA” del Servicio de Evaluación

Ambiental.

De esta forma, se presenta en primer lugar una descripción del modelo de calidad del aire

a utilizar (CALPUFF), donde se detallan sus características principales, el dominio de

modelación seleccionado y la topografía del mismo.

Luego, se realiza una caracterización meteorológica del área del proyecto en donde se

presentan datos de las variables meteorológicas de superficie observadas; velocidad del

viento, dirección del viento, temperatura, humedad relativa y radiación solar, todas

registradas en las estaciones de monitoreo Rancagua I y Rancagua II.

A su vez, se presentan los resultados de la modelación meteorológica (WRF) realizada para

el año 2016. Luego, se presenta un análisis de incertidumbre cualitativo y cuantitativo con

el cual se valida el modelo meteorológico comparando sus resultados con mediciones del

año 2016 para las Estaciones Rancagua I y Rancagua II.

Para cuantificar el estado actual de la calidad del aire en la zona de emplazamiento del

proyecto, se presenta una línea de base de calidad del aire elaborada a partir de

monitoreos de Material Particulado Fino (MP2,5), Material Particulado Respirable (MP10),

Monóxido de Carbono (CO) y Dióxido de Azufre (SO 2 ) en la Estación Rancagua I y de

Material Particulado Fino (MP2,5), Material Particulado Respirable (MP10) en la Estación

Rancagua II para trienio comprendido entre los años 2015 a 2017.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

1

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Se plantean dos escenarios de modelación, el primero corresponde a la Etapa 2 de

Construcción del Proyecto cuya duración es de un año y corresponde a la etapa de mayor

emisiones de la fase de construcción, en dicha etapa se presentan en forma simultánea

emisiones de la fase de operación de proyecto las cuales son incorporadas en el escenario

de emisiones. El segundo escenario de modelación corresponde a la fase de operación del

proyecto el cual considera las emisiones de la operación de un nuevo grupo electrógeno,

la operación de Caldera de Biomasa y las emisiones asociadas al tránsito vehicular.

Se presentan los resultados de la modelación de dispersión de contaminantes para los

contaminantes Material Particulado Fino (MP2,5), Material Particulado Respirable (MP10),

Monóxido de Carbono (CO), Dióxido de Nitrógeno (NO 2 ) y Dióxido de Azufre (SO 2 ) y con

ello se realiza un análisis del aporte del proyecto a 12 receptores discretos para cada

contaminante evaluado. A su vez, se presentan las curvas de isoconcentración de cada

contaminante.

Considerando la línea de base de calidad del aire y los resultados del modelo de dispersión

de contaminantes, se presenta la concentración total esperada en la Estación Rancagua I y

Rancagua II para los contaminantes de interés monitoreados en dichas estaciones.

Finalmente, se presentan las principales conclusiones de este estudio en forma separada

para cada escenario de modelación.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

2

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

#### 2 MODELO DE CALIDAD DEL AIRE

A continuación, se presenta la información relevante respecto del modelo de calidad del

aire utilizado.

**2.1** **Tipo de Modelo de Calidad del Aire Seleccionado**

Los principales factores por considerar para la selección de un modelo corresponden al

tipo de terreno presente en el área del proyecto, es decir, si es plano o complejo, y el tipo

de contaminante a emitir, si es primario o secundario. De acuerdo con lo recomendado en

la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, en el área de

emplazamiento del proyecto existen factores que podrían perturbar el carácter lineal de

los vientos, por lo anterior, es necesario utilizar un modelo que permita simular

meteorología heterogénea. Debido a lo anterior, se ha seleccionado un modelo tipo “puff”

para la ejecución de la modelación de calidad del aire.

A continuación, se presenta el detalle del modelo tipo “puff” a utilizar.

**2.2** **Descripción del Modelo de Calidad del Aire Seleccionado - CALPUFF**

Como se indicó anteriormente, el entorno del área del proyecto presenta sectores de

topografía compleja, que podrían interferir en el carácter lineal de los vientos, se

seleccionó como modelo de calidad del aire, CALPUFF. La descripción del mencionado

modelo se presenta a continuación.

CALPUFF, es un modelo de libre disposición, que fue desarrollado por Research
Corporation, siendo Atmospheric Studies Group de TRC Solutions [1], empresa que es su

soporte técnico actual.

Es un modelo de dispersión de contaminantes, no estacionario, multi-capa, que es capaz

de modelar múltiples especies. Puede simular los efectos del tiempo - y en el espacio - las

diversas condiciones meteorológicas en el transporte de contaminantes. Corresponde a

1 [www.src.com/calpuff/calpuff1.htm](http://www.src.com/calpuff/calpuff1.htm)

www.dfmconsultores.cl

**info@dfmconsultores.cl**

3

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

un modelo Lagrangiano-Gaussiano de transporte y dispersión de “puff” emitidos por las

fuentes emisoras consideradas. Dentro de las capacidades del Modelo de Calidad del Aire,

se puede destacar lo siguiente:

 - Simulación de procesos complejos: fumigación, estancamiento y recirculación.

 - Modelación de transporte de contaminantes de largo alcance.

 - Incorporación de efectos de terreno complejo en la dispersión de contaminantes.

 - Modelación de procesos de transformaciones químicas.

Posee un módulo para realizar el post-procesamiento de datos, denominado CALPOST, el

cual calcula las concentraciones en los receptores de interés, permitiendo gestionar los

datos para cada contaminante según el período de tiempo requerido para el análisis.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

4

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.3** **Características del Modelo de Dispersión de Contaminantes**

**2.3.1** **Dominio de la Modelación**

En la Figura 2-1 se presenta el dominio de modelación, el cual corresponde a un área de

40 × 32 kilómetros con 1280 celdas de 1.000 × 1.000 m.

**Figura 2-1 - Dominio de Modelación.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

5

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.3.2** **Topografía del Sector**

La topografía del sector se ha extraído de Shuttle Radar Topography Mission, SRTM1, cuya

resolución es aproximadamente 30 m.

El archivo SRTM1 ha sido incorporado al modelo con el objetivo de proporcionar la altura

de los puntos de interés. En la Figura 2-2 se presenta una imagen de la información

utilizada.

**Figura 2-2 - Topografía del Dominio de Modelación.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

6

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.4** **Caracterización Meteorológica del Área del Proyecto**

En esta sección se presenta la caracterización de la meteorología observada y modelada

para el sector del proyecto.

**2.4.1** **Meteorología de Superficie - Valores Observados**

La meteorología de superficie utilizada para caracterizar el área del proyecto corresponde

a la registrada en las estaciones Rancagua I y Rancagua II. La Tabla 2-1 resume la

información de las estaciones a analizar junto con el período monitoreado considerado

para el estudio y las coordenadas de ubicación respectivas:

**Tabla 2-1 - Coordenadas de Ubicación Estaciones de Monitoreo Meteorológico.**

|Estación de<br>Monitoreo|Variables Meteorológicas<br>Registradas|Periodo monitoreado<br>considerado para este<br>estudio|Coordenadas UTM [Datum<br>WGS84]|Col5|
|---|---|---|---|---|
|**Estación de**<br>**Monitoreo**|**Variables Meteorológicas**<br>**Registradas**|**Periodo monitoreado**<br>**considerado para este**<br>**estudio**|**Este [m]**|**Norte [m]**|
|Rancagua I|Velocidad del Viento [m/s]<br>Dirección del Viento [°]<br>Temperatura del Aire [°C]<br>Humedad Relativa [%]<br>Radiación Solar [W/m2]|Enero de 2015 a diciembre<br>de 2017|342.015|6.218.523|
|Rancagua II|Velocidad del Viento [m/s]<br>Dirección del Viento [°]<br>Temperatura del Aire [°C]<br>Humedad Relativa [%]<br>Radiación Solar [W/m2]|Enero de 2015 a diciembre<br>de 2017|339.842|6.220.527|

Fuente: Elaboración propia a partir de información disponible en SINCA.

La Figura 2-3 muestra la ubicación de las estaciones de monitoreo meteorológico:

www.dfmconsultores.cl

**info@dfmconsultores.cl**

7

www.dfmconsultores.cl

**info@dfmconsultores.cl**

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-3 - Ubicación Referencial Estaciones de Monitoreo Meteorológico.**

Fuente: Elaboración propia.

8

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.4.1.1** **Estación Rancagua I**

a) Velocidad y Dirección del Viento

En la Tabla 2-2 se presenta el resumen de información para la variable velocidad viento;

promedio, máximo y mínimo además del porcentaje de calmas, que se define como el

porcentaje del tiempo en que la velocidad del viento es menor 0,5 m/s, para el período en

estudio. De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del

Aire en el SEIA”, las series de datos meteorológicos deben contener un 75% de datos

válidos, lo que se cumple para los años 2015, 2016 y 2017:

**Tabla 2-2. Resumen de Información Velocidad del Viento Observada. Estación Rancagua I.**

|Parámetro|Variable|Año|Col4|Col5|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2015**|**2016**|**2017**|
|Velocidad de<br>Viento (m/s)|Promedio|1,59|1,46|1,44|
|Velocidad de<br>Viento (m/s)|Máxima|6,80|6,90|6,60|
|Velocidad de<br>Viento (m/s)|Mínima|0,20|0,00|0,00|
|Velocidad de<br>Viento (m/s)|Porcentaje de Calmas (%)|0,53%|3,49%|2,20%|
|Velocidad de<br>Viento (m/s)|Datos Válidos (%)|99,76%|99,84%|97,99%|

Fuente: Elaboración Propia.

A continuación, se presentan las series de tiempo y ciclos diarios observados para las

variables meteorológicas velocidad del viento y dirección del viento.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

9

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Series de Tiempo

A modo de verificación de la completitud de datos se presenta en la Figura 2-4 la serie de

tiempo para la variable velocidad del viento, mientras que en la Figura 2-5 se presenta la

serie de tiempo para la variable dirección del viento:

**Figura 2-4. Serie de Tiempo para Velocidad del Viento. Período enero 2015 a diciembre 2017. Observado**

**en Estación Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

10

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-5. Serie de Tiempo para Dirección del Viento. Período enero 2015 a diciembre 2017 - Observado**

**en Estación Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

11

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Para caracterizar la información anual registrada tanto para la velocidad como para la

dirección del viento se presenta en la Tabla 2-3 la frecuencia de distribución para la

velocidad y dirección del viento observada:

**Tabla 2-3 - Frecuencia de Distribución, Velocidad y Dirección del Viento. Periodo enero 2015 a diciembre**

**2017. Observado en Estación Rancagua I.**

|Dirección|Col2|Distribución Porcentual de Velocidad del Viento (m/s)|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Dirección**|**Dirección**|**0,50 - 2,10**|**2,10 - 3,60**|**3,60 - 5,70**|**5,70 - 8,80**|**8,80 - 11,10**|**>= 11,10**|**Total (%)**|
|348,75 - 11,25|N|1,92%|0,23%|0,06%|0,00%|0,00%|0,00%|2,20%|
|11,25 - 33,75|NNE|1,88%|0,48%|0,27%|0,02%|0,00%|0,00%|2,65%|
|33,75 - 56,25|NE|1,91%|0,60%|0,20%|0,01%|0,00%|0,00%|2,72%|
|56,25 - 78,75|ENE|1,64%|0,38%|0,03%|0,00%|0,00%|0,00%|2,05%|
|78,75 - 101,25|E|1,60%|0,19%|0,02%|0,00%|0,00%|0,00%|1,81%|
|101,25 - 123,75|ESE|1,95%|0,06%|0,04%|0,00%|0,00%|0,00%|2,06%|
|123,75 - 146,25|SE|3,48%|0,07%|0,00%|0,00%|0,00%|0,00%|3,55%|
|146,25 - 168,75|SSE|7,75%|0,49%|0,02%|0,00%|0,00%|0,00%|8,26%|
|168,75 - 191,25|S|8,44%|0,21%|0,00%|0,00%|0,00%|0,00%|8,66%|
|191,25 - 213,75|SSW|12,86%|7,78%|0,24%|0,00%|0,00%|0,00%|20,88%|
|213,75 - 236,25|SW|20,45%|8,55%|0,18%|0,00%|0,00%|0,00%|29,18%|
|236,25 - 258,75|WSW|5,71%|0,38%|0,00%|0,00%|0,00%|0,00%|6,09%|
|258,75 - 281,25|W|2,41%|0,07%|0,00%|0,00%|0,00%|0,00%|2,49%|
|281,25 - 303,75|WNW|1,81%|0,03%|0,00%|0,00%|0,00%|0,00%|1,84%|
|303,75 - 326,25|NW|1,69%|0,03%|0,00%|0,00%|0,00%|0,00%|1,73%|
|326,25 - 348,75|NNW|1,65%|0,09%|0,02%|0,00%|0,00%|0,00%|1,76%|
|Sub-Total|Sub-Total|77,15%|19,64%|1,09%|0,05%|0,00%|0,00%|97,93%|
|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|2,07%|

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

12

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Ciclos Diarios

En la Figura 2-6 se presenta el ciclo diario para la variable velocidad del viento, donde se

puede observar que las menores velocidades ocurren en el período nocturno y de

madrugada, entre las 00:00 horas y las 08:00 horas con un mínimo promedio aproximado

de 1 m/s entre las 05:00 y 06:00 horas, luego la velocidad comienza a incrementar

sostenidamente, alcanzando las mayores intensidades de viento a las 15:00 horas con un

máximo promedio aproximado de 2,3 m/s, posteriormente la velocidad desciende hasta

alcanzar los valores nocturnos.

**Figura 2-6 Ciclo Diario de Velocidad del Viento. Periodo enero 2015 a diciembre 2017 - Observado en**

**Estación Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

13

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-7 se presenta el ciclo diario de dirección del viento, se puede observar que

durante el periodo diurno predominan vientos con componentes sursudoeste y sudoeste.

Durante el periodo nocturno se tienen vientos de menores frecuencia de las direcciones

sursudoeste y sudoeste, además se observan vientos de las direcciones sursudeste y sur.

**Figura 2-7 Ciclo Diario dirección del Viento. Periodo enero 2015 a diciembre 2017 - Observado en Estación**

**Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

14

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-8 se presenta el ciclo diario anual de vientos observado, se puede apreciar

que las mayores intensidades de viento se producen en los meses de verano durante el

periodo diurno, entre las 13:00 y las 17:00 horas. En cuanto a la dirección del viento, se

observa que es predominantemente suroeste y durante el periodo diurno, durante el

periodo nocturno es predominantemente sur y sudsudoeste.

**Figura 2-8 - Ciclo Diario Anual Vientos. Período enero 2015 a diciembre 2017. Observado en Estación**

**Rancagua I.**

**Fuente: Elaboración Propia.**

www.dfmconsultores.cl

**info@dfmconsultores.cl**

15

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

b) Temperatura

En la Tabla 2-4 se presenta el resumen de información para la variable temperatura;

promedio, máximo y mínimo. De acuerdo con lo establecido en la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA”, las series de datos meteorológicos deben

contener un 75% de datos válidos, lo que se cumple para los años 2015, 2016 y 2017:

**Tabla 2-4 - Resumen de Información Temperatura Observada en Estación Rancagua I.**

|Parámetro|Variable|Año|Col4|Col5|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2015**|**2016**|**2017**|
|Temperatura<br>(°C)|Promedio|17,98|18,00|17,57|
|Temperatura<br>(°C)|Máxima|36,50|37,10|37,00|
|Temperatura<br>(°C)|Mínima|1,40|1,60|-1,00|
|Temperatura<br>(°C)|Datos Válidos (%)|99,76%|99,84%|97,99%|

Fuente: Elaboración Propia.

A continuación, se presentan la serie de tiempo y los ciclos diarios observados para la

variable meteorológica temperatura.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

16

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Serie de Tiempo

A modo de verificación de la completitud de los datos, en la Figura 2-9 se presenta la serie

de tiempo para la variable meteorológica temperatura:

**Figura 2-9 - Serie de Tiempo para la Temperatura. Período enero 2015 a diciembre 2017. Observado en**

**Estación Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

17

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Ciclo Diario

En la Figura 2-10 se presenta el ciclo diario para la variable temperatura. Como se puede

observar, las menores temperaturas ocurren durante el período nocturno y de madrugada

entre las 00:00 y las 07:00 horas, donde se alcanza un mínimo promedio aproximado de

12°C entre las 05:00 y 06:00 horas. A partir de las 06:00 horas la temperatura comienza a

aumentar hasta alcanzar un máximo promedio de alrededor de 24°C cerca de las 15:00

horas, para posteriormente descender en forma gradual hasta llegar a los valores

nocturnos.

**Figura 2-10 - Ciclo Diario Temperatura. Período enero 2015 a diciembre 2017. Observado en Estación**

**Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

18

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-11 se presenta el ciclo diario anual de la temperatura observada, se aprecia

que las mayores temperaturas se obtienen durante los meses de verano en el periodo

diurno, en particular en el mes de enero entre las 14:00 y las 17:00 horas. Por otro lado,

las menores temperaturas se obtienen en los meses de invierno en el periodo de

madrugada, en particular en el mes de junio de las 06:00 a las 7:00 horas.

**Figura 2-11 - Ciclo Diario Anual de Temperatura. Período enero 2015 a diciembre 2017. Observado en**

**Estación Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

19

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

c) Humedad Relativa

En la Tabla 2-5 se presenta el resumen de información para la variable humedad relativa;

promedio, máximo y mínimo. De acuerdo con lo establecido en la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA”, las series de datos meteorológicos deben

contener un 75% de datos válidos, lo que se cumple para los años 2015, 2016 y 2017:

**Tabla 2-5. Resumen de Información Humedad Relativa Observada en Estación Rancagua I.**

|Parámetro|Variable|Año|Col4|Col5|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2015**|**2016**|**2017**|
|Humedad<br>Relativa (%)|Promedio|57,02|60,84|59,57|
|Humedad<br>Relativa (%)|Máxima|92,00|92,00|92,00|
|Humedad<br>Relativa (%)|Mínima|10,00|6,00|0,00|
|Humedad<br>Relativa (%)|% Datos Válidos|99,76%|99,84%|97,99%|

Fuente: Elaboración Propia.

A continuación, se presentan la serie de tiempo y los ciclos diarios observados para la

variable meteorológica humedad relativa.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

20

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Serie de Tiempo

A modo de verificación de la completitud de los datos, en la Figura 2-12 se presenta la

serie de tiempo para la variable meteorológica humedad relativa:

**Figura 2-12. Serie de Tiempo Humedad Relativa. Periodo enero 2015 a diciembre 2017. Observado en**

**Estación Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

21

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Ciclo Diario

En la Figura 2-13 se presenta el ciclo diario para la variable humedad relativa. Como se

puede observar, en el periodo nocturno y de madrugada se presentan los mayores valores

de humedad relativa entre las 00:00 y las 07:00 horas, alcanzando un máximo promedio

de aproximadamente de un 75% a las 06:00 horas. Luego, la humedad relativa comienza a

descender a lo largo del día alcanzando un mínimo promedio aproximado de 41% a las

15:00 horas, para luego comenzar a aumentar hasta alcanzar los valores nocturnos.

**Figura 2-13. Ciclo Diario de Humedad Relativa. Período enero 2015 a diciembre 2017. Observado en**

**Estación Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

22

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-14 se presenta el ciclo diario anual de la humedad relativa observada, se
aprecia que los mayores valores de humedad relativa se obtienen durante los meses de
invierno en el periodo nocturno, alcanzando los máximos valores aproximadamente entre
las 05:00 y las 07:00 horas en el mes de agosto. Por otro lado, durante los meses de
verano en el periodo diurno se tienen los menores valores de humedad relativa, en
particular en diciembre y enero aproximadamente de las 15:00 a las 17:00 horas.

**Figura 2-14 Ciclo Diario Anual de Humedad Relativa. Período enero 2015 a diciembre 2017. Observado en**

**Estación Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

23

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

d) Radiación Solar

En la Tabla 2-6 se presenta el resumen de información para la variable radiación solar;

promedio, máximo y mínimo. De acuerdo con lo establecido en la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA”, las series de datos meteorológicos deben

contener un 75% de datos válidos, lo que se cumple para los años 2015, 2016 y 2017:

**Tabla 2-6. Resumen de Información Radiación Solar Observada en Estación Rancagua I.**

|Parámetro|Variable|Año|Col4|Col5|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2015**|**2016**|**2017**|
|Radiación Solar (W/m2)|Promedio|364,37|376,66|374,14|
|Radiación Solar (W/m2)|Máxima|1464,00|1226,00|1049,00|
|Radiación Solar (W/m2)|Mínima|0,00|0,00|0,00|
|Radiación Solar (W/m2)|% Datos Válidos|58,20%|50,16%|49,14%|

Fuente: Elaboración Propia.

A continuación, se presentan la serie de tiempo y los ciclos diarios observados para la

variable meteorológica radiación solar.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

24

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Serie de Tiempo

A modo de verificación de la completitud de los datos, en la Figura 2-15 se presenta la

serie de tiempo para la variable meteorológica radiación solar:

**Figura 2-15. Serie de Tiempo Radiación Solar. Periodo enero 2015 a diciembre 2017. Observado en**

**Estación Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

25

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Ciclo Diario

En la Figura 2-16 se presenta el ciclo diario para la variable radiación solar. Se aprecia que

durante el periodo nocturno y de madrugada no hay radiación solar. Al comenzar el día,

partir de las 05:00 horas comienza a incrementar sostenidamente esta variable,
alcanzando un máximo promedio aproximado de 650 W/m [2] entre las 12:00 y las 13:00

horas. A partir de las 13:00 horas comienza a disminuir sostenidamente a hasta alcanzar

los valores nocturnos a las 20:00 horas.

**Figura 2-16. Ciclo Diario de Radiación Solar. Período enero 2015 a diciembre 2017. Observado en Estación**

**Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

26

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-17 se presenta el ciclo diario anual de la radiación solar observada. Como es

de esperar, durante todo el año en el periodo nocturno se aprecian nulos valores de

radiación solar. Los mayores valores de radiación solar se presentan durante el verano en

el periodo diurno, en particular en el mes de enero, desde las 12:00 a las 13:00 horas.

**Figura 2-17 Ciclo Diario Anual de Radiación Solar. Período enero 2015 a diciembre 2017. Observado en**

**Estación Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

27

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.4.1.2** **Estación Rancagua II**

a) Velocidad y Dirección del Viento

En la Tabla 2-2 se presenta el resumen de información para la variable velocidad viento;

promedio, máximo y mínimo además del porcentaje de calmas, que se define como el

porcentaje del tiempo en que la velocidad del viento es menor 0,5 m/s, para el período en

estudio. De acuerdo a lo establecido en la “Guía para el Uso de Modelos de Calidad del

Aire en el SEIA”, las series de datos meteorológicos deben contener un 75% de datos

válidos, lo que se cumple para los años 2015, 2016 y 2017:

**Tabla 2-7. Resumen de Información Velocidad del Viento Observada. Estación Rancagua II.**

|Parámetro|Variable|Año|Col4|Col5|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2015**|**2016**|**2017**|
|Velocidad de<br>Viento (m/s)|Promedio|2,25|2,13|2,17|
|Velocidad de<br>Viento (m/s)|Máxima|7,70|6,90|7,10|
|Velocidad de<br>Viento (m/s)|Mínima|0,00|0,00|0,00|
|Velocidad de<br>Viento (m/s)|Porcentaje de Calmas (%)|0,00%|4,84%|7,50%|
|Velocidad de<br>Viento (m/s)|Datos Válidos (%)|99,67%|99,41%|98,85%|

Fuente: Elaboración Propia.

A continuación, se presentan las series de tiempo y ciclos diarios observados para las

variables meteorológicas velocidad del viento y dirección del viento.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

28

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Series de Tiempo

A modo de verificación de la completitud de datos se presenta en la Figura 2-18 la serie de

tiempo para la variable velocidad del viento, mientras que en la Figura 2-19 se presenta la

serie de tiempo para la variable dirección del viento:

**Figura 2-18. Serie de Tiempo para Velocidad del Viento. Período enero 2015 a diciembre 2017. Observado**

**en Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

29

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-19. Serie de Tiempo para Dirección del Viento. Período enero 2015 a diciembre 2017 - Observado**

**en Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

30

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Para caracterizar la información anual registrada tanto para la velocidad como para la

dirección del viento se presenta en la Tabla 2-8 la frecuencia de distribución para la

velocidad y dirección del viento observada:

**Tabla 2-8 - Frecuencia de Distribución, Velocidad y Dirección del Viento. Periodo enero 2015 a diciembre**

**2017. Observado en Estación Rancagua II.**

|Dirección|Col2|Distribución Porcentual de Velocidad del Viento (m/s)|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Dirección**|**Dirección**|**0,50 - 2,10**|**2,10 - 3,60**|**3,60 - 5,70**|**5,70 - 8,80**|**8,80 - 11,10**|**>= 11,10**|**Total (%)**|
|348,75 - 11,25|N|1,91%|0,20%|0,07%|0,01%|0,00%|0,00%|2,19%|
|11,25 - 33,75|NNE|2,34%|0,26%|0,05%|0,00%|0,00%|0,00%|2,65%|
|33,75 - 56,25|NE|3,69%|0,29%|0,05%|0,00%|0,00%|0,00%|4,03%|
|56,25 - 78,75|ENE|3,63%|0,26%|0,04%|0,00%|0,00%|0,00%|3,92%|
|78,75 - 101,25|E|3,28%|0,20%|0,04%|0,00%|0,00%|0,00%|3,53%|
|101,25 - 123,75|ESE|3,10%|0,16%|0,03%|0,00%|0,00%|0,00%|3,29%|
|123,75 - 146,25|SE|4,03%|1,63%|0,56%|0,00%|0,00%|0,00%|6,22%|
|146,25 - 168,75|SSE|6,26%|12,35%|13,25%|0,28%|0,00%|0,00%|32,13%|
|168,75 - 191,25|S|6,21%|8,74%|4,01%|0,04%|0,00%|0,00%|18,99%|
|191,25 - 213,75|SSW|4,51%|1,28%|0,04%|0,00%|0,00%|0,00%|5,83%|
|213,75 - 236,25|SW|3,69%|0,34%|0,05%|0,00%|0,00%|0,00%|4,08%|
|236,25 - 258,75|WSW|2,24%|0,19%|0,04%|0,00%|0,00%|0,00%|2,46%|
|258,75 - 281,25|W|1,68%|0,16%|0,07%|0,01%|0,00%|0,00%|1,91%|
|281,25 - 303,75|WNW|1,24%|0,18%|0,11%|0,02%|0,00%|0,00%|1,55%|
|303,75 - 326,25|NW|1,04%|0,16%|0,07%|0,03%|0,00%|0,00%|1,31%|
|326,25 - 348,75|NNW|1,17%|0,20%|0,13%|0,01%|0,00%|0,00%|1,51%|
|Sub-Total|Sub-Total|50,00%|26,61%|18,59%|0,41%|0,00%|0,00%|95,61%|
|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|4,39%|

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

31

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Ciclos Diarios

En la Figura 2-20 se presenta el ciclo diario para la variable velocidad del viento, donde se

puede observar que las menores velocidades ocurren en el período nocturno y de

madrugada, entre las 00:00 horas y las 07:00 horas con un mínimo promedio aproximado

de 1,1 m/s a las 06:00 horas, luego la velocidad comienza a incrementar sostenidamente,

alcanzando las mayores intensidades de viento a las 15:00 horas con un máximo promedio

aproximado de 3,6 m/s, posteriormente la velocidad desciende hasta alcanzar los valores

nocturnos.

**Figura 2-20 Ciclo Diario de Velocidad del Viento. Periodo enero 2015 a diciembre 2017 - Observado en**

**Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

32

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-21 se presenta el ciclo diario de dirección del viento, se puede observar que

durante el período diurno existe predominancia de vientos sursureste y sur. Durante el

periodo nocturno se observa predominancia en la misma dirección que en el periodo

diurno pero con menor frecuencia.

**Figura 2-21 Ciclo Diario dirección del Viento. Periodo enero 2015 a diciembre 2017 - Observado en**

**Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

33

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-22 se presenta el ciclo diario anual de vientos observado, se puede apreciar

que las mayores intensidades de viento se producen en los meses de verano durante el

periodo diurno, entre las 14:00 y las 17:00 horas. En cuanto a la dirección del viento, se

observa que es predominantemente sudsudeste durante el periodo diurno. Para el

periodo nocturno se aprecian vientos con componentes sureste pero también este, con

menores intensidades de viento.

**Figura 2-22 - Ciclo Diario Anual Vientos. Período enero 2015 a diciembre 2017. Observado en Estación**

**Rancagua II.**

**Fuente: Elaboración Propia.**

www.dfmconsultores.cl

**info@dfmconsultores.cl**

34

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

b) Temperatura

En la Tabla 2-9 se presenta el resumen de información para la variable temperatura;

promedio, máximo y mínimo. De acuerdo a lo establecido en la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA”, las series de datos meteorológicos deben

contener un 75% de datos válidos, lo que se cumple para los años 2015, 2016 y 2017:

**Tabla 2-9 - Resumen de Información Temperatura Observada en Estación Rancagua II.**

|Parámetro|Variable|Año|Col4|Col5|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2015**|**2016**|**2017**|
|Temperatura<br>(°C)|Promedio|15,61|15,74|15,30|
|Temperatura<br>(°C)|Máxima|34,60|34,90|35,90|
|Temperatura<br>(°C)|Mínima|-2,50|-1,40|-3,70|
|Temperatura<br>(°C)|Datos Válidos (%)|99,67%|99,41%|98,85%|

Fuente: Elaboración Propia.

A continuación, se presentan la serie de tiempo y los ciclos diarios observados para la

variable meteorológica temperatura.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

35

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Serie de Tiempo

A modo de verificación de la completitud de los datos, en la Figura 2-23 se presenta la

serie de tiempo para la variable meteorológica temperatura:

**Figura 2-23 - Serie de Tiempo para la Temperatura. Período enero 2015 a diciembre 2017. Observado en**

**Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

36

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Ciclo Diario

En la Figura 2-24 se presenta el ciclo diario para la variable temperatura. Como se puede

observar, las menores temperaturas ocurren durante el período nocturno y de madrugada

9,5°C entre las 05:00 y 06:00 horas. A partir de las 06:00 horas la temperatura comienza a

aumentar hasta alcanzar un máximo promedio de alrededor de 22°C a de las 15:00 horas,

para posteriormente descender en forma gradual hasta llegar a los valores nocturnos.

**Figura 2-24 - Ciclo Diario Temperatura. Período enero 2015 a diciembre 2017. Observado en Estación**

**Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

37

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-25 se presenta el ciclo diario anual de la temperatura observada, se aprecia

que las mayores temperaturas se obtienen durante los meses de verano en el periodo

diurno, en particular en el mes de enero de las 15:00 a las 16:00 horas. Por otro lado, las

menores temperaturas se obtienen en los meses de invierno en el periodo de madrugada,

en particular en el mes de junio de las 04:00 a las 7:00 horas.

**Figura 2-25 - Ciclo Diario Anual de Temperatura. Período enero 2015 a diciembre 2017. Observado en**

**Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

38

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

c) Humedad Relativa

En la Tabla 2-10 se presenta el resumen de información para la variable humedad relativa;

promedio, máximo y mínimo. De acuerdo a lo establecido en la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA”, las series de datos meteorológicos deben

contener un 75% de datos válidos, lo que se cumple para los años 2015, 2016 y 2017:

**Tabla 2-10. Resumen de Información Humedad Relativa Observada en Estación Rancagua II.**

|Parámetro|Variable|Año|Col4|Col5|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2015**|**2016**|**2017**|
|Humedad<br>Relativa (%)|Promedio|61,24|64,30|62,82|
|Humedad<br>Relativa (%)|Máxima|95,00|95,00|95,00|
|Humedad<br>Relativa (%)|Mínima|9,00|7,00|0,00|
|Humedad<br>Relativa (%)|% Datos Válidos|99,67%|99,41%|98,82%|

Fuente: Elaboración Propia.

A continuación, se presentan la serie de tiempo y los ciclos diarios observados para la

variable meteorológica humedad relativa.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

39

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Serie de Tiempo

A modo de verificación de la completitud de los datos, en la Figura 2-26 se presenta la

serie de tiempo para la variable meteorológica humedad relativa:

**Figura 2-26. Serie de Tiempo Humedad Relativa. Periodo enero 2015 a diciembre 2017. Observado en**

**Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

40

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Ciclo Diario

En la Figura 2-27 se presenta el ciclo diario para la variable humedad relativa. Como se

puede observar, en el periodo nocturno y de madrugada se presentan los mayores valores

de humedad relativa entre las 00:00 y las 08:00 horas, alcanzando un máximo promedio

de aproximadamente un 81% a las 05:00 horas. Luego, la humedad relativa comienza a

descender a lo largo del día alcanzando un mínimo promedio aproximado de 42% a las

15:00 horas, para luego comenzar a aumentar hasta alcanzar los valores nocturnos.

**Figura 2-27. Ciclo Diario de Humedad Relativa. Período enero 2015 a diciembre 2017. Observado en**

**Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

41

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-28 se presenta el ciclo diario anual de la humedad observada, se aprecia que
los mayores valores de humedad relativa se obtienen durante los meses de invierno en el
periodo nocturno, alcanzando los máximos valores aproximadamente entre las 05:00 y las
07:00 horas durante el mes de julio. Por otro lado, durante los meses de verano en el
periodo diurno se tienen los menores valores de humedad relativa, en particular en
diciembre, enero y febrero aproximadamente de las 13:00 a las 18:00 horas.

**Figura 2-28 Ciclo Diario Anual de Humedad Relativa. Período enero 2015 a diciembre 2017. Observado en**

**Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

42

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

d) Radiación Solar

En la Tabla 2-11 se presenta el resumen de información para la variable radiación solar;

promedio, máximo y mínimo. De acuerdo a lo establecido en la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA”, las series de datos meteorológicos deben

contener un 75% de datos válidos, lo que se cumple para los años 2015, 2016 y 2017:

**Tabla 2-11. Resumen de Información Radiación Solar Observada en Estación Rancagua II.**

|Parámetro|Variable|Año|Col4|Col5|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2015**|**2016**|**2017**|
|Radiación Solar<br>(W/m2)|Promedio|192,49|183,70|188,13|
|Radiación Solar<br>(W/m2)|Máxima|1039,00|1036,00|1090,00|
|Radiación Solar<br>(W/m2)|Mínima|0,00|0,00|0,00|
|Radiación Solar<br>(W/m2)|% Datos Válidos|99,61%|99,39%|98,82%|

Fuente: Elaboración Propia.

A continuación, se presentan la serie de tiempo y los ciclos diarios observados para la

variable meteorológica radiación solar.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

43

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Serie de Tiempo

A modo de verificación de la completitud de los datos, en la Figura 2-29 se presenta la

serie de tiempo para la variable meteorológica radiación solar:

**Figura 2-29. Serie de Tiempo Radiación Solar. Periodo enero 2015 a diciembre 2017. Observado en**

**Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

44

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Ciclo Diario

En la Figura 2-30 se presenta el ciclo diario para la variable radiación solar. Se aprecia que

durante el periodo nocturno y de madrugada no hay radiación solar. Al comenzar el día,

partir de las 04:00 horas comienza a incrementar sostenidamente esta variable,
alcanzando un máximo promedio aproximado de 600 W/m [2] a las 12:00 horas. A partir de

las 14:00 horas comienza a disminuir sostenidamente a hasta alcanzar los valores

nocturnos a las 20:00 horas.

**Figura 2-30. Ciclo Diario de Radiación Solar. Período enero 2015 a diciembre 2017. Observado en Estación**

**Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

45

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-31 se presenta el ciclo diario anual de la radiación solar observada. Como es

de esperar, durante todo el año en el periodo nocturno se aprecian nulos valores de

radiación solar. Los mayores valores de radiación solar se presentan durante el verano en

el periodo diurno, en particular en el mes de enero y diciembre, desde las 11:00 a las

13:00 horas.

**Figura 2-31 Ciclo Diario Anual de Radiación Solar. Período enero 2015 a diciembre 2017. Observado en**

**Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

46

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.4.2** **Meteorología de Superficie - Valores Modelados**

**2.4.2.1** **Estación Rancagua I**

a) Velocidad y Dirección del Viento

En la Tabla 2-12 se presenta el resumen de información para la variable velocidad viento;

promedio, máximo y mínimo además del porcentaje de calmas, que se define como el

porcentaje del tiempo en que la velocidad del viento es menor 0,5 m/s, para el período en

estudio. De acuerdo a lo establecido en la “Guía para el Uso de Modelos de Calidad del

Aire en el SEIA”, las series de datos meteorológicos deben contener un 75% de datos

válidos, lo que se cumple para el año 2016 debido a que se cuenta con la completitud de

los datos a partir del modelo WRF:

**Tabla 2-12. Resumen de Información Velocidad del Viento Modelada. Estación Rancagua I.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2016**|
|Velocidad de Viento (m/s)|Promedio|2,52|
|Velocidad de Viento (m/s)|Máxima|10,11|
|Velocidad de Viento (m/s)|Mínima|0,02|
|Velocidad de Viento (m/s)|Porcentaje de Calmas (%)|3,53%|
|Velocidad de Viento (m/s)|Datos Válidos (%)|100,00%|

Fuente: Elaboración Propia.

A continuación, se presentan las series de tiempo y ciclos diarios modelados para las

variables meteorológicas velocidad del viento y dirección del viento.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

47

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Series de Tiempo

A modo de verificación de la completitud de datos se presenta en la Figura 2-32 la serie de

tiempo para la variable velocidad del viento, mientras que en la Figura 2-33 se presenta la

serie de tiempo para la variable dirección del viento:

**Figura 2-32. Serie de Tiempo para Velocidad del Viento. Período enero a diciembre 2016. Modelado en**

**Estación Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

48

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-33. Serie de Tiempo para Dirección del Viento. Período enero a diciembre 2016. Modelado en**

**Estación Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

49

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Para caracterizar la información anual registrada tanto para la velocidad como para la

dirección del viento se presenta en la Tabla 2-13 la frecuencia de distribución para la

velocidad y dirección del viento observada:

**Tabla 2-13 - Frecuencia de Distribución, Velocidad y Dirección del Viento. Período enero a diciembre 2016.**

**Modelado en Estación Rancagua I.**

|Dirección|Col2|Distribución Porcentual de Velocidad del Viento (m/s)|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Dirección**|**Dirección**|**0,50 -**<br>**2,10**|**2,10 -**<br>**3,60**|**3,60 -**<br>**5,70**|**5,70 -**<br>**8,80**|**8,80 -**<br>**11,10**|**>=**<br>**11,10**|**Total**<br>**(%)**|
|348,75 - 11,25|N|1,05%|0,80%|1,90%|0,88%|0,10%|0,00%|4,72%|
|11,25 - 33,75|NNE|2,41%|1,97%|0,87%|0,38%|0,02%|0,00%|5,65%|
|33,75 - 56,25|NE|3,56%|1,66%|0,46%|0,02%|0,00%|0,00%|5,70%|
|56,25 - 78,75|ENE|1,98%|0,76%|0,13%|0,01%|0,00%|0,00%|2,88%|
|78,75 - 101,25|E|1,53%|0,46%|0,09%|0,00%|0,00%|0,00%|2,07%|
|101,25 - 123,75|ESE|1,50%|0,27%|0,14%|0,03%|0,00%|0,00%|1,95%|
|123,75 - 146,25|SE|1,55%|0,18%|0,07%|0,00%|0,00%|0,00%|1,80%|
|146,25 - 168,75|SSE|1,48%|0,33%|0,05%|0,01%|0,00%|0,00%|1,87%|
|168,75 - 191,25|S|2,28%|0,59%|0,10%|0,00%|0,00%|0,00%|2,97%|
|191,25 - 213,75|SSW|5,29%|4,16%|2,15%|0,19%|0,00%|0,00%|11,79%|
|213,75 - 236,25|SW|10,25%|17,70%|8,99%|0,72%|0,01%|0,00%|37,67%|
|236,25 - 258,75|WSW|4,37%|3,11%|1,92%|0,56%|0,00%|0,00%|9,96%|
|258,75 - 281,25|W|1,34%|0,42%|0,22%|0,01%|0,00%|0,00%|1,99%|
|281,25 - 303,75|WNW|0,88%|0,51%|0,47%|0,11%|0,00%|0,00%|1,97%|
|303,75 - 326,25|NW|0,81%|0,48%|0,60%|0,06%|0,00%|0,00%|1,95%|
|326,25 - 348,75|NNW|0,81%|0,34%|0,23%|0,13%|0,02%|0,00%|1,53%|
|Sub-Total|Sub-Total|41,09%|33,74%|18,37%|3,11%|0,16%|0,00%|96,47%|
|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|3,53%|

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

50

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Ciclos Diarios

En la Figura 2-34 se presenta el ciclo diario para la variable velocidad del viento, donde se

puede observar que las menores velocidades ocurren en el período nocturno y de

madrugada, entre las 00:00 horas y las 08:00 horas con un mínimo promedio aproximado

de 1,6 m/s a las 07:00 horas, luego la velocidad comienza a incrementar sostenidamente,

alcanzando las mayores intensidades de viento a las 18:00 horas con un máximo promedio

aproximado de 4 m/s, posteriormente la velocidad desciende hasta alcanzar los valores

nocturnos.

**Figura 2-34 Ciclo Diario de Velocidad del Viento. Período enero a diciembre 2016. Modelado en Estación**

**Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

51

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-35 se presenta el ciclo diario de dirección del viento, se puede observar que

durante el período diurno y nocturno existe predominancia de vientos con componente

sursuroeste y suroeste.

**Figura 2-35 Ciclo Diario dirección del Viento. Período enero a diciembre 2016. Modelado en Estación**

**Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

52

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-36 se presenta el ciclo diario anual de vientos observado, se puede apreciar

que las mayores intensidades de viento se producen en los meses de verano y primavera

durante el periodo diurno, entre las 17:00 y las 18:00 horas. En cuanto a la dirección del

viento, se observa que es predominantemente suroeste tanto para el periodo diurno

como nocturno.

**Figura 2-36 - Ciclo Diario Anual Vientos. Período enero a diciembre 2016. Modelado en Estación**

**Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

53

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

b) Temperatura

En la Tabla 2-14 se presenta el resumen de información para la variable temperatura;

promedio, máximo y mínimo. De acuerdo a lo establecido en la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA”, las series de datos meteorológicos deben

contener un 75% de datos válidos, lo que se cumple para el año 2016 debido a que se

cuenta con la completitud de los datos a partir del modelo WRF:

**Tabla 2-14 - Resumen de Información Temperatura Modelada en Estación Rancagua I.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2016**|
|Temperatura (°C)|Promedio|19,39|
|Temperatura (°C)|Máxima|37,17|
|Temperatura (°C)|Mínima|4,21|
|Temperatura (°C)|Datos Válidos (%)|100,00%|

Fuente: Elaboración Propia.

A continuación, se presentan la serie de tiempo y los ciclos diarios modelados para la

variable meteorológica temperatura.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

54

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Serie de Tiempo

A modo de verificación de la completitud de los datos, en la Figura 2-37 se presenta la

serie de tiempo para la variable meteorológica temperatura:

**Figura 2-37 - Serie de Tiempo para la Temperatura. Período enero a diciembre 2016. Modelado en**

**Estación Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

55

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Ciclo Diario

En la Figura 2-38 se presenta el ciclo diario para la variable temperatura. Como se puede

observar, las menores temperaturas ocurren durante el período nocturno y de madrugada

entre las 00:00 y las 08:00 horas, donde se alcanza un mínimo promedio aproximado de

15°C a las 06:00 horas. A partir de las 06:00 horas la temperatura comienza a aumentar

hasta alcanzar un máximo promedio de alrededor de 25°C entre las 15:00 y 16:00 horas,

para posteriormente descender en forma gradual hasta llegar a los valores nocturnos.

**Figura 2-38 - Ciclo Diario Temperatura. Período enero a diciembre 2016. Modelado en Estación**

**Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

56

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-39 se presenta el ciclo diario anual de la temperatura observada, se aprecia

que las mayores temperaturas se obtienen durante los meses de verano en el periodo

diurno, de las 14:00 a las 17:00 horas. Por otro lado, las menores temperaturas se

obtienen en los meses de invierno en el periodo de madrugada, de las 05:00 a las 8:00

horas.

**Figura 2-39 - Ciclo Diario Anual de Temperatura. Período enero a diciembre 2016. Modelado en Estación**

**Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

57

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.4.2.2** **Estación Rancagua II**

a) Velocidad y Dirección del Viento

En la Tabla 2-15 se presenta el resumen de información para la variable velocidad viento;

promedio, máximo y mínimo además del porcentaje de calmas, que se define como el

porcentaje del tiempo en que la velocidad del viento es menor 0,5 m/s, para el período en

estudio. De acuerdo a lo establecido en la “Guía para el Uso de Modelos de Calidad del

Aire en el SEIA”, las series de datos meteorológicos deben contener un 75% de datos

válidos, lo que se cumple para el año 2016 debido a que se cuenta con la completitud de

los datos a partir del modelo WRF:

**Tabla 2-15. Resumen de Información Velocidad del Viento Modelada. Estación Rancagua II.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2016**|
|Velocidad de Viento (m/s)|Promedio|2,52|
|Velocidad de Viento (m/s)|Máxima|9,92|
|Velocidad de Viento (m/s)|Mínima|0,04|
|Velocidad de Viento (m/s)|Porcentaje de Calmas (%)|4,08%|
|Velocidad de Viento (m/s)|Datos Válidos (%)|100,00%|

Fuente: Elaboración Propia.

A continuación, se presentan las series de tiempo y ciclos diarios modelados para las

variables meteorológicas velocidad del viento y dirección del viento.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

58

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Series de Tiempo

A modo de verificación de la completitud de datos se presenta en la Figura 2-40 la serie de

tiempo para la variable velocidad del viento, mientras que en la Figura 2-41 se presenta la

serie de tiempo para la variable dirección del viento:

**Figura 2-40. Serie de Tiempo para Velocidad del Viento. Período enero a diciembre 2016. Modelado en**

**Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

59

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-41. Serie de Tiempo para Dirección del Viento. Período enero a diciembre 2016. Modelado en**

**Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

60

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Para caracterizar la información anual registrada tanto para la velocidad como para la

dirección del viento se presenta en la Tabla 2-16 la frecuencia de distribución para la

velocidad y dirección del viento observada:

**Tabla 2-16 - Frecuencia de Distribución, Velocidad y Dirección del Viento. Período enero a diciembre 2016.**

**Modelado en Estación Rancagua II.**

|Dirección|Col2|Distribución Porcentual de Velocidad del Viento (m/s)|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Dirección**|**Dirección**|**0,50 - 2,10**|**2,10 - 3,60**|**3,60 - 5,70**|**5,70 - 8,80**|**8,80 - 11,10**|**>= 11,10**|**Total (%)**|
|348,75 - 11,25|N|0,96%|0,66%|1,01%|0,49%|0,01%|0,00%|3,13%|
|11,25 - 33,75|NNE|1,94%|1,15%|1,79%|0,76%|0,08%|0,00%|5,71%|
|33,75 - 56,25|NE|3,35%|1,65%|0,44%|0,01%|0,00%|0,00%|5,45%|
|56,25 - 78,75|ENE|3,18%|1,05%|0,14%|0,03%|0,00%|0,00%|4,39%|
|78,75 - 101,25|E|1,72%|0,51%|0,05%|0,01%|0,00%|0,00%|2,29%|
|101,25 - 123,75|ESE|1,21%|0,17%|0,06%|0,01%|0,00%|0,00%|1,45%|
|123,75 - 146,25|SE|0,72%|0,11%|0,01%|0,01%|0,00%|0,00%|0,85%|
|146,25 - 168,75|SSE|0,91%|0,27%|0,03%|0,00%|0,00%|0,00%|1,22%|
|168,75 - 191,25|S|2,08%|0,85%|0,09%|0,01%|0,00%|0,00%|3,04%|
|191,25 - 213,75|SSW|9,18%|11,02%|4,57%|0,17%|0,00%|0,00%|24,93%|
|213,75 - 236,25|SW|8,94%|14,28%|6,71%|0,89%|0,00%|0,00%|30,81%|
|236,25 - 258,75|WSW|2,22%|1,55%|1,26%|0,25%|0,00%|0,00%|5,28%|
|258,75 - 281,25|W|1,14%|0,49%|0,24%|0,01%|0,00%|0,00%|1,88%|
|281,25 - 303,75|WNW|0,66%|0,47%|0,90%|0,17%|0,00%|0,00%|2,20%|
|303,75 - 326,25|NW|0,61%|0,50%|0,80%|0,03%|0,00%|0,00%|1,95%|
|326,25 - 348,75|NNW|0,77%|0,27%|0,17%|0,13%|0,00%|0,00%|1,34%|
|Sub-Total|Sub-Total|39,57%|35,01%|18,26%|2,99%|0,09%|0,00%|95,92%|
|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|4,08%|

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

61

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Ciclos Diarios

En la Figura 2-42 se presenta el ciclo diario para la variable velocidad del viento, donde se

puede observar que las menores velocidades ocurren en el período de madrugada, entre

las 02:00 horas y las 08:00 horas con un mínimo promedio aproximado de 1,6 m/s a las

06:00 horas. Luego, la velocidad comienza a incrementar sostenidamente, alcanzando las

mayores intensidades de viento a las 18:00 horas con un máximo promedio aproximado

de 4 m/s, posteriormente la velocidad desciende hasta alcanzar los valores nocturnos.

**Figura 2-42 Ciclo Diario de Velocidad del Viento. Período enero a diciembre 2016. Modelado en Estación**

**Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

62

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-43 se presenta el ciclo diario de dirección del viento, se puede observar que

durante el período diurno y nocturno existe predominancia de vientos sursuroeste y

suroeste.

**Figura 2-43 Ciclo Diario dirección del Viento. Período enero a diciembre 2016. Modelado en Estación**

**Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

63

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-44 se presenta el ciclo diario anual de vientos observado, se puede apreciar

que las mayores intensidades de viento se producen en los meses de verano y primavera

durante el periodo diurno, entre las 17:00 y las 19:00 horas. En cuanto a la dirección del

viento, se observan vientos predominantemente sudsudoeste durante los meses de

agosto a marzo, en los meses de abril a julio, lo vientos presentan mayor variabilidad a lo

largo del día.

**Figura 2-44 - Ciclo Diario Anual Vientos. Período enero a diciembre 2016. Modelado en Estación Rancagua**

**II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

64

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

b) Temperatura

En la Tabla 2-17 se presenta el resumen de información para la variable temperatura;

promedio, máximo y mínimo. De acuerdo a lo establecido en la “Guía para el Uso de

Modelos de Calidad del Aire en el SEIA”, las series de datos meteorológicos deben

contener un 75% de datos válidos, lo que se cumple para el año 2016 debido a que se

cuenta con la completitud de los datos a partir del modelo WRF:

**Tabla 2-17 - Resumen de Información Temperatura Modelada en Estación Rancagua II.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2016**|
|Temperatura (°C)|Promedio|19,52|
|Temperatura (°C)|Máxima|37,27|
|Temperatura (°C)|Mínima|4,80|
|Temperatura (°C)|Datos Válidos (%)|100,00%|

Fuente: Elaboración Propia.

A continuación, se presentan la serie de tiempo y los ciclos diarios modelados para la

variable meteorológica temperatura.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

65

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Serie de Tiempo

A modo de verificación de la completitud de los datos, en la Figura 2-45 se presenta la

serie de tiempo para la variable meteorológica temperatura:

**Figura 2-45 - Serie de Tiempo para la Temperatura. Período enero a diciembre 2016. Modelado en**

**Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

66

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Ciclo Diario

En la Figura 2-46 se presenta el ciclo diario para la variable temperatura. Como se puede

observar, las menores temperaturas ocurren durante el período de madrugada entre las

02:00 y las 08:00 horas, donde se alcanza un mínimo promedio aproximado de 15°C a las

06:00 horas. A partir de las 06:00 horas la temperatura comienza a aumentar hasta

alcanzar un máximo promedio de alrededor de 25°C cerca de las 15:00 horas, para

posteriormente descender en forma gradual hasta llegar a los valores nocturnos.

**Figura 2-46 - Ciclo Diario Temperatura. Período enero a diciembre 2016. Modelado en Estación Rancagua**

**II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

67

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-47 se presenta el ciclo diario anual de la temperatura observada, se aprecia

que las mayores temperaturas se obtienen durante los meses de verano en el periodo

diurno, de las 14:00 a las 17:00 horas. Por otro lado, las menores temperaturas se

obtienen en los meses de invierno en el periodo de madrugada, de las 04:00 a las 7:00

horas.

**Figura 2-47 - Ciclo Diario Anual de Temperatura. Período enero a diciembre 2016. Modelado en Estación**

**Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

68

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.4.3** **Meteorología de Altura - Valores Observados**

En relación a la meteorología de altura, no existen registros de mediciones disponibles en

las estaciones utilizadas.

**2.4.4** **Meteorología de Altura - Valores Modelados**

Se ha caracterizado la variable altura de la capa de mezcla, que es un parámetro obtenido

del procesamiento de los resultados de modelo meteorológico WRF. La altura de capa de

mezcla corresponde a la altura medida desde la superficie en la que la inestabilidad

favorece la dispersión vertical de contaminantes.

Para lo anterior, se han tomado los datos entregados por el modelo meteorológico WRF

en el sector de las cuatro estaciones meteorológicas. A continuación, se presentan los

valores entregados por el modelo.

**2.4.4.1** **Estación Rancagua I**

a) Altura de Capa de Mezcla

En la Tabla 2-18 se presenta el resumen de información para la variable altura de capa de

mezcla; promedio, máximo y mínimo para el periodo de estudio. De acuerdo a lo

establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, las series

de datos meteorológicos deben contener un 75% de datos válidos, lo que se cumple para

el año 2016 debido a que se cuenta con la completitud de los datos a partir del modelo

WRF:

**Tabla 2-18 - Resumen de Información Altura de Capa de Mezcla Modelada en Estación Rancagua I.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2016**|
|Altura de Capa de Mezcla (m)|Promedio|654,93|
|Altura de Capa de Mezcla (m)|Máxima|3.500,00|
|Altura de Capa de Mezcla (m)|Mínima|10,00|
|Altura de Capa de Mezcla (m)|% Datos Válidos|100,00%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración Propia.

69

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

A continuación, se presentan la serie de tiempo y el ciclo diario modelados para la variable

meteorológica altura de capa de mezcla.

Serie de tiempo

A modo de verificación de la completitud de datos, se presenta en la Figura 2-48 la serie

de tiempo para la variable altura de capa de mezcla.

**Figura 2-48 - Serie de Tiempo para Altura de Capa de Mezcla. Período enero a diciembre 2016. Modelado**

**en Estación Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

70

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Ciclo Diario

En la Figura 2-49 se presenta el ciclo diario para la variable altura de capa de mezcla,

donde se puede observar que durante el periodo nocturno y de madruga esta variable

tiene los menores valores. A partir de las 07:00 horas comienza a aumentar

sostenidamente hasta alcanzar un máximo promedio aproximado de 2.000 metros a las

15:00 horas, para luego descender hasta alcanzar los valores nocturnos.

**Figura 2-49 - Ciclo Diario de Altura de Capa de Mezcla. Período enero a diciembre 2016. Modelado en**

**Estación Rancagua I.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

71

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.4.4.2** **Estación Rancagua II**

a) Altura de Capa de Mezcla

En la Tabla 2-19 se presenta el resumen de información para la variable altura de capa de

mezcla; promedio, máximo y mínimo para el periodo de estudio. De acuerdo a lo

establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el SEIA”, las series

de datos meteorológicos deben contener un 75% de datos válidos, lo que se cumple para

el año 2016 debido a que se cuenta con la completitud de los datos a partir del modelo

WRF:

**Tabla 2-19 - Resumen de Información Altura de Capa de Mezcla Modelada en Estación Rancagua II.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2016**|
|Altura de Capa de Mezcla (m)|Promedio|663,86|
|Altura de Capa de Mezcla (m)|Máxima|3.500,00|
|Altura de Capa de Mezcla (m)|Mínima|10,00|
|Altura de Capa de Mezcla (m)|% Datos Válidos|100,00%|

Fuente: Elaboración Propia.

A continuación, se presentan la serie de tiempo y el ciclo diario modelados para la variable

meteorológica altura de capa de mezcla.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

72

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Serie de tiempo

A modo de verificación de la completitud de datos, se presenta en la Figura 2-50 la serie

de tiempo para la variable altura de capa de mezcla.

**Figura 2-50 - Serie de Tiempo para Altura de Capa de Mezcla. Período enero a diciembre 2016. Modelado**

**en Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

73

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Ciclo Diario

En la Figura 2-51 se presenta el ciclo diario para la variable altura de capa de mezcla,

donde se puede observar que durante el periodo nocturno y de madruga esta variable

tiene los menores valores. A partir de las 07:00 horas comienza a aumentar

sostenidamente hasta alcanzar un máximo promedio aproximado de 2.000 metros a las

15:00 horas, para luego descender hasta alcanzar los valores nocturnos.

**Figura 2-51 - Ciclo Diario de Altura de Capa de Mezcla. Período enero a diciembre 2016. Modelado en**

**Estación Rancagua II.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

74

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.5** **Análisis de Incertidumbre - Comparación Cualitativa**

Debido a que la meteorología de superficie es un factor relevante en la dispersión de los contaminantes, a continuación se busca

validar en forma cualitativa el modelo WRF que será utilizado en conjunto con el modelo de dispersión CALPUFF. Para llevar a cabo lo

anterior, se presenta una comparación de los datos observados en las estaciones Rancagua I y Rancagua II para el periodo

comprendido entre el 1 de enero y el 31 de diciembre del año 2016, mismo periodo para el que se realizó el modelo meteorológico

WRF. Así, se comparan ciclos diarios y anuales para las variables meteorológicas velocidad del viento, dirección del viento y

temperatura.

**2.5.1** **Velocidad y Dirección del Viento**

**2.5.1.1** **Estación Rancagua I**

En la Tabla 2-20 se presenta la comparación de los ciclos diarios y anuales de velocidad del viento y dirección del viento observado y

modelado:

**Tabla 2-20. Comparación Resultados Observados y Modelados de Velocidad del Viento y Dirección del Viento. Periodo enero a diciembre 2016. Estación**

**Rancagua I.**

**Comparación** **Observado** **Modelado**

www.dfmconsultores.cl

**info@dfmconsultores.cl**

75

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

|Comparación|Observado|Modelado|
|---|---|---|
|Ciclo Diario de<br>Velocidad del<br>Viento|||
|Ciclo Diario de<br>Dirección del<br>Viento|||

www.dfmconsultores.cl

**info@dfmconsultores.cl**

76

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

|Comparación|Observado|Modelado|
|---|---|---|
|Ciclo Diario<br>Anual de<br>Velocidad del<br>Viento y<br>Dirección del<br>Viento|||

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

77

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.5.1.2** **Estación Rancagua II**

En la Tabla 2-21 se presenta la comparación de los ciclos diarios y anuales de velocidad del viento y dirección del viento observado y

modelado:

**Tabla 2-21. Comparación Resultados Observados y Modelados de Velocidad del Viento y Dirección del Viento. Periodo enero a diciembre 2016. Estación**

**Rancagua II.**

|Comparación|Observado|Modelado|
|---|---|---|
|Ciclo Diario de<br>Velocidad del<br>Viento|||

www.dfmconsultores.cl

**info@dfmconsultores.cl**

78

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

|Comparación|Observado|Modelado|
|---|---|---|
|Ciclo Diario de<br>Dirección del<br>Viento|||
|Ciclo Diario<br>Anual de<br>Velocidad del<br>Viento y<br>Dirección del<br>Viento|||

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

79

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.5.2** **Temperatura**

**2.5.2.1** **Estación Rancagua I**

En la Tabla 2-22 se presenta la comparación de los ciclos diarios y anuales de temperatura observados y modelados:

**Tabla 2-22. Comparación Resultados Observados y Modelados de Temperatura. Periodo enero a diciembre 2016. Estación Rancagua I.**

|Comparación|Observado|Modelado|
|---|---|---|
|Ciclo Diario de<br>Temperatura|||

www.dfmconsultores.cl

**info@dfmconsultores.cl**

80

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

|Comparación|Observado|Modelado|
|---|---|---|
|Ciclo Diario<br>Anual de<br>Temperatura|||

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

81

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.5.2.2** **Estación Rancagua II**

En la Tabla 2-23 se presenta la comparación de los ciclos diarios y anuales de temperatura observados y modelados:

**Tabla 2-23. Comparación Resultados Observados y Modelados de Temperatura. Periodo enero a diciembre 2016. Estación Rancagua I.**

|Comparación|Observado|Modelado|
|---|---|---|
|Ciclo Diario de<br>Temperatura|||

www.dfmconsultores.cl

**info@dfmconsultores.cl**

82

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

|Comparación|Observado|Modelado|
|---|---|---|
|Ciclo Diario<br>Anual de<br>Temperatura|||

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

83

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.6** **Análisis de Incertidumbre - Comparación Cuantitativa**

Para realizar la comparación cuantitativa se han utilizado tres estadígrafos comúnmente

utilizados para la evaluación del _performance_ de modelos: Sesgo, Error Cuadrático Medio

y el coeficiente de correlación (r), dichos estadígrafos fueron calculados para los ciclos

diarios. A continuación, en la se presentan los estadígrafos:

**Tabla 2-24. Estadígrafos de Dispersión para Velocidad del Viento y Temperatura.**

|Medida de Error|Estación Rancagua I|Col3|Col4|Col5|
|---|---|---|---|---|
|**Medida de Error**|**Velocidad**|**Velocidad**|**Temperatura**|**Temperatura**|
|**Medida de Error**|**Serie de Tiempo**|**Ciclo Diario**|**Serie de Tiempo**|**Ciclo Diario**|
|Sesgo|1,06 m/s|1,06 m/s|1,39 °C|1,39 °C|
|ECM|1,64 m/s|1,17 m/s|3,10 °C|1,58 °C|
|r|0,54|0,89|0,91|0,98|
|**Medida de Error**|**Estación Rancagua II**|**Estación Rancagua II**|**Estación Rancagua II**|**Estación Rancagua II**|
|**Medida de Error**|**Velocidad**|**Velocidad**|**Temperatura**|**Temperatura**|
|**Medida de Error**|**Serie de Tiempo**|**Ciclo Diario**|**Serie de Tiempo**|**Ciclo Diario**|
|Sesgo|0,38 m/s|0,39 m/s|3,77 °C|3,78 °C|
|ECM|1,38 m/s|0,47 m/s|4,85 °C|3,89 °C|
|r|0,55|0,95|0,91|0,98|

Fuente: Elaboración Propia.

Dadas las medidas de dispersión expuestas se observa que el modelo en términos

generales representa de buena manera las variables velocidad del viento y temperatura

en las estaciones Rancagua I y II.

En el caso de la estación Rancagua I, la velocidad del viento muestra un coeficiente de

correlación bajo al comparar las series de datos observados y modelados, sin embargo, el

ajuste del ciclo diario tiene un buen resultado ya que el coeficiente de correlación es de

89%, por otra parte se observa una sobrestimación por parte del modelo de 1,06 m/s. En

el caso de la Temperatura, el coeficiente de correlación tanto para la serie de datos como

para los ciclos es alto, sobre 90%, sin embargo se observa una sobrestimación por parte

del modelo de 1,39 °C .

www.dfmconsultores.cl

**info@dfmconsultores.cl**

84

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En el caso de la estación Rancagua II, la velocidad del viento muestra un coeficiente de

correlación bajo al comparar las series de datos observados y modelados, sin embargo el

ajuste del ciclo diario tiene un buen resultado ya que el coeficiente de correlación es de

95%, por otra parte se observa una sobrestimación por parte del modelo de 0,39 m/s para

el ciclo diario. En el caso de la Temperatura, el coeficiente de correlación tanto para la

serie de datos como para los ciclos es alto, sobre 90%, sin embargo se observa una

sobrestimación por parte del modelo de 3,78 °C para el ciclo diario.

Finalmente Como el modelo sobrestima el comportamiento de la velocidad del viento,

esto se reflejará en una sobrestimación de la dispersión de los contaminantes, lo que

implicaría que los aportes del modelo no reflejen correctamente el aporte sobre

estaciones Rancagua I y II. Dado lo anterior, se ha decidido corregir los resultados de

modelación para cada uno de los receptores, multiplicando por el siguiente factor de

corrección (FC):

FC= [Velocidad Promedio Modelada]

Velocidad Promedio Observada

De esta forma, el factor de corrección en la Estación Rancagua I es de 1,73 y en la Estación
Rancagua II es de 1,18.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

85

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.7** **Normas de Calidad del Aire**

En la Tabla 2-25 se presenta la normativa de calidad del aire existente respecto de los

contaminantes de interés para el proyecto: material particulado respirable fino (MP 2,5),

material particulado respirable (MP10), dióxido de nitrógeno (NO 2 ), dióxido de azufre

(SO 2 ) y monóxido de carbono (CO).

**Tabla 2-25 - Normas de calidad del aire.**

|Contaminante|Decreto Aplicable|Norma|Col4|Periodo de Evaluación de<br>Cumplimiento de Norma|
|---|---|---|---|---|
|**Contaminante**|**Decreto Aplicable**|**Valor**|**Unidad**|**Unidad**|
|Material<br>Particulado<br>Respirable Fino<br>(MP2,5)|Decreto Supremo N°12/2011|50|μg/m3|Percentil 98 de la media<br>aritmética diaria durante un<br>año|
|Material<br>Particulado<br>Respirable Fino<br>(MP2,5)|Decreto Supremo N°12/2011|20|20|Media aritmética trianual|
|Material<br>Particulado<br>Respirable<br>(MP10)|Decreto Supremo N°59/98|150|μg/m3N|Percentil 98 de la media<br>aritmética diaria durante un<br>año|
|Material<br>Particulado<br>Respirable<br>(MP10)|Decreto Supremo N°59/98|50|50|Media aritmética trianual|
|Dióxido de<br>nitrógeno (NO2)|Decreto Supremo No114/02|400|μg/m3N <br>|Percentil 99 de la media<br>aritmética horaria durante un<br>año|
|Dióxido de<br>nitrógeno (NO2)|Decreto Supremo No114/02|100|μg/m~~3~~N|Media aritmética trianual|
|Dióxido de<br>azufre (SO2)|Decreto Supremo 113/02|250|μg/m3N <br>|Percentil 99 anual de la<br>media aritmética diaria|
|Dióxido de<br>azufre (SO2)|Decreto Supremo 113/02|80|μg/m~~3~~N|Media aritmética trianual|
|Monóxido de<br>Carbono (CO)|Decreto Supremo N°115/02|30|mg/m3N|Percentil 99 de la media<br>aritmética horaria durante un<br>año|
|Monóxido de<br>Carbono (CO)|Decreto Supremo N°115/02|10|mg/m3N|Percentil 99 de la media<br>aritmética de 8 horas durante<br>un año|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia.

86

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.8** **Calidad del Aire**

Las estaciones con las que se cuenta con información de monitoreo de Calidad del Aire

corresponden a la Estación Rancagua I y Rancagua II de propiedad del Ministerio del

Medio Ambiente, la estación Rancagua I cuenta actualmente con Monitoreo de Material

Particulado Respirable Fino (MP2,5), de Material Particulado Respirable (MP10), de

Monóxido de carbono (CO), y Dióxido de azufre (SO 2 ). Por otro lado, la Estación

Rancagua II cuenta con de Monitoreo de Material Particulado Respirable Fino (MP2,5) y

de Material Particulado Respirable (MP10). En la Tabla 2-26 se presentan las coordenadas

de ubicación de estas estaciones y en la Figura 2-52 se presenta la ubicación de estas.

**Tabla 2-26 - Estaciones monitoras de calidad del aire.**

|Nombre|Coordenadas UTM, Huso 19 S, Datum WGS-84|Col3|
|---|---|---|
|**Nombre**|**Este [m]**|**Norte [m]**|
|Estación Rancagua I|342.015|6.218.523|
|Estación Rancagua II|339.842|6.220.527|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

87

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-52. Ubicación Referencial Estaciones monitoras de Calidad del Aire.**

Fuente: Elaboración Propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

88

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Tabla 2-27 se presenta el resumen del monitoreo de los años 2015 a 2017 en la

Estación Rancagua I, y su contrastación contra las normas de calidad primarias.

**Tabla 2-27 -Calidad del Aire Estación Rancagua I.**

|Contaminante|Estadígrafo|Periodo|Valor|Unidad|Valor<br>Norma|Porcentaje de la<br>Norma|
|---|---|---|---|---|---|---|
|MP2,5|P98 24 horas|2015|74,7|μg/m3|50|149%|
|MP2,5|P98 24 horas|2016|88,9|88,9|88,9|178%|
|MP2,5|P98 24 horas|2017|73,0|73,0|73,0|146%|
|MP2,5|P98 24 horas|Mayor valor 2015-2017|88,9|88,9|88,9|178%|
|MP2,5|Promedio Anual|2015|24,2|24,2|20|121%|
|MP2,5|Promedio Anual|2016|24,4|24,4|24,4|122%|
|MP2,5|Promedio Anual|2017|23,6|23,6|23,6|118%|
|MP2,5|Promedio Anual|Promedio 2015-2017|24,1|24,1|24,1|120%|
|MP10|P98 24 horas|2015|181,7|μg/m3N|150|121%|
|MP10|P98 24 horas|2016|153,8|153,8|153,8|103%|
|MP10|P98 24 horas|2017|133,0|133,0|133,0|89%|
|MP10|P98 24 horas|Mayor valor 2015-2017|181,7|181,7|181,7|121%|
|MP10|Promedio Anual|2015|80,7|80,7|50|161%|
|MP10|Promedio Anual|2016|73,2|73,2|73,2|146%|
|MP10|Promedio Anual|2017|64,6|64,6|64,6|129%|
|MP10|Promedio Anual|Promedio 2015-2017|72,8|72,8|72,8|146%|
|CO|P99 1 hora|2015|4,84|mg/m3N|30|16%|
|CO|P99 1 hora|2016|5,25|5,25|5,25|18%|
|CO|P99 1 hora|2017|6,55|6,55|6,55|22%|
|CO|P99 1 hora|Mayor valor 2015-2017|6,55|6,55|6,55|22%|
|CO|P99 8 horas|2015|3,45|3,45|10|35%|
|CO|P99 8 horas|2016|3,38|3,38|3,38|34%|
|CO|P99 8 horas|2017|4,55|4,55|4,55|46%|
|CO|P99 8 horas|Mayor valor 2015-2017|4,55|4,55|4,55|46%|
|SO2|P99 24 horas|2015|13,2|μg/m3N|250|5%|
|SO2|P99 24 horas|2016|13,3|13,3|13,3|5%|
|SO2|P99 24 horas|2017|11,6|11,6|11,6|5%|
|SO2|P99 24 horas|Mayor valor 2015-2017|13,3|13,3|13,3|5%|
|SO2|Promedio Anual|2015|4,0|4,0|80|5%|
|SO2|Promedio Anual|2016|4,1|4,1|4,1|5%|
|SO2|Promedio Anual|2017 *|4,8|4,8|4,8|6%|
|SO2|Promedio Anual|Promedio 2015-2016|4,0|4,0|4,0|5%|

Fuente: Elaboración propia a partir de Registros Validados y Preliminares publicados en sinca.mma.gob.cl.

- Valor referencial, cuarto trimestre del año 2017 no cuenta con el 75% de datos válidos.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

89

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

De la Tabla anterior se observa que en la Estación Rancagua I permanece la Condición de

Saturación por Material Particulado Respirable (MP10), como concentración diaria y

anual, y por Material Particulado Fino Respirable (MP2,5), como concentración diaria y

anual.

En la Tabla 2-28 se presenta el resumen del monitoreo de los años 2015 a 2017 en la

Estación Rancagua II, y su contrastación contra las normas de calidad primarias.

**Tabla 2-28 -Calidad del Aire Estación Rancagua II.**

|Contaminante|Estadígrafo|Periodo|Valor|Unidad|Valor<br>Norma|Porcentaje de la<br>Norma|
|---|---|---|---|---|---|---|
|MP2,5|P98 24 horas|2015|97,0|μg/m3|50|194%|
|MP2,5|P98 24 horas|2016|110,0|110,0|110,0|220%|
|MP2,5|P98 24 horas|2017|83,0|83,0|83,0|166%|
|MP2,5|P98 24 horas|Mayor valor 2015-2017|110,0|110,0|110,0|220%|
|MP2,5|Promedio Anual|2015|33,5|33,5|20|168%|
|MP2,5|Promedio Anual|2016|31,0|31,0|31,0|155%|
|MP2,5|Promedio Anual|2017|25,9|25,9|25,9|129%|
|MP2,5|Promedio Anual|Promedio 2015-2017|30,2|30,2|30,2|151%|
|MP10|P98 24 horas|2015|142,1|μg/m3N|150|95%|
|MP10|P98 24 horas|2016|157,6|157,6|157,6|105%|
|MP10|P98 24 horas|2017|109,0|109,0|109,0|73%|
|MP10|P98 24 horas|Mayor valor 2015-2017|157,6|157,6|157,6|105%|
|MP10|Promedio Anual|2015|66,7|66,7|50|133%|
|MP10|Promedio Anual|2016|63,2|63,2|63,2|126%|
|MP10|Promedio Anual|2017|50,0|50,0|50,0|100%|
|MP10|Promedio Anual|Promedio 2015-2017|60,0|60,0|60,0|120%|

Fuente: Elaboración propia a partir de Registros Validados y Preliminares publicados en sinca.mma.gob.cl.

De la Tabla anterior se observa que en la Estación Rancagua II permanece la Condición de

Saturación por Material Particulado Fino Respirable (MP2,5), como concentración diaria y

anual, en el caso de Material Particulado Respirable (MP10) existe Condición de

Saturación como concentración anual, sin embargo, para la concentración diaria no se

observó superación de normativa para 2017.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

90

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.9** **Escenarios Modelados**

**2.9.1** **Escenario 1: Construcción Etapa 2 y Operación Proyectada**

**2.9.1.1** **Fuentes Emisoras**

En este escenario se modelan las fuentes correspondientes a las actividades asociadas a la

etapa 2 de la fase de construcción del proyecto y además las fuentes correspondientes a

la operación del proyecto.

Las fuentes fueron georreferenciadas de acuerdo con la información proporcionada por

ingeniería ( _layout_ del proyecto), para posteriormente ser ingresadas al modelo. Las

actividades modeladas se detallan a continuación:

a) Construcción Etapa 2

 - Tránsito de vehículos (fuente lineal)

 - Operación de Grupo Electrógeno en la Instalación de Faena (fuente puntual)

 - Utilización de Maquinaria (fuente areal)

 - Movimientos de Tierra (fuente areal)

b) Operación Proyectada

 - Operación de Grupo Electrógeno del proyecto (fuente puntual)

 - Operación de Caldera de Biomasa (fuente puntual)

 - Tránsito de vehículos (fuente lineal)

Así, en este escenario se modelan un total de 7 fuentes, de las cuales 2 son lineales, tres

son puntuales y dos son areales.

En la Figura 2-53 se presenta la ubicación espacial de las fuentes emisoras en una vista

general respecto al dominio de modelación y en la Figura 2-54 se presenta la ubicación en

un zoom al sector del proyecto, ambas figuras para el escenario de operación proyectada:

www.dfmconsultores.cl

**info@dfmconsultores.cl**

91

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-53. Ubicación Fuentes Emisoras. Vista General. Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

92

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-54 - Ubicación Fuentes Emisoras. Zoom Sector Proyecto. Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

93

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.9.1.2** **Tasas de Emisión**

Para modelar las emisiones de las fuentes puntuales se consideran las emisiones de cada fuente en toneladas anuales y se
transforman las unidades a gramos por segundo, en la Tabla 2-29 se presenta la caracterización de cada fuente puntual junto con sus
respectivas tasas de emisión:

**Tabla 2-29. Características y Tasas de Emisión de Fuentes Puntuales. Escenario 1.**

|Fase|Fuente|Emisión [t/año]|Col4|Col5|Col6|Col7|Parámetros Fuentes Puntuales|Col9|Col10|Col11|Tiempo|Tasa de Emisión [g/s]|Col14|Col15|Col16|Col17|Variabilidad|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fase**|**Fuente**|**MP2.5**|**MP10**|**CO**|**NO2 **|**SO2 **|**Altura**<br>**chimenea**<br>**[m]**|**Diámetro**<br>**interno**<br>**[m]**|**Velocidad**<br>**salida de**<br>**los gases**<br>**[m/s]**|**Temperatur**<br>**a de salida**<br>**de los gases**<br>**[°C]**|**s/año**|**MP2.5**|**MP10**|**CO**|**NO2 **|**SO2 **|**SO2 **|
|Operación<br>Proyectada|Grupo<br>Electrógeno<br>Proyecto|1,08|1,08|1,355|14,278|0,050|10|0,3047|58,5|416|3.952.800|2,742E-02|2,742E-02|3,427E-01|3,612E+00|1,258E-02|Ciclo<br>Mensual-<br>Diurno, de<br>17:00 a<br>23:00 h y de<br>abril a<br>septiembre.|
|Operación<br>Proyectada|Caldera de<br>Biomasa|0,956|0,956|4,350|13,867|12,327|18,5|1,2|12,75|280|31.536.000|3,031E-02|3,031E-02|1,379E-01|4,397E-01|3,909E-01|-|
|Construcción<br>etapa 2|Grupo<br>Electrógeno<br>IF|0,034|0,034|0,104|0,482|0,032|1,6|0,075|73,56|495|7.488.000|4,586E-03|4,586E-03|1,390E-02|6,435E-02|4,278E-03|Ciclo<br>Semanal-<br>Diurno|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia.

94

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Para modelar las emisiones de las fuentes lineales se consideran las emisiones de cada fuente en toneladas anuales y se transforman
las unidades a gramos por segundo. Luego, dichas emisiones se dividen por el largo de la fuente, en la Tabla 2-30 se presenta la
caracterización de la fuente lineal junto con sus respectivas tasas de emisión:

**Tabla 2-30. Características y Tasas de Emisión de Fuentes Lineales. Escenario 1.**

|Fase|Fuente|Tipo de<br>Fuente|Emisión [t/año]|Col5|Col6|Col7|Col8|Dimensiones Modelo|Col10|Tiempo|Tasa de Emisión [g/m-s]|Col13|Col14|Col15|Col16|Variabilidad|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fase**|**Fuente**|**Tipo de**<br>**Fuente**|**MP2.5**|**MP10**|**CO**|**NO2 **|**SO2 **|**Valor**|**Unidad**|**s/año**|**MP2.5**|**MP10**|**CO**|**NO2 **|**SO2 **|**SO2 **|
|Operación<br>Proyectada|Caminos<br>Pavimentados|Camino|0,525|2,057|0,414|1,786|0,045|31.150|[m]|31.536.000|5,340E-07|2,094E-06|4,214E-07|1,818E-06|4,607E-08|-|
|Construcción<br>etapa 2|Caminos<br>Pavimentados<br>Construcción|Camino|0,282|1,117|0,184|0,793|0,020|31.150|[m]|7.488.000|1,210E-06|4,789E-06|7,883E-07|3,401E-06|8,618E-08|Ciclo<br>Semanal-<br>Diurno|

Fuente: Elaboración propia.

95

www.dfmconsultores.cl

**info@dfmconsultores.cl**

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Para modelar las emisiones de las fuentes areales se consideran las emisiones de cada fuente en toneladas anuales y se transforman
las unidades a gramos por segundo. Luego, dichas emisiones se dividen por el área de la fuente, en la Tabla 2-31 se presenta la
caracterización de la fuente areal junto con sus respectivas tasas de emisión:

**Tabla 2-31. Características y Tasas de Emisión de Fuentes Areales. Escenario 1.**

|Fase|Fuente|Emisión [t/año]|Col4|Col5|Col6|Col7|Dimensiones<br>Modelo|Col9|Tiempo|Tasa de Emisión [g/m2-s]|Col12|Col13|Col14|Col15|Variabilidad|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fase**|**Fuente**|**MP2.5**|**MP10**|**CO**|**NO2 **|**SO2 **|**Valor**|**Unidad**|**s/año**|**MP2.5**|**MP10**|**CO**|**NO2 **|**SO2 **|**SO2 **|
|Construcción<br>etapa 2|Áreas Construcción<br>(Movimientos de Tierra)|0,309|0,656|-|-|-|25.688|[m2]|7.488.000|1,608E-06|3,410E-06|-|-|-|Ciclo Semanal-<br>Diurno|
|Construcción<br>etapa 2|Áreas Construcción<br>(Maquinaria)|0,598|0,598|1,906|6,143|0,000|25.688|[m2]|7.488.000|3,107E-06|3,107E-06|9,909E-06|3,194E-05|0,000E+00|Ciclo Semanal-<br>Diurno|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

96

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.9.2** **Escenario 2: Operación Proyectada**

**2.9.2.1** **Fuentes Emisioras**

Las fuentes fueron georreferenciadas de acuerdo con la información proporcionada por

ingeniería ( _layout_ del proyecto), para posteriormente ser ingresadas al modelo. Las

actividades modeladas se detallan a continuación:

 - Operación de Grupo Electrógeno del proyecto (fuente puntual)

 - Operación de Caldera de Biomasa (fuente puntual)

 - Tránsito de vehículos (fuente lineal)

Así, para el presente escenario se consideran 3 fuentes, dos de tipo puntual y una de tipo

lineal.

En la Figura 2-55 se presenta la ubicación espacial de las fuentes emisoras en una vista

general respecto al dominio de modelación y en la Figura 2-56 se presenta la ubicación en

un zoom al sector del proyecto, ambas figuras para el escenario de operación proyectada:

www.dfmconsultores.cl

**info@dfmconsultores.cl**

97

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-55. Ubicación Fuentes Emisoras. Vista General. Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

98

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-56 - Ubicación Fuentes Emisoras. Zoom Sector Proyecto. Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

99

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.9.2.2** **Tasas de Emisión**

Para modelar las emisiones de las fuentes puntuales se consideran las emisiones de cada fuente en toneladas anuales y se
transforman las unidades a gramos por segundo, en la Tabla 2-32 se presenta la caracterización de cada fuente puntual junto con sus
respectivas tasas de emisión:

**Tabla 2-32. Características y Tasas de Emisión de Fuentes Puntuales. Escenario 2.**

|Fase|Fuente|Emisión [t/año]|Col4|Col5|Col6|Col7|Parámetros Fuentes Puntuales|Col9|Col10|Col11|Tiempo|Tasa de Emisión [g/s]|Col14|Col15|Col16|Col17|Variabilidad|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fase**|**Fuente**|**MP2.5**|**MP10**|**CO**|**NO2 **|**SO2 **|**Altura**<br>**chimenea**<br>**[m]**|**Diámetro**<br>**interno**<br>**[m]**|**Velocidad**<br>**salida de**<br>**los gases**<br>**[m/s]**|**Temperatur**<br>**a de salida**<br>**de los gases**<br>**[°C]**|**s/año**|**MP2.5**|**MP10**|**CO**|**NO2 **|**SO2 **|**SO2 **|
|Operación<br>Proyectada|Grupo<br>Electrógeno<br>Proyecto|1,08|1,08|1,355|14,278|0,050|10|0,3047|58,5|416|3.952.800|2,742E-02|2,742E-02|3,427E-01|3,612E+00|1,258E-02|Ciclo<br>Mensual-<br>Diurno, de<br>17:00 a<br>23:00 h y de<br>abril a<br>septiembre.|
|Operación<br>Proyectada|Caldera de<br>Biomasa|0,956|0,956|4,350|13,867|12,327|18,5|1,2|12,75|280|31.536.000|3,031E-02|3,031E-02|1,379E-01|4,397E-01|3,909E-01|-|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

100

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

Para modelar las emisiones de las fuentes lineales se consideran las emisiones de cada fuente en toneladas anuales y se transforman
las unidades a gramos por segundo. Luego, dichas emisiones se dividen por el largo de la fuente, en la Tabla 2-33 se presenta la
caracterización de la fuente lineal junto con sus respectivas tasas de emisión:

**Tabla 2-33. Características y Tasas de Emisión de Fuentes Lineales. Escenario 2.**

|Fase|Fuente|Tipo de<br>Fuente|Emisión [t/año]|Col5|Col6|Col7|Col8|Dimensiones Modelo|Col10|Tiempo|Tasa de Emisión [g/m-s]|Col13|Col14|Col15|Col16|Variabilidad|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**Fase**|**Fuente**|**Tipo de**<br>**Fuente**|**MP2.5**|**MP10**|**CO**|**NO2 **|**SO2 **|**Valor**|**Unidad**|**s/año**|**MP2.5**|**MP10**|**CO**|**NO2 **|**SO2 **|**SO2 **|
|Operación<br>Proyectada|Caminos<br>Pavimentados|Camino|0,525|2,057|0,414|1,786|0,045|31.150|[m]|31.536.000|5,340E-07|2,094E-06|4,214E-07|1,818E-06|4,607E-08|-|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

101

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.10** **Receptores de Interés**

Se definió una grilla de receptores, de resolución 1.000 x 1.000 m, en todo el dominio de

modelación. Complementariamente, se consideraron 12 receptores discretos, los que se

detallan en la Tabla 2-34.

**Tabla 2-34- Receptores de Interés.**

|ID Receptor|Coordenadas|Col3|Elevación|Descripción|
|---|---|---|---|---|
|**ID Receptor**|**(Datum WGS84)**|**(Datum WGS84)**|**(Datum WGS84)**|**(Datum WGS84)**|
|**ID Receptor**|**Este**|**Norte**|**[msnm]**|**[msnm]**|
|**ID Receptor**|**[m]**|**[m]**|**[m]**|**[m]**|
|R_1|342.015|6.218.523|400,45|Estación Rancagua I|
|R_2|339.842|6.220.527|484,06|Estación Rancagua II|
|R_3|325.546|6.213.076|397,74|Vivienda 1|
|R_4|325.409|6.213.969|399,68|Vivienda 2|
|R_5|325.308|6.213.177|395,6|Vivienda 3|
|R_6|324.834|6.212.845|389,4|Vivienda 4|
|R_7|324.810|6.212.964|390,97|Vivienda 5|
|R_8|324.886|6.213.137|393,22|Vivienda 6|
|R_9|324.535|6.212.934|397,49|Vivienda 7|
|R_10|325.752|6.213.798|401,6|Vivienda 8|
|R_11|325.925|6.213.443|401,89|Vivienda 9|
|R_12|325.602|6.213.293|399,05|Vivienda 10|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

102

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Figura 2-57 se muestra una imagen referencial de la ubicación de los receptores

discretos utilizados en la modelación:

**Figura 2-57 - Ubicación de Receptores de Interés.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

103

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.11** **Resultados de la Modelación**

En este inciso se presentan los resultados de la modelación para todos los escenarios

planteados. Se presentan tablas donde se cuantifica el aporte de cada contaminante

evaluado del proyecto para cada receptor de interés, luego se realiza una comparación

con la normativa de calidad de aire respectiva, para así establecer el porcentaje del aporte

del proyecto respecto a la norma de cada contaminante. Además del análisis cuantitativo,

se presentan las curvas de isoconcentración para todos los escenarios y para todos los

contaminantes.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

104

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.11.1** **Escenario 1: Construcción Etapa 2 y Operación Proyectada**

En esta sección se presentan los resultados de la modelación para el escenario de construcción.

**2.11.1.1** **Material Particulado Fino (MP2,5)**

En la Tabla 2-35 se presentan las concentraciones de Material Particulado Fino (MP2,5) aportadas por el proyecto en los receptores

de interés para el escenario 1:

**Tabla 2-35 - Resultados de modelo de dispersión de MP2.5. Escenario 1.**

|Receptor|Descripción|Coordenadas de Ubicación (Datum WGS84)|Col4|Material Particulado Respirable Fino [MP2.5]|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Coordenadas de Ubicación (Datum WGS84)**|**Coordenadas de Ubicación (Datum WGS84)**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Este [m]**|**Norte [m]**|**Percentil 98 24**<br>**horas**|**Período Anual**|**Percentil 98 24**<br>**horas**|**Período Anual**|**Percentil 98 24**<br>**horas**|**Período Anual**|
|R_1|Estación Rancagua I|342.015|6.218.523|0,00|0,00|50|20|0,01%|0,01%|
|R_2|Estación Rancagua II|339.842|6.220.527|0,01|0,00|0,00|0,00|0,01%|0,01%|
|R_3|Vivienda 1|325.546|6.213.076|0,60|0,13|0,13|0,13|1,19%|0,64%|
|R_4|Vivienda 2|325.409|6.213.969|0,63|0,12|0,12|0,12|1,26%|0,61%|
|R_5|Vivienda 3|325.308|6.213.177|2,39|0,24|0,24|0,24|4,77%|1,20%|
|R_6|Vivienda 4|324.834|6.212.845|0,22|0,02|0,02|0,02|0,43%|0,11%|
|R_7|Vivienda 5|324.810|6.212.964|0,21|0,03|0,03|0,03|0,43%|0,14%|
|R_8|Vivienda 6|324.886|6.213.137|0,48|0,05|0,05|0,05|0,97%|0,23%|
|R_9|Vivienda 7|324.535|6.212.934|0,15|0,02|0,02|0,02|0,31%|0,09%|
|R_10|Vivienda 8|325.752|6.213.798|0,96|0,35|0,35|0,35|1,91%|1,74%|
|R_11|Vivienda 9|325.925|6.213.443|0,34|0,13|0,13|0,13|0,68%|0,63%|
|R_12|Vivienda 10|325.602|6.213.293|1,20|0,23|0,23|0,23|2,41%|1,14%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia.

105

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

A continuación, se presentan las curvas de isoconcentración de Material Particulado Fino

(MP2,5) para el primer escenario para la norma de percentil 98 de 24 horas en la Figura

2-58 y la Figura 2-59 y la norma periodo anual en la Figura 2-60 y la Figura 2-61, se

muestran figuras en vista general y con zoom al sector del proyecto respectivamente:

**Figura 2-58. Curva de Isoconcentración para Percentil 98 período 24 horas MP2,5 (μg/m** **[3]** **N). Vista General.**

**Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

106

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-59. Curva de Isoconcentración para Percentil 98 período 24 horas MP2,5 (μg/m** **[3]** **N). Zoom Sector**

**Proyecto. Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

107

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-60. Curva de Isoconcentración para período anual MP2,5 (μg/m** **[3]** **N). Vista General. Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

108

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-61. Curva de Isoconcentración para período anual MP2,5 (μg/m** **[3]** **N). Zoom Sector Proyecto.**

**Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

109

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.11.1.2** **Material Particulado Respirable (MP10)**

En la Tabla 2-36 se presentan las concentraciones de Material Particulado Respirable (MP10) aportadas por el proyecto en los

receptores de interés para el escenario 1:

**Tabla 2-36 - Resultados de modelo de dispersión de MP10. Escenario 1.**

|Receptor|Descripción|Coordenadas de Ubicación (Datum WGS84)|Col4|Material Particulado Respirable [MP10]|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Coordenadas de Ubicación (Datum WGS84)**|**Coordenadas de Ubicación (Datum WGS84)**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Este [m]**|**Norte [m]**|**Percentil 98 24**<br>**horas**|**Período Anual**|**Percentil 98 24**<br>**horas**|**Período Anual**|**Percentil 98 24**<br>**horas**|**Período Anual**|
|R_1|Estación Rancagua I|342.015|6.218.523|0,02|0,01|150|50|0,01%|0,01%|
|R_2|Estación Rancagua II|339.842|6.220.527|0,02|0,01|0,01|0,01|0,01%|0,01%|
|R_3|Vivienda 1|325.546|6.213.076|1,23|0,33|0,33|0,33|0,82%|0,67%|
|R_4|Vivienda 2|325.409|6.213.969|0,90|0,19|0,19|0,19|0,60%|0,37%|
|R_5|Vivienda 3|325.308|6.213.177|3,64|0,56|0,56|0,56|2,42%|1,12%|
|R_6|Vivienda 4|324.834|6.212.845|0,36|0,04|0,04|0,04|0,24%|0,08%|
|R_7|Vivienda 5|324.810|6.212.964|0,36|0,05|0,05|0,05|0,24%|0,11%|
|R_8|Vivienda 6|324.886|6.213.137|0,72|0,09|0,09|0,09|0,48%|0,19%|
|R_9|Vivienda 7|324.535|6.212.934|0,26|0,04|0,04|0,04|0,17%|0,07%|
|R_10|Vivienda 8|325.752|6.213.798|1,39|0,51|0,51|0,51|0,93%|1,02%|
|R_11|Vivienda 9|325.925|6.213.443|0,84|0,35|0,35|0,35|0,56%|0,69%|
|R_12|Vivienda 10|325.602|6.213.293|1,76|0,44|0,44|0,44|1,18%|0,88%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia.

110

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

A continuación, se presentan las curvas de isoconcentración de Material Particulado

Respirable (MP10) para el primer escenario para la norma de percentil 98 de 24 horas en

la Figura 2-62 y la Figura 2-63 y la norma periodo anual en la Figura 2-64 y la Figura 2-65,

se muestran figuras en vista general y con zoom al sector del proyecto respectivamente:

**Figura 2-62. Curva de Isoconcentración para Percentil 98 período 24 horas MP10 (μg/m** **[3]** **N). Vista General.**

**Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

111

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-63. Curva de Isoconcentración para Percentil 98 período 24 horas MP10 (μg/m** **[3]** **N). Zoom Sector**

**Proyecto. Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

112

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-64. Curva de Isoconcentración para período anual MP10 (μg/m** **[3]** **N). Vista General. Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

113

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-65. Curva de Isoconcentración para período anual MP10 (μg/m** **[3]** **N). Zoom Sector Proyecto.**

**Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

114

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.11.1.3** **Monóxido de Carbono (CO)**

En la Tabla 2-37 se presentan las concentraciones de Monóxido de Carbono (CO) aportadas por el proyecto en los receptores de

interés para el escenario 1:

**Tabla 2-37 - Resultados de modelo de dispersión de CO. Escenario 1.**

|Receptor|Descripción|Coordenadas de Ubicación (Datum WGS84)|Col4|Monóxido de Carbono (CO)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Coordenadas de Ubicación (Datum WGS84)**|**Coordenadas de Ubicación (Datum WGS84)**|**Concentración [mg/m3N] - Aporte**<br>**Proyecto**|**Concentración [mg/m3N] - Aporte**<br>**Proyecto**|**Concentración [mg/m3N] - Norma de**<br>**Calidad**|**Concentración [mg/m3N] - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Este [m]**|**Norte [m]**|**Percentil 99 1**<br>**hora**|**Percentil 99 8**<br>**horas**|**Percentil 99 1 hora**|**Percentil 99 8**<br>**horas**|**Percentil 99 1**<br>**hora**|**Percentil 99 8**<br>**horas**|
|R_1|Estación Rancagua I|342.015|6.218.523|1,75E-04|3,57E-05|30|10|0,00%|0,00%|
|R_2|Estación Rancagua II|339.842|6.220.527|1,79E-04|5,77E-05|5,77E-05|5,77E-05|0,00%|0,00%|
|R_3|Vivienda 1|325.546|6.213.076|3,10E-02|9,98E-03|9,98E-03|9,98E-03|0,10%|0,10%|
|R_4|Vivienda 2|325.409|6.213.969|2,36E-02|6,83E-03|6,83E-03|6,83E-03|0,08%|0,07%|
|R_5|Vivienda 3|325.308|6.213.177|6,47E-02|2,43E-02|2,43E-02|2,43E-02|0,22%|0,24%|
|R_6|Vivienda 4|324.834|6.212.845|7,83E-03|2,93E-03|2,93E-03|2,93E-03|0,03%|0,03%|
|R_7|Vivienda 5|324.810|6.212.964|9,83E-03|4,09E-03|4,09E-03|4,09E-03|0,03%|0,04%|
|R_8|Vivienda 6|324.886|6.213.137|2,13E-02|5,40E-03|5,40E-03|5,40E-03|0,07%|0,05%|
|R_9|Vivienda 7|324.535|6.212.934|9,22E-03|2,95E-03|2,95E-03|2,95E-03|0,03%|0,03%|
|R_10|Vivienda 8|325.752|6.213.798|4,15E-02|1,18E-02|1,18E-02|1,18E-02|0,14%|0,12%|
|R_11|Vivienda 9|325.925|6.213.443|1,25E-02|4,83E-03|4,83E-03|4,83E-03|0,04%|0,05%|
|R_12|Vivienda 10|325.602|6.213.293|7,51E-02|2,02E-02|2,02E-02|2,02E-02|0,25%|0,20%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia.

115

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

A continuación, se presentan las curvas de isoconcentración de Monóxido de Carbono

(CO) para el primer escenario para la norma de percentil 99 de 8 horas en la Figura 2-66 y

la Figura 2-67 y la norma percentil 99 de 1 hora en la Figura 2-68 y la Figura 2-69, se

muestran figuras en vista general y con zoom al sector del proyecto respectivamente:

**Figura 2-66. Curva de Isoconcentración para Percentil 99 período 8 horas CO (mg/m** **[3]** **N). Vista General.**

**Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

116

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-67. Curva de Isoconcentración para Percentil 99 período 8 horas CO (mg/m** **[3]** **N). Zoom Sector**

**Proyecto. Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

117

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-68. Curva de Isoconcentración para Percentil 99 periodo 1 hora CO (mg/m** **[3]** **N). Vista General.**

**Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

118

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-69. Curva de Isoconcentración para Percentil 99 periodo 1 hora CO (mg/m** **[3]** **N). Zoom Sector**

**Proyecto. Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

119

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.11.1.4** **Dióxido de Nitrógeno (NO** **2** **)**

En la Tabla 2-38 se presentan las concentraciones de Dióxido de Nitrógeno (NO 2 ) aportadas por el proyecto en los receptores de

interés para el escenario 1:

**Tabla 2-38 - Resultados de modelo de dispersión de NO** **2** **. Escenario 1.**

|Receptor|Descripción|Coordenadas de Ubicación (Datum WGS84)|Col4|Dióxido de Nitrógeno (NO)<br>2|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Coordenadas de Ubicación (Datum WGS84)**|**Coordenadas de Ubicación (Datum WGS84)**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Este [m]**|**Norte [m]**|**Percentil 99 1**<br>**hora**|**Período Anual**|**Percentil 99 1 hora**|**Período Anual**|**Percentil 99 1**<br>**hora**|**Período Anual**|
|R_1|Estación Rancagua I|342.015|6.218.523|1,32|0,01|400|100|0,33%|0,01%|
|R_2|Estación Rancagua II|339.842|6.220.527|1,48|0,02|0,02|0,02|0,37%|0,02%|
|R_3|Vivienda 1|325.546|6.213.076|124,99|0,76|0,76|0,76|31,25%|0,76%|
|R_4|Vivienda 2|325.409|6.213.969|110,62|1,01|1,01|1,01|27,66%|1,01%|
|R_5|Vivienda 3|325.308|6.213.177|212,82|1,49|1,49|1,49|53,21%|1,49%|
|R_6|Vivienda 4|324.834|6.212.845|66,54|0,30|0,30|0,30|16,64%|0,30%|
|R_7|Vivienda 5|324.810|6.212.964|50,07|0,31|0,31|0,31|12,52%|0,31%|
|R_8|Vivienda 6|324.886|6.213.137|68,89|0,38|0,38|0,38|17,22%|0,38%|
|R_9|Vivienda 7|324.535|6.212.934|40,36|0,21|0,21|0,21|10,09%|0,21%|
|R_10|Vivienda 8|325.752|6.213.798|141,42|3,32|3,32|3,32|35,36%|3,32%|
|R_11|Vivienda 9|325.925|6.213.443|121,07|0,90|0,90|0,90|30,27%|0,90%|
|R_12|Vivienda 10|325.602|6.213.293|240,37|1,75|1,75|1,75|60,09%|1,75%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia.

120

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

A continuación, se presentan las curvas de isoconcentración de Dióxido de Nitrógeno

(NO 2 ) para el primer escenario para la norma de periodo anual en la Figura 2-70 y la Figura

2-71 y la norma de percentil 99 de 1 hora en la Figura 2-72 y la Figura 2-73, se muestran

figuras en vista general y con zoom al sector del proyecto respectivamente:

**Figura 2-70. Curva de Isoconcentración para periodo anual NO** **2** **(μg/m** **[3]** **N). Vista General. Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

121

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-71. Curva de Isoconcentración para periodo anual NO** **2** **(μg/m** **[3]** **N). Zoom Sector Proyecto.**

**Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

122

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-72. Curva de Isoconcentración para Percentil 99 periodo 1 hora NO** **2** **(μg/m** **[3]** **N). Vista General.**

**Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

123

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-73. Curva de Isoconcentración para Percentil 99 periodo 1 hora NO** **2** **(μg/m** **[3]** **N). Zoom Sector**

**Proyecto. Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

124

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.11.1.5** **Dióxido de Azufre (SO** **2** **)**

En la Tabla 2-39 se presentan las concentraciones de Dióxido de Azufre (SO 2 ) aportadas por el proyecto en los receptores de interés

para el escenario 1:

**Tabla 2-39 - Resultados de modelo de dispersión de SO** **2** **. Escenario 1.**

|Receptor|Descripción|Coordenadas de Ubicación (Datum WGS84)|Col4|Dióxido de Azufre (SO)<br>2|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Coordenadas de Ubicación (Datum WGS84)**|**Coordenadas de Ubicación (Datum WGS84)**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Este [m]**|**Norte [m]**|**Percentil 99 24**<br>**horas**|**Período Anual**|**Percentil 99 24**<br>**horas**|**Período Anual**|**Percentil 99 24**<br>**horas**|**Período Anual**|
|R_1|Estación Rancagua I|342.015|6.218.523|1,48E-02|2,39E-03|250|80|0,01%|0,00%|
|R_2|Estación Rancagua II|339.842|6.220.527|2,06E-02|3,59E-03|3,59E-03|3,59E-03|0,01%|0,00%|
|R_3|Vivienda 1|325.546|6.213.076|1,71E-01|3,02E-02|3,02E-02|3,02E-02|0,07%|0,04%|
|R_4|Vivienda 2|325.409|6.213.969|3,24E-01|7,28E-02|7,28E-02|7,28E-02|0,13%|0,09%|
|R_5|Vivienda 3|325.308|6.213.177|2,30E-01|3,96E-02|3,96E-02|3,96E-02|0,09%|0,05%|
|R_6|Vivienda 4|324.834|6.212.845|2,74E-01|3,25E-02|3,25E-02|3,25E-02|0,11%|0,04%|
|R_7|Vivienda 5|324.810|6.212.964|2,91E-01|3,49E-02|3,49E-02|3,49E-02|0,12%|0,04%|
|R_8|Vivienda 6|324.886|6.213.137|2,49E-01|3,64E-02|3,64E-02|3,64E-02|0,10%|0,05%|
|R_9|Vivienda 7|324.535|6.212.934|2,75E-01|3,27E-02|3,27E-02|3,27E-02|0,11%|0,04%|
|R_10|Vivienda 8|325.752|6.213.798|5,75E-01|2,13E-01|2,13E-01|2,13E-01|0,23%|0,27%|
|R_11|Vivienda 9|325.925|6.213.443|4,62E-01|7,24E-02|7,24E-02|7,24E-02|0,18%|0,09%|
|R_12|Vivienda 10|325.602|6.213.293|2,00E-01|3,50E-02|3,50E-02|3,50E-02|0,08%|0,04%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia.

125

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

A continuación, se presentan las curvas de isoconcentración de Dióxido de Azufre (SO 2 )

para el primer escenario para la norma de periodo anual en la Figura 2-74 y la Figura 2-75

y la norma de percentil 99 de 24 horas en la Figura 2-76 y la Figura 2-77, se muestran

figuras en vista general y con zoom al sector del proyecto respectivamente:

**Figura 2-74. Curva de Isoconcentración para período anual SO** **2** **(μg/m** **[3]** **N). Vista General. Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

126

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-75. Curva de Isoconcentración para período anual SO** **2** **(μg/m** **[3]** **N). Zoom Sector Proyecto. Escenario**

**1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

127

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-76. Curva de Isoconcentración para Percentil 99 periodo 24 horas SO** **2** **(μg/m** **[3]** **N). Vista General.**

**Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

128

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-77. Curva de Isoconcentración para Percentil 99 periodo 24 horas SO** **2** **(μg/m** **[3]** **N). Zoom Sector**

**Proyecto. Escenario 1.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

129

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.11.2** **Escenario 2: Operación Proyectada**

En esta sección se presentan los resultados de la modelación para el escenario de operación proyectada.

**2.11.2.1** **Material Particulado Fino (MP2,5)**

En la Tabla 2-40 se presentan las concentraciones de Material Particulado Fino (MP2,5) aportadas por el proyecto en los receptores

de interés para el escenario 2:

**Tabla 2-40 - Resultados de modelo de dispersión de MP2.5. Escenario 2.**

|Receptor|Descripción|Coordenadas de Ubicación (Datum WGS84)|Col4|Material Particulado Respirable Fino [MP2.5]|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Coordenadas de Ubicación (Datum WGS84)**|**Coordenadas de Ubicación (Datum WGS84)**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Este [m]**|**Norte [m]**|**Percentil 98 24**<br>**horas**|**Período Anual**|**Percentil 98 24**<br>**horas**|**Período Anual**|**Percentil 98 24**<br>**horas**|**Período Anual**|
|R_1|Estación Rancagua I|342.015|6.218.523|0,00|0,00|50|20|0,01%|0,01%|
|R_2|Estación Rancagua II|339.842|6.220.527|0,00|0,00|0,00|0,00|0,01%|0,01%|
|R_3|Vivienda 1|325.546|6.213.076|0,16|0,06|0,06|0,06|0,31%|0,30%|
|R_4|Vivienda 2|325.409|6.213.969|0,04|0,01|0,01|0,01|0,09%|0,07%|
|R_5|Vivienda 3|325.308|6.213.177|0,20|0,08|0,08|0,08|0,40%|0,42%|
|R_6|Vivienda 4|324.834|6.212.845|0,04|0,01|0,01|0,01|0,08%|0,04%|
|R_7|Vivienda 5|324.810|6.212.964|0,03|0,01|0,01|0,01|0,07%|0,05%|
|R_8|Vivienda 6|324.886|6.213.137|0,04|0,01|0,01|0,01|0,07%|0,07%|
|R_9|Vivienda 7|324.535|6.212.934|0,02|0,01|0,01|0,01|0,05%|0,04%|
|R_10|Vivienda 8|325.752|6.213.798|0,09|0,04|0,04|0,04|0,17%|0,18%|
|R_11|Vivienda 9|325.925|6.213.443|0,15|0,06|0,06|0,06|0,30%|0,32%|
|R_12|Vivienda 10|325.602|6.213.293|0,11|0,05|0,05|0,05|0,21%|0,24%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia.

130

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

A continuación, se presentan las curvas de isoconcentración de Material Particulado Fino

(MP2,5) para el segundo escenario para la norma de percentil 98 de 24 horas en la Figura

2-78 y la Figura 2-79 y la norma periodo anual en la Figura 2-80 y la Figura 2-81, se

muestran figuras en vista general y con zoom al sector del proyecto respectivamente:

**Figura 2-78. Curva de Isoconcentración para Percentil 98 período 24 horas MP2,5 (μg/m** **[3]** **N). Vista General.**

**Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

131

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-79. Curva de Isoconcentración para Percentil 98 período 24 horas MP2,5 (μg/m** **[3]** **N). Zoom Sector**

**Proyecto. Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

132

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-80. Curva de Isoconcentración para período anual MP2,5 (μg/m** **[3]** **N). Vista General. Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

133

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-81. Curva de Isoconcentración para período anual MP2,5 (μg/m** **[3]** **N). Zoom Sector Proyecto.**

**Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

134

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.11.2.2** **Material Particulado Respirable (MP10)**

En la Tabla 2-41 se presentan las concentraciones de Material Particulado Respirable (MP10) aportadas por el proyecto en los

receptores de interés para el escenario 2:

**Tabla 2-41 - Resultados de modelo de dispersión de MP10. Escenario 2.**

|Receptor|Descripción|Coordenadas de Ubicación (Datum WGS84)|Col4|Material Particulado Respirable [MP10]|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Coordenadas de Ubicación (Datum WGS84)**|**Coordenadas de Ubicación (Datum WGS84)**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Este [m]**|**Norte [m]**|**Percentil 98 24**<br>**horas**|**Período Anual**|**Percentil 98 24**<br>**horas**|**Período Anual**|**Percentil 98 24**<br>**horas**|**Período Anual**|
|R_1|Estación Rancagua I|342.015|6.218.523|0,01|0,00|150|50|0,01%|0,01%|
|R_2|Estación Rancagua II|339.842|6.220.527|0,01|0,00|0,00|0,00|0,01%|0,01%|
|R_3|Vivienda 1|325.546|6.213.076|0,61|0,22|0,22|0,22|0,41%|0,45%|
|R_4|Vivienda 2|325.409|6.213.969|0,10|0,04|0,04|0,04|0,07%|0,08%|
|R_5|Vivienda 3|325.308|6.213.177|0,76|0,32|0,32|0,32|0,51%|0,64%|
|R_6|Vivienda 4|324.834|6.212.845|0,09|0,02|0,02|0,02|0,06%|0,04%|
|R_7|Vivienda 5|324.810|6.212.964|0,09|0,03|0,03|0,03|0,06%|0,06%|
|R_8|Vivienda 6|324.886|6.213.137|0,12|0,05|0,05|0,05|0,08%|0,09%|
|R_9|Vivienda 7|324.535|6.212.934|0,06|0,02|0,02|0,02|0,04%|0,04%|
|R_10|Vivienda 8|325.752|6.213.798|0,18|0,08|0,08|0,08|0,12%|0,15%|
|R_11|Vivienda 9|325.925|6.213.443|0,58|0,23|0,23|0,23|0,39%|0,47%|
|R_12|Vivienda 10|325.602|6.213.293|0,40|0,17|0,17|0,17|0,26%|0,34%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia.

135

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

A continuación, se presentan las curvas de isoconcentración de Material Particulado

Respirable (MP10) para el segundo escenario para la norma de percentil 98 de 24 horas en

la Figura 2-82 y la Figura 2-83 y la norma periodo anual en la Figura 2-84 y la Figura 2-85,

se muestran figuras en vista general y con zoom al sector del proyecto respectivamente:

**Figura 2-82. Curva de Isoconcentración para Percentil 98 período 24 horas MP10 (μg/m** **[3]** **N). Vista General.**

**Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

136

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-83. Curva de Isoconcentración para Percentil 98 período 24 horas MP10 (μg/m** **[3]** **N). Zoom Sector**

**Proyecto. Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

137

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-84. Curva de Isoconcentración para período anual MP10 (μg/m** **[3]** **N). Vista General. Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

138

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-85. Curva de Isoconcentración para período anual MP10 (μg/m** **[3]** **N). Zoom Sector Proyecto.**

**Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

139

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.11.2.3** **Monóxido de Carbono (CO)**

En la Tabla 2-42 se presentan las concentraciones de Monóxido de Carbono (CO) aportadas por el proyecto en los receptores de

interés para el escenario 2:

**Tabla 2-42 - Resultados de modelo de dispersión de CO. Escenario 2.**

|Receptor|Descripción|Coordenadas de Ubicación (Datum WGS84)|Col4|Monóxido de Carbono (CO)|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Coordenadas de Ubicación (Datum WGS84)**|**Coordenadas de Ubicación (Datum WGS84)**|**Concentración [mg/m3N] - Aporte**<br>**Proyecto**|**Concentración [mg/m3N] - Aporte**<br>**Proyecto**|**Concentración [mg/m3N] - Norma de**<br>**Calidad**|**Concentración [mg/m3N] - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Este [m]**|**Norte [m]**|**Percentil 99 1**<br>**hora**|**Percentil 99 8**<br>**horas**|**Percentil 99 1 hora**|**Percentil 99 8**<br>**horas**|**Percentil 99 1**<br>**hora**|**Percentil 99 8**<br>**horas**|
|R_1|Estación Rancagua I|342.015|6.218.523|1,45E-04|3,39E-05|30|10|0,00%|0,00%|
|R_2|Estación Rancagua II|339.842|6.220.527|1,56E-04|5,18E-05|5,18E-05|5,18E-05|0,00%|0,00%|
|R_3|Vivienda 1|325.546|6.213.076|1,99E-03|8,05E-04|8,05E-04|8,05E-04|0,01%|0,01%|
|R_4|Vivienda 2|325.409|6.213.969|6,38E-03|1,67E-03|1,67E-03|1,67E-03|0,02%|0,02%|
|R_5|Vivienda 3|325.308|6.213.177|1,02E-02|2,48E-03|2,48E-03|2,48E-03|0,03%|0,02%|
|R_6|Vivienda 4|324.834|6.212.845|5,24E-03|2,06E-03|2,06E-03|2,06E-03|0,02%|0,02%|
|R_7|Vivienda 5|324.810|6.212.964|4,65E-03|1,65E-03|1,65E-03|1,65E-03|0,02%|0,02%|
|R_8|Vivienda 6|324.886|6.213.137|4,04E-03|1,25E-03|1,25E-03|1,25E-03|0,01%|0,01%|
|R_9|Vivienda 7|324.535|6.212.934|3,09E-03|1,13E-03|1,13E-03|1,13E-03|0,01%|0,01%|
|R_10|Vivienda 8|325.752|6.213.798|1,22E-02|4,45E-03|4,45E-03|4,45E-03|0,04%|0,04%|
|R_11|Vivienda 9|325.925|6.213.443|8,22E-03|2,15E-03|2,15E-03|2,15E-03|0,03%|0,02%|
|R_12|Vivienda 10|325.602|6.213.293|1,17E-02|3,70E-03|3,70E-03|3,70E-03|0,04%|0,04%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia.

140

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

A continuación, se presentan las curvas de isoconcentración de Monóxido de Carbono

(CO) para el segundo escenario para la norma de percentil 99 de 8 horas en la Figura 2-86

y la Figura 2-87 y la norma percentil 99 de 1 hora en la Figura 2-88 y la Figura 2-89, se

muestran figuras en vista general y con zoom al sector del proyecto respectivamente:

**Figura 2-86. Curva de Isoconcentración para Percentil 99 período 8 horas CO (mg/m** **[3]** **N). Vista General.**

**Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

141

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-87. Curva de Isoconcentración para Percentil 99 período 8 horas CO (mg/m** **[3]** **N). Zoom Sector**

**Proyecto. Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

142

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-88. Curva de Isoconcentración para Percentil 99 periodo 1 hora CO (mg/m** **[3]** **N). Vista General.**

**Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

143

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-89. Curva de Isoconcentración para Percentil 99 periodo 1 hora CO (mg/m** **[3]** **N). Zoom Sector**

**Proyecto. Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

144

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.11.2.4** **Dióxido de Nitrógeno (NO** **2** **)**

En la Tabla 2-43 se presentan las concentraciones de Dióxido de Nitrógeno (NO 2 ) aportadas por el proyecto en los receptores de

interés para el escenario 2:

**Tabla 2-43 - Resultados de modelo de dispersión de NO** **2** **. Escenario 2.**

|Receptor|Descripción|Coordenadas de Ubicación (Datum WGS84)|Col4|Dióxido de Nitrógeno (NO)<br>2|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Coordenadas de Ubicación (Datum WGS84)**|**Coordenadas de Ubicación (Datum WGS84)**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Este [m]**|**Norte [m]**|**Percentil 99 1**<br>**hora**|**Período Anual**|**Percentil 99 1 hora**|**Período Anual**|**Percentil 99 1**<br>**hora**|**Período Anual**|
|R_1|Estación Rancagua I|342.015|6.218.523|1,32|0,01|400|100|0,33%|0,01%|
|R_2|Estación Rancagua II|339.842|6.220.527|1,48|0,02|0,02|0,02|0,37%|0,02%|
|R_3|Vivienda 1|325.546|6.213.076|19,28|0,32|0,32|0,32|4,82%|0,32%|
|R_4|Vivienda 2|325.409|6.213.969|66,80|0,29|0,29|0,29|16,70%|0,29%|
|R_5|Vivienda 3|325.308|6.213.177|106,89|0,51|0,51|0,51|26,72%|0,51%|
|R_6|Vivienda 4|324.834|6.212.845|54,03|0,21|0,21|0,21|13,51%|0,21%|
|R_7|Vivienda 5|324.810|6.212.964|48,02|0,19|0,19|0,19|12,01%|0,19%|
|R_8|Vivienda 6|324.886|6.213.137|42,11|0,17|0,17|0,17|10,53%|0,17%|
|R_9|Vivienda 7|324.535|6.212.934|31,59|0,14|0,14|0,14|7,90%|0,14%|
|R_10|Vivienda 8|325.752|6.213.798|127,92|1,19|1,19|1,19|31,98%|1,19%|
|R_11|Vivienda 9|325.925|6.213.443|86,30|0,54|0,54|0,54|21,57%|0,54%|
|R_12|Vivienda 10|325.602|6.213.293|123,09|0,58|0,58|0,58|30,77%|0,58%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia.

145

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

A continuación, se presentan las curvas de isoconcentración de Dióxido de Nitrógeno

(NO 2 ) para el segundo escenario para la norma de periodo anual en la Figura 2-90 y la

Figura 2-91 y la norma de percentil 99 de 1 hora en la Figura 2-92 y la Figura 2-93, se

muestran figuras en vista general y con zoom al sector del proyecto respectivamente:

**Figura 2-90. Curva de Isoconcentración para periodo anual NO** **2** **(μg/m** **[3]** **N). Vista General. Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

146

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-91. Curva de Isoconcentración para periodo anual NO** **2** **(μg/m** **[3]** **N). Zoom Sector Proyecto.**

**Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

147

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-92. Curva de Isoconcentración para Percentil 99 periodo 1 hora NO** **2** **(μg/m** **[3]** **N). Vista General.**

**Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

148

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-93. Curva de Isoconcentración para Percentil 99 periodo 1 hora NO** **2** **(μg/m** **[3]** **N). Zoom Sector**

**Proyecto. Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

149

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.11.2.5** **Dióxido de Azufre (SO** **2** **)**

En la Tabla 2-44 se presentan las concentraciones de Dióxido de Azufre (SO 2 ) aportadas por el proyecto en los receptores de interés

para el escenario 2:

**Tabla 2-44 - Resultados de modelo de dispersión de SO** **2** **. Escenario 2.**

|Receptor|Descripción|Coordenadas de Ubicación (Datum WGS84)|Col4|Dióxido de Azufre (SO)<br>2|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Coordenadas de Ubicación (Datum WGS84)**|**Coordenadas de Ubicación (Datum WGS84)**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Aporte**<br>**Proyecto**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Concentración [μg/m3N] - Norma de**<br>**Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**Este [m]**|**Norte [m]**|**Percentil 99 24**<br>**horas**|**Período Anual**|**Percentil 99 24**<br>**horas**|**Período Anual**|**Percentil 99 24**<br>**horas**|**Período Anual**|
|R_1|Estación Rancagua I|342.015|6.218.523|1,47E-02|2,37E-03|250|80|0,01%|0,00%|
|R_2|Estación Rancagua II|339.842|6.220.527|2,06E-02|3,57E-03|3,57E-03|3,57E-03|0,01%|0,00%|
|R_3|Vivienda 1|325.546|6.213.076|1,65E-01|2,85E-02|2,85E-02|2,85E-02|0,07%|0,04%|
|R_4|Vivienda 2|325.409|6.213.969|3,19E-01|6,97E-02|6,97E-02|6,97E-02|0,13%|0,09%|
|R_5|Vivienda 3|325.308|6.213.177|2,27E-01|3,55E-02|3,55E-02|3,55E-02|0,09%|0,04%|
|R_6|Vivienda 4|324.834|6.212.845|2,74E-01|3,21E-02|3,21E-02|3,21E-02|0,11%|0,04%|
|R_7|Vivienda 5|324.810|6.212.964|2,91E-01|3,42E-02|3,42E-02|3,42E-02|0,12%|0,04%|
|R_8|Vivienda 6|324.886|6.213.137|2,48E-01|3,56E-02|3,56E-02|3,56E-02|0,10%|0,04%|
|R_9|Vivienda 7|324.535|6.212.934|2,75E-01|3,24E-02|3,24E-02|3,24E-02|0,11%|0,04%|
|R_10|Vivienda 8|325.752|6.213.798|5,70E-01|2,06E-01|2,06E-01|2,06E-01|0,23%|0,26%|
|R_11|Vivienda 9|325.925|6.213.443|4,59E-01|7,02E-02|7,02E-02|7,02E-02|0,18%|0,09%|
|R_12|Vivienda 10|325.602|6.213.293|1,99E-01|3,18E-02|3,18E-02|3,18E-02|0,08%|0,04%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Fuente: Elaboración propia.

150

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

A continuación, se presentan las curvas de isoconcentración de Dióxido de Azufre (SO 2 )

para el segundo escenario para la norma de periodo anual en la Figura 2-94 y la Figura

2-95 y la norma de percentil 99 de 24 horas en la Figura 2-96 y la Figura 2-97, se muestran

figuras en vista general y con zoom al sector del proyecto respectivamente:

**Figura 2-94. Curva de Isoconcentración para período anual SO** **2** **(μg/m** **[3]** **N). Vista General. Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

151

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-95. Curva de Isoconcentración para período anual SO** **2** **(μg/m** **[3]** **N). Zoom Sector Proyecto. Escenario**

**2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

152

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-96. Curva de Isoconcentración para Percentil 99 periodo 24 horas SO** **2** **(μg/m** **[3]** **N). Vista General.**

**Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

153

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**Figura 2-97. Curva de Isoconcentración para Percentil 99 periodo 24 horas SO** **2** **(μg/m** **[3]** **N). Vista General.**

**Escenario 2.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

154

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.12** **Concentración Total Esperada**

Con el fin de cuantificar el impacto que tendrá en el proyecto en todos los receptores de interés con los que se cuenta información

monitoreada de la línea de base, se presenta en este inciso la concentración total esperada de cada uno, la que se obtiene sumando

los valores de la línea de base presentados en el inciso 2.8, a los aportes del proyecto presentados en el inciso 2.11.

**2.12.1** **Escenario 1: Construcción Etapa 2 y Operación Proyectada**

En la Tabla 2-45 se presenta la concentración total esperada para el contaminante Material Particulado Respirable Fino (MP2.5) en

los receptores Estación Rancagua I y Estación Rancagua II para el escenario 1:

**Tabla 2-45. Concentración total esperada. Material Particulado Respirable Fino (MP2.5). Escenario 1.**

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación (Datum<br>WGS84)|Col4|Material Particulado Respirable Fino (MP2.5)|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación (Datum**<br>**WGS84)**|**Coordenadas de**<br>**Ubicación (Datum**<br>**WGS84)**|**Concentración**<br>**(μg/m3N) - Línea de**<br>**Base**|**Concentración**<br>**(μg/m3N) - Línea de**<br>**Base**|**Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración Total**<br>**Esperada (μg/m3N)**|**Concentración Total**<br>**Esperada (μg/m3N)**|**Norma de Calidad**<br>**(μg/m3N)**|**Norma de Calidad**<br>**(μg/m3N)**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|
|R_1|Estación Rancagua I|342.015|6.218.523|88,90|24,10|0,00|0,00|88,90|24,10|50|20|178%|121%|
|R_2|Estación Rancagua II|339.842|6.220.527|110,00|30,20|0,01|0,00|110,01|30,20|30,20|30,20|220%|151%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

155

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Tabla 2-46 se presenta la concentración total esperada para el contaminante Material Particulado Respirable (MP10) en los

receptores Estación Rancagua I y Estación Rancagua II para el escenario 1:

**Tabla 2-46. Concentración total esperada. Material Particulado Respirable (MP10). Escenario 1.**

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Material Particulado Respirable (MP10)|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración**<br>**(μg/m3N) - Línea de**<br>**Base**|**Concentración**<br>**(μg/m3N) - Línea de**<br>**Base**|**Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración Total**<br>**Esperada (μg/m3N)**|**Concentración Total**<br>**Esperada (μg/m3N)**|**Norma de Calidad**<br>**(μg/m3N)**|**Norma de Calidad**<br>**(μg/m3N)**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|
|R_1|Estación Rancagua I|342.015|6.218.523|181,70|72,80|0,02|0,01|181,72|72,81|150|50|121%|146%|
|R_2|Estación Rancagua II|339.842|6.220.527|157,60|60,00|0,02|0,01|157,62|60,01|60,01|60,01|105%|120%|

Fuente: Elaboración propia.

En la Tabla 2-47 se presenta la concentración total esperada para el contaminante Monóxido de Carbono (CO) en el receptor

Estación Rancagua I para el escenario 1:

**Tabla 2-47. Concentración total esperada. Monóxido de Carbono (CO). Escenario 1.**

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Monóxido de Carbono (CO)|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración (mg/m3N)**<br>**- Línea de Base**|**Concentración (mg/m3N)**<br>**- Línea de Base**|**Concentración (mg/m3N)**<br>**- Aporte del Proyecto**|**Concentración (mg/m3N)**<br>**- Aporte del Proyecto**|**Concentración Total**<br>**Esperada (mg/m3N)**|**Concentración Total**<br>**Esperada (mg/m3N)**|**Norma de Calidad**<br>**(mg/m3N)**|**Norma de Calidad**<br>**(mg/m3N)**|**Porcentaje de la**<br>**Norma de Calidad**|**Porcentaje de la**<br>**Norma de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil**<br>**99 1 hora**|**Percentil 99**<br>**8 horas**|**Percentil**<br>**99 1 hora**|**Percentil 99**<br>**8 horas**|**Percentil**<br>**99 1 hora**|**Percentil**<br>**99 8 horas**|**Percentil**<br>**99 1 hora**|**Percentil**<br>**99 8 horas**|**Percentil**<br>**99 1 hora**|**Percentil**<br>**99 8**<br>**horas**|
|R_1|Estación Rancagua I|342.015|6.218.523|6,55|4,55|1,75E-04|3,57E-05|6,55|4,55|30|10|22%|46%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

156

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Tabla 2-48 se presenta la concentración total esperada para el contaminante Dióxido de Azufre (SO 2 ) en el receptor Estación

Rancagua I para el escenario 1:

**Tabla 2-48. Concentración total esperada. Dióxido de Azufre (SO** **2** **). Escenario 1.**

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Dióxido de Azufre (SO)<br>2|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración**<br>**(μg/m3N) - Línea de**<br>**Base**|**Concentración**<br>**(μg/m3N) - Línea de**<br>**Base**|**Concentración (μg/m3N) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3N) -**<br>**Aporte del Proyecto**|**Concentración Total**<br>**Esperada (μg/m3N)**|**Concentración Total**<br>**Esperada (μg/m3N)**|**Norma de Calidad**<br>**(μg/m3N)**|**Norma de Calidad**<br>**(μg/m3N)**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil**<br>**99 24**<br>**horas**|**Período**<br>**Anual**|**Percentil 99**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 99**<br>**24 horas**|**Período**<br>**Anual**|**Percentil**<br>**99 24**<br>**horas**|**Período**<br>**Anual**|**Percentil 99**<br>**24 horas**|**Período**<br>**Anual**|
|R_1|Estación Rancagua I|342.015|6.218.523|13,30|4,00|1,48E-02|2,39E-03|13,31|4,00|250|80|5%|5%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

157

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**2.12.2** **Escenario 2: Operación Proyectada**

En la Tabla 2-49 se presenta la concentración total esperada para el contaminante Material Particulado Respirable Fino (MP2.5) en

los receptores Estación Rancagua I y Estación Rancagua II para el escenario 2:

**Tabla 2-49. Concentración total esperada. Material Particulado Respirable Fino (MP2.5). Escenario 2.**

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación (Datum<br>WGS84)|Col4|Material Particulado Respirable Fino (MP2.5)|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación (Datum**<br>**WGS84)**|**Coordenadas de**<br>**Ubicación (Datum**<br>**WGS84)**|**Concentración**<br>**(μg/m3N) - Línea de**<br>**Base**|**Concentración**<br>**(μg/m3N) - Línea de**<br>**Base**|**Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración Total**<br>**Esperada (μg/m3N)**|**Concentración Total**<br>**Esperada (μg/m3N)**|**Norma de Calidad**<br>**(μg/m3N)**|**Norma de Calidad**<br>**(μg/m3N)**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|
|R_1|Estación Rancagua I|342.015|6.218.523|88,90|24,10|0,00|0,00|88,90|24,10|50|20|178%|121%|
|R_2|Estación Rancagua II|339.842|6.220.527|110,00|30,20|0,00|0,00|110,00|30,20|30,20|30,20|220%|151%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

158

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Tabla 2-50 se presenta la concentración total esperada para el contaminante Material Particulado Respirable (MP10) en los

receptores Estación Rancagua I y Estación Rancagua II para el escenario 2:

**Tabla 2-50. Concentración total esperada. Material Particulado Respirable (MP10). Escenario 2.**

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Material Particulado Respirable (MP10)|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración**<br>**(μg/m3N) - Línea de**<br>**Base**|**Concentración**<br>**(μg/m3N) - Línea de**<br>**Base**|**Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto**|**Concentración Total**<br>**Esperada (μg/m3N)**|**Concentración Total**<br>**Esperada (μg/m3N)**|**Norma de Calidad**<br>**(μg/m3N)**|**Norma de Calidad**<br>**(μg/m3N)**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil**<br>**98 24**<br>**horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 98**<br>**24 horas**|**Período**<br>**Anual**|
|R_1|Estación Rancagua I|342.015|6.218.523|181,70|72,80|0,01|0,00|181,71|72,80|150|50|121%|146%|
|R_2|Estación Rancagua II|339.842|6.220.527|157,60|60,00|0,01|0,00|157,61|60,00|60,00|60,00|105%|120%|

Fuente: Elaboración propia.

En la Tabla 2-51 se presenta la concentración total esperada para el contaminante Monóxido de Carbono (CO) en el receptor

Estación Rancagua I para el escenario 2:

**Tabla 2-51. Concentración total esperada. Monóxido de Carbono (CO). Escenario 2.**

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Monóxido de Carbono (CO)|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración (mg/m3N)**<br>**- Línea de Base**|**Concentración (mg/m3N)**<br>**- Línea de Base**|**Concentración (mg/m3N)**<br>**- Aporte del Proyecto**|**Concentración (mg/m3N)**<br>**- Aporte del Proyecto**|**Concentración Total**<br>**Esperada (mg/m3N)**|**Concentración Total**<br>**Esperada (mg/m3N)**|**Norma de Calidad**<br>**(mg/m3N)**|**Norma de Calidad**<br>**(mg/m3N)**|**Porcentaje de la**<br>**Norma de Calidad**|**Porcentaje de la**<br>**Norma de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil**<br>**99 1 hora**|**Percentil 99**<br>**8 horas**|**Percentil**<br>**99 1 hora**|**Percentil 99**<br>**8 horas**|**Percentil**<br>**99 1 hora**|**Percentil**<br>**99 8 horas**|**Percentil**<br>**99 1 hora**|**Percentil**<br>**99 8 horas**|**Percentil**<br>**99 1 hora**|**Percentil**<br>**99 8**<br>**horas**|
|R_1|Estación Rancagua I|342.015|6.218.523|6,55|4,55|1,45E-04|3,39E-05|6,55|4,55|30|10|4%|9%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

159

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

En la Tabla 2-52 se presenta la concentración total esperada para el contaminante Dióxido de Azufre (SO 2 ) en el receptor Estación

Rancagua I para el escenario 2:

**Tabla 2-52. Concentración total esperada. Dióxido de Azufre (SO** **2** **). Escenario 2.**

|ID<br>Receptor|Descripción|Coordenadas de<br>Ubicación<br>(Datum WGS84)|Col4|Dióxido de Azufre (SO)<br>2|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|Col14|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|**ID**<br>**Receptor**|**Descripción**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)**|**Concentración**<br>**(μg/m3N) - Línea de**<br>**Base**|**Concentración**<br>**(μg/m3N) - Línea de**<br>**Base**|**Concentración (μg/m3N) -**<br>**Aporte del Proyecto**|**Concentración (μg/m3N) -**<br>**Aporte del Proyecto**|**Concentración Total**<br>**Esperada (μg/m3N)**|**Concentración Total**<br>**Esperada (μg/m3N)**|**Norma de Calidad**<br>**(μg/m3N)**|**Norma de Calidad**<br>**(μg/m3N)**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**ID**<br>**Receptor**|**Descripción**|**Este (m)**|**Norte (m)**|**Percentil**<br>**99 24**<br>**horas**|**Período**<br>**Anual**|**Percentil 99**<br>**24 horas**|**Período**<br>**Anual**|**Percentil 99**<br>**24 horas**|**Período**<br>**Anual**|**Percentil**<br>**99 24**<br>**horas**|**Período**<br>**Anual**|**Percentil 99**<br>**24 horas**|**Período**<br>**Anual**|
|R_1|Estación Rancagua I|342.015|6.218.523|13,30|4,00|1,47E-02|2,37E-03|13,31|4,00|250|80|5%|5%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

160

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

#### 3 CONCLUSIONES

A través del presente estudio se han discutido las características meteorológicas en el área

del Proyecto y se desarrolló un análisis de incertidumbre para el modelo meteorológico en

las Estaciones Rancagua I y Rancagua II, se observó que el modelo sobrestima el

comportamiento de la velocidad del viento en dichos puntos, lo que se podría traducir en

una subestimación de los aportes por lo que se determinó aplicar un factor de corrección.

A continuación se presentan las principales conclusiones de los escenarios de modelación

de calidad del aire desarrollados:

**3.1** **Conclusiones Modelación Escenario 1**

Para el primer escenario modelado (Construcción Etapa 2 y Operación Proyectada), se
concluye que los principales aportes del proyecto por contaminante son los siguientes:

 - Material Particulado Respirable Fino (MP2.5): el mayor aporte del proyecto para la

norma de percentil 98 de 24 horas corresponde al receptor 5 (vivienda 3) con un
4,77% de la norma. Para la norma de periodo anual el mayor aporte del proyecto
corresponde al receptor 10 (vivienda 8) con un 1,74% de la norma.

 - Material Particulado Respirable (MP10): el mayor aporte del proyecto para la

norma de percentil 98 de 24 horas corresponde al receptor 5 (vivienda 3) con un
2,42% de la norma. Para la norma de periodo anual el mayor aporte del proyecto
corresponde al receptor 5 (vivienda 3) con un 1,12% de la norma.

 - Monóxido de Carbono (CO): el mayor aporte del proyecto para la norma de

percentil 99 de 1 hora corresponde al receptor 12 (vivienda 10) con un 0,25% de la
norma. Para la norma de percentil 99 de 8 horas el mayor aporte del proyecto
corresponde al receptor 5 (vivienda 3) con un 0,24% de la norma.

 - Dióxido de Nitrógeno (NO 2 ): el mayor aporte del proyecto para la norma de

percentil 99 de 1 hora corresponde al receptor 12 (vivienda 10) con un 60,09% de
la norma. Para la norma de periodo anual el mayor aporte del proyecto
corresponde al receptor 10 (vivienda 8) con un 3,32% de la norma.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

161

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

 - Dióxido de Azufre (SO 2 ): el mayor aporte del proyecto para la norma de percentil

99 de 24 horas corresponde al receptor 10 (vivienda 8) con un 0,23% de la norma.
Para la norma de periodo anual el mayor aporte del proyecto corresponde al
receptor 10 (vivienda 8) con un 0,27% de la norma.

**3.2** **Conclusiones Modelación Escenario 2**

Para el segundo escenario modelado (Operación Proyectada), se concluye que los
principales aportes del proyecto por contaminante son los siguientes:

 - Material Particulado Respirable Fino (MP2.5): el mayor aporte del proyecto para la

norma de percentil 98 de 24 horas corresponde al receptor 5 (vivienda 3) con un
0,40% de la norma. Para la norma de periodo anual el mayor aporte del proyecto
corresponde al receptor 5 (vivienda 3) con un 0,42% de la norma.

 - Material Particulado Respirable (MP10): el mayor aporte del proyecto para la

norma de percentil 98 de 24 horas corresponde al receptor 5 (vivienda 3) con un
0,51% de la norma. Para la norma de periodo anual el mayor aporte del proyecto
corresponde al receptor 5 (vivienda 3) con un 0,64% de la norma.

 - Monóxido de Carbono (CO): el mayor aporte del proyecto para la norma de

percentil 99 de 1 hora corresponde al receptor 12 (vivienda 10) con un 0,04% de la
norma. Para la norma de percentil 99 de 8 horas el mayor aporte del proyecto
corresponde al receptor 12 (vivienda 10) con un 0,04% de la norma.

 - Dióxido de Nitrógeno (NO 2 ): el mayor aporte del proyecto para la norma de

percentil 99 de 1 hora corresponde al receptor 10 (vivienda 8) con un 31,98% de la
norma. Para la norma de periodo anual el mayor aporte del proyecto corresponde
al receptor 10 (vivienda 8) con un 1,19% de la norma.

 - Dióxido de Azufre (SO 2 ): el mayor aporte del proyecto para la norma de percentil

99 de 24 horas corresponde al receptor 10 (vivienda 8) con un 0,23% de la norma.
Para la norma de periodo anual el mayor aporte del proyecto corresponde al
receptor 10 (vivienda 8) con un 0,26% de la norma.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

162

**Proyecto “Actualización y Desarrollo**

**Planta Faenadora de Aves Lo Miranda”**

Modelación de Dispersión de Contaminantes Atmosféricos

Abril 2018

**3.3** **Conclusiones Respecto a la Concentración Total Esperada**

El proyecto verifica aportes nulos (menores a 0,5 μg/m [3] N) para los contaminantes MP2,5,

MP10, CO y SO 2 en los receptores correspondientes a las estaciones de monitoreo

Rancagua I y Rancagua II, en los dos Escenarios planteados, para los cuales se cuenta con

un monitores de calidad del aire. Según lo anterior el proyecto no generaría impactos

significativos en dichos puntos, considerando que actualmente dichas estaciones

muestran una condición de saturación para los contaminantes Material Particulado Fino

(MP2,5) y Material Particulado Respirable (MP10).

www.dfmconsultores.cl

**info@dfmconsultores.cl**

163

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2-1: - Coordenadas de Ubicación Estaciones de Monitoreo Meteorológico.****

| Estación de<br>Monitoreo | Variables Meteorológicas<br>Registradas | Periodo monitoreado<br>considerado para este<br>estudio | Coordenadas UTM [Datum<br>WGS84] | Col5 |
| --- | --- | --- | --- | --- |
| **Estación de**<br>**Monitoreo** | **Variables Meteorológicas**<br>**Registradas** | **Periodo monitoreado**<br>**considerado para este**<br>**estudio** | **Este [m]** | **Norte [m]** |
| Rancagua I | Velocidad del Viento [m/s]<br>Dirección del Viento [°]<br>Temperatura del Aire [°C]<br>Humedad Relativa [%]<br>Radiación Solar [W/m2] | Enero de 2015 a diciembre<br>de 2017 | 342.015 | 6.218.523 |
| Rancagua II | Velocidad del Viento [m/s]<br>Dirección del Viento [°]<br>Temperatura del Aire [°C]<br>Humedad Relativa [%]<br>Radiación Solar [W/m2] | Enero de 2015 a diciembre<br>de 2017 | 339.842 | 6.220.527 |

**Tabla 2-2.: Resumen de Información Velocidad del Viento Observada. Estación Rancagua I.****

| Parámetro | Variable | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2015** | **2016** | **2017** |
| Velocidad de<br>Viento (m/s) | Promedio | 1,59 | 1,46 | 1,44 |
| Velocidad de<br>Viento (m/s) | Máxima | 6,80 | 6,90 | 6,60 |
| Velocidad de<br>Viento (m/s) | Mínima | 0,20 | 0,00 | 0,00 |
| Velocidad de<br>Viento (m/s) | Porcentaje de Calmas (%) | 0,53% | 3,49% | 2,20% |
| Velocidad de<br>Viento (m/s) | Datos Válidos (%) | 99,76% | 99,84% | 97,99% |

**Tabla 2-3: - Frecuencia de Distribución, Velocidad y Dirección del Viento. Periodo enero 2015 a diciembre****

| Dirección | Col2 | Distribución Porcentual de Velocidad del Viento (m/s) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección** | **Dirección** | **0,50 - 2,10** | **2,10 - 3,60** | **3,60 - 5,70** | **5,70 - 8,80** | **8,80 - 11,10** | **>= 11,10** | **Total (%)** |
| 348,75 - 11,25 | N | 1,92% | 0,23% | 0,06% | 0,00% | 0,00% | 0,00% | 2,20% |
| 11,25 - 33,75 | NNE | 1,88% | 0,48% | 0,27% | 0,02% | 0,00% | 0,00% | 2,65% |
| 33,75 - 56,25 | NE | 1,91% | 0,60% | 0,20% | 0,01% | 0,00% | 0,00% | 2,72% |
| 56,25 - 78,75 | ENE | 1,64% | 0,38% | 0,03% | 0,00% | 0,00% | 0,00% | 2,05% |
| 78,75 - 101,25 | E | 1,60% | 0,19% | 0,02% | 0,00% | 0,00% | 0,00% | 1,81% |
| 101,25 - 123,75 | ESE | 1,95% | 0,06% | 0,04% | 0,00% | 0,00% | 0,00% | 2,06% |
| 123,75 - 146,25 | SE | 3,48% | 0,07% | 0,00% | 0,00% | 0,00% | 0,00% | 3,55% |
| 146,25 - 168,75 | SSE | 7,75% | 0,49% | 0,02% | 0,00% | 0,00% | 0,00% | 8,26% |
| 168,75 - 191,25 | S | 8,44% | 0,21% | 0,00% | 0,00% | 0,00% | 0,00% | 8,66% |
| 191,25 - 213,75 | SSW | 12,86% | 7,78% | 0,24% | 0,00% | 0,00% | 0,00% | 20,88% |
| 213,75 - 236,25 | SW | 20,45% | 8,55% | 0,18% | 0,00% | 0,00% | 0,00% | 29,18% |
| 236,25 - 258,75 | WSW | 5,71% | 0,38% | 0,00% | 0,00% | 0,00% | 0,00% | 6,09% |
| 258,75 - 281,25 | W | 2,41% | 0,07% | 0,00% | 0,00% | 0,00% | 0,00% | 2,49% |
| 281,25 - 303,75 | WNW | 1,81% | 0,03% | 0,00% | 0,00% | 0,00% | 0,00% | 1,84% |
| 303,75 - 326,25 | NW | 1,69% | 0,03% | 0,00% | 0,00% | 0,00% | 0,00% | 1,73% |
| 326,25 - 348,75 | NNW | 1,65% | 0,09% | 0,02% | 0,00% | 0,00% | 0,00% | 1,76% |
| Sub-Total | Sub-Total | 77,15% | 19,64% | 1,09% | 0,05% | 0,00% | 0,00% | 97,93% |
| Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | 2,07% |

**Tabla 2-4: - Resumen de Información Temperatura Observada en Estación Rancagua I.****

| Parámetro | Variable | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2015** | **2016** | **2017** |
| Temperatura<br>(°C) | Promedio | 17,98 | 18,00 | 17,57 |
| Temperatura<br>(°C) | Máxima | 36,50 | 37,10 | 37,00 |
| Temperatura<br>(°C) | Mínima | 1,40 | 1,60 | -1,00 |
| Temperatura<br>(°C) | Datos Válidos (%) | 99,76% | 99,84% | 97,99% |

**Tabla 2-5.: Resumen de Información Humedad Relativa Observada en Estación Rancagua I.****

| Parámetro | Variable | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2015** | **2016** | **2017** |
| Humedad<br>Relativa (%) | Promedio | 57,02 | 60,84 | 59,57 |
| Humedad<br>Relativa (%) | Máxima | 92,00 | 92,00 | 92,00 |
| Humedad<br>Relativa (%) | Mínima | 10,00 | 6,00 | 0,00 |
| Humedad<br>Relativa (%) | % Datos Válidos | 99,76% | 99,84% | 97,99% |

**Tabla 2-6.: Resumen de Información Radiación Solar Observada en Estación Rancagua I.****

| Parámetro | Variable | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2015** | **2016** | **2017** |
| Radiación Solar (W/m2) | Promedio | 364,37 | 376,66 | 374,14 |
| Radiación Solar (W/m2) | Máxima | 1464,00 | 1226,00 | 1049,00 |
| Radiación Solar (W/m2) | Mínima | 0,00 | 0,00 | 0,00 |
| Radiación Solar (W/m2) | % Datos Válidos | 58,20% | 50,16% | 49,14% |

**Tabla 2-7.: Resumen de Información Velocidad del Viento Observada. Estación Rancagua II.****

| Parámetro | Variable | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2015** | **2016** | **2017** |
| Velocidad de<br>Viento (m/s) | Promedio | 2,25 | 2,13 | 2,17 |
| Velocidad de<br>Viento (m/s) | Máxima | 7,70 | 6,90 | 7,10 |
| Velocidad de<br>Viento (m/s) | Mínima | 0,00 | 0,00 | 0,00 |
| Velocidad de<br>Viento (m/s) | Porcentaje de Calmas (%) | 0,00% | 4,84% | 7,50% |
| Velocidad de<br>Viento (m/s) | Datos Válidos (%) | 99,67% | 99,41% | 98,85% |

**Tabla 2-8: - Frecuencia de Distribución, Velocidad y Dirección del Viento. Periodo enero 2015 a diciembre****

| Dirección | Col2 | Distribución Porcentual de Velocidad del Viento (m/s) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección** | **Dirección** | **0,50 - 2,10** | **2,10 - 3,60** | **3,60 - 5,70** | **5,70 - 8,80** | **8,80 - 11,10** | **>= 11,10** | **Total (%)** |
| 348,75 - 11,25 | N | 1,91% | 0,20% | 0,07% | 0,01% | 0,00% | 0,00% | 2,19% |
| 11,25 - 33,75 | NNE | 2,34% | 0,26% | 0,05% | 0,00% | 0,00% | 0,00% | 2,65% |
| 33,75 - 56,25 | NE | 3,69% | 0,29% | 0,05% | 0,00% | 0,00% | 0,00% | 4,03% |
| 56,25 - 78,75 | ENE | 3,63% | 0,26% | 0,04% | 0,00% | 0,00% | 0,00% | 3,92% |
| 78,75 - 101,25 | E | 3,28% | 0,20% | 0,04% | 0,00% | 0,00% | 0,00% | 3,53% |
| 101,25 - 123,75 | ESE | 3,10% | 0,16% | 0,03% | 0,00% | 0,00% | 0,00% | 3,29% |
| 123,75 - 146,25 | SE | 4,03% | 1,63% | 0,56% | 0,00% | 0,00% | 0,00% | 6,22% |
| 146,25 - 168,75 | SSE | 6,26% | 12,35% | 13,25% | 0,28% | 0,00% | 0,00% | 32,13% |
| 168,75 - 191,25 | S | 6,21% | 8,74% | 4,01% | 0,04% | 0,00% | 0,00% | 18,99% |
| 191,25 - 213,75 | SSW | 4,51% | 1,28% | 0,04% | 0,00% | 0,00% | 0,00% | 5,83% |
| 213,75 - 236,25 | SW | 3,69% | 0,34% | 0,05% | 0,00% | 0,00% | 0,00% | 4,08% |
| 236,25 - 258,75 | WSW | 2,24% | 0,19% | 0,04% | 0,00% | 0,00% | 0,00% | 2,46% |
| 258,75 - 281,25 | W | 1,68% | 0,16% | 0,07% | 0,01% | 0,00% | 0,00% | 1,91% |
| 281,25 - 303,75 | WNW | 1,24% | 0,18% | 0,11% | 0,02% | 0,00% | 0,00% | 1,55% |
| 303,75 - 326,25 | NW | 1,04% | 0,16% | 0,07% | 0,03% | 0,00% | 0,00% | 1,31% |
| 326,25 - 348,75 | NNW | 1,17% | 0,20% | 0,13% | 0,01% | 0,00% | 0,00% | 1,51% |
| Sub-Total | Sub-Total | 50,00% | 26,61% | 18,59% | 0,41% | 0,00% | 0,00% | 95,61% |
| Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | 4,39% |

**Tabla 2-9: - Resumen de Información Temperatura Observada en Estación Rancagua II.****

| Parámetro | Variable | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2015** | **2016** | **2017** |
| Temperatura<br>(°C) | Promedio | 15,61 | 15,74 | 15,30 |
| Temperatura<br>(°C) | Máxima | 34,60 | 34,90 | 35,90 |
| Temperatura<br>(°C) | Mínima | -2,50 | -1,40 | -3,70 |
| Temperatura<br>(°C) | Datos Válidos (%) | 99,67% | 99,41% | 98,85% |

**Tabla 2-10.: Resumen de Información Humedad Relativa Observada en Estación Rancagua II.****

| Parámetro | Variable | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2015** | **2016** | **2017** |
| Humedad<br>Relativa (%) | Promedio | 61,24 | 64,30 | 62,82 |
| Humedad<br>Relativa (%) | Máxima | 95,00 | 95,00 | 95,00 |
| Humedad<br>Relativa (%) | Mínima | 9,00 | 7,00 | 0,00 |
| Humedad<br>Relativa (%) | % Datos Válidos | 99,67% | 99,41% | 98,82% |

**Tabla 2-11.: Resumen de Información Radiación Solar Observada en Estación Rancagua II.****

| Parámetro | Variable | Año | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2015** | **2016** | **2017** |
| Radiación Solar<br>(W/m2) | Promedio | 192,49 | 183,70 | 188,13 |
| Radiación Solar<br>(W/m2) | Máxima | 1039,00 | 1036,00 | 1090,00 |
| Radiación Solar<br>(W/m2) | Mínima | 0,00 | 0,00 | 0,00 |
| Radiación Solar<br>(W/m2) | % Datos Válidos | 99,61% | 99,39% | 98,82% |

**Tabla 2-12.: Resumen de Información Velocidad del Viento Modelada. Estación Rancagua I.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2016** |
| Velocidad de Viento (m/s) | Promedio | 2,52 |
| Velocidad de Viento (m/s) | Máxima | 10,11 |
| Velocidad de Viento (m/s) | Mínima | 0,02 |
| Velocidad de Viento (m/s) | Porcentaje de Calmas (%) | 3,53% |
| Velocidad de Viento (m/s) | Datos Válidos (%) | 100,00% |

**Tabla 2-13: - Frecuencia de Distribución, Velocidad y Dirección del Viento. Período enero a diciembre 2016.****

| Dirección | Col2 | Distribución Porcentual de Velocidad del Viento (m/s) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección** | **Dirección** | **0,50 -**<br>**2,10** | **2,10 -**<br>**3,60** | **3,60 -**<br>**5,70** | **5,70 -**<br>**8,80** | **8,80 -**<br>**11,10** | **>=**<br>**11,10** | **Total**<br>**(%)** |
| 348,75 - 11,25 | N | 1,05% | 0,80% | 1,90% | 0,88% | 0,10% | 0,00% | 4,72% |
| 11,25 - 33,75 | NNE | 2,41% | 1,97% | 0,87% | 0,38% | 0,02% | 0,00% | 5,65% |
| 33,75 - 56,25 | NE | 3,56% | 1,66% | 0,46% | 0,02% | 0,00% | 0,00% | 5,70% |
| 56,25 - 78,75 | ENE | 1,98% | 0,76% | 0,13% | 0,01% | 0,00% | 0,00% | 2,88% |
| 78,75 - 101,25 | E | 1,53% | 0,46% | 0,09% | 0,00% | 0,00% | 0,00% | 2,07% |
| 101,25 - 123,75 | ESE | 1,50% | 0,27% | 0,14% | 0,03% | 0,00% | 0,00% | 1,95% |
| 123,75 - 146,25 | SE | 1,55% | 0,18% | 0,07% | 0,00% | 0,00% | 0,00% | 1,80% |
| 146,25 - 168,75 | SSE | 1,48% | 0,33% | 0,05% | 0,01% | 0,00% | 0,00% | 1,87% |
| 168,75 - 191,25 | S | 2,28% | 0,59% | 0,10% | 0,00% | 0,00% | 0,00% | 2,97% |
| 191,25 - 213,75 | SSW | 5,29% | 4,16% | 2,15% | 0,19% | 0,00% | 0,00% | 11,79% |
| 213,75 - 236,25 | SW | 10,25% | 17,70% | 8,99% | 0,72% | 0,01% | 0,00% | 37,67% |
| 236,25 - 258,75 | WSW | 4,37% | 3,11% | 1,92% | 0,56% | 0,00% | 0,00% | 9,96% |
| 258,75 - 281,25 | W | 1,34% | 0,42% | 0,22% | 0,01% | 0,00% | 0,00% | 1,99% |
| 281,25 - 303,75 | WNW | 0,88% | 0,51% | 0,47% | 0,11% | 0,00% | 0,00% | 1,97% |
| 303,75 - 326,25 | NW | 0,81% | 0,48% | 0,60% | 0,06% | 0,00% | 0,00% | 1,95% |
| 326,25 - 348,75 | NNW | 0,81% | 0,34% | 0,23% | 0,13% | 0,02% | 0,00% | 1,53% |
| Sub-Total | Sub-Total | 41,09% | 33,74% | 18,37% | 3,11% | 0,16% | 0,00% | 96,47% |
| Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | 3,53% |

**Tabla 2-14: - Resumen de Información Temperatura Modelada en Estación Rancagua I.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2016** |
| Temperatura (°C) | Promedio | 19,39 |
| Temperatura (°C) | Máxima | 37,17 |
| Temperatura (°C) | Mínima | 4,21 |
| Temperatura (°C) | Datos Válidos (%) | 100,00% |

**Tabla 2-15.: Resumen de Información Velocidad del Viento Modelada. Estación Rancagua II.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2016** |
| Velocidad de Viento (m/s) | Promedio | 2,52 |
| Velocidad de Viento (m/s) | Máxima | 9,92 |
| Velocidad de Viento (m/s) | Mínima | 0,04 |
| Velocidad de Viento (m/s) | Porcentaje de Calmas (%) | 4,08% |
| Velocidad de Viento (m/s) | Datos Válidos (%) | 100,00% |

**Tabla 2-16: - Frecuencia de Distribución, Velocidad y Dirección del Viento. Período enero a diciembre 2016.****

| Dirección | Col2 | Distribución Porcentual de Velocidad del Viento (m/s) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección** | **Dirección** | **0,50 - 2,10** | **2,10 - 3,60** | **3,60 - 5,70** | **5,70 - 8,80** | **8,80 - 11,10** | **>= 11,10** | **Total (%)** |
| 348,75 - 11,25 | N | 0,96% | 0,66% | 1,01% | 0,49% | 0,01% | 0,00% | 3,13% |
| 11,25 - 33,75 | NNE | 1,94% | 1,15% | 1,79% | 0,76% | 0,08% | 0,00% | 5,71% |
| 33,75 - 56,25 | NE | 3,35% | 1,65% | 0,44% | 0,01% | 0,00% | 0,00% | 5,45% |
| 56,25 - 78,75 | ENE | 3,18% | 1,05% | 0,14% | 0,03% | 0,00% | 0,00% | 4,39% |
| 78,75 - 101,25 | E | 1,72% | 0,51% | 0,05% | 0,01% | 0,00% | 0,00% | 2,29% |
| 101,25 - 123,75 | ESE | 1,21% | 0,17% | 0,06% | 0,01% | 0,00% | 0,00% | 1,45% |
| 123,75 - 146,25 | SE | 0,72% | 0,11% | 0,01% | 0,01% | 0,00% | 0,00% | 0,85% |
| 146,25 - 168,75 | SSE | 0,91% | 0,27% | 0,03% | 0,00% | 0,00% | 0,00% | 1,22% |
| 168,75 - 191,25 | S | 2,08% | 0,85% | 0,09% | 0,01% | 0,00% | 0,00% | 3,04% |
| 191,25 - 213,75 | SSW | 9,18% | 11,02% | 4,57% | 0,17% | 0,00% | 0,00% | 24,93% |
| 213,75 - 236,25 | SW | 8,94% | 14,28% | 6,71% | 0,89% | 0,00% | 0,00% | 30,81% |
| 236,25 - 258,75 | WSW | 2,22% | 1,55% | 1,26% | 0,25% | 0,00% | 0,00% | 5,28% |
| 258,75 - 281,25 | W | 1,14% | 0,49% | 0,24% | 0,01% | 0,00% | 0,00% | 1,88% |
| 281,25 - 303,75 | WNW | 0,66% | 0,47% | 0,90% | 0,17% | 0,00% | 0,00% | 2,20% |
| 303,75 - 326,25 | NW | 0,61% | 0,50% | 0,80% | 0,03% | 0,00% | 0,00% | 1,95% |
| 326,25 - 348,75 | NNW | 0,77% | 0,27% | 0,17% | 0,13% | 0,00% | 0,00% | 1,34% |
| Sub-Total | Sub-Total | 39,57% | 35,01% | 18,26% | 2,99% | 0,09% | 0,00% | 95,92% |
| Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | 4,08% |

**Tabla 2-17: - Resumen de Información Temperatura Modelada en Estación Rancagua II.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2016** |
| Temperatura (°C) | Promedio | 19,52 |
| Temperatura (°C) | Máxima | 37,27 |
| Temperatura (°C) | Mínima | 4,80 |
| Temperatura (°C) | Datos Válidos (%) | 100,00% |

**Tabla 2-18: - Resumen de Información Altura de Capa de Mezcla Modelada en Estación Rancagua I.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2016** |
| Altura de Capa de Mezcla (m) | Promedio | 654,93 |
| Altura de Capa de Mezcla (m) | Máxima | 3.500,00 |
| Altura de Capa de Mezcla (m) | Mínima | 10,00 |
| Altura de Capa de Mezcla (m) | % Datos Válidos | 100,00% |

**Tabla 2-19: - Resumen de Información Altura de Capa de Mezcla Modelada en Estación Rancagua II.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2016** |
| Altura de Capa de Mezcla (m) | Promedio | 663,86 |
| Altura de Capa de Mezcla (m) | Máxima | 3.500,00 |
| Altura de Capa de Mezcla (m) | Mínima | 10,00 |
| Altura de Capa de Mezcla (m) | % Datos Válidos | 100,00% |

**Tabla 2-21.: Comparación Resultados Observados y Modelados de Velocidad del Viento y Dirección del Viento. Periodo enero a diciembre 2016. Estación****

| Comparación | Observado | Modelado |
| --- | --- | --- |
| Ciclo Diario de<br>Velocidad del<br>Viento |  |  |

**Tabla 2-22.: Comparación Resultados Observados y Modelados de Temperatura. Periodo enero a diciembre 2016. Estación Rancagua I.****

| Comparación | Observado | Modelado |
| --- | --- | --- |
| Ciclo Diario de<br>Temperatura |  |  |

**Tabla 2-23.: Comparación Resultados Observados y Modelados de Temperatura. Periodo enero a diciembre 2016. Estación Rancagua I.****

| Comparación | Observado | Modelado |
| --- | --- | --- |
| Ciclo Diario de<br>Temperatura |  |  |

**Tabla 2-24.: Estadígrafos de Dispersión para Velocidad del Viento y Temperatura.****

| Medida de Error | Estación Rancagua I | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| **Medida de Error** | **Velocidad** | **Velocidad** | **Temperatura** | **Temperatura** |
| **Medida de Error** | **Serie de Tiempo** | **Ciclo Diario** | **Serie de Tiempo** | **Ciclo Diario** |
| Sesgo | 1,06 m/s | 1,06 m/s | 1,39 °C | 1,39 °C |
| ECM | 1,64 m/s | 1,17 m/s | 3,10 °C | 1,58 °C |
| r | 0,54 | 0,89 | 0,91 | 0,98 |
| **Medida de Error** | **Estación Rancagua II** | **Estación Rancagua II** | **Estación Rancagua II** | **Estación Rancagua II** |
| **Medida de Error** | **Velocidad** | **Velocidad** | **Temperatura** | **Temperatura** |
| **Medida de Error** | **Serie de Tiempo** | **Ciclo Diario** | **Serie de Tiempo** | **Ciclo Diario** |
| Sesgo | 0,38 m/s | 0,39 m/s | 3,77 °C | 3,78 °C |
| ECM | 1,38 m/s | 0,47 m/s | 4,85 °C | 3,89 °C |
| r | 0,55 | 0,95 | 0,91 | 0,98 |

**Tabla 2-25: - Normas de calidad del aire.****

| Contaminante | Decreto Aplicable | Norma | Col4 | Periodo de Evaluación de<br>Cumplimiento de Norma |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Decreto Aplicable** | **Valor** | **Unidad** | **Unidad** |
| Material<br>Particulado<br>Respirable Fino<br>(MP2,5) | Decreto Supremo N°12/2011 | 50 | μg/m3 | Percentil 98 de la media<br>aritmética diaria durante un<br>año |
| Material<br>Particulado<br>Respirable Fino<br>(MP2,5) | Decreto Supremo N°12/2011 | 20 | 20 | Media aritmética trianual |
| Material<br>Particulado<br>Respirable<br>(MP10) | Decreto Supremo N°59/98 | 150 | μg/m3N | Percentil 98 de la media<br>aritmética diaria durante un<br>año |
| Material<br>Particulado<br>Respirable<br>(MP10) | Decreto Supremo N°59/98 | 50 | 50 | Media aritmética trianual |
| Dióxido de<br>nitrógeno (NO2) | Decreto Supremo No114/02 | 400 | μg/m3N <br> | Percentil 99 de la media<br>aritmética horaria durante un<br>año |
| Dióxido de<br>nitrógeno (NO2) | Decreto Supremo No114/02 | 100 | μg/m~~3~~N | Media aritmética trianual |
| Dióxido de<br>azufre (SO2) | Decreto Supremo 113/02 | 250 | μg/m3N <br> | Percentil 99 anual de la<br>media aritmética diaria |
| Dióxido de<br>azufre (SO2) | Decreto Supremo 113/02 | 80 | μg/m~~3~~N | Media aritmética trianual |
| Monóxido de<br>Carbono (CO) | Decreto Supremo N°115/02 | 30 | mg/m3N | Percentil 99 de la media<br>aritmética horaria durante un<br>año |
| Monóxido de<br>Carbono (CO) | Decreto Supremo N°115/02 | 10 | mg/m3N | Percentil 99 de la media<br>aritmética de 8 horas durante<br>un año |

**Tabla 2-26: - Estaciones monitoras de calidad del aire.****

| Nombre | Coordenadas UTM, Huso 19 S, Datum WGS-84 | Col3 |
| --- | --- | --- |
| **Nombre** | **Este [m]** | **Norte [m]** |
| Estación Rancagua I | 342.015 | 6.218.523 |
| Estación Rancagua II | 339.842 | 6.220.527 |

**Tabla 2-27: -Calidad del Aire Estación Rancagua I.****

| Contaminante | Estadígrafo | Periodo | Valor | Unidad | Valor<br>Norma | Porcentaje de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP2,5 | P98 24 horas | 2015 | 74,7 | μg/m3 | 50 | 149% |
| MP2,5 | P98 24 horas | 2016 | 88,9 | 88,9 | 88,9 | 178% |
| MP2,5 | P98 24 horas | 2017 | 73,0 | 73,0 | 73,0 | 146% |
| MP2,5 | P98 24 horas | Mayor valor 2015-2017 | 88,9 | 88,9 | 88,9 | 178% |
| MP2,5 | Promedio Anual | 2015 | 24,2 | 24,2 | 20 | 121% |
| MP2,5 | Promedio Anual | 2016 | 24,4 | 24,4 | 24,4 | 122% |
| MP2,5 | Promedio Anual | 2017 | 23,6 | 23,6 | 23,6 | 118% |
| MP2,5 | Promedio Anual | Promedio 2015-2017 | 24,1 | 24,1 | 24,1 | 120% |
| MP10 | P98 24 horas | 2015 | 181,7 | μg/m3N | 150 | 121% |
| MP10 | P98 24 horas | 2016 | 153,8 | 153,8 | 153,8 | 103% |
| MP10 | P98 24 horas | 2017 | 133,0 | 133,0 | 133,0 | 89% |
| MP10 | P98 24 horas | Mayor valor 2015-2017 | 181,7 | 181,7 | 181,7 | 121% |
| MP10 | Promedio Anual | 2015 | 80,7 | 80,7 | 50 | 161% |
| MP10 | Promedio Anual | 2016 | 73,2 | 73,2 | 73,2 | 146% |
| MP10 | Promedio Anual | 2017 | 64,6 | 64,6 | 64,6 | 129% |
| MP10 | Promedio Anual | Promedio 2015-2017 | 72,8 | 72,8 | 72,8 | 146% |
| CO | P99 1 hora | 2015 | 4,84 | mg/m3N | 30 | 16% |
| CO | P99 1 hora | 2016 | 5,25 | 5,25 | 5,25 | 18% |
| CO | P99 1 hora | 2017 | 6,55 | 6,55 | 6,55 | 22% |
| CO | P99 1 hora | Mayor valor 2015-2017 | 6,55 | 6,55 | 6,55 | 22% |
| CO | P99 8 horas | 2015 | 3,45 | 3,45 | 10 | 35% |
| CO | P99 8 horas | 2016 | 3,38 | 3,38 | 3,38 | 34% |
| CO | P99 8 horas | 2017 | 4,55 | 4,55 | 4,55 | 46% |
| CO | P99 8 horas | Mayor valor 2015-2017 | 4,55 | 4,55 | 4,55 | 46% |
| SO2 | P99 24 horas | 2015 | 13,2 | μg/m3N | 250 | 5% |
| SO2 | P99 24 horas | 2016 | 13,3 | 13,3 | 13,3 | 5% |
| SO2 | P99 24 horas | 2017 | 11,6 | 11,6 | 11,6 | 5% |
| SO2 | P99 24 horas | Mayor valor 2015-2017 | 13,3 | 13,3 | 13,3 | 5% |
| SO2 | Promedio Anual | 2015 | 4,0 | 4,0 | 80 | 5% |
| SO2 | Promedio Anual | 2016 | 4,1 | 4,1 | 4,1 | 5% |
| SO2 | Promedio Anual | 2017 * | 4,8 | 4,8 | 4,8 | 6% |
| SO2 | Promedio Anual | Promedio 2015-2016 | 4,0 | 4,0 | 4,0 | 5% |

**Tabla 2-28: -Calidad del Aire Estación Rancagua II.****

| Contaminante | Estadígrafo | Periodo | Valor | Unidad | Valor<br>Norma | Porcentaje de la<br>Norma |
| --- | --- | --- | --- | --- | --- | --- |
| MP2,5 | P98 24 horas | 2015 | 97,0 | μg/m3 | 50 | 194% |
| MP2,5 | P98 24 horas | 2016 | 110,0 | 110,0 | 110,0 | 220% |
| MP2,5 | P98 24 horas | 2017 | 83,0 | 83,0 | 83,0 | 166% |
| MP2,5 | P98 24 horas | Mayor valor 2015-2017 | 110,0 | 110,0 | 110,0 | 220% |
| MP2,5 | Promedio Anual | 2015 | 33,5 | 33,5 | 20 | 168% |
| MP2,5 | Promedio Anual | 2016 | 31,0 | 31,0 | 31,0 | 155% |
| MP2,5 | Promedio Anual | 2017 | 25,9 | 25,9 | 25,9 | 129% |
| MP2,5 | Promedio Anual | Promedio 2015-2017 | 30,2 | 30,2 | 30,2 | 151% |
| MP10 | P98 24 horas | 2015 | 142,1 | μg/m3N | 150 | 95% |
| MP10 | P98 24 horas | 2016 | 157,6 | 157,6 | 157,6 | 105% |
| MP10 | P98 24 horas | 2017 | 109,0 | 109,0 | 109,0 | 73% |
| MP10 | P98 24 horas | Mayor valor 2015-2017 | 157,6 | 157,6 | 157,6 | 105% |
| MP10 | Promedio Anual | 2015 | 66,7 | 66,7 | 50 | 133% |
| MP10 | Promedio Anual | 2016 | 63,2 | 63,2 | 63,2 | 126% |
| MP10 | Promedio Anual | 2017 | 50,0 | 50,0 | 50,0 | 100% |
| MP10 | Promedio Anual | Promedio 2015-2017 | 60,0 | 60,0 | 60,0 | 120% |

**Tabla 2-29.: Características y Tasas de Emisión de Fuentes Puntuales. Escenario 1.****

| Fase | Fuente | Emisión [t/año] | Col4 | Col5 | Col6 | Col7 | Parámetros Fuentes Puntuales | Col9 | Col10 | Col11 | Tiempo | Tasa de Emisión [g/s] | Col14 | Col15 | Col16 | Col17 | Variabilidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **Fuente** | **MP2.5** | **MP10** | **CO** | **NO2 ** | **SO2 ** | **Altura**<br>**chimenea**<br>**[m]** | **Diámetro**<br>**interno**<br>**[m]** | **Velocidad**<br>**salida de**<br>**los gases**<br>**[m/s]** | **Temperatur**<br>**a de salida**<br>**de los gases**<br>**[°C]** | **s/año** | **MP2.5** | **MP10** | **CO** | **NO2 ** | **SO2 ** | **SO2 ** |
| Operación<br>Proyectada | Grupo<br>Electrógeno<br>Proyecto | 1,08 | 1,08 | 1,355 | 14,278 | 0,050 | 10 | 0,3047 | 58,5 | 416 | 3.952.800 | 2,742E-02 | 2,742E-02 | 3,427E-01 | 3,612E+00 | 1,258E-02 | Ciclo<br>Mensual-<br>Diurno, de<br>17:00 a<br>23:00 h y de<br>abril a<br>septiembre. |
| Operación<br>Proyectada | Caldera de<br>Biomasa | 0,956 | 0,956 | 4,350 | 13,867 | 12,327 | 18,5 | 1,2 | 12,75 | 280 | 31.536.000 | 3,031E-02 | 3,031E-02 | 1,379E-01 | 4,397E-01 | 3,909E-01 | - |
| Construcción<br>etapa 2 | Grupo<br>Electrógeno<br>IF | 0,034 | 0,034 | 0,104 | 0,482 | 0,032 | 1,6 | 0,075 | 73,56 | 495 | 7.488.000 | 4,586E-03 | 4,586E-03 | 1,390E-02 | 6,435E-02 | 4,278E-03 | Ciclo<br>Semanal-<br>Diurno |

**Tabla 2-30.: Características y Tasas de Emisión de Fuentes Lineales. Escenario 1.****

| Fase | Fuente | Tipo de<br>Fuente | Emisión [t/año] | Col5 | Col6 | Col7 | Col8 | Dimensiones Modelo | Col10 | Tiempo | Tasa de Emisión [g/m-s] | Col13 | Col14 | Col15 | Col16 | Variabilidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **Fuente** | **Tipo de**<br>**Fuente** | **MP2.5** | **MP10** | **CO** | **NO2 ** | **SO2 ** | **Valor** | **Unidad** | **s/año** | **MP2.5** | **MP10** | **CO** | **NO2 ** | **SO2 ** | **SO2 ** |
| Operación<br>Proyectada | Caminos<br>Pavimentados | Camino | 0,525 | 2,057 | 0,414 | 1,786 | 0,045 | 31.150 | [m] | 31.536.000 | 5,340E-07 | 2,094E-06 | 4,214E-07 | 1,818E-06 | 4,607E-08 | - |
| Construcción<br>etapa 2 | Caminos<br>Pavimentados<br>Construcción | Camino | 0,282 | 1,117 | 0,184 | 0,793 | 0,020 | 31.150 | [m] | 7.488.000 | 1,210E-06 | 4,789E-06 | 7,883E-07 | 3,401E-06 | 8,618E-08 | Ciclo<br>Semanal-<br>Diurno |

**Tabla 2-31.: Características y Tasas de Emisión de Fuentes Areales. Escenario 1.****

| Fase | Fuente | Emisión [t/año] | Col4 | Col5 | Col6 | Col7 | Dimensiones<br>Modelo | Col9 | Tiempo | Tasa de Emisión [g/m2-s] | Col12 | Col13 | Col14 | Col15 | Variabilidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **Fuente** | **MP2.5** | **MP10** | **CO** | **NO2 ** | **SO2 ** | **Valor** | **Unidad** | **s/año** | **MP2.5** | **MP10** | **CO** | **NO2 ** | **SO2 ** | **SO2 ** |
| Construcción<br>etapa 2 | Áreas Construcción<br>(Movimientos de Tierra) | 0,309 | 0,656 | - | - | - | 25.688 | [m2] | 7.488.000 | 1,608E-06 | 3,410E-06 | - | - | - | Ciclo Semanal-<br>Diurno |
| Construcción<br>etapa 2 | Áreas Construcción<br>(Maquinaria) | 0,598 | 0,598 | 1,906 | 6,143 | 0,000 | 25.688 | [m2] | 7.488.000 | 3,107E-06 | 3,107E-06 | 9,909E-06 | 3,194E-05 | 0,000E+00 | Ciclo Semanal-<br>Diurno |

**Tabla 2-32.: Características y Tasas de Emisión de Fuentes Puntuales. Escenario 2.****

| Fase | Fuente | Emisión [t/año] | Col4 | Col5 | Col6 | Col7 | Parámetros Fuentes Puntuales | Col9 | Col10 | Col11 | Tiempo | Tasa de Emisión [g/s] | Col14 | Col15 | Col16 | Col17 | Variabilidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **Fuente** | **MP2.5** | **MP10** | **CO** | **NO2 ** | **SO2 ** | **Altura**<br>**chimenea**<br>**[m]** | **Diámetro**<br>**interno**<br>**[m]** | **Velocidad**<br>**salida de**<br>**los gases**<br>**[m/s]** | **Temperatur**<br>**a de salida**<br>**de los gases**<br>**[°C]** | **s/año** | **MP2.5** | **MP10** | **CO** | **NO2 ** | **SO2 ** | **SO2 ** |
| Operación<br>Proyectada | Grupo<br>Electrógeno<br>Proyecto | 1,08 | 1,08 | 1,355 | 14,278 | 0,050 | 10 | 0,3047 | 58,5 | 416 | 3.952.800 | 2,742E-02 | 2,742E-02 | 3,427E-01 | 3,612E+00 | 1,258E-02 | Ciclo<br>Mensual-<br>Diurno, de<br>17:00 a<br>23:00 h y de<br>abril a<br>septiembre. |
| Operación<br>Proyectada | Caldera de<br>Biomasa | 0,956 | 0,956 | 4,350 | 13,867 | 12,327 | 18,5 | 1,2 | 12,75 | 280 | 31.536.000 | 3,031E-02 | 3,031E-02 | 1,379E-01 | 4,397E-01 | 3,909E-01 | - |

**Tabla 2-33.: Características y Tasas de Emisión de Fuentes Lineales. Escenario 2.****

| Fase | Fuente | Tipo de<br>Fuente | Emisión [t/año] | Col5 | Col6 | Col7 | Col8 | Dimensiones Modelo | Col10 | Tiempo | Tasa de Emisión [g/m-s] | Col13 | Col14 | Col15 | Col16 | Variabilidad |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Fase** | **Fuente** | **Tipo de**<br>**Fuente** | **MP2.5** | **MP10** | **CO** | **NO2 ** | **SO2 ** | **Valor** | **Unidad** | **s/año** | **MP2.5** | **MP10** | **CO** | **NO2 ** | **SO2 ** | **SO2 ** |
| Operación<br>Proyectada | Caminos<br>Pavimentados | Camino | 0,525 | 2,057 | 0,414 | 1,786 | 0,045 | 31.150 | [m] | 31.536.000 | 5,340E-07 | 2,094E-06 | 4,214E-07 | 1,818E-06 | 4,607E-08 | - |

**Tabla 2-34-: Receptores de Interés.****

| ID Receptor | Coordenadas | Col3 | Elevación | Descripción |
| --- | --- | --- | --- | --- |
| **ID Receptor** | **(Datum WGS84)** | **(Datum WGS84)** | **(Datum WGS84)** | **(Datum WGS84)** |
| **ID Receptor** | **Este** | **Norte** | **[msnm]** | **[msnm]** |
| **ID Receptor** | **[m]** | **[m]** | **[m]** | **[m]** |
| R_1 | 342.015 | 6.218.523 | 400,45 | Estación Rancagua I |
| R_2 | 339.842 | 6.220.527 | 484,06 | Estación Rancagua II |
| R_3 | 325.546 | 6.213.076 | 397,74 | Vivienda 1 |
| R_4 | 325.409 | 6.213.969 | 399,68 | Vivienda 2 |
| R_5 | 325.308 | 6.213.177 | 395,6 | Vivienda 3 |
| R_6 | 324.834 | 6.212.845 | 389,4 | Vivienda 4 |
| R_7 | 324.810 | 6.212.964 | 390,97 | Vivienda 5 |
| R_8 | 324.886 | 6.213.137 | 393,22 | Vivienda 6 |
| R_9 | 324.535 | 6.212.934 | 397,49 | Vivienda 7 |
| R_10 | 325.752 | 6.213.798 | 401,6 | Vivienda 8 |
| R_11 | 325.925 | 6.213.443 | 401,89 | Vivienda 9 |
| R_12 | 325.602 | 6.213.293 | 399,05 | Vivienda 10 |

**Tabla 2-35: - Resultados de modelo de dispersión de MP2.5. Escenario 1.****

| Receptor | Descripción | Coordenadas de Ubicación (Datum WGS84) | Col4 | Material Particulado Respirable Fino [MP2.5] | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Coordenadas de Ubicación (Datum WGS84)** | **Coordenadas de Ubicación (Datum WGS84)** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Este [m]** | **Norte [m]** | **Percentil 98 24**<br>**horas** | **Período Anual** | **Percentil 98 24**<br>**horas** | **Período Anual** | **Percentil 98 24**<br>**horas** | **Período Anual** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 0,00 | 0,00 | 50 | 20 | 0,01% | 0,01% |
| R_2 | Estación Rancagua II | 339.842 | 6.220.527 | 0,01 | 0,00 | 0,00 | 0,00 | 0,01% | 0,01% |
| R_3 | Vivienda 1 | 325.546 | 6.213.076 | 0,60 | 0,13 | 0,13 | 0,13 | 1,19% | 0,64% |
| R_4 | Vivienda 2 | 325.409 | 6.213.969 | 0,63 | 0,12 | 0,12 | 0,12 | 1,26% | 0,61% |
| R_5 | Vivienda 3 | 325.308 | 6.213.177 | 2,39 | 0,24 | 0,24 | 0,24 | 4,77% | 1,20% |
| R_6 | Vivienda 4 | 324.834 | 6.212.845 | 0,22 | 0,02 | 0,02 | 0,02 | 0,43% | 0,11% |
| R_7 | Vivienda 5 | 324.810 | 6.212.964 | 0,21 | 0,03 | 0,03 | 0,03 | 0,43% | 0,14% |
| R_8 | Vivienda 6 | 324.886 | 6.213.137 | 0,48 | 0,05 | 0,05 | 0,05 | 0,97% | 0,23% |
| R_9 | Vivienda 7 | 324.535 | 6.212.934 | 0,15 | 0,02 | 0,02 | 0,02 | 0,31% | 0,09% |
| R_10 | Vivienda 8 | 325.752 | 6.213.798 | 0,96 | 0,35 | 0,35 | 0,35 | 1,91% | 1,74% |
| R_11 | Vivienda 9 | 325.925 | 6.213.443 | 0,34 | 0,13 | 0,13 | 0,13 | 0,68% | 0,63% |
| R_12 | Vivienda 10 | 325.602 | 6.213.293 | 1,20 | 0,23 | 0,23 | 0,23 | 2,41% | 1,14% |

**Tabla 2-36: - Resultados de modelo de dispersión de MP10. Escenario 1.****

| Receptor | Descripción | Coordenadas de Ubicación (Datum WGS84) | Col4 | Material Particulado Respirable [MP10] | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Coordenadas de Ubicación (Datum WGS84)** | **Coordenadas de Ubicación (Datum WGS84)** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Este [m]** | **Norte [m]** | **Percentil 98 24**<br>**horas** | **Período Anual** | **Percentil 98 24**<br>**horas** | **Período Anual** | **Percentil 98 24**<br>**horas** | **Período Anual** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 0,02 | 0,01 | 150 | 50 | 0,01% | 0,01% |
| R_2 | Estación Rancagua II | 339.842 | 6.220.527 | 0,02 | 0,01 | 0,01 | 0,01 | 0,01% | 0,01% |
| R_3 | Vivienda 1 | 325.546 | 6.213.076 | 1,23 | 0,33 | 0,33 | 0,33 | 0,82% | 0,67% |
| R_4 | Vivienda 2 | 325.409 | 6.213.969 | 0,90 | 0,19 | 0,19 | 0,19 | 0,60% | 0,37% |
| R_5 | Vivienda 3 | 325.308 | 6.213.177 | 3,64 | 0,56 | 0,56 | 0,56 | 2,42% | 1,12% |
| R_6 | Vivienda 4 | 324.834 | 6.212.845 | 0,36 | 0,04 | 0,04 | 0,04 | 0,24% | 0,08% |
| R_7 | Vivienda 5 | 324.810 | 6.212.964 | 0,36 | 0,05 | 0,05 | 0,05 | 0,24% | 0,11% |
| R_8 | Vivienda 6 | 324.886 | 6.213.137 | 0,72 | 0,09 | 0,09 | 0,09 | 0,48% | 0,19% |
| R_9 | Vivienda 7 | 324.535 | 6.212.934 | 0,26 | 0,04 | 0,04 | 0,04 | 0,17% | 0,07% |
| R_10 | Vivienda 8 | 325.752 | 6.213.798 | 1,39 | 0,51 | 0,51 | 0,51 | 0,93% | 1,02% |
| R_11 | Vivienda 9 | 325.925 | 6.213.443 | 0,84 | 0,35 | 0,35 | 0,35 | 0,56% | 0,69% |
| R_12 | Vivienda 10 | 325.602 | 6.213.293 | 1,76 | 0,44 | 0,44 | 0,44 | 1,18% | 0,88% |

**Tabla 2-37: - Resultados de modelo de dispersión de CO. Escenario 1.****

| Receptor | Descripción | Coordenadas de Ubicación (Datum WGS84) | Col4 | Monóxido de Carbono (CO) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Coordenadas de Ubicación (Datum WGS84)** | **Coordenadas de Ubicación (Datum WGS84)** | **Concentración [mg/m3N] - Aporte**<br>**Proyecto** | **Concentración [mg/m3N] - Aporte**<br>**Proyecto** | **Concentración [mg/m3N] - Norma de**<br>**Calidad** | **Concentración [mg/m3N] - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Este [m]** | **Norte [m]** | **Percentil 99 1**<br>**hora** | **Percentil 99 8**<br>**horas** | **Percentil 99 1 hora** | **Percentil 99 8**<br>**horas** | **Percentil 99 1**<br>**hora** | **Percentil 99 8**<br>**horas** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 1,75E-04 | 3,57E-05 | 30 | 10 | 0,00% | 0,00% |
| R_2 | Estación Rancagua II | 339.842 | 6.220.527 | 1,79E-04 | 5,77E-05 | 5,77E-05 | 5,77E-05 | 0,00% | 0,00% |
| R_3 | Vivienda 1 | 325.546 | 6.213.076 | 3,10E-02 | 9,98E-03 | 9,98E-03 | 9,98E-03 | 0,10% | 0,10% |
| R_4 | Vivienda 2 | 325.409 | 6.213.969 | 2,36E-02 | 6,83E-03 | 6,83E-03 | 6,83E-03 | 0,08% | 0,07% |
| R_5 | Vivienda 3 | 325.308 | 6.213.177 | 6,47E-02 | 2,43E-02 | 2,43E-02 | 2,43E-02 | 0,22% | 0,24% |
| R_6 | Vivienda 4 | 324.834 | 6.212.845 | 7,83E-03 | 2,93E-03 | 2,93E-03 | 2,93E-03 | 0,03% | 0,03% |
| R_7 | Vivienda 5 | 324.810 | 6.212.964 | 9,83E-03 | 4,09E-03 | 4,09E-03 | 4,09E-03 | 0,03% | 0,04% |
| R_8 | Vivienda 6 | 324.886 | 6.213.137 | 2,13E-02 | 5,40E-03 | 5,40E-03 | 5,40E-03 | 0,07% | 0,05% |
| R_9 | Vivienda 7 | 324.535 | 6.212.934 | 9,22E-03 | 2,95E-03 | 2,95E-03 | 2,95E-03 | 0,03% | 0,03% |
| R_10 | Vivienda 8 | 325.752 | 6.213.798 | 4,15E-02 | 1,18E-02 | 1,18E-02 | 1,18E-02 | 0,14% | 0,12% |
| R_11 | Vivienda 9 | 325.925 | 6.213.443 | 1,25E-02 | 4,83E-03 | 4,83E-03 | 4,83E-03 | 0,04% | 0,05% |
| R_12 | Vivienda 10 | 325.602 | 6.213.293 | 7,51E-02 | 2,02E-02 | 2,02E-02 | 2,02E-02 | 0,25% | 0,20% |

**Tabla 2-38: - Resultados de modelo de dispersión de NO** **2** **. Escenario 1.****

| Receptor | Descripción | Coordenadas de Ubicación (Datum WGS84) | Col4 | Dióxido de Nitrógeno (NO)<br>2 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Coordenadas de Ubicación (Datum WGS84)** | **Coordenadas de Ubicación (Datum WGS84)** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Este [m]** | **Norte [m]** | **Percentil 99 1**<br>**hora** | **Período Anual** | **Percentil 99 1 hora** | **Período Anual** | **Percentil 99 1**<br>**hora** | **Período Anual** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 1,32 | 0,01 | 400 | 100 | 0,33% | 0,01% |
| R_2 | Estación Rancagua II | 339.842 | 6.220.527 | 1,48 | 0,02 | 0,02 | 0,02 | 0,37% | 0,02% |
| R_3 | Vivienda 1 | 325.546 | 6.213.076 | 124,99 | 0,76 | 0,76 | 0,76 | 31,25% | 0,76% |
| R_4 | Vivienda 2 | 325.409 | 6.213.969 | 110,62 | 1,01 | 1,01 | 1,01 | 27,66% | 1,01% |
| R_5 | Vivienda 3 | 325.308 | 6.213.177 | 212,82 | 1,49 | 1,49 | 1,49 | 53,21% | 1,49% |
| R_6 | Vivienda 4 | 324.834 | 6.212.845 | 66,54 | 0,30 | 0,30 | 0,30 | 16,64% | 0,30% |
| R_7 | Vivienda 5 | 324.810 | 6.212.964 | 50,07 | 0,31 | 0,31 | 0,31 | 12,52% | 0,31% |
| R_8 | Vivienda 6 | 324.886 | 6.213.137 | 68,89 | 0,38 | 0,38 | 0,38 | 17,22% | 0,38% |
| R_9 | Vivienda 7 | 324.535 | 6.212.934 | 40,36 | 0,21 | 0,21 | 0,21 | 10,09% | 0,21% |
| R_10 | Vivienda 8 | 325.752 | 6.213.798 | 141,42 | 3,32 | 3,32 | 3,32 | 35,36% | 3,32% |
| R_11 | Vivienda 9 | 325.925 | 6.213.443 | 121,07 | 0,90 | 0,90 | 0,90 | 30,27% | 0,90% |
| R_12 | Vivienda 10 | 325.602 | 6.213.293 | 240,37 | 1,75 | 1,75 | 1,75 | 60,09% | 1,75% |

**Tabla 2-39: - Resultados de modelo de dispersión de SO** **2** **. Escenario 1.****

| Receptor | Descripción | Coordenadas de Ubicación (Datum WGS84) | Col4 | Dióxido de Azufre (SO)<br>2 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Coordenadas de Ubicación (Datum WGS84)** | **Coordenadas de Ubicación (Datum WGS84)** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Este [m]** | **Norte [m]** | **Percentil 99 24**<br>**horas** | **Período Anual** | **Percentil 99 24**<br>**horas** | **Período Anual** | **Percentil 99 24**<br>**horas** | **Período Anual** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 1,48E-02 | 2,39E-03 | 250 | 80 | 0,01% | 0,00% |
| R_2 | Estación Rancagua II | 339.842 | 6.220.527 | 2,06E-02 | 3,59E-03 | 3,59E-03 | 3,59E-03 | 0,01% | 0,00% |
| R_3 | Vivienda 1 | 325.546 | 6.213.076 | 1,71E-01 | 3,02E-02 | 3,02E-02 | 3,02E-02 | 0,07% | 0,04% |
| R_4 | Vivienda 2 | 325.409 | 6.213.969 | 3,24E-01 | 7,28E-02 | 7,28E-02 | 7,28E-02 | 0,13% | 0,09% |
| R_5 | Vivienda 3 | 325.308 | 6.213.177 | 2,30E-01 | 3,96E-02 | 3,96E-02 | 3,96E-02 | 0,09% | 0,05% |
| R_6 | Vivienda 4 | 324.834 | 6.212.845 | 2,74E-01 | 3,25E-02 | 3,25E-02 | 3,25E-02 | 0,11% | 0,04% |
| R_7 | Vivienda 5 | 324.810 | 6.212.964 | 2,91E-01 | 3,49E-02 | 3,49E-02 | 3,49E-02 | 0,12% | 0,04% |
| R_8 | Vivienda 6 | 324.886 | 6.213.137 | 2,49E-01 | 3,64E-02 | 3,64E-02 | 3,64E-02 | 0,10% | 0,05% |
| R_9 | Vivienda 7 | 324.535 | 6.212.934 | 2,75E-01 | 3,27E-02 | 3,27E-02 | 3,27E-02 | 0,11% | 0,04% |
| R_10 | Vivienda 8 | 325.752 | 6.213.798 | 5,75E-01 | 2,13E-01 | 2,13E-01 | 2,13E-01 | 0,23% | 0,27% |
| R_11 | Vivienda 9 | 325.925 | 6.213.443 | 4,62E-01 | 7,24E-02 | 7,24E-02 | 7,24E-02 | 0,18% | 0,09% |
| R_12 | Vivienda 10 | 325.602 | 6.213.293 | 2,00E-01 | 3,50E-02 | 3,50E-02 | 3,50E-02 | 0,08% | 0,04% |

**Tabla 2-40: - Resultados de modelo de dispersión de MP2.5. Escenario 2.****

| Receptor | Descripción | Coordenadas de Ubicación (Datum WGS84) | Col4 | Material Particulado Respirable Fino [MP2.5] | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Coordenadas de Ubicación (Datum WGS84)** | **Coordenadas de Ubicación (Datum WGS84)** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Este [m]** | **Norte [m]** | **Percentil 98 24**<br>**horas** | **Período Anual** | **Percentil 98 24**<br>**horas** | **Período Anual** | **Percentil 98 24**<br>**horas** | **Período Anual** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 0,00 | 0,00 | 50 | 20 | 0,01% | 0,01% |
| R_2 | Estación Rancagua II | 339.842 | 6.220.527 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01% | 0,01% |
| R_3 | Vivienda 1 | 325.546 | 6.213.076 | 0,16 | 0,06 | 0,06 | 0,06 | 0,31% | 0,30% |
| R_4 | Vivienda 2 | 325.409 | 6.213.969 | 0,04 | 0,01 | 0,01 | 0,01 | 0,09% | 0,07% |
| R_5 | Vivienda 3 | 325.308 | 6.213.177 | 0,20 | 0,08 | 0,08 | 0,08 | 0,40% | 0,42% |
| R_6 | Vivienda 4 | 324.834 | 6.212.845 | 0,04 | 0,01 | 0,01 | 0,01 | 0,08% | 0,04% |
| R_7 | Vivienda 5 | 324.810 | 6.212.964 | 0,03 | 0,01 | 0,01 | 0,01 | 0,07% | 0,05% |
| R_8 | Vivienda 6 | 324.886 | 6.213.137 | 0,04 | 0,01 | 0,01 | 0,01 | 0,07% | 0,07% |
| R_9 | Vivienda 7 | 324.535 | 6.212.934 | 0,02 | 0,01 | 0,01 | 0,01 | 0,05% | 0,04% |
| R_10 | Vivienda 8 | 325.752 | 6.213.798 | 0,09 | 0,04 | 0,04 | 0,04 | 0,17% | 0,18% |
| R_11 | Vivienda 9 | 325.925 | 6.213.443 | 0,15 | 0,06 | 0,06 | 0,06 | 0,30% | 0,32% |
| R_12 | Vivienda 10 | 325.602 | 6.213.293 | 0,11 | 0,05 | 0,05 | 0,05 | 0,21% | 0,24% |

**Tabla 2-41: - Resultados de modelo de dispersión de MP10. Escenario 2.****

| Receptor | Descripción | Coordenadas de Ubicación (Datum WGS84) | Col4 | Material Particulado Respirable [MP10] | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Coordenadas de Ubicación (Datum WGS84)** | **Coordenadas de Ubicación (Datum WGS84)** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Este [m]** | **Norte [m]** | **Percentil 98 24**<br>**horas** | **Período Anual** | **Percentil 98 24**<br>**horas** | **Período Anual** | **Percentil 98 24**<br>**horas** | **Período Anual** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 0,01 | 0,00 | 150 | 50 | 0,01% | 0,01% |
| R_2 | Estación Rancagua II | 339.842 | 6.220.527 | 0,01 | 0,00 | 0,00 | 0,00 | 0,01% | 0,01% |
| R_3 | Vivienda 1 | 325.546 | 6.213.076 | 0,61 | 0,22 | 0,22 | 0,22 | 0,41% | 0,45% |
| R_4 | Vivienda 2 | 325.409 | 6.213.969 | 0,10 | 0,04 | 0,04 | 0,04 | 0,07% | 0,08% |
| R_5 | Vivienda 3 | 325.308 | 6.213.177 | 0,76 | 0,32 | 0,32 | 0,32 | 0,51% | 0,64% |
| R_6 | Vivienda 4 | 324.834 | 6.212.845 | 0,09 | 0,02 | 0,02 | 0,02 | 0,06% | 0,04% |
| R_7 | Vivienda 5 | 324.810 | 6.212.964 | 0,09 | 0,03 | 0,03 | 0,03 | 0,06% | 0,06% |
| R_8 | Vivienda 6 | 324.886 | 6.213.137 | 0,12 | 0,05 | 0,05 | 0,05 | 0,08% | 0,09% |
| R_9 | Vivienda 7 | 324.535 | 6.212.934 | 0,06 | 0,02 | 0,02 | 0,02 | 0,04% | 0,04% |
| R_10 | Vivienda 8 | 325.752 | 6.213.798 | 0,18 | 0,08 | 0,08 | 0,08 | 0,12% | 0,15% |
| R_11 | Vivienda 9 | 325.925 | 6.213.443 | 0,58 | 0,23 | 0,23 | 0,23 | 0,39% | 0,47% |
| R_12 | Vivienda 10 | 325.602 | 6.213.293 | 0,40 | 0,17 | 0,17 | 0,17 | 0,26% | 0,34% |

**Tabla 2-42: - Resultados de modelo de dispersión de CO. Escenario 2.****

| Receptor | Descripción | Coordenadas de Ubicación (Datum WGS84) | Col4 | Monóxido de Carbono (CO) | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Coordenadas de Ubicación (Datum WGS84)** | **Coordenadas de Ubicación (Datum WGS84)** | **Concentración [mg/m3N] - Aporte**<br>**Proyecto** | **Concentración [mg/m3N] - Aporte**<br>**Proyecto** | **Concentración [mg/m3N] - Norma de**<br>**Calidad** | **Concentración [mg/m3N] - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Este [m]** | **Norte [m]** | **Percentil 99 1**<br>**hora** | **Percentil 99 8**<br>**horas** | **Percentil 99 1 hora** | **Percentil 99 8**<br>**horas** | **Percentil 99 1**<br>**hora** | **Percentil 99 8**<br>**horas** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 1,45E-04 | 3,39E-05 | 30 | 10 | 0,00% | 0,00% |
| R_2 | Estación Rancagua II | 339.842 | 6.220.527 | 1,56E-04 | 5,18E-05 | 5,18E-05 | 5,18E-05 | 0,00% | 0,00% |
| R_3 | Vivienda 1 | 325.546 | 6.213.076 | 1,99E-03 | 8,05E-04 | 8,05E-04 | 8,05E-04 | 0,01% | 0,01% |
| R_4 | Vivienda 2 | 325.409 | 6.213.969 | 6,38E-03 | 1,67E-03 | 1,67E-03 | 1,67E-03 | 0,02% | 0,02% |
| R_5 | Vivienda 3 | 325.308 | 6.213.177 | 1,02E-02 | 2,48E-03 | 2,48E-03 | 2,48E-03 | 0,03% | 0,02% |
| R_6 | Vivienda 4 | 324.834 | 6.212.845 | 5,24E-03 | 2,06E-03 | 2,06E-03 | 2,06E-03 | 0,02% | 0,02% |
| R_7 | Vivienda 5 | 324.810 | 6.212.964 | 4,65E-03 | 1,65E-03 | 1,65E-03 | 1,65E-03 | 0,02% | 0,02% |
| R_8 | Vivienda 6 | 324.886 | 6.213.137 | 4,04E-03 | 1,25E-03 | 1,25E-03 | 1,25E-03 | 0,01% | 0,01% |
| R_9 | Vivienda 7 | 324.535 | 6.212.934 | 3,09E-03 | 1,13E-03 | 1,13E-03 | 1,13E-03 | 0,01% | 0,01% |
| R_10 | Vivienda 8 | 325.752 | 6.213.798 | 1,22E-02 | 4,45E-03 | 4,45E-03 | 4,45E-03 | 0,04% | 0,04% |
| R_11 | Vivienda 9 | 325.925 | 6.213.443 | 8,22E-03 | 2,15E-03 | 2,15E-03 | 2,15E-03 | 0,03% | 0,02% |
| R_12 | Vivienda 10 | 325.602 | 6.213.293 | 1,17E-02 | 3,70E-03 | 3,70E-03 | 3,70E-03 | 0,04% | 0,04% |

**Tabla 2-43: - Resultados de modelo de dispersión de NO** **2** **. Escenario 2.****

| Receptor | Descripción | Coordenadas de Ubicación (Datum WGS84) | Col4 | Dióxido de Nitrógeno (NO)<br>2 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Coordenadas de Ubicación (Datum WGS84)** | **Coordenadas de Ubicación (Datum WGS84)** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Este [m]** | **Norte [m]** | **Percentil 99 1**<br>**hora** | **Período Anual** | **Percentil 99 1 hora** | **Período Anual** | **Percentil 99 1**<br>**hora** | **Período Anual** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 1,32 | 0,01 | 400 | 100 | 0,33% | 0,01% |
| R_2 | Estación Rancagua II | 339.842 | 6.220.527 | 1,48 | 0,02 | 0,02 | 0,02 | 0,37% | 0,02% |
| R_3 | Vivienda 1 | 325.546 | 6.213.076 | 19,28 | 0,32 | 0,32 | 0,32 | 4,82% | 0,32% |
| R_4 | Vivienda 2 | 325.409 | 6.213.969 | 66,80 | 0,29 | 0,29 | 0,29 | 16,70% | 0,29% |
| R_5 | Vivienda 3 | 325.308 | 6.213.177 | 106,89 | 0,51 | 0,51 | 0,51 | 26,72% | 0,51% |
| R_6 | Vivienda 4 | 324.834 | 6.212.845 | 54,03 | 0,21 | 0,21 | 0,21 | 13,51% | 0,21% |
| R_7 | Vivienda 5 | 324.810 | 6.212.964 | 48,02 | 0,19 | 0,19 | 0,19 | 12,01% | 0,19% |
| R_8 | Vivienda 6 | 324.886 | 6.213.137 | 42,11 | 0,17 | 0,17 | 0,17 | 10,53% | 0,17% |
| R_9 | Vivienda 7 | 324.535 | 6.212.934 | 31,59 | 0,14 | 0,14 | 0,14 | 7,90% | 0,14% |
| R_10 | Vivienda 8 | 325.752 | 6.213.798 | 127,92 | 1,19 | 1,19 | 1,19 | 31,98% | 1,19% |
| R_11 | Vivienda 9 | 325.925 | 6.213.443 | 86,30 | 0,54 | 0,54 | 0,54 | 21,57% | 0,54% |
| R_12 | Vivienda 10 | 325.602 | 6.213.293 | 123,09 | 0,58 | 0,58 | 0,58 | 30,77% | 0,58% |

**Tabla 2-44: - Resultados de modelo de dispersión de SO** **2** **. Escenario 2.****

| Receptor | Descripción | Coordenadas de Ubicación (Datum WGS84) | Col4 | Dióxido de Azufre (SO)<br>2 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Coordenadas de Ubicación (Datum WGS84)** | **Coordenadas de Ubicación (Datum WGS84)** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Aporte**<br>**Proyecto** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Concentración [μg/m3N] - Norma de**<br>**Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **Este [m]** | **Norte [m]** | **Percentil 99 24**<br>**horas** | **Período Anual** | **Percentil 99 24**<br>**horas** | **Período Anual** | **Percentil 99 24**<br>**horas** | **Período Anual** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 1,47E-02 | 2,37E-03 | 250 | 80 | 0,01% | 0,00% |
| R_2 | Estación Rancagua II | 339.842 | 6.220.527 | 2,06E-02 | 3,57E-03 | 3,57E-03 | 3,57E-03 | 0,01% | 0,00% |
| R_3 | Vivienda 1 | 325.546 | 6.213.076 | 1,65E-01 | 2,85E-02 | 2,85E-02 | 2,85E-02 | 0,07% | 0,04% |
| R_4 | Vivienda 2 | 325.409 | 6.213.969 | 3,19E-01 | 6,97E-02 | 6,97E-02 | 6,97E-02 | 0,13% | 0,09% |
| R_5 | Vivienda 3 | 325.308 | 6.213.177 | 2,27E-01 | 3,55E-02 | 3,55E-02 | 3,55E-02 | 0,09% | 0,04% |
| R_6 | Vivienda 4 | 324.834 | 6.212.845 | 2,74E-01 | 3,21E-02 | 3,21E-02 | 3,21E-02 | 0,11% | 0,04% |
| R_7 | Vivienda 5 | 324.810 | 6.212.964 | 2,91E-01 | 3,42E-02 | 3,42E-02 | 3,42E-02 | 0,12% | 0,04% |
| R_8 | Vivienda 6 | 324.886 | 6.213.137 | 2,48E-01 | 3,56E-02 | 3,56E-02 | 3,56E-02 | 0,10% | 0,04% |
| R_9 | Vivienda 7 | 324.535 | 6.212.934 | 2,75E-01 | 3,24E-02 | 3,24E-02 | 3,24E-02 | 0,11% | 0,04% |
| R_10 | Vivienda 8 | 325.752 | 6.213.798 | 5,70E-01 | 2,06E-01 | 2,06E-01 | 2,06E-01 | 0,23% | 0,26% |
| R_11 | Vivienda 9 | 325.925 | 6.213.443 | 4,59E-01 | 7,02E-02 | 7,02E-02 | 7,02E-02 | 0,18% | 0,09% |
| R_12 | Vivienda 10 | 325.602 | 6.213.293 | 1,99E-01 | 3,18E-02 | 3,18E-02 | 3,18E-02 | 0,08% | 0,04% |

**Tabla 2-45.: Concentración total esperada. Material Particulado Respirable Fino (MP2.5). Escenario 1.****

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación (Datum<br>WGS84) | Col4 | Material Particulado Respirable Fino (MP2.5) | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación (Datum**<br>**WGS84)** | **Coordenadas de**<br>**Ubicación (Datum**<br>**WGS84)** | **Concentración**<br>**(μg/m3N) - Línea de**<br>**Base** | **Concentración**<br>**(μg/m3N) - Línea de**<br>**Base** | **Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración Total**<br>**Esperada (μg/m3N)** | **Concentración Total**<br>**Esperada (μg/m3N)** | **Norma de Calidad**<br>**(μg/m3N)** | **Norma de Calidad**<br>**(μg/m3N)** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 88,90 | 24,10 | 0,00 | 0,00 | 88,90 | 24,10 | 50 | 20 | 178% | 121% |
| R_2 | Estación Rancagua II | 339.842 | 6.220.527 | 110,00 | 30,20 | 0,01 | 0,00 | 110,01 | 30,20 | 30,20 | 30,20 | 220% | 151% |

**Tabla 2-46.: Concentración total esperada. Material Particulado Respirable (MP10). Escenario 1.****

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Material Particulado Respirable (MP10) | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración**<br>**(μg/m3N) - Línea de**<br>**Base** | **Concentración**<br>**(μg/m3N) - Línea de**<br>**Base** | **Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración Total**<br>**Esperada (μg/m3N)** | **Concentración Total**<br>**Esperada (μg/m3N)** | **Norma de Calidad**<br>**(μg/m3N)** | **Norma de Calidad**<br>**(μg/m3N)** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 181,70 | 72,80 | 0,02 | 0,01 | 181,72 | 72,81 | 150 | 50 | 121% | 146% |
| R_2 | Estación Rancagua II | 339.842 | 6.220.527 | 157,60 | 60,00 | 0,02 | 0,01 | 157,62 | 60,01 | 60,01 | 60,01 | 105% | 120% |

**Tabla 2-47.: Concentración total esperada. Monóxido de Carbono (CO). Escenario 1.****

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Monóxido de Carbono (CO) | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración (mg/m3N)**<br>**- Línea de Base** | **Concentración (mg/m3N)**<br>**- Línea de Base** | **Concentración (mg/m3N)**<br>**- Aporte del Proyecto** | **Concentración (mg/m3N)**<br>**- Aporte del Proyecto** | **Concentración Total**<br>**Esperada (mg/m3N)** | **Concentración Total**<br>**Esperada (mg/m3N)** | **Norma de Calidad**<br>**(mg/m3N)** | **Norma de Calidad**<br>**(mg/m3N)** | **Porcentaje de la**<br>**Norma de Calidad** | **Porcentaje de la**<br>**Norma de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil**<br>**99 1 hora** | **Percentil 99**<br>**8 horas** | **Percentil**<br>**99 1 hora** | **Percentil 99**<br>**8 horas** | **Percentil**<br>**99 1 hora** | **Percentil**<br>**99 8 horas** | **Percentil**<br>**99 1 hora** | **Percentil**<br>**99 8 horas** | **Percentil**<br>**99 1 hora** | **Percentil**<br>**99 8**<br>**horas** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 6,55 | 4,55 | 1,75E-04 | 3,57E-05 | 6,55 | 4,55 | 30 | 10 | 22% | 46% |

**Tabla 2-48.: Concentración total esperada. Dióxido de Azufre (SO** **2** **). Escenario 1.****

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Dióxido de Azufre (SO)<br>2 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración**<br>**(μg/m3N) - Línea de**<br>**Base** | **Concentración**<br>**(μg/m3N) - Línea de**<br>**Base** | **Concentración (μg/m3N) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3N) -**<br>**Aporte del Proyecto** | **Concentración Total**<br>**Esperada (μg/m3N)** | **Concentración Total**<br>**Esperada (μg/m3N)** | **Norma de Calidad**<br>**(μg/m3N)** | **Norma de Calidad**<br>**(μg/m3N)** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil**<br>**99 24**<br>**horas** | **Período**<br>**Anual** | **Percentil 99**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 99**<br>**24 horas** | **Período**<br>**Anual** | **Percentil**<br>**99 24**<br>**horas** | **Período**<br>**Anual** | **Percentil 99**<br>**24 horas** | **Período**<br>**Anual** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 13,30 | 4,00 | 1,48E-02 | 2,39E-03 | 13,31 | 4,00 | 250 | 80 | 5% | 5% |

**Tabla 2-49.: Concentración total esperada. Material Particulado Respirable Fino (MP2.5). Escenario 2.****

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación (Datum<br>WGS84) | Col4 | Material Particulado Respirable Fino (MP2.5) | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación (Datum**<br>**WGS84)** | **Coordenadas de**<br>**Ubicación (Datum**<br>**WGS84)** | **Concentración**<br>**(μg/m3N) - Línea de**<br>**Base** | **Concentración**<br>**(μg/m3N) - Línea de**<br>**Base** | **Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración Total**<br>**Esperada (μg/m3N)** | **Concentración Total**<br>**Esperada (μg/m3N)** | **Norma de Calidad**<br>**(μg/m3N)** | **Norma de Calidad**<br>**(μg/m3N)** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 88,90 | 24,10 | 0,00 | 0,00 | 88,90 | 24,10 | 50 | 20 | 178% | 121% |
| R_2 | Estación Rancagua II | 339.842 | 6.220.527 | 110,00 | 30,20 | 0,00 | 0,00 | 110,00 | 30,20 | 30,20 | 30,20 | 220% | 151% |

**Tabla 2-50.: Concentración total esperada. Material Particulado Respirable (MP10). Escenario 2.****

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Material Particulado Respirable (MP10) | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración**<br>**(μg/m3N) - Línea de**<br>**Base** | **Concentración**<br>**(μg/m3N) - Línea de**<br>**Base** | **Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración**<br>**(μg/m3N) - Aporte del**<br>**Proyecto** | **Concentración Total**<br>**Esperada (μg/m3N)** | **Concentración Total**<br>**Esperada (μg/m3N)** | **Norma de Calidad**<br>**(μg/m3N)** | **Norma de Calidad**<br>**(μg/m3N)** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil**<br>**98 24**<br>**horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 98**<br>**24 horas** | **Período**<br>**Anual** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 181,70 | 72,80 | 0,01 | 0,00 | 181,71 | 72,80 | 150 | 50 | 121% | 146% |
| R_2 | Estación Rancagua II | 339.842 | 6.220.527 | 157,60 | 60,00 | 0,01 | 0,00 | 157,61 | 60,00 | 60,00 | 60,00 | 105% | 120% |

**Tabla 2-51.: Concentración total esperada. Monóxido de Carbono (CO). Escenario 2.****

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Monóxido de Carbono (CO) | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración (mg/m3N)**<br>**- Línea de Base** | **Concentración (mg/m3N)**<br>**- Línea de Base** | **Concentración (mg/m3N)**<br>**- Aporte del Proyecto** | **Concentración (mg/m3N)**<br>**- Aporte del Proyecto** | **Concentración Total**<br>**Esperada (mg/m3N)** | **Concentración Total**<br>**Esperada (mg/m3N)** | **Norma de Calidad**<br>**(mg/m3N)** | **Norma de Calidad**<br>**(mg/m3N)** | **Porcentaje de la**<br>**Norma de Calidad** | **Porcentaje de la**<br>**Norma de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil**<br>**99 1 hora** | **Percentil 99**<br>**8 horas** | **Percentil**<br>**99 1 hora** | **Percentil 99**<br>**8 horas** | **Percentil**<br>**99 1 hora** | **Percentil**<br>**99 8 horas** | **Percentil**<br>**99 1 hora** | **Percentil**<br>**99 8 horas** | **Percentil**<br>**99 1 hora** | **Percentil**<br>**99 8**<br>**horas** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 6,55 | 4,55 | 1,45E-04 | 3,39E-05 | 6,55 | 4,55 | 30 | 10 | 4% | 9% |

**Tabla 2-52.: Concentración total esperada. Dióxido de Azufre (SO** **2** **). Escenario 2.****

| ID<br>Receptor | Descripción | Coordenadas de<br>Ubicación<br>(Datum WGS84) | Col4 | Dióxido de Azufre (SO)<br>2 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 | Col14 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID**<br>**Receptor** | **Descripción** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Coordenadas de**<br>**Ubicación**<br>** (Datum WGS84)** | **Concentración**<br>**(μg/m3N) - Línea de**<br>**Base** | **Concentración**<br>**(μg/m3N) - Línea de**<br>**Base** | **Concentración (μg/m3N) -**<br>**Aporte del Proyecto** | **Concentración (μg/m3N) -**<br>**Aporte del Proyecto** | **Concentración Total**<br>**Esperada (μg/m3N)** | **Concentración Total**<br>**Esperada (μg/m3N)** | **Norma de Calidad**<br>**(μg/m3N)** | **Norma de Calidad**<br>**(μg/m3N)** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **ID**<br>**Receptor** | **Descripción** | **Este (m)** | **Norte (m)** | **Percentil**<br>**99 24**<br>**horas** | **Período**<br>**Anual** | **Percentil 99**<br>**24 horas** | **Período**<br>**Anual** | **Percentil 99**<br>**24 horas** | **Período**<br>**Anual** | **Percentil**<br>**99 24**<br>**horas** | **Período**<br>**Anual** | **Percentil 99**<br>**24 horas** | **Período**<br>**Anual** |
| R_1 | Estación Rancagua I | 342.015 | 6.218.523 | 13,30 | 4,00 | 1,47E-02 | 2,37E-03 | 13,31 | 4,00 | 250 | 80 | 5% | 5% |
