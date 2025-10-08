---
title: Sin título
author: ACE Ltda
date: D:20210909161426-03'00'
language: es
type: manual
pages: 26
has_toc: True
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 1 INTRODUCCIÓN
  - 2 DATOS EMPLEADOS EN LA MEMORIA DE CÁLCULO
  - 3 SIMULACIÓN ESTANQUE POR ELEMENTOS FINITOS
  - 4 RESULTADOS DEL ANÁLISIS ESTRUCTURAL
  - 5 TABLA RESUMEN DE RESULTADOS
  - 6 CONSIDERACIONES FINALES
  - 7 DIMENSIONAMIENTO DE PERNOS DE ANCLAJE GRADO A-36
-->

**CAROZZI NOS**

**PLANTA DE TRATAMIENTO DE RILES**

**INGENIERIA DE DETALLES**

**ECOPRENEUR CHILE S.A.**

**MEMORIA DE CÁLCULO ESTRUCTURAL ESTANQUE SULFATO**

**DE ALUMINIO Y ESTANQUE DE SODA D1800 H2400**

**DOCUMENTO No**

**PY 209-493 M S 03**

|Revisión|Descripción|Realizado|Revisado|Aprobado|Fecha|
|---|---|---|---|---|---|
|0|Para Construcción|FF|EL|PA|17-11-2020|
|||||||
|||||||
|||||||

**APPLIED CONSULTING ENGINEERING**

**ACE Ltda.**

**Av. Pedro de Valdivia 0925**

**Fono: +56 9 81920375**

**e-mail:** **[pablo.andrade@acechile.cl](mailto:pablo.andrade@acechile.cl)**

**[www.acechile.cl](http://www.acechile.cl/)**

Memoria de cálculo para el diseño estructural de un Estanque
cilíndrico vertical de FRP de 5m3 y cuyas dimensiones son 1.800 mm
de diámetro y 2.400 mm de altura total, para el almacenamiento de

Sulfato de Aluminio a 42%.

Esta memoria ha sido solicitada por la Empresa Fibra Group Ltda., bajo
los supuestos proporcionados por la Empresa Mandante.

Esta memoria solo tiene validez bajo las condiciones de diseño y de
emplazamiento del equipo. Cualquier modificación debe ser analizada
y validada por el equipo de Diseño de ACE Ltda.

**Diseñó** **Analizó** **Aprobó** **Fecha** **Rev**

Eduardo Leal Pablo Andrade

Francisco

Fernández

30-07-2020

**ÍNDICE**

1 INTRODUCCIÓN .......................................................................................................................... 3

1.1 Objetivo ............................................................................................................................... 3
2 DATOS EMPLEADOS EN LA MEMORIA DE CÁLCULO ................................................................... 4

3 SIMULACIÓN ESTANQUE POR ELEMENTOS FINITOS .................................................................. 5

3.1 Consideraciones iniciales ..................................................................................................... 5

3.2 Determinación de los espesores en manto cilíndrico ......................................................... 5

3.3 Determinación Fondo Plano completamente soportado .................................................... 6

3.4 Condiciones de borde .......................................................................................................... 6

3.5 Condiciones de carga ........................................................................................................... 6

3.5.1 Presión hidrostática ..................................................................................................... 7

3.5.2 Diseño Sísmico; momento volcante - NCh2369-2003 ................................................ 7

3.5.3 Fuerza Dinamicas Laterales ......................................................................................... 8

3.5.4 Carga sísmica Vertical ................................................................................................ 10

3.5.5 Carga producida por la presión de Viento (NCh 432-2010) ...................................... 11

3.6 Combinaciones de carga aplicadas en Estanque ............................................................... 13
4 RESULTADOS DEL ANÁLISIS ESTRUCTURAL .............................................................................. 14

4.1 Esfuerzos máximos en Estanque ....................................................................................... 14

4.1.1 Manto cilíndrico ........................................................................................................ 14

4.1.2 Refuerzos de unión .................................................................................................... 15

4.1.3 Tapa ........................................................................................................................... 15

4.1.4 Sillas de anclaje .......................................................................................................... 16

4.2 Deformación máxima del Estanque .................................................................................. 17

4.3 Desplazamientos máximos en Estanque ........................................................................... 17

5 TABLA RESUMEN DE RESULTADOS ........................................................................................... 19

6 CONSIDERACIONES FINALES ..................................................................................................... 20

7 DIMENSIONAMIENTO DE PERNOS DE ANCLAJE GRADO A-36 .................................................. 22

7.1 Determinación de números de anclajes. ........................................................................... 22

7.2 Determinación de la fuerza en los anclajes por tracción................................................... 22

7.3 Determinación de la fuerza en los anclajes por corte ....................................................... 22

7.4 Determinación de la fuerza en los anclajes por tracción corte ......................................... 24

7.5 Consideraciones finales ..................................................................................................... 25

**Página 2**

# 1 INTRODUCCIÓN

La presente memoria de cálculo determina los espesores mínimos para la fabricación de las distintas

secciones estructurales de un Estanque cilíndrico vertical de FRP para el almacenamiento de Sulfato

de Aluminio al 42%. Esta memoria de cálculo ha utilizado como supuestos que el proceso de

fabricación empleado en la obtención de las secciones estructurales es laminado manual.

Las propiedades mecánicas del material empleado en el desarrollo de esta memoria de cálculo han

sido determinadas mediante lo presente en la normativa ASME RTP-1: “A standard for Reinforced

Plastic Corrosion-Resistant Equipment”.

La **barrera estructural**, para la fabricación del manto, tapa, fondo y vendajes de unión, se considera
la aplicación de WR800 gr/m [2], Mat450 gr/m [2] y resina vinilester BASF Palatal A430.

Para la **barrera química** de todo el equipo se ha considerado la utilización de Resina Vinilester Palatal

A430, cuya secuencia de laminado se consideró de VMM (V=Velo C y M=Mat 450).

En la secuencia de laminado manual en algunas secciones del estanque debe considerarse que

siempre se aplicará una capa de MAT y WR, alternando cada una de estos tipos de material, de no

cumplirse esta condición cambiarán las propiedades mecánicas del laminado e inhabilitará esta

memoria de cálculo. Se debe tomar en consideración que nunca se deberá laminar secuencias de

dos capas conjuntas de WR, dado que mecánicamente la unión entre estas dos capas será resina, y

con ello se disminuirán las propiedades mecánicas del laminado. La temperatura mínima para

realizar el proceso de manufactura deberá ser superior a los 5° C, con objeto de evitar la adición de

humedad durante el proceso de laminado.

Se considera que el proveedor de la Resina suministrará la asesoría técnica necesaria para la

correcta elaboración de la resina bajo condiciones ambientales críticas. Cabe destacar que el

incumplimiento de las especificaciones de elaboración de la Resina, inhabilitará los cálculos

realizados en la presente memoria.

## 1.1 Objetivo

 Determinar el espesor mínimo de las secciones estructurales que componen el estanque

cilíndrico vertical de FRP según el estándar NCh 2369, NCh 3171, NCh 432, ASTM 4097, API

650 y RTP-1.

 Determinar los esfuerzos y desplazamientos generados por la acción de las cargas según los

estándares NCh 2369, NCh 3171, NCh 432, ASTM 4097, API 650 y RTP-1.

**Página 3**

# 2 DATOS EMPLEADOS EN LA MEMORIA DE CÁLCULO

El modelo geométrico del Estanque de FRP para el almacenamiento de Sulfato de Aluminio de 5m [3]

de D1800_H2400, se obtiene del siguiente documento.

|Datos de documento de identificación Estanque de FRP|Col2|
|---|---|
|~~**Estanque**~~<br>|Estanque Sulfato de Aluminio de 5 m3|
|~~**N° Plano**~~<br>|PY 209 - 493 DW C 2|
|~~**Revisión de Plano**~~<br>|REV 4<br>|

**Tabla 1. Información de plano de fabricación del Estanque FRP**

Se considera como elemento base del cálculo de esta memoria las siguientes normativas. ASTM

4097 _"Contact Molded Glass Fiber Reinforced Resin Corrosion Resistant Tanks”_, NCh 2369-2003

_"Diseño sísmico de estructuras e instalaciones industriales"_, NCh 3171 _“Diseño estructural -_

_Disposiciones generales y combinaciones de cargas”_ y RTP-1 _“Reinforced Thermoset Plastic_

_Corrosion-Resistant Equipment”._

La Tabla 2, presenta los parámetros de cálculo iníciales para la elaboración de la memoria de cálculo,

tanto de diseño como operacionales.

|Parámetro|Magnitud|Unidad|
|---|---|---|
|~~**Diámetro Estanque**~~<br>|1,8|m|
|~~**Altura total Estanque**~~<br>|2,4|m|
|~~**Altura manto cilíndrico**~~<br>|2,2|m|
|~~**Altura Hidrostática**~~<br>|2,1|m|
|~~**Densidad del Fluido**~~<br>|1.500|kg/m3|
|~~**Factor de sobre carga**~~<br>|1,2|-|
|~~**Factor de Seguridad**~~<br>|10<br>|- <br>|

**Tabla 2. Parámetros constructivos y operacionales del estanque cilíndrico.**

La Tabla 3, presenta las propiedades mecánicas del FRP obtenidas a partir de los elementos

presentes en la normativa ASME RTP-1: _“Reinforced Thermosed Plastic Corrosion-Resistant_

_Equipment”_ .

|Tela|Parámetro|Magnitud|Unidad|
|---|---|---|---|
|**FRP**|~~**Módulo de Elasticidad**~~<br>|10.500|MPa|
|**FRP**|~~**Resistencia Última**~~<br>|105,5|MPa|
|**FRP**|~~**Factor de seguridad**~~<br>|10|-|
|**FRP**|~~**Resistencia Admisible**~~<br>|10,5|MPa|

**Tabla 3. Propiedades mecánicas del FRP**

**Página 4**

# 3 SIMULACIÓN ESTANQUE POR ELEMENTOS FINITOS

A continuación, se presentan los resultados de la simulación por elementos finitos realizada al

estanque en estudio.

## 3.1 Consideraciones iniciales

El modelo geométrico del estanque tiene simplificaciones geométricas que ayudan a la estabilidad

computacional del modelo analizado mediante el método de elementos finitos. Sin embargo, estas

simplificaciones son menores y no afectan estructuralmente el conjunto. Cabe destacar que el

elemento finito utilizado es el **Shell 181.**

Se realizará el estudio con una configuración de laminados definida, cuyos resultados se verán

reflejados en el apartado _5. Tabla resumen de resultados_ .

## 3.2 Determinación de los espesores en manto cilíndrico

La determinación teórica de los espesores del manto cilíndrico se establece de acuerdo al estándar

ASTM D3299 y ASTM D4097.

**n**

P ii
tt h
= 2SS h

**n**

⁄

**n**

FF

**n**

DDón **n** nn:

Presión cuerpo inferior

Diámetro

Tensión Ruptura FRP

Factor de diseño

**Espesor del Manto del estanque** **6** **mm**
**Tabla 4. Espesor teórico en Manto cilíndrico del Estanque**

Los espesores requeridos en cada sección se ilustran en la Figura 1.

**Manto Cilíndrico** **e =** 6 mm

**n**

**Figura 1. Espesor en Estanque cilíndrico FRP**

**Página 5**

## 3.3 Determinación Fondo Plano completamente soportado

Se considerará el siguiente espesor para el análisis mediante elementos finitos correspondientes al

fondo del estanque.

|Espesor|Magnitud|Unidad|Observación|
|---|---|---|---|
|~~**Espesor Fondo plano**~~|~~6,4~~<br>|~~mm~~<br>|~~Según estándar ASTM D4097~~<br>|

**Tabla 5. Espesor fondo estanque FRP**

## 3.4 Condiciones de borde

Respecto de las condiciones del modelo de Elementos Finitos, se han considerado las siguientes

condiciones de borde.

La Figura 2, presenta la condición de restricción de desplazamiento y la condición de apoyo fijo. La

zona destacada de color amarillo en el fondo del estanque representa la condición de restricción de

desplazamiento en el eje vertical. La segunda, corresponde a los seis puntos de apoyo fijo donde se

ubican en los 6 pernos de anclaje del estanque, demarcados de color amarillo.

**Figura 2. Condiciones de borde en Estanque**

## 3.5 Condiciones de carga

A continuación, se presentan las condiciones de carga que se aplicarán en la modelación del

estanque de FRP, como lo son, la presión hidrostática, momento volcante por sismo y cargas por

presión de viento.

**Página 6**

### 3.5.1 Presión hidrostática

Se ha considerado la presión que ejerce el fluido sobre cada una de las paredes del estanque, es

decir, el manto cilíndrico, fondo y refuerzos de unión manto/fondo.

Esta presión hidrostática, se puede apreciar en la Figura 3, la cual se ha aplicado mediante una

condición de fuerza actuando en todas las superficies interiores del estanque. Esta condición de

presión equivale a **0,03087 MPa**, aplicada a una altura hidrostática de **2,1 m** desde la base del

estanque.

**Figura 3. Presión hidrostática aplicada en Estanque**

### 3.5.2 Diseño Sísmico; momento volcante - NCh2369-2003

A continuación, se presentan los parámetros para la determinación del momento volcante,

considerando la localización geográfica zona sísmica 3 y una clasificación de suelo tipo II. El

coeficiente sismico impulsivo fue calculado tomando en cuenta el coeficiente sismico máximo ( _Tabla_

_5.7, normativa NCh 2369_ ), para el coeficiente sismico convectivo se ultilizo la ecuación 5-2,

normativa Nch 2369.

**Página 7**

|Parámetro|Valor|Observación|
|---|---|---|
|**Wt**|8.015,7|Peso del líquido (kg)|
|**D **|1,8|Diámetro (m)|
|**h col agua**|2,1|Altura (m)|
|**D/H**|0,85||
|**X1**|0,88|Altura desde el fondo del cuerpo del tanque al centroide<br>de la fuerza lateral sísmica aplicada a W1 (m)|
|**X2**|1,62|Altura desde el fondo del tanque al centroide de la fuerza<br>sísmica lateral aplicada a W2 (m)|
|**W1**|6.808,9|Peso de la masa efectiva contenida en el tanque que se<br>mueve al unísono con el cuerpo (kg)|
|**w2**|1.579,9|Peso efectivo de la masa contenida por el tanque que se<br>mueve en el primer oleaje (kg)|
|**C2**|0,3|Coeficiente sísmico lateral|
|**Ws**|300|Peso total del cuerpo del estanque (kg)|
|**Wr**|150|Peso del techo más una carga viva (kg)|
|**Tipo de suelo**|III||
|**n **|1,8|Coeficiente relativo al tipo de suelo|
|**T’**|0,62|Coeficiente relativo al tipo de suelo|
|**R **|3|Factor de modificación de la respuesta|
|**Zona sísmica**|2|Según información de Cliente.|
|**Ξ **|0,02|Razones de amortiguamiento|
|**I **|1,2|Factor de Importancia|
|**C1**|0,3|Coeficiente sísmico|
|**Ht**|2,3|Altura total del estanque (m)|
|**Xs**|1,25|Desde el fondo al centro de gravedad (m)|
|**MOMENTO**<br>**VOLCANTE EN LA BASE**|**3.343,7**<br>|**[Kg-m]**<br>|

**Tabla 6. Momento de volteo en la base del estanque.**

### 3.5.3 Fuerza Dinamicas Laterales

Las fuerzas dinámicas laterales sobre la base serán determinadas según normativa (ACI 350) como

sigue para las masas convectivo e impulsivo señaladas en la Tabla 6 y en la Figura 4:

**Página 8**

**Figura 4. Presión hidrodinámica aplicada en Estanque**

PP = CC 1 ∗ II ∗ MM 0 (carga impulsivo) y

PP = CC 2 ∗ II ∗ MM 1 (carga convectivo)

Los parámetros de diseños sísmicos han sido señalados por la empresa mandante.

|R|CC<br>mmáxx|Col3|Col4|
|---|---|---|---|
|**R **<br>|~~**ξ = 0,02**~~<br>|~~**ξ = 0,03**~~<br>|~~**ξ = 0,05**~~<br>|
|~~**1 **~~<br>|~~0,79~~<br>|~~0,68~~<br>|~~0,55~~<br>|
|~~**2 **~~<br>|~~0,60~~<br>|~~0,49~~<br>|~~0,42~~<br>|
|~~**3 **~~<br>|~~0,40~~<br>|~~0,34~~<br>|~~0,28~~<br>|
|~~**4 **~~<br>|~~0,32~~<br>|~~0,27~~<br>|~~0,22~~<br>|
|~~**5 **~~<br>|~~0,26~~<br>|~~0,23~~<br>|~~0,18~~<br>|
|~~**NOTA - Los valores indicados son válidos para la zona sísmica 3. Para las zonas sísmicas 2 y 1,**~~<br>**los valores de esta tabla se deben multiplicar por 0,75 y 0,50, respectivamente.**<br>|~~**NOTA - Los valores indicados son válidos para la zona sísmica 3. Para las zonas sísmicas 2 y 1,**~~<br>**los valores de esta tabla se deben multiplicar por 0,75 y 0,50, respectivamente.**<br>|~~**NOTA - Los valores indicados son válidos para la zona sísmica 3. Para las zonas sísmicas 2 y 1,**~~<br>**los valores de esta tabla se deben multiplicar por 0,75 y 0,50, respectivamente.**<br>|~~**NOTA - Los valores indicados son válidos para la zona sísmica 3. Para las zonas sísmicas 2 y 1,**~~<br>**los valores de esta tabla se deben multiplicar por 0,75 y 0,50, respectivamente.**<br>|

**Tabla 7. Valores máximos del coeficiente sísmico impulsivo**

Como resultado se obtiene un coeficiente sísmico máximo para el modo impulsivo fue realizado

tomando en cuenta la tabla 6, el que da como resultado de **0,3**, el que genera una carga en esa zona

de **2.451,2 kg,** tomando en cuenta una masa impulsiva de **6.808,9 kg.**

El coeficiente sísmico cálculo para el modo convectivo es de **0,3** que fue calculado tomando en

cuenta los parámetros señalados, el que genera una carga sobre la zona convectiva de **538,8 kg.**

Las curvas del momento cargas impulsivas y convectivas aplicadas en el manto del estanque se

pueden apreciar en la Figura 5.

**Página 9**

**Figura 5. Presión impulsiva y convectiva sobre el manto del estanque.**

El desglose de las cargas de corte de cada componente se puede apreciar en la Tabla 8. La carga de

corte final se calcula con la siguiente formulación QQ t **t** t **t** tt = √(Q **Q** + Q **Q** + Q **Q** ) [22] + Q **Q** [22] **.**

|Parámetro|P (kg)|I|C|Q(kg)|
|---|---|---|---|---|
|**Carga Convectiva**|1.579,9|1,2|0,3|**538,8**|
|**Carga Impulsivo**|6.808,9|1,2|0,3|**2.451,2**|
|**Carga Pared**|300|1,2|0,3|**108**|
|**Carga Techo**|150|1,2|0,3|**54**|
|**Q Total**|**Q Total**|**Q Total**|**Q Total**|**2.674,4**|

**Tabla 8. Cargas de corte producidas en el estanque.**

### 3.5.4 Carga sísmica Vertical

La acción sísmica vertical se puede considerar estática. Para el caso del estanque, es coeficiente
sísmico debe ser 2AA 0 /3gg . De este modo la fuerza sísmica vertical debe ser: FF vv = ±(2 AA 0 ⁄3gg)I **I** .

Donde P es la suma de las cargas permanentes y sobrecargas, el coeficiente de sismo vertical **es de**

**0,26** .

La carga es aplicada como se aprecia en la Figura 6.

**Página 10**

**Figura 6. Aplicación de sismo vertical**

### 3.5.5 Carga producida por la presión de Viento (NCh 432-2010)

La determinación de las presiones de viento para estanque de FRP se calcula de acuerdo a la

siguiente ecuación, que tiene como base lo establecido en la normativa NCh 432-2010.

pp = q **q** qq ff x pp − qq ii xx [(] G p **p** [) ] [ [NN] 2 ]
⁄mm

Dónde:

G p **p** = C **C** C **C** C **C** C **C** C **C** CC d **d** p **p** p **p** ppónn i **i** i **i** i **i** ii
CC PP = C **C** C **C** C **C** C **C** C **C** CC d **d** p **p** p **p** ppónn e **e** e **e** e **e** ee p **p** p **p** t **t** ttho **o**
GG ff = F **F** F **F** F **F** d **d** e **e** e **e** e **e** r **r** r **r** r **r** .
qq = P **P** P **P** m **m** m **m** mm aa b **b** b **b** b **b** b **b** b **b** e **e** e **e** e **e** e **e** ee aa u **u** uu a **a** a **a** a **a** zz s **s** s **s** ss e **e** s **s** s **s** ss

En la Figura 7, se aprecia como se calcula el coeficiente de presión externa para techos con base

circular.

**Página 11**

**Figura 7. Coeficiente de presión externa Cp**

El coeficiente de presión externa (C pp ) para techos con base circular, se encuentra estipulado en

la normativa NCh 432, y se aprecia en la Figura 8.

**Figura 8. Coeficiente de presión externa**

Las presiones se aplican simultáneamente en muros a barlovento y sotavento y en las superficies de

los techos, según lo definido en la normativa.

Los parámetros qq yy qq ii deben ser evaluados usando las categorías de exposición definidas en la

normativa NCh 432-2010.

En la Tabla 9, se aprecian las diferentes presiones de viento y con su respectivo ángulo que se aplica

en el modelo de elementos finitos.

**Página 12**

|Presion de viento aplicadas al modelo|Col2|Col3|Col4|
|---|---|---|---|
||~~**Presiones**~~<br>**negativas**|~~**Presiones**~~<br>**positivas**|~~**Presiones**~~<br>**positivas**|
|θ~~**, grados**~~<br>|0 - 90|0 - 60|61 - 90|
|~~**Presión (Pa)**~~|-377<br>|539<br>|270<br>|

**Tabla 9. Presiones de viento aplicadas al modelo**

Para el viento se utilizará una velocidad de viento de 40 m/s, equivalente a 144 Km/hr. Los valores

de las presiones y succiones serán considerados proporcionales a una magnitud denominada

_“presión básica del viento”_ a la que se puede aplicar la fórmula:

vv [2 ]
PP WW = 16

Pw = es la presión básica, en kg/m2.

v = velocidad máxima instantánea del viento, en m/s.

Lo que genera una presión básica de 95 kg/m2.

## 3.6 Combinaciones de carga aplicadas en Estanque

Para efectos de análisis del estanque, se han realizado tres tipos de combinaciones de carga

establecidas en la normativa API 650, y que se describen en la siguiente tabla:

|Casos|Combinación de cargas|Col3|
|---|---|---|
|~~**Caso 1**~~<br>|D + PH|Peso Propio + Presión Hidrostática|
|~~**Caso 2**~~<br>|D + PH + MVS|Peso Propio + Presión Hidrostática + Sismo Horizontal ±Sismo Vertical|
|~~**Caso 3**~~|D + MVV|Peso Propio + Momento de Volteo por Viento<br>|

**Tabla 10. Combinaciones de carga analizadas**

Dónde:

**D** = Carga Permanente o Peso Propio

**PH** = Presión Hidrostática

**MVS** = Momento de volteo sismo

**MVV** = Momento de volteo viento

Se consideró una sobrecarga de uso de **1kPa** uniformemente distribuida sobre el techo del

Estanque. Esta carga se aplicó para las tres combinaciones de carga establecidas en la Tabla 10.

**Página 13**

# 4 RESULTADOS DEL ANÁLISIS ESTRUCTURAL

A continuación, se presentan los resultados del análisis estructural conforme a la aplicación de la

combinación de carga del Caso 2, es decir, la carga producto del peso propio, la carga producto de

la presión hidrostática sobre los mantos del estanque y la carga generada por momento de volteo

por sismo.

Se debe aplicar una barrera química en las superficies interiores del Estanque, cuya configuración

de laminado será Velo + Mat450 + Mat450, otorgando un espesor adicional aproximado de **2,5mm**

(no se considera espesor estructural en la modelación).

## 4.1 Esfuerzos máximos en Estanque

### 4.1.1 Manto cilíndrico

La Figura 9, presenta los esfuerzos máximos principales del manto cilíndrico del estanque. De estos

resultados, se infiere que los esfuerzos alcanzan un valor máximo en tracción (S1) de **4,72 MPa** .

Destacar, que para el manto se consideró un espesor de **6 mm** fabricado en FRP.

**Figura 9. Esfuerzo máximo en Manto cilíndrico del Estanque - Caso 2**

**Página 14**

### 4.1.2 Refuerzos de unión

La Figura 10, presenta los esfuerzos máximos principales de los refuerzos de unión de FRP. De estos

resultados, se concluye que los esfuerzos alcanzan un valor máximo en tracción (S1) de **1,83 MPa** .

Destacar, que para los vendajes de rodilla superior e inferior se consideró un espesor de **6 mm** .

**Figura 10. Esfuerzo máximo en vendajes de refuerzo del Estanque - Caso 2**

### 4.1.3 Tapa

En la Figura 11, se observan los esfuerzos generados en la Tapa del estanque, la cual se consideró

con un espesor de **6 mm** . De los resultados, se infiere que el máximo esfuerzo en la tapa del

estanque producto de la aplicación de las cargas establecidas para el Caso 2, en conjunto con una

sobrecarga de uso de **1kPa** uniformemente distribuida, alcanza los **8,77 MPa** para el material FRP.

**Página 15**

**Figura 11. Esfuerzo máximo en Tapa del Estanque - Caso 2**

### 4.1.4 Sillas de anclaje

En la Figura 12, se encuentran los esfuerzos equivalentes producidos en las sillas de anclaje, cuya

fabricación está compuesta por placas de acero ASTM A36, donde el esfuerzo máximo es de **71,81**

**MPa.**

**La silla de anclaje tiene como espesor 8 mm en sus secciones laterales, crucetas y base (Acero**

**A36). El vendaje de unión silla/manto se consideró de al menos 8 mm mediante laminado manual.**

**Figura 12. Esfuerzos de von - Mises en Sillas de anclaje del Estanque - Caso 2**

**Página 16**

## 4.2 Deformación máxima del Estanque

En la Figura 13, se observa la deformación máxima del manto del estanque de acuerdo a las cargas

del Caso 2. De los resultados, se desprende que la deformación es de **0,00050806 mm/mm**, este

valor es menor a la deformación última para cargas eventuales de **0,002 mm/mm** .

**Figura 13. Deformación máxima en manto del Estanque de FRP - Caso 2**

## 4.3 Desplazamientos máximos en Estanque

En la Figura 14, se visualiza el desplazamiento generado en el estanque producto de las

combinaciones de carga establecidas en el Caso 2 (condición más desfavorable). De los resultados,

se aprecia que el desplazamiento máximo alcanza los **6,45 mm,** manifestándose en la zona superior

del estanque (tapa), el cual es bajo respecto al valor del desplazamiento admisible de **36 mm** .

**Página 17**

**Figura 14. Desplazamiento máximo en el Estanque - Caso 2**

**Página 18**

# 5 TABLA RESUMEN DE RESULTADOS

En la Tabla 12, se describen los esfuerzos y desplazamientos máximos producidos en los distintos

casos de estudio en esta memoria de cálculo estructural del Estanque, junto a sus Factores de

Seguridad respectivos.

El factor de seguridad se desprende del esfuerzo de ruptura dividido en el esfuerzo máximo

admisible del material. Para el manto cilíndrico, fondo, tapa y sillas se empleó material compuesto

Mat/WR/Mat y para las sillas de anclaje se empleó acero estructural A-36.

Para el manto de Mat/WR/Mat el factor de seguridad está en el orden de 10 según normativa ASME

-RTP1. Por condiciones de diseño para cargas extremas, se considera que los componentes del

Estanque deben alcanzar un factor de seguridad superior a 5, para el material FRP por laminado

manual.

Para las sillas de anclaje el factor de seguridad es de 1,67 según normativa AISC-ASD.

Los seis pernos de anclajes se consideraron de 7/8” de diámetro en material Acero A-36.

La Tabla 11, se observan los esfuerzos máximos de ruptura del material FRP, Laminado Manual,

según lo establecido en la normativa ASME RTP-1, Tabla 2A-3 “Minimum Values of Flat Laminates”.

|Material|Temperatura ambiente<br>(23 °C)|
|---|---|
|~~**FRP**~~<br>|105,5 [MPa]|
|~~**Acero A-36**~~<br>|250 [MPa]<br>|

**Tabla 11. Esfuerzo máximo de ruptura de materiales de fabricación de Estanque**

Los factores de seguridad (Tabla 12), se obtienen de acuerdo a las propiedades mecánicas de

tracción considerando una operación de trabajo del Estanque.

|Casos|Esfuerzo máximo|Col3|Col4|Col5|Desplazamiento<br>Máximo|FS<br>FRP|FS<br>A-36|
|---|---|---|---|---|---|---|---|
|**Casos**<br>|**Manto**|~~**Refuerzo**~~<br>**Unión**|**Tapa**|~~**Sillas de**~~<br>**Anclaje**|~~**Sillas de**~~<br>**Anclaje**|~~**Sillas de**~~<br>**Anclaje**|~~**Sillas de**~~<br>**Anclaje**|
|**Casos**<br>|[MM]|[MM]|[MM]|[MM]|~~**[**~~m<br>]|~~**- **~~<br>|~~**- **~~<br>|
|~~**Caso 1**~~<br>|4,73|1,74|9,60|44,48|7,36|~~**10,98**~~<br>|~~**5,62**~~<br>|
|~~**Caso 2**~~<br>|4,72|1,83|8,77|71,81|6,45|~~**12,02**~~<br>|~~**3,48**~~<br>|
|~~**Caso 3**~~|0,78|0,31<br>|1,59<br>|33,79<br>|1,56<br>|~~**66,35**~~|~~**7,39**~~|

**Tabla 12. Tabla resumen de resultados en casos analizados**

**Página 19**

# 6 CONSIDERACIONES FINALES

Los espesores definidos para las secciones del Manto cilíndrico, Tapa, Fondo, Refuerzo de unión y

Sillas de anclaje para los distintos casos de estudio, soportan eficientemente los esfuerzos

generados por la presión de diseño hidrostática, momento de volteo producidos por viento y sismo,

y cargas operacionales. Estos resultados han sido validados mediante el análisis por elementos

finitos. En dicho análisis, se ha validado que tanto los esfuerzos máximos no han alcanzado los

esfuerzos de diseño establecidas como criterio inicial.

Se recomienda realizar un refuerzo de unión entre el manto y fondo del estanque (refuerzo tipo

rodilla) de al menos **6 mm**, esto con el objetivo de mitigar los esfuerzos generados en la zona inferior

del manto cilíndrico producto de la presión hidrostática más momento de volteo por sismo.

Para las orejas de izaje se consideró un espesor de 8 mm en material acero A-36 y de 8 mm de

espesor para los vendajes de unión (izaje/manto) en FRP por Laminado manual.

Se debe considerar un diámetro de 7/8” para los pernos de anclaje del Estanque en calidad Acero

A36.

El factor de seguridad según normativa ASME-RTP1, se obtiene en base a la carga última del material

compuesto. Esto se debe a que los materiales compuestos, a diferencia de los materiales dúctiles

(acero), no generan carga de fluencia ni zona plástica, por este motivo la validación del diseño en

este tipo de materiales debe ser la carga última con los factores de seguridad señalados en la

normativa correspondiente.

Las cargas de viento aplicadas han sido determinadas utilizando la norma chilena NCh432: Cálculo

de la acción del viento sobre las construcciones. Para la determinación de las fuerzas sobre el equipo

se ha empleado la presión básica según la normativa antes mencionada.

En la simulación se han empleado las propiedades mecánicas del material, obtenidas según

normativa ASME-RTP1.

**Página 20**

**ANEXO PERNOS DE ANCLAJE**

**Página 21**

# 7 DIMENSIONAMIENTO DE PERNOS DE ANCLAJE GRADO A-36

## 7.1 Determinación de números de anclajes.

La cantidad de pernos de anclaje se determina en función del diámetro del estanque, a través de la

siguiente definición.

0,31*D< N < 1.57*D

Dónde: D = Diámetro del estanque (pies).

N = Número de anclajes.

Según esta definición se establece el número mínimo de 2 anclajes y un número máximo de 9

anclajes. **Se selecciona un total de 6 anclajes, distribuidos a 60° respectivamente en el perímetro**

**del estanque.**

## 7.2 Determinación de la fuerza en los anclajes por tracción

La tracción máxima en los pernos de anclaje se encuentra a través de la relación entre el momento

volcante del estanque y del diámetro (el momento se tiene que amplificar por 1,5 al estar trabajando

con clip de anclaje).

T= 1,273M/ D [2] - w t = **1.824,4 [kg/m]**

Dónde: M: Momento de volteo, en [kg-m]

D: Diámetro del estanque, en [m]

w t : ((masa cuerpo + masa techo)/ π*D), en [kg/m]

La fuerza en cada perno de anclaje es de: Tp= T(π*D/N) = **1.719,5 [kgf]** .

Considerando un área transversal de tracción de un anclaje de **7/8”**, se tiene que el esfuerzo en cada

perno alcanza un valor de **43,4 MPa** .

**Finalmente, se puede seleccionar un perno de anclaje Grado A 36 de diámetro 7/8”. Dichos**

**anclajes poseen un esfuerzo de fluencia de 250 MPa.**

## 7.3 Determinación de la fuerza en los anclajes por corte

El corte basal, se obtiene de la normativa API 650 y se describe en la Tabla 1.

|Parámetro|Valor|Observación|
|---|---|---|
|**Wt**|8.015,7|Peso del líquido (kg)|
|**D **|1,8|Diámetro (m)|

**Página 22**

**T** **T** **Q** **Q** **Q** **Q** **6** **k**

**T** **T** **Q** **Q** **Q** **Q** **6** **k**

|h col agua|2,1|Altura (m)|
|---|---|---|
|**D/H**|0,85||
|**X1**|0,88|Altura desde el fondo del cuerpo del tanque al centroide<br>de la fuerza lateral sísmica aplicada a W1 (m)|
|**X2**|1,62|Altura desde el fondo del tanque al centroide de la fuerza<br>sísmica lateral aplicada a W2 (m)|
|**W1**|6.808,9|Peso de la masa efectiva contenida en el tanque que se<br>mueve al unísono con el cuerpo (kg)|
|**w2**|1.579,9|Peso efectivo de la masa contenida por el tanque que se<br>mueve en el primer oleaje (kg)|
|**C2**|0,3|Coeficiente sísmico lateral|
|**Ws**|300|Peso total del cuerpo del estanque (kg)|
|**Wr**|150|Peso del techo más una carga viva (kg)|
|**Tipo de suelo**|III||
|**n **|1,8|Coeficiente relativo al tipo de suelo|
|**T’**|0,62|Coeficiente relativo al tipo de suelo|
|**R **|3|Factor de modificación de la respuesta|
|**Zona sísmica**|2|Según información de Cliente.|
|**Ξ **|0,02|Razones de amortiguamiento|
|**I **|1,2|Factor de Importancia|
|**C1**|0,3|Coeficiente sísmico|
|**Ht**|2,3|Altura total del estanque (m)|
|**Xs**|1,25|Desde el fondo al centro de gravedad (m)|
|**MOMENTO**<br>**VOLCANTE EN LA BASE**|**3.343,7**|**[Kg-m]**|

**Tabla 1. Cálculo de momento volcante según API 650.**

**T** **T** **Q** **Q** **Q** **Q** **6** **k**

El corte basal total, se obtiene de la ecuación de la normativa ACI 350,

Dónde QQ T **T** T **T** TT = √(Q **Q** + Q **Q** + Q **Q** ) [22] + Q **Q** [22] = 22. 6 **6** 66, 44[k **k** kk]

|Parámetro|P (kg)|I|C|Q(kg)|
|---|---|---|---|---|
|**Carga Convectiva**|1.579,9|1,2|0,3|**538,8**|
|**Carga Impulsivo**|6.808,9|1,2|0,3|**2.451,2**|
|**Carga Pared**|300|1,2|0,3|**108**|
|**Carga Techo**|150|1,2|0,3|**54**|
|**Q Total**<br>|**Q Total**<br>|**Q Total**<br>|**Q Total**<br>|**2.674,4**|

**Tabla 2. Cargas de corte producidas en el estanque.**

**Página 23**

**Considerando un perno de 7/8’’ de diámetro y un largo efectivo de entierro de 9”, al estar**

**trabajando con clip de anclaje se realizará una amplificación de carga según lo estipulado en la**

**normativa Nch 2369.**

Aplicando lo estipulado en el apartado **8.6.3.** b de la **Norma NCh 2369, el corte basal debe ser**

**distribuido en dos pernos activos (1/3) del número total de pernos de anclaje en el equipo**,

generando un corte basal de 2.005,7 [kg]

**p** **p** **0** **K**

**f**

**F** **n** [F] **[n]** **[f]**

**n**

**F**

**K** **T** **s** **s** **s** **T** **K**

QQ
QQ(p **p** p **p** pp) = ~~(~~ **0** **K**

**f**

**F** **n** [F] **[n]** **[f]**

**n**

**F**

**K** **T** **s** **s** **s** **T** **K**

**p** **p** ~~)~~ ∗ 1,5 = 22. 0 **0** 00, 77 [K **K** KK]

**f**

**F** **n** [F] **[n]** **[f]**

**n**

**F**

**K** **T** **s** **s** **s** **T** **K**

**p** **p** **0** **K**

2

**f**

**F** **n** [F] **[n]** **[f]**

**n**

**F**

**K** **T** **s** **s** **s** **T** **K**

**p** **p** **0** **K**

El esfuerzo a corte sísmico es de **79,2 [MPa]** para el tercio del sistema de anclajes **.**

Considerando un perno de anclaje de 7/8” de diámetro, según método ASD, se tiene una carga

0,4∗f **f**
máxima de resistencia a corte (Q solicitante=2.005,7 [kgf] < - AA = 3.181,1 [kgf]), por lo tanto,

2

**se verifica el cumplimiento** del sistema de anclaje por método ASD.

Según lo estipulado en la normativa Nch 2369, apostrofe 8.6.3. Se exceptúan de las exigencias de

llaves de corte, a bases de estanques y equipos con esfuerzo de corte inferior a 50 kN; en este caso

se aceptará tomar el 100% del corte con los pernos, considerando activos un tercio del número total

de pernos.

## 7.4 Determinación de la fuerza en los anclajes por tracción corte

La tensión límite de tracción por norma ASD diseño a tracción (A36) es:

[∗ f] **[f]** [ < ] [300]
F **F** = 1,3FF n **n** [−] [ΩF][F] [n] **[n]**

FF n **n**

Dónde: _Ft_ es la resistencia del perno a tracción = 300 [MPa]

_Fv_ es la resistencia del perno al corte = 180 [MPa]

F **F** = 267,1 < 300

La interacción de tracción-corte:

TT = φ(0,75) ∗ Ft ∗ A(área) = 5.282,7 [Kg] Para los 6 anclajes.

La capacidad de perno a tracción es:

TT = 5.282,7 [K **K** KK] > T **T**, s **s** s **s** s **s** T **T** = 1.719,5[K **K** KK]

**Página 24**

**Por tanto, se verifica que la solicitación interacción tracción - corte es mayor que las solicitaciones**

**generadas por tracción.**

## 7.5 Consideraciones finales

De lo expuesto anteriormente, se infiere que:

 - Se deberá seleccionar **un perno de anclaje A36 de 7/8” de diámetro y de 9” de largo**

### efectivo de entierro.

 - El perno señalado tiene una resistencia a la tracción para una carga máxima por perno de

29.072 [kgf] según método ASD, lo cual es mayor que la carga admisible señalada en el

punto 7.2 equivalente a 11.341,2 Kgf, cumpliendo los requeriemientos del perno.

El sistema de anclaje del Estanque vertical de FRP, presenta las siguientes características:

|Característica|Col2|Observación|
|---|---|---|
|~~**Perno**~~<br>|Acero A36||
|~~**No de Anclajes**~~<br>|6|Distribuidos a 60°|
|~~**Diámetro**~~<br>|7/8”|Calidad A-36|
|~~**Entierro**~~|9”<br>|Entierro efectivo<br>|

**Tabla 3. Parámetros de diseño de pernos de anclaje**

**Página 25**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2.: Parámetros constructivos y operacionales del estanque cilíndrico.****

| Tela | Parámetro | Magnitud | Unidad |
| --- | --- | --- | --- |
| **FRP** | ~~**Módulo de Elasticidad**~~<br> | 10.500 | MPa |
| **FRP** | ~~**Resistencia Última**~~<br> | 105,5 | MPa |
| **FRP** | ~~**Factor de seguridad**~~<br> | 10 | - |
| **FRP** | ~~**Resistencia Admisible**~~<br> | 10,5 | MPa |

**Tabla 11.: Esfuerzo máximo de ruptura de materiales de fabricación de Estanque****

| Casos | Esfuerzo máximo | Col3 | Col4 | Col5 | Desplazamiento<br>Máximo | FS<br>FRP | FS<br>A-36 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Casos**<br> | **Manto** | ~~**Refuerzo**~~<br>**Unión** | **Tapa** | ~~**Sillas de**~~<br>**Anclaje** | ~~**Sillas de**~~<br>**Anclaje** | ~~**Sillas de**~~<br>**Anclaje** | ~~**Sillas de**~~<br>**Anclaje** |
| **Casos**<br> | [MM] | [MM] | [MM] | [MM] | ~~**[**~~m<br>] | ~~**- **~~<br> | ~~**- **~~<br> |
| ~~**Caso 1**~~<br> | 4,73 | 1,74 | 9,60 | 44,48 | 7,36 | ~~**10,98**~~<br> | ~~**5,62**~~<br> |
| ~~**Caso 2**~~<br> | 4,72 | 1,83 | 8,77 | 71,81 | 6,45 | ~~**12,02**~~<br> | ~~**3,48**~~<br> |
| ~~**Caso 3**~~ | 0,78 | 0,31<br> | 1,59<br> | 33,79<br> | 1,56<br> | ~~**66,35**~~ | ~~**7,39**~~ |

**Tabla 1.: Cálculo de momento volcante según API 650.****

| Parámetro | P (kg) | I | C | Q(kg) |
| --- | --- | --- | --- | --- |
| **Carga Convectiva** | 1.579,9 | 1,2 | 0,3 | **538,8** |
| **Carga Impulsivo** | 6.808,9 | 1,2 | 0,3 | **2.451,2** |
| **Carga Pared** | 300 | 1,2 | 0,3 | **108** |
| **Carga Techo** | 150 | 1,2 | 0,3 | **54** |
| **Q Total**<br> | **Q Total**<br> | **Q Total**<br> | **Q Total**<br> | **2.674,4** |
