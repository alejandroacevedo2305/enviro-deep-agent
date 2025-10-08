---
title: about:blank
author: Jorge Gutierrez Ronda
date: D:20250709211619-04'00'
language: en
type: general
pages: 9
has_toc: False
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - DETAILED OUTPUT PMD-L
-->

Detailed Output Page 1 of 9

# DETAILED OUTPUT PMD-L

Ruta H-111 / C-1

PMDL
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
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 ------------------------------------------------------------------------
Mov Opposing Movement Total Prac. Prac. Lane Deg.
ID Demand Adjust. Cap. Deg. Spare Util Satn
Flow HV Flow HV Flow Satn Cap.
veh/h % veh/h % pcu/h veh/h xp % % x

 ------------------------------------------------------------------------
East: Ruta H-111 OTE

5 T 127 14.9 0 1603 0.80 907 100 0.079

6 R 3 0.0 0 40 0.80 907 100 0.079

 ------------------------------------------------------------------------
North: C-1

7 L 2 50.0 292 14.4 319 76 0.80 2800 100 0.028

9 R 19 55.6 127 14.9 140 687 0.80 2800 100 0.028

 ------------------------------------------------------------------------
West: Ruta H-111 PTE

10 L 20 47.4 140+ 17.3 157 455 0.80 1721 100 0.044

11 T 144 9.5 0 1695 0.80 841 100 0.085*

 ------------------------------------------------------------------------
* Maximum degree of saturation
+ Percentage of exiting flow included in total opposing flow

```

Go to Table Links (Top)

about:blank 09/07/2025

Detailed Output Page 2 of 9

Movement Performance

Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 --------------------------------------------------------------------------------
Mov Total Total Aver. Eff. Total Perf. Tot.Trav. Tot.Trav. Aver.

ID Delay Delay Delay Stop Stops Index Distance Time Speed
(veh-h/h)(pers-h/h)(sec) Rate (veh-km/h)(veh-h/h) (km/h)

 --------------------------------------------------------------------------------
East: Ruta H-111 OTE

5 T 0.00 0.00 0.0 0.00 0.0 0.82 41.2 0.8 50.0

6 R 0.01 0.01 6.4 0.91 2.9 0.04 1.0 0.0 39.3

 --------------------------------------------------------------------------------
North: C-1

7 L 0.00 0.01 7.5 1.00 2.1 0.03 0.3 0.0 18.8

9 R 0.04 0.05 7.6 0.84 16.0 0.26 2.3 0.1 18.8

 --------------------------------------------------------------------------------
West: Ruta H-111 PTE

10 L 0.06 0.07 10.3 0.64 12.9 0.32 6.0 0.2 34.4

11 T 0.00 0.00 0.0 0.00 0.0 0.93 46.6 0.9 50.0

 --------------------------------------------------------------------------------
```

Go to Table Links (Top)

Fuel Consumption, Emissions and Cost (Total)
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 -------------------------------------------------------------
Mov Cost Fuel CO2 CO HC NOX

ID Total Total Total Total Total Total

$/h L/h kg/h kg/h kg/h kg/h

 -------------------------------------------------------------
East: Ruta H-111 OTE

5 T 29.00 4.0 10.0 0.28 0.011 0.012

6 R 0.90 0.1 0.3 0.03 0.001 0.001

 ----------------------------------------------
29.90 4.1 10.3 0.30 0.012 0.013

 -------------------------------------------------------------
North: C-1

7 L 0.53 0.1 0.2 0.02 0.000 0.000

9 R 4.84 0.8 1.9 0.15 0.003 0.005

 ----------------------------------------------
5.36 0.8 2.1 0.17 0.003 0.005

 -------------------------------------------------------------
West: Ruta H-111 PTE

10 L 7.66 1.5 3.8 0.31 0.005 0.009

11 T 31.81 4.1 10.2 0.30 0.012 0.014

 ----------------------------------------------
39.47 5.6 14.0 0.62 0.017 0.023

 -------------------------------------------------------------
INTERSECTION: 74.74 10.5 26.4 1.09 0.032 0.041

 -------------------------------------------------------------
```

Go to Table Links (Top)

Fuel Consumption, Emissions and Cost (Rate)
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 -------------------------------------------------------------
Mov Cost Fuel CO2 CO HC NOX

ID Rate Rate Rate Rate Rate Rate

$/km L/100km g/km g/km g/km g/km

 -------------------------------------------------------------
East: Ruta H-111 OTE

5 T 0.70 9.6 241.6 6.71 0.272 0.299

6 R 0.88 12.0 299.3 26.20 0.531 0.701

 ----------------------------------------------
0.71 9.7 243.0 7.18 0.278 0.309

 -------------------------------------------------------------
```

about:blank 09/07/2025

Detailed Output Page 3 of 9

```
 North: C-1

 7 L 2.06 31.2 796.5 61.93 1.049 1.900

 9 R 2.07 32.6 833.0 65.22 1.075 2.011

 ----------------------------------------------
 2.07 32.5 829.4 64.89 1.072 2.000

 -------------------------------------------------------------
 West: Ruta H-111 PTE

 10 L 1.28 24.9 634.2 52.20 0.806 1.586

 11 T 0.68 8.7 218.7 6.50 0.267 0.293

 ----------------------------------------------
 0.75 10.6 265.9 11.69 0.329 0.439

 -------------------------------------------------------------
 INTERSECTION: 0.77 10.7 270.9 11.15 0.326 0.424

 -------------------------------------------------------------
```

Go to Table Links (Top)

Intersection Negotiation Data
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 ----------------------------------------------------------------------------
Negn Negn Negn Appr. Downstream Distance
From To Radius Speed Dist. Dist. -------------------Approach Approach Turn m km/h m m m User Spec?

 ----------------------------------------------------------------------------
East: Ruta H-111 OTE

North Right 10.0 20.2 15.7 250 53 No
West Thru S 50.0 10.0 250 122 No

 ----------------------------------------------------------------------------
North: C-1

East Left 6.7 17.3 10.5 100 22 No

West Right 10.0 20.2 15.7 100 28 No

 ----------------------------------------------------------------------------
West: Ruta H-111 PTE

East Thru S 50.0 10.0 250 117 No

North Left 6.5 17.1 10.1 250 64 No

 ----------------------------------------------------------------------------
Downstream distance is distance travelled from the stopline until exit
cruise speed is reached (includes negotiation distance). Acceleration
distance is weighted for light and heavy vehicles. The same distance
applies for both stopped and unstopped vehicles.

```

Go to Table Links (Top)

Movement Speeds and Geometric Delay
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 ---------------------------------------------------------------------------
Queue Move-up
App. Speeds Exit Speeds ------------- Av. Section Spd Geom
Mov ------------ ----------- 1st 2nd --------------- Delay
ID Cruise Negn Negn Cruise Grn Grn Running Overall sec

 ---------------------------------------------------------------------------
East: Ruta H-111 OTE

5 T 50.0 50.0 50.0 50.0 50.0 50.0 0.0

6 R 50.0 20.2 20.2 50.0 39.3 39.3 6.4

 ---------------------------------------------------------------------------
North: C-1

7 L 25.0 0.0 17.3 25.0 19.5 18.8 6.2

9 R 25.0 0.0 20.2 25.0 19.4 18.8 6.2

 ---------------------------------------------------------------------------
West: Ruta H-111 PTE

10 L 50.0 17.1 17.1 40.0 36.4 34.4 7.2

11 T 50.0 50.0 50.0 50.0 50.0 50.0 0.0

 ---------------------------------------------------------------------------
"Running Speed" is the average speed excluding stopped periods.

```

Go to Table Links (Top)

Gap Acceptance Parameters

about:blank 09/07/2025

Detailed Output Page 4 of 9

Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 ------------------------------------------------------------------------
Critical Gap Intra
Opng ------------ Foll-up Entry Bunch Propn
Mov Mov Flow Hdwy Dist Headway HV Hdwy Bnchd
ID Type pcu/h sec m sec Equiv sec

 ------------------------------------------------------------------------
East: Ruta H-111 OTE

No opposed movements on this approach.

 ------------------------------------------------------------------------
North: C-1

7 L Normal 319 6.53 86.5 3.63 2.00 0.60 0.017

9 R Normal 140 6.78 94.1 3.76 2.00 1.80 0.015

 ------------------------------------------------------------------------
West: Ruta H-111 PTE

10 L Normal 157+ 9.97 126.2 5.70 2.00 0.90 0.008

 ------------------------------------------------------------------------
Values in this table are adjusted for heavy vehicles in the entry stream.
+ Percentage of exiting flow included in total opposing flow

```

Go to Table Links (Top)

**Lanes**

Lane Performance

Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 -------------------------------------------------------------
Q u e u e
Flow Cap Deg. Aver. Eff. 95% Back Lane
Lane Satn Delay Stop ------------ Length
No. veh/h veh/h x sec Rate veh m m

 -------------------------------------------------------------
East: Ruta H-111 OTE

1 TR 131 1643 0.079 0.2 0.02 0.0 0.0 500.0

 -------------------------------------------------------------
North: C-1

1 LR 21 763 0.028 7.6 0.86 0.1 1.1 120.0

 -------------------------------------------------------------
West: Ruta H-111 PTE

1 L 20 455 0.044 10.3 0.64 0.2 1.6 50.0T

2 T 144 1695 0.085 0.0 0.00 0.0 0.0 500.0

 -------------------------------------------------------------
T Short lane due to specification of Turn Bay

```

Go to Table Links (Top)

Lane Flow and Capacity Information
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 ---------------------------------------------------
Lane Dem Flow (veh/h) Min Tot Deg. Lane
No. ------------------- Cap Cap Satn Util
Lef Thru Rig Tot veh/h veh/h x %

 ---------------------------------------------------
East: Ruta H-111 OTE

1 TR 0 127 3 131 131 1643 0.079 100

 ---------------------------------------------------
North: C-1

1 LR 2 0 19 21 21 763 0.028 100

 ---------------------------------------------------
West: Ruta H-111 PTE

1 L 20 0 0 20 20 455 0.044 100

2 T 0 144 0 144 144 1695 0.085 100

```

about:blank 09/07/2025

Detailed Output Page 5 of 9

```
 ---------------------------------------------------
 The capacity value for priority and continuous movements is obtained by
 adjusting the basic saturation flow for heavy vehicle and turning vehicle
 effects. Saturation flow scale applies if specified.

```

Go to Table Links (Top)

Lane, Approach and Intersection Performance
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 -------------------------------------------------------------------------
Lane Demand Flow (veh/h) Adj. Eff Grn Deg Aver. Longest Shrt
No. -------------------- %HV Basic (sec) Sat Delay Queue Lane
L T R Tot Satf. 1st 2nd x sec m m

 -------------------------------------------------------------------------
East: Ruta H-111 OTE

1 TR 127 3 131 15 0.079 0.2 0 500

 -----------------------------------------------------------------
0 127 3 131 15 0.079 0.2

 -------------------------------------------------------------------------
North: C-1

1 LR 2 19 21 55 0.028 7.6 1 120

 -----------------------------------------------------------------
2 0 19 21 55 0.028 7.6 1

 -------------------------------------------------------------------------
West: Ruta H-111 PTE

1 L 20 20 47 0.044 10.3 2 50

2 T 144 144 9 0.085 0.0 0 500

 -----------------------------------------------------------------
20 144 0 164 14 0.085 1.3 2

==========================================================================

ALL VEHICLES Total % Max Aver. Max

Flow HV X Delay Queue
316 17 0.085 1.2 2

==========================================================================

Peak flow period = 30 minutes.

Queue values in this table are 95% queue (metres)
Note: Basic Saturation Flows are not adjusted at roundabouts or signcontrolled intersections and apply only to continuous lanes.

```

Go to Table Links (Top)

Driver Characteristics

Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 -------------------------------------------------------
Average Driver
Lane Satn Satn Satn Satn Queue Response
No. Speed Flow Hdwy Spacing Space Time
km/h veh/h sec m m sec

 -------------------------------------------------------
East: Ruta H-111 OTE

1 TR NA - Major Road Movement

 -------------------------------------------------------
North: C-1

1 LR 19.9 960 3.75 20.71 10.30 1.89

 -------------------------------------------------------
West: Ruta H-111 PTE

1 L NA - Short Lane

2 T NA - Major Road Movement

 -------------------------------------------------------
Saturation Flow and Saturation Headway are derived from follow-up headway.

```

Go to Table Links (Top)

Lane Delays
Site:PMD-L

about:blank 09/07/2025

Detailed Output Page 6 of 9

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 ---------------------------------------------------------------------
 -------------- Delay (seconds/veh) --------------- Deg. Stop-line Delay Acc. Queuing Stopd
 Lane Satn 1st 2nd Total Dec. Total MvUp (Idle) Geom Control
 No. x d1 d2 dSL dn dq dqm di dig dic

 ---------------------------------------------------------------------
 East: Ruta H-111 OTE

 1 TR 0.079 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.2 0.2

 ---------------------------------------------------------------------
 North: C-1

 1 LR 0.028 1.4 0.0 1.4 0.6 0.7 0.0 0.7 6.2 7.6

 ---------------------------------------------------------------------
 West: Ruta H-111 PTE

 1 L 0.044 3.1 0.0 3.1 1.4 1.7 0.0 1.7 7.2 10.3

 2 T 0.085 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0

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
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 -----------------------------------------------------------------------------------
Deg. Ovrfl. Back of Queue (veh) Queue Prob. P'ile Cyc-Av. Queue
Lane Satn Queue --------------------------- Stor. Block Block ------------
No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 -----------------------------------------------------------------------------------
East: Ruta H-111 OTE

1 TR 0.079 0.0 0.0 0.0 0.0 0.0 0.00 0.0 100.0 0.0 0.0

 -----------------------------------------------------------------------------------
North: C-1

1 LR 0.028 0.0 0.0 0.0 0.0 0.1 0.01 0.0 100.0 0.0 0.0

 -----------------------------------------------------------------------------------
West: Ruta H-111 PTE

1 L 0.044 0.0 0.1 0.0 0.1 0.2 0.03 0.0 100.0 0.0 0.0

2 T 0.085 0.0 0.0 0.0 0.0 0.0 0.00 0.0 100.0 0.0 0.0

 -----------------------------------------------------------------------------------
```

Go to Table Links (Top)

Lane Queues (Distance)
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 -----------------------------------------------------------------------------------
Deg. Ovrfl. Back of Queue (m) Queue Prob. P'ile Cyc-Av. Queue
Lane Satn Queue --------------------------- Stor. Block Block ------------
No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 -----------------------------------------------------------------------------------
East: Ruta H-111 OTE

1 TR 0.079 0.0 0.0 0.0 0.0 0.0 0.00 0.0 100.0 0.0 0.0

 -----------------------------------------------------------------------------------
North: C-1

1 LR 0.028 0.0 0.4 0.0 0.4 1.1 0.01 0.0 100.0 0.1 0.1

 -----------------------------------------------------------------------------------
West: Ruta H-111 PTE

1 L 0.044 0.0 0.7 0.0 0.7 1.6 0.03 0.0 100.0 0.2 0.3

2 T 0.085 0.0 0.0 0.0 0.0 0.0 0.00 0.0 100.0 0.0 0.0

 -----------------------------------------------------------------------------------
```

Go to Table Links (Top)

about:blank 09/07/2025

Detailed Output Page 7 of 9

Lane Queue Percentiles (Vehicles)
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 ------------------------------------------------------
Deg. Percentile Back of Queue (veh)

Lane Satn ---------------------------------------
No. x 50% 70% 85% 90% 95% 98%

 ------------------------------------------------------
East: Ruta H-111 OTE

1 TR 0.079 0.0 0.0 0.0 0.0 0.0 0.0

 ------------------------------------------------------
North: C-1

1 LR 0.028 0.0 0.1 0.1 0.1 0.1 0.1

 ------------------------------------------------------
West: Ruta H-111 PTE

1 L 0.044 0.1 0.1 0.1 0.1 0.2 0.2

2 T 0.085 0.0 0.0 0.0 0.0 0.0 0.0

 ------------------------------------------------------
```

Go to Table Links (Top)

Lane Queue Percentiles (Distance)
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 ------------------------------------------------------
Deg. Percentile Back of Queue (metres)

Lane Satn ---------------------------------------
No. x 50% 70% 85% 90% 95% 98%

 ------------------------------------------------------
East: Ruta H-111 OTE

1 TR 0.079 0.0 0.0 0.0 0.0 0.0 0.0

 ------------------------------------------------------
North: C-1

1 LR 0.028 0.4 0.6 0.8 0.9 1.1 1.2

 ------------------------------------------------------
West: Ruta H-111 PTE

1 L 0.044 0.7 0.9 1.2 1.4 1.6 1.8

2 T 0.085 0.0 0.0 0.0 0.0 0.0 0.0

 ------------------------------------------------------
```

Go to Table Links (Top)

Lane Stops
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 ---------------------------------------------------------------------
Queue Total
Deg. -- Effective Stop Rate -- Total Move-up Queue Prop.
Lane Satn Geom. Overall Stops Rate Move-ups Queued
No. x he1 he2 hig h H hqm Hqm pq

 ---------------------------------------------------------------------
East: Ruta H-111 OTE

1 TR 0.079 0.00 0.00 0.02 0.02 2.9 0.00 0.0 0.00

 ---------------------------------------------------------------------
North: C-1

1 LR 0.028 0.17 0.00 0.69 0.86 18.1 0.00 0.0 0.31

 ---------------------------------------------------------------------
West: Ruta H-111 PTE

1 L 0.044 0.26 0.00 0.38 0.64 12.9 0.00 0.0 0.39

2 T 0.085 0.00 0.00 0.00 0.00 0.0 0.00 0.0 0.00

 ---------------------------------------------------------------------
hig is the average value for all movements in a shared lane
hqm is average queue move-up rate for all vehicles queued and unqueued

```

Go to Table Links (Top)

about:blank 09/07/2025

Detailed Output Page 8 of 9

**Flow Rates and Demand Analysis**

Movement Definitions and Flow Rates (O-D)
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 ----------------------------------------------------------------------
From To Mov Flow Rate Flow Scale Peak Flow

Approach Approach ID Turn LV HV Fixed Var Factor

 ----------------------------------------------------------------------
East: Ruta H-111 OTE

North 6 Right 3 0 1.00 1.00 0.95
West 5 Thru 108 19 1.00 1.00 0.95

 ----------------------------------------------------------------------
North: C-1

East 7 Left 1 1 1.00 1.00 0.95

West 9 Right 8 11 1.00 1.00 0.95

 ----------------------------------------------------------------------
West: Ruta H-111 PTE

East 11 Thru 131 14 1.00 1.00 0.95

North 10 Left 11 9 1.00 1.00 0.95

 ----------------------------------------------------------------------
Unit Time for Volumes = 60 minutes

Peak Flow Period = 30 minutes

Flow Rates include effects of Flow Scale and Peak Flow Factor

```

Go to Table Links (Top)

Flow Rates (Separate Light and Heavy Vehicles)
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 ----------------------------------------------
Mov Left Through Right

ID --------- --------- --------
LV HV LV HV LV HV

 ----------------------------------------------
Demand flows in veh/h as used by the program

East: Ruta H-111 OTE

5 T 0 0 108 19 0 0

6 R 0 0 0 0 3 0

 ----------------------------------------------
North: C-1

7 L 1 1 0 0 0 0

9 R 0 0 0 0 8 11

 ----------------------------------------------
West: Ruta H-111 PTE

10 L 11 9 0 0 0 0

11 T 0 0 131 14 0 0

 ----------------------------------------------
Unit Time for Volumes = 60 minutes

Peak Flow Period = 30 minutes

Flow Rates include effects of Flow Scale and Peak Flow Factor

```

Go to Table Links (Top)

Flow Rates (Total Vehicles and Percent Heavy)
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

 -------------------------------------------------
Mov Left Through Right

ID ---------- ---------- ---------
Total %HV Total %HV Total %HV

 -------------------------------------------------
Demand flows in veh/h as used by the program

East: Ruta H-111 OTE

```

about:blank 09/07/2025

Detailed Output Page 9 of 9

```
 5 T 0 0.0 127 14.9 0 0.0

 6 R 0 0.0 0 0.0 3 0.0

 -------------------------------------------------
 North: C-1

 7 L 2 50.0 0 0.0 0 0.0

 9 R 0 0.0 0 0.0 19 55.6

 -------------------------------------------------
 West: Ruta H-111 PTE

 10 L 20 47.4 0 0.0 0 0.0

 11 T 0 0.0 144 9.5 0 0.0

 -------------------------------------------------
 Unit Time for Volumes = 60 minutes

 Peak Flow Period = 30 minutes

 Flow Rates include effects of Flow Scale and Peak Flow Factor

```

Go to Table Links (Top)

**Other**

Model Settings
Site:PMD-L

```
Intersection ID: 1

Stop Sign Controlled Intersection

* Basic Parameters:

Intersection Type: Unsignalised - Two-Way Stop Control
Driving on the right-hand side of the road
Input data specified in Metric units
Model Defaults: Standard Right
Peak Flow Period (for performance): 30 minutes
Unit time (for volumes): 60 minutes.
SIDRA Standard Delay model used
SIDRA Standard Queue model used
Level of Service based on: Delay (HCM 2000)
Queue percentile: 95%

```

Go to Table Links (Top)

Parameters Used in Cost Calculations

Site:PMD-L

```
Intersection ID: 1

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
Site:PMD-L

Go to Table Links (Top)

Processed: miércoles, 9 de julio de 2025 09:15:51 p. m. Copyright © 2000-2011 Akcelik and Associates Pty Ltd
SIDRA INTERSECTION 5.1.13.2093 www.sidrasolutions.com

Project: C:\Users\jguti\Mas Ciudad Spa\Proyectos - Doc\236 Planta Chilemink\Modelacion\Rev_1
\Construccion\2_Base\Chilemink_Base.sip
Licensed to JUNLAJUBALAM

about:blank 09/07/2025