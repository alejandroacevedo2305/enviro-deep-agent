---
title: Sin título
author: Rubén Figueroa
date: D:20211105111622-03'00'
language: es
type: report
pages: 38
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - I. MODELACIÓN TÉRMICA
  - II. ANTECEDENTES DE ESTUDIO
  - III. RESULTADOS
-->

**ESTUDIO EFICIENCIA ENERGETICA - PDA TALCA, Lote 6**

**Informe Diagnóstico**

**El Maule**

**05-11-2021**

V3 05-11-2021

Estimado

Nicolás Klein

Rentas RA Cuatro Ltda.

Ref.: 20118_3 Informe PDA

Presentamos informe diagnóstico referente a estudio Eficiencia Energética como base para diseño de sistema

de clima para edificio El Maule de inmobiliaria San Miguel, en función de los requerimientos del Plan de

Descontaminación Atmosférica de Talca.

Tomás Milnes E.

Gerente General

**CALDER S.A.**

ÍNDICE

**I. MODELACIÓN TÉRMICA** **1**

I.1 Balance térmico 1

I.2 Ganancia de calor por radiación solar 3

I.3 Condensación superficial e intersticial 4

Condensación superficial 4

Condensación intersticial 5

I.5 Hermeticidad e infiltración no controlada de aire 7

I.6 Ventilación 8

**II. ANTECEDENTES DE ESTUDIO** **9**

II.1 Infraestructura 9

II.2 Envolvente térmica: U 10

A. Muro 10

B. Piso ventilado 11

C. Techumbre 12

II.3 Escenario climatológico 13

**III. RESULTADOS** **14**

III.1 Modelación térmica 14

A. Nivel 1 14

B. Nivel 2 15

C. Nivel 3 15

D. Nivel 4 al 14 16

E. Nivel 15 16

F. Nivel 16 17

III.2 Ganancia de calor por radiación solar 19

III.3 Condensación 20

Condensación superficial 20

Condensación intersticial 22

III.4 Producción de agua caliente sanitaria 28

III.5 Ventilación y Hermeticidad del aire 29

**ANEXOS**

Anexo 1: Planilla de Cálculos

Anexo 2: Fichas técnicas

NOMENCLATURA

A: Área de intercambio de calor, m [2] .

A z : área de la zona: área neta ocupable de la zona de ventilación, m [2] .

c: Calor específico,

J
kg K [. ]

e i : Espesor del elemento i, m .

f R si,min : Factor de temperatura mínima de diseño en la superficie interior.

h int : Coeficiente de convección interior,

W

m [2] K ~~[.]~~

W

h ext : Coeficiente de convección exterior,

m [2] K ~~[.]~~

k i : Conductividad térmica del elemento i,

̅̅̅:p e Presión exterior media, Pa .

W

mK ~~[.]~~

p sat : Presión de saturación del vapor de agua, Pa .

p sat,min : Presión de saturación mínima aceptable del vapor de agua, Pa .

p si : Presión en la superficie interior, Pa .

P Z : Población de zona: número de personas en la zona de ventilación de uso típico.

q: Flujo de calor, W .

Q: Energía calórica requerida, J, kcal, kWh, etc .

R: Renovaciones de aire en una hora,

1

h ~~[.]~~

R i : Resistencia térmica del elemento i,

R j : Resistencia térmica de la interfaz j,

m [2] K

W ~~[.]~~

m [2] K

W ~~[.]~~

R [′] n : Resistencia térmica acumulada hasta la interfaz n,

m [2] K

W ~~[.]~~

R se : Resistencia térmica de la superficie exterior,

m [2] K

W ~~[.]~~

R si : Resistencia térmica de la superficie interior,

m [2] K

W ~~[.]~~

R si,min : Resistencia térmica total mínima de la superficie interior,

m [2] K

W ~~[.]~~

m [2] K

W ~~[.]~~

R ′T : Resistencia térmica total acumulada,

′

T : Resistencia térmica total acumulada,

R P : Tasa de flujo de aire exterior requerida por persona de acuerdo con lo establecido por la norma

NCh3308,

L

[por persona. ]
s

R a : Tasa de flujo de aire exterior requerido por unidad de área de acuerdo con lo establecido por la

norma NCh3308,

L
s [por ] [m] [2] [. ]

s d,j : Espesor de aire equivalente para la difusión de vapor para la interfaz j, m .

′

S d,n : Espesor de aire equivalente para la difusión de vapor hasta la interfaz n, m .

′

S d,T : Espesor de aire equivalente para la difusión de vapor total acumulada, m .

T C : Temperatura de consumo de agua caliente, °C .

T R : Temperatura del agua de la red, °C .

U: Transmitancia térmica,

W

m [2] K ~~[.]~~

U vol : Relación de la densidad del aire y el calor especifico en función del tiempo,

W

m [3] K [. ]

V bz : Flujo de aire exterior por persona,

V: Volumen de agua consumida, m [3] .

L

s ~~[.]~~

V vol : Volumen de intercambio de calor, m [3] .

ΔT: Diferencia de temperatura, °C .

ΔT ACS : Diferencia de temperatura para agua caliente sanitaria, °C .

μ: Factor de resistencia al vapor de agua.

̅̅̅̅:φ e Humedad relativa media exterior.

φ max : Humedad relativa máxima aceptable.

φ si : Humedad relativa de la superficie interior.

ρ: Densidad,

kg

m [3] ~~[.]~~

̅̅̅:θ e Temperatura exterior media, °C .

θ e : Temperatura exterior, °C .

θ i : Temperatura interior, °C .

θ min : Temperatura mínima aceptable en la superficie interior, °C .

θ n : Temperatura en la interfaz n, °C

1

# I. MODELACIÓN TÉRMICA

El edificio El Maule Lote 6 ha sido modelado bajo las especificaciones técnicas expuestas por el

mandante. A continuación, se muestran los resultados para la envolvente, análisis de condensación

intersticial y superficial, además de un estudio de ventilación y calefacción.

I.1 Balance térmico

Las “pérdidas térmicas” corresponden a los flujos de calor, medidos en kcal/h, kW, etc. (unidades

de potencia); debidos a la diferencia de temperatura entre interior y exterior. En temporada

invierno, se considera que la temperatura interior es superior a la exterior, por lo que los flujos de

calor son desde el interior de la vivienda hacia el exterior. Por otro lado, en temporada verano, los

flujos de calor son en dirección opuesta, debido a que la temperatura exterior se considera superior

a la interior.

Temporada Invierno: T i ≥T e →Pérdidas térmicas

Temporada Verano: T i ≤T e →Ganancias térmicas

De acuerdo con la física de la transferencia de calor, el flujo de calor que experimenta un volumen

de control con su entorno corresponde a:

q = U ∙A ∙∆T

Donde:

U : Transmitancia térmica del volumen de control, medida en W/(m [2] K) o W/(m [2] °C) .

A : Área de intercambio de calor, medida en m [2] .

∆T : Diferencia de temperatura entre interior y exterior (o al revés en caso de verano), medido en °C

o K.

Considerando invierno, las pérdidas de calor pueden ocurrir a través de muros ( q M ), ventanas ( q V ),
techumbre ( q T ), piso ( q P ) y volumétrica ( q vol ). Es decir, en este caso las pérdidas de calor totales se

calculan como:

q = q M + q V + q T + q P + q vol

q = U M A M ∆T + U V A V ∆T + U T A T ∆T + U P A P ∆T + U Vol V Vol ∆T

2

Donde:

V: Volumen de intercambio de calor, medida en m [3]

U vol : Corresponde a la relación de la densidad del aire y el calor especifico en función del tiempo,
medida en W/(m [3] K) .

U Vol = ρ aire c aire R

ρ aire : Densidad del aire, kg/m [3] .

c aire : Calor específico del aire, J/(kgK) o J/(kg°C) .

R: Renovaciones de aire en el recinto, 1/h .

En cuanto a la transmitancia térmica superficial, conocida también como coeficiente global de

transferencia de calor, su valor depende específicamente de los materiales, sus espesores y su

relación con el ambiente. Físicamente, el térmico U representa el inverso de la resistencia térmica

total que se tiene en cada zona. Esto es:

Transmitancia Muro: U M = [1]

R M

R M = [1]

h int

;

+ [e] [1]

k 1

+ [e] [2]

k 2

+ ⋯+ [e] [i]

k i

+ [1]

h ext

+ [1]

i = componentes de muro & h int, h ext coef. convección.

Transmitancia Ventana: U V = [1]

R V

R V = h [1] int

;

+ [e] [1]

k 1

+ [e] [2]

k 2

+ ⋯+ [e] [i]

k i

+ [1]

h ext

+ [1]

i = componentes de ventana & h int, h ext coef. convección.

Transmitancia Techumbre: U T = [1]

R T

R T = [1]

h int

;

+ [e] [1]

k 1

+ [e] [2]

k 2

+ ⋯+ [e] [i]

k i

+ [1]

h ext

+ [1]

i = componentes de techumbre & h int, h ext coef. convección.

3

Transmitancia Piso ventilado: U P = [1]

R P

R P = [1]

h int

+ [e] [1]

k 1

+ [e] [2]

k 2

+ ⋯+ [e] [i]

k i

+ [1]

h ext

;

i = componentes de piso ventilado & h int, h ext coef. convección.

Como se menciona en la sección de antecedentes, cada una de las resistencias térmicas (y por ende
sus transmisividades) dependerán del tipo de envolvente que especifica el mandante.

I.2 Ganancia de calor por radiación solar

Los proyectos de vivienda nueva deberán cumplir exigencias respecto del control de las ganancias

solares a través de vanos traslúcidos o transparentes y exigencias de aislación térmica de

sobrecimiento, para pisos en contacto con el terreno natural, las que serán establecidas por MINVU

mediante acto administrativo.

|Porcentaje máximo de superficie de ventanas según orientación y valor U|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|**Zona PDA**|Orientación U|% V/S Transmitancia térmica U|% V/S Transmitancia térmica U|% V/S Transmitancia térmica U|% V/S Transmitancia térmica U|% V/S Transmitancia térmica U|% V/S Transmitancia térmica U|% V/S Transmitancia térmica U|% V/S Transmitancia térmica U|% V/S Transmitancia térmica U|% V/S Transmitancia térmica U|
|**Zona PDA**|Orientación U|≤1,2|≤1,6|≤2|≤2,4|≤2,8|≤3,2|≤3,6|≤4|≤4,4|≤5,8|
|**Talca - Maule**|Norte|91%|89%|87%|85%|83%|80%|77%|73%|69%|25%|
|**Talca - Maule**|O-P|70%|68%|65%|63%|60%|57%|53%|49%|44%|10%|
|**Talca - Maule**|Sur|59%|57%|54%|51%|48%|44%|40%|35%|29%|15%|
|**Talca - Maule**|Ponderado|41%|40%|38%|37%|35%|33%|31%|28%|25%|10%|

Tabla 1: Porcentaje máximo de superficie de ventana según orientación y valor de transmitancia

térmica U. Fuente: Ministerio de Vivienda y Urbanismo

Por lo tanto, la metodología a desarrollar será basada en determinar el área de las ventanas en cada

orientación y el área del muro correspondiente y realizar la relación de proporción a partir de una
transmitancia térmica de ventanas considerada U = 3,0 W/(m [2] K) .

Cabe mencionar que la transmitancia térmica no tiene relación directa con la radiación solar que

ingresa a través de una ventana, dado que este factor depende de la transmisividad a la radiación

térmica del material. En cambio, la transmitancia térmica corresponde al inverso de la resistencia a

la convección y conducción de calor del material y no a la radiación, es decir, sin importar que tan

4

resistente sea el material, si este material es altamente transmisivo a la radiación térmica ingresará

de igual manera afectando la climatización, principalmente en la temporada de verano.

I.3 Condensación superficial e intersticial

Condensación superficial

La condensación superficial es un fenómeno en el cual el vapor de agua presente en el aire al interior

de un recinto se convierte en líquido en los muros. Esto ocurre cuando la temperatura interior del

elemento constructivo disminuye hasta alcanzar la temperatura de saturación del aire que se

encuentra en el interior.

La metodología utilizada se basa en la norma NCh1973/2014:

1. Se define la temperatura exterior como la media de la temperatura mínima anual sobre una

base de al menos 30 años de información climática y también se determina la humedad

relativa media exterior, por lo tanto, es posible obtener la presión media exterior.

p̅̅̅ = φ e ̅̅̅̅p e sat (θ̅̅̅) e

2. Se define la temperatura interior del recinto y se establece un valor para la generación de

vapor de la vivienda, de acuerdo con la clase de higrometría que se le asigne, para el caso a

analizar, se requiere de una humedad relativa de 65%, 75% y 85%.

3. Con la humedad relativa máxima aceptable en la superficie del elemento ( φ max = 1 ) se

calcula la presión mínima de saturación aceptable de acuerdo con la presión de vapor

saturado.

p sat,min = [φ] [si] [p] [si]

φ max

4. A partir de la presión mínima de saturación aceptable, se determina la temperatura de

superficie mínima aceptable.

θ min =

[237,3 ln ] ~~[(]~~ [p] 610 [sat][,][min],5 [)]

17,269 −ln
~~(~~ ~~[p]~~ 610,5 [sat][,][min] [) ]

265,5 ln
~~(~~ [p] 610 [sat][,][min],5 [)]

{21,875 −ln ~~(~~ ~~[p]~~ 610,5 [sat][,][min] [)]

, para p sat,min ≥610,5 Pa

, para p sat,min < 610,5 Pa

5. Se obtiene el factor de temperatura de diseño en la superficie interior (término

adimensional).

5

f R si min = [θ] [min] θ i −θ [ −θ] e [e]

6. Se determina la resistencia térmica, definiendo si el flujo es horizontal, hacia arriba o hacia

abajo.

|Dirección del flujo de calor|Resistencia térmica R m2K/W<br>si|
|---|---|
|Hacia arriba|0,10|
|Horizontal|0,13|
|Hacia abajo|0,17|

Tabla 2: Resistencias térmicas interiores para la evaluación de condensación intersticial, o la

condensación superficial sobre ventanas y puertas. Fuente: NCh1973/2014.

7. Se calcula la resistencia térmica total mínima de la superficie interior, a partir de la

resistencia térmica definida anteriormente y el factor de temperatura de diseño en la

superficie interior.

R si
R si,min = 1 −f R si min

8. Se realiza la comparación entre la resistencia térmica mínima de la superficie interior y la

resistencia térmica del compuesto del muro a analizar. Si R si,min es menor a la resistencia
térmica del compuesto del muro R T no habrá condensación, en caso contrario, si habrá.

Condensación intersticial

La condensación intersticial es un fenómeno en el cual el vapor de agua presente en el aire se

convierte en líquido en el interior de una solución constructiva, cuando la presión del vapor que

atraviesa dicha solución constructiva es mayor o igual a la presión de saturación de vapor del agua

en algún punto en el interior. Esta presión de saturación depende del perfil de temperaturas al

interior de dicha solución constructiva.

Es recomendable que para elementos cuya resistencia térmica sea mayor a 0,25 m [2] K/W, se
subdividan en capas imaginarias cuya resistencia térmica sea menor o igual a 0,25 m [2] K/W. Estas

subdivisiones se consideran en todos los cálculos como capas independientes de distintos

materiales con interfases entre ellas.

Para elementos cuyo factor de resistencia al vapor de agua se considera como infinito, es decir, que

previenen el paso del vapor de agua, tales como hojas metálicas, se les debe considerar un factor

6

de resistencia al vapor de agua de μ = 100.000, dado que el procedimiento requiere de un valor de
μ finito.

La metodología utilizada se basa en la norma NCh1973/2014, en donde las curvas de saturación de

vapor de agua se construyen en base a los valores acumulados de la resistencia térmica y el espesor

de aire equivalente para la difusión del vapor partiendo del exterior hacia cada interfaz n .

R [′] n = R se j
+ ∑R

j=1

S ′
d,n d,j

= ∑S

j=1

La resistencia térmica total y el espesor de la capa de aire equivalente a la difusión de vapor de agua

están dados por:

R ′T = R se j

+ ∑R

j=1

+ R si

S ′
d,T d,j

= ∑S

j=1

A partir de estos de resultados, se determinan los valores de las temperaturas en cada interfaz entre

cada una de las capas definidas para el elemento constructivo y éstas se pueden obtener de la

siguiente expresión:

θ n = θ e + [R] ′ [n′]

′ [(θ] [i] [−θ] [e] [)]

R T

θ n = θ e + R [′] n ∙q

Donde R ′T corresponde a la resistencia térmica total del elemento constructivo y θ corresponde a la

temperatura en cierto punto ( q es el flujo de calor total por muro, techumbre o piso, dependiendo
el caso). La distribución de temperatura en cada capa es lineal dado el supuesto de condiciones de

estado estacionario.

Luego, se determina la presión de saturación en cada capa del elemento constructivo a partir de la

temperatura en cada capa obtenida con la expresión anterior. Finalmente, si la presión de vapor

superar en alguna interfase a la presión de saturación, se debe considerar que en ese punto ocurre

condensación intersticial.

Todas las propiedades de los materiales de conductividad térmica, resistencia al vapor de agua,

entre otros, fueron obtenidos de la ISO 10456. Cabe mencionar, que para el cálculo de condensación

intersticial se optó por el factor de resistencia al vapor ( μ ) en seco, dado que este escenario permite

obtener un estudio más conservador.

7

I.4 Sistema de agua caliente sanitaria

En conjunto con los requerimientos de calefacción, se solicita el estudio por consumo energético de

agua caliente sanitaria (ACS). Al respecto, se asumirá que cada persona consume agua caliente a

una temperatura de T C = 40°C . Por otro lado, se asume que el agua viene de red a una temperatura
de T R = 14°C . En cambio, para el caso del sistema de producción con acumulación, la temperatura
de generación asciende a 60°C, todo esto de acuerdo con la ley 20.365. Luego:

∆T ACS = T C −T R

La energía requerida al día (Q) en una casa para la producción de ACS es

Q = ρVc∆T ACS →J, kcal, kWh, etc.

ρ : Densidad del agua, medida en kg/m [3]

V: Volumen total consumido al día, medido en m [3]

c : Calor específico del agua, en J/(kgK) o J/(kg°C)

El volumen consumido en el día de ACS se define en función de la cantidad de equipos instalados y

viviendas, todo esto de acuerdo con lo recomendado por el “Manual instalador Junkers”. A su vez,

se realiza un cálculo de simultaneidad incorporando 4 métodos: Método racional, NCh2485, UNE

149.201 y Junkers. Los resultados se obtienen escogiendo el método más conservador. Además, la

simultaneidad del caudal instalado depende de dos factores: simultaneidad dentro de la misma
vivienda y entre viviendas/departamentos.

I.5 Hermeticidad e infiltración no controlada de aire

La hermeticidad al aire de una edificación se define como su capacidad para oponerse a las

infiltraciones de aire. Este se mide en cantidad de renovaciones de aire del volumen de la vivienda

por hora (ach) y se evalúa de manera experimental a un diferencial de presión de 50 Pa.

Una infiltración no controlada de aire es el intercambio de aire a través de grietas ocultas,

encuentros entre materiales y aberturas de la envolvente. Este fenómeno genera cargas térmicas,

de frío o de calor según la temporada, que inciden en el desempeño energético de los edificios.

El plan de descontaminación atmosférica establece las especificaciones técnicas mínimas para

poder cumplir con los estándares de infiltración y hermeticidad del aire.

Todas estas fichas se encuentran adjunta al documento.

8

I.6 Ventilación

El objetivo de un sistema de ventilación es renovar contaminantes que se generan en un cierto

ambiente y proporcionar condiciones de agrado. De acuerdo con las normas NCh3308 y NCh3309,

además de la ASHRAE STANDARD 62-73, se estable la ventilación mínima que debe tener un recinto

por persona, basado en la siguiente formula:

V bz = R P ∙P Z + R a ∙A z

Donde:

V bz = Caudal de aire exterior, medido en L/s.

R P = Tasa de flujo de aire exterior requerida por persona de acuerdo con lo establecido por la norma
NCh3308, medida en L/s por persona.

P Z = Población de zona: número de personas en la zona de ventilación de uso típico.

R a = Tasa de flujo de aire exterior requerido por unidad de área de acuerdo con lo establecido por
la norma NCh3308, medida en L/s por unidad de área.

A z = área de la zona: área neta ocupable de la zona de ventilación, expresado en m [2] .

A su vez, el plan de descontaminación atmosférica (PDA) en el decreto 49, establece que se debe

contar con un **sistema mecánico** de salida del aire al exterior, **pudiendo ser las entradas de aire**

**natural o mecánica**, con al menos dos puntos de extracción de aire ubicados en baño y cocina con

encendido mediante control de higrostato.

9

# II. ANTECEDENTES DE ESTUDIO

II.1 Infraestructura

El edificio cuenta con 17 niveles con hasta 8 departamentos de distinto tipo en cada uno entre los

niveles 1 al 16, y 5 tipos para el nivel 17.

Los medios de transferencia de calor estudiados varían entre cada nivel, dependiendo los ambientes

con los que colinda cada departamento. Los sistemas considerados comprenden:

 Pisos ventilados: Corresponden a losas en contacto con ambientes no calefaccionados.

Considerado para todo el piso del primer nivel, y departamentos tipo 3 del tercer nivel.

 Cielo: Corresponde a la totalidad de la cubierta del nivel 16 y de los departamentos del nivel

15 ubicados debajo de la terraza del nivel superior.

 Ventanas: Se ha diferenciado según orientación, para el cálculo de la ganancia solar.

 Muros exteriores: Comprende transferencia de calor mediante conducción y convección por

toda el área de fachada al ambiente exterior.

 Muros interiores: Se consideran pérdidas de calor mediante muros que separan a ambientes

interiores no calefaccionados, estos son pasillos, escaleras de emergencia, y ascensor.

 Ventilación: Corresponden a las pérdidas por caudales de ventilación. Se consideran

caudales recomendados dependiendo el uso del recinto.

Las especificaciones del sistema constructivo se resumen en la siguiente tabla.

|Sistema|Especificaciones.|
|---|---|
|**Muros**|Hormigón armado 200 mm.|
|**Piso**|Hormigón armado 120 mm.|
|**Techo**|Hormigón armado 150 mm.|

Tabla 3. Especificaciones técnicas de obra gruesa.

10

II.2 Envolvente térmica: U

La envolvente térmica corresponde a los distintos valores de U en conjunto: muros, ventanas,

techumbre y piso. Para obtener estos valores, se deben considerar los espesores y materiales

presentados a continuación.

|Sistema|Envolvente térmica|
|---|---|
|**Muros**|EIFS 40 mm y placa yeso cartón 10 mm.|
|**Piso**|EIFS 60 mm.|
|**Techo 1**|Poliestireno expandido de densidad 30 kg/m3 y espesor 150 mm, placa yeso cartón 10 mm.|
|**Techo 2**|Poliestireno expandido de densidad 30 kg/m3 y espesor 150 mm, placa yeso cartón 10 mm.|

Tabla 4. Distintos envolventes térmicas según sistema.

A continuación, mediante el cálculo realizado de acuerdo con lo señalado en las normas NCh853 y

NCh3117, se demostrará el cumplimiento de la transmitancia o resistencia térmica total de la

solución del complejo. Las propiedades de los materiales a utilizar fueron obtenidas de la ISO 10456

y de la norma NCh853.

A. Muro

El PDA establece que la transmitancia térmica de los muros debe ser como máximo 0,80 W/(m [2] K) o
tener una resistencia térmica de 1,25 m [2] K/W. De acuerdo, a los materiales seleccionados se obtiene

los siguientes resultados.

11

|Material|Espesor (mm)|k ( W/(mK) )|Resistencia m2K/W|
|---|---|---|---|
|**Hormigón armado**|200|1,630|0,12|
|**EIFS den=15 kg/m3 **|40|0,041|0,97|
|**Yeso cartón den=700**|10|0,260|0,04|
|Total resistencias conductivas, m2K/W|Total resistencias conductivas, m2K/W|Total resistencias conductivas, m2K/W|1,13|
|Total resistencias de convección interior y exterior, m2K/W|Total resistencias de convección interior y exterior, m2K/W|Total resistencias de convección interior y exterior, m2K/W|0,17|
|Resistencia térmica total m2K/W|Resistencia térmica total m2K/W|Resistencia térmica total m2K/W|1,30|
|**Transmitancia térmica “U” W/(m2K)**|**Transmitancia térmica “U” W/(m2K)**|**Transmitancia térmica “U” W/(m2K)**|**0,77**|
|**Cumplimiento**|**Cumplimiento**|**Cumplimiento**|**SI**|

Tabla 5. Cálculo térmico muros. Fuente: Elaboración propia.

B. Piso ventilado

El PDA establece que la transmitancia térmica de los muros debe ser como máximo 0,60 W/(m [2] K) o
tener una resistencia térmica de 1,50 m [2] K/W. De acuerdo, a los materiales seleccionados se obtiene

los siguientes resultados.

|Material|Espesor (mm)|k ( W/(mK) )|Resistencia m2K/W|
|---|---|---|---|
|**Hormigón armado**|120|1,630|0,12|
|**ESP den=15**|60|0,041|0,97|
|Total resistencias conductivas, m2K/W|Total resistencias conductivas, m2K/W|Total resistencias conductivas, m2K/W|1,53|
|Total resistencias de convección interior y exterior, m2K/W|Total resistencias de convección interior y exterior, m2K/W|Total resistencias de convección interior y exterior, m2K/W|0,22|
|Resistencia térmica total m2K/W|Resistencia térmica total m2K/W|Resistencia térmica total m2K/W|1,75|
|**Transmitancia térmica “U” W/(m2K)**|**Transmitancia térmica “U” W/(m2K)**|**Transmitancia térmica “U” W/(m2K)**|**0,57**|
|**Cumplimiento**|**Cumplimiento**|**Cumplimiento**|**SI**|

Tabla 6. Cálculo térmico piso ventilado. Fuente: Elaboración propia.

12

C. Techumbre

El PDA establece que la transmitancia térmica de los muros debe como máximo 0,38 W/(m [2] K) o
tener una resistencia térmica de 2,63 m [2] K/W. De acuerdo, a los materiales seleccionados se obtiene

los siguientes resultados.

|Techumbre 1 piso 16|Col2|Col3|Col4|
|---|---|---|---|
|**Material**|**Espesor (mm)**|**k ( W/(mK) )**|**Resistencia m2K/W**|
|**Hormigón armado**|150|1,630|0,12|
|**Poliestireno expandido,**<br>**ρ=30 kg/m3 **|150|0,041|3,65|
|**Yeso cartón, ρ=30 kg/m3 **|10|0,260|0,04|
|Total resistencias conductivas, m2K/W|Total resistencias conductivas, m2K/W|Total resistencias conductivas, m2K/W|3,81|
|Total resistencias de convección interior y exterior, m2K/W|Total resistencias de convección interior y exterior, m2K/W|Total resistencias de convección interior y exterior, m2K/W|0,14|
|Resistencia térmica total m2K/W|Resistencia térmica total m2K/W|Resistencia térmica total m2K/W|3,95|
|**Transmitancia térmica “U” W/(m2K)**|**Transmitancia térmica “U” W/(m2K)**|**Transmitancia térmica “U” W/(m2K)**|**0,25**|
|**Cumplimiento**|**Cumplimiento**|**Cumplimiento**|**SI**|

Tabla 7. Cálculo térmico techumbre 1 piso 16. Fuente: Elaboración propia.

|Techumbre 2 piso 15|Col2|Col3|Col4|
|---|---|---|---|
|**Material**|**Espesor (mm)**|**k ( W/(mK) )**|**Resistencia m2K/W**|
|**Hormigón armado**|150|1,630|0,12|
|**Poliestireno expandido,**<br>**ρ=30 kg/m3 **|150|0,041|3,65|
|**Yeso cartón, ρ=30 kg/m3 **|10|0,260|0,04|
|Total resistencias conductivas, m2K/W|Total resistencias conductivas, m2K/W|Total resistencias conductivas, m2K/W|3,81|
|Total resistencias de convección interior y exterior, m2K/W|Total resistencias de convección interior y exterior, m2K/W|Total resistencias de convección interior y exterior, m2K/W|0,14|
|Resistencia térmica total m2K/W|Resistencia térmica total m2K/W|Resistencia térmica total m2K/W|3,95|
|**Transmitancia térmica “U” W/(m2K)**|**Transmitancia térmica “U” W/(m2K)**|**Transmitancia térmica “U” W/(m2K)**|**0,25**|
|**Cumplimiento**|**Cumplimiento**|**Cumplimiento**|**SI**|

Tabla 8. Cálculo térmico techumbre 2 piso 15. Fuente: Elaboración propia.

13

II.3 Escenario climatológico

Se han utilizado el escenario del mes de julio, considerando la temperatura mínima promedio a las

observadas en el registro histórico de la ubicación.

A continuación, presenta las condiciones de diseño, de temperatura interior, exterior y de pasillo y

la humedad relativa exterior:

|Col1|T / °C<br>i|T / °C<br>e|T /°C<br>p|HR|
|---|---|---|---|---|
|**Mes de julio**|19,0|2,6|14|98%|

Tabla 9. Escenarios de diseño.

14

# III. RESULTADOS

Los resultados de las modelaciones térmicas serán expuestos por el total del edificio para el cual se

presenta su comportamiento térmico respecto a la envolvente térmica, la condensación intersticial

y superficial, la ganancia solar, la producción de agua caliente sanitaria y la ventilación.

III.1 Modelación térmica

El estudio térmico fue realizado para cada uno de los departamentos de cada piso. Para la

presentación de los resultados se presentará 6 niveles distintos térmicamente: 1, 2, 3, 4-14, 15 y 16.

Además en todos estos casos se presentarán distintos tipos de departamentos, los más

representativos.

Para una correcta lectura de los gráficos, los departamentos tipo 1 son aquellos en que la

numeración de este termina en 1, los tipos 2 corresponden a los terminados en 2 y así

sucesivamente.

A. Nivel 1

Este nivel presenta pérdidas térmicas principalmente por las plantas hacia el subterráneo, ventanas,

los muros de su contorno y volumétricas.

Figura 1: Pérdidas térmicas (kcal/h) nivel 1. Fuente: Elaboración propia.

15

B. Nivel 2

Este nivel presenta pérdidas térmicas principalmente por ventanas y volumétricas.

Figura 2: Pérdidas térmicas (kcal/h) nivel 2. Fuente: Elaboración propia.

C. Nivel 3

Este nivel presenta pérdidas térmicas principalmente por ventanas, planta hacia el nivel 2 y

volumétricas.

16

Figura 3: Pérdidas térmicas (kcal/h) nivel 3. Fuente: Elaboración propia.

D. Nivel 4 al 14

Este nivel presenta pérdidas térmicas principalmente por muros de contorno, ventanas y

volumétrica.

Figura 4: Pérdidas térmicas (kcal/h) nivel 4 al 14. Fuente: Elaboración propia.

E. Nivel 15

Este nivel presenta pérdidas térmicas principalmente por muros de contorno, ventanas, cielo

expuesto al ambiente en algunos casos debido a la menor área del nivel 16 y volumétrica.

17

Figura 5: Pérdidas térmicas (kcal/h) nivel 15. Fuente: Elaboración propia.

F. Nivel 16

Este nivel presenta pérdidas térmicas principalmente por muros de contorno, ventanas, cielo

expuesto al ambiente y volumétrica.

Figura 6: Pérdidas térmicas (kcal/h) nivel 16. Fuente: Elaboración propia.

18

Finalmente, las perdidas térmicas del edifico completo por niveles se presenta principalmente en

ventanas, muros externos y volumétricas.

Figura 7: Pérdidas térmicas de todos los niveles. Fuente: Elaboración propia.

A modo de conclusión de la modelación térmica, se ha verificado el rendimiento de los radiadores,

de acuerdo con las pérdidas térmicas por tipo de departamento y la potencia y cantidad de equipos

dispuestos. Si bien es cierto que se están considerando pérdidas térmicas hacia el pasillo (a 14°C), si

éstas no hubiesen sido consideradas las variaciones de pérdidas térmicas prácticamente no

disminuyen, dado que la diferencia de temperatura entre interior y pasillo es muy baja en

comparación con el exterior (5,0°C versus 16,4°C), por lo que se observa una pérdida térmica similar.

19

**Tabla 10.** Pérdidas térmicas por tipo de departamento versus potencia de los radiadores

eléctricos.

Tal como se aprecia en la tabla anterior, los departamentos tipo 2, 8 y 16 presentan una mayor

pérdida térmica, donde los radiadores no son capaces de asumir la carga.

III.2 Ganancia de calor por radiación solar

De acuerdo, a lo estipulado por el plan de descontaminación atmosférica, la ganancia de calor por

radiación solar se estima por la cantidad de superficie que ocupan las ventanas en relación con su

orientación. En la siguiente tabla se observa los resultados obtenidos.

**Orientación** **Área de**
**superficie m** **[2 ]**

**Área ventana**

**m** **[2 ]**

**Porcentaje de**

**relación**

**Cumplimiento** **Diferencia**

**Norte** 1.002 455 45% SI

**Sur** 798 372 47% NO 3%

**Oriente** 844 350 41% SI

**Poniente** 878 332 41% SI

**Ponderado** **881** **385** **11%** SI

Tabla 11. Porcentaje de superficie de ventanas según orientación.

20

III.3 Condensación

A continuación, se presentan los resultados obtenidos para la condensación superficial e intersticial,
de acuerdo con lo estipulado en la norma NCh1973/2014.

Condensación superficial

Los resultados para la condensación superficial, basados en la metodología mencionada
anteriormente, siguiendo la NCh1973/2014, y los antecedentes recibidos, se presentan a

continuación, considerando tres escenarios de humedad relativa en el interior de la vivienda: 65%,

75% y 85%.

**A.** **Muros**

Considerando que la temperatura mínima promedio fue de 2,6 °C y 98% de humedad relativa

exterior, de acuerdo con los datos climatológicos obtenidos para la Provincia de Talca, el flujo de

calor hacia los muros es en dirección horizontal, y que la resistencia térmica del total del muro es

de R M = 1, 3

siguiente:

m [2] K

W ~~[,]~~ [ de acuerdo con las propiedades de los materiales de la ISO 10456, se tiene lo ]

|Prueba de condensación superficial|Col2|Col3|Col4|
|---|---|---|---|
|Presión de saturación del<br>vapor de agua interior|2.196 Pa|2.196 Pa|2.196 Pa|
|Humedad relativa interior|65%|75%|85%|
|Presión de vapor de aire<br>interior|1.427 Pa|1647 Pa|1.866 Pa|
|Humedad relativa máxima<br>aceptable|100%|100%|100%|
|Presión mínima de<br>saturación aceptable|1.427 Pa|1.647 Pa|1.866 Pa|
|Temperatura mínima de<br>superficie interior<br>aceptable|12,3 °C|14,5 °C|16,4 °C|
|Factor de temperatura<br>mínima de diseño|0,59|0,72|0,84|
|Resistencia térmica de la<br>superficie interior|0,13 m2K/W|0,13 m2K/W|0,13 m2K/W|
|Resistencia térmica total<br>interior|0,32 m2K/W|0,47 m2K/W|0,83 m2K/W|
|**Conclusión**|**No hay**<br>**condensación**<br>**superficial**|**No hay**<br>**condensación**<br>**superficial**|**No hay**<br>**condensación**<br>**superficial**|

Tabla 12. Prueba de condensación superficial para Muro con 65%, 75% y 85% de humedad relativa

interior.

21

**B.** **Pisos**

Considerando que la temperatura mínima promedio fue de 2,6 °C y 98% de humedad relativa

exterior, de acuerdo con los datos climatológicos obtenidos para la provincia de Talca, el flujo de

calor hacia el piso es en dirección hacia abajo, y que la resistencia térmica del total del piso es de

R P = 1, 7

siguiente:

m [2] K

W ~~[,]~~ [ de acuerdo con las propiedades de los materiales de la ISO 10456, se tiene lo ]

|Prueba de condensación superficial|Col2|Col3|Col4|
|---|---|---|---|
|Presión de saturación del<br>vapor de agua interior|2.196 Pa|2.196 Pa|2.196 Pa|
|Humedad relativa interior|65%|75%|85%|
|Presión de vapor de aire<br>interior|1.427 Pa|1.647 Pa|1.866 Pa|
|Humedad relativa máxima<br>aceptable|100%|100%|100%|
|Presión mínima de<br>saturación aceptable|1.427 Pa|1.647 Pa|1.866 Pa|
|Temperatura mínima de<br>superficie interior<br>aceptable|12,3 °C|14,5 °C|16,4 °C|
|Factor de temperatura<br>mínima de diseño|0,59|0,72|0,84|
|Resistencia térmica de la<br>superficie interior|0,17 m2K/W|0,17 m2K/W|0,17 m2K/W|
|Resistencia térmica total<br>interior|0,41 m2K/W|0,62 m2K/W|1,08 m2K/W|
|**Conclusión**|**No hay**<br>**condensación**<br>**superficial**|**No hay**<br>**condensación**<br>**superficial**|**No hay**<br>**condensación**<br>**superficial**|

Tabla 13. Prueba de condensación superficial para Piso con 65%, 75% y 85% de humedad relativa

interior.

**C.** **Techumbre**

Considerando que la temperatura mínima promedio fue de 2,6 °C y 98% de humedad relativa

exterior, de acuerdo con los datos climatológicos obtenidos para la Provincia de Talca, el flujo de

calor hacia la techumbre es en dirección hacia arriba, y que la resistencia térmica del total de la

techumbre es de R T = 3, 9

m [2] K

W ~~[,]~~ [ de acuerdo con las propiedades de los materiales de la ISO 10456, ]

y considerando que la resistencia de la techumbre tipo 1 y 2 es de 3,9 m [2] K/W se tiene lo siguiente:

22

|Prueba de condensación superficial|Col2|Col3|Col4|
|---|---|---|---|
|Presión de saturación del<br>vapor de agua interior|2.196 Pa|2.196 Pa|2.196 Pa|
|Humedad relativa interior|65%|75%|85%|
|Presión de vapor de aire<br>interior|1.427 Pa|1.647 Pa|1.866 Pa|
|Humedad relativa máxima<br>aceptable|100%|100%|100%|
|Presión mínima de<br>saturación aceptable|1.427 Pa|1.647 Pa|1866 Pa|
|Temperatura mínima de<br>superficie interior<br>aceptable|12,3 °C|14,5 °C|16,4 °C|
|Factor de temperatura<br>mínima de diseño|0,59|0,72|0,84|
|Resistencia térmica de la<br>superficie interior|0,10 m2K/W|0,10 m2K/W|0,10 m2K/W|
|Resistencia térmica total<br>interior|0,24 m2K/W|0,36 m2K/W|0,64 m2K/W|
|**Conclusión**|**No hay**<br>**condensación**<br>**superficial**|**No hay**<br>**condensación**<br>**superficial**|**No hay**<br>**condensación**<br>**superficial**|

Tabla 14. Prueba de condensación superficial para Techumbre con 65%, 75% y 85% de humedad

relativa interior.

Condensación intersticial

Los resultados para la condensación intersticial, basados en la metodología mencionada
anteriormente, siguiendo la NCh1973/2014, y los antecedentes recibidos, se presentan a

continuación, considerando tres escenarios de humedad relativa en el interior de la vivienda: 65%,

75% y 85%. Se considera que existe condensación intersticial cuando las curvas se intersecan en

alguna parte del recorrido.

23

**A.** **Muros**

Considerando que la temperatura mínima promedio fue de 2,6 °C y 98% de humedad relativa

exterior, de acuerdo con los datos climatológicos obtenidos para la provincia de Talca, el flujo de

calor hacia los muros es en dirección horizontal, y de acuerdo con las propiedades de los materiales

de la ISO 10456, se tiene obtienen los siguientes gráficos:

Figura 8: Gráfico de condensación intersticial en muros para humedad relativa interior de 65%.

Figura 9: Gráfico de condensación intersticial en muros para humedad relativa interior de 75%.

24

Figura 10: Gráfico de condensación intersticial en Muros para humedad relativa interior de 85%.

Es posible observar en los 3 gráficos que las curvas nunca se intersecan en ninguna parte del

recorrido, por lo tanto, se puede concluir que, para los tres escenarios de humedad relativa en el

interior de la vivienda o recinto, **no existirá condensación intersticial en muros.**

**B.** **Pisos**

Considerando que la temperatura mínima promedio fue de 2,6 °C y 98% de humedad relativa

exterior, de acuerdo con los datos climatológicos obtenidos para la provincia de Talca, el flujo de

calor hacia el piso es en dirección hacia abajo, y de acuerdo con las propiedades de los materiales

de la ISO 10456, se obtienen los siguientes gráficos:

25

Figura 11 : Gráfico de condensación intersticial en Piso para humedad relativa interior de 65%.

Figura 12 : Gráfico de condensación intersticial en Piso para humedad relativa interior de 75%.

26

Figura 13: Gráfico de condensación intersticial en Piso para humedad relativa interior de 85%.

Es posible observar en los 3 gráficos que las curvas nunca se intersecan en ninguna parte del

recorrido, por lo tanto, se puede concluir que, para los tres escenarios de humedad relativa en el

interior de la vivienda o recinto, **no existirá condensación intersticial en el piso.**

**C.** **Techumbre**

Considerando que la temperatura mínima promedio fue de 2,6 °C y 98% de humedad relativa

exterior, de acuerdo con los datos climatológicos obtenidos para la provincia de Talca, el flujo de

calor hacia la techumbre es en dirección hacia arriba, y de acuerdo con las propiedades de los

materiales de la ISO 10456, se obtienen los siguientes gráficos:

27

**Techumbres**

Figura 14: Gráfico de condensación intersticial en Techumbre 1 para humedad relativa interior de

65%.

Figura 15: Gráfico de condensación intersticial en Techumbre 1 para humedad relativa interior de

75%.

28

Figura 16: Gráfico de condensación intersticial en Techumbre 1 para humedad relativa interior de

85%.

Es posible observar en los 3 gráficos que las curvas no se intersecan, por lo tanto, se puede concluir

que, para los tres escenarios de humedad relativa en el interior de la vivienda o recinto, **no existirá**

**condensación intersticial en la techumbre.**

Por lo tanto, a modo de resumen, se tiene que **no existe** condensación intersticial para los 3 casos

de humedad relativa, tanto para muros, pisos y techumbres.

III.4 Producción de agua caliente sanitaria

Para definir el consumo de agua caliente de cada departamento se considera la ley 20.365 y los

análisis de simultaneidad. Utilizando los siguientes criterios de diseño.

**Temperatura de consumos de ACS °C** 40

**Temperatura de agua de red °C** 14

**Temperatura de acumulación °C** 60

**Consumo ACS litros/ persona/ día** 60

Tabla 15. Escenarios de diseño del ACS.

29

Al respecto se obtiene que el consumo diario de ACS es de 22.680 L, considerando una producción
por acumulación. Para esto se considera utilizar dos estanques de acumulación de 3.000 L c/u y un

tiempo de recuperación de 2 horas.

De acuerdo con el consumo de agua y a los estanques se considera utilizar dos calderas de
condensación murales con una capacidad de 102 kW y con rendimiento nominal a 80/60°C del

97,4%. Capaces de trabajar con combustible a gas Natural, lo que permite disminuir las emisiones

atmosféricas.

III.5 Ventilación y Hermeticidad del aire

Respecto a la extracción de aire, la normas NCh3308, NCh3309 y ASHRAE Std. 62-73 establecen

caudales de ventilación por recinto y persona. Considerando un escenario conservador entre estas

normas, tenemos que los caudales considerados son:

 Cocinas y baños: 9,4 L/(s persona)

 Dormitorios y recintos comunes: 2,5 L/(s persona)

De acuerdo con esto, se obtiene las renovaciones de aire necesarias por departamento y por recinto,

lo que permite entregar el equipo necesario para la carga de aire. La cantidad de personas por

recinto es referencial por departamento, de acuerdo con la cantidad de dormitorios, espacios

comunes, etc. Los diseños propuestos se muestran a continuación, donde las fichas técnicas de los

equipos se encuentran en anexos. Para este análisis se ha considerado el proyecto de ventilación

presentado en edificio Lote 3, considerando que para el edificio Lote 6 se considerará un proyecto

equivalente.

|Departamento|1601|Diseño Propuesto|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Recintos**|**Ingreso**<br>**de aire**<br>**L/s**|**Aireador**<br>**Muro**<br>**Jonás 4**|**Aireador**<br>**ventana**<br>**Fresh 32**<br>|**Celosía**<br>**en**<br>**puerta**<br>|**UTA**<br>|**Extractor**<br>**R100**<br>**BTH**<br>|**Extractor**<br>**R100**<br>**BTH 12 V**<br>|**Extractor**<br>**S125**<br>**BTH**<br>|**Extractor**<br>**intellivent**<br>**B **<br>|
|Dormitorio 1|45,86|1 <br>||<br>|<br>|<br>|<br>|<br>|<br>|
|Dormitorio 2|Dormitorio 2||1|||||||
|Dormitorio 3|Dormitorio 3||1|||||||
|Living-comedor|Living-comedor|1||||||||
|Hall y sala estar|Hall y sala estar|||||||||
|Cocina|Cocina|||1||||1||
|Baño 1|Baño 1|||1|||1|||
|Baño 2|Baño 2|||1||1||||
|Baño 3|Baño 3|||1||1||||

Tabla 16. Diseño propuesto para ventilación departamento 1601.

30

|Departamento|1606|Diseño Propuesto|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Recintos**|**Ingreso**<br>**de aire**<br>**L/s**|**Aireador**<br>**Muro**<br>**Jonás 4**<br>|**Aireador**<br>**ventana**<br>**Fresh 32**|**Celosía**<br>**en**<br>**puerta**<br>|**UTA**<br>|**Extractor**<br>**R100**<br>**BTH**<br>|**Extractor**<br>**R100**<br>**BTH 12V**<br>|**Extractor**<br>**S125 BTH**<br>|**Extractor**<br>**intellivent**<br>**B **<br>|
|Dormitorio 1|30,22|<br>|1|<br>|<br>|<br>|<br>|<br>|<br>|
|Dormitorio 2|Dormitorio 2||1 <br>|<br>|<br>|<br>|<br>|<br>|<br>|
|Living-comedor|Living-comedor|1 <br>|<br>|<br>||<br>|<br>|<br>|<br>|
|W. closet|W. closet|<br>|<br>||1 <br>|<br>|<br>||<br>|
|Cocina|Cocina|<br>|<br>|1|<br>|<br>||1 <br>|<br>|
|Baño 1|Baño 1|||1|||1|||
|Baño 2|Baño 2|||1|||||1|

Tabla 17. Diseño propuesto para ventilación departamento 1606.

|Departamento|TIPO 1|Diseño Propuesto|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Recintos**|**Ingreso**<br>**de aire**<br>**L/s**|**Aireador**<br>**Muro**<br>**Jonás 4**|**Aireador**<br>**ventana**<br>**Fresh 32**<br>|**Celosía**<br>**en**<br>**puerta**<br>|**UTA**<br>|**Extractor**<br>**R100 BTH**<br>|**Extractor**<br>**R100 BTH**<br>**12V**<br>|**Extractor**<br>**S125 BTH**<br>|**Extractor**<br>**intellivent**<br>**B **<br>|
|Dormitorio 1|37,40|1|<br>|<br>|<br>|<br>|<br>|<br>|<br>|
|Dormitorio 2|Dormitorio 2|1||||||||
|Dormitorio 3|Dormitorio 3|1||||||||
|Living-comedor|Living-comedor||1|||||||
|W. closet|W. closet||||2|||||
|Cocina|Cocina|||||||1||
|Baño 1|Baño 1|||1|||||1|
|Baño 2|Baño 2|||1||1||||
|Baño 3|Baño 3|||1||1||||

Tabla 18. Diseño propuesto para ventilación departamento tipo 1.

|Departamento|TIPO 2|Diseño Propuesto|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Recintos**|**Ingreso**<br>**de aire**<br>**L/s**|**Aireador**<br>**Muro**<br>**Jonás 4**|**Aireador**<br>**ventana**<br>**Fresh 32**<br>|**Celosía**<br>**en**<br>**puerta**<br>|**UTA**<br>|**Extractor**<br>**R100 BTH**<br>|**Extractor**<br>**R100 BTH**<br>**12V**<br>|**Extractor**<br>**S125 BTH**<br>|**Extractor**<br>**intellivent**<br>**B **<br>|
|Dormitorio 1|27,02|1|<br>|<br>|<br>|<br>|<br>|<br>|<br>|
|Dormitorio 2|Dormitorio 2|1 <br>||<br>|<br>|<br>|<br>|<br>|<br>|
|Living-comedor|Living-comedor|<br>|1 <br>|<br>||<br>|<br>|<br>|<br>|
|W. closet|W. closet|<br>|<br>||2 <br>|<br>|<br>||<br>|
|Cocina|Cocina|<br>|<br>|1|<br>|<br>|<br>|1 <br>||
|Baño 1|Baño 1|||1|||||1|
|Baño 2|Baño 2|||1||1||||

Tabla 19. Diseño propuesto para ventilación departamento tipo 2.

31

|Departamento|TIPO 4 y 7|Diseño Propuesto|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Recintos**|**Ingreso**<br>**de aire**<br>**L/s**|**Aireador**<br>**Muro**<br>**Jonás 4**|**Aireador**<br>**ventana**<br>**Fresh 32**<br>|**Celosía**<br>**en**<br>**puerta**<br>|**UTA**<br>|**Extractor**<br>**R100 BTH**<br>|**Extractor**<br>**R100 BTH**<br>**12V**<br>|**Extractor**<br>**S125 BTH**<br>|**Extractor**<br>**intellivent**<br>**B **<br>|
|Dormitorio 1|22,46|1|<br>|<br>|<br>|<br>|<br>|<br>|<br>|
|Dormitorio 2|Dormitorio 2|1||||||||
|Living-comedor-<br>cocina|Living-comedor-<br>cocina|<br>|1 <br>|<br>|<br>|<br>|<br>|1 <br>||
|Baño|Baño||||||||1|

Tabla 20. Diseño propuesto para ventilación departamento tipo 4 y 7.

|Departamento|TIPO 5 y 6|Diseño Propuesto|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Recintos**|**Ingreso**<br>**de aire**<br>**L/s**|**Aireador**<br>**Muro**<br>**Jonás 4**<br>|**Aireador**<br>**ventana**<br>**Fresh 32**|**Celosía**<br>**en**<br>**puerta**<br>|**UTA**<br>|**Extractor**<br>**R100 BTH**<br>|**Extractor**<br>**R100 BTH**<br>**12V**<br>|**Extractor**<br>**S125 BTH**<br>|**Extractor**<br>**intellivent**<br>**B **<br>|
|Dormitorio|14,88||1|||||||
|Living-comedor-<br>cocina|Living-comedor-<br>cocina|<br>|1 <br>||<br>|<br>|<br>|1 <br>|<br>|
|W. closet|W. closet|<br>|<br>|1|<br>|<br>|<br>|<br>||
|Baño|Baño|||1|||||1|

Tabla 21. Diseño propuesto para ventilación departamento tipo 5 y 6.

|Departamento|TIPO 8|Diseño Propuesto|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Recintos**|**Ingreso**<br>**de aire**<br>**L/s**|**Aireador**<br>**Muro**<br>**Jonás 4**<br>|**Aireador**<br>**ventana**<br>**Fresh 32**|**Celosía**<br>**en**<br>**puerta**<br>|**UTA**<br>|**Extractor**<br>**R100 BTH**<br>|**Extractor**<br>**R100 BTH**<br>**12V**<br>|**Extractor**<br>**S125 BTH**<br>|**Extractor**<br>**intellivent**<br>**B **<br>|
|Dormitorio 1|25,73|<br>|1|<br>|<br>|<br>|<br>|<br>|<br>|
|Dormitorio 2|Dormitorio 2||1|||||||
|Living-comedor-<br>cocina|Living-comedor-<br>cocina|<br>|1 <br>|<br>||<br>|<br>|1 <br>|<br>|
|W. closet 1|W. closet 1|<br>|<br>|<br>|1|<br>|<br>|<br>|<br>|
|W. closet 2|W. closet 2|<br>|<br>|<br>|1 <br>|<br>|<br>|<br>||
|Baño 1|Baño 1||||||||1|
|Baño 2|Baño 2|||||1||||

Tabla 22. Diseño propuesto para ventilación departamento tipo 8.

32

|Departamento|TIPO 3|Diseño Propuesto|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|**Recintos**|**Ingreso**<br>**de aire**<br>**L/s**|**Aireador**<br>**Muro**<br>**Jonás 4**<br>|**Aireador**<br>**ventana**<br>**Fresh 32**|**Celosía**<br>**en**<br>**puerta**<br>|**UTA**<br>|**Extractor**<br>**R100 BTH**<br>|**Extractor**<br>**R100 BTH**<br>**12V**<br>|**Extractor**<br>**S125 BTH**<br>|**Extractor**<br>**intellivent**<br>**B **<br>|
|Dormitorio 1||<br>|1|<br>|<br>|<br>|<br>|<br>|<br>|
|Dormitorio 2|Dormitorio 2||1|||||||
|Living-comedor-<br>cocina|Living-comedor-<br>cocina|<br>|1 <br>||<br>|<br>|<br>|1 <br>|<br>|
|W. closet|W. closet|<br>|<br>|1|<br>|<br>|<br>|<br>||
|Baño 1|Baño 1|<br>|<br>|1|<br>||<br>|<br>|1 <br>|
|Baño 2|Baño 2|||1||1||||

Tabla 23. Diseño propuesto para ventilación departamento tipo 3.

Para efectos de cumplir con los estándares señalados en el PDA, se ha optado por el uso de especificaciones

técnicas mínimas del MINVU aplicados en los PDA. Lo anterior entrega un set de soluciones constructivas para

la hermeticidad al paso de aire en ventanas y puertas.

**Ventanas**

El proyecto considera la ficha HV sobre los detalles de las soluciones constructivas para la hermeticidad al

paso del aire en ventanas, la cual forma parte de las especificaciones mínimas del MINVU para el PDA.

De acuerdo con la NCh3297 y NCh3296, una **ventana corredera de 1,4 m x 2,0 m** presenta las siguientes

características relevantes:

 - Transmitancia térmica: 3,5 W/(m [2] K)

 - Permeabilidad al aire a 100 Pa: 5,3 m [3] /(hm [2] )

La exigencia mínima del PDA indica que, para la región del Maule y la provincia de Talca, la permeabilidad
máxima debe ser de 10 m [3] /hm [2], por lo tanto, se cumple con este requerimiento.

De acuerdo con la NCh3297 y NCh3296, una **ventana de abatir de 0,6 m x 1,0 m** presenta las siguientes

características relevantes:

 - Transmitancia térmica: 3,8 W/(m [2] K)

 - Permeabilidad al aire a 100 Pa: 2,0 m [3] /(hm [2] )

La exigencia mínima del PDA indica que para la región del Maule y la provincia de Talca, la permeabilidad
máxima debe ser de 10 m [3] /hm [2], por lo tanto se cumple con este requerimiento.

De acuerdo con la NCh3297 y NCh3296, una **ventana de abatir de 1,2 m x 1,5 m** presenta las siguientes

características relevantes:

 - Transmitancia térmica: 3,6 W/(m [2] K)

 - Permeabilidad al aire a 100 Pa: 4,7 m [3] /(hm [2] )

33

La exigencia mínima del PDA indica que, para la región del Maule y la provincia de Talca, la permeabilidad
máxima debe ser de 10 m [3] /(hm [2] ), por lo tanto, se cumple con este requerimiento.

**Puertas**

El proyecto considera la ficha HP sobre los detalles de las soluciones constructivas para la hermeticidad al

paso del aire en puertas, la cual forma parte de las especificaciones mínimas del MINVU para el PDA.

De acuerdo con la NCh3297 y NCh3296, una **puerta de madera maciza lisa exterior de 0,8 m x 2,0 m** presenta

las siguientes características relevantes:

 - Transmitancia térmica: 1,7 W/(m [2] K)

 - Permeabilidad al aire a 100 Pa: 7,9 m [3] /(hm [2] )

La exigencia mínima del PDA indica que, para la región del Maule y la Provincia de Talca, la permeabilidad
máxima debe ser de 10 m [3] /(hm [2] ), por lo tanto, se cumple con este requerimiento.

De acuerdo con la NCh3297 y NCh3296, una **puerta de madera maciza lisa exterior de 0,85 m x 2,0 m** presenta

las siguientes características relevantes:

 - Transmitancia térmica: 1,7 W/(m [2] K)

 - Permeabilidad al aire a 100 Pa: 7,0 m [3] /(hm [2] )

La exigencia mínima del PDA indica que, para la región del Maule y la Provincia de Talca, la permeabilidad
máxima debe ser de 10 m [3] /(hm [2] ), por lo tanto, se cumple con este requerimiento.

**Nota:**

Las fichas HV y HP sobre los detalles para la hermeticidad al paso del aire para ventanas y puertas se adjunta

en Anexos.

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 5.: Cálculo térmico muros. Fuente: Elaboración propia.**

| Material | Espesor (mm) | k ( W/(mK) ) | Resistencia m2K/W |
| --- | --- | --- | --- |
| **Hormigón armado** | 120 | 1,630 | 0,12 |
| **ESP den=15** | 60 | 0,041 | 0,97 |
| Total resistencias conductivas, m2K/W | Total resistencias conductivas, m2K/W | Total resistencias conductivas, m2K/W | 1,53 |
| Total resistencias de convección interior y exterior, m2K/W | Total resistencias de convección interior y exterior, m2K/W | Total resistencias de convección interior y exterior, m2K/W | 0,22 |
| Resistencia térmica total m2K/W | Resistencia térmica total m2K/W | Resistencia térmica total m2K/W | 1,75 |
| **Transmitancia térmica “U” W/(m2K)** | **Transmitancia térmica “U” W/(m2K)** | **Transmitancia térmica “U” W/(m2K)** | **0,57** |
| **Cumplimiento** | **Cumplimiento** | **Cumplimiento** | **SI** |

**Tabla 7.: Cálculo térmico techumbre 1 piso 16. Fuente: Elaboración propia.**

| Techumbre 2 piso 15 | Col2 | Col3 | Col4 |
| --- | --- | --- | --- |
| **Material** | **Espesor (mm)** | **k ( W/(mK) )** | **Resistencia m2K/W** |
| **Hormigón armado** | 150 | 1,630 | 0,12 |
| **Poliestireno expandido,**<br>**ρ=30 kg/m3 ** | 150 | 0,041 | 3,65 |
| **Yeso cartón, ρ=30 kg/m3 ** | 10 | 0,260 | 0,04 |
| Total resistencias conductivas, m2K/W | Total resistencias conductivas, m2K/W | Total resistencias conductivas, m2K/W | 3,81 |
| Total resistencias de convección interior y exterior, m2K/W | Total resistencias de convección interior y exterior, m2K/W | Total resistencias de convección interior y exterior, m2K/W | 0,14 |
| Resistencia térmica total m2K/W | Resistencia térmica total m2K/W | Resistencia térmica total m2K/W | 3,95 |
| **Transmitancia térmica “U” W/(m2K)** | **Transmitancia térmica “U” W/(m2K)** | **Transmitancia térmica “U” W/(m2K)** | **0,25** |
| **Cumplimiento** | **Cumplimiento** | **Cumplimiento** | **SI** |

**Tabla 16.: Diseño propuesto para ventilación departamento 1601.**

| Departamento | 1606 | Diseño Propuesto | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Recintos** | **Ingreso**<br>**de aire**<br>**L/s** | **Aireador**<br>**Muro**<br>**Jonás 4**<br> | **Aireador**<br>**ventana**<br>**Fresh 32** | **Celosía**<br>**en**<br>**puerta**<br> | **UTA**<br> | **Extractor**<br>**R100**<br>**BTH**<br> | **Extractor**<br>**R100**<br>**BTH 12V**<br> | **Extractor**<br>**S125 BTH**<br> | **Extractor**<br>**intellivent**<br>**B **<br> |
| Dormitorio 1 | 30,22 | <br> | 1 | <br> | <br> | <br> | <br> | <br> | <br> |
| Dormitorio 2 | Dormitorio 2 |  | 1 <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| Living-comedor | Living-comedor | 1 <br> | <br> | <br> |  | <br> | <br> | <br> | <br> |
| W. closet | W. closet | <br> | <br> |  | 1 <br> | <br> | <br> |  | <br> |
| Cocina | Cocina | <br> | <br> | 1 | <br> | <br> |  | 1 <br> | <br> |
| Baño 1 | Baño 1 |  |  | 1 |  |  | 1 |  |  |
| Baño 2 | Baño 2 |  |  | 1 |  |  |  |  | 1 |

**Tabla 17.: Diseño propuesto para ventilación departamento 1606.**

| Departamento | TIPO 1 | Diseño Propuesto | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Recintos** | **Ingreso**<br>**de aire**<br>**L/s** | **Aireador**<br>**Muro**<br>**Jonás 4** | **Aireador**<br>**ventana**<br>**Fresh 32**<br> | **Celosía**<br>**en**<br>**puerta**<br> | **UTA**<br> | **Extractor**<br>**R100 BTH**<br> | **Extractor**<br>**R100 BTH**<br>**12V**<br> | **Extractor**<br>**S125 BTH**<br> | **Extractor**<br>**intellivent**<br>**B **<br> |
| Dormitorio 1 | 37,40 | 1 | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| Dormitorio 2 | Dormitorio 2 | 1 |  |  |  |  |  |  |  |
| Dormitorio 3 | Dormitorio 3 | 1 |  |  |  |  |  |  |  |
| Living-comedor | Living-comedor |  | 1 |  |  |  |  |  |  |
| W. closet | W. closet |  |  |  | 2 |  |  |  |  |
| Cocina | Cocina |  |  |  |  |  |  | 1 |  |
| Baño 1 | Baño 1 |  |  | 1 |  |  |  |  | 1 |
| Baño 2 | Baño 2 |  |  | 1 |  | 1 |  |  |  |
| Baño 3 | Baño 3 |  |  | 1 |  | 1 |  |  |  |

**Tabla 18.: Diseño propuesto para ventilación departamento tipo 1.**

| Departamento | TIPO 2 | Diseño Propuesto | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Recintos** | **Ingreso**<br>**de aire**<br>**L/s** | **Aireador**<br>**Muro**<br>**Jonás 4** | **Aireador**<br>**ventana**<br>**Fresh 32**<br> | **Celosía**<br>**en**<br>**puerta**<br> | **UTA**<br> | **Extractor**<br>**R100 BTH**<br> | **Extractor**<br>**R100 BTH**<br>**12V**<br> | **Extractor**<br>**S125 BTH**<br> | **Extractor**<br>**intellivent**<br>**B **<br> |
| Dormitorio 1 | 27,02 | 1 | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| Dormitorio 2 | Dormitorio 2 | 1 <br> |  | <br> | <br> | <br> | <br> | <br> | <br> |
| Living-comedor | Living-comedor | <br> | 1 <br> | <br> |  | <br> | <br> | <br> | <br> |
| W. closet | W. closet | <br> | <br> |  | 2 <br> | <br> | <br> |  | <br> |
| Cocina | Cocina | <br> | <br> | 1 | <br> | <br> | <br> | 1 <br> |  |
| Baño 1 | Baño 1 |  |  | 1 |  |  |  |  | 1 |
| Baño 2 | Baño 2 |  |  | 1 |  | 1 |  |  |  |

**Tabla 19.: Diseño propuesto para ventilación departamento tipo 2.**

| Departamento | TIPO 4 y 7 | Diseño Propuesto | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Recintos** | **Ingreso**<br>**de aire**<br>**L/s** | **Aireador**<br>**Muro**<br>**Jonás 4** | **Aireador**<br>**ventana**<br>**Fresh 32**<br> | **Celosía**<br>**en**<br>**puerta**<br> | **UTA**<br> | **Extractor**<br>**R100 BTH**<br> | **Extractor**<br>**R100 BTH**<br>**12V**<br> | **Extractor**<br>**S125 BTH**<br> | **Extractor**<br>**intellivent**<br>**B **<br> |
| Dormitorio 1 | 22,46 | 1 | <br> | <br> | <br> | <br> | <br> | <br> | <br> |
| Dormitorio 2 | Dormitorio 2 | 1 |  |  |  |  |  |  |  |
| Living-comedor-<br>cocina | Living-comedor-<br>cocina | <br> | 1 <br> | <br> | <br> | <br> | <br> | 1 <br> |  |
| Baño | Baño |  |  |  |  |  |  |  | 1 |

**Tabla 20.: Diseño propuesto para ventilación departamento tipo 4 y 7.**

| Departamento | TIPO 5 y 6 | Diseño Propuesto | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Recintos** | **Ingreso**<br>**de aire**<br>**L/s** | **Aireador**<br>**Muro**<br>**Jonás 4**<br> | **Aireador**<br>**ventana**<br>**Fresh 32** | **Celosía**<br>**en**<br>**puerta**<br> | **UTA**<br> | **Extractor**<br>**R100 BTH**<br> | **Extractor**<br>**R100 BTH**<br>**12V**<br> | **Extractor**<br>**S125 BTH**<br> | **Extractor**<br>**intellivent**<br>**B **<br> |
| Dormitorio | 14,88 |  | 1 |  |  |  |  |  |  |
| Living-comedor-<br>cocina | Living-comedor-<br>cocina | <br> | 1 <br> |  | <br> | <br> | <br> | 1 <br> | <br> |
| W. closet | W. closet | <br> | <br> | 1 | <br> | <br> | <br> | <br> |  |
| Baño | Baño |  |  | 1 |  |  |  |  | 1 |

**Tabla 21.: Diseño propuesto para ventilación departamento tipo 5 y 6.**

| Departamento | TIPO 8 | Diseño Propuesto | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Recintos** | **Ingreso**<br>**de aire**<br>**L/s** | **Aireador**<br>**Muro**<br>**Jonás 4**<br> | **Aireador**<br>**ventana**<br>**Fresh 32** | **Celosía**<br>**en**<br>**puerta**<br> | **UTA**<br> | **Extractor**<br>**R100 BTH**<br> | **Extractor**<br>**R100 BTH**<br>**12V**<br> | **Extractor**<br>**S125 BTH**<br> | **Extractor**<br>**intellivent**<br>**B **<br> |
| Dormitorio 1 | 25,73 | <br> | 1 | <br> | <br> | <br> | <br> | <br> | <br> |
| Dormitorio 2 | Dormitorio 2 |  | 1 |  |  |  |  |  |  |
| Living-comedor-<br>cocina | Living-comedor-<br>cocina | <br> | 1 <br> | <br> |  | <br> | <br> | 1 <br> | <br> |
| W. closet 1 | W. closet 1 | <br> | <br> | <br> | 1 | <br> | <br> | <br> | <br> |
| W. closet 2 | W. closet 2 | <br> | <br> | <br> | 1 <br> | <br> | <br> | <br> |  |
| Baño 1 | Baño 1 |  |  |  |  |  |  |  | 1 |
| Baño 2 | Baño 2 |  |  |  |  | 1 |  |  |  |

**Tabla 22.: Diseño propuesto para ventilación departamento tipo 8.**

| Departamento | TIPO 3 | Diseño Propuesto | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Recintos** | **Ingreso**<br>**de aire**<br>**L/s** | **Aireador**<br>**Muro**<br>**Jonás 4**<br> | **Aireador**<br>**ventana**<br>**Fresh 32** | **Celosía**<br>**en**<br>**puerta**<br> | **UTA**<br> | **Extractor**<br>**R100 BTH**<br> | **Extractor**<br>**R100 BTH**<br>**12V**<br> | **Extractor**<br>**S125 BTH**<br> | **Extractor**<br>**intellivent**<br>**B **<br> |
| Dormitorio 1 |  | <br> | 1 | <br> | <br> | <br> | <br> | <br> | <br> |
| Dormitorio 2 | Dormitorio 2 |  | 1 |  |  |  |  |  |  |
| Living-comedor-<br>cocina | Living-comedor-<br>cocina | <br> | 1 <br> |  | <br> | <br> | <br> | 1 <br> | <br> |
| W. closet | W. closet | <br> | <br> | 1 | <br> | <br> | <br> | <br> |  |
| Baño 1 | Baño 1 | <br> | <br> | 1 | <br> |  | <br> | <br> | 1 <br> |
| Baño 2 | Baño 2 |  |  | 1 |  | 1 |  |  |  |
