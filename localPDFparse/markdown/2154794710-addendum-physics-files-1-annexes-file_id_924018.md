---
title: Sin título
author: Desconocido
date: Sin fecha
language: es
type: report
pages: 19
has_toc: False
has_tables: True
extraction_quality: high
---

### ADENDA Proyecto “Plan de Desarrollo Michilla”

#### Minera HMC S.A. [REVISIÓN 0]

**Preparado para:**

**Elaborado por**

Minería y Medio Ambiente Ltda.
Monseñor Sotero Sanz 100, Of. 505, Providencia, Santiago, RM.

Teléfono: (56-2) 2442188

[e-mail: jgalaz@myma.cl](mailto:jgalaz@myma.cl)

|ADENDA<br>DECLARACIÓN DE IMPACTO AMBIENTAL<br>Proyecto “Plan de Desarrollo Michilla”<br>Anexo 16: Antecedentes extractor de aire|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|
|---|---|---|---|---|---|---|---|---|
|0|24-02-2023|Revisión Cliente|Revisión Cliente|JVV|PA|PA|HMC/Eelaw|HMC/Eelaw|
|B|16-01-2023|Revisión Cliente|Revisión Cliente|JVV|PA|PA|||
|A|12-01-2022|Revisión Interna|Revisión Interna|JVV|PA||||
|**REV**|**FECHA**|**EMITIDO PARA**|**EMITIDO PARA**|**POR**|**J.Proy.**|**Aprobó**|**J.Proy**|**Aprobó**|
|||||**MYMA**|**MYMA**|**MYMA**|**CLIENTE**|**CLIENTE**|
|**CONSULTOR**<br>|**CONSULTOR**<br>|**CONSULTOR**<br>|**N° Documento**<br>**CODIGO MYMA**<br>**MY-03-2021a **|**N° Documento**<br>**CODIGO MYMA**<br>**MY-03-2021a **|**N° Documento**<br>**CODIGO MYMA**<br>**MY-03-2021a **|**N° Documento**<br>**CODIGO MYMA**<br>**MY-03-2021a **|**REV.**|**REV.**|
||||||||**0 **|**0 **|

|Col1|Nota Técnica Ventilación La<br>Reina Subterránea|Revisión: 0|
|---|---|---|
|<br>|<br>**Nota Técnica Ventilación La**<br>**Reina Subterránea**|Fecha: 02/2023 <br>|
|<br>|<br>**Nota Técnica Ventilación La**<br>**Reina Subterránea**|Página: 1 de 10|

**NOTA TÉCNICA**

**Ventilación La Reina Subterránea**

**NCL Ingeniería y Construcción SpA.**

**Febrero de 2023**

**ÍNDICE**

1 INTRODUCCIÓN ........................................................................................................... 4

2 OBJETIVO ...................................................................................................................... 4

3 NORMATIVA CHILENA VIGENTE A EXPLOTACIÓN Y VENTILACIÓN DE MINAS
SUBTERRÁNEAS .................................................................................................................. 4

4 VENTILACIÓN ................................................................................................................ 5

4.1 Estimación de Caudal ............................................................................................. 5

4.2 Circuito de Ventilación ............................................................................................ 6

4.3 Parámetros Ventsim ............................................................................................... 6

4.3.1 Ajustes de Entrada .......................................................................................... 6
4.3.2 Factor de Fricción ............................................................................................ 6

4.3.3 Factor de Choque ........................................................................................... 6

4.3.4 Eficiencia Ventiladores .................................................................................... 7

4.4 Simulación Ventsim ................................................................................................ 7

4.5 Respaldo ventilación. ............................................................................................ 10

5 ANEXOS ....................................................................................................................... 10

Ventilación La Reina Subterráneo
Nota Técnica

Página 2 de 10

NCL SpA.

**ÍNDICE DE TABLAS**

Tabla 4-1: Requerimiento de Aire ............................................................................................................................ 5
Tabla 4-2: Resultado Simulación ............................................................................................................................. 8

<!-- INICIO TABLA 4-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- NCL SpA. El resultado de la simulación se muestra en la Tabla 4-2. -->

**Tabla 4-2: Resultado Simulación****

| Col1 | Ventilador | Col3 |
| --- | --- | --- |
|  | **HP** | **in w.g** |
| Raise Borer | 890 | 8.6 |

<!-- Estadísticas: 2 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Como referencia el ventilador, que cumple con este requisito, es un Howden 12300-AMF8000, el cual tiene una potencia de motor de1,000 HP según catalogo la que se tiene que ajustar en caudal y caída de presión cuando se adquiera el equipo. En las siguientes figuras se puede ver la presión, eficiencia y potencia de este. -->
<!-- FIN TABLA 4-2 -->


**ÍNDICE DE FIGURAS**

Figura 4-1: Circuito de Ventilación ........................................................................................................................... 7
Figura 4-2: Howden 12300-AMF-8000, Presión vs Caudal ................................................................................... 8
Figura 4-3: Howden 12300-AMF-8000, Eficiencia vs Caudal ............................................................................... 9
Figura 4-4: Howden 12300-AMF-8000, Potencia vs Caudal ................................................................................. 9

Ventilación La Reina Subterráneo
Nota Técnica

Página 3 de 10

NCL SpA.

**1** **INTRODUCCIÓN**

Minera Michilla solicitó a NCL SpA llevar a cabo el estudio de la ventilación para el proyecto

minero “Ventilación La Reina subterráneo”. Este se efectuará mediante una simulación en

el software Ventsim, considerando la normativa chilena vigente.

**2** **OBJETIVO**

El objetivo de esta nota técnica, es determinar las características de los ventiladores
requeridos que serán utilizados para ventilar la mina durante las labores de explotación.

**3** **NORMATIVA CHILENA VIGENTE A EXPLOTACIÓN Y VENTILACIÓN DE MINAS**
**SUBTERRÁNEAS**

Se debe dar cumplimiento a la legislación vigente, en particular lo establecido en el
Reglamento de Seguridad Minera DS N°72, cuyas directrices principales son:

 Caudal de aire por maquinaria diésel: 2,83 m3/min por caballo de fuerza efectivo al

freno (Art. 32)

 Caudal de aire por persona que trabaja en el interior, ascendente a: 3 m3/min (Art.

138)

 Velocidad promedio mínima del aire de 15 m/min (Art. 138)

 Velocidad promedio máxima del aire de 150 m/min (Art. 138)

 Pérdidas máximas por filtraciones de aire de 15%

En términos generales y, en base a lo estipulado en este informe, el dimensionamiento del
sistema de ventilación del Proyecto Ventilación La Reina Subterráneo fue realizado en
conformidad con lo estipulado en la legislación chilena.

Ventilación La Reina Subterráneo
Nota Técnica

Página 4 de 10

NCL SpA.

**4** **VENTILACIÓN**

**4.1 Estimación de Caudal**

Considerando los equipos operativos y el número de personas se calcula el requerimiento
de caudal de aire. Dentro de la flota de equipos presentada, hay equipos que son
susceptibles de ser eliminados del cálculo, como, por ejemplo, los equipos
electrohidráulicos.

La Tabla 4-1, muestra el detalle del cálculo del requerimiento de aire por equipo diésel y
mano de obra, considerando un 13% adicional asociado a pérdidas de aire.

**Tabla 4-1: Requerimiento de Aire**

**RESUMEN** CFM

EQUIPOS DIESEL 428,700

MANO DE OBRA 5,300

SUB-TOTAL 434,000
PÉRDIDAS 13% 55,500

**CAUDAL TOTAL REQUERIDO** **489,500**

|EQUIPOS DIESEL|POTENCIA<br>(HP)|Col3|FACTOR|CANTIDAD|
|---|---|---|---|---|
|Camión Tolva<br>LHD<br>Equipo de Servicio y Utilitario<br>Shotcrete<br>Jumbo 2 Brazos<br>Jumbo Radial<br>Jumbo Apernador|400<br>295<br>101<br>128<br>58<br>58<br>60|400<br>295<br>101<br>128<br>58<br>58<br>60|100%<br>100%<br>100%<br>0%<br>0%<br>0%<br>0%|8 <br>3 <br>2 <br>2 <br>2 <br>2 <br>2|
|POTENCIA|<br>HP<br>|<br>HP<br>|<br>HP<br>|4,287|
|REQUERIMIENTO AIRE|<br>CFM/HP<br>|<br>CFM/HP<br>|<br>CFM/HP<br>|100|
|CAUDAL REQUERIDO|<br>CFM<br>|<br>CFM<br>|<br>CFM<br>|428,700|

Ventilación La Reina Subterráneo
Nota Técnica

Página 5 de 10

NCL SpA.

**4.2 Circuito de Ventilación**

Se considera un sistema de ventilación de extracción. El aire ingresará por la rampa de
acceso, recorrerá los niveles de producción y se evacuará mediante chimenea de
extracción, localizada cerca de la rampa.

El aire fresco ingresará desde la rampa a los distintos niveles activos mediante ventilación
forzada con dispositivos auxiliares y ductos de ventilación.

**4.3 Parámetros Ventsim**

**4.3.1 Ajustes de Entrada**

 - Ventilación natural activada

 Flujo compresible activado

 Superficie de elevación sobre el nivel del mar: 907 metros

 Densidad del aire flujo compresible: 1.04 kg/m [3]

**4.3.2 Factor de Fricción**

Los factores de fricción usados para cada sección son estándares del software Ventsim.

 Chimenea Raise Borer: 27.0 kx10^10 (RaiseBored Airway)

 Chimenea VCR: 107.8 kx10^10(VCR Airway)

 Rampa: 64.7 kx10^10 (Average Blasted)

**4.3.3 Factor de Choque**

Los factores de choque utilizados son en base a un criterio experto.

 - Chimenea: Auto Mid.

 - VCR: Auto Mid.

 Rampa: Auto Mid.

Ventilación La Reina Subterráneo
Nota Técnica

Página 6 de 10

NCL SpA.

**4.3.4 Eficiencia Ventiladores**

La eficiencia de los ventiladores usada en la simulación es de 80%.

**4.4 Simulación Ventsim**

Se realiza una simulación en el software Ventsim, con el fin de determinar la potencia del
ventilador a instalar.

La Figura 4-1, muestra el detalle del circuito principal que muestra que el aire ingresará por
la rampa a los niveles de explotación y será evacuado por la chimenea de extracción
principal.

**Figura 4-1: Circuito de Ventilación**

Ventilación La Reina Subterráneo
Nota Técnica

Página 7 de 10

NCL SpA.

El resultado de la simulación se muestra en la Tabla 4-2.

**Tabla 4-2: Resultado Simulación**

|Col1|Ventilador|Col3|
|---|---|---|
||**HP**|**in w.g**|
|Raise Borer|890|8.6|

Como referencia el ventilador, que cumple con este requisito, es un Howden 12300-AMF8000, el cual tiene una potencia de motor de1,000 HP según catalogo la que se tiene que
ajustar en caudal y caída de presión cuando se adquiera el equipo.

En las siguientes figuras se puede ver la presión, eficiencia y potencia de este.

**Figura 4-2: Howden 12300-AMF-8000, Presión vs Caudal**

Ventilación La Reina Subterráneo
Nota Técnica

Página 8 de 10

NCL SpA.

**Figura 4-3: Howden 12300-AMF-8000, Eficiencia vs Caudal**

**Figura 4-4: Howden 12300-AMF-8000, Potencia vs Caudal**

Ventilación La Reina Subterráneo
Nota Técnica

Página 9 de 10

NCL SpA.

**4.5 Respaldo ventilación.**

Para respaldar el sistema de ventilación principal se considera repartir el caudal requerido
en dos ventiladores principales de iguales características. Frente a la falla de uno de ellos,
el sistema de ventilación operará a una capacidad menor por lo que se reducirán las
actividades en interior mina de acuerdo con la disponibilidad de aire fresco en tanto se
recupera el ventilador en falla. Se podría disponer en faena de un motor eléctrico de
repuesto para esos ventiladores de manera de reducir el plazo de reposición.

**5** **ANEXOS**

 Especificación Técnica con un Ventilador

 Requerimiento Aire La Reina.xlsx

 - Ventsim La Reina.vsm

 Especificación Técnica con dos Ventiladores

Ventilación La Reina Subterráneo
Nota Técnica

Página 10 de 10

NCL SpA.

**Customer:** **Our Reference:**

**Site:** **Reference:**
**Application: Fan Application** **Date: Oct 7 2022**

#### Fan Curves - 12300-AMF-8000

**12300-AMF-8000 Individual Fan Curves**

**Fan:** 12300-AMF-8000 **Tag:** **Speed:** 710 RPM
**Blade Type:** Full **Stages:** 1 **Blade Angle:** 33.4 °
**Power:** 722.3 kW **Flow:** 231.0 m3/s **Pressure** **(TP):** 2,596 Pa
**Density:** 1.006 kg/m3 **Inlet Temperature:** 25 °C **Elevation:** 1050 m

**Customer:** **Our Reference:**

**Site:** **Reference:**
**Application: Fan Application** **Date: Oct 7 2022**

**12300-AMF-8000 Speed - Torque Curves**
**Fan:** 12300-AMF-8000 **Tag:** **Speed:** 710 RPM
**Temperature:** 25.0 °C **Density:** 1.006 kg/m3 **Torque:** 7,165 N·m
**Temperature** **(Start):** 0.0 °C **Density** **(Start):** 1.107 kg/m3 **Torque** **(Start):** 10,390 N·m

**Customer:** **Our Reference:**

**Site:** **Reference:**
**Application: Fan Application** **Date: Oct 7 2022**

#### Fan Data - 12300-AMF-8000

**Site Condition**

**Fan:** 12300-AMF-8000 **Elevation:** 1050 m **Barometer:** 0.09 MPa

**Min. Ambient Temp.:** 0 °C **Power:** 722.3 kW
**Fan Data**

**Fan Type:** AMF **Impeller Diameter:** 3.124 m **Hub Diameter:** 2.048 m
**Blades(Qty):** 16 **Blade** **Speed:** 116.1 m/s **Max. Tip** **Speed:** 152.4 m/s
**Blade Type:** Full **Blade Angle:** 33.4 **Blade Angle** **Setting:** 0.0
**System Data**
**Inlet Temperature:** 25 °C **Outlet Temperature:** 28.1 °C **Temperature Rise:** 3.1 °C
**Density In:** 1.006 kg/m3 **Density** **Out:** 1.035 kg/m3 **Density** **STP:** 1.201 kg/m3
**Actual Flow:** 231.0 m3/s **STP Flow:** 257.1 m3/s **Mass Flow:** 232.38 kg/s
**System Inlet Velocity:** 15.4 m/s **System Outlet Velocity:** 17.4 m/s
**System In SP:** -2,559 Pa **System In Vp:** 119 Pa **System In TP:** -2,440 Pa
**System Out** **SP:** 0 Pa **System Out VP:** 0 Pa **System Out TP:** 156 Pa
**Fan Inlet Velocity:** 15.4 m/s **Fan Outlet Velocity:** 30.1 m/s **Diffuser Outlet Velocity:** 17.4 m/s
**Speed:** 710 **Fan Power:** 722.3 kW **Efficiency** **(TP):** 85 %
**Diffuser:** Yes **Inlet** **Connection:** Open **Outlet** **Connection:** Open
**Frequency:** 60 Hz. **Motor:** 1000 HP 720 RPM CUSTOM MOTOR
**Pressure Losses**

**Losses Total:** 230.73909 Pa **User Add Inlet:** 0 Pa **User Add** **Outlet:** 0 Pa

**Backdraft Damper:** 0 Pa **Belt Drive:** 0 Pa **Exit:** 156.182164 Pa
**Diffuser:** 74.556926 Pa **Inlet Box:** 0 Pa **Inlet** **Screen:** 0 Pa

**Loss** **Outlet** **Screen:** 0 Pa **Loss** **Silencer In:** 0 Pa **Loss** **Silencer Out:** 0 Pa

**Customer:** **Our Reference:**

**Site:** **Reference:**
**Application: Fan Application** **Date: Oct 7 2022**

Fan Data - 12300-AMF-8000 (continued)

**Sound Data**

**Frequency Band** **(Hz.):** 63 125 250 500 1000 2000 4000 8000
**Lw:** 116 113 121 116 114 111 109 105

**End Reflection:** -2 -1 0 0 0 0 0 0

**Lp:** 106 104 113 108 106 103 101 97
**LpA:** 80 88 104 105 106 104 102 96
**Free field** **overall LpA 112 dBA at** **3.2 ft. / 1 m. from the fan.**

**Fan Accessories**

**Inlet** **Screen:** No **Outlet** **Screen:** No **Diffuser:** Yes

**Backdraft Damper:** No **Inlet** **Silencer:** No **Outlet** **Silencer:** No

**System Loads**
Description: **Design**
Is Valid:

Inlet Temperature: 25 °C
Humidity: 70.0 %
Density In: 1.006 kg/m3
Actual Flow Rate: 231 m3/s

Mass Flow: 232.4 kg/s
Inlet Velocity: 15.4 m/s
Outlet Velocity: 17.4 m/s
System In SP: -2559 Pa
System In TP: -2440 Pa
System Out SP: 0 Pa
System Out TP: 156 Pa
Losses Total: 231 Pa

Blade Angle: 33.4 °
Speed: 710 RPM
Power: 722.3 kW

Efficiency (TP): 84.6 %

**Cliente**

**Proyecto** :

#### 1.2. Curva del ventilador

Referencia Howden: Fecha: 20-02-2023 3