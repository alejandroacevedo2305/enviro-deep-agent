---
title: about:blank
author: gomez
date: D:20221114103853-03'00'
language: en
type: report
pages: 11
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Combined Movement Capacity parameters are shown for all Movement Classes.
-->

Detailed Output Page 1 of 11

**DETAILED OUTPUT**

**Site: 1 [1-Gral. Mackenna/San Martín-PML]**

New Site
Site Category: (None)
Signals - Fixed Time Isolated Cycle Time = 60 seconds (Site User-Given Phase Times)

**OUTPUT TABLE LINKS**

Signal Timing

Movement Timing Information
Phase Information

Movements

Intersection Negotiation and Travel Data
Movement Capacity and Performance Parameters
Fuel Consumption, Emissions and Cost

Lanes

Lane Performance and Capacity Information
Lane, Approach and Intersection Performance
Driver Characteristics

SCATS Parameters
Lane Delays
Lane Queues
Lane Queue Percentiles
Lane Stops

Flow Rates

Origin-Destination Flow Rates (Total)
Origin-Destination Flow Rates by Movement Class
Lane Flow Rates

Other

Parameter Settings Summary
Diagnostics

**Signal Timing**

Movement Timing Information
Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

 ----------------------------------------------------------------------------------------------------
 Mov Mov Mov P H A S E M A T R I X Lost Tim Req.Mov.Time Eff. Grn
ID Cl. Typ First Green Second Green -------- ------------ ------- ----------------------- ----------------------- 1st 2nd 1st 2nd 1st 2nd

Fr To Op Pr Und Fr To Op Pr Und Grn Grn Grn Grn Grn Grn

 ----------------------------------------------------------------------------------------------------
 South: Gral. Mackenna Sur

132 # B A 4 39.5 35

131 # *B A 4 39.5 35

130 # B A 5 39.5 34

 ----------------------------------------------------------------------------------------------------
 East: Barros Arana

121 # *A B 4 23.0 17

120 # A B 4 23.0 17

 ----------------------------------------------------------------------------------------------------
 Pedestrian Movements

P1 (Ped) A B 9 15.0 Min 6
P2 (Ped) B A 9 17.0 Min 6
P3 (Ped) A B 9 15.0 Min 6
P4 (Ped) B A 11 17.0 Min 6

 ----------------------------------------------------------------------------------------------------
 Current Phase Sequence: Variable Phasing
Input Phase Sequence: A B
Output Phase Sequence: A B

 ----------------------------------------------------------------------------------------------------
 # Combined timing results are shown for all Movement Classes except any listed separately.
* Critical Movement/Green Period

Movement Types:
Slp Slip/Bypass Lane Movement
Ped Pedestrian

Dum Dummy

CRITICAL MOVEMENTS AND CYCLE TIME

```

about:blank 14-11-2022

Detailed Output Page 2 of 11

```
 ---------------------------------------------------------------------------------
 Crit App Green Phases Adjusted Adjusted Required Required
 Mov and Period ------ Lost Flow Grn Time Movement

 ID Turn Dest Fr To Time Ratio Ratio Time

 ---------------------------------------------------------------------------------
 121LV T1 E_W A B 4 0.285 0.317 23.0
 131LV T1 S_N B A 4 0.533 0.592 39.5

 ---- ------ ------ -----
 Total: 8 0.818 0.909 62.6

 ---------------------------------------------------------------------------------
 Cycle Time:
 Minimum Maximum Practical Chosen

 32 150 88 60

 (Phase times user specified, cycle time = sum of phase times)

```

Go to Table Links (Top)

Phase Information

Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

PHASE INFORMATION

 ---------------------------------------------------------------------------------
 Phase Ref. Change Starting Green Displayed Green Terminating Phase Phase
Phase Time Intgrn Start Green End Intgrn Time Split

 ---------------------------------------------------------------------------------
 A No 39 4 43 17 60 4 21 35%

B Yes 0 4 4 35 39 4 39 65%

 ---------------------------------------------------------------------------------
 (Phase times specified by the user)
Current Phase Sequence: Variable Phasing
Input Phase Sequence: A B
Output Phase Sequence: A B

PHASE YELLOW AND ALL-RED TIMES (INPUT)

 -----------------------
 Phase A B

Yellow Time 3 3

All-Red Time 1 1

Intergreen Time 4 4

 -----------------------
 Phase Yellow and All-Red parameters in this table are user-specified input values.
Intergreen Time (sum of Yellow Time and All-Red Time) is an unadjusted value.
Any adjusted values of Intergreen Time, Phase Time and Green Time determined in cases of
Pedestrian Actuation, Phase Actuation and user-given or implied Phase Frequency values
less than 100% are given in the PHASE INFORMATION table above.

```

Go to Table Links (Top)

**Movements**

Intersection Negotiation and Travel Data
Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

TRAVEL SPEED, TRAVEL DISTANCE AND TRAVEL TIME

 -----------------------------------------------------------------------------------------------
Running Travel Travel Travel Total Travel Distance Tot.Trav.
From To Speed Speed Distance Time Dem Flows Arv Flows Time
Approach Exit Turn km/h km/h m s veh-km/h veh-km/h veh-h/h

 -----------------------------------------------------------------------------------------------
South: Gral. Mackenna Sur

West L2 34.6 17.8 237.7# 48.2# 108.6 108.6 6.1

North T1 38.7 19.2 238.9# 44.9# 300.6 300.6 15.7

East R2 39.2 21.8 302.9# 50.0# 77.2 77.2 3.5

 -----------------------------------------------------------------------------------------------
East: Barros Arana

West T1 34.2 12.1 299.2# 89.1# 156.8 156.8 13.0

North R2 31.4 11.7 299.2# 91.9# 6.0 6.0 0.5

 -----------------------------------------------------------------------------------------------
ALL VEHICLES: 37.0 16.7 258.2# 55.6# 649.1 649.1 38.8

 -----------------------------------------------------------------------------------------------
"Running Speed" is the average speed excluding stopped periods.

```

about:blank 14-11-2022

Detailed Output Page 3 of 11

```
 Travel Time values include cruise times and intersection delays including
 acceleration, deceleration and idling delays.

 # Travel Distance and Travel Time values include travel on the External Exit section based

 on the Exit Distance or user-specified Downstream Distance value as applicable.

 INTERSECTION NEGOTIATION DATA

 -----------------------------------------------------------------------
 Negn Negn Negn App Exit Downstr
 From To Radius Speed Dist Dist Dist Dist
 Approach Exit Turn m km/h m m m m

 -----------------------------------------------------------------------
 South: Gral. Mackenna Sur

 West L2 5.0 15.5 10.0 113 113 NA

 North T1 S 60.0 13.2 113 113 NA

 East R2 10.0 20.2 15.7 113 176 NA

 -----------------------------------------------------------------------
 East: Barros Arana

 West T1 S 60.0 10.0 176 113 NA

 North R2 10.0 20.2 15.7 176 113 NA

 -----------------------------------------------------------------------
 NA Downstream Distance does not apply if:
 - Exit is an internal leg of a network
 - "Program" option was specified
 - Distance specified was less than the Exit Negotiation Distance
 - Distance specified was greater than the exit leg length

 Some Negotiation Radius, Speed or Distance values are user specified.

 MOVEMENT SPEEDS AND GEOMETRIC DELAY

 -----------------------------------------------------------------
 App. Speeds Exit Speeds Queue Move-up Sp

 ------------ ----------- ---------------- Geom

 Mov Cruise Negn Negn Cruise 1st Grn 2nd Grn Delay
 ID Turn km/h km/h km/h km/h km/h km/h sec

 -----------------------------------------------------------------
 South: Gral. Mackenna Sur

 132 L2 60.0 15.5 15.5 60.0 31.3 5.7

 131 T1 60.0 60.0 60.0 60.0 35.5 0.0

 130 R2 60.0 20.2 20.2 60.0 38.6 5.6

 -----------------------------------------------------------------
 East: Barros Arana

 121 T1 60.0 60.0 60.0 60.0 31.2 0.0

 120 R2 60.0 20.2 20.2 60.0 31.2 5.8

 -----------------------------------------------------------------
```

Go to Table Links (Top)

Movement Capacity and Performance Parameters
Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

MOVEMENT CAPACITY PARAMETERS

 ------------------------------------------------
 Mov Turn Mov Arv Total Prac. Prac. Deg.
ID Cl. Flow Cap. Deg. Spare Satn
Satn Cap.
veh/h veh/h xp % x

 ------------------------------------------------
 South: Gral. Mackenna Sur

132 L2 # 457 500 0.90 -1 0.914

131 T1 # 1258 1377 0.90 -1 0.914

130 R2 # 255 279 0.90 -1 0.914

 ------------------------------------------------
 East: Barros Arana

121 T1 # 524 520 0.90 -11 1.007*

120 R2 # 20 20 0.90 -11 1.007*

 ------------------------------------------------
 Pedestrian Movements

P1 17 1200 0.90 0.014

P2 17 1200 0.90 0.014

P3 11 1200 0.90 0.009

P4 17 1200 0.90 0.014

 ------------------------------------------------
 * Maximum degree of saturation
# Combined Movement Capacity parameters are shown for all Movement Classes.

MOVEMENT PERFORMANCE

 --------------------------------------------------------------------------------
```

about:blank 14-11-2022

Detailed Output Page 4 of 11

```
 Mov Turn Total Total Aver. Eff. Total Perf. Tot.Trav. Tot.Trav. Aver.

 ID Delay Delay Delay Stop Stops Index Distance Time Speed
 (veh-h/h)(pers-h/h)(sec) Rate (veh-km/h)(veh-h/h) (km/h)

 --------------------------------------------------------------------------------
 South: Gral. Mackenna Sur

 132 L2 4.35 5.22 34.3 1.10 502.0 54.99 108.6 6.1 17.8

 131 T1 9.98 31.22 28.6 1.12 1406.3 91.76 300.6 15.7 19.2

 130 R2 2.42 2.90 34.1 1.13 288.3 51.22 77.2 3.5 21.8

 --------------------------------------------------------------------------------
 East: Barros Arana

 121 T1 10.31 12.37 70.8 1.52 799.2 54.05 156.8 13.0 12.1

 120 R2 0.43 0.51 76.6 1.52 30.5 37.39 6.0 0.5 11.7

 --------------------------------------------------------------------------------
 Pedestrian Movements

 P1 0.11 0.11 24.3 0.90 15.2 0.30 0.5 0.2 2.2

 P2 0.11 0.11 24.3 0.90 15.2 0.30 0.5 0.2 2.2

 P3 0.07 0.07 24.3 0.90 9.5 0.19 0.3 0.1 2.2

 P4 0.11 0.11 24.3 0.90 15.2 0.31 0.5 0.2 2.4

 --------------------------------------------------------------------------------
```

Go to Table Links (Top)

Fuel Consumption, Emissions and Cost
Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

FUEL CONSUMPTION, EMISSIONS AND COST (TOTAL)

 ---------------------------------------------------------------
Mov Turn Cost Fuel CO2 CO HC NOX

ID Total Total Total Total Total Total

$/h L/h kg/h kg/h kg/h kg/h

 ---------------------------------------------------------------
South: Gral. Mackenna Sur

132 L2 439.30 26.0 61.4 0.07 0.008 0.084

131 T1 1293.45 74.6 176.9 0.20 0.023 0.283

130 R2 275.89 16.1 38.1 0.05 0.005 0.060

 -----------------------------------------------
2008.63 116.6 276.4 0.32 0.035 0.427

 ---------------------------------------------------------------
East: Barros Arana

121 T1 517.36 41.6 98.2 0.09 0.011 0.148

120 R2 19.76 1.7 4.0 0.00 0.000 0.008

 -----------------------------------------------
537.12 43.3 102.2 0.10 0.011 0.155

 ---------------------------------------------------------------
Pedestrian Movements

P1 5.72

P2 5.72

P3 3.57

P4 6.03

 -----------------------------------------------
21.05

 ---------------------------------------------------------------
ALL VEHICLES: 2545.75 159.9 378.6 0.41 0.047 0.582

 ---------------------------------------------------------------
INTERSECTION: 2566.80 159.9 378.6 0.41 0.047 0.582

 ---------------------------------------------------------------
FUEL CONSUMPTION, EMISSIONS AND COST (RATE)

 ---------------------------------------------------------------
Mov Turn Cost Fuel CO2 CO HC NOX

ID Rate Rate Rate Rate Rate Rate

$/km L/100km g/km g/km g/km g/km

 ---------------------------------------------------------------
South: Gral. Mackenna Sur

132 L2 4.05 23.9 565.6 0.63 0.071 0.777

131 T1 4.30 24.8 588.5 0.67 0.076 0.941

130 R2 3.58 20.8 493.3 0.59 0.063 0.775

 -----------------------------------------------
4.13 24.0 568.3 0.65 0.073 0.878

 ---------------------------------------------------------------
East: Barros Arana

121 T1 3.30 26.5 626.2 0.59 0.069 0.942

120 R2 3.30 28.2 670.3 0.61 0.072 1.276

 -----------------------------------------------
3.30 26.6 627.8 0.59 0.069 0.955

 ---------------------------------------------------------------
Pedestrian Movements

P1 11.88

P2 11.88

P3 11.87

P4 11.23

 -----------------------------------------------
11.68

```

about:blank 14-11-2022

Detailed Output Page 5 of 11

```
 ---------------------------------------------------------------
 ALL VEHICLES: 3.92 24.6 583.2 0.63 0.072 0.897

 ---------------------------------------------------------------
 INTERSECTION: 3.95 24.6 583.2 0.63 0.072 0.897

 ---------------------------------------------------------------
```

Go to Table Links (Top)

**Lanes**

Lane Performance and Capacity Information
Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

LANE PERFORMANCE

 ---------------------------------------------------------------------------------------
 Effective Red and Satd Part Q u e u e
Green Times (sec) of Green Arv Cap Deg. Aver. Eff. 95% Back Lane
Lane ----------------- --------- Flow Satn Delay Stop ----------- Length
No. R1 G1 R2 G2 Gs1 Gs2 veh/h veh/h x sec Rate veh m m

 ---------------------------------------------------------------------------------------
 South: Gral. Mackenna Sur

1 25 35 28.5 986 1080 0.914 31.2 1.10 37.6 273.3 113.0

2 25 35 28.5 983 1076 0.914 30.0 1.13 37.5 275.3 113.0

 ---------------------------------------------------------------------------------------
 East: Barros Arana

1 43 17 17.0 544 540 1.007 71.0 1.52 29.9 215.1 176.0

 ---------------------------------------------------------------------------------------
 LANE FLOW AND CAPACITY INFORMATION

 --------------------------------------------------------------------------------
 Saturation Flow Rate

 ------------------------------
 With Lane W/O Lane

Lane Total Lane Adj. Blockage Blockage End Tot Deg. Lane
No. Arv Flow Width Basic 1st 2nd 1st 2nd Cap Cap Satn Util
veh/h m tcu/h veh/h veh/h veh/h veh/h veh/h veh/h x %

 --------------------------------------------------------------------------------
 South: Gral. Mackenna Sur

1 986 3.30 1950 1851 - 0 1080 0.914 100

2 983 3.30 1950 1844 - 0 1076 0.914 100

 --------------------------------------------------------------------------------
 East: Barros Arana

1 544 3.30 1950 1907 - 0 540 1.007 100

 --------------------------------------------------------------------------------
 Basic Saturation Flow in this table is adjusted for area type factor, lane width,
approach grade, parking manoeuvres and number of buses stopping.
Saturation flow scale (Demand & Sensitivity dialog) applies if specified.

Saturation Flow rates without (W/O) the effect of downstream lane blockage used for
signal timing purposes are included in this table when the signal timing option to
exclude downstream lane blockage effects is selected.

```

Go to Table Links (Top)

Lane, Approach and Intersection Performance
Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

 ---------------------------------------------------------------------
 Lane Arrival Adj. Eff Grn Deg Aver. Longest Lane
No. Flow %HV Basic (sec) Sat Delay Queue Length
(veh/h) Satf. 1st 2nd x sec m m

 ---------------------------------------------------------------------
 South: Gral. Mackenna Sur

1 986 5 1950 35 0.914 31.2 273 113

2 983 6 1950 35 0.914 30.0 275 113

 -------------------------------------------------------------
 1969 5 0.914 30.6 275

 ---------------------------------------------------------------------
 East: Barros Arana

1 544 3 1950 17 1.007 71.0 215 176

 -------------------------------------------------------------
 544 3 1.007 71.0 215

 ---------------------------------------------------------------------
 Pedestrians

P1 17 6 0.014 24.3 0.0

P2 17 6 0.014 24.3 0.0

```

about:blank 14-11-2022

Detailed Output Page 6 of 11

```
 P3 11 6 0.009 24.3 0.0

 P4 17 6 0.014 24.3 0.0

 ======================================================================

 ALL VEHICLES

 Total % Cycle Max Aver. Max
 Flow HV Time X Delay Queue
 2514 5 60 1.007 39.4 275

 ======================================================================

 Peak flow period = 30 minutes.

 Queue values in this table are 95% queue (metres)
 Note: Basic Saturation Flows (in through car units) have been adjusted for
 grade, lane widths, parking manoeuvres and bus stops.

```

Go to Table Links (Top)

Driver Characteristics

Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

 -------------------------------------------------------
 Average Driver
Lane Satn Satn Satn Satn Queue Response
No. Speed Flow Hdwy Spacing Space Time
km/h veh/h sec m m sec

 -------------------------------------------------------
 South: Gral. Mackenna Sur

1 31.3 1851 1.95 16.93 7.27 1.11

2 38.6 1844 1.95 20.91 7.35 1.27

 -------------------------------------------------------
 East: Barros Arana

1 44.1 1907 1.89 23.12 7.19 1.30

 -------------------------------------------------------
```

Go to Table Links (Top)

SCATS Parameters

Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

 ----------------------------------------------------------------------------
 Lane Stopline Capacity SCATS SCATS Hdwy Occ Space Deg. Lane
No. Flow Satn MF at MF Time Time Satn Util.

veh/h veh/h Flow sec sec sec x %

 ----------------------------------------------------------------------------
 South: Gral. Mackenna Sur

1 986 1080 1905 1709 2.11 1.03 1.07 0.914 100

2 983 1076 1924 1727 2.08 0.84 1.24 0.914 100

 ----------------------------------------------------------------------------
 East: Barros Arana

1 540 540 1947 1576 2.28 0.73 1.55 1.007 100

 ----------------------------------------------------------------------------
 STOPLINE FLOW: Departure flow rate in veh/h as measured at the stop line.
This cannot exceed capacity.

SCATS SATURATION FLOW: This allows for area type factor, lane width, approach grade and
turning vehicles. Saturation flow scale applies if specified (Demand & Sensitivity dialog).
The effects of movement class, parking manoeuvres, number of buses stopping
and conflicting pedestrian volume are not included.

SCATS MF: This emulates the MF (Maximum Flow) parameter used in the SCATS
control system. It is calculated from the SCATS SATURATION FLOW parameter.
The values estimated for conditions of low capacity per cycle where
the intergreen time is high relative to the green time may not be
representative of MF values reported by SCATS.

DEG. SATN: The Demand (Arrival) Flow Rate may exceed the Stopline Flow
Rate, therefore x > 1 is possible.

```

Go to Table Links (Top)

Lane Delays
Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

LANE DELAYS

 -------------------------------------------------------------------------------------------
 ------------------- Delay (seconds/veh) ------------------
```

about:blank 14-11-2022

Detailed Output Page 7 of 11

```
 Deg. % Arv Prog. Min Stop-line Delay Acc. Queuing Stopd
 Lane Satn During Factor Del 1st 2nd Total Dec. Total MvUp (Idle) Geom Control
 No. x Green dm d1 d2 dSL dn dq dqm di dig dic

 -------------------------------------------------------------------------------------------
 South: Gral. Mackenna Sur

 1 0.914 58.3 1.000 5.2 12.1 16.4 28.5 3.7 24.8 1.4 23.4 2.7 31.2

 2 0.914 58.3 1.000 5.2 12.1 16.4 28.6 4.2 24.3 2.2 22.2 1.4 30.0

 -------------------------------------------------------------------------------------------
 East: Barros Arana

 1 1.007 28.3 1.000 15.4 23.9 46.9 70.8 4.5 66.5 8.9 57.6 0.2 71.0

 -------------------------------------------------------------------------------------------
 SIDRA Standard Delay Model is used. Control Delay is the sum of Stop-line Delay
 and Geometric Delay.
 dm: Minimum delay for gap acceptance cases
 dSL: Stop-line delay (=d1+d2)
 dn: Average stop-start delay for all vehicles queued and unqueued
 dq: Queuing delay (the part of the stop-line delay that includes
 stopped delay and queue move-up delay)
 dqm: Queue move-up delay
 di: Stopped delay (stopped (idling) time at near-zero speed)
 dig: Geometric delay
 dic: Control delay

```

Go to Table Links (Top)

Lane Queues
Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

BACK OF QUEUE (VEHICLES)

 ---------------------------------------------------------------------------------------
 Deg. % Arv Prog. Ovrfl. Back of Queue (veh) Queue Stor. Prob. Prob.
Lane Satn During Factor Queue ----------------------- Ratio Block SL Ov.
No. x Green No Nb1 Nb2 Nb 95% Av. 95% % %

 ---------------------------------------------------------------------------------------
 South: Gral. Mackenna Sur

1 0.914 58.3 1.000 4.5 16.0 7.1 23.0 37.6 1.48 2.42 87.9 NA

2 0.914 58.3 1.000 4.5 15.9 7.0 23.0 37.5 1.49 2.44 88.6 NA

 ---------------------------------------------------------------------------------------
 East: Barros Arana

1 1.007 28.3 1.000 6.7 10.1 8.2 18.3 29.9 0.75 1.22 23.2 NA

 ---------------------------------------------------------------------------------------
 BACK OF QUEUE (DISTANCE)

 ---------------------------------------------------------------------------------------
 Deg. % Arv Prog. Ovrfl. Back of Queue (m) Queue Stor. Prob. Prob.
Lane Satn During Factor Queue ----------------------- Ratio Block SL Ov.
No. x Green No Nb1 Nb2 Nb 95% Av. 95% % %

 ---------------------------------------------------------------------------------------
 South: Gral. Mackenna Sur

1 0.914 58.3 1.000 33.0 116.2 51.3 167.5 273.3 1.48 2.42 87.9 NA

2 0.914 58.3 1.000 33.3 116.9 51.8 168.7 275.3 1.49 2.44 88.6 NA

 ---------------------------------------------------------------------------------------
 East: Barros Arana

1 1.007 28.3 1.000 48.4 72.8 59.0 131.8 215.1 0.75 1.22 23.2 NA

 ---------------------------------------------------------------------------------------
 OTHER QUEUE RESULTS (VEHICLES)

 -----------------------------------------------------------------
 Deg. % Arv Prog. Ovrfl. Queue Start Grn Cyc-Av. Queue
Lane Satn During Factor Queue --------------- ------------ No. x Green No Nr 95% Nc 95%

 -----------------------------------------------------------------
 South: Gral. Mackenna Sur

1 0.914 58.3 1.000 4.5 12.0 19.6 7.8 16.3

2 0.914 58.3 1.000 4.5 12.0 19.5 7.8 16.3

 -----------------------------------------------------------------
 East: Barros Arana

1 1.007 28.3 1.000 6.7 14.0 22.9 10.7 22.4

 -----------------------------------------------------------------
 OTHER QUEUE RESULTS (DISTANCE)

 -----------------------------------------------------------------
 Deg. % Arv Prog. Ovrfl. Queue Start Grn Cyc-Av. Queue
Lane Satn During Factor Queue --------------- ------------ No. x Green No Nr 95% Nc 95%

 -----------------------------------------------------------------
 South: Gral. Mackenna Sur

```

about:blank 14-11-2022

Detailed Output Page 8 of 11

```
 1 0.914 58.3 1.000 33.0 87.2 142.3 56.9 118.9

 2 0.914 58.3 1.000 33.3 87.9 143.4 57.4 119.9

 -----------------------------------------------------------------
 East: Barros Arana

 1 1.007 28.3 1.000 48.4 100.6 164.2 76.9 160.7

 -----------------------------------------------------------------
```

Go to Table Links (Top)

Lane Queue Percentiles
Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

LANE QUEUE PERCENTILES (VEHICLES)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (veh)

Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 South: Gral. Mackenna Sur

1 0.914 23.0 28.5 33.6 35.5 37.6 38.8 39.7

2 0.914 23.0 28.5 33.5 35.4 37.5 38.7 39.6

 -------------------------------------------------------------
 East: Barros Arana

1 1.007 18.3 22.8 26.8 28.3 29.9 31.0 31.7

 -------------------------------------------------------------
 LANE QUEUE PERCENTILES (DISTANCE)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (metres)

Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 South: Gral. Mackenna Sur

1 0.914 167.5 207.7 244.7 258.6 273.3 282.5 288.9

2 0.914 168.7 209.2 246.5 260.5 275.3 284.6 291.0

 -------------------------------------------------------------
 East: Barros Arana

1 1.007 131.8 163.5 192.6 203.6 215.1 222.4 227.4

 -------------------------------------------------------------
```

Go to Table Links (Top)

Lane Stops
Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

 ----------------------------------------------------------------------------------------------------
 Queue Total Aver.
Deg. % Arv Prog. -- Effective Stop Rate -- Total Move-up Queue Prop. Num. of
Lane Satn During Factor Geom. Overall Stops Rate Move-ups Queued Cycles to
No. x Green he1 he2 hig h H hqm Hqm pq Depart

 ----------------------------------------------------------------------------------------------------
 South: Gral. Mackenna Sur

1 0.914 58.3 1.000 0.89 0.20 0.01 1.10 1083.9 0.34 336.9 0.97 1.31

2 0.914 58.3 1.000 0.89 0.24 0.01 1.13 1112.6 0.34 336.8 0.97 1.31

 ----------------------------------------------------------------------------------------------------
 East: Barros Arana

1 1.007 28.3 1.000 0.87 0.65 0.00 1.52 829.7 1.11 603.4 1.00 2.11

 ----------------------------------------------------------------------------------------------------
 hig is the average value for all movements in a shared lane
hqm is average queue move-up rate for all vehicles queued and unqueued

```

Go to Table Links (Top)

**Flow Rates**

Origin-Destination Flow Rates (Total)
Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

```

about:blank 14-11-2022

Detailed Output Page 9 of 11

```
 TOTAL FLOW RATES for All Movement Classes (veh/h)

 ----------------------------------------------------------
 From SOUTH To: W N E

 Turn: L2 T1 R2 TOT

 Flow Rate 456.8 1257.9 254.7 1969.5

 %HV (all designations) 1.6 7.1 2.1 5.2

 ----------------------------------------------------------
 From EAST To: W N

 Turn: T1 R2 TOT

 Flow Rate 524.2 20.0 544.2

 %HV (all designations) 2.4 21.1 3.1

 --------------------------------------------------
 Flow rates shown above are Arrival Flow Rates (veh/h) based on the following input specifications:
 Unit Time for Volumes = 60 minutes

 Peak Flow Period = 30 minutes

 Effects of Volume Factors (Peak Flow Factor, Flow Scale, Growth Rate) are included.
 Arrival Flow Rates may be less than Demand Flow Rates if capacity constraint applies in
 network analysis.

```

Go to Table Links (Top)

Origin-Destination Flow Rates by Movement Class
Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

FLOW RATES for Light Vehicles (veh/h)

 --------------------------------------------------
 From SOUTH To: W N E

Turn: L2 T1 R2 TOT

 --------------------------------------------------
 Flow Rate 449.5 1168.4 249.5 1867.4

Mov Class % 98.4 92.9 97.9 94.8

Flow Scale 1.00 1.00 1.00
 Peak Flow Factor 0.95 0.95 0.95
 Residual Demand 0.0 0.0 0.0 0.0

 --------------------------------------------------
 From EAST To: W N

Turn: T1 R2 TOT

 ------------------------------------------
 Flow Rate 511.6 15.8 527.4

Mov Class % 97.6 78.9 96.9

Flow Scale 1.00 1.00
 Peak Flow Factor 0.95 0.95
 Residual Demand 3.7 0.1 3.9

 ------------------------------------------
 FLOW RATES for Heavy Vehicles (veh/h)

 --------------------------------------------------
 From SOUTH To: W N E

Turn: L2 T1 R2 TOT

 --------------------------------------------------
 Flow Rate 7.4 5.3 5.3 17.9

Mov Class % 1.6 0.4 2.1 0.9

Flow Scale 1.00 1.00 1.00
 Peak Flow Factor 0.95 0.95 0.95
 Residual Demand 0.0 0.0 0.0 0.0

 --------------------------------------------------
 From EAST To: W N

Turn: T1 R2 TOT

 ------------------------------------------
 Flow Rate 12.6 4.2 16.8

Mov Class % 2.4 21.1 3.1

Flow Scale 1.00 1.00
 Peak Flow Factor 0.95 0.95
 Residual Demand 0.1 0.0 0.1

 ------------------------------------------
 FLOW RATES for Buses (veh/h)

 --------------------------------------------------
 From SOUTH To: W N E

Turn: L2 T1 R2 TOT

 --------------------------------------------------
 Flow Rate * 84.2 * 84.2

Mov Class % * 6.7 * 4.3

Flow Scale * 1.00 *
 Peak Flow Factor * 0.95 *
 Residual Demand * 0.0 * 0.0

 --------------------------------------------------
 From EAST To: W N

Turn: T1 R2 TOT

 ------------------------------------------
 Flow Rate * * *

```

about:blank 14-11-2022

Detailed Output Page 10 of 11

```
 Mov Class % * * *

 Flow Scale * *
 Peak Flow Factor * *
 Residual Demand * * *

 ------------------------------------------
 * O-D Movement does not exist

 Flow rates shown above are Arrival Flow Rates (veh/h) based on the following input specifications:
 Unit Time for Volumes = 60 minutes

 Peak Flow Period = 30 minutes

 Effects of Volume Factors (Peak Flow Factor, Flow Scale, Growth Rate) are included.
 Arrival Flow Rates may be less than Demand Flow Rates if capacity constraint applies in
 network analysis.

```

Go to Table Links (Top)

Lane Flow Rates

Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

LANE FLOW RATES AT STOP LINE (veh/h)

 ------------------------------------------------
 From SOUTH To: W N E

Turn: L2 T1 R2 TOT

 ------------------------------------------------
 Lane 1

LV 449.5 492.0 * 941.4

HV 7.4 2.2 * 9.6

B * 35.5 * 35.5

Total 456.8 529.6 * 986.5

Lane 2

LV * 676.5 249.5 925.9

HV * 3.0 5.3 8.3

B * 48.8 * 48.8

Total * 728.3 254.7 983.0

 ------------------------------------------------
 Approach 456.8 1257.9 254.7 1969.5

 ------------------------------------------------
 From EAST To: W N

Turn: T1 R2 TOT

 ----------------------------------------
 Lane 1

LV 511.6 15.8 527.4

HV 12.6 4.2 16.8

Total 524.2 20.0 544.2

 ----------------------------------------
 Approach 524.2 20.0 544.2

 ----------------------------------------
 * Movement not allocated to the lane

EXIT LANE FLOW RATES

 ------------------------------------------------
 Movement Class: LV HV B TOT

 ------------------------------------------------
 Exit: EAST

Lane: 1 249.5 5.3 * 254.7

Total 249.5 5.3 * 254.7

 ------------------------------------------------
 Exit: NORTH

Lane: 1 498.3 3.9 35.5 537.6

Lane: 2 685.9 5.6 48.8 740.3

Total 1184.2 9.5 84.2 1277.9

 ------------------------------------------------
 Exit: WEST

Lane: 1 423.2 8.2 * 431.4

Lane: 2 288.3 6.0 * 294.3

Lane: 3 249.6 5.8 * 255.4

Total 961.1 20.0 * 981.1

 ------------------------------------------------
 * Movement not allocated to the lane

DOWNSTREAM LANE FLOW RATES FOR EXIT ROADS

 ------------------------------------------------
 Movement Class: LV HV B TOT

 ------------------------------------------------
 Exit: EAST

Lane: 1 249.5 5.3 * 254.7

Total 249.5 5.3 * 254.7

 ------------------------------------------------
 Exit: NORTH

Lane: 1 498.3 3.9 35.5 537.6

Lane: 2 685.9 5.6 48.8 740.3

```

about:blank 14-11-2022

Detailed Output Page 11 of 11

```
 Total 1184.2 9.5 84.2 1277.9

 ------------------------------------------------
 Exit: WEST

 Lane: 1 423.2 8.2 * 431.4

 Lane: 2 288.3 6.0 * 294.3

 Lane: 3 249.6 5.8 * 255.4

 Total 961.1 20.0 * 981.1

 ------------------------------------------------
 * Movement not allocated to the lane

 Flow rates shown above are Arrival Flow Rates (veh/h) based on the following input specifications:
 Unit Time for Volumes = 60 minutes

 Peak Flow Period = 30 minutes

 Effects of Volume Factors (Peak Flow Factor, Flow Scale, Growth Rate) are included.
 Arrival Flow Rates may be less than Demand Flow Rates if capacity constraint applies in
 network analysis.

```

Go to Table Links (Top)

**Other**

Parameter Settings Summary
Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

* Basic Parameters:

Intersection Type: Signalised - Fixed Time Isolated
Driving on the right-hand side of the road
Input data specified in Metric units
Model Defaults: Standard Right
Peak Flow Period (for performance): 30 minutes
Unit time (for volumes): 60 minutes.
SIDRA Standard Delay model used
SIDRA Standard Queue model used
Level of Service based on: Delay (SIDRA)
Queue percentile: 95%

```

Go to Table Links (Top)

Diagnostics
Site: 1-Gral. Mackenna/San Martín-PML

```
Site ID: 1

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

Main (Timing-Capacity) Iterations for Signals

Site Model Variability Index (Iterations 3 to N): 0.0%
Number of Iterations: 2 (Maximum: 10)
Largest difference in Movement Effective Green Times in the last two Main Iterations: 0 secs
(stopping condition: 0 secs)

Lane Flow-Capacity Iterations:

Flow-Capacity Iteration Variability Index (Iterations 3 to N): 0.0%
Number of Iterations: 2 (Maximum: 10)
For Signals, the results for "Lane Flow-Capacity Iterations" are reported
for the last Main (Timing-Capacity) Iteration.

Other Diagnostic Messages (if any):

```

Go to Table Links (Top)

**SIDRA INTERSECTION 8.0 | Copyright © 2000-2018 Akcelik and Associates Pty Ltd | sidrasolutions.com**
Organisation: Fenerbahce | Processed: jueves, 10 de noviembre de 2022 9:48:25
Project: C:\Users\gomez\OneDrive\Escritorio\Benj\Transvia\San Martín\San Martín.sip8

about:blank 14-11-2022