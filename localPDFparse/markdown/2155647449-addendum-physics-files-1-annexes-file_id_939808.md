---
title: about:blank
author: gomez
date: D:20221114104739-03'00'
language: en
type: report
pages: 12
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Combined Movement Capacity parameters are shown for all Movement Classes.
-->

Detailed Output Page 1 of 12

**DETAILED OUTPUT**

**Site: 3 [3-San Martín/Carrera-PML]**

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
Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

 ----------------------------------------------------------------------------------------------------
 Mov Mov Mov P H A S E M A T R I X Lost Tim Req.Mov.Time Eff. Grn
ID Cl. Typ First Green Second Green -------- ------------ ------- ----------------------- ----------------------- 1st 2nd 1st 2nd 1st 2nd

Fr To Op Pr Und Fr To Op Pr Und Grn Grn Grn Grn Grn Grn

 ----------------------------------------------------------------------------------------------------
 East: San Martín Oriente

4 # A B 5 20.4 30

5 # *A B 5 20.4 30

 ----------------------------------------------------------------------------------------------------
 North: Carrera Norte

8 # B A 5 18.0 Min 20

9 # *B A 5 18.0 Min 20

 ----------------------------------------------------------------------------------------------------
 Pedestrian Movements

P1 (Ped) A B 10 16.0 Min 6
P2 (Ped) B A 12 18.0 Min 6
P3 (Ped) A B 10 16.0 Min 6
P4 (Ped) B A 12 18.0 Min 6

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

Detailed Output Page 2 of 12

```
 ---------------------------------------------------------------------------------
 Crit App Green Phases Adjusted Adjusted Required Required
 Mov and Period ------ Lost Flow Grn Time Movement

 ID Turn Dest Fr To Time Ratio Ratio Time

 ---------------------------------------------------------------------------------
 5LV T1 E_W A B 5 0.230 0.256 20.4
 9LV R2 N_W B A 18 - - 18.0Min

 ---- ------ ------ -----
 Total: 23 0.230 0.256 38.4

 ---------------------------------------------------------------------------------
 - Flow ratio not used for cycle time calculations and
 the adjusted lost time equals the required movement time
 (=Min or Max as shown in Movement Timing Information)

 Cycle Time:
 Minimum Maximum Practical Chosen

 34 150 34 60

 (Phase times user specified, cycle time = sum of phase times)

```

Go to Table Links (Top)

Phase Information

Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

PHASE INFORMATION

 ---------------------------------------------------------------------------------
 Phase Ref. Change Starting Green Displayed Green Terminating Phase Phase
Phase Time Intgrn Start Green End Intgrn Time Split

 ---------------------------------------------------------------------------------
 A Yes 0 5 5 30 35 5 35 58%

B No 35 5 40 20 60 5 25 42%

 ---------------------------------------------------------------------------------
 (Phase times specified by the user)
Current Phase Sequence: Variable Phasing
Input Phase Sequence: A B
Output Phase Sequence: A B

PHASE YELLOW AND ALL-RED TIMES (INPUT)

 -----------------------
 Phase A B

Yellow Time 3 3

All-Red Time 2 2

Intergreen Time 5 5

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
Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

TRAVEL SPEED, TRAVEL DISTANCE AND TRAVEL TIME

 -----------------------------------------------------------------------------------------------
 Running Travel Travel Travel Total Travel Distance Tot.Trav.
From To Speed Speed Distance Time Dem Flows Arv Flows Time
Approach Exit Turn km/h km/h m s veh-km/h veh-km/h veh-h/h

 -----------------------------------------------------------------------------------------------
 East: San Martín Oriente

South L2 36.2 27.0 240.0# 32.0# 50.5 50.5 1.9

West T1 41.9 30.5 240.0# 28.4# 265.8 265.8 8.7

 -----------------------------------------------------------------------------------------------
 North: Carrera Norte

South T1 42.0 26.3 243.2# 33.2# 34.8 34.8 1.3

West R2 33.9 22.7 245.7# 39.0# 40.3 40.3 1.8

 -----------------------------------------------------------------------------------------------
 ALL VEHICLES: 40.4 28.6 240.9# 30.3# 391.5 391.5 13.7

 -----------------------------------------------------------------------------------------------
 "Running Speed" is the average speed excluding stopped periods.

```

about:blank 14-11-2022

Detailed Output Page 3 of 12

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
 East: San Martín Oriente

 South L2 5.0 15.5 10.0 115 115 NA

 West T1 S 50.0 10.0 115 115 NA

 -----------------------------------------------------------------------
 North: Carrera Norte

 South T1 S 50.0 13.2 115 115 NA

 West R2 10.0 20.2 15.7 115 115 NA

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
 East: San Martín Oriente

 4 L2 50.0 15.5 15.5 50.0 26.8 4.9

 5 T1 50.0 50.0 50.0 50.0 35.3 0.0

 -----------------------------------------------------------------
 North: Carrera Norte

 8 T1 50.0 50.0 50.0 50.0 33.8 0.0

 9 R2 50.0 20.2 20.2 50.0 20.2 4.6

 -----------------------------------------------------------------
```

Go to Table Links (Top)

Movement Capacity and Performance Parameters
Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

MOVEMENT CAPACITY PARAMETERS

 ------------------------------------------------
 Mov Turn Mov Arv Total Prac. Prac. Deg.
ID Cl. Flow Cap. Deg. Spare Satn
Satn Cap.
veh/h veh/h xp % x

 ------------------------------------------------
 East: San Martín Oriente

4 L2 # 211 457 0.90 95 0.461*

5 T1 # 1107 2402 0.90 95 0.461*

 ------------------------------------------------
 North: Carrera Norte

8 T1 # 143 650 0.90 309 0.220

9 R2 # 164 619 0.90 239 0.265

 ------------------------------------------------
 Pedestrian Movements

P1 53 1200 0.90 0.044

P2 53 1200 0.90 0.044

P3 53 1200 0.90 0.044

P4 53 1200 0.90 0.044

 ------------------------------------------------
 * Maximum degree of saturation
# Combined Movement Capacity parameters are shown for all Movement Classes.

MOVEMENT PERFORMANCE

 --------------------------------------------------------------------------------
 Mov Turn Total Total Aver. Eff. Total Perf. Tot.Trav. Tot.Trav. Aver.

ID Delay Delay Delay Stop Stops Index Distance Time Speed

```

about:blank 14-11-2022

Detailed Output Page 4 of 12

```
 (veh-h/h)(pers-h/h)(sec) Rate (veh-km/h)(veh-h/h) (km/h)

 --------------------------------------------------------------------------------
 East: San Martín Oriente

 4 L2 0.91 1.09 15.5 0.70 146.6 7.85 50.5 1.9 27.0

 5 T1 3.26 5.25 10.6 0.62 690.4 27.95 265.8 8.7 30.5

 --------------------------------------------------------------------------------
 North: Carrera Norte

 8 T1 0.63 0.75 15.7 0.61 87.5 3.69 34.8 1.3 26.3

 9 R2 0.94 1.13 20.6 0.75 123.1 4.63 40.3 1.8 22.7

 --------------------------------------------------------------------------------
 Pedestrian Movements

 P1 0.36 0.36 24.4 0.90 47.5 0.94 1.5 0.7 2.2

 P2 0.36 0.36 24.4 0.90 47.5 0.98 1.7 0.7 2.3

 P3 0.36 0.36 24.4 0.90 47.5 0.94 1.5 0.7 2.2

 P4 0.36 0.36 24.4 0.90 47.5 0.98 1.7 0.7 2.3

 --------------------------------------------------------------------------------
```

Go to Table Links (Top)

Fuel Consumption, Emissions and Cost
Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

FUEL CONSUMPTION, EMISSIONS AND COST (TOTAL)

 ---------------------------------------------------------------
 Mov Turn Cost Fuel CO2 CO HC NOX

ID Total Total Total Total Total Total

$/h L/h kg/h kg/h kg/h kg/h

 ---------------------------------------------------------------
 East: San Martín Oriente

4 L2 75.96 7.1 16.8 0.01 0.002 0.011

5 T1 405.91 36.6 86.5 0.08 0.009 0.091

 -----------------------------------------------
 481.87 43.7 103.2 0.09 0.010 0.103

 ---------------------------------------------------------------
 North: Carrera Norte

8 T1 48.08 4.6 10.9 0.01 0.001 0.004

9 R2 65.28 6.2 14.7 0.01 0.001 0.005

 -----------------------------------------------
 113.36 10.9 25.6 0.02 0.002 0.009

 ---------------------------------------------------------------
 Pedestrian Movements

P1 17.89

P2 18.87

P3 17.89

P4 18.87

 -----------------------------------------------
 73.52

 ---------------------------------------------------------------
 ALL VEHICLES: 595.23 54.6 128.9 0.12 0.013 0.112

 ---------------------------------------------------------------
 INTERSECTION: 668.75 54.6 128.9 0.12 0.013 0.112

 ---------------------------------------------------------------
 FUEL CONSUMPTION, EMISSIONS AND COST (RATE)

 ---------------------------------------------------------------
 Mov Turn Cost Fuel CO2 CO HC NOX

ID Rate Rate Rate Rate Rate Rate

$/km L/100km g/km g/km g/km g/km

 ---------------------------------------------------------------
 East: San Martín Oriente

4 L2 1.50 14.1 331.7 0.29 0.032 0.227

5 T1 1.53 13.8 325.4 0.30 0.032 0.344

 -----------------------------------------------
 1.52 13.8 326.4 0.30 0.032 0.325

 ---------------------------------------------------------------
 North: Carrera Norte

8 T1 1.38 13.3 313.6 0.26 0.029 0.104

9 R2 1.62 15.5 364.0 0.31 0.035 0.130

 -----------------------------------------------
 1.51 14.5 340.7 0.28 0.032 0.118

 ---------------------------------------------------------------
 Pedestrian Movements

P1 11.89

P2 11.24

P3 11.89

P4 11.24

 -----------------------------------------------
 11.54

 ---------------------------------------------------------------
 ALL VEHICLES: 1.52 14.0 329.2 0.29 0.032 0.285

 ---------------------------------------------------------------
 INTERSECTION: 1.71 14.0 329.2 0.29 0.032 0.285

 ---------------------------------------------------------------
```

about:blank 14-11-2022

Detailed Output Page 5 of 12

Go to Table Links (Top)

**Lanes**

Lane Performance and Capacity Information
Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

LANE PERFORMANCE

 ---------------------------------------------------------------------------------------
 Effective Red and Satd Part Q u e u e
Green Times (sec) of Green Arv Cap Deg. Aver. Eff. 95% Back Lane
Lane ----------------- --------- Flow Satn Delay Stop ----------- Length
No. R1 G1 R2 G2 Gs1 Gs2 veh/h veh/h x sec Rate veh m m

 ---------------------------------------------------------------------------------------
 East: San Martín Oriente

1 30 30 9.0 435 943 0.461 13.0 0.70 8.4 59.2 115.0

2 30 30 9.0 442 958 0.461 10.6 0.60 8.5 60.7 115.0

3 30 30 9.0 442 958 0.461 10.6 0.60 8.5 60.7 115.0

 ---------------------------------------------------------------------------------------
 North: Carrera Norte

1 40 20 3.2 143 650 0.220 15.7 0.61 3.1 21.4 115.0

2 40 20 3.9 164 619 0.265 20.6 0.75 3.6 25.1 115.0

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
 East: San Martín Oriente

1 435 3.30 1950 1887 - 0 943 0.461 100

2 442 3.30 1950 1916 - 0 958 0.461 100

3 442 3.30 1950 1916 - 0 958 0.461 100

 --------------------------------------------------------------------------------
 North: Carrera Norte

1 143 3.30 1950 1950 - 0 650 0.220 83P

2 164 3.30 1950 1857 - 0 619 0.265 100

 --------------------------------------------------------------------------------
 P Lane under-utilisation found by the Program

Basic Saturation Flow in this table is adjusted for area type factor, lane width,
approach grade, parking manoeuvres and number of buses stopping.
Saturation flow scale (Demand & Sensitivity dialog) applies if specified.

Saturation Flow rates without (W/O) the effect of downstream lane blockage used for
signal timing purposes are included in this table when the signal timing option to
exclude downstream lane blockage effects is selected.

```

Go to Table Links (Top)

Lane, Approach and Intersection Performance
Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

 ---------------------------------------------------------------------
 Lane Arrival Adj. Eff Grn Deg Aver. Longest Lane
No. Flow %HV Basic (sec) Sat Delay Queue Length
(veh/h) Satf. 1st 2nd x sec m m

 ---------------------------------------------------------------------
 East: San Martín Oriente

1 435 1 1950 30 0.461 13.0 59 115

2 442 3 1950 30 0.461 10.6 61 115

3 442 3 1950 30 0.461 10.6 61 115

 -------------------------------------------------------------
 1318 2 0.461 11.4 61

 ---------------------------------------------------------------------
 North: Carrera Norte

1 143 0 1950 20 0.220 15.7 21 115

2 164 0 1950 20 0.265 20.6 25 115

 -------------------------------------------------------------
 307 0 0.265 18.3 25

 ---------------------------------------------------------------------
 Pedestrians

```

about:blank 14-11-2022

Detailed Output Page 6 of 12

```
 P1 53 6 0.044 24.4 0.1

 P2 53 6 0.044 24.4 0.1

 P3 53 6 0.044 24.4 0.1

 P4 53 6 0.044 24.4 0.1

 ======================================================================

 ALL VEHICLES

 Total % Cycle Max Aver. Max
 Flow HV Time X Delay Queue
 1625 2 60 0.461 12.7 61

 ======================================================================

 Peak flow period = 30 minutes.

 Queue values in this table are 95% queue (metres)
 Note: Basic Saturation Flows (in through car units) have been adjusted for
 grade, lane widths, parking manoeuvres and bus stops.

```

Go to Table Links (Top)

Driver Characteristics

Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

 -------------------------------------------------------
 Average Driver
Lane Satn Satn Satn Satn Queue Response
No. Speed Flow Hdwy Spacing Space Time
km/h veh/h sec m m sec

 -------------------------------------------------------
 East: San Martín Oriente

1 26.8 1887 1.91 14.23 7.09 0.96

2 37.5 1916 1.88 19.58 7.17 1.19

3 37.5 1916 1.88 19.58 7.17 1.19

 -------------------------------------------------------
 North: Carrera Norte

1 37.5 1950 1.85 19.23 7.00 1.17

2 20.2 1857 1.94 10.86 7.00 0.69

 -------------------------------------------------------
```

Go to Table Links (Top)

SCATS Parameters

Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

 ----------------------------------------------------------------------------
 Lane Stopline Capacity SCATS SCATS Hdwy Occ Space Deg. Lane
No. Flow Satn MF at MF Time Time Satn Util.

veh/h veh/h Flow sec sec sec x %

 ----------------------------------------------------------------------------
 East: San Martín Oriente

1 435 943 1903 1631 2.21 1.21 1.00 0.461 100

2 442 958 1950 1671 2.15 0.86 1.29 0.461 100

3 442 958 1950 1671 2.15 0.86 1.29 0.461 100

 ----------------------------------------------------------------------------
 North: Carrera Norte

1 143 650 1950 1560 2.31 0.86 1.44 0.220 83P

2 164 619 1857 1486 2.42 1.61 0.82 0.265 100

 ----------------------------------------------------------------------------
 P Lane under-utilisation found by the "Program". This includes cases where
the value of lane under-utilisation due to downstream effects has been

modified by the program during lane flow calculations (e.g. a de facto
exclusive lane has been found).

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

about:blank 14-11-2022

Detailed Output Page 7 of 12

Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

LANE DELAYS

 -------------------------------------------------------------------------------------------
 ------------------- Delay (seconds/veh) ------------------ Deg. % Arv Prog. Min Stop-line Delay Acc. Queuing Stopd
Lane Satn During Factor Del 1st 2nd Total Dec. Total MvUp (Idle) Geom Control
No. x Green dm d1 d2 dSL dn dq dqm di dig dic

 -------------------------------------------------------------------------------------------
 East: San Martín Oriente

1 0.461 50.0 1.000 7.5 10.6 0.0 10.6 2.5 8.1 0.0 8.1 2.4 13.0

2 0.461 50.0 1.000 7.5 10.6 0.0 10.6 2.9 7.7 0.0 7.7 0.0 10.6

3 0.461 50.0 1.000 7.5 10.6 0.0 10.6 2.9 7.7 0.0 7.7 0.0 10.6

 -------------------------------------------------------------------------------------------
 North: Carrera Norte

1 0.220 33.3 1.000 13.3 15.7 0.0 15.7 3.3 12.4 0.0 12.4 0.0 15.7

2 0.265 33.3 1.000 13.3 16.1 0.0 16.1 3.1 12.9 0.0 12.9 4.6 20.6

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
Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

BACK OF QUEUE (VEHICLES)

 ---------------------------------------------------------------------------------------
 Deg. % Arv Prog. Ovrfl. Back of Queue (veh) Queue Stor. Prob. Prob.
Lane Satn During Factor Queue ----------------------- Ratio Block SL Ov.
No. x Green No Nb1 Nb2 Nb 95% Av. 95% % %

 ---------------------------------------------------------------------------------------
 East: San Martín Oriente

1 0.461 50.0 1.000 0.0 5.1 0.0 5.1 8.4 0.32 0.51 0.0 NA

2 0.461 50.0 1.000 0.0 5.2 0.0 5.2 8.5 0.32 0.53 0.0 NA

3 0.461 50.0 1.000 0.0 5.2 0.0 5.2 8.5 0.32 0.53 0.0 NA

 ---------------------------------------------------------------------------------------
 North: Carrera Norte

1 0.220 33.3 1.000 0.0 1.9 0.0 1.9 3.1 0.11 0.19 0.0 NA

2 0.265 33.3 1.000 0.0 2.2 0.0 2.2 3.6 0.13 0.22 0.0 NA

 ---------------------------------------------------------------------------------------
 BACK OF QUEUE (DISTANCE)

 ---------------------------------------------------------------------------------------
 Deg. % Arv Prog. Ovrfl. Back of Queue (m) Queue Stor. Prob. Prob.
Lane Satn During Factor Queue ----------------------- Ratio Block SL Ov.
No. x Green No Nb1 Nb2 Nb 95% Av. 95% % %

 ---------------------------------------------------------------------------------------
 East: San Martín Oriente

1 0.461 50.0 1.000 0.0 36.3 0.0 36.3 59.2 0.32 0.51 0.0 NA

2 0.461 50.0 1.000 0.0 37.2 0.0 37.2 60.7 0.32 0.53 0.0 NA

3 0.461 50.0 1.000 0.0 37.2 0.0 37.2 60.7 0.32 0.53 0.0 NA

 ---------------------------------------------------------------------------------------
 North: Carrera Norte

1 0.220 33.3 1.000 0.0 13.1 0.0 13.1 21.4 0.11 0.19 0.0 NA

2 0.265 33.3 1.000 0.0 15.4 0.0 15.4 25.1 0.13 0.22 0.0 NA

 ---------------------------------------------------------------------------------------
 OTHER QUEUE RESULTS (VEHICLES)

 -----------------------------------------------------------------
 Deg. % Arv Prog. Ovrfl. Queue Start Grn Cyc-Av. Queue
Lane Satn During Factor Queue --------------- ------------ No. x Green No Nr 95% Nc 95%

 -----------------------------------------------------------------
 East: San Martín Oriente

1 0.461 50.0 1.000 0.0 3.9 6.4 1.3 2.7

```

about:blank 14-11-2022

Detailed Output Page 8 of 12

```
 2 0.461 50.0 1.000 0.0 4.0 6.5 1.3 2.7

 3 0.461 50.0 1.000 0.0 4.0 6.5 1.3 2.7

 -----------------------------------------------------------------
 North: Carrera Norte

 1 0.220 33.3 1.000 0.0 1.7 2.8 0.6 1.3

 2 0.265 33.3 1.000 0.0 2.0 3.3 0.7 1.5

 -----------------------------------------------------------------
 OTHER QUEUE RESULTS (DISTANCE)

 -----------------------------------------------------------------
 Deg. % Arv Prog. Ovrfl. Queue Start Grn Cyc-Av. Queue
 Lane Satn During Factor Queue --------------- ------------ No. x Green No Nr 95% Nc 95%

 -----------------------------------------------------------------
 East: San Martín Oriente

 1 0.461 50.0 1.000 0.0 27.9 45.6 9.1 18.9

 2 0.461 50.0 1.000 0.0 28.6 46.7 9.3 19.4

 3 0.461 50.0 1.000 0.0 28.6 46.7 9.3 19.4

 -----------------------------------------------------------------
 North: Carrera Norte

 1 0.220 33.3 1.000 0.0 12.2 19.9 4.4 9.2

 2 0.265 33.3 1.000 0.0 14.0 22.9 5.1 10.7

 -----------------------------------------------------------------
```

Go to Table Links (Top)

Lane Queue Percentiles
Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

LANE QUEUE PERCENTILES (VEHICLES)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (veh)

Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 East: San Martín Oriente

1 0.461 5.1 6.3 7.5 7.9 8.4 8.6 8.8

2 0.461 5.2 6.4 7.6 8.0 8.5 8.8 9.0

3 0.461 5.2 6.4 7.6 8.0 8.5 8.8 9.0

 -------------------------------------------------------------
 North: Carrera Norte

1 0.220 1.9 2.3 2.7 2.9 3.1 3.2 3.2

2 0.265 2.2 2.7 3.2 3.4 3.6 3.7 3.8

 -------------------------------------------------------------
 LANE QUEUE PERCENTILES (DISTANCE)

 -------------------------------------------------------------
 Deg. Percentile Back of Queue (metres)

Lane Satn -----------------------------------------------
 No. x 50% 70% 85% 90% 95% 98% 100%

 -------------------------------------------------------------
 East: San Martín Oriente

1 0.461 36.3 45.0 53.0 56.0 59.2 61.2 62.6

2 0.461 37.2 46.2 54.4 57.5 60.7 62.8 64.2

3 0.461 37.2 46.2 54.4 57.5 60.7 62.8 64.2

 -------------------------------------------------------------
 North: Carrera Norte

1 0.220 13.1 16.3 19.2 20.3 21.4 22.2 22.7

2 0.265 15.4 19.1 22.5 23.7 25.1 25.9 26.5

 -------------------------------------------------------------
```

Go to Table Links (Top)

Lane Stops
Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

 ----------------------------------------------------------------------------------------------------
 Queue Total Aver.
Deg. % Arv Prog. -- Effective Stop Rate -- Total Move-up Queue Prop. Num. of
Lane Satn During Factor Geom. Overall Stops Rate Move-ups Queued Cycles to
No. x Green he1 he2 hig h H hqm Hqm pq Depart

 ----------------------------------------------------------------------------------------------------
 East: San Martín Oriente

```

about:blank 14-11-2022

Detailed Output Page 9 of 12

```
 1 0.461 50.0 1.000 0.60 0.00 0.09 0.70 302.8 0.00 0.0 0.69 0.69

 2 0.461 50.0 1.000 0.60 0.00 0.00 0.60 267.1 0.00 0.0 0.69 0.69

 3 0.461 50.0 1.000 0.60 0.00 0.00 0.60 267.1 0.00 0.0 0.69 0.69

 ----------------------------------------------------------------------------------------------------
 North: Carrera Norte

 1 0.220 33.3 1.000 0.61 0.00 0.00 0.61 87.5 0.00 0.0 0.76 0.76

 2 0.265 33.3 1.000 0.63 0.00 0.12 0.75 123.1 0.00 0.0 0.77 0.77

 ----------------------------------------------------------------------------------------------------
 hig is the average value for all movements in a shared lane
 hqm is average queue move-up rate for all vehicles queued and unqueued

```

Go to Table Links (Top)

**Flow Rates**

Origin-Destination Flow Rates (Total)
Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

TOTAL FLOW RATES for All Movement Classes (veh/h)

 --------------------------------------------------
 From EAST To: S W

Turn: L2 T1 TOT

Flow Rate 210.5 1107.4 1317.9

%HV (all designations) 0.0 2.8 2.3

 --------------------------------------------------
 From NORTH To: S W

Turn: T1 R2 TOT

Flow Rate 143.2 164.2 307.4

%HV (all designations) 0.0 0.0 0.0

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
Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

FLOW RATES for Light Vehicles (veh/h)

 ------------------------------------------
 From EAST To: S W

Turn: L2 T1 TOT

 ------------------------------------------
 Flow Rate 210.5 1076.8 1287.4

Mov Class % 100.0 97.2 97.7

Flow Scale 1.00 1.00
 Peak Flow Factor 0.95 0.95
 Residual Demand 0.0 0.0 0.0

 ------------------------------------------
 From NORTH To: S W

Turn: T1 R2 TOT

 ------------------------------------------
 Flow Rate 143.2 164.2 307.4

Mov Class % 100.0 100.0 100.0

Flow Scale 1.00 1.00
 Peak Flow Factor 0.95 0.95
 Residual Demand 0.0 0.0 0.0

 ------------------------------------------
 FLOW RATES for Heavy Vehicles (veh/h)

 ------------------------------------------
 From EAST To: S W

Turn: L2 T1 TOT

 ------------------------------------------
 Flow Rate 0.0 14.7 14.7

Mov Class % 0.0 1.3 1.1

Flow Scale 1.00 1.00
 Peak Flow Factor 0.95 0.95
 Residual Demand 0.0 0.0 0.0

 ------------------------------------------
 From NORTH To: S W

```

about:blank 14-11-2022

Detailed Output Page 10 of 12

```
 Turn: T1 R2 TOT

 ------------------------------------------
 Flow Rate 0.0 0.0 0.0

 Mov Class % 0.0 0.0 0.0

 Flow Scale 1.00 1.00
 Peak Flow Factor 0.95 0.95
 Residual Demand 0.0 0.0 0.0

 ------------------------------------------
 FLOW RATES for Buses (veh/h)

 ------------------------------------------
 From EAST To: S W

 Turn: L2 T1 TOT

 ------------------------------------------
 Flow Rate * 15.8 15.8

 Mov Class % * 1.4 1.2

 Flow Scale * 1.00
 Peak Flow Factor * 0.95
 Residual Demand * 0.0 0.0

 ------------------------------------------
 From NORTH To: S W

 Turn: T1 R2 TOT

 ------------------------------------------
 Flow Rate * * *

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

Site: 3-San Martín/Carrera-PML

```
Site ID: 3

Signals - Fixed-Time Isolated Cycle Time = 60 sec (Site User-Given Phase Times)

LANE FLOW RATES AT STOP LINE (veh/h)

 ----------------------------------------
From EAST To: S W

Turn: L2 T1 TOT

 ----------------------------------------
Lane 1

LV 210.5 218.2 428.7

HV * 3.0 3.0

B * 3.2 3.2

Total 210.5 224.3 434.9

Lane 2

LV * 429.3 429.3

HV * 5.9 5.9

B * 6.3 6.3

Total * 441.5 441.5

Lane 3

LV * 429.3 429.3

HV * 5.9 5.9

B * 6.3 6.3

Total * 441.5 441.5

 ----------------------------------------
Approach 210.5 1107.4 1317.9

 ----------------------------------------
From NORTH To: S W

Turn: T1 R2 TOT

 ----------------------------------------
Lane 1

LV 143.2 * 143.2

Total 143.2 * 143.2

Lane 2

LV * 164.2 164.2

Total * 164.2 164.2

 ----------------------------------------
Approach 143.2 164.2 307.4

 ----------------------------------------
* Movement not allocated to the lane

EXIT LANE FLOW RATES

 ------------------------------------------------
```

about:blank 14-11-2022

Detailed Output Page 11 of 12

```
 Movement Class: LV HV B TOT

 ------------------------------------------------
 Exit: SOUTH

 Lane: 1 353.7 * * 353.7

 Lane: 2 * * * 0.0

 Total 353.7 * * 353.7

 ------------------------------------------------
 Exit: WEST

 Lane: 1 218.2 3.0 3.2 224.3

 Lane: 2 429.3 5.9 6.3 441.5

 Lane: 3 593.5 5.9 6.3 605.7

 Total 1241.1 14.7 15.8 1271.6

 ------------------------------------------------
 * Movement not allocated to the lane

 DOWNSTREAM LANE FLOW RATES FOR EXIT ROADS

 ------------------------------------------------
 Movement Class: LV HV B TOT

 ------------------------------------------------
 Exit: SOUTH

 Lane: 1 353.7 * * 353.7

 Total 353.7 * * 353.7

 ------------------------------------------------
 Exit: WEST

 Lane: 1 218.2 3.0 3.2 224.3

 Lane: 2 429.3 5.9 6.3 441.5

 Lane: 3 593.5 5.9 6.3 605.7

 Total 1241.1 14.7 15.8 1271.6

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
Site: 3-San Martín/Carrera-PML

```
Site ID: 3

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
Site: 3-San Martín/Carrera-PML

```
Site ID: 3

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

about:blank 14-11-2022

Detailed Output Page 12 of 12

Go to Table Links (Top)

**SIDRA INTERSECTION 8.0 | Copyright © 2000-2018 Akcelik and Associates Pty Ltd | sidrasolutions.com**
Organisation: Fenerbahce | Processed: viernes, 11 de noviembre de 2022 13:34:33
Project: C:\Users\gomez\OneDrive\Escritorio\Benj\Transvia\San Martín\Centro Bello.sip8

about:blank 14-11-2022