---
title: Sin título
author: DEZ
date: D:20210405010623-04'00'
language: en
type: general
pages: 41
has_toc: False
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO SALIDAS MODELO SIDRA
-->

# ANEXO SALIDAS MODELO SIDRA

Proyecto: Extracción de Áridos, Rinconada Los Maitenes.

## Contenido

1. Situación Actual Punta Tarde ...................................................................................................... 2

2. Situación Base Punta Tarde ....................................................................................................... 16

3. Situación Con Proyecto Punta Tarde ......................................................................................... 29

## 1. Situación Actual Punta Tarde

### DETAILED OUTPUT

**Site: AC**

Planta Áridos Los Maitenes
Stop (Two-Way)

**OUTPUT TABLE LINKS**

**Movements**

Intersection Negotiation Data
Site:AC

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 INTERSECTION NEGOTIATION DATA

 ----------------------------------------------------------------------------
 Negn Negn Negn Appr. Downstream Distance
 From To Radius Speed Dist. Dist. ------------------- Approach Exit Turn m km/h m m m User Spec?

 ----------------------------------------------------------------------------
 South: K-25

 West L2 6.6 17.2 10.4 500 82 No

 North T1 S 60.0 10.0 500 339 No

 East R2 10.0 20.2 15.7 500 88 No

```

```
 ----------------------------------------------------------------------------
 East: Proyecto
 South L2 6.6 17.2 10.4 500 99 No

 West T1 S 20.0 10.0 500 101 No

 North R2 10.0 20.2 15.7 500 105 No

 ----------------------------------------------------------------------------
 North: K-25

 East L2 6.6 17.2 10.4 500 85 No

 South T1 S 60.0 10.0 500 457 No

 West R2 10.0 20.2 15.7 500 91 No

 ----------------------------------------------------------------------------
 West: Acceso Part.

 North L2 6.6 17.2 10.4 500 99 No

 East T1 S 20.0 10.0 500 101 No

 South R2 10.0 20.2 15.7 500 105 No

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
 South: K-25

 1 L2 60.0 17.2 17.2 60.0 0.5 55.2 55.2 9.6

 2 T1 60.0 60.0 60.0 60.0 0.5 55.2 55.2 0.0

 3 R2 60.0 20.2 20.2 60.0 0.5 55.2 55.2 9.2

 ----------------------------------------------------------------------------
 East: Proyecto
 4 L2 60.0 0.0 17.2 60.0 19.4 46.5 46.3 10.4

 5 T1 60.0 0.0 20.0 60.0 19.4 46.5 46.3 10.2

 6 R2 60.0 0.0 20.2 60.0 19.4 46.5 46.3 10.7

 ----------------------------------------------------------------------------
 North: K-25

 7 L2 60.0 17.2 17.2 60.0 2.1 54.9 54.9 9.6

 8 T1 60.0 60.0 60.0 60.0 2.1 54.9 54.9 0.0

 9 R2 60.0 20.2 20.2 60.0 2.1 54.9 54.9 9.2

 ----------------------------------------------------------------------------
 West: Acceso Part.

 10 L2 60.0 0.0 17.2 60.0 19.4 46.5 46.3 10.4

 11 T1 60.0 0.0 20.0 60.0 19.4 46.5 46.3 10.2

 12 R2 60.0 0.0 20.2 60.0 19.4 46.5 46.3 10.7

 ----------------------------------------------------------------------------
 "Running Speed" is the average speed excluding stopped periods.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Gap Acceptance Parameters
Site:AC

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -------------------------------------------------------------------------
 Critical Gap Intra
 Opng ------------ Foll-up Entry Bunch Propn
 Opd Dest Flow Hdwy Dist Headway HV Hdwy Bnchd
 Lane pcu/h sec m sec Equiv sec

 -------------------------------------------------------------------------
 South: K-25

```

```
 1 W 107 4.00 66.2 2.00 1.00 1.80 0.011

 -------------------------------------------------------------------------
 East: Proyecto
 1 S 217+ 5.50 89.0 3.50 1.00 0.89 0.017

 1 N 102+ 4.50 75.0 2.50 1.00 1.80 0.011

 1 W 215+ 5.00 81.5 3.00 1.00 0.92 0.012

 -------------------------------------------------------------------------
 North: K-25

 1 E 103 4.00 66.2 2.00 1.00 1.80 0.011

 -------------------------------------------------------------------------
 West: Acceso Part.

 1 S 106+ 4.50 75.0 2.50 1.00 1.80 0.011

 1 E 215+ 5.00 81.5 3.00 1.00 0.92 0.011

 1 N 217+ 5.50 89.0 3.50 1.00 0.90 0.017

 -------------------------------------------------------------------------
 Values in this table are adjusted for heavy vehicles in the entry stream.
 Use the Pedestrians and Priorities input dialogs to specify opposing pedestrian movements.
 + Percentage of exiting flow included in opposing vehicle flow

```

[Go to Table Links (Top)](about:blank#tablelinks)

Movement Capacity and Performance Parameters
Site:AC

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
 South: K-25

 1 L2 # 1 99 107 19 0.98 1708 0.054

 2 T1 # 98 0 0 1806 0.98 1708 0.054

 3 R2 # 1 0 0 19 0.98 1708 0.054

 --------------------------------------------------------------
 East: Proyecto
 4 L2 # 1 205 217 263 0.80 **** 0.004

 5 T1 # 1 203 215 263 0.80 **** 0.004

 6 R2 # 2 98 102 526 0.80 **** 0.004

 --------------------------------------------------------------
 North: K-25

 7 L2 # 4 99 103 72 0.98 1576 0.058*

 8 T1 # 98 0 0 1674 0.98 1576 0.058*

 9 R2 # 1 0 0 18 0.98 1576 0.058*

 --------------------------------------------------------------
 West: Acceso Part.

 10 L2 # 1 205 217 262 0.80 **** 0.004

 11 T1 # 1 203 215 262 0.80 **** 0.004

 12 R2 # 2 98 106 525 0.80 **** 0.004

 --------------------------------------------------------------
 * Maximum degree of saturation
 # Combined Movement Capacity parameters are shown for all Movement Classes.

 MOVEMENT PERFORMANCE

 -------------------------------------------------------------------------------
 Mov Turn Total Total Aver. Eff. Total Perf. Tot.Trav. Tot.Trav. Aver.

 ID Delay Delay Delay Stop Stops Index Distance Time Speed
 (veh-h/h)(pers-h/h)(sec) Rate (veh-km/h)(veh-h/h) (km/h)

 -------------------------------------------------------------------------------
```

```
 South: K-25

 1 L2 0.00 0.00 9.9 0.02 0.0 0.01 0.7 0.0 55.2

 2 T1 0.01 0.01 0.3 0.02 2.4 1.07 62.7 1.1 55.2

 3 R2 0.00 0.00 9.5 0.02 0.0 0.01 0.7 0.0 55.2

 -------------------------------------------------------------------------------
 East: Proyecto
 4 L2 0.00 0.00 11.1 0.86 0.9 0.02 0.6 0.0 46.3

 5 T1 0.00 0.00 10.9 0.86 0.9 0.02 0.6 0.0 46.3

 6 R2 0.01 0.01 11.4 0.86 1.8 0.04 1.3 0.0 46.3

 -------------------------------------------------------------------------------
 North: K-25

 7 L2 0.01 0.01 9.9 0.06 0.3 0.06 2.7 0.0 54.9

 8 T1 0.01 0.01 0.3 0.06 6.0 1.09 62.6 1.1 54.9

 9 R2 0.00 0.00 9.5 0.06 0.1 0.01 0.7 0.0 54.9

 -------------------------------------------------------------------------------
 West: Acceso Part.

 10 L2 0.00 0.00 11.2 0.86 0.9 0.02 0.6 0.0 46.3

 11 T1 0.00 0.00 10.9 0.86 0.9 0.02 0.6 0.0 46.3

 12 R2 0.01 0.01 11.4 0.86 1.8 0.04 1.3 0.0 46.3

 -------------------------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Fuel Consumption, Emissions and Cost
Site:AC

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 FUEL CONSUMPTION, EMISSIONS AND COST (TOTAL)

 --------------------------------------------------------------
 Mov Turn Cost Fuel CO2 CO HC NOX

 ID Total Total Total Total Total Total
 $/h L/h kg/h kg/h kg/h kg/h

 --------------------------------------------------------------
 South: K-25

 1 L2 0.49 0.1 0.1 0.00 0.000 0.001

 2 T1 45.44 5.2 12.4 0.03 0.003 0.047

 3 R2 0.49 0.1 0.1 0.00 0.000 0.001

 -----------------------------------------------
 46.41 5.3 12.7 0.03 0.003 0.048

 --------------------------------------------------------------
 East: Proyecto
 4 L2 0.43 0.0 0.1 0.00 0.000 0.000

 5 T1 0.43 0.0 0.1 0.00 0.000 0.000

 6 R2 0.87 0.1 0.1 0.00 0.000 0.000

 -----------------------------------------------
 1.73 0.1 0.3 0.00 0.000 0.000

 --------------------------------------------------------------
 North: K-25

 7 L2 2.32 0.3 0.8 0.00 0.000 0.004

 8 T1 53.96 7.6 18.2 0.04 0.004 0.085

 9 R2 0.58 0.1 0.2 0.00 0.000 0.001

 -----------------------------------------------
 56.86 8.0 19.2 0.04 0.004 0.089

 --------------------------------------------------------------
 West: Acceso Part.

 10 L2 0.43 0.0 0.1 0.00 0.000 0.000

 11 T1 0.43 0.0 0.1 0.00 0.000 0.000

 12 R2 0.87 0.1 0.1 0.00 0.000 0.000

 -----------------------------------------------
 1.73 0.1 0.2 0.00 0.000 0.000

 --------------------------------------------------------------
 INTERSECTION: 106.74 13.6 32.3 0.07 0.007 0.137

 -------------------------------------------------------------
```

```
 FUEL CONSUMPTION, EMISSIONS AND COST (RATE)

 --------------------------------------------------------------
 Mov Turn Cost Fuel CO2 CO HC NOX

 ID Rate Rate Rate Rate Rate Rate
 $/km L/100km g/km g/km g/km g/km

 --------------------------------------------------------------
 South: K-25

 1 L2 0.73 8.3 198.0 0.48 0.050 0.747

 2 T1 0.73 8.3 198.0 0.48 0.050 0.747

 3 R2 0.73 8.3 198.0 0.48 0.050 0.747

 -----------------------------------------------
 0.73 8.3 198.0 0.48 0.050 0.747

 --------------------------------------------------------------
 East: Proyecto
 4 L2 0.68 4.2 98.6 0.39 0.052 0.009

 5 T1 0.68 4.2 98.6 0.39 0.052 0.009

 6 R2 0.68 4.2 98.6 0.39 0.052 0.009

 -----------------------------------------------
 0.68 4.2 98.6 0.39 0.052 0.009

 --------------------------------------------------------------
 North: K-25

 7 L2 0.86 12.1 290.6 0.59 0.057 1.353

 8 T1 0.86 12.1 290.6 0.59 0.057 1.353

 9 R2 0.86 12.1 290.6 0.59 0.057 1.353

 -----------------------------------------------
 0.86 12.1 290.6 0.59 0.057 1.353

 --------------------------------------------------------------
 West: Acceso Part.

 10 L2 0.68 4.2 98.6 0.39 0.052 0.009

 11 T1 0.68 4.2 98.6 0.39 0.052 0.009

 12 R2 0.68 4.2 98.6 0.39 0.052 0.009

 -----------------------------------------------
 0.68 4.2 98.6 0.39 0.052 0.009

 --------------------------------------------------------------
 INTERSECTION: 0.66 8.4 199.6 0.44 0.045 0.846

 -------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

**Lanes**

Lane Performance and Capacity Information
Site:AC

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
 South: K-25

 1 100 1845 0.054 0.5 0.02 0.3 2.1 500.0

 --------------------------------------------------------------
 East: Proyecto
 1 4 1051 0.004 11.2 0.86 0.0 0.1 500.0

 --------------------------------------------------------------
 North: K-25

 1 103 1764 0.058 0.8 0.06 0.3 2.3 500.0

```

```
 --------------------------------------------------------------
 West: Acceso Part.

 1 4 1050 0.004 11.2 0.86 0.0 0.1 500.0

 --------------------------------------------------------------
 LANE FLOW AND CAPACITY INFORMATION

 ----------------------------------------
 Lane Total Min Tot Deg. Lane
 No. Arv Flow Cap Cap Satn Util
 (veh/h) veh/h veh/h x %

 ----------------------------------------
 South: K-25

 1 100 100 1845 0.054 100

 ----------------------------------------
 East: Proyecto
 1 4 4 1051 0.004 100

 ----------------------------------------
 North: K-25

 1 103 103 1764 0.058 100

 ----------------------------------------
 West: Acceso Part.

 1 4 4 1050 0.004 100

 ----------------------------------------
 The capacity value for priority and continuous movements is obtained by
 adjusting the basic saturation flow for heavy vehicle and turning vehicle
 effects. Saturation flow scale applies if specified.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane, Approach and Intersection Performance
Site:AC

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -----------------------------------------------------------
 Lane Demand Adj. Deg Aver. Longest Shrt
 No. Flow %HV Basic Sat Delay Queue Lane
 (veh/h) Satf. x sec m m

 -----------------------------------------------------------
 South: K-25

 1 100 8 0.054 0.5 2 500

 ---------------------------------------------------
 100 8 0.054 0.5 2

 -----------------------------------------------------------
 East: Proyecto
 1 4 0 0.004 11.2 0 500

 ---------------------------------------------------
 4 0 0.004 11.2 0

 -----------------------------------------------------------
 North: K-25

 1 103 15 0.058 0.8 2 500

 ---------------------------------------------------
 103 15 0.058 0.8 2

 -----------------------------------------------------------
 West: Acceso Part.

 1 4 0 0.004 11.2 0 500

 ---------------------------------------------------
 4 0 0.004 11.2 0

 ============================================================

 ALL VEHICLES

 Total % Max Aver. Max

 Flow HV X Delay Queue
 212 11 0.058 1.1 2

 ============================================================

```

```
 Peak flow period = 30 minutes.

 Queue values in this table are 95% queue (metres)
 Note: Basic Saturation Flows are not adjusted at roundabouts or sign controlled intersections and apply only to continuous lanes.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Driver Characteristics

Site:AC

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -------------------------------------------------------
 Average Driver
 Lane Satn Satn Satn Satn Queue Response
 No. Speed Flow Hdwy Spacing Space Time
 km/h veh/h sec m m sec

 -------------------------------------------------------
 South: K-25

 1 NA - Major Road Movement

 -------------------------------------------------------
 East: Proyecto
 1 19.4 1252 2.88 15.48 7.00 1.58

 -------------------------------------------------------
 North: K-25

 1 NA - Major Road Movement

 -------------------------------------------------------
 West: Acceso Part.

 1 19.4 1252 2.88 15.48 7.00 1.58

 -------------------------------------------------------
 Saturation Flow and Saturation Headway are derived from follow-up headway.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Delays
Site:AC

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE DELAYS

 -----------------------------------------------------------------------------
 ---------------- Delay (seconds/veh) --------------- Deg. Prog. Stop-line Delay Acc. Queuing Stopd
 Lane Satn Factor 1st 2nd Total Dec. Total MvUp (Idle) Geom Control
 No. x d1 d2 dSL dn dq dqm di dig dic

 -----------------------------------------------------------------------------
 South: K-25

 1 0.054 1.000 0.3 0.0 0.3 2.1 0.0 0.0 0.0 0.2 0.5

 -----------------------------------------------------------------------------
 East: Proyecto
 1 0.004 1.000 0.7 0.0 0.7 0.5 0.2 0.0 0.2 10.5 11.2

 -----------------------------------------------------------------------------
 North: K-25

 1 0.058 1.000 0.3 0.0 0.3 2.0 0.0 0.0 0.0 0.5 0.8

 -----------------------------------------------------------------------------
 West: Acceso Part.

 1 0.004 1.000 0.7 0.0 0.7 0.5 0.2 0.0 0.2 10.5 11.2

 -----------------------------------------------------------------------------
```

```
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

Site:AC

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE QUEUES (VEHICLES)

 --------------------------------------------------------------------------------------------
 Deg. Prog. Ovrfl. Back of Queue (veh) Queue Prob. P'ile Cyc-Av. Queue
 Lane Satn Factor Queue ------------------------- Stor. Block Block ------------
 No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 --------------------------------------------------------------------------------------------
 South: K-25

 1 0.054 1.000 0.0 0.1 0.0 0.1 0.3 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
 East: Proyecto
 1 0.004 1.000 0.0 0.0 0.0 0.0 0.0 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
 North: K-25

 1 0.058 1.000 0.0 0.1 0.0 0.1 0.3 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
 West: Acceso Part.

 1 0.004 1.000 0.0 0.0 0.0 0.0 0.0 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
 LANE QUEUES (DISTANCE)

 --------------------------------------------------------------------------------------------
 Deg. Prog. Ovrfl. Back of Queue (m) Queue Prob. P'ile Cyc-Av. Queue
 Lane Satn Factor Queue ------------------------- Stor. Block Block ------------
 No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 --------------------------------------------------------------------------------------------
 South: K-25

 1 0.054 1.000 0.0 0.8 0.0 0.8 2.1 0.00 0.0 100.0 0.1 0.1

 --------------------------------------------------------------------------------------------
 East: Proyecto
 1 0.004 1.000 0.0 0.0 0.0 0.0 0.1 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
 North: K-25

 1 0.058 1.000 0.0 0.9 0.0 0.9 2.3 0.00 0.0 100.0 0.1 0.1

 --------------------------------------------------------------------------------------------
 West: Acceso Part.

 1 0.004 1.000 0.0 0.0 0.0 0.0 0.1 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Queue Percentiles

Site:AC

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE QUEUE PERCENTILES (VEHICLES)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (veh)

 Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 South: K-25

 1 0.054 0.1 0.1 0.2 0.2 0.3 0.3 0.3

 -------------------------------------------------------------
 East: Proyecto
 1 0.004 0.0 0.0 0.0 0.0 0.0 0.0 0.0

 -------------------------------------------------------------
 North: K-25

 1 0.058 0.1 0.2 0.2 0.2 0.3 0.3 0.3

 -------------------------------------------------------------
 West: Acceso Part.

 1 0.004 0.0 0.0 0.0 0.0 0.0 0.0 0.0

 -------------------------------------------------------------
 LANE QUEUE PERCENTILES (DISTANCE)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (metres)

 Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 South: K-25

 1 0.054 0.8 1.1 1.5 1.8 2.1 2.3 2.5

 -------------------------------------------------------------
 East: Proyecto
 1 0.004 0.0 0.1 0.1 0.1 0.1 0.1 0.1

 -------------------------------------------------------------
 North: K-25

 1 0.058 0.9 1.2 1.7 1.9 2.3 2.5 2.7

 -------------------------------------------------------------
 West: Acceso Part.

 1 0.004 0.0 0.1 0.1 0.1 0.1 0.1 0.1

 -------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Stops
Site:AC

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -----------------------------------------------------------------------------
 Queue Total
 Deg. Prog. -- Effective Stop Rate -- Total Move-up Queue Prop.
 Lane Satn Factor Geom. Overall Stops Rate Move-ups Queued
 No. x he1 he2 hig h H hqm Hqm pq

 -----------------------------------------------------------------------------
 South: K-25

```

```
 1 0.054 1.000 0.00 0.00 0.02 0.02 2.4 0.00 0.0 0.21

 -----------------------------------------------------------------------------
 East: Proyecto
 1 0.004 1.000 0.09 0.00 0.77 0.86 3.6 0.00 0.0 0.23

 -----------------------------------------------------------------------------
 North: K-25

 1 0.058 1.000 0.00 0.00 0.06 0.06 6.3 0.00 0.0 0.21

 -----------------------------------------------------------------------------
 West: Acceso Part.

 1 0.004 1.000 0.10 0.00 0.77 0.86 3.6 0.00 0.0 0.23

 -----------------------------------------------------------------------------
 hig is the average value for all movements in a shared lane
 hqm is average queue move-up rate for all vehicles queued and unqueued

```

[Go to Table Links (Top)](about:blank#tablelinks)

**Flow Rates**

Origin-Destination Flow Rates (Total)
Site:AC

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 TOTAL FLOW RATES (ALL MOVEMENT CLASSES)

 ----------------------------------------------------------
 From SOUTH To: W N E

 Turn: L2 T1 R2 TOT

 Flow Rate 1.1 97.9 1.1 100.0

 %HV (all designations) 0.0 8.6 0.0 8.4

 ----------------------------------------------------------
 From EAST To: S W N

 Turn: L2 T1 R2 TOT

 Flow Rate 1.1 1.1 2.1 4.2

 %HV (all designations) 0.0 0.0 0.0 0.0

 ----------------------------------------------------------
 From NORTH To: E S W

 Turn: L2 T1 R2 TOT

 Flow Rate 4.2 97.9 1.1 103.2

 %HV (all designations) 0.0 16.1 0.0 15.3

 ----------------------------------------------------------
 From WEST To: N E S

 Turn: L2 T1 R2 TOT

 Flow Rate 1.1 1.1 2.1 4.2

 %HV (all designations) 0.0 0.0 0.0 0.0

 ----------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Origin-Destination Flow Rates by Movement Class
Site:AC

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 FLOW RATES FOR Light Vehicles

 --------------------------------------------------
 From SOUTH To: W N E

```

```
Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 1.1 89.5 1.1 91.6

Mov Class % 100.0 91.4 100.0 91.6

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From EAST To: S W N

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 1.1 1.1 2.1 4.2

Mov Class % 100.0 100.0 100.0 100.0

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From NORTH To: E S W

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 4.2 82.1 1.1 87.4

Mov Class % 100.0 83.9 100.0 84.7

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From WEST To: N E S

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 1.1 1.1 2.1 4.2

Mov Class % 100.0 100.0 100.0 100.0

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
FLOW RATES FOR Heavy Vehicles

--------------------------------------------------
From SOUTH To: W N E

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 0.0 8.4 0.0 8.4

Mov Class % 0.0 8.6 0.0 8.4

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From EAST To: S W N

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 0.0 0.0 0.0 0.0

Mov Class % 0.0 0.0 0.0 0.0

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From NORTH To: E S W

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 0.0 15.8 0.0 15.8

Mov Class % 0.0 16.1 0.0 15.3

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From WEST To: N E S

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 0.0 0.0 0.0 0.0

Mov Class % 0.0 0.0 0.0 0.0

```

```
 Flow Scale - Fixed 1.00 1.00 1.00

 Flow Scale - Var 1.00 1.00 1.00

 Peak Flow Factor 0.95 0.95 0.95

 --------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Flow Rates

Site:AC

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE FLOW RATES AT STOP LINE

 ------------------------------------------------
 From SOUTH To: W N E

 Turn: L2 T1 R2 TOT

 ------------------------------------------------
 Lane 1

 LV 1.1 89.5 1.1 91.6

 HV * 8.4 * 8.4

 Total 1.1 97.9 1.1 100.0

 ------------------------------------------------
 Approach 1.1 97.9 1.1 100.0

 ------------------------------------------------
 From EAST To: S W N

 Turn: L2 T1 R2 TOT

 ------------------------------------------------
 Lane 1

 LV 1.1 1.1 2.1 4.2

 Total 1.1 1.1 2.1 4.2

 ------------------------------------------------
 Approach 1.1 1.1 2.1 4.2

 ------------------------------------------------
 From NORTH To: E S W

 Turn: L2 T1 R2 TOT

 ------------------------------------------------
 Lane 1

 LV 4.2 82.1 1.1 87.4

 HV * 15.8 * 15.8

 Total 4.2 97.9 1.1 103.2

 ------------------------------------------------
 Approach 4.2 97.9 1.1 103.2

 ------------------------------------------------
 From WEST To: N E S

 Turn: L2 T1 R2 TOT

 ------------------------------------------------
 Lane 1

 LV 1.1 1.1 2.1 4.2

 Total 1.1 1.1 2.1 4.2

 ------------------------------------------------
 Approach 1.1 1.1 2.1 4.2

 ------------------------------------------------
 * Movement not allocated to the lane

 EXIT LANE FLOW RATES

 ----------------------------------------
 Movement Class: LV HV TOT

 ----------------------------------------
 Exit: SOUTH

 Lane: 1 85.3 15.8 101.1

 Total 85.3 15.8 101.1

 ----------------------------------------
 Exit: EAST

```

```
 Lane: 1 6.3 * 6.3

 Total 6.3 * 6.3

 ----------------------------------------
 Exit: NORTH

 Lane: 1 92.6 8.4 101.1

 Total 92.6 8.4 101.1

 ----------------------------------------
 Exit: WEST

 Lane: 1 3.2 * 3.2

 Total 3.2 * 3.2

 ----------------------------------------
 * Movement not allocated to the lane

 DOWNSTREAM LANE FLOW RATES FOR EXIT ROADS

 ----------------------------------------
 Movement Class: LV HV TOT

 ----------------------------------------
 Exit: SOUTH

 Lane: 1 85.3 15.8 101.1

 Total 85.3 15.8 101.1

 ----------------------------------------
 Exit: EAST

 Lane: 1 6.3 * 6.3

 Total 6.3 * 6.3

 ----------------------------------------
 Exit: NORTH

 Lane: 1 92.6 8.4 101.1

 Total 92.6 8.4 101.1

 ----------------------------------------
 Exit: WEST

 Lane: 1 3.2 * 3.2

 Total 3.2 * 3.2

 ----------------------------------------
 * Movement not allocated to the lane

 Unit Time for Volumes = 60 minutes

 Peak Flow Period = 30 minutes

 Flow Rates include effects of Flow Scale and Peak Flow Factor

```

[Go to Table Links (Top)](about:blank#tablelinks)

**Other**

Model Settings Summary
Site:AC

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
Site:AC

[Go to Table Links (Top)](about:blank#tablelinks)

## 2. Situación Base Punta Tarde

### DETAILED OUTPUT

**Site: BA**

Planta Áridos Los Maitenes
Stop (Two-Way)

**OUTPUT TABLE LINKS**

**Movements**

Intersection Negotiation Data
Site:BA

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 INTERSECTION NEGOTIATION DATA

 ----------------------------------------------------------------------------
 Negn Negn Negn Appr. Downstream Distance
 From To Radius Speed Dist. Dist. ------------------- Approach Exit Turn m km/h m m m User Spec?

 ----------------------------------------------------------------------------
 South: K-25

 West L2 6.6 17.2 10.4 500 83 No

 North T1 S 60.0 10.0 500 351 No

 East R2 10.0 20.2 15.7 500 88 No

```

```
 ----------------------------------------------------------------------------
 East: Proyecto
 South L2 6.6 17.2 10.4 500 100 No

 West T1 S 20.0 10.0 500 101 No

 North R2 10.0 20.2 15.7 500 105 No

 ----------------------------------------------------------------------------
 North: K-25

 East L2 6.6 17.2 10.4 500 85 No

 South T1 S 60.0 10.0 500 456 No

 West R2 10.0 20.2 15.7 500 91 No

 ----------------------------------------------------------------------------
 West: Acceso Part.

 North L2 6.6 17.2 10.4 500 100 No

 East T1 S 20.0 10.0 500 101 No

 South R2 10.0 20.2 15.7 500 105 No

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
 South: K-25

 1 L2 60.0 17.2 17.2 60.0 0.4 54.8 54.8 9.6

 2 T1 60.0 60.0 60.0 60.0 0.4 54.8 54.8 0.0

 3 R2 60.0 20.2 20.2 60.0 0.4 54.8 54.8 9.2

 ----------------------------------------------------------------------------
 East: Proyecto
 4 L2 60.0 0.0 17.2 60.0 19.2 46.5 46.1 10.4

 5 T1 60.0 0.0 20.0 60.0 19.2 46.5 46.1 10.2

 6 R2 60.0 0.0 20.2 60.0 19.2 46.5 46.1 10.7

 ----------------------------------------------------------------------------
 North: K-25

 7 L2 60.0 17.2 17.2 60.0 2.2 54.5 54.5 9.6

 8 T1 60.0 60.0 60.0 60.0 2.2 54.5 54.5 0.0

 9 R2 60.0 20.2 20.2 60.0 2.2 54.5 54.5 9.2

 ----------------------------------------------------------------------------
 West: Acceso Part.

 10 L2 60.0 0.0 17.2 60.0 19.2 46.5 46.1 10.4

 11 T1 60.0 0.0 20.0 60.0 19.2 46.5 46.1 10.2

 12 R2 60.0 0.0 20.2 60.0 19.2 46.5 46.1 10.7

 ----------------------------------------------------------------------------
 "Running Speed" is the average speed excluding stopped periods.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Gap Acceptance Parameters
Site:BA

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -------------------------------------------------------------------------
 Critical Gap Intra
 Opng ------------ Foll-up Entry Bunch Propn
 Opd Dest Flow Hdwy Dist Headway HV Hdwy Bnchd
 Lane pcu/h sec m sec Equiv sec

 -------------------------------------------------------------------------
 South: K-25

```

```
 1 W 122 4.00 66.3 2.00 1.00 1.80 0.013

 -------------------------------------------------------------------------
 East: Proyecto
 1 S 250+ 5.50 88.8 3.50 1.00 0.89 0.019

 1 N 118+ 4.50 75.0 2.50 1.00 1.80 0.012

 1 W 247+ 5.00 81.5 3.00 1.00 0.92 0.013

 -------------------------------------------------------------------------
 North: K-25

 1 E 120 4.00 65.9 2.00 1.00 1.80 0.013

 -------------------------------------------------------------------------
 West: Acceso Part.

 1 S 121+ 4.50 75.0 2.50 1.00 1.80 0.013

 1 E 247+ 5.00 81.2 3.00 1.00 0.92 0.013

 1 N 249+ 5.50 88.8 3.50 1.00 0.89 0.019

 -------------------------------------------------------------------------
 Values in this table are adjusted for heavy vehicles in the entry stream.
 Use the Pedestrians and Priorities input dialogs to specify opposing pedestrian movements.
 + Percentage of exiting flow included in opposing vehicle flow

```

[Go to Table Links (Top)](about:blank#tablelinks)

Movement Capacity and Performance Parameters
Site:BA

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
 South: K-25

 1 L2 # 1 113 122 17 0.98 1454 0.063

 2 T1 # 113 0 0 1786 0.98 1454 0.063

 3 R2 # 2 0 0 33 0.98 1454 0.063

 --------------------------------------------------------------
 East: Proyecto
 4 L2 # 2 236 250 335 0.80 **** 0.006

 5 T1 # 1 233 247 167 0.80 **** 0.006

 6 R2 # 3 113 118 502 0.80 **** 0.006

 --------------------------------------------------------------
 North: K-25

 7 L2 # 5 115 120 79 0.98 1366 0.067*

 8 T1 # 112 0 0 1669 0.98 1366 0.067*

 9 R2 # 1 0 0 16 0.98 1366 0.067*

 --------------------------------------------------------------
 West: Acceso Part.

 10 L2 # 2 235 249 334 0.80 **** 0.006

 11 T1 # 1 233 247 167 0.80 **** 0.006

 12 R2 # 3 112 121 502 0.80 **** 0.006

 --------------------------------------------------------------
 * Maximum degree of saturation
 # Combined Movement Capacity parameters are shown for all Movement Classes.

 MOVEMENT PERFORMANCE

 -------------------------------------------------------------------------------
 Mov Turn Total Total Aver. Eff. Total Perf. Tot.Trav. Tot.Trav. Aver.

 ID Delay Delay Delay Stop Stops Index Distance Time Speed
 (veh-h/h)(pers-h/h)(sec) Rate (veh-km/h)(veh-h/h) (km/h)

 -------------------------------------------------------------------------------
```

```
 South: K-25

 1 L2 0.00 0.00 9.9 0.03 0.0 0.01 0.7 0.0 54.8

 2 T1 0.01 0.01 0.4 0.03 3.4 1.23 72.1 1.3 54.8

 3 R2 0.01 0.01 9.5 0.03 0.1 0.03 1.3 0.0 54.8

 -------------------------------------------------------------------------------
 East: Proyecto
 4 L2 0.01 0.01 11.3 0.86 1.8 0.05 1.3 0.0 46.1

 5 T1 0.00 0.00 11.1 0.86 0.9 0.03 0.6 0.0 46.1

 6 R2 0.01 0.01 11.5 0.86 2.7 0.07 1.9 0.0 46.1

 -------------------------------------------------------------------------------
 North: K-25

 7 L2 0.01 0.02 9.9 0.06 0.3 0.07 3.4 0.1 54.5

 8 T1 0.01 0.01 0.4 0.06 7.1 1.24 71.4 1.3 54.5

 9 R2 0.00 0.00 9.5 0.06 0.1 0.01 0.7 0.0 54.5

 -------------------------------------------------------------------------------
 West: Acceso Part.

 10 L2 0.01 0.01 11.3 0.86 1.8 0.05 1.3 0.0 46.1

 11 T1 0.00 0.00 11.1 0.86 0.9 0.03 0.6 0.0 46.1

 12 R2 0.01 0.01 11.5 0.86 2.7 0.07 1.9 0.0 46.1

 -------------------------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Fuel Consumption, Emissions and Cost
Site:BA

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 FUEL CONSUMPTION, EMISSIONS AND COST (TOTAL)

 --------------------------------------------------------------
 Mov Turn Cost Fuel CO2 CO HC NOX

 ID Total Total Total Total Total Total
 $/h L/h kg/h kg/h kg/h kg/h

 --------------------------------------------------------------
 South: K-25

 1 L2 0.50 0.1 0.1 0.00 0.000 0.001

 2 T1 53.48 6.3 14.9 0.04 0.004 0.058

 3 R2 1.00 0.1 0.3 0.00 0.000 0.001

 -----------------------------------------------
 54.98 6.5 15.4 0.04 0.004 0.060

 --------------------------------------------------------------
 East: Proyecto
 4 L2 0.87 0.1 0.1 0.00 0.000 0.000

 5 T1 0.43 0.0 0.1 0.00 0.000 0.000

 6 R2 1.30 0.1 0.2 0.00 0.000 0.000

 -----------------------------------------------
 2.60 0.2 0.4 0.00 0.000 0.000

 --------------------------------------------------------------
 North: K-25

 7 L2 2.91 0.4 1.0 0.00 0.000 0.005

 8 T1 61.63 8.6 20.7 0.04 0.004 0.096

 9 R2 0.58 0.1 0.2 0.00 0.000 0.001

 -----------------------------------------------
 65.12 9.1 21.8 0.04 0.004 0.101

 --------------------------------------------------------------
 West: Acceso Part.

 10 L2 0.87 0.1 0.1 0.00 0.000 0.000

 11 T1 0.43 0.0 0.1 0.00 0.000 0.000

 12 R2 1.30 0.1 0.2 0.00 0.000 0.000

 -----------------------------------------------
 2.60 0.2 0.4 0.00 0.000 0.000

 --------------------------------------------------------------
 INTERSECTION: 125.31 15.9 37.9 0.08 0.008 0.161

 -------------------------------------------------------------
```

```
 FUEL CONSUMPTION, EMISSIONS AND COST (RATE)

 --------------------------------------------------------------
 Mov Turn Cost Fuel CO2 CO HC NOX

 ID Rate Rate Rate Rate Rate Rate
 $/km L/100km g/km g/km g/km g/km

 --------------------------------------------------------------
 South: K-25

 1 L2 0.74 8.7 207.3 0.49 0.051 0.808

 2 T1 0.74 8.7 207.3 0.49 0.051 0.808

 3 R2 0.74 8.7 207.3 0.49 0.051 0.808

 -----------------------------------------------
 0.74 8.7 207.3 0.49 0.051 0.808

 --------------------------------------------------------------
 East: Proyecto
 4 L2 0.68 4.2 98.7 0.39 0.052 0.009

 5 T1 0.68 4.2 98.7 0.39 0.052 0.009

 6 R2 0.68 4.2 98.7 0.39 0.052 0.009

 -----------------------------------------------
 0.68 4.2 98.7 0.39 0.052 0.009

 --------------------------------------------------------------
 North: K-25

 7 L2 0.86 12.1 289.4 0.59 0.057 1.344

 8 T1 0.86 12.1 289.4 0.59 0.057 1.344

 9 R2 0.86 12.1 289.4 0.59 0.057 1.344

 -----------------------------------------------
 0.86 12.1 289.4 0.59 0.057 1.344

 --------------------------------------------------------------
 West: Acceso Part.

 10 L2 0.68 4.2 98.7 0.39 0.052 0.009

 11 T1 0.68 4.2 98.7 0.39 0.052 0.009

 12 R2 0.68 4.2 98.7 0.39 0.052 0.009

 -----------------------------------------------
 0.68 4.2 98.7 0.39 0.052 0.009

 --------------------------------------------------------------
 INTERSECTION: 0.66 8.4 201.2 0.45 0.045 0.855

 -------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

**Lanes**

Lane Performance and Capacity Information
Site:BA

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
 South: K-25

 1 116 1837 0.063 0.6 0.03 0.3 2.5 500.0

 --------------------------------------------------------------
 East: Proyecto
 1 6 1004 0.006 11.4 0.86 0.0 0.2 500.0

 --------------------------------------------------------------
 North: K-25

 1 118 1763 0.067 0.9 0.06 0.3 2.7 500.0

```

```
 --------------------------------------------------------------
 West: Acceso Part.

 1 6 1003 0.006 11.4 0.86 0.0 0.2 500.0

 --------------------------------------------------------------
 LANE FLOW AND CAPACITY INFORMATION

 ----------------------------------------
 Lane Total Min Tot Deg. Lane
 No. Arv Flow Cap Cap Satn Util
 (veh/h) veh/h veh/h x %

 ----------------------------------------
 South: K-25

 1 116 116 1837 0.063 100

 ----------------------------------------
 East: Proyecto
 1 6 6 1004 0.006 100

 ----------------------------------------
 North: K-25

 1 118 118 1763 0.067 100

 ----------------------------------------
 West: Acceso Part.

 1 6 6 1003 0.006 100

 ----------------------------------------
 The capacity value for priority and continuous movements is obtained by
 adjusting the basic saturation flow for heavy vehicle and turning vehicle
 effects. Saturation flow scale applies if specified.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane, Approach and Intersection Performance
Site:BA

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -----------------------------------------------------------
 Lane Demand Adj. Deg Aver. Longest Shrt
 No. Flow %HV Basic Sat Delay Queue Lane
 (veh/h) Satf. x sec m m

 -----------------------------------------------------------
 South: K-25

 1 116 9 0.063 0.6 2 500

 ---------------------------------------------------
 116 9 0.063 0.6 2

 -----------------------------------------------------------
 East: Proyecto
 1 6 0 0.006 11.4 0 500

 ---------------------------------------------------
 6 0 0.006 11.4 0

 -----------------------------------------------------------
 North: K-25

 1 118 15 0.067 0.9 3 500

 ---------------------------------------------------
 118 15 0.067 0.9 3

 -----------------------------------------------------------
 West: Acceso Part.

 1 6 0 0.006 11.4 0 500

 ---------------------------------------------------
 6 0 0.006 11.4 0

 ============================================================

 ALL VEHICLES

 Total % Max Aver. Max

 Flow HV X Delay Queue
 246 12 0.067 1.3 3

 ============================================================

```

```
 Peak flow period = 30 minutes.

 Queue values in this table are 95% queue (metres)
 Note: Basic Saturation Flows are not adjusted at roundabouts or sign controlled intersections and apply only to continuous lanes.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Driver Characteristics

Site:BA

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -------------------------------------------------------
 Average Driver
 Lane Satn Satn Satn Satn Queue Response
 No. Speed Flow Hdwy Spacing Space Time
 km/h veh/h sec m m sec

 -------------------------------------------------------
 South: K-25

 1 NA - Major Road Movement

 -------------------------------------------------------
 East: Proyecto
 1 19.2 1234 2.92 15.52 7.00 1.60

 -------------------------------------------------------
 North: K-25

 1 NA - Major Road Movement

 -------------------------------------------------------
 West: Acceso Part.

 1 19.2 1234 2.92 15.52 7.00 1.60

 -------------------------------------------------------
 Saturation Flow and Saturation Headway are derived from follow-up headway.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Delays
Site:BA

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE DELAYS

 -----------------------------------------------------------------------------
 ---------------- Delay (seconds/veh) --------------- Deg. Prog. Stop-line Delay Acc. Queuing Stopd
 Lane Satn Factor 1st 2nd Total Dec. Total MvUp (Idle) Geom Control
 No. x d1 d2 dSL dn dq dqm di dig dic

 -----------------------------------------------------------------------------
 South: K-25

 1 0.063 1.000 0.4 0.0 0.4 2.3 0.0 0.0 0.0 0.3 0.6

 -----------------------------------------------------------------------------
 East: Proyecto
 1 0.006 1.000 0.9 0.0 0.9 0.5 0.4 0.0 0.4 10.5 11.4

 -----------------------------------------------------------------------------
 North: K-25

 1 0.067 1.000 0.4 0.0 0.4 2.2 0.0 0.0 0.0 0.5 0.9

 -----------------------------------------------------------------------------
 West: Acceso Part.

 1 0.006 1.000 0.9 0.0 0.9 0.5 0.3 0.0 0.3 10.5 11.4

 -----------------------------------------------------------------------------
```

```
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

Site:BA

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE QUEUES (VEHICLES)

 --------------------------------------------------------------------------------------------
 Deg. Prog. Ovrfl. Back of Queue (veh) Queue Prob. P'ile Cyc-Av. Queue
 Lane Satn Factor Queue ------------------------- Stor. Block Block ------------
 No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 --------------------------------------------------------------------------------------------
 South: K-25

 1 0.063 1.000 0.0 0.1 0.0 0.1 0.3 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
 East: Proyecto
 1 0.006 1.000 0.0 0.0 0.0 0.0 0.0 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
 North: K-25

 1 0.067 1.000 0.0 0.1 0.0 0.1 0.3 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
 West: Acceso Part.

 1 0.006 1.000 0.0 0.0 0.0 0.0 0.0 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
 LANE QUEUES (DISTANCE)

 --------------------------------------------------------------------------------------------
 Deg. Prog. Ovrfl. Back of Queue (m) Queue Prob. P'ile Cyc-Av. Queue
 Lane Satn Factor Queue ------------------------- Stor. Block Block ------------
 No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 --------------------------------------------------------------------------------------------
 South: K-25

 1 0.063 1.000 0.0 1.0 0.0 1.0 2.5 0.00 0.0 100.0 0.1 0.2

 --------------------------------------------------------------------------------------------
 East: Proyecto
 1 0.006 1.000 0.0 0.1 0.0 0.1 0.2 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
 North: K-25

 1 0.067 1.000 0.0 1.1 0.0 1.1 2.7 0.00 0.0 100.0 0.1 0.2

 --------------------------------------------------------------------------------------------
 West: Acceso Part.

 1 0.006 1.000 0.0 0.1 0.0 0.1 0.2 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Queue Percentiles

Site:BA

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE QUEUE PERCENTILES (VEHICLES)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (veh)

 Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 South: K-25

 1 0.063 0.1 0.2 0.2 0.3 0.3 0.4 0.4

 -------------------------------------------------------------
 East: Proyecto
 1 0.006 0.0 0.0 0.0 0.0 0.0 0.0 0.0

 -------------------------------------------------------------
 North: K-25

 1 0.067 0.1 0.2 0.2 0.3 0.3 0.4 0.4

 -------------------------------------------------------------
 West: Acceso Part.

 1 0.006 0.0 0.0 0.0 0.0 0.0 0.0 0.0

 -------------------------------------------------------------
 LANE QUEUE PERCENTILES (DISTANCE)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (metres)

 Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 South: K-25

 1 0.063 1.0 1.3 1.8 2.1 2.5 2.8 3.0

 -------------------------------------------------------------
 East: Proyecto
 1 0.006 0.1 0.1 0.1 0.1 0.2 0.2 0.2

 -------------------------------------------------------------
 North: K-25

 1 0.067 1.1 1.4 2.0 2.3 2.7 3.0 3.2

 -------------------------------------------------------------
 West: Acceso Part.

 1 0.006 0.1 0.1 0.1 0.1 0.2 0.2 0.2

 -------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Stops
Site:BA

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -----------------------------------------------------------------------------
 Queue Total
 Deg. Prog. -- Effective Stop Rate -- Total Move-up Queue Prop.
 Lane Satn Factor Geom. Overall Stops Rate Move-ups Queued
 No. x he1 he2 hig h H hqm Hqm pq

 -----------------------------------------------------------------------------
 South: K-25

```

```
 1 0.063 1.000 0.00 0.00 0.03 0.03 3.4 0.00 0.0 0.23

 -----------------------------------------------------------------------------
 East: Proyecto
 1 0.006 1.000 0.11 0.00 0.75 0.86 5.4 0.00 0.0 0.25

 -----------------------------------------------------------------------------
 North: K-25

 1 0.067 1.000 0.01 0.00 0.06 0.06 7.5 0.00 0.0 0.23

 -----------------------------------------------------------------------------
 West: Acceso Part.

 1 0.006 1.000 0.11 0.00 0.75 0.86 5.4 0.00 0.0 0.25

 -----------------------------------------------------------------------------
 hig is the average value for all movements in a shared lane
 hqm is average queue move-up rate for all vehicles queued and unqueued

```

[Go to Table Links (Top)](about:blank#tablelinks)

**Flow Rates**

Origin-Destination Flow Rates (Total)
Site:BA

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 TOTAL FLOW RATES (ALL MOVEMENT CLASSES)

 ----------------------------------------------------------
 From SOUTH To: W N E

 Turn: L2 T1 R2 TOT

 Flow Rate 1.1 112.6 2.1 115.8

 %HV (all designations) 0.0 9.3 0.0 9.1

 ----------------------------------------------------------
 From EAST To: S W N

 Turn: L2 T1 R2 TOT

 Flow Rate 2.1 1.1 3.2 6.3

 %HV (all designations) 0.0 0.0 0.0 0.0

 ----------------------------------------------------------
 From NORTH To: E S W

 Turn: L2 T1 R2 TOT

 Flow Rate 5.3 111.6 1.1 117.9

 %HV (all designations) 0.0 16.0 0.0 15.2

 ----------------------------------------------------------
 From WEST To: N E S

 Turn: L2 T1 R2 TOT

 Flow Rate 2.1 1.1 3.2 6.3

 %HV (all designations) 0.0 0.0 0.0 0.0

 ----------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Origin-Destination Flow Rates by Movement Class
Site:BA

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 FLOW RATES FOR Light Vehicles

 --------------------------------------------------
 From SOUTH To: W N E

```

```
Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 1.1 102.1 2.1 105.3

Mov Class % 100.0 90.7 100.0 90.9

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From EAST To: S W N

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 2.1 1.1 3.2 6.3

Mov Class % 100.0 100.0 100.0 100.0

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From NORTH To: E S W

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 5.3 93.7 1.1 100.0

Mov Class % 100.0 84.0 100.0 84.8

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From WEST To: N E S

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 2.1 1.1 3.2 6.3

Mov Class % 100.0 100.0 100.0 100.0

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
FLOW RATES FOR Heavy Vehicles

--------------------------------------------------
From SOUTH To: W N E

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 0.0 10.5 0.0 10.5

Mov Class % 0.0 9.3 0.0 9.1

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From EAST To: S W N

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 0.0 0.0 0.0 0.0

Mov Class % 0.0 0.0 0.0 0.0

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From NORTH To: E S W

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 0.0 17.9 0.0 17.9

Mov Class % 0.0 16.0 0.0 15.2

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From WEST To: N E S

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 0.0 0.0 0.0 0.0

Mov Class % 0.0 0.0 0.0 0.0

```

```
 Flow Scale - Fixed 1.00 1.00 1.00

 Flow Scale - Var 1.00 1.00 1.00

 Peak Flow Factor 0.95 0.95 0.95

 --------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Flow Rates

Site:BA

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE FLOW RATES AT STOP LINE

 ------------------------------------------------
 From SOUTH To: W N E

 Turn: L2 T1 R2 TOT

 ------------------------------------------------
 Lane 1

 LV 1.1 102.1 2.1 105.3

 HV * 10.5 * 10.5

 Total 1.1 112.6 2.1 115.8

 ------------------------------------------------
 Approach 1.1 112.6 2.1 115.8

 ------------------------------------------------
 From EAST To: S W N

 Turn: L2 T1 R2 TOT

 ------------------------------------------------
 Lane 1

 LV 2.1 1.1 3.2 6.3

 Total 2.1 1.1 3.2 6.3

 ------------------------------------------------
 Approach 2.1 1.1 3.2 6.3

 ------------------------------------------------
 From NORTH To: E S W

 Turn: L2 T1 R2 TOT

 ------------------------------------------------
 Lane 1

 LV 5.3 93.7 1.1 100.0

 HV * 17.9 * 17.9

 Total 5.3 111.6 1.1 117.9

 ------------------------------------------------
 Approach 5.3 111.6 1.1 117.9

 ------------------------------------------------
 From WEST To: N E S

 Turn: L2 T1 R2 TOT

 ------------------------------------------------
 Lane 1

 LV 2.1 1.1 3.2 6.3

 Total 2.1 1.1 3.2 6.3

 ------------------------------------------------
 Approach 2.1 1.1 3.2 6.3

 ------------------------------------------------
 * Movement not allocated to the lane

 EXIT LANE FLOW RATES

 ----------------------------------------
 Movement Class: LV HV TOT

 ----------------------------------------
 Exit: SOUTH

 Lane: 1 98.9 17.9 116.8

 Total 98.9 17.9 116.8

 ----------------------------------------
 Exit: EAST

```

```
 Lane: 1 8.4 * 8.4

 Total 8.4 * 8.4

 ----------------------------------------
 Exit: NORTH

 Lane: 1 107.4 10.5 117.9

 Total 107.4 10.5 117.9

 ----------------------------------------
 Exit: WEST

 Lane: 1 3.2 * 3.2

 Total 3.2 * 3.2

 ----------------------------------------
 * Movement not allocated to the lane

 DOWNSTREAM LANE FLOW RATES FOR EXIT ROADS

 ----------------------------------------
 Movement Class: LV HV TOT

 ----------------------------------------
 Exit: SOUTH

 Lane: 1 98.9 17.9 116.8

 Total 98.9 17.9 116.8

 ----------------------------------------
 Exit: EAST

 Lane: 1 8.4 * 8.4

 Total 8.4 * 8.4

 ----------------------------------------
 Exit: NORTH

 Lane: 1 107.4 10.5 117.9

 Total 107.4 10.5 117.9

 ----------------------------------------
 Exit: WEST

 Lane: 1 3.2 * 3.2

 Total 3.2 * 3.2

 ----------------------------------------
 * Movement not allocated to the lane

 Unit Time for Volumes = 60 minutes

 Peak Flow Period = 30 minutes

 Flow Rates include effects of Flow Scale and Peak Flow Factor

```

[Go to Table Links (Top)](about:blank#tablelinks)

**Other**

Model Settings Summary
Site:BA

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

## 3. Situación Con Proyecto Punta Tarde

### DETAILED OUTPUT

**Site: CP**

Planta Áridos Los Maitenes
Stop (Two-Way)

**OUTPUT TABLE LINKS**

**Movements**

Intersection Negotiation Data
Site:CP

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 INTERSECTION NEGOTIATION DATA

 ----------------------------------------------------------------------------
 Negn Negn Negn Appr. Downstream Distance
 From To Radius Speed Dist. Dist. ------------------- Approach Exit Turn m km/h m m m User Spec?

 ----------------------------------------------------------------------------
 South: K-25

```

```
 West L2 6.6 17.2 10.4 500 86 No

 North T1 S 60.0 10.0 500 357 No

 East R2 10.0 20.2 15.7 500 439 No

 ----------------------------------------------------------------------------
 East: Proyecto
 South L2 6.6 17.2 10.4 500 661 No

 West T1 S 20.0 10.0 500 134 No

 North R2 10.0 20.2 15.7 500 604 No

 ----------------------------------------------------------------------------
 North: K-25

 East L2 6.6 17.2 10.4 500 353 No

 South T1 S 60.0 10.0 500 467 No

 West R2 10.0 20.2 15.7 500 96 No

 ----------------------------------------------------------------------------
 West: Acceso Part.

 North L2 6.6 17.2 10.4 500 100 No

 East T1 S 20.0 10.0 500 101 No

 South R2 10.0 20.2 15.7 500 105 No

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
 South: K-25

 1 L2 60.0 17.2 17.2 60.0 0.4 54.6 54.6 9.6

 2 T1 60.0 60.0 60.0 60.0 0.4 54.6 54.6 0.0

 3 R2 60.0 20.2 20.2 60.0 0.4 54.6 54.6 9.2

 ----------------------------------------------------------------------------
 East: Proyecto
 4 L2 60.0 0.0 17.2 60.0 19.0 46.0 45.2 11.6

 5 T1 60.0 0.0 20.0 60.0 19.0 46.0 45.2 11.2

 6 R2 60.0 0.0 20.2 60.0 19.0 46.0 45.2 11.6

 ----------------------------------------------------------------------------
 North: K-25

 7 L2 60.0 17.2 17.2 60.0 2.7 53.5 53.5 9.6

 8 T1 60.0 60.0 60.0 60.0 2.7 53.5 53.5 0.0

 9 R2 60.0 20.2 20.2 60.0 2.7 53.5 53.5 9.2

 ----------------------------------------------------------------------------
 West: Acceso Part.

 10 L2 60.0 0.0 17.2 60.0 19.2 46.5 46.1 10.4

 11 T1 60.0 0.0 20.0 60.0 19.2 46.5 46.1 10.2

 12 R2 60.0 0.0 20.2 60.0 19.2 46.5 46.1 10.7

 ----------------------------------------------------------------------------
 "Running Speed" is the average speed excluding stopped periods.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Gap Acceptance Parameters
Site:CP

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -------------------------------------------------------------------------
 Critical Gap Intra
 Opng ------------ Foll-up Entry Bunch Propn
 Opd Dest Flow Hdwy Dist Headway HV Hdwy Bnchd

```

```
 Lane pcu/h sec m sec Equiv sec

 -------------------------------------------------------------------------
 South: K-25

 1 W 122 4.00 66.3 2.00 1.00 1.80 0.013

 -------------------------------------------------------------------------
 East: Proyecto
 1 S 264+ 7.07 111.7 4.50 1.29 0.90 0.021

 1 N 118+ 5.62 93.8 3.12 1.25 1.80 0.012

 1 W 261+ 5.00 79.7 3.00 1.00 0.94 0.014

 -------------------------------------------------------------------------
 North: K-25

 1 E 127 4.83 77.3 2.42 1.21 1.80 0.013

 -------------------------------------------------------------------------
 West: Acceso Part.

 1 S 121+ 4.50 75.0 2.50 1.00 1.80 0.013

 1 E 265+ 5.00 78.4 3.00 1.00 0.92 0.014

 1 N 269+ 5.50 85.3 3.50 1.00 0.88 0.021

 -------------------------------------------------------------------------
 Values in this table are adjusted for heavy vehicles in the entry stream.
 Use the Pedestrians and Priorities input dialogs to specify opposing pedestrian movements.
 + Percentage of exiting flow included in opposing vehicle flow

```

[Go to Table Links (Top)](about:blank#tablelinks)

Movement Capacity and Performance Parameters
Site:CP

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
 South: K-25

 1 L2 # 1 113 122 16 0.98 1352 0.067

 2 T1 # 113 0 0 1669 0.98 1352 0.067

 3 R2 # 7 0 0 109 0.98 1352 0.067

 --------------------------------------------------------------
 East: Proyecto
 4 L2 # 7 246 264 293 0.80 3079 0.025

 5 T1 # 1 243 261 42 0.80 3079 0.025

 6 R2 # 11 113 118 418 0.80 3079 0.025

 --------------------------------------------------------------
 North: K-25

 7 L2 # 13 120 127 169 0.98 1207 0.075*

 8 T1 # 112 0 0 1489 0.98 1207 0.075*

 9 R2 # 1 0 0 14 0.98 1207 0.075*

 --------------------------------------------------------------
 West: Acceso Part.

 10 L2 # 2 250 269 330 0.80 **** 0.006

 11 T1 # 1 246 265 165 0.80 **** 0.006

 12 R2 # 3 112 121 495 0.80 **** 0.006

 --------------------------------------------------------------
 * Maximum degree of saturation
 # Combined Movement Capacity parameters are shown for all Movement Classes.

 MOVEMENT PERFORMANCE

 -------------------------------------------------------------------------------
 Mov Turn Total Total Aver. Eff. Total Perf. Tot.Trav. Tot.Trav. Aver.

```

```
 ID Delay Delay Delay Stop Stops Index Distance Time Speed
 (veh-h/h)(pers-h/h)(sec) Rate (veh-km/h)(veh-h/h) (km/h)

 -------------------------------------------------------------------------------
 South: K-25

 1 L2 0.00 0.00 9.9 0.12 0.1 0.01 0.7 0.0 54.6

 2 T1 0.01 0.01 0.4 0.12 13.5 1.29 72.1 1.3 54.6

 3 R2 0.02 0.02 9.5 0.12 0.9 0.10 4.7 0.1 54.6

 -------------------------------------------------------------------------------
 East: Proyecto
 4 L2 0.03 0.03 13.0 0.46 3.4 0.20 4.7 0.1 45.2

 5 T1 0.00 0.00 12.7 0.46 0.5 0.05 0.7 0.0 45.2

 6 R2 0.04 0.05 13.1 0.46 4.9 0.25 6.7 0.1 45.2

 -------------------------------------------------------------------------------
 North: K-25

 7 L2 0.04 0.04 10.1 0.17 2.2 0.18 8.1 0.2 53.5

 8 T1 0.02 0.02 0.6 0.17 19.4 1.32 71.4 1.3 53.5

 9 R2 0.00 0.00 9.8 0.17 0.2 0.02 0.7 0.0 53.5

 -------------------------------------------------------------------------------
 West: Acceso Part.

 10 L2 0.01 0.01 11.4 0.86 1.8 0.05 1.3 0.0 46.1

 11 T1 0.00 0.00 11.1 0.86 0.9 0.03 0.6 0.0 46.1

 12 R2 0.01 0.01 11.6 0.86 2.7 0.07 1.9 0.0 46.1

 -------------------------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Fuel Consumption, Emissions and Cost
Site:CP

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 FUEL CONSUMPTION, EMISSIONS AND COST (TOTAL)

 --------------------------------------------------------------
 Mov Turn Cost Fuel CO2 CO HC NOX

 ID Total Total Total Total Total Total

 $/h L/h kg/h kg/h kg/h kg/h

 --------------------------------------------------------------
 South: K-25

 1 L2 0.55 0.1 0.2 0.00 0.000 0.001

 2 T1 58.95 7.6 18.1 0.04 0.004 0.079

 3 R2 3.86 0.5 1.2 0.00 0.000 0.005

 -----------------------------------------------
 63.36 8.2 19.5 0.04 0.004 0.085

 --------------------------------------------------------------
 East: Proyecto
 4 L2 8.79 1.6 3.9 0.01 0.001 0.023

 5 T1 1.26 0.2 0.6 0.00 0.000 0.003

 6 R2 12.56 2.3 5.6 0.01 0.001 0.032

 -----------------------------------------------
 22.61 4.1 10.1 0.02 0.001 0.058

 --------------------------------------------------------------
 North: K-25

 7 L2 7.73 1.1 2.7 0.01 0.001 0.013

 8 T1 68.26 10.1 24.2 0.05 0.004 0.119

 9 R2 0.64 0.1 0.2 0.00 0.000 0.001

 -----------------------------------------------
 76.63 11.3 27.2 0.05 0.005 0.134

 --------------------------------------------------------------
 West: Acceso Part.

 10 L2 0.87 0.1 0.1 0.00 0.000 0.000

 11 T1 0.43 0.0 0.1 0.00 0.000 0.000

 12 R2 1.30 0.1 0.2 0.00 0.000 0.000

 -----------------------------------------------
 2.61 0.2 0.4 0.00 0.000 0.000

 --------------------------------------------------------------
```

```
 INTERSECTION: 165.20 23.7 57.1 0.11 0.011 0.277

 -------------------------------------------------------------
 FUEL CONSUMPTION, EMISSIONS AND COST (RATE)

 --------------------------------------------------------------
 Mov Turn Cost Fuel CO2 CO HC NOX

 ID Rate Rate Rate Rate Rate Rate

 $/km L/100km g/km g/km g/km g/km

 --------------------------------------------------------------
 South: K-25

 1 L2 0.82 10.5 251.2 0.55 0.055 1.100

 2 T1 0.82 10.5 251.2 0.55 0.055 1.100

 3 R2 0.82 10.5 251.2 0.55 0.055 1.100

 -----------------------------------------------
 0.82 10.5 251.2 0.55 0.055 1.100

 --------------------------------------------------------------
 East: Proyecto

 4 L2 1.88 33.8 841.8 1.36 0.120 4.824

 5 T1 1.88 33.8 841.8 1.36 0.120 4.824

 6 R2 1.88 33.8 841.8 1.36 0.120 4.824

 -----------------------------------------------
 1.88 33.8 841.8 1.36 0.120 4.824

 --------------------------------------------------------------
 North: K-25

 7 L2 0.96 14.1 338.9 0.66 0.063 1.667

 8 T1 0.96 14.1 338.9 0.66 0.063 1.667

 9 R2 0.96 14.1 338.9 0.66 0.063 1.667

 -----------------------------------------------
 0.96 14.1 338.9 0.66 0.063 1.667

 --------------------------------------------------------------
 West: Acceso Part.

 10 L2 0.69 4.2 98.8 0.39 0.052 0.009

 11 T1 0.69 4.2 98.8 0.39 0.052 0.009

 12 R2 0.69 4.2 98.8 0.39 0.052 0.009

 -----------------------------------------------
 0.69 4.2 98.8 0.39 0.052 0.009

 --------------------------------------------------------------
 INTERSECTION: 0.79 11.4 274.5 0.55 0.053 1.331

 -------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

**Lanes**

Lane Performance and Capacity Information
Site:CP

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
 South: K-25

 1 121 1794 0.067 1.0 0.12 0.3 2.7 500.0

 --------------------------------------------------------------
 East: Proyecto
 1 19 753 0.025 13.1 0.46 0.1 0.9 500.0

```

```
 --------------------------------------------------------------
 North: K-25

 1 125 1671 0.075 1.6 0.17 0.5 3.7 500.0

 --------------------------------------------------------------
 West: Acceso Part.

 1 6 989 0.006 11.4 0.86 0.0 0.2 500.0

 --------------------------------------------------------------
 LANE FLOW AND CAPACITY INFORMATION

 ----------------------------------------
 Lane Total Min Tot Deg. Lane
 No. Arv Flow Cap Cap Satn Util
 (veh/h) veh/h veh/h x %

 ----------------------------------------
 South: K-25

 1 121 121 1794 0.067 100

 ----------------------------------------
 East: Proyecto
 1 19 6 753 0.025 100

 ----------------------------------------
 North: K-25

 1 125 58 1671 0.075 100

 ----------------------------------------
 West: Acceso Part.

 1 6 6 989 0.006 100

 ----------------------------------------
 The capacity value for priority and continuous movements is obtained by
 adjusting the basic saturation flow for heavy vehicle and turning vehicle
 effects. Saturation flow scale applies if specified.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane, Approach and Intersection Performance
Site:CP

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -----------------------------------------------------------
 Lane Demand Adj. Deg Aver. Longest Shrt
 No. Flow %HV Basic Sat Delay Queue Lane
 (veh/h) Satf. x sec m m

 -----------------------------------------------------------
 South: K-25

 1 121 12 0.067 1.0 3 500

 ---------------------------------------------------
 121 12 0.067 1.0 3

 -----------------------------------------------------------
 East: Proyecto

 1 19 50 0.025 13.1 1 500

 ---------------------------------------------------
 19 50 0.025 13.1 1

 -----------------------------------------------------------
 North: K-25

 1 125 18 0.075 1.6 4 500

 ---------------------------------------------------
 125 18 0.075 1.6 4

 -----------------------------------------------------------
 West: Acceso Part.

 1 6 0 0.006 11.4 0 500

 ---------------------------------------------------
 6 0 0.006 11.4 0

 ============================================================

 ALL VEHICLES

 Total % Max Aver. Max

```

```
 Flow HV X Delay Queue
 272 17 0.075 2.4 4

 ============================================================

 Peak flow period = 30 minutes.

 Queue values in this table are 95% queue (metres)
 Note: Basic Saturation Flows are not adjusted at roundabouts or sign controlled intersections and apply only to continuous lanes.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Driver Characteristics

Site:CP

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -------------------------------------------------------
 Average Driver
 Lane Satn Satn Satn Satn Queue Response
 No. Speed Flow Hdwy Spacing Space Time
 km/h veh/h sec m m sec

 -------------------------------------------------------
 South: K-25

 1 NA - Major Road Movement

 -------------------------------------------------------
 East: Proyecto
 1 19.0 986 3.65 19.29 10.00 1.76

 -------------------------------------------------------
 North: K-25

 1 NA - Major Road Movement

 -------------------------------------------------------
 West: Acceso Part.

 1 19.2 1234 2.92 15.52 7.00 1.60

 -------------------------------------------------------
 Saturation Flow and Saturation Headway are derived from follow-up headway.

```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Delays
Site:CP

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE DELAYS

 -----------------------------------------------------------------------------
 ---------------- Delay (seconds/veh) --------------- Deg. Prog. Stop-line Delay Acc. Queuing Stopd
 Lane Satn Factor 1st 2nd Total Dec. Total MvUp (Idle) Geom Control
 No. x d1 d2 dSL dn dq dqm di dig dic

 -----------------------------------------------------------------------------
 South: K-25

 1 0.067 1.000 0.4 0.0 0.4 2.3 0.0 0.0 0.0 0.6 1.0

 -----------------------------------------------------------------------------
 East: Proyecto
 1 0.025 1.000 1.5 0.0 1.5 0.6 0.9 0.0 0.9 11.6 13.1

 -----------------------------------------------------------------------------
 North: K-25

 1 0.075 1.000 0.6 0.0 0.6 2.6 0.0 0.0 0.0 1.0 1.6

 -----------------------------------------------------------------------------
```

```
 West: Acceso Part.

 1 0.006 1.000 0.9 0.0 0.9 0.5 0.4 0.0 0.4 10.5 11.4

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

Site:CP

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE QUEUES (VEHICLES)

 --------------------------------------------------------------------------------------------
 Deg. Prog. Ovrfl. Back of Queue (veh) Queue Prob. P'ile Cyc-Av. Queue
 Lane Satn Factor Queue ------------------------- Stor. Block Block ------------
 No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 --------------------------------------------------------------------------------------------
 South: K-25

 1 0.067 1.000 0.0 0.1 0.0 0.1 0.3 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
 East: Proyecto
 1 0.025 1.000 0.0 0.0 0.0 0.0 0.1 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
 North: K-25

 1 0.075 1.000 0.0 0.2 0.0 0.2 0.5 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
 West: Acceso Part.

 1 0.006 1.000 0.0 0.0 0.0 0.0 0.0 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
 LANE QUEUES (DISTANCE)

 --------------------------------------------------------------------------------------------
 Deg. Prog. Ovrfl. Back of Queue (m) Queue Prob. P'ile Cyc-Av. Queue
 Lane Satn Factor Queue ------------------------- Stor. Block Block ------------
 No. x No Nb1 Nb2 Nb 95% Ratio % % Nc 95%

 --------------------------------------------------------------------------------------------
 South: K-25

 1 0.067 1.000 0.0 1.1 0.0 1.1 2.7 0.00 0.0 100.0 0.1 0.2

 --------------------------------------------------------------------------------------------
 East: Proyecto
 1 0.025 1.000 0.0 0.4 0.0 0.4 0.9 0.00 0.0 100.0 0.1 0.1

 --------------------------------------------------------------------------------------------
 North: K-25

 1 0.075 1.000 0.0 1.5 0.0 1.5 3.7 0.00 0.0 100.0 0.2 0.3

 --------------------------------------------------------------------------------------------
 West: Acceso Part.

 1 0.006 1.000 0.0 0.1 0.0 0.1 0.2 0.00 0.0 100.0 0.0 0.0

 --------------------------------------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Queue Percentiles

Site:CP

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE QUEUE PERCENTILES (VEHICLES)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (veh)

 Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 South: K-25

 1 0.067 0.1 0.2 0.3 0.3 0.3 0.4 0.4

 -------------------------------------------------------------
 East: Proyecto
 1 0.025 0.0 0.0 0.1 0.1 0.1 0.1 0.1

 -------------------------------------------------------------
 North: K-25

 1 0.075 0.2 0.2 0.3 0.4 0.5 0.5 0.5

 -------------------------------------------------------------
 West: Acceso Part.

 1 0.006 0.0 0.0 0.0 0.0 0.0 0.0 0.0

 -------------------------------------------------------------
 LANE QUEUE PERCENTILES (DISTANCE)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (metres)

 Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 South: K-25

 1 0.067 1.1 1.4 2.0 2.3 2.7 3.0 3.2

 -------------------------------------------------------------
 East: Proyecto
 1 0.025 0.4 0.5 0.7 0.8 0.9 1.0 1.1

 -------------------------------------------------------------
 North: K-25

 1 0.075 1.5 1.9 2.7 3.1 3.7 4.1 4.4

 -------------------------------------------------------------
 West: Acceso Part.

 1 0.006 0.1 0.1 0.1 0.1 0.2 0.2 0.2

 -------------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Stops
Site:CP

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -----------------------------------------------------------------------------
 Queue Total
 Deg. Prog. -- Effective Stop Rate -- Total Move-up Queue Prop.
 Lane Satn Factor Geom. Overall Stops Rate Move-ups Queued
 No. x he1 he2 hig h H hqm Hqm pq

```

```
 -----------------------------------------------------------------------------
 South: K-25

 1 0.067 1.000 0.00 0.00 0.12 0.12 14.5 0.00 0.0 0.23

 -----------------------------------------------------------------------------
 East: Proyecto
 1 0.025 1.000 0.16 0.00 0.30 0.46 8.8 0.00 0.0 0.29

 -----------------------------------------------------------------------------
 North: K-25

 1 0.075 1.000 0.01 0.00 0.16 0.17 21.8 0.00 0.0 0.27

 -----------------------------------------------------------------------------
 West: Acceso Part.

 1 0.006 1.000 0.12 0.00 0.74 0.86 5.4 0.00 0.0 0.26

 -----------------------------------------------------------------------------
 hig is the average value for all movements in a shared lane
 hqm is average queue move-up rate for all vehicles queued and unqueued

```

[Go to Table Links (Top)](about:blank#tablelinks)

**Flow Rates**

Origin-Destination Flow Rates (Total)
Site:CP

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 TOTAL FLOW RATES (ALL MOVEMENT CLASSES)

 ----------------------------------------------------------
 From SOUTH To: W N E

 Turn: L2 T1 R2 TOT

 Flow Rate 1.1 112.6 7.4 121.1

 %HV (all designations) 0.0 9.3 57.1 12.2

 ----------------------------------------------------------
 From EAST To: S W N

 Turn: L2 T1 R2 TOT

 Flow Rate 7.4 1.1 10.5 18.9

 %HV (all designations) 57.1 0.0 50.0 50.0

 ----------------------------------------------------------
 From NORTH To: E S W

 Turn: L2 T1 R2 TOT

 Flow Rate 12.6 111.6 1.1 125.3

 %HV (all designations) 41.7 16.0 0.0 18.5

 ----------------------------------------------------------
 From WEST To: N E S

 Turn: L2 T1 R2 TOT

 Flow Rate 2.1 1.1 3.2 6.3

 %HV (all designations) 0.0 0.0 0.0 0.0

 ----------------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Origin-Destination Flow Rates by Movement Class
Site:CP

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 FLOW RATES FOR Light Vehicles

```

```
--------------------------------------------------
From SOUTH To: W N E

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 1.1 102.1 3.2 106.3

Mov Class % 100.0 90.7 42.9 87.8

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From EAST To: S W N

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 3.2 1.1 5.3 9.5

Mov Class % 42.9 100.0 50.0 50.0

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From NORTH To: E S W

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 7.4 93.7 1.1 102.1

Mov Class % 58.3 84.0 100.0 81.5

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From WEST To: N E S

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 2.1 1.1 3.2 6.3

Mov Class % 100.0 100.0 100.0 100.0

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
FLOW RATES FOR Heavy Vehicles

--------------------------------------------------
From SOUTH To: W N E

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 0.0 10.5 4.2 14.7

Mov Class % 0.0 9.3 57.1 12.2

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From EAST To: S W N

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 4.2 0.0 5.3 9.5

Mov Class % 57.1 0.0 50.0 50.0

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From NORTH To: E S W

Turn: L2 T1 R2 TOT

--------------------------------------------------
Flow Rate - Veh 5.3 17.9 0.0 23.2

Mov Class % 41.7 16.0 0.0 18.5

Flow Scale - Fixed 1.00 1.00 1.00

Flow Scale - Var 1.00 1.00 1.00

Peak Flow Factor 0.95 0.95 0.95

--------------------------------------------------
From WEST To: N E S

Turn: L2 T1 R2 TOT

--------------------------------------------------
```

```
 Flow Rate - Veh 0.0 0.0 0.0 0.0

 Mov Class % 0.0 0.0 0.0 0.0

 Flow Scale - Fixed 1.00 1.00 1.00

 Flow Scale - Var 1.00 1.00 1.00

 Peak Flow Factor 0.95 0.95 0.95

 --------------------------------------------------
```

[Go to Table Links (Top)](about:blank#tablelinks)

Lane Flow Rates

Site:CP

```
 Intersection ID: 1

 Stop Sign Controlled Intersection

 LANE FLOW RATES AT STOP LINE

 ------------------------------------------------
 From SOUTH To: W N E

 Turn: L2 T1 R2 TOT

 ------------------------------------------------
 Lane 1

 LV 1.1 102.1 3.2 106.3

 HV * 10.5 4.2 14.7

 Total 1.1 112.6 7.4 121.1

 ------------------------------------------------
 Approach 1.1 112.6 7.4 121.1

 ------------------------------------------------
 From EAST To: S W N

 Turn: L2 T1 R2 TOT

 ------------------------------------------------
 Lane 1

 LV 3.2 1.1 5.3 9.5

 HV 4.2 * 5.3 9.5

 Total 7.4 1.1 10.5 18.9

 ------------------------------------------------
 Approach 7.4 1.1 10.5 18.9

 ------------------------------------------------
 From NORTH To: E S W

 Turn: L2 T1 R2 TOT

 ------------------------------------------------
 Lane 1

 LV 7.4 93.7 1.1 102.1

 HV 5.3 17.9 * 23.2

 Total 12.6 111.6 1.1 125.3

 ------------------------------------------------
 Approach 12.6 111.6 1.1 125.3

 ------------------------------------------------
 From WEST To: N E S

 Turn: L2 T1 R2 TOT

 ------------------------------------------------
 Lane 1

 LV 2.1 1.1 3.2 6.3

 Total 2.1 1.1 3.2 6.3

 ------------------------------------------------
 Approach 2.1 1.1 3.2 6.3

 ------------------------------------------------
 * Movement not allocated to the lane

 EXIT LANE FLOW RATES

 ----------------------------------------
 Movement Class: LV HV TOT

 ----------------------------------------
 Exit: SOUTH

 Lane: 1 100.0 22.1 122.1

```

```
 Total 100.0 22.1 122.1

 ----------------------------------------
 Exit: EAST

 Lane: 1 11.6 9.5 21.1

 Total 11.6 9.5 21.1

 ----------------------------------------
 Exit: NORTH

 Lane: 1 109.5 15.8 125.3

 Total 109.5 15.8 125.3

 ----------------------------------------
 Exit: WEST

 Lane: 1 3.2 * 3.2

 Total 3.2 * 3.2

 ----------------------------------------
 * Movement not allocated to the lane

 DOWNSTREAM LANE FLOW RATES FOR EXIT ROADS

 ----------------------------------------
 Movement Class: LV HV TOT

 ----------------------------------------
 Exit: SOUTH

 Lane: 1 100.0 22.1 122.1

 Total 100.0 22.1 122.1

 ----------------------------------------
 Exit: EAST

 Lane: 1 11.6 9.5 21.1

 Total 11.6 9.5 21.1

 ----------------------------------------
 Exit: NORTH

 Lane: 1 109.5 15.8 125.3

 Total 109.5 15.8 125.3

 ----------------------------------------
 Exit: WEST

 Lane: 1 3.2 * 3.2

 Total 3.2 * 3.2

 ----------------------------------------
 * Movement not allocated to the lane

 Unit Time for Volumes = 60 minutes

 Peak Flow Period = 30 minutes

 Flow Rates include effects of Flow Scale and Peak Flow Factor

```

[Go to Table Links (Top)](about:blank#tablelinks)