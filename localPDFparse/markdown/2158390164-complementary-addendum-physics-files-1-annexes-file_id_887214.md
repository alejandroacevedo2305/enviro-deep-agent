---
title: Prediction file DBO
author: Desconocido
date: D:20240412162103Z00'00'
language: en
type: general
pages: 8
has_toc: False
has_tables: False
extraction_quality: high
---

```
CORMIX2 PREDICTION FILE:

2222222222222222222222222222222222222222222222222222222222222222222222

2222222222222222222222222

CORMIX MIXING ZONE EXPERT SYSTEM
Subsystem CORMIX2: Multiport Diffuser Discharges
CORMIX Version 12.0GT
HYDRO2 Version 12.0.1.0 August 2021

---------------------------------------------------------------------
-----------------------
---------------------------------------------------------------------
-----------------------
CASE DESCRIPTION
Site name/label: Rauco
Design case: PD Rauco
FILE NAME: C:\...enante\01Simulaciones\Cuadratura-llenante
DBO.prd
Time stamp: 04/10/2024--11:54:46

ENVIRONMENT PARAMETERS (metric units)
Unbounded section

HA = 40.00 HD = 35.50

UA = 0.045 F = 0.015 USTAR =0.1957E-02

UW = 0.000 UWSTAR=0.0000E+00
Density stratified environment
STRCND= A RHOAM = 1025.3650

RHOAS = 1025.1801 RHOAB = 1025.5500 RHOAH0= 1025.5490 E

=0.9966E-04

DIFFUSER DISCHARGE PARAMETERS (metric units)
Diffuser type: DITYPE= alternating_parallel
BANK = LEFT DISTB = 35.50 YB1 = 22.95 YB2 =

48.05

LD = 35.50 NOPEN = 11 NRISER= 11 SPAC =

3.55 NPPERR = 1

D0 = 0.120 A0 = 0.011 H0 = 0.10 SUB0 =

35.40

D0INP = 0.120 CR0 = 1.000 B0 =0.3186E-02
Nozzle/port arrangement: alternating_without_fanning
GAMMA = 45.00 THETA = 90.00 SIGMA = 0.00 BETA =

90.00
U0 = 0.490 Q0 = 0.061 Q0A =0.6100E-01
RHO0 = 1008.0000 DRHO0 =0.1755E+02 GP0 =0.1678E+00
C0 =0.1167E+04 CUNITS= mg/l
IPOLL = 1 KS =0.0000E+00 KD =0.0000E+00

FLUX VARIABLES - PER UNIT DIFFUSER LENGTH (metric units)
q0 =0.1718E-02 SIGNJ0= 1.0
m0 =U0^2*B0 =0.7659E-03 j0 =U0*GP0*B0 =0.2621E-03 (based on slot
width B0)
m0 =U0*q0 =0.8425E-03 j0 =q0*GP0 =0.2883E-03 (based on

```

```
volume flux q0)
Associated 2-d length scales (meters)
lQ=B = 0.004 lM = 0.19 lm = 0.41
lmp = 2.04 lbp = 6.62 la = 4.53

FLUX VARIABLES - ENTIRE DIFFUSER (metric units)
Q0 =0.6100E-01 M0 =0.2719E-01 J0 =0.9306E-02
Associated 3-d length scales (meters)
LQ = 0.11 LM = 0.69 Lm = 3.83 Lb =
110.85
Lmp = 4.16 Lbp =
10.07

NON-DIMENSIONAL PARAMETERS

FR0 = 21.21 FRD0 = 3.46 R = 10.85 PL =

136.04
(slot) (port/nozzle)

RECOMPUTED SOURCE CONDITIONS FOR ALTERNATING JETS OR RISER GROUPS:

Momentum fluxes: m0 =0.7659E-03 M0 =0.2719E-01
lQ=B = 0.004 lM = 0.19 lm = 0.41 lmp =
2.04
LQ = 0.353 LM = 0.69 Lm = 3.83 Lmp =
4.16
Properties of riser group with 1 ports/nozzles each:
U0 = 0.490 D0 = 0.120 A0 = 0.011 THETA =

90.00

FR0 = 21.21 FRD0 = 3.46 R = 10.85
(slot) (riser group)

FLOW CLASSIFICATION

222222222222222222222222222222222222222222222222
2 Flow class (CORMIX2) = MS6 2
2 Applicable layer depth HS = 35.50 2
222222222222222222222222222222222222222222222222

MIXING ZONE / TOXIC DILUTION / REGION OF INTEREST PARAMETERS
C0 =0.1167E+04 CUNITS= mg/l
NTOX = 0

NSTD = 0

REGMZ = 0

XINT = 5000.00 XMAX = 5000.00

X-Y-Z COORDINATE SYSTEM:
ORIGIN is located at the bottom and the diffuser mid-point:
35.50 m from the LEFT bank/shore.
X-axis points downstream, Y-axis points to left, Z-axis points
upward.
NSTEP = 20 display intervals per module

---------------------------------------------------------------------
```

```
-----------------------
---------------------------------------------------------------------
-----------------------
BEGIN MOD101: DISCHARGE MODULE (SINGLE PORT AT DIFFUSER CENTER)

X Y Z S C BV BH Uc

TT

0.00 0.00 0.10 1.0 0.117E+04 0.06 0.06

0.490 .00000E+00

END OF MOD101: DISCHARGE MODULE (SINGLE PORT AT DIFFUSER CENTER)

---------------------------------------------------------------------
-----------------------
---------------------------------------------------------------------
-----------------------
BEGIN CORJET (MOD110): JET/PLUME NEAR-FIELD MIXING REGION

Plume-like motion in linear stratification with strong crossflow.

Zone of flow establishment: THETAE= 87.81 SIGMAE=

0.00

LE = 0.42 XE = 0.01 YE = 0.00 ZE =

0.52

Profile definitions:
BV = Gaussian 1/e (37%) width, in vertical plane normal to
trajectory
BH = before merging: Gaussian 1/e (37%) half-width in horizontal
plane
normal to trajectory
after merging: top-hat half-width in horizontal plane
parallel to diffuser line
S = hydrodynamic centerline dilution
C = centerline concentration (includes reaction effects, if any)
Uc = Local centerline excess velocity (above ambient)
TT = Cumulative travel time

X Y Z S C BV BH Uc

TT
Individual jet/plumes before merging:
0.01 0.00 0.52 1.0 0.117E+04 0.06 0.06

0.490 .00000E+00

0.01 0.00 0.52 1.0 0.117E+04 0.06 0.06

0.490 .27169E-02

6.47 0.00 2.20 30.9 0.377E+02 0.65 0.65

0.108 .32777E+02

13.24 0.00 2.73 67.2 0.174E+02 1.05 1.05

0.072 .84583E+02
Merging of individual jet/plumes to form plane jet/plume:
17.26 0.00 2.99 112.9 0.103E+02 1.12 18.87

```

```
0.044 .12082E+03

26.78 0.00 3.41 160.8 0.726E+01 1.67 19.42

0.038 .23249E+03

33.56 0.00 3.71 193.2 0.604E+01 2.05 19.80

0.036 .31533E+03

40.33 0.00 4.02 224.7 0.519E+01 2.42 20.17

0.034 .39993E+03

47.11 0.00 4.32 255.5 0.457E+01 2.78 20.53

0.033 .48589E+03

53.88 0.00 4.62 285.6 0.409E+01 3.14 20.89

0.032 .57301E+03

60.66 0.00 4.91 315.0 0.370E+01 3.50 21.25

0.031 .66126E+03

67.43 0.00 5.20 343.6 0.340E+01 3.85 21.60

0.030 .75047E+03

74.19 0.00 5.47 371.3 0.314E+01 4.20 21.95

0.029 .84074E+03

80.95 0.00 5.73 398.1 0.293E+01 4.54 22.29

0.028 .93211E+03

87.72 0.00 5.98 423.9 0.275E+01 4.88 22.63

0.027 .10247E+04

94.48 0.00 6.21 448.5 0.260E+01 5.22 22.97

0.027 .11184E+04

101.25 0.00 6.41 471.9 0.247E+01 5.54 23.29

0.026 .12133E+04

108.01 0.00 6.60 494.0 0.236E+01 5.86 23.61

0.025 .13095E+04

114.78 0.00 6.76 514.7 0.227E+01 6.16 23.91

0.024 .14069E+04

121.55 0.00 6.88 533.9 0.219E+01 6.44 24.19

0.023 .15053E+04

128.32 0.00 6.98 551.5 0.212E+01 6.71 24.46

0.022 .16049E+04

135.08 0.00 7.04 567.5 0.206E+01 6.95 24.70

0.022 .17055E+04

Terminal level in stratified ambient has been reached.
Cumulative travel time = 1705.4668 sec ( 0.47 hrs)

END OF CORJET (MOD110): JET/PLUME NEAR-FIELD MIXING REGION

---------------------------------------------------------------------
-----------------------
---------------------------------------------------------------------
-----------------------
BEGIN MOD244: INTERNAL DENSITY CURRENT DEVELOPING ALONG PARALLEL

DIFFUSER

The plume for this parallel diffuser interacts with the
terminal layer, and a density current forms.
Note: The starting x-coordinate of the developing plume will be
shifted upstream.

```

```
The diffuser near-field dilution is REDUCED because of the PROXIMITY

of the shoreline.

Profile definitions:
BV = top-hat thickness, measured vertically
BH = top-hat half-width, measured horizontally in y-direction
ZU = upper plume boundary (Z-coordinate)
ZL = lower plume boundary (Z-coordinate)
S = hydrodynamic average (bulk) dilution
C = average (bulk) concentration (includes reaction effects, if
any)
TT = Cumulative travel time

X Y Z S C BV BH TT

122.53 0.00 7.04 770.5 0.151E+01 6.95 24.70

.17055E+04

123.79 0.00 7.04 770.5 0.151E+01 7.24 26.25

.17332E+04

125.04 0.00 7.04 770.5 0.151E+01 7.48 27.86

.17610E+04

126.30 0.00 7.04 770.5 0.151E+01 7.68 29.53

.17888E+04

127.55 0.00 7.04 770.5 0.151E+01 7.85 31.23

.18165E+04

128.81 0.00 7.04 770.5 0.151E+01 7.99 32.96

.18443E+04

130.06 0.00 7.04 770.5 0.151E+01 8.12 34.73

.18721E+04

131.32 0.00 7.04 770.5 0.151E+01 8.22 36.52

.18998E+04

132.57 0.00 7.04 770.5 0.151E+01 8.31 38.33

.19276E+04

133.83 0.00 7.04 770.5 0.151E+01 8.39 40.16

.19554E+04

135.08 0.00 7.04 770.5 0.151E+01 8.46 42.01

.19831E+04

136.34 0.00 7.04 770.5 0.151E+01 8.52 43.87

.20109E+04

137.59 0.00 7.04 770.5 0.151E+01 8.57 45.74

.20387E+04

138.85 0.00 7.04 770.5 0.151E+01 8.62 47.63

.20665E+04

140.10 0.00 7.04 770.5 0.151E+01 8.66 49.52

.20942E+04

141.36 0.00 7.04 770.5 0.151E+01 8.70 51.42

.21220E+04

142.61 0.00 7.04 770.5 0.151E+01 8.73 53.33

.21498E+04

143.87 0.00 7.04 770.5 0.151E+01 8.76 55.25

.21775E+04

```

```
145.12 0.00 7.04 770.5 0.151E+01 8.79 57.17

.22053E+04

146.38 0.00 7.04 770.5 0.151E+01 8.81 59.10

.22331E+04

147.63 0.00 7.04 770.5 0.151E+01 8.83 61.03

.22608E+04
Cumulative travel time = 2260.8271 sec ( 0.63 hrs)

END OF MOD244: INTERNAL DENSITY CURRENT DEVELOPING ALONG PARALLEL

DIFFUSER

---------------------------------------------------------------------
-----------------------
** End of NEAR-FIELD REGION (NFR) **

In this design case, the diffuser is located CLOSE TO BANK/SHORE.
Some lateral boundary interaction occurs at end of the near-field.
This may be related to a design case with a VERY LOW AMBIENT
VELOCITY.
The dilution values in one or more of the preceding zones may be
too high.
Carefully evaluate results in near-field and check degree of
interaction.

Consider locating outfall further away from bank or shore.
In the next prediction module, the plume centerline will be set
to follow the bank/shore.

---------------------------------------------------------------------
-----------------------
BEGIN MOD242: BUOYANT TERMINAL LAYER SPREADING

Plume is ATTACHED to LEFT bank/shore.
Plume width is now determined from LEFT bank/shore.

Profile definitions:
BV = top-hat thickness, measured vertically
BH = top-hat half-width, measured horizontally in y-direction
ZU = upper plume boundary (Z-coordinate)
ZL = lower plume boundary (Z-coordinate)
S = hydrodynamic average (bulk) dilution
C = average (bulk) concentration (includes reaction effects, if
any)
TT = Cumulative travel time

Plume Stage 2 (bank attached):
X Y Z S C BV BH ZU

ZL TT

147.63 35.50 7.04 770.5 0.151E+01 11.17 96.53 12.63

1.46 .22608E+04

390.25 35.50 7.04 1055.1 0.111E+01 4.41 335.14 9.25

4.84 .76285E+04

```

```
632.87 35.50 7.04 1156.1 0.101E+01 3.40 475.95 8.74

5.34 .12996E+05

875.49 35.50 7.04 1223.9 0.954E+00 2.92 586.58 8.50

5.58 .18364E+05

1118.11 35.50 7.04 1277.5 0.913E+00 2.63 680.47 8.36

5.73 .23731E+05

1360.73 35.50 7.04 1324.0 0.881E+00 2.43 763.34 8.26

5.83 .29099E+05

1603.34 35.50 7.04 1366.5 0.854E+00 2.28 838.33 8.18

5.90 .34467E+05

1845.96 35.50 7.04 1406.9 0.829E+00 2.17 907.37 8.13

5.96 .39834E+05

2088.58 35.50 7.04 1446.3 0.807E+00 2.08 971.76 8.08

6.00 .45202E+05

2331.20 35.50 7.04 1485.4 0.786E+00 2.01 1032.44 8.05

6.04 .50570E+05

2573.82 35.50 7.04 1524.7 0.765E+00 1.96 1090.08 8.02

6.06 .55937E+05

2816.44 35.50 7.04 1564.5 0.746E+00 1.91 1145.21 8.00

6.09 .61305E+05

3059.05 35.50 7.04 1605.0 0.727E+00 1.87 1198.24 7.98

6.11 .66673E+05

3301.67 35.50 7.04 1646.4 0.709E+00 1.84 1249.51 7.96

6.12 .72040E+05

3544.29 35.50 7.04 1688.7 0.691E+00 1.82 1299.28 7.95

6.13 .77408E+05

3786.91 35.50 7.04 1732.0 0.674E+00 1.80 1347.76 7.94

6.14 .82776E+05

4029.53 35.50 7.04 1776.3 0.657E+00 1.78 1395.14 7.93

6.15 .88143E+05

4272.15 35.50 7.04 1821.6 0.641E+00 1.77 1441.56 7.93

6.16 .93511E+05

4514.76 35.50 7.04 1867.9 0.625E+00 1.76 1487.17 7.92

6.16 .98879E+05

4757.38 35.50 7.04 1915.3 0.609E+00 1.75 1532.05 7.92

6.17 .10425E+06

5000.00 35.50 7.04 1963.6 0.594E+00 1.74 1576.32 7.91

6.17 .10961E+06
Cumulative travel time = 109614.0703 sec ( 30.45 hrs)

Simulation limit based on maximum specified distance = 5000.00 m.
This is the REGION OF INTEREST limitation.

END OF MOD242: BUOYANT TERMINAL LAYER SPREADING

---------------------------------------------------------------------
-----------------------
---------------------------------------------------------------------
-----------------------
CORMIX2: Multiport Diffuser Discharges End of Prediction File
2222222222222222222222222222222222222222222222222222222222222222222222

```

```
2222222222222222222222222

```