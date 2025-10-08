---
title: Sin título
author: Desconocido
date: D:20131124155142-04'00'
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

**Siuacion Base punta Mañana**

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

 Siuacion Base punta Ma ana

 Intersection ID: 1

 Stop Sign Controlled Intersection

 ----------------------------------------------------------------
 From To Mov Flow Rate Flow Peak Flow

 Approach Approach ID Turn LV HV Scale Factor

 ----------------------------------------------------------------
 South: desde calle 10 Norte

 East 32 Right 1 1 1.00 0.95

 North 31 Thru 55 6 1.00 0.95

 ----------------------------------------------------------------
 East: desde Acceso Planta

 South 23 Left 1 1 1.00 0.95

 North 21 Right 1 2 1.00 0.95

 ----------------------------------------------------------------
 North: Desde Enlace

 South 13 Thru 104 54 1.00 0.95

 East 12 Left 29 1 1.00 0.95

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

 Siuacion Base punta Ma ana

 Intersection ID: 1

 Stop Sign Controlled Intersection

 ----------------------------------------------
 Mov Left Through Right

 ID --------- --------- --------
 LV HV LV HV LV HV

 ----------------------------------------------
 Demand flows in veh/hour as used by the program

 South: desde calle 10 Norte

 31 T 0 0 55 6 0 0

 32 R 0 0 0 0 1 1

 ----------------------------------------------
 East: desde Acceso Planta

 23 L 1 1 0 0 0 0

 21 R 0 0 0 0 1 2

 ----------------------------------------------
 North: Desde Enlace

 12 L 29 1 0 0 0 0

 13 T 0 0 104 54 0 0

 ----------------------------------------------
 Unit Time for Volumes = 60 minutes

 Peak Flow Period = 15 minutes

 Flow Rates include effects of Flow Scale and Peak Flow Factor

```

**Table S.2 - Movement Capacity Parameters**

```
 Interseccion Calle servicio con Acceso Planta PF 3

 Siuacion Base punta Ma ana

 Intersection ID: 1

 Stop Sign Controlled Intersection

 ------------------------------------------------------------------------
 Mov Opposing Movement Total Prac. Prac. Lane Deg.
 ID Demand Adjust. Cap. Deg. Spare Util Satn
 Flow HV Flow HV Flow (veh Satn Cap.
 (veh/h) (%) (veh/h) (%) (pcu/h) /h) xp (%) (%) x

 ------------------------------------------------------------------------
 South: desde calle 10 Norte

 31 T 61 9.8 35 11.4 40 872 0.80 1044 100 0.070

 32 R 2 50.0 30 3.3 30 29 0.80 1060 100 0.069

 ------------------------------------------------------------------------
 East: desde Acceso Planta

 23 L 2 50.0 249 24.5 312 187 0.80 7380 100 0.011

 21 R 3 66.7 61 9.8 65 280 0.80 7367 100 0.011

 ------------------------------------------------------------------------
 North: Desde Enlace

 12 L 30 3.3 67+ 13.5 77 120 0.80 220 100 0.250*

 13 T 158 34.2 4+ 57.1 4 631 0.80 219 100 0.250*

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

 31 T 0.01 0.01 0.4 0.16 0.05 0.4 3 0.35 45.5

 32 R 0.00 0.00 4.6 0.16 0.45 0.4 3 0.02 28.3

 -------------------------------------------------------------------------
 East: desde Acceso Planta

 23 L 0.01 0.01 11.6 0.28 0.92 0.1 1 0.03 17.7

 21 R 0.01 0.02 12.1 0.28 0.84 0.1 1 0.04 17.9

 -------------------------------------------------------------------------
 North: Desde Enlace

 12 L 0.04 0.06 4.5 0.04 0.54 1.7 15 0.31 28.2

 13 T 0.01 0.01 0.2 0.04 0.01 1.7 15 1.00 48.9

 -------------------------------------------------------------------------
```

**Table S.7 - Lane Performance**

```
 Interseccion Calle servicio con Acceso Planta PF 3

 Siuacion Base punta Ma ana

 Intersection ID: 1

 Stop Sign Controlled Intersection

 -------------------------------------------------------------
 Dem Q u e u e

 Flow Cap Deg. Aver. Eff. 95% Back Lane
 Lane (veh (veh Satn Delay Stop ------------ Length
 No. /h) /h) x (sec) Rate (vehs) (m) (m)

 -------------------------------------------------------------
 South: desde calle 10 Norte

 1 TR 63 900 0.070 0.5 0.06 0.4 2.9 500.0

 -------------------------------------------------------------
 East: desde Acceso Planta

 1 LR 5 466 0.011 11.9 0.87 0.1 0.6 50.0

 -------------------------------------------------------------
 North: Desde Enlace

 1 LT 188 751 0.250 0.9 0.09 1.7 14.5 500.0

 -------------------------------------------------------------
```

**Table S.10 - Movement Capacity and Performance Summary**

```
 Interseccion Calle servicio con Acceso Planta PF 3

 Siuacion Base punta Ma ana
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -----------------------------------------------------------------
 Mov Mov Dem Total Lane Deg. Aver. Eff. 95% Perf.
 ID Typ Flow Cap. Util Satn Delay Stop Back of Index

 (veh (veh Rate Queue
 /h) /h) (%) x (sec) (veh)

 -----------------------------------------------------------------
 South: desde calle 10 Norte

 31 T 61 872 100 0.070 0.4 0.05 0.4 0.35

 32 R 2 29 100 0.069 4.6 0.45 0.4 0.02

 -----------------------------------------------------------------
 East: desde Acceso Planta

 23 L 2 187 100 0.011 11.6 0.92 0.1 0.03

 21 R 3 280 100 0.011 12.1 0.84 0.1 0.04

 -----------------------------------------------------------------
 North: Desde Enlace

 12 L 30 120 100 0.250* 4.5 0.54 1.7 0.31

 13 T 158 631 100 0.250* 0.2 0.01 1.7 1.00

 -----------------------------------------------------------------
 * Maximum degree of saturation

```

about:blank 24-11-2013

Output Tables Página 4 de 4

**Table S.15 - Capacity and Level of Service**

```
 Interseccion Calle servicio con Acceso Planta PF 3

 Siuacion Base punta Ma ana

 Intersection ID: 1

 Stop Sign Controlled Intersection

 ----------------------------------------------------------------
 Mov Mov Total Total Deg. Aver. LOS Longest Queue
 ID Typ Flow Cap. of Delay 95% Back

 (veh (veh Satn (vehs) (m)
 /h) /h) (v/c) (sec)

 ----------------------------------------------------------------
 South: desde calle 10 Norte

 31 T 61 872 0.070 0.4 A 0.4 3

 32 R 2 29 0.069 4.6 A 0.4 3

 ----------------------------------------------------------------
 East: desde Acceso Planta

 23 L 2 187 0.011 11.6 B 0.1 1

 21 R 3 280 0.011 12.1 B 0.1 1

 ----------------------------------------------------------------
 North: Desde Enlace

 12 L 30 120 0.250* 4.5 A 1.7 15

 13 T 158 631 0.250* 0.2 A 1.7 15

 ----------------------------------------------------------------
 ALL VEHICLES: 256 0.250 1.0 NA 1.7 15

 ----------------------------------------------------------------
 Level of Service calculations are based on

 average control delay including geometric delay (HCM criteria) and v/c ratio,
 independent of the current delay definition used.
 For the criteria, refer to the "Level of Service" topic in the
 SIDRA Output Guide or the Output section of the on-line help.

 NA Not Applicable - Intersection Level of Service is not calculated at
 two-way stop control or give-way/yield controlled intersections.

 * Maximum v/c ratio, or critical green periods

```

Site: situacion base punta mañana
C:\Users\Usuario\Desktop\EIV planta PF3\eiv planta pf situacion base.aap
Processed nov 24, 2013 03:48:11

A1905, Unregistered, Large Office
**Produced by SIDRA Intersection 3.2.0.1455**
**Copyright 2000-2007 Akcelik and Associates Pty Ltd**
**www.sidrasolutions.com**

about:blank 24-11-2013