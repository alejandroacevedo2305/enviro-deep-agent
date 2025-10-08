---
title: Sin título
author: GEOPAL
date: D:20180111094955-03'00'
language: es
type: report
pages: 13
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Informe de Modelación [1]
-->

# Informe de Modelación [1]

## Cálculo de capacidad de carga del proyecto Centro de Cultivo de Salmónidos Canal Almirante Martínez, al Noroeste de Islote Ugalde. Código PERT: 213121037.

### Cultivos Otway S.A.

Preparado por

### Carmen Maluje A. Alejandro Clément D.

**Enero 2018**

1 Informe No 537

## .
### PLANCTON ANDINO SpA

Fonos: +56-65 2 23 50 46: +56-65 2 23 56 63 Terraplén No 869. Casilla 1036. **Puerto Varas**, Chile.
Fono/Fax: +56 -65 2 533 500. Prof. V. Gomez 2449 Int., Bordemar, **Castro**, Archipiélago de Chiloé, Chile.

Calle 1 Casa 782 Valle La Foresta, **Coyhaique**, Región de Aysén, Chile.

**1.** **Introducción**

El crecimiento de la Salmonicultura en el sur austral de Chile, y los problemas sanitarios, evidencian la
necesidad de incorporar criterios oceanográficos y herramientas de modelación cuantitativa a la
evaluación del efecto de esta actividad sobre ecosistemas acuáticos, y sobre otras actividades humanas
que se desarrollan en la región [2] .

Objetivos:

 - Modelar la dispersión de las partículas en el sustrato marino que produce un centro de engorda
de salmónidos, por medio del modelo DEPOMOD, cuantificando la tasa de Carbono Orgánico
Total (COT) depositado sobre el sedimento.

 - Evaluar el efecto del COT en el bentos, por medio del modelo propuesto por Findlay & Watling [3],
que estima la disponibilidad y demanda de oxígeno, a partir de la velocidad de la corriente y
concentración de COT.

2 **Tapia F, y Giglio S. 2010.** Modelos para la Evaluación de la Capacidad de Carga de Fiordos aplicables a Ecosistemas del Sur de

Chile.
3 **Findlay R. H. & L. Watling. 1997.** Prediction of Benthic Impact for Salmon Net-Pens Based on the Balance of Benthic Oxygen

Supply and Demand. Marine Ecology Progress Series. Vol 155: 147-157.

[www.plancton.cl](http://www.plancton.cl/) Página **2** de **13**

## .
### PLANCTON ANDINO SpA

Fonos: +56-65 2 23 50 46: +56-65 2 23 56 63 Terraplén No 869. Casilla 1036. **Puerto Varas**, Chile.
Fono/Fax: +56 -65 2 533 500. Prof. V. Gomez 2449 Int., Bordemar, **Castro**, Archipiélago de Chiloé, Chile.

Calle 1 Casa 782 Valle La Foresta, **Coyhaique**, Región de Aysén, Chile.

**2.** **Metodología**

Con el fin de obtener una evaluación de la tasa de Carbono Orgánico Total depositado en sedimentos, se
usan algoritmos de depositación tomados del modelo DEPOMOD [4] y el Impacto sobre la disponibilidad de
oxígeno disuelto (tomado de los modelos propuestos por Findlay & Watling [3] ).

Para la modelación se tomó los datos batimétricos y de corrientes de la Caracterización Preliminar de
Sitio (CPS), Estudio de Corrientes y los datos productivos del Proyecto Técnico. El ciclo productivo
considerado tiene una duración equivalente a 23 meses de entrega de alimento. El calibre y porcentaje
de uso de alimento fue entregado por el titular, acorde a las tecnologías alimenticias existentes.

**Tabla 1** . Diámetro pellet, % entregado y velocidad de sedimentación.

|Diámetro de pellets (mm)|%|Velocidad de<br>sedimentación (m/s)|
|---|---|---|
|4|5|0,082|
|6 <br>|20 <br>|0,096 <br>|
|9|75|0,122|

Se consideró un diámetro promedio de partículas de fecas de 5 mm y una velocidad de sedimentación,
con distribución normal, de 0,054 m/s ±0,02 m/s (Y-S. Chen et. al. [5] ).

Las variables recién mencionadas son ingresadas al software DEPOMOD v2.2, dando como resultado
tasas de aporte de Carbono Orgánico (calculados en base a Cromey et al. [6] ). De esta forma se evalúa un
año productivo y se predice la distribución de COT depositado en el sedimento.

Luego, los resultados obtenidos son incorporados a los modelos propuestos por Findlay & Watling [3], con
el objetivo de evaluar posibles efectos en el fondo marino, considerando tanto las condiciones
hidrodinámicas como las de producción del centro de cultivo **Canal Almirante Martínez (Cód. Pert:**
**213121037)** .

4 DEPOMOD. Versión 2.2, número de licencia 00-DV-15149C
5 **Y-S. Chen, M. C. M. Beveridge, T. C. Telfer. 1999.** Settling rate characteristics and nutrient content of the faeces of Atlantic

salmon, _Salmo salar_ L., and the implications for modelling of solid waste dispersion. Aquaculture Research. Vol 30: 395-398.
6 **Cromey, C. J.; T. D. Nickell, & K. D. Black. 2002.** DEPOMOD- Modelling the Deposition and Biological Effects of Waste Solids

from Marine Cage Farms. Aquaculture 214. 211-239.

[www.plancton.cl](http://www.plancton.cl/) Página **3** de **13**

## .
### PLANCTON ANDINO SpA

Fonos: +56-65 2 23 50 46: +56-65 2 23 56 63 Terraplén No 869. Casilla 1036. **Puerto Varas**, Chile.
Fono/Fax: +56 -65 2 533 500. Prof. V. Gomez 2449 Int., Bordemar, **Castro**, Archipiélago de Chiloé, Chile.

Calle 1 Casa 782 Valle La Foresta, **Coyhaique**, Región de Aysén, Chile.

**2.1. Limitaciones del Modelo**

 - El modelo acepta hasta 10 mm como diámetro máximo de alimento. Cuando el pellet es de un
calibre mayor, es necesario usar el diámetro máximo en el modelo, manteniendo la velocidad de
sedimentación correspondiente.
Según Y-S. Chen et. al. [5], el parámetro incidente al momento de modelar es la velocidad de
sedimentación del pellet, más que su diámetro.

**2.2. Supuestos del modelo**

Los supuestos del modelo usados en este trabajo: (Cromey et. al. [6] y Buschmann et al. [7] )

a. Contenido de agua del alimento: 9%
b. Porcentaje (%) Alimento no consumido: 3%
c. Porcentaje (%) de Carbono del alimento en peso seco: 49%
d. Porcentaje (%) de Carbono en fecas: 30%
e. Porcentaje (%) de digestibilidad: 85%
f. Coeficientes de dispersión (dirección X): 0,1 m [2] s [-1]
g. Coeficientes de dispersión (dirección Y): 0,1 m [2] s [-1]
h. Coeficientes de dispersión (dirección Z): 0,001 m [2] s [-1]
i. Porcentaje (%) de Certeza del Modelo (Cromey et al. en Corner et al. [8] ) ± 23,1

**2.3. Variables de entrada del modelo**

Las variables de entrada utilizadas en la modelación se extrajeron del Proyecto Técnico (PT) y el Reporte
de alimentación proporcionado por la empresa proveedora de alimento.

a. Número de jaulas: 14.
b. Dimensiones de jaulas: Cuadrada de 40 m x 40 m por 15 m de fondo.
c. Producción de salmónidos: 5.160.000 kg.
d. Factor de conversión: 1,2
e. Alimento total: 6.192.000 Kg/ciclo.
f. Alimento: 640,99 Kg/ jaula/día
g. Batimetría: CPS. Ver Figura 1.
h. Correntometría: Estudio de Corrientes.

i. Velocidad de sedimentación obtenida de Cromey et. al. [6] : ver Tabla 1.

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Para la modelación se tomó los datos batimétricos y de corrientes de la Caracterización Preliminar de Sitio (CPS), Estudio de Corrientes y los datos productivos del Proyecto Técnico. El ciclo productivo considerado tiene una duración equivalente a 23 meses de entrega de alimento. El calibre y porcentaje de uso de alimento fue entregado por el titular, acorde a las tecnologías alimenticias existentes. -->

**Tabla 1: ** . Diámetro pellet, % entregado y velocidad de sedimentación.**

| Diámetro de pellets (mm) | % | Velocidad de<br>sedimentación (m/s) |
| --- | --- | --- |
| 4 | 5 | 0,082 |
| 6 <br> | 20 <br> | 0,096 <br> |
| 9 | 75 | 0,122 |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Se consideró un diámetro promedio de partículas de fecas de 5 mm y una velocidad de sedimentación, con distribución normal, de 0,054 m/s ±0,02 m/s (Y-S. Chen et. al. [5] ). Las variables recién mencionadas son ingresadas al software DEPOMOD v2.2, dando como resultado -->
<!-- FIN TABLA 1 -->

j. Tamaño de pellet usados: ver Tabla 1.

7 **Buschmann, A.; Costa-Pierce, B.; Cross, S.; Iriarte, J.L.; Olsen, Y. & Reid, G. 2007** . Nutrient Impacts of Farmed Atlantic

Salmon ( _Salmo salar_ ) on Pelagic Ecosystems and Implication for Carrying Capacity.
8 **Corner, R.A.; Brooker, A.J.; Telfer, T.C.; Ross, L.G. 2006.** A Fully Integrated GIS-based Model of Particle Waste Distribution

from Marine Fish-Cage Sites. Aquaculture 258, 299-311.

[www.plancton.cl](http://www.plancton.cl/) Página **4** de **13**

## .
### PLANCTON ANDINO SpA

Fonos: +56-65 2 23 50 46: +56-65 2 23 56 63 Terraplén No 869. Casilla 1036. **Puerto Varas**, Chile.
Fono/Fax: +56 -65 2 533 500. Prof. V. Gomez 2449 Int., Bordemar, **Castro**, Archipiélago de Chiloé, Chile.

Calle 1 Casa 782 Valle La Foresta, **Coyhaique**, Región de Aysén, Chile.

**Figura 1** . Batimetría y ubicación de los módulos de cultivo

En Figura 1 se observa que la profundidad aumenta desde la costa hacia el centro del Canal, llegando
hasta los 130 metros aproximadamente. En general las jaulas se localizarían sobre el veril de 40 m de
profundidad.

Así, la cantidad de alimento sedimentable dependerá de factores tales como: vector de corrientes y la
profundidad de la columna de agua (Kautsky & Folke [9] ; Gowen & Bradbury [10] ; Wiesmann et. al. [11] ; e
Iwama [12] ).

En esta modelación, DEPOMOD v2.2 predice la cantidad y tasa de Carbono final depositada en el área
de estudio expresada en **gC/m** **[2]** **/año** en el sedimento bajo las jaulas.

Con la depositación final modelada, el archivo . _out_ generado se exporta a una planilla Excel. Estos
valores se ingresan al modelo propuesto por Findlay & Watling [3], que permite calcular la demanda de
oxígeno del sedimento considerando el COT que ha quedado depositado (previa transformación a

9 **Kautsky N., & Folke C. 1989.** Management of coastal areas for a sustainable development of aquaculture. Biota 5: 1-11.
10 **Gowen, J.R., & Bradbury, N.B., 1987.** The ecological impact of salmonid farming in coastal waters: a review. Oceanogr. Mar.

Biol. Ann. Rev., 25, 563-575.
11 **Wiesmann, D.; Scheid, H; Pfeffer, E. 1988** . Water pollution with phosphorus of dietary origin by intensively fed rainbow trout

( _Salmo gairdneri, Rich_ ). Aquaculture 69. 263-270.
12 **Iwama, G.K. 1991.** Interactions between aquaculture and the environment. Crit. Rev. Environ. Contr. 21.177-216.

[www.plancton.cl](http://www.plancton.cl/) Página **5** de **13**

## .
### PLANCTON ANDINO SpA

Fonos: +56-65 2 23 50 46: +56-65 2 23 56 63 Terraplén No 869. Casilla 1036. **Puerto Varas**, Chile.
Fono/Fax: +56 -65 2 533 500. Prof. V. Gomez 2449 Int., Bordemar, **Castro**, Archipiélago de Chiloé, Chile.

Calle 1 Casa 782 Valle La Foresta, **Coyhaique**, Región de Aysén, Chile.

**mmolC/m** **[2]** **/d** ) y la disponibilidad de oxígeno. Con ello, se predice el Índice de Impacto para la producción
proyectada.

Cromey [13] señala que aportes de COT producen un enriquecimiento del sedimento cuando la depositación
se encuentra entre 36 y 365 gC/m [2] /año, mientras que con valores inferiores a este rango el impacto es
bajo. En el mismo documento se cita a Eleftheriou [14], indicando que aportes de 767 gC/m [2] /año
provocarían el enriquecimiento de la fauna.

Debido a lo anterior, si bien en el presente informe se considera la totalidad de datos entregados por el
modelo, se representa cartográficamente la mancha de dispersión de Carbono utilizando como valor
límite 36 gC/m [2] /año, ya que por sobre esta cifra, según Cromey [13], existen probabilidades que se
produzcan efectos sobre el sedimento, y la isolínea de los 767 gC/m [2] /año, aludiendo a lo expuesto por
Eleftheriou [14] .

Las fórmulas utilizadas son (Findlay & Watling [3] ):

**a) Demanda de Oxígeno (D.O) =** -32,6 + 1,1 * Carbono Depositado (mmolC/m [2] /d)
**b) Disponibilidad O** **2** **=** 736,3 + 672,6 Log * Velocidad de la Corriente
**c) Índice de Findlay & Watling (I) =** Disponibilidad de O 2 / Demanda de O 2 .

 - El índice debe ser > 1, para que el proyecto tenga un impacto ambientalmente compatible con la
capacidad del cuerpo de agua, y la disponibilidad de oxígeno pueda sustentar los procesos

asociados al bentos

 - Con un I ≈ 1, la disponibilidad y demanda de O 2 se acercan a la unidad, los impactos son

moderados.

 - I < 1, la demanda supera la disponibilidad de oxígeno, los sedimentos exhibirán características
anóxicas.

13 **Cromey, C. J.; Nickell, K.D.; Edwards, A. & Jack, I. 1998.** Modelling the Deposition and Biological Effects of Organic Carbon

from Marine Seawage Discharges. Estuarine, Coastal and Shelf Science 47: 295-308.
14 **Eleftheriou, A., Moore, D.C., Basford, D.J. & Robertson, M.R. 1982** . Underwater experiments on the effects of seawage sludge

on a marine ecosystem. Netherlands Journal of Sea Research 16: 465-473. EN: Cromey, C. J.; Nickell, K.D.; Edwards, A. & Jack,
I. 1998. Modelling the Deposition and Biological Effects of Organic Carbon from Marine Seawage Discharges. Estuarine, Coastal
and Shelf Science 47: 295-308.

[www.plancton.cl](http://www.plancton.cl/) Página **6** de **13**

## .
### PLANCTON ANDINO SpA

Fonos: +56-65 2 23 50 46: +56-65 2 23 56 63 Terraplén No 869. Casilla 1036. **Puerto Varas**, Chile.
Fono/Fax: +56 -65 2 533 500. Prof. V. Gomez 2449 Int., Bordemar, **Castro**, Archipiélago de Chiloé, Chile.

Calle 1 Casa 782 Valle La Foresta, **Coyhaique**, Región de Aysén, Chile.

**2.4. Velocidad de corrientes**

La correntometría utilizada comprende un periodo de registro continuo entre el 2 de diciembre del 2017 y
el 1 de enero del 2018, de la cual se escogieron 5 capas equidistantes entre sí, priorizando seleccionar
aquellas bajo las balsas, tomando como base la capa más profunda del estudio de corrientes, pero
considerando 1 de ellas al interior de las jaulas. Las profundidades de las capas corresponden a 13, 27,
41, 55 y 69 metros.

En las tablas 2 y 3 se entrega un resumen de las velocidades de corrientes usadas para el escenario

modelado.

**Tabla 2:** Porcentajes de frecuencia de velocidades, por rango, para cada capa de corrientes usadas.

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- En las tablas 2 y 3 se entrega un resumen de las velocidades de corrientes usadas para el escenario modelado. -->

**Tabla 2: ** Porcentajes de frecuencia de velocidades, por rango, para cada capa de corrientes usadas.**

| Clase | 13 m | 27 m | 41 m | 55 m | 69 m |
| --- | --- | --- | --- | --- | --- |
| < 1,5 cm/s | 0,00 | 0,04 | 0,00 | 0,74 | 7,17 |
| 1,5 - 3 cm/s | 0,02 | 0,02 | 0,14 | 1,79 | 22,06 |
| 3,1 - 5 cm/s | 0,04 | 0,14 | 0,27 | 3,03 | 33,34 |
| 5,1 - 10 cm/s | 0,21 | 0,37 | 1,03 | 7,99 | 35,40 |
| 10,1 - 15 cm/s | 0,45 | 0,39 | 1,07 | 7,56 | 2,00 |
| 15,1 - 20 cm/s | 0,45 | 0,39 | 0,84 | 8,15 | 0,04 |
| 20,1 - 25 cm/s | 0,72 | 0,72 | 1,01 | 6,98 | 0,00 |
| 25,1 - 30 cm/s | 0,78 | 0,54 | 1,07 | 5,72 | 0,00 |
| > 30 cm/s | 97,32 | 97,38 | 94,56 | 58,03 | 0,00 |

<!-- Estadísticas: 9 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 3:** Estadística básica de velocidades de corrientes usadas ( **cm/s** ). |Capa|13 m|27 m|41 m|55 m|69 m| |---|---|---|---|---|---| -->
<!-- FIN TABLA 2 -->


|Clase|13 m|27 m|41 m|55 m|69 m|
|---|---|---|---|---|---|
|< 1,5 cm/s|0,00|0,04|0,00|0,74|7,17|
|1,5 - 3 cm/s|0,02|0,02|0,14|1,79|22,06|
|3,1 - 5 cm/s|0,04|0,14|0,27|3,03|33,34|
|5,1 - 10 cm/s|0,21|0,37|1,03|7,99|35,40|
|10,1 - 15 cm/s|0,45|0,39|1,07|7,56|2,00|
|15,1 - 20 cm/s|0,45|0,39|0,84|8,15|0,04|
|20,1 - 25 cm/s|0,72|0,72|1,01|6,98|0,00|
|25,1 - 30 cm/s|0,78|0,54|1,07|5,72|0,00|
|> 30 cm/s|97,32|97,38|94,56|58,03|0,00|

**Tabla 3:** Estadística básica de velocidades de corrientes usadas ( **cm/s** ).

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |15,1 - 20 cm/s|0,45|0,39|0,84|8,15|0,04| |20,1 - 25 cm/s|0,72|0,72|1,01|6,98|0,00| |25,1 - 30 cm/s|0,78|0,54|1,07|5,72|0,00| |> 30 cm/s|97,32|97,38|94,56|58,03|0,00| -->

**Tabla 3: ** Estadística básica de velocidades de corrientes usadas ( **cm/s** ).**

| Capa | 13 m | 27 m | 41 m | 55 m | 69 m |
| --- | --- | --- | --- | --- | --- |
| MÁXIMA | 740,90 | 711,70 | 611,00 | 204,20 | 16,80 |
| MÍNIMA | 2,80 | 0,60 | 2,00 | 0,00 | 0,00 |
| PROM | 324,90 | 307,95 | 235,26 | 47,87 | 4,55 |
| Prom. 2 horas | 22,97 | 25,41 | 13,75 | 4,21 | 1,88 |
| D.S | 181,44 | 168,45 | 142,64 | 37,84 | 2,37 |

<!-- Estadísticas: 5 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Como se puede apreciar en la Tabla 2, la corriente de la capa más profunda utilizada en el modelo (69 m), se caracteriza por tener tener prácticamente la totalidad de los registros (99,9%) con velocidades inferiores a 15 cm/s. Esto se condice con el valor promedio calculado para dicha capa, que alcanza 4,55 cm/s (ver Tabla 3), cifra con la que se calculó el Índice de Impacto. Por otro lado, también se calculó el -->
<!-- FIN TABLA 3 -->


|Capa|13 m|27 m|41 m|55 m|69 m|
|---|---|---|---|---|---|
|MÁXIMA|740,90|711,70|611,00|204,20|16,80|
|MÍNIMA|2,80|0,60|2,00|0,00|0,00|
|PROM|324,90|307,95|235,26|47,87|4,55|
|Prom. 2 horas|22,97|25,41|13,75|4,21|1,88|
|D.S|181,44|168,45|142,64|37,84|2,37|

Como se puede apreciar en la Tabla 2, la corriente de la capa más profunda utilizada en el modelo (69
m), se caracteriza por tener tener prácticamente la totalidad de los registros (99,9%) con velocidades
inferiores a 15 cm/s. Esto se condice con el valor promedio calculado para dicha capa, que alcanza 4,55
cm/s (ver Tabla 3), cifra con la que se calculó el Índice de Impacto. Por otro lado, también se calculó el
promedio de las 2 horas con velocidades más bajas de la capa profunda, alcanzando una cifra de 1,88

cm/s.

[www.plancton.cl](http://www.plancton.cl/) Página **7** de **13**

## .
### PLANCTON ANDINO SpA

Fonos: +56-65 2 23 50 46: +56-65 2 23 56 63 Terraplén No 869. Casilla 1036. **Puerto Varas**, Chile.
Fono/Fax: +56 -65 2 533 500. Prof. V. Gomez 2449 Int., Bordemar, **Castro**, Archipiélago de Chiloé, Chile.

Calle 1 Casa 782 Valle La Foresta, **Coyhaique**, Región de Aysén, Chile.

**3.** **Resultados.**

La modelación con DEPOMOD v2.2 predice una tasa máxima depositada de 851 gC/m [2] /año y un
promedio de 59 gC/m [2] /año (Figura 2).

Asociado a esta depositación, y de acuerdo al modelo de Findlay & Watling [3], se calcula una demanda
máxima de 178 mmol O 2 /m [2] /d por el bentos. Por su parte, la disponibilidad de oxígeno en el sector es de
1.179 mmol O 2 /m [2] /d, de acuerdo al promedio de la capa profunda de corrientes, mientras que este
parámetro desciende a 920 mmol O 2 /m [2] /d al ser calculado con las 2 horas de velocidades más bajas,
para la misma capa de corrientes.

De esta forma el Índice de Impacto, arroja un valor que oscila entre 5,25 y 6,72 para la máxima
depositación, acorde al promedio de corrientes utilizado: Promedio 2 horas de velocidades más bajas de
la capa profunda, y Promedio de todos los registros de la capa profunda, respectivamente. Según los
mismos autores valores >1 reflejan condiciones aeróbicas en el sedimento.

**Tabla 4.** Resumen de resultados de la modelación.

|Item|Valor 1<br>(Corriente de fondo)|Valor 2<br>(Prom. 2 horas)|
|---|---|---|
|Máxima depositación en este proyecto (gC/m2/año)|851,00|851,00|
|Depositación promedio del área impactada (gC/m2/año)|59,21|59,21|
|Disponibilidad de Oxígeno en el fondo con corriente<br>promedio (mmol/O2/m2/día)|1.178,77|919,89|
|Demanda máxima Oxígeno con depositación máxima<br>(mmol/O2/m2/día)|175,29|175,29|
|Índice de Impacto con máxima depositación (Disponibilidad<br>de O2 / Demanda de O2)|6,72|5,25|

[www.plancton.cl](http://www.plancton.cl/) Página **8** de **13**

## .
### PLANCTON ANDINO SpA

Fonos: +56-65 2 23 50 46: +56-65 2 23 56 63 Terraplén No 869. Casilla 1036. **Puerto Varas**, Chile.
Fono/Fax: +56 -65 2 533 500. Prof. V. Gomez 2449 Int., Bordemar, **Castro**, Archipiélago de Chiloé, Chile.

Calle 1 Casa 782 Valle La Foresta, **Coyhaique**, Región de Aysén, Chile.

**3.1. Depositación de Carbono Orgánico**

En la Figura 2, se aprecia el área de impacto para la peor condición de corrientes (sin resuspensión). La
máxima depositación alcanza una concentración de 851 gC/m [2] /año, emplazada al Noreste de la
concesión.

**Figura 2** . Área de dispersión de Carbono orgánico gC/m [2] /año de acuerdo a la modelación DEPOMOD

V2.2

**Tabla 5** : Resumen estadístico para la depositación y distribución de datos de carbono gC/m [2] /año, en el

sedimento.

|Mínimo|1,00|
|---|---|
|Máximo|851,00|
|Promedio|59,21|
|D.S|105,55|
|Varianza|11.140,02|

[www.plancton.cl](http://www.plancton.cl/) Página **9** de **13**

## .
### PLANCTON ANDINO SpA

Fonos: +56-65 2 23 50 46: +56-65 2 23 56 63 Terraplén No 869. Casilla 1036. **Puerto Varas**, Chile.
Fono/Fax: +56 -65 2 533 500. Prof. V. Gomez 2449 Int., Bordemar, **Castro**, Archipiélago de Chiloé, Chile.

Calle 1 Casa 782 Valle La Foresta, **Coyhaique**, Región de Aysén, Chile.

**3.2. Índice de Impacto**

En la Figura 3 se presenta la dispersión de Carbono Orgánico en función del Índice de Impacto generado
en el modelo por el centro **Canal Almirante Martínez**, al cabo de un año productivo. La zona de mayor
impacto se emplaza adyacente al módulo, con un desplazamiento en dirección Noreste. Cabe destacar
que el Índice de Impacto es mayor a 3 en toda el área de depositación, inclusive en el sector de mayor
concentración de COT.

**Figura 3** . Área de dispersión de Carbono Orgánico en función del Índice de Impacto de acuerdo a la

modelación DEPOMOD V2.2 y fórmula propuesta por Findlay & Watling [3] .

[www.plancton.cl](http://www.plancton.cl/) Página **10** de **13**

## .
### PLANCTON ANDINO SpA

Fonos: +56-65 2 23 50 46: +56-65 2 23 56 63 Terraplén No 869. Casilla 1036. **Puerto Varas**, Chile.
Fono/Fax: +56 -65 2 533 500. Prof. V. Gomez 2449 Int., Bordemar, **Castro**, Archipiélago de Chiloé, Chile.

Calle 1 Casa 782 Valle La Foresta, **Coyhaique**, Región de Aysén, Chile.

**3.3. Análisis de los datos de Carbono entregado por Depomod**

En los porcentajes de frecuencias entre clases de gC/m [2] /año (dato entregado por Depomod), se observa
la agrupación de datos en concentraciones inferiores a los 151 gC/m [2] /año, acumulando un 56,1% de los
datos (ver Tabla 6), específicamente bajo los 36 gC/m [2] /año, mientras que las concentraciones superiores
a 767 gC/m [2] /año agrupan cerca de un 0,6% de los datos.

**Tabla 6.** Porcentajes de frecuencias de gC/m [2] /año entregado por Depomod en el centro **Canal Almirante**

**Martínez** .

|Clase gC/m2/año|Frecuencia|% Frecuencia|% Frecuencia<br>Acumulado|
|---|---|---|---|
|**0-35**|757|56,1|56,1|
|**36-150**|488|36,2|92,3|
|**151-300**|65|4,8|97,1|
|**301-450**|12|0,9|98,0|
|**451-600**|10|0,7|98,7|
|**601-766**|9|0,7|99,4|
|**> 767**|8|0,6|100,0|
|**n **|1349|||

[www.plancton.cl](http://www.plancton.cl/) Página **11** de **13**

## .
### PLANCTON ANDINO SpA

Fonos: +56-65 2 23 50 46: +56-65 2 23 56 63 Terraplén No 869. Casilla 1036. **Puerto Varas**, Chile.
Fono/Fax: +56 -65 2 533 500. Prof. V. Gomez 2449 Int., Bordemar, **Castro**, Archipiélago de Chiloé, Chile.

Calle 1 Casa 782 Valle La Foresta, **Coyhaique**, Región de Aysén, Chile.

En el Histograma, los datos de concentración de gC/m [2] /año de producción (Figura 4), tienden a
acumularse en las clases de bajos valores de COT, especialmente bajo 36 gC/m [2] /año, seguido en
frecuencia por el rango inmediatamente superior de 35 a 150 gC/m [2] /año, reafirmando lo expuesto en la

Tabla 6.

**Figura 4** . Histograma de frecuencia de Clases de concentración de carbono en el CES **Canal Almirante**

**Martínez** .

[www.plancton.cl](http://www.plancton.cl/) Página **12** de **13**

## .
### PLANCTON ANDINO SpA

Fonos: +56-65 2 23 50 46: +56-65 2 23 56 63 Terraplén No 869. Casilla 1036. **Puerto Varas**, Chile.
Fono/Fax: +56 -65 2 533 500. Prof. V. Gomez 2449 Int., Bordemar, **Castro**, Archipiélago de Chiloé, Chile.

Calle 1 Casa 782 Valle La Foresta, **Coyhaique**, Región de Aysén, Chile.

**4.** **Discusión y Conclusiones**

 - Los resultados del proyecto indican un valor máximo de depositación 851 gC/m [2] /año, valor
inferior al observado por Pérez et. al. [15], de 12.000 gC/m [2] /año bajo las jaulas en el mar.

 - Corner [8] ha informado valores de 1.550 gC/m [2] /15 días para la costa oeste de Escocia, los que son
equivalentes a 37.000 gC/m [2] /año, siendo mayores a lo observado en el presente proyecto.

 - La profundidad del área de estudio (lugar de fondeo del correntómetro) es de aproximadamente
73 m. Por otro lado, la velocidad promedio de la corriente de fondo es 4,55 cm/s
aproximadamente, mientras que las 2 horas con menor velocidad promedian 1,88 cm/s. Estos
factores son condicionantes de la depositación bajo las jaulas, ya que la combinación de ambos,
sumado con la forma del relieve marino, incide en la dispersión de las partículas, antes de que se
depositen en el sustrato.

 - Por otro lado, Findlay & Watling [3] reportan que con valores de corrientes inferiores a 0,3 cm/s
pueden ser observados, en el sedimento marino, mantos de _Beggiatoa_ spp.; los valores de
corrientes del presente proyecto son superiores a estos últimos.

 - El modelo de Findlay & Watling [3] determina dos variables muy importantes: la disponibilidad y la
demanda de O 2 en el sedimento impactado, entregando un índice para su mejor entendimiento.

 - Para el proyecto **Canal Almirante Martínez** la disponibilidad de oxígeno es de 1.178,77
mmolO 2 /m [2] /día, para el caso del cálculo realizado con la velocidad promedio de la capa profunda,
y 919,89 mmolO 2 /m [2] /día calculado con las 2 horas de corrientes más bajas de la misma capa. La
demanda es de 1.346,43 mmol/m [2] /día para el área de mayor impacto, en ambos casos. Con
estos datos, el Índice obtenido es de 6,72 y 5,25, para el primer y segundo caso respectivamente.

 - Los datos de concentración de **C/m** **[2]** **/año** entregados por Depomod, se agrupan principalmente
en las clases entre 0 y 150 **gC/m** **[2]** **/año**, corroborando el Índice de Impacto superior a 5 en el
escenario de corrientes modelado, no generando posibles condiciones anóxicas en el fondo

marino.

 - De acuerdo a la modelación Depomod e Índice de Impacto Findlay & Waitling [3], con los datos
modelados, el sector de emplazamiento del CES **Canal Almirante Martínez**, posee condiciones
oceanográficas y de fondo marino suficientes para sustentar ambientalmente una producción
máxima de 5.160 t/ciclo productivo.

15 **Pérez, O. M.; T.C. Telfer, M. C. M. Beveridge and L. G. Ross. 2002.** Geographical Information Systems (GIS) as a Simple Tool

to Aid Modelling of Particulate Waste Distribution at Marine Fish Cage Sites. Estuarine, Coastal and Shelf Science. 54, 761-768.

[www.plancton.cl](http://www.plancton.cl/) Página **13** de **13**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4.: ** Resumen de resultados de la modelación.**

| Item | Valor 1<br>(Corriente de fondo) | Valor 2<br>(Prom. 2 horas) |
| --- | --- | --- |
| Máxima depositación en este proyecto (gC/m2/año) | 851,00 | 851,00 |
| Depositación promedio del área impactada (gC/m2/año) | 59,21 | 59,21 |
| Disponibilidad de Oxígeno en el fondo con corriente<br>promedio (mmol/O2/m2/día) | 1.178,77 | 919,89 |
| Demanda máxima Oxígeno con depositación máxima<br>(mmol/O2/m2/día) | 175,29 | 175,29 |
| Índice de Impacto con máxima depositación (Disponibilidad<br>de O2 / Demanda de O2) | 6,72 | 5,25 |

**Tabla 5: ** : Resumen estadístico para la depositación y distribución de datos de carbono gC/m [2] /año, en el**

| Mínimo | 1,00 |
| --- | --- |
| Máximo | 851,00 |
| Promedio | 59,21 |
| D.S | 105,55 |
| Varianza | 11.140,02 |

**Tabla 6.: ** Porcentajes de frecuencias de gC/m [2] /año entregado por Depomod en el centro **Canal Almirante****

| Clase gC/m2/año | Frecuencia | % Frecuencia | % Frecuencia<br>Acumulado |
| --- | --- | --- | --- |
| **0-35** | 757 | 56,1 | 56,1 |
| **36-150** | 488 | 36,2 | 92,3 |
| **151-300** | 65 | 4,8 | 97,1 |
| **301-450** | 12 | 0,9 | 98,0 |
| **451-600** | 10 | 0,7 | 98,7 |
| **601-766** | 9 | 0,7 | 99,4 |
| **> 767** | 8 | 0,6 | 100,0 |
| **n ** | 1349 |  |  |
