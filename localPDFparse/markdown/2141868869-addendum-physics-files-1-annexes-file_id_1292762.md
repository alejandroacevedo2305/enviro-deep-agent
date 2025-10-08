---
title: 9613.PDF
author: Christian Gerard
date: D:20030415134152
language: es
type: general
pages: 25
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  -  ( 1/ T ) ∫ p f 2 ( ) t dt 
  - ∫
  -  ( 1/ T ) ∫ p f 2 ( ) t dt 
  - / T ) ∫ p f 2 ( ) t dt  / p 02
-->

### ISO 9613 A TENUACIÓN DEL S ONIDO D URANTE LA P ROPAGACIÓN EN E XTERIORES .

**P** **ARTE** **1: C** **ÁLCULO DE LA ABSORCIÓN DEL SONIDO POR LA ATMÓSFERA**

**1 Scope**

Esta parte de ISO 9613 especifica un método analítico para calcular la
atenuación de sonido como resultado de la absorción atmosférica para diversas
condiciones meteorológicas donde el sonido desde cualquier fuente se
propaga a través de la atmósfera exterior.
Para tonos puros de sonido, la atenuación debido a la absorción
atmosférica es especificada en términos de de un coeficiente de atenuación
como función de cuatro variables: frecuencia de sonido, temperatura, humedad
y presión del aire. Calculados los coeficientes de atenuación son mostrados en
forma de tablas para rangos de variables comúnmente encontrados en la
predicción de propagación de sonido en exteriores:

- Frecuencia desde 50Hz hasta 10 kHz.

- Temperatura desde -20 °C a 50 °C

- humedad relativa desde 10% hasta 100% y

- Presión de 101,325 kPa (una atmósfera)
las fórmulas además proporciona un rango adecuado para usos particulares,
por ejemplo, a frecuencias ultrasónicas para modelación a escala, y a bajas
presiones para grandes altitudes hacia el suelo.

Para sonidos de banda ancha analizados con filtros de bandas de tercios

de octava, se especifica un método para calcular la atenuación por efecto de la
absorción atmosférica a partir de estas especificaciones para tonos puros en las
frecuencias centrales. Un método alternativo de integración de espectros se
describe en el anexo D. El espectro de sonido puede ser de banda ancha sin
componentes de frecuencias discretas significantes o puede ser la combinación
de sonidos de frecuencia discreta o de banda ancha.

Esta parte de ISO 9613 está aplicada a una atmósfera con condiciones
meteorológicas uniformes. Puede además ser usada para determinar ajustes
aplicables a mediciones de niveles de presión sonora donde existen diferencias
entre pérdidas de absorción atmosférica bajo diferentes condiciones
meteorológicas. La extensión del método a atmósferas no homogéneas es
considera en el anexo C, en particular condiciones meteorológicas que varían

con la altura sobre el suelo.

Además, esta parte de ISO 9613 considera (calcula) para los principales
mecanismos de absorción presentes en una atmósfera desprovista de humo o
contaminantes. El cálculo de atenuación de sonido por otros mecanismos,
como refracción o reflexión del suelo, esta descrito en ISO 9613-2

**2 Normativa de referencia**

Los siguientes estándares contiene consideraciones las cuales, a través de las
referencias en el texto, constituyen consideraciones de esta parte de ISO 9613.
Son válidas al tiempo de publicación. Todos los estándares están sujetos a
revisión, y parte del comportamiento basado en esta parte de ISO 9613 son
llevados a investigar la posibilidad de aplicar las más recientes ediciones de
estándares indicados más abajo. Miembros de ISO y IEC mantienen registros

de la validación de estándares internacionales corrientes.

ISO 2533:1975. Atmósfera estándar

ISO 266:1975. Acústica, frecuencias preferidas para mediciones
IEC 225:1966. Filtros de octava y tercio de octava para el análisis de ruido y

vibraciones.

**3 Símbolos**

f frecuencia del sonido, en hertz.

f m frecuencia central de una banda, en hertz
h concentración molar de vapor de agua, como un porcentaje
p r presión atmosférica ambiente de referencia, en kilopascales.
p i amplitud de presión sonora inicial, en pascales.
p t amplitud de presión sonora, en pascales
p [0] amplitud de presión sonora de referencia (20 μ Pa)
p a presión atmosférica ambiente, en kilopascales.
s distancia, en metros, a través de la cual el sonido se propaga
T temperatura atmosférica ambiente, en kelvin.
T [0] temperatura de referencia del aire, en kelvin.
α coeficiente de atenuación de tonos puros en decibeles por metro, para

absorción atmosférica.

NOTA 1: Por conveniencia, en esta parte de la ISO 9613, se usará el
término coeficiente de atenuación para α en lugar de una descripción
completa.

δ L t Atenuación debido a la absorción atmosférica, en decibeles

**4 Condiciones atmosféricas de referencia.**

4.1 Composición
La absorción atmosférica es sensible a la composición del aire,
particularmente a la amplia variación de concentración de vapor de agua . Por
ejemplo, para el aire seco a nivel del mar, la concentración molar estándar o los
volúmenes fraccionales de los tres principales, normalmente mezclados
constituyentes, nitrógeno, oxigeno y dioxido de carbono son: 0,78084; 0,209476;
y 0,000314 respectivamente (tomado de ISO 2533). Para el aire seco, otra menor
parte de constituyentes, las cuales no tienen influencia significativa en la
absorción del atmosférica, ocupan la fracción restante de 0,00937. Para cálculos
de absorción atmosférica, la concentración molar estándar de los tres
principales constituyentes del aire seco puede ser asumida como constante
para altitudes de al menos 50 km. sobre el nivel medio del mar. Sin embargo, la
concentración molar del vapor de agua, el cual tiene mayor influencia en la
absorción atmosférica, varía ampliamente cerca del suelo por sobre dos de
magnitud desde el nivel de mar hasta 10 km.

4.2 Presión atmosférica y temperatura.
Para propósitos de esta parte de ISO 9613, la presión atmosférica
ambiente de referencia, p [r], se toma del Estándar Internacional de Atmósfera,
esto es 101,325 kPa. La temperatura de referencia del aire T 0 es 293,15 K (20°C),
es decir, la temperatura a la cual se obtienen los más confiables datos de apoyo
de esta parte de ISO 9613.

**5 Coeficiente de atenuación debido a la absorción para tonos puros.**

5.1 Expresión básica para la atenuación
Como un tono puro se propaga a través de la atmósfera sobre la
distancia s, la amplitud de la presión sonora p t decrece exponencialmente
como resultado del efecto de la absorción atmosférica cubierta por esta parte
de ISO 9613 desde el valor inicial p [i], de acuerdo con la fórmula de decaimiento
para ondas planas en espacio libre.
P t = p i exp (-0,1151 α s) ...(1)

NOTA 2: El término exp (-0,1151 α s) representa la base e del logaritmo
neperiano basado en el exponente indicado por el argumento en
paréntesis y la constante 0,1151 = 1/[10log(e [2] )].

5.2 Atenuación de niveles de presión sonora
La atenuación debido a la absorción atmosférica δ L t (f), en decibeles, en
el nivel de presión sonora de un tono puro con frecuencia f, a partir del valor
inicial a s = 0 al nivel a distancia s, está dado por
δ L t (f) = 10 log ( p i [2] /p t [2] ) dB = α s ...(2)

**6 Procedimiento de cálculo para el coeficiente de atenuación de tonos puros**

6.1 Variables

Las variables acústicas y atmosféricas, es decir frecuencia de sonido,
temperatura atmosférica ambiente, concentración molar de vapor de agua y
presión atmosférica ambiente, están detalladas en la parte 3, junto con sus
símbolos y unidades.

NOTAS

3 Para un ejemplo específico de muestra de aire, la concentración molar
de vapor de agua es la razón (expresada como un porcentaje) del
número de kilomoles de vapor de agua a la suma del número de
kilomoles de vapor de agua y aire húmedo. Por la ley de Abogadro, la
concentración molar del vapor de agua es además la razón de la presión
de vapor de agua a la presión atmosférica.

4

**7 Precisión del coeficiente de atenuación de tonos puros calculado para varios**
**rangos de variables.**

7.1 Precisión de ± 10 %

La precisión del coeficiente de atenuación para tonos puros calculado para
absorción atmosférica es estimado en ± 10 % para variables dentro de los
siguientes rangos:

 - Concentración Molar de vapor de agua: 0,05 % a 5 %

 - Temperatura del aire: 253,15 K a 323,15 K ( -20°C a 50°C)

 - Presión atmosférica: menor que 200 Kpa (2 atm)

 - Razón de frecuencia a presión: 4 x 10 [-4] Hz/Pa a 10 Hz/Pa (40 Hz/atm
a 1MHz/atm)

NOTA 7: Combinaciones de concentraciones de vapor de agua y
temperatura las cuales implican una humedad relativa mayor que un
100% en 7.1 y 7..3 son excluidas a partir de las correspondientes
estimaciones de precisión.

7.2 Precisión de ± 20 %

La precisión del coeficiente de atenuación para tonos puros calculado para
absorción atmosférica es estimado en ± 20 % para variables dentro de los
siguientes rangos:

 - Concentración Molar de vapor de agua: 0,005 % a 0,05 %, y mayor que

5%

 - Temperatura del aire: 253,15 K a 323,15 K ( -20°C a 50°C)

 - Presión atmosférica: menor que 200 Kpa (2 atm)

 - Razón de frecuencia a presión: 4 x 10 [-4] Hz/Pa a 10 Hz/Pa (40 Hz/atm
a 1MHz/atm)

7.3 Precisión de ± 50 %

La precisión del coeficiente de atenuación para tonos puros calculado para
absorción atmosférica es estimado en ± 50 % para variables dentro de los
siguientes rangos, los cuales incluyen las condiciones ambientales
encontradas a altitudes sobre 10 km:

 - Concentración Molar de vapor de agua: menor que 0,005 %

 - Temperatura del aire: mayores que 200 K ( -73°C)

 - Presión atmosférica: menor que 200 Kpa (2 atm)

 - Razón de frecuencia a presión: 4 x 10 [-4] Hz/Pa a 10 Hz/Pa (40 Hz/atm
a 1MHz/atm)

**8 Cálculo de atenuación por absorción atmosférica sonidos de banda ancha**
**analizados por filtros de bandas de octava.**

8.1 Descripción del problema general **y** método de cálculo
Los apartados anteriores de esta parte de la ISO 9613 han considerado el
efecto de la absorción atmosférica en la reducción del nivel de un tono puro
durante la propagación a través de la atmósfera. En la práctica, sin embargo, el
espectro de muchos sonidos cubre un amplio rango de frecuencias, y un
análisis espectral es realizado normalmente por filtros de bandas de octava
esto produce niveles de presión sonora en bandas de frecuencia.

8.2 Método de tonos puros para aproximar atenuación de niveles de banda
8.2.1 Para cada banda de octava de interés y con condiciones metereológicas
especificada uniformes a lo largo del camino de propagación del sonido,
calculamos el coeficiente de atenuación resultante a partir de la absorción
atmosféricas para frecuencias centrales exactas de bandas (como se
determinó desde la ecuación 6), usando el procedimiento de tonos puros
descrito en la sección 6. La atenuación de nivel de banda para cada banda de
frecuencia, en decibeles, es entonces el producto del coeficiente de
atenuación para frecuencias centrales y la longitud del camino, como en la
ecuación 2 para tonos puros. Pueden ocurrir condiciones metereológicas no
uniformes a través de un largo camino, como se discute en el anexo C.
8.2.2 El error en la atenuación del nivel de banda introducido por este método
de cálculo de tonos puros es estimado para no exceder 0,5 dB provocado

por:

 - filtro pasa banda de acuerdo con la clase 1 o clase 0 del limite de
tolerancia de EIC 225;

 - para filtros de banda de tercio de octava, el producto de la longitud del
camino fuente receptor, en kilómetros, y el cuadrado de lafrecuencia
central, en kilohertz no excede 6 km*kHz [2] o la longitud del camino no
excede 6 km (en cualquier banda central);

 - para filtros de octava, el producto de la longitud de camino fuentereceptor, en kilometros, y el cuadrado de la frecuencia central, en

kilohertz no excede 3 km*kHz [2] o la longitud del camino no excede 3 km
(en cualquier banda central).
8.2.3 El método descrito en 8.2.1 es aplicable al cálculo de atenuación de nivel
de banda del sonido producido por fuentes de sonido estacionarias o en
movimiento. Si la fuente de sonido se mueve durante el periodo de interés,
la atenuación a partir de la absorción atmosférica varía con el tiempo porque
la frecuencia efectiva (o longitud de onda efectiva) varia con el tiempo
debido al efecto Doppler. Este efecto debe ser tomado en cuenta calculando
el coeficiente de atenuación para la frecuencia afectada por el efecto
Doppler, aplicable al ángulo de emisión de sonido para cada tiempo de

interés.

8.3 Cálculo de la atenuación de absorción atmosférica para niveles de presión
sonora ponderado A.
Debido a que el efecto de la absorción atmosférica es muy dependiente
de la frecuencia, los procedimientos recomendados para la predicción de la
influencia de la absorción atmosférica en niveles de presión sonora ponderado
A, descritos con un ejemplo en el anexo E, son primero determinar la
atenuación de nivel de banda aplicable al la condición atmosférica. Aplicada la
atenuación de nivel de banda calculado al nivel de presión sonora de banda

determinado a la distancia de referencia.

8.4 Sonidos de banda ancha y tonos puros combinados.
Para señales de banda ancha y con componentes de uno o mas tonos
puros, se debe seguir el siguiente procedimiento para calcular la atenuación de
niveles de presión sonora por bandas de octava como resultado de la absorción
atmosférica. El procedimiento es aplicable a sonidos producidos fuentes en
movimientos o estacionarias. Si la fuente esta en movimiento, el coeficiente de
atenuación debe ser calculado por el efecto Doppler para componentes de
tonos puros o frecuencias centrales de componentes de banda ancha, como se

describe en 8.2.3.

Paso 1Separar el espectro medido, basándose en los niveles de presión rms, en
componentes de tonos puros y de banda ancha. Para componentes de
tonos puros, la frecuencia del tono puede ser determinada por análisis
de espectro con un filtro de banda angosta, con un conocimiento previo
de los tonos de la fuente o definiendo un protocolo de estimación de la
presencia y nivel de un tono basado solamente en cambios relativos en
el nivel de presión sonora de la banda de octava (o tercio de octava)
adyacente. Para casos posteriores, la frecuencia del tono puede ser

asumida como la frecuencia central exacta del filtro de banda. Sin

embargo, si el método de aproximación para tonos puros dado en 8.2 es
usado para el elemento de banda ancha, y si la frecuencia del tono es
asumida como la frecuencia central del filtro de banda, entonces el
procedimiento de separar los componentes espectrales no es necesario

porque la misma atenuación para tono-puro podría aplicarse a ambos
casos de componentes de banda ancha y frecuencias discretas.

Paso 2 Calcular la atenuación sobre la longitud del camino especificado para
cada componente espectral separadamente utilizando los métodos
especificados en 5.2 y 6.3 para componentes de tonos puros, y en 8.2
para componentes de banda ancha.

Paso 3 Si el espectro inicial es del sonido de la fuente en el punto de ubicación
de la fuente, reste las atenuaciones de la absorción atmosférica calculada
de las frecuencias discretas separada y componentes de banda ancha,
para obtener estimaciones de los niveles de presión sonora de los
componentes separados del espectro en la posición del receptor,
tomando en cuenta solamente perdidas por absorción atmosféricas. Si el
espectro inicial es el de un sonido en la ubicación del receptor las
atenuaciones calculadas de la absorción atmosférica para obtener
estimaciones de los NPS correspondientes a la posición de la fuente.
Además reste (sume) estimaciones para atenuación debido a otros
mecanismos ( divergencia de ondas, etc.) al nivel de presión de las
bandas de frecuencia del espectro inicial.

Paso4: Combine las estimaciones para las presiones de sonido rms de los
componentes por separados del espectro para obtener los NPS de las
bandas del espectro compuesto en la posición del receptor o fuente.

### ISO 9613 A TENUACIÓN DE S ONIDO D URANTE LA P ROPAGACIÓN EN E XTERIORES .

**P** **ARTE** **2: M** **ÉTODO GENERAL DE CÁLCULO** **.**

**1 Resumen**

Esta parte de la ISO 9613 especifica un método ingenieril para calcular la
atenuación de sonido durante la propagación en exteriores para predecir los

niveles de ruido ambiental a una distancia de una variedad de fuentes. El

método. El método predice el nivel de presión sonora continuo equivalente
ponderado A (como se describe en las partes 1 a la 3 de ISO 1996) bajo
condiciones meteorológicas favorables para la propagación a partir de fuentes

de emisión de sonido conocido.

Esta condiciones son para propagación con bajo viento, como se
especifica en 5.4.3.3 de ISO 1996-2:1987 o equivalentemente propagación bajo
inversión de temperatura, tal como ocurre comúnmente ocurre en la noche. Las
condiciones de inversión sobre superficies de agua no son cubiertas y pueden
resultar en niveles de presión sonora más altos como se predice en esta parte

de ISO 9613.

EL método además predice un promedio de nivel de presión sonora
ponderado A como se especifica en ISO 1996-1 y ISO 1996-2. El promedio de
nivel de presión sonora ponderado A abarca niveles para una amplia variedad
de condiciones meteorológicas.
EL método especificado en esta parte de ISO 9613 consiste
específicamente de algoritmos de banda de octava (con frecuencias centrales
nominales a partir de 63 Hz y hasta 8 kHz) para calcular la atenuación de sondo
el cual se origina a partir de una fuente puntual o un grupo de fuentes
puntuales. La fuente (o fuentes) pueden estar en movimiento o estacionarias.
Los términos específicos son proporcionados en los algoritmos para los
siguientes efectos físicos:

 - Divergencia geométrica

 - Absorción atmosférica

 - Efecto del suelo

 - Reflexiones de superficies

 - Apantallamiento por obstáculos.

Información adicional concerniente a la propagación a través de casas bosques
y sitios industriales están dadas en el anexo A.
Este método es aplicable en la práctica a una gran variedad de fuentes y
ambiente de ruido. Es aplicable, directa o indirectamente, a muchas situaciones
concernientes a tráfico rodado o de ferrocarriles, fuentes de ruido industrial,
actividades de construcción y muchas otras fuentes de ruido. Esto no es
aplicable a ruido de aviones en vuelo o ondas explosiones de la minería o
militares u operaciones similares.

Para aplicar el método de esta parte de ISO 9613, varios parámetros necesitan
ser conocidos con respecto a la geometría de la fuente y del ambiente, las
características de la superficie del suelo, y de la fuerza de la fuente en términos
de niveles de presión sonora en bandas de octava para direcciones relevantes a
la propagación.

Nota 1: Si solamente se conocen niveles de presión sonora ponderado A,
el término de atenuación para 500 Hz puede ser usado para estimar la

atenuación resultante.

La precisión del método y las limitaciones de este uso en la práctica están
descritas en la parte 9.

**2 Normativa de referencia**

Los siguientes estándares contienen previsiones las cuales, a través de
referencias en el texto, constituyen previsiones de esta parte de ISO 9613. Al
mismo tiempo de publicación, la edición indica su validez. Todos los
estándares están sujetos a revisión, y parte del acuerdo basado en esta parte de
ISO 9613 están alentando la investigación de la posibilidad de aplicar la más
reciente edición de los estándares indicados debajo. Miembros del IEEC e ISO
mantienen registro de la validación de estándares internacionales.

ISO 1996-1: 1982 Descripción y medición de ambientes de ruido. Parte 1:
cantidades básicas y procedimientos.
ISO 1996-2: 1987 Descripción y medición de ambientes de ruido. Parte 2:
Adquisición de datos pertinentes al uso de suelo.
ISO 1996-3: 1987 Descripción y medición de ambientes de ruido. Parte 3:
Aplicación de limites de ruido.
ISO 9613-1: 1993 Atenuación de sonido durante la propagación en exteriores.
Parte 1: Calculo de la absorción de sonido por la atmósfera.
IEC 651: 1979 Medidores de nivel de sonido, mejora 1: 1993.

**3 Definiciones**

Para los propósitos de esta parte de ISO 9613, las definiciones dadas en ISO
1996-1 y las siguientes definiciones aplicadas.

3.1 Nivel de presión sonora continuo equivalente, en decibeles, definido por la

ecuación 1:

 _T_ 
##  []  ( 1/ T ) ∫ p A 2 ( ) t dt 

 []  0 

L [AT] = 10 log  ( 1/ _T_ ) _p_ _A_ 2 ( )


 []

 [] [ dB ....(1) ]

 []

 _T_
##  ( 1/ T ) ∫

 _T_ 
##  ( 1/ T ) ∫ p A 2 ( ) t dt 

 0 

## / T ) ∫ p A 2 ( ) t dt  / p 02

0 

donde:

p [A] (t) es la presión de sonido ponderado A instantánea, en pascales;
p 0 es la presión sonora de referencia (=20x 10 [-6 ] Pa);
T es el intervalo de tiempo especificado, es segundos.

La ponderación A por frecuencias está especificado para los medidores de
nivel en IEC 651.

Nota 2 El intervalo de tiempo T debe ser bastante largo para promediar
el efecto de la variación de parámetros meteorológicos. Dos diferentes
situaciones son consideradas en esta parte de ISO 9613, llamadas término corto
bajo viento y término largo sobre el promedio.

Símbolo Definición Unidad

A Atenuación por banda de octava dB
C [met] Corrección meteorológica dB
d Distancia desde la fuente puntual al receptor ( ver fig. 3) m
d p Distancia desde la fuente puntual al receptor proyectado

en el plano del suelo (ver fig. 1) m

d [s,o ] Distancia entre fuente y punto de reflexión en el obstáculo

reflectante (ver fig. 8) m

d o,r Distancia entre el punto de reflexión en el obstáculo

reflectante y el receptor (ver fig. 8) m

d [ss ] Distancia desde la fuente al (primer) borde de difracción

(der fig. 6 y 7) m

d sr Distancia desde (segundo) el borde de difracción al

receptor (ver figuras 6 y 7) m

D [i] Indice de directividad de la fuente sonora puntual D [z ] Atenuación por apantallamiento e Distancia entre el primer y segundo borde de difracción

(ver fig. 7) m

G Factor de suelo
h m

Atenuación por banda de octava
Corrección meteorológica
Distancia desde la fuente puntual al receptor ( ver fig. 3)
Distancia desde la fuente puntual al receptor proyectado
en el plano del suelo (ver fig. 1)
Distancia entre fuente y punto de reflexión en el obstáculo
reflectante (ver fig. 8)
Distancia entre el punto de reflexión en el obstáculo
reflectante y el receptor (ver fig. 8)
Distancia desde la fuente al (primer) borde de difracción
(der fig. 6 y 7)
Distancia desde (segundo) el borde de difracción al
receptor (ver figuras 6 y 7)
Indice de directividad de la fuente sonora puntual
Atenuación por apantallamiento
Distancia entre el primer y segundo borde de difracción
(ver fig. 7)

Factor de suelo

Altura media del receptor y fuente

dB

dB

m

m

m

m

m

m



m


m

h [s]

h r

h m

H [max]

I min

L

α
β

ρ

Altura de la fuente puntual sobre el suelo (ver fig. 1)
Altura del receptor sobre el suelo (ver fig. 1)
Altura media del camino de propagación sobre el suelo
(ver fig. 3)
Mayor dimensión de la fuente
Menor dimensión (largo o alto) del plano reflectante (ver
fig.8)
Nivel de presión sonora

Coeficiente de atenuación atmosférica

Angulo de incidencia

Coeficiente de Reflexión de sonido

[s] m

h r Altura del receptor sobre el suelo (ver fig. 1) m
h m Altura media del camino de propagación sobre el suelo

(ver fig. 3) m

H [max] Mayor dimensión de la fuente m
I min Menor dimensión (largo o alto) del plano reflectante (ver

fig.8) m

L Nivel de presión sonora dB

α Coeficiente de atenuación atmosférica dB/km
β Angulo de incidencia rad
ρ Coeficiente de Reflexión de sonido

3.2 Nivel de presión sonora continuo equivalente por bandas de octava
Downwind, L fT (DW): El nivel de presión sonora, en decibeles, está definido
por la ecuación (2):

_T_
#  ( 1/ T ) ∫ p f 2 ( ) t dt 

 []  0 

L (DW) = 10 log  ( 1/ _T_ ) _p_ _f_ 2 ( )



 dB ...(2)

 []

 []

 _T_

 ( 1/ _T_ )
# ∫

 _T_ 
#  ( 1/ T ) ∫ p f 2 ( ) t dt 

 0 

# / T ) ∫ p f 2 ( ) t dt  / p 02

0 

donde p f (t) es la presión sonora instantánea por bandas de octava
downwing, en pascales, y el subíndice f representa frecuencia central nominal

del filtro de banda de octava.

Nota 3: Las características eléctricas de los filtros de banda de octava

deberían ser acordes al menos con los requerimientos de la clase 2 de

IEC 1260.

3.3 Pérdida por inserción (de una barrera): Diferencia, en decibeles, entre el
nivel de presión sonora en el receptor en una posición específica bajo dos

condiciones:

 - sin la presencia de la barrera, y

 - con la barrera presente.

Y sin otros cambios significativos que afecten la propagación del sonido.

4 **Descripción de la fuente**

Las ecuaciones a ser usadas son las atenuación de sonido a partir de
fuentes puntuales. Extensiones de fuentes de ruido, tales como tráfico de
vehículos y ferrocarriles o un complejo industrial (el cual incluye varias
instalaciones o plantas junto con el movimiento de tráfico en el lugar) deberían
ser representadas por un conjunto de secciones, cada una teniendo un cierto
nivel de potencia sonora y directividad. La atenuación calculada para sonidos
a partir de un punto representativo dentro de una sección es usado para
representar la atenuación de sonido desde la sección completa. Una línea
puede ser dividida en secciones de líneas, una área fuente en dos secciones,
cada una representada por una fuente puntual en el centro.
Sin embargo, un grupo de fuentes puntuales puede ser descrito como
una fuente puntual equivalente situada en la mitad del grupo, en particular si:

 - Las fuentes tienen aproximadamente las mismas energía y altura
sobre el plano del suelo.

 - existen las mismas condiciones de propagación desde la fuente al
punto de recepción., y

 - la distancia d a partir de una fuente puntual equivalente al receptor
excede dos veces la mayor dimensión H [max] de la fuente (d>2 H [max] ).

Si la distancia d es menor (d< H max ), o si las condiciones de propagación
para los componentes de la fuente puntual son diferentes (debido a una
barrera, por ejemplo), la fuente sonora total debería ser dividida en
componentes de fuentes puntuales.

Nota 4: En suma la condición real de las fuentes descrita arriba, se deen
incluir fuentes imágenes para describir las reflexiones de sonido de
muros y techos (pero no del suelo), como se describe en 7.5.

**5 Condiciones Meteorológicas**

Las condiciones de propagación downwind para el método especificado
en esta parte de ISO 9613 son mostradas en la sección 5.4.3.3 de ISO 1996-2:
1987, es decir:

 - dirección del viento dentro de un ángulo de ± 45° de la dirección
conteniendo el centro de fuente sonora dominante y el centro de la
región receptora especificada, con el viento soplando desde la fuente
hacia el receptor,

 - la velocidad del viento entre aproximadamente 1m/s y 5 m/s,
medido a una altura de entre 3m y 11m. sobre el suelo.

Las ecuaciones para calcular el promedio de nivel de presión sonora
downwind L [AT] (DW) en esta parte de ISO 9613., incluyendo las ecuaciones para

la atenuación dadas en la cláusula 2 dentro de este límite. El término

promediado aquí, recurre al promedio sobre un corto intervalo de tiempo,
como se define en 3.1.

Estas ecuaciones además mantienen, equivalentemente, para el
promedio de propagación bajo una inversión de temperatura del suelo
moderada, tal como ocurre comúnmente en las noches.

**6 Ecuaciones básicas**

El nivel de presión sonora continuo equivalente por bandas de octava
downwind, L fT (DW), debe ser calculado para cada fuente puntual y sus fuentes
imagen, y por cada banda de octava con la frecuencia central nominal desde 63
Hz y hasta 8kHz a partir de la ecuación (3):

L fT (DW) = L w + D c - A ...(3)

donde:

L w es el nivel de potencia sonora por bandas de octava, en decibeles,
producido por la fuente sonora puntual relativo a una potencia
sonora de referencia de 1 picowatt (1pW);
D [c] es la corrección por directividad, en decibeles, esto describe la
extensión por la cual el nivel de presión sonora continuo
equivalente a partir de una fuente puntual desvía en una dirección
específica a partir del nivel de una fuente sonora puntual
omnidireccional produciendo un nivel de potencia sonora L [w], D [c] es
igual al índice de directividad D i de una fuente puntual más un
índice D Ο acorde con la propagación de sonido en ángulos sólidos
menores que 4 π estereoradianes; para una fuente puntual
omnidireccional radiando en el espacio libre, D [c] = o dB;
A es la atenuación por bandas de octava, en decibeles, esta ocurre
durante la propagación desde una fuente sonora puntual hasta el

receptor.

Notas

5 La letra A significa atenuación en esta parte de ISO 9613 excepto en
subíndices, donde indica ponderación A de frecuencia.
6 Los niveles de potencia sonora en la ecuación (3) pueden ser
determinados a partir de mediciones, por ejemplo como se describe en
ISO 3740(para maquinaria) o en ISO 8297 (para industriales).

El termino de atenuación A en la ecuación (3) esta dado por la ecuación (4):

A = A div + A atm + A gr +A bar + A misc

donde

A div atenuación debido a la divergencia geométrica (ver 7.1);

A [atm] atenuación debido a la absorción atmosférica (ver 7.2);
A gr atenuación por efecto del suelo (ver 7.3);
A bar atenuación por efecto de barreras (ver 7.4);
A misc atenuación por otros efectos similares (ver anexo A).

El método general para calcular los primeros cuatro términos en la
ecuación (4) son especificados en esta parte de ISO 9613. Información de tres
tipos contribuciones al último término, A misc (la atenuación debido a la
propagación a través de bosque, sitios industriales y áreas habitacionales), esta
dada en el anexo A.

El nivel de presión sonora continuo equivalente downwind ponderado
A se obtiene sumando las contribuciones de presión sonora time mean square
calculadas de acuerdo a las ecuaciones (3) y (4) para cada fuente sonora
puntual, para cada fuente imagen y para cada banda de octava, como se
especifica en la ecuación (5):

donde

n es el número de contribuciones i (fuentes y caminos);
j es un índice que indica en octavo estándar de frecuencia
central por octava desde 63 Hz hasta 8kHz;
A f denota la poderación A estandarizada (ver IEC 651).

El término promedio de nivel de presión sonora ponderado A L [AT] (LT) debe
ser calculado de acuerdo a:

L AT (LT) = L AT (DW) - C met ....(6)

donde C met es la corrección meteorológica descrita en la cláusula 8.
El cálculo y significado de varios términos en las ecuaciones (1) a la (6)
son explicados en las siguientes cláusulas. Para un tratamiento más detallado
de los términos de atenuación, ver la literatura de referencia dada en el anexo

B.

**7 Cálculo de términos de atenuación**

7.1 Divergencia geométrica (A div )
La divergencia geométrica ocurre para propagación esférica en el
espacio libre desde una fuente sonora puntual, haciendo la atenuación, en
decibeles, igual a:

A [div] = 20 log (d/d [0] ) + 11 dB .....(7)

donde

d es la distancia desde la fuente al receptor, en metros;
d [0] es la distancia de referencia (=1 m).

Nota 7 La constante en la ecuación 7relaciona al nivel de potencia sonora
al nivel de presión sonora a una distancia de referencia d 0 la cual es de 1 m.
para una fuente sonora omnidireccional puntual.

**7.2** Absorción atmosférica (A atm )
La atenuación debido a la absorción atmosférica A atm, en decibeles,
durante la propagación a través de una distancia d, en metros, está dada por la
ecuación (8):

A atm = α d/1000 ...(8)

donde α es la coeficiente de atenuación atmosférica, en decibeles por
kilometro, para cada banda de octava en la frecuencia central (ve r tabla 2).
Para valores de α en condiciones no cubiertas en la tabla 2, ver ISO 9613-1.

Notas

|Notas 8 el coeficiente se atenuación atmosférica depende fuertemente de la frecuencia de sonido, la temperatura ambiente y humedad relativa del aire, pero débilmente de la presión ambiente. 9 para calcular el nivel de ruido ambiental, el coeficiente de atenuación atmosférica se debe basar en valores promedio determinados por el rango del tiempo ambiental el cual es relevante para el lugar. Coeficiente de absorción atmosférica [dB/km]|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|
|---|---|---|---|---|---|---|---|---|---|
|<br>Coeficiente de absorción atmosféricaα [dB/km]|<br>Coeficiente de absorción atmosféricaα [dB/km]|<br>Coeficiente de absorción atmosféricaα [dB/km]|<br>Coeficiente de absorción atmosféricaα [dB/km]|<br>Coeficiente de absorción atmosféricaα [dB/km]|<br>Coeficiente de absorción atmosféricaα [dB/km]|<br>Coeficiente de absorción atmosféricaα [dB/km]|<br>Coeficiente de absorción atmosféricaα [dB/km]|<br>Coeficiente de absorción atmosféricaα [dB/km]|<br>Coeficiente de absorción atmosféricaα [dB/km]|
|Temperatura|Humedad<br>Relativa|Frecuencia central nominal [Hz]|Frecuencia central nominal [Hz]|Frecuencia central nominal [Hz]|Frecuencia central nominal [Hz]|Frecuencia central nominal [Hz]|Frecuencia central nominal [Hz]|Frecuencia central nominal [Hz]|Frecuencia central nominal [Hz]|
|°C|%|63|125|250|500|1000|2000|4000|8000|
|10|70|0,1|0,4|1,0|1,9|3,7|9,7|32,8|117|
|20|70|0,1|0,3|1,1|2,8|5,0|9,0|22,9|76,6|
|30|70|0,1|0,3|1,0|3,1|7,4|12,7|23,1|59,3|
|15|20|0,3|0,6|1,2|2,7|8,2|28,2|88,8|202|
|15|50|0,1|0,5|1,2|2,2|4,2|10,8|36,2|129|
|15|80|0,1|0,3|1,1|2,4|4,1|8,3|23,7|82,8|

7.3 Efecto del suelo (A gr )
7.3.1 Método general de cálculo
La atenuación, A [gr], es principalmente el resultado del sonido reflejado
por la superficie del suelo que interfiere con la propagación de sonido
directamente desde la fuente al receptor.
El camino de propagación downwind-curving, asegura que esta
atenuación es determinada principalmente por la superficie del suelo cercana a
la fuente y cerca al receptor. Este método de cálculo del efecto del suelo el
aplicable solamente al suelo que es aproximadamente plano, o
horizontalmente o con una pendiente constante. Se especifican tres distintas
regiones para la atenuación de sonido (ver figura 1):

a) región de la fuente, extendida sobre una distancia desde la fuente hacia el
receptor de 30h s, con un máximo de distancia de d p (h s es la altura de la
fuente, y d [p] la distancia desde la fuente al receptor, como proyectado sobre
el plano);
b) región del receptor, extendida sobre la distancia desde el receptor hacia la
fuente de 30 h r, con un máximo de distancia de d p (h r es la altura del
receptor);
c) región media, extendida sobre la distancia entre la región de la fuente y del
receptor. Si d p < (30 h s + 30h r ), las regiones de fuente y receptor están sobre
estimadas y no existe región media.

De acuerdo con este esquema, la atenuación del suelo no se incrementa
con el tamaño de la región media pero es más dependiente de las propiedades
de las regiones de fuente y receptor. Las propiedades acústicas de cada región
de suelo son tomadas en cuenta a través de un factor G. Se especifican tres
categorías de superficies reflectantes, estas son:

a) Suelo duro, incluye pavimentos, agua hielo, concreto y otros tipos de
superficie que tengan baja porosidad. Mezclas de suelo, como generalmente
ocurre en sitios industriales, pueden ser considerados duros. Para suelos

duros G = o.

Nota 10 Hay que resaltar que las condiciones de inversión sobre agua no
son cubiertas por esta parte de ISO 9613.

b) Suelo poroso, incluye suelo cubierto por pasto, árboles u otro tipo de
vegetación, y todo tipo de suelo adecuado para el crecimiento de
vegetación, tal como las tierras de cultivo. Para suelos porosos G = 1.
c) Suelo mixto, si la superficie consiste de suelos duros y porosos, entonces G
toma en valor entre 0 y 1, siendo este valor la fracción de la región porosa.

Para calcular la atenuación del suelo para una banda de octava
específica, primero se calcula el componente de atenuación A s para la región
fuente especificada por el factor G s (para esta región), A r para la región
especificada por el factor G r, y A m para la región media entre especificada por
el factor G [m], usando las expresiones de la tabla 3. (Alternativamente, las

<!-- INICIO TABLA 3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- A gr = A s + A r +A m .... (9) Nota 11 en zonas con edificios, la influencia del suelo en la propagación de sonido puede ser cambiada (ver A3). -->

**Tabla 3: - Expresiones usadas para calcular la contribución de atenuación de****

| Frecuencia central<br>nominal [Hz] | A o A 1) dB<br>s r | A dB<br>m |
| --- | --- | --- |
| 63 | -1,5 | -3q2) |
| 125 | -1,5 + G x a ́(h) | <br> <br> <br>-3q ( 1 - Gm) <br> <br> <br> |
| 250<br>500 | -1,5 + G x b ́(h)<br>-1,5 + G x c ́(h) | -1,5 + G x b ́(h)<br>-1,5 + G x c ́(h) |
| 1000 | -1,5 + G x d(h) | -1,5 + G x d(h) |
| 2000 | -1,5 (1 - G) | -1,5 (1 - G) |
| 4000 | -1,5 (1 - G) | -1,5 (1 - G) |
| 8000 | -1,5 (1 - G) | -1,5 (1 - G) |
| NOTAS<br>a ́(h) = 1,5 + 3,0 e-0,12(h-5))h -5) (1- e-dp/50) + 5,7 e-0,09 h h( 1 - e-2,8 x 10 -6 x dp x dp) <br> <br>b ́(h) = 1,5 + 8,6 e-0,09 h h ( 1 - e -dp/50) <br> <br>c ́(h) = 1,5 + 14,0 e -0,9 h h( 1 - e-dp/50) <br> <br>d ́(h) = 1,5 + 5,0 e-0,9 h h (1 - e-dp/50) | NOTAS<br>a ́(h) = 1,5 + 3,0 e-0,12(h-5))h -5) (1- e-dp/50) + 5,7 e-0,09 h h( 1 - e-2,8 x 10 -6 x dp x dp) <br> <br>b ́(h) = 1,5 + 8,6 e-0,09 h h ( 1 - e -dp/50) <br> <br>c ́(h) = 1,5 + 14,0 e -0,9 h h( 1 - e-dp/50) <br> <br>d ́(h) = 1,5 + 5,0 e-0,9 h h (1 - e-dp/50) | NOTAS<br>a ́(h) = 1,5 + 3,0 e-0,12(h-5))h -5) (1- e-dp/50) + 5,7 e-0,09 h h( 1 - e-2,8 x 10 -6 x dp x dp) <br> <br>b ́(h) = 1,5 + 8,6 e-0,09 h h ( 1 - e -dp/50) <br> <br>c ́(h) = 1,5 + 14,0 e -0,9 h h( 1 - e-dp/50) <br> <br>d ́(h) = 1,5 + 5,0 e-0,9 h h (1 - e-dp/50) |
| 1) Para calcular As,tomamos G = Gs y h = hs.Para calcular Ar tomamos G = Gr y<br>h = hr. Ver 7.3.1 para valores de G para varios superficies de suelo.<br>2) q = 0 donde dp < 30 (hs + hr) <br> <br> q = 1- 30(hs + hr)/dp donde dp > 30 (hs + hr) <br> <br> donde dp es la distancia fuente receptor, en metros, proyectado en el plano<br>del suelo. | 1) Para calcular As,tomamos G = Gs y h = hs.Para calcular Ar tomamos G = Gr y<br>h = hr. Ver 7.3.1 para valores de G para varios superficies de suelo.<br>2) q = 0 donde dp < 30 (hs + hr) <br> <br> q = 1- 30(hs + hr)/dp donde dp > 30 (hs + hr) <br> <br> donde dp es la distancia fuente receptor, en metros, proyectado en el plano<br>del suelo. | 1) Para calcular As,tomamos G = Gs y h = hs.Para calcular Ar tomamos G = Gr y<br>h = hr. Ver 7.3.1 para valores de G para varios superficies de suelo.<br>2) q = 0 donde dp < 30 (hs + hr) <br> <br> q = 1- 30(hs + hr)/dp donde dp > 30 (hs + hr) <br> <br> donde dp es la distancia fuente receptor, en metros, proyectado en el plano<br>del suelo. |

<!-- Estadísticas: 9 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- 7.3.2 Método alternativo de cálculo para niveles de presión sonora ponderadoA. Bajo las siguientes condiciones específicas: -->
<!-- FIN TABLA 3 -->

funciones a ́,b ́,c ́ y d ́ en la tabla 3 puede ser obtenida directamente desde las
curvas de la figura 2). La atenuación total para bandas de octava debe ser
obtenida de la ecuación (9):

A gr = A s + A r +A m .... (9)

Nota 11 en zonas con edificios, la influencia del suelo en la propagación
de sonido puede ser cambiada (ver A3).

**Tabla 3 - Expresiones usadas para calcular la contribución de atenuación de**
**suelo A** **s** **, A** **r** **, y A** **m** **en bandas de octava.**

|Frecuencia central<br>nominal [Hz]|A o A 1) dB<br>s r|A dB<br>m|
|---|---|---|
|63|-1,5|-3q2)|
|125|-1,5 + G x a ́(h)|<br> <br> <br>-3q ( 1 - Gm) <br> <br> <br>|
|250<br>500|-1,5 + G x b ́(h)<br>-1,5 + G x c ́(h)|-1,5 + G x b ́(h)<br>-1,5 + G x c ́(h)|
|1000|-1,5 + G x d(h)|-1,5 + G x d(h)|
|2000|-1,5 (1 - G)|-1,5 (1 - G)|
|4000|-1,5 (1 - G)|-1,5 (1 - G)|
|8000|-1,5 (1 - G)|-1,5 (1 - G)|
|NOTAS<br>a ́(h) = 1,5 + 3,0 e-0,12(h-5))h -5) (1- e-dp/50) + 5,7 e-0,09 h h( 1 - e-2,8 x 10 -6 x dp x dp) <br> <br>b ́(h) = 1,5 + 8,6 e-0,09 h h ( 1 - e -dp/50) <br> <br>c ́(h) = 1,5 + 14,0 e -0,9 h h( 1 - e-dp/50) <br> <br>d ́(h) = 1,5 + 5,0 e-0,9 h h (1 - e-dp/50)|NOTAS<br>a ́(h) = 1,5 + 3,0 e-0,12(h-5))h -5) (1- e-dp/50) + 5,7 e-0,09 h h( 1 - e-2,8 x 10 -6 x dp x dp) <br> <br>b ́(h) = 1,5 + 8,6 e-0,09 h h ( 1 - e -dp/50) <br> <br>c ́(h) = 1,5 + 14,0 e -0,9 h h( 1 - e-dp/50) <br> <br>d ́(h) = 1,5 + 5,0 e-0,9 h h (1 - e-dp/50)|NOTAS<br>a ́(h) = 1,5 + 3,0 e-0,12(h-5))h -5) (1- e-dp/50) + 5,7 e-0,09 h h( 1 - e-2,8 x 10 -6 x dp x dp) <br> <br>b ́(h) = 1,5 + 8,6 e-0,09 h h ( 1 - e -dp/50) <br> <br>c ́(h) = 1,5 + 14,0 e -0,9 h h( 1 - e-dp/50) <br> <br>d ́(h) = 1,5 + 5,0 e-0,9 h h (1 - e-dp/50)|
|1) Para calcular As,tomamos G = Gs y h = hs.Para calcular Ar tomamos G = Gr y<br>h = hr. Ver 7.3.1 para valores de G para varios superficies de suelo.<br>2) q = 0 donde dp < 30 (hs + hr) <br> <br> q = 1- 30(hs + hr)/dp donde dp > 30 (hs + hr) <br> <br> donde dp es la distancia fuente receptor, en metros, proyectado en el plano<br>del suelo.|1) Para calcular As,tomamos G = Gs y h = hs.Para calcular Ar tomamos G = Gr y<br>h = hr. Ver 7.3.1 para valores de G para varios superficies de suelo.<br>2) q = 0 donde dp < 30 (hs + hr) <br> <br> q = 1- 30(hs + hr)/dp donde dp > 30 (hs + hr) <br> <br> donde dp es la distancia fuente receptor, en metros, proyectado en el plano<br>del suelo.|1) Para calcular As,tomamos G = Gs y h = hs.Para calcular Ar tomamos G = Gr y<br>h = hr. Ver 7.3.1 para valores de G para varios superficies de suelo.<br>2) q = 0 donde dp < 30 (hs + hr) <br> <br> q = 1- 30(hs + hr)/dp donde dp > 30 (hs + hr) <br> <br> donde dp es la distancia fuente receptor, en metros, proyectado en el plano<br>del suelo.|

7.3.2 Método alternativo de cálculo para niveles de presión sonora
ponderadoA.
Bajo las siguientes condiciones específicas:

 - solo niveles de presión sonora ponderado A en la posición del
receptor de interés.

 - la propagación de sonido ocurre sobre suelo poroso o suelo mixto
que en su mayor parte es poroso. (ver 7.3.1)

 - el sonido no es un tono puro.

y para suelos de cualquier forma, la atenuación puede ser calculada por la
ecuación (10):

A [gr] = 4,8 - (2h [m] /d) [ 17 + (300/d)] > o dB ...(10)

donde

h m es la altura media del camino de propagación sobre el suelo, en

metros;
d distancia desde la fuente al receptor, en metros.
La altura media h m puede ser evaluada por el método mostrado en la
figura 3. Los valores negativos para A gr de la ecuación (10) deben ser
reemplazados por ceros.

Nota 12 para distancias cortas, la ecuación (10) no predice atenuación y
la ecuación (9) puede ser más exacta.

Cuando el efecto del suelo es calculado usando la ecuación (10), la
corrección de directividad D c en la ecuación (3) debe incluir el término D Ο, en
decibeles, para considerar el aparente incremento de atenuación en el nivel de
potencia sonora de la fuente debido a reflexiones desde el suelo cercano a la
fuente.

D Ο = 10 log { 1 + [d p [2] + (h s - h r ) [2] ] / [d p [2] +(h s + h r ) [2] ] } dB ...(11)

donde

h s altura de la fuente sobre el suelo, en metros;
h r altura del receptor sobre el suelo, en metros;
d [p] distancia fuente - receptor proyectada en el plano del suelo, en

metros.

7.4 Apantallamiento (A [bar] )
Un objeto debe ser tomado en cuenta como un obstáculo de
apantallamiento (barrera) si cumple con los siguientes requerimientos:

- densidad superficial de al menos 10 Kg/m [2],

- el objeto tiene una superficie cerrada sin grandes grietas o huecos

- la dimensión horizontal del objeto normal a la línea fuente - receptor es
mayor que la longitud de onda λ en la frecuencia dentral nominal de cada
banda de frecuencia de interés; en otras palabras l l + l r - λ ( ver figura 4).

Cada objeto que cumpla con estos requerimientos debe ser representado
por una barrera con bordes verticales. El borde tope de la barrera es una fuerte
línea que puede tener pendiente.
Para propósitos de esta parte de ISO 9613, la atenuación por una barrera,
A [bar], está dada por la pérdida de inserción. La difracción sobre el tope de la
barrera y alrededor de los bordes verticales de una barrera pueden ser de
importancia. (ver figura 5). Para propagación de sonido downwind, el efecto de
la difracción (en decibeles) sobre el tope es calculado por:

A bar = D z - A gr - 0 ...(12)

y para la difracción alrededor de el borde vertical por

A bar = D z - 0

donde

D z atenuación para cada banda de octava (ver ecuación (14));
A [gr] atenuación del suelo en ausencia de la barrera (es decir con el
objeto apantallador removido) (ver 7.3).

Notas

13 cuando A [bar] definida por la ecuación (12) es sustituida en la ecuación
(4) para encontrar la atenuación total A, los dos términos A gr en la
ecuación (4) son cancelados. La atenuación de la barrera D z en la
ecuación (12) entonces incluye el efecto del suelo en presencia de la

barrera.

14 para distancias mayores y barreras altas, la pérdida por inserción
calculada por la ecuación (12) no es suficientemente confirmada por

mediciones.

15 en cálculos de pérdida por inserción plantas industriales multifuentes
por construcciones altas (más de 10 m. sobre el nivel de suelo), y además
para fuentes de ruido elevado dentro de la planta, la ecuación (13) debe
ser usada en ambos casos para determinar el long term de nivel de
presión sonora promedio (usando la ecuación (6)).
16 para sonido proveniente de una carretera deprimida, esto puede ser
atenuación en suma con lo indicado por la ecuación (12) a lo largo de la
superficie del suelo fuera de la depresión, debido a esta superficie de

suelo.

Para calcular la atenuación de la barrera D z, se asume que existe
solamente un camino significante de propagación de sonido desde la fuente
sonora hasta el receptor. Si esta presunción no es valida, se necesitan cálculos
separados para otros caminos de propagación (como se ilustra en la figura 5) y

se asume la contribución a partir de varios caminos a la presión sonora al
cuadrado en el receptor.
La atenuación de la barrera D z, en decibeles, debe ser calculada para este
camino por la ecuación (14):

D z = 10 log [3+(C 2 / λ )C 3 zK met ] dB ...(14)

donde

C [2 ] es igual a 20, e incluye el efecto de reflexiones del suelo; si se
toman en cuenta casos especial de reflexiones del suelo
separadamente por fuentes imagen, C 2 = 40;
C 3 es igual a 1 para una difracción simple (ver figura 6);

C 3 = [1+(5 λ /e [2] ]/[(1/3) + (5 λ/ e ) [2] ] ...(15)

para doble difracción (ver ecuación 7);
λ longitud de onda del sonido de la frecuencia central nominal de
cada banda de octava, en metros;
z es la diferencia de camino entre el sonido directo y difractado,
calculado por la ecuación (16( y (17), en metros.
K [met] factor de corrección por efectos meteorológicos, dado por la
ecuación (18):

e distancia entre los dos bordes de difracción en caso de difracción

doble (ver figura 7)

Para una difracción, como se muestra en la figura 6, la diferencia de
camino z se debe calcular por medio de la ecuación (16):

z = [(d [ss] +d [sr] ) [2] + a [2] ] - d ...(16)

donde

d ss es la distancia desde la fuente al primer borde de difracción, en

metros;
d sr distancia desde el borde de difracción (segundo) al receptor, en

metros;
a componente de distancia paralelo al borde de la barrera entre la
fuente y el receptor, en metros.

Si la línea de vista entre la fuente S y el receptor R pasa por sobre el tope
del borde de la barrera, z da un número negativo.
Para doble difracción, como se muestra en la figura 7, la diferencia de
camino z debe ser calculado por:

z = [(d ss + d sr + e) [2] + a [2] ] [1/2] - d ....(17)

El factor de corrección K [met] para condiciones meteorológicas en la
ecuación (14) debe ser calculado usando la ecuación (18):

para z > 0

K met = 1 para z < 0 ...(18)

Para la difracción por los bordes de los obstáculos, se asume el factor
K [met ] = 1 (ver figura 5).

Notas

17 Para distancias fuente receptor menores que 100 m. el cálculo
utilizando la ecuación (14) muestra que K [met] puede ser asumido como 1,
para un precisión de 1 dB.
18 La ecuación (5) proporciona una transición continua desde el caso de
difracción simple (e=0) donde C 3 = 1, esto es para una difracción doble
bien separada (e>> λ ) donde C [3] = 3.
19 Una barrera puede ser menos efectiva que la calculada por las
ecuaciones (12) y (18) como resultado de reflexiones desde otras
superficies acústicamente duras cercanas al camino de la fuente desde la
fuente al receptor o por reflexiones múltiples entre y una barrera
acústicamente dura y la fuente.

La atenuación por la barrera D z en cualquier banda, no debe ser tomada
como mayor de 20 dB en el caso de una sola difracción (barreras delgadas) y 25
dB en el caso de doble difracción (barreras gruesas).
La atenuación para dos barreras es calculada usando la ecuación (14)
para doble difracción, como se indica en la parte baja de la figura 7. La
atenuación para más de dos barreras puede ser calculada aproximadamente
usando la ecuación (14), eligiendo las dos barreras mas efectivas, despreciando

los efectos de las otras.

7.5 Reflexiones

Aquí las reflexiones son consideradas en términos de fuentes imagen.
Estas reflexiones provienen de cielos abiertos o superficies más o menos
verticales, tales como fachadas de edificios, las cuales pueden incrementar el
nivel de presión sonora en el receptor. El efecto de reflexiones desde el suelo
no son incluidas porque ellas están en el cálculo de A gr .
Las reflexiones desde un obstáculo deben ser calculadas para todas las
bandas de octava para las cuales los siguientes requerimientos se cumplen:

 - Una reflexión specular se puede construir, como se muestra en la
figura 8;

 - La magnitud del coeficiente de reflexión sonora para la superficie de
un obstáculo es mayor que 0,2;

 - La superficie es mayor

donde
λ es la longitud de onda (en metros) de la frecuencia central
nominal f (en hertz) de la banda de octava;
d s,o distancia entre la fuente y el punto de reflexión del obstáculo;
d o,r distancia entre el punto de reflexión en el obstáculo y el receptor;
β ángulo de incidencia, en radianes (ver figura 8);
l min dimensión mínima (altura o longitud) de la superficie reflectante
(ver figura 8).

Si cualquiera de estas condiciones no se cumple para una banda de
octava dada, la reflexión puede ser despreciada.
La fuente real y la fuente imaginaria son tratadas en forma separada. El
nivel de potencia sonora de la fuente imagen L w,mi es calculado por:

L w,mi = L w + 10 log ( ρ ) dB + D ir

donde
ρ coeficiente de reflexión de sonido a un ángulo β en la superficie
del obstáculo (> 0,2).
D ir índice de directividad de la fuente en dirección del receptor
imagen.

Si no hay datos específicos del coeficiente de reflexión de sonido, el

valor debe ser estimado usando la tabla 4.

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Para la fuente sonora imagen, los términos de atenuación de la ecuación (4), así como ρ D [ir] en la ecuación (20), serán determinados de acuerdo al camino de propagación del sonido reflejado. -->

**Tabla 4: - Estimación del coeficiente de reflexión sonora** **ρ** .**

| Col1 | Φ es el suplemento del ángulo entre<br>las líneas SC y CR. |
| --- | --- |
| Instalaciones abiertas (pipes, torres, etc) | 0 |
| * Estas expresiones se aplican solamente si la distancia dsc desde la fuente S al<br>cilindro C es mucho mayor que la distancia d cr desde el cilindro al receptor, ver<br>figura 9. | * Estas expresiones se aplican solamente si la distancia dsc desde la fuente S al<br>cilindro C es mucho mayor que la distancia d cr desde el cilindro al receptor, ver<br>figura 9. |

<!-- Estadísticas: 2 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- **8 Corrección Meteorológica (C** **met** **)** Usando la ecuación (3) se obtienen directamente un nivel de presión sonora continuo equivalente ponderado A, L [AT] en el receptor para condiciones -->
<!-- FIN TABLA 4 -->


Para la fuente sonora imagen, los términos de atenuación de la ecuación
(4), así como ρ D [ir] en la ecuación (20), serán determinados de acuerdo al camino
de propagación del sonido reflejado.

**Tabla 4 - Estimación del coeficiente de reflexión sonora** **ρ** .

|Objetos|ρ|
|---|---|
|Paredes planas duras.|1|
|Paredes de edificios con ventanas y<br>pequeños agregados.|0,8|
|Paredes de industrias con 50% de la<br>superficie de abertura, instalaciones o<br>pipes|0,4|
|Cilindros<br>con<br>superficies<br>duras<br>(tanques, silos)|(D seno (Φ/2))*/(2dsc) <br> <br>donde:<br>D es el diámetro del cilindro;<br>dsc es la distancia desde la fuente al<br>centro C del cilindro;|

|Col1|Φ es el suplemento del ángulo entre<br>las líneas SC y CR.|
|---|---|
|Instalaciones abiertas (pipes, torres, etc)|0|
|* Estas expresiones se aplican solamente si la distancia dsc desde la fuente S al<br>cilindro C es mucho mayor que la distancia d cr desde el cilindro al receptor, ver<br>figura 9.|* Estas expresiones se aplican solamente si la distancia dsc desde la fuente S al<br>cilindro C es mucho mayor que la distancia d cr desde el cilindro al receptor, ver<br>figura 9.|

**8 Corrección Meteorológica (C** **met** **)**

Usando la ecuación (3) se obtienen directamente un nivel de presión
sonora continuo equivalente ponderado A, L [AT] en el receptor para condiciones
meteorológicas las cuales son favorables para la propagación desde la fuente
sonora al receptor, como se describe en la cláusula 5. Esta puede ser la
condición apropiada para encontrar un límite de ruido comunitario específico,
es decir, un límite que raramente sea excedido (ver ISO 1996-3). A menudo sin
embargo, se necesita un nivel de presión sonora ponderado A promedio
L AT (LT), cuando el intervalo de tiempo T es de varios meses o un año. Tales
períodos de tiempo incluyen normalmente una variedad de condiciones
meteorológicas, ambas favorables y desfavorables a la propagación. Se puede
obtener un valor para L AT (LT) en esta situación a partir del cálculo de L AT (DW)
por la ecuación (3), usando la corrección meteorológica C met en la ecuación (6).
Un valor (en decibeles) para C [met] en la ecuación (6) puede ser calculado
usando la ecuación (21) y (22) para cada caso de fuente puntual con una salida
que efectivamente constante en el tiempo:

C [met ] = 0 ...(21)

si d p < 10 (h s + h r )

C [met] = C [0 ] [1 - 10(h [s] - h [r] )/d [p] ] ...(22)

si d p - 10 (hs + h r )

donde

h s altura de la fuente, en metros;
h r altura del receptor, en metros;
d [p] distancia entre la fuente y el receptor proyectado en el plano
horizontal del suelo, en metros;
C 0 factor, en decibeles, que depende de las estadísticas
meteorológicas locales para velocidad y dirección del viento, y
gradientes de temperatura.

El efecto de las condiciones meteorológicas en la propagación del
sonido son pequeñas para distancias cortas d p, y para distancias mas largas y a
mayores alturas de fuente y receptor. Las ecuaciones (21) y (22) aproximan
estos factores, como se muestra en la figura 10.

**9 Precisión y limitaciones del método**

La atenuación de la propagación de sonido en exteriores entre una
mezcla de fluctuaciones del receptor y de la fuente debido a variaciones en las
condiciones meteorológicas a lo largo del camino de propagación. Si nos
restringimos a condiciones de propagación downwind moderadas, como se
específica en la cláusula 5, el límite del efecto de las condiciones
meteorológicas variables en la atenuación para valores razonables.
Esta es información para apoyar el método de cálculo dado en las
cláusulas 4 a la 8 (ver anexo B) para fuentes de ruido de banda ancha. El
comportamiento entres los valores medidos y calculados de en nivel de
presión sonora ponderado A promedio, L AT (DW), respalda la precisión
estimada por los cálculos mostrados en la tabla. Estas estimaciones de
precisión son restringidas a un rango de condiciones especificadas por la
validez de las ecuaciones en las cláusulas 3 a la 8 y son independientes de
incertezas en la determinación de potencia sonora.

Nota 24 Las estimaciones de precisión en la tabla 5 son para condiciones
downwind promedio sobre situaciones independientes (como se
especifica en la cláusula 5). Ellas no deberían necesariamente ser
especificadas para agree con la variación en metros hechas en un lugar
dado en un día dado. Lo posterior puede ser considerablemente mayor
que los valores de la tabla 5.

<!-- INICIO TABLA 5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Estos son además un sustancial número de limitaciones (no - meteorológicas) en el uso de ecuaciones individuales. La ecuación (8) es, por ejemplo, limitado a terrenos aproximadamente planos. Estas específicas limitaciones son descritas en el texto que acompaña la ecuación relevante. -->

**Tabla 5: - Precisión estimada para ruidos de banda ancha de L** **AT** **(DW)****

| Altura, h* | Distancia, d*<br>0 < d < 100 m. 100 m. < d < 1000 m. | Col3 |
| --- | --- | --- |
| 0 < h < 5 m.<br>5m < h < 30m. | 3 dB<br>1 dB | 3 dB<br>3 dB |
| * h es la altura media de la fuente y el receptor.<br> d es la distancia entre la fuente y el receptor. | * h es la altura media de la fuente y el receptor.<br> d es la distancia entre la fuente y el receptor. | * h es la altura media de la fuente y el receptor.<br> d es la distancia entre la fuente y el receptor. |
| NOTA: Estas estimaciones han sido hechas a partir de situaciones donde no<br>hay efectos debido a reflexiones o atenuaciones debido al apantallamiento. | NOTA: Estas estimaciones han sido hechas a partir de situaciones donde no<br>hay efectos debido a reflexiones o atenuaciones debido al apantallamiento. | NOTA: Estas estimaciones han sido hechas a partir de situaciones donde no<br>hay efectos debido a reflexiones o atenuaciones debido al apantallamiento. |

<!-- Estadísticas: 3 filas, 3 columnas -->
<!-- FIN TABLA 5 -->


Los errores estimados en los cálculos del promedio de nivel de presión
sonora por bandas de octava, así como el nivel de presión para tonos puros,
bajo las mismas condiciones, puede ser aveces mayor que el error estimado
dado para niveles de presión sonora ponderado A de fuentes de ruido de

banda ancha en la tabla 5.

En la tabla 5 no se estima precisión para esta parte de ISO 9613 para distancias
d mayores de 1000m sobre el límite.
Por medio de esta parte de ISO 9613 las condiciones meteorológicas bajo

consideraciones son limitadas a solamente dos casos:

a) condiciones downwind moderadas de propagación, o su equivalente, como
se define en la cláusula 5;
b) una variedad de condiciones meteorológicas as they exist sobre meses o

años.

El uso de las ecuaciones (1) a la (5) y (7) a la (20) (y por lo tanto también la tabla
5) está limitada a los casos:
a) condiciones meteorológicas solamente
b) es relevante solo el uso de las ecuaciones (6), (21) y (22).

Estos son además un sustancial número de limitaciones (no - meteorológicas)
en el uso de ecuaciones individuales. La ecuación (8) es, por ejemplo, limitado
a terrenos aproximadamente planos. Estas específicas limitaciones son
descritas en el texto que acompaña la ecuación relevante.

**Tabla 5 - Precisión estimada para ruidos de banda ancha de L** **AT** **(DW)**

**calculado usando las ecuaciones (1) a la (10).**

|Altura, h*|Distancia, d*<br>0 < d < 100 m. 100 m. < d < 1000 m.|Col3|
|---|---|---|
|0 < h < 5 m.<br>5m < h < 30m.|3 dB<br>1 dB|3 dB<br>3 dB|
|* h es la altura media de la fuente y el receptor.<br> d es la distancia entre la fuente y el receptor.|* h es la altura media de la fuente y el receptor.<br> d es la distancia entre la fuente y el receptor.|* h es la altura media de la fuente y el receptor.<br> d es la distancia entre la fuente y el receptor.|
|NOTA: Estas estimaciones han sido hechas a partir de situaciones donde no<br>hay efectos debido a reflexiones o atenuaciones debido al apantallamiento.|NOTA: Estas estimaciones han sido hechas a partir de situaciones donde no<br>hay efectos debido a reflexiones o atenuaciones debido al apantallamiento.|NOTA: Estas estimaciones han sido hechas a partir de situaciones donde no<br>hay efectos debido a reflexiones o atenuaciones debido al apantallamiento.|