---
title: Prediction file AyG
author: Desconocido
date: D:20240412163110Z00'00'
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
FILE NAME: C:\...-vaciante\01Simulaciones\Sicigia-vaciante
AyG.prd
Time stamp: 04/10/2024--12:33:26

ENVIRONMENT PARAMETERS (metric units)
Unbounded section

HA = 40.00 HD = 35.50

UA = 0.099 F = 0.015 USTAR =0.4287E-02

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
C0 =0.1490E+03 CUNITS= mg/l
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
lQ=B = 0.004 lM = 0.18 lm = 0.09
lmp = 1.50 lbp = 4.25 la = 6.29

FLUX VARIABLES - ENTIRE DIFFUSER (metric units)
Q0 =0.6100E-01 M0 =0.2719E-01 J0 =0.9638E-02
Associated 3-d length scales (meters)
LQ = 0.11 LM = 0.68 Lm = 1.75 Lb =
10.93
Lmp = 3.32 Lbp =
7.22

NON-DIMENSIONAL PARAMETERS

FR0 = 20.84 FRD0 = 3.40 R = 4.95 PL =

137.64
(slot) (port/nozzle)

RECOMPUTED SOURCE CONDITIONS FOR ALTERNATING JETS OR RISER GROUPS:

Momentum fluxes: m0 =0.7659E-03 M0 =0.2719E-01
lQ=B = 0.004 lM = 0.18 lm = 0.09 lmp =
1.50
LQ = 0.353 LM = 0.68 Lm = 1.75 Lmp =
3.32
Properties of riser group with 1 ports/nozzles each:
U0 = 0.490 D0 = 0.120 A0 = 0.011 THETA =

90.00

FR0 = 20.84 FRD0 = 3.40 R = 4.95
(slot) (riser group)

FLOW CLASSIFICATION

222222222222222222222222222222222222222222222222
2 Flow class (CORMIX2) = MS6 2
2 Applicable layer depth HS = 35.50 2
222222222222222222222222222222222222222222222222

MIXING ZONE / TOXIC DILUTION / REGION OF INTEREST PARAMETERS
C0 =0.1490E+03 CUNITS= mg/l
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

0.00 0.00 0.10 1.0 0.149E+03 0.06 0.06

0.490 .00000E+00

END OF MOD101: DISCHARGE MODULE (SINGLE PORT AT DIFFUSER CENTER)

---------------------------------------------------------------------
-----------------------
---------------------------------------------------------------------
-----------------------
BEGIN CORJET (MOD110): JET/PLUME NEAR-FIELD MIXING REGION

Plume-like motion in linear stratification with strong crossflow.

Zone of flow establishment: THETAE= 85.22 SIGMAE=

0.00

LE = 0.21 XE = 0.01 YE = 0.00 ZE =

0.31

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
0.01 0.00 0.31 1.0 0.149E+03 0.06 0.06

0.490 .00000E+00

0.01 0.00 0.31 1.0 0.149E+03 0.06 0.06

0.490 .14676E-02

9.61 0.00 1.34 34.0 0.439E+01 0.58 0.58

0.060 .48778E+02

19.29 0.00 1.72 69.3 0.215E+01 0.86 0.86

0.040 .11461E+03

28.98 0.00 1.96 103.9 0.143E+01 1.07 1.07

0.031 .18680E+03

```

```
38.67 0.00 2.17 139.4 0.107E+01 1.25 1.25

0.027 .26266E+03
Merging of individual jet/plumes to form plane jet/plume:
39.14 0.00 2.18 169.9 0.877E+00 1.11 18.86

0.019 .26638E+03

58.05 0.00 2.47 225.0 0.662E+00 1.50 19.25

0.016 .42915E+03

67.75 0.00 2.61 251.4 0.593E+00 1.68 19.43

0.015 .51368E+03

77.44 0.00 2.75 276.8 0.538E+00 1.86 19.61

0.015 .59880E+03

87.13 0.00 2.89 301.1 0.495E+00 2.03 19.78

0.014 .68444E+03

96.82 0.00 3.01 324.3 0.459E+00 2.19 19.94

0.013 .77051E+03

106.52 0.00 3.13 346.5 0.430E+00 2.35 20.10

0.013 .85690E+03

116.21 0.00 3.24 367.6 0.405E+00 2.50 20.25

0.012 .94386E+03

125.90 0.00 3.35 387.6 0.384E+00 2.64 20.39

0.012 .10311E+04

135.53 0.00 3.44 406.2 0.367E+00 2.78 20.53

0.011 .11181E+04

145.15 0.00 3.52 423.6 0.352E+00 2.90 20.65

0.011 .12050E+04

154.77 0.00 3.59 439.8 0.339E+00 3.02 20.77

0.011 .12927E+04

164.39 0.00 3.65 454.7 0.328E+00 3.13 20.88

0.010 .13808E+04

174.01 0.00 3.70 468.4 0.318E+00 3.23 20.98

0.010 .14688E+04

183.63 0.00 3.73 480.7 0.310E+00 3.32 21.07

0.010 .15569E+04

193.25 0.00 3.75 491.7 0.303E+00 3.40 21.15

0.010 .16450E+04

Terminal level in stratified ambient has been reached.
Cumulative travel time = 1644.9659 sec ( 0.46 hrs)

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

180.70 0.00 3.75 667.6 0.223E+00 3.40 21.15

.16450E+04

181.95 0.00 3.75 667.6 0.223E+00 3.65 21.71

.16576E+04

183.21 0.00 3.75 667.6 0.223E+00 3.88 22.30

.16703E+04

184.46 0.00 3.75 667.6 0.223E+00 4.09 22.93

.16830E+04

185.72 0.00 3.75 667.6 0.223E+00 4.28 23.59

.16957E+04

186.97 0.00 3.75 667.6 0.223E+00 4.46 24.28

.17084E+04

188.23 0.00 3.75 667.6 0.223E+00 4.62 24.99

.17210E+04

189.48 0.00 3.75 667.6 0.223E+00 4.77 25.73

.17337E+04

190.74 0.00 3.75 667.6 0.223E+00 4.91 26.50

.17464E+04

191.99 0.00 3.75 667.6 0.223E+00 5.03 27.28

.17591E+04

193.25 0.00 3.75 667.6 0.223E+00 5.15 28.09

.17717E+04

194.50 0.00 3.75 667.6 0.223E+00 5.25 28.91

.17844E+04

195.76 0.00 3.75 667.6 0.223E+00 5.35 29.74

.17971E+04

197.01 0.00 3.75 667.6 0.223E+00 5.44 30.59

.18098E+04

198.27 0.00 3.75 667.6 0.223E+00 5.52 31.46

.18225E+04

199.53 0.00 3.75 667.6 0.223E+00 5.60 32.33

.18351E+04

200.78 0.00 3.75 667.6 0.223E+00 5.67 33.22

.18478E+04

202.04 0.00 3.75 667.6 0.223E+00 5.73 34.12

.18605E+04

```

```
203.29 0.00 3.75 667.6 0.223E+00 5.79 35.03

.18732E+04

204.55 0.00 3.75 667.6 0.223E+00 5.84 35.95

.18858E+04

205.80 0.00 3.75 667.6 0.223E+00 5.89 36.87

.18985E+04
Cumulative travel time = 1898.5244 sec ( 0.53 hrs)

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

205.80 35.50 3.75 667.6 0.223E+00 6.01 72.37 6.75

0.75 .18985E+04

445.51 35.50 3.75 845.0 0.176E+00 3.03 181.85 5.26

2.24 .43198E+04

```

```
685.22 35.50 3.75 927.9 0.161E+00 2.39 252.74 4.95

2.56 .67411E+04

924.93 35.50 3.75 993.9 0.150E+00 2.09 310.11 4.79

2.71 .91625E+04

1164.64 35.50 3.75 1056.6 0.141E+00 1.91 360.09 4.71

2.80 .11584E+05

1404.35 35.50 3.75 1120.5 0.133E+00 1.80 405.42 4.65

2.85 .14005E+05

1644.06 35.50 3.75 1187.6 0.125E+00 1.73 447.63 4.62

2.89 .16426E+05

1883.77 35.50 3.75 1258.9 0.118E+00 1.68 487.67 4.59

2.91 .18848E+05

2123.48 35.50 3.75 1334.4 0.112E+00 1.65 526.18 4.58

2.93 .21269E+05

2363.19 35.50 3.75 1414.1 0.105E+00 1.63 563.59 4.57

2.93 .23690E+05

2602.90 35.50 3.75 1497.8 0.995E-01 1.62 600.21 4.56

2.94 .26112E+05

2842.61 35.50 3.75 1585.2 0.940E-01 1.62 636.26 4.56

2.94 .28533E+05

3082.32 35.50 3.75 1676.1 0.889E-01 1.62 671.90 4.56

2.94 .30954E+05

3322.03 35.50 3.75 1770.2 0.842E-01 1.63 707.27 4.57

2.94 .33376E+05

3561.74 35.50 3.75 1867.3 0.798E-01 1.64 742.44 4.57

2.93 .35797E+05

3801.45 35.50 3.75 1967.2 0.757E-01 1.65 777.49 4.58

2.93 .38218E+05

4041.16 35.50 3.75 2069.7 0.720E-01 1.66 812.46 4.58

2.92 .40640E+05

4280.87 35.50 3.75 2174.7 0.685E-01 1.67 847.40 4.59

2.92 .43061E+05

4520.58 35.50 3.75 2282.0 0.653E-01 1.68 882.34 4.59

2.91 .45482E+05

4760.29 35.50 3.75 2391.5 0.623E-01 1.70 917.29 4.60

2.90 .47903E+05

5000.00 35.50 3.75 2503.2 0.595E-01 1.71 952.28 4.61

2.90 .50325E+05
Cumulative travel time = 50324.7773 sec ( 13.98 hrs)

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