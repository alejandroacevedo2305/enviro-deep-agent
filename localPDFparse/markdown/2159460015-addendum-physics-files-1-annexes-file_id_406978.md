---
title: Sin título
author: Bisso Miguel
date: D:20240514212523-04'00'
language: es
type: report
pages: 9
has_toc: False
has_tables: True
extraction_quality: high
---

**INFORME DE DESARROLLO CONCEPTUAL PUENTE BASCULANTE**

**ANTECEDENTES GENERALES**

En el contexto del desarrollo del estudio conceptual para la instalación de una infraestructura portuaria,

consistente en un muelle flotante fondeado en lecho marino y un puente basculante de acceso entre

dicho muelle y la zona intermareal, en lo que sigue se presenta el proceso de diseño para el

dimensionamiento de las obras necesarias de construir en tierra, como apoyo fijo del puente basculante.

Para determinar el volumen de obras requeridas, se procedió a ejecutar la modelación de un diseño

posible de la estructura, con cargas de diseño de acuerdo a lo informado por la empresa mandataria,

posicionando el puente en su condición más desfavorable, esto es, con un desnivel de 1.5 entre su apoyo

fijo en la playa y la parte superior del muelle.

**MODELACIÓN**

De acuerdo a los requerimientos informados por la empresa, el puente deberá ser de 30 m de largo, por

4 de ancho, lo suficientemente rígido para soportar un vehículo tipo tracto camión con carro de hasta 45

toneladas, cuyas capacidades resistentes se encuentran por sobre la plataforma de rodado. De acuerdo a

esto y en base a la geometría y materialidad de otras estructuras similares instaladas en el país, la

modelación utilizada para la evaluación indicada, es la siguiente:

|Vistas Lateral y Frontal y Detalle|Vista Isométrica|
|---|---|
|||
|**Carga de Tránsito sobre Planchas de Acero, Camión de 45 ton.**|**Carga de Tránsito sobre Planchas de Acero, Camión de 45 ton.**|
|||

**VERIFICACION DE DISEÑO DE LA ESTRUCTURA DE PUENTE**

Para determinar las dimensiones de las fundaciones terrestres de la estructura, primero se debe diseñar

una, que sea resistente y capaz, que represente las condiciones reales a las que los cimientos se verán

expuestas.

Básicamente se usó una serie de perfiles tubulares de sección circular como estructura vertical y del tipo

W, como soporte horizontal, todo de calidad ASTM A36. El método de diseño es el LRFD, de factores de

carga y resistencia.

A continuación, se muestran los resultados obtenidos para los perfiles en base a sus factores de utilización.

**Estados de carga considerados :**
DS1=1.4CM

DS2=1.4CM+1.6TT

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------**Descripción** **Sección** **Miembro** **Ec. ctrl** **Relación Estatus**
**Referencia**

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Alma Diag Horiz** _**PIPE 6x0.280 - Copy(1)**_ **203** DS2 en 100.00% 0.23 Bien
**Alma Diagonal** **48** DS2 en 100.00% 0.19 Bien
**apoyo** _**PIPE 8x0.875XXS - Copy(1)**_ **2** DS2 en 100.00% 0.08 Bien
**Cordón superior** _**W 6X16 - Copy(1)**_ **17** DS2 en 100.00% **1.10** **No Cumple**
**Longerina** _**W 6X8.5 - Copy(1)**_ **539** DS2 en 37.50% 0.53 Bien
**Travesaño** _**W 6X16 - Copy(1)**_ **331** DS2 en 100.00% 0.77 Bien
**Vert Lateral** _**PIPE 6x0.280 - Copy(1)**_ **186** DS2 en 0.00% 0.20 Bien
**Viga** _**W 6X16 - Copy(1)**_ **125** DS2 en 0.00% 0.47 Bien

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
|Diagrama de Distribución de Tensiones|Figura Deformada|
|---|---|
|||

**VERIFICACION DE DISEÑO DE FUNDACIONES TERRESTRES**

Para la determinación de las dimensiones de las cimentaciones necesarias de ejecutar en la playa, para el

soporte del puente de acceso, se usaron las reacciones de apoyo generadas por la acción del tránsito

vehicular sobre la estructura, en su posición más desfavorable. El resultado para cada uno de los dos

puntos de apoyo, se muestra en el siguiente párrafo:

Datos Generales

Estatus global : Bien
Código de diseño : ACI 318-2019
Tipo de zapata : Aislada
Tipo de columna : Pedestal

**Materiales**
Hormigón, f'c : 210.92 [Kg/cm2] Acero, fy : 4218.40 [Kg/cm2]
Tipo de concreto : Normal Recubrimiento epóxico : No
Módulo de elasticidad hormigón : 219498.50 [Kg/c... Módulo de elasticidad acero : 2038891.00 [Kg/...
Peso unitario : 2399.84 [Kg/m3]

**Suelo**
Coeficiente de balasto : 3150000.00 [Kg/... Cohesión : 0.00 [Kg/m2]
Peso unitario (húmedo) : 1750.00 [Kg/m3] Ángulo de fricción interna : 30.00 [o]
Peso unitario saturado : 2250.00 [Kg/m3] Profundidad del nivel freático : 30.00 [m]
Inclinación del terreno : 0.00 [o]

Geometría

Longitud : 1.30 [m]
Ancho : 1.30 [m]
Espesor : 0.30 [m]
Profundidad de la base : 0.50 [m]

Área de la base : 1.69 [m2]
Volumen de la zapata : 0.51 [m3]

Longitud del pedestal : 30.00 [cm]
Ancho del pedestal : 30.00 [cm]
Alto del pedestal : 50.00 [cm]
Posición del pedestal respecto al c.g. de la zapata : Centrada

Refuerzo

**Armadura longitudinal**
Recubrimiento libre : 8.00 [cm]
Relación máxima permitida entre Rho/Rho balanceo : 0.75
Armadura // a L (xx) inferior : 4-#5 @ 38.00cm
Armadura // a B (zz) inferior : 4-#5 @ 38.00cm (Zona 1)

**Armadura del pedestal**
Longitudinal : 4 - #6
Recubrimiento libre : 2.50 [cm]
Área provista : 11.35 [cm2]
Número de barras // al eje x : 2
Número de barras // al eje z : 2

Transversal : #6 @ 30.00cm
Número de ramas // al eje x : 3
Número de ramas // al eje z : 3

Condiciones de carga
**Servicio:**

SC1 : CM

SC2 : CM+TT

**Límite ultimo:**

DC1 : 1.4CM

DC2 : 1.4CM+1.6TT

**Cargas**
**Estado** **Zapata** **Nudo** **Axial** **Mxx** **Mzz** **Vx** **Vz**

[Kg] [Ton*m] [Ton*m] [Kg] [Kg]

-----------------------------------------------------------------------------------------------------------------------------------------------
CM 1 36 6394.33 0.00 0.00 334.65 767.13

TT 1 36 6856.53 0.00 0.00 358.84 676.03

-----------------------------------------------------------------------------------------------------------------------------------------------
Diseño

Estatus : Bien

_**Interacción suelo - fundación**_

Esfuerzo debido al peso del relleno y de la zapata : 1.17E03 [Kg/m2]
Factor de seguridad min. para capacidad portante : 2.50
Factor de seguridad min. para deslizamiento : 1.25
Factor de seguridad min. a vuelco : 1.25

Esfuerzo efectivo previo (qef) : 875 [Kg/m2]
Estado gobernante : SC2 - 1

**Estado** **qu** **qnmax** **qnav** **FS**  **max** **Área** **Volteo** **FS**
**Zapata** [Kg/m2] [Kg/m2] [Kg/m2] **C. Port.** [cm] comp(%) **FSx** **FSz desliz.**

SC2 - 1 3.36E04 9.79E03 8.04E03 3.34 0.338 100 22.61 47.05 3.23

_**Flexión**_

Factor  : 0.90
Cuantía mínima : 0.00180

Longitud de desarrollo
**Eje** **Pos.** **ld** **lhd** **Dist1** **Dist2**

[cm] [cm] [cm] [cm]

---------------------------------------------------------------------------------------------------------------------------
z Inf. 61.04 21.36 42.00 42.00

x Inf. 61.04 21.36 42.00 42.00

---------------------------------------------------------------------------------------------------------------------------

**Eje** **Pos.** **Estado** **Mu**  ***Mn** **Asreq** **Asprov** **Asreq/Asprov Mu/(**  ***Mn)**
**Zapata** [Ton*m] [Ton*m] [cm2] [cm2]

----------------------------------------------------------------------------------------------------------------------------------------------------------------

zz Sup. DC1 - 1 0.00 0.00 0.00 0.00 0.000 0.000

zz Inf. DC2 - 1 2.02 6.22 7.02 8.00 0.878 0.325

xx Sup. DC1 - 1 0.00 0.00 0.00 0.00 0.000 0.000

xx Inf. DC2 - 1 2.13 5.74 7.02 8.00 0.878 0.371

----------------------------------------------------------------------------------------------------------------------------------------------------------------
_**Cortantes**_

Factor  : 0.75
Área de corte plano zz : 0.28 [m2]
Área de corte plano xx : 0.26 [m2]

**Plano** **Estado** **Vu** **Vc** **Vu/(**  ***Vn)**
**Zapata** [Kg] [Kg]

---------------------------------------------------------------------------------------------------------------------------

xy DC2 - 1 5190.45 11501.46 0.602

yz DC2 - 1 4661.58 12113.82 0.513

---------------------------------------------------------------------------------------------------------------------------
_**Corte por punzonamiento**_

Factor  : 0.75
Perímetro de corte (bo 1) : 2.02 [m]
Área de punzonamiento : 0.41 [m2]

**Columna** **Estado** **Vu** **Vc** **Vu/(**  ***Vn)**
**Zapata** [Kg] [Kg]

---------------------------------------------------------------------------------------------------------------------------

columna 1 DC2 - 1 16926.56 63403.19 0.356

---------------------------------------------------------------------------------------------------------------------------
_**Diseño del Pedestal**_

**Armadura:**
**Pedestal** **Asreq** **Asprov** **Asreq/Asprov**

[cm2] [cm2]

-----------------------------------------------------------------------------
1 9.00 11.35 0.79

-----------------------------------------------------------------------------
**Flexión biaxial:**

**Pedestal** **Estado** **Muxx** **Muzz**  ***Mnxx**  ***Mnzz** **Mc/(**  ***Mn)**
**Zapata** [Ton*m] [Ton*m] [Ton*m] [Ton*m]

------------------------------------------------------------------------------------------------------------------------------------------------------

1 DC2 - 1 0.00 0.48 0.00 6.72 0.07

------------------------------------------------------------------------------------------------------------------------------------------------------
**Axial:**

**Pedestal** **Estado** **Pu**  ***Pn** **Pu/(**  ***Pn)**
**Zapata** [Kg] [Kg]

------------------------------------------------------------------------------------------------------------------

1 DC2 - 1 -19922.50 -107752.90 0.18

------------------------------------------------------------------------------------------------------------------
**Corte:**

**Pedestal 1:**
S adoptado : 30.00 [cm]
S calculado : 30.00 [cm]

**Estado** **Dir.** **Vu** **Vc** **Vs**  ***Vn** **Vu/(**  ***Vn)**

[Kg] [Kg] [Kg] [Kg]

-----------------------------------------------------------------------------------------------------------------------------------------------------

DC2 x 1042.66 6590.01 22774.70 22023.53 0.05

DC2 z 2155.63 6590.01 22774.70 22023.53 0.10

-----------------------------------------------------------------------------------------------------------------------------------------------------

**VERIFICACION Y DIMENSIONAMIENTO DE DISEÑO DE FUNDACIONES TERRESTRES**

Para la determinación de las dimensiones de las cimentaciones necesarias de ejecutar en la playa, para el

soporte del puente de acceso, se usaron las reacciones de apoyo generadas por la acción del tránsito

vehicular sobre la estructura, en su posición más desfavorable. El resultado para cada uno de los dos

puntos de apoyo, se muestra en el siguiente párrafo:

Datos Generales

Estatus global : Bien
Código de diseño : ACI 318-2019
Tipo de zapata : Aislada
Tipo de columna : Pedestal

**Materiales**
Hormigón, f'c : 210.92 [Kg/cm2] Acero, fy : 4218.40 [Kg/cm2]
Tipo de concreto : Normal Recubrimiento epóxico : No
Módulo de elasticidad hormigón : 219498.50 [Kg/c... Módulo de elasticidad acero : 2038891.00 [Kg/...
Peso unitario : 2399.84 [Kg/m3]

**Suelo**
Coeficiente de balasto : 3150000.00 [Kg/... Cohesión : 0.00 [Kg/m2]
Peso unitario (húmedo) : 1750.00 [Kg/m3] Ángulo de fricción interna : 30.00 [o]
Peso unitario saturado : 2250.00 [Kg/m3] Profundidad del nivel freático : 30.00 [m]
Inclinación del terreno : 0.00 [o]

Geometría

Longitud : 1.30 [m]
Ancho : 1.30 [m]
Espesor : 0.30 [m]
Profundidad de la base : 0.50 [m]
Área de la base : 1.69 [m2]
Volumen de la zapata : 0.51 [m3]

Longitud del pedestal : 30.00 [cm]
Ancho del pedestal : 30.00 [cm]
Alto del pedestal : 50.00 [cm]
Posición del pedestal respecto al c.g. de la zapata : Centrada

Refuerzo

**Armadura longitudinal**
Recubrimiento libre : 8.00 [cm]
Relación máxima permitida entre Rho/Rho balanceo : 0.75
Armadura // a L (xx) inferior : 4-#5 @ 38.00cm
Armadura // a B (zz) inferior : 4-#5 @ 38.00cm (Zona 1)
**Armadura del pedestal**
Longitudinal : 4 - #6
Recubrimiento libre : 2.50 [cm]
Área provista : 11.35 [cm2]

Número de barras // al eje x : 2
Número de barras // al eje z : 2

Transversal : #6 @ 30.00cm
Número de ramas // al eje x : 3
Número de ramas // al eje z : 3

Condiciones de carga
**Servicio:**

SC1 : CM

SC2 : CM+TT

**Límite ultimo:**

DC1 : 1.4CM
DC2 : 1.4CM+1.6TT

**Cargas**
**Estado** **Zapata** **Nudo** **Axial** **Mxx** **Mzz** **Vx** **Vz**

[Kg] [Ton*m] [Ton*m] [Kg] [Kg]

-----------------------------------------------------------------------------------------------------------------------------------------------
CM 1 36 6394.33 0.00 0.00 334.65 767.13

TT 1 36 6856.53 0.00 0.00 358.84 676.03

-----------------------------------------------------------------------------------------------------------------------------------------------
Diseño

Estatus : Bien

_**Interacción suelo - fundación**_
Esfuerzo debido al peso del relleno y de la zapata : 1.17E03 [Kg/m2]
Factor de seguridad min. para capacidad portante : 2.50
Factor de seguridad min. para deslizamiento : 1.25
Factor de seguridad min. a vuelco : 1.25
Esfuerzo efectivo previo (qef) : 875 [Kg/m2]
Estado gobernante : SC2 - 1

**Estado** **qu** **qnmax** **qnav** **FS**  **max** **Área** **Volteo** **FS**
**Zapata** [Kg/m2] [Kg/m2] [Kg/m2] **C. Port.** [cm] comp(%) **FSx** **FSz desliz.**

SC2 - 1 3.36E04 9.79E03 8.04E03 3.34 0.338 100 22.61 47.05 3.23

_**Flexión**_

Factor  : 0.90
Cuantía mínima : 0.00180
Longitud de desarrollo
**Eje** **Pos.** **ld** **lhd** **Dist1** **Dist2**

[cm] [cm] [cm] [cm]

---------------------------------------------------------------------------------------------------------------------------
z Inf. 61.04 21.36 42.00 42.00

x Inf. 61.04 21.36 42.00 42.00

---------------------------------------------------------------------------------------------------------------------------
**Eje** **Pos.** **Estado** **Mu**  ***Mn** **Asreq** **Asprov** **Asreq/Asprov Mu/(**  ***Mn)**
**Zapata** [Ton*m] [Ton*m] [cm2] [cm2]

----------------------------------------------------------------------------------------------------------------------------------------------------------------

zz Sup. DC1 - 1 0.00 0.00 0.00 0.00 0.000 0.000

zz Inf. DC2 - 1 2.02 6.22 7.02 8.00 0.878 0.325

xx Sup. DC1 - 1 0.00 0.00 0.00 0.00 0.000 0.000

xx Inf. DC2 - 1 2.13 5.74 7.02 8.00 0.878 0.371

----------------------------------------------------------------------------------------------------------------------------------------------------------------
_**Cortantes**_

Factor  : 0.75
Área de corte plano zz : 0.28 [m2]
Área de corte plano xx : 0.26 [m2]

**Plano** **Estado** **Vu** **Vc** **Vu/(**  ***Vn)**
**Zapata** [Kg] [Kg]

---------------------------------------------------------------------------------------------------------------------------

xy DC2 - 1 5190.45 11501.46 0.602

yz DC2 - 1 4661.58 12113.82 0.513

---------------------------------------------------------------------------------------------------------------------------
_**Corte por punzonamiento**_

Factor  : 0.75
Perímetro de corte (bo 1) : 2.02 [m]
Área de punzonamiento : 0.41 [m2]

**Columna** **Estado** **Vu** **Vc** **Vu/(**  ***Vn)**
**Zapata** [Kg] [Kg]

---------------------------------------------------------------------------------------------------------------------------

columna 1 DC2 - 1 16926.56 63403.19 0.356

---------------------------------------------------------------------------------------------------------------------------
_**Diseño del Pedestal**_

**Armadura:**
**Pedestal** **Asreq** **Asprov** **Asreq/Asprov**

[cm2] [cm2]

-----------------------------------------------------------------------------
1 9.00 11.35 0.79

-----------------------------------------------------------------------------
**Flexión biaxial:**

**Pedestal** **Estado** **Muxx** **Muzz**  ***Mnxx**  ***Mnzz** **Mc/(**  ***Mn)**
**Zapata** [Ton*m] [Ton*m] [Ton*m] [Ton*m]

------------------------------------------------------------------------------------------------------------------------------------------------------

1 DC2 - 1 0.00 0.48 0.00 6.72 0.07

------------------------------------------------------------------------------------------------------------------------------------------------------
**Axial:**

**Pedestal** **Estado** **Pu**  ***Pn** **Pu/(**  ***Pn)**
**Zapata** [Kg] [Kg]

------------------------------------------------------------------------------------------------------------------

1 DC2 - 1 -19922.50 -107752.90 0.18

------------------------------------------------------------------------------------------------------------------
**Corte:**

**Pedestal 1:**
S adoptado : 30.00 [cm]
S calculado : 30.00 [cm]

**Estado** **Dir.** **Vu** **Vc** **Vs**  ***Vn** **Vu/(**  ***Vn)**

[Kg] [Kg] [Kg] [Kg]

-----------------------------------------------------------------------------------------------------------------------------------------------------

DC2 x 1042.66 6590.01 22774.70 22023.53 0.05

DC2 z 2155.63 6590.01 22774.70 22023.53 0.10

-----------------------------------------------------------------------------------------------------------------------------------------------------

**DIMENSIONES DE OBRAS TERRESTRES**

Para dimensionar la intervención a realizar en el sector playa, en relación a la cimentación de las
fundaciones requeridas para la instalación del puente basculante, se tomarán en cuenta las dimensiones
unitarias de las fundaciones calculadas, fusionándolas y uniéndolas mediante un muro pantalla, que
permita el apoyo rotulado del puente.
El sistema fundacional así descrito, permitiría una buena distribución de tensiones en el suelo de
fundación, bajo las admisibles; paralelamente, evitará el desplazamiento horizontal del apoyo, así como
la rotación de la zapata.
Las dimensiones de la excavación, con la holgura requerida para generar un área de obras adecuada, serán
de 1.5 m de profundidad, de 2.5 metros de ancho por 6.0 m de largo, en el fondo, considerándose un
talud de 3:2 (H:V), debido al tipo de material que podría tener desprendimientos durante el proceso

constructivo.

Las excavaciones consideran las dimensiones para dar cabida a las obras de hormigón armado, los
mejoramientos de suelo y emplantillados, bajo el sello de fundación y los sobreanchos necesarios para la
circulación de personal u la instalación de moldajes.

**APOYOS EXTREMOS DEL PUENTE BASCULANTE**

Los apoyos extremos del puente consistirán en elementos que representen los teorizados en la
modelación para su diseño; en el caso del apoyo rotulado del extremo en tierra, se diseñarán piezas de
acero que materialicen una bisagra que le permita a la estructura pivotear libremente sin desplazarse
horizontalmente. Para el caso del apoyo sobre el muelle flotante, la estructura deberá contar con un patín
metálico reforzado en cada viga del puente, que le permita deslizarse libremente en ambos sentidos por
la posibilidad de un movimiento lateral del muelle.