---
title: SOCIEDAD CHILENA DE INGENIERIA HIDRAULICA
author: sochid.cl
date: D:20031023105708Z
language: es
type: manual
pages: 11
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ∫
-->

SOCIEDAD CHILENA DE INGENIERÍA HIDRÁULICA
XVI CONGRESO CHILENO DE INGENIERÍA HIDRÁULICA

##### USO “RACIONAL” DE LA FORMULA RACIONAL

LUDWIG STÖWHAS B.
Departamento Obras Civiles, Universidad Técnica Federico Santa María, Casilla 110V, Valparaíso, lstowhas@ociv.utfsm.cl

**RESUMEN**

Se analiza en forma teórica la respuesta de una cuenca bajo el enfoque de la
Fórmula Racional, proponiéndose expresiones analíticas para una estimación más objetiva
del coeficiente de escorrentía, en función de la magnitud de la precipitación, el tiempo de
concentración de la cuenca y la tasa de abstracción o infiltración. Las expresiones
propuestas se cotejan favorablemente con resultados y coeficientes obtenidos en forma
empírica. Las expresiones propuestas son válidas para regiones donde las curvas
intensidad - duración de las precipitaciones puedan representarse por la ley de Grunsky.

**ABSTRACT**

A theoretical analysis is performed of the behaviour of a watershed under the Rational
Method approach and analytical expressions are proposed for a more objective estimation of
the runoff coefficient, as a function of the precipitation magnitude, the time of concentration
of the basin and the abstraction or infiltration rates. The proposed expressions are validated
against empirical coefficients and results. The proposed method is applicable in regions
where the intensity - duration curves can be represented by the Grunsky formula.

Santiago, Chile 13 y 14 de Noviembre 2003

SOCIEDAD CHILENA DE INGENIERÍA HIDRÁULICA
XVI CONGRESO CHILENO DE INGENIERÍA HIDRÁULICA

**USO “RACIONAL” DE LA FORMULA RACIONAL**

**1.- INTRODUCCION**

Tal vez, la fórmula hidrológica más utilizada a nivel mundial, sea la denominada
"fórmula racional", que pretende reproducir el caudal máximo instantáneo de una
crecida pluvial en cuencas pequeñas, a través de la expresión:

_Q_ = _c_ - _i_ - _A_ (1)

donde Q= caudal máximo instantáneo
A= área de la cuenca
i= intensidad media máxima de lluvia para una duración

⋅
correspondiente al tiempo de concentración de la cuenca
c= coeficiente de escorrentía de origen empírico que valida la igualdad
establecida por la fórmula.

El origen de la popularidad de la fórmula racional estriba indudablemente en su
extraordinaria simplicidad; el área de la cuenca es fácilmente determinable, la información
respecto a intensidades medias máximas de lluvias está frecuentemente disponible,
restando sólo establecer el tiempo de concentración de la cuenca y el valor del coeficiente
de escorrentía.

Respecto del primero, t c, se han propuesto diversas fórmulas que permiten su
estimación (1), con un nivel de exactitud aún no adecuadamente establecido; respecto del
coeficiente de escorrentía, se argumenta que la gran experiencia que se dispone respecto
de su cuantificación, es precisamente una de las ventajas de la aplicación de la fórmula
racional. De hecho, en un estudio desarrollado para la DGÁ (2), se propone, entre otras, el
uso de esta fórmula, extendiendo su aplicabilidad a tamaños de cuencas bastante mayores
a los tradicionalmente utilizados, recomendándose valores regionales para el coeficiente de
escorrentía.

Sin embargo, en la experiencia del autor al respecto, ha podido constatar una gran
incertidumbre en cuanto a la cuantificación del coeficiente de escorrentía, desconocimiento
de las hipótesis simplificatorias en las que descansa el método, interpretaciones físicas
discutibles del significado del coeficiente de escorrentía, o aplicación de la fórmula a
condiciones y tamaños de cuencas fuera de su rango de validez.

En el presente trabajo se discuten algunos conceptos que permiten orientar hacia
una utilización más "racional” de la fórmula racional, en particular en cuanto a su
aplicabilidad y cuantificación del coeficiente de escorrentía.

**2.- CONCEPTOS BASICOS** .

2.1.- Diagrama Tiempo - Area.

Santiago, Chile 13 y 14 de Noviembre 2003

SOCIEDAD CHILENA DE INGENIERÍA HIDRÁULICA
XVI CONGRESO CHILENO DE INGENIERÍA HIDRÁULICA

Dada una cuenca específica, es conceptualmente posible establecer la ubicación de
las líneas isocronas o líneas de igual tiempo de viaje hasta la sección de salida de la misma.
Calculando el área de la cuenca ubicada aguas abajo de cada línea isocrona y graficando
ésta en función del tiempo de viaje, se obtiene el denominado diagrama tiempo - área, que
representa la variación del área aportante de la cuenca en función del tiempo, hasta
alcanzar el área total de la misma para el tiempo de concentración de la cuenca, t c .

2.2.- Hidrograma de escorrentía directa.

Si ocurre sobre la cuenca una precipitación uniformemente repartida en el espacio,
cuyo hietograma de precipitación efectiva sea conocido, el caudal de salida dependerá de la
función de transferencia de la cuenca. En cuanto a las características de esta función de
transferencia, aún cuando la metodología para su análisis en base al comportamiento de
sistemas no lineales fue propuesta hace mas de 25 años, ésta no ha tenido mayor acogida,
posiblemente debido a que la eventual mejora de los resultados respecto a una hipótesis de
comportamiento lineal, no compensa el notable aumento de complejidad del análisis.
Aceptando, en consecuencia, que la cuenca se comporta como un sistema lineal, siendo el
diagrama tiempo - área invariante, entonces el caudal en la sección de salida en un instante
dado viene expresado por la integral de convolución,

_t_

###### = i e ( t − Τ )* u ( Τ ) d Τ
# ∫

###### Q ( t ) = i e ( t − Τ )* u ( Τ ) d

###### ( t ) = i e ( t − Τ )* u ( Τ ) d Τ (2)

0

donde i e (t-T) es el hietograma de precipitación efectiva,
u(T)= δA/δT es la derivada del diagrama tiempo - área y
T es una variable muda de integración.

La estructura de la fórmula (2) es idéntica a la definición del Hidrograma Unitario
Instantáneo, de donde resulta que bajo las hipótesis impuestas, el diagrama tiempo - área
es proporcional al hidrograma en S y su derivada o histograma de tiempo - área,
corresponde al Hidrograma Unitario Instantáneo de la cuenca. Esta función es en
consecuencia determinística estando definida en el tiempo desde el inicio de la tormenta
hasta el tiempo de concentración de la cuenca, t c .

El hietograma de precipitación efectiva, por otra parte, es una función aleatoria que
se anula a partir del tiempo de duración de la lluvia efectiva, t e .

La evaluación de la convolución, en consecuencia, dependerá del tiempo de
duración de la lluvia efectiva, del tiempo de concentración de la cuenca y del tiempo de
estimación del caudal o límite de integración t.

Diversos estudios se han realizado para establecer la existencia de secuencias
típicas o distribuciones temporales preferenciales de las tormentas (3,4), sin haberse
obtenido resultados concluyentes. Ante lo anterior, sólo es posible estimar a priori el caudal,
bajo el enfoque de la fórmula racional, utilizando un valor promedio esperado de la
intensidad de la lluvia. En consecuencia, la integral de convolución se transforma en:

Santiago, Chile 13 y 14 de Noviembre 2003

SOCIEDAD CHILENA DE INGENIERÍA HIDRÁULICA
XVI CONGRESO CHILENO DE INGENIERÍA HIDRÁULICA

_t_

= _i_ _e_ ( _t_ ) _u_ ( Τ ) _d_ Τ =
## ∫

_Q_ ( _t_ ) = _i_ _e_ ( _t_ ) _u_ ( Τ ) _d_ Τ = _i_ _e_ ( _t_ ) - _A_ ( _t_

( _t_ ) = _i_ _e_ ( _t_ ) _u_ ( Τ ) _d_ Τ = _i_ _e_ ( _t_ ) - _A_ ( _t_ ) (3)

0

donde i e (t) es la intensidad media de la precipitación efectiva para la duración t.

Considerando todas las combinaciones posibles de duración de lluvia, tiempo de
concentración de la cuenca e instante de evaluación del caudal, se obtienen los siguientes
resultados:

_Q_ ( _t_ ) = _i_ _e_ ( _t_ ) - _A_ ( _t_ ) para t < t e (4.1)

t < t c

_Q_ ( _t_ ) = _i_ _e_ ( _t_ _e_ ) - ( _A_ ( _t_ ) − _A_ ( _t_ − _t_ _e_ )) para t e < t < t c (4.2)

_Q_ ( _t_ ) = _i_ _e_ ( _t_ ) - _A_ [para t] c [ < t < t] e [ (4.3)]
_Q_ ( _t_ ) = _i_ _e_ ( _t_ _c_ + _t_ _e_ − _t_ ) - ( _A_ − _A_ ( _t_ − _t_ _e_ )) [ para t > t] c [(4.4) ]
t > t e

donde Q(t) es el caudal esperado para el instante t y A es el área total de la cuenca.

El caudal máximo para una duración "t" resultará utilizando el valor máximo de i e, es
decir, la intensidad media máxima para la duración de lluvia correspondiente. A su vez, el
caudal máximo instantáneo de la crecida, resultará determinando el valor del tiempo t que
maximice el valor del caudal, previo establecimiento del tiempo de concentración de la
cuenca y de la duración de la lluvia efectiva.

2.3.- Intensidad - Duración de la Lluvia.

Diversos estudios de curvas de intensidad-duración se han desarrollado tanto en
Chile como en el extranjero, determinando coeficientes generalizados de duración.(5,6).
Para los efectos prácticos, dentro del nivel de precisión posible de lograr mediante el uso de
la fórmula racional, uno de los resultados más interesantes de estos estudios es que
ratifican la validez, para tormentas de origen ciclónico y sin un excesivo efecto orográfico, de
la llamada fórmula de Grunsky (7), de amplia aplicación en Chile para la estimación de
intensidades medias máximas de lluvias de diferentes duraciones.

Según esta fórmula, la intensidad media máxima i(t) para una duración cualquiera, se
puede estimar como:

_i_ ( _t_ ) = _i_ 24 - (5)

donde i 24, es la intensidad media máxima en 24 horas.

Para duraciones extremadamente pequeñas, la estructura de la fórmula de Grunsky
tiende a dar intensidades excesivas, por lo que para fines prácticos se recomienda utilizar
como intensidad máxima probable, el valor resultante de una duración de aproximadamente
0.1 horas o 6 minutos, es decir,

−

_i_ _max_ = 155.* _i_ 24 para t< 0.1 horas

Santiago, Chile 13 y 14 de Noviembre 2003

SOCIEDAD CHILENA DE INGENIERÍA HIDRÁULICA
XVI CONGRESO CHILENO DE INGENIERÍA HIDRÁULICA

Si consideramos una tormenta centrada, simétrica y monomodal, siguiendo el
criterio de diseño de los bloques alternantes, por definición de promedio, se tiene **,**

_t_

+

2

_P_ ( _t_ ) = _i_ ( _t_ ) - _t_ = _i_ ( Τ ) _d_ Τ (6)
### ∫

_t_

### ∫

( _t_ ) = _i_ ( _t_ ) - _t_ = _i_ ( Τ )

= _i_ ( _t_ ) - _t_ = _i_ ( Τ ) _d_ Τ

− _t_

2

donde _t_ se mide con origen en el instante de máxima intensidad.

Reemplazando (5) en (6) se obtiene,

_t_

+

2

### ∫

### P ( t ) = i 24 * 24 t = ∫ i ( Τ ) d Τ (7)

_t_

( _t_ ) = _i_ 24 - 24 _t_ = _i_ ( Τ )

= _i_ 24 - 24 _t_ = _i_ ( Τ ) _d_ Τ

− _t_

2

Por último, la derivada de la ecuación (7) respecto a t, en el presente caso se reduce

a

_i_ ( _t_, ) = _i_ 24 - _t_, (8)

donde i(t ́) es la intensidad instantánea de precipitación en un instante a una distancia t ́ del
punto de máxima intensidad de una tormenta centrada, simétrica y monomodal, que respete
la ley de Grunsky.

2.4 Tasas de infiltración

Las tasas de infiltración o de pérdidas en general, son sin lugar a dudas una de las
variables de mayor incertidumbre para los propósitos del análisis y síntesis hidrológicos. De
las diversas metodologías o índices utilizados para su cuantificación, la tasa final de
infiltración de acuerdo al modelo de Horton o similares, es la más fácil de conceptualizar.
Este índice o tasa de infiltración se define como la tasa de infiltración potencial constante a
la cual tiende un suelo una vez que se independiza de las condiciones iniciales.

Si aceptamos este modelo, despreciando su variabilidad inicial, la intensidad de
precipitación efectiva queda dada por
_i_ _e_ ( _t_ ) = _i_ ( _t_ ) − _f_ (9)

donde f es la tasa de infiltración o pérdida constante.

Reemplazando (8) en (9) e imponiendo la condición de que la precipitación efectiva
sea nula, se obtiene una expresión para la duración de la precipitación efectiva:
#### [t] [ =] e 6 * ( i 24 f ) 2 (10)

de donde resulta que su intensidad media para la duración efectiva total, vale

_i_ _e_ ( _t_ _e_ ) = _i_ 24 _t_ _e_ − _f_ (11)

Santiago, Chile 13 y 14 de Noviembre 2003

SOCIEDAD CHILENA DE INGENIERÍA HIDRÁULICA
XVI CONGRESO CHILENO DE INGENIERÍA HIDRÁULICA

Reemplazando (10) en (11) se obtiene

_i_ _e_ ( _t_ _e_ ) = _f_ (12)

Nótese que si la precipitación efectiva total de la tormenta fuese conocida, producto
de la aplicación de algún método como el de la Curva Número o similar, la intensidad media
de la precipitación efectiva, igual a la tasa de infiltración, resulta,

( _t_ ) = _f_ = _P_ _ef_ = 6 - ( _i_ 24 [)] 2 (13)

_P_
_i_ ( _t_ ) = _f_ =

_i_ _e_ ( _t_ _e_ ) = _f_ = _t_ _ef_ = 6 - ( _iP_ 24

_e_ _ef_

2.5.- Caudal máximo de la crecida.

Del análisis de las ecuaciones (4), se observa que la 4.2 y 4.3 se maximizan para
duraciones iguales a t e y t c respectivamente. Por otra parte, la ecuación 4.4 puede reducirse
mediante un cambio de variable, a una forma equivalente a la ecuación 4.1. En esta última,
reemplazando el valor propuesto para la intensidad de la lluvia efectiva y estimando A(t)

como

_t_
_A_ ( _t_ ) = _A_ *( ) - _c_ _f_ - _c_ _p_ para t<t c (14.1)
_t_ _c_

_A_ ( _t_ ) = _A_ para t>t c (14.2)

es decir, una relación en principio lineal, corregida por un factor de forma c f y un factor de
pendiente c p, se obtiene:

24 _t_
_Q_ ( _t_ ) = ( _i_ 24 − _f_ )* _A_ - ( ~~)~~ - _c_ _f_ - _c_ _p_ (15)
_t_ _t_ _c_

Despreciando la variabilidad de los coeficientes c f y c p en las cercanías del máximo
caudal, derivando la ecuación (15) e igualando a cero, se obtiene: t=t e

Esta relación es válida para t e <t c, de donde

_Q_ _max_ = _i_ _e_ ( _t_ _e_ ) - _A_ _max_ ( _t_ _e_ ) (16)

A max es la máxima área que puede aportar, para un intervalo igual a la duración de la
precipitación efectiva. Si t e >t c, la ecuación (15) no alcanza un máximo, obteniéndose el
máximo caudal para el menor valor posible de t, en este caso, t c.

De todo lo antrior, concluye que la aplicación de la fórmula racional se reduce a

_Q_ _max_ = _i_ _e_ ( _t_ _e_ ) - _A_ _max_ ( _t_ _e_ ) para t e < t c (17)

Santiago, Chile 13 y 14 de Noviembre 2003

SOCIEDAD CHILENA DE INGENIERÍA HIDRÁULICA
XVI CONGRESO CHILENO DE INGENIERÍA HIDRÁULICA

o _Q_ _max_ = _i_ _e_ ( _t_ _c_ ) - _A_ [para t] e [ > t] c [ (18) ]

2.6 Coeficientes de forma y de pendiente

El efecto de la forma de la cuenca sobre el diagrama tiempo-área ha sido estudiado
en forma teórica, pudiendo calcularse de estos estudios valores típicos de coeficientes de
forma para algunos modelos geométricos regulares, según se indica en la Tabla N°1.

Tabla 1 Coeficientes de forma

t/t c Triangular Rectangular Cuadrada Sectorial

0.2 2.3 1.2 1.4 1.7
0.3 1.9 1.18 1.36 1.65
0.4 1.6 1.15 1.33 1.58
0.6 1.4 1.10 1.26 1.4
0.8 1.2 1.05 1.16 1.2
1.0 1.0 1.0 1.0 1.0

Comparando estas cifras con algunos valores resultantes del análisis de curvas áreatiempo de cuencas reales, se propone, en ausencia de mejor información, la relación
aproximada,

= 

[]

 _t_ _e_ 

 []  []

_t_ _c_

 

− .0325

_c_ _f_ =  [] _t_ _e_  [] para t e /t c - 0.047 (19)
_t_

_c_

 []


limitado al valor _[c]_ _f_ = 7.2 para t e /t c < 0.047.

Menos información existe respecto a los coeficientes de pendiente, los cuales
debieran ser cercanos a la unidad para pendientes uniformes, mayores de 1 para formas
cóncavas y menores de 1 para formas convexas, adoptándose en adelante el valor 1.0.

**3.- ESTIMACIÓN DE COEFICIENTES DE ESCORRENTÍA** .

De acuerdo a la definición de coeficiente de escorrentía, dado por la fórmula (1), y los
resultados de las ecuaciones (17) y (18), se obtienen las siguientes expresiones:

i) Para duraciones de la precipitación efectiva menores al tiempo de concentración de
la cuenca, t e < t c :

= _i_ _e_ ( _t_ _e_ ) - _A_ _max_ ( _t_ _e_ )
(20)

_i_ ( _t_ ) - _A_

_c_ = _i_ _e_ ( _t_ _e_ ) - _A_ _max_ ( _t_
_i_ ( _t_ ) - _A_

_c_

Reemplazando para cada una de las variables las expresiones propuestas por el
presente modelo, se obtiene:

_c_ = _f_ - _A_ - _t_ _e_ _t_ _c_ - _c_ _p_ - _c_ _f_ = _f_ - _t_ _e_ - _c_ _p_ - _c_ _f_ = 1 - 6 - _i_ 24 - _c_ _f_

- _A_ - _e_ _t_ _c_ - _c_ _p_ - _c_ _f_ _f_ - _t_ _e_ - _c_ _p_ - _c_ _f_ 1 6 _i_ 24

_e_ _t_ _c_ _c_ _p_ _c_ _f_ = _f_ - _t_ _e_ - _c_ _p_ - _c_ _f_ = 1 - 6 - _i_ 24 - _c_ _f_ - _c_

24 _i_ - 24 - _t_ 2 _t_ _f_

_f_ - _t_ - _c_ - _c_

- -

= _c_ = _e_ _p_ _f_ = - - 24 - _c_ - _c_ (21)

_e_ _p_ _f_

_c_ 2 _t_ _c_ _f_ _f_ _p_

|t<br>f *A* e *c *c<br>t p f<br>c|Col2|
|---|---|
|_i_<br>*<br>24|_c_<br>_A_<br>_t_<br>*<br>24|

Santiago, Chile 13 y 14 de Noviembre 2003

SOCIEDAD CHILENA DE INGENIERÍA HIDRÁULICA
XVI CONGRESO CHILENO DE INGENIERÍA HIDRÁULICA

ii) Para duraciones de la precipitación efectiva mayores que el tiempo de concentración
de la cuenca, t e - t c,

_c_ = _i_ _e_ ( _t_ _c_ ) = 1 − 1 - _t_ _c_ - _f_
_i_ ( _t_ _c_ ) 2 6 _i_ 24

= _e_ _c_ = 1 − - _c_ - (22)

_c_

Definiendo la variable adimensional,

- = _t_ _e_ = 6 - _i_ 24 (23)

_t_ - = _t_ _e_ = 6 - _i_
_t_ _c_ _t_ _c_ _f_

_c_ _c_

la estimación del coeficiente de escorrentía se reduce a

_c_ = 1 - _t_ - - _c_ _f_ - _c_ _p_ para t* < 1 (24)
2

1
_c_ = para t* = 1 (25)
2

1
_c_ = 1 − - para t* > 1 (26)

2 - _t_

Las expresiones anteriores se basan en una tasa final de infiltración constante. Si la
precipitación ocurre sobre un suelo relativamente seco, los coeficientes de escorrentía
serían menores a los indicados por las fórmulas propuestas. En este sentido resulta
conveniente estimar la tasa de infiltración adecuada a cada situación, a través de la
ecuación (13), a partir de una estimación independiente de la precipitación efectiva.

4 **.- EJEMPLOS DE APLICACIÓN** .

4.1.- Valores numéricos del coeficiente de escorrentía.

De todos los considerandos anteriores, se concluye que la magnitud del coeficiente
de escorrentía depende de la magnitud de la precipitación, del tiempo de concentración de
la cuenca y de la tasa de pérd idas o infiltración. A manera de ejemplo, en la Tabla N°2 se
presentan valores resultantes para el coeficiente de escorrentía siguiendo el procedimiento
propuesto, para distintas combinaciones de magnitud de la precipitación en 24 horas,
tiempo de concentración de la cuenca y distintas tasas de infiltración.

Cotejando las cifras con valores del coeficiente de escorrentía propuestos en
diversos textos, (1), resultan valores bastante coherentes para condiciones similares, con la
ventaja de que los valores aquí propuestos, resultan mucho mas objetivos.

4.2.- Comparación con cifras propuestas por DGA.

La DGA (2) ha propuesto valores para el coeficiente de escorrentía para distintas
cuencas del país, para un período de retorno base de 10 años, así como coefi cientes de

Santiago, Chile 13 y 14 de Noviembre 2003

SOCIEDAD CHILENA DE INGENIERÍA HIDRÁULICA
XVI CONGRESO CHILENO DE INGENIERÍA HIDRÁULICA

TABLA N°2. COEFICIENTES DE ESCORRENTIA.

CUENCA PEQUEÑA : Tc=0.5 HRS
f P=60 P=80 P=1OO P=120 P=140
(mm/hr)

2 0.88 0.91 0.93 0.94 0.95

4 0.77 0.83 0.86 0.88 0.90

8 0.54 0.65 0.72 0.77 0.80

16 0.40 0.45 0.48 0.54 0.60

CUENCA MEDIA: Tc=2.0 HRS

2 0.77 0.83 0.86 0.88 0.90

4 0.54 0.65 0.72 0.77 0.80

8 0.40 0.45 0.48 0.54 0.60

16 0.32 0.35 0.38 0.40 0.43

CUENCA MAYOR: Tc=8 HRS

2 0.54 0.65 0.72 0.77 0.80

4 0.40 0.45 0.48 0.54 0.60

8 0.32 0.35 0.38 0.40 0.43

16 0.18 0.24 0.30 0.32 0.33

32 0.07 0.12 0.15 0.18 0.21

frecuencia para otros períodos de retorno. En la Tabla N°3 se presentan los coeficientes de
escorrentía propuestos por la DGA y las precipitaciones máximas en 24 horas típicas de
cada región (8), para un período de retorno de 10 años, junto a las tasas de infiltración
requeridas para cuencas de distinto tiempo de concentración, que permitan reproducir
dichos coeficientes de escorrentía, con la fórmula propuesta. Para la III Región y cuenca del
Elqui, las tasas requeridas superan la tasa máxima de validez de la fórmula propuesta. En
otras palabras, no es posible reproducir coeficientes de escorrentía tan bajos para una
cuenca homogénea y la escorrentía debiera ser nula. La existencia de escorrentía sólo se
explicaría en el caso de una cuenca heterogénea, en la cual sólo una pequeña fracción de
la cuenca estuviese aportando. De Limarí al Sur, se obtienen ya tasas de infiltración
admisibles, siendo los valores correspondientes a tiempos de concentración de 16 hrs a 48
hrs., los más razonables.

Por último, en la Figura N°1, se presenta la diferencia en porcentaje entre la
estimación del coeficiente de escorrentía que resulta para distintos períodos de retorno, de
la aplicación de los coeficientes de frecuencia propuestos por la DGA y de la aplicación de la
fórmula propuesta, adoptando las precipitaciones diarias típicas para cada período de
retorno en cada región.( 8).

Tabla N°3. Infiltración necesaria para reproducir coeficientes DGA (mm/hr)

|Región|III|Elqui|Limarí|V-Choapa|VI|VII|VIII|iX|
|---|---|---|---|---|---|---|---|---|
|P(10) mm<br>Cd(10) DGA<br>|40<br>0.009<br>|70<br>0.025<br>|80<br>0.078<br>|85<br>0.08<br>|100<br>0.31<br>|110<br>0.39<br>|100<br>0.36<br>|90<br>0.28<br>|
|~~Tc=4 hr~~|~~305~~|~~193~~|~~71~~|~~73~~|~~20~~|~~11~~|~~13~~|~~22~~|
|Tc=16 hr<br>|153<br>|96<br>|35<br>|36<br>|10<br>|6 <br>|7 <br>|11<br>|
|~~Tc=48 hr~~|~~88~~|~~56~~|~~20~~|~~21~~|~~6 ~~|~~3 ~~|~~4 ~~|~~6 ~~|
|Inf. max.<br>|26|45|52|55|65|71|65|58|

Santiago, Chile 13 y 14 de Noviembre 2003

SOCIEDAD CHILENA DE INGENIERÍA HIDRÁULICA
XVI CONGRESO CHILENO DE INGENIERÍA HIDRÁULICA

Se observa que en 4 de las 9 regiones comparadas, Limarí, Aconcagua, VII y VIII
regiones, las diferencias entre los coeficientes propuestos por la DGA y los que resultan
del procedimiento propuesto, no superan el 10%; en la IX Región, las diferencias
alcanzan hasta el 20%, mientras en las 4 restantes, III, Elqui, Choapa y VI, las
diferencias superan el 50% en los casos más extremos.

Aún cuando estas últimas cifras parecieran ser importantes, el nivel de precisión
que puede alcanzarse en este tipo de análisis, absolutamente generalizado, no es muy
alto, por lo que los resultados obtenidos, no hacen más que validar, con un nivel de
error menor al esperado, el procedimiento propuesto para el cálculo de los coeficientes.

4.3.- Comparación con la fórmula de Verni y King.

Reemplazando los valores propuestos para el coeficiente de escorrentía en la
fórmula racional original, los caudales máximos instantáneos de la crecida, en m [3] /seg,
quedan dados por las siguientes expresiones:

= .003125* _P_ 242 - _A_ para Φ < 5.4 (27.1)

_Q_ _max_ = .003125* _P_ 242 - _A_

_max_ = .003125* 2

_Q_ _max_ [=] .001287 - _P_ 240.1.673346 - .0 _A_

_Q_ = .00567*  _P_ 24 − _f_ 24 _t_

_max_ [=] .001287 - 240.673 - .0346 para 5.4 < Φ < 96 (27.2)

= .00567*  _P_ 24 − _f_ 24 _t_ _c_  - _A_ para Φ - 96 (27.3)

_max_ = .00567*  _P_ 24 − _f_ 24 _t_ _c_ 

_c_ - _A_

|f t c * * 2 346 .0 673 . 0 346 .1 24 * * f A t P c −|Col2|
|---|---|
|_t_<br>_f_<br>_P_<br>_c_<br>24<br>24<br>−|_t_<br>_f_<br>_P_<br>_c_<br>24<br>24<br>−|
||_t_<br>_c_|

_P_ 242

_t_ - _f_

Φ = _t_ _c_ - 24 _f_ 2 y las unidades son P (mm), t (hr) y A (km [2)] .

donde Φ = 24
2

En la Figura N°2 se comparan los resultados del procedimiento propuesto, para
distintas tasas de abstracción o infiltración, con los que arroja la fórmula propuesta por
Verni y King (2), para el caso de una cuenca de 500km [2], con un tiempo de
concentración estimado de 8 horas. Nuevamente, la excelente concordancia obtenida,
valida el procedimiento propuesto.

5.- Referencias Bibliográficas:

1.- Ven Te Chow et al., "Hidrología Aplicada", Mc Graw-Hill,1996
2.- DGA, "Manual de Cálculo de Crecidas y Caudales Mínimos”, DGA N°1, 1996.
3.- Espíldora, B.y Echavarría A.,"Criterios para la Caracterización y Selección de
Lluvias de Diseño", IV Col. Nac de Hidráulica, SOCHID, 1978
4.- Benitez, A. y Verni, F.,"Distribución Porcentual de las Precipitaciones para
Duraciones entre 12 y 72 horas", VII Cong. Nac. de Hidráulica, SOCHID,1985
5.- Espíldora B.,"Estimación de Curvas Intensidad-Duración-Frecuencia Mediante
Coeficientes Generalizados, I Col. Nac. de Hidráulica, SOCHID, 1969.
6.- Varas E. y Sánchez S., "Relaciones Intensidad-Duración-Frecuencia Generalizadas",
VI Congr. Nac. de Hidráulica, SOCHID,1983.

Santiago, Chile 13 y 14 de Noviembre 2003

SOCIEDAD CHILENA DE INGENIERÍA HIDRÁULICA
XVI CONGRESO CHILENO DE INGENIERÍA HIDRÁULICA

7.- Arretz A., "Método de Grunsky para el Cálculo de Crecidas", Revista Chilena de
Ingeniería, N°2, 1943
8.- DGA, ”Precipitaciones Máximas en 1,2 y 3 Días”,1991

**FIG N°1 DIFERENCIA ENTRE COEFICIENTES DGA Y PROPUESTOS**

80

60

40

III REGION

20

0

-20

-40

-60

**PERIODO DE RETORNO (AÑOS)**

**F i g . N ° 2 C o m p a r a c i ó n c o n V e r n i y K i n g**

**A=500 km2 Tc=8 hrs**

verni-king f=4 mm/hr f = 6 m m / h r f=8 mm/hr

ELQUI

LIMARI

CHOAPA

ACONCAGUA

VI REGION

VII REGION

VIII REGION

IX REGION

1 0 0 0

9 0 0

8 0 0

7 0 0

6 0 0

5 0 0

4 0 0

3 0 0

2 0 0

1 0 0

0

0 2 0 4 0 6 0 8 0 1 0 0 1 2 0 1 4 0 1 6 0

**P r e c i p i t a c i ó n d i a r i a ( m m )**

Santiago, Chile 13 y 14 de Noviembre 2003