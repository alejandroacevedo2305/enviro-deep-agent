---
title: Sin título
author: Argis
date: D:20240612115135-04'00'
language: es
type: report
pages: 253
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Informe Modelación de Calidad de Aire Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo
-->

## ADENDA COMPLEMENTARIA ANEXO OBS. 071a MODELACIÓN CALIDAD DEL AIRE PARTE 1

Declaración de Impacto Ambiental

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo
Adenda Complementaria

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Fecha Abril de 2024
Servidas Localidad de Maitencillo
Página 1 de 252

# Informe Modelación de Calidad de Aire Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo

#### Proyecto : 0126 Cliente: ESVAL S.A. Dirigido a : Mario Figueroa

CONTROL INTERNO **www.arechile.com**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 2 de 252

**CONTROL INTERNO**

Proyecto Redes Primarias y Planta de Tratamiento de
Proyecto
Aguas Servidas Localidad de Maitencillo

ID Proyecto MC-0126

Servicio Modelación de Calidad del Aire

Solicitado por : ESVAL S.A.

Mario Figueroa
Contacto:

Jefe Depto. Calidad y Medio Ambiente

Preparado por: Are Project SpA.

Aprobado por: Gerardo González - Gerente General

Fecha: Abril de 2024

|Versión del documento|Descripción|Fecha|
|---|---|---|
|V0.1|Reporte borrador|15-abr-2024|
||||

|Elaboración|Col2|Aprobación|Col4|
|---|---|---|---|
|Nombre|Oscar<br>Santamaría|Nombre|Gerardo<br>González|
|Cargo|Ingeniero<br>de<br>Proyectos|Cargo|Gerente<br>General|
|Fecha|15-abr-2024|Fecha|16-abr-2024|
|Firma||Firma||

CONTROL INTERNO **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 3 de 252

**ÍNDICE**

CONTROL INTERNO .......................................................................................................................... 2
ÍNDICE ................................................................................................................................................ 3
1 INTRODUCCIÓN ........................................................................................................................ 11
1.1 DESCRIPCIÓN DEL PROYECTO ...................................................................................... 11
1.2 ANTECEDENTES ESPECÍFICOS ...................................................................................... 13
2 OBJETIVOS................................................................................................................................ 14
2.1 OBJETIVO GENERAL ........................................................................................................ 14
2.2 OBJETIVOS ESPECÍFICOS ............................................................................................... 14
3 JUSTIFICACIÓN Y DESCRIPCIÓN DEL MODELO .................................................................... 15
3.1 JUSTIFICACIÓN DEL MODELO ........................................................................................ 15
3.2 DESCRIPCIÓN DEL MODELO .......................................................................................... 17
3.3 PROCESO DE MODELACIÓN ........................................................................................... 17
4 CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN ........................................................... 19
4.1 DOMINIO DE MODELACIÓN ............................................................................................. 19
4.2 BASE METEOROLÓGICA ................................................................................................. 21
4.2.1 PERIODO DE MODELACIÓN ........................................................................................ 21
4.2.2 FUENTE DE DATOS METEOROLÓGICOS ................................................................... 21
4.2.3 DATOS TOPOGRÁFICOS Y DE USO DE SUELO ......................................................... 21
4.2.4 CONFIGURACIÓN DEL MODELO ................................................................................. 23
4.2.5 PARAMETRIZACIÓN RECEPTORES ............................................................................ 24
5 FUENTES DE EMISIÓN ............................................................................................................. 25
6 LÍNEA DE BASE ......................................................................................................................... 26
6.1 NORMATIVA APLICABLE .................................................................................................. 26
6.2 BASE DE DATOS RED DE MONITOREO VENTANAS ...................................................... 27
6.3 ANÁLISIS VARIABILIDAD TEMPORAL CONTAMINANTES .............................................. 28
6.4 ANÁLISIS DE RESULTADOS DE LÍNEA BASE DE CALIDAD DEL AIRE ESTIMADA ....... 39
7 EMISIONES ATMOSFÉRICAS ................................................................................................... 43
7.1 IDENTIFICACIÓN DE FUENTES DE EMISIÓN .................................................................. 43
7.2 TASAS DE EMISIÓN .......................................................................................................... 43
7.3 CONFORMACIÓN DE ESCENARIOS DE MODELACIÓN ................................................. 44
7.4 OTRAS CONSIDERACIONES ........................................................................................... 49
8 RECEPTORES DISCRETOS...................................................................................................... 50
9 ANÁLISIS DE INCERTIDUMBRE ............................................................................................... 55
9.1 DESCRIPCIÓN DEL ANÁLISIS CUALITATIVO Y CUANTITATIVO .................................... 57
9.2 ANÁLISIS CUALITATIVO: VELOCIDAD DEL VIENTO ....................................................... 59
9.2.1 VELOCIDAD DEL VIENTO ESTACIÓN PUCHUNCAVÍ.................................................. 59
9.2.2 VELOCIDAD DEL VIENTO ESTACIÓN LA GREDA ....................................................... 62
9.2.3 VELOCIDAD DEL VIENTO ESTACIÓN VENTANAS ...................................................... 65
9.3 ANÁLISIS CUALITATIVO: DIRECCIÓN DEL VIENTO ....................................................... 68
9.3.1 DIRECCIÓN DEL VIENTO ESTACIÓN PUCHUNCAVÍ .................................................. 68
9.3.2 DIRECCIÓN DEL VIENTO ESTACIÓN LA GREDA ........................................................ 70
9.3.3 DIRECCIÓN DEL VIENTO ESTACIÓN VENTANAS ...................................................... 72
9.3.4 ROSAS DE VIENTO ESTACIÓN PUCHUNCAVÍ ............................................................ 74
9.3.5 ROSAS DE VIENTO CICLO ANUAL HORARIO ESTACIÓN PUCHUNCAVÍ .................. 75
9.3.6 ROSAS DE VIENTO ESTACIÓN LA GREDA ................................................................. 76
9.3.7 ROSAS DE VIENTO CICLO ANUAL HORARIO ESTACIÓN LA GREDA ....................... 77
9.3.8 ROSAS DE VIENTO ESTACIÓN VENTANAS ................................................................ 78
9.3.9 ROSAS DE VIENTO CICLO ANUAL HORARIO ESTACIÓN VENTANAS ...................... 79
9.4 ANÁLISIS CUANTITATIVO ................................................................................................ 80

ÍNDICE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 4 de 252

10 ANÁLISIS DE RESULTADOS INCERTIDUMBRE DEL MODELO .............................................. 80
11 RESULTADOS DE MODELACIÓN ETAPA DE CONSTRUCCIÓN ............................................. 81

11.1 CONCENTRACIONES DE MATERIAL PARTICULADO FINO (MP 2,5 ) EN RECEPTORES
SENSIBLES .................................................................................................................................... 82
11.2 CONCENTRACIONES DE MATERIAL PARTICULADO RESPIRABLE (MP 10 ) EN
RECEPTORES SENSIBLES .......................................................................................................... 83
11.3 CONCENTRACIONES DE DIÓXIDO DE AZUFRE (SO 2 ) NORMA PRIMARIA EN
RECEPTORES SENSIBLES .......................................................................................................... 84
11.4 CONCENTRACIONES DE DIÓXIDO DE AZUFRE (SO 2 ) NORMA SECUNDARIA EN
RECEPTORES SENSIBLES .......................................................................................................... 85
11.5 CONCENTRACIONES DE MONÓXIDO DE CARBONO (CO) NORMA PRIMARIA EN
RECEPTORES SENSIBLES .......................................................................................................... 86
11.6 CONCENTRACIONES DE DIÓXIDO DE NITRÓGENO (NO2) NORMA PRIMARIA EN
RECEPTORES SENSIBLES .......................................................................................................... 87
11.7 APORTE DEL PROYECTO A LAS CONCENTRACIONES BASALES ............................... 88
12 CONCLUSIONES ....................................................................................................................... 89
13 BIBLIOGRAFÍA ........................................................................................................................... 92
14 ANEXO 1 - MODELACIÓN MATERIAL PARTICULADO SEDIMENTABLE ................................ 94
15 ANEXO 2 - ANÁLISIS GUÍA: CRITERIO DE EVALUACIÓN EN EL SEIA - IMPACTO DE
EMISIONES EN ZONAS SATURADAS POR MATERIAL PARTICULADO RESPIRABLE MP 10 Y
MATERIAL PARTICULADO FINO RESPIRABLE MP 2.5 ................................................................................................................. 97

15.1 EVALUACIÓN DEL IMPACTO DE LAS EMISIONES ATMOSFÉRICAS DE MATERIAL
PARTICULADO RESPIRABLE SOBRE EL RIESGO PARA LA SALUD DE LA POBLACIÓN EN EL

MARCO DEL SEIA ......................................................................................................................... 97
15.2 CARACTERIZACIÓN DE LOS NIVELES DE MP 10 Y MP 2,5 EN LOS RECEPTORES
HUMANOS DEL ÁREA DE INFLUENCIA ....................................................................................... 98

15.3 CRITERIOS PARA EVALUAR LA SIGNIFICANCIA DEL APORTE DE EMISIONES DE
MATERIAL PARTICULADO RESPIRABLE, MP 10 y MP 2,5 ....................................................................................................... 99
16 ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP 2,5, MP 10, SO 2, CO y NO 2 ............................................ 101

16.1 ESCENARIO 1 - ISOLÍNEAS DE CONCENTRACIÓN MP 2,5, MP 10, SO 2, CO Y NO 2 .............. 102
16.2 ESCENARIO 2 - ISOLÍNEAS DE CONCENTRACIÓN MP 2,5, MP 10 SO 2 CO Y NO 2 ................. 115
16.3 ESCENARIO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP 2,5, MP 10 SO 2 CO Y NO 2 ................. 128
16.4 ESCENARIO 4 - ISOLÍNEAS DE CONCENTRACIÓN MP 2,5, MP 10 SO 2 CO Y NO 2 ................. 141
16.5 ESCENARIO 5 - ISOLÍNEAS DE CONCENTRACIÓN MP 2,5, MP 10 SO 2 CO Y NO 2 ................. 154
17 ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN .................................... 167

17.1 FUENTES DE EMISIÓN - ESCENARIO 1 ........................................................................ 167
17.2 FUENTES DE EMISIÓN - ESCENARIO 2 ........................................................................ 194
17.3 FUENTES DE EMISIÓN - ESCENARIO 3 ........................................................................ 206
17.4 FUENTES DE EMISIÓN - ESCENARIO 4 ........................................................................ 217
17.5 FUENTES DE EMISIÓN - ESCENARIO 5 ........................................................................ 239

ÍNDICE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 5 de 252

**ÍNDICE DE TABLAS**
Tabla 1. Análisis porcentual de vientos calmos - Estación Puchuncaví ............................................. 19
Tabla 2. Parametrización grilla 1 receptores ...................................................................................... 24
Tabla 3. Parametrización grilla 2 receptores ...................................................................................... 24
Tabla 4. Parametrización grilla 3 receptores ...................................................................................... 24
Tabla 5. Parametrización grilla 4 receptores ...................................................................................... 24
Tabla 6. Parametrización grilla 5 receptores ...................................................................................... 24
Tabla 7. Normas de Calidad del Aire vigentes aplicables a la zona de estudio ................................... 26
Tabla 8. Estaciones de Calidad del Aire ............................................................................................. 27
Tabla 9. Porcentaje de datos en válidos - Estaciones de Calidad del Aire .......................................... 28
Tabla 10. Estadísticos de Comparación Norma Primaria MP 2,5 ................................................................................................ 40
Tabla 11. Estadísticos de Comparación Normas Primaria MP 10 .............................................................................................. 40
Tabla 12. Estadísticos de Comparación Normas Primaria SO 2 ................................................................................................ 41
Tabla 13. Estadísticos de Comparación Normas Secundaria SO 2 ........................................................................................ 41
Tabla 14. Estadísticos de Comparación Normas Primaria NO 2 ................................................................................................ 42
Tabla 15. Estadísticos de Comparación Normas Primaria CO............................................................ 42
Tabla 16. Actividades y tipología de fuentes ...................................................................................... 43
Tabla 17. Escenarios de modelación .................................................................................................. 44
Tabla 18. Actividades del proyecto y Emisiones Etapa 1 y 2 .............................................................. 45
Tabla 19. Actividades del proyecto y Emisiones Etapa 3 y 4 .............................................................. 46
Tabla 20. Actividades del proyecto y Emisiones Etapa PTAS 1 y 2 .................................................... 47
Tabla 21. Actividades del proyecto y Emisiones Etapa PTAS 3 ......................................................... 48
Tabla 22. Receptores discretos parte 1 .............................................................................................. 50
Tabla 23. Receptores discretos parte 2 .............................................................................................. 51
Tabla 24. Receptores discretos parte 3 .............................................................................................. 52
Tabla 25. Receptores discretos parte 4 .............................................................................................. 53
Tabla 26. Coordenadas de ubicación estaciones meteorológicas superficiales .................................. 55
Tabla 27. Porcentaje de datos validados en estaciones meteorológicas superficiales ........................ 56
Tabla 28. Rosa de viento ciclo anual modelada y observada Estación Puchuncaví ........................... 74
Tabla 29. Rosas de viento anual horario Estación Puchuncaví .......................................................... 75
Tabla 30. Rosa de viento ciclo anual modelada y observada Estación La Greda ............................... 76
Tabla 31. Rosas de viento anual horario - Estación La Greda ........................................................... 77
Tabla 32. Rosa de viento ciclo anual modelada y observada Estación Ventanas ............................... 78
Tabla 33. Rosas de viento anual horario - Estación Ventanas ........................................................... 79
Tabla 34 Estadísticos velocidad del viento ......................................................................................... 80

Tabla 35 Estadísticos dirección del viento .......................................................................................... 80
Tabla 36. Escenarios modelación ...................................................................................................... 81
Tabla 37. Norma MP 2,5 [μg/m [3] ] - Promedio 24 horas - Percentil 98 ................................................... 82
Tabla 38. Norma MP 2,5 [μg/m [3] ] - Promedio Anual .............................................................................. 82
Tabla 39. Norma MP 10 [μg/m [3] ] - Promedio 24 horas - Percentil 98 ................................................... 83
Tabla 40. Norma MP 10 [μg/m [3] ] - Promedio Anual ............................................................................... 83
Tabla 41. Norma primaria SO 2 [μg/m [3] ] - Promedio 1 hora - Percentil 98,5 ........................................ 84
Tabla 42. Norma primaria SO 2 [μg/m [3] ] - Promedio 24 horas - Percentil 99 ....................................... 84
Tabla 43. Norma primaria SO 2 [μg/m [3] ] - Promedio Anual .................................................................. 84
Tabla 44. Norma secundaria SO 2 [μg/m [3] ] - Promedio 1 hora - Percentil 99,73.................................. 85
Tabla 45. Norma secundaria SO 2 [μg/m [3] ] - Promedio 24 horas - Percentil 99,7 ................................ 85
Tabla 46. Norma secundaria SO 2 [μg/m [3] ] - Promedio Anual .............................................................. 85
Tabla 47. Norma primaria CO [mg/m [3] ] - Promedio 8 hora - Percentil 99 ........................................... 86
Tabla 48. Norma primaria CO [mg/m [3] ] - Promedio 1 hora - Percentil 99 ........................................... 86
Tabla 49. Norma primaria NO 2 [ug/m [3] ] - Promedio 1 hora - Percentil 99 ........................................... 87
Tabla 50. Norma primaria NO 2 [μg/m [3] ] - Promedio Anual .................................................................. 87

ÍNDICE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 6 de 252

Tabla 51. Aumento de las concentraciones basales en EMRP Puchuncaví ....................................... 88
Tabla 52. Escenarios modelación MPS .............................................................................................. 95
Tabla 53 MPS como concentración media aritmética anual ............................................................... 95
Tabla 54 Valores de significancia para el aumento de concentraciones de MP 10 y MP 2,5 sobre
receptores humanos corregidos para impactos con una duración menor a 3 años en zonas que
sobrepasen el valor de la norma ........................................................................................................ 99
Tabla 55 Valores de significancia para el aumento de concentraciones de MP 10 ................................................. 100
Tabla 56 Valores de significancia para el aumento de concentraciones de MP 2.5 ................................................ 100
Tabla 57. Fuentes de Emisión - Escenario 1 parte 1 ....................................................................... 167
Tabla 58. Fuentes de Emisión - Escenario 1 parte 2 ....................................................................... 168
Tabla 59. Fuentes de Emisión - Escenario 1 parte 3 ....................................................................... 169
Tabla 60. Fuentes de Emisión - Escenario 1 parte 4 ....................................................................... 170
Tabla 61. Fuentes de Emisión - Escenario 1 parte 5 ....................................................................... 171
Tabla 62. Fuentes de Emisión - Escenario 1 parte 6 ....................................................................... 172
Tabla 63. Fuentes de Emisión - Escenario 1 parte 7 ....................................................................... 173
Tabla 64. Fuentes de Emisión - Escenario 1 parte 8 ....................................................................... 174
Tabla 65. Fuentes de Emisión - Escenario 1 parte 9 ....................................................................... 175
Tabla 66. Fuentes de Emisión - Escenario 1 parte 10 ..................................................................... 176
Tabla 67. Fuentes de Emisión - Escenario 1 parte 11 ..................................................................... 177
Tabla 68. Fuentes de Emisión - Escenario 1 parte 12 ..................................................................... 178
Tabla 69. Fuentes de Emisión - Escenario 1 parte 13 ..................................................................... 179
Tabla 70. Fuentes de Emisión - Escenario 1 parte 14 ..................................................................... 180
Tabla 71. Fuentes de Emisión - Escenario 1 parte 15 ..................................................................... 181
Tabla 72. Fuentes de Emisión - Escenario 1 parte 16 ..................................................................... 182
Tabla 73. Fuentes de Emisión - Escenario 1 parte 17 ..................................................................... 183
Tabla 74. Fuentes de Emisión - Escenario 1 parte 18 ..................................................................... 184
Tabla 75. Fuentes de Emisión - Escenario 1 parte 19 ..................................................................... 185
Tabla 76. Fuentes de Emisión - Escenario 1 parte 20 ..................................................................... 186
Tabla 77. Fuentes de Emisión - Escenario 1 parte 21 ..................................................................... 187
Tabla 78. Fuentes de Emisión - Escenario 1 parte 22 ..................................................................... 188
Tabla 79. Fuentes de Emisión - Escenario 1 parte 23 ..................................................................... 189
Tabla 80. Fuentes de Emisión - Escenario 1 parte 24 ..................................................................... 190
Tabla 81. Fuentes de Emisión - Escenario 1 parte 25 ..................................................................... 191
Tabla 82. Fuentes de Emisión - Escenario 1 parte 26 ..................................................................... 192
Tabla 83. Fuentes de Emisión - Escenario 1 parte 27 ..................................................................... 193
Tabla 84. Fuentes de Emisión - Escenario 1 parte 28 ..................................................................... 194
Tabla 85. Fuentes de Emisión - Escenario 2 parte 1 ....................................................................... 194
Tabla 86. Fuentes de Emisión - Escenario 2 parte 2 ....................................................................... 195
Tabla 87. Fuentes de Emisión - Escenario 2 parte 3 ....................................................................... 196
Tabla 88. Fuentes de Emisión - Escenario 2 parte 4 ....................................................................... 197
Tabla 89. Fuentes de Emisión - Escenario 2 parte 5 ....................................................................... 198
Tabla 90. Fuentes de Emisión - Escenario 2 parte 6 ....................................................................... 199
Tabla 91. Fuentes de Emisión - Escenario 2 parte 7 ....................................................................... 200
Tabla 92. Fuentes de Emisión - Escenario 2 parte 8 ....................................................................... 201
Tabla 93. Fuentes de Emisión - Escenario 2 parte 9 ....................................................................... 202
Tabla 94. Fuentes de Emisión - Escenario 2 parte 10 ..................................................................... 203
Tabla 95. Fuentes de Emisión - Escenario 2 parte 11 ..................................................................... 204
Tabla 96. Fuentes de Emisión - Escenario 2 parte 12 ..................................................................... 205
Tabla 97. Fuentes de Emisión - Escenario 2 parte 13 ..................................................................... 205
Tabla 98. Fuentes de Emisión - Escenario 2 parte 14 ..................................................................... 206
Tabla 99. Fuentes de Emisión - Escenario 3 parte 1 ....................................................................... 206

ÍNDICE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 7 de 252

Tabla 100. Fuentes de Emisión - Escenario 3 parte 2 ..................................................................... 207
Tabla 101. Fuentes de Emisión - Escenario 3 parte 3 ..................................................................... 208
Tabla 102. Fuentes de Emisión - Escenario 3 parte 4 ..................................................................... 209
Tabla 103. Fuentes de Emisión - Escenario 3 parte 5 ..................................................................... 210
Tabla 104. Fuentes de Emisión - Escenario 3 parte 6 ..................................................................... 211
Tabla 105. Fuentes de Emisión - Escenario 3 parte 7 ..................................................................... 212
Tabla 106. Fuentes de Emisión - Escenario 3 parte 8 ..................................................................... 213
Tabla 107. Fuentes de Emisión - Escenario 3 parte 9 ..................................................................... 214
Tabla 108. Fuentes de Emisión - Escenario 3 parte 10 ................................................................... 215
Tabla 109. Fuentes de Emisión - Escenario 3 parte 11 ................................................................... 216
Tabla 110. Fuentes de Emisión - Escenario 3 parte 12 ................................................................... 217
Tabla 111. Fuentes de Emisión - Escenario 3 parte 13 ................................................................... 217
Tabla 112. Fuentes de Emisión - Escenario 4 parte 1 ..................................................................... 217
Tabla 113. Fuentes de Emisión - Escenario 4 parte 2 ..................................................................... 218
Tabla 114. Fuentes de Emisión - Escenario 4 parte 3 ..................................................................... 219
Tabla 115. Fuentes de Emisión - Escenario 4 parte 4 ..................................................................... 220
Tabla 116. Fuentes de Emisión - Escenario 4 parte 5 ..................................................................... 221
Tabla 117. Fuentes de Emisión - Escenario 4 parte 6 ..................................................................... 222
Tabla 118. Fuentes de Emisión - Escenario 4 parte 7 ..................................................................... 223
Tabla 119. Fuentes de Emisión - Escenario 4 parte 8 ..................................................................... 224
Tabla 120. Fuentes de Emisión - Escenario 4 parte 9 ..................................................................... 225
Tabla 121. Fuentes de Emisión - Escenario 4 parte 10 ................................................................... 226
Tabla 122. Fuentes de Emisión - Escenario 4 parte 11 ................................................................... 227
Tabla 123. Fuentes de Emisión - Escenario 4 parte 12 ................................................................... 228
Tabla 124. Fuentes de Emisión - Escenario 4 parte 13 ................................................................... 229
Tabla 125. Fuentes de Emisión - Escenario 4 parte 14 ................................................................... 230
Tabla 126. Fuentes de Emisión - Escenario 4 parte 15 ................................................................... 231
Tabla 127. Fuentes de Emisión - Escenario 4 parte 16 ................................................................... 232
Tabla 128. Fuentes de Emisión - Escenario 4 parte 17 ................................................................... 233
Tabla 129. Fuentes de Emisión - Escenario 4 parte 18 ................................................................... 234
Tabla 130. Fuentes de Emisión - Escenario 4 parte 19 ................................................................... 235
Tabla 131. Fuentes de Emisión - Escenario 4 parte 20 ................................................................... 236
Tabla 132. Fuentes de Emisión - Escenario 4 parte 21 ................................................................... 237
Tabla 133. Fuentes de Emisión - Escenario 4 parte 22 ................................................................... 238
Tabla 134. Fuentes de Emisión - Escenario 4 parte 23 ................................................................... 238
Tabla 135. Fuentes de Emisión - Escenario 5 parte 1 ..................................................................... 239
Tabla 136. Fuentes de Emisión - Escenario 5 parte 2 ..................................................................... 240
Tabla 137. Fuentes de Emisión - Escenario 5 parte 3 ..................................................................... 241
Tabla 138. Fuentes de Emisión - Escenario 5 parte 4 ..................................................................... 242
Tabla 139. Fuentes de Emisión - Escenario 5 parte 5 ..................................................................... 243
Tabla 140. Fuentes de Emisión - Escenario 5 parte 6 ..................................................................... 244
Tabla 141. Fuentes de Emisión - Escenario 5 parte 7 ..................................................................... 245
Tabla 142. Fuentes de Emisión - Escenario 5 parte 8 ..................................................................... 246
Tabla 143. Fuentes de Emisión - Escenario 5 parte 9 ..................................................................... 247
Tabla 144. Fuentes de Emisión - Escenario 5 parte 10 ................................................................... 248
Tabla 145. Fuentes de Emisión - Escenario 5 parte 11 ................................................................... 249
Tabla 146. Fuentes de Emisión - Escenario 5 parte 12 ................................................................... 250
Tabla 147. Fuentes de Emisión - Escenario 5 parte 13 ................................................................... 251
Tabla 148. Fuentes de Emisión - Escenario 5 parte 14 ................................................................... 252
Tabla 149. Fuentes de Emisión - Escenario 5 parte 15 ................................................................... 252

ÍNDICE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 8 de 252

**ÍNDICE DE FIGURAS**
Figura 1. Localización PTAS Maitencillo ............................................................................................ 12
Figura 2. Modelación de calidad de aire ............................................................................................. 18
Figura 3. Dominio de modelación ....................................................................................................... 20
Figura 4. Elevación de terreno del dominio ........................................................................................ 22
Figura 5. Uso de suelo del dominio .................................................................................................... 23
Figura 6. Series Diarias MP 10, Años 2021 a 2023 Red SINCA ........................................................... 29
Figura 7. Series Diarias MP 25, Años 2021 a 2023 Red SINCA ........................................................... 30
Figura 8. Series Diarias SO 2, Años 2021 a 2023 Red SINCA ............................................................. 30
Figura 9. Series Diarias NO 2, Años 2021 a 2023 Red SINCA ............................................................. 32
Figura 10. Series Diarias CO, Años 2021 a 2023 Red SINCA ............................................................ 33
Figura 11. Ciclos Diarios MP 10 Año 2021, 2022 y 2023 Red SINCA ................................................... 34
Figura 12. Ciclos Diarios MP 25 Año 2021, 2022 y 2023 Red SINCA ................................................... 34
Figura 13. Ciclos Diarios SO 2 Año 2021, 2022 y 2023 Red SINCA .................................................... 35
Figura 14. Ciclos Diarios NO 2 Año 2021, 2022 y 2023 Red SINCA .................................................... 37
Figura 15. Ciclos Diarios CO Año 2021, 2022 y 2023 Red SINCA ..................................................... 38
Figura 16. Cronograma de obras fase construcción ........................................................................... 44
Figura 17. Ubicación de receptores discretos ..................................................................................... 54
Figura 18. Serie de tiempo velocidad del viento modelada Estación Puchuncaví ............................... 59
Figura 19. Serie de tiempo velocidad del viento observada Estación Puchuncaví .............................. 59
Figura 20. Ciclo diario velocidad del viento modelada Estación Puchuncaví ...................................... 60
Figura 21. Ciclo diario velocidad del viento observada Estación Puchuncaví ..................................... 60
Figura 22. Comparativo porcentaje de frecuencia de vientos calmos modelada y observada Estación
Puchuncaví ........................................................................................................................................ 61
Figura 23. Serie de tiempo velocidad del viento modelada Estación La Greda ................................... 62
Figura 24. Serie de tiempo velocidad del viento observada Estación La Greda .................................. 62
Figura 25. Ciclo diario velocidad del viento modelada Estación La Greda .......................................... 63
Figura 26. Ciclo diario velocidad del viento observada Estación La Greda ......................................... 63
Figura 27. Comparativo porcentaje de frecuencia de vientos calmos modelada y observada - Estación
La Greda ............................................................................................................................................ 64
Figura 28. Serie de tiempo velocidad del viento modelada Estación Ventanas ................................... 65
Figura 29. Serie de tiempo velocidad del viento observada Estación Ventanas .................................. 65
Figura 30. Ciclo diario velocidad del viento modelada Estación Ventanas .......................................... 66
Figura 31. Ciclo diario velocidad del viento observada Estación Ventanas ......................................... 66
Figura 32. Comparativo porcentaje de frecuencia de vientos calmos modelada y observada - Estación
Ventanas............................................................................................................................................ 67
Figura 33. Ciclo diario dirección del viento modelada Estación Puchuncaví ....................................... 68
Figura 34. Ciclo diario dirección del viento observada Estación Puchuncaví ...................................... 68
Figura 35. Ciclo estacional dirección del viento modelada Estación Puchuncaví ................................ 69
Figura 36. Ciclo estacional dirección del viento observada Estación Puchuncaví ............................... 69
Figura 37. Ciclo diario dirección del viento modelada ......................................................................... 70
Figura 38. Ciclo diario dirección del viento observada Estación La Greda .......................................... 70
Figura 39. Ciclo estacional dirección del viento modelada Estación La Greda .................................... 71
Figura 40. ciclo estacional dirección del viento observada Estación La Greda ................................... 71
Figura 41. Ciclo diario dirección del viento modelada ......................................................................... 72
Figura 42. Ciclo diario dirección del viento observada Estación Ventanas .......................................... 72
Figura 43. Ciclo estacional dirección del viento modelada Estación Ventanas ................................... 73
Figura 44. Ciclo estacional dirección del viento observada Estación Ventanas .................................. 73
Figura 45 E1 Isolíneas MPS como concentración media aritmética anual en receptores ................... 96
Figura 46. E1 Isolíneas MP 2,5 Percentil 98-24 [h] .............................................................................. 102

ÍNDICE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 9 de 252

Figura 47. E1 Isolíneas MP 2,5 Anual ................................................................................................. 103
Figura 48. E1 Isolíneas MP 10 Percentil 98-24 [h] .............................................................................. 104
Figura 49. E1 Isolíneas MP 10 Anual ................................................................................................. 105
Figura 50. E1 Isolíneas SO 2 Percentil 98,5-1 [h] .............................................................................. 106
Figura 51. E1 Isolíneas SO 2 Percentil 99-24 [h] ............................................................................... 107
Figura 52. E1 Isolíneas SO 2 Percentil 99,73-1 [h] ............................................................................ 108
Figura 53. E1 Isolíneas SO 2 Percentil 99,7-24 [h] ............................................................................ 109
Figura 54. E1 Isolíneas SO 2 Anual ................................................................................................... 110
Figura 55. E1 Isolíneas CO Percentil 99-1 [h] .................................................................................. 111
Figura 56. E1 Isolíneas CO Percentil 99-8 [h] .................................................................................. 112
Figura 57. E1 Isolíneas NO 2 Percentil 99-1 [h] ................................................................................. 113
Figura 58. E1 Isolíneas NO 2 Anual ................................................................................................... 114
Figura 59. E2 Isolíneas MP 2,5 Percentil 98-24 [h] .............................................................................. 115
Figura 60. E2 Isolíneas MP 2,5 Anual ................................................................................................. 116
Figura 61. E2 Isolíneas MP 10 Percentil 98-24 [h] .............................................................................. 117
Figura 62. E2 Isolíneas MP 10 Anual ................................................................................................. 118
Figura 63. E2 Isolíneas SO 2 Percentil 98,5-1 [h] .............................................................................. 119
Figura 64. E2 Isolíneas SO 2 Percentil 99-24 [h] ............................................................................... 120
Figura 65. E2 Isolíneas SO 2 Percentil 99,73-1 [h] ............................................................................ 121
Figura 66. E2 Isolíneas SO 2 Percentil 99,7-24 [h] ............................................................................ 122
Figura 67. E2 Isolíneas SO 2 Anual ................................................................................................... 123
Figura 68. E2 Isolíneas CO Percentil 99-1 [h] .................................................................................. 124
Figura 69. E2 Isolíneas CO Percentil 99-8 [h] .................................................................................. 125
Figura 70. E2 Isolíneas NO 2 Percentil 99-1 [h] ................................................................................. 126
Figura 71. E2 Isolíneas NO 2 Anual ................................................................................................... 127
Figura 72. E3 Isolíneas MP 2,5 Percentil 98-24 [h] .............................................................................. 128
Figura 73. E3 Isolíneas MP 2,5 Anual ................................................................................................. 129
Figura 74. E3 Isolíneas MP 10 Percentil 98-24 [h] .............................................................................. 130
Figura 75. E3 Isolíneas MP 10 Anual ................................................................................................. 131
Figura 76. E3 Isolíneas SO 2 Percentil 98,5-1 [h] .............................................................................. 132
Figura 77. E3 Isolíneas SO 2 Percentil 99-24 [h] ............................................................................... 133
Figura 78. E3 Isolíneas SO 2 Percentil 99,73-1 [h] ............................................................................ 134
Figura 79. E3 Isolíneas SO 2 Percentil 99,7-24 [h] ............................................................................ 135
Figura 80. E3 Isolíneas SO 2 Anual ................................................................................................... 136
Figura 81. E3 Isolíneas CO Percentil 99-1 [h] .................................................................................. 137
Figura 82. E3 Isolíneas CO Percentil 99-8 [h] .................................................................................. 138
Figura 83. E3 Isolíneas NO 2 Percentil 99-1 [h] ................................................................................. 139
Figura 84. E3 Isolíneas NO 2 Anual ................................................................................................... 140
Figura 85. E4 Isolíneas MP 2,5 Percentil 98-24 [h] .............................................................................. 141
Figura 86. E4 Isolíneas MP 2,5 Anual ................................................................................................. 142
Figura 87. E4 Isolíneas MP 10 Percentil 98-24 [h] .............................................................................. 143
Figura 88. E4 Isolíneas MP 10 Anual ................................................................................................. 144
Figura 89. E4 Isolíneas SO 2 Percentil 98,5-1 [h] .............................................................................. 145
Figura 90. E4 Isolíneas SO 2 Percentil 99-24 [h] ............................................................................... 146
Figura 91. E4 Isolíneas SO 2 Percentil 99,73-1 [h] ............................................................................ 147
Figura 92. E4 Isolíneas SO 2 Percentil 99,7-24 [h] ............................................................................ 148
Figura 93. E4 Isolíneas SO 2 Anual ................................................................................................... 149
Figura 94. E4 Isolíneas CO Percentil 99-1 [h] .................................................................................. 150
Figura 95. E4 Isolíneas CO Percentil 99-8 [h] .................................................................................. 151
Figura 96. E4 Isolíneas NO 2 Percentil 99-1 [h] ................................................................................. 152
Figura 97. E4 Isolíneas NO 2 Anual ................................................................................................... 153

ÍNDICE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 10 de 252

Figura 98. E5 Isolíneas MP 2,5 Percentil 98-24 [h] .............................................................................. 154
Figura 99. E5 Isolíneas MP 2,5 Anual ................................................................................................. 155
Figura 100. E5 Isolíneas MP 10 Percentil 98-24 [h] ............................................................................ 156
Figura 101. E5 Isolíneas MP 10 Anual................................................................................................ 157
Figura 102. E5 Isolíneas SO 2 Percentil 98,5-1 [h] ............................................................................ 158
Figura 103. E5 Isolíneas SO 2 Percentil 99-24 [h] ............................................................................. 159
Figura 104. E5 Isolíneas SO 2 Percentil 99,73-1 [h] .......................................................................... 160
Figura 105. E5 Isolíneas SO 2 Percentil 99,7-24 [h] .......................................................................... 161
Figura 106. E5 Isolíneas SO 2 Anual ................................................................................................. 162
Figura 107. E5 Isolíneas CO Percentil 99-1 [h] ................................................................................ 163
Figura 108. E5 Isolíneas CO Percentil 99-8 [h] ................................................................................ 164
Figura 109. E5 Isolíneas NO 2 Percentil 99-1 [h] ............................................................................... 165
Figura 110. E5 Isolíneas NO 2 Anual ................................................................................................. 166

ÍNDICE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 11 de 252

**1 INTRODUCCIÓN**

**1.1 DESCRIPCIÓN DEL PROYECTO**

En el marco del Sistema de Evaluación de Impacto Ambiental, conforme a lo señalado en la
Ley N°19.300/94 - Bases Generales del Medio Ambiente y el D.S. 40/2012 - Reglamento del
Sistema de Evaluación de Impacto Ambiental, ESVAL S.A. somete a evaluación el proyecto
denominado “Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de
Maitencillo” mediante Declaración de Impacto Ambiental (DIA).

El presente informe describe los resultados de la modelación de calidad del aire en
cumplimiento a los lineamientos y requerimientos descritos en la Guía para el Uso de
Modelos de Calidad del Aire en el SEIA para la evaluación ambiental de esta componente
como parte de la caracterización basal de medio físico.

El proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de
Maitencillo, tiene por objeto proporcionar de la infraestructura de redes primarias de
alcantarillado, sistemas de elevación e impulsión de las aguas servidas, así como de una
planta de tratamiento para tratar los residuos generados en esta localidad.

La planta se proyecta en la Región de Valparaíso, Comuna de Puchuncaví, específicamente
en la localidad balnearia de Maitencillo. Se ubica a aproximadamente a 50 [km] al norte de la
ciudad de Valparaíso y a 7 [km] al noroeste de la ciudad de Puchuncaví. Basado en los
Instrumentos de Planificación Territorial aplicables según lo señalado la Guía para el Uso del
Territorio en el SEIA, la instalación se inserta fuera del límite urbano del Plan Regulador de la
Comuna de Puchuncaví - Localidad de Maitencillo (Municipalidad de Puchuncaví, 2011) y en
la Zona de Extensión Urbana - ZEU 20 cuyo uso de suelo permitido entre otros, indica:

Infraestructura:
-Sanitaria, de carácter inofensiva, destinada a edificaciones o instalaciones de plantas de
captación y tratamiento de agua potable y de aguas servidas.

Esto definido en resolución 34, sobre la modificación del Plan Regulador Intercomunal de
Valparaíso.

INTRODUCCIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Figura 1. Localización PTAS Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 12 de 252

INTRODUCCIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**1.2 ANTECEDENTES ESPECÍFICOS**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 13 de 252

El sistema de recolección y tratamiento de las aguas servidas de Maitencillo se compone de
redes de colectores primarios, Plantas Elevadoras de Aguas Servidas (PEAS), impulsiones y
una planta de tratamiento que recibirá la totalidad de las aguas de la ciudad.

El tratamiento se inicia con el ingreso del caudal afluente a una cámara repartidora donde
será conducido a un sistema de pretratamiento compacto. Posteriormente, el agua cruda se
porteará gravitacionalmente hacia un estanque de aireación (sectorizado) para su tratamiento
biológico, operando en forma diferenciada para temporada alta y baja.

Posteriormente el licor mezclado generado fluye a un clarificador secundario, de donde se
separa la parte líquida de la sólida. La primera, se canaliza hacia la cámara de contacto para
su desinfección. Por su parte, la segunda pasa a formar la línea de lodos RAS/WAS, donde
el RAS vuelve directamente al reactor, y el WAS se envía hacia el espesador de lodos. En
los periodos no punta de la primera etapa se contempla solamente el uso de la centrífuga
producto de la baja carga. En temporada alta, la línea de lodo considera el espesado y
deshidratado del lodo, produciendo un lodo estabilizado para ser dispuesto en primera
instancia a disposición benéfica de suelos agrícolas y en caso de que esto no sea posible se
enviará a relleno sanitario y/o monorelleno más cercano.

El efluente tratado en la línea de aguas se conducirá hasta una laguna de regadío del
Conjunto Inmobiliario Marbella el cual reutilizará las aguas para el riego de las áreas verdes
presentes en sus instalaciones. Los excesos de efluentes podrán ser dispuestos en emisario
submarino (existente) cuya capacidad máxima es de 42 [L/s].

INTRODUCCIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 14 de 252

**2 OBJETIVOS**

**2.1 OBJETIVO GENERAL**

Determinación del área de influencia que ve afectada su calidad de aire por el proyecto
Redes Primarias Aguas Servidas y Planta de Tratamiento Aguas Servidas Localidad de
Maitencillo, basado en la fase de construcción.

**2.2 OBJETIVOS ESPECÍFICOS**

1. Caracterización de fuentes emisoras descritas en cada fase del proyecto
2. Estimación de incertidumbre asociada a la base meteorológica aplicada.
3. Modelación de dispersión de contaminantes en base a la estimación de emisiones para

las fases de construcción.
4. Estimar la concentración y contribución del proyecto en los puntos receptores dentro del

área de influencia.
5. Evaluar el cumplimiento normativo de la calidad del aire proyectada en la fase de

construcción del proyecto.

OBJETIVOS **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**3 JUSTIFICACIÓN Y DESCRIPCIÓN DEL MODELO**

**3.1 JUSTIFICACIÓN DEL MODELO**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 15 de 252

Para asegurar la calidad de la modelación tanto en los datos utilizados como en los
resultados obtenidos, se aplicaron criterios de buenas prácticas para modelos de calidad del
aire. De manera que toda la información de entrada como datos topográficos, datos
observados y configuraciones del modelo, permitan la reproducción de los resultados
relevantes para la evaluación por parte de la autoridad ambiental.

En concordancia con lo descrito en la Guía para el Uso de Modelos de Calidad del Aire en el
SEIA, los criterios de selección del modelo se basaron en el tipo de terreno en el cual se
inserta el proyecto en evaluación (plano o complejo) y el tipo de contaminante emitido al
ambiente en las distintas fases del proyecto.

El primer criterio asociado al tipo de terreno permite representar el impacto de las emisiones
del proyecto a partir de las condiciones meteorológicas locales del dominio de modelación
definido. Debido a que estas condiciones están vinculadas a las características topográficas
como orografía, uso de suelo, rugosidad superficial, presencia de cuerpos de agua, zona
costera, valle interior, entre otros. Por lo tanto, mientras más heterogéneas son las
características del área de interés, más complejo es el terreno y, en consecuencia, dado el
impacto en la meteorología local, más heterogénea (horizontal y verticalmente) es la
meteorología.

Tal como señala la Guía del SEA, a diferencia de otros países que cuentan en muchas
partes con terreno plano (con características homogéneas), las características de gran parte
del territorio chileno se debieran considerar complejas (heterogéneas). Por esta razón, se
deben considerar modelos capaces de representar esa heterogeneidad de la mejor manera
posible.
En complemento a este criterio, señala que en el caso que se requiera estimar el impacto en
la calidad del aire a distancias mayores a 5 [km], lo más adecuado es utilizar un modelo que
permita simular meteorología heterogénea. Los modelos capaces de esto son los de tipo
“puff” o Eulerianos. El modelo tipo “puff” recomendado es el modelo CALPUFF.

Los modelos tipo “puff” son una combinación entre los modelos Gaussianos y los modelos
Lagrangeanos, en el sentido de que esencialmente calculan la dispersión de contaminantes
provenientes de una emisión instantánea, llamada “puff”, a lo largo de una trayectoria. Su
aproximación matemática consiste en estimar la dispersión en forma Gaussiana en cada
punto de una trayectoria; es decir, a diferencia de los modelos Langrangeanos que necesitan
el cálculo de un gran número de trayectorias para una fuente, los modelos tipo “puff” sólo
requieren una trayectoria por “puff”, lo que hace su cálculo mucho más rápido. En el caso de
emisiones continuas, se simulan las trayectorias y la dispersión Gaussiana de muchos
“puffs”.

Debido a las características costeras de la región en donde se emplaza el proyecto en
estudio, cobra relevancia la capacidad del modelo de representar el comportamiento del
viento sobre las masas de agua y su interacción en la relación mar/tierra (Barclay, 2011),

JUSTIFICACIÓN Y DESCRIPCIÓN DEL MODELO **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 16 de 252

puesto que, podría incrementar el potencial de impacto en receptores situados próximos a la
instalación. Estas condiciones de dispersión son abordadas con un modelo de tipo “puff”
como CALPUFF.
Dado que este modelo no presenta limitaciones respecto a bajas velocidades de viento,
permitiendo al “puff” crecer y difundirse sin un efecto de advección. Tal característica permite
representar eventos de estancamiento en periodos con condición de calma donde los “puff”
se acumularían en función del tiempo. Por otro lado, es importante tener en consideración,
que el modelo CALPUFF permite una representación más realista de la dinámica de vientos
en la zona interés, al utilizar campos de vientos tridimensionales, propiedad ausente en un
modelo de tipo Gaussiano. A su vez, los modelos Gaussianos carecen de efecto memoria de
los contaminantes emitidos en horas previas, esta característica es de importancia en
dominios donde se presenten condiciones de vientos de baja velocidad o de calma (Barclay,
2011).

El segundo criterio para la selección del modelo es el tipo de contaminante a modelar.
Debido a que los contaminantes emitidos a la atmósfera en las distintas fases del proyecto
corresponden mayormente a contaminantes primarios, se justifica la aplicación de un modelo
como CALPUFF.

Con relación al modelo meteorológico utilizado, se consideró como criterio de selección las
características geográficas del área entorno al proyecto las que la definen como terreno
complejo de meteorología heterogénea. Debido principalmente a la presencia de masas de
aguas oceánicas, zona costera y condiciones topográficas que afectan la linealidad de las
emisiones generadas por el proyecto. Por lo anterior, se utilizó el campo meteorológico
tridimensional horario del último año disponible, correspondiente al 2021. El cual fue
generado utilizando el modelo meteorológico WRF (v4.0) y procesado con MMIF (v3.3) para
su uso directo en el modelo de calidad de aire CALPUFF. Esto debido a que MMIF procesa
los datos obtenidos de la simulación WRF a formato requeridos para el ingreso directo al
modelo de dispersión CALPUFF, como una alternativa a CALMET (Brashers, 2014).

Adicionalmente, el procesamiento de la meteorología de pronóstico WRF usando CALMET
no es recomendable y genera un deterioro en el desempeño de la base meteorológica (Fox,
Clarification on EPA-FLM Recommended Settings for CALMET. U.S. Environmental
Protection Agency, 2009).

En estudios realizados por la EPA, se ha verificado que el desempeño del modelo
CALPUFF/MMIF y CALPUFF/CALMET es similar. Sin embargo, las variaciones del modelo
de predicción de CALPUFF usando MMIF son menores que las registradas usando CALMET
(Fox, Supplemental Information for EPA's 2009 Draft Report regarding Reassessment of IW
AQM Phase 2 Recommendations. U.S. Environmental Protection Agency, 2015).

JUSTIFICACIÓN Y DESCRIPCIÓN DEL MODELO **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**3.2** **DESCRIPCIÓN DEL MODELO**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 17 de 252

Para la estimación del área de influencia y la cuantificación de impactos por emisiones
atmofericas, se aplicó el software de modelación atmosférica Calpuff en su versión aprobada
por la EPA 5.8.5, el cual es señalado por la U.S. Environmental Protection Agency como
modelo alternativo para la evaluación de calidad del aire con propósitos regulatorios. El
software se complementó con los módulos de análisis numérico Calpost (7.2.1).

Para la simulación de campos de viento, temperaturas y otras variables meteorológicas, en
un dominio de modelación tridimensional, la Guía para el Uso de Modelos de Calidad del Aire
en el SEIA se señala que en el caso de utilizar Calpuff, se recomienda usar la información del
modelo de pronóstico directamente, sin usar el preprocesador Calmet. Por lo tanto, en
concordancia a lo anterior se utilizó el preprocesador meteorológico el modelo MMIF
(Mesoscale Model Interface Program) aprobado por U.S. EPA, en la generación de los
campos tridimensionales necesarios para la dispersión de emisiones en el modelo.

El módulo Calpuff es un modelo tipo “puff” Lagrangiano Gaussiano no estacionario, que
permite representar la dispersión de una emisión continua como un número discreto de
paquetes de material de o los contaminantes modelados. De esta forma el modelo describe
la contribución de un “puff” en la concentración atmosférica de un receptor en un instante
determinado. Donde la concentración total en un receptor estará dada por la sumatoria de las
contribuciones de todos los “puff” (Scire, 2000).

**3.3 PROCESO DE MODELACIÓN**

La primera etapa del proceso de modelación de calidad del aire corresponde al modelo
numérico meteorológico WRF, cuyo sistema de preprocesamiento (WPS) integra un conjunto
de programas para la preparación de los datos de entrada para el modelo meteorológico
WRF. Mediante Geogrid se preparan los datos geográficos, tales como uso de suelo y
elevaciones de terreno. Ungrib extrae campos meteorológicos globales de archivos con
formato GRIB; y Metgrid interpola horizontalmente los campos meteorológicos extraídos por
Ungrib a las cuadrículas del modelo definidas por Geogrid. El trabajo de interpolación vertical
de campos meteorológicos de WRF se realiza dentro del programa Real.

Posteriormente se aplica el programa WRF para el pronóstico de la meteorología en el
dominio caracterizado. Una vez terminada la simulación meteorológica, se aplica el
procesador MMIF para convertir los datos de salida WRF (WRF.OUT) al formato
CALMET.DAT. Este archivo de salida contiene la meteorología tridimensional utilizada por el
modelo de dispersión CALPUFF, para el cálculo de dispersión y transporte de
contaminantes. En una grilla de cálculo, se obtienen las concentraciones (CONC.DAT)
provenientes de las fuentes de emisión y sus respectivas tasas de emisión ingresadas.
Los resultados son obtenidos con el procesador CALPOST, para la interpolación de las
isolíneas de concentración en conjunto con las concentraciones en receptores discretos
definidos, basado en los criterios normativos aplicables.

JUSTIFICACIÓN Y DESCRIPCIÓN DEL MODELO **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Figura 2. Modelación de calidad de aire

Fuente: Are Project.

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 18 de 252

JUSTIFICACIÓN Y DESCRIPCIÓN DEL MODELO **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**4 CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN**

**4.1 DOMINIO DE MODELACIÓN**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 19 de 252

La extensión del área de modelación, o dominio espacial, fue definida en función de la
magnitud del proyecto y de las emisiones identificadas en las 3 etapas del proyecto.
Considerando la presencia de receptores susceptibles de ser afectados en el área de
emplazamiento del proyecto.

El dominio definido corresponde a 62 x 62 [km], con un tamaño de celda de 1 [km], en
concordancia a lo solicitado por el Servicio de Evaluación Ambiental.

La justificación de la selección del año meteorológico según lo indicado en la Guía para el
Uso de Modelos de Calidad del Aire en el SEIA se basa en la elección del escenario que
representa las condiciones más desfavorables para la dispersión de los contaminantes. Esta
elección se fundamenta en el análisis de los datos observados de la estación meteorológica
Puchuncaví, seleccionada debido a su proximidad al proyecto en cuestión. Se enfocó
principalmente en las condiciones de calma, identificadas a través de la variable velocidad
del viento, ya que estas condiciones representan una dispersión menos efectiva de los
contaminantes.

El resultado del análisis de las condiciones meteorológicas se presenta en la tabla adjunta.

Tabla 1. Análisis porcentual de vientos calmos - Estación Puchuncaví

|Año|% de vientos<br>calmos|% datos<br>válidos|
|---|---|---|
|2021|21,24|92,71%|
|2022|22,21|93,31%|
|2023|25,37|92,98%|

Con base en este análisis, se optó por utilizar los datos meteorológicos pronosticados para el
año 2023, debido que presentó mayor porcentaje de vientos de calma.

Los datos fueron obtenidos a partir del modelo WRF y preprocesados por MMIF. Estos datos
cubren un periodo anual y consideran 11 niveles verticales a partir del nivel superficial de 0
metros.

CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Figura 3. Dominio de modelación

Fuente: Elaborado por Are Project, basado en Google Earth 2024.

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 20 de 252

CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**4.2 BASE METEOROLÓGICA**

**4.2.1 PERIODO DE MODELACIÓN**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 21 de 252

Basado en lo recomendado por la Guía del SEA, la simulación del modelo de dispersión
consideró un periodo anual 2023 completo, para representar la variabilidad climática
relevante de la zona de interés. Esto abarcando los rangos de variaciones horarias y
estacionales para asegurar la inclusión de las condiciones meteorológicas más
desfavorables.

**4.2.2 FUENTE DE DATOS METEOROLÓGICOS**

Existen dos tipos de datos meteorológicos: datos observados y datos generados por un
modelo numérico. En todos los tipos de modelaciones se requiere de ambos. A su vez, los
datos meteorológicos se dividen en datos en superficie y datos en altura. En Chile, la
información de ambos tipos es muchas veces escasa o inexistente.

Se recomienda que el porcentaje de datos válidos de las series de tiempo sea siempre
superior al 75% en un año y que los datos en superficie y altura cubran exactamente el
mismo período. Respecto a la información en altura, el nivel mínimo debiera cubrir los 200

[m] aproximadamente, medidos desde la superficie.

Debido a que el dominio meteorológico definido no se dispone de suficiente información
superficial observada, para la caracterización adecuada de los campos de vientos locales, se
consideró la utilización de información generada por el modelo pronóstico WRF a partir de
datos FNL del último año disponible, correspondiente al año 2023. Por lo tanto, las
estaciones observadas validadas dentro del dominio fueron utilizadas como referencia para
la evaluación del modelo meteorológico en concordancia a lo señalado por la Guía del SEA
(2023). La comparación de las observaciones con las simulaciones del modelo de pronóstico
en el punto de medición permite evaluar la incertidumbre de los datos meteorológicos
tridimensionales generados y de los resultados del modelo de calidad del aire, siempre que
estos datos observados no sean usados como información de entrada del modelo de
pronóstico.

**4.2.3 DATOS TOPOGRÁFICOS Y DE USO DE SUELO**

La escasez de información meteorológica en altura representativa es una limitante a la hora
de evaluar cualquier modelo. El modelo numérico recomendado para la generación de datos
meteorológicos es el Weather Research and Forecasting Model (WRF). WRF es uno de los
modelos meteorológicos de pronóstico más avanzados y completos y es mantenido por el
National Center for Atmospheric Research (NCAR) y National Oceanic and Atmospheric
Administration (NOAA) de Estados Unidos. Además, como señala la Guía del SEA (2023),
este tipo de modelo se ha ocupado en la mayoría de los proyectos relacionados con
modelación atmosférica encargados por organismos estatales, respaldando su aplicación al
contexto de evaluación ambiental, siempre que la resolución horizontal de WRF sea de 1

[km].

CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 22 de 252

De acuerdo a Schmitz et al. (2011), en el caso de los modelos tipo “puff” y Eulerianos, si bien
son capaces de representar meteorología heterogénea en el dominio de modelación, no
tienen un desempeño muy superior a los modelos Gaussianos si se utilizan con información
meteorológica de sólo una estación y un radiosondeo como información de entrada. Es por
ello que estos modelos debieran usarse únicamente con datos provenientes de un modelo
meteorológico de pronóstico. En el caso de CALPUFF, se recomienda usar la información del
modelo de pronóstico directa mente, sin usar el preprocesador CALMET.

La fuente de información topográfica del dominio de modelación considerado en CALPUFF
corresponde a cartas topográficas digitales adquiridos desde la base de “U.S. Geological
Survey (USGS) - Global Multi-resolution Terrain Elevation Data 2010 (GMTED2010)” con
curvas de nivel de resolución 30 [arc-second], equivalente a 920 [m] aproximadamente.
Con relación al uso de suelo, el modelo meteorológico utilizó información satelital de la base
de datos “Moderate Resolution Imaging Spectroradiometer (MODIS)” para Sudamérica con
una resolución 15 [arc-second], equivalente a 465 [m] aproximadamente.

Figura 4. Elevación de terreno del dominio

CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Figura 5. Uso de suelo del dominio

**4.2.4 CONFIGURACIÓN DEL MODELO**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 23 de 252

Todos los modelos requieren ser configurados para su aplicación en cada caso específico.
Estas configuraciones determinan características como el periodo y dominio geográfico de la
simulación, resolución espacial horizontal y vertical, parametrizaciones físicas, formato de
resultados, entre otros. Dado que la distribución temporal y espacial de las concentraciones
de contaminantes depende en gran medida de la meteorología, las parametrizaciones de los
modelos meteorológicos (o pre-procesadores meteorológicos) requieren una atención
especial.

En concordancia a lo descrito en la Guía del SEA, se consideró la configuración por defecto
del modelo Calpuff, considerando además la misma resolución horizontal que la obtenida por
el modelo meteorológico WRF.

CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**4.2.5 PARAMETRIZACIÓN RECEPTORES**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 24 de 252

Tal como lo señala la Guía de Calidad del Aire: En el modelo se debe configurar una
cuadrícula o grilla de receptores, diferente de los receptores discretos. Al definir la grilla de
receptores más adecuada para el proyecto, se debe asegurar que el tamaño de esta sea lo
suficientemente grande para garantizar la cuantificación de la concentración máxima a nivel
del suelo (Servicio de Evaluación Ambiental, 2023).

Dado lo anterior, se utilizó la grilla anidada de receptores, cuya parametrización es la
siguiente, según lo que establece la Guía:

Tabla 2. Parametrización grilla 1 receptores

|Distancia desde el<br>centro de las fuentes<br>[m]|Espaciado del<br>receptor|Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur|Col4|Altura de los<br>receptores|
|---|---|---|---|---|
|Distancia desde el<br>centro de las fuentes<br>[m]|[m]|X|Y|[m]|
|500|50|272.495|6.386.450|1,5|
|1.000|250|250|250|250|

Tabla 3. Parametrización grilla 2 receptores

|Distancia desde el<br>centro de las fuentes<br>[m]|Espaciado del<br>receptor|Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur|Col4|Altura de los<br>receptores|
|---|---|---|---|---|
|Distancia desde el<br>centro de las fuentes<br>[m]|[m]|X|Y|[m]|
|500|50|272.306|6.385.136|1,5|
|1.000|250|250|250|250|

Tabla 4. Parametrización grilla 3 receptores

|Distancia desde el<br>centro de las fuentes<br>[m]|Espaciado del<br>receptor|Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur|Col4|Altura de los<br>receptores|
|---|---|---|---|---|
|Distancia desde el<br>centro de las fuentes<br>[m]|[m]|X|Y|[m]|
|500|50|272.956|6.384.019|1,5|
|1.000|250|250|250|250|

Tabla 5. Parametrización grilla 4 receptores

|Distancia desde el<br>centro de las fuentes<br>[m]|Espaciado del<br>receptor|Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur|Col4|Altura de los<br>receptores|
|---|---|---|---|---|
|Distancia desde el<br>centro de las fuentes<br>[m]|[m]|X|Y|[m]|
|500|50|272.714|6.382.885|1,5|
|1.000|250|250|250|250|

Tabla 6. Parametrización grilla 5 receptores

|Distancia desde el<br>centro de las fuentes<br>[m]|Espaciado del<br>receptor|Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur|Col4|Altura de los<br>receptores|
|---|---|---|---|---|
|Distancia desde el<br>centro de las fuentes<br>[m]|[m]|X|Y|[m]|
|20.000|1.000|272.829|6.385.151|1,5|

CARACTERÍSTICAS DEL DOMINIO DE MODELACIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**5 FUENTES DE EMISIÓN**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 25 de 252

Tal como señala la Guía del SEA, para el proyecto se identificaron las fuentes de emisión
relevantes para la calidad del aire, estimando su emisión en las distintas fases del proyecto.
Esto permite contrastar a nivel normativo la contribución de las fuentes de emisión
identificadas en las concentraciones de los distintos puntos de inmisión en el área de
influencia del proyecto.

Las fuentes de emisión fueron caracterizadas mediante la aplicación de tasas de emisión
estimadas a partir de factores de emisión según inventario de emisiones desarrollado por
consultores de GSI. A partir de lo anterior, se incorporaron a los datos de entrada del modelo
ciclos de emisión horarios y estacionales, con el objeto de representar la situación más
desfavorable para la evaluación del proyecto. Los factores utilizados para la estimación
corresponden además a la última actualización disponible de los documentos de referencia,
tanto a nivel nacional como internacional.

Asimismo, se conformaron situaciones de operación concordantes con la representación
aquella actividad o fase del proyecto cuya emisión al ambiente permita responder a la
posibilidad generación de algún impacto de relevancia sobre la calidad del aire, la salud de
las personas u otro componente del medio ambiente. A partir de lo anterior es factible el
análisis de la magnitud del alcance de las emisiones, así como su duración, incluyendo
aquellas actividades temporales de impacto acotado.

FUENTES DE EMISIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 26 de 252

**6 LÍNEA DE BASE**

**6.1 NORMATIVA APLICABLE**

La normativa nacional aplicable al área de estudio comprende las normas primarias y
secundarias de calidad del aire para los contaminantes Material Particulado Respirable
(MP 10 ), Material Particulado Fino (MP 2,5 ), Dióxido de Azufre (SO 2 ), Dióxido de Nitrógeno
(NO 2 ), Monóxido de Carbono (CO) y el reciente Plan de Prevención y Descontaminación
(PPDA) entrado en vigencia con fecha 30 de Marzo del año 2019 para el control de las
emisiones de los mismos contaminantes descritos.

Las normas de calidad descritas son resumidas en la Tabla 1 y contienen los decretos
mediante el cual fueron promulgadas, los umbrales y el periodo de aplicación de las normas.

Tabla 7. Normas de Calidad del Aire vigentes aplicables a la zona de estudio

|Decreto|Contaminante|Tipo de Norma|Unidad|Estadístico|Tipo|Límite|
|---|---|---|---|---|---|---|
|D.S.<br>No12/2011|MP2,5|Primaria|[μg/m3]|Percentil 98 de<br>concentraciones de 24<br>horas|Diaria|50|
|D.S.<br>No12/2011|MP2,5|Primaria|[μg/m3]|Promedio Aritmético<br>Trianual|Anual|20|
|D.S.<br>No12/2021|MP10|Primaria|[μg/m3]|Percentil 98 de<br>concentraciones de 24<br>horas|Diaria|130|
|D.S.<br>No12/2021|MP10|Primaria|[μg/m3]|Promedio Aritmético<br>Trianual|Anual|50|
|D.S.<br>N°104/2019|SO2|Primaria|[μg/m3]|Promedio Aritmético<br>Trianual del Percentil 99|1 hora|350|
|D.S.<br>N°104/2019|SO2|Primaria|[μg/m3]|Promedio Aritmético<br>Trianual del Percentil 99|24<br>horas|150|
|D.S.<br>N°104/2019|SO2|Primaria|[μg/m3]|Promedio Aritmético<br>Trianual|Anual|60|
|D.S.<br>N°22/2010|SO2|Secundario|[μg/m3]|Promedio Aritmético<br>Trianual del Percentil 99,73|1 hora|1.000|
|D.S.<br>N°22/2010|SO2|Secundario|[μg/m3]|Promedio Aritmético<br>Trianual del Percentil 99,7|24<br>Horas|365|
|D.S.<br>N°22/2010|SO2|Secundario|[μg/m3]|Promedio Aritmético<br>Trianual|Anual|80|
|D.S.<br>N°114/2002|NO2|Primaria|[μg/m3]|Promedio Aritmético<br>Trianual|Anual|100|
|D.S.<br>N°114/2002|NO2|Primaria|[μg/m3]|Percentil 99 de los<br>máximos diarios de<br>concentración 1 hora|1 hora|400|
|D.S.<br>N°115/2002|CO|Primaria|[mg/m3]|Percentil 99 de los<br>máximos diarios de 8 horas|8 <br>horas|10|
|D.S.<br>N°115/2002|CO|Primaria|[mg/m3]|Percentil 99 de los<br>máximos diarios de 1 hora|1 hora|30|

Por otro lado, el Plan de Prevención y Descontaminación Atmosférico (PPDA), D.S.105/2018
“Aprueba Plan de Prevención y Descontaminación Atmosférica para las Comunas de Concón
Quintero y Puchuncaví”, tiene por objetivo evitar la superación de las normas primarias de

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 27 de 252

calidad ambiental para MP10, como concentración anual, y para MP2,5 como concentración
de 24 horas, además de recuperar los niveles en que los contaminantes regulados en el
presente PPDA, se encontrasen en niveles de saturación. Para cumplir con este objetivo, se
plantea disminuir las concentraciones de contaminantes existentes en un plazo de 5 años
contado desde la publicación del presente decreto.

Adicionalmente, se establece la reducción de emisiones de compuestos orgánicos volátiles
(COVs) mediante la implementación de mejores técnicas de control de este compuesto,
justificado por el aporte que tienen estas emisiones en la formación de aerosoles
secundarios, que inciden directamente en la formación de MP 2,5 . Finalmente se establecen
medidas adicionales para fuentes emisoras, tales como calderas, fuentes areales, quemas
agrícolas, calefacción domiciliaria, entre otras. Adicionalmente, el Plan contempla una
Gestión de Episodios Críticos destinada a que no se generen altas concentraciones de SO 2
(en periodos de una hora) y MP 2,5 (en periodos de 24 horas) y de COVS, ante malas
condiciones de ventilación (DS. No105/2018).

**6.2 BASE DE DATOS RED DE MONITOREO VENTANAS**

Para la elaboración de la línea base del área de estudio, y descripción de las series y ciclos
diarios de los contaminantes, se descargó y analizó la información de la Red del Sistema de
Información Nacional de Calidad del Aire (SINCA) para los años 2021, 2022 y 2023, la cual
fueron contabilizadas 7 estaciones para el análisis de las métricas de las especies
contaminantes.

Tabla 8. Estaciones de Calidad del Aire

|ID|Nombre|Coordenadas UTM [m] WGS-84 Huso 19<br>Sur|Col4|Estadístico estimado|
|---|---|---|---|---|
|1|Quintero|262.528 E|6.371.087 N|MP10, MP2.5, SO2,NO2, CO|
|2|La Greda|268.185 E|6.373.910 N|MP10, MP2.5, SO2,NO2|
|3|Puchuncaví|274.379 E|6.377.331 N|MP10, MP2.5, SO2,NO2|
|4|Los Maitenes|270.073 E|6.372.171 N|MP10, MP2.5, SO2,NO2, CO|
|5|Valle Alegre|271.889 E|6.367.413 N|MP10, MP2.5, SO2|
|6|Centro Quintero|262.853 E|6.369.407 N|MP10, MP2.5, SO2,NO2, CO|
|7|Loncura|266.226 E|6.368.689 N|MP10, MP2.5, SO2,NO2, CO|

Respecto a la disponibilidad de datos (validación según lo indicado en Normas primarias y
Decreto 61/2008) estos son mostrados en la Tabla No3, donde se visualiza que la mayoría se
encuentra sobre el 90% de disponibilidad, la excepción es indicada para el MP 2,5 donde el
NA, corresponde a no aplica para las estaciones Centro Quintero y Loncura siguiendo el
lineamiento de la documentación obtenida para mostrar la presente línea base.

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

 Tabla 9. Porcentaje de datos en válidos Estaciones de Calidad del Aire

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 28 de 252

|Estaciones/Años|MP<br>2,5|Col3|Col4|MP<br>10|Col6|Col7|SO<br>2|Col9|Col10|NO<br>2|Col12|Col13|CO|Col15|Col16|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Estaciones/Años|2021|2022|2023|2021|2022|2023|2021|2022|2023|2021|2022|2023|2021|2022|2023|
|Quintero|97,38|97,56|97,81|99,45|99,49|98,53|99,12|99,09|99,15|98,99|99,08|99,18|99,09|99,01|98,91|
|La Greda|96,56|98,26|99,55|98,89|99,20|99,69|98,97|98,56|99,15|98,03|98,21|97,11|S/I|S/I|S/I|
|Puchuncaví|95,45|97,53|99,13|99,52|99,04|98,57|99,18|99,18|99,13|97,86|98,05|98,61|S/I|S/I|S/I|
|Los Maitenes|93,37|95,47|93,74|99,36|99,12|99,78|99,23|98,41|99,29|98,88|98,32|98,75|97,99|98,51|97,68|
|Valle Alegre|S/I|S/I|S/I|96,08|94,79|94,86|98,66|96,21|99,28|99,22|96,30|97,80|S/I|S/I|S/I|
|Centro Quintero|99,73|99,68|99,90|99,64|99,68|99,60|98,85|99,10|99,12|99,36|99,95|99,26|97,60|98,98|98,32|
|Loncura|95,42|95,58|92,60|96,63|96,47|97,55|97,06|97,02|97,70|97,04|96,96|96,76|96,81|96,98|97,29|

**6.3 ANÁLISIS VARIABILIDAD TEMPORAL CONTAMINANTES**

A continuación se muestran las series diarias y ciclos diarios de los contaminantes.

El monitoreo de un contaminante no está presente en todas las estaciones, razón por la cual varía el número de
estaciones a mostrar en cada mosaico de cada contaminante.

El orden para mostrar es primero las estaciones asociadas a MP 10, luego a MP 25, siguiendo de SO 2, luego NO 2 y finalmente
CO. Se homologa la misma estructura respecto a las figuras de ciclos diarios.

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Figura 6. Series Diarias MP 10, Años 2021 a 2023 Red SINCA

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 29 de 252

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Figura 7. Series Diarias MP 25, Años 2021 a 2023 Red SINCA

Figura 8. Series Diarias SO 2, Años 2021 a 2023 Red SINCA

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 30 de 252

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 31 de 252

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Figura 9. Series Diarias NO 2, Años 2021 a 2023 Red SINCA

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 32 de 252

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Figura 10. Series Diarias CO, Años 2021 a 2023 Red SINCA

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 33 de 252

Se observa un incremento en las

concentraciones durante los meses de invierno, atribuido a una combinación de factores, entre los que se incluyen condiciones
meteorológicas, descritas en el DS 105/2018, como inversiones térmicas, bajas presiones costeras, una menor altura de la
capa límite y una atmósfera más estable con menor movimiento. Estos factores contribuyen al aumento de contaminantes,
principalmente derivados de fuentes de combustión y del parque industrial, como el SO 2, MP 2.5, NO 2 y CO. Sin embargo,
respecto al MP 10, al ser una especie de origen biogénico, su incremento durante este periodo no es tan evidente como el de
otros contaminantes.

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Figura 11. Ciclos Diarios MP 10 Año 2021, 2022 y 2023 Red SINCA

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 34 de 252

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Figura 12. Ciclos Diarios MP 25 Año 2021, 2022 y 2023 Red SINCA

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 35 de 252

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Figura 13. Ciclos Diarios SO 2 Año 2021, 2022 y 2023 Red SINCA

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 36 de 252

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Figura 14. Ciclos Diarios NO 2 Año 2021, 2022 y 2023 Red SINCA

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 37 de 252

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Figura 15. Ciclos Diarios CO Año 2021, 2022 y 2023 Red SINCA

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 38 de 252

Evaluando los ciclos diarios de las figuras anteriores, se observa un patrón claro: los picos de concentración de SO 2 en las
estaciones ubicadas en la bahía de Quintero se producen durante la noche, mientras que en las estaciones al norte del parque
industrial de Ventanas, se registran durante el día.

En cuanto a los contaminantes NO 2 y CO, generalmente se observan picos durante las horas pico, es decir, cuando hay mayor
movilización de personas, ya sea para ir al trabajo, para la escuela, u otras actividades diarias.

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 39 de 252

**6.4 ANÁLISIS DE RESULTADOS DE LÍNEA BASE DE CALIDAD DEL AIRE ESTIMADA**

Se procedió al análisis de estadísticos para la comparación con las normas primarias de MP 10 y
MP 2,5, SO 2, primaria y secundaria, NO 2 y CO.

MP 2,5 Percentil 98 - 24 horas

De acuerdo con los resultados obtenidos a partir de los datos disponibles para los años 2021,
2022 y 2023, se determinó que existe condición de latencia en estación Centro Quintero

MP 2,5 Anual

De acuerdo con los resultados obtenidos a partir de los datos disponibles para los años 2021,
2022 y 2023, se determinó que no se visualizan condiciones de latencia o saturación en ninguna
de las estaciones analizadas.

MP 10 Norma Anual

De acuerdo con los resultados obtenidos a partir de los datos disponibles para los años 2021,
2022 y 2023, se determinó que en estación Puchuncaví, se encuentra en condición de latente
con un 82.12% respecto al umbral determinado en la respectiva norma primaria.

MP 10 Percentil 98 - 24 horas

De acuerdo con los resultados obtenidos a partir de los datos disponibles para los años 2021,
2022 y 2023, se determinó que no se visualizan condiciones de latencia o saturación en ninguna
de las estaciones analizadas.

SO 2

En cuanto a los estadísticos evaluados para SO 2, estos no superaron los límites establecidos,
tanto en su norma horaria y anual.

NO 2

En cuanto a los estadísticos evaluados para NO 2, estos no superaron los límites establecidos,
tanto en su norma horaria y diaria y anual.

CO

En cuanto a los estadísticos evaluados para CO, estos no superaron los límites establecidos, tanto
en su norma horaria y de 8 horas.

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Tabla 10. Estadísticos de Comparación Norma Primaria MP 2,5

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 40 de 252

|Estaciones|Años|P98 Diario<br>[ug/m3]|% Norma|Trianual<br>[ug/m3]|Promedio Tri<br>Anual [ug/m3]|% Norma|
|---|---|---|---|---|---|---|
|Centro<br>Quintero|~~2021~~<br>|~~55,42~~<br>|~~110,83~~<br>|~~20,75~~<br>|19|95|
|Centro<br>Quintero|~~2022~~<br>|~~45,54~~<br>|~~91,08~~<br>|~~18,81~~<br>|~~18,81~~<br>|~~18,81~~<br>|
|Centro<br>Quintero|~~2023~~<br>|~~43,67~~<br>|~~87,33~~<br>|~~17,43~~<br>|~~17,43~~<br>|~~17,43~~<br>|
|<br>Loncura|~~2021~~<br>|~~35,92~~<br>|~~71,83~~<br>|~~14,74~~<br>|12.69|63.43|
|<br>Loncura|~~2022~~<br>|~~26,71~~<br>|~~53,42~~<br>|~~12,03~~<br>|~~12,03~~<br>|~~12,03~~<br>|
|<br>Loncura|~~2023~~<br>|~~31,23~~<br>|~~62,45~~<br>|~~11,29~~<br>|~~11,29~~<br>|~~11,29~~<br>|
|<br>Los Maitenes|~~2021~~<br>|~~23,96~~<br>|~~47,92~~<br>|~~12,03~~<br>|12.30|61.50|
|<br>Los Maitenes|~~2022~~<br>|~~22,13~~<br>|~~44,25~~<br>|~~11,37~~<br>|~~11,37~~<br>|~~11,37~~<br>|
|<br>Los Maitenes|~~2023~~<br>|~~31,29~~<br>|~~62,58~~<br>|~~13,51~~<br>|~~13,51~~<br>|~~13,51~~<br>|
|<br>Quintero|~~2021~~<br>|~~34,38~~<br>|~~68,75~~<br>|~~15,99~~<br>|14.04|70.22|
|<br>Quintero|~~2022~~<br>|~~26,70~~<br>|~~53,40~~<br>|~~13,33~~<br>|~~13,33~~<br>|~~13,33~~<br>|
|<br>Quintero|~~2023~~<br>|~~28,33~~<br>|~~56,67~~<br>|~~12,81~~<br>|~~12,81~~<br>|~~12,81~~<br>|
|<br>La Greda|~~2021~~<br>|~~41,08~~<br>|~~82,17~~<br>|~~16,45~~<br>|15.60|78.01|
|<br>La Greda|~~2022~~<br>|~~31,22~~<br>|~~62,43~~<br>|~~15,53~~<br>|~~15,53~~<br>|~~15,53~~<br>|
|<br>La Greda|~~2023~~<br>|~~33,92~~<br>|~~67,83~~<br>|~~14,82~~<br>|~~14,82~~<br>|~~14,82~~<br>|
|<br>Puchuncaví|~~2021~~<br>|~~32,17~~<br>|~~64,33~~<br>|~~14,52~~<br>|14.86|74.29|
|<br>Puchuncaví|~~2022~~<br>|~~33,71~~<br>|~~67,43~~<br>|~~15,52~~<br>|~~15,52~~<br>|~~15,52~~<br>|
|<br>Puchuncaví|~~2023~~|~~30,67~~|~~61,33~~|~~14,54~~|~~14,54~~|~~14,54~~|

Tabla 11. Estadísticos de Comparación Normas Primaria MP 10

|Estaciones|Años|P98 Diario<br>[ug/m3]|% Norma|Trianual<br>[ug/m3]|Promedio Tri<br>Anual [ug/m3]|% Norma|
|---|---|---|---|---|---|---|
|Centro<br>Quintero|~~2021~~<br>|~~76,46~~<br>|~~58,81~~<br>|~~39,81~~<br>|39.04|78.08|
|Centro<br>Quintero|~~2022~~<br>|~~83,29~~<br>|~~64,07~~<br>|~~39,63~~<br>|~~39,63~~<br>|~~39,63~~<br>|
|Centro<br>Quintero|~~2023~~<br>|~~68,21~~<br>|~~52,47~~<br>|~~37,68~~<br>|~~37,68~~<br>|~~37,68~~<br>|
|<br>Loncura|~~2021~~<br>|~~72,67~~<br>|~~55,90~~<br>|~~38,65~~<br>|37.74|75.49|
|<br>Loncura|~~2022~~<br>|~~73,21~~<br>|~~56,31~~<br>|~~39,44~~<br>|~~39,44~~<br>|~~39,44~~<br>|
|<br>Loncura|~~2023~~<br>|~~69,25~~<br>|~~53,27~~<br>|~~35,14~~<br>|~~35,14~~<br>|~~35,14~~<br>|
|<br>Los Maitenes|~~2021~~<br>|~~56,88~~<br>|~~43,75~~<br>|~~26,67~~<br>|29.67|59.34|
|<br>Los Maitenes|~~2022~~<br>|~~73,63~~<br>|~~56,63~~<br>|~~31,73~~<br>|~~31,73~~<br>|~~31,73~~<br>|
|<br>Los Maitenes|~~2023~~<br>|~~61,88~~<br>|~~47,60~~<br>|~~30,62~~<br>|~~30,62~~<br>|~~30,62~~<br>|
|<br>Quintero|~~2021~~<br>|~~75,54~~<br>|~~58,11~~<br>|~~37,98~~<br>|37.93|75.87|
|<br>Quintero|~~2022~~<br>|~~73,38~~<br>|~~56,44~~<br>|~~36,84~~<br>|~~36,84~~<br>|~~36,84~~<br>|
|<br>Quintero|~~2023~~<br>|~~75,38~~<br>|~~57,98~~<br>|~~38,98~~<br>|~~38,98~~<br>|~~38,98~~<br>|
|<br>La Greda|~~2021~~<br>|~~78,17~~<br>|~~60,13~~<br>|~~36,71~~<br>|37.20|74.41|
|<br>La Greda|~~2022~~<br>|~~62,00~~<br>|~~47,69~~<br>|~~35,45~~<br>|~~35,45~~<br>|~~35,45~~<br>|
|<br>La Greda|~~2023~~<br>|~~72,00~~<br>|~~55,38~~<br>|~~39,44~~<br>|~~39,44~~<br>|~~39,44~~<br>|
|<br>Puchuncaví|~~2021~~<br>|~~68,29~~<br>|~~52,53~~<br>|~~38,84~~<br>|41.06|82.12|
|<br>Puchuncaví|~~2022~~<br>|~~78,25~~<br>|~~60,19~~<br>|~~44,14~~<br>|~~44,14~~<br>|~~44,14~~<br>|
|<br>Puchuncaví|~~2023~~<br>|~~68,38~~<br>|~~52,60~~<br>|~~40,20~~<br>|~~40,20~~<br>|~~40,20~~<br>|
|<br>Valle Alegre|~~2021~~<br>|~~45,71~~<br>|~~35,16~~<br>|~~25,69~~<br>|25.80|51.59|
|<br>Valle Alegre|~~2022~~<br>|~~48,35~~<br>|~~37,19~~<br>|~~25,37~~<br>|~~25,37~~<br>|~~25,37~~<br>|
|<br>Valle Alegre|~~2023~~|~~52,92~~|~~40,71~~|~~26,33~~|~~26,33~~|~~26,33~~|

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Tabla 12. Estadísticos de Comparación Normas Primaria SO 2

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 41 de 252

|Estaciones|Norma Diaria|Col3|Col4|Col5|Norma Anual|Col7|Col8|Norma Horaria|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|<br>Estaciones|Años<br>|P99<br>Diario<br>|Promedio<br>Tri Anual|% <br>Norma|Trianual<br>|Promedio<br>Tri Anual|% <br>Norma|P99<br>Hora<br>|Promedio<br>Tri Anual|% <br>Norma|
|Centro<br>Quintero|~~2021~~<br>|~~65,37~~<br>|53,79|35,86|~~15,61~~<br>|13,18|21,97|~~148,01~~<br>|116,58|33,31|
|Centro<br>Quintero|~~2022~~<br>|~~53,24~~<br>|~~53,24~~<br>|~~53,24~~<br>|~~13,24~~<br>|~~13,24~~<br>|~~13,24~~<br>|~~124,65~~<br>|~~124,65~~<br>|~~124,65~~<br>|
|Centro<br>Quintero|~~2023~~<br>|~~42,78~~<br>|~~42,78~~<br>|~~42,78~~<br>|~~10,69~~<br>|~~10,69~~<br>|~~10,69~~<br>|~~77,07~~<br>|~~77,07~~<br>|~~77,07~~<br>|
|<br>Loncura|~~2021~~<br>|~~38,60~~<br>|33|22|~~8,68~~<br>|6,49|10,82|~~88,19~~<br>|740,41|20,12|
|<br>Loncura|~~2022~~<br>|~~38,30~~<br>|~~38,30~~<br>|~~38,30~~<br>|~~6,65~~<br>|~~6,65~~<br>|~~6,65~~<br>|~~78,69~~<br>|~~78,69~~<br>|~~78,69~~<br>|
|<br>Loncura|~~2023~~<br>|~~22,11~~<br>|~~22,11~~<br>|~~22,11~~<br>|~~4,14~~<br>|~~4,14~~<br>|~~4,14~~<br>|~~44,34~~<br>|~~44,34~~<br>|~~44,34~~<br>|
|Los<br>Maitenes|~~2021~~<br>|~~63,74~~<br>|62,69|41,79|~~21,36~~<br>|17,29|28,82|~~206,29~~<br>|179,17|51,19|
|Los<br>Maitenes|~~2022~~<br>|~~59,92~~<br>|~~59,92~~<br>|~~59,92~~<br>|~~15,30~~<br>|~~15,30~~<br>|~~15,30~~<br>|~~174,24~~<br>|~~174,24~~<br>|~~174,24~~<br>|
|Los<br>Maitenes|~~2023~~<br>|~~64,42~~<br>|~~64,42~~<br>|~~64,42~~<br>|~~15,22~~<br>|~~15,22~~<br>|~~15,22~~<br>|~~156,96~~<br>|~~156,96~~<br>|~~156,96~~<br>|
|<br>Quintero|~~2021~~<br>|~~80,91~~<br>|63,65|42,43|~~18,03~~<br>|13,82|23,04|~~215,32~~<br>|142,72|40,78|
|<br>Quintero|~~2022~~<br>|~~66,13~~<br>|~~66,13~~<br>|~~66,13~~<br>|~~13,99~~<br>|~~13,99~~<br>|~~13,99~~<br>|~~132,35~~<br>|~~132,35~~<br>|~~132,35~~<br>|
|<br>Quintero|~~2023~~<br>|~~43,91~~<br>|~~43,91~~<br>|~~43,91~~<br>|~~9,46~~<br>|~~9,46~~<br>|~~9,46~~<br>|~~80,49~~<br>|~~80,49~~<br>|~~80,49~~<br>|
|<br>La Greda|~~2021~~<br>|~~32,80~~<br>|28,06|18,71|~~13,05~~<br>|11,30|18,83|~~60,47~~<br>|44,77|12,79|
|<br>La Greda|~~2022~~<br>|~~30,05~~<br>|~~30,05~~<br>|~~30,05~~<br>|~~13,30~~<br>|~~13,30~~<br>|~~13,30~~<br>|~~50,42~~<br>|~~50,42~~<br>|~~50,42~~<br>|
|<br>La Greda|~~2023~~<br>|~~21,34~~<br>|~~21,34~~<br>|~~21,34~~<br>|~~7,54~~<br>|~~7,54~~<br>|~~7,54~~<br>|~~23,41~~<br>|~~23,41~~<br>|~~23,41~~<br>|
|<br>Puchuncaví|~~2021~~<br>|~~31,77~~<br>|28,89|19,26|~~15,04~~<br>|14,09|23,48|~~67,25~~<br>|57,86|16,53|
|<br>Puchuncaví|~~2022~~<br>|~~31,46~~<br>|~~31,46~~<br>|~~31,46~~<br>|~~16,17~~<br>|~~16,17~~<br>|~~16,17~~<br>|~~63,16~~<br>|~~63,16~~<br>|~~63,16~~<br>|
|<br>Puchuncaví|~~2023~~<br>|~~23,44~~<br>|~~23,44~~<br>|~~23,44~~<br>|~~11,05~~<br>|~~11,05~~<br>|~~11,05~~<br>|~~43,16~~<br>|~~43,16~~<br>|~~43,16~~<br>|
|Valle<br>Alegre|~~2021~~<br>|~~38,94~~<br>|29,90|19,93|~~17,06~~<br>|11,20|18,66|~~83,31~~<br>|62,98|17,99|
|Valle<br>Alegre|~~2022~~<br>|~~33,22~~<br>|~~33,22~~<br>|~~33,22~~<br>|~~10,92~~<br>|~~10,92~~<br>|~~10,92~~<br>|~~68,40~~<br>|~~68,40~~<br>|~~68,40~~<br>|
|Valle<br>Alegre|~~2023~~|~~17,53~~|~~17,53~~|~~17,53~~|~~5,61~~|~~5,61~~|~~5,61~~|~~37,21~~|~~37,21~~|~~37,21~~|

Tabla 13. Estadísticos de Comparación Normas Secundaria SO 2

|Estaciones|Norma Diaria|Col3|Col4|Col5|Norma Anual|Col7|Col8|Norma Horaria|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|<br>Estaciones|Años<br>|P99 .7<br>Diario<br>|Promedio<br>Tri Anual|% <br>Norma|Trianual<br>|Promedio<br>Tri Anual|% <br>Norma|P99.73<br>Hora<br>|Promedio<br>Tri Anual|% <br>Norma|
|Centro<br>Quintero|~~2021~~<br>|~~87,01~~<br>|65,78|18,02|~~15,67~~<br>|13,19|16,49|~~217,07~~<br>|184,14|18,41|
|Centro<br>Quintero|~~2022~~<br>|~~63,46~~<br>|~~63,46~~<br>|~~63,46~~<br>|~~13,24~~<br>|~~13,24~~<br>|~~13,24~~<br>|~~205,56~~<br>|~~205,56~~<br>|~~205,56~~<br>|
|Centro<br>Quintero|~~2023~~<br>|~~46,88~~<br>|~~46,88~~<br>|~~46,88~~<br>|~~10,67~~<br>|~~10,67~~<br>|~~10,67~~<br>|~~129,79~~<br>|~~129,79~~<br>|~~129,79~~<br>|
|<br>Loncura|~~2021~~<br>|~~65,63~~<br>|46,97|12,87|~~8,80~~<br>|6,54|8,18|~~152,18~~<br>|119,66|1196|
|<br>Loncura|~~2022~~<br>|~~43,64~~<br>|~~43,64~~<br>|~~43,64~~<br>|~~6,69~~<br>|~~6,69~~<br>|~~6,69~~<br>|~~129,48~~<br>|~~129,48~~<br>|~~129,48~~<br>|
|<br>Loncura|~~2023~~<br>|~~31,65~~<br>|~~31,65~~<br>|~~31,65~~<br>|~~4,14~~<br>|~~4,14~~<br>|~~4,14~~<br>|~~77,30~~<br>|~~77,30~~<br>|~~77,30~~<br>|
|Los<br>Maitenes|~~2021~~<br>|~~74,68~~<br>|77,68|21,28|~~21,33~~<br>|17,27|21,58|~~292,99~~<br>|278,16|27,81|
|Los<br>Maitenes|~~2022~~<br>|~~68,47~~<br>|~~68,47~~<br>|~~68,47~~<br>|~~15,34~~<br>|~~15,34~~<br>|~~15,34~~<br>|~~274,18~~<br>|~~274,18~~<br>|~~274,18~~<br>|
|Los<br>Maitenes|~~2023~~<br>|~~89,88~~<br>|~~89,88~~<br>|~~89,88~~<br>|~~15,13~~<br>|~~15,13~~<br>|~~15,13~~<br>|~~267,29~~<br>|~~267,29~~<br>|~~267,29~~<br>|
|<br>Quintero|~~2021~~<br>|~~92,98~~<br>|76,98|21,09|~~18,08~~<br>|13,84|17,30|~~331,28~~<br>|249,86|24,98|
|<br>Quintero|~~2022~~<br>|~~86,65~~<br>|~~86,65~~<br>|~~86,65~~<br>|~~13,96~~<br>|~~13,96~~<br>|~~13,96~~<br>|~~269,79~~<br>|~~269,79~~<br>|~~269,79~~<br>|
|<br>Quintero|~~2023~~<br>|~~51,30~~<br>|~~51,30~~<br>|~~51,30~~<br>|~~9,48~~<br>|~~9,48~~<br>|~~9,48~~<br>|~~148,48~~<br>|~~148,48~~<br>|~~148,48~~<br>|
|<br>La Greda|~~2021~~<br>|~~33,51~~<br>|30,22|8,28|~~13,06~~<br>|11,29|14,11|~~105,91~~<br>|79,61|7,96|
|<br>La Greda|~~2022~~<br>|~~34,74~~<br>|~~34,74~~<br>|~~34,74~~<br>|~~13,30~~<br>|~~13,30~~<br>|~~13,30~~<br>|~~90,69~~<br>|~~90,69~~<br>|~~90,69~~<br>|
|<br>La Greda|~~2023~~<br>|~~22,42~~<br>|~~22,42~~<br>|~~22,42~~<br>|~~7,51~~<br>|~~7,51~~<br>|~~7,51~~<br>|~~42,22~~<br>|~~42,22~~<br>|~~42,22~~<br>|
|<br>Puchuncaví|~~2021~~<br>|~~34,21~~<br>|31,98|8,76|~~15,02~~<br>|14,08|17,60|~~98,94~~<br>|81,75|8,17|
|<br>Puchuncaví|~~2022~~<br>|~~37,30~~<br>|~~37,30~~<br>|~~37,30~~<br>|~~16,16~~<br>|~~16,16~~<br>|~~16,16~~<br>|~~85,45~~<br>|~~85,45~~<br>|~~85,45~~<br>|
|<br>Puchuncaví|~~2023~~<br>|~~24,43~~<br>|~~24,43~~<br>|~~24,43~~<br>|~~11,06~~<br>|~~11,06~~<br>|~~11,06~~<br>|~~60,83~~<br>|~~60,83~~<br>|~~60,83~~<br>|
|Valle<br>Alegre|~~2021~~<br>|~~40,71~~<br>|34,11|9,34|~~17,07~~<br>|11,82|14,77|~~121,41~~<br>|95,59|9,55|
|Valle<br>Alegre|~~2022~~<br>|~~39,54~~<br>|~~39,54~~<br>|~~39,54~~<br>|~~12,80~~<br>|~~12,80~~<br>|~~12,80~~<br>|~~100,69~~<br>|~~100,69~~<br>|~~100,69~~<br>|
|Valle<br>Alegre|~~2023~~|~~22,06~~|~~22,06~~|~~22,06~~|~~5,58~~|~~5,58~~|~~5,58~~|~~64,64~~|~~64,64~~|~~64,64~~|

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Tabla 14. Estadísticos de Comparación Normas Primaria NO 2

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 42 de 252

|Estaciones|Años|P99<br>Horario|Promedio<br>Tri Anual|% Norma|Trianual|Promedio<br>Tri Anual|% Norma|
|---|---|---|---|---|---|---|---|
|Centro<br>Quintero|~~2021~~<br>|~~64,84~~<br>|104,78|26,20|~~16,83~~<br>|17,21|17,21|
|Centro<br>Quintero|~~2022~~<br>|~~187,04~~<br>|~~187,04~~<br>|~~187,04~~<br>|~~17,32~~<br>|~~17,32~~<br>|~~17,32~~<br>|
|Centro<br>Quintero|~~2023~~<br>|~~62,47~~<br>|~~62,47~~<br>|~~62,47~~<br>|~~17,48~~<br>|~~17,48~~<br>|~~17,48~~<br>|
|<br>Loncura|~~2021~~<br>|~~56,66~~<br>|51,25|12,81|~~11,40~~<br>|10,46|10,46|
|<br>Loncura|~~2022~~<br>|~~51,55~~<br>|~~51,55~~<br>|~~51,55~~<br>|~~10,01~~<br>|~~10,01~~<br>|~~10,01~~<br>|
|<br>Loncura|~~2023~~<br>|~~45,53~~<br>|~~45,53~~<br>|~~45,53~~<br>|~~9,98~~<br>|~~9,98~~<br>|~~9,98~~<br>|
|Los<br>Maitenes|~~2021~~<br>|~~57,34~~<br>|53,17|13,29|~~11,64~~<br>|10,62|10,62|
|Los<br>Maitenes|~~2022~~<br>|~~50,80~~<br>|~~50,80~~<br>|~~50,80~~<br>|~~10,59~~<br>|~~10,59~~<br>|~~10,59~~<br>|
|Los<br>Maitenes|~~2023~~<br>|~~51,36~~<br>|~~51,36~~<br>|~~51,36~~<br>|~~9,63~~<br>|~~9,63~~<br>|~~9,63~~<br>|
|<br>Quintero|~~2021~~<br>|~~59,56~~<br>|70,28|17,57|~~14,90~~<br>|15,37|15,37|
|<br>Quintero|~~2022~~<br>|~~92,59~~<br>|~~92,59~~<br>|~~92,59~~<br>|~~16,10~~<br>|~~16,10~~<br>|~~16,10~~<br>|
|<br>Quintero|~~2023~~<br>|~~58,69~~<br>|~~58,69~~<br>|~~58,69~~<br>|~~15,13~~<br>|~~15,13~~<br>|~~15,13~~<br>|
|<br>La Greda|~~2021~~<br>|~~57,85~~<br>|57,79|14,45|~~15,38~~<br>|16,95|16,95|
|<br>La Greda|~~2022~~<br>|~~52,70~~<br>|~~52,70~~<br>|~~52,70~~<br>|~~18,48~~<br>|~~18,48~~<br>|~~18,48~~<br>|
|<br>La Greda|~~2023~~<br>|~~62,83~~<br>|~~62,83~~<br>|~~62,83~~<br>|~~17,00~~<br>|~~17,00~~<br>|~~17,00~~<br>|
|<br>Puchuncaví|~~2021~~<br>|~~57,90~~<br>|54,52|13,63|~~15,41~~<br>|14,77|14,77|
|<br>Puchuncaví|~~2022~~<br>|~~54,80~~<br>|~~54,80~~<br>|~~54,80~~<br>|~~14,81~~<br>|~~14,81~~<br>|~~14,81~~<br>|
|<br>Puchuncaví|~~2023~~<br>|~~50,85~~<br>|~~50,85~~<br>|~~50,85~~<br>|~~14,10~~<br>|~~14,10~~<br>|~~14,10~~<br>|
|Valle<br>Alegre|~~2021~~<br>|~~55,70~~<br>|49,65|12,41|~~9,83~~<br>|10,40|10,40|
|Valle<br>Alegre|~~2022~~<br>|~~43,82~~<br>|~~43,82~~<br>|~~43,82~~<br>|~~8,99~~<br>|~~8,99~~<br>|~~8,99~~<br>|
|Valle<br>Alegre|~~2023~~|~~49,43~~|~~49,43~~|~~49,43~~|~~12,38~~|~~12,38~~|~~12,38~~|

Tabla 15. Estadísticos de Comparación Normas Primaria CO

|Estaciones|Años|P99<br>Horario|Promedio<br>Tri Anual|% Norma|P99 8<br>Horas|Promedio<br>Tri Anual|% Norma|
|---|---|---|---|---|---|---|---|
|Centro<br>Quintero|~~2021~~<br>|~~1,73~~<br>|1,70|5,67|~~1,15~~<br>|1,05|10,49|
|Centro<br>Quintero|~~2022~~<br>|~~1,84~~<br>|~~1,84~~<br>|~~1,84~~<br>|~~1,07~~<br>|~~1,07~~<br>|~~1,07~~<br>|
|Centro<br>Quintero|~~2023~~<br>|~~1,54~~<br>|~~1,54~~<br>|~~1,54~~<br>|~~0,93~~<br>|~~0,93~~<br>|~~0,93~~<br>|
|<br>Loncura|~~2021~~<br>|~~1,08~~<br>|1,37|4,56|~~0,77~~<br>|1,10|11|
|<br>Loncura|~~2022~~<br>|~~1,49~~<br>|~~1,49~~<br>|~~1,49~~<br>|~~1,26~~<br>|~~1,26~~<br>|~~1,26~~<br>|
|<br>Loncura|~~2023~~<br>|~~1,53~~<br>|~~1,53~~<br>|~~1,53~~<br>|~~1,27~~<br>|~~1,27~~<br>|~~1,27~~<br>|
|Los<br>Maitenes|~~2021~~<br>|~~0,79~~<br>|0,80|2,67|~~0,74~~<br>|0,55|5,54|
|Los<br>Maitenes|~~2022~~<br>|~~0,81~~<br>|~~0,81~~<br>|~~0,81~~<br>|~~0,44~~<br>|~~0,44~~<br>|~~0,44~~<br>|
|Los<br>Maitenes|~~2023~~<br>|~~0,81~~<br>|~~0,81~~<br>|~~0,81~~<br>|~~0,49~~<br>|~~0,49~~<br>|~~0,49~~<br>|
|<br>Quintero|~~2021~~<br>|~~1,46~~<br>|1,31|4,37|~~0,88~~<br>|0,70|7,02|
|<br>Quintero|~~2022~~<br>|~~1,40~~<br>|~~1,40~~<br>|~~1,40~~<br>|~~0,67~~<br>|~~0,67~~<br>|~~0,67~~<br>|
|<br>Quintero|~~2023~~|~~1,07~~|~~1,07~~|~~1,07~~|~~0,56~~|~~0,56~~|~~0,56~~|

LÍNEA DE BASE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**7 EMISIONES ATMOSFÉRICAS**

**7.1 IDENTIFICACIÓN DE FUENTES DE EMISIÓN**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 43 de 252

Las fuentes de emisión identificadas corresponden a las actividades consideradas por el
inventario de emisiones elaborado por parte de consultores GSI. Los criterios utilizados se
presentan a continuación:

Las fuentes fueron agrupadas según el tipo de fuente, considerando fuentes de área,
puntuales y volumétricas, las cuales fueron ingresadas al modelo de dispersión CALPUFF
para su respectiva modelación atmosférica. A continuación, se presenta una tabla resumen
con la clasificación de las fuentes provenientes de los tipos de actividades de acuerdo con el
proyecto:

Tabla 16. Actividades y tipología de fuentes

|Actividades|Fuente|
|---|---|
|~~Camino Pavimentado~~<br>|~~Área~~<br>|
|~~Excavaciones y movimientos de tierra~~<br>|~~Área~~<br>|
|~~Transferencia de material~~<br>|~~Volumétrica~~<br>|
|~~Combustión de maquinaria~~<br>|~~Área~~<br>|
|~~Combustión interna vehículos pesados~~|~~Área~~|
|Combustión interna de grupos<br>electrógenos<br>|Puntual<br>|
|~~Dispersión por acopio de material~~|~~Área~~|

Lo anterior es considerado para la etapa del proyecto del presente informe, donde la gran
diferencia es presentada en los frentes de trabajo, los cuales van cambiando
geográficamente dentro del área del proyecto y las tasas de emisión que son consecuencia
de lo anterior.

**7.2 TASAS DE EMISIÓN**

Al igual que el punto 7.1, las tasas de emisión consideradas provienen del inventario de
emisiones realizado por los consultores de GSI. Dado que el proyecto consta de varias
etapas o escenarios, se ha decidido combinar las emisiones de actividades comunes en
ciertos frentes de trabajo durante las etapas que se superponen en el tiempo, basado en el
cronograma, para obtener una proyección anual.

EMISIONES ATMOSFÉRICAS **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Figura 16. Cronograma de obras fase construcción

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 44 de 252

Fuente: GSI Consultores 2024.

Posteriormente las emisiones fueron distribuidas en los distintos frentes de trabajo en
proporción de las emisiones de cada etapa o escenario considerando el cronograma de la
descripción del proyecto junto a la cartografía de las etapas del proyecto.

**7.3 CONFORMACIÓN DE ESCENARIOS DE MODELACIÓN**

De acuerdo con las actividades descritas en el cronograma de las obras del proyecto, se han
establecido los siguientes escenarios de modelación:

Tabla 17. Escenarios de modelación

|Escenarios modelación|Fuentes|
|---|---|
|E1:<br>Escenario 1|Proyecto Maitencillo Etapa 1|
|E1:<br>Escenario 1|-PEAS 1, PEAS 2, PEAS 3 e impulsiones|
|E1:<br>Escenario 1|-PEAS 5.1 e impulsión|
|E1:<br>Escenario 1|-PEAS 5.2 e impulsión|
|E1:<br>Escenario 1|-Red Primaria de A.S.|
|E1:<br>Escenario 1||
|E1:<br>Escenario 1|Sistema Planta de Tratamiento|
|E1:<br>Escenario 1|-Proyecto PTAS Maitencillo Etapa 1|
|E2:<br>Escenario 2|Proyecto Maitencillo Etapa 2|
|E2:<br>Escenario 2|-PEAS 6, PEAS 7, PEAS 8 e impulsiones|
|E2:<br>Escenario 2|-Red Primaria de A.S.|
|E3:<br>Escenario 3|Proyecto Maitencillo Etapa 3|
|E3:<br>Escenario 3|-PEAS 9, PEAS 10 e impulsiones|
|E4:<br>Escenario 4|Proyecto Maitencillo Etapa 4|
|E4:<br>Escenario 4|-Red Primaria de A.S.|
|E4:<br>Escenario 4||
|E4:<br>Escenario 4|Sistema Planta de Tratamiento|
|E4:<br>Escenario 4|-Proyecto PTAS Maitencillo Etapa 2|
|E5:<br>Escenario 5|Sistema Planta de Tratamiento|
|E5:<br>Escenario 5|-Proyecto PTAS Maitencillo Etapa 3|

EMISIONES ATMOSFÉRICAS **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 45 de 252

A continuación, se presentan las emisiones de cada etapa del proyecto en unidades de

[kg/día] consideradas para la modelación de dispersión de contaminantes, para:

Tabla 18. Actividades del proyecto y Emisiones Etapa 1 y 2

|Fase|Etapa<br>Proyecto|Tipo de Emisión|MP<br>10<br>[kg/d]|MP<br>2,5<br>[kg/d]|MPS<br>[kg/d]|SO<br>2<br>[kg/d]|NOX<br>[kg/d]|CO<br>[kg/d]|
|---|---|---|---|---|---|---|---|---|
|Construcción|1|Camino<br>Pavimentado|0,471|0,114|0,140|0,000|0.00|0.00|
|Construcción|1|Excavaciones y<br>Movimientos de<br>Tierra|39,812|20,435|194,617|0,000|0.00|0.00|
|Construcción|1|Transferencia<br>de Material|1,482|0,224|2,345|0,000|0.00|0.00|
|Construcción|1|Combustión de<br>Maquinaria|0,000|0,000|0,000|0,000|0.00|0.00|
|Construcción|1|Combustión<br>Interna<br>Vehículos<br>Pesados|0,000|0,000|0,000|0,016|0.25|0.06|
|Construcción|1|Combustión<br>Interna Grupo|0,633|0,153|0,000|0,000|17.97|3.88|
|Construcción|1 <br>|Dispersión por<br>Acopio de<br>Material<br>|1,576<br>|0,247<br>|1,695<br>|0,000<br>|0.00<br>|0.00<br>|
|~~TOTAL~~|~~TOTAL~~|~~TOTAL~~|~~43.974~~|~~21.173~~|~~198,796~~|~~0,016~~|~~18,219~~|~~3,940~~|
|Construcción|2|Camino<br>Pavimentado|0,216|0,052|0,064|0,000|0.000|0.000|
|Construcción|2|Excavaciones y<br>Movimientos de<br>Tierra|9,959|5,112|48,683|0,000|0.000|0.000|
|Construcción|2|Transferencia<br>de Material|0,377|0,057|0,596|0,000|0.000|0.000|
|Construcción|2|Combustión de<br>Maquinaria|0,000|0,000|0,000|0,000|0.000|0.000|
|Construcción|2|Combustión<br>Interna<br>Vehículos<br>Pesados|0,000|0,000|0,000|0,024|0.298|0.071|
|Construcción|2|Combustión<br>Interna Grupo|0,633|0,153|0,000|0,000|17.972|3.881|
|Construcción|2 <br>|Dispersión por<br>Acopio de<br>Material<br>|0,410<br>|0,064<br>|0,440<br>|0,000<br>|0.000<br>|0.000<br>|
|~~TOTAL~~|~~TOTAL~~|~~TOTAL~~|~~11.595~~|~~5.438~~|~~49,784~~|~~0,024~~|~~18,269~~|~~3,952~~|

EMISIONES ATMOSFÉRICAS **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Tabla 19. Actividades del proyecto y Emisiones Etapa 3 y 4

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 46 de 252

|Fase|Etapa<br>Proyecto|Tipo de Emisión|MP<br>10<br>[kg/d]|MP<br>2,5<br>[kg/d]|MPS<br>[kg/d]|SO<br>2<br>[kg/d]|NOX<br>[kg/d]|CO<br>[kg/d]|
|---|---|---|---|---|---|---|---|---|
|Construcción|3|Camino<br>Pavimentado|0,035|0,009|0,010|0,000|0.000|0.000|
|Construcción|3|Excavaciones y<br>Movimientos de<br>Tierra|2,242|1,151|10,959|0,000|0.000|0.000|
|Construcción|3|Transferencia de<br>Material|0,139|0,021|0,219|0,000|0.000|0.000|
|Construcción|3|Combustión de<br>Maquinaria|0,000|0,000|0,000|0,000|0.000|0.000|
|Construcción|3|Combustión<br>Interna<br>Vehículos<br>Pesados|0,000|0,000|0,000|0,007|0.098|0.023|
|Construcción|3|Combustión<br>Interna Grupo|0,172|0,042|0,000|0,000|4.892|1.056|
|Construcción|3 <br>|Dispersión por<br>Acopio de<br>Material<br>|0,181<br>|0,028<br>|0,195<br>|0,000<br>|0.000<br>|0.000<br>|
|~~TOTAL~~|~~TOTAL~~|~~TOTAL~~|~~2.769~~|~~1.250~~|~~11,384~~|~~0,007~~|~~4,990~~|~~1,080~~|
|Construcción|4|Camino<br>Pavimentado|0,018|0,004|0,005|0,000|0.000|0.000|
|Construcción|4|Excavaciones y<br>Movimientos de<br>Tierra|1,270|0,652|6,208|0,000|0.000|0.000|
|Construcción|4|Transferencia de<br>Material|0,042|0,006|0,067|0,000|0.000|0.000|
|Construcción|4|Combustión de<br>Maquinaria|0,000|0,000|0,000|0,000|0.000|0.000|
|Construcción|4|Combustión<br>Interna<br>Vehículos<br>Pesados|0,000|0,000|0,000|0,008|0.138|0.033|
|Construcción|4|Combustión<br>Interna Grupo|0,172|0,042|0,000|0,000|4.892|1.056|
|Construcción|4 <br>|Dispersión por<br>Acopio de<br>Material<br>|0,043<br>|0,007<br>|0,046<br>|0,000<br>|0.000<br>|0.000<br>|
|~~TOTAL~~|~~TOTAL~~|~~TOTAL~~|~~1.546~~|~~0.711~~|~~6,327~~|~~0,008~~|~~5,029~~|~~1,089~~|

EMISIONES ATMOSFÉRICAS **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Tabla 20. Actividades del proyecto y Emisiones Etapa PTAS 1 y 2

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 47 de 252

|Fase|Etapa<br>Proyecto|Tipo de Emisión|MP<br>10<br>[kg/d]|MP<br>2,5<br>[kg/d]|MPS<br>[kg/d]|SO<br>2<br>[kg/d]|NOX<br>[kg/d]|CO<br>[kg/d]|
|---|---|---|---|---|---|---|---|---|
|Construcción|1 PTAS|Camino<br>Pavimentado|0,013|0,003|0,004|0,000|0.000|0.000|
|Construcción|1 PTAS|Excavaciones<br>y <br>Movimientos<br>de<br>Tierra|3,814|1,958|18,644|0,000|0.000|0.000|
|Construcción|1 PTAS|Transferencia<br>de<br>Material|0,131|0,020|0,207|0,000|0.000|0.000|
|Construcción|1 PTAS|Combustión<br>de<br>Maquinaria|0,000|0,000|0,000|0,000|0.000|0.000|
|Construcción|1 PTAS|Combustión<br>Interna Vehículos<br>Pesados|0,000|0,000|0,000|0,002|0.044|0.010|
|Construcción|1 PTAS|Combustión<br>Interna Grupo|0,086|0,021|0,000|0,000|2.453|0.530|
|Construcción<br>|1 PTAS|Dispersión<br>por<br>Acopio de Material|0,116<br>|0,018<br>|0,125<br>|0,000<br>|0.000<br>|0.000<br>|
|~~TOTAL~~|~~TOTAL~~|~~TOTAL~~|~~4.160~~|~~2.020~~|~~18,980~~|~~0,002~~|~~2,497~~|~~0,540~~|
|Construcción|2 PTAS|Camino<br>Pavimentado|0,002|0,001|0,001|0,000|0.000|0.000|
|Construcción|2 PTAS|Excavaciones<br>y <br>Movimientos<br>de<br>Tierra|0,464|0,238|2,266|0,000|0.000|0.000|
|Construcción|2 PTAS|Transferencia<br>de<br>Material|0,018|0,003|0,028|0,000|0.000|0.000|
|Construcción|2 PTAS|Combustión<br>de<br>Maquinaria|0,000|0,000|0,000|0,000|0.000|0.000|
|Construcción|2 PTAS|Combustión<br>Interna Vehículos<br>Pesados|0,000|0,000|0,000|0,002|0.037|0.009|
|Construcción|2 PTAS|Combustión<br>Interna Grupo|0,086|0,021|0,000|0,000|2.453|0.530|
|Construcción<br>|2 PTAS|Dispersión<br>por<br>Acopio de Material|0,018<br>|0,003<br>|0,020<br>|0,000<br>|0.000<br>|0.000<br>|
|~~TOTAL~~|~~TOTAL~~|~~TOTAL~~|~~0.589~~|~~0.265~~|~~2,315~~|~~0,002~~|~~2,489~~|~~0,538~~|

EMISIONES ATMOSFÉRICAS **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Tabla 21. Actividades del proyecto y Emisiones Etapa PTAS 3

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 48 de 252

|Fase|Etapa<br>Proyecto|Tipo de Emisión|MP<br>10<br>[kg/d]|MP<br>2,5<br>[kg/d]|MPS<br>[kg/d]|SO<br>2<br>[kg/d]|NOX<br>[kg/d]|CO<br>[kg/d]|
|---|---|---|---|---|---|---|---|---|
|Construcción|3 PTAS|Camino<br>Pavimentado|0,003|0,001|0,001|0,000|0,000|0,000|
|Construcción|3 PTAS|Excavaciones y<br>Movimientos de<br>Tierra|0,713|0,366|3,488|0,000|0,000|0,000|
|Construcción|3 PTAS|Transferencia de<br>Material|0,028|0,004|0,044|0,000|0,000|0,000|
|Construcción|3 PTAS|Combustión de<br>Maquinaria|0,000|0,000|0,000|0,000|0,000|0,000|
|Construcción|3 PTAS|Combustión<br>Interna<br>Vehículos<br>Pesados|0,000|0,000|0,000|0,002|0,037|0,009|
|Construcción|3 PTAS|Combustión<br>Interna Grupo|0,086|0,021|0,000|0,000|2,453|0,530|
|Construcción|3 PTAS<br>|Dispersión por<br>Acopio de<br>Material|0,028<br>|0,004<br>|0,031<br>|0,000<br>|0,000<br>|0,000<br>|
|~~TOTAL~~|~~TOTAL~~|~~TOTAL~~|~~0,859~~|~~0,397~~|~~3,563~~|~~0,002~~|~~2,489~~|~~0,538~~|

EMISIONES ATMOSFÉRICAS **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**7.4 OTRAS CONSIDERACIONES**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 49 de 252

A continuación, se presentan criterios aplicados para la modelación de calidad del aire:

Emisiones y su temporalidad

Las tasas de emisiones indicadas anteriormente fueron convertidas a [g/s] y en [g/m [2] s], para
su ingreso al modelo de dispersión.

Se consideró las horas de trabajo diurno, esto es 12 horas diarias del ejercicio de las labores,
tomando en cuenta lo indicado en la sección de ruido del Capítulo 2: Descripción del
proyecto.

El ciclo de emisión de las fuentes consideró nivel de actividad según inventario de emisiones
de GSI, cuya temporalidad se presenta al final del presente informe.

Tránsito de vehículos en caminos

La ubicación de los caminos fue en base a la cartografía de Rutas del Proyecto.

Se consideró los principales ingresos a Maitencillo por el norte, ruta E-46 y E-30F y por el
sur, la ruta F-30 E.

Los caminos considerados se enmarcaron en el sector área del proyecto, de acuerdo con la
figura de Ubicación general del Proyecto, según lo indicado por el mandante.

La totalidad de los caminos fueron considerados como pavimentados.

Grupos electrógenos

Para la representación de los grupos electrógenos, se utilizaron características de referencia
provenientes del estudio Anexo 6.1: Línea de Base Meteorología, Calidad del Aire y
Modelación Meteorológica del EIA Concesión Américo Vespucio Oriente. Tramo Avenida El
Salto.

EMISIONES ATMOSFÉRICAS **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**8 RECEPTORES DISCRETOS**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 50 de 252

Para la evaluación de las normas primarias y secundarias del aire se han identificado un total
de 26 receptores, ubicados en las cercanías del proyecto. Estos fueron considerados en
base al estudio de ruido y olores, los cuales fueron definidos por el titular en función de la
cercanía con las obras a ejecutar en el presente proyecto. Por otro lado, se evaluó como
punto receptor la Estación Puchuncaví, la cual fue seleccionada en base a su cercanía con el
proyecto. A su vez, esta estación es caracterizada como EMRP (Estación Monitora con
Representativa Poblacional) para gases y MP 10, bajo resolución N°305/2004 y N°1924/2000.

Tabla 22. Receptores discretos parte 1

|ID|Coordenadas UTM [m]<br>(WGS84-H19S)|Col3|Descripción|Col5|
|---|---|---|---|---|
|ID|X:Este|Y: Sur|Y: Sur|Y: Sur|
|R1|273.467|6.387.304|Receptor ruido 1|Receptor 1, corresponde a una vivienda existente ubicada<br>dentro del límite urbano del Plan Regulador Comunal de<br>Putaendo, específicamente en la zona Z4.<br>Por otro lado, el receptor se encuentra dentro del límite del<br>Plan Regulador Intercomunal de Valparaíso -Satélite Borde<br>Costero Norte, específicamente en la zona área urbana<br>(AU).|
|R2|273.165|6.386.964|Receptor ruido 2|Receptor 2, corresponde a una vivienda existente ubicada<br>dentro del límite urbano del Plan Regulador Comunal de<br>Putaendo, específicamente en la zona Z4.<br>Por otro lado, el receptor se encuentra dentro del límite del<br>Plan Regulador Intercomunal de Valparaíso -Satélite Borde<br>Costero Norte, específicamente en la zona área urbana<br>(AU).|
|R3|272.667|6.386.718|Receptor ruido 3|Receptor 3, corresponde a una vivienda existente ubicada<br>dentro del límite urbano del Plan Regulador Comunal de<br>Putaendo, específicamente en la zona ZRR.<br>Por otro lado, el receptor se encuentra dentro del límite del<br>Plan Regulador Intercomunal de Valparaíso -Satélite Borde<br>Costero Norte, específicamente en la zona área urbana<br>(AU).|
|R4|272.686|6.386.266|Receptor ruido 4|Receptor 4, corresponde a una vivienda existente ubicada<br>dentro del límite urbano del Plan Regulador Comunal de<br>Putaendo, específicamente en la zona Z4.<br>Por otro lado, el receptor se encuentra dentro del límite del<br>Plan Regulador Intercomunal de Valparaíso -Satélite Borde<br>Costero Norte, específicamente en la zona área urbana<br>(AU).|
|R5|272.095|6.386.403|Receptor ruido 5|Receptor 5, corresponde a un acceso a la zona costera<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z6.<br>Por otro lado, el receptor se encuentra dentro del límite del<br>Plan Regulador Intercomunal de Valparaíso -Satélite Borde<br>Costero Norte, específicamente en la zona área urbana<br>(AU).|

RECEPTORES DISCRETOS **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Tabla 23. Receptores discretos parte 2

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 51 de 252

|ID|Coordenadas UTM [m]<br>(WGS84-H19S)|Col3|Descripción|Col5|
|---|---|---|---|---|
|ID|X: Este|Y: Sur|Y: Sur|Y: Sur|
|R6|272.061|6.386.029|Receptor ruido 6|Receptor 6, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z6.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU).|
|R7|272.062|6.385.336|Receptor ruido 7|Receptor 7, corresponde Retén Mitencillo ubicada dentro<br>del límite urbano del Plan Regulador Comunal de<br>Putaendo, específicamente en la zona Z9.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU).|
|R8|272.550|6.385.155|Receptor ruido 8|Receptor 8, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z9.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU).|
|R9|272.361|6.384.963|Receptor ruido 9|Receptor 9, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z9.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU).|
|R10|272.633|6.384.083|Receptor ruido 10|Receptor 10, corresponde a la planta elevadora ubicada<br>fuera del límite urbano del Plan Regulador Comunal de<br>Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU).|
|R11|271.742|6.385.511|Receptor ruido 12|Receptor 11, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z7.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU).|
|R12|271.303|6.385.031|Receptor ruido 13|Receptor 12, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z7.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU).|
|R13|270.870|6.384.346|Receptor ruido 14|Receptor 13, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z7.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU).|

RECEPTORES DISCRETOS **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Tabla 24. Receptores discretos parte 3

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 52 de 252

|ID|Coordenadas UTM [m]<br>(WGS84-H19S)|Col3|Descripción|Col5|
|---|---|---|---|---|
|ID|X: Este|Y: Sur|Y: Sur|Y: Sur|
|R14|271.064|6.383.040|Receptor ruido 15|Receptor 14, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z6.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU).|
|R15|271.195|6.382.539|Receptor ruido 16|Receptor 15, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z5.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU).|
|R16|273.437|6.383.498|Receptor fauna|Receptor 16, corresponde a un punto receptor de fauna<br>ubicado en una zona boscosa presente fuera del límite<br>urbano del Plan Regulador Comunal de Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte (ZEU 20).|
|R17|272.900|6.384.175|Receptor olor 1|Receptor 17, corresponde a una vivienda existente fuera<br>del límite urbano del Plan Regulador Comunal de<br>Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte (ZEU 20).|
|R18|273.262|6.384.342|Receptor olor 2|Receptor 18, corresponde a una vivienda existente fuera<br>del límite urbano del Plan Regulador Comunal de<br>Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte (ZEU 20).|
|R19|273.332|6.384.523|Receptor olor 3|Receptor 19, corresponde a una vivienda existente fuera<br>del límite urbano del Plan Regulador Comunal de<br>Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte (ZEU 20).|
|R20|273.201|6.382.149|Receptor olor 4|Receptor 20 corresponde a una vivienda existente<br>situada fuera del límite urbano del Plan Regulador<br>Comunal de Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso - Satélite<br>Borde Costero Norte (ZEU 20).|
|R21|274.626|6.383.665|Receptor olor 5|Receptor<br>21,<br>corresponde<br>a <br>instalación<br>de<br>telecomunicaciones existente fuera del límite urbano del<br>Plan Regulador Comunal de Puchuncaví,<br>Por otro lado, el receptor se encuentra fuera del límite del<br>Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte (Área Rural).|
|R22|275.043|6.382.044|Receptor olor 6|Receptor 22, corresponde a una vivienda existente fuera<br>del límite urbano del Plan Regulador Comunal de<br>Puchuncaví.<br>Por otro lado, el receptor se encuentra fuera del límite del<br>Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte (Área Rural).|

RECEPTORES DISCRETOS **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Tabla 25. Receptores discretos parte 4

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 53 de 252

|ID|Coordenadas UTM [m]<br>(WGS84-H19S)|Col3|Descripción|Col5|
|---|---|---|---|---|
|ID|X: Este|X: Este|X: Este|X: Este|
|R23|272.529|6.383.695|Receptor olor 7|Receptor 23, corresponde a una vivienda existente fuera<br>del límite urbano del Plan Regulador Comunal de<br>Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona de<br>extensión urbana 3 (ZEU 23 B).|
|R24|272.543|6.383.117|Receptor olor 8|Receptor 24, corresponde a una vivienda existente fuera<br>del límite urbano del Plan Regulador Comunal de<br>Puchuncaví,<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona de<br>extensión urbana 3 (ZEU 23 B).|
|R25|272.512|6.382.513|Receptor olor 9|Receptor 25, Centro comercial Pronto Copec, fuera del<br>límite<br>urbano<br>del<br>Plan<br>Regulador<br>Comunal<br>de<br>Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona de<br>extensión urbana 3 (ZEU 23 B).|
|R26|274.379|6.377.371|Estación Puchuncaví|Receptor 26, Estación meteorológica y calidad del aire<br>Puchuncaví, se encuentra dentro del límite urbano del<br>Plan Regulador Comunal de Putaendo, específicamente<br>en la zona Z4.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU).|

RECEPTORES DISCRETOS **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 54 de 252

Figura 17. Ubicación de receptores discretos

Fuente: Elaborado por Are Project, basado en Google Earth 2020.

RECEPTORES DISCRETOS **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**9 ANÁLISIS DE INCERTIDUMBRE**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 55 de 252

Los modelos utilizados en la evaluación de calidad del aire son potentes herramientas
matemáticas que representan una aproximación de los procesos atmosféricos que ocurren
en la realidad. No obstante, los resultados de las modelaciones tienen incertidumbres
asociadas, las cuales se expresan por medio de las diferencias entre lo estimado (modelado)
y las observaciones (mediciones). Por otra parte, tal como lo señala la Guía de Uso de
modelos para la calidad del aire en el SEIA, _“...un análisis de incertidumbre tiene como_
_objetivo evaluar la capacidad de un modelo de representar una cierta situación atmosférica._
_En este sentido, es importante señalar que este análisis no es ningún juicio sobre la bondad_
_del modelo o su usuario, sino sólo un reconocimiento de que ningún modelo es capaz de_
_representar la atmósfera en forma exacta y que, además, su desempeño depende de cada_
_situación particular “._

En lo que se refiere a la dispersión de contaminantes atmosféricos, la meteorología es clave
en la variabilidad de las concentraciones de los contaminantes, siendo necesario analizar la
incertidumbre de las variables meteorológicas relevantes, las cuales corresponden a la
velocidad y dirección del viento, temperatura y la humedad relativa (Servicio de Evaluación
Ambiental, 2023). Sin embargo, no siempre ha de existir información y validada.

El análisis de incertidumbre pretende estimar las diferencias entre lo estimado y lo
observado. Para el caso de la meteorología, la evaluación se debe centrar tanto a nivel de
altura como superficial. Sin embargo, en Chile, los datos meteorológicos de altura son
escasos. La fuente de información pública relacionada a la medición por medio de
radiosondeos, está a cargo de la Dirección Meteorológica de Chile (DCM), la cual realiza
mediciones en las localidades de Antofagasta, Santo Domingo, Puerto Montt y Punta Arenas,
principalmente.
En base a lo planteado, el análisis presentado para el presente estudio consideró la
evaluación de la incertidumbre del modelo meteorológico de pronóstico WRF, aplicado para
el período del año 2023, siendo contrastado con información de 3 estaciones meteorológicas
superficiales correspondiente a la red de monitoreo del Sistema de Información Nacional de
Calidad del Aire (SINCA) para el mismo período. A continuación, la siguiente tabla describe
la ubicación de cada estación considerada.

Tabla 26. Coordenadas de ubicación estaciones meteorológicas superficiales

|ID|Nombre<br>estación|Distancia hacia<br>proyecto [km]|Coordenadas UTM [m] WGS-84 Huso 19 Sur|Col5|
|---|---|---|---|---|
|ID|Nombre<br>estación|Distancia hacia<br>proyecto [km]|X: Este|Y: Sur|
|1 <br>2 <br>3|Puchuncaví<br>La Greda<br>Ventanas|7,32<br>11,43<br>11,09|274.379<br>268.185<br>267.546|6.377.331<br>6.373.910<br>6.374.609|

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 56 de 252

Las estaciones fueron seleccionadas según cercanía hacia el proyecto en estudio,
representatividad meteorológica, altura de medición y porcentaje de datos válidos, según los
criterios establecidos en la Guía de Uso de modelos para la calidad del aire en el SEIA. Las
variables analizadas y disponibles corresponden a velocidad y dirección del viento, cuyos
datos han sido validados de acuerdo con los criterios establecidos en la guía EPA
Meteorological Monitoring Guidance for Regulatory Modeling Applications. Los resultados de
la validación de datos son exhibidos en la siguiente tabla, donde se alcanzó sobre el 75% de
los datos validados, cumpliendo el criterio para la realización del análisis de incertidumbre.

Tabla 27. Porcentaje de datos validados en estaciones meteorológicas superficiales

|ID|Nombre|% de datos válidos por variable meteorológica|Col4|
|---|---|---|---|
|ID|Nombre|Dirección del viento|Velocidad del viento|
|1 <br>2 <br>3|Puchuncaví<br>La Greda<br>Ventanas|99,74%<br>99,60%<br>99,24%|92,98%<br>87,43%<br>97,96%|

El análisis sólo consideró información meteorológica superficial, debido a que no se dispone
de información validada de altura y cercana al área de estudio.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**9.1 DESCRIPCIÓN DEL ANÁLISIS CUALITATIVO Y CUANTITATIVO**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 57 de 252

El análisis de incertidumbre consideró el contraste entre lo simulado y lo observado. Para
esto, se realizó la extracción de las series de los datos simulados por el modelo
meteorológico de pronóstico WRF en las coordenadas de ubicación de las estaciones
superficiales seleccionadas, para las variables de velocidad y dirección del viento a la
altura de 10 [m], de acuerdo con la medición observada. La información es presentada
según:

Análisis cualitativo: Comparaciones entre datos meteorológicos simulados y observados.

Series de datos: Estos gráficos permiten un análisis cualitativo de los datos en términos

de completitud de la serie y periodos con datos faltantes, valores fuera de rango y
problemas de equipo (estación meteorológica superficial).

Ciclos diarios: Estos gráficos muestran la variación típica de cada variable como su

variabilidad interdiaria.

- Ciclos estacionales: En ellos se visualiza la variación estacional de sus ciclos diarios

para las variables analizadas.

Rosas de viento: Permiten ilustrar la variabilidad del viento en términos de velocidad y

dirección para ciclos anuales y horarios.

Análisis cuantitativo: Aplicación de métricas estadísticas para la evaluación de la precisión
de la simulación meteorológica respecto de lo observado, los índices utilizados
correspondieron a:

- Error cuadrático medio: Corresponde a la medida de diferencias en promedio entre los

valores pronosticados y los observados, definido como (Pielke R., 1984):

N
#### RMSE = √∑

i=1

(∅ i − ∅ iobs ) [2]

N

##### Dónde: ∅ i Corresponde al valor pronóstico en el tiempo i ∅ iobs Corresponde al valor observado en el tiempo i

N Corresponde al número de datos analizados.

- Error absoluto medio: Señala la varianza residual entre los valores pronosticados y

observados (Stauffer & Seaman, 1990):

N

### MAE = ∑

i=1

∅ i − ∅ iobs

N

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

̅ ̅

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 58 de 252

̅ ̅

- Error absoluto medio: Toma en cuenta el peso del error respecto al valor de la variable

medida, normaliza el error absoluto (Stauffer & Seaman, 1990):

̅ ̅

N

### NMAE = ∑

̅ ̅

|∅ i − ∅ iobs |

̅ ̅

⁄

̅ ̅

##### ∅ iobs

̅ ̅

N
i=1

Sesgo (BIAS): Proporciona información sobre la tendencia del modelo a sobrestimar o

̅ ̅

subestimar una variable

̅ ̅

N

### BIAS = ∑

i=i

̅ ̅

(∅ i − ∅ iobs )

N

̅ ̅

 El Índice de Acuerdo (IOA): Medida de la coincidencia entre la salida de cada predicción

de la media observada y la salida de cada observación de la media observada. Así, la
correspondencia entre las predicciones y los valores observados a través del dominio
en un momento dado pueden ser cuantificados en un solo métrico y se muestra como
una serie de tiempo. El índice de acuerdo tiene un rango teórico de 0 a 1, la última
puntuación sugiere un acuerdo perfecto. ∑ N (P i − O i ) 2

IOA = 1 − i=1
~~∑~~ ~~[N]~~ ~~(|P~~ i ~~− O~~ mean ~~| + |O~~ i ~~− O~~ mean ~~|)~~ ~~[2]~~

i=1

Dónde: N es el número de observaciones
P i son los valores pronosticados
O i son los valores observados

O mean es la medida de las observaciones

 - Coeficiente de correlación Pearson: Un índice que mide el grado de relación de dos

variables siempre y cuando ambas sean cuantitativas.

[(x] [i] [ − x̅) (y] [i] [ − y̅) ]
∑ i [n] =1
r = ̅ ̅
##### ~~√ ∑ [n] (x i − x) [2] ∑ [n] (y 1 − y) [2]~~

i=1 i=1

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

**9.2 ANÁLISIS CUALITATIVO: VELOCIDAD DEL VIENTO**

**9.2.1 VELOCIDAD DEL VIENTO ESTACIÓN PUCHUNCAVÍ**

A continuación, se presentan las comparaciones entre lo modelado y observado por estación.

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 59 de 252

Figura 18. Serie de tiempo velocidad del viento modelada
Estación Puchuncaví

Figura 19. Serie de tiempo velocidad del viento
observada Estación Puchuncaví

Al evaluar las series de tiempo tanto modelada como observada en la estación Puchuncaví, estas presentaron registros
dentro del rango esperado.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 60 de 252

Figura 20. Ciclo diario velocidad del viento modelada
Estación Puchuncaví

Figura 21. Ciclo diario velocidad del viento observada
Estación Puchuncaví

En cuanto al ciclo diario, el modelo reprodujo la curva de los promedios observados y su tendencia, sin embargo,
sobreestimó la velocidad del viento principalmente entre las 14:00 y 18:00 [h], con una máxima de 1,1 [m/s] en promedio.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 61 de 252

Figura 22. Comparativo porcentaje de frecuencia de vientos calmos modelada y observada Estación Puchuncaví

Al comparar la frecuencia de vientos inferiores a 0,5 [m/s], el modelo sobreestimó la frecuencia para el ciclo AM
principalmente entre las 08:00 y 10:00 [h], arrojando una diferencia máxima de 25%, durante el periodo PM y nocturno se
subestima la frecuencia con un máximo de 14%.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

**9.2.2 VELOCIDAD DEL VIENTO ESTACIÓN LA GREDA**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 62 de 252

Figura 23. Serie de tiempo velocidad del viento modelada
Estación La Greda

Figura 24. Serie de tiempo velocidad del viento
observada Estación La Greda

Del análisis de las gráficas, se pudo apreciar valores dentro del rango esperado de velocidad. Por otro lado, no se
apreciaron periodos extensos de datos faltantes.

.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 63 de 252

Figura 25. Ciclo diario velocidad del viento modelada
Estación La Greda

Figura 26. Ciclo diario velocidad del viento observada
Estación La Greda

Al comparar los ciclos diarios, el modelo logró reproducir la curva de los promedios y tendencia observada. Sin embargo,
presentó una leve subestimación en los vientos durante el periodo AM, con una máxima promedio de 0,8 [m/s].

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 64 de 252

Figura 27. Comparativo porcentaje de frecuencia de vientos calmos modelada y observada - Estación La Greda

En cuanto a la frecuencia de vientos calmos, el modelo sobreestimó a lo observado. Principalmente en horario AM y PM,
con una diferencia máxima de 36%.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

**9.2.3 VELOCIDAD DEL VIENTO ESTACIÓN VENTANAS**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 65 de 252

Figura 28. Serie de tiempo velocidad del viento modelada
Estación Ventanas

Figura 29. Serie de tiempo velocidad del viento observada
Estación Ventanas

En cuanto a la estación Ventanas, presentó registros dentro del rango esperado sin anomalías en las velocidades de
viento. No se observaron periodo de datos faltantes extensos en dicha estación.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 66 de 252

Figura 30. Ciclo diario velocidad del viento modelada
Estación Ventanas

Figura 31. Ciclo diario velocidad del viento observada
Estación Ventanas

De la gráfica, se tiene que el modelo logra reproducir la tendencia de los promedios observados, subestimando la
velocidad del viento con un promedio de 0,4 [m/s], durante todo el ciclo horario.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 67 de 252

Figura 32. Comparativo porcentaje de frecuencia de vientos calmos modelada y observada - Estación Ventanas

En la comparación de frecuencias de vientos calmos modelada y observada, el modelo sobreestimó lo observado en la
totalidad del ciclo diario evaluado, con una diferencia máxima de hasta 23%.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

**9.3 ANÁLISIS CUALITATIVO: DIRECCIÓN DEL VIENTO**

**9.3.1 DIRECCIÓN DEL VIENTO ESTACIÓN PUCHUNCAVÍ**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 68 de 252

Figura 33. Ciclo diario dirección del viento modelada
Estación Puchuncaví

Figura 34. Ciclo diario dirección del viento observada
Estación Puchuncaví

Es posible visualizar que el modelo reprodujo el comportamiento de la dirección del viento observado. Con diferencias en
la frecuencia de los vientos predominantes.
El modelo presentó mayor frecuencia para el rango 220° a 260°, un 28,95%. Mientras que lo observado la mayor
frecuencia estuvo en el rango 280° a 320° con un 27,15%.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 69 de 252

Figura 35. Ciclo estacional dirección del viento modelada
Estación Puchuncaví

Figura 36. Ciclo estacional dirección del viento observada
Estación Puchuncaví

Al comparar ambas gráficas, se observó que el modelo reprodujo la variabilidad de los campos de vientos observados,
tanto para el ciclo horario como mensual, no obstante, presentó sobreestimación en la velocidad del viento, acentuándose
mayormente en los meses de verano-primavera en horarios AM y PM. Mientras que en los meses de otoño-invierno, la
sobrestimación estuvo marcada en el mes de agosto, en horario PM.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

**9.3.2 DIRECCIÓN DEL VIENTO ESTACIÓN LA GREDA**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 70 de 252

Figura 37. Ciclo diario dirección del viento modelada
Estación La Greda

Figura 38. Ciclo diario dirección del viento observada
Estación La Greda

Se puede observar que en general el modelo logró reproducir la variabilidad direccional horaria de lo observado en la
Estación La Greda, no obstante, presentó subestimación en las direcciones de mayor frecuencia respecto a lo observado.
El modelo presentó mayor frecuencia para el rango 220° a 280° (37,41%). Mientras que lo observado la mayor frecuencia
estuvo en el rango 240° a 300° (32,46%).

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 71 de 252

Figura 39. Ciclo estacional dirección del viento modelada
Estación La Greda

Figura 40. ciclo estacional dirección del viento observada
Estación La Greda

Al comparar ambas gráficas, se tiene que la serie modelada reprodujo la variabilidad de los campos de viento observados
y sus variaciones estacionales. Se apreció que la serie modelada reprodujo vientos de menor intensidad, sin embargo, se
aprecia una subestimación durante los meses invernales.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

**9.3.3 DIRECCIÓN DEL VIENTO ESTACIÓN VENTANAS**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 72 de 252

Figura 41. Ciclo diario dirección del viento modelada
Estación Ventanas

Figura 42. Ciclo diario dirección del viento observada
Estación Ventanas

Al comparar ambas gráficas, resultó ser que el modelo logró reproducir la variabilidad direccional observada, con
diferencias en la frecuencia de los vientos predominantes.
Tanto el modelo como lo observado presentaron una mayor frecuencia para los vientos del rango 220° a 260°, sin
embargo, lo modelado subestima en un 2,26% a lo observado.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 73 de 252

Figura 43. Ciclo estacional dirección del viento modelada
Estación Ventanas

Figura 44. Ciclo estacional dirección del viento
observada Estación Ventanas

De las comparaciones realizadas, se observó que el modelo reprodujo la variabilidad estacional de los campos de vientos
en el sector Ventanas, tanto para el ciclo horario como mensual, sin embargo, presentó una evidente subestimación en la
intensidad del viento, principalmente en horario AM y PM.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**9.3.4 ROSAS DE VIENTO ESTACIÓN PUCHUNCAVÍ**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 74 de 252

Tabla 28. Rosa de viento ciclo anual modelada y observada Estación Puchuncaví

|Col1|Modelado|Col3|Observado|Col5|
|---|---|---|---|---|
|Anual|||||
|Anual|Promedio velocidad|1,43 [m/s]|Promedio velocidad|1,16 [m/s]|
|Anual|Frec. calmas|26,42 %|Frec. calmas|25,37 %|

Del análisis de las rosas de viento se observa que, la serie modelada reprodujo las
variaciones de los campos de viento. Sin embargo, el modelo presentó una sobrestimación
del 11% en la frecuencia de las componentes agrupadas en el 3° cuadrante. Mientras que,
para el 4° cuadrante, la frecuencia se subestimó en un 13% en comparación con lo
observado. En cuanto a la frecuencia de vientos calmos, el modelo logró reproducir en
términos anuales la frecuencia con una leve sobrestimación cercana al 1%.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 75 de 252

**9.3.5 ROSAS DE VIENTO CICLO ANUAL HORARIO ESTACIÓN PUCHUNCAVÍ**

Tabla 29. Rosas de viento anual horario Estación Puchuncaví

|Col1|Modelado|Col3|Col4|Observado|Col6|Col7|Escala|
|---|---|---|---|---|---|---|---|
|||||||||
|Anual Nocturno|Anual Nocturno|Anual Nocturno|Anual Nocturno|Anual Nocturno|Anual Nocturno|Anual Nocturno|Anual Nocturno|
|Anual Nocturno|Promedio|0,58 [m/s]|0,58 [m/s]|Promedio|0,47 [m/s]|0,47 [m/s]||
|Anual Nocturno|Frec. calmas<br>|35,75 %<br>|35,75 %<br>|Frec. calmas<br>|40,50 %<br>|40,50 %<br>|40,50 %<br>|
||~~Modelado~~|~~Modelado~~|~~Modelado~~|~~Observado~~|~~Observado~~|~~Observado~~|~~Escala~~|
|Anual AM||||||||
|Anual AM|Promedio|Promedio|1,72 [m/s]|Promedio|Promedio|1,70 [m/s]||
|Anual AM|Frec. calmas<br>|Frec. calmas<br>|26,61 %<br>|Frec. calmas<br>|Frec. calmas<br>|14,45 %<br>|14,45 %<br>|
||~~Modelado~~|~~Modelado~~|~~Modelado~~|~~Observado~~|~~Observado~~|~~Observado~~|~~Escala~~|
|Anual PM||||||||
|Anual PM|Promedio|1,82 [m/s]|1,82 [m/s]|Promedio|1,14 [m/s]|1,14 [m/s]||
|Anual PM|Frec. calmas|19,45 %|19,45 %|Frec. calmas|25,02 %|25,02 %|25,02 %|

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**9.3.6 ROSAS DE VIENTO ESTACIÓN LA GREDA**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 76 de 252

Tabla 30. Rosa de viento ciclo anual modelada y observada Estación La Greda

|Col1|Modelado|Col3|Observado|Col5|
|---|---|---|---|---|
|Anual|||||
|Anual|Promedio velocidad|1,29 [m/s]|Promedio velocidad|1,47 [m/s]|
|Anual|Frec. calmas|24,58 %|Frec. calmas|19,17 %|

En estación La Greda, el modelo reprodujo las variaciones direccionales de los campos de
viento. No obstante, presentó diferencias en la frecuencia de los vientos predominantes.
Para la componente ONO presentó una subestimación del 13%, mientras que para la
componente SO presentó una sobrestimación del 10% de la frecuencia anual. Por otro
lado, el modelo sobrestimó la frecuencia de vientos calmos en un 5% aproximadamente.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 77 de 252

**9.3.7 ROSAS DE VIENTO CICLO ANUAL HORARIO ESTACIÓN LA GREDA**

Tabla 31. Rosas de viento anual horario - Estación La Greda

|Col1|Modelado|Col3|Observado|Col5|Escala|
|---|---|---|---|---|---|
|Anual Nocturno|||||<br>|
|Anual Nocturno|Promedio|0,60 [m/s]|Promedio|0,52 [m/s]|0,52 [m/s]|
|Anual Nocturno|Frec. calmas<br>|35,80 %<br>|Frec. calmas<br>|34,57 %<br>|34,57 %<br>|
||~~Modelado ~~|~~Modelado ~~|~~Observado ~~|~~Observado ~~|~~Escala ~~|
|Anual AM|||||<br>|
|Anual AM|Promedio|1,54 [m/s]|Promedio|2,15 [m/s]|2,15 [m/s]|
|Anual AM|Frec. calmas<br>|23,80 %<br>|Frec. calmas<br>|6,82 %<br>|6,82 %<br>|
||~~Modelado~~|~~Modelado~~|~~Observado~~|~~Observado~~|~~Escala~~|
|Anual PM||||||
|Anual PM|Promedio|1,59 [m/s]|Promedio|1,54 [m/s]|1,54 [m/s]|
|Anual PM|Frec. calmas|16,89 %|Frec. calmas|17,75 %|17,75 %|

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**9.3.8 ROSAS DE VIENTO ESTACIÓN VENTANAS**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 78 de 252

Tabla 32. Rosa de viento ciclo anual modelada y observada Estación Ventanas

|Col1|Modelado|Col3|Observado|Col5|
|---|---|---|---|---|
|Anual|||||
|Anual|Promedio velocidad|1,53 [m/s]|Promedio velocidad|1,99 [m/s]|
|Anual|Frec. calmas|19,11 %|Frec. calmas|6,83 %|

Al evaluar la estación Ventanas, en general, el modelo tuvo un desempeño positivo en la
reproducción de los cambios de vientos, con diferencias en la frecuencia de los vientos de
mayor predominancia. En el 2° cuadrante el modelo subestimó en 5% la frecuencia
respecto a lo observado, mientras que, en el 3° y 4° cuadrante, el modelo sobrestimó en
un 4% lo observado. En cuanto al análisis de vientos calmos, el modelo sobrestimó en un
12% la frecuencia anual.

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 79 de 252

**9.3.9 ROSAS DE VIENTO CICLO ANUAL HORARIO ESTACIÓN VENTANAS**

Tabla 33. Rosas de viento anual horario - Estación Ventanas

|Col1|Modelado|Col3|Observado|Col5|Escala|
|---|---|---|---|---|---|
|Anual Nocturno|||||<br>|
|Anual Nocturno|Promedio|0,78 [m/s]|Promedio|1,20 [m/s]|1,20 [m/s]|
|Anual Nocturno|% calmas<br>|28,22 %<br>|% calmas<br>|9,63 %<br>|9,63 %<br>|
||~~Modelado~~|~~Modelado~~|~~Observado~~|~~Observado~~|~~Escala~~|
|Anual AM|||||<br>|
|Anual AM|Promedio|1,82 [m/s]|Promedio|2,50 [m/s]|2,50 [m/s]|
|Anual AM|% calmas<br>|17,67 %<br>|% calmas<br>|5,68 %<br>|5,68 %<br>|
||~~Modelado~~|~~Modelado~~|~~Observado~~|~~Observado~~|~~Escala~~|
|Anual PM||||||
|Anual PM|Promedio|1,75 [m/s]|Promedio|2,06 [m/s]|2,06 [m/s]|
|Anual PM|% calmas|14,79 %|% calmas|6,06 %|6,06 %|

ANÁLISIS DE INCERTIDUMBRE **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

**9.4 ANÁLISIS CUANTITATIVO**

Tabla 34 Estadísticos velocidad del viento

|Estadísticos|Puchuncaví|La Greda|Ventanas|
|---|---|---|---|
|RMSE<br>NRMSD<br>NMAE<br>BIAS<br>Coeficiente Correlación<br>IOA|1,07<br>0.15<br>0.10<br>0.32<br>0,73<br>0,81|0,85<br>0,14<br>0,10<br>-0,10<br>0,76<br>0,79|1.02<br>0.12<br>0.09<br>-0,45<br>0.77<br>0.79|

Tabla 35 Estadísticos dirección del viento

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 80 de 252

|Estadísticos|Puchuncaví|La Greda|Ventanas|
|---|---|---|---|
|Error Grueso<br>BIAS|36<br>28|40<br>-15|32<br>5|

Los resultados de los índices estadísticos arrojaron lo siguiente para el modelo pronóstico,
respecto de las observaciones:

 El modelo presentó diferencias cercanas a 1 [m/s], tras evaluar RMSE.

 El sesgo indicó que el modelo subestima bajo 0,5 [m/s] en los sectores de La Greda y
Ventanas. Mientras que, en Puchuncaví, sobrestima la velocidad del viento en 0,32 [m/s].

 La correlación entre lo modelado y observado fue positiva alta.

 El índice de concordancia fue positivo, cercano al acuerdo perfecto (IOA=1).

Del análisis por estación, el modelo se ajusta a las condiciones locales, arrojando índices
dentro de los rangos de aceptabilidad indicados tanto por la Guía para el Uso de Modelos
de Calidad del Aire en el SEIA (SEA, 2023) y Emery, C., Tai, & Yarwood, 2001.

**10 ANÁLISIS DE RESULTADOS INCERTIDUMBRE DEL MODELO**

Del análisis por estación, el modelo presentó un buen desempeño tanto en la precisión y en
la exactitud para cada sector, reproduciendo las condiciones locales de dispersión respecto a
lo observado. Al evaluar los estadísticos, estos resultaron dentro del rango esperado, basado
en Emery, C., Tai, & Yarwood, 2001. Adicional, el modelo representa la frecuencia de
vientos calmos a nivel local, siendo conservador. Por lo anterior, se desestima el aplicar un
factor de corrección al modelo.

ANÁLISIS DE RESULTADOS INCERTIDUMBRE DEL MODELO **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

**11 RESULTADOS DE MODELACIÓN ETAPA DE CONSTRUCCIÓN**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 81 de 252

A continuación, se presentan los resultados obtenidos de la modelación de calidad del aire para las etapas de construcción del
proyecto.
Los resultados muestran las concentraciones en receptores discretos y la comparación con el límite de la normativa de calidad
del aire aplicable para los distintos escenarios de modelación conformados en función del cronograma de Obras Fase
Construcción:

Tabla 36. Escenarios modelación

|Escenarios<br>modelación|Fuentes|
|---|---|
|E1:<br>Escenario 1|Proyecto Maitencillo Etapa 1|
|E1:<br>Escenario 1|-PEAS 1, PEAS 2, PEAS 3 e impulsiones|
|E1:<br>Escenario 1|-PEAS 5.1 e impulsión|
|E1:<br>Escenario 1|-PEAS 5.2 e impulsión|
|E1:<br>Escenario 1|-Red Primaria de A.S.|
|E1:<br>Escenario 1||
|E1:<br>Escenario 1|Sistema Planta de Tratamiento|
|E1:<br>Escenario 1|-Proyecto PTAS Maitencillo Etapa 1|
|E2:<br>Escenario 2|Proyecto Maitencillo Etapa 2|
|E2:<br>Escenario 2|-PEAS 6, PEAS 7, PEAS 8 e impulsiones|
|E2:<br>Escenario 2|-Red Primaria de A.S.|
|E3:<br>Escenario 3|Proyecto Maitencillo Etapa 3|
|E3:<br>Escenario 3|-PEAS 9, PEAS 10 e impulsiones|
|E4:<br>Escenario 4|Proyecto Maitencillo Etapa 4|
|E4:<br>Escenario 4|-Red Primaria de A.S.|
|E4:<br>Escenario 4||
|E4:<br>Escenario 4|Sistema Planta de Tratamiento|
|E4:<br>Escenario 4|-Proyecto PTAS Maitencillo Etapa 2|
|E5:<br>Escenario 5|Sistema Planta de Tratamiento|
|E5:<br>Escenario 5|-Proyecto PTAS Maitencillo Etapa 3|

Las isolíneas de concentración al igual que las concentraciones en receptores son presentadas en ANEXO3 del presente
informe.

RESULTADOS DE MODELACIÓN ETAPA DE CONSTRUCCIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 82 de 252

**11.1 CONCENTRACIONES DE MATERIAL PARTICULADO FINO (MP** **2,5** **) EN RECEPTORES SENSIBLES**

Tabla 37. Norma MP 2,5 [μg/m [3] ] - Promedio 24 horas - Percentil 98

Norma MP 2.5 [μg/m [3] ] - Promedio 24 horas -Percentil 98

|Escenario|Criterio<br>Normativo|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|R13|R14|R15|R16|R17|R18|R19|R20|R21|R22|R23|R24|R25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E1|50<br>[μg/m3]|0,05|0,06|0,71|0,08|0,19|0,18|2,08|0,17|0,65|0,69|4,29|0,83|4,38|0,09|0,05|3,40|0,42|0,56|0,41|0,41|1,39|0,59|0,29|0,14|0,12|
|E2|E2|0,63|0,88|0,13|0,12|0,02|0,04|0,03|0,03|0,03|0,04|0,03|0,04|0,05|1,76|0,33|0,02|0,03|0,02|0,02|0,02|0,01|0,01|0,04|0,05|0,03|
|E3|E3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,03|0,20|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,01|0,01|0,01|
|E4|E4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,02|0,11|0,01|0,00|0,00|0,00|0,00|0,01|0,00|0,00|0,01|0,01|
|E5|E5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,02|0,00|0,00|0,00|0,00|0,01|0,00|0,00|0,00|0,00|

Tabla 38. Norma MP 2,5 [μg/m [3] ] - Promedio Anual

Norma MP 2.5 [μg/m [3] ] - Promedio Anual

|Escenario|Criterio<br>Normativo|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|R13|R14|R15|R16|R17|R18|R19|R20|R21|R22|R23|R24|R25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E1|20<br>[μg/m3]|0,12|0,13|1,44|0,16|0,38|0,37|4,19|0,34|1,31|1,38|8,64|1,68|8,83|0,18|0,10|6,83|0,87|1,14|0,84|0,83|2,79|1,18|0,58|0,28|0,26|
|E2|E2|0,05|0,11|0,01|0,01|0,00|0,01|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,17|0,03|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E3|E3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,02|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E4|E4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,02|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E5|E5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

RESULTADOS DE MODELACIÓN ETAPA DE CONSTRUCCIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 83 de 252

**11.2 CONCENTRACIONES DE MATERIAL PARTICULADO RESPIRABLE (MP** **10** **) EN RECEPTORES SENSIBLES**

Tabla 39. Norma MP 10 [μg/m [3] ] - Promedio 24 horas - Percentil 98

Norma MP 10 [μg/m [3] ] - Promedio 24 horas -Percentil 98

|Escenario|Criterio<br>Normativo|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|R13|R14|R15|R16|R17|R18|R19|R20|R21|R22|R23|R24|R25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E1|130<br>[μg/m3]|0,12|0,13|1,44|0,16|0,38|0,37|4,19|0,34|1,31|1,38|8,64|1,68|8,83|0,18|0,10|6,83|0,87|1,14|0,84|0,83|2,79|1,18|0,58|0,28|0,26|
|E2|E2|1,29|1,78|0,26|0,24|0,04|0,09|0,06|0,06|0,07|0,07|0,07|0,08|0,10|3,55|0,67|0,05|0,05|0,04|0,04|0,03|0,02|0,02|0,08|0,09|0,07|
|E3|E3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,01|0,01|0,00|0,00|0,00|0,06|0,41|0,01|0,01|0,00|0,00|0,00|0,00|0,00|0,01|0,01|0,01|
|E4|E4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,01|0,00|0,00|0,00|0,03|0,23|0,02|0,01|0,01|0,01|0,01|0,01|0,00|0,01|0,01|0,01|
|E5|E5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,02|0,00|0,00|0,00|0,00|0,01|0,00|0,00|0,00|0,00|

Tabla 40. Norma MP 10 [μg/m [3] ] - Promedio Anual

Norma MP 10 [μg/m [3] ] - Promedio Anual

|Escenario|Criterio<br>Normativo|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|R13|R14|R15|R16|R17|R18|R19|R20|R21|R22|R23|R24|R25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E1|50<br>[μg/m3]|0,02|0,03|0,16|0,03|0,03|0,03|0,31|0,08|0,16|0,16|1,00|0,15|0,86|0,03|0,01|0,87|0,13|0,15|0,13|0,11|0,39|0,17|0,11|0,07|0,04|
|E2|E2|0,11|0,23|0,02|0,02|0,00|0,01|0,01|0,01|0,01|0,01|0,01|0,01|0,01|0,35|0,06|0,00|0,01|0,01|0,00|0,00|0,00|0,00|0,01|0,01|0,01|
|E3|E3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,04|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E4|E4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,03|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E5|E5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

RESULTADOS DE MODELACIÓN ETAPA DE CONSTRUCCIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 84 de 252

**11.3 CONCENTRACIONES DE DIÓXIDO DE AZUFRE (SO** **2** **) NORMA PRIMARIA EN RECEPTORES SENSIBLES**

Tabla 41. Norma primaria SO 2 [μg/m [3] ] - Promedio 1 hora - Percentil 98,5

Norma Primaria SO 2 [μg/m [3] ] - Promedio 1 hora -Percentil 98,5

|Escenario|Criterio<br>Normativo|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|R13|R14|R15|R16|R17|R18|R19|R20|R21|R22|R23|R24|R25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E1|350<br>[μg/m3]|0,08|0,10|0,10|0,05|0,01|0,02|0,01|0,01|0,01|0,02|0,01|0,01|0,00|0,00|0,00|0,15|0,02|0,02|0,02|0,05|0,01|0,02|0,01|0,03|0,07|
|E2|E2|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E3|E3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E4|E4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E5|E5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

Tabla 42. Norma primaria SO 2 [μg/m [3] ] - Promedio 24 horas - Percentil 99

Norma Primaria SO 2 [μg/m [3] ] - Promedio 24 horas -Percentil 99

|Escenario|Criterio<br>Normativo|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|R13|R14|R15|R16|R17|R18|R19|R20|R21|R22|R23|R24|R25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E1|150<br>[μg/m3]|0,03|0,03|0,03|0,02|0,00|0,01|0,00|0,00|0,00|0,01|0,00|0,00|0,00|0,00|0,00|0,07|0,01|0,01|0,01|0,02|0,01|0,01|0,01|0,01|0,03|
|E2|E2|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E3|E3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E4|E4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E5|E5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

Tabla 43. Norma primaria SO 2 [μg/m [3] ] - Promedio Anual

Norma Primaria SO 2 [μg/m [3] ] - Promedio Anual

|Escenario|Criterio<br>Normativo|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|R13|R14|R15|R16|R17|R18|R19|R20|R21|R22|R23|R24|R25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E1|60<br>[μg/m3]|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,01|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E2|E2|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E3|E3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E4|E4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E5|E5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

RESULTADOS DE MODELACIÓN ETAPA DE CONSTRUCCIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 85 de 252

**11.4 CONCENTRACIONES DE DIÓXIDO DE AZUFRE (SO** **2** **) NORMA SECUNDARIA EN RECEPTORES SENSIBLES**

Tabla 44. Norma secundaria SO 2 [μg/m [3] ] - Promedio 1 hora - Percentil 99,73

Norma Secundaria SO 2 [μg/m [3] ] - Promedio 1 hora -Percentil 99,73

|Escenario|Criterio<br>Normativo|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|R13|R14|R15|R16|R17|R18|R19|R20|R21|R22|R23|R24|R25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E1|1.000<br>[μg/m3]|0,15|0,14|0,13|0,10|0,02|0,02|0,01|0,01|0,01|0,03|0,02|0,01|0,01|0,00|0,00|0,19|0,03|0,03|0,03|0,07|0,02|0,03|0,02|0,05|0,12|
|E2|E2|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E3|E3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E4|E4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E5|E5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

Tabla 45. Norma secundaria SO 2 [μg/m [3] ] - Promedio 24 horas - Percentil 99,7

Norma Secundaria SO 2 [μg/m [3] ] - Promedio 24 horas -Percentil 99,7

|Escenario|Criterio<br>Normativo|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|R13|R14|R15|R16|R17|R18|R19|R20|R21|R22|R23|R24|R25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E1|365<br>[μg/m3]|0,03|0,05|0,04|0,03|0,01|0,01|0,01|0,00|0,00|0,01|0,01|0,00|0,00|0,00|0,00|0,08|0,01|0,01|0,01|0,02|0,01|0,01|0,01|0,02|0,03|
|E2|E2|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E3|E3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E4|E4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E5|E5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

Tabla 46. Norma secundaria SO 2 [μg/m [3] ] - Promedio Anual

Norma Secundaria SO 2 [μg/m [3] ] - Promedio Anual

|Escenario|Criterio<br>Normativo|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|R13|R14|R15|R16|R17|R18|R19|R20|R21|R22|R23|R24|R25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E1|80<br>[μg/m3]|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,01|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E2|E2|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E3|E3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E4|E4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E5|E5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

RESULTADOS DE MODELACIÓN ETAPA DE CONSTRUCCIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 86 de 252

**11.5 CONCENTRACIONES DE MONÓXIDO DE CARBONO (CO) NORMA PRIMARIA EN RECEPTORES SENSIBLES**

Tabla 47. Norma primaria CO [mg/m [3] ] - Promedio 8 hora - Percentil 99

Norma Primaria CO [mg/m [3] ] - Promedio 8 hora - Percentil 99

|Escenario|Criterio<br>Normativo|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|R13|R14|R15|R16|R17|R18|R19|R20|R21|R22|R23|R24|R25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E1|10<br>[mg/m3]|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E2|E2|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E3|E3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E4|E4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E5|E5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

Tabla 48. Norma primaria CO [mg/m [3] ] - Promedio 1 hora - Percentil 99

Norma Primaria CO [mg/m [3] ] - Promedio 1 hora - Percentil 99

|Escenario|Criterio<br>Normativo|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|R13|R14|R15|R16|R17|R18|R19|R20|R21|R22|R23|R24|R25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E1|30<br>[mg/m3]|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E2|E2|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E3|E3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E4|E4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E5|E5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

RESULTADOS DE MODELACIÓN ETAPA DE CONSTRUCCIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 87 de 252

**11.6 CONCENTRACIONES DE DIÓXIDO DE NITRÓGENO (NO2) NORMA PRIMARIA EN RECEPTORES SENSIBLES**

Tabla 49. Norma primaria NO 2 [ug/m [3] ] - Promedio 1 hora - Percentil 99

Norma Primaria NO 2 [ug/m [3] ] - Promedio 1 hora - Percentil 99

|Escenario|Criterio<br>Normativo|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|R13|R14|R15|R16|R17|R18|R19|R20|R21|R22|R23|R24|R25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E1|10<br>[mg/m3]|0,28|0,30|0,36|0,41|0,33|0,44|0,67|3,24|1,63|0,71|0,27|0,24|0,29|0,33|0,40|0,77|0,77|0,59|0,50|0,68|0,58|0,38|0,51|0,43|0,37|
|E2|E2|0,02|0,03|0,03|0,04|0,02|0,03|0,04|0,52|0,22|0,05|0,02|0,01|0,02|0,03|0,02|0,05|0,06|0,05|0,05|0,06|0,04|0,02|0,03|0,02|0,01|
|E3|E3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,04|0,01|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E4|E4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,01|0,00|0,01|0,01|0,02|0,03|0,01|0,00|0,00|0,00|
|E5|E5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,01|0,00|0,00|0,00|0,00|

Tabla 50. Norma primaria NO 2 [μg/m [3] ] - Promedio Anual

Norma Primaria NO 2 [ug/m [3] ] - Promedio Anual

|Escenario|Criterio<br>Normativo|R1|R2|R3|R4|R5|R6|R7|R8|R9|R10|R11|R12|R13|R14|R15|R16|R17|R18|R19|R20|R21|R22|R23|R24|R25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|E1|30<br>[mg/m3]|0,01|0,01|0,01|0,01|0,00|0,00|0,01|0,11|0,06|0,01|0,00|0,00|0,00|0,00|0,00|0,01|0,01|0,01|0,01|0,01|0,01|0,01|0,01|0,00|0,00|
|E2|E2|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,01|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E3|E3|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E4|E4|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|
|E5|E5|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|0,00|

RESULTADOS DE MODELACIÓN ETAPA DE CONSTRUCCIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

**11.7 APORTE DEL PROYECTO A LAS CONCENTRACIONES BASALES**

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 88 de 252

A continuación, se presentan los resultados de los contaminantes simulados en la Estación Puchuncaví (EMRP) y la
comparación con las concentraciones basales de calidad del aire monitoreadas.

Tabla 51. Aumento de las concentraciones basales en EMRP Puchuncaví

|Contaminante|Tipo|Estadísticos|Medido<br>EMRP<br>Puchuncaví<br>[μg/m3]|Modelado EMRP Puchuncaví [μg/m3]|Col6|Col7|Col8|Col9|Total Aporte proyecto + línea base [μg/m3]|Col11|Col12|Col13|Col14|Límite<br>Norma|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Contaminante|Tipo|Estadísticos|Medido<br>EMRP<br>Puchuncaví<br>[μg/m3]|E1|E2|E3|E4|E5|E1|E2|E3|E4|E5|E5|
|MP2,5|Primaria|Percentil<br>98-24 horas|30.66|0.0396344|0.0046487|0.0007975|0.0005594|0.00030196|30.70|30.66|30.66|30.66|30.66|50|
|MP2,5|Primaria|Promedio<br>Anual|14.85|0.0071685|0.0003239|0.0000732|0.0000898|0.00003930|14.86|14.85|14.85|14.85|14.85|20|
|MP10|Primaria|Percentil<br>98-24 horas|68.38|0.0826615|0.0095187|0.0003556|0.0011344|0.00031078|68.46|68.39|68.38|68.38|68.38|130|
|MP10|Primaria|Promedio<br>Anual|41.05|0.0174626|0.0007197|0.0000308|0.0001836|0.00004252|41.07|41.05|41.05|41.05|41.05|50|
|SO2|Primaria|Percentil<br>98,5-1 hora|57.86|0.0626492|0.0001855|0.0000555|0.0001975|0.00002125|57.92|57.86|57.86|57.86|57.86|350|
|SO2|Primaria|Percentil<br>99-24 horas|28.89|0.0236960|0.0001591|0.0000476|0.0000844|0.00001238|28.91|28.89|28.89|28.89|28.89|150|
|SO2|Primaria|Promedio<br>Anual|14.85|0.0029110|0.0000128|0.0000038|0.0000157|0.00000178|14.85|14.85|14.85|14.85|14.85|60|
|SO2|Secundaria|Percentil<br>99,73-1|81.74|0.1142482|0.0005695|0.0001705|0.0005422|0.00004562|81.85|81.74|81.74|81.74|81.74|1.000|
|SO2|Secundaria|Percentil<br>99,7-24|31.97|0.0322760|0.0002784|0.0000833|0.0001326|0.0000216|32.00|31.97|31.97|31.97|31.97|365|
|SO2|Secundaria|Promedio<br>Anual|14.08|0.0029319|0.0000127|0.0000038|0.0000156|0.00000176|14.08|14.08|14.08|14.08|14.08|80|
|NO2|Primaria|Percentil 99<br>máximos<br>diarios|54.52|0.1291323|0.0087953|0.0019608|0.0028024|0.00073896|54.65|54.53|54.52|54.52|54.52|400|
|NO2|Primaria|Promedio<br>tri anual|14.77|0.0025209|0.0000737|0.0000120|0.0000445|0.00000904|14.77|14.77|14.77|14.77|14.77|100|

De los resultados obtenidos por escenario evaluado, indicaron que los aportes del proyecto a las concentraciones basales
medidas en la estación de Puchuncaví son de baja significancia y no altera la condición basal al momento de la ejecución del
proyecto.

RESULTADOS DE MODELACIÓN ETAPA DE CONSTRUCCIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas

Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 89 de 252

**12CONCLUSIONES**

En base a la información obtenida desde SINCA a partir de los años 2021, 2022 y 2023, e
información otorgada por el solicitante de estudio, se concluye que:

Línea Base Calidad del Aire

MP 2,5 Percentil 98 - 24 horas
Se determinó que para el año 2023, último de año del estudio, el percentil 98 tiene un valor
de 43,67 [ug/m [3] ] que corresponde al 87,33% respecto a la norma, indicando estado de
latencia en la estación Centro Quintero. El resto de las estaciones no presenta condiciones
de saturación ni latencia.

MP 2,5 Anual
En la estación Centro Quintero, para el promedio trianual de las concentraciones de 24 horas
presenta una condición de latencia llegando a un 95% de la norma. El resto de las estaciones
no presenta condiciones de latencia ni de saturación.

MP 10 Percentil 98 - 24 horas
De acuerdo con el análisis efectuado y la determinación del percentil 98 con las
concentraciones de 24 horas para los años 2021, 2022 y 2023, se determinó que el valor de
la norma diaria de MP 10, no presenta condiciones de saturación ni latencia.

MP 10 Anual
Para el promedio trianual muestra que en la estación Puchuncaví presenta condiciones de
latencia al llegar la norma al 82,12% respecto a la norma respectiva.

SO 2
En cuanto a los estadísticos evaluados para SO 2, estos no superaron los límites
establecidos, tanto en su norma horaria, diaria y anual según D.S. No114/2019 y D.S.
N°22/2010.

NO2
En cuanto a los estadísticos evaluados para NO 2, estos no superaron los límites
establecidos, y tampoco existen condiciones de latencia, tanto en su norma horaria y anual
según D.S. No114/2002.

CO
En cuanto a los estadísticos evaluados para CO, estos no superaron los límites establecidos,
y tampoco existen condiciones de latencia, tanto en su norma horaria y de 8 horas según
D.S. No115/2002.

CONCLUSIONES **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 90 de 252

|Contaminante|Tipo|Estadísticos|Medido<br>EMRP<br>Puchuncaví<br>[μg/m3]|Modelado EMRP Puchuncaví [μg/m3]|Col6|Col7|Col8|Col9|Total Aporte proyecto + línea base [μg/m3]|Col11|Col12|Col13|Col14|Límite<br>Norma|Cumple|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Contaminante|Tipo|Estadísticos|Medido<br>EMRP<br>Puchuncaví<br>[μg/m3]|E1|E2|E3|E4|E5|E1|E2|E3|E4|E5|E5|E5|
|MP2,5|Primaria|Percentil<br>98-24 horas|30.66|0.0396344|0.0046487|0.0007975|0.0005594|0.00030196|30.70|30.66|30.66|30.66|30.66|50|SI|
|MP2,5|Primaria|Promedio<br>Anual|14.85|0.0071685|0.0003239|0.0000732|0.0000898|0.00003930|14.86|14.85|14.85|14.85|14.85|20|20|
|MP10|Primaria|Percentil<br>98-24 horas|68.38|0.0826615|0.0095187|0.0003556|0.0011344|0.00031078|68.46|68.39|68.38|68.38|68.38|130|130|
|MP10|Primaria|Promedio<br>Anual|41.05|0.0174626|0.0007197|0.0000308|0.0001836|0.00004252|41.07|41.05|41.05|41.05|41.05|50|50|
|SO2|Primaria|Percentil<br>98,5-1 hora|57.86|0.0626492|0.0001855|0.0000555|0.0001975|0.00002125|57.92|57.86|57.86|57.86|57.86|350|350|
|SO2|Primaria|Percentil<br>99-24 horas|28.89|0.0236960|0.0001591|0.0000476|0.0000844|0.00001238|28.91|28.89|28.89|28.89|28.89|150|150|
|SO2|Primaria|Promedio<br>Anual|14.85|0.0029110|0.0000128|0.0000038|0.0000157|0.00000178|14.85|14.85|14.85|14.85|14.85|60|60|
|SO2|Secundaria|Percentil<br>99,73-1|81.74|0.1142482|0.0005695|0.0001705|0.0005422|0.00004562|81.85|81.74|81.74|81.74|81.74|1.000|1.000|
|SO2|Secundaria|Percentil<br>99,7-24|31.97|0.0322760|0.0002784|0.0000833|0.0001326|0.0000216|32.00|31.97|31.97|31.97|31.97|365|365|
|SO2|Secundaria|Promedio<br>Anual|14.08|0.0029319|0.0000127|0.0000038|0.0000156|0.00000176|14.08|14.08|14.08|14.08|14.08|80|80|
|NO2|Primaria|Percentil 99<br>máximos<br>diarios|54.52|0.1291323|0.0087953|0.0019608|0.0028024|0.00073896|54.65|54.53|54.52|54.52|54.52|400|400|
|NO2|Primaria|Promedio tri<br>anual|14.77|0.0025209|0.0000737|0.0000120|0.0000445|0.00000904|14.77|14.77|14.77|14.77|14.77|100|100|

Por lo tanto, en cuanto a la evaluación del cumplimiento de la normativa aplicable utilizando la estación de monitoreo más
cercana (Estación EMRP Puchuncaví), el proyecto no altera la condición inicial de la línea base. Si bien, se presentan niveles
de latencia por MP 2,5 en su norma anual y diaria, y latencia para el MP10 en su norma anual, la mayor contribución
corresponde a la línea base y no al Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de
Maitencillo.

CONCLUSIONES **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de

Aguas Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 91 de 252

Emisiones:

Las emisiones fueron obtenidas de los consultores GSI, tomando los valores de unidades de

[kg/día] para los contaminantes MP 2,5, MP 10, MPS, SO 2, NO 2, y CO. De estos valores las
mayores emisiones en todas las actividades de construcción del proyecto corresponden a
**excavaciones y movimientos de tierra** .

Modelación de Emisiones Atmosféricas:

Para el contaminante MP 2,5 y en todos los escenarios, tanto en su norma diaria y anual, se
visualiza que las máximas concentraciones se presentan en las obras de construcción del
proyecto, donde la isolínea de valor 0,5 [μg/m3] es la que alcanza mayor alcance respecto a
su fuente de emisión, pero no llegando con aporte significativo a la zona de Ventanas,
Quintero (concentraciones cercanas a cero).

Respecto al aporte máximo en los receptores considerados, estos presentan variabilidad
respecto a la actividad de la fuente emisora y por ende del contaminante, sin embargo todos
corresponden al escenario 1 del proyecto, los cuales se exponen a continuación:

 - MP 10 y MP 2.5 Anual: receptor 11 con 1 y 0,49 [ug/m [3] ] respectivamente.

 - MP 10 y MP 2.5 Diario: receptor 13 con 8,82 y 4,38 [ug/m [3] ] respectivamente.

 SO2 norma primaria y secundaria, anual, diaria y horaria: en receptor 16

`o` Norma primaria anual, diaria y horaria: 0,008 [ug/m [3] ], 0,069 [ug/m [3] ], 0,150

[ug/m [3] ] respectivamente.
`o` Norma secundaria anual, diaria y horaria: 0,008 [ug/m [3] ], 0,076 [ug/m [3] ], 0,188

[ug/m [3] ] respectivamente.

 - NO 2 norma anual y horaria: la condición se visualiza en el receptor 8 con 0,10 y 3,23

[ug/m [3] ] respectivamente.

 CO norma horaria y de 8 horas: se visualiza la condición en el receptor 8 con 0,004 y
0,001 [mg/m [3] ] respectivamente.

Para el SO 2, el aporte del proyecto se aprecia desde el punto de vista de la espacialidad, con
isolíneas más acotadas y más puntuales respecto a los contaminantes MP 10 y MP 2.5 . Esto se
debe a que el SO 2 es generalmente es producido por la combustión de vehículos y grupos
electrógenos. Por lo tanto el aporte del proyecto de este contaminante a la condición basal es
mínimo.

Modelación Meteorológica:

Los resultados del análisis de incertidumbre del modelo indicaron que la meteorología
pronosticada WRF-MMIF año 2023 es representativa de las condiciones locales de
dispersión dado que:

 Reproduce los campos de vientos a nivel local.

 El modelo meteorológico representa las condiciones desfavorables de dispersión,

dado que reproduce los vientos de baja intensidad y calmas.

 Los resultados de los índices estadísticos entre lo modelado y observado se ajustan a

los índices de desempeño de aceptabilidad indicados tanto por la Guía para el Uso de
Modelos de Calidad del Aire en el SEIA (SEA, 2023) y Emery, C., Tai, & Yarwood,
2001.

Proyecto Redes Primarias y Planta de Tratamiento de

Aguas Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 92 de 252

**13BIBLIOGRAFÍA**

Barclay, J. S. (2011). _Generic Guidance and Optimum Model Settings for the CALPUFF_

_Modeling System for Inclusion into the Approved Methods for the Modeling and_
_Assessments of Air Pollutants in NSW, Australia. TRC Environmental Corporation._
BCN. (11 de Junio de 2019). _Biblioteca del Congreso Nacional de Chile_ . Obtenido de

[https://www.bcn.cl/siit/nuestropais/region5/clima.htm](http://www.bcn.cl/siit/nuestropais/region5/clima.htm)
Burlingame, G. A., Suffet, I., & Khiari, D. (2004). _Development of an odor wheel classification_

_scheme for wastewater. Water Science and Technology, Vol. 49._ United Kingdom.
Chen, L. (2009). _Evaluation of Wood Chip-Based Biofilters to Reduce Odor, Hydrogen_

_Sulfide, and Ammonia from Swine Barn Ventilation Air. Journal of the Air & Waste_
_Management Association - Department of Agricultural and Biosystems Engineering,_
_Iowa State University._ USA.
Emery, C., Tai, E., & Yarwood, G. (2001). _Enhanced Meteorological Modeling and_

_Performance Evaluation for Two Texas Ozone Episodes, prepared for the Texas_
_Natural Resource Conservation Commission, prepared by ENVIRON International_
_Corporation, Novato, CA._
EPA. (2005). _Revision to the Guideline on Air Quality Models: Adoption of a Preferred_

_General Purpose (Flat and Complex Terrain) Dispersion Model and Other Revisions;_
_Final Rule._ USA.
ESVAL S.A. (2022). _Declaración de Impacto Ambiental: Proyecto Redes Primarias y Planta_

_de Tratamiento de Aguas Servidas Localidad de Maitencillo. GSI Ingeniería Ltda._
Chile.
Gobierno Regional de Valparaíso. (2005). _Gobierno Regional de Valparaíso. 2005._

_Modificación Plan Intercomunal de Valparaíso. Comunas de Puchuncaví, Zapallar,_
_Papudo, La ligua - Satélite Borde Costero Norte. Secretaría Regional Ministerial de_
_Vivienda y Urbanismo V Región de Valparaíso._ Chile.
Ilustre Municipalidad de Puchuncaví. (2009). _Plan de Desarrollo Comunal. Gobierno Regional_

_de Valparaíso._ Chile.
Instituo Nacional de Estadistíca. (2010). _Síntesis geográfica regional._ Chile.
Karageorgos, P., Latos, M., Kotsifaki, C., Lazaridis, M., & Kalogerakis, N. (2010). _Treatment_

_of Unpleasant Odors in Municipal Wastewater Treatment Plants. Water Science &_
_Technology - WST._ Greece.
Mesoscale Model Interface Program. (s.f.).
Ministerio del Medio Ambiente. (2011). _Ley No 19.300, sobre Bases Generales del Medio_

_Ambiente - Ley Orgánica de la Superintendencia del Medio Ambiente. División_
_Jurídica del Medio Ambiente._ Chile.
Ministerio del Medio Ambiente. (2014). _Decreto No 40: Aprueba Reglamento del Sistema de_

_Evaluación de Impacto Ambiental. Ministerio Secretaría General de la Presidencia._
Chile.
Municipalidad de Puchuncaví. (2011). _Decreto 1576: Aprueba Proyecto “Actualización Plan_

_Regulador, Comuna de Puchuncaví”. Comisión Regional de Medio Ambiente._ Chile.
Pielke, R. (1984). _Mesoscale Metereological Modeling. Academic Pess._ Orlando.

Proyecto Redes Primarias y Planta de Tratamiento de

Aguas Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 93 de 252

Scire, J. S. (2000). _A User's Guide for the Calpuff Dispersion Model. Earth Tech, Inc._
Servicio de Evaluación Ambiental. (2023). _Guía par el Uso de Modelos de Calidad del Aire en_

_el SEIA. Ministerio del Medio Ambiente._ Chile.
Stauffer, D., & Seaman, N. (1990). _Use of Four - Dimensional Data assimilation in a limited -_

_Area Mesoscale Model. Part I: Experiments with Synoptic - scale Data._
Sullivan, E. D. (2018). _MPCA Air Dispersion Modeling Practices Manual. Minnesota Pollution_

_Control Agency._ USA.
UNTEC. (2011). _Uso de modelos de calidad del aire en la evaluación ambiental de proyectos._

Chile.

Proyecto Redes Primarias y Planta de Tratamiento de

Aguas Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 94 de 252

**14ANEXO 1 - MODELACIÓN MATERIAL PARTICULADO SEDIMENTABLE**

De acuerdo con lo solicitado por la autoridad ambiental y según lo establecido en el artículo 6
letra d) del D.S. 40/2012, Reglamento del Sistema de Evaluación de Impacto Ambiental
(SEIA), se complementa el análisis con el límite para la evaluación del impacto de Material
Particulado Sedimentable (MPS) el valor referencial establecido en la Ordenanza para el
Control de la Contaminación del Aire (OAPC) de la Confederación Suiza, que se encuentra
incluida en el listado del artículo 11 correspondiente al D.S. 40/2012.

En el Anexo 7 (Annex 7102 - Ambient limit values for air Pollutants) de la OAPC, se establece
como valor límite de depositación de polvo total en el ambiente, 200 [mg/m [2] día], como
promedio anual de depositación de MPS sobre recursos naturales, valor que es comúnmente
utilizado como referencia para la evaluación de dicho contaminante en los proyectos que se
someten a evaluación ambiental, como por el ejemplo el Proyecto Inmobiliario Trocadero
(RCA 17/2020), el cual se encuentra ubicado en el área de influencia de PTAS Maitencillo.

Es importante destacar que la OAPC tiene como objetivo principal la protección de los seres
humanos, animales, planta, sus comunidades biológicas y hábitats, y al suelo, de los efectos
nocivos o trastornos producidos por la contaminación del aire, en cumplimiento con el
objetivo de las normativas nacionales y específicamente lo mencionado en el artículo 6 del
Reglamento del SEIA. En cuanto a la evaluación de la similitud de la norma de referencia al
área de Maitencillo, se presentan las siguientes consideraciones relevantes:

Enfoque en la Protección Ambiental: La normativa suiza comparte un enfoque común con la
normativa nacional en la protección ambiental. Ambas buscan preservar la calidad del aire y
la salud de los ecosistemas.

Protección de Recursos Naturales: La normativa suiza, según lo expresado por el Dr. Martin
Schiess, Jefe de la División de Gestión de Aire y Control de la Contaminación Química, de la
oficina Federal del Medio Amiente (FOEN), se centra en la protección de la fertilidad del
suelo, vegetación, aguas lo que en última instancia conduce a la protección humada y salud
animal.

En el caso de Maitencillo, un área costera, presenta una atención similar hacia la
preservación de los recursos naturales, especialmente dada la sensibilidad de los
ecosistemas costeros.

Dado lo anterior, se llevó a cabo una simulación utilizando el modelo de dispersión WRFCALPUFF para estimar la concentración de Material Particulado Sedimentable (MPS) en el
peor escenario de emisión, correspondiente al Escenario 1 de la Fase de Construcción del
inventario de emisiones proporcionado por GSI. Los receptores de interés se definieron en el
contexto del Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas en la
localidad de Maitencillo. Para la simulación se siguieron las pautas establecidas en la Guía
de Uso de Modelos para la Calidad del Aire en el SEIA, y se consideró el periodo del 2023.

Proyecto Redes Primarias y Planta de Tratamiento de

Aguas Servidas Localidad de Maitencillo

Tabla 52. Escenarios modelación MPS

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 95 de 252

|Escenario<br>modelación|Fuentes|
|---|---|
|E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción)|Proyecto Maitencillo Etapa 1|
|E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción)|-PEAS 1, PEAS 2, PEAS 3 e impulsiones|
|E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción)|-PEAS 5.1 e impulsión|
|E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción)|-PEAS 5.2 e impulsión|
|E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción)|-Red Primaria de A.S.|
|E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción)||
|E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción)|Sistema Planta de Tratamiento|
|E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción)|-Proyecto PTAS Maitencillo Etapa 1|

Cabe destacar que para la evaluación de la línea base, no se dispone de una estación
cercana al proyecto y con datos disponibles en el Sistema de Información Nacional de
Calidad del Aire para la evaluación, no obstante, se realiza la modelación de dispersión de
MPS sobre los receptores caracterizados.

A continuación se presentan los resultados de la modelación de dispersión de MPS.

Tabla 53 MPS como concentración media aritmética anual.

|ID Receptor|Concentración<br>media aritmética<br>anual.<br>[mg/m2 día]|Límite<br>OAPC Suiza|
|---|---|---|
|Receptor 1<br>|~~0,0096~~<br>|200 [mg/m2 día]<br>Media Aritmética<br>Anual|
|~~Receptor 2~~|~~0,0106~~<br>|~~0,0106~~<br>|
|Receptor 3<br>|~~0,1056~~<br>|~~0,1056~~<br>|
|~~Receptor 4~~|~~0,0146~~<br>|~~0,0146~~<br>|
|Receptor 5|~~0,0148~~<br>|~~0,0148~~<br>|
|Receptor 6|~~0,0165~~<br>|~~0,0165~~<br>|
|Receptor 7|~~0,3365~~<br>|~~0,3365~~<br>|
|Receptor 8<br>|~~0,0422~~<br>|~~0,0422~~<br>|
|~~Receptor 9~~|~~0,1273~~<br>|~~0,1273~~<br>|
|Receptor 10|~~0,2440~~<br>|~~0,2440~~<br>|
|Receptor 11<br>|~~0,8176~~<br>|~~0,8176~~<br>|
|~~Receptor 12~~|~~0,2595~~<br>|~~0,2595~~<br>|
|Receptor 13<br>|~~0,7156~~<br>|~~0,7156~~<br>|
|~~Receptor 14~~|~~0,0118~~<br>|~~0,0118~~<br>|
|Receptor 15<br>|~~0,0057~~<br>|~~0,0057~~<br>|
|~~Receptor 16~~|~~0,4373~~<br>|~~0,4373~~<br>|
|Receptor 17|~~0,0876~~<br>|~~0,0876~~<br>|
|Receptor 18<br>|~~0,1306~~<br>|~~0,1306~~<br>|
|~~Receptor 19~~|~~0,1138~~<br>|~~0,1138~~<br>|
|Receptor 20<br>|~~0,0571~~<br>|~~0,0571~~<br>|
|~~Receptor 21~~|~~0,4261~~<br>|~~0,4261~~<br>|
|Receptor 22|~~0,0828~~<br>|~~0,0828~~<br>|
|Receptor 23<br>|~~0,1111~~<br>|~~0,1111~~<br>|
|~~Receptor 24~~|~~0,0363~~<br>|~~0,0363~~<br>|
|Receptor 25<br>|~~0,0165~~<br>|~~0,0165~~<br>|
|~~Receptor 26~~|~~0,0122~~|~~0,0122~~|

Proyecto Redes Primarias y Planta de Tratamiento de

Aguas Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 96 de 252

Figura 45 E1 Isolíneas MPS como concentración media aritmética anual en receptores.

Resultados

Para la justificación de la inexistencia de los efectos en el área de influencia a raíz de las
emisiones de MPS, se evaluaron las concentraciones modeladas en receptores discretos con
los límites establecidos en la Ordenanza para el Control de la Contaminación del Aire
(OAPC) de la Confederación Suiza, que se encuentra incluida en el listado del artículo 11
correspondiente al D.S. 40/2012, específicamente el Anexo 7 (Annex 7102 - Ambient limit
values for air Pollutants) de la OAPC, se establece como valor límite de depositación de
polvo total en el ambiente, 200 [mg/m [2] día], como promedio anual de depositación de MPS
sobre recursos naturales. Los resultados obtenidos muestran que las concentraciones de
MPS se sitúan por debajo de los límites normativos establecidos, por lo que se descartan
tanto los impactos como los riesgos para los receptores evaluados.

Proyecto Redes Primarias y Planta de Tratamiento de

Aguas Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 97 de 252

**15ANEXO 2 - ANÁLISIS GUÍA: CRITERIO DE EVALUACIÓN EN EL SEIA - IMPACTO DE**

**EMISIONES EN ZONAS SATURADAS POR MATERIAL PARTICULADO RESPIRABLE**

**MP** **10** **Y MATERIAL PARTICULADO FINO RESPIRABLE MP** **2.5**

El presente análisis se fundamenta en la guía " Criterio de Evaluación en el SEIA: Impacto de
Emisiones en Zonas Saturadas por Material Particulado Respirable MP 10 y Material
Particulado Fino Respirable MP 2.5 ".

El objetivo es proporcionar directrices para determinar aumentos o disminuciones
significativas de la concentración de material particulado respirable por encima de los límites
establecidos en las normativas ambientales. Para ello, se establecen criterios que abordan
tanto las zonas oficialmente declaradas saturadas como aquellas que exceden los umbrales
sin una designación oficial, con un enfoque en la evaluación del riesgo preexistente para la
salud pública.

**15.1 EVALUACIÓN DEL IMPACTO DE LAS EMISIONES ATMOSFÉRICAS DE MATERIAL**

**PARTICULADO RESPIRABLE SOBRE EL RIESGO PARA LA SALUD DE LA**
**POBLACIÓN EN EL MARCO DEL SEIA.**

Según lo establecido en el artículo 18, literal f), del Reglamento del SEIA, los Estudios de
Impacto Ambiental (EIA) deben incluir una evaluación que determine si los impactos
previstos constituyen impactos significativos según los criterios establecidos en la Ley. Este
párrafo destaca dos conceptos clave: la predicción de impactos y la significancia de los
mismos, los cuales serán abordados y diferenciados a continuación:

a) Predicción La predicción de impactos consiste “[...] en la identificación y estimación
o cuantificación de las alteraciones directas o indirectas a los elementos del medio
ambiente [...]”5 (énfasis agregado). Predicción cuantitativa del impacto ambiental
utilizando modelos matemáticos, conocidos como "modelos de calidad del aire",
que simulan la dispersión y transformación de contaminantes en la atmósfera. Los
criterios a utilizar corresponden a los mencionados en Guía para el uso de modelos
de calidad del aire en el SEIA (SEA, 2023a).

b) Significancia: La determinación de la significancia de los impactos ambientales,
según lo establecido en el Reglamento del SEIA, se basa en los efectos,
características y circunstancias detalladas en la Ley N°19.300. Específicamente,
para evaluar el impacto en la salud de la población, se considera significativo si hay
superación de los valores establecidos en las normas primarias de calidad
ambiental vigentes o un aumento/diminución significativos de la concentración por
encima de estos límites.

El Reglamento del SEIA reconoce situaciones donde los receptores humanos pueden estar
expuestos a concentraciones de contaminantes que superen los límites establecidos en las
normativas. En estos casos, se evalúa el aumento significativo de la concentración sobre
estos límites, lo que implica un riesgo preexistente para la salud pública. Es esencial realizar
una adecuada identificación de la condición existente del contaminante en el área de
influencia mediante la caracterización del componente ambiental o línea de base. Esto aplica
incluso en ausencia de un decreto que declare la saturación de la zona.

Proyecto Redes Primarias y Planta de Tratamiento de

Aguas Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 98 de 252

En presencia de una declaratoria oficial de saturación, se considerarán los valores
establecidos en ella, atendiendo al principio precautorio. Sin embargo, el titular del proyecto
aún debe elaborar una caracterización de la calidad del aire. Es fundamental comprender
que el riesgo preexistente viene determinado por la existencia de un decreto de saturación, el
cual no puede ser cuestionado durante la evaluación ambiental.

**15.2 CARACTERIZACIÓN DE LOS NIVELES DE MP** **10** **Y MP** **2,5** **EN LOS RECEPTORES**

**HUMANOS DEL ÁREA DE INFLUENCIA**

Para ellos, se requiere identificar si existe un riesgo preexistente en el área. Esto se
establece de dos maneras:

a) Si la zona está declarada como saturada según la normativa de MP 10 y MP 2,5, los

receptores humanos en esa área se consideran bajo un escenario de riesgo
preexistente.

b) En zonas no declaradas como saturadas, pero donde las estaciones de monitoreo

indiquen valores superiores a las normativas de calidad del aire para MP 10 y MP 2,5, la
evaluación del impacto se realiza bajo un escenario de riesgo preexistente.

De acuerdo con lo declarado en D.S. No10 de 2015, del Ministerio del Medio Ambiente, se
declaró zona saturada por Material Particulado Fino Respirable MP 2,5, como concentración
anual, zona latente por el mismo contaminante como concentración de 24 horas, y zona
latente por Material Particulado Respirable MP 10, como concentración anual, la zona
geográfica que comprende las comunas de Concón, Quintero y Puchuncaví de la Región de
Valparaíso. Por lo tanto, se realiza el análisis respectivo dada la condición de riesgo
preexistente.

Proyecto Redes Primarias y Planta de Tratamiento de

Aguas Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 99 de 252

**15.3 CRITERIOS PARA EVALUAR LA SIGNIFICANCIA DEL APORTE DE EMISIONES DE**

**MATERIAL PARTICULADO RESPIRABLE, MP** **10** **y MP** **2,5**

A continuación se presenta la siguiente tabla con los valores que se deben considerar como
significativos para la evaluación de impacto en un escenario de riesgo preexistente, en
cuanto al aporte o incremento de concentraciones de MP 10 y MP 2,5 en el o los receptores
humanos de interés emplazados en el área de influencia para un período de duración menor
a 3 años, esto en función de temporalidad del proyecto en estudio.

Dada la declaración D.S. No10 de 2015, que establece zona saturada por Material
Particulado Fino Respirable MP 2,5, como concentración anual, zona latente por el mismo
contaminante como concentración de 24 horas, y zona latente por Material Particulado
Respirable MP 10, como concentración anual, la zona geográfica que comprende las comunas
de Concón, Quintero y Puchuncaví, se realiza el presente análisis:

De acuerdo con la modelación de calidad del aire realizada para el Escenario 1, que
representa el escenario de mayor emisión y cuya temporalidad se proyectó para 12 meses
como la peor condición, los valores significativos a utilizar para la evaluación del impacto en
un escenario de riesgo preexistente serán los valores indicados para el mes 12, según la
siguiente tabla:

Tabla 54 Valores de significancia para el aumento de concentraciones de MP 10 y MP 2,5 sobre
receptores humanos corregidos para impactos con una duración menor a 3 años en zonas
que sobrepasen el valor de la norma

|DURACIÓN IMPACTO|Col2|Col3|MP [μg/m3]<br>10|Col5|MP [μg/m3]<br>2,5|Col7|
|---|---|---|---|---|---|---|
|Año|Mes|Proporcional (años)|24 horas|Anual|24 horas|Anual|
|**1 **|1|0,1|10,00|10,00|10,00|10,00|
|**1 **|2|0,2|10,00|10,00|10,00|5,94|
|**1 **|3|0,3|10,00|10,00|10,00|3,96|
|**1 **|4|0,3|10,00|9,00|10,00|2,97|
|**1 **|5|0,4|10,00|7,20|10,00|2,38|
|**1 **|6|0,5|10,00|6,00|10,00|1,98|
|**1 **|7|0,6|10,00|5,14|8,79|1,70|
|**1 **|8|0,7|10,00|4,50|7,70|1,49|
|**1 **|9|0,8|10,00|4,00|6,84|1,32|
|**1 **|10|0,8|10,00|3,60|6,16|1,19|
|**1 **|11|0,9|10,00|3,27|5,60|1,08|
|**1 **|**12**|**1,0**|**10,00**|**3,00**|**5,13**|**0,99**|

Proyecto Redes Primarias y Planta de Tratamiento de

Aguas Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 100 de 252

Los resultados del modelo para los receptores con el máximo impacto para MP 10 y MP 2,5 para
24 horas y anual, evaluados dentro del área de influencia, indicaron que no se ha excedido
los valores de significancia para el aumento de concentraciones de MP 10 y MP 2,5 sobre los
receptores humanos corregidos para impactos con una duración menor a 3 años en zonas
que superen el valor de la norma.

Tabla 55 Valores de significancia para el aumento de concentraciones de MP 10

|Contaminante|Duración<br>Impacto|Unidad|Tipo|Límite|R13|R11|
|---|---|---|---|---|---|---|
|MP10|1 año|[μg/m3]|24 horas|10|8.83|8.64|
|MP10|1 año|[μg/m3]|Anual|3|0.86|1.00|

Tabla 56 Valores de significancia para el aumento de concentraciones de MP 2.5

|Contaminante|Duración<br>Impacto|Unidad|Tipo|Límite|R13|R11|
|---|---|---|---|---|---|---|
|MP2.5|1 año|[μg/m3]|24 horas|5.13|4.38|4.29|
|MP2.5|1 año|[μg/m3]|Anual|0.99|0.43|0.50|

Cabe destacar que las actividades de mayor emisión corresponden a aquellas asociadas a
Excavaciones y Movimientos de Tierra, cuya duración temporal de impacto es de 1 mes. Por
lo tanto, incluso considerando lo anterior, los valores arrojados por el modelo de calidad del
aire estarían dentro de los valores de significancia mencionados anteriormente.

Proyecto Redes Primarias y Planta de Tratamiento de

Aguas Servidas Localidad de Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 101 de 252

**16 ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP** **2,5** **, MP** **10** **, SO** **2** **, CO Y NO** **2**

Para la visualización de las isolíneas de concentración de los contaminantes evaluados
excluyendo las normas horarias, se utilizó como referencia el criterio umbral de 0,5 [μg/m [3] ],
criterio utilizado en proyectos sometidos al SEIA tales como “Concesión Américo Vespucio
Oriente. Tramo Avenida El Salto - Príncipe de Gales (Resolución Exenta No471/2017),
donde se hace referencia a que las concentraciones medidas por estaciones bajo este
umbral son consideradas como 0 [μg/m [3] ], debido a que rangos de incertidumbre tienden a
superar los valores absolutos medidos en concentraciones de magnitudes tan bajas.

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 102 de 252

**16.1 ESCENARIO 1 - ISOLÍNEAS DE CONCENTRACIÓN MP** **2,5** **, MP** **10** **, SO** **2** **, CO Y NO** **2**

Figura 46. E1 Isolíneas MP 2,5 Percentil 98-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 103 de 252

Figura 47. E1 Isolíneas MP 2,5 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 104 de 252

Figura 48. E1 Isolíneas MP 10 Percentil 98-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 105 de 252

Figura 49. E1 Isolíneas MP 10 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 106 de 252

Figura 50. E1 Isolíneas SO 2 Percentil 98,5-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 107 de 252

Figura 51. E1 Isolíneas SO 2 Percentil 99-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 108 de 252

Figura 52. E1 Isolíneas SO 2 Percentil 99,73-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 109 de 252

Figura 53. E1 Isolíneas SO 2 Percentil 99,7-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 110 de 252

Figura 54. E1 Isolíneas SO 2 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 111 de 252

Figura 55. E1 Isolíneas CO Percentil 99-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 112 de 252

Figura 56. E1 Isolíneas CO Percentil 99-8 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 113 de 252

Figura 57. E1 Isolíneas NO 2 Percentil 99-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 114 de 252

Figura 58. E1 Isolíneas NO 2 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 115 de 252

**16.2 ESCENARIO 2 - ISOLÍNEAS DE CONCENTRACIÓN MP** **2,5** **, MP** **10** **SO** **2** **CO Y NO** **2**

Figura 59. E2 Isolíneas MP 2,5 Percentil 98-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 116 de 252

Figura 60. E2 Isolíneas MP 2,5 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 117 de 252

Figura 61. E2 Isolíneas MP 10 Percentil 98-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 118 de 252

Figura 62. E2 Isolíneas MP 10 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 119 de 252

Figura 63. E2 Isolíneas SO 2 Percentil 98,5-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 120 de 252

Figura 64. E2 Isolíneas SO 2 Percentil 99-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 121 de 252

Figura 65. E2 Isolíneas SO 2 Percentil 99,73-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 122 de 252

Figura 66. E2 Isolíneas SO 2 Percentil 99,7-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 123 de 252

Figura 67. E2 Isolíneas SO 2 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 124 de 252

Figura 68. E2 Isolíneas CO Percentil 99-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 125 de 252

Figura 69. E2 Isolíneas CO Percentil 99-8 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 126 de 252

Figura 70. E2 Isolíneas NO 2 Percentil 99-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 127 de 252

Figura 71. E2 Isolíneas NO 2 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 128 de 252

**16.3 ESCENARIO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP** **2,5** **, MP** **10** **SO** **2** **CO Y NO** **2**

Figura 72. E3 Isolíneas MP 2,5 Percentil 98-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 129 de 252

Figura 73. E3 Isolíneas MP 2,5 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 130 de 252

Figura 74. E3 Isolíneas MP 10 Percentil 98-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 131 de 252

Figura 75. E3 Isolíneas MP 10 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 132 de 252

Figura 76. E3 Isolíneas SO 2 Percentil 98,5-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 133 de 252

Figura 77. E3 Isolíneas SO 2 Percentil 99-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 134 de 252

Figura 78. E3 Isolíneas SO 2 Percentil 99,73-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 135 de 252

Figura 79. E3 Isolíneas SO 2 Percentil 99,7-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 136 de 252

Figura 80. E3 Isolíneas SO 2 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 137 de 252

Figura 81. E3 Isolíneas CO Percentil 99-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 138 de 252

Figura 82. E3 Isolíneas CO Percentil 99-8 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 139 de 252

Figura 83. E3 Isolíneas NO 2 Percentil 99-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 140 de 252

Figura 84. E3 Isolíneas NO 2 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 141 de 252

**16.4 ESCENARIO 4 - ISOLÍNEAS DE CONCENTRACIÓN MP** **2,5** **, MP** **10** **SO** **2** **CO Y NO** **2**

Figura 85. E4 Isolíneas MP 2,5 Percentil 98-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 142 de 252

Figura 86. E4 Isolíneas MP 2,5 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 143 de 252

Figura 87. E4 Isolíneas MP 10 Percentil 98-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 144 de 252

Figura 88. E4 Isolíneas MP 10 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 145 de 252

Figura 89. E4 Isolíneas SO 2 Percentil 98,5-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 146 de 252

Figura 90. E4 Isolíneas SO 2 Percentil 99-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 147 de 252

Figura 91. E4 Isolíneas SO 2 Percentil 99,73-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 148 de 252

Figura 92. E4 Isolíneas SO 2 Percentil 99,7-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 149 de 252

Figura 93. E4 Isolíneas SO 2 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 150 de 252

Figura 94. E4 Isolíneas CO Percentil 99-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 151 de 252

Figura 95. E4 Isolíneas CO Percentil 99-8 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 152 de 252

Figura 96. E4 Isolíneas NO 2 Percentil 99-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 153 de 252

Figura 97. E4 Isolíneas NO 2 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 154 de 252

**16.5 ESCENARIO 5 - ISOLÍNEAS DE CONCENTRACIÓN MP** **2,5** **, MP** **10** **SO** **2** **CO Y NO** **2**

Figura 98. E5 Isolíneas MP 2,5 Percentil 98-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 155 de 252

Figura 99. E5 Isolíneas MP 2,5 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 156 de 252

Figura 100. E5 Isolíneas MP 10 Percentil 98-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 157 de 252

Figura 101. E5 Isolíneas MP 10 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 158 de 252

Figura 102. E5 Isolíneas SO 2 Percentil 98,5-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 159 de 252

Figura 103. E5 Isolíneas SO 2 Percentil 99-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 160 de 252

Figura 104. E5 Isolíneas SO 2 Percentil 99,73-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 161 de 252

Figura 105. E5 Isolíneas SO 2 Percentil 99,7-24 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 162 de 252

Figura 106. E5 Isolíneas SO 2 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 163 de 252

Figura 107. E5 Isolíneas CO Percentil 99-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 164 de 252

Figura 108. E5 Isolíneas CO Percentil 99-8 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 165 de 252

Figura 109. E5 Isolíneas NO 2 Percentil 99-1 [h]

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto: 0126 - V.01
Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de Maitencillo Fecha Abril de 2024
Página 166 de 252

Figura 110. E5 Isolíneas NO 2 Anual

ANEXO 3 - ISOLÍNEAS DE CONCENTRACIÓN MP2,5, MP10, SO2, CO y NO2 **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

**17ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN**

**17.1 FUENTES DE EMISIÓN - ESCENARIO 1**

Tabla 57. Fuentes de Emisión - Escenario 1 parte 1

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 167 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_1|Peas_1|270862|6384348|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_2|Peas_2|271312|6385052|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_3|Peas_3|272644|6386732|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_4|Peas_5.1|271757|6385539|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_5|Peas_5.2|272602|6384124|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_6|Colec_1.1|270894|6383950|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_7|Colec_1.2|270876|6384052|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_8|Colec_1.3|270873|6384151|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_9|Colec_1.4|270873|6384253|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_10|Col_1_2.1|270931|6384850|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_11|Col_1_2.2|271016|6384942|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_12|Col_1_2.3|271106|6384990|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_13|Col_1_2.4|271203|6385001|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_14|Colec_2.1|271534|6385454|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_15|Colec_2.2|271640|6385468|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_16|Colec_2.3|271734|6385512|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_17|Colec_5.1.1|271798|6385551|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_18|Colec_5.1.2|271860|6385633|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_19|Colec_5.1.3|271915|6385715|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_20|Colec_5.1.4|271973|6385798|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_21|Colec_5.1.5|272032|6385882|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_22|Colec_5.1.6|272063|6385983|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_23|Colec_5.1.7|272071|6386082|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_24|Colec_5.1.8|272080|6386180|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_25|Colec_5.1.9|272092|6386283|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_26|Colec_5.1.10|272101|6386381|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_27|Colec_5.1.11|272112|6386484|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 58. Fuentes de Emisión - Escenario 1 parte 2

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 168 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_28|Colec_5.1.12|272122|6386584|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_29|Colec_5.1.13|272132|6386683|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_30|Colec_5.1.14|272171|6386767|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_31|Colec_5.1.15|272225|6386788|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_32|Imp_1.1|270869|6384373|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_33|Imp_1.2|270883|6384472|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_34|Imp_1.3|270915|6384567|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_35|Imp_1.4|270907|6384662|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_36|Imp_1.5|270863|6384741|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_37|Imp_2.1|271310|6385050|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_38|Imp_2.2|271349|6385137|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_39|Imp_2.3|271379|6385235|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_40|Imp_2.4|271425|6385313|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_41|Imp_2.5|271473|6385362|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_42|Imp_3.1|272362|6386742|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_43|Imp_3.2|272478|6386683|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_44|Imp_3.3|272646|6386701|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_45|Imp_5.1.1|271781|6385537|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_46|Imp_5.1.2|271876|6385511|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_47|Imp_5.1.3|271846|6385422|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_48|Imp_5.1.4|271858|6385339|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_49|Imp_5.1.5|271954|6385328|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_50|Imp_5.1.6|272056|6385329|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_51|Imp_5.1.7|272156|6385329|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_52|Imp_5.1.8|272220|6385336|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_53|Imp_5.1.9|272311|6385344|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_54|Imp_5.1.10|272285|6385236|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_55|Imp_5.1.11|272304|6385134|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_56|Imp_5.1.12|272336|6385038|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_57|Imp_5.1.13|272407|6384841|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_58|Imp_5.1.14|272372|6384937|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_59|Imp_5.1.15|272450|6384738|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 59. Fuentes de Emisión - Escenario 1 parte 3

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 169 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_60|Imp_5.1.16|272488|6384641|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_61|Imp_5.1.17|272524|6384542|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_62|Imp_5.1.18|272555|6384455|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_63|Imp_5.1.19|272599|6384360|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_64|Imp_5.1.20|272630|6384265|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_65|Imp_5.2.1|272632|6384030|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_66|Imp_5.2.2|272629|6383932|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_67|Imp_5.2.3|272630|6383829|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_68|Imp_5.2.4|272630|6383727|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_69|Imp_5.2.5|272640|6383641|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_70|Imp_5.2.6|272746|6383639|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_71|Imp_5.2.7|272851|6383632|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_72|Imp_5.2.8|272942|6383633|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_73|Imp_5.2.9|273063|6383633|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_74|Imp_5.2.10|273174|6383643|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_75|Imp_5.2.11|273241|6383541|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_76|Imp_5.2.12|273289|6383443|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_77|Imp_5.2.13|273365|6383370|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_78|Imp_5.2.14|273435|6383287|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_79|Imp_5.2.15|273517|6383233|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_80|Imp_5.2.16|273550|6383131|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_81|IF_1_Redes|272317|6384978|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_82|IF_2_PTAS|273520|6383274|10 meses|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_83|Tub_1.1|272633|6383633|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_84|Tub_1.2|272635|6383539|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_85|Tub_1.3|272525|6383555|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_86|Tub_1.4|272458|6383630|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_87|Tub_1.5|272378|6383683|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_88|Tub_1.6|272300|6383735|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_89|Tub_1.7|272197|6383722|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_90|Tub_1.8|272122|6383755|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_91|Tub_1.9|272060|6383844|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 60. Fuentes de Emisión - Escenario 1 parte 4

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 170 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_92|Tub_1.10|271961|6383846|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_93|Tub_1.11|271862|6383794|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_94|Tub_1.12|271766|6383745|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_95|Tub_1.13|271669|6383720|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_96|Tub_1.14|271564|6383688|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_97|Tub_1.15|271501|6383601|1 mes|4,00|2,33,E-03|1,16,E-03|0,01103|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_98|Tub_1.16|271424|6383524|1 mes|4,00|2,3,E-03|1,2,E-03|1,1,E-02|0,0,E+00|0,0,E+00|0,0,E+00|
|AREA|SRC_99|Tub_1.17|271369|6383436|1 mes|4,00|2,3,E-03|1,2,E-03|1,1,E-02|0,0,E+00|0,0,E+00|0,0,E+00|
|AREA|SRC_100|Tub_1.18|271340|6383353|1 mes|4,00|2,3,E-03|1,2,E-03|1,1,E-02|0,0,E+00|0,0,E+00|0,0,E+00|
|AREA|SRC_101|Tub_1.19|271274|6383286|1 mes|4,00|2,3,E-03|1,2,E-03|1,1,E-02|0,0,E+00|0,0,E+00|0,0,E+00|
|AREA|SRC_102|Tub_1.20|271248|6383193|1 mes|4,00|2,3,E-03|1,2,E-03|1,1,E-02|0,0,E+00|0,0,E+00|0,0,E+00|
|AREA|SRC_103|Tub_1.21|271205|6383096|1 mes|4,00|2,3,E-03|1,2,E-03|1,1,E-02|0,0,E+00|0,0,E+00|0,0,E+00|
|AREA|SRC_209|Cam_Cat_1-PEAS e Imp|273043|6387323|3 mes|383,32|8,7,E-08|2,1,E-08|2,6,E-08|4,6,E-08|4,6,E-08|1,1,E-08|
|AREA|SRC_210|Cam_Cat_2-PEAS e Imp|273206|6387558|3 mes|1145,03|2,9,E-08|7,0,E-09|8,6,E-09|1,5,E-08|1,5,E-08|3,6,E-09|
|AREA|SRC_211|Cam_Cat_3-PEAS e Imp|273308|6387612|3 mes|456,00|7,3,E-08|1,8,E-08|2,2,E-08|3,8,E-08|3,8,E-08|9,1,E-09|
|AREA|SRC_212|Cam_Cat_4-PEAS e Imp|273511|6387668|3 mes|843,57|3,9,E-08|9,5,E-09|1,2,E-08|2,1,E-08|2,1,E-08|4,9,E-09|
|AREA|SRC_213|Cam_Cat_5-PEAS e Imp|273721|6387707|3 mes|853,32|3,9,E-08|9,4,E-09|1,2,E-08|2,0,E-08|2,0,E-08|4,9,E-09|
|AREA|SRC_214|Cam_Cat_6-PEAS e Imp|273880|6387880|3 mes|945,26|3,5,E-08|8,5,E-09|1,0,E-08|1,8,E-08|1,8,E-08|4,4,E-09|
|AREA|SRC_215|Cam_Cat_7-PEAS e Imp|273982|6387934|3 mes|457,52|7,3,E-08|1,8,E-08|2,2,E-08|3,8,E-08|3,8,E-08|9,1,E-09|
|AREA|SRC_216|Cam_Cat_8-PEAS e Imp|274178|6387916|3 mes|782,20|4,2,E-08|1,0,E-08|1,3,E-08|2,2,E-08|2,2,E-08|5,3,E-09|
|AREA|SRC_217|Cam_Cat_9-PEAS e Imp|274216|6387945|3 mes|195,48|1,7,E-07|4,1,E-08|5,0,E-08|8,9,E-08|8,9,E-08|2,1,E-08|
|AREA|SRC_218|Cam_Cat_10-PEAS e Imp|274213|6388017|3 mes|295,61|1,1,E-07|2,7,E-08|3,3,E-08|5,9,E-08|5,9,E-08|1,4,E-08|
|AREA|SRC_219|Cam_Cat_11-PEAS e Imp|274177|6388250|3 mes|941,53|3,5,E-08|8,5,E-09|1,0,E-08|1,9,E-08|1,9,E-08|4,4,E-09|
|AREA|SRC_220|Cam_Cat_12-PEAS e Imp|274185|6388365|3 mes|458,34|7,2,E-08|1,8,E-08|2,1,E-08|3,8,E-08|3,8,E-08|9,1,E-09|
|AREA|SRC_221|Cam_Cat_13-PEAS e Imp|274352|6388558|3 mes|1016,92|3,3,E-08|7,9,E-09|9,7,E-09|1,7,E-08|1,7,E-08|4,1,E-09|
|AREA|SRC_222|Cam_Cat_14-PEAS e Imp|274654|6388846|3 mes|1667,00|2,0,E-08|4,8,E-09|5,9,E-09|1,0,E-08|1,0,E-08|2,5,E-09|
|AREA|SRC_223|Cam_Cat_15-PEAS e Imp|274745|6388895|3 mes|409,81|8,1,E-08|2,0,E-08|2,4,E-08|4,3,E-08|4,3,E-08|1,0,E-08|
|AREA|SRC_224|Cam_Cat_16-PEAS e Imp|274834|6388862|3 mes|371,12|9,0,E-08|2,2,E-08|2,7,E-08|4,7,E-08|4,7,E-08|1,1,E-08|
|AREA|SRC_225|Cam_Cat_17-PEAS e Imp|274882|6388794|3 mes|331,29|1,0,E-07|2,4,E-08|3,0,E-08|5,3,E-08|5,3,E-08|1,3,E-08|
|AREA|SRC_226|Cam_Cat_18-PEAS e Imp|274979|6388768|3 mes|406,63|8,2,E-08|2,0,E-08|2,4,E-08|4,3,E-08|4,3,E-08|1,0,E-08|
|AREA|SRC_227|Cam_Cat_19-PEAS e Imp|275069|6388799|3 mes|384,16|8,6,E-08|2,1,E-08|2,6,E-08|4,5,E-08|4,5,E-08|1,1,E-08|
|AREA|SRC_228|Cam_Cat_20-PEAS e Imp|275059|6388911|3 mes|459,52|7,2,E-08|1,7,E-08|2,1,E-08|3,8,E-08|3,8,E-08|9,0,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 61. Fuentes de Emisión - Escenario 1 parte 5

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 171 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_229|Cam_Cat_21-PEAS e Imp|275040|6389003|3 mes|374,05|8,9,E-08|2,1,E-08|2,6,E-08|4,7,E-08|4,7,E-08|1,1,E-08|
|AREA|SRC_230|Cam_Cat_22-PEAS e Imp|274958|6389092|3 mes|489,11|6,8,E-08|1,6,E-08|2,0,E-08|3,6,E-08|3,6,E-08|8,5,E-09|
|AREA|SRC_231|Cam_Cat_23-PEAS e Imp|274915|6389184|3 mes|402,20|8,3,E-08|2,0,E-08|2,4,E-08|4,3,E-08|4,3,E-08|1,0,E-08|
|AREA|SRC_232|Cam_Cat_24-PEAS e Imp|274946|6389307|3 mes|502,79|6,6,E-08|1,6,E-08|2,0,E-08|3,5,E-08|3,5,E-08|8,3,E-09|
|AREA|SRC_233|Cam_Cat_25-PEAS e Imp|275049|6389374|3 mes|485,06|6,8,E-08|1,7,E-08|2,0,E-08|3,6,E-08|3,6,E-08|8,6,E-09|
|AREA|SRC_234|Cam_Cat_26-PEAS e Imp|275181|6389406|3 mes|541,36|6,1,E-08|1,5,E-08|1,8,E-08|3,2,E-08|3,2,E-08|7,7,E-09|
|AREA|SRC_235|Cam_Cat_27-PEAS e Imp|275286|6389385|3 mes|424,34|7,8,E-08|1,9,E-08|2,3,E-08|4,1,E-08|4,1,E-08|9,8,E-09|
|AREA|SRC_236|Cam_Cat_28-PEAS e Imp|275372|6389387|3 mes|345,06|9,6,E-08|2,3,E-08|2,9,E-08|5,1,E-08|5,1,E-08|1,2,E-08|
|AREA|SRC_237|Cam_Cat_29-PEAS e Imp|275519|6389442|3 mes|633,26|5,2,E-08|1,3,E-08|1,6,E-08|2,8,E-08|2,8,E-08|6,6,E-09|
|AREA|SRC_238|Cam_Cat_30-PEAS e Imp|275575|6389512|3 mes|360,36|9,2,E-08|2,2,E-08|2,7,E-08|4,8,E-08|4,8,E-08|1,2,E-08|
|AREA|SRC_239|Cam_Cat_31-PEAS e Imp|275579|6389623|3 mes|447,31|7,4,E-08|1,8,E-08|2,2,E-08|3,9,E-08|3,9,E-08|9,3,E-09|
|AREA|SRC_240|Cam_Cat_32-PEAS e Imp|275473|6389738|3 mes|629,59|5,3,E-08|1,3,E-08|1,6,E-08|2,8,E-08|2,8,E-08|6,6,E-09|
|AREA|SRC_241|Cam_Cat_33-PEAS e Imp|275397|6389809|3 mes|419,18|7,9,E-08|1,9,E-08|2,3,E-08|4,2,E-08|4,2,E-08|9,9,E-09|
|AREA|SRC_242|Cam_Cat_34-PEAS e Imp|275382|6389918|3 mes|432,78|7,7,E-08|1,9,E-08|2,3,E-08|4,0,E-08|4,0,E-08|9,6,E-09|
|AREA|SRC_243|Cam_Cat_35-PEAS e Imp|275487|6390018|3 mes|576,65|5,8,E-08|1,4,E-08|1,7,E-08|3,0,E-08|3,0,E-08|7,2,E-09|
|AREA|SRC_244|Cam_Cat_36-PEAS e Imp|275630|6390045|3 mes|576,34|5,8,E-08|1,4,E-08|1,7,E-08|3,0,E-08|3,0,E-08|7,2,E-09|
|AREA|SRC_245|Cam_Cat_37-PEAS e Imp|275763|6390025|3 mes|532,94|6,2,E-08|1,5,E-08|1,8,E-08|3,3,E-08|3,3,E-08|7,8,E-09|
|AREA|SRC_246|Cam_Cat_38-PEAS e Imp|275861|6389993|3 mes|411,71|8,1,E-08|2,0,E-08|2,4,E-08|4,2,E-08|4,2,E-08|1,0,E-08|
|AREA|SRC_247|Cam_Cat_39-PEAS e Imp|276044|6389963|3 mes|742,87|4,5,E-08|1,1,E-08|1,3,E-08|2,3,E-08|2,3,E-08|5,6,E-09|
|AREA|SRC_248|Cam_Cat_40-PEAS e Imp|276114|6389925|3 mes|316,96|1,0,E-07|2,5,E-08|3,1,E-08|5,5,E-08|5,5,E-08|1,3,E-08|
|AREA|SRC_249|Cam_Cat_41-PEAS e Imp|276133|6389885|3 mes|172,93|1,9,E-07|4,6,E-08|5,7,E-08|1,0,E-07|1,0,E-07|2,4,E-08|
|AREA|SRC_250|Cam_Cat_42-PEAS e Imp|276158|6389818|3 mes|286,84|1,2,E-07|2,8,E-08|3,4,E-08|6,1,E-08|6,1,E-08|1,4,E-08|
|AREA|SRC_251|Cam_Cat_43-PEAS e Imp|276157|6389659|3 mes|632,84|5,2,E-08|1,3,E-08|1,6,E-08|2,8,E-08|2,8,E-08|6,6,E-09|
|AREA|SRC_252|Cam_Cat_44-PEAS e Imp|276172|6389529|3 mes|521,10|6,4,E-08|1,5,E-08|1,9,E-08|3,3,E-08|3,3,E-08|8,0,E-09|
|AREA|SRC_253|Cam_Cat_45-PEAS e Imp|276275|6389477|3 mes|468,32|7,1,E-08|1,7,E-08|2,1,E-08|3,7,E-08|3,7,E-08|8,9,E-09|
|AREA|SRC_254|Cam_Cat_46-PEAS e Imp|276411|6389458|3 mes|553,37|6,0,E-08|1,5,E-08|1,8,E-08|3,2,E-08|3,2,E-08|7,5,E-09|
|AREA|SRC_255|Cam_Cat_47-PEAS e Imp|276501|6389471|3 mes|366,24|9,1,E-08|2,2,E-08|2,7,E-08|4,8,E-08|4,8,E-08|1,1,E-08|
|AREA|SRC_256|Cam_Cat_48-PEAS e Imp|276706|6389673|3 mes|1151,46|2,9,E-08|7,0,E-09|8,6,E-09|1,5,E-08|1,5,E-08|3,6,E-09|
|AREA|SRC_257|Cam_Cat_49-PEAS e Imp|277353|6390498|3 mes|4195,41|7,9,E-09|1,9,E-09|2,3,E-09|4,2,E-09|4,2,E-09|9,9,E-10|
|AREA|SRC_258|Cam_Cat_50-PEAS e Imp|277494|6390575|3 mes|640,03|5,2,E-08|1,3,E-08|1,5,E-08|2,7,E-08|2,7,E-08|6,5,E-09|
|AREA|SRC_259|Cam_Cat_51-PEAS e Imp|279440|6391244|3 mes|8223,68|4,0,E-09|9,8,E-10|1,2,E-09|2,1,E-09|2,1,E-09|5,1,E-10|
|AREA|SRC_260|Cam_Cat_52-PEAS e Imp|283346|6393239|3 mes|17540,88|1,9,E-09|4,6,E-10|5,6,E-10|9,9,E-10|9,9,E-10|2,4,E-10|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 62. Fuentes de Emisión - Escenario 1 parte 6

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 172 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_261|Cam_Cat_53-PEAS e Imp|287745|6394661|3 mes|18483,13|1,8,E-09|4,3,E-10|5,3,E-10|9,4,E-10|9,4,E-10|2,2,E-10|
|AREA|SRC_262|Cam_Pta_1-PEAS e Imp|273147|6383634|3 mes|1866,42|1,8,E-08|4,3,E-09|5,3,E-09|9,3,E-09|9,3,E-09|2,2,E-09|
|AREA|SRC_263|Cam_Pta_2-PEAS e Imp|273165|6383642|3 mes|80,85|4,1,E-07|9,9,E-08|1,2,E-07|2,2,E-07|2,2,E-07|5,1,E-08|
|AREA|SRC_264|Cam_Pta_3-PEAS e Imp|273189|6383637|3 mes|94,14|3,5,E-07|8,5,E-08|1,0,E-07|1,9,E-07|1,9,E-07|4,4,E-08|
|AREA|SRC_265|Cam_Pta_4-PEAS e Imp|273241|6383562|3 mes|359,95|9,2,E-08|2,2,E-08|2,7,E-08|4,8,E-08|4,8,E-08|1,2,E-08|
|AREA|SRC_266|Cam_Pta_5-PEAS e Imp|273289|6383445|3 mes|505,57|6,6,E-08|1,6,E-08|1,9,E-08|3,5,E-08|3,5,E-08|8,2,E-09|
|AREA|SRC_267|Cam_Pta_6-PEAS e Imp|273304|6383402|3 mes|179,62|1,8,E-07|4,5,E-08|5,5,E-08|9,7,E-08|9,7,E-08|2,3,E-08|
|AREA|SRC_268|Cam_Pta_7-PEAS e Imp|273331|6383382|3 mes|138,45|2,4,E-07|5,8,E-08|7,1,E-08|1,3,E-07|1,3,E-07|3,0,E-08|
|AREA|SRC_269|Cam_Pta_8-PEAS e Imp|273361|6383362|3 mes|145,56|2,3,E-07|5,5,E-08|6,8,E-08|1,2,E-07|1,2,E-07|2,9,E-08|
|AREA|SRC_270|Cam_Pta_9-PEAS e Imp|273393|6383346|3 mes|143,99|2,3,E-07|5,6,E-08|6,8,E-08|1,2,E-07|1,2,E-07|2,9,E-08|
|AREA|SRC_271|Cam_Pta_10-PEAS e Imp|273413|6383324|3 mes|116,32|2,9,E-07|6,9,E-08|8,5,E-08|1,5,E-07|1,5,E-07|3,6,E-08|
|AREA|SRC_272|Cam_Pta_11-PEAS e Imp|273447|6383229|3 mes|400,03|8,3,E-08|2,0,E-08|2,5,E-08|4,4,E-08|4,4,E-08|1,0,E-08|
|AREA|SRC_273|Cam_Pta_12-PEAS e Imp|273463|6383220|3 mes|80,13|4,1,E-07|1,0,E-07|1,2,E-07|2,2,E-07|2,2,E-07|5,2,E-08|
|AREA|SRC_274|Cam_Pta_13-PEAS e Imp|273473|6383218|3 mes|45,12|7,4,E-07|1,8,E-07|2,2,E-07|3,9,E-07|3,9,E-07|9,2,E-08|
|AREA|SRC_275|Cam_Pta_14-PEAS e Imp|273519|6383228|3 mes|188,53|1,8,E-07|4,3,E-08|5,2,E-08|9,3,E-08|9,3,E-08|2,2,E-08|
|AREA|SRC_276|Cam_Valpo_1-PEAS e Imp|267407|6370003|3 mes|9181,86|3,6,E-09|8,8,E-10|1,1,E-09|1,9,E-09|1,9,E-09|4,5,E-10|
|AREA|SRC_277|Cam_Valpo_2-PEAS e Imp|267402|6370088|3 mes|338,29|9,8,E-08|2,4,E-08|2,9,E-08|5,2,E-08|5,2,E-08|1,2,E-08|
|AREA|SRC_278|Cam_Valpo_3-PEAS e Imp|267699|6371506|3 mes|5788,94|5,7,E-09|1,4,E-09|1,7,E-09|3,0,E-09|3,0,E-09|7,2,E-10|
|AREA|SRC_279|Cam_Valpo_4-PEAS e Imp|267700|6371619|3 mes|452,00|7,3,E-08|1,8,E-08|2,2,E-08|3,9,E-08|3,9,E-08|9,2,E-09|
|AREA|SRC_280|Cam_Valpo_5-PEAS e Imp|267517|6371917|3 mes|1401,44|2,4,E-08|5,7,E-09|7,0,E-09|1,2,E-08|1,2,E-08|3,0,E-09|
|AREA|SRC_281|Cam_Valpo_6-PEAS e Imp|267499|6371980|3 mes|261,10|1,3,E-07|3,1,E-08|3,8,E-08|6,7,E-08|6,7,E-08|1,6,E-08|
|AREA|SRC_282|Cam_Valpo_7-PEAS e Imp|267496|6372042|3 mes|247,03|1,3,E-07|3,3,E-08|4,0,E-08|7,1,E-08|7,1,E-08|1,7,E-08|
|AREA|SRC_283|Cam_Valpo_8-PEAS e Imp|267518|6372113|3 mes|294,47|1,1,E-07|2,7,E-08|3,3,E-08|5,9,E-08|5,9,E-08|1,4,E-08|
|AREA|SRC_284|Cam_Valpo_9-PEAS e Imp|267547|6372151|3 mes|187,43|1,8,E-07|4,3,E-08|5,3,E-08|9,3,E-08|9,3,E-08|2,2,E-08|
|AREA|SRC_285|Cam_Valpo_10-PEAS e Imp|267569|6372177|3 mes|137,02|2,4,E-07|5,9,E-08|7,2,E-08|1,3,E-07|1,3,E-07|3,0,E-08|
|AREA|SRC_286|Cam_Valpo_11-PEAS e Imp|267738|6372319|3 mes|879,83|3,8,E-08|9,1,E-09|1,1,E-08|2,0,E-08|2,0,E-08|4,7,E-09|
|AREA|SRC_287|Cam_Valpo_12-PEAS e Imp|267762|6372358|3 mes|186,57|1,8,E-07|4,3,E-08|5,3,E-08|9,4,E-08|9,4,E-08|2,2,E-08|
|AREA|SRC_288|Cam_Valpo_13-PEAS e Imp|267783|6372410|3 mes|224,51|1,5,E-07|3,6,E-08|4,4,E-08|7,8,E-08|7,8,E-08|1,9,E-08|
|AREA|SRC_289|Cam_Valpo_14-PEAS e Imp|267855|6372669|3 mes|1075,61|3,1,E-08|7,5,E-09|9,2,E-09|1,6,E-08|1,6,E-08|3,9,E-09|
|AREA|SRC_290|Cam_Valpo_15-PEAS e Imp|267848|6372720|3 mes|207,78|1,6,E-07|3,9,E-08|4,7,E-08|8,4,E-08|8,4,E-08|2,0,E-08|
|AREA|SRC_291|Cam_Valpo_16-PEAS e Imp|267715|6373066|3 mes|1484,08|2,2,E-08|5,4,E-09|6,6,E-09|1,2,E-08|1,2,E-08|2,8,E-09|
|AREA|SRC_292|Cam_Valpo_17-PEAS e Imp|267705|6373122|3 mes|225,43|1,5,E-07|3,6,E-08|4,4,E-08|7,7,E-08|7,7,E-08|1,8,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 63. Fuentes de Emisión - Escenario 1 parte 7

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 173 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_293|Cam_Valpo_18-PEAS e Imp|267701|6373182|3 mes|241,22|1,4,E-07|3,3,E-08|4,1,E-08|7,2,E-08|7,2,E-08|1,7,E-08|
|AREA|SRC_294|Cam_Valpo_19-PEAS e Imp|267704|6373237|3 mes|217,96|1,5,E-07|3,7,E-08|4,5,E-08|8,0,E-08|8,0,E-08|1,9,E-08|
|AREA|SRC_295|Cam_Valpo_20-PEAS e Imp|267713|6373309|3 mes|291,26|1,1,E-07|2,8,E-08|3,4,E-08|6,0,E-08|6,0,E-08|1,4,E-08|
|AREA|SRC_296|Cam_Valpo_21-PEAS e Imp|267741|6373522|3 mes|860,16|3,9,E-08|9,3,E-09|1,1,E-08|2,0,E-08|2,0,E-08|4,8,E-09|
|AREA|SRC_297|Cam_Valpo_22-PEAS e Imp|267757|6373574|3 mes|213,85|1,6,E-07|3,8,E-08|4,6,E-08|8,2,E-08|8,2,E-08|1,9,E-08|
|AREA|SRC_298|Cam_Valpo_23-PEAS e Imp|267777|6373617|3 mes|187,32|1,8,E-07|4,3,E-08|5,3,E-08|9,3,E-08|9,3,E-08|2,2,E-08|
|AREA|SRC_299|Cam_Valpo_24-PEAS e Imp|267817|6373719|3 mes|441,14|7,5,E-08|1,8,E-08|2,2,E-08|4,0,E-08|4,0,E-08|9,4,E-09|
|AREA|SRC_300|Cam_Valpo_25-PEAS e Imp|267843|6373782|3 mes|272,58|1,2,E-07|2,9,E-08|3,6,E-08|6,4,E-08|6,4,E-08|1,5,E-08|
|AREA|SRC_301|Cam_Valpo_26-PEAS e Imp|267877|6373831|3 mes|236,03|1,4,E-07|3,4,E-08|4,2,E-08|7,4,E-08|7,4,E-08|1,8,E-08|
|AREA|SRC_302|Cam_Valpo_27-PEAS e Imp|267910|6373883|3 mes|246,12|1,3,E-07|3,3,E-08|4,0,E-08|7,1,E-08|7,1,E-08|1,7,E-08|
|AREA|SRC_303|Cam_Valpo_28-PEAS e Imp|268105|6374174|3 mes|1399,53|2,4,E-08|5,7,E-09|7,0,E-09|1,2,E-08|1,2,E-08|3,0,E-09|
|AREA|SRC_304|Cam_Valpo_29-PEAS e Imp|268274|6374430|3 mes|1228,07|2,7,E-08|6,5,E-09|8,0,E-09|1,4,E-08|1,4,E-08|3,4,E-09|
|AREA|SRC_305|Cam_Valpo_30-PEAS e Imp|268317|6374478|3 mes|254,35|1,3,E-07|3,2,E-08|3,9,E-08|6,9,E-08|6,9,E-08|1,6,E-08|
|AREA|SRC_306|Cam_Valpo_31-PEAS e Imp|268347|6374502|3 mes|154,46|2,2,E-07|5,2,E-08|6,4,E-08|1,1,E-07|1,1,E-07|2,7,E-08|
|AREA|SRC_307|Cam_Valpo_32-PEAS e Imp|269602|6375295|3 mes|5935,56|5,6,E-09|1,4,E-09|1,7,E-09|2,9,E-09|2,9,E-09|7,0,E-10|
|AREA|SRC_308|Cam_Valpo_33-PEAS e Imp|270646|6375956|3 mes|4938,33|6,7,E-09|1,6,E-09|2,0,E-09|3,5,E-09|3,5,E-09|8,4,E-10|
|AREA|SRC_309|Cam_Valpo_34-PEAS e Imp|270700|6375970|3 mes|220,74|1,5,E-07|3,6,E-08|4,5,E-08|7,9,E-08|7,9,E-08|1,9,E-08|
|AREA|SRC_310|Cam_Valpo_35-PEAS e Imp|270759|6375972|3 mes|232,03|1,4,E-07|3,5,E-08|4,2,E-08|7,5,E-08|7,5,E-08|1,8,E-08|
|AREA|SRC_311|Cam_Valpo_36-PEAS e Imp|270817|6375960|3 mes|237,83|1,4,E-07|3,4,E-08|4,1,E-08|7,3,E-08|7,3,E-08|1,7,E-08|
|AREA|SRC_312|Cam_Valpo_37-PEAS e Imp|271210|6375788|3 mes|1710,95|1,9,E-08|4,7,E-09|5,8,E-09|1,0,E-08|1,0,E-08|2,4,E-09|
|AREA|SRC_313|Cam_Valpo_38-PEAS e Imp|271299|6375786|3 mes|362,06|9,2,E-08|2,2,E-08|2,7,E-08|4,8,E-08|4,8,E-08|1,1,E-08|
|AREA|SRC_314|Cam_Valpo_39-PEAS e Imp|271410|6375784|3 mes|444,09|7,5,E-08|1,8,E-08|2,2,E-08|3,9,E-08|3,9,E-08|9,4,E-09|
|AREA|SRC_315|Cam_Valpo_40-PEAS e Imp|271537|6375829|3 mes|539,94|6,2,E-08|1,5,E-08|1,8,E-08|3,2,E-08|3,2,E-08|7,7,E-09|
|AREA|SRC_316|Cam_Valpo_41-PEAS e Imp|271698|6375908|3 mes|717,64|4,6,E-08|1,1,E-08|1,4,E-08|2,4,E-08|2,4,E-08|5,8,E-09|
|AREA|SRC_317|Cam_Valpo_42-PEAS e Imp|271943|6376040|3 mes|1111,41|3,0,E-08|7,2,E-09|8,9,E-09|1,6,E-08|1,6,E-08|3,7,E-09|
|AREA|SRC_318|Cam_Valpo_43-PEAS e Imp|272216|6376245|3 mes|1365,82|2,4,E-08|5,9,E-09|7,2,E-09|1,3,E-08|1,3,E-08|3,0,E-09|
|AREA|SRC_319|Cam_Valpo_44-PEAS e Imp|272308|6376283|3 mes|396,81|8,4,E-08|2,0,E-08|2,5,E-08|4,4,E-08|4,4,E-08|1,0,E-08|
|AREA|SRC_320|Cam_Valpo_45-PEAS e Imp|272828|6376412|3 mes|2139,51|1,6,E-08|3,8,E-09|4,6,E-09|8,2,E-09|8,2,E-09|1,9,E-09|
|AREA|SRC_321|Cam_Valpo_46-PEAS e Imp|272961|6376463|3 mes|572,90|5,8,E-08|1,4,E-08|1,7,E-08|3,0,E-08|3,0,E-08|7,3,E-09|
|AREA|SRC_322|Cam_Valpo_47-PEAS e Imp|273101|6376548|3 mes|656,43|5,1,E-08|1,2,E-08|1,5,E-08|2,7,E-08|2,7,E-08|6,3,E-09|
|AREA|SRC_323|Cam_Valpo_48-PEAS e Imp|273683|6376890|3 mes|2699,98|1,2,E-08|3,0,E-09|3,6,E-09|6,5,E-09|6,5,E-09|1,5,E-09|
|AREA|SRC_324|Cam_Valpo_49-PEAS e Imp|273729|6376911|3 mes|198,66|1,7,E-07|4,0,E-08|5,0,E-08|8,8,E-08|8,8,E-08|2,1,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 64. Fuentes de Emisión - Escenario 1 parte 8

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 174 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_325|Cam_Valpo_50-PEAS e Imp|273841|6376934|3 mes|455,50|7,3,E-08|1,8,E-08|2,2,E-08|3,8,E-08|3,8,E-08|9,1,E-09|
|AREA|SRC_326|Cam_Valpo_51-PEAS e Imp|273918|6376948|3 mes|314,84|1,1,E-07|2,6,E-08|3,1,E-08|5,5,E-08|5,5,E-08|1,3,E-08|
|AREA|SRC_327|Cam_Valpo_52-PEAS e Imp|273963|6376959|3 mes|182,29|1,8,E-07|4,4,E-08|5,4,E-08|9,6,E-08|9,6,E-08|2,3,E-08|
|AREA|SRC_328|Cam_Valpo_53-PEAS e Imp|274013|6376981|3 mes|220,22|1,5,E-07|3,6,E-08|4,5,E-08|7,9,E-08|7,9,E-08|1,9,E-08|
|AREA|SRC_329|Cam_Valpo_54-PEAS e Imp|274045|6377010|3 mes|175,74|1,9,E-07|4,6,E-08|5,6,E-08|9,9,E-08|9,9,E-08|2,4,E-08|
|AREA|SRC_330|Cam_Valpo_55-PEAS e Imp|274402|6377569|3 mes|2654,98|1,3,E-08|3,0,E-09|3,7,E-09|6,6,E-09|6,6,E-09|1,6,E-09|
|AREA|SRC_331|Cam_Valpo_56-PEAS e Imp|274508|6377712|3 mes|712,20|4,7,E-08|1,1,E-08|1,4,E-08|2,4,E-08|2,4,E-08|5,8,E-09|
|AREA|SRC_332|Cam_Valpo_57-PEAS e Imp|274515|6377737|3 mes|105,54|3,1,E-07|7,6,E-08|9,3,E-08|1,7,E-07|1,7,E-07|3,9,E-08|
|AREA|SRC_333|Cam_Valpo_58-PEAS e Imp|274530|6377783|3 mes|190,85|1,7,E-07|4,2,E-08|5,2,E-08|9,1,E-08|9,1,E-08|2,2,E-08|
|AREA|SRC_334|Cam_Valpo_59-PEAS e Imp|274571|6378190|3 mes|1640,54|2,0,E-08|4,9,E-09|6,0,E-09|1,1,E-08|1,1,E-08|2,5,E-09|
|AREA|SRC_335|Cam_Valpo_60-PEAS e Imp|274512|6378662|3 mes|1902,24|1,7,E-08|4,2,E-09|5,2,E-09|9,2,E-09|9,2,E-09|2,2,E-09|
|AREA|SRC_336|Cam_Valpo_61-PEAS e Imp|274484|6378742|3 mes|339,36|9,8,E-08|2,4,E-08|2,9,E-08|5,1,E-08|5,1,E-08|1,2,E-08|
|AREA|SRC_337|Cam_Valpo_62-PEAS e Imp|274397|6378959|3 mes|934,88|3,6,E-08|8,6,E-09|1,1,E-08|1,9,E-08|1,9,E-08|4,4,E-09|
|AREA|SRC_338|Cam_Valpo_63-PEAS e Imp|274391|6379006|3 mes|189,58|1,8,E-07|4,2,E-08|5,2,E-08|9,2,E-08|9,2,E-08|2,2,E-08|
|AREA|SRC_339|Cam_Valpo_64-PEAS e Imp|274392|6379034|3 mes|109,49|3,0,E-07|7,3,E-08|9,0,E-08|1,6,E-07|1,6,E-07|3,8,E-08|
|AREA|SRC_340|Cam_Valpo_65-PEAS e Imp|274513|6379469|3 mes|1805,57|1,8,E-08|4,5,E-09|5,5,E-09|9,7,E-09|9,7,E-09|2,3,E-09|
|AREA|SRC_341|Cam_Valpo_66-PEAS e Imp|274514|6379510|3 mes|163,36|2,0,E-07|4,9,E-08|6,0,E-08|1,1,E-07|1,1,E-07|2,5,E-08|
|AREA|SRC_342|Cam_Valpo_67-PEAS e Imp|274503|6379560|3 mes|208,73|1,6,E-07|3,9,E-08|4,7,E-08|8,4,E-08|8,4,E-08|2,0,E-08|
|AREA|SRC_343|Cam_Valpo_68-PEAS e Imp|274488|6379623|3 mes|255,44|1,3,E-07|3,1,E-08|3,9,E-08|6,8,E-08|6,8,E-08|1,6,E-08|
|AREA|SRC_344|Cam_Valpo_69-PEAS e Imp|274426|6379798|3 mes|745,56|4,5,E-08|1,1,E-08|1,3,E-08|2,3,E-08|2,3,E-08|5,6,E-09|
|AREA|SRC_345|Cam_Valpo_70-PEAS e Imp|274386|6379897|3 mes|428,53|7,8,E-08|1,9,E-08|2,3,E-08|4,1,E-08|4,1,E-08|9,7,E-09|
|AREA|SRC_346|Cam_Valpo_71-PEAS e Imp|274352|6379981|3 mes|360,23|9,2,E-08|2,2,E-08|2,7,E-08|4,8,E-08|4,8,E-08|1,2,E-08|
|AREA|SRC_347|Cam_Valpo_72-PEAS e Imp|274336|6380041|3 mes|249,49|1,3,E-07|3,2,E-08|3,9,E-08|7,0,E-08|7,0,E-08|1,7,E-08|
|AREA|SRC_348|Cam_Valpo_73-PEAS e Imp|274333|6380099|3 mes|227,80|1,5,E-07|3,5,E-08|4,3,E-08|7,7,E-08|7,7,E-08|1,8,E-08|
|AREA|SRC_349|Cam_Valpo_74-PEAS e Imp|274332|6380163|3 mes|257,27|1,3,E-07|3,1,E-08|3,8,E-08|6,8,E-08|6,8,E-08|1,6,E-08|
|AREA|SRC_350|Cam_Valpo_75-PEAS e Imp|274329|6380546|3 mes|1530,44|2,2,E-08|5,3,E-09|6,4,E-09|1,1,E-08|1,1,E-08|2,7,E-09|
|AREA|SRC_351|Cam_Valpo_76-PEAS e Imp|274323|6380578|3 mes|130,55|2,5,E-07|6,2,E-08|7,5,E-08|1,3,E-07|1,3,E-07|3,2,E-08|
|AREA|SRC_352|Cam_Valpo_77-PEAS e Imp|274308|6380608|3 mes|138,17|2,4,E-07|5,8,E-08|7,1,E-08|1,3,E-07|1,3,E-07|3,0,E-08|
|AREA|SRC_353|Cam_Valpo_78-PEAS e Imp|274078|6381086|3 mes|2120,50|1,6,E-08|3,8,E-09|4,6,E-09|8,2,E-09|8,2,E-09|2,0,E-09|
|AREA|SRC_354|Cam_Valpo_79-PEAS e Imp|274036|6381146|3 mes|292,96|1,1,E-07|2,7,E-08|3,4,E-08|6,0,E-08|6,0,E-08|1,4,E-08|
|AREA|SRC_355|Cam_Valpo_80-PEAS e Imp|273997|6381192|3 mes|242,71|1,4,E-07|3,3,E-08|4,1,E-08|7,2,E-08|7,2,E-08|1,7,E-08|
|AREA|SRC_356|Cam_Valpo_81-PEAS e Imp|273945|6381212|3 mes|225,25|1,5,E-07|3,6,E-08|4,4,E-08|7,7,E-08|7,7,E-08|1,8,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 65. Fuentes de Emisión - Escenario 1 parte 9

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 175 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_357|Cam_Valpo_82-PEAS e Imp|273863|6381235|3 mes|340,59|9,8,E-08|2,4,E-08|2,9,E-08|5,1,E-08|5,1,E-08|1,2,E-08|
|AREA|SRC_358|Cam_Valpo_83-PEAS e Imp|273527|6381309|3 mes|1376,67|2,4,E-08|5,8,E-09|7,2,E-09|1,3,E-08|1,3,E-08|3,0,E-09|
|AREA|SRC_359|Cam_Valpo_84-PEAS e Imp|273488|6381317|3 mes|158,83|2,1,E-07|5,1,E-08|6,2,E-08|1,1,E-07|1,1,E-07|2,6,E-08|
|AREA|SRC_360|Cam_Valpo_85-PEAS e Imp|273437|6381311|3 mes|210,61|1,6,E-07|3,8,E-08|4,7,E-08|8,3,E-08|8,3,E-08|2,0,E-08|
|AREA|SRC_361|Cam_Valpo_86-PEAS e Imp|273400|6381306|3 mes|148,75|2,2,E-07|5,4,E-08|6,6,E-08|1,2,E-07|1,2,E-07|2,8,E-08|
|AREA|SRC_362|Cam_Valpo_87-PEAS e Imp|273330|6381278|3 mes|302,02|1,1,E-07|2,7,E-08|3,3,E-08|5,8,E-08|5,8,E-08|1,4,E-08|
|AREA|SRC_363|Cam_Valpo_88-PEAS e Imp|273269|6381275|3 mes|240,32|1,4,E-07|3,3,E-08|4,1,E-08|7,3,E-08|7,3,E-08|1,7,E-08|
|AREA|SRC_364|Cam_Valpo_89-PEAS e Imp|273210|6381284|3 mes|238,69|1,4,E-07|3,4,E-08|4,1,E-08|7,3,E-08|7,3,E-08|1,7,E-08|
|AREA|SRC_365|Cam_Valpo_90-PEAS e Imp|273140|6381307|3 mes|291,89|1,1,E-07|2,8,E-08|3,4,E-08|6,0,E-08|6,0,E-08|1,4,E-08|
|AREA|SRC_366|Cam_Valpo_91-PEAS e Imp|273026|6381364|3 mes|510,61|6,5,E-08|1,6,E-08|1,9,E-08|3,4,E-08|3,4,E-08|8,1,E-09|
|AREA|SRC_367|Cam_Valpo_92-PEAS e Imp|272787|6381471|3 mes|1046,47|3,2,E-08|7,7,E-09|9,4,E-09|1,7,E-08|1,7,E-08|4,0,E-09|
|AREA|SRC_368|Cam_Valpo_93-PEAS e Imp|272625|6381553|3 mes|726,81|4,6,E-08|1,1,E-08|1,4,E-08|2,4,E-08|2,4,E-08|5,7,E-09|
|AREA|SRC_369|Cam_Valpo_94-PEAS e Imp|272586|6381587|3 mes|205,87|1,6,E-07|3,9,E-08|4,8,E-08|8,5,E-08|8,5,E-08|2,0,E-08|
|AREA|SRC_370|Cam_Valpo_95-PEAS e Imp|272567|6381621|3 mes|150,25|2,2,E-07|5,3,E-08|6,6,E-08|1,2,E-07|1,2,E-07|2,8,E-08|
|AREA|SRC_371|Cam_Valpo_96-PEAS e Imp|272558|6381659|3 mes|154,59|2,1,E-07|5,2,E-08|6,4,E-08|1,1,E-07|1,1,E-07|2,7,E-08|
|AREA|SRC_372|Cam_Valpo_97-PEAS e Imp|272513|6381931|3 mes|1103,20|3,0,E-08|7,3,E-09|8,9,E-09|1,6,E-08|1,6,E-08|3,8,E-09|
|AREA|SRC_373|Cam_Valpo_98-PEAS e Imp|272500|6382030|3 mes|398,37|8,3,E-08|2,0,E-08|2,5,E-08|4,4,E-08|4,4,E-08|1,0,E-08|
|AREA|SRC_374|Cam_Valpo_99-PEAS e Imp|272492|6382086|3 mes|223,87|1,5,E-07|3,6,E-08|4,4,E-08|7,8,E-08|7,8,E-08|1,9,E-08|
|AREA|SRC_375|Cam_Valpo_100-PEAS e Imp|272491|6382127|3 mes|164,32|2,0,E-07|4,9,E-08|6,0,E-08|1,1,E-07|1,1,E-07|2,5,E-08|
|AREA|SRC_376|Cam_Valpo_101-PEAS e Imp|272506|6382188|3 mes|247,33|1,3,E-07|3,2,E-08|4,0,E-08|7,1,E-08|7,1,E-08|1,7,E-08|
|AREA|SRC_377|Cam_Valpo_102-PEAS e Imp|272660|6383439|3 mes|5043,31|6,6,E-09|1,6,E-09|2,0,E-09|3,5,E-09|3,5,E-09|8,2,E-10|
|AREA|SRC_378|Cam_Valpo_103-PEAS e Imp|272630|6384559|3 mes|4478,91|7,4,E-09|1,8,E-09|2,2,E-09|3,9,E-09|3,9,E-09|9,3,E-10|
|AREA|SRC_379|Cam_Valpo_104-PEAS e Imp|272626|6385227|3 mes|2671,08|1,2,E-08|3,0,E-09|3,7,E-09|6,5,E-09|6,5,E-09|1,6,E-09|
|AREA|SRC_380|Cam_Valpo_105-PEAS e Imp|272602|6386454|3 mes|4905,80|6,8,E-09|1,6,E-09|2,0,E-09|3,6,E-09|3,6,E-09|8,5,E-10|
|AREA|SRC_381|Cam_Valpo_106-PEAS e Imp|272609|6386527|3 mes|292,53|1,1,E-07|2,7,E-08|3,4,E-08|6,0,E-08|6,0,E-08|1,4,E-08|
|AREA|SRC_382|Cam_Valpo_107-PEAS e Imp|272650|6386615|3 mes|384,69|8,6,E-08|2,1,E-08|2,6,E-08|4,5,E-08|4,5,E-08|1,1,E-08|
|AREA|SRC_383|Cam_Valpo_108-PEAS e Imp|272755|6386705|3 mes|550,00|6,0,E-08|1,5,E-08|1,8,E-08|3,2,E-08|3,2,E-08|7,6,E-09|
|AREA|SRC_384|Cam_Valpo_109-PEAS e Imp|272846|6386776|3 mes|460,85|7,2,E-08|1,7,E-08|2,1,E-08|3,8,E-08|3,8,E-08|9,0,E-09|
|AREA|SRC_385|Cam_Valpo_110-PEAS e Imp|272918|6386821|3 mes|338,79|9,8,E-08|2,4,E-08|2,9,E-08|5,1,E-08|5,1,E-08|1,2,E-08|
|AREA|SRC_386|Cam_Valpo_111-PEAS e Imp|272959|6386856|3 mes|215,71|1,5,E-07|3,7,E-08|4,6,E-08|8,1,E-08|8,1,E-08|1,9,E-08|
|AREA|SRC_387|Cam_Valpo_112-PEAS e Imp|272979|6386909|3 mes|229,32|1,4,E-07|3,5,E-08|4,3,E-08|7,6,E-08|7,6,E-08|1,8,E-08|
|AREA|SRC_388|Cam_Valpo_113-PEAS e Imp|272982|6386950|3 mes|168,20|2,0,E-07|4,8,E-08|5,9,E-08|1,0,E-07|1,0,E-07|2,5,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 66. Fuentes de Emisión - Escenario 1 parte 10

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 176 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_389|Cam_Valpo_114-PEAS e Imp|272974|6387033|3 mes|334,56|9,9,E-08|2,4,E-08|2,9,E-08|5,2,E-08|5,2,E-08|1,2,E-08|
|AREA|SRC_390|Cam_Valpo_115-PEAS e Imp|272969|6387289|3 mes|1021,26|3,3,E-08|7,9,E-09|9,6,E-09|1,7,E-08|1,7,E-08|4,1,E-09|
|AREA|SRC_391|Cam_Valpo_116-PEAS e Imp|272950|6387316|3 mes|135,86|2,4,E-07|5,9,E-08|7,2,E-08|1,3,E-07|1,3,E-07|3,1,E-08|
|AREA|SRC_392|Cam_Valpo_117-PEAS e Imp|272918|6387332|3 mes|150,62|2,2,E-07|5,3,E-08|6,5,E-08|1,2,E-07|1,2,E-07|2,8,E-08|
|AREA|SRC_393|Cam_Valpo_118-PEAS e Imp|272871|6387328|3 mes|193,11|1,7,E-07|4,2,E-08|5,1,E-08|9,0,E-08|9,0,E-08|2,2,E-08|
|AREA|SRC_394|Cam_Valpo_119-PEAS e Imp|272818|6387319|3 mes|214,82|1,5,E-07|3,7,E-08|4,6,E-08|8,1,E-08|8,1,E-08|1,9,E-08|
|AREA|SRC_395|Cam_Valpo_120-PEAS e Imp|272669|6387324|3 mes|593,51|5,6,E-08|1,4,E-08|1,7,E-08|2,9,E-08|2,9,E-08|7,0,E-09|
|AREA|SRC_396|Cam_Valpo_121-PEAS e Imp|272536|6387380|3 mes|574,11|5,8,E-08|1,4,E-08|1,7,E-08|3,0,E-08|3,0,E-08|7,2,E-09|
|AREA|SRC_397|Cam_Valpo_122-PEAS e Imp|272406|6387475|3 mes|642,85|5,2,E-08|1,3,E-08|1,5,E-08|2,7,E-08|2,7,E-08|6,5,E-09|
|AREA|SRC_398|Cam_Valpo_123-PEAS e Imp|272321|6387544|3 mes|438,86|7,6,E-08|1,8,E-08|2,2,E-08|4,0,E-08|4,0,E-08|9,5,E-09|
|AREA|SRC_399|Cam_Valpo_124-PEAS e Imp|272252|6387605|3 mes|366,01|9,1,E-08|2,2,E-08|2,7,E-08|4,8,E-08|4,8,E-08|1,1,E-08|
|AREA|SRC_400|Cam_Valpo_125-PEAS e Imp|272138|6387749|3 mes|733,97|4,5,E-08|1,1,E-08|1,3,E-08|2,4,E-08|2,4,E-08|5,7,E-09|
|AREA|SRC_401|Cam_Valpo_126-PEAS e Imp|272059|6387890|3 mes|645,70|5,1,E-08|1,2,E-08|1,5,E-08|2,7,E-08|2,7,E-08|6,4,E-09|
|AREA|SRC_402|Cam_Valpo_127-PEAS e Imp|272019|6388008|3 mes|494,29|6,7,E-08|1,6,E-08|2,0,E-08|3,5,E-08|3,5,E-08|8,4,E-09|
|AREA|SRC_403|Cam_Valpo_128-PEAS e Imp|272005|6388086|3 mes|318,17|1,0,E-07|2,5,E-08|3,1,E-08|5,5,E-08|5,5,E-08|1,3,E-08|
|AREA|SRC_404|Cam_Valpo_129-PEAS e Imp|272005|6388171|3 mes|338,40|9,8,E-08|2,4,E-08|2,9,E-08|5,2,E-08|5,2,E-08|1,2,E-08|
|AREA|SRC_405|Cam_Valpo_130-PEAS e Imp|272018|6388207|3 mes|149,40|2,2,E-07|5,4,E-08|6,6,E-08|1,2,E-07|1,2,E-07|2,8,E-08|
|AREA|SRC_406|Cam_Valpo_131-PEAS e Imp|272053|6388222|3 mes|144,57|2,3,E-07|5,6,E-08|6,8,E-08|1,2,E-07|1,2,E-07|2,9,E-08|
|AREA|SRC_407|Cam_Valpo_132-PEAS e Imp|272113|6388260|3 mes|286,19|1,2,E-07|2,8,E-08|3,4,E-08|6,1,E-08|6,1,E-08|1,5,E-08|
|AREA|SRC_408|Cam_Valpo_133-PEAS e Imp|272165|6388289|3 mes|236,50|1,4,E-07|3,4,E-08|4,2,E-08|7,4,E-08|7,4,E-08|1,8,E-08|
|AREA|SRC_409|Cam_Valpo_134-PEAS e Imp|272170|6388313|3 mes|103,04|3,2,E-07|7,8,E-08|9,6,E-08|1,7,E-07|1,7,E-07|4,0,E-08|
|AREA|SRC_410|Cam_Valpo_135-PEAS e Imp|272160|6388355|3 mes|178,67|1,9,E-07|4,5,E-08|5,5,E-08|9,8,E-08|9,8,E-08|2,3,E-08|
|AREA|SRC_411|Cam_Valpo_136-PEAS e Imp|272116|6388384|3 mes|213,17|1,6,E-07|3,8,E-08|4,6,E-08|8,2,E-08|8,2,E-08|1,9,E-08|
|AREA|SRC_412|Cam_Valpo_137-PEAS e Imp|271990|6388473|3 mes|618,26|5,4,E-08|1,3,E-08|1,6,E-08|2,8,E-08|2,8,E-08|6,7,E-09|
|AREA|SRC_413|Cam_Valpo_138-PEAS e Imp|271909|6388570|3 mes|502,24|6,6,E-08|1,6,E-08|2,0,E-08|3,5,E-08|3,5,E-08|8,3,E-09|
|AREA|SRC_414|Cam_Valpo_139-PEAS e Imp|271887|6388631|3 mes|257,67|1,3,E-07|3,1,E-08|3,8,E-08|6,8,E-08|6,8,E-08|1,6,E-08|
|AREA|SRC_415|Cam_Valpo_140-PEAS e Imp|271869|6388710|3 mes|324,57|1,0,E-07|2,5,E-08|3,0,E-08|5,4,E-08|5,4,E-08|1,3,E-08|
|AREA|SRC_416|Cam_Valpo_141-PEAS e Imp|271879|6388778|3 mes|270,72|1,2,E-07|3,0,E-08|3,6,E-08|6,4,E-08|6,4,E-08|1,5,E-08|
|AREA|SRC_417|Cam_Valpo_142-PEAS e Imp|271889|6388831|3 mes|215,81|1,5,E-07|3,7,E-08|4,6,E-08|8,1,E-08|8,1,E-08|1,9,E-08|
|AREA|SRC_418|Cam_Valpo_143-PEAS e Imp|271888|6388910|3 mes|317,54|1,0,E-07|2,5,E-08|3,1,E-08|5,5,E-08|5,5,E-08|1,3,E-08|
|AREA|SRC_419|Cam_Valpo_144-PEAS e Imp|271765|6389249|3 mes|1443,83|2,3,E-08|5,6,E-09|6,8,E-09|1,2,E-08|1,2,E-08|2,9,E-09|
|AREA|SRC_420|Cam_Valpo_145-PEAS e Imp|271745|6389323|3 mes|308,68|1,1,E-07|2,6,E-08|3,2,E-08|5,7,E-08|5,7,E-08|1,3,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 67. Fuentes de Emisión - Escenario 1 parte 11

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 177 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_421|Cam_Valpo_146-PEAS e Imp|271746|6389404|3 mes|321,13|1,0,E-07|2,5,E-08|3,1,E-08|5,4,E-08|5,4,E-08|1,3,E-08|
|AREA|SRC_422|Cam_Valpo_147-PEAS e Imp|271745|6389713|3 mes|1235,33|2,7,E-08|6,5,E-09|8,0,E-09|1,4,E-08|1,4,E-08|3,4,E-09|
|AREA|SRC_423|Cam_Valpo_148-PEAS e Imp|271729|6389779|3 mes|274,74|1,2,E-07|2,9,E-08|3,6,E-08|6,3,E-08|6,3,E-08|1,5,E-08|
|AREA|SRC_424|Cam_Valpo_149-PEAS e Imp|271405|6390771|3 mes|4169,69|8,0,E-09|1,9,E-09|2,4,E-09|4,2,E-09|4,2,E-09|1,0,E-09|
|AREA|SRC_425|Cam_Valpo_150-PEAS e Imp|271408|6390852|3 mes|324,07|1,0,E-07|2,5,E-08|3,0,E-08|5,4,E-08|5,4,E-08|1,3,E-08|
|AREA|SRC_426|Cam_Valpo_151-PEAS e Imp|271425|6390918|3 mes|269,76|1,2,E-07|3,0,E-08|3,7,E-08|6,5,E-08|6,5,E-08|1,5,E-08|
|AREA|SRC_427|Cam_Valpo_152-PEAS e Imp|271595|6391444|3 mes|2210,20|1,5,E-08|3,6,E-09|4,5,E-09|7,9,E-09|7,9,E-09|1,9,E-09|
|AREA|SRC_428|Cam_Valpo_153-PEAS e Imp|271601|6391518|3 mes|297,07|1,1,E-07|2,7,E-08|3,3,E-08|5,9,E-08|5,9,E-08|1,4,E-08|
|AREA|SRC_429|Cam_Valpo_154-PEAS e Imp|271583|6391599|3 mes|334,56|9,9,E-08|2,4,E-08|2,9,E-08|5,2,E-08|5,2,E-08|1,2,E-08|
|AREA|SRC_430|Cam_Valpo_155-PEAS e Imp|271490|6391665|3 mes|462,29|7,2,E-08|1,7,E-08|2,1,E-08|3,8,E-08|3,8,E-08|9,0,E-09|
|AREA|SRC_431|Cam_Valpo_156-PEAS e Imp|271388|6391779|3 mes|610,49|5,4,E-08|1,3,E-08|1,6,E-08|2,9,E-08|2,9,E-08|6,8,E-09|
|AREA|SRC_432|Cam_Valpo_157-PEAS e Imp|271303|6391969|3 mes|829,95|4,0,E-08|9,7,E-09|1,2,E-08|2,1,E-08|2,1,E-08|5,0,E-09|
|AREA|SRC_433|Cam_Valpo_158-PEAS e Imp|271249|6392048|3 mes|385,48|8,6,E-08|2,1,E-08|2,6,E-08|4,5,E-08|4,5,E-08|1,1,E-08|
|AREA|SRC_434|Cam_Valpo_159-PEAS e Imp|271095|6392199|3 mes|863,11|3,8,E-08|9,3,E-09|1,1,E-08|2,0,E-08|2,0,E-08|4,8,E-09|
|AREA|SRC_435|Cam_Valpo_160-PEAS e Imp|271003|6392357|3 mes|727,41|4,6,E-08|1,1,E-08|1,4,E-08|2,4,E-08|2,4,E-08|5,7,E-09|
|AREA|SRC_436|Cam_Valpo_161-PEAS e Imp|270864|6392618|3 mes|1181,67|2,8,E-08|6,8,E-09|8,3,E-09|1,5,E-08|1,5,E-08|3,5,E-09|
|AREA|SRC_437|Cam_Valpo_162-PEAS e Imp|270665|6392901|3 mes|1386,67|2,4,E-08|5,8,E-09|7,1,E-09|1,3,E-08|1,3,E-08|3,0,E-09|
|AREA|SRC_438|Cam_Valpo_163-PEAS e Imp|270570|6393060|3 mes|739,81|4,5,E-08|1,1,E-08|1,3,E-08|2,4,E-08|2,4,E-08|5,6,E-09|
|AREA|SRC_439|Cam_Valpo_164-PEAS e Imp|270535|6393162|3 mes|427,94|7,8,E-08|1,9,E-08|2,3,E-08|4,1,E-08|4,1,E-08|9,7,E-09|
|AREA|SRC_440|Cam_Valpo_165-PEAS e Imp|270408|6393157|3 mes|516,16|6,4,E-08|1,6,E-08|1,9,E-08|3,4,E-08|3,4,E-08|8,1,E-09|
|AREA|SRC_441|Cam_Valpo_166-PEAS e Imp|270322|6393156|3 mes|344,11|9,7,E-08|2,3,E-08|2,9,E-08|5,1,E-08|5,1,E-08|1,2,E-08|
|AREA|SRC_442|Cam_Valpo_167-PEAS e Imp|270198|6393225|3 mes|562,03|5,9,E-08|1,4,E-08|1,8,E-08|3,1,E-08|3,1,E-08|7,4,E-09|
|AREA|SRC_443|Cam_Valpo_168-PEAS e Imp|270084|6393222|3 mes|461,57|7,2,E-08|1,7,E-08|2,1,E-08|3,8,E-08|3,8,E-08|9,0,E-09|
|AREA|SRC_444|Cam_Valpo_169-PEAS e Imp|270014|6393114|3 mes|520,05|6,4,E-08|1,5,E-08|1,9,E-08|3,4,E-08|3,4,E-08|8,0,E-09|
|AREA|SRC_445|Cam_Valpo_170-PEAS e Imp|269944|6393026|3 mes|448,19|7,4,E-08|1,8,E-08|2,2,E-08|3,9,E-08|3,9,E-08|9,3,E-09|
|AREA|SRC_446|Cam_Valpo_171-PEAS e Imp|269831|6392981|3 mes|484,35|6,9,E-08|1,7,E-08|2,0,E-08|3,6,E-08|3,6,E-08|8,6,E-09|
|AREA|SRC_447|Cam_Valpo_172-PEAS e Imp|269702|6392966|3 mes|516,99|6,4,E-08|1,6,E-08|1,9,E-08|3,4,E-08|3,4,E-08|8,0,E-09|
|AREA|SRC_448|Cam_Valpo_173-PEAS e Imp|269506|6393084|3 mes|906,73|3,7,E-08|8,9,E-09|1,1,E-08|1,9,E-08|1,9,E-08|4,6,E-09|
|AREA|SRC_449|Cam_Valpo_174-PEAS e Imp|269407|6393106|3 mes|410,62|8,1,E-08|2,0,E-08|2,4,E-08|4,2,E-08|4,2,E-08|1,0,E-08|
|AREA|SRC_450|Cam_Valpo_175-PEAS e Imp|269355|6393219|3 mes|493,13|6,7,E-08|1,6,E-08|2,0,E-08|3,5,E-08|3,5,E-08|8,4,E-09|
|AREA|SRC_451|Cam_Valpo_176-PEAS e Imp|269450|6393436|3 mes|939,57|3,5,E-08|8,6,E-09|1,0,E-08|1,9,E-08|1,9,E-08|4,4,E-09|
|AREA|SRC_452|Cam_Valpo_177-PEAS e Imp|269537|6393768|3 mes|1375,49|2,4,E-08|5,8,E-09|7,2,E-09|1,3,E-08|1,3,E-08|3,0,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 68. Fuentes de Emisión - Escenario 1 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 178 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_453|Cam_Valpo_178-PEAS e Imp|269541|6393876|3 mes|433,16|7,7,E-08|1,9,E-08|2,3,E-08|4,0,E-08|4,0,E-08|9,6,E-09|
|AREA|SRC_454|Cam_Valpo_179-PEAS e Imp|269514|6393952|3 mes|327,49|1,0,E-07|2,5,E-08|3,0,E-08|5,3,E-08|5,3,E-08|1,3,E-08|
|AREA|SRC_455|Cam_Valpo_180-PEAS e Imp|269461|6394006|3 mes|302,03|1,1,E-07|2,7,E-08|3,3,E-08|5,8,E-08|5,8,E-08|1,4,E-08|
|AREA|SRC_456|Cam_Valpo_181-PEAS e Imp|269456|6394087|3 mes|317,54|1,0,E-07|2,5,E-08|3,1,E-08|5,5,E-08|5,5,E-08|1,3,E-08|
|AREA|SRC_457|Cam_Valpo_182-PEAS e Imp|269494|6394169|3 mes|358,94|9,3,E-08|2,2,E-08|2,7,E-08|4,9,E-08|4,9,E-08|1,2,E-08|
|AREA|SRC_458|Cam_Valpo_183-PEAS e Imp|269580|6394296|3 mes|611,99|5,4,E-08|1,3,E-08|1,6,E-08|2,9,E-08|2,9,E-08|6,8,E-09|
|AREA|SRC_459|Cam_Valpo_184-PEAS e Imp|269614|6394394|3 mes|416,61|8,0,E-08|1,9,E-08|2,4,E-08|4,2,E-08|4,2,E-08|1,0,E-08|
|AREA|SRC_460|Cam_Valpo_185-PEAS e Imp|269617|6394492|3 mes|396,57|8,4,E-08|2,0,E-08|2,5,E-08|4,4,E-08|4,4,E-08|1,0,E-08|
|AREA|SRC_461|Cam_Valpo_186-PEAS e Imp|269532|6394634|3 mes|664,18|5,0,E-08|1,2,E-08|1,5,E-08|2,6,E-08|2,6,E-08|6,3,E-09|
|AREA|SRC_462|Cam_Valpo_187-PEAS e Imp|269478|6394752|3 mes|518,20|6,4,E-08|1,6,E-08|1,9,E-08|3,4,E-08|3,4,E-08|8,0,E-09|
|AREA|SRC_463|Cam_Valpo_188-PEAS e Imp|269437|6394881|3 mes|540,93|6,1,E-08|1,5,E-08|1,8,E-08|3,2,E-08|3,2,E-08|7,7,E-09|
|AREA|SRC_464|Cam_Valpo_189-PEAS e Imp|269448|6395002|3 mes|483,46|6,9,E-08|1,7,E-08|2,0,E-08|3,6,E-08|3,6,E-08|8,6,E-09|
|AREA|SRC_465|Cam_Valpo_190-PEAS e Imp|269465|6395049|3 mes|197,82|1,7,E-07|4,1,E-08|5,0,E-08|8,8,E-08|8,8,E-08|2,1,E-08|
|AREA|SRC_466|Cam_Valpo_191-PEAS e Imp|269701|6395188|3 mes|1088,66|3,1,E-08|7,4,E-09|9,0,E-09|1,6,E-08|1,6,E-08|3,8,E-09|
|AREA|SRC_467|Cam_Valpo_192-PEAS e Imp|269737|6395244|3 mes|269,38|1,2,E-07|3,0,E-08|3,7,E-08|6,5,E-08|6,5,E-08|1,5,E-08|
|AREA|SRC_468|Cam_Valpo_193-PEAS e Imp|269748|6395318|3 mes|301,88|1,1,E-07|2,7,E-08|3,3,E-08|5,8,E-08|5,8,E-08|1,4,E-08|
|AREA|SRC_469|Cam_Valpo_194-PEAS e Imp|269734|6395473|3 mes|624,02|5,3,E-08|1,3,E-08|1,6,E-08|2,8,E-08|2,8,E-08|6,7,E-09|
|AREA|SRC_470|Cam_Valpo_195-PEAS e Imp|269791|6395575|3 mes|462,91|7,2,E-08|1,7,E-08|2,1,E-08|3,8,E-08|3,8,E-08|9,0,E-09|
|AREA|SRC_471|Cam_Valpo_196-PEAS e Imp|269918|6395634|3 mes|557,57|6,0,E-08|1,4,E-08|1,8,E-08|3,1,E-08|3,1,E-08|7,5,E-09|
|AREA|SRC_472|Cam_Valpo_197-PEAS e Imp|269951|6395703|3 mes|311,66|1,1,E-07|2,6,E-08|3,2,E-08|5,6,E-08|5,6,E-08|1,3,E-08|
|AREA|SRC_473|Cam_Valpo_198-PEAS e Imp|269926|6395767|3 mes|277,87|1,2,E-07|2,9,E-08|3,5,E-08|6,3,E-08|6,3,E-08|1,5,E-08|
|AREA|SRC_474|Cam_Valpo_199-PEAS e Imp|269853|6395812|3 mes|348,28|9,5,E-08|2,3,E-08|2,8,E-08|5,0,E-08|5,0,E-08|1,2,E-08|
|AREA|SRC_475|Cam_Valpo_200-PEAS e Imp|269732|6395847|3 mes|504,67|6,6,E-08|1,6,E-08|2,0,E-08|3,5,E-08|3,5,E-08|8,2,E-09|
|AREA|SRC_476|Cam_Valpo_201-PEAS e Imp|269688|6395928|3 mes|365,46|9,1,E-08|2,2,E-08|2,7,E-08|4,8,E-08|4,8,E-08|1,1,E-08|
|AREA|SRC_477|Cam_Valpo_202-PEAS e Imp|269717|6396047|3 mes|484,68|6,9,E-08|1,7,E-08|2,0,E-08|3,6,E-08|3,6,E-08|8,6,E-09|
|AREA|SRC_478|Cam_Valpo_203-PEAS e Imp|269712|6396106|3 mes|237,49|1,4,E-07|3,4,E-08|4,1,E-08|7,3,E-08|7,3,E-08|1,7,E-08|
|AREA|SRC_479|Cam_Valpo_204-PEAS e Imp|269657|6396143|3 mes|271,48|1,2,E-07|3,0,E-08|3,6,E-08|6,4,E-08|6,4,E-08|1,5,E-08|
|AREA|SRC_480|Cam_Valpo_205-PEAS e Imp|269580|6396120|3 mes|326,46|1,0,E-07|2,5,E-08|3,0,E-08|5,3,E-08|5,3,E-08|1,3,E-08|
|AREA|SRC_481|Cam_Valpo_206-PEAS e Imp|269501|6396070|3 mes|376,20|8,8,E-08|2,1,E-08|2,6,E-08|4,6,E-08|4,6,E-08|1,1,E-08|
|AREA|SRC_482|Cam_Valpo_207-PEAS e Imp|269359|6396026|3 mes|593,54|5,6,E-08|1,4,E-08|1,7,E-08|2,9,E-08|2,9,E-08|7,0,E-09|
|AREA|SRC_483|Cam_Valpo_208-PEAS e Imp|269272|6396023|3 mes|343,48|9,7,E-08|2,3,E-08|2,9,E-08|5,1,E-08|5,1,E-08|1,2,E-08|
|AREA|SRC_484|Cam_Valpo_209-PEAS e Imp|269222|6396073|3 mes|275,81|1,2,E-07|2,9,E-08|3,6,E-08|6,3,E-08|6,3,E-08|1,5,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 69. Fuentes de Emisión - Escenario 1 parte 13

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 179 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_485|Cam_Valpo_210-PEAS e Imp|269210|6396185|3 mes|446,25|7,4,E-08|1,8,E-08|2,2,E-08|3,9,E-08|3,9,E-08|9,3,E-09|
|AREA|SRC_486|Cam_Valpo_211-PEAS e Imp|269167|6396232|3 mes|255,46|1,3,E-07|3,1,E-08|3,9,E-08|6,8,E-08|6,8,E-08|1,6,E-08|
|AREA|SRC_487|Cam_Valpo_212-PEAS e Imp|269082|6396226|3 mes|349,58|9,5,E-08|2,3,E-08|2,8,E-08|5,0,E-08|5,0,E-08|1,2,E-08|
|AREA|SRC_488|Cam_Valpo_213-PEAS e Imp|268998|6396240|3 mes|335,54|9,9,E-08|2,4,E-08|2,9,E-08|5,2,E-08|5,2,E-08|1,2,E-08|
|AREA|SRC_489|Cam_Valpo_214-PEAS e Imp|268894|6396300|3 mes|480,09|6,9,E-08|1,7,E-08|2,1,E-08|3,6,E-08|3,6,E-08|8,7,E-09|
|AREA|SRC_490|Cam_Valpo_215-PEAS e Imp|268805|6396381|3 mes|477,49|7,0,E-08|1,7,E-08|2,1,E-08|3,7,E-08|3,7,E-08|8,7,E-09|
|AREA|SRC_491|Cam_Valpo_216-PEAS e Imp|268734|6396481|3 mes|489,34|6,8,E-08|1,6,E-08|2,0,E-08|3,6,E-08|3,6,E-08|8,5,E-09|
|AREA|SRC_492|Cam_Valpo_217-PEAS e Imp|268692|6396569|3 mes|388,32|8,6,E-08|2,1,E-08|2,5,E-08|4,5,E-08|4,5,E-08|1,1,E-08|
|AREA|SRC_493|Cam_Valpo_218-PEAS e Imp|268614|6396686|3 mes|563,68|5,9,E-08|1,4,E-08|1,7,E-08|3,1,E-08|3,1,E-08|7,4,E-09|
|AREA|SRC_494|Cam_Valpo_219-PEAS e Imp|268551|6396751|3 mes|365,13|9,1,E-08|2,2,E-08|2,7,E-08|4,8,E-08|4,8,E-08|1,1,E-08|
|AREA|SRC_495|Cam_Valpo_220-PEAS e Imp|268525|6396834|3 mes|342,75|9,7,E-08|2,3,E-08|2,9,E-08|5,1,E-08|5,1,E-08|1,2,E-08|
|AREA|SRC_496|Cam_Valpo_221-PEAS e Imp|268521|6396918|3 mes|335,20|9,9,E-08|2,4,E-08|2,9,E-08|5,2,E-08|5,2,E-08|1,2,E-08|
|AREA|SRC_497|Cam_Valpo_222-PEAS e Imp|268510|6396996|3 mes|312,17|1,1,E-07|2,6,E-08|3,2,E-08|5,6,E-08|5,6,E-08|1,3,E-08|
|AREA|SRC_498|Cam_Valpo_223-PEAS e Imp|268441|6397095|3 mes|486,78|6,8,E-08|1,7,E-08|2,0,E-08|3,6,E-08|3,6,E-08|8,5,E-09|
|AREA|SRC_499|Cam_Valpo_224-PEAS e Imp|268352|6397195|3 mes|537,81|6,2,E-08|1,5,E-08|1,8,E-08|3,2,E-08|3,2,E-08|7,7,E-09|
|AREA|SRC_500|Cam_Valpo_225-PEAS e Imp|268295|6397296|3 mes|460,41|7,2,E-08|1,7,E-08|2,1,E-08|3,8,E-08|3,8,E-08|9,0,E-09|
|AREA|SRC_501|Cam_Valpo_226-PEAS e Imp|268265|6397370|3 mes|319,00|1,0,E-07|2,5,E-08|3,1,E-08|5,5,E-08|5,5,E-08|1,3,E-08|
|AREA|SRC_502|Cam_Valpo_227-PEAS e Imp|268236|6397470|3 mes|414,51|8,0,E-08|1,9,E-08|2,4,E-08|4,2,E-08|4,2,E-08|1,0,E-08|
|AREA|SRC_503|Cam_Valpo_228-PEAS e Imp|268225|6397539|3 mes|278,02|1,2,E-07|2,9,E-08|3,5,E-08|6,3,E-08|6,3,E-08|1,5,E-08|
|AREA|SRC_504|Cam_Valpo_229-PEAS e Imp|268212|6397650|3 mes|446,47|7,4,E-08|1,8,E-08|2,2,E-08|3,9,E-08|3,9,E-08|9,3,E-09|
|AREA|SRC_505|Cam_Valpo_230-PEAS e Imp|268292|6397691|3 mes|352,90|9,4,E-08|2,3,E-08|2,8,E-08|4,9,E-08|4,9,E-08|1,2,E-08|
|AREA|SRC_506|Cam_Valpo_231-PEAS e Imp|268324|6397741|3 mes|244,09|1,4,E-07|3,3,E-08|4,0,E-08|7,1,E-08|7,1,E-08|1,7,E-08|
|AREA|SRC_507|Cam_Valpo_232-PEAS e Imp|268344|6397809|3 mes|284,52|1,2,E-07|2,8,E-08|3,5,E-08|6,1,E-08|6,1,E-08|1,5,E-08|
|AREA|SRC_508|Cam_Valpo_233-PEAS e Imp|268317|6397871|3 mes|277,40|1,2,E-07|2,9,E-08|3,6,E-08|6,3,E-08|6,3,E-08|1,5,E-08|
|AREA|SRC_509|Cam_Valpo_234-PEAS e Imp|268289|6397931|3 mes|263,44|1,3,E-07|3,1,E-08|3,7,E-08|6,6,E-08|6,6,E-08|1,6,E-08|
|AREA|SRC_510|Cam_Valpo_235-PEAS e Imp|268281|6397993|3 mes|246,21|1,3,E-07|3,3,E-08|4,0,E-08|7,1,E-08|7,1,E-08|1,7,E-08|
|AREA|SRC_511|Cam_Valpo_236-PEAS e Imp|268325|6398057|3 mes|307,11|1,1,E-07|2,6,E-08|3,2,E-08|5,7,E-08|5,7,E-08|1,4,E-08|
|AREA|SRC_512|Cam_Valpo_237-PEAS e Imp|268339|6398092|3 mes|154,12|2,2,E-07|5,2,E-08|6,4,E-08|1,1,E-07|1,1,E-07|2,7,E-08|
|AREA|SRC_513|Cam_Valpo_238-PEAS e Imp|268362|6398151|3 mes|251,56|1,3,E-07|3,2,E-08|3,9,E-08|6,9,E-08|6,9,E-08|1,7,E-08|
|AREA|SRC_514|Cam_Valpo_239-PEAS e Imp|268383|6398192|3 mes|185,19|1,8,E-07|4,3,E-08|5,3,E-08|9,4,E-08|9,4,E-08|2,2,E-08|
|AREA|SRC_515|Cam_Valpo_240-PEAS e Imp|268355|6398247|3 mes|250,18|1,3,E-07|3,2,E-08|3,9,E-08|7,0,E-08|7,0,E-08|1,7,E-08|
|AREA|SRC_516|Cam_Valpo_241-PEAS e Imp|268227|6398303|3 mes|566,84|5,9,E-08|1,4,E-08|1,7,E-08|3,1,E-08|3,1,E-08|7,3,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 70. Fuentes de Emisión - Escenario 1 parte 14

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 180 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_517|Cam_Valpo_242-PEAS e Imp|268140|6398362|3 mes|418,83|7,9,E-08|1,9,E-08|2,4,E-08|4,2,E-08|4,2,E-08|9,9,E-09|
|AREA|SRC_518|Cam_Valpo_243-PEAS e Imp|268089|6398427|3 mes|325,43|1,0,E-07|2,5,E-08|3,0,E-08|5,4,E-08|5,4,E-08|1,3,E-08|
|AREA|SRC_519|Cam_Valpo_244-PEAS e Imp|268005|6398483|3 mes|406,15|8,2,E-08|2,0,E-08|2,4,E-08|4,3,E-08|4,3,E-08|1,0,E-08|
|AREA|SRC_520|Cam_Valpo_245-PEAS e Imp|267956|6398553|3 mes|338,26|9,8,E-08|2,4,E-08|2,9,E-08|5,2,E-08|5,2,E-08|1,2,E-08|
|AREA|SRC_521|Cam_Valpo_246-PEAS e Imp|267920|6398673|3 mes|498,96|6,7,E-08|1,6,E-08|2,0,E-08|3,5,E-08|3,5,E-08|8,3,E-09|
|AREA|SRC_522|Cam_Valpo_247-PEAS e Imp|267908|6398749|3 mes|308,37|1,1,E-07|2,6,E-08|3,2,E-08|5,7,E-08|5,7,E-08|1,3,E-08|
|AREA|SRC_523|Cam_Valpo_248-PEAS e Imp|267894|6398771|3 mes|107,41|3,1,E-07|7,5,E-08|9,2,E-08|1,6,E-07|1,6,E-07|3,9,E-08|
|AREA|SRC_524|Cam_Valpo_249-PEAS e Imp|267791|6398823|3 mes|466,56|7,1,E-08|1,7,E-08|2,1,E-08|3,7,E-08|3,7,E-08|8,9,E-09|
|AREA|SRC_525|Cam_Valpo_250-PEAS e Imp|267747|6398849|3 mes|204,00|1,6,E-07|3,9,E-08|4,8,E-08|8,6,E-08|8,6,E-08|2,0,E-08|
|AREA|SRC_526|Cam_Valpo_251-PEAS e Imp|267699|6398875|3 mes|217,15|1,5,E-07|3,7,E-08|4,5,E-08|8,0,E-08|8,0,E-08|1,9,E-08|
|AREA|SRC_527|Cam_Valpo_252-PEAS e Imp|267673|6398943|3 mes|285,91|1,2,E-07|2,8,E-08|3,4,E-08|6,1,E-08|6,1,E-08|1,5,E-08|
|AREA|SRC_528|Cam_Valpo_253-PEAS e Imp|267740|6399152|3 mes|871,99|3,8,E-08|9,2,E-09|1,1,E-08|2,0,E-08|2,0,E-08|4,8,E-09|
|AREA|SRC_529|Cam_Valpo_254-PEAS e Imp|267754|6399259|3 mes|434,37|7,6,E-08|1,9,E-08|2,3,E-08|4,0,E-08|4,0,E-08|9,6,E-09|
|AREA|SRC_530|Cam_Valpo_255-PEAS e Imp|267756|6399372|3 mes|452,93|7,3,E-08|1,8,E-08|2,2,E-08|3,9,E-08|3,9,E-08|9,2,E-09|
|AREA|SRC_531|Cam_Valpo_256-PEAS e Imp|267702|6399478|3 mes|480,03|6,9,E-08|1,7,E-08|2,1,E-08|3,6,E-08|3,6,E-08|8,7,E-09|
|AREA|SRC_532|Cam_Valpo_257-PEAS e Imp|267740|6399547|3 mes|307,21|1,1,E-07|2,6,E-08|3,2,E-08|5,7,E-08|5,7,E-08|1,4,E-08|
|AREA|SRC_533|Cam_Valpo_258-PEAS e Imp|267742|6399624|3 mes|311,56|1,1,E-07|2,6,E-08|3,2,E-08|5,6,E-08|5,6,E-08|1,3,E-08|
|AREA|SRC_534|Cam_Valpo_259-PEAS e Imp|267731|6399695|3 mes|287,58|1,2,E-07|2,8,E-08|3,4,E-08|6,1,E-08|6,1,E-08|1,4,E-08|
|AREA|SRC_535|Cam_Valpo_260-PEAS e Imp|267682|6399788|3 mes|425,70|7,8,E-08|1,9,E-08|2,3,E-08|4,1,E-08|4,1,E-08|9,8,E-09|
|AREA|SRC_536|Cam_Valpo_261-PEAS e Imp|267661|6399830|3 mes|187,04|1,8,E-07|4,3,E-08|5,3,E-08|9,3,E-08|9,3,E-08|2,2,E-08|
|AREA|SRC_537|PTAS|273586|6383219|10 meses|4,00|2,3,E-02|1,1,E-02|1,1,E-01|0,0,E+00|0,0,E+00|0,0,E+00|
|AREA|SRC_540|Cam_Cat_1-PTAS|273043|6387323|10 meses|383,32|2,3,E-09|5,6,E-10|6,9,E-10|3,4,E-10|8,1,E-09|1,9,E-09|
|AREA|SRC_541|Cam_Cat_2-PTAS|273206|6387558|10 meses|1145,03|7,8,E-10|1,9,E-10|2,3,E-10|1,1,E-10|2,7,E-09|6,3,E-10|
|AREA|SRC_542|Cam_Cat_3-PTAS|273308|6387612|10 meses|456,00|2,0,E-09|4,7,E-10|5,8,E-10|2,9,E-10|6,8,E-09|1,6,E-09|
|AREA|SRC_543|Cam_Cat_4-PTAS|273511|6387668|10 meses|843,57|1,1,E-09|2,6,E-10|3,1,E-10|1,6,E-10|3,7,E-09|8,6,E-10|
|AREA|SRC_544|Cam_Cat_5-PTAS|273721|6387707|10 meses|853,32|1,0,E-09|2,5,E-10|3,1,E-10|1,5,E-10|3,7,E-09|8,5,E-10|
|AREA|SRC_545|Cam_Cat_6-PTAS|273880|6387880|10 meses|945,26|9,4,E-10|2,3,E-10|2,8,E-10|1,4,E-10|3,3,E-09|7,7,E-10|
|AREA|SRC_546|Cam_Cat_7-PTAS|273982|6387934|10 meses|457,52|2,0,E-09|4,7,E-10|5,8,E-10|2,9,E-10|6,8,E-09|1,6,E-09|
|AREA|SRC_547|Cam_Cat_8-PTAS|274178|6387916|10 meses|782,20|1,1,E-09|2,8,E-10|3,4,E-10|1,7,E-10|4,0,E-09|9,3,E-10|
|AREA|SRC_548|Cam_Cat_9-PTAS|274216|6387945|10 meses|195,48|4,6,E-09|1,1,E-09|1,4,E-09|6,7,E-10|1,6,E-08|3,7,E-09|
|AREA|SRC_549|Cam_Cat_10-PTAS|274213|6388017|10 meses|295,61|3,0,E-09|7,3,E-10|9,0,E-10|4,4,E-10|1,1,E-08|2,5,E-09|
|AREA|SRC_550|Cam_Cat_11-PTAS|274177|6388250|10 meses|941,53|9,5,E-10|2,3,E-10|2,8,E-10|1,4,E-10|3,3,E-09|7,7,E-10|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 71. Fuentes de Emisión - Escenario 1 parte 15

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 181 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_551|Cam_Cat_12-PTAS|274185|6388365|10 meses|458,34|1,9,E-09|4,7,E-10|5,8,E-10|2,9,E-10|6,8,E-09|1,6,E-09|
|AREA|SRC_552|Cam_Cat_13-PTAS|274352|6388558|10 meses|1016,92|8,8,E-10|2,1,E-10|2,6,E-10|1,3,E-10|3,1,E-09|7,1,E-10|
|AREA|SRC_553|Cam_Cat_14-PTAS|274654|6388846|10 meses|1667,00|5,4,E-10|1,3,E-10|1,6,E-10|7,8,E-11|1,9,E-09|4,4,E-10|
|AREA|SRC_554|Cam_Cat_15-PTAS|274745|6388895|10 meses|409,81|2,2,E-09|5,3,E-10|6,5,E-10|3,2,E-10|7,6,E-09|1,8,E-09|
|AREA|SRC_555|Cam_Cat_16-PTAS|274834|6388862|10 meses|371,12|2,4,E-09|5,8,E-10|7,1,E-10|3,5,E-10|8,4,E-09|2,0,E-09|
|AREA|SRC_556|Cam_Cat_17-PTAS|274882|6388794|10 meses|331,29|2,7,E-09|6,5,E-10|8,0,E-10|3,9,E-10|9,4,E-09|2,2,E-09|
|AREA|SRC_557|Cam_Cat_18-PTAS|274979|6388768|10 meses|406,63|2,2,E-09|5,3,E-10|6,5,E-10|3,2,E-10|7,7,E-09|1,8,E-09|
|AREA|SRC_558|Cam_Cat_19-PTAS|275069|6388799|10 meses|384,16|2,3,E-09|5,6,E-10|6,9,E-10|3,4,E-10|8,1,E-09|1,9,E-09|
|AREA|SRC_559|Cam_Cat_20-PTAS|275059|6388911|10 meses|459,52|1,9,E-09|4,7,E-10|5,8,E-10|2,8,E-10|6,8,E-09|1,6,E-09|
|AREA|SRC_560|Cam_Cat_21-PTAS|275040|6389003|10 meses|374,05|2,4,E-09|5,8,E-10|7,1,E-10|3,5,E-10|8,3,E-09|1,9,E-09|
|AREA|SRC_561|Cam_Cat_22-PTAS|274958|6389092|10 meses|489,11|1,8,E-09|4,4,E-10|5,4,E-10|2,7,E-10|6,4,E-09|1,5,E-09|
|AREA|SRC_562|Cam_Cat_23-PTAS|274915|6389184|10 meses|402,20|2,2,E-09|5,4,E-10|6,6,E-10|3,3,E-10|7,8,E-09|1,8,E-09|
|AREA|SRC_563|Cam_Cat_24-PTAS|274946|6389307|10 meses|502,79|1,8,E-09|4,3,E-10|5,3,E-10|2,6,E-10|6,2,E-09|1,4,E-09|
|AREA|SRC_564|Cam_Cat_25-PTAS|275049|6389374|10 meses|485,06|1,8,E-09|4,5,E-10|5,5,E-10|2,7,E-10|6,4,E-09|1,5,E-09|
|AREA|SRC_565|Cam_Cat_26-PTAS|275181|6389406|10 meses|541,36|1,6,E-09|4,0,E-10|4,9,E-10|2,4,E-10|5,8,E-09|1,3,E-09|
|AREA|SRC_566|Cam_Cat_27-PTAS|275286|6389385|10 meses|424,34|2,1,E-09|5,1,E-10|6,2,E-10|3,1,E-10|7,4,E-09|1,7,E-09|
|AREA|SRC_567|Cam_Cat_28-PTAS|275372|6389387|10 meses|345,06|2,6,E-09|6,3,E-10|7,7,E-10|3,8,E-10|9,0,E-09|2,1,E-09|
|AREA|SRC_568|Cam_Cat_29-PTAS|275519|6389442|10 meses|633,26|1,4,E-09|3,4,E-10|4,2,E-10|2,1,E-10|4,9,E-09|1,1,E-09|
|AREA|SRC_569|Cam_Cat_30-PTAS|275575|6389512|10 meses|360,36|2,5,E-09|6,0,E-10|7,3,E-10|3,6,E-10|8,7,E-09|2,0,E-09|
|AREA|SRC_570|Cam_Cat_31-PTAS|275579|6389623|10 meses|447,31|2,0,E-09|4,8,E-10|5,9,E-10|2,9,E-10|7,0,E-09|1,6,E-09|
|AREA|SRC_571|Cam_Cat_32-PTAS|275473|6389738|10 meses|629,59|1,4,E-09|3,4,E-10|4,2,E-10|2,1,E-10|5,0,E-09|1,2,E-09|
|AREA|SRC_572|Cam_Cat_33-PTAS|275397|6389809|10 meses|419,18|2,1,E-09|5,2,E-10|6,3,E-10|3,1,E-10|7,4,E-09|1,7,E-09|
|AREA|SRC_573|Cam_Cat_34-PTAS|275382|6389918|10 meses|432,78|2,1,E-09|5,0,E-10|6,1,E-10|3,0,E-10|7,2,E-09|1,7,E-09|
|AREA|SRC_574|Cam_Cat_35-PTAS|275487|6390018|10 meses|576,65|1,5,E-09|3,7,E-10|4,6,E-10|2,3,E-10|5,4,E-09|1,3,E-09|
|AREA|SRC_575|Cam_Cat_36-PTAS|275630|6390045|10 meses|576,34|1,5,E-09|3,7,E-10|4,6,E-10|2,3,E-10|5,4,E-09|1,3,E-09|
|AREA|SRC_576|Cam_Cat_37-PTAS|275763|6390025|10 meses|532,94|1,7,E-09|4,1,E-10|5,0,E-10|2,5,E-10|5,9,E-09|1,4,E-09|
|AREA|SRC_577|Cam_Cat_38-PTAS|275861|6389993|10 meses|411,71|2,2,E-09|5,2,E-10|6,4,E-10|3,2,E-10|7,6,E-09|1,8,E-09|
|AREA|SRC_578|Cam_Cat_39-PTAS|276044|6389963|10 meses|742,87|1,2,E-09|2,9,E-10|3,6,E-10|1,8,E-10|4,2,E-09|9,8,E-10|
|AREA|SRC_579|Cam_Cat_40-PTAS|276114|6389925|10 meses|316,96|2,8,E-09|6,8,E-10|8,3,E-10|4,1,E-10|9,8,E-09|2,3,E-09|
|AREA|SRC_580|Cam_Cat_41-PTAS|276133|6389885|10 meses|172,93|5,2,E-09|1,2,E-09|1,5,E-09|7,6,E-10|1,8,E-08|4,2,E-09|
|AREA|SRC_581|Cam_Cat_42-PTAS|276158|6389818|10 meses|286,84|3,1,E-09|7,5,E-10|9,2,E-10|4,6,E-10|1,1,E-08|2,5,E-09|
|AREA|SRC_582|Cam_Cat_43-PTAS|276157|6389659|10 meses|632,84|1,4,E-09|3,4,E-10|4,2,E-10|2,1,E-10|4,9,E-09|1,1,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 72. Fuentes de Emisión - Escenario 1 parte 16

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 182 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_583|Cam_Cat_44-PTAS|276172|6389529|10 meses|521,10|1,7,E-09|4,1,E-10|5,1,E-10|2,5,E-10|6,0,E-09|1,4,E-09|
|AREA|SRC_584|Cam_Cat_45-PTAS|276275|6389477|10 meses|468,32|1,9,E-09|4,6,E-10|5,7,E-10|2,8,E-10|6,7,E-09|1,6,E-09|
|AREA|SRC_585|Cam_Cat_46-PTAS|276411|6389458|10 meses|553,37|1,6,E-09|3,9,E-10|4,8,E-10|2,4,E-10|5,6,E-09|1,3,E-09|
|AREA|SRC_586|Cam_Cat_47-PTAS|276501|6389471|10 meses|366,24|2,4,E-09|5,9,E-10|7,2,E-10|3,6,E-10|8,5,E-09|2,0,E-09|
|AREA|SRC_587|Cam_Cat_48-PTAS|276706|6389673|10 meses|1151,46|7,8,E-10|1,9,E-10|2,3,E-10|1,1,E-10|2,7,E-09|6,3,E-10|
|AREA|SRC_588|Cam_Cat_49-PTAS|277353|6390498|10 meses|4195,41|2,1,E-10|5,1,E-11|6,3,E-11|3,1,E-11|7,4,E-10|1,7,E-10|
|AREA|SRC_589|Cam_Cat_50-PTAS|277494|6390575|10 meses|640,03|1,4,E-09|3,4,E-10|4,1,E-10|2,0,E-10|4,9,E-09|1,1,E-09|
|AREA|SRC_590|Cam_Cat_51-PTAS|279440|6391244|10 meses|8223,68|1,1,E-10|2,6,E-11|3,2,E-11|1,6,E-11|3,8,E-10|8,8,E-11|
|AREA|SRC_591|Cam_Cat_52-PTAS|283346|6393239|10 meses|17540,88|5,1,E-11|1,2,E-11|1,5,E-11|7,5,E-12|1,8,E-10|4,1,E-11|
|AREA|SRC_592|Cam_Cat_53-PTAS|287745|6394661|10 meses|18483,13|4,8,E-11|1,2,E-11|1,4,E-11|7,1,E-12|1,7,E-10|3,9,E-11|
|AREA|SRC_593|Cam_Pta_1-PTAS|273147|6383634|10 meses|1866,42|4,8,E-10|1,2,E-10|1,4,E-10|7,0,E-11|1,7,E-09|3,9,E-10|
|AREA|SRC_594|Cam_Pta_2-PTAS|273165|6383642|10 meses|80,85|1,1,E-08|2,7,E-09|3,3,E-09|1,6,E-09|3,9,E-08|9,0,E-09|
|AREA|SRC_595|Cam_Pta_3-PTAS|273189|6383637|10 meses|94,14|9,5,E-09|2,3,E-09|2,8,E-09|1,4,E-09|3,3,E-08|7,7,E-09|
|AREA|SRC_596|Cam_Pta_4-PTAS|273241|6383562|10 meses|359,95|2,5,E-09|6,0,E-10|7,4,E-10|3,6,E-10|8,7,E-09|2,0,E-09|
|AREA|SRC_597|Cam_Pta_5-PTAS|273289|6383445|10 meses|505,57|1,8,E-09|4,3,E-10|5,2,E-10|2,6,E-10|6,2,E-09|1,4,E-09|
|AREA|SRC_598|Cam_Pta_6-PTAS|273304|6383402|10 meses|179,62|5,0,E-09|1,2,E-09|1,5,E-09|7,3,E-10|1,7,E-08|4,0,E-09|
|AREA|SRC_599|Cam_Pta_7-PTAS|273331|6383382|10 meses|138,45|6,4,E-09|1,6,E-09|1,9,E-09|9,5,E-10|2,3,E-08|5,2,E-09|
|AREA|SRC_600|Cam_Pta_8-PTAS|273361|6383362|10 meses|145,56|6,1,E-09|1,5,E-09|1,8,E-09|9,0,E-10|2,1,E-08|5,0,E-09|
|AREA|SRC_601|Cam_Pta_9-PTAS|273393|6383346|10 meses|143,99|6,2,E-09|1,5,E-09|1,8,E-09|9,1,E-10|2,2,E-08|5,0,E-09|
|AREA|SRC_602|Cam_Pta_10-PTAS|273413|6383324|10 meses|116,32|7,7,E-09|1,9,E-09|2,3,E-09|1,1,E-09|2,7,E-08|6,2,E-09|
|AREA|SRC_603|Cam_Pta_11-PTAS|273447|6383229|10 meses|400,03|2,2,E-09|5,4,E-10|6,6,E-10|3,3,E-10|7,8,E-09|1,8,E-09|
|AREA|SRC_604|Cam_Pta_12-PTAS|273463|6383220|10 meses|80,13|1,1,E-08|2,7,E-09|3,3,E-09|1,6,E-09|3,9,E-08|9,1,E-09|
|AREA|SRC_605|Cam_Pta_13-PTAS|273473|6383218|10 meses|45,12|2,0,E-08|4,8,E-09|5,9,E-09|2,9,E-09|6,9,E-08|1,6,E-08|
|AREA|SRC_606|Cam_Pta_14-PTAS|273519|6383228|10 meses|188,53|4,7,E-09|1,1,E-09|1,4,E-09|6,9,E-10|1,7,E-08|3,9,E-09|
|AREA|SRC_607|Cam_Valpo_1-PTAS|267407|6370003|10 meses|9181,86|9,7,E-11|2,4,E-11|2,9,E-11|1,4,E-11|3,4,E-10|7,9,E-11|
|AREA|SRC_608|Cam_Valpo_2-PTAS|267402|6370088|10 meses|338,29|2,6,E-09|6,4,E-10|7,8,E-10|3,9,E-10|9,2,E-09|2,1,E-09|
|AREA|SRC_609|Cam_Valpo_3-PTAS|267699|6371506|10 meses|5788,94|1,5,E-10|3,7,E-11|4,6,E-11|2,3,E-11|5,4,E-10|1,3,E-10|
|AREA|SRC_610|Cam_Valpo_4-PTAS|267700|6371619|10 meses|452,00|2,0,E-09|4,8,E-10|5,9,E-10|2,9,E-10|6,9,E-09|1,6,E-09|
|AREA|SRC_611|Cam_Valpo_5-PTAS|267517|6371917|10 meses|1401,44|6,4,E-10|1,5,E-10|1,9,E-10|9,3,E-11|2,2,E-09|5,2,E-10|
|AREA|SRC_612|Cam_Valpo_6-PTAS|267499|6371980|10 meses|261,10|3,4,E-09|8,3,E-10|1,0,E-09|5,0,E-10|1,2,E-08|2,8,E-09|
|AREA|SRC_613|Cam_Valpo_7-PTAS|267496|6372042|10 meses|247,03|3,6,E-09|8,7,E-10|1,1,E-09|5,3,E-10|1,3,E-08|2,9,E-09|
|AREA|SRC_614|Cam_Valpo_8-PTAS|267518|6372113|10 meses|294,47|3,0,E-09|7,3,E-10|9,0,E-10|4,4,E-10|1,1,E-08|2,5,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 73. Fuentes de Emisión - Escenario 1 parte 17

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 183 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_615|Cam_Valpo_9-PTAS|267547|6372151|10 meses|187,43|4,8,E-09|1,2,E-09|1,4,E-09|7,0,E-10|1,7,E-08|3,9,E-09|
|AREA|SRC_616|Cam_Valpo_10-PTAS|267569|6372177|10 meses|137,02|6,5,E-09|1,6,E-09|1,9,E-09|9,5,E-10|2,3,E-08|5,3,E-09|
|AREA|SRC_617|Cam_Valpo_11-PTAS|267738|6372319|10 meses|879,83|1,0,E-09|2,5,E-10|3,0,E-10|1,5,E-10|3,5,E-09|8,3,E-10|
|AREA|SRC_618|Cam_Valpo_12-PTAS|267762|6372358|10 meses|186,57|4,8,E-09|1,2,E-09|1,4,E-09|7,0,E-10|1,7,E-08|3,9,E-09|
|AREA|SRC_619|Cam_Valpo_13-PTAS|267783|6372410|10 meses|224,51|4,0,E-09|9,6,E-10|1,2,E-09|5,8,E-10|1,4,E-08|3,2,E-09|
|AREA|SRC_620|Cam_Valpo_14-PTAS|267855|6372669|10 meses|1075,61|8,3,E-10|2,0,E-10|2,5,E-10|1,2,E-10|2,9,E-09|6,7,E-10|
|AREA|SRC_621|Cam_Valpo_15-PTAS|267848|6372720|10 meses|207,78|4,3,E-09|1,0,E-09|1,3,E-09|6,3,E-10|1,5,E-08|3,5,E-09|
|AREA|SRC_622|Cam_Valpo_16-PTAS|267715|6373066|10 meses|1484,08|6,0,E-10|1,5,E-10|1,8,E-10|8,8,E-11|2,1,E-09|4,9,E-10|
|AREA|SRC_623|Cam_Valpo_17-PTAS|267705|6373122|10 meses|225,43|4,0,E-09|9,6,E-10|1,2,E-09|5,8,E-10|1,4,E-08|3,2,E-09|
|AREA|SRC_624|Cam_Valpo_18-PTAS|267701|6373182|10 meses|241,22|3,7,E-09|9,0,E-10|1,1,E-09|5,4,E-10|1,3,E-08|3,0,E-09|
|AREA|SRC_625|Cam_Valpo_19-PTAS|267704|6373237|10 meses|217,96|4,1,E-09|9,9,E-10|1,2,E-09|6,0,E-10|1,4,E-08|3,3,E-09|
|AREA|SRC_626|Cam_Valpo_20-PTAS|267713|6373309|10 meses|291,26|3,1,E-09|7,4,E-10|9,1,E-10|4,5,E-10|1,1,E-08|2,5,E-09|
|AREA|SRC_627|Cam_Valpo_21-PTAS|267741|6373522|10 meses|860,16|1,0,E-09|2,5,E-10|3,1,E-10|1,5,E-10|3,6,E-09|8,4,E-10|
|AREA|SRC_628|Cam_Valpo_22-PTAS|267757|6373574|10 meses|213,85|4,2,E-09|1,0,E-09|1,2,E-09|6,1,E-10|1,5,E-08|3,4,E-09|
|AREA|SRC_629|Cam_Valpo_23-PTAS|267777|6373617|10 meses|187,32|4,8,E-09|1,2,E-09|1,4,E-09|7,0,E-10|1,7,E-08|3,9,E-09|
|AREA|SRC_630|Cam_Valpo_24-PTAS|267817|6373719|10 meses|441,14|2,0,E-09|4,9,E-10|6,0,E-10|3,0,E-10|7,1,E-09|1,6,E-09|
|AREA|SRC_631|Cam_Valpo_25-PTAS|267843|6373782|10 meses|272,58|3,3,E-09|7,9,E-10|9,7,E-10|4,8,E-10|1,1,E-08|2,7,E-09|
|AREA|SRC_632|Cam_Valpo_26-PTAS|267877|6373831|10 meses|236,03|3,8,E-09|9,2,E-10|1,1,E-09|5,5,E-10|1,3,E-08|3,1,E-09|
|AREA|SRC_633|Cam_Valpo_27-PTAS|267910|6373883|10 meses|246,12|3,6,E-09|8,8,E-10|1,1,E-09|5,3,E-10|1,3,E-08|2,9,E-09|
|AREA|SRC_634|Cam_Valpo_28-PTAS|268105|6374174|10 meses|1399,53|6,4,E-10|1,5,E-10|1,9,E-10|9,3,E-11|2,2,E-09|5,2,E-10|
|AREA|SRC_635|Cam_Valpo_29-PTAS|268274|6374430|10 meses|1228,07|7,3,E-10|1,8,E-10|2,2,E-10|1,1,E-10|2,5,E-09|5,9,E-10|
|AREA|SRC_636|Cam_Valpo_30-PTAS|268317|6374478|10 meses|254,35|3,5,E-09|8,5,E-10|1,0,E-09|5,1,E-10|1,2,E-08|2,9,E-09|
|AREA|SRC_637|Cam_Valpo_31-PTAS|268347|6374502|10 meses|154,46|5,8,E-09|1,4,E-09|1,7,E-09|8,5,E-10|2,0,E-08|4,7,E-09|
|AREA|SRC_638|Cam_Valpo_32-PTAS|269602|6375295|10 meses|5935,56|1,5,E-10|3,6,E-11|4,5,E-11|2,2,E-11|5,3,E-10|1,2,E-10|
|AREA|SRC_639|Cam_Valpo_33-PTAS|270646|6375956|10 meses|4938,33|1,8,E-10|4,4,E-11|5,4,E-11|2,6,E-11|6,3,E-10|1,5,E-10|
|AREA|SRC_640|Cam_Valpo_34-PTAS|270700|6375970|10 meses|220,74|4,0,E-09|9,8,E-10|1,2,E-09|5,9,E-10|1,4,E-08|3,3,E-09|
|AREA|SRC_641|Cam_Valpo_35-PTAS|270759|6375972|10 meses|232,03|3,8,E-09|9,3,E-10|1,1,E-09|5,6,E-10|1,3,E-08|3,1,E-09|
|AREA|SRC_642|Cam_Valpo_36-PTAS|270817|6375960|10 meses|237,83|3,8,E-09|9,1,E-10|1,1,E-09|5,5,E-10|1,3,E-08|3,1,E-09|
|AREA|SRC_643|Cam_Valpo_37-PTAS|271210|6375788|10 meses|1710,95|5,2,E-10|1,3,E-10|1,5,E-10|7,6,E-11|1,8,E-09|4,2,E-10|
|AREA|SRC_644|Cam_Valpo_38-PTAS|271299|6375786|10 meses|362,06|2,5,E-09|6,0,E-10|7,3,E-10|3,6,E-10|8,6,E-09|2,0,E-09|
|AREA|SRC_645|Cam_Valpo_39-PTAS|271410|6375784|10 meses|444,09|2,0,E-09|4,9,E-10|6,0,E-10|2,9,E-10|7,0,E-09|1,6,E-09|
|AREA|SRC_646|Cam_Valpo_40-PTAS|271537|6375829|10 meses|539,94|1,7,E-09|4,0,E-10|4,9,E-10|2,4,E-10|5,8,E-09|1,3,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 74. Fuentes de Emisión - Escenario 1 parte 18

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 184 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_647|Cam_Valpo_41-PTAS|271698|6375908|10 meses|717,64|1,2,E-09|3,0,E-10|3,7,E-10|1,8,E-10|4,3,E-09|1,0,E-09|
|AREA|SRC_648|Cam_Valpo_42-PTAS|271943|6376040|10 meses|1111,41|8,0,E-10|1,9,E-10|2,4,E-10|1,2,E-10|2,8,E-09|6,5,E-10|
|AREA|SRC_649|Cam_Valpo_43-PTAS|272216|6376245|10 meses|1365,82|6,5,E-10|1,6,E-10|1,9,E-10|9,6,E-11|2,3,E-09|5,3,E-10|
|AREA|SRC_650|Cam_Valpo_44-PTAS|272308|6376283|10 meses|396,81|2,2,E-09|5,4,E-10|6,7,E-10|3,3,E-10|7,9,E-09|1,8,E-09|
|AREA|SRC_651|Cam_Valpo_45-PTAS|272828|6376412|10 meses|2139,51|4,2,E-10|1,0,E-10|1,2,E-10|6,1,E-11|1,5,E-09|3,4,E-10|
|AREA|SRC_652|Cam_Valpo_46-PTAS|272961|6376463|10 meses|572,90|1,6,E-09|3,8,E-10|4,6,E-10|2,3,E-10|5,4,E-09|1,3,E-09|
|AREA|SRC_653|Cam_Valpo_47-PTAS|273101|6376548|10 meses|656,43|1,4,E-09|3,3,E-10|4,0,E-10|2,0,E-10|4,8,E-09|1,1,E-09|
|AREA|SRC_654|Cam_Valpo_48-PTAS|273683|6376890|10 meses|2699,98|3,3,E-10|8,0,E-11|9,8,E-11|4,8,E-11|1,2,E-09|2,7,E-10|
|AREA|SRC_655|Cam_Valpo_49-PTAS|273729|6376911|10 meses|198,66|4,5,E-09|1,1,E-09|1,3,E-09|6,6,E-10|1,6,E-08|3,7,E-09|
|AREA|SRC_656|Cam_Valpo_50-PTAS|273841|6376934|10 meses|455,50|2,0,E-09|4,7,E-10|5,8,E-10|2,9,E-10|6,9,E-09|1,6,E-09|
|AREA|SRC_657|Cam_Valpo_51-PTAS|273918|6376948|10 meses|314,84|2,8,E-09|6,9,E-10|8,4,E-10|4,2,E-10|9,9,E-09|2,3,E-09|
|AREA|SRC_658|Cam_Valpo_52-PTAS|273963|6376959|10 meses|182,29|4,9,E-09|1,2,E-09|1,5,E-09|7,2,E-10|1,7,E-08|4,0,E-09|
|AREA|SRC_659|Cam_Valpo_53-PTAS|274013|6376981|10 meses|220,22|4,1,E-09|9,8,E-10|1,2,E-09|5,9,E-10|1,4,E-08|3,3,E-09|
|AREA|SRC_660|Cam_Valpo_54-PTAS|274045|6377010|10 meses|175,74|5,1,E-09|1,2,E-09|1,5,E-09|7,4,E-10|1,8,E-08|4,1,E-09|
|AREA|SRC_661|Cam_Valpo_55-PTAS|274402|6377569|10 meses|2654,98|3,4,E-10|8,1,E-11|1,0,E-10|4,9,E-11|1,2,E-09|2,7,E-10|
|AREA|SRC_662|Cam_Valpo_56-PTAS|274508|6377712|10 meses|712,20|1,3,E-09|3,0,E-10|3,7,E-10|1,8,E-10|4,4,E-09|1,0,E-09|
|AREA|SRC_663|Cam_Valpo_57-PTAS|274515|6377737|10 meses|105,54|8,5,E-09|2,0,E-09|2,5,E-09|1,2,E-09|3,0,E-08|6,9,E-09|
|AREA|SRC_664|Cam_Valpo_58-PTAS|274530|6377783|10 meses|190,85|4,7,E-09|1,1,E-09|1,4,E-09|6,9,E-10|1,6,E-08|3,8,E-09|
|AREA|SRC_665|Cam_Valpo_59-PTAS|274571|6378190|10 meses|1640,54|5,4,E-10|1,3,E-10|1,6,E-10|8,0,E-11|1,9,E-09|4,4,E-10|
|AREA|SRC_666|Cam_Valpo_60-PTAS|274512|6378662|10 meses|1902,24|4,7,E-10|1,1,E-10|1,4,E-10|6,9,E-11|1,6,E-09|3,8,E-10|
|AREA|SRC_667|Cam_Valpo_61-PTAS|274484|6378742|10 meses|339,36|2,6,E-09|6,4,E-10|7,8,E-10|3,9,E-10|9,2,E-09|2,1,E-09|
|AREA|SRC_668|Cam_Valpo_62-PTAS|274397|6378959|10 meses|934,88|9,5,E-10|2,3,E-10|2,8,E-10|1,4,E-10|3,3,E-09|7,8,E-10|
|AREA|SRC_669|Cam_Valpo_63-PTAS|274391|6379006|10 meses|189,58|4,7,E-09|1,1,E-09|1,4,E-09|6,9,E-10|1,6,E-08|3,8,E-09|
|AREA|SRC_670|Cam_Valpo_64-PTAS|274392|6379034|10 meses|109,49|8,2,E-09|2,0,E-09|2,4,E-09|1,2,E-09|2,9,E-08|6,6,E-09|
|AREA|SRC_671|Cam_Valpo_65-PTAS|274513|6379469|10 meses|1805,57|4,9,E-10|1,2,E-10|1,5,E-10|7,2,E-11|1,7,E-09|4,0,E-10|
|AREA|SRC_672|Cam_Valpo_66-PTAS|274514|6379510|10 meses|163,36|5,5,E-09|1,3,E-09|1,6,E-09|8,0,E-10|1,9,E-08|4,4,E-09|
|AREA|SRC_673|Cam_Valpo_67-PTAS|274503|6379560|10 meses|208,73|4,3,E-09|1,0,E-09|1,3,E-09|6,3,E-10|1,5,E-08|3,5,E-09|
|AREA|SRC_674|Cam_Valpo_68-PTAS|274488|6379623|10 meses|255,44|3,5,E-09|8,5,E-10|1,0,E-09|5,1,E-10|1,2,E-08|2,8,E-09|
|AREA|SRC_675|Cam_Valpo_69-PTAS|274426|6379798|10 meses|745,56|1,2,E-09|2,9,E-10|3,5,E-10|1,8,E-10|4,2,E-09|9,7,E-10|
|AREA|SRC_676|Cam_Valpo_70-PTAS|274386|6379897|10 meses|428,53|2,1,E-09|5,0,E-10|6,2,E-10|3,1,E-10|7,3,E-09|1,7,E-09|
|AREA|SRC_677|Cam_Valpo_71-PTAS|274352|6379981|10 meses|360,23|2,5,E-09|6,0,E-10|7,3,E-10|3,6,E-10|8,7,E-09|2,0,E-09|
|AREA|SRC_678|Cam_Valpo_72-PTAS|274336|6380041|10 meses|249,49|3,6,E-09|8,7,E-10|1,1,E-09|5,2,E-10|1,3,E-08|2,9,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 75. Fuentes de Emisión - Escenario 1 parte 19

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 185 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_679|Cam_Valpo_73-PTAS|274333|6380099|10 meses|227,80|3,9,E-09|9,5,E-10|1,2,E-09|5,7,E-10|1,4,E-08|3,2,E-09|
|AREA|SRC_680|Cam_Valpo_74-PTAS|274332|6380163|10 meses|257,27|3,5,E-09|8,4,E-10|1,0,E-09|5,1,E-10|1,2,E-08|2,8,E-09|
|AREA|SRC_681|Cam_Valpo_75-PTAS|274329|6380546|10 meses|1530,44|5,8,E-10|1,4,E-10|1,7,E-10|8,5,E-11|2,0,E-09|4,7,E-10|
|AREA|SRC_682|Cam_Valpo_76-PTAS|274323|6380578|10 meses|130,55|6,8,E-09|1,7,E-09|2,0,E-09|1,0,E-09|2,4,E-08|5,6,E-09|
|AREA|SRC_683|Cam_Valpo_77-PTAS|274308|6380608|10 meses|138,17|6,5,E-09|1,6,E-09|1,9,E-09|9,5,E-10|2,3,E-08|5,3,E-09|
|AREA|SRC_684|Cam_Valpo_78-PTAS|274078|6381086|10 meses|2120,50|4,2,E-10|1,0,E-10|1,2,E-10|6,2,E-11|1,5,E-09|3,4,E-10|
|AREA|SRC_685|Cam_Valpo_79-PTAS|274036|6381146|10 meses|292,96|3,0,E-09|7,4,E-10|9,0,E-10|4,5,E-10|1,1,E-08|2,5,E-09|
|AREA|SRC_686|Cam_Valpo_80-PTAS|273997|6381192|10 meses|242,71|3,7,E-09|8,9,E-10|1,1,E-09|5,4,E-10|1,3,E-08|3,0,E-09|
|AREA|SRC_687|Cam_Valpo_81-PTAS|273945|6381212|10 meses|225,25|4,0,E-09|9,6,E-10|1,2,E-09|5,8,E-10|1,4,E-08|3,2,E-09|
|AREA|SRC_688|Cam_Valpo_82-PTAS|273863|6381235|10 meses|340,59|2,6,E-09|6,3,E-10|7,8,E-10|3,8,E-10|9,2,E-09|2,1,E-09|
|AREA|SRC_689|Cam_Valpo_83-PTAS|273527|6381309|10 meses|1376,67|6,5,E-10|1,6,E-10|1,9,E-10|9,5,E-11|2,3,E-09|5,3,E-10|
|AREA|SRC_690|Cam_Valpo_84-PTAS|273488|6381317|10 meses|158,83|5,6,E-09|1,4,E-09|1,7,E-09|8,2,E-10|2,0,E-08|4,6,E-09|
|AREA|SRC_691|Cam_Valpo_85-PTAS|273437|6381311|10 meses|210,61|4,2,E-09|1,0,E-09|1,3,E-09|6,2,E-10|1,5,E-08|3,4,E-09|
|AREA|SRC_692|Cam_Valpo_86-PTAS|273400|6381306|10 meses|148,75|6,0,E-09|1,5,E-09|1,8,E-09|8,8,E-10|2,1,E-08|4,9,E-09|
|AREA|SRC_693|Cam_Valpo_87-PTAS|273330|6381278|10 meses|302,02|3,0,E-09|7,2,E-10|8,8,E-10|4,3,E-10|1,0,E-08|2,4,E-09|
|AREA|SRC_694|Cam_Valpo_88-PTAS|273269|6381275|10 meses|240,32|3,7,E-09|9,0,E-10|1,1,E-09|5,4,E-10|1,3,E-08|3,0,E-09|
|AREA|SRC_695|Cam_Valpo_89-PTAS|273210|6381284|10 meses|238,69|3,7,E-09|9,0,E-10|1,1,E-09|5,5,E-10|1,3,E-08|3,0,E-09|
|AREA|SRC_696|Cam_Valpo_90-PTAS|273140|6381307|10 meses|291,89|3,1,E-09|7,4,E-10|9,1,E-10|4,5,E-10|1,1,E-08|2,5,E-09|
|AREA|SRC_697|Cam_Valpo_91-PTAS|273026|6381364|10 meses|510,61|1,7,E-09|4,2,E-10|5,2,E-10|2,6,E-10|6,1,E-09|1,4,E-09|
|AREA|SRC_698|Cam_Valpo_92-PTAS|272787|6381471|10 meses|1046,47|8,5,E-10|2,1,E-10|2,5,E-10|1,3,E-10|3,0,E-09|6,9,E-10|
|AREA|SRC_699|Cam_Valpo_93-PTAS|272625|6381553|10 meses|726,81|1,2,E-09|3,0,E-10|3,6,E-10|1,8,E-10|4,3,E-09|1,0,E-09|
|AREA|SRC_700|Cam_Valpo_94-PTAS|272586|6381587|10 meses|205,87|4,3,E-09|1,0,E-09|1,3,E-09|6,4,E-10|1,5,E-08|3,5,E-09|
|AREA|SRC_701|Cam_Valpo_95-PTAS|272567|6381621|10 meses|150,25|5,9,E-09|1,4,E-09|1,8,E-09|8,7,E-10|2,1,E-08|4,8,E-09|
|AREA|SRC_702|Cam_Valpo_96-PTAS|272558|6381659|10 meses|154,59|5,8,E-09|1,4,E-09|1,7,E-09|8,5,E-10|2,0,E-08|4,7,E-09|
|AREA|SRC_703|Cam_Valpo_97-PTAS|272513|6381931|10 meses|1103,20|8,1,E-10|2,0,E-10|2,4,E-10|1,2,E-10|2,8,E-09|6,6,E-10|
|AREA|SRC_704|Cam_Valpo_98-PTAS|272500|6382030|10 meses|398,37|2,2,E-09|5,4,E-10|6,6,E-10|3,3,E-10|7,8,E-09|1,8,E-09|
|AREA|SRC_705|Cam_Valpo_99-PTAS|272492|6382086|10 meses|223,87|4,0,E-09|9,6,E-10|1,2,E-09|5,8,E-10|1,4,E-08|3,2,E-09|
|AREA|SRC_706|Cam_Valpo_100-PTAS|272491|6382127|10 meses|164,32|5,4,E-09|1,3,E-09|1,6,E-09|8,0,E-10|1,9,E-08|4,4,E-09|
|AREA|SRC_707|Cam_Valpo_101-PTAS|272506|6382188|10 meses|247,33|3,6,E-09|8,7,E-10|1,1,E-09|5,3,E-10|1,3,E-08|2,9,E-09|
|AREA|SRC_708|Cam_Valpo_102-PTAS|272660|6383439|10 meses|5043,31|1,8,E-10|4,3,E-11|5,2,E-11|2,6,E-11|6,2,E-10|1,4,E-10|
|AREA|SRC_709|Cam_Valpo_103-PTAS|272630|6384559|10 meses|4478,91|2,0,E-10|4,8,E-11|5,9,E-11|2,9,E-11|7,0,E-10|1,6,E-10|
|AREA|SRC_710|Cam_Valpo_104-PTAS|272626|6385227|10 meses|2671,08|3,3,E-10|8,1,E-11|9,9,E-11|4,9,E-11|1,2,E-09|2,7,E-10|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 76. Fuentes de Emisión - Escenario 1 parte 20

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 186 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_711|Cam_Valpo_105-PTAS|272602|6386454|10 meses|4905,80|1,8,E-10|4,4,E-11|5,4,E-11|2,7,E-11|6,4,E-10|1,5,E-10|
|AREA|SRC_712|Cam_Valpo_106-PTAS|272609|6386527|10 meses|292,53|3,1,E-09|7,4,E-10|9,0,E-10|4,5,E-10|1,1,E-08|2,5,E-09|
|AREA|SRC_713|Cam_Valpo_107-PTAS|272650|6386615|10 meses|384,69|2,3,E-09|5,6,E-10|6,9,E-10|3,4,E-10|8,1,E-09|1,9,E-09|
|AREA|SRC_714|Cam_Valpo_108-PTAS|272755|6386705|10 meses|550,00|1,6,E-09|3,9,E-10|4,8,E-10|2,4,E-10|5,7,E-09|1,3,E-09|
|AREA|SRC_715|Cam_Valpo_109-PTAS|272846|6386776|10 meses|460,85|1,9,E-09|4,7,E-10|5,7,E-10|2,8,E-10|6,8,E-09|1,6,E-09|
|AREA|SRC_716|Cam_Valpo_110-PTAS|272918|6386821|10 meses|338,79|2,6,E-09|6,4,E-10|7,8,E-10|3,9,E-10|9,2,E-09|2,1,E-09|
|AREA|SRC_717|Cam_Valpo_111-PTAS|272959|6386856|10 meses|215,71|4,1,E-09|1,0,E-09|1,2,E-09|6,1,E-10|1,4,E-08|3,4,E-09|
|AREA|SRC_718|Cam_Valpo_112-PTAS|272979|6386909|10 meses|229,32|3,9,E-09|9,4,E-10|1,2,E-09|5,7,E-10|1,4,E-08|3,2,E-09|
|AREA|SRC_719|Cam_Valpo_113-PTAS|272982|6386950|10 meses|168,20|5,3,E-09|1,3,E-09|1,6,E-09|7,8,E-10|1,9,E-08|4,3,E-09|
|AREA|SRC_720|Cam_Valpo_114-PTAS|272974|6387033|10 meses|334,56|2,7,E-09|6,5,E-10|7,9,E-10|3,9,E-10|9,3,E-09|2,2,E-09|
|AREA|SRC_721|Cam_Valpo_115-PTAS|272969|6387289|10 meses|1021,26|8,7,E-10|2,1,E-10|2,6,E-10|1,3,E-10|3,1,E-09|7,1,E-10|
|AREA|SRC_722|Cam_Valpo_116-PTAS|272950|6387316|10 meses|135,86|6,6,E-09|1,6,E-09|1,9,E-09|9,6,E-10|2,3,E-08|5,3,E-09|
|AREA|SRC_723|Cam_Valpo_117-PTAS|272918|6387332|10 meses|150,62|5,9,E-09|1,4,E-09|1,8,E-09|8,7,E-10|2,1,E-08|4,8,E-09|
|AREA|SRC_724|Cam_Valpo_118-PTAS|272871|6387328|10 meses|193,11|4,6,E-09|1,1,E-09|1,4,E-09|6,8,E-10|1,6,E-08|3,8,E-09|
|AREA|SRC_725|Cam_Valpo_119-PTAS|272818|6387319|10 meses|214,82|4,2,E-09|1,0,E-09|1,2,E-09|6,1,E-10|1,5,E-08|3,4,E-09|
|AREA|SRC_726|Cam_Valpo_120-PTAS|272669|6387324|10 meses|593,51|1,5,E-09|3,6,E-10|4,5,E-10|2,2,E-10|5,3,E-09|1,2,E-09|
|AREA|SRC_727|Cam_Valpo_121-PTAS|272536|6387380|10 meses|574,11|1,6,E-09|3,8,E-10|4,6,E-10|2,3,E-10|5,4,E-09|1,3,E-09|
|AREA|SRC_728|Cam_Valpo_122-PTAS|272406|6387475|10 meses|642,85|1,4,E-09|3,4,E-10|4,1,E-10|2,0,E-10|4,9,E-09|1,1,E-09|
|AREA|SRC_729|Cam_Valpo_123-PTAS|272321|6387544|10 meses|438,86|2,0,E-09|4,9,E-10|6,0,E-10|3,0,E-10|7,1,E-09|1,7,E-09|
|AREA|SRC_730|Cam_Valpo_124-PTAS|272252|6387605|10 meses|366,01|2,4,E-09|5,9,E-10|7,2,E-10|3,6,E-10|8,5,E-09|2,0,E-09|
|AREA|SRC_731|Cam_Valpo_125-PTAS|272138|6387749|10 meses|733,97|1,2,E-09|2,9,E-10|3,6,E-10|1,8,E-10|4,3,E-09|9,9,E-10|
|AREA|SRC_732|Cam_Valpo_126-PTAS|272059|6387890|10 meses|645,70|1,4,E-09|3,3,E-10|4,1,E-10|2,0,E-10|4,8,E-09|1,1,E-09|
|AREA|SRC_733|Cam_Valpo_127-PTAS|272019|6388008|10 meses|494,29|1,8,E-09|4,4,E-10|5,4,E-10|2,6,E-10|6,3,E-09|1,5,E-09|
|AREA|SRC_734|Cam_Valpo_128-PTAS|272005|6388086|10 meses|318,17|2,8,E-09|6,8,E-10|8,3,E-10|4,1,E-10|9,8,E-09|2,3,E-09|
|AREA|SRC_735|Cam_Valpo_129-PTAS|272005|6388171|10 meses|338,40|2,6,E-09|6,4,E-10|7,8,E-10|3,9,E-10|9,2,E-09|2,1,E-09|
|AREA|SRC_736|Cam_Valpo_130-PTAS|272018|6388207|10 meses|149,40|6,0,E-09|1,4,E-09|1,8,E-09|8,8,E-10|2,1,E-08|4,9,E-09|
|AREA|SRC_737|Cam_Valpo_131-PTAS|272053|6388222|10 meses|144,57|6,2,E-09|1,5,E-09|1,8,E-09|9,1,E-10|2,2,E-08|5,0,E-09|
|AREA|SRC_738|Cam_Valpo_132-PTAS|272113|6388260|10 meses|286,19|3,1,E-09|7,5,E-10|9,2,E-10|4,6,E-10|1,1,E-08|2,5,E-09|
|AREA|SRC_739|Cam_Valpo_133-PTAS|272165|6388289|10 meses|236,50|3,8,E-09|9,1,E-10|1,1,E-09|5,5,E-10|1,3,E-08|3,1,E-09|
|AREA|SRC_740|Cam_Valpo_134-PTAS|272170|6388313|10 meses|103,04|8,7,E-09|2,1,E-09|2,6,E-09|1,3,E-09|3,0,E-08|7,0,E-09|
|AREA|SRC_741|Cam_Valpo_135-PTAS|272160|6388355|10 meses|178,67|5,0,E-09|1,2,E-09|1,5,E-09|7,3,E-10|1,7,E-08|4,1,E-09|
|AREA|SRC_742|Cam_Valpo_136-PTAS|272116|6388384|10 meses|213,17|4,2,E-09|1,0,E-09|1,2,E-09|6,1,E-10|1,5,E-08|3,4,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 77. Fuentes de Emisión - Escenario 1 parte 21

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 187 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_743|Cam_Valpo_137-PTAS|271990|6388473|10 meses|618,26|1,4,E-09|3,5,E-10|4,3,E-10|2,1,E-10|5,0,E-09|1,2,E-09|
|AREA|SRC_744|Cam_Valpo_138-PTAS|271909|6388570|10 meses|502,24|1,8,E-09|4,3,E-10|5,3,E-10|2,6,E-10|6,2,E-09|1,4,E-09|
|AREA|SRC_745|Cam_Valpo_139-PTAS|271887|6388631|10 meses|257,67|3,5,E-09|8,4,E-10|1,0,E-09|5,1,E-10|1,2,E-08|2,8,E-09|
|AREA|SRC_746|Cam_Valpo_140-PTAS|271869|6388710|10 meses|324,57|2,8,E-09|6,7,E-10|8,2,E-10|4,0,E-10|9,6,E-09|2,2,E-09|
|AREA|SRC_747|Cam_Valpo_141-PTAS|271879|6388778|10 meses|270,72|3,3,E-09|8,0,E-10|9,8,E-10|4,8,E-10|1,2,E-08|2,7,E-09|
|AREA|SRC_748|Cam_Valpo_142-PTAS|271889|6388831|10 meses|215,81|4,1,E-09|1,0,E-09|1,2,E-09|6,1,E-10|1,4,E-08|3,4,E-09|
|AREA|SRC_749|Cam_Valpo_143-PTAS|271888|6388910|10 meses|317,54|2,8,E-09|6,8,E-10|8,3,E-10|4,1,E-10|9,8,E-09|2,3,E-09|
|AREA|SRC_750|Cam_Valpo_144-PTAS|271765|6389249|10 meses|1443,83|6,2,E-10|1,5,E-10|1,8,E-10|9,1,E-11|2,2,E-09|5,0,E-10|
|AREA|SRC_751|Cam_Valpo_145-PTAS|271745|6389323|10 meses|308,68|2,9,E-09|7,0,E-10|8,6,E-10|4,2,E-10|1,0,E-08|2,4,E-09|
|AREA|SRC_752|Cam_Valpo_146-PTAS|271746|6389404|10 meses|321,13|2,8,E-09|6,7,E-10|8,2,E-10|4,1,E-10|9,7,E-09|2,3,E-09|
|AREA|SRC_753|Cam_Valpo_147-PTAS|271745|6389713|10 meses|1235,33|7,2,E-10|1,7,E-10|2,1,E-10|1,1,E-10|2,5,E-09|5,9,E-10|
|AREA|SRC_754|Cam_Valpo_148-PTAS|271729|6389779|10 meses|274,74|3,2,E-09|7,9,E-10|9,6,E-10|4,8,E-10|1,1,E-08|2,6,E-09|
|AREA|SRC_755|Cam_Valpo_149-PTAS|271405|6390771|10 meses|4169,69|2,1,E-10|5,2,E-11|6,3,E-11|3,1,E-11|7,5,E-10|1,7,E-10|
|AREA|SRC_756|Cam_Valpo_150-PTAS|271408|6390852|10 meses|324,07|2,8,E-09|6,7,E-10|8,2,E-10|4,0,E-10|9,6,E-09|2,2,E-09|
|AREA|SRC_757|Cam_Valpo_151-PTAS|271425|6390918|10 meses|269,76|3,3,E-09|8,0,E-10|9,8,E-10|4,9,E-10|1,2,E-08|2,7,E-09|
|AREA|SRC_758|Cam_Valpo_152-PTAS|271595|6391444|10 meses|2210,20|4,0,E-10|9,8,E-11|1,2,E-10|5,9,E-11|1,4,E-09|3,3,E-10|
|AREA|SRC_759|Cam_Valpo_153-PTAS|271601|6391518|10 meses|297,07|3,0,E-09|7,3,E-10|8,9,E-10|4,4,E-10|1,1,E-08|2,4,E-09|
|AREA|SRC_760|Cam_Valpo_154-PTAS|271583|6391599|10 meses|334,56|2,7,E-09|6,5,E-10|7,9,E-10|3,9,E-10|9,3,E-09|2,2,E-09|
|AREA|SRC_761|Cam_Valpo_155-PTAS|271490|6391665|10 meses|462,29|1,9,E-09|4,7,E-10|5,7,E-10|2,8,E-10|6,8,E-09|1,6,E-09|
|AREA|SRC_762|Cam_Valpo_156-PTAS|271388|6391779|10 meses|610,49|1,5,E-09|3,5,E-10|4,3,E-10|2,1,E-10|5,1,E-09|1,2,E-09|
|AREA|SRC_763|Cam_Valpo_157-PTAS|271303|6391969|10 meses|829,95|1,1,E-09|2,6,E-10|3,2,E-10|1,6,E-10|3,8,E-09|8,7,E-10|
|AREA|SRC_764|Cam_Valpo_158-PTAS|271249|6392048|10 meses|385,48|2,3,E-09|5,6,E-10|6,9,E-10|3,4,E-10|8,1,E-09|1,9,E-09|
|AREA|SRC_765|Cam_Valpo_159-PTAS|271095|6392199|10 meses|863,11|1,0,E-09|2,5,E-10|3,1,E-10|1,5,E-10|3,6,E-09|8,4,E-10|
|AREA|SRC_766|Cam_Valpo_160-PTAS|271003|6392357|10 meses|727,41|1,2,E-09|3,0,E-10|3,6,E-10|1,8,E-10|4,3,E-09|1,0,E-09|
|AREA|SRC_767|Cam_Valpo_161-PTAS|270864|6392618|10 meses|1181,67|7,6,E-10|1,8,E-10|2,2,E-10|1,1,E-10|2,6,E-09|6,1,E-10|
|AREA|SRC_768|Cam_Valpo_162-PTAS|270665|6392901|10 meses|1386,67|6,4,E-10|1,6,E-10|1,9,E-10|9,4,E-11|2,3,E-09|5,2,E-10|
|AREA|SRC_769|Cam_Valpo_163-PTAS|270570|6393060|10 meses|739,81|1,2,E-09|2,9,E-10|3,6,E-10|1,8,E-10|4,2,E-09|9,8,E-10|
|AREA|SRC_770|Cam_Valpo_164-PTAS|270535|6393162|10 meses|427,94|2,1,E-09|5,0,E-10|6,2,E-10|3,1,E-10|7,3,E-09|1,7,E-09|
|AREA|SRC_771|Cam_Valpo_165-PTAS|270408|6393157|10 meses|516,16|1,7,E-09|4,2,E-10|5,1,E-10|2,5,E-10|6,0,E-09|1,4,E-09|
|AREA|SRC_772|Cam_Valpo_166-PTAS|270322|6393156|10 meses|344,11|2,6,E-09|6,3,E-10|7,7,E-10|3,8,E-10|9,1,E-09|2,1,E-09|
|AREA|SRC_773|Cam_Valpo_167-PTAS|270198|6393225|10 meses|562,03|1,6,E-09|3,8,E-10|4,7,E-10|2,3,E-10|5,6,E-09|1,3,E-09|
|AREA|SRC_774|Cam_Valpo_168-PTAS|270084|6393222|10 meses|461,57|1,9,E-09|4,7,E-10|5,7,E-10|2,8,E-10|6,8,E-09|1,6,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 78. Fuentes de Emisión - Escenario 1 parte 22

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 188 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_775|Cam_Valpo_169-PTAS|270014|6393114|10 meses|520,05|1,7,E-09|4,2,E-10|5,1,E-10|2,5,E-10|6,0,E-09|1,4,E-09|
|AREA|SRC_776|Cam_Valpo_170-PTAS|269944|6393026|10 meses|448,19|2,0,E-09|4,8,E-10|5,9,E-10|2,9,E-10|7,0,E-09|1,6,E-09|
|AREA|SRC_777|Cam_Valpo_171-PTAS|269831|6392981|10 meses|484,35|1,8,E-09|4,5,E-10|5,5,E-10|2,7,E-10|6,4,E-09|1,5,E-09|
|AREA|SRC_778|Cam_Valpo_172-PTAS|269702|6392966|10 meses|516,99|1,7,E-09|4,2,E-10|5,1,E-10|2,5,E-10|6,0,E-09|1,4,E-09|
|AREA|SRC_779|Cam_Valpo_173-PTAS|269506|6393084|10 meses|906,73|9,8,E-10|2,4,E-10|2,9,E-10|1,4,E-10|3,4,E-09|8,0,E-10|
|AREA|SRC_780|Cam_Valpo_174-PTAS|269407|6393106|10 meses|410,62|2,2,E-09|5,3,E-10|6,4,E-10|3,2,E-10|7,6,E-09|1,8,E-09|
|AREA|SRC_781|Cam_Valpo_175-PTAS|269355|6393219|10 meses|493,13|1,8,E-09|4,4,E-10|5,4,E-10|2,7,E-10|6,3,E-09|1,5,E-09|
|AREA|SRC_782|Cam_Valpo_176-PTAS|269450|6393436|10 meses|939,57|9,5,E-10|2,3,E-10|2,8,E-10|1,4,E-10|3,3,E-09|7,7,E-10|
|AREA|SRC_783|Cam_Valpo_177-PTAS|269537|6393768|10 meses|1375,49|6,5,E-10|1,6,E-10|1,9,E-10|9,5,E-11|2,3,E-09|5,3,E-10|
|AREA|SRC_784|Cam_Valpo_178-PTAS|269541|6393876|10 meses|433,16|2,1,E-09|5,0,E-10|6,1,E-10|3,0,E-10|7,2,E-09|1,7,E-09|
|AREA|SRC_785|Cam_Valpo_179-PTAS|269514|6393952|10 meses|327,49|2,7,E-09|6,6,E-10|8,1,E-10|4,0,E-10|9,5,E-09|2,2,E-09|
|AREA|SRC_786|Cam_Valpo_180-PTAS|269461|6394006|10 meses|302,03|3,0,E-09|7,2,E-10|8,8,E-10|4,3,E-10|1,0,E-08|2,4,E-09|
|AREA|SRC_787|Cam_Valpo_181-PTAS|269456|6394087|10 meses|317,54|2,8,E-09|6,8,E-10|8,3,E-10|4,1,E-10|9,8,E-09|2,3,E-09|
|AREA|SRC_788|Cam_Valpo_182-PTAS|269494|6394169|10 meses|358,94|2,5,E-09|6,0,E-10|7,4,E-10|3,6,E-10|8,7,E-09|2,0,E-09|
|AREA|SRC_789|Cam_Valpo_183-PTAS|269580|6394296|10 meses|611,99|1,5,E-09|3,5,E-10|4,3,E-10|2,1,E-10|5,1,E-09|1,2,E-09|
|AREA|SRC_790|Cam_Valpo_184-PTAS|269614|6394394|10 meses|416,61|2,1,E-09|5,2,E-10|6,4,E-10|3,1,E-10|7,5,E-09|1,7,E-09|
|AREA|SRC_791|Cam_Valpo_185-PTAS|269617|6394492|10 meses|396,57|2,3,E-09|5,4,E-10|6,7,E-10|3,3,E-10|7,9,E-09|1,8,E-09|
|AREA|SRC_792|Cam_Valpo_186-PTAS|269532|6394634|10 meses|664,18|1,3,E-09|3,3,E-10|4,0,E-10|2,0,E-10|4,7,E-09|1,1,E-09|
|AREA|SRC_793|Cam_Valpo_187-PTAS|269478|6394752|10 meses|518,20|1,7,E-09|4,2,E-10|5,1,E-10|2,5,E-10|6,0,E-09|1,4,E-09|
|AREA|SRC_794|Cam_Valpo_188-PTAS|269437|6394881|10 meses|540,93|1,7,E-09|4,0,E-10|4,9,E-10|2,4,E-10|5,8,E-09|1,3,E-09|
|AREA|SRC_795|Cam_Valpo_189-PTAS|269448|6395002|10 meses|483,46|1,8,E-09|4,5,E-10|5,5,E-10|2,7,E-10|6,5,E-09|1,5,E-09|
|AREA|SRC_796|Cam_Valpo_190-PTAS|269465|6395049|10 meses|197,82|4,5,E-09|1,1,E-09|1,3,E-09|6,6,E-10|1,6,E-08|3,7,E-09|
|AREA|SRC_797|Cam_Valpo_191-PTAS|269701|6395188|10 meses|1088,66|8,2,E-10|2,0,E-10|2,4,E-10|1,2,E-10|2,9,E-09|6,7,E-10|
|AREA|SRC_798|Cam_Valpo_192-PTAS|269737|6395244|10 meses|269,38|3,3,E-09|8,0,E-10|9,8,E-10|4,9,E-10|1,2,E-08|2,7,E-09|
|AREA|SRC_799|Cam_Valpo_193-PTAS|269748|6395318|10 meses|301,88|3,0,E-09|7,2,E-10|8,8,E-10|4,3,E-10|1,0,E-08|2,4,E-09|
|AREA|SRC_800|Cam_Valpo_194-PTAS|269734|6395473|10 meses|624,02|1,4,E-09|3,5,E-10|4,2,E-10|2,1,E-10|5,0,E-09|1,2,E-09|
|AREA|SRC_801|Cam_Valpo_195-PTAS|269791|6395575|10 meses|462,91|1,9,E-09|4,7,E-10|5,7,E-10|2,8,E-10|6,7,E-09|1,6,E-09|
|AREA|SRC_802|Cam_Valpo_196-PTAS|269918|6395634|10 meses|557,57|1,6,E-09|3,9,E-10|4,7,E-10|2,3,E-10|5,6,E-09|1,3,E-09|
|AREA|SRC_803|Cam_Valpo_197-PTAS|269951|6395703|10 meses|311,66|2,9,E-09|6,9,E-10|8,5,E-10|4,2,E-10|1,0,E-08|2,3,E-09|
|AREA|SRC_804|Cam_Valpo_198-PTAS|269926|6395767|10 meses|277,87|3,2,E-09|7,8,E-10|9,5,E-10|4,7,E-10|1,1,E-08|2,6,E-09|
|AREA|SRC_805|Cam_Valpo_199-PTAS|269853|6395812|10 meses|348,28|2,6,E-09|6,2,E-10|7,6,E-10|3,8,E-10|9,0,E-09|2,1,E-09|
|AREA|SRC_806|Cam_Valpo_200-PTAS|269732|6395847|10 meses|504,67|1,8,E-09|4,3,E-10|5,2,E-10|2,6,E-10|6,2,E-09|1,4,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 79. Fuentes de Emisión - Escenario 1 parte 23

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 189 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_807|Cam_Valpo_201-PTAS|269688|6395928|10 meses|365,46|2,4,E-09|5,9,E-10|7,2,E-10|3,6,E-10|8,5,E-09|2,0,E-09|
|AREA|SRC_808|Cam_Valpo_202-PTAS|269717|6396047|10 meses|484,68|1,8,E-09|4,5,E-10|5,5,E-10|2,7,E-10|6,4,E-09|1,5,E-09|
|AREA|SRC_809|Cam_Valpo_203-PTAS|269712|6396106|10 meses|237,49|3,8,E-09|9,1,E-10|1,1,E-09|5,5,E-10|1,3,E-08|3,1,E-09|
|AREA|SRC_810|Cam_Valpo_204-PTAS|269657|6396143|10 meses|271,48|3,3,E-09|8,0,E-10|9,7,E-10|4,8,E-10|1,1,E-08|2,7,E-09|
|AREA|SRC_811|Cam_Valpo_205-PTAS|269580|6396120|10 meses|326,46|2,7,E-09|6,6,E-10|8,1,E-10|4,0,E-10|9,6,E-09|2,2,E-09|
|AREA|SRC_812|Cam_Valpo_206-PTAS|269501|6396070|10 meses|376,20|2,4,E-09|5,7,E-10|7,0,E-10|3,5,E-10|8,3,E-09|1,9,E-09|
|AREA|SRC_813|Cam_Valpo_207-PTAS|269359|6396026|10 meses|593,54|1,5,E-09|3,6,E-10|4,5,E-10|2,2,E-10|5,3,E-09|1,2,E-09|
|AREA|SRC_814|Cam_Valpo_208-PTAS|269272|6396023|10 meses|343,48|2,6,E-09|6,3,E-10|7,7,E-10|3,8,E-10|9,1,E-09|2,1,E-09|
|AREA|SRC_815|Cam_Valpo_209-PTAS|269222|6396073|10 meses|275,81|3,2,E-09|7,8,E-10|9,6,E-10|4,7,E-10|1,1,E-08|2,6,E-09|
|AREA|SRC_816|Cam_Valpo_210-PTAS|269210|6396185|10 meses|446,25|2,0,E-09|4,8,E-10|5,9,E-10|2,9,E-10|7,0,E-09|1,6,E-09|
|AREA|SRC_817|Cam_Valpo_211-PTAS|269167|6396232|10 meses|255,46|3,5,E-09|8,5,E-10|1,0,E-09|5,1,E-10|1,2,E-08|2,8,E-09|
|AREA|SRC_818|Cam_Valpo_212-PTAS|269082|6396226|10 meses|349,58|2,6,E-09|6,2,E-10|7,6,E-10|3,7,E-10|8,9,E-09|2,1,E-09|
|AREA|SRC_819|Cam_Valpo_213-PTAS|268998|6396240|10 meses|335,54|2,7,E-09|6,4,E-10|7,9,E-10|3,9,E-10|9,3,E-09|2,2,E-09|
|AREA|SRC_820|Cam_Valpo_214-PTAS|268894|6396300|10 meses|480,09|1,9,E-09|4,5,E-10|5,5,E-10|2,7,E-10|6,5,E-09|1,5,E-09|
|AREA|SRC_821|Cam_Valpo_215-PTAS|268805|6396381|10 meses|477,49|1,9,E-09|4,5,E-10|5,5,E-10|2,7,E-10|6,5,E-09|1,5,E-09|
|AREA|SRC_822|Cam_Valpo_216-PTAS|268734|6396481|10 meses|489,34|1,8,E-09|4,4,E-10|5,4,E-10|2,7,E-10|6,4,E-09|1,5,E-09|
|AREA|SRC_823|Cam_Valpo_217-PTAS|268692|6396569|10 meses|388,32|2,3,E-09|5,6,E-10|6,8,E-10|3,4,E-10|8,0,E-09|1,9,E-09|
|AREA|SRC_824|Cam_Valpo_218-PTAS|268614|6396686|10 meses|563,68|1,6,E-09|3,8,E-10|4,7,E-10|2,3,E-10|5,5,E-09|1,3,E-09|
|AREA|SRC_825|Cam_Valpo_219-PTAS|268551|6396751|10 meses|365,13|2,4,E-09|5,9,E-10|7,2,E-10|3,6,E-10|8,5,E-09|2,0,E-09|
|AREA|SRC_826|Cam_Valpo_220-PTAS|268525|6396834|10 meses|342,75|2,6,E-09|6,3,E-10|7,7,E-10|3,8,E-10|9,1,E-09|2,1,E-09|
|AREA|SRC_827|Cam_Valpo_221-PTAS|268521|6396918|10 meses|335,20|2,7,E-09|6,4,E-10|7,9,E-10|3,9,E-10|9,3,E-09|2,2,E-09|
|AREA|SRC_828|Cam_Valpo_222-PTAS|268510|6396996|10 meses|312,17|2,9,E-09|6,9,E-10|8,5,E-10|4,2,E-10|1,0,E-08|2,3,E-09|
|AREA|SRC_829|Cam_Valpo_223-PTAS|268441|6397095|10 meses|486,78|1,8,E-09|4,4,E-10|5,4,E-10|2,7,E-10|6,4,E-09|1,5,E-09|
|AREA|SRC_830|Cam_Valpo_224-PTAS|268352|6397195|10 meses|537,81|1,7,E-09|4,0,E-10|4,9,E-10|2,4,E-10|5,8,E-09|1,3,E-09|
|AREA|SRC_831|Cam_Valpo_225-PTAS|268295|6397296|10 meses|460,41|1,9,E-09|4,7,E-10|5,7,E-10|2,8,E-10|6,8,E-09|1,6,E-09|
|AREA|SRC_832|Cam_Valpo_226-PTAS|268265|6397370|10 meses|319,00|2,8,E-09|6,8,E-10|8,3,E-10|4,1,E-10|9,8,E-09|2,3,E-09|
|AREA|SRC_833|Cam_Valpo_227-PTAS|268236|6397470|10 meses|414,51|2,2,E-09|5,2,E-10|6,4,E-10|3,2,E-10|7,5,E-09|1,8,E-09|
|AREA|SRC_834|Cam_Valpo_228-PTAS|268225|6397539|10 meses|278,02|3,2,E-09|7,8,E-10|9,5,E-10|4,7,E-10|1,1,E-08|2,6,E-09|
|AREA|SRC_835|Cam_Valpo_229-PTAS|268212|6397650|10 meses|446,47|2,0,E-09|4,8,E-10|5,9,E-10|2,9,E-10|7,0,E-09|1,6,E-09|
|AREA|SRC_836|Cam_Valpo_230-PTAS|268292|6397691|10 meses|352,90|2,5,E-09|6,1,E-10|7,5,E-10|3,7,E-10|8,8,E-09|2,1,E-09|
|AREA|SRC_837|Cam_Valpo_231-PTAS|268324|6397741|10 meses|244,09|3,7,E-09|8,8,E-10|1,1,E-09|5,4,E-10|1,3,E-08|3,0,E-09|
|AREA|SRC_838|Cam_Valpo_232-PTAS|268344|6397809|10 meses|284,52|3,1,E-09|7,6,E-10|9,3,E-10|4,6,E-10|1,1,E-08|2,6,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 80. Fuentes de Emisión - Escenario 1 parte 24

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 190 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_839|Cam_Valpo_233-PTAS|268317|6397871|10 meses|277,40|3,2,E-09|7,8,E-10|9,5,E-10|4,7,E-10|1,1,E-08|2,6,E-09|
|AREA|SRC_840|Cam_Valpo_234-PTAS|268289|6397931|10 meses|263,44|3,4,E-09|8,2,E-10|1,0,E-09|5,0,E-10|1,2,E-08|2,8,E-09|
|AREA|SRC_841|Cam_Valpo_235-PTAS|268281|6397993|10 meses|246,21|3,6,E-09|8,8,E-10|1,1,E-09|5,3,E-10|1,3,E-08|2,9,E-09|
|AREA|SRC_842|Cam_Valpo_236-PTAS|268325|6398057|10 meses|307,11|2,9,E-09|7,0,E-10|8,6,E-10|4,3,E-10|1,0,E-08|2,4,E-09|
|AREA|SRC_843|Cam_Valpo_237-PTAS|268339|6398092|10 meses|154,12|5,8,E-09|1,4,E-09|1,7,E-09|8,5,E-10|2,0,E-08|4,7,E-09|
|AREA|SRC_844|Cam_Valpo_238-PTAS|268362|6398151|10 meses|251,56|3,5,E-09|8,6,E-10|1,1,E-09|5,2,E-10|1,2,E-08|2,9,E-09|
|AREA|SRC_845|Cam_Valpo_239-PTAS|268383|6398192|10 meses|185,19|4,8,E-09|1,2,E-09|1,4,E-09|7,1,E-10|1,7,E-08|3,9,E-09|
|AREA|SRC_846|Cam_Valpo_240-PTAS|268355|6398247|10 meses|250,18|3,6,E-09|8,6,E-10|1,1,E-09|5,2,E-10|1,2,E-08|2,9,E-09|
|AREA|SRC_847|Cam_Valpo_241-PTAS|268227|6398303|10 meses|566,84|1,6,E-09|3,8,E-10|4,7,E-10|2,3,E-10|5,5,E-09|1,3,E-09|
|AREA|SRC_848|Cam_Valpo_242-PTAS|268140|6398362|10 meses|418,83|2,1,E-09|5,2,E-10|6,3,E-10|3,1,E-10|7,5,E-09|1,7,E-09|
|AREA|SRC_849|Cam_Valpo_243-PTAS|268089|6398427|10 meses|325,43|2,7,E-09|6,6,E-10|8,1,E-10|4,0,E-10|9,6,E-09|2,2,E-09|
|AREA|SRC_850|Cam_Valpo_244-PTAS|268005|6398483|10 meses|406,15|2,2,E-09|5,3,E-10|6,5,E-10|3,2,E-10|7,7,E-09|1,8,E-09|
|AREA|SRC_851|Cam_Valpo_245-PTAS|267956|6398553|10 meses|338,26|2,6,E-09|6,4,E-10|7,8,E-10|3,9,E-10|9,2,E-09|2,1,E-09|
|AREA|SRC_852|Cam_Valpo_246-PTAS|267920|6398673|10 meses|498,96|1,8,E-09|4,3,E-10|5,3,E-10|2,6,E-10|6,3,E-09|1,5,E-09|
|AREA|SRC_853|Cam_Valpo_247-PTAS|267908|6398749|10 meses|308,37|2,9,E-09|7,0,E-10|8,6,E-10|4,2,E-10|1,0,E-08|2,4,E-09|
|AREA|SRC_854|Cam_Valpo_248-PTAS|267894|6398771|10 meses|107,41|8,3,E-09|2,0,E-09|2,5,E-09|1,2,E-09|2,9,E-08|6,8,E-09|
|AREA|SRC_855|Cam_Valpo_249-PTAS|267791|6398823|10 meses|466,56|1,9,E-09|4,6,E-10|5,7,E-10|2,8,E-10|6,7,E-09|1,6,E-09|
|AREA|SRC_856|Cam_Valpo_250-PTAS|267747|6398849|10 meses|204,00|4,4,E-09|1,1,E-09|1,3,E-09|6,4,E-10|1,5,E-08|3,6,E-09|
|AREA|SRC_857|Cam_Valpo_251-PTAS|267699|6398875|10 meses|217,15|4,1,E-09|9,9,E-10|1,2,E-09|6,0,E-10|1,4,E-08|3,3,E-09|
|AREA|SRC_858|Cam_Valpo_252-PTAS|267673|6398943|10 meses|285,91|3,1,E-09|7,6,E-10|9,3,E-10|4,6,E-10|1,1,E-08|2,5,E-09|
|AREA|SRC_859|Cam_Valpo_253-PTAS|267740|6399152|10 meses|871,99|1,0,E-09|2,5,E-10|3,0,E-10|1,5,E-10|3,6,E-09|8,3,E-10|
|AREA|SRC_860|Cam_Valpo_254-PTAS|267754|6399259|10 meses|434,37|2,1,E-09|5,0,E-10|6,1,E-10|3,0,E-10|7,2,E-09|1,7,E-09|
|AREA|SRC_861|Cam_Valpo_255-PTAS|267756|6399372|10 meses|452,93|2,0,E-09|4,8,E-10|5,8,E-10|2,9,E-10|6,9,E-09|1,6,E-09|
|AREA|SRC_862|Cam_Valpo_256-PTAS|267702|6399478|10 meses|480,03|1,9,E-09|4,5,E-10|5,5,E-10|2,7,E-10|6,5,E-09|1,5,E-09|
|AREA|SRC_863|Cam_Valpo_257-PTAS|267740|6399547|10 meses|307,21|2,9,E-09|7,0,E-10|8,6,E-10|4,3,E-10|1,0,E-08|2,4,E-09|
|AREA|SRC_864|Cam_Valpo_258-PTAS|267742|6399624|10 meses|311,56|2,9,E-09|6,9,E-10|8,5,E-10|4,2,E-10|1,0,E-08|2,3,E-09|
|AREA|SRC_865|Cam_Valpo_259-PTAS|267731|6399695|10 meses|287,58|3,1,E-09|7,5,E-10|9,2,E-10|4,6,E-10|1,1,E-08|2,5,E-09|
|AREA|SRC_866|Cam_Valpo_260-PTAS|267682|6399788|10 meses|425,70|2,1,E-09|5,1,E-10|6,2,E-10|3,1,E-10|7,3,E-09|1,7,E-09|
|AREA|SRC_867|Cam_Valpo_261-PTAS|267661|6399830|10 meses|187,04|4,8,E-09|1,2,E-09|1,4,E-09|7,0,E-10|1,7,E-08|3,9,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 81. Fuentes de Emisión - Escenario 1 parte 25

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 191 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/s]|[g/s]|[g/s]|[g/s]|[g/s]|[g/s]|
|VOLUMEN|SRC_104|Peas_1|270864|6384350|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_105|Peas_2|271314|6385054|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_106|Peas_3|272646|6386734|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_107|Peas_5.1|271759|6385541|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_108|Peas_5.2|272604|6384126|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_109|Colec_1.1|270896|6383952|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_110|Colec_1.2|270878|6384054|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_111|Colec_1.3|270875|6384153|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_112|Colec_1.4|270875|6384255|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_113|Col_1_2.1|270933|6384852|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_114|Col_1_2.2|271018|6384944|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_115|Col_1_2.3|271108|6384992|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_116|Col_1_2.4|271205|6385003|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_117|Colec_2.1|271536|6385456|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_118|Colec_2.2|271642|6385470|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_119|Colec_2.3|271736|6385514|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_120|Colec_5.1.1|271800|6385553|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_121|Colec_5.1.2|271862|6385635|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_122|Colec_5.1.3|271917|6385717|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_123|Colec_5.1.4|271975|6385800|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_124|Colec_5.1.5|272034|6385884|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_125|Colec_5.1.6|272065|6385985|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_126|Colec_5.1.7|272073|6386084|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_127|Colec_5.1.8|272082|6386182|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_128|Colec_5.1.9|272094|6386285|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_129|Colec_5.1.10|272103|6386383|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_130|Colec_5.1.11|272114|6386486|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_131|Colec_5.1.12|272124|6386586|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_132|Colec_5.1.13|272134|6386685|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_133|Colec_5.1.14|272173|6386769|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_134|Colec_5.1.15|272227|6386790|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_135|Imp_1.1|270871|6384375|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 82. Fuentes de Emisión - Escenario 1 parte 26

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 192 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/s]|[g/s]|[g/s]|[g/s]|[g/s]|[g/s]|
|VOLUMEN|SRC_136|Imp_1.2|270885|6384474|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_137|Imp_1.3|270917|6384569|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_138|Imp_1.4|270909|6384664|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_139|Imp_1.5|270865|6384743|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_140|Imp_2.1|271312|6385052|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_141|Imp_2.2|271351|6385139|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_142|Imp_2.3|271381|6385237|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_143|Imp_2.4|271427|6385315|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_144|Imp_2.5|271475|6385364|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_145|Imp_3.1|272364|6386744|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_146|Imp_3.2|272480|6386685|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_147|Imp_3.3|272648|6386703|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_148|Imp_5.1.1|271783|6385539|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_149|Imp_5.1.2|271878|6385513|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_150|Imp_5.1.3|271848|6385424|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_151|Imp_5.1.4|271860|6385341|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_152|Imp_5.1.5|271956|6385330|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_153|Imp_5.1.6|272058|6385331|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_154|Imp_5.1.7|272158|6385331|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_155|Imp_5.1.8|272222|6385338|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_156|Imp_5.1.9|272313|6385346|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_157|Imp_5.1.10|272287|6385238|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_158|Imp_5.1.11|272306|6385136|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_159|Imp_5.1.12|272338|6385040|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_160|Imp_5.1.13|272409|6384843|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_161|Imp_5.1.14|272374|6384939|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_162|Imp_5.1.15|272452|6384740|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_163|Imp_5.1.16|272490|6384643|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_164|Imp_5.1.17|272526|6384544|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_165|Imp_5.1.18|272557|6384457|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_166|Imp_5.1.19|272601|6384362|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_167|Imp_5.1.20|272632|6384267|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 83. Fuentes de Emisión - Escenario 1 parte 27

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 193 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/s]|[g/s]|[g/s]|[g/s]|[g/s]|[g/s]|
|VOLUMEN|SRC_168|Imp_5.2.1|272634|6384032|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_169|Imp_5.2.2|272631|6383934|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_170|Imp_5.2.3|272632|6383831|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_171|Imp_5.2.4|272632|6383729|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_172|Imp_5.2.5|272642|6383643|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_173|Imp_5.2.6|272748|6383641|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_174|Imp_5.2.7|272853|6383634|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_175|Imp_5.2.8|272944|6383635|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_176|Imp_5.2.9|273065|6383635|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_177|Imp_5.2.10|273176|6383645|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_178|Imp_5.2.11|273243|6383543|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_179|Imp_5.2.12|273291|6383445|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_180|Imp_5.2.13|273367|6383372|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_181|Imp_5.2.14|273437|6383289|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_182|Imp_5.2.15|273519|6383235|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_183|Imp_5.2.16|273552|6383133|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_184|IF_1_Redes|272319|6384980|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_185|IF_2_PTAS|273522|6383276|10 meses|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_186|Tub_1.1|272635|6383635|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_187|Tub_1.2|272637|6383541|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_188|Tub_1.3|272527|6383557|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_189|Tub_1.4|272460|6383632|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_190|Tub_1.5|272380|6383685|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_191|Tub_1.6|272302|6383737|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_192|Tub_1.7|272199|6383724|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_193|Tub_1.8|272124|6383757|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_194|Tub_1.9|272062|6383846|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_195|Tub_1.10|271963|6383848|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_196|Tub_1.11|271864|6383796|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_197|Tub_1.12|271768|6383747|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_198|Tub_1.13|271671|6383722|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_199|Tub_1.14|271566|6383690|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 84. Fuentes de Emisión - Escenario 1 parte 28

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 194 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|MPS|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/s]|[g/s]|[g/s]|[g/s]|[g/s]|[g/s]|
|VOLUMEN|SRC_200|Tub_1.15|271503|6383603|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_201|Tub_1.16|271426|6383526|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_202|Tub_1.17|271371|6383438|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_203|Tub_1.18|271342|6383355|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_204|Tub_1.19|271276|6383288|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_205|Tub_1.20|271250|6383195|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_206|Tub_1.21|271207|6383098|1 mes|4,00|3,33,E-04|5,05,E-05|0,000527|0,00,E+00|0,00,E+00|0,00,E+00|
|PUNTUAL|SRC_207|IF_1_Redes|272319|6384980|10 meses|0,05|7,32,E-03|1,77,E-03|0,000000|0,00,E+00|2,08,E-01|4,49,E-02|
|PUNTUAL|SRC_208|IF_2_PTAS|273522|6383276|10 meses|0,05|7,32,E-03|1,77,E-03|0,000000|0,00,E+00|2,08,E-01|4,49,E-02|
|VOLUMEN|SRC_538|PTAS|273588|6383221|10 meses|4,00|3,04,E-03|4,60,E-04|0,004803|0,00,E+00|0,00,E+00|0,00,E+00|
|PUNTUAL|SRC_539|PTAS|273588|6383221|10 meses|0,05|2,00,E-03|4,82,E-04|0,000000|0,00,E+00|5,68,E-02|1,23,E-02|

**17.2 FUENTES DE EMISIÓN - ESCENARIO 2**

Tabla 85. Fuentes de Emisión - Escenario 2 parte 1

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_1|Peas_6|271066|6383088|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_2|Peas_7|273477|6387272|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_3|Peas_8|273248|6387021|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_4|Imp_6|271081|6383206|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_5|Imp_6.1|271071|6383155|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_6|Imp_7.1|273429|6387230|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_7|Imp_7.2|273335|6387133|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_8|Imp_8.1|273085|6386931|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_9|Imp_8.2|272998|6386876|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_10|colec_6.1|270895|6383951|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_11|colec_6.2|270931|6383854|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_12|colec_6.3|270972|6383762|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_13|colec_6.4|271000|6383665|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_14|colec_6.5|271028|6383558|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 84. Fuentes de Emisión - Escenario 1 parte 28

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 195 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_15|colec_6.6|271047|6383446|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_16|colec_6.7|271063|6383340|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_17|colec_6.8|271072|6383259|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_18|colec_6.9|271097|6383128|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_19|colec_6.10|271119|6383027|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_20|colec_6.11|271134|6382922|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_21|colec_6.12|271145|6382826|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_22|colec_6.13|271162|6382779|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_23|Colec_8.1|272914|6386818|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_24|Colec_8.2|272830|6386759|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_25|Colec_8.3|272777|6386719|1 mes|4,00|2,40,E-03|1,20,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_53|Cam_Cat_1-PEAS e Imp|273043|6387323|1 mes|383,32|3,99,E-08|9,64,E-09|4,37,E-09|5,48,E-08|1,30,E-08|
|AREA|SRC_54|Cam_Cat_2-PEAS e Imp|273206|6387558|1 mes|1145,03|1,33,E-08|3,23,E-09|1,46,E-09|1,83,E-08|4,37,E-09|
|AREA|SRC_55|Cam_Cat_3-PEAS e Imp|273308|6387612|1 mes|456,00|3,35,E-08|8,11,E-09|3,67,E-09|4,61,E-08|1,10,E-08|
|AREA|SRC_56|Cam_Cat_4-PEAS e Imp|273511|6387668|1 mes|843,57|1,81,E-08|4,38,E-09|1,98,E-09|2,49,E-08|5,93,E-09|
|AREA|SRC_57|Cam_Cat_5-PEAS e Imp|273721|6387707|1 mes|853,32|1,79,E-08|4,33,E-09|1,96,E-09|2,46,E-08|5,86,E-09|
|AREA|SRC_58|Cam_Cat_6-PEAS e Imp|273880|6387880|1 mes|945,26|1,62,E-08|3,91,E-09|1,77,E-09|2,22,E-08|5,29,E-09|
|AREA|SRC_59|Cam_Cat_7-PEAS e Imp|273982|6387934|1 mes|457,52|3,34,E-08|8,08,E-09|3,66,E-09|4,59,E-08|1,09,E-08|
|AREA|SRC_60|Cam_Cat_8-PEAS e Imp|274178|6387916|1 mes|782,20|1,95,E-08|4,73,E-09|2,14,E-09|2,69,E-08|6,39,E-09|
|AREA|SRC_61|Cam_Cat_9-PEAS e Imp|274216|6387945|1 mes|195,48|7,82,E-08|1,89,E-08|8,56,E-09|1,07,E-07|2,56,E-08|
|AREA|SRC_62|Cam_Cat_10-PEAS e Imp|274213|6388017|1 mes|295,61|5,17,E-08|1,25,E-08|5,66,E-09|7,11,E-08|1,69,E-08|
|AREA|SRC_63|Cam_Cat_11-PEAS e Imp|274177|6388250|1 mes|941,53|1,62,E-08|3,93,E-09|1,78,E-09|2,23,E-08|5,31,E-09|
|AREA|SRC_64|Cam_Cat_12-PEAS e Imp|274185|6388365|1 mes|458,34|3,33,E-08|8,06,E-09|3,65,E-09|4,58,E-08|1,09,E-08|
|AREA|SRC_65|Cam_Cat_13-PEAS e Imp|274352|6388558|1 mes|1016,92|1,50,E-08|3,63,E-09|1,65,E-09|2,07,E-08|4,92,E-09|
|AREA|SRC_66|Cam_Cat_14-PEAS e Imp|274654|6388846|1 mes|1667,00|9,16,E-09|2,22,E-09|1,00,E-09|1,26,E-08|3,00,E-09|
|AREA|SRC_67|Cam_Cat_15-PEAS e Imp|274745|6388895|1 mes|409,81|3,73,E-08|9,02,E-09|4,08,E-09|5,13,E-08|1,22,E-08|
|AREA|SRC_68|Cam_Cat_16-PEAS e Imp|274834|6388862|1 mes|371,12|4,12,E-08|9,96,E-09|4,51,E-09|5,66,E-08|1,35,E-08|
|AREA|SRC_69|Cam_Cat_17-PEAS e Imp|274882|6388794|1 mes|331,29|4,61,E-08|1,12,E-08|5,05,E-09|6,34,E-08|1,51,E-08|
|AREA|SRC_70|Cam_Cat_18-PEAS e Imp|274979|6388768|1 mes|406,63|3,76,E-08|9,09,E-09|4,12,E-09|5,17,E-08|1,23,E-08|
|AREA|SRC_71|Cam_Cat_19-PEAS e Imp|275069|6388799|1 mes|384,16|3,98,E-08|9,62,E-09|4,36,E-09|5,47,E-08|1,30,E-08|
|AREA|SRC_72|Cam_Cat_20-PEAS e Imp|275059|6388911|1 mes|459,52|3,32,E-08|8,04,E-09|3,64,E-09|4,57,E-08|1,09,E-08|
|AREA|SRC_73|Cam_Cat_21-PEAS e Imp|275040|6389003|1 mes|374,05|4,08,E-08|9,88,E-09|4,48,E-09|5,62,E-08|1,34,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 84. Fuentes de Emisión - Escenario 1 parte 28

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 196 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_74|Cam_Cat_22-PEAS e Imp|274958|6389092|1 mes|489,11|3,12,E-08|7,56,E-09|3,42,E-09|4,29,E-08|1,02,E-08|
|AREA|SRC_75|Cam_Cat_23-PEAS e Imp|274915|6389184|1 mes|402,20|3,80,E-08|9,19,E-09|4,16,E-09|5,22,E-08|1,24,E-08|
|AREA|SRC_76|Cam_Cat_24-PEAS e Imp|274946|6389307|1 mes|502,79|3,04,E-08|7,35,E-09|3,33,E-09|4,18,E-08|9,94,E-09|
|AREA|SRC_77|Cam_Cat_25-PEAS e Imp|275049|6389374|1 mes|485,06|3,15,E-08|7,62,E-09|3,45,E-09|4,33,E-08|1,03,E-08|
|AREA|SRC_78|Cam_Cat_26-PEAS e Imp|275181|6389406|1 mes|541,36|2,82,E-08|6,83,E-09|3,09,E-09|3,88,E-08|9,24,E-09|
|AREA|SRC_79|Cam_Cat_27-PEAS e Imp|275286|6389385|1 mes|424,34|3,60,E-08|8,71,E-09|3,94,E-09|4,95,E-08|1,18,E-08|
|AREA|SRC_80|Cam_Cat_28-PEAS e Imp|275372|6389387|1 mes|345,06|4,43,E-08|1,07,E-08|4,85,E-09|6,09,E-08|1,45,E-08|
|AREA|SRC_81|Cam_Cat_29-PEAS e Imp|275519|6389442|1 mes|633,26|2,41,E-08|5,84,E-09|2,64,E-09|3,32,E-08|7,90,E-09|
|AREA|SRC_82|Cam_Cat_30-PEAS e Imp|275575|6389512|1 mes|360,36|4,24,E-08|1,03,E-08|4,65,E-09|5,83,E-08|1,39,E-08|
|AREA|SRC_83|Cam_Cat_31-PEAS e Imp|275579|6389623|1 mes|447,31|3,42,E-08|8,26,E-09|3,74,E-09|4,70,E-08|1,12,E-08|
|AREA|SRC_84|Cam_Cat_32-PEAS e Imp|275473|6389738|1 mes|629,59|2,43,E-08|5,87,E-09|2,66,E-09|3,34,E-08|7,94,E-09|
|AREA|SRC_85|Cam_Cat_33-PEAS e Imp|275397|6389809|1 mes|419,18|3,64,E-08|8,82,E-09|3,99,E-09|5,01,E-08|1,19,E-08|
|AREA|SRC_86|Cam_Cat_34-PEAS e Imp|275382|6389918|1 mes|432,78|3,53,E-08|8,54,E-09|3,87,E-09|4,85,E-08|1,16,E-08|
|AREA|SRC_87|Cam_Cat_35-PEAS e Imp|275487|6390018|1 mes|576,65|2,65,E-08|6,41,E-09|2,90,E-09|3,64,E-08|8,67,E-09|
|AREA|SRC_88|Cam_Cat_36-PEAS e Imp|275630|6390045|1 mes|576,34|2,65,E-08|6,41,E-09|2,90,E-09|3,64,E-08|8,67,E-09|
|AREA|SRC_89|Cam_Cat_37-PEAS e Imp|275763|6390025|1 mes|532,94|2,87,E-08|6,94,E-09|3,14,E-09|3,94,E-08|9,38,E-09|
|AREA|SRC_90|Cam_Cat_38-PEAS e Imp|275861|6389993|1 mes|411,71|3,71,E-08|8,98,E-09|4,07,E-09|5,10,E-08|1,21,E-08|
|AREA|SRC_91|Cam_Cat_39-PEAS e Imp|276044|6389963|1 mes|742,87|2,06,E-08|4,98,E-09|2,25,E-09|2,83,E-08|6,73,E-09|
|AREA|SRC_92|Cam_Cat_40-PEAS e Imp|276114|6389925|1 mes|316,96|4,82,E-08|1,17,E-08|5,28,E-09|6,63,E-08|1,58,E-08|
|AREA|SRC_93|Cam_Cat_41-PEAS e Imp|276133|6389885|1 mes|172,93|8,83,E-08|2,14,E-08|9,68,E-09|1,21,E-07|2,89,E-08|
|AREA|SRC_94|Cam_Cat_42-PEAS e Imp|276158|6389818|1 mes|286,84|5,33,E-08|1,29,E-08|5,84,E-09|7,32,E-08|1,74,E-08|
|AREA|SRC_95|Cam_Cat_43-PEAS e Imp|276157|6389659|1 mes|632,84|2,41,E-08|5,84,E-09|2,65,E-09|3,32,E-08|7,90,E-09|
|AREA|SRC_96|Cam_Cat_44-PEAS e Imp|276172|6389529|1 mes|521,10|2,93,E-08|7,09,E-09|3,21,E-09|4,03,E-08|9,59,E-09|
|AREA|SRC_97|Cam_Cat_45-PEAS e Imp|276275|6389477|1 mes|468,32|3,26,E-08|7,89,E-09|3,57,E-09|4,49,E-08|1,07,E-08|
|AREA|SRC_98|Cam_Cat_46-PEAS e Imp|276411|6389458|1 mes|553,37|2,76,E-08|6,68,E-09|3,03,E-09|3,80,E-08|9,03,E-09|
|AREA|SRC_99|Cam_Cat_47-PEAS e Imp|276501|6389471|1 mes|366,24|4,17,E-08|1,01,E-08|4,57,E-09|5,74,E-08|1,37,E-08|
|AREA|SRC_100|Cam_Cat_48-PEAS e Imp|276706|6389673|1 mes|1151,46|1,33,E-08|3,21,E-09|1,45,E-09|1,82,E-08|4,34,E-09|
|AREA|SRC_101|Cam_Cat_49-PEAS e Imp|277353|6390498|1 mes|4195,41|3,64,E-09|8,81,E-10|3,99,E-10|5,01,E-09|1,19,E-09|
|AREA|SRC_102|Cam_Cat_50-PEAS e Imp|277494|6390575|1 mes|640,03|2,39,E-08|5,77,E-09|2,62,E-09|3,28,E-08|7,81,E-09|
|AREA|SRC_103|Cam_Cat_51-PEAS e Imp|279440|6391244|1 mes|8223,68|1,86,E-09|4,49,E-10|2,04,E-10|2,55,E-09|6,08,E-10|
|AREA|SRC_104|Cam_Cat_52-PEAS e Imp|283346|6393239|1 mes|17540,88|8,71,E-10|2,11,E-10|9,54,E-11|1,20,E-09|2,85,E-10|
|AREA|SRC_105|Cam_Cat_53-PEAS e Imp|287745|6394661|1 mes|18483,13|8,27,E-10|2,00,E-10|9,06,E-11|1,14,E-09|2,71,E-10|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 84. Fuentes de Emisión - Escenario 1 parte 28

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 197 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_106|Cam_Pta_1-PEAS e Imp|273147|6383634|1 mes|1866,42|8,19,E-09|1,98,E-09|8,97,E-10|1,13,E-08|2,68,E-09|
|AREA|SRC_107|Cam_Pta_2-PEAS e Imp|273165|6383642|1 mes|80,85|1,89,E-07|4,57,E-08|2,07,E-08|2,60,E-07|6,18,E-08|
|AREA|SRC_108|Cam_Pta_3-PEAS e Imp|273189|6383637|1 mes|94,14|1,62,E-07|3,93,E-08|1,78,E-08|2,23,E-07|5,31,E-08|
|AREA|SRC_109|Cam_Pta_4-PEAS e Imp|273241|6383562|1 mes|359,95|4,24,E-08|1,03,E-08|4,65,E-09|5,84,E-08|1,39,E-08|
|AREA|SRC_110|Cam_Pta_5-PEAS e Imp|273289|6383445|1 mes|505,57|3,02,E-08|7,31,E-09|3,31,E-09|4,15,E-08|9,89,E-09|
|AREA|SRC_111|Cam_Pta_6-PEAS e Imp|273304|6383402|1 mes|179,62|8,51,E-08|2,06,E-08|9,32,E-09|1,17,E-07|2,78,E-08|
|AREA|SRC_112|Cam_Pta_7-PEAS e Imp|273331|6383382|1 mes|138,45|1,10,E-07|2,67,E-08|1,21,E-08|1,52,E-07|3,61,E-08|
|AREA|SRC_113|Cam_Pta_8-PEAS e Imp|273361|6383362|1 mes|145,56|1,05,E-07|2,54,E-08|1,15,E-08|1,44,E-07|3,43,E-08|
|AREA|SRC_114|Cam_Pta_9-PEAS e Imp|273393|6383346|1 mes|143,99|1,06,E-07|2,57,E-08|1,16,E-08|1,46,E-07|3,47,E-08|
|AREA|SRC_115|Cam_Pta_10-PEAS e Imp|273413|6383324|1 mes|116,32|1,31,E-07|3,18,E-08|1,44,E-08|1,81,E-07|4,30,E-08|
|AREA|SRC_116|Cam_Pta_11-PEAS e Imp|273447|6383229|1 mes|400,03|3,82,E-08|9,24,E-09|4,18,E-09|5,25,E-08|1,25,E-08|
|AREA|SRC_117|Cam_Pta_12-PEAS e Imp|273463|6383220|1 mes|80,13|1,91,E-07|4,61,E-08|2,09,E-08|2,62,E-07|6,24,E-08|
|AREA|SRC_118|Cam_Pta_13-PEAS e Imp|273473|6383218|1 mes|45,12|3,39,E-07|8,19,E-08|3,71,E-08|4,66,E-07|1,11,E-07|
|AREA|SRC_119|Cam_Pta_14-PEAS e Imp|273519|6383228|1 mes|188,53|8,10,E-08|1,96,E-08|8,88,E-09|1,11,E-07|2,65,E-08|
|AREA|SRC_120|Cam_Valpo_1-PEAS e Imp|267407|6370003|1 mes|9181,86|1,66,E-09|4,03,E-10|1,82,E-10|2,29,E-09|5,45,E-10|
|AREA|SRC_121|Cam_Valpo_2-PEAS e Imp|267402|6370088|1 mes|338,29|4,52,E-08|1,09,E-08|4,95,E-09|6,21,E-08|1,48,E-08|
|AREA|SRC_122|Cam_Valpo_3-PEAS e Imp|267699|6371506|1 mes|5788,94|2,64,E-09|6,38,E-10|2,89,E-10|3,63,E-09|8,64,E-10|
|AREA|SRC_123|Cam_Valpo_4-PEAS e Imp|267700|6371619|1 mes|452,00|3,38,E-08|8,18,E-09|3,70,E-09|4,65,E-08|1,11,E-08|
|AREA|SRC_124|Cam_Valpo_5-PEAS e Imp|267517|6371917|1 mes|1401,44|1,09,E-08|2,64,E-09|1,19,E-09|1,50,E-08|3,57,E-09|
|AREA|SRC_125|Cam_Valpo_6-PEAS e Imp|267499|6371980|1 mes|261,10|5,85,E-08|1,42,E-08|6,41,E-09|8,05,E-08|1,91,E-08|
|AREA|SRC_126|Cam_Valpo_7-PEAS e Imp|267496|6372042|1 mes|247,03|6,18,E-08|1,50,E-08|6,78,E-09|8,50,E-08|2,02,E-08|
|AREA|SRC_127|Cam_Valpo_8-PEAS e Imp|267518|6372113|1 mes|294,47|5,19,E-08|1,26,E-08|5,68,E-09|7,13,E-08|1,70,E-08|
|AREA|SRC_128|Cam_Valpo_9-PEAS e Imp|267547|6372151|1 mes|187,43|8,15,E-08|1,97,E-08|8,93,E-09|1,12,E-07|2,67,E-08|
|AREA|SRC_129|Cam_Valpo_10-PEAS e Imp|267569|6372177|1 mes|137,02|1,12,E-07|2,70,E-08|1,22,E-08|1,53,E-07|3,65,E-08|
|AREA|SRC_130|Cam_Valpo_11-PEAS e Imp|267738|6372319|1 mes|879,83|1,74,E-08|4,20,E-09|1,90,E-09|2,39,E-08|5,68,E-09|
|AREA|SRC_131|Cam_Valpo_12-PEAS e Imp|267762|6372358|1 mes|186,57|8,19,E-08|1,98,E-08|8,97,E-09|1,13,E-07|2,68,E-08|
|AREA|SRC_132|Cam_Valpo_13-PEAS e Imp|267783|6372410|1 mes|224,51|6,80,E-08|1,65,E-08|7,46,E-09|9,36,E-08|2,23,E-08|
|AREA|SRC_133|Cam_Valpo_14-PEAS e Imp|267855|6372669|1 mes|1075,61|1,42,E-08|3,44,E-09|1,56,E-09|1,95,E-08|4,65,E-09|
|AREA|SRC_134|Cam_Valpo_15-PEAS e Imp|267848|6372720|1 mes|207,78|7,35,E-08|1,78,E-08|8,06,E-09|1,01,E-07|2,41,E-08|
|AREA|SRC_135|Cam_Valpo_16-PEAS e Imp|267715|6373066|1 mes|1484,08|1,03,E-08|2,49,E-09|1,13,E-09|1,42,E-08|3,37,E-09|
|AREA|SRC_136|Cam_Valpo_17-PEAS e Imp|267705|6373122|1 mes|225,43|6,78,E-08|1,64,E-08|7,43,E-09|9,32,E-08|2,22,E-08|
|AREA|SRC_137|Cam_Valpo_18-PEAS e Imp|267701|6373182|1 mes|241,22|6,33,E-08|1,53,E-08|6,94,E-09|8,71,E-08|2,07,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 84. Fuentes de Emisión - Escenario 1 parte 28

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 198 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_138|Cam_Valpo_19-PEAS e Imp|267704|6373237|1 mes|217,96|7,01,E-08|1,70,E-08|7,68,E-09|9,64,E-08|2,29,E-08|
|AREA|SRC_139|Cam_Valpo_20-PEAS e Imp|267713|6373309|1 mes|291,26|5,25,E-08|1,27,E-08|5,75,E-09|7,21,E-08|1,72,E-08|
|AREA|SRC_140|Cam_Valpo_21-PEAS e Imp|267741|6373522|1 mes|860,16|1,78,E-08|4,30,E-09|1,95,E-09|2,44,E-08|5,81,E-09|
|AREA|SRC_141|Cam_Valpo_22-PEAS e Imp|267757|6373574|1 mes|213,85|7,14,E-08|1,73,E-08|7,83,E-09|9,82,E-08|2,34,E-08|
|AREA|SRC_142|Cam_Valpo_23-PEAS e Imp|267777|6373617|1 mes|187,32|8,16,E-08|1,97,E-08|8,94,E-09|1,12,E-07|2,67,E-08|
|AREA|SRC_143|Cam_Valpo_24-PEAS e Imp|267817|6373719|1 mes|441,14|3,46,E-08|8,38,E-09|3,79,E-09|4,76,E-08|1,13,E-08|
|AREA|SRC_144|Cam_Valpo_25-PEAS e Imp|267843|6373782|1 mes|272,58|5,60,E-08|1,36,E-08|6,14,E-09|7,71,E-08|1,83,E-08|
|AREA|SRC_145|Cam_Valpo_26-PEAS e Imp|267877|6373831|1 mes|236,03|6,47,E-08|1,57,E-08|7,09,E-09|8,90,E-08|2,12,E-08|
|AREA|SRC_146|Cam_Valpo_27-PEAS e Imp|267910|6373883|1 mes|246,12|6,21,E-08|1,50,E-08|6,80,E-09|8,53,E-08|2,03,E-08|
|AREA|SRC_147|Cam_Valpo_28-PEAS e Imp|268105|6374174|1 mes|1399,53|1,09,E-08|2,64,E-09|1,20,E-09|1,50,E-08|3,57,E-09|
|AREA|SRC_148|Cam_Valpo_29-PEAS e Imp|268274|6374430|1 mes|1228,07|1,24,E-08|3,01,E-09|1,36,E-09|1,71,E-08|4,07,E-09|
|AREA|SRC_149|Cam_Valpo_30-PEAS e Imp|268317|6374478|1 mes|254,35|6,01,E-08|1,45,E-08|6,58,E-09|8,26,E-08|1,97,E-08|
|AREA|SRC_150|Cam_Valpo_31-PEAS e Imp|268347|6374502|1 mes|154,46|9,89,E-08|2,39,E-08|1,08,E-08|1,36,E-07|3,24,E-08|
|AREA|SRC_151|Cam_Valpo_32-PEAS e Imp|269602|6375295|1 mes|5935,56|2,57,E-09|6,23,E-10|2,82,E-10|3,54,E-09|8,42,E-10|
|AREA|SRC_152|Cam_Valpo_33-PEAS e Imp|270646|6375956|1 mes|4938,33|3,09,E-09|7,48,E-10|3,39,E-10|4,25,E-09|1,01,E-09|
|AREA|SRC_153|Cam_Valpo_34-PEAS e Imp|270700|6375970|1 mes|220,74|6,92,E-08|1,67,E-08|7,58,E-09|9,52,E-08|2,26,E-08|
|AREA|SRC_154|Cam_Valpo_35-PEAS e Imp|270759|6375972|1 mes|232,03|6,58,E-08|1,59,E-08|7,21,E-09|9,05,E-08|2,15,E-08|
|AREA|SRC_155|Cam_Valpo_36-PEAS e Imp|270817|6375960|1 mes|237,83|6,42,E-08|1,55,E-08|7,04,E-09|8,83,E-08|2,10,E-08|
|AREA|SRC_156|Cam_Valpo_37-PEAS e Imp|271210|6375788|1 mes|1710,95|8,93,E-09|2,16,E-09|9,78,E-10|1,23,E-08|2,92,E-09|
|AREA|SRC_157|Cam_Valpo_38-PEAS e Imp|271299|6375786|1 mes|362,06|4,22,E-08|1,02,E-08|4,62,E-09|5,80,E-08|1,38,E-08|
|AREA|SRC_158|Cam_Valpo_39-PEAS e Imp|271410|6375784|1 mes|444,09|3,44,E-08|8,32,E-09|3,77,E-09|4,73,E-08|1,13,E-08|
|AREA|SRC_159|Cam_Valpo_40-PEAS e Imp|271537|6375829|1 mes|539,94|2,83,E-08|6,85,E-09|3,10,E-09|3,89,E-08|9,26,E-09|
|AREA|SRC_160|Cam_Valpo_41-PEAS e Imp|271698|6375908|1 mes|717,64|2,13,E-08|5,15,E-09|2,33,E-09|2,93,E-08|6,97,E-09|
|AREA|SRC_161|Cam_Valpo_42-PEAS e Imp|271943|6376040|1 mes|1111,41|1,37,E-08|3,33,E-09|1,51,E-09|1,89,E-08|4,50,E-09|
|AREA|SRC_162|Cam_Valpo_43-PEAS e Imp|272216|6376245|1 mes|1365,82|1,12,E-08|2,71,E-09|1,23,E-09|1,54,E-08|3,66,E-09|
|AREA|SRC_163|Cam_Valpo_44-PEAS e Imp|272308|6376283|1 mes|396,81|3,85,E-08|9,31,E-09|4,22,E-09|5,29,E-08|1,26,E-08|
|AREA|SRC_164|Cam_Valpo_45-PEAS e Imp|272828|6376412|1 mes|2139,51|7,14,E-09|1,73,E-09|7,82,E-10|9,82,E-09|2,34,E-09|
|AREA|SRC_165|Cam_Valpo_46-PEAS e Imp|272961|6376463|1 mes|572,90|2,67,E-08|6,45,E-09|2,92,E-09|3,67,E-08|8,73,E-09|
|AREA|SRC_166|Cam_Valpo_47-PEAS e Imp|273101|6376548|1 mes|656,43|2,33,E-08|5,63,E-09|2,55,E-09|3,20,E-08|7,62,E-09|
|AREA|SRC_167|Cam_Valpo_48-PEAS e Imp|273683|6376890|1 mes|2699,98|5,66,E-09|1,37,E-09|6,20,E-10|7,78,E-09|1,85,E-09|
|AREA|SRC_168|Cam_Valpo_49-PEAS e Imp|273729|6376911|1 mes|198,66|7,69,E-08|1,86,E-08|8,43,E-09|1,06,E-07|2,52,E-08|
|AREA|SRC_169|Cam_Valpo_50-PEAS e Imp|273841|6376934|1 mes|455,50|3,35,E-08|8,11,E-09|3,68,E-09|4,61,E-08|1,10,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 84. Fuentes de Emisión - Escenario 1 parte 28

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 199 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_170|Cam_Valpo_51-PEAS e Imp|273918|6376948|1 mes|314,84|4,85,E-08|1,17,E-08|5,32,E-09|6,67,E-08|1,59,E-08|
|AREA|SRC_171|Cam_Valpo_52-PEAS e Imp|273963|6376959|1 mes|182,29|8,38,E-08|2,03,E-08|9,18,E-09|1,15,E-07|2,74,E-08|
|AREA|SRC_172|Cam_Valpo_53-PEAS e Imp|274013|6376981|1 mes|220,22|6,94,E-08|1,68,E-08|7,60,E-09|9,54,E-08|2,27,E-08|
|AREA|SRC_173|Cam_Valpo_54-PEAS e Imp|274045|6377010|1 mes|175,74|8,69,E-08|2,10,E-08|9,53,E-09|1,20,E-07|2,84,E-08|
|AREA|SRC_174|Cam_Valpo_55-PEAS e Imp|274402|6377569|1 mes|2654,98|5,75,E-09|1,39,E-09|6,31,E-10|7,91,E-09|1,88,E-09|
|AREA|SRC_175|Cam_Valpo_56-PEAS e Imp|274508|6377712|1 mes|712,20|2,15,E-08|5,19,E-09|2,35,E-09|2,95,E-08|7,02,E-09|
|AREA|SRC_176|Cam_Valpo_57-PEAS e Imp|274515|6377737|1 mes|105,54|1,45,E-07|3,50,E-08|1,59,E-08|1,99,E-07|4,74,E-08|
|AREA|SRC_177|Cam_Valpo_58-PEAS e Imp|274530|6377783|1 mes|190,85|8,00,E-08|1,94,E-08|8,77,E-09|1,10,E-07|2,62,E-08|
|AREA|SRC_178|Cam_Valpo_59-PEAS e Imp|274571|6378190|1 mes|1640,54|9,31,E-09|2,25,E-09|1,02,E-09|1,28,E-08|3,05,E-09|
|AREA|SRC_179|Cam_Valpo_60-PEAS e Imp|274512|6378662|1 mes|1902,24|8,03,E-09|1,94,E-09|8,80,E-10|1,10,E-08|2,63,E-09|
|AREA|SRC_180|Cam_Valpo_61-PEAS e Imp|274484|6378742|1 mes|339,36|4,50,E-08|1,09,E-08|4,93,E-09|6,19,E-08|1,47,E-08|
|AREA|SRC_181|Cam_Valpo_62-PEAS e Imp|274397|6378959|1 mes|934,88|1,63,E-08|3,95,E-09|1,79,E-09|2,25,E-08|5,35,E-09|
|AREA|SRC_182|Cam_Valpo_63-PEAS e Imp|274391|6379006|1 mes|189,58|8,06,E-08|1,95,E-08|8,83,E-09|1,11,E-07|2,64,E-08|
|AREA|SRC_183|Cam_Valpo_64-PEAS e Imp|274392|6379034|1 mes|109,49|1,40,E-07|3,38,E-08|1,53,E-08|1,92,E-07|4,57,E-08|
|AREA|SRC_184|Cam_Valpo_65-PEAS e Imp|274513|6379469|1 mes|1805,57|8,46,E-09|2,05,E-09|9,27,E-10|1,16,E-08|2,77,E-09|
|AREA|SRC_185|Cam_Valpo_66-PEAS e Imp|274514|6379510|1 mes|163,36|9,35,E-08|2,26,E-08|1,02,E-08|1,29,E-07|3,06,E-08|
|AREA|SRC_186|Cam_Valpo_67-PEAS e Imp|274503|6379560|1 mes|208,73|7,32,E-08|1,77,E-08|8,02,E-09|1,01,E-07|2,40,E-08|
|AREA|SRC_187|Cam_Valpo_68-PEAS e Imp|274488|6379623|1 mes|255,44|5,98,E-08|1,45,E-08|6,55,E-09|8,22,E-08|1,96,E-08|
|AREA|SRC_188|Cam_Valpo_69-PEAS e Imp|274426|6379798|1 mes|745,56|2,05,E-08|4,96,E-09|2,25,E-09|2,82,E-08|6,71,E-09|
|AREA|SRC_189|Cam_Valpo_70-PEAS e Imp|274386|6379897|1 mes|428,53|3,57,E-08|8,62,E-09|3,91,E-09|4,90,E-08|1,17,E-08|
|AREA|SRC_190|Cam_Valpo_71-PEAS e Imp|274352|6379981|1 mes|360,23|4,24,E-08|1,03,E-08|4,65,E-09|5,83,E-08|1,39,E-08|
|AREA|SRC_191|Cam_Valpo_72-PEAS e Imp|274336|6380041|1 mes|249,49|6,12,E-08|1,48,E-08|6,71,E-09|8,42,E-08|2,00,E-08|
|AREA|SRC_192|Cam_Valpo_73-PEAS e Imp|274333|6380099|1 mes|227,80|6,71,E-08|1,62,E-08|7,35,E-09|9,22,E-08|2,19,E-08|
|AREA|SRC_193|Cam_Valpo_74-PEAS e Imp|274332|6380163|1 mes|257,27|5,94,E-08|1,44,E-08|6,51,E-09|8,16,E-08|1,94,E-08|
|AREA|SRC_194|Cam_Valpo_75-PEAS e Imp|274329|6380546|1 mes|1530,44|9,98,E-09|2,42,E-09|1,09,E-09|1,37,E-08|3,27,E-09|
|AREA|SRC_195|Cam_Valpo_76-PEAS e Imp|274323|6380578|1 mes|130,55|1,17,E-07|2,83,E-08|1,28,E-08|1,61,E-07|3,83,E-08|
|AREA|SRC_196|Cam_Valpo_77-PEAS e Imp|274308|6380608|1 mes|138,17|1,11,E-07|2,68,E-08|1,21,E-08|1,52,E-07|3,62,E-08|
|AREA|SRC_197|Cam_Valpo_78-PEAS e Imp|274078|6381086|1 mes|2120,50|7,20,E-09|1,74,E-09|7,89,E-10|9,91,E-09|2,36,E-09|
|AREA|SRC_198|Cam_Valpo_79-PEAS e Imp|274036|6381146|1 mes|292,96|5,21,E-08|1,26,E-08|5,71,E-09|7,17,E-08|1,71,E-08|
|AREA|SRC_199|Cam_Valpo_80-PEAS e Imp|273997|6381192|1 mes|242,71|6,29,E-08|1,52,E-08|6,90,E-09|8,65,E-08|2,06,E-08|
|AREA|SRC_200|Cam_Valpo_81-PEAS e Imp|273945|6381212|1 mes|225,25|6,78,E-08|1,64,E-08|7,43,E-09|9,33,E-08|2,22,E-08|
|AREA|SRC_201|Cam_Valpo_82-PEAS e Imp|273863|6381235|1 mes|340,59|4,49,E-08|1,09,E-08|4,91,E-09|6,17,E-08|1,47,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 84. Fuentes de Emisión - Escenario 1 parte 28

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 200 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_202|Cam_Valpo_83-PEAS e Imp|273527|6381309|1 mes|1376,67|1,11,E-08|2,68,E-09|1,22,E-09|1,53,E-08|3,63,E-09|
|AREA|SRC_203|Cam_Valpo_84-PEAS e Imp|273488|6381317|1 mes|158,83|9,62,E-08|2,33,E-08|1,05,E-08|1,32,E-07|3,15,E-08|
|AREA|SRC_204|Cam_Valpo_85-PEAS e Imp|273437|6381311|1 mes|210,61|7,25,E-08|1,76,E-08|7,95,E-09|9,97,E-08|2,37,E-08|
|AREA|SRC_205|Cam_Valpo_86-PEAS e Imp|273400|6381306|1 mes|148,75|1,03,E-07|2,48,E-08|1,13,E-08|1,41,E-07|3,36,E-08|
|AREA|SRC_206|Cam_Valpo_87-PEAS e Imp|273330|6381278|1 mes|302,02|5,06,E-08|1,22,E-08|5,54,E-09|6,96,E-08|1,66,E-08|
|AREA|SRC_207|Cam_Valpo_88-PEAS e Imp|273269|6381275|1 mes|240,32|6,36,E-08|1,54,E-08|6,97,E-09|8,74,E-08|2,08,E-08|
|AREA|SRC_208|Cam_Valpo_89-PEAS e Imp|273210|6381284|1 mes|238,69|6,40,E-08|1,55,E-08|7,01,E-09|8,80,E-08|2,09,E-08|
|AREA|SRC_209|Cam_Valpo_90-PEAS e Imp|273140|6381307|1 mes|291,89|5,23,E-08|1,27,E-08|5,74,E-09|7,20,E-08|1,71,E-08|
|AREA|SRC_210|Cam_Valpo_91-PEAS e Imp|273026|6381364|1 mes|510,61|2,99,E-08|7,24,E-09|3,28,E-09|4,11,E-08|9,79,E-09|
|AREA|SRC_211|Cam_Valpo_92-PEAS e Imp|272787|6381471|1 mes|1046,47|1,46,E-08|3,53,E-09|1,60,E-09|2,01,E-08|4,78,E-09|
|AREA|SRC_212|Cam_Valpo_93-PEAS e Imp|272625|6381553|1 mes|726,81|2,10,E-08|5,09,E-09|2,30,E-09|2,89,E-08|6,88,E-09|
|AREA|SRC_213|Cam_Valpo_94-PEAS e Imp|272586|6381587|1 mes|205,87|7,42,E-08|1,80,E-08|8,13,E-09|1,02,E-07|2,43,E-08|
|AREA|SRC_214|Cam_Valpo_95-PEAS e Imp|272567|6381621|1 mes|150,25|1,02,E-07|2,46,E-08|1,11,E-08|1,40,E-07|3,33,E-08|
|AREA|SRC_215|Cam_Valpo_96-PEAS e Imp|272558|6381659|1 mes|154,59|9,88,E-08|2,39,E-08|1,08,E-08|1,36,E-07|3,23,E-08|
|AREA|SRC_216|Cam_Valpo_97-PEAS e Imp|272513|6381931|1 mes|1103,20|1,38,E-08|3,35,E-09|1,52,E-09|1,90,E-08|4,53,E-09|
|AREA|SRC_217|Cam_Valpo_98-PEAS e Imp|272500|6382030|1 mes|398,37|3,83,E-08|9,28,E-09|4,20,E-09|5,27,E-08|1,26,E-08|
|AREA|SRC_218|Cam_Valpo_99-PEAS e Imp|272492|6382086|1 mes|223,87|6,82,E-08|1,65,E-08|7,48,E-09|9,38,E-08|2,23,E-08|
|AREA|SRC_219|Cam_Valpo_100-PEAS e Imp|272491|6382127|1 mes|164,32|9,30,E-08|2,25,E-08|1,02,E-08|1,28,E-07|3,04,E-08|
|AREA|SRC_220|Cam_Valpo_101-PEAS e Imp|272506|6382188|1 mes|247,33|6,18,E-08|1,49,E-08|6,77,E-09|8,49,E-08|2,02,E-08|
|AREA|SRC_221|Cam_Valpo_102-PEAS e Imp|272660|6383439|1 mes|5043,31|3,03,E-09|7,33,E-10|3,32,E-10|4,17,E-09|9,91,E-10|
|AREA|SRC_222|Cam_Valpo_103-PEAS e Imp|272630|6384559|1 mes|4478,91|3,41,E-09|8,25,E-10|3,74,E-10|4,69,E-09|1,12,E-09|
|AREA|SRC_223|Cam_Valpo_104-PEAS e Imp|272626|6385227|1 mes|2671,08|5,72,E-09|1,38,E-09|6,27,E-10|7,86,E-09|1,87,E-09|
|AREA|SRC_224|Cam_Valpo_105-PEAS e Imp|272602|6386454|1 mes|4905,80|3,11,E-09|7,53,E-10|3,41,E-10|4,28,E-09|1,02,E-09|
|AREA|SRC_225|Cam_Valpo_106-PEAS e Imp|272609|6386527|1 mes|292,53|5,22,E-08|1,26,E-08|5,72,E-09|7,18,E-08|1,71,E-08|
|AREA|SRC_226|Cam_Valpo_107-PEAS e Imp|272650|6386615|1 mes|384,69|3,97,E-08|9,61,E-09|4,35,E-09|5,46,E-08|1,30,E-08|
|AREA|SRC_227|Cam_Valpo_108-PEAS e Imp|272755|6386705|1 mes|550,00|2,78,E-08|6,72,E-09|3,04,E-09|3,82,E-08|9,09,E-09|
|AREA|SRC_228|Cam_Valpo_109-PEAS e Imp|272846|6386776|1 mes|460,85|3,32,E-08|8,02,E-09|3,63,E-09|4,56,E-08|1,08,E-08|
|AREA|SRC_229|Cam_Valpo_110-PEAS e Imp|272918|6386821|1 mes|338,79|4,51,E-08|1,09,E-08|4,94,E-09|6,20,E-08|1,48,E-08|
|AREA|SRC_230|Cam_Valpo_111-PEAS e Imp|272959|6386856|1 mes|215,71|7,08,E-08|1,71,E-08|7,76,E-09|9,74,E-08|2,32,E-08|
|AREA|SRC_231|Cam_Valpo_112-PEAS e Imp|272979|6386909|1 mes|229,32|6,66,E-08|1,61,E-08|7,30,E-09|9,16,E-08|2,18,E-08|
|AREA|SRC_232|Cam_Valpo_113-PEAS e Imp|272982|6386950|1 mes|168,20|9,08,E-08|2,20,E-08|9,95,E-09|1,25,E-07|2,97,E-08|
|AREA|SRC_233|Cam_Valpo_114-PEAS e Imp|272974|6387033|1 mes|334,56|4,57,E-08|1,10,E-08|5,00,E-09|6,28,E-08|1,49,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 84. Fuentes de Emisión - Escenario 1 parte 28

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 201 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_234|Cam_Valpo_115-PEAS e Imp|272969|6387289|1 mes|1021,26|1,50,E-08|3,62,E-09|1,64,E-09|2,06,E-08|4,90,E-09|
|AREA|SRC_235|Cam_Valpo_116-PEAS e Imp|272950|6387316|1 mes|135,86|1,12,E-07|2,72,E-08|1,23,E-08|1,55,E-07|3,68,E-08|
|AREA|SRC_236|Cam_Valpo_117-PEAS e Imp|272918|6387332|1 mes|150,62|1,01,E-07|2,45,E-08|1,11,E-08|1,39,E-07|3,32,E-08|
|AREA|SRC_237|Cam_Valpo_118-PEAS e Imp|272871|6387328|1 mes|193,11|7,91,E-08|1,91,E-08|8,67,E-09|1,09,E-07|2,59,E-08|
|AREA|SRC_238|Cam_Valpo_119-PEAS e Imp|272818|6387319|1 mes|214,82|7,11,E-08|1,72,E-08|7,79,E-09|9,78,E-08|2,33,E-08|
|AREA|SRC_239|Cam_Valpo_120-PEAS e Imp|272669|6387324|1 mes|593,51|2,57,E-08|6,23,E-09|2,82,E-09|3,54,E-08|8,42,E-09|
|AREA|SRC_240|Cam_Valpo_121-PEAS e Imp|272536|6387380|1 mes|574,11|2,66,E-08|6,44,E-09|2,92,E-09|3,66,E-08|8,71,E-09|
|AREA|SRC_241|Cam_Valpo_122-PEAS e Imp|272406|6387475|1 mes|642,85|2,38,E-08|5,75,E-09|2,60,E-09|3,27,E-08|7,78,E-09|
|AREA|SRC_242|Cam_Valpo_123-PEAS e Imp|272321|6387544|1 mes|438,86|3,48,E-08|8,42,E-09|3,81,E-09|4,79,E-08|1,14,E-08|
|AREA|SRC_243|Cam_Valpo_124-PEAS e Imp|272252|6387605|1 mes|366,01|4,17,E-08|1,01,E-08|4,57,E-09|5,74,E-08|1,37,E-08|
|AREA|SRC_244|Cam_Valpo_125-PEAS e Imp|272138|6387749|1 mes|733,97|2,08,E-08|5,04,E-09|2,28,E-09|2,86,E-08|6,81,E-09|
|AREA|SRC_245|Cam_Valpo_126-PEAS e Imp|272059|6387890|1 mes|645,70|2,37,E-08|5,72,E-09|2,59,E-09|3,25,E-08|7,74,E-09|
|AREA|SRC_246|Cam_Valpo_127-PEAS e Imp|272019|6388008|1 mes|494,29|3,09,E-08|7,48,E-09|3,39,E-09|4,25,E-08|1,01,E-08|
|AREA|SRC_247|Cam_Valpo_128-PEAS e Imp|272005|6388086|1 mes|318,17|4,80,E-08|1,16,E-08|5,26,E-09|6,60,E-08|1,57,E-08|
|AREA|SRC_248|Cam_Valpo_129-PEAS e Imp|272005|6388171|1 mes|338,40|4,51,E-08|1,09,E-08|4,95,E-09|6,21,E-08|1,48,E-08|
|AREA|SRC_249|Cam_Valpo_130-PEAS e Imp|272018|6388207|1 mes|149,40|1,02,E-07|2,47,E-08|1,12,E-08|1,41,E-07|3,35,E-08|
|AREA|SRC_250|Cam_Valpo_131-PEAS e Imp|272053|6388222|1 mes|144,57|1,06,E-07|2,56,E-08|1,16,E-08|1,45,E-07|3,46,E-08|
|AREA|SRC_251|Cam_Valpo_132-PEAS e Imp|272113|6388260|1 mes|286,19|5,34,E-08|1,29,E-08|5,85,E-09|7,34,E-08|1,75,E-08|
|AREA|SRC_252|Cam_Valpo_133-PEAS e Imp|272165|6388289|1 mes|236,50|6,46,E-08|1,56,E-08|7,08,E-09|8,88,E-08|2,11,E-08|
|AREA|SRC_253|Cam_Valpo_134-PEAS e Imp|272170|6388313|1 mes|103,04|1,48,E-07|3,59,E-08|1,62,E-08|2,04,E-07|4,85,E-08|
|AREA|SRC_254|Cam_Valpo_135-PEAS e Imp|272160|6388355|1 mes|178,67|8,55,E-08|2,07,E-08|9,37,E-09|1,18,E-07|2,80,E-08|
|AREA|SRC_255|Cam_Valpo_136-PEAS e Imp|272116|6388384|1 mes|213,17|7,17,E-08|1,73,E-08|7,85,E-09|9,85,E-08|2,35,E-08|
|AREA|SRC_256|Cam_Valpo_137-PEAS e Imp|271990|6388473|1 mes|618,26|2,47,E-08|5,98,E-09|2,71,E-09|3,40,E-08|8,09,E-09|
|AREA|SRC_257|Cam_Valpo_138-PEAS e Imp|271909|6388570|1 mes|502,24|3,04,E-08|7,36,E-09|3,33,E-09|4,18,E-08|9,95,E-09|
|AREA|SRC_258|Cam_Valpo_139-PEAS e Imp|271887|6388631|1 mes|257,67|5,93,E-08|1,43,E-08|6,50,E-09|8,15,E-08|1,94,E-08|
|AREA|SRC_259|Cam_Valpo_140-PEAS e Imp|271869|6388710|1 mes|324,57|4,71,E-08|1,14,E-08|5,16,E-09|6,47,E-08|1,54,E-08|
|AREA|SRC_260|Cam_Valpo_141-PEAS e Imp|271879|6388778|1 mes|270,72|5,64,E-08|1,37,E-08|6,18,E-09|7,76,E-08|1,85,E-08|
|AREA|SRC_261|Cam_Valpo_142-PEAS e Imp|271889|6388831|1 mes|215,81|7,08,E-08|1,71,E-08|7,76,E-09|9,73,E-08|2,32,E-08|
|AREA|SRC_262|Cam_Valpo_143-PEAS e Imp|271888|6388910|1 mes|317,54|4,81,E-08|1,16,E-08|5,27,E-09|6,62,E-08|1,57,E-08|
|AREA|SRC_263|Cam_Valpo_144-PEAS e Imp|271765|6389249|1 mes|1443,83|1,06,E-08|2,56,E-09|1,16,E-09|1,45,E-08|3,46,E-09|
|AREA|SRC_264|Cam_Valpo_145-PEAS e Imp|271745|6389323|1 mes|308,68|4,95,E-08|1,20,E-08|5,42,E-09|6,81,E-08|1,62,E-08|
|AREA|SRC_265|Cam_Valpo_146-PEAS e Imp|271746|6389404|1 mes|321,13|4,76,E-08|1,15,E-08|5,21,E-09|6,54,E-08|1,56,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 84. Fuentes de Emisión - Escenario 1 parte 28

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 202 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_266|Cam_Valpo_147-PEAS e Imp|271745|6389713|1 mes|1235,33|1,24,E-08|2,99,E-09|1,36,E-09|1,70,E-08|4,05,E-09|
|AREA|SRC_267|Cam_Valpo_148-PEAS e Imp|271729|6389779|1 mes|274,74|5,56,E-08|1,35,E-08|6,09,E-09|7,65,E-08|1,82,E-08|
|AREA|SRC_268|Cam_Valpo_149-PEAS e Imp|271405|6390771|1 mes|4169,69|3,66,E-09|8,86,E-10|4,01,E-10|5,04,E-09|1,20,E-09|
|AREA|SRC_269|Cam_Valpo_150-PEAS e Imp|271408|6390852|1 mes|324,07|4,71,E-08|1,14,E-08|5,17,E-09|6,48,E-08|1,54,E-08|
|AREA|SRC_270|Cam_Valpo_151-PEAS e Imp|271425|6390918|1 mes|269,76|5,66,E-08|1,37,E-08|6,21,E-09|7,79,E-08|1,85,E-08|
|AREA|SRC_271|Cam_Valpo_152-PEAS e Imp|271595|6391444|1 mes|2210,20|6,91,E-09|1,67,E-09|7,57,E-10|9,50,E-09|2,26,E-09|
|AREA|SRC_272|Cam_Valpo_153-PEAS e Imp|271601|6391518|1 mes|297,07|5,14,E-08|1,24,E-08|5,64,E-09|7,07,E-08|1,68,E-08|
|AREA|SRC_273|Cam_Valpo_154-PEAS e Imp|271583|6391599|1 mes|334,56|4,57,E-08|1,10,E-08|5,00,E-09|6,28,E-08|1,49,E-08|
|AREA|SRC_274|Cam_Valpo_155-PEAS e Imp|271490|6391665|1 mes|462,29|3,30,E-08|8,00,E-09|3,62,E-09|4,54,E-08|1,08,E-08|
|AREA|SRC_275|Cam_Valpo_156-PEAS e Imp|271388|6391779|1 mes|610,49|2,50,E-08|6,05,E-09|2,74,E-09|3,44,E-08|8,19,E-09|
|AREA|SRC_276|Cam_Valpo_157-PEAS e Imp|271303|6391969|1 mes|829,95|1,84,E-08|4,45,E-09|2,02,E-09|2,53,E-08|6,02,E-09|
|AREA|SRC_277|Cam_Valpo_158-PEAS e Imp|271249|6392048|1 mes|385,48|3,96,E-08|9,59,E-09|4,34,E-09|5,45,E-08|1,30,E-08|
|AREA|SRC_278|Cam_Valpo_159-PEAS e Imp|271095|6392199|1 mes|863,11|1,77,E-08|4,28,E-09|1,94,E-09|2,43,E-08|5,79,E-09|
|AREA|SRC_279|Cam_Valpo_160-PEAS e Imp|271003|6392357|1 mes|727,41|2,10,E-08|5,08,E-09|2,30,E-09|2,89,E-08|6,87,E-09|
|AREA|SRC_280|Cam_Valpo_161-PEAS e Imp|270864|6392618|1 mes|1181,67|1,29,E-08|3,13,E-09|1,42,E-09|1,78,E-08|4,23,E-09|
|AREA|SRC_281|Cam_Valpo_162-PEAS e Imp|270665|6392901|1 mes|1386,67|1,10,E-08|2,67,E-09|1,21,E-09|1,51,E-08|3,61,E-09|
|AREA|SRC_282|Cam_Valpo_163-PEAS e Imp|270570|6393060|1 mes|739,81|2,07,E-08|5,00,E-09|2,26,E-09|2,84,E-08|6,76,E-09|
|AREA|SRC_283|Cam_Valpo_164-PEAS e Imp|270535|6393162|1 mes|427,94|3,57,E-08|8,64,E-09|3,91,E-09|4,91,E-08|1,17,E-08|
|AREA|SRC_284|Cam_Valpo_165-PEAS e Imp|270408|6393157|1 mes|516,16|2,96,E-08|7,16,E-09|3,24,E-09|4,07,E-08|9,69,E-09|
|AREA|SRC_285|Cam_Valpo_166-PEAS e Imp|270322|6393156|1 mes|344,11|4,44,E-08|1,07,E-08|4,86,E-09|6,10,E-08|1,45,E-08|
|AREA|SRC_286|Cam_Valpo_167-PEAS e Imp|270198|6393225|1 mes|562,03|2,72,E-08|6,58,E-09|2,98,E-09|3,74,E-08|8,90,E-09|
|AREA|SRC_287|Cam_Valpo_168-PEAS e Imp|270084|6393222|1 mes|461,57|3,31,E-08|8,01,E-09|3,63,E-09|4,55,E-08|1,08,E-08|
|AREA|SRC_288|Cam_Valpo_169-PEAS e Imp|270014|6393114|1 mes|520,05|2,94,E-08|7,11,E-09|3,22,E-09|4,04,E-08|9,61,E-09|
|AREA|SRC_289|Cam_Valpo_170-PEAS e Imp|269944|6393026|1 mes|448,19|3,41,E-08|8,25,E-09|3,74,E-09|4,69,E-08|1,12,E-08|
|AREA|SRC_290|Cam_Valpo_171-PEAS e Imp|269831|6392981|1 mes|484,35|3,15,E-08|7,63,E-09|3,46,E-09|4,34,E-08|1,03,E-08|
|AREA|SRC_291|Cam_Valpo_172-PEAS e Imp|269702|6392966|1 mes|516,99|2,96,E-08|7,15,E-09|3,24,E-09|4,06,E-08|9,67,E-09|
|AREA|SRC_292|Cam_Valpo_173-PEAS e Imp|269506|6393084|1 mes|906,73|1,68,E-08|4,08,E-09|1,85,E-09|2,32,E-08|5,51,E-09|
|AREA|SRC_293|Cam_Valpo_174-PEAS e Imp|269407|6393106|1 mes|410,62|3,72,E-08|9,00,E-09|4,08,E-09|5,12,E-08|1,22,E-08|
|AREA|SRC_294|Cam_Valpo_175-PEAS e Imp|269355|6393219|1 mes|493,13|3,10,E-08|7,50,E-09|3,39,E-09|4,26,E-08|1,01,E-08|
|AREA|SRC_295|Cam_Valpo_176-PEAS e Imp|269450|6393436|1 mes|939,57|1,63,E-08|3,93,E-09|1,78,E-09|2,24,E-08|5,32,E-09|
|AREA|SRC_296|Cam_Valpo_177-PEAS e Imp|269537|6393768|1 mes|1375,49|1,11,E-08|2,69,E-09|1,22,E-09|1,53,E-08|3,63,E-09|
|AREA|SRC_297|Cam_Valpo_178-PEAS e Imp|269541|6393876|1 mes|433,16|3,53,E-08|8,53,E-09|3,86,E-09|4,85,E-08|1,15,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 84. Fuentes de Emisión - Escenario 1 parte 28

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 203 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_298|Cam_Valpo_179-PEAS e Imp|269514|6393952|1 mes|327,49|4,66,E-08|1,13,E-08|5,11,E-09|6,41,E-08|1,53,E-08|
|AREA|SRC_299|Cam_Valpo_180-PEAS e Imp|269461|6394006|1 mes|302,03|5,06,E-08|1,22,E-08|5,54,E-09|6,95,E-08|1,66,E-08|
|AREA|SRC_300|Cam_Valpo_181-PEAS e Imp|269456|6394087|1 mes|317,54|4,81,E-08|1,16,E-08|5,27,E-09|6,62,E-08|1,57,E-08|
|AREA|SRC_301|Cam_Valpo_182-PEAS e Imp|269494|6394169|1 mes|358,94|4,26,E-08|1,03,E-08|4,66,E-09|5,85,E-08|1,39,E-08|
|AREA|SRC_302|Cam_Valpo_183-PEAS e Imp|269580|6394296|1 mes|611,99|2,50,E-08|6,04,E-09|2,74,E-09|3,43,E-08|8,17,E-09|
|AREA|SRC_303|Cam_Valpo_184-PEAS e Imp|269614|6394394|1 mes|416,61|3,67,E-08|8,87,E-09|4,02,E-09|5,04,E-08|1,20,E-08|
|AREA|SRC_304|Cam_Valpo_185-PEAS e Imp|269617|6394492|1 mes|396,57|3,85,E-08|9,32,E-09|4,22,E-09|5,30,E-08|1,26,E-08|
|AREA|SRC_305|Cam_Valpo_186-PEAS e Imp|269532|6394634|1 mes|664,18|2,30,E-08|5,56,E-09|2,52,E-09|3,16,E-08|7,53,E-09|
|AREA|SRC_306|Cam_Valpo_187-PEAS e Imp|269478|6394752|1 mes|518,20|2,95,E-08|7,13,E-09|3,23,E-09|4,05,E-08|9,65,E-09|
|AREA|SRC_307|Cam_Valpo_188-PEAS e Imp|269437|6394881|1 mes|540,93|2,82,E-08|6,83,E-09|3,09,E-09|3,88,E-08|9,24,E-09|
|AREA|SRC_308|Cam_Valpo_189-PEAS e Imp|269448|6395002|1 mes|483,46|3,16,E-08|7,65,E-09|3,46,E-09|4,34,E-08|1,03,E-08|
|AREA|SRC_309|Cam_Valpo_190-PEAS e Imp|269465|6395049|1 mes|197,82|7,72,E-08|1,87,E-08|8,46,E-09|1,06,E-07|2,53,E-08|
|AREA|SRC_310|Cam_Valpo_191-PEAS e Imp|269701|6395188|1 mes|1088,66|1,40,E-08|3,40,E-09|1,54,E-09|1,93,E-08|4,59,E-09|
|AREA|SRC_311|Cam_Valpo_192-PEAS e Imp|269737|6395244|1 mes|269,38|5,67,E-08|1,37,E-08|6,21,E-09|7,80,E-08|1,86,E-08|
|AREA|SRC_312|Cam_Valpo_193-PEAS e Imp|269748|6395318|1 mes|301,88|5,06,E-08|1,22,E-08|5,55,E-09|6,96,E-08|1,66,E-08|
|AREA|SRC_313|Cam_Valpo_194-PEAS e Imp|269734|6395473|1 mes|624,02|2,45,E-08|5,92,E-09|2,68,E-09|3,37,E-08|8,01,E-09|
|AREA|SRC_314|Cam_Valpo_195-PEAS e Imp|269791|6395575|1 mes|462,91|3,30,E-08|7,98,E-09|3,62,E-09|4,54,E-08|1,08,E-08|
|AREA|SRC_315|Cam_Valpo_196-PEAS e Imp|269918|6395634|1 mes|557,57|2,74,E-08|6,63,E-09|3,00,E-09|3,77,E-08|8,97,E-09|
|AREA|SRC_316|Cam_Valpo_197-PEAS e Imp|269951|6395703|1 mes|311,66|4,90,E-08|1,19,E-08|5,37,E-09|6,74,E-08|1,60,E-08|
|AREA|SRC_317|Cam_Valpo_198-PEAS e Imp|269926|6395767|1 mes|277,87|5,50,E-08|1,33,E-08|6,02,E-09|7,56,E-08|1,80,E-08|
|AREA|SRC_318|Cam_Valpo_199-PEAS e Imp|269853|6395812|1 mes|348,28|4,39,E-08|1,06,E-08|4,81,E-09|6,03,E-08|1,44,E-08|
|AREA|SRC_319|Cam_Valpo_200-PEAS e Imp|269732|6395847|1 mes|504,67|3,03,E-08|7,32,E-09|3,32,E-09|4,16,E-08|9,91,E-09|
|AREA|SRC_320|Cam_Valpo_201-PEAS e Imp|269688|6395928|1 mes|365,46|4,18,E-08|1,01,E-08|4,58,E-09|5,75,E-08|1,37,E-08|
|AREA|SRC_321|Cam_Valpo_202-PEAS e Imp|269717|6396047|1 mes|484,68|3,15,E-08|7,63,E-09|3,45,E-09|4,33,E-08|1,03,E-08|
|AREA|SRC_322|Cam_Valpo_203-PEAS e Imp|269712|6396106|1 mes|237,49|6,43,E-08|1,56,E-08|7,05,E-09|8,84,E-08|2,11,E-08|
|AREA|SRC_323|Cam_Valpo_204-PEAS e Imp|269657|6396143|1 mes|271,48|5,63,E-08|1,36,E-08|6,17,E-09|7,74,E-08|1,84,E-08|
|AREA|SRC_324|Cam_Valpo_205-PEAS e Imp|269580|6396120|1 mes|326,46|4,68,E-08|1,13,E-08|5,13,E-09|6,43,E-08|1,53,E-08|
|AREA|SRC_325|Cam_Valpo_206-PEAS e Imp|269501|6396070|1 mes|376,20|4,06,E-08|9,82,E-09|4,45,E-09|5,58,E-08|1,33,E-08|
|AREA|SRC_326|Cam_Valpo_207-PEAS e Imp|269359|6396026|1 mes|593,54|2,57,E-08|6,23,E-09|2,82,E-09|3,54,E-08|8,42,E-09|
|AREA|SRC_327|Cam_Valpo_208-PEAS e Imp|269272|6396023|1 mes|343,48|4,45,E-08|1,08,E-08|4,87,E-09|6,12,E-08|1,46,E-08|
|AREA|SRC_328|Cam_Valpo_209-PEAS e Imp|269222|6396073|1 mes|275,81|5,54,E-08|1,34,E-08|6,07,E-09|7,62,E-08|1,81,E-08|
|AREA|SRC_329|Cam_Valpo_210-PEAS e Imp|269210|6396185|1 mes|446,25|3,42,E-08|8,28,E-09|3,75,E-09|4,71,E-08|1,12,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 84. Fuentes de Emisión - Escenario 1 parte 28

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 204 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_330|Cam_Valpo_211-PEAS e Imp|269167|6396232|1 mes|255,46|5,98,E-08|1,45,E-08|6,55,E-09|8,22,E-08|1,96,E-08|
|AREA|SRC_331|Cam_Valpo_212-PEAS e Imp|269082|6396226|1 mes|349,58|4,37,E-08|1,06,E-08|4,79,E-09|6,01,E-08|1,43,E-08|
|AREA|SRC_332|Cam_Valpo_213-PEAS e Imp|268998|6396240|1 mes|335,54|4,55,E-08|1,10,E-08|4,99,E-09|6,26,E-08|1,49,E-08|
|AREA|SRC_333|Cam_Valpo_214-PEAS e Imp|268894|6396300|1 mes|480,09|3,18,E-08|7,70,E-09|3,49,E-09|4,38,E-08|1,04,E-08|
|AREA|SRC_334|Cam_Valpo_215-PEAS e Imp|268805|6396381|1 mes|477,49|3,20,E-08|7,74,E-09|3,51,E-09|4,40,E-08|1,05,E-08|
|AREA|SRC_335|Cam_Valpo_216-PEAS e Imp|268734|6396481|1 mes|489,34|3,12,E-08|7,55,E-09|3,42,E-09|4,29,E-08|1,02,E-08|
|AREA|SRC_336|Cam_Valpo_217-PEAS e Imp|268692|6396569|1 mes|388,32|3,93,E-08|9,52,E-09|4,31,E-09|5,41,E-08|1,29,E-08|
|AREA|SRC_337|Cam_Valpo_218-PEAS e Imp|268614|6396686|1 mes|563,68|2,71,E-08|6,56,E-09|2,97,E-09|3,73,E-08|8,87,E-09|
|AREA|SRC_338|Cam_Valpo_219-PEAS e Imp|268551|6396751|1 mes|365,13|4,18,E-08|1,01,E-08|4,58,E-09|5,75,E-08|1,37,E-08|
|AREA|SRC_339|Cam_Valpo_220-PEAS e Imp|268525|6396834|1 mes|342,75|4,46,E-08|1,08,E-08|4,88,E-09|6,13,E-08|1,46,E-08|
|AREA|SRC_340|Cam_Valpo_221-PEAS e Imp|268521|6396918|1 mes|335,20|4,56,E-08|1,10,E-08|4,99,E-09|6,27,E-08|1,49,E-08|
|AREA|SRC_341|Cam_Valpo_222-PEAS e Imp|268510|6396996|1 mes|312,17|4,89,E-08|1,18,E-08|5,36,E-09|6,73,E-08|1,60,E-08|
|AREA|SRC_342|Cam_Valpo_223-PEAS e Imp|268441|6397095|1 mes|486,78|3,14,E-08|7,59,E-09|3,44,E-09|4,32,E-08|1,03,E-08|
|AREA|SRC_343|Cam_Valpo_224-PEAS e Imp|268352|6397195|1 mes|537,81|2,84,E-08|6,87,E-09|3,11,E-09|3,91,E-08|9,30,E-09|
|AREA|SRC_344|Cam_Valpo_225-PEAS e Imp|268295|6397296|1 mes|460,41|3,32,E-08|8,03,E-09|3,64,E-09|4,56,E-08|1,09,E-08|
|AREA|SRC_345|Cam_Valpo_226-PEAS e Imp|268265|6397370|1 mes|319,00|4,79,E-08|1,16,E-08|5,25,E-09|6,58,E-08|1,57,E-08|
|AREA|SRC_346|Cam_Valpo_227-PEAS e Imp|268236|6397470|1 mes|414,51|3,69,E-08|8,92,E-09|4,04,E-09|5,07,E-08|1,21,E-08|
|AREA|SRC_347|Cam_Valpo_228-PEAS e Imp|268225|6397539|1 mes|278,02|5,50,E-08|1,33,E-08|6,02,E-09|7,56,E-08|1,80,E-08|
|AREA|SRC_348|Cam_Valpo_229-PEAS e Imp|268212|6397650|1 mes|446,47|3,42,E-08|8,28,E-09|3,75,E-09|4,70,E-08|1,12,E-08|
|AREA|SRC_349|Cam_Valpo_230-PEAS e Imp|268292|6397691|1 mes|352,90|4,33,E-08|1,05,E-08|4,74,E-09|5,95,E-08|1,42,E-08|
|AREA|SRC_350|Cam_Valpo_231-PEAS e Imp|268324|6397741|1 mes|244,09|6,26,E-08|1,51,E-08|6,86,E-09|8,61,E-08|2,05,E-08|
|AREA|SRC_351|Cam_Valpo_232-PEAS e Imp|268344|6397809|1 mes|284,52|5,37,E-08|1,30,E-08|5,88,E-09|7,38,E-08|1,76,E-08|
|AREA|SRC_352|Cam_Valpo_233-PEAS e Imp|268317|6397871|1 mes|277,40|5,51,E-08|1,33,E-08|6,03,E-09|7,57,E-08|1,80,E-08|
|AREA|SRC_353|Cam_Valpo_234-PEAS e Imp|268289|6397931|1 mes|263,44|5,80,E-08|1,40,E-08|6,35,E-09|7,97,E-08|1,90,E-08|
|AREA|SRC_354|Cam_Valpo_235-PEAS e Imp|268281|6397993|1 mes|246,21|6,20,E-08|1,50,E-08|6,80,E-09|8,53,E-08|2,03,E-08|
|AREA|SRC_355|Cam_Valpo_236-PEAS e Imp|268325|6398057|1 mes|307,11|4,97,E-08|1,20,E-08|5,45,E-09|6,84,E-08|1,63,E-08|
|AREA|SRC_356|Cam_Valpo_237-PEAS e Imp|268339|6398092|1 mes|154,12|9,91,E-08|2,40,E-08|1,09,E-08|1,36,E-07|3,24,E-08|
|AREA|SRC_357|Cam_Valpo_238-PEAS e Imp|268362|6398151|1 mes|251,56|6,07,E-08|1,47,E-08|6,65,E-09|8,35,E-08|1,99,E-08|
|AREA|SRC_358|Cam_Valpo_239-PEAS e Imp|268383|6398192|1 mes|185,19|8,25,E-08|2,00,E-08|9,04,E-09|1,13,E-07|2,70,E-08|
|AREA|SRC_359|Cam_Valpo_240-PEAS e Imp|268355|6398247|1 mes|250,18|6,11,E-08|1,48,E-08|6,69,E-09|8,40,E-08|2,00,E-08|
|AREA|SRC_360|Cam_Valpo_241-PEAS e Imp|268227|6398303|1 mes|566,84|2,70,E-08|6,52,E-09|2,95,E-09|3,71,E-08|8,82,E-09|
|AREA|SRC_361|Cam_Valpo_242-PEAS e Imp|268140|6398362|1 mes|418,83|3,65,E-08|8,82,E-09|4,00,E-09|5,02,E-08|1,19,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 84. Fuentes de Emisión - Escenario 1 parte 28

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 205 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_362|Cam_Valpo_243-PEAS e Imp|268089|6398427|1 mes|325,43|4,69,E-08|1,14,E-08|5,14,E-09|6,45,E-08|1,54,E-08|
|AREA|SRC_363|Cam_Valpo_244-PEAS e Imp|268005|6398483|1 mes|406,15|3,76,E-08|9,10,E-09|4,12,E-09|5,17,E-08|1,23,E-08|
|AREA|SRC_364|Cam_Valpo_245-PEAS e Imp|267956|6398553|1 mes|338,26|4,52,E-08|1,09,E-08|4,95,E-09|6,21,E-08|1,48,E-08|
|AREA|SRC_365|Cam_Valpo_246-PEAS e Imp|267920|6398673|1 mes|498,96|3,06,E-08|7,41,E-09|3,36,E-09|4,21,E-08|1,00,E-08|
|AREA|SRC_366|Cam_Valpo_247-PEAS e Imp|267908|6398749|1 mes|308,37|4,95,E-08|1,20,E-08|5,43,E-09|6,81,E-08|1,62,E-08|
|AREA|SRC_367|Cam_Valpo_248-PEAS e Imp|267894|6398771|1 mes|107,41|1,42,E-07|3,44,E-08|1,56,E-08|1,96,E-07|4,65,E-08|
|AREA|SRC_368|Cam_Valpo_249-PEAS e Imp|267791|6398823|1 mes|466,56|3,27,E-08|7,92,E-09|3,59,E-09|4,50,E-08|1,07,E-08|
|AREA|SRC_369|Cam_Valpo_250-PEAS e Imp|267747|6398849|1 mes|204,00|7,49,E-08|1,81,E-08|8,21,E-09|1,03,E-07|2,45,E-08|
|AREA|SRC_370|Cam_Valpo_251-PEAS e Imp|267699|6398875|1 mes|217,15|7,04,E-08|1,70,E-08|7,71,E-09|9,67,E-08|2,30,E-08|
|AREA|SRC_371|Cam_Valpo_252-PEAS e Imp|267673|6398943|1 mes|285,91|5,34,E-08|1,29,E-08|5,85,E-09|7,35,E-08|1,75,E-08|
|AREA|SRC_372|Cam_Valpo_253-PEAS e Imp|267740|6399152|1 mes|871,99|1,75,E-08|4,24,E-09|1,92,E-09|2,41,E-08|5,73,E-09|
|AREA|SRC_373|Cam_Valpo_254-PEAS e Imp|267754|6399259|1 mes|434,37|3,52,E-08|8,51,E-09|3,85,E-09|4,84,E-08|1,15,E-08|
|AREA|SRC_374|Cam_Valpo_255-PEAS e Imp|267756|6399372|1 mes|452,93|3,37,E-08|8,16,E-09|3,70,E-09|4,64,E-08|1,10,E-08|
|AREA|SRC_375|Cam_Valpo_256-PEAS e Imp|267702|6399478|1 mes|480,03|3,18,E-08|7,70,E-09|3,49,E-09|4,38,E-08|1,04,E-08|
|AREA|SRC_376|Cam_Valpo_257-PEAS e Imp|267740|6399547|1 mes|307,21|4,97,E-08|1,20,E-08|5,45,E-09|6,84,E-08|1,63,E-08|
|AREA|SRC_377|Cam_Valpo_258-PEAS e Imp|267742|6399624|1 mes|311,56|4,90,E-08|1,19,E-08|5,37,E-09|6,74,E-08|1,60,E-08|
|AREA|SRC_378|Cam_Valpo_259-PEAS e Imp|267731|6399695|1 mes|287,58|5,31,E-08|1,29,E-08|5,82,E-09|7,30,E-08|1,74,E-08|
|AREA|SRC_379|Cam_Valpo_260-PEAS e Imp|267682|6399788|1 mes|425,70|3,59,E-08|8,68,E-09|3,93,E-09|4,93,E-08|1,17,E-08|
|AREA|SRC_380|Cam_Valpo_261-PEAS e Imp|267661|6399830|1 mes|187,04|8,17,E-08|1,98,E-08|8,95,E-09|1,12,E-07|2,67,E-08|

Tabla 97. Fuentes de Emisión - Escenario 2 parte 13

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/s]|[g/s]|[g/s]|[g/s]|[g/s]|
|VOLUMEN|SRC_26|Peas_6|271068|6383090|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_27|Peas_7|273479|6387274|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_28|Peas_8|273250|6387023|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_29|Imp_6|271083|6383208|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_30|Imp_6.1|271073|6383157|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_31|Imp_7.1|273426|6387238|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_32|Imp_7.2|273337|6387135|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_33|Imp_8.1|273075|6386932|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_34|Imp_8.2|272990|6386855|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 84. Fuentes de Emisión - Escenario 1 parte 28

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 206 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/s]|[g/s]|[g/s]|[g/s]|[g/s]|
|VOLUMEN|SRC_35|colec_6.1|270897|6383953|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_36|colec_6.2|270933|6383856|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_37|colec_6.3|270974|6383764|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_38|colec_6.4|271002|6383667|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_39|colec_6.5|271030|6383560|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_40|colec_6.6|271049|6383448|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_41|colec_6.7|271065|6383342|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_42|colec_6.8|271079|6383231|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_43|colec_6.9|271101|6383133|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_44|colec_6.10|271121|6383029|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_45|colec_6.11|271136|6382924|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_46|colec_6.12|271147|6382828|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_47|colec_6.13|271164|6382781|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_48|Colec_8.1|272916|6386820|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_49|Colec_8.2|272832|6386761|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_50|Colec_8.3|272733|6386713|1 mes|4,00|4,83,E-04|7,32,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|PUNTUAL|SRC_51|IF 1|272319|6384980|1 mes|0,05|7,32,E-03|1,77,E-03|0,00,E+00|2,08,E-01|4,49,E-02|
|PUNTUAL|SRC_52|IF 2|273522|6383276|1 mes|0,05|7,32,E-03|1,77,E-03|0,00,E+00|2,08,E-01|4,49,E-02|

**17.3 FUENTES DE EMISIÓN - ESCENARIO 3**

Tabla 99. Fuentes de Emisión - Escenario 3 parte 1

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_1|Peas_9|271160|6382780|1 mes|4,00|2,81,E-03|1,37,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_2|Peas_10|271257|6382753|1 mes|4,00|2,81,E-03|1,37,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_3|Imp_9|271319|6382719|1 mes|4,00|2,81,E-03|1,37,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_4|Imp_10.1|271266|6382656|1 mes|4,00|2,81,E-03|1,37,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_5|Imp_10.2|271215|6382599|1 mes|4,00|2,81,E-03|1,37,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_53|Cam_Cat_1-PEAS e Imp|273043|6387323|1 mes|383,32|6,48,E-09|1,57,E-09|1,31,E-09|1,80,E-08|4,29,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 100. Fuentes de Emisión - Escenario 3 parte 2

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 207 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_54|Cam_Cat_2-PEAS e Imp|273206|6387558|1 mes|1145,03|2,17,E-09|5,25,E-10|4,38,E-10|6,04,E-09|1,43,E-09|
|AREA|SRC_55|Cam_Cat_3-PEAS e Imp|273308|6387612|1 mes|456,00|5,45,E-09|1,32,E-09|1,10,E-09|1,52,E-08|3,60,E-09|
|AREA|SRC_56|Cam_Cat_4-PEAS e Imp|273511|6387668|1 mes|843,57|2,95,E-09|7,13,E-10|5,94,E-10|8,20,E-09|1,95,E-09|
|AREA|SRC_57|Cam_Cat_5-PEAS e Imp|273721|6387707|1 mes|853,32|2,91,E-09|7,05,E-10|5,87,E-10|8,10,E-09|1,93,E-09|
|AREA|SRC_58|Cam_Cat_6-PEAS e Imp|273880|6387880|1 mes|945,26|2,63,E-09|6,36,E-10|5,30,E-10|7,32,E-09|1,74,E-09|
|AREA|SRC_59|Cam_Cat_7-PEAS e Imp|273982|6387934|1 mes|457,52|5,43,E-09|1,31,E-09|1,10,E-09|1,51,E-08|3,59,E-09|
|AREA|SRC_60|Cam_Cat_8-PEAS e Imp|274178|6387916|1 mes|782,20|3,18,E-09|7,69,E-10|6,41,E-10|8,84,E-09|2,10,E-09|
|AREA|SRC_61|Cam_Cat_9-PEAS e Imp|274216|6387945|1 mes|195,48|1,27,E-08|3,08,E-09|2,56,E-09|3,54,E-08|8,40,E-09|
|AREA|SRC_62|Cam_Cat_10-PEAS e Imp|274213|6388017|1 mes|295,61|8,41,E-09|2,03,E-09|1,70,E-09|2,34,E-08|5,56,E-09|
|AREA|SRC_63|Cam_Cat_11-PEAS e Imp|274177|6388250|1 mes|941,53|2,64,E-09|6,39,E-10|5,32,E-10|7,34,E-09|1,74,E-09|
|AREA|SRC_64|Cam_Cat_12-PEAS e Imp|274185|6388365|1 mes|458,34|5,42,E-09|1,31,E-09|1,09,E-09|1,51,E-08|3,58,E-09|
|AREA|SRC_65|Cam_Cat_13-PEAS e Imp|274352|6388558|1 mes|1016,92|2,44,E-09|5,91,E-10|4,93,E-10|6,80,E-09|1,62,E-09|
|AREA|SRC_66|Cam_Cat_14-PEAS e Imp|274654|6388846|1 mes|1667,00|1,49,E-09|3,61,E-10|3,01,E-10|4,15,E-09|9,85,E-10|
|AREA|SRC_67|Cam_Cat_15-PEAS e Imp|274745|6388895|1 mes|409,81|6,07,E-09|1,47,E-09|1,22,E-09|1,69,E-08|4,01,E-09|
|AREA|SRC_68|Cam_Cat_16-PEAS e Imp|274834|6388862|1 mes|371,12|6,70,E-09|1,62,E-09|1,35,E-09|1,86,E-08|4,43,E-09|
|AREA|SRC_69|Cam_Cat_17-PEAS e Imp|274882|6388794|1 mes|331,29|7,50,E-09|1,82,E-09|1,51,E-09|2,09,E-08|4,96,E-09|
|AREA|SRC_70|Cam_Cat_18-PEAS e Imp|274979|6388768|1 mes|406,63|6,11,E-09|1,48,E-09|1,23,E-09|1,70,E-08|4,04,E-09|
|AREA|SRC_71|Cam_Cat_19-PEAS e Imp|275069|6388799|1 mes|384,16|6,47,E-09|1,57,E-09|1,30,E-09|1,80,E-08|4,28,E-09|
|AREA|SRC_72|Cam_Cat_20-PEAS e Imp|275059|6388911|1 mes|459,52|5,41,E-09|1,31,E-09|1,09,E-09|1,50,E-08|3,57,E-09|
|AREA|SRC_73|Cam_Cat_21-PEAS e Imp|275040|6389003|1 mes|374,05|6,64,E-09|1,61,E-09|1,34,E-09|1,85,E-08|4,39,E-09|
|AREA|SRC_74|Cam_Cat_22-PEAS e Imp|274958|6389092|1 mes|489,11|5,08,E-09|1,23,E-09|1,02,E-09|1,41,E-08|3,36,E-09|
|AREA|SRC_75|Cam_Cat_23-PEAS e Imp|274915|6389184|1 mes|402,20|6,18,E-09|1,50,E-09|1,25,E-09|1,72,E-08|4,08,E-09|
|AREA|SRC_76|Cam_Cat_24-PEAS e Imp|274946|6389307|1 mes|502,79|4,94,E-09|1,20,E-09|9,97,E-10|1,38,E-08|3,27,E-09|
|AREA|SRC_77|Cam_Cat_25-PEAS e Imp|275049|6389374|1 mes|485,06|5,12,E-09|1,24,E-09|1,03,E-09|1,43,E-08|3,39,E-09|
|AREA|SRC_78|Cam_Cat_26-PEAS e Imp|275181|6389406|1 mes|541,36|4,59,E-09|1,11,E-09|9,26,E-10|1,28,E-08|3,03,E-09|
|AREA|SRC_79|Cam_Cat_27-PEAS e Imp|275286|6389385|1 mes|424,34|5,86,E-09|1,42,E-09|1,18,E-09|1,63,E-08|3,87,E-09|
|AREA|SRC_80|Cam_Cat_28-PEAS e Imp|275372|6389387|1 mes|345,06|7,20,E-09|1,74,E-09|1,45,E-09|2,00,E-08|4,76,E-09|
|AREA|SRC_81|Cam_Cat_29-PEAS e Imp|275519|6389442|1 mes|633,26|3,93,E-09|9,50,E-10|7,91,E-10|1,09,E-08|2,59,E-09|
|AREA|SRC_82|Cam_Cat_30-PEAS e Imp|275575|6389512|1 mes|360,36|6,90,E-09|1,67,E-09|1,39,E-09|1,92,E-08|4,56,E-09|
|AREA|SRC_83|Cam_Cat_31-PEAS e Imp|275579|6389623|1 mes|447,31|5,56,E-09|1,34,E-09|1,12,E-09|1,55,E-08|3,67,E-09|
|AREA|SRC_84|Cam_Cat_32-PEAS e Imp|275473|6389738|1 mes|629,59|3,95,E-09|9,55,E-10|7,96,E-10|1,10,E-08|2,61,E-09|
|AREA|SRC_85|Cam_Cat_33-PEAS e Imp|275397|6389809|1 mes|419,18|5,93,E-09|1,43,E-09|1,20,E-09|1,65,E-08|3,92,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 101. Fuentes de Emisión - Escenario 3 parte 3

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 208 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_86|Cam_Cat_34-PEAS e Imp|275382|6389918|1 mes|432,78|5,74,E-09|1,39,E-09|1,16,E-09|1,60,E-08|3,80,E-09|
|AREA|SRC_87|Cam_Cat_35-PEAS e Imp|275487|6390018|1 mes|576,65|4,31,E-09|1,04,E-09|8,69,E-10|1,20,E-08|2,85,E-09|
|AREA|SRC_88|Cam_Cat_36-PEAS e Imp|275630|6390045|1 mes|576,34|4,31,E-09|1,04,E-09|8,69,E-10|1,20,E-08|2,85,E-09|
|AREA|SRC_89|Cam_Cat_37-PEAS e Imp|275763|6390025|1 mes|532,94|4,66,E-09|1,13,E-09|9,40,E-10|1,30,E-08|3,08,E-09|
|AREA|SRC_90|Cam_Cat_38-PEAS e Imp|275861|6389993|1 mes|411,71|6,04,E-09|1,46,E-09|1,22,E-09|1,68,E-08|3,99,E-09|
|AREA|SRC_91|Cam_Cat_39-PEAS e Imp|276044|6389963|1 mes|742,87|3,35,E-09|8,09,E-10|6,75,E-10|9,31,E-09|2,21,E-09|
|AREA|SRC_92|Cam_Cat_40-PEAS e Imp|276114|6389925|1 mes|316,96|7,84,E-09|1,90,E-09|1,58,E-09|2,18,E-08|5,18,E-09|
|AREA|SRC_93|Cam_Cat_41-PEAS e Imp|276133|6389885|1 mes|172,93|1,44,E-08|3,48,E-09|2,90,E-09|4,00,E-08|9,50,E-09|
|AREA|SRC_94|Cam_Cat_42-PEAS e Imp|276158|6389818|1 mes|286,84|8,67,E-09|2,10,E-09|1,75,E-09|2,41,E-08|5,73,E-09|
|AREA|SRC_95|Cam_Cat_43-PEAS e Imp|276157|6389659|1 mes|632,84|3,93,E-09|9,50,E-10|7,92,E-10|1,09,E-08|2,60,E-09|
|AREA|SRC_96|Cam_Cat_44-PEAS e Imp|276172|6389529|1 mes|521,10|4,77,E-09|1,15,E-09|9,62,E-10|1,33,E-08|3,15,E-09|
|AREA|SRC_97|Cam_Cat_45-PEAS e Imp|276275|6389477|1 mes|468,32|5,31,E-09|1,28,E-09|1,07,E-09|1,48,E-08|3,51,E-09|
|AREA|SRC_98|Cam_Cat_46-PEAS e Imp|276411|6389458|1 mes|553,37|4,49,E-09|1,09,E-09|9,06,E-10|1,25,E-08|2,97,E-09|
|AREA|SRC_99|Cam_Cat_47-PEAS e Imp|276501|6389471|1 mes|366,24|6,79,E-09|1,64,E-09|1,37,E-09|1,89,E-08|4,49,E-09|
|AREA|SRC_100|Cam_Cat_48-PEAS e Imp|276706|6389673|1 mes|1151,46|2,16,E-09|5,22,E-10|4,35,E-10|6,01,E-09|1,43,E-09|
|AREA|SRC_101|Cam_Cat_49-PEAS e Imp|277353|6390498|1 mes|4195,41|5,92,E-10|1,43,E-10|1,19,E-10|1,65,E-09|3,92,E-10|
|AREA|SRC_102|Cam_Cat_50-PEAS e Imp|277494|6390575|1 mes|640,03|3,88,E-09|9,40,E-10|7,83,E-10|1,08,E-08|2,57,E-09|
|AREA|SRC_103|Cam_Cat_51-PEAS e Imp|279440|6391244|1 mes|8223,68|3,02,E-10|7,31,E-11|6,09,E-11|8,41,E-10|2,00,E-10|
|AREA|SRC_104|Cam_Cat_52-PEAS e Imp|283346|6393239|1 mes|17540,88|1,42,E-10|3,43,E-11|2,86,E-11|3,94,E-10|9,36,E-11|
|AREA|SRC_105|Cam_Cat_53-PEAS e Imp|287745|6394661|1 mes|18483,13|1,34,E-10|3,25,E-11|2,71,E-11|3,74,E-10|8,89,E-11|
|AREA|SRC_106|Cam_Pta_1-PEAS e Imp|273147|6383634|1 mes|1866,42|1,33,E-09|3,22,E-10|2,68,E-10|3,71,E-09|8,80,E-10|
|AREA|SRC_107|Cam_Pta_2-PEAS e Imp|273165|6383642|1 mes|80,85|3,07,E-08|7,44,E-09|6,20,E-09|8,55,E-08|2,03,E-08|
|AREA|SRC_108|Cam_Pta_3-PEAS e Imp|273189|6383637|1 mes|94,14|2,64,E-08|6,39,E-09|5,32,E-09|7,35,E-08|1,74,E-08|
|AREA|SRC_109|Cam_Pta_4-PEAS e Imp|273241|6383562|1 mes|359,95|6,91,E-09|1,67,E-09|1,39,E-09|1,92,E-08|4,56,E-09|
|AREA|SRC_110|Cam_Pta_5-PEAS e Imp|273289|6383445|1 mes|505,57|4,92,E-09|1,19,E-09|9,91,E-10|1,37,E-08|3,25,E-09|
|AREA|SRC_111|Cam_Pta_6-PEAS e Imp|273304|6383402|1 mes|179,62|1,38,E-08|3,35,E-09|2,79,E-09|3,85,E-08|9,15,E-09|
|AREA|SRC_112|Cam_Pta_7-PEAS e Imp|273331|6383382|1 mes|138,45|1,80,E-08|4,34,E-09|3,62,E-09|4,99,E-08|1,19,E-08|
|AREA|SRC_113|Cam_Pta_8-PEAS e Imp|273361|6383362|1 mes|145,56|1,71,E-08|4,13,E-09|3,44,E-09|4,75,E-08|1,13,E-08|
|AREA|SRC_114|Cam_Pta_9-PEAS e Imp|273393|6383346|1 mes|143,99|1,73,E-08|4,18,E-09|3,48,E-09|4,80,E-08|1,14,E-08|
|AREA|SRC_115|Cam_Pta_10-PEAS e Imp|273413|6383324|1 mes|116,32|2,14,E-08|5,17,E-09|4,31,E-09|5,95,E-08|1,41,E-08|
|AREA|SRC_116|Cam_Pta_11-PEAS e Imp|273447|6383229|1 mes|400,03|6,21,E-09|1,50,E-09|1,25,E-09|1,73,E-08|4,11,E-09|
|AREA|SRC_117|Cam_Pta_12-PEAS e Imp|273463|6383220|1 mes|80,13|3,10,E-08|7,50,E-09|6,25,E-09|8,63,E-08|2,05,E-08|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 102. Fuentes de Emisión - Escenario 3 parte 4

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 209 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_118|Cam_Pta_13-PEAS e Imp|273473|6383218|1 mes|45,12|5,51,E-08|1,33,E-08|1,11,E-08|1,53,E-07|3,64,E-08|
|AREA|SRC_119|Cam_Pta_14-PEAS e Imp|273519|6383228|1 mes|188,53|1,32,E-08|3,19,E-09|2,66,E-09|3,67,E-08|8,71,E-09|
|AREA|SRC_120|Cam_Valpo_1-PEAS e Imp|267407|6370003|1 mes|9181,86|2,71,E-10|6,55,E-11|5,46,E-11|7,53,E-10|1,79,E-10|
|AREA|SRC_121|Cam_Valpo_2-PEAS e Imp|267402|6370088|1 mes|338,29|7,35,E-09|1,78,E-09|1,48,E-09|2,04,E-08|4,86,E-09|
|AREA|SRC_122|Cam_Valpo_3-PEAS e Imp|267699|6371506|1 mes|5788,94|4,29,E-10|1,04,E-10|8,66,E-11|1,19,E-09|2,84,E-10|
|AREA|SRC_123|Cam_Valpo_4-PEAS e Imp|267700|6371619|1 mes|452,00|5,50,E-09|1,33,E-09|1,11,E-09|1,53,E-08|3,63,E-09|
|AREA|SRC_124|Cam_Valpo_5-PEAS e Imp|267517|6371917|1 mes|1401,44|1,77,E-09|4,29,E-10|3,58,E-10|4,93,E-09|1,17,E-09|
|AREA|SRC_125|Cam_Valpo_6-PEAS e Imp|267499|6371980|1 mes|261,10|9,52,E-09|2,30,E-09|1,92,E-09|2,65,E-08|6,29,E-09|
|AREA|SRC_126|Cam_Valpo_7-PEAS e Imp|267496|6372042|1 mes|247,03|1,01,E-08|2,43,E-09|2,03,E-09|2,80,E-08|6,65,E-09|
|AREA|SRC_127|Cam_Valpo_8-PEAS e Imp|267518|6372113|1 mes|294,47|8,44,E-09|2,04,E-09|1,70,E-09|2,35,E-08|5,58,E-09|
|AREA|SRC_128|Cam_Valpo_9-PEAS e Imp|267547|6372151|1 mes|187,43|1,33,E-08|3,21,E-09|2,67,E-09|3,69,E-08|8,76,E-09|
|AREA|SRC_129|Cam_Valpo_10-PEAS e Imp|267569|6372177|1 mes|137,02|1,81,E-08|4,39,E-09|3,66,E-09|5,05,E-08|1,20,E-08|
|AREA|SRC_130|Cam_Valpo_11-PEAS e Imp|267738|6372319|1 mes|879,83|2,83,E-09|6,83,E-10|5,70,E-10|7,86,E-09|1,87,E-09|
|AREA|SRC_131|Cam_Valpo_12-PEAS e Imp|267762|6372358|1 mes|186,57|1,33,E-08|3,22,E-09|2,69,E-09|3,71,E-08|8,80,E-09|
|AREA|SRC_132|Cam_Valpo_13-PEAS e Imp|267783|6372410|1 mes|224,51|1,11,E-08|2,68,E-09|2,23,E-09|3,08,E-08|7,32,E-09|
|AREA|SRC_133|Cam_Valpo_14-PEAS e Imp|267855|6372669|1 mes|1075,61|2,31,E-09|5,59,E-10|4,66,E-10|6,43,E-09|1,53,E-09|
|AREA|SRC_134|Cam_Valpo_15-PEAS e Imp|267848|6372720|1 mes|207,78|1,20,E-08|2,89,E-09|2,41,E-09|3,33,E-08|7,91,E-09|
|AREA|SRC_135|Cam_Valpo_16-PEAS e Imp|267715|6373066|1 mes|1484,08|1,67,E-09|4,05,E-10|3,38,E-10|4,66,E-09|1,11,E-09|
|AREA|SRC_136|Cam_Valpo_17-PEAS e Imp|267705|6373122|1 mes|225,43|1,10,E-08|2,67,E-09|2,22,E-09|3,07,E-08|7,29,E-09|
|AREA|SRC_137|Cam_Valpo_18-PEAS e Imp|267701|6373182|1 mes|241,22|1,03,E-08|2,49,E-09|2,08,E-09|2,87,E-08|6,81,E-09|
|AREA|SRC_138|Cam_Valpo_19-PEAS e Imp|267704|6373237|1 mes|217,96|1,14,E-08|2,76,E-09|2,30,E-09|3,17,E-08|7,54,E-09|
|AREA|SRC_139|Cam_Valpo_20-PEAS e Imp|267713|6373309|1 mes|291,26|8,53,E-09|2,06,E-09|1,72,E-09|2,37,E-08|5,64,E-09|
|AREA|SRC_140|Cam_Valpo_21-PEAS e Imp|267741|6373522|1 mes|860,16|2,89,E-09|6,99,E-10|5,83,E-10|8,04,E-09|1,91,E-09|
|AREA|SRC_141|Cam_Valpo_22-PEAS e Imp|267757|6373574|1 mes|213,85|1,16,E-08|2,81,E-09|2,34,E-09|3,23,E-08|7,68,E-09|
|AREA|SRC_142|Cam_Valpo_23-PEAS e Imp|267777|6373617|1 mes|187,32|1,33,E-08|3,21,E-09|2,68,E-09|3,69,E-08|8,77,E-09|
|AREA|SRC_143|Cam_Valpo_24-PEAS e Imp|267817|6373719|1 mes|441,14|5,63,E-09|1,36,E-09|1,14,E-09|1,57,E-08|3,72,E-09|
|AREA|SRC_144|Cam_Valpo_25-PEAS e Imp|267843|6373782|1 mes|272,58|9,12,E-09|2,21,E-09|1,84,E-09|2,54,E-08|6,03,E-09|
|AREA|SRC_145|Cam_Valpo_26-PEAS e Imp|267877|6373831|1 mes|236,03|1,05,E-08|2,55,E-09|2,12,E-09|2,93,E-08|6,96,E-09|
|AREA|SRC_146|Cam_Valpo_27-PEAS e Imp|267910|6373883|1 mes|246,12|1,01,E-08|2,44,E-09|2,04,E-09|2,81,E-08|6,67,E-09|
|AREA|SRC_147|Cam_Valpo_28-PEAS e Imp|268105|6374174|1 mes|1399,53|1,78,E-09|4,30,E-10|3,58,E-10|4,94,E-09|1,17,E-09|
|AREA|SRC_148|Cam_Valpo_29-PEAS e Imp|268274|6374430|1 mes|1228,07|2,02,E-09|4,90,E-10|4,08,E-10|5,63,E-09|1,34,E-09|
|AREA|SRC_149|Cam_Valpo_30-PEAS e Imp|268317|6374478|1 mes|254,35|9,77,E-09|2,36,E-09|1,97,E-09|2,72,E-08|6,46,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 103. Fuentes de Emisión - Escenario 3 parte 5

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 210 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_150|Cam_Valpo_31-PEAS e Imp|268347|6374502|1 mes|154,46|1,61,E-08|3,89,E-09|3,24,E-09|4,48,E-08|1,06,E-08|
|AREA|SRC_151|Cam_Valpo_32-PEAS e Imp|269602|6375295|1 mes|5935,56|4,19,E-10|1,01,E-10|8,44,E-11|1,17,E-09|2,77,E-10|
|AREA|SRC_152|Cam_Valpo_33-PEAS e Imp|270646|6375956|1 mes|4938,33|5,03,E-10|1,22,E-10|1,01,E-10|1,40,E-09|3,33,E-10|
|AREA|SRC_153|Cam_Valpo_34-PEAS e Imp|270700|6375970|1 mes|220,74|1,13,E-08|2,72,E-09|2,27,E-09|3,13,E-08|7,44,E-09|
|AREA|SRC_154|Cam_Valpo_35-PEAS e Imp|270759|6375972|1 mes|232,03|1,07,E-08|2,59,E-09|2,16,E-09|2,98,E-08|7,08,E-09|
|AREA|SRC_155|Cam_Valpo_36-PEAS e Imp|270817|6375960|1 mes|237,83|1,05,E-08|2,53,E-09|2,11,E-09|2,91,E-08|6,91,E-09|
|AREA|SRC_156|Cam_Valpo_37-PEAS e Imp|271210|6375788|1 mes|1710,95|1,45,E-09|3,51,E-10|2,93,E-10|4,04,E-09|9,60,E-10|
|AREA|SRC_157|Cam_Valpo_38-PEAS e Imp|271299|6375786|1 mes|362,06|6,87,E-09|1,66,E-09|1,38,E-09|1,91,E-08|4,54,E-09|
|AREA|SRC_158|Cam_Valpo_39-PEAS e Imp|271410|6375784|1 mes|444,09|5,60,E-09|1,35,E-09|1,13,E-09|1,56,E-08|3,70,E-09|
|AREA|SRC_159|Cam_Valpo_40-PEAS e Imp|271537|6375829|1 mes|539,94|4,60,E-09|1,11,E-09|9,28,E-10|1,28,E-08|3,04,E-09|
|AREA|SRC_160|Cam_Valpo_41-PEAS e Imp|271698|6375908|1 mes|717,64|3,46,E-09|8,38,E-10|6,98,E-10|9,64,E-09|2,29,E-09|
|AREA|SRC_161|Cam_Valpo_42-PEAS e Imp|271943|6376040|1 mes|1111,41|2,24,E-09|5,41,E-10|4,51,E-10|6,22,E-09|1,48,E-09|
|AREA|SRC_162|Cam_Valpo_43-PEAS e Imp|272216|6376245|1 mes|1365,82|1,82,E-09|4,40,E-10|3,67,E-10|5,06,E-09|1,20,E-09|
|AREA|SRC_163|Cam_Valpo_44-PEAS e Imp|272308|6376283|1 mes|396,81|6,26,E-09|1,52,E-09|1,26,E-09|1,74,E-08|4,14,E-09|
|AREA|SRC_164|Cam_Valpo_45-PEAS e Imp|272828|6376412|1 mes|2139,51|1,16,E-09|2,81,E-10|2,34,E-10|3,23,E-09|7,68,E-10|
|AREA|SRC_165|Cam_Valpo_46-PEAS e Imp|272961|6376463|1 mes|572,90|4,34,E-09|1,05,E-09|8,75,E-10|1,21,E-08|2,87,E-09|
|AREA|SRC_166|Cam_Valpo_47-PEAS e Imp|273101|6376548|1 mes|656,43|3,79,E-09|9,16,E-10|7,63,E-10|1,05,E-08|2,50,E-09|
|AREA|SRC_167|Cam_Valpo_48-PEAS e Imp|273683|6376890|1 mes|2699,98|9,21,E-10|2,23,E-10|1,86,E-10|2,56,E-09|6,08,E-10|
|AREA|SRC_168|Cam_Valpo_49-PEAS e Imp|273729|6376911|1 mes|198,66|1,25,E-08|3,03,E-09|2,52,E-09|3,48,E-08|8,27,E-09|
|AREA|SRC_169|Cam_Valpo_50-PEAS e Imp|273841|6376934|1 mes|455,50|5,46,E-09|1,32,E-09|1,10,E-09|1,52,E-08|3,61,E-09|
|AREA|SRC_170|Cam_Valpo_51-PEAS e Imp|273918|6376948|1 mes|314,84|7,89,E-09|1,91,E-09|1,59,E-09|2,20,E-08|5,22,E-09|
|AREA|SRC_171|Cam_Valpo_52-PEAS e Imp|273963|6376959|1 mes|182,29|1,36,E-08|3,30,E-09|2,75,E-09|3,79,E-08|9,01,E-09|
|AREA|SRC_172|Cam_Valpo_53-PEAS e Imp|274013|6376981|1 mes|220,22|1,13,E-08|2,73,E-09|2,28,E-09|3,14,E-08|7,46,E-09|
|AREA|SRC_173|Cam_Valpo_54-PEAS e Imp|274045|6377010|1 mes|175,74|1,41,E-08|3,42,E-09|2,85,E-09|3,93,E-08|9,35,E-09|
|AREA|SRC_174|Cam_Valpo_55-PEAS e Imp|274402|6377569|1 mes|2654,98|9,36,E-10|2,27,E-10|1,89,E-10|2,60,E-09|6,19,E-10|
|AREA|SRC_175|Cam_Valpo_56-PEAS e Imp|274508|6377712|1 mes|712,20|3,49,E-09|8,44,E-10|7,04,E-10|9,71,E-09|2,31,E-09|
|AREA|SRC_176|Cam_Valpo_57-PEAS e Imp|274515|6377737|1 mes|105,54|2,36,E-08|5,70,E-09|4,75,E-09|6,55,E-08|1,56,E-08|
|AREA|SRC_177|Cam_Valpo_58-PEAS e Imp|274530|6377783|1 mes|190,85|1,30,E-08|3,15,E-09|2,63,E-09|3,62,E-08|8,61,E-09|
|AREA|SRC_178|Cam_Valpo_59-PEAS e Imp|274571|6378190|1 mes|1640,54|1,52,E-09|3,67,E-10|3,05,E-10|4,22,E-09|1,00,E-09|
|AREA|SRC_179|Cam_Valpo_60-PEAS e Imp|274512|6378662|1 mes|1902,24|1,31,E-09|3,16,E-10|2,63,E-10|3,64,E-09|8,64,E-10|
|AREA|SRC_180|Cam_Valpo_61-PEAS e Imp|274484|6378742|1 mes|339,36|7,32,E-09|1,77,E-09|1,48,E-09|2,04,E-08|4,84,E-09|
|AREA|SRC_181|Cam_Valpo_62-PEAS e Imp|274397|6378959|1 mes|934,88|2,66,E-09|6,43,E-10|5,36,E-10|7,40,E-09|1,76,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 104. Fuentes de Emisión - Escenario 3 parte 6

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 211 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_182|Cam_Valpo_63-PEAS e Imp|274391|6379006|1 mes|189,58|1,31,E-08|3,17,E-09|2,64,E-09|3,65,E-08|8,66,E-09|
|AREA|SRC_183|Cam_Valpo_64-PEAS e Imp|274392|6379034|1 mes|109,49|2,27,E-08|5,49,E-09|4,58,E-09|6,32,E-08|1,50,E-08|
|AREA|SRC_184|Cam_Valpo_65-PEAS e Imp|274513|6379469|1 mes|1805,57|1,38,E-09|3,33,E-10|2,78,E-10|3,83,E-09|9,10,E-10|
|AREA|SRC_185|Cam_Valpo_66-PEAS e Imp|274514|6379510|1 mes|163,36|1,52,E-08|3,68,E-09|3,07,E-09|4,23,E-08|1,01,E-08|
|AREA|SRC_186|Cam_Valpo_67-PEAS e Imp|274503|6379560|1 mes|208,73|1,19,E-08|2,88,E-09|2,40,E-09|3,31,E-08|7,87,E-09|
|AREA|SRC_187|Cam_Valpo_68-PEAS e Imp|274488|6379623|1 mes|255,44|9,73,E-09|2,35,E-09|1,96,E-09|2,71,E-08|6,43,E-09|
|AREA|SRC_188|Cam_Valpo_69-PEAS e Imp|274426|6379798|1 mes|745,56|3,33,E-09|8,07,E-10|6,72,E-10|9,28,E-09|2,20,E-09|
|AREA|SRC_189|Cam_Valpo_70-PEAS e Imp|274386|6379897|1 mes|428,53|5,80,E-09|1,40,E-09|1,17,E-09|1,61,E-08|3,83,E-09|
|AREA|SRC_190|Cam_Valpo_71-PEAS e Imp|274352|6379981|1 mes|360,23|6,90,E-09|1,67,E-09|1,39,E-09|1,92,E-08|4,56,E-09|
|AREA|SRC_191|Cam_Valpo_72-PEAS e Imp|274336|6380041|1 mes|249,49|9,96,E-09|2,41,E-09|2,01,E-09|2,77,E-08|6,58,E-09|
|AREA|SRC_192|Cam_Valpo_73-PEAS e Imp|274333|6380099|1 mes|227,80|1,09,E-08|2,64,E-09|2,20,E-09|3,04,E-08|7,21,E-09|
|AREA|SRC_193|Cam_Valpo_74-PEAS e Imp|274332|6380163|1 mes|257,27|9,66,E-09|2,34,E-09|1,95,E-09|2,69,E-08|6,38,E-09|
|AREA|SRC_194|Cam_Valpo_75-PEAS e Imp|274329|6380546|1 mes|1530,44|1,62,E-09|3,93,E-10|3,27,E-10|4,52,E-09|1,07,E-09|
|AREA|SRC_195|Cam_Valpo_76-PEAS e Imp|274323|6380578|1 mes|130,55|1,90,E-08|4,61,E-09|3,84,E-09|5,30,E-08|1,26,E-08|
|AREA|SRC_196|Cam_Valpo_77-PEAS e Imp|274308|6380608|1 mes|138,17|1,80,E-08|4,35,E-09|3,63,E-09|5,00,E-08|1,19,E-08|
|AREA|SRC_197|Cam_Valpo_78-PEAS e Imp|274078|6381086|1 mes|2120,50|1,17,E-09|2,84,E-10|2,36,E-10|3,26,E-09|7,75,E-10|
|AREA|SRC_198|Cam_Valpo_79-PEAS e Imp|274036|6381146|1 mes|292,96|8,48,E-09|2,05,E-09|1,71,E-09|2,36,E-08|5,61,E-09|
|AREA|SRC_199|Cam_Valpo_80-PEAS e Imp|273997|6381192|1 mes|242,71|1,02,E-08|2,48,E-09|2,06,E-09|2,85,E-08|6,77,E-09|
|AREA|SRC_200|Cam_Valpo_81-PEAS e Imp|273945|6381212|1 mes|225,25|1,10,E-08|2,67,E-09|2,22,E-09|3,07,E-08|7,29,E-09|
|AREA|SRC_201|Cam_Valpo_82-PEAS e Imp|273863|6381235|1 mes|340,59|7,30,E-09|1,77,E-09|1,47,E-09|2,03,E-08|4,82,E-09|
|AREA|SRC_202|Cam_Valpo_83-PEAS e Imp|273527|6381309|1 mes|1376,67|1,81,E-09|4,37,E-10|3,64,E-10|5,02,E-09|1,19,E-09|
|AREA|SRC_203|Cam_Valpo_84-PEAS e Imp|273488|6381317|1 mes|158,83|1,56,E-08|3,79,E-09|3,15,E-09|4,35,E-08|1,03,E-08|
|AREA|SRC_204|Cam_Valpo_85-PEAS e Imp|273437|6381311|1 mes|210,61|1,18,E-08|2,86,E-09|2,38,E-09|3,28,E-08|7,80,E-09|
|AREA|SRC_205|Cam_Valpo_86-PEAS e Imp|273400|6381306|1 mes|148,75|1,67,E-08|4,04,E-09|3,37,E-09|4,65,E-08|1,10,E-08|
|AREA|SRC_206|Cam_Valpo_87-PEAS e Imp|273330|6381278|1 mes|302,02|8,23,E-09|1,99,E-09|1,66,E-09|2,29,E-08|5,44,E-09|
|AREA|SRC_207|Cam_Valpo_88-PEAS e Imp|273269|6381275|1 mes|240,32|1,03,E-08|2,50,E-09|2,09,E-09|2,88,E-08|6,84,E-09|
|AREA|SRC_208|Cam_Valpo_89-PEAS e Imp|273210|6381284|1 mes|238,69|1,04,E-08|2,52,E-09|2,10,E-09|2,90,E-08|6,88,E-09|
|AREA|SRC_209|Cam_Valpo_90-PEAS e Imp|273140|6381307|1 mes|291,89|8,52,E-09|2,06,E-09|1,72,E-09|2,37,E-08|5,63,E-09|
|AREA|SRC_210|Cam_Valpo_91-PEAS e Imp|273026|6381364|1 mes|510,61|4,87,E-09|1,18,E-09|9,81,E-10|1,35,E-08|3,22,E-09|
|AREA|SRC_211|Cam_Valpo_92-PEAS e Imp|272787|6381471|1 mes|1046,47|2,38,E-09|5,75,E-10|4,79,E-10|6,61,E-09|1,57,E-09|
|AREA|SRC_212|Cam_Valpo_93-PEAS e Imp|272625|6381553|1 mes|726,81|3,42,E-09|8,27,E-10|6,89,E-10|9,51,E-09|2,26,E-09|
|AREA|SRC_213|Cam_Valpo_94-PEAS e Imp|272586|6381587|1 mes|205,87|1,21,E-08|2,92,E-09|2,43,E-09|3,36,E-08|7,98,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 105. Fuentes de Emisión - Escenario 3 parte 7

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 212 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_214|Cam_Valpo_95-PEAS e Imp|272567|6381621|1 mes|150,25|1,65,E-08|4,00,E-09|3,34,E-09|4,60,E-08|1,09,E-08|
|AREA|SRC_215|Cam_Valpo_96-PEAS e Imp|272558|6381659|1 mes|154,59|1,61,E-08|3,89,E-09|3,24,E-09|4,47,E-08|1,06,E-08|
|AREA|SRC_216|Cam_Valpo_97-PEAS e Imp|272513|6381931|1 mes|1103,20|2,25,E-09|5,45,E-10|4,54,E-10|6,27,E-09|1,49,E-09|
|AREA|SRC_217|Cam_Valpo_98-PEAS e Imp|272500|6382030|1 mes|398,37|6,24,E-09|1,51,E-09|1,26,E-09|1,74,E-08|4,12,E-09|
|AREA|SRC_218|Cam_Valpo_99-PEAS e Imp|272492|6382086|1 mes|223,87|1,11,E-08|2,69,E-09|2,24,E-09|3,09,E-08|7,34,E-09|
|AREA|SRC_219|Cam_Valpo_100-PEAS e Imp|272491|6382127|1 mes|164,32|1,51,E-08|3,66,E-09|3,05,E-09|4,21,E-08|1,00,E-08|
|AREA|SRC_220|Cam_Valpo_101-PEAS e Imp|272506|6382188|1 mes|247,33|1,00,E-08|2,43,E-09|2,03,E-09|2,80,E-08|6,64,E-09|
|AREA|SRC_221|Cam_Valpo_102-PEAS e Imp|272660|6383439|1 mes|5043,31|4,93,E-10|1,19,E-10|9,94,E-11|1,37,E-09|3,26,E-10|
|AREA|SRC_222|Cam_Valpo_103-PEAS e Imp|272630|6384559|1 mes|4478,91|5,55,E-10|1,34,E-10|1,12,E-10|1,54,E-09|3,67,E-10|
|AREA|SRC_223|Cam_Valpo_104-PEAS e Imp|272626|6385227|1 mes|2671,08|9,31,E-10|2,25,E-10|1,88,E-10|2,59,E-09|6,15,E-10|
|AREA|SRC_224|Cam_Valpo_105-PEAS e Imp|272602|6386454|1 mes|4905,80|5,07,E-10|1,23,E-10|1,02,E-10|1,41,E-09|3,35,E-10|
|AREA|SRC_225|Cam_Valpo_106-PEAS e Imp|272609|6386527|1 mes|292,53|8,50,E-09|2,06,E-09|1,71,E-09|2,36,E-08|5,62,E-09|
|AREA|SRC_226|Cam_Valpo_107-PEAS e Imp|272650|6386615|1 mes|384,69|6,46,E-09|1,56,E-09|1,30,E-09|1,80,E-08|4,27,E-09|
|AREA|SRC_227|Cam_Valpo_108-PEAS e Imp|272755|6386705|1 mes|550,00|4,52,E-09|1,09,E-09|9,11,E-10|1,26,E-08|2,99,E-09|
|AREA|SRC_228|Cam_Valpo_109-PEAS e Imp|272846|6386776|1 mes|460,85|5,39,E-09|1,30,E-09|1,09,E-09|1,50,E-08|3,56,E-09|
|AREA|SRC_229|Cam_Valpo_110-PEAS e Imp|272918|6386821|1 mes|338,79|7,34,E-09|1,77,E-09|1,48,E-09|2,04,E-08|4,85,E-09|
|AREA|SRC_230|Cam_Valpo_111-PEAS e Imp|272959|6386856|1 mes|215,71|1,15,E-08|2,79,E-09|2,32,E-09|3,21,E-08|7,62,E-09|
|AREA|SRC_231|Cam_Valpo_112-PEAS e Imp|272979|6386909|1 mes|229,32|1,08,E-08|2,62,E-09|2,19,E-09|3,02,E-08|7,16,E-09|
|AREA|SRC_232|Cam_Valpo_113-PEAS e Imp|272982|6386950|1 mes|168,20|1,48,E-08|3,58,E-09|2,98,E-09|4,11,E-08|9,77,E-09|
|AREA|SRC_233|Cam_Valpo_114-PEAS e Imp|272974|6387033|1 mes|334,56|7,43,E-09|1,80,E-09|1,50,E-09|2,07,E-08|4,91,E-09|
|AREA|SRC_234|Cam_Valpo_115-PEAS e Imp|272969|6387289|1 mes|1021,26|2,43,E-09|5,89,E-10|4,91,E-10|6,77,E-09|1,61,E-09|
|AREA|SRC_235|Cam_Valpo_116-PEAS e Imp|272950|6387316|1 mes|135,86|1,83,E-08|4,43,E-09|3,69,E-09|5,09,E-08|1,21,E-08|
|AREA|SRC_236|Cam_Valpo_117-PEAS e Imp|272918|6387332|1 mes|150,62|1,65,E-08|3,99,E-09|3,33,E-09|4,59,E-08|1,09,E-08|
|AREA|SRC_237|Cam_Valpo_118-PEAS e Imp|272871|6387328|1 mes|193,11|1,29,E-08|3,11,E-09|2,59,E-09|3,58,E-08|8,51,E-09|
|AREA|SRC_238|Cam_Valpo_119-PEAS e Imp|272818|6387319|1 mes|214,82|1,16,E-08|2,80,E-09|2,33,E-09|3,22,E-08|7,65,E-09|
|AREA|SRC_239|Cam_Valpo_120-PEAS e Imp|272669|6387324|1 mes|593,51|4,19,E-09|1,01,E-09|8,44,E-10|1,17,E-08|2,77,E-09|
|AREA|SRC_240|Cam_Valpo_121-PEAS e Imp|272536|6387380|1 mes|574,11|4,33,E-09|1,05,E-09|8,73,E-10|1,20,E-08|2,86,E-09|
|AREA|SRC_241|Cam_Valpo_122-PEAS e Imp|272406|6387475|1 mes|642,85|3,87,E-09|9,35,E-10|7,79,E-10|1,08,E-08|2,56,E-09|
|AREA|SRC_242|Cam_Valpo_123-PEAS e Imp|272321|6387544|1 mes|438,86|5,66,E-09|1,37,E-09|1,14,E-09|1,58,E-08|3,74,E-09|
|AREA|SRC_243|Cam_Valpo_124-PEAS e Imp|272252|6387605|1 mes|366,01|6,79,E-09|1,64,E-09|1,37,E-09|1,89,E-08|4,49,E-09|
|AREA|SRC_244|Cam_Valpo_125-PEAS e Imp|272138|6387749|1 mes|733,97|3,39,E-09|8,19,E-10|6,83,E-10|9,42,E-09|2,24,E-09|
|AREA|SRC_245|Cam_Valpo_126-PEAS e Imp|272059|6387890|1 mes|645,70|3,85,E-09|9,31,E-10|7,76,E-10|1,07,E-08|2,54,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 106. Fuentes de Emisión - Escenario 3 parte 8

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 213 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_246|Cam_Valpo_127-PEAS e Imp|272019|6388008|1 mes|494,29|5,03,E-09|1,22,E-09|1,01,E-09|1,40,E-08|3,32,E-09|
|AREA|SRC_247|Cam_Valpo_128-PEAS e Imp|272005|6388086|1 mes|318,17|7,81,E-09|1,89,E-09|1,57,E-09|2,17,E-08|5,16,E-09|
|AREA|SRC_248|Cam_Valpo_129-PEAS e Imp|272005|6388171|1 mes|338,40|7,35,E-09|1,78,E-09|1,48,E-09|2,04,E-08|4,85,E-09|
|AREA|SRC_249|Cam_Valpo_130-PEAS e Imp|272018|6388207|1 mes|149,40|1,66,E-08|4,03,E-09|3,35,E-09|4,63,E-08|1,10,E-08|
|AREA|SRC_250|Cam_Valpo_131-PEAS e Imp|272053|6388222|1 mes|144,57|1,72,E-08|4,16,E-09|3,47,E-09|4,78,E-08|1,14,E-08|
|AREA|SRC_251|Cam_Valpo_132-PEAS e Imp|272113|6388260|1 mes|286,19|8,68,E-09|2,10,E-09|1,75,E-09|2,42,E-08|5,74,E-09|
|AREA|SRC_252|Cam_Valpo_133-PEAS e Imp|272165|6388289|1 mes|236,50|1,05,E-08|2,54,E-09|2,12,E-09|2,92,E-08|6,95,E-09|
|AREA|SRC_253|Cam_Valpo_134-PEAS e Imp|272170|6388313|1 mes|103,04|2,41,E-08|5,84,E-09|4,86,E-09|6,71,E-08|1,59,E-08|
|AREA|SRC_254|Cam_Valpo_135-PEAS e Imp|272160|6388355|1 mes|178,67|1,39,E-08|3,37,E-09|2,80,E-09|3,87,E-08|9,19,E-09|
|AREA|SRC_255|Cam_Valpo_136-PEAS e Imp|272116|6388384|1 mes|213,17|1,17,E-08|2,82,E-09|2,35,E-09|3,24,E-08|7,71,E-09|
|AREA|SRC_256|Cam_Valpo_137-PEAS e Imp|271990|6388473|1 mes|618,26|4,02,E-09|9,73,E-10|8,11,E-10|1,12,E-08|2,66,E-09|
|AREA|SRC_257|Cam_Valpo_138-PEAS e Imp|271909|6388570|1 mes|502,24|4,95,E-09|1,20,E-09|9,98,E-10|1,38,E-08|3,27,E-09|
|AREA|SRC_258|Cam_Valpo_139-PEAS e Imp|271887|6388631|1 mes|257,67|9,65,E-09|2,33,E-09|1,94,E-09|2,68,E-08|6,38,E-09|
|AREA|SRC_259|Cam_Valpo_140-PEAS e Imp|271869|6388710|1 mes|324,57|7,66,E-09|1,85,E-09|1,54,E-09|2,13,E-08|5,06,E-09|
|AREA|SRC_260|Cam_Valpo_141-PEAS e Imp|271879|6388778|1 mes|270,72|9,18,E-09|2,22,E-09|1,85,E-09|2,55,E-08|6,07,E-09|
|AREA|SRC_261|Cam_Valpo_142-PEAS e Imp|271889|6388831|1 mes|215,81|1,15,E-08|2,79,E-09|2,32,E-09|3,20,E-08|7,61,E-09|
|AREA|SRC_262|Cam_Valpo_143-PEAS e Imp|271888|6388910|1 mes|317,54|7,83,E-09|1,89,E-09|1,58,E-09|2,18,E-08|5,17,E-09|
|AREA|SRC_263|Cam_Valpo_144-PEAS e Imp|271765|6389249|1 mes|1443,83|1,72,E-09|4,16,E-10|3,47,E-10|4,79,E-09|1,14,E-09|
|AREA|SRC_264|Cam_Valpo_145-PEAS e Imp|271745|6389323|1 mes|308,68|8,05,E-09|1,95,E-09|1,62,E-09|2,24,E-08|5,32,E-09|
|AREA|SRC_265|Cam_Valpo_146-PEAS e Imp|271746|6389404|1 mes|321,13|7,74,E-09|1,87,E-09|1,56,E-09|2,15,E-08|5,12,E-09|
|AREA|SRC_266|Cam_Valpo_147-PEAS e Imp|271745|6389713|1 mes|1235,33|2,01,E-09|4,87,E-10|4,06,E-10|5,60,E-09|1,33,E-09|
|AREA|SRC_267|Cam_Valpo_148-PEAS e Imp|271729|6389779|1 mes|274,74|9,05,E-09|2,19,E-09|1,82,E-09|2,52,E-08|5,98,E-09|
|AREA|SRC_268|Cam_Valpo_149-PEAS e Imp|271405|6390771|1 mes|4169,69|5,96,E-10|1,44,E-10|1,20,E-10|1,66,E-09|3,94,E-10|
|AREA|SRC_269|Cam_Valpo_150-PEAS e Imp|271408|6390852|1 mes|324,07|7,67,E-09|1,86,E-09|1,55,E-09|2,13,E-08|5,07,E-09|
|AREA|SRC_270|Cam_Valpo_151-PEAS e Imp|271425|6390918|1 mes|269,76|9,21,E-09|2,23,E-09|1,86,E-09|2,56,E-08|6,09,E-09|
|AREA|SRC_271|Cam_Valpo_152-PEAS e Imp|271595|6391444|1 mes|2210,20|1,12,E-09|2,72,E-10|2,27,E-10|3,13,E-09|7,43,E-10|
|AREA|SRC_272|Cam_Valpo_153-PEAS e Imp|271601|6391518|1 mes|297,07|8,37,E-09|2,02,E-09|1,69,E-09|2,33,E-08|5,53,E-09|
|AREA|SRC_273|Cam_Valpo_154-PEAS e Imp|271583|6391599|1 mes|334,56|7,43,E-09|1,80,E-09|1,50,E-09|2,07,E-08|4,91,E-09|
|AREA|SRC_274|Cam_Valpo_155-PEAS e Imp|271490|6391665|1 mes|462,29|5,38,E-09|1,30,E-09|1,08,E-09|1,50,E-08|3,55,E-09|
|AREA|SRC_275|Cam_Valpo_156-PEAS e Imp|271388|6391779|1 mes|610,49|4,07,E-09|9,85,E-10|8,21,E-10|1,13,E-08|2,69,E-09|
|AREA|SRC_276|Cam_Valpo_157-PEAS e Imp|271303|6391969|1 mes|829,95|2,99,E-09|7,25,E-10|6,04,E-10|8,33,E-09|1,98,E-09|
|AREA|SRC_277|Cam_Valpo_158-PEAS e Imp|271249|6392048|1 mes|385,48|6,45,E-09|1,56,E-09|1,30,E-09|1,79,E-08|4,26,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 107. Fuentes de Emisión - Escenario 3 parte 9

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 214 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_278|Cam_Valpo_159-PEAS e Imp|271095|6392199|1 mes|863,11|2,88,E-09|6,97,E-10|5,81,E-10|8,01,E-09|1,90,E-09|
|AREA|SRC_279|Cam_Valpo_160-PEAS e Imp|271003|6392357|1 mes|727,41|3,42,E-09|8,27,E-10|6,89,E-10|9,51,E-09|2,26,E-09|
|AREA|SRC_280|Cam_Valpo_161-PEAS e Imp|270864|6392618|1 mes|1181,67|2,10,E-09|5,09,E-10|4,24,E-10|5,85,E-09|1,39,E-09|
|AREA|SRC_281|Cam_Valpo_162-PEAS e Imp|270665|6392901|1 mes|1386,67|1,79,E-09|4,34,E-10|3,61,E-10|4,99,E-09|1,18,E-09|
|AREA|SRC_282|Cam_Valpo_163-PEAS e Imp|270570|6393060|1 mes|739,81|3,36,E-09|8,13,E-10|6,77,E-10|9,35,E-09|2,22,E-09|
|AREA|SRC_283|Cam_Valpo_164-PEAS e Imp|270535|6393162|1 mes|427,94|5,81,E-09|1,41,E-09|1,17,E-09|1,62,E-08|3,84,E-09|
|AREA|SRC_284|Cam_Valpo_165-PEAS e Imp|270408|6393157|1 mes|516,16|4,82,E-09|1,17,E-09|9,71,E-10|1,34,E-08|3,18,E-09|
|AREA|SRC_285|Cam_Valpo_166-PEAS e Imp|270322|6393156|1 mes|344,11|7,22,E-09|1,75,E-09|1,46,E-09|2,01,E-08|4,77,E-09|
|AREA|SRC_286|Cam_Valpo_167-PEAS e Imp|270198|6393225|1 mes|562,03|4,42,E-09|1,07,E-09|8,92,E-10|1,23,E-08|2,92,E-09|
|AREA|SRC_287|Cam_Valpo_168-PEAS e Imp|270084|6393222|1 mes|461,57|5,38,E-09|1,30,E-09|1,09,E-09|1,50,E-08|3,56,E-09|
|AREA|SRC_288|Cam_Valpo_169-PEAS e Imp|270014|6393114|1 mes|520,05|4,78,E-09|1,16,E-09|9,64,E-10|1,33,E-08|3,16,E-09|
|AREA|SRC_289|Cam_Valpo_170-PEAS e Imp|269944|6393026|1 mes|448,19|5,55,E-09|1,34,E-09|1,12,E-09|1,54,E-08|3,67,E-09|
|AREA|SRC_290|Cam_Valpo_171-PEAS e Imp|269831|6392981|1 mes|484,35|5,13,E-09|1,24,E-09|1,03,E-09|1,43,E-08|3,39,E-09|
|AREA|SRC_291|Cam_Valpo_172-PEAS e Imp|269702|6392966|1 mes|516,99|4,81,E-09|1,16,E-09|9,69,E-10|1,34,E-08|3,18,E-09|
|AREA|SRC_292|Cam_Valpo_173-PEAS e Imp|269506|6393084|1 mes|906,73|2,74,E-09|6,63,E-10|5,53,E-10|7,63,E-09|1,81,E-09|
|AREA|SRC_293|Cam_Valpo_174-PEAS e Imp|269407|6393106|1 mes|410,62|6,05,E-09|1,46,E-09|1,22,E-09|1,68,E-08|4,00,E-09|
|AREA|SRC_294|Cam_Valpo_175-PEAS e Imp|269355|6393219|1 mes|493,13|5,04,E-09|1,22,E-09|1,02,E-09|1,40,E-08|3,33,E-09|
|AREA|SRC_295|Cam_Valpo_176-PEAS e Imp|269450|6393436|1 mes|939,57|2,65,E-09|6,40,E-10|5,33,E-10|7,36,E-09|1,75,E-09|
|AREA|SRC_296|Cam_Valpo_177-PEAS e Imp|269537|6393768|1 mes|1375,49|1,81,E-09|4,37,E-10|3,64,E-10|5,03,E-09|1,19,E-09|
|AREA|SRC_297|Cam_Valpo_178-PEAS e Imp|269541|6393876|1 mes|433,16|5,74,E-09|1,39,E-09|1,16,E-09|1,60,E-08|3,79,E-09|
|AREA|SRC_298|Cam_Valpo_179-PEAS e Imp|269514|6393952|1 mes|327,49|7,59,E-09|1,84,E-09|1,53,E-09|2,11,E-08|5,02,E-09|
|AREA|SRC_299|Cam_Valpo_180-PEAS e Imp|269461|6394006|1 mes|302,03|8,23,E-09|1,99,E-09|1,66,E-09|2,29,E-08|5,44,E-09|
|AREA|SRC_300|Cam_Valpo_181-PEAS e Imp|269456|6394087|1 mes|317,54|7,83,E-09|1,89,E-09|1,58,E-09|2,18,E-08|5,17,E-09|
|AREA|SRC_301|Cam_Valpo_182-PEAS e Imp|269494|6394169|1 mes|358,94|6,92,E-09|1,68,E-09|1,40,E-09|1,93,E-08|4,58,E-09|
|AREA|SRC_302|Cam_Valpo_183-PEAS e Imp|269580|6394296|1 mes|611,99|4,06,E-09|9,83,E-10|8,19,E-10|1,13,E-08|2,68,E-09|
|AREA|SRC_303|Cam_Valpo_184-PEAS e Imp|269614|6394394|1 mes|416,61|5,97,E-09|1,44,E-09|1,20,E-09|1,66,E-08|3,94,E-09|
|AREA|SRC_304|Cam_Valpo_185-PEAS e Imp|269617|6394492|1 mes|396,57|6,27,E-09|1,52,E-09|1,26,E-09|1,74,E-08|4,14,E-09|
|AREA|SRC_305|Cam_Valpo_186-PEAS e Imp|269532|6394634|1 mes|664,18|3,74,E-09|9,05,E-10|7,54,E-10|1,04,E-08|2,47,E-09|
|AREA|SRC_306|Cam_Valpo_187-PEAS e Imp|269478|6394752|1 mes|518,20|4,80,E-09|1,16,E-09|9,67,E-10|1,33,E-08|3,17,E-09|
|AREA|SRC_307|Cam_Valpo_188-PEAS e Imp|269437|6394881|1 mes|540,93|4,59,E-09|1,11,E-09|9,26,E-10|1,28,E-08|3,04,E-09|
|AREA|SRC_308|Cam_Valpo_189-PEAS e Imp|269448|6395002|1 mes|483,46|5,14,E-09|1,24,E-09|1,04,E-09|1,43,E-08|3,40,E-09|
|AREA|SRC_309|Cam_Valpo_190-PEAS e Imp|269465|6395049|1 mes|197,82|1,26,E-08|3,04,E-09|2,53,E-09|3,50,E-08|8,30,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 108. Fuentes de Emisión - Escenario 3 parte 10

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 215 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_310|Cam_Valpo_191-PEAS e Imp|269701|6395188|1 mes|1088,66|2,28,E-09|5,52,E-10|4,60,E-10|6,35,E-09|1,51,E-09|
|AREA|SRC_311|Cam_Valpo_192-PEAS e Imp|269737|6395244|1 mes|269,38|9,23,E-09|2,23,E-09|1,86,E-09|2,57,E-08|6,10,E-09|
|AREA|SRC_312|Cam_Valpo_193-PEAS e Imp|269748|6395318|1 mes|301,88|8,23,E-09|1,99,E-09|1,66,E-09|2,29,E-08|5,44,E-09|
|AREA|SRC_313|Cam_Valpo_194-PEAS e Imp|269734|6395473|1 mes|624,02|3,98,E-09|9,64,E-10|8,03,E-10|1,11,E-08|2,63,E-09|
|AREA|SRC_314|Cam_Valpo_195-PEAS e Imp|269791|6395575|1 mes|462,91|5,37,E-09|1,30,E-09|1,08,E-09|1,49,E-08|3,55,E-09|
|AREA|SRC_315|Cam_Valpo_196-PEAS e Imp|269918|6395634|1 mes|557,57|4,46,E-09|1,08,E-09|8,99,E-10|1,24,E-08|2,95,E-09|
|AREA|SRC_316|Cam_Valpo_197-PEAS e Imp|269951|6395703|1 mes|311,66|7,98,E-09|1,93,E-09|1,61,E-09|2,22,E-08|5,27,E-09|
|AREA|SRC_317|Cam_Valpo_198-PEAS e Imp|269926|6395767|1 mes|277,87|8,94,E-09|2,16,E-09|1,80,E-09|2,49,E-08|5,91,E-09|
|AREA|SRC_318|Cam_Valpo_199-PEAS e Imp|269853|6395812|1 mes|348,28|7,14,E-09|1,73,E-09|1,44,E-09|1,99,E-08|4,72,E-09|
|AREA|SRC_319|Cam_Valpo_200-PEAS e Imp|269732|6395847|1 mes|504,67|4,93,E-09|1,19,E-09|9,93,E-10|1,37,E-08|3,25,E-09|
|AREA|SRC_320|Cam_Valpo_201-PEAS e Imp|269688|6395928|1 mes|365,46|6,80,E-09|1,65,E-09|1,37,E-09|1,89,E-08|4,49,E-09|
|AREA|SRC_321|Cam_Valpo_202-PEAS e Imp|269717|6396047|1 mes|484,68|5,13,E-09|1,24,E-09|1,03,E-09|1,43,E-08|3,39,E-09|
|AREA|SRC_322|Cam_Valpo_203-PEAS e Imp|269712|6396106|1 mes|237,49|1,05,E-08|2,53,E-09|2,11,E-09|2,91,E-08|6,92,E-09|
|AREA|SRC_323|Cam_Valpo_204-PEAS e Imp|269657|6396143|1 mes|271,48|9,16,E-09|2,22,E-09|1,85,E-09|2,55,E-08|6,05,E-09|
|AREA|SRC_324|Cam_Valpo_205-PEAS e Imp|269580|6396120|1 mes|326,46|7,61,E-09|1,84,E-09|1,53,E-09|2,12,E-08|5,03,E-09|
|AREA|SRC_325|Cam_Valpo_206-PEAS e Imp|269501|6396070|1 mes|376,20|6,61,E-09|1,60,E-09|1,33,E-09|1,84,E-08|4,37,E-09|
|AREA|SRC_326|Cam_Valpo_207-PEAS e Imp|269359|6396026|1 mes|593,54|4,19,E-09|1,01,E-09|8,44,E-10|1,17,E-08|2,77,E-09|
|AREA|SRC_327|Cam_Valpo_208-PEAS e Imp|269272|6396023|1 mes|343,48|7,24,E-09|1,75,E-09|1,46,E-09|2,01,E-08|4,78,E-09|
|AREA|SRC_328|Cam_Valpo_209-PEAS e Imp|269222|6396073|1 mes|275,81|9,01,E-09|2,18,E-09|1,82,E-09|2,51,E-08|5,96,E-09|
|AREA|SRC_329|Cam_Valpo_210-PEAS e Imp|269210|6396185|1 mes|446,25|5,57,E-09|1,35,E-09|1,12,E-09|1,55,E-08|3,68,E-09|
|AREA|SRC_330|Cam_Valpo_211-PEAS e Imp|269167|6396232|1 mes|255,46|9,73,E-09|2,35,E-09|1,96,E-09|2,71,E-08|6,43,E-09|
|AREA|SRC_331|Cam_Valpo_212-PEAS e Imp|269082|6396226|1 mes|349,58|7,11,E-09|1,72,E-09|1,43,E-09|1,98,E-08|4,70,E-09|
|AREA|SRC_332|Cam_Valpo_213-PEAS e Imp|268998|6396240|1 mes|335,54|7,41,E-09|1,79,E-09|1,49,E-09|2,06,E-08|4,90,E-09|
|AREA|SRC_333|Cam_Valpo_214-PEAS e Imp|268894|6396300|1 mes|480,09|5,18,E-09|1,25,E-09|1,04,E-09|1,44,E-08|3,42,E-09|
|AREA|SRC_334|Cam_Valpo_215-PEAS e Imp|268805|6396381|1 mes|477,49|5,21,E-09|1,26,E-09|1,05,E-09|1,45,E-08|3,44,E-09|
|AREA|SRC_335|Cam_Valpo_216-PEAS e Imp|268734|6396481|1 mes|489,34|5,08,E-09|1,23,E-09|1,02,E-09|1,41,E-08|3,36,E-09|
|AREA|SRC_336|Cam_Valpo_217-PEAS e Imp|268692|6396569|1 mes|388,32|6,40,E-09|1,55,E-09|1,29,E-09|1,78,E-08|4,23,E-09|
|AREA|SRC_337|Cam_Valpo_218-PEAS e Imp|268614|6396686|1 mes|563,68|4,41,E-09|1,07,E-09|8,89,E-10|1,23,E-08|2,91,E-09|
|AREA|SRC_338|Cam_Valpo_219-PEAS e Imp|268551|6396751|1 mes|365,13|6,81,E-09|1,65,E-09|1,37,E-09|1,89,E-08|4,50,E-09|
|AREA|SRC_339|Cam_Valpo_220-PEAS e Imp|268525|6396834|1 mes|342,75|7,25,E-09|1,75,E-09|1,46,E-09|2,02,E-08|4,79,E-09|
|AREA|SRC_340|Cam_Valpo_221-PEAS e Imp|268521|6396918|1 mes|335,20|7,42,E-09|1,79,E-09|1,49,E-09|2,06,E-08|4,90,E-09|
|AREA|SRC_341|Cam_Valpo_222-PEAS e Imp|268510|6396996|1 mes|312,17|7,96,E-09|1,93,E-09|1,61,E-09|2,22,E-08|5,26,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 109. Fuentes de Emisión - Escenario 3 parte 11

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 216 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_342|Cam_Valpo_223-PEAS e Imp|268441|6397095|1 mes|486,78|5,11,E-09|1,24,E-09|1,03,E-09|1,42,E-08|3,37,E-09|
|AREA|SRC_343|Cam_Valpo_224-PEAS e Imp|268352|6397195|1 mes|537,81|4,62,E-09|1,12,E-09|9,32,E-10|1,29,E-08|3,05,E-09|
|AREA|SRC_344|Cam_Valpo_225-PEAS e Imp|268295|6397296|1 mes|460,41|5,40,E-09|1,31,E-09|1,09,E-09|1,50,E-08|3,57,E-09|
|AREA|SRC_345|Cam_Valpo_226-PEAS e Imp|268265|6397370|1 mes|319,00|7,79,E-09|1,89,E-09|1,57,E-09|2,17,E-08|5,15,E-09|
|AREA|SRC_346|Cam_Valpo_227-PEAS e Imp|268236|6397470|1 mes|414,51|6,00,E-09|1,45,E-09|1,21,E-09|1,67,E-08|3,96,E-09|
|AREA|SRC_347|Cam_Valpo_228-PEAS e Imp|268225|6397539|1 mes|278,02|8,94,E-09|2,16,E-09|1,80,E-09|2,49,E-08|5,91,E-09|
|AREA|SRC_348|Cam_Valpo_229-PEAS e Imp|268212|6397650|1 mes|446,47|5,57,E-09|1,35,E-09|1,12,E-09|1,55,E-08|3,68,E-09|
|AREA|SRC_349|Cam_Valpo_230-PEAS e Imp|268292|6397691|1 mes|352,90|7,04,E-09|1,70,E-09|1,42,E-09|1,96,E-08|4,65,E-09|
|AREA|SRC_350|Cam_Valpo_231-PEAS e Imp|268324|6397741|1 mes|244,09|1,02,E-08|2,46,E-09|2,05,E-09|2,83,E-08|6,73,E-09|
|AREA|SRC_351|Cam_Valpo_232-PEAS e Imp|268344|6397809|1 mes|284,52|8,74,E-09|2,11,E-09|1,76,E-09|2,43,E-08|5,77,E-09|
|AREA|SRC_352|Cam_Valpo_233-PEAS e Imp|268317|6397871|1 mes|277,40|8,96,E-09|2,17,E-09|1,81,E-09|2,49,E-08|5,92,E-09|
|AREA|SRC_353|Cam_Valpo_234-PEAS e Imp|268289|6397931|1 mes|263,44|9,43,E-09|2,28,E-09|1,90,E-09|2,62,E-08|6,24,E-09|
|AREA|SRC_354|Cam_Valpo_235-PEAS e Imp|268281|6397993|1 mes|246,21|1,01,E-08|2,44,E-09|2,04,E-09|2,81,E-08|6,67,E-09|
|AREA|SRC_355|Cam_Valpo_236-PEAS e Imp|268325|6398057|1 mes|307,11|8,09,E-09|1,96,E-09|1,63,E-09|2,25,E-08|5,35,E-09|
|AREA|SRC_356|Cam_Valpo_237-PEAS e Imp|268339|6398092|1 mes|154,12|1,61,E-08|3,90,E-09|3,25,E-09|4,49,E-08|1,07,E-08|
|AREA|SRC_357|Cam_Valpo_238-PEAS e Imp|268362|6398151|1 mes|251,56|9,88,E-09|2,39,E-09|1,99,E-09|2,75,E-08|6,53,E-09|
|AREA|SRC_358|Cam_Valpo_239-PEAS e Imp|268383|6398192|1 mes|185,19|1,34,E-08|3,25,E-09|2,71,E-09|3,73,E-08|8,87,E-09|
|AREA|SRC_359|Cam_Valpo_240-PEAS e Imp|268355|6398247|1 mes|250,18|9,94,E-09|2,40,E-09|2,00,E-09|2,76,E-08|6,57,E-09|
|AREA|SRC_360|Cam_Valpo_241-PEAS e Imp|268227|6398303|1 mes|566,84|4,38,E-09|1,06,E-09|8,84,E-10|1,22,E-08|2,90,E-09|
|AREA|SRC_361|Cam_Valpo_242-PEAS e Imp|268140|6398362|1 mes|418,83|5,93,E-09|1,44,E-09|1,20,E-09|1,65,E-08|3,92,E-09|
|AREA|SRC_362|Cam_Valpo_243-PEAS e Imp|268089|6398427|1 mes|325,43|7,64,E-09|1,85,E-09|1,54,E-09|2,12,E-08|5,05,E-09|
|AREA|SRC_363|Cam_Valpo_244-PEAS e Imp|268005|6398483|1 mes|406,15|6,12,E-09|1,48,E-09|1,23,E-09|1,70,E-08|4,04,E-09|
|AREA|SRC_364|Cam_Valpo_245-PEAS e Imp|267956|6398553|1 mes|338,26|7,35,E-09|1,78,E-09|1,48,E-09|2,04,E-08|4,86,E-09|
|AREA|SRC_365|Cam_Valpo_246-PEAS e Imp|267920|6398673|1 mes|498,96|4,98,E-09|1,21,E-09|1,00,E-09|1,39,E-08|3,29,E-09|
|AREA|SRC_366|Cam_Valpo_247-PEAS e Imp|267908|6398749|1 mes|308,37|8,06,E-09|1,95,E-09|1,63,E-09|2,24,E-08|5,33,E-09|
|AREA|SRC_367|Cam_Valpo_248-PEAS e Imp|267894|6398771|1 mes|107,41|2,31,E-08|5,60,E-09|4,67,E-09|6,44,E-08|1,53,E-08|
|AREA|SRC_368|Cam_Valpo_249-PEAS e Imp|267791|6398823|1 mes|466,56|5,33,E-09|1,29,E-09|1,07,E-09|1,48,E-08|3,52,E-09|
|AREA|SRC_369|Cam_Valpo_250-PEAS e Imp|267747|6398849|1 mes|204,00|1,22,E-08|2,95,E-09|2,46,E-09|3,39,E-08|8,05,E-09|
|AREA|SRC_370|Cam_Valpo_251-PEAS e Imp|267699|6398875|1 mes|217,15|1,14,E-08|2,77,E-09|2,31,E-09|3,18,E-08|7,56,E-09|
|AREA|SRC_371|Cam_Valpo_252-PEAS e Imp|267673|6398943|1 mes|285,91|8,69,E-09|2,10,E-09|1,75,E-09|2,42,E-08|5,75,E-09|
|AREA|SRC_372|Cam_Valpo_253-PEAS e Imp|267740|6399152|1 mes|871,99|2,85,E-09|6,90,E-10|5,75,E-10|7,93,E-09|1,88,E-09|
|AREA|SRC_373|Cam_Valpo_254-PEAS e Imp|267754|6399259|1 mes|434,37|5,72,E-09|1,38,E-09|1,15,E-09|1,59,E-08|3,78,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 217 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_374|Cam_Valpo_255-PEAS e Imp|267756|6399372|1 mes|452,93|5,49,E-09|1,33,E-09|1,11,E-09|1,53,E-08|3,63,E-09|
|AREA|SRC_375|Cam_Valpo_256-PEAS e Imp|267702|6399478|1 mes|480,03|5,18,E-09|1,25,E-09|1,04,E-09|1,44,E-08|3,42,E-09|
|AREA|SRC_376|Cam_Valpo_257-PEAS e Imp|267740|6399547|1 mes|307,21|8,09,E-09|1,96,E-09|1,63,E-09|2,25,E-08|5,35,E-09|
|AREA|SRC_377|Cam_Valpo_258-PEAS e Imp|267742|6399624|1 mes|311,56|7,98,E-09|1,93,E-09|1,61,E-09|2,22,E-08|5,27,E-09|
|AREA|SRC_378|Cam_Valpo_259-PEAS e Imp|267731|6399695|1 mes|287,58|8,64,E-09|2,09,E-09|1,74,E-09|2,40,E-08|5,71,E-09|
|AREA|SRC_379|Cam_Valpo_260-PEAS e Imp|267682|6399788|1 mes|425,70|5,84,E-09|1,41,E-09|1,18,E-09|1,62,E-08|3,86,E-09|
|AREA|SRC_380|Cam_Valpo_261-PEAS e Imp|267661|6399830|1 mes|187,04|1,33,E-08|3,22,E-09|2,68,E-09|3,70,E-08|8,78,E-09|

Tabla 111. Fuentes de Emisión - Escenario 3 parte 13

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/s]|[g/s]|[g/s]|[g/s]|[g/s]|
|VOLUMEN|SRC_26|Peas_9|272534,98|6385157,02|1 mes|4|0,00,E+00|0,00,E+00|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_27|Peas_10|272710,98|6386276,01|1 mes|4|0,00,E+00|0,00,E+00|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_28|Imp_9|272634,97|6385155,98|1 mes|4|0,00,E+00|0,00,E+00|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_29|Imp_10.1|272663,05|6386154,98|1 mes|4|0,00,E+00|0,00,E+00|0,00,E+00|0,00,E+00|0,00,E+00|
|VOLUMEN|SRC_30|Imp_10.2|272621,03|6386107,97|1 mes|4|0,00,E+00|0,00,E+00|0,00,E+00|0,00,E+00|0,00,E+00|
|PUNTUAL|SRC_51|IF 1|272319|6384980|1 mes|0,05|1,99,E-03|4,81,E-04|0,00,E+00|5,66,E-02|1,22,E-02|
|PUNTUAL|SRC_52|IF 2|273521,82|6383276,23|1 mes|0,05|1,99,E-03|4,81,E-04|0,00,E+00|5,66,E-02|1,22,E-02|

**17.4 FUENTES DE EMISIÓN - ESCENARIO 4**

Tabla 112. Fuentes de Emisión - Escenario 4 parte 1

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_1|Colec_x1|271160|6382780|3 meses|4,00|1,09,E-03|5,45,E-04|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_2|Colec_x2|271232|6382755|3 meses|4,00|1,09,E-03|5,45,E-04|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_3|Colec_x3|271317|6382733|3 meses|4,00|1,09,E-03|5,45,E-04|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_4|Colec_x4|271281|6382672|3 meses|4,00|1,09,E-03|5,45,E-04|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_5|Colec_x5|271238|6382627|3 meses|4,00|1,09,E-03|5,45,E-04|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_6|Colec_x6|271296|6382492|3 meses|4,00|1,09,E-03|5,45,E-04|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_7|Colec_x7|271377|6382401|3 meses|4,00|1,09,E-03|5,45,E-04|0,00,E+00|0,00,E+00|0,00,E+00|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 218 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>273043|[m]<br>6387323|[m]<br>6387323|[m2]<br>383,32|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_17|Cam_Cat_1-PEAS e Imp|Cam_Cat_1-PEAS e Imp|Cam_Cat_1-PEAS e Imp|3 meses|3 meses|3,31,E-09|8,00,E-10|1,45,E-09|2,53,E-08|6,02,E-09|
|AREA|SRC_18|Cam_Cat_2-PEAS e Imp|273206|6387558|3 meses|1145,03|1,11,E-09|2,68,E-10|4,85,E-10|8,48,E-09|2,01,E-09|
|AREA|SRC_19|Cam_Cat_3-PEAS e Imp|273308|6387612|3 meses|456,00|2,78,E-09|6,73,E-10|1,22,E-09|2,13,E-08|5,06,E-09|
|AREA|SRC_20|Cam_Cat_4-PEAS e Imp|273511|6387668|3 meses|843,57|1,50,E-09|3,64,E-10|6,58,E-10|1,15,E-08|2,73,E-09|
|AREA|SRC_21|Cam_Cat_5-PEAS e Imp|273721|6387707|3 meses|853,32|1,49,E-09|3,59,E-10|6,50,E-10|1,14,E-08|2,70,E-09|
|AREA|SRC_22|Cam_Cat_6-PEAS e Imp|273880|6387880|3 meses|945,26|1,34,E-09|3,24,E-10|5,87,E-10|1,03,E-08|2,44,E-09|
|AREA|SRC_23|Cam_Cat_7-PEAS e Imp|273982|6387934|3 meses|457,52|2,77,E-09|6,70,E-10|1,21,E-09|2,12,E-08|5,04,E-09|
|AREA|SRC_24|Cam_Cat_8-PEAS e Imp|274178|6387916|3 meses|782,20|1,62,E-09|3,92,E-10|7,09,E-10|1,24,E-08|2,95,E-09|
|AREA|SRC_25|Cam_Cat_9-PEAS e Imp|274216|6387945|3 meses|195,48|6,49,E-09|1,57,E-09|2,84,E-09|4,97,E-08|1,18,E-08|
|AREA|SRC_26|Cam_Cat_10-PEAS e Imp|274213|6388017|3 meses|295,61|4,29,E-09|1,04,E-09|1,88,E-09|3,28,E-08|7,80,E-09|
|AREA|SRC_27|Cam_Cat_11-PEAS e Imp|274177|6388250|3 meses|941,53|1,35,E-09|3,26,E-10|5,89,E-10|1,03,E-08|2,45,E-09|
|AREA|SRC_28|Cam_Cat_12-PEAS e Imp|274185|6388365|3 meses|458,34|2,77,E-09|6,69,E-10|1,21,E-09|2,12,E-08|5,03,E-09|
|AREA|SRC_29|Cam_Cat_13-PEAS e Imp|274352|6388558|3 meses|1016,92|1,25,E-09|3,02,E-10|5,46,E-10|9,55,E-09|2,27,E-09|
|AREA|SRC_30|Cam_Cat_14-PEAS e Imp|274654|6388846|3 meses|1667,00|7,61,E-10|1,84,E-10|3,33,E-10|5,82,E-09|1,38,E-09|
|AREA|SRC_31|Cam_Cat_15-PEAS e Imp|274745|6388895|3 meses|409,81|3,09,E-09|7,48,E-10|1,35,E-09|2,37,E-08|5,63,E-09|
|AREA|SRC_32|Cam_Cat_16-PEAS e Imp|274834|6388862|3 meses|371,12|3,42,E-09|8,27,E-10|1,50,E-09|2,62,E-08|6,22,E-09|
|AREA|SRC_33|Cam_Cat_17-PEAS e Imp|274882|6388794|3 meses|331,29|3,83,E-09|9,26,E-10|1,68,E-09|2,93,E-08|6,96,E-09|
|AREA|SRC_34|Cam_Cat_18-PEAS e Imp|274979|6388768|3 meses|406,63|3,12,E-09|7,54,E-10|1,36,E-09|2,39,E-08|5,67,E-09|
|AREA|SRC_35|Cam_Cat_19-PEAS e Imp|275069|6388799|3 meses|384,16|3,30,E-09|7,98,E-10|1,44,E-09|2,53,E-08|6,00,E-09|
|AREA|SRC_36|Cam_Cat_20-PEAS e Imp|275059|6388911|3 meses|459,52|2,76,E-09|6,68,E-10|1,21,E-09|2,11,E-08|5,02,E-09|
|AREA|SRC_37|Cam_Cat_21-PEAS e Imp|275040|6389003|3 meses|374,05|3,39,E-09|8,20,E-10|1,48,E-09|2,60,E-08|6,17,E-09|
|AREA|SRC_38|Cam_Cat_22-PEAS e Imp|274958|6389092|3 meses|489,11|2,59,E-09|6,27,E-10|1,13,E-09|1,99,E-08|4,72,E-09|
|AREA|SRC_39|Cam_Cat_23-PEAS e Imp|274915|6389184|3 meses|402,20|3,15,E-09|7,63,E-10|1,38,E-09|2,41,E-08|5,73,E-09|
|AREA|SRC_40|Cam_Cat_24-PEAS e Imp|274946|6389307|3 meses|502,79|2,52,E-09|6,10,E-10|1,10,E-09|1,93,E-08|4,59,E-09|
|AREA|SRC_41|Cam_Cat_25-PEAS e Imp|275049|6389374|3 meses|485,06|2,61,E-09|6,32,E-10|1,14,E-09|2,00,E-08|4,76,E-09|
|AREA|SRC_42|Cam_Cat_26-PEAS e Imp|275181|6389406|3 meses|541,36|2,34,E-09|5,67,E-10|1,03,E-09|1,79,E-08|4,26,E-09|
|AREA|SRC_43|Cam_Cat_27-PEAS e Imp|275286|6389385|3 meses|424,34|2,99,E-09|7,23,E-10|1,31,E-09|2,29,E-08|5,44,E-09|
|AREA|SRC_44|Cam_Cat_28-PEAS e Imp|275372|6389387|3 meses|345,06|3,67,E-09|8,89,E-10|1,61,E-09|2,81,E-08|6,68,E-09|
|AREA|SRC_45|Cam_Cat_29-PEAS e Imp|275519|6389442|3 meses|633,26|2,00,E-09|4,84,E-10|8,76,E-10|1,53,E-08|3,64,E-09|
|AREA|SRC_46|Cam_Cat_30-PEAS e Imp|275575|6389512|3 meses|360,36|3,52,E-09|8,51,E-10|1,54,E-09|2,69,E-08|6,40,E-09|
|AREA|SRC_47|Cam_Cat_31-PEAS e Imp|275579|6389623|3 meses|447,31|2,83,E-09|6,86,E-10|1,24,E-09|2,17,E-08|5,16,E-09|
|AREA|SRC_48|Cam_Cat_32-PEAS e Imp|275473|6389738|3 meses|629,59|2,01,E-09|4,87,E-10|8,81,E-10|1,54,E-08|3,66,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 219 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>275397|[m]<br>6389809|[m]<br>6389809|[m2]<br>419,18|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_49|Cam_Cat_33-PEAS e Imp|Cam_Cat_33-PEAS e Imp|Cam_Cat_33-PEAS e Imp|3 meses|3 meses|3,02,E-09|7,32,E-10|1,32,E-09|2,32,E-08|5,50,E-09|
|AREA|SRC_50|Cam_Cat_34-PEAS e Imp|275382|6389918|3 meses|432,78|2,93,E-09|7,09,E-10|1,28,E-09|2,24,E-08|5,33,E-09|
|AREA|SRC_51|Cam_Cat_35-PEAS e Imp|275487|6390018|3 meses|576,65|2,20,E-09|5,32,E-10|9,62,E-10|1,68,E-08|4,00,E-09|
|AREA|SRC_52|Cam_Cat_36-PEAS e Imp|275630|6390045|3 meses|576,34|2,20,E-09|5,32,E-10|9,63,E-10|1,68,E-08|4,00,E-09|
|AREA|SRC_53|Cam_Cat_37-PEAS e Imp|275763|6390025|3 meses|532,94|2,38,E-09|5,76,E-10|1,04,E-09|1,82,E-08|4,33,E-09|
|AREA|SRC_54|Cam_Cat_38-PEAS e Imp|275861|6389993|3 meses|411,71|3,08,E-09|7,45,E-10|1,35,E-09|2,36,E-08|5,60,E-09|
|AREA|SRC_55|Cam_Cat_39-PEAS e Imp|276044|6389963|3 meses|742,87|1,71,E-09|4,13,E-10|7,47,E-10|1,31,E-08|3,10,E-09|
|AREA|SRC_56|Cam_Cat_40-PEAS e Imp|276114|6389925|3 meses|316,96|4,00,E-09|9,68,E-10|1,75,E-09|3,06,E-08|7,28,E-09|
|AREA|SRC_57|Cam_Cat_41-PEAS e Imp|276133|6389885|3 meses|172,93|7,33,E-09|1,77,E-09|3,21,E-09|5,61,E-08|1,33,E-08|
|AREA|SRC_58|Cam_Cat_42-PEAS e Imp|276158|6389818|3 meses|286,84|4,42,E-09|1,07,E-09|1,93,E-09|3,38,E-08|8,04,E-09|
|AREA|SRC_59|Cam_Cat_43-PEAS e Imp|276157|6389659|3 meses|632,84|2,00,E-09|4,85,E-10|8,77,E-10|1,53,E-08|3,64,E-09|
|AREA|SRC_60|Cam_Cat_44-PEAS e Imp|276172|6389529|3 meses|521,10|2,43,E-09|5,89,E-10|1,06,E-09|1,86,E-08|4,43,E-09|
|AREA|SRC_61|Cam_Cat_45-PEAS e Imp|276275|6389477|3 meses|468,32|2,71,E-09|6,55,E-10|1,18,E-09|2,07,E-08|4,93,E-09|
|AREA|SRC_62|Cam_Cat_46-PEAS e Imp|276411|6389458|3 meses|553,37|2,29,E-09|5,54,E-10|1,00,E-09|1,75,E-08|4,17,E-09|
|AREA|SRC_63|Cam_Cat_47-PEAS e Imp|276501|6389471|3 meses|366,24|3,46,E-09|8,38,E-10|1,52,E-09|2,65,E-08|6,30,E-09|
|AREA|SRC_64|Cam_Cat_48-PEAS e Imp|276706|6389673|3 meses|1151,46|1,10,E-09|2,66,E-10|4,82,E-10|8,43,E-09|2,00,E-09|
|AREA|SRC_65|Cam_Cat_49-PEAS e Imp|277353|6390498|3 meses|4195,41|3,02,E-10|7,31,E-11|1,32,E-10|2,31,E-09|5,50,E-10|
|AREA|SRC_66|Cam_Cat_50-PEAS e Imp|277494|6390575|3 meses|640,03|1,98,E-09|4,79,E-10|8,67,E-10|1,52,E-08|3,60,E-09|
|AREA|SRC_67|Cam_Cat_51-PEAS e Imp|279440|6391244|3 meses|8223,68|1,54,E-10|3,73,E-11|6,75,E-11|1,18,E-09|2,80,E-10|
|AREA|SRC_68|Cam_Cat_52-PEAS e Imp|283346|6393239|3 meses|17540,88|7,23,E-11|1,75,E-11|3,16,E-11|5,54,E-10|1,31,E-10|
|AREA|SRC_69|Cam_Cat_53-PEAS e Imp|287745|6394661|3 meses|18483,13|6,86,E-11|1,66,E-11|3,00,E-11|5,25,E-10|1,25,E-10|
|AREA|SRC_70|Cam_Pta_1-PEAS e Imp|273147|6383634|3 meses|1866,42|6,79,E-10|1,64,E-10|2,97,E-10|5,20,E-09|1,24,E-09|
|AREA|SRC_71|Cam_Pta_2-PEAS e Imp|273165|6383642|3 meses|80,85|1,57,E-08|3,79,E-09|6,86,E-09|1,20,E-07|2,85,E-08|
|AREA|SRC_72|Cam_Pta_3-PEAS e Imp|273189|6383637|3 meses|94,14|1,35,E-08|3,26,E-09|5,89,E-09|1,03,E-07|2,45,E-08|
|AREA|SRC_73|Cam_Pta_4-PEAS e Imp|273241|6383562|3 meses|359,95|3,52,E-09|8,52,E-10|1,54,E-09|2,70,E-08|6,41,E-09|
|AREA|SRC_74|Cam_Pta_5-PEAS e Imp|273289|6383445|3 meses|505,57|2,51,E-09|6,07,E-10|1,10,E-09|1,92,E-08|4,56,E-09|
|AREA|SRC_75|Cam_Pta_6-PEAS e Imp|273304|6383402|3 meses|179,62|7,06,E-09|1,71,E-09|3,09,E-09|5,41,E-08|1,28,E-08|
|AREA|SRC_76|Cam_Pta_7-PEAS e Imp|273331|6383382|3 meses|138,45|9,16,E-09|2,22,E-09|4,01,E-09|7,01,E-08|1,67,E-08|
|AREA|SRC_77|Cam_Pta_8-PEAS e Imp|273361|6383362|3 meses|145,56|8,71,E-09|2,11,E-09|3,81,E-09|6,67,E-08|1,58,E-08|
|AREA|SRC_78|Cam_Pta_9-PEAS e Imp|273393|6383346|3 meses|143,99|8,81,E-09|2,13,E-09|3,85,E-09|6,74,E-08|1,60,E-08|
|AREA|SRC_79|Cam_Pta_10-PEAS e Imp|273413|6383324|3 meses|116,32|1,09,E-08|2,64,E-09|4,77,E-09|8,35,E-08|1,98,E-08|
|AREA|SRC_80|Cam_Pta_11-PEAS e Imp|273447|6383229|3 meses|400,03|3,17,E-09|7,67,E-10|1,39,E-09|2,43,E-08|5,77,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 220 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>273463|[m]<br>6383220|[m]<br>6383220|[m2]<br>80,13|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_81|Cam_Pta_12-PEAS e Imp|Cam_Pta_12-PEAS e Imp|Cam_Pta_12-PEAS e Imp|3 meses|3 meses|1,58,E-08|3,83,E-09|6,93,E-09|1,21,E-07|2,88,E-08|
|AREA|SRC_82|Cam_Pta_13-PEAS e Imp|273473|6383218|3 meses|45,12|2,81,E-08|6,80,E-09|1,23,E-08|2,15,E-07|5,11,E-08|
|AREA|SRC_83|Cam_Pta_14-PEAS e Imp|273519|6383228|3 meses|188,53|6,72,E-09|1,63,E-09|2,94,E-09|5,15,E-08|1,22,E-08|
|AREA|SRC_84|Cam_Valpo_1-PEAS e Imp|267407|6370003|3 meses|9181,86|1,38,E-10|3,34,E-11|6,04,E-11|1,06,E-09|2,51,E-10|
|AREA|SRC_85|Cam_Valpo_2-PEAS e Imp|267402|6370088|3 meses|338,29|3,75,E-09|9,07,E-10|1,64,E-09|2,87,E-08|6,82,E-09|
|AREA|SRC_86|Cam_Valpo_3-PEAS e Imp|267699|6371506|3 meses|5788,94|2,19,E-10|5,30,E-11|9,59,E-11|1,68,E-09|3,98,E-10|
|AREA|SRC_87|Cam_Valpo_4-PEAS e Imp|267700|6371619|3 meses|452,00|2,80,E-09|6,79,E-10|1,23,E-09|2,15,E-08|5,10,E-09|
|AREA|SRC_88|Cam_Valpo_5-PEAS e Imp|267517|6371917|3 meses|1401,44|9,05,E-10|2,19,E-10|3,96,E-10|6,93,E-09|1,65,E-09|
|AREA|SRC_89|Cam_Valpo_6-PEAS e Imp|267499|6371980|3 meses|261,10|4,86,E-09|1,17,E-09|2,13,E-09|3,72,E-08|8,83,E-09|
|AREA|SRC_90|Cam_Valpo_7-PEAS e Imp|267496|6372042|3 meses|247,03|5,13,E-09|1,24,E-09|2,25,E-09|3,93,E-08|9,34,E-09|
|AREA|SRC_91|Cam_Valpo_8-PEAS e Imp|267518|6372113|3 meses|294,47|4,31,E-09|1,04,E-09|1,88,E-09|3,30,E-08|7,83,E-09|
|AREA|SRC_92|Cam_Valpo_9-PEAS e Imp|267547|6372151|3 meses|187,43|6,76,E-09|1,64,E-09|2,96,E-09|5,18,E-08|1,23,E-08|
|AREA|SRC_93|Cam_Valpo_10-PEAS e Imp|267569|6372177|3 meses|137,02|9,25,E-09|2,24,E-09|4,05,E-09|7,09,E-08|1,68,E-08|
|AREA|SRC_94|Cam_Valpo_11-PEAS e Imp|267738|6372319|3 meses|879,83|1,44,E-09|3,49,E-10|6,31,E-10|1,10,E-08|2,62,E-09|
|AREA|SRC_95|Cam_Valpo_12-PEAS e Imp|267762|6372358|3 meses|186,57|6,80,E-09|1,64,E-09|2,97,E-09|5,20,E-08|1,24,E-08|
|AREA|SRC_96|Cam_Valpo_13-PEAS e Imp|267783|6372410|3 meses|224,51|5,65,E-09|1,37,E-09|2,47,E-09|4,32,E-08|1,03,E-08|
|AREA|SRC_97|Cam_Valpo_14-PEAS e Imp|267855|6372669|3 meses|1075,61|1,18,E-09|2,85,E-10|5,16,E-10|9,03,E-09|2,14,E-09|
|AREA|SRC_98|Cam_Valpo_15-PEAS e Imp|267848|6372720|3 meses|207,78|6,10,E-09|1,48,E-09|2,67,E-09|4,67,E-08|1,11,E-08|
|AREA|SRC_99|Cam_Valpo_16-PEAS e Imp|267715|6373066|3 meses|1484,08|8,54,E-10|2,07,E-10|3,74,E-10|6,54,E-09|1,55,E-09|
|AREA|SRC_100|Cam_Valpo_17-PEAS e Imp|267705|6373122|3 meses|225,43|5,62,E-09|1,36,E-09|2,46,E-09|4,31,E-08|1,02,E-08|
|AREA|SRC_101|Cam_Valpo_18-PEAS e Imp|267701|6373182|3 meses|241,22|5,26,E-09|1,27,E-09|2,30,E-09|4,02,E-08|9,56,E-09|
|AREA|SRC_102|Cam_Valpo_19-PEAS e Imp|267704|6373237|3 meses|217,96|5,82,E-09|1,41,E-09|2,55,E-09|4,45,E-08|1,06,E-08|
|AREA|SRC_103|Cam_Valpo_20-PEAS e Imp|267713|6373309|3 meses|291,26|4,35,E-09|1,05,E-09|1,91,E-09|3,33,E-08|7,92,E-09|
|AREA|SRC_104|Cam_Valpo_21-PEAS e Imp|267741|6373522|3 meses|860,16|1,47,E-09|3,57,E-10|6,45,E-10|1,13,E-08|2,68,E-09|
|AREA|SRC_105|Cam_Valpo_22-PEAS e Imp|267757|6373574|3 meses|213,85|5,93,E-09|1,43,E-09|2,59,E-09|4,54,E-08|1,08,E-08|
|AREA|SRC_106|Cam_Valpo_23-PEAS e Imp|267777|6373617|3 meses|187,32|6,77,E-09|1,64,E-09|2,96,E-09|5,18,E-08|1,23,E-08|
|AREA|SRC_107|Cam_Valpo_24-PEAS e Imp|267817|6373719|3 meses|441,14|2,87,E-09|6,95,E-10|1,26,E-09|2,20,E-08|5,23,E-09|
|AREA|SRC_108|Cam_Valpo_25-PEAS e Imp|267843|6373782|3 meses|272,58|4,65,E-09|1,13,E-09|2,04,E-09|3,56,E-08|8,46,E-09|
|AREA|SRC_109|Cam_Valpo_26-PEAS e Imp|267877|6373831|3 meses|236,03|5,37,E-09|1,30,E-09|2,35,E-09|4,11,E-08|9,77,E-09|
|AREA|SRC_110|Cam_Valpo_27-PEAS e Imp|267910|6373883|3 meses|246,12|5,15,E-09|1,25,E-09|2,25,E-09|3,94,E-08|9,37,E-09|
|AREA|SRC_111|Cam_Valpo_28-PEAS e Imp|268105|6374174|3 meses|1399,53|9,06,E-10|2,19,E-10|3,97,E-10|6,94,E-09|1,65,E-09|
|AREA|SRC_112|Cam_Valpo_29-PEAS e Imp|268274|6374430|3 meses|1228,07|1,03,E-09|2,50,E-10|4,52,E-10|7,91,E-09|1,88,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 221 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>268317|[m]<br>6374478|[m]<br>6374478|[m2]<br>254,35|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_113|Cam_Valpo_30-PEAS e Imp|Cam_Valpo_30-PEAS e Imp|Cam_Valpo_30-PEAS e Imp|3 meses|3 meses|4,98,E-09|1,21,E-09|2,18,E-09|3,82,E-08|9,07,E-09|
|AREA|SRC_114|Cam_Valpo_31-PEAS e Imp|268347|6374502|3 meses|154,46|8,21,E-09|1,99,E-09|3,59,E-09|6,29,E-08|1,49,E-08|
|AREA|SRC_115|Cam_Valpo_32-PEAS e Imp|269602|6375295|3 meses|5935,56|2,14,E-10|5,17,E-11|9,35,E-11|1,64,E-09|3,89,E-10|
|AREA|SRC_116|Cam_Valpo_33-PEAS e Imp|270646|6375956|3 meses|4938,33|2,57,E-10|6,21,E-11|1,12,E-10|1,97,E-09|4,67,E-10|
|AREA|SRC_117|Cam_Valpo_34-PEAS e Imp|270700|6375970|3 meses|220,74|5,74,E-09|1,39,E-09|2,51,E-09|4,40,E-08|1,04,E-08|
|AREA|SRC_118|Cam_Valpo_35-PEAS e Imp|270759|6375972|3 meses|232,03|5,46,E-09|1,32,E-09|2,39,E-09|4,18,E-08|9,94,E-09|
|AREA|SRC_119|Cam_Valpo_36-PEAS e Imp|270817|6375960|3 meses|237,83|5,33,E-09|1,29,E-09|2,33,E-09|4,08,E-08|9,70,E-09|
|AREA|SRC_120|Cam_Valpo_37-PEAS e Imp|271210|6375788|3 meses|1710,95|7,41,E-10|1,79,E-10|3,24,E-10|5,67,E-09|1,35,E-09|
|AREA|SRC_121|Cam_Valpo_38-PEAS e Imp|271299|6375786|3 meses|362,06|3,50,E-09|8,47,E-10|1,53,E-09|2,68,E-08|6,37,E-09|
|AREA|SRC_122|Cam_Valpo_39-PEAS e Imp|271410|6375784|3 meses|444,09|2,85,E-09|6,91,E-10|1,25,E-09|2,19,E-08|5,19,E-09|
|AREA|SRC_123|Cam_Valpo_40-PEAS e Imp|271537|6375829|3 meses|539,94|2,35,E-09|5,68,E-10|1,03,E-09|1,80,E-08|4,27,E-09|
|AREA|SRC_124|Cam_Valpo_41-PEAS e Imp|271698|6375908|3 meses|717,64|1,77,E-09|4,27,E-10|7,73,E-10|1,35,E-08|3,21,E-09|
|AREA|SRC_125|Cam_Valpo_42-PEAS e Imp|271943|6376040|3 meses|1111,41|1,14,E-09|2,76,E-10|4,99,E-10|8,74,E-09|2,08,E-09|
|AREA|SRC_126|Cam_Valpo_43-PEAS e Imp|272216|6376245|3 meses|1365,82|9,28,E-10|2,25,E-10|4,06,E-10|7,11,E-09|1,69,E-09|
|AREA|SRC_127|Cam_Valpo_44-PEAS e Imp|272308|6376283|3 meses|396,81|3,20,E-09|7,73,E-10|1,40,E-09|2,45,E-08|5,81,E-09|
|AREA|SRC_128|Cam_Valpo_45-PEAS e Imp|272828|6376412|3 meses|2139,51|5,93,E-10|1,43,E-10|2,59,E-10|4,54,E-09|1,08,E-09|
|AREA|SRC_129|Cam_Valpo_46-PEAS e Imp|272961|6376463|3 meses|572,90|2,21,E-09|5,35,E-10|9,69,E-10|1,69,E-08|4,03,E-09|
|AREA|SRC_130|Cam_Valpo_47-PEAS e Imp|273101|6376548|3 meses|656,43|1,93,E-09|4,67,E-10|8,45,E-10|1,48,E-08|3,51,E-09|
|AREA|SRC_131|Cam_Valpo_48-PEAS e Imp|273683|6376890|3 meses|2699,98|4,70,E-10|1,14,E-10|2,06,E-10|3,60,E-09|8,54,E-10|
|AREA|SRC_132|Cam_Valpo_49-PEAS e Imp|273729|6376911|3 meses|198,66|6,38,E-09|1,54,E-09|2,79,E-09|4,89,E-08|1,16,E-08|
|AREA|SRC_133|Cam_Valpo_50-PEAS e Imp|273841|6376934|3 meses|455,50|2,78,E-09|6,73,E-10|1,22,E-09|2,13,E-08|5,06,E-09|
|AREA|SRC_134|Cam_Valpo_51-PEAS e Imp|273918|6376948|3 meses|314,84|4,03,E-09|9,74,E-10|1,76,E-09|3,08,E-08|7,33,E-09|
|AREA|SRC_135|Cam_Valpo_52-PEAS e Imp|273963|6376959|3 meses|182,29|6,96,E-09|1,68,E-09|3,04,E-09|5,33,E-08|1,27,E-08|
|AREA|SRC_136|Cam_Valpo_53-PEAS e Imp|274013|6376981|3 meses|220,22|5,76,E-09|1,39,E-09|2,52,E-09|4,41,E-08|1,05,E-08|
|AREA|SRC_137|Cam_Valpo_54-PEAS e Imp|274045|6377010|3 meses|175,74|7,21,E-09|1,75,E-09|3,16,E-09|5,52,E-08|1,31,E-08|
|AREA|SRC_138|Cam_Valpo_55-PEAS e Imp|274402|6377569|3 meses|2654,98|4,78,E-10|1,16,E-10|2,09,E-10|3,66,E-09|8,69,E-10|
|AREA|SRC_139|Cam_Valpo_56-PEAS e Imp|274508|6377712|3 meses|712,20|1,78,E-09|4,31,E-10|7,79,E-10|1,36,E-08|3,24,E-09|
|AREA|SRC_140|Cam_Valpo_57-PEAS e Imp|274515|6377737|3 meses|105,54|1,20,E-08|2,91,E-09|5,26,E-09|9,20,E-08|2,19,E-08|
|AREA|SRC_141|Cam_Valpo_58-PEAS e Imp|274530|6377783|3 meses|190,85|6,64,E-09|1,61,E-09|2,91,E-09|5,09,E-08|1,21,E-08|
|AREA|SRC_142|Cam_Valpo_59-PEAS e Imp|274571|6378190|3 meses|1640,54|7,73,E-10|1,87,E-10|3,38,E-10|5,92,E-09|1,41,E-09|
|AREA|SRC_143|Cam_Valpo_60-PEAS e Imp|274512|6378662|3 meses|1902,24|6,66,E-10|1,61,E-10|2,92,E-10|5,10,E-09|1,21,E-09|
|AREA|SRC_144|Cam_Valpo_61-PEAS e Imp|274484|6378742|3 meses|339,36|3,74,E-09|9,04,E-10|1,64,E-09|2,86,E-08|6,80,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 222 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>274397|[m]<br>6378959|[m]<br>6378959|[m2]<br>934,88|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_145|Cam_Valpo_62-PEAS e Imp|Cam_Valpo_62-PEAS e Imp|Cam_Valpo_62-PEAS e Imp|3 meses|3 meses|1,36,E-09|3,28,E-10|5,94,E-10|1,04,E-08|2,47,E-09|
|AREA|SRC_146|Cam_Valpo_63-PEAS e Imp|274391|6379006|3 meses|189,58|6,69,E-09|1,62,E-09|2,93,E-09|5,12,E-08|1,22,E-08|
|AREA|SRC_147|Cam_Valpo_64-PEAS e Imp|274392|6379034|3 meses|109,49|1,16,E-08|2,80,E-09|5,07,E-09|8,87,E-08|2,11,E-08|
|AREA|SRC_148|Cam_Valpo_65-PEAS e Imp|274513|6379469|3 meses|1805,57|7,02,E-10|1,70,E-10|3,07,E-10|5,38,E-09|1,28,E-09|
|AREA|SRC_149|Cam_Valpo_66-PEAS e Imp|274514|6379510|3 meses|163,36|7,76,E-09|1,88,E-09|3,40,E-09|5,94,E-08|1,41,E-08|
|AREA|SRC_150|Cam_Valpo_67-PEAS e Imp|274503|6379560|3 meses|208,73|6,07,E-09|1,47,E-09|2,66,E-09|4,65,E-08|1,11,E-08|
|AREA|SRC_151|Cam_Valpo_68-PEAS e Imp|274488|6379623|3 meses|255,44|4,96,E-09|1,20,E-09|2,17,E-09|3,80,E-08|9,03,E-09|
|AREA|SRC_152|Cam_Valpo_69-PEAS e Imp|274426|6379798|3 meses|745,56|1,70,E-09|4,11,E-10|7,44,E-10|1,30,E-08|3,09,E-09|
|AREA|SRC_153|Cam_Valpo_70-PEAS e Imp|274386|6379897|3 meses|428,53|2,96,E-09|7,16,E-10|1,29,E-09|2,27,E-08|5,38,E-09|
|AREA|SRC_154|Cam_Valpo_71-PEAS e Imp|274352|6379981|3 meses|360,23|3,52,E-09|8,51,E-10|1,54,E-09|2,70,E-08|6,40,E-09|
|AREA|SRC_155|Cam_Valpo_72-PEAS e Imp|274336|6380041|3 meses|249,49|5,08,E-09|1,23,E-09|2,22,E-09|3,89,E-08|9,25,E-09|
|AREA|SRC_156|Cam_Valpo_73-PEAS e Imp|274333|6380099|3 meses|227,80|5,57,E-09|1,35,E-09|2,44,E-09|4,26,E-08|1,01,E-08|
|AREA|SRC_157|Cam_Valpo_74-PEAS e Imp|274332|6380163|3 meses|257,27|4,93,E-09|1,19,E-09|2,16,E-09|3,77,E-08|8,97,E-09|
|AREA|SRC_158|Cam_Valpo_75-PEAS e Imp|274329|6380546|3 meses|1530,44|8,28,E-10|2,00,E-10|3,63,E-10|6,34,E-09|1,51,E-09|
|AREA|SRC_159|Cam_Valpo_76-PEAS e Imp|274323|6380578|3 meses|130,55|9,71,E-09|2,35,E-09|4,25,E-09|7,44,E-08|1,77,E-08|
|AREA|SRC_160|Cam_Valpo_77-PEAS e Imp|274308|6380608|3 meses|138,17|9,18,E-09|2,22,E-09|4,02,E-09|7,03,E-08|1,67,E-08|
|AREA|SRC_161|Cam_Valpo_78-PEAS e Imp|274078|6381086|3 meses|2120,50|5,98,E-10|1,45,E-10|2,62,E-10|4,58,E-09|1,09,E-09|
|AREA|SRC_162|Cam_Valpo_79-PEAS e Imp|274036|6381146|3 meses|292,96|4,33,E-09|1,05,E-09|1,89,E-09|3,31,E-08|7,87,E-09|
|AREA|SRC_163|Cam_Valpo_80-PEAS e Imp|273997|6381192|3 meses|242,71|5,22,E-09|1,26,E-09|2,29,E-09|4,00,E-08|9,50,E-09|
|AREA|SRC_164|Cam_Valpo_81-PEAS e Imp|273945|6381212|3 meses|225,25|5,63,E-09|1,36,E-09|2,46,E-09|4,31,E-08|1,02,E-08|
|AREA|SRC_165|Cam_Valpo_82-PEAS e Imp|273863|6381235|3 meses|340,59|3,72,E-09|9,01,E-10|1,63,E-09|2,85,E-08|6,77,E-09|
|AREA|SRC_166|Cam_Valpo_83-PEAS e Imp|273527|6381309|3 meses|1376,67|9,21,E-10|2,23,E-10|4,03,E-10|7,05,E-09|1,68,E-09|
|AREA|SRC_167|Cam_Valpo_84-PEAS e Imp|273488|6381317|3 meses|158,83|7,98,E-09|1,93,E-09|3,49,E-09|6,11,E-08|1,45,E-08|
|AREA|SRC_168|Cam_Valpo_85-PEAS e Imp|273437|6381311|3 meses|210,61|6,02,E-09|1,46,E-09|2,63,E-09|4,61,E-08|1,10,E-08|
|AREA|SRC_169|Cam_Valpo_86-PEAS e Imp|273400|6381306|3 meses|148,75|8,52,E-09|2,06,E-09|3,73,E-09|6,53,E-08|1,55,E-08|
|AREA|SRC_170|Cam_Valpo_87-PEAS e Imp|273330|6381278|3 meses|302,02|4,20,E-09|1,02,E-09|1,84,E-09|3,21,E-08|7,64,E-09|
|AREA|SRC_171|Cam_Valpo_88-PEAS e Imp|273269|6381275|3 meses|240,32|5,28,E-09|1,28,E-09|2,31,E-09|4,04,E-08|9,60,E-09|
|AREA|SRC_172|Cam_Valpo_89-PEAS e Imp|273210|6381284|3 meses|238,69|5,31,E-09|1,29,E-09|2,32,E-09|4,07,E-08|9,66,E-09|
|AREA|SRC_173|Cam_Valpo_90-PEAS e Imp|273140|6381307|3 meses|291,89|4,34,E-09|1,05,E-09|1,90,E-09|3,33,E-08|7,90,E-09|
|AREA|SRC_174|Cam_Valpo_91-PEAS e Imp|273026|6381364|3 meses|510,61|2,48,E-09|6,01,E-10|1,09,E-09|1,90,E-08|4,52,E-09|
|AREA|SRC_175|Cam_Valpo_92-PEAS e Imp|272787|6381471|3 meses|1046,47|1,21,E-09|2,93,E-10|5,30,E-10|9,28,E-09|2,20,E-09|
|AREA|SRC_176|Cam_Valpo_93-PEAS e Imp|272625|6381553|3 meses|726,81|1,74,E-09|4,22,E-10|7,64,E-10|1,34,E-08|3,17,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 223 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>272586|[m]<br>6381587|[m]<br>6381587|[m2]<br>205,87|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_177|Cam_Valpo_94-PEAS e Imp|Cam_Valpo_94-PEAS e Imp|Cam_Valpo_94-PEAS e Imp|3 meses|3 meses|6,16,E-09|1,49,E-09|2,70,E-09|4,72,E-08|1,12,E-08|
|AREA|SRC_178|Cam_Valpo_95-PEAS e Imp|272567|6381621|3 meses|150,25|8,44,E-09|2,04,E-09|3,69,E-09|6,46,E-08|1,54,E-08|
|AREA|SRC_179|Cam_Valpo_96-PEAS e Imp|272558|6381659|3 meses|154,59|8,20,E-09|1,98,E-09|3,59,E-09|6,28,E-08|1,49,E-08|
|AREA|SRC_180|Cam_Valpo_97-PEAS e Imp|272513|6381931|3 meses|1103,20|1,15,E-09|2,78,E-10|5,03,E-10|8,80,E-09|2,09,E-09|
|AREA|SRC_181|Cam_Valpo_98-PEAS e Imp|272500|6382030|3 meses|398,37|3,18,E-09|7,70,E-10|1,39,E-09|2,44,E-08|5,79,E-09|
|AREA|SRC_182|Cam_Valpo_99-PEAS e Imp|272492|6382086|3 meses|223,87|5,66,E-09|1,37,E-09|2,48,E-09|4,34,E-08|1,03,E-08|
|AREA|SRC_183|Cam_Valpo_100-PEAS e Imp|272491|6382127|3 meses|164,32|7,72,E-09|1,87,E-09|3,38,E-09|5,91,E-08|1,40,E-08|
|AREA|SRC_184|Cam_Valpo_101-PEAS e Imp|272506|6382188|3 meses|247,33|5,13,E-09|1,24,E-09|2,24,E-09|3,93,E-08|9,33,E-09|
|AREA|SRC_185|Cam_Valpo_102-PEAS e Imp|272660|6383439|3 meses|5043,31|2,51,E-10|6,08,E-11|1,10,E-10|1,93,E-09|4,57,E-10|
|AREA|SRC_186|Cam_Valpo_103-PEAS e Imp|272630|6384559|3 meses|4478,91|2,83,E-10|6,85,E-11|1,24,E-10|2,17,E-09|5,15,E-10|
|AREA|SRC_187|Cam_Valpo_104-PEAS e Imp|272626|6385227|3 meses|2671,08|4,75,E-10|1,15,E-10|2,08,E-10|3,63,E-09|8,64,E-10|
|AREA|SRC_188|Cam_Valpo_105-PEAS e Imp|272602|6386454|3 meses|4905,80|2,58,E-10|6,25,E-11|1,13,E-10|1,98,E-09|4,70,E-10|
|AREA|SRC_189|Cam_Valpo_106-PEAS e Imp|272609|6386527|3 meses|292,53|4,33,E-09|1,05,E-09|1,90,E-09|3,32,E-08|7,88,E-09|
|AREA|SRC_190|Cam_Valpo_107-PEAS e Imp|272650|6386615|3 meses|384,69|3,30,E-09|7,97,E-10|1,44,E-09|2,52,E-08|6,00,E-09|
|AREA|SRC_191|Cam_Valpo_108-PEAS e Imp|272755|6386705|3 meses|550,00|2,31,E-09|5,58,E-10|1,01,E-09|1,77,E-08|4,19,E-09|
|AREA|SRC_192|Cam_Valpo_109-PEAS e Imp|272846|6386776|3 meses|460,85|2,75,E-09|6,66,E-10|1,20,E-09|2,11,E-08|5,00,E-09|
|AREA|SRC_193|Cam_Valpo_110-PEAS e Imp|272918|6386821|3 meses|338,79|3,74,E-09|9,05,E-10|1,64,E-09|2,87,E-08|6,81,E-09|
|AREA|SRC_194|Cam_Valpo_111-PEAS e Imp|272959|6386856|3 meses|215,71|5,88,E-09|1,42,E-09|2,57,E-09|4,50,E-08|1,07,E-08|
|AREA|SRC_195|Cam_Valpo_112-PEAS e Imp|272979|6386909|3 meses|229,32|5,53,E-09|1,34,E-09|2,42,E-09|4,23,E-08|1,01,E-08|
|AREA|SRC_196|Cam_Valpo_113-PEAS e Imp|272982|6386950|3 meses|168,20|7,54,E-09|1,82,E-09|3,30,E-09|5,77,E-08|1,37,E-08|
|AREA|SRC_197|Cam_Valpo_114-PEAS e Imp|272974|6387033|3 meses|334,56|3,79,E-09|9,17,E-10|1,66,E-09|2,90,E-08|6,89,E-09|
|AREA|SRC_198|Cam_Valpo_115-PEAS e Imp|272969|6387289|3 meses|1021,26|1,24,E-09|3,00,E-10|5,43,E-10|9,51,E-09|2,26,E-09|
|AREA|SRC_199|Cam_Valpo_116-PEAS e Imp|272950|6387316|3 meses|135,86|9,33,E-09|2,26,E-09|4,08,E-09|7,15,E-08|1,70,E-08|
|AREA|SRC_200|Cam_Valpo_117-PEAS e Imp|272918|6387332|3 meses|150,62|8,42,E-09|2,04,E-09|3,68,E-09|6,45,E-08|1,53,E-08|
|AREA|SRC_201|Cam_Valpo_118-PEAS e Imp|272871|6387328|3 meses|193,11|6,57,E-09|1,59,E-09|2,87,E-09|5,03,E-08|1,19,E-08|
|AREA|SRC_202|Cam_Valpo_119-PEAS e Imp|272818|6387319|3 meses|214,82|5,90,E-09|1,43,E-09|2,58,E-09|4,52,E-08|1,07,E-08|
|AREA|SRC_203|Cam_Valpo_120-PEAS e Imp|272669|6387324|3 meses|593,51|2,14,E-09|5,17,E-10|9,35,E-10|1,64,E-08|3,89,E-09|
|AREA|SRC_204|Cam_Valpo_121-PEAS e Imp|272536|6387380|3 meses|574,11|2,21,E-09|5,34,E-10|9,67,E-10|1,69,E-08|4,02,E-09|
|AREA|SRC_205|Cam_Valpo_122-PEAS e Imp|272406|6387475|3 meses|642,85|1,97,E-09|4,77,E-10|8,63,E-10|1,51,E-08|3,59,E-09|
|AREA|SRC_206|Cam_Valpo_123-PEAS e Imp|272321|6387544|3 meses|438,86|2,89,E-09|6,99,E-10|1,26,E-09|2,21,E-08|5,26,E-09|
|AREA|SRC_207|Cam_Valpo_124-PEAS e Imp|272252|6387605|3 meses|366,01|3,46,E-09|8,38,E-10|1,52,E-09|2,65,E-08|6,30,E-09|
|AREA|SRC_208|Cam_Valpo_125-PEAS e Imp|272138|6387749|3 meses|733,97|1,73,E-09|4,18,E-10|7,56,E-10|1,32,E-08|3,14,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 224 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>272059|[m]<br>6387890|[m]<br>6387890|[m2]<br>645,70|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_209|Cam_Valpo_126-PEAS e Imp|Cam_Valpo_126-PEAS e Imp|Cam_Valpo_126-PEAS e Imp|3 meses|3 meses|1,96,E-09|4,75,E-10|8,59,E-10|1,50,E-08|3,57,E-09|
|AREA|SRC_210|Cam_Valpo_127-PEAS e Imp|272019|6388008|3 meses|494,29|2,56,E-09|6,21,E-10|1,12,E-09|1,96,E-08|4,67,E-09|
|AREA|SRC_211|Cam_Valpo_128-PEAS e Imp|272005|6388086|3 meses|318,17|3,98,E-09|9,64,E-10|1,74,E-09|3,05,E-08|7,25,E-09|
|AREA|SRC_212|Cam_Valpo_129-PEAS e Imp|272005|6388171|3 meses|338,40|3,75,E-09|9,06,E-10|1,64,E-09|2,87,E-08|6,82,E-09|
|AREA|SRC_213|Cam_Valpo_130-PEAS e Imp|272018|6388207|3 meses|149,40|8,49,E-09|2,05,E-09|3,71,E-09|6,50,E-08|1,54,E-08|
|AREA|SRC_214|Cam_Valpo_131-PEAS e Imp|272053|6388222|3 meses|144,57|8,77,E-09|2,12,E-09|3,84,E-09|6,72,E-08|1,60,E-08|
|AREA|SRC_215|Cam_Valpo_132-PEAS e Imp|272113|6388260|3 meses|286,19|4,43,E-09|1,07,E-09|1,94,E-09|3,39,E-08|8,06,E-09|
|AREA|SRC_216|Cam_Valpo_133-PEAS e Imp|272165|6388289|3 meses|236,50|5,36,E-09|1,30,E-09|2,35,E-09|4,11,E-08|9,75,E-09|
|AREA|SRC_217|Cam_Valpo_134-PEAS e Imp|272170|6388313|3 meses|103,04|1,23,E-08|2,98,E-09|5,39,E-09|9,42,E-08|2,24,E-08|
|AREA|SRC_218|Cam_Valpo_135-PEAS e Imp|272160|6388355|3 meses|178,67|7,10,E-09|1,72,E-09|3,11,E-09|5,43,E-08|1,29,E-08|
|AREA|SRC_219|Cam_Valpo_136-PEAS e Imp|272116|6388384|3 meses|213,17|5,95,E-09|1,44,E-09|2,60,E-09|4,55,E-08|1,08,E-08|
|AREA|SRC_220|Cam_Valpo_137-PEAS e Imp|271990|6388473|3 meses|618,26|2,05,E-09|4,96,E-10|8,98,E-10|1,57,E-08|3,73,E-09|
|AREA|SRC_221|Cam_Valpo_138-PEAS e Imp|271909|6388570|3 meses|502,24|2,52,E-09|6,11,E-10|1,10,E-09|1,93,E-08|4,59,E-09|
|AREA|SRC_222|Cam_Valpo_139-PEAS e Imp|271887|6388631|3 meses|257,67|4,92,E-09|1,19,E-09|2,15,E-09|3,77,E-08|8,95,E-09|
|AREA|SRC_223|Cam_Valpo_140-PEAS e Imp|271869|6388710|3 meses|324,57|3,91,E-09|9,45,E-10|1,71,E-09|2,99,E-08|7,11,E-09|
|AREA|SRC_224|Cam_Valpo_141-PEAS e Imp|271879|6388778|3 meses|270,72|4,68,E-09|1,13,E-09|2,05,E-09|3,59,E-08|8,52,E-09|
|AREA|SRC_225|Cam_Valpo_142-PEAS e Imp|271889|6388831|3 meses|215,81|5,87,E-09|1,42,E-09|2,57,E-09|4,50,E-08|1,07,E-08|
|AREA|SRC_226|Cam_Valpo_143-PEAS e Imp|271888|6388910|3 meses|317,54|3,99,E-09|9,66,E-10|1,75,E-09|3,06,E-08|7,26,E-09|
|AREA|SRC_227|Cam_Valpo_144-PEAS e Imp|271765|6389249|3 meses|1443,83|8,78,E-10|2,12,E-10|3,84,E-10|6,72,E-09|1,60,E-09|
|AREA|SRC_228|Cam_Valpo_145-PEAS e Imp|271745|6389323|3 meses|308,68|4,11,E-09|9,94,E-10|1,80,E-09|3,15,E-08|7,47,E-09|
|AREA|SRC_229|Cam_Valpo_146-PEAS e Imp|271746|6389404|3 meses|321,13|3,95,E-09|9,55,E-10|1,73,E-09|3,02,E-08|7,18,E-09|
|AREA|SRC_230|Cam_Valpo_147-PEAS e Imp|271745|6389713|3 meses|1235,33|1,03,E-09|2,48,E-10|4,49,E-10|7,86,E-09|1,87,E-09|
|AREA|SRC_231|Cam_Valpo_148-PEAS e Imp|271729|6389779|3 meses|274,74|4,61,E-09|1,12,E-09|2,02,E-09|3,53,E-08|8,40,E-09|
|AREA|SRC_232|Cam_Valpo_149-PEAS e Imp|271405|6390771|3 meses|4169,69|3,04,E-10|7,36,E-11|1,33,E-10|2,33,E-09|5,53,E-10|
|AREA|SRC_233|Cam_Valpo_150-PEAS e Imp|271408|6390852|3 meses|324,07|3,91,E-09|9,46,E-10|1,71,E-09|3,00,E-08|7,12,E-09|
|AREA|SRC_234|Cam_Valpo_151-PEAS e Imp|271425|6390918|3 meses|269,76|4,70,E-09|1,14,E-09|2,06,E-09|3,60,E-08|8,55,E-09|
|AREA|SRC_235|Cam_Valpo_152-PEAS e Imp|271595|6391444|3 meses|2210,20|5,74,E-10|1,39,E-10|2,51,E-10|4,39,E-09|1,04,E-09|
|AREA|SRC_236|Cam_Valpo_153-PEAS e Imp|271601|6391518|3 meses|297,07|4,27,E-09|1,03,E-09|1,87,E-09|3,27,E-08|7,76,E-09|
|AREA|SRC_237|Cam_Valpo_154-PEAS e Imp|271583|6391599|3 meses|334,56|3,79,E-09|9,17,E-10|1,66,E-09|2,90,E-08|6,89,E-09|
|AREA|SRC_238|Cam_Valpo_155-PEAS e Imp|271490|6391665|3 meses|462,29|2,74,E-09|6,64,E-10|1,20,E-09|2,10,E-08|4,99,E-09|
|AREA|SRC_239|Cam_Valpo_156-PEAS e Imp|271388|6391779|3 meses|610,49|2,08,E-09|5,02,E-10|9,09,E-10|1,59,E-08|3,78,E-09|
|AREA|SRC_240|Cam_Valpo_157-PEAS e Imp|271303|6391969|3 meses|829,95|1,53,E-09|3,70,E-10|6,69,E-10|1,17,E-08|2,78,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 225 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>271249|[m]<br>6392048|[m]<br>6392048|[m2]<br>385,48|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_241|Cam_Valpo_158-PEAS e Imp|Cam_Valpo_158-PEAS e Imp|Cam_Valpo_158-PEAS e Imp|3 meses|3 meses|3,29,E-09|7,96,E-10|1,44,E-09|2,52,E-08|5,98,E-09|
|AREA|SRC_242|Cam_Valpo_159-PEAS e Imp|271095|6392199|3 meses|863,11|1,47,E-09|3,55,E-10|6,43,E-10|1,12,E-08|2,67,E-09|
|AREA|SRC_243|Cam_Valpo_160-PEAS e Imp|271003|6392357|3 meses|727,41|1,74,E-09|4,22,E-10|7,63,E-10|1,33,E-08|3,17,E-09|
|AREA|SRC_244|Cam_Valpo_161-PEAS e Imp|270864|6392618|3 meses|1181,67|1,07,E-09|2,60,E-10|4,70,E-10|8,22,E-09|1,95,E-09|
|AREA|SRC_245|Cam_Valpo_162-PEAS e Imp|270665|6392901|3 meses|1386,67|9,14,E-10|2,21,E-10|4,00,E-10|7,00,E-09|1,66,E-09|
|AREA|SRC_246|Cam_Valpo_163-PEAS e Imp|270570|6393060|3 meses|739,81|1,71,E-09|4,15,E-10|7,50,E-10|1,31,E-08|3,12,E-09|
|AREA|SRC_247|Cam_Valpo_164-PEAS e Imp|270535|6393162|3 meses|427,94|2,96,E-09|7,17,E-10|1,30,E-09|2,27,E-08|5,39,E-09|
|AREA|SRC_248|Cam_Valpo_165-PEAS e Imp|270408|6393157|3 meses|516,16|2,46,E-09|5,94,E-10|1,08,E-09|1,88,E-08|4,47,E-09|
|AREA|SRC_249|Cam_Valpo_166-PEAS e Imp|270322|6393156|3 meses|344,11|3,68,E-09|8,91,E-10|1,61,E-09|2,82,E-08|6,70,E-09|
|AREA|SRC_250|Cam_Valpo_167-PEAS e Imp|270198|6393225|3 meses|562,03|2,26,E-09|5,46,E-10|9,87,E-10|1,73,E-08|4,10,E-09|
|AREA|SRC_251|Cam_Valpo_168-PEAS e Imp|270084|6393222|3 meses|461,57|2,75,E-09|6,65,E-10|1,20,E-09|2,10,E-08|5,00,E-09|
|AREA|SRC_252|Cam_Valpo_169-PEAS e Imp|270014|6393114|3 meses|520,05|2,44,E-09|5,90,E-10|1,07,E-09|1,87,E-08|4,44,E-09|
|AREA|SRC_253|Cam_Valpo_170-PEAS e Imp|269944|6393026|3 meses|448,19|2,83,E-09|6,84,E-10|1,24,E-09|2,17,E-08|5,15,E-09|
|AREA|SRC_254|Cam_Valpo_171-PEAS e Imp|269831|6392981|3 meses|484,35|2,62,E-09|6,33,E-10|1,15,E-09|2,00,E-08|4,76,E-09|
|AREA|SRC_255|Cam_Valpo_172-PEAS e Imp|269702|6392966|3 meses|516,99|2,45,E-09|5,93,E-10|1,07,E-09|1,88,E-08|4,46,E-09|
|AREA|SRC_256|Cam_Valpo_173-PEAS e Imp|269506|6393084|3 meses|906,73|1,40,E-09|3,38,E-10|6,12,E-10|1,07,E-08|2,54,E-09|
|AREA|SRC_257|Cam_Valpo_174-PEAS e Imp|269407|6393106|3 meses|410,62|3,09,E-09|7,47,E-10|1,35,E-09|2,36,E-08|5,62,E-09|
|AREA|SRC_258|Cam_Valpo_175-PEAS e Imp|269355|6393219|3 meses|493,13|2,57,E-09|6,22,E-10|1,13,E-09|1,97,E-08|4,68,E-09|
|AREA|SRC_259|Cam_Valpo_176-PEAS e Imp|269450|6393436|3 meses|939,57|1,35,E-09|3,26,E-10|5,91,E-10|1,03,E-08|2,45,E-09|
|AREA|SRC_260|Cam_Valpo_177-PEAS e Imp|269537|6393768|3 meses|1375,49|9,22,E-10|2,23,E-10|4,03,E-10|7,06,E-09|1,68,E-09|
|AREA|SRC_261|Cam_Valpo_178-PEAS e Imp|269541|6393876|3 meses|433,16|2,93,E-09|7,08,E-10|1,28,E-09|2,24,E-08|5,32,E-09|
|AREA|SRC_262|Cam_Valpo_179-PEAS e Imp|269514|6393952|3 meses|327,49|3,87,E-09|9,37,E-10|1,69,E-09|2,96,E-08|7,04,E-09|
|AREA|SRC_263|Cam_Valpo_180-PEAS e Imp|269461|6394006|3 meses|302,03|4,20,E-09|1,02,E-09|1,84,E-09|3,21,E-08|7,64,E-09|
|AREA|SRC_264|Cam_Valpo_181-PEAS e Imp|269456|6394087|3 meses|317,54|3,99,E-09|9,66,E-10|1,75,E-09|3,06,E-08|7,26,E-09|
|AREA|SRC_265|Cam_Valpo_182-PEAS e Imp|269494|6394169|3 meses|358,94|3,53,E-09|8,55,E-10|1,55,E-09|2,70,E-08|6,43,E-09|
|AREA|SRC_266|Cam_Valpo_183-PEAS e Imp|269580|6394296|3 meses|611,99|2,07,E-09|5,01,E-10|9,07,E-10|1,59,E-08|3,77,E-09|
|AREA|SRC_267|Cam_Valpo_184-PEAS e Imp|269614|6394394|3 meses|416,61|3,04,E-09|7,36,E-10|1,33,E-09|2,33,E-08|5,54,E-09|
|AREA|SRC_268|Cam_Valpo_185-PEAS e Imp|269617|6394492|3 meses|396,57|3,20,E-09|7,73,E-10|1,40,E-09|2,45,E-08|5,82,E-09|
|AREA|SRC_269|Cam_Valpo_186-PEAS e Imp|269532|6394634|3 meses|664,18|1,91,E-09|4,62,E-10|8,36,E-10|1,46,E-08|3,47,E-09|
|AREA|SRC_270|Cam_Valpo_187-PEAS e Imp|269478|6394752|3 meses|518,20|2,45,E-09|5,92,E-10|1,07,E-09|1,87,E-08|4,45,E-09|
|AREA|SRC_271|Cam_Valpo_188-PEAS e Imp|269437|6394881|3 meses|540,93|2,34,E-09|5,67,E-10|1,03,E-09|1,79,E-08|4,26,E-09|
|AREA|SRC_272|Cam_Valpo_189-PEAS e Imp|269448|6395002|3 meses|483,46|2,62,E-09|6,34,E-10|1,15,E-09|2,01,E-08|4,77,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 226 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>269465|[m]<br>6395049|[m]<br>6395049|[m2]<br>197,82|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_273|Cam_Valpo_190-PEAS e Imp|Cam_Valpo_190-PEAS e Imp|Cam_Valpo_190-PEAS e Imp|3 meses|3 meses|6,41,E-09|1,55,E-09|2,81,E-09|4,91,E-08|1,17,E-08|
|AREA|SRC_274|Cam_Valpo_191-PEAS e Imp|269701|6395188|3 meses|1088,66|1,16,E-09|2,82,E-10|5,10,E-10|8,92,E-09|2,12,E-09|
|AREA|SRC_275|Cam_Valpo_192-PEAS e Imp|269737|6395244|3 meses|269,38|4,71,E-09|1,14,E-09|2,06,E-09|3,60,E-08|8,56,E-09|
|AREA|SRC_276|Cam_Valpo_193-PEAS e Imp|269748|6395318|3 meses|301,88|4,20,E-09|1,02,E-09|1,84,E-09|3,22,E-08|7,64,E-09|
|AREA|SRC_277|Cam_Valpo_194-PEAS e Imp|269734|6395473|3 meses|624,02|2,03,E-09|4,92,E-10|8,89,E-10|1,56,E-08|3,70,E-09|
|AREA|SRC_278|Cam_Valpo_195-PEAS e Imp|269791|6395575|3 meses|462,91|2,74,E-09|6,63,E-10|1,20,E-09|2,10,E-08|4,98,E-09|
|AREA|SRC_279|Cam_Valpo_196-PEAS e Imp|269918|6395634|3 meses|557,57|2,27,E-09|5,50,E-10|9,95,E-10|1,74,E-08|4,14,E-09|
|AREA|SRC_280|Cam_Valpo_197-PEAS e Imp|269951|6395703|3 meses|311,66|4,07,E-09|9,84,E-10|1,78,E-09|3,12,E-08|7,40,E-09|
|AREA|SRC_281|Cam_Valpo_198-PEAS e Imp|269926|6395767|3 meses|277,87|4,56,E-09|1,10,E-09|2,00,E-09|3,49,E-08|8,30,E-09|
|AREA|SRC_282|Cam_Valpo_199-PEAS e Imp|269853|6395812|3 meses|348,28|3,64,E-09|8,81,E-10|1,59,E-09|2,79,E-08|6,62,E-09|
|AREA|SRC_283|Cam_Valpo_200-PEAS e Imp|269732|6395847|3 meses|504,67|2,51,E-09|6,08,E-10|1,10,E-09|1,92,E-08|4,57,E-09|
|AREA|SRC_284|Cam_Valpo_201-PEAS e Imp|269688|6395928|3 meses|365,46|3,47,E-09|8,39,E-10|1,52,E-09|2,66,E-08|6,31,E-09|
|AREA|SRC_285|Cam_Valpo_202-PEAS e Imp|269717|6396047|3 meses|484,68|2,62,E-09|6,33,E-10|1,14,E-09|2,00,E-08|4,76,E-09|
|AREA|SRC_286|Cam_Valpo_203-PEAS e Imp|269712|6396106|3 meses|237,49|5,34,E-09|1,29,E-09|2,34,E-09|4,09,E-08|9,71,E-09|
|AREA|SRC_287|Cam_Valpo_204-PEAS e Imp|269657|6396143|3 meses|271,48|4,67,E-09|1,13,E-09|2,04,E-09|3,58,E-08|8,50,E-09|
|AREA|SRC_288|Cam_Valpo_205-PEAS e Imp|269580|6396120|3 meses|326,46|3,88,E-09|9,40,E-10|1,70,E-09|2,97,E-08|7,07,E-09|
|AREA|SRC_289|Cam_Valpo_206-PEAS e Imp|269501|6396070|3 meses|376,20|3,37,E-09|8,15,E-10|1,48,E-09|2,58,E-08|6,13,E-09|
|AREA|SRC_290|Cam_Valpo_207-PEAS e Imp|269359|6396026|3 meses|593,54|2,14,E-09|5,17,E-10|9,35,E-10|1,64,E-08|3,89,E-09|
|AREA|SRC_291|Cam_Valpo_208-PEAS e Imp|269272|6396023|3 meses|343,48|3,69,E-09|8,93,E-10|1,62,E-09|2,83,E-08|6,72,E-09|
|AREA|SRC_292|Cam_Valpo_209-PEAS e Imp|269222|6396073|3 meses|275,81|4,60,E-09|1,11,E-09|2,01,E-09|3,52,E-08|8,36,E-09|
|AREA|SRC_293|Cam_Valpo_210-PEAS e Imp|269210|6396185|3 meses|446,25|2,84,E-09|6,87,E-10|1,24,E-09|2,18,E-08|5,17,E-09|
|AREA|SRC_294|Cam_Valpo_211-PEAS e Imp|269167|6396232|3 meses|255,46|4,96,E-09|1,20,E-09|2,17,E-09|3,80,E-08|9,03,E-09|
|AREA|SRC_295|Cam_Valpo_212-PEAS e Imp|269082|6396226|3 meses|349,58|3,63,E-09|8,77,E-10|1,59,E-09|2,78,E-08|6,60,E-09|
|AREA|SRC_296|Cam_Valpo_213-PEAS e Imp|268998|6396240|3 meses|335,54|3,78,E-09|9,14,E-10|1,65,E-09|2,89,E-08|6,87,E-09|
|AREA|SRC_297|Cam_Valpo_214-PEAS e Imp|268894|6396300|3 meses|480,09|2,64,E-09|6,39,E-10|1,16,E-09|2,02,E-08|4,80,E-09|
|AREA|SRC_298|Cam_Valpo_215-PEAS e Imp|268805|6396381|3 meses|477,49|2,66,E-09|6,42,E-10|1,16,E-09|2,03,E-08|4,83,E-09|
|AREA|SRC_299|Cam_Valpo_216-PEAS e Imp|268734|6396481|3 meses|489,34|2,59,E-09|6,27,E-10|1,13,E-09|1,98,E-08|4,71,E-09|
|AREA|SRC_300|Cam_Valpo_217-PEAS e Imp|268692|6396569|3 meses|388,32|3,26,E-09|7,90,E-10|1,43,E-09|2,50,E-08|5,94,E-09|
|AREA|SRC_301|Cam_Valpo_218-PEAS e Imp|268614|6396686|3 meses|563,68|2,25,E-09|5,44,E-10|9,84,E-10|1,72,E-08|4,09,E-09|
|AREA|SRC_302|Cam_Valpo_219-PEAS e Imp|268551|6396751|3 meses|365,13|3,47,E-09|8,40,E-10|1,52,E-09|2,66,E-08|6,32,E-09|
|AREA|SRC_303|Cam_Valpo_220-PEAS e Imp|268525|6396834|3 meses|342,75|3,70,E-09|8,95,E-10|1,62,E-09|2,83,E-08|6,73,E-09|
|AREA|SRC_304|Cam_Valpo_221-PEAS e Imp|268521|6396918|3 meses|335,20|3,78,E-09|9,15,E-10|1,66,E-09|2,90,E-08|6,88,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 227 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>268510|[m]<br>6396996|[m]<br>6396996|[m2]<br>312,17|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_305|Cam_Valpo_222-PEAS e Imp|Cam_Valpo_222-PEAS e Imp|Cam_Valpo_222-PEAS e Imp|3 meses|3 meses|4,06,E-09|9,83,E-10|1,78,E-09|3,11,E-08|7,39,E-09|
|AREA|SRC_306|Cam_Valpo_223-PEAS e Imp|268441|6397095|3 meses|486,78|2,60,E-09|6,30,E-10|1,14,E-09|1,99,E-08|4,74,E-09|
|AREA|SRC_307|Cam_Valpo_224-PEAS e Imp|268352|6397195|3 meses|537,81|2,36,E-09|5,70,E-10|1,03,E-09|1,81,E-08|4,29,E-09|
|AREA|SRC_308|Cam_Valpo_225-PEAS e Imp|268295|6397296|3 meses|460,41|2,75,E-09|6,66,E-10|1,21,E-09|2,11,E-08|5,01,E-09|
|AREA|SRC_309|Cam_Valpo_226-PEAS e Imp|268265|6397370|3 meses|319,00|3,97,E-09|9,62,E-10|1,74,E-09|3,04,E-08|7,23,E-09|
|AREA|SRC_310|Cam_Valpo_227-PEAS e Imp|268236|6397470|3 meses|414,51|3,06,E-09|7,40,E-10|1,34,E-09|2,34,E-08|5,56,E-09|
|AREA|SRC_311|Cam_Valpo_228-PEAS e Imp|268225|6397539|3 meses|278,02|4,56,E-09|1,10,E-09|2,00,E-09|3,49,E-08|8,30,E-09|
|AREA|SRC_312|Cam_Valpo_229-PEAS e Imp|268212|6397650|3 meses|446,47|2,84,E-09|6,87,E-10|1,24,E-09|2,17,E-08|5,17,E-09|
|AREA|SRC_313|Cam_Valpo_230-PEAS e Imp|268292|6397691|3 meses|352,90|3,59,E-09|8,69,E-10|1,57,E-09|2,75,E-08|6,54,E-09|
|AREA|SRC_314|Cam_Valpo_231-PEAS e Imp|268324|6397741|3 meses|244,09|5,19,E-09|1,26,E-09|2,27,E-09|3,98,E-08|9,45,E-09|
|AREA|SRC_315|Cam_Valpo_232-PEAS e Imp|268344|6397809|3 meses|284,52|4,46,E-09|1,08,E-09|1,95,E-09|3,41,E-08|8,11,E-09|
|AREA|SRC_316|Cam_Valpo_233-PEAS e Imp|268317|6397871|3 meses|277,40|4,57,E-09|1,11,E-09|2,00,E-09|3,50,E-08|8,31,E-09|
|AREA|SRC_317|Cam_Valpo_234-PEAS e Imp|268289|6397931|3 meses|263,44|4,81,E-09|1,16,E-09|2,11,E-09|3,69,E-08|8,76,E-09|
|AREA|SRC_318|Cam_Valpo_235-PEAS e Imp|268281|6397993|3 meses|246,21|5,15,E-09|1,25,E-09|2,25,E-09|3,94,E-08|9,37,E-09|
|AREA|SRC_319|Cam_Valpo_236-PEAS e Imp|268325|6398057|3 meses|307,11|4,13,E-09|9,99,E-10|1,81,E-09|3,16,E-08|7,51,E-09|
|AREA|SRC_320|Cam_Valpo_237-PEAS e Imp|268339|6398092|3 meses|154,12|8,23,E-09|1,99,E-09|3,60,E-09|6,30,E-08|1,50,E-08|
|AREA|SRC_321|Cam_Valpo_238-PEAS e Imp|268362|6398151|3 meses|251,56|5,04,E-09|1,22,E-09|2,21,E-09|3,86,E-08|9,17,E-09|
|AREA|SRC_322|Cam_Valpo_239-PEAS e Imp|268383|6398192|3 meses|185,19|6,85,E-09|1,66,E-09|3,00,E-09|5,24,E-08|1,25,E-08|
|AREA|SRC_323|Cam_Valpo_240-PEAS e Imp|268355|6398247|3 meses|250,18|5,07,E-09|1,23,E-09|2,22,E-09|3,88,E-08|9,22,E-09|
|AREA|SRC_324|Cam_Valpo_241-PEAS e Imp|268227|6398303|3 meses|566,84|2,24,E-09|5,41,E-10|9,79,E-10|1,71,E-08|4,07,E-09|
|AREA|SRC_325|Cam_Valpo_242-PEAS e Imp|268140|6398362|3 meses|418,83|3,03,E-09|7,32,E-10|1,32,E-09|2,32,E-08|5,51,E-09|
|AREA|SRC_326|Cam_Valpo_243-PEAS e Imp|268089|6398427|3 meses|325,43|3,90,E-09|9,43,E-10|1,71,E-09|2,98,E-08|7,09,E-09|
|AREA|SRC_327|Cam_Valpo_244-PEAS e Imp|268005|6398483|3 meses|406,15|3,12,E-09|7,55,E-10|1,37,E-09|2,39,E-08|5,68,E-09|
|AREA|SRC_328|Cam_Valpo_245-PEAS e Imp|267956|6398553|3 meses|338,26|3,75,E-09|9,07,E-10|1,64,E-09|2,87,E-08|6,82,E-09|
|AREA|SRC_329|Cam_Valpo_246-PEAS e Imp|267920|6398673|3 meses|498,96|2,54,E-09|6,15,E-10|1,11,E-09|1,95,E-08|4,62,E-09|
|AREA|SRC_330|Cam_Valpo_247-PEAS e Imp|267908|6398749|3 meses|308,37|4,11,E-09|9,95,E-10|1,80,E-09|3,15,E-08|7,48,E-09|
|AREA|SRC_331|Cam_Valpo_248-PEAS e Imp|267894|6398771|3 meses|107,41|1,18,E-08|2,86,E-09|5,17,E-09|9,04,E-08|2,15,E-08|
|AREA|SRC_332|Cam_Valpo_249-PEAS e Imp|267791|6398823|3 meses|466,56|2,72,E-09|6,57,E-10|1,19,E-09|2,08,E-08|4,94,E-09|
|AREA|SRC_333|Cam_Valpo_250-PEAS e Imp|267747|6398849|3 meses|204,00|6,21,E-09|1,50,E-09|2,72,E-09|4,76,E-08|1,13,E-08|
|AREA|SRC_334|Cam_Valpo_251-PEAS e Imp|267699|6398875|3 meses|217,15|5,84,E-09|1,41,E-09|2,56,E-09|4,47,E-08|1,06,E-08|
|AREA|SRC_335|Cam_Valpo_252-PEAS e Imp|267673|6398943|3 meses|285,91|4,43,E-09|1,07,E-09|1,94,E-09|3,40,E-08|8,07,E-09|
|AREA|SRC_336|Cam_Valpo_253-PEAS e Imp|267740|6399152|3 meses|871,99|1,45,E-09|3,52,E-10|6,36,E-10|1,11,E-08|2,65,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 228 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>267754|[m]<br>6399259|[m]<br>6399259|[m2]<br>434,37|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_337|Cam_Valpo_254-PEAS e Imp|Cam_Valpo_254-PEAS e Imp|Cam_Valpo_254-PEAS e Imp|3 meses|3 meses|2,92,E-09|7,06,E-10|1,28,E-09|2,24,E-08|5,31,E-09|
|AREA|SRC_338|Cam_Valpo_255-PEAS e Imp|267756|6399372|3 meses|452,93|2,80,E-09|6,77,E-10|1,23,E-09|2,14,E-08|5,09,E-09|
|AREA|SRC_339|Cam_Valpo_256-PEAS e Imp|267702|6399478|3 meses|480,03|2,64,E-09|6,39,E-10|1,16,E-09|2,02,E-08|4,80,E-09|
|AREA|SRC_340|Cam_Valpo_257-PEAS e Imp|267740|6399547|3 meses|307,21|4,13,E-09|9,98,E-10|1,81,E-09|3,16,E-08|7,51,E-09|
|AREA|SRC_341|Cam_Valpo_258-PEAS e Imp|267742|6399624|3 meses|311,56|4,07,E-09|9,85,E-10|1,78,E-09|3,12,E-08|7,40,E-09|
|AREA|SRC_342|Cam_Valpo_259-PEAS e Imp|267731|6399695|3 meses|287,58|4,41,E-09|1,07,E-09|1,93,E-09|3,38,E-08|8,02,E-09|
|AREA|SRC_343|Cam_Valpo_260-PEAS e Imp|267682|6399788|3 meses|425,70|2,98,E-09|7,21,E-10|1,30,E-09|2,28,E-08|5,42,E-09|
|AREA|SRC_344|Cam_Valpo_261-PEAS e Imp|267661|6399830|3 meses|187,04|6,78,E-09|1,64,E-09|2,97,E-09|5,19,E-08|1,23,E-08|
|AREA|SRC_345|PTAS|273586|6383219|7 meses|4,00|2,79,E-03|1,39,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_348|Cam_Cat_1-PTAS|273043|6387323|7 meses|383,32|4,55,E-10|4,55,E-10|4,55,E-10|4,55,E-10|4,55,E-10|
|AREA|SRC_349|Cam_Cat_2-PTAS|273206|6387558|7 meses|1145,03|1,52,E-10|1,52,E-10|1,52,E-10|1,52,E-10|1,52,E-10|
|AREA|SRC_350|Cam_Cat_3-PTAS|273308|6387612|7 meses|456,00|3,82,E-10|3,82,E-10|3,82,E-10|3,82,E-10|3,82,E-10|
|AREA|SRC_351|Cam_Cat_4-PTAS|273511|6387668|7 meses|843,57|2,07,E-10|2,07,E-10|2,07,E-10|2,07,E-10|2,07,E-10|
|AREA|SRC_352|Cam_Cat_5-PTAS|273721|6387707|7 meses|853,32|2,04,E-10|2,04,E-10|2,04,E-10|2,04,E-10|2,04,E-10|
|AREA|SRC_353|Cam_Cat_6-PTAS|273880|6387880|7 meses|945,26|1,84,E-10|1,84,E-10|1,84,E-10|1,84,E-10|1,84,E-10|
|AREA|SRC_354|Cam_Cat_7-PTAS|273982|6387934|7 meses|457,52|3,81,E-10|3,81,E-10|3,81,E-10|3,81,E-10|3,81,E-10|
|AREA|SRC_355|Cam_Cat_8-PTAS|274178|6387916|7 meses|782,20|2,23,E-10|2,23,E-10|2,23,E-10|2,23,E-10|2,23,E-10|
|AREA|SRC_356|Cam_Cat_9-PTAS|274216|6387945|7 meses|195,48|8,91,E-10|8,91,E-10|8,91,E-10|8,91,E-10|8,91,E-10|
|AREA|SRC_357|Cam_Cat_10-PTAS|274213|6388017|7 meses|295,61|5,89,E-10|5,89,E-10|5,89,E-10|5,89,E-10|5,89,E-10|
|AREA|SRC_358|Cam_Cat_11-PTAS|274177|6388250|7 meses|941,53|1,85,E-10|1,85,E-10|1,85,E-10|1,85,E-10|1,85,E-10|
|AREA|SRC_359|Cam_Cat_12-PTAS|274185|6388365|7 meses|458,34|3,80,E-10|3,80,E-10|3,80,E-10|3,80,E-10|3,80,E-10|
|AREA|SRC_360|Cam_Cat_13-PTAS|274352|6388558|7 meses|1016,92|1,71,E-10|1,71,E-10|1,71,E-10|1,71,E-10|1,71,E-10|
|AREA|SRC_361|Cam_Cat_14-PTAS|274654|6388846|7 meses|1667,00|1,05,E-10|1,05,E-10|1,05,E-10|1,05,E-10|1,05,E-10|
|AREA|SRC_362|Cam_Cat_15-PTAS|274745|6388895|7 meses|409,81|4,25,E-10|4,25,E-10|4,25,E-10|4,25,E-10|4,25,E-10|
|AREA|SRC_363|Cam_Cat_16-PTAS|274834|6388862|7 meses|371,12|4,70,E-10|4,70,E-10|4,70,E-10|4,70,E-10|4,70,E-10|
|AREA|SRC_364|Cam_Cat_17-PTAS|274882|6388794|7 meses|331,29|5,26,E-10|5,26,E-10|5,26,E-10|5,26,E-10|5,26,E-10|
|AREA|SRC_365|Cam_Cat_18-PTAS|274979|6388768|7 meses|406,63|4,29,E-10|4,29,E-10|4,29,E-10|4,29,E-10|4,29,E-10|
|AREA|SRC_366|Cam_Cat_19-PTAS|275069|6388799|7 meses|384,16|4,54,E-10|4,54,E-10|4,54,E-10|4,54,E-10|4,54,E-10|
|AREA|SRC_367|Cam_Cat_20-PTAS|275059|6388911|7 meses|459,52|3,79,E-10|3,79,E-10|3,79,E-10|3,79,E-10|3,79,E-10|
|AREA|SRC_368|Cam_Cat_21-PTAS|275040|6389003|7 meses|374,05|4,66,E-10|4,66,E-10|4,66,E-10|4,66,E-10|4,66,E-10|
|AREA|SRC_369|Cam_Cat_22-PTAS|274958|6389092|7 meses|489,11|3,56,E-10|3,56,E-10|3,56,E-10|3,56,E-10|3,56,E-10|
|AREA|SRC_370|Cam_Cat_23-PTAS|274915|6389184|7 meses|402,20|4,33,E-10|4,33,E-10|4,33,E-10|4,33,E-10|4,33,E-10|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 229 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>274946|[m]<br>6389307|[m]<br>6389307|[m2]<br>502,79|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_371|Cam_Cat_24-PTAS|Cam_Cat_24-PTAS|Cam_Cat_24-PTAS|7 meses|7 meses|3,47,E-10|3,47,E-10|3,47,E-10|3,47,E-10|3,47,E-10|
|AREA|SRC_372|Cam_Cat_25-PTAS|275049|6389374|7 meses|485,06|3,59,E-10|3,59,E-10|3,59,E-10|3,59,E-10|3,59,E-10|
|AREA|SRC_373|Cam_Cat_26-PTAS|275181|6389406|7 meses|541,36|3,22,E-10|3,22,E-10|3,22,E-10|3,22,E-10|3,22,E-10|
|AREA|SRC_374|Cam_Cat_27-PTAS|275286|6389385|7 meses|424,34|4,11,E-10|4,11,E-10|4,11,E-10|4,11,E-10|4,11,E-10|
|AREA|SRC_375|Cam_Cat_28-PTAS|275372|6389387|7 meses|345,06|5,05,E-10|5,05,E-10|5,05,E-10|5,05,E-10|5,05,E-10|
|AREA|SRC_376|Cam_Cat_29-PTAS|275519|6389442|7 meses|633,26|2,75,E-10|2,75,E-10|2,75,E-10|2,75,E-10|2,75,E-10|
|AREA|SRC_377|Cam_Cat_30-PTAS|275575|6389512|7 meses|360,36|4,84,E-10|4,84,E-10|4,84,E-10|4,84,E-10|4,84,E-10|
|AREA|SRC_378|Cam_Cat_31-PTAS|275579|6389623|7 meses|447,31|3,90,E-10|3,90,E-10|3,90,E-10|3,90,E-10|3,90,E-10|
|AREA|SRC_379|Cam_Cat_32-PTAS|275473|6389738|7 meses|629,59|2,77,E-10|2,77,E-10|2,77,E-10|2,77,E-10|2,77,E-10|
|AREA|SRC_380|Cam_Cat_33-PTAS|275397|6389809|7 meses|419,18|4,16,E-10|4,16,E-10|4,16,E-10|4,16,E-10|4,16,E-10|
|AREA|SRC_381|Cam_Cat_34-PTAS|275382|6389918|7 meses|432,78|4,03,E-10|4,03,E-10|4,03,E-10|4,03,E-10|4,03,E-10|
|AREA|SRC_382|Cam_Cat_35-PTAS|275487|6390018|7 meses|576,65|3,02,E-10|3,02,E-10|3,02,E-10|3,02,E-10|3,02,E-10|
|AREA|SRC_383|Cam_Cat_36-PTAS|275630|6390045|7 meses|576,34|3,02,E-10|3,02,E-10|3,02,E-10|3,02,E-10|3,02,E-10|
|AREA|SRC_384|Cam_Cat_37-PTAS|275763|6390025|7 meses|532,94|3,27,E-10|3,27,E-10|3,27,E-10|3,27,E-10|3,27,E-10|
|AREA|SRC_385|Cam_Cat_38-PTAS|275861|6389993|7 meses|411,71|4,23,E-10|4,23,E-10|4,23,E-10|4,23,E-10|4,23,E-10|
|AREA|SRC_386|Cam_Cat_39-PTAS|276044|6389963|7 meses|742,87|2,35,E-10|2,35,E-10|2,35,E-10|2,35,E-10|2,35,E-10|
|AREA|SRC_387|Cam_Cat_40-PTAS|276114|6389925|7 meses|316,96|5,50,E-10|5,50,E-10|5,50,E-10|5,50,E-10|5,50,E-10|
|AREA|SRC_388|Cam_Cat_41-PTAS|276133|6389885|7 meses|172,93|1,01,E-09|1,01,E-09|1,01,E-09|1,01,E-09|1,01,E-09|
|AREA|SRC_389|Cam_Cat_42-PTAS|276158|6389818|7 meses|286,84|6,07,E-10|6,07,E-10|6,07,E-10|6,07,E-10|6,07,E-10|
|AREA|SRC_390|Cam_Cat_43-PTAS|276157|6389659|7 meses|632,84|2,75,E-10|2,75,E-10|2,75,E-10|2,75,E-10|2,75,E-10|
|AREA|SRC_391|Cam_Cat_44-PTAS|276172|6389529|7 meses|521,10|3,34,E-10|3,34,E-10|3,34,E-10|3,34,E-10|3,34,E-10|
|AREA|SRC_392|Cam_Cat_45-PTAS|276275|6389477|7 meses|468,32|3,72,E-10|3,72,E-10|3,72,E-10|3,72,E-10|3,72,E-10|
|AREA|SRC_393|Cam_Cat_46-PTAS|276411|6389458|7 meses|553,37|3,15,E-10|3,15,E-10|3,15,E-10|3,15,E-10|3,15,E-10|
|AREA|SRC_394|Cam_Cat_47-PTAS|276501|6389471|7 meses|366,24|4,76,E-10|4,76,E-10|4,76,E-10|4,76,E-10|4,76,E-10|
|AREA|SRC_395|Cam_Cat_48-PTAS|276706|6389673|7 meses|1151,46|1,51,E-10|1,51,E-10|1,51,E-10|1,51,E-10|1,51,E-10|
|AREA|SRC_396|Cam_Cat_49-PTAS|277353|6390498|7 meses|4195,41|4,15,E-11|4,15,E-11|4,15,E-11|4,15,E-11|4,15,E-11|
|AREA|SRC_397|Cam_Cat_50-PTAS|277494|6390575|7 meses|640,03|2,72,E-10|2,72,E-10|2,72,E-10|2,72,E-10|2,72,E-10|
|AREA|SRC_398|Cam_Cat_51-PTAS|279440|6391244|7 meses|8223,68|2,12,E-11|2,12,E-11|2,12,E-11|2,12,E-11|2,12,E-11|
|AREA|SRC_399|Cam_Cat_52-PTAS|283346|6393239|7 meses|17540,88|9,93,E-12|9,93,E-12|9,93,E-12|9,93,E-12|9,93,E-12|
|AREA|SRC_400|Cam_Cat_53-PTAS|287745|6394661|7 meses|18483,13|9,43,E-12|9,43,E-12|9,43,E-12|9,43,E-12|9,43,E-12|
|AREA|SRC_401|Cam_Pta_1-PTAS|273147|6383634|7 meses|1866,42|9,34,E-11|9,34,E-11|9,34,E-11|9,34,E-11|9,34,E-11|
|AREA|SRC_402|Cam_Pta_2-PTAS|273165|6383642|7 meses|80,85|2,16,E-09|2,16,E-09|2,16,E-09|2,16,E-09|2,16,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 230 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>273189|[m]<br>6383637|[m]<br>6383637|[m2]<br>94,14|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_403|Cam_Pta_3-PTAS|Cam_Pta_3-PTAS|Cam_Pta_3-PTAS|7 meses|7 meses|1,85,E-09|1,85,E-09|1,85,E-09|1,85,E-09|1,85,E-09|
|AREA|SRC_404|Cam_Pta_4-PTAS|273241|6383562|7 meses|359,95|4,84,E-10|4,84,E-10|4,84,E-10|4,84,E-10|4,84,E-10|
|AREA|SRC_405|Cam_Pta_5-PTAS|273289|6383445|7 meses|505,57|3,45,E-10|3,45,E-10|3,45,E-10|3,45,E-10|3,45,E-10|
|AREA|SRC_406|Cam_Pta_6-PTAS|273304|6383402|7 meses|179,62|9,70,E-10|9,70,E-10|9,70,E-10|9,70,E-10|9,70,E-10|
|AREA|SRC_407|Cam_Pta_7-PTAS|273331|6383382|7 meses|138,45|1,26,E-09|1,26,E-09|1,26,E-09|1,26,E-09|1,26,E-09|
|AREA|SRC_408|Cam_Pta_8-PTAS|273361|6383362|7 meses|145,56|1,20,E-09|1,20,E-09|1,20,E-09|1,20,E-09|1,20,E-09|
|AREA|SRC_409|Cam_Pta_9-PTAS|273393|6383346|7 meses|143,99|1,21,E-09|1,21,E-09|1,21,E-09|1,21,E-09|1,21,E-09|
|AREA|SRC_410|Cam_Pta_10-PTAS|273413|6383324|7 meses|116,32|1,50,E-09|1,50,E-09|1,50,E-09|1,50,E-09|1,50,E-09|
|AREA|SRC_411|Cam_Pta_11-PTAS|273447|6383229|7 meses|400,03|4,36,E-10|4,36,E-10|4,36,E-10|4,36,E-10|4,36,E-10|
|AREA|SRC_412|Cam_Pta_12-PTAS|273463|6383220|7 meses|80,13|2,17,E-09|2,17,E-09|2,17,E-09|2,17,E-09|2,17,E-09|
|AREA|SRC_413|Cam_Pta_13-PTAS|273473|6383218|7 meses|45,12|3,86,E-09|3,86,E-09|3,86,E-09|3,86,E-09|3,86,E-09|
|AREA|SRC_414|Cam_Pta_14-PTAS|273519|6383228|7 meses|188,53|9,24,E-10|9,24,E-10|9,24,E-10|9,24,E-10|9,24,E-10|
|AREA|SRC_415|Cam_Valpo_1-PTAS|267407|6370003|7 meses|9181,86|1,90,E-11|1,90,E-11|1,90,E-11|1,90,E-11|1,90,E-11|
|AREA|SRC_416|Cam_Valpo_2-PTAS|267402|6370088|7 meses|338,29|5,15,E-10|5,15,E-10|5,15,E-10|5,15,E-10|5,15,E-10|
|AREA|SRC_417|Cam_Valpo_3-PTAS|267699|6371506|7 meses|5788,94|3,01,E-11|3,01,E-11|3,01,E-11|3,01,E-11|3,01,E-11|
|AREA|SRC_418|Cam_Valpo_4-PTAS|267700|6371619|7 meses|452,00|3,86,E-10|3,86,E-10|3,86,E-10|3,86,E-10|3,86,E-10|
|AREA|SRC_419|Cam_Valpo_5-PTAS|267517|6371917|7 meses|1401,44|1,24,E-10|1,24,E-10|1,24,E-10|1,24,E-10|1,24,E-10|
|AREA|SRC_420|Cam_Valpo_6-PTAS|267499|6371980|7 meses|261,10|6,67,E-10|6,67,E-10|6,67,E-10|6,67,E-10|6,67,E-10|
|AREA|SRC_421|Cam_Valpo_7-PTAS|267496|6372042|7 meses|247,03|7,05,E-10|7,05,E-10|7,05,E-10|7,05,E-10|7,05,E-10|
|AREA|SRC_422|Cam_Valpo_8-PTAS|267518|6372113|7 meses|294,47|5,92,E-10|5,92,E-10|5,92,E-10|5,92,E-10|5,92,E-10|
|AREA|SRC_423|Cam_Valpo_9-PTAS|267547|6372151|7 meses|187,43|9,30,E-10|9,30,E-10|9,30,E-10|9,30,E-10|9,30,E-10|
|AREA|SRC_424|Cam_Valpo_10-PTAS|267569|6372177|7 meses|137,02|1,27,E-09|1,27,E-09|1,27,E-09|1,27,E-09|1,27,E-09|
|AREA|SRC_425|Cam_Valpo_11-PTAS|267738|6372319|7 meses|879,83|1,98,E-10|1,98,E-10|1,98,E-10|1,98,E-10|1,98,E-10|
|AREA|SRC_426|Cam_Valpo_12-PTAS|267762|6372358|7 meses|186,57|9,34,E-10|9,34,E-10|9,34,E-10|9,34,E-10|9,34,E-10|
|AREA|SRC_427|Cam_Valpo_13-PTAS|267783|6372410|7 meses|224,51|7,76,E-10|7,76,E-10|7,76,E-10|7,76,E-10|7,76,E-10|
|AREA|SRC_428|Cam_Valpo_14-PTAS|267855|6372669|7 meses|1075,61|1,62,E-10|1,62,E-10|1,62,E-10|1,62,E-10|1,62,E-10|
|AREA|SRC_429|Cam_Valpo_15-PTAS|267848|6372720|7 meses|207,78|8,39,E-10|8,39,E-10|8,39,E-10|8,39,E-10|8,39,E-10|
|AREA|SRC_430|Cam_Valpo_16-PTAS|267715|6373066|7 meses|1484,08|1,17,E-10|1,17,E-10|1,17,E-10|1,17,E-10|1,17,E-10|
|AREA|SRC_431|Cam_Valpo_17-PTAS|267705|6373122|7 meses|225,43|7,73,E-10|7,73,E-10|7,73,E-10|7,73,E-10|7,73,E-10|
|AREA|SRC_432|Cam_Valpo_18-PTAS|267701|6373182|7 meses|241,22|7,22,E-10|7,22,E-10|7,22,E-10|7,22,E-10|7,22,E-10|
|AREA|SRC_433|Cam_Valpo_19-PTAS|267704|6373237|7 meses|217,96|7,99,E-10|7,99,E-10|7,99,E-10|7,99,E-10|7,99,E-10|
|AREA|SRC_434|Cam_Valpo_20-PTAS|267713|6373309|7 meses|291,26|5,98,E-10|5,98,E-10|5,98,E-10|5,98,E-10|5,98,E-10|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 231 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>267741|[m]<br>6373522|[m]<br>6373522|[m2]<br>860,16|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_435|Cam_Valpo_21-PTAS|Cam_Valpo_21-PTAS|Cam_Valpo_21-PTAS|7 meses|7 meses|2,03,E-10|2,03,E-10|2,03,E-10|2,03,E-10|2,03,E-10|
|AREA|SRC_436|Cam_Valpo_22-PTAS|267757|6373574|7 meses|213,85|8,15,E-10|8,15,E-10|8,15,E-10|8,15,E-10|8,15,E-10|
|AREA|SRC_437|Cam_Valpo_23-PTAS|267777|6373617|7 meses|187,32|9,30,E-10|9,30,E-10|9,30,E-10|9,30,E-10|9,30,E-10|
|AREA|SRC_438|Cam_Valpo_24-PTAS|267817|6373719|7 meses|441,14|3,95,E-10|3,95,E-10|3,95,E-10|3,95,E-10|3,95,E-10|
|AREA|SRC_439|Cam_Valpo_25-PTAS|267843|6373782|7 meses|272,58|6,39,E-10|6,39,E-10|6,39,E-10|6,39,E-10|6,39,E-10|
|AREA|SRC_440|Cam_Valpo_26-PTAS|267877|6373831|7 meses|236,03|7,38,E-10|7,38,E-10|7,38,E-10|7,38,E-10|7,38,E-10|
|AREA|SRC_441|Cam_Valpo_27-PTAS|267910|6373883|7 meses|246,12|7,08,E-10|7,08,E-10|7,08,E-10|7,08,E-10|7,08,E-10|
|AREA|SRC_442|Cam_Valpo_28-PTAS|268105|6374174|7 meses|1399,53|1,25,E-10|1,25,E-10|1,25,E-10|1,25,E-10|1,25,E-10|
|AREA|SRC_443|Cam_Valpo_29-PTAS|268274|6374430|7 meses|1228,07|1,42,E-10|1,42,E-10|1,42,E-10|1,42,E-10|1,42,E-10|
|AREA|SRC_444|Cam_Valpo_30-PTAS|268317|6374478|7 meses|254,35|6,85,E-10|6,85,E-10|6,85,E-10|6,85,E-10|6,85,E-10|
|AREA|SRC_445|Cam_Valpo_31-PTAS|268347|6374502|7 meses|154,46|1,13,E-09|1,13,E-09|1,13,E-09|1,13,E-09|1,13,E-09|
|AREA|SRC_446|Cam_Valpo_32-PTAS|269602|6375295|7 meses|5935,56|2,94,E-11|2,94,E-11|2,94,E-11|2,94,E-11|2,94,E-11|
|AREA|SRC_447|Cam_Valpo_33-PTAS|270646|6375956|7 meses|4938,33|3,53,E-11|3,53,E-11|3,53,E-11|3,53,E-11|3,53,E-11|
|AREA|SRC_448|Cam_Valpo_34-PTAS|270700|6375970|7 meses|220,74|7,89,E-10|7,89,E-10|7,89,E-10|7,89,E-10|7,89,E-10|
|AREA|SRC_449|Cam_Valpo_35-PTAS|270759|6375972|7 meses|232,03|7,51,E-10|7,51,E-10|7,51,E-10|7,51,E-10|7,51,E-10|
|AREA|SRC_450|Cam_Valpo_36-PTAS|270817|6375960|7 meses|237,83|7,33,E-10|7,33,E-10|7,33,E-10|7,33,E-10|7,33,E-10|
|AREA|SRC_451|Cam_Valpo_37-PTAS|271210|6375788|7 meses|1710,95|1,02,E-10|1,02,E-10|1,02,E-10|1,02,E-10|1,02,E-10|
|AREA|SRC_452|Cam_Valpo_38-PTAS|271299|6375786|7 meses|362,06|4,81,E-10|4,81,E-10|4,81,E-10|4,81,E-10|4,81,E-10|
|AREA|SRC_453|Cam_Valpo_39-PTAS|271410|6375784|7 meses|444,09|3,92,E-10|3,92,E-10|3,92,E-10|3,92,E-10|3,92,E-10|
|AREA|SRC_454|Cam_Valpo_40-PTAS|271537|6375829|7 meses|539,94|3,23,E-10|3,23,E-10|3,23,E-10|3,23,E-10|3,23,E-10|
|AREA|SRC_455|Cam_Valpo_41-PTAS|271698|6375908|7 meses|717,64|2,43,E-10|2,43,E-10|2,43,E-10|2,43,E-10|2,43,E-10|
|AREA|SRC_456|Cam_Valpo_42-PTAS|271943|6376040|7 meses|1111,41|1,57,E-10|1,57,E-10|1,57,E-10|1,57,E-10|1,57,E-10|
|AREA|SRC_457|Cam_Valpo_43-PTAS|272216|6376245|7 meses|1365,82|1,28,E-10|1,28,E-10|1,28,E-10|1,28,E-10|1,28,E-10|
|AREA|SRC_458|Cam_Valpo_44-PTAS|272308|6376283|7 meses|396,81|4,39,E-10|4,39,E-10|4,39,E-10|4,39,E-10|4,39,E-10|
|AREA|SRC_459|Cam_Valpo_45-PTAS|272828|6376412|7 meses|2139,51|8,14,E-11|8,14,E-11|8,14,E-11|8,14,E-11|8,14,E-11|
|AREA|SRC_460|Cam_Valpo_46-PTAS|272961|6376463|7 meses|572,90|3,04,E-10|3,04,E-10|3,04,E-10|3,04,E-10|3,04,E-10|
|AREA|SRC_461|Cam_Valpo_47-PTAS|273101|6376548|7 meses|656,43|2,65,E-10|2,65,E-10|2,65,E-10|2,65,E-10|2,65,E-10|
|AREA|SRC_462|Cam_Valpo_48-PTAS|273683|6376890|7 meses|2699,98|6,45,E-11|6,45,E-11|6,45,E-11|6,45,E-11|6,45,E-11|
|AREA|SRC_463|Cam_Valpo_49-PTAS|273729|6376911|7 meses|198,66|8,77,E-10|8,77,E-10|8,77,E-10|8,77,E-10|8,77,E-10|
|AREA|SRC_464|Cam_Valpo_50-PTAS|273841|6376934|7 meses|455,50|3,83,E-10|3,83,E-10|3,83,E-10|3,83,E-10|3,83,E-10|
|AREA|SRC_465|Cam_Valpo_51-PTAS|273918|6376948|7 meses|314,84|5,53,E-10|5,53,E-10|5,53,E-10|5,53,E-10|5,53,E-10|
|AREA|SRC_466|Cam_Valpo_52-PTAS|273963|6376959|7 meses|182,29|9,56,E-10|9,56,E-10|9,56,E-10|9,56,E-10|9,56,E-10|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 232 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>274013|[m]<br>6376981|[m]<br>6376981|[m2]<br>220,22|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_467|Cam_Valpo_53-PTAS|Cam_Valpo_53-PTAS|Cam_Valpo_53-PTAS|7 meses|7 meses|7,91,E-10|7,91,E-10|7,91,E-10|7,91,E-10|7,91,E-10|
|AREA|SRC_468|Cam_Valpo_54-PTAS|274045|6377010|7 meses|175,74|9,92,E-10|9,92,E-10|9,92,E-10|9,92,E-10|9,92,E-10|
|AREA|SRC_469|Cam_Valpo_55-PTAS|274402|6377569|7 meses|2654,98|6,56,E-11|6,56,E-11|6,56,E-11|6,56,E-11|6,56,E-11|
|AREA|SRC_470|Cam_Valpo_56-PTAS|274508|6377712|7 meses|712,20|2,45,E-10|2,45,E-10|2,45,E-10|2,45,E-10|2,45,E-10|
|AREA|SRC_471|Cam_Valpo_57-PTAS|274515|6377737|7 meses|105,54|1,65,E-09|1,65,E-09|1,65,E-09|1,65,E-09|1,65,E-09|
|AREA|SRC_472|Cam_Valpo_58-PTAS|274530|6377783|7 meses|190,85|9,13,E-10|9,13,E-10|9,13,E-10|9,13,E-10|9,13,E-10|
|AREA|SRC_473|Cam_Valpo_59-PTAS|274571|6378190|7 meses|1640,54|1,06,E-10|1,06,E-10|1,06,E-10|1,06,E-10|1,06,E-10|
|AREA|SRC_474|Cam_Valpo_60-PTAS|274512|6378662|7 meses|1902,24|9,16,E-11|9,16,E-11|9,16,E-11|9,16,E-11|9,16,E-11|
|AREA|SRC_475|Cam_Valpo_61-PTAS|274484|6378742|7 meses|339,36|5,13,E-10|5,13,E-10|5,13,E-10|5,13,E-10|5,13,E-10|
|AREA|SRC_476|Cam_Valpo_62-PTAS|274397|6378959|7 meses|934,88|1,86,E-10|1,86,E-10|1,86,E-10|1,86,E-10|1,86,E-10|
|AREA|SRC_477|Cam_Valpo_63-PTAS|274391|6379006|7 meses|189,58|9,19,E-10|9,19,E-10|9,19,E-10|9,19,E-10|9,19,E-10|
|AREA|SRC_478|Cam_Valpo_64-PTAS|274392|6379034|7 meses|109,49|1,59,E-09|1,59,E-09|1,59,E-09|1,59,E-09|1,59,E-09|
|AREA|SRC_479|Cam_Valpo_65-PTAS|274513|6379469|7 meses|1805,57|9,65,E-11|9,65,E-11|9,65,E-11|9,65,E-11|9,65,E-11|
|AREA|SRC_480|Cam_Valpo_66-PTAS|274514|6379510|7 meses|163,36|1,07,E-09|1,07,E-09|1,07,E-09|1,07,E-09|1,07,E-09|
|AREA|SRC_481|Cam_Valpo_67-PTAS|274503|6379560|7 meses|208,73|8,35,E-10|8,35,E-10|8,35,E-10|8,35,E-10|8,35,E-10|
|AREA|SRC_482|Cam_Valpo_68-PTAS|274488|6379623|7 meses|255,44|6,82,E-10|6,82,E-10|6,82,E-10|6,82,E-10|6,82,E-10|
|AREA|SRC_483|Cam_Valpo_69-PTAS|274426|6379798|7 meses|745,56|2,34,E-10|2,34,E-10|2,34,E-10|2,34,E-10|2,34,E-10|
|AREA|SRC_484|Cam_Valpo_70-PTAS|274386|6379897|7 meses|428,53|4,07,E-10|4,07,E-10|4,07,E-10|4,07,E-10|4,07,E-10|
|AREA|SRC_485|Cam_Valpo_71-PTAS|274352|6379981|7 meses|360,23|4,84,E-10|4,84,E-10|4,84,E-10|4,84,E-10|4,84,E-10|
|AREA|SRC_486|Cam_Valpo_72-PTAS|274336|6380041|7 meses|249,49|6,98,E-10|6,98,E-10|6,98,E-10|6,98,E-10|6,98,E-10|
|AREA|SRC_487|Cam_Valpo_73-PTAS|274333|6380099|7 meses|227,80|7,65,E-10|7,65,E-10|7,65,E-10|7,65,E-10|7,65,E-10|
|AREA|SRC_488|Cam_Valpo_74-PTAS|274332|6380163|7 meses|257,27|6,77,E-10|6,77,E-10|6,77,E-10|6,77,E-10|6,77,E-10|
|AREA|SRC_489|Cam_Valpo_75-PTAS|274329|6380546|7 meses|1530,44|1,14,E-10|1,14,E-10|1,14,E-10|1,14,E-10|1,14,E-10|
|AREA|SRC_490|Cam_Valpo_76-PTAS|274323|6380578|7 meses|130,55|1,33,E-09|1,33,E-09|1,33,E-09|1,33,E-09|1,33,E-09|
|AREA|SRC_491|Cam_Valpo_77-PTAS|274308|6380608|7 meses|138,17|1,26,E-09|1,26,E-09|1,26,E-09|1,26,E-09|1,26,E-09|
|AREA|SRC_492|Cam_Valpo_78-PTAS|274078|6381086|7 meses|2120,50|8,22,E-11|8,22,E-11|8,22,E-11|8,22,E-11|8,22,E-11|
|AREA|SRC_493|Cam_Valpo_79-PTAS|274036|6381146|7 meses|292,96|5,95,E-10|5,95,E-10|5,95,E-10|5,95,E-10|5,95,E-10|
|AREA|SRC_494|Cam_Valpo_80-PTAS|273997|6381192|7 meses|242,71|7,18,E-10|7,18,E-10|7,18,E-10|7,18,E-10|7,18,E-10|
|AREA|SRC_495|Cam_Valpo_81-PTAS|273945|6381212|7 meses|225,25|7,74,E-10|7,74,E-10|7,74,E-10|7,74,E-10|7,74,E-10|
|AREA|SRC_496|Cam_Valpo_82-PTAS|273863|6381235|7 meses|340,59|5,12,E-10|5,12,E-10|5,12,E-10|5,12,E-10|5,12,E-10|
|AREA|SRC_497|Cam_Valpo_83-PTAS|273527|6381309|7 meses|1376,67|1,27,E-10|1,27,E-10|1,27,E-10|1,27,E-10|1,27,E-10|
|AREA|SRC_498|Cam_Valpo_84-PTAS|273488|6381317|7 meses|158,83|1,10,E-09|1,10,E-09|1,10,E-09|1,10,E-09|1,10,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 233 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>273437|[m]<br>6381311|[m]<br>6381311|[m2]<br>210,61|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_499|Cam_Valpo_85-PTAS|Cam_Valpo_85-PTAS|Cam_Valpo_85-PTAS|7 meses|7 meses|8,27,E-10|8,27,E-10|8,27,E-10|8,27,E-10|8,27,E-10|
|AREA|SRC_500|Cam_Valpo_86-PTAS|273400|6381306|7 meses|148,75|1,17,E-09|1,17,E-09|1,17,E-09|1,17,E-09|1,17,E-09|
|AREA|SRC_501|Cam_Valpo_87-PTAS|273330|6381278|7 meses|302,02|5,77,E-10|5,77,E-10|5,77,E-10|5,77,E-10|5,77,E-10|
|AREA|SRC_502|Cam_Valpo_88-PTAS|273269|6381275|7 meses|240,32|7,25,E-10|7,25,E-10|7,25,E-10|7,25,E-10|7,25,E-10|
|AREA|SRC_503|Cam_Valpo_89-PTAS|273210|6381284|7 meses|238,69|7,30,E-10|7,30,E-10|7,30,E-10|7,30,E-10|7,30,E-10|
|AREA|SRC_504|Cam_Valpo_90-PTAS|273140|6381307|7 meses|291,89|5,97,E-10|5,97,E-10|5,97,E-10|5,97,E-10|5,97,E-10|
|AREA|SRC_505|Cam_Valpo_91-PTAS|273026|6381364|7 meses|510,61|3,41,E-10|3,41,E-10|3,41,E-10|3,41,E-10|3,41,E-10|
|AREA|SRC_506|Cam_Valpo_92-PTAS|272787|6381471|7 meses|1046,47|1,67,E-10|1,67,E-10|1,67,E-10|1,67,E-10|1,67,E-10|
|AREA|SRC_507|Cam_Valpo_93-PTAS|272625|6381553|7 meses|726,81|2,40,E-10|2,40,E-10|2,40,E-10|2,40,E-10|2,40,E-10|
|AREA|SRC_508|Cam_Valpo_94-PTAS|272586|6381587|7 meses|205,87|8,46,E-10|8,46,E-10|8,46,E-10|8,46,E-10|8,46,E-10|
|AREA|SRC_509|Cam_Valpo_95-PTAS|272567|6381621|7 meses|150,25|1,16,E-09|1,16,E-09|1,16,E-09|1,16,E-09|1,16,E-09|
|AREA|SRC_510|Cam_Valpo_96-PTAS|272558|6381659|7 meses|154,59|1,13,E-09|1,13,E-09|1,13,E-09|1,13,E-09|1,13,E-09|
|AREA|SRC_511|Cam_Valpo_97-PTAS|272513|6381931|7 meses|1103,20|1,58,E-10|1,58,E-10|1,58,E-10|1,58,E-10|1,58,E-10|
|AREA|SRC_512|Cam_Valpo_98-PTAS|272500|6382030|7 meses|398,37|4,37,E-10|4,37,E-10|4,37,E-10|4,37,E-10|4,37,E-10|
|AREA|SRC_513|Cam_Valpo_99-PTAS|272492|6382086|7 meses|223,87|7,78,E-10|7,78,E-10|7,78,E-10|7,78,E-10|7,78,E-10|
|AREA|SRC_514|Cam_Valpo_100-PTAS|272491|6382127|7 meses|164,32|1,06,E-09|1,06,E-09|1,06,E-09|1,06,E-09|1,06,E-09|
|AREA|SRC_515|Cam_Valpo_101-PTAS|272506|6382188|7 meses|247,33|7,05,E-10|7,05,E-10|7,05,E-10|7,05,E-10|7,05,E-10|
|AREA|SRC_516|Cam_Valpo_102-PTAS|272660|6383439|7 meses|5043,31|3,46,E-11|3,46,E-11|3,46,E-11|3,46,E-11|3,46,E-11|
|AREA|SRC_517|Cam_Valpo_103-PTAS|272630|6384559|7 meses|4478,91|3,89,E-11|3,89,E-11|3,89,E-11|3,89,E-11|3,89,E-11|
|AREA|SRC_518|Cam_Valpo_104-PTAS|272626|6385227|7 meses|2671,08|6,52,E-11|6,52,E-11|6,52,E-11|6,52,E-11|6,52,E-11|
|AREA|SRC_519|Cam_Valpo_105-PTAS|272602|6386454|7 meses|4905,80|3,55,E-11|3,55,E-11|3,55,E-11|3,55,E-11|3,55,E-11|
|AREA|SRC_520|Cam_Valpo_106-PTAS|272609|6386527|7 meses|292,53|5,96,E-10|5,96,E-10|5,96,E-10|5,96,E-10|5,96,E-10|
|AREA|SRC_521|Cam_Valpo_107-PTAS|272650|6386615|7 meses|384,69|4,53,E-10|4,53,E-10|4,53,E-10|4,53,E-10|4,53,E-10|
|AREA|SRC_522|Cam_Valpo_108-PTAS|272755|6386705|7 meses|550,00|3,17,E-10|3,17,E-10|3,17,E-10|3,17,E-10|3,17,E-10|
|AREA|SRC_523|Cam_Valpo_109-PTAS|272846|6386776|7 meses|460,85|3,78,E-10|3,78,E-10|3,78,E-10|3,78,E-10|3,78,E-10|
|AREA|SRC_524|Cam_Valpo_110-PTAS|272918|6386821|7 meses|338,79|5,14,E-10|5,14,E-10|5,14,E-10|5,14,E-10|5,14,E-10|
|AREA|SRC_525|Cam_Valpo_111-PTAS|272959|6386856|7 meses|215,71|8,08,E-10|8,08,E-10|8,08,E-10|8,08,E-10|8,08,E-10|
|AREA|SRC_526|Cam_Valpo_112-PTAS|272979|6386909|7 meses|229,32|7,60,E-10|7,60,E-10|7,60,E-10|7,60,E-10|7,60,E-10|
|AREA|SRC_527|Cam_Valpo_113-PTAS|272982|6386950|7 meses|168,20|1,04,E-09|1,04,E-09|1,04,E-09|1,04,E-09|1,04,E-09|
|AREA|SRC_528|Cam_Valpo_114-PTAS|272974|6387033|7 meses|334,56|5,21,E-10|5,21,E-10|5,21,E-10|5,21,E-10|5,21,E-10|
|AREA|SRC_529|Cam_Valpo_115-PTAS|272969|6387289|7 meses|1021,26|1,71,E-10|1,71,E-10|1,71,E-10|1,71,E-10|1,71,E-10|
|AREA|SRC_530|Cam_Valpo_116-PTAS|272950|6387316|7 meses|135,86|1,28,E-09|1,28,E-09|1,28,E-09|1,28,E-09|1,28,E-09|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 234 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>272918|[m]<br>6387332|[m]<br>6387332|[m2]<br>150,62|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_531|Cam_Valpo_117-PTAS|Cam_Valpo_117-PTAS|Cam_Valpo_117-PTAS|7 meses|7 meses|1,16,E-09|1,16,E-09|1,16,E-09|1,16,E-09|1,16,E-09|
|AREA|SRC_532|Cam_Valpo_118-PTAS|272871|6387328|7 meses|193,11|9,02,E-10|9,02,E-10|9,02,E-10|9,02,E-10|9,02,E-10|
|AREA|SRC_533|Cam_Valpo_119-PTAS|272818|6387319|7 meses|214,82|8,11,E-10|8,11,E-10|8,11,E-10|8,11,E-10|8,11,E-10|
|AREA|SRC_534|Cam_Valpo_120-PTAS|272669|6387324|7 meses|593,51|2,94,E-10|2,94,E-10|2,94,E-10|2,94,E-10|2,94,E-10|
|AREA|SRC_535|Cam_Valpo_121-PTAS|272536|6387380|7 meses|574,11|3,04,E-10|3,04,E-10|3,04,E-10|3,04,E-10|3,04,E-10|
|AREA|SRC_536|Cam_Valpo_122-PTAS|272406|6387475|7 meses|642,85|2,71,E-10|2,71,E-10|2,71,E-10|2,71,E-10|2,71,E-10|
|AREA|SRC_537|Cam_Valpo_123-PTAS|272321|6387544|7 meses|438,86|3,97,E-10|3,97,E-10|3,97,E-10|3,97,E-10|3,97,E-10|
|AREA|SRC_538|Cam_Valpo_124-PTAS|272252|6387605|7 meses|366,01|4,76,E-10|4,76,E-10|4,76,E-10|4,76,E-10|4,76,E-10|
|AREA|SRC_539|Cam_Valpo_125-PTAS|272138|6387749|7 meses|733,97|2,37,E-10|2,37,E-10|2,37,E-10|2,37,E-10|2,37,E-10|
|AREA|SRC_540|Cam_Valpo_126-PTAS|272059|6387890|7 meses|645,70|2,70,E-10|2,70,E-10|2,70,E-10|2,70,E-10|2,70,E-10|
|AREA|SRC_541|Cam_Valpo_127-PTAS|272019|6388008|7 meses|494,29|3,53,E-10|3,53,E-10|3,53,E-10|3,53,E-10|3,53,E-10|
|AREA|SRC_542|Cam_Valpo_128-PTAS|272005|6388086|7 meses|318,17|5,48,E-10|5,48,E-10|5,48,E-10|5,48,E-10|5,48,E-10|
|AREA|SRC_543|Cam_Valpo_129-PTAS|272005|6388171|7 meses|338,40|5,15,E-10|5,15,E-10|5,15,E-10|5,15,E-10|5,15,E-10|
|AREA|SRC_544|Cam_Valpo_130-PTAS|272018|6388207|7 meses|149,40|1,17,E-09|1,17,E-09|1,17,E-09|1,17,E-09|1,17,E-09|
|AREA|SRC_545|Cam_Valpo_131-PTAS|272053|6388222|7 meses|144,57|1,21,E-09|1,21,E-09|1,21,E-09|1,21,E-09|1,21,E-09|
|AREA|SRC_546|Cam_Valpo_132-PTAS|272113|6388260|7 meses|286,19|6,09,E-10|6,09,E-10|6,09,E-10|6,09,E-10|6,09,E-10|
|AREA|SRC_547|Cam_Valpo_133-PTAS|272165|6388289|7 meses|236,50|7,37,E-10|7,37,E-10|7,37,E-10|7,37,E-10|7,37,E-10|
|AREA|SRC_548|Cam_Valpo_134-PTAS|272170|6388313|7 meses|103,04|1,69,E-09|1,69,E-09|1,69,E-09|1,69,E-09|1,69,E-09|
|AREA|SRC_549|Cam_Valpo_135-PTAS|272160|6388355|7 meses|178,67|9,75,E-10|9,75,E-10|9,75,E-10|9,75,E-10|9,75,E-10|
|AREA|SRC_550|Cam_Valpo_136-PTAS|272116|6388384|7 meses|213,17|8,17,E-10|8,17,E-10|8,17,E-10|8,17,E-10|8,17,E-10|
|AREA|SRC_551|Cam_Valpo_137-PTAS|271990|6388473|7 meses|618,26|2,82,E-10|2,82,E-10|2,82,E-10|2,82,E-10|2,82,E-10|
|AREA|SRC_552|Cam_Valpo_138-PTAS|271909|6388570|7 meses|502,24|3,47,E-10|3,47,E-10|3,47,E-10|3,47,E-10|3,47,E-10|
|AREA|SRC_553|Cam_Valpo_139-PTAS|271887|6388631|7 meses|257,67|6,76,E-10|6,76,E-10|6,76,E-10|6,76,E-10|6,76,E-10|
|AREA|SRC_554|Cam_Valpo_140-PTAS|271869|6388710|7 meses|324,57|5,37,E-10|5,37,E-10|5,37,E-10|5,37,E-10|5,37,E-10|
|AREA|SRC_555|Cam_Valpo_141-PTAS|271879|6388778|7 meses|270,72|6,44,E-10|6,44,E-10|6,44,E-10|6,44,E-10|6,44,E-10|
|AREA|SRC_556|Cam_Valpo_142-PTAS|271889|6388831|7 meses|215,81|8,07,E-10|8,07,E-10|8,07,E-10|8,07,E-10|8,07,E-10|
|AREA|SRC_557|Cam_Valpo_143-PTAS|271888|6388910|7 meses|317,54|5,49,E-10|5,49,E-10|5,49,E-10|5,49,E-10|5,49,E-10|
|AREA|SRC_558|Cam_Valpo_144-PTAS|271765|6389249|7 meses|1443,83|1,21,E-10|1,21,E-10|1,21,E-10|1,21,E-10|1,21,E-10|
|AREA|SRC_559|Cam_Valpo_145-PTAS|271745|6389323|7 meses|308,68|5,65,E-10|5,65,E-10|5,65,E-10|5,65,E-10|5,65,E-10|
|AREA|SRC_560|Cam_Valpo_146-PTAS|271746|6389404|7 meses|321,13|5,43,E-10|5,43,E-10|5,43,E-10|5,43,E-10|5,43,E-10|
|AREA|SRC_561|Cam_Valpo_147-PTAS|271745|6389713|7 meses|1235,33|1,41,E-10|1,41,E-10|1,41,E-10|1,41,E-10|1,41,E-10|
|AREA|SRC_562|Cam_Valpo_148-PTAS|271729|6389779|7 meses|274,74|6,34,E-10|6,34,E-10|6,34,E-10|6,34,E-10|6,34,E-10|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 235 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>271405|[m]<br>6390771|[m]<br>6390771|[m2]<br>4169,69|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_563|Cam_Valpo_149-PTAS|Cam_Valpo_149-PTAS|Cam_Valpo_149-PTAS|7 meses|7 meses|4,18,E-11|4,18,E-11|4,18,E-11|4,18,E-11|4,18,E-11|
|AREA|SRC_564|Cam_Valpo_150-PTAS|271408|6390852|7 meses|324,07|5,38,E-10|5,38,E-10|5,38,E-10|5,38,E-10|5,38,E-10|
|AREA|SRC_565|Cam_Valpo_151-PTAS|271425|6390918|7 meses|269,76|6,46,E-10|6,46,E-10|6,46,E-10|6,46,E-10|6,46,E-10|
|AREA|SRC_566|Cam_Valpo_152-PTAS|271595|6391444|7 meses|2210,20|7,88,E-11|7,88,E-11|7,88,E-11|7,88,E-11|7,88,E-11|
|AREA|SRC_567|Cam_Valpo_153-PTAS|271601|6391518|7 meses|297,07|5,87,E-10|5,87,E-10|5,87,E-10|5,87,E-10|5,87,E-10|
|AREA|SRC_568|Cam_Valpo_154-PTAS|271583|6391599|7 meses|334,56|5,21,E-10|5,21,E-10|5,21,E-10|5,21,E-10|5,21,E-10|
|AREA|SRC_569|Cam_Valpo_155-PTAS|271490|6391665|7 meses|462,29|3,77,E-10|3,77,E-10|3,77,E-10|3,77,E-10|3,77,E-10|
|AREA|SRC_570|Cam_Valpo_156-PTAS|271388|6391779|7 meses|610,49|2,85,E-10|2,85,E-10|2,85,E-10|2,85,E-10|2,85,E-10|
|AREA|SRC_571|Cam_Valpo_157-PTAS|271303|6391969|7 meses|829,95|2,10,E-10|2,10,E-10|2,10,E-10|2,10,E-10|2,10,E-10|
|AREA|SRC_572|Cam_Valpo_158-PTAS|271249|6392048|7 meses|385,48|4,52,E-10|4,52,E-10|4,52,E-10|4,52,E-10|4,52,E-10|
|AREA|SRC_573|Cam_Valpo_159-PTAS|271095|6392199|7 meses|863,11|2,02,E-10|2,02,E-10|2,02,E-10|2,02,E-10|2,02,E-10|
|AREA|SRC_574|Cam_Valpo_160-PTAS|271003|6392357|7 meses|727,41|2,40,E-10|2,40,E-10|2,40,E-10|2,40,E-10|2,40,E-10|
|AREA|SRC_575|Cam_Valpo_161-PTAS|270864|6392618|7 meses|1181,67|1,47,E-10|1,47,E-10|1,47,E-10|1,47,E-10|1,47,E-10|
|AREA|SRC_576|Cam_Valpo_162-PTAS|270665|6392901|7 meses|1386,67|1,26,E-10|1,26,E-10|1,26,E-10|1,26,E-10|1,26,E-10|
|AREA|SRC_577|Cam_Valpo_163-PTAS|270570|6393060|7 meses|739,81|2,36,E-10|2,36,E-10|2,36,E-10|2,36,E-10|2,36,E-10|
|AREA|SRC_578|Cam_Valpo_164-PTAS|270535|6393162|7 meses|427,94|4,07,E-10|4,07,E-10|4,07,E-10|4,07,E-10|4,07,E-10|
|AREA|SRC_579|Cam_Valpo_165-PTAS|270408|6393157|7 meses|516,16|3,38,E-10|3,38,E-10|3,38,E-10|3,38,E-10|3,38,E-10|
|AREA|SRC_580|Cam_Valpo_166-PTAS|270322|6393156|7 meses|344,11|5,06,E-10|5,06,E-10|5,06,E-10|5,06,E-10|5,06,E-10|
|AREA|SRC_581|Cam_Valpo_167-PTAS|270198|6393225|7 meses|562,03|3,10,E-10|3,10,E-10|3,10,E-10|3,10,E-10|3,10,E-10|
|AREA|SRC_582|Cam_Valpo_168-PTAS|270084|6393222|7 meses|461,57|3,78,E-10|3,78,E-10|3,78,E-10|3,78,E-10|3,78,E-10|
|AREA|SRC_583|Cam_Valpo_169-PTAS|270014|6393114|7 meses|520,05|3,35,E-10|3,35,E-10|3,35,E-10|3,35,E-10|3,35,E-10|
|AREA|SRC_584|Cam_Valpo_170-PTAS|269944|6393026|7 meses|448,19|3,89,E-10|3,89,E-10|3,89,E-10|3,89,E-10|3,89,E-10|
|AREA|SRC_585|Cam_Valpo_171-PTAS|269831|6392981|7 meses|484,35|3,60,E-10|3,60,E-10|3,60,E-10|3,60,E-10|3,60,E-10|
|AREA|SRC_586|Cam_Valpo_172-PTAS|269702|6392966|7 meses|516,99|3,37,E-10|3,37,E-10|3,37,E-10|3,37,E-10|3,37,E-10|
|AREA|SRC_587|Cam_Valpo_173-PTAS|269506|6393084|7 meses|906,73|1,92,E-10|1,92,E-10|1,92,E-10|1,92,E-10|1,92,E-10|
|AREA|SRC_588|Cam_Valpo_174-PTAS|269407|6393106|7 meses|410,62|4,24,E-10|4,24,E-10|4,24,E-10|4,24,E-10|4,24,E-10|
|AREA|SRC_589|Cam_Valpo_175-PTAS|269355|6393219|7 meses|493,13|3,53,E-10|3,53,E-10|3,53,E-10|3,53,E-10|3,53,E-10|
|AREA|SRC_590|Cam_Valpo_176-PTAS|269450|6393436|7 meses|939,57|1,85,E-10|1,85,E-10|1,85,E-10|1,85,E-10|1,85,E-10|
|AREA|SRC_591|Cam_Valpo_177-PTAS|269537|6393768|7 meses|1375,49|1,27,E-10|1,27,E-10|1,27,E-10|1,27,E-10|1,27,E-10|
|AREA|SRC_592|Cam_Valpo_178-PTAS|269541|6393876|7 meses|433,16|4,02,E-10|4,02,E-10|4,02,E-10|4,02,E-10|4,02,E-10|
|AREA|SRC_593|Cam_Valpo_179-PTAS|269514|6393952|7 meses|327,49|5,32,E-10|5,32,E-10|5,32,E-10|5,32,E-10|5,32,E-10|
|AREA|SRC_594|Cam_Valpo_180-PTAS|269461|6394006|7 meses|302,03|5,77,E-10|5,77,E-10|5,77,E-10|5,77,E-10|5,77,E-10|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 236 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>269456|[m]<br>6394087|[m]<br>6394087|[m2]<br>317,54|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_595|Cam_Valpo_181-PTAS|Cam_Valpo_181-PTAS|Cam_Valpo_181-PTAS|7 meses|7 meses|5,49,E-10|5,49,E-10|5,49,E-10|5,49,E-10|5,49,E-10|
|AREA|SRC_596|Cam_Valpo_182-PTAS|269494|6394169|7 meses|358,94|4,85,E-10|4,85,E-10|4,85,E-10|4,85,E-10|4,85,E-10|
|AREA|SRC_597|Cam_Valpo_183-PTAS|269580|6394296|7 meses|611,99|2,85,E-10|2,85,E-10|2,85,E-10|2,85,E-10|2,85,E-10|
|AREA|SRC_598|Cam_Valpo_184-PTAS|269614|6394394|7 meses|416,61|4,18,E-10|4,18,E-10|4,18,E-10|4,18,E-10|4,18,E-10|
|AREA|SRC_599|Cam_Valpo_185-PTAS|269617|6394492|7 meses|396,57|4,39,E-10|4,39,E-10|4,39,E-10|4,39,E-10|4,39,E-10|
|AREA|SRC_600|Cam_Valpo_186-PTAS|269532|6394634|7 meses|664,18|2,62,E-10|2,62,E-10|2,62,E-10|2,62,E-10|2,62,E-10|
|AREA|SRC_601|Cam_Valpo_187-PTAS|269478|6394752|7 meses|518,20|3,36,E-10|3,36,E-10|3,36,E-10|3,36,E-10|3,36,E-10|
|AREA|SRC_602|Cam_Valpo_188-PTAS|269437|6394881|7 meses|540,93|3,22,E-10|3,22,E-10|3,22,E-10|3,22,E-10|3,22,E-10|
|AREA|SRC_603|Cam_Valpo_189-PTAS|269448|6395002|7 meses|483,46|3,60,E-10|3,60,E-10|3,60,E-10|3,60,E-10|3,60,E-10|
|AREA|SRC_604|Cam_Valpo_190-PTAS|269465|6395049|7 meses|197,82|8,81,E-10|8,81,E-10|8,81,E-10|8,81,E-10|8,81,E-10|
|AREA|SRC_605|Cam_Valpo_191-PTAS|269701|6395188|7 meses|1088,66|1,60,E-10|1,60,E-10|1,60,E-10|1,60,E-10|1,60,E-10|
|AREA|SRC_606|Cam_Valpo_192-PTAS|269737|6395244|7 meses|269,38|6,47,E-10|6,47,E-10|6,47,E-10|6,47,E-10|6,47,E-10|
|AREA|SRC_607|Cam_Valpo_193-PTAS|269748|6395318|7 meses|301,88|5,77,E-10|5,77,E-10|5,77,E-10|5,77,E-10|5,77,E-10|
|AREA|SRC_608|Cam_Valpo_194-PTAS|269734|6395473|7 meses|624,02|2,79,E-10|2,79,E-10|2,79,E-10|2,79,E-10|2,79,E-10|
|AREA|SRC_609|Cam_Valpo_195-PTAS|269791|6395575|7 meses|462,91|3,76,E-10|3,76,E-10|3,76,E-10|3,76,E-10|3,76,E-10|
|AREA|SRC_610|Cam_Valpo_196-PTAS|269918|6395634|7 meses|557,57|3,13,E-10|3,13,E-10|3,13,E-10|3,13,E-10|3,13,E-10|
|AREA|SRC_611|Cam_Valpo_197-PTAS|269951|6395703|7 meses|311,66|5,59,E-10|5,59,E-10|5,59,E-10|5,59,E-10|5,59,E-10|
|AREA|SRC_612|Cam_Valpo_198-PTAS|269926|6395767|7 meses|277,87|6,27,E-10|6,27,E-10|6,27,E-10|6,27,E-10|6,27,E-10|
|AREA|SRC_613|Cam_Valpo_199-PTAS|269853|6395812|7 meses|348,28|5,00,E-10|5,00,E-10|5,00,E-10|5,00,E-10|5,00,E-10|
|AREA|SRC_614|Cam_Valpo_200-PTAS|269732|6395847|7 meses|504,67|3,45,E-10|3,45,E-10|3,45,E-10|3,45,E-10|3,45,E-10|
|AREA|SRC_615|Cam_Valpo_201-PTAS|269688|6395928|7 meses|365,46|4,77,E-10|4,77,E-10|4,77,E-10|4,77,E-10|4,77,E-10|
|AREA|SRC_616|Cam_Valpo_202-PTAS|269717|6396047|7 meses|484,68|3,60,E-10|3,60,E-10|3,60,E-10|3,60,E-10|3,60,E-10|
|AREA|SRC_617|Cam_Valpo_203-PTAS|269712|6396106|7 meses|237,49|7,34,E-10|7,34,E-10|7,34,E-10|7,34,E-10|7,34,E-10|
|AREA|SRC_618|Cam_Valpo_204-PTAS|269657|6396143|7 meses|271,48|6,42,E-10|6,42,E-10|6,42,E-10|6,42,E-10|6,42,E-10|
|AREA|SRC_619|Cam_Valpo_205-PTAS|269580|6396120|7 meses|326,46|5,34,E-10|5,34,E-10|5,34,E-10|5,34,E-10|5,34,E-10|
|AREA|SRC_620|Cam_Valpo_206-PTAS|269501|6396070|7 meses|376,20|4,63,E-10|4,63,E-10|4,63,E-10|4,63,E-10|4,63,E-10|
|AREA|SRC_621|Cam_Valpo_207-PTAS|269359|6396026|7 meses|593,54|2,94,E-10|2,94,E-10|2,94,E-10|2,94,E-10|2,94,E-10|
|AREA|SRC_622|Cam_Valpo_208-PTAS|269272|6396023|7 meses|343,48|5,07,E-10|5,07,E-10|5,07,E-10|5,07,E-10|5,07,E-10|
|AREA|SRC_623|Cam_Valpo_209-PTAS|269222|6396073|7 meses|275,81|6,32,E-10|6,32,E-10|6,32,E-10|6,32,E-10|6,32,E-10|
|AREA|SRC_624|Cam_Valpo_210-PTAS|269210|6396185|7 meses|446,25|3,90,E-10|3,90,E-10|3,90,E-10|3,90,E-10|3,90,E-10|
|AREA|SRC_625|Cam_Valpo_211-PTAS|269167|6396232|7 meses|255,46|6,82,E-10|6,82,E-10|6,82,E-10|6,82,E-10|6,82,E-10|
|AREA|SRC_626|Cam_Valpo_212-PTAS|269082|6396226|7 meses|349,58|4,98,E-10|4,98,E-10|4,98,E-10|4,98,E-10|4,98,E-10|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 237 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>268998|[m]<br>6396240|[m]<br>6396240|[m2]<br>335,54|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_627|Cam_Valpo_213-PTAS|Cam_Valpo_213-PTAS|Cam_Valpo_213-PTAS|7 meses|7 meses|5,19,E-10|5,19,E-10|5,19,E-10|5,19,E-10|5,19,E-10|
|AREA|SRC_628|Cam_Valpo_214-PTAS|268894|6396300|7 meses|480,09|3,63,E-10|3,63,E-10|3,63,E-10|3,63,E-10|3,63,E-10|
|AREA|SRC_629|Cam_Valpo_215-PTAS|268805|6396381|7 meses|477,49|3,65,E-10|3,65,E-10|3,65,E-10|3,65,E-10|3,65,E-10|
|AREA|SRC_630|Cam_Valpo_216-PTAS|268734|6396481|7 meses|489,34|3,56,E-10|3,56,E-10|3,56,E-10|3,56,E-10|3,56,E-10|
|AREA|SRC_631|Cam_Valpo_217-PTAS|268692|6396569|7 meses|388,32|4,49,E-10|4,49,E-10|4,49,E-10|4,49,E-10|4,49,E-10|
|AREA|SRC_632|Cam_Valpo_218-PTAS|268614|6396686|7 meses|563,68|3,09,E-10|3,09,E-10|3,09,E-10|3,09,E-10|3,09,E-10|
|AREA|SRC_633|Cam_Valpo_219-PTAS|268551|6396751|7 meses|365,13|4,77,E-10|4,77,E-10|4,77,E-10|4,77,E-10|4,77,E-10|
|AREA|SRC_634|Cam_Valpo_220-PTAS|268525|6396834|7 meses|342,75|5,08,E-10|5,08,E-10|5,08,E-10|5,08,E-10|5,08,E-10|
|AREA|SRC_635|Cam_Valpo_221-PTAS|268521|6396918|7 meses|335,20|5,20,E-10|5,20,E-10|5,20,E-10|5,20,E-10|5,20,E-10|
|AREA|SRC_636|Cam_Valpo_222-PTAS|268510|6396996|7 meses|312,17|5,58,E-10|5,58,E-10|5,58,E-10|5,58,E-10|5,58,E-10|
|AREA|SRC_637|Cam_Valpo_223-PTAS|268441|6397095|7 meses|486,78|3,58,E-10|3,58,E-10|3,58,E-10|3,58,E-10|3,58,E-10|
|AREA|SRC_638|Cam_Valpo_224-PTAS|268352|6397195|7 meses|537,81|3,24,E-10|3,24,E-10|3,24,E-10|3,24,E-10|3,24,E-10|
|AREA|SRC_639|Cam_Valpo_225-PTAS|268295|6397296|7 meses|460,41|3,78,E-10|3,78,E-10|3,78,E-10|3,78,E-10|3,78,E-10|
|AREA|SRC_640|Cam_Valpo_226-PTAS|268265|6397370|7 meses|319,00|5,46,E-10|5,46,E-10|5,46,E-10|5,46,E-10|5,46,E-10|
|AREA|SRC_641|Cam_Valpo_227-PTAS|268236|6397470|7 meses|414,51|4,20,E-10|4,20,E-10|4,20,E-10|4,20,E-10|4,20,E-10|
|AREA|SRC_642|Cam_Valpo_228-PTAS|268225|6397539|7 meses|278,02|6,27,E-10|6,27,E-10|6,27,E-10|6,27,E-10|6,27,E-10|
|AREA|SRC_643|Cam_Valpo_229-PTAS|268212|6397650|7 meses|446,47|3,90,E-10|3,90,E-10|3,90,E-10|3,90,E-10|3,90,E-10|
|AREA|SRC_644|Cam_Valpo_230-PTAS|268292|6397691|7 meses|352,90|4,94,E-10|4,94,E-10|4,94,E-10|4,94,E-10|4,94,E-10|
|AREA|SRC_645|Cam_Valpo_231-PTAS|268324|6397741|7 meses|244,09|7,14,E-10|7,14,E-10|7,14,E-10|7,14,E-10|7,14,E-10|
|AREA|SRC_646|Cam_Valpo_232-PTAS|268344|6397809|7 meses|284,52|6,12,E-10|6,12,E-10|6,12,E-10|6,12,E-10|6,12,E-10|
|AREA|SRC_647|Cam_Valpo_233-PTAS|268317|6397871|7 meses|277,40|6,28,E-10|6,28,E-10|6,28,E-10|6,28,E-10|6,28,E-10|
|AREA|SRC_648|Cam_Valpo_234-PTAS|268289|6397931|7 meses|263,44|6,61,E-10|6,61,E-10|6,61,E-10|6,61,E-10|6,61,E-10|
|AREA|SRC_649|Cam_Valpo_235-PTAS|268281|6397993|7 meses|246,21|7,08,E-10|7,08,E-10|7,08,E-10|7,08,E-10|7,08,E-10|
|AREA|SRC_650|Cam_Valpo_236-PTAS|268325|6398057|7 meses|307,11|5,67,E-10|5,67,E-10|5,67,E-10|5,67,E-10|5,67,E-10|
|AREA|SRC_651|Cam_Valpo_237-PTAS|268339|6398092|7 meses|154,12|1,13,E-09|1,13,E-09|1,13,E-09|1,13,E-09|1,13,E-09|
|AREA|SRC_652|Cam_Valpo_238-PTAS|268362|6398151|7 meses|251,56|6,93,E-10|6,93,E-10|6,93,E-10|6,93,E-10|6,93,E-10|
|AREA|SRC_653|Cam_Valpo_239-PTAS|268383|6398192|7 meses|185,19|9,41,E-10|9,41,E-10|9,41,E-10|9,41,E-10|9,41,E-10|
|AREA|SRC_654|Cam_Valpo_240-PTAS|268355|6398247|7 meses|250,18|6,97,E-10|6,97,E-10|6,97,E-10|6,97,E-10|6,97,E-10|
|AREA|SRC_655|Cam_Valpo_241-PTAS|268227|6398303|7 meses|566,84|3,07,E-10|3,07,E-10|3,07,E-10|3,07,E-10|3,07,E-10|
|AREA|SRC_656|Cam_Valpo_242-PTAS|268140|6398362|7 meses|418,83|4,16,E-10|4,16,E-10|4,16,E-10|4,16,E-10|4,16,E-10|
|AREA|SRC_657|Cam_Valpo_243-PTAS|268089|6398427|7 meses|325,43|5,35,E-10|5,35,E-10|5,35,E-10|5,35,E-10|5,35,E-10|
|AREA|SRC_658|Cam_Valpo_244-PTAS|268005|6398483|7 meses|406,15|4,29,E-10|4,29,E-10|4,29,E-10|4,29,E-10|4,29,E-10|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 238 de 252

Tabla 110. Fuentes de Emisión - Escenario 3 parte 12

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>267956|[m]<br>6398553|[m]<br>6398553|[m2]<br>338,26|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_659|Cam_Valpo_245-PTAS|Cam_Valpo_245-PTAS|Cam_Valpo_245-PTAS|7 meses|7 meses|5,15,E-10|5,15,E-10|5,15,E-10|5,15,E-10|5,15,E-10|
|AREA|SRC_660|Cam_Valpo_246-PTAS|267920|6398673|7 meses|498,96|3,49,E-10|3,49,E-10|3,49,E-10|3,49,E-10|3,49,E-10|
|AREA|SRC_661|Cam_Valpo_247-PTAS|267908|6398749|7 meses|308,37|5,65,E-10|5,65,E-10|5,65,E-10|5,65,E-10|5,65,E-10|
|AREA|SRC_662|Cam_Valpo_248-PTAS|267894|6398771|7 meses|107,41|1,62,E-09|1,62,E-09|1,62,E-09|1,62,E-09|1,62,E-09|
|AREA|SRC_663|Cam_Valpo_249-PTAS|267791|6398823|7 meses|466,56|3,73,E-10|3,73,E-10|3,73,E-10|3,73,E-10|3,73,E-10|
|AREA|SRC_664|Cam_Valpo_250-PTAS|267747|6398849|7 meses|204,00|8,54,E-10|8,54,E-10|8,54,E-10|8,54,E-10|8,54,E-10|
|AREA|SRC_665|Cam_Valpo_251-PTAS|267699|6398875|7 meses|217,15|8,02,E-10|8,02,E-10|8,02,E-10|8,02,E-10|8,02,E-10|
|AREA|SRC_666|Cam_Valpo_252-PTAS|267673|6398943|7 meses|285,91|6,09,E-10|6,09,E-10|6,09,E-10|6,09,E-10|6,09,E-10|
|AREA|SRC_667|Cam_Valpo_253-PTAS|267740|6399152|7 meses|871,99|2,00,E-10|2,00,E-10|2,00,E-10|2,00,E-10|2,00,E-10|
|AREA|SRC_668|Cam_Valpo_254-PTAS|267754|6399259|7 meses|434,37|4,01,E-10|4,01,E-10|4,01,E-10|4,01,E-10|4,01,E-10|
|AREA|SRC_669|Cam_Valpo_255-PTAS|267756|6399372|7 meses|452,93|3,85,E-10|3,85,E-10|3,85,E-10|3,85,E-10|3,85,E-10|
|AREA|SRC_670|Cam_Valpo_256-PTAS|267702|6399478|7 meses|480,03|3,63,E-10|3,63,E-10|3,63,E-10|3,63,E-10|3,63,E-10|
|AREA|SRC_671|Cam_Valpo_257-PTAS|267740|6399547|7 meses|307,21|5,67,E-10|5,67,E-10|5,67,E-10|5,67,E-10|5,67,E-10|
|AREA|SRC_672|Cam_Valpo_258-PTAS|267742|6399624|7 meses|311,56|5,59,E-10|5,59,E-10|5,59,E-10|5,59,E-10|5,59,E-10|
|AREA|SRC_673|Cam_Valpo_259-PTAS|267731|6399695|7 meses|287,58|6,06,E-10|6,06,E-10|6,06,E-10|6,06,E-10|6,06,E-10|
|AREA|SRC_674|Cam_Valpo_260-PTAS|267682|6399788|7 meses|425,70|4,09,E-10|4,09,E-10|4,09,E-10|4,09,E-10|4,09,E-10|
|AREA|SRC_675|Cam_Valpo_261-PTAS|267661|6399830|7 meses|187,04|9,32,E-10|9,32,E-10|9,32,E-10|9,32,E-10|9,32,E-10|

Tabla 134. Fuentes de Emisión - Escenario 4 parte 23

|Tipo|ID|Descripción|X1|Y1|Ciclo operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/s]|[g/s]|[g/s]|[g/s]|[g/s]|
|VOLUMEN|SRC_8|Colec_x1|271162|6382782|3 meses|4,00|0,00014|0,00002|0,00000|0,00000|0,00000|
|VOLUMEN|SRC_9|Colec_x2|271234|6382757|3 meses|4,00|0,00014|0,00002|0,00000|0,00000|0,00000|
|VOLUMEN|SRC_10|Colec_x3|271319|6382735|3 meses|4,00|0,00014|0,00002|0,00000|0,00000|0,00000|
|VOLUMEN|SRC_11|Colec_x4|271283|6382674|3 meses|4,00|0,00014|0,00002|0,00000|0,00000|0,00000|
|VOLUMEN|SRC_12|Colec_x5|271240|6382629|3 meses|4,00|0,00014|0,00002|0,00000|0,00000|0,00000|
|VOLUMEN|SRC_13|Colec_x6|271298|6382494|3 meses|4,00|0,00014|0,00002|0,00000|0,00000|0,00000|
|VOLUMEN|SRC_14|Colec_x7|271379|6382403|3 meses|4,00|0,00014|0,00002|0,00000|0,00000|0,00000|
|VOLUMEN|SRC_346|PTAS|273588|6383221|7 meses|4,00|0,00064|0,00010|0,00000|0,00000|0,00000|
|PUNTUAL|SRC_15|IF1|273522|6383276|3 meses|0,05|0,00199|0,00048|0,00000|0,05662|0,01223|
|PUNTUAL|SRC_16|IF2|273522|6383276|3 meses|0,05|0,00199|0,00048|0,00000|0,05662|0,01223|
|PUNTUAL|SRC_347|PTAS|273588|6383221|7 meses|0,05|0,00200|0,00048|0,00000|0,05677|0,01226|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

**17.5 FUENTES DE EMISIÓN - ESCENARIO 5**

Tabla 135. Fuentes de Emisión - Escenario 5 parte 1

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 239 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_1|PTAS|273586|6383219|4 mes|4,00|4,29,E-03|4,29,E-03|0,00,E+00|0,00,E+00|0,00,E+00|
|AREA|SRC_4|Cam_Cat_1-PEAS e Imp|273043|6387323|3 mes|383,32|6,04,E-10|1,46,E-10|3,40,E-10|6,80,E-09|1,93,E-11|
|AREA|SRC_5|Cam_Cat_2-PEAS e Imp|273206|6387558|3 mes|1145,03|2,02,E-10|4,89,E-11|1,14,E-10|2,28,E-09|6,45,E-12|
|AREA|SRC_6|Cam_Cat_3-PEAS e Imp|273308|6387612|3 mes|456,00|5,07,E-10|1,23,E-10|2,86,E-10|5,72,E-09|1,62,E-11|
|AREA|SRC_7|Cam_Cat_4-PEAS e Imp|273511|6387668|3 mes|843,57|2,74,E-10|6,64,E-11|1,54,E-10|3,09,E-09|8,75,E-12|
|AREA|SRC_8|Cam_Cat_5-PEAS e Imp|273721|6387707|3 mes|853,32|2,71,E-10|6,56,E-11|1,53,E-10|3,05,E-09|8,65,E-12|
|AREA|SRC_9|Cam_Cat_6-PEAS e Imp|273880|6387880|3 mes|945,26|2,45,E-10|5,92,E-11|1,38,E-10|2,76,E-09|7,81,E-12|
|AREA|SRC_10|Cam_Cat_7-PEAS e Imp|273982|6387934|3 mes|457,52|5,06,E-10|1,22,E-10|2,85,E-10|5,70,E-09|1,61,E-11|
|AREA|SRC_11|Cam_Cat_8-PEAS e Imp|274178|6387916|3 mes|782,20|2,96,E-10|7,16,E-11|1,67,E-10|3,33,E-09|9,44,E-12|
|AREA|SRC_12|Cam_Cat_9-PEAS e Imp|274216|6387945|3 mes|195,48|1,18,E-09|2,86,E-10|6,66,E-10|1,33,E-08|3,78,E-11|
|AREA|SRC_13|Cam_Cat_10-PEAS e Imp|274213|6388017|3 mes|295,61|7,83,E-10|1,89,E-10|4,41,E-10|8,82,E-09|2,50,E-11|
|AREA|SRC_14|Cam_Cat_11-PEAS e Imp|274177|6388250|3 mes|941,53|2,46,E-10|5,95,E-11|1,38,E-10|2,77,E-09|7,84,E-12|
|AREA|SRC_15|Cam_Cat_12-PEAS e Imp|274185|6388365|3 mes|458,34|5,05,E-10|1,22,E-10|2,84,E-10|5,69,E-09|1,61,E-11|
|AREA|SRC_16|Cam_Cat_13-PEAS e Imp|274352|6388558|3 mes|1016,92|2,28,E-10|5,50,E-11|1,28,E-10|2,56,E-09|7,26,E-12|
|AREA|SRC_17|Cam_Cat_14-PEAS e Imp|274654|6388846|3 mes|1667,00|1,39,E-10|3,36,E-11|7,81,E-11|1,56,E-09|4,43,E-12|
|AREA|SRC_18|Cam_Cat_15-PEAS e Imp|274745|6388895|3 mes|409,81|5,65,E-10|1,37,E-10|3,18,E-10|6,36,E-09|1,80,E-11|
|AREA|SRC_19|Cam_Cat_16-PEAS e Imp|274834|6388862|3 mes|371,12|6,23,E-10|1,51,E-10|3,51,E-10|7,02,E-09|1,99,E-11|
|AREA|SRC_20|Cam_Cat_17-PEAS e Imp|274882|6388794|3 mes|331,29|6,98,E-10|1,69,E-10|3,93,E-10|7,87,E-09|2,23,E-11|
|AREA|SRC_21|Cam_Cat_18-PEAS e Imp|274979|6388768|3 mes|406,63|5,69,E-10|1,38,E-10|3,20,E-10|6,41,E-09|1,82,E-11|
|AREA|SRC_22|Cam_Cat_19-PEAS e Imp|275069|6388799|3 mes|384,16|6,02,E-10|1,46,E-10|3,39,E-10|6,78,E-09|1,92,E-11|
|AREA|SRC_23|Cam_Cat_20-PEAS e Imp|275059|6388911|3 mes|459,52|5,04,E-10|1,22,E-10|2,83,E-10|5,67,E-09|1,61,E-11|
|AREA|SRC_24|Cam_Cat_21-PEAS e Imp|275040|6389003|3 mes|374,05|6,19,E-10|1,50,E-10|3,48,E-10|6,97,E-09|1,97,E-11|
|AREA|SRC_25|Cam_Cat_22-PEAS e Imp|274958|6389092|3 mes|489,11|4,73,E-10|1,14,E-10|2,66,E-10|5,33,E-09|1,51,E-11|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 136. Fuentes de Emisión - Escenario 5 parte 2

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 240 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>274915|[m]<br>6389184|[m]<br>6389184|[m2]<br>402,20|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_26|Cam_Cat_23-PEAS e Imp|Cam_Cat_23-PEAS e Imp|Cam_Cat_23-PEAS e Imp|3 mes|3 mes|5,75,E-10|1,39,E-10|3,24,E-10|6,48,E-09|1,84,E-11|
|AREA|SRC_27|Cam_Cat_24-PEAS e Imp|274946|6389307|3 mes|502,79|4,60,E-10|1,11,E-10|2,59,E-10|5,18,E-09|1,47,E-11|
|AREA|SRC_28|Cam_Cat_25-PEAS e Imp|275049|6389374|3 mes|485,06|4,77,E-10|1,15,E-10|2,69,E-10|5,37,E-09|1,52,E-11|
|AREA|SRC_29|Cam_Cat_26-PEAS e Imp|275181|6389406|3 mes|541,36|4,27,E-10|1,03,E-10|2,41,E-10|4,81,E-09|1,36,E-11|
|AREA|SRC_30|Cam_Cat_27-PEAS e Imp|275286|6389385|3 mes|424,34|5,45,E-10|1,32,E-10|3,07,E-10|6,14,E-09|1,74,E-11|
|AREA|SRC_31|Cam_Cat_28-PEAS e Imp|275372|6389387|3 mes|345,06|6,71,E-10|1,62,E-10|3,77,E-10|7,55,E-09|2,14,E-11|
|AREA|SRC_32|Cam_Cat_29-PEAS e Imp|275519|6389442|3 mes|633,26|3,65,E-10|8,84,E-11|2,06,E-10|4,12,E-09|1,17,E-11|
|AREA|SRC_33|Cam_Cat_30-PEAS e Imp|275575|6389512|3 mes|360,36|6,42,E-10|1,55,E-10|3,61,E-10|7,23,E-09|2,05,E-11|
|AREA|SRC_34|Cam_Cat_31-PEAS e Imp|275579|6389623|3 mes|447,31|5,17,E-10|1,25,E-10|2,91,E-10|5,83,E-09|1,65,E-11|
|AREA|SRC_35|Cam_Cat_32-PEAS e Imp|275473|6389738|3 mes|629,59|3,68,E-10|8,89,E-11|2,07,E-10|4,14,E-09|1,17,E-11|
|AREA|SRC_36|Cam_Cat_33-PEAS e Imp|275397|6389809|3 mes|419,18|5,52,E-10|1,34,E-10|3,11,E-10|6,22,E-09|1,76,E-11|
|AREA|SRC_37|Cam_Cat_34-PEAS e Imp|275382|6389918|3 mes|432,78|5,35,E-10|1,29,E-10|3,01,E-10|6,02,E-09|1,71,E-11|
|AREA|SRC_38|Cam_Cat_35-PEAS e Imp|275487|6390018|3 mes|576,65|4,01,E-10|9,71,E-11|2,26,E-10|4,52,E-09|1,28,E-11|
|AREA|SRC_39|Cam_Cat_36-PEAS e Imp|275630|6390045|3 mes|576,34|4,01,E-10|9,71,E-11|2,26,E-10|4,52,E-09|1,28,E-11|
|AREA|SRC_40|Cam_Cat_37-PEAS e Imp|275763|6390025|3 mes|532,94|4,34,E-10|1,05,E-10|2,44,E-10|4,89,E-09|1,39,E-11|
|AREA|SRC_41|Cam_Cat_38-PEAS e Imp|275861|6389993|3 mes|411,71|5,62,E-10|1,36,E-10|3,16,E-10|6,33,E-09|1,79,E-11|
|AREA|SRC_42|Cam_Cat_39-PEAS e Imp|276044|6389963|3 mes|742,87|3,11,E-10|7,54,E-11|1,75,E-10|3,51,E-09|9,94,E-12|
|AREA|SRC_43|Cam_Cat_40-PEAS e Imp|276114|6389925|3 mes|316,96|7,30,E-10|1,77,E-10|4,11,E-10|8,22,E-09|2,33,E-11|
|AREA|SRC_44|Cam_Cat_41-PEAS e Imp|276133|6389885|3 mes|172,93|1,34,E-09|3,24,E-10|7,53,E-10|1,51,E-08|4,27,E-11|
|AREA|SRC_45|Cam_Cat_42-PEAS e Imp|276158|6389818|3 mes|286,84|8,07,E-10|1,95,E-10|4,54,E-10|9,09,E-09|2,57,E-11|
|AREA|SRC_46|Cam_Cat_43-PEAS e Imp|276157|6389659|3 mes|632,84|3,66,E-10|8,85,E-11|2,06,E-10|4,12,E-09|1,17,E-11|
|AREA|SRC_47|Cam_Cat_44-PEAS e Imp|276172|6389529|3 mes|521,10|4,44,E-10|1,07,E-10|2,50,E-10|5,00,E-09|1,42,E-11|
|AREA|SRC_48|Cam_Cat_45-PEAS e Imp|276275|6389477|3 mes|468,32|4,94,E-10|1,20,E-10|2,78,E-10|5,56,E-09|1,58,E-11|
|AREA|SRC_49|Cam_Cat_46-PEAS e Imp|276411|6389458|3 mes|553,37|4,18,E-10|1,01,E-10|2,35,E-10|4,71,E-09|1,33,E-11|
|AREA|SRC_50|Cam_Cat_47-PEAS e Imp|276501|6389471|3 mes|366,24|6,32,E-10|1,53,E-10|3,56,E-10|7,12,E-09|2,02,E-11|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 137. Fuentes de Emisión - Escenario 5 parte 3

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 241 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>276706|[m]<br>6389673|[m]<br>6389673|[m2]<br>1151,46|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_51|Cam_Cat_48-PEAS e Imp|Cam_Cat_48-PEAS e Imp|Cam_Cat_48-PEAS e Imp|3 mes|3 mes|2,01,E-10|4,86,E-11|1,13,E-10|2,26,E-09|6,41,E-12|
|AREA|SRC_52|Cam_Cat_49-PEAS e Imp|277353|6390498|3 mes|4195,41|5,52,E-11|1,33,E-11|3,10,E-11|6,21,E-10|1,76,E-12|
|AREA|SRC_53|Cam_Cat_50-PEAS e Imp|277494|6390575|3 mes|640,03|3,62,E-10|8,75,E-11|2,03,E-10|4,07,E-09|1,15,E-11|
|AREA|SRC_54|Cam_Cat_51-PEAS e Imp|279440|6391244|3 mes|8223,68|2,81,E-11|6,81,E-12|1,58,E-11|3,17,E-10|8,98,E-13|
|AREA|SRC_55|Cam_Cat_52-PEAS e Imp|283346|6393239|3 mes|17540,88|1,32,E-11|3,19,E-12|7,43,E-12|1,49,E-10|4,21,E-13|
|AREA|SRC_56|Cam_Cat_53-PEAS e Imp|287745|6394661|3 mes|18483,13|1,25,E-11|3,03,E-12|7,05,E-12|1,41,E-10|3,99,E-13|
|AREA|SRC_57|Cam_Pta_1-PEAS e Imp|273147|6383634|3 mes|1866,42|1,24,E-10|3,00,E-11|6,98,E-11|1,40,E-09|3,96,E-12|
|AREA|SRC_58|Cam_Pta_2-PEAS e Imp|273165|6383642|3 mes|80,85|2,86,E-09|6,92,E-10|1,61,E-09|3,22,E-08|9,13,E-11|
|AREA|SRC_59|Cam_Pta_3-PEAS e Imp|273189|6383637|3 mes|94,14|2,46,E-09|5,95,E-10|1,38,E-09|2,77,E-08|7,84,E-11|
|AREA|SRC_60|Cam_Pta_4-PEAS e Imp|273241|6383562|3 mes|359,95|6,43,E-10|1,56,E-10|3,62,E-10|7,24,E-09|2,05,E-11|
|AREA|SRC_61|Cam_Pta_5-PEAS e Imp|273289|6383445|3 mes|505,57|4,58,E-10|1,11,E-10|2,58,E-10|5,15,E-09|1,46,E-11|
|AREA|SRC_62|Cam_Pta_6-PEAS e Imp|273304|6383402|3 mes|179,62|1,29,E-09|3,12,E-10|7,25,E-10|1,45,E-08|4,11,E-11|
|AREA|SRC_63|Cam_Pta_7-PEAS e Imp|273331|6383382|3 mes|138,45|1,67,E-09|4,04,E-10|9,41,E-10|1,88,E-08|5,33,E-11|
|AREA|SRC_64|Cam_Pta_8-PEAS e Imp|273361|6383362|3 mes|145,56|1,59,E-09|3,85,E-10|8,95,E-10|1,79,E-08|5,07,E-11|
|AREA|SRC_65|Cam_Pta_9-PEAS e Imp|273393|6383346|3 mes|143,99|1,61,E-09|3,89,E-10|9,05,E-10|1,81,E-08|5,13,E-11|
|AREA|SRC_66|Cam_Pta_10-PEAS e Imp|273413|6383324|3 mes|116,32|1,99,E-09|4,81,E-10|1,12,E-09|2,24,E-08|6,35,E-11|
|AREA|SRC_67|Cam_Pta_11-PEAS e Imp|273447|6383229|3 mes|400,03|5,78,E-10|1,40,E-10|3,26,E-10|6,51,E-09|1,85,E-11|
|AREA|SRC_68|Cam_Pta_12-PEAS e Imp|273463|6383220|3 mes|80,13|2,89,E-09|6,99,E-10|1,63,E-09|3,25,E-08|9,21,E-11|
|AREA|SRC_69|Cam_Pta_13-PEAS e Imp|273473|6383218|3 mes|45,12|5,13,E-09|1,24,E-09|2,89,E-09|5,78,E-08|1,64,E-10|
|AREA|SRC_70|Cam_Pta_14-PEAS e Imp|273519|6383228|3 mes|188,53|1,23,E-09|2,97,E-10|6,91,E-10|1,38,E-08|3,92,E-11|
|AREA|SRC_71|Cam_Valpo_1-PEAS e Imp|267407|6370003|3 mes|9181,86|2,52,E-11|6,10,E-12|1,42,E-11|2,84,E-10|8,04,E-13|
|AREA|SRC_72|Cam_Valpo_2-PEAS e Imp|267402|6370088|3 mes|338,29|6,84,E-10|1,65,E-10|3,85,E-10|7,70,E-09|2,18,E-11|
|AREA|SRC_73|Cam_Valpo_3-PEAS e Imp|267699|6371506|3 mes|5788,94|4,00,E-11|9,67,E-12|2,25,E-11|4,50,E-10|1,28,E-12|
|AREA|SRC_74|Cam_Valpo_4-PEAS e Imp|267700|6371619|3 mes|452,00|5,12,E-10|1,24,E-10|2,88,E-10|5,77,E-09|1,63,E-11|
|AREA|SRC_75|Cam_Valpo_5-PEAS e Imp|267517|6371917|3 mes|1401,44|1,65,E-10|3,99,E-11|9,29,E-11|1,86,E-09|5,27,E-12|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 138. Fuentes de Emisión - Escenario 5 parte 4

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 242 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>267499|[m]<br>6371980|[m]<br>6371980|[m2]<br>261,10|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_76|Cam_Valpo_6-PEAS e Imp|Cam_Valpo_6-PEAS e Imp|Cam_Valpo_6-PEAS e Imp|3 mes|3 mes|8,86,E-10|2,14,E-10|4,99,E-10|9,98,E-09|2,83,E-11|
|AREA|SRC_77|Cam_Valpo_7-PEAS e Imp|267496|6372042|3 mes|247,03|9,37,E-10|2,27,E-10|5,27,E-10|1,06,E-08|2,99,E-11|
|AREA|SRC_78|Cam_Valpo_8-PEAS e Imp|267518|6372113|3 mes|294,47|7,86,E-10|1,90,E-10|4,42,E-10|8,85,E-09|2,51,E-11|
|AREA|SRC_79|Cam_Valpo_9-PEAS e Imp|267547|6372151|3 mes|187,43|1,23,E-09|2,99,E-10|6,95,E-10|1,39,E-08|3,94,E-11|
|AREA|SRC_80|Cam_Valpo_10-PEAS e Imp|267569|6372177|3 mes|137,02|1,69,E-09|4,09,E-10|9,51,E-10|1,90,E-08|5,39,E-11|
|AREA|SRC_81|Cam_Valpo_11-PEAS e Imp|267738|6372319|3 mes|879,83|2,63,E-10|6,36,E-11|1,48,E-10|2,96,E-09|8,39,E-12|
|AREA|SRC_82|Cam_Valpo_12-PEAS e Imp|267762|6372358|3 mes|186,57|1,24,E-09|3,00,E-10|6,98,E-10|1,40,E-08|3,96,E-11|
|AREA|SRC_83|Cam_Valpo_13-PEAS e Imp|267783|6372410|3 mes|224,51|1,03,E-09|2,49,E-10|5,80,E-10|1,16,E-08|3,29,E-11|
|AREA|SRC_84|Cam_Valpo_14-PEAS e Imp|267855|6372669|3 mes|1075,61|2,15,E-10|5,20,E-11|1,21,E-10|2,42,E-09|6,86,E-12|
|AREA|SRC_85|Cam_Valpo_15-PEAS e Imp|267848|6372720|3 mes|207,78|1,11,E-09|2,69,E-10|6,27,E-10|1,25,E-08|3,55,E-11|
|AREA|SRC_86|Cam_Valpo_16-PEAS e Imp|267715|6373066|3 mes|1484,08|1,56,E-10|3,77,E-11|8,78,E-11|1,76,E-09|4,98,E-12|
|AREA|SRC_87|Cam_Valpo_17-PEAS e Imp|267705|6373122|3 mes|225,43|1,03,E-09|2,48,E-10|5,78,E-10|1,16,E-08|3,28,E-11|
|AREA|SRC_88|Cam_Valpo_18-PEAS e Imp|267701|6373182|3 mes|241,22|9,59,E-10|2,32,E-10|5,40,E-10|1,08,E-08|3,06,E-11|
|AREA|SRC_89|Cam_Valpo_19-PEAS e Imp|267704|6373237|3 mes|217,96|1,06,E-09|2,57,E-10|5,98,E-10|1,20,E-08|3,39,E-11|
|AREA|SRC_90|Cam_Valpo_20-PEAS e Imp|267713|6373309|3 mes|291,26|7,94,E-10|1,92,E-10|4,47,E-10|8,95,E-09|2,54,E-11|
|AREA|SRC_91|Cam_Valpo_21-PEAS e Imp|267741|6373522|3 mes|860,16|2,69,E-10|6,51,E-11|1,51,E-10|3,03,E-09|8,58,E-12|
|AREA|SRC_92|Cam_Valpo_22-PEAS e Imp|267757|6373574|3 mes|213,85|1,08,E-09|2,62,E-10|6,09,E-10|1,22,E-08|3,45,E-11|
|AREA|SRC_93|Cam_Valpo_23-PEAS e Imp|267777|6373617|3 mes|187,32|1,24,E-09|2,99,E-10|6,95,E-10|1,39,E-08|3,94,E-11|
|AREA|SRC_94|Cam_Valpo_24-PEAS e Imp|267817|6373719|3 mes|441,14|5,25,E-10|1,27,E-10|2,95,E-10|5,91,E-09|1,67,E-11|
|AREA|SRC_95|Cam_Valpo_25-PEAS e Imp|267843|6373782|3 mes|272,58|8,49,E-10|2,05,E-10|4,78,E-10|9,56,E-09|2,71,E-11|
|AREA|SRC_96|Cam_Valpo_26-PEAS e Imp|267877|6373831|3 mes|236,03|9,80,E-10|2,37,E-10|5,52,E-10|1,10,E-08|3,13,E-11|
|AREA|SRC_97|Cam_Valpo_27-PEAS e Imp|267910|6373883|3 mes|246,12|9,40,E-10|2,27,E-10|5,29,E-10|1,06,E-08|3,00,E-11|
|AREA|SRC_98|Cam_Valpo_28-PEAS e Imp|268105|6374174|3 mes|1399,53|1,65,E-10|4,00,E-11|9,31,E-11|1,86,E-09|5,28,E-12|
|AREA|SRC_99|Cam_Valpo_29-PEAS e Imp|268274|6374430|3 mes|1228,07|1,88,E-10|4,56,E-11|1,06,E-10|2,12,E-09|6,01,E-12|
|AREA|SRC_100|Cam_Valpo_30-PEAS e Imp|268317|6374478|3 mes|254,35|9,10,E-10|2,20,E-10|5,12,E-10|1,02,E-08|2,90,E-11|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 139. Fuentes de Emisión - Escenario 5 parte 5

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 243 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>268347|[m]<br>6374502|[m]<br>6374502|[m2]<br>154,46|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_101|Cam_Valpo_31-PEAS e Imp|Cam_Valpo_31-PEAS e Imp|Cam_Valpo_31-PEAS e Imp|3 mes|3 mes|1,50,E-09|3,62,E-10|8,43,E-10|1,69,E-08|4,78,E-11|
|AREA|SRC_102|Cam_Valpo_32-PEAS e Imp|269602|6375295|3 mes|5935,56|3,90,E-11|9,43,E-12|2,19,E-11|4,39,E-10|1,24,E-12|
|AREA|SRC_103|Cam_Valpo_33-PEAS e Imp|270646|6375956|3 mes|4938,33|4,69,E-11|1,13,E-11|2,64,E-11|5,28,E-10|1,50,E-12|
|AREA|SRC_104|Cam_Valpo_34-PEAS e Imp|270700|6375970|3 mes|220,74|1,05,E-09|2,54,E-10|5,90,E-10|1,18,E-08|3,34,E-11|
|AREA|SRC_105|Cam_Valpo_35-PEAS e Imp|270759|6375972|3 mes|232,03|9,97,E-10|2,41,E-10|5,61,E-10|1,12,E-08|3,18,E-11|
|AREA|SRC_106|Cam_Valpo_36-PEAS e Imp|270817|6375960|3 mes|237,83|9,73,E-10|2,35,E-10|5,48,E-10|1,10,E-08|3,10,E-11|
|AREA|SRC_107|Cam_Valpo_37-PEAS e Imp|271210|6375788|3 mes|1710,95|1,35,E-10|3,27,E-11|7,61,E-11|1,52,E-09|4,32,E-12|
|AREA|SRC_108|Cam_Valpo_38-PEAS e Imp|271299|6375786|3 mes|362,06|6,39,E-10|1,55,E-10|3,60,E-10|7,20,E-09|2,04,E-11|
|AREA|SRC_109|Cam_Valpo_39-PEAS e Imp|271410|6375784|3 mes|444,09|5,21,E-10|1,26,E-10|2,93,E-10|5,87,E-09|1,66,E-11|
|AREA|SRC_110|Cam_Valpo_40-PEAS e Imp|271537|6375829|3 mes|539,94|4,29,E-10|1,04,E-10|2,41,E-10|4,83,E-09|1,37,E-11|
|AREA|SRC_111|Cam_Valpo_41-PEAS e Imp|271698|6375908|3 mes|717,64|3,22,E-10|7,80,E-11|1,81,E-10|3,63,E-09|1,03,E-11|
|AREA|SRC_112|Cam_Valpo_42-PEAS e Imp|271943|6376040|3 mes|1111,41|2,08,E-10|5,04,E-11|1,17,E-10|2,34,E-09|6,64,E-12|
|AREA|SRC_113|Cam_Valpo_43-PEAS e Imp|272216|6376245|3 mes|1365,82|1,69,E-10|4,10,E-11|9,54,E-11|1,91,E-09|5,41,E-12|
|AREA|SRC_114|Cam_Valpo_44-PEAS e Imp|272308|6376283|3 mes|396,81|5,83,E-10|1,41,E-10|3,28,E-10|6,57,E-09|1,86,E-11|
|AREA|SRC_115|Cam_Valpo_45-PEAS e Imp|272828|6376412|3 mes|2139,51|1,08,E-10|2,62,E-11|6,09,E-11|1,22,E-09|3,45,E-12|
|AREA|SRC_116|Cam_Valpo_46-PEAS e Imp|272961|6376463|3 mes|572,90|4,04,E-10|9,77,E-11|2,27,E-10|4,55,E-09|1,29,E-11|
|AREA|SRC_117|Cam_Valpo_47-PEAS e Imp|273101|6376548|3 mes|656,43|3,52,E-10|8,53,E-11|1,98,E-10|3,97,E-09|1,12,E-11|
|AREA|SRC_118|Cam_Valpo_48-PEAS e Imp|273683|6376890|3 mes|2699,98|8,57,E-11|2,07,E-11|4,82,E-11|9,65,E-10|2,73,E-12|
|AREA|SRC_119|Cam_Valpo_49-PEAS e Imp|273729|6376911|3 mes|198,66|1,16,E-09|2,82,E-10|6,56,E-10|1,31,E-08|3,72,E-11|
|AREA|SRC_120|Cam_Valpo_50-PEAS e Imp|273841|6376934|3 mes|455,50|5,08,E-10|1,23,E-10|2,86,E-10|5,72,E-09|1,62,E-11|
|AREA|SRC_121|Cam_Valpo_51-PEAS e Imp|273918|6376948|3 mes|314,84|7,35,E-10|1,78,E-10|4,14,E-10|8,28,E-09|2,35,E-11|
|AREA|SRC_122|Cam_Valpo_52-PEAS e Imp|273963|6376959|3 mes|182,29|1,27,E-09|3,07,E-10|7,14,E-10|1,43,E-08|4,05,E-11|
|AREA|SRC_123|Cam_Valpo_53-PEAS e Imp|274013|6376981|3 mes|220,22|1,05,E-09|2,54,E-10|5,91,E-10|1,18,E-08|3,35,E-11|
|AREA|SRC_124|Cam_Valpo_54-PEAS e Imp|274045|6377010|3 mes|175,74|1,32,E-09|3,19,E-10|7,41,E-10|1,48,E-08|4,20,E-11|
|AREA|SRC_125|Cam_Valpo_55-PEAS e Imp|274402|6377569|3 mes|2654,98|8,72,E-11|2,11,E-11|4,91,E-11|9,82,E-10|2,78,E-12|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 140. Fuentes de Emisión - Escenario 5 parte 6

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 244 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>274508|[m]<br>6377712|[m]<br>6377712|[m2]<br>712,20|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_126|Cam_Valpo_56-PEAS e Imp|Cam_Valpo_56-PEAS e Imp|Cam_Valpo_56-PEAS e Imp|3 mes|3 mes|3,25,E-10|7,86,E-11|1,83,E-10|3,66,E-09|1,04,E-11|
|AREA|SRC_127|Cam_Valpo_57-PEAS e Imp|274515|6377737|3 mes|105,54|2,19,E-09|5,30,E-10|1,23,E-09|2,47,E-08|7,00,E-11|
|AREA|SRC_128|Cam_Valpo_58-PEAS e Imp|274530|6377783|3 mes|190,85|1,21,E-09|2,93,E-10|6,82,E-10|1,37,E-08|3,87,E-11|
|AREA|SRC_129|Cam_Valpo_59-PEAS e Imp|274571|6378190|3 mes|1640,54|1,41,E-10|3,41,E-11|7,94,E-11|1,59,E-09|4,50,E-12|
|AREA|SRC_130|Cam_Valpo_60-PEAS e Imp|274512|6378662|3 mes|1902,24|1,22,E-10|2,94,E-11|6,85,E-11|1,37,E-09|3,88,E-12|
|AREA|SRC_131|Cam_Valpo_61-PEAS e Imp|274484|6378742|3 mes|339,36|6,82,E-10|1,65,E-10|3,84,E-10|7,68,E-09|2,18,E-11|
|AREA|SRC_132|Cam_Valpo_62-PEAS e Imp|274397|6378959|3 mes|934,88|2,48,E-10|5,99,E-11|1,39,E-10|2,79,E-09|7,90,E-12|
|AREA|SRC_133|Cam_Valpo_63-PEAS e Imp|274391|6379006|3 mes|189,58|1,22,E-09|2,95,E-10|6,87,E-10|1,37,E-08|3,89,E-11|
|AREA|SRC_134|Cam_Valpo_64-PEAS e Imp|274392|6379034|3 mes|109,49|2,11,E-09|5,11,E-10|1,19,E-09|2,38,E-08|6,74,E-11|
|AREA|SRC_135|Cam_Valpo_65-PEAS e Imp|274513|6379469|3 mes|1805,57|1,28,E-10|3,10,E-11|7,21,E-11|1,44,E-09|4,09,E-12|
|AREA|SRC_136|Cam_Valpo_66-PEAS e Imp|274514|6379510|3 mes|163,36|1,42,E-09|3,43,E-10|7,97,E-10|1,60,E-08|4,52,E-11|
|AREA|SRC_137|Cam_Valpo_67-PEAS e Imp|274503|6379560|3 mes|208,73|1,11,E-09|2,68,E-10|6,24,E-10|1,25,E-08|3,54,E-11|
|AREA|SRC_138|Cam_Valpo_68-PEAS e Imp|274488|6379623|3 mes|255,44|9,06,E-10|2,19,E-10|5,10,E-10|1,02,E-08|2,89,E-11|
|AREA|SRC_139|Cam_Valpo_69-PEAS e Imp|274426|6379798|3 mes|745,56|3,10,E-10|7,51,E-11|1,75,E-10|3,50,E-09|9,90,E-12|
|AREA|SRC_140|Cam_Valpo_70-PEAS e Imp|274386|6379897|3 mes|428,53|5,40,E-10|1,31,E-10|3,04,E-10|6,08,E-09|1,72,E-11|
|AREA|SRC_141|Cam_Valpo_71-PEAS e Imp|274352|6379981|3 mes|360,23|6,42,E-10|1,55,E-10|3,62,E-10|7,23,E-09|2,05,E-11|
|AREA|SRC_142|Cam_Valpo_72-PEAS e Imp|274336|6380041|3 mes|249,49|9,27,E-10|2,24,E-10|5,22,E-10|1,04,E-08|2,96,E-11|
|AREA|SRC_143|Cam_Valpo_73-PEAS e Imp|274333|6380099|3 mes|227,80|1,02,E-09|2,46,E-10|5,72,E-10|1,14,E-08|3,24,E-11|
|AREA|SRC_144|Cam_Valpo_74-PEAS e Imp|274332|6380163|3 mes|257,27|8,99,E-10|2,18,E-10|5,06,E-10|1,01,E-08|2,87,E-11|
|AREA|SRC_145|Cam_Valpo_75-PEAS e Imp|274329|6380546|3 mes|1530,44|1,51,E-10|3,66,E-11|8,51,E-11|1,70,E-09|4,82,E-12|
|AREA|SRC_146|Cam_Valpo_76-PEAS e Imp|274323|6380578|3 mes|130,55|1,77,E-09|4,29,E-10|9,98,E-10|2,00,E-08|5,66,E-11|
|AREA|SRC_147|Cam_Valpo_77-PEAS e Imp|274308|6380608|3 mes|138,17|1,67,E-09|4,05,E-10|9,43,E-10|1,89,E-08|5,34,E-11|
|AREA|SRC_148|Cam_Valpo_78-PEAS e Imp|274078|6381086|3 mes|2120,50|1,09,E-10|2,64,E-11|6,14,E-11|1,23,E-09|3,48,E-12|
|AREA|SRC_149|Cam_Valpo_79-PEAS e Imp|274036|6381146|3 mes|292,96|7,90,E-10|1,91,E-10|4,45,E-10|8,90,E-09|2,52,E-11|
|AREA|SRC_150|Cam_Valpo_80-PEAS e Imp|273997|6381192|3 mes|242,71|9,53,E-10|2,31,E-10|5,37,E-10|1,07,E-08|3,04,E-11|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 141. Fuentes de Emisión - Escenario 5 parte 7

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 245 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>273945|[m]<br>6381212|[m]<br>6381212|[m2]<br>225,25|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_151|Cam_Valpo_81-PEAS e Imp|Cam_Valpo_81-PEAS e Imp|Cam_Valpo_81-PEAS e Imp|3 mes|3 mes|1,03,E-09|2,49,E-10|5,78,E-10|1,16,E-08|3,28,E-11|
|AREA|SRC_152|Cam_Valpo_82-PEAS e Imp|273863|6381235|3 mes|340,59|6,79,E-10|1,64,E-10|3,82,E-10|7,65,E-09|2,17,E-11|
|AREA|SRC_153|Cam_Valpo_83-PEAS e Imp|273527|6381309|3 mes|1376,67|1,68,E-10|4,07,E-11|9,46,E-11|1,89,E-09|5,36,E-12|
|AREA|SRC_154|Cam_Valpo_84-PEAS e Imp|273488|6381317|3 mes|158,83|1,46,E-09|3,52,E-10|8,20,E-10|1,64,E-08|4,65,E-11|
|AREA|SRC_155|Cam_Valpo_85-PEAS e Imp|273437|6381311|3 mes|210,61|1,10,E-09|2,66,E-10|6,18,E-10|1,24,E-08|3,51,E-11|
|AREA|SRC_156|Cam_Valpo_86-PEAS e Imp|273400|6381306|3 mes|148,75|1,56,E-09|3,76,E-10|8,76,E-10|1,75,E-08|4,96,E-11|
|AREA|SRC_157|Cam_Valpo_87-PEAS e Imp|273330|6381278|3 mes|302,02|7,66,E-10|1,85,E-10|4,31,E-10|8,63,E-09|2,44,E-11|
|AREA|SRC_158|Cam_Valpo_88-PEAS e Imp|273269|6381275|3 mes|240,32|9,63,E-10|2,33,E-10|5,42,E-10|1,08,E-08|3,07,E-11|
|AREA|SRC_159|Cam_Valpo_89-PEAS e Imp|273210|6381284|3 mes|238,69|9,69,E-10|2,35,E-10|5,46,E-10|1,09,E-08|3,09,E-11|
|AREA|SRC_160|Cam_Valpo_90-PEAS e Imp|273140|6381307|3 mes|291,89|7,93,E-10|1,92,E-10|4,46,E-10|8,93,E-09|2,53,E-11|
|AREA|SRC_161|Cam_Valpo_91-PEAS e Imp|273026|6381364|3 mes|510,61|4,53,E-10|1,10,E-10|2,55,E-10|5,10,E-09|1,45,E-11|
|AREA|SRC_162|Cam_Valpo_92-PEAS e Imp|272787|6381471|3 mes|1046,47|2,21,E-10|5,35,E-11|1,24,E-10|2,49,E-09|7,06,E-12|
|AREA|SRC_163|Cam_Valpo_93-PEAS e Imp|272625|6381553|3 mes|726,81|3,18,E-10|7,70,E-11|1,79,E-10|3,59,E-09|1,02,E-11|
|AREA|SRC_164|Cam_Valpo_94-PEAS e Imp|272586|6381587|3 mes|205,87|1,12,E-09|2,72,E-10|6,33,E-10|1,27,E-08|3,59,E-11|
|AREA|SRC_165|Cam_Valpo_95-PEAS e Imp|272567|6381621|3 mes|150,25|1,54,E-09|3,73,E-10|8,67,E-10|1,73,E-08|4,91,E-11|
|AREA|SRC_166|Cam_Valpo_96-PEAS e Imp|272558|6381659|3 mes|154,59|1,50,E-09|3,62,E-10|8,43,E-10|1,69,E-08|4,78,E-11|
|AREA|SRC_167|Cam_Valpo_97-PEAS e Imp|272513|6381931|3 mes|1103,20|2,10,E-10|5,07,E-11|1,18,E-10|2,36,E-09|6,69,E-12|
|AREA|SRC_168|Cam_Valpo_98-PEAS e Imp|272500|6382030|3 mes|398,37|5,81,E-10|1,41,E-10|3,27,E-10|6,54,E-09|1,85,E-11|
|AREA|SRC_169|Cam_Valpo_99-PEAS e Imp|272492|6382086|3 mes|223,87|1,03,E-09|2,50,E-10|5,82,E-10|1,16,E-08|3,30,E-11|
|AREA|SRC_170|Cam_Valpo_100-PEAS e Imp|272491|6382127|3 mes|164,32|1,41,E-09|3,41,E-10|7,93,E-10|1,59,E-08|4,49,E-11|
|AREA|SRC_171|Cam_Valpo_101-PEAS e Imp|272506|6382188|3 mes|247,33|9,36,E-10|2,26,E-10|5,27,E-10|1,05,E-08|2,99,E-11|
|AREA|SRC_172|Cam_Valpo_102-PEAS e Imp|272660|6383439|3 mes|5043,31|4,59,E-11|1,11,E-11|2,58,E-11|5,17,E-10|1,46,E-12|
|AREA|SRC_173|Cam_Valpo_103-PEAS e Imp|272630|6384559|3 mes|4478,91|5,17,E-11|1,25,E-11|2,91,E-11|5,82,E-10|1,65,E-12|
|AREA|SRC_174|Cam_Valpo_104-PEAS e Imp|272626|6385227|3 mes|2671,08|8,66,E-11|2,10,E-11|4,88,E-11|9,76,E-10|2,76,E-12|
|AREA|SRC_175|Cam_Valpo_105-PEAS e Imp|272602|6386454|3 mes|4905,80|4,72,E-11|1,14,E-11|2,65,E-11|5,31,E-10|1,51,E-12|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 142. Fuentes de Emisión - Escenario 5 parte 8

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 246 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>272609|[m]<br>6386527|[m]<br>6386527|[m2]<br>292,53|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_176|Cam_Valpo_106-PEAS e Imp|Cam_Valpo_106-PEAS e Imp|Cam_Valpo_106-PEAS e Imp|3 mes|3 mes|7,91,E-10|1,91,E-10|4,45,E-10|8,91,E-09|2,52,E-11|
|AREA|SRC_177|Cam_Valpo_107-PEAS e Imp|272650|6386615|3 mes|384,69|6,01,E-10|1,46,E-10|3,39,E-10|6,77,E-09|1,92,E-11|
|AREA|SRC_178|Cam_Valpo_108-PEAS e Imp|272755|6386705|3 mes|550,00|4,21,E-10|1,02,E-10|2,37,E-10|4,74,E-09|1,34,E-11|
|AREA|SRC_179|Cam_Valpo_109-PEAS e Imp|272846|6386776|3 mes|460,85|5,02,E-10|1,21,E-10|2,83,E-10|5,66,E-09|1,60,E-11|
|AREA|SRC_180|Cam_Valpo_110-PEAS e Imp|272918|6386821|3 mes|338,79|6,83,E-10|1,65,E-10|3,84,E-10|7,69,E-09|2,18,E-11|
|AREA|SRC_181|Cam_Valpo_111-PEAS e Imp|272959|6386856|3 mes|215,71|1,07,E-09|2,60,E-10|6,04,E-10|1,21,E-08|3,42,E-11|
|AREA|SRC_182|Cam_Valpo_112-PEAS e Imp|272979|6386909|3 mes|229,32|1,01,E-09|2,44,E-10|5,68,E-10|1,14,E-08|3,22,E-11|
|AREA|SRC_183|Cam_Valpo_113-PEAS e Imp|272982|6386950|3 mes|168,20|1,38,E-09|3,33,E-10|7,74,E-10|1,55,E-08|4,39,E-11|
|AREA|SRC_184|Cam_Valpo_114-PEAS e Imp|272974|6387033|3 mes|334,56|6,92,E-10|1,67,E-10|3,89,E-10|7,79,E-09|2,21,E-11|
|AREA|SRC_185|Cam_Valpo_115-PEAS e Imp|272969|6387289|3 mes|1021,26|2,27,E-10|5,48,E-11|1,28,E-10|2,55,E-09|7,23,E-12|
|AREA|SRC_186|Cam_Valpo_116-PEAS e Imp|272950|6387316|3 mes|135,86|1,70,E-09|4,12,E-10|9,59,E-10|1,92,E-08|5,43,E-11|
|AREA|SRC_187|Cam_Valpo_117-PEAS e Imp|272918|6387332|3 mes|150,62|1,54,E-09|3,72,E-10|8,65,E-10|1,73,E-08|4,90,E-11|
|AREA|SRC_188|Cam_Valpo_118-PEAS e Imp|272871|6387328|3 mes|193,11|1,20,E-09|2,90,E-10|6,74,E-10|1,35,E-08|3,82,E-11|
|AREA|SRC_189|Cam_Valpo_119-PEAS e Imp|272818|6387319|3 mes|214,82|1,08,E-09|2,61,E-10|6,06,E-10|1,21,E-08|3,44,E-11|
|AREA|SRC_190|Cam_Valpo_120-PEAS e Imp|272669|6387324|3 mes|593,51|3,90,E-10|9,43,E-11|2,19,E-10|4,39,E-09|1,24,E-11|
|AREA|SRC_191|Cam_Valpo_121-PEAS e Imp|272536|6387380|3 mes|574,11|4,03,E-10|9,75,E-11|2,27,E-10|4,54,E-09|1,29,E-11|
|AREA|SRC_192|Cam_Valpo_122-PEAS e Imp|272406|6387475|3 mes|642,85|3,60,E-10|8,71,E-11|2,03,E-10|4,05,E-09|1,15,E-11|
|AREA|SRC_193|Cam_Valpo_123-PEAS e Imp|272321|6387544|3 mes|438,86|5,27,E-10|1,28,E-10|2,97,E-10|5,94,E-09|1,68,E-11|
|AREA|SRC_194|Cam_Valpo_124-PEAS e Imp|272252|6387605|3 mes|366,01|6,32,E-10|1,53,E-10|3,56,E-10|7,12,E-09|2,02,E-11|
|AREA|SRC_195|Cam_Valpo_125-PEAS e Imp|272138|6387749|3 mes|733,97|3,15,E-10|7,63,E-11|1,77,E-10|3,55,E-09|1,01,E-11|
|AREA|SRC_196|Cam_Valpo_126-PEAS e Imp|272059|6387890|3 mes|645,70|3,58,E-10|8,67,E-11|2,02,E-10|4,04,E-09|1,14,E-11|
|AREA|SRC_197|Cam_Valpo_127-PEAS e Imp|272019|6388008|3 mes|494,29|4,68,E-10|1,13,E-10|2,63,E-10|5,27,E-09|1,49,E-11|
|AREA|SRC_198|Cam_Valpo_128-PEAS e Imp|272005|6388086|3 mes|318,17|7,27,E-10|1,76,E-10|4,09,E-10|8,19,E-09|2,32,E-11|
|AREA|SRC_199|Cam_Valpo_129-PEAS e Imp|272005|6388171|3 mes|338,40|6,84,E-10|1,65,E-10|3,85,E-10|7,70,E-09|2,18,E-11|
|AREA|SRC_200|Cam_Valpo_130-PEAS e Imp|272018|6388207|3 mes|149,40|1,55,E-09|3,75,E-10|8,72,E-10|1,74,E-08|4,94,E-11|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 143. Fuentes de Emisión - Escenario 5 parte 9

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 247 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>272053|[m]<br>6388222|[m]<br>6388222|[m2]<br>144,57|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_201|Cam_Valpo_131-PEAS e Imp|Cam_Valpo_131-PEAS e Imp|Cam_Valpo_131-PEAS e Imp|3 mes|3 mes|1,60,E-09|3,87,E-10|9,01,E-10|1,80,E-08|5,11,E-11|
|AREA|SRC_202|Cam_Valpo_132-PEAS e Imp|272113|6388260|3 mes|286,19|8,09,E-10|1,96,E-10|4,55,E-10|9,11,E-09|2,58,E-11|
|AREA|SRC_203|Cam_Valpo_133-PEAS e Imp|272165|6388289|3 mes|236,50|9,78,E-10|2,37,E-10|5,51,E-10|1,10,E-08|3,12,E-11|
|AREA|SRC_204|Cam_Valpo_134-PEAS e Imp|272170|6388313|3 mes|103,04|2,25,E-09|5,43,E-10|1,26,E-09|2,53,E-08|7,17,E-11|
|AREA|SRC_205|Cam_Valpo_135-PEAS e Imp|272160|6388355|3 mes|178,67|1,30,E-09|3,13,E-10|7,29,E-10|1,46,E-08|4,13,E-11|
|AREA|SRC_206|Cam_Valpo_136-PEAS e Imp|272116|6388384|3 mes|213,17|1,09,E-09|2,63,E-10|6,11,E-10|1,22,E-08|3,46,E-11|
|AREA|SRC_207|Cam_Valpo_137-PEAS e Imp|271990|6388473|3 mes|618,26|3,74,E-10|9,05,E-11|2,11,E-10|4,22,E-09|1,19,E-11|
|AREA|SRC_208|Cam_Valpo_138-PEAS e Imp|271909|6388570|3 mes|502,24|4,61,E-10|1,11,E-10|2,59,E-10|5,19,E-09|1,47,E-11|
|AREA|SRC_209|Cam_Valpo_139-PEAS e Imp|271887|6388631|3 mes|257,67|8,98,E-10|2,17,E-10|5,05,E-10|1,01,E-08|2,87,E-11|
|AREA|SRC_210|Cam_Valpo_140-PEAS e Imp|271869|6388710|3 mes|324,57|7,13,E-10|1,72,E-10|4,01,E-10|8,03,E-09|2,27,E-11|
|AREA|SRC_211|Cam_Valpo_141-PEAS e Imp|271879|6388778|3 mes|270,72|8,55,E-10|2,07,E-10|4,81,E-10|9,63,E-09|2,73,E-11|
|AREA|SRC_212|Cam_Valpo_142-PEAS e Imp|271889|6388831|3 mes|215,81|1,07,E-09|2,59,E-10|6,04,E-10|1,21,E-08|3,42,E-11|
|AREA|SRC_213|Cam_Valpo_143-PEAS e Imp|271888|6388910|3 mes|317,54|7,29,E-10|1,76,E-10|4,10,E-10|8,21,E-09|2,33,E-11|
|AREA|SRC_214|Cam_Valpo_144-PEAS e Imp|271765|6389249|3 mes|1443,83|1,60,E-10|3,88,E-11|9,02,E-11|1,81,E-09|5,11,E-12|
|AREA|SRC_215|Cam_Valpo_145-PEAS e Imp|271745|6389323|3 mes|308,68|7,50,E-10|1,81,E-10|4,22,E-10|8,44,E-09|2,39,E-11|
|AREA|SRC_216|Cam_Valpo_146-PEAS e Imp|271746|6389404|3 mes|321,13|7,21,E-10|1,74,E-10|4,06,E-10|8,12,E-09|2,30,E-11|
|AREA|SRC_217|Cam_Valpo_147-PEAS e Imp|271745|6389713|3 mes|1235,33|1,87,E-10|4,53,E-11|1,05,E-10|2,11,E-09|5,98,E-12|
|AREA|SRC_218|Cam_Valpo_148-PEAS e Imp|271729|6389779|3 mes|274,74|8,42,E-10|2,04,E-10|4,74,E-10|9,49,E-09|2,69,E-11|
|AREA|SRC_219|Cam_Valpo_149-PEAS e Imp|271405|6390771|3 mes|4169,69|5,55,E-11|1,34,E-11|3,12,E-11|6,25,E-10|1,77,E-12|
|AREA|SRC_220|Cam_Valpo_150-PEAS e Imp|271408|6390852|3 mes|324,07|7,14,E-10|1,73,E-10|4,02,E-10|8,04,E-09|2,28,E-11|
|AREA|SRC_221|Cam_Valpo_151-PEAS e Imp|271425|6390918|3 mes|269,76|8,58,E-10|2,08,E-10|4,83,E-10|9,66,E-09|2,74,E-11|
|AREA|SRC_222|Cam_Valpo_152-PEAS e Imp|271595|6391444|3 mes|2210,20|1,05,E-10|2,53,E-11|5,89,E-11|1,18,E-09|3,34,E-12|
|AREA|SRC_223|Cam_Valpo_153-PEAS e Imp|271601|6391518|3 mes|297,07|7,79,E-10|1,88,E-10|4,38,E-10|8,77,E-09|2,49,E-11|
|AREA|SRC_224|Cam_Valpo_154-PEAS e Imp|271583|6391599|3 mes|334,56|6,92,E-10|1,67,E-10|3,89,E-10|7,79,E-09|2,21,E-11|
|AREA|SRC_225|Cam_Valpo_155-PEAS e Imp|271490|6391665|3 mes|462,29|5,01,E-10|1,21,E-10|2,82,E-10|5,64,E-09|1,60,E-11|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 144. Fuentes de Emisión - Escenario 5 parte 10

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 248 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>271388|[m]<br>6391779|[m]<br>6391779|[m2]<br>610,49|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_226|Cam_Valpo_156-PEAS e Imp|Cam_Valpo_156-PEAS e Imp|Cam_Valpo_156-PEAS e Imp|3 mes|3 mes|3,79,E-10|9,17,E-11|2,13,E-10|4,27,E-09|1,21,E-11|
|AREA|SRC_227|Cam_Valpo_157-PEAS e Imp|271303|6391969|3 mes|829,95|2,79,E-10|6,75,E-11|1,57,E-10|3,14,E-09|8,90,E-12|
|AREA|SRC_228|Cam_Valpo_158-PEAS e Imp|271249|6392048|3 mes|385,48|6,00,E-10|1,45,E-10|3,38,E-10|6,76,E-09|1,92,E-11|
|AREA|SRC_229|Cam_Valpo_159-PEAS e Imp|271095|6392199|3 mes|863,11|2,68,E-10|6,49,E-11|1,51,E-10|3,02,E-09|8,55,E-12|
|AREA|SRC_230|Cam_Valpo_160-PEAS e Imp|271003|6392357|3 mes|727,41|3,18,E-10|7,70,E-11|1,79,E-10|3,58,E-09|1,02,E-11|
|AREA|SRC_231|Cam_Valpo_161-PEAS e Imp|270864|6392618|3 mes|1181,67|1,96,E-10|4,74,E-11|1,10,E-10|2,21,E-09|6,25,E-12|
|AREA|SRC_232|Cam_Valpo_162-PEAS e Imp|270665|6392901|3 mes|1386,67|1,67,E-10|4,04,E-11|9,39,E-11|1,88,E-09|5,32,E-12|
|AREA|SRC_233|Cam_Valpo_163-PEAS e Imp|270570|6393060|3 mes|739,81|3,13,E-10|7,57,E-11|1,76,E-10|3,52,E-09|9,98,E-12|
|AREA|SRC_234|Cam_Valpo_164-PEAS e Imp|270535|6393162|3 mes|427,94|5,41,E-10|1,31,E-10|3,04,E-10|6,09,E-09|1,73,E-11|
|AREA|SRC_235|Cam_Valpo_165-PEAS e Imp|270408|6393157|3 mes|516,16|4,48,E-10|1,08,E-10|2,52,E-10|5,05,E-09|1,43,E-11|
|AREA|SRC_236|Cam_Valpo_166-PEAS e Imp|270322|6393156|3 mes|344,11|6,72,E-10|1,63,E-10|3,78,E-10|7,57,E-09|2,15,E-11|
|AREA|SRC_237|Cam_Valpo_167-PEAS e Imp|270198|6393225|3 mes|562,03|4,12,E-10|9,96,E-11|2,32,E-10|4,64,E-09|1,31,E-11|
|AREA|SRC_238|Cam_Valpo_168-PEAS e Imp|270084|6393222|3 mes|461,57|5,01,E-10|1,21,E-10|2,82,E-10|5,65,E-09|1,60,E-11|
|AREA|SRC_239|Cam_Valpo_169-PEAS e Imp|270014|6393114|3 mes|520,05|4,45,E-10|1,08,E-10|2,50,E-10|5,01,E-09|1,42,E-11|
|AREA|SRC_240|Cam_Valpo_170-PEAS e Imp|269944|6393026|3 mes|448,19|5,16,E-10|1,25,E-10|2,91,E-10|5,81,E-09|1,65,E-11|
|AREA|SRC_241|Cam_Valpo_171-PEAS e Imp|269831|6392981|3 mes|484,35|4,78,E-10|1,16,E-10|2,69,E-10|5,38,E-09|1,52,E-11|
|AREA|SRC_242|Cam_Valpo_172-PEAS e Imp|269702|6392966|3 mes|516,99|4,48,E-10|1,08,E-10|2,52,E-10|5,04,E-09|1,43,E-11|
|AREA|SRC_243|Cam_Valpo_173-PEAS e Imp|269506|6393084|3 mes|906,73|2,55,E-10|6,17,E-11|1,44,E-10|2,87,E-09|8,14,E-12|
|AREA|SRC_244|Cam_Valpo_174-PEAS e Imp|269407|6393106|3 mes|410,62|5,64,E-10|1,36,E-10|3,17,E-10|6,35,E-09|1,80,E-11|
|AREA|SRC_245|Cam_Valpo_175-PEAS e Imp|269355|6393219|3 mes|493,13|4,69,E-10|1,14,E-10|2,64,E-10|5,28,E-09|1,50,E-11|
|AREA|SRC_246|Cam_Valpo_176-PEAS e Imp|269450|6393436|3 mes|939,57|2,46,E-10|5,96,E-11|1,39,E-10|2,77,E-09|7,86,E-12|
|AREA|SRC_247|Cam_Valpo_177-PEAS e Imp|269537|6393768|3 mes|1375,49|1,68,E-10|4,07,E-11|9,47,E-11|1,89,E-09|5,37,E-12|
|AREA|SRC_248|Cam_Valpo_178-PEAS e Imp|269541|6393876|3 mes|433,16|5,34,E-10|1,29,E-10|3,01,E-10|6,02,E-09|1,70,E-11|
|AREA|SRC_249|Cam_Valpo_179-PEAS e Imp|269514|6393952|3 mes|327,49|7,07,E-10|1,71,E-10|3,98,E-10|7,96,E-09|2,25,E-11|
|AREA|SRC_250|Cam_Valpo_180-PEAS e Imp|269461|6394006|3 mes|302,03|7,66,E-10|1,85,E-10|4,31,E-10|8,63,E-09|2,44,E-11|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 145. Fuentes de Emisión - Escenario 5 parte 11

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 249 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>269456|[m]<br>6394087|[m]<br>6394087|[m2]<br>317,54|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_251|Cam_Valpo_181-PEAS e Imp|Cam_Valpo_181-PEAS e Imp|Cam_Valpo_181-PEAS e Imp|3 mes|3 mes|7,29,E-10|1,76,E-10|4,10,E-10|8,21,E-09|2,33,E-11|
|AREA|SRC_252|Cam_Valpo_182-PEAS e Imp|269494|6394169|3 mes|358,94|6,45,E-10|1,56,E-10|3,63,E-10|7,26,E-09|2,06,E-11|
|AREA|SRC_253|Cam_Valpo_183-PEAS e Imp|269580|6394296|3 mes|611,99|3,78,E-10|9,15,E-11|2,13,E-10|4,26,E-09|1,21,E-11|
|AREA|SRC_254|Cam_Valpo_184-PEAS e Imp|269614|6394394|3 mes|416,61|5,55,E-10|1,34,E-10|3,13,E-10|6,26,E-09|1,77,E-11|
|AREA|SRC_255|Cam_Valpo_185-PEAS e Imp|269617|6394492|3 mes|396,57|5,83,E-10|1,41,E-10|3,28,E-10|6,57,E-09|1,86,E-11|
|AREA|SRC_256|Cam_Valpo_186-PEAS e Imp|269532|6394634|3 mes|664,18|3,48,E-10|8,43,E-11|1,96,E-10|3,92,E-09|1,11,E-11|
|AREA|SRC_257|Cam_Valpo_187-PEAS e Imp|269478|6394752|3 mes|518,20|4,47,E-10|1,08,E-10|2,51,E-10|5,03,E-09|1,42,E-11|
|AREA|SRC_258|Cam_Valpo_188-PEAS e Imp|269437|6394881|3 mes|540,93|4,28,E-10|1,03,E-10|2,41,E-10|4,82,E-09|1,36,E-11|
|AREA|SRC_259|Cam_Valpo_189-PEAS e Imp|269448|6395002|3 mes|483,46|4,79,E-10|1,16,E-10|2,69,E-10|5,39,E-09|1,53,E-11|
|AREA|SRC_260|Cam_Valpo_190-PEAS e Imp|269465|6395049|3 mes|197,82|1,17,E-09|2,83,E-10|6,58,E-10|1,32,E-08|3,73,E-11|
|AREA|SRC_261|Cam_Valpo_191-PEAS e Imp|269701|6395188|3 mes|1088,66|2,13,E-10|5,14,E-11|1,20,E-10|2,39,E-09|6,78,E-12|
|AREA|SRC_262|Cam_Valpo_192-PEAS e Imp|269737|6395244|3 mes|269,38|8,59,E-10|2,08,E-10|4,84,E-10|9,67,E-09|2,74,E-11|
|AREA|SRC_263|Cam_Valpo_193-PEAS e Imp|269748|6395318|3 mes|301,88|7,66,E-10|1,85,E-10|4,31,E-10|8,63,E-09|2,45,E-11|
|AREA|SRC_264|Cam_Valpo_194-PEAS e Imp|269734|6395473|3 mes|624,02|3,71,E-10|8,97,E-11|2,09,E-10|4,18,E-09|1,18,E-11|
|AREA|SRC_265|Cam_Valpo_195-PEAS e Imp|269791|6395575|3 mes|462,91|5,00,E-10|1,21,E-10|2,81,E-10|5,63,E-09|1,60,E-11|
|AREA|SRC_266|Cam_Valpo_196-PEAS e Imp|269918|6395634|3 mes|557,57|4,15,E-10|1,00,E-10|2,34,E-10|4,67,E-09|1,32,E-11|
|AREA|SRC_267|Cam_Valpo_197-PEAS e Imp|269951|6395703|3 mes|311,66|7,42,E-10|1,80,E-10|4,18,E-10|8,36,E-09|2,37,E-11|
|AREA|SRC_268|Cam_Valpo_198-PEAS e Imp|269926|6395767|3 mes|277,87|8,33,E-10|2,01,E-10|4,69,E-10|9,38,E-09|2,66,E-11|
|AREA|SRC_269|Cam_Valpo_199-PEAS e Imp|269853|6395812|3 mes|348,28|6,64,E-10|1,61,E-10|3,74,E-10|7,48,E-09|2,12,E-11|
|AREA|SRC_270|Cam_Valpo_200-PEAS e Imp|269732|6395847|3 mes|504,67|4,58,E-10|1,11,E-10|2,58,E-10|5,16,E-09|1,46,E-11|
|AREA|SRC_271|Cam_Valpo_201-PEAS e Imp|269688|6395928|3 mes|365,46|6,33,E-10|1,53,E-10|3,56,E-10|7,13,E-09|2,02,E-11|
|AREA|SRC_272|Cam_Valpo_202-PEAS e Imp|269717|6396047|3 mes|484,68|4,77,E-10|1,16,E-10|2,69,E-10|5,38,E-09|1,52,E-11|
|AREA|SRC_273|Cam_Valpo_203-PEAS e Imp|269712|6396106|3 mes|237,49|9,74,E-10|2,36,E-10|5,48,E-10|1,10,E-08|3,11,E-11|
|AREA|SRC_274|Cam_Valpo_204-PEAS e Imp|269657|6396143|3 mes|271,48|8,52,E-10|2,06,E-10|4,80,E-10|9,60,E-09|2,72,E-11|
|AREA|SRC_275|Cam_Valpo_205-PEAS e Imp|269580|6396120|3 mes|326,46|7,09,E-10|1,71,E-10|3,99,E-10|7,98,E-09|2,26,E-11|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 146. Fuentes de Emisión - Escenario 5 parte 12

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 250 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>269501|[m]<br>6396070|[m]<br>6396070|[m2]<br>376,20|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_276|Cam_Valpo_206-PEAS e Imp|Cam_Valpo_206-PEAS e Imp|Cam_Valpo_206-PEAS e Imp|3 mes|3 mes|6,15,E-10|1,49,E-10|3,46,E-10|6,93,E-09|1,96,E-11|
|AREA|SRC_277|Cam_Valpo_207-PEAS e Imp|269359|6396026|3 mes|593,54|3,90,E-10|9,43,E-11|2,19,E-10|4,39,E-09|1,24,E-11|
|AREA|SRC_278|Cam_Valpo_208-PEAS e Imp|269272|6396023|3 mes|343,48|6,74,E-10|1,63,E-10|3,79,E-10|7,59,E-09|2,15,E-11|
|AREA|SRC_279|Cam_Valpo_209-PEAS e Imp|269222|6396073|3 mes|275,81|8,39,E-10|2,03,E-10|4,72,E-10|9,45,E-09|2,68,E-11|
|AREA|SRC_280|Cam_Valpo_210-PEAS e Imp|269210|6396185|3 mes|446,25|5,19,E-10|1,25,E-10|2,92,E-10|5,84,E-09|1,65,E-11|
|AREA|SRC_281|Cam_Valpo_211-PEAS e Imp|269167|6396232|3 mes|255,46|9,06,E-10|2,19,E-10|5,10,E-10|1,02,E-08|2,89,E-11|
|AREA|SRC_282|Cam_Valpo_212-PEAS e Imp|269082|6396226|3 mes|349,58|6,62,E-10|1,60,E-10|3,73,E-10|7,46,E-09|2,11,E-11|
|AREA|SRC_283|Cam_Valpo_213-PEAS e Imp|268998|6396240|3 mes|335,54|6,90,E-10|1,67,E-10|3,88,E-10|7,77,E-09|2,20,E-11|
|AREA|SRC_284|Cam_Valpo_214-PEAS e Imp|268894|6396300|3 mes|480,09|4,82,E-10|1,17,E-10|2,71,E-10|5,43,E-09|1,54,E-11|
|AREA|SRC_285|Cam_Valpo_215-PEAS e Imp|268805|6396381|3 mes|477,49|4,85,E-10|1,17,E-10|2,73,E-10|5,46,E-09|1,55,E-11|
|AREA|SRC_286|Cam_Valpo_216-PEAS e Imp|268734|6396481|3 mes|489,34|4,73,E-10|1,14,E-10|2,66,E-10|5,33,E-09|1,51,E-11|
|AREA|SRC_287|Cam_Valpo_217-PEAS e Imp|268692|6396569|3 mes|388,32|5,96,E-10|1,44,E-10|3,35,E-10|6,71,E-09|1,90,E-11|
|AREA|SRC_288|Cam_Valpo_218-PEAS e Imp|268614|6396686|3 mes|563,68|4,10,E-10|9,93,E-11|2,31,E-10|4,62,E-09|1,31,E-11|
|AREA|SRC_289|Cam_Valpo_219-PEAS e Imp|268551|6396751|3 mes|365,13|6,34,E-10|1,53,E-10|3,57,E-10|7,14,E-09|2,02,E-11|
|AREA|SRC_290|Cam_Valpo_220-PEAS e Imp|268525|6396834|3 mes|342,75|6,75,E-10|1,63,E-10|3,80,E-10|7,60,E-09|2,15,E-11|
|AREA|SRC_291|Cam_Valpo_221-PEAS e Imp|268521|6396918|3 mes|335,20|6,90,E-10|1,67,E-10|3,89,E-10|7,78,E-09|2,20,E-11|
|AREA|SRC_292|Cam_Valpo_222-PEAS e Imp|268510|6396996|3 mes|312,17|7,41,E-10|1,79,E-10|4,17,E-10|8,35,E-09|2,37,E-11|
|AREA|SRC_293|Cam_Valpo_223-PEAS e Imp|268441|6397095|3 mes|486,78|4,75,E-10|1,15,E-10|2,68,E-10|5,35,E-09|1,52,E-11|
|AREA|SRC_294|Cam_Valpo_224-PEAS e Imp|268352|6397195|3 mes|537,81|4,30,E-10|1,04,E-10|2,42,E-10|4,85,E-09|1,37,E-11|
|AREA|SRC_295|Cam_Valpo_225-PEAS e Imp|268295|6397296|3 mes|460,41|5,03,E-10|1,22,E-10|2,83,E-10|5,66,E-09|1,60,E-11|
|AREA|SRC_296|Cam_Valpo_226-PEAS e Imp|268265|6397370|3 mes|319,00|7,25,E-10|1,75,E-10|4,08,E-10|8,17,E-09|2,31,E-11|
|AREA|SRC_297|Cam_Valpo_227-PEAS e Imp|268236|6397470|3 mes|414,51|5,58,E-10|1,35,E-10|3,14,E-10|6,29,E-09|1,78,E-11|
|AREA|SRC_298|Cam_Valpo_228-PEAS e Imp|268225|6397539|3 mes|278,02|8,32,E-10|2,01,E-10|4,68,E-10|9,37,E-09|2,66,E-11|
|AREA|SRC_299|Cam_Valpo_229-PEAS e Imp|268212|6397650|3 mes|446,47|5,18,E-10|1,25,E-10|2,92,E-10|5,84,E-09|1,65,E-11|
|AREA|SRC_300|Cam_Valpo_230-PEAS e Imp|268292|6397691|3 mes|352,90|6,56,E-10|1,59,E-10|3,69,E-10|7,38,E-09|2,09,E-11|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 147. Fuentes de Emisión - Escenario 5 parte 13

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 251 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>268324|[m]<br>6397741|[m]<br>6397741|[m2]<br>244,09|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_301|Cam_Valpo_231-PEAS e Imp|Cam_Valpo_231-PEAS e Imp|Cam_Valpo_231-PEAS e Imp|3 mes|3 mes|9,48,E-10|2,29,E-10|5,34,E-10|1,07,E-08|3,02,E-11|
|AREA|SRC_302|Cam_Valpo_232-PEAS e Imp|268344|6397809|3 mes|284,52|8,13,E-10|1,97,E-10|4,58,E-10|9,16,E-09|2,60,E-11|
|AREA|SRC_303|Cam_Valpo_233-PEAS e Imp|268317|6397871|3 mes|277,40|8,34,E-10|2,02,E-10|4,70,E-10|9,39,E-09|2,66,E-11|
|AREA|SRC_304|Cam_Valpo_234-PEAS e Imp|268289|6397931|3 mes|263,44|8,78,E-10|2,12,E-10|4,94,E-10|9,89,E-09|2,80,E-11|
|AREA|SRC_305|Cam_Valpo_235-PEAS e Imp|268281|6397993|3 mes|246,21|9,40,E-10|2,27,E-10|5,29,E-10|1,06,E-08|3,00,E-11|
|AREA|SRC_306|Cam_Valpo_236-PEAS e Imp|268325|6398057|3 mes|307,11|7,53,E-10|1,82,E-10|4,24,E-10|8,49,E-09|2,40,E-11|
|AREA|SRC_307|Cam_Valpo_237-PEAS e Imp|268339|6398092|3 mes|154,12|1,50,E-09|3,63,E-10|8,45,E-10|1,69,E-08|4,79,E-11|
|AREA|SRC_308|Cam_Valpo_238-PEAS e Imp|268362|6398151|3 mes|251,56|9,20,E-10|2,23,E-10|5,18,E-10|1,04,E-08|2,94,E-11|
|AREA|SRC_309|Cam_Valpo_239-PEAS e Imp|268383|6398192|3 mes|185,19|1,25,E-09|3,02,E-10|7,03,E-10|1,41,E-08|3,99,E-11|
|AREA|SRC_310|Cam_Valpo_240-PEAS e Imp|268355|6398247|3 mes|250,18|9,25,E-10|2,24,E-10|5,21,E-10|1,04,E-08|2,95,E-11|
|AREA|SRC_311|Cam_Valpo_241-PEAS e Imp|268227|6398303|3 mes|566,84|4,08,E-10|9,88,E-11|2,30,E-10|4,60,E-09|1,30,E-11|
|AREA|SRC_312|Cam_Valpo_242-PEAS e Imp|268140|6398362|3 mes|418,83|5,52,E-10|1,34,E-10|3,11,E-10|6,22,E-09|1,76,E-11|
|AREA|SRC_313|Cam_Valpo_243-PEAS e Imp|268089|6398427|3 mes|325,43|7,11,E-10|1,72,E-10|4,00,E-10|8,01,E-09|2,27,E-11|
|AREA|SRC_314|Cam_Valpo_244-PEAS e Imp|268005|6398483|3 mes|406,15|5,70,E-10|1,38,E-10|3,21,E-10|6,42,E-09|1,82,E-11|
|AREA|SRC_315|Cam_Valpo_245-PEAS e Imp|267956|6398553|3 mes|338,26|6,84,E-10|1,65,E-10|3,85,E-10|7,70,E-09|2,18,E-11|
|AREA|SRC_316|Cam_Valpo_246-PEAS e Imp|267920|6398673|3 mes|498,96|4,64,E-10|1,12,E-10|2,61,E-10|5,22,E-09|1,48,E-11|
|AREA|SRC_317|Cam_Valpo_247-PEAS e Imp|267908|6398749|3 mes|308,37|7,50,E-10|1,82,E-10|4,22,E-10|8,45,E-09|2,39,E-11|
|AREA|SRC_318|Cam_Valpo_248-PEAS e Imp|267894|6398771|3 mes|107,41|2,15,E-09|5,21,E-10|1,21,E-09|2,43,E-08|6,87,E-11|
|AREA|SRC_319|Cam_Valpo_249-PEAS e Imp|267791|6398823|3 mes|466,56|4,96,E-10|1,20,E-10|2,79,E-10|5,59,E-09|1,58,E-11|
|AREA|SRC_320|Cam_Valpo_250-PEAS e Imp|267747|6398849|3 mes|204,00|1,13,E-09|2,74,E-10|6,38,E-10|1,28,E-08|3,62,E-11|
|AREA|SRC_321|Cam_Valpo_251-PEAS e Imp|267699|6398875|3 mes|217,15|1,07,E-09|2,58,E-10|6,00,E-10|1,20,E-08|3,40,E-11|
|AREA|SRC_322|Cam_Valpo_252-PEAS e Imp|267673|6398943|3 mes|285,91|8,09,E-10|1,96,E-10|4,56,E-10|9,12,E-09|2,58,E-11|
|AREA|SRC_323|Cam_Valpo_253-PEAS e Imp|267740|6399152|3 mes|871,99|2,65,E-10|6,42,E-11|1,49,E-10|2,99,E-09|8,47,E-12|
|AREA|SRC_324|Cam_Valpo_254-PEAS e Imp|267754|6399259|3 mes|434,37|5,33,E-10|1,29,E-10|3,00,E-10|6,00,E-09|1,70,E-11|
|AREA|SRC_325|Cam_Valpo_255-PEAS e Imp|267756|6399372|3 mes|452,93|5,11,E-10|1,24,E-10|2,88,E-10|5,75,E-09|1,63,E-11|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

Proyecto Redes Primarias y Planta de Tratamiento de Aguas Servidas Localidad de

Maitencillo

Tabla 148. Fuentes de Emisión - Escenario 5 parte 14

Proyecto: 0126 - V.01

Fecha Abril de 2024

Página 252 de 252

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]<br>267702|[m]<br>6399478|[m]<br>6399478|[m2]<br>480,03|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|[g/m2s]|
|AREA|SRC_326|Cam_Valpo_256-PEAS e Imp|Cam_Valpo_256-PEAS e Imp|Cam_Valpo_256-PEAS e Imp|3 mes|3 mes|4,82,E-10|1,17,E-10|2,71,E-10|5,43,E-09|1,54,E-11|
|AREA|SRC_327|Cam_Valpo_257-PEAS e Imp|267740|6399547|3 mes|307,21|7,53,E-10|1,82,E-10|4,24,E-10|8,48,E-09|2,40,E-11|
|AREA|SRC_328|Cam_Valpo_258-PEAS e Imp|267742|6399624|3 mes|311,56|7,43,E-10|1,80,E-10|4,18,E-10|8,36,E-09|2,37,E-11|
|AREA|SRC_329|Cam_Valpo_259-PEAS e Imp|267731|6399695|3 mes|287,58|8,05,E-10|1,95,E-10|4,53,E-10|9,06,E-09|2,57,E-11|
|AREA|SRC_330|Cam_Valpo_260-PEAS e Imp|267682|6399788|3 mes|425,70|5,44,E-10|1,32,E-10|3,06,E-10|6,12,E-09|1,73,E-11|
|AREA|SRC_331|Cam_Valpo_261-PEAS e Imp|267661|6399830|3 mes|187,04|1,24,E-09|2,99,E-10|6,96,E-10|1,39,E-08|3,95,E-11|

Tabla 149. Fuentes de Emisión - Escenario 5 parte 15

|Tipo|ID|Descripción|X1|Y1|Ciclo<br>operación|Área|PM10|PM2.5|SO2|NOX|CO|
|---|---|---|---|---|---|---|---|---|---|---|---|
|Tipo|ID|Descripción|[m]|[m]|[m]|[m2]|[g/s]|[g/s]|[g/s]|[g/s]|[g/s]|
|VOLUMEN|SRC_2|PTAS|273588|6383221|<br>4 mes|4,00|6,44,E-04|9,75,E-05|0,00,E+00|0,00,E+00|0,00,E+00|
|PUNTUAL|SRC_3|IF 2|273522|6383276|<br>4 mes|0,05|9,99,E-04|2,41,E-04|0,00,E+00|2,84,E-02|6,13,E-03|

ANEXO 4 - FUENTES INGRESADAS AL MODELO DE DISPERSIÓN **[www.arechile.com](http://www.arechile.com/)**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Análisis porcentual de vientos calmos - Estación Puchuncaví**

| Año | % de vientos<br>calmos | % datos<br>válidos |
| --- | --- | --- |
| 2021 | 21,24 | 92,71% |
| 2022 | 22,21 | 93,31% |
| 2023 | 25,37 | 92,98% |

**Tabla 2.: Parametrización grilla 1 receptores**

| Distancia desde el<br>centro de las fuentes<br>[m] | Espaciado del<br>receptor | Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur | Col4 | Altura de los<br>receptores |
| --- | --- | --- | --- | --- |
| Distancia desde el<br>centro de las fuentes<br>[m] | [m] | X | Y | [m] |
| 500 | 50 | 272.495 | 6.386.450 | 1,5 |
| 1.000 | 250 | 250 | 250 | 250 |

**Tabla 3.: Parametrización grilla 2 receptores**

| Distancia desde el<br>centro de las fuentes<br>[m] | Espaciado del<br>receptor | Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur | Col4 | Altura de los<br>receptores |
| --- | --- | --- | --- | --- |
| Distancia desde el<br>centro de las fuentes<br>[m] | [m] | X | Y | [m] |
| 500 | 50 | 272.306 | 6.385.136 | 1,5 |
| 1.000 | 250 | 250 | 250 | 250 |

**Tabla 4.: Parametrización grilla 3 receptores**

| Distancia desde el<br>centro de las fuentes<br>[m] | Espaciado del<br>receptor | Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur | Col4 | Altura de los<br>receptores |
| --- | --- | --- | --- | --- |
| Distancia desde el<br>centro de las fuentes<br>[m] | [m] | X | Y | [m] |
| 500 | 50 | 272.956 | 6.384.019 | 1,5 |
| 1.000 | 250 | 250 | 250 | 250 |

**Tabla 5.: Parametrización grilla 4 receptores**

| Distancia desde el<br>centro de las fuentes<br>[m] | Espaciado del<br>receptor | Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur | Col4 | Altura de los<br>receptores |
| --- | --- | --- | --- | --- |
| Distancia desde el<br>centro de las fuentes<br>[m] | [m] | X | Y | [m] |
| 500 | 50 | 272.714 | 6.382.885 | 1,5 |
| 1.000 | 250 | 250 | 250 | 250 |

**Tabla 6.: Parametrización grilla 5 receptores**

| Distancia desde el<br>centro de las fuentes<br>[m] | Espaciado del<br>receptor | Coordenadas centro de la grilla en UTM [m]<br>WGS-84 Huso 19 Sur | Col4 | Altura de los<br>receptores |
| --- | --- | --- | --- | --- |
| Distancia desde el<br>centro de las fuentes<br>[m] | [m] | X | Y | [m] |
| 20.000 | 1.000 | 272.829 | 6.385.151 | 1,5 |

**Tabla 7.: Normas de Calidad del Aire vigentes aplicables a la zona de estudio**

| Decreto | Contaminante | Tipo de Norma | Unidad | Estadístico | Tipo | Límite |
| --- | --- | --- | --- | --- | --- | --- |
| D.S.<br>No12/2011 | MP2,5 | Primaria | [μg/m3] | Percentil 98 de<br>concentraciones de 24<br>horas | Diaria | 50 |
| D.S.<br>No12/2011 | MP2,5 | Primaria | [μg/m3] | Promedio Aritmético<br>Trianual | Anual | 20 |
| D.S.<br>No12/2021 | MP10 | Primaria | [μg/m3] | Percentil 98 de<br>concentraciones de 24<br>horas | Diaria | 130 |
| D.S.<br>No12/2021 | MP10 | Primaria | [μg/m3] | Promedio Aritmético<br>Trianual | Anual | 50 |
| D.S.<br>N°104/2019 | SO2 | Primaria | [μg/m3] | Promedio Aritmético<br>Trianual del Percentil 99 | 1 hora | 350 |
| D.S.<br>N°104/2019 | SO2 | Primaria | [μg/m3] | Promedio Aritmético<br>Trianual del Percentil 99 | 24<br>horas | 150 |
| D.S.<br>N°104/2019 | SO2 | Primaria | [μg/m3] | Promedio Aritmético<br>Trianual | Anual | 60 |
| D.S.<br>N°22/2010 | SO2 | Secundario | [μg/m3] | Promedio Aritmético<br>Trianual del Percentil 99,73 | 1 hora | 1.000 |
| D.S.<br>N°22/2010 | SO2 | Secundario | [μg/m3] | Promedio Aritmético<br>Trianual del Percentil 99,7 | 24<br>Horas | 365 |
| D.S.<br>N°22/2010 | SO2 | Secundario | [μg/m3] | Promedio Aritmético<br>Trianual | Anual | 80 |
| D.S.<br>N°114/2002 | NO2 | Primaria | [μg/m3] | Promedio Aritmético<br>Trianual | Anual | 100 |
| D.S.<br>N°114/2002 | NO2 | Primaria | [μg/m3] | Percentil 99 de los<br>máximos diarios de<br>concentración 1 hora | 1 hora | 400 |
| D.S.<br>N°115/2002 | CO | Primaria | [mg/m3] | Percentil 99 de los<br>máximos diarios de 8 horas | 8 <br>horas | 10 |
| D.S.<br>N°115/2002 | CO | Primaria | [mg/m3] | Percentil 99 de los<br>máximos diarios de 1 hora | 1 hora | 30 |

**Tabla 8.: Estaciones de Calidad del Aire**

| ID | Nombre | Coordenadas UTM [m] WGS-84 Huso 19<br>Sur | Col4 | Estadístico estimado |
| --- | --- | --- | --- | --- |
| 1 | Quintero | 262.528 E | 6.371.087 N | MP10, MP2.5, SO2,NO2, CO |
| 2 | La Greda | 268.185 E | 6.373.910 N | MP10, MP2.5, SO2,NO2 |
| 3 | Puchuncaví | 274.379 E | 6.377.331 N | MP10, MP2.5, SO2,NO2 |
| 4 | Los Maitenes | 270.073 E | 6.372.171 N | MP10, MP2.5, SO2,NO2, CO |
| 5 | Valle Alegre | 271.889 E | 6.367.413 N | MP10, MP2.5, SO2 |
| 6 | Centro Quintero | 262.853 E | 6.369.407 N | MP10, MP2.5, SO2,NO2, CO |
| 7 | Loncura | 266.226 E | 6.368.689 N | MP10, MP2.5, SO2,NO2, CO |

**Tabla 9.: Porcentaje de datos en válidos Estaciones de Calidad del Aire**

| Estaciones/Años | MP<br>2,5 | Col3 | Col4 | MP<br>10 | Col6 | Col7 | SO<br>2 | Col9 | Col10 | NO<br>2 | Col12 | Col13 | CO | Col15 | Col16 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Estaciones/Años | 2021 | 2022 | 2023 | 2021 | 2022 | 2023 | 2021 | 2022 | 2023 | 2021 | 2022 | 2023 | 2021 | 2022 | 2023 |
| Quintero | 97,38 | 97,56 | 97,81 | 99,45 | 99,49 | 98,53 | 99,12 | 99,09 | 99,15 | 98,99 | 99,08 | 99,18 | 99,09 | 99,01 | 98,91 |
| La Greda | 96,56 | 98,26 | 99,55 | 98,89 | 99,20 | 99,69 | 98,97 | 98,56 | 99,15 | 98,03 | 98,21 | 97,11 | S/I | S/I | S/I |
| Puchuncaví | 95,45 | 97,53 | 99,13 | 99,52 | 99,04 | 98,57 | 99,18 | 99,18 | 99,13 | 97,86 | 98,05 | 98,61 | S/I | S/I | S/I |
| Los Maitenes | 93,37 | 95,47 | 93,74 | 99,36 | 99,12 | 99,78 | 99,23 | 98,41 | 99,29 | 98,88 | 98,32 | 98,75 | 97,99 | 98,51 | 97,68 |
| Valle Alegre | S/I | S/I | S/I | 96,08 | 94,79 | 94,86 | 98,66 | 96,21 | 99,28 | 99,22 | 96,30 | 97,80 | S/I | S/I | S/I |
| Centro Quintero | 99,73 | 99,68 | 99,90 | 99,64 | 99,68 | 99,60 | 98,85 | 99,10 | 99,12 | 99,36 | 99,95 | 99,26 | 97,60 | 98,98 | 98,32 |
| Loncura | 95,42 | 95,58 | 92,60 | 96,63 | 96,47 | 97,55 | 97,06 | 97,02 | 97,70 | 97,04 | 96,96 | 96,76 | 96,81 | 96,98 | 97,29 |

**Tabla 10.: Estadísticos de Comparación Norma Primaria MP 2,5**

| Estaciones | Años | P98 Diario<br>[ug/m3] | % Norma | Trianual<br>[ug/m3] | Promedio Tri<br>Anual [ug/m3] | % Norma |
| --- | --- | --- | --- | --- | --- | --- |
| Centro<br>Quintero | ~~2021~~<br> | ~~55,42~~<br> | ~~110,83~~<br> | ~~20,75~~<br> | 19 | 95 |
| Centro<br>Quintero | ~~2022~~<br> | ~~45,54~~<br> | ~~91,08~~<br> | ~~18,81~~<br> | ~~18,81~~<br> | ~~18,81~~<br> |
| Centro<br>Quintero | ~~2023~~<br> | ~~43,67~~<br> | ~~87,33~~<br> | ~~17,43~~<br> | ~~17,43~~<br> | ~~17,43~~<br> |
| <br>Loncura | ~~2021~~<br> | ~~35,92~~<br> | ~~71,83~~<br> | ~~14,74~~<br> | 12.69 | 63.43 |
| <br>Loncura | ~~2022~~<br> | ~~26,71~~<br> | ~~53,42~~<br> | ~~12,03~~<br> | ~~12,03~~<br> | ~~12,03~~<br> |
| <br>Loncura | ~~2023~~<br> | ~~31,23~~<br> | ~~62,45~~<br> | ~~11,29~~<br> | ~~11,29~~<br> | ~~11,29~~<br> |
| <br>Los Maitenes | ~~2021~~<br> | ~~23,96~~<br> | ~~47,92~~<br> | ~~12,03~~<br> | 12.30 | 61.50 |
| <br>Los Maitenes | ~~2022~~<br> | ~~22,13~~<br> | ~~44,25~~<br> | ~~11,37~~<br> | ~~11,37~~<br> | ~~11,37~~<br> |
| <br>Los Maitenes | ~~2023~~<br> | ~~31,29~~<br> | ~~62,58~~<br> | ~~13,51~~<br> | ~~13,51~~<br> | ~~13,51~~<br> |
| <br>Quintero | ~~2021~~<br> | ~~34,38~~<br> | ~~68,75~~<br> | ~~15,99~~<br> | 14.04 | 70.22 |
| <br>Quintero | ~~2022~~<br> | ~~26,70~~<br> | ~~53,40~~<br> | ~~13,33~~<br> | ~~13,33~~<br> | ~~13,33~~<br> |
| <br>Quintero | ~~2023~~<br> | ~~28,33~~<br> | ~~56,67~~<br> | ~~12,81~~<br> | ~~12,81~~<br> | ~~12,81~~<br> |
| <br>La Greda | ~~2021~~<br> | ~~41,08~~<br> | ~~82,17~~<br> | ~~16,45~~<br> | 15.60 | 78.01 |
| <br>La Greda | ~~2022~~<br> | ~~31,22~~<br> | ~~62,43~~<br> | ~~15,53~~<br> | ~~15,53~~<br> | ~~15,53~~<br> |
| <br>La Greda | ~~2023~~<br> | ~~33,92~~<br> | ~~67,83~~<br> | ~~14,82~~<br> | ~~14,82~~<br> | ~~14,82~~<br> |
| <br>Puchuncaví | ~~2021~~<br> | ~~32,17~~<br> | ~~64,33~~<br> | ~~14,52~~<br> | 14.86 | 74.29 |
| <br>Puchuncaví | ~~2022~~<br> | ~~33,71~~<br> | ~~67,43~~<br> | ~~15,52~~<br> | ~~15,52~~<br> | ~~15,52~~<br> |
| <br>Puchuncaví | ~~2023~~ | ~~30,67~~ | ~~61,33~~ | ~~14,54~~ | ~~14,54~~ | ~~14,54~~ |

**Tabla 11.: Estadísticos de Comparación Normas Primaria MP 10**

| Estaciones | Años | P98 Diario<br>[ug/m3] | % Norma | Trianual<br>[ug/m3] | Promedio Tri<br>Anual [ug/m3] | % Norma |
| --- | --- | --- | --- | --- | --- | --- |
| Centro<br>Quintero | ~~2021~~<br> | ~~76,46~~<br> | ~~58,81~~<br> | ~~39,81~~<br> | 39.04 | 78.08 |
| Centro<br>Quintero | ~~2022~~<br> | ~~83,29~~<br> | ~~64,07~~<br> | ~~39,63~~<br> | ~~39,63~~<br> | ~~39,63~~<br> |
| Centro<br>Quintero | ~~2023~~<br> | ~~68,21~~<br> | ~~52,47~~<br> | ~~37,68~~<br> | ~~37,68~~<br> | ~~37,68~~<br> |
| <br>Loncura | ~~2021~~<br> | ~~72,67~~<br> | ~~55,90~~<br> | ~~38,65~~<br> | 37.74 | 75.49 |
| <br>Loncura | ~~2022~~<br> | ~~73,21~~<br> | ~~56,31~~<br> | ~~39,44~~<br> | ~~39,44~~<br> | ~~39,44~~<br> |
| <br>Loncura | ~~2023~~<br> | ~~69,25~~<br> | ~~53,27~~<br> | ~~35,14~~<br> | ~~35,14~~<br> | ~~35,14~~<br> |
| <br>Los Maitenes | ~~2021~~<br> | ~~56,88~~<br> | ~~43,75~~<br> | ~~26,67~~<br> | 29.67 | 59.34 |
| <br>Los Maitenes | ~~2022~~<br> | ~~73,63~~<br> | ~~56,63~~<br> | ~~31,73~~<br> | ~~31,73~~<br> | ~~31,73~~<br> |
| <br>Los Maitenes | ~~2023~~<br> | ~~61,88~~<br> | ~~47,60~~<br> | ~~30,62~~<br> | ~~30,62~~<br> | ~~30,62~~<br> |
| <br>Quintero | ~~2021~~<br> | ~~75,54~~<br> | ~~58,11~~<br> | ~~37,98~~<br> | 37.93 | 75.87 |
| <br>Quintero | ~~2022~~<br> | ~~73,38~~<br> | ~~56,44~~<br> | ~~36,84~~<br> | ~~36,84~~<br> | ~~36,84~~<br> |
| <br>Quintero | ~~2023~~<br> | ~~75,38~~<br> | ~~57,98~~<br> | ~~38,98~~<br> | ~~38,98~~<br> | ~~38,98~~<br> |
| <br>La Greda | ~~2021~~<br> | ~~78,17~~<br> | ~~60,13~~<br> | ~~36,71~~<br> | 37.20 | 74.41 |
| <br>La Greda | ~~2022~~<br> | ~~62,00~~<br> | ~~47,69~~<br> | ~~35,45~~<br> | ~~35,45~~<br> | ~~35,45~~<br> |
| <br>La Greda | ~~2023~~<br> | ~~72,00~~<br> | ~~55,38~~<br> | ~~39,44~~<br> | ~~39,44~~<br> | ~~39,44~~<br> |
| <br>Puchuncaví | ~~2021~~<br> | ~~68,29~~<br> | ~~52,53~~<br> | ~~38,84~~<br> | 41.06 | 82.12 |
| <br>Puchuncaví | ~~2022~~<br> | ~~78,25~~<br> | ~~60,19~~<br> | ~~44,14~~<br> | ~~44,14~~<br> | ~~44,14~~<br> |
| <br>Puchuncaví | ~~2023~~<br> | ~~68,38~~<br> | ~~52,60~~<br> | ~~40,20~~<br> | ~~40,20~~<br> | ~~40,20~~<br> |
| <br>Valle Alegre | ~~2021~~<br> | ~~45,71~~<br> | ~~35,16~~<br> | ~~25,69~~<br> | 25.80 | 51.59 |
| <br>Valle Alegre | ~~2022~~<br> | ~~48,35~~<br> | ~~37,19~~<br> | ~~25,37~~<br> | ~~25,37~~<br> | ~~25,37~~<br> |
| <br>Valle Alegre | ~~2023~~ | ~~52,92~~ | ~~40,71~~ | ~~26,33~~ | ~~26,33~~ | ~~26,33~~ |

**Tabla 12.: Estadísticos de Comparación Normas Primaria SO 2**

| Estaciones | Norma Diaria | Col3 | Col4 | Col5 | Norma Anual | Col7 | Col8 | Norma Horaria | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <br>Estaciones | Años<br> | P99<br>Diario<br> | Promedio<br>Tri Anual | % <br>Norma | Trianual<br> | Promedio<br>Tri Anual | % <br>Norma | P99<br>Hora<br> | Promedio<br>Tri Anual | % <br>Norma |
| Centro<br>Quintero | ~~2021~~<br> | ~~65,37~~<br> | 53,79 | 35,86 | ~~15,61~~<br> | 13,18 | 21,97 | ~~148,01~~<br> | 116,58 | 33,31 |
| Centro<br>Quintero | ~~2022~~<br> | ~~53,24~~<br> | ~~53,24~~<br> | ~~53,24~~<br> | ~~13,24~~<br> | ~~13,24~~<br> | ~~13,24~~<br> | ~~124,65~~<br> | ~~124,65~~<br> | ~~124,65~~<br> |
| Centro<br>Quintero | ~~2023~~<br> | ~~42,78~~<br> | ~~42,78~~<br> | ~~42,78~~<br> | ~~10,69~~<br> | ~~10,69~~<br> | ~~10,69~~<br> | ~~77,07~~<br> | ~~77,07~~<br> | ~~77,07~~<br> |
| <br>Loncura | ~~2021~~<br> | ~~38,60~~<br> | 33 | 22 | ~~8,68~~<br> | 6,49 | 10,82 | ~~88,19~~<br> | 740,41 | 20,12 |
| <br>Loncura | ~~2022~~<br> | ~~38,30~~<br> | ~~38,30~~<br> | ~~38,30~~<br> | ~~6,65~~<br> | ~~6,65~~<br> | ~~6,65~~<br> | ~~78,69~~<br> | ~~78,69~~<br> | ~~78,69~~<br> |
| <br>Loncura | ~~2023~~<br> | ~~22,11~~<br> | ~~22,11~~<br> | ~~22,11~~<br> | ~~4,14~~<br> | ~~4,14~~<br> | ~~4,14~~<br> | ~~44,34~~<br> | ~~44,34~~<br> | ~~44,34~~<br> |
| Los<br>Maitenes | ~~2021~~<br> | ~~63,74~~<br> | 62,69 | 41,79 | ~~21,36~~<br> | 17,29 | 28,82 | ~~206,29~~<br> | 179,17 | 51,19 |
| Los<br>Maitenes | ~~2022~~<br> | ~~59,92~~<br> | ~~59,92~~<br> | ~~59,92~~<br> | ~~15,30~~<br> | ~~15,30~~<br> | ~~15,30~~<br> | ~~174,24~~<br> | ~~174,24~~<br> | ~~174,24~~<br> |
| Los<br>Maitenes | ~~2023~~<br> | ~~64,42~~<br> | ~~64,42~~<br> | ~~64,42~~<br> | ~~15,22~~<br> | ~~15,22~~<br> | ~~15,22~~<br> | ~~156,96~~<br> | ~~156,96~~<br> | ~~156,96~~<br> |
| <br>Quintero | ~~2021~~<br> | ~~80,91~~<br> | 63,65 | 42,43 | ~~18,03~~<br> | 13,82 | 23,04 | ~~215,32~~<br> | 142,72 | 40,78 |
| <br>Quintero | ~~2022~~<br> | ~~66,13~~<br> | ~~66,13~~<br> | ~~66,13~~<br> | ~~13,99~~<br> | ~~13,99~~<br> | ~~13,99~~<br> | ~~132,35~~<br> | ~~132,35~~<br> | ~~132,35~~<br> |
| <br>Quintero | ~~2023~~<br> | ~~43,91~~<br> | ~~43,91~~<br> | ~~43,91~~<br> | ~~9,46~~<br> | ~~9,46~~<br> | ~~9,46~~<br> | ~~80,49~~<br> | ~~80,49~~<br> | ~~80,49~~<br> |
| <br>La Greda | ~~2021~~<br> | ~~32,80~~<br> | 28,06 | 18,71 | ~~13,05~~<br> | 11,30 | 18,83 | ~~60,47~~<br> | 44,77 | 12,79 |
| <br>La Greda | ~~2022~~<br> | ~~30,05~~<br> | ~~30,05~~<br> | ~~30,05~~<br> | ~~13,30~~<br> | ~~13,30~~<br> | ~~13,30~~<br> | ~~50,42~~<br> | ~~50,42~~<br> | ~~50,42~~<br> |
| <br>La Greda | ~~2023~~<br> | ~~21,34~~<br> | ~~21,34~~<br> | ~~21,34~~<br> | ~~7,54~~<br> | ~~7,54~~<br> | ~~7,54~~<br> | ~~23,41~~<br> | ~~23,41~~<br> | ~~23,41~~<br> |
| <br>Puchuncaví | ~~2021~~<br> | ~~31,77~~<br> | 28,89 | 19,26 | ~~15,04~~<br> | 14,09 | 23,48 | ~~67,25~~<br> | 57,86 | 16,53 |
| <br>Puchuncaví | ~~2022~~<br> | ~~31,46~~<br> | ~~31,46~~<br> | ~~31,46~~<br> | ~~16,17~~<br> | ~~16,17~~<br> | ~~16,17~~<br> | ~~63,16~~<br> | ~~63,16~~<br> | ~~63,16~~<br> |
| <br>Puchuncaví | ~~2023~~<br> | ~~23,44~~<br> | ~~23,44~~<br> | ~~23,44~~<br> | ~~11,05~~<br> | ~~11,05~~<br> | ~~11,05~~<br> | ~~43,16~~<br> | ~~43,16~~<br> | ~~43,16~~<br> |
| Valle<br>Alegre | ~~2021~~<br> | ~~38,94~~<br> | 29,90 | 19,93 | ~~17,06~~<br> | 11,20 | 18,66 | ~~83,31~~<br> | 62,98 | 17,99 |
| Valle<br>Alegre | ~~2022~~<br> | ~~33,22~~<br> | ~~33,22~~<br> | ~~33,22~~<br> | ~~10,92~~<br> | ~~10,92~~<br> | ~~10,92~~<br> | ~~68,40~~<br> | ~~68,40~~<br> | ~~68,40~~<br> |
| Valle<br>Alegre | ~~2023~~ | ~~17,53~~ | ~~17,53~~ | ~~17,53~~ | ~~5,61~~ | ~~5,61~~ | ~~5,61~~ | ~~37,21~~ | ~~37,21~~ | ~~37,21~~ |

**Tabla 13.: Estadísticos de Comparación Normas Secundaria SO 2**

| Estaciones | Norma Diaria | Col3 | Col4 | Col5 | Norma Anual | Col7 | Col8 | Norma Horaria | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| <br>Estaciones | Años<br> | P99 .7<br>Diario<br> | Promedio<br>Tri Anual | % <br>Norma | Trianual<br> | Promedio<br>Tri Anual | % <br>Norma | P99.73<br>Hora<br> | Promedio<br>Tri Anual | % <br>Norma |
| Centro<br>Quintero | ~~2021~~<br> | ~~87,01~~<br> | 65,78 | 18,02 | ~~15,67~~<br> | 13,19 | 16,49 | ~~217,07~~<br> | 184,14 | 18,41 |
| Centro<br>Quintero | ~~2022~~<br> | ~~63,46~~<br> | ~~63,46~~<br> | ~~63,46~~<br> | ~~13,24~~<br> | ~~13,24~~<br> | ~~13,24~~<br> | ~~205,56~~<br> | ~~205,56~~<br> | ~~205,56~~<br> |
| Centro<br>Quintero | ~~2023~~<br> | ~~46,88~~<br> | ~~46,88~~<br> | ~~46,88~~<br> | ~~10,67~~<br> | ~~10,67~~<br> | ~~10,67~~<br> | ~~129,79~~<br> | ~~129,79~~<br> | ~~129,79~~<br> |
| <br>Loncura | ~~2021~~<br> | ~~65,63~~<br> | 46,97 | 12,87 | ~~8,80~~<br> | 6,54 | 8,18 | ~~152,18~~<br> | 119,66 | 1196 |
| <br>Loncura | ~~2022~~<br> | ~~43,64~~<br> | ~~43,64~~<br> | ~~43,64~~<br> | ~~6,69~~<br> | ~~6,69~~<br> | ~~6,69~~<br> | ~~129,48~~<br> | ~~129,48~~<br> | ~~129,48~~<br> |
| <br>Loncura | ~~2023~~<br> | ~~31,65~~<br> | ~~31,65~~<br> | ~~31,65~~<br> | ~~4,14~~<br> | ~~4,14~~<br> | ~~4,14~~<br> | ~~77,30~~<br> | ~~77,30~~<br> | ~~77,30~~<br> |
| Los<br>Maitenes | ~~2021~~<br> | ~~74,68~~<br> | 77,68 | 21,28 | ~~21,33~~<br> | 17,27 | 21,58 | ~~292,99~~<br> | 278,16 | 27,81 |
| Los<br>Maitenes | ~~2022~~<br> | ~~68,47~~<br> | ~~68,47~~<br> | ~~68,47~~<br> | ~~15,34~~<br> | ~~15,34~~<br> | ~~15,34~~<br> | ~~274,18~~<br> | ~~274,18~~<br> | ~~274,18~~<br> |
| Los<br>Maitenes | ~~2023~~<br> | ~~89,88~~<br> | ~~89,88~~<br> | ~~89,88~~<br> | ~~15,13~~<br> | ~~15,13~~<br> | ~~15,13~~<br> | ~~267,29~~<br> | ~~267,29~~<br> | ~~267,29~~<br> |
| <br>Quintero | ~~2021~~<br> | ~~92,98~~<br> | 76,98 | 21,09 | ~~18,08~~<br> | 13,84 | 17,30 | ~~331,28~~<br> | 249,86 | 24,98 |
| <br>Quintero | ~~2022~~<br> | ~~86,65~~<br> | ~~86,65~~<br> | ~~86,65~~<br> | ~~13,96~~<br> | ~~13,96~~<br> | ~~13,96~~<br> | ~~269,79~~<br> | ~~269,79~~<br> | ~~269,79~~<br> |
| <br>Quintero | ~~2023~~<br> | ~~51,30~~<br> | ~~51,30~~<br> | ~~51,30~~<br> | ~~9,48~~<br> | ~~9,48~~<br> | ~~9,48~~<br> | ~~148,48~~<br> | ~~148,48~~<br> | ~~148,48~~<br> |
| <br>La Greda | ~~2021~~<br> | ~~33,51~~<br> | 30,22 | 8,28 | ~~13,06~~<br> | 11,29 | 14,11 | ~~105,91~~<br> | 79,61 | 7,96 |
| <br>La Greda | ~~2022~~<br> | ~~34,74~~<br> | ~~34,74~~<br> | ~~34,74~~<br> | ~~13,30~~<br> | ~~13,30~~<br> | ~~13,30~~<br> | ~~90,69~~<br> | ~~90,69~~<br> | ~~90,69~~<br> |
| <br>La Greda | ~~2023~~<br> | ~~22,42~~<br> | ~~22,42~~<br> | ~~22,42~~<br> | ~~7,51~~<br> | ~~7,51~~<br> | ~~7,51~~<br> | ~~42,22~~<br> | ~~42,22~~<br> | ~~42,22~~<br> |
| <br>Puchuncaví | ~~2021~~<br> | ~~34,21~~<br> | 31,98 | 8,76 | ~~15,02~~<br> | 14,08 | 17,60 | ~~98,94~~<br> | 81,75 | 8,17 |
| <br>Puchuncaví | ~~2022~~<br> | ~~37,30~~<br> | ~~37,30~~<br> | ~~37,30~~<br> | ~~16,16~~<br> | ~~16,16~~<br> | ~~16,16~~<br> | ~~85,45~~<br> | ~~85,45~~<br> | ~~85,45~~<br> |
| <br>Puchuncaví | ~~2023~~<br> | ~~24,43~~<br> | ~~24,43~~<br> | ~~24,43~~<br> | ~~11,06~~<br> | ~~11,06~~<br> | ~~11,06~~<br> | ~~60,83~~<br> | ~~60,83~~<br> | ~~60,83~~<br> |
| Valle<br>Alegre | ~~2021~~<br> | ~~40,71~~<br> | 34,11 | 9,34 | ~~17,07~~<br> | 11,82 | 14,77 | ~~121,41~~<br> | 95,59 | 9,55 |
| Valle<br>Alegre | ~~2022~~<br> | ~~39,54~~<br> | ~~39,54~~<br> | ~~39,54~~<br> | ~~12,80~~<br> | ~~12,80~~<br> | ~~12,80~~<br> | ~~100,69~~<br> | ~~100,69~~<br> | ~~100,69~~<br> |
| Valle<br>Alegre | ~~2023~~ | ~~22,06~~ | ~~22,06~~ | ~~22,06~~ | ~~5,58~~ | ~~5,58~~ | ~~5,58~~ | ~~64,64~~ | ~~64,64~~ | ~~64,64~~ |

**Tabla 14.: Estadísticos de Comparación Normas Primaria NO 2**

| Estaciones | Años | P99<br>Horario | Promedio<br>Tri Anual | % Norma | Trianual | Promedio<br>Tri Anual | % Norma |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Centro<br>Quintero | ~~2021~~<br> | ~~64,84~~<br> | 104,78 | 26,20 | ~~16,83~~<br> | 17,21 | 17,21 |
| Centro<br>Quintero | ~~2022~~<br> | ~~187,04~~<br> | ~~187,04~~<br> | ~~187,04~~<br> | ~~17,32~~<br> | ~~17,32~~<br> | ~~17,32~~<br> |
| Centro<br>Quintero | ~~2023~~<br> | ~~62,47~~<br> | ~~62,47~~<br> | ~~62,47~~<br> | ~~17,48~~<br> | ~~17,48~~<br> | ~~17,48~~<br> |
| <br>Loncura | ~~2021~~<br> | ~~56,66~~<br> | 51,25 | 12,81 | ~~11,40~~<br> | 10,46 | 10,46 |
| <br>Loncura | ~~2022~~<br> | ~~51,55~~<br> | ~~51,55~~<br> | ~~51,55~~<br> | ~~10,01~~<br> | ~~10,01~~<br> | ~~10,01~~<br> |
| <br>Loncura | ~~2023~~<br> | ~~45,53~~<br> | ~~45,53~~<br> | ~~45,53~~<br> | ~~9,98~~<br> | ~~9,98~~<br> | ~~9,98~~<br> |
| Los<br>Maitenes | ~~2021~~<br> | ~~57,34~~<br> | 53,17 | 13,29 | ~~11,64~~<br> | 10,62 | 10,62 |
| Los<br>Maitenes | ~~2022~~<br> | ~~50,80~~<br> | ~~50,80~~<br> | ~~50,80~~<br> | ~~10,59~~<br> | ~~10,59~~<br> | ~~10,59~~<br> |
| Los<br>Maitenes | ~~2023~~<br> | ~~51,36~~<br> | ~~51,36~~<br> | ~~51,36~~<br> | ~~9,63~~<br> | ~~9,63~~<br> | ~~9,63~~<br> |
| <br>Quintero | ~~2021~~<br> | ~~59,56~~<br> | 70,28 | 17,57 | ~~14,90~~<br> | 15,37 | 15,37 |
| <br>Quintero | ~~2022~~<br> | ~~92,59~~<br> | ~~92,59~~<br> | ~~92,59~~<br> | ~~16,10~~<br> | ~~16,10~~<br> | ~~16,10~~<br> |
| <br>Quintero | ~~2023~~<br> | ~~58,69~~<br> | ~~58,69~~<br> | ~~58,69~~<br> | ~~15,13~~<br> | ~~15,13~~<br> | ~~15,13~~<br> |
| <br>La Greda | ~~2021~~<br> | ~~57,85~~<br> | 57,79 | 14,45 | ~~15,38~~<br> | 16,95 | 16,95 |
| <br>La Greda | ~~2022~~<br> | ~~52,70~~<br> | ~~52,70~~<br> | ~~52,70~~<br> | ~~18,48~~<br> | ~~18,48~~<br> | ~~18,48~~<br> |
| <br>La Greda | ~~2023~~<br> | ~~62,83~~<br> | ~~62,83~~<br> | ~~62,83~~<br> | ~~17,00~~<br> | ~~17,00~~<br> | ~~17,00~~<br> |
| <br>Puchuncaví | ~~2021~~<br> | ~~57,90~~<br> | 54,52 | 13,63 | ~~15,41~~<br> | 14,77 | 14,77 |
| <br>Puchuncaví | ~~2022~~<br> | ~~54,80~~<br> | ~~54,80~~<br> | ~~54,80~~<br> | ~~14,81~~<br> | ~~14,81~~<br> | ~~14,81~~<br> |
| <br>Puchuncaví | ~~2023~~<br> | ~~50,85~~<br> | ~~50,85~~<br> | ~~50,85~~<br> | ~~14,10~~<br> | ~~14,10~~<br> | ~~14,10~~<br> |
| Valle<br>Alegre | ~~2021~~<br> | ~~55,70~~<br> | 49,65 | 12,41 | ~~9,83~~<br> | 10,40 | 10,40 |
| Valle<br>Alegre | ~~2022~~<br> | ~~43,82~~<br> | ~~43,82~~<br> | ~~43,82~~<br> | ~~8,99~~<br> | ~~8,99~~<br> | ~~8,99~~<br> |
| Valle<br>Alegre | ~~2023~~ | ~~49,43~~ | ~~49,43~~ | ~~49,43~~ | ~~12,38~~ | ~~12,38~~ | ~~12,38~~ |

**Tabla 15.: Estadísticos de Comparación Normas Primaria CO**

| Estaciones | Años | P99<br>Horario | Promedio<br>Tri Anual | % Norma | P99 8<br>Horas | Promedio<br>Tri Anual | % Norma |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Centro<br>Quintero | ~~2021~~<br> | ~~1,73~~<br> | 1,70 | 5,67 | ~~1,15~~<br> | 1,05 | 10,49 |
| Centro<br>Quintero | ~~2022~~<br> | ~~1,84~~<br> | ~~1,84~~<br> | ~~1,84~~<br> | ~~1,07~~<br> | ~~1,07~~<br> | ~~1,07~~<br> |
| Centro<br>Quintero | ~~2023~~<br> | ~~1,54~~<br> | ~~1,54~~<br> | ~~1,54~~<br> | ~~0,93~~<br> | ~~0,93~~<br> | ~~0,93~~<br> |
| <br>Loncura | ~~2021~~<br> | ~~1,08~~<br> | 1,37 | 4,56 | ~~0,77~~<br> | 1,10 | 11 |
| <br>Loncura | ~~2022~~<br> | ~~1,49~~<br> | ~~1,49~~<br> | ~~1,49~~<br> | ~~1,26~~<br> | ~~1,26~~<br> | ~~1,26~~<br> |
| <br>Loncura | ~~2023~~<br> | ~~1,53~~<br> | ~~1,53~~<br> | ~~1,53~~<br> | ~~1,27~~<br> | ~~1,27~~<br> | ~~1,27~~<br> |
| Los<br>Maitenes | ~~2021~~<br> | ~~0,79~~<br> | 0,80 | 2,67 | ~~0,74~~<br> | 0,55 | 5,54 |
| Los<br>Maitenes | ~~2022~~<br> | ~~0,81~~<br> | ~~0,81~~<br> | ~~0,81~~<br> | ~~0,44~~<br> | ~~0,44~~<br> | ~~0,44~~<br> |
| Los<br>Maitenes | ~~2023~~<br> | ~~0,81~~<br> | ~~0,81~~<br> | ~~0,81~~<br> | ~~0,49~~<br> | ~~0,49~~<br> | ~~0,49~~<br> |
| <br>Quintero | ~~2021~~<br> | ~~1,46~~<br> | 1,31 | 4,37 | ~~0,88~~<br> | 0,70 | 7,02 |
| <br>Quintero | ~~2022~~<br> | ~~1,40~~<br> | ~~1,40~~<br> | ~~1,40~~<br> | ~~0,67~~<br> | ~~0,67~~<br> | ~~0,67~~<br> |
| <br>Quintero | ~~2023~~ | ~~1,07~~ | ~~1,07~~ | ~~1,07~~ | ~~0,56~~ | ~~0,56~~ | ~~0,56~~ |

**Tabla 16.: Actividades y tipología de fuentes**

| Actividades | Fuente |
| --- | --- |
| ~~Camino Pavimentado~~<br> | ~~Área~~<br> |
| ~~Excavaciones y movimientos de tierra~~<br> | ~~Área~~<br> |
| ~~Transferencia de material~~<br> | ~~Volumétrica~~<br> |
| ~~Combustión de maquinaria~~<br> | ~~Área~~<br> |
| ~~Combustión interna vehículos pesados~~ | ~~Área~~ |
| Combustión interna de grupos<br>electrógenos<br> | Puntual<br> |
| ~~Dispersión por acopio de material~~ | ~~Área~~ |

**Tabla 17.: Escenarios de modelación**

| Escenarios modelación | Fuentes |
| --- | --- |
| E1:<br>Escenario 1 | Proyecto Maitencillo Etapa 1 |
| E1:<br>Escenario 1 | -PEAS 1, PEAS 2, PEAS 3 e impulsiones |
| E1:<br>Escenario 1 | -PEAS 5.1 e impulsión |
| E1:<br>Escenario 1 | -PEAS 5.2 e impulsión |
| E1:<br>Escenario 1 | -Red Primaria de A.S. |
| E1:<br>Escenario 1 |  |
| E1:<br>Escenario 1 | Sistema Planta de Tratamiento |
| E1:<br>Escenario 1 | -Proyecto PTAS Maitencillo Etapa 1 |
| E2:<br>Escenario 2 | Proyecto Maitencillo Etapa 2 |
| E2:<br>Escenario 2 | -PEAS 6, PEAS 7, PEAS 8 e impulsiones |
| E2:<br>Escenario 2 | -Red Primaria de A.S. |
| E3:<br>Escenario 3 | Proyecto Maitencillo Etapa 3 |
| E3:<br>Escenario 3 | -PEAS 9, PEAS 10 e impulsiones |
| E4:<br>Escenario 4 | Proyecto Maitencillo Etapa 4 |
| E4:<br>Escenario 4 | -Red Primaria de A.S. |
| E4:<br>Escenario 4 |  |
| E4:<br>Escenario 4 | Sistema Planta de Tratamiento |
| E4:<br>Escenario 4 | -Proyecto PTAS Maitencillo Etapa 2 |
| E5:<br>Escenario 5 | Sistema Planta de Tratamiento |
| E5:<br>Escenario 5 | -Proyecto PTAS Maitencillo Etapa 3 |

**Tabla 18.: Actividades del proyecto y Emisiones Etapa 1 y 2**

| Fase | Etapa<br>Proyecto | Tipo de Emisión | MP<br>10<br>[kg/d] | MP<br>2,5<br>[kg/d] | MPS<br>[kg/d] | SO<br>2<br>[kg/d] | NOX<br>[kg/d] | CO<br>[kg/d] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Construcción | 1 | Camino<br>Pavimentado | 0,471 | 0,114 | 0,140 | 0,000 | 0.00 | 0.00 |
| Construcción | 1 | Excavaciones y<br>Movimientos de<br>Tierra | 39,812 | 20,435 | 194,617 | 0,000 | 0.00 | 0.00 |
| Construcción | 1 | Transferencia<br>de Material | 1,482 | 0,224 | 2,345 | 0,000 | 0.00 | 0.00 |
| Construcción | 1 | Combustión de<br>Maquinaria | 0,000 | 0,000 | 0,000 | 0,000 | 0.00 | 0.00 |
| Construcción | 1 | Combustión<br>Interna<br>Vehículos<br>Pesados | 0,000 | 0,000 | 0,000 | 0,016 | 0.25 | 0.06 |
| Construcción | 1 | Combustión<br>Interna Grupo | 0,633 | 0,153 | 0,000 | 0,000 | 17.97 | 3.88 |
| Construcción | 1 <br> | Dispersión por<br>Acopio de<br>Material<br> | 1,576<br> | 0,247<br> | 1,695<br> | 0,000<br> | 0.00<br> | 0.00<br> |
| ~~TOTAL~~ | ~~TOTAL~~ | ~~TOTAL~~ | ~~43.974~~ | ~~21.173~~ | ~~198,796~~ | ~~0,016~~ | ~~18,219~~ | ~~3,940~~ |
| Construcción | 2 | Camino<br>Pavimentado | 0,216 | 0,052 | 0,064 | 0,000 | 0.000 | 0.000 |
| Construcción | 2 | Excavaciones y<br>Movimientos de<br>Tierra | 9,959 | 5,112 | 48,683 | 0,000 | 0.000 | 0.000 |
| Construcción | 2 | Transferencia<br>de Material | 0,377 | 0,057 | 0,596 | 0,000 | 0.000 | 0.000 |
| Construcción | 2 | Combustión de<br>Maquinaria | 0,000 | 0,000 | 0,000 | 0,000 | 0.000 | 0.000 |
| Construcción | 2 | Combustión<br>Interna<br>Vehículos<br>Pesados | 0,000 | 0,000 | 0,000 | 0,024 | 0.298 | 0.071 |
| Construcción | 2 | Combustión<br>Interna Grupo | 0,633 | 0,153 | 0,000 | 0,000 | 17.972 | 3.881 |
| Construcción | 2 <br> | Dispersión por<br>Acopio de<br>Material<br> | 0,410<br> | 0,064<br> | 0,440<br> | 0,000<br> | 0.000<br> | 0.000<br> |
| ~~TOTAL~~ | ~~TOTAL~~ | ~~TOTAL~~ | ~~11.595~~ | ~~5.438~~ | ~~49,784~~ | ~~0,024~~ | ~~18,269~~ | ~~3,952~~ |

**Tabla 19.: Actividades del proyecto y Emisiones Etapa 3 y 4**

| Fase | Etapa<br>Proyecto | Tipo de Emisión | MP<br>10<br>[kg/d] | MP<br>2,5<br>[kg/d] | MPS<br>[kg/d] | SO<br>2<br>[kg/d] | NOX<br>[kg/d] | CO<br>[kg/d] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Construcción | 3 | Camino<br>Pavimentado | 0,035 | 0,009 | 0,010 | 0,000 | 0.000 | 0.000 |
| Construcción | 3 | Excavaciones y<br>Movimientos de<br>Tierra | 2,242 | 1,151 | 10,959 | 0,000 | 0.000 | 0.000 |
| Construcción | 3 | Transferencia de<br>Material | 0,139 | 0,021 | 0,219 | 0,000 | 0.000 | 0.000 |
| Construcción | 3 | Combustión de<br>Maquinaria | 0,000 | 0,000 | 0,000 | 0,000 | 0.000 | 0.000 |
| Construcción | 3 | Combustión<br>Interna<br>Vehículos<br>Pesados | 0,000 | 0,000 | 0,000 | 0,007 | 0.098 | 0.023 |
| Construcción | 3 | Combustión<br>Interna Grupo | 0,172 | 0,042 | 0,000 | 0,000 | 4.892 | 1.056 |
| Construcción | 3 <br> | Dispersión por<br>Acopio de<br>Material<br> | 0,181<br> | 0,028<br> | 0,195<br> | 0,000<br> | 0.000<br> | 0.000<br> |
| ~~TOTAL~~ | ~~TOTAL~~ | ~~TOTAL~~ | ~~2.769~~ | ~~1.250~~ | ~~11,384~~ | ~~0,007~~ | ~~4,990~~ | ~~1,080~~ |
| Construcción | 4 | Camino<br>Pavimentado | 0,018 | 0,004 | 0,005 | 0,000 | 0.000 | 0.000 |
| Construcción | 4 | Excavaciones y<br>Movimientos de<br>Tierra | 1,270 | 0,652 | 6,208 | 0,000 | 0.000 | 0.000 |
| Construcción | 4 | Transferencia de<br>Material | 0,042 | 0,006 | 0,067 | 0,000 | 0.000 | 0.000 |
| Construcción | 4 | Combustión de<br>Maquinaria | 0,000 | 0,000 | 0,000 | 0,000 | 0.000 | 0.000 |
| Construcción | 4 | Combustión<br>Interna<br>Vehículos<br>Pesados | 0,000 | 0,000 | 0,000 | 0,008 | 0.138 | 0.033 |
| Construcción | 4 | Combustión<br>Interna Grupo | 0,172 | 0,042 | 0,000 | 0,000 | 4.892 | 1.056 |
| Construcción | 4 <br> | Dispersión por<br>Acopio de<br>Material<br> | 0,043<br> | 0,007<br> | 0,046<br> | 0,000<br> | 0.000<br> | 0.000<br> |
| ~~TOTAL~~ | ~~TOTAL~~ | ~~TOTAL~~ | ~~1.546~~ | ~~0.711~~ | ~~6,327~~ | ~~0,008~~ | ~~5,029~~ | ~~1,089~~ |

**Tabla 20.: Actividades del proyecto y Emisiones Etapa PTAS 1 y 2**

| Fase | Etapa<br>Proyecto | Tipo de Emisión | MP<br>10<br>[kg/d] | MP<br>2,5<br>[kg/d] | MPS<br>[kg/d] | SO<br>2<br>[kg/d] | NOX<br>[kg/d] | CO<br>[kg/d] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Construcción | 1 PTAS | Camino<br>Pavimentado | 0,013 | 0,003 | 0,004 | 0,000 | 0.000 | 0.000 |
| Construcción | 1 PTAS | Excavaciones<br>y <br>Movimientos<br>de<br>Tierra | 3,814 | 1,958 | 18,644 | 0,000 | 0.000 | 0.000 |
| Construcción | 1 PTAS | Transferencia<br>de<br>Material | 0,131 | 0,020 | 0,207 | 0,000 | 0.000 | 0.000 |
| Construcción | 1 PTAS | Combustión<br>de<br>Maquinaria | 0,000 | 0,000 | 0,000 | 0,000 | 0.000 | 0.000 |
| Construcción | 1 PTAS | Combustión<br>Interna Vehículos<br>Pesados | 0,000 | 0,000 | 0,000 | 0,002 | 0.044 | 0.010 |
| Construcción | 1 PTAS | Combustión<br>Interna Grupo | 0,086 | 0,021 | 0,000 | 0,000 | 2.453 | 0.530 |
| Construcción<br> | 1 PTAS | Dispersión<br>por<br>Acopio de Material | 0,116<br> | 0,018<br> | 0,125<br> | 0,000<br> | 0.000<br> | 0.000<br> |
| ~~TOTAL~~ | ~~TOTAL~~ | ~~TOTAL~~ | ~~4.160~~ | ~~2.020~~ | ~~18,980~~ | ~~0,002~~ | ~~2,497~~ | ~~0,540~~ |
| Construcción | 2 PTAS | Camino<br>Pavimentado | 0,002 | 0,001 | 0,001 | 0,000 | 0.000 | 0.000 |
| Construcción | 2 PTAS | Excavaciones<br>y <br>Movimientos<br>de<br>Tierra | 0,464 | 0,238 | 2,266 | 0,000 | 0.000 | 0.000 |
| Construcción | 2 PTAS | Transferencia<br>de<br>Material | 0,018 | 0,003 | 0,028 | 0,000 | 0.000 | 0.000 |
| Construcción | 2 PTAS | Combustión<br>de<br>Maquinaria | 0,000 | 0,000 | 0,000 | 0,000 | 0.000 | 0.000 |
| Construcción | 2 PTAS | Combustión<br>Interna Vehículos<br>Pesados | 0,000 | 0,000 | 0,000 | 0,002 | 0.037 | 0.009 |
| Construcción | 2 PTAS | Combustión<br>Interna Grupo | 0,086 | 0,021 | 0,000 | 0,000 | 2.453 | 0.530 |
| Construcción<br> | 2 PTAS | Dispersión<br>por<br>Acopio de Material | 0,018<br> | 0,003<br> | 0,020<br> | 0,000<br> | 0.000<br> | 0.000<br> |
| ~~TOTAL~~ | ~~TOTAL~~ | ~~TOTAL~~ | ~~0.589~~ | ~~0.265~~ | ~~2,315~~ | ~~0,002~~ | ~~2,489~~ | ~~0,538~~ |

**Tabla 21.: Actividades del proyecto y Emisiones Etapa PTAS 3**

| Fase | Etapa<br>Proyecto | Tipo de Emisión | MP<br>10<br>[kg/d] | MP<br>2,5<br>[kg/d] | MPS<br>[kg/d] | SO<br>2<br>[kg/d] | NOX<br>[kg/d] | CO<br>[kg/d] |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Construcción | 3 PTAS | Camino<br>Pavimentado | 0,003 | 0,001 | 0,001 | 0,000 | 0,000 | 0,000 |
| Construcción | 3 PTAS | Excavaciones y<br>Movimientos de<br>Tierra | 0,713 | 0,366 | 3,488 | 0,000 | 0,000 | 0,000 |
| Construcción | 3 PTAS | Transferencia de<br>Material | 0,028 | 0,004 | 0,044 | 0,000 | 0,000 | 0,000 |
| Construcción | 3 PTAS | Combustión de<br>Maquinaria | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 | 0,000 |
| Construcción | 3 PTAS | Combustión<br>Interna<br>Vehículos<br>Pesados | 0,000 | 0,000 | 0,000 | 0,002 | 0,037 | 0,009 |
| Construcción | 3 PTAS | Combustión<br>Interna Grupo | 0,086 | 0,021 | 0,000 | 0,000 | 2,453 | 0,530 |
| Construcción | 3 PTAS<br> | Dispersión por<br>Acopio de<br>Material | 0,028<br> | 0,004<br> | 0,031<br> | 0,000<br> | 0,000<br> | 0,000<br> |
| ~~TOTAL~~ | ~~TOTAL~~ | ~~TOTAL~~ | ~~0,859~~ | ~~0,397~~ | ~~3,563~~ | ~~0,002~~ | ~~2,489~~ | ~~0,538~~ |

**Tabla 22.: Receptores discretos parte 1**

| ID | Coordenadas UTM [m]<br>(WGS84-H19S) | Col3 | Descripción | Col5 |
| --- | --- | --- | --- | --- |
| ID | X:Este | Y: Sur | Y: Sur | Y: Sur |
| R1 | 273.467 | 6.387.304 | Receptor ruido 1 | Receptor 1, corresponde a una vivienda existente ubicada<br>dentro del límite urbano del Plan Regulador Comunal de<br>Putaendo, específicamente en la zona Z4.<br>Por otro lado, el receptor se encuentra dentro del límite del<br>Plan Regulador Intercomunal de Valparaíso -Satélite Borde<br>Costero Norte, específicamente en la zona área urbana<br>(AU). |
| R2 | 273.165 | 6.386.964 | Receptor ruido 2 | Receptor 2, corresponde a una vivienda existente ubicada<br>dentro del límite urbano del Plan Regulador Comunal de<br>Putaendo, específicamente en la zona Z4.<br>Por otro lado, el receptor se encuentra dentro del límite del<br>Plan Regulador Intercomunal de Valparaíso -Satélite Borde<br>Costero Norte, específicamente en la zona área urbana<br>(AU). |
| R3 | 272.667 | 6.386.718 | Receptor ruido 3 | Receptor 3, corresponde a una vivienda existente ubicada<br>dentro del límite urbano del Plan Regulador Comunal de<br>Putaendo, específicamente en la zona ZRR.<br>Por otro lado, el receptor se encuentra dentro del límite del<br>Plan Regulador Intercomunal de Valparaíso -Satélite Borde<br>Costero Norte, específicamente en la zona área urbana<br>(AU). |
| R4 | 272.686 | 6.386.266 | Receptor ruido 4 | Receptor 4, corresponde a una vivienda existente ubicada<br>dentro del límite urbano del Plan Regulador Comunal de<br>Putaendo, específicamente en la zona Z4.<br>Por otro lado, el receptor se encuentra dentro del límite del<br>Plan Regulador Intercomunal de Valparaíso -Satélite Borde<br>Costero Norte, específicamente en la zona área urbana<br>(AU). |
| R5 | 272.095 | 6.386.403 | Receptor ruido 5 | Receptor 5, corresponde a un acceso a la zona costera<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z6.<br>Por otro lado, el receptor se encuentra dentro del límite del<br>Plan Regulador Intercomunal de Valparaíso -Satélite Borde<br>Costero Norte, específicamente en la zona área urbana<br>(AU). |

**Tabla 23.: Receptores discretos parte 2**

| ID | Coordenadas UTM [m]<br>(WGS84-H19S) | Col3 | Descripción | Col5 |
| --- | --- | --- | --- | --- |
| ID | X: Este | Y: Sur | Y: Sur | Y: Sur |
| R6 | 272.061 | 6.386.029 | Receptor ruido 6 | Receptor 6, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z6.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU). |
| R7 | 272.062 | 6.385.336 | Receptor ruido 7 | Receptor 7, corresponde Retén Mitencillo ubicada dentro<br>del límite urbano del Plan Regulador Comunal de<br>Putaendo, específicamente en la zona Z9.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU). |
| R8 | 272.550 | 6.385.155 | Receptor ruido 8 | Receptor 8, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z9.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU). |
| R9 | 272.361 | 6.384.963 | Receptor ruido 9 | Receptor 9, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z9.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU). |
| R10 | 272.633 | 6.384.083 | Receptor ruido 10 | Receptor 10, corresponde a la planta elevadora ubicada<br>fuera del límite urbano del Plan Regulador Comunal de<br>Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU). |
| R11 | 271.742 | 6.385.511 | Receptor ruido 12 | Receptor 11, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z7.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU). |
| R12 | 271.303 | 6.385.031 | Receptor ruido 13 | Receptor 12, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z7.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU). |
| R13 | 270.870 | 6.384.346 | Receptor ruido 14 | Receptor 13, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z7.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU). |

**Tabla 24.: Receptores discretos parte 3**

| ID | Coordenadas UTM [m]<br>(WGS84-H19S) | Col3 | Descripción | Col5 |
| --- | --- | --- | --- | --- |
| ID | X: Este | Y: Sur | Y: Sur | Y: Sur |
| R14 | 271.064 | 6.383.040 | Receptor ruido 15 | Receptor 14, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z6.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU). |
| R15 | 271.195 | 6.382.539 | Receptor ruido 16 | Receptor 15, corresponde a una vivienda existente<br>ubicada dentro del límite urbano del Plan Regulador<br>Comunal de Putaendo, específicamente en la zona Z5.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU). |
| R16 | 273.437 | 6.383.498 | Receptor fauna | Receptor 16, corresponde a un punto receptor de fauna<br>ubicado en una zona boscosa presente fuera del límite<br>urbano del Plan Regulador Comunal de Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte (ZEU 20). |
| R17 | 272.900 | 6.384.175 | Receptor olor 1 | Receptor 17, corresponde a una vivienda existente fuera<br>del límite urbano del Plan Regulador Comunal de<br>Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte (ZEU 20). |
| R18 | 273.262 | 6.384.342 | Receptor olor 2 | Receptor 18, corresponde a una vivienda existente fuera<br>del límite urbano del Plan Regulador Comunal de<br>Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte (ZEU 20). |
| R19 | 273.332 | 6.384.523 | Receptor olor 3 | Receptor 19, corresponde a una vivienda existente fuera<br>del límite urbano del Plan Regulador Comunal de<br>Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte (ZEU 20). |
| R20 | 273.201 | 6.382.149 | Receptor olor 4 | Receptor 20 corresponde a una vivienda existente<br>situada fuera del límite urbano del Plan Regulador<br>Comunal de Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso - Satélite<br>Borde Costero Norte (ZEU 20). |
| R21 | 274.626 | 6.383.665 | Receptor olor 5 | Receptor<br>21,<br>corresponde<br>a <br>instalación<br>de<br>telecomunicaciones existente fuera del límite urbano del<br>Plan Regulador Comunal de Puchuncaví,<br>Por otro lado, el receptor se encuentra fuera del límite del<br>Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte (Área Rural). |
| R22 | 275.043 | 6.382.044 | Receptor olor 6 | Receptor 22, corresponde a una vivienda existente fuera<br>del límite urbano del Plan Regulador Comunal de<br>Puchuncaví.<br>Por otro lado, el receptor se encuentra fuera del límite del<br>Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte (Área Rural). |

**Tabla 25.: Receptores discretos parte 4**

| ID | Coordenadas UTM [m]<br>(WGS84-H19S) | Col3 | Descripción | Col5 |
| --- | --- | --- | --- | --- |
| ID | X: Este | X: Este | X: Este | X: Este |
| R23 | 272.529 | 6.383.695 | Receptor olor 7 | Receptor 23, corresponde a una vivienda existente fuera<br>del límite urbano del Plan Regulador Comunal de<br>Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona de<br>extensión urbana 3 (ZEU 23 B). |
| R24 | 272.543 | 6.383.117 | Receptor olor 8 | Receptor 24, corresponde a una vivienda existente fuera<br>del límite urbano del Plan Regulador Comunal de<br>Puchuncaví,<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona de<br>extensión urbana 3 (ZEU 23 B). |
| R25 | 272.512 | 6.382.513 | Receptor olor 9 | Receptor 25, Centro comercial Pronto Copec, fuera del<br>límite<br>urbano<br>del<br>Plan<br>Regulador<br>Comunal<br>de<br>Puchuncaví.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona de<br>extensión urbana 3 (ZEU 23 B). |
| R26 | 274.379 | 6.377.371 | Estación Puchuncaví | Receptor 26, Estación meteorológica y calidad del aire<br>Puchuncaví, se encuentra dentro del límite urbano del<br>Plan Regulador Comunal de Putaendo, específicamente<br>en la zona Z4.<br>Por otro lado, el receptor se encuentra dentro del límite<br>del Plan Regulador Intercomunal de Valparaíso -Satélite<br>Borde Costero Norte, específicamente en la zona área<br>urbana (AU). |

**Tabla 26.: Coordenadas de ubicación estaciones meteorológicas superficiales**

| ID | Nombre<br>estación | Distancia hacia<br>proyecto [km] | Coordenadas UTM [m] WGS-84 Huso 19 Sur | Col5 |
| --- | --- | --- | --- | --- |
| ID | Nombre<br>estación | Distancia hacia<br>proyecto [km] | X: Este | Y: Sur |
| 1 <br>2 <br>3 | Puchuncaví<br>La Greda<br>Ventanas | 7,32<br>11,43<br>11,09 | 274.379<br>268.185<br>267.546 | 6.377.331<br>6.373.910<br>6.374.609 |

**Tabla 27.: Porcentaje de datos validados en estaciones meteorológicas superficiales**

| ID | Nombre | % de datos válidos por variable meteorológica | Col4 |
| --- | --- | --- | --- |
| ID | Nombre | Dirección del viento | Velocidad del viento |
| 1 <br>2 <br>3 | Puchuncaví<br>La Greda<br>Ventanas | 99,74%<br>99,60%<br>99,24% | 92,98%<br>87,43%<br>97,96% |

**Tabla 28.: Rosa de viento ciclo anual modelada y observada Estación Puchuncaví**

| Col1 | Modelado | Col3 | Observado | Col5 |
| --- | --- | --- | --- | --- |
| Anual |  |  |  |  |
| Anual | Promedio velocidad | 1,43 [m/s] | Promedio velocidad | 1,16 [m/s] |
| Anual | Frec. calmas | 26,42 % | Frec. calmas | 25,37 % |

**Tabla 29.: Rosas de viento anual horario Estación Puchuncaví**

| Col1 | Modelado | Col3 | Col4 | Observado | Col6 | Col7 | Escala |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |  |
| Anual Nocturno | Anual Nocturno | Anual Nocturno | Anual Nocturno | Anual Nocturno | Anual Nocturno | Anual Nocturno | Anual Nocturno |
| Anual Nocturno | Promedio | 0,58 [m/s] | 0,58 [m/s] | Promedio | 0,47 [m/s] | 0,47 [m/s] |  |
| Anual Nocturno | Frec. calmas<br> | 35,75 %<br> | 35,75 %<br> | Frec. calmas<br> | 40,50 %<br> | 40,50 %<br> | 40,50 %<br> |
|  | ~~Modelado~~ | ~~Modelado~~ | ~~Modelado~~ | ~~Observado~~ | ~~Observado~~ | ~~Observado~~ | ~~Escala~~ |
| Anual AM |  |  |  |  |  |  |  |
| Anual AM | Promedio | Promedio | 1,72 [m/s] | Promedio | Promedio | 1,70 [m/s] |  |
| Anual AM | Frec. calmas<br> | Frec. calmas<br> | 26,61 %<br> | Frec. calmas<br> | Frec. calmas<br> | 14,45 %<br> | 14,45 %<br> |
|  | ~~Modelado~~ | ~~Modelado~~ | ~~Modelado~~ | ~~Observado~~ | ~~Observado~~ | ~~Observado~~ | ~~Escala~~ |
| Anual PM |  |  |  |  |  |  |  |
| Anual PM | Promedio | 1,82 [m/s] | 1,82 [m/s] | Promedio | 1,14 [m/s] | 1,14 [m/s] |  |
| Anual PM | Frec. calmas | 19,45 % | 19,45 % | Frec. calmas | 25,02 % | 25,02 % | 25,02 % |

**Tabla 30.: Rosa de viento ciclo anual modelada y observada Estación La Greda**

| Col1 | Modelado | Col3 | Observado | Col5 |
| --- | --- | --- | --- | --- |
| Anual |  |  |  |  |
| Anual | Promedio velocidad | 1,29 [m/s] | Promedio velocidad | 1,47 [m/s] |
| Anual | Frec. calmas | 24,58 % | Frec. calmas | 19,17 % |

**Tabla 31.: Rosas de viento anual horario - Estación La Greda**

| Col1 | Modelado | Col3 | Observado | Col5 | Escala |
| --- | --- | --- | --- | --- | --- |
| Anual Nocturno |  |  |  |  | <br> |
| Anual Nocturno | Promedio | 0,60 [m/s] | Promedio | 0,52 [m/s] | 0,52 [m/s] |
| Anual Nocturno | Frec. calmas<br> | 35,80 %<br> | Frec. calmas<br> | 34,57 %<br> | 34,57 %<br> |
|  | ~~Modelado ~~ | ~~Modelado ~~ | ~~Observado ~~ | ~~Observado ~~ | ~~Escala ~~ |
| Anual AM |  |  |  |  | <br> |
| Anual AM | Promedio | 1,54 [m/s] | Promedio | 2,15 [m/s] | 2,15 [m/s] |
| Anual AM | Frec. calmas<br> | 23,80 %<br> | Frec. calmas<br> | 6,82 %<br> | 6,82 %<br> |
|  | ~~Modelado~~ | ~~Modelado~~ | ~~Observado~~ | ~~Observado~~ | ~~Escala~~ |
| Anual PM |  |  |  |  |  |
| Anual PM | Promedio | 1,59 [m/s] | Promedio | 1,54 [m/s] | 1,54 [m/s] |
| Anual PM | Frec. calmas | 16,89 % | Frec. calmas | 17,75 % | 17,75 % |

**Tabla 32.: Rosa de viento ciclo anual modelada y observada Estación Ventanas**

| Col1 | Modelado | Col3 | Observado | Col5 |
| --- | --- | --- | --- | --- |
| Anual |  |  |  |  |
| Anual | Promedio velocidad | 1,53 [m/s] | Promedio velocidad | 1,99 [m/s] |
| Anual | Frec. calmas | 19,11 % | Frec. calmas | 6,83 % |

**Tabla 33.: Rosas de viento anual horario - Estación Ventanas**

| Col1 | Modelado | Col3 | Observado | Col5 | Escala |
| --- | --- | --- | --- | --- | --- |
| Anual Nocturno |  |  |  |  | <br> |
| Anual Nocturno | Promedio | 0,78 [m/s] | Promedio | 1,20 [m/s] | 1,20 [m/s] |
| Anual Nocturno | % calmas<br> | 28,22 %<br> | % calmas<br> | 9,63 %<br> | 9,63 %<br> |
|  | ~~Modelado~~ | ~~Modelado~~ | ~~Observado~~ | ~~Observado~~ | ~~Escala~~ |
| Anual AM |  |  |  |  | <br> |
| Anual AM | Promedio | 1,82 [m/s] | Promedio | 2,50 [m/s] | 2,50 [m/s] |
| Anual AM | % calmas<br> | 17,67 %<br> | % calmas<br> | 5,68 %<br> | 5,68 %<br> |
|  | ~~Modelado~~ | ~~Modelado~~ | ~~Observado~~ | ~~Observado~~ | ~~Escala~~ |
| Anual PM |  |  |  |  |  |
| Anual PM | Promedio | 1,75 [m/s] | Promedio | 2,06 [m/s] | 2,06 [m/s] |
| Anual PM | % calmas | 14,79 % | % calmas | 6,06 % | 6,06 % |

**Tabla 34: Estadísticos velocidad del viento**

| Estadísticos | Puchuncaví | La Greda | Ventanas |
| --- | --- | --- | --- |
| RMSE<br>NRMSD<br>NMAE<br>BIAS<br>Coeficiente Correlación<br>IOA | 1,07<br>0.15<br>0.10<br>0.32<br>0,73<br>0,81 | 0,85<br>0,14<br>0,10<br>-0,10<br>0,76<br>0,79 | 1.02<br>0.12<br>0.09<br>-0,45<br>0.77<br>0.79 |

**Tabla 35: Estadísticos dirección del viento**

| Estadísticos | Puchuncaví | La Greda | Ventanas |
| --- | --- | --- | --- |
| Error Grueso<br>BIAS | 36<br>28 | 40<br>-15 | 32<br>5 |

**Tabla 36.: Escenarios modelación**

| Escenarios<br>modelación | Fuentes |
| --- | --- |
| E1:<br>Escenario 1 | Proyecto Maitencillo Etapa 1 |
| E1:<br>Escenario 1 | -PEAS 1, PEAS 2, PEAS 3 e impulsiones |
| E1:<br>Escenario 1 | -PEAS 5.1 e impulsión |
| E1:<br>Escenario 1 | -PEAS 5.2 e impulsión |
| E1:<br>Escenario 1 | -Red Primaria de A.S. |
| E1:<br>Escenario 1 |  |
| E1:<br>Escenario 1 | Sistema Planta de Tratamiento |
| E1:<br>Escenario 1 | -Proyecto PTAS Maitencillo Etapa 1 |
| E2:<br>Escenario 2 | Proyecto Maitencillo Etapa 2 |
| E2:<br>Escenario 2 | -PEAS 6, PEAS 7, PEAS 8 e impulsiones |
| E2:<br>Escenario 2 | -Red Primaria de A.S. |
| E3:<br>Escenario 3 | Proyecto Maitencillo Etapa 3 |
| E3:<br>Escenario 3 | -PEAS 9, PEAS 10 e impulsiones |
| E4:<br>Escenario 4 | Proyecto Maitencillo Etapa 4 |
| E4:<br>Escenario 4 | -Red Primaria de A.S. |
| E4:<br>Escenario 4 |  |
| E4:<br>Escenario 4 | Sistema Planta de Tratamiento |
| E4:<br>Escenario 4 | -Proyecto PTAS Maitencillo Etapa 2 |
| E5:<br>Escenario 5 | Sistema Planta de Tratamiento |
| E5:<br>Escenario 5 | -Proyecto PTAS Maitencillo Etapa 3 |

**Tabla 37.: Norma MP 2,5 [μg/m [3] ] - Promedio 24 horas - Percentil 98**

| Escenario | Criterio<br>Normativo | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | 50<br>[μg/m3] | 0,05 | 0,06 | 0,71 | 0,08 | 0,19 | 0,18 | 2,08 | 0,17 | 0,65 | 0,69 | 4,29 | 0,83 | 4,38 | 0,09 | 0,05 | 3,40 | 0,42 | 0,56 | 0,41 | 0,41 | 1,39 | 0,59 | 0,29 | 0,14 | 0,12 |
| E2 | E2 | 0,63 | 0,88 | 0,13 | 0,12 | 0,02 | 0,04 | 0,03 | 0,03 | 0,03 | 0,04 | 0,03 | 0,04 | 0,05 | 1,76 | 0,33 | 0,02 | 0,03 | 0,02 | 0,02 | 0,02 | 0,01 | 0,01 | 0,04 | 0,05 | 0,03 |
| E3 | E3 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,03 | 0,20 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01 | 0,01 | 0,01 |
| E4 | E4 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,02 | 0,11 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01 | 0,00 | 0,00 | 0,01 | 0,01 |
| E5 | E5 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,02 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 |

**Tabla 38.: Norma MP 2,5 [μg/m [3] ] - Promedio Anual**

| Escenario | Criterio<br>Normativo | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | 20<br>[μg/m3] | 0,12 | 0,13 | 1,44 | 0,16 | 0,38 | 0,37 | 4,19 | 0,34 | 1,31 | 1,38 | 8,64 | 1,68 | 8,83 | 0,18 | 0,10 | 6,83 | 0,87 | 1,14 | 0,84 | 0,83 | 2,79 | 1,18 | 0,58 | 0,28 | 0,26 |
| E2 | E2 | 0,05 | 0,11 | 0,01 | 0,01 | 0,00 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,17 | 0,03 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E3 | E3 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,02 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E4 | E4 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,02 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E5 | E5 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |

**Tabla 39.: Norma MP 10 [μg/m [3] ] - Promedio 24 horas - Percentil 98**

| Escenario | Criterio<br>Normativo | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | 130<br>[μg/m3] | 0,12 | 0,13 | 1,44 | 0,16 | 0,38 | 0,37 | 4,19 | 0,34 | 1,31 | 1,38 | 8,64 | 1,68 | 8,83 | 0,18 | 0,10 | 6,83 | 0,87 | 1,14 | 0,84 | 0,83 | 2,79 | 1,18 | 0,58 | 0,28 | 0,26 |
| E2 | E2 | 1,29 | 1,78 | 0,26 | 0,24 | 0,04 | 0,09 | 0,06 | 0,06 | 0,07 | 0,07 | 0,07 | 0,08 | 0,10 | 3,55 | 0,67 | 0,05 | 0,05 | 0,04 | 0,04 | 0,03 | 0,02 | 0,02 | 0,08 | 0,09 | 0,07 |
| E3 | E3 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01 | 0,01 | 0,00 | 0,00 | 0,00 | 0,06 | 0,41 | 0,01 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01 | 0,01 | 0,01 |
| E4 | E4 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01 | 0,00 | 0,00 | 0,00 | 0,03 | 0,23 | 0,02 | 0,01 | 0,01 | 0,01 | 0,01 | 0,01 | 0,00 | 0,01 | 0,01 | 0,01 |
| E5 | E5 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,02 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 |

**Tabla 40.: Norma MP 10 [μg/m [3] ] - Promedio Anual**

| Escenario | Criterio<br>Normativo | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | 50<br>[μg/m3] | 0,02 | 0,03 | 0,16 | 0,03 | 0,03 | 0,03 | 0,31 | 0,08 | 0,16 | 0,16 | 1,00 | 0,15 | 0,86 | 0,03 | 0,01 | 0,87 | 0,13 | 0,15 | 0,13 | 0,11 | 0,39 | 0,17 | 0,11 | 0,07 | 0,04 |
| E2 | E2 | 0,11 | 0,23 | 0,02 | 0,02 | 0,00 | 0,01 | 0,01 | 0,01 | 0,01 | 0,01 | 0,01 | 0,01 | 0,01 | 0,35 | 0,06 | 0,00 | 0,01 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01 | 0,01 | 0,01 |
| E3 | E3 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,04 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E4 | E4 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,03 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E5 | E5 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |

**Tabla 41.: Norma primaria SO 2 [μg/m [3] ] - Promedio 1 hora - Percentil 98,5**

| Escenario | Criterio<br>Normativo | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | 350<br>[μg/m3] | 0,08 | 0,10 | 0,10 | 0,05 | 0,01 | 0,02 | 0,01 | 0,01 | 0,01 | 0,02 | 0,01 | 0,01 | 0,00 | 0,00 | 0,00 | 0,15 | 0,02 | 0,02 | 0,02 | 0,05 | 0,01 | 0,02 | 0,01 | 0,03 | 0,07 |
| E2 | E2 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E3 | E3 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E4 | E4 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E5 | E5 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |

**Tabla 42.: Norma primaria SO 2 [μg/m [3] ] - Promedio 24 horas - Percentil 99**

| Escenario | Criterio<br>Normativo | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | 150<br>[μg/m3] | 0,03 | 0,03 | 0,03 | 0,02 | 0,00 | 0,01 | 0,00 | 0,00 | 0,00 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,07 | 0,01 | 0,01 | 0,01 | 0,02 | 0,01 | 0,01 | 0,01 | 0,01 | 0,03 |
| E2 | E2 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E3 | E3 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E4 | E4 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E5 | E5 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |

**Tabla 43.: Norma primaria SO 2 [μg/m [3] ] - Promedio Anual**

| Escenario | Criterio<br>Normativo | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | 60<br>[μg/m3] | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E2 | E2 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E3 | E3 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E4 | E4 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E5 | E5 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |

**Tabla 44.: Norma secundaria SO 2 [μg/m [3] ] - Promedio 1 hora - Percentil 99,73**

| Escenario | Criterio<br>Normativo | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | 1.000<br>[μg/m3] | 0,15 | 0,14 | 0,13 | 0,10 | 0,02 | 0,02 | 0,01 | 0,01 | 0,01 | 0,03 | 0,02 | 0,01 | 0,01 | 0,00 | 0,00 | 0,19 | 0,03 | 0,03 | 0,03 | 0,07 | 0,02 | 0,03 | 0,02 | 0,05 | 0,12 |
| E2 | E2 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E3 | E3 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E4 | E4 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E5 | E5 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |

**Tabla 45.: Norma secundaria SO 2 [μg/m [3] ] - Promedio 24 horas - Percentil 99,7**

| Escenario | Criterio<br>Normativo | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | 365<br>[μg/m3] | 0,03 | 0,05 | 0,04 | 0,03 | 0,01 | 0,01 | 0,01 | 0,00 | 0,00 | 0,01 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,08 | 0,01 | 0,01 | 0,01 | 0,02 | 0,01 | 0,01 | 0,01 | 0,02 | 0,03 |
| E2 | E2 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E3 | E3 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E4 | E4 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E5 | E5 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |

**Tabla 46.: Norma secundaria SO 2 [μg/m [3] ] - Promedio Anual**

| Escenario | Criterio<br>Normativo | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | 80<br>[μg/m3] | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E2 | E2 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E3 | E3 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E4 | E4 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E5 | E5 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |

**Tabla 47.: Norma primaria CO [mg/m [3] ] - Promedio 8 hora - Percentil 99**

| Escenario | Criterio<br>Normativo | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | 10<br>[mg/m3] | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E2 | E2 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E3 | E3 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E4 | E4 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E5 | E5 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |

**Tabla 48.: Norma primaria CO [mg/m [3] ] - Promedio 1 hora - Percentil 99**

| Escenario | Criterio<br>Normativo | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | 30<br>[mg/m3] | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E2 | E2 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E3 | E3 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E4 | E4 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E5 | E5 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |

**Tabla 49.: Norma primaria NO 2 [ug/m [3] ] - Promedio 1 hora - Percentil 99**

| Escenario | Criterio<br>Normativo | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | 10<br>[mg/m3] | 0,28 | 0,30 | 0,36 | 0,41 | 0,33 | 0,44 | 0,67 | 3,24 | 1,63 | 0,71 | 0,27 | 0,24 | 0,29 | 0,33 | 0,40 | 0,77 | 0,77 | 0,59 | 0,50 | 0,68 | 0,58 | 0,38 | 0,51 | 0,43 | 0,37 |
| E2 | E2 | 0,02 | 0,03 | 0,03 | 0,04 | 0,02 | 0,03 | 0,04 | 0,52 | 0,22 | 0,05 | 0,02 | 0,01 | 0,02 | 0,03 | 0,02 | 0,05 | 0,06 | 0,05 | 0,05 | 0,06 | 0,04 | 0,02 | 0,03 | 0,02 | 0,01 |
| E3 | E3 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,04 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E4 | E4 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01 | 0,00 | 0,01 | 0,01 | 0,02 | 0,03 | 0,01 | 0,00 | 0,00 | 0,00 |
| E5 | E5 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 |

**Tabla 50.: Norma primaria NO 2 [μg/m [3] ] - Promedio Anual**

| Escenario | Criterio<br>Normativo | R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20 | R21 | R22 | R23 | R24 | R25 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E1 | 30<br>[mg/m3] | 0,01 | 0,01 | 0,01 | 0,01 | 0,00 | 0,00 | 0,01 | 0,11 | 0,06 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01 | 0,01 | 0,01 | 0,01 | 0,01 | 0,01 | 0,01 | 0,01 | 0,00 | 0,00 |
| E2 | E2 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,01 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E3 | E3 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E4 | E4 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |
| E5 | E5 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 | 0,00 |

**Tabla 51.: Aumento de las concentraciones basales en EMRP Puchuncaví**

| Contaminante | Tipo | Estadísticos | Medido<br>EMRP<br>Puchuncaví<br>[μg/m3] | Modelado EMRP Puchuncaví [μg/m3] | Col6 | Col7 | Col8 | Col9 | Total Aporte proyecto + línea base [μg/m3] | Col11 | Col12 | Col13 | Col14 | Límite<br>Norma |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contaminante | Tipo | Estadísticos | Medido<br>EMRP<br>Puchuncaví<br>[μg/m3] | E1 | E2 | E3 | E4 | E5 | E1 | E2 | E3 | E4 | E5 | E5 |
| MP2,5 | Primaria | Percentil<br>98-24 horas | 30.66 | 0.0396344 | 0.0046487 | 0.0007975 | 0.0005594 | 0.00030196 | 30.70 | 30.66 | 30.66 | 30.66 | 30.66 | 50 |
| MP2,5 | Primaria | Promedio<br>Anual | 14.85 | 0.0071685 | 0.0003239 | 0.0000732 | 0.0000898 | 0.00003930 | 14.86 | 14.85 | 14.85 | 14.85 | 14.85 | 20 |
| MP10 | Primaria | Percentil<br>98-24 horas | 68.38 | 0.0826615 | 0.0095187 | 0.0003556 | 0.0011344 | 0.00031078 | 68.46 | 68.39 | 68.38 | 68.38 | 68.38 | 130 |
| MP10 | Primaria | Promedio<br>Anual | 41.05 | 0.0174626 | 0.0007197 | 0.0000308 | 0.0001836 | 0.00004252 | 41.07 | 41.05 | 41.05 | 41.05 | 41.05 | 50 |
| SO2 | Primaria | Percentil<br>98,5-1 hora | 57.86 | 0.0626492 | 0.0001855 | 0.0000555 | 0.0001975 | 0.00002125 | 57.92 | 57.86 | 57.86 | 57.86 | 57.86 | 350 |
| SO2 | Primaria | Percentil<br>99-24 horas | 28.89 | 0.0236960 | 0.0001591 | 0.0000476 | 0.0000844 | 0.00001238 | 28.91 | 28.89 | 28.89 | 28.89 | 28.89 | 150 |
| SO2 | Primaria | Promedio<br>Anual | 14.85 | 0.0029110 | 0.0000128 | 0.0000038 | 0.0000157 | 0.00000178 | 14.85 | 14.85 | 14.85 | 14.85 | 14.85 | 60 |
| SO2 | Secundaria | Percentil<br>99,73-1 | 81.74 | 0.1142482 | 0.0005695 | 0.0001705 | 0.0005422 | 0.00004562 | 81.85 | 81.74 | 81.74 | 81.74 | 81.74 | 1.000 |
| SO2 | Secundaria | Percentil<br>99,7-24 | 31.97 | 0.0322760 | 0.0002784 | 0.0000833 | 0.0001326 | 0.0000216 | 32.00 | 31.97 | 31.97 | 31.97 | 31.97 | 365 |
| SO2 | Secundaria | Promedio<br>Anual | 14.08 | 0.0029319 | 0.0000127 | 0.0000038 | 0.0000156 | 0.00000176 | 14.08 | 14.08 | 14.08 | 14.08 | 14.08 | 80 |
| NO2 | Primaria | Percentil 99<br>máximos<br>diarios | 54.52 | 0.1291323 | 0.0087953 | 0.0019608 | 0.0028024 | 0.00073896 | 54.65 | 54.53 | 54.52 | 54.52 | 54.52 | 400 |
| NO2 | Primaria | Promedio<br>tri anual | 14.77 | 0.0025209 | 0.0000737 | 0.0000120 | 0.0000445 | 0.00000904 | 14.77 | 14.77 | 14.77 | 14.77 | 14.77 | 100 |

**Tabla 52.: Escenarios modelación MPS**

| Escenario<br>modelación | Fuentes |
| --- | --- |
| E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción) | Proyecto Maitencillo Etapa 1 |
| E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción) | -PEAS 1, PEAS 2, PEAS 3 e impulsiones |
| E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción) | -PEAS 5.1 e impulsión |
| E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción) | -PEAS 5.2 e impulsión |
| E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción) | -Red Primaria de A.S. |
| E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción) |  |
| E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción) | Sistema Planta de Tratamiento |
| E1:<br>Escenario 1<br>(Fase<br>de<br>contrucción) | -Proyecto PTAS Maitencillo Etapa 1 |

**Tabla 53: MPS como concentración media aritmética anual.**

| ID Receptor | Concentración<br>media aritmética<br>anual.<br>[mg/m2 día] | Límite<br>OAPC Suiza |
| --- | --- | --- |
| Receptor 1<br> | ~~0,0096~~<br> | 200 [mg/m2 día]<br>Media Aritmética<br>Anual |
| ~~Receptor 2~~ | ~~0,0106~~<br> | ~~0,0106~~<br> |
| Receptor 3<br> | ~~0,1056~~<br> | ~~0,1056~~<br> |
| ~~Receptor 4~~ | ~~0,0146~~<br> | ~~0,0146~~<br> |
| Receptor 5 | ~~0,0148~~<br> | ~~0,0148~~<br> |
| Receptor 6 | ~~0,0165~~<br> | ~~0,0165~~<br> |
| Receptor 7 | ~~0,3365~~<br> | ~~0,3365~~<br> |
| Receptor 8<br> | ~~0,0422~~<br> | ~~0,0422~~<br> |
| ~~Receptor 9~~ | ~~0,1273~~<br> | ~~0,1273~~<br> |
| Receptor 10 | ~~0,2440~~<br> | ~~0,2440~~<br> |
| Receptor 11<br> | ~~0,8176~~<br> | ~~0,8176~~<br> |
| ~~Receptor 12~~ | ~~0,2595~~<br> | ~~0,2595~~<br> |
| Receptor 13<br> | ~~0,7156~~<br> | ~~0,7156~~<br> |
| ~~Receptor 14~~ | ~~0,0118~~<br> | ~~0,0118~~<br> |
| Receptor 15<br> | ~~0,0057~~<br> | ~~0,0057~~<br> |
| ~~Receptor 16~~ | ~~0,4373~~<br> | ~~0,4373~~<br> |
| Receptor 17 | ~~0,0876~~<br> | ~~0,0876~~<br> |
| Receptor 18<br> | ~~0,1306~~<br> | ~~0,1306~~<br> |
| ~~Receptor 19~~ | ~~0,1138~~<br> | ~~0,1138~~<br> |
| Receptor 20<br> | ~~0,0571~~<br> | ~~0,0571~~<br> |
| ~~Receptor 21~~ | ~~0,4261~~<br> | ~~0,4261~~<br> |
| Receptor 22 | ~~0,0828~~<br> | ~~0,0828~~<br> |
| Receptor 23<br> | ~~0,1111~~<br> | ~~0,1111~~<br> |
| ~~Receptor 24~~ | ~~0,0363~~<br> | ~~0,0363~~<br> |
| Receptor 25<br> | ~~0,0165~~<br> | ~~0,0165~~<br> |
| ~~Receptor 26~~ | ~~0,0122~~ | ~~0,0122~~ |

**Tabla 54: Valores de significancia para el aumento de concentraciones de MP 10 y MP 2,5 sobre**

| DURACIÓN IMPACTO | Col2 | Col3 | MP [μg/m3]<br>10 | Col5 | MP [μg/m3]<br>2,5 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Año | Mes | Proporcional (años) | 24 horas | Anual | 24 horas | Anual |
| **1 ** | 1 | 0,1 | 10,00 | 10,00 | 10,00 | 10,00 |
| **1 ** | 2 | 0,2 | 10,00 | 10,00 | 10,00 | 5,94 |
| **1 ** | 3 | 0,3 | 10,00 | 10,00 | 10,00 | 3,96 |
| **1 ** | 4 | 0,3 | 10,00 | 9,00 | 10,00 | 2,97 |
| **1 ** | 5 | 0,4 | 10,00 | 7,20 | 10,00 | 2,38 |
| **1 ** | 6 | 0,5 | 10,00 | 6,00 | 10,00 | 1,98 |
| **1 ** | 7 | 0,6 | 10,00 | 5,14 | 8,79 | 1,70 |
| **1 ** | 8 | 0,7 | 10,00 | 4,50 | 7,70 | 1,49 |
| **1 ** | 9 | 0,8 | 10,00 | 4,00 | 6,84 | 1,32 |
| **1 ** | 10 | 0,8 | 10,00 | 3,60 | 6,16 | 1,19 |
| **1 ** | 11 | 0,9 | 10,00 | 3,27 | 5,60 | 1,08 |
| **1 ** | **12** | **1,0** | **10,00** | **3,00** | **5,13** | **0,99** |

**Tabla 55: Valores de significancia para el aumento de concentraciones de MP 10**

| Contaminante | Duración<br>Impacto | Unidad | Tipo | Límite | R13 | R11 |
| --- | --- | --- | --- | --- | --- | --- |
| MP2.5 | 1 año | [μg/m3] | 24 horas | 5.13 | 4.38 | 4.29 |
| MP2.5 | 1 año | [μg/m3] | Anual | 0.99 | 0.43 | 0.50 |

**Tabla 57.: Fuentes de Emisión - Escenario 1 parte 1**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_1 | Peas_1 | 270862 | 6384348 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_2 | Peas_2 | 271312 | 6385052 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_3 | Peas_3 | 272644 | 6386732 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_4 | Peas_5.1 | 271757 | 6385539 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_5 | Peas_5.2 | 272602 | 6384124 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_6 | Colec_1.1 | 270894 | 6383950 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_7 | Colec_1.2 | 270876 | 6384052 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_8 | Colec_1.3 | 270873 | 6384151 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_9 | Colec_1.4 | 270873 | 6384253 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_10 | Col_1_2.1 | 270931 | 6384850 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_11 | Col_1_2.2 | 271016 | 6384942 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_12 | Col_1_2.3 | 271106 | 6384990 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_13 | Col_1_2.4 | 271203 | 6385001 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_14 | Colec_2.1 | 271534 | 6385454 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_15 | Colec_2.2 | 271640 | 6385468 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_16 | Colec_2.3 | 271734 | 6385512 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_17 | Colec_5.1.1 | 271798 | 6385551 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_18 | Colec_5.1.2 | 271860 | 6385633 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_19 | Colec_5.1.3 | 271915 | 6385715 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_20 | Colec_5.1.4 | 271973 | 6385798 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_21 | Colec_5.1.5 | 272032 | 6385882 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_22 | Colec_5.1.6 | 272063 | 6385983 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_23 | Colec_5.1.7 | 272071 | 6386082 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_24 | Colec_5.1.8 | 272080 | 6386180 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_25 | Colec_5.1.9 | 272092 | 6386283 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_26 | Colec_5.1.10 | 272101 | 6386381 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_27 | Colec_5.1.11 | 272112 | 6386484 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |

**Tabla 58.: Fuentes de Emisión - Escenario 1 parte 2**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_28 | Colec_5.1.12 | 272122 | 6386584 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_29 | Colec_5.1.13 | 272132 | 6386683 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_30 | Colec_5.1.14 | 272171 | 6386767 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_31 | Colec_5.1.15 | 272225 | 6386788 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_32 | Imp_1.1 | 270869 | 6384373 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_33 | Imp_1.2 | 270883 | 6384472 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_34 | Imp_1.3 | 270915 | 6384567 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_35 | Imp_1.4 | 270907 | 6384662 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_36 | Imp_1.5 | 270863 | 6384741 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_37 | Imp_2.1 | 271310 | 6385050 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_38 | Imp_2.2 | 271349 | 6385137 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_39 | Imp_2.3 | 271379 | 6385235 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_40 | Imp_2.4 | 271425 | 6385313 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_41 | Imp_2.5 | 271473 | 6385362 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_42 | Imp_3.1 | 272362 | 6386742 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_43 | Imp_3.2 | 272478 | 6386683 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_44 | Imp_3.3 | 272646 | 6386701 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_45 | Imp_5.1.1 | 271781 | 6385537 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_46 | Imp_5.1.2 | 271876 | 6385511 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_47 | Imp_5.1.3 | 271846 | 6385422 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_48 | Imp_5.1.4 | 271858 | 6385339 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_49 | Imp_5.1.5 | 271954 | 6385328 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_50 | Imp_5.1.6 | 272056 | 6385329 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_51 | Imp_5.1.7 | 272156 | 6385329 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_52 | Imp_5.1.8 | 272220 | 6385336 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_53 | Imp_5.1.9 | 272311 | 6385344 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_54 | Imp_5.1.10 | 272285 | 6385236 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_55 | Imp_5.1.11 | 272304 | 6385134 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_56 | Imp_5.1.12 | 272336 | 6385038 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_57 | Imp_5.1.13 | 272407 | 6384841 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_58 | Imp_5.1.14 | 272372 | 6384937 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_59 | Imp_5.1.15 | 272450 | 6384738 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |

**Tabla 59.: Fuentes de Emisión - Escenario 1 parte 3**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_60 | Imp_5.1.16 | 272488 | 6384641 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_61 | Imp_5.1.17 | 272524 | 6384542 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_62 | Imp_5.1.18 | 272555 | 6384455 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_63 | Imp_5.1.19 | 272599 | 6384360 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_64 | Imp_5.1.20 | 272630 | 6384265 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_65 | Imp_5.2.1 | 272632 | 6384030 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_66 | Imp_5.2.2 | 272629 | 6383932 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_67 | Imp_5.2.3 | 272630 | 6383829 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_68 | Imp_5.2.4 | 272630 | 6383727 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_69 | Imp_5.2.5 | 272640 | 6383641 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_70 | Imp_5.2.6 | 272746 | 6383639 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_71 | Imp_5.2.7 | 272851 | 6383632 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_72 | Imp_5.2.8 | 272942 | 6383633 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_73 | Imp_5.2.9 | 273063 | 6383633 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_74 | Imp_5.2.10 | 273174 | 6383643 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_75 | Imp_5.2.11 | 273241 | 6383541 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_76 | Imp_5.2.12 | 273289 | 6383443 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_77 | Imp_5.2.13 | 273365 | 6383370 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_78 | Imp_5.2.14 | 273435 | 6383287 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_79 | Imp_5.2.15 | 273517 | 6383233 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_80 | Imp_5.2.16 | 273550 | 6383131 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_81 | IF_1_Redes | 272317 | 6384978 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_82 | IF_2_PTAS | 273520 | 6383274 | 10 meses | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_83 | Tub_1.1 | 272633 | 6383633 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_84 | Tub_1.2 | 272635 | 6383539 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_85 | Tub_1.3 | 272525 | 6383555 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_86 | Tub_1.4 | 272458 | 6383630 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_87 | Tub_1.5 | 272378 | 6383683 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_88 | Tub_1.6 | 272300 | 6383735 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_89 | Tub_1.7 | 272197 | 6383722 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_90 | Tub_1.8 | 272122 | 6383755 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_91 | Tub_1.9 | 272060 | 6383844 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |

**Tabla 60.: Fuentes de Emisión - Escenario 1 parte 4**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_92 | Tub_1.10 | 271961 | 6383846 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_93 | Tub_1.11 | 271862 | 6383794 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_94 | Tub_1.12 | 271766 | 6383745 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_95 | Tub_1.13 | 271669 | 6383720 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_96 | Tub_1.14 | 271564 | 6383688 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_97 | Tub_1.15 | 271501 | 6383601 | 1 mes | 4,00 | 2,33,E-03 | 1,16,E-03 | 0,01103 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_98 | Tub_1.16 | 271424 | 6383524 | 1 mes | 4,00 | 2,3,E-03 | 1,2,E-03 | 1,1,E-02 | 0,0,E+00 | 0,0,E+00 | 0,0,E+00 |
| AREA | SRC_99 | Tub_1.17 | 271369 | 6383436 | 1 mes | 4,00 | 2,3,E-03 | 1,2,E-03 | 1,1,E-02 | 0,0,E+00 | 0,0,E+00 | 0,0,E+00 |
| AREA | SRC_100 | Tub_1.18 | 271340 | 6383353 | 1 mes | 4,00 | 2,3,E-03 | 1,2,E-03 | 1,1,E-02 | 0,0,E+00 | 0,0,E+00 | 0,0,E+00 |
| AREA | SRC_101 | Tub_1.19 | 271274 | 6383286 | 1 mes | 4,00 | 2,3,E-03 | 1,2,E-03 | 1,1,E-02 | 0,0,E+00 | 0,0,E+00 | 0,0,E+00 |
| AREA | SRC_102 | Tub_1.20 | 271248 | 6383193 | 1 mes | 4,00 | 2,3,E-03 | 1,2,E-03 | 1,1,E-02 | 0,0,E+00 | 0,0,E+00 | 0,0,E+00 |
| AREA | SRC_103 | Tub_1.21 | 271205 | 6383096 | 1 mes | 4,00 | 2,3,E-03 | 1,2,E-03 | 1,1,E-02 | 0,0,E+00 | 0,0,E+00 | 0,0,E+00 |
| AREA | SRC_209 | Cam_Cat_1-PEAS e Imp | 273043 | 6387323 | 3 mes | 383,32 | 8,7,E-08 | 2,1,E-08 | 2,6,E-08 | 4,6,E-08 | 4,6,E-08 | 1,1,E-08 |
| AREA | SRC_210 | Cam_Cat_2-PEAS e Imp | 273206 | 6387558 | 3 mes | 1145,03 | 2,9,E-08 | 7,0,E-09 | 8,6,E-09 | 1,5,E-08 | 1,5,E-08 | 3,6,E-09 |
| AREA | SRC_211 | Cam_Cat_3-PEAS e Imp | 273308 | 6387612 | 3 mes | 456,00 | 7,3,E-08 | 1,8,E-08 | 2,2,E-08 | 3,8,E-08 | 3,8,E-08 | 9,1,E-09 |
| AREA | SRC_212 | Cam_Cat_4-PEAS e Imp | 273511 | 6387668 | 3 mes | 843,57 | 3,9,E-08 | 9,5,E-09 | 1,2,E-08 | 2,1,E-08 | 2,1,E-08 | 4,9,E-09 |
| AREA | SRC_213 | Cam_Cat_5-PEAS e Imp | 273721 | 6387707 | 3 mes | 853,32 | 3,9,E-08 | 9,4,E-09 | 1,2,E-08 | 2,0,E-08 | 2,0,E-08 | 4,9,E-09 |
| AREA | SRC_214 | Cam_Cat_6-PEAS e Imp | 273880 | 6387880 | 3 mes | 945,26 | 3,5,E-08 | 8,5,E-09 | 1,0,E-08 | 1,8,E-08 | 1,8,E-08 | 4,4,E-09 |
| AREA | SRC_215 | Cam_Cat_7-PEAS e Imp | 273982 | 6387934 | 3 mes | 457,52 | 7,3,E-08 | 1,8,E-08 | 2,2,E-08 | 3,8,E-08 | 3,8,E-08 | 9,1,E-09 |
| AREA | SRC_216 | Cam_Cat_8-PEAS e Imp | 274178 | 6387916 | 3 mes | 782,20 | 4,2,E-08 | 1,0,E-08 | 1,3,E-08 | 2,2,E-08 | 2,2,E-08 | 5,3,E-09 |
| AREA | SRC_217 | Cam_Cat_9-PEAS e Imp | 274216 | 6387945 | 3 mes | 195,48 | 1,7,E-07 | 4,1,E-08 | 5,0,E-08 | 8,9,E-08 | 8,9,E-08 | 2,1,E-08 |
| AREA | SRC_218 | Cam_Cat_10-PEAS e Imp | 274213 | 6388017 | 3 mes | 295,61 | 1,1,E-07 | 2,7,E-08 | 3,3,E-08 | 5,9,E-08 | 5,9,E-08 | 1,4,E-08 |
| AREA | SRC_219 | Cam_Cat_11-PEAS e Imp | 274177 | 6388250 | 3 mes | 941,53 | 3,5,E-08 | 8,5,E-09 | 1,0,E-08 | 1,9,E-08 | 1,9,E-08 | 4,4,E-09 |
| AREA | SRC_220 | Cam_Cat_12-PEAS e Imp | 274185 | 6388365 | 3 mes | 458,34 | 7,2,E-08 | 1,8,E-08 | 2,1,E-08 | 3,8,E-08 | 3,8,E-08 | 9,1,E-09 |
| AREA | SRC_221 | Cam_Cat_13-PEAS e Imp | 274352 | 6388558 | 3 mes | 1016,92 | 3,3,E-08 | 7,9,E-09 | 9,7,E-09 | 1,7,E-08 | 1,7,E-08 | 4,1,E-09 |
| AREA | SRC_222 | Cam_Cat_14-PEAS e Imp | 274654 | 6388846 | 3 mes | 1667,00 | 2,0,E-08 | 4,8,E-09 | 5,9,E-09 | 1,0,E-08 | 1,0,E-08 | 2,5,E-09 |
| AREA | SRC_223 | Cam_Cat_15-PEAS e Imp | 274745 | 6388895 | 3 mes | 409,81 | 8,1,E-08 | 2,0,E-08 | 2,4,E-08 | 4,3,E-08 | 4,3,E-08 | 1,0,E-08 |
| AREA | SRC_224 | Cam_Cat_16-PEAS e Imp | 274834 | 6388862 | 3 mes | 371,12 | 9,0,E-08 | 2,2,E-08 | 2,7,E-08 | 4,7,E-08 | 4,7,E-08 | 1,1,E-08 |
| AREA | SRC_225 | Cam_Cat_17-PEAS e Imp | 274882 | 6388794 | 3 mes | 331,29 | 1,0,E-07 | 2,4,E-08 | 3,0,E-08 | 5,3,E-08 | 5,3,E-08 | 1,3,E-08 |
| AREA | SRC_226 | Cam_Cat_18-PEAS e Imp | 274979 | 6388768 | 3 mes | 406,63 | 8,2,E-08 | 2,0,E-08 | 2,4,E-08 | 4,3,E-08 | 4,3,E-08 | 1,0,E-08 |
| AREA | SRC_227 | Cam_Cat_19-PEAS e Imp | 275069 | 6388799 | 3 mes | 384,16 | 8,6,E-08 | 2,1,E-08 | 2,6,E-08 | 4,5,E-08 | 4,5,E-08 | 1,1,E-08 |
| AREA | SRC_228 | Cam_Cat_20-PEAS e Imp | 275059 | 6388911 | 3 mes | 459,52 | 7,2,E-08 | 1,7,E-08 | 2,1,E-08 | 3,8,E-08 | 3,8,E-08 | 9,0,E-09 |

**Tabla 61.: Fuentes de Emisión - Escenario 1 parte 5**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_229 | Cam_Cat_21-PEAS e Imp | 275040 | 6389003 | 3 mes | 374,05 | 8,9,E-08 | 2,1,E-08 | 2,6,E-08 | 4,7,E-08 | 4,7,E-08 | 1,1,E-08 |
| AREA | SRC_230 | Cam_Cat_22-PEAS e Imp | 274958 | 6389092 | 3 mes | 489,11 | 6,8,E-08 | 1,6,E-08 | 2,0,E-08 | 3,6,E-08 | 3,6,E-08 | 8,5,E-09 |
| AREA | SRC_231 | Cam_Cat_23-PEAS e Imp | 274915 | 6389184 | 3 mes | 402,20 | 8,3,E-08 | 2,0,E-08 | 2,4,E-08 | 4,3,E-08 | 4,3,E-08 | 1,0,E-08 |
| AREA | SRC_232 | Cam_Cat_24-PEAS e Imp | 274946 | 6389307 | 3 mes | 502,79 | 6,6,E-08 | 1,6,E-08 | 2,0,E-08 | 3,5,E-08 | 3,5,E-08 | 8,3,E-09 |
| AREA | SRC_233 | Cam_Cat_25-PEAS e Imp | 275049 | 6389374 | 3 mes | 485,06 | 6,8,E-08 | 1,7,E-08 | 2,0,E-08 | 3,6,E-08 | 3,6,E-08 | 8,6,E-09 |
| AREA | SRC_234 | Cam_Cat_26-PEAS e Imp | 275181 | 6389406 | 3 mes | 541,36 | 6,1,E-08 | 1,5,E-08 | 1,8,E-08 | 3,2,E-08 | 3,2,E-08 | 7,7,E-09 |
| AREA | SRC_235 | Cam_Cat_27-PEAS e Imp | 275286 | 6389385 | 3 mes | 424,34 | 7,8,E-08 | 1,9,E-08 | 2,3,E-08 | 4,1,E-08 | 4,1,E-08 | 9,8,E-09 |
| AREA | SRC_236 | Cam_Cat_28-PEAS e Imp | 275372 | 6389387 | 3 mes | 345,06 | 9,6,E-08 | 2,3,E-08 | 2,9,E-08 | 5,1,E-08 | 5,1,E-08 | 1,2,E-08 |
| AREA | SRC_237 | Cam_Cat_29-PEAS e Imp | 275519 | 6389442 | 3 mes | 633,26 | 5,2,E-08 | 1,3,E-08 | 1,6,E-08 | 2,8,E-08 | 2,8,E-08 | 6,6,E-09 |
| AREA | SRC_238 | Cam_Cat_30-PEAS e Imp | 275575 | 6389512 | 3 mes | 360,36 | 9,2,E-08 | 2,2,E-08 | 2,7,E-08 | 4,8,E-08 | 4,8,E-08 | 1,2,E-08 |
| AREA | SRC_239 | Cam_Cat_31-PEAS e Imp | 275579 | 6389623 | 3 mes | 447,31 | 7,4,E-08 | 1,8,E-08 | 2,2,E-08 | 3,9,E-08 | 3,9,E-08 | 9,3,E-09 |
| AREA | SRC_240 | Cam_Cat_32-PEAS e Imp | 275473 | 6389738 | 3 mes | 629,59 | 5,3,E-08 | 1,3,E-08 | 1,6,E-08 | 2,8,E-08 | 2,8,E-08 | 6,6,E-09 |
| AREA | SRC_241 | Cam_Cat_33-PEAS e Imp | 275397 | 6389809 | 3 mes | 419,18 | 7,9,E-08 | 1,9,E-08 | 2,3,E-08 | 4,2,E-08 | 4,2,E-08 | 9,9,E-09 |
| AREA | SRC_242 | Cam_Cat_34-PEAS e Imp | 275382 | 6389918 | 3 mes | 432,78 | 7,7,E-08 | 1,9,E-08 | 2,3,E-08 | 4,0,E-08 | 4,0,E-08 | 9,6,E-09 |
| AREA | SRC_243 | Cam_Cat_35-PEAS e Imp | 275487 | 6390018 | 3 mes | 576,65 | 5,8,E-08 | 1,4,E-08 | 1,7,E-08 | 3,0,E-08 | 3,0,E-08 | 7,2,E-09 |
| AREA | SRC_244 | Cam_Cat_36-PEAS e Imp | 275630 | 6390045 | 3 mes | 576,34 | 5,8,E-08 | 1,4,E-08 | 1,7,E-08 | 3,0,E-08 | 3,0,E-08 | 7,2,E-09 |
| AREA | SRC_245 | Cam_Cat_37-PEAS e Imp | 275763 | 6390025 | 3 mes | 532,94 | 6,2,E-08 | 1,5,E-08 | 1,8,E-08 | 3,3,E-08 | 3,3,E-08 | 7,8,E-09 |
| AREA | SRC_246 | Cam_Cat_38-PEAS e Imp | 275861 | 6389993 | 3 mes | 411,71 | 8,1,E-08 | 2,0,E-08 | 2,4,E-08 | 4,2,E-08 | 4,2,E-08 | 1,0,E-08 |
| AREA | SRC_247 | Cam_Cat_39-PEAS e Imp | 276044 | 6389963 | 3 mes | 742,87 | 4,5,E-08 | 1,1,E-08 | 1,3,E-08 | 2,3,E-08 | 2,3,E-08 | 5,6,E-09 |
| AREA | SRC_248 | Cam_Cat_40-PEAS e Imp | 276114 | 6389925 | 3 mes | 316,96 | 1,0,E-07 | 2,5,E-08 | 3,1,E-08 | 5,5,E-08 | 5,5,E-08 | 1,3,E-08 |
| AREA | SRC_249 | Cam_Cat_41-PEAS e Imp | 276133 | 6389885 | 3 mes | 172,93 | 1,9,E-07 | 4,6,E-08 | 5,7,E-08 | 1,0,E-07 | 1,0,E-07 | 2,4,E-08 |
| AREA | SRC_250 | Cam_Cat_42-PEAS e Imp | 276158 | 6389818 | 3 mes | 286,84 | 1,2,E-07 | 2,8,E-08 | 3,4,E-08 | 6,1,E-08 | 6,1,E-08 | 1,4,E-08 |
| AREA | SRC_251 | Cam_Cat_43-PEAS e Imp | 276157 | 6389659 | 3 mes | 632,84 | 5,2,E-08 | 1,3,E-08 | 1,6,E-08 | 2,8,E-08 | 2,8,E-08 | 6,6,E-09 |
| AREA | SRC_252 | Cam_Cat_44-PEAS e Imp | 276172 | 6389529 | 3 mes | 521,10 | 6,4,E-08 | 1,5,E-08 | 1,9,E-08 | 3,3,E-08 | 3,3,E-08 | 8,0,E-09 |
| AREA | SRC_253 | Cam_Cat_45-PEAS e Imp | 276275 | 6389477 | 3 mes | 468,32 | 7,1,E-08 | 1,7,E-08 | 2,1,E-08 | 3,7,E-08 | 3,7,E-08 | 8,9,E-09 |
| AREA | SRC_254 | Cam_Cat_46-PEAS e Imp | 276411 | 6389458 | 3 mes | 553,37 | 6,0,E-08 | 1,5,E-08 | 1,8,E-08 | 3,2,E-08 | 3,2,E-08 | 7,5,E-09 |
| AREA | SRC_255 | Cam_Cat_47-PEAS e Imp | 276501 | 6389471 | 3 mes | 366,24 | 9,1,E-08 | 2,2,E-08 | 2,7,E-08 | 4,8,E-08 | 4,8,E-08 | 1,1,E-08 |
| AREA | SRC_256 | Cam_Cat_48-PEAS e Imp | 276706 | 6389673 | 3 mes | 1151,46 | 2,9,E-08 | 7,0,E-09 | 8,6,E-09 | 1,5,E-08 | 1,5,E-08 | 3,6,E-09 |
| AREA | SRC_257 | Cam_Cat_49-PEAS e Imp | 277353 | 6390498 | 3 mes | 4195,41 | 7,9,E-09 | 1,9,E-09 | 2,3,E-09 | 4,2,E-09 | 4,2,E-09 | 9,9,E-10 |
| AREA | SRC_258 | Cam_Cat_50-PEAS e Imp | 277494 | 6390575 | 3 mes | 640,03 | 5,2,E-08 | 1,3,E-08 | 1,5,E-08 | 2,7,E-08 | 2,7,E-08 | 6,5,E-09 |
| AREA | SRC_259 | Cam_Cat_51-PEAS e Imp | 279440 | 6391244 | 3 mes | 8223,68 | 4,0,E-09 | 9,8,E-10 | 1,2,E-09 | 2,1,E-09 | 2,1,E-09 | 5,1,E-10 |
| AREA | SRC_260 | Cam_Cat_52-PEAS e Imp | 283346 | 6393239 | 3 mes | 17540,88 | 1,9,E-09 | 4,6,E-10 | 5,6,E-10 | 9,9,E-10 | 9,9,E-10 | 2,4,E-10 |

**Tabla 62.: Fuentes de Emisión - Escenario 1 parte 6**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_261 | Cam_Cat_53-PEAS e Imp | 287745 | 6394661 | 3 mes | 18483,13 | 1,8,E-09 | 4,3,E-10 | 5,3,E-10 | 9,4,E-10 | 9,4,E-10 | 2,2,E-10 |
| AREA | SRC_262 | Cam_Pta_1-PEAS e Imp | 273147 | 6383634 | 3 mes | 1866,42 | 1,8,E-08 | 4,3,E-09 | 5,3,E-09 | 9,3,E-09 | 9,3,E-09 | 2,2,E-09 |
| AREA | SRC_263 | Cam_Pta_2-PEAS e Imp | 273165 | 6383642 | 3 mes | 80,85 | 4,1,E-07 | 9,9,E-08 | 1,2,E-07 | 2,2,E-07 | 2,2,E-07 | 5,1,E-08 |
| AREA | SRC_264 | Cam_Pta_3-PEAS e Imp | 273189 | 6383637 | 3 mes | 94,14 | 3,5,E-07 | 8,5,E-08 | 1,0,E-07 | 1,9,E-07 | 1,9,E-07 | 4,4,E-08 |
| AREA | SRC_265 | Cam_Pta_4-PEAS e Imp | 273241 | 6383562 | 3 mes | 359,95 | 9,2,E-08 | 2,2,E-08 | 2,7,E-08 | 4,8,E-08 | 4,8,E-08 | 1,2,E-08 |
| AREA | SRC_266 | Cam_Pta_5-PEAS e Imp | 273289 | 6383445 | 3 mes | 505,57 | 6,6,E-08 | 1,6,E-08 | 1,9,E-08 | 3,5,E-08 | 3,5,E-08 | 8,2,E-09 |
| AREA | SRC_267 | Cam_Pta_6-PEAS e Imp | 273304 | 6383402 | 3 mes | 179,62 | 1,8,E-07 | 4,5,E-08 | 5,5,E-08 | 9,7,E-08 | 9,7,E-08 | 2,3,E-08 |
| AREA | SRC_268 | Cam_Pta_7-PEAS e Imp | 273331 | 6383382 | 3 mes | 138,45 | 2,4,E-07 | 5,8,E-08 | 7,1,E-08 | 1,3,E-07 | 1,3,E-07 | 3,0,E-08 |
| AREA | SRC_269 | Cam_Pta_8-PEAS e Imp | 273361 | 6383362 | 3 mes | 145,56 | 2,3,E-07 | 5,5,E-08 | 6,8,E-08 | 1,2,E-07 | 1,2,E-07 | 2,9,E-08 |
| AREA | SRC_270 | Cam_Pta_9-PEAS e Imp | 273393 | 6383346 | 3 mes | 143,99 | 2,3,E-07 | 5,6,E-08 | 6,8,E-08 | 1,2,E-07 | 1,2,E-07 | 2,9,E-08 |
| AREA | SRC_271 | Cam_Pta_10-PEAS e Imp | 273413 | 6383324 | 3 mes | 116,32 | 2,9,E-07 | 6,9,E-08 | 8,5,E-08 | 1,5,E-07 | 1,5,E-07 | 3,6,E-08 |
| AREA | SRC_272 | Cam_Pta_11-PEAS e Imp | 273447 | 6383229 | 3 mes | 400,03 | 8,3,E-08 | 2,0,E-08 | 2,5,E-08 | 4,4,E-08 | 4,4,E-08 | 1,0,E-08 |
| AREA | SRC_273 | Cam_Pta_12-PEAS e Imp | 273463 | 6383220 | 3 mes | 80,13 | 4,1,E-07 | 1,0,E-07 | 1,2,E-07 | 2,2,E-07 | 2,2,E-07 | 5,2,E-08 |
| AREA | SRC_274 | Cam_Pta_13-PEAS e Imp | 273473 | 6383218 | 3 mes | 45,12 | 7,4,E-07 | 1,8,E-07 | 2,2,E-07 | 3,9,E-07 | 3,9,E-07 | 9,2,E-08 |
| AREA | SRC_275 | Cam_Pta_14-PEAS e Imp | 273519 | 6383228 | 3 mes | 188,53 | 1,8,E-07 | 4,3,E-08 | 5,2,E-08 | 9,3,E-08 | 9,3,E-08 | 2,2,E-08 |
| AREA | SRC_276 | Cam_Valpo_1-PEAS e Imp | 267407 | 6370003 | 3 mes | 9181,86 | 3,6,E-09 | 8,8,E-10 | 1,1,E-09 | 1,9,E-09 | 1,9,E-09 | 4,5,E-10 |
| AREA | SRC_277 | Cam_Valpo_2-PEAS e Imp | 267402 | 6370088 | 3 mes | 338,29 | 9,8,E-08 | 2,4,E-08 | 2,9,E-08 | 5,2,E-08 | 5,2,E-08 | 1,2,E-08 |
| AREA | SRC_278 | Cam_Valpo_3-PEAS e Imp | 267699 | 6371506 | 3 mes | 5788,94 | 5,7,E-09 | 1,4,E-09 | 1,7,E-09 | 3,0,E-09 | 3,0,E-09 | 7,2,E-10 |
| AREA | SRC_279 | Cam_Valpo_4-PEAS e Imp | 267700 | 6371619 | 3 mes | 452,00 | 7,3,E-08 | 1,8,E-08 | 2,2,E-08 | 3,9,E-08 | 3,9,E-08 | 9,2,E-09 |
| AREA | SRC_280 | Cam_Valpo_5-PEAS e Imp | 267517 | 6371917 | 3 mes | 1401,44 | 2,4,E-08 | 5,7,E-09 | 7,0,E-09 | 1,2,E-08 | 1,2,E-08 | 3,0,E-09 |
| AREA | SRC_281 | Cam_Valpo_6-PEAS e Imp | 267499 | 6371980 | 3 mes | 261,10 | 1,3,E-07 | 3,1,E-08 | 3,8,E-08 | 6,7,E-08 | 6,7,E-08 | 1,6,E-08 |
| AREA | SRC_282 | Cam_Valpo_7-PEAS e Imp | 267496 | 6372042 | 3 mes | 247,03 | 1,3,E-07 | 3,3,E-08 | 4,0,E-08 | 7,1,E-08 | 7,1,E-08 | 1,7,E-08 |
| AREA | SRC_283 | Cam_Valpo_8-PEAS e Imp | 267518 | 6372113 | 3 mes | 294,47 | 1,1,E-07 | 2,7,E-08 | 3,3,E-08 | 5,9,E-08 | 5,9,E-08 | 1,4,E-08 |
| AREA | SRC_284 | Cam_Valpo_9-PEAS e Imp | 267547 | 6372151 | 3 mes | 187,43 | 1,8,E-07 | 4,3,E-08 | 5,3,E-08 | 9,3,E-08 | 9,3,E-08 | 2,2,E-08 |
| AREA | SRC_285 | Cam_Valpo_10-PEAS e Imp | 267569 | 6372177 | 3 mes | 137,02 | 2,4,E-07 | 5,9,E-08 | 7,2,E-08 | 1,3,E-07 | 1,3,E-07 | 3,0,E-08 |
| AREA | SRC_286 | Cam_Valpo_11-PEAS e Imp | 267738 | 6372319 | 3 mes | 879,83 | 3,8,E-08 | 9,1,E-09 | 1,1,E-08 | 2,0,E-08 | 2,0,E-08 | 4,7,E-09 |
| AREA | SRC_287 | Cam_Valpo_12-PEAS e Imp | 267762 | 6372358 | 3 mes | 186,57 | 1,8,E-07 | 4,3,E-08 | 5,3,E-08 | 9,4,E-08 | 9,4,E-08 | 2,2,E-08 |
| AREA | SRC_288 | Cam_Valpo_13-PEAS e Imp | 267783 | 6372410 | 3 mes | 224,51 | 1,5,E-07 | 3,6,E-08 | 4,4,E-08 | 7,8,E-08 | 7,8,E-08 | 1,9,E-08 |
| AREA | SRC_289 | Cam_Valpo_14-PEAS e Imp | 267855 | 6372669 | 3 mes | 1075,61 | 3,1,E-08 | 7,5,E-09 | 9,2,E-09 | 1,6,E-08 | 1,6,E-08 | 3,9,E-09 |
| AREA | SRC_290 | Cam_Valpo_15-PEAS e Imp | 267848 | 6372720 | 3 mes | 207,78 | 1,6,E-07 | 3,9,E-08 | 4,7,E-08 | 8,4,E-08 | 8,4,E-08 | 2,0,E-08 |
| AREA | SRC_291 | Cam_Valpo_16-PEAS e Imp | 267715 | 6373066 | 3 mes | 1484,08 | 2,2,E-08 | 5,4,E-09 | 6,6,E-09 | 1,2,E-08 | 1,2,E-08 | 2,8,E-09 |
| AREA | SRC_292 | Cam_Valpo_17-PEAS e Imp | 267705 | 6373122 | 3 mes | 225,43 | 1,5,E-07 | 3,6,E-08 | 4,4,E-08 | 7,7,E-08 | 7,7,E-08 | 1,8,E-08 |

**Tabla 63.: Fuentes de Emisión - Escenario 1 parte 7**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_293 | Cam_Valpo_18-PEAS e Imp | 267701 | 6373182 | 3 mes | 241,22 | 1,4,E-07 | 3,3,E-08 | 4,1,E-08 | 7,2,E-08 | 7,2,E-08 | 1,7,E-08 |
| AREA | SRC_294 | Cam_Valpo_19-PEAS e Imp | 267704 | 6373237 | 3 mes | 217,96 | 1,5,E-07 | 3,7,E-08 | 4,5,E-08 | 8,0,E-08 | 8,0,E-08 | 1,9,E-08 |
| AREA | SRC_295 | Cam_Valpo_20-PEAS e Imp | 267713 | 6373309 | 3 mes | 291,26 | 1,1,E-07 | 2,8,E-08 | 3,4,E-08 | 6,0,E-08 | 6,0,E-08 | 1,4,E-08 |
| AREA | SRC_296 | Cam_Valpo_21-PEAS e Imp | 267741 | 6373522 | 3 mes | 860,16 | 3,9,E-08 | 9,3,E-09 | 1,1,E-08 | 2,0,E-08 | 2,0,E-08 | 4,8,E-09 |
| AREA | SRC_297 | Cam_Valpo_22-PEAS e Imp | 267757 | 6373574 | 3 mes | 213,85 | 1,6,E-07 | 3,8,E-08 | 4,6,E-08 | 8,2,E-08 | 8,2,E-08 | 1,9,E-08 |
| AREA | SRC_298 | Cam_Valpo_23-PEAS e Imp | 267777 | 6373617 | 3 mes | 187,32 | 1,8,E-07 | 4,3,E-08 | 5,3,E-08 | 9,3,E-08 | 9,3,E-08 | 2,2,E-08 |
| AREA | SRC_299 | Cam_Valpo_24-PEAS e Imp | 267817 | 6373719 | 3 mes | 441,14 | 7,5,E-08 | 1,8,E-08 | 2,2,E-08 | 4,0,E-08 | 4,0,E-08 | 9,4,E-09 |
| AREA | SRC_300 | Cam_Valpo_25-PEAS e Imp | 267843 | 6373782 | 3 mes | 272,58 | 1,2,E-07 | 2,9,E-08 | 3,6,E-08 | 6,4,E-08 | 6,4,E-08 | 1,5,E-08 |
| AREA | SRC_301 | Cam_Valpo_26-PEAS e Imp | 267877 | 6373831 | 3 mes | 236,03 | 1,4,E-07 | 3,4,E-08 | 4,2,E-08 | 7,4,E-08 | 7,4,E-08 | 1,8,E-08 |
| AREA | SRC_302 | Cam_Valpo_27-PEAS e Imp | 267910 | 6373883 | 3 mes | 246,12 | 1,3,E-07 | 3,3,E-08 | 4,0,E-08 | 7,1,E-08 | 7,1,E-08 | 1,7,E-08 |
| AREA | SRC_303 | Cam_Valpo_28-PEAS e Imp | 268105 | 6374174 | 3 mes | 1399,53 | 2,4,E-08 | 5,7,E-09 | 7,0,E-09 | 1,2,E-08 | 1,2,E-08 | 3,0,E-09 |
| AREA | SRC_304 | Cam_Valpo_29-PEAS e Imp | 268274 | 6374430 | 3 mes | 1228,07 | 2,7,E-08 | 6,5,E-09 | 8,0,E-09 | 1,4,E-08 | 1,4,E-08 | 3,4,E-09 |
| AREA | SRC_305 | Cam_Valpo_30-PEAS e Imp | 268317 | 6374478 | 3 mes | 254,35 | 1,3,E-07 | 3,2,E-08 | 3,9,E-08 | 6,9,E-08 | 6,9,E-08 | 1,6,E-08 |
| AREA | SRC_306 | Cam_Valpo_31-PEAS e Imp | 268347 | 6374502 | 3 mes | 154,46 | 2,2,E-07 | 5,2,E-08 | 6,4,E-08 | 1,1,E-07 | 1,1,E-07 | 2,7,E-08 |
| AREA | SRC_307 | Cam_Valpo_32-PEAS e Imp | 269602 | 6375295 | 3 mes | 5935,56 | 5,6,E-09 | 1,4,E-09 | 1,7,E-09 | 2,9,E-09 | 2,9,E-09 | 7,0,E-10 |
| AREA | SRC_308 | Cam_Valpo_33-PEAS e Imp | 270646 | 6375956 | 3 mes | 4938,33 | 6,7,E-09 | 1,6,E-09 | 2,0,E-09 | 3,5,E-09 | 3,5,E-09 | 8,4,E-10 |
| AREA | SRC_309 | Cam_Valpo_34-PEAS e Imp | 270700 | 6375970 | 3 mes | 220,74 | 1,5,E-07 | 3,6,E-08 | 4,5,E-08 | 7,9,E-08 | 7,9,E-08 | 1,9,E-08 |
| AREA | SRC_310 | Cam_Valpo_35-PEAS e Imp | 270759 | 6375972 | 3 mes | 232,03 | 1,4,E-07 | 3,5,E-08 | 4,2,E-08 | 7,5,E-08 | 7,5,E-08 | 1,8,E-08 |
| AREA | SRC_311 | Cam_Valpo_36-PEAS e Imp | 270817 | 6375960 | 3 mes | 237,83 | 1,4,E-07 | 3,4,E-08 | 4,1,E-08 | 7,3,E-08 | 7,3,E-08 | 1,7,E-08 |
| AREA | SRC_312 | Cam_Valpo_37-PEAS e Imp | 271210 | 6375788 | 3 mes | 1710,95 | 1,9,E-08 | 4,7,E-09 | 5,8,E-09 | 1,0,E-08 | 1,0,E-08 | 2,4,E-09 |
| AREA | SRC_313 | Cam_Valpo_38-PEAS e Imp | 271299 | 6375786 | 3 mes | 362,06 | 9,2,E-08 | 2,2,E-08 | 2,7,E-08 | 4,8,E-08 | 4,8,E-08 | 1,1,E-08 |
| AREA | SRC_314 | Cam_Valpo_39-PEAS e Imp | 271410 | 6375784 | 3 mes | 444,09 | 7,5,E-08 | 1,8,E-08 | 2,2,E-08 | 3,9,E-08 | 3,9,E-08 | 9,4,E-09 |
| AREA | SRC_315 | Cam_Valpo_40-PEAS e Imp | 271537 | 6375829 | 3 mes | 539,94 | 6,2,E-08 | 1,5,E-08 | 1,8,E-08 | 3,2,E-08 | 3,2,E-08 | 7,7,E-09 |
| AREA | SRC_316 | Cam_Valpo_41-PEAS e Imp | 271698 | 6375908 | 3 mes | 717,64 | 4,6,E-08 | 1,1,E-08 | 1,4,E-08 | 2,4,E-08 | 2,4,E-08 | 5,8,E-09 |
| AREA | SRC_317 | Cam_Valpo_42-PEAS e Imp | 271943 | 6376040 | 3 mes | 1111,41 | 3,0,E-08 | 7,2,E-09 | 8,9,E-09 | 1,6,E-08 | 1,6,E-08 | 3,7,E-09 |
| AREA | SRC_318 | Cam_Valpo_43-PEAS e Imp | 272216 | 6376245 | 3 mes | 1365,82 | 2,4,E-08 | 5,9,E-09 | 7,2,E-09 | 1,3,E-08 | 1,3,E-08 | 3,0,E-09 |
| AREA | SRC_319 | Cam_Valpo_44-PEAS e Imp | 272308 | 6376283 | 3 mes | 396,81 | 8,4,E-08 | 2,0,E-08 | 2,5,E-08 | 4,4,E-08 | 4,4,E-08 | 1,0,E-08 |
| AREA | SRC_320 | Cam_Valpo_45-PEAS e Imp | 272828 | 6376412 | 3 mes | 2139,51 | 1,6,E-08 | 3,8,E-09 | 4,6,E-09 | 8,2,E-09 | 8,2,E-09 | 1,9,E-09 |
| AREA | SRC_321 | Cam_Valpo_46-PEAS e Imp | 272961 | 6376463 | 3 mes | 572,90 | 5,8,E-08 | 1,4,E-08 | 1,7,E-08 | 3,0,E-08 | 3,0,E-08 | 7,3,E-09 |
| AREA | SRC_322 | Cam_Valpo_47-PEAS e Imp | 273101 | 6376548 | 3 mes | 656,43 | 5,1,E-08 | 1,2,E-08 | 1,5,E-08 | 2,7,E-08 | 2,7,E-08 | 6,3,E-09 |
| AREA | SRC_323 | Cam_Valpo_48-PEAS e Imp | 273683 | 6376890 | 3 mes | 2699,98 | 1,2,E-08 | 3,0,E-09 | 3,6,E-09 | 6,5,E-09 | 6,5,E-09 | 1,5,E-09 |
| AREA | SRC_324 | Cam_Valpo_49-PEAS e Imp | 273729 | 6376911 | 3 mes | 198,66 | 1,7,E-07 | 4,0,E-08 | 5,0,E-08 | 8,8,E-08 | 8,8,E-08 | 2,1,E-08 |

**Tabla 64.: Fuentes de Emisión - Escenario 1 parte 8**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_325 | Cam_Valpo_50-PEAS e Imp | 273841 | 6376934 | 3 mes | 455,50 | 7,3,E-08 | 1,8,E-08 | 2,2,E-08 | 3,8,E-08 | 3,8,E-08 | 9,1,E-09 |
| AREA | SRC_326 | Cam_Valpo_51-PEAS e Imp | 273918 | 6376948 | 3 mes | 314,84 | 1,1,E-07 | 2,6,E-08 | 3,1,E-08 | 5,5,E-08 | 5,5,E-08 | 1,3,E-08 |
| AREA | SRC_327 | Cam_Valpo_52-PEAS e Imp | 273963 | 6376959 | 3 mes | 182,29 | 1,8,E-07 | 4,4,E-08 | 5,4,E-08 | 9,6,E-08 | 9,6,E-08 | 2,3,E-08 |
| AREA | SRC_328 | Cam_Valpo_53-PEAS e Imp | 274013 | 6376981 | 3 mes | 220,22 | 1,5,E-07 | 3,6,E-08 | 4,5,E-08 | 7,9,E-08 | 7,9,E-08 | 1,9,E-08 |
| AREA | SRC_329 | Cam_Valpo_54-PEAS e Imp | 274045 | 6377010 | 3 mes | 175,74 | 1,9,E-07 | 4,6,E-08 | 5,6,E-08 | 9,9,E-08 | 9,9,E-08 | 2,4,E-08 |
| AREA | SRC_330 | Cam_Valpo_55-PEAS e Imp | 274402 | 6377569 | 3 mes | 2654,98 | 1,3,E-08 | 3,0,E-09 | 3,7,E-09 | 6,6,E-09 | 6,6,E-09 | 1,6,E-09 |
| AREA | SRC_331 | Cam_Valpo_56-PEAS e Imp | 274508 | 6377712 | 3 mes | 712,20 | 4,7,E-08 | 1,1,E-08 | 1,4,E-08 | 2,4,E-08 | 2,4,E-08 | 5,8,E-09 |
| AREA | SRC_332 | Cam_Valpo_57-PEAS e Imp | 274515 | 6377737 | 3 mes | 105,54 | 3,1,E-07 | 7,6,E-08 | 9,3,E-08 | 1,7,E-07 | 1,7,E-07 | 3,9,E-08 |
| AREA | SRC_333 | Cam_Valpo_58-PEAS e Imp | 274530 | 6377783 | 3 mes | 190,85 | 1,7,E-07 | 4,2,E-08 | 5,2,E-08 | 9,1,E-08 | 9,1,E-08 | 2,2,E-08 |
| AREA | SRC_334 | Cam_Valpo_59-PEAS e Imp | 274571 | 6378190 | 3 mes | 1640,54 | 2,0,E-08 | 4,9,E-09 | 6,0,E-09 | 1,1,E-08 | 1,1,E-08 | 2,5,E-09 |
| AREA | SRC_335 | Cam_Valpo_60-PEAS e Imp | 274512 | 6378662 | 3 mes | 1902,24 | 1,7,E-08 | 4,2,E-09 | 5,2,E-09 | 9,2,E-09 | 9,2,E-09 | 2,2,E-09 |
| AREA | SRC_336 | Cam_Valpo_61-PEAS e Imp | 274484 | 6378742 | 3 mes | 339,36 | 9,8,E-08 | 2,4,E-08 | 2,9,E-08 | 5,1,E-08 | 5,1,E-08 | 1,2,E-08 |
| AREA | SRC_337 | Cam_Valpo_62-PEAS e Imp | 274397 | 6378959 | 3 mes | 934,88 | 3,6,E-08 | 8,6,E-09 | 1,1,E-08 | 1,9,E-08 | 1,9,E-08 | 4,4,E-09 |
| AREA | SRC_338 | Cam_Valpo_63-PEAS e Imp | 274391 | 6379006 | 3 mes | 189,58 | 1,8,E-07 | 4,2,E-08 | 5,2,E-08 | 9,2,E-08 | 9,2,E-08 | 2,2,E-08 |
| AREA | SRC_339 | Cam_Valpo_64-PEAS e Imp | 274392 | 6379034 | 3 mes | 109,49 | 3,0,E-07 | 7,3,E-08 | 9,0,E-08 | 1,6,E-07 | 1,6,E-07 | 3,8,E-08 |
| AREA | SRC_340 | Cam_Valpo_65-PEAS e Imp | 274513 | 6379469 | 3 mes | 1805,57 | 1,8,E-08 | 4,5,E-09 | 5,5,E-09 | 9,7,E-09 | 9,7,E-09 | 2,3,E-09 |
| AREA | SRC_341 | Cam_Valpo_66-PEAS e Imp | 274514 | 6379510 | 3 mes | 163,36 | 2,0,E-07 | 4,9,E-08 | 6,0,E-08 | 1,1,E-07 | 1,1,E-07 | 2,5,E-08 |
| AREA | SRC_342 | Cam_Valpo_67-PEAS e Imp | 274503 | 6379560 | 3 mes | 208,73 | 1,6,E-07 | 3,9,E-08 | 4,7,E-08 | 8,4,E-08 | 8,4,E-08 | 2,0,E-08 |
| AREA | SRC_343 | Cam_Valpo_68-PEAS e Imp | 274488 | 6379623 | 3 mes | 255,44 | 1,3,E-07 | 3,1,E-08 | 3,9,E-08 | 6,8,E-08 | 6,8,E-08 | 1,6,E-08 |
| AREA | SRC_344 | Cam_Valpo_69-PEAS e Imp | 274426 | 6379798 | 3 mes | 745,56 | 4,5,E-08 | 1,1,E-08 | 1,3,E-08 | 2,3,E-08 | 2,3,E-08 | 5,6,E-09 |
| AREA | SRC_345 | Cam_Valpo_70-PEAS e Imp | 274386 | 6379897 | 3 mes | 428,53 | 7,8,E-08 | 1,9,E-08 | 2,3,E-08 | 4,1,E-08 | 4,1,E-08 | 9,7,E-09 |
| AREA | SRC_346 | Cam_Valpo_71-PEAS e Imp | 274352 | 6379981 | 3 mes | 360,23 | 9,2,E-08 | 2,2,E-08 | 2,7,E-08 | 4,8,E-08 | 4,8,E-08 | 1,2,E-08 |
| AREA | SRC_347 | Cam_Valpo_72-PEAS e Imp | 274336 | 6380041 | 3 mes | 249,49 | 1,3,E-07 | 3,2,E-08 | 3,9,E-08 | 7,0,E-08 | 7,0,E-08 | 1,7,E-08 |
| AREA | SRC_348 | Cam_Valpo_73-PEAS e Imp | 274333 | 6380099 | 3 mes | 227,80 | 1,5,E-07 | 3,5,E-08 | 4,3,E-08 | 7,7,E-08 | 7,7,E-08 | 1,8,E-08 |
| AREA | SRC_349 | Cam_Valpo_74-PEAS e Imp | 274332 | 6380163 | 3 mes | 257,27 | 1,3,E-07 | 3,1,E-08 | 3,8,E-08 | 6,8,E-08 | 6,8,E-08 | 1,6,E-08 |
| AREA | SRC_350 | Cam_Valpo_75-PEAS e Imp | 274329 | 6380546 | 3 mes | 1530,44 | 2,2,E-08 | 5,3,E-09 | 6,4,E-09 | 1,1,E-08 | 1,1,E-08 | 2,7,E-09 |
| AREA | SRC_351 | Cam_Valpo_76-PEAS e Imp | 274323 | 6380578 | 3 mes | 130,55 | 2,5,E-07 | 6,2,E-08 | 7,5,E-08 | 1,3,E-07 | 1,3,E-07 | 3,2,E-08 |
| AREA | SRC_352 | Cam_Valpo_77-PEAS e Imp | 274308 | 6380608 | 3 mes | 138,17 | 2,4,E-07 | 5,8,E-08 | 7,1,E-08 | 1,3,E-07 | 1,3,E-07 | 3,0,E-08 |
| AREA | SRC_353 | Cam_Valpo_78-PEAS e Imp | 274078 | 6381086 | 3 mes | 2120,50 | 1,6,E-08 | 3,8,E-09 | 4,6,E-09 | 8,2,E-09 | 8,2,E-09 | 2,0,E-09 |
| AREA | SRC_354 | Cam_Valpo_79-PEAS e Imp | 274036 | 6381146 | 3 mes | 292,96 | 1,1,E-07 | 2,7,E-08 | 3,4,E-08 | 6,0,E-08 | 6,0,E-08 | 1,4,E-08 |
| AREA | SRC_355 | Cam_Valpo_80-PEAS e Imp | 273997 | 6381192 | 3 mes | 242,71 | 1,4,E-07 | 3,3,E-08 | 4,1,E-08 | 7,2,E-08 | 7,2,E-08 | 1,7,E-08 |
| AREA | SRC_356 | Cam_Valpo_81-PEAS e Imp | 273945 | 6381212 | 3 mes | 225,25 | 1,5,E-07 | 3,6,E-08 | 4,4,E-08 | 7,7,E-08 | 7,7,E-08 | 1,8,E-08 |

**Tabla 65.: Fuentes de Emisión - Escenario 1 parte 9**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_357 | Cam_Valpo_82-PEAS e Imp | 273863 | 6381235 | 3 mes | 340,59 | 9,8,E-08 | 2,4,E-08 | 2,9,E-08 | 5,1,E-08 | 5,1,E-08 | 1,2,E-08 |
| AREA | SRC_358 | Cam_Valpo_83-PEAS e Imp | 273527 | 6381309 | 3 mes | 1376,67 | 2,4,E-08 | 5,8,E-09 | 7,2,E-09 | 1,3,E-08 | 1,3,E-08 | 3,0,E-09 |
| AREA | SRC_359 | Cam_Valpo_84-PEAS e Imp | 273488 | 6381317 | 3 mes | 158,83 | 2,1,E-07 | 5,1,E-08 | 6,2,E-08 | 1,1,E-07 | 1,1,E-07 | 2,6,E-08 |
| AREA | SRC_360 | Cam_Valpo_85-PEAS e Imp | 273437 | 6381311 | 3 mes | 210,61 | 1,6,E-07 | 3,8,E-08 | 4,7,E-08 | 8,3,E-08 | 8,3,E-08 | 2,0,E-08 |
| AREA | SRC_361 | Cam_Valpo_86-PEAS e Imp | 273400 | 6381306 | 3 mes | 148,75 | 2,2,E-07 | 5,4,E-08 | 6,6,E-08 | 1,2,E-07 | 1,2,E-07 | 2,8,E-08 |
| AREA | SRC_362 | Cam_Valpo_87-PEAS e Imp | 273330 | 6381278 | 3 mes | 302,02 | 1,1,E-07 | 2,7,E-08 | 3,3,E-08 | 5,8,E-08 | 5,8,E-08 | 1,4,E-08 |
| AREA | SRC_363 | Cam_Valpo_88-PEAS e Imp | 273269 | 6381275 | 3 mes | 240,32 | 1,4,E-07 | 3,3,E-08 | 4,1,E-08 | 7,3,E-08 | 7,3,E-08 | 1,7,E-08 |
| AREA | SRC_364 | Cam_Valpo_89-PEAS e Imp | 273210 | 6381284 | 3 mes | 238,69 | 1,4,E-07 | 3,4,E-08 | 4,1,E-08 | 7,3,E-08 | 7,3,E-08 | 1,7,E-08 |
| AREA | SRC_365 | Cam_Valpo_90-PEAS e Imp | 273140 | 6381307 | 3 mes | 291,89 | 1,1,E-07 | 2,8,E-08 | 3,4,E-08 | 6,0,E-08 | 6,0,E-08 | 1,4,E-08 |
| AREA | SRC_366 | Cam_Valpo_91-PEAS e Imp | 273026 | 6381364 | 3 mes | 510,61 | 6,5,E-08 | 1,6,E-08 | 1,9,E-08 | 3,4,E-08 | 3,4,E-08 | 8,1,E-09 |
| AREA | SRC_367 | Cam_Valpo_92-PEAS e Imp | 272787 | 6381471 | 3 mes | 1046,47 | 3,2,E-08 | 7,7,E-09 | 9,4,E-09 | 1,7,E-08 | 1,7,E-08 | 4,0,E-09 |
| AREA | SRC_368 | Cam_Valpo_93-PEAS e Imp | 272625 | 6381553 | 3 mes | 726,81 | 4,6,E-08 | 1,1,E-08 | 1,4,E-08 | 2,4,E-08 | 2,4,E-08 | 5,7,E-09 |
| AREA | SRC_369 | Cam_Valpo_94-PEAS e Imp | 272586 | 6381587 | 3 mes | 205,87 | 1,6,E-07 | 3,9,E-08 | 4,8,E-08 | 8,5,E-08 | 8,5,E-08 | 2,0,E-08 |
| AREA | SRC_370 | Cam_Valpo_95-PEAS e Imp | 272567 | 6381621 | 3 mes | 150,25 | 2,2,E-07 | 5,3,E-08 | 6,6,E-08 | 1,2,E-07 | 1,2,E-07 | 2,8,E-08 |
| AREA | SRC_371 | Cam_Valpo_96-PEAS e Imp | 272558 | 6381659 | 3 mes | 154,59 | 2,1,E-07 | 5,2,E-08 | 6,4,E-08 | 1,1,E-07 | 1,1,E-07 | 2,7,E-08 |
| AREA | SRC_372 | Cam_Valpo_97-PEAS e Imp | 272513 | 6381931 | 3 mes | 1103,20 | 3,0,E-08 | 7,3,E-09 | 8,9,E-09 | 1,6,E-08 | 1,6,E-08 | 3,8,E-09 |
| AREA | SRC_373 | Cam_Valpo_98-PEAS e Imp | 272500 | 6382030 | 3 mes | 398,37 | 8,3,E-08 | 2,0,E-08 | 2,5,E-08 | 4,4,E-08 | 4,4,E-08 | 1,0,E-08 |
| AREA | SRC_374 | Cam_Valpo_99-PEAS e Imp | 272492 | 6382086 | 3 mes | 223,87 | 1,5,E-07 | 3,6,E-08 | 4,4,E-08 | 7,8,E-08 | 7,8,E-08 | 1,9,E-08 |
| AREA | SRC_375 | Cam_Valpo_100-PEAS e Imp | 272491 | 6382127 | 3 mes | 164,32 | 2,0,E-07 | 4,9,E-08 | 6,0,E-08 | 1,1,E-07 | 1,1,E-07 | 2,5,E-08 |
| AREA | SRC_376 | Cam_Valpo_101-PEAS e Imp | 272506 | 6382188 | 3 mes | 247,33 | 1,3,E-07 | 3,2,E-08 | 4,0,E-08 | 7,1,E-08 | 7,1,E-08 | 1,7,E-08 |
| AREA | SRC_377 | Cam_Valpo_102-PEAS e Imp | 272660 | 6383439 | 3 mes | 5043,31 | 6,6,E-09 | 1,6,E-09 | 2,0,E-09 | 3,5,E-09 | 3,5,E-09 | 8,2,E-10 |
| AREA | SRC_378 | Cam_Valpo_103-PEAS e Imp | 272630 | 6384559 | 3 mes | 4478,91 | 7,4,E-09 | 1,8,E-09 | 2,2,E-09 | 3,9,E-09 | 3,9,E-09 | 9,3,E-10 |
| AREA | SRC_379 | Cam_Valpo_104-PEAS e Imp | 272626 | 6385227 | 3 mes | 2671,08 | 1,2,E-08 | 3,0,E-09 | 3,7,E-09 | 6,5,E-09 | 6,5,E-09 | 1,6,E-09 |
| AREA | SRC_380 | Cam_Valpo_105-PEAS e Imp | 272602 | 6386454 | 3 mes | 4905,80 | 6,8,E-09 | 1,6,E-09 | 2,0,E-09 | 3,6,E-09 | 3,6,E-09 | 8,5,E-10 |
| AREA | SRC_381 | Cam_Valpo_106-PEAS e Imp | 272609 | 6386527 | 3 mes | 292,53 | 1,1,E-07 | 2,7,E-08 | 3,4,E-08 | 6,0,E-08 | 6,0,E-08 | 1,4,E-08 |
| AREA | SRC_382 | Cam_Valpo_107-PEAS e Imp | 272650 | 6386615 | 3 mes | 384,69 | 8,6,E-08 | 2,1,E-08 | 2,6,E-08 | 4,5,E-08 | 4,5,E-08 | 1,1,E-08 |
| AREA | SRC_383 | Cam_Valpo_108-PEAS e Imp | 272755 | 6386705 | 3 mes | 550,00 | 6,0,E-08 | 1,5,E-08 | 1,8,E-08 | 3,2,E-08 | 3,2,E-08 | 7,6,E-09 |
| AREA | SRC_384 | Cam_Valpo_109-PEAS e Imp | 272846 | 6386776 | 3 mes | 460,85 | 7,2,E-08 | 1,7,E-08 | 2,1,E-08 | 3,8,E-08 | 3,8,E-08 | 9,0,E-09 |
| AREA | SRC_385 | Cam_Valpo_110-PEAS e Imp | 272918 | 6386821 | 3 mes | 338,79 | 9,8,E-08 | 2,4,E-08 | 2,9,E-08 | 5,1,E-08 | 5,1,E-08 | 1,2,E-08 |
| AREA | SRC_386 | Cam_Valpo_111-PEAS e Imp | 272959 | 6386856 | 3 mes | 215,71 | 1,5,E-07 | 3,7,E-08 | 4,6,E-08 | 8,1,E-08 | 8,1,E-08 | 1,9,E-08 |
| AREA | SRC_387 | Cam_Valpo_112-PEAS e Imp | 272979 | 6386909 | 3 mes | 229,32 | 1,4,E-07 | 3,5,E-08 | 4,3,E-08 | 7,6,E-08 | 7,6,E-08 | 1,8,E-08 |
| AREA | SRC_388 | Cam_Valpo_113-PEAS e Imp | 272982 | 6386950 | 3 mes | 168,20 | 2,0,E-07 | 4,8,E-08 | 5,9,E-08 | 1,0,E-07 | 1,0,E-07 | 2,5,E-08 |

**Tabla 66.: Fuentes de Emisión - Escenario 1 parte 10**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_389 | Cam_Valpo_114-PEAS e Imp | 272974 | 6387033 | 3 mes | 334,56 | 9,9,E-08 | 2,4,E-08 | 2,9,E-08 | 5,2,E-08 | 5,2,E-08 | 1,2,E-08 |
| AREA | SRC_390 | Cam_Valpo_115-PEAS e Imp | 272969 | 6387289 | 3 mes | 1021,26 | 3,3,E-08 | 7,9,E-09 | 9,6,E-09 | 1,7,E-08 | 1,7,E-08 | 4,1,E-09 |
| AREA | SRC_391 | Cam_Valpo_116-PEAS e Imp | 272950 | 6387316 | 3 mes | 135,86 | 2,4,E-07 | 5,9,E-08 | 7,2,E-08 | 1,3,E-07 | 1,3,E-07 | 3,1,E-08 |
| AREA | SRC_392 | Cam_Valpo_117-PEAS e Imp | 272918 | 6387332 | 3 mes | 150,62 | 2,2,E-07 | 5,3,E-08 | 6,5,E-08 | 1,2,E-07 | 1,2,E-07 | 2,8,E-08 |
| AREA | SRC_393 | Cam_Valpo_118-PEAS e Imp | 272871 | 6387328 | 3 mes | 193,11 | 1,7,E-07 | 4,2,E-08 | 5,1,E-08 | 9,0,E-08 | 9,0,E-08 | 2,2,E-08 |
| AREA | SRC_394 | Cam_Valpo_119-PEAS e Imp | 272818 | 6387319 | 3 mes | 214,82 | 1,5,E-07 | 3,7,E-08 | 4,6,E-08 | 8,1,E-08 | 8,1,E-08 | 1,9,E-08 |
| AREA | SRC_395 | Cam_Valpo_120-PEAS e Imp | 272669 | 6387324 | 3 mes | 593,51 | 5,6,E-08 | 1,4,E-08 | 1,7,E-08 | 2,9,E-08 | 2,9,E-08 | 7,0,E-09 |
| AREA | SRC_396 | Cam_Valpo_121-PEAS e Imp | 272536 | 6387380 | 3 mes | 574,11 | 5,8,E-08 | 1,4,E-08 | 1,7,E-08 | 3,0,E-08 | 3,0,E-08 | 7,2,E-09 |
| AREA | SRC_397 | Cam_Valpo_122-PEAS e Imp | 272406 | 6387475 | 3 mes | 642,85 | 5,2,E-08 | 1,3,E-08 | 1,5,E-08 | 2,7,E-08 | 2,7,E-08 | 6,5,E-09 |
| AREA | SRC_398 | Cam_Valpo_123-PEAS e Imp | 272321 | 6387544 | 3 mes | 438,86 | 7,6,E-08 | 1,8,E-08 | 2,2,E-08 | 4,0,E-08 | 4,0,E-08 | 9,5,E-09 |
| AREA | SRC_399 | Cam_Valpo_124-PEAS e Imp | 272252 | 6387605 | 3 mes | 366,01 | 9,1,E-08 | 2,2,E-08 | 2,7,E-08 | 4,8,E-08 | 4,8,E-08 | 1,1,E-08 |
| AREA | SRC_400 | Cam_Valpo_125-PEAS e Imp | 272138 | 6387749 | 3 mes | 733,97 | 4,5,E-08 | 1,1,E-08 | 1,3,E-08 | 2,4,E-08 | 2,4,E-08 | 5,7,E-09 |
| AREA | SRC_401 | Cam_Valpo_126-PEAS e Imp | 272059 | 6387890 | 3 mes | 645,70 | 5,1,E-08 | 1,2,E-08 | 1,5,E-08 | 2,7,E-08 | 2,7,E-08 | 6,4,E-09 |
| AREA | SRC_402 | Cam_Valpo_127-PEAS e Imp | 272019 | 6388008 | 3 mes | 494,29 | 6,7,E-08 | 1,6,E-08 | 2,0,E-08 | 3,5,E-08 | 3,5,E-08 | 8,4,E-09 |
| AREA | SRC_403 | Cam_Valpo_128-PEAS e Imp | 272005 | 6388086 | 3 mes | 318,17 | 1,0,E-07 | 2,5,E-08 | 3,1,E-08 | 5,5,E-08 | 5,5,E-08 | 1,3,E-08 |
| AREA | SRC_404 | Cam_Valpo_129-PEAS e Imp | 272005 | 6388171 | 3 mes | 338,40 | 9,8,E-08 | 2,4,E-08 | 2,9,E-08 | 5,2,E-08 | 5,2,E-08 | 1,2,E-08 |
| AREA | SRC_405 | Cam_Valpo_130-PEAS e Imp | 272018 | 6388207 | 3 mes | 149,40 | 2,2,E-07 | 5,4,E-08 | 6,6,E-08 | 1,2,E-07 | 1,2,E-07 | 2,8,E-08 |
| AREA | SRC_406 | Cam_Valpo_131-PEAS e Imp | 272053 | 6388222 | 3 mes | 144,57 | 2,3,E-07 | 5,6,E-08 | 6,8,E-08 | 1,2,E-07 | 1,2,E-07 | 2,9,E-08 |
| AREA | SRC_407 | Cam_Valpo_132-PEAS e Imp | 272113 | 6388260 | 3 mes | 286,19 | 1,2,E-07 | 2,8,E-08 | 3,4,E-08 | 6,1,E-08 | 6,1,E-08 | 1,5,E-08 |
| AREA | SRC_408 | Cam_Valpo_133-PEAS e Imp | 272165 | 6388289 | 3 mes | 236,50 | 1,4,E-07 | 3,4,E-08 | 4,2,E-08 | 7,4,E-08 | 7,4,E-08 | 1,8,E-08 |
| AREA | SRC_409 | Cam_Valpo_134-PEAS e Imp | 272170 | 6388313 | 3 mes | 103,04 | 3,2,E-07 | 7,8,E-08 | 9,6,E-08 | 1,7,E-07 | 1,7,E-07 | 4,0,E-08 |
| AREA | SRC_410 | Cam_Valpo_135-PEAS e Imp | 272160 | 6388355 | 3 mes | 178,67 | 1,9,E-07 | 4,5,E-08 | 5,5,E-08 | 9,8,E-08 | 9,8,E-08 | 2,3,E-08 |
| AREA | SRC_411 | Cam_Valpo_136-PEAS e Imp | 272116 | 6388384 | 3 mes | 213,17 | 1,6,E-07 | 3,8,E-08 | 4,6,E-08 | 8,2,E-08 | 8,2,E-08 | 1,9,E-08 |
| AREA | SRC_412 | Cam_Valpo_137-PEAS e Imp | 271990 | 6388473 | 3 mes | 618,26 | 5,4,E-08 | 1,3,E-08 | 1,6,E-08 | 2,8,E-08 | 2,8,E-08 | 6,7,E-09 |
| AREA | SRC_413 | Cam_Valpo_138-PEAS e Imp | 271909 | 6388570 | 3 mes | 502,24 | 6,6,E-08 | 1,6,E-08 | 2,0,E-08 | 3,5,E-08 | 3,5,E-08 | 8,3,E-09 |
| AREA | SRC_414 | Cam_Valpo_139-PEAS e Imp | 271887 | 6388631 | 3 mes | 257,67 | 1,3,E-07 | 3,1,E-08 | 3,8,E-08 | 6,8,E-08 | 6,8,E-08 | 1,6,E-08 |
| AREA | SRC_415 | Cam_Valpo_140-PEAS e Imp | 271869 | 6388710 | 3 mes | 324,57 | 1,0,E-07 | 2,5,E-08 | 3,0,E-08 | 5,4,E-08 | 5,4,E-08 | 1,3,E-08 |
| AREA | SRC_416 | Cam_Valpo_141-PEAS e Imp | 271879 | 6388778 | 3 mes | 270,72 | 1,2,E-07 | 3,0,E-08 | 3,6,E-08 | 6,4,E-08 | 6,4,E-08 | 1,5,E-08 |
| AREA | SRC_417 | Cam_Valpo_142-PEAS e Imp | 271889 | 6388831 | 3 mes | 215,81 | 1,5,E-07 | 3,7,E-08 | 4,6,E-08 | 8,1,E-08 | 8,1,E-08 | 1,9,E-08 |
| AREA | SRC_418 | Cam_Valpo_143-PEAS e Imp | 271888 | 6388910 | 3 mes | 317,54 | 1,0,E-07 | 2,5,E-08 | 3,1,E-08 | 5,5,E-08 | 5,5,E-08 | 1,3,E-08 |
| AREA | SRC_419 | Cam_Valpo_144-PEAS e Imp | 271765 | 6389249 | 3 mes | 1443,83 | 2,3,E-08 | 5,6,E-09 | 6,8,E-09 | 1,2,E-08 | 1,2,E-08 | 2,9,E-09 |
| AREA | SRC_420 | Cam_Valpo_145-PEAS e Imp | 271745 | 6389323 | 3 mes | 308,68 | 1,1,E-07 | 2,6,E-08 | 3,2,E-08 | 5,7,E-08 | 5,7,E-08 | 1,3,E-08 |

**Tabla 67.: Fuentes de Emisión - Escenario 1 parte 11**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_421 | Cam_Valpo_146-PEAS e Imp | 271746 | 6389404 | 3 mes | 321,13 | 1,0,E-07 | 2,5,E-08 | 3,1,E-08 | 5,4,E-08 | 5,4,E-08 | 1,3,E-08 |
| AREA | SRC_422 | Cam_Valpo_147-PEAS e Imp | 271745 | 6389713 | 3 mes | 1235,33 | 2,7,E-08 | 6,5,E-09 | 8,0,E-09 | 1,4,E-08 | 1,4,E-08 | 3,4,E-09 |
| AREA | SRC_423 | Cam_Valpo_148-PEAS e Imp | 271729 | 6389779 | 3 mes | 274,74 | 1,2,E-07 | 2,9,E-08 | 3,6,E-08 | 6,3,E-08 | 6,3,E-08 | 1,5,E-08 |
| AREA | SRC_424 | Cam_Valpo_149-PEAS e Imp | 271405 | 6390771 | 3 mes | 4169,69 | 8,0,E-09 | 1,9,E-09 | 2,4,E-09 | 4,2,E-09 | 4,2,E-09 | 1,0,E-09 |
| AREA | SRC_425 | Cam_Valpo_150-PEAS e Imp | 271408 | 6390852 | 3 mes | 324,07 | 1,0,E-07 | 2,5,E-08 | 3,0,E-08 | 5,4,E-08 | 5,4,E-08 | 1,3,E-08 |
| AREA | SRC_426 | Cam_Valpo_151-PEAS e Imp | 271425 | 6390918 | 3 mes | 269,76 | 1,2,E-07 | 3,0,E-08 | 3,7,E-08 | 6,5,E-08 | 6,5,E-08 | 1,5,E-08 |
| AREA | SRC_427 | Cam_Valpo_152-PEAS e Imp | 271595 | 6391444 | 3 mes | 2210,20 | 1,5,E-08 | 3,6,E-09 | 4,5,E-09 | 7,9,E-09 | 7,9,E-09 | 1,9,E-09 |
| AREA | SRC_428 | Cam_Valpo_153-PEAS e Imp | 271601 | 6391518 | 3 mes | 297,07 | 1,1,E-07 | 2,7,E-08 | 3,3,E-08 | 5,9,E-08 | 5,9,E-08 | 1,4,E-08 |
| AREA | SRC_429 | Cam_Valpo_154-PEAS e Imp | 271583 | 6391599 | 3 mes | 334,56 | 9,9,E-08 | 2,4,E-08 | 2,9,E-08 | 5,2,E-08 | 5,2,E-08 | 1,2,E-08 |
| AREA | SRC_430 | Cam_Valpo_155-PEAS e Imp | 271490 | 6391665 | 3 mes | 462,29 | 7,2,E-08 | 1,7,E-08 | 2,1,E-08 | 3,8,E-08 | 3,8,E-08 | 9,0,E-09 |
| AREA | SRC_431 | Cam_Valpo_156-PEAS e Imp | 271388 | 6391779 | 3 mes | 610,49 | 5,4,E-08 | 1,3,E-08 | 1,6,E-08 | 2,9,E-08 | 2,9,E-08 | 6,8,E-09 |
| AREA | SRC_432 | Cam_Valpo_157-PEAS e Imp | 271303 | 6391969 | 3 mes | 829,95 | 4,0,E-08 | 9,7,E-09 | 1,2,E-08 | 2,1,E-08 | 2,1,E-08 | 5,0,E-09 |
| AREA | SRC_433 | Cam_Valpo_158-PEAS e Imp | 271249 | 6392048 | 3 mes | 385,48 | 8,6,E-08 | 2,1,E-08 | 2,6,E-08 | 4,5,E-08 | 4,5,E-08 | 1,1,E-08 |
| AREA | SRC_434 | Cam_Valpo_159-PEAS e Imp | 271095 | 6392199 | 3 mes | 863,11 | 3,8,E-08 | 9,3,E-09 | 1,1,E-08 | 2,0,E-08 | 2,0,E-08 | 4,8,E-09 |
| AREA | SRC_435 | Cam_Valpo_160-PEAS e Imp | 271003 | 6392357 | 3 mes | 727,41 | 4,6,E-08 | 1,1,E-08 | 1,4,E-08 | 2,4,E-08 | 2,4,E-08 | 5,7,E-09 |
| AREA | SRC_436 | Cam_Valpo_161-PEAS e Imp | 270864 | 6392618 | 3 mes | 1181,67 | 2,8,E-08 | 6,8,E-09 | 8,3,E-09 | 1,5,E-08 | 1,5,E-08 | 3,5,E-09 |
| AREA | SRC_437 | Cam_Valpo_162-PEAS e Imp | 270665 | 6392901 | 3 mes | 1386,67 | 2,4,E-08 | 5,8,E-09 | 7,1,E-09 | 1,3,E-08 | 1,3,E-08 | 3,0,E-09 |
| AREA | SRC_438 | Cam_Valpo_163-PEAS e Imp | 270570 | 6393060 | 3 mes | 739,81 | 4,5,E-08 | 1,1,E-08 | 1,3,E-08 | 2,4,E-08 | 2,4,E-08 | 5,6,E-09 |
| AREA | SRC_439 | Cam_Valpo_164-PEAS e Imp | 270535 | 6393162 | 3 mes | 427,94 | 7,8,E-08 | 1,9,E-08 | 2,3,E-08 | 4,1,E-08 | 4,1,E-08 | 9,7,E-09 |
| AREA | SRC_440 | Cam_Valpo_165-PEAS e Imp | 270408 | 6393157 | 3 mes | 516,16 | 6,4,E-08 | 1,6,E-08 | 1,9,E-08 | 3,4,E-08 | 3,4,E-08 | 8,1,E-09 |
| AREA | SRC_441 | Cam_Valpo_166-PEAS e Imp | 270322 | 6393156 | 3 mes | 344,11 | 9,7,E-08 | 2,3,E-08 | 2,9,E-08 | 5,1,E-08 | 5,1,E-08 | 1,2,E-08 |
| AREA | SRC_442 | Cam_Valpo_167-PEAS e Imp | 270198 | 6393225 | 3 mes | 562,03 | 5,9,E-08 | 1,4,E-08 | 1,8,E-08 | 3,1,E-08 | 3,1,E-08 | 7,4,E-09 |
| AREA | SRC_443 | Cam_Valpo_168-PEAS e Imp | 270084 | 6393222 | 3 mes | 461,57 | 7,2,E-08 | 1,7,E-08 | 2,1,E-08 | 3,8,E-08 | 3,8,E-08 | 9,0,E-09 |
| AREA | SRC_444 | Cam_Valpo_169-PEAS e Imp | 270014 | 6393114 | 3 mes | 520,05 | 6,4,E-08 | 1,5,E-08 | 1,9,E-08 | 3,4,E-08 | 3,4,E-08 | 8,0,E-09 |
| AREA | SRC_445 | Cam_Valpo_170-PEAS e Imp | 269944 | 6393026 | 3 mes | 448,19 | 7,4,E-08 | 1,8,E-08 | 2,2,E-08 | 3,9,E-08 | 3,9,E-08 | 9,3,E-09 |
| AREA | SRC_446 | Cam_Valpo_171-PEAS e Imp | 269831 | 6392981 | 3 mes | 484,35 | 6,9,E-08 | 1,7,E-08 | 2,0,E-08 | 3,6,E-08 | 3,6,E-08 | 8,6,E-09 |
| AREA | SRC_447 | Cam_Valpo_172-PEAS e Imp | 269702 | 6392966 | 3 mes | 516,99 | 6,4,E-08 | 1,6,E-08 | 1,9,E-08 | 3,4,E-08 | 3,4,E-08 | 8,0,E-09 |
| AREA | SRC_448 | Cam_Valpo_173-PEAS e Imp | 269506 | 6393084 | 3 mes | 906,73 | 3,7,E-08 | 8,9,E-09 | 1,1,E-08 | 1,9,E-08 | 1,9,E-08 | 4,6,E-09 |
| AREA | SRC_449 | Cam_Valpo_174-PEAS e Imp | 269407 | 6393106 | 3 mes | 410,62 | 8,1,E-08 | 2,0,E-08 | 2,4,E-08 | 4,2,E-08 | 4,2,E-08 | 1,0,E-08 |
| AREA | SRC_450 | Cam_Valpo_175-PEAS e Imp | 269355 | 6393219 | 3 mes | 493,13 | 6,7,E-08 | 1,6,E-08 | 2,0,E-08 | 3,5,E-08 | 3,5,E-08 | 8,4,E-09 |
| AREA | SRC_451 | Cam_Valpo_176-PEAS e Imp | 269450 | 6393436 | 3 mes | 939,57 | 3,5,E-08 | 8,6,E-09 | 1,0,E-08 | 1,9,E-08 | 1,9,E-08 | 4,4,E-09 |
| AREA | SRC_452 | Cam_Valpo_177-PEAS e Imp | 269537 | 6393768 | 3 mes | 1375,49 | 2,4,E-08 | 5,8,E-09 | 7,2,E-09 | 1,3,E-08 | 1,3,E-08 | 3,0,E-09 |

**Tabla 68.: Fuentes de Emisión - Escenario 1 parte 12**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_453 | Cam_Valpo_178-PEAS e Imp | 269541 | 6393876 | 3 mes | 433,16 | 7,7,E-08 | 1,9,E-08 | 2,3,E-08 | 4,0,E-08 | 4,0,E-08 | 9,6,E-09 |
| AREA | SRC_454 | Cam_Valpo_179-PEAS e Imp | 269514 | 6393952 | 3 mes | 327,49 | 1,0,E-07 | 2,5,E-08 | 3,0,E-08 | 5,3,E-08 | 5,3,E-08 | 1,3,E-08 |
| AREA | SRC_455 | Cam_Valpo_180-PEAS e Imp | 269461 | 6394006 | 3 mes | 302,03 | 1,1,E-07 | 2,7,E-08 | 3,3,E-08 | 5,8,E-08 | 5,8,E-08 | 1,4,E-08 |
| AREA | SRC_456 | Cam_Valpo_181-PEAS e Imp | 269456 | 6394087 | 3 mes | 317,54 | 1,0,E-07 | 2,5,E-08 | 3,1,E-08 | 5,5,E-08 | 5,5,E-08 | 1,3,E-08 |
| AREA | SRC_457 | Cam_Valpo_182-PEAS e Imp | 269494 | 6394169 | 3 mes | 358,94 | 9,3,E-08 | 2,2,E-08 | 2,7,E-08 | 4,9,E-08 | 4,9,E-08 | 1,2,E-08 |
| AREA | SRC_458 | Cam_Valpo_183-PEAS e Imp | 269580 | 6394296 | 3 mes | 611,99 | 5,4,E-08 | 1,3,E-08 | 1,6,E-08 | 2,9,E-08 | 2,9,E-08 | 6,8,E-09 |
| AREA | SRC_459 | Cam_Valpo_184-PEAS e Imp | 269614 | 6394394 | 3 mes | 416,61 | 8,0,E-08 | 1,9,E-08 | 2,4,E-08 | 4,2,E-08 | 4,2,E-08 | 1,0,E-08 |
| AREA | SRC_460 | Cam_Valpo_185-PEAS e Imp | 269617 | 6394492 | 3 mes | 396,57 | 8,4,E-08 | 2,0,E-08 | 2,5,E-08 | 4,4,E-08 | 4,4,E-08 | 1,0,E-08 |
| AREA | SRC_461 | Cam_Valpo_186-PEAS e Imp | 269532 | 6394634 | 3 mes | 664,18 | 5,0,E-08 | 1,2,E-08 | 1,5,E-08 | 2,6,E-08 | 2,6,E-08 | 6,3,E-09 |
| AREA | SRC_462 | Cam_Valpo_187-PEAS e Imp | 269478 | 6394752 | 3 mes | 518,20 | 6,4,E-08 | 1,6,E-08 | 1,9,E-08 | 3,4,E-08 | 3,4,E-08 | 8,0,E-09 |
| AREA | SRC_463 | Cam_Valpo_188-PEAS e Imp | 269437 | 6394881 | 3 mes | 540,93 | 6,1,E-08 | 1,5,E-08 | 1,8,E-08 | 3,2,E-08 | 3,2,E-08 | 7,7,E-09 |
| AREA | SRC_464 | Cam_Valpo_189-PEAS e Imp | 269448 | 6395002 | 3 mes | 483,46 | 6,9,E-08 | 1,7,E-08 | 2,0,E-08 | 3,6,E-08 | 3,6,E-08 | 8,6,E-09 |
| AREA | SRC_465 | Cam_Valpo_190-PEAS e Imp | 269465 | 6395049 | 3 mes | 197,82 | 1,7,E-07 | 4,1,E-08 | 5,0,E-08 | 8,8,E-08 | 8,8,E-08 | 2,1,E-08 |
| AREA | SRC_466 | Cam_Valpo_191-PEAS e Imp | 269701 | 6395188 | 3 mes | 1088,66 | 3,1,E-08 | 7,4,E-09 | 9,0,E-09 | 1,6,E-08 | 1,6,E-08 | 3,8,E-09 |
| AREA | SRC_467 | Cam_Valpo_192-PEAS e Imp | 269737 | 6395244 | 3 mes | 269,38 | 1,2,E-07 | 3,0,E-08 | 3,7,E-08 | 6,5,E-08 | 6,5,E-08 | 1,5,E-08 |
| AREA | SRC_468 | Cam_Valpo_193-PEAS e Imp | 269748 | 6395318 | 3 mes | 301,88 | 1,1,E-07 | 2,7,E-08 | 3,3,E-08 | 5,8,E-08 | 5,8,E-08 | 1,4,E-08 |
| AREA | SRC_469 | Cam_Valpo_194-PEAS e Imp | 269734 | 6395473 | 3 mes | 624,02 | 5,3,E-08 | 1,3,E-08 | 1,6,E-08 | 2,8,E-08 | 2,8,E-08 | 6,7,E-09 |
| AREA | SRC_470 | Cam_Valpo_195-PEAS e Imp | 269791 | 6395575 | 3 mes | 462,91 | 7,2,E-08 | 1,7,E-08 | 2,1,E-08 | 3,8,E-08 | 3,8,E-08 | 9,0,E-09 |
| AREA | SRC_471 | Cam_Valpo_196-PEAS e Imp | 269918 | 6395634 | 3 mes | 557,57 | 6,0,E-08 | 1,4,E-08 | 1,8,E-08 | 3,1,E-08 | 3,1,E-08 | 7,5,E-09 |
| AREA | SRC_472 | Cam_Valpo_197-PEAS e Imp | 269951 | 6395703 | 3 mes | 311,66 | 1,1,E-07 | 2,6,E-08 | 3,2,E-08 | 5,6,E-08 | 5,6,E-08 | 1,3,E-08 |
| AREA | SRC_473 | Cam_Valpo_198-PEAS e Imp | 269926 | 6395767 | 3 mes | 277,87 | 1,2,E-07 | 2,9,E-08 | 3,5,E-08 | 6,3,E-08 | 6,3,E-08 | 1,5,E-08 |
| AREA | SRC_474 | Cam_Valpo_199-PEAS e Imp | 269853 | 6395812 | 3 mes | 348,28 | 9,5,E-08 | 2,3,E-08 | 2,8,E-08 | 5,0,E-08 | 5,0,E-08 | 1,2,E-08 |
| AREA | SRC_475 | Cam_Valpo_200-PEAS e Imp | 269732 | 6395847 | 3 mes | 504,67 | 6,6,E-08 | 1,6,E-08 | 2,0,E-08 | 3,5,E-08 | 3,5,E-08 | 8,2,E-09 |
| AREA | SRC_476 | Cam_Valpo_201-PEAS e Imp | 269688 | 6395928 | 3 mes | 365,46 | 9,1,E-08 | 2,2,E-08 | 2,7,E-08 | 4,8,E-08 | 4,8,E-08 | 1,1,E-08 |
| AREA | SRC_477 | Cam_Valpo_202-PEAS e Imp | 269717 | 6396047 | 3 mes | 484,68 | 6,9,E-08 | 1,7,E-08 | 2,0,E-08 | 3,6,E-08 | 3,6,E-08 | 8,6,E-09 |
| AREA | SRC_478 | Cam_Valpo_203-PEAS e Imp | 269712 | 6396106 | 3 mes | 237,49 | 1,4,E-07 | 3,4,E-08 | 4,1,E-08 | 7,3,E-08 | 7,3,E-08 | 1,7,E-08 |
| AREA | SRC_479 | Cam_Valpo_204-PEAS e Imp | 269657 | 6396143 | 3 mes | 271,48 | 1,2,E-07 | 3,0,E-08 | 3,6,E-08 | 6,4,E-08 | 6,4,E-08 | 1,5,E-08 |
| AREA | SRC_480 | Cam_Valpo_205-PEAS e Imp | 269580 | 6396120 | 3 mes | 326,46 | 1,0,E-07 | 2,5,E-08 | 3,0,E-08 | 5,3,E-08 | 5,3,E-08 | 1,3,E-08 |
| AREA | SRC_481 | Cam_Valpo_206-PEAS e Imp | 269501 | 6396070 | 3 mes | 376,20 | 8,8,E-08 | 2,1,E-08 | 2,6,E-08 | 4,6,E-08 | 4,6,E-08 | 1,1,E-08 |
| AREA | SRC_482 | Cam_Valpo_207-PEAS e Imp | 269359 | 6396026 | 3 mes | 593,54 | 5,6,E-08 | 1,4,E-08 | 1,7,E-08 | 2,9,E-08 | 2,9,E-08 | 7,0,E-09 |
| AREA | SRC_483 | Cam_Valpo_208-PEAS e Imp | 269272 | 6396023 | 3 mes | 343,48 | 9,7,E-08 | 2,3,E-08 | 2,9,E-08 | 5,1,E-08 | 5,1,E-08 | 1,2,E-08 |
| AREA | SRC_484 | Cam_Valpo_209-PEAS e Imp | 269222 | 6396073 | 3 mes | 275,81 | 1,2,E-07 | 2,9,E-08 | 3,6,E-08 | 6,3,E-08 | 6,3,E-08 | 1,5,E-08 |

**Tabla 69.: Fuentes de Emisión - Escenario 1 parte 13**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_485 | Cam_Valpo_210-PEAS e Imp | 269210 | 6396185 | 3 mes | 446,25 | 7,4,E-08 | 1,8,E-08 | 2,2,E-08 | 3,9,E-08 | 3,9,E-08 | 9,3,E-09 |
| AREA | SRC_486 | Cam_Valpo_211-PEAS e Imp | 269167 | 6396232 | 3 mes | 255,46 | 1,3,E-07 | 3,1,E-08 | 3,9,E-08 | 6,8,E-08 | 6,8,E-08 | 1,6,E-08 |
| AREA | SRC_487 | Cam_Valpo_212-PEAS e Imp | 269082 | 6396226 | 3 mes | 349,58 | 9,5,E-08 | 2,3,E-08 | 2,8,E-08 | 5,0,E-08 | 5,0,E-08 | 1,2,E-08 |
| AREA | SRC_488 | Cam_Valpo_213-PEAS e Imp | 268998 | 6396240 | 3 mes | 335,54 | 9,9,E-08 | 2,4,E-08 | 2,9,E-08 | 5,2,E-08 | 5,2,E-08 | 1,2,E-08 |
| AREA | SRC_489 | Cam_Valpo_214-PEAS e Imp | 268894 | 6396300 | 3 mes | 480,09 | 6,9,E-08 | 1,7,E-08 | 2,1,E-08 | 3,6,E-08 | 3,6,E-08 | 8,7,E-09 |
| AREA | SRC_490 | Cam_Valpo_215-PEAS e Imp | 268805 | 6396381 | 3 mes | 477,49 | 7,0,E-08 | 1,7,E-08 | 2,1,E-08 | 3,7,E-08 | 3,7,E-08 | 8,7,E-09 |
| AREA | SRC_491 | Cam_Valpo_216-PEAS e Imp | 268734 | 6396481 | 3 mes | 489,34 | 6,8,E-08 | 1,6,E-08 | 2,0,E-08 | 3,6,E-08 | 3,6,E-08 | 8,5,E-09 |
| AREA | SRC_492 | Cam_Valpo_217-PEAS e Imp | 268692 | 6396569 | 3 mes | 388,32 | 8,6,E-08 | 2,1,E-08 | 2,5,E-08 | 4,5,E-08 | 4,5,E-08 | 1,1,E-08 |
| AREA | SRC_493 | Cam_Valpo_218-PEAS e Imp | 268614 | 6396686 | 3 mes | 563,68 | 5,9,E-08 | 1,4,E-08 | 1,7,E-08 | 3,1,E-08 | 3,1,E-08 | 7,4,E-09 |
| AREA | SRC_494 | Cam_Valpo_219-PEAS e Imp | 268551 | 6396751 | 3 mes | 365,13 | 9,1,E-08 | 2,2,E-08 | 2,7,E-08 | 4,8,E-08 | 4,8,E-08 | 1,1,E-08 |
| AREA | SRC_495 | Cam_Valpo_220-PEAS e Imp | 268525 | 6396834 | 3 mes | 342,75 | 9,7,E-08 | 2,3,E-08 | 2,9,E-08 | 5,1,E-08 | 5,1,E-08 | 1,2,E-08 |
| AREA | SRC_496 | Cam_Valpo_221-PEAS e Imp | 268521 | 6396918 | 3 mes | 335,20 | 9,9,E-08 | 2,4,E-08 | 2,9,E-08 | 5,2,E-08 | 5,2,E-08 | 1,2,E-08 |
| AREA | SRC_497 | Cam_Valpo_222-PEAS e Imp | 268510 | 6396996 | 3 mes | 312,17 | 1,1,E-07 | 2,6,E-08 | 3,2,E-08 | 5,6,E-08 | 5,6,E-08 | 1,3,E-08 |
| AREA | SRC_498 | Cam_Valpo_223-PEAS e Imp | 268441 | 6397095 | 3 mes | 486,78 | 6,8,E-08 | 1,7,E-08 | 2,0,E-08 | 3,6,E-08 | 3,6,E-08 | 8,5,E-09 |
| AREA | SRC_499 | Cam_Valpo_224-PEAS e Imp | 268352 | 6397195 | 3 mes | 537,81 | 6,2,E-08 | 1,5,E-08 | 1,8,E-08 | 3,2,E-08 | 3,2,E-08 | 7,7,E-09 |
| AREA | SRC_500 | Cam_Valpo_225-PEAS e Imp | 268295 | 6397296 | 3 mes | 460,41 | 7,2,E-08 | 1,7,E-08 | 2,1,E-08 | 3,8,E-08 | 3,8,E-08 | 9,0,E-09 |
| AREA | SRC_501 | Cam_Valpo_226-PEAS e Imp | 268265 | 6397370 | 3 mes | 319,00 | 1,0,E-07 | 2,5,E-08 | 3,1,E-08 | 5,5,E-08 | 5,5,E-08 | 1,3,E-08 |
| AREA | SRC_502 | Cam_Valpo_227-PEAS e Imp | 268236 | 6397470 | 3 mes | 414,51 | 8,0,E-08 | 1,9,E-08 | 2,4,E-08 | 4,2,E-08 | 4,2,E-08 | 1,0,E-08 |
| AREA | SRC_503 | Cam_Valpo_228-PEAS e Imp | 268225 | 6397539 | 3 mes | 278,02 | 1,2,E-07 | 2,9,E-08 | 3,5,E-08 | 6,3,E-08 | 6,3,E-08 | 1,5,E-08 |
| AREA | SRC_504 | Cam_Valpo_229-PEAS e Imp | 268212 | 6397650 | 3 mes | 446,47 | 7,4,E-08 | 1,8,E-08 | 2,2,E-08 | 3,9,E-08 | 3,9,E-08 | 9,3,E-09 |
| AREA | SRC_505 | Cam_Valpo_230-PEAS e Imp | 268292 | 6397691 | 3 mes | 352,90 | 9,4,E-08 | 2,3,E-08 | 2,8,E-08 | 4,9,E-08 | 4,9,E-08 | 1,2,E-08 |
| AREA | SRC_506 | Cam_Valpo_231-PEAS e Imp | 268324 | 6397741 | 3 mes | 244,09 | 1,4,E-07 | 3,3,E-08 | 4,0,E-08 | 7,1,E-08 | 7,1,E-08 | 1,7,E-08 |
| AREA | SRC_507 | Cam_Valpo_232-PEAS e Imp | 268344 | 6397809 | 3 mes | 284,52 | 1,2,E-07 | 2,8,E-08 | 3,5,E-08 | 6,1,E-08 | 6,1,E-08 | 1,5,E-08 |
| AREA | SRC_508 | Cam_Valpo_233-PEAS e Imp | 268317 | 6397871 | 3 mes | 277,40 | 1,2,E-07 | 2,9,E-08 | 3,6,E-08 | 6,3,E-08 | 6,3,E-08 | 1,5,E-08 |
| AREA | SRC_509 | Cam_Valpo_234-PEAS e Imp | 268289 | 6397931 | 3 mes | 263,44 | 1,3,E-07 | 3,1,E-08 | 3,7,E-08 | 6,6,E-08 | 6,6,E-08 | 1,6,E-08 |
| AREA | SRC_510 | Cam_Valpo_235-PEAS e Imp | 268281 | 6397993 | 3 mes | 246,21 | 1,3,E-07 | 3,3,E-08 | 4,0,E-08 | 7,1,E-08 | 7,1,E-08 | 1,7,E-08 |
| AREA | SRC_511 | Cam_Valpo_236-PEAS e Imp | 268325 | 6398057 | 3 mes | 307,11 | 1,1,E-07 | 2,6,E-08 | 3,2,E-08 | 5,7,E-08 | 5,7,E-08 | 1,4,E-08 |
| AREA | SRC_512 | Cam_Valpo_237-PEAS e Imp | 268339 | 6398092 | 3 mes | 154,12 | 2,2,E-07 | 5,2,E-08 | 6,4,E-08 | 1,1,E-07 | 1,1,E-07 | 2,7,E-08 |
| AREA | SRC_513 | Cam_Valpo_238-PEAS e Imp | 268362 | 6398151 | 3 mes | 251,56 | 1,3,E-07 | 3,2,E-08 | 3,9,E-08 | 6,9,E-08 | 6,9,E-08 | 1,7,E-08 |
| AREA | SRC_514 | Cam_Valpo_239-PEAS e Imp | 268383 | 6398192 | 3 mes | 185,19 | 1,8,E-07 | 4,3,E-08 | 5,3,E-08 | 9,4,E-08 | 9,4,E-08 | 2,2,E-08 |
| AREA | SRC_515 | Cam_Valpo_240-PEAS e Imp | 268355 | 6398247 | 3 mes | 250,18 | 1,3,E-07 | 3,2,E-08 | 3,9,E-08 | 7,0,E-08 | 7,0,E-08 | 1,7,E-08 |
| AREA | SRC_516 | Cam_Valpo_241-PEAS e Imp | 268227 | 6398303 | 3 mes | 566,84 | 5,9,E-08 | 1,4,E-08 | 1,7,E-08 | 3,1,E-08 | 3,1,E-08 | 7,3,E-09 |

**Tabla 70.: Fuentes de Emisión - Escenario 1 parte 14**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_517 | Cam_Valpo_242-PEAS e Imp | 268140 | 6398362 | 3 mes | 418,83 | 7,9,E-08 | 1,9,E-08 | 2,4,E-08 | 4,2,E-08 | 4,2,E-08 | 9,9,E-09 |
| AREA | SRC_518 | Cam_Valpo_243-PEAS e Imp | 268089 | 6398427 | 3 mes | 325,43 | 1,0,E-07 | 2,5,E-08 | 3,0,E-08 | 5,4,E-08 | 5,4,E-08 | 1,3,E-08 |
| AREA | SRC_519 | Cam_Valpo_244-PEAS e Imp | 268005 | 6398483 | 3 mes | 406,15 | 8,2,E-08 | 2,0,E-08 | 2,4,E-08 | 4,3,E-08 | 4,3,E-08 | 1,0,E-08 |
| AREA | SRC_520 | Cam_Valpo_245-PEAS e Imp | 267956 | 6398553 | 3 mes | 338,26 | 9,8,E-08 | 2,4,E-08 | 2,9,E-08 | 5,2,E-08 | 5,2,E-08 | 1,2,E-08 |
| AREA | SRC_521 | Cam_Valpo_246-PEAS e Imp | 267920 | 6398673 | 3 mes | 498,96 | 6,7,E-08 | 1,6,E-08 | 2,0,E-08 | 3,5,E-08 | 3,5,E-08 | 8,3,E-09 |
| AREA | SRC_522 | Cam_Valpo_247-PEAS e Imp | 267908 | 6398749 | 3 mes | 308,37 | 1,1,E-07 | 2,6,E-08 | 3,2,E-08 | 5,7,E-08 | 5,7,E-08 | 1,3,E-08 |
| AREA | SRC_523 | Cam_Valpo_248-PEAS e Imp | 267894 | 6398771 | 3 mes | 107,41 | 3,1,E-07 | 7,5,E-08 | 9,2,E-08 | 1,6,E-07 | 1,6,E-07 | 3,9,E-08 |
| AREA | SRC_524 | Cam_Valpo_249-PEAS e Imp | 267791 | 6398823 | 3 mes | 466,56 | 7,1,E-08 | 1,7,E-08 | 2,1,E-08 | 3,7,E-08 | 3,7,E-08 | 8,9,E-09 |
| AREA | SRC_525 | Cam_Valpo_250-PEAS e Imp | 267747 | 6398849 | 3 mes | 204,00 | 1,6,E-07 | 3,9,E-08 | 4,8,E-08 | 8,6,E-08 | 8,6,E-08 | 2,0,E-08 |
| AREA | SRC_526 | Cam_Valpo_251-PEAS e Imp | 267699 | 6398875 | 3 mes | 217,15 | 1,5,E-07 | 3,7,E-08 | 4,5,E-08 | 8,0,E-08 | 8,0,E-08 | 1,9,E-08 |
| AREA | SRC_527 | Cam_Valpo_252-PEAS e Imp | 267673 | 6398943 | 3 mes | 285,91 | 1,2,E-07 | 2,8,E-08 | 3,4,E-08 | 6,1,E-08 | 6,1,E-08 | 1,5,E-08 |
| AREA | SRC_528 | Cam_Valpo_253-PEAS e Imp | 267740 | 6399152 | 3 mes | 871,99 | 3,8,E-08 | 9,2,E-09 | 1,1,E-08 | 2,0,E-08 | 2,0,E-08 | 4,8,E-09 |
| AREA | SRC_529 | Cam_Valpo_254-PEAS e Imp | 267754 | 6399259 | 3 mes | 434,37 | 7,6,E-08 | 1,9,E-08 | 2,3,E-08 | 4,0,E-08 | 4,0,E-08 | 9,6,E-09 |
| AREA | SRC_530 | Cam_Valpo_255-PEAS e Imp | 267756 | 6399372 | 3 mes | 452,93 | 7,3,E-08 | 1,8,E-08 | 2,2,E-08 | 3,9,E-08 | 3,9,E-08 | 9,2,E-09 |
| AREA | SRC_531 | Cam_Valpo_256-PEAS e Imp | 267702 | 6399478 | 3 mes | 480,03 | 6,9,E-08 | 1,7,E-08 | 2,1,E-08 | 3,6,E-08 | 3,6,E-08 | 8,7,E-09 |
| AREA | SRC_532 | Cam_Valpo_257-PEAS e Imp | 267740 | 6399547 | 3 mes | 307,21 | 1,1,E-07 | 2,6,E-08 | 3,2,E-08 | 5,7,E-08 | 5,7,E-08 | 1,4,E-08 |
| AREA | SRC_533 | Cam_Valpo_258-PEAS e Imp | 267742 | 6399624 | 3 mes | 311,56 | 1,1,E-07 | 2,6,E-08 | 3,2,E-08 | 5,6,E-08 | 5,6,E-08 | 1,3,E-08 |
| AREA | SRC_534 | Cam_Valpo_259-PEAS e Imp | 267731 | 6399695 | 3 mes | 287,58 | 1,2,E-07 | 2,8,E-08 | 3,4,E-08 | 6,1,E-08 | 6,1,E-08 | 1,4,E-08 |
| AREA | SRC_535 | Cam_Valpo_260-PEAS e Imp | 267682 | 6399788 | 3 mes | 425,70 | 7,8,E-08 | 1,9,E-08 | 2,3,E-08 | 4,1,E-08 | 4,1,E-08 | 9,8,E-09 |
| AREA | SRC_536 | Cam_Valpo_261-PEAS e Imp | 267661 | 6399830 | 3 mes | 187,04 | 1,8,E-07 | 4,3,E-08 | 5,3,E-08 | 9,3,E-08 | 9,3,E-08 | 2,2,E-08 |
| AREA | SRC_537 | PTAS | 273586 | 6383219 | 10 meses | 4,00 | 2,3,E-02 | 1,1,E-02 | 1,1,E-01 | 0,0,E+00 | 0,0,E+00 | 0,0,E+00 |
| AREA | SRC_540 | Cam_Cat_1-PTAS | 273043 | 6387323 | 10 meses | 383,32 | 2,3,E-09 | 5,6,E-10 | 6,9,E-10 | 3,4,E-10 | 8,1,E-09 | 1,9,E-09 |
| AREA | SRC_541 | Cam_Cat_2-PTAS | 273206 | 6387558 | 10 meses | 1145,03 | 7,8,E-10 | 1,9,E-10 | 2,3,E-10 | 1,1,E-10 | 2,7,E-09 | 6,3,E-10 |
| AREA | SRC_542 | Cam_Cat_3-PTAS | 273308 | 6387612 | 10 meses | 456,00 | 2,0,E-09 | 4,7,E-10 | 5,8,E-10 | 2,9,E-10 | 6,8,E-09 | 1,6,E-09 |
| AREA | SRC_543 | Cam_Cat_4-PTAS | 273511 | 6387668 | 10 meses | 843,57 | 1,1,E-09 | 2,6,E-10 | 3,1,E-10 | 1,6,E-10 | 3,7,E-09 | 8,6,E-10 |
| AREA | SRC_544 | Cam_Cat_5-PTAS | 273721 | 6387707 | 10 meses | 853,32 | 1,0,E-09 | 2,5,E-10 | 3,1,E-10 | 1,5,E-10 | 3,7,E-09 | 8,5,E-10 |
| AREA | SRC_545 | Cam_Cat_6-PTAS | 273880 | 6387880 | 10 meses | 945,26 | 9,4,E-10 | 2,3,E-10 | 2,8,E-10 | 1,4,E-10 | 3,3,E-09 | 7,7,E-10 |
| AREA | SRC_546 | Cam_Cat_7-PTAS | 273982 | 6387934 | 10 meses | 457,52 | 2,0,E-09 | 4,7,E-10 | 5,8,E-10 | 2,9,E-10 | 6,8,E-09 | 1,6,E-09 |
| AREA | SRC_547 | Cam_Cat_8-PTAS | 274178 | 6387916 | 10 meses | 782,20 | 1,1,E-09 | 2,8,E-10 | 3,4,E-10 | 1,7,E-10 | 4,0,E-09 | 9,3,E-10 |
| AREA | SRC_548 | Cam_Cat_9-PTAS | 274216 | 6387945 | 10 meses | 195,48 | 4,6,E-09 | 1,1,E-09 | 1,4,E-09 | 6,7,E-10 | 1,6,E-08 | 3,7,E-09 |
| AREA | SRC_549 | Cam_Cat_10-PTAS | 274213 | 6388017 | 10 meses | 295,61 | 3,0,E-09 | 7,3,E-10 | 9,0,E-10 | 4,4,E-10 | 1,1,E-08 | 2,5,E-09 |
| AREA | SRC_550 | Cam_Cat_11-PTAS | 274177 | 6388250 | 10 meses | 941,53 | 9,5,E-10 | 2,3,E-10 | 2,8,E-10 | 1,4,E-10 | 3,3,E-09 | 7,7,E-10 |

**Tabla 71.: Fuentes de Emisión - Escenario 1 parte 15**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_551 | Cam_Cat_12-PTAS | 274185 | 6388365 | 10 meses | 458,34 | 1,9,E-09 | 4,7,E-10 | 5,8,E-10 | 2,9,E-10 | 6,8,E-09 | 1,6,E-09 |
| AREA | SRC_552 | Cam_Cat_13-PTAS | 274352 | 6388558 | 10 meses | 1016,92 | 8,8,E-10 | 2,1,E-10 | 2,6,E-10 | 1,3,E-10 | 3,1,E-09 | 7,1,E-10 |
| AREA | SRC_553 | Cam_Cat_14-PTAS | 274654 | 6388846 | 10 meses | 1667,00 | 5,4,E-10 | 1,3,E-10 | 1,6,E-10 | 7,8,E-11 | 1,9,E-09 | 4,4,E-10 |
| AREA | SRC_554 | Cam_Cat_15-PTAS | 274745 | 6388895 | 10 meses | 409,81 | 2,2,E-09 | 5,3,E-10 | 6,5,E-10 | 3,2,E-10 | 7,6,E-09 | 1,8,E-09 |
| AREA | SRC_555 | Cam_Cat_16-PTAS | 274834 | 6388862 | 10 meses | 371,12 | 2,4,E-09 | 5,8,E-10 | 7,1,E-10 | 3,5,E-10 | 8,4,E-09 | 2,0,E-09 |
| AREA | SRC_556 | Cam_Cat_17-PTAS | 274882 | 6388794 | 10 meses | 331,29 | 2,7,E-09 | 6,5,E-10 | 8,0,E-10 | 3,9,E-10 | 9,4,E-09 | 2,2,E-09 |
| AREA | SRC_557 | Cam_Cat_18-PTAS | 274979 | 6388768 | 10 meses | 406,63 | 2,2,E-09 | 5,3,E-10 | 6,5,E-10 | 3,2,E-10 | 7,7,E-09 | 1,8,E-09 |
| AREA | SRC_558 | Cam_Cat_19-PTAS | 275069 | 6388799 | 10 meses | 384,16 | 2,3,E-09 | 5,6,E-10 | 6,9,E-10 | 3,4,E-10 | 8,1,E-09 | 1,9,E-09 |
| AREA | SRC_559 | Cam_Cat_20-PTAS | 275059 | 6388911 | 10 meses | 459,52 | 1,9,E-09 | 4,7,E-10 | 5,8,E-10 | 2,8,E-10 | 6,8,E-09 | 1,6,E-09 |
| AREA | SRC_560 | Cam_Cat_21-PTAS | 275040 | 6389003 | 10 meses | 374,05 | 2,4,E-09 | 5,8,E-10 | 7,1,E-10 | 3,5,E-10 | 8,3,E-09 | 1,9,E-09 |
| AREA | SRC_561 | Cam_Cat_22-PTAS | 274958 | 6389092 | 10 meses | 489,11 | 1,8,E-09 | 4,4,E-10 | 5,4,E-10 | 2,7,E-10 | 6,4,E-09 | 1,5,E-09 |
| AREA | SRC_562 | Cam_Cat_23-PTAS | 274915 | 6389184 | 10 meses | 402,20 | 2,2,E-09 | 5,4,E-10 | 6,6,E-10 | 3,3,E-10 | 7,8,E-09 | 1,8,E-09 |
| AREA | SRC_563 | Cam_Cat_24-PTAS | 274946 | 6389307 | 10 meses | 502,79 | 1,8,E-09 | 4,3,E-10 | 5,3,E-10 | 2,6,E-10 | 6,2,E-09 | 1,4,E-09 |
| AREA | SRC_564 | Cam_Cat_25-PTAS | 275049 | 6389374 | 10 meses | 485,06 | 1,8,E-09 | 4,5,E-10 | 5,5,E-10 | 2,7,E-10 | 6,4,E-09 | 1,5,E-09 |
| AREA | SRC_565 | Cam_Cat_26-PTAS | 275181 | 6389406 | 10 meses | 541,36 | 1,6,E-09 | 4,0,E-10 | 4,9,E-10 | 2,4,E-10 | 5,8,E-09 | 1,3,E-09 |
| AREA | SRC_566 | Cam_Cat_27-PTAS | 275286 | 6389385 | 10 meses | 424,34 | 2,1,E-09 | 5,1,E-10 | 6,2,E-10 | 3,1,E-10 | 7,4,E-09 | 1,7,E-09 |
| AREA | SRC_567 | Cam_Cat_28-PTAS | 275372 | 6389387 | 10 meses | 345,06 | 2,6,E-09 | 6,3,E-10 | 7,7,E-10 | 3,8,E-10 | 9,0,E-09 | 2,1,E-09 |
| AREA | SRC_568 | Cam_Cat_29-PTAS | 275519 | 6389442 | 10 meses | 633,26 | 1,4,E-09 | 3,4,E-10 | 4,2,E-10 | 2,1,E-10 | 4,9,E-09 | 1,1,E-09 |
| AREA | SRC_569 | Cam_Cat_30-PTAS | 275575 | 6389512 | 10 meses | 360,36 | 2,5,E-09 | 6,0,E-10 | 7,3,E-10 | 3,6,E-10 | 8,7,E-09 | 2,0,E-09 |
| AREA | SRC_570 | Cam_Cat_31-PTAS | 275579 | 6389623 | 10 meses | 447,31 | 2,0,E-09 | 4,8,E-10 | 5,9,E-10 | 2,9,E-10 | 7,0,E-09 | 1,6,E-09 |
| AREA | SRC_571 | Cam_Cat_32-PTAS | 275473 | 6389738 | 10 meses | 629,59 | 1,4,E-09 | 3,4,E-10 | 4,2,E-10 | 2,1,E-10 | 5,0,E-09 | 1,2,E-09 |
| AREA | SRC_572 | Cam_Cat_33-PTAS | 275397 | 6389809 | 10 meses | 419,18 | 2,1,E-09 | 5,2,E-10 | 6,3,E-10 | 3,1,E-10 | 7,4,E-09 | 1,7,E-09 |
| AREA | SRC_573 | Cam_Cat_34-PTAS | 275382 | 6389918 | 10 meses | 432,78 | 2,1,E-09 | 5,0,E-10 | 6,1,E-10 | 3,0,E-10 | 7,2,E-09 | 1,7,E-09 |
| AREA | SRC_574 | Cam_Cat_35-PTAS | 275487 | 6390018 | 10 meses | 576,65 | 1,5,E-09 | 3,7,E-10 | 4,6,E-10 | 2,3,E-10 | 5,4,E-09 | 1,3,E-09 |
| AREA | SRC_575 | Cam_Cat_36-PTAS | 275630 | 6390045 | 10 meses | 576,34 | 1,5,E-09 | 3,7,E-10 | 4,6,E-10 | 2,3,E-10 | 5,4,E-09 | 1,3,E-09 |
| AREA | SRC_576 | Cam_Cat_37-PTAS | 275763 | 6390025 | 10 meses | 532,94 | 1,7,E-09 | 4,1,E-10 | 5,0,E-10 | 2,5,E-10 | 5,9,E-09 | 1,4,E-09 |
| AREA | SRC_577 | Cam_Cat_38-PTAS | 275861 | 6389993 | 10 meses | 411,71 | 2,2,E-09 | 5,2,E-10 | 6,4,E-10 | 3,2,E-10 | 7,6,E-09 | 1,8,E-09 |
| AREA | SRC_578 | Cam_Cat_39-PTAS | 276044 | 6389963 | 10 meses | 742,87 | 1,2,E-09 | 2,9,E-10 | 3,6,E-10 | 1,8,E-10 | 4,2,E-09 | 9,8,E-10 |
| AREA | SRC_579 | Cam_Cat_40-PTAS | 276114 | 6389925 | 10 meses | 316,96 | 2,8,E-09 | 6,8,E-10 | 8,3,E-10 | 4,1,E-10 | 9,8,E-09 | 2,3,E-09 |
| AREA | SRC_580 | Cam_Cat_41-PTAS | 276133 | 6389885 | 10 meses | 172,93 | 5,2,E-09 | 1,2,E-09 | 1,5,E-09 | 7,6,E-10 | 1,8,E-08 | 4,2,E-09 |
| AREA | SRC_581 | Cam_Cat_42-PTAS | 276158 | 6389818 | 10 meses | 286,84 | 3,1,E-09 | 7,5,E-10 | 9,2,E-10 | 4,6,E-10 | 1,1,E-08 | 2,5,E-09 |
| AREA | SRC_582 | Cam_Cat_43-PTAS | 276157 | 6389659 | 10 meses | 632,84 | 1,4,E-09 | 3,4,E-10 | 4,2,E-10 | 2,1,E-10 | 4,9,E-09 | 1,1,E-09 |

**Tabla 72.: Fuentes de Emisión - Escenario 1 parte 16**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_583 | Cam_Cat_44-PTAS | 276172 | 6389529 | 10 meses | 521,10 | 1,7,E-09 | 4,1,E-10 | 5,1,E-10 | 2,5,E-10 | 6,0,E-09 | 1,4,E-09 |
| AREA | SRC_584 | Cam_Cat_45-PTAS | 276275 | 6389477 | 10 meses | 468,32 | 1,9,E-09 | 4,6,E-10 | 5,7,E-10 | 2,8,E-10 | 6,7,E-09 | 1,6,E-09 |
| AREA | SRC_585 | Cam_Cat_46-PTAS | 276411 | 6389458 | 10 meses | 553,37 | 1,6,E-09 | 3,9,E-10 | 4,8,E-10 | 2,4,E-10 | 5,6,E-09 | 1,3,E-09 |
| AREA | SRC_586 | Cam_Cat_47-PTAS | 276501 | 6389471 | 10 meses | 366,24 | 2,4,E-09 | 5,9,E-10 | 7,2,E-10 | 3,6,E-10 | 8,5,E-09 | 2,0,E-09 |
| AREA | SRC_587 | Cam_Cat_48-PTAS | 276706 | 6389673 | 10 meses | 1151,46 | 7,8,E-10 | 1,9,E-10 | 2,3,E-10 | 1,1,E-10 | 2,7,E-09 | 6,3,E-10 |
| AREA | SRC_588 | Cam_Cat_49-PTAS | 277353 | 6390498 | 10 meses | 4195,41 | 2,1,E-10 | 5,1,E-11 | 6,3,E-11 | 3,1,E-11 | 7,4,E-10 | 1,7,E-10 |
| AREA | SRC_589 | Cam_Cat_50-PTAS | 277494 | 6390575 | 10 meses | 640,03 | 1,4,E-09 | 3,4,E-10 | 4,1,E-10 | 2,0,E-10 | 4,9,E-09 | 1,1,E-09 |
| AREA | SRC_590 | Cam_Cat_51-PTAS | 279440 | 6391244 | 10 meses | 8223,68 | 1,1,E-10 | 2,6,E-11 | 3,2,E-11 | 1,6,E-11 | 3,8,E-10 | 8,8,E-11 |
| AREA | SRC_591 | Cam_Cat_52-PTAS | 283346 | 6393239 | 10 meses | 17540,88 | 5,1,E-11 | 1,2,E-11 | 1,5,E-11 | 7,5,E-12 | 1,8,E-10 | 4,1,E-11 |
| AREA | SRC_592 | Cam_Cat_53-PTAS | 287745 | 6394661 | 10 meses | 18483,13 | 4,8,E-11 | 1,2,E-11 | 1,4,E-11 | 7,1,E-12 | 1,7,E-10 | 3,9,E-11 |
| AREA | SRC_593 | Cam_Pta_1-PTAS | 273147 | 6383634 | 10 meses | 1866,42 | 4,8,E-10 | 1,2,E-10 | 1,4,E-10 | 7,0,E-11 | 1,7,E-09 | 3,9,E-10 |
| AREA | SRC_594 | Cam_Pta_2-PTAS | 273165 | 6383642 | 10 meses | 80,85 | 1,1,E-08 | 2,7,E-09 | 3,3,E-09 | 1,6,E-09 | 3,9,E-08 | 9,0,E-09 |
| AREA | SRC_595 | Cam_Pta_3-PTAS | 273189 | 6383637 | 10 meses | 94,14 | 9,5,E-09 | 2,3,E-09 | 2,8,E-09 | 1,4,E-09 | 3,3,E-08 | 7,7,E-09 |
| AREA | SRC_596 | Cam_Pta_4-PTAS | 273241 | 6383562 | 10 meses | 359,95 | 2,5,E-09 | 6,0,E-10 | 7,4,E-10 | 3,6,E-10 | 8,7,E-09 | 2,0,E-09 |
| AREA | SRC_597 | Cam_Pta_5-PTAS | 273289 | 6383445 | 10 meses | 505,57 | 1,8,E-09 | 4,3,E-10 | 5,2,E-10 | 2,6,E-10 | 6,2,E-09 | 1,4,E-09 |
| AREA | SRC_598 | Cam_Pta_6-PTAS | 273304 | 6383402 | 10 meses | 179,62 | 5,0,E-09 | 1,2,E-09 | 1,5,E-09 | 7,3,E-10 | 1,7,E-08 | 4,0,E-09 |
| AREA | SRC_599 | Cam_Pta_7-PTAS | 273331 | 6383382 | 10 meses | 138,45 | 6,4,E-09 | 1,6,E-09 | 1,9,E-09 | 9,5,E-10 | 2,3,E-08 | 5,2,E-09 |
| AREA | SRC_600 | Cam_Pta_8-PTAS | 273361 | 6383362 | 10 meses | 145,56 | 6,1,E-09 | 1,5,E-09 | 1,8,E-09 | 9,0,E-10 | 2,1,E-08 | 5,0,E-09 |
| AREA | SRC_601 | Cam_Pta_9-PTAS | 273393 | 6383346 | 10 meses | 143,99 | 6,2,E-09 | 1,5,E-09 | 1,8,E-09 | 9,1,E-10 | 2,2,E-08 | 5,0,E-09 |
| AREA | SRC_602 | Cam_Pta_10-PTAS | 273413 | 6383324 | 10 meses | 116,32 | 7,7,E-09 | 1,9,E-09 | 2,3,E-09 | 1,1,E-09 | 2,7,E-08 | 6,2,E-09 |
| AREA | SRC_603 | Cam_Pta_11-PTAS | 273447 | 6383229 | 10 meses | 400,03 | 2,2,E-09 | 5,4,E-10 | 6,6,E-10 | 3,3,E-10 | 7,8,E-09 | 1,8,E-09 |
| AREA | SRC_604 | Cam_Pta_12-PTAS | 273463 | 6383220 | 10 meses | 80,13 | 1,1,E-08 | 2,7,E-09 | 3,3,E-09 | 1,6,E-09 | 3,9,E-08 | 9,1,E-09 |
| AREA | SRC_605 | Cam_Pta_13-PTAS | 273473 | 6383218 | 10 meses | 45,12 | 2,0,E-08 | 4,8,E-09 | 5,9,E-09 | 2,9,E-09 | 6,9,E-08 | 1,6,E-08 |
| AREA | SRC_606 | Cam_Pta_14-PTAS | 273519 | 6383228 | 10 meses | 188,53 | 4,7,E-09 | 1,1,E-09 | 1,4,E-09 | 6,9,E-10 | 1,7,E-08 | 3,9,E-09 |
| AREA | SRC_607 | Cam_Valpo_1-PTAS | 267407 | 6370003 | 10 meses | 9181,86 | 9,7,E-11 | 2,4,E-11 | 2,9,E-11 | 1,4,E-11 | 3,4,E-10 | 7,9,E-11 |
| AREA | SRC_608 | Cam_Valpo_2-PTAS | 267402 | 6370088 | 10 meses | 338,29 | 2,6,E-09 | 6,4,E-10 | 7,8,E-10 | 3,9,E-10 | 9,2,E-09 | 2,1,E-09 |
| AREA | SRC_609 | Cam_Valpo_3-PTAS | 267699 | 6371506 | 10 meses | 5788,94 | 1,5,E-10 | 3,7,E-11 | 4,6,E-11 | 2,3,E-11 | 5,4,E-10 | 1,3,E-10 |
| AREA | SRC_610 | Cam_Valpo_4-PTAS | 267700 | 6371619 | 10 meses | 452,00 | 2,0,E-09 | 4,8,E-10 | 5,9,E-10 | 2,9,E-10 | 6,9,E-09 | 1,6,E-09 |
| AREA | SRC_611 | Cam_Valpo_5-PTAS | 267517 | 6371917 | 10 meses | 1401,44 | 6,4,E-10 | 1,5,E-10 | 1,9,E-10 | 9,3,E-11 | 2,2,E-09 | 5,2,E-10 |
| AREA | SRC_612 | Cam_Valpo_6-PTAS | 267499 | 6371980 | 10 meses | 261,10 | 3,4,E-09 | 8,3,E-10 | 1,0,E-09 | 5,0,E-10 | 1,2,E-08 | 2,8,E-09 |
| AREA | SRC_613 | Cam_Valpo_7-PTAS | 267496 | 6372042 | 10 meses | 247,03 | 3,6,E-09 | 8,7,E-10 | 1,1,E-09 | 5,3,E-10 | 1,3,E-08 | 2,9,E-09 |
| AREA | SRC_614 | Cam_Valpo_8-PTAS | 267518 | 6372113 | 10 meses | 294,47 | 3,0,E-09 | 7,3,E-10 | 9,0,E-10 | 4,4,E-10 | 1,1,E-08 | 2,5,E-09 |

**Tabla 73.: Fuentes de Emisión - Escenario 1 parte 17**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_615 | Cam_Valpo_9-PTAS | 267547 | 6372151 | 10 meses | 187,43 | 4,8,E-09 | 1,2,E-09 | 1,4,E-09 | 7,0,E-10 | 1,7,E-08 | 3,9,E-09 |
| AREA | SRC_616 | Cam_Valpo_10-PTAS | 267569 | 6372177 | 10 meses | 137,02 | 6,5,E-09 | 1,6,E-09 | 1,9,E-09 | 9,5,E-10 | 2,3,E-08 | 5,3,E-09 |
| AREA | SRC_617 | Cam_Valpo_11-PTAS | 267738 | 6372319 | 10 meses | 879,83 | 1,0,E-09 | 2,5,E-10 | 3,0,E-10 | 1,5,E-10 | 3,5,E-09 | 8,3,E-10 |
| AREA | SRC_618 | Cam_Valpo_12-PTAS | 267762 | 6372358 | 10 meses | 186,57 | 4,8,E-09 | 1,2,E-09 | 1,4,E-09 | 7,0,E-10 | 1,7,E-08 | 3,9,E-09 |
| AREA | SRC_619 | Cam_Valpo_13-PTAS | 267783 | 6372410 | 10 meses | 224,51 | 4,0,E-09 | 9,6,E-10 | 1,2,E-09 | 5,8,E-10 | 1,4,E-08 | 3,2,E-09 |
| AREA | SRC_620 | Cam_Valpo_14-PTAS | 267855 | 6372669 | 10 meses | 1075,61 | 8,3,E-10 | 2,0,E-10 | 2,5,E-10 | 1,2,E-10 | 2,9,E-09 | 6,7,E-10 |
| AREA | SRC_621 | Cam_Valpo_15-PTAS | 267848 | 6372720 | 10 meses | 207,78 | 4,3,E-09 | 1,0,E-09 | 1,3,E-09 | 6,3,E-10 | 1,5,E-08 | 3,5,E-09 |
| AREA | SRC_622 | Cam_Valpo_16-PTAS | 267715 | 6373066 | 10 meses | 1484,08 | 6,0,E-10 | 1,5,E-10 | 1,8,E-10 | 8,8,E-11 | 2,1,E-09 | 4,9,E-10 |
| AREA | SRC_623 | Cam_Valpo_17-PTAS | 267705 | 6373122 | 10 meses | 225,43 | 4,0,E-09 | 9,6,E-10 | 1,2,E-09 | 5,8,E-10 | 1,4,E-08 | 3,2,E-09 |
| AREA | SRC_624 | Cam_Valpo_18-PTAS | 267701 | 6373182 | 10 meses | 241,22 | 3,7,E-09 | 9,0,E-10 | 1,1,E-09 | 5,4,E-10 | 1,3,E-08 | 3,0,E-09 |
| AREA | SRC_625 | Cam_Valpo_19-PTAS | 267704 | 6373237 | 10 meses | 217,96 | 4,1,E-09 | 9,9,E-10 | 1,2,E-09 | 6,0,E-10 | 1,4,E-08 | 3,3,E-09 |
| AREA | SRC_626 | Cam_Valpo_20-PTAS | 267713 | 6373309 | 10 meses | 291,26 | 3,1,E-09 | 7,4,E-10 | 9,1,E-10 | 4,5,E-10 | 1,1,E-08 | 2,5,E-09 |
| AREA | SRC_627 | Cam_Valpo_21-PTAS | 267741 | 6373522 | 10 meses | 860,16 | 1,0,E-09 | 2,5,E-10 | 3,1,E-10 | 1,5,E-10 | 3,6,E-09 | 8,4,E-10 |
| AREA | SRC_628 | Cam_Valpo_22-PTAS | 267757 | 6373574 | 10 meses | 213,85 | 4,2,E-09 | 1,0,E-09 | 1,2,E-09 | 6,1,E-10 | 1,5,E-08 | 3,4,E-09 |
| AREA | SRC_629 | Cam_Valpo_23-PTAS | 267777 | 6373617 | 10 meses | 187,32 | 4,8,E-09 | 1,2,E-09 | 1,4,E-09 | 7,0,E-10 | 1,7,E-08 | 3,9,E-09 |
| AREA | SRC_630 | Cam_Valpo_24-PTAS | 267817 | 6373719 | 10 meses | 441,14 | 2,0,E-09 | 4,9,E-10 | 6,0,E-10 | 3,0,E-10 | 7,1,E-09 | 1,6,E-09 |
| AREA | SRC_631 | Cam_Valpo_25-PTAS | 267843 | 6373782 | 10 meses | 272,58 | 3,3,E-09 | 7,9,E-10 | 9,7,E-10 | 4,8,E-10 | 1,1,E-08 | 2,7,E-09 |
| AREA | SRC_632 | Cam_Valpo_26-PTAS | 267877 | 6373831 | 10 meses | 236,03 | 3,8,E-09 | 9,2,E-10 | 1,1,E-09 | 5,5,E-10 | 1,3,E-08 | 3,1,E-09 |
| AREA | SRC_633 | Cam_Valpo_27-PTAS | 267910 | 6373883 | 10 meses | 246,12 | 3,6,E-09 | 8,8,E-10 | 1,1,E-09 | 5,3,E-10 | 1,3,E-08 | 2,9,E-09 |
| AREA | SRC_634 | Cam_Valpo_28-PTAS | 268105 | 6374174 | 10 meses | 1399,53 | 6,4,E-10 | 1,5,E-10 | 1,9,E-10 | 9,3,E-11 | 2,2,E-09 | 5,2,E-10 |
| AREA | SRC_635 | Cam_Valpo_29-PTAS | 268274 | 6374430 | 10 meses | 1228,07 | 7,3,E-10 | 1,8,E-10 | 2,2,E-10 | 1,1,E-10 | 2,5,E-09 | 5,9,E-10 |
| AREA | SRC_636 | Cam_Valpo_30-PTAS | 268317 | 6374478 | 10 meses | 254,35 | 3,5,E-09 | 8,5,E-10 | 1,0,E-09 | 5,1,E-10 | 1,2,E-08 | 2,9,E-09 |
| AREA | SRC_637 | Cam_Valpo_31-PTAS | 268347 | 6374502 | 10 meses | 154,46 | 5,8,E-09 | 1,4,E-09 | 1,7,E-09 | 8,5,E-10 | 2,0,E-08 | 4,7,E-09 |
| AREA | SRC_638 | Cam_Valpo_32-PTAS | 269602 | 6375295 | 10 meses | 5935,56 | 1,5,E-10 | 3,6,E-11 | 4,5,E-11 | 2,2,E-11 | 5,3,E-10 | 1,2,E-10 |
| AREA | SRC_639 | Cam_Valpo_33-PTAS | 270646 | 6375956 | 10 meses | 4938,33 | 1,8,E-10 | 4,4,E-11 | 5,4,E-11 | 2,6,E-11 | 6,3,E-10 | 1,5,E-10 |
| AREA | SRC_640 | Cam_Valpo_34-PTAS | 270700 | 6375970 | 10 meses | 220,74 | 4,0,E-09 | 9,8,E-10 | 1,2,E-09 | 5,9,E-10 | 1,4,E-08 | 3,3,E-09 |
| AREA | SRC_641 | Cam_Valpo_35-PTAS | 270759 | 6375972 | 10 meses | 232,03 | 3,8,E-09 | 9,3,E-10 | 1,1,E-09 | 5,6,E-10 | 1,3,E-08 | 3,1,E-09 |
| AREA | SRC_642 | Cam_Valpo_36-PTAS | 270817 | 6375960 | 10 meses | 237,83 | 3,8,E-09 | 9,1,E-10 | 1,1,E-09 | 5,5,E-10 | 1,3,E-08 | 3,1,E-09 |
| AREA | SRC_643 | Cam_Valpo_37-PTAS | 271210 | 6375788 | 10 meses | 1710,95 | 5,2,E-10 | 1,3,E-10 | 1,5,E-10 | 7,6,E-11 | 1,8,E-09 | 4,2,E-10 |
| AREA | SRC_644 | Cam_Valpo_38-PTAS | 271299 | 6375786 | 10 meses | 362,06 | 2,5,E-09 | 6,0,E-10 | 7,3,E-10 | 3,6,E-10 | 8,6,E-09 | 2,0,E-09 |
| AREA | SRC_645 | Cam_Valpo_39-PTAS | 271410 | 6375784 | 10 meses | 444,09 | 2,0,E-09 | 4,9,E-10 | 6,0,E-10 | 2,9,E-10 | 7,0,E-09 | 1,6,E-09 |
| AREA | SRC_646 | Cam_Valpo_40-PTAS | 271537 | 6375829 | 10 meses | 539,94 | 1,7,E-09 | 4,0,E-10 | 4,9,E-10 | 2,4,E-10 | 5,8,E-09 | 1,3,E-09 |

**Tabla 74.: Fuentes de Emisión - Escenario 1 parte 18**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_647 | Cam_Valpo_41-PTAS | 271698 | 6375908 | 10 meses | 717,64 | 1,2,E-09 | 3,0,E-10 | 3,7,E-10 | 1,8,E-10 | 4,3,E-09 | 1,0,E-09 |
| AREA | SRC_648 | Cam_Valpo_42-PTAS | 271943 | 6376040 | 10 meses | 1111,41 | 8,0,E-10 | 1,9,E-10 | 2,4,E-10 | 1,2,E-10 | 2,8,E-09 | 6,5,E-10 |
| AREA | SRC_649 | Cam_Valpo_43-PTAS | 272216 | 6376245 | 10 meses | 1365,82 | 6,5,E-10 | 1,6,E-10 | 1,9,E-10 | 9,6,E-11 | 2,3,E-09 | 5,3,E-10 |
| AREA | SRC_650 | Cam_Valpo_44-PTAS | 272308 | 6376283 | 10 meses | 396,81 | 2,2,E-09 | 5,4,E-10 | 6,7,E-10 | 3,3,E-10 | 7,9,E-09 | 1,8,E-09 |
| AREA | SRC_651 | Cam_Valpo_45-PTAS | 272828 | 6376412 | 10 meses | 2139,51 | 4,2,E-10 | 1,0,E-10 | 1,2,E-10 | 6,1,E-11 | 1,5,E-09 | 3,4,E-10 |
| AREA | SRC_652 | Cam_Valpo_46-PTAS | 272961 | 6376463 | 10 meses | 572,90 | 1,6,E-09 | 3,8,E-10 | 4,6,E-10 | 2,3,E-10 | 5,4,E-09 | 1,3,E-09 |
| AREA | SRC_653 | Cam_Valpo_47-PTAS | 273101 | 6376548 | 10 meses | 656,43 | 1,4,E-09 | 3,3,E-10 | 4,0,E-10 | 2,0,E-10 | 4,8,E-09 | 1,1,E-09 |
| AREA | SRC_654 | Cam_Valpo_48-PTAS | 273683 | 6376890 | 10 meses | 2699,98 | 3,3,E-10 | 8,0,E-11 | 9,8,E-11 | 4,8,E-11 | 1,2,E-09 | 2,7,E-10 |
| AREA | SRC_655 | Cam_Valpo_49-PTAS | 273729 | 6376911 | 10 meses | 198,66 | 4,5,E-09 | 1,1,E-09 | 1,3,E-09 | 6,6,E-10 | 1,6,E-08 | 3,7,E-09 |
| AREA | SRC_656 | Cam_Valpo_50-PTAS | 273841 | 6376934 | 10 meses | 455,50 | 2,0,E-09 | 4,7,E-10 | 5,8,E-10 | 2,9,E-10 | 6,9,E-09 | 1,6,E-09 |
| AREA | SRC_657 | Cam_Valpo_51-PTAS | 273918 | 6376948 | 10 meses | 314,84 | 2,8,E-09 | 6,9,E-10 | 8,4,E-10 | 4,2,E-10 | 9,9,E-09 | 2,3,E-09 |
| AREA | SRC_658 | Cam_Valpo_52-PTAS | 273963 | 6376959 | 10 meses | 182,29 | 4,9,E-09 | 1,2,E-09 | 1,5,E-09 | 7,2,E-10 | 1,7,E-08 | 4,0,E-09 |
| AREA | SRC_659 | Cam_Valpo_53-PTAS | 274013 | 6376981 | 10 meses | 220,22 | 4,1,E-09 | 9,8,E-10 | 1,2,E-09 | 5,9,E-10 | 1,4,E-08 | 3,3,E-09 |
| AREA | SRC_660 | Cam_Valpo_54-PTAS | 274045 | 6377010 | 10 meses | 175,74 | 5,1,E-09 | 1,2,E-09 | 1,5,E-09 | 7,4,E-10 | 1,8,E-08 | 4,1,E-09 |
| AREA | SRC_661 | Cam_Valpo_55-PTAS | 274402 | 6377569 | 10 meses | 2654,98 | 3,4,E-10 | 8,1,E-11 | 1,0,E-10 | 4,9,E-11 | 1,2,E-09 | 2,7,E-10 |
| AREA | SRC_662 | Cam_Valpo_56-PTAS | 274508 | 6377712 | 10 meses | 712,20 | 1,3,E-09 | 3,0,E-10 | 3,7,E-10 | 1,8,E-10 | 4,4,E-09 | 1,0,E-09 |
| AREA | SRC_663 | Cam_Valpo_57-PTAS | 274515 | 6377737 | 10 meses | 105,54 | 8,5,E-09 | 2,0,E-09 | 2,5,E-09 | 1,2,E-09 | 3,0,E-08 | 6,9,E-09 |
| AREA | SRC_664 | Cam_Valpo_58-PTAS | 274530 | 6377783 | 10 meses | 190,85 | 4,7,E-09 | 1,1,E-09 | 1,4,E-09 | 6,9,E-10 | 1,6,E-08 | 3,8,E-09 |
| AREA | SRC_665 | Cam_Valpo_59-PTAS | 274571 | 6378190 | 10 meses | 1640,54 | 5,4,E-10 | 1,3,E-10 | 1,6,E-10 | 8,0,E-11 | 1,9,E-09 | 4,4,E-10 |
| AREA | SRC_666 | Cam_Valpo_60-PTAS | 274512 | 6378662 | 10 meses | 1902,24 | 4,7,E-10 | 1,1,E-10 | 1,4,E-10 | 6,9,E-11 | 1,6,E-09 | 3,8,E-10 |
| AREA | SRC_667 | Cam_Valpo_61-PTAS | 274484 | 6378742 | 10 meses | 339,36 | 2,6,E-09 | 6,4,E-10 | 7,8,E-10 | 3,9,E-10 | 9,2,E-09 | 2,1,E-09 |
| AREA | SRC_668 | Cam_Valpo_62-PTAS | 274397 | 6378959 | 10 meses | 934,88 | 9,5,E-10 | 2,3,E-10 | 2,8,E-10 | 1,4,E-10 | 3,3,E-09 | 7,8,E-10 |
| AREA | SRC_669 | Cam_Valpo_63-PTAS | 274391 | 6379006 | 10 meses | 189,58 | 4,7,E-09 | 1,1,E-09 | 1,4,E-09 | 6,9,E-10 | 1,6,E-08 | 3,8,E-09 |
| AREA | SRC_670 | Cam_Valpo_64-PTAS | 274392 | 6379034 | 10 meses | 109,49 | 8,2,E-09 | 2,0,E-09 | 2,4,E-09 | 1,2,E-09 | 2,9,E-08 | 6,6,E-09 |
| AREA | SRC_671 | Cam_Valpo_65-PTAS | 274513 | 6379469 | 10 meses | 1805,57 | 4,9,E-10 | 1,2,E-10 | 1,5,E-10 | 7,2,E-11 | 1,7,E-09 | 4,0,E-10 |
| AREA | SRC_672 | Cam_Valpo_66-PTAS | 274514 | 6379510 | 10 meses | 163,36 | 5,5,E-09 | 1,3,E-09 | 1,6,E-09 | 8,0,E-10 | 1,9,E-08 | 4,4,E-09 |
| AREA | SRC_673 | Cam_Valpo_67-PTAS | 274503 | 6379560 | 10 meses | 208,73 | 4,3,E-09 | 1,0,E-09 | 1,3,E-09 | 6,3,E-10 | 1,5,E-08 | 3,5,E-09 |
| AREA | SRC_674 | Cam_Valpo_68-PTAS | 274488 | 6379623 | 10 meses | 255,44 | 3,5,E-09 | 8,5,E-10 | 1,0,E-09 | 5,1,E-10 | 1,2,E-08 | 2,8,E-09 |
| AREA | SRC_675 | Cam_Valpo_69-PTAS | 274426 | 6379798 | 10 meses | 745,56 | 1,2,E-09 | 2,9,E-10 | 3,5,E-10 | 1,8,E-10 | 4,2,E-09 | 9,7,E-10 |
| AREA | SRC_676 | Cam_Valpo_70-PTAS | 274386 | 6379897 | 10 meses | 428,53 | 2,1,E-09 | 5,0,E-10 | 6,2,E-10 | 3,1,E-10 | 7,3,E-09 | 1,7,E-09 |
| AREA | SRC_677 | Cam_Valpo_71-PTAS | 274352 | 6379981 | 10 meses | 360,23 | 2,5,E-09 | 6,0,E-10 | 7,3,E-10 | 3,6,E-10 | 8,7,E-09 | 2,0,E-09 |
| AREA | SRC_678 | Cam_Valpo_72-PTAS | 274336 | 6380041 | 10 meses | 249,49 | 3,6,E-09 | 8,7,E-10 | 1,1,E-09 | 5,2,E-10 | 1,3,E-08 | 2,9,E-09 |

**Tabla 75.: Fuentes de Emisión - Escenario 1 parte 19**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_679 | Cam_Valpo_73-PTAS | 274333 | 6380099 | 10 meses | 227,80 | 3,9,E-09 | 9,5,E-10 | 1,2,E-09 | 5,7,E-10 | 1,4,E-08 | 3,2,E-09 |
| AREA | SRC_680 | Cam_Valpo_74-PTAS | 274332 | 6380163 | 10 meses | 257,27 | 3,5,E-09 | 8,4,E-10 | 1,0,E-09 | 5,1,E-10 | 1,2,E-08 | 2,8,E-09 |
| AREA | SRC_681 | Cam_Valpo_75-PTAS | 274329 | 6380546 | 10 meses | 1530,44 | 5,8,E-10 | 1,4,E-10 | 1,7,E-10 | 8,5,E-11 | 2,0,E-09 | 4,7,E-10 |
| AREA | SRC_682 | Cam_Valpo_76-PTAS | 274323 | 6380578 | 10 meses | 130,55 | 6,8,E-09 | 1,7,E-09 | 2,0,E-09 | 1,0,E-09 | 2,4,E-08 | 5,6,E-09 |
| AREA | SRC_683 | Cam_Valpo_77-PTAS | 274308 | 6380608 | 10 meses | 138,17 | 6,5,E-09 | 1,6,E-09 | 1,9,E-09 | 9,5,E-10 | 2,3,E-08 | 5,3,E-09 |
| AREA | SRC_684 | Cam_Valpo_78-PTAS | 274078 | 6381086 | 10 meses | 2120,50 | 4,2,E-10 | 1,0,E-10 | 1,2,E-10 | 6,2,E-11 | 1,5,E-09 | 3,4,E-10 |
| AREA | SRC_685 | Cam_Valpo_79-PTAS | 274036 | 6381146 | 10 meses | 292,96 | 3,0,E-09 | 7,4,E-10 | 9,0,E-10 | 4,5,E-10 | 1,1,E-08 | 2,5,E-09 |
| AREA | SRC_686 | Cam_Valpo_80-PTAS | 273997 | 6381192 | 10 meses | 242,71 | 3,7,E-09 | 8,9,E-10 | 1,1,E-09 | 5,4,E-10 | 1,3,E-08 | 3,0,E-09 |
| AREA | SRC_687 | Cam_Valpo_81-PTAS | 273945 | 6381212 | 10 meses | 225,25 | 4,0,E-09 | 9,6,E-10 | 1,2,E-09 | 5,8,E-10 | 1,4,E-08 | 3,2,E-09 |
| AREA | SRC_688 | Cam_Valpo_82-PTAS | 273863 | 6381235 | 10 meses | 340,59 | 2,6,E-09 | 6,3,E-10 | 7,8,E-10 | 3,8,E-10 | 9,2,E-09 | 2,1,E-09 |
| AREA | SRC_689 | Cam_Valpo_83-PTAS | 273527 | 6381309 | 10 meses | 1376,67 | 6,5,E-10 | 1,6,E-10 | 1,9,E-10 | 9,5,E-11 | 2,3,E-09 | 5,3,E-10 |
| AREA | SRC_690 | Cam_Valpo_84-PTAS | 273488 | 6381317 | 10 meses | 158,83 | 5,6,E-09 | 1,4,E-09 | 1,7,E-09 | 8,2,E-10 | 2,0,E-08 | 4,6,E-09 |
| AREA | SRC_691 | Cam_Valpo_85-PTAS | 273437 | 6381311 | 10 meses | 210,61 | 4,2,E-09 | 1,0,E-09 | 1,3,E-09 | 6,2,E-10 | 1,5,E-08 | 3,4,E-09 |
| AREA | SRC_692 | Cam_Valpo_86-PTAS | 273400 | 6381306 | 10 meses | 148,75 | 6,0,E-09 | 1,5,E-09 | 1,8,E-09 | 8,8,E-10 | 2,1,E-08 | 4,9,E-09 |
| AREA | SRC_693 | Cam_Valpo_87-PTAS | 273330 | 6381278 | 10 meses | 302,02 | 3,0,E-09 | 7,2,E-10 | 8,8,E-10 | 4,3,E-10 | 1,0,E-08 | 2,4,E-09 |
| AREA | SRC_694 | Cam_Valpo_88-PTAS | 273269 | 6381275 | 10 meses | 240,32 | 3,7,E-09 | 9,0,E-10 | 1,1,E-09 | 5,4,E-10 | 1,3,E-08 | 3,0,E-09 |
| AREA | SRC_695 | Cam_Valpo_89-PTAS | 273210 | 6381284 | 10 meses | 238,69 | 3,7,E-09 | 9,0,E-10 | 1,1,E-09 | 5,5,E-10 | 1,3,E-08 | 3,0,E-09 |
| AREA | SRC_696 | Cam_Valpo_90-PTAS | 273140 | 6381307 | 10 meses | 291,89 | 3,1,E-09 | 7,4,E-10 | 9,1,E-10 | 4,5,E-10 | 1,1,E-08 | 2,5,E-09 |
| AREA | SRC_697 | Cam_Valpo_91-PTAS | 273026 | 6381364 | 10 meses | 510,61 | 1,7,E-09 | 4,2,E-10 | 5,2,E-10 | 2,6,E-10 | 6,1,E-09 | 1,4,E-09 |
| AREA | SRC_698 | Cam_Valpo_92-PTAS | 272787 | 6381471 | 10 meses | 1046,47 | 8,5,E-10 | 2,1,E-10 | 2,5,E-10 | 1,3,E-10 | 3,0,E-09 | 6,9,E-10 |
| AREA | SRC_699 | Cam_Valpo_93-PTAS | 272625 | 6381553 | 10 meses | 726,81 | 1,2,E-09 | 3,0,E-10 | 3,6,E-10 | 1,8,E-10 | 4,3,E-09 | 1,0,E-09 |
| AREA | SRC_700 | Cam_Valpo_94-PTAS | 272586 | 6381587 | 10 meses | 205,87 | 4,3,E-09 | 1,0,E-09 | 1,3,E-09 | 6,4,E-10 | 1,5,E-08 | 3,5,E-09 |
| AREA | SRC_701 | Cam_Valpo_95-PTAS | 272567 | 6381621 | 10 meses | 150,25 | 5,9,E-09 | 1,4,E-09 | 1,8,E-09 | 8,7,E-10 | 2,1,E-08 | 4,8,E-09 |
| AREA | SRC_702 | Cam_Valpo_96-PTAS | 272558 | 6381659 | 10 meses | 154,59 | 5,8,E-09 | 1,4,E-09 | 1,7,E-09 | 8,5,E-10 | 2,0,E-08 | 4,7,E-09 |
| AREA | SRC_703 | Cam_Valpo_97-PTAS | 272513 | 6381931 | 10 meses | 1103,20 | 8,1,E-10 | 2,0,E-10 | 2,4,E-10 | 1,2,E-10 | 2,8,E-09 | 6,6,E-10 |
| AREA | SRC_704 | Cam_Valpo_98-PTAS | 272500 | 6382030 | 10 meses | 398,37 | 2,2,E-09 | 5,4,E-10 | 6,6,E-10 | 3,3,E-10 | 7,8,E-09 | 1,8,E-09 |
| AREA | SRC_705 | Cam_Valpo_99-PTAS | 272492 | 6382086 | 10 meses | 223,87 | 4,0,E-09 | 9,6,E-10 | 1,2,E-09 | 5,8,E-10 | 1,4,E-08 | 3,2,E-09 |
| AREA | SRC_706 | Cam_Valpo_100-PTAS | 272491 | 6382127 | 10 meses | 164,32 | 5,4,E-09 | 1,3,E-09 | 1,6,E-09 | 8,0,E-10 | 1,9,E-08 | 4,4,E-09 |
| AREA | SRC_707 | Cam_Valpo_101-PTAS | 272506 | 6382188 | 10 meses | 247,33 | 3,6,E-09 | 8,7,E-10 | 1,1,E-09 | 5,3,E-10 | 1,3,E-08 | 2,9,E-09 |
| AREA | SRC_708 | Cam_Valpo_102-PTAS | 272660 | 6383439 | 10 meses | 5043,31 | 1,8,E-10 | 4,3,E-11 | 5,2,E-11 | 2,6,E-11 | 6,2,E-10 | 1,4,E-10 |
| AREA | SRC_709 | Cam_Valpo_103-PTAS | 272630 | 6384559 | 10 meses | 4478,91 | 2,0,E-10 | 4,8,E-11 | 5,9,E-11 | 2,9,E-11 | 7,0,E-10 | 1,6,E-10 |
| AREA | SRC_710 | Cam_Valpo_104-PTAS | 272626 | 6385227 | 10 meses | 2671,08 | 3,3,E-10 | 8,1,E-11 | 9,9,E-11 | 4,9,E-11 | 1,2,E-09 | 2,7,E-10 |

**Tabla 76.: Fuentes de Emisión - Escenario 1 parte 20**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_711 | Cam_Valpo_105-PTAS | 272602 | 6386454 | 10 meses | 4905,80 | 1,8,E-10 | 4,4,E-11 | 5,4,E-11 | 2,7,E-11 | 6,4,E-10 | 1,5,E-10 |
| AREA | SRC_712 | Cam_Valpo_106-PTAS | 272609 | 6386527 | 10 meses | 292,53 | 3,1,E-09 | 7,4,E-10 | 9,0,E-10 | 4,5,E-10 | 1,1,E-08 | 2,5,E-09 |
| AREA | SRC_713 | Cam_Valpo_107-PTAS | 272650 | 6386615 | 10 meses | 384,69 | 2,3,E-09 | 5,6,E-10 | 6,9,E-10 | 3,4,E-10 | 8,1,E-09 | 1,9,E-09 |
| AREA | SRC_714 | Cam_Valpo_108-PTAS | 272755 | 6386705 | 10 meses | 550,00 | 1,6,E-09 | 3,9,E-10 | 4,8,E-10 | 2,4,E-10 | 5,7,E-09 | 1,3,E-09 |
| AREA | SRC_715 | Cam_Valpo_109-PTAS | 272846 | 6386776 | 10 meses | 460,85 | 1,9,E-09 | 4,7,E-10 | 5,7,E-10 | 2,8,E-10 | 6,8,E-09 | 1,6,E-09 |
| AREA | SRC_716 | Cam_Valpo_110-PTAS | 272918 | 6386821 | 10 meses | 338,79 | 2,6,E-09 | 6,4,E-10 | 7,8,E-10 | 3,9,E-10 | 9,2,E-09 | 2,1,E-09 |
| AREA | SRC_717 | Cam_Valpo_111-PTAS | 272959 | 6386856 | 10 meses | 215,71 | 4,1,E-09 | 1,0,E-09 | 1,2,E-09 | 6,1,E-10 | 1,4,E-08 | 3,4,E-09 |
| AREA | SRC_718 | Cam_Valpo_112-PTAS | 272979 | 6386909 | 10 meses | 229,32 | 3,9,E-09 | 9,4,E-10 | 1,2,E-09 | 5,7,E-10 | 1,4,E-08 | 3,2,E-09 |
| AREA | SRC_719 | Cam_Valpo_113-PTAS | 272982 | 6386950 | 10 meses | 168,20 | 5,3,E-09 | 1,3,E-09 | 1,6,E-09 | 7,8,E-10 | 1,9,E-08 | 4,3,E-09 |
| AREA | SRC_720 | Cam_Valpo_114-PTAS | 272974 | 6387033 | 10 meses | 334,56 | 2,7,E-09 | 6,5,E-10 | 7,9,E-10 | 3,9,E-10 | 9,3,E-09 | 2,2,E-09 |
| AREA | SRC_721 | Cam_Valpo_115-PTAS | 272969 | 6387289 | 10 meses | 1021,26 | 8,7,E-10 | 2,1,E-10 | 2,6,E-10 | 1,3,E-10 | 3,1,E-09 | 7,1,E-10 |
| AREA | SRC_722 | Cam_Valpo_116-PTAS | 272950 | 6387316 | 10 meses | 135,86 | 6,6,E-09 | 1,6,E-09 | 1,9,E-09 | 9,6,E-10 | 2,3,E-08 | 5,3,E-09 |
| AREA | SRC_723 | Cam_Valpo_117-PTAS | 272918 | 6387332 | 10 meses | 150,62 | 5,9,E-09 | 1,4,E-09 | 1,8,E-09 | 8,7,E-10 | 2,1,E-08 | 4,8,E-09 |
| AREA | SRC_724 | Cam_Valpo_118-PTAS | 272871 | 6387328 | 10 meses | 193,11 | 4,6,E-09 | 1,1,E-09 | 1,4,E-09 | 6,8,E-10 | 1,6,E-08 | 3,8,E-09 |
| AREA | SRC_725 | Cam_Valpo_119-PTAS | 272818 | 6387319 | 10 meses | 214,82 | 4,2,E-09 | 1,0,E-09 | 1,2,E-09 | 6,1,E-10 | 1,5,E-08 | 3,4,E-09 |
| AREA | SRC_726 | Cam_Valpo_120-PTAS | 272669 | 6387324 | 10 meses | 593,51 | 1,5,E-09 | 3,6,E-10 | 4,5,E-10 | 2,2,E-10 | 5,3,E-09 | 1,2,E-09 |
| AREA | SRC_727 | Cam_Valpo_121-PTAS | 272536 | 6387380 | 10 meses | 574,11 | 1,6,E-09 | 3,8,E-10 | 4,6,E-10 | 2,3,E-10 | 5,4,E-09 | 1,3,E-09 |
| AREA | SRC_728 | Cam_Valpo_122-PTAS | 272406 | 6387475 | 10 meses | 642,85 | 1,4,E-09 | 3,4,E-10 | 4,1,E-10 | 2,0,E-10 | 4,9,E-09 | 1,1,E-09 |
| AREA | SRC_729 | Cam_Valpo_123-PTAS | 272321 | 6387544 | 10 meses | 438,86 | 2,0,E-09 | 4,9,E-10 | 6,0,E-10 | 3,0,E-10 | 7,1,E-09 | 1,7,E-09 |
| AREA | SRC_730 | Cam_Valpo_124-PTAS | 272252 | 6387605 | 10 meses | 366,01 | 2,4,E-09 | 5,9,E-10 | 7,2,E-10 | 3,6,E-10 | 8,5,E-09 | 2,0,E-09 |
| AREA | SRC_731 | Cam_Valpo_125-PTAS | 272138 | 6387749 | 10 meses | 733,97 | 1,2,E-09 | 2,9,E-10 | 3,6,E-10 | 1,8,E-10 | 4,3,E-09 | 9,9,E-10 |
| AREA | SRC_732 | Cam_Valpo_126-PTAS | 272059 | 6387890 | 10 meses | 645,70 | 1,4,E-09 | 3,3,E-10 | 4,1,E-10 | 2,0,E-10 | 4,8,E-09 | 1,1,E-09 |
| AREA | SRC_733 | Cam_Valpo_127-PTAS | 272019 | 6388008 | 10 meses | 494,29 | 1,8,E-09 | 4,4,E-10 | 5,4,E-10 | 2,6,E-10 | 6,3,E-09 | 1,5,E-09 |
| AREA | SRC_734 | Cam_Valpo_128-PTAS | 272005 | 6388086 | 10 meses | 318,17 | 2,8,E-09 | 6,8,E-10 | 8,3,E-10 | 4,1,E-10 | 9,8,E-09 | 2,3,E-09 |
| AREA | SRC_735 | Cam_Valpo_129-PTAS | 272005 | 6388171 | 10 meses | 338,40 | 2,6,E-09 | 6,4,E-10 | 7,8,E-10 | 3,9,E-10 | 9,2,E-09 | 2,1,E-09 |
| AREA | SRC_736 | Cam_Valpo_130-PTAS | 272018 | 6388207 | 10 meses | 149,40 | 6,0,E-09 | 1,4,E-09 | 1,8,E-09 | 8,8,E-10 | 2,1,E-08 | 4,9,E-09 |
| AREA | SRC_737 | Cam_Valpo_131-PTAS | 272053 | 6388222 | 10 meses | 144,57 | 6,2,E-09 | 1,5,E-09 | 1,8,E-09 | 9,1,E-10 | 2,2,E-08 | 5,0,E-09 |
| AREA | SRC_738 | Cam_Valpo_132-PTAS | 272113 | 6388260 | 10 meses | 286,19 | 3,1,E-09 | 7,5,E-10 | 9,2,E-10 | 4,6,E-10 | 1,1,E-08 | 2,5,E-09 |
| AREA | SRC_739 | Cam_Valpo_133-PTAS | 272165 | 6388289 | 10 meses | 236,50 | 3,8,E-09 | 9,1,E-10 | 1,1,E-09 | 5,5,E-10 | 1,3,E-08 | 3,1,E-09 |
| AREA | SRC_740 | Cam_Valpo_134-PTAS | 272170 | 6388313 | 10 meses | 103,04 | 8,7,E-09 | 2,1,E-09 | 2,6,E-09 | 1,3,E-09 | 3,0,E-08 | 7,0,E-09 |
| AREA | SRC_741 | Cam_Valpo_135-PTAS | 272160 | 6388355 | 10 meses | 178,67 | 5,0,E-09 | 1,2,E-09 | 1,5,E-09 | 7,3,E-10 | 1,7,E-08 | 4,1,E-09 |
| AREA | SRC_742 | Cam_Valpo_136-PTAS | 272116 | 6388384 | 10 meses | 213,17 | 4,2,E-09 | 1,0,E-09 | 1,2,E-09 | 6,1,E-10 | 1,5,E-08 | 3,4,E-09 |

**Tabla 77.: Fuentes de Emisión - Escenario 1 parte 21**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_743 | Cam_Valpo_137-PTAS | 271990 | 6388473 | 10 meses | 618,26 | 1,4,E-09 | 3,5,E-10 | 4,3,E-10 | 2,1,E-10 | 5,0,E-09 | 1,2,E-09 |
| AREA | SRC_744 | Cam_Valpo_138-PTAS | 271909 | 6388570 | 10 meses | 502,24 | 1,8,E-09 | 4,3,E-10 | 5,3,E-10 | 2,6,E-10 | 6,2,E-09 | 1,4,E-09 |
| AREA | SRC_745 | Cam_Valpo_139-PTAS | 271887 | 6388631 | 10 meses | 257,67 | 3,5,E-09 | 8,4,E-10 | 1,0,E-09 | 5,1,E-10 | 1,2,E-08 | 2,8,E-09 |
| AREA | SRC_746 | Cam_Valpo_140-PTAS | 271869 | 6388710 | 10 meses | 324,57 | 2,8,E-09 | 6,7,E-10 | 8,2,E-10 | 4,0,E-10 | 9,6,E-09 | 2,2,E-09 |
| AREA | SRC_747 | Cam_Valpo_141-PTAS | 271879 | 6388778 | 10 meses | 270,72 | 3,3,E-09 | 8,0,E-10 | 9,8,E-10 | 4,8,E-10 | 1,2,E-08 | 2,7,E-09 |
| AREA | SRC_748 | Cam_Valpo_142-PTAS | 271889 | 6388831 | 10 meses | 215,81 | 4,1,E-09 | 1,0,E-09 | 1,2,E-09 | 6,1,E-10 | 1,4,E-08 | 3,4,E-09 |
| AREA | SRC_749 | Cam_Valpo_143-PTAS | 271888 | 6388910 | 10 meses | 317,54 | 2,8,E-09 | 6,8,E-10 | 8,3,E-10 | 4,1,E-10 | 9,8,E-09 | 2,3,E-09 |
| AREA | SRC_750 | Cam_Valpo_144-PTAS | 271765 | 6389249 | 10 meses | 1443,83 | 6,2,E-10 | 1,5,E-10 | 1,8,E-10 | 9,1,E-11 | 2,2,E-09 | 5,0,E-10 |
| AREA | SRC_751 | Cam_Valpo_145-PTAS | 271745 | 6389323 | 10 meses | 308,68 | 2,9,E-09 | 7,0,E-10 | 8,6,E-10 | 4,2,E-10 | 1,0,E-08 | 2,4,E-09 |
| AREA | SRC_752 | Cam_Valpo_146-PTAS | 271746 | 6389404 | 10 meses | 321,13 | 2,8,E-09 | 6,7,E-10 | 8,2,E-10 | 4,1,E-10 | 9,7,E-09 | 2,3,E-09 |
| AREA | SRC_753 | Cam_Valpo_147-PTAS | 271745 | 6389713 | 10 meses | 1235,33 | 7,2,E-10 | 1,7,E-10 | 2,1,E-10 | 1,1,E-10 | 2,5,E-09 | 5,9,E-10 |
| AREA | SRC_754 | Cam_Valpo_148-PTAS | 271729 | 6389779 | 10 meses | 274,74 | 3,2,E-09 | 7,9,E-10 | 9,6,E-10 | 4,8,E-10 | 1,1,E-08 | 2,6,E-09 |
| AREA | SRC_755 | Cam_Valpo_149-PTAS | 271405 | 6390771 | 10 meses | 4169,69 | 2,1,E-10 | 5,2,E-11 | 6,3,E-11 | 3,1,E-11 | 7,5,E-10 | 1,7,E-10 |
| AREA | SRC_756 | Cam_Valpo_150-PTAS | 271408 | 6390852 | 10 meses | 324,07 | 2,8,E-09 | 6,7,E-10 | 8,2,E-10 | 4,0,E-10 | 9,6,E-09 | 2,2,E-09 |
| AREA | SRC_757 | Cam_Valpo_151-PTAS | 271425 | 6390918 | 10 meses | 269,76 | 3,3,E-09 | 8,0,E-10 | 9,8,E-10 | 4,9,E-10 | 1,2,E-08 | 2,7,E-09 |
| AREA | SRC_758 | Cam_Valpo_152-PTAS | 271595 | 6391444 | 10 meses | 2210,20 | 4,0,E-10 | 9,8,E-11 | 1,2,E-10 | 5,9,E-11 | 1,4,E-09 | 3,3,E-10 |
| AREA | SRC_759 | Cam_Valpo_153-PTAS | 271601 | 6391518 | 10 meses | 297,07 | 3,0,E-09 | 7,3,E-10 | 8,9,E-10 | 4,4,E-10 | 1,1,E-08 | 2,4,E-09 |
| AREA | SRC_760 | Cam_Valpo_154-PTAS | 271583 | 6391599 | 10 meses | 334,56 | 2,7,E-09 | 6,5,E-10 | 7,9,E-10 | 3,9,E-10 | 9,3,E-09 | 2,2,E-09 |
| AREA | SRC_761 | Cam_Valpo_155-PTAS | 271490 | 6391665 | 10 meses | 462,29 | 1,9,E-09 | 4,7,E-10 | 5,7,E-10 | 2,8,E-10 | 6,8,E-09 | 1,6,E-09 |
| AREA | SRC_762 | Cam_Valpo_156-PTAS | 271388 | 6391779 | 10 meses | 610,49 | 1,5,E-09 | 3,5,E-10 | 4,3,E-10 | 2,1,E-10 | 5,1,E-09 | 1,2,E-09 |
| AREA | SRC_763 | Cam_Valpo_157-PTAS | 271303 | 6391969 | 10 meses | 829,95 | 1,1,E-09 | 2,6,E-10 | 3,2,E-10 | 1,6,E-10 | 3,8,E-09 | 8,7,E-10 |
| AREA | SRC_764 | Cam_Valpo_158-PTAS | 271249 | 6392048 | 10 meses | 385,48 | 2,3,E-09 | 5,6,E-10 | 6,9,E-10 | 3,4,E-10 | 8,1,E-09 | 1,9,E-09 |
| AREA | SRC_765 | Cam_Valpo_159-PTAS | 271095 | 6392199 | 10 meses | 863,11 | 1,0,E-09 | 2,5,E-10 | 3,1,E-10 | 1,5,E-10 | 3,6,E-09 | 8,4,E-10 |
| AREA | SRC_766 | Cam_Valpo_160-PTAS | 271003 | 6392357 | 10 meses | 727,41 | 1,2,E-09 | 3,0,E-10 | 3,6,E-10 | 1,8,E-10 | 4,3,E-09 | 1,0,E-09 |
| AREA | SRC_767 | Cam_Valpo_161-PTAS | 270864 | 6392618 | 10 meses | 1181,67 | 7,6,E-10 | 1,8,E-10 | 2,2,E-10 | 1,1,E-10 | 2,6,E-09 | 6,1,E-10 |
| AREA | SRC_768 | Cam_Valpo_162-PTAS | 270665 | 6392901 | 10 meses | 1386,67 | 6,4,E-10 | 1,6,E-10 | 1,9,E-10 | 9,4,E-11 | 2,3,E-09 | 5,2,E-10 |
| AREA | SRC_769 | Cam_Valpo_163-PTAS | 270570 | 6393060 | 10 meses | 739,81 | 1,2,E-09 | 2,9,E-10 | 3,6,E-10 | 1,8,E-10 | 4,2,E-09 | 9,8,E-10 |
| AREA | SRC_770 | Cam_Valpo_164-PTAS | 270535 | 6393162 | 10 meses | 427,94 | 2,1,E-09 | 5,0,E-10 | 6,2,E-10 | 3,1,E-10 | 7,3,E-09 | 1,7,E-09 |
| AREA | SRC_771 | Cam_Valpo_165-PTAS | 270408 | 6393157 | 10 meses | 516,16 | 1,7,E-09 | 4,2,E-10 | 5,1,E-10 | 2,5,E-10 | 6,0,E-09 | 1,4,E-09 |
| AREA | SRC_772 | Cam_Valpo_166-PTAS | 270322 | 6393156 | 10 meses | 344,11 | 2,6,E-09 | 6,3,E-10 | 7,7,E-10 | 3,8,E-10 | 9,1,E-09 | 2,1,E-09 |
| AREA | SRC_773 | Cam_Valpo_167-PTAS | 270198 | 6393225 | 10 meses | 562,03 | 1,6,E-09 | 3,8,E-10 | 4,7,E-10 | 2,3,E-10 | 5,6,E-09 | 1,3,E-09 |
| AREA | SRC_774 | Cam_Valpo_168-PTAS | 270084 | 6393222 | 10 meses | 461,57 | 1,9,E-09 | 4,7,E-10 | 5,7,E-10 | 2,8,E-10 | 6,8,E-09 | 1,6,E-09 |

**Tabla 78.: Fuentes de Emisión - Escenario 1 parte 22**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_775 | Cam_Valpo_169-PTAS | 270014 | 6393114 | 10 meses | 520,05 | 1,7,E-09 | 4,2,E-10 | 5,1,E-10 | 2,5,E-10 | 6,0,E-09 | 1,4,E-09 |
| AREA | SRC_776 | Cam_Valpo_170-PTAS | 269944 | 6393026 | 10 meses | 448,19 | 2,0,E-09 | 4,8,E-10 | 5,9,E-10 | 2,9,E-10 | 7,0,E-09 | 1,6,E-09 |
| AREA | SRC_777 | Cam_Valpo_171-PTAS | 269831 | 6392981 | 10 meses | 484,35 | 1,8,E-09 | 4,5,E-10 | 5,5,E-10 | 2,7,E-10 | 6,4,E-09 | 1,5,E-09 |
| AREA | SRC_778 | Cam_Valpo_172-PTAS | 269702 | 6392966 | 10 meses | 516,99 | 1,7,E-09 | 4,2,E-10 | 5,1,E-10 | 2,5,E-10 | 6,0,E-09 | 1,4,E-09 |
| AREA | SRC_779 | Cam_Valpo_173-PTAS | 269506 | 6393084 | 10 meses | 906,73 | 9,8,E-10 | 2,4,E-10 | 2,9,E-10 | 1,4,E-10 | 3,4,E-09 | 8,0,E-10 |
| AREA | SRC_780 | Cam_Valpo_174-PTAS | 269407 | 6393106 | 10 meses | 410,62 | 2,2,E-09 | 5,3,E-10 | 6,4,E-10 | 3,2,E-10 | 7,6,E-09 | 1,8,E-09 |
| AREA | SRC_781 | Cam_Valpo_175-PTAS | 269355 | 6393219 | 10 meses | 493,13 | 1,8,E-09 | 4,4,E-10 | 5,4,E-10 | 2,7,E-10 | 6,3,E-09 | 1,5,E-09 |
| AREA | SRC_782 | Cam_Valpo_176-PTAS | 269450 | 6393436 | 10 meses | 939,57 | 9,5,E-10 | 2,3,E-10 | 2,8,E-10 | 1,4,E-10 | 3,3,E-09 | 7,7,E-10 |
| AREA | SRC_783 | Cam_Valpo_177-PTAS | 269537 | 6393768 | 10 meses | 1375,49 | 6,5,E-10 | 1,6,E-10 | 1,9,E-10 | 9,5,E-11 | 2,3,E-09 | 5,3,E-10 |
| AREA | SRC_784 | Cam_Valpo_178-PTAS | 269541 | 6393876 | 10 meses | 433,16 | 2,1,E-09 | 5,0,E-10 | 6,1,E-10 | 3,0,E-10 | 7,2,E-09 | 1,7,E-09 |
| AREA | SRC_785 | Cam_Valpo_179-PTAS | 269514 | 6393952 | 10 meses | 327,49 | 2,7,E-09 | 6,6,E-10 | 8,1,E-10 | 4,0,E-10 | 9,5,E-09 | 2,2,E-09 |
| AREA | SRC_786 | Cam_Valpo_180-PTAS | 269461 | 6394006 | 10 meses | 302,03 | 3,0,E-09 | 7,2,E-10 | 8,8,E-10 | 4,3,E-10 | 1,0,E-08 | 2,4,E-09 |
| AREA | SRC_787 | Cam_Valpo_181-PTAS | 269456 | 6394087 | 10 meses | 317,54 | 2,8,E-09 | 6,8,E-10 | 8,3,E-10 | 4,1,E-10 | 9,8,E-09 | 2,3,E-09 |
| AREA | SRC_788 | Cam_Valpo_182-PTAS | 269494 | 6394169 | 10 meses | 358,94 | 2,5,E-09 | 6,0,E-10 | 7,4,E-10 | 3,6,E-10 | 8,7,E-09 | 2,0,E-09 |
| AREA | SRC_789 | Cam_Valpo_183-PTAS | 269580 | 6394296 | 10 meses | 611,99 | 1,5,E-09 | 3,5,E-10 | 4,3,E-10 | 2,1,E-10 | 5,1,E-09 | 1,2,E-09 |
| AREA | SRC_790 | Cam_Valpo_184-PTAS | 269614 | 6394394 | 10 meses | 416,61 | 2,1,E-09 | 5,2,E-10 | 6,4,E-10 | 3,1,E-10 | 7,5,E-09 | 1,7,E-09 |
| AREA | SRC_791 | Cam_Valpo_185-PTAS | 269617 | 6394492 | 10 meses | 396,57 | 2,3,E-09 | 5,4,E-10 | 6,7,E-10 | 3,3,E-10 | 7,9,E-09 | 1,8,E-09 |
| AREA | SRC_792 | Cam_Valpo_186-PTAS | 269532 | 6394634 | 10 meses | 664,18 | 1,3,E-09 | 3,3,E-10 | 4,0,E-10 | 2,0,E-10 | 4,7,E-09 | 1,1,E-09 |
| AREA | SRC_793 | Cam_Valpo_187-PTAS | 269478 | 6394752 | 10 meses | 518,20 | 1,7,E-09 | 4,2,E-10 | 5,1,E-10 | 2,5,E-10 | 6,0,E-09 | 1,4,E-09 |
| AREA | SRC_794 | Cam_Valpo_188-PTAS | 269437 | 6394881 | 10 meses | 540,93 | 1,7,E-09 | 4,0,E-10 | 4,9,E-10 | 2,4,E-10 | 5,8,E-09 | 1,3,E-09 |
| AREA | SRC_795 | Cam_Valpo_189-PTAS | 269448 | 6395002 | 10 meses | 483,46 | 1,8,E-09 | 4,5,E-10 | 5,5,E-10 | 2,7,E-10 | 6,5,E-09 | 1,5,E-09 |
| AREA | SRC_796 | Cam_Valpo_190-PTAS | 269465 | 6395049 | 10 meses | 197,82 | 4,5,E-09 | 1,1,E-09 | 1,3,E-09 | 6,6,E-10 | 1,6,E-08 | 3,7,E-09 |
| AREA | SRC_797 | Cam_Valpo_191-PTAS | 269701 | 6395188 | 10 meses | 1088,66 | 8,2,E-10 | 2,0,E-10 | 2,4,E-10 | 1,2,E-10 | 2,9,E-09 | 6,7,E-10 |
| AREA | SRC_798 | Cam_Valpo_192-PTAS | 269737 | 6395244 | 10 meses | 269,38 | 3,3,E-09 | 8,0,E-10 | 9,8,E-10 | 4,9,E-10 | 1,2,E-08 | 2,7,E-09 |
| AREA | SRC_799 | Cam_Valpo_193-PTAS | 269748 | 6395318 | 10 meses | 301,88 | 3,0,E-09 | 7,2,E-10 | 8,8,E-10 | 4,3,E-10 | 1,0,E-08 | 2,4,E-09 |
| AREA | SRC_800 | Cam_Valpo_194-PTAS | 269734 | 6395473 | 10 meses | 624,02 | 1,4,E-09 | 3,5,E-10 | 4,2,E-10 | 2,1,E-10 | 5,0,E-09 | 1,2,E-09 |
| AREA | SRC_801 | Cam_Valpo_195-PTAS | 269791 | 6395575 | 10 meses | 462,91 | 1,9,E-09 | 4,7,E-10 | 5,7,E-10 | 2,8,E-10 | 6,7,E-09 | 1,6,E-09 |
| AREA | SRC_802 | Cam_Valpo_196-PTAS | 269918 | 6395634 | 10 meses | 557,57 | 1,6,E-09 | 3,9,E-10 | 4,7,E-10 | 2,3,E-10 | 5,6,E-09 | 1,3,E-09 |
| AREA | SRC_803 | Cam_Valpo_197-PTAS | 269951 | 6395703 | 10 meses | 311,66 | 2,9,E-09 | 6,9,E-10 | 8,5,E-10 | 4,2,E-10 | 1,0,E-08 | 2,3,E-09 |
| AREA | SRC_804 | Cam_Valpo_198-PTAS | 269926 | 6395767 | 10 meses | 277,87 | 3,2,E-09 | 7,8,E-10 | 9,5,E-10 | 4,7,E-10 | 1,1,E-08 | 2,6,E-09 |
| AREA | SRC_805 | Cam_Valpo_199-PTAS | 269853 | 6395812 | 10 meses | 348,28 | 2,6,E-09 | 6,2,E-10 | 7,6,E-10 | 3,8,E-10 | 9,0,E-09 | 2,1,E-09 |
| AREA | SRC_806 | Cam_Valpo_200-PTAS | 269732 | 6395847 | 10 meses | 504,67 | 1,8,E-09 | 4,3,E-10 | 5,2,E-10 | 2,6,E-10 | 6,2,E-09 | 1,4,E-09 |

**Tabla 79.: Fuentes de Emisión - Escenario 1 parte 23**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_807 | Cam_Valpo_201-PTAS | 269688 | 6395928 | 10 meses | 365,46 | 2,4,E-09 | 5,9,E-10 | 7,2,E-10 | 3,6,E-10 | 8,5,E-09 | 2,0,E-09 |
| AREA | SRC_808 | Cam_Valpo_202-PTAS | 269717 | 6396047 | 10 meses | 484,68 | 1,8,E-09 | 4,5,E-10 | 5,5,E-10 | 2,7,E-10 | 6,4,E-09 | 1,5,E-09 |
| AREA | SRC_809 | Cam_Valpo_203-PTAS | 269712 | 6396106 | 10 meses | 237,49 | 3,8,E-09 | 9,1,E-10 | 1,1,E-09 | 5,5,E-10 | 1,3,E-08 | 3,1,E-09 |
| AREA | SRC_810 | Cam_Valpo_204-PTAS | 269657 | 6396143 | 10 meses | 271,48 | 3,3,E-09 | 8,0,E-10 | 9,7,E-10 | 4,8,E-10 | 1,1,E-08 | 2,7,E-09 |
| AREA | SRC_811 | Cam_Valpo_205-PTAS | 269580 | 6396120 | 10 meses | 326,46 | 2,7,E-09 | 6,6,E-10 | 8,1,E-10 | 4,0,E-10 | 9,6,E-09 | 2,2,E-09 |
| AREA | SRC_812 | Cam_Valpo_206-PTAS | 269501 | 6396070 | 10 meses | 376,20 | 2,4,E-09 | 5,7,E-10 | 7,0,E-10 | 3,5,E-10 | 8,3,E-09 | 1,9,E-09 |
| AREA | SRC_813 | Cam_Valpo_207-PTAS | 269359 | 6396026 | 10 meses | 593,54 | 1,5,E-09 | 3,6,E-10 | 4,5,E-10 | 2,2,E-10 | 5,3,E-09 | 1,2,E-09 |
| AREA | SRC_814 | Cam_Valpo_208-PTAS | 269272 | 6396023 | 10 meses | 343,48 | 2,6,E-09 | 6,3,E-10 | 7,7,E-10 | 3,8,E-10 | 9,1,E-09 | 2,1,E-09 |
| AREA | SRC_815 | Cam_Valpo_209-PTAS | 269222 | 6396073 | 10 meses | 275,81 | 3,2,E-09 | 7,8,E-10 | 9,6,E-10 | 4,7,E-10 | 1,1,E-08 | 2,6,E-09 |
| AREA | SRC_816 | Cam_Valpo_210-PTAS | 269210 | 6396185 | 10 meses | 446,25 | 2,0,E-09 | 4,8,E-10 | 5,9,E-10 | 2,9,E-10 | 7,0,E-09 | 1,6,E-09 |
| AREA | SRC_817 | Cam_Valpo_211-PTAS | 269167 | 6396232 | 10 meses | 255,46 | 3,5,E-09 | 8,5,E-10 | 1,0,E-09 | 5,1,E-10 | 1,2,E-08 | 2,8,E-09 |
| AREA | SRC_818 | Cam_Valpo_212-PTAS | 269082 | 6396226 | 10 meses | 349,58 | 2,6,E-09 | 6,2,E-10 | 7,6,E-10 | 3,7,E-10 | 8,9,E-09 | 2,1,E-09 |
| AREA | SRC_819 | Cam_Valpo_213-PTAS | 268998 | 6396240 | 10 meses | 335,54 | 2,7,E-09 | 6,4,E-10 | 7,9,E-10 | 3,9,E-10 | 9,3,E-09 | 2,2,E-09 |
| AREA | SRC_820 | Cam_Valpo_214-PTAS | 268894 | 6396300 | 10 meses | 480,09 | 1,9,E-09 | 4,5,E-10 | 5,5,E-10 | 2,7,E-10 | 6,5,E-09 | 1,5,E-09 |
| AREA | SRC_821 | Cam_Valpo_215-PTAS | 268805 | 6396381 | 10 meses | 477,49 | 1,9,E-09 | 4,5,E-10 | 5,5,E-10 | 2,7,E-10 | 6,5,E-09 | 1,5,E-09 |
| AREA | SRC_822 | Cam_Valpo_216-PTAS | 268734 | 6396481 | 10 meses | 489,34 | 1,8,E-09 | 4,4,E-10 | 5,4,E-10 | 2,7,E-10 | 6,4,E-09 | 1,5,E-09 |
| AREA | SRC_823 | Cam_Valpo_217-PTAS | 268692 | 6396569 | 10 meses | 388,32 | 2,3,E-09 | 5,6,E-10 | 6,8,E-10 | 3,4,E-10 | 8,0,E-09 | 1,9,E-09 |
| AREA | SRC_824 | Cam_Valpo_218-PTAS | 268614 | 6396686 | 10 meses | 563,68 | 1,6,E-09 | 3,8,E-10 | 4,7,E-10 | 2,3,E-10 | 5,5,E-09 | 1,3,E-09 |
| AREA | SRC_825 | Cam_Valpo_219-PTAS | 268551 | 6396751 | 10 meses | 365,13 | 2,4,E-09 | 5,9,E-10 | 7,2,E-10 | 3,6,E-10 | 8,5,E-09 | 2,0,E-09 |
| AREA | SRC_826 | Cam_Valpo_220-PTAS | 268525 | 6396834 | 10 meses | 342,75 | 2,6,E-09 | 6,3,E-10 | 7,7,E-10 | 3,8,E-10 | 9,1,E-09 | 2,1,E-09 |
| AREA | SRC_827 | Cam_Valpo_221-PTAS | 268521 | 6396918 | 10 meses | 335,20 | 2,7,E-09 | 6,4,E-10 | 7,9,E-10 | 3,9,E-10 | 9,3,E-09 | 2,2,E-09 |
| AREA | SRC_828 | Cam_Valpo_222-PTAS | 268510 | 6396996 | 10 meses | 312,17 | 2,9,E-09 | 6,9,E-10 | 8,5,E-10 | 4,2,E-10 | 1,0,E-08 | 2,3,E-09 |
| AREA | SRC_829 | Cam_Valpo_223-PTAS | 268441 | 6397095 | 10 meses | 486,78 | 1,8,E-09 | 4,4,E-10 | 5,4,E-10 | 2,7,E-10 | 6,4,E-09 | 1,5,E-09 |
| AREA | SRC_830 | Cam_Valpo_224-PTAS | 268352 | 6397195 | 10 meses | 537,81 | 1,7,E-09 | 4,0,E-10 | 4,9,E-10 | 2,4,E-10 | 5,8,E-09 | 1,3,E-09 |
| AREA | SRC_831 | Cam_Valpo_225-PTAS | 268295 | 6397296 | 10 meses | 460,41 | 1,9,E-09 | 4,7,E-10 | 5,7,E-10 | 2,8,E-10 | 6,8,E-09 | 1,6,E-09 |
| AREA | SRC_832 | Cam_Valpo_226-PTAS | 268265 | 6397370 | 10 meses | 319,00 | 2,8,E-09 | 6,8,E-10 | 8,3,E-10 | 4,1,E-10 | 9,8,E-09 | 2,3,E-09 |
| AREA | SRC_833 | Cam_Valpo_227-PTAS | 268236 | 6397470 | 10 meses | 414,51 | 2,2,E-09 | 5,2,E-10 | 6,4,E-10 | 3,2,E-10 | 7,5,E-09 | 1,8,E-09 |
| AREA | SRC_834 | Cam_Valpo_228-PTAS | 268225 | 6397539 | 10 meses | 278,02 | 3,2,E-09 | 7,8,E-10 | 9,5,E-10 | 4,7,E-10 | 1,1,E-08 | 2,6,E-09 |
| AREA | SRC_835 | Cam_Valpo_229-PTAS | 268212 | 6397650 | 10 meses | 446,47 | 2,0,E-09 | 4,8,E-10 | 5,9,E-10 | 2,9,E-10 | 7,0,E-09 | 1,6,E-09 |
| AREA | SRC_836 | Cam_Valpo_230-PTAS | 268292 | 6397691 | 10 meses | 352,90 | 2,5,E-09 | 6,1,E-10 | 7,5,E-10 | 3,7,E-10 | 8,8,E-09 | 2,1,E-09 |
| AREA | SRC_837 | Cam_Valpo_231-PTAS | 268324 | 6397741 | 10 meses | 244,09 | 3,7,E-09 | 8,8,E-10 | 1,1,E-09 | 5,4,E-10 | 1,3,E-08 | 3,0,E-09 |
| AREA | SRC_838 | Cam_Valpo_232-PTAS | 268344 | 6397809 | 10 meses | 284,52 | 3,1,E-09 | 7,6,E-10 | 9,3,E-10 | 4,6,E-10 | 1,1,E-08 | 2,6,E-09 |

**Tabla 80.: Fuentes de Emisión - Escenario 1 parte 24**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_839 | Cam_Valpo_233-PTAS | 268317 | 6397871 | 10 meses | 277,40 | 3,2,E-09 | 7,8,E-10 | 9,5,E-10 | 4,7,E-10 | 1,1,E-08 | 2,6,E-09 |
| AREA | SRC_840 | Cam_Valpo_234-PTAS | 268289 | 6397931 | 10 meses | 263,44 | 3,4,E-09 | 8,2,E-10 | 1,0,E-09 | 5,0,E-10 | 1,2,E-08 | 2,8,E-09 |
| AREA | SRC_841 | Cam_Valpo_235-PTAS | 268281 | 6397993 | 10 meses | 246,21 | 3,6,E-09 | 8,8,E-10 | 1,1,E-09 | 5,3,E-10 | 1,3,E-08 | 2,9,E-09 |
| AREA | SRC_842 | Cam_Valpo_236-PTAS | 268325 | 6398057 | 10 meses | 307,11 | 2,9,E-09 | 7,0,E-10 | 8,6,E-10 | 4,3,E-10 | 1,0,E-08 | 2,4,E-09 |
| AREA | SRC_843 | Cam_Valpo_237-PTAS | 268339 | 6398092 | 10 meses | 154,12 | 5,8,E-09 | 1,4,E-09 | 1,7,E-09 | 8,5,E-10 | 2,0,E-08 | 4,7,E-09 |
| AREA | SRC_844 | Cam_Valpo_238-PTAS | 268362 | 6398151 | 10 meses | 251,56 | 3,5,E-09 | 8,6,E-10 | 1,1,E-09 | 5,2,E-10 | 1,2,E-08 | 2,9,E-09 |
| AREA | SRC_845 | Cam_Valpo_239-PTAS | 268383 | 6398192 | 10 meses | 185,19 | 4,8,E-09 | 1,2,E-09 | 1,4,E-09 | 7,1,E-10 | 1,7,E-08 | 3,9,E-09 |
| AREA | SRC_846 | Cam_Valpo_240-PTAS | 268355 | 6398247 | 10 meses | 250,18 | 3,6,E-09 | 8,6,E-10 | 1,1,E-09 | 5,2,E-10 | 1,2,E-08 | 2,9,E-09 |
| AREA | SRC_847 | Cam_Valpo_241-PTAS | 268227 | 6398303 | 10 meses | 566,84 | 1,6,E-09 | 3,8,E-10 | 4,7,E-10 | 2,3,E-10 | 5,5,E-09 | 1,3,E-09 |
| AREA | SRC_848 | Cam_Valpo_242-PTAS | 268140 | 6398362 | 10 meses | 418,83 | 2,1,E-09 | 5,2,E-10 | 6,3,E-10 | 3,1,E-10 | 7,5,E-09 | 1,7,E-09 |
| AREA | SRC_849 | Cam_Valpo_243-PTAS | 268089 | 6398427 | 10 meses | 325,43 | 2,7,E-09 | 6,6,E-10 | 8,1,E-10 | 4,0,E-10 | 9,6,E-09 | 2,2,E-09 |
| AREA | SRC_850 | Cam_Valpo_244-PTAS | 268005 | 6398483 | 10 meses | 406,15 | 2,2,E-09 | 5,3,E-10 | 6,5,E-10 | 3,2,E-10 | 7,7,E-09 | 1,8,E-09 |
| AREA | SRC_851 | Cam_Valpo_245-PTAS | 267956 | 6398553 | 10 meses | 338,26 | 2,6,E-09 | 6,4,E-10 | 7,8,E-10 | 3,9,E-10 | 9,2,E-09 | 2,1,E-09 |
| AREA | SRC_852 | Cam_Valpo_246-PTAS | 267920 | 6398673 | 10 meses | 498,96 | 1,8,E-09 | 4,3,E-10 | 5,3,E-10 | 2,6,E-10 | 6,3,E-09 | 1,5,E-09 |
| AREA | SRC_853 | Cam_Valpo_247-PTAS | 267908 | 6398749 | 10 meses | 308,37 | 2,9,E-09 | 7,0,E-10 | 8,6,E-10 | 4,2,E-10 | 1,0,E-08 | 2,4,E-09 |
| AREA | SRC_854 | Cam_Valpo_248-PTAS | 267894 | 6398771 | 10 meses | 107,41 | 8,3,E-09 | 2,0,E-09 | 2,5,E-09 | 1,2,E-09 | 2,9,E-08 | 6,8,E-09 |
| AREA | SRC_855 | Cam_Valpo_249-PTAS | 267791 | 6398823 | 10 meses | 466,56 | 1,9,E-09 | 4,6,E-10 | 5,7,E-10 | 2,8,E-10 | 6,7,E-09 | 1,6,E-09 |
| AREA | SRC_856 | Cam_Valpo_250-PTAS | 267747 | 6398849 | 10 meses | 204,00 | 4,4,E-09 | 1,1,E-09 | 1,3,E-09 | 6,4,E-10 | 1,5,E-08 | 3,6,E-09 |
| AREA | SRC_857 | Cam_Valpo_251-PTAS | 267699 | 6398875 | 10 meses | 217,15 | 4,1,E-09 | 9,9,E-10 | 1,2,E-09 | 6,0,E-10 | 1,4,E-08 | 3,3,E-09 |
| AREA | SRC_858 | Cam_Valpo_252-PTAS | 267673 | 6398943 | 10 meses | 285,91 | 3,1,E-09 | 7,6,E-10 | 9,3,E-10 | 4,6,E-10 | 1,1,E-08 | 2,5,E-09 |
| AREA | SRC_859 | Cam_Valpo_253-PTAS | 267740 | 6399152 | 10 meses | 871,99 | 1,0,E-09 | 2,5,E-10 | 3,0,E-10 | 1,5,E-10 | 3,6,E-09 | 8,3,E-10 |
| AREA | SRC_860 | Cam_Valpo_254-PTAS | 267754 | 6399259 | 10 meses | 434,37 | 2,1,E-09 | 5,0,E-10 | 6,1,E-10 | 3,0,E-10 | 7,2,E-09 | 1,7,E-09 |
| AREA | SRC_861 | Cam_Valpo_255-PTAS | 267756 | 6399372 | 10 meses | 452,93 | 2,0,E-09 | 4,8,E-10 | 5,8,E-10 | 2,9,E-10 | 6,9,E-09 | 1,6,E-09 |
| AREA | SRC_862 | Cam_Valpo_256-PTAS | 267702 | 6399478 | 10 meses | 480,03 | 1,9,E-09 | 4,5,E-10 | 5,5,E-10 | 2,7,E-10 | 6,5,E-09 | 1,5,E-09 |
| AREA | SRC_863 | Cam_Valpo_257-PTAS | 267740 | 6399547 | 10 meses | 307,21 | 2,9,E-09 | 7,0,E-10 | 8,6,E-10 | 4,3,E-10 | 1,0,E-08 | 2,4,E-09 |
| AREA | SRC_864 | Cam_Valpo_258-PTAS | 267742 | 6399624 | 10 meses | 311,56 | 2,9,E-09 | 6,9,E-10 | 8,5,E-10 | 4,2,E-10 | 1,0,E-08 | 2,3,E-09 |
| AREA | SRC_865 | Cam_Valpo_259-PTAS | 267731 | 6399695 | 10 meses | 287,58 | 3,1,E-09 | 7,5,E-10 | 9,2,E-10 | 4,6,E-10 | 1,1,E-08 | 2,5,E-09 |
| AREA | SRC_866 | Cam_Valpo_260-PTAS | 267682 | 6399788 | 10 meses | 425,70 | 2,1,E-09 | 5,1,E-10 | 6,2,E-10 | 3,1,E-10 | 7,3,E-09 | 1,7,E-09 |
| AREA | SRC_867 | Cam_Valpo_261-PTAS | 267661 | 6399830 | 10 meses | 187,04 | 4,8,E-09 | 1,2,E-09 | 1,4,E-09 | 7,0,E-10 | 1,7,E-08 | 3,9,E-09 |

**Tabla 81.: Fuentes de Emisión - Escenario 1 parte 25**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/s] | [g/s] | [g/s] | [g/s] | [g/s] | [g/s] |
| VOLUMEN | SRC_104 | Peas_1 | 270864 | 6384350 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_105 | Peas_2 | 271314 | 6385054 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_106 | Peas_3 | 272646 | 6386734 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_107 | Peas_5.1 | 271759 | 6385541 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_108 | Peas_5.2 | 272604 | 6384126 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_109 | Colec_1.1 | 270896 | 6383952 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_110 | Colec_1.2 | 270878 | 6384054 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_111 | Colec_1.3 | 270875 | 6384153 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_112 | Colec_1.4 | 270875 | 6384255 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_113 | Col_1_2.1 | 270933 | 6384852 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_114 | Col_1_2.2 | 271018 | 6384944 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_115 | Col_1_2.3 | 271108 | 6384992 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_116 | Col_1_2.4 | 271205 | 6385003 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_117 | Colec_2.1 | 271536 | 6385456 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_118 | Colec_2.2 | 271642 | 6385470 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_119 | Colec_2.3 | 271736 | 6385514 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_120 | Colec_5.1.1 | 271800 | 6385553 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_121 | Colec_5.1.2 | 271862 | 6385635 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_122 | Colec_5.1.3 | 271917 | 6385717 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_123 | Colec_5.1.4 | 271975 | 6385800 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_124 | Colec_5.1.5 | 272034 | 6385884 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_125 | Colec_5.1.6 | 272065 | 6385985 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_126 | Colec_5.1.7 | 272073 | 6386084 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_127 | Colec_5.1.8 | 272082 | 6386182 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_128 | Colec_5.1.9 | 272094 | 6386285 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_129 | Colec_5.1.10 | 272103 | 6386383 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_130 | Colec_5.1.11 | 272114 | 6386486 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_131 | Colec_5.1.12 | 272124 | 6386586 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_132 | Colec_5.1.13 | 272134 | 6386685 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_133 | Colec_5.1.14 | 272173 | 6386769 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_134 | Colec_5.1.15 | 272227 | 6386790 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_135 | Imp_1.1 | 270871 | 6384375 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |

**Tabla 82.: Fuentes de Emisión - Escenario 1 parte 26**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/s] | [g/s] | [g/s] | [g/s] | [g/s] | [g/s] |
| VOLUMEN | SRC_136 | Imp_1.2 | 270885 | 6384474 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_137 | Imp_1.3 | 270917 | 6384569 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_138 | Imp_1.4 | 270909 | 6384664 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_139 | Imp_1.5 | 270865 | 6384743 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_140 | Imp_2.1 | 271312 | 6385052 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_141 | Imp_2.2 | 271351 | 6385139 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_142 | Imp_2.3 | 271381 | 6385237 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_143 | Imp_2.4 | 271427 | 6385315 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_144 | Imp_2.5 | 271475 | 6385364 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_145 | Imp_3.1 | 272364 | 6386744 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_146 | Imp_3.2 | 272480 | 6386685 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_147 | Imp_3.3 | 272648 | 6386703 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_148 | Imp_5.1.1 | 271783 | 6385539 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_149 | Imp_5.1.2 | 271878 | 6385513 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_150 | Imp_5.1.3 | 271848 | 6385424 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_151 | Imp_5.1.4 | 271860 | 6385341 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_152 | Imp_5.1.5 | 271956 | 6385330 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_153 | Imp_5.1.6 | 272058 | 6385331 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_154 | Imp_5.1.7 | 272158 | 6385331 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_155 | Imp_5.1.8 | 272222 | 6385338 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_156 | Imp_5.1.9 | 272313 | 6385346 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_157 | Imp_5.1.10 | 272287 | 6385238 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_158 | Imp_5.1.11 | 272306 | 6385136 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_159 | Imp_5.1.12 | 272338 | 6385040 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_160 | Imp_5.1.13 | 272409 | 6384843 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_161 | Imp_5.1.14 | 272374 | 6384939 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_162 | Imp_5.1.15 | 272452 | 6384740 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_163 | Imp_5.1.16 | 272490 | 6384643 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_164 | Imp_5.1.17 | 272526 | 6384544 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_165 | Imp_5.1.18 | 272557 | 6384457 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_166 | Imp_5.1.19 | 272601 | 6384362 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_167 | Imp_5.1.20 | 272632 | 6384267 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |

**Tabla 83.: Fuentes de Emisión - Escenario 1 parte 27**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | MPS | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/s] | [g/s] | [g/s] | [g/s] | [g/s] | [g/s] |
| VOLUMEN | SRC_168 | Imp_5.2.1 | 272634 | 6384032 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_169 | Imp_5.2.2 | 272631 | 6383934 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_170 | Imp_5.2.3 | 272632 | 6383831 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_171 | Imp_5.2.4 | 272632 | 6383729 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_172 | Imp_5.2.5 | 272642 | 6383643 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_173 | Imp_5.2.6 | 272748 | 6383641 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_174 | Imp_5.2.7 | 272853 | 6383634 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_175 | Imp_5.2.8 | 272944 | 6383635 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_176 | Imp_5.2.9 | 273065 | 6383635 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_177 | Imp_5.2.10 | 273176 | 6383645 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_178 | Imp_5.2.11 | 273243 | 6383543 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_179 | Imp_5.2.12 | 273291 | 6383445 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_180 | Imp_5.2.13 | 273367 | 6383372 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_181 | Imp_5.2.14 | 273437 | 6383289 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_182 | Imp_5.2.15 | 273519 | 6383235 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_183 | Imp_5.2.16 | 273552 | 6383133 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_184 | IF_1_Redes | 272319 | 6384980 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_185 | IF_2_PTAS | 273522 | 6383276 | 10 meses | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_186 | Tub_1.1 | 272635 | 6383635 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_187 | Tub_1.2 | 272637 | 6383541 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_188 | Tub_1.3 | 272527 | 6383557 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_189 | Tub_1.4 | 272460 | 6383632 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_190 | Tub_1.5 | 272380 | 6383685 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_191 | Tub_1.6 | 272302 | 6383737 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_192 | Tub_1.7 | 272199 | 6383724 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_193 | Tub_1.8 | 272124 | 6383757 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_194 | Tub_1.9 | 272062 | 6383846 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_195 | Tub_1.10 | 271963 | 6383848 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_196 | Tub_1.11 | 271864 | 6383796 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_197 | Tub_1.12 | 271768 | 6383747 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_198 | Tub_1.13 | 271671 | 6383722 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_199 | Tub_1.14 | 271566 | 6383690 | 1 mes | 4,00 | 3,33,E-04 | 5,05,E-05 | 0,000527 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |

**Tabla 84.: Fuentes de Emisión - Escenario 1 parte 28**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/s] | [g/s] | [g/s] | [g/s] | [g/s] |
| VOLUMEN | SRC_35 | colec_6.1 | 270897 | 6383953 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_36 | colec_6.2 | 270933 | 6383856 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_37 | colec_6.3 | 270974 | 6383764 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_38 | colec_6.4 | 271002 | 6383667 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_39 | colec_6.5 | 271030 | 6383560 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_40 | colec_6.6 | 271049 | 6383448 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_41 | colec_6.7 | 271065 | 6383342 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_42 | colec_6.8 | 271079 | 6383231 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_43 | colec_6.9 | 271101 | 6383133 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_44 | colec_6.10 | 271121 | 6383029 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_45 | colec_6.11 | 271136 | 6382924 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_46 | colec_6.12 | 271147 | 6382828 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_47 | colec_6.13 | 271164 | 6382781 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_48 | Colec_8.1 | 272916 | 6386820 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_49 | Colec_8.2 | 272832 | 6386761 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_50 | Colec_8.3 | 272733 | 6386713 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| PUNTUAL | SRC_51 | IF 1 | 272319 | 6384980 | 1 mes | 0,05 | 7,32,E-03 | 1,77,E-03 | 0,00,E+00 | 2,08,E-01 | 4,49,E-02 |
| PUNTUAL | SRC_52 | IF 2 | 273522 | 6383276 | 1 mes | 0,05 | 7,32,E-03 | 1,77,E-03 | 0,00,E+00 | 2,08,E-01 | 4,49,E-02 |

**Tabla 85.: Fuentes de Emisión - Escenario 2 parte 1**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_1 | Peas_6 | 271066 | 6383088 | 1 mes | 4,00 | 2,40,E-03 | 1,20,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_2 | Peas_7 | 273477 | 6387272 | 1 mes | 4,00 | 2,40,E-03 | 1,20,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_3 | Peas_8 | 273248 | 6387021 | 1 mes | 4,00 | 2,40,E-03 | 1,20,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_4 | Imp_6 | 271081 | 6383206 | 1 mes | 4,00 | 2,40,E-03 | 1,20,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_5 | Imp_6.1 | 271071 | 6383155 | 1 mes | 4,00 | 2,40,E-03 | 1,20,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_6 | Imp_7.1 | 273429 | 6387230 | 1 mes | 4,00 | 2,40,E-03 | 1,20,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_7 | Imp_7.2 | 273335 | 6387133 | 1 mes | 4,00 | 2,40,E-03 | 1,20,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_8 | Imp_8.1 | 273085 | 6386931 | 1 mes | 4,00 | 2,40,E-03 | 1,20,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_9 | Imp_8.2 | 272998 | 6386876 | 1 mes | 4,00 | 2,40,E-03 | 1,20,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_10 | colec_6.1 | 270895 | 6383951 | 1 mes | 4,00 | 2,40,E-03 | 1,20,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_11 | colec_6.2 | 270931 | 6383854 | 1 mes | 4,00 | 2,40,E-03 | 1,20,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_12 | colec_6.3 | 270972 | 6383762 | 1 mes | 4,00 | 2,40,E-03 | 1,20,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_13 | colec_6.4 | 271000 | 6383665 | 1 mes | 4,00 | 2,40,E-03 | 1,20,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_14 | colec_6.5 | 271028 | 6383558 | 1 mes | 4,00 | 2,40,E-03 | 1,20,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |

**Tabla 97.: Fuentes de Emisión - Escenario 2 parte 13**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/s] | [g/s] | [g/s] | [g/s] | [g/s] |
| VOLUMEN | SRC_26 | Peas_6 | 271068 | 6383090 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_27 | Peas_7 | 273479 | 6387274 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_28 | Peas_8 | 273250 | 6387023 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_29 | Imp_6 | 271083 | 6383208 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_30 | Imp_6.1 | 271073 | 6383157 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_31 | Imp_7.1 | 273426 | 6387238 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_32 | Imp_7.2 | 273337 | 6387135 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_33 | Imp_8.1 | 273075 | 6386932 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_34 | Imp_8.2 | 272990 | 6386855 | 1 mes | 4,00 | 4,83,E-04 | 7,32,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |

**Tabla 99.: Fuentes de Emisión - Escenario 3 parte 1**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_1 | Peas_9 | 271160 | 6382780 | 1 mes | 4,00 | 2,81,E-03 | 1,37,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_2 | Peas_10 | 271257 | 6382753 | 1 mes | 4,00 | 2,81,E-03 | 1,37,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_3 | Imp_9 | 271319 | 6382719 | 1 mes | 4,00 | 2,81,E-03 | 1,37,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_4 | Imp_10.1 | 271266 | 6382656 | 1 mes | 4,00 | 2,81,E-03 | 1,37,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_5 | Imp_10.2 | 271215 | 6382599 | 1 mes | 4,00 | 2,81,E-03 | 1,37,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_53 | Cam_Cat_1-PEAS e Imp | 273043 | 6387323 | 1 mes | 383,32 | 6,48,E-09 | 1,57,E-09 | 1,31,E-09 | 1,80,E-08 | 4,29,E-09 |

**Tabla 100.: Fuentes de Emisión - Escenario 3 parte 2**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_54 | Cam_Cat_2-PEAS e Imp | 273206 | 6387558 | 1 mes | 1145,03 | 2,17,E-09 | 5,25,E-10 | 4,38,E-10 | 6,04,E-09 | 1,43,E-09 |
| AREA | SRC_55 | Cam_Cat_3-PEAS e Imp | 273308 | 6387612 | 1 mes | 456,00 | 5,45,E-09 | 1,32,E-09 | 1,10,E-09 | 1,52,E-08 | 3,60,E-09 |
| AREA | SRC_56 | Cam_Cat_4-PEAS e Imp | 273511 | 6387668 | 1 mes | 843,57 | 2,95,E-09 | 7,13,E-10 | 5,94,E-10 | 8,20,E-09 | 1,95,E-09 |
| AREA | SRC_57 | Cam_Cat_5-PEAS e Imp | 273721 | 6387707 | 1 mes | 853,32 | 2,91,E-09 | 7,05,E-10 | 5,87,E-10 | 8,10,E-09 | 1,93,E-09 |
| AREA | SRC_58 | Cam_Cat_6-PEAS e Imp | 273880 | 6387880 | 1 mes | 945,26 | 2,63,E-09 | 6,36,E-10 | 5,30,E-10 | 7,32,E-09 | 1,74,E-09 |
| AREA | SRC_59 | Cam_Cat_7-PEAS e Imp | 273982 | 6387934 | 1 mes | 457,52 | 5,43,E-09 | 1,31,E-09 | 1,10,E-09 | 1,51,E-08 | 3,59,E-09 |
| AREA | SRC_60 | Cam_Cat_8-PEAS e Imp | 274178 | 6387916 | 1 mes | 782,20 | 3,18,E-09 | 7,69,E-10 | 6,41,E-10 | 8,84,E-09 | 2,10,E-09 |
| AREA | SRC_61 | Cam_Cat_9-PEAS e Imp | 274216 | 6387945 | 1 mes | 195,48 | 1,27,E-08 | 3,08,E-09 | 2,56,E-09 | 3,54,E-08 | 8,40,E-09 |
| AREA | SRC_62 | Cam_Cat_10-PEAS e Imp | 274213 | 6388017 | 1 mes | 295,61 | 8,41,E-09 | 2,03,E-09 | 1,70,E-09 | 2,34,E-08 | 5,56,E-09 |
| AREA | SRC_63 | Cam_Cat_11-PEAS e Imp | 274177 | 6388250 | 1 mes | 941,53 | 2,64,E-09 | 6,39,E-10 | 5,32,E-10 | 7,34,E-09 | 1,74,E-09 |
| AREA | SRC_64 | Cam_Cat_12-PEAS e Imp | 274185 | 6388365 | 1 mes | 458,34 | 5,42,E-09 | 1,31,E-09 | 1,09,E-09 | 1,51,E-08 | 3,58,E-09 |
| AREA | SRC_65 | Cam_Cat_13-PEAS e Imp | 274352 | 6388558 | 1 mes | 1016,92 | 2,44,E-09 | 5,91,E-10 | 4,93,E-10 | 6,80,E-09 | 1,62,E-09 |
| AREA | SRC_66 | Cam_Cat_14-PEAS e Imp | 274654 | 6388846 | 1 mes | 1667,00 | 1,49,E-09 | 3,61,E-10 | 3,01,E-10 | 4,15,E-09 | 9,85,E-10 |
| AREA | SRC_67 | Cam_Cat_15-PEAS e Imp | 274745 | 6388895 | 1 mes | 409,81 | 6,07,E-09 | 1,47,E-09 | 1,22,E-09 | 1,69,E-08 | 4,01,E-09 |
| AREA | SRC_68 | Cam_Cat_16-PEAS e Imp | 274834 | 6388862 | 1 mes | 371,12 | 6,70,E-09 | 1,62,E-09 | 1,35,E-09 | 1,86,E-08 | 4,43,E-09 |
| AREA | SRC_69 | Cam_Cat_17-PEAS e Imp | 274882 | 6388794 | 1 mes | 331,29 | 7,50,E-09 | 1,82,E-09 | 1,51,E-09 | 2,09,E-08 | 4,96,E-09 |
| AREA | SRC_70 | Cam_Cat_18-PEAS e Imp | 274979 | 6388768 | 1 mes | 406,63 | 6,11,E-09 | 1,48,E-09 | 1,23,E-09 | 1,70,E-08 | 4,04,E-09 |
| AREA | SRC_71 | Cam_Cat_19-PEAS e Imp | 275069 | 6388799 | 1 mes | 384,16 | 6,47,E-09 | 1,57,E-09 | 1,30,E-09 | 1,80,E-08 | 4,28,E-09 |
| AREA | SRC_72 | Cam_Cat_20-PEAS e Imp | 275059 | 6388911 | 1 mes | 459,52 | 5,41,E-09 | 1,31,E-09 | 1,09,E-09 | 1,50,E-08 | 3,57,E-09 |
| AREA | SRC_73 | Cam_Cat_21-PEAS e Imp | 275040 | 6389003 | 1 mes | 374,05 | 6,64,E-09 | 1,61,E-09 | 1,34,E-09 | 1,85,E-08 | 4,39,E-09 |
| AREA | SRC_74 | Cam_Cat_22-PEAS e Imp | 274958 | 6389092 | 1 mes | 489,11 | 5,08,E-09 | 1,23,E-09 | 1,02,E-09 | 1,41,E-08 | 3,36,E-09 |
| AREA | SRC_75 | Cam_Cat_23-PEAS e Imp | 274915 | 6389184 | 1 mes | 402,20 | 6,18,E-09 | 1,50,E-09 | 1,25,E-09 | 1,72,E-08 | 4,08,E-09 |
| AREA | SRC_76 | Cam_Cat_24-PEAS e Imp | 274946 | 6389307 | 1 mes | 502,79 | 4,94,E-09 | 1,20,E-09 | 9,97,E-10 | 1,38,E-08 | 3,27,E-09 |
| AREA | SRC_77 | Cam_Cat_25-PEAS e Imp | 275049 | 6389374 | 1 mes | 485,06 | 5,12,E-09 | 1,24,E-09 | 1,03,E-09 | 1,43,E-08 | 3,39,E-09 |
| AREA | SRC_78 | Cam_Cat_26-PEAS e Imp | 275181 | 6389406 | 1 mes | 541,36 | 4,59,E-09 | 1,11,E-09 | 9,26,E-10 | 1,28,E-08 | 3,03,E-09 |
| AREA | SRC_79 | Cam_Cat_27-PEAS e Imp | 275286 | 6389385 | 1 mes | 424,34 | 5,86,E-09 | 1,42,E-09 | 1,18,E-09 | 1,63,E-08 | 3,87,E-09 |
| AREA | SRC_80 | Cam_Cat_28-PEAS e Imp | 275372 | 6389387 | 1 mes | 345,06 | 7,20,E-09 | 1,74,E-09 | 1,45,E-09 | 2,00,E-08 | 4,76,E-09 |
| AREA | SRC_81 | Cam_Cat_29-PEAS e Imp | 275519 | 6389442 | 1 mes | 633,26 | 3,93,E-09 | 9,50,E-10 | 7,91,E-10 | 1,09,E-08 | 2,59,E-09 |
| AREA | SRC_82 | Cam_Cat_30-PEAS e Imp | 275575 | 6389512 | 1 mes | 360,36 | 6,90,E-09 | 1,67,E-09 | 1,39,E-09 | 1,92,E-08 | 4,56,E-09 |
| AREA | SRC_83 | Cam_Cat_31-PEAS e Imp | 275579 | 6389623 | 1 mes | 447,31 | 5,56,E-09 | 1,34,E-09 | 1,12,E-09 | 1,55,E-08 | 3,67,E-09 |
| AREA | SRC_84 | Cam_Cat_32-PEAS e Imp | 275473 | 6389738 | 1 mes | 629,59 | 3,95,E-09 | 9,55,E-10 | 7,96,E-10 | 1,10,E-08 | 2,61,E-09 |
| AREA | SRC_85 | Cam_Cat_33-PEAS e Imp | 275397 | 6389809 | 1 mes | 419,18 | 5,93,E-09 | 1,43,E-09 | 1,20,E-09 | 1,65,E-08 | 3,92,E-09 |

**Tabla 101.: Fuentes de Emisión - Escenario 3 parte 3**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_86 | Cam_Cat_34-PEAS e Imp | 275382 | 6389918 | 1 mes | 432,78 | 5,74,E-09 | 1,39,E-09 | 1,16,E-09 | 1,60,E-08 | 3,80,E-09 |
| AREA | SRC_87 | Cam_Cat_35-PEAS e Imp | 275487 | 6390018 | 1 mes | 576,65 | 4,31,E-09 | 1,04,E-09 | 8,69,E-10 | 1,20,E-08 | 2,85,E-09 |
| AREA | SRC_88 | Cam_Cat_36-PEAS e Imp | 275630 | 6390045 | 1 mes | 576,34 | 4,31,E-09 | 1,04,E-09 | 8,69,E-10 | 1,20,E-08 | 2,85,E-09 |
| AREA | SRC_89 | Cam_Cat_37-PEAS e Imp | 275763 | 6390025 | 1 mes | 532,94 | 4,66,E-09 | 1,13,E-09 | 9,40,E-10 | 1,30,E-08 | 3,08,E-09 |
| AREA | SRC_90 | Cam_Cat_38-PEAS e Imp | 275861 | 6389993 | 1 mes | 411,71 | 6,04,E-09 | 1,46,E-09 | 1,22,E-09 | 1,68,E-08 | 3,99,E-09 |
| AREA | SRC_91 | Cam_Cat_39-PEAS e Imp | 276044 | 6389963 | 1 mes | 742,87 | 3,35,E-09 | 8,09,E-10 | 6,75,E-10 | 9,31,E-09 | 2,21,E-09 |
| AREA | SRC_92 | Cam_Cat_40-PEAS e Imp | 276114 | 6389925 | 1 mes | 316,96 | 7,84,E-09 | 1,90,E-09 | 1,58,E-09 | 2,18,E-08 | 5,18,E-09 |
| AREA | SRC_93 | Cam_Cat_41-PEAS e Imp | 276133 | 6389885 | 1 mes | 172,93 | 1,44,E-08 | 3,48,E-09 | 2,90,E-09 | 4,00,E-08 | 9,50,E-09 |
| AREA | SRC_94 | Cam_Cat_42-PEAS e Imp | 276158 | 6389818 | 1 mes | 286,84 | 8,67,E-09 | 2,10,E-09 | 1,75,E-09 | 2,41,E-08 | 5,73,E-09 |
| AREA | SRC_95 | Cam_Cat_43-PEAS e Imp | 276157 | 6389659 | 1 mes | 632,84 | 3,93,E-09 | 9,50,E-10 | 7,92,E-10 | 1,09,E-08 | 2,60,E-09 |
| AREA | SRC_96 | Cam_Cat_44-PEAS e Imp | 276172 | 6389529 | 1 mes | 521,10 | 4,77,E-09 | 1,15,E-09 | 9,62,E-10 | 1,33,E-08 | 3,15,E-09 |
| AREA | SRC_97 | Cam_Cat_45-PEAS e Imp | 276275 | 6389477 | 1 mes | 468,32 | 5,31,E-09 | 1,28,E-09 | 1,07,E-09 | 1,48,E-08 | 3,51,E-09 |
| AREA | SRC_98 | Cam_Cat_46-PEAS e Imp | 276411 | 6389458 | 1 mes | 553,37 | 4,49,E-09 | 1,09,E-09 | 9,06,E-10 | 1,25,E-08 | 2,97,E-09 |
| AREA | SRC_99 | Cam_Cat_47-PEAS e Imp | 276501 | 6389471 | 1 mes | 366,24 | 6,79,E-09 | 1,64,E-09 | 1,37,E-09 | 1,89,E-08 | 4,49,E-09 |
| AREA | SRC_100 | Cam_Cat_48-PEAS e Imp | 276706 | 6389673 | 1 mes | 1151,46 | 2,16,E-09 | 5,22,E-10 | 4,35,E-10 | 6,01,E-09 | 1,43,E-09 |
| AREA | SRC_101 | Cam_Cat_49-PEAS e Imp | 277353 | 6390498 | 1 mes | 4195,41 | 5,92,E-10 | 1,43,E-10 | 1,19,E-10 | 1,65,E-09 | 3,92,E-10 |
| AREA | SRC_102 | Cam_Cat_50-PEAS e Imp | 277494 | 6390575 | 1 mes | 640,03 | 3,88,E-09 | 9,40,E-10 | 7,83,E-10 | 1,08,E-08 | 2,57,E-09 |
| AREA | SRC_103 | Cam_Cat_51-PEAS e Imp | 279440 | 6391244 | 1 mes | 8223,68 | 3,02,E-10 | 7,31,E-11 | 6,09,E-11 | 8,41,E-10 | 2,00,E-10 |
| AREA | SRC_104 | Cam_Cat_52-PEAS e Imp | 283346 | 6393239 | 1 mes | 17540,88 | 1,42,E-10 | 3,43,E-11 | 2,86,E-11 | 3,94,E-10 | 9,36,E-11 |
| AREA | SRC_105 | Cam_Cat_53-PEAS e Imp | 287745 | 6394661 | 1 mes | 18483,13 | 1,34,E-10 | 3,25,E-11 | 2,71,E-11 | 3,74,E-10 | 8,89,E-11 |
| AREA | SRC_106 | Cam_Pta_1-PEAS e Imp | 273147 | 6383634 | 1 mes | 1866,42 | 1,33,E-09 | 3,22,E-10 | 2,68,E-10 | 3,71,E-09 | 8,80,E-10 |
| AREA | SRC_107 | Cam_Pta_2-PEAS e Imp | 273165 | 6383642 | 1 mes | 80,85 | 3,07,E-08 | 7,44,E-09 | 6,20,E-09 | 8,55,E-08 | 2,03,E-08 |
| AREA | SRC_108 | Cam_Pta_3-PEAS e Imp | 273189 | 6383637 | 1 mes | 94,14 | 2,64,E-08 | 6,39,E-09 | 5,32,E-09 | 7,35,E-08 | 1,74,E-08 |
| AREA | SRC_109 | Cam_Pta_4-PEAS e Imp | 273241 | 6383562 | 1 mes | 359,95 | 6,91,E-09 | 1,67,E-09 | 1,39,E-09 | 1,92,E-08 | 4,56,E-09 |
| AREA | SRC_110 | Cam_Pta_5-PEAS e Imp | 273289 | 6383445 | 1 mes | 505,57 | 4,92,E-09 | 1,19,E-09 | 9,91,E-10 | 1,37,E-08 | 3,25,E-09 |
| AREA | SRC_111 | Cam_Pta_6-PEAS e Imp | 273304 | 6383402 | 1 mes | 179,62 | 1,38,E-08 | 3,35,E-09 | 2,79,E-09 | 3,85,E-08 | 9,15,E-09 |
| AREA | SRC_112 | Cam_Pta_7-PEAS e Imp | 273331 | 6383382 | 1 mes | 138,45 | 1,80,E-08 | 4,34,E-09 | 3,62,E-09 | 4,99,E-08 | 1,19,E-08 |
| AREA | SRC_113 | Cam_Pta_8-PEAS e Imp | 273361 | 6383362 | 1 mes | 145,56 | 1,71,E-08 | 4,13,E-09 | 3,44,E-09 | 4,75,E-08 | 1,13,E-08 |
| AREA | SRC_114 | Cam_Pta_9-PEAS e Imp | 273393 | 6383346 | 1 mes | 143,99 | 1,73,E-08 | 4,18,E-09 | 3,48,E-09 | 4,80,E-08 | 1,14,E-08 |
| AREA | SRC_115 | Cam_Pta_10-PEAS e Imp | 273413 | 6383324 | 1 mes | 116,32 | 2,14,E-08 | 5,17,E-09 | 4,31,E-09 | 5,95,E-08 | 1,41,E-08 |
| AREA | SRC_116 | Cam_Pta_11-PEAS e Imp | 273447 | 6383229 | 1 mes | 400,03 | 6,21,E-09 | 1,50,E-09 | 1,25,E-09 | 1,73,E-08 | 4,11,E-09 |
| AREA | SRC_117 | Cam_Pta_12-PEAS e Imp | 273463 | 6383220 | 1 mes | 80,13 | 3,10,E-08 | 7,50,E-09 | 6,25,E-09 | 8,63,E-08 | 2,05,E-08 |

**Tabla 102.: Fuentes de Emisión - Escenario 3 parte 4**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_118 | Cam_Pta_13-PEAS e Imp | 273473 | 6383218 | 1 mes | 45,12 | 5,51,E-08 | 1,33,E-08 | 1,11,E-08 | 1,53,E-07 | 3,64,E-08 |
| AREA | SRC_119 | Cam_Pta_14-PEAS e Imp | 273519 | 6383228 | 1 mes | 188,53 | 1,32,E-08 | 3,19,E-09 | 2,66,E-09 | 3,67,E-08 | 8,71,E-09 |
| AREA | SRC_120 | Cam_Valpo_1-PEAS e Imp | 267407 | 6370003 | 1 mes | 9181,86 | 2,71,E-10 | 6,55,E-11 | 5,46,E-11 | 7,53,E-10 | 1,79,E-10 |
| AREA | SRC_121 | Cam_Valpo_2-PEAS e Imp | 267402 | 6370088 | 1 mes | 338,29 | 7,35,E-09 | 1,78,E-09 | 1,48,E-09 | 2,04,E-08 | 4,86,E-09 |
| AREA | SRC_122 | Cam_Valpo_3-PEAS e Imp | 267699 | 6371506 | 1 mes | 5788,94 | 4,29,E-10 | 1,04,E-10 | 8,66,E-11 | 1,19,E-09 | 2,84,E-10 |
| AREA | SRC_123 | Cam_Valpo_4-PEAS e Imp | 267700 | 6371619 | 1 mes | 452,00 | 5,50,E-09 | 1,33,E-09 | 1,11,E-09 | 1,53,E-08 | 3,63,E-09 |
| AREA | SRC_124 | Cam_Valpo_5-PEAS e Imp | 267517 | 6371917 | 1 mes | 1401,44 | 1,77,E-09 | 4,29,E-10 | 3,58,E-10 | 4,93,E-09 | 1,17,E-09 |
| AREA | SRC_125 | Cam_Valpo_6-PEAS e Imp | 267499 | 6371980 | 1 mes | 261,10 | 9,52,E-09 | 2,30,E-09 | 1,92,E-09 | 2,65,E-08 | 6,29,E-09 |
| AREA | SRC_126 | Cam_Valpo_7-PEAS e Imp | 267496 | 6372042 | 1 mes | 247,03 | 1,01,E-08 | 2,43,E-09 | 2,03,E-09 | 2,80,E-08 | 6,65,E-09 |
| AREA | SRC_127 | Cam_Valpo_8-PEAS e Imp | 267518 | 6372113 | 1 mes | 294,47 | 8,44,E-09 | 2,04,E-09 | 1,70,E-09 | 2,35,E-08 | 5,58,E-09 |
| AREA | SRC_128 | Cam_Valpo_9-PEAS e Imp | 267547 | 6372151 | 1 mes | 187,43 | 1,33,E-08 | 3,21,E-09 | 2,67,E-09 | 3,69,E-08 | 8,76,E-09 |
| AREA | SRC_129 | Cam_Valpo_10-PEAS e Imp | 267569 | 6372177 | 1 mes | 137,02 | 1,81,E-08 | 4,39,E-09 | 3,66,E-09 | 5,05,E-08 | 1,20,E-08 |
| AREA | SRC_130 | Cam_Valpo_11-PEAS e Imp | 267738 | 6372319 | 1 mes | 879,83 | 2,83,E-09 | 6,83,E-10 | 5,70,E-10 | 7,86,E-09 | 1,87,E-09 |
| AREA | SRC_131 | Cam_Valpo_12-PEAS e Imp | 267762 | 6372358 | 1 mes | 186,57 | 1,33,E-08 | 3,22,E-09 | 2,69,E-09 | 3,71,E-08 | 8,80,E-09 |
| AREA | SRC_132 | Cam_Valpo_13-PEAS e Imp | 267783 | 6372410 | 1 mes | 224,51 | 1,11,E-08 | 2,68,E-09 | 2,23,E-09 | 3,08,E-08 | 7,32,E-09 |
| AREA | SRC_133 | Cam_Valpo_14-PEAS e Imp | 267855 | 6372669 | 1 mes | 1075,61 | 2,31,E-09 | 5,59,E-10 | 4,66,E-10 | 6,43,E-09 | 1,53,E-09 |
| AREA | SRC_134 | Cam_Valpo_15-PEAS e Imp | 267848 | 6372720 | 1 mes | 207,78 | 1,20,E-08 | 2,89,E-09 | 2,41,E-09 | 3,33,E-08 | 7,91,E-09 |
| AREA | SRC_135 | Cam_Valpo_16-PEAS e Imp | 267715 | 6373066 | 1 mes | 1484,08 | 1,67,E-09 | 4,05,E-10 | 3,38,E-10 | 4,66,E-09 | 1,11,E-09 |
| AREA | SRC_136 | Cam_Valpo_17-PEAS e Imp | 267705 | 6373122 | 1 mes | 225,43 | 1,10,E-08 | 2,67,E-09 | 2,22,E-09 | 3,07,E-08 | 7,29,E-09 |
| AREA | SRC_137 | Cam_Valpo_18-PEAS e Imp | 267701 | 6373182 | 1 mes | 241,22 | 1,03,E-08 | 2,49,E-09 | 2,08,E-09 | 2,87,E-08 | 6,81,E-09 |
| AREA | SRC_138 | Cam_Valpo_19-PEAS e Imp | 267704 | 6373237 | 1 mes | 217,96 | 1,14,E-08 | 2,76,E-09 | 2,30,E-09 | 3,17,E-08 | 7,54,E-09 |
| AREA | SRC_139 | Cam_Valpo_20-PEAS e Imp | 267713 | 6373309 | 1 mes | 291,26 | 8,53,E-09 | 2,06,E-09 | 1,72,E-09 | 2,37,E-08 | 5,64,E-09 |
| AREA | SRC_140 | Cam_Valpo_21-PEAS e Imp | 267741 | 6373522 | 1 mes | 860,16 | 2,89,E-09 | 6,99,E-10 | 5,83,E-10 | 8,04,E-09 | 1,91,E-09 |
| AREA | SRC_141 | Cam_Valpo_22-PEAS e Imp | 267757 | 6373574 | 1 mes | 213,85 | 1,16,E-08 | 2,81,E-09 | 2,34,E-09 | 3,23,E-08 | 7,68,E-09 |
| AREA | SRC_142 | Cam_Valpo_23-PEAS e Imp | 267777 | 6373617 | 1 mes | 187,32 | 1,33,E-08 | 3,21,E-09 | 2,68,E-09 | 3,69,E-08 | 8,77,E-09 |
| AREA | SRC_143 | Cam_Valpo_24-PEAS e Imp | 267817 | 6373719 | 1 mes | 441,14 | 5,63,E-09 | 1,36,E-09 | 1,14,E-09 | 1,57,E-08 | 3,72,E-09 |
| AREA | SRC_144 | Cam_Valpo_25-PEAS e Imp | 267843 | 6373782 | 1 mes | 272,58 | 9,12,E-09 | 2,21,E-09 | 1,84,E-09 | 2,54,E-08 | 6,03,E-09 |
| AREA | SRC_145 | Cam_Valpo_26-PEAS e Imp | 267877 | 6373831 | 1 mes | 236,03 | 1,05,E-08 | 2,55,E-09 | 2,12,E-09 | 2,93,E-08 | 6,96,E-09 |
| AREA | SRC_146 | Cam_Valpo_27-PEAS e Imp | 267910 | 6373883 | 1 mes | 246,12 | 1,01,E-08 | 2,44,E-09 | 2,04,E-09 | 2,81,E-08 | 6,67,E-09 |
| AREA | SRC_147 | Cam_Valpo_28-PEAS e Imp | 268105 | 6374174 | 1 mes | 1399,53 | 1,78,E-09 | 4,30,E-10 | 3,58,E-10 | 4,94,E-09 | 1,17,E-09 |
| AREA | SRC_148 | Cam_Valpo_29-PEAS e Imp | 268274 | 6374430 | 1 mes | 1228,07 | 2,02,E-09 | 4,90,E-10 | 4,08,E-10 | 5,63,E-09 | 1,34,E-09 |
| AREA | SRC_149 | Cam_Valpo_30-PEAS e Imp | 268317 | 6374478 | 1 mes | 254,35 | 9,77,E-09 | 2,36,E-09 | 1,97,E-09 | 2,72,E-08 | 6,46,E-09 |

**Tabla 103.: Fuentes de Emisión - Escenario 3 parte 5**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_150 | Cam_Valpo_31-PEAS e Imp | 268347 | 6374502 | 1 mes | 154,46 | 1,61,E-08 | 3,89,E-09 | 3,24,E-09 | 4,48,E-08 | 1,06,E-08 |
| AREA | SRC_151 | Cam_Valpo_32-PEAS e Imp | 269602 | 6375295 | 1 mes | 5935,56 | 4,19,E-10 | 1,01,E-10 | 8,44,E-11 | 1,17,E-09 | 2,77,E-10 |
| AREA | SRC_152 | Cam_Valpo_33-PEAS e Imp | 270646 | 6375956 | 1 mes | 4938,33 | 5,03,E-10 | 1,22,E-10 | 1,01,E-10 | 1,40,E-09 | 3,33,E-10 |
| AREA | SRC_153 | Cam_Valpo_34-PEAS e Imp | 270700 | 6375970 | 1 mes | 220,74 | 1,13,E-08 | 2,72,E-09 | 2,27,E-09 | 3,13,E-08 | 7,44,E-09 |
| AREA | SRC_154 | Cam_Valpo_35-PEAS e Imp | 270759 | 6375972 | 1 mes | 232,03 | 1,07,E-08 | 2,59,E-09 | 2,16,E-09 | 2,98,E-08 | 7,08,E-09 |
| AREA | SRC_155 | Cam_Valpo_36-PEAS e Imp | 270817 | 6375960 | 1 mes | 237,83 | 1,05,E-08 | 2,53,E-09 | 2,11,E-09 | 2,91,E-08 | 6,91,E-09 |
| AREA | SRC_156 | Cam_Valpo_37-PEAS e Imp | 271210 | 6375788 | 1 mes | 1710,95 | 1,45,E-09 | 3,51,E-10 | 2,93,E-10 | 4,04,E-09 | 9,60,E-10 |
| AREA | SRC_157 | Cam_Valpo_38-PEAS e Imp | 271299 | 6375786 | 1 mes | 362,06 | 6,87,E-09 | 1,66,E-09 | 1,38,E-09 | 1,91,E-08 | 4,54,E-09 |
| AREA | SRC_158 | Cam_Valpo_39-PEAS e Imp | 271410 | 6375784 | 1 mes | 444,09 | 5,60,E-09 | 1,35,E-09 | 1,13,E-09 | 1,56,E-08 | 3,70,E-09 |
| AREA | SRC_159 | Cam_Valpo_40-PEAS e Imp | 271537 | 6375829 | 1 mes | 539,94 | 4,60,E-09 | 1,11,E-09 | 9,28,E-10 | 1,28,E-08 | 3,04,E-09 |
| AREA | SRC_160 | Cam_Valpo_41-PEAS e Imp | 271698 | 6375908 | 1 mes | 717,64 | 3,46,E-09 | 8,38,E-10 | 6,98,E-10 | 9,64,E-09 | 2,29,E-09 |
| AREA | SRC_161 | Cam_Valpo_42-PEAS e Imp | 271943 | 6376040 | 1 mes | 1111,41 | 2,24,E-09 | 5,41,E-10 | 4,51,E-10 | 6,22,E-09 | 1,48,E-09 |
| AREA | SRC_162 | Cam_Valpo_43-PEAS e Imp | 272216 | 6376245 | 1 mes | 1365,82 | 1,82,E-09 | 4,40,E-10 | 3,67,E-10 | 5,06,E-09 | 1,20,E-09 |
| AREA | SRC_163 | Cam_Valpo_44-PEAS e Imp | 272308 | 6376283 | 1 mes | 396,81 | 6,26,E-09 | 1,52,E-09 | 1,26,E-09 | 1,74,E-08 | 4,14,E-09 |
| AREA | SRC_164 | Cam_Valpo_45-PEAS e Imp | 272828 | 6376412 | 1 mes | 2139,51 | 1,16,E-09 | 2,81,E-10 | 2,34,E-10 | 3,23,E-09 | 7,68,E-10 |
| AREA | SRC_165 | Cam_Valpo_46-PEAS e Imp | 272961 | 6376463 | 1 mes | 572,90 | 4,34,E-09 | 1,05,E-09 | 8,75,E-10 | 1,21,E-08 | 2,87,E-09 |
| AREA | SRC_166 | Cam_Valpo_47-PEAS e Imp | 273101 | 6376548 | 1 mes | 656,43 | 3,79,E-09 | 9,16,E-10 | 7,63,E-10 | 1,05,E-08 | 2,50,E-09 |
| AREA | SRC_167 | Cam_Valpo_48-PEAS e Imp | 273683 | 6376890 | 1 mes | 2699,98 | 9,21,E-10 | 2,23,E-10 | 1,86,E-10 | 2,56,E-09 | 6,08,E-10 |
| AREA | SRC_168 | Cam_Valpo_49-PEAS e Imp | 273729 | 6376911 | 1 mes | 198,66 | 1,25,E-08 | 3,03,E-09 | 2,52,E-09 | 3,48,E-08 | 8,27,E-09 |
| AREA | SRC_169 | Cam_Valpo_50-PEAS e Imp | 273841 | 6376934 | 1 mes | 455,50 | 5,46,E-09 | 1,32,E-09 | 1,10,E-09 | 1,52,E-08 | 3,61,E-09 |
| AREA | SRC_170 | Cam_Valpo_51-PEAS e Imp | 273918 | 6376948 | 1 mes | 314,84 | 7,89,E-09 | 1,91,E-09 | 1,59,E-09 | 2,20,E-08 | 5,22,E-09 |
| AREA | SRC_171 | Cam_Valpo_52-PEAS e Imp | 273963 | 6376959 | 1 mes | 182,29 | 1,36,E-08 | 3,30,E-09 | 2,75,E-09 | 3,79,E-08 | 9,01,E-09 |
| AREA | SRC_172 | Cam_Valpo_53-PEAS e Imp | 274013 | 6376981 | 1 mes | 220,22 | 1,13,E-08 | 2,73,E-09 | 2,28,E-09 | 3,14,E-08 | 7,46,E-09 |
| AREA | SRC_173 | Cam_Valpo_54-PEAS e Imp | 274045 | 6377010 | 1 mes | 175,74 | 1,41,E-08 | 3,42,E-09 | 2,85,E-09 | 3,93,E-08 | 9,35,E-09 |
| AREA | SRC_174 | Cam_Valpo_55-PEAS e Imp | 274402 | 6377569 | 1 mes | 2654,98 | 9,36,E-10 | 2,27,E-10 | 1,89,E-10 | 2,60,E-09 | 6,19,E-10 |
| AREA | SRC_175 | Cam_Valpo_56-PEAS e Imp | 274508 | 6377712 | 1 mes | 712,20 | 3,49,E-09 | 8,44,E-10 | 7,04,E-10 | 9,71,E-09 | 2,31,E-09 |
| AREA | SRC_176 | Cam_Valpo_57-PEAS e Imp | 274515 | 6377737 | 1 mes | 105,54 | 2,36,E-08 | 5,70,E-09 | 4,75,E-09 | 6,55,E-08 | 1,56,E-08 |
| AREA | SRC_177 | Cam_Valpo_58-PEAS e Imp | 274530 | 6377783 | 1 mes | 190,85 | 1,30,E-08 | 3,15,E-09 | 2,63,E-09 | 3,62,E-08 | 8,61,E-09 |
| AREA | SRC_178 | Cam_Valpo_59-PEAS e Imp | 274571 | 6378190 | 1 mes | 1640,54 | 1,52,E-09 | 3,67,E-10 | 3,05,E-10 | 4,22,E-09 | 1,00,E-09 |
| AREA | SRC_179 | Cam_Valpo_60-PEAS e Imp | 274512 | 6378662 | 1 mes | 1902,24 | 1,31,E-09 | 3,16,E-10 | 2,63,E-10 | 3,64,E-09 | 8,64,E-10 |
| AREA | SRC_180 | Cam_Valpo_61-PEAS e Imp | 274484 | 6378742 | 1 mes | 339,36 | 7,32,E-09 | 1,77,E-09 | 1,48,E-09 | 2,04,E-08 | 4,84,E-09 |
| AREA | SRC_181 | Cam_Valpo_62-PEAS e Imp | 274397 | 6378959 | 1 mes | 934,88 | 2,66,E-09 | 6,43,E-10 | 5,36,E-10 | 7,40,E-09 | 1,76,E-09 |

**Tabla 104.: Fuentes de Emisión - Escenario 3 parte 6**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_182 | Cam_Valpo_63-PEAS e Imp | 274391 | 6379006 | 1 mes | 189,58 | 1,31,E-08 | 3,17,E-09 | 2,64,E-09 | 3,65,E-08 | 8,66,E-09 |
| AREA | SRC_183 | Cam_Valpo_64-PEAS e Imp | 274392 | 6379034 | 1 mes | 109,49 | 2,27,E-08 | 5,49,E-09 | 4,58,E-09 | 6,32,E-08 | 1,50,E-08 |
| AREA | SRC_184 | Cam_Valpo_65-PEAS e Imp | 274513 | 6379469 | 1 mes | 1805,57 | 1,38,E-09 | 3,33,E-10 | 2,78,E-10 | 3,83,E-09 | 9,10,E-10 |
| AREA | SRC_185 | Cam_Valpo_66-PEAS e Imp | 274514 | 6379510 | 1 mes | 163,36 | 1,52,E-08 | 3,68,E-09 | 3,07,E-09 | 4,23,E-08 | 1,01,E-08 |
| AREA | SRC_186 | Cam_Valpo_67-PEAS e Imp | 274503 | 6379560 | 1 mes | 208,73 | 1,19,E-08 | 2,88,E-09 | 2,40,E-09 | 3,31,E-08 | 7,87,E-09 |
| AREA | SRC_187 | Cam_Valpo_68-PEAS e Imp | 274488 | 6379623 | 1 mes | 255,44 | 9,73,E-09 | 2,35,E-09 | 1,96,E-09 | 2,71,E-08 | 6,43,E-09 |
| AREA | SRC_188 | Cam_Valpo_69-PEAS e Imp | 274426 | 6379798 | 1 mes | 745,56 | 3,33,E-09 | 8,07,E-10 | 6,72,E-10 | 9,28,E-09 | 2,20,E-09 |
| AREA | SRC_189 | Cam_Valpo_70-PEAS e Imp | 274386 | 6379897 | 1 mes | 428,53 | 5,80,E-09 | 1,40,E-09 | 1,17,E-09 | 1,61,E-08 | 3,83,E-09 |
| AREA | SRC_190 | Cam_Valpo_71-PEAS e Imp | 274352 | 6379981 | 1 mes | 360,23 | 6,90,E-09 | 1,67,E-09 | 1,39,E-09 | 1,92,E-08 | 4,56,E-09 |
| AREA | SRC_191 | Cam_Valpo_72-PEAS e Imp | 274336 | 6380041 | 1 mes | 249,49 | 9,96,E-09 | 2,41,E-09 | 2,01,E-09 | 2,77,E-08 | 6,58,E-09 |
| AREA | SRC_192 | Cam_Valpo_73-PEAS e Imp | 274333 | 6380099 | 1 mes | 227,80 | 1,09,E-08 | 2,64,E-09 | 2,20,E-09 | 3,04,E-08 | 7,21,E-09 |
| AREA | SRC_193 | Cam_Valpo_74-PEAS e Imp | 274332 | 6380163 | 1 mes | 257,27 | 9,66,E-09 | 2,34,E-09 | 1,95,E-09 | 2,69,E-08 | 6,38,E-09 |
| AREA | SRC_194 | Cam_Valpo_75-PEAS e Imp | 274329 | 6380546 | 1 mes | 1530,44 | 1,62,E-09 | 3,93,E-10 | 3,27,E-10 | 4,52,E-09 | 1,07,E-09 |
| AREA | SRC_195 | Cam_Valpo_76-PEAS e Imp | 274323 | 6380578 | 1 mes | 130,55 | 1,90,E-08 | 4,61,E-09 | 3,84,E-09 | 5,30,E-08 | 1,26,E-08 |
| AREA | SRC_196 | Cam_Valpo_77-PEAS e Imp | 274308 | 6380608 | 1 mes | 138,17 | 1,80,E-08 | 4,35,E-09 | 3,63,E-09 | 5,00,E-08 | 1,19,E-08 |
| AREA | SRC_197 | Cam_Valpo_78-PEAS e Imp | 274078 | 6381086 | 1 mes | 2120,50 | 1,17,E-09 | 2,84,E-10 | 2,36,E-10 | 3,26,E-09 | 7,75,E-10 |
| AREA | SRC_198 | Cam_Valpo_79-PEAS e Imp | 274036 | 6381146 | 1 mes | 292,96 | 8,48,E-09 | 2,05,E-09 | 1,71,E-09 | 2,36,E-08 | 5,61,E-09 |
| AREA | SRC_199 | Cam_Valpo_80-PEAS e Imp | 273997 | 6381192 | 1 mes | 242,71 | 1,02,E-08 | 2,48,E-09 | 2,06,E-09 | 2,85,E-08 | 6,77,E-09 |
| AREA | SRC_200 | Cam_Valpo_81-PEAS e Imp | 273945 | 6381212 | 1 mes | 225,25 | 1,10,E-08 | 2,67,E-09 | 2,22,E-09 | 3,07,E-08 | 7,29,E-09 |
| AREA | SRC_201 | Cam_Valpo_82-PEAS e Imp | 273863 | 6381235 | 1 mes | 340,59 | 7,30,E-09 | 1,77,E-09 | 1,47,E-09 | 2,03,E-08 | 4,82,E-09 |
| AREA | SRC_202 | Cam_Valpo_83-PEAS e Imp | 273527 | 6381309 | 1 mes | 1376,67 | 1,81,E-09 | 4,37,E-10 | 3,64,E-10 | 5,02,E-09 | 1,19,E-09 |
| AREA | SRC_203 | Cam_Valpo_84-PEAS e Imp | 273488 | 6381317 | 1 mes | 158,83 | 1,56,E-08 | 3,79,E-09 | 3,15,E-09 | 4,35,E-08 | 1,03,E-08 |
| AREA | SRC_204 | Cam_Valpo_85-PEAS e Imp | 273437 | 6381311 | 1 mes | 210,61 | 1,18,E-08 | 2,86,E-09 | 2,38,E-09 | 3,28,E-08 | 7,80,E-09 |
| AREA | SRC_205 | Cam_Valpo_86-PEAS e Imp | 273400 | 6381306 | 1 mes | 148,75 | 1,67,E-08 | 4,04,E-09 | 3,37,E-09 | 4,65,E-08 | 1,10,E-08 |
| AREA | SRC_206 | Cam_Valpo_87-PEAS e Imp | 273330 | 6381278 | 1 mes | 302,02 | 8,23,E-09 | 1,99,E-09 | 1,66,E-09 | 2,29,E-08 | 5,44,E-09 |
| AREA | SRC_207 | Cam_Valpo_88-PEAS e Imp | 273269 | 6381275 | 1 mes | 240,32 | 1,03,E-08 | 2,50,E-09 | 2,09,E-09 | 2,88,E-08 | 6,84,E-09 |
| AREA | SRC_208 | Cam_Valpo_89-PEAS e Imp | 273210 | 6381284 | 1 mes | 238,69 | 1,04,E-08 | 2,52,E-09 | 2,10,E-09 | 2,90,E-08 | 6,88,E-09 |
| AREA | SRC_209 | Cam_Valpo_90-PEAS e Imp | 273140 | 6381307 | 1 mes | 291,89 | 8,52,E-09 | 2,06,E-09 | 1,72,E-09 | 2,37,E-08 | 5,63,E-09 |
| AREA | SRC_210 | Cam_Valpo_91-PEAS e Imp | 273026 | 6381364 | 1 mes | 510,61 | 4,87,E-09 | 1,18,E-09 | 9,81,E-10 | 1,35,E-08 | 3,22,E-09 |
| AREA | SRC_211 | Cam_Valpo_92-PEAS e Imp | 272787 | 6381471 | 1 mes | 1046,47 | 2,38,E-09 | 5,75,E-10 | 4,79,E-10 | 6,61,E-09 | 1,57,E-09 |
| AREA | SRC_212 | Cam_Valpo_93-PEAS e Imp | 272625 | 6381553 | 1 mes | 726,81 | 3,42,E-09 | 8,27,E-10 | 6,89,E-10 | 9,51,E-09 | 2,26,E-09 |
| AREA | SRC_213 | Cam_Valpo_94-PEAS e Imp | 272586 | 6381587 | 1 mes | 205,87 | 1,21,E-08 | 2,92,E-09 | 2,43,E-09 | 3,36,E-08 | 7,98,E-09 |

**Tabla 105.: Fuentes de Emisión - Escenario 3 parte 7**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_214 | Cam_Valpo_95-PEAS e Imp | 272567 | 6381621 | 1 mes | 150,25 | 1,65,E-08 | 4,00,E-09 | 3,34,E-09 | 4,60,E-08 | 1,09,E-08 |
| AREA | SRC_215 | Cam_Valpo_96-PEAS e Imp | 272558 | 6381659 | 1 mes | 154,59 | 1,61,E-08 | 3,89,E-09 | 3,24,E-09 | 4,47,E-08 | 1,06,E-08 |
| AREA | SRC_216 | Cam_Valpo_97-PEAS e Imp | 272513 | 6381931 | 1 mes | 1103,20 | 2,25,E-09 | 5,45,E-10 | 4,54,E-10 | 6,27,E-09 | 1,49,E-09 |
| AREA | SRC_217 | Cam_Valpo_98-PEAS e Imp | 272500 | 6382030 | 1 mes | 398,37 | 6,24,E-09 | 1,51,E-09 | 1,26,E-09 | 1,74,E-08 | 4,12,E-09 |
| AREA | SRC_218 | Cam_Valpo_99-PEAS e Imp | 272492 | 6382086 | 1 mes | 223,87 | 1,11,E-08 | 2,69,E-09 | 2,24,E-09 | 3,09,E-08 | 7,34,E-09 |
| AREA | SRC_219 | Cam_Valpo_100-PEAS e Imp | 272491 | 6382127 | 1 mes | 164,32 | 1,51,E-08 | 3,66,E-09 | 3,05,E-09 | 4,21,E-08 | 1,00,E-08 |
| AREA | SRC_220 | Cam_Valpo_101-PEAS e Imp | 272506 | 6382188 | 1 mes | 247,33 | 1,00,E-08 | 2,43,E-09 | 2,03,E-09 | 2,80,E-08 | 6,64,E-09 |
| AREA | SRC_221 | Cam_Valpo_102-PEAS e Imp | 272660 | 6383439 | 1 mes | 5043,31 | 4,93,E-10 | 1,19,E-10 | 9,94,E-11 | 1,37,E-09 | 3,26,E-10 |
| AREA | SRC_222 | Cam_Valpo_103-PEAS e Imp | 272630 | 6384559 | 1 mes | 4478,91 | 5,55,E-10 | 1,34,E-10 | 1,12,E-10 | 1,54,E-09 | 3,67,E-10 |
| AREA | SRC_223 | Cam_Valpo_104-PEAS e Imp | 272626 | 6385227 | 1 mes | 2671,08 | 9,31,E-10 | 2,25,E-10 | 1,88,E-10 | 2,59,E-09 | 6,15,E-10 |
| AREA | SRC_224 | Cam_Valpo_105-PEAS e Imp | 272602 | 6386454 | 1 mes | 4905,80 | 5,07,E-10 | 1,23,E-10 | 1,02,E-10 | 1,41,E-09 | 3,35,E-10 |
| AREA | SRC_225 | Cam_Valpo_106-PEAS e Imp | 272609 | 6386527 | 1 mes | 292,53 | 8,50,E-09 | 2,06,E-09 | 1,71,E-09 | 2,36,E-08 | 5,62,E-09 |
| AREA | SRC_226 | Cam_Valpo_107-PEAS e Imp | 272650 | 6386615 | 1 mes | 384,69 | 6,46,E-09 | 1,56,E-09 | 1,30,E-09 | 1,80,E-08 | 4,27,E-09 |
| AREA | SRC_227 | Cam_Valpo_108-PEAS e Imp | 272755 | 6386705 | 1 mes | 550,00 | 4,52,E-09 | 1,09,E-09 | 9,11,E-10 | 1,26,E-08 | 2,99,E-09 |
| AREA | SRC_228 | Cam_Valpo_109-PEAS e Imp | 272846 | 6386776 | 1 mes | 460,85 | 5,39,E-09 | 1,30,E-09 | 1,09,E-09 | 1,50,E-08 | 3,56,E-09 |
| AREA | SRC_229 | Cam_Valpo_110-PEAS e Imp | 272918 | 6386821 | 1 mes | 338,79 | 7,34,E-09 | 1,77,E-09 | 1,48,E-09 | 2,04,E-08 | 4,85,E-09 |
| AREA | SRC_230 | Cam_Valpo_111-PEAS e Imp | 272959 | 6386856 | 1 mes | 215,71 | 1,15,E-08 | 2,79,E-09 | 2,32,E-09 | 3,21,E-08 | 7,62,E-09 |
| AREA | SRC_231 | Cam_Valpo_112-PEAS e Imp | 272979 | 6386909 | 1 mes | 229,32 | 1,08,E-08 | 2,62,E-09 | 2,19,E-09 | 3,02,E-08 | 7,16,E-09 |
| AREA | SRC_232 | Cam_Valpo_113-PEAS e Imp | 272982 | 6386950 | 1 mes | 168,20 | 1,48,E-08 | 3,58,E-09 | 2,98,E-09 | 4,11,E-08 | 9,77,E-09 |
| AREA | SRC_233 | Cam_Valpo_114-PEAS e Imp | 272974 | 6387033 | 1 mes | 334,56 | 7,43,E-09 | 1,80,E-09 | 1,50,E-09 | 2,07,E-08 | 4,91,E-09 |
| AREA | SRC_234 | Cam_Valpo_115-PEAS e Imp | 272969 | 6387289 | 1 mes | 1021,26 | 2,43,E-09 | 5,89,E-10 | 4,91,E-10 | 6,77,E-09 | 1,61,E-09 |
| AREA | SRC_235 | Cam_Valpo_116-PEAS e Imp | 272950 | 6387316 | 1 mes | 135,86 | 1,83,E-08 | 4,43,E-09 | 3,69,E-09 | 5,09,E-08 | 1,21,E-08 |
| AREA | SRC_236 | Cam_Valpo_117-PEAS e Imp | 272918 | 6387332 | 1 mes | 150,62 | 1,65,E-08 | 3,99,E-09 | 3,33,E-09 | 4,59,E-08 | 1,09,E-08 |
| AREA | SRC_237 | Cam_Valpo_118-PEAS e Imp | 272871 | 6387328 | 1 mes | 193,11 | 1,29,E-08 | 3,11,E-09 | 2,59,E-09 | 3,58,E-08 | 8,51,E-09 |
| AREA | SRC_238 | Cam_Valpo_119-PEAS e Imp | 272818 | 6387319 | 1 mes | 214,82 | 1,16,E-08 | 2,80,E-09 | 2,33,E-09 | 3,22,E-08 | 7,65,E-09 |
| AREA | SRC_239 | Cam_Valpo_120-PEAS e Imp | 272669 | 6387324 | 1 mes | 593,51 | 4,19,E-09 | 1,01,E-09 | 8,44,E-10 | 1,17,E-08 | 2,77,E-09 |
| AREA | SRC_240 | Cam_Valpo_121-PEAS e Imp | 272536 | 6387380 | 1 mes | 574,11 | 4,33,E-09 | 1,05,E-09 | 8,73,E-10 | 1,20,E-08 | 2,86,E-09 |
| AREA | SRC_241 | Cam_Valpo_122-PEAS e Imp | 272406 | 6387475 | 1 mes | 642,85 | 3,87,E-09 | 9,35,E-10 | 7,79,E-10 | 1,08,E-08 | 2,56,E-09 |
| AREA | SRC_242 | Cam_Valpo_123-PEAS e Imp | 272321 | 6387544 | 1 mes | 438,86 | 5,66,E-09 | 1,37,E-09 | 1,14,E-09 | 1,58,E-08 | 3,74,E-09 |
| AREA | SRC_243 | Cam_Valpo_124-PEAS e Imp | 272252 | 6387605 | 1 mes | 366,01 | 6,79,E-09 | 1,64,E-09 | 1,37,E-09 | 1,89,E-08 | 4,49,E-09 |
| AREA | SRC_244 | Cam_Valpo_125-PEAS e Imp | 272138 | 6387749 | 1 mes | 733,97 | 3,39,E-09 | 8,19,E-10 | 6,83,E-10 | 9,42,E-09 | 2,24,E-09 |
| AREA | SRC_245 | Cam_Valpo_126-PEAS e Imp | 272059 | 6387890 | 1 mes | 645,70 | 3,85,E-09 | 9,31,E-10 | 7,76,E-10 | 1,07,E-08 | 2,54,E-09 |

**Tabla 106.: Fuentes de Emisión - Escenario 3 parte 8**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_246 | Cam_Valpo_127-PEAS e Imp | 272019 | 6388008 | 1 mes | 494,29 | 5,03,E-09 | 1,22,E-09 | 1,01,E-09 | 1,40,E-08 | 3,32,E-09 |
| AREA | SRC_247 | Cam_Valpo_128-PEAS e Imp | 272005 | 6388086 | 1 mes | 318,17 | 7,81,E-09 | 1,89,E-09 | 1,57,E-09 | 2,17,E-08 | 5,16,E-09 |
| AREA | SRC_248 | Cam_Valpo_129-PEAS e Imp | 272005 | 6388171 | 1 mes | 338,40 | 7,35,E-09 | 1,78,E-09 | 1,48,E-09 | 2,04,E-08 | 4,85,E-09 |
| AREA | SRC_249 | Cam_Valpo_130-PEAS e Imp | 272018 | 6388207 | 1 mes | 149,40 | 1,66,E-08 | 4,03,E-09 | 3,35,E-09 | 4,63,E-08 | 1,10,E-08 |
| AREA | SRC_250 | Cam_Valpo_131-PEAS e Imp | 272053 | 6388222 | 1 mes | 144,57 | 1,72,E-08 | 4,16,E-09 | 3,47,E-09 | 4,78,E-08 | 1,14,E-08 |
| AREA | SRC_251 | Cam_Valpo_132-PEAS e Imp | 272113 | 6388260 | 1 mes | 286,19 | 8,68,E-09 | 2,10,E-09 | 1,75,E-09 | 2,42,E-08 | 5,74,E-09 |
| AREA | SRC_252 | Cam_Valpo_133-PEAS e Imp | 272165 | 6388289 | 1 mes | 236,50 | 1,05,E-08 | 2,54,E-09 | 2,12,E-09 | 2,92,E-08 | 6,95,E-09 |
| AREA | SRC_253 | Cam_Valpo_134-PEAS e Imp | 272170 | 6388313 | 1 mes | 103,04 | 2,41,E-08 | 5,84,E-09 | 4,86,E-09 | 6,71,E-08 | 1,59,E-08 |
| AREA | SRC_254 | Cam_Valpo_135-PEAS e Imp | 272160 | 6388355 | 1 mes | 178,67 | 1,39,E-08 | 3,37,E-09 | 2,80,E-09 | 3,87,E-08 | 9,19,E-09 |
| AREA | SRC_255 | Cam_Valpo_136-PEAS e Imp | 272116 | 6388384 | 1 mes | 213,17 | 1,17,E-08 | 2,82,E-09 | 2,35,E-09 | 3,24,E-08 | 7,71,E-09 |
| AREA | SRC_256 | Cam_Valpo_137-PEAS e Imp | 271990 | 6388473 | 1 mes | 618,26 | 4,02,E-09 | 9,73,E-10 | 8,11,E-10 | 1,12,E-08 | 2,66,E-09 |
| AREA | SRC_257 | Cam_Valpo_138-PEAS e Imp | 271909 | 6388570 | 1 mes | 502,24 | 4,95,E-09 | 1,20,E-09 | 9,98,E-10 | 1,38,E-08 | 3,27,E-09 |
| AREA | SRC_258 | Cam_Valpo_139-PEAS e Imp | 271887 | 6388631 | 1 mes | 257,67 | 9,65,E-09 | 2,33,E-09 | 1,94,E-09 | 2,68,E-08 | 6,38,E-09 |
| AREA | SRC_259 | Cam_Valpo_140-PEAS e Imp | 271869 | 6388710 | 1 mes | 324,57 | 7,66,E-09 | 1,85,E-09 | 1,54,E-09 | 2,13,E-08 | 5,06,E-09 |
| AREA | SRC_260 | Cam_Valpo_141-PEAS e Imp | 271879 | 6388778 | 1 mes | 270,72 | 9,18,E-09 | 2,22,E-09 | 1,85,E-09 | 2,55,E-08 | 6,07,E-09 |
| AREA | SRC_261 | Cam_Valpo_142-PEAS e Imp | 271889 | 6388831 | 1 mes | 215,81 | 1,15,E-08 | 2,79,E-09 | 2,32,E-09 | 3,20,E-08 | 7,61,E-09 |
| AREA | SRC_262 | Cam_Valpo_143-PEAS e Imp | 271888 | 6388910 | 1 mes | 317,54 | 7,83,E-09 | 1,89,E-09 | 1,58,E-09 | 2,18,E-08 | 5,17,E-09 |
| AREA | SRC_263 | Cam_Valpo_144-PEAS e Imp | 271765 | 6389249 | 1 mes | 1443,83 | 1,72,E-09 | 4,16,E-10 | 3,47,E-10 | 4,79,E-09 | 1,14,E-09 |
| AREA | SRC_264 | Cam_Valpo_145-PEAS e Imp | 271745 | 6389323 | 1 mes | 308,68 | 8,05,E-09 | 1,95,E-09 | 1,62,E-09 | 2,24,E-08 | 5,32,E-09 |
| AREA | SRC_265 | Cam_Valpo_146-PEAS e Imp | 271746 | 6389404 | 1 mes | 321,13 | 7,74,E-09 | 1,87,E-09 | 1,56,E-09 | 2,15,E-08 | 5,12,E-09 |
| AREA | SRC_266 | Cam_Valpo_147-PEAS e Imp | 271745 | 6389713 | 1 mes | 1235,33 | 2,01,E-09 | 4,87,E-10 | 4,06,E-10 | 5,60,E-09 | 1,33,E-09 |
| AREA | SRC_267 | Cam_Valpo_148-PEAS e Imp | 271729 | 6389779 | 1 mes | 274,74 | 9,05,E-09 | 2,19,E-09 | 1,82,E-09 | 2,52,E-08 | 5,98,E-09 |
| AREA | SRC_268 | Cam_Valpo_149-PEAS e Imp | 271405 | 6390771 | 1 mes | 4169,69 | 5,96,E-10 | 1,44,E-10 | 1,20,E-10 | 1,66,E-09 | 3,94,E-10 |
| AREA | SRC_269 | Cam_Valpo_150-PEAS e Imp | 271408 | 6390852 | 1 mes | 324,07 | 7,67,E-09 | 1,86,E-09 | 1,55,E-09 | 2,13,E-08 | 5,07,E-09 |
| AREA | SRC_270 | Cam_Valpo_151-PEAS e Imp | 271425 | 6390918 | 1 mes | 269,76 | 9,21,E-09 | 2,23,E-09 | 1,86,E-09 | 2,56,E-08 | 6,09,E-09 |
| AREA | SRC_271 | Cam_Valpo_152-PEAS e Imp | 271595 | 6391444 | 1 mes | 2210,20 | 1,12,E-09 | 2,72,E-10 | 2,27,E-10 | 3,13,E-09 | 7,43,E-10 |
| AREA | SRC_272 | Cam_Valpo_153-PEAS e Imp | 271601 | 6391518 | 1 mes | 297,07 | 8,37,E-09 | 2,02,E-09 | 1,69,E-09 | 2,33,E-08 | 5,53,E-09 |
| AREA | SRC_273 | Cam_Valpo_154-PEAS e Imp | 271583 | 6391599 | 1 mes | 334,56 | 7,43,E-09 | 1,80,E-09 | 1,50,E-09 | 2,07,E-08 | 4,91,E-09 |
| AREA | SRC_274 | Cam_Valpo_155-PEAS e Imp | 271490 | 6391665 | 1 mes | 462,29 | 5,38,E-09 | 1,30,E-09 | 1,08,E-09 | 1,50,E-08 | 3,55,E-09 |
| AREA | SRC_275 | Cam_Valpo_156-PEAS e Imp | 271388 | 6391779 | 1 mes | 610,49 | 4,07,E-09 | 9,85,E-10 | 8,21,E-10 | 1,13,E-08 | 2,69,E-09 |
| AREA | SRC_276 | Cam_Valpo_157-PEAS e Imp | 271303 | 6391969 | 1 mes | 829,95 | 2,99,E-09 | 7,25,E-10 | 6,04,E-10 | 8,33,E-09 | 1,98,E-09 |
| AREA | SRC_277 | Cam_Valpo_158-PEAS e Imp | 271249 | 6392048 | 1 mes | 385,48 | 6,45,E-09 | 1,56,E-09 | 1,30,E-09 | 1,79,E-08 | 4,26,E-09 |

**Tabla 107.: Fuentes de Emisión - Escenario 3 parte 9**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_278 | Cam_Valpo_159-PEAS e Imp | 271095 | 6392199 | 1 mes | 863,11 | 2,88,E-09 | 6,97,E-10 | 5,81,E-10 | 8,01,E-09 | 1,90,E-09 |
| AREA | SRC_279 | Cam_Valpo_160-PEAS e Imp | 271003 | 6392357 | 1 mes | 727,41 | 3,42,E-09 | 8,27,E-10 | 6,89,E-10 | 9,51,E-09 | 2,26,E-09 |
| AREA | SRC_280 | Cam_Valpo_161-PEAS e Imp | 270864 | 6392618 | 1 mes | 1181,67 | 2,10,E-09 | 5,09,E-10 | 4,24,E-10 | 5,85,E-09 | 1,39,E-09 |
| AREA | SRC_281 | Cam_Valpo_162-PEAS e Imp | 270665 | 6392901 | 1 mes | 1386,67 | 1,79,E-09 | 4,34,E-10 | 3,61,E-10 | 4,99,E-09 | 1,18,E-09 |
| AREA | SRC_282 | Cam_Valpo_163-PEAS e Imp | 270570 | 6393060 | 1 mes | 739,81 | 3,36,E-09 | 8,13,E-10 | 6,77,E-10 | 9,35,E-09 | 2,22,E-09 |
| AREA | SRC_283 | Cam_Valpo_164-PEAS e Imp | 270535 | 6393162 | 1 mes | 427,94 | 5,81,E-09 | 1,41,E-09 | 1,17,E-09 | 1,62,E-08 | 3,84,E-09 |
| AREA | SRC_284 | Cam_Valpo_165-PEAS e Imp | 270408 | 6393157 | 1 mes | 516,16 | 4,82,E-09 | 1,17,E-09 | 9,71,E-10 | 1,34,E-08 | 3,18,E-09 |
| AREA | SRC_285 | Cam_Valpo_166-PEAS e Imp | 270322 | 6393156 | 1 mes | 344,11 | 7,22,E-09 | 1,75,E-09 | 1,46,E-09 | 2,01,E-08 | 4,77,E-09 |
| AREA | SRC_286 | Cam_Valpo_167-PEAS e Imp | 270198 | 6393225 | 1 mes | 562,03 | 4,42,E-09 | 1,07,E-09 | 8,92,E-10 | 1,23,E-08 | 2,92,E-09 |
| AREA | SRC_287 | Cam_Valpo_168-PEAS e Imp | 270084 | 6393222 | 1 mes | 461,57 | 5,38,E-09 | 1,30,E-09 | 1,09,E-09 | 1,50,E-08 | 3,56,E-09 |
| AREA | SRC_288 | Cam_Valpo_169-PEAS e Imp | 270014 | 6393114 | 1 mes | 520,05 | 4,78,E-09 | 1,16,E-09 | 9,64,E-10 | 1,33,E-08 | 3,16,E-09 |
| AREA | SRC_289 | Cam_Valpo_170-PEAS e Imp | 269944 | 6393026 | 1 mes | 448,19 | 5,55,E-09 | 1,34,E-09 | 1,12,E-09 | 1,54,E-08 | 3,67,E-09 |
| AREA | SRC_290 | Cam_Valpo_171-PEAS e Imp | 269831 | 6392981 | 1 mes | 484,35 | 5,13,E-09 | 1,24,E-09 | 1,03,E-09 | 1,43,E-08 | 3,39,E-09 |
| AREA | SRC_291 | Cam_Valpo_172-PEAS e Imp | 269702 | 6392966 | 1 mes | 516,99 | 4,81,E-09 | 1,16,E-09 | 9,69,E-10 | 1,34,E-08 | 3,18,E-09 |
| AREA | SRC_292 | Cam_Valpo_173-PEAS e Imp | 269506 | 6393084 | 1 mes | 906,73 | 2,74,E-09 | 6,63,E-10 | 5,53,E-10 | 7,63,E-09 | 1,81,E-09 |
| AREA | SRC_293 | Cam_Valpo_174-PEAS e Imp | 269407 | 6393106 | 1 mes | 410,62 | 6,05,E-09 | 1,46,E-09 | 1,22,E-09 | 1,68,E-08 | 4,00,E-09 |
| AREA | SRC_294 | Cam_Valpo_175-PEAS e Imp | 269355 | 6393219 | 1 mes | 493,13 | 5,04,E-09 | 1,22,E-09 | 1,02,E-09 | 1,40,E-08 | 3,33,E-09 |
| AREA | SRC_295 | Cam_Valpo_176-PEAS e Imp | 269450 | 6393436 | 1 mes | 939,57 | 2,65,E-09 | 6,40,E-10 | 5,33,E-10 | 7,36,E-09 | 1,75,E-09 |
| AREA | SRC_296 | Cam_Valpo_177-PEAS e Imp | 269537 | 6393768 | 1 mes | 1375,49 | 1,81,E-09 | 4,37,E-10 | 3,64,E-10 | 5,03,E-09 | 1,19,E-09 |
| AREA | SRC_297 | Cam_Valpo_178-PEAS e Imp | 269541 | 6393876 | 1 mes | 433,16 | 5,74,E-09 | 1,39,E-09 | 1,16,E-09 | 1,60,E-08 | 3,79,E-09 |
| AREA | SRC_298 | Cam_Valpo_179-PEAS e Imp | 269514 | 6393952 | 1 mes | 327,49 | 7,59,E-09 | 1,84,E-09 | 1,53,E-09 | 2,11,E-08 | 5,02,E-09 |
| AREA | SRC_299 | Cam_Valpo_180-PEAS e Imp | 269461 | 6394006 | 1 mes | 302,03 | 8,23,E-09 | 1,99,E-09 | 1,66,E-09 | 2,29,E-08 | 5,44,E-09 |
| AREA | SRC_300 | Cam_Valpo_181-PEAS e Imp | 269456 | 6394087 | 1 mes | 317,54 | 7,83,E-09 | 1,89,E-09 | 1,58,E-09 | 2,18,E-08 | 5,17,E-09 |
| AREA | SRC_301 | Cam_Valpo_182-PEAS e Imp | 269494 | 6394169 | 1 mes | 358,94 | 6,92,E-09 | 1,68,E-09 | 1,40,E-09 | 1,93,E-08 | 4,58,E-09 |
| AREA | SRC_302 | Cam_Valpo_183-PEAS e Imp | 269580 | 6394296 | 1 mes | 611,99 | 4,06,E-09 | 9,83,E-10 | 8,19,E-10 | 1,13,E-08 | 2,68,E-09 |
| AREA | SRC_303 | Cam_Valpo_184-PEAS e Imp | 269614 | 6394394 | 1 mes | 416,61 | 5,97,E-09 | 1,44,E-09 | 1,20,E-09 | 1,66,E-08 | 3,94,E-09 |
| AREA | SRC_304 | Cam_Valpo_185-PEAS e Imp | 269617 | 6394492 | 1 mes | 396,57 | 6,27,E-09 | 1,52,E-09 | 1,26,E-09 | 1,74,E-08 | 4,14,E-09 |
| AREA | SRC_305 | Cam_Valpo_186-PEAS e Imp | 269532 | 6394634 | 1 mes | 664,18 | 3,74,E-09 | 9,05,E-10 | 7,54,E-10 | 1,04,E-08 | 2,47,E-09 |
| AREA | SRC_306 | Cam_Valpo_187-PEAS e Imp | 269478 | 6394752 | 1 mes | 518,20 | 4,80,E-09 | 1,16,E-09 | 9,67,E-10 | 1,33,E-08 | 3,17,E-09 |
| AREA | SRC_307 | Cam_Valpo_188-PEAS e Imp | 269437 | 6394881 | 1 mes | 540,93 | 4,59,E-09 | 1,11,E-09 | 9,26,E-10 | 1,28,E-08 | 3,04,E-09 |
| AREA | SRC_308 | Cam_Valpo_189-PEAS e Imp | 269448 | 6395002 | 1 mes | 483,46 | 5,14,E-09 | 1,24,E-09 | 1,04,E-09 | 1,43,E-08 | 3,40,E-09 |
| AREA | SRC_309 | Cam_Valpo_190-PEAS e Imp | 269465 | 6395049 | 1 mes | 197,82 | 1,26,E-08 | 3,04,E-09 | 2,53,E-09 | 3,50,E-08 | 8,30,E-09 |

**Tabla 108.: Fuentes de Emisión - Escenario 3 parte 10**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_310 | Cam_Valpo_191-PEAS e Imp | 269701 | 6395188 | 1 mes | 1088,66 | 2,28,E-09 | 5,52,E-10 | 4,60,E-10 | 6,35,E-09 | 1,51,E-09 |
| AREA | SRC_311 | Cam_Valpo_192-PEAS e Imp | 269737 | 6395244 | 1 mes | 269,38 | 9,23,E-09 | 2,23,E-09 | 1,86,E-09 | 2,57,E-08 | 6,10,E-09 |
| AREA | SRC_312 | Cam_Valpo_193-PEAS e Imp | 269748 | 6395318 | 1 mes | 301,88 | 8,23,E-09 | 1,99,E-09 | 1,66,E-09 | 2,29,E-08 | 5,44,E-09 |
| AREA | SRC_313 | Cam_Valpo_194-PEAS e Imp | 269734 | 6395473 | 1 mes | 624,02 | 3,98,E-09 | 9,64,E-10 | 8,03,E-10 | 1,11,E-08 | 2,63,E-09 |
| AREA | SRC_314 | Cam_Valpo_195-PEAS e Imp | 269791 | 6395575 | 1 mes | 462,91 | 5,37,E-09 | 1,30,E-09 | 1,08,E-09 | 1,49,E-08 | 3,55,E-09 |
| AREA | SRC_315 | Cam_Valpo_196-PEAS e Imp | 269918 | 6395634 | 1 mes | 557,57 | 4,46,E-09 | 1,08,E-09 | 8,99,E-10 | 1,24,E-08 | 2,95,E-09 |
| AREA | SRC_316 | Cam_Valpo_197-PEAS e Imp | 269951 | 6395703 | 1 mes | 311,66 | 7,98,E-09 | 1,93,E-09 | 1,61,E-09 | 2,22,E-08 | 5,27,E-09 |
| AREA | SRC_317 | Cam_Valpo_198-PEAS e Imp | 269926 | 6395767 | 1 mes | 277,87 | 8,94,E-09 | 2,16,E-09 | 1,80,E-09 | 2,49,E-08 | 5,91,E-09 |
| AREA | SRC_318 | Cam_Valpo_199-PEAS e Imp | 269853 | 6395812 | 1 mes | 348,28 | 7,14,E-09 | 1,73,E-09 | 1,44,E-09 | 1,99,E-08 | 4,72,E-09 |
| AREA | SRC_319 | Cam_Valpo_200-PEAS e Imp | 269732 | 6395847 | 1 mes | 504,67 | 4,93,E-09 | 1,19,E-09 | 9,93,E-10 | 1,37,E-08 | 3,25,E-09 |
| AREA | SRC_320 | Cam_Valpo_201-PEAS e Imp | 269688 | 6395928 | 1 mes | 365,46 | 6,80,E-09 | 1,65,E-09 | 1,37,E-09 | 1,89,E-08 | 4,49,E-09 |
| AREA | SRC_321 | Cam_Valpo_202-PEAS e Imp | 269717 | 6396047 | 1 mes | 484,68 | 5,13,E-09 | 1,24,E-09 | 1,03,E-09 | 1,43,E-08 | 3,39,E-09 |
| AREA | SRC_322 | Cam_Valpo_203-PEAS e Imp | 269712 | 6396106 | 1 mes | 237,49 | 1,05,E-08 | 2,53,E-09 | 2,11,E-09 | 2,91,E-08 | 6,92,E-09 |
| AREA | SRC_323 | Cam_Valpo_204-PEAS e Imp | 269657 | 6396143 | 1 mes | 271,48 | 9,16,E-09 | 2,22,E-09 | 1,85,E-09 | 2,55,E-08 | 6,05,E-09 |
| AREA | SRC_324 | Cam_Valpo_205-PEAS e Imp | 269580 | 6396120 | 1 mes | 326,46 | 7,61,E-09 | 1,84,E-09 | 1,53,E-09 | 2,12,E-08 | 5,03,E-09 |
| AREA | SRC_325 | Cam_Valpo_206-PEAS e Imp | 269501 | 6396070 | 1 mes | 376,20 | 6,61,E-09 | 1,60,E-09 | 1,33,E-09 | 1,84,E-08 | 4,37,E-09 |
| AREA | SRC_326 | Cam_Valpo_207-PEAS e Imp | 269359 | 6396026 | 1 mes | 593,54 | 4,19,E-09 | 1,01,E-09 | 8,44,E-10 | 1,17,E-08 | 2,77,E-09 |
| AREA | SRC_327 | Cam_Valpo_208-PEAS e Imp | 269272 | 6396023 | 1 mes | 343,48 | 7,24,E-09 | 1,75,E-09 | 1,46,E-09 | 2,01,E-08 | 4,78,E-09 |
| AREA | SRC_328 | Cam_Valpo_209-PEAS e Imp | 269222 | 6396073 | 1 mes | 275,81 | 9,01,E-09 | 2,18,E-09 | 1,82,E-09 | 2,51,E-08 | 5,96,E-09 |
| AREA | SRC_329 | Cam_Valpo_210-PEAS e Imp | 269210 | 6396185 | 1 mes | 446,25 | 5,57,E-09 | 1,35,E-09 | 1,12,E-09 | 1,55,E-08 | 3,68,E-09 |
| AREA | SRC_330 | Cam_Valpo_211-PEAS e Imp | 269167 | 6396232 | 1 mes | 255,46 | 9,73,E-09 | 2,35,E-09 | 1,96,E-09 | 2,71,E-08 | 6,43,E-09 |
| AREA | SRC_331 | Cam_Valpo_212-PEAS e Imp | 269082 | 6396226 | 1 mes | 349,58 | 7,11,E-09 | 1,72,E-09 | 1,43,E-09 | 1,98,E-08 | 4,70,E-09 |
| AREA | SRC_332 | Cam_Valpo_213-PEAS e Imp | 268998 | 6396240 | 1 mes | 335,54 | 7,41,E-09 | 1,79,E-09 | 1,49,E-09 | 2,06,E-08 | 4,90,E-09 |
| AREA | SRC_333 | Cam_Valpo_214-PEAS e Imp | 268894 | 6396300 | 1 mes | 480,09 | 5,18,E-09 | 1,25,E-09 | 1,04,E-09 | 1,44,E-08 | 3,42,E-09 |
| AREA | SRC_334 | Cam_Valpo_215-PEAS e Imp | 268805 | 6396381 | 1 mes | 477,49 | 5,21,E-09 | 1,26,E-09 | 1,05,E-09 | 1,45,E-08 | 3,44,E-09 |
| AREA | SRC_335 | Cam_Valpo_216-PEAS e Imp | 268734 | 6396481 | 1 mes | 489,34 | 5,08,E-09 | 1,23,E-09 | 1,02,E-09 | 1,41,E-08 | 3,36,E-09 |
| AREA | SRC_336 | Cam_Valpo_217-PEAS e Imp | 268692 | 6396569 | 1 mes | 388,32 | 6,40,E-09 | 1,55,E-09 | 1,29,E-09 | 1,78,E-08 | 4,23,E-09 |
| AREA | SRC_337 | Cam_Valpo_218-PEAS e Imp | 268614 | 6396686 | 1 mes | 563,68 | 4,41,E-09 | 1,07,E-09 | 8,89,E-10 | 1,23,E-08 | 2,91,E-09 |
| AREA | SRC_338 | Cam_Valpo_219-PEAS e Imp | 268551 | 6396751 | 1 mes | 365,13 | 6,81,E-09 | 1,65,E-09 | 1,37,E-09 | 1,89,E-08 | 4,50,E-09 |
| AREA | SRC_339 | Cam_Valpo_220-PEAS e Imp | 268525 | 6396834 | 1 mes | 342,75 | 7,25,E-09 | 1,75,E-09 | 1,46,E-09 | 2,02,E-08 | 4,79,E-09 |
| AREA | SRC_340 | Cam_Valpo_221-PEAS e Imp | 268521 | 6396918 | 1 mes | 335,20 | 7,42,E-09 | 1,79,E-09 | 1,49,E-09 | 2,06,E-08 | 4,90,E-09 |
| AREA | SRC_341 | Cam_Valpo_222-PEAS e Imp | 268510 | 6396996 | 1 mes | 312,17 | 7,96,E-09 | 1,93,E-09 | 1,61,E-09 | 2,22,E-08 | 5,26,E-09 |

**Tabla 109.: Fuentes de Emisión - Escenario 3 parte 11**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_342 | Cam_Valpo_223-PEAS e Imp | 268441 | 6397095 | 1 mes | 486,78 | 5,11,E-09 | 1,24,E-09 | 1,03,E-09 | 1,42,E-08 | 3,37,E-09 |
| AREA | SRC_343 | Cam_Valpo_224-PEAS e Imp | 268352 | 6397195 | 1 mes | 537,81 | 4,62,E-09 | 1,12,E-09 | 9,32,E-10 | 1,29,E-08 | 3,05,E-09 |
| AREA | SRC_344 | Cam_Valpo_225-PEAS e Imp | 268295 | 6397296 | 1 mes | 460,41 | 5,40,E-09 | 1,31,E-09 | 1,09,E-09 | 1,50,E-08 | 3,57,E-09 |
| AREA | SRC_345 | Cam_Valpo_226-PEAS e Imp | 268265 | 6397370 | 1 mes | 319,00 | 7,79,E-09 | 1,89,E-09 | 1,57,E-09 | 2,17,E-08 | 5,15,E-09 |
| AREA | SRC_346 | Cam_Valpo_227-PEAS e Imp | 268236 | 6397470 | 1 mes | 414,51 | 6,00,E-09 | 1,45,E-09 | 1,21,E-09 | 1,67,E-08 | 3,96,E-09 |
| AREA | SRC_347 | Cam_Valpo_228-PEAS e Imp | 268225 | 6397539 | 1 mes | 278,02 | 8,94,E-09 | 2,16,E-09 | 1,80,E-09 | 2,49,E-08 | 5,91,E-09 |
| AREA | SRC_348 | Cam_Valpo_229-PEAS e Imp | 268212 | 6397650 | 1 mes | 446,47 | 5,57,E-09 | 1,35,E-09 | 1,12,E-09 | 1,55,E-08 | 3,68,E-09 |
| AREA | SRC_349 | Cam_Valpo_230-PEAS e Imp | 268292 | 6397691 | 1 mes | 352,90 | 7,04,E-09 | 1,70,E-09 | 1,42,E-09 | 1,96,E-08 | 4,65,E-09 |
| AREA | SRC_350 | Cam_Valpo_231-PEAS e Imp | 268324 | 6397741 | 1 mes | 244,09 | 1,02,E-08 | 2,46,E-09 | 2,05,E-09 | 2,83,E-08 | 6,73,E-09 |
| AREA | SRC_351 | Cam_Valpo_232-PEAS e Imp | 268344 | 6397809 | 1 mes | 284,52 | 8,74,E-09 | 2,11,E-09 | 1,76,E-09 | 2,43,E-08 | 5,77,E-09 |
| AREA | SRC_352 | Cam_Valpo_233-PEAS e Imp | 268317 | 6397871 | 1 mes | 277,40 | 8,96,E-09 | 2,17,E-09 | 1,81,E-09 | 2,49,E-08 | 5,92,E-09 |
| AREA | SRC_353 | Cam_Valpo_234-PEAS e Imp | 268289 | 6397931 | 1 mes | 263,44 | 9,43,E-09 | 2,28,E-09 | 1,90,E-09 | 2,62,E-08 | 6,24,E-09 |
| AREA | SRC_354 | Cam_Valpo_235-PEAS e Imp | 268281 | 6397993 | 1 mes | 246,21 | 1,01,E-08 | 2,44,E-09 | 2,04,E-09 | 2,81,E-08 | 6,67,E-09 |
| AREA | SRC_355 | Cam_Valpo_236-PEAS e Imp | 268325 | 6398057 | 1 mes | 307,11 | 8,09,E-09 | 1,96,E-09 | 1,63,E-09 | 2,25,E-08 | 5,35,E-09 |
| AREA | SRC_356 | Cam_Valpo_237-PEAS e Imp | 268339 | 6398092 | 1 mes | 154,12 | 1,61,E-08 | 3,90,E-09 | 3,25,E-09 | 4,49,E-08 | 1,07,E-08 |
| AREA | SRC_357 | Cam_Valpo_238-PEAS e Imp | 268362 | 6398151 | 1 mes | 251,56 | 9,88,E-09 | 2,39,E-09 | 1,99,E-09 | 2,75,E-08 | 6,53,E-09 |
| AREA | SRC_358 | Cam_Valpo_239-PEAS e Imp | 268383 | 6398192 | 1 mes | 185,19 | 1,34,E-08 | 3,25,E-09 | 2,71,E-09 | 3,73,E-08 | 8,87,E-09 |
| AREA | SRC_359 | Cam_Valpo_240-PEAS e Imp | 268355 | 6398247 | 1 mes | 250,18 | 9,94,E-09 | 2,40,E-09 | 2,00,E-09 | 2,76,E-08 | 6,57,E-09 |
| AREA | SRC_360 | Cam_Valpo_241-PEAS e Imp | 268227 | 6398303 | 1 mes | 566,84 | 4,38,E-09 | 1,06,E-09 | 8,84,E-10 | 1,22,E-08 | 2,90,E-09 |
| AREA | SRC_361 | Cam_Valpo_242-PEAS e Imp | 268140 | 6398362 | 1 mes | 418,83 | 5,93,E-09 | 1,44,E-09 | 1,20,E-09 | 1,65,E-08 | 3,92,E-09 |
| AREA | SRC_362 | Cam_Valpo_243-PEAS e Imp | 268089 | 6398427 | 1 mes | 325,43 | 7,64,E-09 | 1,85,E-09 | 1,54,E-09 | 2,12,E-08 | 5,05,E-09 |
| AREA | SRC_363 | Cam_Valpo_244-PEAS e Imp | 268005 | 6398483 | 1 mes | 406,15 | 6,12,E-09 | 1,48,E-09 | 1,23,E-09 | 1,70,E-08 | 4,04,E-09 |
| AREA | SRC_364 | Cam_Valpo_245-PEAS e Imp | 267956 | 6398553 | 1 mes | 338,26 | 7,35,E-09 | 1,78,E-09 | 1,48,E-09 | 2,04,E-08 | 4,86,E-09 |
| AREA | SRC_365 | Cam_Valpo_246-PEAS e Imp | 267920 | 6398673 | 1 mes | 498,96 | 4,98,E-09 | 1,21,E-09 | 1,00,E-09 | 1,39,E-08 | 3,29,E-09 |
| AREA | SRC_366 | Cam_Valpo_247-PEAS e Imp | 267908 | 6398749 | 1 mes | 308,37 | 8,06,E-09 | 1,95,E-09 | 1,63,E-09 | 2,24,E-08 | 5,33,E-09 |
| AREA | SRC_367 | Cam_Valpo_248-PEAS e Imp | 267894 | 6398771 | 1 mes | 107,41 | 2,31,E-08 | 5,60,E-09 | 4,67,E-09 | 6,44,E-08 | 1,53,E-08 |
| AREA | SRC_368 | Cam_Valpo_249-PEAS e Imp | 267791 | 6398823 | 1 mes | 466,56 | 5,33,E-09 | 1,29,E-09 | 1,07,E-09 | 1,48,E-08 | 3,52,E-09 |
| AREA | SRC_369 | Cam_Valpo_250-PEAS e Imp | 267747 | 6398849 | 1 mes | 204,00 | 1,22,E-08 | 2,95,E-09 | 2,46,E-09 | 3,39,E-08 | 8,05,E-09 |
| AREA | SRC_370 | Cam_Valpo_251-PEAS e Imp | 267699 | 6398875 | 1 mes | 217,15 | 1,14,E-08 | 2,77,E-09 | 2,31,E-09 | 3,18,E-08 | 7,56,E-09 |
| AREA | SRC_371 | Cam_Valpo_252-PEAS e Imp | 267673 | 6398943 | 1 mes | 285,91 | 8,69,E-09 | 2,10,E-09 | 1,75,E-09 | 2,42,E-08 | 5,75,E-09 |
| AREA | SRC_372 | Cam_Valpo_253-PEAS e Imp | 267740 | 6399152 | 1 mes | 871,99 | 2,85,E-09 | 6,90,E-10 | 5,75,E-10 | 7,93,E-09 | 1,88,E-09 |
| AREA | SRC_373 | Cam_Valpo_254-PEAS e Imp | 267754 | 6399259 | 1 mes | 434,37 | 5,72,E-09 | 1,38,E-09 | 1,15,E-09 | 1,59,E-08 | 3,78,E-09 |

**Tabla 110.: Fuentes de Emisión - Escenario 3 parte 12**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m]<br>267956 | [m]<br>6398553 | [m]<br>6398553 | [m2]<br>338,26 | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_659 | Cam_Valpo_245-PTAS | Cam_Valpo_245-PTAS | Cam_Valpo_245-PTAS | 7 meses | 7 meses | 5,15,E-10 | 5,15,E-10 | 5,15,E-10 | 5,15,E-10 | 5,15,E-10 |
| AREA | SRC_660 | Cam_Valpo_246-PTAS | 267920 | 6398673 | 7 meses | 498,96 | 3,49,E-10 | 3,49,E-10 | 3,49,E-10 | 3,49,E-10 | 3,49,E-10 |
| AREA | SRC_661 | Cam_Valpo_247-PTAS | 267908 | 6398749 | 7 meses | 308,37 | 5,65,E-10 | 5,65,E-10 | 5,65,E-10 | 5,65,E-10 | 5,65,E-10 |
| AREA | SRC_662 | Cam_Valpo_248-PTAS | 267894 | 6398771 | 7 meses | 107,41 | 1,62,E-09 | 1,62,E-09 | 1,62,E-09 | 1,62,E-09 | 1,62,E-09 |
| AREA | SRC_663 | Cam_Valpo_249-PTAS | 267791 | 6398823 | 7 meses | 466,56 | 3,73,E-10 | 3,73,E-10 | 3,73,E-10 | 3,73,E-10 | 3,73,E-10 |
| AREA | SRC_664 | Cam_Valpo_250-PTAS | 267747 | 6398849 | 7 meses | 204,00 | 8,54,E-10 | 8,54,E-10 | 8,54,E-10 | 8,54,E-10 | 8,54,E-10 |
| AREA | SRC_665 | Cam_Valpo_251-PTAS | 267699 | 6398875 | 7 meses | 217,15 | 8,02,E-10 | 8,02,E-10 | 8,02,E-10 | 8,02,E-10 | 8,02,E-10 |
| AREA | SRC_666 | Cam_Valpo_252-PTAS | 267673 | 6398943 | 7 meses | 285,91 | 6,09,E-10 | 6,09,E-10 | 6,09,E-10 | 6,09,E-10 | 6,09,E-10 |
| AREA | SRC_667 | Cam_Valpo_253-PTAS | 267740 | 6399152 | 7 meses | 871,99 | 2,00,E-10 | 2,00,E-10 | 2,00,E-10 | 2,00,E-10 | 2,00,E-10 |
| AREA | SRC_668 | Cam_Valpo_254-PTAS | 267754 | 6399259 | 7 meses | 434,37 | 4,01,E-10 | 4,01,E-10 | 4,01,E-10 | 4,01,E-10 | 4,01,E-10 |
| AREA | SRC_669 | Cam_Valpo_255-PTAS | 267756 | 6399372 | 7 meses | 452,93 | 3,85,E-10 | 3,85,E-10 | 3,85,E-10 | 3,85,E-10 | 3,85,E-10 |
| AREA | SRC_670 | Cam_Valpo_256-PTAS | 267702 | 6399478 | 7 meses | 480,03 | 3,63,E-10 | 3,63,E-10 | 3,63,E-10 | 3,63,E-10 | 3,63,E-10 |
| AREA | SRC_671 | Cam_Valpo_257-PTAS | 267740 | 6399547 | 7 meses | 307,21 | 5,67,E-10 | 5,67,E-10 | 5,67,E-10 | 5,67,E-10 | 5,67,E-10 |
| AREA | SRC_672 | Cam_Valpo_258-PTAS | 267742 | 6399624 | 7 meses | 311,56 | 5,59,E-10 | 5,59,E-10 | 5,59,E-10 | 5,59,E-10 | 5,59,E-10 |
| AREA | SRC_673 | Cam_Valpo_259-PTAS | 267731 | 6399695 | 7 meses | 287,58 | 6,06,E-10 | 6,06,E-10 | 6,06,E-10 | 6,06,E-10 | 6,06,E-10 |
| AREA | SRC_674 | Cam_Valpo_260-PTAS | 267682 | 6399788 | 7 meses | 425,70 | 4,09,E-10 | 4,09,E-10 | 4,09,E-10 | 4,09,E-10 | 4,09,E-10 |
| AREA | SRC_675 | Cam_Valpo_261-PTAS | 267661 | 6399830 | 7 meses | 187,04 | 9,32,E-10 | 9,32,E-10 | 9,32,E-10 | 9,32,E-10 | 9,32,E-10 |

**Tabla 111.: Fuentes de Emisión - Escenario 3 parte 13**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/s] | [g/s] | [g/s] | [g/s] | [g/s] |
| VOLUMEN | SRC_26 | Peas_9 | 272534,98 | 6385157,02 | 1 mes | 4 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_27 | Peas_10 | 272710,98 | 6386276,01 | 1 mes | 4 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_28 | Imp_9 | 272634,97 | 6385155,98 | 1 mes | 4 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_29 | Imp_10.1 | 272663,05 | 6386154,98 | 1 mes | 4 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| VOLUMEN | SRC_30 | Imp_10.2 | 272621,03 | 6386107,97 | 1 mes | 4 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| PUNTUAL | SRC_51 | IF 1 | 272319 | 6384980 | 1 mes | 0,05 | 1,99,E-03 | 4,81,E-04 | 0,00,E+00 | 5,66,E-02 | 1,22,E-02 |
| PUNTUAL | SRC_52 | IF 2 | 273521,82 | 6383276,23 | 1 mes | 0,05 | 1,99,E-03 | 4,81,E-04 | 0,00,E+00 | 5,66,E-02 | 1,22,E-02 |

**Tabla 112.: Fuentes de Emisión - Escenario 4 parte 1**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_1 | Colec_x1 | 271160 | 6382780 | 3 meses | 4,00 | 1,09,E-03 | 5,45,E-04 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_2 | Colec_x2 | 271232 | 6382755 | 3 meses | 4,00 | 1,09,E-03 | 5,45,E-04 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_3 | Colec_x3 | 271317 | 6382733 | 3 meses | 4,00 | 1,09,E-03 | 5,45,E-04 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_4 | Colec_x4 | 271281 | 6382672 | 3 meses | 4,00 | 1,09,E-03 | 5,45,E-04 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_5 | Colec_x5 | 271238 | 6382627 | 3 meses | 4,00 | 1,09,E-03 | 5,45,E-04 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_6 | Colec_x6 | 271296 | 6382492 | 3 meses | 4,00 | 1,09,E-03 | 5,45,E-04 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_7 | Colec_x7 | 271377 | 6382401 | 3 meses | 4,00 | 1,09,E-03 | 5,45,E-04 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |

**Tabla 134.: Fuentes de Emisión - Escenario 4 parte 23**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/s] | [g/s] | [g/s] | [g/s] | [g/s] |
| VOLUMEN | SRC_8 | Colec_x1 | 271162 | 6382782 | 3 meses | 4,00 | 0,00014 | 0,00002 | 0,00000 | 0,00000 | 0,00000 |
| VOLUMEN | SRC_9 | Colec_x2 | 271234 | 6382757 | 3 meses | 4,00 | 0,00014 | 0,00002 | 0,00000 | 0,00000 | 0,00000 |
| VOLUMEN | SRC_10 | Colec_x3 | 271319 | 6382735 | 3 meses | 4,00 | 0,00014 | 0,00002 | 0,00000 | 0,00000 | 0,00000 |
| VOLUMEN | SRC_11 | Colec_x4 | 271283 | 6382674 | 3 meses | 4,00 | 0,00014 | 0,00002 | 0,00000 | 0,00000 | 0,00000 |
| VOLUMEN | SRC_12 | Colec_x5 | 271240 | 6382629 | 3 meses | 4,00 | 0,00014 | 0,00002 | 0,00000 | 0,00000 | 0,00000 |
| VOLUMEN | SRC_13 | Colec_x6 | 271298 | 6382494 | 3 meses | 4,00 | 0,00014 | 0,00002 | 0,00000 | 0,00000 | 0,00000 |
| VOLUMEN | SRC_14 | Colec_x7 | 271379 | 6382403 | 3 meses | 4,00 | 0,00014 | 0,00002 | 0,00000 | 0,00000 | 0,00000 |
| VOLUMEN | SRC_346 | PTAS | 273588 | 6383221 | 7 meses | 4,00 | 0,00064 | 0,00010 | 0,00000 | 0,00000 | 0,00000 |
| PUNTUAL | SRC_15 | IF1 | 273522 | 6383276 | 3 meses | 0,05 | 0,00199 | 0,00048 | 0,00000 | 0,05662 | 0,01223 |
| PUNTUAL | SRC_16 | IF2 | 273522 | 6383276 | 3 meses | 0,05 | 0,00199 | 0,00048 | 0,00000 | 0,05662 | 0,01223 |
| PUNTUAL | SRC_347 | PTAS | 273588 | 6383221 | 7 meses | 0,05 | 0,00200 | 0,00048 | 0,00000 | 0,05677 | 0,01226 |

**Tabla 135.: Fuentes de Emisión - Escenario 5 parte 1**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_1 | PTAS | 273586 | 6383219 | 4 mes | 4,00 | 4,29,E-03 | 4,29,E-03 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| AREA | SRC_4 | Cam_Cat_1-PEAS e Imp | 273043 | 6387323 | 3 mes | 383,32 | 6,04,E-10 | 1,46,E-10 | 3,40,E-10 | 6,80,E-09 | 1,93,E-11 |
| AREA | SRC_5 | Cam_Cat_2-PEAS e Imp | 273206 | 6387558 | 3 mes | 1145,03 | 2,02,E-10 | 4,89,E-11 | 1,14,E-10 | 2,28,E-09 | 6,45,E-12 |
| AREA | SRC_6 | Cam_Cat_3-PEAS e Imp | 273308 | 6387612 | 3 mes | 456,00 | 5,07,E-10 | 1,23,E-10 | 2,86,E-10 | 5,72,E-09 | 1,62,E-11 |
| AREA | SRC_7 | Cam_Cat_4-PEAS e Imp | 273511 | 6387668 | 3 mes | 843,57 | 2,74,E-10 | 6,64,E-11 | 1,54,E-10 | 3,09,E-09 | 8,75,E-12 |
| AREA | SRC_8 | Cam_Cat_5-PEAS e Imp | 273721 | 6387707 | 3 mes | 853,32 | 2,71,E-10 | 6,56,E-11 | 1,53,E-10 | 3,05,E-09 | 8,65,E-12 |
| AREA | SRC_9 | Cam_Cat_6-PEAS e Imp | 273880 | 6387880 | 3 mes | 945,26 | 2,45,E-10 | 5,92,E-11 | 1,38,E-10 | 2,76,E-09 | 7,81,E-12 |
| AREA | SRC_10 | Cam_Cat_7-PEAS e Imp | 273982 | 6387934 | 3 mes | 457,52 | 5,06,E-10 | 1,22,E-10 | 2,85,E-10 | 5,70,E-09 | 1,61,E-11 |
| AREA | SRC_11 | Cam_Cat_8-PEAS e Imp | 274178 | 6387916 | 3 mes | 782,20 | 2,96,E-10 | 7,16,E-11 | 1,67,E-10 | 3,33,E-09 | 9,44,E-12 |
| AREA | SRC_12 | Cam_Cat_9-PEAS e Imp | 274216 | 6387945 | 3 mes | 195,48 | 1,18,E-09 | 2,86,E-10 | 6,66,E-10 | 1,33,E-08 | 3,78,E-11 |
| AREA | SRC_13 | Cam_Cat_10-PEAS e Imp | 274213 | 6388017 | 3 mes | 295,61 | 7,83,E-10 | 1,89,E-10 | 4,41,E-10 | 8,82,E-09 | 2,50,E-11 |
| AREA | SRC_14 | Cam_Cat_11-PEAS e Imp | 274177 | 6388250 | 3 mes | 941,53 | 2,46,E-10 | 5,95,E-11 | 1,38,E-10 | 2,77,E-09 | 7,84,E-12 |
| AREA | SRC_15 | Cam_Cat_12-PEAS e Imp | 274185 | 6388365 | 3 mes | 458,34 | 5,05,E-10 | 1,22,E-10 | 2,84,E-10 | 5,69,E-09 | 1,61,E-11 |
| AREA | SRC_16 | Cam_Cat_13-PEAS e Imp | 274352 | 6388558 | 3 mes | 1016,92 | 2,28,E-10 | 5,50,E-11 | 1,28,E-10 | 2,56,E-09 | 7,26,E-12 |
| AREA | SRC_17 | Cam_Cat_14-PEAS e Imp | 274654 | 6388846 | 3 mes | 1667,00 | 1,39,E-10 | 3,36,E-11 | 7,81,E-11 | 1,56,E-09 | 4,43,E-12 |
| AREA | SRC_18 | Cam_Cat_15-PEAS e Imp | 274745 | 6388895 | 3 mes | 409,81 | 5,65,E-10 | 1,37,E-10 | 3,18,E-10 | 6,36,E-09 | 1,80,E-11 |
| AREA | SRC_19 | Cam_Cat_16-PEAS e Imp | 274834 | 6388862 | 3 mes | 371,12 | 6,23,E-10 | 1,51,E-10 | 3,51,E-10 | 7,02,E-09 | 1,99,E-11 |
| AREA | SRC_20 | Cam_Cat_17-PEAS e Imp | 274882 | 6388794 | 3 mes | 331,29 | 6,98,E-10 | 1,69,E-10 | 3,93,E-10 | 7,87,E-09 | 2,23,E-11 |
| AREA | SRC_21 | Cam_Cat_18-PEAS e Imp | 274979 | 6388768 | 3 mes | 406,63 | 5,69,E-10 | 1,38,E-10 | 3,20,E-10 | 6,41,E-09 | 1,82,E-11 |
| AREA | SRC_22 | Cam_Cat_19-PEAS e Imp | 275069 | 6388799 | 3 mes | 384,16 | 6,02,E-10 | 1,46,E-10 | 3,39,E-10 | 6,78,E-09 | 1,92,E-11 |
| AREA | SRC_23 | Cam_Cat_20-PEAS e Imp | 275059 | 6388911 | 3 mes | 459,52 | 5,04,E-10 | 1,22,E-10 | 2,83,E-10 | 5,67,E-09 | 1,61,E-11 |
| AREA | SRC_24 | Cam_Cat_21-PEAS e Imp | 275040 | 6389003 | 3 mes | 374,05 | 6,19,E-10 | 1,50,E-10 | 3,48,E-10 | 6,97,E-09 | 1,97,E-11 |
| AREA | SRC_25 | Cam_Cat_22-PEAS e Imp | 274958 | 6389092 | 3 mes | 489,11 | 4,73,E-10 | 1,14,E-10 | 2,66,E-10 | 5,33,E-09 | 1,51,E-11 |

**Tabla 136.: Fuentes de Emisión - Escenario 5 parte 2**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m]<br>274915 | [m]<br>6389184 | [m]<br>6389184 | [m2]<br>402,20 | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_26 | Cam_Cat_23-PEAS e Imp | Cam_Cat_23-PEAS e Imp | Cam_Cat_23-PEAS e Imp | 3 mes | 3 mes | 5,75,E-10 | 1,39,E-10 | 3,24,E-10 | 6,48,E-09 | 1,84,E-11 |
| AREA | SRC_27 | Cam_Cat_24-PEAS e Imp | 274946 | 6389307 | 3 mes | 502,79 | 4,60,E-10 | 1,11,E-10 | 2,59,E-10 | 5,18,E-09 | 1,47,E-11 |
| AREA | SRC_28 | Cam_Cat_25-PEAS e Imp | 275049 | 6389374 | 3 mes | 485,06 | 4,77,E-10 | 1,15,E-10 | 2,69,E-10 | 5,37,E-09 | 1,52,E-11 |
| AREA | SRC_29 | Cam_Cat_26-PEAS e Imp | 275181 | 6389406 | 3 mes | 541,36 | 4,27,E-10 | 1,03,E-10 | 2,41,E-10 | 4,81,E-09 | 1,36,E-11 |
| AREA | SRC_30 | Cam_Cat_27-PEAS e Imp | 275286 | 6389385 | 3 mes | 424,34 | 5,45,E-10 | 1,32,E-10 | 3,07,E-10 | 6,14,E-09 | 1,74,E-11 |
| AREA | SRC_31 | Cam_Cat_28-PEAS e Imp | 275372 | 6389387 | 3 mes | 345,06 | 6,71,E-10 | 1,62,E-10 | 3,77,E-10 | 7,55,E-09 | 2,14,E-11 |
| AREA | SRC_32 | Cam_Cat_29-PEAS e Imp | 275519 | 6389442 | 3 mes | 633,26 | 3,65,E-10 | 8,84,E-11 | 2,06,E-10 | 4,12,E-09 | 1,17,E-11 |
| AREA | SRC_33 | Cam_Cat_30-PEAS e Imp | 275575 | 6389512 | 3 mes | 360,36 | 6,42,E-10 | 1,55,E-10 | 3,61,E-10 | 7,23,E-09 | 2,05,E-11 |
| AREA | SRC_34 | Cam_Cat_31-PEAS e Imp | 275579 | 6389623 | 3 mes | 447,31 | 5,17,E-10 | 1,25,E-10 | 2,91,E-10 | 5,83,E-09 | 1,65,E-11 |
| AREA | SRC_35 | Cam_Cat_32-PEAS e Imp | 275473 | 6389738 | 3 mes | 629,59 | 3,68,E-10 | 8,89,E-11 | 2,07,E-10 | 4,14,E-09 | 1,17,E-11 |
| AREA | SRC_36 | Cam_Cat_33-PEAS e Imp | 275397 | 6389809 | 3 mes | 419,18 | 5,52,E-10 | 1,34,E-10 | 3,11,E-10 | 6,22,E-09 | 1,76,E-11 |
| AREA | SRC_37 | Cam_Cat_34-PEAS e Imp | 275382 | 6389918 | 3 mes | 432,78 | 5,35,E-10 | 1,29,E-10 | 3,01,E-10 | 6,02,E-09 | 1,71,E-11 |
| AREA | SRC_38 | Cam_Cat_35-PEAS e Imp | 275487 | 6390018 | 3 mes | 576,65 | 4,01,E-10 | 9,71,E-11 | 2,26,E-10 | 4,52,E-09 | 1,28,E-11 |
| AREA | SRC_39 | Cam_Cat_36-PEAS e Imp | 275630 | 6390045 | 3 mes | 576,34 | 4,01,E-10 | 9,71,E-11 | 2,26,E-10 | 4,52,E-09 | 1,28,E-11 |
| AREA | SRC_40 | Cam_Cat_37-PEAS e Imp | 275763 | 6390025 | 3 mes | 532,94 | 4,34,E-10 | 1,05,E-10 | 2,44,E-10 | 4,89,E-09 | 1,39,E-11 |
| AREA | SRC_41 | Cam_Cat_38-PEAS e Imp | 275861 | 6389993 | 3 mes | 411,71 | 5,62,E-10 | 1,36,E-10 | 3,16,E-10 | 6,33,E-09 | 1,79,E-11 |
| AREA | SRC_42 | Cam_Cat_39-PEAS e Imp | 276044 | 6389963 | 3 mes | 742,87 | 3,11,E-10 | 7,54,E-11 | 1,75,E-10 | 3,51,E-09 | 9,94,E-12 |
| AREA | SRC_43 | Cam_Cat_40-PEAS e Imp | 276114 | 6389925 | 3 mes | 316,96 | 7,30,E-10 | 1,77,E-10 | 4,11,E-10 | 8,22,E-09 | 2,33,E-11 |
| AREA | SRC_44 | Cam_Cat_41-PEAS e Imp | 276133 | 6389885 | 3 mes | 172,93 | 1,34,E-09 | 3,24,E-10 | 7,53,E-10 | 1,51,E-08 | 4,27,E-11 |
| AREA | SRC_45 | Cam_Cat_42-PEAS e Imp | 276158 | 6389818 | 3 mes | 286,84 | 8,07,E-10 | 1,95,E-10 | 4,54,E-10 | 9,09,E-09 | 2,57,E-11 |
| AREA | SRC_46 | Cam_Cat_43-PEAS e Imp | 276157 | 6389659 | 3 mes | 632,84 | 3,66,E-10 | 8,85,E-11 | 2,06,E-10 | 4,12,E-09 | 1,17,E-11 |
| AREA | SRC_47 | Cam_Cat_44-PEAS e Imp | 276172 | 6389529 | 3 mes | 521,10 | 4,44,E-10 | 1,07,E-10 | 2,50,E-10 | 5,00,E-09 | 1,42,E-11 |
| AREA | SRC_48 | Cam_Cat_45-PEAS e Imp | 276275 | 6389477 | 3 mes | 468,32 | 4,94,E-10 | 1,20,E-10 | 2,78,E-10 | 5,56,E-09 | 1,58,E-11 |
| AREA | SRC_49 | Cam_Cat_46-PEAS e Imp | 276411 | 6389458 | 3 mes | 553,37 | 4,18,E-10 | 1,01,E-10 | 2,35,E-10 | 4,71,E-09 | 1,33,E-11 |
| AREA | SRC_50 | Cam_Cat_47-PEAS e Imp | 276501 | 6389471 | 3 mes | 366,24 | 6,32,E-10 | 1,53,E-10 | 3,56,E-10 | 7,12,E-09 | 2,02,E-11 |

**Tabla 137.: Fuentes de Emisión - Escenario 5 parte 3**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m]<br>276706 | [m]<br>6389673 | [m]<br>6389673 | [m2]<br>1151,46 | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_51 | Cam_Cat_48-PEAS e Imp | Cam_Cat_48-PEAS e Imp | Cam_Cat_48-PEAS e Imp | 3 mes | 3 mes | 2,01,E-10 | 4,86,E-11 | 1,13,E-10 | 2,26,E-09 | 6,41,E-12 |
| AREA | SRC_52 | Cam_Cat_49-PEAS e Imp | 277353 | 6390498 | 3 mes | 4195,41 | 5,52,E-11 | 1,33,E-11 | 3,10,E-11 | 6,21,E-10 | 1,76,E-12 |
| AREA | SRC_53 | Cam_Cat_50-PEAS e Imp | 277494 | 6390575 | 3 mes | 640,03 | 3,62,E-10 | 8,75,E-11 | 2,03,E-10 | 4,07,E-09 | 1,15,E-11 |
| AREA | SRC_54 | Cam_Cat_51-PEAS e Imp | 279440 | 6391244 | 3 mes | 8223,68 | 2,81,E-11 | 6,81,E-12 | 1,58,E-11 | 3,17,E-10 | 8,98,E-13 |
| AREA | SRC_55 | Cam_Cat_52-PEAS e Imp | 283346 | 6393239 | 3 mes | 17540,88 | 1,32,E-11 | 3,19,E-12 | 7,43,E-12 | 1,49,E-10 | 4,21,E-13 |
| AREA | SRC_56 | Cam_Cat_53-PEAS e Imp | 287745 | 6394661 | 3 mes | 18483,13 | 1,25,E-11 | 3,03,E-12 | 7,05,E-12 | 1,41,E-10 | 3,99,E-13 |
| AREA | SRC_57 | Cam_Pta_1-PEAS e Imp | 273147 | 6383634 | 3 mes | 1866,42 | 1,24,E-10 | 3,00,E-11 | 6,98,E-11 | 1,40,E-09 | 3,96,E-12 |
| AREA | SRC_58 | Cam_Pta_2-PEAS e Imp | 273165 | 6383642 | 3 mes | 80,85 | 2,86,E-09 | 6,92,E-10 | 1,61,E-09 | 3,22,E-08 | 9,13,E-11 |
| AREA | SRC_59 | Cam_Pta_3-PEAS e Imp | 273189 | 6383637 | 3 mes | 94,14 | 2,46,E-09 | 5,95,E-10 | 1,38,E-09 | 2,77,E-08 | 7,84,E-11 |
| AREA | SRC_60 | Cam_Pta_4-PEAS e Imp | 273241 | 6383562 | 3 mes | 359,95 | 6,43,E-10 | 1,56,E-10 | 3,62,E-10 | 7,24,E-09 | 2,05,E-11 |
| AREA | SRC_61 | Cam_Pta_5-PEAS e Imp | 273289 | 6383445 | 3 mes | 505,57 | 4,58,E-10 | 1,11,E-10 | 2,58,E-10 | 5,15,E-09 | 1,46,E-11 |
| AREA | SRC_62 | Cam_Pta_6-PEAS e Imp | 273304 | 6383402 | 3 mes | 179,62 | 1,29,E-09 | 3,12,E-10 | 7,25,E-10 | 1,45,E-08 | 4,11,E-11 |
| AREA | SRC_63 | Cam_Pta_7-PEAS e Imp | 273331 | 6383382 | 3 mes | 138,45 | 1,67,E-09 | 4,04,E-10 | 9,41,E-10 | 1,88,E-08 | 5,33,E-11 |
| AREA | SRC_64 | Cam_Pta_8-PEAS e Imp | 273361 | 6383362 | 3 mes | 145,56 | 1,59,E-09 | 3,85,E-10 | 8,95,E-10 | 1,79,E-08 | 5,07,E-11 |
| AREA | SRC_65 | Cam_Pta_9-PEAS e Imp | 273393 | 6383346 | 3 mes | 143,99 | 1,61,E-09 | 3,89,E-10 | 9,05,E-10 | 1,81,E-08 | 5,13,E-11 |
| AREA | SRC_66 | Cam_Pta_10-PEAS e Imp | 273413 | 6383324 | 3 mes | 116,32 | 1,99,E-09 | 4,81,E-10 | 1,12,E-09 | 2,24,E-08 | 6,35,E-11 |
| AREA | SRC_67 | Cam_Pta_11-PEAS e Imp | 273447 | 6383229 | 3 mes | 400,03 | 5,78,E-10 | 1,40,E-10 | 3,26,E-10 | 6,51,E-09 | 1,85,E-11 |
| AREA | SRC_68 | Cam_Pta_12-PEAS e Imp | 273463 | 6383220 | 3 mes | 80,13 | 2,89,E-09 | 6,99,E-10 | 1,63,E-09 | 3,25,E-08 | 9,21,E-11 |
| AREA | SRC_69 | Cam_Pta_13-PEAS e Imp | 273473 | 6383218 | 3 mes | 45,12 | 5,13,E-09 | 1,24,E-09 | 2,89,E-09 | 5,78,E-08 | 1,64,E-10 |
| AREA | SRC_70 | Cam_Pta_14-PEAS e Imp | 273519 | 6383228 | 3 mes | 188,53 | 1,23,E-09 | 2,97,E-10 | 6,91,E-10 | 1,38,E-08 | 3,92,E-11 |
| AREA | SRC_71 | Cam_Valpo_1-PEAS e Imp | 267407 | 6370003 | 3 mes | 9181,86 | 2,52,E-11 | 6,10,E-12 | 1,42,E-11 | 2,84,E-10 | 8,04,E-13 |
| AREA | SRC_72 | Cam_Valpo_2-PEAS e Imp | 267402 | 6370088 | 3 mes | 338,29 | 6,84,E-10 | 1,65,E-10 | 3,85,E-10 | 7,70,E-09 | 2,18,E-11 |
| AREA | SRC_73 | Cam_Valpo_3-PEAS e Imp | 267699 | 6371506 | 3 mes | 5788,94 | 4,00,E-11 | 9,67,E-12 | 2,25,E-11 | 4,50,E-10 | 1,28,E-12 |
| AREA | SRC_74 | Cam_Valpo_4-PEAS e Imp | 267700 | 6371619 | 3 mes | 452,00 | 5,12,E-10 | 1,24,E-10 | 2,88,E-10 | 5,77,E-09 | 1,63,E-11 |
| AREA | SRC_75 | Cam_Valpo_5-PEAS e Imp | 267517 | 6371917 | 3 mes | 1401,44 | 1,65,E-10 | 3,99,E-11 | 9,29,E-11 | 1,86,E-09 | 5,27,E-12 |

**Tabla 138.: Fuentes de Emisión - Escenario 5 parte 4**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m]<br>267499 | [m]<br>6371980 | [m]<br>6371980 | [m2]<br>261,10 | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_76 | Cam_Valpo_6-PEAS e Imp | Cam_Valpo_6-PEAS e Imp | Cam_Valpo_6-PEAS e Imp | 3 mes | 3 mes | 8,86,E-10 | 2,14,E-10 | 4,99,E-10 | 9,98,E-09 | 2,83,E-11 |
| AREA | SRC_77 | Cam_Valpo_7-PEAS e Imp | 267496 | 6372042 | 3 mes | 247,03 | 9,37,E-10 | 2,27,E-10 | 5,27,E-10 | 1,06,E-08 | 2,99,E-11 |
| AREA | SRC_78 | Cam_Valpo_8-PEAS e Imp | 267518 | 6372113 | 3 mes | 294,47 | 7,86,E-10 | 1,90,E-10 | 4,42,E-10 | 8,85,E-09 | 2,51,E-11 |
| AREA | SRC_79 | Cam_Valpo_9-PEAS e Imp | 267547 | 6372151 | 3 mes | 187,43 | 1,23,E-09 | 2,99,E-10 | 6,95,E-10 | 1,39,E-08 | 3,94,E-11 |
| AREA | SRC_80 | Cam_Valpo_10-PEAS e Imp | 267569 | 6372177 | 3 mes | 137,02 | 1,69,E-09 | 4,09,E-10 | 9,51,E-10 | 1,90,E-08 | 5,39,E-11 |
| AREA | SRC_81 | Cam_Valpo_11-PEAS e Imp | 267738 | 6372319 | 3 mes | 879,83 | 2,63,E-10 | 6,36,E-11 | 1,48,E-10 | 2,96,E-09 | 8,39,E-12 |
| AREA | SRC_82 | Cam_Valpo_12-PEAS e Imp | 267762 | 6372358 | 3 mes | 186,57 | 1,24,E-09 | 3,00,E-10 | 6,98,E-10 | 1,40,E-08 | 3,96,E-11 |
| AREA | SRC_83 | Cam_Valpo_13-PEAS e Imp | 267783 | 6372410 | 3 mes | 224,51 | 1,03,E-09 | 2,49,E-10 | 5,80,E-10 | 1,16,E-08 | 3,29,E-11 |
| AREA | SRC_84 | Cam_Valpo_14-PEAS e Imp | 267855 | 6372669 | 3 mes | 1075,61 | 2,15,E-10 | 5,20,E-11 | 1,21,E-10 | 2,42,E-09 | 6,86,E-12 |
| AREA | SRC_85 | Cam_Valpo_15-PEAS e Imp | 267848 | 6372720 | 3 mes | 207,78 | 1,11,E-09 | 2,69,E-10 | 6,27,E-10 | 1,25,E-08 | 3,55,E-11 |
| AREA | SRC_86 | Cam_Valpo_16-PEAS e Imp | 267715 | 6373066 | 3 mes | 1484,08 | 1,56,E-10 | 3,77,E-11 | 8,78,E-11 | 1,76,E-09 | 4,98,E-12 |
| AREA | SRC_87 | Cam_Valpo_17-PEAS e Imp | 267705 | 6373122 | 3 mes | 225,43 | 1,03,E-09 | 2,48,E-10 | 5,78,E-10 | 1,16,E-08 | 3,28,E-11 |
| AREA | SRC_88 | Cam_Valpo_18-PEAS e Imp | 267701 | 6373182 | 3 mes | 241,22 | 9,59,E-10 | 2,32,E-10 | 5,40,E-10 | 1,08,E-08 | 3,06,E-11 |
| AREA | SRC_89 | Cam_Valpo_19-PEAS e Imp | 267704 | 6373237 | 3 mes | 217,96 | 1,06,E-09 | 2,57,E-10 | 5,98,E-10 | 1,20,E-08 | 3,39,E-11 |
| AREA | SRC_90 | Cam_Valpo_20-PEAS e Imp | 267713 | 6373309 | 3 mes | 291,26 | 7,94,E-10 | 1,92,E-10 | 4,47,E-10 | 8,95,E-09 | 2,54,E-11 |
| AREA | SRC_91 | Cam_Valpo_21-PEAS e Imp | 267741 | 6373522 | 3 mes | 860,16 | 2,69,E-10 | 6,51,E-11 | 1,51,E-10 | 3,03,E-09 | 8,58,E-12 |
| AREA | SRC_92 | Cam_Valpo_22-PEAS e Imp | 267757 | 6373574 | 3 mes | 213,85 | 1,08,E-09 | 2,62,E-10 | 6,09,E-10 | 1,22,E-08 | 3,45,E-11 |
| AREA | SRC_93 | Cam_Valpo_23-PEAS e Imp | 267777 | 6373617 | 3 mes | 187,32 | 1,24,E-09 | 2,99,E-10 | 6,95,E-10 | 1,39,E-08 | 3,94,E-11 |
| AREA | SRC_94 | Cam_Valpo_24-PEAS e Imp | 267817 | 6373719 | 3 mes | 441,14 | 5,25,E-10 | 1,27,E-10 | 2,95,E-10 | 5,91,E-09 | 1,67,E-11 |
| AREA | SRC_95 | Cam_Valpo_25-PEAS e Imp | 267843 | 6373782 | 3 mes | 272,58 | 8,49,E-10 | 2,05,E-10 | 4,78,E-10 | 9,56,E-09 | 2,71,E-11 |
| AREA | SRC_96 | Cam_Valpo_26-PEAS e Imp | 267877 | 6373831 | 3 mes | 236,03 | 9,80,E-10 | 2,37,E-10 | 5,52,E-10 | 1,10,E-08 | 3,13,E-11 |
| AREA | SRC_97 | Cam_Valpo_27-PEAS e Imp | 267910 | 6373883 | 3 mes | 246,12 | 9,40,E-10 | 2,27,E-10 | 5,29,E-10 | 1,06,E-08 | 3,00,E-11 |
| AREA | SRC_98 | Cam_Valpo_28-PEAS e Imp | 268105 | 6374174 | 3 mes | 1399,53 | 1,65,E-10 | 4,00,E-11 | 9,31,E-11 | 1,86,E-09 | 5,28,E-12 |
| AREA | SRC_99 | Cam_Valpo_29-PEAS e Imp | 268274 | 6374430 | 3 mes | 1228,07 | 1,88,E-10 | 4,56,E-11 | 1,06,E-10 | 2,12,E-09 | 6,01,E-12 |
| AREA | SRC_100 | Cam_Valpo_30-PEAS e Imp | 268317 | 6374478 | 3 mes | 254,35 | 9,10,E-10 | 2,20,E-10 | 5,12,E-10 | 1,02,E-08 | 2,90,E-11 |

**Tabla 139.: Fuentes de Emisión - Escenario 5 parte 5**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m]<br>268347 | [m]<br>6374502 | [m]<br>6374502 | [m2]<br>154,46 | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_101 | Cam_Valpo_31-PEAS e Imp | Cam_Valpo_31-PEAS e Imp | Cam_Valpo_31-PEAS e Imp | 3 mes | 3 mes | 1,50,E-09 | 3,62,E-10 | 8,43,E-10 | 1,69,E-08 | 4,78,E-11 |
| AREA | SRC_102 | Cam_Valpo_32-PEAS e Imp | 269602 | 6375295 | 3 mes | 5935,56 | 3,90,E-11 | 9,43,E-12 | 2,19,E-11 | 4,39,E-10 | 1,24,E-12 |
| AREA | SRC_103 | Cam_Valpo_33-PEAS e Imp | 270646 | 6375956 | 3 mes | 4938,33 | 4,69,E-11 | 1,13,E-11 | 2,64,E-11 | 5,28,E-10 | 1,50,E-12 |
| AREA | SRC_104 | Cam_Valpo_34-PEAS e Imp | 270700 | 6375970 | 3 mes | 220,74 | 1,05,E-09 | 2,54,E-10 | 5,90,E-10 | 1,18,E-08 | 3,34,E-11 |
| AREA | SRC_105 | Cam_Valpo_35-PEAS e Imp | 270759 | 6375972 | 3 mes | 232,03 | 9,97,E-10 | 2,41,E-10 | 5,61,E-10 | 1,12,E-08 | 3,18,E-11 |
| AREA | SRC_106 | Cam_Valpo_36-PEAS e Imp | 270817 | 6375960 | 3 mes | 237,83 | 9,73,E-10 | 2,35,E-10 | 5,48,E-10 | 1,10,E-08 | 3,10,E-11 |
| AREA | SRC_107 | Cam_Valpo_37-PEAS e Imp | 271210 | 6375788 | 3 mes | 1710,95 | 1,35,E-10 | 3,27,E-11 | 7,61,E-11 | 1,52,E-09 | 4,32,E-12 |
| AREA | SRC_108 | Cam_Valpo_38-PEAS e Imp | 271299 | 6375786 | 3 mes | 362,06 | 6,39,E-10 | 1,55,E-10 | 3,60,E-10 | 7,20,E-09 | 2,04,E-11 |
| AREA | SRC_109 | Cam_Valpo_39-PEAS e Imp | 271410 | 6375784 | 3 mes | 444,09 | 5,21,E-10 | 1,26,E-10 | 2,93,E-10 | 5,87,E-09 | 1,66,E-11 |
| AREA | SRC_110 | Cam_Valpo_40-PEAS e Imp | 271537 | 6375829 | 3 mes | 539,94 | 4,29,E-10 | 1,04,E-10 | 2,41,E-10 | 4,83,E-09 | 1,37,E-11 |
| AREA | SRC_111 | Cam_Valpo_41-PEAS e Imp | 271698 | 6375908 | 3 mes | 717,64 | 3,22,E-10 | 7,80,E-11 | 1,81,E-10 | 3,63,E-09 | 1,03,E-11 |
| AREA | SRC_112 | Cam_Valpo_42-PEAS e Imp | 271943 | 6376040 | 3 mes | 1111,41 | 2,08,E-10 | 5,04,E-11 | 1,17,E-10 | 2,34,E-09 | 6,64,E-12 |
| AREA | SRC_113 | Cam_Valpo_43-PEAS e Imp | 272216 | 6376245 | 3 mes | 1365,82 | 1,69,E-10 | 4,10,E-11 | 9,54,E-11 | 1,91,E-09 | 5,41,E-12 |
| AREA | SRC_114 | Cam_Valpo_44-PEAS e Imp | 272308 | 6376283 | 3 mes | 396,81 | 5,83,E-10 | 1,41,E-10 | 3,28,E-10 | 6,57,E-09 | 1,86,E-11 |
| AREA | SRC_115 | Cam_Valpo_45-PEAS e Imp | 272828 | 6376412 | 3 mes | 2139,51 | 1,08,E-10 | 2,62,E-11 | 6,09,E-11 | 1,22,E-09 | 3,45,E-12 |
| AREA | SRC_116 | Cam_Valpo_46-PEAS e Imp | 272961 | 6376463 | 3 mes | 572,90 | 4,04,E-10 | 9,77,E-11 | 2,27,E-10 | 4,55,E-09 | 1,29,E-11 |
| AREA | SRC_117 | Cam_Valpo_47-PEAS e Imp | 273101 | 6376548 | 3 mes | 656,43 | 3,52,E-10 | 8,53,E-11 | 1,98,E-10 | 3,97,E-09 | 1,12,E-11 |
| AREA | SRC_118 | Cam_Valpo_48-PEAS e Imp | 273683 | 6376890 | 3 mes | 2699,98 | 8,57,E-11 | 2,07,E-11 | 4,82,E-11 | 9,65,E-10 | 2,73,E-12 |
| AREA | SRC_119 | Cam_Valpo_49-PEAS e Imp | 273729 | 6376911 | 3 mes | 198,66 | 1,16,E-09 | 2,82,E-10 | 6,56,E-10 | 1,31,E-08 | 3,72,E-11 |
| AREA | SRC_120 | Cam_Valpo_50-PEAS e Imp | 273841 | 6376934 | 3 mes | 455,50 | 5,08,E-10 | 1,23,E-10 | 2,86,E-10 | 5,72,E-09 | 1,62,E-11 |
| AREA | SRC_121 | Cam_Valpo_51-PEAS e Imp | 273918 | 6376948 | 3 mes | 314,84 | 7,35,E-10 | 1,78,E-10 | 4,14,E-10 | 8,28,E-09 | 2,35,E-11 |
| AREA | SRC_122 | Cam_Valpo_52-PEAS e Imp | 273963 | 6376959 | 3 mes | 182,29 | 1,27,E-09 | 3,07,E-10 | 7,14,E-10 | 1,43,E-08 | 4,05,E-11 |
| AREA | SRC_123 | Cam_Valpo_53-PEAS e Imp | 274013 | 6376981 | 3 mes | 220,22 | 1,05,E-09 | 2,54,E-10 | 5,91,E-10 | 1,18,E-08 | 3,35,E-11 |
| AREA | SRC_124 | Cam_Valpo_54-PEAS e Imp | 274045 | 6377010 | 3 mes | 175,74 | 1,32,E-09 | 3,19,E-10 | 7,41,E-10 | 1,48,E-08 | 4,20,E-11 |
| AREA | SRC_125 | Cam_Valpo_55-PEAS e Imp | 274402 | 6377569 | 3 mes | 2654,98 | 8,72,E-11 | 2,11,E-11 | 4,91,E-11 | 9,82,E-10 | 2,78,E-12 |

**Tabla 140.: Fuentes de Emisión - Escenario 5 parte 6**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m]<br>274508 | [m]<br>6377712 | [m]<br>6377712 | [m2]<br>712,20 | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_126 | Cam_Valpo_56-PEAS e Imp | Cam_Valpo_56-PEAS e Imp | Cam_Valpo_56-PEAS e Imp | 3 mes | 3 mes | 3,25,E-10 | 7,86,E-11 | 1,83,E-10 | 3,66,E-09 | 1,04,E-11 |
| AREA | SRC_127 | Cam_Valpo_57-PEAS e Imp | 274515 | 6377737 | 3 mes | 105,54 | 2,19,E-09 | 5,30,E-10 | 1,23,E-09 | 2,47,E-08 | 7,00,E-11 |
| AREA | SRC_128 | Cam_Valpo_58-PEAS e Imp | 274530 | 6377783 | 3 mes | 190,85 | 1,21,E-09 | 2,93,E-10 | 6,82,E-10 | 1,37,E-08 | 3,87,E-11 |
| AREA | SRC_129 | Cam_Valpo_59-PEAS e Imp | 274571 | 6378190 | 3 mes | 1640,54 | 1,41,E-10 | 3,41,E-11 | 7,94,E-11 | 1,59,E-09 | 4,50,E-12 |
| AREA | SRC_130 | Cam_Valpo_60-PEAS e Imp | 274512 | 6378662 | 3 mes | 1902,24 | 1,22,E-10 | 2,94,E-11 | 6,85,E-11 | 1,37,E-09 | 3,88,E-12 |
| AREA | SRC_131 | Cam_Valpo_61-PEAS e Imp | 274484 | 6378742 | 3 mes | 339,36 | 6,82,E-10 | 1,65,E-10 | 3,84,E-10 | 7,68,E-09 | 2,18,E-11 |
| AREA | SRC_132 | Cam_Valpo_62-PEAS e Imp | 274397 | 6378959 | 3 mes | 934,88 | 2,48,E-10 | 5,99,E-11 | 1,39,E-10 | 2,79,E-09 | 7,90,E-12 |
| AREA | SRC_133 | Cam_Valpo_63-PEAS e Imp | 274391 | 6379006 | 3 mes | 189,58 | 1,22,E-09 | 2,95,E-10 | 6,87,E-10 | 1,37,E-08 | 3,89,E-11 |
| AREA | SRC_134 | Cam_Valpo_64-PEAS e Imp | 274392 | 6379034 | 3 mes | 109,49 | 2,11,E-09 | 5,11,E-10 | 1,19,E-09 | 2,38,E-08 | 6,74,E-11 |
| AREA | SRC_135 | Cam_Valpo_65-PEAS e Imp | 274513 | 6379469 | 3 mes | 1805,57 | 1,28,E-10 | 3,10,E-11 | 7,21,E-11 | 1,44,E-09 | 4,09,E-12 |
| AREA | SRC_136 | Cam_Valpo_66-PEAS e Imp | 274514 | 6379510 | 3 mes | 163,36 | 1,42,E-09 | 3,43,E-10 | 7,97,E-10 | 1,60,E-08 | 4,52,E-11 |
| AREA | SRC_137 | Cam_Valpo_67-PEAS e Imp | 274503 | 6379560 | 3 mes | 208,73 | 1,11,E-09 | 2,68,E-10 | 6,24,E-10 | 1,25,E-08 | 3,54,E-11 |
| AREA | SRC_138 | Cam_Valpo_68-PEAS e Imp | 274488 | 6379623 | 3 mes | 255,44 | 9,06,E-10 | 2,19,E-10 | 5,10,E-10 | 1,02,E-08 | 2,89,E-11 |
| AREA | SRC_139 | Cam_Valpo_69-PEAS e Imp | 274426 | 6379798 | 3 mes | 745,56 | 3,10,E-10 | 7,51,E-11 | 1,75,E-10 | 3,50,E-09 | 9,90,E-12 |
| AREA | SRC_140 | Cam_Valpo_70-PEAS e Imp | 274386 | 6379897 | 3 mes | 428,53 | 5,40,E-10 | 1,31,E-10 | 3,04,E-10 | 6,08,E-09 | 1,72,E-11 |
| AREA | SRC_141 | Cam_Valpo_71-PEAS e Imp | 274352 | 6379981 | 3 mes | 360,23 | 6,42,E-10 | 1,55,E-10 | 3,62,E-10 | 7,23,E-09 | 2,05,E-11 |
| AREA | SRC_142 | Cam_Valpo_72-PEAS e Imp | 274336 | 6380041 | 3 mes | 249,49 | 9,27,E-10 | 2,24,E-10 | 5,22,E-10 | 1,04,E-08 | 2,96,E-11 |
| AREA | SRC_143 | Cam_Valpo_73-PEAS e Imp | 274333 | 6380099 | 3 mes | 227,80 | 1,02,E-09 | 2,46,E-10 | 5,72,E-10 | 1,14,E-08 | 3,24,E-11 |
| AREA | SRC_144 | Cam_Valpo_74-PEAS e Imp | 274332 | 6380163 | 3 mes | 257,27 | 8,99,E-10 | 2,18,E-10 | 5,06,E-10 | 1,01,E-08 | 2,87,E-11 |
| AREA | SRC_145 | Cam_Valpo_75-PEAS e Imp | 274329 | 6380546 | 3 mes | 1530,44 | 1,51,E-10 | 3,66,E-11 | 8,51,E-11 | 1,70,E-09 | 4,82,E-12 |
| AREA | SRC_146 | Cam_Valpo_76-PEAS e Imp | 274323 | 6380578 | 3 mes | 130,55 | 1,77,E-09 | 4,29,E-10 | 9,98,E-10 | 2,00,E-08 | 5,66,E-11 |
| AREA | SRC_147 | Cam_Valpo_77-PEAS e Imp | 274308 | 6380608 | 3 mes | 138,17 | 1,67,E-09 | 4,05,E-10 | 9,43,E-10 | 1,89,E-08 | 5,34,E-11 |
| AREA | SRC_148 | Cam_Valpo_78-PEAS e Imp | 274078 | 6381086 | 3 mes | 2120,50 | 1,09,E-10 | 2,64,E-11 | 6,14,E-11 | 1,23,E-09 | 3,48,E-12 |
| AREA | SRC_149 | Cam_Valpo_79-PEAS e Imp | 274036 | 6381146 | 3 mes | 292,96 | 7,90,E-10 | 1,91,E-10 | 4,45,E-10 | 8,90,E-09 | 2,52,E-11 |
| AREA | SRC_150 | Cam_Valpo_80-PEAS e Imp | 273997 | 6381192 | 3 mes | 242,71 | 9,53,E-10 | 2,31,E-10 | 5,37,E-10 | 1,07,E-08 | 3,04,E-11 |

**Tabla 141.: Fuentes de Emisión - Escenario 5 parte 7**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m]<br>273945 | [m]<br>6381212 | [m]<br>6381212 | [m2]<br>225,25 | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_151 | Cam_Valpo_81-PEAS e Imp | Cam_Valpo_81-PEAS e Imp | Cam_Valpo_81-PEAS e Imp | 3 mes | 3 mes | 1,03,E-09 | 2,49,E-10 | 5,78,E-10 | 1,16,E-08 | 3,28,E-11 |
| AREA | SRC_152 | Cam_Valpo_82-PEAS e Imp | 273863 | 6381235 | 3 mes | 340,59 | 6,79,E-10 | 1,64,E-10 | 3,82,E-10 | 7,65,E-09 | 2,17,E-11 |
| AREA | SRC_153 | Cam_Valpo_83-PEAS e Imp | 273527 | 6381309 | 3 mes | 1376,67 | 1,68,E-10 | 4,07,E-11 | 9,46,E-11 | 1,89,E-09 | 5,36,E-12 |
| AREA | SRC_154 | Cam_Valpo_84-PEAS e Imp | 273488 | 6381317 | 3 mes | 158,83 | 1,46,E-09 | 3,52,E-10 | 8,20,E-10 | 1,64,E-08 | 4,65,E-11 |
| AREA | SRC_155 | Cam_Valpo_85-PEAS e Imp | 273437 | 6381311 | 3 mes | 210,61 | 1,10,E-09 | 2,66,E-10 | 6,18,E-10 | 1,24,E-08 | 3,51,E-11 |
| AREA | SRC_156 | Cam_Valpo_86-PEAS e Imp | 273400 | 6381306 | 3 mes | 148,75 | 1,56,E-09 | 3,76,E-10 | 8,76,E-10 | 1,75,E-08 | 4,96,E-11 |
| AREA | SRC_157 | Cam_Valpo_87-PEAS e Imp | 273330 | 6381278 | 3 mes | 302,02 | 7,66,E-10 | 1,85,E-10 | 4,31,E-10 | 8,63,E-09 | 2,44,E-11 |
| AREA | SRC_158 | Cam_Valpo_88-PEAS e Imp | 273269 | 6381275 | 3 mes | 240,32 | 9,63,E-10 | 2,33,E-10 | 5,42,E-10 | 1,08,E-08 | 3,07,E-11 |
| AREA | SRC_159 | Cam_Valpo_89-PEAS e Imp | 273210 | 6381284 | 3 mes | 238,69 | 9,69,E-10 | 2,35,E-10 | 5,46,E-10 | 1,09,E-08 | 3,09,E-11 |
| AREA | SRC_160 | Cam_Valpo_90-PEAS e Imp | 273140 | 6381307 | 3 mes | 291,89 | 7,93,E-10 | 1,92,E-10 | 4,46,E-10 | 8,93,E-09 | 2,53,E-11 |
| AREA | SRC_161 | Cam_Valpo_91-PEAS e Imp | 273026 | 6381364 | 3 mes | 510,61 | 4,53,E-10 | 1,10,E-10 | 2,55,E-10 | 5,10,E-09 | 1,45,E-11 |
| AREA | SRC_162 | Cam_Valpo_92-PEAS e Imp | 272787 | 6381471 | 3 mes | 1046,47 | 2,21,E-10 | 5,35,E-11 | 1,24,E-10 | 2,49,E-09 | 7,06,E-12 |
| AREA | SRC_163 | Cam_Valpo_93-PEAS e Imp | 272625 | 6381553 | 3 mes | 726,81 | 3,18,E-10 | 7,70,E-11 | 1,79,E-10 | 3,59,E-09 | 1,02,E-11 |
| AREA | SRC_164 | Cam_Valpo_94-PEAS e Imp | 272586 | 6381587 | 3 mes | 205,87 | 1,12,E-09 | 2,72,E-10 | 6,33,E-10 | 1,27,E-08 | 3,59,E-11 |
| AREA | SRC_165 | Cam_Valpo_95-PEAS e Imp | 272567 | 6381621 | 3 mes | 150,25 | 1,54,E-09 | 3,73,E-10 | 8,67,E-10 | 1,73,E-08 | 4,91,E-11 |
| AREA | SRC_166 | Cam_Valpo_96-PEAS e Imp | 272558 | 6381659 | 3 mes | 154,59 | 1,50,E-09 | 3,62,E-10 | 8,43,E-10 | 1,69,E-08 | 4,78,E-11 |
| AREA | SRC_167 | Cam_Valpo_97-PEAS e Imp | 272513 | 6381931 | 3 mes | 1103,20 | 2,10,E-10 | 5,07,E-11 | 1,18,E-10 | 2,36,E-09 | 6,69,E-12 |
| AREA | SRC_168 | Cam_Valpo_98-PEAS e Imp | 272500 | 6382030 | 3 mes | 398,37 | 5,81,E-10 | 1,41,E-10 | 3,27,E-10 | 6,54,E-09 | 1,85,E-11 |
| AREA | SRC_169 | Cam_Valpo_99-PEAS e Imp | 272492 | 6382086 | 3 mes | 223,87 | 1,03,E-09 | 2,50,E-10 | 5,82,E-10 | 1,16,E-08 | 3,30,E-11 |
| AREA | SRC_170 | Cam_Valpo_100-PEAS e Imp | 272491 | 6382127 | 3 mes | 164,32 | 1,41,E-09 | 3,41,E-10 | 7,93,E-10 | 1,59,E-08 | 4,49,E-11 |
| AREA | SRC_171 | Cam_Valpo_101-PEAS e Imp | 272506 | 6382188 | 3 mes | 247,33 | 9,36,E-10 | 2,26,E-10 | 5,27,E-10 | 1,05,E-08 | 2,99,E-11 |
| AREA | SRC_172 | Cam_Valpo_102-PEAS e Imp | 272660 | 6383439 | 3 mes | 5043,31 | 4,59,E-11 | 1,11,E-11 | 2,58,E-11 | 5,17,E-10 | 1,46,E-12 |
| AREA | SRC_173 | Cam_Valpo_103-PEAS e Imp | 272630 | 6384559 | 3 mes | 4478,91 | 5,17,E-11 | 1,25,E-11 | 2,91,E-11 | 5,82,E-10 | 1,65,E-12 |
| AREA | SRC_174 | Cam_Valpo_104-PEAS e Imp | 272626 | 6385227 | 3 mes | 2671,08 | 8,66,E-11 | 2,10,E-11 | 4,88,E-11 | 9,76,E-10 | 2,76,E-12 |
| AREA | SRC_175 | Cam_Valpo_105-PEAS e Imp | 272602 | 6386454 | 3 mes | 4905,80 | 4,72,E-11 | 1,14,E-11 | 2,65,E-11 | 5,31,E-10 | 1,51,E-12 |

**Tabla 142.: Fuentes de Emisión - Escenario 5 parte 8**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m]<br>272609 | [m]<br>6386527 | [m]<br>6386527 | [m2]<br>292,53 | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_176 | Cam_Valpo_106-PEAS e Imp | Cam_Valpo_106-PEAS e Imp | Cam_Valpo_106-PEAS e Imp | 3 mes | 3 mes | 7,91,E-10 | 1,91,E-10 | 4,45,E-10 | 8,91,E-09 | 2,52,E-11 |
| AREA | SRC_177 | Cam_Valpo_107-PEAS e Imp | 272650 | 6386615 | 3 mes | 384,69 | 6,01,E-10 | 1,46,E-10 | 3,39,E-10 | 6,77,E-09 | 1,92,E-11 |
| AREA | SRC_178 | Cam_Valpo_108-PEAS e Imp | 272755 | 6386705 | 3 mes | 550,00 | 4,21,E-10 | 1,02,E-10 | 2,37,E-10 | 4,74,E-09 | 1,34,E-11 |
| AREA | SRC_179 | Cam_Valpo_109-PEAS e Imp | 272846 | 6386776 | 3 mes | 460,85 | 5,02,E-10 | 1,21,E-10 | 2,83,E-10 | 5,66,E-09 | 1,60,E-11 |
| AREA | SRC_180 | Cam_Valpo_110-PEAS e Imp | 272918 | 6386821 | 3 mes | 338,79 | 6,83,E-10 | 1,65,E-10 | 3,84,E-10 | 7,69,E-09 | 2,18,E-11 |
| AREA | SRC_181 | Cam_Valpo_111-PEAS e Imp | 272959 | 6386856 | 3 mes | 215,71 | 1,07,E-09 | 2,60,E-10 | 6,04,E-10 | 1,21,E-08 | 3,42,E-11 |
| AREA | SRC_182 | Cam_Valpo_112-PEAS e Imp | 272979 | 6386909 | 3 mes | 229,32 | 1,01,E-09 | 2,44,E-10 | 5,68,E-10 | 1,14,E-08 | 3,22,E-11 |
| AREA | SRC_183 | Cam_Valpo_113-PEAS e Imp | 272982 | 6386950 | 3 mes | 168,20 | 1,38,E-09 | 3,33,E-10 | 7,74,E-10 | 1,55,E-08 | 4,39,E-11 |
| AREA | SRC_184 | Cam_Valpo_114-PEAS e Imp | 272974 | 6387033 | 3 mes | 334,56 | 6,92,E-10 | 1,67,E-10 | 3,89,E-10 | 7,79,E-09 | 2,21,E-11 |
| AREA | SRC_185 | Cam_Valpo_115-PEAS e Imp | 272969 | 6387289 | 3 mes | 1021,26 | 2,27,E-10 | 5,48,E-11 | 1,28,E-10 | 2,55,E-09 | 7,23,E-12 |
| AREA | SRC_186 | Cam_Valpo_116-PEAS e Imp | 272950 | 6387316 | 3 mes | 135,86 | 1,70,E-09 | 4,12,E-10 | 9,59,E-10 | 1,92,E-08 | 5,43,E-11 |
| AREA | SRC_187 | Cam_Valpo_117-PEAS e Imp | 272918 | 6387332 | 3 mes | 150,62 | 1,54,E-09 | 3,72,E-10 | 8,65,E-10 | 1,73,E-08 | 4,90,E-11 |
| AREA | SRC_188 | Cam_Valpo_118-PEAS e Imp | 272871 | 6387328 | 3 mes | 193,11 | 1,20,E-09 | 2,90,E-10 | 6,74,E-10 | 1,35,E-08 | 3,82,E-11 |
| AREA | SRC_189 | Cam_Valpo_119-PEAS e Imp | 272818 | 6387319 | 3 mes | 214,82 | 1,08,E-09 | 2,61,E-10 | 6,06,E-10 | 1,21,E-08 | 3,44,E-11 |
| AREA | SRC_190 | Cam_Valpo_120-PEAS e Imp | 272669 | 6387324 | 3 mes | 593,51 | 3,90,E-10 | 9,43,E-11 | 2,19,E-10 | 4,39,E-09 | 1,24,E-11 |
| AREA | SRC_191 | Cam_Valpo_121-PEAS e Imp | 272536 | 6387380 | 3 mes | 574,11 | 4,03,E-10 | 9,75,E-11 | 2,27,E-10 | 4,54,E-09 | 1,29,E-11 |
| AREA | SRC_192 | Cam_Valpo_122-PEAS e Imp | 272406 | 6387475 | 3 mes | 642,85 | 3,60,E-10 | 8,71,E-11 | 2,03,E-10 | 4,05,E-09 | 1,15,E-11 |
| AREA | SRC_193 | Cam_Valpo_123-PEAS e Imp | 272321 | 6387544 | 3 mes | 438,86 | 5,27,E-10 | 1,28,E-10 | 2,97,E-10 | 5,94,E-09 | 1,68,E-11 |
| AREA | SRC_194 | Cam_Valpo_124-PEAS e Imp | 272252 | 6387605 | 3 mes | 366,01 | 6,32,E-10 | 1,53,E-10 | 3,56,E-10 | 7,12,E-09 | 2,02,E-11 |
| AREA | SRC_195 | Cam_Valpo_125-PEAS e Imp | 272138 | 6387749 | 3 mes | 733,97 | 3,15,E-10 | 7,63,E-11 | 1,77,E-10 | 3,55,E-09 | 1,01,E-11 |
| AREA | SRC_196 | Cam_Valpo_126-PEAS e Imp | 272059 | 6387890 | 3 mes | 645,70 | 3,58,E-10 | 8,67,E-11 | 2,02,E-10 | 4,04,E-09 | 1,14,E-11 |
| AREA | SRC_197 | Cam_Valpo_127-PEAS e Imp | 272019 | 6388008 | 3 mes | 494,29 | 4,68,E-10 | 1,13,E-10 | 2,63,E-10 | 5,27,E-09 | 1,49,E-11 |
| AREA | SRC_198 | Cam_Valpo_128-PEAS e Imp | 272005 | 6388086 | 3 mes | 318,17 | 7,27,E-10 | 1,76,E-10 | 4,09,E-10 | 8,19,E-09 | 2,32,E-11 |
| AREA | SRC_199 | Cam_Valpo_129-PEAS e Imp | 272005 | 6388171 | 3 mes | 338,40 | 6,84,E-10 | 1,65,E-10 | 3,85,E-10 | 7,70,E-09 | 2,18,E-11 |
| AREA | SRC_200 | Cam_Valpo_130-PEAS e Imp | 272018 | 6388207 | 3 mes | 149,40 | 1,55,E-09 | 3,75,E-10 | 8,72,E-10 | 1,74,E-08 | 4,94,E-11 |

**Tabla 143.: Fuentes de Emisión - Escenario 5 parte 9**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m]<br>272053 | [m]<br>6388222 | [m]<br>6388222 | [m2]<br>144,57 | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_201 | Cam_Valpo_131-PEAS e Imp | Cam_Valpo_131-PEAS e Imp | Cam_Valpo_131-PEAS e Imp | 3 mes | 3 mes | 1,60,E-09 | 3,87,E-10 | 9,01,E-10 | 1,80,E-08 | 5,11,E-11 |
| AREA | SRC_202 | Cam_Valpo_132-PEAS e Imp | 272113 | 6388260 | 3 mes | 286,19 | 8,09,E-10 | 1,96,E-10 | 4,55,E-10 | 9,11,E-09 | 2,58,E-11 |
| AREA | SRC_203 | Cam_Valpo_133-PEAS e Imp | 272165 | 6388289 | 3 mes | 236,50 | 9,78,E-10 | 2,37,E-10 | 5,51,E-10 | 1,10,E-08 | 3,12,E-11 |
| AREA | SRC_204 | Cam_Valpo_134-PEAS e Imp | 272170 | 6388313 | 3 mes | 103,04 | 2,25,E-09 | 5,43,E-10 | 1,26,E-09 | 2,53,E-08 | 7,17,E-11 |
| AREA | SRC_205 | Cam_Valpo_135-PEAS e Imp | 272160 | 6388355 | 3 mes | 178,67 | 1,30,E-09 | 3,13,E-10 | 7,29,E-10 | 1,46,E-08 | 4,13,E-11 |
| AREA | SRC_206 | Cam_Valpo_136-PEAS e Imp | 272116 | 6388384 | 3 mes | 213,17 | 1,09,E-09 | 2,63,E-10 | 6,11,E-10 | 1,22,E-08 | 3,46,E-11 |
| AREA | SRC_207 | Cam_Valpo_137-PEAS e Imp | 271990 | 6388473 | 3 mes | 618,26 | 3,74,E-10 | 9,05,E-11 | 2,11,E-10 | 4,22,E-09 | 1,19,E-11 |
| AREA | SRC_208 | Cam_Valpo_138-PEAS e Imp | 271909 | 6388570 | 3 mes | 502,24 | 4,61,E-10 | 1,11,E-10 | 2,59,E-10 | 5,19,E-09 | 1,47,E-11 |
| AREA | SRC_209 | Cam_Valpo_139-PEAS e Imp | 271887 | 6388631 | 3 mes | 257,67 | 8,98,E-10 | 2,17,E-10 | 5,05,E-10 | 1,01,E-08 | 2,87,E-11 |
| AREA | SRC_210 | Cam_Valpo_140-PEAS e Imp | 271869 | 6388710 | 3 mes | 324,57 | 7,13,E-10 | 1,72,E-10 | 4,01,E-10 | 8,03,E-09 | 2,27,E-11 |
| AREA | SRC_211 | Cam_Valpo_141-PEAS e Imp | 271879 | 6388778 | 3 mes | 270,72 | 8,55,E-10 | 2,07,E-10 | 4,81,E-10 | 9,63,E-09 | 2,73,E-11 |
| AREA | SRC_212 | Cam_Valpo_142-PEAS e Imp | 271889 | 6388831 | 3 mes | 215,81 | 1,07,E-09 | 2,59,E-10 | 6,04,E-10 | 1,21,E-08 | 3,42,E-11 |
| AREA | SRC_213 | Cam_Valpo_143-PEAS e Imp | 271888 | 6388910 | 3 mes | 317,54 | 7,29,E-10 | 1,76,E-10 | 4,10,E-10 | 8,21,E-09 | 2,33,E-11 |
| AREA | SRC_214 | Cam_Valpo_144-PEAS e Imp | 271765 | 6389249 | 3 mes | 1443,83 | 1,60,E-10 | 3,88,E-11 | 9,02,E-11 | 1,81,E-09 | 5,11,E-12 |
| AREA | SRC_215 | Cam_Valpo_145-PEAS e Imp | 271745 | 6389323 | 3 mes | 308,68 | 7,50,E-10 | 1,81,E-10 | 4,22,E-10 | 8,44,E-09 | 2,39,E-11 |
| AREA | SRC_216 | Cam_Valpo_146-PEAS e Imp | 271746 | 6389404 | 3 mes | 321,13 | 7,21,E-10 | 1,74,E-10 | 4,06,E-10 | 8,12,E-09 | 2,30,E-11 |
| AREA | SRC_217 | Cam_Valpo_147-PEAS e Imp | 271745 | 6389713 | 3 mes | 1235,33 | 1,87,E-10 | 4,53,E-11 | 1,05,E-10 | 2,11,E-09 | 5,98,E-12 |
| AREA | SRC_218 | Cam_Valpo_148-PEAS e Imp | 271729 | 6389779 | 3 mes | 274,74 | 8,42,E-10 | 2,04,E-10 | 4,74,E-10 | 9,49,E-09 | 2,69,E-11 |
| AREA | SRC_219 | Cam_Valpo_149-PEAS e Imp | 271405 | 6390771 | 3 mes | 4169,69 | 5,55,E-11 | 1,34,E-11 | 3,12,E-11 | 6,25,E-10 | 1,77,E-12 |
| AREA | SRC_220 | Cam_Valpo_150-PEAS e Imp | 271408 | 6390852 | 3 mes | 324,07 | 7,14,E-10 | 1,73,E-10 | 4,02,E-10 | 8,04,E-09 | 2,28,E-11 |
| AREA | SRC_221 | Cam_Valpo_151-PEAS e Imp | 271425 | 6390918 | 3 mes | 269,76 | 8,58,E-10 | 2,08,E-10 | 4,83,E-10 | 9,66,E-09 | 2,74,E-11 |
| AREA | SRC_222 | Cam_Valpo_152-PEAS e Imp | 271595 | 6391444 | 3 mes | 2210,20 | 1,05,E-10 | 2,53,E-11 | 5,89,E-11 | 1,18,E-09 | 3,34,E-12 |
| AREA | SRC_223 | Cam_Valpo_153-PEAS e Imp | 271601 | 6391518 | 3 mes | 297,07 | 7,79,E-10 | 1,88,E-10 | 4,38,E-10 | 8,77,E-09 | 2,49,E-11 |
| AREA | SRC_224 | Cam_Valpo_154-PEAS e Imp | 271583 | 6391599 | 3 mes | 334,56 | 6,92,E-10 | 1,67,E-10 | 3,89,E-10 | 7,79,E-09 | 2,21,E-11 |
| AREA | SRC_225 | Cam_Valpo_155-PEAS e Imp | 271490 | 6391665 | 3 mes | 462,29 | 5,01,E-10 | 1,21,E-10 | 2,82,E-10 | 5,64,E-09 | 1,60,E-11 |

**Tabla 144.: Fuentes de Emisión - Escenario 5 parte 10**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m]<br>271388 | [m]<br>6391779 | [m]<br>6391779 | [m2]<br>610,49 | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_226 | Cam_Valpo_156-PEAS e Imp | Cam_Valpo_156-PEAS e Imp | Cam_Valpo_156-PEAS e Imp | 3 mes | 3 mes | 3,79,E-10 | 9,17,E-11 | 2,13,E-10 | 4,27,E-09 | 1,21,E-11 |
| AREA | SRC_227 | Cam_Valpo_157-PEAS e Imp | 271303 | 6391969 | 3 mes | 829,95 | 2,79,E-10 | 6,75,E-11 | 1,57,E-10 | 3,14,E-09 | 8,90,E-12 |
| AREA | SRC_228 | Cam_Valpo_158-PEAS e Imp | 271249 | 6392048 | 3 mes | 385,48 | 6,00,E-10 | 1,45,E-10 | 3,38,E-10 | 6,76,E-09 | 1,92,E-11 |
| AREA | SRC_229 | Cam_Valpo_159-PEAS e Imp | 271095 | 6392199 | 3 mes | 863,11 | 2,68,E-10 | 6,49,E-11 | 1,51,E-10 | 3,02,E-09 | 8,55,E-12 |
| AREA | SRC_230 | Cam_Valpo_160-PEAS e Imp | 271003 | 6392357 | 3 mes | 727,41 | 3,18,E-10 | 7,70,E-11 | 1,79,E-10 | 3,58,E-09 | 1,02,E-11 |
| AREA | SRC_231 | Cam_Valpo_161-PEAS e Imp | 270864 | 6392618 | 3 mes | 1181,67 | 1,96,E-10 | 4,74,E-11 | 1,10,E-10 | 2,21,E-09 | 6,25,E-12 |
| AREA | SRC_232 | Cam_Valpo_162-PEAS e Imp | 270665 | 6392901 | 3 mes | 1386,67 | 1,67,E-10 | 4,04,E-11 | 9,39,E-11 | 1,88,E-09 | 5,32,E-12 |
| AREA | SRC_233 | Cam_Valpo_163-PEAS e Imp | 270570 | 6393060 | 3 mes | 739,81 | 3,13,E-10 | 7,57,E-11 | 1,76,E-10 | 3,52,E-09 | 9,98,E-12 |
| AREA | SRC_234 | Cam_Valpo_164-PEAS e Imp | 270535 | 6393162 | 3 mes | 427,94 | 5,41,E-10 | 1,31,E-10 | 3,04,E-10 | 6,09,E-09 | 1,73,E-11 |
| AREA | SRC_235 | Cam_Valpo_165-PEAS e Imp | 270408 | 6393157 | 3 mes | 516,16 | 4,48,E-10 | 1,08,E-10 | 2,52,E-10 | 5,05,E-09 | 1,43,E-11 |
| AREA | SRC_236 | Cam_Valpo_166-PEAS e Imp | 270322 | 6393156 | 3 mes | 344,11 | 6,72,E-10 | 1,63,E-10 | 3,78,E-10 | 7,57,E-09 | 2,15,E-11 |
| AREA | SRC_237 | Cam_Valpo_167-PEAS e Imp | 270198 | 6393225 | 3 mes | 562,03 | 4,12,E-10 | 9,96,E-11 | 2,32,E-10 | 4,64,E-09 | 1,31,E-11 |
| AREA | SRC_238 | Cam_Valpo_168-PEAS e Imp | 270084 | 6393222 | 3 mes | 461,57 | 5,01,E-10 | 1,21,E-10 | 2,82,E-10 | 5,65,E-09 | 1,60,E-11 |
| AREA | SRC_239 | Cam_Valpo_169-PEAS e Imp | 270014 | 6393114 | 3 mes | 520,05 | 4,45,E-10 | 1,08,E-10 | 2,50,E-10 | 5,01,E-09 | 1,42,E-11 |
| AREA | SRC_240 | Cam_Valpo_170-PEAS e Imp | 269944 | 6393026 | 3 mes | 448,19 | 5,16,E-10 | 1,25,E-10 | 2,91,E-10 | 5,81,E-09 | 1,65,E-11 |
| AREA | SRC_241 | Cam_Valpo_171-PEAS e Imp | 269831 | 6392981 | 3 mes | 484,35 | 4,78,E-10 | 1,16,E-10 | 2,69,E-10 | 5,38,E-09 | 1,52,E-11 |
| AREA | SRC_242 | Cam_Valpo_172-PEAS e Imp | 269702 | 6392966 | 3 mes | 516,99 | 4,48,E-10 | 1,08,E-10 | 2,52,E-10 | 5,04,E-09 | 1,43,E-11 |
| AREA | SRC_243 | Cam_Valpo_173-PEAS e Imp | 269506 | 6393084 | 3 mes | 906,73 | 2,55,E-10 | 6,17,E-11 | 1,44,E-10 | 2,87,E-09 | 8,14,E-12 |
| AREA | SRC_244 | Cam_Valpo_174-PEAS e Imp | 269407 | 6393106 | 3 mes | 410,62 | 5,64,E-10 | 1,36,E-10 | 3,17,E-10 | 6,35,E-09 | 1,80,E-11 |
| AREA | SRC_245 | Cam_Valpo_175-PEAS e Imp | 269355 | 6393219 | 3 mes | 493,13 | 4,69,E-10 | 1,14,E-10 | 2,64,E-10 | 5,28,E-09 | 1,50,E-11 |
| AREA | SRC_246 | Cam_Valpo_176-PEAS e Imp | 269450 | 6393436 | 3 mes | 939,57 | 2,46,E-10 | 5,96,E-11 | 1,39,E-10 | 2,77,E-09 | 7,86,E-12 |
| AREA | SRC_247 | Cam_Valpo_177-PEAS e Imp | 269537 | 6393768 | 3 mes | 1375,49 | 1,68,E-10 | 4,07,E-11 | 9,47,E-11 | 1,89,E-09 | 5,37,E-12 |
| AREA | SRC_248 | Cam_Valpo_178-PEAS e Imp | 269541 | 6393876 | 3 mes | 433,16 | 5,34,E-10 | 1,29,E-10 | 3,01,E-10 | 6,02,E-09 | 1,70,E-11 |
| AREA | SRC_249 | Cam_Valpo_179-PEAS e Imp | 269514 | 6393952 | 3 mes | 327,49 | 7,07,E-10 | 1,71,E-10 | 3,98,E-10 | 7,96,E-09 | 2,25,E-11 |
| AREA | SRC_250 | Cam_Valpo_180-PEAS e Imp | 269461 | 6394006 | 3 mes | 302,03 | 7,66,E-10 | 1,85,E-10 | 4,31,E-10 | 8,63,E-09 | 2,44,E-11 |

**Tabla 145.: Fuentes de Emisión - Escenario 5 parte 11**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m]<br>269456 | [m]<br>6394087 | [m]<br>6394087 | [m2]<br>317,54 | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_251 | Cam_Valpo_181-PEAS e Imp | Cam_Valpo_181-PEAS e Imp | Cam_Valpo_181-PEAS e Imp | 3 mes | 3 mes | 7,29,E-10 | 1,76,E-10 | 4,10,E-10 | 8,21,E-09 | 2,33,E-11 |
| AREA | SRC_252 | Cam_Valpo_182-PEAS e Imp | 269494 | 6394169 | 3 mes | 358,94 | 6,45,E-10 | 1,56,E-10 | 3,63,E-10 | 7,26,E-09 | 2,06,E-11 |
| AREA | SRC_253 | Cam_Valpo_183-PEAS e Imp | 269580 | 6394296 | 3 mes | 611,99 | 3,78,E-10 | 9,15,E-11 | 2,13,E-10 | 4,26,E-09 | 1,21,E-11 |
| AREA | SRC_254 | Cam_Valpo_184-PEAS e Imp | 269614 | 6394394 | 3 mes | 416,61 | 5,55,E-10 | 1,34,E-10 | 3,13,E-10 | 6,26,E-09 | 1,77,E-11 |
| AREA | SRC_255 | Cam_Valpo_185-PEAS e Imp | 269617 | 6394492 | 3 mes | 396,57 | 5,83,E-10 | 1,41,E-10 | 3,28,E-10 | 6,57,E-09 | 1,86,E-11 |
| AREA | SRC_256 | Cam_Valpo_186-PEAS e Imp | 269532 | 6394634 | 3 mes | 664,18 | 3,48,E-10 | 8,43,E-11 | 1,96,E-10 | 3,92,E-09 | 1,11,E-11 |
| AREA | SRC_257 | Cam_Valpo_187-PEAS e Imp | 269478 | 6394752 | 3 mes | 518,20 | 4,47,E-10 | 1,08,E-10 | 2,51,E-10 | 5,03,E-09 | 1,42,E-11 |
| AREA | SRC_258 | Cam_Valpo_188-PEAS e Imp | 269437 | 6394881 | 3 mes | 540,93 | 4,28,E-10 | 1,03,E-10 | 2,41,E-10 | 4,82,E-09 | 1,36,E-11 |
| AREA | SRC_259 | Cam_Valpo_189-PEAS e Imp | 269448 | 6395002 | 3 mes | 483,46 | 4,79,E-10 | 1,16,E-10 | 2,69,E-10 | 5,39,E-09 | 1,53,E-11 |
| AREA | SRC_260 | Cam_Valpo_190-PEAS e Imp | 269465 | 6395049 | 3 mes | 197,82 | 1,17,E-09 | 2,83,E-10 | 6,58,E-10 | 1,32,E-08 | 3,73,E-11 |
| AREA | SRC_261 | Cam_Valpo_191-PEAS e Imp | 269701 | 6395188 | 3 mes | 1088,66 | 2,13,E-10 | 5,14,E-11 | 1,20,E-10 | 2,39,E-09 | 6,78,E-12 |
| AREA | SRC_262 | Cam_Valpo_192-PEAS e Imp | 269737 | 6395244 | 3 mes | 269,38 | 8,59,E-10 | 2,08,E-10 | 4,84,E-10 | 9,67,E-09 | 2,74,E-11 |
| AREA | SRC_263 | Cam_Valpo_193-PEAS e Imp | 269748 | 6395318 | 3 mes | 301,88 | 7,66,E-10 | 1,85,E-10 | 4,31,E-10 | 8,63,E-09 | 2,45,E-11 |
| AREA | SRC_264 | Cam_Valpo_194-PEAS e Imp | 269734 | 6395473 | 3 mes | 624,02 | 3,71,E-10 | 8,97,E-11 | 2,09,E-10 | 4,18,E-09 | 1,18,E-11 |
| AREA | SRC_265 | Cam_Valpo_195-PEAS e Imp | 269791 | 6395575 | 3 mes | 462,91 | 5,00,E-10 | 1,21,E-10 | 2,81,E-10 | 5,63,E-09 | 1,60,E-11 |
| AREA | SRC_266 | Cam_Valpo_196-PEAS e Imp | 269918 | 6395634 | 3 mes | 557,57 | 4,15,E-10 | 1,00,E-10 | 2,34,E-10 | 4,67,E-09 | 1,32,E-11 |
| AREA | SRC_267 | Cam_Valpo_197-PEAS e Imp | 269951 | 6395703 | 3 mes | 311,66 | 7,42,E-10 | 1,80,E-10 | 4,18,E-10 | 8,36,E-09 | 2,37,E-11 |
| AREA | SRC_268 | Cam_Valpo_198-PEAS e Imp | 269926 | 6395767 | 3 mes | 277,87 | 8,33,E-10 | 2,01,E-10 | 4,69,E-10 | 9,38,E-09 | 2,66,E-11 |
| AREA | SRC_269 | Cam_Valpo_199-PEAS e Imp | 269853 | 6395812 | 3 mes | 348,28 | 6,64,E-10 | 1,61,E-10 | 3,74,E-10 | 7,48,E-09 | 2,12,E-11 |
| AREA | SRC_270 | Cam_Valpo_200-PEAS e Imp | 269732 | 6395847 | 3 mes | 504,67 | 4,58,E-10 | 1,11,E-10 | 2,58,E-10 | 5,16,E-09 | 1,46,E-11 |
| AREA | SRC_271 | Cam_Valpo_201-PEAS e Imp | 269688 | 6395928 | 3 mes | 365,46 | 6,33,E-10 | 1,53,E-10 | 3,56,E-10 | 7,13,E-09 | 2,02,E-11 |
| AREA | SRC_272 | Cam_Valpo_202-PEAS e Imp | 269717 | 6396047 | 3 mes | 484,68 | 4,77,E-10 | 1,16,E-10 | 2,69,E-10 | 5,38,E-09 | 1,52,E-11 |
| AREA | SRC_273 | Cam_Valpo_203-PEAS e Imp | 269712 | 6396106 | 3 mes | 237,49 | 9,74,E-10 | 2,36,E-10 | 5,48,E-10 | 1,10,E-08 | 3,11,E-11 |
| AREA | SRC_274 | Cam_Valpo_204-PEAS e Imp | 269657 | 6396143 | 3 mes | 271,48 | 8,52,E-10 | 2,06,E-10 | 4,80,E-10 | 9,60,E-09 | 2,72,E-11 |
| AREA | SRC_275 | Cam_Valpo_205-PEAS e Imp | 269580 | 6396120 | 3 mes | 326,46 | 7,09,E-10 | 1,71,E-10 | 3,99,E-10 | 7,98,E-09 | 2,26,E-11 |

**Tabla 146.: Fuentes de Emisión - Escenario 5 parte 12**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m]<br>269501 | [m]<br>6396070 | [m]<br>6396070 | [m2]<br>376,20 | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_276 | Cam_Valpo_206-PEAS e Imp | Cam_Valpo_206-PEAS e Imp | Cam_Valpo_206-PEAS e Imp | 3 mes | 3 mes | 6,15,E-10 | 1,49,E-10 | 3,46,E-10 | 6,93,E-09 | 1,96,E-11 |
| AREA | SRC_277 | Cam_Valpo_207-PEAS e Imp | 269359 | 6396026 | 3 mes | 593,54 | 3,90,E-10 | 9,43,E-11 | 2,19,E-10 | 4,39,E-09 | 1,24,E-11 |
| AREA | SRC_278 | Cam_Valpo_208-PEAS e Imp | 269272 | 6396023 | 3 mes | 343,48 | 6,74,E-10 | 1,63,E-10 | 3,79,E-10 | 7,59,E-09 | 2,15,E-11 |
| AREA | SRC_279 | Cam_Valpo_209-PEAS e Imp | 269222 | 6396073 | 3 mes | 275,81 | 8,39,E-10 | 2,03,E-10 | 4,72,E-10 | 9,45,E-09 | 2,68,E-11 |
| AREA | SRC_280 | Cam_Valpo_210-PEAS e Imp | 269210 | 6396185 | 3 mes | 446,25 | 5,19,E-10 | 1,25,E-10 | 2,92,E-10 | 5,84,E-09 | 1,65,E-11 |
| AREA | SRC_281 | Cam_Valpo_211-PEAS e Imp | 269167 | 6396232 | 3 mes | 255,46 | 9,06,E-10 | 2,19,E-10 | 5,10,E-10 | 1,02,E-08 | 2,89,E-11 |
| AREA | SRC_282 | Cam_Valpo_212-PEAS e Imp | 269082 | 6396226 | 3 mes | 349,58 | 6,62,E-10 | 1,60,E-10 | 3,73,E-10 | 7,46,E-09 | 2,11,E-11 |
| AREA | SRC_283 | Cam_Valpo_213-PEAS e Imp | 268998 | 6396240 | 3 mes | 335,54 | 6,90,E-10 | 1,67,E-10 | 3,88,E-10 | 7,77,E-09 | 2,20,E-11 |
| AREA | SRC_284 | Cam_Valpo_214-PEAS e Imp | 268894 | 6396300 | 3 mes | 480,09 | 4,82,E-10 | 1,17,E-10 | 2,71,E-10 | 5,43,E-09 | 1,54,E-11 |
| AREA | SRC_285 | Cam_Valpo_215-PEAS e Imp | 268805 | 6396381 | 3 mes | 477,49 | 4,85,E-10 | 1,17,E-10 | 2,73,E-10 | 5,46,E-09 | 1,55,E-11 |
| AREA | SRC_286 | Cam_Valpo_216-PEAS e Imp | 268734 | 6396481 | 3 mes | 489,34 | 4,73,E-10 | 1,14,E-10 | 2,66,E-10 | 5,33,E-09 | 1,51,E-11 |
| AREA | SRC_287 | Cam_Valpo_217-PEAS e Imp | 268692 | 6396569 | 3 mes | 388,32 | 5,96,E-10 | 1,44,E-10 | 3,35,E-10 | 6,71,E-09 | 1,90,E-11 |
| AREA | SRC_288 | Cam_Valpo_218-PEAS e Imp | 268614 | 6396686 | 3 mes | 563,68 | 4,10,E-10 | 9,93,E-11 | 2,31,E-10 | 4,62,E-09 | 1,31,E-11 |
| AREA | SRC_289 | Cam_Valpo_219-PEAS e Imp | 268551 | 6396751 | 3 mes | 365,13 | 6,34,E-10 | 1,53,E-10 | 3,57,E-10 | 7,14,E-09 | 2,02,E-11 |
| AREA | SRC_290 | Cam_Valpo_220-PEAS e Imp | 268525 | 6396834 | 3 mes | 342,75 | 6,75,E-10 | 1,63,E-10 | 3,80,E-10 | 7,60,E-09 | 2,15,E-11 |
| AREA | SRC_291 | Cam_Valpo_221-PEAS e Imp | 268521 | 6396918 | 3 mes | 335,20 | 6,90,E-10 | 1,67,E-10 | 3,89,E-10 | 7,78,E-09 | 2,20,E-11 |
| AREA | SRC_292 | Cam_Valpo_222-PEAS e Imp | 268510 | 6396996 | 3 mes | 312,17 | 7,41,E-10 | 1,79,E-10 | 4,17,E-10 | 8,35,E-09 | 2,37,E-11 |
| AREA | SRC_293 | Cam_Valpo_223-PEAS e Imp | 268441 | 6397095 | 3 mes | 486,78 | 4,75,E-10 | 1,15,E-10 | 2,68,E-10 | 5,35,E-09 | 1,52,E-11 |
| AREA | SRC_294 | Cam_Valpo_224-PEAS e Imp | 268352 | 6397195 | 3 mes | 537,81 | 4,30,E-10 | 1,04,E-10 | 2,42,E-10 | 4,85,E-09 | 1,37,E-11 |
| AREA | SRC_295 | Cam_Valpo_225-PEAS e Imp | 268295 | 6397296 | 3 mes | 460,41 | 5,03,E-10 | 1,22,E-10 | 2,83,E-10 | 5,66,E-09 | 1,60,E-11 |
| AREA | SRC_296 | Cam_Valpo_226-PEAS e Imp | 268265 | 6397370 | 3 mes | 319,00 | 7,25,E-10 | 1,75,E-10 | 4,08,E-10 | 8,17,E-09 | 2,31,E-11 |
| AREA | SRC_297 | Cam_Valpo_227-PEAS e Imp | 268236 | 6397470 | 3 mes | 414,51 | 5,58,E-10 | 1,35,E-10 | 3,14,E-10 | 6,29,E-09 | 1,78,E-11 |
| AREA | SRC_298 | Cam_Valpo_228-PEAS e Imp | 268225 | 6397539 | 3 mes | 278,02 | 8,32,E-10 | 2,01,E-10 | 4,68,E-10 | 9,37,E-09 | 2,66,E-11 |
| AREA | SRC_299 | Cam_Valpo_229-PEAS e Imp | 268212 | 6397650 | 3 mes | 446,47 | 5,18,E-10 | 1,25,E-10 | 2,92,E-10 | 5,84,E-09 | 1,65,E-11 |
| AREA | SRC_300 | Cam_Valpo_230-PEAS e Imp | 268292 | 6397691 | 3 mes | 352,90 | 6,56,E-10 | 1,59,E-10 | 3,69,E-10 | 7,38,E-09 | 2,09,E-11 |

**Tabla 147.: Fuentes de Emisión - Escenario 5 parte 13**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m]<br>268324 | [m]<br>6397741 | [m]<br>6397741 | [m2]<br>244,09 | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_301 | Cam_Valpo_231-PEAS e Imp | Cam_Valpo_231-PEAS e Imp | Cam_Valpo_231-PEAS e Imp | 3 mes | 3 mes | 9,48,E-10 | 2,29,E-10 | 5,34,E-10 | 1,07,E-08 | 3,02,E-11 |
| AREA | SRC_302 | Cam_Valpo_232-PEAS e Imp | 268344 | 6397809 | 3 mes | 284,52 | 8,13,E-10 | 1,97,E-10 | 4,58,E-10 | 9,16,E-09 | 2,60,E-11 |
| AREA | SRC_303 | Cam_Valpo_233-PEAS e Imp | 268317 | 6397871 | 3 mes | 277,40 | 8,34,E-10 | 2,02,E-10 | 4,70,E-10 | 9,39,E-09 | 2,66,E-11 |
| AREA | SRC_304 | Cam_Valpo_234-PEAS e Imp | 268289 | 6397931 | 3 mes | 263,44 | 8,78,E-10 | 2,12,E-10 | 4,94,E-10 | 9,89,E-09 | 2,80,E-11 |
| AREA | SRC_305 | Cam_Valpo_235-PEAS e Imp | 268281 | 6397993 | 3 mes | 246,21 | 9,40,E-10 | 2,27,E-10 | 5,29,E-10 | 1,06,E-08 | 3,00,E-11 |
| AREA | SRC_306 | Cam_Valpo_236-PEAS e Imp | 268325 | 6398057 | 3 mes | 307,11 | 7,53,E-10 | 1,82,E-10 | 4,24,E-10 | 8,49,E-09 | 2,40,E-11 |
| AREA | SRC_307 | Cam_Valpo_237-PEAS e Imp | 268339 | 6398092 | 3 mes | 154,12 | 1,50,E-09 | 3,63,E-10 | 8,45,E-10 | 1,69,E-08 | 4,79,E-11 |
| AREA | SRC_308 | Cam_Valpo_238-PEAS e Imp | 268362 | 6398151 | 3 mes | 251,56 | 9,20,E-10 | 2,23,E-10 | 5,18,E-10 | 1,04,E-08 | 2,94,E-11 |
| AREA | SRC_309 | Cam_Valpo_239-PEAS e Imp | 268383 | 6398192 | 3 mes | 185,19 | 1,25,E-09 | 3,02,E-10 | 7,03,E-10 | 1,41,E-08 | 3,99,E-11 |
| AREA | SRC_310 | Cam_Valpo_240-PEAS e Imp | 268355 | 6398247 | 3 mes | 250,18 | 9,25,E-10 | 2,24,E-10 | 5,21,E-10 | 1,04,E-08 | 2,95,E-11 |
| AREA | SRC_311 | Cam_Valpo_241-PEAS e Imp | 268227 | 6398303 | 3 mes | 566,84 | 4,08,E-10 | 9,88,E-11 | 2,30,E-10 | 4,60,E-09 | 1,30,E-11 |
| AREA | SRC_312 | Cam_Valpo_242-PEAS e Imp | 268140 | 6398362 | 3 mes | 418,83 | 5,52,E-10 | 1,34,E-10 | 3,11,E-10 | 6,22,E-09 | 1,76,E-11 |
| AREA | SRC_313 | Cam_Valpo_243-PEAS e Imp | 268089 | 6398427 | 3 mes | 325,43 | 7,11,E-10 | 1,72,E-10 | 4,00,E-10 | 8,01,E-09 | 2,27,E-11 |
| AREA | SRC_314 | Cam_Valpo_244-PEAS e Imp | 268005 | 6398483 | 3 mes | 406,15 | 5,70,E-10 | 1,38,E-10 | 3,21,E-10 | 6,42,E-09 | 1,82,E-11 |
| AREA | SRC_315 | Cam_Valpo_245-PEAS e Imp | 267956 | 6398553 | 3 mes | 338,26 | 6,84,E-10 | 1,65,E-10 | 3,85,E-10 | 7,70,E-09 | 2,18,E-11 |
| AREA | SRC_316 | Cam_Valpo_246-PEAS e Imp | 267920 | 6398673 | 3 mes | 498,96 | 4,64,E-10 | 1,12,E-10 | 2,61,E-10 | 5,22,E-09 | 1,48,E-11 |
| AREA | SRC_317 | Cam_Valpo_247-PEAS e Imp | 267908 | 6398749 | 3 mes | 308,37 | 7,50,E-10 | 1,82,E-10 | 4,22,E-10 | 8,45,E-09 | 2,39,E-11 |
| AREA | SRC_318 | Cam_Valpo_248-PEAS e Imp | 267894 | 6398771 | 3 mes | 107,41 | 2,15,E-09 | 5,21,E-10 | 1,21,E-09 | 2,43,E-08 | 6,87,E-11 |
| AREA | SRC_319 | Cam_Valpo_249-PEAS e Imp | 267791 | 6398823 | 3 mes | 466,56 | 4,96,E-10 | 1,20,E-10 | 2,79,E-10 | 5,59,E-09 | 1,58,E-11 |
| AREA | SRC_320 | Cam_Valpo_250-PEAS e Imp | 267747 | 6398849 | 3 mes | 204,00 | 1,13,E-09 | 2,74,E-10 | 6,38,E-10 | 1,28,E-08 | 3,62,E-11 |
| AREA | SRC_321 | Cam_Valpo_251-PEAS e Imp | 267699 | 6398875 | 3 mes | 217,15 | 1,07,E-09 | 2,58,E-10 | 6,00,E-10 | 1,20,E-08 | 3,40,E-11 |
| AREA | SRC_322 | Cam_Valpo_252-PEAS e Imp | 267673 | 6398943 | 3 mes | 285,91 | 8,09,E-10 | 1,96,E-10 | 4,56,E-10 | 9,12,E-09 | 2,58,E-11 |
| AREA | SRC_323 | Cam_Valpo_253-PEAS e Imp | 267740 | 6399152 | 3 mes | 871,99 | 2,65,E-10 | 6,42,E-11 | 1,49,E-10 | 2,99,E-09 | 8,47,E-12 |
| AREA | SRC_324 | Cam_Valpo_254-PEAS e Imp | 267754 | 6399259 | 3 mes | 434,37 | 5,33,E-10 | 1,29,E-10 | 3,00,E-10 | 6,00,E-09 | 1,70,E-11 |
| AREA | SRC_325 | Cam_Valpo_255-PEAS e Imp | 267756 | 6399372 | 3 mes | 452,93 | 5,11,E-10 | 1,24,E-10 | 2,88,E-10 | 5,75,E-09 | 1,63,E-11 |

**Tabla 148.: Fuentes de Emisión - Escenario 5 parte 14**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m]<br>267702 | [m]<br>6399478 | [m]<br>6399478 | [m2]<br>480,03 | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] | [g/m2s] |
| AREA | SRC_326 | Cam_Valpo_256-PEAS e Imp | Cam_Valpo_256-PEAS e Imp | Cam_Valpo_256-PEAS e Imp | 3 mes | 3 mes | 4,82,E-10 | 1,17,E-10 | 2,71,E-10 | 5,43,E-09 | 1,54,E-11 |
| AREA | SRC_327 | Cam_Valpo_257-PEAS e Imp | 267740 | 6399547 | 3 mes | 307,21 | 7,53,E-10 | 1,82,E-10 | 4,24,E-10 | 8,48,E-09 | 2,40,E-11 |
| AREA | SRC_328 | Cam_Valpo_258-PEAS e Imp | 267742 | 6399624 | 3 mes | 311,56 | 7,43,E-10 | 1,80,E-10 | 4,18,E-10 | 8,36,E-09 | 2,37,E-11 |
| AREA | SRC_329 | Cam_Valpo_259-PEAS e Imp | 267731 | 6399695 | 3 mes | 287,58 | 8,05,E-10 | 1,95,E-10 | 4,53,E-10 | 9,06,E-09 | 2,57,E-11 |
| AREA | SRC_330 | Cam_Valpo_260-PEAS e Imp | 267682 | 6399788 | 3 mes | 425,70 | 5,44,E-10 | 1,32,E-10 | 3,06,E-10 | 6,12,E-09 | 1,73,E-11 |
| AREA | SRC_331 | Cam_Valpo_261-PEAS e Imp | 267661 | 6399830 | 3 mes | 187,04 | 1,24,E-09 | 2,99,E-10 | 6,96,E-10 | 1,39,E-08 | 3,95,E-11 |

**Tabla 149.: Fuentes de Emisión - Escenario 5 parte 15**

| Tipo | ID | Descripción | X1 | Y1 | Ciclo<br>operación | Área | PM10 | PM2.5 | SO2 | NOX | CO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Tipo | ID | Descripción | [m] | [m] | [m] | [m2] | [g/s] | [g/s] | [g/s] | [g/s] | [g/s] |
| VOLUMEN | SRC_2 | PTAS | 273588 | 6383221 | <br>4 mes | 4,00 | 6,44,E-04 | 9,75,E-05 | 0,00,E+00 | 0,00,E+00 | 0,00,E+00 |
| PUNTUAL | SRC_3 | IF 2 | 273522 | 6383276 | <br>4 mes | 0,05 | 9,99,E-04 | 2,41,E-04 | 0,00,E+00 | 2,84,E-02 | 6,13,E-03 |
