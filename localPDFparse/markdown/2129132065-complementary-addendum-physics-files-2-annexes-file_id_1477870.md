---
title: Sin título
author: Desconocido
date: D:20131124155937-04'00'
language: en
type: manual
pages: 4
has_toc: False
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Output Tables
-->

Output Tables Página 1 de 4

# Output Tables

## Interseccion Calle servicio con Acceso Planta PF 3

**Siuacion Base punta Tarde**

**Run Information**

```
 * Basic Parameters:

 Intersection Type: Unsignalised - Two-Way Stop Control
 Driving on the right-hand side of the road
 Input data specified in Metric units
 Model Defaults: Standard Right
 Peak Flow Period (for performance): 15 minutes
 Unit time (for volumes): 60 minutes.
 Delay definition: Control delay
 Geometric delay included
 SIDRA Standard Delay model used

 SIDRA Standard Queue model used

 Level of Service based on: Delay and degree of saturation
 Queue definition: Back of queue, 95th Percentile

```

**Table B.1 - Movement Definitions and Flow Rates (Origin-Destination)**

```
 Interseccion Calle servicio con Acceso Planta PF 3

 Siuacion Base punta Tarde

 Intersection ID: 1

 Stop Sign Controlled Intersection

 ----------------------------------------------------------------
 From To Mov Flow Rate Flow Peak Flow

 Approach Approach ID Turn LV HV Scale Factor

 ----------------------------------------------------------------
 South: desde calle 10 Norte

 East 32 Right 2 1 1.00 0.95

 North 31 Thru 31 3 1.00 0.95

 ----------------------------------------------------------------
 East: desde Acceso Planta

 South 23 Left 2 1 1.00 0.95

 North 21 Right 38 2 1.00 0.95

 ----------------------------------------------------------------
 North: Desde Enlace

 South 13 Thru 66 13 1.00 0.95

 East 12 Left 1 4 1.00 0.95

 ----------------------------------------------------------------
 Unit Time for Volumes = 60 minutes

 Peak Flow Period = 15 minutes

 Flow Rates include effects of Flow Scale and Peak Flow Factor

```

**Table B.2A - Flow Rates (Separate Light and Heavy Vehicles)**

about:blank 24-11-2013

Output Tables Página 2 de 4

```
 Interseccion Calle servicio con Acceso Planta PF 3

 Siuacion Base punta Tarde

 Intersection ID: 1

 Stop Sign Controlled Intersection

 ----------------------------------------------
 Mov Left Through Right

 ID --------- --------- --------
 LV HV LV HV LV HV

 ----------------------------------------------
 Demand flows in veh/hour as used by the program

 South: desde calle 10 Norte

 31 T 0 0 31 3 0 0

 32 R 0 0 0 0 2 1

 ----------------------------------------------
 East: desde Acceso Planta

 23 L 2 1 0 0 0 0

 21 R 0 0 0 0 38 2

 ----------------------------------------------
 North: Desde Enlace

 12 L 1 4 0 0 0 0

 13 T 0 0 66 13 0 0

 ----------------------------------------------
 Unit Time for Volumes = 60 minutes

 Peak Flow Period = 15 minutes

 Flow Rates include effects of Flow Scale and Peak Flow Factor

```

**Table S.2 - Movement Capacity Parameters**

```
 Interseccion Calle servicio con Acceso Planta PF 3

 Siuacion Base punta Tarde

 Intersection ID: 1

 Stop Sign Controlled Intersection

 ------------------------------------------------------------------------
 Mov Opposing Movement Total Prac. Prac. Lane Deg.
 ID Demand Adjust. Cap. Deg. Spare Util Satn
 Flow HV Flow HV Flow (veh Satn Cap.
 (veh/h) (%) (veh/h) (%) (pcu/h) /h) xp (%) (%) x

 ------------------------------------------------------------------------
 South: desde calle 10 Norte

 31 T 34 8.8 48 14.6 57 820 0.80 1829 100 0.041

 32 R 3 33.3 5 80.0 14 72 0.80 1820 100 0.042

 ------------------------------------------------------------------------
 East: desde Acceso Planta

 23 L 3 33.3 118 16.9 136 90 0.80 2300 100 0.033

 21 R 40 5.0 34 8.8 36 1202 0.80 2304 100 0.033

 ------------------------------------------------------------------------
 North: Desde Enlace

 12 L 5 80.0 60+ 10.0 65 45 0.80 620 100 0.111*

 13 T 79 16.5 23+ 8.7 25 718 0.80 627 100 0.110

 ------------------------------------------------------------------------
 + Percentage of exiting flow included in total opposing flow

```

**Table S.5 - Movement Performance**

```
 -------------------------------------------------------------------------
 Mov Total Total Aver. Prop. Eff. Longest Queue Perf. Aver.
 ID Delay Delay Delay Queued Stop 95% Back Index Speed
 (veh-h/h)(pers-h/h)(sec) Rate (vehs) (m) (km/h)

```

about:blank 24-11-2013

Output Tables Página 3 de 4

```
 -------------------------------------------------------------------------
 South: desde calle 10 Norte

 31 T 0.00 0.01 0.4 0.16 0.06 0.2 2 0.20 45.6

 32 R 0.00 0.01 4.5 0.16 0.43 0.2 2 0.03 28.3

 -------------------------------------------------------------------------
 East: desde Acceso Planta

 23 L 0.01 0.01 8.1 0.11 0.95 0.2 1 0.04 20.3

 21 R 0.08 0.12 7.3 0.11 0.92 0.2 1 0.47 20.5

 -------------------------------------------------------------------------
 North: Desde Enlace

 12 L 0.01 0.01 5.9 0.14 0.54 0.6 5 0.05 27.5

 13 T 0.01 0.02 0.6 0.14 0.04 0.6 5 0.49 46.1

 -------------------------------------------------------------------------
```

**Table S.7 - Lane Performance**

```
 Interseccion Calle servicio con Acceso Planta PF 3

 Siuacion Base punta Tarde

 Intersection ID: 1

 Stop Sign Controlled Intersection

 -------------------------------------------------------------
 Dem Q u e u e

 Flow Cap Deg. Aver. Eff. 95% Back Lane
 Lane (veh (veh Satn Delay Stop ------------ Length
 No. /h) /h) x (sec) Rate (vehs) (m) (m)

 -------------------------------------------------------------
 South: desde calle 10 Norte

 1 TR 37 893 0.041 0.8 0.09 0.2 1.7 500.0

 -------------------------------------------------------------
 East: desde Acceso Planta

 1 LR 43 1292 0.033 7.3 0.92 0.2 1.3 50.0

 -------------------------------------------------------------
 North: Desde Enlace

 1 LT 84 763 0.110 0.9 0.07 0.6 5.2 500.0

 -------------------------------------------------------------
```

**Table S.10 - Movement Capacity and Performance Summary**

```
 Interseccion Calle servicio con Acceso Planta PF 3

 Siuacion Base punta Tarde
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -----------------------------------------------------------------
 Mov Mov Dem Total Lane Deg. Aver. Eff. 95% Perf.
 ID Typ Flow Cap. Util Satn Delay Stop Back of Index

 (veh (veh Rate Queue
 /h) /h) (%) x (sec) (veh)

 -----------------------------------------------------------------
 South: desde calle 10 Norte

 31 T 34 820 100 0.041 0.4 0.06 0.2 0.20

 32 R 3 72 100 0.042 4.5 0.43 0.2 0.03

 -----------------------------------------------------------------
 East: desde Acceso Planta

 23 L 3 90 100 0.033 8.1 0.95 0.2 0.04

 21 R 40 1202 100 0.033 7.3 0.92 0.2 0.47

 -----------------------------------------------------------------
 North: Desde Enlace

 12 L 5 45 100 0.111* 5.9 0.54 0.6 0.05

 13 T 79 718 100 0.110 0.6 0.04 0.6 0.49

 -----------------------------------------------------------------
 * Maximum degree of saturation

```

about:blank 24-11-2013

Output Tables Página 4 de 4

**Table S.15 - Capacity and Level of Service**

```
 Interseccion Calle servicio con Acceso Planta PF 3

 Siuacion Base punta Tarde

 Intersection ID: 1

 Stop Sign Controlled Intersection

 ----------------------------------------------------------------
 Mov Mov Total Total Deg. Aver. LOS Longest Queue
 ID Typ Flow Cap. of Delay 95% Back

 (veh (veh Satn (vehs) (m)
 /h) /h) (v/c) (sec)

 ----------------------------------------------------------------
 South: desde calle 10 Norte

 31 T 34 820 0.041 0.4 A 0.2 2

 32 R 3 72 0.042 4.5 A 0.2 2

 ----------------------------------------------------------------
 East: desde Acceso Planta

 23 L 3 90 0.033 8.1 A 0.2 1

 21 R 40 1202 0.033 7.3 A 0.2 1

 ----------------------------------------------------------------
 North: Desde Enlace

 12 L 5 45 0.111* 5.9 A 0.6 5

 13 T 79 718 0.110 0.6 A 0.6 5

 ----------------------------------------------------------------
 ALL VEHICLES: 164 0.111 2.6 NA 0.6 5

 ----------------------------------------------------------------
 Level of Service calculations are based on

 average control delay including geometric delay (HCM criteria) and v/c ratio,
 independent of the current delay definition used.
 For the criteria, refer to the "Level of Service" topic in the
 SIDRA Output Guide or the Output section of the on-line help.

 NA Not Applicable - Intersection Level of Service is not calculated at
 two-way stop control or give-way/yield controlled intersections.

 * Maximum v/c ratio, or critical green periods
 " Movement Level of service has been determined using adjacent lane
 v/c ratio rather than short lane v/c ratio (v/c=1.0)

```

Site: situacion Base punta tarde
C:\Users\Usuario\Desktop\EIV planta PF3\eiv planta pf situacion base.aap
Processed nov 24, 2013 03:57:56

A1905, Unregistered, Large Office
**Produced by SIDRA Intersection 3.2.0.1455**
**Copyright 2000-2007 Akcelik and Associates Pty Ltd**
**www.sidrasolutions.com**

about:blank 24-11-2013