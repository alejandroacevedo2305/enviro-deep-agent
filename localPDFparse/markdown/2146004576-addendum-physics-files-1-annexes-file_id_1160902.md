---
title: Sin título
author: DEZ
date: D:20210216173539-03'00'
language: en
type: general
pages: 34
has_toc: False
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Situación Actual
  - Situación Base (2023)
  - Situación con Proyecto (2023)
-->

ANEXO

Salida modelo SIDRA

# Situación Actual

## DETAILED OUTPUT

**Site: AC 2021**

New Site
Stop (Two-Way)

**OUTPUT TABLE LINKS**

**Movements**

Intersection Negotiation Data
Site:AC 2021

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 INTERSECTION NEGOTIATION DATA

 ----------------------------------------------------------------------------
 Negn Negn Negn Appr. Downstream Distance
 From To Radius Speed Dist. Dist. ------------------- Approach Exit Turn m km/h m m m User Spec?

 ----------------------------------------------------------------------------
 South: C Cementerio

 West L2 6.6 17.2 10.4 200 168 No

 North T1 S 60.0 10.0 200 383 No

 ----------------------------------------------------------------------------
 North: C Cementerio

 South T1 S 60.0 10.0 200 340 No

 West R2 10.0 20.2 15.7 200 125 No

 ----------------------------------------------------------------------------
```

```
 West: Las Catalpas
 North L2 6.6 17.2 10.4 200 191 No

 South R2 10.0 20.2 15.7 200 171 No

 ----------------------------------------------------------------------------
 Downstream distance is distance travelled from the stopline until exit
 cruise speed is reached (includes negotiation distance). Acceleration
 distance is weighted for light and heavy vehicles. The same distance
 applies for both stopped and unstopped vehicles.

 MOVEMENT SPEEDS AND GEOMETRIC DELAY

 ----------------------------------------------------------------------------
 Queue Move-up
 App. Speeds Exit Speeds ------------- Av. Section Spd Geom
 Mov Turn ------------ ----------- 1st 2nd --------------- Delay
 ID Cruise Negn Negn Cruise Grn Grn Running Overall sec

 ----------------------------------------------------------------------------
 South: C Cementerio

 1 L2 60.0 17.2 17.2 60.0 5.2 43.7 43.7 9.6

 2 T1 60.0 60.0 60.0 60.0 5.2 43.7 43.7 0.0

 ----------------------------------------------------------------------------
 North: C Cementerio

 8 T1 60.0 60.0 60.0 60.0 53.7 53.7 0.0

 9 R2 60.0 20.2 20.2 60.0 53.7 53.7 9.2

 ----------------------------------------------------------------------------
 West: Las Catalpas
 10 L2 60.0 0.0 17.2 60.0 17.3 38.1 36.4 11.6

 12 R2 60.0 0.0 20.2 60.0 17.3 38.1 36.4 11.6

 ----------------------------------------------------------------------------
 "Running Speed" is the average speed excluding stopped periods.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Gap Acceptance Parameters
Site:AC 2021

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -------------------------------------------------------------------------
 Critical Gap Intra
 Opng ------------ Foll-up Entry Bunch Propn
 Opd Dest Flow Hdwy Dist Headway HV Hdwy Bnchd
 Lane pcu/h sec m sec Equiv sec

 -------------------------------------------------------------------------
 South: C Cementerio

 1 W 313 4.20 58.4 2.10 1.05 1.80 0.036

 -------------------------------------------------------------------------
 North: C Cementerio

 No opposed movements on this approach.

 -------------------------------------------------------------------------
 West: Las Catalpas
 1 S 236+ 4.58 76.3 2.54 1.02 1.80 0.026

 1 N 536+ 4.95 76.0 3.20 1.03 0.92 0.031

 -------------------------------------------------------------------------
 Values in this table are adjusted for heavy vehicles in the entry stream.
 Use the Pedestrians and Priorities input dialogs to specify opposing pedestrian movements.
 + Percentage of exiting flow included in opposing vehicle flow

```

[Go to Table Links (Top)](about:blank#tablelinks)

Movement Capacity and Performance Parameters
Site:AC 2021

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 MOVEMENT CAPACITY PARAMETERS

 --------------------------------------------------------------
 Mov Turn Mov Opng Movement Total Prac. Prac. Deg.
 ID Cl. Arv Adjust. Cap. Deg. Spare Satn
 Flow Flow Flow Satn Cap.
 veh/h veh/h pcu/h veh/h xp % x

 --------------------------------------------------------------
 South: C Cementerio

 1 L2 # 53 304 313 350 0.98 551 0.150

 2 T1 # 197 0 0 1309 0.98 551 0.150

 --------------------------------------------------------------
 North: C Cementerio

 8 T1 # 228 0 0 1393 0.98 497 0.164*

 9 R2 # 76 0 0 462 0.98 497 0.164*

 --------------------------------------------------------------
 West: Las Catalpas
 10 L2 # 34 516 536 416 0.80 887 0.081

 12 R2 # 31 228 236 377 0.80 887 0.081

 --------------------------------------------------------------
 * Maximum degree of saturation
 # Combined Movement Capacity parameters are shown for all Movement Classes.

 MOVEMENT PERFORMANCE

 -------------------------------------------------------------------------------
 Mov Turn Total Total Aver. Eff. Total Perf. Tot.Trav. Tot.Trav. Aver.

 ID Delay Delay Delay Stop Stops Index Distance Time Speed
 (veh-h/h)(pers-h/h)(sec) Rate (veh-km/h)(veh-h/h) (km/h)

 -------------------------------------------------------------------------------
 South: C Cementerio

 1 L2 0.16 0.19 10.9 0.21 11.0 0.52 17.8 0.4 43.7

 2 T1 0.07 0.09 1.4 0.21 41.1 1.41 66.7 1.5 43.7

 -------------------------------------------------------------------------------
 North: C Cementerio

 8 T1 0.00 0.00 0.0 0.26 60.5 1.63 77.5 1.4 53.7

 9 R2 0.19 0.23 9.2 0.26 20.1 0.73 25.7 0.5 53.7

 -------------------------------------------------------------------------------
 West: Las Catalpas
 10 L2 0.13 0.15 13.8 0.83 28.1 0.70 11.3 0.3 36.4

 12 R2 0.12 0.14 13.9 0.83 25.5 0.66 10.2 0.3 36.4

 -------------------------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Fuel Consumption, Emissions and Cost
Site:AC 2021

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 FUEL CONSUMPTION, EMISSIONS AND COST (TOTAL)

 --------------------------------------------------------------
 Mov Turn Cost Fuel CO2 CO HC NOX

 ID Total Total Total Total Total Total
 $/h L/h kg/h kg/h kg/h kg/h

 --------------------------------------------------------------
 South: C Cementerio

 1 L2 18.18 2.3 5.4 0.01 0.001 0.024

 2 T1 67.99 8.5 20.2 0.04 0.005 0.091

```

```
 -----------------------------------------------
 86.16 10.7 25.5 0.06 0.006 0.115

 --------------------------------------------------------------
 North: C Cementerio

 8 T1 60.19 6.9 16.2 0.04 0.004 0.061

 9 R2 19.97 2.3 5.4 0.01 0.001 0.020

 -----------------------------------------------
 80.16 9.1 21.6 0.05 0.006 0.082

 --------------------------------------------------------------
 West: Las Catalpas
 10 L2 11.97 1.1 2.5 0.01 0.001 0.009

 12 R2 10.85 1.0 2.3 0.01 0.001 0.008

 -----------------------------------------------
 22.82 2.1 4.8 0.01 0.002 0.016

 --------------------------------------------------------------
 INTERSECTION: 189.14 21.9 52.0 0.12 0.013 0.213

 -------------------------------------------------------------
 FUEL CONSUMPTION, EMISSIONS AND COST (RATE)

 --------------------------------------------------------------
 Mov Turn Cost Fuel CO2 CO HC NOX

 ID Rate Rate Rate Rate Rate Rate
 $/km L/100km g/km g/km g/km g/km

 --------------------------------------------------------------
 South: C Cementerio

 1 L2 1.02 12.7 302.3 0.66 0.070 1.365

 2 T1 1.02 12.7 302.3 0.66 0.070 1.365

 -----------------------------------------------
 1.02 12.7 302.3 0.66 0.070 1.365

 --------------------------------------------------------------
 North: C Cementerio

 8 T1 0.78 8.8 209.4 0.51 0.054 0.790

 9 R2 0.78 8.8 209.4 0.51 0.054 0.790

 -----------------------------------------------
 0.78 8.8 209.4 0.51 0.054 0.790

 --------------------------------------------------------------
 West: Las Catalpas
 10 L2 1.06 9.5 225.0 0.61 0.078 0.754

 12 R2 1.06 9.5 225.0 0.61 0.078 0.754

 -----------------------------------------------
 1.06 9.5 225.0 0.61 0.078 0.754

 --------------------------------------------------------------
 INTERSECTION: 0.75 8.7 207.1 0.48 0.052 0.849

 -------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

**Lanes**

Lane Performance and Capacity Information
Site:AC 2021

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE PERFORMANCE

 --------------------------------------------------------------
 Q u e u e
 Flow Cap Deg. Aver. Eff. 95% Back Lane
 Lane Satn Delay Stop ------------ Length
 No. veh/h veh/h x sec Rate veh m m

 --------------------------------------------------------------
 South: C Cementerio

```

```
 1 249 1658 0.150 3.4 0.21 1.0 7.2 200.0

 --------------------------------------------------------------
 North: C Cementerio

 1 304 1855 0.164 2.3 0.26 200.0

 --------------------------------------------------------------
 West: Las Catalpas
 1 64 792 0.081 13.8 0.83 0.3 2.1 200.0

 --------------------------------------------------------------
 LANE FLOW AND CAPACITY INFORMATION

 ----------------------------------------
 Lane Total Min Tot Deg. Lane
 No. Arv Flow Cap Cap Satn Util
 (veh/h) veh/h veh/h x %

 ----------------------------------------
 South: C Cementerio

 1 249 28 1658 0.150 100

 ----------------------------------------
 North: C Cementerio

 1 304 304 1855 0.164 100

 ----------------------------------------
 West: Las Catalpas
 1 64 6 792 0.081 100

 ----------------------------------------
 The capacity value for priority and continuous movements is obtained by
 adjusting the basic saturation flow for heavy vehicle and turning vehicle
 effects. Saturation flow scale applies if specified.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane, Approach and Intersection Performance
Site:AC 2021

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -----------------------------------------------------------
 Lane Demand Adj. Deg Aver. Longest Shrt
 No. Flow %HV Basic Sat Delay Queue Lane
 (veh/h) Satf. x sec m m

 -----------------------------------------------------------
 South: C Cementerio

 1 249 10 0.150 3.4 7 200

 ---------------------------------------------------
 249 10 0.150 3.4 7

 -----------------------------------------------------------
 North: C Cementerio

 1 304 6 1950 0.164 2.3 200

 ---------------------------------------------------
 304 6 0.164 2.3

 -----------------------------------------------------------
 West: Las Catalpas
 1 64 5 0.081 13.8 2 200

 ---------------------------------------------------
 64 5 0.081 13.8 2

 ============================================================

 ALL VEHICLES

 Total % Max Aver. Max

 Flow HV X Delay Queue
 618 7 0.164 3.9 7

 ============================================================

 Peak flow period = 30 minutes.

 Queue values in this table are 95% queue (metres)
 Note: Basic Saturation Flows are not adjusted at roundabouts or sign controlled intersections and apply only to continuous lanes.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Driver Characteristics

Site:AC 2021

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -------------------------------------------------------
 Average Driver
 Lane Satn Satn Satn Satn Queue Response
 No. Speed Flow Hdwy Spacing Space Time
 km/h veh/h sec m m sec

 -------------------------------------------------------
 South: C Cementerio

 1 NA - Major Road Movement

 -------------------------------------------------------
 North: C Cementerio

 1 NA - Continuous Movement

 -------------------------------------------------------
 West: Las Catalpas
 1 18.6 1247 2.89 14.93 7.30 1.48

 -------------------------------------------------------
 Saturation Flow and Saturation Headway are derived from follow-up headway.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Delays
Site:AC 2021

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE DELAYS

 -----------------------------------------------------------------------------
 ---------------- Delay (seconds/veh) --------------- Deg. Prog. Stop-line Delay Acc. Queuing Stopd
 Lane Satn Factor 1st 2nd Total Dec. Total MvUp (Idle) Geom Control
 No. x d1 d2 dSL dn dq dqm di dig dic

 -----------------------------------------------------------------------------
 South: C Cementerio

 1 0.150 1.000 1.4 0.0 1.4 3.8 0.0 0.0 0.0 2.0 3.4

 -----------------------------------------------------------------------------
 North: C Cementerio

 1 0.164 0.0 2.3 2.3

 -----------------------------------------------------------------------------
 West: Las Catalpas

 1 0.081 1.000 2.2 0.0 2.2 0.8 1.4 0.0 1.4 11.6 13.8

 -----------------------------------------------------------------------------
 SIDRA Standard Delay Model is used. Control Delay is the sum of Stop-line Delay
 and Geometric Delay.
 dSL: Stop-line delay (=d1+d2)
 dn: Average stop-start delay for all vehicles queued and unqueued
 dq: Queuing delay (the part of the stop-line delay that includes
 stopped delay and queue move-up delay)
 dqm: Queue move-up delay
 di: Stopped delay (stopped (idling) time at near-zero speed)
 dig: Geometric delay
 dic: Control delay

```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Queues
Site:AC 2021

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE QUEUES (VEHICLES)

 --------------------------------------------------------------------------------------------
 Deg. Prog. Ovrfl. Back of Queue (veh) Queue Prob. P'ile Cyc-Av. Queue
 Lane Satn Factor Queue ------------------------- Stor. Block Block ------------
 No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 --------------------------------------------------------------------------------------------
 South: C Cementerio

 1 0.150 1.000 0.0 0.4 0.0 0.4 1.0 0.01 0.0 100.0 0.1 0.2

 --------------------------------------------------------------------------------------------
 North: C Cementerio

 --------------------------------------------------------------------------------------------
 West: Las Catalpas
 1 0.081 1.000 0.0 0.1 0.0 0.1 0.3 0.00 0.0 100.0 0.0 0.1

 --------------------------------------------------------------------------------------------
 LANE QUEUES (DISTANCE)

 --------------------------------------------------------------------------------------------
 Deg. Prog. Ovrfl. Back of Queue (m) Queue Prob. P'ile Cyc-Av. Queue
 Lane Satn Factor Queue ------------------------- Stor. Block Block ------------
 No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 --------------------------------------------------------------------------------------------
 South: C Cementerio

 1 0.150 1.000 0.0 2.9 0.0 2.9 7.2 0.01 0.0 100.0 0.7 1.3

 --------------------------------------------------------------------------------------------
 North: C Cementerio

 --------------------------------------------------------------------------------------------
 West: Las Catalpas
 1 0.081 1.000 0.0 0.8 0.0 0.8 2.1 0.00 0.0 100.0 0.3 0.5

 --------------------------------------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Queue Percentiles
Site:AC 2021

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE QUEUE PERCENTILES (VEHICLES)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (veh)

 Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 South: C Cementerio

 1 0.150 0.4 0.5 0.7 0.8 1.0 1.1 1.1

 -------------------------------------------------------------
 North: C Cementerio

 -------------------------------------------------------------
 West: Las Catalpas
 1 0.081 0.1 0.1 0.2 0.2 0.3 0.3 0.3

 -------------------------------------------------------------
```

```
 LANE QUEUE PERCENTILES (DISTANCE)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (metres)

 Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 South: C Cementerio

 1 0.150 2.9 3.8 5.3 6.1 7.2 8.0 8.6

 -------------------------------------------------------------
 North: C Cementerio

 -------------------------------------------------------------
 West: Las Catalpas
 1 0.081 0.8 1.1 1.5 1.8 2.1 2.3 2.5

 -------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Stops
Site:AC 2021

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -----------------------------------------------------------------------------
 Queue Total
 Deg. Prog. -- Effective Stop Rate -- Total Move-up Queue Prop.
 Lane Satn Factor Geom. Overall Stops Rate Move-ups Queued
 No. x he1 he2 hig h H hqm Hqm pq

 -----------------------------------------------------------------------------
 South: C Cementerio

 1 0.150 1.000 0.07 0.00 0.14 0.21 52.0 0.00 0.0 0.44

 -----------------------------------------------------------------------------
 North: C Cementerio

 1 0.164 1.000 0.26 0.26 80.6

 -----------------------------------------------------------------------------
 West: Las Catalpas
 1 0.081 1.000 0.31 0.00 0.53 0.83 53.6 0.00 0.0 0.40

 -----------------------------------------------------------------------------
 hig is the average value for all movements in a shared lane
 hqm is average queue move-up rate for all vehicles queued and unqueued

```

[Go to Table Links (Top)](about:blank#tablelinks)

**Flow Rates**

Origin-Destination Flow Rates (Total)
Site:AC 2021

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 TOTAL FLOW RATES (ALL MOVEMENT CLASSES)

 --------------------------------------------------
 From SOUTH To: W N

 Turn: L2 T1 TOT

 Flow Rate 52.6 196.8 249.5

 %HV (all designations) 10.0 9.6 9.7

 --------------------------------------------------
```

```
 From NORTH To: S W

 Turn: T1 R2 TOT

 Flow Rate 228.4 75.8 304.2

 %HV (all designations) 6.9 2.8 5.9

 --------------------------------------------------
 From WEST To: N S

 Turn: L2 R2 TOT

 Flow Rate 33.7 30.5 64.2

 %HV (all designations) 6.2 3.4 4.9

 --------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Origin-Destination Flow Rates by Movement Class
Site:AC 2021

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 FLOW RATES FOR Light Vehicles

 ------------------------------------------
 From SOUTH To: W N

 Turn: L2 T1 TOT

 ------------------------------------------
 Flow Rate - Veh 47.4 177.9 225.3

 Mov Class % 90.0 90.4 90.3

 Flow Scale - Fixed 1.00 1.00

 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
 From NORTH To: S W

 Turn: T1 R2 TOT

 ------------------------------------------
 Flow Rate - Veh 212.6 73.7 286.3

 Mov Class % 93.1 97.2 94.1

 Flow Scale - Fixed 1.00 1.00

 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
 From WEST To: N S

 Turn: L2 R2 TOT

 ------------------------------------------
 Flow Rate - Veh 31.6 29.5 61.1

 Mov Class % 93.8 96.6 95.1

 Flow Scale - Fixed 1.00 1.00

 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
 FLOW RATES FOR Heavy Vehicles

 ------------------------------------------
 From SOUTH To: W N

 Turn: L2 T1 TOT

 ------------------------------------------
 Flow Rate - Veh 5.3 18.9 24.2

 Mov Class % 10.0 9.6 9.7

 Flow Scale - Fixed 1.00 1.00

 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
 From NORTH To: S W

 Turn: T1 R2 TOT

 ------------------------------------------
 Flow Rate - Veh 15.8 2.1 17.9

 Mov Class % 6.9 2.8 5.9

 Flow Scale - Fixed 1.00 1.00

```

```
 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
 From WEST To: N S

 Turn: L2 R2 TOT

 ------------------------------------------
 Flow Rate - Veh 2.1 1.1 3.2

 Mov Class % 6.2 3.4 4.9

 Flow Scale - Fixed 1.00 1.00

 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Flow Rates

Site:AC 2021

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE FLOW RATES AT STOP LINE

 ----------------------------------------
 From SOUTH To: W N

 Turn: L2 T1 TOT

 ----------------------------------------
 Lane 1

 LV 47.4 177.9 225.3

 HV 5.3 18.9 24.2

 Total 52.6 196.8 249.5

 ----------------------------------------
 Approach 52.6 196.8 249.5

 ----------------------------------------
 From NORTH To: S W

 Turn: T1 R2 TOT

 ----------------------------------------
 Lane 1

 LV 212.6 73.7 286.3

 HV 15.8 2.1 17.9

 Total 228.4 75.8 304.2

 ----------------------------------------
 Approach 228.4 75.8 304.2

 ----------------------------------------
 From WEST To: N S

 Turn: L2 R2 TOT

 ----------------------------------------
 Lane 1

 LV 31.6 29.5 61.1

 HV 2.1 1.1 3.2

 Total 33.7 30.5 64.2

 ----------------------------------------
 Approach 33.7 30.5 64.2

 ----------------------------------------
 EXIT LANE FLOW RATES

 ----------------------------------------
 Movement Class: LV HV TOT

 ----------------------------------------
 Exit: SOUTH

 Lane: 1 242.1 16.8 258.9

 Total 242.1 16.8 258.9

 ----------------------------------------
 Exit: NORTH

 Lane: 1 209.5 21.1 230.5

 Total 209.5 21.1 230.5

```

```
 ----------------------------------------
 Exit: WEST

 Lane: 1 121.1 7.4 128.4

 Total 121.1 7.4 128.4

 ----------------------------------------
 DOWNSTREAM LANE FLOW RATES FOR EXIT ROADS

 ----------------------------------------
 Movement Class: LV HV TOT

 ----------------------------------------
 Exit: SOUTH

 Lane: 1 242.1 16.8 258.9

 Total 242.1 16.8 258.9

 ----------------------------------------
 Exit: NORTH

 Lane: 1 209.5 21.1 230.5

 Total 209.5 21.1 230.5

 ----------------------------------------
 Exit: WEST

 Lane: 1 121.1 7.4 128.4

 Total 121.1 7.4 128.4

 ----------------------------------------
 Unit Time for Volumes = 60 minutes

 Peak Flow Period = 30 minutes

 Flow Rates include effects of Flow Scale and Peak Flow Factor

```

[Go to Table Links (Top)](about:blank#tablelinks)

**Other**

Model Settings Summary
Site:AC 2021

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

[Go to Table Links (Top)](about:blank#tablelinks)

Diagnostics
Site:AC 2021

[Go to Table Links (Top)](about:blank#tablelinks)

# Situación Base (2023)

## DETAILED OUTPUT

**Site: BA 2023**

New Site
Stop (Two-Way)

**OUTPUT TABLE LINKS**

**Movements**

Intersection Negotiation Data
Site:BA 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 INTERSECTION NEGOTIATION DATA

 ----------------------------------------------------------------------------
 Negn Negn Negn Appr. Downstream Distance
 From To Radius Speed Dist. Dist. ------------------- Approach Exit Turn m km/h m m m User Spec?

 ----------------------------------------------------------------------------
 South: C Cementerio

 West L2 6.6 17.2 10.4 200 161 No

 North T1 S 60.0 10.0 200 374 No

 ----------------------------------------------------------------------------
 North: C Cementerio

 South T1 S 60.0 10.0 200 335 No

 West R2 10.0 20.2 15.7 200 123 No

 ----------------------------------------------------------------------------
```

```
 West: Las Catalpas
 North L2 6.6 17.2 10.4 200 185 No

 South R2 10.0 20.2 15.7 200 168 No

 ----------------------------------------------------------------------------
 Downstream distance is distance travelled from the stopline until exit
 cruise speed is reached (includes negotiation distance). Acceleration
 distance is weighted for light and heavy vehicles. The same distance
 applies for both stopped and unstopped vehicles.

 MOVEMENT SPEEDS AND GEOMETRIC DELAY

 ----------------------------------------------------------------------------
 Queue Move-up
 App. Speeds Exit Speeds ------------- Av. Section Spd Geom
 Mov Turn ------------ ----------- 1st 2nd --------------- Delay
 ID Cruise Negn Negn Cruise Grn Grn Running Overall sec

 ----------------------------------------------------------------------------
 South: C Cementerio

 1 L2 60.0 17.2 17.2 60.0 4.9 43.0 43.0 9.6

 2 T1 60.0 60.0 60.0 60.0 4.9 43.0 43.0 0.0

 ----------------------------------------------------------------------------
 North: C Cementerio

 8 T1 60.0 60.0 60.0 60.0 53.7 53.7 0.0

 9 R2 60.0 20.2 20.2 60.0 53.7 53.7 9.2

 ----------------------------------------------------------------------------
 West: Las Catalpas
 10 L2 60.0 0.0 17.2 60.0 16.9 38.1 36.0 11.6

 12 R2 60.0 0.0 20.2 60.0 16.9 38.1 36.0 11.6

 ----------------------------------------------------------------------------
 "Running Speed" is the average speed excluding stopped periods.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Gap Acceptance Parameters
Site:BA 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -------------------------------------------------------------------------
 Critical Gap Intra
 Opng ------------ Foll-up Entry Bunch Propn
 Opd Dest Flow Hdwy Dist Headway HV Hdwy Bnchd
 Lane pcu/h sec m sec Equiv sec

 -------------------------------------------------------------------------
 South: C Cementerio

 1 W 351 4.18 58.1 2.09 1.04 1.80 0.041

 -------------------------------------------------------------------------
 North: C Cementerio

 No opposed movements on this approach.

 -------------------------------------------------------------------------
 West: Las Catalpas
 1 S 264+ 4.57 76.2 2.54 1.02 1.80 0.030

 1 N 599+ 4.93 75.8 3.19 1.03 0.92 0.035

 -------------------------------------------------------------------------
 Values in this table are adjusted for heavy vehicles in the entry stream.
 Use the Pedestrians and Priorities input dialogs to specify opposing pedestrian movements.
 + Percentage of exiting flow included in opposing vehicle flow

```

[Go to Table Links (Top)](about:blank#tablelinks)

Movement Capacity and Performance Parameters
Site:BA 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 MOVEMENT CAPACITY PARAMETERS

 --------------------------------------------------------------
 Mov Turn Mov Opng Movement Total Prac. Prac. Deg.
 ID Cl. Arv Adjust. Cap. Deg. Spare Satn
 Flow Flow Flow Satn Cap.
 veh/h veh/h pcu/h veh/h xp % x

 --------------------------------------------------------------
 South: C Cementerio

 1 L2 # 59 341 351 348 0.98 478 0.169

 2 T1 # 220 0 0 1299 0.98 478 0.169

 --------------------------------------------------------------
 North: C Cementerio

 8 T1 # 256 0 0 1394 0.98 434 0.184*

 9 R2 # 85 0 0 465 0.98 434 0.184*

 --------------------------------------------------------------
 West: Las Catalpas
 10 L2 # 38 577 599 394 0.80 732 0.096

 12 R2 # 34 256 264 350 0.80 732 0.096

 --------------------------------------------------------------
 * Maximum degree of saturation
 # Combined Movement Capacity parameters are shown for all Movement Classes.

 MOVEMENT PERFORMANCE

 -------------------------------------------------------------------------------
 Mov Turn Total Total Aver. Eff. Total Perf. Tot.Trav. Tot.Trav. Aver.

 ID Delay Delay Delay Stop Stops Index Distance Time Speed
 (veh-h/h)(pers-h/h)(sec) Rate (veh-km/h)(veh-h/h) (km/h)

 -------------------------------------------------------------------------------
 South: C Cementerio

 1 L2 0.18 0.22 11.1 0.21 12.3 0.58 20.0 0.5 43.0

 2 T1 0.10 0.12 1.6 0.21 46.1 1.60 74.5 1.7 43.0

 -------------------------------------------------------------------------------
 North: C Cementerio

 8 T1 0.00 0.00 0.0 0.27 68.0 1.82 86.8 1.6 53.7

 9 R2 0.22 0.26 9.2 0.27 22.7 0.83 28.9 0.5 53.7

 -------------------------------------------------------------------------------
 West: Las Catalpas
 10 L2 0.15 0.18 14.2 0.86 32.5 0.81 12.7 0.4 36.0

 12 R2 0.13 0.16 14.3 0.86 28.9 0.75 11.3 0.3 36.0

 -------------------------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Fuel Consumption, Emissions and Cost
Site:BA 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 FUEL CONSUMPTION, EMISSIONS AND COST (TOTAL)

 --------------------------------------------------------------
 Mov Turn Cost Fuel CO2 CO HC NOX

 ID Total Total Total Total Total Total
 $/h L/h kg/h kg/h kg/h kg/h

 --------------------------------------------------------------
 South: C Cementerio

 1 L2 20.07 2.4 5.8 0.01 0.001 0.026

 2 T1 74.90 9.1 21.6 0.05 0.005 0.095

```

```
 -----------------------------------------------
 94.97 11.5 27.3 0.06 0.007 0.121

 --------------------------------------------------------------
 North: C Cementerio

 8 T1 66.49 7.4 17.6 0.04 0.005 0.065

 9 R2 22.16 2.5 5.9 0.01 0.002 0.022

 -----------------------------------------------
 88.65 9.9 23.4 0.06 0.006 0.086

 --------------------------------------------------------------
 West: Las Catalpas
 10 L2 13.31 1.2 2.7 0.01 0.001 0.009

 12 R2 11.83 1.0 2.4 0.01 0.001 0.008

 -----------------------------------------------
 25.14 2.2 5.2 0.01 0.002 0.016

 --------------------------------------------------------------
 INTERSECTION: 208.77 23.6 55.9 0.13 0.015 0.223

 -------------------------------------------------------------
 FUEL CONSUMPTION, EMISSIONS AND COST (RATE)

 --------------------------------------------------------------
 Mov Turn Cost Fuel CO2 CO HC NOX

 ID Rate Rate Rate Rate Rate Rate
 $/km L/100km g/km g/km g/km g/km

 --------------------------------------------------------------
 South: C Cementerio

 1 L2 1.00 12.2 289.3 0.65 0.070 1.277

 2 T1 1.00 12.2 289.3 0.65 0.070 1.277

 -----------------------------------------------
 1.00 12.2 289.3 0.65 0.070 1.277

 --------------------------------------------------------------
 North: C Cementerio

 8 T1 0.77 8.6 202.6 0.50 0.053 0.746

 9 R2 0.77 8.6 202.6 0.50 0.053 0.746

 -----------------------------------------------
 0.77 8.6 202.6 0.50 0.053 0.746

 --------------------------------------------------------------
 West: Las Catalpas
 10 L2 1.05 9.1 214.5 0.60 0.077 0.678

 12 R2 1.05 9.1 214.5 0.60 0.077 0.678

 -----------------------------------------------
 1.05 9.1 214.5 0.60 0.077 0.678

 --------------------------------------------------------------
 INTERSECTION: 0.74 8.4 199.0 0.47 0.052 0.795

 -------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

**Lanes**

Lane Performance and Capacity Information
Site:BA 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE PERFORMANCE

 --------------------------------------------------------------
 Q u e u e
 Flow Cap Deg. Aver. Eff. 95% Back Lane
 Lane Satn Delay Stop ------------ Length
 No. veh/h veh/h x sec Rate veh m m

 --------------------------------------------------------------
 South: C Cementerio

```

```
 1 279 1646 0.169 3.6 0.21 1.1 8.4 200.0

 --------------------------------------------------------------
 North: C Cementerio

 1 341 1859 0.184 2.3 0.27 200.0

 --------------------------------------------------------------
 West: Las Catalpas
 1 72 744 0.096 14.2 0.86 0.3 2.4 200.0

 --------------------------------------------------------------
 LANE FLOW AND CAPACITY INFORMATION

 ----------------------------------------
 Lane Total Min Tot Deg. Lane
 No. Arv Flow Cap Cap Satn Util
 (veh/h) veh/h veh/h x %

 ----------------------------------------
 South: C Cementerio

 1 279 28 1646 0.169 100

 ----------------------------------------
 North: C Cementerio

 1 341 341 1859 0.184 100

 ----------------------------------------
 West: Las Catalpas
 1 72 6 744 0.096 100

 ----------------------------------------
 The capacity value for priority and continuous movements is obtained by
 adjusting the basic saturation flow for heavy vehicle and turning vehicle
 effects. Saturation flow scale applies if specified.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane, Approach and Intersection Performance
Site:BA 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -----------------------------------------------------------
 Lane Demand Adj. Deg Aver. Longest Shrt
 No. Flow %HV Basic Sat Delay Queue Lane
 (veh/h) Satf. x sec m m

 -----------------------------------------------------------
 South: C Cementerio

 1 279 9 0.169 3.6 8 200

 ---------------------------------------------------
 279 9 0.169 3.6 8

 -----------------------------------------------------------
 North: C Cementerio

 1 341 6 1950 0.184 2.3 200

 ---------------------------------------------------
 341 6 0.184 2.3

 -----------------------------------------------------------
 West: Las Catalpas
 1 72 4 0.096 14.2 2 200

 ---------------------------------------------------
 72 4 0.096 14.2 2

 ============================================================

 ALL VEHICLES

 Total % Max Aver. Max

 Flow HV X Delay Queue
 692 7 0.184 4.1 8

 ============================================================

 Peak flow period = 30 minutes.

 Queue values in this table are 95% queue (metres)
 Note: Basic Saturation Flows are not adjusted at roundabouts or sign controlled intersections and apply only to continuous lanes.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Driver Characteristics

Site:BA 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -------------------------------------------------------
 Average Driver
 Lane Satn Satn Satn Satn Queue Response
 No. Speed Flow Hdwy Spacing Space Time
 km/h veh/h sec m m sec

 -------------------------------------------------------
 South: C Cementerio

 1 NA - Major Road Movement

 -------------------------------------------------------
 North: C Cementerio

 1 NA - Continuous Movement

 -------------------------------------------------------
 West: Las Catalpas
 1 18.6 1249 2.88 14.89 7.26 1.48

 -------------------------------------------------------
 Saturation Flow and Saturation Headway are derived from follow-up headway.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Delays
Site:BA 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE DELAYS

 -----------------------------------------------------------------------------
 ---------------- Delay (seconds/veh) --------------- Deg. Prog. Stop-line Delay Acc. Queuing Stopd
 Lane Satn Factor 1st 2nd Total Dec. Total MvUp (Idle) Geom Control
 No. x d1 d2 dSL dn dq dqm di dig dic

 -----------------------------------------------------------------------------
 South: C Cementerio

 1 0.169 1.000 1.6 0.0 1.6 4.1 0.0 0.0 0.0 2.0 3.6

 -----------------------------------------------------------------------------
 North: C Cementerio

 1 0.184 0.0 2.3 2.3

 -----------------------------------------------------------------------------
 West: Las Catalpas

 1 0.096 1.000 2.6 0.0 2.6 0.8 1.8 0.0 1.8 11.6 14.2

 -----------------------------------------------------------------------------
 SIDRA Standard Delay Model is used. Control Delay is the sum of Stop-line Delay
 and Geometric Delay.
 dSL: Stop-line delay (=d1+d2)
 dn: Average stop-start delay for all vehicles queued and unqueued
 dq: Queuing delay (the part of the stop-line delay that includes
 stopped delay and queue move-up delay)
 dqm: Queue move-up delay
 di: Stopped delay (stopped (idling) time at near-zero speed)
 dig: Geometric delay
 dic: Control delay

```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Queues
Site:BA 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE QUEUES (VEHICLES)

 --------------------------------------------------------------------------------------------
 Deg. Prog. Ovrfl. Back of Queue (veh) Queue Prob. P'ile Cyc-Av. Queue
 Lane Satn Factor Queue ------------------------- Stor. Block Block ------------
 No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 --------------------------------------------------------------------------------------------
 South: C Cementerio

 1 0.169 1.000 0.0 0.4 0.0 0.4 1.1 0.02 0.0 100.0 0.1 0.2

 --------------------------------------------------------------------------------------------
 North: C Cementerio

 --------------------------------------------------------------------------------------------
 West: Las Catalpas
 1 0.096 1.000 0.0 0.1 0.0 0.1 0.3 0.00 0.0 100.0 0.1 0.1

 --------------------------------------------------------------------------------------------
 LANE QUEUES (DISTANCE)

 --------------------------------------------------------------------------------------------
 Deg. Prog. Ovrfl. Back of Queue (m) Queue Prob. P'ile Cyc-Av. Queue
 Lane Satn Factor Queue ------------------------- Stor. Block Block ------------
 No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 --------------------------------------------------------------------------------------------
 South: C Cementerio

 1 0.169 1.000 0.0 3.4 0.0 3.4 8.4 0.02 0.0 100.0 0.9 1.7

 --------------------------------------------------------------------------------------------
 North: C Cementerio

 --------------------------------------------------------------------------------------------
 West: Las Catalpas
 1 0.096 1.000 0.0 1.0 0.0 1.0 2.4 0.00 0.0 100.0 0.4 0.7

 --------------------------------------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Queue Percentiles
Site:BA 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE QUEUE PERCENTILES (VEHICLES)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (veh)

 Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 South: C Cementerio

 1 0.169 0.4 0.6 0.8 0.9 1.1 1.2 1.3

 -------------------------------------------------------------
 North: C Cementerio

 -------------------------------------------------------------
 West: Las Catalpas
 1 0.096 0.1 0.2 0.2 0.3 0.3 0.4 0.4

 -------------------------------------------------------------
```

```
 LANE QUEUE PERCENTILES (DISTANCE)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (metres)

 Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 South: C Cementerio

 1 0.169 3.4 4.4 6.2 7.1 8.4 9.3 10.0

 -------------------------------------------------------------
 North: C Cementerio

 -------------------------------------------------------------
 West: Las Catalpas
 1 0.096 1.0 1.3 1.8 2.1 2.4 2.7 2.9

 -------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Stops
Site:BA 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -----------------------------------------------------------------------------
 Queue Total
 Deg. Prog. -- Effective Stop Rate -- Total Move-up Queue Prop.
 Lane Satn Factor Geom. Overall Stops Rate Move-ups Queued
 No. x he1 he2 hig h H hqm Hqm pq

 -----------------------------------------------------------------------------
 South: C Cementerio

 1 0.169 1.000 0.07 0.00 0.13 0.21 58.4 0.00 0.0 0.48

 -----------------------------------------------------------------------------
 North: C Cementerio

 1 0.184 1.000 0.27 0.27 90.7

 -----------------------------------------------------------------------------
 West: Las Catalpas
 1 0.096 1.000 0.35 0.00 0.51 0.86 61.4 0.00 0.0 0.43

 -----------------------------------------------------------------------------
 hig is the average value for all movements in a shared lane
 hqm is average queue move-up rate for all vehicles queued and unqueued

```

[Go to Table Links (Top)](about:blank#tablelinks)

**Flow Rates**

Origin-Destination Flow Rates (Total)
Site:BA 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 TOTAL FLOW RATES (ALL MOVEMENT CLASSES)

 --------------------------------------------------
 From SOUTH To: W N

 Turn: L2 T1 TOT

 Flow Rate 58.9 220.0 278.9

 %HV (all designations) 8.9 9.1 9.1

 --------------------------------------------------
```

```
 From NORTH To: S W

 Turn: T1 R2 TOT

 Flow Rate 255.8 85.3 341.1

 %HV (all designations) 6.6 2.5 5.6

 --------------------------------------------------
 From WEST To: N S

 Turn: L2 R2 TOT

 Flow Rate 37.9 33.7 71.6

 %HV (all designations) 5.6 3.1 4.4

 --------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Origin-Destination Flow Rates by Movement Class
Site:BA 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 FLOW RATES FOR Light Vehicles

 ------------------------------------------
 From SOUTH To: W N

 Turn: L2 T1 TOT

 ------------------------------------------
 Flow Rate - Veh 53.7 200.0 253.7

 Mov Class % 91.1 90.9 90.9

 Flow Scale - Fixed 1.00 1.00

 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
 From NORTH To: S W

 Turn: T1 R2 TOT

 ------------------------------------------
 Flow Rate - Veh 238.9 83.2 322.1

 Mov Class % 93.4 97.5 94.4

 Flow Scale - Fixed 1.00 1.00

 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
 From WEST To: N S

 Turn: L2 R2 TOT

 ------------------------------------------
 Flow Rate - Veh 35.8 32.6 68.4

 Mov Class % 94.4 96.9 95.6

 Flow Scale - Fixed 1.00 1.00

 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
 FLOW RATES FOR Heavy Vehicles

 ------------------------------------------
 From SOUTH To: W N

 Turn: L2 T1 TOT

 ------------------------------------------
 Flow Rate - Veh 5.3 20.0 25.3

 Mov Class % 8.9 9.1 9.1

 Flow Scale - Fixed 1.00 1.00

 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
 From NORTH To: S W

 Turn: T1 R2 TOT

 ------------------------------------------
 Flow Rate - Veh 16.8 2.1 18.9

 Mov Class % 6.6 2.5 5.6

 Flow Scale - Fixed 1.00 1.00

```

```
 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
 From WEST To: N S

 Turn: L2 R2 TOT

 ------------------------------------------
 Flow Rate - Veh 2.1 1.1 3.2

 Mov Class % 5.6 3.1 4.4

 Flow Scale - Fixed 1.00 1.00

 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Flow Rates

Site:BA 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE FLOW RATES AT STOP LINE

 ----------------------------------------
 From SOUTH To: W N

 Turn: L2 T1 TOT

 ----------------------------------------
 Lane 1

 LV 53.7 200.0 253.7

 HV 5.3 20.0 25.3

 Total 58.9 220.0 278.9

 ----------------------------------------
 Approach 58.9 220.0 278.9

 ----------------------------------------
 From NORTH To: S W

 Turn: T1 R2 TOT

 ----------------------------------------
 Lane 1

 LV 238.9 83.2 322.1

 HV 16.8 2.1 18.9

 Total 255.8 85.3 341.1

 ----------------------------------------
 Approach 255.8 85.3 341.1

 ----------------------------------------
 From WEST To: N S

 Turn: L2 R2 TOT

 ----------------------------------------
 Lane 1

 LV 35.8 32.6 68.4

 HV 2.1 1.1 3.2

 Total 37.9 33.7 71.6

 ----------------------------------------
 Approach 37.9 33.7 71.6

 ----------------------------------------
 EXIT LANE FLOW RATES

 ----------------------------------------
 Movement Class: LV HV TOT

 ----------------------------------------
 Exit: SOUTH

 Lane: 1 271.6 17.9 289.5

 Total 271.6 17.9 289.5

 ----------------------------------------
 Exit: NORTH

 Lane: 1 235.8 22.1 257.9

 Total 235.8 22.1 257.9

```

```
 ----------------------------------------
 Exit: WEST

 Lane: 1 136.8 7.4 144.2

 Total 136.8 7.4 144.2

 ----------------------------------------
 DOWNSTREAM LANE FLOW RATES FOR EXIT ROADS

 ----------------------------------------
 Movement Class: LV HV TOT

 ----------------------------------------
 Exit: SOUTH

 Lane: 1 271.6 17.9 289.5

 Total 271.6 17.9 289.5

 ----------------------------------------
 Exit: NORTH

 Lane: 1 235.8 22.1 257.9

 Total 235.8 22.1 257.9

 ----------------------------------------
 Exit: WEST

 Lane: 1 136.8 7.4 144.2

 Total 136.8 7.4 144.2

 ----------------------------------------
 Unit Time for Volumes = 60 minutes

 Peak Flow Period = 30 minutes

 Flow Rates include effects of Flow Scale and Peak Flow Factor

```

[Go to Table Links (Top)](about:blank#tablelinks)

**Other**

Model Settings Summary
Site:BA 2023

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

[Go to Table Links (Top)](about:blank#tablelinks)

Diagnostics
Site:BA 2023

[Go to Table Links (Top)](about:blank#tablelinks)

# Situación con Proyecto (2023)

## DETAILED OUTPUT

**Site: CP 2023**

New Site
Stop (Two-Way)

**OUTPUT TABLE LINKS**

**Movements**

Intersection Negotiation Data
Site:CP 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 INTERSECTION NEGOTIATION DATA

 ----------------------------------------------------------------------------
 Negn Negn Negn Appr. Downstream Distance
 From To Radius Speed Dist. Dist. ------------------- Approach Exit Turn m km/h m m m User Spec?

 ----------------------------------------------------------------------------
 South: C Cementerio

 West L2 6.6 17.2 10.4 200 161 No

 North T1 S 60.0 10.0 200 374 No

 ----------------------------------------------------------------------------
 North: C Cementerio

 South T1 S 60.0 10.0 200 340 No

 West R2 10.0 20.2 15.7 200 193 No

 ----------------------------------------------------------------------------
```

```
 West: Las Catalpas
 North L2 6.6 17.2 10.4 200 322 No

 South R2 10.0 20.2 15.7 200 168 No

 ----------------------------------------------------------------------------
 Downstream distance is distance travelled from the stopline until exit
 cruise speed is reached (includes negotiation distance). Acceleration
 distance is weighted for light and heavy vehicles. The same distance
 applies for both stopped and unstopped vehicles.

 MOVEMENT SPEEDS AND GEOMETRIC DELAY

 ----------------------------------------------------------------------------
 Queue Move-up
 App. Speeds Exit Speeds ------------- Av. Section Spd Geom
 Mov Turn ------------ ----------- 1st 2nd --------------- Delay
 ID Cruise Negn Negn Cruise Grn Grn Running Overall sec

 ----------------------------------------------------------------------------
 South: C Cementerio

 1 L2 60.0 17.2 17.2 60.0 4.7 42.6 42.6 9.6

 2 T1 60.0 60.0 60.0 60.0 4.7 42.6 42.6 0.0

 ----------------------------------------------------------------------------
 North: C Cementerio

 8 T1 60.0 60.0 60.0 60.0 53.1 53.1 0.0

 9 R2 60.0 20.2 20.2 60.0 53.1 53.1 9.2

 ----------------------------------------------------------------------------
 West: Las Catalpas
 10 L2 60.0 0.0 17.2 60.0 16.5 38.0 35.0 11.6

 12 R2 60.0 0.0 20.2 60.0 16.5 38.0 35.0 11.6

 ----------------------------------------------------------------------------
 "Running Speed" is the average speed excluding stopped periods.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Gap Acceptance Parameters
Site:CP 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -------------------------------------------------------------------------
 Critical Gap Intra
 Opng ------------ Foll-up Entry Bunch Propn
 Opd Dest Flow Hdwy Dist Headway HV Hdwy Bnchd
 Lane pcu/h sec m sec Equiv sec

 -------------------------------------------------------------------------
 South: C Cementerio

 1 W 380 4.18 55.8 2.09 1.04 1.80 0.045

 -------------------------------------------------------------------------
 North: C Cementerio

 No opposed movements on this approach.

 -------------------------------------------------------------------------
 West: Las Catalpas
 1 S 264+ 4.57 76.2 2.54 1.02 1.80 0.030

 1 N 614+ 5.29 81.2 3.42 1.10 0.94 0.037

 -------------------------------------------------------------------------
 Values in this table are adjusted for heavy vehicles in the entry stream.
 Use the Pedestrians and Priorities input dialogs to specify opposing pedestrian movements.
 + Percentage of exiting flow included in opposing vehicle flow

```

[Go to Table Links (Top)](about:blank#tablelinks)

Movement Capacity and Performance Parameters
Site:CP 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 MOVEMENT CAPACITY PARAMETERS

 --------------------------------------------------------------
 Mov Turn Mov Opng Movement Total Prac. Prac. Deg.
 ID Cl. Arv Adjust. Cap. Deg. Spare Satn
 Flow Flow Flow Satn Cap.
 veh/h veh/h pcu/h veh/h xp % x

 --------------------------------------------------------------
 South: C Cementerio

 1 L2 # 59 365 380 344 0.98 473 0.171

 2 T1 # 220 0 0 1286 0.98 473 0.171

 --------------------------------------------------------------
 North: C Cementerio

 8 T1 # 256 0 0 1275 0.98 389 0.201*

 9 R2 # 109 0 0 546 0.98 389 0.201*

 --------------------------------------------------------------
 West: Las Catalpas
 10 L2 # 62 589 614 403 0.80 419 0.154

 12 R2 # 34 256 264 219 0.80 419 0.154

 --------------------------------------------------------------
 * Maximum degree of saturation
 # Combined Movement Capacity parameters are shown for all Movement Classes.

 MOVEMENT PERFORMANCE

 -------------------------------------------------------------------------------
 Mov Turn Total Total Aver. Eff. Total Perf. Tot.Trav. Tot.Trav. Aver.

 ID Delay Delay Delay Stop Stops Index Distance Time Speed
 (veh-h/h)(pers-h/h)(sec) Rate (veh-km/h)(veh-h/h) (km/h)

 -------------------------------------------------------------------------------
 South: C Cementerio

 1 L2 0.19 0.22 11.3 0.21 12.4 0.59 20.0 0.5 42.6

 2 T1 0.11 0.13 1.8 0.21 46.2 1.61 74.5 1.8 42.6

 -------------------------------------------------------------------------------
 North: C Cementerio

 8 T1 0.00 0.00 0.0 0.29 73.8 1.86 86.7 1.6 53.1

 9 R2 0.28 0.33 9.2 0.29 31.6 1.07 37.1 0.7 53.1

 -------------------------------------------------------------------------------
 West: Las Catalpas
 10 L2 0.26 0.32 15.2 0.80 49.6 1.32 20.8 0.6 35.0

 12 R2 0.14 0.17 15.3 0.80 26.9 0.92 11.3 0.3 35.0

 -------------------------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Fuel Consumption, Emissions and Cost
Site:CP 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 FUEL CONSUMPTION, EMISSIONS AND COST (TOTAL)

 --------------------------------------------------------------
 Mov Turn Cost Fuel CO2 CO HC NOX

 ID Total Total Total Total Total Total
 $/h L/h kg/h kg/h kg/h kg/h

 --------------------------------------------------------------
 South: C Cementerio

 1 L2 20.19 2.4 5.8 0.01 0.001 0.026

 2 T1 75.34 9.1 21.6 0.05 0.005 0.095

```

```
 -----------------------------------------------
 95.53 11.5 27.4 0.06 0.007 0.121

 --------------------------------------------------------------
 North: C Cementerio

 8 T1 76.12 9.5 22.5 0.05 0.005 0.097

 9 R2 32.58 4.1 9.6 0.02 0.002 0.041

 -----------------------------------------------
 108.70 13.5 32.1 0.07 0.007 0.138

 --------------------------------------------------------------
 West: Las Catalpas
 10 L2 30.74 3.9 9.2 0.02 0.002 0.045

 12 R2 16.67 2.1 5.0 0.01 0.001 0.025

 -----------------------------------------------
 47.41 5.9 14.2 0.03 0.003 0.070

 --------------------------------------------------------------
 INTERSECTION: 251.64 31.0 73.7 0.16 0.017 0.329

 -------------------------------------------------------------
 FUEL CONSUMPTION, EMISSIONS AND COST (RATE)

 --------------------------------------------------------------
 Mov Turn Cost Fuel CO2 CO HC NOX

 ID Rate Rate Rate Rate Rate Rate
 $/km L/100km g/km g/km g/km g/km

 --------------------------------------------------------------
 South: C Cementerio

 1 L2 1.01 12.2 289.9 0.65 0.070 1.279

 2 T1 1.01 12.2 289.9 0.65 0.070 1.279

 -----------------------------------------------
 1.01 12.2 289.9 0.65 0.070 1.279

 --------------------------------------------------------------
 North: C Cementerio

 8 T1 0.88 10.9 259.3 0.58 0.060 1.117

 9 R2 0.88 10.9 259.3 0.58 0.060 1.117

 -----------------------------------------------
 0.88 10.9 259.3 0.58 0.060 1.117

 --------------------------------------------------------------
 West: Las Catalpas
 10 L2 1.48 18.5 442.3 0.94 0.104 2.182

 12 R2 1.48 18.5 442.3 0.94 0.104 2.182

 -----------------------------------------------
 1.48 18.5 442.3 0.94 0.104 2.182

 --------------------------------------------------------------
 INTERSECTION: 0.84 10.3 245.3 0.54 0.058 1.096

 -------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

**Lanes**

Lane Performance and Capacity Information
Site:CP 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE PERFORMANCE

 --------------------------------------------------------------
 Q u e u e
 Flow Cap Deg. Aver. Eff. 95% Back Lane
 Lane Satn Delay Stop ------------ Length
 No. veh/h veh/h x sec Rate veh m m

 --------------------------------------------------------------
 South: C Cementerio

```

```
 1 279 1630 0.171 3.8 0.21 1.1 8.6 200.0

 --------------------------------------------------------------
 North: C Cementerio

 1 365 1821 0.201 2.8 0.29 200.0

 --------------------------------------------------------------
 West: Las Catalpas
 1 96 621 0.154 15.3 0.80 0.5 4.2 200.0

 --------------------------------------------------------------
 LANE FLOW AND CAPACITY INFORMATION

 ----------------------------------------
 Lane Total Min Tot Deg. Lane
 No. Arv Flow Cap Cap Satn Util
 (veh/h) veh/h veh/h x %

 ----------------------------------------
 South: C Cementerio

 1 279 28 1630 0.171 100

 ----------------------------------------
 North: C Cementerio

 1 365 365 1821 0.201 100

 ----------------------------------------
 West: Las Catalpas
 1 96 6 621 0.154 100

 ----------------------------------------
 The capacity value for priority and continuous movements is obtained by
 adjusting the basic saturation flow for heavy vehicle and turning vehicle
 effects. Saturation flow scale applies if specified.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane, Approach and Intersection Performance
Site:CP 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -----------------------------------------------------------
 Lane Demand Adj. Deg Aver. Longest Shrt
 No. Flow %HV Basic Sat Delay Queue Lane
 (veh/h) Satf. x sec m m

 -----------------------------------------------------------
 South: C Cementerio

 1 279 9 0.171 3.8 9 200

 ---------------------------------------------------
 279 9 0.171 3.8 9

 -----------------------------------------------------------
 North: C Cementerio

 1 365 8 1950 0.201 2.8 200

 ---------------------------------------------------
 365 8 0.201 2.8

 -----------------------------------------------------------
 West: Las Catalpas
 1 96 14 0.154 15.3 4 200

 ---------------------------------------------------
 96 14 0.154 15.3 4

 ============================================================

 ALL VEHICLES

 Total % Max Aver. Max

 Flow HV X Delay Queue
 740 9 0.201 4.8 9

 ============================================================

 Peak flow period = 30 minutes.

 Queue values in this table are 95% queue (metres)
 Note: Basic Saturation Flows are not adjusted at roundabouts or sign controlled intersections and apply only to continuous lanes.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Driver Characteristics

Site:CP 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -------------------------------------------------------
 Average Driver
 Lane Satn Satn Satn Satn Queue Response
 No. Speed Flow Hdwy Spacing Space Time
 km/h veh/h sec m m sec

 -------------------------------------------------------
 South: C Cementerio

 1 NA - Major Road Movement

 -------------------------------------------------------
 North: C Cementerio

 1 NA - Continuous Movement

 -------------------------------------------------------
 West: Las Catalpas
 1 18.3 1159 3.11 15.75 7.86 1.56

 -------------------------------------------------------
 Saturation Flow and Saturation Headway are derived from follow-up headway.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Delays
Site:CP 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE DELAYS

 -----------------------------------------------------------------------------
 ---------------- Delay (seconds/veh) --------------- Deg. Prog. Stop-line Delay Acc. Queuing Stopd
 Lane Satn Factor 1st 2nd Total Dec. Total MvUp (Idle) Geom Control
 No. x d1 d2 dSL dn dq dqm di dig dic

 -----------------------------------------------------------------------------
 South: C Cementerio

 1 0.171 1.000 1.8 0.0 1.8 4.3 0.0 0.0 0.0 2.0 3.8

 -----------------------------------------------------------------------------
 North: C Cementerio

 1 0.201 0.0 2.7 2.8

 -----------------------------------------------------------------------------
 West: Las Catalpas

 1 0.154 1.000 3.7 0.0 3.7 0.9 2.7 0.0 2.7 11.6 15.3

 -----------------------------------------------------------------------------
 SIDRA Standard Delay Model is used. Control Delay is the sum of Stop-line Delay
 and Geometric Delay.
 dSL: Stop-line delay (=d1+d2)
 dn: Average stop-start delay for all vehicles queued and unqueued
 dq: Queuing delay (the part of the stop-line delay that includes
 stopped delay and queue move-up delay)
 dqm: Queue move-up delay
 di: Stopped delay (stopped (idling) time at near-zero speed)
 dig: Geometric delay
 dic: Control delay

```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Queues
Site:CP 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE QUEUES (VEHICLES)

 --------------------------------------------------------------------------------------------
 Deg. Prog. Ovrfl. Back of Queue (veh) Queue Prob. P'ile Cyc-Av. Queue
 Lane Satn Factor Queue ------------------------- Stor. Block Block ------------
 No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 --------------------------------------------------------------------------------------------
 South: C Cementerio

 1 0.171 1.000 0.0 0.5 0.0 0.5 1.1 0.02 0.0 100.0 0.1 0.2

 --------------------------------------------------------------------------------------------
 North: C Cementerio

 --------------------------------------------------------------------------------------------
 West: Las Catalpas
 1 0.154 1.000 0.0 0.2 0.0 0.2 0.5 0.01 0.0 100.0 0.1 0.2

 --------------------------------------------------------------------------------------------
 LANE QUEUES (DISTANCE)

 --------------------------------------------------------------------------------------------
 Deg. Prog. Ovrfl. Back of Queue (m) Queue Prob. P'ile Cyc-Av. Queue
 Lane Satn Factor Queue ------------------------- Stor. Block Block ------------
 No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 --------------------------------------------------------------------------------------------
 South: C Cementerio

 1 0.171 1.000 0.0 3.5 0.0 3.5 8.6 0.02 0.0 100.0 1.0 1.9

 --------------------------------------------------------------------------------------------
 North: C Cementerio

 --------------------------------------------------------------------------------------------
 West: Las Catalpas
 1 0.154 1.000 0.0 1.7 0.0 1.7 4.2 0.01 0.0 100.0 0.8 1.4

 --------------------------------------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Queue Percentiles
Site:CP 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE QUEUE PERCENTILES (VEHICLES)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (veh)

 Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 South: C Cementerio

 1 0.171 0.5 0.6 0.8 1.0 1.1 1.3 1.4

 -------------------------------------------------------------
 North: C Cementerio

 -------------------------------------------------------------
 West: Las Catalpas
 1 0.154 0.2 0.3 0.4 0.5 0.5 0.6 0.6

 -------------------------------------------------------------
```

```
 LANE QUEUE PERCENTILES (DISTANCE)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (metres)

 Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 South: C Cementerio

 1 0.171 3.5 4.5 6.3 7.3 8.6 9.6 10.3

 -------------------------------------------------------------
 North: C Cementerio

 -------------------------------------------------------------
 West: Las Catalpas
 1 0.154 1.7 2.2 3.1 3.6 4.2 4.7 5.1

 -------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Stops
Site:CP 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -----------------------------------------------------------------------------
 Queue Total
 Deg. Prog. -- Effective Stop Rate -- Total Move-up Queue Prop.
 Lane Satn Factor Geom. Overall Stops Rate Move-ups Queued
 No. x he1 he2 hig h H hqm Hqm pq

 -----------------------------------------------------------------------------
 South: C Cementerio

 1 0.171 1.000 0.08 0.00 0.13 0.21 58.6 0.00 0.0 0.50

 -----------------------------------------------------------------------------
 North: C Cementerio

 1 0.201 1.000 0.29 0.29 105.4

 -----------------------------------------------------------------------------
 West: Las Catalpas
 1 0.154 1.000 0.42 0.00 0.38 0.80 76.6 0.00 0.0 0.48

 -----------------------------------------------------------------------------
 hig is the average value for all movements in a shared lane
 hqm is average queue move-up rate for all vehicles queued and unqueued

```

[Go to Table Links (Top)](about:blank#tablelinks)

**Flow Rates**

Origin-Destination Flow Rates (Total)
Site:CP 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 TOTAL FLOW RATES (ALL MOVEMENT CLASSES)

 --------------------------------------------------
 From SOUTH To: W N

 Turn: L2 T1 TOT

 Flow Rate 58.9 220.0 278.9

 %HV (all designations) 8.9 9.1 9.1

 --------------------------------------------------
```

```
 From NORTH To: S W

 Turn: T1 R2 TOT

 Flow Rate 255.8 109.5 365.3

 %HV (all designations) 6.6 11.5 8.1

 --------------------------------------------------
 From WEST To: N S

 Turn: L2 R2 TOT

 Flow Rate 62.1 33.7 95.8

 %HV (all designations) 20.3 3.1 14.3

 --------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Origin-Destination Flow Rates by Movement Class
Site:CP 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 FLOW RATES FOR Light Vehicles

 ------------------------------------------
 From SOUTH To: W N

 Turn: L2 T1 TOT

 ------------------------------------------
 Flow Rate - Veh 53.7 200.0 253.7

 Mov Class % 91.1 90.9 90.9

 Flow Scale - Fixed 1.00 1.00

 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
 From NORTH To: S W

 Turn: T1 R2 TOT

 ------------------------------------------
 Flow Rate - Veh 238.9 96.8 335.8

 Mov Class % 93.4 88.5 91.9

 Flow Scale - Fixed 1.00 1.00

 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
 From WEST To: N S

 Turn: L2 R2 TOT

 ------------------------------------------
 Flow Rate - Veh 49.5 32.6 82.1

 Mov Class % 79.7 96.9 85.7

 Flow Scale - Fixed 1.00 1.00

 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
 FLOW RATES FOR Heavy Vehicles

 ------------------------------------------
 From SOUTH To: W N

 Turn: L2 T1 TOT

 ------------------------------------------
 Flow Rate - Veh 5.3 20.0 25.3

 Mov Class % 8.9 9.1 9.1

 Flow Scale - Fixed 1.00 1.00

 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
 From NORTH To: S W

 Turn: T1 R2 TOT

 ------------------------------------------
 Flow Rate - Veh 16.8 12.6 29.5

 Mov Class % 6.6 11.5 8.1

 Flow Scale - Fixed 1.00 1.00

```

```
 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
 From WEST To: N S

 Turn: L2 R2 TOT

 ------------------------------------------
 Flow Rate - Veh 12.6 1.1 13.7

 Mov Class % 20.3 3.1 14.3

 Flow Scale - Fixed 1.00 1.00

 Flow Scale - Var 1.00 1.00

 Peak Flow Factor 0.95 0.95

 ------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Flow Rates

Site:CP 2023

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE FLOW RATES AT STOP LINE

 ----------------------------------------
 From SOUTH To: W N

 Turn: L2 T1 TOT

 ----------------------------------------
 Lane 1

 LV 53.7 200.0 253.7

 HV 5.3 20.0 25.3

 Total 58.9 220.0 278.9

 ----------------------------------------
 Approach 58.9 220.0 278.9

 ----------------------------------------
 From NORTH To: S W

 Turn: T1 R2 TOT

 ----------------------------------------
 Lane 1

 LV 238.9 96.8 335.8

 HV 16.8 12.6 29.5

 Total 255.8 109.5 365.3

 ----------------------------------------
 Approach 255.8 109.5 365.3

 ----------------------------------------
 From WEST To: N S

 Turn: L2 R2 TOT

 ----------------------------------------
 Lane 1

 LV 49.5 32.6 82.1

 HV 12.6 1.1 13.7

 Total 62.1 33.7 95.8

 ----------------------------------------
 Approach 62.1 33.7 95.8

 ----------------------------------------
 EXIT LANE FLOW RATES

 ----------------------------------------
 Movement Class: LV HV TOT

 ----------------------------------------
 Exit: SOUTH

 Lane: 1 271.6 17.9 289.5

 Total 271.6 17.9 289.5

 ----------------------------------------
 Exit: NORTH

 Lane: 1 249.5 32.6 282.1

 Total 249.5 32.6 282.1

```

```
 ----------------------------------------
 Exit: WEST

 Lane: 1 150.5 17.9 168.4

 Total 150.5 17.9 168.4

 ----------------------------------------
 DOWNSTREAM LANE FLOW RATES FOR EXIT ROADS

 ----------------------------------------
 Movement Class: LV HV TOT

 ----------------------------------------
 Exit: SOUTH

 Lane: 1 271.6 17.9 289.5

 Total 271.6 17.9 289.5

 ----------------------------------------
 Exit: NORTH

 Lane: 1 249.5 32.6 282.1

 Total 249.5 32.6 282.1

 ----------------------------------------
 Exit: WEST

 Lane: 1 150.5 17.9 168.4

 Total 150.5 17.9 168.4

 ----------------------------------------
 Unit Time for Volumes = 60 minutes

 Peak Flow Period = 30 minutes

 Flow Rates include effects of Flow Scale and Peak Flow Factor

```

[Go to Table Links (Top)](about:blank#tablelinks)

**Other**

Model Settings Summary
Site:CP 2023

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

[Go to Table Links (Top)](about:blank#tablelinks)

Diagnostics
Site:CP 2023

[Go to Table Links (Top)](about:blank#tablelinks)