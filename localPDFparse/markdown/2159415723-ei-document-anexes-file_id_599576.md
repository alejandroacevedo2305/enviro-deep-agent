---
title: Sin título
author: Andrés Burboa Lizama
date: D:20230308125345-03'00'
language: es
type: manual
pages: 37
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01 ESTUDIO DE INUNDACIÓN PARQUE FOTOVOLTAICO LLANOS DE RUNGUE
  - Contenidos
  - Figuras
  - Tablas
  - 1. Introducción
  - 2. Alcances y objetivos
  - 3. Zona de estudio
  - 4. Datos
  - 5. Metodología
  - 6. Resultados
  ... y 3 secciones más
-->

**BAQUA Ingeniería**

www.baqua.cl
contacto@baqua.cl

# ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01 ESTUDIO DE INUNDACIÓN PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

para UKA CHILE y PLAN 8

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
||||||||
|B|-|08/03/2023|Cliente|DMM|BGP|ABL|
|A|-|20/01/2023|Cliente|DMM|ENC|ABL|
|**Rev.**|**Rev. Int.**|**Fecha**|**Emitido para**|**Emitido por**|**Revisado por**|**Aprobado por**|

|Col1|Comuna de Illapel<br>Región de Coquimbo|Col3|
|---|---|---|
|<br>|UKA-B22032-EHID-DOC-01.01|**Rev. B**|

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

# Contenidos

**1.** **Introducción .................................................................................................................... 5**

**2.** **Alcances y objetivos ........................................................................................................ 5**

**3.** **Zona de estudio ............................................................................................................... 6**

3.1. Ubicación general ................................................................................................................................ 6
3.2. Identificación de los cauces ................................................................................................................ 7

**4.** **Datos ............................................................................................................................... 8**

4.1. Estaciones fluviométricas .................................................................................................................. 8

4.2. Estaciones pluviométricas ................................................................................................................. 8
4.3. Modelo de elevación digital .............................................................................................................. 9
4.4. Uso de suelo y clasificación ............................................................................................................... 11

**5.** **Metodología ................................................................................................................... 12**

5.1. Parámetros geomorfométricos ....................................................................................................... 13
5.2. Análisis de frecuencia ........................................................................................................................ 14

5.3. Variabilidad espacial .......................................................................................................................... 16

5.4. Valores IDF ........................................................................................................................................... 16

5.5. Método racional .................................................................................................................................. 18

**6.** **Resultados ..................................................................................................................... 18**

6.1. Parámetros geomorfométricos ....................................................................................................... 18
6.2. Análisis de frecuencia ........................................................................................................................23

6.3. Variabilidad espacial ..........................................................................................................................23

6.4. Valores IDF .......................................................................................................................................... 24

6.5. Método racional .................................................................................................................................. 27

**7.** **Conclusiones y comentarios ........................................................................................... 31**

**8.** **Referencias ..................................................................................................................... 31**

**9.** **Apéndice ........................................................................................................................ 33**

9.1. Series POT ........................................................................................................................................... 33

9.2. Tests de bondad de ajuste .............................................................................................................. 35

ii
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

# Figuras

Figura 3-1: Ubicación y sectores del proyecto .............................................................................................................. 6

Figura 3-2: Cauces del grupo C_01 (celeste) ................................................................................................................. 7

Figura 4-1: Ubicación de estaciones pluviométricas ................................................................................................... 9

Figura 4-2: Representación del modelo de elevación digital (DEM) ..................................................................... 10

Figura 4-3: Representación del modelo digital de terreno (MDT) ..........................................................................11

Figura 4-4: Uso de suelo y clasificación ....................................................................................................................... 12

Figura 5-1. Serie de datos (arriba) y comparación entre una serie POT (izquierda) y una serie AM (derecha).

Modificado de (Chow et al., 1988) ................................................................................................................................ 15

Figura 6-1. Ubicación de las cuencas del grupo de cauces C_01 incluyendo sus cauces principales (celeste) 21

Figura 6-2: Detalle de cuencas del grupo de cauces C_01 incluyendo sus cauces principales (celeste). Ramal

norte .................................................................................................................................................................................. 22

Figura 6-3: Detalle de cuencas del grupo de cauces C_01 incluyendo sus cauces principales (celeste). Ramal

sur ....................................................................................................................................................................................... 22

Figura 6-4. Ráster de precipitación máxima diaria para periodo de retorno de 100 años ................................ 24

Figura 6-5. Curvas IDF para duraciones entre 1 y 24 horas ..................................................................................... 25

Figura 6-6. Curvas IDF para duraciones menores a 1 hora ...................................................................................... 26

# Tablas

Tabla 3-1. Coordenadas representativas del proyecto ............................................................................................... 6

Tabla 3-2. Ubicación del grupo de cauces C_01 según BNA ..................................................................................... 8

Tabla 4-1. Información de las estaciones pluviométricas según DGA ..................................................................... 8

Tabla 5-1. Coeficientes de duración estación Illapel ................................................................................................... 17

Tabla 6-1. Parámetros morfométricos de las cuencas C_01. Parte 1 ..................................................................... 18

Tabla 6-2. Parámetros morfométricos de las cuencas C_01. Parte 2 .....................................................................19

Tabla 6-3. Parámetros morfométricos de las cuencas C_01. Parte 3 .................................................................... 20

Tabla 6-4. Parámetros morfométricos de las cuencas C_01. Parte 4 ................................................................... 20

Tabla 6-5. Precipitación máxima diaria por estación para diferentes periodos de retorno [mm] ................... 23

Tabla 6-6. Precipitación máxima diaria en las cuencas del grupo C_01 ............................................................... 23

Tabla 6-7. Valores IDF para duraciones entre 1 y 24 horas [mm/hora]................................................................. 24

Tabla 6-8. Valores IDF para duraciones menores a 1 hora [mm/hora] ................................................................. 25

Tabla 6-9. Valores IDF para el tiempo de concentración de las cuencas del grupo C_01 [mm/hora]. Parte 1

............................................................................................................................................................................................ 26

Tabla 6-10. Valores IDF para el tiempo de concentración de las cuencas del grupo C_01 [mm/hora]. Parte 2

............................................................................................................................................................................................ 26

iii
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Tabla 6-11. Valores IDF para el tiempo de concentración de las cuencas del grupo C_01 [mm/hora]. Parte 3

............................................................................................................................................................................................ 27

Tabla 6-12. Estimación del coeficiente de escorrentía. Parte 1 ............................................................................... 27

Tabla 6-13. Estimación del coeficiente de escorrentía. Parte 2............................................................................... 27

Tabla 6-14. Estimación del coeficiente de escorrentía. Parte 3 .............................................................................. 28

Tabla 6-15. Estimación del coeficiente de escorrentía. Parte 4 .............................................................................. 28

Tabla 6-16. Estimación del coeficiente de escorrentía. Parte 5 .............................................................................. 28

Tabla 6-17. Estimación del coeficiente de escorrentía. Parte 6 .............................................................................. 28

Tabla 6-18. Amplificación del coeficiente de escorrentía en función del periodo de retorno. Parte 1............. 29

Tabla 6-19. Amplificación del coeficiente de escorrentía en función del periodo de retorno. Parte 2 ............ 29

Tabla 6-20. Amplificación del coeficiente de escorrentía en función del periodo de retorno. Parte 3 ........... 29

Tabla 6-21. Caudal máximo instantáneo con el Método racional [m [3] /s]. Parte 1 ................................................ 30

Tabla 6-22. Caudal máximo instantáneo con el Método racional [m [3] /s]. Parte 2 ............................................... 30

Tabla 6-23. Caudal máximo instantáneo con el Método racional [m [3] /s]. Parte 3 ............................................... 30

Tabla 7-1. Resumen caudal máximo instantáneo [m [3] /s]. Parte 1 ............................................................................ 31

Tabla 7-2. Resumen caudal máximo instantáneo [m [3] /s]. Parte 2 ........................................................................... 31

Tabla 7-3. Resumen caudal máximo instantáneo [m [3] /s]. Parte 3 ........................................................................... 31

Tabla 9-1: Series POT para estaciones Mincha Norte e Illapel DGA ...................................................................... 33

<!-- INICIO TABLA 9-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En las siguientes tablas se presentan las series de duración parcial o POT para las cuatro estaciones utilizadas en el análisis de frecuencia. -->

**Tabla 9-1: Series POT para estaciones Mincha Norte e Illapel DGA**

| ID | Mincha norte | Col3 | Illapel DGA | Col5 |
| --- | --- | --- | --- | --- |
| **ID** | **Fecha** | **Precipitación [mm]** | **Fecha** | **Precipitación [mm]** |
| 1 | 3/6/2002 | 95.0 | 16/8/1997 | 83.0 |
| 2 | 6/8/2015 | 80.0 | 11/5/2017 | 81.0 |
| 3 | 16/8/1997 | 68.0 | 3/6/2002 | 78.0 |
| 4 | 23/6/2000 | 64.0 | 23/6/2000 | 60.0 |
| 5 | 7/6/2006 | 59.0 | 5/6/1992 | 57.0 |
| 6 | 20/5/2003 | 54.0 | 14/6/2000 | 52.0 |
| 7 | 15/8/2008 | 50.0 | 11/6/1997 | 51.0 |
| 8 | 11/6/2014 | 49.5 | 6/8/2015 | 50.0 |
| 9 | 25/6/2017 | 49.0 | 18/7/2001 | 47.5 |
| 10 | 9/5/2017 | 48.0 | 6/7/1996 | 47.0 |
| 11 | 4/7/2018 | 47.0 | 6/5/1993 | 45.0 |
| 12 | 30/7/2001 | 45.0 | 2/6/2016 | 44.5 |
| 13 | 25/7/2006 | 43.0 | 30/8/1992 | 43.0 |
| 14 | 2/6/2016 | 43.0 | 15/8/2008 | 41.5 |
| 15 | 18/7/2001 | 42.5 | 11/6/2014 | 40.5 |
| 16 | 20/6/2011 | 42.0 | 23/7/2002 | 40.0 |
| 17 | 29/8/1992 | 40.5 | 20/7/2002 | 39.0 |
| 18 | 5/6/1992 | 40.0 | 20/5/2003 | 38.0 |
| 19 | 6/7/1996 | 39.1 | 12/7/2015 | 36.0 |
| 20 | 14/6/2000 | 37.5 | 15/7/2011 | 35.5 |
| 21 | 25/5/2002 | 37.0 | 24/6/1992 | 35.0 |
| 22 | 20/7/2004 | 37.0 | 26/5/2002 | 34.5 |
| 23 | 15/7/2011 | 37.0 | 7/6/2006 | 34.5 |
| 24 | 27/5/2013 | 37.0 | 7/6/1992 | 34.0 |

<!-- Estadísticas: 25 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- 33 BAQUA Ingeniería www.baqua.cl -->
<!-- FIN TABLA 9-1 -->


Tabla 9-2: Series POT para estaciones Limahuida y La Canela DMC .................................................................... 34

<!-- INICIO TABLA 9-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |25|27/8/2002|35.5|23/6/1997|34.0| |26|25/8/2001|35.0|16/6/2017|34.0| |27|23/7/2002|35.0|21/4/2004|33.0| |28|13/10/2006|35.0|27/6/2009|33.0| -->

**Tabla 9-2: Series POT para estaciones Limahuida y La Canela DMC**

| ID | Limahuida | Col3 | La Canela DMC | Col5 |
| --- | --- | --- | --- | --- |
| **ID** | **Fecha** | **Precipitación [mm]** | **Fecha** | **Precipitación [mm]** |
| 1 | 3/6/2002 | 86.0 | 16/8/1997 | 90.0 |
| 2 | 10/5/2017 | 76.5 | 10/5/2017 | 81.0 |
| 3 | 6/8/2015 | 68.5 | 20/6/2011 | 63.2 |
| 4 | 12/7/2015 | 65.5 | 5/6/1992 | 63.0 |
| 5 | 23/6/2000 | 65.0 | 3/6/2002 | 60.0 |
| 6 | 15/8/2008 | 65.0 | 6/8/2015 | 56.3 |
| 7 | 18/7/2001 | 62.0 | 18/7/2001 | 54.5 |
| 8 | 2/6/2016 | 62.0 | 12/7/2015 | 53.0 |
| 9 | 5/6/1992 | 50.0 | 20/5/2003 | 48.0 |
| 10 | 16/8/1997 | 48.0 | 15/8/2009 | 46.8 |
| 11 | 14/6/2000 | 48.0 | 16/8/2012 | 46.2 |
| 12 | 30/8/1992 | 46.0 | 23/6/2000 | 43.5 |
| 13 | 20/5/2003 | 46.0 | 11/6/2014 | 42.5 |
| 14 | 21/4/2004 | 46.0 | 4/6/1997 | 42.0 |
| 15 | 11/6/2014 | 44.5 | 14/6/2000 | 41.5 |
| 16 | 24/6/1992 | 44.0 | 7/6/1992 | 39.5 |
| 17 | 26/5/2002 | 44.0 | 15/6/2017 | 39.0 |
| 18 | 20/6/1997 | 41.0 | 6/7/1996 | 37.0 |
| 19 | 11/6/1997 | 40.0 | 13/10/1997 | 37.0 |
| 20 | 23/7/2002 | 40.0 | 30/7/2001 | 36.8 |
| 21 | 7/6/1992 | 38.0 | 25/7/2006 | 35.5 |
| 22 | 20/7/2002 | 38.0 | 13/4/1993 | 35.0 |
| 23 | 16/8/2012 | 37.2 | 2/6/2016 | 34.4 |
| 24 | 30/7/2001 | 36.5 | 21/4/2004 | 34.0 |

<!-- Estadísticas: 25 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- 34 BAQUA Ingeniería www.baqua.cl -->
<!-- FIN TABLA 9-2 -->


Tabla 9-3: Resultados tests de bondad de ajuste para estación Mincha Norte .................................................. 35

<!-- INICIO TABLA 9-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- de esto, en ambos casos se escoge la distribución Generalizada de Pareto, debido a que presenta los menores resultados de estadísticos en todos los tests aplicados. -->

**Tabla 9-3: Resultados tests de bondad de ajuste para estación Mincha Norte**

| Test de<br>bondad | Gamma | Generalizada<br>de Valores<br>Extremos | Generalizada<br>de Pareto | Gumbel | Log-normal | Normal |
| --- | --- | --- | --- | --- | --- | --- |
| KS | 0.175 | 0.099 | 0.084 | 0.160 | 0.164 | 0.210 |
| AD | 0.229 | 0.034 | 0.026 | 0.148 | 0.182 | 0.338 |
| CvM | 1.402 | 0.291 | 0.211 | 0.948 | 1.152 | 1.970 |
| Chi2 | 11.320 | 2.656 | 1.413 | 8.030 | 9.205 | 17.443 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 9-4: Resultados tests de bondad de ajuste para estación Limahuida |Test de<br>bondad|Gamma|Generalizada<br>de Valores<br>Extremos|Generalizada<br>de Pareto|Gumbel|Log-normal|Normal| |---|---|---|---|---|---|---| -->
<!-- FIN TABLA 9-3 -->


Tabla 9-4: Resultados tests de bondad de ajuste para estación Limahuida ....................................................... 35

<!-- INICIO TABLA 9-4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |KS|0.175|0.099|0.084|0.160|0.164|0.210| |AD|0.229|0.034|0.026|0.148|0.182|0.338| |CvM|1.402|0.291|0.211|0.948|1.152|1.970| |Chi2|11.320|2.656|1.413|8.030|9.205|17.443| -->

**Tabla 9-4: Resultados tests de bondad de ajuste para estación Limahuida**

| Test de<br>bondad | Gamma | Generalizada<br>de Valores<br>Extremos | Generalizada<br>de Pareto | Gumbel | Log-normal | Normal |
| --- | --- | --- | --- | --- | --- | --- |
| KS | 0.181 | 0.139 | 0.115 | 0.144 | 0.163 | 0.213 |
| AD | 0.193 | 0.072 | 0.054 | 0.117 | 0.163 | 0.260 |
| CvM | 1.068 | 0.482 | - | 0.704 | 0.923 | 1.400 |
| Chi2 | 6.952 | 3.179 | 3.105 | 4.800 | 5.896 | 9.859 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Para las estaciones Illapel DGA y La Canela DMC, se obtiene lo expuesto en la Tabla 9-5 y la Tabla 9-6. En estos casos, se escoge la distribución Generalizada de Valores Extremos, debido a que presenta los menores -->
<!-- FIN TABLA 9-4 -->


Tabla 9-5: Resultados tests de bondad de ajuste para estación Illapel DGA ...................................................... 36

<!-- INICIO TABLA 9-5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01 ESTUDIO DE INUNDACIÓN PARQUE FOTOVOLTAICO LLANOS DE RUNGUE -->

**Tabla 9-5: Resultados tests de bondad de ajuste para estación Illapel DGA**

| Test de<br>bondad | Gamma | Generalizada<br>de Valores<br>Extremos | Generalizada<br>de Pareto | Gumbel | Log-normal | Normal |
| --- | --- | --- | --- | --- | --- | --- |
| KS | 0.150 | 0.099 | 0.107 | 0.150 | 0.136 | 0.179 |
| AD | 0.206 | 0.045 | 0.027 | 0.135 | 0.164 | 0.307 |
| CvM | 1.435 | 0.408 | 0.297 | 0.974 | 1.188 | 2.008 |
| Chi2 | 9.569 | 2.237 | 1.029 | 6.881 | 7.648 | 15.096 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 9-6: Resultados tests de bondad de ajuste para estación La Canela DMC |Test de<br>bondad|Gamma|Generalizada<br>de Valores<br>Extremos|Generalizada<br>de Pareto|Gumbel|Log-normal|Normal| |---|---|---|---|---|---|---| -->
<!-- FIN TABLA 9-5 -->


Tabla 9-6: Resultados tests de bondad de ajuste para estación La Canela DMC ............................................... 36

<!-- INICIO TABLA 9-6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |KS|0.150|0.099|0.107|0.150|0.136|0.179| |AD|0.206|0.045|0.027|0.135|0.164|0.307| |CvM|1.435|0.408|0.297|0.974|1.188|2.008| |Chi2|9.569|2.237|1.029|6.881|7.648|15.096| -->

**Tabla 9-6: Resultados tests de bondad de ajuste para estación La Canela DMC**

| Test de<br>bondad | Gamma | Generalizada<br>de Valores<br>Extremos | Generalizada<br>de Pareto | Gumbel | Log-normal | Normal |
| --- | --- | --- | --- | --- | --- | --- |
| KS | 0.155 | 0.111 | 0.115 | 0.159 | 0.143 | 0.182 |
| AD | 0.169 | 0.047 | 0.029 | 0.107 | 0.137 | 0.247 |
| CvM | 1.099 | 0.397 | 0.293 | 0.747 | 0.916 | 1.545 |
| Chi2 | 5.522 | 0.789 | 0.535 | 3.411 | 4.189 | 9.508 |

<!-- Estadísticas: 4 filas, 7 columnas -->
<!-- Contexto posterior: -->
<!-- 36 BAQUA Ingeniería www.baqua.cl -->
<!-- FIN TABLA 9-6 -->


iv
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

# 1. Introducción

El proyecto Parque Fotovoltaico Llanos de Rungue consiste en un Parque Fotovoltaico (PF) que se ubicará

en la comuna de Illapel, Región de Coquimbo. El proyecto posee un área de generación, pero no incluye una

Línea de Transmisión, puesto que utilizará la Línea de transmisión Pan de Azúcar - Punta Sierra - Centella,

que se ubicará prácticamente sobre el área de generación del Parque.

El PF se encuentra dividido en ocho sectores ubicados en la ribera norte del Río Choapa, con superficies que

varían entre 5 y 128 hectáreas, sumando en total unas 356 hectáreas.

En el contexto de la evaluación ambiental del proyecto, se ha desarrollado un Estudio de inundación que

considera los cauces más relevantes de la zona de interés. Este estudio se divide en dos grandes partes: (1)

un Análisis hidrológico, donde se estiman caudales de crecida, y (2) un Modelo hidráulico, que incluye

resultados de superficie inundada, profundidad y velocidad del flujo.

A su vez, el Estudio de inundación fue dividido por cauce o conjuntos de cauces que fuera posible reunir en

un mismo modelo hidráulico. Estos conjuntos de cauces han sido nombrados con un ID correlativo. La misma

notación se ha utilizado para las cuencas asociadas a dichos cauces.

A continuación, se presenta el Análisis hidrológico del grupo de cauces C_01.

# 2. Alcances y objetivos

Se elaboró el Análisis hidrológico del grupo de cauces denominado C_01 que se ubica en la zona de estudio

del proyecto Parque Fotovoltaico Llanos de Rungue, atendiendo los requerimientos señalados en el

reglamento del Sistema de Evaluación de Impacto Ambiental (reglamento SEIA; Decreto 40, año 2013), la

Guía “Permiso para efectuar modificaciones de cauce” (SEA & DGA, 2014), llamada Guía PAS 156, y la Guía

“Permiso obras de regularización y defensa de cauces naturales” (SEA, DGA, & DOH, 2014), denominada

Guía PAS 157.

Se desarrollaron los contenidos hidrológicos necesarios para estimar las zonas de inundación, lo que

permitirá evaluar el requerimiento de posibles PAS 156 y PAS 157 asociados a las obras del proyecto, con el

objetivo de recibir el pronunciamiento favorable del Servicio de Evaluación Ambiental (SEA) y de la Dirección

General de Aguas (DGA). En concreto, se han determinado los caudales máximos instantáneos

correspondientes a los periodos de retorno indicados en la Guía PAS 157, cuya exigencia es mayor en este

sentido respecto a la Guía PAS 156.

5
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

# 3. Zona de estudio

## 3.1. Ubicación general

El proyecto Parque Fotovoltaico Llanos de Rungue se ubica en la comuna de Illapel, en la Región de

Coquimbo. En particular, el sector del PF se encuentra a aproximadamente 5 kilómetros al sureste de la

localidad de Mincha.

La Figura 3-1 muestra en cartografía la ubicación del proyecto y la delimitación de los ocho sectores del

proyecto. La Tabla 3-1 muestra la coordenada del centroide de cada sector del PF.

Figura 3-1: Ubicación y sectores del proyecto

Tabla 3-1. Coordenadas representativas del proyecto

6

|Sector|Este [m]|Norte [m]|CRS (*)|
|---|---|---|---|
|1|274 444.6|6 500 605.4|UTM WGS84 H19 S|
|2|273 534.6|6 500 292.8|UTM WGS84 H19 S|
|3|273 403.5|6 499 821.2|UTM WGS84 H19 S|

BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

|Sector|Este [m]|Norte [m]|CRS (*)|
|---|---|---|---|
|4|274 765.7|6 499 716.5|UTM WGS84 H19 S|
|5|275 249.3|6 500 878.2|UTM WGS84 H19 S|
|6|275 562.5|6 500 543.3|UTM WGS84 H19 S|
|7|275 794.2|6 500 667.0|UTM WGS84 H19 S|
|8|275 965.5|6 499 129.6|UTM WGS84 H19 S|

(*) Coordinate reference system

## 3.2. Identificación de los cauces

La red hidrográfica en el área del proyecto está formada por diferentes cauces, entre los que destaca el Río

Choapa, la Quebrada Atelcura y el Estero Millahue; además de varios cauces sin nombre que son afluentes

a los anteriores.

De igual forma, el grupo de cauces C_01 se encuentra al sur de la Quebrada Atelcura y es tributario del Río

Choapa. Las cuencas pertenecientes a este grupo poseen superficies que varían entre los 0.05 km [2] y los 9.60

km [2], aproximadamente. Se generó la red de drenaje del grupo de cauces C_01 a partir de un Modelo de

Elevación Digital y se obtuvo lo siguiente:

Figura 3-2: Cauces del grupo C_01 (celeste)

De acuerdo con la delimitación oficial de la Dirección General de Aguas (DGA) y su Banco Nacional de Aguas

(BNA), la ubicación del grupo de cauces C_01 es:

7
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Tabla 3-2. Ubicación del grupo de cauces C_01 según BNA

|División|Nombre|Código|
|---|---|---|
|Cuenca|Río Choapa|047|
|Subcuenca|Rio Choapa Bajo (entre Rio Illapel y Desembocadura)|0473|
|Subsubcuenca|Rio Choapa Entre Rio Illapel y Estero Canela|04730|

# 4. Datos

## 4.1. Estaciones fluviométricas

Las estaciones fluviométricas más cercanas son Río Choapa Aguas Arriba Estero La Canela (código BNA

04730001-0), con una cuenca aportante de unos 350 km [2], y Rio Illapel en el Peral (código BNA 04726001
9), con una cuenca de 220 km [2], aproximadamente. Tomando en cuenta el gran tamaño de estas cuencas en

comparación a las de los cauces de interés, se descartó su uso.

## 4.2. Estaciones pluviométricas

Se escogieron 4 estaciones pluviométricas en un radio de 25 km alrededor del proyecto. La ubicación de las

estaciones y su información general se presenta a continuación:

Tabla 4-1. Información de las estaciones pluviométricas según DGA

|Nombre estación|Código BNA|Coordenadas (*)|Col4|Fecha|Col6|
|---|---|---|---|---|---|
|**Nombre estación**|**Código BNA**|**Este [m]**|**Norte [m]**|**Inicio**|**Fin**|
|Illapel DGA|04726003-5|293 094|6 497 017|1974|2020|
|La Canela DMC|04732001-1|266 445|6 523 752|1974|2020|
|Limahuida|04716005-7|294 965|6 485 124|1964|2020|
|Mincha Norte|04730004-5|267 509|6 502 706|1973|2020|

(*) UTM WGS84 H 19 S

Si bien la información entregada por la DGA indica que todas las estaciones seleccionadas cuentan con datos

al menos desde el año 1974, se selecciona el rango desde el 1992 hasta el 2019, dado que corresponde al

periodo con mayor cantidad de información. Nótese que la estación Río Illapel en el Peral (código BNA

04726001-9) se encuentra dentro del radio seleccionado, específicamente a 13 km del centroide del PF pero

se descartó su uso debido a que solo cuenta con datos desde el año 2012.

La Figura 4-1 muestra la ubicación de las estaciones pluviométricas seleccionadas.

8
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Figura 4-1: Ubicación de estaciones pluviométricas

## 4.3. Modelo de elevación digital

Se utilizaron dos fuentes de información de elevación de terreno: (i) un modelo de elevación digital (DEM,

en inglés), en formato ráster, del producto ALOS PALSAR RTC (ASF DAAC, 2011), cuya resolución espacial

es de 12.5 m, y (ii) un modelo digital de terreno (MDT), también en formato ráster, que fue proporcionado

por el cliente y cuya resolución es de 2.0 m.

La representación del DEM y el MDT se muestra a continuación:

9
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Figura 4-2: Representación del modelo de elevación digital (DEM)

10
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Figura 4-3: Representación del modelo digital de terreno (MDT)

En la gran mayoría de los casos se delimitó las cuencas utilizando el MDT, ya que el tamaño de ellas es

pequeño y son contenidas completamente por este ráster. En los casos que no fuera efectivo lo anterior, se

complementó la delimitación del MDT con la del DEM.

## 4.4. Uso de suelo y clasificación

La información del uso y cobertura de suelo (LULC, en inglés) se obtuvo a partir de un archivo en formato

ráster del producto “Sentinel-2 land cover time series 2017-2021” (Karra, y otros, 2021), cuya resolución

espacial es de 10 m y se extiende por sobre toda el área de estudio. La representación del uso de suelo se

muestra en la siguiente figura:

11
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Figura 4-4: Uso de suelo y clasificación

# 5. Metodología

No existen estaciones fluviométricas representativas de la zona de estudio, por lo tanto, se estimaron los

caudales máximos mediante métodos indirectos del tipo precipitación-escorrentía.

En este caso, solo se puede utilizar el método racional, ya que las cuencas no poseen el tamaño suficiente

para la aplicación de otras técnicas, tal como se señala en el “Manual de cálculo de crecidas” de la DGA (1995),

donde los métodos convencionales son válidos para cuencas con superficie mayor a 20 km [2], o en la “Guía

metodológica para proyectos de modificación de cauce” (DGA, 2016), donde se recomienda el método

racional para cuencas menores a 20 km [2] .

El análisis está enfocado en las cuencas que conforman el grupo de cauces C_01, estimando los caudales

máximos instantáneos con periodos de retorno de 2, 5, 10, 25, 50, 100 y 200 años.

La metodología empleada para la estimación de los caudales se presenta a continuación.

12
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

## 5.1. Parámetros geomorfométricos

Las cuencas se delimitaron mediante el programa QGIS, utilizando los MDT y DEM mencionados antes, cuya

resolución espacial es de 2.0 y 12.5 m, respectivamente.

Con este DEM se determinaron los principales parámetros morfométricos de la cuenca, tales como su

superficie, longitud del cauce principal, cota máxima y mínima y pendiente media.

Además, en el caso del método racional se debe estimar el tiempo de concentración de la cuenca. Para ello,

se utilizaron las expresiones de Normas Españolas, California Culverts Practice y Giandotti (MOP, 2020),

junto a las expresiones de Bransby Williams (Maidment, 1993) y del SCS (NRCS, 2010).

t c1 = 18 ∙ S [L] [0.76][0.19] (1)

t c2 = 57 ∙( [L] H [3] ~~[)]~~

0.385

t c3 = 60 ∙ [4 ∙] ~~[√]~~ [A+ 1.5 ∙L]

0.8 ∙ ~~√~~ H media

(2)

(3)

t c4 = 21.3 ∙L⋅A [−0.1] ⋅S [−0.2] (4)

t c5 = 60 ∙ [L] [0.8] 1140 ⋅S [ ⋅(S] [′] [ + 1)] [0.5] [0.7] (5)

Donde:

t cX : tiempo de concentración según (1) Normas Españolas,

(2) California Culverts Practice, (3) Giandotti,

(4) Bransby Williams y (5) SCS [minutos]

L : longitud del cauce principal [km], [mi], [ft]

S : pendiente media de la cuenca [m/m], [ft/ft], [%]

A : área de la cuenca [km [2] ], [mi [2] ]

H medio : desnivel medio de la cuenca [m]

S′ : retención potencial del método de curva número [-]

13
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Las expresiones de Normas Españolas, California Culverts Practice y Giandotti utilizan unidades de [km],

[m/m] y [km [2] ]. En cambio, Bransby Williams emplea [mi], [ft/ft] y [mi [2] ], mientras que SCS utiliza [ft] y [%],

sin unidades de área.

Por último, la expresión del SCS utiliza la retención potencial proveniente del método de curva número. Para

calcular el valor de curva número (CN) se utilizó la información de uso de suelos mencionada en el capítulo

anterior. Se asignó un valor de CN para cada clasificación de suelo (Chow, Maidment, & Mays, 1988) y se

calculó el valor de cada cuenca como una media ponderada sobre su superficie.

Nótese que la expresión del SCS posee algunas inconsistencias en la forma presentada en fuentes como el

Manual de Carreteras (MOP, 2020), así que se optó por presentarla en una versión más cercana a la fuente

original (NRCS, 2010).

## 5.2. Análisis de frecuencia

Se utilizó un enfoque de duración parcial (Chow, Maidment, & Mays, 1988; Maidment, 1993), también

llamado de máximos sobre umbral (peaks over threshold o POT, en inglés). Su principal diferencia con una

serie de máximos anuales (AM, en inglés) radica en que una serie POT no ignora el segundo o tercer valor

más alto de un mismo año (que podría ser mayor al máximo de otro año). Este enfoque representa de forma

más acertada la definición teórica de periodo de retorno como un intervalo medio de recurrencia entre

eventos. La Figura 5-1 muestra un ejemplo con la diferencia entre ambas series:

14
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Figura 5-1. Serie de datos (arriba) y comparación entre una serie POT (izquierda) y una serie AM (derecha).

Modificado de (Chow et al., 1988)

Para las cuatro estaciones ya mencionadas, se seleccionó un periodo de 28 años de datos comprendidos

entre 1992 a 2019. Por otra parte, para la selección de los máximos se definió un criterio de independencia,

o periodo seco, entre tormentas de 24 horas, con el objetivo de no mezclar eventos que pudieran ser

dependientes entre sí.

En función de lo anterior se generaron series POT de 28 máximos para cada estación. A cada una de estas

series se ajustó las siguientes distribuciones de probabilidad:

 - Gamma - Gumbel

 - Generalizada de Valores Extremos - Log-Normal

 - Generalizada de Pareto - Normal

Se evaluó la bondad de ajuste de cada distribución comparando los estadísticos de Kolmogórov-Smirnov

(KS), Anderson-Darling (AD), Cramér-von Mises (CvM) y Chi Cuadrado (chi2). Luego, se seleccionó la

distribución con mejor ajuste, como aquella con el estadístico de valor más bajo. Con la distribución escogida

se calculó la precipitación máxima diaria para periodos de retorno entre 2 y 200 años.

15
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

## 5.3. Variabilidad espacial

Se interpoló espacialmente los resultados del análisis de frecuencia de las cuatro estaciones pluviométricas

mediante un método de interpolación de spline bicúbica, utilizando nuevamente el programa QGIS. Como

resultado de esta interpolación se obtuvo un ráster de precipitación máxima diaria para cada uno de los

periodos de retorno.

Aunque existen métodos de interpolación que pueden ser más adecuados para trabajar con datos de

precipitación (como el kriging o el co-kriging), se optó por la spline porque su aplicación es más simple y en

general entrega un resultado un poco más conservador (valores de precipitación levemente mayores dentro

de la zona de estudio).

A diferencia de los cálculos de parámetros geomorfométricos, donde se entrega un valor para cada cuenca

del grupo, en este caso se obtuvo valores únicos de precipitación para el grupo de cauces completo, ya que

la variación de la precipitación dentro de un mismo grupo era mínima. De esta forma, se unificó las cuencas

en una sola zona y se calculó la media espacial de cada ráster de precipitación sobre dicha área.

## 5.4. Valores IDF

Los valores de intensidad-duración-frecuencia (IDF) se estimaron a partir de los coeficientes de duración y

frecuencia presentes en la literatura, utilizando la siguiente expresión (MOP, 2020):

T = K∙CD d ∙CF T ∙P D

P d

10 (6)

Donde:

P dT : precipitación con periodo de retorno T años y duración d horas [mm]

K : coeficiente de ajuste entre la precipitación máxima diaria y la

precipitación máxima en 24 horas continuas [-]

CD d : coeficiente de duración para d horas [-]

CF [T] : coeficiente de frecuencia para T años [-]

P D10 : precipitación diaria con periodo de retorno 10 años [mm]

En el caso del método racional, la duración de interés debe ser igual al tiempo de concentración de la cuenca.

Dado que las cuencas son de menor tamaño, es probable que su tiempo de concentración será menor a una

hora, en cuyo caso se utiliza además la expresión de Bell (MOP, 2020):

16
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

T = (0.54 ∙d 0.25 −0.5) ∙(0.21 ∙ln(T) + 0.52) ∙P 1

P d

10 (7)

Donde:

P dT : precipitación con periodo de retorno T años y duración d minutos [mm]

P 110 : precipitación con periodo de retorno 10 años y duración 1 hora [mm]

Sin embargo, en este caso no se necesitan cálculos asociados a la frecuencia de la precipitación, ya que se

cuenta con el análisis de frecuencia completo para diferentes periodos de retorno. Por lo tanto, las

ecuaciones (6) y (7) se simplifican de la siguiente forma:

T = K∙CD d ∙P DT

P d

T

D (8)

T 0.25
= (0.54 ∙d −0.5) ∙P 1

P d

T (9)

T es la precipitación diaria con periodo de retorno T años y P 1

Donde P DT

T es la precipitación en 1 hora con

periodo de retorno T años. En este caso, se utilizaron los coeficientes de duración de la estación Illapel entre

1 y 24 horas (MOP, 2020).

Tabla 5-1. Coeficientes de duración estación Illapel

1 0.14 10 0.73

2 0.25 12 0.79

4 0.41 14 0.84

6 0.54 18 0.92

8 0.66 24 1.00

|Duración<br>[horas]|CD<br>d<br>[-]|
|---|---|
|1|0.14|
|2|0.25|
|4|0.41|
|6|0.54|
|8|0.66|

|Duración<br>[horas]|CD<br>d<br>[-]|
|---|---|
|10|0.73|
|12|0.79|
|14|0.84|
|18|0.92|
|24|1.00|

Por último, la intensidad de precipitación i dT queda definida por:

dT = P d

i d

T /d (10)

donde d se mide en horas.

17
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

## 5.5. Método racional

Este método ha sido ampliamente utilizado en hidrología, siendo su principal característica la suposición de

una proporcionalidad directa entre la escorrentía y el agua caída. El caudal máximo según el método racional

queda definido por la expresión (MOP, 2020):

Q=

C∙i tT c ∙A (11)

3.6

Donde:

Q : caudal máximo instantáneo [m [3] /s]

C : coeficiente de escorrentía adimensional [-]

i tT c : intensidad de precipitación con periodo de retorno T

y duración igual al tiempo de concentración t c [mm/hora]

A : área pluvial de la cuenca [km [2] ]

La intensidad asociada al tiempo de concentración se obtiene a partir de las ecuaciones (8), (9) y (10). Por

otra parte, el coeficiente de escorrentía se calcula según el método propuesto en el Manual de Carreteras

(MOP, 2020) que examina 4 factores que influyen en su magnitud (relieve, infiltración, vegetación y

capacidad de almacenamiento), sumando las contribuciones de cada uno.

Se recomienda el uso del método racional en cuencas con una superficie menor a 20 km [2] (DGA, 2016).

# 6. Resultados

## 6.1. Parámetros geomorfométricos

Se delimitaron las cuencas asociadas al grupo de cauces C_01 Los parámetros geomorfométricos de las

cuencas son los siguientes:

Tabla 6-1. Parámetros morfométricos de las cuencas C_01. Parte 1

|Parámetro|Símbolo|Unidad|C_01_00|C_01_01|C_01_02|C_01_03|C_01_04|
|---|---|---|---|---|---|---|---|
|Superficie|A|km2|9.59|1.95|1.72|0.34|0.97|
|Longitud del cauce principal|L|km|7.53|3.74|2.95|1.23|2.15|
|Cota mínima|zmin|msnm|137.0|133.1|184.2|217.5|217.2|

18
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

|Parámetro|Símbolo|Unidad|C_01_00|C_01_01|C_01_02|C_01_03|C_01_04|
|---|---|---|---|---|---|---|---|
|Cota máxima|zmax|msnm|926.0|304.2|304.2|258.8|304.2|
|Cota media|zmedia|msnm|384.4|234.6|240.3|234.0|250.6|
|Pendiente media|S|m/m|0.252|0.082|0.057|0.028|0.054|
|Desnivel máximo|Hmax|m|789.0|171.1|120.0|41.3|87.0|
|Desnivel medio|Hmedio|m|247.4|101.5|56.1|16.5|33.3|
|Tiempo de concentración|tc1|minutos|108.4|78.8|70.4|41.6|56.1|
|Tiempo de concentración|tc2|minutos|45.0|36.1|31.4|17.3|24.7|
|Tiempo de concentración|tc3|minutos|112.9|83.4|96.8|77.2|93.1|
|Tiempo de concentración|tc4|minutos|31.9|28.7|27.4|18.5|56.4|
|Tiempo de concentración|tc5|minutos|115.5|84.2|72.1|41.0|71.5|
|Tiempo de concentración|tc|minutos|112.0|84.4|71.3|41.3|56.2|
|Curva número|CN|-|77.0|77.0|77.0|77.0|77.0|

Tabla 6-2. Parámetros morfométricos de las cuencas C_01. Parte 2

|Parámetro|Símbolo|Unidad|C_01_05|C_01_06|C_01_07|C_01_08|C_01_09|
|---|---|---|---|---|---|---|---|
|Superficie|A|km2|0.43|0.11|7.29|6.71|0.38|
|Longitud del cauce principal|L|km|1.06|0.36|6.99|6.07|0.92|
|Cota mínima|zmin|msnm|240.1|262.0|169.0|204.0|200.3|
|Cota máxima|zmax|msnm|304.2|304.2|926.0|926.0|283.2|
|Cota media|zmedia|msnm|265.1|279.3|424.2|440.5|247.5|
|Pendiente media|S|m/m|0.063|0.076|0.299|0.307|0.138|
|Desnivel máximo|Hmax|m|64.1|42.1|757.0|722.0|83.0|
|Desnivel medio|Hmedio|m|25.0|17.3|255.2|236.5|47.3|
|Tiempo de concentración|tc1|minutos|31.9|13.4|99.2|88.7|24.6|
|Tiempo de concentración|tc2|minutos|12.3|4.1|41.9|36.3|9.5|
|Tiempo de concentración|tc3|minutos|63.4|33.5|99.9|94.9|41.8|
|Tiempo de concentración|tc4|minutos|12.1|4.8|28.2|25.1|8.0|
|Tiempo de concentración|tc5|minutos|29.3|10.9|106.5|92.7|22.0|
|Tiempo de concentración|tc|minutos|33.0|12.9|102.9|90.7|23.1|
|Curva número|CN|-|77.0|77.0|77.0|77.0|77.0|

19
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Tabla 6-3. Parámetros morfométricos de las cuencas C_01. Parte 3

|Parámetro|Símbolo|Unidad|C_01_10|C_01_11|C_01_12|C_01_13|C_01_14|
|---|---|---|---|---|---|---|---|
|Superficie|A|km2|0.07|5.81|0.08|0.04|5.55|
|Longitud del cauce principal|L|km|0.64|4.99|0.42|0.17|4.49|
|Cota mínima|zmin|msnm|255.0|230.0|211.4|235.2|242.0|
|Cota máxima|zmax|msnm|283.2|926.0|263.2|263.2|926.0|
|Cota media|zmedia|msnm|270.1|468.4|246.3|252.8|477.9|
|Pendiente media|S|m/m|0.062|0.332|0.120|0.081|0.341|
|Desnivel máximo|Hmax|m|28.1|696.0|51.9|28.0|684.0|
|Desnivel medio|Hmedio|m|15.0|238.4|34.9|17.6|235.9|
|Tiempo de concentración|tc1|minutos|21.8|75.3|14.0|7.4|69.2|
|Tiempo de concentración|tc2|minutos|9.5|29.4|4.6|2.0|26.2|
|Tiempo de concentración|tc3|minutos|38.8|83.2|22.0|19.6|78.9|
|Tiempo de concentración|tc4|minutos|8.3|20.9|4.6|2.6|19.1|
|Tiempo de concentración|tc5|minutos|21.4|76.2|12.2|5.5|68.5|
|Tiempo de concentración|tc|minutos|22.9|75.8|13.0|10.0|68.8|
|Curva número|CN|-|77.0|77.0|77.0|77.0|77.0|

Tabla 6-4. Parámetros morfométricos de las cuencas C_01. Parte 4

|Parámetro|Símbolo|Unidad|C_01_15|C_01_16|
|---|---|---|---|---|
|Superficie|A|km2|3.41|3.26|
|Longitud del cauce principal|L|km|3.71|3.15|
|Cota mínima|zmin|msnm|241.8|269.0|
|Cota máxima|zmax|msnm|902.7|902.7|
|Cota media|zmedia|msnm|517.4|529.1|
|Pendiente media|S|m/m|0.435|0.446|
|Desnivel máximo|Hmax|m|660.9|633.8|
|Desnivel medio|Hmedio|m|275.6|260.1|
|Tiempo de concentración|tc1|minutos|57.1|50.2|
|Tiempo de concentración|tc2|minutos|21.3|17.9|
|Tiempo de concentración|tc3|minutos|58.5|55.6|
|Tiempo de concentración|tc4|minutos|15.0|13.1|
|Tiempo de concentración|tc5|minutos|56.6|48.1|
|Tiempo de concentración|tc|minutos|56.8|49.1|

20
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

|Parámetro|Símbolo|Unidad|C_01_15|C_01_16|
|---|---|---|---|---|
|Curva número|CN|-|77.0|77.0|

Debido a las diferencias entre algunos métodos y la similitud de otros, se definió el tiempo de concentración

de la cuenca como el promedio entre las expresiones de Normas Españolas, Bransby Williams y SCS,

denominado t c, con un valor mínimo de 10 minutos. No obstante, en los casos donde la desviación estándar

entre las tres expresiones recién mencionadas fuera elevada, se utiliza solo el promedio entre Normas

Españolas y Bransby Williams, dado que, para esos casos, el método SCS entrega tiempos de concentración

mayores. A continuación, se presenta la ubicación de las cuencas pertenecientes al grupo C_01:

Figura 6-1. Ubicación de las cuencas del grupo de cauces C_01 incluyendo sus cauces principales (celeste)

Nótese que la cuenca C_01_14 contiene a la cuenca C_01_15, la que a su vez contiene a la C_01_16; la cuenca

C_01_12 incluye en su extensión a la C_01_13; y la cuenca C_01_09 incluye la C_09_10. Todas las anteriores

están incluidas en la cuenca C_01_08, la cual está incluida en la C_01_07.

21
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Figura 6-2: Detalle de cuencas del grupo de cauces C_01 incluyendo sus cauces principales (celeste). Ramal

norte

Por el ramal sur del grupo, la cuenca C_01_06 está incluida en la C_01_05, y esta última está incluida en la

C_01_04. Hacia aguas abajo de esta rama, la cuenca C_01_02 incluye a las cuencas C_01_03 y C_01_04, y

está a su vez incluida en la C_01_01. Finalmente, la cuenca C_01_00 incluye a todas las cuencas del grupo.

Figura 6-3: Detalle de cuencas del grupo de cauces C_01 incluyendo sus cauces principales (celeste). Ramal

sur

22
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

## 6.2. Análisis de frecuencia

Se ajusto las distribuciones de probabilidad a las cuatro estaciones meteorológicas, obteniendo las siguientes

precipitaciones máximas:

Tabla 6-5. Precipitación máxima diaria por estación para diferentes periodos de retorno [mm]

|Nombre Estación|Periodo de retorno T [años]|Col3|Col4|Col5|Col6|Col7|Col8|
|---|---|---|---|---|---|---|---|
|**Nombre Estación**|**2 **|**5 **|**10**|**25**|**50**|**100**|**200**|
|Illapel DGA|41.34|52.28|62.00|78.08|93.54|112.68|136.44|
|La Canela DMC|42.35|53.66|63.38|78.99|93.56|111.16|132.47|
|Limahuida|45.12|59.62|69.51|81.30|89.34|96.69|103.41|
|Mincha Norte|42.16|54.34|64.94|81.05|95.06|110.86|128.68|

A partir de la comparación de los estadísticos de los tests aplicados, se deduce que las estaciones Illapel DGA

y La Canela DMC presentaron un mejor ajuste con la distribución Generalizada de Valores Extremos,

mientras que Limahuida y Mincha Norte presentaron un mejor ajuste con la distribución Generalizada de

Pareto. Para más detalles, las series POT para cada estación y los valores de los estadísticos de cada test se

presentan en la Sección 9.1 y 9.2, respectivamente.

## 6.3. Variabilidad espacial

Se utilizaron los resultados del análisis de frecuencia para generar un ráster de precipitación máxima diaria

por cada periodo de retorno. Luego, se calculó la precipitación sobre la zona de interés para cada uno de los

ráster. Los resultados de precipitación máxima diaria se presentan en la Tabla 6-6. Además, la Figura 6-4

incluye un ejemplo de cálculo con el ráster correspondiente al periodo de retorno de 100 años.

Tabla 6-6. Precipitación máxima diaria en las cuencas del grupo C_01

23
BAQUA Ingeniería

www.baqua.cl

|T [años]|Precipitación [mm]|
|---|---|
|2|42.2|
|5|54.3|
|10|64.5|
|25|80.2|
|50|94.0|
|100|110.0|
|200|128.6|

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Figura 6-4. Ráster de precipitación máxima diaria para periodo de retorno de 100 años

## 6.4. Valores IDF

Tabla 6-7. Valores IDF para duraciones entre 1 y 24 horas [mm/hora]

|T [años]|Duración [horas]|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|T** [años]**|**1 **|**2 **|**4 **|**6 **|**8 **|**10**|**12**|**14**|**18**|**24**|
|2|6.51|5.81|4.76|4.18|3.83|3.39|3.06|2.79|2.38|1.94|
|5|8.36|7.46|6.12|5.37|4.92|4.36|3.93|3.58|3.05|2.49|
|10|9.93|8.87|7.27|6.39|5.85|5.18|4.67|4.26|3.63|2.96|
|25|12.35|11.02|9.04|7.94|7.28|6.44|5.81|5.29|4.51|3.67|
|50|14.48|12.93|10.60|9.31|8.54|7.55|6.81|6.21|5.29|4.31|
|100|16.95|15.13|12.41|10.89|9.99|8.84|7.97|7.26|6.19|5.04|
|200|19.81|17.68|14.50|12.73|11.67|10.33|9.31|8.49|7.23|5.89|

24
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Figura 6-5. Curvas IDF para duraciones entre 1 y 24 horas

Tabla 6-8. Valores IDF para duraciones menores a 1 hora [mm/hora]

25

|T [años]|Duración [minutos]|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|T** [años]**|**10**|**20**|**30**|**40**|**50**|**60**|
|2|17.97|12.53|9.94|8.37|7.31|6.52|
|5|23.08|16.09|12.77|10.76|9.39|8.38|
|10|27.44|19.13|15.18|12.79|11.16|9.96|
|25|34.10|23.78|18.86|15.89|13.87|12.38|
|50|40.00|27.89|22.12|18.64|16.27|14.53|
|100|46.80|32.64|25.89|21.81|19.03|17.00|
|200|54.69|38.14|30.25|25.49|22.24|19.86|

BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Figura 6-6. Curvas IDF para duraciones menores a 1 hora

Tabla 6-9. Valores IDF para el tiempo de concentración de las cuencas del grupo C_01 [mm/hora]. Parte 1

|T [años]|C_01_00|C_01_01|C_01_02|C_01_03|C_01_04|C_01_05|C_01_06|
|---|---|---|---|---|---|---|---|
|2|5.86|6.10|6.29|8.21|6.80|9.40|15.86|
|5|7.53|7.84|8.07|10.55|8.73|12.08|20.37|
|10|8.95|9.32|9.60|12.54|10.38|14.36|24.22|
|25|11.12|11.58|11.93|15.59|12.90|17.84|30.10|
|50|13.04|13.59|13.99|18.28|15.13|20.93|35.31|
|100|15.26|15.90|16.37|21.39|17.70|24.49|41.31|
|200|17.84|18.58|19.13|25.00|20.69|28.62|48.28|

Tabla 6-10. Valores IDF para el tiempo de concentración de las cuencas del grupo C_01 [mm/hora]. Parte 2

|T [años]|C_01_07|C_01_08|C_01_09|C_01_10|C_01_11|C_01_12|C_01_13|
|---|---|---|---|---|---|---|---|
|2|5.92|6.03|11.55|11.61|6.22|15.75|17.97|
|5|7.61|7.75|14.83|14.91|7.98|20.23|23.08|
|10|9.05|9.21|17.64|17.73|9.49|24.05|27.44|
|25|11.25|11.45|21.92|22.04|11.80|29.89|34.10|
|50|13.19|13.43|25.71|25.85|13.84|35.06|40.00|
|100|15.43|15.72|30.09|30.24|16.19|41.02|46.80|
|200|18.04|18.37|35.16|35.34|18.92|47.94|54.69|

26
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Tabla 6-11. Valores IDF para el tiempo de concentración de las cuencas del grupo C_01 [mm/hora]. Parte 3

|T [años]|C_01_14|C_01_15|C_01_16|
|---|---|---|---|
|2|6.33|6.75|7.39|
|5|8.13|8.67|9.49|
|10|9.66|10.30|11.28|
|25|12.01|12.81|14.02|
|50|14.09|15.02|16.44|
|100|16.48|17.58|19.24|
|200|19.26|20.54|22.48|

## 6.5. Método racional

En primer lugar, se estimó el coeficiente de escorrentía y se amplificó en función del periodo de retorno,

obteniendo lo siguiente:

Tabla 6-12. Estimación del coeficiente de escorrentía. Parte 1

|Factor|C_01_00|Col3|C_01_01|Col5|C_01_02|Col7|
|---|---|---|---|---|---|---|
|**Factor**|**Categoría**|**Valor**|**Categoría**|**Valor**|**Categoría**|**Valor**|
|Relieve|Alto|0.26|Normal|0.18|Normal|0.15|
|Infiltración|Alto|0.10|Alto|0.10|Alto|0.10|
|Cobertura vegetal|Normal|0.08|Alto|0.09|Alto|0.09|
|Almacenamiento superficial|Alto|0.08|Alto|0.08|Alto|0.08|
|**Suma**||**0.52**||**0.45**||**0.42**|

Tabla 6-13. Estimación del coeficiente de escorrentía. Parte 2

|Factor|C_01_03|Col3|C_01_04|Col5|C_01_05|Col7|
|---|---|---|---|---|---|---|
|**Factor**|**Categoría**|**Valor**|**Categoría**|**Valor**|**Categoría**|**Valor**|
|Relieve|Bajo|0.11|Normal|0.14|Normal|0.16|
|Infiltración|Alto|0.10|Alto|0.10|Alto|0.10|
|Cobertura vegetal|Alto|0.10|Alto|0.09|Alto|0.09|
|Almacenamiento superficial|Alto|0.08|Alto|0.08|Alto|0.08|
|**Suma**||**0.39**||**0.41**||**0.43**|

27
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Tabla 6-14. Estimación del coeficiente de escorrentía. Parte 3

|Factor|C_01_06|Col3|C_01_07|Col5|C_01_08|Col7|
|---|---|---|---|---|---|---|
|**Factor**|**Categoría**|**Valor**|**Categoría**|**Valor**|**Categoría**|**Valor**|
|Relieve|Normal|0.17|Alto|0.28|Alto|0.28|
|Infiltración|Alto|0.10|Alto|0.10|Alto|0.10|
|Cobertura vegetal|Alto|0.10|Normal|0.08|Normal|0.08|
|Almacenamiento superficial|Alto|0.08|Alto|0.08|Alto|0.08|
|**Suma**||**0.45**||**0.54**||**0.54**|

Tabla 6-15. Estimación del coeficiente de escorrentía. Parte 4

|Factor|C_01_09|Col3|C_01_10|Col5|C_01_11|Col7|
|---|---|---|---|---|---|---|
|**Factor**|**Categoría**|**Valor**|**Categoría**|**Valor**|**Categoría**|**Valor**|
|Relieve|Alto|0.22|Normal|0.15|Extremo|0.29|
|Infiltración|Alto|0.10|Alto|0.10|Alto|0.10|
|Cobertura vegetal|Alto|0.09|Alto|0.10|Normal|0.07|
|Almacenamiento superficial|Alto|0.08|Alto|0.08|Alto|0.08|
|**Suma**||**0.49**||**0.43**||**0.54**|

Tabla 6-16. Estimación del coeficiente de escorrentía. Parte 5

|Factor|C_01_12|Col3|C_01_13|Col5|C_01_14|Col7|
|---|---|---|---|---|---|---|
|**Factor**|**Categoría**|**Valor**|**Categoría**|**Valor**|**Categoría**|**Valor**|
|Relieve|Alto|0.21|Normal|0.18|Extremo|0.29|
|Infiltración|Alto|0.10|Alto|0.10|Alto|0.10|
|Cobertura vegetal|Alto|0.09|Alto|0.10|Normal|0.07|
|Almacenamiento superficial|Alto|0.08|Alto|0.08|Alto|0.07|
|**Suma**||**0.48**||**0.46**||**0.53**|

Tabla 6-17. Estimación del coeficiente de escorrentía. Parte 6

28

|Factor|C_01_15|Col3|C_01_16|Col5|
|---|---|---|---|---|
|**Factor**|**Categoría**|**Valor**|**Categoría**|**Valor**|
|Relieve|Extremo|0.33|Extremo|0.33|
|Infiltración|Alto|0.10|Alto|0.08|
|Cobertura vegetal|Normal|0.07|Normal|0.06|
|Almacenamiento superficial|Alto|0.06|Alto|0.06|

BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

|Factor|C_01_15|Col3|C_01_16|Col5|
|---|---|---|---|---|
|**Factor**|**Categoría**|**Valor**|**Categoría**|**Valor**|
|**Suma**||**0.56**||**0.53**|

Tabla 6-18. Amplificación del coeficiente de escorrentía en función del periodo de retorno. Parte 1

|T [años]|Factor de<br>amplificación|C_01_00|C_01_01|C_01_02|C_01_03|C_01_04|C_01_05|
|---|---|---|---|---|---|---|---|
|2|1.00|0.52|0.45|0.42|0.39|0.41|0.43|
|5|1.00|0.52|0.45|0.42|0.39|0.41|0.43|
|10|1.00|0.52|0.45|0.42|0.39|0.41|0.43|
|25|1.10|0.57|0.50|0.46|0.43|0.45|0.47|
|50|1.20|0.62|0.54|0.50|0.47|0.49|0.52|
|100|1.25|0.65|0.56|0.53|0.49|0.51|0.54|
|200|1.25|0.65|0.56|0.53|0.49|0.51|0.54|

Tabla 6-19. Amplificación del coeficiente de escorrentía en función del periodo de retorno. Parte 2

|T [años]|Factor de<br>amplificación|C_01_06|C_01_07|C_01_08|C_01_09|C_01_10|C_01_11|
|---|---|---|---|---|---|---|---|
|2|1.00|0.45|0.54|0.54|0.49|0.43|0.54|
|5|1.00|0.45|0.54|0.54|0.49|0.43|0.54|
|10|1.00|0.45|0.54|0.54|0.49|0.43|0.54|
|25|1.10|0.50|0.59|0.59|0.54|0.47|0.59|
|50|1.20|0.54|0.65|0.65|0.59|0.52|0.65|
|100|1.25|0.56|0.68|0.68|0.61|0.54|0.68|
|200|1.25|0.56|0.68|0.68|0.61|0.54|0.68|

Tabla 6-20. Amplificación del coeficiente de escorrentía en función del periodo de retorno. Parte 3

29

|T [años]|Factor de<br>amplificación|C_01_12|C_01_13|C_01_14|C_01_15|C_01_16|
|---|---|---|---|---|---|---|
|2|1.00|0.48|0.46|0.53|0.56|0.53|
|5|1.00|0.48|0.46|0.53|0.56|0.53|
|10|1.00|0.48|0.46|0.53|0.56|0.53|
|25|1.10|0.53|0.51|0.58|0.62|0.58|
|50|1.20|0.58|0.55|0.64|0.67|0.64|
|100|1.25|0.60|0.58|0.66|0.70|0.66|

BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

|T [años]|Factor de<br>amplificación|C_01_12|C_01_13|C_01_14|C_01_15|C_01_16|
|---|---|---|---|---|---|---|
|200|1.25|0.60|0.58|0.66|0.70|0.66|

Luego, los caudales máximos instantáneos para las diferentes cuencas son:

Tabla 6-21. Caudal máximo instantáneo con el Método racional [m [3] /s]. Parte 1

|T [años]|C_01_00|C_01_01|C_01_02|C_01_03|C_01_04|C_01_05|C_01_06|
|---|---|---|---|---|---|---|---|
|2|8.12|1.49|1.26|0.30|0.75|0.49|0.22|
|5|10.43|1.91|1.62|0.39|0.97|0.63|0.28|
|10|12.40|2.27|1.92|0.46|1.15|0.74|0.33|
|25|16.95|3.11|2.63|0.64|1.57|1.02|0.45|
|50|21.69|3.98|3.37|0.81|2.01|1.30|0.58|
|100|26.44|4.85|4.10|0.99|2.45|1.59|0.71|
|200|30.90|5.66|4.79|1.16|2.87|1.85|0.82|

Tabla 6-22. Caudal máximo instantáneo con el Método racional [m [3] /s]. Parte 2

|T [años]|C_01_07|C_01_08|C_01_09|C_01_10|C_01_11|C_01_12|C_01_13|
|---|---|---|---|---|---|---|---|
|2|6.48|6.08|0.59|0.09|5.42|0.16|0.10|
|5|8.32|7.80|0.76|0.12|6.96|0.21|0.13|
|10|9.89|9.28|0.90|0.14|8.27|0.24|0.16|
|25|13.52|12.68|1.23|0.20|11.31|0.33|0.21|
|50|17.30|16.23|1.58|0.25|14.48|0.43|0.27|
|100|21.09|19.78|1.92|0.31|17.64|0.52|0.33|
|200|24.65|23.12|2.25|0.36|20.62|0.61|0.39|

Tabla 6-23. Caudal máximo instantáneo con el Método racional [m [3] /s]. Parte 3

30
BAQUA Ingeniería

www.baqua.cl

|T [años]|C_01_14|C_01_15|C_01_16|
|---|---|---|---|
|2|5.17|3.58|3.54|
|5|6.64|4.60|4.55|
|10|7.90|5.47|5.41|
|25|10.80|7.48|7.39|
|50|13.82|9.57|9.46|
|100|16.84|11.67|11.53|
|200|19.68|13.63|13.47|

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

# 7. Conclusiones y comentarios

Se estimaron los caudales máximos instantáneos del grupo de cauces C_01 para los periodos de retorno de

2 a 200 años. Los resultados permitirán evaluar el comportamiento hidráulico de cada cauce y, en particular,

estos caudales permitirán los límites del cauce como la superficie inundada por el caudal con periodo de

retorno de 100 años. Los resultados para este periodo de retorno se presentan a continuación:

Tabla 7-1. Resumen caudal máximo instantáneo [m [3] /s]. Parte 1

|T [años]|C_01_00|C_01_01|C_01_02|C_01_03|C_01_04|C_01_05|C_01_06|
|---|---|---|---|---|---|---|---|
|100|26.44|4.85|4.10|0.99|2.45|1.59|0.71|

Tabla 7-2. Resumen caudal máximo instantáneo [m [3] /s]. Parte 2

|T [años]|C_01_07|C_01_08|C_01_09|C_01_10|C_01_11|C_01_12|C_01_13|
|---|---|---|---|---|---|---|---|
|100|21.09|19.78|1.92|0.31|17.64|0.52|0.33|

Tabla 7-3. Resumen caudal máximo instantáneo [m [3] /s]. Parte 3

# 8. Referencias

|T [años]|C_01_14|C_01_15|C_01_16|
|---|---|---|---|
|100|16.84|11.67|11.53|

ASF DAAC. (2011). ALOS PALSAR_Radiometric_Terrain_Corrected_high_res; Includes Material ©

JAXA/METI 2007. ALOS PALSAR_Radiometric_Terrain_Corrected_high_res; Includes Material ©
JAXA/METI 2007. doi:10.5067/Z97HFCNKR6VA

Chow, V. T., Maidment, D. R., & Mays, L. W. (1988). Applied hydrology. Singapore: McGraw-Hill.

DGA. (1995). Manual de cálculo de crecidas y caudales mínimos en cuencas sin información fluviométrica.

Santiago: Dirección General de Aguas.

DGA. (2016). Guías metodológicas para la presentación y revisión técnica de proyectos de modificación de

cauces naturales y artificiales. Santiago: Dirección General de Aguas.

Karra, K., Kontgis, C., Statman-Weil, Z., Mazzariello, J. C., Mathis, M., & Brumby, S. P. (2021). Global land use

/ land cover with Sentinel 2 and deep learning. 2021 IEEE International Geoscience and Remote
Sensing Symposium IGARSS, (págs. 4704-4707). doi:10.1109/IGARSS47720.2021.9553499

Maidment, D. R. (1993). Handbook of hydrology. McGraw-Hill.

31
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

MOP. (2020). Manual de Carreteras. Volumen 3. Instrucciones y criterios de diseño. Ministerio de Obras

Públicas.

NRCS. (2010). Chapter 15. Time of concentration. En National Engineering Handbook. Part 630 Hydrology.

Natural Resources Conservation Service, U.S. Department of Agriculture.

SEA, & DGA. (2014). Permiso para efectuar modificaciones de cauce. Servicio de Evaluación Ambiental.

SEA, DGA, & DOH. (2014). Permiso obras de regularización o defensa de cauces naturales. Servicio de

Evaluación Ambiental.

32
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

# 9. Apéndice

## 9.1. Series POT

En las siguientes tablas se presentan las series de duración parcial o POT para las cuatro estaciones utilizadas

en el análisis de frecuencia.

Tabla 9-1: Series POT para estaciones Mincha Norte e Illapel DGA

|ID|Mincha norte|Col3|Illapel DGA|Col5|
|---|---|---|---|---|
|**ID**|**Fecha**|**Precipitación [mm]**|**Fecha**|**Precipitación [mm]**|
|1|3/6/2002|95.0|16/8/1997|83.0|
|2|6/8/2015|80.0|11/5/2017|81.0|
|3|16/8/1997|68.0|3/6/2002|78.0|
|4|23/6/2000|64.0|23/6/2000|60.0|
|5|7/6/2006|59.0|5/6/1992|57.0|
|6|20/5/2003|54.0|14/6/2000|52.0|
|7|15/8/2008|50.0|11/6/1997|51.0|
|8|11/6/2014|49.5|6/8/2015|50.0|
|9|25/6/2017|49.0|18/7/2001|47.5|
|10|9/5/2017|48.0|6/7/1996|47.0|
|11|4/7/2018|47.0|6/5/1993|45.0|
|12|30/7/2001|45.0|2/6/2016|44.5|
|13|25/7/2006|43.0|30/8/1992|43.0|
|14|2/6/2016|43.0|15/8/2008|41.5|
|15|18/7/2001|42.5|11/6/2014|40.5|
|16|20/6/2011|42.0|23/7/2002|40.0|
|17|29/8/1992|40.5|20/7/2002|39.0|
|18|5/6/1992|40.0|20/5/2003|38.0|
|19|6/7/1996|39.1|12/7/2015|36.0|
|20|14/6/2000|37.5|15/7/2011|35.5|
|21|25/5/2002|37.0|24/6/1992|35.0|
|22|20/7/2004|37.0|26/5/2002|34.5|
|23|15/7/2011|37.0|7/6/2006|34.5|
|24|27/5/2013|37.0|7/6/1992|34.0|

33
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

|ID|Mincha norte|Col3|Illapel DGA|Col5|
|---|---|---|---|---|
|**ID**|**Fecha**|**Precipitación [mm]**|**Fecha**|**Precipitación [mm]**|
|25|27/8/2002|35.5|23/6/1997|34.0|
|26|25/8/2001|35.0|16/6/2017|34.0|
|27|23/7/2002|35.0|21/4/2004|33.0|
|28|13/10/2006|35.0|27/6/2009|33.0|

Tabla 9-2: Series POT para estaciones Limahuida y La Canela DMC

|ID|Limahuida|Col3|La Canela DMC|Col5|
|---|---|---|---|---|
|**ID**|**Fecha**|**Precipitación [mm]**|**Fecha**|**Precipitación [mm]**|
|1|3/6/2002|86.0|16/8/1997|90.0|
|2|10/5/2017|76.5|10/5/2017|81.0|
|3|6/8/2015|68.5|20/6/2011|63.2|
|4|12/7/2015|65.5|5/6/1992|63.0|
|5|23/6/2000|65.0|3/6/2002|60.0|
|6|15/8/2008|65.0|6/8/2015|56.3|
|7|18/7/2001|62.0|18/7/2001|54.5|
|8|2/6/2016|62.0|12/7/2015|53.0|
|9|5/6/1992|50.0|20/5/2003|48.0|
|10|16/8/1997|48.0|15/8/2009|46.8|
|11|14/6/2000|48.0|16/8/2012|46.2|
|12|30/8/1992|46.0|23/6/2000|43.5|
|13|20/5/2003|46.0|11/6/2014|42.5|
|14|21/4/2004|46.0|4/6/1997|42.0|
|15|11/6/2014|44.5|14/6/2000|41.5|
|16|24/6/1992|44.0|7/6/1992|39.5|
|17|26/5/2002|44.0|15/6/2017|39.0|
|18|20/6/1997|41.0|6/7/1996|37.0|
|19|11/6/1997|40.0|13/10/1997|37.0|
|20|23/7/2002|40.0|30/7/2001|36.8|
|21|7/6/1992|38.0|25/7/2006|35.5|
|22|20/7/2002|38.0|13/4/1993|35.0|
|23|16/8/2012|37.2|2/6/2016|34.4|
|24|30/7/2001|36.5|21/4/2004|34.0|

34
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

|ID|Limahuida|Col3|La Canela DMC|Col5|
|---|---|---|---|---|
|**ID**|**Fecha**|**Precipitación [mm]**|**Fecha**|**Precipitación [mm]**|
|25|27/5/2013|36.5|13/10/2006|34.0|
|26|6/5/1993|36.0|25/6/2017|34.0|
|27|6/7/1996|35.0|30/8/1992|33.8|
|28|30/8/1999|32.5|29/8/1993|32.0|

## 9.2. Tests de bondad de ajuste

Para las estaciones Mincha Norte y Limahuida, se obtiene lo expuesto en la Tabla 9-3 y la Tabla 9-4. A partir

de esto, en ambos casos se escoge la distribución Generalizada de Pareto, debido a que presenta los menores

resultados de estadísticos en todos los tests aplicados.

Tabla 9-3: Resultados tests de bondad de ajuste para estación Mincha Norte

|Test de<br>bondad|Gamma|Generalizada<br>de Valores<br>Extremos|Generalizada<br>de Pareto|Gumbel|Log-normal|Normal|
|---|---|---|---|---|---|---|
|KS|0.175|0.099|0.084|0.160|0.164|0.210|
|AD|0.229|0.034|0.026|0.148|0.182|0.338|
|CvM|1.402|0.291|0.211|0.948|1.152|1.970|
|Chi2|11.320|2.656|1.413|8.030|9.205|17.443|

Tabla 9-4: Resultados tests de bondad de ajuste para estación Limahuida

|Test de<br>bondad|Gamma|Generalizada<br>de Valores<br>Extremos|Generalizada<br>de Pareto|Gumbel|Log-normal|Normal|
|---|---|---|---|---|---|---|
|KS|0.181|0.139|0.115|0.144|0.163|0.213|
|AD|0.193|0.072|0.054|0.117|0.163|0.260|
|CvM|1.068|0.482|-|0.704|0.923|1.400|
|Chi2|6.952|3.179|3.105|4.800|5.896|9.859|

Para las estaciones Illapel DGA y La Canela DMC, se obtiene lo expuesto en la Tabla 9-5 y la Tabla 9-6. En

estos casos, se escoge la distribución Generalizada de Valores Extremos, debido a que presenta los menores

valores para el estadístico del test de Kolmogorov-Smirnof y entrega precipitaciones mayores para periodos

de retorno más altos (50, 100 y 200 años), por lo que se considera un escenario más conservador.

35
BAQUA Ingeniería

www.baqua.cl

ANEXO 1.01 ANÁLISIS HIDROLÓGICO C_01
ESTUDIO DE INUNDACIÓN

PARQUE FOTOVOLTAICO LLANOS DE RUNGUE

Tabla 9-5: Resultados tests de bondad de ajuste para estación Illapel DGA

|Test de<br>bondad|Gamma|Generalizada<br>de Valores<br>Extremos|Generalizada<br>de Pareto|Gumbel|Log-normal|Normal|
|---|---|---|---|---|---|---|
|KS|0.150|0.099|0.107|0.150|0.136|0.179|
|AD|0.206|0.045|0.027|0.135|0.164|0.307|
|CvM|1.435|0.408|0.297|0.974|1.188|2.008|
|Chi2|9.569|2.237|1.029|6.881|7.648|15.096|

Tabla 9-6: Resultados tests de bondad de ajuste para estación La Canela DMC

|Test de<br>bondad|Gamma|Generalizada<br>de Valores<br>Extremos|Generalizada<br>de Pareto|Gumbel|Log-normal|Normal|
|---|---|---|---|---|---|---|
|KS|0.155|0.111|0.115|0.159|0.143|0.182|
|AD|0.169|0.047|0.029|0.107|0.137|0.247|
|CvM|1.099|0.397|0.293|0.747|0.916|1.545|
|Chi2|5.522|0.789|0.535|3.411|4.189|9.508|

36
BAQUA Ingeniería

www.baqua.cl

[www.baqua.cl](https://www.baqua.cl/) 2 3210 6670

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3-1.: Coordenadas representativas del proyecto**

| Sector | Este [m] | Norte [m] | CRS (*) |
| --- | --- | --- | --- |
| 1 | 274 444.6 | 6 500 605.4 | UTM WGS84 H19 S |
| 2 | 273 534.6 | 6 500 292.8 | UTM WGS84 H19 S |
| 3 | 273 403.5 | 6 499 821.2 | UTM WGS84 H19 S |

**Tabla 3-2.: Ubicación del grupo de cauces C_01 según BNA**

| División | Nombre | Código |
| --- | --- | --- |
| Cuenca | Río Choapa | 047 |
| Subcuenca | Rio Choapa Bajo (entre Rio Illapel y Desembocadura) | 0473 |
| Subsubcuenca | Rio Choapa Entre Rio Illapel y Estero Canela | 04730 |

**Tabla 4-1.: Información de las estaciones pluviométricas según DGA**

| Nombre estación | Código BNA | Coordenadas (*) | Col4 | Fecha | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Nombre estación** | **Código BNA** | **Este [m]** | **Norte [m]** | **Inicio** | **Fin** |
| Illapel DGA | 04726003-5 | 293 094 | 6 497 017 | 1974 | 2020 |
| La Canela DMC | 04732001-1 | 266 445 | 6 523 752 | 1974 | 2020 |
| Limahuida | 04716005-7 | 294 965 | 6 485 124 | 1964 | 2020 |
| Mincha Norte | 04730004-5 | 267 509 | 6 502 706 | 1973 | 2020 |

**Tabla 6-1.: Parámetros morfométricos de las cuencas C_01. Parte 1**

| Parámetro | Símbolo | Unidad | C_01_00 | C_01_01 | C_01_02 | C_01_03 | C_01_04 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Superficie | A | km2 | 9.59 | 1.95 | 1.72 | 0.34 | 0.97 |
| Longitud del cauce principal | L | km | 7.53 | 3.74 | 2.95 | 1.23 | 2.15 |
| Cota mínima | zmin | msnm | 137.0 | 133.1 | 184.2 | 217.5 | 217.2 |

**Tabla 6-2.: Parámetros morfométricos de las cuencas C_01. Parte 2**

| Parámetro | Símbolo | Unidad | C_01_05 | C_01_06 | C_01_07 | C_01_08 | C_01_09 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Superficie | A | km2 | 0.43 | 0.11 | 7.29 | 6.71 | 0.38 |
| Longitud del cauce principal | L | km | 1.06 | 0.36 | 6.99 | 6.07 | 0.92 |
| Cota mínima | zmin | msnm | 240.1 | 262.0 | 169.0 | 204.0 | 200.3 |
| Cota máxima | zmax | msnm | 304.2 | 304.2 | 926.0 | 926.0 | 283.2 |
| Cota media | zmedia | msnm | 265.1 | 279.3 | 424.2 | 440.5 | 247.5 |
| Pendiente media | S | m/m | 0.063 | 0.076 | 0.299 | 0.307 | 0.138 |
| Desnivel máximo | Hmax | m | 64.1 | 42.1 | 757.0 | 722.0 | 83.0 |
| Desnivel medio | Hmedio | m | 25.0 | 17.3 | 255.2 | 236.5 | 47.3 |
| Tiempo de concentración | tc1 | minutos | 31.9 | 13.4 | 99.2 | 88.7 | 24.6 |
| Tiempo de concentración | tc2 | minutos | 12.3 | 4.1 | 41.9 | 36.3 | 9.5 |
| Tiempo de concentración | tc3 | minutos | 63.4 | 33.5 | 99.9 | 94.9 | 41.8 |
| Tiempo de concentración | tc4 | minutos | 12.1 | 4.8 | 28.2 | 25.1 | 8.0 |
| Tiempo de concentración | tc5 | minutos | 29.3 | 10.9 | 106.5 | 92.7 | 22.0 |
| Tiempo de concentración | tc | minutos | 33.0 | 12.9 | 102.9 | 90.7 | 23.1 |
| Curva número | CN | - | 77.0 | 77.0 | 77.0 | 77.0 | 77.0 |

**Tabla 6-3.: Parámetros morfométricos de las cuencas C_01. Parte 3**

| Parámetro | Símbolo | Unidad | C_01_10 | C_01_11 | C_01_12 | C_01_13 | C_01_14 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Superficie | A | km2 | 0.07 | 5.81 | 0.08 | 0.04 | 5.55 |
| Longitud del cauce principal | L | km | 0.64 | 4.99 | 0.42 | 0.17 | 4.49 |
| Cota mínima | zmin | msnm | 255.0 | 230.0 | 211.4 | 235.2 | 242.0 |
| Cota máxima | zmax | msnm | 283.2 | 926.0 | 263.2 | 263.2 | 926.0 |
| Cota media | zmedia | msnm | 270.1 | 468.4 | 246.3 | 252.8 | 477.9 |
| Pendiente media | S | m/m | 0.062 | 0.332 | 0.120 | 0.081 | 0.341 |
| Desnivel máximo | Hmax | m | 28.1 | 696.0 | 51.9 | 28.0 | 684.0 |
| Desnivel medio | Hmedio | m | 15.0 | 238.4 | 34.9 | 17.6 | 235.9 |
| Tiempo de concentración | tc1 | minutos | 21.8 | 75.3 | 14.0 | 7.4 | 69.2 |
| Tiempo de concentración | tc2 | minutos | 9.5 | 29.4 | 4.6 | 2.0 | 26.2 |
| Tiempo de concentración | tc3 | minutos | 38.8 | 83.2 | 22.0 | 19.6 | 78.9 |
| Tiempo de concentración | tc4 | minutos | 8.3 | 20.9 | 4.6 | 2.6 | 19.1 |
| Tiempo de concentración | tc5 | minutos | 21.4 | 76.2 | 12.2 | 5.5 | 68.5 |
| Tiempo de concentración | tc | minutos | 22.9 | 75.8 | 13.0 | 10.0 | 68.8 |
| Curva número | CN | - | 77.0 | 77.0 | 77.0 | 77.0 | 77.0 |

**Tabla 6-4.: Parámetros morfométricos de las cuencas C_01. Parte 4**

| Parámetro | Símbolo | Unidad | C_01_15 | C_01_16 |
| --- | --- | --- | --- | --- |
| Superficie | A | km2 | 3.41 | 3.26 |
| Longitud del cauce principal | L | km | 3.71 | 3.15 |
| Cota mínima | zmin | msnm | 241.8 | 269.0 |
| Cota máxima | zmax | msnm | 902.7 | 902.7 |
| Cota media | zmedia | msnm | 517.4 | 529.1 |
| Pendiente media | S | m/m | 0.435 | 0.446 |
| Desnivel máximo | Hmax | m | 660.9 | 633.8 |
| Desnivel medio | Hmedio | m | 275.6 | 260.1 |
| Tiempo de concentración | tc1 | minutos | 57.1 | 50.2 |
| Tiempo de concentración | tc2 | minutos | 21.3 | 17.9 |
| Tiempo de concentración | tc3 | minutos | 58.5 | 55.6 |
| Tiempo de concentración | tc4 | minutos | 15.0 | 13.1 |
| Tiempo de concentración | tc5 | minutos | 56.6 | 48.1 |
| Tiempo de concentración | tc | minutos | 56.8 | 49.1 |

**Tabla 6-5.: Precipitación máxima diaria por estación para diferentes periodos de retorno [mm]**

| Nombre Estación | Periodo de retorno T [años] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Nombre Estación** | **2 ** | **5 ** | **10** | **25** | **50** | **100** | **200** |
| Illapel DGA | 41.34 | 52.28 | 62.00 | 78.08 | 93.54 | 112.68 | 136.44 |
| La Canela DMC | 42.35 | 53.66 | 63.38 | 78.99 | 93.56 | 111.16 | 132.47 |
| Limahuida | 45.12 | 59.62 | 69.51 | 81.30 | 89.34 | 96.69 | 103.41 |
| Mincha Norte | 42.16 | 54.34 | 64.94 | 81.05 | 95.06 | 110.86 | 128.68 |

**Tabla 6-6.: Precipitación máxima diaria en las cuencas del grupo C_01**

| T [años] | Precipitación [mm] |
| --- | --- |
| 2 | 42.2 |
| 5 | 54.3 |
| 10 | 64.5 |
| 25 | 80.2 |
| 50 | 94.0 |
| 100 | 110.0 |
| 200 | 128.6 |

**Tabla 6-7.: Valores IDF para duraciones entre 1 y 24 horas [mm/hora]**

| T [años] | Duración [horas] | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| T** [años]** | **1 ** | **2 ** | **4 ** | **6 ** | **8 ** | **10** | **12** | **14** | **18** | **24** |
| 2 | 6.51 | 5.81 | 4.76 | 4.18 | 3.83 | 3.39 | 3.06 | 2.79 | 2.38 | 1.94 |
| 5 | 8.36 | 7.46 | 6.12 | 5.37 | 4.92 | 4.36 | 3.93 | 3.58 | 3.05 | 2.49 |
| 10 | 9.93 | 8.87 | 7.27 | 6.39 | 5.85 | 5.18 | 4.67 | 4.26 | 3.63 | 2.96 |
| 25 | 12.35 | 11.02 | 9.04 | 7.94 | 7.28 | 6.44 | 5.81 | 5.29 | 4.51 | 3.67 |
| 50 | 14.48 | 12.93 | 10.60 | 9.31 | 8.54 | 7.55 | 6.81 | 6.21 | 5.29 | 4.31 |
| 100 | 16.95 | 15.13 | 12.41 | 10.89 | 9.99 | 8.84 | 7.97 | 7.26 | 6.19 | 5.04 |
| 200 | 19.81 | 17.68 | 14.50 | 12.73 | 11.67 | 10.33 | 9.31 | 8.49 | 7.23 | 5.89 |

**Tabla 6-8.: Valores IDF para duraciones menores a 1 hora [mm/hora]**

| T [años] | Duración [minutos] | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| T** [años]** | **10** | **20** | **30** | **40** | **50** | **60** |
| 2 | 17.97 | 12.53 | 9.94 | 8.37 | 7.31 | 6.52 |
| 5 | 23.08 | 16.09 | 12.77 | 10.76 | 9.39 | 8.38 |
| 10 | 27.44 | 19.13 | 15.18 | 12.79 | 11.16 | 9.96 |
| 25 | 34.10 | 23.78 | 18.86 | 15.89 | 13.87 | 12.38 |
| 50 | 40.00 | 27.89 | 22.12 | 18.64 | 16.27 | 14.53 |
| 100 | 46.80 | 32.64 | 25.89 | 21.81 | 19.03 | 17.00 |
| 200 | 54.69 | 38.14 | 30.25 | 25.49 | 22.24 | 19.86 |

**Tabla 6-9.: Valores IDF para el tiempo de concentración de las cuencas del grupo C_01 [mm/hora]. Parte 1**

| T [años] | C_01_00 | C_01_01 | C_01_02 | C_01_03 | C_01_04 | C_01_05 | C_01_06 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 5.86 | 6.10 | 6.29 | 8.21 | 6.80 | 9.40 | 15.86 |
| 5 | 7.53 | 7.84 | 8.07 | 10.55 | 8.73 | 12.08 | 20.37 |
| 10 | 8.95 | 9.32 | 9.60 | 12.54 | 10.38 | 14.36 | 24.22 |
| 25 | 11.12 | 11.58 | 11.93 | 15.59 | 12.90 | 17.84 | 30.10 |
| 50 | 13.04 | 13.59 | 13.99 | 18.28 | 15.13 | 20.93 | 35.31 |
| 100 | 15.26 | 15.90 | 16.37 | 21.39 | 17.70 | 24.49 | 41.31 |
| 200 | 17.84 | 18.58 | 19.13 | 25.00 | 20.69 | 28.62 | 48.28 |

**Tabla 6-10.: Valores IDF para el tiempo de concentración de las cuencas del grupo C_01 [mm/hora]. Parte 2**

| T [años] | C_01_07 | C_01_08 | C_01_09 | C_01_10 | C_01_11 | C_01_12 | C_01_13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 5.92 | 6.03 | 11.55 | 11.61 | 6.22 | 15.75 | 17.97 |
| 5 | 7.61 | 7.75 | 14.83 | 14.91 | 7.98 | 20.23 | 23.08 |
| 10 | 9.05 | 9.21 | 17.64 | 17.73 | 9.49 | 24.05 | 27.44 |
| 25 | 11.25 | 11.45 | 21.92 | 22.04 | 11.80 | 29.89 | 34.10 |
| 50 | 13.19 | 13.43 | 25.71 | 25.85 | 13.84 | 35.06 | 40.00 |
| 100 | 15.43 | 15.72 | 30.09 | 30.24 | 16.19 | 41.02 | 46.80 |
| 200 | 18.04 | 18.37 | 35.16 | 35.34 | 18.92 | 47.94 | 54.69 |

**Tabla 6-11.: Valores IDF para el tiempo de concentración de las cuencas del grupo C_01 [mm/hora]. Parte 3**

| T [años] | C_01_14 | C_01_15 | C_01_16 |
| --- | --- | --- | --- |
| 2 | 6.33 | 6.75 | 7.39 |
| 5 | 8.13 | 8.67 | 9.49 |
| 10 | 9.66 | 10.30 | 11.28 |
| 25 | 12.01 | 12.81 | 14.02 |
| 50 | 14.09 | 15.02 | 16.44 |
| 100 | 16.48 | 17.58 | 19.24 |
| 200 | 19.26 | 20.54 | 22.48 |

**Tabla 6-12.: Estimación del coeficiente de escorrentía. Parte 1**

| Factor | C_01_00 | Col3 | C_01_01 | Col5 | C_01_02 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Factor** | **Categoría** | **Valor** | **Categoría** | **Valor** | **Categoría** | **Valor** |
| Relieve | Alto | 0.26 | Normal | 0.18 | Normal | 0.15 |
| Infiltración | Alto | 0.10 | Alto | 0.10 | Alto | 0.10 |
| Cobertura vegetal | Normal | 0.08 | Alto | 0.09 | Alto | 0.09 |
| Almacenamiento superficial | Alto | 0.08 | Alto | 0.08 | Alto | 0.08 |
| **Suma** |  | **0.52** |  | **0.45** |  | **0.42** |

**Tabla 6-13.: Estimación del coeficiente de escorrentía. Parte 2**

| Factor | C_01_03 | Col3 | C_01_04 | Col5 | C_01_05 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Factor** | **Categoría** | **Valor** | **Categoría** | **Valor** | **Categoría** | **Valor** |
| Relieve | Bajo | 0.11 | Normal | 0.14 | Normal | 0.16 |
| Infiltración | Alto | 0.10 | Alto | 0.10 | Alto | 0.10 |
| Cobertura vegetal | Alto | 0.10 | Alto | 0.09 | Alto | 0.09 |
| Almacenamiento superficial | Alto | 0.08 | Alto | 0.08 | Alto | 0.08 |
| **Suma** |  | **0.39** |  | **0.41** |  | **0.43** |

**Tabla 6-14.: Estimación del coeficiente de escorrentía. Parte 3**

| Factor | C_01_06 | Col3 | C_01_07 | Col5 | C_01_08 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Factor** | **Categoría** | **Valor** | **Categoría** | **Valor** | **Categoría** | **Valor** |
| Relieve | Normal | 0.17 | Alto | 0.28 | Alto | 0.28 |
| Infiltración | Alto | 0.10 | Alto | 0.10 | Alto | 0.10 |
| Cobertura vegetal | Alto | 0.10 | Normal | 0.08 | Normal | 0.08 |
| Almacenamiento superficial | Alto | 0.08 | Alto | 0.08 | Alto | 0.08 |
| **Suma** |  | **0.45** |  | **0.54** |  | **0.54** |

**Tabla 6-15.: Estimación del coeficiente de escorrentía. Parte 4**

| Factor | C_01_09 | Col3 | C_01_10 | Col5 | C_01_11 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Factor** | **Categoría** | **Valor** | **Categoría** | **Valor** | **Categoría** | **Valor** |
| Relieve | Alto | 0.22 | Normal | 0.15 | Extremo | 0.29 |
| Infiltración | Alto | 0.10 | Alto | 0.10 | Alto | 0.10 |
| Cobertura vegetal | Alto | 0.09 | Alto | 0.10 | Normal | 0.07 |
| Almacenamiento superficial | Alto | 0.08 | Alto | 0.08 | Alto | 0.08 |
| **Suma** |  | **0.49** |  | **0.43** |  | **0.54** |

**Tabla 6-16.: Estimación del coeficiente de escorrentía. Parte 5**

| Factor | C_01_12 | Col3 | C_01_13 | Col5 | C_01_14 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Factor** | **Categoría** | **Valor** | **Categoría** | **Valor** | **Categoría** | **Valor** |
| Relieve | Alto | 0.21 | Normal | 0.18 | Extremo | 0.29 |
| Infiltración | Alto | 0.10 | Alto | 0.10 | Alto | 0.10 |
| Cobertura vegetal | Alto | 0.09 | Alto | 0.10 | Normal | 0.07 |
| Almacenamiento superficial | Alto | 0.08 | Alto | 0.08 | Alto | 0.07 |
| **Suma** |  | **0.48** |  | **0.46** |  | **0.53** |

**Tabla 6-17.: Estimación del coeficiente de escorrentía. Parte 6**

| Factor | C_01_15 | Col3 | C_01_16 | Col5 |
| --- | --- | --- | --- | --- |
| **Factor** | **Categoría** | **Valor** | **Categoría** | **Valor** |
| Relieve | Extremo | 0.33 | Extremo | 0.33 |
| Infiltración | Alto | 0.10 | Alto | 0.08 |
| Cobertura vegetal | Normal | 0.07 | Normal | 0.06 |
| Almacenamiento superficial | Alto | 0.06 | Alto | 0.06 |

**Tabla 6-18.: Amplificación del coeficiente de escorrentía en función del periodo de retorno. Parte 1**

| T [años] | Factor de<br>amplificación | C_01_00 | C_01_01 | C_01_02 | C_01_03 | C_01_04 | C_01_05 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1.00 | 0.52 | 0.45 | 0.42 | 0.39 | 0.41 | 0.43 |
| 5 | 1.00 | 0.52 | 0.45 | 0.42 | 0.39 | 0.41 | 0.43 |
| 10 | 1.00 | 0.52 | 0.45 | 0.42 | 0.39 | 0.41 | 0.43 |
| 25 | 1.10 | 0.57 | 0.50 | 0.46 | 0.43 | 0.45 | 0.47 |
| 50 | 1.20 | 0.62 | 0.54 | 0.50 | 0.47 | 0.49 | 0.52 |
| 100 | 1.25 | 0.65 | 0.56 | 0.53 | 0.49 | 0.51 | 0.54 |
| 200 | 1.25 | 0.65 | 0.56 | 0.53 | 0.49 | 0.51 | 0.54 |

**Tabla 6-19.: Amplificación del coeficiente de escorrentía en función del periodo de retorno. Parte 2**

| T [años] | Factor de<br>amplificación | C_01_06 | C_01_07 | C_01_08 | C_01_09 | C_01_10 | C_01_11 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 1.00 | 0.45 | 0.54 | 0.54 | 0.49 | 0.43 | 0.54 |
| 5 | 1.00 | 0.45 | 0.54 | 0.54 | 0.49 | 0.43 | 0.54 |
| 10 | 1.00 | 0.45 | 0.54 | 0.54 | 0.49 | 0.43 | 0.54 |
| 25 | 1.10 | 0.50 | 0.59 | 0.59 | 0.54 | 0.47 | 0.59 |
| 50 | 1.20 | 0.54 | 0.65 | 0.65 | 0.59 | 0.52 | 0.65 |
| 100 | 1.25 | 0.56 | 0.68 | 0.68 | 0.61 | 0.54 | 0.68 |
| 200 | 1.25 | 0.56 | 0.68 | 0.68 | 0.61 | 0.54 | 0.68 |

**Tabla 6-20.: Amplificación del coeficiente de escorrentía en función del periodo de retorno. Parte 3**

| T [años] | Factor de<br>amplificación | C_01_12 | C_01_13 | C_01_14 | C_01_15 | C_01_16 |
| --- | --- | --- | --- | --- | --- | --- |
| 2 | 1.00 | 0.48 | 0.46 | 0.53 | 0.56 | 0.53 |
| 5 | 1.00 | 0.48 | 0.46 | 0.53 | 0.56 | 0.53 |
| 10 | 1.00 | 0.48 | 0.46 | 0.53 | 0.56 | 0.53 |
| 25 | 1.10 | 0.53 | 0.51 | 0.58 | 0.62 | 0.58 |
| 50 | 1.20 | 0.58 | 0.55 | 0.64 | 0.67 | 0.64 |
| 100 | 1.25 | 0.60 | 0.58 | 0.66 | 0.70 | 0.66 |

**Tabla 6-21.: Caudal máximo instantáneo con el Método racional [m [3] /s]. Parte 1**

| T [años] | C_01_00 | C_01_01 | C_01_02 | C_01_03 | C_01_04 | C_01_05 | C_01_06 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 8.12 | 1.49 | 1.26 | 0.30 | 0.75 | 0.49 | 0.22 |
| 5 | 10.43 | 1.91 | 1.62 | 0.39 | 0.97 | 0.63 | 0.28 |
| 10 | 12.40 | 2.27 | 1.92 | 0.46 | 1.15 | 0.74 | 0.33 |
| 25 | 16.95 | 3.11 | 2.63 | 0.64 | 1.57 | 1.02 | 0.45 |
| 50 | 21.69 | 3.98 | 3.37 | 0.81 | 2.01 | 1.30 | 0.58 |
| 100 | 26.44 | 4.85 | 4.10 | 0.99 | 2.45 | 1.59 | 0.71 |
| 200 | 30.90 | 5.66 | 4.79 | 1.16 | 2.87 | 1.85 | 0.82 |

**Tabla 6-22.: Caudal máximo instantáneo con el Método racional [m [3] /s]. Parte 2**

| T [años] | C_01_07 | C_01_08 | C_01_09 | C_01_10 | C_01_11 | C_01_12 | C_01_13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2 | 6.48 | 6.08 | 0.59 | 0.09 | 5.42 | 0.16 | 0.10 |
| 5 | 8.32 | 7.80 | 0.76 | 0.12 | 6.96 | 0.21 | 0.13 |
| 10 | 9.89 | 9.28 | 0.90 | 0.14 | 8.27 | 0.24 | 0.16 |
| 25 | 13.52 | 12.68 | 1.23 | 0.20 | 11.31 | 0.33 | 0.21 |
| 50 | 17.30 | 16.23 | 1.58 | 0.25 | 14.48 | 0.43 | 0.27 |
| 100 | 21.09 | 19.78 | 1.92 | 0.31 | 17.64 | 0.52 | 0.33 |
| 200 | 24.65 | 23.12 | 2.25 | 0.36 | 20.62 | 0.61 | 0.39 |

**Tabla 6-23.: Caudal máximo instantáneo con el Método racional [m [3] /s]. Parte 3**

| T [años] | C_01_14 | C_01_15 | C_01_16 |
| --- | --- | --- | --- |
| 2 | 5.17 | 3.58 | 3.54 |
| 5 | 6.64 | 4.60 | 4.55 |
| 10 | 7.90 | 5.47 | 5.41 |
| 25 | 10.80 | 7.48 | 7.39 |
| 50 | 13.82 | 9.57 | 9.46 |
| 100 | 16.84 | 11.67 | 11.53 |
| 200 | 19.68 | 13.63 | 13.47 |

**Tabla 7-1.: Resumen caudal máximo instantáneo [m [3] /s]. Parte 1**

| T [años] | C_01_07 | C_01_08 | C_01_09 | C_01_10 | C_01_11 | C_01_12 | C_01_13 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 100 | 21.09 | 19.78 | 1.92 | 0.31 | 17.64 | 0.52 | 0.33 |

**Tabla 7-3.: Resumen caudal máximo instantáneo [m [3] /s]. Parte 3**

| T [años] | C_01_14 | C_01_15 | C_01_16 |
| --- | --- | --- | --- |
| 100 | 16.84 | 11.67 | 11.53 |
