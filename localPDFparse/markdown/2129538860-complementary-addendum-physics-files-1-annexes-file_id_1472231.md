---
title: Normas de Calidad Primaria Aplicables al Proyecto
author: automat
date: D:20141013193133-03'00'
language: es
type: report
pages: 12
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - PLANTA DE PAPEL TISSUE Y UNIDAD ASOCIADA DE ELABORACIÓN DE PELLET DE MADERA PARA AUTOCONSUMO, COMUNA DE VALDIVIA
-->

## INFORME DE EMISIONES ATMOSFERICAS PARA FUENTE ESTACIONARIA

### Proyecto:

# PLANTA DE PAPEL TISSUE Y UNIDAD ASOCIADA DE ELABORACIÓN DE PELLET DE MADERA PARA AUTOCONSUMO, COMUNA DE VALDIVIA

### Octubre 2014

**Antecedentes generales**

Este informe de emisiones atmosféricas se realizó para la evaluación ambiental del

proyecto nuevo “Planta de Papel Tissue y unidad asociada de Elaboración de Pellet de

Madera para Autoconsumo”, ubicado en la comuna de Valdivia, Región de Los Ríos.

El modelamiento de las emisiones se proyectó para una caldera a pellet de madera marca

Servimet modelo Seco 1500-VPM, con un consumo de pellet de 282 Kg/hora.

Ser modelo utilizando el Software Screen View v 3,5 de Lakes Environmental Software,

basado en el modelo de dispersión en aire SCREEN 3 de la US EPA.

**Normas de Calidad Primaria Aplicables al Proyecto**

La norma de calidad primaria aplicada ver tabla adjunta.

La concentración está definida en las Normas de Calidad Primaria del Aire como el valor promedio

temporal detectado en el aire en microgramos por metro cúbico normal (μg/ m3N) y en

miligramos por metro cúbico normal (mg/ m3N), según corresponda.

**Descripción del Modelo SCREEN 3**

El modelo SCREEN 3, son de corto plazo. Se basa en la línea recta y ecuación gaussiana de la pluma

en estado estacionario.

El modelo I SCREEN 3 para chimeneas usa la ecuación gaussiana de la pluma en estado

estacionario. La concentración horaria a una distancia x (en metros) en dirección del viento y a una

distancia transversal y (en metros) está dada por:

Donde Q es la tasa de emisión del contaminante, K es el coeficiente de escalamiento para

Convertir (g/s) en (g/m3), V es el termino vertical, **D** es el termino de decaimiento, **Oy**, **Oz** son las

desviaciones estándar de distribución de concentración lateral y vertical y **Us** es la velocidad media

del viento a la altura de la chimenea en [m/s].

**CÁLCULO DE EMISIONES OPERACIÓN DE CALDERA DE BIOMASA**

**Antecedentes Generales**

En la etapa de operación se producen principalmente emisiones de PM10 y emisiones gaseosas

como, SO2, NO2 y CO producto de la quema de combustible en la caldera. Para estimar tales

emisiones se utilizarán metodologías propuestas por la EPA .

**Emisiones de la caldera**

**Metodología**

En el presente informe se aplica un procedimiento de proyección simple de acuerdo a los

lineamientos de la US EPA para estimar las emisiones de MP 10, CO, NOx y SO2 de la caldera de

biomasa. En este procedimiento se realizará primero una proyección con el modelo SCREEN3 que

según sus especificaciones, es representativo para receptores que se encuentran hasta 100 mts de

la fuente.

Finalmente los resultados de las modelaciones (concentración) son comparados con las Normas

Primarias de Calidad del Aire vigente, lo que permite determinar si las emisiones generadas por la

nueva caldera se ajustarán o no a dicha normativa.

**Cálculos de operación de la caldera**

Para calcular las emisiones del proyecto, primero se debe definir y calcular las variables que se

ingresarán al modelo.

**Actividad de la caldera**

El nivel de funcionamiento de la caldera es de 282 Kg/hr de consumo de pellet y una generación

de 1500 Kg/hr, con un funcionamiento de 24 hora/dia y 365 dias/año.

Considerando que el poder calorífico de la biomasa corresponde a 3867 Kcal/Kg, se calcula el

consumo energético de combustible.

### C energetico= M x P calorifico

**C energético =** Consumo energético de combustible, Kcal/h

**M =** consumo de combustible, Kg/h

**P calorífico =** Poder Calorífico del combustible, Kcal/kg

### C energético = 1.090.494 Kcal/h

Por conversión de unidades, se sabe que:

|Caloría|Joules|
|---|---|
|**1 **|**4,184**|

**Cálculo de emisión atmosférica**

|Parámetros|Factor de emisión<br>Kg/MMJ|Factor de emisión<br>Kg/MMJ|Consumo energético<br>MMJ/h|Emisión atmosférica<br>Kg/h|Emisión atmosférica<br>g/s|
|---|---|---|---|---|---|
|MP-10|1,38E-04|0,000138|4,562|0,000629556|**0,000175017**|
|NOx|9,40E-05|0,0000946|4,562|0,000431565|**0,000119975**|
|SOx|1,08E-05|0,0000108|4,562|4,92696E-05|**1,36969E-05**|
|CO|2,58E-04|0,000258|4,562|0,001176996|**0,000327205**|

**Datos para entrada al modelo**

|Parametros|Unidad|Valor|
|---|---|---|
|Altura de chimenea (h)|m|**6 **|
|Altura efectiva de chimenea (h)|m|**6 **|
|Diámetro equivalente de chimenea<br>(m)|m|**0,35**|
|Caudal de salida de los gases (Q)|m3/s||
|Velocidad de salida de los gases (V)|m/s|**6,6394**|
|Temperatura de salida de los gases<br>(T)|K|**573**|
|Temperatura atmosférica(T)|K|**283**|
|Flujo másico MP-10|g/s|**0,000175**|
|Flujo másico Nox|g/s|**0,000119**|
|Flujo másico SO2|g/s|**0,0000137**|
|Flujo másico CO|g/s|**0,000327**|
|Presión atmosférica|Milibar|**10**|
|Altura del receptor|m|**10**|

a _) Selección de condición urbana o rural_

Ya que la zona del proyecto presenta cierto nivel de rugosidad, debido a la topografía del sector,

para efectos de la modelación de dispersión se utilizó la condición urbana.

b) _Consideración del efecto de remoción por edificios cercanos_

Los edificios ubicados en las inmediaciones de una chimenea influyen de manera diferente en el

desarrollo de la pluma de acuerdo a la relación entre su altura y su ancho, No obstante no se

encuentran edificios cercanos a la planta que puedan obstruir la dispersión de la pluma .

c) _Selección de receptores_

Se solicita al modelo que calcule las zonas de mayor concentración, para posteriormente

superponerlas en los planos y hacer el análisis de posibles receptores.

d) _Condiciones atmosférica_

Para detectar las condiciones atmosféricas de peor caso, es decir aquéllas que implican la

concentración horaria más alta, se pueden tener en cuenta todas las combinaciones posibles de

estabilidad - velocidad de viento - altura de la capa de mezcla. No obstante en vista de la escasez

de información se eligen las condiciones más adversas, de modo que la proyección esté siempre

igual o por sobre las emisiones reales.

### Resultado MP-10

|Parámetros|Concentración máxima horario<br>(ug/m3N)|Distancia desde la caldera (m)<br>donde se produce la mayor<br>concentración|
|---|---|---|
|MP10|87,73|1|

|Norma de<br>Calidad|Periodo|Máximo Norma (ug/m3N)|Modelo SCREEN 3<br>(ug/m3N)|
|---|---|---|---|
|D.S No 59/1998.<br>(MP10)|Concentración 24 Horas|150|35,092|
|D.S No 59/1998.<br>(MP10)|Concentración anual|50|7,0184|

### Resultado NOx

|Parámetros|Concentración máxima horario<br>(ug/m3N)|Distancia desde la caldera (m) donde<br>se produce la mayor concentración|
|---|---|---|
|NOx|60,11|1|

|Norma de<br>Calidad|Periodo|Máximo Norma (ug/m3N)|Modelo SCREEN 3<br>(ug/m3N)|
|---|---|---|---|
|D.S No<br>114/2002. (NOx)|Concentración 1 Horas|400|42,077|
|D.S No<br>114/2002. (NOx)|Concentración anual|100|4,8088|

### Resultado SOx

|Parámetros|Concentración máxima horario<br>(ug/m3N)|Distancia desde la caldera (m) donde<br>se produce la mayor concentración|
|---|---|---|
|SOx|6,818|1|

|Norma de<br>Calidad|Periodo|Máximo Norma (ug/m3N)|Modelo SCREEN 3<br>(ug/m3N)|
|---|---|---|---|
|D.S No<br>114/2002. (SOx)|Concentración diaria|250|4,7726|
|D.S No<br>114/2002. (SOx)|Concentración anual|80|0,54544|

### Resultado CO

|Parámetros|Concentración máxima horario<br>(mg/m3N)|Distancia desde la caldera (m) donde<br>se produce la mayor concentración|
|---|---|---|
|CO|0,164|1|

|Norma de<br>Calidad|Periodo|Máximo Norma (mg/m3N)|Modelo SCREEN 3<br>(mg/m3N)|
|---|---|---|---|
|D.S No<br>115/2002. (CO)|Concentración 1 Hora|30|0,1639|
|D.S No<br>115/2002. (CO)|Concentración 8 Horas|10|0,11473|

Los valores que entrega el modelo son los máximos horarios, los cuales se pueden multiplicar por

los siguientes factores mostrados en la tabla siguiente, para obtener las concentraciones máximas

en 8 horas, diarias y promedio anual.

**Área de Influencia**

El área de influencia debido a la emisiones atmosféricas, emanadas de la chimenea de la

caldera de combustión de pellet de madera modelo Seco 1500 VPMA se restringe al

perímetro del sitio destinado a la construcción de la planta, toda vez que las

concentraciones máximas bajo el umbral de la normativa se obtienen a no más de un par

de metros de la chimenea para los cuatro componentes modelados.

**Concentraciones máximas permitidas por las normas de emisión vigentes y**

**concentraciones máximas modeladas con el modelo SCREEN 3.**

|Norma de<br>Calidad|Periodo|Maximo Norma (ug/m3N)<br>CO (mg/m3N)|Modelo SCREEN 3 (ug/m3N)<br>CO (mg/m3N)|
|---|---|---|---|
|D.S No 59/1998.<br>(MP10)|Concentración 24 Horas|150|35,092|
|D.S No 59/1998.<br>(MP10)|Concentración anual|50|7,0184|
|D.S No<br>114/2002. (NOx)|Concentración 1 Horas|400|42,077|
|D.S No<br>114/2002. (NOx)|Concentración anual|100|4,8088|
|D.S No<br>113/2002. (SOx)|Concentración diaria|250|4,7726|
|D.S No<br>113/2002. (SOx)|Concentración anual|80|0,54544|
|D.S No<br>115/2002. (CO)|Concentración 1 Hora|30|0,1639|
|D.S No<br>115/2002. (CO)|Concentración 8 Horas|10|0,11473|

Elaborado por: **PATRICIO LOPEZ**
Ingeniero Mecánico

Gerente Técnico

AUTOMAT SpA