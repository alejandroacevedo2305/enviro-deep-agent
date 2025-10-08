---
title: Sin título
author: Matías Sebastián Pêllet Alveal
date: D:20210924120433-03'00'
language: es
type: report
pages: 23
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ρ=
  - q∗B∗(1 −υ [2] ) ∗Ι
  - Ε
-->

#### Septiembre 2021

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

e-mail: hringenieria@hringenieria.cl 0

#### _INDICE_

1. INTRODUCCION ....................................................................................... `3`

2. ANTECEDENTES PARA EL DESARROLLO DEL ESTUDIO .................... `3`

3. ANTECEDENTES DE MECÁNICA DE SUELOS ....................................... `4`

_3.1._ _Exploración del subsuelo ....................................................................._ _`4`_

_3.2._ _Perfil estratigráfico ..............................................................................._ _`6`_

_3.3_ _Presencia de Napa Freática ................................................................._ _`6`_

4. PARÁMETROS PARA EL DISEÑO DE FUNDACIONES .......................... `7`

_4.1._ _Nivel de Sello de Fundación ................................................................_ _`7`_

_4.2._ _Tensiones de contacto admisibles ......................................................._ _`7`_

_4.3._ _Parámetros Geotécnicos de Diseño ...................................................._ _`7`_

_4.4._ _Consideraciones NCh. 2369 Mod.2003 ..............................................._ _`8`_

_4.5._ _Constante de Balasto .........................................................................._ _`8`_

_4.6._ _Estimación de Asentamientos ............................................................._ _`9`_

5. EMPUJES DE SUELO ............................................................................. `10`

_5.1_ _Muros no arriostrados en extremo superior .........................................._ _`10`_

_5.2_ _Muros arriostrados en extremo superior (subterráneos) ......................._ _`13`_

6. ESPECIFICACIONES TÉCNICAS CONSTRUCTIVAS GENERALES ..... `15`

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

1
e-mail: hringenieria@hringenieria.cl

_**INDICE DE TABLAS**_

_Tabla 1: Detalle Emplazamiento Calicatas ....................................................................................... 4_
_Tabla 2: Perfil Estratigráfico Predominante ...................................................................................... 6_
_Tabla 3: Tensiones de Contacto Admisibles .................................................................................... 7_

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |---|---|---|---| |Estrato de Fundación|Estrato de Fundación|Estático|Sísmico| |1|Arcilla Arenosa|1.10|1.40| |2|Arena Arcillosa|2.10|2.70| -->

**Tabla 3: Tensiones de Contacto Admisibles****

| Parámetros Geotécnicos de Diseño | Estrato de Fundación | Col3 |
| --- | --- | --- |
| **Parámetros Geotécnicos de Diseño** | **Arcilla**<br>**Arenosa** | **Arena Arcillosa** |
| Clasificación USCS | CL | SC |
| Cohesión_C _[T/m2] | 1.00 | 1.00 |
| Angulo de Fricción [°] | 26 | 36 |
| Peso Específico [t/m3] | 1.50 | 1.70 |
| Peso Específico Saturado [t/m3] | 1.70 | 1.90 |
| Módulo de Elasticidad_E _[T/m2] | 1000 | 2500 |
| Módulo de Elasticidad Cíclico_Ed_[T/m2] | 3000 | 7500 |

<!-- Estadísticas: 8 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 4: Parámetros Geotécnicos de Diseño.** Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790. -->
<!-- FIN TABLA 3 -->


_Tabla 4: Parámetros Geotécnicos de Diseño. .................................................................................. 7_

_Tabla 5: Constante de Balasto ........................................................................................................ 8_
_Tabla 6: Factores de forma para zapatas rígidas ............................................................................. 9_

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |L/B|1.0|1.5|2.0|5.0|10| |---|---|---|---|---|---| |I|0.82|1.06|1.20|1.70|2.10| -->

**Tabla 6: Factores de forma para zapatas rígidas.****

| L/B | 1.0 | 1.5 | 2.0 | 5.0 | 10 |
| --- | --- | --- | --- | --- | --- |
| Ir | 0.95 | 1.15 | 1.30 | 1.83 | 2.25 |

<!-- Estadísticas: 1 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- **Tabla 7: Factores de forma para zapatas flexibles.** Para el cálculo de los asentamientos de una zapata de ancho B, se debe considerar el módulo de deformación a una profundidad B bajo el sello de fundación. -->
<!-- FIN TABLA 6 -->

_Tabla 7: Factores de forma para zapatas flexibles ........................................................................... 9_
_Tabla 8: Parámetros para la determinación de empujes .................................................................. 10_
_Tabla 9: Taludes Recomendados .................................................................................................. 15_
_Tabla 10: Estratigrafía Calicata N°1 -El Portal- Bocatoma. ............................................................ 18_
_Tabla 11: Estratigrafía Calicata N°2 - El Portal - Tubería en Presión ............................................ 19_
_Tabla 12: Estratigrafía Calicata N°3 - El Portal - Casa de Máquinas ............................................. 20_

_**INDICE DE FOTOGRAFÍAS**_

_Fotografía N° 1: Calicata N°1 - El Portal - Camara de Carga. ....................................................... 21_
_Fotografía N° 2: Calicata N°2 - El Portal - Tubería en Presión. ..................................................... 22_
_Fotografía N° 3: Calicata N°3 - El Portal -Bocatoma ..................................................................... 23_

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

2
e-mail: hringenieria@hringenieria.cl

**1.** **INTRODUCCION**

Con motivo de llevar a cabo el diseño estructural y la posterior construcción de las
obras “Bocatoma”, “Tubería en Presión” y “Casa de Máquinas” de la Central Hidroeléctrica
“El Portal”, emplazada a las afueras de la localidad de Mulchén, VIII Región del Bío-Bío, se
ha encargado al suscrito la elaboración del presente Informe de Mecánica de Suelos.

El estudio que se presenta en este informe incluye entre otros aspectos los
resultados de la exploración del subsuelo realizada en terreno, de los cuales se pueden
obtener los siguientes antecedentes:

 Estratigrafía del subsuelo.

 Presencia de napa freática.

 Propiedades geo mecánicas.

 Clasificación de tipo de suelo según normas sísmicas oficiales.

 - Profundidad mínima del sello de fundación.

 - Tensiones de contacto admisibles de contacto normal y eventual.

 - Coeficientes de balasto.

 - Taludes de Corte.

 - Recomendaciones constructivas generales.

**2.** **ANTECEDENTES PARA EL DESARROLLO DEL ESTUDIO**

En la preparación de este informe se han considerado los antecedentes siguientes:

A) Visitas a terreno y exploración geotécnica realizada por personal de esta

oficina en mayo 2020.

B) Antecedentes del proyecto proporcionados por el mandante Sr. Alberto

Treknais (HLT ENERGIA Spa).

C) Bases Técnicas Mecánica de Suelos, N°146003-BT-01, “HLT ENERGÍAProyecto Hidroeléctrico Centrales El Portal, La Bifurcada, El Brinco, Alto La
Viña, La Viña, Chumulco y Pitraco - Ingeniería de Detalles” Rev. B emitido
por EIC Ingenieros Consultores (24/11/2014).

D) Ensayos de laboratorio certificados por IOC Ingeniería (N° 1.401) realizados

para proyectos La viña y La Bifurcada.

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

3
e-mail: hringenieria@hringenieria.cl

**3.** **ANTECEDENTES DE MECÁNICA DE SUELOS**

**3.1.** **Exploración del subsuelo**

La exploración del sub suelo consistió en la ejecución de 3 calicatas [1], emplazadas
en las áreas donde se proyecta la construcción de las obras “Bocatoma”, “Tubería en
Presión” y “Casa de Máquinas”, sus profundidades alcanzaron los 6.00m, 3.00m y 3.00m
respectivamente.

De acuerdo a la conformación del subsuelo se obtuvieron muestras alteradas e
inalteradas las cuales permiten definir la similitud del subsuelo encontrado en los programas
de ensayos de laboratorio anteriores realizados para proyecto la Viña y la Bifurcada, los
cuales fueron certificados por IOC Ingeniería.

En la Tabla 1 se detalla la denominación, profundidad y coordenadas de cada una
de las calicatas realizadas.

|TABLA 1: Emplazamiento Calicatas - "Central Hidroeléctrica El<br>Portal”|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|Denominación|Profundidad (m)|Coordenadas|Coordenadas|Obra|
|Denominación|Profundidad (m)|Norte (m)|Este (m)|Este (m)|
|_El Portal C1_|_3.00_|_5.823.883_|_754.562_|Casa de Maquinas|
|_El Portal C2_|_3.00_|_5.823.814_|_754.707_|Tubería en presión|
|_El Portal C3_|_6.00_|_5.823.723_|_755.205_|Bocatoma|

**Tabla 1: Detalle Emplazamiento Calicatas.**

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

4
e-mail: hringenieria@hringenieria.cl

La Imagen N° 1, describe el emplazamiento de las calicatas ejecutadas.

**Imagen N° 1: Emplazamiento de Calicatas.**

La Imagen N°2 muestra en perspectiva el emplazamiento de las calicatas y la cercanía con
los proyectos mencionados anteriormente

**Imagen N°2: Emplazamiento proyecto**

1 Emplazamiento y profundidad de calicatas definido por el mandante.

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

5
e-mail: hringenieria@hringenieria.cl

**3.2.** **Perfil estratigráfico**

De acuerdo a la exploración geotécnica realizada, el sub suelo del sector, se
caracteriza por la existencia de un perfil estratigráfico **predominante**, compuesto por las
siguientes unidades:

|"Central Hidroeléctrica El Portal - Bocatoma, Tubería en Presión y Casa de Maquinas "|Col2|Col3|Col4|
|---|---|---|---|
|**Unidad**|**Profundidad (m)**|**Profundidad (m)**|**Descripción**<br>**Tipo de Suelo**|
|**Unidad**|Desde|Hasta|Hasta|
|U - 1|0.00|0.15|**Cubierta Vegetal.**|
|U - 2|0.15|1.80 a 4.50|**Arcilla Arenosa.**Color café, humedad media, estructura<br>homogénea, plasticidad media, consistencia media a alta. Se<br>observa la presencia de raíces, raicillas y gravas aisladas de<br>forma redondeada con tamaño máximo 8” y una media de 2<br>1⁄2“. Estrato de suelo natural que clasifica como CL según<br>USCS.|
|U - 3|1.80 a 4.50|6.00|**Arena Arcillosa,**localmente denominada “Maicillo”, color café<br>amarillento, humedad alta, dureza media. Estrato de suelo<br>natural que clasifica como SC según USCS.|
|**Obs.:**|Se observa la presencia de napa freática a una profundidad variable entre 4.00 m<br>y 5.30m.|Se observa la presencia de napa freática a una profundidad variable entre 4.00 m<br>y 5.30m.|Se observa la presencia de napa freática a una profundidad variable entre 4.00 m<br>y 5.30m.|

**Tabla 2: Perfil Estratigráfico Predominante**

**3.3** **Presencia de Napa Freática**

En cuanto a la presencia de napa freática, ésta fue detectada dentro de las
profundidades reconocidas en la fecha de exploración (mayo 2020).

 - Bocatoma : 2.80m

 - Tubería en Presión : 2.60m

 - Casa de Máquinas : 5.30m

Nota: Se desconoce su variación estacional y en el tiempo, antecedente que escapa a

esta especialidad.

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

6
e-mail: hringenieria@hringenieria.cl

~~**4.**~~ ~~**PARÁMETROS PARA EL**~~
**DISEÑO DE FUNDACIONES**

**4.1.** **Nivel de Sello de Fundación**

El nivel del sello de fundación quedará en función de las cotas definitivas dadas por
el proyecto hidráulico. Considerando la envergadura de las obras y la sección típica de las
mismas, se puede estimar que el sello de fundación corresponderá a uno de los siguientes
estratos:

Arcilla Arenosa: (CL - Según USCS) _(Profundidad Mínima 1.00m)_

Maicillo : (SC - Según USCS) _(Profundidad Mínima 1.90m - 4.60m)_

**4.2.** **Tensiones de contacto admisibles**

Acorde a la experiencia de esta oficina en este tipo de suelo, se recomiendan las
siguientes tensiones admisibles para cada uno de los posibles estratos de fundación:

|Estrato de Fundación|Col2|Q [kg/cm2]<br>adm|Col4|
|---|---|---|---|
|Estrato de Fundación|Estrato de Fundación|Estático|Sísmico|
|1|Arcilla Arenosa|1.10|1.40|
|2|Arena Arcillosa|2.10|2.70|

**Tabla 3: Tensiones de Contacto Admisibles**

**4.3.** **Parámetros Geotécnicos de Diseño**

Con la finalidad de ejecutar el diseño de las obras consideradas en la ejecución de
este proyecto, se adjunta un resumen con los parámetros geotécnicos estimados del
subsuelo según los estratos y condiciones identificados en la exploración geotécnica.

|Parámetros Geotécnicos de Diseño|Estrato de Fundación|Col3|
|---|---|---|
|**Parámetros Geotécnicos de Diseño**|**Arcilla**<br>**Arenosa**|**Arena Arcillosa**|
|Clasificación USCS|CL|SC|
|Cohesión_C _[T/m2]|1.00|1.00|
|Angulo de Fricción [°]|26|36|
|Peso Específico [t/m3]|1.50|1.70|
|Peso Específico Saturado [t/m3]|1.70|1.90|
|Módulo de Elasticidad_E _[T/m2]|1000|2500|
|Módulo de Elasticidad Cíclico_Ed_[T/m2]|3000|7500|

**Tabla 4: Parámetros Geotécnicos de Diseño.**

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

7
e-mail: hringenieria@hringenieria.cl

**4.4.** **Consideraciones NCh. 2369 Mod.2003.**

Para los efectos de aplicar la norma de diseño sísmico de edificios, se deberá
considerar lo siguiente:

Tipo de Suelo: III
Zona Sísmica: 2

**4.5.** **Constante de Balasto**

Con el objeto de determinar los asentamientos de las fundaciones, se deberá
considerar la siguiente expresión para determinar la constante de balasto (Placa de
30x30cm):

##### _E_ k =
#### (1 −  2

_p_

2
##### )· B · I

Donde:

E = Según Tabla 4, módulo de deformación del suelo
 = 0,3 (módulo de Poisson)
B = 0,3 (m) Ancho de Placa de carga
I = 0,88

Mediante la expresión anterior el valor para la constante de balasto, son los
siguientes:

|Estrato de Fundación|Col2|K<br>30<br>[kg/cm3]|
|---|---|---|
|Estrato de Fundación|Estrato de Fundación|Estático|
|1|Arcilla Arenosa|4.00|
|**2 **|Arena Arcillosa|10.00|

**Tabla 5: Constante de Balasto**

Para zapatas de ancho B (m), usar la siguiente expresión:

K (B) = **K** **30** *0,3/B

Para zapatas corridas de dimensiones B/L, usar la siguiente expresión:

K (B/L) = K (B)*2/3*(1+ (B/2L))

*Para solicitaciones sísmicas multiplicar por 3 el valor de la constante de Balasto.

*Para estimar la constante de balasto al giro se debe multiplicar este valor por 2,5.

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

8
e-mail: hringenieria@hringenieria.cl

**4.6.** **Estimación de Asentamientos**

Para calcular los asentamientos sobre el estrato portante se utilizó la teoría de la
Elasticidad, en la siguiente expresión:

# ρ=

# q∗B∗(1 −υ [2] ) ∗Ι
### ρ

# Ε
### s

Donde:

: Asentamientos instantáneos (m)
q: Presión de contacto (t/m2)
B: Ancho mínimo de la fundación, (m)
E S : Módulo de deformación (t/m2)
: Módulo de Poisson
I  : Factor de forma

|L/B|1.0|1.5|2.0|5.0|10|
|---|---|---|---|---|---|
|I|0.82|1.06|1.20|1.70|2.10|

**Tabla 6: Factores de forma para zapatas rígidas.**

|L/B|1.0|1.5|2.0|5.0|10|
|---|---|---|---|---|---|
|Ir|0.95|1.15|1.30|1.83|2.25|

**Tabla 7: Factores de forma para zapatas flexibles.**

Para el cálculo de los asentamientos de una zapata de ancho B, se debe considerar el
módulo de deformación a una profundidad B bajo el sello de fundación.

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

9
e-mail: hringenieria@hringenieria.cl

**5.** **EMPUJES DE SUELO**

La determinación de empujes y su variabilidad según el estrato que está actuando
se determinara según los apartados 5.1 y 5.2 según sea el caso y se deberán considerar
los siguientes parámetros:

|Estrato|Arcilla Arenosa<br>(U - 2)|Arena Arcillosa<br>(U - 3)|
|---|---|---|
|_Empuje Activo (Ka)_|0,390|0,260|
|_Empuje Sísmico (Ks)_|0,109|0,087|
|_Empuje Estático (Ko)_|0,560|0,410|
|_Empuje Pasivo (Kp)_|2,561|3,852|

**Tabla 8: Parámetros para la determinación de empujes.**

Los empujes de suelo se deberán calcular siguiendo las expresiones que se
desarrollan en los puntos siguientes, caso napa freática.

**5.1** **Muros no arriostrados en extremo superior**

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

10
e-mail: hringenieria@hringenieria.cl

**5.1.1** **Empuje Estático**

**Se define:**

Coeficiente de empuje activo _K_ _a_ = (según tabla 6)
Presión activa ( _Z_ ) σ 0 =  [] - _K_ _a_ _·_ Z
Sobre Carga σ q = _K_ _a_ _· q_
Napa Freática (sólo caso _Z > Dw_ ) σ nf =   - ( _Z - Dw)_

 [] =  h para _Z < Dw_ (caso sin napa)

 [] =  sat - 1 para _Z ≥ Dw_ (caso con napa)

Donde:

_K_ _a_ = Coeficiente de empuje activo.
_Z_ = Profundidad a la que se evalúa el empuje.
_q_ _=_ Sobrecarga.
 h = Peso unitario húmedo del material.

 sat = Peso unitario saturado del material.
 w = Peso unitario del agua.
_Dw_ = Profundidad a la que aparece la napa freática.

_K_ _a_
_Z_

_q_

 h

=

=

_=_

=

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

11
e-mail: hringenieria@hringenieria.cl

**5.1.2. Empuje Pasivo**

El empuje pasivo a considerar en la zona enterrada de los muros de contención se
calculará de acuerdo a la siguiente formulación:

Coeficiente de empuje pasivo
_K_ _p_ = (según tabla 6)

 [] =  h para _Z < Dw_ (caso sin napa)

 [] =  sat - 1 para _Z ≥ Dw_ (caso con napa)

Donde:

_K_ _p_ = Coeficiente de empuje pasivo.
_Z ́_ = Profundidad a la que se evalúa el empuje.
 h = Peso unitario húmedo del material.
 sat = Peso unitario saturado del material.

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

12
e-mail: hringenieria@hringenieria.cl

**5.2** **Muros arriostrados en extremo superior (subterráneos)**

Los empujes laterales que actuarán sobre las obras tendrán las siguientes
magnitudes. Todos los valores que se entregan son por unidad de longitud.

**5.2.1. Empuje Estático**

Coeficiente de empuje estático _K_ _0_ = (según tabla 6)
Presión en reposo ( _Z_ ) σ 0 =  [] - _K_ _0_ _·_ Z
Sobre Carga σ q = _K_ _0_ _· q_
Napa Freática (sólo caso _Z > Dw_ ) σ nf =   - ( _Z - Dw)_

 [] =  h para _Z < Dw_ (caso sin napa)

 [] =  sat - 1 para _Z ≥ Dw_ (caso con napa)

Donde:

_K_ _0_ = Coeficiente de empuje estático.
_Z_ = Profundidad a la que se evalúa el empuje.
_q_ _=_ Sobrecarga.
 h = Peso unitario húmedo del material.

 sat = Peso unitario saturado del material.
 w = Peso unitario del agua.
_Dw_ = Profundidad a la que aparece la napa freática.

_K_ _0_
_Z_

_q_

 h

=

=

_=_

=

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

13
e-mail: hringenieria@hringenieria.cl

**5.2.2 Empuje Sísmico**

De acuerdo a la Norma NCh 433 Of.96.mod2009, la componente sísmica del empuje
de suelos para muros subterráneos arriostrados superiormente se deberá evaluar con la
siguiente expresión:

#### σ s = 0.30 · Cr ·  [] ·  ·    g [Ton/m [2] ]  [] =  h Caso sin napa.  sat - Dw ( sat -  h )  [] = -------------- Caso con napa, en que H > Dw H Donde: σ s = Presión sísmica. H = Altura del muro.  h = Peso unitario húmedo del material. sat = Peso unitario saturado del material.  0 = Aceleración efectiva (0.30g, Zona sísmica 2). C r = 0.50.

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

14
e-mail: hringenieria@hringenieria.cl

**6.** **POTENCIAL DE LICUEFACCIÓN**

Según lo indicado por el método de Seed - Idriss, el potencial de licuefacción se evalúa
según el factor de seguridad obtenido de la siguiente expresión:

0.8S u MSF∗Cr

FS= [CRR]

CSR [=]

σ EFF

d [0.65σ] [TOTAL] [a] [max]
(r σ EFF ∙g ~~)~~

Donde:

rd: factor de reducción por profundidad (1.0 superficial, 0.9 a 10 metros)
a_max: aceleración sísmica máxima (0.3g según zona sísmica)
σ TOTAL : tensión total [kg/m2]
σ EFF: tensión efectiva [kg/m2]
Su: Resistencia al corte suelo cohesivo (Suelo tipo III) [kg/m2]

MSF: Coeficiente por el sismo evaluado ( MSF=

10 [2.24]

MSF: Coeficiente por el sismo evaluado ( MSF= [) ]

MW [2.56]
Cr: Coeficiente de reducción por densidad relativa (75% = 0.6)

Las tensiones se calculan como:

σ TOTAL : γ d (z−h) + (γ Sat h)
σ EFF : γ d (z−h) + h(γ Sat −γ w )

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

15
e-mail: hringenieria@hringenieria.cl

Donde:

γ d : peso específico terreno [kg/m3]
γ sat: peso específico terreno saturado [kg/m3]
γ w: peso específico del agua [kg/m3]
z: nivel del terreno hasta el punto de aplicación
h: nivel del agua hasta el punto de aplicación

Cabe señalar, que el factor de seguridad debe ser mayor a 1 para no tener potencial de
licuefacción.

Considerando lo anterior y evaluando el potencial de licuefacción al nivel de la fundación de
las obras, al nivel de la losa de fundación, tenemos el siguiente esquema:

Donde observa que a nivel de sello de fundación no actúa la napa freática, por lo que la
columna de agua no se considera en el análisis.

Como resumen los resultados en la siguiente tabla:

|Parámetro|Valor|Unidad|
|---|---|---|
|σTOTAL|2295|Kg/m2|
|σEFF|2295|Kg/m2|
|rd|1|Adim (conservador)|
|Su|0.025|MPa (conservador)|
|MSF|0,62|Adim (sismo grado 9)|
|Z|1,53|m|
|**Factor de seguridad FS**|**1,71**||

Resultando una no potencial licuefacción de las obras frente a un sismo de grado 9 en la zona
de Mulchén.

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

16
e-mail: hringenieria@hringenieria.cl

**7.** **ESPECIFICACIONES TÉCNICAS CONSTRUCTIVAS GENERALES**

 - Método de excavación

1.- Las faenas de excavación se podrán realizar en forma mecanizada, sin

embargo, se recomienda que los últimos 20cm se excaven manualmente
con el objeto de evitar tanto la perturbación del suelo natural como la
sobre-excavación.

2.- Las excavaciones se deben efectuar de acuerdo a las dimensiones y

emplazamiento indicados en los planos del proyecto y de acuerdo con las
recomendaciones dadas precedentemente. Las excavaciones deberán
ser recibidas por la ITO en cuanto a sus emplazamientos.

 - Tratamiento de la sobre-excavación

3.- Cualquier sobre-excavación que se produzca podrá ser rellenada con

hormigón pobre de 2 sacos de cemento por metro cúbico.

 - Taludes de Excavación

4.- Independiente del tipo de suelo, se considerará un talud vertical para todas

las excavaciones menores a 1,50 [m]. Para excavaciones más profundas
considerar:

|Estrato|Talud Corte|Col3|
|---|---|---|
|**Estrato**|~~Construcción~~|~~Permanente~~|
|Arcilla Arenosa|1H:3V|1H:2V|
|Arena Arcillosa|1H:3V|1H:2V|

**Tabla 9: Taludes Recomendados.**

Los taludes antes mencionados están limitados a una altura de
excavación de 4m. En caso de excavaciones más profundas se
deberán generar bermas de 1m a la mitad de la altura en corte.

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

17
e-mail: hringenieria@hringenieria.cl

 - Tratamiento del Sello

5.- Con anterioridad a la colocación del emplantillado de hormigón pobre, se
deberá remover del sello de fundación todo material suelto y/o extraño
que pudiera haberse depositado durante las faenas de excavación. **No se**
**requiere re compactar el sello de fundación.**

6.- Los sellos de fundación deberán ser recibidos por la I

 - Protección en caso de lluvias

7.- En caso de lluvias, antes de continuar con los rellenos y compactación
se deberá remover de la superficie todo el lodo superficial, producto del
arrastre natural de partículas como consecuencia del escurrimiento
superficial.

 - Rellenos laterales

8.- La reposición del material excavado a los costados de la excavación, se
deberá compactar por capas hasta alcanzar una densidad no inferior a
un 90 % del ensayo Proctor Modificado o una Densidad relativa de 75%.
El espesor de las capas dependerá del equipo de compactación que se
utilice, pero se deberá cumplir siempre con la densidad antes indicada.
De todas formas, se recomienda compactación liviana para no cargar en
exceso los muros de las estructuras colindantes.

Se podrá contemplar la reutilización del material definido como U-3 en
3.2 para lo confección de rellenos no estructurales. Rellenos estructurales
deberán considerar el empleo de material del tipo estabilizado.

9.- El avance de las capas de relleno debe ser parejo, de manera que no se
produzcan desniveles superiores a 0,50 [m] entre sectores contiguos.

Cualquier situación no prevista en el presente informe, así como modificaciones que se
deseará realizar en su contenido, deberá ser consultada y aprobada por el suscrito.

________________________
**Herbert Rowlands Jimeno**

**Ingeniero Civil**

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

18
e-mail: hringenieria@hringenieria.cl

## ANEXO A ESTRATIGRAFIA ANEXO B FOTOGRAFIAS

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

19
e-mail: hringenieria@hringenieria.cl

**Fotografía N° 1: Calicata N°1 - El Portal - Casa de Maquinas.**

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

20
e-mail: hringenieria@hringenieria.cl

**Fotografía N° 2: Calicata N°2 - El Portal - Tubería en Presión.**

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

21
e-mail: hringenieria@hringenieria.cl

**Fotografía N° 3: Calicata N°3 - El Portal -Bocatoma.**

Miguel Claro 922 - Providencia. Fono: +56 (02) 26119790.

22
e-mail: hringenieria@hringenieria.cl