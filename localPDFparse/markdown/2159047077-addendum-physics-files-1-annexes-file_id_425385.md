---
title: Sin título
author: Juan Salazar León
date: D:20240311180232-03'00'
language: es
type: report
pages: 16
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - 22015-ID-ES-MC-01-B DISEÑO TRANQUE AGRÍCOLA ESTRELLA OBRA DE ENTREGA A RIEGO MEMORIA ESTRUCTURAL
-->

# 22015-ID-ES-MC-01-B DISEÑO TRANQUE AGRÍCOLA ESTRELLA OBRA DE ENTREGA A RIEGO MEMORIA ESTRUCTURAL

|ELABORÓ:|JSL|20-02-2024|REV.B|
|---|---|---|---|
|REVISÓ:|RVR|20-02-2024|REV.B|
|APROBÓ:|MRC|20-02-2024|REV.B|

**22015-ID-ES-MC-01-B**
**DISEÑO TRANQUE AGRÍCOLA ESTRELLA**

**OBRA DE ENTREGA A RIEGO**

**MEMORIA ESTRUCTURAL**

1. Introducción ................................................................................................................................ 3

2. Datos Geométricos de los Muros ................................................................................................ 3

3. Nomenclatura .............................................................................................................................. 4

4. Antecedentes............................................................................................................................... 5

4.1. Referencias............................................................................................................ 5

4.2. Antecedentes sísmicos .......................................................................................... 5

5. Condiciones de diseño ................................................................................................................. 5

6. Obra entrega a riego ................................................................................................................... 6

6.1. Verificación de las tuberías bajo el muro ............................................................. 6
6.2. Verificación de deformación horizontal (ovalamiento) ........................................ 6
6.3. Verificación de deformación vertical (condición de construcción) ...................... 8

6.4. Verificación al Pandeo del Manto de la Tubería ................................................... 9

6.5. Cálculo de cargas externas ..................................................................................10
6.6. Cargas de tráfico .................................................................................................11
6.7. Verificación flotación (condición de llenado) .....................................................12
6.8. Verificación deslizamiento (condición de vaciado) .............................................13

6.9. Verificación de la enfierraduras en las Cámaras .................................................14

7. Conclusiones ..............................................................................................................................16

22015-ID-ES-MC-01-B 2

**1.** **Introducción**

La presente memoria estructural corresponde al cálculo estructural del diseño de la obra de entrega
al sistema de riego del proyecto “ **Tranque Agrícola Estrella** ”.

El proyecto contempla la construcción de dos pretiles, los cuales se materializarán con rellenos
compactados provenientes del mismo entorno de las obras. El pretil principal, es una estructura de
13 m de altura ubicada al sur del sitio del embalse, este muro lleva en su parte inferior dos tuberías
de acero de D = 500mm. Estos ductos, permitirán distribuir los recursos de agua contenidos en el
embalse y ayudar a cubrir la demanda de riego según las necesidades del predio.

El pretil secundario cuya altura es de aproximadamente 8 m, construida de igual forma que el pretil
principal, cumple el objetivo de cerrar el vaso por el costado norte, permitiendo con esto lograr el
volumen de agua requerido de diseño.

La presente memoria de cálculo detalla las obras relacionadas a la obra de entrega a riego
emplazada en muro principal.

En la **¡Error! No se encuentra el origen de la referencia.** . se muestra el emplazamiento general del
proyecto del tranque Agrícola Estrella.

Figura 1.1 Planta general del proyecto.

**2.** **Datos Geométricos de los Muros**

A continuación, se presenta los datos geométricos de los muros de las presas que constituyen
relevantes en para el diseño estructural de las obras:

 - Cota de coronamiento: 143,00 m.s.n.m.

 - Altura del pretil principal (medido en el eje de la presa): 13,00 m.

 - Altura del pretil secundaria (medida en el eje de la presa): 8,00 m.

 - Taludes simétricos aguas arriba y aguas abajo: 2,5:1 (H:V).

 - Ancho de coronamiento de ambos pretiles: 4,50 m.

En la **¡Error! No se encuentra el origen de la referencia.** . se muestra el perfil transversal del pretil
principal donde se ubica la obra de entrega de riego.

22015-ID-ES-MC-01-B 3

Figura 2.1 Obras Pretil principal.

**3.** **Nomenclatura**

A continuación, se presentan los parámetros de entrada y salida utilizados en el desarrollo de la
presente memoria de cálculo, con una breve descripción de su significado. Las unidades empleadas
se verán reflejadas en los capítulos correspondientes, de acuerdo con la metodología empleada.

Cuadro 3.1. Nomenclatura general.

D m Diámetro medio de la tubería W T Carga total sobre la tubería (lineal)
r Radio de la tubería W m Carga muerta sobre la tubería (lineal)
r m Radio medio de la tubería W v Carga de uso sobre la tubería (lineal)

E Módulo de inercia de la tubería Q a Presión límite para la deformación

I t Momento de inercia de la tubería Q e Presión externa sobre la tubería

F' c Resistencia a la compresión del Δ x Deflexión horizontal de la tubería

h w Altura del agua (sobre la clave) Δ L Desplazamiento horizontal

γ s,sat Peso específico del relleno R w Coeficiente de flotación de la tubería

|Col1|Cuadro 3.1. No|
|---|---|
|De|Diámetro exterior de la tubería|
|Di|Diámetro interior de la tubería|
|Dm|Diámetro medio de la tubería|
|r|Radio de la tubería|
|rm|Radio medio de la tubería|
|e|Espesor de la tubería|
|E|Módulo de inercia de la tubería|
|It|Momento de inercia de la tubería|
|Im|Momento de inercia del manto de<br>la tubería|
|Fy|Fluencia del acero|
|F'c|Resistencia a la compresión del<br>hormigón|
|h|Altura del relleno (sobre la clave)|
|hw|Altura del agua (sobre la clave)|
|γs|Peso específico del relleno|
|γs,sat|Peso<br>específico<br>del<br>relleno<br>saturado|
|γw|Peso específico del agua|
|φ|Ángulo de fricción interna|

|σ<br>est|Tensión admisible estática|
|---|---|
|σdin|Tensión admisible dinámica|
|WT|Carga total sobre la tubería (lineal)|
|Wm|Carga muerta sobre la tubería (lineal)|
|Wv|Carga de uso sobre la tubería (lineal)|
|Qc|Presión crítica de pandeo|
|Qa|Presión límite para la deformación|
|Qe|Presión externa sobre la tubería|
|Qt|Presión por tráfico|
|QT|Presión total sobre la tubería|
|Δx|Deflexión horizontal de la tubería|
|Δy|Deflexión vertical de la tubería|
|ΔL|Desplazamiento<br>horizontal<br>longitudinal|
|FS|Factor de seguridad|
|Rw|Coeficiente de flotación de la tubería|
|K|Coeficiente de apoyo|
|k|Coeficiente de Rankine|

22015-ID-ES-MC-01-B 4

E' Módulo de resistencia del relleno a Coeficiente de expansión térmica

P t Peso de la tubería (lineal) B' Coeficiente empírico de soporte

|E'|Módulo de resistencia del relleno|
|---|---|
|B|Ancho de zanja|
|La|Longitud entre anclajes|
|α|Ángulo del talud|
|Pt|Peso de la tubería (lineal)|
|Ph|Peso del hormigón (lineal)|
|Pw|Peso del agua (lineal)|
|CD|Coeficiente de carga|

**4.** **Antecedentes**

|a|Coeficiente de expansión térmica|
|---|---|
|ΔT|Variación de temperatura|
|μ|Coeficiente de fricción interna|
|DL|Coeficiente de mayoración|
|B'|Coeficiente<br>empírico<br>de<br>soporte<br>elástico|
|If|Coeficiente de impacto|
|kh|Factor de sismo horizontal|
|Ka|Coeficiente de empuje activo|

Se presentan los antecedentes utilizados para el desarrollo de la presente memoria,
correspondientes a informes, guías de diseño y bibliografía afín.

**4.1.** **Referencias**

Ref. 1. Karl Terzaghi & Raph Peck, "Soil Mechanics in Engineering Practice". John Wiley & Sons,

1948.

Ref. 2. Calculo Estructural de Tuberías Enterradas. Etc., Daniel Gálvez Cruz, Tesis Doctoral

Universidad Politécnica de Madrid 2011.

Ref. 3. Concrete Culverts and Conduits PCA (Portland Cement Association) (1975).
Ref. 4. Guías de Diseño Estructural R GD-E01 ENDESA (1983).
Ref. 5. Norma AWWA M11 Pipe- A Guide for Design and Installation (1999).
Ref. 6. Estudios Básicos Geológico-Geotécnico 22015-EB-GEO-INF.01-A Tranque Estrella.

**4.2.** **Antecedentes sísmicos**

Según el estudio geotécnico de la Ref. 6. se utilizará un coeficiente horizontal: K h = 0,20.

**5.** **Condiciones de diseño**

Las tuberías de acero de entrega al riego se instalarán en zanjas, para este efecto el pretil principal
deberá estar debidamente compactado y recibido a la Cota: 132,00 m, cota desde donde se
comenzará a excavar para lograr la cota de apoyo de las tuberías.

Los rellenos entre las tuberías y en los contornos de estas con el talud de excavación, estarán
constituidos por arenas arcillosas con compactados por capas, hasta alcanzar una densidad
(D.M.C.S) del 95%, medida según el ensaye de Proctor Estándar.

Cuando las tuberías vayan dispuestas en terraplén, deberán quedar perfectamente apoyadas sobre
una capa preliminar (inferior) compactada y recibida, con un grado de compactación igual o
superiores al 95% de la densidad Proctor Modificado. En esta condición (de terraplén), los rellenos
laterales y hasta 1,0 m sobre la clave de la tubería, se ejecutarán usando un rodillo compactador
con un peso estático no superior a los 1.300 kg. Solo una vez recibidos estos rellenos se podrá
continuar con la utilización de equipos de mayor energía o peso, como los que se utilicen en los
rellenos masivos de la presa.

Cuando las tuberías se dispongan en zanjas, se deberán respetar las granulometrías y grado de
compactación de todas las capas de relleno, tal como se describen en las Especificaciones Técnicas
(ET) del proyecto.

22015-ID-ES-MC-01-B 5

**6.** **Obra entrega a riego**

Se verifican los elementos pertenecientes a la Obra de entrega a riego, correspondientes a la tubería
de acero enterrada, cámara de captación en hormigón armado y cámara de salida en hormigón
armado. Todos los elementos, según detalles presentados en los planos de proyecto.

**6.1.** **Verificación de las tuberías bajo el muro**

Debido a la configuración de la solución adoptada para la presa, las tuberías serán dispuestas sobre
los rellenos propios del pretil principal o cuerpo de la presa propiamente tal, que posterior a
excavación de la zanja donde quedarán alojadas ambas tuberías representan la condición de
“Instalación de tuberías en zanja”. De optarse por la solución de colocación tipo “Instalación de
tuberías en terraplén” los espesores de las tuberías deberán ser incrementados, justificados y
aprobados por la ITO.

La comprobación de la resistencia de la tubería se basa, por un lado, en la limitación de las
deformaciones diametrales horizontales del ducto, tomándose como criterio de diseño un máximo
de deformación horizontal del 5% de su diámetro. Esta limitación del ovalamiento, asegura que la
distribución de esfuerzos sobre la sección de tubería pueda seguir considerándose circular, sin
riesgo de una deformación mayor.

Por otro lado, las paredes de la tubería deberán ser verificadas al pandeo, dado el estado de
compresión predominante, resultante de la condición normal de carga sobre el vacío.

**6.2.** **Verificación de deformación horizontal (ovalamiento)**

Para el cálculo del ovalamiento se usará la fórmula de Iowa (Spangler M.G.1982), en su más reciente
formulación, este autor demostró que las fórmulas clásicas de Marston (método tradicional
utilizado para tuberías rígidas), no podían aplicarse en tuberías flexibles, como es el caso tratado.
En la **Figura 6.1** . se presenta un esquema de deformaciones para tuberías flexibles.

Figura 6.1. Esquema de deformaciones para una tubería flexible.

22015-ID-ES-MC-01-B 6

La formulación o método de cálculo mencionado, permite evaluar la deformación horizontal de un
ducto flexible mediante la siguiente expresión:

D L ∗K∗W∗r [3]
∆x máx =

E∗I+ (0.061 ∗E [′] ∗r [3] )

Donde:

D L : Coeficiente de mayoración, con valores que varían entre 1 a 2.
K: Constante que depende del apoyo de la tubería (k = 0,1).
W: Carga total sobre la tubería por metro lineal (kg/m).
r: Radio de tubería (m).
E: Módulo de inercia de la tubería (kg/m [2] ).
E’: Módulo de resistencia del suelo (kg/m [2] ).
I: Inercia de la pared (m [4] /m = m [3] ).

Para la definición del módulo **E’** se ocupará como referencia el **Cuadro 6.1** (Tabla de Howard), donde
se define los valores para cada uno de los tipos de relleno y grado de compactación de estos.

Cuadro 6.1. Valores de reacción del relleno para diferentes suelos y grados de compactación.

|Tabla de Howard - E' en kg/cm2|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|Tipo de Suelo|S/Comp.|Comp. Leve|Comp. Moderada|Comp. Alta|
|Tipo de Suelo|S/Comp.|<85% Proctor|85-95% Proctor|>95% Proctor|
|Tipo de Suelo|S/Comp.|<40% Dens. Rel.|40-70% Dens. Rel.|>70% Dens. Rel.|
|Suelo de granulometría fina (LL>50)<br>plasticidad media a alta|Este tipo de suelos requiere un análisis especial para determinar la densidad<br>requerida - contenido de humedad y compactación|Este tipo de suelos requiere un análisis especial para determinar la densidad<br>requerida - contenido de humedad y compactación|Este tipo de suelos requiere un análisis especial para determinar la densidad<br>requerida - contenido de humedad y compactación|Este tipo de suelos requiere un análisis especial para determinar la densidad<br>requerida - contenido de humedad y compactación|
|suelo finos de plasticidad nula a media<br>(LL<50) con menos de 25% de material<br>granular<br>CL, ML, ML-CL, CL-CH, ML-MH|3,4|13,8|27,6|69|
|Suelos de granulometría fina con<br>plasticidad nula a media (LL<50) con<br>más del 25% de material granular<br>ML, ML-CL, CL-CH, ML-MH.<br>Suelos de granulometría gruesa con más<br>de 12% de finos GM, GC, SM, SC|6,9|27,6|69|138|
|Suelos de granulometría gruesa con<br>menos del 12% de finos GW, GP, SW, SP|13,8|69|138|207|
|Roca repartida|69|207|207|207|
|Deflexión adicional (en % del diámetro)|±2%|±2%|±2%|±0,5%|

Para el cálculo de W se recurre a la Ecuación de Marston para el cálculo de las cargas debidas al

relleno.

El **Cuadro 6.2** . muestra los cálculos realizados para las condiciones de diseño de la tubería. La carga
sobre las tuberías se considera como la presión que transmitirá el relleno en forma íntegra, en la
condición más negativa (bajo el coronamiento de la presa), condición que está por el lado de la
seguridad dada la forma del relleno.

22015-ID-ES-MC-01-B 7

Cuadro 6.2. Cálculo de la deformación horizontal - Obra entrega a riego.

|D|0,5|m|Diámetro interno tubería<br>Espesor de la tubería<br>Diámetro exterior tubería<br>Radio de la tubería<br>Peso específico del relleno<br>Altura del relleno sobre la tubería<br>Coeficiente de mayoración (entre 1 y 2)<br>Carga total sobre la tubería (lineal)<br>Coeficiente de apoyo|
|---|---|---|---|
|e<br>De<br>r<br>γs<br>H<br>DL<br>WT<br>K|8<br>0,516<br>0,25<br>1,9<br>1,5<br>1<br>14,7<br>0,1|mm<br>m<br>m<br>ton/m3<br>m<br>kN/m|mm<br>m<br>m<br>ton/m3<br>m<br>kN/m|
|E|2,E+08|kN/m2|Módulo de inercia de la tubería<br>Módulo de resistencia del relleno|
|E'|6900|kN/m2|kN/m2|
|I|4,27E-08|m4/m|Momento de inercia|
|EI|8,96|||

|Δ<br>x|1,48|mm|Deflexión horizontal de la tubería|
|---|---|---|---|
|%Δx|0,30|%|Porcentaje de deformación; < 5,00%|

La deformación calculada es:

∆ máx = 0,30% < 5,00%

Condición que es satisfecha con una tubería de espesor comercial **e = 8 mm** .

**6.3.** **Verificación de deformación vertical (condición de construcción)**

La verificación de deformación vertical se realiza principalmente por las condiciones a las que estará
expuesta la tubería durante la etapa de construcción, ya que, durante la confección de los muros
(pretiles) y el montaje de la tubería, se debe compactar el terreno sobre ésta. Provocando así una
condición puntual a la que no volverá a estar expuesta en su etapa de servicio.

Para tales efectos, se limitará la carga máxima de rodillo compactador a 1300 kg durante los
primeros metros.

La verificación de los efectos de deformación vertical se realiza nuevamente mediante la teoría de

Spangler, mediante la siguiente expresión:

∆ máx = [(D] [L] [∗Q] [R] [+ Q] [T] [) ∗K]

2 ∗E

3 [+ 0,061 ∗E′]

3 ∗
~~(~~ [D] e

e [)]

Donde:

22015-ID-ES-MC-01-B 8

DL: Coeficiente de mayoración, con valores que varían entre 1 a 2.
QR: Carga vertical sobre la clave de la tubería (Marston) (kg/m).
QT: Carga correspondiente al tránsito (kg/m).
K: Constante que depende del apoyo de la tubería (k = 0,1).
D: Diámetro exterior de la tubería (m).
e: Espesor de la tubería (mm).
E: Módulo de inercia de la tubería (kg/m [2] ).
E’: Módulo de resistencia del suelo (kg/m [2] ).

**6.4.** **Verificación al Pandeo del Manto de la Tubería**

La condición de diseño debe satisfacer los siguientes requerimientos:

 - Esfuerzo de compresión deberá ser menor que 0,4 * Fy = 1.012 kg/cm [2] (donde Fy = 2.530
kg/cm [2], tensión de fluencia del Acero A36).

 - Factor de Seguridad **FS** será:

`o` 2,5 para h/D ≥ 2.
`o` 3,0 para h/D < 2.

Acorde a la Norma AWWA M11 (1999), el esfuerzo de compresión admisible (q a ) de pandeo en una
tubería enterrada, puede estimarse acorde a la siguiente expresión:

q a [1]
= (

D [3] [)]

[1]

FS [) ∗(32 ∗R] [w] [∗B] [′] [ ∗E] [′] [ ∗EI] D [3]

0,5

Donde:

q a : Presión admisible de pandeo.
FS: Coeficiente o factor de seguridad.
R w : Coeficiente de flotación de la tubería.

B’: Coeficiente de origen empírico del soporte elástico.

E’: Módulo de reacción del relleno.

EI: Rigidez de la pared del tubo.

E: Módulo de elasticidad del acero.

I: Momento de inercia del manto (espesor) por unidad de longitud de la tubería.

En el **Cuadro 6.3** . se presenta el cálculo de la carga crítica.

22015-ID-ES-MC-01-B 9

Cuadro 6.3. Cálculo de la carga crítica - Obra entrega a riego.

|FS|1|Col3|Coeficiente de seguridad (crítica)|
|---|---|---|---|
|EIm|2520|kN*m||
|B'|0,68||Coeficiente empírico de soporte elástico|
|RW|0,70||Coeficiente de flotación de la tubería|

|Q<br>c|43821,47|kN/m2|Presión crítica de pandeo|
|---|---|---|---|
|Qc|438,21|kg/cm2|kg/cm2|

El valor de E’ es el mismo que se adoptó para el cálculo de la deformación horizontal de la tubería y
para el cálculo del ovalamiento de la tubería.

Se verifica que:

q crítico
= 441,57 ( [kg]

⁄cm [2] ) < 0,4 ∗F y = 1.012 ( [kg]

⁄ 🗸 Cumple
cm [2] )

**6.5.** **Cálculo de cargas externas**

Para determinación de las cargas máximas sobre la tubería, se considera el embalse con su nivel de
agua en su cota máxima (142,00 m.s.n.m.), y la carga transmitida por el terreno a la tubería, justo
bajo el eje de la presa.

La expresión general es la siguiente:

q t = γ w ∗H w + f f ∗W e + W t + P v ( [ton] ⁄m [2] )

Donde:

γ w : Peso unitario del agua (ton/m [3] ).
H w : Altura de agua sobre la clave de la tubería (m).
f f : Coeficiente de flotación.
W e : Carga vertical debida al suelo (ton/m [3] ).
W t : Carga vertical debida al tráfico (ton/m [3] ).
P v : Carga vertical transiente (ton/m [3] ).

En el **Cuadro 6.4** . se presenta el cálculo de las cargas externas.

22015-ID-ES-MC-01-B 10

Cuadro 6.4. Cálculo de las cargas externas - Obra entrega a riego.

|R<br>w<br>W<br>e|0,70<br>21,85|ton/m2|Coeficiente de flotación<br>Carga vertical debida al suelo|
|---|---|---|---|
|qt<br>qt1|25,77<br>13,30|ton/m2<br>ton/m2|Carga distribuida sobre la tubería|
|qt<br>qt1|25,77<br>13,30|ton/m2<br>ton/m2|Carga lineal (1m)|

|Q<br>e|83,10|kg/cm2|Carga externa sobre la tuberia|
|---|---|---|---|
|FS|5,15||> 2,5|

**6.6.** **Cargas de tráfico**

Las cargas de tránsito se producen cuando la traza de la tubería se encuentra por debajo de una
calzada. La condición actual no presenta dicha situación, sin embargo, se realizará de manera
conservadora la verificación, ya que las condiciones de construcción generan una exigencia adicional

a la tubería.

La norma AWWA se basa para el análisis de las cargas de tránsito en la norma AASHTO.

En las tuberías de acero, las acciones del tráfico se calculan mediante la teoría de Boussinesq
(BOUSSINESQ, J.V. 1885), la cual se encuentra desarrollada de forma simplificada en la IET07 (2007).

La sobrecarga vertical que actúa sobre el plano de la generatriz superior de la tubería puede
calcularse mediante la expresión:

Q T = I f ∗C T ∗P r

Donde:

Q T : Carga vertical debido a las cargas de tráfico.
I f : Coeficiente de impacto (If = 1,5. AWWA).
C T : Coeficiente de carga por tráfico.
P r : Peso por rueda (carga directa).

Con:

H [)]]

C T = [3]

[∗[cos] [5] [ (atan2,25]
H [2] H

[3]

π [∗D] H

H [) + cos] [5] [ (atan0,45] H

Donde H corresponde a la altura de relleno sobre la clave de la tubería.

22015-ID-ES-MC-01-B 11

El Cuadro 6.5. muestra los cálculos realizados para la verificación de la deformación vertical,
considerando la Carga de tráfico.

**Cuadro 6.5. Cálculo de deformación vertical Δy - Obra entrega a riego.**

|De|516|mm|Diámetro exterior tubería|
|---|---|---|---|
|r|258|mm|Radio de la tubería|
|e|8|mm|Espesor de la tubería|
|h|11,50|m|Altura de relleno (sobre la clave)|
|B|1,00|m|Ancho de zanja|
|Pr|0|kg|Peso por rueda|
|γs|1900|kg/cm3|Peso específico del relleno|
|φ|28|°|Ángulo de fricción interna|
|E|14000|kg/cm2|Módulo de inercia de la tubería|
|E'|69|kg/cm2|Módulo resistente del relleno|
|K|0,1||Coeficiente de apoyo|
|μ|0,53||Coeficiente de fricción interna|
|k|0,36||Coeficiente de Rankine|
|k*μ|0,19||Coeficiente de carga|
|CD|2,57|||
|Wm|2522,71|kg/m|Carga muerta sobre la tubería (lineal)|
|CT|0,007||Coeficiente de carga por tránsito|
|If|1,5||Coeficiente de impacto (AWWA-AASHO)|
|Wv|0,00|kg/m|Carga de uso sobre la tubería (lineal)|
|DL|1,5||Coeficiente de mayoración (entre 1 a 2)|
|WT|2522,71|kg/m|Carga total sobre la tubería (lineal)|

|Δ<br>y|0,89|cm|Deformación vertical|
|---|---|---|---|
|%Δy|1,73|%|% Deformación|
|%Δy TOTAL|3,73|%|% Deformación total (Howard)|

**6.7.** **Verificación flotación (condición de llenado)**

Se verifica el efecto de flotación de la cámara de entrada debida al empuje vertical de la masa de
agua durante el proceso de llenado del tranque. Se asume el llenado parcial de la cámara de entrada
en el proceso.

Para garantizar que la estructura no flota, se verifica lo siguiente:

∑V1,3 [≥∑F] [flotantes] [ (Condición eventual)]

22015-ID-ES-MC-01-B 12

Donde, para condición eventual (llenado) se tiene:

∑V : Suma de fuerzas verticales que se oponen a la flotación.

∑F flotantes : Cargas de agua que favorecen a la flotación.

∑V = Volumen de hormigón de la cámara de entrada* 2,5 (t / m [3] )

∑V = 4,5 m3*2,5 t/m3 = 10,4 t.

∑F = Volumen desplazado hasta la cota 132,00 (parte inferior de la reja) = 7,5 m3 * 1,0 (t/m [3] )

∑F = 7,7 t.

Con lo anterior se obtiene un factor de seguridad a la flotación de:

FS = 10,4 t/7,7 t = 1,35 > 1,3 Por lo que cumple la condición de estabilidad para la condición

de llenado.

**6.8.** **Verificación deslizamiento (condición de vaciado)**

Se verifica el empuje horizontal del relleno de la ladera saturada sobre la cámara de salida, durante
el vaciado del tranque. Se asume cámara vacía.

Para evitar el deslizamiento horizontal de la cámara de salida, debida al empuje activo del suelo
saturado durante el vaciado, se verifica lo siguiente:

FR= [F] [roce]

FS roce

F c
+
FS cohesión

E
p
+
FS
pasivo

≥FD

Donde:

FR: Fuerza resistente total.

F roce : Fuerza de roce.
Fc: Resistencia generada por la cohesión (Fc = C * A).
Ep: Empuje pasivo.
Fp: Resistencia entregada por pernos de anclaje.

FD: Fuerza deslizante.

Cuadro 6.6. Factores de seguridad al deslizamiento.

|Factores de<br>Seguridad al<br>deslizamiento|Fuerza de Roce|Cohesión|Empuje pasivo|
|---|---|---|---|
|Condición normal|1,5|4,0|4,0|
|Condición eventual|1,3|3,0|3,0|

La fuerza deslizante sería la presión hidrostática por el trasdós del muro de respaldo.

Empuje = Υ suelo H [2] /2* L * Ka

Donde:

H : 0,6 Nivel del relleno tras la cámara de salida (m)
L : 2,8 Largo de la cámara de salida (m)
Empuje : 2,1 * 1,2 [2 ] / 2 * 2,82 * 0,27 = 1,15 (ton).

22015-ID-ES-MC-01-B 13

FR : Fuerza resistente (considerando solo en roce, suelo-hormigón).

Con fr: 0,4 como coeficiente de roce, se tiene:

FR = Peso de cámara de salida * fr = 6,7 t * 0,4 = 2,68 ton.
FS = FR / Empuje = 2,68 (ton) /1,15 = 2,34 > 1,3 Cumple condición de deslizamiento.

**6.9.** **Verificación de la enfierraduras en las Cámaras**

Las cámaras de mayor dimensión son las que se encuentran en la zona de entrada (sector inundado)
de los ductos. Esta normalmente funciona a presiones compensadas por su lado interior y exterior,
y debido a sus bajas solicitaciones estructurales, se verificarán para el esfuerzo mínimo de acero
que establece _REF. 6_ ( **¡Error! No se encuentra el origen de la referencia.** ) para las obras Tipo I (Obras
menores de riego):

Obras Tipo I: Cuantía mínima (uno por mil = 0,001), respecto de la sección considerada armadura
lo que resulta ser:

Acero mínimo: 2 cm [2] /m (para muros de 20x100 de sección transversal).

En la **Figura 6.2** . se presenta un esquema de la cámara.

Figura 6.2. Esquema de cámara.

En el **Cuadro 6.7** y el **Cuadro 6.8**, se presenta la verificación de la enfierradura de la cámara.

22015-ID-ES-MC-01-B 14

|γs|1,8|ton/m3|Peso específico del relleno<br>Peso específico del relleno saturado<br>Ángulo de fricción interna<br>Coeficiente empuje activo|
|---|---|---|---|
|γs,sat|2,1|ton/m3|ton/m3|
|φ|28|°|°|
|Ka|0,36|||

|Suelo|Col2|Agua|Col4|Col5|
|---|---|---|---|---|
||||||
|qΔ (ton/m)|1,36|1,36|1,80|1,80|
|K|2,09|2,09|2,75|2,75|

|Momentos|mi|Suelo Mi (ton*m)|Agua Mi (ton*m)|i= Ki mi q2 2 = qmáx q 2 = 0|
|---|---|---|---|---|
|Mxr|59,4|0,04|0,05|Borde 1 - 1 (libre superior)|
|Mxm|41,7|0,05|0,07||
|Mym|61,0|0,03|0,05||
|(-)Mer|-41,9|-0,05|-0,07|Apoyo superior en vano no apoyado|
|(-)Mem|-16,8|-0,12|-0,16|Borde 1 - 2 (ly)|
|(-)Mey|-14,6|-0,14|-0,19|Borde 2 - 2 (lx)|

|lx|1,7|m|Ancho<br>Alto<br>Suelo<br>Agua|
|---|---|---|---|
|ly|1,8|m|m|
|e = ly/lx|1,06|||
|Ka*γ*ly|1,36|ton/m2/m|ton/m2/m|
|γw*ly|1,8|ton/m2/m|ton/m2/m|
|b|100|cm||
|h|20|cm||
|r|4|cm|Recubrimiento|
|d (h-rec)|16|cm||
|Fy|4200|kg/cm2|Fluencia acero|
|Fc'|210|kg/cm2|Resistencia hormigón|
|As|2,51|cm2|Φ8@20|
|ρ|1,26|‰|Cuantía sección total|
|β|0,425||fc' < 280 kg/cm2|
|Mn|132939,3|kg*cm|Momento nominal|
|Mn|1,33|ton*m|Momento nominal|
|Φ*Mn|1,20|ton*m|Momento nominal reducido|

|Mu|-0,26|ton*m|Estado de carga: 1,4D + 1,4L|
|---|---|---|---|
|Mu|-0,38|ton*m|Estado de carga: 0,75(1,4F + 1,7H)|
|Mu < Φ*Mn|OK|OK|Verificación|

Cuadro 6.8. Verificación 2 enfierradura.

|γsuelo|1,8|ton/m3|Peso unitario del suelo|
|---|---|---|---|
|γsuelo saturado|2,1|ton/m3|Peso unitario del suelo saturado|
|φ|28|°|Ángulo de fricción|
|Ka|0,36||Coeficiente empuje activo|

|Suelo|Col2|Agua|Col4|Col5|
|---|---|---|---|---|
||||||
|qΔ (ton/m)|1,36|1,36|1,80|1,80|
|K|2,09|2,09|2,75|2,75|

|Momentos|mi|Suelo Mi (ton*m)|Agua Mi (ton*m)|i= Ki mi q2 2 = qmáx q 2 = 0|
|---|---|---|---|---|
|Mxr|59,4|0,04|0,05|Borde 1 - 1 (libre superior)|
|Mxm|41,7|0,05|0,07||
|Mym|61,0|0,03|0,05||
|(-)Mer|-41,9|-0,05|-0,07|Apoyo superior en vano no apoyado|
|(-)Mem|-16,8|-0,12|-0,16|Borde 1 - 2 (ly)|
|(-)Mey|-14,6|-0,14|-0,19|Borde 2 - 2 (lx)|

|lx|1,7|m|Ancho|
|---|---|---|---|
|ly|1,8|m|Alto|
|e = ly/lx|1,06|||
|Ka*γ*ly|1,36|ton/m2/m|Suelo|
|γw*ly|1,8|ton/m2/m|Agua|
|b|100|cm||
|h|20|cm||
|r|4|cm|Recubrimiento|
|d (h-rec)|16|cm||
|Fy|4200|kg/cm2|Fluencia acero|
|Fc'|210|kg/cm2|Resistencia hormigón|
|As|2,51|cm2|Φ8@20|
|ρ|1,26|‰|Cuantía sección total|
|β|0,425||fc' < 280 kg/cm2|
|Mn|132939,3|kg*cm|Momento nominal|
|Mn|1,33|ton*m|Momento nominal|
|Φ*Mn|1,20|ton*m|Momento nominal reducido|

|Mu|-0,26|ton*m|Estado de carga: 1,4D + 1,4L|
|---|---|---|---|
|Mu|-0,38|ton*m|Estado de carga: 0,75(1,4F + 1,7H)|
|Mu < Φ*Mn|OK|OK|Verificación|

Por tanto, los muros y los radieres deberán contar con armadura de: **Φ 8 a 20 (cm)** (en ambas caras),

en Acero A630-420H.

22015-ID-ES-MC-01-B 15

**7.** **Conclusiones**

De acuerdo con las verificaciones realizadas en 6.1, 6.2, 6.3, 6.4, 6.5 y 6.6 se adopta una tubería de
las siguientes características:

 - Diámetro Interior: 508mm.

 - Espesor: 9,53mm.

 - Tipo de Acero: A36.

Adicionalmente, por lo establecido en las verificaciones 6.7 y 6.8 **,** las cámaras de entrada y salida de
riego cumplen con las condiciones de diseño supuestas.

22015-ID-ES-MC-01-B 16

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 6.1.: Valores de reacción del relleno para diferentes suelos y grados de compactación.**

| Tabla de Howard - E' en kg/cm2 | Col2 | Col3 | Col4 | Col5 |
| --- | --- | --- | --- | --- |
| Tipo de Suelo | S/Comp. | Comp. Leve | Comp. Moderada | Comp. Alta |
| Tipo de Suelo | S/Comp. | <85% Proctor | 85-95% Proctor | >95% Proctor |
| Tipo de Suelo | S/Comp. | <40% Dens. Rel. | 40-70% Dens. Rel. | >70% Dens. Rel. |
| Suelo de granulometría fina (LL>50)<br>plasticidad media a alta | Este tipo de suelos requiere un análisis especial para determinar la densidad<br>requerida - contenido de humedad y compactación | Este tipo de suelos requiere un análisis especial para determinar la densidad<br>requerida - contenido de humedad y compactación | Este tipo de suelos requiere un análisis especial para determinar la densidad<br>requerida - contenido de humedad y compactación | Este tipo de suelos requiere un análisis especial para determinar la densidad<br>requerida - contenido de humedad y compactación |
| suelo finos de plasticidad nula a media<br>(LL<50) con menos de 25% de material<br>granular<br>CL, ML, ML-CL, CL-CH, ML-MH | 3,4 | 13,8 | 27,6 | 69 |
| Suelos de granulometría fina con<br>plasticidad nula a media (LL<50) con<br>más del 25% de material granular<br>ML, ML-CL, CL-CH, ML-MH.<br>Suelos de granulometría gruesa con más<br>de 12% de finos GM, GC, SM, SC | 6,9 | 27,6 | 69 | 138 |
| Suelos de granulometría gruesa con<br>menos del 12% de finos GW, GP, SW, SP | 13,8 | 69 | 138 | 207 |
| Roca repartida | 69 | 207 | 207 | 207 |
| Deflexión adicional (en % del diámetro) | ±2% | ±2% | ±2% | ±0,5% |

**Tabla 6.2.: Cálculo de la deformación horizontal - Obra entrega a riego.**

| D | 0,5 | m | Diámetro interno tubería<br>Espesor de la tubería<br>Diámetro exterior tubería<br>Radio de la tubería<br>Peso específico del relleno<br>Altura del relleno sobre la tubería<br>Coeficiente de mayoración (entre 1 y 2)<br>Carga total sobre la tubería (lineal)<br>Coeficiente de apoyo |
| --- | --- | --- | --- |
| e<br>De<br>r<br>γs<br>H<br>DL<br>WT<br>K | 8<br>0,516<br>0,25<br>1,9<br>1,5<br>1<br>14,7<br>0,1 | mm<br>m<br>m<br>ton/m3<br>m<br>kN/m | mm<br>m<br>m<br>ton/m3<br>m<br>kN/m |
| E | 2,E+08 | kN/m2 | Módulo de inercia de la tubería<br>Módulo de resistencia del relleno |
| E' | 6900 | kN/m2 | kN/m2 |
| I | 4,27E-08 | m4/m | Momento de inercia |
| EI | 8,96 |  |  |

**Tabla 6.3.: Cálculo de la carga crítica - Obra entrega a riego.**

| Q<br>c | 43821,47 | kN/m2 | Presión crítica de pandeo |
| --- | --- | --- | --- |
| Qc | 438,21 | kg/cm2 | kg/cm2 |

**Tabla 6.4.: Cálculo de las cargas externas - Obra entrega a riego.**

| Q<br>e | 83,10 | kg/cm2 | Carga externa sobre la tuberia |
| --- | --- | --- | --- |
| FS | 5,15 |  | > 2,5 |

**Tabla 6.5.: Cálculo de deformación vertical Δy - Obra entrega a riego.****

| De | 516 | mm | Diámetro exterior tubería |
| --- | --- | --- | --- |
| r | 258 | mm | Radio de la tubería |
| e | 8 | mm | Espesor de la tubería |
| h | 11,50 | m | Altura de relleno (sobre la clave) |
| B | 1,00 | m | Ancho de zanja |
| Pr | 0 | kg | Peso por rueda |
| γs | 1900 | kg/cm3 | Peso específico del relleno |
| φ | 28 | ° | Ángulo de fricción interna |
| E | 14000 | kg/cm2 | Módulo de inercia de la tubería |
| E' | 69 | kg/cm2 | Módulo resistente del relleno |
| K | 0,1 |  | Coeficiente de apoyo |
| μ | 0,53 |  | Coeficiente de fricción interna |
| k | 0,36 |  | Coeficiente de Rankine |
| k*μ | 0,19 |  | Coeficiente de carga |
| CD | 2,57 |  |  |
| Wm | 2522,71 | kg/m | Carga muerta sobre la tubería (lineal) |
| CT | 0,007 |  | Coeficiente de carga por tránsito |
| If | 1,5 |  | Coeficiente de impacto (AWWA-AASHO) |
| Wv | 0,00 | kg/m | Carga de uso sobre la tubería (lineal) |
| DL | 1,5 |  | Coeficiente de mayoración (entre 1 a 2) |
| WT | 2522,71 | kg/m | Carga total sobre la tubería (lineal) |

**Tabla 6.6.: Factores de seguridad al deslizamiento.**

| Factores de<br>Seguridad al<br>deslizamiento | Fuerza de Roce | Cohesión | Empuje pasivo |
| --- | --- | --- | --- |
| Condición normal | 1,5 | 4,0 | 4,0 |
| Condición eventual | 1,3 | 3,0 | 3,0 |

**Tabla 6.8.: Verificación 2 enfierradura.**

| Suelo | Col2 | Agua | Col4 | Col5 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
| qΔ (ton/m) | 1,36 | 1,36 | 1,80 | 1,80 |
| K | 2,09 | 2,09 | 2,75 | 2,75 |
