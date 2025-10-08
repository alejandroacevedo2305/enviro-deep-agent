---
title: Sin título
author: Desconocido
date: D:20131124155630-04'00'
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

**Siuacion Base punta Medio Dia**

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

 Siuacion Base punta Medio Dia

 Intersection ID: 1

 Stop Sign Controlled Intersection

 ----------------------------------------------------------------
 From To Mov Flow Rate Flow Peak Flow

 Approach Approach ID Turn LV HV Scale Factor

 ----------------------------------------------------------------
 South: desde calle 10 Norte

 East 32 Right 1 2 1.00 0.95

 North 31 Thru 40 5 1.00 0.95

 ----------------------------------------------------------------
 East: desde Acceso Planta

 South 23 Left 2 1 1.00 0.95

 North 21 Right 34 3 1.00 0.95

 ----------------------------------------------------------------
 North: Desde Enlace

 South 13 Thru 67 11 1.00 0.95

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

 Siuacion Base punta Medio Dia

 Intersection ID: 1

 Stop Sign Controlled Intersection

 ----------------------------------------------
 Mov Left Through Right

 ID --------- --------- --------
 LV HV LV HV LV HV

 ----------------------------------------------
 Demand flows in veh/hour as used by the program

 South: desde calle 10 Norte

 31 T 0 0 40 5 0 0

 32 R 0 0 0 0 1 2

 ----------------------------------------------
 East: desde Acceso Planta

 23 L 2 1 0 0 0 0

 21 R 0 0 0 0 34 3

 ----------------------------------------------
 North: Desde Enlace

 12 L 1 4 0 0 0 0

 13 T 0 0 67 11 0 0

 ----------------------------------------------
 Unit Time for Volumes = 60 minutes

 Peak Flow Period = 15 minutes

 Flow Rates include effects of Flow Scale and Peak Flow Factor

```

**Table S.2 - Movement Capacity Parameters**

```
 Interseccion Calle servicio con Acceso Planta PF 3

 Siuacion Base punta Medio Dia

 Intersection ID: 1

 Stop Sign Controlled Intersection

 ------------------------------------------------------------------------
 Mov Opposing Movement Total Prac. Prac. Lane Deg.
 ID Demand Adjust. Cap. Deg. Spare Util Satn
 Flow HV Flow HV Flow (veh Satn Cap.
 (veh/h) (%) (veh/h) (%) (pcu/h) /h) xp (%) (%) x

 ------------------------------------------------------------------------
 South: desde calle 10 Norte

 31 T 45 11.1 45 17.8 56 794 0.80 1312 100 0.057

 32 R 3 66.7 5 80.0 14 53 0.80 1313 100 0.057

 ------------------------------------------------------------------------
 East: desde Acceso Planta

 23 L 3 33.3 128 15.6 146 91 0.80 2327 100 0.033

 21 R 37 8.1 45 11.1 49 1122 0.80 2326 100 0.033

 ------------------------------------------------------------------------
 North: Desde Enlace

 12 L 5 80.0 70+ 13.7 80 46 0.80 636 100 0.109*

 13 T 78 14.1 22+ 11.6 24 725 0.80 644 100 0.108

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

 31 T 0.01 0.01 0.5 0.17 0.06 0.3 2 0.27 45.2

 32 R 0.00 0.01 4.9 0.17 0.43 0.3 2 0.03 28.2

 -------------------------------------------------------------------------
 East: desde Acceso Planta

 23 L 0.01 0.01 8.1 0.14 0.94 0.2 1 0.04 20.3

 21 R 0.08 0.11 7.5 0.14 0.91 0.2 1 0.44 20.5

 -------------------------------------------------------------------------
 North: Desde Enlace

 12 L 0.01 0.01 5.9 0.13 0.55 0.6 5 0.05 27.4

 13 T 0.01 0.02 0.7 0.13 0.04 0.6 5 0.49 46.2

 -------------------------------------------------------------------------
```

**Table S.7 - Lane Performance**

```
 Interseccion Calle servicio con Acceso Planta PF 3

 Siuacion Base punta Medio Dia

 Intersection ID: 1

 Stop Sign Controlled Intersection

 -------------------------------------------------------------
 Dem Q u e u e

 Flow Cap Deg. Aver. Eff. 95% Back Lane
 Lane (veh (veh Satn Delay Stop ------------ Length
 No. /h) /h) x (sec) Rate (vehs) (m) (m)

 -------------------------------------------------------------
 South: desde calle 10 Norte

 1 TR 48 847 0.057 0.8 0.08 0.3 2.4 500.0

 -------------------------------------------------------------
 East: desde Acceso Planta

 1 LR 40 1213 0.033 7.5 0.91 0.2 1.3 50.0

 -------------------------------------------------------------
 North: Desde Enlace

 1 LT 83 771 0.108 1.0 0.07 0.6 5.0 500.0

 -------------------------------------------------------------
```

**Table S.10 - Movement Capacity and Performance Summary**

```
 Interseccion Calle servicio con Acceso Planta PF 3

 Siuacion Base punta Medio Dia
 Intersection ID: 1

 Stop Sign Controlled Intersection

 -----------------------------------------------------------------
 Mov Mov Dem Total Lane Deg. Aver. Eff. 95% Perf.
 ID Typ Flow Cap. Util Satn Delay Stop Back of Index

 (veh (veh Rate Queue
 /h) /h) (%) x (sec) (veh)

 -----------------------------------------------------------------
 South: desde calle 10 Norte

 31 T 45 794 100 0.057 0.5 0.06 0.3 0.27

 32 R 3 53 100 0.057 4.9 0.43 0.3 0.03

 -----------------------------------------------------------------
 East: desde Acceso Planta

 23 L 3 91 100 0.033 8.1 0.94 0.2 0.04

 21 R 37 1122 100 0.033 7.5 0.91 0.2 0.44

 -----------------------------------------------------------------
 North: Desde Enlace

 12 L 5 46 100 0.109* 5.9 0.55 0.6 0.05

 13 T 78 725 100 0.108 0.7 0.04 0.6 0.49

 -----------------------------------------------------------------
 * Maximum degree of saturation

```

about:blank 24-11-2013

Output Tables Página 4 de 4

**Table S.15 - Capacity and Level of Service**

```
 Interseccion Calle servicio con Acceso Planta PF 3

 Siuacion Base punta Medio Dia

 Intersection ID: 1

 Stop Sign Controlled Intersection

 ----------------------------------------------------------------
 Mov Mov Total Total Deg. Aver. LOS Longest Queue
 ID Typ Flow Cap. of Delay 95% Back

 (veh (veh Satn (vehs) (m)
 /h) /h) (v/c) (sec)

 ----------------------------------------------------------------
 South: desde calle 10 Norte

 31 T 45 794 0.057 0.5 A 0.3 2

 32 R 3 53 0.057 4.9 A 0.3 2

 ----------------------------------------------------------------
 East: desde Acceso Planta

 23 L 3 91 0.033 8.1 A 0.2 1

 21 R 37 1122 0.033 7.5 A 0.2 1

 ----------------------------------------------------------------
 North: Desde Enlace

 12 L 5 46 0.109* 5.9 A 0.6 5

 13 T 78 725 0.108 0.7 A 0.6 5

 ----------------------------------------------------------------
 ALL VEHICLES: 171 0.109 2.4 NA 0.6 5

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

Site: situacion Base punta medio dia
C:\Users\Usuario\Desktop\EIV planta PF3\eiv planta pf situacion base.aap
Processed nov 24, 2013 03:54:14

A1905, Unregistered, Large Office
**Produced by SIDRA Intersection 3.2.0.1455**
**Copyright 2000-2007 Akcelik and Associates Pty Ltd**
**www.sidrasolutions.com**

about:blank 24-11-2013