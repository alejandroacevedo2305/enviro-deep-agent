---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: general
pages: 25
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 9.1 FICHAS DE CÁLCULO SOFTWARE DE MODELACIÓN
-->

# 9.1 FICHAS DE CÁLCULO SOFTWARE DE MODELACIÓN

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Resultado principal**
**Cálculo:** PE Purranque 1 - Versión Adenda

**Modelo de cálculo de ruido:**

ISO 9613-2 General
**Velocidad del viento (en Altura de buje):**
6,0 m/s - 12,0 m/s, step 1,0 m/s
**Atenuación del suelo:**
General, Fator Suelo: 0,5
**Coeficiente meteorológico, C0:**
0,0 dB
**Tipo de demanda en el cálculo:**
1: El ruido del AG se compara a la demanda (DK, DE, SE, NL etc.)
**Valores de ruido en cálculo:**
Valores de ruido medios (Lwa) (normal)
**Tonos puros:**
Ignorar la configuración de tonos puros en AGs
**Altura sobre el nivel del suelo, cuando no hay valores en objeto**
**NSA:**
4,0 m; No permitir reemplazar el modelo de altura con la altura del objeto NSA
**Margen de Incertidumbre:**
0,0 dB; El margen de incertidumbre en NSA tiene prioridad
**Desviación respecto a las exigencias de ruido "oficiales". Negativo**
**es más restrictivo, positivoe s menos restrictivo.:**
0,0 dB(A)

(C) OpenStreetMap contributors, Data OpenStreetMap and contributors, ODbL

Todas las coordenadas estan en

Escala 1:40.000

UTM (south)-WGS84 Zona: 18 Nuevo AG Zona Sensible al Ruido (NSA)

**AGs**

**Tipo de AG** **Datos de ruido**
hacia hacia Sur Z Datos Válido Fabricante Modelo de AG Potencia, Diámetro Altura Creador Nombre primera LwaRef Última LwaRef Tonos
Este brutos/Descripción nominal de buje velocidad velocidad puros
rotor viento de

viento

[m] [kW] [m] [m] [m/s] [dB(A)] [m/s] [dB(A)]
1 656.825 5.468.746 121,1 AG1 Sí NORDEX N163/6.X-6.800 6.800 163,0 145,0 USER Nordex N163/6.X - Mode 7 (STE) 6,0 103,5 12,0 103,5 Núm
2 657.276 5.468.147 128,4 AG2 Sí NORDEX N163/6.X-6.800 6.800 163,0 145,0 USER Nordex N163/6.X - Mode 1 (STE) 6,0 106,4 12,0 106,4 Núm
3 657.800 5.468.092 152,5 AG3 Sí NORDEX N163/6.X-6.800 6.800 163,0 145,0 USER Nordex N163/6.X - Mode 1 (STE) 6,0 106,4 12,0 106,4 Núm

Resultados del cálculo

**Nivel de Sonido**

**Zona Sensible al Ruido (NSA)** **Nivel de Sonido**
Núm. Nombre hacia Este hacia Sur Z Altura de imissión Max Desde AGs

[m] [m] [dB(A)]
A R1 656.063 5.468.809 116,8 4,0 35,6
B R2 656.107 5.468.943 116,6 4,0 35,6
C R3 656.132 5.469.030 117,0 4,0 35,5
D R4 656.313 5.469.309 112,4 4,0 35,3
E R5 656.587 5.469.367 119,7 4,0 36,5
F R6 656.808 5.469.281 119,6 4,0 38,5
G R7 657.138 5.469.270 123,5 4,0 38,1
H R8 657.268 5.468.851 127,4 4,0 41,8
I R9 657.334 5.468.644 127,1 4,0 43,3
J R10 657.452 5.468.563 137,6 4,0 44,0
K R11 658.254 5.467.854 137,0 4,0 41,1
L R12 657.378 5.467.012 140,1 4,0 35,3

**Distancias (m)**

**AG**

NSA 1 2 3

A 765 1382 1879

B 745 1414 1895

C 749 1445 1914

D 761 1509 1922

E 665 1401 1760

F 535 1227 1548

G 610 1131 1351

H 455 704 927

I 519 500 722

J 653 452 586

K 1685 1021 513

L 1820 1140 1160

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 1 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** PE Purranque 1 - Versión Adenda **Modelo de cálculo de ruido:** ISO 9613-2 General
Suposiciones

Calculado L(DW) = LWA,ref + K + Dc - (Adiv + Aatm + Agr + Abar + Amisc) - Cmet
(al calcular con atenuación de tierra, entonces Dc = Domega)

LWA,ref: Nivel presión de sonido en AG
K: Tono puro
Dc: Corrección de directividad
Adiv: la atenuación debido a la divergencia geométrica
Aatm: la atenuación debida a la absorción atmosférica
Agr: la atenuación debida al efecto de la tierra
Abar: la atenuación debido a una barrera

Amisc: la atenuación debida a otros efectos
Cmet: Corrección meteorológica

Resultados del cálculo

**Zona Sensible al Ruido (NSA): A R1**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 765 778 **33,31** 103,5 0,00 68,82 - - 0,00 0,00 2 1.382 1.390 **29,71** 106,4 0,00 73,86 - - 0,00 0,00 3 1.879 1.887 **26,06** 106,4 0,00 76,52 - - 0,00 0,00 Suma **35,42**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 765 778 **33,32** 103,5 0,00 68,82 - - 0,00 0,00 2 1.382 1.390 **29,72** 106,4 0,00 73,86 - - 0,00 0,00 3 1.879 1.887 **26,07** 106,4 0,00 76,52 - - 0,00 0,00 Suma **35,43**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 765 778 **33,42** 103,5 0,00 68,82 - - 0,00 0,00 2 1.382 1.390 **29,87** 106,4 0,00 73,86 - - 0,00 0,00 3 1.879 1.887 **26,24** 106,4 0,00 76,52 - - 0,00 0,00 Suma **35,55**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 765 778 **33,42** 103,5 0,00 68,82 - - 0,00 0,00 2 1.382 1.390 **29,87** 106,4 0,00 73,86 - - 0,00 0,00 3 1.879 1.887 **26,24** 106,4 0,00 76,52 - - 0,00 0,00 Suma **35,55**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 765 778 **33,42** 103,5 0,00 68,82 - - 0,00 0,00 2 1.382 1.390 **29,87** 106,4 0,00 73,86 - - 0,00 0,00 3 1.879 1.887 **26,24** 106,4 0,00 76,52 - - 0,00 0,00 Suma **35,55**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 1 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** PE Purranque 1 - Versión Adenda **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 765 778 **33,42** 103,5 0,00 68,82 - - 0,00 0,00 2 1.382 1.390 **29,87** 106,4 0,00 73,86 - - 0,00 0,00 3 1.879 1.887 **26,24** 106,4 0,00 76,52 - - 0,00 0,00 Suma **35,55**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 765 778 **33,42** 103,5 0,00 68,82 - - 0,00 0,00 2 1.382 1.390 **29,87** 106,4 0,00 73,86 - - 0,00 0,00 3 1.879 1.887 **26,24** 106,4 0,00 76,52 - - 0,00 0,00 Suma **35,55**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): B R2**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 745 759 **33,59** 103,5 0,00 68,60 - - 0,00 0,00 2 1.414 1.423 **29,44** 106,4 0,00 74,06 - - 0,00 0,00 3 1.895 1.903 **25,96** 106,4 0,00 76,59 - - 0,00 0,00 Suma **35,51**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 745 759 **33,60** 103,5 0,00 68,60 - - 0,00 0,00 2 1.414 1.423 **29,45** 106,4 0,00 74,06 - - 0,00 0,00 3 1.895 1.903 **25,97** 106,4 0,00 76,59 - - 0,00 0,00 Suma **35,52**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 745 759 **33,70** 103,5 0,00 68,60 - - 0,00 0,00 2 1.414 1.423 **29,60** 106,4 0,00 74,06 - - 0,00 0,00 3 1.895 1.903 **26,14** 106,4 0,00 76,59 - - 0,00 0,00 Suma **35,64**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 745 759 **33,70** 103,5 0,00 68,60 - - 0,00 0,00 2 1.414 1.423 **29,60** 106,4 0,00 74,06 - - 0,00 0,00 3 1.895 1.903 **26,14** 106,4 0,00 76,59 - - 0,00 0,00 Suma **35,64**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 745 759 **33,70** 103,5 0,00 68,60 - - 0,00 0,00 2 1.414 1.423 **29,60** 106,4 0,00 74,06 - - 0,00 0,00 3 1.895 1.903 **26,14** 106,4 0,00 76,59 - - 0,00 0,00 Suma **35,64**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 2 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** PE Purranque 1 - Versión Adenda **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 745 759 **33,70** 103,5 0,00 68,60 - - 0,00 0,00 2 1.414 1.423 **29,60** 106,4 0,00 74,06 - - 0,00 0,00 3 1.895 1.903 **26,14** 106,4 0,00 76,59 - - 0,00 0,00 Suma **35,64**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 745 759 **33,70** 103,5 0,00 68,60 - - 0,00 0,00 2 1.414 1.423 **29,60** 106,4 0,00 74,06 - - 0,00 0,00 3 1.895 1.903 **26,14** 106,4 0,00 76,59 - - 0,00 0,00 Suma **35,64**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): C R3**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 749 763 **33,53** 103,5 0,00 68,65 - - 0,00 0,00 2 1.445 1.453 **29,19** 106,4 0,00 74,25 - - 0,00 0,00 3 1.914 1.922 **25,84** 106,4 0,00 76,67 - - 0,00 0,00 Suma **35,40**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 749 763 **33,54** 103,5 0,00 68,65 - - 0,00 0,00 2 1.445 1.453 **29,20** 106,4 0,00 74,25 - - 0,00 0,00 3 1.914 1.922 **25,85** 106,4 0,00 76,67 - - 0,00 0,00 Suma **35,41**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 749 763 **33,64** 103,5 0,00 68,65 - - 0,00 0,00 2 1.445 1.453 **29,35** 106,4 0,00 74,25 - - 0,00 0,00 3 1.914 1.922 **26,02** 106,4 0,00 76,67 - - 0,00 0,00 Suma **35,53**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 749 763 **33,64** 103,5 0,00 68,65 - - 0,00 0,00 2 1.445 1.453 **29,35** 106,4 0,00 74,25 - - 0,00 0,00 3 1.914 1.922 **26,02** 106,4 0,00 76,67 - - 0,00 0,00 Suma **35,53**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 749 763 **33,64** 103,5 0,00 68,65 - - 0,00 0,00 2 1.445 1.453 **29,35** 106,4 0,00 74,25 - - 0,00 0,00 3 1.914 1.922 **26,02** 106,4 0,00 76,67 - - 0,00 0,00 Suma **35,53**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 3 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** PE Purranque 1 - Versión Adenda **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 749 763 **33,64** 103,5 0,00 68,65 - - 0,00 0,00 2 1.445 1.453 **29,35** 106,4 0,00 74,25 - - 0,00 0,00 3 1.914 1.922 **26,02** 106,4 0,00 76,67 - - 0,00 0,00 Suma **35,53**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 749 763 **33,64** 103,5 0,00 68,65 - - 0,00 0,00 2 1.445 1.453 **29,35** 106,4 0,00 74,25 - - 0,00 0,00 3 1.914 1.922 **26,02** 106,4 0,00 76,67 - - 0,00 0,00 Suma **35,53**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): D R4**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 761 776 **33,35** 103,5 0,00 68,79 - - 0,00 0,00 2 1.509 1.517 **28,68** 106,4 0,00 74,62 - - 0,00 0,00 3 1.922 1.930 **25,79** 106,4 0,00 76,71 - - 0,00 0,00 Suma **35,16**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 761 776 **33,36** 103,5 0,00 68,79 - - 0,00 0,00 2 1.509 1.517 **28,69** 106,4 0,00 74,62 - - 0,00 0,00 3 1.922 1.930 **25,80** 106,4 0,00 76,71 - - 0,00 0,00 Suma **35,17**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 761 776 **33,46** 103,5 0,00 68,79 - - 0,00 0,00 2 1.509 1.517 **28,85** 106,4 0,00 74,62 - - 0,00 0,00 3 1.922 1.930 **25,97** 106,4 0,00 76,71 - - 0,00 0,00 Suma **35,29**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 761 776 **33,46** 103,5 0,00 68,79 - - 0,00 0,00 2 1.509 1.517 **28,85** 106,4 0,00 74,62 - - 0,00 0,00 3 1.922 1.930 **25,97** 106,4 0,00 76,71 - - 0,00 0,00 Suma **35,29**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 761 776 **33,46** 103,5 0,00 68,79 - - 0,00 0,00 2 1.509 1.517 **28,85** 106,4 0,00 74,62 - - 0,00 0,00 3 1.922 1.930 **25,97** 106,4 0,00 76,71 - - 0,00 0,00 Suma **35,29**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 4 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** PE Purranque 1 - Versión Adenda **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 761 776 **33,46** 103,5 0,00 68,79 - - 0,00 0,00 2 1.509 1.517 **28,85** 106,4 0,00 74,62 - - 0,00 0,00 3 1.922 1.930 **25,97** 106,4 0,00 76,71 - - 0,00 0,00 Suma **35,29**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 761 776 **33,46** 103,5 0,00 68,79 - - 0,00 0,00 2 1.509 1.517 **28,85** 106,4 0,00 74,62 - - 0,00 0,00 3 1.922 1.930 **25,97** 106,4 0,00 76,71 - - 0,00 0,00 Suma **35,29**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): E R5**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 665 680 **34,76** 103,5 0,00 67,65 - - 0,00 0,00 2 1.401 1.409 **29,55** 106,4 0,00 73,98 - - 0,00 0,00 3 1.760 1.768 **26,85** 106,4 0,00 75,95 - - 0,00 0,00 Suma **36,41**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 665 680 **34,77** 103,5 0,00 67,65 - - 0,00 0,00 2 1.401 1.409 **29,56** 106,4 0,00 73,98 - - 0,00 0,00 3 1.760 1.768 **26,86** 106,4 0,00 75,95 - - 0,00 0,00 Suma **36,42**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 665 680 **34,85** 103,5 0,00 67,65 - - 0,00 0,00 2 1.401 1.409 **29,71** 106,4 0,00 73,98 - - 0,00 0,00 3 1.760 1.768 **27,03** 106,4 0,00 75,95 - - 0,00 0,00 Suma **36,53**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 665 680 **34,85** 103,5 0,00 67,65 - - 0,00 0,00 2 1.401 1.409 **29,71** 106,4 0,00 73,98 - - 0,00 0,00 3 1.760 1.768 **27,03** 106,4 0,00 75,95 - - 0,00 0,00 Suma **36,53**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 665 680 **34,85** 103,5 0,00 67,65 - - 0,00 0,00 2 1.401 1.409 **29,71** 106,4 0,00 73,98 - - 0,00 0,00 3 1.760 1.768 **27,03** 106,4 0,00 75,95 - - 0,00 0,00 Suma **36,53**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 5 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** PE Purranque 1 - Versión Adenda **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 665 680 **34,85** 103,5 0,00 67,65 - - 0,00 0,00 2 1.401 1.409 **29,71** 106,4 0,00 73,98 - - 0,00 0,00 3 1.760 1.768 **27,03** 106,4 0,00 75,95 - - 0,00 0,00 Suma **36,53**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 665 680 **34,85** 103,5 0,00 67,65 - - 0,00 0,00 2 1.401 1.409 **29,71** 106,4 0,00 73,98 - - 0,00 0,00 3 1.760 1.768 **27,03** 106,4 0,00 75,95 - - 0,00 0,00 Suma **36,53**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): F R6**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 535 554 **36,91** 103,5 0,00 65,87 - - 0,00 0,00 2 1.227 1.236 **31,07** 106,4 0,00 72,84 - - 0,00 0,00 3 1.548 1.558 **28,37** 106,4 0,00 74,85 - - 0,00 0,00 Suma **38,37**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 535 554 **36,92** 103,5 0,00 65,87 - - 0,00 0,00 2 1.227 1.236 **31,08** 106,4 0,00 72,84 - - 0,00 0,00 3 1.548 1.558 **28,38** 106,4 0,00 74,85 - - 0,00 0,00 Suma **38,38**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 535 554 **36,99** 103,5 0,00 65,87 - - 0,00 0,00 2 1.227 1.236 **31,22** 106,4 0,00 72,84 - - 0,00 0,00 3 1.548 1.558 **28,54** 106,4 0,00 74,85 - - 0,00 0,00 Suma **38,47**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 535 554 **36,99** 103,5 0,00 65,87 - - 0,00 0,00 2 1.227 1.236 **31,22** 106,4 0,00 72,84 - - 0,00 0,00 3 1.548 1.558 **28,54** 106,4 0,00 74,85 - - 0,00 0,00 Suma **38,47**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 535 554 **36,99** 103,5 0,00 65,87 - - 0,00 0,00 2 1.227 1.236 **31,22** 106,4 0,00 72,84 - - 0,00 0,00 3 1.548 1.558 **28,54** 106,4 0,00 74,85 - - 0,00 0,00 Suma **38,47**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 6 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** PE Purranque 1 - Versión Adenda **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 535 554 **36,99** 103,5 0,00 65,87 - - 0,00 0,00 2 1.227 1.236 **31,22** 106,4 0,00 72,84 - - 0,00 0,00 3 1.548 1.558 **28,54** 106,4 0,00 74,85 - - 0,00 0,00 Suma **38,47**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 535 554 **36,99** 103,5 0,00 65,87 - - 0,00 0,00 2 1.227 1.236 **31,22** 106,4 0,00 72,84 - - 0,00 0,00 3 1.548 1.558 **28,54** 106,4 0,00 74,85 - - 0,00 0,00 Suma **38,47**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): G R7**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 610 626 **35,63** 103,5 0,00 66,93 - - 0,00 0,00 2 1.131 1.141 **31,98** 106,4 0,00 72,14 - - 0,00 0,00 3 1.351 1.362 **29,95** 106,4 0,00 73,68 - - 0,00 0,00 Suma **37,94**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 610 626 **35,65** 103,5 0,00 66,93 - - 0,00 0,00 2 1.131 1.141 **31,99** 106,4 0,00 72,14 - - 0,00 0,00 3 1.351 1.362 **29,96** 106,4 0,00 73,68 - - 0,00 0,00 Suma **37,95**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 610 626 **35,72** 103,5 0,00 66,93 - - 0,00 0,00 2 1.131 1.141 **32,12** 106,4 0,00 72,14 - - 0,00 0,00 3 1.351 1.362 **30,11** 106,4 0,00 73,68 - - 0,00 0,00 Suma **38,06**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 610 626 **35,72** 103,5 0,00 66,93 - - 0,00 0,00 2 1.131 1.141 **32,12** 106,4 0,00 72,14 - - 0,00 0,00 3 1.351 1.362 **30,11** 106,4 0,00 73,68 - - 0,00 0,00 Suma **38,06**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 610 626 **35,72** 103,5 0,00 66,93 - - 0,00 0,00 2 1.131 1.141 **32,12** 106,4 0,00 72,14 - - 0,00 0,00 3 1.351 1.362 **30,11** 106,4 0,00 73,68 - - 0,00 0,00 Suma **38,06**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 7 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** PE Purranque 1 - Versión Adenda **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 610 626 **35,72** 103,5 0,00 66,93 - - 0,00 0,00 2 1.131 1.141 **32,12** 106,4 0,00 72,14 - - 0,00 0,00 3 1.351 1.362 **30,11** 106,4 0,00 73,68 - - 0,00 0,00 Suma **38,06**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 610 626 **35,72** 103,5 0,00 66,93 - - 0,00 0,00 2 1.131 1.141 **32,12** 106,4 0,00 72,14 - - 0,00 0,00 3 1.351 1.362 **30,11** 106,4 0,00 73,68 - - 0,00 0,00 Suma **38,06**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): H R8**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 455 475 **38,49** 103,5 0,00 64,53 - - 0,00 0,00 2 704 718 **37,08** 106,4 0,00 68,13 - - 0,00 0,00 3 927 942 **34,13** 106,4 0,00 70,48 - - 0,00 0,00 Suma **41,69**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 455 475 **38,51** 103,5 0,00 64,53 - - 0,00 0,00 2 704 718 **37,09** 106,4 0,00 68,13 - - 0,00 0,00 3 927 942 **34,14** 106,4 0,00 70,48 - - 0,00 0,00 Suma **41,70**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 455 475 **38,56** 103,5 0,00 64,53 - - 0,00 0,00 2 704 718 **37,18** 106,4 0,00 68,13 - - 0,00 0,00 3 927 942 **34,26** 106,4 0,00 70,48 - - 0,00 0,00 Suma **41,78**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 455 475 **38,56** 103,5 0,00 64,53 - - 0,00 0,00 2 704 718 **37,18** 106,4 0,00 68,13 - - 0,00 0,00 3 927 942 **34,26** 106,4 0,00 70,48 - - 0,00 0,00 Suma **41,78**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 455 475 **38,56** 103,5 0,00 64,53 - - 0,00 0,00 2 704 718 **37,18** 106,4 0,00 68,13 - - 0,00 0,00 3 927 942 **34,26** 106,4 0,00 70,48 - - 0,00 0,00 Suma **41,78**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 8 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** PE Purranque 1 - Versión Adenda **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 455 475 **38,56** 103,5 0,00 64,53 - - 0,00 0,00 2 704 718 **37,18** 106,4 0,00 68,13 - - 0,00 0,00 3 927 942 **34,26** 106,4 0,00 70,48 - - 0,00 0,00 Suma **41,78**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 455 475 **38,56** 103,5 0,00 64,53 - - 0,00 0,00 2 704 718 **37,18** 106,4 0,00 68,13 - - 0,00 0,00 3 927 942 **34,26** 106,4 0,00 70,48 - - 0,00 0,00 Suma **41,78**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): I R9**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 519 536 **37,24** 103,5 0,00 65,59 - - 0,00 0,00 2 500 520 **40,46** 106,4 0,00 65,32 - - 0,00 0,00 3 722 741 **36,74** 106,4 0,00 68,40 - - 0,00 0,00 Suma **43,25**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 519 536 **37,26** 103,5 0,00 65,59 - - 0,00 0,00 2 500 520 **40,47** 106,4 0,00 65,32 - - 0,00 0,00 3 722 741 **36,75** 106,4 0,00 68,40 - - 0,00 0,00 Suma **43,26**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 519 536 **37,32** 103,5 0,00 65,59 - - 0,00 0,00 2 500 520 **40,53** 106,4 0,00 65,32 - - 0,00 0,00 3 722 741 **36,84** 106,4 0,00 68,40 - - 0,00 0,00 Suma **43,33**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 519 536 **37,32** 103,5 0,00 65,59 - - 0,00 0,00 2 500 520 **40,53** 106,4 0,00 65,32 - - 0,00 0,00 3 722 741 **36,84** 106,4 0,00 68,40 - - 0,00 0,00 Suma **43,33**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 519 536 **37,32** 103,5 0,00 65,59 - - 0,00 0,00 2 500 520 **40,53** 106,4 0,00 65,32 - - 0,00 0,00 3 722 741 **36,84** 106,4 0,00 68,40 - - 0,00 0,00 Suma **43,33**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 9 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** PE Purranque 1 - Versión Adenda **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 519 536 **37,32** 103,5 0,00 65,59 - - 0,00 0,00 2 500 520 **40,53** 106,4 0,00 65,32 - - 0,00 0,00 3 722 741 **36,84** 106,4 0,00 68,40 - - 0,00 0,00 Suma **43,33**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 519 536 **37,32** 103,5 0,00 65,59 - - 0,00 0,00 2 500 520 **40,53** 106,4 0,00 65,32 - - 0,00 0,00 3 722 741 **36,84** 106,4 0,00 68,40 - - 0,00 0,00 Suma **43,33**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): J R10**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 653 665 **35,00** 103,5 0,00 67,46 - - 0,00 0,00 2 452 471 **41,49** 106,4 0,00 64,45 - - 0,00 0,00 3 586 606 **38,87** 106,4 0,00 66,65 - - 0,00 0,00 Suma **43,97**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 653 665 **35,01** 103,5 0,00 67,46 - - 0,00 0,00 2 452 471 **41,50** 106,4 0,00 64,45 - - 0,00 0,00 3 586 606 **38,89** 106,4 0,00 66,65 - - 0,00 0,00 Suma **43,99**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 653 665 **35,09** 103,5 0,00 67,46 - - 0,00 0,00 2 452 471 **41,55** 106,4 0,00 64,45 - - 0,00 0,00 3 586 606 **38,96** 106,4 0,00 66,65 - - 0,00 0,00 Suma **44,05**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 653 665 **35,09** 103,5 0,00 67,46 - - 0,00 0,00 2 452 471 **41,55** 106,4 0,00 64,45 - - 0,00 0,00 3 586 606 **38,96** 106,4 0,00 66,65 - - 0,00 0,00 Suma **44,05**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 653 665 **35,09** 103,5 0,00 67,46 - - 0,00 0,00 2 452 471 **41,55** 106,4 0,00 64,45 - - 0,00 0,00 3 586 606 **38,96** 106,4 0,00 66,65 - - 0,00 0,00 Suma **44,05**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 10 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** PE Purranque 1 - Versión Adenda **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 653 665 **35,09** 103,5 0,00 67,46 - - 0,00 0,00 2 452 471 **41,55** 106,4 0,00 64,45 - - 0,00 0,00 3 586 606 **38,96** 106,4 0,00 66,65 - - 0,00 0,00 Suma **44,05**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 653 665 **35,09** 103,5 0,00 67,46 - - 0,00 0,00 2 452 471 **41,55** 106,4 0,00 64,45 - - 0,00 0,00 3 586 606 **38,96** 106,4 0,00 66,65 - - 0,00 0,00 Suma **44,05**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): K R11**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 1.685 1.689 **24,51** 103,5 0,00 75,55 - - 0,00 0,00 2 1.021 1.029 **33,14** 106,4 0,00 71,25 - - 0,00 0,00 3 513 536 **40,15** 106,4 0,00 65,58 - - 0,00 0,00 Suma **41,04**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 1.685 1.689 **24,51** 103,5 0,00 75,55 - - 0,00 0,00 2 1.021 1.029 **33,15** 106,4 0,00 71,25 - - 0,00 0,00 3 513 536 **40,17** 106,4 0,00 65,58 - - 0,00 0,00 Suma **41,05**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 1.685 1.689 **24,68** 103,5 0,00 75,55 - - 0,00 0,00 2 1.021 1.029 **33,27** 106,4 0,00 71,25 - - 0,00 0,00 3 513 536 **40,23** 106,4 0,00 65,58 - - 0,00 0,00 Suma **41,13**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 1.685 1.689 **24,68** 103,5 0,00 75,55 - - 0,00 0,00 2 1.021 1.029 **33,27** 106,4 0,00 71,25 - - 0,00 0,00 3 513 536 **40,23** 106,4 0,00 65,58 - - 0,00 0,00 Suma **41,13**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 1.685 1.689 **24,68** 103,5 0,00 75,55 - - 0,00 0,00 2 1.021 1.029 **33,27** 106,4 0,00 71,25 - - 0,00 0,00 3 513 536 **40,23** 106,4 0,00 65,58 - - 0,00 0,00 Suma **41,13**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 11 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** PE Purranque 1 - Versión Adenda **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 1.685 1.689 **24,68** 103,5 0,00 75,55 - - 0,00 0,00 2 1.021 1.029 **33,27** 106,4 0,00 71,25 - - 0,00 0,00 3 513 536 **40,23** 106,4 0,00 65,58 - - 0,00 0,00 Suma **41,13**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 1.685 1.689 **24,68** 103,5 0,00 75,55 - - 0,00 0,00 2 1.021 1.029 **33,27** 106,4 0,00 71,25 - - 0,00 0,00 3 513 536 **40,23** 106,4 0,00 65,58 - - 0,00 0,00 Suma **41,13**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): L R12**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 1.820 1.824 **23,58** 103,5 0,00 76,22 - - 0,00 0,00 2 1.140 1.147 **31,92** 106,4 0,00 72,19 - - 0,00 0,00 3 1.160 1.170 **31,70** 106,4 0,00 72,36 - - 0,00 0,00 Suma **35,14**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 1.820 1.824 **23,59** 103,5 0,00 76,22 - - 0,00 0,00 2 1.140 1.147 **31,93** 106,4 0,00 72,19 - - 0,00 0,00 3 1.160 1.170 **31,71** 106,4 0,00 72,36 - - 0,00 0,00 Suma **35,14**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 1.820 1.824 **23,76** 103,5 0,00 76,22 - - 0,00 0,00 2 1.140 1.147 **32,07** 106,4 0,00 72,19 - - 0,00 0,00 3 1.160 1.170 **31,84** 106,4 0,00 72,36 - - 0,00 0,00 Suma **35,28**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 1.820 1.824 **23,76** 103,5 0,00 76,22 - - 0,00 0,00 2 1.140 1.147 **32,07** 106,4 0,00 72,19 - - 0,00 0,00 3 1.160 1.170 **31,84** 106,4 0,00 72,36 - - 0,00 0,00 Suma **35,28**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 1.820 1.824 **23,76** 103,5 0,00 76,22 - - 0,00 0,00 2 1.140 1.147 **32,07** 106,4 0,00 72,19 - - 0,00 0,00 3 1.160 1.170 **31,84** 106,4 0,00 72,36 - - 0,00 0,00 Suma **35,28**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 12 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** PE Purranque 1 - Versión Adenda **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 1.820 1.824 **23,76** 103,5 0,00 76,22 - - 0,00 0,00 2 1.140 1.147 **32,07** 106,4 0,00 72,19 - - 0,00 0,00 3 1.160 1.170 **31,84** 106,4 0,00 72,36 - - 0,00 0,00 Suma **35,28**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
1 1.820 1.824 **23,76** 103,5 0,00 76,22 - - 0,00 0,00 2 1.140 1.147 **32,07** 106,4 0,00 72,19 - - 0,00 0,00 3 1.160 1.170 **31,84** 106,4 0,00 72,36 - - 0,00 0,00 Suma **35,28**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 13 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Suposiciones para cálculo de ruido**
**Cálculo:** PE Purranque 1 - Versión Adenda

**Modelo de cálculo de ruido:**

ISO 9613-2 General
**Velocidad del viento (en Altura de buje):**
6,0 m/s - 12,0 m/s, step 1,0 m/s
**Atenuación del suelo:**
General, Fator Suelo: 0,5
**Coeficiente meteorológico, C0:**
0,0 dB
**Tipo de demanda en el cálculo:**
1: El ruido del AG se compara a la demanda (DK, DE, SE, NL etc.)
**Valores de ruido en cálculo:**
Valores de ruido medios (Lwa) (normal)
**Tonos puros:**
Ignorar la configuración de tonos puros en AGs
**Altura sobre el nivel del suelo, cuando no hay valores en objeto NSA:**
4,0 m; No permitir reemplazar el modelo de altura con la altura del objeto NSA
**Margen de Incertidumbre:**
0,0 dB; El margen de incertidumbre en NSA tiene prioridad
**Desviación respecto a las exigencias de ruido "oficiales". Negativo es más restrictivo, positivoe s menos restrictivo.:**
0,0 dB(A)
**Datos de octavas requeridas**

Absorción de aire dependiente de la frecuencia

63 125 250 500 1.000 2.000 4.000 8.000

[dB/km] [dB/km] [dB/km] [dB/km] [dB/km] [dB/km] [dB/km] [dB/km]

0,10 0,40 1,00 1,90 3,70 9,70 32,80 117,00

Todas las coordenadas estan en
UTM (south)-WGS84 Zona: 18

**AG:** NORDEX N163/6.X 6800 163.0 !O!
**Ruido:** Nordex N163/6.X - Mode 7 (STE)

Origen Fuente/Fecha Creador Editado
Nordex 20-01-2022 USER 20-01-2022 16:45

**Datos de Octavas**
Estatus Velocidad del viento LwA,ref Tonos puros 63 125 250 500 1000 2000 4000 8000

[m/s] [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
De Catálogo AGs 6,0 103,5 Núm 84,8 91,4 95,1 97,2 98,5 96,6 87,0 79,1
De Catálogo AGs 7,0 103,5 Núm 84,9 91,4 95,1 97,2 98,5 96,7 87,1 79,2
De Catálogo AGs 8,0 103,5 Núm 85,2 91,4 95,1 97,7 98,4 95,9 88,3 80,3
De Catálogo AGs 9,0 103,5 Núm 85,2 91,4 95,1 97,7 98,4 95,9 88,3 80,3
De Catálogo AGs 10,0 103,5 Núm 85,2 91,4 95,1 97,7 98,4 95,9 88,3 80,3
De Catálogo AGs 11,0 103,5 Núm 85,2 91,4 95,1 97,7 98,4 95,9 88,3 80,3
De Catálogo AGs 12,0 103,5 Núm 85,2 91,4 95,1 97,7 98,4 95,9 88,3 80,3

**AG:** NORDEX N163/6.X 6800 163.0 !O!
**Ruido:** Nordex N163/6.X - Mode 1 (STE)

Origen Fuente/Fecha Creador Editado
Nordex 15-07-2021 USER 20-01-2022 15:44

**Datos de Octavas**
Estatus Velocidad del viento LwA,ref Tonos puros 63 125 250 500 1000 2000 4000 8000

[m/s] [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
De Catálogo AGs 6,0 106,4 Núm 87,7 94,3 98,0 100,1 101,4 99,5 89,9 82,0
De Catálogo AGs 7,0 106,4 Núm 87,8 94,3 98,0 100,1 101,4 99,6 90,0 82,1
De Catálogo AGs 8,0 106,4 Núm 88,1 94,3 98,0 100,6 101,3 98,8 91,2 83,2
De Catálogo AGs 9,0 106,4 Núm 88,1 94,3 98,0 100,6 101,3 98,8 91,2 83,2
De Catálogo AGs 10,0 106,4 Núm 88,1 94,3 98,0 100,6 101,3 98,8 91,2 83,2
De Catálogo AGs 11,0 106,4 Núm 88,1 94,3 98,0 100,6 101,3 98,8 91,2 83,2
De Catálogo AGs 12,0 106,4 Núm 88,1 94,3 98,0 100,6 101,3 98,8 91,2 83,2

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 1 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Suposiciones para cálculo de ruido**
**Cálculo:** PE Purranque 1 - Versión Adenda
**AG:** NORDEX N163/6.X 6800 163.0 !O!
**Ruido:** Nordex N163/6.X - Mode 1 (STE)

Origen Fuente/Fecha Creador Editado
Nordex 15-07-2021 USER 20-01-2022 15:44

**Datos de Octavas**
Estatus Velocidad del viento LwA,ref Tonos puros 63 125 250 500 1000 2000 4000 8000

[m/s] [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
De Catálogo AGs 6,0 106,4 Núm 87,7 94,3 98,0 100,1 101,4 99,5 89,9 82,0
De Catálogo AGs 7,0 106,4 Núm 87,8 94,3 98,0 100,1 101,4 99,6 90,0 82,1
De Catálogo AGs 8,0 106,4 Núm 88,1 94,3 98,0 100,6 101,3 98,8 91,2 83,2
De Catálogo AGs 9,0 106,4 Núm 88,1 94,3 98,0 100,6 101,3 98,8 91,2 83,2
De Catálogo AGs 10,0 106,4 Núm 88,1 94,3 98,0 100,6 101,3 98,8 91,2 83,2
De Catálogo AGs 11,0 106,4 Núm 88,1 94,3 98,0 100,6 101,3 98,8 91,2 83,2
De Catálogo AGs 12,0 106,4 Núm 88,1 94,3 98,0 100,6 101,3 98,8 91,2 83,2

**Zona Sensible al Ruido (NSA): A R1**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): B R2**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): C R3**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): D R4**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): E R5**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): F R6**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): G R7**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): H R8**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): I R9**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): J R10**
**Sin demanda de ruido**

**Sin demanda de distancia**

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 2 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Suposiciones para cálculo de ruido**
**Cálculo:** PE Purranque 1 - Versión Adenda
**Zona Sensible al Ruido (NSA): K R11**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): L R12**
**Sin demanda de ruido**

**Sin demanda de distancia**

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 16:12 / 3 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Mapa 6,0 m/s**
**Cálculo:** PE Purranque 1 - Versión Adenda

|Ruido [dB(A)]<br>35<br>40<br>45<br>50<br>55<br>Ruido [dB(A)]<br>35 - <40<br>40 - <45<br>45 - <50<br>50 - <55<br>55 - <=53<br>(C) OpenStreetMap contributors, Data OpenStreetMap and contributors, ODbL|Col2|Col3|Col4|Col5|Col6|Ruido [dB(A)]<br>35<br>40<br>45<br>50<br>55<br>Ruido [dB(A)]<br>35 - <40<br>40 - <45<br>45 - <50<br>50 - <55<br>55 - <=53|
|---|---|---|---|---|---|---|
||||||||

0 500 1000 1500 2000 m
Mapa: EMD OpenStreetMap, Escala de impresión 1:40.000, Centro de mapa UTM (south)-WGS84 Zona: 18 Este: 657.313 Norte: 5.468.419
Nuevo AG Zona Sensible al Ruido (NSA)

Modelo de cálculo de ruido: ISO 9613-2 General. Velocidad del viento: 6,0 m/s

Altura sobre el nivel del mar del objeto de línea activo

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 15:48 / 1 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Mapa 7,0 m/s**
**Cálculo:** PE Purranque 1 - Versión Adenda

|Ruido [dB(A)]<br>35<br>40<br>45<br>50<br>55<br>Ruido [dB(A)]<br>35 - <40<br>40 - <45<br>45 - <50<br>50 - <55<br>55 - <=54<br>(C) OpenStreetMap contributors, Data OpenStreetMap and contributors, ODbL|Col2|Col3|Col4|Col5|Col6|Ruido [dB(A)]<br>35<br>40<br>45<br>50<br>55<br>Ruido [dB(A)]<br>35 - <40<br>40 - <45<br>45 - <50<br>50 - <55<br>55 - <=54|
|---|---|---|---|---|---|---|
||||||||

0 500 1000 1500 2000 m
Mapa: EMD OpenStreetMap, Escala de impresión 1:40.000, Centro de mapa UTM (south)-WGS84 Zona: 18 Este: 657.313 Norte: 5.468.419
Nuevo AG Zona Sensible al Ruido (NSA)

Modelo de cálculo de ruido: ISO 9613-2 General. Velocidad del viento: 7,0 m/s

Altura sobre el nivel del mar del objeto de línea activo

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 15:48 / 2 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Mapa 8,0 m/s**
**Cálculo:** PE Purranque 1 - Versión Adenda

|Ruido [dB(A)]<br>35<br>40<br>45<br>50<br>55<br>Ruido [dB(A)]<br>35 - <40<br>40 - <45<br>45 - <50<br>50 - <55<br>55 - <=54<br>(C) OpenStreetMap contributors, Data OpenStreetMap and contributors, ODbL|Col2|Col3|Col4|Col5|Col6|Ruido [dB(A)]<br>35<br>40<br>45<br>50<br>55<br>Ruido [dB(A)]<br>35 - <40<br>40 - <45<br>45 - <50<br>50 - <55<br>55 - <=54|
|---|---|---|---|---|---|---|
||||||||

0 500 1000 1500 2000 m
Mapa: EMD OpenStreetMap, Escala de impresión 1:40.000, Centro de mapa UTM (south)-WGS84 Zona: 18 Este: 657.313 Norte: 5.468.419
Nuevo AG Zona Sensible al Ruido (NSA)

Modelo de cálculo de ruido: ISO 9613-2 General. Velocidad del viento: 8,0 m/s

Altura sobre el nivel del mar del objeto de línea activo

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 15:48 / 3 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Mapa 9,0 m/s**
**Cálculo:** PE Purranque 1 - Versión Adenda

|Ruido [dB(A)]<br>35<br>40<br>45<br>50<br>55<br>Ruido [dB(A)]<br>35 - <40<br>40 - <45<br>45 - <50<br>50 - <55<br>55 - <=54<br>(C) OpenStreetMap contributors, Data OpenStreetMap and contributors, ODbL|Col2|Col3|Col4|Col5|Col6|Ruido [dB(A)]<br>35<br>40<br>45<br>50<br>55<br>Ruido [dB(A)]<br>35 - <40<br>40 - <45<br>45 - <50<br>50 - <55<br>55 - <=54|
|---|---|---|---|---|---|---|
||||||||

0 500 1000 1500 2000 m
Mapa: EMD OpenStreetMap, Escala de impresión 1:40.000, Centro de mapa UTM (south)-WGS84 Zona: 18 Este: 657.313 Norte: 5.468.419
Nuevo AG Zona Sensible al Ruido (NSA)

Modelo de cálculo de ruido: ISO 9613-2 General. Velocidad del viento: 9,0 m/s

Altura sobre el nivel del mar del objeto de línea activo

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 15:48 / 4 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Mapa 10,0 m/s**
**Cálculo:** PE Purranque 1 - Versión Adenda

|Ruido [dB(A)]<br>35<br>40<br>45<br>50<br>55<br>Ruido [dB(A)]<br>35 - <40<br>40 - <45<br>45 - <50<br>50 - <55<br>55 - <=54<br>(C) OpenStreetMap contributors, Data OpenStreetMap and contributors, ODbL|Col2|Col3|Col4|Col5|Col6|Ruido [dB(A)]<br>35<br>40<br>45<br>50<br>55<br>Ruido [dB(A)]<br>35 - <40<br>40 - <45<br>45 - <50<br>50 - <55<br>55 - <=54|
|---|---|---|---|---|---|---|
||||||||

0 500 1000 1500 2000 m
Mapa: EMD OpenStreetMap, Escala de impresión 1:40.000, Centro de mapa UTM (south)-WGS84 Zona: 18 Este: 657.313 Norte: 5.468.419
Nuevo AG Zona Sensible al Ruido (NSA)

Modelo de cálculo de ruido: ISO 9613-2 General. Velocidad del viento: 10,0 m/s

Altura sobre el nivel del mar del objeto de línea activo

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 15:48 / 5 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Mapa 11,0 m/s**
**Cálculo:** PE Purranque 1 - Versión Adenda

|Ruido [dB(A)]<br>35<br>40<br>45<br>50<br>55<br>Ruido [dB(A)]<br>35 - <40<br>40 - <45<br>45 - <50<br>50 - <55<br>55 - <=54<br>(C) OpenStreetMap contributors, Data OpenStreetMap and contributors, ODbL|Col2|Col3|Col4|Col5|Col6|Ruido [dB(A)]<br>35<br>40<br>45<br>50<br>55<br>Ruido [dB(A)]<br>35 - <40<br>40 - <45<br>45 - <50<br>50 - <55<br>55 - <=54|
|---|---|---|---|---|---|---|
||||||||

0 500 1000 1500 2000 m
Mapa: EMD OpenStreetMap, Escala de impresión 1:40.000, Centro de mapa UTM (south)-WGS84 Zona: 18 Este: 657.313 Norte: 5.468.419
Nuevo AG Zona Sensible al Ruido (NSA)

Modelo de cálculo de ruido: ISO 9613-2 General. Velocidad del viento: 11,0 m/s

Altura sobre el nivel del mar del objeto de línea activo

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 15:48 / 6 windPRO

Proyecto: Usuario con licencia:
**PE Purranque 1** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-05-2022 17:50/3.5.552

**DECIBEL - Mapa 12,0 m/s**
**Cálculo:** PE Purranque 1 - Versión Adenda

|Ruido [dB(A)]<br>35<br>40<br>45<br>50<br>55<br>Ruido [dB(A)]<br>35 - <40<br>40 - <45<br>45 - <50<br>50 - <55<br>55 - <=54<br>(C) OpenStreetMap contributors, Data OpenStreetMap and contributors, ODbL|Col2|Col3|Col4|Col5|Col6|Ruido [dB(A)]<br>35<br>40<br>45<br>50<br>55<br>Ruido [dB(A)]<br>35 - <40<br>40 - <45<br>45 - <50<br>50 - <55<br>55 - <=54|
|---|---|---|---|---|---|---|
||||||||

0 500 1000 1500 2000 m
Mapa: EMD OpenStreetMap, Escala de impresión 1:40.000, Centro de mapa UTM (south)-WGS84 Zona: 18 Este: 657.313 Norte: 5.468.419
Nuevo AG Zona Sensible al Ruido (NSA)

Modelo de cálculo de ruido: ISO 9613-2 General. Velocidad del viento: 12,0 m/s

Altura sobre el nivel del mar del objeto de línea activo

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-05-2022 15:48 / 7 windPRO