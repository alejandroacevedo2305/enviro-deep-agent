---
title: Sin título
author: Jorge
date: D:20170319021735-03'00'
language: es
type: report
pages: 23
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Modelación de Emisiones Contaminantes de COV para estanques de almacenamiento y de proceso, en instalaciones de Renner - Sayerlack Chile S.A.
  - Anexo #1
-->

# Modelación de Emisiones Contaminantes de COV para estanques de almacenamiento y de proceso, en instalaciones de Renner - Sayerlack Chile S.A.

**OBJETIVO**

Determinar las emanaciones de Compuestos Orgánicos Volátiles (COV) al Medio
Ambiente de los distintos compuestos orgánicos volátiles, presentes en el almacenamiento
de Materias Primas para la fabricación de pinturas y barnices industriales.

**ALCANCE**

Esta modelación es aplicable a los estanques de Materias Primas y Productos terminados de
la empresa Renner Sayerlack Chile S.A., ubicada en la comuna de Lampa, Región
Metropolitana.

El cálculo de COV corresponde a las siguientes zonas:

- Producción.

- Fraccionamiento de materias primas en Bodega Inflamable.

- Estanques superficiales y subterráneos.

- Dispersores y Mixer de procesos.

**METODOLOGIA**

Para el modelamiento se utiliza el software EPA TANKS 4.09 del American Petroleum
Institute (API), que permite una rápida estimación de emisiones desde estanques de
almacenamiento.

EPA TANKS es un programa informático basado en Windows que calcula las emisiones de
compuestos orgánicos volátiles (COV) y contaminantes peligrosos del aire (HAP) de los
tanques de almacenamiento de techo fijo y flotante. TANKS se basa en los procedimientos
de estimación de emisiones de la Compilación de Factores de Emisión de Contaminantes
Atmosféricos (AP-42) de la EPA.

Los tanques de almacenamiento con cubiertas techo fijo que contienen líquidos orgánicos
son ampliamente utilizados en todas las industrias que producen o consumen líquidos
orgánicos. Las emisiones de los tanques de almacenamiento de techo fijo (COV) consisten
en pérdidas por trabajo y pérdidas respiratorias (a menudo denominadas pérdidas
permanentes).

_**Emanaciones o pérdidas por trabajo**_

Las pérdidas de trabajo se producen cuando el vapor en el espacio de vapor sobre el líquido
se desplaza del tanque mediante la adición de líquido orgánico durante el llenado del
tanque. Las pérdidas por trabajo dependen de la cantidad anual de material bombeado, de la
presión de vapor del material almacenado y de la temperatura ambiente. Las pérdidas por
trabajo pueden estimarse mediante:

Lw = Qw (1/359)(273.15/T)(VP/760)(MW)(KN)(Kp) (1)

KN, factor de renovación, está basado en el número de renovaciones por año,
N, el cual está definido como
N = Qw/VT.
KN = (180 + N)/6N para N > 36 y KN = 1 para N < 36.
Kp, factor de pérdidas por trabajo, está definido como Kp = 0.75 para aceite crudo y Kp =
1.0 para líquido orgánico

_**Emanaciones o pérdidas respiratorias**_

Las pérdidas respiratorias se producen porque las diferencias de temperatura (como los
cambios entre las temperaturas diurnas y nocturnas) afectan la presión del espacio de vapor
dentro de los tanques de almacenamiento. Los vapores se expanden con un aumento de
temperatura y se contraen con una disminución de la temperatura. Además, la
concentración de vapor saturado de una sustancia en el aire aumenta con el aumento de la
temperatura y disminuye con la disminución de la temperatura. A medida que la
temperatura exterior aumenta durante el día, la presión dentro de un tanque aumenta y el
aire será expulsado del tanque. A medida que la temperatura disminuye durante la noche, la
presión en el tanque disminuye y el aire fresco fluye hacia el tanque. El método
simplificado para calcular las pérdidas respiratorias es una adaptación de un método EPA.
Considere un tanque con un volumen de VT y un nivel de líquido LT. El espacio de vapor
del tanque es:

Vv = VT(100 - LT)/100 (2)

El factor de expansión (KE) del vapor debido a la fluctuación de la temperatura día-noche
se define como:

KE = TR/T (3)

Donde la temperatura ambiente media es T y la fluctuación de la temperatura diurna es TR.
El desplazamiento total de aire por día se calcula mediante:

Maire = (Vv)(1/359)(KE)(273.15/T) (4)

Donde la temperatura ambiente media es T y la fluctuación de la temperatura diurna es TR.
El desplazamiento total de aire por día se calcula mediante:

Lb = 365Maire(VP/760)(MW) (5)

_**Metodología convencional de la EPA**_

El procedimiento de la EPA para estimar las pérdidas por trabajo asume una temperatura
constante de 15 ° C (59 ° F), pero es por lo demás idéntico al método de atajo descrito
anteriormente. El método adoptado por la EPA para estimar las pérdidas respiratorias se
describe en su totalidad. La ecuación básica es:

Ls = 365(Vv)(Wv)(KE)(Ks) (6)

En términos generales, el factor de expansión del espacio de vapor (KE) representa el
efecto combinado de la fluctuación de la temperatura día-noche sobre el volumen de los
vapores y sobre la presión de vapor del líquido en el tanque. El factor de saturación de
vapor ventilado (Ks) puede ser visto como el acercamiento a la saturación del líquido en el
espacio de vapor. Se rige por la presión de vapor del líquido y la interrupción del tanque
(altura del espacio de vapor en el tanque). El factor de saturación se aproxima a 1,0 cuando
la presión de vapor es baja o la interrupción del tanque es pequeña.

Los términos anteriores. El método EPA reconoce que la temperatura del líquido y la
temperatura del espacio de vapor pueden ser diferentes de la temperatura ambiente. Se
proporcionan fórmulas empíricas para determinar las temperaturas del líquido y de los
vapores si se dan la temperatura ambiente y el intervalo diario. Todas estas consideraciones
están el el software EPA TANK.

**UBICACIÓN**

Se presenta Lay-out de planta donde se indica la ubicación de las diferentes zonas del
proyecto sujetas a este estudio.

**ESTANQUES A CONSIDERAR**

|N° Estanque|Capacidad|Solvente|Estatus|
|---|---|---|---|
|1|10 m3|Metanol|Existente|
|2|10 m3|Aguarrás|Existente|
|3|10 m3|Xilol|Existente|
|4|10 m3|Acetato de etilo|Existente|
|5|10 m3|Aguarrás|Existente|
|6|20 m3|Resina base Aguarrás|Proyectado|
|7|20 m3|Resina base Metanol|Proyectado|
|8|20 m3|Resina base Xilol|Proyectado|
|9|1,1 m3|Dispersión base Xilol|Existente|
|10|1,1 m3|Dispersión base Xilol|Existente|
|11|1,1 m3|Dispersión<br>base<br>Aguarrás|Existente|
|12|1,1 m3|Dispersión<br>base<br>Aguarrás|Existente|

**MATERIAS PRIMAS UTILIZADAS**

El modelamiento considera utilizar las materias primas que son utilizadas en la fabricación
de pinturas, barnices y tintas que emplean resinas dispersas en base de solvente orgánico, y
el solvente predominante en la formulación de la mezcla.

En la tabla siguiente se presentan las sustancias inflamables que componen las diferentes
materias primas y productos terminados que serán almacenados en los estanques de
almacenamiento.

|Producto|NU|Clase|
|---|---|---|
|Metanol|1230|3|
|Aguarrás|1263|3|
|Xilol|1307|3|
|Acetato de etilo|1173|3|

**RESULTADOS**

La aplicación del software de EPA TANKS 4.09 considerando condiciones de presión y
temperatura promedio de Enero de 2017 arroja como resultado de la modelación:

|N° Estanque|Solvente|COV<br>Emisiones<br>Lb/año|COV<br>Emisiones<br>Kg/año|
|---|---|---|---|
|1|Metanol|27,7|12,57|
|2|Aguarrás|0,66|0,29|
|3|Xilol|4,38|1,98|
|4|Acetato de etilo|60,83|27,61|
|5|Aguarrás|0,66|0,29|
|6|Resina base Aguarrás|1,7|0,77|
|7|Resina base Metanol|80,51|36,55|
|8|Resina base Xilol|11,44|5,19|
|9|Dispersión de resina en<br>base Xilol|11,36|5,16|
|10|Dispersión de resina en<br>base Xilol|11,36|5,16|
|11|Dispersión de resina en<br>base Aguarrás|38,52|17,49|
|12|Dispersión de resina en<br>base Aguarrás|38,52|17,49|
|**TOTAL**||**287,6**|**130,5**|

Las emanaciones de Compuestos Orgánicos Volátiles (COV) al Medio Ambiente,
determinado para los compuestos relevantes corresponde a 130,5 kilógramos por año.

Se adjuntan a continuación las fichas de cálculo para cada estanque.

# Anexo #1

## Reportes generados por el software EPA TKS

**TANKS 4.0.9d**

**Emissions Report - Summary Format**
**Tank Indentification and Physical Characteristics**

**Identification**

User Identification: Tk N°1
City: Santiago
State: Chile

Company:

Type of Tank: Horizontal Tank
Description: Contiene Metanol
**Tank Dimensions**
Shell Length (ft): 10,49
Diameter (ft): 6,56
Volume (gallons): 2.642,00
Turnovers: 12,00
Net Throughput(gal/yr): 31.704,00
Is Tank Heated (y/n): N
Is Tank Underground (y/n): Y
**Paint Characteristics**

Shell Color/Shade:

Shell Condition
**Breather Vent Settings**
Vacuum Settings (psig): -0,03
Pressure Settings (psig) 0,03
Meterological Data used in Emissions Calculations: Santiago, Chile (Avg Atmospheric Pressure = 13 psia)

**Tk N°1 - Horizontal Tank**
**Santiago, Chile**

**TANKS 4.0.9d**

**Emissions Report - Summary Format**

**Liquid Contents of Storage Tank**

Liquid

Daily Liquid Surf.
Temperature (deg F)

Bulk
Temp Vapor Pressure (psia)

Vapor

Liquid

Vapor

Temperature (deg F) Temp Vapor Pressure (psia) Mol. Mass Mass Mol. Basis f

Mixture/Component Month Avg. Min. Max. (deg F) Avg. Min. Max. Weight. Fract. Fract. Weight Calcul

Mol.

Mass

Methyl alcohol All 52,80 52,80 52,80 52,36 1,1452 1,1452 1,1452 32,0400 32,04 Option

**TANKS 4.0.9d**

**Emissions Report - Summary Format**

**Individual Tank Emission Totals**

**Emissions Report for: Annual**

**Tk N°1 - Horizontal Tank**
**Santiago, Chile**

|Col1|Losses(lbs)|Col3|Col4|
|---|---|---|---|
|Components|Working Loss|Breathing Loss|Total Emissions|
|Methyl alcohol|27,70|0,00|27,70|

**TANKS 4.0.9d**

**Emissions Report - Summary Format**
**Tank Indentification and Physical Characteristics**

**Identification**

User Identification: Tk N°2
City: Santiago
State: Chile
Company:
Type of Tank: Horizontal Tank
Description: Contiene Aguarrás
**Tank Dimensions**
Shell Length (ft): 10,49
Diameter (ft): 6,56
Volume (gallons): 2.642,00
Turnovers: 12,00
Net Throughput(gal/yr): 31.704,00
Is Tank Heated (y/n): N
Is Tank Underground (y/n): Y
**Paint Characteristics**

Shell Color/Shade:

Shell Condition
**Breather Vent Settings**
Vacuum Settings (psig): -0,03
Pressure Settings (psig) 0,03
Meterological Data used in Emissions Calculations: Santiago, Chile (Avg Atmospheric Pressure = 13 psia)

**TANKS 4.0.9d**

**Emissions Report - Summary Format**

**Liquid Contents of Storage Tank**

**Tk N°2 - Horizontal Tank**
**Santiago, Chile**

Liquid

Daily Liquid Surf.
Temperature (deg F)

Bulk
Temp Vapor Pressure (psia)

Vapor

Liquid

Vapor

Temperature (deg F) Temp Vapor Pressure (psia) Mol. Mass Mass Mol. Basis

Mixture/Component Month Avg. Min. Max. (deg F) Avg. Min. Max. Weight. Fract. Fract. Weight Calcu

Mol.

Mass

Jet kerosene All 52,80 52,80 52,80 52,36 0,0067 0,0067 0,0067 130,0000 162,00 Option

**Emissions Report for: Annual**

**Tk N°2 - Horizontal Tank**
**Santiago, Chile**

**TANKS 4.0.9d**

**Emissions Report - Summary Format**

**Individual Tank Emission Totals**

|Col1|Losses(lbs)|Col3|Col4|
|---|---|---|---|
|Components|Working Loss|Breathing Loss|Total Emissions|
|Jet kerosene|0,66|0,00|0,66|

**TANKS 4.0.9d**

**Emissions Report - Summary Format**
**Tank Indentification and Physical Characteristics**

**Identification**

User Identification: Tk N°3
City: Santiago
State: Chile
Company:
Type of Tank: Horizontal Tank
Description: Contiene Xilol
**Tank Dimensions**
Shell Length (ft): 10,49
Diameter (ft): 6,56
Volume (gallons): 2.642,00
Turnovers: 12,00
Net Throughput(gal/yr): 31.704,00
Is Tank Heated (y/n): N
Is Tank Underground (y/n): Y
**Paint Characteristics**

Shell Color/Shade:

Shell Condition
**Breather Vent Settings**
Vacuum Settings (psig): -0,03
Pressure Settings (psig) 0,03
Meterological Data used in Emissions Calculations: Santiago, Chile (Avg Atmospheric Pressure = 13 psia)

**TANKS 4.0.9d**

**Emissions Report - Summary Format**

**Liquid Contents of Storage Tank**

**Tk N°3 - Horizontal Tank**
**Santiago, Chile**

Liquid

Daily Liquid Surf.
Temperature (deg F)

Bulk
Temp Vapor Pressure (psia)

Vapor

Liquid

Vapor

Temperature (deg F) Temp Vapor Pressure (psia) Mol. Mass Mass Mol. Basis

Mixture/Component Month Avg. Min. Max. (deg F) Avg. Min. Max. Weight. Fract. Fract. Weight Calcu

Mol.

Mass

Xylene (-o) All 52,80 52,80 52,80 52,36 0,0546 0,0546 0,0546 106,1700 106,17 Option

**Emissions Report for: Annual**

**Tk N°3 - Horizontal Tank**
**Santiago, Chile**

**TANKS 4.0.9d**

**Emissions Report - Summary Format**

**Individual Tank Emission Totals**

|Col1|Losses(lbs)|Col3|Col4|
|---|---|---|---|
|Components|Working Loss|Breathing Loss|Total Emissions|
|Xylene (-o)|4,38|0,00|4,38|

**TANKS 4.0.9d**

**Emissions Report - Summary Format**
**Tank Indentification and Physical Characteristics**

**Identification**

User Identification: Tk N°4
City: Santiago
State: Chile
Company:
Type of Tank: Horizontal Tank
Description: Contiene Acetato de etilo
**Tank Dimensions**
Shell Length (ft): 10,49
Diameter (ft): 6,56
Volume (gallons): 2.642,00
Turnovers: 12,00
Net Throughput(gal/yr): 31.704,00
Is Tank Heated (y/n): N
Is Tank Underground (y/n): Y
**Paint Characteristics**

Shell Color/Shade:

Shell Condition
**Breather Vent Settings**
Vacuum Settings (psig): -0,03
Pressure Settings (psig) 0,03
Meterological Data used in Emissions Calculations: Santiago, Chile (Avg Atmospheric Pressure = 13 psia)

**TANKS 4.0.9d**

**Emissions Report - Summary Format**

**Liquid Contents of Storage Tank**

**Tk N°4 - Horizontal Tank**
**Santiago, Chile**

Liquid

Daily Liquid Surf.
Temperature (deg F)

Bulk
Temp Vapor Pressure (psia)

Vapor

Liquid

Vapor

Temperature (deg F) Temp Vapor Pressure (psia) Mol. Mass Mass Mol. Basis f

Mixture/Component Month Avg. Min. Max. (deg F) Avg. Min. Max. Weight. Fract. Fract. Weight Calcul

Mol.

Mass

Ethyl acetate All 52,80 52,80 52,80 52,36 0,9146 0,9146 0,9146 88,1000 88,10 Option

**Emissions Report for: Annual**

**Tk N°4 - Horizontal Tank**
**Santiago, Chile**

**TANKS 4.0.9d**

**Emissions Report - Summary Format**

**Individual Tank Emission Totals**

|Col1|Losses(lbs)|Col3|Col4|
|---|---|---|---|
|Components|Working Loss|Breathing Loss|Total Emissions|
|Ethyl acetate|60,83|0,00|60,83|

**TANKS 4.0.9d**

**Emissions Report - Summary Format**
**Tank Indentification and Physical Characteristics**

**Identification**

User Identification: Tk N°5
City: Santiago
State: Chile
Company:
Type of Tank: Horizontal Tank
Description: Contiene Aguarras
**Tank Dimensions**
Shell Length (ft): 10,49
Diameter (ft): 6,56
Volume (gallons): 2.642,00
Turnovers: 12,00
Net Throughput(gal/yr): 31.704,00
Is Tank Heated (y/n): N
Is Tank Underground (y/n): Y
**Paint Characteristics**

Shell Color/Shade:

Shell Condition
**Breather Vent Settings**
Vacuum Settings (psig): -0,03
Pressure Settings (psig) 0,03
Meterological Data used in Emissions Calculations: Santiago, Chile (Avg Atmospheric Pressure = 13 psia)

**Emissions Report - Summary Format**

**Liquid Contents of Storage Tank**

**Tk N°5 - Horizontal Tank**
**Santiago, Chile**

Liquid

Daily Liquid Surf.
Temperature (deg F)

Bulk
Temp Vapor Pressure (psia)

Vapor

Liquid

Vapor

Temperature (deg F) Temp Vapor Pressure (psia) Mol. Mass Mass Mol. Basis

Mixture/Component Month Avg. Min. Max. (deg F) Avg. Min. Max. Weight. Fract. Fract. Weight Calcu

Mol.

Mass

Jet kerosene All 52,80 52,80 52,80 52,36 0,0067 0,0067 0,0067 130,0000 162,00 Option

**Emissions Report for: Annual**

**Tk N°5 - Horizontal Tank**
**Santiago, Chile**

**TANKS 4.0.9d**

**Emissions Report - Summary Format**

**Individual Tank Emission Totals**

|Col1|Losses(lbs)|Col3|Col4|
|---|---|---|---|
|Components|Working Loss|Breathing Loss|Total Emissions|
|Jet kerosene|0,66|0,00|0,66|

**TANKS 4.0.9d**

**Emissions Report - Summary Format**
**Tank Indentification and Physical Characteristics**

**Identification**

User Identification: Tk N°6
City: Santiago
State: Chile
Company:
Type of Tank: Vertical Fixed Roof Tank
Description: Contiene aguarrás
**Tank Dimensions**
Shell Height (ft): 20,99
Diameter (ft): 6,56
Liquid Height (ft) : 18,80
Avg. Liquid Height (ft): 18,80
Volume (gallons): 4.753,23
Turnovers: 12,00
Net Throughput(gal/yr): 57.038,73
Is Tank Heated (y/n): N
**Paint Characteristics**

Shell Color/Shade: White/White

Shell Condition Good

Roof Color/Shade: White/White

Roof Condition: Good

**Roof Characteristics**
Type: Dome
Height (ft) 0,98
Radius (ft) (Dome Roof) 6,56
**Breather Vent Settings**
Vacuum Settings (psig): -0,03
Pressure Settings (psig) 0,03
Meterological Data used in Emissions Calculations: Santiago, Chile (Avg Atmospheric Pressure = 13 psia)

**TANKS 4.0.9d**

**Emissions Report - Summary Format**

**Liquid Contents of Storage Tank**

**Tk N°6 - Vertical Fixed Roof Tank**
**Santiago, Chile**

Liquid

Daily Liquid Surf.
Temperature (deg F)

Bulk
Temp Vapor Pressure (psia)

Vapor

Liquid

Vapor

Temperature (deg F) Temp Vapor Pressure (psia) Mol. Mass Mass Mol. Basis

Mixture/Component Month Avg. Min. Max. (deg F) Avg. Min. Max. Weight. Fract. Fract. Weight Calcu

Mol.

Mass

Jet kerosene All 55,74 46,66 64,83 53,38 0,0074 0,0054 0,0097 130,0000 162,00 Option

**Emissions Report for: Annual**

**Tk N°6 - Vertical Fixed Roof Tank**
**Santiago, Chile**

**TANKS 4.0.9d**

**Emissions Report - Summary Format**

**Individual Tank Emission Totals**

|Col1|Losses(lbs)|Col3|Col4|
|---|---|---|---|
|Components|Working Loss|Breathing Loss|Total Emissions|
|Jet kerosene|1,31|0,39|1,70|

**TANKS 4.0.9d**

**Emissions Report - Summary Format**
**Tank Indentification and Physical Characteristics**

**Identification**

User Identification: Tk N°7
City: Santiago
State: Chile
Company:
Type of Tank: Vertical Fixed Roof Tank
Description: Contiene Metanol
**Tank Dimensions**
Shell Height (ft): 20,99
Diameter (ft): 6,56
Liquid Height (ft) : 18,80
Avg. Liquid Height (ft): 18,80
Volume (gallons): 4.753,23
Turnovers: 12,00
Net Throughput(gal/yr): 57.038,73
Is Tank Heated (y/n): N
**Paint Characteristics**

Shell Color/Shade: White/White

Shell Condition Good

Roof Color/Shade: White/White

Roof Condition: Good

**Roof Characteristics**
Type: Dome
Height (ft) 0,98
Radius (ft) (Dome Roof) 6,56
**Breather Vent Settings**
Vacuum Settings (psig): -0,03
Pressure Settings (psig) 0,03
Meterological Data used in Emissions Calculations: Santiago, Chile (Avg Atmospheric Pressure = 13 psia)

**TANKS 4.0.9d**

**Emissions Report - Summary Format**

**Liquid Contents of Storage Tank**

**Tk N°7 - Vertical Fixed Roof Tank**
**Santiago, Chile**

Liquid

Daily Liquid Surf.
Temperature (deg F)

Bulk
Temp Vapor Pressure (psia)

Vapor

Liquid

Vapor

Temperature (deg F) Temp Vapor Pressure (psia) Mol. Mass Mass Mol. Basis f

Mixture/Component Month Avg. Min. Max. (deg F) Avg. Min. Max. Weight. Fract. Fract. Weight Calcul

Mol.

Mass

Methyl alcohol All 55,74 46,66 64,83 53,38 1,2595 0,9350 1,6761 32,0400 32,04 Option

**Emissions Report for: Annual**

**Tk N°7 - Vertical Fixed Roof Tank**
**Santiago, Chile**

**TANKS 4.0.9d**

**Emissions Report - Summary Format**

**Individual Tank Emission Totals**

|Col1|Losses(lbs)|Col3|Col4|
|---|---|---|---|
|Components|Working Loss|Breathing Loss|Total Emissions|
|Methyl alcohol|54,80|25,71|80,51|

**TANKS 4.0.9d**

**Emissions Report - Summary Format**
**Tank Indentification and Physical Characteristics**

**Identification**

User Identification: Tk N°8
City: Santiago
State: Chile
Company:
Type of Tank: Vertical Fixed Roof Tank
Description: Contiene Xilol
**Tank Dimensions**
Shell Height (ft): 20,99
Diameter (ft): 6,56
Liquid Height (ft) : 18,80
Avg. Liquid Height (ft): 18,80
Volume (gallons): 4.753,23
Turnovers: 12,00
Net Throughput(gal/yr): 57.038,73
Is Tank Heated (y/n): N
**Paint Characteristics**

Shell Color/Shade: White/White

Shell Condition Good

Roof Color/Shade: White/White

Roof Condition: Good

**Roof Characteristics**
Type: Dome
Height (ft) 0,98
Radius (ft) (Dome Roof) 6,56
**Breather Vent Settings**
Vacuum Settings (psig): -0,03
Pressure Settings (psig) 0,03
Meterological Data used in Emissions Calculations: Santiago, Chile (Avg Atmospheric Pressure = 13 psia)

**TANKS 4.0.9d**

**Emissions Report - Summary Format**

**Liquid Contents of Storage Tank**

**Tk N°8 - Vertical Fixed Roof Tank**
**Santiago, Chile**

Liquid

Daily Liquid Surf.
Temperature (deg F)

Bulk
Temp Vapor Pressure (psia)

Vapor

Liquid

Vapor

Temperature (deg F) Temp Vapor Pressure (psia) Mol. Mass Mass Mol. Basis

Mixture/Component Month Avg. Min. Max. (deg F) Avg. Min. Max. Weight. Fract. Fract. Weight Calcu

Mol.

Mass

Xylene (-o) All 55,74 46,66 64,83 53,38 0,0609 0,0433 0,0843 106,1700 106,17 Option

**Emissions Report for: Annual**

**Tk N°8 - Vertical Fixed Roof Tank**
**Santiago, Chile**

**TANKS 4.0.9d**

**Emissions Report - Summary Format**

**Individual Tank Emission Totals**

|Col1|Losses(lbs)|Col3|Col4|
|---|---|---|---|
|Components|Working Loss|Breathing Loss|Total Emissions|
|Xylene (-o)|8,78|2,66|11,44|

## Estimación de pérdidas en estanques pequeños (dispersores)

Lg = [24/1.000]*[P/(14,7-P)]^0.68 * D^1.73 * H^0.51 * T^0.50 * Fp * C

Lg = Pérdidas por respiración (bbl/año)

P = Presión de vapor verdadera a la temperatura promedio del líquido (psi)

D = Diámetro del estanque (ft)

H = Altura de vapor incluyendo la altura equivalente al volumen de la parte cónica del estanque (ft)

parte cónica del estanque (ft)

T = Cambio diario promedio de temperatura ambiente (o F)

Fp = Factor de pintura

C = Factor de corrección por el tamaño del estanque, si este tiene un

diámetro menor de 30 ft.

L = (0,08M/W) * Lg

L = Pérdida del líquido (bbl/año)
Lg = Pérdida de gasolina
(bbl/año)
W = Densidad del líquido
(lb/galón)

M = Peso molecular del líquido

|Col1|BBL /año|P =<br>Presión<br>de<br>vapor|D = Diámetro<br>del estanque<br>(ft)|H =<br>Altura<br>de vapor<br>(ft).|T =Cambio diario<br>promedio de la<br>temperatura<br>ambiente (o F).|Fp = Factor<br>de pintura.|C= Factor de<br>corrección por el<br>tamaño del<br>estanque|
|---|---|---|---|---|---|---|---|
|Tk 9 <br>Dispersión <br> <br> <br>|Xileno|0,1015|3,93|3,28|59|0,6|0,5|
|Tk 9 <br>Dispersión <br> <br> <br>|0,04|BBL<br>/año||||||
|Tk 9 <br>Dispersión <br> <br> <br>|5,87|l/año||||||
|Tk 9 <br>Dispersión <br> <br> <br>|5,16|kg/año||||||
|Tk 9 <br>Dispersión <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|
|Tk 11 <br>Dispersión <br> <br> <br>|Aguarrás|0,7438|3,93|3,28|59|0,6|0,5|
|Tk 11 <br>Dispersión <br> <br> <br>|0,15|BBL<br>/año||||||
|Tk 11 <br>Dispersión <br> <br> <br>|23,44|l/año||||||
|Tk 11 <br>Dispersión <br> <br> <br>|17,49|kg/año||||||
|Tk 11 <br>Dispersión <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|<br> <br> <br> <br> <br> <br>|