---
title: Sin título
author: ECOGESTION
date: D:20171116143423-03'00'
language: unknown
type: report
pages: 21
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MODELACIÓN PLUMA DE DESCARGA PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS MONTE AGUILA ESTERO MONTE AGUILA
-->

|Col1|MODELACIÓN DESCARGA<br>PTAS MONTE AGUILA|No DOCUMENTO<br>242017|EDICIÓN 1|
|---|---|---|---|
||**MODELACIÓN DESCARGA**<br>**PTAS MONTE AGUILA**|Fecha de emisión:16/11/2017|Emitido por: Ecogestión<br>Ambiental Ltda.|

# MODELACIÓN PLUMA DE DESCARGA PLANTA DE TRATAMIENTO DE AGUAS SERVIDAS MONTE AGUILA ESTERO MONTE AGUILA

**Preparado**

**por**

Concepción, 16 de noviembre de 2017

1

**MODELACION DE LA DESCARGA DE RILES**

**I. ANTECEDENTES**

El presente informe analiza los resultados obtenidos de la modelación hidráulica de la pluma de
descarga del efluente proveniente planta de tratamiento de aguas servidas (PTAS), MONTE
AGUILA, que se ubica al final de la calle San Sebastian, hacia el sur oeste de la ciudad de
MONTE AGUILA, provincia del Biobío. En la Figura 1 se muestra la ubicación de la PTAS
MONTE AGUILA, indicando el punto de descarga de aguas tratadas al Estero Monte Aguila,
ubicado en las coordenadas UTM E 727133 - N5892433 (Huso 18H).

La descarga, corresponde a un ducto de 315 mm de diámetro, que vierte su efluente a la Estero
Monte Aguila a través de una descarga superficial.

La descarga de un efluente en un cuerpo receptor (natural o artificial), dependiendo de su
naturaleza y composición físico-química, aporta una carga contaminante al cuerpo receptor o un
aporte de energía (temperatura), cuyo comportamiento, en duración y extensión, dependerá de
una serie de variables que se conjugan en los procesos de dilución y difusión, tales como el
comportamiento hidrodinámico del cuerpo receptor, las concentraciones de los parámetros
asociados a la descarga, las condiciones físicas de la descarga, volúmenes de descarga, entre

otros.

**Figura 1.** Ubicación de la descarga de la PTAS MONTE AGUILA, Estero Monte Aguila (E0
Descarga).

2

**II. OBJETIVOS DE LA MODELACION**

El objetivo del presente estudio es determinar el comportamiento dinámico de la pluma de
descarga de las aguas servidas al Estero Monte Aguila en la localidad de MONTE AGUILA,
provincia del Biobío.

El efecto generado por la descarga del efluente se determinará en base al cumplimiento de la
Norma de emisión vigente en Chile, D.S. N° 90/00, en función de los parámetros la DBO 5 como
condición de descarga.

La modelación de la dilución de la descarga del efluente busca evaluar el comportamiento de ésta
en el cuerpo receptor de manera de definir el área de influencia directa de la descarga para efectos
de dicho componente. El área de influencia se define como aquella requerida para lograr los
requerimientos mínimos de dilución del efluente. El proceso de dilución se lleva a cabo en dos
fases: dilución de campo cercano y dilución de campo lejano. La primera, se relaciona con la
mezcla turbulenta que tiene lugar en el penacho que se genera en la salida de la descarga, producto
de la velocidad (momentum) del chorro. En esta fase se logra la mayor y más eficiente dilución,
y es en ésta donde influyen las variables de diseño del sistema.

Una vez que el efluente es diluido por los procesos de mezcla turbulenta del campo cercano, el
proceso pasa a la dilución de campo lejano. En este proceso, la pluma de la descarga es
transportada por el flujo que induce una dilución adicional de advección-difusión. En esta
condición, la pluma de descarga se independiza de la forma de descarga y su comportamiento
queda gobernado por los patrones hidráulicos del cuerpo receptor, la capacidad de dispersión
turbulenta del medio y la fuerza gravitacional relativa que se ejerce sobre el efluente de mayor

densidad.

3

**III. METODOLOGÍA DE LA MODELACIÓN HIDRÁULICA DE LA PLUMA DE**

**DESCARGA.**

La dilución de la pluma, generada por el momentum de la descarga y los efectos boyantes que
ocurren entre el punto de salida y el cuerpo receptor, se define como dilución inicial, y la región
en que esto ocurre se define como el campo cercano. El campo cercano se modeló utilizando el
modelo CORMIX v 10.0.0 (R. L. Doneker & G. H. Jirka).

CORMIX es una suite de modelos para el análisis, predicción y diseño de descargas en diversos
tipos de cuerpos de agua, así como en la atmósfera. El modelo se desarrolló originalmente en
1988, y su uso, extendido a nivel mundial, ha permitido su mejora constante, de la mano con la
validación de sus resultados, a través de gran cantidad de proyectos y casos de estudio. La suite
CORMIX emplea un sistema experto sobre la base de la clasificación de flujos, utilizando escalas
de longitud para determinar la interacción descarga/medio y el proceso del flujo que controla la
mezcla inicial de campo cercano y la transición al comportamiento en campo lejano (región de
difusión pasiva).

Respecto a la modelación de la dilución de la pluma de DBO se utilizó las condiciones de descarga
post tratamiento, utilizando como condiciones de entrada, morfológicas del cauce receptor (Estero
Monte Aguila), las características hidráulicas del cauce y las condiciones del efluente de descarga.

El modelamiento de la condición hidráulica del oxígeno disuelto en el cauce se realizó a través de
la modelación matemática de la relación decaimiento de la DBO y desoxigenación y reaireación
del cauce, a través de la ecuación diferencial de la curva de variación de oxígeno disuelto (DO
curva de hundimiento) se deriva. La solución de esta ecuación diferencial puede demostrarse que
es esencialmente el mismo que el de la bien conocida ecuación de Streeter-Phelps (Streeter y
Phelps, 1925). A diferencia de este último, la ecuación diferencial derivada en el presente
documento se puede resolver numéricamente y, por lo tanto, no requiere la integración. Por otra
parte, la ecuación diferencial es válida para todas las constantes de desoxigenación y la
oxigenación, a diferencia de la ecuación de Streeter-Phelps, que es indefinido cuando estas
constantes son iguales.

4

**ECUACIÓN DE LA DEMANDA DE OXÍGENO**

El decaimiento exponencial de la demanda de oxígeno puede ser modelado como sigue
(Tchobanoglous y Schroeder, 1985):

D = D u e [−k] [d] [∗t]

Dónde:

D = Demanda bioquímica de oxígeno (DBO) (mg/L);
Du = DBO final inmediatamente aguas abajo de la descarga del efluente (mg/L);
Kd = constante de desoxigenación (d -1);
t = tiempo (d).

Luego, la ecuación diferencial para la demanda de oxígeno es:

dD

dt [= −k] [d] [ ∗D] [u] [e] [−k] [d] [∗t]

Utilizando la regla de la cadena, en busca de una solución numérica, la ecuación de la demanda
de oxígeno se convierte en el dominio espacial:

[DD] dx ~~[)]~~ [ (dx] dt

( [DD] dx

dt ~~[)]~~ [ = −k] [d] [∗D] [u] [e] [−k] [d] [∗t]

~~(~~ [dD] dx

[dD] dx [) = −] ~~[(]~~ [k] v [d]

[d]

v

v ~~[)]~~ [ ∗D] [u] [e] [−(k] [d]

v [d] ~~[)]~~ [∗x]

Dónde:

x = distancia a lo largo del caudal, medida aguas abajo de la descarga de efluentes (m);
v = velocidad del flujo (m/d).

**UMBRAL DE DBO**

En el umbral, de aguas arriba del caudal se tiene que el balance de masas lleva a:

D u = [(Q] (Q [s] [D] [s] s [+ Q] + Q [e] e [D] ) [e] [)]

Dónde:

Du = DBO final, inmediatamente aguas abajo de la descarga del efluente (mg/L);

5

Qs = descarga efluente (m [3] /s);
Ds = DBO en la corriente, inmediatamente aguas arriba de la descarga (mg/L);
Qe = descarga de efluentes (m [3] /s);
De = DBO de descarga del efluente (mg/L);

Suponiendo que el flujo de aguas arriba está limpio: Ds ≅ 0:

D u = Q e
~~(~~ (Q s + Q e ) [) D] [e]

**ECUACIÓN DE SUMINISTRO DE OXÍGENO**

La ecuación diferencial para el suministro de oxígeno en el caudal del cuerpo receptor puede ser
modelado como sigue (Tchobanoglous y Schroeder, 1985):

~~(~~ [dS] dt ~~[)]~~ [ = k] [o] [(S] [s] [−S)]

Dónde:

ko = coeficiente de oxigenación constante (d -1);
S s = concentración de oxígeno disuelto a saturación, una función de la temperatura, la salinidad,
y la presión atmosférica (mg/L);
S = concentración de oxígeno disuelto (mg/L).

Luego, el valor del diferencial (Ss - S) corresponde al déficit de oxígeno.
El uso de la regla de la cadena, la ecuación de suministro de oxígeno se convierte en el dominio
espacial:

(dx [dS]

dx [dS][) = ] ~~[(]~~ [k] v [o]

[o]

v [) (S] [s] [−S)]

**ECUACIÓN DE LA VARIACIÓN DE OXÍGENO**

La variación del oxígeno en el espacio viene dada por:

~~(~~ dx [do]

dx [do] ~~[)]~~ [ = (dS] dx

dx ~~[)]~~ [ + (dD] dx

dx ~~[)]~~

6

(dx [do]

dx [do] ~~[)]~~ [ = ] ~~[(]~~ [k] v [o]

[o]

v [) (S] [s] [−S) −(k] v [d]

v

v [d] ~~[)]~~ [ ∗D] [u] [e] [−(k] [d]

v [d] ~~[)]~~ [∗x]

Dónde:

S = concentración de oxígeno disuelto (mg/L).

Desde S = O:

~~(~~ dx [do]

dx [do] ~~[)]~~ [ = ] ~~[(]~~ [k] v [o]

[o]

v ~~[)]~~ [ (S] [s] [−O) −] ~~[(]~~ [k] v [d]

[d]

v

v ~~[)]~~ [ ∗D] [u] [e] [−(k] [d]

v [d] ~~[)]~~ [∗x]

En un volumen de control (alcance computacional) de longitud L (m), con el índice (j) de aguas
arriba y el índice (j +1) aguas abajo:

~~(~~ [O] [j][1] [ −O] L [j]

[k] v [o] ~~[)]~~ [ (S] [s] [−O] [j] [) −] ~~[(]~~ [k] v [d]

[ −O] [j]

L ) = ~~(~~ [k] v [o]

[d]

v

v [) ∗D] [u] [e] [−(k] [d]

v [d] ~~[)]~~ [∗x] [j+1]

O j1 = O j
+ L( [k] v [o]

[o]

v ~~[)]~~ [ (S] [s] [−O] [j] [) −(k] v [d]

v

v [d] ~~[)]~~ [ ∗D] [u] [e] [−(k] [d]

v [d] ~~[)]~~ [∗x] [j+1]

**DO INICIAL**

Para j = 0: O j = O 0

En el umbral aguas arriba, un balance de masas lleva a:

O 0 =

(Q s O s + Q e O e )

(Q s + Q e )

Dónde:

O0 = concentración de oxígeno disuelto inmediatamente aguas abajo de la descarga del efluente
(mg/L);
Qs = descarga corriente (m [3] /s);
Os = concentración de oxígeno disuelto en la corriente, inmediatamente aguas arriba de la
descarga del efluente (mg/L);
Qe = descarga de efluentes (m [3] /s);
Oe= concentración de oxígeno disuelto de la descarga del efluente (mg/L);

Suponiendo que el efluente es anóxico: O e ≅ 0:

O 0 Q s
= [(Q s + Q e ) ~~[]]~~ [ O] [s]

7

**COMPARACIÓN CON LA ECUACIÓN STREETER-PHELPS**

La forma clásica de resolver la ecuación de variación de oxígeno disuelto es la ecuación de
Streeter-Phelps, que se remonta a 1925 (Streeter-Phelps, 1925; Tchobanoglous y Schroeder,
1984).

La ecuación de Streeter-Phelps es una ecuación algebraica derivada mediante la integración de la
ecuación diferencial que rige la variación de oxígeno. La ecuación diferencial derivada en el
presente estudio se basa en los mismos principios que la de Streeter-Phelps. Sin embargo, la
ecuación diferencial no está integrado como en el caso de Streeter-Phelps, sino que se resuelve
directamente, usando diferencias finitas. En la mayoría de los casos, ambos métodos darán lugar
a la misma respuesta. Cabe destacar que la ecuación de Streeter-Phelps sufre está sin definir para
valores iguales de las constantes de la oxigenación y desoxigenación, mientras que el método
numérico (este artículo) no lo es. Por lo tanto, el método numérico es un mejor predictor que el
modelo de Streeter-Phelps, aplicable para todas las constantes de oxigenación y desoxigenación,
independientemente de sus valores.

**Características y condiciones de descarga del efluente superficial**

Los datos y las condiciones de entrada del modelo son los que se resumen del reporte de sesión
presentada en el Apéndice I, donde se reportan los datos del ducto de descarga y las condiciones
físicas e hidráulicas del cuerpo receptor.

8

**IV. RESULTADOS**

Modelación de la pluma de descarga.

Los resultados de la modelación del efluente muestran las condiciones de dilución la pluma en el
cuerpo receptor, por cuanto el comportamiento de la descarga del DBO 5 asociados al efluente,
tendrán efecto sobre la calidad del cauce (Estero Monte Aguila), en términos de las condiciones
ambientales de dicho cuerpo de agua, expresados en niveles de oxígeno disuelto, presencia de
materia orgánica en la columna de agua, entre otros.

En tal sentido, se consideró la modelación de la condición del efluente con una concentración de

descarga de DBO 5, correspondiente al efluente tratado en la PTAS de MONTE AGUILA, según
se detalla en el Apéndice I.

En efecto, la modelación hidráulica de la pluma busca detectar la disminución, por efecto de la
dilución de la pluma, tanto en el campo cercano (área inmediata al punto de descarga), como en
el lejano.

Los resultados de la modelación hidráulica de la pluma de descarga en los distintos planos
dimensionales (3D) se reportan en la Figura 2, donde se presenta una aproximación gráfica del
comportamiento de la pluma en el cuerpo receptor en condiciones consideradas en la modelación,
donde se presentan los diferentes planos del comportamiento de la pluma en el cuerpo receptor.

**Figura 2.** Planos 3D de la pluma hidráulica de descarga del efluente, plano 3D vista superior desde
el punto de descarga en dirección del caudal del Estero Monte Aguila (plano lateral).

9

La figura anterior muestra un plano espacial de la dinámica de la pluma considerando la
configuración general de la dilución y dispersión de la descarga en condiciones de operación
regular, donde es posible obtener una primera aproximación gráfica del comportamiento de la
pluma en el cauce desde el punto de descarga hacia la dirección del flujo del Estero Monte Aguila,
donde es posible apreciar que en el campo cercano, inferior a los 4 metros se mantiene una
concentración promedio entre los 10,0 mg/L, y se observa una pluma en condición de disminución
de la concentración hasta llegar a valores cercanos a los niveles basales a una distancia de los
17,74 metros desde el punto de descarga.

Los resultados del comportamiento de la pluma asociada a la carga contaminante del RIL para el
parámetro DBO 5, se presentan en la Figura 3, para la representación de la Concentración y en la
Figura 4 en términos del comportamiento de la dilución de la descarga, para la condición de campo

cercano.

**Figura 3.** Comportamiento de la pluma de descarga del efluente en el campo cercano y campo
lejano del punto de descarga DBO5 (mg/L) de PTAS MONTE AGUILA en el Estero Monte
Aguila.

El comportamiento hidráulico del efluente al cuerpo receptor obtenido de la modelación del

DBO5, da cuenta de una condición de un decaimiento sostenido de la concentración del efluente

desde el punto de descarga. Dicha condición, según se reporta en la Figura 3, muestra que la
pluma, una muy rápida disminución de su concentración en el cuerpo receptor en el punto de
descarga para alcanzar la condición basal del cauce antes de los 20 m aguas abajo de la descarga,
condición que se mantiene estable, aguas debajo de la descarga.

10

Asimismo, la condición de decaimiento de la concentración del DBO 5, considerando la condición

conservativa del parámetro en el cuerpo receptor, es el resultado de un conjunto de procesos
fisicoquímicos y biológicos que participan en la dilución del efluente, cuya característica y
comportamiento se presentan en la Figura 4.

**Figura 4.** Comportamiento de la dilución de la pluma de descarga del efluente del punto de
descarga DBO5 (mg/L) de PTAS MONTE AGUILA en el Estero Monte Aguila.

Respecto a la condición de dilución presentada en la figura anterior, es importante señalar que el
modelo CORMIX, considera como condición de descarga un modelo estado estacionario, que
representa únicamente el decaimiento por efecto de la dilución y dispersión respondiendo a las
características y condiciones físicas de la intersección del flujo del efluente y el cuerpo receptor.

Sobre el particular de la pluma en el cuerpo receptor, dichos valores es posible evidenciarlos en
la isocurva de concentración donde se observa la concentración remanente en el cuerpo receptor
en un gradiente de 0,5 metros desde el punto de descarga hasta una distancia de 60 m, con valores
menores a 2 mg/L a partir de los 20 m desde el punto de descarga (Figura 5).

La tasa de dilución de la pluma muestra que en los primeros 0,5 metros desde el punto de descarga
en un comportamiento exponencial, se obtiene una condición de dilución S=3,23, la dilución (S)
que indica el número de veces que la pluma se diluye respecto de la condición inicial de descarga,
para luego presentar un comportamiento de crecimiento lineal, hasta una distancia modelada de
hasta 60 metros desde el punto de descarga, donde la dilución resultante es S=28,3.

11

Las Figuras 3 y 4 muestran claramente el comportamiento de las plumas de descarga, la cual se
mezcla en el cuerpo de agua receptor, logrando una dilución en el campo lejano, donde en los
primeros metros, desde el punto de descarga, se produce una notable dilución de dicha pluma, lo
cual es resultado de dilución y decaimiento presentada en las gráficas respectivas, cuya
representación en términos de las Isolíneas de concentración en el cuerpo receptor se presentan en
la Figura 5.

**Figura 5.** Isolineas de concentración de la pluma de descarga (DBO 5 ) aguas abajo del punto de
descarga PTAS MONTE AGUILA en el Estero Monte Aguila

12

Para el caso de la pluma de dilución en un campo de isocurva de dilución que dan cuenta de las
concentraciones presentadas en la figura anterior, se presentan en la Figura 6.

**Figura 6.** Isolineas de dilución de la pluma de descarga (DBO 5 ) aguas abajo del punto de descarga
PTAS MONTE AGUILA en el Estero Monte Aguila.

La condición del comportamiento de la pluma del efluente en el cuerpo receptor considerando la
condición hidráulica del cuerpo receptor y la interacción entre la relación Oxígeno DisueltoDBO 5, se obtuvo mediante la modelación hidráulica de ambos parámetros, para lo cual se utilizó
un modelo matemático que estima la curva de oxígeno disuelto en una corriente de agua, bajo los
principios del modelo de Streeter-Phelps.

**RELACIÓN DBO - OD EN EL CUERPO RECEPTOR**

Los resultados de dicho modelo permitieron tener los descriptores del comportamiento de los
parámetros OD (oxígeno disuelto) y DBO 5 (como expresión de la carga orgánica) en el cuerpo
receptor (Estero Monte Aguila), inmediatamente aguas abajo del punto de descarga del efluente.
Para efectos de modelación se utilizó los parámetros de entrada del modelo descritos en la Tabla
1 señalada precedentemente.

Los resultados obtenidos del modelo son representados en la Figura 7, en el cual se muestra el
comportamiento espacial de la curva de oxígeno, cuyo comportamiento en los primeros 100
metros desde la descarga del efluente de la planta de tratamiento de ESSBIO, indica una tendencia
al aumento del valor de saturación de oxígeno en una relación aproximadamente lineal, en
respuesta al decaimiento de la DBO, en una relación exponencialmente inversa.

13

Consecuentemente con el aumento de los niveles de oxígeno en el cuerpo receptor, se produce un
aumento sostenido del decaimiento de la DBO en niveles que van más allá de los resultados de
modelación de la pluma presentada por CORMIX, lo cual es consecuente con los resultados de
los monitoreos de campo de la DBO 5 en el Estero Monte Aguila aguas debajo de la descarga con
valores registrados que están incluso más abajo del límite de detección a los 100 metros aguas
abajo del punto de descarga.

**Figura 7.** Curva de decaimiento oxígeno disuelto - DBO 5 en el cuerpo receptor aguas debajo del
punto de descarga del efluente

El decaimiento de la curva de DBO5, en el tiempo, considerando las constantes de aireación y
desoxigenación del efluente, se presentan en la Figura 8.

14

**Figura 8.** Curva de decaimiento neto y tasas de consumo DBO 5 en el Estero Monte Aguila, en
función de constante de aireación (Kr) y de desoxigenación (Kd).

15

**V. CONCLUSIONES GENERALES**

Según se muestra en los resultados, el comportamiento de la pluma de descarga del efluente,
muestra un área de impacto marcadamente definida en el cuerpo receptor, donde la condición de
descarga de la pluma, en función del DBO5 (mg/L) presentan un comportamiento hidráulico con
notables condiciones de abatimiento de la concentración en el punto de descarga del efluente, con
niveles de dilución notablemente altos en el punto exacto de la descarga, para luego alcanzar
niveles basales a partir de una distancia aproximada de 20 metros aguas abajo del punto de
descarga, produciendo una baja sostenida en la concentración para el caso del DBO 5, en el punto
de descarga y área inmediatamente adyacente, manteniendo valores menores a 2 mg/L a una
distancia aproximadamente antes de los 20 m aguas debajo de la descarga del Estero Monte
Aguila.

Asimismo, los resultados del estudio del comportamiento de la pluma de dilución, considerando
un modelo bidimensional de la condición de descarga, confirma la situación de una condición
reducida de extensión de la pluma en el cuerpo receptor, con efecto en un área reducida al punto
descarga y al eje central de la pluma (centerline).

Lo anterior, define la condición efecto local de la descarga en el Estero Monte Aguila, condición
que se traduce en un área de afectación impacto acotado (aproximadamente de 3-20 metros desde
el punto de descarga del efluente) en condiciones detectables de DBO 5 y confinado a dicho
punto, destacando que concentraciones cercanas al nivel basal se registra a una distancia de 20 m
desde el punto de descarga.

La curva de saturación de Oxígeno disuelto (OD) y decaimiento del DBO 5 presentadas en las
Figuras 7 y 8, donde el modelo de Streeter & Phelps, sobre la base de los datos modelados permiten
evaluar el comportamiento de los niveles de oxígeno del cuerpo receptor por efecto de una descarga
de efluente con una carga contaminante orgánica, y el decaimiento de la curva del DBO en el
trayecto del cauce del Estero Monte Aguila aguas abajo al punto de descarga, datos que avalan los
resultados de la modelación hidráulica de la pluma de descarga

16

**VI. REFERENCIAS**

 - Robert L. Doneker and Gerhard H. Jirka. 2007. A Hydrodynamic Mixing Zone Model

and Decision Support System for Pollutant Discharges into Surface Waters. Washington,

D.C. CORMIX User Manual.

 - Streeter, HW, y EB Phelps. 1925. Un estudio de la contaminación y purificación natural del

río Ohio. III. Factores interesados en los fenómenos de oxidación y aireación. Servicio de

Salud Pública de los EE.UU., Boletín N o 146.

 - Tchobanoglous, G., y ED Schroeder. 1984: Calidad del agua. Características, modelado,

modificación. Addison-Wesley, Massachussets.

17

**APENDICE I**

**(SALIDAS DEL MODELO CORMIX)**

```
CORMIX SESSION REPORT:

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

CORMIX MIXING ZONE EXPERT SYSTEM

CORMIX Version 10.0GTD

HYDRO1:Version-10.0.0.0 July,2016
SITE NAME/LABEL: ESTERO MONTEAGUILA

DESIGN CASE: PTAS MONTEAGUILA

FILE NAME: C:\Users\Julio1977\Desktop\MODELACIONES\ESSBIO
2017\MONTEAGUILA\PTAS MONTEAGUILA.prd
Using subsystem CORMIX1: Single Port Discharges
Start of session: 11/16/2017--02:24:30

*****************************************************************************

SUMMARY OF INPUT DATA:

----------------------------------------------------------------------------
AMBIENT PARAMETERS:

Cross-section = bounded

Width BS = 3 m

Channel regularity ICHREG = 1
Ambient flowrate QA = 2.34 m^3/s
Average depth HA = 0.25 m
Depth at discharge HD = 0.2 m
Ambient velocity UA = 3.12 m/s
Darcy-Weisbach friction factor F = 0.2521
Calculated from Manning's n = 0.045
Wind velocity UW = 0.51 m/s
Stratification Type STRCND = U
Surface temperature = 10.20 degC
Bottom temperature = 10.20 degC

Calculated FRESH-WATER DENSITY values:
Surface density RHOAS = 999.6840 kg/m^3
Bottom density RHOAB = 999.6840 kg/m^3

----------------------------------------------------------------------------
DISCHARGE PARAMETERS: Single Port Discharge
Nearest bank = right
Distance to bank DISTB = 0.05 m

Port diameter D0 = 0.315 m

Port cross-sectional area A0 = 0.0350 m^2
Discharge velocity U0 = 1.06 m/s
Discharge flowrate Q0 = 0.037 m^3/s
Discharge port height H0 = 0.2 m
Vertical discharge angle THETA = -90 deg
Horizontal discharge angle SIGMA = 0 deg
Discharge temperature (freshwater) = 10.9 degC
Corresponding density RHO0 = 999.6172 kg/m^3
Density difference DRHO = 0.0668 kg/m^3
Buoyant acceleration GP0 = 0.0007 m/s^2
Discharge concentration C0 = 35 mg/l
Surface heat exchange coeff. KS = 0 m/s
Coefficient of decay KD = 0 /s

----------------------------------------------------------------------------
DISCHARGE/ENVIRONMENT LENGTH SCALES:

LQ = 0.19 m Lm = 0.06 m Lb = 0.00 m

LM = 17.88 m Lm' = 99999 m Lb' = 99999 m

----------------------------------------------------------------------------
NON-DIMENSIONAL PARAMETERS:

Port densimetric Froude number FR0 = 90.03

Velocity ratio R = 0.34

----------------------------------------------------------------------------
MIXING ZONE / TOXIC DILUTION ZONE / AREA OF INTEREST PARAMETERS:

Toxic discharge = no
Water quality standard specified = no
Regulatory mixing zone = no
Region of interest = 200 m downstream

*****************************************************************************

HYDRODYNAMIC CLASSIFICATION:

*------------------------*

| FLOW CLASS = IPV3 |

*------------------------*

This flow configuration applies to a layer corresponding to the full water
depth at the discharge site.
Applicable layer depth = water depth = 0.2 m

Limiting Dilution S = (QA/Q0)+ 1.0 = 64.2

*****************************************************************************

MIXING ZONE EVALUATION (hydrodynamic and regulatory summary):

----------------------------------------------------------------------------
X-Y-Z Coordinate system:
Origin is located at the BOTTOM below the port/diffuser center:
0.05 m from the right bank/shore.
Number of display steps NSTEP = 25 per module.

----------------------------------------------------------------------------
NEAR-FIELD REGION (NFR) CONDITIONS :
Note: The NFR is the zone of strong initial mixing. It has no regulatory
implication. However, this information may be useful for the discharge
designer because the mixing in the NFR is usually sensitive to the
discharge design conditions.
Pollutant concentration at NFR edge c = 3.6733 mg/l
Dilution at edge of NFR s = 9.5
NFR Location: x = 1.90 m

```

18

```
(centerline coordinates) y = 0 m
z = 0 m

NFR plume dimensions: half-width (bh) = 0.28 m
thickness (bv) = 0.2 m

Cumulative travel time: 0.4404 sec.

----------------------------------------------------------------------------
Buoyancy assessment:
The effluent density is less than the surrounding ambient water
density at the discharge level.
Therefore, the effluent is POSITIVELY BUOYANT and will tend to rise towards

the surface.

----------------------------------------------------------------------------
FAR-FIELD MIXING SUMMARY:

Plume becomes vertically fully mixed ALREADY IN NEAR-FIELD at 1.90 m
downstream and continues as vertically mixed into the far-field.

----------------------------------------------------------------------------
PLUME BANK CONTACT SUMMARY:

Plume in bounded section contacts one bank only at 1.90 m downstream.

************************ TOXIC DILUTION ZONE SUMMARY ************************

No TDZ was specified for this simulation.

********************** REGULATORY MIXING ZONE SUMMARY ***********************

No RMZ and no ambient water quality standard have been specified.

********************* FINAL DESIGN ADVICE AND COMMENTS **********************

REMINDER: The user must take note that HYDRODYNAMIC MODELING by any known
technique is NOT AN EXACT SCIENCE.
Extensive comparison with field and laboratory data has shown that the
CORMIX predictions on dilutions and concentrations (with associated
plume geometries) are reliable for the majority of cases and are accurate
to within about +-50% (standard deviation).
As a further safeguard, CORMIX will not give predictions whenever it judges
the design configuration as highly complex and uncertain for prediction.

CORMIX1 PREDICTION FILE:

11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

CORMIX MIXING ZONE EXPERT SYSTEM

Subsystem CORMIX1: Single Port Discharges
CORMIX Version 10.0GTD

HYDRO1 Version 10.0.0.0 July 2016

---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
CASE DESCRIPTION

Site name/label: ESTERO MONTEAGUILA
Design case: PTAS MONTEAGUILA
FILE NAME: C:\...ONES\ESSBIO 2017\MONTEAGUILA\PTAS MONTEAGUILA.prd
Time stamp: 11/16/2017--02:24:30

ENVIRONMENT PARAMETERS (metric units)

Bounded section

BS = 3.00 AS = 0.75 QA = 2.34 ICHREG= 1

HA = 0.25 HD = 0.20

UA = 3.120 F = 0.252 USTAR =0.5538E+00

UW = 0.514 UWSTAR=0.5440E-03

Uniform density environment
STRCND= U RHOAM = 999.6840

DISCHARGE PARAMETERS (metric units)
Above Surface Discharge:
Re-computed discharge conditions at entry point at water surface.
BANK = RIGHT DISTB = 0.05

D0 = 0.211 A0 = 0.035 H0 = 0.20 SUB0 = 0.00

THETA = 90.00 SIGMA = 0.00

U0 = 1.058 Q0 = 0.037 =0.3700E-01

RHO0 = 999.6172 DRHO0 =0.6677E-01 GP0 =0.6550E-03
C0 =0.3500E+02 CUNITS= mg/l
IPOLL = 1 KS =0.0000E+00 KD =0.0000E+00

FLUX VARIABLES (metric units)
Q0 =0.3700E-01 M0 =0.3916E-01 J0 =0.2424E-04 SIGNJ0= 1.0
Associated length scales (meters)
LQ = 0.19 LM = 17.88 Lm = 0.06 Lb = 0.00
Lmp = 99999.00 Lbp = 99999.00

NON-DIMENSIONAL PARAMETERS

FR0 = 90.03 R = 0.34

FLOW CLASSIFICATION

111111111111111111111111111111111111111111

1 Flow class (CORMIX1) = IPV3 1
1 Applicable layer depth HS = 0.20 1
1 Limiting Dilution S =QA/Q0= 64.24 1
111111111111111111111111111111111111111111

MIXING ZONE / TOXIC DILUTION / REGION OF INTEREST PARAMETERS
C0 =0.3500E+02 CUNITS= mg/l
NTOX = 0

NSTD = 0

REGMZ = 0

XINT = 200.00 XMAX = 200.00

X-Y-Z COORDINATE SYSTEM:

ORIGIN is located at the bottom and below the center of the port:
0.05 m from the RIGHT bank/shore.
X-axis points downstream, Y-axis points to left, Z-axis points upward.
NSTEP = 25 display intervals per module

---------------------------------------------------------------------------------------------
```

19

```
---------------------------------------------------------------------------------------------
BEGIN MOD101: DISCHARGE MODULE

X Y Z S C B Uc TT

0.00 0.00 0.20 1.0 0.350E+02 0.11 1.058 .00000E+00

END OF MOD101: DISCHARGE MODULE

---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
BEGIN CORJET (MOD110): JET/PLUME NEAR-FIELD MIXING REGION

Zone of flow establishment: THETAE= -39.32 SIGMAE= 0.00

LE = 0.00 XE = 0.00 YE = 0.00 ZE = 0.20

Profile definitions:
B = Gaussian 1/e (37%) half-width, normal to trajectory
S = hydrodynamic centerline dilution
C = centerline concentration (includes reaction effects, if any)
Uc = Local centerline excess velocity (above ambient)
TT = Cumulative travel time

X Y Z S C B Uc TT

0.00 0.00 0.20 1.5 0.238E+02 0.10 -3.591 .32374E-03

0.06 0.00 0.18 1.8 0.192E+02 0.09 -3.209 .10048E-01

0.13 0.00 0.18 2.1 0.167E+02 0.09 -2.701 .21008E-01

0.19 0.00 0.17 2.3 0.151E+02 0.09 -2.382 .32720E-01

0.26 0.00 0.17 2.5 0.138E+02 0.10 -2.153 .45008E-01

0.32 0.00 0.16 2.7 0.128E+02 0.10 -1.978 .57762E-01

0.39 0.00 0.16 2.9 0.120E+02 0.10 -1.839 .70908E-01

0.46 0.00 0.16 3.1 0.113E+02 0.10 -1.723 .84392E-01

0.52 0.00 0.15 3.3 0.107E+02 0.10 -1.629 .97751E-01

0.59 0.00 0.15 3.4 0.102E+02 0.11 -1.545 .11179E+00

0.65 0.00 0.15 3.6 0.973E+01 0.11 -1.471 .12606E+00

0.72 0.00 0.15 3.8 0.933E+01 0.11 -1.406 .14055E+00

0.78 0.00 0.15 3.9 0.897E+01 0.11 -1.349 .15523E+00

0.85 0.00 0.14 4.0 0.864E+01 0.11 -1.297 .17009E+00

0.92 0.00 0.14 4.2 0.835E+01 0.11 -1.250 .18512E+00

0.98 0.00 0.14 4.3 0.808E+01 0.12 -1.209 .19984E+00

1.05 0.00 0.14 4.5 0.783E+01 0.12 -1.170 .21516E+00

1.11 0.00 0.14 4.6 0.760E+01 0.12 -1.134 .23062E+00

1.18 0.00 0.14 4.7 0.739E+01 0.12 -1.101 .24620E+00

1.24 0.00 0.14 4.9 0.719E+01 0.12 -1.070 .26190E+00

1.31 0.00 0.13 5.0 0.701E+01 0.12 -1.041 .27771E+00

1.38 0.00 0.13 5.1 0.683E+01 0.12 -1.014 .29363E+00

1.44 0.00 0.13 5.2 0.668E+01 0.13 -0.990 .30915E+00

1.51 0.00 0.13 5.4 0.652E+01 0.13 -0.967 .32526E+00

1.57 0.00 0.13 5.5 0.638E+01 0.13 -0.944 .34146E+00

1.64 0.00 0.13 5.6 0.624E+01 0.13 -0.924 .35753E+00

Cumulative travel time = 0.3575 sec ( 0.00 hrs)

END OF CORJET (MOD110): JET/PLUME NEAR-FIELD MIXING REGION

---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
BEGIN MOD131: LAYER BOUNDARY/TERMINAL LAYER APPROACH

Control volume inflow:

X Y Z S C B TT

1.64 0.00 0.13 5.6 0.624E+01 0.13 .35753E+00

Profile definitions:

BV = top-hat thickness, measured vertically
BH = top-hat half-width, measured horizontally in Y-direction
ZU = upper plume boundary (Z-coordinate)
ZL = lower plume boundary (Z-coordinate)
S = hydrodynamic average (bulk) dilution
C = average (bulk) concentration (includes reaction effects, if any)
TT = Cumulative travel time

X Y Z S C BV BH ZU ZL TT

1.51 0.00 0.00 5.6 0.624E+01 0.00 0.00 0.00 0.00 .35753E+00

1.55 0.00 0.00 5.6 0.624E+01 0.13 0.09 0.13 0.00 .35753E+00

1.59 0.00 0.00 5.6 0.624E+01 0.15 0.13 0.15 0.00 .35753E+00

1.63 0.00 0.00 5.6 0.624E+01 0.16 0.15 0.16 0.00 .35753E+00

1.66 0.00 0.00 5.8 0.608E+01 0.18 0.18 0.18 0.00 .36582E+00

1.70 0.00 0.00 6.5 0.541E+01 0.18 0.20 0.18 0.00 .37826E+00

1.74 0.00 0.00 7.5 0.469E+01 0.19 0.22 0.19 0.00 .39069E+00

1.78 0.00 0.00 8.4 0.419E+01 0.19 0.24 0.19 0.00 .40313E+00

1.82 0.00 0.00 9.0 0.390E+01 0.20 0.25 0.20 0.00 .41556E+00

1.86 0.00 0.00 9.3 0.376E+01 0.20 0.27 0.20 0.00 .42800E+00

1.90 0.00 0.00 9.5 0.367E+01 0.20 0.28 0.20 0.00 .44043E+00

Cumulative travel time = 0.4404 sec ( 0.00 hrs)

END OF MOD131: LAYER BOUNDARY/TERMINAL LAYER APPROACH

---------------------------------------------------------------------------------------------
** End of NEAR-FIELD REGION (NFR) **

WAKE FLOW CONDITIONS: The discharge velocity (U0) is less than or equal to the
ambient velocity (Ua) and results in wake flow conditions. There is no discharge
momentum induced mixing. The mixing characteristics are UNDESIRABLE.

In this design case, the discharge is located CLOSE TO BANK/SHORE.
Some lateral boundary interaction occurs at end of the near-field.
This may be related to a design case with a very LOW AMBIENT VELOCITY.
The dilution values in one or more of the preceding zones may be too high.
Carefully evaluate results in near-field and check degree of interaction.

```

20

```
Consider locating outfall further away from bank or shore.
In the next prediction module, the plume centerline will be set
to follow the bank/shore.

---------------------------------------------------------------------------------------------
BEGIN MOD141: BUOYANT AMBIENT SPREADING

Plume is ATTACHED to RIGHT bank/shore.
Plume width is now determined from RIGHT bank/shore.

Discharge is non-buoyant or weakly buoyant.
Therefore BUOYANT SPREADING REGIME is ABSENT.

END OF MOD141: BUOYANT AMBIENT SPREADING

---------------------------------------------------------------------------------------------
Due to the attachment or proximity of the plume to the bottom, the bottom
coordinate for the FAR-FIELD differs from the ambient depth, ZFB = 0 m.
In a subsequent analysis set "depth at discharge" equal to "ambient depth".

---------------------------------------------------------------------------------------------
BEGIN MOD161: PASSIVE AMBIENT MIXING IN UNIFORM AMBIENT

Vertical diffusivity (initial value) = 0.222E-01 m^2/s
Horizontal diffusivity (initial value) = 0.277E-01 m^2/s

The passive diffusion plume is VERTICALLY FULLY MIXED at beginning of region.

Profile definitions:
BV = Gaussian s.d.*sqrt(pi/2) (46%) thickness, measured vertically
= or equal to layer depth, if fully mixed
BH = Gaussian s.d.*sqrt(pi/2) (46%) half-width,
measured horizontally in Y-direction
ZU = upper plume boundary (Z-coordinate)
ZL = lower plume boundary (Z-coordinate)
S = hydrodynamic centerline dilution
C = centerline concentration (includes reaction effects, if any)
TT = Cumulative travel time

Plume Stage 2 (bank attached):

X Y Z S C BV BH ZU ZL TT

1.90 -0.05 0.00 9.5 0.367E+01 0.25 0.45 0.25 0.00 .44043E+00

9.82 -0.05 0.00 13.7 0.256E+01 0.20 0.65 0.20 0.00 .29407E+01

17.74 -0.05 0.00 16.9 0.208E+01 0.20 0.80 0.20 0.00 .54409E+01

25.67 -0.05 0.00 19.5 0.179E+01 0.20 0.93 0.20 0.00 .79412E+01

33.59 -0.05 0.00 21.9 0.160E+01 0.20 1.04 0.20 0.00 .10441E+02

41.52 -0.05 0.00 24.0 0.146E+01 0.20 1.14 0.20 0.00 .12942E+02

49.44 -0.05 0.00 25.9 0.135E+01 0.20 1.23 0.20 0.00 .15442E+02

57.37 -0.05 0.00 27.7 0.126E+01 0.20 1.31 0.20 0.00 .17942E+02

65.29 -0.05 0.00 29.4 0.119E+01 0.20 1.39 0.20 0.00 .20442E+02

73.21 -0.05 0.00 31.0 0.113E+01 0.20 1.47 0.20 0.00 .22943E+02

81.14 -0.05 0.00 32.5 0.108E+01 0.20 1.54 0.20 0.00 .25443E+02

89.06 -0.05 0.00 34.0 0.103E+01 0.20 1.61 0.20 0.00 .27943E+02

96.99 -0.05 0.00 35.4 0.990E+00 0.20 1.68 0.20 0.00 .30443E+02

104.91 -0.05 0.00 36.7 0.953E+00 0.20 1.74 0.20 0.00 .32944E+02

112.83 -0.05 0.00 38.0 0.921E+00 0.20 1.80 0.20 0.00 .35444E+02

120.76 -0.05 0.00 39.3 0.892E+00 0.20 1.86 0.20 0.00 .37944E+02

128.68 -0.05 0.00 40.5 0.865E+00 0.20 1.92 0.20 0.00 .40444E+02

136.61 -0.05 0.00 41.6 0.840E+00 0.20 1.98 0.20 0.00 .42945E+02

144.53 -0.05 0.00 42.8 0.818E+00 0.20 2.03 0.20 0.00 .45445E+02

152.46 -0.05 0.00 43.9 0.797E+00 0.20 2.08 0.20 0.00 .47945E+02

160.38 -0.05 0.00 45.0 0.778E+00 0.20 2.13 0.20 0.00 .50445E+02

168.30 -0.05 0.00 46.1 0.760E+00 0.20 2.18 0.20 0.00 .52946E+02

176.23 -0.05 0.00 47.1 0.743E+00 0.20 2.23 0.20 0.00 .55446E+02

184.15 -0.05 0.00 48.1 0.728E+00 0.20 2.28 0.20 0.00 .57946E+02

192.08 -0.05 0.00 49.1 0.713E+00 0.20 2.33 0.20 0.00 .60447E+02

200.00 -0.05 0.00 50.1 0.699E+00 0.20 2.38 0.20 0.00 .62947E+02

Cumulative travel time = 62.9468 sec ( 0.02 hrs)

Simulation limit based on maximum specified distance = 200.00 m.
This is the REGION OF INTEREST limitation.

END OF MOD161: PASSIVE AMBIENT MIXING IN UNIFORM AMBIENT

---------------------------------------------------------------------------------------------
---------------------------------------------------------------------------------------------
CORMIX1: Single Port Discharges End of Prediction File

11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111

```

21