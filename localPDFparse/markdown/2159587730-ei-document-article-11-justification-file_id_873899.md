---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: report
pages: 21
has_toc: False
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 12.4 FICHAS DE CÁLCULO SOFTWARE DE MODELACIÓN
-->

# 12.4 FICHAS DE CÁLCULO SOFTWARE DE MODELACIÓN

PE Coloane

Condiciones de modelación

```
Report: List of model properties
Model: Fase Construcción

Model property

Description Fase Construcción
Responsible Ricardo
Calculation method #-1 | Industrial noise | ISO 9613 |

Created by Ricardo on 05-07-2023
Last accessed by Ricardo on 13-07-2023
Model created using iNoise V2023 rev 1

Day Period 07:00 - 19:00
Evening Period 19:00 - 23:00
Night Period 23:00 - 07:00
Compound period Lden
Value Avg(Day, Evening + 5, Night + 10)

Default terrain level 0

Contour calculation height 1,5

Detail level receiver results Source results

Detail level grid results Group results
Calculation optimization on Yes
Fetching radius [m] 5000
Dynamic Error MarginRemove inner walls Yes

Terrain model Use full DTM

Meteorological correction No meteorological correction
Temperature [K] 293,15
Pressure [kPa] 101,325
Air humidity [%] 60,0
Air absorption [dB/km] 0,03 0,10 0,39 1,23 2,79 4,80 9,25 25,43 87,77
Ground attenuation General method, ground factor = 0,5
Barrier/ground attenuation Avoid overestimating barrier effect
IOA-GPG Valley correction No
IOA-GPG Limit screening No
Max. barrier att. According to ISO 9613-1: 20 / 25
Barrier effect Calculate barrier effect also for direct sight

Max.refl.distanceMax.refl.depth 1

```

iNoise V2023 rev 1 Pro Licensed to MARCELO CONCHA - TEBAL ESTUDIOS E INGENIERIA AMBIENTAL LTDA13-07-2023 18:24:27

PE Coloane

Condiciones de modelación

```
Comments

```

iNoise V2023 rev 1 Pro Licensed to MARCELO CONCHA - TEBAL ESTUDIOS E INGENIERIA AMBIENTAL LTDA13-07-2023 18:24:27

PE Coloane
Propiedades Receptor

```
Model: Fase Construcción

 Fase Construcción - Area

Group: (main group)
Listing of: Receivers, for method Industrial noise - ISO 9613

Name X Y Terrain L HDef. Heights

R1 609434,00 5363944,00 40,00 Relative 1,50
R2 609516,00 5361708,00 29,23 Relative 1,50
R2a 609458,00 5361828,00 24,90 Relative 1,50
R2b 609332,00 5361606,00 34,83 Relative 1,50
R3 609079,00 5361478,00 40,00 Relative 1,50

R4 608798,00 5361853,00 40,00 Relative 1,50
R5 608530,00 5362283,00 40,00 Relative 1,50
R5a 608520,00 5362259,00 40,00 Relative 1,50
R5b 608494,00 5362340,00 40,00 Relative 1,50

```

iNoise V2023 rev 1 Pro Licensed to MARCELO CONCHA - TEBAL ESTUDIOS E INGENIERIA AMBIENTAL LTDA13-07-2023 18:22:45

PE Coloane
Propiedades Maquinaria

```
Model: Fase Construcción

 Fase Construcción - Area

Group: (main group)
Listing of: Point sources, for method Industrial noise - ISO 9613

Name Desc. Height X Y LwTot 63 LwTot 125 LwTot 250 LwTot 1k LwTot 2k LwTot 4k LwTot 8k LwTot Tot

LMT Construcción Línea de Media Tensión 1,50 609282,00 5361945,00 90,90 97,70 98,10 104,90 103,80 99,50 90,80 109,69
Platafor. Construcción plataformas de montaje 1,50 609299,00 5362843,00 102,30 100,40 100,80 105,60 104,10 100,00 90,90 111,57
Fund. Construcción Fundaciones 1,50 609396,00 5362357,00 92,10 99,30 99,80 106,10 105,10 100,00 92,00 111,01
Montaje Montaje Aerogeneradores 1,50 609141,00 5363052,00 87,00 91,60 93,90 101,80 103,00 93,50 82,40 106,99

```

iNoise V2023 rev 1 Pro Licensed to MARCELO CONCHA - TEBAL ESTUDIOS E INGENIERIA AMBIENTAL LTDA 13-07-2023 18:23:41

PE Coloane
Propiedades Maquinaria

```
Model: Fase Construcción

 Fase Construcción - Area

Group: (main group)
Listing of: Point sources, for method Industrial noise - ISO 9613

Name LwTot 500

LMT 101,60

Platafor. 104,80

Fund. 103,40
Montaje 99,10

```

iNoise V2023 rev 1 Pro Licensed to MARCELO CONCHA - TEBAL ESTUDIOS E INGENIERIA AMBIENTAL LTDA 13-07-2023 18:23:41

PE Coloane

Fase Construcción

```
Report: Table of Control
Model: Fase Construcción
Path: C:\Users\Ricardo\Desktop\Tebal\PE Coloane\Modelaciones\iNoise\PE Coloane\
Group: (main group)
Period: Day

Name Description R1_A R2_A R2a_A R2b_A R3_A R4_A R5_A R5a_A R5b_A

Group shps -- -- -- -- -- -- -- -- -LMT Construcción Línea de Media Tensión 22,2 44,2 49,0 43,9 35,9 36,3 30,1 30,1 29,3
Platafor. Construcción plataformas de montaje 36,9 32,2 33,3 31,5 30,4 32,6 34,1 33,8 34,1
Fund. Construcción Fundaciones 26,4 37,6 40,2 36,0 29,9 32,1 30,5 30,3 30,1
Montaje Montaje Aerogeneradores 29,2 20,2 21,5 19,6 18,5 21,7 24,9 24,6 25,2

 Total 38,0 45,3 49,6 44,8 37,8 39,0 37,0 36,8 36,8
 (no category) -- -- -- -- -- -- -- -- - Exceeding -- -- -- -- -- -- -- -- -
All shown dB values are A-weighted

```

iNoise V2023 rev 1 Pro Licensed to MARCELO CONCHA - TEBAL ESTUDIOS E INGENIERIA AMBIENTAL LTDA13-07-2023 18:25:59

PE Coloane

Fase Construcción - Tránsito vehicular

```
Report: Table of Control
Model: Fase Construcción - Tránsito vehicular
Path: C:\Users\Ricardo\Desktop\Tebal\PE Coloane\Modelaciones\iNoise\PE Coloane\
Group: (main group)
Period: Day

Name Description R1_A R2_A R2a_A R2b_A R3_A R4_A R5_A R5a_A R5b_A

Group shps -- -- -- -- -- -- -- -- -Ruta 5 0,4 20,4 19,1 25,1 24,5 17,3 9,7 9,8 9,0

Acceso -4,6 12,3 15,2 13,1 11,6 15,5 8,2 8,2 7,3

 Total 1,6 21,0 20,6 25,4 24,7 19,5 12,0 12,1 11,2
 (no category) -- -- -- -- -- -- -- -- - Exceeding -- -- -- -- -- -- -- -- -
All shown dB values are A-weighted

```

iNoise V2023 rev 1 Pro Licensed to MARCELO CONCHA - TEBAL ESTUDIOS E INGENIERIA AMBIENTAL LTDA13-07-2023 18:27:01

Proyecto: Usuario con licencia:
**PE Coloane** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-07-2023 22:49/3.5.552

**DECIBEL - Resultado principal**

**Cálculo:** Modelación de Ruido

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
Se ha añadido una penalización fijada al ruido de origen de los AGs con tonos puros
Modelo: 5,0 dB(A)
**Altura sobre el nivel del suelo, cuando no hay valores en objeto NSA:**
4,0 m; No permitir reemplazar el modelo de altura con la altura del objeto NSA
**Margen de Incertidumbre:**
0,0 dB; El margen de incertidumbre en NSA tiene prioridad
**Desviación respecto a las exigencias de ruido "oficiales". Negativo es más**
**restrictivo, positivoe s menos restrictivo.:**
0,0 dB(A)

(C) OpenStreetMap contributors, Data OpenStreetMap and contributors, ODbL

Todas las coordenadas estan en
UTM (south)-WGS84 Zona: 18

**AGs**

Escala 1:50.000
Nuevo AG Zona Sensible al Ruido (NSA)

**Tipo de AG** **Datos de ruido**
hacia hacia Sur Z Datos brutos/Descripción Válido Fabricante Modelo de AG Potencia, Diámetro Altura Creador Nombre primera LwaRef Última LwaRef
Este nominal de buje velocidad velocidad
rotor viento de

viento

[m] [kW] [m] [m] [m/s] [dB(A)] [m/s] [dB(A)]
AE01 609.122 5.363.092 16,0 VESTAS V172-7.2 7200 172.0 !... Sí VESTAS V172-7.2-7.200 7.200 172,0 163,0 EMD Level 0 - Measured - PO7200 6,0 98,6 12,0 106,9 h
AE02 609.288 5.362.874 16,0 VESTAS V172-7.2 7200 172.0 !... Sí VESTAS V172-7.2-7.200 7.200 172,0 163,0 EMD Level 0 - Measured - PO7200 6,0 98,6 12,0 106,9 h
AE03 609.400 5.362.557 19,7 VESTAS V172-7.2 7200 172.0 !... Sí VESTAS V172-7.2-7.200 7.200 172,0 163,0 EMD Level 0 - Measured - PO7200 6,0 98,6 12,0 106,9 h
**h) Usados datos de octavas genéricos**
Resultados del cálculo

**Nivel de Sonido**

**Zona Sensible al Ruido (NSA)** **Nivel de Sonido**
Núm. Nombre hacia Este hacia Sur Z Altura de imissión Max Desde AGs

[m] [m] [dB(A)]
R1 Noise sensitive point: User defined (1) 609.434 5.363.944 40,6 4,0 38,1
R2 Noise sensitive point: User defined (2) 609.511 5.361.696 33,3 4,0 38,0
R2a Noise sensitive point: User defined (3) 609.460 5.361.813 33,1 4,0 39,3
R2b Noise sensitive point: User defined (4) 609.332 5.361.606 34,4 4,0 37,2
R3 Noise sensitive point: User defined (5) 609.079 5.361.478 46,5 4,0 35,7
R4 Noise sensitive point: User defined (6) 608.798 5.361.853 54,0 4,0 38,1
R5 Noise sensitive point: User defined (7) 608.530 5.362.283 41,3 4,0 39,3
R5a Noise sensitive point: User defined (8) 608.520 5.362.259 42,6 4,0 39,1
R5b Noise sensitive point: User defined (9) 608.494 5.362.340 35,7 4,0 39,3

**Distancias (m)**

**AG**

NSA AE01 AE02 AE03

R1 907 1080 1387

R2 1449 1199 868

R2a 1323 1075 746

R2b 1501 1269 953

R3 1615 1412 1126

R4 1281 1132 926

R5 1002 961 912

R5a 1028 984 929

R5b 980 957 932

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-07-2023 16:50 / 1 windPRO

Proyecto: Usuario con licencia:
**PE Coloane** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-07-2023 22:49/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** Modelación de Ruido **Modelo de cálculo de ruido:** ISO 9613-2 General
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

**Zona Sensible al Ruido (NSA): R1 Noise sensitive point: User defined (1)**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 907 917 **26,85** 98,6 0,00 70,25 - - 0,00 0,00 AE02 1.080 1.088 **24,99** 98,6 0,00 71,73 - - 0,00 0,00 AE03 1.387 1.394 **22,21** 98,6 0,00 73,89 - - 0,00 0,00 Suma **29,85**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 907 917 **30,44** 102,2 0,00 70,25 - - 0,00 0,00 AE02 1.080 1.088 **28,57** 102,2 0,00 71,73 - - 0,00 0,00 AE03 1.387 1.394 **25,79** 102,2 0,00 73,89 - - 0,00 0,00 Suma **33,43**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 907 917 **33,83** 105,6 0,00 70,25 - - 0,00 0,00 AE02 1.080 1.088 **31,97** 105,6 0,00 71,73 - - 0,00 0,00 AE03 1.387 1.394 **29,19** 105,6 0,00 73,89 - - 0,00 0,00 Suma **36,83**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 907 917 **35,13** 106,9 0,00 70,25 - - 0,00 0,00 AE02 1.080 1.088 **33,27** 106,9 0,00 71,73 - - 0,00 0,00 AE03 1.387 1.394 **30,49** 106,9 0,00 73,89 - - 0,00 0,00 Suma **38,13**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 907 917 **35,13** 106,9 0,00 70,25 - - 0,00 0,00 AE02 1.080 1.088 **33,27** 106,9 0,00 71,73 - - 0,00 0,00 AE03 1.387 1.394 **30,49** 106,9 0,00 73,89 - - 0,00 0,00 Suma **38,13**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-07-2023 16:50 / 1 windPRO

Proyecto: Usuario con licencia:
**PE Coloane** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-07-2023 22:49/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** Modelación de Ruido **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 907 917 **35,13** 106,9 0,00 70,25 - - 0,00 0,00 AE02 1.080 1.088 **33,27** 106,9 0,00 71,73 - - 0,00 0,00 AE03 1.387 1.394 **30,49** 106,9 0,00 73,89 - - 0,00 0,00 Suma **38,13**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 907 917 **35,13** 106,9 0,00 70,25 - - 0,00 0,00 AE02 1.080 1.088 **33,27** 106,9 0,00 71,73 - - 0,00 0,00 AE03 1.387 1.394 **30,49** 106,9 0,00 73,89 - - 0,00 0,00 Suma **38,13**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): R2 Noise sensitive point: User defined (2)**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.449 1.456 **21,71** 98,6 0,00 74,26 - - 0,00 0,00 AE02 1.199 1.207 **23,83** 98,6 0,00 72,64 - - 0,00 0,00 AE03 868 880 **27,29** 98,6 0,00 69,89 - - 0,00 0,00 Suma **29,67**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.449 1.456 **25,30** 102,2 0,00 74,26 - - 0,00 0,00 AE02 1.199 1.207 **27,42** 102,2 0,00 72,64 - - 0,00 0,00 AE03 868 880 **30,88** 102,2 0,00 69,89 - - 0,00 0,00 Suma **33,25**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.449 1.456 **28,69** 105,6 0,00 74,26 - - 0,00 0,00 AE02 1.199 1.207 **30,82** 105,6 0,00 72,64 - - 0,00 0,00 AE03 868 880 **34,27** 105,6 0,00 69,89 - - 0,00 0,00 Suma **36,65**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.449 1.456 **29,99** 106,9 0,00 74,26 - - 0,00 0,00 AE02 1.199 1.207 **32,12** 106,9 0,00 72,64 - - 0,00 0,00 AE03 868 880 **35,58** 106,9 0,00 69,89 - - 0,00 0,00 Suma **37,95**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.449 1.456 **29,99** 106,9 0,00 74,26 - - 0,00 0,00 AE02 1.199 1.207 **32,12** 106,9 0,00 72,64 - - 0,00 0,00 AE03 868 880 **35,58** 106,9 0,00 69,89 - - 0,00 0,00 Suma **37,95**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-07-2023 16:50 / 2 windPRO

Proyecto: Usuario con licencia:
**PE Coloane** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-07-2023 22:49/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** Modelación de Ruido **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.449 1.456 **29,99** 106,9 0,00 74,26 - - 0,00 0,00 AE02 1.199 1.207 **32,12** 106,9 0,00 72,64 - - 0,00 0,00 AE03 868 880 **35,58** 106,9 0,00 69,89 - - 0,00 0,00 Suma **37,95**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.449 1.456 **29,99** 106,9 0,00 74,26 - - 0,00 0,00 AE02 1.199 1.207 **32,12** 106,9 0,00 72,64 - - 0,00 0,00 AE03 868 880 **35,58** 106,9 0,00 69,89 - - 0,00 0,00 Suma **37,95**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): R2a Noise sensitive point: User defined (3)**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.323 1.331 **22,74** 98,6 0,00 73,48 - - 0,00 0,00 AE02 1.075 1.084 **25,03** 98,6 0,00 71,70 - - 0,00 0,00 AE03 746 760 **28,85** 98,6 0,00 68,62 - - 0,00 0,00 Suma **31,05**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.323 1.331 **26,32** 102,2 0,00 73,48 - - 0,00 0,00 AE02 1.075 1.084 **28,61** 102,2 0,00 71,70 - - 0,00 0,00 AE03 746 760 **32,43** 102,2 0,00 68,62 - - 0,00 0,00 Suma **34,63**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.323 1.331 **29,72** 105,6 0,00 73,48 - - 0,00 0,00 AE02 1.075 1.084 **32,01** 105,6 0,00 71,70 - - 0,00 0,00 AE03 746 760 **35,83** 105,6 0,00 68,62 - - 0,00 0,00 Suma **38,03**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.323 1.331 **31,02** 106,9 0,00 73,48 - - 0,00 0,00 AE02 1.075 1.084 **33,31** 106,9 0,00 71,70 - - 0,00 0,00 AE03 746 760 **37,13** 106,9 0,00 68,62 - - 0,00 0,00 Suma **39,33**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.323 1.331 **31,02** 106,9 0,00 73,48 - - 0,00 0,00 AE02 1.075 1.084 **33,31** 106,9 0,00 71,70 - - 0,00 0,00 AE03 746 760 **37,13** 106,9 0,00 68,62 - - 0,00 0,00 Suma **39,33**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-07-2023 16:50 / 3 windPRO

Proyecto: Usuario con licencia:
**PE Coloane** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-07-2023 22:49/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** Modelación de Ruido **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.323 1.331 **31,02** 106,9 0,00 73,48 - - 0,00 0,00 AE02 1.075 1.084 **33,31** 106,9 0,00 71,70 - - 0,00 0,00 AE03 746 760 **37,13** 106,9 0,00 68,62 - - 0,00 0,00 Suma **39,33**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.323 1.331 **31,02** 106,9 0,00 73,48 - - 0,00 0,00 AE02 1.075 1.084 **33,31** 106,9 0,00 71,70 - - 0,00 0,00 AE03 746 760 **37,13** 106,9 0,00 68,62 - - 0,00 0,00 Suma **39,33**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): R2b Noise sensitive point: User defined (4)**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.501 1.507 **21,31** 98,6 0,00 74,56 - - 0,00 0,00 AE02 1.269 1.277 **23,21** 98,6 0,00 73,12 - - 0,00 0,00 AE03 953 964 **26,31** 98,6 0,00 70,68 - - 0,00 0,00 Suma **28,88**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.501 1.507 **24,90** 102,2 0,00 74,56 - - 0,00 0,00 AE02 1.269 1.277 **26,79** 102,2 0,00 73,12 - - 0,00 0,00 AE03 953 964 **29,89** 102,2 0,00 70,68 - - 0,00 0,00 Suma **32,46**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.501 1.507 **28,29** 105,6 0,00 74,56 - - 0,00 0,00 AE02 1.269 1.277 **30,19** 105,6 0,00 73,12 - - 0,00 0,00 AE03 953 964 **33,29** 105,6 0,00 70,68 - - 0,00 0,00 Suma **35,86**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.501 1.507 **29,60** 106,9 0,00 74,56 - - 0,00 0,00 AE02 1.269 1.277 **31,49** 106,9 0,00 73,12 - - 0,00 0,00 AE03 953 964 **34,59** 106,9 0,00 70,68 - - 0,00 0,00 Suma **37,16**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.501 1.507 **29,60** 106,9 0,00 74,56 - - 0,00 0,00 AE02 1.269 1.277 **31,49** 106,9 0,00 73,12 - - 0,00 0,00 AE03 953 964 **34,59** 106,9 0,00 70,68 - - 0,00 0,00 Suma **37,16**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-07-2023 16:50 / 4 windPRO

Proyecto: Usuario con licencia:
**PE Coloane** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-07-2023 22:49/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** Modelación de Ruido **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.501 1.507 **29,60** 106,9 0,00 74,56 - - 0,00 0,00 AE02 1.269 1.277 **31,49** 106,9 0,00 73,12 - - 0,00 0,00 AE03 953 964 **34,59** 106,9 0,00 70,68 - - 0,00 0,00 Suma **37,16**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.501 1.507 **29,60** 106,9 0,00 74,56 - - 0,00 0,00 AE02 1.269 1.277 **31,49** 106,9 0,00 73,12 - - 0,00 0,00 AE03 953 964 **34,59** 106,9 0,00 70,68 - - 0,00 0,00 Suma **37,16**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): R3 Noise sensitive point: User defined (5)**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.615 1.620 **20,48** 98,6 0,00 75,19 - - 0,00 0,00 AE02 1.412 1.417 **22,02** 98,6 0,00 74,03 - - 0,00 0,00 AE03 1.126 1.133 **24,54** 98,6 0,00 72,09 - - 0,00 0,00 Suma **27,44**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.615 1.620 **24,06** 102,2 0,00 75,19 - - 0,00 0,00 AE02 1.412 1.417 **25,60** 102,2 0,00 74,03 - - 0,00 0,00 AE03 1.126 1.133 **28,12** 102,2 0,00 72,09 - - 0,00 0,00 Suma **31,03**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.615 1.620 **27,46** 105,6 0,00 75,19 - - 0,00 0,00 AE02 1.412 1.417 **29,00** 105,6 0,00 74,03 - - 0,00 0,00 AE03 1.126 1.133 **31,52** 105,6 0,00 72,09 - - 0,00 0,00 Suma **34,42**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.615 1.620 **28,76** 106,9 0,00 75,19 - - 0,00 0,00 AE02 1.412 1.417 **30,30** 106,9 0,00 74,03 - - 0,00 0,00 AE03 1.126 1.133 **32,82** 106,9 0,00 72,09 - - 0,00 0,00 Suma **35,73**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.615 1.620 **28,76** 106,9 0,00 75,19 - - 0,00 0,00 AE02 1.412 1.417 **30,30** 106,9 0,00 74,03 - - 0,00 0,00 AE03 1.126 1.133 **32,82** 106,9 0,00 72,09 - - 0,00 0,00 Suma **35,73**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-07-2023 16:50 / 5 windPRO

Proyecto: Usuario con licencia:
**PE Coloane** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-07-2023 22:49/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** Modelación de Ruido **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.615 1.620 **28,76** 106,9 0,00 75,19 - - 0,00 0,00 AE02 1.412 1.417 **30,30** 106,9 0,00 74,03 - - 0,00 0,00 AE03 1.126 1.133 **32,82** 106,9 0,00 72,09 - - 0,00 0,00 Suma **35,73**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.615 1.620 **28,76** 106,9 0,00 75,19 - - 0,00 0,00 AE02 1.412 1.417 **30,30** 106,9 0,00 74,03 - - 0,00 0,00 AE03 1.126 1.133 **32,82** 106,9 0,00 72,09 - - 0,00 0,00 Suma **35,73**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): R4 Noise sensitive point: User defined (6)**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.281 1.286 **23,12** 98,6 0,00 73,19 - - 0,00 0,00 AE02 1.132 1.139 **24,48** 98,6 0,00 72,13 - - 0,00 0,00 AE03 926 935 **26,65** 98,6 0,00 70,41 - - 0,00 0,00 Suma **29,77**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.281 1.286 **26,71** 102,2 0,00 73,19 - - 0,00 0,00 AE02 1.132 1.139 **28,07** 102,2 0,00 72,13 - - 0,00 0,00 AE03 926 935 **30,23** 102,2 0,00 70,41 - - 0,00 0,00 Suma **33,35**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.281 1.286 **30,10** 105,6 0,00 73,19 - - 0,00 0,00 AE02 1.132 1.139 **31,46** 105,6 0,00 72,13 - - 0,00 0,00 AE03 926 935 **33,63** 105,6 0,00 70,41 - - 0,00 0,00 Suma **36,75**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.281 1.286 **31,41** 106,9 0,00 73,19 - - 0,00 0,00 AE02 1.132 1.139 **32,77** 106,9 0,00 72,13 - - 0,00 0,00 AE03 926 935 **34,93** 106,9 0,00 70,41 - - 0,00 0,00 Suma **38,05**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.281 1.286 **31,41** 106,9 0,00 73,19 - - 0,00 0,00 AE02 1.132 1.139 **32,77** 106,9 0,00 72,13 - - 0,00 0,00 AE03 926 935 **34,93** 106,9 0,00 70,41 - - 0,00 0,00 Suma **38,05**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-07-2023 16:50 / 6 windPRO

Proyecto: Usuario con licencia:
**PE Coloane** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-07-2023 22:49/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** Modelación de Ruido **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.281 1.286 **31,41** 106,9 0,00 73,19 - - 0,00 0,00 AE02 1.132 1.139 **32,77** 106,9 0,00 72,13 - - 0,00 0,00 AE03 926 935 **34,93** 106,9 0,00 70,41 - - 0,00 0,00 Suma **38,05**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.281 1.286 **31,41** 106,9 0,00 73,19 - - 0,00 0,00 AE02 1.132 1.139 **32,77** 106,9 0,00 72,13 - - 0,00 0,00 AE03 926 935 **34,93** 106,9 0,00 70,41 - - 0,00 0,00 Suma **38,05**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): R5 Noise sensitive point: User defined (7)**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.002 1.011 **25,79** 98,6 0,00 71,10 - - 0,00 0,00 AE02 961 970 **26,24** 98,6 0,00 70,74 - - 0,00 0,00 AE03 912 922 **26,79** 98,6 0,00 70,30 - - 0,00 0,00 Suma **31,06**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.002 1.011 **29,38** 102,2 0,00 71,10 - - 0,00 0,00 AE02 961 970 **29,83** 102,2 0,00 70,74 - - 0,00 0,00 AE03 912 922 **30,37** 102,2 0,00 70,30 - - 0,00 0,00 Suma **34,65**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.002 1.011 **32,77** 105,6 0,00 71,10 - - 0,00 0,00 AE02 961 970 **33,22** 105,6 0,00 70,74 - - 0,00 0,00 AE03 912 922 **33,77** 105,6 0,00 70,30 - - 0,00 0,00 Suma **38,04**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.002 1.011 **34,07** 106,9 0,00 71,10 - - 0,00 0,00 AE02 961 970 **34,52** 106,9 0,00 70,74 - - 0,00 0,00 AE03 912 922 **35,07** 106,9 0,00 70,30 - - 0,00 0,00 Suma **39,35**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.002 1.011 **34,07** 106,9 0,00 71,10 - - 0,00 0,00 AE02 961 970 **34,52** 106,9 0,00 70,74 - - 0,00 0,00 AE03 912 922 **35,07** 106,9 0,00 70,30 - - 0,00 0,00 Suma **39,35**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-07-2023 16:50 / 7 windPRO

Proyecto: Usuario con licencia:
**PE Coloane** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-07-2023 22:49/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** Modelación de Ruido **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.002 1.011 **34,07** 106,9 0,00 71,10 - - 0,00 0,00 AE02 961 970 **34,52** 106,9 0,00 70,74 - - 0,00 0,00 AE03 912 922 **35,07** 106,9 0,00 70,30 - - 0,00 0,00 Suma **39,35**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.002 1.011 **34,07** 106,9 0,00 71,10 - - 0,00 0,00 AE02 961 970 **34,52** 106,9 0,00 70,74 - - 0,00 0,00 AE03 912 922 **35,07** 106,9 0,00 70,30 - - 0,00 0,00 Suma **39,35**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): R5a Noise sensitive point: User defined (8)**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.028 1.036 **25,52** 98,6 0,00 71,31 - - 0,00 0,00 AE02 984 993 **25,99** 98,6 0,00 70,94 - - 0,00 0,00 AE03 929 939 **26,60** 98,6 0,00 70,45 - - 0,00 0,00 Suma **30,83**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.028 1.036 **29,11** 102,2 0,00 71,31 - - 0,00 0,00 AE02 984 993 **29,58** 102,2 0,00 70,94 - - 0,00 0,00 AE03 929 939 **30,18** 102,2 0,00 70,45 - - 0,00 0,00 Suma **34,42**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.028 1.036 **32,51** 105,6 0,00 71,31 - - 0,00 0,00 AE02 984 993 **32,97** 105,6 0,00 70,94 - - 0,00 0,00 AE03 929 939 **33,58** 105,6 0,00 70,45 - - 0,00 0,00 Suma **37,81**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.028 1.036 **33,81** 106,9 0,00 71,31 - - 0,00 0,00 AE02 984 993 **34,28** 106,9 0,00 70,94 - - 0,00 0,00 AE03 929 939 **34,88** 106,9 0,00 70,45 - - 0,00 0,00 Suma **39,12**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.028 1.036 **33,81** 106,9 0,00 71,31 - - 0,00 0,00 AE02 984 993 **34,28** 106,9 0,00 70,94 - - 0,00 0,00 AE03 929 939 **34,88** 106,9 0,00 70,45 - - 0,00 0,00 Suma **39,12**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-07-2023 16:50 / 8 windPRO

Proyecto: Usuario con licencia:
**PE Coloane** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-07-2023 22:49/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** Modelación de Ruido **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.028 1.036 **33,81** 106,9 0,00 71,31 - - 0,00 0,00 AE02 984 993 **34,28** 106,9 0,00 70,94 - - 0,00 0,00 AE03 929 939 **34,88** 106,9 0,00 70,45 - - 0,00 0,00 Suma **39,12**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 1.028 1.036 **33,81** 106,9 0,00 71,31 - - 0,00 0,00 AE02 984 993 **34,28** 106,9 0,00 70,94 - - 0,00 0,00 AE03 929 939 **34,88** 106,9 0,00 70,45 - - 0,00 0,00 Suma **39,12**

_- Datos no definidos debido al cálculo con datos de octava_

**Zona Sensible al Ruido (NSA): R5b Noise sensitive point: User defined (9)**

Velocidad del viento: 6,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 980 990 **26,03** 98,6 0,00 70,91 - - 0,00 0,00 AE02 957 967 **26,28** 98,6 0,00 70,71 - - 0,00 0,00 AE03 932 943 **26,56** 98,6 0,00 70,49 - - 0,00 0,00 Suma **31,06**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 7,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 980 990 **29,61** 102,2 0,00 70,91 - - 0,00 0,00 AE02 957 967 **29,86** 102,2 0,00 70,71 - - 0,00 0,00 AE03 932 943 **30,14** 102,2 0,00 70,49 - - 0,00 0,00 Suma **34,65**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 8,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 980 990 **33,01** 105,6 0,00 70,91 - - 0,00 0,00 AE02 957 967 **33,26** 105,6 0,00 70,71 - - 0,00 0,00 AE03 932 943 **33,54** 105,6 0,00 70,49 - - 0,00 0,00 Suma **38,05**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 9,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 980 990 **34,31** 106,9 0,00 70,91 - - 0,00 0,00 AE02 957 967 **34,56** 106,9 0,00 70,71 - - 0,00 0,00 AE03 932 943 **34,84** 106,9 0,00 70,49 - - 0,00 0,00 Suma **39,35**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 10,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 980 990 **34,31** 106,9 0,00 70,91 - - 0,00 0,00 AE02 957 967 **34,56** 106,9 0,00 70,71 - - 0,00 0,00 AE03 932 943 **34,84** 106,9 0,00 70,49 - - 0,00 0,00 Suma **39,35**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-07-2023 16:50 / 9 windPRO

Proyecto: Usuario con licencia:
**PE Coloane** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-07-2023 22:49/3.5.552

**DECIBEL - Resultados detallados**

**Cálculo:** Modelación de Ruido **Modelo de cálculo de ruido:** ISO 9613-2 General

Velocidad del viento: 11,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 980 990 **34,31** 106,9 0,00 70,91 - - 0,00 0,00 AE02 957 967 **34,56** 106,9 0,00 70,71 - - 0,00 0,00 AE03 932 943 **34,84** 106,9 0,00 70,49 - - 0,00 0,00 Suma **39,35**

_- Datos no definidos debido al cálculo con datos de octava_

Velocidad del viento: 12,0 m/s
**AG**
Núm. Distancia Distancia de ruido **Calculado** LwA,ref Dc Adiv Aatm Agr Abar Amisc A

[m] [m] **[dB(A)]** [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
AE01 980 990 **34,31** 106,9 0,00 70,91 - - 0,00 0,00 AE02 957 967 **34,56** 106,9 0,00 70,71 - - 0,00 0,00 AE03 932 943 **34,84** 106,9 0,00 70,49 - - 0,00 0,00 Suma **39,35**

_- Datos no definidos debido al cálculo con datos de octava_

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-07-2023 16:50 / 10 windPRO

Proyecto: Usuario con licencia:
**PE Coloane** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-07-2023 22:49/3.5.552

**DECIBEL - Suposiciones para cálculo de ruido**

**Cálculo:** Modelación de Ruido

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
Se ha añadido una penalización fijada al ruido de origen de los AGs con tonos puros
Modelo: 5,0 dB(A)
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

**AG:** VESTAS V172-7.2 7200 172.0 !O!
**Ruido:** Level 0 - Measured - PO7200

Origen Fuente/Fecha Creador Editado
Manufacturer 08-07-2022 EMD 06-10-2022 14:58

Based on Document no.: 0127-1584 V01.

**Datos de Octavas**
Estatus Velocidad del viento LwA,ref Tonos puros 63 125 250 500 1000 2000 4000 8000

[m/s] [dB(A)] [dB] [dB] [dB] [dB] [dB] [dB] [dB] [dB]
De Catálogo AGs 6,0 98,6 Núm Datos genéricos 80,2 87,2 90,6 93,2 93,0 90,1 85,3 75,8
De Catálogo AGs 7,0 102,2 Núm Datos genéricos 83,8 90,8 94,2 96,8 96,6 93,7 88,9 79,4
De Catálogo AGs 8,0 105,6 Núm Datos genéricos 87,2 94,2 97,6 100,2 100,0 97,1 92,3 82,8
De Catálogo AGs 9,0 106,9 Núm Datos genéricos 88,5 95,5 98,9 101,5 101,3 98,4 93,6 84,1
De Catálogo AGs 10,0 106,9 Núm Datos genéricos 88,5 95,5 98,9 101,5 101,3 98,4 93,6 84,1
De Catálogo AGs 11,0 106,9 Núm Datos genéricos 88,5 95,5 98,9 101,5 101,3 98,4 93,6 84,1
De Catálogo AGs 12,0 106,9 Núm Datos genéricos 88,5 95,5 98,9 101,5 101,3 98,4 93,6 84,1

**Zona Sensible al Ruido (NSA): R1 Noise sensitive point: User defined (1)**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): R2 Noise sensitive point: User defined (2)**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): R2a Noise sensitive point: User defined (3)**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): R2b Noise sensitive point: User defined (4)**
**Sin demanda de ruido**

**Sin demanda de distancia**

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-07-2023 10:19 / 1 windPRO

Proyecto: Usuario con licencia:
**PE Coloane** **Tebal Estudios e Ingenieria Ambiental**

Andrés de Fuenzalida 17 Oficina 34 Providencia
CL- Santiago de Chile
+56-2-2222 70 59
Ricardo Martinez / rmartinez@tebal.cl
Calculado:

12-07-2023 22:49/3.5.552

**DECIBEL - Suposiciones para cálculo de ruido**

**Cálculo:** Modelación de Ruido
**Zona Sensible al Ruido (NSA): R3 Noise sensitive point: User defined (5)**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): R4 Noise sensitive point: User defined (6)**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): R5 Noise sensitive point: User defined (7)**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): R5a Noise sensitive point: User defined (8)**
**Sin demanda de ruido**

**Sin demanda de distancia**

**Zona Sensible al Ruido (NSA): R5b Noise sensitive point: User defined (9)**
**Sin demanda de ruido**

**Sin demanda de distancia**

_windPRO 3.5.552 por EMD International A/S, Tel. +45 96 35 44 44, www.emd.dk, windpro@emd.dk_ 13-07-2023 10:19 / 2 windPRO