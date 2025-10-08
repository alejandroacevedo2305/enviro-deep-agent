---
title: about:blank
author: Pablo Machuca
date: D:20171205171717-03'00'
language: en
type: report
pages: 9
has_toc: False
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - DETAILED OUTPUT PC06 ETAPA 2
-->

Detailed Output Page 1 of 9

# DETAILED OUTPUT PC06 ETAPA 2

PC 06 Ruta C-468 - Sitio Las Losas
Stop (Two-Way)

**OUTPUT TABLE LINKS**

Movements

Movement Capacity Parameters
Movement Performance
Fuel Consumption, Emissions and Cost (Total)
Fuel Consumption, Emissions and Cost (Rate)
Intersection Negotiation Data
Movement Speeds and Geometric Delay
Gap Acceptance Parameters

Lanes

Lane Performance
Lane Flow and Capacity Information
Lane, Approach and Intersection Performance
Driver Characteristics
Lane Delays
Lane Queues (Vehicles)
Lane Queues (Distance)
Lane Queue Percentiles (Vehicles)
Lane Queue Percentiles (Distance)
Lane Stops

Flow Rates and Demand Analysis

Movement Definitions and Flow Rates (O-D)
Flow Rates (Separate Light and Heavy Vehicles)
Flow Rates (Total Vehicles and Percent Heavy)

Other

Model Settings
Parameters Used in Cost Calculations
Diagnostics

**Movements**

Movement Capacity Parameters
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 ------------------------------------------------------------------------
Mov Opposing Movement Total Prac. Prac. Lane Deg.
ID Demand Adjust. Cap. Deg. Spare Util Satn
Flow HV Flow HV Flow Satn Cap.
veh/h % veh/h % pcu/h veh/h xp % % x

 ------------------------------------------------------------------------
NorthEast: Ruta C-468

25 T 445 14.2 0 1632 0.80 193 100 0.273*

26 R 3 66.7 0 12 0.80 193 100 0.273*

 ------------------------------------------------------------------------
NorthWest: Sitio Las Losas

27 L 1 0.0 555+ 14.6 609 71 0.80 5317 100 0.015

29 R 3 66.7 447+ 14.4 489 214 0.80 5317 100 0.015

 ------------------------------------------------------------------------
SouthWest: Ruta C-468

30 L 3 66.7 450+ 14.7 494 37 0.80 841 100 0.085

31 T 105 14.0 0 1239 0.80 841 100 0.085

 ------------------------------------------------------------------------
* Maximum degree of saturation
+ Percentage of exiting flow included in total opposing flow

```

Go to Table Links (Top)

about:blank 05-12-2017

Detailed Output Page 2 of 9

Movement Performance

Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 --------------------------------------------------------------------------------
Mov Total Total Aver. Eff. Total Perf. Tot.Trav. Tot.Trav. Aver.

ID Delay Delay Delay Stop Stops Index Distance Time Speed
(veh-h/h)(pers-h/h)(sec) Rate (veh-km/h)(veh-h/h) (km/h)

 --------------------------------------------------------------------------------
NorthEast: Ruta C-468

25 T 0.00 0.00 0.0 0.00 0.0 4.50 270.0 4.5 60.0

26 R 0.01 0.01 10.6 1.23 3.9 0.06 1.9 0.0 49.0

 --------------------------------------------------------------------------------
 NorthWest: Sitio Las Losas

27 L 0.01 0.01 19.9 0.92 1.0 0.03 0.6 0.0 39.6

29 R 0.02 0.03 24.1 0.91 2.9 0.08 1.9 0.0 39.5

 --------------------------------------------------------------------------------
SouthWest: Ruta C-468

30 L 0.03 0.04 35.5 1.01 3.2 0.11 1.9 0.1 33.6

31 T 0.71 0.86 24.4 0.00 0.0 2.80 63.8 1.9 33.9

 --------------------------------------------------------------------------------
```

Go to Table Links (Top)

Fuel Consumption, Emissions and Cost (Total)
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 -------------------------------------------------------------
Mov Cost Fuel CO2 CO HC NOX

ID Total Total Total Total Total Total

$/h L/h kg/h kg/h kg/h kg/h

 -------------------------------------------------------------
NorthEast: Ruta C-468

25 T 165.15 25.4 63.9 1.44 0.068 0.087

26 R 2.32 0.6 1.6 0.14 0.002 0.004

 ----------------------------------------------
167.47 26.0 65.5 1.57 0.070 0.091

 -------------------------------------------------------------
NorthWest: Sitio Las Losas

27 L 0.55 0.1 0.2 0.02 0.000 0.000

29 R 2.70 0.7 1.7 0.15 0.002 0.005

 ----------------------------------------------
3.25 0.8 1.9 0.17 0.002 0.005

 -------------------------------------------------------------
SouthWest: Ruta C-468

30 L 3.03 0.7 1.8 0.15 0.002 0.005

31 T 68.08 10.9 27.4 2.13 0.041 0.066

 ----------------------------------------------
71.11 11.6 29.2 2.28 0.043 0.071

 -------------------------------------------------------------
INTERSECTION: 241.84 38.4 96.6 4.02 0.115 0.167

 -------------------------------------------------------------
```

Go to Table Links (Top)

Fuel Consumption, Emissions and Cost (Rate)
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 -------------------------------------------------------------
Mov Cost Fuel CO2 CO HC NOX

ID Rate Rate Rate Rate Rate Rate

$/km L/100km g/km g/km g/km g/km

 -------------------------------------------------------------
NorthEast: Ruta C-468

25 T 0.61 9.4 236.6 5.32 0.253 0.322

26 R 1.22 32.6 836.9 71.55 0.966 2.208

 ----------------------------------------------
0.62 9.6 240.9 5.78 0.258 0.335

 -------------------------------------------------------------
NorthWest: Sitio Las Losas

```

about:blank 05-12-2017

Detailed Output Page 3 of 9

```
 27 L 0.88 12.2 304.6 25.03 0.542 0.720

 29 R 1.41 35.5 910.7 79.38 1.089 2.434

 ----------------------------------------------
 1.28 29.7 759.9 65.86 0.953 2.008

 -------------------------------------------------------------
 SouthWest: Ruta C-468

 30 L 1.60 36.5 937.0 77.43 1.104 2.436

 31 T 1.07 17.1 429.2 33.43 0.638 1.041

 ----------------------------------------------
 1.08 17.6 443.8 34.70 0.651 1.081

 -------------------------------------------------------------
 INTERSECTION: 0.71 11.3 284.0 11.82 0.339 0.492

 -------------------------------------------------------------
```

Go to Table Links (Top)

Intersection Negotiation Data
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 ----------------------------------------------------------------------------
Negn Negn Negn Appr. Downstream Distance
From To Radius Speed Dist. Dist. -------------------Approach Approach Turn m km/h m m m User Spec?

 ----------------------------------------------------------------------------
NorthEast: Ruta C-468

NorthWest Right 10.0 20.2 15.7 500 98 No
SouthWest Thru S 60.0 10.1 500 176 No

 ----------------------------------------------------------------------------
NorthWest: Sitio Las Losas

NorthEast Left 6.7 17.3 10.5 500 100 No

SouthWest Right 10.0 20.2 15.7 500 160 No

 ----------------------------------------------------------------------------
SouthWest: Ruta C-468

NorthEast Thru S 60.0 10.1 500 178 No

NorthWest Left 6.7 17.3 10.5 500 95 No

 ----------------------------------------------------------------------------
Downstream distance is distance travelled from the stopline until exit
cruise speed is reached (includes negotiation distance). Acceleration
distance is weighted for light and heavy vehicles. The same distance
applies for both stopped and unstopped vehicles.

```

Go to Table Links (Top)

Movement Speeds and Geometric Delay
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 ---------------------------------------------------------------------------
Queue Move-up
App. Speeds Exit Speeds ------------- Av. Section Spd Geom
Mov ------------ ----------- 1st 2nd --------------- Delay
ID Cruise Negn Negn Cruise Grn Grn Running Overall sec

 ---------------------------------------------------------------------------
NorthEast: Ruta C-468

25 T 60.0 60.0 60.0 60.0 60.0 60.0 0.0

26 R 60.0 20.2 20.2 60.0 49.0 49.0 10.6

 ---------------------------------------------------------------------------
NorthWest: Sitio Las Losas

27 L 60.0 0.0 17.3 60.0 46.7 39.6 10.5

29 R 60.0 0.0 20.2 60.0 46.3 39.5 14.6

 ---------------------------------------------------------------------------
SouthWest: Ruta C-468

30 L 60.0 17.3 17.3 60.0 50.0 33.6 11.1

31 T 60.0 60.0 60.0 60.0 45.3 33.9 0.0

 ---------------------------------------------------------------------------
"Running Speed" is the average speed excluding stopped periods.

```

Go to Table Links (Top)

Gap Acceptance Parameters
Site:PC06 ETAPA 2

about:blank 05-12-2017

Detailed Output Page 4 of 9

```
Intersection ID: 6

Stop Sign Controlled Intersection

 ------------------------------------------------------------------------
Critical Gap Intra
Opng ------------ Foll-up Entry Bunch Propn
Mov Mov Flow Hdwy Dist Headway HV Hdwy Bnchd
ID Type pcu/h sec m sec Equiv sec

 ------------------------------------------------------------------------
NorthEast: Ruta C-468

No opposed movements on this approach.

 ------------------------------------------------------------------------
NorthWest: Sitio Las Losas

27 L Normal 609+ 7.00 115.8 4.00 2.00 0.90 0.035

29 R Normal 489+ 8.08 134.1 4.85 2.00 1.80 0.061

 ------------------------------------------------------------------------
SouthWest: Ruta C-468

30 L Normal 494+ 11.32 186.9 6.47 2.00 0.90 0.027

 ------------------------------------------------------------------------
Values in this table are adjusted for heavy vehicles in the entry stream.
+ Percentage of exiting flow included in total opposing flow

```

Go to Table Links (Top)

**Lanes**

Lane Performance

Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 -------------------------------------------------------------
Q u e u e
Flow Cap Deg. Aver. Eff. 95% Back Lane
Lane Satn Delay Stop ------------ Length
No. veh/h veh/h x sec Rate veh m m

 -------------------------------------------------------------
NorthEast: Ruta C-468

1 TR 448 1643 0.273 0.1 0.01 0.0 0.0 500.0

 -------------------------------------------------------------
NorthWest: Sitio Las Losas

1 LR 4 285 0.015 23.0 0.92 0.0 0.5 500.0

 -------------------------------------------------------------
SouthWest: Ruta C-468

1 LT 108 1276 0.085 24.7 0.03 2.6 20.8 500.0

 -------------------------------------------------------------
```

Go to Table Links (Top)

Lane Flow and Capacity Information
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 ---------------------------------------------------
Lane Dem Flow (veh/h) Min Tot Deg. Lane
No. ------------------- Cap Cap Satn Util
Lef Thru Rig Tot veh/h veh/h x %

 ---------------------------------------------------
NorthEast: Ruta C-468

1 TR 0 445 3 448 448 1643 0.273 100

 ---------------------------------------------------
NorthWest: Sitio Las Losas

1 LR 1 0 3 4 4 285 0.015 100

 ---------------------------------------------------
SouthWest: Ruta C-468

1 LT 3 105 0 108 108 1276 0.085 100

 ---------------------------------------------------
The capacity value for priority and continuous movements is obtained by
adjusting the basic saturation flow for heavy vehicle and turning vehicle
effects. Saturation flow scale applies if specified.

```

about:blank 05-12-2017

Detailed Output Page 5 of 9

Go to Table Links (Top)

Lane, Approach and Intersection Performance
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 -------------------------------------------------------------------------
Lane Demand Flow (veh/h) Adj. Eff Grn Deg Aver. Longest Shrt
No. -------------------- %HV Basic (sec) Sat Delay Queue Lane
L T R Tot Satf. 1st 2nd x sec m m

 -------------------------------------------------------------------------
NorthEast: Ruta C-468

1 TR 445 3 448 15 0.273 0.1 0 500

 -----------------------------------------------------------------
0 445 3 448 15 0.273 0.1

 -------------------------------------------------------------------------
NorthWest: Sitio Las Losas

1 LR 1 3 4 50 0.015 23.0 0 500

 -----------------------------------------------------------------
1 0 3 4 50 0.015 23.0 0

 -------------------------------------------------------------------------
SouthWest: Ruta C-468

1 LT 3 105 108 16 0.085 24.7 21 500

 -----------------------------------------------------------------
3 105 0 108 16 0.085 24.7 21

==========================================================================

ALL VEHICLES Total % Max Aver. Max

Flow HV X Delay Queue
561 15 0.273 5.0 21

==========================================================================

Peak flow period = 30 minutes.

Queue values in this table are 95% queue (metres)
Note: Basic Saturation Flows are not adjusted at roundabouts or signcontrolled intersections and apply only to continuous lanes.

```

Go to Table Links (Top)

Driver Characteristics

Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 -------------------------------------------------------
Average Driver
Lane Satn Satn Satn Satn Queue Response
No. Speed Flow Hdwy Spacing Space Time
km/h veh/h sec m m sec

 -------------------------------------------------------
NorthEast: Ruta C-468

1 TR NA - Major Road Movement

 -------------------------------------------------------
NorthWest: Sitio Las Losas

1 LR 19.5 776 4.64 25.06 10.00 2.79

 -------------------------------------------------------
SouthWest: Ruta C-468

1 LT NA - Major Road Movement

 -------------------------------------------------------
Saturation Flow and Saturation Headway are derived from follow-up headway.

```

Go to Table Links (Top)

Lane Delays
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 ---------------------------------------------------------------------
 -------------- Delay (seconds/veh) ---------------Deg. Stop-line Delay Acc. Queuing Stopd
Lane Satn 1st 2nd Total Dec. Total MvUp (Idle) Geom Control

```

about:blank 05-12-2017

Detailed Output Page 6 of 9

```
 No. x d1 d2 dSL dn dq dqm di dig dic

 ---------------------------------------------------------------------
 NorthEast: Ruta C-468

 1 TR 0.273 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.1 0.1

 ---------------------------------------------------------------------
 NorthWest: Sitio Las Losas

 1 LR 0.015 9.4 0.0 9.4 1.3 8.2 0.0 8.2 13.6 23.0

 ---------------------------------------------------------------------
 SouthWest: Ruta C-468

 1 LT 0.085 24.4 0.0 24.4 8.1 16.2 0.0 16.2 0.3 24.7

 ---------------------------------------------------------------------
 dSL: Stop-line delay (=d1+d2)
 dn: Average stop-start delay for all vehicles queued and unqueued
 dq: Queuing delay (the part of the stop-line delay that includes
 stopped delay and queue move-up delay)
 dqm: Queue move-up delay
 di: Stopped delay (stopped (idling) time at near-zero speed)
 dig: Geometric delay
 dic: Intersection control delay (sum of stop-line and geometric delays)

```

Go to Table Links (Top)

Lane Queues (Vehicles)
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 -----------------------------------------------------------------------------------
Deg. Ovrfl. Back of Queue (veh) Queue Prob. P'ile Cyc-Av. Queue
Lane Satn Queue --------------------------- Stor. Block Block ------------
No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 -----------------------------------------------------------------------------------
NorthEast: Ruta C-468

1 TR 0.273 0.0 0.0 0.0 0.0 0.0 0.00 0.0 100.0 0.0 0.0

 -----------------------------------------------------------------------------------
NorthWest: Sitio Las Losas

1 LR 0.015 0.0 0.0 0.0 0.0 0.0 0.00 0.0 100.0 0.0 0.0

 -----------------------------------------------------------------------------------
SouthWest: Ruta C-468

1 LT 0.085 0.0 1.1 0.0 1.1 2.6 0.04 0.0 100.0 0.7 1.3

 -----------------------------------------------------------------------------------
```

Go to Table Links (Top)

Lane Queues (Distance)
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 -----------------------------------------------------------------------------------
Deg. Ovrfl. Back of Queue (m) Queue Prob. P'ile Cyc-Av. Queue
Lane Satn Queue --------------------------- Stor. Block Block ------------
No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 -----------------------------------------------------------------------------------
NorthEast: Ruta C-468

1 TR 0.273 0.0 0.0 0.0 0.0 0.0 0.00 0.0 100.0 0.0 0.0

 -----------------------------------------------------------------------------------
NorthWest: Sitio Las Losas

1 LR 0.015 0.0 0.2 0.0 0.2 0.5 0.00 0.0 100.0 0.1 0.2

 -----------------------------------------------------------------------------------
SouthWest: Ruta C-468

1 LT 0.085 0.0 8.4 0.0 8.4 20.8 0.04 0.0 100.0 5.8 10.6

 -----------------------------------------------------------------------------------
```

Go to Table Links (Top)

Lane Queue Percentiles (Vehicles)
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 ------------------------------------------------------
```

about:blank 05-12-2017

Detailed Output Page 7 of 9

```
 Deg. Percentile Back of Queue (veh)

 Lane Satn ---------------------------------------
 No. x 50% 70% 85% 90% 95% 98%

 ------------------------------------------------------
 NorthEast: Ruta C-468

 1 TR 0.273 0.0 0.0 0.0 0.0 0.0 0.0

 ------------------------------------------------------
 NorthWest: Sitio Las Losas

 1 LR 0.015 0.0 0.0 0.0 0.0 0.0 0.1

 ------------------------------------------------------
 SouthWest: Ruta C-468

 1 LT 0.085 1.1 1.4 1.9 2.2 2.6 2.9

 ------------------------------------------------------
```

Go to Table Links (Top)

Lane Queue Percentiles (Distance)
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 ------------------------------------------------------
Deg. Percentile Back of Queue (metres)

Lane Satn ---------------------------------------
No. x 50% 70% 85% 90% 95% 98%

 ------------------------------------------------------
NorthEast: Ruta C-468

1 TR 0.273 0.0 0.0 0.0 0.0 0.0 0.0

 ------------------------------------------------------
NorthWest: Sitio Las Losas

1 LR 0.015 0.2 0.3 0.4 0.4 0.5 0.5

 ------------------------------------------------------
SouthWest: Ruta C-468

1 LT 0.085 8.3 10.8 15.2 17.7 20.8 23.0

 ------------------------------------------------------
```

Go to Table Links (Top)

Lane Stops
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 ---------------------------------------------------------------------
Queue Total
Deg. -- Effective Stop Rate -- Total Move-up Queue Prop.
Lane Satn Geom. Overall Stops Rate Move-ups Queued
No. x he1 he2 hig h H hqm Hqm pq

 ---------------------------------------------------------------------
NorthEast: Ruta C-468

1 TR 0.273 0.00 0.00 0.01 0.01 3.9 0.00 0.0 0.00

 ---------------------------------------------------------------------
NorthWest: Sitio Las Losas

1 LR 0.015 0.55 0.00 0.36 0.92 3.9 0.00 0.0 0.64

 ---------------------------------------------------------------------
SouthWest: Ruta C-468

1 LT 0.085 0.03 0.00 0.00 0.03 3.2 0.00 0.0 0.97

 ---------------------------------------------------------------------
hig is the average value for all movements in a shared lane
hqm is average queue move-up rate for all vehicles queued and unqueued

```

Go to Table Links (Top)

**Flow Rates and Demand Analysis**

Movement Definitions and Flow Rates (O-D)
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

```

about:blank 05-12-2017

Detailed Output Page 8 of 9

```
 ----------------------------------------------------------------------
 From To Mov Flow Rate Flow Scale Peak Flow

 Approach Approach ID Turn LV HV Fixed Var Factor

 ----------------------------------------------------------------------
 NorthEast: Ruta C-468

 NorthWest 26 Right 1 2 1.00 1.00 0.95
 SouthWest 25 Thru 382 63 1.00 1.00 0.95

 ----------------------------------------------------------------------
 NorthWest: Sitio Las Losas

 NorthEast 27 Left 1 0 1.00 1.00 0.95

 SouthWest 29 Right 1 2 1.00 1.00 0.95

 ----------------------------------------------------------------------
 SouthWest: Ruta C-468

 NorthEast 31 Thru 91 15 1.00 1.00 0.95

 NorthWest 30 Left 1 2 1.00 1.00 0.95

 ----------------------------------------------------------------------
 Unit Time for Volumes = 60 minutes

 Peak Flow Period = 30 minutes

 Flow Rates include effects of Flow Scale and Peak Flow Factor

```

Go to Table Links (Top)

Flow Rates (Separate Light and Heavy Vehicles)
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 ----------------------------------------------
Mov Left Through Right

ID --------- --------- --------
LV HV LV HV LV HV

 ----------------------------------------------
Demand flows in veh/h as used by the program
NorthEast: Ruta C-468

25 T 0 0 382 63 0 0

26 R 0 0 0 0 1 2

 ----------------------------------------------
NorthWest: Sitio Las Losas

27 L 1 0 0 0 0 0

29 R 0 0 0 0 1 2

 ----------------------------------------------
SouthWest: Ruta C-468

30 L 1 2 0 0 0 0

31 T 0 0 91 15 0 0

 ----------------------------------------------
Unit Time for Volumes = 60 minutes

Peak Flow Period = 30 minutes

Flow Rates include effects of Flow Scale and Peak Flow Factor

```

Go to Table Links (Top)

Flow Rates (Total Vehicles and Percent Heavy)
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

 -------------------------------------------------
Mov Left Through Right

ID ---------- ---------- ---------
Total %HV Total %HV Total %HV

 -------------------------------------------------
Demand flows in veh/h as used by the program
NorthEast: Ruta C-468

25 T 0 0.0 445 14.2 0 0.0

26 R 0 0.0 0 0.0 3 66.7

 -------------------------------------------------
NorthWest: Sitio Las Losas

27 L 1 0.0 0 0.0 0 0.0

29 R 0 0.0 0 0.0 3 66.7

 -------------------------------------------------
SouthWest: Ruta C-468

30 L 3 66.7 0 0.0 0 0.0

31 T 0 0.0 105 14.0 0 0.0

 -------------------------------------------------
Unit Time for Volumes = 60 minutes

```

about:blank 05-12-2017

Detailed Output Page 9 of 9

```
 Peak Flow Period = 30 minutes

 Flow Rates include effects of Flow Scale and Peak Flow Factor

```

Go to Table Links (Top)

**Other**

Model Settings
Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

* Basic Parameters:

Intersection Type: Unsignalised - Two-Way Stop Control
Driving on the right-hand side of the road
Input data specified in Metric units
Model Defaults: Standard Right - Copy - Copy
Peak Flow Period (for performance): 30 minutes
Unit time (for volumes): 60 minutes.
SIDRA Standard Delay model used
SIDRA Standard Queue model used
Level of Service based on: Delay (HCM 2000)
Queue percentile: 95%

```

Go to Table Links (Top)

Parameters Used in Cost Calculations

Site:PC06 ETAPA 2

```
Intersection ID: 6

Stop Sign Controlled Intersection

Pump price of fuel ($/L) = 1.300
Fuel resource cost factor = 0.50

Ratio of running cost to fuel cost = 3.0
Average income ($/h) = 35.00
Time value factor = 0.60

Light vehicle mass (1000 kg) = 1.4
Heavy vehicle mass (1000 kg) = 11.0
Light vehicle idle fuel rate (L/h) = 1.350
Heavy vehicle idle fuel rate (L/h) = 2.000

```

Go to Table Links (Top)

Diagnostics
Site:PC06 ETAPA 2

Go to Table Links (Top)

Processed: martes, 5 de diciembre de 2017 16:11:05 Copyright © 2000-2011 Akcelik and Associates Pty Ltd
SIDRA INTERSECTION 5.1.12.2089 www.sidrasolutions.com

Project: C:\Users\Pablo Machuca\Documents\10 PROYECTOS VIGENTES\150 GUACOLDA\04 INFORME R02
\APENDICE B MODELACION\GUACOLDA.sip
Licensed to JUNLAJUBALAM

about:blank 05-12-2017