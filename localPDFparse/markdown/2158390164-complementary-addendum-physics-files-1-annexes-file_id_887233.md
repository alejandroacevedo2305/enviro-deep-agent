---
title: Prediction file ColFec
author: Desconocido
date: D:20240412163425Z00'00'
language: en
type: general
pages: 7
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
FILE NAME: C:\...nte\01Simulaciones\Cuadratura-llenante
ColFec.prd
Time stamp: 04/10/2024--13:36:07

ENVIRONMENT PARAMETERS (metric units)
Unbounded section

HA = 40.00 HD = 35.50

UA = 0.037 F = 0.015 USTAR =0.1611E-02

UW = 0.000 UWSTAR=0.0000E+00
Density stratified environment
STRCND= A RHOAM = 1025.7300

RHOAS = 1025.2700 RHOAB = 1026.1899 RHOAH0= 1026.1874 E

=0.2477E-03

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
RHO0 = 1008.0000 DRHO0 =0.1819E+02 GP0 =0.1738E+00

C0 =0.3000E+05 CUNITS= bacteria-counts

IPOLL = 1 KS =0.0000E+00 KD =0.0000E+00

FLUX VARIABLES - PER UNIT DIFFUSER LENGTH (metric units)
q0 =0.1718E-02 SIGNJ0= 1.0
m0 =U0^2*B0 =0.7659E-03 j0 =U0*GP0*B0 =0.2715E-03 (based on slot
width B0)
m0 =U0*q0 =0.8425E-03 j0 =q0*GP0 =0.2987E-03 (based on

```

```
volume flux q0)
Associated 2-d length scales (meters)
lQ=B = 0.004 lM = 0.18 lm = 0.61
lmp = 1.50 lbp = 4.25 la = 2.36

FLUX VARIABLES - ENTIRE DIFFUSER (metric units)
Q0 =0.6100E-01 M0 =0.2719E-01 J0 =0.9638E-02
Associated 3-d length scales (meters)
LQ = 0.11 LM = 0.68 Lm = 4.65 Lb =
205.95
Lmp = 3.32 Lbp =
7.22

NON-DIMENSIONAL PARAMETERS

FR0 = 20.84 FRD0 = 3.40 R = 13.18 PL =

137.64
(slot) (port/nozzle)

RECOMPUTED SOURCE CONDITIONS FOR ALTERNATING JETS OR RISER GROUPS:

Momentum fluxes: m0 =0.7659E-03 M0 =0.2719E-01
lQ=B = 0.004 lM = 0.18 lm = 0.61 lmp =
1.50
LQ = 0.353 LM = 0.68 Lm = 4.65 Lmp =
3.32
Properties of riser group with 1 ports/nozzles each:
U0 = 0.490 D0 = 0.120 A0 = 0.011 THETA =

90.00

FR0 = 20.84 FRD0 = 3.40 R = 13.18
(slot) (riser group)

FLOW CLASSIFICATION

222222222222222222222222222222222222222222222222
2 Flow class (CORMIX2) = MS7 2
2 Applicable layer depth HS = 35.50 2
222222222222222222222222222222222222222222222222

MIXING ZONE / TOXIC DILUTION / REGION OF INTEREST PARAMETERS
C0 =0.3000E+05 CUNITS= bacteria-counts

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

0.00 0.00 0.10 1.0 0.300E+05 0.06 0.06

0.490 .00000E+00

END OF MOD101: DISCHARGE MODULE (SINGLE PORT AT DIFFUSER CENTER)

---------------------------------------------------------------------
-----------------------
---------------------------------------------------------------------
-----------------------
BEGIN CORJET (MOD110): JET/PLUME NEAR-FIELD MIXING REGION

Plume-like motion in linear stratification with weak crossflow.

Zone of flow establishment: THETAE= 88.20 SIGMAE=

0.00

LE = 0.45 XE = 0.01 YE = 0.00 ZE =

0.55

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
0.01 0.00 0.55 1.0 0.300E+05 0.06 0.06

0.490 .00000E+00

0.01 0.00 0.55 1.0 0.300E+05 0.06 0.06

0.490 .26508E-02

3.32 0.00 2.02 17.0 0.177E+04 0.45 0.45

0.160 .14081E+02

6.97 0.00 2.61 36.9 0.814E+03 0.74 0.74

0.112 .36105E+02

10.67 0.00 2.96 57.9 0.518E+03 0.99 0.99

0.088 .63444E+02

```

```
14.36 0.00 3.25 80.6 0.372E+03 1.21 1.21

0.074 .94989E+02
Merging of individual jet/plumes to form plane jet/plume:
15.20 0.00 3.31 108.0 0.278E+03 1.12 18.87

0.051 .10261E+03

21.77 0.00 3.65 143.7 0.209E+03 1.58 19.33

0.044 .18066E+03

25.47 0.00 3.85 162.7 0.184E+03 1.83 19.58

0.042 .22673E+03

29.17 0.00 4.04 181.1 0.166E+03 2.07 19.82

0.041 .27395E+03

32.88 0.00 4.23 198.9 0.151E+03 2.31 20.06

0.039 .32215E+03

36.58 0.00 4.41 216.2 0.139E+03 2.55 20.30

0.038 .37126E+03

40.28 0.00 4.58 232.9 0.129E+03 2.78 20.53

0.036 .42124E+03

43.98 0.00 4.74 249.0 0.120E+03 3.02 20.77

0.035 .47212E+03

47.68 0.00 4.90 264.4 0.113E+03 3.25 21.00

0.034 .52389E+03

51.38 0.00 5.04 279.2 0.107E+03 3.47 21.22

0.033 .57651E+03

55.08 0.00 5.17 293.3 0.102E+03 3.70 21.45

0.031 .63005E+03

58.79 0.00 5.29 306.7 0.978E+02 3.91 21.66

0.030 .68446E+03

62.49 0.00 5.38 319.3 0.940E+02 4.12 21.87

0.029 .73970E+03

66.20 0.00 5.46 331.0 0.906E+02 4.32 22.07

0.028 .79581E+03

69.90 0.00 5.52 342.0 0.877E+02 4.51 22.26

0.028 .85270E+03

73.60 0.00 5.56 352.0 0.852E+02 4.68 22.43

0.027 .91028E+03

Terminal level in stratified ambient has been reached.
Cumulative travel time = 910.2791 sec ( 0.25 hrs)

END OF CORJET (MOD110): JET/PLUME NEAR-FIELD MIXING REGION

---------------------------------------------------------------------
-----------------------
---------------------------------------------------------------------
-----------------------
BEGIN MOD236: TERMINAL LAYER IMPINGEMENT/UPSTREAM SPREADING

Vertical angle of layer/boundary impingement = 0.43 deg
Horizontal angle of layer/boundary impingement = 0.00 deg

UPSTREAM INTRUSION PROPERTIES:
Maximum elevation of jet/plume rise = 8.50 m

```

```
Layer thickness in impingement region = 5.67 m
Upstream intrusion length = 62.92 m
X-position of upstream stagnation point = 10.69 m
Thickness in intrusion region = 5.67 m
Half-width at downstream end = 123.70 m

Thickness at downstream end = 3.31 m

Control volume inflow:

X Y Z S C BV BH TT

73.60 0.00 5.56 352.0 0.852E+02 4.68 22.43

.91028E+03

Profile definitions:
BV = top-hat thickness, measured vertically
BH = top-hat half-width, measured horizontally in y-direction
ZU = upper plume boundary (Z-coordinate)
ZL = lower plume boundary (Z-coordinate)
S = hydrodynamic average (bulk) dilution
C = average (bulk) concentration (includes reaction effects, if
any)
TT = Cumulative travel time

X Y Z S C BV BH ZU

ZL TT

10.69 0.00 5.56 9999.9 0.000E+00 0.00 0.00 5.56

5.56 .26016E+04

13.18 0.00 5.56 1410.6 0.213E+02 1.42 20.17 6.27

4.86 .25345E+04

25.41 0.00 5.56 587.2 0.511E+02 3.40 49.00 7.26

3.86 .22058E+04

37.64 0.00 5.56 445.9 0.673E+02 4.48 66.30 7.80

3.32 .18771E+04

49.86 0.00 5.56 386.5 0.776E+02 5.17 79.94 8.15

2.98 .15484E+04

62.09 0.00 5.56 359.4 0.835E+02 5.56 91.57 8.34

2.79 .12197E+04

74.32 0.00 5.56 352.1 0.852E+02 5.67 117.30 8.40

2.73 .92950E+03

86.55 0.00 5.56 375.6 0.799E+02 5.29 118.77 8.21

2.92 .12582E+04

98.77 0.00 5.56 423.2 0.709E+02 4.53 120.12 7.83

3.30 .15869E+04

111.00 0.00 5.56 464.9 0.645E+02 3.86 121.39 7.49

3.64 .19156E+04

123.23 0.00 5.56 487.8 0.615E+02 3.49 122.58 7.31

3.82 .22442E+04

135.45 0.00 5.56 499.0 0.601E+02 3.31 123.70 7.22

3.91 .25729E+04
Cumulative travel time = 2572.9333 sec ( 0.71 hrs)

```

```
END OF MOD236: TERMINAL LAYER IMPINGEMENT/UPSTREAM SPREADING

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

135.45 35.50 5.56 499.0 0.601E+02 5.14 159.20 8.13

2.99 .25729E+04

378.68 35.50 5.56 631.9 0.475E+02 2.58 401.29 6.85

4.27 .91113E+04

621.91 35.50 5.56 687.6 0.436E+02 2.04 551.42 6.59

4.54 .15650E+05

865.14 35.50 5.56 725.8 0.413E+02 1.78 668.98 6.45

4.67 .22188E+05

1108.36 35.50 5.56 756.4 0.397E+02 1.61 768.21 6.37

4.76 .28726E+05

1351.59 35.50 5.56 783.3 0.383E+02 1.50 855.42 6.31

4.81 .35265E+05

1594.82 35.50 5.56 808.1 0.371E+02 1.42 934.05 6.27

```

```
4.85 .41803E+05

1838.05 35.50 5.56 832.0 0.361E+02 1.36 1006.26 6.24

4.89 .48342E+05

2081.27 35.50 5.56 855.3 0.351E+02 1.31 1073.48 6.22

4.91 .54880E+05

2324.50 35.50 5.56 878.7 0.341E+02 1.27 1136.74 6.20

4.93 .61418E+05

2567.73 35.50 5.56 902.2 0.333E+02 1.24 1196.79 6.18

4.95 .67957E+05

2810.95 35.50 5.56 926.1 0.324E+02 1.21 1254.19 6.17

4.96 .74495E+05

3054.18 35.50 5.56 950.4 0.316E+02 1.19 1309.40 6.16

4.97 .81033E+05

3297.41 35.50 5.56 975.3 0.308E+02 1.17 1362.75 6.15

4.98 .87572E+05

3540.64 35.50 5.56 1000.7 0.300E+02 1.16 1414.54 6.14

4.98 .94110E+05

3783.86 35.50 5.56 1026.7 0.292E+02 1.15 1465.00 6.14

4.99 .10065E+06

4027.09 35.50 5.56 1053.3 0.285E+02 1.14 1514.32 6.13

4.99 .10719E+06

4270.32 35.50 5.56 1080.4 0.278E+02 1.13 1562.65 6.13

5.00 .11373E+06

4513.55 35.50 5.56 1108.2 0.271E+02 1.13 1610.13 6.13

5.00 .12026E+06

4756.77 35.50 5.56 1136.5 0.264E+02 1.12 1656.87 6.13

5.00 .12680E+06

5000.00 35.50 5.56 1165.3 0.257E+02 1.12 1702.97 6.12

5.00 .13334E+06
Cumulative travel time = 133340.2969 sec ( 37.04 hrs)

Simulation limit based on maximum specified distance = 5000.00 m.
This is the REGION OF INTEREST limitation.

END OF MOD242: BUOYANT TERMINAL LAYER SPREADING

---------------------------------------------------------------------
-----------------------
---------------------------------------------------------------------
-----------------------
CORMIX2: Multiport Diffuser Discharges End of Prediction File
2222222222222222222222222222222222222222222222222222222222222222222222

2222222222222222222222222

```