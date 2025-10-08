---
title: Sin título
author: Asesorías del Favero y Meneses
date: D:20240124194723-03'00'
language: es
type: report
pages: 234
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Proyecto “Optimización Operacional Mina Carola”
-->

## Modelación de Dispersión de Contaminantes

# Proyecto “Optimización Operacional Mina Carola”

## Enero 2024

**PREPARADO PARA**

Grupo Minero Carola-COEMIN

|REVISIONES|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|No REV.|ELABORADO POR|REVISADO POR|FECHA|FIRMA RESPONSABLE|
|Rev. 1|María Soledad<br>Landaeta Toloza|Benjamín del Favero<br>Tocornal|24-01-2024||
|Rev. 1|Ingeniera Ambiental,<br>USACH.|Ingeniero Civil de Industrias<br>con Mención en Ingeniería<br>Ambiental, PUC.|Ingeniero Civil de Industrias<br>con Mención en Ingeniería<br>Ambiental, PUC.|Ingeniero Civil de Industrias<br>con Mención en Ingeniería<br>Ambiental, PUC.|

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**ÍNDICE**

1 INTRODUCCIÓN .......................................................................................................... 1

2 OBJETIVOS ................................................................................................................... 3

2.1 Objetivo General ......................................................................................................... 3

2.2 Objetivos Específicos .................................................................................................. 3

3 METODOLOGÍA ........................................................................................................... 4

4 RESUMEN INVENTARIO DE EMISIONES ATMOSFÉRICAS ............................................ 7

5 MODELO DE CALIDAD DEL AIRE .................................................................................. 8

5.1 Tipo de Modelo de Calidad del Aire Seleccionado ..................................................... 8

5.2 Descripción del Modelo de Calidad del Aire Seleccionado - CALPUFF ....................... 8

5.3 Descripción del Modelo Meteorológico Seleccionado - WRF .................................... 9

5.3.1 Selección del Año de Modelación ............................................................................. 11

5.4 Características del Modelo de Dispersión de Contaminantes .................................. 12

5.4.1 Dominio de la Modelación ........................................................................................ 12

5.4.2 Topografía del Sector ................................................................................................ 14

5.4.3 Uso de Suelos ............................................................................................................ 16

5.5 Caracterización Meteorológica del área del Proyecto ............................................. 18

5.5.1 Meteorología de Superficie- Valores Observados .................................................... 18

5.5.2 Meteorología de Superficie- Valores Modelados ..................................................... 48

5.5.3 Meteorología de Altura - Valores Observados ........................................................ 61

5.5.4 Meteorología de Altura - Valores Modelados ......................................................... 61

5.6 Análisis de Incertidumbre ......................................................................................... 65

5.6.1 Estación Meteorológica Tierra Amarilla ................................................................... 65

5.7 Normativa de Calidad del Aire y Valores de Referencia ........................................... 73

5.8 Línea de Base de Calidad del Aire ............................................................................. 74

5.8.1 Línea de Base Medida ............................................................................................... 74

www.dfmconsultores.cl

i

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.8.2 Línea de Base Proyectada ......................................................................................... 79

5.9 Escenarios Modelados .............................................................................................. 83

5.9.1 Fase de Operación Base ............................................................................................ 83

5.9.2 Fase de Operación Proyectada ............................................................................... 113

5.10 Análisis de Significancia de Operación del Proyecto .............................................. 143

6 ÁREA DE INFLUENCIA .............................................................................................. 147

6.1 Área de Influencia Base .......................................................................................... 149

6.2 Área de Influencia Proyectada ................................................................................ 151

7 EFECTO SINÉRGICO PROYECTO “OPTIMIZACIÓN OPERACIONAL MINA CAROLA” . 153

7.1 Fuentes Emisoras Escenario Sinérgico .................................................................... 153

7.2 Receptores de Interés Escenario Sinérgico ............................................................ 160

7.3 Resultados Modelación Escenario Sinérgico Fase de Operación Base ................... 164

7.3.1 Material Particulado Respirable Fino (MP2.5) ....................................................... 165

7.3.2 Material Particulado Respirable (MP10) ................................................................ 169

7.3.3 Material Particulado Sedimentable (MPS) ............................................................. 173

7.3.4 Monóxido de Carbono (CO) .................................................................................... 177

7.3.5 Dióxido de Nitrógeno (NO 2 ) .................................................................................... 179

7.3.6 Dióxido de Azufre (SO 2 ) .......................................................................................... 183

7.4 Resultados Modelación Escenario Sinérgico Fase de Operación Proyectada ........ 186

7.4.1 Material Particulado Respirable Fino (MP2.5) ....................................................... 187

7.4.2 Material Particulado Respirable (MP10) ................................................................ 191

7.4.3 Material Particulado Sedimentable (MPS) ............................................................. 195

7.4.4 Monóxido de Carbono (CO) .................................................................................... 199

7.4.5 Dióxido de Nitrógeno (NO 2 ) .................................................................................... 201

7.4.6 Dióxido de Azufre (SO 2 ) .......................................................................................... 205

7.5 Análisis de Significancia del Escenario Sinérgico .................................................... 208

www.dfmconsultores.cl

ii

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

7.6 Concentración Total Proyectada ............................................................................ 212

8 CONCLUSIONES ....................................................................................................... 217

www.dfmconsultores.cl

iii

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**ÍNDICE TABLAS**

Tabla 4-1. Resumen Emisiones. Fase de Operación Base. ..................................................... 7

Tabla 4-2. Resumen Emisiones. Fase de Operación Proyectada. ........................................... 7

Tabla 5-1. Configuración parámetros principales modelo meteorológico WRF. ................. 10

Tabla 5-2. Estadígrafos de y MP10. Periodo 2020- 2022. Estación Tierra Amarilla. ............ 12

Tabla 5-3. Caracterización Estación de Monitoreo Meteorológico. .................................... 18

Tabla 5-4. Resumen de información Velocidad del Viento. Estación Tierra Amarilla. ......... 20

Tabla 5-5. Frecuencia de distribución Velocidad y Dirección del Viento. Periodo enero 2021

a diciembre de 2022. Estación Tierra Amarilla. .................................................................... 23

Tabla 5-6. Resumen de información Temperatura. Estación Tierra Amarilla. ..................... 29

Tabla 5-7. Resumen de información Humedad Relativa. Estación Tierra Amarilla.............. 33

Tabla 5-8. Resumen de información Precipitaciones Acumuladas. Estación Tierra Amarilla.

.............................................................................................................................................. 37

Tabla 5-9. Resumen de información Radiación Solar. Estación Tierra Amarilla. ................. 40

Tabla 5-10. Resumen de Información Presión Atmosférica. Estación Tierra Amarilla. ....... 44

Tabla 5-11. Resumen de información Velocidad del Viento Modelada. Estación Tierra

Amarilla. ................................................................................................................................ 48

Tabla 5-12. Frecuencia de distribución Velocidad y Dirección del Viento Modelada. Enero a

diciembre de 2021. Estación Tierra Amarilla. ...................................................................... 51

Tabla 5-13. Resumen de información Temperatura Modelada. Estación Tierra Amarilla. .. 57

Tabla 5-14. Resumen de Información Altura de Capa de Mezcla Modelada. Estación Tierra

Amarilla. ................................................................................................................................ 61

Tabla 5-15. Comparación Registros de Velocidad del Viento y Temperatura Observadas y

Modeladas. Enero a diciembre de 2021. Estación Tierra Amarilla. ..................................... 71

Tabla 5-16. Estadígrafos de Dispersión de Velocidad del Viento y Temperatura. Estación

Tierra Amarilla. ..................................................................................................................... 71

Tabla 5-17. Estadígrafos de Dispersión de Velocidad del Viento y Temperatura. Estación

Tierra Amarilla. ..................................................................................................................... 72

www.dfmconsultores.cl

iv

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Tabla 5-18. Normas de Calidad del Aire. .............................................................................. 73

Tabla 5-19. Caracterización de Estación de Monitoreo de Calidad del Aire. ....................... 75

Tabla 5-20. Resumen Línea de Base de Calidad del Aire. ..................................................... 77

Tabla 5-21. Análisis de otros proyectos dentro del dominio de modelación. ..................... 80

Tabla 5-22. Línea de Base de Calidad del Aire Proyectada................................................... 82

Tabla 5-23. Características de Fuentes Emisoras y Tasas de Emisión. Fase de Operación

Base....................................................................................................................................... 85

Tabla 5-24. Receptores de Interés. Fase de Operación Base. ............................................. 87

Tabla 5-25. Resultados del modelo de dispersión para MP2.5 [μg/m [3] ]. Fase de Operación

Base....................................................................................................................................... 92

Tabla 5-26. Resultados del modelo de dispersión para MP10 [μg/m [3] N]. Fase de Operación

Base....................................................................................................................................... 96

Tabla 5-27. Resultados del modelo de dispersión para MPS [mg/m [2∙] día]. Fase de Operación

Base..................................................................................................................................... 100

Tabla 5-28. Resultados del modelo de dispersión para CO [mg/m [3] N]. Fase de Operación

Base..................................................................................................................................... 104

Tabla 5-29. Resultados del modelo de dispersión para NO 2 [μg/m [3] N]. Fase de Operación

Base..................................................................................................................................... 106

Tabla 5-30. Resultados del modelo de dispersión para SO 2 [μg/m [3] N]. Fase de Operación

Base..................................................................................................................................... 110

Tabla 5-31. Características de Fuentes Emisoras y Tasas de Emisión. Fase de Operación

Proyectada. ......................................................................................................................... 115

Tabla 5-32. Receptores de Interés. Fase de Operación Proyectada. ................................ 117

Tabla 5-33. Resultados del modelo de dispersión para MP2.5 [μg/m [3] ]. Fase de Operación

Proyectada. ......................................................................................................................... 122

Tabla 5-34. Resultados del modelo de dispersión para MP10 [μg/m [3] N]. Fase de Operación

Proyectada. ......................................................................................................................... 126

Tabla 5-35. Resultados del modelo de dispersión para MPS [mg/m [2] ∙día]. Fase de Operación

Proyectada. ......................................................................................................................... 130

www.dfmconsultores.cl

v

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Tabla 5-36. Resultados del modelo de dispersión para CO [mg/m [3] N]. Fase de Operación

Proyectada. ......................................................................................................................... 134

Tabla 5-37. Resultados del modelo de dispersión para NO 2 [μg/m [3] N]. Fase de Operación

Proyectada. ......................................................................................................................... 136

Tabla 5-38. Resultados del modelo de dispersión para SO 2 [μg/m [3] N]. Fase de Operación

Proyectada. ......................................................................................................................... 140

Tabla 5-39. Análisis de Significancia Fase de Operación. MP10 [μg/m [3] N]......................... 143

Tabla 6-1. Valores de significancia para la evaluación de impacto significativo en un

escenario de riesgo preexistente. ...................................................................................... 148

Tabla 7-1. Características de Fuentes Emisoras y Tasas de Emisión. Escenario Sinérgico Fase

de Operación Base. ............................................................................................................. 155

Tabla 7-2. Características de Fuentes Emisoras y Tasas de Emisión. Escenario Sinérgico Fase

de Operación Proyectado. .................................................................................................. 157

Tabla 7-3. Receptores de Interés. Escenario Sinérgico Fase de Operación. ..................... 160

Tabla 7-4. Resultados del modelo de dispersión para MP2.5 [μg/m [3] ]. Escenario Sinérgico

Fase de Operación Base...................................................................................................... 165

Tabla 7-5. Resultados del modelo de dispersión para MP10 [μg/m [3] N]. Escenario Sinérgico

Fase de Operación Base...................................................................................................... 169

Tabla 7-6. Resultados del modelo de dispersión para MPS [mg/m [2∙] día]. Escenario Sinérgico

Fase de Operación Base...................................................................................................... 173

Tabla 7-7. Resultados del modelo de dispersión para CO [mg/m [3] N]. Escenario Sinérgico Fase

de Operación Base. ............................................................................................................. 177

Tabla 7-8. Resultados del modelo de dispersión para NO 2 [μg/m [3] N]. Escenario Sinérgico Fase

de Operación Base. ............................................................................................................. 179

Tabla 7-9. Resultados del modelo de dispersión para SO 2 [μg/m [3] N]. Escenario Sinérgico Fase

de Operación Base. ............................................................................................................. 183

Tabla 7-10. Resultados del modelo de dispersión para MP2.5 [μg/m [3] ]. Escenario Sinérgico

Fase de Operación Proyectada. .......................................................................................... 187

www.dfmconsultores.cl

vi

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Tabla 7-11. Resultados del modelo de dispersión para MP10 [μg/m [3] N]. Escenario Sinérgico

Fase de Operación Proyectada. .......................................................................................... 191

Tabla 7-12. Resultados del modelo de dispersión para MPS [mg/m [2∙] día]. Escenario Sinérgico

Fase de Operación Proyectada. .......................................................................................... 195

Tabla 7-13. Resultados del modelo de dispersión para CO [mg/m [3] N]. Escenario Sinérgico

Fase de Operación Proyectada. .......................................................................................... 199

Tabla 7-14. Resultados del modelo de dispersión para NO 2 [μg/m [3] N]. Escenario Sinérgico

Fase de Operación Proyectada. .......................................................................................... 201

Tabla 7-15. Resultados del modelo de dispersión para SO 2 [μg/m [3] N]. Escenario Sinérgico

Fase de Operación Proyectada. .......................................................................................... 205

Tabla 7-16. Análisis de Significancia Fase de Operación Sinérgica. MP10 [μg/m [3] N]. ........ 208

Tabla 7-17. Concentración/ Depositación Total Sinérgica Proyectada. Estación Tierra

Amarilla. .............................................................................................................................. 212

Tabla 7-18. Concentración Total Sinérgica Proyectada. Estación Luis Uribe. .................... 213

Tabla 7-19. Concentración Total Sinérgica Proyectada. Estación Kozan. .......................... 213

Tabla 7-20. Concentración Total Sinérgica Proyectada. Estación Ojanco. ......................... 213

Tabla 7-21. Concentración Total Sinérgica Proyectada. Estación COEMIN. ...................... 213

Tabla 7-22. Concentración Total Sinérgica Proyectada. Estación Nantoco. ...................... 214

Tabla 7-23. Concentración Total Sinérgica Proyectada. Estación C5. ................................ 214

Tabla 7-24. Concentración Total Sinérgica Proyectada. Estación C6. ................................ 214

Tabla 7-25. Concentración Total Sinérgica Proyectada. Estación C8. ................................ 214

Tabla 7-26. Concentración Total Sinérgica Proyectada. Estación C2. ................................ 214

Tabla 7-27. Concentración Total Sinérgica Proyectada. Estación C1. ................................ 215

Tabla 7-28. Concentración Total Sinérgica Proyectada. Estación C3. ................................ 215

Tabla 7-29. Concentración Total Sinérgica Proyectada. Estación C7. ................................ 215

Tabla 8-1. Archivos de modelación entregados. ................................................................ 220

www.dfmconsultores.cl

vii

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**ÍNDICE FIGURAS**

Figura 3-1. Diagrama Metodología de Trabajo. ..................................................................... 6

Figura 5-1. Dominio de Modelación. .................................................................................... 13

Figura 5-2. Topografía del Dominio de Modelación. ............................................................ 15

Figura 5-3. Uso de Suelos del Dominio de Modelación. ....................................................... 17

Figura 5-4. Ubicación Referencial Estación de Monitoreo Meteorológico. ........................ 19

Figura 5-5. Serie de Tiempo Velocidad del Viento. Periodo enero 2021 a diciembre de 2022.

Estación Tierra Amarilla. ....................................................................................................... 21

Figura 5-6. Serie de Tiempo Dirección del Viento Periodo enero 2021 a diciembre de 2022.

Estación Tierra Amarilla. ....................................................................................................... 22

Figura 5-7. Ciclo Diario Velocidad del Viento. Periodo enero 2021 a diciembre de 2022.

Estación Tierra Amarilla. ....................................................................................................... 24

Figura 5-8. Ciclo Diario Dirección del Viento. Periodo enero 2021 a diciembre de 2022.

Estación Tierra Amarilla. ....................................................................................................... 26

Figura 5-9. Rosas de Vientos. Periodo de 0 a 8 horas, 8 a 16 horas y 16 a 0 horas. Periodo

enero 2021 a diciembre de 2022. Estación Tierra Amarilla. ................................................ 27

Figura 5-10. Ciclo Estacional Vientos. Periodo enero 2021 a diciembre de 2022. Estación

Tierra Amarilla. ..................................................................................................................... 28

Figura 5-11. Serie de Tiempo Temperatura. Periodo enero 2021 a diciembre de 2022.

Estación Tierra Amarilla. ....................................................................................................... 30

Figura 5-12. Ciclo Diario Temperatura. Periodo enero 2021 a diciembre de 2022. Estación

Tierra Amarilla. ..................................................................................................................... 31

Figura 5-13. Ciclo Estacional Temperatura. Periodo enero 2021 a diciembre de 2022.

Estación Tierra Amarilla. ....................................................................................................... 32

Figura 5-14. Serie de Tiempo Humedad Relativa. Periodo enero 2021 a diciembre de 2022.

Estación Tierra Amarilla. ....................................................................................................... 34

Figura 5-15. Ciclo Diario Humedad Relativa. Periodo enero 2021 a diciembre de 2022.

Estación Tierra Amarilla. ....................................................................................................... 35

www.dfmconsultores.cl

viii

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Figura 5-16. Ciclo Estacional Humedad Relativa. Periodo enero 2021 a diciembre de 2022.

Estación Tierra Amarilla. ....................................................................................................... 36

Figura 5-17. Serie de Tiempo Precipitación Acumulada Diaria. Periodo enero 2021 a

diciembre de 2022. Estación Tierra Amarilla. ...................................................................... 38

Figura 5-18. Serie de Tiempo Precipitación Acumulada Mensual. Periodo enero 2021 a

diciembre de 2022. Estación Tierra Amarilla. ...................................................................... 39

Figura 5-19. Serie de Tiempo Radiación Solar. Periodo enero 2021 a diciembre de 2022.

Estación Tierra Amarilla. ....................................................................................................... 41

Figura 5-20. Ciclo Diario Radiación Solar. Periodo enero 2021 a diciembre de 2022. Estación

Tierra Amarilla. ..................................................................................................................... 42

Figura 5-21. Ciclo Estacional Radiación Solar. Periodo enero 2021 a diciembre de 2022.

Estación Tierra Amarilla. ....................................................................................................... 43

Figura 5-22. Serie de Tiempo Presión Atmosférica. Periodo enero 2021 a diciembre de 2022.

Estación Tierra Amarilla. ....................................................................................................... 45

Figura 5-23. Ciclo Diario Presión Atmosférica. Periodo enero 2021 a diciembre de 2022.

Estación Tierra Amarilla. ....................................................................................................... 46

Figura 5-24. Ciclo Estacional Presión Atmosférica. Periodo enero 2021 a diciembre de 2022.

Estación Tierra Amarilla. ....................................................................................................... 47

Figura 5-25. Serie de Tiempo Velocidad del Viento Modelada. Enero a diciembre de 2021.

Estación Tierra Amarilla. ....................................................................................................... 49

Figura 5-26. Serie de Tiempo Dirección del Viento Modelada. Enero a diciembre de 2021.

Estación Tierra Amarilla. ....................................................................................................... 50

Figura 5-27. Ciclo Diario Velocidad del Viento Modelada. Enero a diciembre de 2021.

Estación Tierra Amarilla. ....................................................................................................... 52

Figura 5-28. Ciclo Diario Dirección del Viento Modelada. Enero a diciembre de 2021.

Estación Tierra Amarilla. ....................................................................................................... 54

Figura 5-29. Rosas de Vientos Modelados. Periodo de 0 a 8 horas, 8 a 16 horas y 16 a 0

horas. Enero a diciembre de 2021. Estación Tierra Amarilla. .............................................. 55

Figura 5-30. Ciclo Estacional de Velocidad y Dirección del Viento Observado. Enero a

diciembre de 2021. Estación Tierra Amarilla. ...................................................................... 56

www.dfmconsultores.cl

ix

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Figura 5-31. Serie de Tiempo Temperatura Modelada. Enero a diciembre de 2021. Estación

Tierra Amarilla. ..................................................................................................................... 58

Figura 5-32. Ciclo Diario Temperatura Modelada. Enero a diciembre de 2021. Estación Tierra

Amarilla. ................................................................................................................................ 59

Figura 5-33. Ciclo Estacional Temperatura Modelada. Enero a diciembre de 2021. Estación

Tierra Amarilla. ..................................................................................................................... 60

Figura 5-34. Serie de tiempo para Altura de Capa de Mezcla. Enero a diciembre de 2021.

Estación Tierra Amarilla. ....................................................................................................... 62

Figura 5-35. Ciclo diario para Altura de Capa de Mezcla. Enero a diciembre de 2021. Estación

Tierra Amarilla. ..................................................................................................................... 63

Figura 5-36. Ciclo estacional Altura Capa de Mezcla Modelada. Enero a diciembre de 2021.

Estación Tierra Amarilla. ....................................................................................................... 64

Figura 5-37. Comparación de Ciclos Diarios de Velocidad del Viento. Enero a diciembre de

2021. Estación Tierra Amarilla. ............................................................................................. 66

Figura 5-38. Comparación de Ciclos Diarios de Dirección del Viento. Enero a diciembre de

2021. Estación Tierra Amarilla. ............................................................................................. 67

Figura 5-39. Comparación de Ciclos Estacionales de Velocidad y Dirección del Viento. Enero

a diciembre de 2021. Estación Tierra Amarilla. .................................................................... 68

Figura 5-40. Comparación de Ciclos Diarios de Temperatura. Enero a diciembre de 2021.

Estación Tierra Amarilla. ....................................................................................................... 69

Figura 5-41. Comparación de Ciclos Estacionales de Temperatura. Enero a diciembre de

2021. Estación Tierra Amarilla. ............................................................................................. 70

Figura 5-42. Ubicación Referencial Estaciones de Monitoreo de Calidad del Aire. ............. 76

Figura 5-43. Ubicación Fuentes Emisoras. Fase de Operación Base. ................................... 84

Figura 5-44. Ubicación Grilla de Receptores. Fase de Operación Base. ............................... 89

Figura 5-45. Ubicación de Receptores de Interés. Fase de Operación Base. ....................... 90

Figura 5-46. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP2.5 [μg/m [3] ].

Fase de Operación Base........................................................................................................ 94

www.dfmconsultores.cl

x

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Figura 5-47. Curvas de isoconcentración para periodo anual. MP2.5 [μg/m [3] ]. Fase de

Operación Base. .................................................................................................................... 95

Figura 5-48. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP10

[μg/m [3] N]. Fase de Operación Base. ..................................................................................... 98

Figura 5-49. Curvas de isoconcentración para periodo anual. MP10 [μg/m [3] N]. Fase de

Operación Base. .................................................................................................................... 99

Figura 5-50. Curvas de isodepositación para periodo mensual. MPS [mg/m [2] ∙día]. Fase de

Operación Base. .................................................................................................................. 102

Figura 5-51. Curvas de isodepositación para periodo anual. MPS [mg/m [2] ∙día]. Fase de

Operación Base. .................................................................................................................. 103

Figura 5-52. Curvas de isoconcentración para percentil 99 periodo 1 hora. NO 2 [μg/m [3] N].

Fase de Operación Base...................................................................................................... 108

Figura 5-53. Curvas de isoconcentración para periodo anual. NO 2 [μg/m [3] N]. Fase de

Operación Base. .................................................................................................................. 109

Figura 5-54. Ubicación Fuentes Emisoras. Fase de Operación Proyectada. ...................... 114

Figura 5-55. Ubicación Grilla de Receptores. Fase de Operación Proyectada. .................. 119

Figura 5-56. Ubicación de Receptores de Interés. Fase de Operación Proyectada. .......... 120

Figura 5-57. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP2.5 [μg/m [3] ].

Fase de Operación Proyectada. .......................................................................................... 124

Figura 5-58. Curvas de isoconcentración para periodo anual. MP2.5 [μg/m [3] ]. Fase de

Operación Proyectada. ....................................................................................................... 125

Figura 5-59. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP10 [μg/m [3] ].

Fase de Operación Proyectada. .......................................................................................... 128

Figura 5-60. Curvas de isoconcentración para periodo anual. MP10 [μg/m [3] N]. Fase de

Operación Proyectada. ....................................................................................................... 129

Figura 5-61. Curvas de isodepositación para periodo mensual. MPS [mg/m [2] ∙día]. Fase de

Operación Proyectada. ....................................................................................................... 132

Figura 5-62. Curvas de isodepositación para periodo anual. MPS [mg/m [2] ∙día]. Fase de

Operación Proyectada. ....................................................................................................... 133

www.dfmconsultores.cl

xi

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Figura 5-63. Curvas de isoconcentración para percentil 99 periodo 1 hora. NO 2 [μg/m [3] N].

Fase de Operación Proyectada. .......................................................................................... 138

Figura 5-64. Curvas de isoconcentración para periodo anual. NO 2 [μg/m [3] N]. Fase de

Operación Proyectada. ....................................................................................................... 139

Figura 6-1. Área de Influencia del Proyecto para Normas Primarias de Calidad de Aire. Fase

de Operación Base. ............................................................................................................. 150

Figura 6-2. Área de Influencia del Proyecto para Normas Primarias de Calidad de Aire. Fase

de Operación Proyectada. .................................................................................................. 152

Figura 7-1. Ubicación Fuentes Emisoras. Escenario Sinérgico Fase de Operación. ........... 154

Figura 7-2. Ubicación Grilla de Receptores. Escenario Sinérgico Fase de Operación. ....... 162

Figura 7-3. Ubicación de Receptores de Interés. Escenario Sinérgico Fase de Operación. 163

Figura 7-4. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP2.5 [μg/m [3] ].

Escenario Sinérgico Fase de Operación Base. .................................................................... 167

Figura 7-5. Curvas de isoconcentración para periodo anual. MP2.5 [μg/m [3] ]. Escenario

Sinérgico Fase de Operación Base. ..................................................................................... 168

Figura 7-6. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP10 [μg/m [3] N].

Escenario Sinérgico Fase de Operación Base. .................................................................... 171

Figura 7-7. Curvas de isoconcentración para periodo anual. MP10 [μg/m [3] N]. Escenario

Sinérgico Fase de Operación Base. ..................................................................................... 172

Figura 7-8. Curvas de isodepositación para periodo mensual. MPS [mg/m [2] ∙día]. Escenario

Sinérgico Fase de Operación Base. ..................................................................................... 175

Figura 7-9. Curvas de isodepositación para periodo anual. MPS [mg/m [2] ∙día]. Escenario

Sinérgico Fase de Operación Base. ..................................................................................... 176

Figura 7-10. Curvas de isoconcentración para percentil 99 periodo 1 hora. NO 2 [μg/m [3] N].

Escenario Sinérgico Fase de Operación Base. .................................................................... 181

Figura 7-11. Curvas de isoconcentración para periodo anual. NO 2 (μg/m [3] N). Escenario

Sinérgico Fase de Operación Base. ..................................................................................... 182

Figura 7-12. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP2.5 [μg/m [3] ].

Escenario Sinérgico Fase de Operación Proyectada........................................................... 189

www.dfmconsultores.cl

xii

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Figura 7-13. Curvas de isoconcentración para periodo anual. MP2.5 [μg/m [3] ]. Escenario

Sinérgico Fase de Operación Proyectada. .......................................................................... 190

Figura 7-14. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP10

[μg/m [3] N]. Escenario Sinérgico Fase de Operación Proyectada. ........................................ 193

Figura 7-15. Curvas de isoconcentración para periodo anual. MP10 [μg/m [3] N]. Escenario

Sinérgico Fase de Operación Proyectada. .......................................................................... 194

Figura 7-16. Curvas de isodepositación para periodo mensual. MPS [mg/m [2] ∙día]. Escenario

Sinérgico Fase de Operación Proyectada. .......................................................................... 197

Figura 7-17. Curvas de isodepositación para periodo anual. MPS [mg/m [2] ∙día]. Escenario

Sinérgico Fase de Operación Proyectada. .......................................................................... 198

Figura 7-18. Curvas de isoconcentración para percentil 99 periodo 1 hora. NO 2 [μg/m [3] N].

Escenario Sinérgico Fase de Operación Proyectada........................................................... 203

Figura 7-19. Curvas de isoconcentración para periodo anual. NO 2 [μg/m [3] N]. Escenario

Sinérgico Fase de Operación Proyectada. .......................................................................... 204

www.dfmconsultores.cl

xiii

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

### 1 INTRODUCCIÓN

El presente informe contiene la modelación de dispersión de contaminantes atmosféricos

correspondientes al Proyecto “Optimización Operacional Mina Carola”, en adelante “el

Proyecto”, ubicado en la comuna de Tierra Amarilla, Región de Atacama; conforme a los

requerimientos establecidos en la Ley 19.300 de Bases Generales del Medio Ambiente, sus

modificaciones a través de la Ley N°20.417 y el Reglamento del Sistema de Evaluación de

Impacto Ambiental (SEIA) D.S. N°40/2012 en relación a los requisitos mínimos y criterios

para el ingreso de una modificación de un proyecto calificado ambientalmente de manera

favorable con anterioridad en el SEIA.

El Proyecto consiste en el aumento del ritmo de extracción de mineral desde la faena

subterránea de Mina Carola, con el objeto de incrementar la producción actual de 240.000

[t/mes], aprobada mediante la Resolución de Calificación Ambiental (RCA) N°108/2018, en

hasta 264.000 [t/mes].

De acuerdo con lo establecido en el Reglamento del SEIA, en el siguiente documento se

presenta la descripción del tipo de modelo de calidad del aire seleccionado, definiendo las

principales características del dominio de modelación, además de la caracterización

meteorológica del área del Proyecto a partir de los registros de monitoreo de la estación

Tierra Amarilla, la cual dispone información sobre las variables de velocidad y dirección del

viento, temperatura, humedad relativa, precipitación acumulada, radiación solar y presión

atmosférica.

De igual manera, se presentan los resultados de la modelación meteorológica de superficie

tras la utilización del software _Weather Research and Forecasting Model_ (WRF) para la

misma ubicación de la estación de monitoreo Tierra Amarilla, considerando las variables de

velocidad y dirección del viento, así como también de temperatura. Mientras que, para la

caracterización de la meteorología de altura, se presentan los resultados del modelo para

la variable altura capa de mezcla.

Tras ello, conforme a los lineamientos establecidos en la “Guía para el Uso de Modelos de

Calidad el Aire en el SEIA” del Servicio de Evaluación Ambiental (SEA), se realiza un análisis

de incertidumbre cualitativo y cuantitativo con el objeto de comparar la información

meteorológica observada y modelada, estableciendo la validez del modelo meteorológico

utilizado.

www.dfmconsultores.cl

1

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Posteriormente, a modo de determinar el estado actual de la calidad del aire en la zona de

emplazamiento del Proyecto, se presenta la línea de base para esta componente ambiental,

analizando los resultados de monitoreo de las estaciones Tierra Amarilla, Ojanco, Luis Uribe,

Kozan, COEMIN, Nantoco, C5, C6, C8, C2, C1, C3 y C7, en conjunto a las normativas

nacionales e internacionales de calidad del aire aplicables a los contaminantes medidos.

Además, se presenta una línea de base de calidad del aire proyectada, considerando

aquellos proyectos aprobados por el SEIA que, hasta la fecha de elaboración del presente

documento, aún no han iniciado su etapa de construcción.

Luego, se muestran los escenarios de modelación conforme a lo presentado en el Anexo 2
1.2 “Estimación de Emisiones Atmosféricas Proyecto Optimización Mina Carola”, así como

también los receptores de interés, los cuales corresponden a los puntos en donde se

evaluará el aporte especifico del Proyecto para cada uno de los contaminantes modelados.

De esta manera, los efectos del Proyecto se estiman a partir de los resultados de las

modelaciones realizadas para las fases de operación actual y proyectada, identificando los

aportes de concentración y depositación sobre los receptores de interés causados por

aquellas fuentes del Proyecto que presentan una modificación en su nivel de actividad entre

el escenario actual y futuro, obteniendo así la variación de los aportes totales mediante la

diferencia entre ambos escenarios.

Finalmente, se presentan las principales conclusiones del estudio.

www.dfmconsultores.cl

2

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

### 2 OBJETIVOS

#### 2.1 Objetivo General

Presentar la modelación de dispersión de contaminantes atmosféricos asociados a las fases

de operación actual y proyectada del Proyecto "Optimización Operacional Mina Carola”

conforme a lo establecido en la Ley 19.300 de Bases Generales del Medio Ambiente, sus

modificaciones a través de la Ley N°20.417 y el Reglamento del SEIA D.S. N°40/2012.

#### 2.2 Objetivos Específicos

 - Definir un dominio de modelación acorde a la magnitud del Proyecto y la capacidad

potencial que tengan los contaminantes a dispersar en la atmósfera, así como

también a los receptores de interés.

 - Presentar la caracterización de la meteorología de la zona de emplazamiento del

Proyecto a partir de los registros de monitoreo de la estación Tierra Amarilla y del

modelo meteorológico WRF para las mismas coordenadas.

 - Establecer la validez del modelo meteorológico WRF por medio de un análisis de

incertidumbre y utilizarlo como dato de entrada en la modelación de dispersión de

contaminantes en el software CALPUFF.

 - Identificar las principales fuentes de emisión asociadas al Proyecto y

georreferenciarlas dentro del dominio de modelación.

 - Modelar la dispersión de los contaminantes atmosféricos mediante el software

CALPUFF para ambos escenarios en estudio.

 - Establecer los aportes totales actuales del Proyecto sobre la concentración y

depositación de contaminantes atmosféricos en cada receptor de interés, valores ya

reflejados en la línea de base de calidad del aire conformada, y los aportes totales

proyectados causados por la modificación de los niveles de actividad de éste, para

luego representarlas dentro del dominio de modelación mediante curvas de

isoconcentración e isodepositación para cada contaminante según corresponda.

 - Establecer las áreas de influencias del Proyecto, tanto actuales como proyectadas,

respecto a la componente calidad del aire.

www.dfmconsultores.cl

3

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

### 3 METODOLOGÍA

En el siguiente apartado, se describen los pasos que definen la metodología utilizada para

la elaboración de la modelación de dispersión de contaminantes del Proyecto.

 - _Estimación de emisiones y fuentes de emisión:_ a partir de los resultados del

inventario de emisiones (Ver Anexo 2-1.2), se definen las fuentes de emisión y

emisiones asociadas a cada una de ellas, las cuales son georreferenciadas dentro del

dominio de modelación. Cabe señalar que, para la estimación de los efectos del

Proyecto sobre la línea de base de calidad del aire, la cual ya refleja la fase de

operación actual de éste, se han considerado solamente aquellas fuentes cuya tasa

de emisión se ven modificadas durante la fase de operación futura para la

conformación del modelo de dispersión.

 - _Receptores discretos:_ se definen los receptores de interés dentro del dominio de

modelación con el fin de evaluar el aporte de la concentración y depositación de

contaminantes atmosféricos sobre cada uno de estos, tales como estaciones de

monitoreo, viviendas, etc.

 - _Caracterización meteorológica:_ se realiza una caracterización de las variables

meteorológicas relevantes a partir del registro de monitoreo de una estación

cercana al emplazamiento del Proyecto.

 - _Modelo meteorológico Weather Research and Forecasting (WRF):_ se modela la

meteorología de un año calendario, para posteriormente utilizar dicho modelo en la

modelación de dispersión de contaminantes atmosféricos.

 - _Análisis de Incertidumbre:_ se realiza una comparación cuantitativa y cualitativa de

los datos meteorológicos observados y modelados para una misma locación, a modo

de determinar la incertidumbre del modelo meteorológico WRF y establecer su

validez como dato de entrada al modelo de dispersión atmosférico.

 - _Topografía:_ se obtienen los datos de topografía del dominio de modelación a partir

de Shuttle Radar Topography (SRTM1), cuya resolución es aproximadamente de 30

metros. Estos datos son parámetros relevantes de entrada en cuanto al relieve del

dominio de modelación.

www.dfmconsultores.cl

4

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

 - _Uso de suelos:_ se obtienen los datos de uso de suelos de la zona a partir de los

archivos Global Land Cover Characterization (GLCC) publicados por el US Geological

Survey (USGS). Estos datos son parámetros relevantes de entrada para que el

modelo posea la información acerca de los diversos tipos de uso de suelos presente

dentro del dominio de modelación.

 - _Modelación de dispersión de contaminantes atmosféricos (CALPUFF):_ a partir de los

principales datos de entrada del modelo, tales como fuentes de emisión, receptores

discretos, datos meteorológicos, topografía y uso de suelos, se realiza la modelación

de dispersión de contaminantes utilizando el software CALPUFF, a modo de

determinar la dispersión de los siguientes contaminantes: material particulado

respirable fino (MP2.5), material particulado respirable (MP10), material

particulado sedimentable (MPS), dióxido de nitrógeno (NO 2 ), dióxido de azufre (SO 2 )

y monóxido de carbono (CO).

 - _Análisis de resultados:_ a partir de los resultados de la modelación, se presentan los

aportes del Proyecto en cuanto a la concentración y depositación de los

contaminantes modelados para cada uno de los receptores discretos identificados.

Además, se presentan las curvas de isoconcentración e isodepositación dentro del

dominio de modelación, así como también las áreas de influencias del Proyecto para

la componente de calidad del aire.

 - _Conclusiones:_ se presentan las principales conclusiones del estudio realizado.

De esta manera, conforme a cada uno de los pasos señalados anteriormente, en la siguiente

figura se muestra un mapa conceptual con los principales ejes de la metodología de trabajo

descrita.

www.dfmconsultores.cl

5

**info@dfmconsultores.cl**

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 3-1. Diagrama Metodología de Trabajo.**

Fuente: Elaboración propia.

6

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

### 4 RESUMEN INVENTARIO DE EMISIONES ATMOSFÉRICAS

A continuación, en la Tabla 4-1 y Tabla 4-2 se presentan las emisiones por modelar

correspondientes al desarrollo de la fase de operación actual y proyectada del Proyecto

respectivamente, considerando un periodo de ejecución anual.

Es necesario mencionar que, a modo conservador, se han descartado aquellas obras y

actividades que no presentan una variación de sus emisiones entre el escenario actual y

proyectado, particularmente las emisiones asociadas a la combustión por el uso de grupos

electrógenos y a los movimientos de tierra asociados al botadero Cobriza, ubicado en el

sector Carola Sur.

**Tabla 4-1. Resumen Emisiones. Fase de Operación Base.**

|Actividad|Resumen de Emisiones [t]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Actividad**|**MP2.5**|**MP10**|**MP30**|**CO**|**NOX **|**COV**|**SOx **|**NH3 **|
|Combustión Maquinaria|1,270|1,270|1,270|16,871|19,809|2,012|0,051|0,013|
|Combustión Transporte|0,035|0,035|0,035|0,328|1,185|0,062|0,001|0,001|
|Resuspensión Transporte|0,605|5,154|17,128||||||
|Movimientos de Material|12,364|22,784|96,530||||||
|**Total**|**14,274**|**29,242**|**114,962**|**17,199**|**20,994**|**2,074**|**0,052**|**0,014**|

Fuente: Elaboración propia.

**Tabla 4-2. Resumen Emisiones. Fase de Operación Proyectada.**

|Actividad|Resumen de Emisiones [t]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Actividad**|**MP2.5**|**MP10**|**MP30**|**CO**|**NOX **|**COV**|**SOx **|**NH3 **|
|Combustión Maquinaria|1,397|1,397|1,397|18,558|21,790|2,213|0,056|0,015|
|Combustión Transporte|0,035|0,035|0,035|0,330|1,193|0,062|0,001|0,001|
|Resuspensión Transporte|0,294|2,149|7,770||||||
|Movimientos de Material|13,601|25,061|106,181||||||
|**Total**|**15,327**|**28,642**|**115,383**|**18,888**|**22,983**|**2,275**|**0,057**|**0,015**|

Fuente: Elaboración propia.

www.dfmconsultores.cl

7

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

### 5 MODELO DE CALIDAD DEL AIRE

En la siguiente sección, se presenta la información relevante respecto del modelo de calidad

del aire utilizado.

#### 5.1 Tipo de Modelo de Calidad del Aire Seleccionado

Los principales factores por considerar para la selección de un modelo corresponden al tipo

de terreno presente en el área del Proyecto, es decir, si es plano o complejo, y el tipo de

contaminante a emitir, si es primario o secundario.

De acuerdo con lo recomendado en la “Guía para el Uso de Modelos de Calidad del Aire en

el SEIA”, en el área de emplazamiento del Proyecto existen factores que podrían perturbar

el carácter lineal de los vientos, por lo anterior, es necesario utilizar un modelo que permita

simular meteorología heterogénea. En consecuencia, se ha seleccionado un modelo tipo

“ _puff_ ” para la ejecución de la modelación de calidad del aire.

A continuación, se presenta el detalle del modelo tipo “ _puff_ ” a utilizar.

#### 5.2 Descripción del Modelo de Calidad del Aire Seleccionado - CALPUFF

Como se indicó anteriormente, el entorno del área del Proyecto presenta sectores de

topografía compleja, los cuales podrían interferir en el carácter lineal de los vientos. Es por

ello por lo que, se ha seleccionado el modelo de calidad del aire correspondiente al software

CALPUFF, modelo de libre disposición desarrollado por _Research Corporation_, siendo

_Exponent_ [1] la empresa de su soporte técnico actual.

Este programa consiste en un modelo de dispersión de contaminantes, no estacionario,

multicapa, capaz de modelar múltiples especies, pudiendo simular los efectos del tiempo y

en el espacio de las diversas condiciones meteorológicas en el transporte de contaminantes.

Además, corresponde a un modelo de tipo Lagrangiano-Gaussiano de transporte y

dispersión de “ _puff_ ” emitidos por las fuentes emisoras consideradas.

Dentro de las capacidades del modelo de calidad del aire, se pueden destacar los siguientes

aspectos:

1 [Enlace web: www.src.com/calpuff/calpuff1.htm](http://www.src.com/calpuff/calpuff1.htm)

www.dfmconsultores.cl

8

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

 - Simulación de procesos complejos: fumigación, estancamiento y recirculación.

 - Modelación de transporte de contaminantes de largo alcance.

 - Incorporación de efectos de terreno complejo en la dispersión de contaminantes.

 - Modelación de procesos de transformaciones químicas.

Adicionalmente, CALPUFF posee un módulo para realizar un procesamiento de datos

posterior a su ejecución, denominado CALPOST, el cual calcula el aporte de las

concentraciones y depositaciones de contaminantes emitidas por las fuentes emisoras

ingresadas en los receptores de interés, permitiendo gestionar los datos para cada

contaminante según el período de tiempo requerido para el análisis.

Cabe señalar que, ante los altos valores de emisión de óxidos de nitrógeno (NO X ) estimados

para ambos escenarios del Proyecto y considerando las capacidades del software

mencionadas con anterioridad, el presente estudio ha incluido la transformación química

de gases tales como NO X y SO X por medio del mecanismo RIVAD, el que en conjunto con el

modelo de equilibrio de gas-partícula inorgánica ISORROPIA, permite la conversión de

emisiones de NO y NO 2 a HNO 3 y NO 3, así como también de SO 2 a SO 4 .

Por tanto, con tal de un adecuado funcionamiento del modelo, aquellas emisiones de NO X

han sido distribuidas previamente considerando una relación entre NO 2 y NO X equivalente

a 1:10, mientras que, las emisiones de NO se han estimado por medio de la ponderación

entre el peso molecular del compuesto y las emisiones totales de NO X .

#### 5.3 Descripción del Modelo Meteorológico Seleccionado - WRF

_Weather Research and Forecasting_ _Model_ (WRF) es un sistema de modelación atmosférico

de mesoescala ampliamente usado a nivel mundial en contextos de investigación y de

pronósticos operacionales. En Chile, es el modelo numérico recomendado para la

generación de datos meteorológicos según lo indicado en la Guía para el Uso de Modelos

de Calidad del Aire en el SEIA (SEA, 2023).

El modelo utiliza una grilla tridimensional para representar la atmósfera y sus procesos tales

como radiación atmosférica, capa superficial, capa límite y procesos de formación de nubes

y precipitaciones, entre otros, en distintas escalas espaciales, las cuales pueden variar desde

decenas de metros hasta miles de kilómetros. Asimismo, utiliza información de topografía,

usos de suelo y meteorología observada o modelada proveniente de modelos

www.dfmconsultores.cl

9

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

meteorológicos globales para definir las condiciones iniciales y de borde para la simulación

de pronósticos meteorológicos.

A continuación, se describen las fuentes de información suministradas y su respectivo

tratamiento.

 - _Topografía del dominio de modelación:_ se ha utilizado la información topográfica de

alta resolución proveniente del modelo _Shuttle Radar Topography Mission (SRTM1)_,

cuya resolución es de aproximadamente 30 metros.

 - _Uso de suelo:_ se ha utilizado la información de usos de suelo de alta resolución

proveniente del modelo _Copernicus Global Land Saervice: Land Cover_ 100 m, cuya

resolución es de 100 metros.

 - _Meteorología proveniente de un modelo meteorológico global:_ se han utilizado los

resultados del modelo ERA 5 año 2021, el cual corresponde a estimaciones horarias

de una gran cantidad de variables climáticas atmosféricas, terrestres y oceánicas.

Los datos cubren la Tierra en una grilla de aproximadamente 30 kilómetros de

resolución y resuelven la atmosfera hasta una altura de 80 kilómetros.

A continuación, en la Tabla 5-1 se presentan los principales parámetros utilizados para la

configuración del modelo meteorológico, los cuales fueron seleccionados por su capacidad

de adaptación a la compleja topografía y a modelos de alta resolución (< 3 km). La

configuración del modelo se presenta en el Anexo 1. Archivos Digitales de Modelación.

**Tabla 5-1. Configuración parámetros principales modelo meteorológico WRF.**

|Parámetro|Col2|Valor|
|---|---|---|
|Dominio|Resolución horizontal|1 km|
|Dominio|Proyección|Lambert|
|Dominio|Dimensión|76x76x44|
|Dominio|Número de niveles verticales|44|
|Dominio|Niveles verticales (eta)|0.000000, 0.051578, 0.101822, 0.150735, 0.198315,<br>0.244562, 0.289477, 0.333059, 0.375309, 0.416226,<br>0.455810, 0.494062, 0.530982, 0.566569, 0.600823,<br>0.633745, 0.665334, 0.695591, 0.724515, 0.752107,<br>0.778366, 0.803292, 0.826886, 0.849148, 0.870076,<br>0.889673, 0.907937, 0.923302, 0.937101, 0.949333,<br>0.960000, 0.969101, 0.976635, 0.982603, 0.987005,<br>0.989841, 0.991111, 0.992381, 0.993651, 0.994921,<br>0.996190, 0.997460, 0.998730, 1.000000,|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

10

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Parámetro|Col2|Valor|
|---|---|---|
|Física|Esquema de radiación|RRTMG-fast (Onda corta y larga)|
|Física|Modelo de suelo|Modelo Noah Land Surface|
|Física|Tratamiento de capa superficial|Revised MM5 surface layer|
|Física|Parametrización de capa límite|Yonsei University|
|Física|Esquema de convección|Kain-Fritsch|
|Física|Microfísica de nubes y precipitación|WSM 3-class|
|Dinámica|Parametrización de turbulencia|Smagorinsky|
|Dinámica|Núcleo dinámico|EM (Advanced Mass) y No hidroestático|
|Dinámica|Advección|positiva-definitiva|

Fuente: Elaboración propia.

5.3.1 Selección del Año de Modelación

Para la selección del año de modelación, se han considerado los registros públicos de

monitoreo de calidad del aire para el periodo comprendido entre enero de 2020 y diciembre

de 2022 de las estaciones circundantes al área del Proyecto, particularmente de las

estaciones Tierra Amarilla, Ojanco, Luis Uribe, Kozan, COEMIN, Nantoco, C5, C6, C8, C2, C1,

C3 y C7.

Tal información ha sido recopilada por medio del Sistema Nacional de Información de

Fiscalización Ambiental, específicamente a través de los informes de monitoreo de las

unidades fiscalizables Compañía Contractual Minera Candelaria, Sociedad Contractual

Minera Atacama Kozan y Compañía Exploradora y Explotadora de Minas Chileno-rumana

(COEMIN).

Sin embargo, tras considerar la periodicidad de muestreo de las estaciones señaladas, se

han descartado las estaciones Ojanco, Luis Uribe, Kozan y COEMIN, las que presentan

registros de monitoreo cada 3 días, así como también las estaciones Nantoco, C5, C6, C8,

C2, C1, C3 y C7, las cuales presentan información de manera trimestral.

De este modo, la selección del año a modelar se ha basado en los registros de monitoreo

de material particulado MP10 de la estación Tierra Amarilla, la cual presenta un registro

continuo de las concentraciones medidas, siendo así un indicador más fidedigno de las

condiciones de dispersión de contaminantes en comparación con aquellas mediciones de

carácter discreto, pues estas últimas no registran los datos diariamente.

En la Tabla 5-2 se presentan las concentraciones medias anuales de material particulado

MP10 estimadas para los años 2020, 2021 y 2022 de la estación indicada.

www.dfmconsultores.cl

11

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Tabla 5-2. Estadígrafos de y MP10. Periodo 2020- 2022. Estación Tierra Amarilla.**

|Estación|Año|Media anual MP10 [μg/m3N]|
|---|---|---|
|Tierra Amarilla|2020|52,3|
|Tierra Amarilla|2021|58,5|
|Tierra Amarilla|2022|56,8|

Fuente: Elaboración propia.

De acuerdo con los valores de la tabla precedente, es posible observar que las

concentraciones medias anuales de MP10 durante el trienio 2020-2022 superan los 52

[μg/m [3] N], destacándose el año 2021 como aquel de máxima concentración con un valor de

58,5 [μg/m [3] N]. Por tanto, a modo de considerar un escenario conservador en cuanto a la

calidad del aire de material particulado en la zona de emplazamiento del Proyecto, se ha

seleccionado el año 2021 como periodo de modelación.

#### 5.4 Características del Modelo de Dispersión de Contaminantes

A continuación, se describen las características principales del modelo de dispersión de

contaminantes atmosféricos implementado, específicamente el dominio de modelación,

topografía y usos de suelo del sector.

5.4.1 Dominio de la Modelación

El dominio de modelación considerado corresponde a un área de 37 × 43 kilómetros con

1.591 celdas de 1.000 × 1.000 m, tal como se indica en Figura 5-1.

Cabe destacar que, el dominio de modelación se ha definido considerando el área

rectangular que permita abarcar todas las fuentes emisoras y los receptores de interés

asociados al Proyecto, así como también el área de influencia del Proyecto para el

componente calidad del aire.

www.dfmconsultores.cl

12

**info@dfmconsultores.cl**

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-1. Dominio de Modelación.**

Fuente: Elaboración propia.

13

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.4.2 Topografía del Sector

La topografía del sector se ha extraído de _Shuttle Radar Topography Mission, SRTM1_, cuya

resolución es aproximadamente 30 m. Este se ha sido incorporado al modelo con el objetivo

de proporcionar la altura de los puntos de interés.

A continuación, en la Figura 5-2 se representa la información utilizada.

www.dfmconsultores.cl

14

**info@dfmconsultores.cl**

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-2. Topografía del Dominio de Modelación.**

Fuente: Elaboración propia.

15

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.4.3 Uso de Suelos

De acuerdo con el dominio de modelación y con la información relacionada al uso de suelo

de la zona, obtenida a través de los archivos _Global Land Cover Characterization (GLCC)_

publicados por el _U.S. Geological Survey (USGS)_, en la Figura 5-3 se presentan los principales

usos de suelos dentro del dominio señalado, en donde se puede apreciar que predominan

los suelos de tierra estéril y, en menor proporción, los suelos de tipo pastizal.

www.dfmconsultores.cl

16

**info@dfmconsultores.cl**

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-3. Uso de Suelos del Dominio de Modelación.**

Fuente: Elaboración propia.

17

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

#### 5.5 Caracterización Meteorológica del área del Proyecto

En la siguiente sección se presenta la caracterización de la meteorología observada y

modelada para el sector del Proyecto.

5.5.1 Meteorología de Superficie- Valores Observados

La meteorología de superficie utilizada para caracterizar el área del Proyecto corresponde

a los registros horarios de velocidad y dirección del viento, temperatura, humedad relativa,

precipitación acumulada, radiación solar y presión atmosférica, monitoreados en la

estación Tierra Amarilla, ubicada en la comuna de Tierra Amarilla, Región de Atacama.

En la Tabla 5-3 se presentan las coordenadas UTM de la estación indicada, junto con las

variables consideradas y el periodo de monitoreo respectivo.

**Tabla 5-3. Caracterización Estación de Monitoreo Meteorológico.**

|Estación de<br>Monitoreo|Variables Meteorológicas<br>Registradas|Período de Datos<br>Disponibles|Coordenadas UTM (Datum<br>WGS84 19S)|Col5|
|---|---|---|---|---|
|**Estación de**<br>**Monitoreo**|**Variables Meteorológicas**<br>**Registradas**|**Período de Datos**<br>**Disponibles**|**Este [m]**|**Norte [m]**|
|Tierra Amarilla|▪ <br>Dirección del Viento (°)<br>▪ <br>Velocidad del Viento (m/s)<br>▪ <br>Temperatura (°C)<br>▪ <br>Humedad Relativa (%)<br>▪ <br>Precipitación Acumulada (mm)<br>▪ <br>Radiación Solar (W/m2) <br>▪ <br>Presión Atmosférica (hPa)|Enero de 2021 a<br>diciembre de 2022|374.932|6.960.241|

Fuente: Elaboración propia.

A continuación, en la Figura 5-4 se muestra la ubicación referencial de la estación de

monitoreo meteorológico mencionada con respecto a la zona de emplazamiento del

Proyecto en evaluación.

www.dfmconsultores.cl

18

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-4. Ubicación Referencial Estación de Monitoreo Meteorológico.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

19

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.5.1.1 Estación Meteorológica Tierra Amarilla

5.5.1.1.1 Velocidad y Dirección del Viento

En la Tabla 5-4 se presenta el resumen de información para la variable velocidad del viento,

específicamente el promedio, máximo y mínimo para cada uno de los años en estudio,

además del porcentaje de calmas, el cual se define como el porcentaje del tiempo en que

la velocidad del viento es menor a 0,5 m/s.

De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA”, las series de datos meteorológicos deben contener un 75% de datos válidos, lo cual

se cumple para los años 2021 y 2022. En consecuencia, los años mencionados serán

utilizados para los siguientes análisis.

**Tabla 5-4. Resumen de información Velocidad del Viento. Estación Tierra Amarilla.**

|Parámetro|Variable|Año|Col4|Bienio|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2021**|**2022**|**2022**|
|Velocidad de Viento (m/s)|Promedio|2,33|2,29|2,31|
|Velocidad de Viento (m/s)|Máximo|5,43|5,96|5,96|
|Velocidad de Viento (m/s)|Mínimo|0,03|0,00|0,00|
|Porcentaje de Calmas (%)|Porcentaje de Calmas (%)|4,44%|5,04%|4,74%|
|Datos Válidos (%)|Datos Válidos (%)|99,59%|97,84%|98,72%|

Fuente: Elaboración propia.

A continuación, se muestran las series de tiempo, ciclos diarios y ciclo estacional para las

variables meteorológicas velocidad y dirección del viento.

www.dfmconsultores.cl

20

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Series de Tiempo_

De tal manera de verificar la completitud de los datos, en la Figura 5-5 y Figura 5-6 se

presentan las series de tiempo para la variable velocidad y dirección del viento

respectivamente, en donde es posible observar que se presenta el 98,7% de los registros

para ambas variables, como consecuencia de un breve intervalo de ausencia de datos

observados durante el mes de octubre del año 2022.

Además, se puede identificar que las velocidades de viento se encuentran mayormente

entre los 0 y 5 m/s, exceptuando ciertos valores que sobrepasan este intervalo, alcanzando

registros de hasta los 5,96 m/s.

**Figura 5-5. Serie de Tiempo Velocidad del Viento. Periodo enero 2021 a diciembre de 2022. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

21

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Por otro lado, en cuanto a la dirección del viento predominante, se observa que los valores

oscilan dentro del rango de 0 a 360°, destacándose una mayor cantidad registros entre los

0 y 50° a lo largo del periodo analizado, así como también entre los 150 y 200° durante los

meses de marzo a octubre de cada año.

**Figura 5-6. Serie de Tiempo Dirección del Viento Periodo enero 2021 a diciembre de 2022. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

Por otro lado, para caracterizar la información anual registrada, tanto para la velocidad

como para la dirección del viento, en la Tabla 5-5 se presenta la frecuencia de distribución

para la velocidad y dirección del viento observada.

www.dfmconsultores.cl

22

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Tabla 5-5. Frecuencia de distribución Velocidad y Dirección del Viento. Periodo enero 2021 a diciembre de 2022. Estación Tierra Amarilla.**

|Dirección|Col2|Distribución Porcentual de Velocidad del Viento (m/s)|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Dirección**|**Dirección**|**0,50 - 2,10**|**2,10 - 3,60**|**3,60 - 5,70**|**5,70 - 8,80**|**8,80 - 11,10**|**>= 11,10**|**Total (%)**|
|348,75 - 11,25|N|5,80%|3,00%|2,29%|0,00%|0,00%|0,00%|11,08%|
|11,25 - 33,75|NNE|14,30%|22,01%|18,73%|0,00%|0,00%|0,00%|55,04%|
|33,75 - 56,25|NE|2,82%|1,13%|0,84%|0,01%|0,00%|0,00%|4,81%|
|56,25 - 78,75|ENE|1,04%|0,01%|0,00%|0,00%|0,00%|0,00%|1,05%|
|78,75 - 101,25|E|0,49%|0,00%|0,00%|0,00%|0,00%|0,00%|0,49%|
|101,25 - 123,75|ESE|0,34%|0,00%|0,00%|0,00%|0,00%|0,00%|0,34%|
|123,75 - 146,25|SE|0,42%|0,00%|0,00%|0,00%|0,00%|0,00%|0,42%|
|146,25 - 168,75|SSE|2,18%|0,03%|0,00%|0,00%|0,00%|0,00%|2,21%|
|168,75 - 191,25|S|8,67%|0,25%|0,00%|0,00%|0,00%|0,00%|8,92%|
|191,25 - 213,75|SSW|4,21%|0,21%|0,01%|0,00%|0,00%|0,00%|4,43%|
|213,75 - 236,25|SW|0,95%|0,05%|0,00%|0,00%|0,00%|0,00%|1,00%|
|236,25 - 258,75|WSW|0,63%|0,01%|0,00%|0,00%|0,00%|0,00%|0,64%|
|258,75 - 281,25|W|0,60%|0,08%|0,00%|0,00%|0,00%|0,00%|0,68%|
|281,25 - 303,75|WNW|0,62%|0,15%|0,00%|0,00%|0,00%|0,00%|0,76%|
|303,75 - 326,25|NW|0,93%|0,43%|0,03%|0,00%|0,00%|0,00%|1,39%|
|326,25 - 348,75|NNW|1,92%|0,62%|0,14%|0,00%|0,00%|0,00%|2,68%|
|Sub-Total|Sub-Total|45,91%|27,97%|22,04%|0,01%|0,00%|0,00%|95,93%|
|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|4,07%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

23

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclos Diarios_

En la Figura 5-7 se presenta el ciclo diario para la variable velocidad del viento, en donde se

puede observar que las menores velocidades ocurren durante el periodo nocturno y de

madrugada, específicamente entre las 23:00 y 7:00 horas, en donde se alcanza un mínimo

promedio de velocidad de viento de aproximadamente 1,3 m/s. Luego, la velocidad

comienza a incrementar sostenidamente alcanzando las mayores intensidades de viento a

las 14:00 horas, adoptando valores máximos promedios de aproximadamente 3,8 m/s.

Posteriormente, la velocidad desciende hasta alcanzar los valores nocturnos, iniciando

nuevamente el ciclo. Cabe mencionar que el rango de oscilación del 90% de los datos posee

una diferencia de 2,6 m/s al momento de máxima velocidad y de 2,0 m/s al momento de

mínima velocidad.

**Figura 5-7. Ciclo Diario Velocidad del Viento. Periodo enero 2021 a diciembre de 2022. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

24

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Por otro lado, con el fin de caracterizar de una manera más gráfica las distribuciones de las

direcciones y velocidades de viento, a continuación, en la Figura 5-8 y Figura 5-9 se

presentan el ciclo diario de dirección del viento y las rosas de vientos conformadas por

periodos de 8 horas, es decir, considerando los registros desde las 0 hasta las 8 horas, desde

las 8 hasta las 16 horas y desde las 16 hasta las 0 horas para el periodo de monitoreo

comprendido entre enero de 2021 y diciembre de 2022.

De acuerdo con las figuras presentadas, se puede observar que los vientos registrados entre

las 0 y 8 horas se presentan con frecuencias superiores al 25% en dirección nornoreste

(NNE) y sur (S), alcanzando velocidades de viento de hasta 3,6 m/s. Asimismo, se observan

vientos en menor proporción en dirección norte (N) y sursuroeste (SSO), los que presentan

velocidades de hasta 3,6 m/s igualmente.

Luego, durante el periodo comprendido entre las 8 y 16 horas, se aprecian frecuencias de

vientos mayores al 52% en dirección nornoreste (NNE), con velocidades de viento de hasta

5,7 m/s. Mientras que, los vientos en dirección norte (N) y noreste (NE) se presentan con

frecuencias entre el 7 y 12%, y de igual manera, con velocidades que pueden alcanzar hasta

los 5,7 m/s.

Por último, durante el periodo comprendido entre las 16 y 0 horas, los vientos se presentan

de manera notoriamente predominante en dirección nornoreste (NNE) con frecuencias por

sobre el 60% y con velocidades de viento que pueden alcanzar hasta los 5,7 m/s. Mientras

que, los vientos en dirección norte (N) se presentan en menor proporción, pero de igual

manera con velocidades que pueden alcanzar los 5,7 m/s.

Así, posterior a este último periodo descrito, las direcciones de viento cambian nuevamente

dando inicio al ciclo.

www.dfmconsultores.cl

25

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-8. Ciclo Diario Dirección del Viento. Periodo enero 2021 a diciembre de 2022. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

26

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-9. Rosas de Vientos. Periodo de 0 a 8 horas, 8 a 16 horas y 16 a 0 horas. Periodo enero 2021 a diciembre de 2022. Estación Tierra Amarilla.**

|Período 0 a 8 horas|Período 8 a 16 horas|Período 16 a 0 horas|
|---|---|---|
||||
|**Simbología**|**Simbología**|**Simbología**|
||||

Fuente: Elaboración propia.

www.dfmconsultores.cl

27

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclo Estacional_

En la Figura 5-10 se presenta el ciclo estacional de vientos observados, en donde es posible

apreciar que las mayores intensidades de viento se producen durante los meses de octubre

a febrero, específicamente entre las 12:00 y 18:00 horas durante la estación primaveral y

entre las 17:00 y 18:00 horas durante el verano. En cambio, las menores intensidades se

presentan durante el periodo comprendido entre febrero y octubre, entre las 22:00 y 10:00

horas aproximadamente.

Por otro lado, en cuanto a la dirección del viento, es posible observar una marcada

predominancia de vientos nornoreste (NNE) a lo largo del año entre las 10:00 y 20:00 horas,

así como también entre las 21:00 y 9:00 horas durante los meses de octubre a marzo.

Mientras que, durante el periodo nocturno y de madrugada de los meses de invierno, se

puede observar una variación en la dirección de los vientos, presentándose en mayor

proporción en dirección sur (S) durante los meses de mayo a septiembre.

**Figura 5-10. Ciclo Estacional Vientos. Periodo enero 2021 a diciembre de 2022. Estación Tierra Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

28

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.5.1.1.2 Temperatura

En la Tabla 5-6 se muestra el resumen de información para la variable temperatura,

especificando promedio, máximo y mínimo anual para cada uno de los años en estudio.

De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA”, las series de datos meteorológicos deben contar con un 75% de datos válidos, lo cual

se cumple para el bienio 2021-2022. En consecuencia, los años mencionados serán

utilizados para los siguientes análisis.

**Tabla 5-6. Resumen de información Temperatura. Estación Tierra Amarilla.**

|Parámetro|Variable|Año|Col4|Bienio|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2021**|**2022**|**2022**|
|Temperatura (°C)|Promedio|16,23|15,99|16,11|
|Temperatura (°C)|Máximo|34,70|33,30|34,70|
|Temperatura (°C)|Mínimo|1,74|2,08|1,74|
|Datos Válidos (%)|Datos Válidos (%)|99,61%|97,84%|98,73%|

Fuente: Elaboración propia.

A continuación, en los siguientes apartados se presenta la serie de tiempo, ciclo diario y

ciclo estacional observados para la variable meteorológica temperatura.

www.dfmconsultores.cl

29

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Serie de Tiempo_

A modo de verificación de la completitud de los datos obtenidos mediante la estación de

monitoreo meteorológico Tierra Amarilla, en la Figura 5-11 se presenta la serie de tiempo

para la variable temperatura. En ella es posible apreciar un breve intervalo con ausencia de

datos durante octubre de 2022. Sin embargo, el porcentaje mínimo de datos válidos se

cumple para el año en cuestión, por lo que es posible considerarlo en el análisis de esta

variable.

Por otro lado, se puede identificar que las temperaturas registradas se encuentran

principalmente entre los 2 y 34°C aproximadamente, a excepción de ciertos valores que se

encuentran fuera del rango descrito, alcanzando valores cercanos a los 35°C.

**Figura 5-11. Serie de Tiempo Temperatura. Periodo enero 2021 a diciembre de 2022. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

30

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclo Diario_

En la Figura 5-12 se expone el ciclo diario para la variable temperatura, en donde es posible

observar que las menores temperaturas ocurren durante la madrugada, específicamente

entre las 22:00 y 6:00 horas, alcanzando un mínimo promedio de temperatura de

aproximadamente 10°C a las 6:00 horas. Tras ello, la temperatura comienza a aumentar

paulatinamente hasta alcanzar un máximo promedio aproximado de 25°C a las 15:00 horas,

para luego comenzar a disminuir de manera gradual hasta alcanzar los valores de

temperatura nocturnas, por bajo los 14°C aproximadamente, dando comienzo nuevamente

al ciclo. Cabe mencionar que el rango de oscilación del 90% de los datos posee una

diferencia de 14°C al momento de máxima temperatura y de 11°C al momento de mínima

temperatura.

**Figura 5-12. Ciclo Diario Temperatura. Periodo enero 2021 a diciembre de 2022. Estación Tierra Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

31

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclo Estacional_

En la Figura 5-13 se presenta el ciclo estacional de la temperatura observada, en donde es

posible notar que las mayores temperaturas se registran durante los meses de verano,

específicamente entre noviembre y febrero, en el periodo diurno comprendido entre las

13:00 y 16:00 horas, alcanzando valores aproximados de 30°C. En cambio, las menores

temperaturas se aprecian durante el periodo de madrugada comprendido entre las 1:00 y

7:00 horas durante los meses de mayo a agosto, registrando temperaturas cercanas a los

5°C. Además, se puede observar que las máximas temperaturas registradas durante el

periodo diurno en la temporada invernal, específicamente en el mes de julio, alcanzan

máximas por bajo los 20°C.

**Figura 5-13. Ciclo Estacional Temperatura. Periodo enero 2021 a diciembre de 2022. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

32

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.5.1.1.3 Humedad Relativa

En la Tabla 5-7 se presenta el resumen de información para la variable humedad relativa,

detallando los valores promedio, máximos y mínimos para cada uno de los años en estudio.

De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA”, las series de datos meteorológicos deben contar con un 75% de datos válidos, lo cual

se cumple para el bienio 2021-2022. En consecuencia, los años mencionados serán

utilizados para los siguientes análisis.

**Tabla 5-7. Resumen de información Humedad Relativa. Estación Tierra Amarilla.**

|Parámetro|Variable|Año|Col4|Bienio|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2021**|**2022**|**2022**|
|Humedad Relativa (%)|Promedio|55,16|63,02|59,09|
|Humedad Relativa (%)|Máximo|95,49|99,07|99,07|
|Humedad Relativa (%)|Mínimo|2,69|2,25|2,25|
|Datos Válidos (%)|Datos Válidos (%)|99,61%|97,84%|98,73%|

Fuente: Elaboración propia.

A continuación, se presentan la serie de tiempo, ciclo diario y ciclo estacional observados

para la variable meteorológica humedad relativa.

www.dfmconsultores.cl

33

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Serie de Tiempo_

A modo de verificación de completitud de datos, en la Figura 5-14 se presenta la serie de

tiempo para la variable meteorológica humedad relativa, en donde es posible apreciar un

breve intervalo con ausencia de datos durante octubre de 2022. No obstante, se cumple

con el porcentaje mínimo de datos válidos para el año en cuestión, por lo que es posible

considerarlo en el análisis de esta variable.

Por otro lado, se puede observar que los valores de humedad relativa se encuentran

mayormente entre el 10% y 100%, a excepción de ciertos valores que se encuentran por

bajo este intervalo y alcanzan valores de hasta 2,25%.

**Figura 5-14. Serie de Tiempo Humedad Relativa. Periodo enero 2021 a diciembre de 2022. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

34

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclo Diario_

En la Figura 5-15 se presenta el ciclo diario para la variable humedad relativa, en donde es

posible apreciar que durante el periodo nocturno y de madrugada, es decir entre las 23:00

y 08:00 horas, se presentan los máximos valores de humedad, alcanzando un registro

máximo aproximado de 80% a las 6:00 horas. Tras ello, los valores comienzan a descender

a lo largo del día alcanzando un mínimo promedio aproximado de 32% a las 15:00 horas,

para luego aumentar de manera paulatina hasta adoptar los valores nocturnos, dando inicio

nuevamente al ciclo. Cabe mencionar que el rango de oscilación del 90% de los datos posee

una diferencia de 31% al momento de mínima humedad y de 41% al momento de máxima

humedad relativa.

**Figura 5-15. Ciclo Diario Humedad Relativa. Periodo enero 2021 a diciembre de 2022. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

35

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclo Estacional_

En la Figura 5-16 se presenta el ciclo estacional de la humedad relativa, en donde se puede

apreciar que los mayores porcentajes de humedad se registran durante los meses de julio

a noviembre durante el periodo de madrugada, alcanzando valores por sobre el 80% de

humedad. En cambio, los menores porcentajes se presentan durante los meses de agosto a

febrero durante el periodo diurno, específicamente entre las 13:00 y 17:00 horas,

registrando valores por bajo el 30%. Además, es posible observar que, durante la

temporada invernal, particularmente en los meses de junio y julio, la humedad presenta

una variación del 45% durante el transcurso del día, mientras que, durante el periodo de

verano, los valores pueden alcanzar una diferencia de hasta un 55% de humedad.

**Figura 5-16. Ciclo Estacional Humedad Relativa. Periodo enero 2021 a diciembre de 2022. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

36

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.5.1.1.4 Precipitación Acumulada

En la Tabla 5-8 se presenta el resumen de información para la variable precipitación diaria

y mensual acumulada, especificando los valores promedios, máximos y mínimos anuales

para cada uno de los años en estudio, además del total de precipitaciones anual

acumuladas.

De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA”, las series de datos meteorológicos deben contar con un 75% de datos válidos, lo cual

se cumple para el bienio 2021-2022. En consecuencia, los años mencionados serán

utilizados para los siguientes análisis.

**Tabla 5-8. Resumen de información Precipitaciones Acumuladas. Estación Tierra Amarilla.**

|Parámetro|Variable|Año|Col4|Bienio|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2021**|**2022**|**2022**|
|Precipitación Diaria Acumulada (mm)|Máximo|4,40|16,10|16,10|
|Precipitación Mensual Acumulada (mm)|Máximo|8,80|26,30|26,30|
|Precipitación Anual Acumulada (mm)|Precipitación Anual Acumulada (mm)|12,50|27,80|20,15|
|Datos Válidos (%)|Datos Válidos (%)|99,62%|81,15%|90,39%|

Fuente: Elaboración propia.

A continuación, se muestran las series de tiempo para las variables meteorológicas

precipitación diaria y mensual acumulada.

www.dfmconsultores.cl

37

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Series de Tiempo_

A modo de verificación de la completitud de los datos obtenidos mediante la estación de

monitoreo Tierra Amarilla, en la Figura 5-17 se presenta la serie de tiempo para la variable

meteorológica precipitación diaria acumulada. En ella se puede apreciar que las mayores

precipitaciones diarias acumuladas se registran durante el periodo invernal durante los

años 2021 y 2022, alcanzando registros por sobre los 4 y 16 mm de agua caída

respectivamente.

**Figura 5-17. Serie de Tiempo Precipitación Acumulada Diaria. Periodo enero 2021 a diciembre de 2022.**

**Estación Tierra Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

38

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Por otro lado, en la Figura 5-18 se presenta la serie de tiempo para la variable meteorológica

precipitacion mensual acumulada, en donde es posible apreciar que las mayores

precipitaciones se registran durante agosto de 2021, con una precipitación mensual

acumulada de 8,8 mm, y julio de 2022, con una precipitación mensual acumulada de 26,3

mm. Cabe destacar que, durante los meses de septiembre a mayo no se registran

precipitaciones en la zona.

**Figura 5-18. Serie de Tiempo Precipitación Acumulada Mensual. Periodo enero 2021 a diciembre de 2022.**

**Estación Tierra Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

39

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.5.1.1.5 Radiación Solar

En la Tabla 5-9 se presenta el resumen de información para la variable radiación solar,

especificando los valores máximos, mínimos y promedio anual para cada uno de los años

en estudio.

De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA”, las series de datos meteorológicos deben contar con un 75% de datos válidos, lo cual

se cumple para el bienio 2021-2022. En consecuencia, los años mencionados serán

utilizados para los siguientes análisis.

**Tabla 5-9. Resumen de información Radiación Solar. Estación Tierra Amarilla.**

|Parámetro|Variable|Año|Col4|Bienio|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2021**|**2022**|**2022**|
|Radiación Solar (W/m2)|Promedio|200,92|217,34|209,13|
|Radiación Solar (W/m2)|Máximo|1.007,92|1.030,83|1.030,83|
|Radiación Solar (W/m2)|Mínimo|0,00|0,00|0,00|
|Datos Válidos (%)<br>|Datos Válidos (%)<br>|99,55%<br>|97,04%|98,30%|

Fuente: Elaboración propia.

A continuación, se muestran la serie de tiempo, ciclo diario y ciclo estacional observados

para la variable meteorológica radiación solar.

www.dfmconsultores.cl

40

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Serie de Tiempo_

A modo de verificación de la completitud de los datos, en la Figura 5-19 se presenta la serie

de tiempo para la variable meteorológica radiación solar, es posible apreciar un breve

intervalo con ausencia de datos durante octubre de 2022. Sin embargo, el porcentaje

mínimo de datos válidos se cumple para el año en cuestión, por lo que es posible

considerarlo en el análisis de esta variable.

Por otro lado, se puede identificar que, los registros de radiación solar oscilan entre los 0 y

1000 W/m [2], a excepción de ciertos registros que superan este intervalo alcanzando valores

de hasta 1.030 W/m [2] . Además, se observa que las máximas radiaciones se presentan

durante el periodo de verano y las mínimas radiaciones durante el periodo invernal, de

modo que se genera un comportamiento oscilatorio de esta variable en función del tiempo.

**Figura 5-19. Serie de Tiempo Radiación Solar. Periodo enero 2021 a diciembre de 2022. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

41

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclo Diario_

En la Figura 5-20 se presenta el ciclo diario para la variable radiación solar, en donde se

puede apreciar que durante el periodo nocturno y de madrugada no se registra radiación

solar, específicamente entre las 20:00 y 5:00 horas. Tras dicho intervalo de tiempo, la

radiación solar incrementa de manera sostenida hasta alcanzar un máximo promedio

aproximado de 730 W/m [2] a las 13:00 horas. Luego, la radiación solar comienza a disminuir

rápidamente durante la tarde hasta no registrar valores, dando inicio nuevamente al ciclo

descrito. Cabe mencionar que el rango de oscilación del 90% de los datos posee una

diferencia de 600 W/m [2] aproximadamente al momento de máxima radiación.

**Figura 5-20. Ciclo Diario Radiación Solar. Periodo enero 2021 a diciembre de 2022. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

42

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclo Estacional_

En la Figura 5-21 se presenta el ciclo estacional de radiación solar observada, en donde es

posible apreciar que, durante el periodo nocturno y de madrugada, comprendido entre las

19:00 y 6:00 horas, no se presentan valores para esta variable meteorológica. Por el

contrario, las máximas radiaciones solares registradas se presentan durante los meses de

octubre a enero, particularmente entre las 11:00 y 14:00 horas, con valores que superan los

900 W/m [2] . Cabe mencionar que, durante las épocas de otoño-invierno comprendida por

los meses de mayo y julio, las máximas radiaciones registradas durante el día no superan

los 400 W/m [2], generándose un ciclo diario de radiación de menor variación en comparación

a los meses restantes.

**Figura 5-21. Ciclo Estacional Radiación Solar. Periodo enero 2021 a diciembre de 2022. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

43

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.5.1.1.6 Presión Atmosférica

En la Tabla 5-10 se presenta el resumen de información para la variable presión atmosférica,

detallando los valores máximos, mínimos y promedio anual para cada uno de los años en

estudio.

De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA”, las series de datos meteorológicos deben contar con un 75% de datos válidos, lo cual

se cumple para el bienio 2021-2022. En consecuencia, los años mencionados serán

utilizados para los siguientes análisis.

**Tabla 5-10. Resumen de Información Presión Atmosférica. Estación Tierra Amarilla.**

|Parámetro|Variable|Año|Col4|Bienio|
|---|---|---|---|---|
|**Parámetro**|**Variable**|**2021**|**2022**|**2022**|
|Presión Atmosférica (hPa)|Promedio|719,42|719,34|719,38|
|Presión Atmosférica (hPa)|Máximo|726,56|726,14|726,56|
|Presión Atmosférica (hPa)|Mínimo|714,53|714,54|714,53|
|Datos Válidos (%)|Datos Válidos (%)|99,60%|97,85%|98,73%|

Fuente: Elaboración propia.

De esta forma, a continuación, se presenta la serie de tiempo, ciclo diario y ciclo estacional

observados para la variable meteorológica presión atmosférica.

www.dfmconsultores.cl

44

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Serie de Tiempo_

A modo de verificación de la completitud de los datos, en la Figura 5-22 se presenta la serie

de tiempo para la variable meteorológica presión atmosférica, en donde es posible apreciar

un breve intervalo con ausencia de datos durante octubre de 2022. Sin embargo, el

porcentaje mínimo de datos válidos se cumple para el año en cuestión, por lo que es posible

considerarlo en el análisis de esta variable.

Por otro lado, se puede identificar que, los registros de presión atmosférica oscilan

mayormente entre los 714 y 727 hPa, alcanzando los máximos registros durante el periodo

invernal y los valores mínimos durante la temporada de verano, de modo que se genera un

comportamiento oscilatorio de esta variable en función del tiempo.

**Figura 5-22. Serie de Tiempo Presión Atmosférica. Periodo enero 2021 a diciembre de 2022. Estación**

**Tierra Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

45

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclo Diario_

En la Figura 5-23 se presenta el ciclo diario para la variable presión atmosférica, en donde

se puede visualizar un ciclo sinusoidal relativamente estable a lo largo del día, pues los

maximos valores de presión atmosférica se aproximan a los 720,5 hPa, mientras que los

valores más bajos se acercan a los 718 hPa, especificamente a las 16:00. Cabe mencionar

que, en esta última hora el ciclo presenta una ligera disminución de los valores mínimos

registrados en comparación a los valores presentados durante la madrugada,

especificamente entre las 3:00 y 4:00 horas, en donde la presión atmosférica alcanza un

valor mínimo de 719,3 hPa.

**Figura 5-23. Ciclo Diario Presión Atmosférica. Periodo enero 2021 a diciembre de 2022. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

46

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclo Anual_

En la Figura 5-24 se presenta el ciclo anual para la variable presión atmosférica, en donde

es posible apreciar que, conforme a los registros disponibles de esta variable meteorológica,

los máximos valores de presión se presentan durante los meses de junio a septiembre,

alcanzando un máximo valor de aproximadamente 720,6 durante el mes de agosto. Por el

contrario, los menores valores se registran durante el periodo de verano, particularmente

en el mes de febrero, alcanzando registros cercanos a los 718,1 hPa.

**Figura 5-24. Ciclo Estacional Presión Atmosférica. Periodo enero 2021 a diciembre de 2022. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

47

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.5.2 Meteorología de Superficie- Valores Modelados

5.5.2.1 Estación Meteorológica Tierra Amarilla

5.5.2.1.1 Velocidad y Dirección del Viento

En la Tabla 5-11 se presenta el resumen de información para la variable velocidad del viento

modelada, específicamente el promedio, máximo y mínimo del año en estudio, además del

porcentaje de calmas, el cual se define como el porcentaje del tiempo en que la velocidad

del viento es menor a 0,5 m/s.

De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA”, las series de datos meteorológicos deben contener un 75% de datos válidos, lo cual

se cumple para el año 2021 debido a que se cuenta con la completitud de los datos a partir

del modelo WRF.

**Tabla 5-11. Resumen de información Velocidad del Viento Modelada. Estación Tierra Amarilla.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2021**|
|Velocidad de Viento (m/s)|Promedio|3,40|
|Velocidad de Viento (m/s)|Máximo|11,30|
|Velocidad de Viento (m/s)|Mínimo|0,03|
|Porcentaje de Calmas (%)|Porcentaje de Calmas (%)|4,75|
|Datos Válidos (%)|Datos Válidos (%)|100,00%|

Fuente: Elaboración propia.

A continuación, se muestran las series de tiempo, ciclos diarios y ciclo estacional para las

variables meteorológicas modeladas velocidad y dirección del viento.

www.dfmconsultores.cl

48

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Series de Tiempo_

De tal manera de verificar la completitud de los datos, en la Figura 5-25 y Figura 5-26 se

presentan las series de tiempo para la variable velocidad y dirección del viento modeladas

respectivamente, en donde es posible observar que se cuenta con el 100% de los registros

para ambas variables.

Además, se puede identificar que las velocidades de viento se encuentran mayormente

entre los 0 y 10 m/s, exceptuando ciertos valores que sobrepasan este intervalo, alcanzando

registros de hasta los 11,3 m/s durante el periodo de verano.

**Figura 5-25. Serie de Tiempo Velocidad del Viento Modelada. Enero a diciembre de 2021. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

49

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

En cuanto a la dirección del viento, se puede identificar una mayor concentración de datos

entre los 0° y 50°, 150° y 200°, y entre los 250°y 300°, no obstante, éste último intervalo de

direcciones de viento se presenta principalmente durante los periodos cálidos,

específicamente durante los meses de septiembre a abril.

**Figura 5-26. Serie de Tiempo Dirección del Viento Modelada. Enero a diciembre de 2021. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

Por otro lado, para caracterizar la información anual registrada tanto para la velocidad

como para la dirección del viento, en la Tabla 5-12 se presenta la frecuencia de distribución

para la velocidad y dirección del viento modelada.

www.dfmconsultores.cl

50

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Tabla 5-12. Frecuencia de distribución Velocidad y Dirección del Viento Modelada. Enero a diciembre de 2021. Estación Tierra Amarilla.**

|Dirección|Col2|Distribución Porcentual de Velocidad del Viento (m/s)|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|**Dirección**|**Dirección**|**0,50 - 2,10**|**2,10 - 3,60**|**3,60 - 5,70**|**5,70 - 8,80**|**8,80 - 11,10**|**>= 11,10**|**Total (%)**|
|348,75 - 11,25|N|3,15%|5,00%|7,60%|13,78%|1,77%|0,02%|31,32%|
|11,25 - 33,75|NNE|5,18%|3,97%|4,19%|0,39%|0,19%|0,00%|13,93%|
|33,75 - 56,25|NE|1,77%|0,47%|0,07%|0,00%|0,00%|0,00%|2,31%|
|56,25 - 78,75|ENE|0,37%|0,01%|0,00%|0,00%|0,00%|0,00%|0,38%|
|78,75 - 101,25|E|0,21%|0,01%|0,02%|0,00%|0,00%|0,00%|0,24%|
|101,25 - 123,75|ESE|0,24%|0,00%|0,00%|0,00%|0,00%|0,00%|0,24%|
|123,75 - 146,25|SE|0,64%|0,01%|0,01%|0,00%|0,00%|0,00%|0,66%|
|146,25 - 168,75|SSE|2,52%|0,35%|0,00%|0,00%|0,00%|0,00%|2,88%|
|168,75 - 191,25|S|11,07%|7,01%|0,34%|0,00%|0,00%|0,00%|18,42%|
|191,25 - 213,75|SSO|5,02%|0,34%|0,01%|0,00%|0,00%|0,00%|5,38%|
|213,75 - 236,25|SO|1,39%|0,02%|0,03%|0,06%|0,00%|0,00%|1,51%|
|236,25 - 258,75|OSO|0,51%|0,02%|0,25%|0,16%|0,01%|0,00%|0,96%|
|258,75 - 281,25|O|0,43%|0,10%|3,33%|0,70%|0,00%|0,00%|4,57%|
|281,25 - 303,75|ONO|0,32%|0,22%|6,02%|0,63%|0,01%|0,00%|7,19%|
|303,75 - 326,25|NO|0,53%|0,16%|1,37%|0,05%|0,00%|0,00%|2,10%|
|326,25 - 348,75|NNO|1,61%|0,31%|0,89%|0,37%|0,00%|0,00%|3,17%|
|Sub-Total|Sub-Total|34,97%|18,01%|24,14%|16,12%|1,99%|0,02%|95,25%|
|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|Calmas|4,75%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

51

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclos Diarios_

En la Figura 5-27 se presenta el ciclo diario para la variable velocidad del viento modelada,

en donde se puede observar que las menores velocidades ocurren durante el periodo

nocturno y de madrugada, específicamente entre las 22:00 y 8:00 horas, en donde se

alcanza un mínimo promedio de velocidad de viento de aproximadamente 1,4 m/s a las 8:00

horas. A partir de esta última hora, la velocidad comienza a incrementar sostenidamente

alcanzando las mayores intensidades de viento entre las 11:00 y 18:00 horas, adoptando

valores máximos promedios de aproximadamente 6 m/s. Posteriormente, la velocidad

desciende hasta alcanzar los valores nocturnos, iniciando nuevamente el ciclo. Cabe

mencionar que el rango de oscilación del 90% de los datos posee una diferencia de 5,5 m/s

al momento de máxima velocidad y de 2,5 m/s al momento de mínima velocidad.

**Figura 5-27. Ciclo Diario Velocidad del Viento Modelada. Enero a diciembre de 2021. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

52
**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Por otro lado, con el fin de caracterizar de una manera más gráfica las distribuciones de las

direcciones y velocidades de viento modeladas, a continuación, en la Figura 5-28 y Figura

5-29 se presenta el ciclo diario de dirección del viento y las rosas de vientos modelados

conformadas por periodos de 8 horas, es decir, considerando los registros desde las 0 hasta

las 8 horas, desde las 8 hasta las 16 horas y desde las 16 hasta las 0 horas para el periodo

comprendido entre enero y diciembre de 2021.

De acuerdo con las figuras presentadas, se puede observar que los vientos registrados entre

las 0 y 8 horas se presentan con frecuencia superior al 36% en dirección sur (S), alcanzando

velocidades de viento de hasta 5,7 m/s. Por otro lado, los vientos en dirección sur suroeste

(SSO) y nornoreste (NNE) se presentan con frecuencias por sobre el 9% y con velocidades

de viento de hasta 3,6 m/s y 5,7 m/s según orden de mención.

Luego, durante el periodo comprendido entre las 8 y 16 horas, se aprecian frecuencias de

vientos mayores al 40% en dirección norte (N), con velocidades de viento de hasta 11,1 m/s.

Mientras que, los vientos en componentes oeste noroeste (ONO) y oeste (O) se presentan

en menor proporción, con frecuencias por sobre el 10%, y alcanzando velocidades de hasta

8,8 m/s.

Por último, durante el periodo comprendido entre las 16 y 0 horas, los vientos se presentan

de manera predominante en dirección norte (N) y nornoreste (NNE), con frecuencias

superiores al 32% y 24% respectivamente, y con velocidades que alcanzan hasta los 11,1

m/s. En cambio, los vientos en dirección sur (S) oeste noroeste (ONO) se presentan en

menor proporción con frecuencias por bajo el 16% y 5,7 m/s y 8,8 m/s según orden de

mención. Posterior a este último periodo descrito, las direcciones de viento cambian

nuevamente dando inicio al ciclo.

www.dfmconsultores.cl

53
**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-28. Ciclo Diario Dirección del Viento Modelada. Enero a diciembre de 2021. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

54
**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-29. Rosas de Vientos Modelados. Periodo de 0 a 8 horas, 8 a 16 horas y 16 a 0 horas. Enero a diciembre de 2021. Estación Tierra Amarilla.**

|Período 0 a 8 horas|Período 8 a 16 horas|Período 16 a 0 horas|
|---|---|---|
||||
|**Simbología**|**Simbología**|**Simbología**|
||||

Fuente: Elaboración propia.

www.dfmconsultores.cl

55

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclo Estacional_

En la Figura 5-30 se presenta el ciclo estacional de vientos modelados, en donde es posible

apreciar que las mayores intensidades de viento se producen entre los meses de agosto a

diciembre durante horas de la tarde, específicamente entre las 16:00 y 19:00 horas;

mientras que las menores intensidades se presentan durante el periodo nocturno y de

madrugada, entre las 22:00 y 0:00 horas durante los meses de enero a octubre, así como

también entre las 1:00 y 8:00 horas durante los meses de octubre a abril. Por otro lado, en

cuanto a la dirección del viento, es posible observar una marcada predominancia de vientos

sur (S) durante el periodo nocturno y de madrugada, mientras que durante el periodo diario

se identifican mayormente vientos en dirección norte (N) durante los meses de junio a

agosto y vientos en dirección oeste noroeste (ONO) durante los meses de noviembre a

marzo.

**Figura 5-30. Ciclo Estacional de Velocidad y Dirección del Viento Observado. Enero a diciembre de 2021.**

**Estación Tierra Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

56

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.5.2.1.2 Temperatura

A continuación, en la Tabla 5-13 se muestra el resumen de información para la variable

temperatura modelada, especificando promedio, máximo y mínimo anual para el año en

estudio.

De acuerdo con lo establecido en la “Guía para el Uso de Modelos de Calidad del Aire en el

SEIA”, las series de datos meteorológicos deben contar con un 75% de datos válidos, lo cual

se cumple para el año 2021 debido a que se cuenta con la completitud de los datos a partir

del modelo WRF.

**Tabla 5-13. Resumen de información Temperatura Modelada. Estación Tierra Amarilla.**

|Parámetro|Variable|Año|
|---|---|---|
|**Parámetro**|**Variable**|**2021**|
|Temperatura (°C)|Promedio|17,94|
|Temperatura (°C)|Máximo|33,97|
|Temperatura (°C)|Mínimo|4,31|
|Datos Válidos (%)|Datos Válidos (%)|100,00%|

Fuente: Elaboración propia.

A continuación, en los siguientes apartados se presenta la serie de tiempo, ciclo diario y

ciclo estacional modelados para la variable meteorológica temperatura.

www.dfmconsultores.cl

57

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Serie de Tiempo_

A modo de verificación de la completitud de los datos, en la Figura 5-31 se presenta la serie

de tiempo para la variable temperatura modelada, en donde es posible observar que se

cuenta con el 100% de los registros para dicha variable en concordancia con el uso de los

registros entregados por el modelo meteorológico WRF.

Por otro lado, se puede identificar que las temperaturas registradas se encuentran

principalmente entre los 5 y 30°C aproximadamente, con algunas excepciones durante los

periodos cálidos, en donde se observan temperaturas de hasta 33,97°C.

**Figura 5-31. Serie de Tiempo Temperatura Modelada. Enero a diciembre de 2021. Estación Tierra Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

58

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclo Diario_

En la Figura 5-32 se expone el ciclo diario para la variable temperatura modelada, en donde

es posible observar que las menores temperaturas ocurren durante la madrugada,

específicamente entre las 21:00 y 6:00 horas, alcanzando un mínimo promedio de

temperatura de aproximadamente 13°C a las 6:00 horas. Luego, la temperatura comienza

a aumentar paulatinamente hasta alcanzar un máximo promedio aproximado de 26°C a las

14:00 horas, para luego comenzar a disminuir de manera gradual hasta alcanzar los valores

de temperatura nocturnas, dando comienzo nuevamente al ciclo. Cabe mencionar que el

rango de oscilación del 90% de los datos posee una diferencia de 10°C al momento de

máxima temperatura y de 9°C al momento de mínima temperatura.

**Figura 5-32. Ciclo Diario Temperatura Modelada. Enero a diciembre de 2021. Estación Tierra Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

59

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclo Estacional_

En la Figura 5-33 se presenta el ciclo estacional de la temperatura modelada, en donde es

posible notar que las mayores temperaturas se registran durante los meses de verano,

específicamente entre noviembre y marzo, en el periodo diurno comprendido entre las

12:00 y 16:00 horas, alcanzando valores que rondan los 30°C. En cambio, las menores

temperaturas se registran durante los meses de julio a octubre, especialmente en el periodo

nocturno, en donde se presentan temperaturas mínimas promedio aproximadas de 10°C

entre las 1:00 y 8:00 horas.

**Figura 5-33. Ciclo Estacional Temperatura Modelada. Enero a diciembre de 2021. Estación Tierra Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

60

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.5.3 Meteorología de Altura - Valores Observados

Con respecto a la meteorología de altura, no existen registros de mediciones disponibles

en la estación utilizada que puedan ser incorporadas en este estudio.

5.5.4 Meteorología de Altura - Valores Modelados

5.5.4.1 Estación Meteorológica Tierra Amarilla

5.5.4.1.1 Altura de Capa de Mezcla

La altura de capa de mezcla es un parámetro obtenido tras el procesamiento de los

resultados del modelo meteorológico WRF, el cual representa la altura medida desde la

superficie en donde la inestabilidad favorece la dispersión vertical de contaminantes.

En consecuencia, a continuación, se presenta la caracterización de la variable meteorológica

altura de capa de mezcla, considerado los datos entregados por el modelo meteorológico

WRF correspondiente al año 2021 para el sector del Proyecto, identificando los valores

promedio, máximo y mínimo para esta variable, tal como se muestra en la Tabla 5-14.

<!-- INICIO TABLA 5-14. -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- WRF correspondiente al año 2021 para el sector del Proyecto, identificando los valores promedio, máximo y mínimo para esta variable, tal como se muestra en la Tabla 5-14. -->

**Tabla 5-14.: Resumen de Información Altura de Capa de Mezcla Modelada. Estación Tierra Amarilla.****

| Parámetro | Variable | Año 2021 |
| --- | --- | --- |
| Altura de Capa de Mezcla (m) | Promedio | 363,73 |
| Altura de Capa de Mezcla (m) | Máximo | 2.563,13 |
| Altura de Capa de Mezcla (m) | Mínimo | 30,34 |
| Altura de Capa de Mezcla (m) | Datos Válidos (%) | 100,00% |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. A continuación, se presenta la serie de tiempo, ciclo diario y ciclo estacional modelados para -->
<!-- FIN TABLA 5-14. -->


**Tabla 5-14. Resumen de Información Altura de Capa de Mezcla Modelada. Estación Tierra Amarilla.**

|Parámetro|Variable|Año 2021|
|---|---|---|
|Altura de Capa de Mezcla (m)|Promedio|363,73|
|Altura de Capa de Mezcla (m)|Máximo|2.563,13|
|Altura de Capa de Mezcla (m)|Mínimo|30,34|
|Altura de Capa de Mezcla (m)|Datos Válidos (%)|100,00%|

Fuente: Elaboración propia.

A continuación, se presenta la serie de tiempo, ciclo diario y ciclo estacional modelados para

la variable meteorológica altura de capa de mezcla.

www.dfmconsultores.cl

61

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Serie de Tiempo_

En la Figura 5-34 se presenta la serie de tiempo para la variable altura de capa de mezcla

modelada, en donde es posible observar una completitud de los datos, esto ya que el

parámetro ha sido calculado conforme a los resultados del modelo meteorológico WRF.

En ella se puede identificar que, los valores modelados se concentran mayormente entre

los 0 y 1.500 metros, a excepción de ciertas alturas que sobrepasan este último valor,

registrando datos de hasta 2.563 metros de altura de capa de mezcla.

**Figura 5-34. Serie de tiempo para Altura de Capa de Mezcla. Enero a diciembre de 2021. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

62

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclo Diario_

En la Figura 5-35 se presenta el ciclo diario para la variable altura de capa de mezcla

modelada, en donde se puede observar que los menores valores se presentan durante el

periodo nocturno y de madrugada, presentándose una estabilidad a los 30 metros

aproximadamente. A partir de las 7:00 horas, los valores incrementan de manera sostenida

conforme a la incidencia de la radiación solar, alcanzando un valor máximo promedio

aproximado de 1.180 metros a las 15:00 horas. Posterior a ello, la altura de la capa de

mezcla comienza a disminuir en magnitud hasta alcanzar los valores nocturnos, dando inicio

nuevamente al ciclo. Cabe mencionar que, el rango de oscilación del 90% de los datos de

esta variable es de aproximadamente 1.100 metros al momento de máxima altura.

**Figura 5-35. Ciclo diario para Altura de Capa de Mezcla. Enero a diciembre de 2021. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

63

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

_Ciclo Estacional_

En la Figura 5-36 se presenta el ciclo estacional de la altura de capa de mezcla modelada,

en donde es posible notar que las mayores alturas se registran durante los meses de enero

a marzo, alcanzando valores cercanos a los 1.500 metros, específicamente entre las 13:00

y 16:00 horas. Por el contrario, las menores alturas se presentan a lo largo del año durante

el periodo nocturno, especialmente entre las 22:00 y 7:00 horas, registrando valores

cercanos a los 30 metros de altura.

**Figura 5-36. Ciclo estacional Altura Capa de Mezcla Modelada. Enero a diciembre de 2021. Estación Tierra**

**Amarilla.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

64

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Diciembre 2023

#### 5.6 Análisis de Incertidumbre

Con el fin de determinar la incertidumbre entre los resultados del modelo meteorológico y

aquellos observados en la estación meteorológica Tierra Amarilla, en la siguiente sección se

presenta la comparación cualitativa y cuantitativa entre la meteorología observada y

modelada.

5.6.1 Estación Meteorológica Tierra Amarilla

5.6.1.1 Comparación Cualitativa

La meteorología de superficie es un factor relevante en la dispersión de los contaminantes,

por tanto, en el presente inciso se busca validar el modelo WRF de manera cualitativa, el

cual será utilizado como información base de entrada al modelo de dispersión CALPUFF.

Para ello, se presenta la comparación de los datos observados por la estación meteorológica

Tierra Amarilla para el periodo comprendido entre el 1 de enero al 31 de diciembre de 2021,

mismo periodo utilizado por el modelo meteorológico WRF. De este modo, se contrastan

los ciclos diarios y estacionales para las variables meteorológicas velocidad del viento,

dirección del viento y temperatura.

5.6.1.1.1 Velocidad y Dirección del Viento

A continuación, desde la Figura 5-37 a la Figura 5-39, se muestra una comparación entre los

resultados de los ciclos diarios y estacionales de la velocidad y dirección del viento

observados y modelados, además del histograma de frecuencias de direcciones de viento,

para así determinar la incertidumbre de dichas variables de manera cualitativa.

En la Figura 5-37 se puede observar que el modelo calcula de manera apropiada el

incremento de velocidad en el período diurno, así como la disminución de la magnitud de

esta variable durante la noche. Sin perjuicio de lo anterior, es posible identificar una

sobrestimación de la velocidad del viento por parte del modelo para el ciclo diario,

especialmente durante el periodo diurno, alcanzando una máxima de 6 m/s, mientras que

la máxima observada es de aproximadamente 4 m/s. Además, se observa una mayor

dispersión de los valores durante el periodo diurno en comparación a los valores

observados por la estación meteorológica.

www.dfmconsultores.cl

65

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-37. Comparación de Ciclos Diarios de Velocidad del Viento. Enero a diciembre de 2021. Estación Tierra Amarilla.**

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia.

En la Figura 5-38 se observa que el modelo realiza una aproximación razonable de la dirección de origen de los vientos a lo largo del

día, presentando una mayor exactitud durante el periodo nocturno y de madrugada, no obstante, se identifican sobreestimaciones y

subestimaciones de las frecuencias de los vientos a lo largo del ciclo, como por ejemplo un incremento del porcentaje de vientos en

dirección sur (S) durante la madrugada, así como también una disminución de la frecuencia de los vientos en dirección nornoreste

(NNE) durante el mismo periodo.

www.dfmconsultores.cl

66

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-38. Comparación de Ciclos Diarios de Dirección del Viento. Enero a diciembre de 2021. Estación Tierra Amarilla.**

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia.

En la Figura 5-39 se observa que el modelo tiende a sobreestimar la magnitud de la velocidad del viento tanto en periodo diurno como

nocturno, sin embargo, los valores asociados para el periodo nocturno y de madrugada presentar una mayor aproximación a los valores

observados por la estación en comparación a los valores asociados para el periodo diurno. En cuanto a la dirección del viento, se

aprecia que el modelo presenta una buena aproximación el ciclo diario asociado a los meses de mayo a agosto, mientras que, durante

los meses restante, el modelo tiende a representar de manera imprecisa esta variable meteorológica en ciertos periodos del día.

www.dfmconsultores.cl

67

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-39. Comparación de Ciclos Estacionales de Velocidad y Dirección del Viento. Enero a diciembre de 2021. Estación Tierra Amarilla.**

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia.

5.6.1.1.2 Temperatura

A continuación, con el fin de comparar los resultados de la meteorología observada y modelada en las distintas horas del día y a lo

largo del año, en la Figura 5-40 y Figura 5-41 se presenta una comparación de los ciclos diarios y estacionales, observados y modelados,

presentados en los incisos anteriores para la variable temperatura.

www.dfmconsultores.cl

68

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-40. Comparación de Ciclos Diarios de Temperatura. Enero a diciembre de 2021. Estación Tierra Amarilla.**

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia.

De acuerdo con las figuras anteriores, se puede apreciar que el modelo tiende a sobreestimar levemente las temperaturas en periodo

nocturno, pues la temperatura mínima indicada por el modelo alcanza un valor de 4,3°C aproximadamente, mientras que los registros

observados indican temperaturas mínimas de aproximadamente 1,7°C. En cambio, para el periodo diurno, el modelo representa de

manera adecuada el incremento de temperatura, así como también las máximas temperaturas registras por la estación de monitoreo.

www.dfmconsultores.cl

69

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-41. Comparación de Ciclos Estacionales de Temperatura. Enero a diciembre de 2021. Estación Tierra Amarilla.**

|Observado|Modelado|
|---|---|
|||

Fuente: Elaboración propia.

De acuerdo con los ciclos estacionales presentados, se puede apreciar que el modelo sobrestima las temperaturas correspondientes

al periodo nocturno comprendido entre las 21:00 y 8:00, en cambio, aquellas presentes en el periodo diurno son representadas de

manera adecuada, específicamente las temperaturas correspondientes al periodo entre las 12:00 y 16:00 horas. En consecuencia, es

posible establecer que, el modelo representa de manera adecuada la variación de las temperaturas durante los ciclos diarios y anuales.

www.dfmconsultores.cl

70

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.6.1.2 Comparación cuantitativa

A modo de establecer una comparación cuantitativa entre los registros de meteorología

observada en la estación Tierra Amarilla y aquellos generados mediante el modelo

meteorológico WRF, en primera instancia, en la siguiente tabla se presentan los valores

promedios, mínimos y máximos de velocidad del viento y temperatura correspondientes a

ambos conjuntos de datos.

**Tabla 5-15. Comparación Registros de Velocidad del Viento y Temperatura Observadas y Modeladas.**

**Enero a diciembre de 2021. Estación Tierra Amarilla.**

|Parámetro|Velocidad del Viento [m/s]|Col3|Temperatura [°C]|Col5|
|---|---|---|---|---|
|**Parámetro**|**Observada**|**Modelada**|**Observada**|**Modelada**|
|Promedio|2,33|3,40|16,23|17,94|
|Máximo|5,43|11,30|34,70|33,97|
|Mínimo|0,03|0,03|1,74|4,31|
|Datos disponibles [%]|99,59%|100,00%|99,61%|100,00%|

Fuente: Elaboración propia.

Por otro lado, a continuación, se presentan los estadígrafos utilizados para la evaluación de

la _performance_ del modelo meteorológico, los cuales corresponden a: sesgo (error medio o

BIAS), error absoluto medio (MAE), raíz del error cuadrático medio (RMSE) y coeficiente de

correlación (r). Estos han sido aplicados para el análisis de las series de tiempo y ciclos

diarios de las variables velocidad del viento y temperatura observadas y modeladas.

De este modo, en la Tabla 5-16 se presentan los resultados de estadígrafos mencionados

para las variables en estudio.

**Tabla 5-16. Estadígrafos de Dispersión de Velocidad del Viento y Temperatura. Estación Tierra Amarilla.**

|Medida de Error|Velocidad del Viento|Col3|Temperatura|Col5|
|---|---|---|---|---|
|**Medida de Error**|**Serie de Tiempo**|**Ciclo Diario**|**Serie de Tiempo**|**Ciclo Diario**|
|BIAS|1,064|1,089|1,695|1,830|
|MAE|1,427|1,093|2,512|1,830|
|RMSE|1,915|1,451|3,334|1,983|
|r|0,764|0,983|0,895|0,994|

Fuente: Elaboración propia.

Conforme a los valores de dispersión presentados en la tabla anterior, se observa que el

modelo representa de manera aceptable las series de valores de las variables velocidad del

viento y temperatura, pues los coeficientes de correlación resultantes para ambas variables,

www.dfmconsultores.cl

71

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

76,4% y 89,5% respectivamente, indican una buena aproximación del modelo para

representar los registros observados de estas variables meteorológicas.

No obstante, considerando los valores de MAE, RMSE y especialmente de BIAS obtenidos,

se puede establecer que el modelo presenta una sobreestimación de los registros

monitoreados en la estación Tierra Amarilla, incrementando las velocidades de viento en

1,064 m/s en promedio y las temperaturas en 1,695 °C en promedio.

Mientras que, respecto a las medidas de dispersión presentadas para los valores de ciclos

diarios de las variables velocidad del viento y temperatura, es posible establecer que el

modelo representa de muy buena manera el comportamiento de ambas variables

meteorológicas durante el periodo en estudio, pues los coeficientes de correlación

resultantes superan el 98% de aproximación en ambos casos.

Sin embargo, considerando los valores de MAE, RMSE y principalmente de BIAS, se puede

identificar una sobreestimación por parte del modelo meteorológico para la representación

de los ciclos diarios observados en la estación de monitoreo, aumentando los valores de

velocidad del viento en 1,089 m/s en promedio y de temperatura en 1,830°C en promedio

igualmente.

Por otro lado, de acuerdo con los valores recomendados en la “Guía para el Uso de Modelos

de Calidad del Aire en el SEIA” (Servicio de Evaluación Ambiental, 2023) para los

estadígrafos de dispersión estudiados con anterioridad para todo el territorio nacional,

específicamente para las variables de velocidad del viento, medida a 10 metros sobre el

suelo, y temperatura, medida a 2 metros sobre el suelo, a continuación, se presenta una

comparación entre los valores obtenidos mediante el análisis de incertidumbre del modelo

meteorológico WRF 2021 y los valores recomendados por la guía mencionada.

**Tabla 5-17. Estadígrafos de Dispersión de Velocidad del Viento y Temperatura. Estación Tierra Amarilla.**

|Medida de Error|Velocidad del Viento|Col3|Temperatura|Col5|
|---|---|---|---|---|
|**Medida de Error**|**WRF 2021**|**Guía 2023**|**WRF 2021**|**Guía 2023**|
|BIAS|1,064|[-2,5;2,5]|1,695|[-4;4]|
|MAE|1,427|≤ 3|2,512|≤ 4|
|RMSE|1,915|≤ 3,5|3,334|≤ 4,5|
|r|0,764|> 0,6|0,895|> 0,8|

Fuente: Elaboración propia.

www.dfmconsultores.cl

72

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Tal como se observa en la tabla anterior, los valores resultantes para el cálculo de los

estadígrafos indicados en ambas variables meteorológicas se encuentran dentro de los

rangos recomendados por el organismo público, por lo que, es posible establecer que el

modelo meteorológico WRF permite representar de manera adecuada las condiciones de

las variables meteorológicas de superficie y, por tanto, puede ser ingresado como archivo

de entrada en la modelación de dispersión de contaminantes, específicamente en el

software CALPUFF.

#### 5.7 Normativa de Calidad del Aire y Valores de Referencia

En Tabla 5-18 se presenta la normativa de calidad del aire de los contaminantes de interés

para el Proyecto, los cuales corresponden a: material particulado respirable fino (MP2.5),

material particulado respirable (MP10), material particulado sedimentable (MPS), dióxido

de nitrógeno (NO 2 ), dióxido de azufre (SO 2 ) y monóxido de carbono (CO).

Para el caso del material particulado sedimentable, ante la ausencia de una norma de

calidad nacional aplicable para la zona del Proyecto, se evaluará el cumplimiento de los

valores obtenidos a través de la utilización de una norma de referencia, de acuerdo con lo

establecido en el Reglamento de Evaluación Ambiental. En consecuencia, se considerará la

norma de referencia de la Confederación Suiza y de la República de Argentina para el

análisis de este contaminante.

**Tabla 5-18. Normas de Calidad del Aire.**

|Contaminante|Decreto Aplicable|Norma|Col4|Periodo de Evaluación de<br>Cumplimiento de Norma|
|---|---|---|---|---|
|**Contaminante**|**Decreto Aplicable**|**Valor**|**Unidad**|**Unidad**|
|Material particulado<br>respirable fino (MP2.5)|Decreto Supremo<br>N°12/2011|50|μg/m3|Percentil 98 de la media aritmética<br>diaria durante un año.|
|Material particulado<br>respirable fino (MP2.5)|Decreto Supremo<br>N°12/2011|20|20|Media aritmética trianual|
|Material particulado<br>respirable (MP10)|Decreto Supremo<br>N°12/2021|130|μg/m3N|Percentil 98 de la media aritmética<br>diaria durante un año.|
|Material particulado<br>respirable (MP10)|Decreto Supremo<br>N°12/2021|50|50|Media aritmética trianual.|
|Material particulado<br>sedimentable (MPS)|Norma de referencia<br>Confederación Suiza,<br>Recursos Naturales|200|mg/m2-día|Media aritmética anual|
|Material particulado<br>sedimentable (MPS)|República de Argentina|333|mg/m2-día|Media aritmética mensual|
|Dióxido de nitrógeno<br>(NO2)|Decreto Supremo<br>N°114/2002|400|μg/m3N|Percentil 99 de la media aritmética<br>horaria durante un año.|
|Dióxido de nitrógeno<br>(NO2)|Decreto Supremo<br>N°114/2002|100|100|Media aritmética trianual.|
|Dióxido de azufre (SO2)|Decreto Supremo<br>N°104/2019|350|μg/m3N|Percentil 98,5 de las concentraciones<br>de 1 hora.|
|Dióxido de azufre (SO2)|Decreto Supremo<br>N°104/2019|150|150|Percentil 99 de las concentraciones de<br>24 horas|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

73

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Contaminante|Decreto Aplicable|Norma|Col4|Periodo de Evaluación de<br>Cumplimiento de Norma|
|---|---|---|---|---|
|**Contaminante**|**Decreto Aplicable**|**Valor**|**Unidad**|**Unidad**|
|**Contaminante**|**Decreto Aplicable**|60||Concentración anual|
|Monóxido de carbono<br>(CO)|Decreto Supremo<br>N°115/2002|30|mg/m3N|Percentil 99 de la media aritmética<br>horaria durante un año.|
|Monóxido de carbono<br>(CO)|Decreto Supremo<br>N°115/2002|10|10|Percentil 99 de la media aritmética de 8<br>horas durante un año.|

Fuente: Elaboración propia.

#### 5.8 Línea de Base de Calidad del Aire

A continuación, se describe la línea base de material particulado en sus distintas fracciones

de acuerdo con los registros disponibles en las estaciones de monitoreo cercanas a las

inmediaciones del Proyecto en evaluación.

5.8.1 Línea de Base Medida

5.8.1.1 Estaciones de Monitoreo

Las estaciones de monitoreo con la que se cuenta información pública actualizada

disponible en la zona del Proyecto, con datos correspondientes al periodo de enero 2020 a

diciembre de 2022, corresponden a las estaciones Tierra Amarilla, Ojanco, Luis Uribe, Kozan,

COEMIN, Nantoco, C5, C6, C8, C2, C1, C3 y C7.

La información utilizada para la caracterización de calidad del aire fue obtenida a partir de

los datos disponibles en el Sistema Nacional de Información de Fiscalización Ambiental

(SNIFA) [2], particularmente de los documentos de monitoreo de calidad del aire

correspondientes a las unidades fiscalizables Compañía Contractual Minera Candelaria,

Sociedad Contractual Minera Atacama Kozan y Compañía Exploradora y Explotadora de

Minas Chileno-rumana (COEMIN).

Cabe señalar que, las estaciones Nantoco, C5, C6, C8, C2, C1, C3 y C7 se han incorporado en

el presente estudio de manera referencial ante la periodicidad de muestreo del

contaminante, pues los registros disponibles corresponden a mediciones trimestrales.

A continuación, en la Tabla 5-19 se presentan las coordenadas geográficas, contaminantes

medidos y periodo de medición para cada una de las estaciones de monitoreo mencionadas.

2 [Link web: https://snifa.sma.gob.cl/](https://snifa.sma.gob.cl/)

www.dfmconsultores.cl

74

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Tabla 5-19. Caracterización de Estación de Monitoreo de Calidad del Aire.**

|Estación de<br>Monitoreo|Coordenadas UTM<br>(Datum WGS84)|Col3|Contaminantes medidos|Periodo de Datos<br>Disponibles|
|---|---|---|---|---|
|**Estación de**<br>**Monitoreo**|**Este (m)**|**Norte (m)**|**Norte (m)**|**Norte (m)**|
|Tierra Amarilla|374.932|6.960.241|• Material particulado respirable (MP10)<br>• Material particulado respirable fino (MP2.5)<br>• Material particulado sedimentable (MPS)|Enero de 2020 a<br>diciembre de 2022|
|Ojanco|374.757|6.958.891|• Material particulado respirable (MP10)<br>• Material particulado respirable fino (MP2.5)|Enero de 2020 a<br>diciembre de 2022|
|Luis Uribe|374.942|6.961.596|• Material particulado respirable (MP10)<br>• Material particulado respirable fino (MP2.5)|Enero de 2020 a<br>diciembre de 2022|
|Kozan|375.065|6.956.287|• Material particulado respirable (MP10)|Enero de 2020 a<br>diciembre de 2022|
|COEMIN|377.146|6.949.777|• Material particulado respirable (MP10)|Enero de 2020 a<br>diciembre de 2022|
|Nantoco|374.903|6.952.384|• Material particulado respirable (MP10)|Enero de 2020 a<br>octubre de 2022|
|C5|375.723|6.949.811|• Material particulado respirable (MP10)|Enero de 2020 a<br>octubre de 2022|
|C6|375.453|6.950.426|• Material particulado respirable (MP10)|Enero de 2020 a<br>octubre de 2022|
|C8|375.345|6.950.895|• Material particulado respirable (MP10)|Enero de 2020 a<br>octubre de 2022|
|C2|377.121|6.946.865|• Material particulado respirable (MP10)|Enero de 2020 a<br>octubre de 2022|
|C1|377.154|6.947.080|• Material particulado respirable (MP10)|Enero de 2020 a<br>octubre de 2022|
|C3|376.995|6.946.944|• Material particulado respirable (MP10)|Enero de 2020 a<br>octubre de 2022|
|C7|375.348|6.950.777|• Material particulado respirable (MP10)|Enero de 2020 a<br>octubre de 2022|

Fuente: Elaboración propia.

Por otro lado, en la Figura 5-42 se muestra la ubicación de las estaciones de monitoreo de

calidad del aire con respecto a la zona de emplazamiento del Proyecto.

www.dfmconsultores.cl

75

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-42. Ubicación Referencial Estaciones de Monitoreo de Calidad del Aire.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

76

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.8.1.2 Resumen Línea de Base de Calidad del Aire

A continuación, en la Tabla 5-20 se presenta el resumen de la línea de base de calidad del

aire correspondiente al periodo de datos disponibles en las estaciones analizadas.

**Tabla 5-20. Resumen Línea de Base de Calidad del Aire.**

|Estación|Contaminante|MP10|Col4|MP2.5|Col6|MPS|Col8|
|---|---|---|---|---|---|---|---|
|**Estación**|**Estadígrafo**|**P98 24**<br>**horas**|**Media**<br>**anual**|**P98 24**<br>**horas**|**Media**<br>**anual**|**Media**<br>**mensual**|**Media**<br>**anual**|
|**Estación**|**Norma**|**130**|**50**|**50**|**20**|**333**|**200**|
|**Estación**|**Unidad**|**μg/m3N **|**μg/m3N **|**μg/m3 **|**μg/m3 **|**mg/m2día**|**mg/m2día**|
|Tierra Amarilla|Valor|123,4|55,9|31,0|14,1|356,0|226,8|
|Tierra Amarilla|% Norma|94,9%|111,8%|62,0%|70,5%|106,9%|113,4%|
|Ojanco|Valor|72,0|46,0|15,0|9,6|||
|Ojanco|% Norma|55,4%|92,0%|30,0%|48,0%|||
|Luis Uribe|Valor|74,0|49,0|14,0|8,7|||
|Luis Uribe|% Norma|56,9%|98,0%|28,0%|43,5%|||
|Kozan|Valor|73,1|45,8|||||
|Kozan|% Norma|56,2%|91,6%|||||
|COEMIN|Valor|96,0|45,8|||||
|COEMIN|% Norma|73,8%|91,6%|||||
|Nantoco|Valor|103,0|64,5|||||
|Nantoco|% Norma|79,2%|129,0%|||||
|C5|Valor|54,0|39,5|||||
|C5|% Norma|41,5%|79,0%|||||
|C6|Valor|62,0|50,8|||||
|C6|% Norma|47,7%|101,6%|||||
|C8|Valor|52,0|36,8|||||
|C8|% Norma|40,0%|73,6%|||||
|C2|Valor|59,0|53,8|||||
|C2|% Norma|45,4%|107,6%|||||
|C1|Valor|57,0|51,3|||||
|C1|% Norma|43,8%|102,6%|||||
|C3|Valor|61,0|53,2|||||
|C3|% Norma|46,9%|106,4%|||||
|C7|Valor|63,0|52,7|||||
|C7|% Norma|48,5%|105,4%|||||

Fuente: Elaboración propia.

De la tabla resumen presentada, es posible apreciar que, de acuerdo con la información

disponible en las estaciones de monitoreo Tierra Amarilla, Ojanco y Luis Uribe, el percentil

98 de las concentraciones diarias y la concentración media anual de material particulado

www.dfmconsultores.cl

77

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

respirable (MP2.5) correspondiente al trienio 2020-2022 se presentan por bajo los límites

de las normativas asociadas, por lo que se descarta una condición de saturación e inclusive

de latencia para este contaminante durante el periodo analizado.

Por otro lado, en cuanto a material particulado respirable (MP10), conforme a la

información disponible en las estaciones de monitoreo Ojanco, Luis Uribe, Kozan y COEMIN,

se puede observar que el percentil 98 de las concentraciones diarias y la concentración

media anual de este contaminante se encuentran por bajo los niveles permitidos por las

normas respectivas, no obstante, la concentración media anual se encuentra por sobre el

umbral de latencia [3] .

En cambio, conforme a los registros de monitoreo en la estación Tierra Amarilla, se puede

apreciar que el percentil 98 de las concentraciones diarias se representa por sobre el 90%

de la norma respectiva, mientras que la concentración media anual se encuentra por sobre

el límite de saturación de este contaminante para este periodo, por lo que es posible

establecer una condición de saturación [4] de MP10 para el periodo comprendido entre enero

de 2020 y diciembre de 2022 en esta estación.

Asimismo, a modo referencial, de acuerdo con los registros de monitoreo de las estaciones

Nantoco, C6, C2, C1, C3 y C7, es posible identificar que la concentración media anual de

material particulado respirable se encuentra por sobre el umbral de saturación establecido

por la normativa respectiva, por lo que se puede establecer una condición de saturación de

este contaminante en periodo anual para el trienio 2020-2022 en las estaciones

mencionadas.

Por otro lado, de acuerdo con los registros de material particulado sedimentable (MPS) en

estación Tierra Amarilla, se puede observar que, las depositaciones mensuales y la media

trianual resultante correspondiente al trienio 2020- 2022 se encuentran por sobre los

límites establecidos por las normativas de referencia de la República de Argentina y de

Confederación Suiza. En consecuencia, es posible establecer una condición de saturación

de este contaminante para el sector circundante a la estación de monitoreo durante el

periodo en estudio.

3 Condición de latencia corresponde a aquella en que la medición de la concentración de contaminantes en el
aire se sitúa entre el 80% y el 100% del valor de la respectiva norma de calidad ambiental.
4 Condición de saturación corresponde a aquella en que la medición de la concentración de contaminantes en
el aire se sitúa por sobre el 100% del valor de la respectiva norma de calidad ambiental.

www.dfmconsultores.cl

78

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.8.2 Línea de Base Proyectada

Con el objetivo de considerar el eventual aporte sinérgico en concentración de

contaminantes atmosféricos presentados por proyectos que se encuentran con una

Resolución de Calificación Ambiental (RCA) favorable y que aún no han iniciado la fase de

construcción, a continuación, en la Tabla 5-21 se presenta un breve análisis de aquellos

proyectos que cumplen con las características mencionadas y se emplazarán en la comuna

de Tierra Amarilla, específicamente durante el periodo comprendido entre los años 2018 y

2023.

www.dfmconsultores.cl

79

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Tabla 5-21. Análisis de otros proyectos dentro del dominio de modelación.**

|Nombre Proyecto|Titular|RCA|Expediente SEIA|Estado SNIFA|Observación|Fuente|
|---|---|---|---|---|---|---|
|Proyecto Minero<br>Tránsito|Sociedad Punta<br>del Cobre S.A.|20230300139/2023|http://seia.sea.gob.cl/expedie<br>nte/ficha/fichaPrincipal.php?i<br>d_expediente=2152997536|Sin Información|Presenta aportes<br>en las estaciones<br>Tierra Amarilla,<br>Ojanco, Luis Uribe<br>y Kozan|https://seia.sea.gob.cl/archivos/2<br>021/08/25/Anexo_2.2_Modelacio<br>n_de_Dispersion_de_Cont_Rev_0<br>.pdf|
|Ampliación Central<br>Desierto de Atacama|Copiapó Solar<br>SpA.|20220300142/2022|http://seia.sea.gob.cl/expedie<br>nte/ficha/fichaPrincipal.php?i<br>d_expediente=2151133877|Sin información|Presenta aportes<br>en estación Tierra<br>Amarilla|https://seia.sea.gob.cl/archivos/2<br>021/03/16/1a9_PHC0025_Anexo_<br>1.7_Modelacion_de_calidad_del_<br>aire_Rev_0.pdf|
|Parque Fotovoltaico<br>Alianza|Parque Solar<br>Alianzas SpA.|72/2021|http://seia.sea.gob.cl/expedie<br>nte/ficha/fichaPrincipal.php?i<br>d_expediente=2146014549|No iniciada la<br>fase de<br>construcción|No presenta<br>modelación de<br>dispersión de<br>contaminantes|https://infofirma.sea.gob.cl/Docu<br>mentosSEA/MostrarDocumento?<br>docId=79/2c/f1fa7f87577e24fe58<br>e9b89d7f6af7c3f97c|
|Transporte de<br>Sustancias Peligrosas|Daniel Ocaña<br>Medina|176/2020|https://seia.sea.gob.cl/expedi<br>ente/ficha/fichaPrincipal.php?<br>modo=ficha&id_expediente=2<br>145507755|Sin información|No presenta<br>modelación de<br>dispersión de<br>contaminantes|https://seia.sea.gob.cl/archivos/2<br>020/01/20/87b_Capitulo_2_Descr<br>ipcion_del_Proyecto.pdf|
|Modificación de la LAT<br>del Proyecto Central<br>Desierto de Atacama|Copiapó Solar<br>SpA|138/2020|https://seia.sea.gob.cl/expedi<br>ente/ficha/fichaPrincipal.php?<br>modo=ficha&id_expediente=2<br>145240380|Sin información|No presenta<br>modelación de<br>dispersión de<br>contaminantes|https://seia.sea.gob.cl/archivos/2<br>019/12/18/Anexo_4_-<br>_Emisiones_Atmosfericas_VERSIO<br>N_SEIA.pdf|
|Transporte terrestre<br>de sustancias<br>corrosivas|Transfahum SpA.|175/2020|https://seia.sea.gob.cl/expedi<br>ente/ficha/fichaPrincipal.php?<br>modo=ficha&id_expediente=2<br>144896397|Sin información|No presenta<br>modelación de<br>dispersión de<br>contaminantes|https://infofirma.sea.gob.cl/Docu<br>mentosSEA/MostrarDocumento?<br>docId=58/88/7a73bb7446509347<br>aa8dd5ddcff815f19cc0|
|Mejoramiento Planta<br>de Tratamiento de<br>Aguas Servidas<br>Localidad Los Loros|Ilustre<br>Municipalidad de<br>Tierra Amarilla|79/2020|https://seia.sea.gob.cl/expedi<br>ente/expedientesEvaluacion.p<br>hp?modo=ficha&id_expedient<br>e=2144135727|Sin información|No presenta<br>aportes en las<br>estaciones<br>estudiadas|http://seia.sea.gob.cl/archivos/20<br>19/09/01/Anexo_Emisiones_Atm<br>osfericas_PTAS_Los_Loros_REV_0<br>.pdf|
|Continuidad<br>Operacional Mina<br>Mantos de Cobre|Sociedad Punta<br>del Cobre S.A.|145/2021|https://seia.sea.gob.cl/expedi<br>ente/ficha/fichaPrincipal.php?<br>modo=ficha&id_expediente=2<br>144075495|No iniciada la<br>fase de<br>construcción|Presenta aportes<br>en las estaciones<br>Tierra Amarilla,<br>Ojanco y Luis Uribe|https://seia.sea.gob.cl/archivos/2<br>019/08/28/190_Cap_2_-<br>_Analisis_Art_11_Rev_1.pdf|

80

www.dfmconsultores.cl

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Nombre Proyecto|Titular|RCA|Expediente SEIA|Estado SNIFA|Observación|Fuente|
|---|---|---|---|---|---|---|
|Exploración Minera La<br>Pepa|Mineros Chile<br>SpA.|62/2020|https://seia.sea.gob.cl/expedi<br>ente/ficha/fichaPrincipal.php?<br>modo=ficha&id_expediente=2<br>143861970|Sin información|No presenta<br>aportes en las<br>estaciones<br>estudiadas|https://seia.sea.gob.cl/archivos/2<br>019/07/26/ac3_Anexo_6.zip|
|Transporte terrestre<br>de sustancias<br>peligrosas|Hilmar SpA.|1061/2019|https://seia.sea.gob.cl/expedi<br>ente/ficha/fichaPrincipal.php?<br>modo=ficha&id_expediente=2<br>142177433|Sin información|No presenta<br>modelación de<br>dispersión de<br>contaminantes|http://seia.sea.gob.cl/archivos/20<br>18/12/27/Anexo_H_Estimacion_E<br>misiones_Atmosfericas.rar|
|Proyecto Vidalita|EMU Chile SpA.|139/2019|https://seia.sea.gob.cl/expedi<br>ente/ficha/fichaPrincipal.php?<br>modo=ficha&id_expediente=2<br>141400807|Sin información|No presenta<br>aportes en las<br>estaciones<br>estudiadas|http://seia.sea.gob.cl/archivos/20<br>18/09/13/Anexo_1_-<br>_Emisiones_y_Calidad_del_Aire.p<br>df|
|Prospección Minera<br>Norte Abierto Sector<br>Caspiche|Compañía<br>Minera Casale<br>SpA.|9/2019|https://seia.sea.gob.cl/expedi<br>ente/ficha/fichaPrincipal.php?<br>modo=ficha&id_expediente=2<br>140858839|No iniciada la<br>fase de<br>construcción|No presenta<br>aportes en las<br>estaciones<br>estudiadas|http://seia.sea.gob.cl/archivos/20<br>18/06/22/Anx_3_Emisiones.zip|

Fuente: Elaboración propia.

A partir de lo expuesto en la tabla precedente, los proyectos a considerar para la elaboración de la línea de base de calidad del aire

proyectada corresponden a los siguientes: “Proyecto Minero Tránsito”, “Ampliación Central Desierto de Atacama” y “Continuidad

Operacional Mina Mantos de Cobre”.

De este modo, en la Tabla 5-22 se presenta la línea de base de calidad del aire proyectada, correspondiente a la suma entre los aportes

de concentración de contaminantes atmosféricos por generar durante el desarrollo de la fase de construcción de los proyectos

mencionados con anterioridad y las concentraciones monitoreadas durante el periodo comprendido entre enero de 2020 y diciembre

de 2022 en las estaciones Tierra Amarilla, Ojanco, Luis Uribe y Kozan, valores presentados en la línea de base de calidad del aire en la

Tabla 5-20.

www.dfmconsultores.cl

81

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Es necesario mencionar que, la línea de base de calidad del aire proyectada es presentada

con el fin de evaluar un escenario más conservador, en donde se realiza el estudio bajo el

supuesto en que los aportes de los proyectos calificados de manera favorable

ambientalmente se desarrollan de manera simultánea al momento del inicio de la ejecución

del presente Proyecto.

**Tabla 5-22. Línea de Base de Calidad del Aire Proyectada.**

|Estación|Contaminante|MP10|Col4|MP2.5|Col6|MPS|Col8|
|---|---|---|---|---|---|---|---|
|**Estación**|**Estadígrafo**|**P98 24**<br>**horas**|**Media**<br>**anual**|**P98 24**<br>**horas**|**Media**<br>**anual**|**Media**<br>**mensual**|**Media**<br>**anual**|
|**Estación**|**Norma**|**130**|**50**|**50**|**20**|**333**|**200**|
|**Estación**|**Unidad**|**μg/m3N **|**μg/m3N **|**μg/m3 **|**μg/m3 **|**mg/m2día**|**mg/m2día**|
|Tierra Amarilla|Valor|125,4|56,4|31,4|14,2|356,0|226,8|
|Tierra Amarilla|% Norma|96,5%|112,7%|62,8%|70,9%|106,9%|113,4%|
|Ojanco|Valor|72,1|46,0|15,0|9,6|||
|Ojanco|% Norma|55,5%|92,0%|30,0%|48,0%|||
|Luis Uribe|Valor|74,2|49,1|14,0|8,7|||
|Luis Uribe|% Norma|57,1%|98,2%|28,0%|43,5%|||
|Kozan|Valor|73,1|45,8|||||
|Kozan|% Norma|56,2%|91,6%|||||

Fuente: Elaboración propia.

De acuerdo con lo expuesto en la tabla anterior, se puede observar que las concentraciones

resultantes para cada estadígrafo de los contaminantes estudiados presentan valores

similares a los obtenidos en la línea de base de calidad del aire expuesta en la sección previa.

Por lo que el percentil 98 de las concentraciones medias diarias y las concentraciones

medias anuales de MP2.5 en las estaciones Tierra Amarilla, Ojanco y Luis Uribe se

mantienen por bajo los límites de las normativas asociadas, así como también el percentil

98 de las concentraciones medias diarias y las concentraciones medias anuales de MP10 en

las estaciones Ojanco, Luis Uribe y Kozan. No obstante, las medias anuales resultantes en

las últimas estaciones mencionadas se mantienen por sobre el umbral de latencia de la

normativa respectiva.

En cambio, las concentraciones de MP10 en periodo diario y anual en la estación Tierra

Amarilla se mantienen por sobre el umbral de latencia y saturación respectivamente

conforme a la normativa vigente de este contaminante.

www.dfmconsultores.cl

82

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Por último, las depositaciones mensuales y media anual resultante en estación Tierra

Amarilla se mantienen por sobre los límites establecidos por las normativas de referencia

de la República de Argentina y Confederación Suiza.

#### 5.9 Escenarios Modelados

Para la modelación de dispersión de contaminantes, específicamente de MP2.5, MP10,

MPS, CO, NO 2 y SO 2, se han considerado las emisiones correspondientes a las fases de

operación actual y proyectada del Proyecto, las que se muestran de manera detallada en el

Anexo 2-1.2 Estimación de Emisiones Atmosféricas del Proyecto “Optimización Operacional

Mina Carola”.

En consecuencia, a continuación, se presenta el detalle de la configuración de cada modelo

de manera independiente, especificando las fuentes emisoras y receptores considerandos,

además de los aportes de concentración y depositación resultantes para cada escenario de

operación.

5.9.1 Fase de Operación Base

5.9.1.1 Fuentes Emisoras

Las fuentes emisoras de la fase de operación base han sido georreferenciadas de acuerdo

con la información proporcionada por la ingeniería del Proyecto, para posteriormente ser

ingresadas al modelo de dispersión de contaminantes.

Por tanto, en la Figura 5-43 se presentan las fuentes emisoras del tipo areal y caminos,

mientras que en la Tabla 5-23 se muestra el detalle de las características de las fuentes y las

tasas de emisión asociadas a cada una.

Cabe destacar que, existen ciertas fuentes en la fase de operación actual de Mina Carola

que no modificarán sus niveles de actividad en la fase de operación futura, particularmente,

los movimientos de tierra asociados al botadero Cobriza y los grupos electrógenos, los

cuales no cambiarán su régimen de operación como tampoco las características de los

equipos, por tanto, no modificarán sus emisiones producto del Proyecto en evaluación, tal

como se muestra en el Anexo 2-1.2. Es por ello que, tales fuentes no han sido consideradas

en la presente modelación, esto ya que no se requieren en la evaluación de la modificación

de las concentraciones ambientales, así como tampoco en la estimación de las

concentraciones y depositaciones totales proyectadas, pues sus aportes ya se ven reflejados

en la línea de base medida.

www.dfmconsultores.cl

83

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-43. Ubicación Fuentes Emisoras. Fase de Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

84

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Tabla 5-23. Características de Fuentes Emisoras y Tasas de Emisión. Fase de Operación Base.**

|ID|Descripción|Tipo de fuente|Tasas de emisión|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Descripción**|**Tipo de fuente**|**MP2.5**|**MP10**|**MPS**|**NO**|**NO2 **|**SO2 **|**CO**|**Unidad**|
|SRC_1|Tramo C1|Camino|2,78 E-07|9,83 E-07|4,90 E-06|1,23 E-06|2,10 E-07|2,29 E-09|5,46 E-07|g/s/m|
|SRC_2|Tramo C2|Camino|1,40 E-06|5,60 E-06|2,89 E-05|1,71 E-06|2,92 E-07|3,06 E-09|7,28 E-07|g/s/m|
|SRC_3|Tramo C3|Camino|1,15 E-06|4,63 E-06|2,39 E-05|1,20 E-06|2,05 E-07|2,07 E-09|4,93 E-07|g/s/m|
|SRC_4|Tramo C4|Camino|8,87 E-08|3,12 E-07|1,56 E-06|3,13 E-07|5,34 E-08|6,53 E-10|1,53 E-07|g/s/m|
|SRC_5|Tramo C5|Camino|1,33 E-06|5,32 E-06|2,75 E-05|1,59 E-06|2,71 E-07|2,80 E-09|6,69 E-07|g/s/m|
|SRC_6|Tramo C6|Camino|2,13 E-06|8,69 E-06|4,51 E-05|1,06 E-06|1,81 E-07|1,82 E-09|4,35 E-07|g/s/m|
|SRC_7|Tramo C7|Camino|8,09 E-07|3,27 E-06|1,69 E-05|7,18 E-07|1,22 E-07|1,24 E-09|2,95 E-07|g/s/m|
|SRC_8|Tramo C9|Camino|8,31 E-07|3,35 E-06|1,74 E-05|7,42 E-07|1,26 E-07|1,28 E-09|3,05 E-07|g/s/m|
|SRC_9|Tramo C10|Camino|8,77 E-07|3,54 E-06|1,83 E-05|8,06 E-07|1,37 E-07|1,39 E-09|3,30 E-07|g/s/m|
|SRC_10|Tramo C11|Camino|5,30 E-08|2,10 E-07|1,08 E-06|8,42 E-08|1,44 E-08|1,44 E-10|3,42 E-08|g/s/m|
|SRC_11|Tramo C12|Camino|6,46 E-07|2,53 E-06|1,30 E-05|1,10 E-06|1,87 E-07|2,01 E-09|4,77 E-07|g/s/m|
|SRC_12|Tramo N1|Camino|6,62 E-07|6,43 E-06|2,61 E-05|4,62 E-07|7,87 E-08|8,79 E-10|2,13 E-07|g/s/m|
|SRC_13|Tramo N2|Camino|6,02 E-07|5,84 E-06|2,37 E-05|4,20 E-07|7,15 E-08|7,99 E-10|1,94 E-07|g/s/m|
|SRC_14|Tramo N3|Camino|2,80 E-07|2,68 E-06|1,09 E-05|2,94 E-07|5,01 E-08|5,36 E-10|1,34 E-07|g/s/m|
|SRC_15|Tramo N4|Camino|1,15 E-06|1,14 E-05|4,63 E-05|4,63 E-07|7,88 E-08|7,96 E-10|1,90 E-07|g/s/m|
|SRC_16|Tramo N5|Camino|1,02 E-06|1,00 E-05|4,08 E-05|4,07 E-07|6,94 E-08|7,00 E-10|1,67 E-07|g/s/m|
|SRC_17|Tramo S1|Camino|2,93 E-06|2,92 E-05|8,45 E-05|2,12 E-07|3,61 E-08|5,78 E-10|1,22 E-07|g/s/m|
|SRC_18|Tramo S2|Camino|3,11 E-06|3,10 E-05|8,96 E-05|2,25 E-07|3,83 E-08|6,13 E-10|1,30 E-07|g/s/m|
|SRC_19|Tramo S3|Camino|7,72 E-06|7,69 E-05|2,23 E-04|7,00 E-07|1,19 E-07|1,20 E-09|2,88 E-07|g/s/m|
|SRC_20|Tramo S4|Camino|2,14 E-05|2,14 E-04|6,18 E-04|1,43 E-06|2,43 E-07|2,87 E-09|6,55 E-07|g/s/m|
|SRC_21|Tramo P1|Camino|2,48 E-08|9,32 E-08|4,73 E-07|8,55 E-08|1,46 E-08|1,47 E-10|3,51 E-08|g/s/m|
|SRC_22|Tramo P2|Camino|2,77 E-08|1,04 E-07|5,28 E-07|9,55 E-08|1,63 E-08|1,64 E-10|3,92 E-08|g/s/m|
|SRC_23|Tramo P3|Camino|2,08 E-07|7,12 E-07|3,51 E-06|9,01 E-07|1,54 E-07|1,88 E-09|4,34 E-07|g/s/m|
|SRC_24|Tramo P4|Camino|2,07 E-07|7,08 E-07|3,49 E-06|8,96 E-07|1,53 E-07|1,87 E-09|4,32 E-07|g/s/m|
|SRC_25|Tramo P5|Camino|1,80 E-07|6,06 E-07|2,97 E-06|8,02 E-07|1,37 E-07|1,71 E-09|3,93 E-07|g/s/m|

www.dfmconsultores.cl

85

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|ID|Descripción|Tipo de fuente|Tasas de emisión|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Descripción**|**Tipo de fuente**|**MP2.5**|**MP10**|**MPS**|**NO**|**NO2 **|**SO2 **|**CO**|**Unidad**|
|SRC_26|Tramo P6|Camino|1,56 E-07|5,34 E-07|2,63 E-06|6,60 E-07|1,13 E-07|1,40 E-09|3,21 E-07|g/s/m|
|SRC_27|Tramo P7|Camino|1,81 E-07|6,20 E-07|3,06 E-06|7,62 E-07|1,30 E-07|1,62 E-09|3,69 E-07|g/s/m|
|SRC_28|Tramo P8|Camino|3,68 E-09|9,56 E-09|4,22 E-08|1,40 E-08|2,38 E-09|5,55 E-11|1,09 E-08|g/s/m|
|SRC_29|Tramo P9|Camino|4,78 E-08|1,74 E-07|8,77 E-07|1,76 E-07|3,00 E-08|3,34 E-10|7,71 E-08|g/s/m|
|SRC_30|Tramo P10|Camino|1,05 E-07|3,59 E-07|1,77 E-06|3,88 E-07|6,61 E-08|9,18 E-10|2,01 E-07|g/s/m|
|SRC_31|Tramo P11|Camino|4,69 E-08|1,60 E-07|7,90 E-07|2,18 E-07|3,71 E-08|4,33 E-10|1,02 E-07|g/s/m|
|SRC_32|Carola Norte|Área|1,31 E-07|3,12 E-07|5,50 E-07|9,76 E-07|1,66 E-07|4,33 E-09|5,44 E-06|g/s/m2|
|SRC_33|Carola Central|Área|8,22 E-06|1,44 E-05|5,93 E-05|6,10 E-06|1,04 E-06|2,66 E-08|1,03 E-05|g/s/m2|

Fuente: Elaboración propia.

www.dfmconsultores.cl

86

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.1.2 Receptores de Interés

Para la evaluación del aporte de las emisiones atmosféricas del Proyecto, se han definido

dos grillas de receptores, la primera con resolución de 37.000 x 43.000 m con espaciado

cada 1.000 m y la segunda, correspondiente a una grilla anidada, con resolución de 3.500 x

3.500 m con espaciado cada 500 m en el sector Carola Norte, más una resolución de 8.500

x 8.500 m con espaciado cada 500 m en el sector Carola Centro y una resolución de 5.000 x

4.500 m con espaciado cada 500 m en el sector Carola Sur.

De este modo, la primera grilla abarca gran parte del dominio de modelación, procurando

contender todas las fuentes emisoras mencionadas con anterioridad, mientras que la

segunda se centraliza en las distintas áreas de trabajo de Mina Carola.

A modo complementario, se han considerado 35 receptores discretos, los cuales

representan puntos de interés tales como: medio humano y estaciones de monitoreo. La

ubicación de tales puntos se muestra de manera detallada en la Tabla 5-24.

**Tabla 5-24. Receptores de Interés. Fase de Operación Base.**

|ID|Receptor|Coordenadas [Datum WGS84]|Col4|Elevación<br>[m.s.n.m.]|
|---|---|---|---|---|
|**ID**|**Receptor**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|R_1|Estación Luis Uribe|374.942|6.961.596|514,30|
|R_2|Estación Tierra Amarilla|374.904|6.960.235|521,39|
|R_3|Estación Ojanco|374.772|6.958.885|513,93|
|R_4|Estación Kozan|375.076|6.956.263|568,74|
|R_5|133 casa (Carola Norte)|375.842|6.961.206|561,91|
|R_6|Iglesia Tierra Amarilla|375.270|6.961.216|518,20|
|R_7|El Minero|375.114|6.958.078|540,49|
|R_8|Testigoteca|375.054|6.957.920|541,09|
|R_9|Estadio|375.353|6.956.715|573,60|
|R_10|Agrouva I|375.347|6.956.543|567,13|
|R_11|Agrouva II|375.370|6.956.345|551,88|
|R_12|Receptor ruido (viviendas 1 piso, material mixto)|375.021|6.958.033|539,80|
|R_13|Receptor ruido (viviendas 1 piso, material ligero)|375.005|6.957.965|540,10|
|R_14|Receptor ruido (viviendas 1 piso, material ligero)|374.966|6.957.769|542,55|
|R_15|Receptor ruido (Oficinas, galpones y container, material<br>mixto)|375.215|6.957.683|554,95|
|R_16|Receptor ruido (Vivienda 2 pisos, material ligero)|375.126|6.957.573|558,76|
|R_17|Receptor ruido (Viviendas 1 y 2 pisos, material ligero)|375.093|6.957.335|555,04|

www.dfmconsultores.cl

87

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|ID|Receptor|Coordenadas [Datum WGS84]|Col4|Elevación<br>[m.s.n.m.]|
|---|---|---|---|---|
|**ID**|**Receptor**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|R_18|Receptor ruido (Viviendas 1 y 2 pisos, material mixto)|375.248|6.957.084|566,44|
|R_19|Receptor ruido (Viviendas 1 y 2 pisos, material ligero)|375.278|6.956.755|573,88|
|R_20|Receptor ruido (Viviendas 1 piso, material ligero)|375.476|6.956.834|575,09|
|R_21|Receptor ruido (Vivienda 1 piso, material ligero)|375.633|6.956.813|584,48|
|R_22|Receptor ruido (Viviendas 1 y 2 pisos, material ligero)|375.105|6.956.579|575,38|
|R_23|Receptor ruido (Oficinas Empresa Agrícola Uvas del Norte,<br>ubicada frente a Planta Cerrillos- COEMIN)|377.121|6.949.607|642,08|
|R_24|Receptor ruido (Km 21 Carretera C-35. Entrada Fundo<br>Alianza Agricultura)|376.866|6.948.610|631,11|
|R_25|Receptor ruido (Km 21 Carretera C-35. Frente a casa-<br>almacén)|376.669|6.946.880|627,97|
|R_26|Receptor ruido (Punto ubicado a 5 k. Planta Cerrillos, por<br>carretera C-35, localidad de Nantoco)|374.539|6.953.171|552,36|
|R_27|Estación COEMIN|377.146|6.949.777|640,22|
|R_28|Estación Nantoco|374.903|6.952.384|575,29|
|R_29|Estación C6|375.453|6.950.426|599,45|
|R_30|Estación C5|375.723|6.949.811|616,72|
|R_31|Estación C8|375.345|6 950 895|595,90|
|R_32|Estación C2|377.121|6.946.865|644,54|
|R_33|Estación C1|377.154|6.947.080|643,66|
|R_34|Estación C3|376.995|6.946.944|633,39|
|R_35|Estación C7|375.348|6.950.777|603,95|

Fuente: Elaboración propia.

A continuación, en la Figura 5-44 se presentan las grillas de receptores utilizadas, mientras

que en la Figura 5-45 se muestran los receptores de interés considerados en la modelación

de dispersión de contaminantes.

www.dfmconsultores.cl

88

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-44. Ubicación Grilla de Receptores. Fase de Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

89

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-45. Ubicación de Receptores de Interés. Fase de Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

90

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.1.3 Resultados de Modelación

A continuación, en los siguientes apartados se presentan los resultados de la modelación

de dispersión de contaminantes realizada para la fase de operación actual o base del

Proyecto “Optimización Operacional Mina Carola”, considerando un tiempo de desarrollo

de 12 meses.

Para ello, se muestran las concentraciones aportadas por el Proyecto, para cada uno de los

contaminantes considerados en el estudio, sobre los receptores de interés mencionados

con anterioridad, realizando un análisis normativo de cada uno de los estadígrafos indicados

por las normativas y valores de referencia señalados en la sección 5.7.

Además, a modo complementario, se presentan las curvas de isoconcentración e

isodepositación, según corresponde, conforme a las concentraciones y depositaciones

obtenidas y percibidas en el dominio de modelación.

www.dfmconsultores.cl

91

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.1.3.1 Material Particulado Respirable Fino (MP2.5)

En la Tabla 5-25 se presentan los aportes generados durante la fase de operación actual del

Proyecto sobre los receptores de interés, específicamente sobre receptores de medio

humano y estaciones de monitoreo, conforme con la norma primaria para material

particulado respirable fino (MP2.5).

**Tabla 5-25. Resultados del modelo de dispersión para MP2.5 [μg/m** **[3]** **]. Fase de Operación Base.**

|Receptor|Descripción|Material Particulado Respirable Fino (MP2.5)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3] **|**Concentración [μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|0,785|0,378|50|20|1,6%|1,9%|
|R_2|Estación Tierra Amarilla|1,334|0,655|0,655|0,655|2,7%|3,3%|
|R_3|Estación Ojanco|1,159|0,438|0,438|0,438|2,3%|2,2%|
|R_4|Estación Kozan|2,660|0,634|0,634|0,634|5,3%|3,2%|
|R_5|133 casa (Carola Norte)|0,679|0,309|0,309|0,309|1,4%|1,5%|
|R_6|Iglesia Tierra Amarilla|1,031|0,518|0,518|0,518|2,1%|2,6%|
|R_7|El Minero|3,801|1,127|1,127|1,127|7,6%|5,6%|
|R_8|Testigoteca|2,329|0,632|0,632|0,632|4,7%|3,2%|
|R_9|Estadio|7,671|2,135|2,135|2,135|15,3%|10,7%|
|R_10|Agrouva I|4,637|1,357|1,357|1,357|9,3%|6,8%|
|R_11|Agrouva II|1,711|0,722|0,722|0,722|3,4%|3,6%|
|R_12|Receptor ruido|2,333|0,656|0,656|0,656|4,7%|3,3%|
|R_13|Receptor ruido|2,146|0,566|0,566|0,566|4,3%|2,8%|
|R_14|Receptor ruido|1,769|0,492|0,492|0,492|3,5%|2,5%|
|R_15|Receptor ruido|4,868|1,516|1,516|1,516|9,7%|7,6%|
|R_16|Receptor ruido|5,586|1,709|1,709|1,709|11,2%|8,5%|
|R_17|Receptor ruido|3,362|0,989|0,989|0,989|6,7%|4,9%|
|R_18|Receptor ruido|19,729|3,888|3,888|3,888|39,5%|19,4%|
|R_19|Receptor ruido|9,288|2,345|2,345|2,345|18,6%|11,7%|
|R_20|Receptor ruido|10,184|2,854|2,854|2,854|20,4%|14,3%|
|R_21|Receptor ruido|8,725|2,602|2,602|2,602|17,5%|13,0%|
|R_22|Receptor ruido|5,607|1,090|1,090|1,090|11,2%|5,4%|
|R_23|Receptor ruido|0,264|0,068|0,068|0,068|0,5%|0,3%|
|R_24|Receptor ruido|0,180|0,060|0,060|0,060|0,4%|0,3%|
|R_25|Receptor ruido|0,101|0,039|0,039|0,039|0,2%|0,2%|
|R_26|Receptor ruido|0,263|0,119|0,119|0,119|0,5%|0,6%|
|R_27|Estación COEMIN|0,273|0,069|0,069|0,069|0,5%|0,3%|
|R_28|Estación Nantoco|0,284|0,124|0,124|0,124|0,6%|0,6%|

www.dfmconsultores.cl

92

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Material Particulado Respirable Fino (MP2.5)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3] **|**Concentración [μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_29|Estación C6|0,218|0,085|||0,4%|0,4%|
|R_30|Estación C5|0,189|0,073|0,073|0,073|0,4%|0,4%|
|R_31|Estación C8|0,246|0,099|0,099|0,099|0,5%|0,5%|
|R_32|Estación C2|0,109|0,042|0,042|0,042|0,2%|0,2%|
|R_33|Estación C1|0,116|0,044|0,044|0,044|0,2%|0,2%|
|R_34|Estación C3|0,109|0,042|0,042|0,042|0,2%|0,2%|
|R_35|Estación C7|0,238|0,096|0,096|0,096|0,5%|0,5%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes actuales del Proyecto sobre los

receptores de interés alcanzan un máximo de 39,5% y 20,4% de la norma de este

contaminante en periodo diario, específicamente sobre los receptores denominados

“R_18” y “R_20”, los que corresponden a viviendas construidas con material mixto y

material ligero respectivamente. Por su parte, en cuanto a los aportes actuales de MP2.5

estimados para periodo anual, estos representan hasta un 19,4% y 14,3% de la normativa

respectiva, particularmente en los receptores indicados con anterioridad.

A continuación, en las siguientes figuras se presentan las curvas de isoconcentración de

material particulado respirable fino (MP2.5) para periodo de 24 horas y periodo anual.

www.dfmconsultores.cl

93

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-46. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP2.5 [μg/m** **[3]** **]. Fase de**

**Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

94

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-47. Curvas de isoconcentración para periodo anual. MP2.5 [μg/m** **[3]** **]. Fase de Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

95

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.1.3.2 Material Particulado Respirable (MP10)

En la Tabla 5-26 se presentan los aportes generados durante la fase de operación actual del

Proyecto sobre los receptores de interés, específicamente sobre receptores de medio

humano y estaciones de monitoreo, conforme con la norma primaria para material

particulado respirable (MP10).

**Tabla 5-26. Resultados del modelo de dispersión para MP10 [μg/m** **[3]** **N]. Fase de Operación Base.**

|Receptor|Descripción|Material Particulado Respirable (MP10)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|1,486|0,726|130|50|1,1%|1,5%|
|R_2|Estación Tierra Amarilla|2,453|1,231|1,231|1,231|1,9%|2,5%|
|R_3|Estación Ojanco|2,162|0,849|0,849|0,849|1,7%|1,7%|
|R_4|Estación Kozan|4,893|1,365|1,365|1,365|3,8%|2,7%|
|R_5|133 casa (Carola Norte)|1,798|0,943|0,943|0,943|1,4%|1,9%|
|R_6|Iglesia Tierra Amarilla|2,061|1,044|1,044|1,044|1,6%|2,1%|
|R_7|El Minero|6,692|2,140|2,140|2,140|5,1%|4,3%|
|R_8|Testigoteca|4,241|1,259|1,259|1,259|3,3%|2,5%|
|R_9|Estadio|16,952|5,678|5,678|5,678|13,0%|11,4%|
|R_10|Agrouva I|9,619|3,405|3,405|3,405|7,4%|6,8%|
|R_11|Agrouva II|3,315|1,483|1,483|1,483|2,6%|3,0%|
|R_12|Receptor ruido|4,217|1,327|1,327|1,327|3,2%|2,7%|
|R_13|Receptor ruido|3,895|1,139|1,139|1,139|3,0%|2,3%|
|R_14|Receptor ruido|3,143|1,010|1,010|1,010|2,4%|2,0%|
|R_15|Receptor ruido|8,705|2,915|2,915|2,915|6,7%|5,8%|
|R_16|Receptor ruido|10,061|3,176|3,176|3,176|7,7%|6,4%|
|R_17|Receptor ruido|6,276|1,941|1,941|1,941|4,8%|3,9%|
|R_18|Receptor ruido|33,660|7,185|7,185|7,185|25,9%|14,4%|
|R_19|Receptor ruido|21,222|7,049|7,049|7,049|16,3%|14,1%|
|R_20|Receptor ruido|19,096|6,305|6,305|6,305|14,7%|12,6%|
|R_21|Receptor ruido|17,324|6,435|6,435|6,435|13,3%|12,9%|
|R_22|Receptor ruido|10,656|2,465|2,465|2,465|8,2%|4,9%|
|R_23|Receptor ruido|0,482|0,138|0,138|0,138|0,4%|0,3%|
|R_24|Receptor ruido|0,352|0,119|0,119|0,119|0,3%|0,2%|
|R_25|Receptor ruido|0,200|0,077|0,077|0,077|0,2%|0,2%|
|R_26|Receptor ruido|0,534|0,240|0,240|0,240|0,4%|0,5%|
|R_27|Estación COEMIN|0,521|0,139|0,139|0,139|0,4%|0,3%|
|R_28|Estación Nantoco|0,546|0,251|0,251|0,251|0,4%|0,5%|

www.dfmconsultores.cl

96

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Material Particulado Respirable (MP10)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_29|Estación C6|0,426|0,172|||0,3%|0,3%|
|R_30|Estación C5|0,371|0,147|0,147|0,147|0,3%|0,3%|
|R_31|Estación C8|0,481|0,208|0,208|0,208|0,4%|0,4%|
|R_32|Estación C2|0,209|0,082|0,082|0,082|0,2%|0,2%|
|R_33|Estación C1|0,224|0,086|0,086|0,086|0,2%|0,2%|
|R_34|Estación C3|0,210|0,082|0,082|0,082|0,2%|0,2%|
|R_35|Estación C7|0,463|0,201|0,201|0,201|0,4%|0,4%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes actuales del Proyecto sobre los

receptores de interés alcanzan un máximo de 25,9% y 16,3% de la norma de este

contaminante en periodo diario, específicamente sobre los receptores denominados

“R_18” y “R_19”, los que corresponden a viviendas construidas con material mixto y

material ligero según orden de mención. Por su parte, en cuanto a los aportes actuales de

MP10 estimados para periodo anual, estos representan hasta un 14,4% y 14,1% de la

normativa respectiva, particularmente en los receptores indicados con anterioridad.

A continuación, en las siguientes figuras se presentan las curvas de isoconcentración de

material particulado respirable (MP10) para periodo de 24 horas y periodo anual.

www.dfmconsultores.cl

97

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-48. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP10 [μg/m** **[3]** **N]. Fase de**

**Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

98

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-49. Curvas de isoconcentración para periodo anual. MP10 [μg/m** **[3]** **N]. Fase de Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

99

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.1.3.3 Material Particulado Sedimentable (MPS)

En la Tabla 5-27 se presentan los aportes generados durante la fase de operación actual del

Proyecto sobre los receptores de interés, específicamente sobre receptores de medio

humano y estaciones de monitoreo, conforme con las normas de referencia internacionales

de material particulado sedimentable (MPS).

**Tabla 5-27. Resultados del modelo de dispersión para MPS [mg/m** **[2∙]** **día]. Fase de Operación Base.**

|Receptor|Descripción|Material Particulado Sedimentable (MPS)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**Media**<br>**Anual**|**Máxima**<br>**Media**<br>**Mensual**|**Conf. Suiza**|**República**<br>**Argentina**|**Conf. Suiza**|**República**<br>**Argentina**|
|R_1|Estación Luis Uribe|0,993|1,724|200|333|0,5%|0,5%|
|R_2|Estación Tierra Amarilla|1,724|2,922|2,922|2,922|0,9%|0,9%|
|R_3|Estación Ojanco|0,810|1,082|1,082|1,082|0,4%|0,3%|
|R_4|Estación Kozan|2,775|3,736|3,736|3,736|1,4%|1,1%|
|R_5|133 casa (Carola Norte)|2,745|3,276|3,276|3,276|1,4%|1,0%|
|R_6|Iglesia Tierra Amarilla|1,592|2,710|2,710|2,710|0,8%|0,8%|
|R_7|El Minero|4,582|6,989|6,989|6,989|2,3%|2,1%|
|R_8|Testigoteca|2,370|3,725|3,725|3,725|1,2%|1,1%|
|R_9|Estadio|16,080|17,118|17,118|17,118|8,0%|5,1%|
|R_10|Agrouva I|8,955|9,736|9,736|9,736|4,5%|2,9%|
|R_11|Agrouva II|3,983|5,061|5,061|5,061|2,0%|1,5%|
|R_12|Receptor ruido|2,574|3,857|3,857|3,857|1,3%|1,2%|
|R_13|Receptor ruido|2,016|3,115|3,115|3,115|1,0%|0,9%|
|R_14|Receptor ruido|1,843|2,269|2,269|2,269|0,9%|0,7%|
|R_15|Receptor ruido|7,913|11,687|11,687|11,687|4,0%|3,5%|
|R_16|Receptor ruido|7,703|12,071|12,071|12,071|3,9%|3,6%|
|R_17|Receptor ruido|4,238|5,971|5,971|5,971|2,1%|1,8%|
|R_18|Receptor ruido|18,810|24,021|24,021|24,021|9,4%|7,2%|
|R_19|Receptor ruido|21,840|23,558|23,558|23,558|10,9%|7,1%|
|R_20|Receptor ruido|15,730|18,055|18,055|18,055|7,9%|5,4%|
|R_21|Receptor ruido|15,554|18,007|18,007|18,007|7,8%|5,4%|
|R_22|Receptor ruido|5,417|6,573|6,573|6,573|2,7%|2,0%|
|R_23|Receptor ruido|0,177|0,237|0,237|0,237|0,1%|0,1%|
|R_24|Receptor ruido|0,155|0,207|0,207|0,207|0,1%|0,1%|
|R_25|Receptor ruido|0,094|0,151|0,151|0,151|0,0%|0,0%|
|R_26|Receptor ruido|0,462|0,603|0,603|0,603|0,2%|0,2%|
|R_27|Estación COEMIN|0,178|0,240|0,240|0,240|0,1%|0,1%|

www.dfmconsultores.cl

100

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Material Particulado Sedimentable (MPS)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**Media**<br>**Anual**|**Máxima**<br>**Media**<br>**Mensual**|**Conf. Suiza**|**República**<br>**Argentina**|**Conf. Suiza**|**República**<br>**Argentina**|
|R_28|Estación Nantoco|0,449|0,539|||0,2%|0,2%|
|R_29|Estación C6|0,271|0,354|0,354|0,354|0,1%|0,1%|
|R_30|Estación C5|0,213|0,291|0,291|0,291|0,1%|0,1%|
|R_31|Estación C8|0,397|0,526|0,526|0,526|0,2%|0,2%|
|R_32|Estación C2|0,102|0,157|0,157|0,157|0,1%|0,0%|
|R_33|Estación C1|0,108|0,164|0,164|0,164|0,1%|0,0%|
|R_34|Estación C3|0,102|0,159|0,159|0,159|0,1%|0,0%|
|R_35|Estación C7|0,378|0,506|0,506|0,506|0,2%|0,2%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes actuales del Proyecto sobre los

receptores de interés alcanzan un máximo de 10,9% y 9,4% de la norma de referencia para

periodo anual de la Confederación Suiza, particularmente sobre los receptores

denominados “R_19” y “R_18”, los que corresponden a viviendas construidas con material

ligero y material mixto según orden de mención. Por su parte, en cuanto a los valores

actuales de depositación de MPS mensuales estimados, estos representan hasta un 7,1% y

7,2% de la norma de referencia para periodo mensual de la República de Argentina,

específicamente en los receptores ya mencionados.

A continuación, en las siguientes figuras se presentan las curvas de isodepositación de

material particulado sedimentable (MPS) para periodo mensual y anual.

www.dfmconsultores.cl

101

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-50. Curvas de isodepositación para periodo mensual. MPS [mg/m** **[2]** **∙día]. Fase de Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

102

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-51. Curvas de isodepositación para periodo anual. MPS [mg/m** **[2]** **∙día]. Fase de Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

103

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.1.3.4 Monóxido de Carbono (CO)

En la Tabla 5-28 se presentan los aportes generados durante la fase de operación actual del

Proyecto sobre los receptores de interés, específicamente sobre receptores de medio

humano y estaciones de monitoreo, conforme con la norma primaria para monóxido de

carbono (CO).

**Tabla 5-28. Resultados del modelo de dispersión para CO [mg/m** **[3]** **N]. Fase de Operación Base.**

|Receptor|Descripción|Monóxido de Carbono (CO)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[mg/m3N]**|**Concentración**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|
|R_1|Estación Luis Uribe|0,005|0,002|30|10|0,0%|0,0%|
|R_2|Estación Tierra Amarilla|0,009|0,003|0,003|0,003|0,0%|0,0%|
|R_3|Estación Ojanco|0,014|0,003|0,003|0,003|0,0%|0,0%|
|R_4|Estación Kozan|0,030|0,007|0,007|0,007|0,1%|0,1%|
|R_5|133 casa (Carola Norte)|0,005|0,001|0,001|0,001|0,0%|0,0%|
|R_6|Iglesia Tierra Amarilla|0,006|0,002|0,002|0,002|0,0%|0,0%|
|R_7|El Minero|0,065|0,010|0,010|0,010|0,2%|0,1%|
|R_8|Testigoteca|0,050|0,008|0,008|0,008|0,2%|0,1%|
|R_9|Estadio|0,132|0,024|0,024|0,024|0,4%|0,2%|
|R_10|Agrouva I|0,073|0,013|0,013|0,013|0,2%|0,1%|
|R_11|Agrouva II|0,018|0,004|0,004|0,004|0,1%|0,0%|
|R_12|Receptor ruido|0,049|0,007|0,007|0,007|0,2%|0,1%|
|R_13|Receptor ruido|0,046|0,007|0,007|0,007|0,2%|0,1%|
|R_14|Receptor ruido|0,030|0,005|0,005|0,005|0,1%|0,1%|
|R_15|Receptor ruido|0,078|0,014|0,014|0,014|0,3%|0,1%|
|R_16|Receptor ruido|0,091|0,016|0,016|0,016|0,3%|0,2%|
|R_17|Receptor ruido|0,057|0,010|0,010|0,010|0,2%|0,1%|
|R_18|Receptor ruido|0,281|0,057|0,057|0,057|0,9%|0,6%|
|R_19|Receptor ruido|0,137|0,027|0,027|0,027|0,5%|0,3%|
|R_20|Receptor ruido|0,184|0,031|0,031|0,031|0,6%|0,3%|
|R_21|Receptor ruido|0,152|0,027|0,027|0,027|0,5%|0,3%|
|R_22|Receptor ruido|0,077|0,016|0,016|0,016|0,3%|0,2%|
|R_23|Receptor ruido|0,003|0,001|0,001|0,001|0,0%|0,0%|
|R_24|Receptor ruido|0,001|0,000|0,000|0,000|0,0%|0,0%|
|R_25|Receptor ruido|0,001|0,000|0,000|0,000|0,0%|0,0%|
|R_26|Receptor ruido|0,002|0,001|0,001|0,001|0,0%|0,0%|
|R_27|Estación COEMIN|0,003|0,001|0,001|0,001|0,0%|0,0%|
|R_28|Estación Nantoco|0,002|0,001|0,001|0,001|0,0%|0,0%|

www.dfmconsultores.cl

104

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Monóxido de Carbono (CO)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[mg/m3N]**|**Concentración**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|
|R_29|Estación C6|0,001|0,000|||0,0%|0,0%|
|R_30|Estación C5|0,001|0,000|0,000|0,000|0,0%|0,0%|
|R_31|Estación C8|0,001|0,000|0,000|0,000|0,0%|0,0%|
|R_32|Estación C2|0,001|0,000|0,000|0,000|0,0%|0,0%|
|R_33|Estación C1|0,001|0,000|0,000|0,000|0,0%|0,0%|
|R_34|Estación C3|0,001|0,000|0,000|0,000|0,0%|0,0%|
|R_35|Estación C7|0,001|0,000|0,000|0,000|0,0%|0,0%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes actuales del Proyecto sobre los

receptores de interés alcanzan un máximo de 0,9% y 0,6% de la norma de este

contaminante en periodo horario, específicamente sobre los receptores denominado

“R_18” y “R_20”, los que corresponden a viviendas construidas con material mixto y

material ligero respectivamente. Asimismo, para periodo de 8 horas, las concentraciones

actuales estimadas no sobrepasan el 0,6% de la norma respectiva, particularmente en el

receptor “R_18”. En consecuencia, es posible establecer que la contribución actual del

Proyecto sobre los receptores de interés, en cuanto a emisiones de CO, es prácticamente

mínima.

En consecuencia, considerando que los aportes de concentración de CO percibidos en los

receptores son menores a 1,5 mg/m [3] N en periodo horario y 0,4889 mg/m [3] N en periodo de

ocho horas, valores correspondientes a los límites de los Niveles de Impacto Significativo

para este contaminante según lo indicado en el documento “Evaluación Significancia del

Impacto de las Emisiones de un Proyecto o Actividad en Zonas Saturadas en el Marco del

SEIA” (DICTUC, 2022), en esta oportunidad no se presentan curvas de isoconcentración de

monóxido de carbono asociadas a la fase de operación base del Proyecto.

www.dfmconsultores.cl

105

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.1.3.5 Dióxido de Nitrógeno (NO 2 )

En la Tabla 5-29 se presentan los aportes generados durante la fase de operación actual del

Proyecto sobre los receptores de interés, específicamente sobre receptores de medio

humano y estaciones de monitoreo, conforme con la norma primaria para dióxido de

nitrógeno (NO 2 ).

**Tabla 5-29. Resultados del modelo de dispersión para NO** **2** **[μg/m** **[3]** **N]. Fase de Operación Base.**

|Receptor|Descripción|Dióxido de Nitrógeno (NO )<br>2|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|5,887|0,426|400|100|1,5%|0,4%|
|R_2|Estación Tierra Amarilla|9,637|0,737|0,737|0,737|2,4%|0,7%|
|R_3|Estación Ojanco|14,766|0,472|0,472|0,472|3,7%|0,5%|
|R_4|Estación Kozan|27,530|0,619|0,619|0,619|6,9%|0,6%|
|R_5|133 casa (Carola Norte)|4,333|0,297|0,297|0,297|1,1%|0,3%|
|R_6|Iglesia Tierra Amarilla|5,654|0,569|0,569|0,569|1,4%|0,6%|
|R_7|El Minero|46,539|0,855|0,855|0,855|11,6%|0,9%|
|R_8|Testigoteca|34,687|0,471|0,471|0,471|8,7%|0,5%|
|R_9|Estadio|95,304|1,688|1,688|1,688|23,8%|1,7%|
|R_10|Agrouva I|56,130|1,191|1,191|1,191|14,0%|1,2%|
|R_11|Agrouva II|19,391|0,746|0,746|0,746|4,8%|0,7%|
|R_12|Receptor ruido|38,283|0,524|0,524|0,524|9,6%|0,5%|
|R_13|Receptor ruido|35,404|0,445|0,445|0,445|8,9%|0,4%|
|R_14|Receptor ruido|20,175|0,372|0,372|0,372|5,0%|0,4%|
|R_15|Receptor ruido|39,438|0,849|0,849|0,849|9,9%|0,8%|
|R_16|Receptor ruido|53,136|1,007|1,007|1,007|13,3%|1,0%|
|R_17|Receptor ruido|38,518|0,676|0,676|0,676|9,6%|0,7%|
|R_18|Receptor ruido|200,690|2,672|2,672|2,672|50,2%|2,7%|
|R_19|Receptor ruido|110,130|1,733|1,733|1,733|27,5%|1,7%|
|R_20|Receptor ruido|127,960|2,239|2,239|2,239|32,0%|2,2%|
|R_21|Receptor ruido|107,940|2,017|2,017|2,017|27,0%|2,0%|
|R_22|Receptor ruido|60,019|0,959|0,959|0,959|15,0%|1,0%|
|R_23|Receptor ruido|1,876|0,061|0,061|0,061|0,5%|0,1%|
|R_24|Receptor ruido|1,206|0,054|0,054|0,054|0,3%|0,1%|
|R_25|Receptor ruido|0,488|0,035|0,035|0,035|0,1%|0,0%|
|R_26|Receptor ruido|2,327|0,122|0,122|0,122|0,6%|0,1%|
|R_27|Estación COEMIN|1,967|0,061|0,061|0,061|0,5%|0,1%|
|R_28|Estación Nantoco|1,805|0,120|0,120|0,120|0,5%|0,1%|
|R_29|Estación C6|1,452|0,078|0,078|0,078|0,4%|0,1%|

www.dfmconsultores.cl

106

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Dióxido de Nitrógeno (NO )<br>2|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|
|R_30|Estación C5|1,158|0,067|||0,3%|0,1%|
|R_31|Estación C8|1,629|0,091|0,091|0,091|0,4%|0,1%|
|R_32|Estación C2|0,678|0,037|0,037|0,037|0,2%|0,0%|
|R_33|Estación C1|0,765|0,039|0,039|0,039|0,2%|0,0%|
|R_34|Estación C3|0,654|0,037|0,037|0,037|0,2%|0,0%|
|R_35|Estación C7|1,590|0,088|0,088|0,088|0,4%|0,1%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes actuales del Proyecto sobre los

receptores de interés alcanzan un máximo de 50,2% y 32,0% de la norma de este

contaminante en periodo horario, específicamente sobre los receptores denominados

“R_18” y “R_20”, los que corresponden a viviendas construidas con material mixto y

material ligero según orden de mención. Por su parte, en cuanto a las concentraciones

actuales de NO 2 estimadas para periodo anual, estas representan hasta un 2,7% y 2,2% de

la normativa respectiva, particularmente en los receptores ya indicados.

A continuación, en las siguientes figuras se presentan las curvas de isoconcentración de

dióxido de nitrógeno (NO 2 ) para periodo de 1 hora y periodo anual.

www.dfmconsultores.cl

107

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-52. Curvas de isoconcentración para percentil 99 periodo 1 hora. NO** **2** **[μg/m** **[3]** **N]. Fase de**

**Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

108

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-53. Curvas de isoconcentración para periodo anual. NO** **2** **[μg/m** **[3]** **N]. Fase de Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

109

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.1.3.6 Dióxido de Azufre (SO 2 )

En la Tabla 5-30 se presentan los aportes generados durante la fase de operación actual del Proyecto sobre los receptores de interés,

específicamente sobre receptores de medio humano y estaciones de monitoreo, conforme con la norma primaria para dióxido de

azufre (SO 2 ).

**Tabla 5-30. Resultados del modelo de dispersión para SO** **2** **[μg/m** **[3]** **N]. Fase de Operación Base.**

|Receptor|Descripción|Dióxido de Azufre (SO )<br>2|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|0,008|0,003|0,001|350|150|60|0,0%|0,0%|0,0%|
|R_2|Estación Tierra Amarilla|0,014|0,004|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_3|Estación Ojanco|0,018|0,004|0,001|0,001|0,001|0,001|0,0%|0,0%|0,0%|
|R_4|Estación Kozan|0,022|0,010|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_5|133 casa (Carola Norte)|0,007|0,002|0,001|0,001|0,001|0,001|0,0%|0,0%|0,0%|
|R_6|Iglesia Tierra Amarilla|0,010|0,003|0,001|0,001|0,001|0,001|0,0%|0,0%|0,0%|
|R_7|El Minero|0,057|0,012|0,003|0,003|0,003|0,003|0,0%|0,0%|0,0%|
|R_8|Testigoteca|0,035|0,010|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_9|Estadio|0,087|0,033|0,005|0,005|0,005|0,005|0,0%|0,0%|0,0%|
|R_10|Agrouva I|0,046|0,018|0,004|0,004|0,004|0,004|0,0%|0,0%|0,0%|
|R_11|Agrouva II|0,020|0,005|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_12|Receptor ruido|0,036|0,010|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_13|Receptor ruido|0,029|0,009|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_14|Receptor ruido|0,027|0,007|0,001|0,001|0,001|0,001|0,0%|0,0%|0,0%|
|R_15|Receptor ruido|0,096|0,016|0,004|0,004|0,004|0,004|0,0%|0,0%|0,0%|
|R_16|Receptor ruido|0,115|0,018|0,005|0,005|0,005|0,005|0,0%|0,0%|0,0%|
|R_17|Receptor ruido|0,062|0,014|0,003|0,003|0,003|0,003|0,0%|0,0%|0,0%|
|R_18|Receptor ruido|0,245|0,061|0,011|0,011|0,011|0,011|0,1%|0,0%|0,0%|

www.dfmconsultores.cl

110

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Dióxido de Azufre (SO )<br>2|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|
|R_19|Receptor ruido|0,092|0,037|0,006||||0,0%|0,0%|0,0%|
|R_20|Receptor ruido|0,136|0,045|0,008|0,008|0,008|0,008|0,0%|0,0%|0,0%|
|R_21|Receptor ruido|0,122|0,030|0,007|0,007|0,007|0,007|0,0%|0,0%|0,0%|
|R_22|Receptor ruido|0,042|0,017|0,003|0,003|0,003|0,003|0,0%|0,0%|0,0%|
|R_23|Receptor ruido|0,002|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_24|Receptor ruido|0,001|0,000|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_25|Receptor ruido|0,001|0,000|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_26|Receptor ruido|0,003|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_27|Estación COEMIN|0,002|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_28|Estación Nantoco|0,002|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_29|Estación C6|0,002|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_30|Estación C5|0,001|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_31|Estación C8|0,002|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_32|Estación C2|0,001|0,000|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_33|Estación C1|0,001|0,000|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_34|Estación C3|0,001|0,000|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_35|Estación C7|0,002|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

111

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Tal como se observa en la tabla anterior, los aportes actuales del Proyecto sobre los

receptores de interés no superan el 0,1% de la norma de este contaminante en periodo

horario, específicamente sobre el receptor denominado “R_18”, el cual corresponde a

viviendas construidas con material mixto. Mientras que, para periodo diario y anual, las

concentraciones actuales estimadas no sobrepasan el 0,0% de las normativas respectivas,

en cada uno de los receptores estudiados. En consecuencia, es posible establecer que la

contribución actual del Proyecto sobre los receptores de interés, en cuanto a emisiones de

SO 2, es prácticamente nula.

En consecuencia, considerando que los aportes de concentración de SO 2 percibidos en los

receptores son menores a 14,0 μg/m [3] N en periodo horario, 2,0 μg/m [3] N en periodo diario y

1,2 μg/m [3] N en periodo anual, valores correspondientes a los límites de los Niveles de

Impacto Significativo para este contaminante según lo indicado en el documento

“Evaluación Significancia del Impacto de las Emisiones de un Proyecto o Actividad en Zonas

Saturadas en el Marco del SEIA” (DICTUC, 2022), en esta oportunidad no se presentan

curvas de isoconcentración de dióxido de azufre asociadas a la fase de operación base del

Proyecto.

www.dfmconsultores.cl

112

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.2 Fase de Operación Proyectada

5.9.2.1 Fuentes Emisoras

Las fuentes emisoras de la fase de operación proyectada han sido georreferenciadas de

acuerdo con la información proporcionada por la ingeniería del Proyecto, para

posteriormente ser ingresadas al modelo de dispersión de contaminantes.

Por tanto, en la Figura 5-54 se presentan las fuentes emisoras del tipo areal y caminos,

mientras que en la Tabla 5-31 se muestra el detalle de las características de las fuentes y las

tasas de emisión asociadas a cada una.

www.dfmconsultores.cl

113

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-54. Ubicación Fuentes Emisoras. Fase de Operación Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

114

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Tabla 5-31. Características de Fuentes Emisoras y Tasas de Emisión. Fase de Operación Proyectada.**

|ID|Descripción|Tipo de fuente|Tasas de emisión|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Descripción**|**Tipo de fuente**|**MP2.5**|**MP10**|**MPS**|**NO**|**NO2 **|**SO2 **|**CO**|**Unidad**|
|SRC_1|Tramo C1|Camino|1,88 E-07|6,11 E-07|2,96 E-06|1,23 E-06|2,10 E-07|2,29 E-09|5,46 E-07|g/s/m|
|SRC_2|Tramo C2|Camino|9,22 E-07|3,60 E-06|1,84 E-05|1,79 E-06|3,05 E-07|3,20 E-09|7,60 E-07|g/s/m|
|SRC_3|Tramo C3|Camino|7,56 E-07|2,99 E-06|1,54 E-05|1,27 E-06|2,17 E-07|2,19 E-09|5,22 E-07|g/s/m|
|SRC_4|Tramo C4|Camino|6,01 E-08|1,94 E-07|9,40 E-07|3,13 E-07|5,34 E-08|6,53 E-10|1,53 E-07|g/s/m|
|SRC_5|Tramo C5|Camino|1,42 E-06|5,68 E-06|2,93 E-05|1,67 E-06|2,85 E-07|2,93 E-09|7,02 E-07|g/s/m|
|SRC_6|Tramo C6|Camino|2,32 E-06|9,45 E-06|4,91 E-05|1,13 E-06|1,92 E-07|1,94 E-09|4,64 E-07|g/s/m|
|SRC_7|Tramo C7|Camino|8,90 E-07|3,59 E-06|1,86 E-05|7,90 E-07|1,35 E-07|1,36 E-09|3,24 E-07|g/s/m|
|SRC_8|Tramo C9|Camino|7,50 E-07|3,01 E-06|1,56 E-05|8,15 E-07|1,39 E-07|1,40 E-09|3,35 E-07|g/s/m|
|SRC_9|Tramo C10|Camino|5,89 E-07|2,34 E-06|1,21 E-05|8,80 E-07|1,50 E-07|1,51 E-09|3,61 E-07|g/s/m|
|SRC_10|Tramo C11|Camino|3,30 E-08|1,27 E-07|6,49 E-07|8,42 E-08|1,44 E-08|1,44 E-10|3,42 E-08|g/s/m|
|SRC_11|Tramo C12|Camino|4,05 E-07|1,54 E-06|7,81 E-06|1,10 E-06|1,87 E-07|2,01 E-09|4,77 E-07|g/s/m|
|SRC_12|Tramo N1|Camino|2,35 E-07|2,16 E-06|8,71 E-06|4,62 E-07|7,87 E-08|8,79 E-10|2,13 E-07|g/s/m|
|SRC_13|Tramo N2|Camino|2,14 E-07|1,96 E-06|7,92 E-06|4,20 E-07|7,15 E-08|7,99 E-10|1,94 E-07|g/s/m|
|SRC_14|Tramo N3|Camino|1,02 E-07|9,02 E-07|3,63 E-06|2,94 E-07|5,01 E-08|5,36 E-10|1,34 E-07|g/s/m|
|SRC_15|Tramo N4|Camino|4,34 E-07|4,18 E-06|1,69 E-05|5,08 E-07|8,66 E-08|8,74 E-10|2,09 E-07|g/s/m|
|SRC_16|Tramo N5|Camino|3,83 E-07|3,69 E-06|1,50 E-05|4,47 E-07|7,62 E-08|7,69 E-10|1,84 E-07|g/s/m|
|SRC_17|Tramo S1|Camino|9,89 E-07|9,75 E-06|2,82 E-05|2,12 E-07|3,61 E-08|5,78 E-10|1,22 E-07|g/s/m|
|SRC_18|Tramo S2|Camino|1,05 E-06|1,03 E-05|2,99 E-05|2,25 E-07|3,83 E-08|6,13 E-10|1,30 E-07|g/s/m|
|SRC_19|Tramo S3|Camino|2,82 E-06|2,80 E-05|8,09 E-05|7,61 E-07|1,30 E-07|1,31 E-09|3,12 E-07|g/s/m|
|SRC_20|Tramo S4|Camino|7,68 E-06|7,62 E-05|2,20 E-04|1,55 E-06|2,64 E-07|3,08 E-09|7,04 E-07|g/s/m|
|SRC_21|Tramo P1|Camino|2,48 E-08|9,32 E-08|4,73 E-07|8,55 E-08|1,46 E-08|1,47 E-10|3,51 E-08|g/s/m|
|SRC_22|Tramo P2|Camino|2,77 E-08|1,04 E-07|5,28 E-07|9,55 E-08|1,63 E-08|1,64 E-10|3,92 E-08|g/s/m|
|SRC_23|Tramo P3|Camino|2,08 E-07|7,12 E-07|3,51 E-06|9,01 E-07|1,54 E-07|1,88 E-09|4,34 E-07|g/s/m|
|SRC_24|Tramo P4|Camino|2,07 E-07|7,08 E-07|3,49 E-06|8,96 E-07|1,53 E-07|1,87 E-09|4,32 E-07|g/s/m|
|SRC_25|Tramo P5|Camino|1,80 E-07|6,06 E-07|2,97 E-06|8,02 E-07|1,37 E-07|1,71 E-09|3,93 E-07|g/s/m|

www.dfmconsultores.cl

115

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|ID|Descripción|Tipo de fuente|Tasas de emisión|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Descripción**|**Tipo de fuente**|**MP2.5**|**MP10**|**MPS**|**NO**|**NO2 **|**SO2 **|**CO**|**Unidad**|
|SRC_26|Tramo P6|Camino|1,08 E-07|3,34 E-07|1,59 E-06|6,60 E-07|1,13 E-07|1,40 E-09|3,21 E-07|g/s/m|
|SRC_27|Tramo P7|Camino|1,25 E-07|3,88 E-07|1,85 E-06|7,62 E-07|1,30 E-07|1,62 E-09|3,69 E-07|g/s/m|
|SRC_28|Tramo P8|Camino|3,68 E-09|9,56 E-09|4,22 E-08|1,40 E-08|2,38 E-09|5,55 E-11|1,09 E-08|g/s/m|
|SRC_29|Tramo P9|Camino|3,70 E-08|1,29 E-07|6,43 E-07|1,76 E-07|3,00 E-08|3,34 E-10|7,71 E-08|g/s/m|
|SRC_30|Tramo P10|Camino|7,28 E-08|2,25 E-07|1,07 E-06|3,88 E-07|6,61 E-08|9,18 E-10|2,01 E-07|g/s/m|
|SRC_31|Tramo P11|Camino|4,69 E-08|1,60 E-07|7,90 E-07|2,18 E-07|3,71 E-08|4,33 E-10|1,02 E-07|g/s/m|
|SRC_32|Carola Norte|Área|1,44 E-07|3,43 E-07|6,04 E-07|1,07 E-06|1,83 E-07|4,76 E-09|1,52 E-06|g/s/m2|
|SRC_33|Carola Central|Área|9,04 E-06|1,58 E-05|6,53 E-05|6,71 E-06|1,14 E-06|2,93 E-08|9,78 E-06|g/s/m2|

Fuente: Elaboración propia.

www.dfmconsultores.cl

116

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.2.2 Receptores de Interés

Para la evaluación del aporte de las emisiones atmosféricas del Proyecto, se han definido

dos grillas de receptores, la primera con resolución de 37.000 x 43.000 m con espaciado

cada 1.000 m y la segunda, correspondiente a una grilla anidada, con resolución de 3.500 x

3.500 m con espaciado cada 500 m en el sector Carola Norte, más una resolución de 8.500

x 8.500 m con espaciado cada 500 m en el sector Carola Centro y una resolución de 5.000 x

4.500 m con espaciado cada 500 m en el sector Carola Sur.

De este modo, la primera grilla abarca gran parte del dominio de modelación, procurando

contender todas las fuentes emisoras mencionadas con anterioridad, mientras que la

segunda se centraliza en las distintas áreas de trabajo de Mina Carola.

A modo complementario, se han considerado 35 receptores discretos, los cuales

representan puntos de interés tales como: medio humano y estaciones de monitoreo. La

ubicación de tales puntos se muestra de manera detallada en la Tabla 5-32.

**Tabla 5-32. Receptores de Interés. Fase de Operación Proyectada.**

|ID|Receptor|Coordenadas [Datum WGS84]|Col4|Elevación<br>[m.s.n.m.]|
|---|---|---|---|---|
|**ID**|**Receptor**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|R_1|Estación Luis Uribe|374.942|6.961.596|514,30|
|R_2|Estación Tierra Amarilla|374.904|6.960.235|521,39|
|R_3|Estación Ojanco|374.772|6.958.885|513,93|
|R_4|Estación Kozan|375.076|6.956.263|568,74|
|R_5|133 casa (Carola Norte)|375.842|6.961.206|561,91|
|R_6|Iglesia Tierra Amarilla|375.270|6.961.216|518,20|
|R_7|El Minero|375.114|6.958.078|540,49|
|R_8|Testigoteca|375.054|6.957.920|541,09|
|R_9|Estadio|375.353|6.956.715|573,60|
|R_10|Agrouva I|375.347|6.956.543|567,13|
|R_11|Agrouva II|375.370|6.956.345|551,88|
|R_12|Receptor ruido (viviendas 1 piso, material mixto)|375.021|6.958.033|539,80|
|R_13|Receptor ruido (viviendas 1 piso, material ligero)|375.005|6.957.965|540,10|
|R_14|Receptor ruido (viviendas 1 piso, material ligero)|374.966|6.957.769|542,55|
|R_15|Receptor ruido (Oficinas, galpones y container, material<br>mixto)|375.215|6.957.683|554,95|
|R_16|Receptor ruido (Vivienda 2 pisos, material ligero)|375.126|6.957.573|558,76|
|R_17|Receptor ruido (Viviendas 1 y 2 pisos, material ligero)|375.093|6.957.335|555,04|

www.dfmconsultores.cl

117

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|ID|Receptor|Coordenadas [Datum WGS84]|Col4|Elevación<br>[m.s.n.m.]|
|---|---|---|---|---|
|**ID**|**Receptor**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|R_18|Receptor ruido (Viviendas 1 y 2 pisos, material mixto)|375.248|6.957.084|566,44|
|R_19|Receptor ruido (Viviendas 1 y 2 pisos, material ligero)|375.278|6.956.755|573,88|
|R_20|Receptor ruido (Viviendas 1 piso, material ligero)|375.476|6.956.834|575,09|
|R_21|Receptor ruido (Vivienda 1 piso, material ligero)|375.633|6.956.813|584,48|
|R_22|Receptor ruido (Viviendas 1 y 2 pisos, material ligero)|375.105|6.956.579|575,38|
|R_23|Receptor ruido (Oficinas Empresa Agrícola Uvas del Norte,<br>ubicada frente a Planta Cerrillos- COEMIN)|377.121|6.949.607|642,08|
|R_24|Receptor ruido (Km 21 Carretera C-35. Entrada Fundo<br>Alianza Agricultura)|376.866|6.948.610|631,11|
|R_25|Receptor ruido (Km 21 Carretera C-35. Frente a casa-<br>almacén)|376.669|6.946.880|627,97|
|R_26|Receptor ruido (Punto ubicado a 5 k. Planta Cerrillos, por<br>carretera C-35, localidad de Nantoco)|374.539|6.953.171|552,36|
|R_27|Estación COEMIN|377.146|6.949.777|640,22|
|R_28|Estación Nantoco|374.903|6.952.384|575,29|
|R_29|Estación C6|375.453|6.950.426|599,45|
|R_30|Estación C5|375.723|6.949.811|616,72|
|R_31|Estación C8|375.345|6 950 895|595,90|
|R_32|Estación C2|377.121|6.946.865|644,54|
|R_33|Estación C1|377.154|6.947.080|643,66|
|R_34|Estación C3|376.995|6.946.944|633,39|
|R_35|Estación C7|375.348|6.950.777|603,95|

Fuente: Elaboración propia.

A continuación, en la Figura 5-55 se presentan las grillas de receptores utilizadas, mientras

que en la Figura 5-56 se muestran los receptores de interés considerados en la modelación

de dispersión de contaminantes.

www.dfmconsultores.cl

118

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-55. Ubicación Grilla de Receptores. Fase de Operación Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

119

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-56. Ubicación de Receptores de Interés. Fase de Operación Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

120

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.2.3 Resultados de Modelación

A continuación, en los siguientes apartados se presentan los resultados de la modelación

de dispersión de contaminantes realizada para la fase de operación proyectada del Proyecto

“Optimización Operacional Mina Carola”, considerando un tiempo de desarrollo de 12

meses.

Para ello, se muestran las concentraciones aportadas por el Proyecto, para cada uno de los

contaminantes considerados en el estudio, sobre los receptores de interés mencionados

con anterioridad, realizando un análisis normativo de cada uno de los estadígrafos indicados

por las normativas y valores de referencia señalados en la sección 5.7.

Además, a modo complementario, se presentan las curvas de isoconcentración e

isodepositación, según corresponde, conforme a las concentraciones y depositaciones

obtenidas y percibidas en el dominio de modelación.

www.dfmconsultores.cl

121

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.2.3.1 Material Particulado Respirable Fino (MP2.5)

En la Tabla 5-33 se presentan los aportes generados durante la fase de operación

proyectada del Proyecto sobre los receptores de interés, específicamente sobre receptores

de medio humano y estaciones de monitoreo, conforme con la norma primaria para

material particulado respirable fino (MP2.5).

**Tabla 5-33. Resultados del modelo de dispersión para MP2.5 [μg/m** **[3]** **]. Fase de Operación Proyectada.**

|Receptor|Descripción|Material Particulado Respirable Fino (MP2.5)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3] **|**Concentración [μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|0,851|0,409|50|20|1,7%|2,0%|
|R_2|Estación Tierra Amarilla|1,456|0,711|0,711|0,711|2,9%|3,6%|
|R_3|Estación Ojanco|1,269|0,473|0,473|0,473|2,5%|2,4%|
|R_4|Estación Kozan|2,922|0,673|0,673|0,673|5,8%|3,4%|
|R_5|133 casa (Carola Norte)|0,730|0,302|0,302|0,302|1,5%|1,5%|
|R_6|Iglesia Tierra Amarilla|1,106|0,557|0,557|0,557|2,2%|2,8%|
|R_7|El Minero|4,164|1,219|1,219|1,219|8,3%|6,1%|
|R_8|Testigoteca|2,545|0,679|0,679|0,679|5,1%|3,4%|
|R_9|Estadio|8,225|2,169|2,169|2,169|16,4%|10,8%|
|R_10|Agrouva I|4,954|1,398|1,398|1,398|9,9%|7,0%|
|R_11|Agrouva II|1,826|0,773|0,773|0,773|3,7%|3,9%|
|R_12|Receptor ruido|2,545|0,698|0,698|0,698|5,1%|3,5%|
|R_13|Receptor ruido|2,336|0,606|0,606|0,606|4,7%|3,0%|
|R_14|Receptor ruido|1,938|0,524|0,524|0,524|3,9%|2,6%|
|R_15|Receptor ruido|5,332|1,638|1,638|1,638|10,7%|8,2%|
|R_16|Receptor ruido|6,134|1,861|1,861|1,861|12,3%|9,3%|
|R_17|Receptor ruido|3,650|1,066|1,066|1,066|7,3%|5,3%|
|R_18|Receptor ruido|21,716|4,240|4,240|4,240|43,4%|21,2%|
|R_19|Receptor ruido|9,904|2,305|2,305|2,305|19,8%|11,5%|
|R_20|Receptor ruido|11,102|3,019|3,019|3,019|22,2%|15,1%|
|R_21|Receptor ruido|9,477|2,691|2,691|2,691|19,0%|13,5%|
|R_22|Receptor ruido|5,993|1,145|1,145|1,145|12,0%|5,7%|
|R_23|Receptor ruido|0,289|0,073|0,073|0,073|0,6%|0,4%|
|R_24|Receptor ruido|0,195|0,064|0,064|0,064|0,4%|0,3%|
|R_25|Receptor ruido|0,109|0,042|0,042|0,042|0,2%|0,2%|
|R_26|Receptor ruido|0,285|0,128|0,128|0,128|0,6%|0,6%|
|R_27|Estación COEMIN|0,299|0,074|0,074|0,074|0,6%|0,4%|
|R_28|Estación Nantoco|0,307|0,133|0,133|0,133|0,6%|0,7%|

www.dfmconsultores.cl

122

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Material Particulado Respirable Fino (MP2.5)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3] **|**Concentración [μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_29|Estación C6|0,235|0,091|||0,5%|0,5%|
|R_30|Estación C5|0,204|0,078|0,078|0,078|0,4%|0,4%|
|R_31|Estación C8|0,266|0,105|0,105|0,105|0,5%|0,5%|
|R_32|Estación C2|0,118|0,045|0,045|0,045|0,2%|0,2%|
|R_33|Estación C1|0,126|0,047|0,047|0,047|0,3%|0,2%|
|R_34|Estación C3|0,118|0,045|0,045|0,045|0,2%|0,2%|
|R_35|Estación C7|0,255|0,101|0,101|0,101|0,5%|0,5%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes proyectados del Proyecto sobre los

receptores de interés alcanzan un máximo de 43,4% y 22,2% de la norma de este

contaminante en periodo diario, específicamente sobre los receptores denominados

“R_18” y “R_20”, los que corresponden a viviendas construidas con material mixto y

material ligero respectivamente. Por su parte, en cuanto a los aportes proyectados de

MP2.5 estimados para periodo anual, estos representan hasta un 21,2% y 15,1% de la

normativa respectiva, particularmente en los receptores indicados con anterioridad.

A continuación, en las siguientes figuras se presentan las curvas de isoconcentración de

material particulado respirable fino (MP2.5) para periodo de 24 horas y periodo anual.

www.dfmconsultores.cl

123

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-57. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP2.5 [μg/m** **[3]** **]. Fase de**

**Operación Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

124

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-58. Curvas de isoconcentración para periodo anual. MP2.5 [μg/m** **[3]** **]. Fase de Operación**

**Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

125

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.2.3.2 Material Particulado Respirable (MP10)

En la Tabla 5-34 se presentan los aportes generados durante la fase de operación

proyectada del Proyecto sobre los receptores de interés, específicamente sobre receptores

de medio humano y estaciones de monitoreo, conforme con la norma primaria para

material particulado respirable (MP10).

**Tabla 5-34. Resultados del modelo de dispersión para MP10 [μg/m** **[3]** **N]. Fase de Operación Proyectada.**

|Receptor|Descripción|Material Particulado Respirable (MP10)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|1,537|0,738|130|50|1,2%|1,5%|
|R_2|Estación Tierra Amarilla|2,549|1,269|1,269|1,269|2,0%|2,5%|
|R_3|Estación Ojanco|2,224|0,848|0,848|0,848|1,7%|1,7%|
|R_4|Estación Kozan|4,989|1,253|1,253|1,253|3,8%|2,5%|
|R_5|133 casa (Carola Norte)|1,359|0,658|0,658|0,658|1,0%|1,3%|
|R_6|Iglesia Tierra Amarilla|2,030|1,016|1,016|1,016|1,6%|2,0%|
|R_7|El Minero|7,206|2,186|2,186|2,186|5,5%|4,4%|
|R_8|Testigoteca|4,477|1,236|1,236|1,236|3,4%|2,5%|
|R_9|Estadio|14,962|4,407|4,407|4,407|11,5%|8,8%|
|R_10|Agrouva I|9,029|2,777|2,777|2,777|6,9%|5,6%|
|R_11|Agrouva II|3,261|1,418|1,418|1,418|2,5%|2,8%|
|R_12|Receptor ruido|4,415|1,284|1,284|1,284|3,4%|2,6%|
|R_13|Receptor ruido|4,101|1,107|1,107|1,107|3,2%|2,2%|
|R_14|Receptor ruido|3,378|0,964|0,964|0,964|2,6%|1,9%|
|R_15|Receptor ruido|9,364|2,971|2,971|2,971|7,2%|5,9%|
|R_16|Receptor ruido|10,748|3,300|3,300|3,300|8,3%|6,6%|
|R_17|Receptor ruido|6,484|1,925|1,925|1,925|5,0%|3,9%|
|R_18|Receptor ruido|36,581|7,458|7,458|7,458|28,1%|14,9%|
|R_19|Receptor ruido|18,369|4,972|4,972|4,972|14,1%|9,9%|
|R_20|Receptor ruido|19,314|5,666|5,666|5,666|14,9%|11,3%|
|R_21|Receptor ruido|16,482|5,304|5,304|5,304|12,7%|10,6%|
|R_22|Receptor ruido|10,650|2,176|2,176|2,176|8,2%|4,4%|
|R_23|Receptor ruido|0,495|0,133|0,133|0,133|0,4%|0,3%|
|R_24|Receptor ruido|0,348|0,116|0,116|0,116|0,3%|0,2%|
|R_25|Receptor ruido|0,198|0,076|0,076|0,076|0,2%|0,2%|
|R_26|Receptor ruido|0,507|0,234|0,234|0,234|0,4%|0,5%|
|R_27|Estación COEMIN|0,515|0,134|0,134|0,134|0,4%|0,3%|
|R_28|Estación Nantoco|0,540|0,244|0,244|0,244|0,4%|0,5%|

www.dfmconsultores.cl

126

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Material Particulado Respirable (MP10)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_29|Estación C6|0,415|0,167|||0,3%|0,3%|
|R_30|Estación C5|0,362|0,143|0,143|0,143|0,3%|0,3%|
|R_31|Estación C8|0,468|0,198|0,198|0,198|0,4%|0,4%|
|R_32|Estación C2|0,208|0,081|0,081|0,081|0,2%|0,2%|
|R_33|Estación C1|0,221|0,085|0,085|0,085|0,2%|0,2%|
|R_34|Estación C3|0,209|0,081|0,081|0,081|0,2%|0,2%|
|R_35|Estación C7|0,454|0,191|0,191|0,191|0,3%|0,4%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes proyectados del Proyecto sobre los

receptores de interés alcanzan un máximo de 28,1% y 14,9% de la norma de este

contaminante en periodo diario, específicamente sobre los receptores denominados

“R_18” y “R_20”, los que corresponden a viviendas construidas con material mixto y

material ligero respectivamente. Por su parte, en cuanto a los aportes proyectados de MP10

estimados para periodo anual, estos representan hasta un 14,9% y 11,3% de la normativa

respectiva, particularmente en los receptores indicados con anterioridad.

A continuación, en las siguientes figuras se presentan las curvas de isoconcentración de

material particulado respirable (MP10) para periodo de 24 horas y periodo anual.

www.dfmconsultores.cl

127

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-59. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP10 [μg/m** **[3]** **]. Fase de**

**Operación Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

128

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-60. Curvas de isoconcentración para periodo anual. MP10 [μg/m** **[3]** **N]. Fase de Operación**

**Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

129

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.2.3.3 Material Particulado Sedimentable (MPS)

En la Tabla 5-35 se presentan los aportes generados durante la fase de operación

proyectada del Proyecto sobre los receptores de interés, específicamente sobre receptores

de medio humano y estaciones de monitoreo, conforme con las normas de referencia

internacionales de material particulado sedimentable (MPS).

**Tabla 5-35. Resultados del modelo de dispersión para MPS [mg/m** **[2]** **∙día]. Fase de Operación Proyectada.**

|Receptor|Descripción|Material Particulado Sedimentable (MPS)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**Media**<br>**Anual**|**Máxima**<br>**Media**<br>**Mensual**|**Conf. Suiza**|**República**<br>**Argentina**|**Conf. Suiza**|**República**<br>**Argentina**|
|R_1|Estación Luis Uribe|1,023|1,813|200|333|0,5%|0,5%|
|R_2|Estación Tierra Amarilla|1,805|3,096|3,096|3,096|0,9%|0,9%|
|R_3|Estación Ojanco|0,824|1,108|1,108|1,108|0,4%|0,3%|
|R_4|Estación Kozan|2,464|3,244|3,244|3,244|1,2%|1,0%|
|R_5|133 casa (Carola Norte)|1,228|1,400|1,400|1,400|0,6%|0,4%|
|R_6|Iglesia Tierra Amarilla|1,439|2,626|2,626|2,626|0,7%|0,8%|
|R_7|El Minero|4,788|7,398|7,398|7,398|2,4%|2,2%|
|R_8|Testigoteca|2,438|3,898|3,898|3,898|1,2%|1,2%|
|R_9|Estadio|10,956|11,920|11,920|11,920|5,5%|3,6%|
|R_10|Agrouva I|6,545|7,372|7,372|7,372|3,3%|2,2%|
|R_11|Agrouva II|3,667|4,698|4,698|4,698|1,8%|1,4%|
|R_12|Receptor ruido|2,464|3,834|3,834|3,834|1,2%|1,2%|
|R_13|Receptor ruido|2,022|3,203|3,203|3,203|1,0%|1,0%|
|R_14|Receptor ruido|1,820|2,270|2,270|2,270|0,9%|0,7%|
|R_15|Receptor ruido|8,236|12,215|12,215|12,215|4,1%|3,7%|
|R_16|Receptor ruido|8,212|12,923|12,923|12,923|4,1%|3,9%|
|R_17|Receptor ruido|4,317|6,140|6,140|6,140|2,2%|1,8%|
|R_18|Receptor ruido|19,609|25,115|25,115|25,115|9,8%|7,5%|
|R_19|Receptor ruido|13,100|14,676|14,676|14,676|6,6%|4,4%|
|R_20|Receptor ruido|13,505|15,185|15,185|15,185|6,8%|4,6%|
|R_21|Receptor ruido|11,743|13,112|13,112|13,112|5,9%|3,9%|
|R_22|Receptor ruido|4,351|5,296|5,296|5,296|2,2%|1,6%|
|R_23|Receptor ruido|0,180|0,239|0,239|0,239|0,1%|0,1%|
|R_24|Receptor ruido|0,159|0,212|0,212|0,212|0,1%|0,1%|
|R_25|Receptor ruido|0,097|0,157|0,157|0,157|0,0%|0,0%|
|R_26|Receptor ruido|0,469|0,613|0,613|0,613|0,2%|0,2%|
|R_27|Estación COEMIN|0,181|0,241|0,241|0,241|0,1%|0,1%|

www.dfmconsultores.cl

130

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Material Particulado Sedimentable (MPS)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**Media**<br>**Anual**|**Máxima**<br>**Media**<br>**Mensual**|**Conf. Suiza**|**República**<br>**Argentina**|**Conf. Suiza**|**República**<br>**Argentina**|
|R_28|Estación Nantoco|0,448|0,532|||0,2%|0,2%|
|R_29|Estación C6|0,264|0,350|0,350|0,350|0,1%|0,1%|
|R_30|Estación C5|0,212|0,292|0,292|0,292|0,1%|0,1%|
|R_31|Estación C8|0,366|0,487|0,487|0,487|0,2%|0,1%|
|R_32|Estación C2|0,105|0,162|0,162|0,162|0,1%|0,0%|
|R_33|Estación C1|0,111|0,169|0,169|0,169|0,1%|0,1%|
|R_34|Estación C3|0,105|0,164|0,164|0,164|0,1%|0,0%|
|R_35|Estación C7|0,349|0,470|0,470|0,470|0,2%|0,1%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes proyectados del Proyecto sobre los

receptores de interés alcanzan un máximo de 9,8% y 6,8% de la norma de referencia para

periodo anual de la Confederación Suiza, particularmente sobre los receptores

denominados “R_18” y “R_20”, los que corresponden a viviendas construidas con material

mixto y material ligero respectivamente. Por su parte, en cuanto a los valores proyectados

de depositación de MPS mensuales estimados, estos representan hasta un 7,5% y 4,6% de

la norma de referencia para periodo mensual de la República de Argentina, específicamente

en los receptores ya mencionados.

A continuación, en las siguientes figuras se presentan las curvas de isodepositación de

material particulado sedimentable (MPS) para periodo mensual y anual.

www.dfmconsultores.cl

131

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-61. Curvas de isodepositación para periodo mensual. MPS [mg/m** **[2]** **∙día]. Fase de Operación**

**Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

132

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-62. Curvas de isodepositación para periodo anual. MPS [mg/m** **[2]** **∙día]. Fase de Operación**

**Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

133

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.2.3.4 Monóxido de Carbono (CO)

En la Tabla 5-36 se presentan los aportes generados durante la fase de operación

proyectada del Proyecto sobre los receptores de interés, específicamente sobre receptores

de medio humano y estaciones de monitoreo, conforme con la norma primaria para

monóxido de carbono (CO).

**Tabla 5-36. Resultados del modelo de dispersión para CO [mg/m** **[3]** **N]. Fase de Operación Proyectada.**

|Receptor|Descripción|Monóxido de Carbono (CO)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[mg/m3N]**|**Concentración**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|
|R_1|Estación Luis Uribe|0,006|0,002|30|10|0,0%|0,0%|
|R_2|Estación Tierra Amarilla|0,010|0,004|0,004|0,004|0,0%|0,0%|
|R_3|Estación Ojanco|0,015|0,004|0,004|0,004|0,0%|0,0%|
|R_4|Estación Kozan|0,033|0,008|0,008|0,008|0,1%|0,1%|
|R_5|133 casa (Carola Norte)|0,006|0,002|0,002|0,002|0,0%|0,0%|
|R_6|Iglesia Tierra Amarilla|0,006|0,003|0,003|0,003|0,0%|0,0%|
|R_7|El Minero|0,071|0,011|0,011|0,011|0,2%|0,1%|
|R_8|Testigoteca|0,055|0,008|0,008|0,008|0,2%|0,1%|
|R_9|Estadio|0,145|0,027|0,027|0,027|0,5%|0,3%|
|R_10|Agrouva I|0,080|0,014|0,014|0,014|0,3%|0,1%|
|R_11|Agrouva II|0,019|0,005|0,005|0,005|0,1%|0,0%|
|R_12|Receptor ruido|0,054|0,008|0,008|0,008|0,2%|0,1%|
|R_13|Receptor ruido|0,051|0,008|0,008|0,008|0,2%|0,1%|
|R_14|Receptor ruido|0,033|0,006|0,006|0,006|0,1%|0,1%|
|R_15|Receptor ruido|0,085|0,016|0,016|0,016|0,3%|0,2%|
|R_16|Receptor ruido|0,100|0,018|0,018|0,018|0,3%|0,2%|
|R_17|Receptor ruido|0,063|0,011|0,011|0,011|0,2%|0,1%|
|R_18|Receptor ruido|0,309|0,063|0,063|0,063|1,0%|0,6%|
|R_19|Receptor ruido|0,151|0,030|0,030|0,030|0,5%|0,3%|
|R_20|Receptor ruido|0,202|0,034|0,034|0,034|0,7%|0,3%|
|R_21|Receptor ruido|0,167|0,029|0,029|0,029|0,6%|0,3%|
|R_22|Receptor ruido|0,084|0,018|0,018|0,018|0,3%|0,2%|
|R_23|Receptor ruido|0,003|0,001|0,001|0,001|0,0%|0,0%|
|R_24|Receptor ruido|0,001|0,000|0,000|0,000|0,0%|0,0%|
|R_25|Receptor ruido|0,001|0,000|0,000|0,000|0,0%|0,0%|
|R_26|Receptor ruido|0,002|0,001|0,001|0,001|0,0%|0,0%|
|R_27|Estación COEMIN|0,003|0,001|0,001|0,001|0,0%|0,0%|
|R_28|Estación Nantoco|0,002|0,001|0,001|0,001|0,0%|0,0%|

www.dfmconsultores.cl

134

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Monóxido de Carbono (CO)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[mg/m3N]**|**Concentración**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|
|R_29|Estación C6|0,001|0,000|||0,0%|0,0%|
|R_30|Estación C5|0,001|0,000|0,000|0,000|0,0%|0,0%|
|R_31|Estación C8|0,002|0,000|0,000|0,000|0,0%|0,0%|
|R_32|Estación C2|0,001|0,000|0,000|0,000|0,0%|0,0%|
|R_33|Estación C1|0,001|0,000|0,000|0,000|0,0%|0,0%|
|R_34|Estación C3|0,001|0,000|0,000|0,000|0,0%|0,0%|
|R_35|Estación C7|0,002|0,000|0,000|0,000|0,0%|0,0%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes proyectados del Proyecto sobre los

receptores de interés alcanzan un máximo de 1,0% y 0,7% de la norma de este

contaminante en periodo horario, específicamente sobre los receptores denominados

“R_18” y “R_20”, los que corresponden a viviendas construidas con material mixto y

material ligero respectivamente. Mientras que, para periodo de 8 horas, las

concentraciones proyectadas estimadas no sobrepasan el 0,6% de la norma respectiva,

particularmente en el receptor “R_18”. En consecuencia, es posible establecer que las

contribuciones proyectadas del Proyecto sobre los receptores de interés, en cuanto a

emisiones de CO, es prácticamente mínima.

En consecuencia, considerando que los aportes de concentración de CO percibidos en los

receptores son menores a 1,5 mg/m [3] N en periodo horario y 0,4889 mg/m [3] N en periodo de

ocho horas, valores correspondientes a los límites de los Niveles de Impacto Significativo

para este contaminante según lo indicado en el documento “Evaluación Significancia del

Impacto de las Emisiones de un Proyecto o Actividad en Zonas Saturadas en el Marco del

SEIA” (DICTUC, 2022), en esta oportunidad no se presentan curvas de isoconcentración de

monóxido de carbono asociadas a la fase de operación proyectada del Proyecto.

www.dfmconsultores.cl

135

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.2.3.5 Dióxido de Nitrógeno (NO 2 )

En la Tabla 5-37 se presentan los aportes generados durante la fase de operación

proyectada del Proyecto sobre los receptores de interés, específicamente sobre receptores

de medio humano y estaciones de monitoreo, conforme con la norma primaria para dióxido

de nitrógeno (NO 2 ).

**Tabla 5-37. Resultados del modelo de dispersión para NO** **2** **[μg/m** **[3]** **N]. Fase de Operación Proyectada.**

|Receptor|Descripción|Dióxido de Nitrógeno (NO )<br>2|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|6,455|0,465|400|100|1,6%|0,5%|
|R_2|Estación Tierra Amarilla|10,570|0,807|0,807|0,807|2,6%|0,8%|
|R_3|Estación Ojanco|16,156|0,515|0,515|0,515|4,0%|0,5%|
|R_4|Estación Kozan|30,111|0,678|0,678|0,678|7,5%|0,7%|
|R_5|133 casa (Carola Norte)|4,753|0,325|0,325|0,325|1,2%|0,3%|
|R_6|Iglesia Tierra Amarilla|6,207|0,623|0,623|0,623|1,6%|0,6%|
|R_7|El Minero|51,024|0,936|0,936|0,936|12,8%|0,9%|
|R_8|Testigoteca|38,051|0,515|0,515|0,515|9,5%|0,5%|
|R_9|Estadio|104,420|1,851|1,851|1,851|26,1%|1,9%|
|R_10|Agrouva I|61,445|1,305|1,305|1,305|15,4%|1,3%|
|R_11|Agrouva II|21,263|0,818|0,818|0,818|5,3%|0,8%|
|R_12|Receptor ruido|41,977|0,572|0,572|0,572|10,5%|0,6%|
|R_13|Receptor ruido|38,835|0,486|0,486|0,486|9,7%|0,5%|
|R_14|Receptor ruido|22,143|0,406|0,406|0,406|5,5%|0,4%|
|R_15|Receptor ruido|43,253|0,930|0,930|0,930|10,8%|0,9%|
|R_16|Receptor ruido|58,380|1,103|1,103|1,103|14,6%|1,1%|
|R_17|Receptor ruido|42,251|0,740|0,740|0,740|10,6%|0,7%|
|R_18|Receptor ruido|220,030|2,929|2,929|2,929|55,0%|2,9%|
|R_19|Receptor ruido|120,800|1,900|1,900|1,900|30,2%|1,9%|
|R_20|Receptor ruido|140,250|2,455|2,455|2,455|35,1%|2,5%|
|R_21|Receptor ruido|118,240|2,211|2,211|2,211|29,6%|2,2%|
|R_22|Receptor ruido|65,755|1,050|1,050|1,050|16,4%|1,1%|
|R_23|Receptor ruido|2,039|0,067|0,067|0,067|0,5%|0,1%|
|R_24|Receptor ruido|1,320|0,059|0,059|0,059|0,3%|0,1%|
|R_25|Receptor ruido|0,534|0,038|0,038|0,038|0,1%|0,0%|
|R_26|Receptor ruido|2,556|0,133|0,133|0,133|0,6%|0,1%|
|R_27|Estación COEMIN|2,138|0,067|0,067|0,067|0,5%|0,1%|
|R_28|Estación Nantoco|1,977|0,131|0,131|0,131|0,5%|0,1%|

www.dfmconsultores.cl

136

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Dióxido de Nitrógeno (NO )<br>2|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|
|R_29|Estación C6|1,584|0,085|||0,4%|0,1%|
|R_30|Estación C5|1,267|0,073|0,073|0,073|0,3%|0,1%|
|R_31|Estación C8|1,785|0,099|0,099|0,099|0,4%|0,1%|
|R_32|Estación C2|0,741|0,041|0,041|0,041|0,2%|0,0%|
|R_33|Estación C1|0,838|0,043|0,043|0,043|0,2%|0,0%|
|R_34|Estación C3|0,715|0,041|0,041|0,041|0,2%|0,0%|
|R_35|Estación C7|1,736|0,095|0,095|0,095|0,4%|0,1%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes proyectados del Proyecto sobre los

receptores de interés alcanzan un máximo de 55,0% y 35,1% de la norma de este

contaminante en periodo horario, específicamente sobre los receptores denominados

“R_18” y “R_20”, los que corresponden a viviendas construidas con material mixto y

material ligero respectivamente. Por su parte, en cuanto a las concentraciones proyectadas

de NO 2 estimadas para periodo anual, estas representan hasta un 2,9% y 2,5% de la

normativa respectiva, particularmente en los receptores ya indicados.

A continuación, en las siguientes figuras se presentan las curvas de isoconcentración de

dióxido de nitrógeno (NO 2 ) para periodo de 1 hora y periodo anual.

www.dfmconsultores.cl

137

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-63. Curvas de isoconcentración para percentil 99 periodo 1 hora. NO** **2** **[μg/m** **[3]** **N]. Fase de**

**Operación Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

138

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 5-64. Curvas de isoconcentración para periodo anual. NO** **2** **[μg/m** **[3]** **N]. Fase de Operación**

**Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

139

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

5.9.2.3.6 Dióxido de Azufre (SO 2 )

En la Tabla 5-38 se presentan los aportes generados durante la fase de operación proyectada del Proyecto sobre los receptores de

interés, específicamente sobre receptores de medio humano y estaciones de monitoreo, conforme con la norma primaria para dióxido

de azufre (SO 2 ).

**Tabla 5-38. Resultados del modelo de dispersión para SO** **2** **[μg/m** **[3]** **N]. Fase de Operación Proyectada.**

|Receptor|Descripción|Dióxido de Azufre (SO )<br>2|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|0,009|0,003|0,001|350|150|60|0,0%|0,0%|0,0%|
|R_2|Estación Tierra Amarilla|0,016|0,005|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_3|Estación Ojanco|0,020|0,004|0,001|0,001|0,001|0,001|0,0%|0,0%|0,0%|
|R_4|Estación Kozan|0,024|0,011|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_5|133 casa (Carola Norte)|0,007|0,002|0,001|0,001|0,001|0,001|0,0%|0,0%|0,0%|
|R_6|Iglesia Tierra Amarilla|0,011|0,004|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_7|El Minero|0,063|0,013|0,004|0,004|0,004|0,004|0,0%|0,0%|0,0%|
|R_8|Testigoteca|0,038|0,011|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_9|Estadio|0,096|0,037|0,006|0,006|0,006|0,006|0,0%|0,0%|0,0%|
|R_10|Agrouva I|0,051|0,019|0,004|0,004|0,004|0,004|0,0%|0,0%|0,0%|
|R_11|Agrouva II|0,022|0,006|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_12|Receptor ruido|0,040|0,011|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_13|Receptor ruido|0,032|0,010|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_14|Receptor ruido|0,029|0,007|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_15|Receptor ruido|0,106|0,018|0,005|0,005|0,005|0,005|0,0%|0,0%|0,0%|
|R_16|Receptor ruido|0,126|0,020|0,006|0,006|0,006|0,006|0,0%|0,0%|0,0%|
|R_17|Receptor ruido|0,069|0,015|0,003|0,003|0,003|0,003|0,0%|0,0%|0,0%|

www.dfmconsultores.cl

140

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Dióxido de Azufre (SO )<br>2|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|
|R_18|Receptor ruido|0,270|0,067|0,012||||0,1%|0,0%|0,0%|
|R_19|Receptor ruido|0,101|0,041|0,006|0,006|0,006|0,006|0,0%|0,0%|0,0%|
|R_20|Receptor ruido|0,150|0,050|0,009|0,009|0,009|0,009|0,0%|0,0%|0,0%|
|R_21|Receptor ruido|0,134|0,033|0,008|0,008|0,008|0,008|0,0%|0,0%|0,0%|
|R_22|Receptor ruido|0,046|0,019|0,003|0,003|0,003|0,003|0,0%|0,0%|0,0%|
|R_23|Receptor ruido|0,002|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_24|Receptor ruido|0,002|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_25|Receptor ruido|0,001|0,000|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_26|Receptor ruido|0,003|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_27|Estación COEMIN|0,002|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_28|Estación Nantoco|0,003|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_29|Estación C6|0,002|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_30|Estación C5|0,002|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_31|Estación C8|0,002|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_32|Estación C2|0,001|0,000|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_33|Estación C1|0,001|0,000|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_34|Estación C3|0,001|0,000|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_35|Estación C7|0,002|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

141

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Tal como se observa en la tabla anterior, los aportes proyectados del Proyecto sobre los

receptores de interés no superan el 0,1% de la norma de este contaminante en periodo

horario, específicamente sobre el receptor denominado “R_18”, el cual corresponde a

viviendas construidas con material mixto. Mientras que, para periodo diario y anual, las

concentraciones proyectadas estimadas no sobrepasan el 0,0% de las normativas

respectivas, en cada uno de los receptores estudiados. En consecuencia, es posible

establecer que la contribución proyectada del Proyecto sobre los receptores de interés, en

cuanto a emisiones de SO 2, es prácticamente nula.

En consecuencia, considerando que los aportes de concentración de SO 2 percibidos en los

receptores son menores a 14,0 μg/m [3] N en periodo horario, 2,0 μg/m [3] N en periodo diario y

1,2 μg/m [3] N en periodo anual, valores correspondientes a los límites de los Niveles de

Impacto Significativo para este contaminante según lo indicado en el documento

“Evaluación Significancia del Impacto de las Emisiones de un Proyecto o Actividad en Zonas

Saturadas en el Marco del SEIA” (DICTUC, 2022), en esta oportunidad no se presentan

curvas de isoconcentración de dióxido de azufre asociadas a la fase de operación

proyectada del Proyecto.

www.dfmconsultores.cl

142

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

#### 5.10 Análisis de Significancia de Operación del Proyecto

En consideración de la condición de calidad del aire actual en la zona de emplazamiento del

Proyecto, particularmente a lo establecido por el Decreto N°15/2021 del Ministerio del

Medio Ambiente, el cual declara zona saturada por material particulado respirable (MP10)

como concentración de 24 horas y anual a la zona de Copiapó y Tierra Amarilla, a

continuación, se presenta la variación entre los aportes del contaminante indicado

asociados al escenario de operación actual y proyectado del Proyecto sobre cada uno de los

receptores de interés, y además su comparación con los niveles de impacto significativo

(SILs) establecidos por la autoridad.

Cabe mencionar que, los SILs considerados en el presente análisis corresponden a aquellos

aportes de concentración de material particulado respirable sobre receptores humanos

consideradas significativas para la evaluación de impacto en un escenario de riesgo

preexistente, particularmente para un periodo de desarrollo de obras y actividades igual o

mayor a tres años, establecidos en el documento “Criterio de evaluación en el SEIA: Impacto

de emisiones en zonas saturadas por material particulado respirable MP10 y material

particulado respirable fino MP2.5”, elaborado por el Servicio de Evaluación Ambiental y

vigente desde septiembre de 2023 por medio de la Resolución Exenta

N°202399101721/2023 [5] .

Es necesario indicar que, de manera conservadora, se ha considerado un aporte nulo en las

situaciones en donde las concentraciones de material particulado respirable actuales

superan aquellas proyectadas.

**Tabla 5-39. Análisis de Significancia Fase de Operación. MP10** **[μg/m** **[3]** **N]** **.**

|Receptor|Nivel de Impacto Significativo|Col3|Col4|Escenario Actual|Col6|Escenario Proyectado|Col8|Variación|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% SILs**|**Valor**|**% SILs**|**Valor**|**% SILs**|
|R_1|P98 24 horas|5|μg/m3N|1,49|29,7%|1,54|30,7%|0,05|1,0%|
|R_1|Media anual|1|μg/m3N|0,73|72,6%|0,74|73,8%|0,01|1,1%|
|R_2|P98 24 horas|5|μg/m3N|2,45|49,1%|2,55|51,0%|0,10|1,9%|
|R_2|Media anual|1|μg/m3N|1,23|123,1%|1,27|126,9%|0,04|3,8%|
|R_3|P98 24 horas|5|μg/m3N|2,16|43,2%|2,22|44,5%|0,06|1,2%|
|R_3|Media anual|1|μg/m3N|0,85|84,9%|0,85|84,8%|0,00|-0,1%|

5 [Link web: https://www.sea.gob.cl/sites/default/files/imce/archivos/2023/09/08/DT_Zonas-Saturadas_MP](https://www.sea.gob.cl/sites/default/files/imce/archivos/2023/09/08/DT_Zonas-Saturadas_MP%20_2023.pdf)
[_2023.pdf](https://www.sea.gob.cl/sites/default/files/imce/archivos/2023/09/08/DT_Zonas-Saturadas_MP%20_2023.pdf)

www.dfmconsultores.cl

143

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Nivel de Impacto Significativo|Col3|Col4|Escenario Actual|Col6|Escenario Proyectado|Col8|Variación|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% SILs**|**Valor**|**% SILs**|**Valor**|**% SILs**|
|R_4|P98 24 horas|5|μg/m3N|4,89|97,9%|4,99|99,8%|0,10|1,9%|
|R_4|Media anual|1|μg/m3N|1,36|136,5%|1,25|125,3%|0,00|0,0%|
|R_5|P98 24 horas|5|μg/m3N|1,80|36,0%|0,21|4,2%|0,00|0,0%|
|R_5|Media anual|1|μg/m3N|0,94|94,3%|0,11|11,3%|0,00|0,0%|
|R_6|P98 24 horas|5|μg/m3N|2,06|41,2%|2,03|40,6%|0,00|0,0%|
|R_6|Media anual|1|μg/m3N|1,04|104,4%|1,02|101,6%|0,00|0,0%|
|R_7|P98 24 horas|5|μg/m3N|6,69|133,8%|7,21|144,1%|0,51|10,3%|
|R_7|Media anual|1|μg/m3N|2,14|214,0%|2,19|218,6%|0,05|4,6%|
|R_8|P98 24 horas|5|μg/m3N|4,24|84,8%|4,48|89,5%|0,24|4,7%|
|R_8|Media anual|1|μg/m3N|1,26|125,9%|1,24|123,6%|0,00|0,0%|
|R_9|P98 24 horas|5|μg/m3N|16,95|339,0%|14,96|299,2%|0,00|0,0%|
|R_9|Media anual|1|μg/m3N|5,68|567,8%|4,41|440,7%|0,00|0,0%|
|R_10|P98 24 horas|5|μg/m3N|9,62|192,4%|9,03|180,6%|0,00|0,0%|
|R_10|Media anual|1|μg/m3N|3,41|340,5%|2,78|277,7%|0,00|0,0%|
|R_11|P98 24 horas|5|μg/m3N|3,32|66,3%|3,26|65,2%|0,00|0,0%|
|R_11|Media anual|1|μg/m3N|1,48|148,3%|1,42|141,8%|0,00|0,0%|
|R_12|P98 24 horas|5|μg/m3N|4,22|84,3%|4,42|88,3%|0,20|4,0%|
|R_12|Media anual|1|μg/m3N|1,33|132,7%|1,28|128,4%|0,00|0,0%|
|R_13|P98 24 horas|5|μg/m3N|3,89|77,9%|4,10|82,0%|0,21|4,1%|
|R_13|Media anual|1|μg/m3N|1,14|113,9%|1,11|110,7%|0,00|0,0%|
|R_14|P98 24 horas|5|μg/m3N|3,14|62,9%|3,38|67,6%|0,24|4,7%|
|R_14|Media anual|1|μg/m3N|1,01|101,0%|0,96|96,4%|0,00|0,0%|
|R_15|P98 24 horas|5|μg/m3N|8,70|174,1%|9,36|187,3%|0,66|13,2%|
|R_15|Media anual|1|μg/m3N|2,91|291,5%|2,97|297,1%|0,06|5,6%|
|R_16|P98 24 horas|5|μg/m3N|10,06|201,2%|10,75|215,0%|0,69|13,7%|
|R_16|Media anual|1|μg/m3N|3,18|317,6%|3,30|330,0%|0,12|12,3%|
|R_17|P98 24 horas|5|μg/m3N|6,28|125,5%|6,48|129,7%|0,21|4,2%|
|R_17|Media anual|1|μg/m3N|1,94|194,1%|1,93|192,5%|0,00|0,0%|
|R_18|P98 24 horas|5|μg/m3N|33,66|673,2%|36,58|731,6%|2,92|58,4%|
|R_18|Media anual|1|μg/m3N|7,18|718,5%|7,46|745,8%|0,27|27,3%|
|R_19|P98 24 horas|5|μg/m3N|21,22|424,4%|18,37|367,4%|0,00|0,0%|
|R_19|Media anual|1|μg/m3N|7,05|704,9%|4,97|497,2%|0,00|0,0%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

144

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Nivel de Impacto Significativo|Col3|Col4|Escenario Actual|Col6|Escenario Proyectado|Col8|Variación|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% SILs**|**Valor**|**% SILs**|**Valor**|**% SILs**|
|R_20|P98 24 horas|5|μg/m3N|19,10|381,9%|19,31|386,3%|0,22|4,4%|
|R_20|Media anual|1|μg/m3N|6,31|630,5%|5,67|566,6%|0,00|0,0%|
|R_21|P98 24 horas|5|μg/m3N|17,32|346,5%|16,48|329,6%|0,00|0,0%|
|R_21|Media anual|1|μg/m3N|6,44|643,5%|5,30|530,4%|0,00|0,0%|
|R_22|P98 24 horas|5|μg/m3N|10,66|213,1%|10,65|213,0%|0,00|0,0%|
|R_22|Media anual|1|μg/m3N|2,46|246,5%|2,18|217,6%|0,00|0,0%|
|R_23|P98 24 horas|5|μg/m3N|0,48|9,6%|0,49|9,9%|0,01|0,3%|
|R_23|Media anual|1|μg/m3N|0,14|13,8%|0,13|13,3%|0,00|0,0%|
|R_24|P98 24 horas|5|μg/m3N|0,35|7,0%|0,35|7,0%|0,00|0,0%|
|R_24|Media anual|1|μg/m3N|0,12|11,9%|0,12|11,6%|0,00|0,0%|
|R_25|P98 24 horas|5|μg/m3N|0,20|4,0%|0,20|4,0%|0,00|0,0%|
|R_25|Media anual|1|μg/m3N|0,08|7,7%|0,08|7,6%|0,00|0,0%|
|R_26|P98 24 horas|5|μg/m3N|0,53|10,7%|0,51|10,1%|0,00|0,0%|
|R_26|Media anual|1|μg/m3N|0,24|24,0%|0,23|23,4%|0,00|0,0%|
|R_27|P98 24 horas|5|μg/m3N|0,52|10,4%|0,51|10,3%|0,00|0,0%|
|R_27|Media anual|1|μg/m3N|0,14|13,9%|0,13|13,4%|0,00|0,0%|
|R_28|P98 24 horas|5|μg/m3N|0,55|10,9%|0,54|10,8%|0,00|0,0%|
|R_28|Media anual|1|μg/m3N|0,25|25,1%|0,24|24,4%|0,00|0,0%|
|R_29|P98 24 horas|5|μg/m3N|0,43|8,5%|0,42|8,3%|0,00|0,0%|
|R_29|Media anual|1|μg/m3N|0,17|17,2%|0,17|16,7%|0,00|0,0%|
|R_30|P98 24 horas|5|μg/m3N|0,37|7,4%|0,36|7,2%|0,00|0,0%|
|R_30|Media anual|1|μg/m3N|0,15|14,7%|0,14|14,3%|0,00|0,0%|
|R_31|P98 24 horas|5|μg/m3N|0,48|9,6%|0,47|9,4%|0,00|0,0%|
|R_31|Media anual|1|μg/m3N|0,21|20,8%|0,20|19,8%|0,00|0,0%|
|R_32|P98 24 horas|5|μg/m3N|0,21|4,2%|0,21|4,2%|0,00|0,0%|
|R_32|Media anual|1|μg/m3N|0,08|8,2%|0,08|8,1%|0,00|0,0%|
|R_33|P98 24 horas|5|μg/m3N|0,22|4,5%|0,22|4,4%|0,00|0,0%|
|R_33|Media anual|1|μg/m3N|0,09|8,6%|0,08|8,5%|0,00|0,0%|
|R_34|P98 24 horas|5|μg/m3N|0,21|4,2%|0,21|4,2%|0,00|0,0%|
|R_34|Media anual|1|μg/m3N|0,08|8,2%|0,08|8,1%|0,00|0,0%|
|R_35|P98 24 horas|5|μg/m3N|0,46|9,3%|0,45|9,1%|0,00|0,0%|
|R_35|Media anual|1|μg/m3N|0,20|20,1%|0,19|19,1%|0,00|0,0%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

145

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Conforme a los resultados de la tabla anterior, es posible observar que gran parte de los

receptores de interés estudiados presenta una disminución de los aportes de material

particulado respirable del Proyecto durante el desarrollo de la fase de operación proyectada

en comparación con aquellos valores estimados para la fase de operación actual. De este

modo, y de manera conservadora, se establece una variación nula de las concentraciones

de MP10 en los receptores denominados “R_5”, “R_6”, “R_9”, “R_10”, “R_11”, R_19”,

“R_21”, “R_22”, “R_24”, R_25”, R_26”, R_27”, R_28”, R_29”, R_30”, R_32”, R_33”, R_34” y

“R_35”. En consecuencia, tales concentraciones representan aportes insignificantes en

comparación a los valores de impacto significativo indicados para este contaminante.

En cambio, es posible identificar que, los receptores denominados “R_3”, “R_4”, “R_8”,

“R_12”, “R_13”, “R_14”, “R_17”, “R_20” y “R_23”, correspondientes a estaciones de

monitoreo, oficinas, sectores de trabajo y viviendas habitacionales, presentan un aumento

en los aportes de MP10 en periodo diario durante el escenario proyectado del Proyecto,

incrementando las concentraciones en hasta 0,24 [μg/m [3] N]. Por su parte, los receptores

denominados “R_1”, “R_2”, “R_7”, “R_15”, “R_16” y “R_18”, correspondientes a estaciones

de monitoreo, sectores de trabajo y viviendas habitacionales, presentan un aumento en los

aportes de MP10 en periodo diario y anual durante el escenario ya indicado, incrementando

las concentraciones en hasta 2,92 y 0,27 [μg/m [3] N] en periodo diario y anual

respectivamente.

No obstante, las magnitudes mencionadas en el párrafo anterior se encuentran por bajo los

límites de impacto significativo establecidos por el documento señalado con anterioridad,

por lo que se descarta la afectación sobre el riesgo de salud de la población, en cuanto a

calidad del aire se trata, como consecuencia del desarrollo de las futuras obras del Proyecto.

www.dfmconsultores.cl

146

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

### 6 ÁREA DE INFLUENCIA

Tomando en consideración lo señalado en los artículos 5 y 6 del Reglamento del SEIA (D.S.
N°40/2012), así como lo estipulado en la “Guía Calidad del Aire en el Área de Influencia de

Proyectos que ingresan al SEIA” (SEA, 2015) para la definición del área de influencia

asociada al desarrollo de obras y actividades de un proyecto, y en función de evaluar el

riesgo a la salud de la población y la afectación de los recursos naturales renovables debido

a la calidad del aire presente en la zona, en el presente estudio se han considerado criterios

sobre la base de los receptores sensibles en los cuales existe un objeto de protección, con

norma primaria o secundaria vigente en Chile, o alguna norma de referencia de los estados

indicados en el artículo 11 del Reglamento.

Lo anterior se realiza en función de establecer si, con los aportes de concentración de

contaminantes atmosféricos generados por el Proyecto, se produce o no una superación de

los limites normativos de los distintos parámetros de las concentraciones ambientales.

De esta manera, considerando los receptores sensibles identificados en el presente estudio

y la zona de emplazamiento del Proyecto, correspondiente a zona saturada por material

particulado respirable como concentración de 24 horas y anual conforme a lo señalado en

el Decreto N°15/2021 del Ministerio del Medio Ambiente [6], el área de influencia se define

en base a los criterios indicados en el documento “Criterio de evaluación en el SEIA: Impacto

de emisiones en zonas saturadas por material particulado respirable MP10 y material

particulado respirable fino MP2.5”, elaborado por el Servicio de Evaluación Ambiental y

vigente desde septiembre de 2023 por medio de la Resolución Exenta

N°202399101721/2023 [7] .

Así, los valores de impacto significativo por considerar para MP2.5 y MP10 corresponden a

aquellos expuestos en la Tabla 1 del documento señalado, los cuales se asocian al aumento

de concentraciones de MP10 y MP2.5 sobre receptores humanos en un período igual o

mayor a 3 años en zonas que sobrepasan el valor de las normas primarias de calidad del

aire correspondientes para cada contaminante en sus distintos periodos de análisis.

Por su parte, el área de influencia asociada a las normativas primarias de calidad del aire de

gases tales como dióxido de azufre (SO 2 ), dióxido de nitrógeno (NO 2 ) y monóxido de

6 [Link web: https://www.bcn.cl/leychile/navegar?idNorma=1166716](https://www.bcn.cl/leychile/navegar?idNorma=1166716)
7 [Link web: https://www.sea.gob.cl/sites/default/files/imce/archivos/2023/09/08/DT_Zonas-](https://www.sea.gob.cl/sites/default/files/imce/archivos/2023/09/08/DT_Zonas-Saturadas_MP_2023.pdf)
[Saturadas_MP_2023.pdf](https://www.sea.gob.cl/sites/default/files/imce/archivos/2023/09/08/DT_Zonas-Saturadas_MP_2023.pdf)

www.dfmconsultores.cl

147

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

carbono (CO), se ha definido en base a los Niveles de Impacto Significativo (SILs), los cuales

corresponden a las variaciones en las concentraciones en el aire ambiental de los

contaminantes criterio consideradas intrascendentes en comparación a los Estándares

Nacionales de Calidad del Aire (NAAQS [8] ) y a la variabilidad propia de las concentraciones de

cada contaminante respecto a las registros de monitoreo respectivos, las que de acuerdo

con el documento “Evaluación Significancia del Impacto de las Emisiones de un Proyecto o

Actividad en Zonas Saturadas en el Marco del SEIA”, elaborado por DICTUC para el SEA

(2022), corresponden a los valores presentados en la Tabla 7-5 del mencionado informe.

De este modo, en la Tabla 6-1 se presentan los valores de impacto significativo considerados

para cada contaminante conforme a los criterios señalados con anterioridad.

**Tabla 6-1. Valores de significancia para la evaluación de impacto significativo en un escenario de riesgo**

**preexistente.**

|Contaminante|Período|SIL Porcentual<br>US EPA|Incremento Significativo en<br>la Concentración [ug/m3]|Referencia|
|---|---|---|---|---|
|MP2.5|24 horas|3,4%|1,71|Tabla 1. Capítulo 4. “Criterio de<br>Evaluación en el SEIA: Impacto de<br>emisiones en zonas saturadas por<br>material particulado respirable<br>MP10 y material particulado fino<br>respirable MP2.5” (SEA, 2023).|
|MP2.5|Anual|1,7%|0,33|0,33|
|MP10|24 horas|3,3%|5,00|5,00|
|MP10|Anual|2,0%|1,00|1,00|
|NO2|1 hora|4,0%|16,00|Tabla 7-5, Capítulo 8. “Evaluación<br>Significancia del Impacto de las<br>Emisiones de un Proyecto o<br>Actividad en Zonas Saturadas en el<br>Marco del SEIA” (DICTUC, 2022)|
|NO2|Anual|1,0%|1,00|1,00|
|CO|1 hora|5,0%|1.500,00|1.500,00|
|CO|8 horas|4,9%|488,90|488,90|
|SO2|1 hora|4,0%|14,00|14,00|
|SO2|24 horas|1,4%|2,00|2,00|
|SO2|Anual|2,0%|1,20|1,20|

Fuente: Elaboración propia.

Es necesario indicar que aquellas variaciones de concentración por debajo de los valores

indicados en la tabla precedente son considerados estadísticamente no significativos, toda

vez que desde un punto de vista estadístico no se pueden diferenciar de la variabilidad

observada en las mediciones.

8 NAAQS: National Ambient Air Quality Standards.

www.dfmconsultores.cl

148

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Por tanto, se han considerado dichos valores para la determinación del área de influencia

del Proyecto para ambos escenarios en estudio, de modo que esta represente la superficie

en donde la ejecución del Proyecto podría modificar de manera estadísticamente

significativa la concentración ambiental de algunos de los contaminantes atmosféricos

regulados por la normativa ambiental nacional vigente.

#### 6.1 Área de Influencia Base

De acuerdo con los criterios mencionados con anterioridad, a continuación, en la siguiente

figura se presenta el área de influencia para la componente calidad del aire asociada al

desarrollo de la fase de operación actual del Proyecto, la cual corresponde a la combinación

de las curvas de límite de significancia estadística para los aportes de material particulado

respirable fino en periodo diario y anual, material particulado respirable en periodo diario

y anual, y dióxido de nitrógeno en periodo horario y anual.

www.dfmconsultores.cl

149

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 6-1. Área de Influencia del Proyecto para Normas Primarias de Calidad de Aire. Fase de Operación**

**Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

150

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

#### 6.2 Área de Influencia Proyectada

De acuerdo con los criterios mencionados en la Tabla 6-1, a continuación, en la siguiente

figura se presenta el área de influencia para la componente calidad del aire asociada al

desarrollo de la fase de operación proyectada del Proyecto, la cual corresponde a la

combinación de las curvas de límite de significancia estadística para los aportes de material

particulado respirable fino en periodo diario y anual, material particulado respirable en

periodo diario y anual, y dióxido de nitrógeno en periodo horario y anual.

www.dfmconsultores.cl

151

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 6-2. Área de Influencia del Proyecto para Normas Primarias de Calidad de Aire. Fase de Operación**

**Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

152

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

### 7 EFECTO SINÉRGICO PROYECTO “OPTIMIZACIÓN OPERACIONAL MINA CAROLA”

El proyecto “Optimización Operacional Planta Cerrillos” corresponde al aumento de

procesamiento de mineral en Planta Cerrillos, incrementando la producción actual 240.000

[t/mes] de concentrado de cobre, aprobada mediante la RCA N°349/2008, en hasta 264.000

[t/mes].

Tal modificación se relaciona directamente con el aumento del ritmo de extracción de

mineral desde la faena subterránea de Mina Carola presentada a evaluación ambiental en

este estudio, pues el mineral extraído es transportado hacia Planta Cerrillos para su

posterior transformación.

En consecuencia, considerando que ambos proyectos, es decir “Optimización Operacional

Mina Carola” y “Optimización Operacional Planta Cerrillos”, operan de manera simultánea

y se sustentan mutuamente, en la siguiente sección se presentan las modelaciones de

dispersión de contaminantes, específicamente de MP2.5, MP10, MPS, CO, NO 2 y SO 2,

correspondientes a los escenarios sinérgicos actuales y proyectados generados por la

ejecución de las fases de operación actual y futura de los proyectos en cuestión.

De modo que, a continuación, se presenta el detalle de la configuración de ambos modelos

desarrollados, especificando las fuentes emisoras y receptores considerados para cada

caso, además de los aportes de concentración y depositación resultantes para cada

escenario sinérgico de operación.

#### 7.1 Fuentes Emisoras Escenario Sinérgico

Las fuentes emisoras del escenario de modelación sinérgica de los proyectos “Optimización

Operacional Mina Carola” y “Optimización Operacional Planta Cerrillos”, tanto base como

proyectado, han sido georreferenciadas de acuerdo con la información proporcionada por

ingeniería del Proyecto, para posteriormente ser ingresadas al modelo de dispersión de

contaminantes.

Por tanto, en la Figura 7-1 se presentan las fuentes emisoras del tipo areal y caminos

considerados, mientras que en la Tabla 7-1 y Tabla 7-2 se muestra el detalle de las

características de las fuentes y las tasas de emisión asociadas a los escenarios sinérgicos de

las fases de operación base y proyectada respectivamente.

www.dfmconsultores.cl

153

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-1. Ubicación Fuentes Emisoras. Escenario Sinérgico Fase de Operación.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

154

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Tabla 7-1. Características de Fuentes Emisoras y Tasas de Emisión. Escenario Sinérgico Fase de Operación Base.**

|ID|Descripción|Tipo de fuente|Tasas de emisión|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Descripción**|**Tipo de fuente**|**MP2.5**|**MP10**|**MPS**|**NO**|**NO2 **|**SO2 **|**CO**|**Unidad**|
|SRC_1|Tramo C1|Camino|2,78 E-07|9,83 E-07|4,90 E-06|1,23 E-06|2,10 E-07|2,29 E-09|5,46 E-07|g/s/m|
|SRC_2|Tramo C2|Camino|1,40 E-06|5,60 E-06|2,89 E-05|1,71 E-06|2,92 E-07|3,06 E-09|7,28 E-07|g/s/m|
|SRC_3|Tramo C3|Camino|1,15 E-06|4,63 E-06|2,39 E-05|1,20 E-06|2,05 E-07|2,07 E-09|4,93 E-07|g/s/m|
|SRC_4|Tramo C4|Camino|8,87 E-08|3,12 E-07|1,56 E-06|3,13 E-07|5,34 E-08|6,53 E-10|1,53 E-07|g/s/m|
|SRC_5|Tramo C5|Camino|1,33 E-06|5,32 E-06|2,75 E-05|1,59 E-06|2,71 E-07|2,80 E-09|6,69 E-07|g/s/m|
|SRC_6|Tramo C6|Camino|2,13 E-06|8,69 E-06|4,51 E-05|1,06 E-06|1,81 E-07|1,82 E-09|4,35 E-07|g/s/m|
|SRC_7|Tramo C7|Camino|8,09 E-07|3,27 E-06|1,69 E-05|7,18 E-07|1,22 E-07|1,24 E-09|2,95 E-07|g/s/m|
|SRC_8|Tramo C9|Camino|8,31 E-07|3,35 E-06|1,74 E-05|7,42 E-07|1,26 E-07|1,28 E-09|3,05 E-07|g/s/m|
|SRC_9|Tramo C10|Camino|8,77 E-07|3,54 E-06|1,83 E-05|8,06 E-07|1,37 E-07|1,39 E-09|3,30 E-07|g/s/m|
|SRC_10|Tramo C11|Camino|5,30 E-08|2,10 E-07|1,08 E-06|8,42 E-08|1,44 E-08|1,44 E-10|3,42 E-08|g/s/m|
|SRC_11|Tramo C12|Camino|6,46 E-07|2,53 E-06|1,30 E-05|1,10 E-06|1,87 E-07|2,01 E-09|4,77 E-07|g/s/m|
|SRC_12|Tramo N1|Camino|6,62 E-07|6,43 E-06|2,61 E-05|4,62 E-07|7,87 E-08|8,79 E-10|2,13 E-07|g/s/m|
|SRC_13|Tramo N2|Camino|6,02 E-07|5,84 E-06|2,37 E-05|4,20 E-07|7,15 E-08|7,99 E-10|1,94 E-07|g/s/m|
|SRC_14|Tramo N3|Camino|2,80 E-07|2,68 E-06|1,09 E-05|2,94 E-07|5,01 E-08|5,36 E-10|1,34 E-07|g/s/m|
|SRC_15|Tramo N4|Camino|1,15 E-06|1,14 E-05|4,63 E-05|4,63 E-07|7,88 E-08|7,96 E-10|1,90 E-07|g/s/m|
|SRC_16|Tramo N5|Camino|1,02 E-06|1,00 E-05|4,08 E-05|4,07 E-07|6,94 E-08|7,00 E-10|1,67 E-07|g/s/m|
|SRC_17|Tramo S1|Camino|2,93 E-06|2,92 E-05|8,45 E-05|2,12 E-07|3,61 E-08|5,78 E-10|1,22 E-07|g/s/m|
|SRC_18|Tramo S2|Camino|3,11 E-06|3,10 E-05|8,96 E-05|2,25 E-07|3,83 E-08|6,13 E-10|1,30 E-07|g/s/m|
|SRC_19|Tramo S3|Camino|7,72 E-06|7,69 E-05|2,23 E-04|7,00 E-07|1,19 E-07|1,20 E-09|2,88 E-07|g/s/m|
|SRC_20|Tramo S4|Camino|2,14 E-05|2,14 E-04|6,18 E-04|1,43 E-06|2,43 E-07|2,87 E-09|6,55 E-07|g/s/m|
|SRC_21|Tramo P1|Camino|2,48 E-08|9,32 E-08|4,73 E-07|8,55 E-08|1,46 E-08|1,47 E-10|3,51 E-08|g/s/m|
|SRC_22|Tramo P2|Camino|2,77 E-08|1,04 E-07|5,28 E-07|9,55 E-08|1,63 E-08|1,64 E-10|3,92 E-08|g/s/m|
|SRC_23|Tramo P3|Camino|2,08 E-07|7,12 E-07|3,51 E-06|9,01 E-07|1,54 E-07|1,88 E-09|4,34 E-07|g/s/m|

www.dfmconsultores.cl

155

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|ID|Descripción|Tipo de fuente|Tasas de emisión|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Descripción**|**Tipo de fuente**|**MP2.5**|**MP10**|**MPS**|**NO**|**NO2 **|**SO2 **|**CO**|**Unidad**|
|SRC_24|Tramo P4|Camino|2,07 E-07|7,08 E-07|3,49 E-06|8,96 E-07|1,53 E-07|1,87 E-09|4,32 E-07|g/s/m|
|SRC_25|Tramo P5|Camino|1,80 E-07|6,06 E-07|2,97 E-06|8,02 E-07|1,37 E-07|1,71 E-09|3,93 E-07|g/s/m|
|SRC_26|Tramo P6|Camino|1,56 E-07|5,34 E-07|2,63 E-06|6,60 E-07|1,13 E-07|1,40 E-09|3,21 E-07|g/s/m|
|SRC_27|Tramo P7|Camino|1,81 E-07|6,20 E-07|3,06 E-06|7,62 E-07|1,30 E-07|1,62 E-09|3,69 E-07|g/s/m|
|SRC_28|Tramo P8|Camino|3,68 E-09|9,56 E-09|4,22 E-08|1,40 E-08|2,38 E-09|5,55 E-11|1,09 E-08|g/s/m|
|SRC_29|Tramo P9|Camino|4,78 E-08|1,74 E-07|8,77 E-07|1,76 E-07|3,00 E-08|3,34 E-10|7,71 E-08|g/s/m|
|SRC_30|Tramo P10|Camino|1,05 E-07|3,59 E-07|1,77 E-06|3,88 E-07|6,61 E-08|9,18 E-10|2,01 E-07|g/s/m|
|SRC_31|Tramo P11|Camino|4,69 E-08|1,60 E-07|7,90 E-07|2,18 E-07|3,71 E-08|4,33 E-10|1,02 E-07|g/s/m|
|SRC_32|Carola Norte|Área|1,31 E-07|3,12 E-07|5,50 E-07|9,76 E-07|1,66 E-07|4,33 E-09|5,44 E-06|g/s/m2|
|SRC_33|Carola Central|Área|8,22 E-06|1,44 E-05|5,93 E-05|6,10 E-06|1,04 E-06|2,66 E-08|1,03 E-05|g/s/m2|
|SRC_34|Planta Cerrillos|Área|7,36 E-07|2,78 E-06|1,04 E-05|3,77 E-07|6,42 E-08|4,19 E-09|1,06 E-06|g/s/m2|
|SRC_35|Tramo 1A|Camino|8,51 E-08|2,81 E-07|1,37 E-06|1,75 E-07|2,99 E-08|6,96 E-10|1,37 E-07|g/s/m|
|SRC_36|Tramo 1B|Camino|8,51 E-08|2,81 E-07|1,37 E-06|1,75 E-07|2,99 E-08|6,96 E-10|1,37 E-07|g/s/m|
|SRC_37|Tramo 2|Camino|3,25 E-06|3,23 E-05|9,34 E-05|2,01 E-07|3,43 E-08|7,32 E-10|1,46 E-07|g/s/m|
|SRC_38|Tramo 3|Camino|3,24 E-06|3,22 E-05|9,32 E-05|2,01 E-07|3,42 E-08|7,30 E-10|1,46 E-07|g/s/m|
|SRC_39|Tramo 4|Camino|2,85 E-06|2,83 E-05|8,19 E-05|1,70 E-07|2,90 E-08|6,75 E-10|1,33 E-07|g/s/m|
|SRC_40|Tramo 5|Camino|4,29 E-07|1,57 E-06|7,90 E-06|1,40 E-06|2,39 E-07|2,80 E-09|6,37 E-07|g/s/m|
|SRC_41|Tramo 6|Camino|9,27 E-06|3,51 E-05|1,78 E-04|2,91 E-05|4,96 E-06|5,04 E-08|1,19 E-05|g/s/m|
|SRC_42|Tramo 7|Camino|5,24 E-08|1,43 E-07|6,49 E-07|2,02 E-07|3,44 E-08|7,36 E-10|1,47 E-07|g/s/m|
|SRC_43|Tramo 8|Camino|9,20 E-06|3,49 E-05|1,77 E-04|2,89 E-05|4,92 E-06|4,96 E-08|1,18 E-05|g/s/m|
|SRC_44|Tramo 9A|Camino|3,88 E-07|1,47 E-06|7,46 E-06|1,23 E-06|2,10 E-07|2,12 E-09|5,03 E-07|g/s/m|
|SRC_45|Tramo 9b|Camino|3,88 E-07|1,47 E-06|7,46 E-06|1,23 E-06|2,10 E-07|2,12 E-09|5,03 E-07|g/s/m|
|SRC_46|Tramo 10|Camino|3,93 E-07|1,49 E-06|7,57 E-06|1,25 E-06|2,13 E-07|2,15 E-09|5,10 E-07|g/s/m|
|SRC_47|Tramo 11|Camino|9,19 E-06|3,48 E-05|1,77 E-04|2,88 E-05|4,91 E-06|4,95 E-08|1,18 E-05|g/s/m|

www.dfmconsultores.cl

156

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|ID|Descripción|Tipo de fuente|Tasas de emisión|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Descripción**|**Tipo de fuente**|**MP2.5**|**MP10**|**MPS**|**NO**|**NO2 **|**SO2 **|**CO**|**Unidad**|
|SRC_48|Tramo 12|Camino|9,20 E-06|3,49 E-05|1,77 E-04|2,89 E-05|4,92 E-06|4,95 E-08|1,18 E-05|g/s/m|
|SRC_49|Tramo 13|Camino|3,83 E-07|1,45 E-06|7,38 E-06|1,22 E-06|2,08 E-07|2,09 E-09|4,97 E-07|g/s/m|
|SRC_50|Tramo 14|Camino|8,84 E-06|3,35 E-05|1,71 E-04|2,77 E-05|4,72 E-06|4,76 E-08|1,13 E-05|g/s/m|
|SRC_51|Tramo 15|Camino|5,20 E-08|1,42 E-07|6,44 E-07|2,01 E-07|3,42 E-08|7,30 E-10|1,46 E-07|g/s/m|
|SRC_52|Tramo 16|Camino|3,24 E-06|3,22 E-05|9,32 E-05|2,01 E-07|3,42 E-08|7,30 E-10|1,46 E-07|g/s/m|
|SRC_53|Tramo 17|Camino|3,89 E-07|1,47 E-06|7,50 E-06|1,24 E-06|2,11 E-07|2,13 E-09|5,06 E-07|g/s/m|

Fuente: Elaboración propia.

**Tabla 7-2. Características de Fuentes Emisoras y Tasas de Emisión. Escenario Sinérgico Fase de Operación Proyectado.**

|ID|Descripción|Tipo de fuente|Tasas de emisión|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Descripción**|**Tipo de fuente**|**MP2.5**|**MP10**|**MPS**|**NO**|**NO2 **|**SO2 **|**CO**|**Unidad**|
|SRC_1|Tramo C1|Camino|1,88 E-07|6,11 E-07|2,96 E-06|1,23 E-06|2,10 E-07|2,29 E-09|5,46 E-07|g/s/m|
|SRC_2|Tramo C2|Camino|9,22 E-07|3,60 E-06|1,84 E-05|1,79 E-06|3,05 E-07|3,20 E-09|7,60 E-07|g/s/m|
|SRC_3|Tramo C3|Camino|7,56 E-07|2,99 E-06|1,54 E-05|1,27 E-06|2,17 E-07|2,19 E-09|5,22 E-07|g/s/m|
|SRC_4|Tramo C4|Camino|6,01 E-08|1,94 E-07|9,40 E-07|3,13 E-07|5,34 E-08|6,53 E-10|1,53 E-07|g/s/m|
|SRC_5|Tramo C5|Camino|1,42 E-06|5,68 E-06|2,93 E-05|1,67 E-06|2,85 E-07|2,93 E-09|7,02 E-07|g/s/m|
|SRC_6|Tramo C6|Camino|2,32 E-06|9,45 E-06|4,91 E-05|1,13 E-06|1,92 E-07|1,94 E-09|4,64 E-07|g/s/m|
|SRC_7|Tramo C7|Camino|8,90 E-07|3,59 E-06|1,86 E-05|7,90 E-07|1,35 E-07|1,36 E-09|3,24 E-07|g/s/m|
|SRC_8|Tramo C9|Camino|7,50 E-07|3,01 E-06|1,56 E-05|8,15 E-07|1,39 E-07|1,40 E-09|3,35 E-07|g/s/m|
|SRC_9|Tramo C10|Camino|5,89 E-07|2,34 E-06|1,21 E-05|8,80 E-07|1,50 E-07|1,51 E-09|3,61 E-07|g/s/m|
|SRC_10|Tramo C11|Camino|3,30 E-08|1,27 E-07|6,49 E-07|8,42 E-08|1,44 E-08|1,44 E-10|3,42 E-08|g/s/m|
|SRC_11|Tramo C12|Camino|4,05 E-07|1,54 E-06|7,81 E-06|1,10 E-06|1,87 E-07|2,01 E-09|4,77 E-07|g/s/m|
|SRC_12|Tramo N1|Camino|2,35 E-07|2,16 E-06|8,71 E-06|4,62 E-07|7,87 E-08|8,79 E-10|2,13 E-07|g/s/m|
|SRC_13|Tramo N2|Camino|2,14 E-07|1,96 E-06|7,92 E-06|4,20 E-07|7,15 E-08|7,99 E-10|1,94 E-07|g/s/m|

www.dfmconsultores.cl

157

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|ID|Descripción|Tipo de fuente|Tasas de emisión|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Descripción**|**Tipo de fuente**|**MP2.5**|**MP10**|**MPS**|**NO**|**NO2 **|**SO2 **|**CO**|**Unidad**|
|SRC_14|Tramo N3|Camino|1,02 E-07|9,02 E-07|3,63 E-06|2,94 E-07|5,01 E-08|5,36 E-10|1,34 E-07|g/s/m|
|SRC_15|Tramo N4|Camino|4,34 E-07|4,18 E-06|1,69 E-05|5,08 E-07|8,66 E-08|8,74 E-10|2,09 E-07|g/s/m|
|SRC_16|Tramo N5|Camino|3,83 E-07|3,69 E-06|1,50 E-05|4,47 E-07|7,62 E-08|7,69 E-10|1,84 E-07|g/s/m|
|SRC_17|Tramo S1|Camino|9,89 E-07|9,75 E-06|2,82 E-05|2,12 E-07|3,61 E-08|5,78 E-10|1,22 E-07|g/s/m|
|SRC_18|Tramo S2|Camino|1,05 E-06|1,03 E-05|2,99 E-05|2,25 E-07|3,83 E-08|6,13 E-10|1,30 E-07|g/s/m|
|SRC_19|Tramo S3|Camino|2,82 E-06|2,80 E-05|8,09 E-05|7,61 E-07|1,30 E-07|1,31 E-09|3,12 E-07|g/s/m|
|SRC_20|Tramo S4|Camino|7,68 E-06|7,62 E-05|2,20 E-04|1,55 E-06|2,64 E-07|3,08 E-09|7,04 E-07|g/s/m|
|SRC_21|Tramo P1|Camino|2,48 E-08|9,32 E-08|4,73 E-07|8,55 E-08|1,46 E-08|1,47 E-10|3,51 E-08|g/s/m|
|SRC_22|Tramo P2|Camino|2,77 E-08|1,04 E-07|5,28 E-07|9,55 E-08|1,63 E-08|1,64 E-10|3,92 E-08|g/s/m|
|SRC_23|Tramo P3|Camino|2,08 E-07|7,12 E-07|3,51 E-06|9,01 E-07|1,54 E-07|1,88 E-09|4,34 E-07|g/s/m|
|SRC_24|Tramo P4|Camino|2,07 E-07|7,08 E-07|3,49 E-06|8,96 E-07|1,53 E-07|1,87 E-09|4,32 E-07|g/s/m|
|SRC_25|Tramo P5|Camino|1,80 E-07|6,06 E-07|2,97 E-06|8,02 E-07|1,37 E-07|1,71 E-09|3,93 E-07|g/s/m|
|SRC_26|Tramo P6|Camino|1,08 E-07|3,34 E-07|1,59 E-06|6,60 E-07|1,13 E-07|1,40 E-09|3,21 E-07|g/s/m|
|SRC_27|Tramo P7|Camino|1,25 E-07|3,88 E-07|1,85 E-06|7,62 E-07|1,30 E-07|1,62 E-09|3,69 E-07|g/s/m|
|SRC_28|Tramo P8|Camino|3,68 E-09|9,56 E-09|4,22 E-08|1,40 E-08|2,38 E-09|5,55 E-11|1,09 E-08|g/s/m|
|SRC_29|Tramo P9|Camino|3,70 E-08|1,29 E-07|6,43 E-07|1,76 E-07|3,00 E-08|3,34 E-10|7,71 E-08|g/s/m|
|SRC_30|Tramo P10|Camino|7,28 E-08|2,25 E-07|1,07 E-06|3,88 E-07|6,61 E-08|9,18 E-10|2,01 E-07|g/s/m|
|SRC_31|Tramo P11|Camino|4,69 E-08|1,60 E-07|7,90 E-07|2,18 E-07|3,71 E-08|4,33 E-10|1,02 E-07|g/s/m|
|SRC_32|Carola Norte|Área|1,44 E-07|3,43 E-07|6,04 E-07|1,07 E-06|1,83 E-07|4,76 E-09|1,52 E-06|g/s/m2|
|SRC_33|Carola Central|Área|9,04 E-06|1,58 E-05|6,53 E-05|6,71 E-06|1,14 E-06|2,93 E-08|9,78 E-06|g/s/m2|
|SRC_34|Planta Cerrillos|Área|8,10 E-07|3,06 E-06|1,15 E-05|4,15 E-07|7,07 E-08|4,61 E-09|1,16 E-06|g/s/m2|
|SRC_35|Tramo 1A|Camino|9,37 E-08|3,09 E-07|1,50 E-06|1,93 E-07|3,28 E-08|7,65 E-10|1,51 E-07|g/s/m|
|SRC_36|Tramo 1B|Camino|9,37 E-08|3,09 E-07|1,50 E-06|1,93 E-07|3,28 E-08|7,65 E-10|1,51 E-07|g/s/m|
|SRC_37|Tramo 2|Camino|1,21 E-06|1,19 E-05|3,43 E-05|2,21 E-07|3,77 E-08|8,05 E-10|1,61 E-07|g/s/m|

www.dfmconsultores.cl

158

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|ID|Descripción|Tipo de fuente|Tasas de emisión|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**ID**|**Descripción**|**Tipo de fuente**|**MP2.5**|**MP10**|**MPS**|**NO**|**NO2 **|**SO2 **|**CO**|**Unidad**|
|SRC_38|Tramo 3|Camino|1,21 E-06|1,18 E-05|3,42 E-05|2,21 E-07|3,76 E-08|8,04 E-10|1,61 E-07|g/s/m|
|SRC_39|Tramo 4|Camino|1,06 E-06|1,04 E-05|3,00 E-05|1,87 E-07|3,19 E-08|7,43 E-10|1,46 E-07|g/s/m|
|SRC_40|Tramo 5|Camino|3,12 E-07|1,06 E-06|5,24 E-06|1,54 E-06|2,63 E-07|3,08 E-09|7,01 E-07|g/s/m|
|SRC_41|Tramo 6|Camino|6,57 E-06|2,36 E-05|1,18 E-04|3,20 E-05|5,46 E-06|5,54 E-08|1,31 E-05|g/s/m|
|SRC_42|Tramo 7|Camino|4,49 E-08|1,05 E-07|4,39 E-07|2,22 E-07|3,79 E-08|8,09 E-10|1,62 E-07|g/s/m|
|SRC_43|Tramo 8|Camino|7,70 E-06|2,84 E-05|1,43 E-04|3,18 E-05|5,41 E-06|5,45 E-08|1,30 E-05|g/s/m|
|SRC_44|Tramo 9A|Camino|2,75 E-07|9,88 E-07|4,95 E-06|1,36 E-06|2,31 E-07|2,33 E-09|5,54 E-07|g/s/m|
|SRC_45|Tramo 9b|Camino|2,75 E-07|9,88 E-07|4,95 E-06|1,36 E-06|2,31 E-07|2,33 E-09|5,54 E-07|g/s/m|
|SRC_46|Tramo 10|Camino|4,32 E-07|1,64 E-06|8,33 E-06|1,38 E-06|2,34 E-07|2,36 E-09|5,61 E-07|g/s/m|
|SRC_47|Tramo 11|Camino|6,51 E-06|2,34 E-05|1,17 E-04|3,17 E-05|5,41 E-06|5,45 E-08|1,29 E-05|g/s/m|
|SRC_48|Tramo 12|Camino|1,41 E-06|2,35 E-06|7,59 E-06|3,17 E-05|5,41 E-06|5,45 E-08|1,29 E-05|g/s/m|
|SRC_49|Tramo 13|Camino|4,21 E-07|1,59 E-06|8,11 E-06|1,34 E-06|2,28 E-07|2,30 E-09|5,47 E-07|g/s/m|
|SRC_50|Tramo 14|Camino|6,26 E-06|2,25 E-05|1,13 E-04|3,05 E-05|5,20 E-06|5,23 E-08|1,24 E-05|g/s/m|
|SRC_51|Tramo 15|Camino|5,72 E-08|1,57 E-07|7,09 E-07|2,21 E-07|3,76 E-08|8,03 E-10|1,61 E-07|g/s/m|
|SRC_52|Tramo 16|Camino|1,21 E-06|1,18 E-05|3,42 E-05|2,21 E-07|3,76 E-08|8,03 E-10|1,61 E-07|g/s/m|
|SRC_53|Tramo 17|Camino|4,28 E-07|1,62 E-06|8,25 E-06|1,36 E-06|2,32 E-07|2,34 E-09|5,56 E-07|g/s/m|

Fuente: Elaboración propia.

www.dfmconsultores.cl

159

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

#### 7.2 Receptores de Interés Escenario Sinérgico

Para la evaluación del aporte de las emisiones atmosféricas de los proyectos “Optimización

Operacional Mina Carola” y “Optimización Operacional Planta Cerrillos”, se ha definido una

grilla de receptores con resolución de 37.000 x 43.000 m con espaciado cada 1.000 m,

abarcando gran parte del dominio de modelación y procurando contender las fuentes

emisoras asociadas a ambos proyectos en estudio.

A modo complementario, se han considerado 35 receptores discretos, los cuales

representan puntos de interés tales como: medio humano y estaciones de monitoreo. La

ubicación de tales puntos se muestra de manera detallada en la Tabla 7-3.

**Tabla 7-3. Receptores de Interés. Escenario Sinérgico Fase de Operación.**

|ID|Receptor|Coordenadas [Datum WGS84]|Col4|Elevación<br>[m.s.n.m.]|
|---|---|---|---|---|
|**ID**|**Receptor**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|R_1|Estación Luis Uribe|374.942|6.961.596|514,30|
|R_2|Estación Tierra Amarilla|374.904|6.960.235|521,39|
|R_3|Estación Ojanco|374.772|6.958.885|513,93|
|R_4|Estación Kozan|375.076|6.956.263|568,74|
|R_5|133 casa (Carola Norte)|375.842|6.961.206|561,91|
|R_6|Iglesia Tierra Amarilla|375.270|6.961.216|518,20|
|R_7|El Minero|375.114|6.958.078|540,49|
|R_8|Testigoteca|375.054|6.957.920|541,09|
|R_9|Estadio|375.353|6.956.715|573,60|
|R_10|Agrouva I|375.347|6.956.543|567,13|
|R_11|Agrouva II|375.370|6.956.345|551,88|
|R_12|Receptor ruido (viviendas 1 piso, material mixto)|375.021|6.958.033|539,80|
|R_13|Receptor ruido (viviendas 1 piso, material ligero)|375.005|6.957.965|540,10|
|R_14|Receptor ruido (viviendas 1 piso, material ligero)|374.966|6.957.769|542,55|
|R_15|Receptor ruido (Oficinas, galpones y container, material<br>mixto)|375.215|6.957.683|554,95|
|R_16|Receptor ruido (Vivienda 2 pisos, material ligero)|375.126|6.957.573|558,76|
|R_17|Receptor ruido (Viviendas 1 y 2 pisos, material ligero)|375.093|6.957.335|555,04|
|R_18|Receptor ruido (Viviendas 1 y 2 pisos, material mixto)|375.248|6.957.084|566,44|
|R_19|Receptor ruido (Viviendas 1 y 2 pisos, material ligero)|375.278|6.956.755|573,88|
|R_20|Receptor ruido (Viviendas 1 piso, material ligero)|375.476|6.956.834|575,09|
|R_21|Receptor ruido (Vivienda 1 piso, material ligero)|375.633|6.956.813|584,48|

www.dfmconsultores.cl

160

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|ID|Receptor|Coordenadas [Datum WGS84]|Col4|Elevación<br>[m.s.n.m.]|
|---|---|---|---|---|
|**ID**|**Receptor**|**Este (m)**|**Norte (m)**|**Norte (m)**|
|R_22|Receptor ruido (Viviendas 1 y 2 pisos, material ligero)|375.105|6.956.579|575,38|
|R_23|Receptor ruido (Oficinas Empresa Agrícola Uvas del Norte,<br>ubicada frente a Planta Cerrillos- COEMIN)|377.121|6.949.607|642,08|
|R_24|Receptor ruido (Km 21 Carretera C-35. Entrada Fundo<br>Alianza Agricultura)|376.866|6.948.610|631,11|
|R_25|Receptor ruido (Km 21 Carretera C-35. Frente a casa-<br>almacén)|376.669|6.946.880|627,97|
|R_26|Receptor ruido (Punto ubicado a 5 k. Planta Cerrillos, por<br>carretera C-35, localidad de Nantoco)|374.539|6.953.171|552,36|
|R_27|Estación COEMIN|377.146|6.949.777|640,22|
|R_28|Estación Nantoco|374.903|6.952.384|575,29|
|R_29|Estación C6|375.453|6.950.426|599,45|
|R_30|Estación C5|375.723|6.949.811|616,72|
|R_31|Estación C8|375.345|6 950 895|595,90|
|R_32|Estación C2|377.121|6.946.865|644,54|
|R_33|Estación C1|377.154|6.947.080|643,66|
|R_34|Estación C3|376.995|6.946.944|633,39|
|R_35|Estación C7|375.348|6.950.777|603,95|

Fuente: Elaboración propia.

A continuación, en la Figura 7-2 se presenta la grilla de receptores utilizada, mientras que

en la Figura 7-3 se muestran los receptores de interés considerados en la modelación de

dispersión de contaminantes.

www.dfmconsultores.cl

161

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-2. Ubicación Grilla de Receptores. Escenario Sinérgico Fase de Operación.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

162

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-3. Ubicación de Receptores de Interés. Escenario Sinérgico Fase de Operación.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

163

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

#### 7.3 Resultados Modelación Escenario Sinérgico Fase de Operación Base

A continuación, en los siguientes apartados se presentan los resultados de la modelación

de dispersión de contaminantes realizada para el escenario sinérgico base correspondiente

a la fase de operación actual de los proyectos “Optimización Operacional Planta Cerrillos” y

“Optimización Operacional Mina Carola”, considerando un tiempo de desarrollo de 12

meses.

Para ello, se muestran las concentraciones actuales aportadas sobre los receptores de

interés mencionados con anterioridad a causa de la ejecución simultánea de ambos

proyectos indicados, realizando un análisis normativo de cada uno de los estadígrafos

indicados por las normativas y valores de referencia señalados en la sección 5.7.

A modo complementario, se presentan las curvas de isoconcentración e isodepositación,

según corresponde, conforme a las concentraciones y depositaciones obtenidas y

percibidas en el dominio de modelación.

www.dfmconsultores.cl

164

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

7.3.1 Material Particulado Respirable Fino (MP2.5)

En la Tabla 7-4 se presentan los aportes sinérgicos generados durante la fase de operación

actual de los proyectos “Optimización Operacional Planta Cerrillos” y “Optimización

Operacional Mina Carola” sobre los receptores de interés, específicamente sobre

receptores de medio humano y estaciones de monitoreo, conforme con la norma primaria

para material particulado respirable fino (MP2.5).

**Tabla 7-4. Resultados del modelo de dispersión para MP2.5 [μg/m** **[3]** **]. Escenario Sinérgico Fase de**

**Operación Base.**

|Receptor|Descripción|Material Particulado Respirable Fino (MP2.5)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3] **|**Concentración [μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|0,950|0,462|50|20|1,9%|2,3%|
|R_2|Estación Tierra Amarilla|1,513|0,775|0,775|0,775|3,0%|3,9%|
|R_3|Estación Ojanco|1,430|0,646|0,646|0,646|2,9%|3,2%|
|R_4|Estación Kozan|3,778|1,430|1,430|1,430|7,6%|7,2%|
|R_5|133 casa (Carola Norte)|0,759|0,350|0,350|0,350|1,5%|1,7%|
|R_6|Iglesia Tierra Amarilla|1,157|0,590|0,590|0,590|2,3%|2,9%|
|R_7|El Minero|4,472|1,719|1,719|1,719|8,9%|8,6%|
|R_8|Testigoteca|2,742|1,040|1,040|1,040|5,5%|5,2%|
|R_9|Estadio|8,552|2,554|2,554|2,554|17,1%|12,8%|
|R_10|Agrouva I|5,284|1,823|1,823|1,823|10,6%|9,1%|
|R_11|Agrouva II|1,961|1,021|1,021|1,021|3,9%|5,1%|
|R_12|Receptor ruido|3,695|1,754|1,754|1,754|7,4%|8,8%|
|R_13|Receptor ruido|2,712|1,097|1,097|1,097|5,4%|5,5%|
|R_14|Receptor ruido|2,342|1,117|1,117|1,117|4,7%|5,6%|
|R_15|Receptor ruido|5,235|1,823|1,823|1,823|10,5%|9,1%|
|R_16|Receptor ruido|6,304|2,088|2,088|2,088|12,6%|10,4%|
|R_17|Receptor ruido|4,229|1,619|1,619|1,619|8,5%|8,1%|
|R_18|Receptor ruido|20,338|4,302|4,302|4,302|40,7%|21,5%|
|R_19|Receptor ruido|10,464|2,872|2,872|2,872|20,9%|14,4%|
|R_20|Receptor ruido|10,721|3,153|3,153|3,153|21,4%|15,8%|
|R_21|Receptor ruido|8,916|2,832|2,832|2,832|17,8%|14,2%|
|R_22|Receptor ruido|8,589|2,751|2,751|2,751|17,2%|13,8%|
|R_23|Receptor ruido|15,538|7,321|7,321|7,321|31,1%|36,6%|
|R_24|Receptor ruido|2,455|0,703|0,703|0,703|4,9%|3,5%|
|R_25|Receptor ruido|0,270|0,103|0,103|0,103|0,5%|0,5%|
|R_26|Receptor ruido|1,982|1,066|1,066|1,066|4,0%|5,3%|

www.dfmconsultores.cl

165

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Material Particulado Respirable Fino (MP2.5)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3] **|**Concentración [μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_27|Estación COEMIN|11,610|5,123|||23,2%|25,6%|
|R_28|Estación Nantoco|2,245|0,978|0,978|0,978|4,5%|4,9%|
|R_29|Estación C6|1,287|0,705|0,705|0,705|2,6%|3,5%|
|R_30|Estación C5|1,096|0,526|0,526|0,526|2,2%|2,6%|
|R_31|Estación C8|2,526|1,264|1,264|1,264|5,1%|6,3%|
|R_32|Estación C2|0,334|0,125|0,125|0,125|0,7%|0,6%|
|R_33|Estación C1|0,368|0,140|0,140|0,140|0,7%|0,7%|
|R_34|Estación C3|0,335|0,124|0,124|0,124|0,7%|0,6%|
|R_35|Estación C7|2,608|1,356|1,356|1,356|5,2%|6,8%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes sinérgicos actuales de los proyectos

sobre los receptores de interés alcanzan un máximo de 40,7% y 31,1% de la norma de este

contaminante en periodo diario, específicamente sobre los receptores denominados

“R_18” y “R_23”, correspondientes a viviendas de material de construcción mixto y a las

oficinas de la empresa agrícola Uvas del Norte según orden de mención. Por su parte, en

cuanto a los aportes sinérgicos actuales de MP2.5 estimados para periodo anual, estos

representan hasta un 36,6% y 25,6% de la normativa respectiva, particularmente en los

receptores “R_23” y “R_27”, este último correspondiente a la estación de monitoreo

COEMIN.

A continuación, en las siguientes figuras se presentan las curvas de isoconcentración de

material particulado respirable fino (MP2.5) para periodo de 24 horas y periodo anual.

www.dfmconsultores.cl

166

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-4. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP2.5 [μg/m** **[3]** **]. Escenario**

**Sinérgico Fase de Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

167

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-5. Curvas de isoconcentración para periodo anual. MP2.5 [μg/m** **[3]** **]. Escenario Sinérgico Fase de**

**Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

168

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

7.3.2 Material Particulado Respirable (MP10)

En la Tabla 7-5 se presentan los aportes sinérgicos generados durante la fase de operación

actual de los proyectos “Optimización Operacional Planta Cerrillos” y “Optimización

Operacional Mina Carola” sobre los receptores de interés, específicamente sobre

receptores de medio humano y estaciones de monitoreo, conforme con la norma primaria

para material particulado respirable (MP10).

**Tabla 7-5. Resultados del modelo de dispersión para MP10 [μg/m** **[3]** **N]. Escenario Sinérgico Fase de**

**Operación Base.**

|Receptor|Descripción|Material Particulado Respirable (MP10)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|2,123|1,051|130|50|1,6%|2,1%|
|R_2|Estación Tierra Amarilla|3,307|1,689|1,689|1,689|2,5%|3,4%|
|R_3|Estación Ojanco|3,179|1,634|1,634|1,634|2,4%|3,3%|
|R_4|Estación Kozan|11,366|4,355|4,355|4,355|8,7%|8,7%|
|R_5|133 casa (Carola Norte)|2,021|1,106|1,106|1,106|1,6%|2,2%|
|R_6|Iglesia Tierra Amarilla|2,559|1,322|1,322|1,322|2,0%|2,6%|
|R_7|El Minero|10,230|4,393|4,393|4,393|7,9%|8,8%|
|R_8|Testigoteca|6,753|2,813|2,813|2,813|5,2%|5,6%|
|R_9|Estadio|19,227|7,238|7,238|7,238|14,8%|14,5%|
|R_10|Agrouva I|12,081|5,134|5,134|5,134|9,3%|10,3%|
|R_11|Agrouva II|4,320|2,594|2,594|2,594|3,3%|5,2%|
|R_12|Receptor ruido|10,596|5,496|5,496|5,496|8,2%|11,0%|
|R_13|Receptor ruido|6,898|3,157|3,157|3,157|5,3%|6,3%|
|R_14|Receptor ruido|5,989|3,384|3,384|3,384|4,6%|6,8%|
|R_15|Receptor ruido|10,524|4,080|4,080|4,080|8,1%|8,2%|
|R_16|Receptor ruido|12,508|4,614|4,614|4,614|9,6%|9,2%|
|R_17|Receptor ruido|10,447|4,331|4,331|4,331|8,0%|8,7%|
|R_18|Receptor ruido|35,795|8,743|8,743|8,743|27,5%|17,5%|
|R_19|Receptor ruido|23,265|9,016|9,016|9,016|17,9%|18,0%|
|R_20|Receptor ruido|20,820|7,424|7,424|7,424|16,0%|14,8%|
|R_21|Receptor ruido|18,367|7,300|7,300|7,300|14,1%|14,6%|
|R_22|Receptor ruido|21,231|8,726|8,726|8,726|16,3%|17,5%|
|R_23|Receptor ruido|62,560|28,861|28,861|28,861|48,1%|57,7%|
|R_24|Receptor ruido|9,554|2,647|2,647|2,647|7,3%|5,3%|
|R_25|Receptor ruido|0,918|0,328|0,328|0,328|0,7%|0,7%|
|R_26|Receptor ruido|7,205|3,797|3,797|3,797|5,5%|7,6%|

www.dfmconsultores.cl

169

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Material Particulado Respirable (MP10)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_27|Estación COEMIN|45,440|19,908|||35,0%|39,8%|
|R_28|Estación Nantoco|8,369|3,502|3,502|3,502|6,4%|7,0%|
|R_29|Estación C6|4,654|2,550|2,550|2,550|3,6%|5,1%|
|R_30|Estación C5|4,119|1,911|1,911|1,911|3,2%|3,8%|
|R_31|Estación C8|9,448|4,636|4,636|4,636|7,3%|9,3%|
|R_32|Estación C2|1,152|0,413|0,413|0,413|0,9%|0,8%|
|R_33|Estación C1|1,283|0,469|0,469|0,469|1,0%|0,9%|
|R_34|Estación C3|1,126|0,408|0,408|0,408|0,9%|0,8%|
|R_35|Estación C7|9,780|4,990|4,990|4,990|7,5%|10,0%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes sinérgicos actuales de los proyectos

sobre los receptores de interés alcanzan un máximo de 48,1% y 35,0% de la norma de este

contaminante en periodo diario, particularmente sobre los receptores denominados

“R_23” y “R_27”, los que corresponden a las oficinas de la empresa agrícola Uvas del Norte

y a la estación de monitoreo COEMIN según orden de mención. Por su parte, en cuanto a

los aportes sinérgicos actuales de MP10 estimados para periodo anual, estos representan

hasta un 57,7% y 39,8% de la normativa respectiva, específicamente en los receptores

indicados con anterioridad.

A continuación, en las siguientes figuras se presentan las curvas de isoconcentración de

material particulado respirable (MP10) para periodo de 24 horas y periodo anual.

www.dfmconsultores.cl

170

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-6. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP10 [μg/m** **[3]** **N]. Escenario**

**Sinérgico Fase de Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

171

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-7. Curvas de isoconcentración para periodo anual. MP10 [μg/m** **[3]** **N]. Escenario Sinérgico Fase de**

**Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

172

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

7.3.3 Material Particulado Sedimentable (MPS)

En la Tabla 7-6 se presentan los aportes sinérgicos generados durante la fase de operación

actual de los proyectos “Optimización Operacional Planta Cerrillos” y “Optimización

Operacional Mina Carola” sobre los receptores de interés, específicamente sobre

receptores de medio humano y estaciones de monitoreo, conforme con las normas de

referencia internacionales de material particulado sedimentable (MPS).

**Tabla 7-6. Resultados del modelo de dispersión para MPS [mg/m** **[2∙]** **día]. Escenario Sinérgico Fase de**

**Operación Base.**

|Receptor|Descripción|Material Particulado Sedimentable (MPS)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**Media**<br>**Anual**|**Máxima**<br>**Media**<br>**Mensual**|**Conf. Suiza**|**República**<br>**Argentina**|**Conf. Suiza**|**República**<br>**Argentina**|
|R_1|Estación Luis Uribe|1,477|2,448|200|333|0,7%|0,7%|
|R_2|Estación Tierra Amarilla|2,338|3,908|3,908|3,908|1,2%|1,2%|
|R_3|Estación Ojanco|1,900|2,852|2,852|2,852|0,9%|0,9%|
|R_4|Estación Kozan|17,819|22,066|22,066|22,066|8,9%|6,6%|
|R_5|133 casa (Carola Norte)|2,868|3,391|3,391|3,391|1,4%|1,0%|
|R_6|Iglesia Tierra Amarilla|1,860|3,169|3,169|3,169|0,9%|1,0%|
|R_7|El Minero|15,222|20,032|20,032|20,032|7,6%|6,0%|
|R_8|Testigoteca|9,453|11,185|11,185|11,185|4,7%|3,4%|
|R_9|Estadio|21,047|22,784|22,784|22,784|10,5%|6,8%|
|R_10|Agrouva I|14,874|16,094|16,094|16,094|7,4%|4,8%|
|R_11|Agrouva II|6,915|8,065|8,065|8,065|3,5%|2,4%|
|R_12|Receptor ruido|25,493|32,586|32,586|32,586|12,7%|9,8%|
|R_13|Receptor ruido|12,248|14,776|14,776|14,776|6,1%|4,4%|
|R_14|Receptor ruido|14,239|15,777|15,777|15,777|7,1%|4,7%|
|R_15|Receptor ruido|12,245|17,079|17,079|17,079|6,1%|5,1%|
|R_16|Receptor ruido|13,403|18,935|18,935|18,935|6,7%|5,7%|
|R_17|Receptor ruido|15,585|18,731|18,731|18,731|7,8%|5,6%|
|R_18|Receptor ruido|24,462|30,588|30,588|30,588|12,2%|9,2%|
|R_19|Receptor ruido|29,015|31,874|31,874|31,874|14,5%|9,6%|
|R_20|Receptor ruido|18,752|21,588|21,588|21,588|9,4%|6,5%|
|R_21|Receptor ruido|17,542|20,347|20,347|20,347|8,8%|6,1%|
|R_22|Receptor ruido|44,728|53,543|53,543|53,543|22,4%|16,1%|
|R_23|Receptor ruido|103,480|127,549|127,549|127,549|51,7%|38,3%|
|R_24|Receptor ruido|4,875|5,850|5,850|5,850|2,4%|1,8%|
|R_25|Receptor ruido|0,335|0,431|0,431|0,431|0,2%|0,1%|

www.dfmconsultores.cl

173

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Material Particulado Sedimentable (MPS)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**Media**<br>**Anual**|**Máxima**<br>**Media**<br>**Mensual**|**Conf. Suiza**|**República**<br>**Argentina**|**Conf. Suiza**|**República**<br>**Argentina**|
|R_26|Receptor ruido|16,206|20,818|||8,1%|6,3%|
|R_27|Estación COEMIN|63,856|78,286|78,286|78,286|31,9%|23,5%|
|R_28|Estación Nantoco|14,340|20,962|20,962|20,962|7,2%|6,3%|
|R_29|Estación C6|11,221|13,682|13,682|13,682|5,6%|4,1%|
|R_30|Estación C5|6,775|8,188|8,188|8,188|3,4%|2,5%|
|R_31|Estación C8|22,701|30,817|30,817|30,817|11,4%|9,3%|
|R_32|Estación C2|0,442|0,567|0,567|0,567|0,2%|0,2%|
|R_33|Estación C1|0,508|0,646|0,646|0,646|0,3%|0,2%|
|R_34|Estación C3|0,427|0,547|0,547|0,547|0,2%|0,2%|
|R_35|Estación C7|24,692|35,107|35,107|35,107|12,3%|10,5%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes sinérgicos actuales de los proyectos

sobre los receptores de interés alcanzan un máximo de 51,7% y 31,9% de la norma de

referencia para periodo anual de la Confederación Suiza, particularmente sobre los

receptores denominados “R_23” y “R_27”, los que corresponden a las oficinas de la

empresa agrícola Uvas del Norte y a la estación de monitoreo COEMIN según orden de

mención. Por su parte, en cuanto a los valores actuales de depositación sinérgica de MPS

mensuales estimados, estos representan hasta un 38,3% y 23,5% de la norma de referencia

para periodo mensual de la República de Argentina, específicamente en los receptores ya

mencionados.

A continuación, en las siguientes figuras se presentan las curvas de isodepositación de

material particulado sedimentable (MPS) para periodo mensual y anual.

www.dfmconsultores.cl

174

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-8. Curvas de isodepositación para periodo mensual. MPS [mg/m** **[2]** **∙día]. Escenario Sinérgico Fase**

**de Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

175

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-9. Curvas de isodepositación para periodo anual. MPS [mg/m** **[2]** **∙día]. Escenario Sinérgico Fase de**

**Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

176

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

7.3.4 Monóxido de Carbono (CO)

En la Tabla 7-7 se presentan los aportes sinérgicos generados durante la fase de operación

actual de los proyectos “Optimización Operacional Planta Cerrillos” y “Optimización

Operacional Mina Carola” sobre los receptores de interés, específicamente sobre

receptores de medio humano y estaciones de monitoreo, conforme con la norma primaria

para monóxido de carbono (CO).

**Tabla 7-7. Resultados del modelo de dispersión para CO [mg/m** **[3]** **N]. Escenario Sinérgico Fase de Operación**

**Base.**

|Receptor|Descripción|Monóxido de Carbono (CO)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[mg/m3N]**|**Concentración**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|
|R_1|Estación Luis Uribe|0,007|0,003|30|10|0,0%|0,0%|
|R_2|Estación Tierra Amarilla|0,011|0,004|0,004|0,004|0,0%|0,0%|
|R_3|Estación Ojanco|0,016|0,005|0,005|0,005|0,1%|0,0%|
|R_4|Estación Kozan|0,038|0,013|0,013|0,013|0,1%|0,1%|
|R_5|133 casa (Carola Norte)|0,006|0,002|0,002|0,002|0,0%|0,0%|
|R_6|Iglesia Tierra Amarilla|0,007|0,003|0,003|0,003|0,0%|0,0%|
|R_7|El Minero|0,079|0,014|0,014|0,014|0,3%|0,1%|
|R_8|Testigoteca|0,058|0,010|0,010|0,010|0,2%|0,1%|
|R_9|Estadio|0,154|0,029|0,029|0,029|0,5%|0,3%|
|R_10|Agrouva I|0,085|0,017|0,017|0,017|0,3%|0,2%|
|R_11|Agrouva II|0,021|0,005|0,005|0,005|0,1%|0,1%|
|R_12|Receptor ruido|0,062|0,012|0,012|0,012|0,2%|0,1%|
|R_13|Receptor ruido|0,054|0,010|0,010|0,010|0,2%|0,1%|
|R_14|Receptor ruido|0,035|0,007|0,007|0,007|0,1%|0,1%|
|R_15|Receptor ruido|0,091|0,017|0,017|0,017|0,3%|0,2%|
|R_16|Receptor ruido|0,106|0,020|0,020|0,020|0,4%|0,2%|
|R_17|Receptor ruido|0,071|0,014|0,014|0,014|0,2%|0,1%|
|R_18|Receptor ruido|0,326|0,067|0,067|0,067|1,1%|0,7%|
|R_19|Receptor ruido|0,166|0,032|0,032|0,032|0,6%|0,3%|
|R_20|Receptor ruido|0,214|0,036|0,036|0,036|0,7%|0,4%|
|R_21|Receptor ruido|0,177|0,032|0,032|0,032|0,6%|0,3%|
|R_22|Receptor ruido|0,101|0,028|0,028|0,028|0,3%|0,3%|
|R_23|Receptor ruido|0,141|0,047|0,047|0,047|0,5%|0,5%|
|R_24|Receptor ruido|0,035|0,008|0,008|0,008|0,1%|0,1%|
|R_25|Receptor ruido|0,002|0,001|0,001|0,001|0,0%|0,0%|
|R_26|Receptor ruido|0,011|0,005|0,005|0,005|0,0%|0,1%|

www.dfmconsultores.cl

177

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Monóxido de Carbono (CO)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[mg/m3N]**|**Concentración**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|
|R_27|Estación COEMIN|0,125|0,038|||0,4%|0,4%|
|R_28|Estación Nantoco|0,017|0,007|0,007|0,007|0,1%|0,1%|
|R_29|Estación C6|0,013|0,004|0,004|0,004|0,0%|0,0%|
|R_30|Estación C5|0,014|0,003|0,003|0,003|0,0%|0,0%|
|R_31|Estación C8|0,022|0,007|0,007|0,007|0,1%|0,1%|
|R_32|Estación C2|0,002|0,001|0,001|0,001|0,0%|0,0%|
|R_33|Estación C1|0,002|0,001|0,001|0,001|0,0%|0,0%|
|R_34|Estación C3|0,002|0,001|0,001|0,001|0,0%|0,0%|
|R_35|Estación C7|0,025|0,009|0,009|0,009|0,1%|0,1%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes sinérgicos actuales de los proyectos

sobre los receptores de interés alcanzan un máximo de 1,1% y 0,7% de este contaminante

en periodo horario, específicamente sobre los receptores denominados “R_18” y “R_20”,

los que corresponden a viviendas construidas con material mixto y material ligero

respectivamente. Mientras que, en cuanto a las concentraciones sinérgicas actuales

estimadas para periodo de 8 horas, éstas no superan el 0,7% de la norma respectiva,

particularmente en el receptor “R_18”. En consecuencia, es posible establecer que la

contribución sinérgica actual de los proyectos sobre los receptores de interés, en cuanto a

emisiones de CO, es bastante mínima.

En consecuencia, considerando que los aportes de concentración de CO percibidos en los

receptores son menores a 1,5 mg/m [3] N en periodo horario y 0,4889 mg/m [3] N en periodo de

ocho horas, valores correspondientes a los límites de los Niveles de Impacto Significativo

para este contaminante según lo indicado en el documento “Evaluación Significancia del

Impacto de las Emisiones de un Proyecto o Actividad en Zonas Saturadas en el Marco del

SEIA” (DICTUC, 2022), en esta oportunidad no se presentan curvas de isoconcentración de

monóxido de carbono asociadas al efecto sinérgico de la fase de operación actual de los

proyectos señalados.

www.dfmconsultores.cl

178

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

7.3.5 Dióxido de Nitrógeno (NO 2 )

En la Tabla 7-8 se presentan los aportes sinérgicos generados durante la fase de operación

actual de los proyectos “Optimización Operacional Planta Cerrillos” y “Optimización

Operacional Mina Carola” sobre los receptores de interés, específicamente sobre

receptores de medio humano y estaciones de monitoreo, conforme con la norma primaria

para dióxido de nitrógeno (NO 2 ).

**Tabla 7-8. Resultados del modelo de dispersión para NO** **2** **[μg/m** **[3]** **N]. Escenario Sinérgico Fase de Operación**

**Base.**

|Receptor|Descripción|Dióxido de Nitrógeno (NO )<br>2|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|6,866|0,668|400|100|1,7%|0,7%|
|R_2|Estación Tierra Amarilla|12,448|1,114|1,114|1,114|3,1%|1,1%|
|R_3|Estación Ojanco|16,481|1,237|1,237|1,237|4,1%|1,2%|
|R_4|Estación Kozan|32,737|1,741|1,741|1,741|8,2%|1,7%|
|R_5|133 casa (Carola Norte)|5,148|0,408|0,408|0,408|1,3%|0,4%|
|R_6|Iglesia Tierra Amarilla|6,877|0,788|0,788|0,788|1,7%|0,8%|
|R_7|El Minero|50,532|1,562|1,562|1,562|12,6%|1,6%|
|R_8|Testigoteca|35,586|1,110|1,110|1,110|8,9%|1,1%|
|R_9|Estadio|99,246|2,661|2,661|2,661|24,8%|2,7%|
|R_10|Agrouva I|58,638|2,252|2,252|2,252|14,7%|2,3%|
|R_11|Agrouva II|20,055|1,568|1,568|1,568|5,0%|1,6%|
|R_12|Receptor ruido|41,342|1,538|1,538|1,538|10,3%|1,5%|
|R_13|Receptor ruido|36,394|1,165|1,165|1,165|9,1%|1,2%|
|R_14|Receptor ruido|20,329|1,168|1,168|1,168|5,1%|1,2%|
|R_15|Receptor ruido|41,803|1,425|1,425|1,425|10,5%|1,4%|
|R_16|Receptor ruido|56,478|1,658|1,658|1,658|14,1%|1,7%|
|R_17|Receptor ruido|41,873|1,471|1,471|1,471|10,5%|1,5%|
|R_18|Receptor ruido|204,480|3,490|3,490|3,490|51,1%|3,5%|
|R_19|Receptor ruido|115,590|2,810|2,810|2,810|28,9%|2,8%|
|R_20|Receptor ruido|128,880|3,000|3,000|3,000|32,2%|3,0%|
|R_21|Receptor ruido|112,500|2,649|2,649|2,649|28,1%|2,6%|
|R_22|Receptor ruido|74,364|2,587|2,587|2,587|18,6%|2,6%|
|R_23|Receptor ruido|41,221|2,533|2,533|2,533|10,3%|2,5%|
|R_24|Receptor ruido|15,596|0,684|0,684|0,684|3,9%|0,7%|
|R_25|Receptor ruido|1,956|0,154|0,154|0,154|0,5%|0,2%|
|R_26|Receptor ruido|14,495|1,503|1,503|1,503|3,6%|1,5%|

www.dfmconsultores.cl

179

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Dióxido de Nitrógeno (NO )<br>2|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|
|R_27|Estación COEMIN|37,897|1,972|||9,5%|2,0%|
|R_28|Estación Nantoco|17,294|1,187|1,187|1,187|4,3%|1,2%|
|R_29|Estación C6|12,187|0,792|0,792|0,792|3,0%|0,8%|
|R_30|Estación C5|8,951|0,616|0,616|0,616|2,2%|0,6%|
|R_31|Estación C8|17,674|1,215|1,215|1,215|4,4%|1,2%|
|R_32|Estación C2|2,463|0,185|0,185|0,185|0,6%|0,2%|
|R_33|Estación C1|2,766|0,205|0,205|0,205|0,7%|0,2%|
|R_34|Estación C3|2,432|0,185|0,185|0,185|0,6%|0,2%|
|R_35|Estación C7|19,630|1,260|1,260|1,260|4,9%|1,3%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes sinérgicos actuales de los proyectos

sobre los receptores de interés alcanzan un máximo de 51,1% y 32,2% de la norma de este

contaminante en periodo horario, específicamente sobre los receptores denominados

“R_18” y “R_20”, los que corresponden a viviendas construidas con material mixto y

material ligero respectivamente. Por su parte, en cuanto a las concentraciones sinérgicas

actuales de NO 2 estimadas para periodo anual, estas representan hasta un 3,5% y 3,0% de

la normativa respectiva, particularmente en los receptores ya mencionados.

A continuación, en las siguientes figuras se presentan las curvas de isoconcentración de

dióxido de nitrógeno (NO 2 ) para periodo de 1 hora y periodo anual.

www.dfmconsultores.cl

180

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-10. Curvas de isoconcentración para percentil 99 periodo 1 hora. NO** **2** **[μg/m** **[3]** **N]. Escenario**

**Sinérgico Fase de Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

181

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-11. Curvas de isoconcentración para periodo anual. NO** **2** **(μg/m** **[3]** **N). Escenario Sinérgico Fase de**

**Operación Base.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

182

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

7.3.6 Dióxido de Azufre (SO 2 )

En la Tabla 7-9 se presentan los aportes sinérgicos generados durante la fase de operación actual de los proyectos “Optimización

Operacional Planta Cerrillos” y “Optimización Operacional Mina Carola” sobre los receptores de interés, específicamente sobre

receptores de medio humano y estaciones de monitoreo, conforme con la norma primaria para dióxido de azufre (SO 2 ).

**Tabla 7-9. Resultados del modelo de dispersión para SO** **2** **[μg/m** **[3]** **N]. Escenario Sinérgico Fase de Operación Base.**

|Receptor|Descripción|Dióxido de Azufre (SO )<br>2|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|0,010|0,003|0,002|350|150|60|0,0%|0,0%|0,0%|
|R_2|Estación Tierra Amarilla|0,016|0,006|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_3|Estación Ojanco|0,020|0,005|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_4|Estación Kozan|0,064|0,017|0,006|0,006|0,006|0,006|0,0%|0,0%|0,0%|
|R_5|133 casa (Carola Norte)|0,007|0,002|0,001|0,001|0,001|0,001|0,0%|0,0%|0,0%|
|R_6|Iglesia Tierra Amarilla|0,011|0,004|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_7|El Minero|0,068|0,016|0,006|0,006|0,006|0,006|0,0%|0,0%|0,0%|
|R_8|Testigoteca|0,046|0,013|0,004|0,004|0,004|0,004|0,0%|0,0%|0,0%|
|R_9|Estadio|0,100|0,035|0,007|0,007|0,007|0,007|0,0%|0,0%|0,0%|
|R_10|Agrouva I|0,055|0,019|0,006|0,006|0,006|0,006|0,0%|0,0%|0,0%|
|R_11|Agrouva II|0,022|0,006|0,003|0,003|0,003|0,003|0,0%|0,0%|0,0%|
|R_12|Receptor ruido|0,087|0,017|0,008|0,008|0,008|0,008|0,0%|0,0%|0,0%|
|R_13|Receptor ruido|0,047|0,014|0,004|0,004|0,004|0,004|0,0%|0,0%|0,0%|
|R_14|Receptor ruido|0,041|0,010|0,005|0,005|0,005|0,005|0,0%|0,0%|0,0%|
|R_15|Receptor ruido|0,107|0,018|0,006|0,006|0,006|0,006|0,0%|0,0%|0,0%|
|R_16|Receptor ruido|0,132|0,023|0,007|0,007|0,007|0,007|0,0%|0,0%|0,0%|
|R_17|Receptor ruido|0,082|0,017|0,006|0,006|0,006|0,006|0,0%|0,0%|0,0%|
|R_18|Receptor ruido|0,265|0,063|0,013|0,013|0,013|0,013|0,1%|0,0%|0,0%|

www.dfmconsultores.cl

183

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Dióxido de Azufre (SO )<br>2|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|
|R_19|Receptor ruido|0,108|0,040|0,008||||0,0%|0,0%|0,0%|
|R_20|Receptor ruido|0,147|0,046|0,009|0,009|0,009|0,009|0,0%|0,0%|0,0%|
|R_21|Receptor ruido|0,126|0,031|0,008|0,008|0,008|0,008|0,0%|0,0%|0,0%|
|R_22|Receptor ruido|0,107|0,033|0,012|0,012|0,012|0,012|0,0%|0,0%|0,0%|
|R_23|Receptor ruido|0,339|0,086|0,038|0,038|0,038|0,038|0,1%|0,1%|0,1%|
|R_24|Receptor ruido|0,063|0,012|0,003|0,003|0,003|0,003|0,0%|0,0%|0,0%|
|R_25|Receptor ruido|0,003|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_26|Receptor ruido|0,031|0,010|0,005|0,005|0,005|0,005|0,0%|0,0%|0,0%|
|R_27|Estación COEMIN|0,309|0,062|0,026|0,026|0,026|0,026|0,1%|0,0%|0,0%|
|R_28|Estación Nantoco|0,048|0,012|0,005|0,005|0,005|0,005|0,0%|0,0%|0,0%|
|R_29|Estación C6|0,042|0,008|0,003|0,003|0,003|0,003|0,0%|0,0%|0,0%|
|R_30|Estación C5|0,025|0,006|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_31|Estación C8|0,064|0,014|0,006|0,006|0,006|0,006|0,0%|0,0%|0,0%|
|R_32|Estación C2|0,004|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_33|Estación C1|0,005|0,001|0,001|0,001|0,001|0,001|0,0%|0,0%|0,0%|
|R_34|Estación C3|0,004|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_35|Estación C7|0,072|0,015|0,007|0,007|0,007|0,007|0,0%|0,0%|0,0%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

184

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Tal como se observa en la tabla anterior, los aportes sinérgicos actuales de los proyectos

sobre los receptores de interés no superan el 0,1% de la norma de este contaminante en

periodo horario, diario y anual, específicamente sobre el receptor denominado “R_23”, el

cual corresponde a las oficinas de la empresa agrícola Uvas del Norte. En consecuencia, es

posible establecer que la contribución sinérgica actual de los proyectos sobre los receptores

de interés, en cuanto a emisiones de SO 2, es prácticamente nula.

En consecuencia, considerando que los aportes de concentración de SO 2 percibidos en los

receptores son menores a 14,0 μg/m [3] N en periodo horario, 2,0 μg/m [3] N en periodo diario y

1,2 μg/m [3] N en periodo anual, valores correspondientes a los límites de los Niveles de

Impacto Significativo para este contaminante según lo indicado en el documento

“Evaluación Significancia del Impacto de las Emisiones de un Proyecto o Actividad en Zonas

Saturadas en el Marco del SEIA” (DICTUC, 2022), en esta oportunidad no se presentan

curvas de isoconcentración de dióxido de azufre asociadas al efecto sinérgico de la fase de

operación actual de los proyectos señalados.

www.dfmconsultores.cl

185

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

#### 7.4 Resultados Modelación Escenario Sinérgico Fase de Operación Proyectada

A continuación, en los siguientes apartados se presentan los resultados de la modelación

de dispersión de contaminantes realizada para el escenario sinérgico proyectado

correspondiente a la fase de operación futura de los proyectos “Optimización Operacional

Planta Cerrillos” y “Optimización Operacional Mina Carola”, considerando un tiempo de

desarrollo de 12 meses.

Para ello, se muestran las concentraciones proyectadas aportadas sobre los receptores de

interés mencionados con anterioridad a causa de la ejecución simultánea de ambos

proyectos indicados, realizando un análisis normativo de cada uno de los estadígrafos

indicados por las normativas y valores de referencia señalados en la sección 5.7.

A modo complementario, se presentan las curvas de isoconcentración e isodepositación,

según corresponde, conforme a las concentraciones y depositaciones obtenidas y

percibidas en el dominio de modelación.

www.dfmconsultores.cl

186

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

7.4.1 Material Particulado Respirable Fino (MP2.5)

En la Tabla 7-10 se presentan los aportes sinérgicos generados durante la fase de operación

proyectada de los proyectos “Optimización Operacional Planta Cerrillos” y “Optimización

Operacional Mina Carola” sobre los receptores de interés, específicamente sobre

receptores de medio humano y estaciones de monitoreo, conforme con la norma primaria

para material particulado respirable fino (MP2.5).

**Tabla 7-10. Resultados del modelo de dispersión para MP2.5 [μg/m** **[3]** **]. Escenario Sinérgico Fase de**

**Operación Proyectada.**

|Receptor|Descripción|Material Particulado Respirable Fino (MP2.5)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3] **|**Concentración [μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|0,986|0,475|50|20|2,0%|2,4%|
|R_2|Estación Tierra Amarilla|1,570|0,805|0,805|0,805|3,1%|4,0%|
|R_3|Estación Ojanco|1,481|0,642|0,642|0,642|3,0%|3,2%|
|R_4|Estación Kozan|3,773|1,320|1,320|1,320|7,5%|6,6%|
|R_5|133 casa (Carola Norte)|0,782|0,334|0,334|0,334|1,6%|1,7%|
|R_6|Iglesia Tierra Amarilla|1,216|0,613|0,613|0,613|2,4%|3,1%|
|R_7|El Minero|4,660|1,656|1,656|1,656|9,3%|8,3%|
|R_8|Testigoteca|2,805|0,995|0,995|0,995|5,6%|5,0%|
|R_9|Estadio|8,916|2,499|2,499|2,499|17,8%|12,5%|
|R_10|Agrouva I|5,466|1,766|1,766|1,766|10,9%|8,8%|
|R_11|Agrouva II|2,025|0,998|0,998|0,998|4,0%|5,0%|
|R_12|Receptor ruido|3,453|1,505|1,505|1,505|6,9%|7,5%|
|R_13|Receptor ruido|2,599|1,021|1,021|1,021|5,2%|5,1%|
|R_14|Receptor ruido|2,412|1,032|1,032|1,032|4,8%|5,2%|
|R_15|Receptor ruido|5,625|1,875|1,875|1,875|11,3%|9,4%|
|R_16|Receptor ruido|6,744|2,163|2,163|2,163|13,5%|10,8%|
|R_17|Receptor ruido|4,348|1,581|1,581|1,581|8,7%|7,9%|
|R_18|Receptor ruido|22,286|4,571|4,571|4,571|44,6%|22,9%|
|R_19|Receptor ruido|10,752|2,728|2,728|2,728|21,5%|13,6%|
|R_20|Receptor ruido|11,520|3,249|3,249|3,249|23,0%|16,2%|
|R_21|Receptor ruido|9,618|2,864|2,864|2,864|19,2%|14,3%|
|R_22|Receptor ruido|8,407|2,520|2,520|2,520|16,8%|12,6%|
|R_23|Receptor ruido|16,566|7,839|7,839|7,839|33,1%|39,2%|
|R_24|Receptor ruido|2,548|0,716|0,716|0,716|5,1%|3,6%|
|R_25|Receptor ruido|0,262|0,097|0,097|0,097|0,5%|0,5%|
|R_26|Receptor ruido|0,772|0,451|0,451|0,451|1,5%|2,3%|

www.dfmconsultores.cl

187

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Material Particulado Respirable Fino (MP2.5)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3] **|**Concentración [μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Norma de Calidad**<br>**[μg/m3] **|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_27|Estación COEMIN|12,467|5,512|||24,9%|27,6%|
|R_28|Estación Nantoco|1,388|0,646|0,646|0,646|2,8%|3,2%|
|R_29|Estación C6|1,036|0,562|0,562|0,562|2,1%|2,8%|
|R_30|Estación C5|0,890|0,438|0,438|0,438|1,8%|2,2%|
|R_31|Estación C8|1,871|0,969|0,969|0,969|3,7%|4,8%|
|R_32|Estación C2|0,326|0,120|0,120|0,120|0,7%|0,6%|
|R_33|Estación C1|0,366|0,134|0,134|0,134|0,7%|0,7%|
|R_34|Estación C3|0,321|0,118|0,118|0,118|0,6%|0,6%|
|R_35|Estación C7|1,951|1,030|1,030|1,030|3,9%|5,2%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes sinérgicos proyectados de los proyectos

sobre los receptores de interés alcanzan un máximo de 44,6% y 33,1% de la norma de este

contaminante en periodo diario, específicamente sobre los receptores denominados

“R_18” y “R_23”, los que corresponden a viviendas construidas con material mixto y a las

oficinas de la empresa agrícola Uvas del Norte según orden de mención. Por su parte, en

cuanto a los aportes sinérgicos proyectados de MP2.5 estimados para periodo anual, estos

representan hasta un 39,2% y 27,6% de la normativa respectiva, particularmente en los

receptores “R_23” y “R_27”, este último correspondiente a la estación de monitoreo

COEMIN.

A continuación, en las siguientes figuras se presentan las curvas de isoconcentración de

material particulado respirable fino (MP2.5) para periodo de 24 horas y periodo anual.

www.dfmconsultores.cl

188

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-12. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP2.5 [μg/m** **[3]** **]. Escenario**

**Sinérgico Fase de Operación Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

189

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-13. Curvas de isoconcentración para periodo anual. MP2.5 [μg/m** **[3]** **]. Escenario Sinérgico Fase de**

**Operación Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

190

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

7.4.2 Material Particulado Respirable (MP10)

En la Tabla 7-11 se presentan los aportes sinérgicos generados durante la fase de operación

proyectada de los proyectos “Optimización Operacional Planta Cerrillos” y “Optimización

Operacional Mina Carola” sobre los receptores de interés, específicamente sobre

receptores de medio humano y estaciones de monitoreo, conforme con la norma primaria

para material particulado respirable (MP10).

**Tabla 7-11. Resultados del modelo de dispersión para MP10 [μg/m** **[3]** **N]. Escenario Sinérgico Fase de**

**Operación Proyectada.**

|Receptor|Descripción|Material Particulado Respirable (MP10)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|2,014|0,976|130|50|1,5%|2,0%|
|R_2|Estación Tierra Amarilla|3,176|1,602|1,602|1,602|2,4%|3,2%|
|R_3|Estación Ojanco|2,982|1,443|1,443|1,443|2,3%|2,9%|
|R_4|Estación Kozan|9,906|3,564|3,564|3,564|7,6%|7,1%|
|R_5|133 casa (Carola Norte)|1,512|0,771|0,771|0,771|1,2%|1,5%|
|R_6|Iglesia Tierra Amarilla|2,386|1,214|1,214|1,214|1,8%|2,4%|
|R_7|El Minero|9,072|3,753|3,753|3,753|7,0%|7,5%|
|R_8|Testigoteca|5,826|2,373|2,373|2,373|4,5%|4,7%|
|R_9|Estadio|17,324|5,555|5,555|5,555|13,3%|11,1%|
|R_10|Agrouva I|10,725|4,050|4,050|4,050|8,3%|8,1%|
|R_11|Agrouva II|3,979|2,182|2,182|2,182|3,1%|4,4%|
|R_12|Receptor ruido|8,419|4,192|4,192|4,192|6,5%|8,4%|
|R_13|Receptor ruido|5,700|2,609|2,609|2,609|4,4%|5,2%|
|R_14|Receptor ruido|5,275|2,815|2,815|2,815|4,1%|5,6%|
|R_15|Receptor ruido|10,726|3,819|3,819|3,819|8,3%|7,6%|
|R_16|Receptor ruido|12,655|4,385|4,385|4,385|9,7%|8,8%|
|R_17|Receptor ruido|9,274|3,793|3,793|3,793|7,1%|7,6%|
|R_18|Receptor ruido|38,453|8,635|8,635|8,635|29,6%|17,3%|
|R_19|Receptor ruido|20,960|6,459|6,459|6,459|16,1%|12,9%|
|R_20|Receptor ruido|20,749|6,463|6,463|6,463|16,0%|12,9%|
|R_21|Receptor ruido|16,945|5,901|5,901|5,901|13,0%|11,8%|
|R_22|Receptor ruido|18,869|7,163|7,163|7,163|14,5%|14,3%|
|R_23|Receptor ruido|62,984|29,811|29,811|29,811|48,4%|59,6%|
|R_24|Receptor ruido|9,490|2,565|2,565|2,565|7,3%|5,1%|
|R_25|Receptor ruido|0,760|0,278|0,278|0,278|0,6%|0,6%|
|R_26|Receptor ruido|1,975|1,135|1,135|1,135|1,5%|2,3%|

www.dfmconsultores.cl

191

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Material Particulado Respirable (MP10)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|**P98 24**<br>**horas**|**Período**<br>**Anual**|
|R_27|Estación COEMIN|47,362|20,805|||36,4%|41,6%|
|R_28|Estación Nantoco|4,429|2,009|2,009|2,009|3,4%|4,0%|
|R_29|Estación C6|3,435|1,870|1,870|1,870|2,6%|3,7%|
|R_30|Estación C5|3,005|1,460|1,460|1,460|2,3%|2,9%|
|R_31|Estación C8|6,646|3,296|3,296|3,296|5,1%|6,6%|
|R_32|Estación C2|1,022|0,358|0,358|0,358|0,8%|0,7%|
|R_33|Estación C1|1,152|0,410|0,410|0,410|0,9%|0,8%|
|R_34|Estación C3|1,017|0,352|0,352|0,352|0,8%|0,7%|
|R_35|Estación C7|6,792|3,525|3,525|3,525|5,2%|7,1%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes sinérgicos proyectados de los proyectos

sobre los receptores de interés alcanzan un máximo de 48,4% y 36,4% de la norma de este

contaminante en periodo diario, específicamente sobre los receptores denominados

“R_23” y “R_27”, los que corresponden a las oficinas de la empresa agrícola Uvas del Norte

y a la estación de monitoreo COEMIN según orden de mención. Por su parte, en cuanto a

los aportes sinérgicos proyectados de MP10 estimados para periodo anual, estos

representan hasta un 59,6% y 41,6% de la normativa respectiva, particularmente en los

receptores indicados con anterioridad.

A continuación, en las siguientes figuras se presentan las curvas de isoconcentración de

material particulado respirable (MP10) para periodo de 24 horas y periodo anual.

www.dfmconsultores.cl

192

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-14. Curvas de isoconcentración para percentil 98 periodo 24 horas. MP10 [μg/m** **[3]** **N]. Escenario**

**Sinérgico Fase de Operación Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

193

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-15. Curvas de isoconcentración para periodo anual. MP10 [μg/m** **[3]** **N]. Escenario Sinérgico Fase de**

**Operación Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

194

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

7.4.3 Material Particulado Sedimentable (MPS)

En la Tabla 7-12 se presentan los aportes sinérgicos generados durante la fase de operación

proyectada de los proyectos “Optimización Operacional Planta Cerrillos” y “Optimización

Operacional Mina Carola” sobre los receptores de interés, específicamente sobre

receptores de medio humano y estaciones de monitoreo, conforme con las normas de

referencia internacionales de material particulado sedimentable (MPS).

**Tabla 7-12. Resultados del modelo de dispersión para MPS [mg/m** **[2∙]** **día]. Escenario Sinérgico Fase de**

**Operación Proyectada.**

|Receptor|Descripción|Material Particulado Sedimentable (MPS)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**Media**<br>**Anual**|**Máxima**<br>**Media**<br>**Mensual**|**Conf. Suiza**|**República**<br>**Argentina**|**Conf. Suiza**|**República**<br>**Argentina**|
|R_1|Estación Luis Uribe|1,373|2,340|200|333|0,7%|0,7%|
|R_2|Estación Tierra Amarilla|2,239|3,802|3,802|3,802|1,1%|1,1%|
|R_3|Estación Ojanco|1,642|2,393|2,393|2,393|0,8%|0,7%|
|R_4|Estación Kozan|14,456|17,876|17,876|17,876|7,2%|5,4%|
|R_5|133 casa (Carola Norte)|1,312|1,514|1,514|1,514|0,7%|0,5%|
|R_6|Iglesia Tierra Amarilla|1,627|2,949|2,949|2,949|0,8%|0,9%|
|R_7|El Minero|12,039|15,482|15,482|15,482|6,0%|4,6%|
|R_8|Testigoteca|7,571|9,082|9,082|9,082|3,8%|2,7%|
|R_9|Estadio|14,817|16,336|16,336|16,336|7,4%|4,9%|
|R_10|Agrouva I|11,158|11,990|11,990|11,990|5,6%|3,6%|
|R_11|Agrouva II|5,861|7,085|7,085|7,085|2,9%|2,1%|
|R_12|Receptor ruido|18,134|23,004|23,004|23,004|9,1%|6,9%|
|R_13|Receptor ruido|9,560|11,365|11,365|11,365|4,8%|3,4%|
|R_14|Receptor ruido|11,566|12,779|12,779|12,779|5,8%|3,8%|
|R_15|Receptor ruido|11,416|16,176|16,176|16,176|5,7%|4,9%|
|R_16|Receptor ruido|12,598|18,192|18,192|18,192|6,3%|5,5%|
|R_17|Receptor ruido|13,335|16,239|16,239|16,239|6,7%|4,9%|
|R_18|Receptor ruido|24,047|30,275|30,275|30,275|12,0%|9,1%|
|R_19|Receptor ruido|18,750|21,228|21,228|21,228|9,4%|6,4%|
|R_20|Receptor ruido|15,807|17,877|17,877|17,877|7,9%|5,4%|
|R_21|Receptor ruido|13,218|14,848|14,848|14,848|6,6%|4,5%|
|R_22|Receptor ruido|35,927|42,816|42,816|42,816|18,0%|12,9%|
|R_23|Receptor ruido|107,610|131,339|131,339|131,339|53,8%|39,4%|
|R_24|Receptor ruido|4,713|5,621|5,621|5,621|2,4%|1,7%|
|R_25|Receptor ruido|0,278|0,358|0,358|0,358|0,1%|0,1%|

www.dfmconsultores.cl

195

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Material Particulado Sedimentable (MPS)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Tasa de depositación**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Norma de Calidad**<br>**[mg/m2∙día]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**Media**<br>**Anual**|**Máxima**<br>**Media**<br>**Mensual**|**Conf. Suiza**|**República**<br>**Argentina**|**Conf. Suiza**|**República**<br>**Argentina**|
|R_26|Receptor ruido|1,830|2,562|||0,9%|0,8%|
|R_27|Estación COEMIN|67,216|81,553|81,553|81,553|33,6%|24,5%|
|R_28|Estación Nantoco|6,651|9,813|9,813|9,813|3,3%|2,9%|
|R_29|Estación C6|7,585|9,213|9,213|9,213|3,8%|2,8%|
|R_30|Estación C5|4,651|5,588|5,588|5,588|2,3%|1,7%|
|R_31|Estación C8|15,231|20,710|20,710|20,710|7,6%|6,2%|
|R_32|Estación C2|0,391|0,495|0,495|0,495|0,2%|0,1%|
|R_33|Estación C1|0,454|0,571|0,571|0,571|0,2%|0,2%|
|R_34|Estación C3|0,372|0,471|0,471|0,471|0,2%|0,1%|
|R_35|Estación C7|16,536|23,499|23,499|23,499|8,3%|7,1%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes sinérgicos proyectados del Proyecto

sobre los receptores de interés alcanzan un máximo de 53,8% y 33,6% de la norma de

referencia para periodo anual de la Confederación Suiza, particularmente sobre los

receptores denominados “R_23” y “R_27”, los que corresponden a las oficinas de la

empresa agrícola Uvas del Norte y a la estación de monitoreo COEMIN según orden de

mención. Por su parte, en cuanto a los valores proyectados de depositación de MPS

mensuales estimados, estos representan hasta un 39,4% y 24,5% de la norma de referencia

para periodo mensual de la República de Argentina, específicamente en los receptores ya

mencionados.

A continuación, en las siguientes figuras se presentan las curvas de isodepositación de

material particulado sedimentable (MPS) para periodo mensual y anual.

www.dfmconsultores.cl

196

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-16. Curvas de isodepositación para periodo mensual. MPS [mg/m** **[2]** **∙día]. Escenario Sinérgico Fase**

**de Operación Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

197

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-17. Curvas de isodepositación para periodo anual. MPS [mg/m** **[2]** **∙día]. Escenario Sinérgico Fase de**

**Operación Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

198

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

7.4.4 Monóxido de Carbono (CO)

En la Tabla 7-13 se presentan los aportes sinérgicos generados durante la fase de operación

proyectada de los proyectos “Optimización Operacional Planta Cerrillos” y “Optimización

Operacional Mina Carola” sobre los receptores de interés, específicamente sobre

receptores de medio humano y estaciones de monitoreo, conforme con la norma primaria

para monóxido de carbono (CO).

**Tabla 7-13. Resultados del modelo de dispersión para CO [mg/m** **[3]** **N]. Escenario Sinérgico Fase de**

**Operación Proyectada.**

|Receptor|Descripción|Monóxido de Carbono (CO)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[mg/m3N]**|**Concentración**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|
|R_1|Estación Luis Uribe|0,006|0,003|30|10|0,0%|0,0%|
|R_2|Estación Tierra Amarilla|0,010|0,004|0,004|0,004|0,0%|0,0%|
|R_3|Estación Ojanco|0,016|0,004|0,004|0,004|0,1%|0,0%|
|R_4|Estación Kozan|0,037|0,013|0,013|0,013|0,1%|0,1%|
|R_5|133 casa (Carola Norte)|0,006|0,002|0,002|0,002|0,0%|0,0%|
|R_6|Iglesia Tierra Amarilla|0,006|0,003|0,003|0,003|0,0%|0,0%|
|R_7|El Minero|0,076|0,014|0,014|0,014|0,3%|0,1%|
|R_8|Testigoteca|0,056|0,010|0,010|0,010|0,2%|0,1%|
|R_9|Estadio|0,146|0,028|0,028|0,028|0,5%|0,3%|
|R_10|Agrouva I|0,081|0,016|0,016|0,016|0,3%|0,2%|
|R_11|Agrouva II|0,020|0,005|0,005|0,005|0,1%|0,0%|
|R_12|Receptor ruido|0,059|0,012|0,012|0,012|0,2%|0,1%|
|R_13|Receptor ruido|0,051|0,010|0,010|0,010|0,2%|0,1%|
|R_14|Receptor ruido|0,033|0,007|0,007|0,007|0,1%|0,1%|
|R_15|Receptor ruido|0,087|0,016|0,016|0,016|0,3%|0,2%|
|R_16|Receptor ruido|0,102|0,019|0,019|0,019|0,3%|0,2%|
|R_17|Receptor ruido|0,069|0,014|0,014|0,014|0,2%|0,1%|
|R_18|Receptor ruido|0,311|0,063|0,063|0,063|1,0%|0,6%|
|R_19|Receptor ruido|0,159|0,031|0,031|0,031|0,5%|0,3%|
|R_20|Receptor ruido|0,203|0,034|0,034|0,034|0,7%|0,3%|
|R_21|Receptor ruido|0,169|0,030|0,030|0,030|0,6%|0,3%|
|R_22|Receptor ruido|0,098|0,028|0,028|0,028|0,3%|0,3%|
|R_23|Receptor ruido|0,155|0,051|0,051|0,051|0,5%|0,5%|
|R_24|Receptor ruido|0,039|0,009|0,009|0,009|0,1%|0,1%|
|R_25|Receptor ruido|0,002|0,001|0,001|0,001|0,0%|0,0%|
|R_26|Receptor ruido|0,012|0,006|0,006|0,006|0,0%|0,1%|

www.dfmconsultores.cl

199

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Monóxido de Carbono (CO)|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[mg/m3N]**|**Concentración**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Norma de Calidad**<br>**[mg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|**P99 1 hora**|**P99 8**<br>**horas**|
|R_27|Estación COEMIN|0,137|0,042|||0,5%|0,4%|
|R_28|Estación Nantoco|0,019|0,008|0,008|0,008|0,1%|0,1%|
|R_29|Estación C6|0,015|0,004|0,004|0,004|0,0%|0,0%|
|R_30|Estación C5|0,015|0,004|0,004|0,004|0,0%|0,0%|
|R_31|Estación C8|0,024|0,008|0,008|0,008|0,1%|0,1%|
|R_32|Estación C2|0,002|0,001|0,001|0,001|0,0%|0,0%|
|R_33|Estación C1|0,003|0,001|0,001|0,001|0,0%|0,0%|
|R_34|Estación C3|0,002|0,001|0,001|0,001|0,0%|0,0%|
|R_35|Estación C7|0,027|0,009|0,009|0,009|0,1%|0,1%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes sinérgicos proyectados de los proyectos

sobre los receptores de interés alcanzan un máximo de 1,0% y 0,7% de este contaminante

en periodo horario, específicamente sobre los receptores denominados “R_18” y “R_20”,

los que corresponden a viviendas construidas con material mixto y material ligero

respectivamente. Mientras que, en cuanto a las concentraciones sinérgicas proyectadas

estimadas para periodo de 8 horas, éstas no superan el 0,6% de la norma respectiva,

particularmente en el receptor “R_18”. En consecuencia, es posible establecer que la

contribución sinérgica proyectada de los proyectos sobre los receptores de interés, en

cuanto a emisiones de CO, es bastante mínima.

En consecuencia, considerando que los aportes de concentración de CO percibidos en los

receptores son menores a 1,5 mg/m [3] N en periodo horario y 0,4889 mg/m [3] N en periodo de

ocho horas, valores correspondientes a los límites de los Niveles de Impacto Significativo

para este contaminante según lo indicado en el documento “Evaluación Significancia del

Impacto de las Emisiones de un Proyecto o Actividad en Zonas Saturadas en el Marco del

SEIA” (DICTUC, 2022), en esta oportunidad no se presentan curvas de isoconcentración de

monóxido de carbono asociadas al efecto sinérgico de la fase de operación proyectada de

los proyectos señalados.

www.dfmconsultores.cl

200

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

7.4.5 Dióxido de Nitrógeno (NO 2 )

En la Tabla 7-14 se presentan los aportes sinérgicos generados durante la fase de operación

proyectada de los proyectos “Optimización Operacional Planta Cerrillos” y “Optimización

Operacional Mina Carola” sobre los receptores de interés, específicamente sobre

receptores de medio humano y estaciones de monitoreo, conforme con la norma primaria

para dióxido de nitrógeno (NO 2 ).

**Tabla 7-14. Resultados del modelo de dispersión para NO** **2** **[μg/m** **[3]** **N]. Escenario Sinérgico Fase de**

**Operación Proyectada.**

|Receptor|Descripción|Dióxido de Nitrógeno (NO )<br>2|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|7,531|0,732|400|100|1,9%|0,7%|
|R_2|Estación Tierra Amarilla|13,661|1,221|1,221|1,221|3,4%|1,2%|
|R_3|Estación Ojanco|18,093|1,357|1,357|1,357|4,5%|1,4%|
|R_4|Estación Kozan|35,882|1,911|1,911|1,911|9,0%|1,9%|
|R_5|133 casa (Carola Norte)|5,646|0,446|0,446|0,446|1,4%|0,4%|
|R_6|Iglesia Tierra Amarilla|7,527|0,864|0,864|0,864|1,9%|0,9%|
|R_7|El Minero|55,415|1,713|1,713|1,713|13,9%|1,7%|
|R_8|Testigoteca|39,039|1,218|1,218|1,218|9,8%|1,2%|
|R_9|Estadio|108,880|2,920|2,920|2,920|27,2%|2,9%|
|R_10|Agrouva I|64,202|2,472|2,472|2,472|16,1%|2,5%|
|R_11|Agrouva II|21,993|1,722|1,722|1,722|5,5%|1,7%|
|R_12|Receptor ruido|45,341|1,687|1,687|1,687|11,3%|1,7%|
|R_13|Receptor ruido|39,923|1,278|1,278|1,278|10,0%|1,3%|
|R_14|Receptor ruido|22,312|1,281|1,281|1,281|5,6%|1,3%|
|R_15|Receptor ruido|45,854|1,564|1,564|1,564|11,5%|1,6%|
|R_16|Receptor ruido|61,936|1,818|1,818|1,818|15,5%|1,8%|
|R_17|Receptor ruido|45,969|1,614|1,614|1,614|11,5%|1,6%|
|R_18|Receptor ruido|224,180|3,829|3,829|3,829|56,0%|3,8%|
|R_19|Receptor ruido|126,800|3,084|3,084|3,084|31,7%|3,1%|
|R_20|Receptor ruido|141,250|3,291|3,291|3,291|35,3%|3,3%|
|R_21|Receptor ruido|123,410|2,906|2,906|2,906|30,9%|2,9%|
|R_22|Receptor ruido|81,598|2,840|2,840|2,840|20,4%|2,8%|
|R_23|Receptor ruido|45,229|2,783|2,783|2,783|11,3%|2,8%|
|R_24|Receptor ruido|17,104|0,751|0,751|0,751|4,3%|0,8%|
|R_25|Receptor ruido|2,146|0,169|0,169|0,169|0,5%|0,2%|
|R_26|Receptor ruido|15,932|1,651|1,651|1,651|4,0%|1,7%|
|R_27|Estación COEMIN|41,577|2,166|2,166|2,166|10,4%|2,2%|

www.dfmconsultores.cl

201

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Dióxido de Nitrógeno (NO )<br>2|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración**<br>**[μg/m3N]**|**Concentración**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Norma de Calidad**<br>**[μg/m3N]**|**Porcentaje de la Norma**<br>**de Calidad**|**Porcentaje de la Norma**<br>**de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|**P99 1 hora**|**Período**<br>**Anual**|
|R_28|Estación Nantoco|18,990|1,304|||4,7%|1,3%|
|R_29|Estación C6|13,385|0,870|0,870|0,870|3,3%|0,9%|
|R_30|Estación C5|9,834|0,677|0,677|0,677|2,5%|0,7%|
|R_31|Estación C8|19,407|1,335|1,335|1,335|4,9%|1,3%|
|R_32|Estación C2|2,699|0,204|0,204|0,204|0,7%|0,2%|
|R_33|Estación C1|3,037|0,226|0,226|0,226|0,8%|0,2%|
|R_34|Estación C3|2,665|0,204|0,204|0,204|0,7%|0,2%|
|R_35|Estación C7|21,566|1,385|1,385|1,385|5,4%|1,4%|

Fuente: Elaboración propia.

Tal como se observa en la tabla anterior, los aportes sinérgicos proyectados de los proyectos

sobre los receptores de interés alcanzan un máximo de 56,0% y 35,3% de la norma de este

contaminante en periodo horario, específicamente sobre los receptores denominados

“R_18” y “R_20”, los que corresponden a viviendas construidas con material mixto y

material ligero respectivamente. Por su parte, en cuanto a las concentraciones sinérgicas

proyectadas de NO 2 estimadas para periodo anual, estas representan hasta un 3,8% y 3,3%

de la normativa respectiva, particularmente en los receptores ya mencionados.

A continuación, en las siguientes figuras se presentan las curvas de isoconcentración de

dióxido de nitrógeno (NO 2 ) para periodo de 1 hora y periodo anual.

www.dfmconsultores.cl

202

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-18. Curvas de isoconcentración para percentil 99 periodo 1 hora. NO** **2** **[μg/m** **[3]** **N]. Escenario**

**Sinérgico Fase de Operación Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

203

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Figura 7-19. Curvas de isoconcentración para periodo anual. NO** **2** **[μg/m** **[3]** **N]. Escenario Sinérgico Fase de**

**Operación Proyectada.**

Fuente: Elaboración propia.

www.dfmconsultores.cl

204

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

7.4.6 Dióxido de Azufre (SO 2 )

En la Tabla 7-15 se presentan los aportes sinérgicos generados durante la fase de operación proyectada de los proyectos “Optimización

Operacional Planta Cerrillos” y “Optimización Operacional Mina Carola” sobre los receptores de interés, específicamente sobre

receptores de medio humano y estaciones de monitoreo, conforme con la norma primaria para dióxido de azufre (SO 2 ).

**Tabla 7-15. Resultados del modelo de dispersión para SO** **2** **[μg/m** **[3]** **N]. Escenario Sinérgico Fase de Operación Proyectada.**

|Receptor|Descripción|Dióxido de Azufre (SO )<br>2|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|
|R_1|Estación Luis Uribe|0,011|0,004|0,002|350|150|60|0,0%|0,0%|0,0%|
|R_2|Estación Tierra Amarilla|0,018|0,006|0,003|0,003|0,003|0,003|0,0%|0,0%|0,0%|
|R_3|Estación Ojanco|0,022|0,005|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_4|Estación Kozan|0,070|0,018|0,006|0,006|0,006|0,006|0,0%|0,0%|0,0%|
|R_5|133 casa (Carola Norte)|0,008|0,002|0,001|0,001|0,001|0,001|0,0%|0,0%|0,0%|
|R_6|Iglesia Tierra Amarilla|0,013|0,004|0,002|0,002|0,002|0,002|0,0%|0,0%|0,0%|
|R_7|El Minero|0,075|0,018|0,007|0,007|0,007|0,007|0,0%|0,0%|0,0%|
|R_8|Testigoteca|0,051|0,015|0,004|0,004|0,004|0,004|0,0%|0,0%|0,0%|
|R_9|Estadio|0,110|0,038|0,008|0,008|0,008|0,008|0,0%|0,0%|0,0%|
|R_10|Agrouva I|0,060|0,021|0,006|0,006|0,006|0,006|0,0%|0,0%|0,0%|
|R_11|Agrouva II|0,024|0,007|0,004|0,004|0,004|0,004|0,0%|0,0%|0,0%|
|R_12|Receptor ruido|0,095|0,019|0,009|0,009|0,009|0,009|0,0%|0,0%|0,0%|
|R_13|Receptor ruido|0,051|0,015|0,005|0,005|0,005|0,005|0,0%|0,0%|0,0%|
|R_14|Receptor ruido|0,045|0,011|0,005|0,005|0,005|0,005|0,0%|0,0%|0,0%|
|R_15|Receptor ruido|0,118|0,020|0,007|0,007|0,007|0,007|0,0%|0,0%|0,0%|
|R_16|Receptor ruido|0,145|0,026|0,008|0,008|0,008|0,008|0,0%|0,0%|0,0%|
|R_17|Receptor ruido|0,090|0,019|0,007|0,007|0,007|0,007|0,0%|0,0%|0,0%|
|R_18|Receptor ruido|0,291|0,069|0,015|0,015|0,015|0,015|0,1%|0,0%|0,0%|

www.dfmconsultores.cl

205

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Descripción|Dióxido de Azufre (SO )<br>2|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Descripción**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Concentración [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Norma de Calidad [μg/m3N]**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|**Porcentaje de la Norma de Calidad**|
|**Receptor**|**Descripción**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|**P99 1 hora**|**P99 24**<br>**horas**|**Período**<br>**Anual**|
|R_19|Receptor ruido|0,119|0,043|0,009||||0,0%|0,0%|0,0%|
|R_20|Receptor ruido|0,162|0,051|0,010|0,010|0,010|0,010|0,0%|0,0%|0,0%|
|R_21|Receptor ruido|0,138|0,034|0,009|0,009|0,009|0,009|0,0%|0,0%|0,0%|
|R_22|Receptor ruido|0,118|0,036|0,013|0,013|0,013|0,013|0,0%|0,0%|0,0%|
|R_23|Receptor ruido|0,372|0,095|0,042|0,042|0,042|0,042|0,1%|0,1%|0,1%|
|R_24|Receptor ruido|0,069|0,014|0,003|0,003|0,003|0,003|0,0%|0,0%|0,0%|
|R_25|Receptor ruido|0,003|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_26|Receptor ruido|0,034|0,011|0,006|0,006|0,006|0,006|0,0%|0,0%|0,0%|
|R_27|Estación COEMIN|0,340|0,068|0,029|0,029|0,029|0,029|0,1%|0,0%|0,0%|
|R_28|Estación Nantoco|0,053|0,014|0,005|0,005|0,005|0,005|0,0%|0,0%|0,0%|
|R_29|Estación C6|0,047|0,009|0,004|0,004|0,004|0,004|0,0%|0,0%|0,0%|
|R_30|Estación C5|0,027|0,007|0,003|0,003|0,003|0,003|0,0%|0,0%|0,0%|
|R_31|Estación C8|0,071|0,015|0,007|0,007|0,007|0,007|0,0%|0,0%|0,0%|
|R_32|Estación C2|0,004|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_33|Estación C1|0,005|0,002|0,001|0,001|0,001|0,001|0,0%|0,0%|0,0%|
|R_34|Estación C3|0,004|0,001|0,000|0,000|0,000|0,000|0,0%|0,0%|0,0%|
|R_35|Estación C7|0,079|0,016|0,007|0,007|0,007|0,007|0,0%|0,0%|0,0%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

206

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

Tal como se observa en la tabla anterior, los aportes sinérgicos proyectados de los proyectos

sobre los receptores de interés no superan el 0,1% de la norma de este contaminante en

periodo horario, diario y anual, específicamente sobre el receptor denominado “R_23”, el

cual corresponde a las oficinas de la empresa agrícola Uvas del Norte. En consecuencia, es

posible establecer que la contribución sinérgica proyectada de los proyectos sobre los

receptores de interés, en cuanto a emisiones de SO 2, es prácticamente nula.

En consecuencia, considerando que los aportes de concentración de SO 2 percibidos en los

receptores son menores a 14,0 μg/m [3] N en periodo horario, 2,0 μg/m [3] N en periodo diario y

1,2 μg/m [3] N en periodo anual, valores correspondientes a los límites de los Niveles de

Impacto Significativo para este contaminante según lo indicado en el documento

“Evaluación Significancia del Impacto de las Emisiones de un Proyecto o Actividad en Zonas

Saturadas en el Marco del SEIA” (DICTUC, 2022), en esta oportunidad no se presentan

curvas de isoconcentración de dióxido de azufre asociadas al efecto sinérgico de la fase de

operación proyectada de los proyectos señalados.

www.dfmconsultores.cl

207

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

#### 7.5 Análisis de Significancia del Escenario Sinérgico

Tal como se ha señalado con anterioridad, el lugar de emplazamiento del Proyecto se ubica

en el área establecida como zona saturada por material particulado respirable (MP10) como

concentración diaria y anual de acuerdo con lo indicado en el Decreto N°15/2021 del

Ministerio del Medio Ambiente, por lo que se considera la presencia de un riesgo

preexistente conforme a la norma primaria de calidad ambiental asociada a este

contaminante. A causa de ello, y con el fin de evaluar la significancia del impacto de las

emisiones atmosféricas de este contaminante ocasionadas por el desarrollo del Proyecto, a

continuación, se presenta la variación entre los aportes de material particulado respirable

correspondientes a la operación actual y proyectada del Proyecto sobre cada uno de los

receptores de interés, estableciendo además su comparación con respecto a los niveles de

impacto significativo (SILs) establecidos por la autoridad.

Cabe señalar que, de manera conservadora, se ha considerado un aporte nulo en las

situaciones en donde las concentraciones de material particulado respirable actuales

superan aquellas proyectadas.

**Tabla 7-16. Análisis de Significancia Fase de Operación Sinérgica. MP10** **[μg/m** **[3]** **N]** **.**

|Receptor|Nivel de Impacto Significativo|Col3|Col4|Escenario Actual|Col6|Escenario Proyectado|Col8|Variación|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% SILs**|**Valor**|**% SILs**|**Valor**|**% SILs**|
|R_1|P98 24 horas|5|μg/m3N|2,12|42,5%|2,01|40,3%|0,00|0,0%|
|R_1|Media anual|1|μg/m3N|1,05|105,1%|0,98|97,6%|0,00|0,0%|
|R_2|P98 24 horas|5|μg/m3N|3,31|66,1%|3,18|63,5%|0,00|0,0%|
|R_2|Media anual|1|μg/m3N|1,69|168,9%|1,60|160,2%|0,00|0,0%|
|R_3|P98 24 horas|5|μg/m3N|3,18|63,6%|2,98|59,6%|0,00|0,0%|
|R_3|Media anual|1|μg/m3N|1,63|163,4%|1,44|144,3%|0,00|0,0%|
|R_4|P98 24 horas|5|μg/m3N|11,37|227,3%|9,91|198,1%|0,00|0,0%|
|R_4|Media anual|1|μg/m3N|4,35|435,5%|3,56|356,4%|0,00|0,0%|
|R_5|P98 24 horas|5|μg/m3N|2,02|40,4%|1,51|30,2%|0,00|0,0%|
|R_5|Media anual|1|μg/m3N|1,11|110,6%|0,77|77,1%|0,00|0,0%|
|R_6|P98 24 horas|5|μg/m3N|2,56|51,2%|2,39|47,7%|0,00|0,0%|
|R_6|Media anual|1|μg/m3N|1,32|132,2%|1,21|121,4%|0,00|0,0%|
|R_7|P98 24 horas|5|μg/m3N|10,23|204,6%|9,07|181,4%|0,00|0,0%|
|R_7|Media anual|1|μg/m3N|4,39|439,3%|3,75|375,3%|0,00|0,0%|

www.dfmconsultores.cl

208

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Nivel de Impacto Significativo|Col3|Col4|Escenario Actual|Col6|Escenario Proyectado|Col8|Variación|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% SILs**|**Valor**|**% SILs**|**Valor**|**% SILs**|
|R_8|P98 24 horas|5|μg/m3N|6,75|135,1%|5,83|116,5%|0,00|0,0%|
|R_8|Media anual|1|μg/m3N|2,81|281,3%|2,37|237,3%|0,00|0,0%|
|R_9|P98 24 horas|5|μg/m3N|19,23|384,5%|17,32|346,5%|0,00|0,0%|
|R_9|Media anual|1|μg/m3N|7,24|723,8%|5,56|555,5%|0,00|0,0%|
|R_10|P98 24 horas|5|μg/m3N|12,08|241,6%|10,73|214,5%|0,00|0,0%|
|R_10|Media anual|1|μg/m3N|5,13|513,4%|4,05|405,0%|0,00|0,0%|
|R_11|P98 24 horas|5|μg/m3N|4,32|86,4%|3,98|79,6%|0,00|0,0%|
|R_11|Media anual|1|μg/m3N|2,59|259,4%|2,18|218,2%|0,00|0,0%|
|R_12|P98 24 horas|5|μg/m3N|10,60|211,9%|8,42|168,4%|0,00|0,0%|
|R_12|Media anual|1|μg/m3N|5,50|549,6%|4,19|419,2%|0,00|0,0%|
|R_13|P98 24 horas|5|μg/m3N|6,90|138,0%|5,70|114,0%|0,00|0,0%|
|R_13|Media anual|1|μg/m3N|3,16|315,7%|2,61|260,9%|0,00|0,0%|
|R_14|P98 24 horas|5|μg/m3N|5,99|119,8%|5,27|105,5%|0,00|0,0%|
|R_14|Media anual|1|μg/m3N|3,38|338,4%|2,82|281,5%|0,00|0,0%|
|R_15|P98 24 horas|5|μg/m3N|10,52|210,5%|10,73|214,5%|0,20|4,0%|
|R_15|Media anual|1|μg/m3N|4,08|408,0%|3,82|381,9%|0,00|0,0%|
|R_16|P98 24 horas|5|μg/m3N|12,51|250,2%|12,66|253,1%|0,15|2,9%|
|R_16|Media anual|1|μg/m3N|4,61|461,4%|4,39|438,5%|0,00|0,0%|
|R_17|P98 24 horas|5|μg/m3N|10,45|208,9%|9,27|185,5%|0,00|0,0%|
|R_17|Media anual|1|μg/m3N|4,33|433,1%|3,79|379,3%|0,00|0,0%|
|R_18|P98 24 horas|5|μg/m3N|35,80|715,9%|38,45|769,1%|2,66|53,2%|
|R_18|Media anual|1|μg/m3N|8,74|874,3%|8,64|863,5%|0,00|0,0%|
|R_19|P98 24 horas|5|μg/m3N|23,27|465,3%|20,96|419,2%|0,00|0,0%|
|R_19|Media anual|1|μg/m3N|9,02|901,6%|6,46|645,9%|0,00|0,0%|
|R_20|P98 24 horas|5|μg/m3N|20,82|416,4%|20,75|415,0%|0,00|0,0%|
|R_20|Media anual|1|μg/m3N|7,42|742,4%|6,46|646,3%|0,00|0,0%|
|R_21|P98 24 horas|5|μg/m3N|18,37|367,3%|16,95|338,9%|0,00|0,0%|
|R_21|Media anual|1|μg/m3N|7,30|730,0%|5,90|590,1%|0,00|0,0%|
|R_22|P98 24 horas|5|μg/m3N|21,23|424,6%|18,87|377,4%|0,00|0,0%|
|R_22|Media anual|1|μg/m3N|8,73|872,6%|7,16|716,3%|0,00|0,0%|
|R_23|P98 24 horas|5|μg/m3N|62,56|1251,2%|62,98|1259,7%|0,42|8,5%|
|R_23|Media anual|1|μg/m3N|28,86|2886,1%|29,81|2981,1%|0,95|95,0%|

www.dfmconsultores.cl

**info@dfmconsultores.cl**

209

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

|Receptor|Nivel de Impacto Significativo|Col3|Col4|Escenario Actual|Col6|Escenario Proyectado|Col8|Variación|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Receptor**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% SILs**|**Valor**|**% SILs**|**Valor**|**% SILs**|
|R_24|P98 24 horas|5|μg/m3N|9,55|191,1%|9,49|189,8%|0,00|0,0%|
|R_24|Media anual|1|μg/m3N|2,65|264,7%|2,57|256,5%|0,00|0,0%|
|R_25|P98 24 horas|5|μg/m3N|0,92|18,4%|0,76|15,2%|0,00|0,0%|
|R_25|Media anual|1|μg/m3N|0,33|32,8%|0,28|27,8%|0,00|0,0%|
|R_26|P98 24 horas|5|μg/m3N|7,21|144,1%|1,98|39,5%|0,00|0,0%|
|R_26|Media anual|1|μg/m3N|3,80|379,7%|1,13|113,5%|0,00|0,0%|
|R_27|P98 24 horas|5|μg/m3N|45,44|908,8%|47,36|947,2%|1,92|38,4%|
|R_27|Media anual|1|μg/m3N|19,91|1990,8%|20,81|2080,5%|0,90|89,7%|
|R_28|P98 24 horas|5|μg/m3N|8,37|167,4%|4,43|88,6%|0,00|0,0%|
|R_28|Media anual|1|μg/m3N|3,50|350,2%|2,01|200,9%|0,00|0,0%|
|R_29|P98 24 horas|5|μg/m3N|4,65|93,1%|3,43|68,7%|0,00|0,0%|
|R_29|Media anual|1|μg/m3N|2,55|255,0%|1,87|187,0%|0,00|0,0%|
|R_30|P98 24 horas|5|μg/m3N|4,12|82,4%|3,01|60,1%|0,00|0,0%|
|R_30|Media anual|1|μg/m3N|1,91|191,1%|1,46|146,0%|0,00|0,0%|
|R_31|P98 24 horas|5|μg/m3N|9,45|189,0%|6,65|132,9%|0,00|0,0%|
|R_31|Media anual|1|μg/m3N|4,64|463,6%|3,30|329,6%|0,00|0,0%|
|R_32|P98 24 horas|5|μg/m3N|1,15|23,0%|1,02|20,4%|0,00|0,0%|
|R_32|Media anual|1|μg/m3N|0,41|41,3%|0,36|35,8%|0,00|0,0%|
|R_33|P98 24 horas|5|μg/m3N|1,28|25,7%|1,15|23,0%|0,00|0,0%|
|R_33|Media anual|1|μg/m3N|0,47|46,9%|0,41|41,0%|0,00|0,0%|
|R_34|P98 24 horas|5|μg/m3N|1,13|22,5%|1,02|20,3%|0,00|0,0%|
|R_34|Media anual|1|μg/m3N|0,41|40,8%|0,35|35,2%|0,00|0,0%|
|R_35|P98 24 horas|5|μg/m3N|9,78|195,6%|6,79|135,8%|0,00|0,0%|
|R_35|Media anual|1|μg/m3N|4,99|499,0%|3,53|352,5%|0,00|0,0%|

Fuente: Elaboración propia.

Conforme a los resultados de la tabla anterior, es posible observar que gran cantidad de los

receptores de interés estudiados presenta una disminución de los aportes de material

particulado respirable percibidos durante el desarrollo de la fase de operación sinérgica

proyectada de los proyectos “Optimización Operacional Mina Carola” y “Optimización

Operacional Planta Cerrillos”, en comparación con aquellos valores estimados para la fase

de operación sinérgica actual. De este modo, y de manera conservadora, se establece una

www.dfmconsultores.cl

210

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

variación nula de las concentraciones de MP10 y, en consecuencia, aportes insignificantes

en comparación a los niveles de impacto significativos indicados para este contaminante.

En cambio, es posible identificar que, los receptores denominados “R_15”, “R_16” y “R_18”,

correspondientes a oficinas (galpones y container) de material mixto, viviendas de material

ligero y viviendas de material mixto respectivamente, presentan un incremento en los

aportes de MP10 en periodo diario durante la operación sinérgica proyectada de los

proyectos ya mencionados, aumentando las concentraciones en 0,20, 0,15 y 2,66 [μg/m [3] N]

según orden de mención.

Por su parte, los receptores denominados “R_23” y “R_27” correspondientes a las oficinas

de la empresa agrícola Uvas del Norte y a la estación de monitoreo COEMIN según orden

de mención, presentan un aumento de los aportes de MP10 en periodo diario y anual

durante el escenario sinérgico proyectado, incrementando las magnitudes de este

contaminante en 0,42 y 1,92 [μg/m [3] N] en periodo diario y, 0,95 y 0,90 [μg/m [3] N] en periodo

anual respectivamente.

Sin embargo, los aportes de MP10 estimados para los receptores señalados en los párrafos

anteriores se encuentran por bajo los límites de impacto significativo establecidos por la

autoridad, por lo que es posible descartar la afectación sobre el riesgo de la salud de la

población, en cuanto a calidad del aire se trata, como consecuencia del desarrollo en

conjunto de las operaciones de los proyectos.

www.dfmconsultores.cl

211

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

#### 7.6 Concentración Total Proyectada

A continuación, se presentan las concentraciones totales sinérgicas esperadas en aquellos

lugares geográficos con los que se cuenta con registros de monitoreo de calidad del aire, las

cuales se han calculado por medio de la suma entre las concentraciones correspondientes

a la línea de base proyectada y los aportes sinérgicos proyectados de contaminantes

atmosféricos relacionados a la fase de operación de los proyectos “Optimización

Operacional Mina Carola” y “Optimización Operacional Planta Cerrillos”. Además, se

presenta un breve análisis de los valores resultantes en comparación a las normativas

primarias y de referencia de calidad del aire vigentes.

Cabe señalar que, tal como se indicó anteriormente, ambos proyectos se encuentran

actualmente en su etapa de operación, por lo que los aportes sinérgicos proyectados

resultantes corresponden a la diferencia entre las concentraciones y/o depositaciones

sinérgicas proyectadas y sinérgicas basales, esto con el fin de obtener solamente aquellos

aportes asociados al aumento de producción y procesamiento de ambos proyectos en

cuestión. De este modo, los aportes sinérgicos corresponden a lo siguiente:

Aportes Sinérgicos de Proyectos

= Aportes Escenario Sinérgico Proyectado−Aportes Escenario Sinérgico Base

Es necesario indicar que, de manera conservadora, se ha considerado un aporte nulo en las

situaciones en donde las concentraciones y/o depositaciones sinérgicas superan aquellas

sinérgicas proyectadas.

**Tabla 7-17. Concentración/ Depositación Total Sinérgica Proyectada. Estación Tierra Amarilla.**

|Contaminante|Normativa Vigente|Col3|Col4|Línea de Base<br>Proyectada|Col6|Aportes Sinérgicos de<br>Proyectos|Col8|Concentración/<br>Depositación Total<br>Sinérgica Proyectada|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% Norma**|**Valor**|**% Norma**|**Valor**|**% Norma**|
|Material Particulado<br>Respirable Fino<br>(MP2.5)|P98 24 horas|50|μg/m3N|31,4|62,8%|0,1|0,1%|31,5|62,9%|
|Material Particulado<br>Respirable Fino<br>(MP2.5)|Media anual|20|μg/m3N|14,2|70,9%|0,0|0,2%|14,2|71,1%|
|Material Particulado<br>Respirable (MP10)|P98 24 horas|130|μg/m3N|125,4|96,5%|0,0|0,0%|125,4|96,5%|
|Material Particulado<br>Respirable (MP10)|Media anual|50|μg/m3N|56,4|112,7%|0,0|0,0%|56,4|112,7%|
|Material Particulado<br>Sedimentable (MPS)|Media mensual|333|mg/m2día|356,0|106,9%|0,0|0,0%|356,0|106,9%|
|Material Particulado<br>Sedimentable (MPS)|Media anual|200|mg/m2día|226,8|113,4%|0,0|0,0%|226,8|113,4%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

212

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Tabla 7-18. Concentración Total Sinérgica Proyectada. Estación Luis Uribe.**

|Contaminante|Normativa Vigente|Col3|Col4|Línea de Base<br>Proyectada|Col6|Aportes Sinérgicos de<br>Proyectos|Col8|Concentración Total<br>Sinérgica Proyectada|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% Norma**|**Valor**|**% Norma**|**Valor**|**% Norma**|
|Material Particulado<br>Respirable Fino<br>(MP2.5)|P98 24 horas|50|μg/m3N|14,0|28,0%|0,0|0,1%|14,0|28,1%|
|Material Particulado<br>Respirable Fino<br>(MP2.5)|Media anual|20|μg/m3N|8,7|43,5%|0,0|0,1%|8,7|43,6%|
|Material Particulado<br>Respirable (MP10)|P98 24 horas|130|μg/m3N|74,2|57,1%|0,0|0,0%|74,2|57,1%|
|Material Particulado<br>Respirable (MP10)|Media anual|50|μg/m3N|49,1|98,2%|0,0|0,0%|49,1|98,2%|

|Contaminante|Normativa Vigente|Col3|Col4|Línea de Base<br>Proyectada|Col6|Aportes Sinérgicos de<br>Proyectos|Col8|Concentración Total<br>Sinérgica Proyectada|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% Norma**|**Valor**|**% Norma**|**Valor**|**% Norma**|
|Material Particulado<br>Respirable (MP10)|P98 24 horas|130|μg/m3N|73,1|56,2%|0,0|0,0%|73,1|56,2%|
|Material Particulado<br>Respirable (MP10)|Media anual|50|μg/m3N|45,8|91,6%|0,0|0,0%|45,8|91,6%|

|Contaminante|Normativa Vigente|Col3|Col4|Línea de Base<br>Proyectada|Col6|Aportes Sinérgicos de<br>Proyecto|Col8|Concentración Total<br>Sinérgica Proyectada|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% Norma**|**Valor**|**% Norma**|**Valor**|**% Norma**|
|Material Particulado<br>Respirable Fino<br>(MP2.5)|P98 24 horas|50|μg/m3N|15,0|30,0%|0,1|0,1%|15,1|30,1%|
|Material Particulado<br>Respirable Fino<br>(MP2.5)|Media anual|20|μg/m3N|9,6|48,0%|0,0|0,0%|9,6|48,0%|
|Material Particulado<br>Respirable (MP10)|P98 24 horas|130|μg/m3N|72,1|55,5%|0,0|0,0%|72,1|55,5%|
|Material Particulado<br>Respirable (MP10)|Media anual|50|μg/m3N|46,0|92,0%|0,0|0,0%|46,0|92,0%|

Fuente: Elaboración propia.

Fuente: Elaboración propia.

**Tabla 7-19. Concentración Total Sinérgica Proyectada. Estación Kozan.**

Fuente: Elaboración propia.

**Tabla 7-20. Concentración Total Sinérgica Proyectada. Estación Ojanco.**

**Tabla 7-21. Concentración Total Sinérgica Proyectada. Estación COEMIN.**

|Contaminante|Normativa Vigente|Col3|Col4|Línea de Base<br>Proyectada|Col6|Aportes Sinérgicos de<br>Proyecto|Col8|Concentración Total<br>Sinérgica Proyectada|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% Norma**|<br>**Valor**|**% Norma**|<br>**Valor**|**% Norma**|
|Material Particulado<br>Respirable (MP10)|P98 24 horas|130|μg/m3N|96,0|73,8%|1,9|1,5%|97,9|75,3%|
|Material Particulado<br>Respirable (MP10)|Media anual|50|μg/m3N|45,8|91,6%|0,9|1,8%|46,7|93,4%|

Fuente: Elaboración propia.

www.dfmconsultores.cl

**info@dfmconsultores.cl**

213

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Tabla 7-22. Concentración Total Sinérgica Proyectada. Estación Nantoco.**

|Contaminante|Normativa Vigente|Col3|Col4|Línea de Base<br>Proyectada|Col6|Aportes Sinérgicos de<br>Proyecto|Col8|Concentración Total<br>Sinérgica Proyectada|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% Norma**|**Valor**|**% Norma**|**Valor**|**% Norma**|
|Material Particulado<br>Respirable (MP10)|P98 24 horas|130|μg/m3N|103,0|79,2%|0,0|0,0%|103,0|79,2%|
|Material Particulado<br>Respirable (MP10)|Media anual|50|μg/m3N|64,5|129,0%|0,0|0,0%|64,5|129,0%|

|Contaminante|Normativa Vigente|Col3|Col4|Línea de Base<br>Proyectada|Col6|Aportes Sinérgicos de<br>Proyecto|Col8|Concentración Total<br>Sinérgica Proyectada|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% Norma**|**Valor**|**% Norma**|**Valor**|**% Norma**|
|Material Particulado<br>Respirable (MP10)|P98 24 horas|130|μg/m3N|54,0|41,5%|0,0|0,0%|54,0|41,5%|
|Material Particulado<br>Respirable (MP10)|Media anual|50|μg/m3N|39,5|79,0%|0,0|0,0%|39,5|79,0%|

|Contaminante|Normativa Vigente|Col3|Col4|Línea de Base<br>Proyectada|Col6|Aportes Sinérgicos de<br>Proyecto|Col8|Concentración Total<br>Sinérgica Proyectada|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% Norma**|**Valor**|**% Norma**|**Valor**|**% Norma**|
|Material Particulado<br>Respirable (MP10)|P98 24 horas|130|μg/m3N|62,0|47,7%|0,0|0,0%|62,0|47,7%|
|Material Particulado<br>Respirable (MP10)|Media anual|50|μg/m3N|50,8|101,6%|0,0|0,0%|50,8|101,6%|

|Contaminante|Normativa Vigente|Col3|Col4|Línea de Base<br>Proyectada|Col6|Aportes Sinérgicos de<br>Proyecto|Col8|Concentración Total<br>Sinérgica Proyectada|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% Norma**|**Valor**|**% Norma**|**Valor**|**% Norma**|
|Material Particulado<br>Respirable (MP10)|P98 24 horas|130|μg/m3N|52,0|40,0%|0,0|0,0%|52,0|40,0%|
|Material Particulado<br>Respirable (MP10)|Media anual|50|μg/m3N|36,8|73,6%|0,0|0,0%|36,8|73,6%|

|Contaminante|Normativa Vigente|Col3|Col4|Línea de Base<br>Proyectada|Col6|Aportes Sinérgicos de<br>Proyecto|Col8|Concentración Total<br>Sinérgica Proyectada|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% Norma**|**Valor**|**% Norma**|**Valor**|**% Norma**|
|Material Particulado<br>Respirable (MP10)|P98 24 horas|130|μg/m3N|59,0|45,4%|0,0|0,0%|59,0|45,4%|
|Material Particulado<br>Respirable (MP10)|Media anual|50|μg/m3N|53,8|107,6%|0,0|0,0%|53,8|107,6%|

Fuente: Elaboración propia.

Fuente: Elaboración propia.

**Tabla 7-23. Concentración Total Sinérgica Proyectada. Estación C5.**

Fuente: Elaboración propia.

**Tabla 7-24. Concentración Total Sinérgica Proyectada. Estación C6.**

Fuente: Elaboración propia.

**Tabla 7-25. Concentración Total Sinérgica Proyectada. Estación C8.**

Fuente: Elaboración propia.

**Tabla 7-26. Concentración Total Sinérgica Proyectada. Estación C2.**

www.dfmconsultores.cl

**info@dfmconsultores.cl**

214

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**Tabla 7-27. Concentración Total Sinérgica Proyectada. Estación C1.**

|Contaminante|Normativa Vigente|Col3|Col4|Línea de Base<br>Proyectada|Col6|Aportes Sinérgicos de<br>Proyecto|Col8|Concentración Total<br>Sinérgica Proyectada|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% Norma**|**Valor**|**% Norma**|**Valor**|**% Norma**|
|Material Particulado<br>Respirable (MP10)|P98 24 horas|130|μg/m3N|57,0|43,8%|0,0|0,0%|57,0|43,8%|
|Material Particulado<br>Respirable (MP10)|Media anual|50|μg/m3N|51,3|102,6%|0,0|0,0%|51,3|102,6%|

|Contaminante|Normativa Vigente|Col3|Col4|Línea de Base<br>Proyectada|Col6|Aportes Sinérgicos de<br>Proyecto|Col8|Concentración Total<br>Sinérgica Proyectada|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% Norma**|**Valor**|**% Norma**|**Valor**|**% Norma**|
|Material Particulado<br>Respirable (MP10)|P98 24 horas|130|μg/m3N|61,0|46,9%|0,0|0,0%|61,0|46,9%|
|Material Particulado<br>Respirable (MP10)|Media anual|50|μg/m3N|53,2|106,4%|0,0|0,0%|53,2|106,4%|

|Contaminante|Normativa Vigente|Col3|Col4|Línea de Base<br>Proyectada|Col6|Aportes Sinérgicos de<br>Proyecto|Col8|Concentración Total<br>Sinérgica Proyectada|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Contaminante**|**Estadígrafo**|**Valor**|**Unidad**|**Valor**|**% Norma**|**Valor**|**% Norma**|**Valor**|**% Norma**|
|Material Particulado<br>Respirable (MP10)|P98 24 horas|130|μg/m3N|63,0|48,5%|0,0|0,0%|61,0|46,9%|
|Material Particulado<br>Respirable (MP10)|Media anual|50|μg/m3N|52,7|105,4%|0,0|0,0%|53,2|106,4%|

Fuente: Elaboración propia.

Fuente: Elaboración propia.

**Tabla 7-28. Concentración Total Sinérgica Proyectada. Estación C3.**

Fuente: Elaboración propia.

**Tabla 7-29. Concentración Total Sinérgica Proyectada. Estación C7.**

De acuerdo con los resultados obtenidos en las tablas anteriores, es posible observar que,

las estaciones Tierra Amarilla, Luis Uribe y Ojanco presentan un mínimo incremento en los

aportes sinérgicos de MP2.5, tanto en periodo diario como anual, aumentando las

concentraciones totales de este contaminante en un máximo de 0,1% y 0,2% con respecto

a las normas para periodo diario y anual asociadas según orden de mención.

Asimismo, en la estación COEMIN se presenta un incremento de los aportes sinérgicos de

MP10, tanto para periodo diario como anual, aumentando las concentraciones totales de

este contaminante en un 1,5% y 1,8% con respecto a la normativa vigente para periodo

diario y anual respectivamente.

En cambio, los aportes sinérgicos de MP10 en las estaciones Tierra Amarilla, Luis Uribe,

Kozan, Ojanco, Nantoco, C6, C5, C8, C2, C1, C3 y C7 son nulos, así como también los aportes

de MPS en la estación Tierra Amarilla, pues las concentraciones y depositaciones estimadas

www.dfmconsultores.cl

215

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

asociadas al escenario sinérgico base superan el valor de aquellas estimadas para la fase de

operación sinérgica proyectada.

En consecuencia, es posible establecer que la futura operación conjunta de los proyectos

“Optimización Operacional Mina Carola” y “Optimización Operacional Planta Cerrillos” no

genera un incremento significativo de las concentraciones y depositaciones percibidas en

las locaciones de las estaciones de monitoreo de calidad del aire estudiadas, pues en gran

parte de ellas no se percibe un incremento alguno de las concentraciones de material

particulado respirable, como tampoco de las depositaciones de material particulado

sedimentable.

www.dfmconsultores.cl

216

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

### 8 CONCLUSIONES

En el presente informe se ha estimado y analizado el efecto sobre la calidad del aire sobre

receptores de interés cercanos durante el desarrollo de la fase de operación actual y

proyectada del Proyecto “Optimización Operacional Mina Carola”.

En primera instancia, es necesario indicar que, conforme al análisis del periodo

comprendido en el levantamiento de la línea de base de calidad del aire, Tierra Amarilla

registra una condición de saturación respecto a la norma primaria de calidad del aire de

material particulado respirable como concentración media anual. Esta situación se verifica

particularmente en los registros de monitoreo de la estación Tierra Amarilla, lo que

concuerda con lo establecido por el Decreto N°15/2021 del Ministerio del Medio Ambiente,

la cual establece las zonas de Copiapó y Tierra Amarilla como zonas saturadas por MP10

como concentración de 24 horas y anual.

Tras el análisis de los resultados de la modelación de dispersión de contaminantes,

específicamente de MP2.5, MP10, MPS, CO, NO 2 y SO 2, para ambos escenarios en estudio,

es posible mencionar que, gracias a la implementación de medidas de control de emisión

de polvo adicionales, particularmente las mejoras en la supresión de polvo en caminos no

pavimentados y el aspirado de ciertas calles pavimentadas, la fase de operación proyectada

del Proyecto presenta un mínimo aumento de las concentraciones de material particulado

en sus distintas fracciones en los receptores de interés estudiados. No obstante, se aprecia

una leve disminución de los aportes de material particulado respirable en ciertos

receptores.

Así, el incremento de las concentraciones de MP2.5 representa hasta un 4,0% y 1,8% de la

normativa asociada a este contaminante para periodo diario y anual respectivamente, lo

cual se percibe particularmente en el receptor denominado “R_18”, correspondiente a una

vivienda de material mixto.

Por su parte, los receptores denominados “R_3”, “R_4”, “R_8”, “R_12”, “R_13”, “R_14”,

“R_17”, “R_20” y “R_23”, correspondientes a estaciones de monitoreo, oficinas, sectores

de trabajo y viviendas habitacionales, presentan un aumento en los aportes de MP10 en

periodo diario durante el escenario proyectado del Proyecto, incrementando las

concentraciones en hasta 0,24 [μg/m [3] N]; mientras que los receptores denominados “R_1”,

“R_2”, “R_7”, “R_15”, “R_16” y “R_18”, correspondientes a estaciones de monitoreo,

sectores de trabajo y viviendas habitacionales, presentan un aumento en los aportes de

www.dfmconsultores.cl

217

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

este contaminante en periodo diario y anual, incrementando las concentraciones en hasta

2,92 y 0,27 [μg/m [3] N] en periodo diario y anual respectivamente.

En cuanto a las depositaciones de MPS, estas incrementan levemente en gran parte de los

receptores estudiados, alcanzando un máximo de 0,4% y 0,3% de las normativas de

referencia para periodo anual y mensual, correspondientes a la Confederación Suiza y

respectivamente.

Por su parte, en cuanto a la variación de las concentraciones de gases aportados por el

Proyecto durante el escenario actual y futuro sobre los distintos receptores, estas

representan un máximo de 0,1% de la norma de monóxido de carbono (CO) para periodo

horario y de ocho horas, 4,8% y 0,3% de la norma de dióxido de nitrógeno para periodo

horario y anual según orden de mención, y 0,0% de la norma de dióxido de azufre para

periodo horario, diario y anual. En consecuencia, es posible establecer que las

concentraciones de gases aportadas por el Proyecto son prácticamente mínimas y/o nulas.

Por otro lado, conforme a los criterios indicados en el documento “Criterio de evaluación

en el SEIA: Impacto de emisiones en zonas saturadas por material particulado respirable

MP10 y material particulado respirable fino MP2.5” (SEA, 2023) y en base a los Niveles de

Impacto Significativos establecidos por los Estándares Nacionales de Calidad del Aire,

específicamente en el documento “Evaluación Significancia del Impacto de las Emisiones de

un Proyecto o Actividad en Zonas Saturadas en el Marco del SEIA” (DICTUC, 2022), las áreas

de influencias para la componente calidad del aire determinadas para la fase de operación

actual y proyectada del Proyecto representan la combinación las curvas de límite de

significancia estadística para los aportes de material particulado respirable fino en periodo

diario y anual, material particulado respirable en periodo diario y anual, y dióxido de

nitrógeno en periodo diario y anual resultantes para cada escenario, concluyendo en un

rango geográfico similar, el cual comprende principalmente el sector de trabajo de SCM

Mina Carola Norte y SCM Mina Carola Centro, así como también aquellas rutas que

representan un mayor flujo vehicular durante el desarrollo del Proyecto.

En cambio, las curvas de isoconcentración de los contaminantes tales como monóxido de

carbono (CO) y dióxido de azufre (SO 2 ) presentan una magnitud máxima por bajo la curva

del límite de significancia estadístico establecido en el documento señalado anteriormente,

por lo que no han sido consideradas para la determinación del área de influencia de la

componente en estudio.

www.dfmconsultores.cl

218

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

En consecuencia, de acuerdo con los resultados de modelación de dispersión de

contaminantes obtenidos, y particularmente considerando los aportes de concentración de

material particulado respirable resultantes sobre los distintos receptores de interés

seleccionados para este estudio, es posible establecer que la proyección de la fase de

operación del Proyecto no genera un incremento significativo en los aportes de este

contaminante, pues en gran parte de los lugares geográficos de interés no se presenta

aporte de MP10 alguno.

Por último, considerando la situación de basal de calidad del aire en la zona y tras analizar

el efecto sinérgico generado por la ejecución simultanea de los proyectos “Optimización

Operacional Mina Carola” y “Optimización Operacional Planta Cerrillos” sobre los

receptores de interés, y particularmente sobre las estaciones de monitoreo disponibles, es

posible mencionar que la operación conjunta de ambos proyectos no genera un incremento

significativo de las concentraciones y depositaciones percibidas en las locaciones en donde

se ubican las estaciones monitoras.

www.dfmconsultores.cl

219

**info@dfmconsultores.cl**

Modelación de Dispersión de Contaminantes

**Proyecto “Optimización Operacional Mina Carola”**

Enero 2024

**ANEXO 1: ARCHIVOS DIGITALES MODELACIÓN**

En la siguiente tabla se detallan los archivos de entrada y salida de la modelación de calidad

del aire presentada en este estudio. Los archivos se listan según lo indicado en la “Guía para

el uso de modelos de calidad del aire en el SEIA”, considerando los archivos de entrada y

salida de los módulos CALMET, CALPUFF y CALPOST.

**Tabla 8-1. Archivos de modelación entregados.**

|Archivos|Entregado|Observación|
|---|---|---|
|**Archivos CALPUFF**|**Archivos CALPUFF**|**Archivos CALPUFF**|
|CALPUFF.DAT|NO|Corresponde al archivo CONC.DAT|
|CALPUFF.LST|SI|-|
|CALPUFF.INP|SI|-|
|CONC.DAT|SI|-|
|DFLX.DAT|SI|-|
|WFLX.DAT|NO|-|
|**Archivos Meteorológicos CALMET**|**Archivos Meteorológicos CALMET**|**Archivos Meteorológicos CALMET**|
|CALMET.DAT|SI|Corresponde al archivo:calmetv6_Tierra_Amarilla.dat|
|GEO.DAT|SI|-|
|SURF.DAT|NO|No fueron utilizados debido a que se usó, directamente<br>en CALPUFF, la meteorología proveniente del modelo<br>meteorológico WRF.|
|UP.DAT|NO|NO|
|CALMET.LST|NO|NO|
|CALMET.INP|NO|NO|
|namelist.wps|SI|Archivo de configuración de preproceso de WRF (WPS)|
|namelist.input|SI|Archivo de configuración de WRF|
|**Archivos CALPOST**|**Archivos CALPOST**|**Archivos CALPOST**|
|CALPOST.DAT|SI|Los archivos se presentan en forma separada según<br>contaminantes y periodo.|
|CALPOST.LST|SI|SI|
|CALPOST.INP|SI|SI|
|**Archivos Complementarios**|**Archivos Complementarios**|**Archivos Complementarios**|
|-Coastline Data File, Dry Flux Data File,<br>Wet Flux Data File, Ozone Data File,<br>Chem Data File.|NO|No se incluyen, debido a que corresponden a datos que no<br>fueron modelados.|

Fuente: Elaboración propia.

www.dfmconsultores.cl

220

**info@dfmconsultores.cl**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4-1.: Resumen Emisiones. Fase de Operación Base.****

| Actividad | Resumen de Emisiones [t] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **MP2.5** | **MP10** | **MP30** | **CO** | **NOX ** | **COV** | **SOx ** | **NH3 ** |
| Combustión Maquinaria | 1,270 | 1,270 | 1,270 | 16,871 | 19,809 | 2,012 | 0,051 | 0,013 |
| Combustión Transporte | 0,035 | 0,035 | 0,035 | 0,328 | 1,185 | 0,062 | 0,001 | 0,001 |
| Resuspensión Transporte | 0,605 | 5,154 | 17,128 |  |  |  |  |  |
| Movimientos de Material | 12,364 | 22,784 | 96,530 |  |  |  |  |  |
| **Total** | **14,274** | **29,242** | **114,962** | **17,199** | **20,994** | **2,074** | **0,052** | **0,014** |

**Tabla 4-2.: Resumen Emisiones. Fase de Operación Proyectada.****

| Actividad | Resumen de Emisiones [t] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Actividad** | **MP2.5** | **MP10** | **MP30** | **CO** | **NOX ** | **COV** | **SOx ** | **NH3 ** |
| Combustión Maquinaria | 1,397 | 1,397 | 1,397 | 18,558 | 21,790 | 2,213 | 0,056 | 0,015 |
| Combustión Transporte | 0,035 | 0,035 | 0,035 | 0,330 | 1,193 | 0,062 | 0,001 | 0,001 |
| Resuspensión Transporte | 0,294 | 2,149 | 7,770 |  |  |  |  |  |
| Movimientos de Material | 13,601 | 25,061 | 106,181 |  |  |  |  |  |
| **Total** | **15,327** | **28,642** | **115,383** | **18,888** | **22,983** | **2,275** | **0,057** | **0,015** |

**Tabla 5-1.: Configuración parámetros principales modelo meteorológico WRF.****

| Parámetro | Col2 | Valor |
| --- | --- | --- |
| Dominio | Resolución horizontal | 1 km |
| Dominio | Proyección | Lambert |
| Dominio | Dimensión | 76x76x44 |
| Dominio | Número de niveles verticales | 44 |
| Dominio | Niveles verticales (eta) | 0.000000, 0.051578, 0.101822, 0.150735, 0.198315,<br>0.244562, 0.289477, 0.333059, 0.375309, 0.416226,<br>0.455810, 0.494062, 0.530982, 0.566569, 0.600823,<br>0.633745, 0.665334, 0.695591, 0.724515, 0.752107,<br>0.778366, 0.803292, 0.826886, 0.849148, 0.870076,<br>0.889673, 0.907937, 0.923302, 0.937101, 0.949333,<br>0.960000, 0.969101, 0.976635, 0.982603, 0.987005,<br>0.989841, 0.991111, 0.992381, 0.993651, 0.994921,<br>0.996190, 0.997460, 0.998730, 1.000000, |

**Tabla 5-2.: Estadígrafos de y MP10. Periodo 2020- 2022. Estación Tierra Amarilla.****

| Estación | Año | Media anual MP10 [μg/m3N] |
| --- | --- | --- |
| Tierra Amarilla | 2020 | 52,3 |
| Tierra Amarilla | 2021 | 58,5 |
| Tierra Amarilla | 2022 | 56,8 |

**Tabla 5-3.: Caracterización Estación de Monitoreo Meteorológico.****

| Estación de<br>Monitoreo | Variables Meteorológicas<br>Registradas | Período de Datos<br>Disponibles | Coordenadas UTM (Datum<br>WGS84 19S) | Col5 |
| --- | --- | --- | --- | --- |
| **Estación de**<br>**Monitoreo** | **Variables Meteorológicas**<br>**Registradas** | **Período de Datos**<br>**Disponibles** | **Este [m]** | **Norte [m]** |
| Tierra Amarilla | ▪ <br>Dirección del Viento (°)<br>▪ <br>Velocidad del Viento (m/s)<br>▪ <br>Temperatura (°C)<br>▪ <br>Humedad Relativa (%)<br>▪ <br>Precipitación Acumulada (mm)<br>▪ <br>Radiación Solar (W/m2) <br>▪ <br>Presión Atmosférica (hPa) | Enero de 2021 a<br>diciembre de 2022 | 374.932 | 6.960.241 |

**Tabla 5-4.: Resumen de información Velocidad del Viento. Estación Tierra Amarilla.****

| Parámetro | Variable | Año | Col4 | Bienio |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2021** | **2022** | **2022** |
| Velocidad de Viento (m/s) | Promedio | 2,33 | 2,29 | 2,31 |
| Velocidad de Viento (m/s) | Máximo | 5,43 | 5,96 | 5,96 |
| Velocidad de Viento (m/s) | Mínimo | 0,03 | 0,00 | 0,00 |
| Porcentaje de Calmas (%) | Porcentaje de Calmas (%) | 4,44% | 5,04% | 4,74% |
| Datos Válidos (%) | Datos Válidos (%) | 99,59% | 97,84% | 98,72% |

**Tabla 5-5.: Frecuencia de distribución Velocidad y Dirección del Viento. Periodo enero 2021 a diciembre de 2022. Estación Tierra Amarilla.****

| Dirección | Col2 | Distribución Porcentual de Velocidad del Viento (m/s) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección** | **Dirección** | **0,50 - 2,10** | **2,10 - 3,60** | **3,60 - 5,70** | **5,70 - 8,80** | **8,80 - 11,10** | **>= 11,10** | **Total (%)** |
| 348,75 - 11,25 | N | 5,80% | 3,00% | 2,29% | 0,00% | 0,00% | 0,00% | 11,08% |
| 11,25 - 33,75 | NNE | 14,30% | 22,01% | 18,73% | 0,00% | 0,00% | 0,00% | 55,04% |
| 33,75 - 56,25 | NE | 2,82% | 1,13% | 0,84% | 0,01% | 0,00% | 0,00% | 4,81% |
| 56,25 - 78,75 | ENE | 1,04% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% | 1,05% |
| 78,75 - 101,25 | E | 0,49% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,49% |
| 101,25 - 123,75 | ESE | 0,34% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,34% |
| 123,75 - 146,25 | SE | 0,42% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,42% |
| 146,25 - 168,75 | SSE | 2,18% | 0,03% | 0,00% | 0,00% | 0,00% | 0,00% | 2,21% |
| 168,75 - 191,25 | S | 8,67% | 0,25% | 0,00% | 0,00% | 0,00% | 0,00% | 8,92% |
| 191,25 - 213,75 | SSW | 4,21% | 0,21% | 0,01% | 0,00% | 0,00% | 0,00% | 4,43% |
| 213,75 - 236,25 | SW | 0,95% | 0,05% | 0,00% | 0,00% | 0,00% | 0,00% | 1,00% |
| 236,25 - 258,75 | WSW | 0,63% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% | 0,64% |
| 258,75 - 281,25 | W | 0,60% | 0,08% | 0,00% | 0,00% | 0,00% | 0,00% | 0,68% |
| 281,25 - 303,75 | WNW | 0,62% | 0,15% | 0,00% | 0,00% | 0,00% | 0,00% | 0,76% |
| 303,75 - 326,25 | NW | 0,93% | 0,43% | 0,03% | 0,00% | 0,00% | 0,00% | 1,39% |
| 326,25 - 348,75 | NNW | 1,92% | 0,62% | 0,14% | 0,00% | 0,00% | 0,00% | 2,68% |
| Sub-Total | Sub-Total | 45,91% | 27,97% | 22,04% | 0,01% | 0,00% | 0,00% | 95,93% |
| Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | 4,07% |

**Tabla 5-6.: Resumen de información Temperatura. Estación Tierra Amarilla.****

| Parámetro | Variable | Año | Col4 | Bienio |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2021** | **2022** | **2022** |
| Temperatura (°C) | Promedio | 16,23 | 15,99 | 16,11 |
| Temperatura (°C) | Máximo | 34,70 | 33,30 | 34,70 |
| Temperatura (°C) | Mínimo | 1,74 | 2,08 | 1,74 |
| Datos Válidos (%) | Datos Válidos (%) | 99,61% | 97,84% | 98,73% |

**Tabla 5-7.: Resumen de información Humedad Relativa. Estación Tierra Amarilla.****

| Parámetro | Variable | Año | Col4 | Bienio |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2021** | **2022** | **2022** |
| Humedad Relativa (%) | Promedio | 55,16 | 63,02 | 59,09 |
| Humedad Relativa (%) | Máximo | 95,49 | 99,07 | 99,07 |
| Humedad Relativa (%) | Mínimo | 2,69 | 2,25 | 2,25 |
| Datos Válidos (%) | Datos Válidos (%) | 99,61% | 97,84% | 98,73% |

**Tabla 5-8.: Resumen de información Precipitaciones Acumuladas. Estación Tierra Amarilla.****

| Parámetro | Variable | Año | Col4 | Bienio |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2021** | **2022** | **2022** |
| Precipitación Diaria Acumulada (mm) | Máximo | 4,40 | 16,10 | 16,10 |
| Precipitación Mensual Acumulada (mm) | Máximo | 8,80 | 26,30 | 26,30 |
| Precipitación Anual Acumulada (mm) | Precipitación Anual Acumulada (mm) | 12,50 | 27,80 | 20,15 |
| Datos Válidos (%) | Datos Válidos (%) | 99,62% | 81,15% | 90,39% |

**Tabla 5-9.: Resumen de información Radiación Solar. Estación Tierra Amarilla.****

| Parámetro | Variable | Año | Col4 | Bienio |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2021** | **2022** | **2022** |
| Radiación Solar (W/m2) | Promedio | 200,92 | 217,34 | 209,13 |
| Radiación Solar (W/m2) | Máximo | 1.007,92 | 1.030,83 | 1.030,83 |
| Radiación Solar (W/m2) | Mínimo | 0,00 | 0,00 | 0,00 |
| Datos Válidos (%)<br> | Datos Válidos (%)<br> | 99,55%<br> | 97,04% | 98,30% |

**Tabla 5-10.: Resumen de Información Presión Atmosférica. Estación Tierra Amarilla.****

| Parámetro | Variable | Año | Col4 | Bienio |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Variable** | **2021** | **2022** | **2022** |
| Presión Atmosférica (hPa) | Promedio | 719,42 | 719,34 | 719,38 |
| Presión Atmosférica (hPa) | Máximo | 726,56 | 726,14 | 726,56 |
| Presión Atmosférica (hPa) | Mínimo | 714,53 | 714,54 | 714,53 |
| Datos Válidos (%) | Datos Válidos (%) | 99,60% | 97,85% | 98,73% |

**Tabla 5-11.: Resumen de información Velocidad del Viento Modelada. Estación Tierra Amarilla.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2021** |
| Velocidad de Viento (m/s) | Promedio | 3,40 |
| Velocidad de Viento (m/s) | Máximo | 11,30 |
| Velocidad de Viento (m/s) | Mínimo | 0,03 |
| Porcentaje de Calmas (%) | Porcentaje de Calmas (%) | 4,75 |
| Datos Válidos (%) | Datos Válidos (%) | 100,00% |

**Tabla 5-12.: Frecuencia de distribución Velocidad y Dirección del Viento Modelada. Enero a diciembre de 2021. Estación Tierra Amarilla.****

| Dirección | Col2 | Distribución Porcentual de Velocidad del Viento (m/s) | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Dirección** | **Dirección** | **0,50 - 2,10** | **2,10 - 3,60** | **3,60 - 5,70** | **5,70 - 8,80** | **8,80 - 11,10** | **>= 11,10** | **Total (%)** |
| 348,75 - 11,25 | N | 3,15% | 5,00% | 7,60% | 13,78% | 1,77% | 0,02% | 31,32% |
| 11,25 - 33,75 | NNE | 5,18% | 3,97% | 4,19% | 0,39% | 0,19% | 0,00% | 13,93% |
| 33,75 - 56,25 | NE | 1,77% | 0,47% | 0,07% | 0,00% | 0,00% | 0,00% | 2,31% |
| 56,25 - 78,75 | ENE | 0,37% | 0,01% | 0,00% | 0,00% | 0,00% | 0,00% | 0,38% |
| 78,75 - 101,25 | E | 0,21% | 0,01% | 0,02% | 0,00% | 0,00% | 0,00% | 0,24% |
| 101,25 - 123,75 | ESE | 0,24% | 0,00% | 0,00% | 0,00% | 0,00% | 0,00% | 0,24% |
| 123,75 - 146,25 | SE | 0,64% | 0,01% | 0,01% | 0,00% | 0,00% | 0,00% | 0,66% |
| 146,25 - 168,75 | SSE | 2,52% | 0,35% | 0,00% | 0,00% | 0,00% | 0,00% | 2,88% |
| 168,75 - 191,25 | S | 11,07% | 7,01% | 0,34% | 0,00% | 0,00% | 0,00% | 18,42% |
| 191,25 - 213,75 | SSO | 5,02% | 0,34% | 0,01% | 0,00% | 0,00% | 0,00% | 5,38% |
| 213,75 - 236,25 | SO | 1,39% | 0,02% | 0,03% | 0,06% | 0,00% | 0,00% | 1,51% |
| 236,25 - 258,75 | OSO | 0,51% | 0,02% | 0,25% | 0,16% | 0,01% | 0,00% | 0,96% |
| 258,75 - 281,25 | O | 0,43% | 0,10% | 3,33% | 0,70% | 0,00% | 0,00% | 4,57% |
| 281,25 - 303,75 | ONO | 0,32% | 0,22% | 6,02% | 0,63% | 0,01% | 0,00% | 7,19% |
| 303,75 - 326,25 | NO | 0,53% | 0,16% | 1,37% | 0,05% | 0,00% | 0,00% | 2,10% |
| 326,25 - 348,75 | NNO | 1,61% | 0,31% | 0,89% | 0,37% | 0,00% | 0,00% | 3,17% |
| Sub-Total | Sub-Total | 34,97% | 18,01% | 24,14% | 16,12% | 1,99% | 0,02% | 95,25% |
| Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | Calmas | 4,75% |

**Tabla 5-13.: Resumen de información Temperatura Modelada. Estación Tierra Amarilla.****

| Parámetro | Variable | Año |
| --- | --- | --- |
| **Parámetro** | **Variable** | **2021** |
| Temperatura (°C) | Promedio | 17,94 |
| Temperatura (°C) | Máximo | 33,97 |
| Temperatura (°C) | Mínimo | 4,31 |
| Datos Válidos (%) | Datos Válidos (%) | 100,00% |

**Tabla 5-15.: Comparación Registros de Velocidad del Viento y Temperatura Observadas y Modeladas.****

| Parámetro | Velocidad del Viento [m/s] | Col3 | Temperatura [°C] | Col5 |
| --- | --- | --- | --- | --- |
| **Parámetro** | **Observada** | **Modelada** | **Observada** | **Modelada** |
| Promedio | 2,33 | 3,40 | 16,23 | 17,94 |
| Máximo | 5,43 | 11,30 | 34,70 | 33,97 |
| Mínimo | 0,03 | 0,03 | 1,74 | 4,31 |
| Datos disponibles [%] | 99,59% | 100,00% | 99,61% | 100,00% |

**Tabla 5-16.: Estadígrafos de Dispersión de Velocidad del Viento y Temperatura. Estación Tierra Amarilla.****

| Medida de Error | Velocidad del Viento | Col3 | Temperatura | Col5 |
| --- | --- | --- | --- | --- |
| **Medida de Error** | **Serie de Tiempo** | **Ciclo Diario** | **Serie de Tiempo** | **Ciclo Diario** |
| BIAS | 1,064 | 1,089 | 1,695 | 1,830 |
| MAE | 1,427 | 1,093 | 2,512 | 1,830 |
| RMSE | 1,915 | 1,451 | 3,334 | 1,983 |
| r | 0,764 | 0,983 | 0,895 | 0,994 |

**Tabla 5-17.: Estadígrafos de Dispersión de Velocidad del Viento y Temperatura. Estación Tierra Amarilla.****

| Medida de Error | Velocidad del Viento | Col3 | Temperatura | Col5 |
| --- | --- | --- | --- | --- |
| **Medida de Error** | **WRF 2021** | **Guía 2023** | **WRF 2021** | **Guía 2023** |
| BIAS | 1,064 | [-2,5;2,5] | 1,695 | [-4;4] |
| MAE | 1,427 | ≤ 3 | 2,512 | ≤ 4 |
| RMSE | 1,915 | ≤ 3,5 | 3,334 | ≤ 4,5 |
| r | 0,764 | > 0,6 | 0,895 | > 0,8 |

**Tabla 5-18.: Normas de Calidad del Aire.****

| Contaminante | Decreto Aplicable | Norma | Col4 | Periodo de Evaluación de<br>Cumplimiento de Norma |
| --- | --- | --- | --- | --- |
| **Contaminante** | **Decreto Aplicable** | **Valor** | **Unidad** | **Unidad** |
| Material particulado<br>respirable fino (MP2.5) | Decreto Supremo<br>N°12/2011 | 50 | μg/m3 | Percentil 98 de la media aritmética<br>diaria durante un año. |
| Material particulado<br>respirable fino (MP2.5) | Decreto Supremo<br>N°12/2011 | 20 | 20 | Media aritmética trianual |
| Material particulado<br>respirable (MP10) | Decreto Supremo<br>N°12/2021 | 130 | μg/m3N | Percentil 98 de la media aritmética<br>diaria durante un año. |
| Material particulado<br>respirable (MP10) | Decreto Supremo<br>N°12/2021 | 50 | 50 | Media aritmética trianual. |
| Material particulado<br>sedimentable (MPS) | Norma de referencia<br>Confederación Suiza,<br>Recursos Naturales | 200 | mg/m2-día | Media aritmética anual |
| Material particulado<br>sedimentable (MPS) | República de Argentina | 333 | mg/m2-día | Media aritmética mensual |
| Dióxido de nitrógeno<br>(NO2) | Decreto Supremo<br>N°114/2002 | 400 | μg/m3N | Percentil 99 de la media aritmética<br>horaria durante un año. |
| Dióxido de nitrógeno<br>(NO2) | Decreto Supremo<br>N°114/2002 | 100 | 100 | Media aritmética trianual. |
| Dióxido de azufre (SO2) | Decreto Supremo<br>N°104/2019 | 350 | μg/m3N | Percentil 98,5 de las concentraciones<br>de 1 hora. |
| Dióxido de azufre (SO2) | Decreto Supremo<br>N°104/2019 | 150 | 150 | Percentil 99 de las concentraciones de<br>24 horas |

**Tabla 5-19.: Caracterización de Estación de Monitoreo de Calidad del Aire.****

| Estación de<br>Monitoreo | Coordenadas UTM<br>(Datum WGS84) | Col3 | Contaminantes medidos | Periodo de Datos<br>Disponibles |
| --- | --- | --- | --- | --- |
| **Estación de**<br>**Monitoreo** | **Este (m)** | **Norte (m)** | **Norte (m)** | **Norte (m)** |
| Tierra Amarilla | 374.932 | 6.960.241 | • Material particulado respirable (MP10)<br>• Material particulado respirable fino (MP2.5)<br>• Material particulado sedimentable (MPS) | Enero de 2020 a<br>diciembre de 2022 |
| Ojanco | 374.757 | 6.958.891 | • Material particulado respirable (MP10)<br>• Material particulado respirable fino (MP2.5) | Enero de 2020 a<br>diciembre de 2022 |
| Luis Uribe | 374.942 | 6.961.596 | • Material particulado respirable (MP10)<br>• Material particulado respirable fino (MP2.5) | Enero de 2020 a<br>diciembre de 2022 |
| Kozan | 375.065 | 6.956.287 | • Material particulado respirable (MP10) | Enero de 2020 a<br>diciembre de 2022 |
| COEMIN | 377.146 | 6.949.777 | • Material particulado respirable (MP10) | Enero de 2020 a<br>diciembre de 2022 |
| Nantoco | 374.903 | 6.952.384 | • Material particulado respirable (MP10) | Enero de 2020 a<br>octubre de 2022 |
| C5 | 375.723 | 6.949.811 | • Material particulado respirable (MP10) | Enero de 2020 a<br>octubre de 2022 |
| C6 | 375.453 | 6.950.426 | • Material particulado respirable (MP10) | Enero de 2020 a<br>octubre de 2022 |
| C8 | 375.345 | 6.950.895 | • Material particulado respirable (MP10) | Enero de 2020 a<br>octubre de 2022 |
| C2 | 377.121 | 6.946.865 | • Material particulado respirable (MP10) | Enero de 2020 a<br>octubre de 2022 |
| C1 | 377.154 | 6.947.080 | • Material particulado respirable (MP10) | Enero de 2020 a<br>octubre de 2022 |
| C3 | 376.995 | 6.946.944 | • Material particulado respirable (MP10) | Enero de 2020 a<br>octubre de 2022 |
| C7 | 375.348 | 6.950.777 | • Material particulado respirable (MP10) | Enero de 2020 a<br>octubre de 2022 |

**Tabla 5-20.: Resumen Línea de Base de Calidad del Aire.****

| Estación | Contaminante | MP10 | Col4 | MP2.5 | Col6 | MPS | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Estación** | **Estadígrafo** | **P98 24**<br>**horas** | **Media**<br>**anual** | **P98 24**<br>**horas** | **Media**<br>**anual** | **Media**<br>**mensual** | **Media**<br>**anual** |
| **Estación** | **Norma** | **130** | **50** | **50** | **20** | **333** | **200** |
| **Estación** | **Unidad** | **μg/m3N ** | **μg/m3N ** | **μg/m3 ** | **μg/m3 ** | **mg/m2día** | **mg/m2día** |
| Tierra Amarilla | Valor | 123,4 | 55,9 | 31,0 | 14,1 | 356,0 | 226,8 |
| Tierra Amarilla | % Norma | 94,9% | 111,8% | 62,0% | 70,5% | 106,9% | 113,4% |
| Ojanco | Valor | 72,0 | 46,0 | 15,0 | 9,6 |  |  |
| Ojanco | % Norma | 55,4% | 92,0% | 30,0% | 48,0% |  |  |
| Luis Uribe | Valor | 74,0 | 49,0 | 14,0 | 8,7 |  |  |
| Luis Uribe | % Norma | 56,9% | 98,0% | 28,0% | 43,5% |  |  |
| Kozan | Valor | 73,1 | 45,8 |  |  |  |  |
| Kozan | % Norma | 56,2% | 91,6% |  |  |  |  |
| COEMIN | Valor | 96,0 | 45,8 |  |  |  |  |
| COEMIN | % Norma | 73,8% | 91,6% |  |  |  |  |
| Nantoco | Valor | 103,0 | 64,5 |  |  |  |  |
| Nantoco | % Norma | 79,2% | 129,0% |  |  |  |  |
| C5 | Valor | 54,0 | 39,5 |  |  |  |  |
| C5 | % Norma | 41,5% | 79,0% |  |  |  |  |
| C6 | Valor | 62,0 | 50,8 |  |  |  |  |
| C6 | % Norma | 47,7% | 101,6% |  |  |  |  |
| C8 | Valor | 52,0 | 36,8 |  |  |  |  |
| C8 | % Norma | 40,0% | 73,6% |  |  |  |  |
| C2 | Valor | 59,0 | 53,8 |  |  |  |  |
| C2 | % Norma | 45,4% | 107,6% |  |  |  |  |
| C1 | Valor | 57,0 | 51,3 |  |  |  |  |
| C1 | % Norma | 43,8% | 102,6% |  |  |  |  |
| C3 | Valor | 61,0 | 53,2 |  |  |  |  |
| C3 | % Norma | 46,9% | 106,4% |  |  |  |  |
| C7 | Valor | 63,0 | 52,7 |  |  |  |  |
| C7 | % Norma | 48,5% | 105,4% |  |  |  |  |

**Tabla 5-21.: Análisis de otros proyectos dentro del dominio de modelación.****

| Nombre Proyecto | Titular | RCA | Expediente SEIA | Estado SNIFA | Observación | Fuente |
| --- | --- | --- | --- | --- | --- | --- |
| Proyecto Minero<br>Tránsito | Sociedad Punta<br>del Cobre S.A. | 20230300139/2023 | http://seia.sea.gob.cl/expedie<br>nte/ficha/fichaPrincipal.php?i<br>d_expediente=2152997536 | Sin Información | Presenta aportes<br>en las estaciones<br>Tierra Amarilla,<br>Ojanco, Luis Uribe<br>y Kozan | https://seia.sea.gob.cl/archivos/2<br>021/08/25/Anexo_2.2_Modelacio<br>n_de_Dispersion_de_Cont_Rev_0<br>.pdf |
| Ampliación Central<br>Desierto de Atacama | Copiapó Solar<br>SpA. | 20220300142/2022 | http://seia.sea.gob.cl/expedie<br>nte/ficha/fichaPrincipal.php?i<br>d_expediente=2151133877 | Sin información | Presenta aportes<br>en estación Tierra<br>Amarilla | https://seia.sea.gob.cl/archivos/2<br>021/03/16/1a9_PHC0025_Anexo_<br>1.7_Modelacion_de_calidad_del_<br>aire_Rev_0.pdf |
| Parque Fotovoltaico<br>Alianza | Parque Solar<br>Alianzas SpA. | 72/2021 | http://seia.sea.gob.cl/expedie<br>nte/ficha/fichaPrincipal.php?i<br>d_expediente=2146014549 | No iniciada la<br>fase de<br>construcción | No presenta<br>modelación de<br>dispersión de<br>contaminantes | https://infofirma.sea.gob.cl/Docu<br>mentosSEA/MostrarDocumento?<br>docId=79/2c/f1fa7f87577e24fe58<br>e9b89d7f6af7c3f97c |
| Transporte de<br>Sustancias Peligrosas | Daniel Ocaña<br>Medina | 176/2020 | https://seia.sea.gob.cl/expedi<br>ente/ficha/fichaPrincipal.php?<br>modo=ficha&id_expediente=2<br>145507755 | Sin información | No presenta<br>modelación de<br>dispersión de<br>contaminantes | https://seia.sea.gob.cl/archivos/2<br>020/01/20/87b_Capitulo_2_Descr<br>ipcion_del_Proyecto.pdf |
| Modificación de la LAT<br>del Proyecto Central<br>Desierto de Atacama | Copiapó Solar<br>SpA | 138/2020 | https://seia.sea.gob.cl/expedi<br>ente/ficha/fichaPrincipal.php?<br>modo=ficha&id_expediente=2<br>145240380 | Sin información | No presenta<br>modelación de<br>dispersión de<br>contaminantes | https://seia.sea.gob.cl/archivos/2<br>019/12/18/Anexo_4_-<br>_Emisiones_Atmosfericas_VERSIO<br>N_SEIA.pdf |
| Transporte terrestre<br>de sustancias<br>corrosivas | Transfahum SpA. | 175/2020 | https://seia.sea.gob.cl/expedi<br>ente/ficha/fichaPrincipal.php?<br>modo=ficha&id_expediente=2<br>144896397 | Sin información | No presenta<br>modelación de<br>dispersión de<br>contaminantes | https://infofirma.sea.gob.cl/Docu<br>mentosSEA/MostrarDocumento?<br>docId=58/88/7a73bb7446509347<br>aa8dd5ddcff815f19cc0 |
| Mejoramiento Planta<br>de Tratamiento de<br>Aguas Servidas<br>Localidad Los Loros | Ilustre<br>Municipalidad de<br>Tierra Amarilla | 79/2020 | https://seia.sea.gob.cl/expedi<br>ente/expedientesEvaluacion.p<br>hp?modo=ficha&id_expedient<br>e=2144135727 | Sin información | No presenta<br>aportes en las<br>estaciones<br>estudiadas | http://seia.sea.gob.cl/archivos/20<br>19/09/01/Anexo_Emisiones_Atm<br>osfericas_PTAS_Los_Loros_REV_0<br>.pdf |
| Continuidad<br>Operacional Mina<br>Mantos de Cobre | Sociedad Punta<br>del Cobre S.A. | 145/2021 | https://seia.sea.gob.cl/expedi<br>ente/ficha/fichaPrincipal.php?<br>modo=ficha&id_expediente=2<br>144075495 | No iniciada la<br>fase de<br>construcción | Presenta aportes<br>en las estaciones<br>Tierra Amarilla,<br>Ojanco y Luis Uribe | https://seia.sea.gob.cl/archivos/2<br>019/08/28/190_Cap_2_-<br>_Analisis_Art_11_Rev_1.pdf |

**Tabla 5-22.: Línea de Base de Calidad del Aire Proyectada.****

| Estación | Contaminante | MP10 | Col4 | MP2.5 | Col6 | MPS | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Estación** | **Estadígrafo** | **P98 24**<br>**horas** | **Media**<br>**anual** | **P98 24**<br>**horas** | **Media**<br>**anual** | **Media**<br>**mensual** | **Media**<br>**anual** |
| **Estación** | **Norma** | **130** | **50** | **50** | **20** | **333** | **200** |
| **Estación** | **Unidad** | **μg/m3N ** | **μg/m3N ** | **μg/m3 ** | **μg/m3 ** | **mg/m2día** | **mg/m2día** |
| Tierra Amarilla | Valor | 125,4 | 56,4 | 31,4 | 14,2 | 356,0 | 226,8 |
| Tierra Amarilla | % Norma | 96,5% | 112,7% | 62,8% | 70,9% | 106,9% | 113,4% |
| Ojanco | Valor | 72,1 | 46,0 | 15,0 | 9,6 |  |  |
| Ojanco | % Norma | 55,5% | 92,0% | 30,0% | 48,0% |  |  |
| Luis Uribe | Valor | 74,2 | 49,1 | 14,0 | 8,7 |  |  |
| Luis Uribe | % Norma | 57,1% | 98,2% | 28,0% | 43,5% |  |  |
| Kozan | Valor | 73,1 | 45,8 |  |  |  |  |
| Kozan | % Norma | 56,2% | 91,6% |  |  |  |  |

**Tabla 5-23.: Características de Fuentes Emisoras y Tasas de Emisión. Fase de Operación Base.****

| ID | Descripción | Tipo de fuente | Tasas de emisión | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **Descripción** | **Tipo de fuente** | **MP2.5** | **MP10** | **MPS** | **NO** | **NO2 ** | **SO2 ** | **CO** | **Unidad** |
| SRC_1 | Tramo C1 | Camino | 2,78 E-07 | 9,83 E-07 | 4,90 E-06 | 1,23 E-06 | 2,10 E-07 | 2,29 E-09 | 5,46 E-07 | g/s/m |
| SRC_2 | Tramo C2 | Camino | 1,40 E-06 | 5,60 E-06 | 2,89 E-05 | 1,71 E-06 | 2,92 E-07 | 3,06 E-09 | 7,28 E-07 | g/s/m |
| SRC_3 | Tramo C3 | Camino | 1,15 E-06 | 4,63 E-06 | 2,39 E-05 | 1,20 E-06 | 2,05 E-07 | 2,07 E-09 | 4,93 E-07 | g/s/m |
| SRC_4 | Tramo C4 | Camino | 8,87 E-08 | 3,12 E-07 | 1,56 E-06 | 3,13 E-07 | 5,34 E-08 | 6,53 E-10 | 1,53 E-07 | g/s/m |
| SRC_5 | Tramo C5 | Camino | 1,33 E-06 | 5,32 E-06 | 2,75 E-05 | 1,59 E-06 | 2,71 E-07 | 2,80 E-09 | 6,69 E-07 | g/s/m |
| SRC_6 | Tramo C6 | Camino | 2,13 E-06 | 8,69 E-06 | 4,51 E-05 | 1,06 E-06 | 1,81 E-07 | 1,82 E-09 | 4,35 E-07 | g/s/m |
| SRC_7 | Tramo C7 | Camino | 8,09 E-07 | 3,27 E-06 | 1,69 E-05 | 7,18 E-07 | 1,22 E-07 | 1,24 E-09 | 2,95 E-07 | g/s/m |
| SRC_8 | Tramo C9 | Camino | 8,31 E-07 | 3,35 E-06 | 1,74 E-05 | 7,42 E-07 | 1,26 E-07 | 1,28 E-09 | 3,05 E-07 | g/s/m |
| SRC_9 | Tramo C10 | Camino | 8,77 E-07 | 3,54 E-06 | 1,83 E-05 | 8,06 E-07 | 1,37 E-07 | 1,39 E-09 | 3,30 E-07 | g/s/m |
| SRC_10 | Tramo C11 | Camino | 5,30 E-08 | 2,10 E-07 | 1,08 E-06 | 8,42 E-08 | 1,44 E-08 | 1,44 E-10 | 3,42 E-08 | g/s/m |
| SRC_11 | Tramo C12 | Camino | 6,46 E-07 | 2,53 E-06 | 1,30 E-05 | 1,10 E-06 | 1,87 E-07 | 2,01 E-09 | 4,77 E-07 | g/s/m |
| SRC_12 | Tramo N1 | Camino | 6,62 E-07 | 6,43 E-06 | 2,61 E-05 | 4,62 E-07 | 7,87 E-08 | 8,79 E-10 | 2,13 E-07 | g/s/m |
| SRC_13 | Tramo N2 | Camino | 6,02 E-07 | 5,84 E-06 | 2,37 E-05 | 4,20 E-07 | 7,15 E-08 | 7,99 E-10 | 1,94 E-07 | g/s/m |
| SRC_14 | Tramo N3 | Camino | 2,80 E-07 | 2,68 E-06 | 1,09 E-05 | 2,94 E-07 | 5,01 E-08 | 5,36 E-10 | 1,34 E-07 | g/s/m |
| SRC_15 | Tramo N4 | Camino | 1,15 E-06 | 1,14 E-05 | 4,63 E-05 | 4,63 E-07 | 7,88 E-08 | 7,96 E-10 | 1,90 E-07 | g/s/m |
| SRC_16 | Tramo N5 | Camino | 1,02 E-06 | 1,00 E-05 | 4,08 E-05 | 4,07 E-07 | 6,94 E-08 | 7,00 E-10 | 1,67 E-07 | g/s/m |
| SRC_17 | Tramo S1 | Camino | 2,93 E-06 | 2,92 E-05 | 8,45 E-05 | 2,12 E-07 | 3,61 E-08 | 5,78 E-10 | 1,22 E-07 | g/s/m |
| SRC_18 | Tramo S2 | Camino | 3,11 E-06 | 3,10 E-05 | 8,96 E-05 | 2,25 E-07 | 3,83 E-08 | 6,13 E-10 | 1,30 E-07 | g/s/m |
| SRC_19 | Tramo S3 | Camino | 7,72 E-06 | 7,69 E-05 | 2,23 E-04 | 7,00 E-07 | 1,19 E-07 | 1,20 E-09 | 2,88 E-07 | g/s/m |
| SRC_20 | Tramo S4 | Camino | 2,14 E-05 | 2,14 E-04 | 6,18 E-04 | 1,43 E-06 | 2,43 E-07 | 2,87 E-09 | 6,55 E-07 | g/s/m |
| SRC_21 | Tramo P1 | Camino | 2,48 E-08 | 9,32 E-08 | 4,73 E-07 | 8,55 E-08 | 1,46 E-08 | 1,47 E-10 | 3,51 E-08 | g/s/m |
| SRC_22 | Tramo P2 | Camino | 2,77 E-08 | 1,04 E-07 | 5,28 E-07 | 9,55 E-08 | 1,63 E-08 | 1,64 E-10 | 3,92 E-08 | g/s/m |
| SRC_23 | Tramo P3 | Camino | 2,08 E-07 | 7,12 E-07 | 3,51 E-06 | 9,01 E-07 | 1,54 E-07 | 1,88 E-09 | 4,34 E-07 | g/s/m |
| SRC_24 | Tramo P4 | Camino | 2,07 E-07 | 7,08 E-07 | 3,49 E-06 | 8,96 E-07 | 1,53 E-07 | 1,87 E-09 | 4,32 E-07 | g/s/m |
| SRC_25 | Tramo P5 | Camino | 1,80 E-07 | 6,06 E-07 | 2,97 E-06 | 8,02 E-07 | 1,37 E-07 | 1,71 E-09 | 3,93 E-07 | g/s/m |

**Tabla 5-24.: Receptores de Interés. Fase de Operación Base.****

| ID | Receptor | Coordenadas [Datum WGS84] | Col4 | Elevación<br>[m.s.n.m.] |
| --- | --- | --- | --- | --- |
| **ID** | **Receptor** | **Este (m)** | **Norte (m)** | **Norte (m)** |
| R_1 | Estación Luis Uribe | 374.942 | 6.961.596 | 514,30 |
| R_2 | Estación Tierra Amarilla | 374.904 | 6.960.235 | 521,39 |
| R_3 | Estación Ojanco | 374.772 | 6.958.885 | 513,93 |
| R_4 | Estación Kozan | 375.076 | 6.956.263 | 568,74 |
| R_5 | 133 casa (Carola Norte) | 375.842 | 6.961.206 | 561,91 |
| R_6 | Iglesia Tierra Amarilla | 375.270 | 6.961.216 | 518,20 |
| R_7 | El Minero | 375.114 | 6.958.078 | 540,49 |
| R_8 | Testigoteca | 375.054 | 6.957.920 | 541,09 |
| R_9 | Estadio | 375.353 | 6.956.715 | 573,60 |
| R_10 | Agrouva I | 375.347 | 6.956.543 | 567,13 |
| R_11 | Agrouva II | 375.370 | 6.956.345 | 551,88 |
| R_12 | Receptor ruido (viviendas 1 piso, material mixto) | 375.021 | 6.958.033 | 539,80 |
| R_13 | Receptor ruido (viviendas 1 piso, material ligero) | 375.005 | 6.957.965 | 540,10 |
| R_14 | Receptor ruido (viviendas 1 piso, material ligero) | 374.966 | 6.957.769 | 542,55 |
| R_15 | Receptor ruido (Oficinas, galpones y container, material<br>mixto) | 375.215 | 6.957.683 | 554,95 |
| R_16 | Receptor ruido (Vivienda 2 pisos, material ligero) | 375.126 | 6.957.573 | 558,76 |
| R_17 | Receptor ruido (Viviendas 1 y 2 pisos, material ligero) | 375.093 | 6.957.335 | 555,04 |

**Tabla 5-25.: Resultados del modelo de dispersión para MP2.5 [μg/m** **[3]** **]. Fase de Operación Base.****

| Receptor | Descripción | Material Particulado Respirable Fino (MP2.5) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [μg/m3] ** | **Concentración [μg/m3] ** | **Norma de Calidad**<br>**[μg/m3] ** | **Norma de Calidad**<br>**[μg/m3] ** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 0,785 | 0,378 | 50 | 20 | 1,6% | 1,9% |
| R_2 | Estación Tierra Amarilla | 1,334 | 0,655 | 0,655 | 0,655 | 2,7% | 3,3% |
| R_3 | Estación Ojanco | 1,159 | 0,438 | 0,438 | 0,438 | 2,3% | 2,2% |
| R_4 | Estación Kozan | 2,660 | 0,634 | 0,634 | 0,634 | 5,3% | 3,2% |
| R_5 | 133 casa (Carola Norte) | 0,679 | 0,309 | 0,309 | 0,309 | 1,4% | 1,5% |
| R_6 | Iglesia Tierra Amarilla | 1,031 | 0,518 | 0,518 | 0,518 | 2,1% | 2,6% |
| R_7 | El Minero | 3,801 | 1,127 | 1,127 | 1,127 | 7,6% | 5,6% |
| R_8 | Testigoteca | 2,329 | 0,632 | 0,632 | 0,632 | 4,7% | 3,2% |
| R_9 | Estadio | 7,671 | 2,135 | 2,135 | 2,135 | 15,3% | 10,7% |
| R_10 | Agrouva I | 4,637 | 1,357 | 1,357 | 1,357 | 9,3% | 6,8% |
| R_11 | Agrouva II | 1,711 | 0,722 | 0,722 | 0,722 | 3,4% | 3,6% |
| R_12 | Receptor ruido | 2,333 | 0,656 | 0,656 | 0,656 | 4,7% | 3,3% |
| R_13 | Receptor ruido | 2,146 | 0,566 | 0,566 | 0,566 | 4,3% | 2,8% |
| R_14 | Receptor ruido | 1,769 | 0,492 | 0,492 | 0,492 | 3,5% | 2,5% |
| R_15 | Receptor ruido | 4,868 | 1,516 | 1,516 | 1,516 | 9,7% | 7,6% |
| R_16 | Receptor ruido | 5,586 | 1,709 | 1,709 | 1,709 | 11,2% | 8,5% |
| R_17 | Receptor ruido | 3,362 | 0,989 | 0,989 | 0,989 | 6,7% | 4,9% |
| R_18 | Receptor ruido | 19,729 | 3,888 | 3,888 | 3,888 | 39,5% | 19,4% |
| R_19 | Receptor ruido | 9,288 | 2,345 | 2,345 | 2,345 | 18,6% | 11,7% |
| R_20 | Receptor ruido | 10,184 | 2,854 | 2,854 | 2,854 | 20,4% | 14,3% |
| R_21 | Receptor ruido | 8,725 | 2,602 | 2,602 | 2,602 | 17,5% | 13,0% |
| R_22 | Receptor ruido | 5,607 | 1,090 | 1,090 | 1,090 | 11,2% | 5,4% |
| R_23 | Receptor ruido | 0,264 | 0,068 | 0,068 | 0,068 | 0,5% | 0,3% |
| R_24 | Receptor ruido | 0,180 | 0,060 | 0,060 | 0,060 | 0,4% | 0,3% |
| R_25 | Receptor ruido | 0,101 | 0,039 | 0,039 | 0,039 | 0,2% | 0,2% |
| R_26 | Receptor ruido | 0,263 | 0,119 | 0,119 | 0,119 | 0,5% | 0,6% |
| R_27 | Estación COEMIN | 0,273 | 0,069 | 0,069 | 0,069 | 0,5% | 0,3% |
| R_28 | Estación Nantoco | 0,284 | 0,124 | 0,124 | 0,124 | 0,6% | 0,6% |

**Tabla 5-26.: Resultados del modelo de dispersión para MP10 [μg/m** **[3]** **N]. Fase de Operación Base.****

| Receptor | Descripción | Material Particulado Respirable (MP10) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración**<br>**[μg/m3N]** | **Concentración**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 1,486 | 0,726 | 130 | 50 | 1,1% | 1,5% |
| R_2 | Estación Tierra Amarilla | 2,453 | 1,231 | 1,231 | 1,231 | 1,9% | 2,5% |
| R_3 | Estación Ojanco | 2,162 | 0,849 | 0,849 | 0,849 | 1,7% | 1,7% |
| R_4 | Estación Kozan | 4,893 | 1,365 | 1,365 | 1,365 | 3,8% | 2,7% |
| R_5 | 133 casa (Carola Norte) | 1,798 | 0,943 | 0,943 | 0,943 | 1,4% | 1,9% |
| R_6 | Iglesia Tierra Amarilla | 2,061 | 1,044 | 1,044 | 1,044 | 1,6% | 2,1% |
| R_7 | El Minero | 6,692 | 2,140 | 2,140 | 2,140 | 5,1% | 4,3% |
| R_8 | Testigoteca | 4,241 | 1,259 | 1,259 | 1,259 | 3,3% | 2,5% |
| R_9 | Estadio | 16,952 | 5,678 | 5,678 | 5,678 | 13,0% | 11,4% |
| R_10 | Agrouva I | 9,619 | 3,405 | 3,405 | 3,405 | 7,4% | 6,8% |
| R_11 | Agrouva II | 3,315 | 1,483 | 1,483 | 1,483 | 2,6% | 3,0% |
| R_12 | Receptor ruido | 4,217 | 1,327 | 1,327 | 1,327 | 3,2% | 2,7% |
| R_13 | Receptor ruido | 3,895 | 1,139 | 1,139 | 1,139 | 3,0% | 2,3% |
| R_14 | Receptor ruido | 3,143 | 1,010 | 1,010 | 1,010 | 2,4% | 2,0% |
| R_15 | Receptor ruido | 8,705 | 2,915 | 2,915 | 2,915 | 6,7% | 5,8% |
| R_16 | Receptor ruido | 10,061 | 3,176 | 3,176 | 3,176 | 7,7% | 6,4% |
| R_17 | Receptor ruido | 6,276 | 1,941 | 1,941 | 1,941 | 4,8% | 3,9% |
| R_18 | Receptor ruido | 33,660 | 7,185 | 7,185 | 7,185 | 25,9% | 14,4% |
| R_19 | Receptor ruido | 21,222 | 7,049 | 7,049 | 7,049 | 16,3% | 14,1% |
| R_20 | Receptor ruido | 19,096 | 6,305 | 6,305 | 6,305 | 14,7% | 12,6% |
| R_21 | Receptor ruido | 17,324 | 6,435 | 6,435 | 6,435 | 13,3% | 12,9% |
| R_22 | Receptor ruido | 10,656 | 2,465 | 2,465 | 2,465 | 8,2% | 4,9% |
| R_23 | Receptor ruido | 0,482 | 0,138 | 0,138 | 0,138 | 0,4% | 0,3% |
| R_24 | Receptor ruido | 0,352 | 0,119 | 0,119 | 0,119 | 0,3% | 0,2% |
| R_25 | Receptor ruido | 0,200 | 0,077 | 0,077 | 0,077 | 0,2% | 0,2% |
| R_26 | Receptor ruido | 0,534 | 0,240 | 0,240 | 0,240 | 0,4% | 0,5% |
| R_27 | Estación COEMIN | 0,521 | 0,139 | 0,139 | 0,139 | 0,4% | 0,3% |
| R_28 | Estación Nantoco | 0,546 | 0,251 | 0,251 | 0,251 | 0,4% | 0,5% |

**Tabla 5-27.: Resultados del modelo de dispersión para MPS [mg/m** **[2∙]** **día]. Fase de Operación Base.****

| Receptor | Descripción | Material Particulado Sedimentable (MPS) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Tasa de depositación**<br>**[mg/m2∙día]** | **Tasa de depositación**<br>**[mg/m2∙día]** | **Norma de Calidad**<br>**[mg/m2∙día]** | **Norma de Calidad**<br>**[mg/m2∙día]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **Media**<br>**Anual** | **Máxima**<br>**Media**<br>**Mensual** | **Conf. Suiza** | **República**<br>**Argentina** | **Conf. Suiza** | **República**<br>**Argentina** |
| R_1 | Estación Luis Uribe | 0,993 | 1,724 | 200 | 333 | 0,5% | 0,5% |
| R_2 | Estación Tierra Amarilla | 1,724 | 2,922 | 2,922 | 2,922 | 0,9% | 0,9% |
| R_3 | Estación Ojanco | 0,810 | 1,082 | 1,082 | 1,082 | 0,4% | 0,3% |
| R_4 | Estación Kozan | 2,775 | 3,736 | 3,736 | 3,736 | 1,4% | 1,1% |
| R_5 | 133 casa (Carola Norte) | 2,745 | 3,276 | 3,276 | 3,276 | 1,4% | 1,0% |
| R_6 | Iglesia Tierra Amarilla | 1,592 | 2,710 | 2,710 | 2,710 | 0,8% | 0,8% |
| R_7 | El Minero | 4,582 | 6,989 | 6,989 | 6,989 | 2,3% | 2,1% |
| R_8 | Testigoteca | 2,370 | 3,725 | 3,725 | 3,725 | 1,2% | 1,1% |
| R_9 | Estadio | 16,080 | 17,118 | 17,118 | 17,118 | 8,0% | 5,1% |
| R_10 | Agrouva I | 8,955 | 9,736 | 9,736 | 9,736 | 4,5% | 2,9% |
| R_11 | Agrouva II | 3,983 | 5,061 | 5,061 | 5,061 | 2,0% | 1,5% |
| R_12 | Receptor ruido | 2,574 | 3,857 | 3,857 | 3,857 | 1,3% | 1,2% |
| R_13 | Receptor ruido | 2,016 | 3,115 | 3,115 | 3,115 | 1,0% | 0,9% |
| R_14 | Receptor ruido | 1,843 | 2,269 | 2,269 | 2,269 | 0,9% | 0,7% |
| R_15 | Receptor ruido | 7,913 | 11,687 | 11,687 | 11,687 | 4,0% | 3,5% |
| R_16 | Receptor ruido | 7,703 | 12,071 | 12,071 | 12,071 | 3,9% | 3,6% |
| R_17 | Receptor ruido | 4,238 | 5,971 | 5,971 | 5,971 | 2,1% | 1,8% |
| R_18 | Receptor ruido | 18,810 | 24,021 | 24,021 | 24,021 | 9,4% | 7,2% |
| R_19 | Receptor ruido | 21,840 | 23,558 | 23,558 | 23,558 | 10,9% | 7,1% |
| R_20 | Receptor ruido | 15,730 | 18,055 | 18,055 | 18,055 | 7,9% | 5,4% |
| R_21 | Receptor ruido | 15,554 | 18,007 | 18,007 | 18,007 | 7,8% | 5,4% |
| R_22 | Receptor ruido | 5,417 | 6,573 | 6,573 | 6,573 | 2,7% | 2,0% |
| R_23 | Receptor ruido | 0,177 | 0,237 | 0,237 | 0,237 | 0,1% | 0,1% |
| R_24 | Receptor ruido | 0,155 | 0,207 | 0,207 | 0,207 | 0,1% | 0,1% |
| R_25 | Receptor ruido | 0,094 | 0,151 | 0,151 | 0,151 | 0,0% | 0,0% |
| R_26 | Receptor ruido | 0,462 | 0,603 | 0,603 | 0,603 | 0,2% | 0,2% |
| R_27 | Estación COEMIN | 0,178 | 0,240 | 0,240 | 0,240 | 0,1% | 0,1% |

**Tabla 5-28.: Resultados del modelo de dispersión para CO [mg/m** **[3]** **N]. Fase de Operación Base.****

| Receptor | Descripción | Monóxido de Carbono (CO) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración**<br>**[mg/m3N]** | **Concentración**<br>**[mg/m3N]** | **Norma de Calidad**<br>**[mg/m3N]** | **Norma de Calidad**<br>**[mg/m3N]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P99 1 hora** | **P99 8**<br>**horas** | **P99 1 hora** | **P99 8**<br>**horas** | **P99 1 hora** | **P99 8**<br>**horas** |
| R_1 | Estación Luis Uribe | 0,005 | 0,002 | 30 | 10 | 0,0% | 0,0% |
| R_2 | Estación Tierra Amarilla | 0,009 | 0,003 | 0,003 | 0,003 | 0,0% | 0,0% |
| R_3 | Estación Ojanco | 0,014 | 0,003 | 0,003 | 0,003 | 0,0% | 0,0% |
| R_4 | Estación Kozan | 0,030 | 0,007 | 0,007 | 0,007 | 0,1% | 0,1% |
| R_5 | 133 casa (Carola Norte) | 0,005 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% |
| R_6 | Iglesia Tierra Amarilla | 0,006 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% |
| R_7 | El Minero | 0,065 | 0,010 | 0,010 | 0,010 | 0,2% | 0,1% |
| R_8 | Testigoteca | 0,050 | 0,008 | 0,008 | 0,008 | 0,2% | 0,1% |
| R_9 | Estadio | 0,132 | 0,024 | 0,024 | 0,024 | 0,4% | 0,2% |
| R_10 | Agrouva I | 0,073 | 0,013 | 0,013 | 0,013 | 0,2% | 0,1% |
| R_11 | Agrouva II | 0,018 | 0,004 | 0,004 | 0,004 | 0,1% | 0,0% |
| R_12 | Receptor ruido | 0,049 | 0,007 | 0,007 | 0,007 | 0,2% | 0,1% |
| R_13 | Receptor ruido | 0,046 | 0,007 | 0,007 | 0,007 | 0,2% | 0,1% |
| R_14 | Receptor ruido | 0,030 | 0,005 | 0,005 | 0,005 | 0,1% | 0,1% |
| R_15 | Receptor ruido | 0,078 | 0,014 | 0,014 | 0,014 | 0,3% | 0,1% |
| R_16 | Receptor ruido | 0,091 | 0,016 | 0,016 | 0,016 | 0,3% | 0,2% |
| R_17 | Receptor ruido | 0,057 | 0,010 | 0,010 | 0,010 | 0,2% | 0,1% |
| R_18 | Receptor ruido | 0,281 | 0,057 | 0,057 | 0,057 | 0,9% | 0,6% |
| R_19 | Receptor ruido | 0,137 | 0,027 | 0,027 | 0,027 | 0,5% | 0,3% |
| R_20 | Receptor ruido | 0,184 | 0,031 | 0,031 | 0,031 | 0,6% | 0,3% |
| R_21 | Receptor ruido | 0,152 | 0,027 | 0,027 | 0,027 | 0,5% | 0,3% |
| R_22 | Receptor ruido | 0,077 | 0,016 | 0,016 | 0,016 | 0,3% | 0,2% |
| R_23 | Receptor ruido | 0,003 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% |
| R_24 | Receptor ruido | 0,001 | 0,000 | 0,000 | 0,000 | 0,0% | 0,0% |
| R_25 | Receptor ruido | 0,001 | 0,000 | 0,000 | 0,000 | 0,0% | 0,0% |
| R_26 | Receptor ruido | 0,002 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% |
| R_27 | Estación COEMIN | 0,003 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% |
| R_28 | Estación Nantoco | 0,002 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% |

**Tabla 5-29.: Resultados del modelo de dispersión para NO** **2** **[μg/m** **[3]** **N]. Fase de Operación Base.****

| Receptor | Descripción | Dióxido de Nitrógeno (NO )<br>2 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración**<br>**[μg/m3N]** | **Concentración**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P99 1 hora** | **Período**<br>**Anual** | **P99 1 hora** | **Período**<br>**Anual** | **P99 1 hora** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 5,887 | 0,426 | 400 | 100 | 1,5% | 0,4% |
| R_2 | Estación Tierra Amarilla | 9,637 | 0,737 | 0,737 | 0,737 | 2,4% | 0,7% |
| R_3 | Estación Ojanco | 14,766 | 0,472 | 0,472 | 0,472 | 3,7% | 0,5% |
| R_4 | Estación Kozan | 27,530 | 0,619 | 0,619 | 0,619 | 6,9% | 0,6% |
| R_5 | 133 casa (Carola Norte) | 4,333 | 0,297 | 0,297 | 0,297 | 1,1% | 0,3% |
| R_6 | Iglesia Tierra Amarilla | 5,654 | 0,569 | 0,569 | 0,569 | 1,4% | 0,6% |
| R_7 | El Minero | 46,539 | 0,855 | 0,855 | 0,855 | 11,6% | 0,9% |
| R_8 | Testigoteca | 34,687 | 0,471 | 0,471 | 0,471 | 8,7% | 0,5% |
| R_9 | Estadio | 95,304 | 1,688 | 1,688 | 1,688 | 23,8% | 1,7% |
| R_10 | Agrouva I | 56,130 | 1,191 | 1,191 | 1,191 | 14,0% | 1,2% |
| R_11 | Agrouva II | 19,391 | 0,746 | 0,746 | 0,746 | 4,8% | 0,7% |
| R_12 | Receptor ruido | 38,283 | 0,524 | 0,524 | 0,524 | 9,6% | 0,5% |
| R_13 | Receptor ruido | 35,404 | 0,445 | 0,445 | 0,445 | 8,9% | 0,4% |
| R_14 | Receptor ruido | 20,175 | 0,372 | 0,372 | 0,372 | 5,0% | 0,4% |
| R_15 | Receptor ruido | 39,438 | 0,849 | 0,849 | 0,849 | 9,9% | 0,8% |
| R_16 | Receptor ruido | 53,136 | 1,007 | 1,007 | 1,007 | 13,3% | 1,0% |
| R_17 | Receptor ruido | 38,518 | 0,676 | 0,676 | 0,676 | 9,6% | 0,7% |
| R_18 | Receptor ruido | 200,690 | 2,672 | 2,672 | 2,672 | 50,2% | 2,7% |
| R_19 | Receptor ruido | 110,130 | 1,733 | 1,733 | 1,733 | 27,5% | 1,7% |
| R_20 | Receptor ruido | 127,960 | 2,239 | 2,239 | 2,239 | 32,0% | 2,2% |
| R_21 | Receptor ruido | 107,940 | 2,017 | 2,017 | 2,017 | 27,0% | 2,0% |
| R_22 | Receptor ruido | 60,019 | 0,959 | 0,959 | 0,959 | 15,0% | 1,0% |
| R_23 | Receptor ruido | 1,876 | 0,061 | 0,061 | 0,061 | 0,5% | 0,1% |
| R_24 | Receptor ruido | 1,206 | 0,054 | 0,054 | 0,054 | 0,3% | 0,1% |
| R_25 | Receptor ruido | 0,488 | 0,035 | 0,035 | 0,035 | 0,1% | 0,0% |
| R_26 | Receptor ruido | 2,327 | 0,122 | 0,122 | 0,122 | 0,6% | 0,1% |
| R_27 | Estación COEMIN | 1,967 | 0,061 | 0,061 | 0,061 | 0,5% | 0,1% |
| R_28 | Estación Nantoco | 1,805 | 0,120 | 0,120 | 0,120 | 0,5% | 0,1% |
| R_29 | Estación C6 | 1,452 | 0,078 | 0,078 | 0,078 | 0,4% | 0,1% |

**Tabla 5-30.: Resultados del modelo de dispersión para SO** **2** **[μg/m** **[3]** **N]. Fase de Operación Base.****

| Receptor | Descripción | Dióxido de Azufre (SO )<br>2 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Norma de Calidad [μg/m3N]** | **Norma de Calidad [μg/m3N]** | **Norma de Calidad [μg/m3N]** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **P99 1 hora** | **P99 24**<br>**horas** | **Período**<br>**Anual** | **P99 1 hora** | **P99 24**<br>**horas** | **Período**<br>**Anual** | **P99 1 hora** | **P99 24**<br>**horas** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 0,008 | 0,003 | 0,001 | 350 | 150 | 60 | 0,0% | 0,0% | 0,0% |
| R_2 | Estación Tierra Amarilla | 0,014 | 0,004 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_3 | Estación Ojanco | 0,018 | 0,004 | 0,001 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% | 0,0% |
| R_4 | Estación Kozan | 0,022 | 0,010 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_5 | 133 casa (Carola Norte) | 0,007 | 0,002 | 0,001 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% | 0,0% |
| R_6 | Iglesia Tierra Amarilla | 0,010 | 0,003 | 0,001 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% | 0,0% |
| R_7 | El Minero | 0,057 | 0,012 | 0,003 | 0,003 | 0,003 | 0,003 | 0,0% | 0,0% | 0,0% |
| R_8 | Testigoteca | 0,035 | 0,010 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_9 | Estadio | 0,087 | 0,033 | 0,005 | 0,005 | 0,005 | 0,005 | 0,0% | 0,0% | 0,0% |
| R_10 | Agrouva I | 0,046 | 0,018 | 0,004 | 0,004 | 0,004 | 0,004 | 0,0% | 0,0% | 0,0% |
| R_11 | Agrouva II | 0,020 | 0,005 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_12 | Receptor ruido | 0,036 | 0,010 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_13 | Receptor ruido | 0,029 | 0,009 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_14 | Receptor ruido | 0,027 | 0,007 | 0,001 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% | 0,0% |
| R_15 | Receptor ruido | 0,096 | 0,016 | 0,004 | 0,004 | 0,004 | 0,004 | 0,0% | 0,0% | 0,0% |
| R_16 | Receptor ruido | 0,115 | 0,018 | 0,005 | 0,005 | 0,005 | 0,005 | 0,0% | 0,0% | 0,0% |
| R_17 | Receptor ruido | 0,062 | 0,014 | 0,003 | 0,003 | 0,003 | 0,003 | 0,0% | 0,0% | 0,0% |
| R_18 | Receptor ruido | 0,245 | 0,061 | 0,011 | 0,011 | 0,011 | 0,011 | 0,1% | 0,0% | 0,0% |

**Tabla 5-31.: Características de Fuentes Emisoras y Tasas de Emisión. Fase de Operación Proyectada.****

| ID | Descripción | Tipo de fuente | Tasas de emisión | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **Descripción** | **Tipo de fuente** | **MP2.5** | **MP10** | **MPS** | **NO** | **NO2 ** | **SO2 ** | **CO** | **Unidad** |
| SRC_1 | Tramo C1 | Camino | 1,88 E-07 | 6,11 E-07 | 2,96 E-06 | 1,23 E-06 | 2,10 E-07 | 2,29 E-09 | 5,46 E-07 | g/s/m |
| SRC_2 | Tramo C2 | Camino | 9,22 E-07 | 3,60 E-06 | 1,84 E-05 | 1,79 E-06 | 3,05 E-07 | 3,20 E-09 | 7,60 E-07 | g/s/m |
| SRC_3 | Tramo C3 | Camino | 7,56 E-07 | 2,99 E-06 | 1,54 E-05 | 1,27 E-06 | 2,17 E-07 | 2,19 E-09 | 5,22 E-07 | g/s/m |
| SRC_4 | Tramo C4 | Camino | 6,01 E-08 | 1,94 E-07 | 9,40 E-07 | 3,13 E-07 | 5,34 E-08 | 6,53 E-10 | 1,53 E-07 | g/s/m |
| SRC_5 | Tramo C5 | Camino | 1,42 E-06 | 5,68 E-06 | 2,93 E-05 | 1,67 E-06 | 2,85 E-07 | 2,93 E-09 | 7,02 E-07 | g/s/m |
| SRC_6 | Tramo C6 | Camino | 2,32 E-06 | 9,45 E-06 | 4,91 E-05 | 1,13 E-06 | 1,92 E-07 | 1,94 E-09 | 4,64 E-07 | g/s/m |
| SRC_7 | Tramo C7 | Camino | 8,90 E-07 | 3,59 E-06 | 1,86 E-05 | 7,90 E-07 | 1,35 E-07 | 1,36 E-09 | 3,24 E-07 | g/s/m |
| SRC_8 | Tramo C9 | Camino | 7,50 E-07 | 3,01 E-06 | 1,56 E-05 | 8,15 E-07 | 1,39 E-07 | 1,40 E-09 | 3,35 E-07 | g/s/m |
| SRC_9 | Tramo C10 | Camino | 5,89 E-07 | 2,34 E-06 | 1,21 E-05 | 8,80 E-07 | 1,50 E-07 | 1,51 E-09 | 3,61 E-07 | g/s/m |
| SRC_10 | Tramo C11 | Camino | 3,30 E-08 | 1,27 E-07 | 6,49 E-07 | 8,42 E-08 | 1,44 E-08 | 1,44 E-10 | 3,42 E-08 | g/s/m |
| SRC_11 | Tramo C12 | Camino | 4,05 E-07 | 1,54 E-06 | 7,81 E-06 | 1,10 E-06 | 1,87 E-07 | 2,01 E-09 | 4,77 E-07 | g/s/m |
| SRC_12 | Tramo N1 | Camino | 2,35 E-07 | 2,16 E-06 | 8,71 E-06 | 4,62 E-07 | 7,87 E-08 | 8,79 E-10 | 2,13 E-07 | g/s/m |
| SRC_13 | Tramo N2 | Camino | 2,14 E-07 | 1,96 E-06 | 7,92 E-06 | 4,20 E-07 | 7,15 E-08 | 7,99 E-10 | 1,94 E-07 | g/s/m |
| SRC_14 | Tramo N3 | Camino | 1,02 E-07 | 9,02 E-07 | 3,63 E-06 | 2,94 E-07 | 5,01 E-08 | 5,36 E-10 | 1,34 E-07 | g/s/m |
| SRC_15 | Tramo N4 | Camino | 4,34 E-07 | 4,18 E-06 | 1,69 E-05 | 5,08 E-07 | 8,66 E-08 | 8,74 E-10 | 2,09 E-07 | g/s/m |
| SRC_16 | Tramo N5 | Camino | 3,83 E-07 | 3,69 E-06 | 1,50 E-05 | 4,47 E-07 | 7,62 E-08 | 7,69 E-10 | 1,84 E-07 | g/s/m |
| SRC_17 | Tramo S1 | Camino | 9,89 E-07 | 9,75 E-06 | 2,82 E-05 | 2,12 E-07 | 3,61 E-08 | 5,78 E-10 | 1,22 E-07 | g/s/m |
| SRC_18 | Tramo S2 | Camino | 1,05 E-06 | 1,03 E-05 | 2,99 E-05 | 2,25 E-07 | 3,83 E-08 | 6,13 E-10 | 1,30 E-07 | g/s/m |
| SRC_19 | Tramo S3 | Camino | 2,82 E-06 | 2,80 E-05 | 8,09 E-05 | 7,61 E-07 | 1,30 E-07 | 1,31 E-09 | 3,12 E-07 | g/s/m |
| SRC_20 | Tramo S4 | Camino | 7,68 E-06 | 7,62 E-05 | 2,20 E-04 | 1,55 E-06 | 2,64 E-07 | 3,08 E-09 | 7,04 E-07 | g/s/m |
| SRC_21 | Tramo P1 | Camino | 2,48 E-08 | 9,32 E-08 | 4,73 E-07 | 8,55 E-08 | 1,46 E-08 | 1,47 E-10 | 3,51 E-08 | g/s/m |
| SRC_22 | Tramo P2 | Camino | 2,77 E-08 | 1,04 E-07 | 5,28 E-07 | 9,55 E-08 | 1,63 E-08 | 1,64 E-10 | 3,92 E-08 | g/s/m |
| SRC_23 | Tramo P3 | Camino | 2,08 E-07 | 7,12 E-07 | 3,51 E-06 | 9,01 E-07 | 1,54 E-07 | 1,88 E-09 | 4,34 E-07 | g/s/m |
| SRC_24 | Tramo P4 | Camino | 2,07 E-07 | 7,08 E-07 | 3,49 E-06 | 8,96 E-07 | 1,53 E-07 | 1,87 E-09 | 4,32 E-07 | g/s/m |
| SRC_25 | Tramo P5 | Camino | 1,80 E-07 | 6,06 E-07 | 2,97 E-06 | 8,02 E-07 | 1,37 E-07 | 1,71 E-09 | 3,93 E-07 | g/s/m |

**Tabla 5-32.: Receptores de Interés. Fase de Operación Proyectada.****

| ID | Receptor | Coordenadas [Datum WGS84] | Col4 | Elevación<br>[m.s.n.m.] |
| --- | --- | --- | --- | --- |
| **ID** | **Receptor** | **Este (m)** | **Norte (m)** | **Norte (m)** |
| R_1 | Estación Luis Uribe | 374.942 | 6.961.596 | 514,30 |
| R_2 | Estación Tierra Amarilla | 374.904 | 6.960.235 | 521,39 |
| R_3 | Estación Ojanco | 374.772 | 6.958.885 | 513,93 |
| R_4 | Estación Kozan | 375.076 | 6.956.263 | 568,74 |
| R_5 | 133 casa (Carola Norte) | 375.842 | 6.961.206 | 561,91 |
| R_6 | Iglesia Tierra Amarilla | 375.270 | 6.961.216 | 518,20 |
| R_7 | El Minero | 375.114 | 6.958.078 | 540,49 |
| R_8 | Testigoteca | 375.054 | 6.957.920 | 541,09 |
| R_9 | Estadio | 375.353 | 6.956.715 | 573,60 |
| R_10 | Agrouva I | 375.347 | 6.956.543 | 567,13 |
| R_11 | Agrouva II | 375.370 | 6.956.345 | 551,88 |
| R_12 | Receptor ruido (viviendas 1 piso, material mixto) | 375.021 | 6.958.033 | 539,80 |
| R_13 | Receptor ruido (viviendas 1 piso, material ligero) | 375.005 | 6.957.965 | 540,10 |
| R_14 | Receptor ruido (viviendas 1 piso, material ligero) | 374.966 | 6.957.769 | 542,55 |
| R_15 | Receptor ruido (Oficinas, galpones y container, material<br>mixto) | 375.215 | 6.957.683 | 554,95 |
| R_16 | Receptor ruido (Vivienda 2 pisos, material ligero) | 375.126 | 6.957.573 | 558,76 |
| R_17 | Receptor ruido (Viviendas 1 y 2 pisos, material ligero) | 375.093 | 6.957.335 | 555,04 |

**Tabla 5-33.: Resultados del modelo de dispersión para MP2.5 [μg/m** **[3]** **]. Fase de Operación Proyectada.****

| Receptor | Descripción | Material Particulado Respirable Fino (MP2.5) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [μg/m3] ** | **Concentración [μg/m3] ** | **Norma de Calidad**<br>**[μg/m3] ** | **Norma de Calidad**<br>**[μg/m3] ** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 0,851 | 0,409 | 50 | 20 | 1,7% | 2,0% |
| R_2 | Estación Tierra Amarilla | 1,456 | 0,711 | 0,711 | 0,711 | 2,9% | 3,6% |
| R_3 | Estación Ojanco | 1,269 | 0,473 | 0,473 | 0,473 | 2,5% | 2,4% |
| R_4 | Estación Kozan | 2,922 | 0,673 | 0,673 | 0,673 | 5,8% | 3,4% |
| R_5 | 133 casa (Carola Norte) | 0,730 | 0,302 | 0,302 | 0,302 | 1,5% | 1,5% |
| R_6 | Iglesia Tierra Amarilla | 1,106 | 0,557 | 0,557 | 0,557 | 2,2% | 2,8% |
| R_7 | El Minero | 4,164 | 1,219 | 1,219 | 1,219 | 8,3% | 6,1% |
| R_8 | Testigoteca | 2,545 | 0,679 | 0,679 | 0,679 | 5,1% | 3,4% |
| R_9 | Estadio | 8,225 | 2,169 | 2,169 | 2,169 | 16,4% | 10,8% |
| R_10 | Agrouva I | 4,954 | 1,398 | 1,398 | 1,398 | 9,9% | 7,0% |
| R_11 | Agrouva II | 1,826 | 0,773 | 0,773 | 0,773 | 3,7% | 3,9% |
| R_12 | Receptor ruido | 2,545 | 0,698 | 0,698 | 0,698 | 5,1% | 3,5% |
| R_13 | Receptor ruido | 2,336 | 0,606 | 0,606 | 0,606 | 4,7% | 3,0% |
| R_14 | Receptor ruido | 1,938 | 0,524 | 0,524 | 0,524 | 3,9% | 2,6% |
| R_15 | Receptor ruido | 5,332 | 1,638 | 1,638 | 1,638 | 10,7% | 8,2% |
| R_16 | Receptor ruido | 6,134 | 1,861 | 1,861 | 1,861 | 12,3% | 9,3% |
| R_17 | Receptor ruido | 3,650 | 1,066 | 1,066 | 1,066 | 7,3% | 5,3% |
| R_18 | Receptor ruido | 21,716 | 4,240 | 4,240 | 4,240 | 43,4% | 21,2% |
| R_19 | Receptor ruido | 9,904 | 2,305 | 2,305 | 2,305 | 19,8% | 11,5% |
| R_20 | Receptor ruido | 11,102 | 3,019 | 3,019 | 3,019 | 22,2% | 15,1% |
| R_21 | Receptor ruido | 9,477 | 2,691 | 2,691 | 2,691 | 19,0% | 13,5% |
| R_22 | Receptor ruido | 5,993 | 1,145 | 1,145 | 1,145 | 12,0% | 5,7% |
| R_23 | Receptor ruido | 0,289 | 0,073 | 0,073 | 0,073 | 0,6% | 0,4% |
| R_24 | Receptor ruido | 0,195 | 0,064 | 0,064 | 0,064 | 0,4% | 0,3% |
| R_25 | Receptor ruido | 0,109 | 0,042 | 0,042 | 0,042 | 0,2% | 0,2% |
| R_26 | Receptor ruido | 0,285 | 0,128 | 0,128 | 0,128 | 0,6% | 0,6% |
| R_27 | Estación COEMIN | 0,299 | 0,074 | 0,074 | 0,074 | 0,6% | 0,4% |
| R_28 | Estación Nantoco | 0,307 | 0,133 | 0,133 | 0,133 | 0,6% | 0,7% |

**Tabla 5-34.: Resultados del modelo de dispersión para MP10 [μg/m** **[3]** **N]. Fase de Operación Proyectada.****

| Receptor | Descripción | Material Particulado Respirable (MP10) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración**<br>**[μg/m3N]** | **Concentración**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 1,537 | 0,738 | 130 | 50 | 1,2% | 1,5% |
| R_2 | Estación Tierra Amarilla | 2,549 | 1,269 | 1,269 | 1,269 | 2,0% | 2,5% |
| R_3 | Estación Ojanco | 2,224 | 0,848 | 0,848 | 0,848 | 1,7% | 1,7% |
| R_4 | Estación Kozan | 4,989 | 1,253 | 1,253 | 1,253 | 3,8% | 2,5% |
| R_5 | 133 casa (Carola Norte) | 1,359 | 0,658 | 0,658 | 0,658 | 1,0% | 1,3% |
| R_6 | Iglesia Tierra Amarilla | 2,030 | 1,016 | 1,016 | 1,016 | 1,6% | 2,0% |
| R_7 | El Minero | 7,206 | 2,186 | 2,186 | 2,186 | 5,5% | 4,4% |
| R_8 | Testigoteca | 4,477 | 1,236 | 1,236 | 1,236 | 3,4% | 2,5% |
| R_9 | Estadio | 14,962 | 4,407 | 4,407 | 4,407 | 11,5% | 8,8% |
| R_10 | Agrouva I | 9,029 | 2,777 | 2,777 | 2,777 | 6,9% | 5,6% |
| R_11 | Agrouva II | 3,261 | 1,418 | 1,418 | 1,418 | 2,5% | 2,8% |
| R_12 | Receptor ruido | 4,415 | 1,284 | 1,284 | 1,284 | 3,4% | 2,6% |
| R_13 | Receptor ruido | 4,101 | 1,107 | 1,107 | 1,107 | 3,2% | 2,2% |
| R_14 | Receptor ruido | 3,378 | 0,964 | 0,964 | 0,964 | 2,6% | 1,9% |
| R_15 | Receptor ruido | 9,364 | 2,971 | 2,971 | 2,971 | 7,2% | 5,9% |
| R_16 | Receptor ruido | 10,748 | 3,300 | 3,300 | 3,300 | 8,3% | 6,6% |
| R_17 | Receptor ruido | 6,484 | 1,925 | 1,925 | 1,925 | 5,0% | 3,9% |
| R_18 | Receptor ruido | 36,581 | 7,458 | 7,458 | 7,458 | 28,1% | 14,9% |
| R_19 | Receptor ruido | 18,369 | 4,972 | 4,972 | 4,972 | 14,1% | 9,9% |
| R_20 | Receptor ruido | 19,314 | 5,666 | 5,666 | 5,666 | 14,9% | 11,3% |
| R_21 | Receptor ruido | 16,482 | 5,304 | 5,304 | 5,304 | 12,7% | 10,6% |
| R_22 | Receptor ruido | 10,650 | 2,176 | 2,176 | 2,176 | 8,2% | 4,4% |
| R_23 | Receptor ruido | 0,495 | 0,133 | 0,133 | 0,133 | 0,4% | 0,3% |
| R_24 | Receptor ruido | 0,348 | 0,116 | 0,116 | 0,116 | 0,3% | 0,2% |
| R_25 | Receptor ruido | 0,198 | 0,076 | 0,076 | 0,076 | 0,2% | 0,2% |
| R_26 | Receptor ruido | 0,507 | 0,234 | 0,234 | 0,234 | 0,4% | 0,5% |
| R_27 | Estación COEMIN | 0,515 | 0,134 | 0,134 | 0,134 | 0,4% | 0,3% |
| R_28 | Estación Nantoco | 0,540 | 0,244 | 0,244 | 0,244 | 0,4% | 0,5% |

**Tabla 5-35.: Resultados del modelo de dispersión para MPS [mg/m** **[2]** **∙día]. Fase de Operación Proyectada.****

| Receptor | Descripción | Material Particulado Sedimentable (MPS) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Tasa de depositación**<br>**[mg/m2∙día]** | **Tasa de depositación**<br>**[mg/m2∙día]** | **Norma de Calidad**<br>**[mg/m2∙día]** | **Norma de Calidad**<br>**[mg/m2∙día]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **Media**<br>**Anual** | **Máxima**<br>**Media**<br>**Mensual** | **Conf. Suiza** | **República**<br>**Argentina** | **Conf. Suiza** | **República**<br>**Argentina** |
| R_1 | Estación Luis Uribe | 1,023 | 1,813 | 200 | 333 | 0,5% | 0,5% |
| R_2 | Estación Tierra Amarilla | 1,805 | 3,096 | 3,096 | 3,096 | 0,9% | 0,9% |
| R_3 | Estación Ojanco | 0,824 | 1,108 | 1,108 | 1,108 | 0,4% | 0,3% |
| R_4 | Estación Kozan | 2,464 | 3,244 | 3,244 | 3,244 | 1,2% | 1,0% |
| R_5 | 133 casa (Carola Norte) | 1,228 | 1,400 | 1,400 | 1,400 | 0,6% | 0,4% |
| R_6 | Iglesia Tierra Amarilla | 1,439 | 2,626 | 2,626 | 2,626 | 0,7% | 0,8% |
| R_7 | El Minero | 4,788 | 7,398 | 7,398 | 7,398 | 2,4% | 2,2% |
| R_8 | Testigoteca | 2,438 | 3,898 | 3,898 | 3,898 | 1,2% | 1,2% |
| R_9 | Estadio | 10,956 | 11,920 | 11,920 | 11,920 | 5,5% | 3,6% |
| R_10 | Agrouva I | 6,545 | 7,372 | 7,372 | 7,372 | 3,3% | 2,2% |
| R_11 | Agrouva II | 3,667 | 4,698 | 4,698 | 4,698 | 1,8% | 1,4% |
| R_12 | Receptor ruido | 2,464 | 3,834 | 3,834 | 3,834 | 1,2% | 1,2% |
| R_13 | Receptor ruido | 2,022 | 3,203 | 3,203 | 3,203 | 1,0% | 1,0% |
| R_14 | Receptor ruido | 1,820 | 2,270 | 2,270 | 2,270 | 0,9% | 0,7% |
| R_15 | Receptor ruido | 8,236 | 12,215 | 12,215 | 12,215 | 4,1% | 3,7% |
| R_16 | Receptor ruido | 8,212 | 12,923 | 12,923 | 12,923 | 4,1% | 3,9% |
| R_17 | Receptor ruido | 4,317 | 6,140 | 6,140 | 6,140 | 2,2% | 1,8% |
| R_18 | Receptor ruido | 19,609 | 25,115 | 25,115 | 25,115 | 9,8% | 7,5% |
| R_19 | Receptor ruido | 13,100 | 14,676 | 14,676 | 14,676 | 6,6% | 4,4% |
| R_20 | Receptor ruido | 13,505 | 15,185 | 15,185 | 15,185 | 6,8% | 4,6% |
| R_21 | Receptor ruido | 11,743 | 13,112 | 13,112 | 13,112 | 5,9% | 3,9% |
| R_22 | Receptor ruido | 4,351 | 5,296 | 5,296 | 5,296 | 2,2% | 1,6% |
| R_23 | Receptor ruido | 0,180 | 0,239 | 0,239 | 0,239 | 0,1% | 0,1% |
| R_24 | Receptor ruido | 0,159 | 0,212 | 0,212 | 0,212 | 0,1% | 0,1% |
| R_25 | Receptor ruido | 0,097 | 0,157 | 0,157 | 0,157 | 0,0% | 0,0% |
| R_26 | Receptor ruido | 0,469 | 0,613 | 0,613 | 0,613 | 0,2% | 0,2% |
| R_27 | Estación COEMIN | 0,181 | 0,241 | 0,241 | 0,241 | 0,1% | 0,1% |

**Tabla 5-36.: Resultados del modelo de dispersión para CO [mg/m** **[3]** **N]. Fase de Operación Proyectada.****

| Receptor | Descripción | Monóxido de Carbono (CO) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración**<br>**[mg/m3N]** | **Concentración**<br>**[mg/m3N]** | **Norma de Calidad**<br>**[mg/m3N]** | **Norma de Calidad**<br>**[mg/m3N]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P99 1 hora** | **P99 8**<br>**horas** | **P99 1 hora** | **P99 8**<br>**horas** | **P99 1 hora** | **P99 8**<br>**horas** |
| R_1 | Estación Luis Uribe | 0,006 | 0,002 | 30 | 10 | 0,0% | 0,0% |
| R_2 | Estación Tierra Amarilla | 0,010 | 0,004 | 0,004 | 0,004 | 0,0% | 0,0% |
| R_3 | Estación Ojanco | 0,015 | 0,004 | 0,004 | 0,004 | 0,0% | 0,0% |
| R_4 | Estación Kozan | 0,033 | 0,008 | 0,008 | 0,008 | 0,1% | 0,1% |
| R_5 | 133 casa (Carola Norte) | 0,006 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% |
| R_6 | Iglesia Tierra Amarilla | 0,006 | 0,003 | 0,003 | 0,003 | 0,0% | 0,0% |
| R_7 | El Minero | 0,071 | 0,011 | 0,011 | 0,011 | 0,2% | 0,1% |
| R_8 | Testigoteca | 0,055 | 0,008 | 0,008 | 0,008 | 0,2% | 0,1% |
| R_9 | Estadio | 0,145 | 0,027 | 0,027 | 0,027 | 0,5% | 0,3% |
| R_10 | Agrouva I | 0,080 | 0,014 | 0,014 | 0,014 | 0,3% | 0,1% |
| R_11 | Agrouva II | 0,019 | 0,005 | 0,005 | 0,005 | 0,1% | 0,0% |
| R_12 | Receptor ruido | 0,054 | 0,008 | 0,008 | 0,008 | 0,2% | 0,1% |
| R_13 | Receptor ruido | 0,051 | 0,008 | 0,008 | 0,008 | 0,2% | 0,1% |
| R_14 | Receptor ruido | 0,033 | 0,006 | 0,006 | 0,006 | 0,1% | 0,1% |
| R_15 | Receptor ruido | 0,085 | 0,016 | 0,016 | 0,016 | 0,3% | 0,2% |
| R_16 | Receptor ruido | 0,100 | 0,018 | 0,018 | 0,018 | 0,3% | 0,2% |
| R_17 | Receptor ruido | 0,063 | 0,011 | 0,011 | 0,011 | 0,2% | 0,1% |
| R_18 | Receptor ruido | 0,309 | 0,063 | 0,063 | 0,063 | 1,0% | 0,6% |
| R_19 | Receptor ruido | 0,151 | 0,030 | 0,030 | 0,030 | 0,5% | 0,3% |
| R_20 | Receptor ruido | 0,202 | 0,034 | 0,034 | 0,034 | 0,7% | 0,3% |
| R_21 | Receptor ruido | 0,167 | 0,029 | 0,029 | 0,029 | 0,6% | 0,3% |
| R_22 | Receptor ruido | 0,084 | 0,018 | 0,018 | 0,018 | 0,3% | 0,2% |
| R_23 | Receptor ruido | 0,003 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% |
| R_24 | Receptor ruido | 0,001 | 0,000 | 0,000 | 0,000 | 0,0% | 0,0% |
| R_25 | Receptor ruido | 0,001 | 0,000 | 0,000 | 0,000 | 0,0% | 0,0% |
| R_26 | Receptor ruido | 0,002 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% |
| R_27 | Estación COEMIN | 0,003 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% |
| R_28 | Estación Nantoco | 0,002 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% |

**Tabla 5-37.: Resultados del modelo de dispersión para NO** **2** **[μg/m** **[3]** **N]. Fase de Operación Proyectada.****

| Receptor | Descripción | Dióxido de Nitrógeno (NO )<br>2 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración**<br>**[μg/m3N]** | **Concentración**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P99 1 hora** | **Período**<br>**Anual** | **P99 1 hora** | **Período**<br>**Anual** | **P99 1 hora** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 6,455 | 0,465 | 400 | 100 | 1,6% | 0,5% |
| R_2 | Estación Tierra Amarilla | 10,570 | 0,807 | 0,807 | 0,807 | 2,6% | 0,8% |
| R_3 | Estación Ojanco | 16,156 | 0,515 | 0,515 | 0,515 | 4,0% | 0,5% |
| R_4 | Estación Kozan | 30,111 | 0,678 | 0,678 | 0,678 | 7,5% | 0,7% |
| R_5 | 133 casa (Carola Norte) | 4,753 | 0,325 | 0,325 | 0,325 | 1,2% | 0,3% |
| R_6 | Iglesia Tierra Amarilla | 6,207 | 0,623 | 0,623 | 0,623 | 1,6% | 0,6% |
| R_7 | El Minero | 51,024 | 0,936 | 0,936 | 0,936 | 12,8% | 0,9% |
| R_8 | Testigoteca | 38,051 | 0,515 | 0,515 | 0,515 | 9,5% | 0,5% |
| R_9 | Estadio | 104,420 | 1,851 | 1,851 | 1,851 | 26,1% | 1,9% |
| R_10 | Agrouva I | 61,445 | 1,305 | 1,305 | 1,305 | 15,4% | 1,3% |
| R_11 | Agrouva II | 21,263 | 0,818 | 0,818 | 0,818 | 5,3% | 0,8% |
| R_12 | Receptor ruido | 41,977 | 0,572 | 0,572 | 0,572 | 10,5% | 0,6% |
| R_13 | Receptor ruido | 38,835 | 0,486 | 0,486 | 0,486 | 9,7% | 0,5% |
| R_14 | Receptor ruido | 22,143 | 0,406 | 0,406 | 0,406 | 5,5% | 0,4% |
| R_15 | Receptor ruido | 43,253 | 0,930 | 0,930 | 0,930 | 10,8% | 0,9% |
| R_16 | Receptor ruido | 58,380 | 1,103 | 1,103 | 1,103 | 14,6% | 1,1% |
| R_17 | Receptor ruido | 42,251 | 0,740 | 0,740 | 0,740 | 10,6% | 0,7% |
| R_18 | Receptor ruido | 220,030 | 2,929 | 2,929 | 2,929 | 55,0% | 2,9% |
| R_19 | Receptor ruido | 120,800 | 1,900 | 1,900 | 1,900 | 30,2% | 1,9% |
| R_20 | Receptor ruido | 140,250 | 2,455 | 2,455 | 2,455 | 35,1% | 2,5% |
| R_21 | Receptor ruido | 118,240 | 2,211 | 2,211 | 2,211 | 29,6% | 2,2% |
| R_22 | Receptor ruido | 65,755 | 1,050 | 1,050 | 1,050 | 16,4% | 1,1% |
| R_23 | Receptor ruido | 2,039 | 0,067 | 0,067 | 0,067 | 0,5% | 0,1% |
| R_24 | Receptor ruido | 1,320 | 0,059 | 0,059 | 0,059 | 0,3% | 0,1% |
| R_25 | Receptor ruido | 0,534 | 0,038 | 0,038 | 0,038 | 0,1% | 0,0% |
| R_26 | Receptor ruido | 2,556 | 0,133 | 0,133 | 0,133 | 0,6% | 0,1% |
| R_27 | Estación COEMIN | 2,138 | 0,067 | 0,067 | 0,067 | 0,5% | 0,1% |
| R_28 | Estación Nantoco | 1,977 | 0,131 | 0,131 | 0,131 | 0,5% | 0,1% |

**Tabla 5-38.: Resultados del modelo de dispersión para SO** **2** **[μg/m** **[3]** **N]. Fase de Operación Proyectada.****

| Receptor | Descripción | Dióxido de Azufre (SO )<br>2 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Norma de Calidad [μg/m3N]** | **Norma de Calidad [μg/m3N]** | **Norma de Calidad [μg/m3N]** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **P99 1 hora** | **P99 24**<br>**horas** | **Período**<br>**Anual** | **P99 1 hora** | **P99 24**<br>**horas** | **Período**<br>**Anual** | **P99 1 hora** | **P99 24**<br>**horas** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 0,009 | 0,003 | 0,001 | 350 | 150 | 60 | 0,0% | 0,0% | 0,0% |
| R_2 | Estación Tierra Amarilla | 0,016 | 0,005 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_3 | Estación Ojanco | 0,020 | 0,004 | 0,001 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% | 0,0% |
| R_4 | Estación Kozan | 0,024 | 0,011 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_5 | 133 casa (Carola Norte) | 0,007 | 0,002 | 0,001 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% | 0,0% |
| R_6 | Iglesia Tierra Amarilla | 0,011 | 0,004 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_7 | El Minero | 0,063 | 0,013 | 0,004 | 0,004 | 0,004 | 0,004 | 0,0% | 0,0% | 0,0% |
| R_8 | Testigoteca | 0,038 | 0,011 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_9 | Estadio | 0,096 | 0,037 | 0,006 | 0,006 | 0,006 | 0,006 | 0,0% | 0,0% | 0,0% |
| R_10 | Agrouva I | 0,051 | 0,019 | 0,004 | 0,004 | 0,004 | 0,004 | 0,0% | 0,0% | 0,0% |
| R_11 | Agrouva II | 0,022 | 0,006 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_12 | Receptor ruido | 0,040 | 0,011 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_13 | Receptor ruido | 0,032 | 0,010 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_14 | Receptor ruido | 0,029 | 0,007 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_15 | Receptor ruido | 0,106 | 0,018 | 0,005 | 0,005 | 0,005 | 0,005 | 0,0% | 0,0% | 0,0% |
| R_16 | Receptor ruido | 0,126 | 0,020 | 0,006 | 0,006 | 0,006 | 0,006 | 0,0% | 0,0% | 0,0% |
| R_17 | Receptor ruido | 0,069 | 0,015 | 0,003 | 0,003 | 0,003 | 0,003 | 0,0% | 0,0% | 0,0% |

**Tabla 5-39.: Análisis de Significancia Fase de Operación. MP10** **[μg/m** **[3]** **N]** **.****

| Receptor | Nivel de Impacto Significativo | Col3 | Col4 | Escenario Actual | Col6 | Escenario Proyectado | Col8 | Variación | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Estadígrafo** | **Valor** | **Unidad** | **Valor** | **% SILs** | **Valor** | **% SILs** | **Valor** | **% SILs** |
| R_1 | P98 24 horas | 5 | μg/m3N | 1,49 | 29,7% | 1,54 | 30,7% | 0,05 | 1,0% |
| R_1 | Media anual | 1 | μg/m3N | 0,73 | 72,6% | 0,74 | 73,8% | 0,01 | 1,1% |
| R_2 | P98 24 horas | 5 | μg/m3N | 2,45 | 49,1% | 2,55 | 51,0% | 0,10 | 1,9% |
| R_2 | Media anual | 1 | μg/m3N | 1,23 | 123,1% | 1,27 | 126,9% | 0,04 | 3,8% |
| R_3 | P98 24 horas | 5 | μg/m3N | 2,16 | 43,2% | 2,22 | 44,5% | 0,06 | 1,2% |
| R_3 | Media anual | 1 | μg/m3N | 0,85 | 84,9% | 0,85 | 84,8% | 0,00 | -0,1% |

**Tabla 6-1.: Valores de significancia para la evaluación de impacto significativo en un escenario de riesgo****

| Contaminante | Período | SIL Porcentual<br>US EPA | Incremento Significativo en<br>la Concentración [ug/m3] | Referencia |
| --- | --- | --- | --- | --- |
| MP2.5 | 24 horas | 3,4% | 1,71 | Tabla 1. Capítulo 4. “Criterio de<br>Evaluación en el SEIA: Impacto de<br>emisiones en zonas saturadas por<br>material particulado respirable<br>MP10 y material particulado fino<br>respirable MP2.5” (SEA, 2023). |
| MP2.5 | Anual | 1,7% | 0,33 | 0,33 |
| MP10 | 24 horas | 3,3% | 5,00 | 5,00 |
| MP10 | Anual | 2,0% | 1,00 | 1,00 |
| NO2 | 1 hora | 4,0% | 16,00 | Tabla 7-5, Capítulo 8. “Evaluación<br>Significancia del Impacto de las<br>Emisiones de un Proyecto o<br>Actividad en Zonas Saturadas en el<br>Marco del SEIA” (DICTUC, 2022) |
| NO2 | Anual | 1,0% | 1,00 | 1,00 |
| CO | 1 hora | 5,0% | 1.500,00 | 1.500,00 |
| CO | 8 horas | 4,9% | 488,90 | 488,90 |
| SO2 | 1 hora | 4,0% | 14,00 | 14,00 |
| SO2 | 24 horas | 1,4% | 2,00 | 2,00 |
| SO2 | Anual | 2,0% | 1,20 | 1,20 |

**Tabla 7-1.: Características de Fuentes Emisoras y Tasas de Emisión. Escenario Sinérgico Fase de Operación Base.****

| ID | Descripción | Tipo de fuente | Tasas de emisión | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **Descripción** | **Tipo de fuente** | **MP2.5** | **MP10** | **MPS** | **NO** | **NO2 ** | **SO2 ** | **CO** | **Unidad** |
| SRC_1 | Tramo C1 | Camino | 2,78 E-07 | 9,83 E-07 | 4,90 E-06 | 1,23 E-06 | 2,10 E-07 | 2,29 E-09 | 5,46 E-07 | g/s/m |
| SRC_2 | Tramo C2 | Camino | 1,40 E-06 | 5,60 E-06 | 2,89 E-05 | 1,71 E-06 | 2,92 E-07 | 3,06 E-09 | 7,28 E-07 | g/s/m |
| SRC_3 | Tramo C3 | Camino | 1,15 E-06 | 4,63 E-06 | 2,39 E-05 | 1,20 E-06 | 2,05 E-07 | 2,07 E-09 | 4,93 E-07 | g/s/m |
| SRC_4 | Tramo C4 | Camino | 8,87 E-08 | 3,12 E-07 | 1,56 E-06 | 3,13 E-07 | 5,34 E-08 | 6,53 E-10 | 1,53 E-07 | g/s/m |
| SRC_5 | Tramo C5 | Camino | 1,33 E-06 | 5,32 E-06 | 2,75 E-05 | 1,59 E-06 | 2,71 E-07 | 2,80 E-09 | 6,69 E-07 | g/s/m |
| SRC_6 | Tramo C6 | Camino | 2,13 E-06 | 8,69 E-06 | 4,51 E-05 | 1,06 E-06 | 1,81 E-07 | 1,82 E-09 | 4,35 E-07 | g/s/m |
| SRC_7 | Tramo C7 | Camino | 8,09 E-07 | 3,27 E-06 | 1,69 E-05 | 7,18 E-07 | 1,22 E-07 | 1,24 E-09 | 2,95 E-07 | g/s/m |
| SRC_8 | Tramo C9 | Camino | 8,31 E-07 | 3,35 E-06 | 1,74 E-05 | 7,42 E-07 | 1,26 E-07 | 1,28 E-09 | 3,05 E-07 | g/s/m |
| SRC_9 | Tramo C10 | Camino | 8,77 E-07 | 3,54 E-06 | 1,83 E-05 | 8,06 E-07 | 1,37 E-07 | 1,39 E-09 | 3,30 E-07 | g/s/m |
| SRC_10 | Tramo C11 | Camino | 5,30 E-08 | 2,10 E-07 | 1,08 E-06 | 8,42 E-08 | 1,44 E-08 | 1,44 E-10 | 3,42 E-08 | g/s/m |
| SRC_11 | Tramo C12 | Camino | 6,46 E-07 | 2,53 E-06 | 1,30 E-05 | 1,10 E-06 | 1,87 E-07 | 2,01 E-09 | 4,77 E-07 | g/s/m |
| SRC_12 | Tramo N1 | Camino | 6,62 E-07 | 6,43 E-06 | 2,61 E-05 | 4,62 E-07 | 7,87 E-08 | 8,79 E-10 | 2,13 E-07 | g/s/m |
| SRC_13 | Tramo N2 | Camino | 6,02 E-07 | 5,84 E-06 | 2,37 E-05 | 4,20 E-07 | 7,15 E-08 | 7,99 E-10 | 1,94 E-07 | g/s/m |
| SRC_14 | Tramo N3 | Camino | 2,80 E-07 | 2,68 E-06 | 1,09 E-05 | 2,94 E-07 | 5,01 E-08 | 5,36 E-10 | 1,34 E-07 | g/s/m |
| SRC_15 | Tramo N4 | Camino | 1,15 E-06 | 1,14 E-05 | 4,63 E-05 | 4,63 E-07 | 7,88 E-08 | 7,96 E-10 | 1,90 E-07 | g/s/m |
| SRC_16 | Tramo N5 | Camino | 1,02 E-06 | 1,00 E-05 | 4,08 E-05 | 4,07 E-07 | 6,94 E-08 | 7,00 E-10 | 1,67 E-07 | g/s/m |
| SRC_17 | Tramo S1 | Camino | 2,93 E-06 | 2,92 E-05 | 8,45 E-05 | 2,12 E-07 | 3,61 E-08 | 5,78 E-10 | 1,22 E-07 | g/s/m |
| SRC_18 | Tramo S2 | Camino | 3,11 E-06 | 3,10 E-05 | 8,96 E-05 | 2,25 E-07 | 3,83 E-08 | 6,13 E-10 | 1,30 E-07 | g/s/m |
| SRC_19 | Tramo S3 | Camino | 7,72 E-06 | 7,69 E-05 | 2,23 E-04 | 7,00 E-07 | 1,19 E-07 | 1,20 E-09 | 2,88 E-07 | g/s/m |
| SRC_20 | Tramo S4 | Camino | 2,14 E-05 | 2,14 E-04 | 6,18 E-04 | 1,43 E-06 | 2,43 E-07 | 2,87 E-09 | 6,55 E-07 | g/s/m |
| SRC_21 | Tramo P1 | Camino | 2,48 E-08 | 9,32 E-08 | 4,73 E-07 | 8,55 E-08 | 1,46 E-08 | 1,47 E-10 | 3,51 E-08 | g/s/m |
| SRC_22 | Tramo P2 | Camino | 2,77 E-08 | 1,04 E-07 | 5,28 E-07 | 9,55 E-08 | 1,63 E-08 | 1,64 E-10 | 3,92 E-08 | g/s/m |
| SRC_23 | Tramo P3 | Camino | 2,08 E-07 | 7,12 E-07 | 3,51 E-06 | 9,01 E-07 | 1,54 E-07 | 1,88 E-09 | 4,34 E-07 | g/s/m |

**Tabla 7-2.: Características de Fuentes Emisoras y Tasas de Emisión. Escenario Sinérgico Fase de Operación Proyectado.****

| ID | Descripción | Tipo de fuente | Tasas de emisión | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **ID** | **Descripción** | **Tipo de fuente** | **MP2.5** | **MP10** | **MPS** | **NO** | **NO2 ** | **SO2 ** | **CO** | **Unidad** |
| SRC_1 | Tramo C1 | Camino | 1,88 E-07 | 6,11 E-07 | 2,96 E-06 | 1,23 E-06 | 2,10 E-07 | 2,29 E-09 | 5,46 E-07 | g/s/m |
| SRC_2 | Tramo C2 | Camino | 9,22 E-07 | 3,60 E-06 | 1,84 E-05 | 1,79 E-06 | 3,05 E-07 | 3,20 E-09 | 7,60 E-07 | g/s/m |
| SRC_3 | Tramo C3 | Camino | 7,56 E-07 | 2,99 E-06 | 1,54 E-05 | 1,27 E-06 | 2,17 E-07 | 2,19 E-09 | 5,22 E-07 | g/s/m |
| SRC_4 | Tramo C4 | Camino | 6,01 E-08 | 1,94 E-07 | 9,40 E-07 | 3,13 E-07 | 5,34 E-08 | 6,53 E-10 | 1,53 E-07 | g/s/m |
| SRC_5 | Tramo C5 | Camino | 1,42 E-06 | 5,68 E-06 | 2,93 E-05 | 1,67 E-06 | 2,85 E-07 | 2,93 E-09 | 7,02 E-07 | g/s/m |
| SRC_6 | Tramo C6 | Camino | 2,32 E-06 | 9,45 E-06 | 4,91 E-05 | 1,13 E-06 | 1,92 E-07 | 1,94 E-09 | 4,64 E-07 | g/s/m |
| SRC_7 | Tramo C7 | Camino | 8,90 E-07 | 3,59 E-06 | 1,86 E-05 | 7,90 E-07 | 1,35 E-07 | 1,36 E-09 | 3,24 E-07 | g/s/m |
| SRC_8 | Tramo C9 | Camino | 7,50 E-07 | 3,01 E-06 | 1,56 E-05 | 8,15 E-07 | 1,39 E-07 | 1,40 E-09 | 3,35 E-07 | g/s/m |
| SRC_9 | Tramo C10 | Camino | 5,89 E-07 | 2,34 E-06 | 1,21 E-05 | 8,80 E-07 | 1,50 E-07 | 1,51 E-09 | 3,61 E-07 | g/s/m |
| SRC_10 | Tramo C11 | Camino | 3,30 E-08 | 1,27 E-07 | 6,49 E-07 | 8,42 E-08 | 1,44 E-08 | 1,44 E-10 | 3,42 E-08 | g/s/m |
| SRC_11 | Tramo C12 | Camino | 4,05 E-07 | 1,54 E-06 | 7,81 E-06 | 1,10 E-06 | 1,87 E-07 | 2,01 E-09 | 4,77 E-07 | g/s/m |
| SRC_12 | Tramo N1 | Camino | 2,35 E-07 | 2,16 E-06 | 8,71 E-06 | 4,62 E-07 | 7,87 E-08 | 8,79 E-10 | 2,13 E-07 | g/s/m |
| SRC_13 | Tramo N2 | Camino | 2,14 E-07 | 1,96 E-06 | 7,92 E-06 | 4,20 E-07 | 7,15 E-08 | 7,99 E-10 | 1,94 E-07 | g/s/m |

**Tabla 7-3.: Receptores de Interés. Escenario Sinérgico Fase de Operación.****

| ID | Receptor | Coordenadas [Datum WGS84] | Col4 | Elevación<br>[m.s.n.m.] |
| --- | --- | --- | --- | --- |
| **ID** | **Receptor** | **Este (m)** | **Norte (m)** | **Norte (m)** |
| R_1 | Estación Luis Uribe | 374.942 | 6.961.596 | 514,30 |
| R_2 | Estación Tierra Amarilla | 374.904 | 6.960.235 | 521,39 |
| R_3 | Estación Ojanco | 374.772 | 6.958.885 | 513,93 |
| R_4 | Estación Kozan | 375.076 | 6.956.263 | 568,74 |
| R_5 | 133 casa (Carola Norte) | 375.842 | 6.961.206 | 561,91 |
| R_6 | Iglesia Tierra Amarilla | 375.270 | 6.961.216 | 518,20 |
| R_7 | El Minero | 375.114 | 6.958.078 | 540,49 |
| R_8 | Testigoteca | 375.054 | 6.957.920 | 541,09 |
| R_9 | Estadio | 375.353 | 6.956.715 | 573,60 |
| R_10 | Agrouva I | 375.347 | 6.956.543 | 567,13 |
| R_11 | Agrouva II | 375.370 | 6.956.345 | 551,88 |
| R_12 | Receptor ruido (viviendas 1 piso, material mixto) | 375.021 | 6.958.033 | 539,80 |
| R_13 | Receptor ruido (viviendas 1 piso, material ligero) | 375.005 | 6.957.965 | 540,10 |
| R_14 | Receptor ruido (viviendas 1 piso, material ligero) | 374.966 | 6.957.769 | 542,55 |
| R_15 | Receptor ruido (Oficinas, galpones y container, material<br>mixto) | 375.215 | 6.957.683 | 554,95 |
| R_16 | Receptor ruido (Vivienda 2 pisos, material ligero) | 375.126 | 6.957.573 | 558,76 |
| R_17 | Receptor ruido (Viviendas 1 y 2 pisos, material ligero) | 375.093 | 6.957.335 | 555,04 |
| R_18 | Receptor ruido (Viviendas 1 y 2 pisos, material mixto) | 375.248 | 6.957.084 | 566,44 |
| R_19 | Receptor ruido (Viviendas 1 y 2 pisos, material ligero) | 375.278 | 6.956.755 | 573,88 |
| R_20 | Receptor ruido (Viviendas 1 piso, material ligero) | 375.476 | 6.956.834 | 575,09 |
| R_21 | Receptor ruido (Vivienda 1 piso, material ligero) | 375.633 | 6.956.813 | 584,48 |

**Tabla 7-4.: Resultados del modelo de dispersión para MP2.5 [μg/m** **[3]** **]. Escenario Sinérgico Fase de****

| Receptor | Descripción | Material Particulado Respirable Fino (MP2.5) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [μg/m3] ** | **Concentración [μg/m3] ** | **Norma de Calidad**<br>**[μg/m3] ** | **Norma de Calidad**<br>**[μg/m3] ** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 0,950 | 0,462 | 50 | 20 | 1,9% | 2,3% |
| R_2 | Estación Tierra Amarilla | 1,513 | 0,775 | 0,775 | 0,775 | 3,0% | 3,9% |
| R_3 | Estación Ojanco | 1,430 | 0,646 | 0,646 | 0,646 | 2,9% | 3,2% |
| R_4 | Estación Kozan | 3,778 | 1,430 | 1,430 | 1,430 | 7,6% | 7,2% |
| R_5 | 133 casa (Carola Norte) | 0,759 | 0,350 | 0,350 | 0,350 | 1,5% | 1,7% |
| R_6 | Iglesia Tierra Amarilla | 1,157 | 0,590 | 0,590 | 0,590 | 2,3% | 2,9% |
| R_7 | El Minero | 4,472 | 1,719 | 1,719 | 1,719 | 8,9% | 8,6% |
| R_8 | Testigoteca | 2,742 | 1,040 | 1,040 | 1,040 | 5,5% | 5,2% |
| R_9 | Estadio | 8,552 | 2,554 | 2,554 | 2,554 | 17,1% | 12,8% |
| R_10 | Agrouva I | 5,284 | 1,823 | 1,823 | 1,823 | 10,6% | 9,1% |
| R_11 | Agrouva II | 1,961 | 1,021 | 1,021 | 1,021 | 3,9% | 5,1% |
| R_12 | Receptor ruido | 3,695 | 1,754 | 1,754 | 1,754 | 7,4% | 8,8% |
| R_13 | Receptor ruido | 2,712 | 1,097 | 1,097 | 1,097 | 5,4% | 5,5% |
| R_14 | Receptor ruido | 2,342 | 1,117 | 1,117 | 1,117 | 4,7% | 5,6% |
| R_15 | Receptor ruido | 5,235 | 1,823 | 1,823 | 1,823 | 10,5% | 9,1% |
| R_16 | Receptor ruido | 6,304 | 2,088 | 2,088 | 2,088 | 12,6% | 10,4% |
| R_17 | Receptor ruido | 4,229 | 1,619 | 1,619 | 1,619 | 8,5% | 8,1% |
| R_18 | Receptor ruido | 20,338 | 4,302 | 4,302 | 4,302 | 40,7% | 21,5% |
| R_19 | Receptor ruido | 10,464 | 2,872 | 2,872 | 2,872 | 20,9% | 14,4% |
| R_20 | Receptor ruido | 10,721 | 3,153 | 3,153 | 3,153 | 21,4% | 15,8% |
| R_21 | Receptor ruido | 8,916 | 2,832 | 2,832 | 2,832 | 17,8% | 14,2% |
| R_22 | Receptor ruido | 8,589 | 2,751 | 2,751 | 2,751 | 17,2% | 13,8% |
| R_23 | Receptor ruido | 15,538 | 7,321 | 7,321 | 7,321 | 31,1% | 36,6% |
| R_24 | Receptor ruido | 2,455 | 0,703 | 0,703 | 0,703 | 4,9% | 3,5% |
| R_25 | Receptor ruido | 0,270 | 0,103 | 0,103 | 0,103 | 0,5% | 0,5% |
| R_26 | Receptor ruido | 1,982 | 1,066 | 1,066 | 1,066 | 4,0% | 5,3% |

**Tabla 7-5.: Resultados del modelo de dispersión para MP10 [μg/m** **[3]** **N]. Escenario Sinérgico Fase de****

| Receptor | Descripción | Material Particulado Respirable (MP10) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración**<br>**[μg/m3N]** | **Concentración**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 2,123 | 1,051 | 130 | 50 | 1,6% | 2,1% |
| R_2 | Estación Tierra Amarilla | 3,307 | 1,689 | 1,689 | 1,689 | 2,5% | 3,4% |
| R_3 | Estación Ojanco | 3,179 | 1,634 | 1,634 | 1,634 | 2,4% | 3,3% |
| R_4 | Estación Kozan | 11,366 | 4,355 | 4,355 | 4,355 | 8,7% | 8,7% |
| R_5 | 133 casa (Carola Norte) | 2,021 | 1,106 | 1,106 | 1,106 | 1,6% | 2,2% |
| R_6 | Iglesia Tierra Amarilla | 2,559 | 1,322 | 1,322 | 1,322 | 2,0% | 2,6% |
| R_7 | El Minero | 10,230 | 4,393 | 4,393 | 4,393 | 7,9% | 8,8% |
| R_8 | Testigoteca | 6,753 | 2,813 | 2,813 | 2,813 | 5,2% | 5,6% |
| R_9 | Estadio | 19,227 | 7,238 | 7,238 | 7,238 | 14,8% | 14,5% |
| R_10 | Agrouva I | 12,081 | 5,134 | 5,134 | 5,134 | 9,3% | 10,3% |
| R_11 | Agrouva II | 4,320 | 2,594 | 2,594 | 2,594 | 3,3% | 5,2% |
| R_12 | Receptor ruido | 10,596 | 5,496 | 5,496 | 5,496 | 8,2% | 11,0% |
| R_13 | Receptor ruido | 6,898 | 3,157 | 3,157 | 3,157 | 5,3% | 6,3% |
| R_14 | Receptor ruido | 5,989 | 3,384 | 3,384 | 3,384 | 4,6% | 6,8% |
| R_15 | Receptor ruido | 10,524 | 4,080 | 4,080 | 4,080 | 8,1% | 8,2% |
| R_16 | Receptor ruido | 12,508 | 4,614 | 4,614 | 4,614 | 9,6% | 9,2% |
| R_17 | Receptor ruido | 10,447 | 4,331 | 4,331 | 4,331 | 8,0% | 8,7% |
| R_18 | Receptor ruido | 35,795 | 8,743 | 8,743 | 8,743 | 27,5% | 17,5% |
| R_19 | Receptor ruido | 23,265 | 9,016 | 9,016 | 9,016 | 17,9% | 18,0% |
| R_20 | Receptor ruido | 20,820 | 7,424 | 7,424 | 7,424 | 16,0% | 14,8% |
| R_21 | Receptor ruido | 18,367 | 7,300 | 7,300 | 7,300 | 14,1% | 14,6% |
| R_22 | Receptor ruido | 21,231 | 8,726 | 8,726 | 8,726 | 16,3% | 17,5% |
| R_23 | Receptor ruido | 62,560 | 28,861 | 28,861 | 28,861 | 48,1% | 57,7% |
| R_24 | Receptor ruido | 9,554 | 2,647 | 2,647 | 2,647 | 7,3% | 5,3% |
| R_25 | Receptor ruido | 0,918 | 0,328 | 0,328 | 0,328 | 0,7% | 0,7% |
| R_26 | Receptor ruido | 7,205 | 3,797 | 3,797 | 3,797 | 5,5% | 7,6% |

**Tabla 7-6.: Resultados del modelo de dispersión para MPS [mg/m** **[2∙]** **día]. Escenario Sinérgico Fase de****

| Receptor | Descripción | Material Particulado Sedimentable (MPS) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Tasa de depositación**<br>**[mg/m2∙día]** | **Tasa de depositación**<br>**[mg/m2∙día]** | **Norma de Calidad**<br>**[mg/m2∙día]** | **Norma de Calidad**<br>**[mg/m2∙día]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **Media**<br>**Anual** | **Máxima**<br>**Media**<br>**Mensual** | **Conf. Suiza** | **República**<br>**Argentina** | **Conf. Suiza** | **República**<br>**Argentina** |
| R_1 | Estación Luis Uribe | 1,477 | 2,448 | 200 | 333 | 0,7% | 0,7% |
| R_2 | Estación Tierra Amarilla | 2,338 | 3,908 | 3,908 | 3,908 | 1,2% | 1,2% |
| R_3 | Estación Ojanco | 1,900 | 2,852 | 2,852 | 2,852 | 0,9% | 0,9% |
| R_4 | Estación Kozan | 17,819 | 22,066 | 22,066 | 22,066 | 8,9% | 6,6% |
| R_5 | 133 casa (Carola Norte) | 2,868 | 3,391 | 3,391 | 3,391 | 1,4% | 1,0% |
| R_6 | Iglesia Tierra Amarilla | 1,860 | 3,169 | 3,169 | 3,169 | 0,9% | 1,0% |
| R_7 | El Minero | 15,222 | 20,032 | 20,032 | 20,032 | 7,6% | 6,0% |
| R_8 | Testigoteca | 9,453 | 11,185 | 11,185 | 11,185 | 4,7% | 3,4% |
| R_9 | Estadio | 21,047 | 22,784 | 22,784 | 22,784 | 10,5% | 6,8% |
| R_10 | Agrouva I | 14,874 | 16,094 | 16,094 | 16,094 | 7,4% | 4,8% |
| R_11 | Agrouva II | 6,915 | 8,065 | 8,065 | 8,065 | 3,5% | 2,4% |
| R_12 | Receptor ruido | 25,493 | 32,586 | 32,586 | 32,586 | 12,7% | 9,8% |
| R_13 | Receptor ruido | 12,248 | 14,776 | 14,776 | 14,776 | 6,1% | 4,4% |
| R_14 | Receptor ruido | 14,239 | 15,777 | 15,777 | 15,777 | 7,1% | 4,7% |
| R_15 | Receptor ruido | 12,245 | 17,079 | 17,079 | 17,079 | 6,1% | 5,1% |
| R_16 | Receptor ruido | 13,403 | 18,935 | 18,935 | 18,935 | 6,7% | 5,7% |
| R_17 | Receptor ruido | 15,585 | 18,731 | 18,731 | 18,731 | 7,8% | 5,6% |
| R_18 | Receptor ruido | 24,462 | 30,588 | 30,588 | 30,588 | 12,2% | 9,2% |
| R_19 | Receptor ruido | 29,015 | 31,874 | 31,874 | 31,874 | 14,5% | 9,6% |
| R_20 | Receptor ruido | 18,752 | 21,588 | 21,588 | 21,588 | 9,4% | 6,5% |
| R_21 | Receptor ruido | 17,542 | 20,347 | 20,347 | 20,347 | 8,8% | 6,1% |
| R_22 | Receptor ruido | 44,728 | 53,543 | 53,543 | 53,543 | 22,4% | 16,1% |
| R_23 | Receptor ruido | 103,480 | 127,549 | 127,549 | 127,549 | 51,7% | 38,3% |
| R_24 | Receptor ruido | 4,875 | 5,850 | 5,850 | 5,850 | 2,4% | 1,8% |
| R_25 | Receptor ruido | 0,335 | 0,431 | 0,431 | 0,431 | 0,2% | 0,1% |

**Tabla 7-7.: Resultados del modelo de dispersión para CO [mg/m** **[3]** **N]. Escenario Sinérgico Fase de Operación****

| Receptor | Descripción | Monóxido de Carbono (CO) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración**<br>**[mg/m3N]** | **Concentración**<br>**[mg/m3N]** | **Norma de Calidad**<br>**[mg/m3N]** | **Norma de Calidad**<br>**[mg/m3N]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P99 1 hora** | **P99 8**<br>**horas** | **P99 1 hora** | **P99 8**<br>**horas** | **P99 1 hora** | **P99 8**<br>**horas** |
| R_1 | Estación Luis Uribe | 0,007 | 0,003 | 30 | 10 | 0,0% | 0,0% |
| R_2 | Estación Tierra Amarilla | 0,011 | 0,004 | 0,004 | 0,004 | 0,0% | 0,0% |
| R_3 | Estación Ojanco | 0,016 | 0,005 | 0,005 | 0,005 | 0,1% | 0,0% |
| R_4 | Estación Kozan | 0,038 | 0,013 | 0,013 | 0,013 | 0,1% | 0,1% |
| R_5 | 133 casa (Carola Norte) | 0,006 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% |
| R_6 | Iglesia Tierra Amarilla | 0,007 | 0,003 | 0,003 | 0,003 | 0,0% | 0,0% |
| R_7 | El Minero | 0,079 | 0,014 | 0,014 | 0,014 | 0,3% | 0,1% |
| R_8 | Testigoteca | 0,058 | 0,010 | 0,010 | 0,010 | 0,2% | 0,1% |
| R_9 | Estadio | 0,154 | 0,029 | 0,029 | 0,029 | 0,5% | 0,3% |
| R_10 | Agrouva I | 0,085 | 0,017 | 0,017 | 0,017 | 0,3% | 0,2% |
| R_11 | Agrouva II | 0,021 | 0,005 | 0,005 | 0,005 | 0,1% | 0,1% |
| R_12 | Receptor ruido | 0,062 | 0,012 | 0,012 | 0,012 | 0,2% | 0,1% |
| R_13 | Receptor ruido | 0,054 | 0,010 | 0,010 | 0,010 | 0,2% | 0,1% |
| R_14 | Receptor ruido | 0,035 | 0,007 | 0,007 | 0,007 | 0,1% | 0,1% |
| R_15 | Receptor ruido | 0,091 | 0,017 | 0,017 | 0,017 | 0,3% | 0,2% |
| R_16 | Receptor ruido | 0,106 | 0,020 | 0,020 | 0,020 | 0,4% | 0,2% |
| R_17 | Receptor ruido | 0,071 | 0,014 | 0,014 | 0,014 | 0,2% | 0,1% |
| R_18 | Receptor ruido | 0,326 | 0,067 | 0,067 | 0,067 | 1,1% | 0,7% |
| R_19 | Receptor ruido | 0,166 | 0,032 | 0,032 | 0,032 | 0,6% | 0,3% |
| R_20 | Receptor ruido | 0,214 | 0,036 | 0,036 | 0,036 | 0,7% | 0,4% |
| R_21 | Receptor ruido | 0,177 | 0,032 | 0,032 | 0,032 | 0,6% | 0,3% |
| R_22 | Receptor ruido | 0,101 | 0,028 | 0,028 | 0,028 | 0,3% | 0,3% |
| R_23 | Receptor ruido | 0,141 | 0,047 | 0,047 | 0,047 | 0,5% | 0,5% |
| R_24 | Receptor ruido | 0,035 | 0,008 | 0,008 | 0,008 | 0,1% | 0,1% |
| R_25 | Receptor ruido | 0,002 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% |
| R_26 | Receptor ruido | 0,011 | 0,005 | 0,005 | 0,005 | 0,0% | 0,1% |

**Tabla 7-8.: Resultados del modelo de dispersión para NO** **2** **[μg/m** **[3]** **N]. Escenario Sinérgico Fase de Operación****

| Receptor | Descripción | Dióxido de Nitrógeno (NO )<br>2 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración**<br>**[μg/m3N]** | **Concentración**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P99 1 hora** | **Período**<br>**Anual** | **P99 1 hora** | **Período**<br>**Anual** | **P99 1 hora** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 6,866 | 0,668 | 400 | 100 | 1,7% | 0,7% |
| R_2 | Estación Tierra Amarilla | 12,448 | 1,114 | 1,114 | 1,114 | 3,1% | 1,1% |
| R_3 | Estación Ojanco | 16,481 | 1,237 | 1,237 | 1,237 | 4,1% | 1,2% |
| R_4 | Estación Kozan | 32,737 | 1,741 | 1,741 | 1,741 | 8,2% | 1,7% |
| R_5 | 133 casa (Carola Norte) | 5,148 | 0,408 | 0,408 | 0,408 | 1,3% | 0,4% |
| R_6 | Iglesia Tierra Amarilla | 6,877 | 0,788 | 0,788 | 0,788 | 1,7% | 0,8% |
| R_7 | El Minero | 50,532 | 1,562 | 1,562 | 1,562 | 12,6% | 1,6% |
| R_8 | Testigoteca | 35,586 | 1,110 | 1,110 | 1,110 | 8,9% | 1,1% |
| R_9 | Estadio | 99,246 | 2,661 | 2,661 | 2,661 | 24,8% | 2,7% |
| R_10 | Agrouva I | 58,638 | 2,252 | 2,252 | 2,252 | 14,7% | 2,3% |
| R_11 | Agrouva II | 20,055 | 1,568 | 1,568 | 1,568 | 5,0% | 1,6% |
| R_12 | Receptor ruido | 41,342 | 1,538 | 1,538 | 1,538 | 10,3% | 1,5% |
| R_13 | Receptor ruido | 36,394 | 1,165 | 1,165 | 1,165 | 9,1% | 1,2% |
| R_14 | Receptor ruido | 20,329 | 1,168 | 1,168 | 1,168 | 5,1% | 1,2% |
| R_15 | Receptor ruido | 41,803 | 1,425 | 1,425 | 1,425 | 10,5% | 1,4% |
| R_16 | Receptor ruido | 56,478 | 1,658 | 1,658 | 1,658 | 14,1% | 1,7% |
| R_17 | Receptor ruido | 41,873 | 1,471 | 1,471 | 1,471 | 10,5% | 1,5% |
| R_18 | Receptor ruido | 204,480 | 3,490 | 3,490 | 3,490 | 51,1% | 3,5% |
| R_19 | Receptor ruido | 115,590 | 2,810 | 2,810 | 2,810 | 28,9% | 2,8% |
| R_20 | Receptor ruido | 128,880 | 3,000 | 3,000 | 3,000 | 32,2% | 3,0% |
| R_21 | Receptor ruido | 112,500 | 2,649 | 2,649 | 2,649 | 28,1% | 2,6% |
| R_22 | Receptor ruido | 74,364 | 2,587 | 2,587 | 2,587 | 18,6% | 2,6% |
| R_23 | Receptor ruido | 41,221 | 2,533 | 2,533 | 2,533 | 10,3% | 2,5% |
| R_24 | Receptor ruido | 15,596 | 0,684 | 0,684 | 0,684 | 3,9% | 0,7% |
| R_25 | Receptor ruido | 1,956 | 0,154 | 0,154 | 0,154 | 0,5% | 0,2% |
| R_26 | Receptor ruido | 14,495 | 1,503 | 1,503 | 1,503 | 3,6% | 1,5% |

**Tabla 7-9.: Resultados del modelo de dispersión para SO** **2** **[μg/m** **[3]** **N]. Escenario Sinérgico Fase de Operación Base.****

| Receptor | Descripción | Dióxido de Azufre (SO )<br>2 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Norma de Calidad [μg/m3N]** | **Norma de Calidad [μg/m3N]** | **Norma de Calidad [μg/m3N]** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **P99 1 hora** | **P99 24**<br>**horas** | **Período**<br>**Anual** | **P99 1 hora** | **P99 24**<br>**horas** | **Período**<br>**Anual** | **P99 1 hora** | **P99 24**<br>**horas** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 0,010 | 0,003 | 0,002 | 350 | 150 | 60 | 0,0% | 0,0% | 0,0% |
| R_2 | Estación Tierra Amarilla | 0,016 | 0,006 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_3 | Estación Ojanco | 0,020 | 0,005 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_4 | Estación Kozan | 0,064 | 0,017 | 0,006 | 0,006 | 0,006 | 0,006 | 0,0% | 0,0% | 0,0% |
| R_5 | 133 casa (Carola Norte) | 0,007 | 0,002 | 0,001 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% | 0,0% |
| R_6 | Iglesia Tierra Amarilla | 0,011 | 0,004 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_7 | El Minero | 0,068 | 0,016 | 0,006 | 0,006 | 0,006 | 0,006 | 0,0% | 0,0% | 0,0% |
| R_8 | Testigoteca | 0,046 | 0,013 | 0,004 | 0,004 | 0,004 | 0,004 | 0,0% | 0,0% | 0,0% |
| R_9 | Estadio | 0,100 | 0,035 | 0,007 | 0,007 | 0,007 | 0,007 | 0,0% | 0,0% | 0,0% |
| R_10 | Agrouva I | 0,055 | 0,019 | 0,006 | 0,006 | 0,006 | 0,006 | 0,0% | 0,0% | 0,0% |
| R_11 | Agrouva II | 0,022 | 0,006 | 0,003 | 0,003 | 0,003 | 0,003 | 0,0% | 0,0% | 0,0% |
| R_12 | Receptor ruido | 0,087 | 0,017 | 0,008 | 0,008 | 0,008 | 0,008 | 0,0% | 0,0% | 0,0% |
| R_13 | Receptor ruido | 0,047 | 0,014 | 0,004 | 0,004 | 0,004 | 0,004 | 0,0% | 0,0% | 0,0% |
| R_14 | Receptor ruido | 0,041 | 0,010 | 0,005 | 0,005 | 0,005 | 0,005 | 0,0% | 0,0% | 0,0% |
| R_15 | Receptor ruido | 0,107 | 0,018 | 0,006 | 0,006 | 0,006 | 0,006 | 0,0% | 0,0% | 0,0% |
| R_16 | Receptor ruido | 0,132 | 0,023 | 0,007 | 0,007 | 0,007 | 0,007 | 0,0% | 0,0% | 0,0% |
| R_17 | Receptor ruido | 0,082 | 0,017 | 0,006 | 0,006 | 0,006 | 0,006 | 0,0% | 0,0% | 0,0% |
| R_18 | Receptor ruido | 0,265 | 0,063 | 0,013 | 0,013 | 0,013 | 0,013 | 0,1% | 0,0% | 0,0% |

**Tabla 7-10.: Resultados del modelo de dispersión para MP2.5 [μg/m** **[3]** **]. Escenario Sinérgico Fase de****

| Receptor | Descripción | Material Particulado Respirable Fino (MP2.5) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [μg/m3] ** | **Concentración [μg/m3] ** | **Norma de Calidad**<br>**[μg/m3] ** | **Norma de Calidad**<br>**[μg/m3] ** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 0,986 | 0,475 | 50 | 20 | 2,0% | 2,4% |
| R_2 | Estación Tierra Amarilla | 1,570 | 0,805 | 0,805 | 0,805 | 3,1% | 4,0% |
| R_3 | Estación Ojanco | 1,481 | 0,642 | 0,642 | 0,642 | 3,0% | 3,2% |
| R_4 | Estación Kozan | 3,773 | 1,320 | 1,320 | 1,320 | 7,5% | 6,6% |
| R_5 | 133 casa (Carola Norte) | 0,782 | 0,334 | 0,334 | 0,334 | 1,6% | 1,7% |
| R_6 | Iglesia Tierra Amarilla | 1,216 | 0,613 | 0,613 | 0,613 | 2,4% | 3,1% |
| R_7 | El Minero | 4,660 | 1,656 | 1,656 | 1,656 | 9,3% | 8,3% |
| R_8 | Testigoteca | 2,805 | 0,995 | 0,995 | 0,995 | 5,6% | 5,0% |
| R_9 | Estadio | 8,916 | 2,499 | 2,499 | 2,499 | 17,8% | 12,5% |
| R_10 | Agrouva I | 5,466 | 1,766 | 1,766 | 1,766 | 10,9% | 8,8% |
| R_11 | Agrouva II | 2,025 | 0,998 | 0,998 | 0,998 | 4,0% | 5,0% |
| R_12 | Receptor ruido | 3,453 | 1,505 | 1,505 | 1,505 | 6,9% | 7,5% |
| R_13 | Receptor ruido | 2,599 | 1,021 | 1,021 | 1,021 | 5,2% | 5,1% |
| R_14 | Receptor ruido | 2,412 | 1,032 | 1,032 | 1,032 | 4,8% | 5,2% |
| R_15 | Receptor ruido | 5,625 | 1,875 | 1,875 | 1,875 | 11,3% | 9,4% |
| R_16 | Receptor ruido | 6,744 | 2,163 | 2,163 | 2,163 | 13,5% | 10,8% |
| R_17 | Receptor ruido | 4,348 | 1,581 | 1,581 | 1,581 | 8,7% | 7,9% |
| R_18 | Receptor ruido | 22,286 | 4,571 | 4,571 | 4,571 | 44,6% | 22,9% |
| R_19 | Receptor ruido | 10,752 | 2,728 | 2,728 | 2,728 | 21,5% | 13,6% |
| R_20 | Receptor ruido | 11,520 | 3,249 | 3,249 | 3,249 | 23,0% | 16,2% |
| R_21 | Receptor ruido | 9,618 | 2,864 | 2,864 | 2,864 | 19,2% | 14,3% |
| R_22 | Receptor ruido | 8,407 | 2,520 | 2,520 | 2,520 | 16,8% | 12,6% |
| R_23 | Receptor ruido | 16,566 | 7,839 | 7,839 | 7,839 | 33,1% | 39,2% |
| R_24 | Receptor ruido | 2,548 | 0,716 | 0,716 | 0,716 | 5,1% | 3,6% |
| R_25 | Receptor ruido | 0,262 | 0,097 | 0,097 | 0,097 | 0,5% | 0,5% |
| R_26 | Receptor ruido | 0,772 | 0,451 | 0,451 | 0,451 | 1,5% | 2,3% |

**Tabla 7-11.: Resultados del modelo de dispersión para MP10 [μg/m** **[3]** **N]. Escenario Sinérgico Fase de****

| Receptor | Descripción | Material Particulado Respirable (MP10) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración**<br>**[μg/m3N]** | **Concentración**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** | **P98 24**<br>**horas** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 2,014 | 0,976 | 130 | 50 | 1,5% | 2,0% |
| R_2 | Estación Tierra Amarilla | 3,176 | 1,602 | 1,602 | 1,602 | 2,4% | 3,2% |
| R_3 | Estación Ojanco | 2,982 | 1,443 | 1,443 | 1,443 | 2,3% | 2,9% |
| R_4 | Estación Kozan | 9,906 | 3,564 | 3,564 | 3,564 | 7,6% | 7,1% |
| R_5 | 133 casa (Carola Norte) | 1,512 | 0,771 | 0,771 | 0,771 | 1,2% | 1,5% |
| R_6 | Iglesia Tierra Amarilla | 2,386 | 1,214 | 1,214 | 1,214 | 1,8% | 2,4% |
| R_7 | El Minero | 9,072 | 3,753 | 3,753 | 3,753 | 7,0% | 7,5% |
| R_8 | Testigoteca | 5,826 | 2,373 | 2,373 | 2,373 | 4,5% | 4,7% |
| R_9 | Estadio | 17,324 | 5,555 | 5,555 | 5,555 | 13,3% | 11,1% |
| R_10 | Agrouva I | 10,725 | 4,050 | 4,050 | 4,050 | 8,3% | 8,1% |
| R_11 | Agrouva II | 3,979 | 2,182 | 2,182 | 2,182 | 3,1% | 4,4% |
| R_12 | Receptor ruido | 8,419 | 4,192 | 4,192 | 4,192 | 6,5% | 8,4% |
| R_13 | Receptor ruido | 5,700 | 2,609 | 2,609 | 2,609 | 4,4% | 5,2% |
| R_14 | Receptor ruido | 5,275 | 2,815 | 2,815 | 2,815 | 4,1% | 5,6% |
| R_15 | Receptor ruido | 10,726 | 3,819 | 3,819 | 3,819 | 8,3% | 7,6% |
| R_16 | Receptor ruido | 12,655 | 4,385 | 4,385 | 4,385 | 9,7% | 8,8% |
| R_17 | Receptor ruido | 9,274 | 3,793 | 3,793 | 3,793 | 7,1% | 7,6% |
| R_18 | Receptor ruido | 38,453 | 8,635 | 8,635 | 8,635 | 29,6% | 17,3% |
| R_19 | Receptor ruido | 20,960 | 6,459 | 6,459 | 6,459 | 16,1% | 12,9% |
| R_20 | Receptor ruido | 20,749 | 6,463 | 6,463 | 6,463 | 16,0% | 12,9% |
| R_21 | Receptor ruido | 16,945 | 5,901 | 5,901 | 5,901 | 13,0% | 11,8% |
| R_22 | Receptor ruido | 18,869 | 7,163 | 7,163 | 7,163 | 14,5% | 14,3% |
| R_23 | Receptor ruido | 62,984 | 29,811 | 29,811 | 29,811 | 48,4% | 59,6% |
| R_24 | Receptor ruido | 9,490 | 2,565 | 2,565 | 2,565 | 7,3% | 5,1% |
| R_25 | Receptor ruido | 0,760 | 0,278 | 0,278 | 0,278 | 0,6% | 0,6% |
| R_26 | Receptor ruido | 1,975 | 1,135 | 1,135 | 1,135 | 1,5% | 2,3% |

**Tabla 7-12.: Resultados del modelo de dispersión para MPS [mg/m** **[2∙]** **día]. Escenario Sinérgico Fase de****

| Receptor | Descripción | Material Particulado Sedimentable (MPS) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Tasa de depositación**<br>**[mg/m2∙día]** | **Tasa de depositación**<br>**[mg/m2∙día]** | **Norma de Calidad**<br>**[mg/m2∙día]** | **Norma de Calidad**<br>**[mg/m2∙día]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **Media**<br>**Anual** | **Máxima**<br>**Media**<br>**Mensual** | **Conf. Suiza** | **República**<br>**Argentina** | **Conf. Suiza** | **República**<br>**Argentina** |
| R_1 | Estación Luis Uribe | 1,373 | 2,340 | 200 | 333 | 0,7% | 0,7% |
| R_2 | Estación Tierra Amarilla | 2,239 | 3,802 | 3,802 | 3,802 | 1,1% | 1,1% |
| R_3 | Estación Ojanco | 1,642 | 2,393 | 2,393 | 2,393 | 0,8% | 0,7% |
| R_4 | Estación Kozan | 14,456 | 17,876 | 17,876 | 17,876 | 7,2% | 5,4% |
| R_5 | 133 casa (Carola Norte) | 1,312 | 1,514 | 1,514 | 1,514 | 0,7% | 0,5% |
| R_6 | Iglesia Tierra Amarilla | 1,627 | 2,949 | 2,949 | 2,949 | 0,8% | 0,9% |
| R_7 | El Minero | 12,039 | 15,482 | 15,482 | 15,482 | 6,0% | 4,6% |
| R_8 | Testigoteca | 7,571 | 9,082 | 9,082 | 9,082 | 3,8% | 2,7% |
| R_9 | Estadio | 14,817 | 16,336 | 16,336 | 16,336 | 7,4% | 4,9% |
| R_10 | Agrouva I | 11,158 | 11,990 | 11,990 | 11,990 | 5,6% | 3,6% |
| R_11 | Agrouva II | 5,861 | 7,085 | 7,085 | 7,085 | 2,9% | 2,1% |
| R_12 | Receptor ruido | 18,134 | 23,004 | 23,004 | 23,004 | 9,1% | 6,9% |
| R_13 | Receptor ruido | 9,560 | 11,365 | 11,365 | 11,365 | 4,8% | 3,4% |
| R_14 | Receptor ruido | 11,566 | 12,779 | 12,779 | 12,779 | 5,8% | 3,8% |
| R_15 | Receptor ruido | 11,416 | 16,176 | 16,176 | 16,176 | 5,7% | 4,9% |
| R_16 | Receptor ruido | 12,598 | 18,192 | 18,192 | 18,192 | 6,3% | 5,5% |
| R_17 | Receptor ruido | 13,335 | 16,239 | 16,239 | 16,239 | 6,7% | 4,9% |
| R_18 | Receptor ruido | 24,047 | 30,275 | 30,275 | 30,275 | 12,0% | 9,1% |
| R_19 | Receptor ruido | 18,750 | 21,228 | 21,228 | 21,228 | 9,4% | 6,4% |
| R_20 | Receptor ruido | 15,807 | 17,877 | 17,877 | 17,877 | 7,9% | 5,4% |
| R_21 | Receptor ruido | 13,218 | 14,848 | 14,848 | 14,848 | 6,6% | 4,5% |
| R_22 | Receptor ruido | 35,927 | 42,816 | 42,816 | 42,816 | 18,0% | 12,9% |
| R_23 | Receptor ruido | 107,610 | 131,339 | 131,339 | 131,339 | 53,8% | 39,4% |
| R_24 | Receptor ruido | 4,713 | 5,621 | 5,621 | 5,621 | 2,4% | 1,7% |
| R_25 | Receptor ruido | 0,278 | 0,358 | 0,358 | 0,358 | 0,1% | 0,1% |

**Tabla 7-13.: Resultados del modelo de dispersión para CO [mg/m** **[3]** **N]. Escenario Sinérgico Fase de****

| Receptor | Descripción | Monóxido de Carbono (CO) | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración**<br>**[mg/m3N]** | **Concentración**<br>**[mg/m3N]** | **Norma de Calidad**<br>**[mg/m3N]** | **Norma de Calidad**<br>**[mg/m3N]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P99 1 hora** | **P99 8**<br>**horas** | **P99 1 hora** | **P99 8**<br>**horas** | **P99 1 hora** | **P99 8**<br>**horas** |
| R_1 | Estación Luis Uribe | 0,006 | 0,003 | 30 | 10 | 0,0% | 0,0% |
| R_2 | Estación Tierra Amarilla | 0,010 | 0,004 | 0,004 | 0,004 | 0,0% | 0,0% |
| R_3 | Estación Ojanco | 0,016 | 0,004 | 0,004 | 0,004 | 0,1% | 0,0% |
| R_4 | Estación Kozan | 0,037 | 0,013 | 0,013 | 0,013 | 0,1% | 0,1% |
| R_5 | 133 casa (Carola Norte) | 0,006 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% |
| R_6 | Iglesia Tierra Amarilla | 0,006 | 0,003 | 0,003 | 0,003 | 0,0% | 0,0% |
| R_7 | El Minero | 0,076 | 0,014 | 0,014 | 0,014 | 0,3% | 0,1% |
| R_8 | Testigoteca | 0,056 | 0,010 | 0,010 | 0,010 | 0,2% | 0,1% |
| R_9 | Estadio | 0,146 | 0,028 | 0,028 | 0,028 | 0,5% | 0,3% |
| R_10 | Agrouva I | 0,081 | 0,016 | 0,016 | 0,016 | 0,3% | 0,2% |
| R_11 | Agrouva II | 0,020 | 0,005 | 0,005 | 0,005 | 0,1% | 0,0% |
| R_12 | Receptor ruido | 0,059 | 0,012 | 0,012 | 0,012 | 0,2% | 0,1% |
| R_13 | Receptor ruido | 0,051 | 0,010 | 0,010 | 0,010 | 0,2% | 0,1% |
| R_14 | Receptor ruido | 0,033 | 0,007 | 0,007 | 0,007 | 0,1% | 0,1% |
| R_15 | Receptor ruido | 0,087 | 0,016 | 0,016 | 0,016 | 0,3% | 0,2% |
| R_16 | Receptor ruido | 0,102 | 0,019 | 0,019 | 0,019 | 0,3% | 0,2% |
| R_17 | Receptor ruido | 0,069 | 0,014 | 0,014 | 0,014 | 0,2% | 0,1% |
| R_18 | Receptor ruido | 0,311 | 0,063 | 0,063 | 0,063 | 1,0% | 0,6% |
| R_19 | Receptor ruido | 0,159 | 0,031 | 0,031 | 0,031 | 0,5% | 0,3% |
| R_20 | Receptor ruido | 0,203 | 0,034 | 0,034 | 0,034 | 0,7% | 0,3% |
| R_21 | Receptor ruido | 0,169 | 0,030 | 0,030 | 0,030 | 0,6% | 0,3% |
| R_22 | Receptor ruido | 0,098 | 0,028 | 0,028 | 0,028 | 0,3% | 0,3% |
| R_23 | Receptor ruido | 0,155 | 0,051 | 0,051 | 0,051 | 0,5% | 0,5% |
| R_24 | Receptor ruido | 0,039 | 0,009 | 0,009 | 0,009 | 0,1% | 0,1% |
| R_25 | Receptor ruido | 0,002 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% |
| R_26 | Receptor ruido | 0,012 | 0,006 | 0,006 | 0,006 | 0,0% | 0,1% |

**Tabla 7-14.: Resultados del modelo de dispersión para NO** **2** **[μg/m** **[3]** **N]. Escenario Sinérgico Fase de****

| Receptor | Descripción | Dióxido de Nitrógeno (NO )<br>2 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración**<br>**[μg/m3N]** | **Concentración**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Norma de Calidad**<br>**[μg/m3N]** | **Porcentaje de la Norma**<br>**de Calidad** | **Porcentaje de la Norma**<br>**de Calidad** |
| **Receptor** | **Descripción** | **P99 1 hora** | **Período**<br>**Anual** | **P99 1 hora** | **Período**<br>**Anual** | **P99 1 hora** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 7,531 | 0,732 | 400 | 100 | 1,9% | 0,7% |
| R_2 | Estación Tierra Amarilla | 13,661 | 1,221 | 1,221 | 1,221 | 3,4% | 1,2% |
| R_3 | Estación Ojanco | 18,093 | 1,357 | 1,357 | 1,357 | 4,5% | 1,4% |
| R_4 | Estación Kozan | 35,882 | 1,911 | 1,911 | 1,911 | 9,0% | 1,9% |
| R_5 | 133 casa (Carola Norte) | 5,646 | 0,446 | 0,446 | 0,446 | 1,4% | 0,4% |
| R_6 | Iglesia Tierra Amarilla | 7,527 | 0,864 | 0,864 | 0,864 | 1,9% | 0,9% |
| R_7 | El Minero | 55,415 | 1,713 | 1,713 | 1,713 | 13,9% | 1,7% |
| R_8 | Testigoteca | 39,039 | 1,218 | 1,218 | 1,218 | 9,8% | 1,2% |
| R_9 | Estadio | 108,880 | 2,920 | 2,920 | 2,920 | 27,2% | 2,9% |
| R_10 | Agrouva I | 64,202 | 2,472 | 2,472 | 2,472 | 16,1% | 2,5% |
| R_11 | Agrouva II | 21,993 | 1,722 | 1,722 | 1,722 | 5,5% | 1,7% |
| R_12 | Receptor ruido | 45,341 | 1,687 | 1,687 | 1,687 | 11,3% | 1,7% |
| R_13 | Receptor ruido | 39,923 | 1,278 | 1,278 | 1,278 | 10,0% | 1,3% |
| R_14 | Receptor ruido | 22,312 | 1,281 | 1,281 | 1,281 | 5,6% | 1,3% |
| R_15 | Receptor ruido | 45,854 | 1,564 | 1,564 | 1,564 | 11,5% | 1,6% |
| R_16 | Receptor ruido | 61,936 | 1,818 | 1,818 | 1,818 | 15,5% | 1,8% |
| R_17 | Receptor ruido | 45,969 | 1,614 | 1,614 | 1,614 | 11,5% | 1,6% |
| R_18 | Receptor ruido | 224,180 | 3,829 | 3,829 | 3,829 | 56,0% | 3,8% |
| R_19 | Receptor ruido | 126,800 | 3,084 | 3,084 | 3,084 | 31,7% | 3,1% |
| R_20 | Receptor ruido | 141,250 | 3,291 | 3,291 | 3,291 | 35,3% | 3,3% |
| R_21 | Receptor ruido | 123,410 | 2,906 | 2,906 | 2,906 | 30,9% | 2,9% |
| R_22 | Receptor ruido | 81,598 | 2,840 | 2,840 | 2,840 | 20,4% | 2,8% |
| R_23 | Receptor ruido | 45,229 | 2,783 | 2,783 | 2,783 | 11,3% | 2,8% |
| R_24 | Receptor ruido | 17,104 | 0,751 | 0,751 | 0,751 | 4,3% | 0,8% |
| R_25 | Receptor ruido | 2,146 | 0,169 | 0,169 | 0,169 | 0,5% | 0,2% |
| R_26 | Receptor ruido | 15,932 | 1,651 | 1,651 | 1,651 | 4,0% | 1,7% |
| R_27 | Estación COEMIN | 41,577 | 2,166 | 2,166 | 2,166 | 10,4% | 2,2% |

**Tabla 7-15.: Resultados del modelo de dispersión para SO** **2** **[μg/m** **[3]** **N]. Escenario Sinérgico Fase de Operación Proyectada.****

| Receptor | Descripción | Dióxido de Azufre (SO )<br>2 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Descripción** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Concentración [μg/m3N]** | **Norma de Calidad [μg/m3N]** | **Norma de Calidad [μg/m3N]** | **Norma de Calidad [μg/m3N]** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** | **Porcentaje de la Norma de Calidad** |
| **Receptor** | **Descripción** | **P99 1 hora** | **P99 24**<br>**horas** | **Período**<br>**Anual** | **P99 1 hora** | **P99 24**<br>**horas** | **Período**<br>**Anual** | **P99 1 hora** | **P99 24**<br>**horas** | **Período**<br>**Anual** |
| R_1 | Estación Luis Uribe | 0,011 | 0,004 | 0,002 | 350 | 150 | 60 | 0,0% | 0,0% | 0,0% |
| R_2 | Estación Tierra Amarilla | 0,018 | 0,006 | 0,003 | 0,003 | 0,003 | 0,003 | 0,0% | 0,0% | 0,0% |
| R_3 | Estación Ojanco | 0,022 | 0,005 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_4 | Estación Kozan | 0,070 | 0,018 | 0,006 | 0,006 | 0,006 | 0,006 | 0,0% | 0,0% | 0,0% |
| R_5 | 133 casa (Carola Norte) | 0,008 | 0,002 | 0,001 | 0,001 | 0,001 | 0,001 | 0,0% | 0,0% | 0,0% |
| R_6 | Iglesia Tierra Amarilla | 0,013 | 0,004 | 0,002 | 0,002 | 0,002 | 0,002 | 0,0% | 0,0% | 0,0% |
| R_7 | El Minero | 0,075 | 0,018 | 0,007 | 0,007 | 0,007 | 0,007 | 0,0% | 0,0% | 0,0% |
| R_8 | Testigoteca | 0,051 | 0,015 | 0,004 | 0,004 | 0,004 | 0,004 | 0,0% | 0,0% | 0,0% |
| R_9 | Estadio | 0,110 | 0,038 | 0,008 | 0,008 | 0,008 | 0,008 | 0,0% | 0,0% | 0,0% |
| R_10 | Agrouva I | 0,060 | 0,021 | 0,006 | 0,006 | 0,006 | 0,006 | 0,0% | 0,0% | 0,0% |
| R_11 | Agrouva II | 0,024 | 0,007 | 0,004 | 0,004 | 0,004 | 0,004 | 0,0% | 0,0% | 0,0% |
| R_12 | Receptor ruido | 0,095 | 0,019 | 0,009 | 0,009 | 0,009 | 0,009 | 0,0% | 0,0% | 0,0% |
| R_13 | Receptor ruido | 0,051 | 0,015 | 0,005 | 0,005 | 0,005 | 0,005 | 0,0% | 0,0% | 0,0% |
| R_14 | Receptor ruido | 0,045 | 0,011 | 0,005 | 0,005 | 0,005 | 0,005 | 0,0% | 0,0% | 0,0% |
| R_15 | Receptor ruido | 0,118 | 0,020 | 0,007 | 0,007 | 0,007 | 0,007 | 0,0% | 0,0% | 0,0% |
| R_16 | Receptor ruido | 0,145 | 0,026 | 0,008 | 0,008 | 0,008 | 0,008 | 0,0% | 0,0% | 0,0% |
| R_17 | Receptor ruido | 0,090 | 0,019 | 0,007 | 0,007 | 0,007 | 0,007 | 0,0% | 0,0% | 0,0% |
| R_18 | Receptor ruido | 0,291 | 0,069 | 0,015 | 0,015 | 0,015 | 0,015 | 0,1% | 0,0% | 0,0% |

**Tabla 7-16.: Análisis de Significancia Fase de Operación Sinérgica. MP10** **[μg/m** **[3]** **N]** **.****

| Receptor | Nivel de Impacto Significativo | Col3 | Col4 | Escenario Actual | Col6 | Escenario Proyectado | Col8 | Variación | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Receptor** | **Estadígrafo** | **Valor** | **Unidad** | **Valor** | **% SILs** | **Valor** | **% SILs** | **Valor** | **% SILs** |
| R_1 | P98 24 horas | 5 | μg/m3N | 2,12 | 42,5% | 2,01 | 40,3% | 0,00 | 0,0% |
| R_1 | Media anual | 1 | μg/m3N | 1,05 | 105,1% | 0,98 | 97,6% | 0,00 | 0,0% |
| R_2 | P98 24 horas | 5 | μg/m3N | 3,31 | 66,1% | 3,18 | 63,5% | 0,00 | 0,0% |
| R_2 | Media anual | 1 | μg/m3N | 1,69 | 168,9% | 1,60 | 160,2% | 0,00 | 0,0% |
| R_3 | P98 24 horas | 5 | μg/m3N | 3,18 | 63,6% | 2,98 | 59,6% | 0,00 | 0,0% |
| R_3 | Media anual | 1 | μg/m3N | 1,63 | 163,4% | 1,44 | 144,3% | 0,00 | 0,0% |
| R_4 | P98 24 horas | 5 | μg/m3N | 11,37 | 227,3% | 9,91 | 198,1% | 0,00 | 0,0% |
| R_4 | Media anual | 1 | μg/m3N | 4,35 | 435,5% | 3,56 | 356,4% | 0,00 | 0,0% |
| R_5 | P98 24 horas | 5 | μg/m3N | 2,02 | 40,4% | 1,51 | 30,2% | 0,00 | 0,0% |
| R_5 | Media anual | 1 | μg/m3N | 1,11 | 110,6% | 0,77 | 77,1% | 0,00 | 0,0% |
| R_6 | P98 24 horas | 5 | μg/m3N | 2,56 | 51,2% | 2,39 | 47,7% | 0,00 | 0,0% |
| R_6 | Media anual | 1 | μg/m3N | 1,32 | 132,2% | 1,21 | 121,4% | 0,00 | 0,0% |
| R_7 | P98 24 horas | 5 | μg/m3N | 10,23 | 204,6% | 9,07 | 181,4% | 0,00 | 0,0% |
| R_7 | Media anual | 1 | μg/m3N | 4,39 | 439,3% | 3,75 | 375,3% | 0,00 | 0,0% |

**Tabla 7-17.: Concentración/ Depositación Total Sinérgica Proyectada. Estación Tierra Amarilla.****

| Contaminante | Normativa Vigente | Col3 | Col4 | Línea de Base<br>Proyectada | Col6 | Aportes Sinérgicos de<br>Proyectos | Col8 | Concentración/<br>Depositación Total<br>Sinérgica Proyectada | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Estadígrafo** | **Valor** | **Unidad** | **Valor** | **% Norma** | **Valor** | **% Norma** | **Valor** | **% Norma** |
| Material Particulado<br>Respirable Fino<br>(MP2.5) | P98 24 horas | 50 | μg/m3N | 31,4 | 62,8% | 0,1 | 0,1% | 31,5 | 62,9% |
| Material Particulado<br>Respirable Fino<br>(MP2.5) | Media anual | 20 | μg/m3N | 14,2 | 70,9% | 0,0 | 0,2% | 14,2 | 71,1% |
| Material Particulado<br>Respirable (MP10) | P98 24 horas | 130 | μg/m3N | 125,4 | 96,5% | 0,0 | 0,0% | 125,4 | 96,5% |
| Material Particulado<br>Respirable (MP10) | Media anual | 50 | μg/m3N | 56,4 | 112,7% | 0,0 | 0,0% | 56,4 | 112,7% |
| Material Particulado<br>Sedimentable (MPS) | Media mensual | 333 | mg/m2día | 356,0 | 106,9% | 0,0 | 0,0% | 356,0 | 106,9% |
| Material Particulado<br>Sedimentable (MPS) | Media anual | 200 | mg/m2día | 226,8 | 113,4% | 0,0 | 0,0% | 226,8 | 113,4% |

**Tabla 7-18.: Concentración Total Sinérgica Proyectada. Estación Luis Uribe.****

| Contaminante | Normativa Vigente | Col3 | Col4 | Línea de Base<br>Proyectada | Col6 | Aportes Sinérgicos de<br>Proyectos | Col8 | Concentración Total<br>Sinérgica Proyectada | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Estadígrafo** | **Valor** | **Unidad** | **Valor** | **% Norma** | **Valor** | **% Norma** | **Valor** | **% Norma** |
| Material Particulado<br>Respirable Fino<br>(MP2.5) | P98 24 horas | 50 | μg/m3N | 14,0 | 28,0% | 0,0 | 0,1% | 14,0 | 28,1% |
| Material Particulado<br>Respirable Fino<br>(MP2.5) | Media anual | 20 | μg/m3N | 8,7 | 43,5% | 0,0 | 0,1% | 8,7 | 43,6% |
| Material Particulado<br>Respirable (MP10) | P98 24 horas | 130 | μg/m3N | 74,2 | 57,1% | 0,0 | 0,0% | 74,2 | 57,1% |
| Material Particulado<br>Respirable (MP10) | Media anual | 50 | μg/m3N | 49,1 | 98,2% | 0,0 | 0,0% | 49,1 | 98,2% |

**Tabla 7-19.: Concentración Total Sinérgica Proyectada. Estación Kozan.****

| Contaminante | Normativa Vigente | Col3 | Col4 | Línea de Base<br>Proyectada | Col6 | Aportes Sinérgicos de<br>Proyecto | Col8 | Concentración Total<br>Sinérgica Proyectada | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Estadígrafo** | **Valor** | **Unidad** | **Valor** | **% Norma** | <br>**Valor** | **% Norma** | <br>**Valor** | **% Norma** |
| Material Particulado<br>Respirable (MP10) | P98 24 horas | 130 | μg/m3N | 96,0 | 73,8% | 1,9 | 1,5% | 97,9 | 75,3% |
| Material Particulado<br>Respirable (MP10) | Media anual | 50 | μg/m3N | 45,8 | 91,6% | 0,9 | 1,8% | 46,7 | 93,4% |

**Tabla 7-22.: Concentración Total Sinérgica Proyectada. Estación Nantoco.****

| Contaminante | Normativa Vigente | Col3 | Col4 | Línea de Base<br>Proyectada | Col6 | Aportes Sinérgicos de<br>Proyecto | Col8 | Concentración Total<br>Sinérgica Proyectada | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Estadígrafo** | **Valor** | **Unidad** | **Valor** | **% Norma** | **Valor** | **% Norma** | **Valor** | **% Norma** |
| Material Particulado<br>Respirable (MP10) | P98 24 horas | 130 | μg/m3N | 54,0 | 41,5% | 0,0 | 0,0% | 54,0 | 41,5% |
| Material Particulado<br>Respirable (MP10) | Media anual | 50 | μg/m3N | 39,5 | 79,0% | 0,0 | 0,0% | 39,5 | 79,0% |

**Tabla 7-27.: Concentración Total Sinérgica Proyectada. Estación C1.****

| Contaminante | Normativa Vigente | Col3 | Col4 | Línea de Base<br>Proyectada | Col6 | Aportes Sinérgicos de<br>Proyecto | Col8 | Concentración Total<br>Sinérgica Proyectada | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Contaminante** | **Estadígrafo** | **Valor** | **Unidad** | **Valor** | **% Norma** | **Valor** | **% Norma** | **Valor** | **% Norma** |
| Material Particulado<br>Respirable (MP10) | P98 24 horas | 130 | μg/m3N | 61,0 | 46,9% | 0,0 | 0,0% | 61,0 | 46,9% |
| Material Particulado<br>Respirable (MP10) | Media anual | 50 | μg/m3N | 53,2 | 106,4% | 0,0 | 0,0% | 53,2 | 106,4% |

**Tabla 8-1.: Archivos de modelación entregados.****

| Archivos | Entregado | Observación |
| --- | --- | --- |
| **Archivos CALPUFF** | **Archivos CALPUFF** | **Archivos CALPUFF** |
| CALPUFF.DAT | NO | Corresponde al archivo CONC.DAT |
| CALPUFF.LST | SI | - |
| CALPUFF.INP | SI | - |
| CONC.DAT | SI | - |
| DFLX.DAT | SI | - |
| WFLX.DAT | NO | - |
| **Archivos Meteorológicos CALMET** | **Archivos Meteorológicos CALMET** | **Archivos Meteorológicos CALMET** |
| CALMET.DAT | SI | Corresponde al archivo:calmetv6_Tierra_Amarilla.dat |
| GEO.DAT | SI | - |
| SURF.DAT | NO | No fueron utilizados debido a que se usó, directamente<br>en CALPUFF, la meteorología proveniente del modelo<br>meteorológico WRF. |
| UP.DAT | NO | NO |
| CALMET.LST | NO | NO |
| CALMET.INP | NO | NO |
| namelist.wps | SI | Archivo de configuración de preproceso de WRF (WPS) |
| namelist.input | SI | Archivo de configuración de WRF |
| **Archivos CALPOST** | **Archivos CALPOST** | **Archivos CALPOST** |
| CALPOST.DAT | SI | Los archivos se presentan en forma separada según<br>contaminantes y periodo. |
| CALPOST.LST | SI | SI |
| CALPOST.INP | SI | SI |
| **Archivos Complementarios** | **Archivos Complementarios** | **Archivos Complementarios** |
| -Coastline Data File, Dry Flux Data File,<br>Wet Flux Data File, Ozone Data File,<br>Chem Data File. | NO | No se incluyen, debido a que corresponden a datos que no<br>fueron modelados. |
