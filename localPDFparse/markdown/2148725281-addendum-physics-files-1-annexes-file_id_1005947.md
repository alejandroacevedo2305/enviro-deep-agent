---
title: MEMORIA CALCULOagroreservas
author: Claudia Muñoz Poblete
date: D:20201106142811Z00'00'
language: es
type: manual
pages: 13
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - MEMORIA DE CÁLCULO ESTRUCTURAL
-->

# MEMORIA DE CÁLCULO ESTRUCTURAL

## BODEGA Y TALLER AGRICOLA - AGRORESERVAS

|Mandante|ITO.|Cálculo|Fecha|
|---|---|---|---|
|<br>AGRORESERVAS DE CHILE SpA|<br> <br>|<br>IVÁN BARRIONUEVO|<br>Marzo 2017|

almacenamiento inofensivo

Memoria de Cálculo

### C O N T E N I D O

**1.0** **INTRODUCCIÓN .......................................................................................................................... 2**

**2.0** **BASES DE DISEÑO ..................................................................................................................... 2**

**3.0** **CRITERIOS DE DISEÑO ............................................................................................................... 4**

**4.0** **DISEÑO DE EDIFICIO PRINCIPAL .............................................................................................. 10**

Pág **1** de **13**

almacenamiento inofensivo

Memoria de Cálculo

**1.0** **INTRODUCCIÓN**

La Propiedad se encuentra emplazado en Fundo Longovilos - Melipilla, Santiago.

El proyecto considera la construcción de un galpón de estructura metálica destinado para almacenaje
inofensivo.

El sistema constructivo y/o materialidad será completamente en estructura metálica, los elementos de
apoyo y radieres se considera de hormigón con refuerzo armado, se construirá perimetralmente en base a
revestimiento metálico.

A la memoria de Estructuras no se adjunta estudio de mecánica.

**2.0** **BASES DE DISEÑO**

**2.1.** **Descripción de los materiales**

Ø Hormigón (ACI 318-08)

|DETALLE|Grado del<br>hormigón|Resistencia<br>especificada<br>fc’ (Kgf/cm2) *|Bolón<br>desplazador %|Nivel de<br>confianza<br>%|
|---|---|---|---|---|
|Emplantillado y Relleno|H-5|30|-|85|
|Radieres|H-25|200|-|95|
|Fundaciones|H-20|160|-|90|
|Pilares, vigas, cadenas|H-25|200|-|95|

Esta resistencia corresponde a los 28 días.

Ø Acero de refuerzo (ACI 318-08)

La calidad del acero que se utilizará corresponde al **A 63 - 42H.**

|Col1|Recubrimientos mínimos<br>cm.|
|---|---|
|Fundaciones|7.5|
|Pilares, vigas y cadenas|3.0|

Ø Acero Estructural (NCh 427 Of99)

La calidad del acero que se utilizará corresponde al **A 42 - 27 ES.**

**2.2.** **Modelación**
La estructura se modelo en base a marcos estructurales de acero, sistema tomando los criterios de
LRFD.

Pág **2** de **13**

almacenamiento inofensivo

Memoria de Cálculo

**2.3.** **Zona sísmica**
El emplazamiento del edificio será en Melipilla. Por tanto, corresponde a la zona sísmica 3.

Categoría del edificio tipo C, suelo tipo II.
Componente Sísmica del empuje: ss = 0,35 Ton/m2

**2.4.** **Tipo de suelo**

El suelo se clasifica según U.S.C.S. como **SM.**
Capacidad de Soporte qult : 1.00 kg/cm2 (asumido)
Capacidad de Soporte Sísmico qults : 1.50 kg/cm2
Conste. De Balasto Ks : 7 Kg/cm2
Asentamiento esperado ρ < 1.00 cm

**2.5.** **Combinaciones de carga.**

**-**
**COMBINACIONES DE CARGA PARA HORMIGÓN (ACI 318** **02):**

COMB 1 : 1.4D

COMB 2 : 1.2D + 1.6L

COMB 3 : 1.2D + L ± 1.6V

COMB 4 : 1.2D ± 0.80V

COMB 5 : 0.9D ± 1.6V

COMB 6 : 1.2D + L ± SX

COMB 7 : 1.2D + L ± SY

COMB 8 : 0.9D ± SX

COMB 9 : 0.9D ± SY

**COMBINACIONES DE CARGA ESTÁTICA PARA LOSAS Y VIGAS DE HORMIGÓN (ACI 318):**

COMB_10: 1.4D + 1.7L

**PARA DISEÑO DE ACERO: SEGÚN L.R.F.D. NCH 2369**

DSTL1 : 1.4D

DSTL 2 : 1.2D + 1.6L

DSTL 3 : 1.2D + 0.5L ± 1.3V

DSTL 4 : 0.9D ± 1.3V

DSTL 5 : 1.2D + 0.5L ± SX

DSTL 6 : 1.2D + 0.5L ± SY

DSTL 7 : 0.9D ± SX

DSTL 8 : 0.9D ± SY

Donde:
D: Peso Propio
L: Sobre Carga
V: Viento Transversal

N: Nieve

Pág **3** de **13**

almacenamiento inofensivo

Memoria de Cálculo

**PARA FUNDACIONES Y VERIFICACIÓN DE DEFORMACIONES: SEGÚN A.S.D.**

ASD1 : D + L

ASD2 : D + L + SX

ASD3 : D + L + SY

ASD4 : D + L + V

**2.6.** **Normas y códigos asumidos para el diseño**

NCh. 170 Of. 85 “Hormigón - Requisitos generales”
NCh. 1998 Of. 89 “Hormigón - Evaluación estadística de la resistencia mecánica”
NCh. 1537 “Diseño estructural de edificios - cargas permanentes y sobrecargas de uso”
NCh 432 of94 “Cálculo de la acción del viento sobre las construcciones”
NCh 431 of94 “Construcción-Sobrecargas de nieve”
NCh 433 Of. 96 “Diseño sísmico de edificios”
Código ACI 318-08 “Diseño de hormigón armado”
NCh 427 cR76 “Especificaciones para el cálculo de estructuras de acero para edificios”
NCh 2369 Of 2003 “Diseño sísmico de estructuras e instalaciones Industriales”
Manual de Diseño para Estructuras de Acero. Instituto Chileno del Acero ICHA. Año 2001.

**2.7.** **Software utilizados:**

§ SAP 2000 versión v12

§ AUTOCAD 2012

**3.0** **CRITERIOS DE DISEÑO**

**3.1** **Criterios de diseño y cálculo de columnas y muros de hormigón armado.**
Las verificaciones se deben realizar de acuerdo con los criterios que fija el código ACI318-08. Se debe
verificar:

Ø Interacción.

Ø Corte

**3.2** **Verificación de Deformaciones, AISC-ASD.**
Según recomendaciones entregadas por NCH427

**3.3** **Diseño de Anclajes**
Según antiguo manual ICHA, Capítulo 1.8.2 pág. 590.

**3.4** **Criterios de diseño y cálculo de fundaciones.**
Se deben diseñar las fundaciones corridas y aisladas ante cargas de servicio, verificando:

þ Tensiones de contacto para condición de carga estática y condición de carga estática combinada

con sismo.
þ Volcamiento, aceptando una compresión mínima de 80%.

Pág **4** de **13**

almacenamiento inofensivo

Memoria de Cálculo

**3.5** **Capacidad de Carga del Suelo de Fundación**
La Capacidad de Carga de fundaciones continuas, colocadas sobre suelos cohesivos o no cohesivos, se
obtiene por medio de la ecuación (Terzaghi):

1
s max = C ́ Nc + g ́ Df ́ Nq + 2 g ́ b ́ Ng

Donde:

s MAX : Es la tensión máxima que el suelo de fundación es capaz de soportar, por unidad de
longitud, L = 1 mt.
B : Ancho de la fundación
H : Altura de la parte enterrada de la fundación.
C : Cohesión del suelo de fundación.

g : Peso unitario del suelo.

Nc, Nq y N corresponden a los parámetros de capacidad de carga de Terzaghi. g

g

g

Pág **5** de **13**

almacenamiento inofensivo

Memoria de Cálculo

Esta ecuación permite determinar la tensión máxima que puede soportar el suelo, en función de la
geometría de la zapata.

**3.6** **Tensiones de Trabajo del Suelo de Fundación**
Las tensiones de trabajo se obtienen a partir de las cargas de servicio, es decir, por tensiones admisibles

Se pueden presentar dos situaciones, dependiendo de la excentricidad resultante, estas son:

Excentricidad dentro del Núcleo Central:

= _N_ _G_ *æ +ç1 6* _e_ ö÷

_L_ - _b_ è _L_ ø

s 1 = _N_ - _G_ *æ +ç1 6*

_G_ *ç1 _e_

_L_ - _b_ è _L_

, y


= _N_ _G_ - æ -ç1 6 _e_ ö÷

_L_ - _b_ è _L_ ø

s 2 = _N_ - _G_ - æ -ç1 6

_G_ - ç1 _e_

_L_ - _b_ è _L_

Excentricidad fuera del Núcleo Central:

2 1 =

3* _b_

2 - _N_ _G_

=

s =
3* _b_ *μ

, y

_L_

μ = - _e_
2

,

Pág **6** de **13**

almacenamiento inofensivo

Memoria de Cálculo

Donde:

s1 = Corresponde a la tensión máxima que llega al sello de fundación producto de las cargas

externas aplicadas.
μ = Corresponde a la tensión mínima que llega al sello de fundación producto de las cargas

externas aplicadas
N G = Carga vertical que llega al centro geométrico de la fundación a nivel del sello de fundación
e = Excentricidad generada por el momento que llega al centro geométrico del sello de fundación,

e = MG/NG.

b = Ancho basal de la fundación.
L = Longitud de la fundación.

**Factores de Seguridad**
Existen dos factores de seguridad para la realización de las verificaciones de las tensiones de contacto:
uno para las tensiones que se obtienen a partir de la combinación de carga que incluye las cargas
estáticas y las cargas sísmicas; y otro para las tensiones obtenidas de la combinación que solo incluye
las cargas estáticas:

Estos factores de seguridad son:

@ FS ESTÁTICO + SISMO = 2

@ FS ESTÁTICO = 3

**Verificaciones**

Tensiones: Se realiza una verificación para cada estado de carga:

Con sismo:

s £ 1 s _MAX_

2

Sin sismo:

s £ 1 s _MAX_

3

Porcentaje de Compresión: Se realiza de manera distinta, dependiendo de la condición de excentricidad:

Excentricidad dentro del Núcleo Central:

_COMPRESIÓN_ = s - 1 s

1 2

% = *100

s

1

Excentricidad fuera del Núcleo Central:

% = 3*μ *100
_COMPRESIÓN_
_L_

Pág **7** de **13**

**3.7** **Te Cargas y Sobrecargas verticales y horizontales**

þ Selección de Elementos Estructurales

**Estructura**

**Vigas metálicas**

almacenamiento inofensivo

Memoria de Cálculo

Pág **8** de **13**

**Cerchas, tensores**

**Costaneras**

almacenamiento inofensivo

Memoria de Cálculo

Pág **9** de **13**

þ Cuadro de Cargas [Kg/m2].

A: Cálculo automático Software

þ Descripción Estados Básicos de Carga Módulo de dos pisos.

q Peso propio.

Ø Peso propio estructura: Automático.

Ø Peso propio cubierta: Manual.

**PP = 12 Kg/m2 (Panel PV6 = 0.5 mm)**

q Presión del Viento. Según NCh 432 Of77

Para una edificación de dos pisos, ubicación en ciudad.

**Presión Básica = 75 Kg/m2 (cuidad).**

q Sobrecarga de Nieve. Según NCh 431 Of94

Para ubicación en Santiago.

**Sobrecarga básica de Nieve = 25 Kg/m2**

**4.0** **DISEÑO DE EDIFICIO PRINCIPAL**

**4.1** **Modelación y Estructuración**
La modelación se realizó mediante software, como se muestra en la figura:

**Modelamiento Estructura - Isometria**

almacenamiento inofensivo

Memoria de Cálculo

Pág **10** de **13**

**Modelamiento Estructura SAP2000 v12 - Isometría**

**Modelo MARCO EJE 3-3**

almacenamiento inofensivo

Memoria de Cálculo

Pág **11** de **13**

**Deformada de la MARCO (Peso Propio) (mm)**

**Deformada de la MARCO (Viento) (mm)**

almacenamiento inofensivo

Memoria de Cálculo

Pág **12** de **13**