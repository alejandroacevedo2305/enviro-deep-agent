---
title: Microsoft Word - Calculo ET0.doc
author: icf
date: D:20111213095452
language: es
type: report
pages: 13
has_toc: False
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Cálculo de ET 0 : MÉTODO DE PENMAN-MONTEITH
-->

# Cálculo de ET 0 : MÉTODO DE PENMAN-MONTEITH

LA FORMULACIÓN ESTÁ EXTRAIDA DE:

FOOD AND AGRICULTURE ORGANIZATION OF THE UNITED NATIONS

Rome
Italy
28-31 May1990

Expert consultation on revision of FAO methodologies for crop water requirements

ANNEX V, FAO PENMAN-MONTEITH FORMULA,

La fórmula utilizada para el cálculo de ET 0 es la [f69]

(Con actualización en el cálculo de la radiación neta de onda larga según Monografía no 56 de la FAO)

(Traducido por Tragsatec)

PARÁMETROS USADOS EN LA ECUACIÓN DE LA ET 0

Conversión entre los sistemas S.I. (Sistema Internacional) - C.G.S. (Sistema Cegesimal de Unidades)

Se usan las unidades S.I. en aplicación de los estándares internacionales, en todos los parámetros y
ecuaciones remplazando las unidades c.g.s usadas anteriormente. Se usan los siguientes factores de
conversión:

Presión 1 mbar ⇒ 0,1 kPa (kiloPascal)
Radiación 1 cal cm [-2] d [-1] ⇒ 0,041868 MJ m [-2] d [-1]
1 MJ m [-2] d [-1] ⇒ 23,884 cal cm [-2] d [-1] ⇒ 0,408 mm d [-1]
1 mm d [-1] ⇒ 2,45 MJ m [-2] d [-1] ⇒ 58,6 cal cm [-2] d [-1]
1 Wm [-2] ⇒ 0,0864 MJ m [-2] d [-1] ⇒ 2,064 cal cm [-2] d [-1]

Calor Latente de Vaporización (λ)

λ = 2,501 - ( 2,361 * 10 [-3] ) T

donde λ: Calor Latente de Vaporización [ MJ kg [-1] ]
**T** : Temperatura del Aire [oC]

Referencia: Harrison 1963

Página 1 de 13

Pendiente de la Curva de Presión de Vapor (∆): (Relaciona la presión del vapor con la temperatura)

∆ = 4098 e a
2
### ( T + 237,3 )

Donde **∆** : Pendiente de la Curva de Presión de Vapor [kPa oC [-1] ]
e a : Presión de Vapor de Saturación a temperatura T [kPa]
T: Temperatura del Aire [oC]

Referencias: Tetens (1930), Murray (1967). Obtenida de la ecuación (10).

Constante Psicrométrica (γ)

γ = c p Px 10 -3 =0,00163 P
ελ λ

Donde **γ** : Constante Psicrométrica [kPa oC [-1] ]
c p : Calor específico del aire húmedo = 1,013 [kJ kg [-1] oC [-1] ]
P: Presión Atmosférica [kPa]
ε: Relación peso molecular aire húmedo/aire seco = 0,622
**λ** : Calor Latente [ MJ kg-1]

Referencias: Brunt (1952)

Presión Atmosférica (P)

5,26
, 3 293 - 0,0065z 

P = 101, 3 293 - 0,0065z 
 293 

,

Donde P: Presión atmosférica a una cota z [ kPa]
z: altura sobre el nivel del mar (cota) [m]

Asumiendo que:
P o = 101,3 [kPa] a z o = 0
Tk o = 293 [K] for T = 20 [oC]

Referencias: Burman et al. (1987)

Densidad Atmosférica (ρ)

1000 P

=

P P

T kv R =3,486 T

= =

ρ,

T kv R T kv

T

Página 2 de 13

Donde **ρ** : Desidad atmosférica [kg m-3]
P: Presión atmosférica a una altura z [ kPa]
R: Constante específica del gas = 287 [J kg [-1] K [-1] ]
T kv : Temperatura [K]

-1
T kv = T k  1 0 -,378 e d 
 P 

Donde T k : Temperatura absoluta [K] _ 273 + T [oC]
e d : Presión de vapor en el punto de rocío [kPa]
P: Presión atmosférica a una altura z [ kPa]

La Figura muestra las pequeñas variaciones de Tkv para diferentes valores de la temperatura, humedad
y altitud.

**Figura 1**

Presión de Vapor de Saturación (ea)

e a =0,611 exp  17,27 T

 T + 237,3

 17,27 T 

 T + 237,3 




Donde e a : Presión de Vapor de Saturación [kPa]
T: Temperatura [oC]

Referencias: Tetens, 1930.

Presión de Vapor Actual (ed)

Se define como la Presión de Vapor de Saturación a la temperatura del punto de rocío (ed). La Presión
de Vapor Actual o media diaria del vapor de presión, puede ser determinada a partir de:

Página 3 de 13

Medida higrométrica (RH) donde: La media diaria del vapor de presión es mejor calcularla a partir de la
medida de dos humedades relativas a Tmax (a primera hora de la tarde) y a Tmin (a primera hora de la
mañana)

+ e d ( T max ) = 1 e a( T min ) . RH max + 1 e a( T max ) RH

2 2 100 2 100

e d =e d ( T min ) + e d ( T max ) = 1 e a( T min ) . RH max + 1 e a( T max ) RH min

min max

min max

Radiación Extraterrestre (Ra)

24x60
R a = G sc d r _( ω s sin φ sin δ + cos φ cos δ sin ω s )
π

Donde R a : Radiación Extraterrestre [MJ m [-2] d [-1] ]
G sc : Constante Solar [MJ m-2 min-1] = 0,0820
d r : Distancia relativa Tierra-Sol
**δ** : Declinación solar [rad]
**φ** : Latitud [rad]
**ω** s : Ángulo a la hora de la puesta de Sol [rad]

ω s = arccos(- tan φ tan δ )

2 π
d r = 1 +0,033 cos( 365 _J)= 1 +0,033 cos (0,0172J)

2 π
δ =0,409 sin( 3651 - J,39)_ =0,409 sin (0,0172J1 -,39)

Donde J: Día Juliano [ ]

Referencias: Duffie and Beckman (1980)

Para valores mensuales J puede ser calculado por:

### J= integer ( 30,42 M - 15,23 )

Donde M: Numero del mes (1 - 12) [ ]

Referencias: Gommes (1983)

Para valores diarios, J puede ser calculado por:

J = integer  275 M -30 + D  − 2
 9 

Donde M: Numero del mes (1 - 12) [ ]
D: Día del mes [ ]
Si M < 3, entonces J = J+2.

Página 4 de 13

SI el año es bisiesto y M > 2, entonces J = J+1

Referencias: Craig (1984).

Nota: Para los meses de invierno y latitudes por encima de los 55 grados, la ecuación tiene una validez
limitada y se debería consultar las tablas de Smithsonian para comprobar posibles desviaciones.

Horas de Luz (N)

24
N = ω s =7,64 ω s
π

Donde N: Horas de Luz [h]
**ω** s : Ángulo a la hora de la puesta de Sol [rad]

Página 5 de 13

ECUACIÓN DE PENMAN- MONTEITH

La forma original de la ecuación de Penman-Monteith puede ser escrita como:

ET o = ∆ ( R n - G)+ ρ c p ( e a - e d )/ r

∆ + γ (1+ r c [ / ] r a )

λ ET o = ∆ ( R n - G)+ ρ
∆ +

= n p a d r a

o

∆ + γ (1+ r c [ / ] r a )

Donde **λ** ET 0 : Flujo del Calor Latente de Evaporación [kJ m [-2] s [-1] ]
R n : Flujo de la Radiación neta en superficie [kJ m [-2] s [-1] ]
G: Flujo térmico del suelo [kJ m [-2] s [-1] ]
**ρ** : Densidad atmosférica [kg m [-3] ]
c p : Calor específico del aire húmedo [kJ kg [-1] oC [-1] ]
(e a -e d ): Déficit de Presión de Vapor [kPa]
r c : Resistencia de la cubierta vegetal [s m [-1] ]
r a : Resistencia aerodinámica [s m [-1] ]
**∆** Pendiente de la Curva de Presión de Vapor [kPa oC [-1] ]
**γ** : Constante Psicrométrica [kPa oC [-1] ]
λ: Calor Latente de Vaporización [ MJ kg [-1] ]

Referencias : Monteith (1965, 1981)

Factores de Resistencia

Para valores de velocidad del viento, temperatura y humedad medidos a una altura estándar de 2,00 m,
y un valor para la altura de la cubierta vegetal de 0,12 m, la resistencia aerodinámica puede ser estimada como
sigue:

208
r a =
U 2

Donde r a : Resistencia aerodinámica [s m [-1] ]
U 2 : Velocidad del viento a 2 metros de altura [m s [-1] ]
Coeficiente 208 [ ] para temperatura/humedad medidas a 2 m de
altura, estándar recomendado por OMM para estaciones agrícolas
Coeficiente 199 [ ] para temperatura/humedad medidas a 5 m de
altura, práctica común aun en muchas estaciones no automáticas
con sensor de temperatura a nivel de los ojos.

Página 6 de 13

Constante Psicrométrica Modificada (γ*)

 [] 1+ r c  []

 r a 



r
= γ  [] 1+

 r

a

γ - = γ  [] 1+ r c

 []


Donde **γ** *: Constante psicrométrica modificada [kPa oC [-1] ]
**γ** : Constante psicrométrica [kPa oC [-1] ]
r c : Resistencia de la cubierta vegetal [s m [-1] ]
r a : Resistencia aerodinámica [s m [-1] ]

Referencias : Monteith (1965)

Término Aerodinámico

Las fórmulas correspondientes al termino aerodinámico, se encuentran integradas en la fórmula de
Penman-Monteith f(30).

Término de Radiación

Radiación Neta (Rn)

R n = R ns ↓ - R nl ↑

Donde R n : Radiación neta [MJ m [-2] d [-1] ]
R ns : Radiación neta entrante de onda corta [MJ m [-2] d [-1] ]
R nl : Radiación neta saliente de onda larga [MJ m [-2] d [-1] ]

Radiación neta de onda corta Rns La radiación neta de onda corta es la radiación recibida por la
cubierta vegetal teniendo en cuenta las perdidas por reflexión:

R ns = (1 - α )R s ≈ 0,77 R s

Donde **α** : Albedo o coeficiente de reflexión de la cubierta = 0,23 valor medio
para hierba.
R s : Radiación solar entrante [MJ m [-2] d [-1] ]

La radiación solar puede ser medida en las estaciones agrometeorológicas más avanzadas mediante
distintos radiómetros y piranómetros. En cualquier caso requieren de cuidadosas calibraciones y
mantenimientos. Aunque las estaciones automáticas equipadas con piranómetros están muy extendidas, la
medida de la radiación solar puede que no este disponible en algunas estaciones agrometeorológicas.

Página 7 de 13

La radiación de onda corta puede ser, en algunos casos, estimada a partir de la medida de las horas de
insolación, atendiendo a la siguiente fórmula empírica:

R s =  a s +b s Nn  R a

Donde a s : Fracción de la radiación extraterrestre (Ra) en días cubiertos ≈
0,25 para climas medios.
a s + b s : Fracción de la radiación en días claros ≈ 0,75
b s ≈ 0.50 para climas medios
n/N: Fracción relativa de insolación [ ]
n: Horas de insolación por día [hr]
N: Longitud total del día [hr]
Ra: Radiación extraterrestre [MJ m [-2] d [-1] ]

Los datos disponibles de radiación local pueden ser usados para determinar, a partir de un análisis de
regresión, los coeficientes as y bs de acuerdo a la siguiente relación:

R so =( a s + b s )R a ≈ (0,75) R a

Donde R so : medida de la radiación de onda corta durante la insolación [MJ m [-2] d [-1] ]
Ra: Radiación extraterrestre [MJ m [-2] d [-1] ]

Dependiendo de las condiciones atmosféricas (humedad, polvo) y la declinación solar (latitud y mes del
año) los valores de los coeficientes as y bs pueden variar.

Cuando no se dispone de datos de radiación solar actuales y no se han realizado calibraciones para
mejorar los valores de as y bs, los siguientes valores son recomendados para climas medios:

as = 0,25
bs = 0,50
Para α = 0,23 cultivo de referencia (cubierta de gramíneas)

Radiación neta de onda larga (Rnl) (Modificación de la FAO en su monografía No 56, Pág. 52, Fórmula
39)

Se trata de la radiación térmica que emite la vegetación y el suelo hacia la atmósfera y la radiación
reflejada por la atmósfera y las nubes. Puede ser expresada, según la ley de radiación, como sigue:

FAO Monografía no 56, Pág. 52.

##  (,034 −,014 e a )  [],135 R s −

R

  so

## = σ T max, K 4 + T min, K 4  (,034 −,014 e a )  [],135 R s −,035

2 R

 

4 4
T max, K + T min, K 

2

 

R
## (,034 −,014 e a )  [],135 s −,035 []

R

 so 

 R s − 

 [],135,035 []

R

 so 

## R nl = σ T max, K + T min, K (,034 −,014 e a )  [],135 R s

2 R

 

so

Donde R nl : Radiación neta de onda larga [MJ m [-2] d [-1] ]
Σ: Constante de Stefan-Boltzmann = 4.903 x 10 [-9] [MJ m [-2] K [-4] d [-1] ]
Tmax: Temperatura máxima en un periodo de 24 horas [K ]

Página 8 de 13

Tmin: Temperatura mínima en un periodo de 24 horas [K]
Ea: Presión de Vapor Actual [Kpa] (Epsilon)
R s /R so : Radiación relativa de onda corta (factor)
R s : Radiación solar medida o calculada [MJm [-2 ] d [-1] ]
R so : Radiación calculada con cielo despejado calculada [MJm [-2] d [-1] ]

Factor de nubosidad (f) Cuando los datos de radiación solar están disponibles, la radiación térmica
neta puede ser estimada usando la siguiente expresión para determinar el factor de nubosidad:

f= R nl =  [] a c R s +b c
R nlo  R so

 []


nl

 [] a c R s +b c  []

 R so 

=  a c s

nlo  R

Donde f: Factor de nubosidad [ ]
R nl : Radiación neta de onda larga [MJ m [-2] d [-1] ]
R nlo : Radiación neta de onda larga para cielos despejados [MJ m [-2] d [-1] ]
R s : Radiación solar de onda corta medida [MJ m [-2] d [-1] ]
Rso: Radiación solar de onda corta con cielo despejado [MJ m [-2] d [-1] ]
ac + bc: Factor de nubosidad para cielo despejado [ ] = 1.0
ac ≈1,35 (Zonas áridas) - 1.0 (Zonas húmedas)

Referencias: Wright y Jensen (1972), Jensen et al. (1990).

Emisividad neta **ε** '

′
## ε =( ε a - ε vs )= ( a l + b l e d ) ( _ 0.34 - 0.14 e d )

Donde **ε** ': Emisividad neta

e d : Presión de Vapor en punto de rocío [kPa]
a l : Coeficiente de Correlación [] 0,34 - 0,44
b l : Coeficiente de Correlación [] -0,14 - -0,25

Referencias : Brunt (1932), Jensen et al. (1990)

Flujo Térmico del Suelo (G)

El calor se almacena y se desprende del suelo. Para estimar el flujo térmico del suelo para un periodo
dado se puede usar la siguiente ecuación:

 G = c s d s  T n ∆ Tt n-1 

Donde G: Flujo Térmico del Suelo [MJ m [-2] d [-1] ]
T n : Temperatura [oC] en el día (o en el mes) n
T n-1 : Temperatura [oC] en el día precedente (o en el mes) n-1
**∆** t: Longitud del periodo n [d]

Página 9 de 13

c s : Calor específico [MJ m [-3] oC [-1] ] ≈ 2.1 [MJ m [-3] oC [-1] ] para un suelo mojado
medio.
ds: Profundidad estimada del suelo efectivo [m]

Referencias : V. Wijk and De Vries (1963)

Página 10 de 13

FÓRMULA COMBINADA RECOMENDADA PARA LA EVAPOTRANSPIRACIÓN DE REFERENCIA

(ET 0 )

Se define la Evapotranspiración de Referencia (ET 0 ) como el valor de Evapotranspiración para un cultivo
ideal de 12 cm de altura, con una resistencia de cubierta fija de 70 sm [-1] y un albedo de 0,23, muy similar a la
evapotranspiración de una superficie extensa de gramíneas de altura uniforme, crecimiento activo, sombreando
completamente el terreno y bien regado. La estimación de la ET 0 puede ser determinada con la fórmula
combinada basada en la propuesta de Penman-Monteith. Cuando se combinan las fórmulas encontradas para
los términos aerodinámicos y de radiación, la fórmula puede ser anotada como:

900
0,408 ∆ ( R n - G)+ γ U 2 ( e a - e d )
ET o = T + 273

∆ + γ (1+ 0,34U 2 )

n 2 a d

γ

,

∆

o

∆ + γ (1+ 0,

∆

+ γ (1+ 0,34U 2 )

γ

Donde Et 0 : Evapotranspiración de referencia [mm d [-1] ]
Rn: Radiación neta en la superficie de la planta [MJ m [-2] d [-1] ]
G: Flujo térmico del suelo [MJ m [-2] d [-1] ]
T: Temperatura media [oC]
U 2 : Velocidad del viento medida a 2 m de altura [m s [-1] ]
(e a -e d ) Déficit de la Presión de Vapor [kPa]
**∆** : Pendiente de la Curva de Presión de Vapor [kPa oC [-1] ]
**γ** : Constante psicrométrica [kPa oC [-1] ]: ecuación (4)
900: Factor de conversión

Cuando los datos de la medición de la radiación no están disponibles, la radiación neta puede ser
estimada como sigue:

= R n R ns R nl

n
R ns =0,77(0,25 +0,50 )R a

N

R nl =2,45 . 10 - 9 (0,9 n + _0,1)(0,340 -,14 ed ( ) T 4kx +T 4kn

,45 . 10 - 9 (0,9 + _0,1)(0,340 -,

N + _0,1)(0,340 -,14 ed ( ) T kx +T kn )

G =0,14( T monthn - T monthn -1 )_ ≈ 0

Donde R n : Radiación neta [MJ m [-2] d [-1] ]
R [ns] : Radiación neta de onda corta [MJ m [-2] d [-1] ]
R nl : Radiación neta de onda larga [MJ m [-2] d [-1] ]
R a : Radiación extraterrestre [MJ m [-2] d [-1] ].
n/N: Fracción relativa de Insolación []
T kx Temperatura máxima [K]
T kn : Temperatura mínima [K]
e d : Presión de Vapor Actual [kPa]
G: Flujo térmico del suelo [MJ m [-2] d [-1] ]

Página 11 de 13

REFERENCIAS DEL INFORME DE LA FAO

- Allen R.G. (1986). A Penman for all seasons. J. Irrig. and Drain Engng., ASCE, 112(4):348368.

- Allen R.G. and Pruitt W.O. (1986). Rational use of the Blaney-Criddle formula. J. Irrig. and
Drain. Engrg. ASCE 112(IR2):139-155

- Allen R.G., Jensen M.E., Wright J.L. and Burman R.D. (1989). Operational estimates of
evapotranspiration. Agron. J. 81:650-662.

- Bosen J.F. (1958). An approximation formula to compute relative humidity from dry bulb
and dew point termperatures. Monthly Weather Rev. 86(12):486.

- Brunt D. (1932). Notes on radiation in the atmosphere. Quart. J. Roy. Meteorol. oc. 58:389418.

- Brunt D. (1952). Physical and dynamical meteorology, 2nd ed. University Press,
Cambridge. 428 pp.

- Brutsaert W. (1975). The roughness length for water vapor, sensible heat and other
scalars. J. Atm. Sci. 32:2028-2031.

- Burman R.D., Jensen M.E. and Allen R.G. (1987). Thermodynamic factors in
evapotranspiration. In: Proc. Irrig. and Drain. Spec. Conf., James L.G. and English M.J.
(eds). ASCE, Portland, Ore., July. pp. 28-30.

- Craig J.C. (1984). Basic routines for the Casio computer. Wayne Green Books,
Peterborough, NH 03458. 131 pp.

- Doorenbos J. and Pruitt W.O. (1976). Guidelines for predicting crop water requirements.
FAO Irrigation and Drainage Paper 24, 2nd ed. Rome. 156 pp.

- Duffie J.A. and Beckman W.A. (1980). Solar engineering of thermal processes. John WIley
and Sons, New York. pp. 1-109.

- Frère M. and Popov G.F. (1979). Agrometeorological crop monitoring and forecasting. FAO
Plant Production and Protection Paper 17, Rome. pp. 38-43.

- Frevert D.K., Hill R.W. and Braaten B.C. (1983). Estimation of FAO evapotranspiration
coefficients. J. Irrig. and Drain. ASCE 109(IR2):265-270.

- Gommes R.a. (1983). Pocket computers in agrometeorology. FAO Plant Production and
Protection Paper 45, Rome.

- Harrison L.P. (1963). Fundamental concepts and definitions relating to humidity. In:
Humidity and Moisture. Vol. 3. Wexler A. (ed). Reinhold Publishing Company, New York.

- Idso S.B. and Jackson R.D. (1969). Thermal radiation from the atmosphere. J. Geophys.
Res. 74:5397-5403.

- Jensen M.E., Burman R.D. and Allen R.G. (1990). Evapotranspiration and irrigation water
requirements. ASCE Manual No. 70.

- Monteith J.L. (1965). Evaporation and the environment. In: The State and Movement of
Water in Living Organisms. XIXth Symposium. Soc. for xp. Biol., Swansea. Cambridge
University Press. pp. 205-234.

- Monteith J.L. (1981) Evaporation and surface temperature. Quarterly J. Royal Meteo. Soc.
107:1-27.

- Monteith J.L. and Unsworth M.H. (1990). Principles of Environmental Physics. Edward
Arnold, London.

- Murray F.W. (1967). On the computation of saturation vapor pressure. J. Appl. Meteor.
6:203-204.

Página 12 de 13

- Smith M. (1988). Calculation procedures of modified Penman equation for computers and
calculators. FAO, Land and Water Development Division, Rome.

- Tetens O. (1930). Uber einige meteorologische Begriffe. Z. Geophys. 6:297-309.

- van Wijk W.R. and de Vries D.A. (1963). Periodic temperature variations in a homogeneous
soil. In. Physics of the Plant Environment. van Wijk W.R. (ed). North-Holland Publishing
Co., Amsterdam. pp. 102-143.

- Wright J.L. (1982). New evapotranspiration crop coefficients. J. Irrig. and Drain. Div., ASCE
108(IR2):57-74.

- Wright J.L. and Jensen M.E. (1972). Peak water requirements of crops in Southern Idaho.
J. Irrig. and Drain. Div., ASCE 96(IR1):193-201.

Página 13 de 13