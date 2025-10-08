---
title: Sin título
author: Sergio Arriaza
date: D:20240702072126-04'00'
language: es
type: general
pages: 41
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Anexo 1.4 Estudio de Campos Electromagnéticos
-->

# Anexo 1.4 Estudio de Campos Electromagnéticos

## Parque Fotovoltaico Nueva Paillaco

Código P446-E-EST-01

Revisión A

Preparado por Sergio Arriaza Sánchez

Preparado para IM2 Solar

Emisión 09-04-2024

Estudio de Campos Electromagnéticos Rev. A

### Tabla de contenidos

1 Introducción ..................................................................................................................................... 4

2 Objetivos .......................................................................................................................................... 5

2.1 Línea de base ........................................................................................................................................ 5

2.2 Simulación de campos electromagnéticos .......................................................................................... 5

3 Metodología ..................................................................................................................................... 6

3.1 Cálculo del campo eléctrico .................................................................................................................. 6

3.2 Cálculo del campo magnético .............................................................................................................. 9

4 Línea de base ................................................................................................................................. 12

4.1 Mediciones puntuales ......................................................................................................................... 12

5 Modelación..................................................................................................................................... 17

5.1 Línea de distribución de 13,2 kV ....................................................................................................... 17

5.1.1 Características de la instalación .................................................................................................... 17

5.1.2 Cálculo del campo eléctrico ........................................................................................................... 19

5.1.3 Cálculo del campo magnético ........................................................................................................ 20

5.3 Línea de distribución soterrada 13,2 kV ............................................................................................ 21

5.3.1 Características de la instalación .................................................................................................... 21

5.3.2 Cálculo del campo eléctrico ........................................................................................................... 22

5.3.3 Cálculo del campo magnético ........................................................................................................ 22

5.4 Cables de fuerza en baja tensión ....................................................................................................... 23

5.4.1 Características de la instalación .................................................................................................... 23

5.4.2 Cálculo del campo eléctrico ........................................................................................................... 24

5.4.3 Cálculo del campo magnético ........................................................................................................ 24

5.5 Centro de transformación ................................................................................................................... 28

5.5.1 Características de la instalación .................................................................................................... 28

5.5.2 Cálculo del campo eléctrico ........................................................................................................... 29

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 2 de 41

Estudio de Campos Electromagnéticos Rev. A

5.5.3 Cálculo del campo magnético ........................................................................................................ 29

6 Límites de exposición humana a CEM ............................................................................................. 31

6.1 Normativa aplicable ............................................................................................................................ 31

6.2 Verificación de las mediciones realizadas ......................................................................................... 33

6.3 Análisis de receptores ......................................................................................................................... 34

6.4 Verificación de línea aérea de 13,2 [kV] ............................................................................................ 36

6.5 Verificación de línea de 13,2 [kV] soterrada ..................................................................................... 36

6.6 Verificación de línea de 800 V en baja tensión ................................................................................. 37

6.7 Verificación de la subestación inversora y transformadora .............................................................. 37

7 Conclusiones .................................................................................................................................. 38

8 Especificaciones del equipo de medida y certificado ....................................................................... 39

9 Referencias .................................................................................................................................... 41

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 3 de 41

Estudio de Campos Electromagnéticos Rev. A

1 Introducción

El Proyecto Parque Fotovoltaico Nueva Paillaco consiste en la construcción y operación de un Parque Solar,

con una potencia instalada de 7,42 MWp con una inyección maxima a la red de 4,5 [MW].

El Proyecto comprende la instalación de 2 transformadores de 3 [MVA] y de 12.272 paneles fotovoltaicos

y un sistema de almacenamiento de energía por medio de baterías denominado BESS.

A su vez, el parque será conectado mediante una línea de media tensión a las redes de SOCOEPA, de

aproximadamente 461 [m] como linea soterrada y 15 metros como línea aérea. a través del alimentador

52C1 perteneciente a la compañía distribuidora Socoepa.

El Proyecto se emplazará en el Fundo Manao Hijuela 1 Lote B del área rural de la comuna de Paillacoo,

provincia de Valdivia,Región de Los Ríos.

Figura 1-1 - Imagen satelital del área de emplazamiento del proyecto

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 4 de 41

Estudio de Campos Electromagnéticos Rev. A

2 Objetivos

2.1 Línea de base

Se realizará la línea de base del proyecto, midiendo los campos electromagnéticos (CEM), en la

infraestructura eléctrica cercana a la zona donde se emplazará el proyecto.

2.2 Simulación de campos electromagnéticos

A partir de simulaciones computacionales se calcularán los campos electromagnéticos (CEM), generados

por la operación en condiciones nominales del Proyecto.

En particular, se realizarán simulaciones en para determinar los campos eléctricos y magnéticos, a un

metro del suelo, generados por los siguientes elementos del Proyecto:

Tabla 2-1 Elementos constitutivos de campos eléctricos y/o magnéticos relevantes

|Línea de media tensión|Transformador|Línea soterrada|Línea BT|
|---|---|---|---|
|Línea de 13,2 kV|3000 kVA 13,2/0,8 kV|Línea de 13,2 kV|0,8 kV / 300 A max|

En particular se caracterizarán los siguientes elementos del proyecto:

1. Línea aérea de media tensión en 13,2 [kV]

2. Centro de transformación BT/MT de 3000 [kVA]

3. Línea subterránea de media tensión en 13,2 [kV]

4. Línea subterránea de baja tensión en 0,8 [kV]

Los valores de campo eléctrico y magnéticos obtenidos mediante simulación computacional serán

comparados con los límites de exposición humana admisibles para un entorno ocupacional y de público

general y son válidas para ambas etapas del proyecto.

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 5 de 41

Estudio de Campos Electromagnéticos Rev. A

3 Metodología

3.1 Cálculo del campo eléctrico

En este estudio se determinan los campos eléctricos, mediante un análisis simplificado en dos

dimensiones. Este análisis permite calcular el campo eléctrico de una línea de transmisión con una

precisión aceptable. [1]

Las consideraciones de este análisis son las siguientes:

Los conductores de las líneas de transmisión son simulados como conductores cilíndricos de longitud

infinita, paralelos entre sí y sobre un terreno perfectamente plano.

La tierra se asume como un conductor perfecto. El dieléctrico entre los conductores y la tierra es aire, cuya

permitividad se supondrá igual a la permitividad del espacio vacío (ɛ0= 8,854·10-12 F/m)

No se consideran las estructuras metálicas, ni los cables de guardia.

Con las restricciones antes expuestas, es posible resolver el problema de forma precisa utilizando el

método de simulación de cargas o método de las imágenes.

De esta manera los conductores se representan como una carga puntual ubicada en el centro de cada

conductor, y una carga imagen, ubicada en la tierra, a una profundidad igual a la altura del conductor.

El valor de las cargas en cada conductor se puede determinar a partir de la tensión fasorial aplicada a cada

conductor (V) y la matriz de los coeficientes de potencial de Maxwell (P).

[Q] = [P] [−1] [V] Ec. 1

Los elementos de la matriz de coeficientes de Maxwell se calculan a partir de las siguientes expresiones

Ec. 2y Ec. 3.

1
P kk = 2πε

ln ( [4H] [k]

d k

Ec. 2
)

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 6 de 41

Estudio de Campos Electromagnéticos Rev. A

1
P =
kj 2πε

D k′ j

ln (

D
kj

Ec. 3

~~)~~

Donde:

Pkk es el coeficiente de potencial propio del conductor k.

Pkj es el coeficiente de potencial mutuo entre los conductores k y l.

dk es el diámetro del conductor k.

Hk es la altura sobre el suelo del conductor k.

Dkj Es la distancia entre los conductores k y j.

D’kj Es la distancia entre los conductores k y la imagen del conductor j.

ɛ0 8,854·10-12 F/m

En el caso de líneas compuestas por sub conductores en cada fase (bundle), se calcula un diámetro

equivalente determinado por las siguientes expresiones, Ec. 4, Ec. 5:

s
d b =

sin ~~[π]~~

n

1

) n

Ec. 4

Ec. 5

d eq = d b ~~(~~ [nd] d b

1

n

Donde:

db corresponde al diámetro del grupo de conductores.

n es el número de sub conductores por grupo.

d es el diámetro de los sub conductores (diámetro del círculo que pasa por cada sub conductor).

s es el espacio entre dos sub conductores adyacentes.

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 7 de 41

Estudio de Campos Electromagnéticos Rev. A

La solución de Ec. 1 permite obtener la carga eléctrica en cada conductor. Conocida esta información, es

posible conocer el potencial del campo eléctrico en cada punto del espacio.

Luego, las componentes vectoriales del campo eléctrico producidas por el k-ésimo conductor, quedarían

representadas por las siguientes ecuaciones:

[+ jQ] [ik] X M

2πε ∙(X M2 + (H k

X M

2 2 ~~[)]~~

M + (H k + H M )

E kx = [Q] [rk] [+ jQ] [ik]

X M X M

2 2 [−] 2

M + (H k −H M ) X M + (H k

Ec. 6

[+ jQ] [ik] H M −H k

2πε ∙(X M2 + (H k

H M −H k Ec. 7

2 2 [)]

M + (H k + H M )

E = [Q] [rk] [+ jQ] [ik]
ky

H M −H k H M −H k

2 2 [−] 2

M + (H k −H M ) X M + (H k

E x kx
= ∑E

k

E
y ky
= ∑E

k

Ec. 8

Ec. 9

Donde:

Ekx Componente horizontal del campo eléctrico

Eky Componente vertical del campo eléctrico

Qrk Componente real de carga eléctrica

Qik Componente imaginaria de carga eléctrica

XM Distancia horizontal entre el punto de medida y el conductor k-ésimo

YM Coordenada Y del punto del espacio donde se medirá el campo eléctrico

H k Coordenada Y de conductor k-ésimo

ɛ En este caso, permitividad del espacio vacío: ɛ0 = 8,854E−12 C2N-1m-2

El valor eficaz (RMS) de las componentes reales e imaginarias, queda entonces definido por:

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 8 de 41

Estudio de Campos Electromagnéticos Rev. A

Ec. 10
E rms = E x [2] + E y [2]
~~√~~

Como el campo eléctrico, es un campo vectorial complejo, el cual puede estar polarizado circular ó

elípticamente. La Ec. 10 determina el valor eficaz máximo de campo, el cual corresponde a la magnitud del

semieje mayor.

3.2 Cálculo del campo magnético

El campo magnético producido por las líneas de transmisión eléctricas puede ser calculado con precisión

utilizando un método simplificado en dos dimensiones, de manera análoga al campo eléctrico. [1]

Las consideraciones para este análisis son las siguientes:

Los conductores de las líneas de transmisión son simulados como conductores cilíndricos de longitud

infinita, paralelos entre sí y sobre un terreno perfectamente plano.

La tierra se asume como un mal conductor del campo magnético. La presencia de la tierra puede ser

simulada por imágenes del conductor enterrados a una profundidad compleja, que puede ser aproximado

a una profundidad real. En la práctica, la profundidad del conductor imagen es tan grande, que, para

cálculos en las zonas adyacentes a las líneas de transmisión, podría ser ignorado, sin una pérdida de

precisión significativa.

La profundidad del conductor imagen, es aproximadamente 1,31, donde  corresponde a la profundidad

aparente de la tierra (skin depth), dada por la ecuación:

δ= √

ρ

πfμ

Ec. 11

La permeabilidad del suelo es cercana a la permeabilidad del aire en la mayoría de las situaciones. ( =

410 [-7] ).

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 9 de 41

Estudio de Campos Electromagnéticos Rev. A

Considere un conductor k, con una magnitud de corriente I k y una fase de  k . Esta corriente también puede

ser expresada de forma cartesiana, como la suma de sus componentes reales e imaginaria:

I k = I kr + jI ki

El campo magnético producido por esta corriente tiene una componente horizontal y una componente

vertical real y una componente imaginaria, B kr y B ki respectivamente, que a su vez están compuestas por

dos componentes ortogonales normales al conductor.

2 ∙10 [−7] I kr (x m −x k ) Ec. 12
B krx =

√(x M −x k ) [2] + (h M −h k ) [2]

2 ∙10 [−7] I kr (h M −h k ) Ec. 13
B krh =

√(x M −x k ) [2] + (h M −h k ) [2]

2 ∙10 [−7] I ki (x m −x k ) Ec. 14
B kix =

√(x M −x k ) [2] + (h M −h k ) [2]

2 ∙10 [−7] I ki (h M −h k )
B kih =

√(x M −x k ) [2] + (h M −h k ) [2]

Ec. 15

Donde:

B krx Componente horizontal real del campo magnético

B krh Componente vertical real del campo magnético

B kix Componente horizontal imaginaria del campo magnético

B kih Componente vertical imaginaria del campo magnético

X M Distancia horizontal entre el punto de medida (punto M) y el conductor k-ésimo

H M Distancia vertical entre el punto de medida (punto M) y el conductor k-ésimo

H K Coordenada Y de conductor k-ésimo

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 10 de 41

Estudio de Campos Electromagnéticos Rev. A

Para una línea de transmisión de n conductores (k=1...n), las componentes reales e imaginarias del campo

magnético horizontal en el punto M, se calculan de forma independiente para cada conductor, para luego

ser sumadas, como se indica en la Ec. 16

Una vez determinado el campo vertical y horizontal a partir de la Ec. 17 es posible determinar la magnitud

del campo magnético resultante según la Ec. 18.

B rx = ∑B k krx B rh = ∑B k krh B ix = ∑B k kix B ih = ∑B k kih Ec. 16

B x = B rx 2 + B ix 2
~~√~~

Ec. 17
2

ix 2 B y = B ry 2 + B iy 2

~~√~~

Ec. 18
B= B x [2] + B y [2]
~~√~~

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 11 de 41

Estudio de Campos Electromagnéticos Rev. A

4 Línea de base

Las mediciones de campo eléctrico y magnético bajo una línea eléctrica se llevan a cabo según lo

establecido en el estándar IEEE 644-2019 [2]. Fueron realizadas por el Ingeniero Civil Sr. Sergio Arriaza

Sánchez el día 06 de Marzo de 2024 a las 13:00 Hrs.

Al momento de la medición el cielo estaba despejado, y el suelo seco, sin vestigios de precipitaciones

recientes.

Se utilizó el equipo Holaday HI-3604, N° de Serie 75921. En el punto 8, se indican las características

principales del equipo de medición, junto con su certificado de calibración.

En el caso de lineas de media tension casos de registran valores de forma aledaña a la estructura y a una

distancia variable respecto de esta.

4.1 Mediciones puntuales

En este punto, se presentan las mediciones realizadas en las instalaciones cercanas al proyecto que son

fuentes de campo eléctromagnético.

Las coordenadas de las mediciones, y los valores de campo eléctrico y campo magnético registrados en

terreno, se presentan en la Tabla 4-1.

<!-- INICIO TABLA 4-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Un resumen gráfico de la zona donde se realizaron cada una de estas mediciones y su cercanía a elementos del sistema de distribución eléctrica existente en la zona, se puede encontrar en la Figura 4-1. -->

**Tabla 4-1: - Mediciones puntuales de campo**

| Medida | Coord.<br>UTM E [m] | Coord.<br>UTM N [m] | Campo Eléctrico<br>[V/m] | Campo magnético<br>[T] |
| --- | --- | --- | --- | --- |
| Poste MT AW0820 (0m) | 686.006 | 5.558.674 | 678 | 0,043 |
| Poste MT AW0820 (3m) | 686.006 | 5.558.674 | 254 | 0,050 |
| Poste Sin Placa (Al. Futrono) (0 m) | 687.631 | 5.556.911 | 883 | 0,024 |
| Poste Sin Placa (Al. Futrono) (3 m) | 687.631 | 5.556.911 | 517 | 0,027 |
| Poste Sin Placa (Al. Futrono) (6 m) | 687.631 | 5.556.911 | 184,8 | 0,024 |

<!-- Estadísticas: 5 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia (Coordenadas WGS 84 Huso 18G) (*) Coordenadas referentes al inicio de la medida -->
<!-- FIN TABLA 4-1 -->


Un resumen gráfico de la zona donde se realizaron cada una de estas mediciones y su cercanía a

elementos del sistema de distribución eléctrica existente en la zona, se puede encontrar en la Figura 4-1.

Tabla 4-1 - Mediciones puntuales de campo

|Medida|Coord.<br>UTM E [m]|Coord.<br>UTM N [m]|Campo Eléctrico<br>[V/m]|Campo magnético<br>[T]|
|---|---|---|---|---|
|Poste MT AW0820 (0m)|686.006|5.558.674|678|0,043|
|Poste MT AW0820 (3m)|686.006|5.558.674|254|0,050|
|Poste Sin Placa (Al. Futrono) (0 m)|687.631|5.556.911|883|0,024|
|Poste Sin Placa (Al. Futrono) (3 m)|687.631|5.556.911|517|0,027|
|Poste Sin Placa (Al. Futrono) (6 m)|687.631|5.556.911|184,8|0,024|

Fuente: Elaboración propia (Coordenadas WGS 84 Huso 18G)

(*) Coordenadas referentes al inicio de la medida

Tabla 4-2 - Perfil Línea MT 13.2 kV 52C1 Paillaco Socoepa

|Medida|Campo Eléctrico<br>[V/m]|Campo magnético<br>[T]|
|---|---|---|
|-6|43,40|0,023|
|-3|141,90|0,021|
|0|94,70|0,118|
|3|160,70|0,036|

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 12 de 41

Estudio de Campos Electromagnéticos Rev. A

|Medida|Campo Eléctrico<br>[V/m]|Campo magnético<br>[T]|
|---|---|---|
|6|99,40|0,038|

Fuente: Elaboración propia (Coordenadas WGS 84 Huso 18G)

Eje de la medida : 686.654 E 5.558.330 N

Figura 4-1 - Imagen satelital de las mediciones realizadas

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 13 de 41

Estudio de Campos Electromagnéticos Rev. A

Figura 4-2 Estructura AW0820, Alimentador APSA (SAESA)

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 14 de 41

Estudio de Campos Electromagnéticos Rev. A

Figura 4-3 Estructura P.100780 (Alim. Paillaco - Socoepa)

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 15 de 41

Estudio de Campos Electromagnéticos Rev. A

Figura 4-4 Estructura Sin Placa (Alim. Futrono - SAESA)

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 16 de 41

Estudio de Campos Electromagnéticos Rev. A

5 Modelación

5.1 Línea de distribución de 13,2 kV

5.1.1 Características de la instalación

Se modelará una línea de distribución típica de 13,2 [kV] con una estructura típica de hormigón armado de

11,5 [m] y una cruceta de 2,4 [m]. Se ha considerado la disposición de estructura de anclaje, en la cual los

conductores de fase están espaciados 1,1 [m] entre sí.

Debido a la potencia del PMGD, se ha considerado un conductor de aleación de aluminio AAAC Cairo de

sección 236 mm2.

Figura 5-1 - Estructura de anclaje típica modelada

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 17 de 41

Estudio de Campos Electromagnéticos Rev. A

Tabla 5-1 Datos de entrada para la modelación

|X|Y|Fase|Conductor|r|R|N|V|I|P|
|---|---|---|---|---|---|---|---|---|---|
|-1,10|6,00|a|AAAC Cairo|0,0099|0,0099|1|13,2|197|4,5|
|0,00|6,00|b|AAAC Cairo|0,0099|0,0099|1|13,2|197|4,5|
|1,10|6,00|c|AAAC Cairo|0,0099|0,0099|1|13,2|197|4,5|

Donde :

 - X : Coordenada x del conductor de fase (m)

 - Y: Coordenda y del conductor de fase (m)

 - Fase : Fase modelada (a,b,c)

 - Conductor: Nombre comercial del conductor

 - r : Radio del conductor expresado en metros (m)

 - R : Radio equivalente del conjunto de conductores, en el caso de líneas con un solo conductor por

fase equivale a r (m)

 - N: Número de conductores por fase

 - V : Tensión nominal del conductor (kV)

 - I: Corriente nominal del conductor (A)

 - P: Potencia (MVA)

Figura 5-2 Disposición de los conductores para línea de 13,2 kV

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 18 de 41

Estudio de Campos Electromagnéticos Rev. A

5.1.2 Cálculo del campo eléctrico

A fin de determinar el escenario más desfavorable respecto de la instalación, se ha considerado la altura

de los conductores como la mínima reglamentaria (6 [m] sobre el nivel de suelo), para líneas de media

tensión según el Artículo 6.3 del RPTD N°07. [3]

Los datos de entrada corresponde a los de la Tabla 5-1.

<!-- INICIO TABLA 5-1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 17 de 41 Estudio de Campos Electromagnéticos Rev. A -->

**Tabla 5-1: Datos de entrada para la modelación**

| X | Y | Fase | Conductor | r | R | N | V | I | P |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| -1,10 | 6,00 | a | AAAC Cairo | 0,0099 | 0,0099 | 1 | 13,2 | 197 | 4,5 |
| 0,00 | 6,00 | b | AAAC Cairo | 0,0099 | 0,0099 | 1 | 13,2 | 197 | 4,5 |
| 1,10 | 6,00 | c | AAAC Cairo | 0,0099 | 0,0099 | 1 | 13,2 | 197 | 4,5 |

<!-- Estadísticas: 3 filas, 10 columnas -->
<!-- Contexto posterior: -->
<!-- Donde : - X : Coordenada x del conductor de fase (m) -->
<!-- FIN TABLA 5-1 -->


A continuación se presenta el perfil calculado a partir del método indicado en

|Perfil de campo electrico<br>Linea MT 13.2 kV<br>0.50<br>[kV/m]<br>0.40<br>eléctrico<br>0.30<br>campo<br>0.20<br>de<br>ad|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|0.20<br>0.30<br>0.40<br>0.50<br>ad de campo eléctrico [kV/m]<br>**Perfil de campo electrico**<br>**Linea MT 13.2 kV**||||||||||||
|0.20<br>0.30<br>0.40<br>0.50<br>ad de campo eléctrico [kV/m]<br>**Perfil de campo electrico**<br>**Linea MT 13.2 kV**|||||0.20<br>0.30<br>0.40|||||||
|ntensid|||||0.10|||||||
|0.00<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>I<br>Distancia al eje de la línea de transmisión [m]|0.00<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>I<br>Distancia al eje de la línea de transmisión [m]|0.00<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>I<br>Distancia al eje de la línea de transmisión [m]|0.00<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>I<br>Distancia al eje de la línea de transmisión [m]|0.00<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>I<br>Distancia al eje de la línea de transmisión [m]|0.00<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>I<br>Distancia al eje de la línea de transmisión [m]|0.00<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>I<br>Distancia al eje de la línea de transmisión [m]|0.00<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>I<br>Distancia al eje de la línea de transmisión [m]|0.00<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>I<br>Distancia al eje de la línea de transmisión [m]|0.00<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>I<br>Distancia al eje de la línea de transmisión [m]|0.00<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>I<br>Distancia al eje de la línea de transmisión [m]|0.00<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>I<br>Distancia al eje de la línea de transmisión [m]|

Figura 5-3 Perfil de campo eléctrico línea de 13.2 kV del PMGD

Tabla 5-2 Valores límites de campo eléctrico

|Punto de medida|x [m]|y[m]|Campo Eléctrico [kV/m]|
|---|---|---|---|
|Limite franja seguridad derecha|4,00|1|0,102|
|Limite franja seguridad izquierda|-4,00|1|0,102|
|Valor máximo en perfil|-3,50|1|0,104|

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 19 de 41

Estudio de Campos Electromagnéticos Rev. A

5.1.3 Cálculo del campo magnético

A fin de determinar el escenario más desfavorable respecto de la instalación, se ha considerado la altura

de los conductores como la mínima reglamentaria (6 [m] sobre el nivel de suelo), para líneas de media

tensión según el Artículo 6.3 del RPTD N°07. [3]

Además, se considerará la corriente nominal de la línea MT. Para 4,5 [MW] en 13,2 [kV], corresponderá a

una corriente de 197 [A]

Tabla 5-3 - Condiciones para cálculo del campo magnético

|Perfil de campo magnético<br>Linea MT 13.2 kV<br>10.0<br>[μT]<br>7.5<br>magnético<br>5.0<br>ampo|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|Col13|
|---|---|---|---|---|---|---|---|---|---|---|---|---|
|5.0<br>7.5<br>10.0<br>ampo magnético [μT]<br>**Perfil de campo magnético**<br>Linea MT 13.2 kV|||||||||||||
|5.0<br>7.5<br>10.0<br>ampo magnético [μT]<br>**Perfil de campo magnético**<br>Linea MT 13.2 kV|||||7.5|7.5|||||||
|5.0<br>7.5<br>10.0<br>ampo magnético [μT]<br>**Perfil de campo magnético**<br>Linea MT 13.2 kV|||||||||||||
|5.0<br>7.5<br>10.0<br>ampo magnético [μT]<br>**Perfil de campo magnético**<br>Linea MT 13.2 kV|||||5.0|5.0|||||||
|5.0<br>7.5<br>10.0<br>ampo magnético [μT]<br>**Perfil de campo magnético**<br>Linea MT 13.2 kV|||||||||||||
|5.0<br>7.5<br>10.0<br>ampo magnético [μT]<br>**Perfil de campo magnético**<br>Linea MT 13.2 kV|||||||||||||
|C||||||.5|||||||
|C|||||||||||||
|C|||||||||||||
|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|

|Col1|Coordenada X|Coordenada Y|Corriente [A Rms]|
|---|---|---|---|
|Fase A|-1,1 [m]|6 [m]|197∠−120°|
|Fase B|0 [m]|6 [m]|197∠0°|
|Fase C|1,1 [m]|6 [m]|197∠120°|

Figura 5-4 Perfil de campo magnético línea de 13,2 kV

Tabla 5-4 Valores límites de campo magnético

|Punto de medida|x [m]|y[m]|Campo Magnético [T]|
|---|---|---|---|
|Limite franja seguridad derecha|4,00|1|1,83|
|Limite franja seguridad izquierda|-4,00|1|1,83|
|Valor máximo en perfil|0,00|1|2,89|

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 20 de 41

Estudio de Campos Electromagnéticos Rev. A

5.3 Línea de distribución soterrada 13,2 kV

5.3.1 Características de la instalación

En la salida de la subestación transformadora, el cableado de corriente alterna de media tensión (13,2

[kV]), se realizará mediante canalizaciones subterráneas dentro del área de paneles. Esta línea lleva el

aporte de los transformadores en un solo circuito para formar la línea de evacuación que transporta la

energía hacia la subestación.

Se utilizará el cable del tipo Aluminio XLPE, de sección hasta 1 x 240 mm2, apantallado.

Figura 5-5 - Instalación de cable subterráneo típico modelado

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 21 de 41

Estudio de Campos Electromagnéticos Rev. A

5.3.2 Cálculo del campo eléctrico

El cable con pantalla metálica aterrizada encierra el campo eléctrico producido por la tensión de su

conductor activo. Por lo tanto, no será necesaria su simulación, pues se considera una fuente nula de

campo eléctrico visto desde el exterior. [4]

5.3.3 Cálculo del campo magnético

A fin de determinar el escenario más desfavorable respecto de la instalación, se ha considerado los cables

directamente enterrados en el suelo a una profundidad 0,95 [m] del suelo, en una zanja de 0,6 [m] de

ancho.

Se considerará la corriente nominal de la línea MT. Para 4.5 [MW] en 13,2 [kV], corresponderá a una

corriente de 197 [A].

Tabla 5-5 - Condiciones para el cálculo de campo magnético en línea soterrada de 13,2 [kV]

|Col1|Coordenada X|Coordenada Y|Tensión F-N [V Rms]|Corriente [A]|
|---|---|---|---|---|
|Fase A|-0,15 [m]|- 1 [m]|13200<br>√3<br>∠0°|197∠0°|
|Fase B|0 [m]|- 1 [m]|13200<br>√3<br>∠120°|197∠120°|
|Fase C|0,15 [m]|- 1 [m]|132000<br>√3<br>∠−120°|197∠−120°|

|Perfil de campo magnético<br>Circuito 13.2 kV 4.5 MW<br>5.0<br>4.0<br>[μT]<br>agnético<br>3.0|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
|3.0<br>4.0<br>5.0<br>agnético [μT]<br>**Perfil de campo magnético**<br>Circuito 13.2 kV 4.5 MW||||||||||||
|3.0<br>4.0<br>5.0<br>agnético [μT]<br>**Perfil de campo magnético**<br>Circuito 13.2 kV 4.5 MW|||||4.0|||||||
|3.0<br>4.0<br>5.0<br>agnético [μT]<br>**Perfil de campo magnético**<br>Circuito 13.2 kV 4.5 MW||||||||||||
|3.0<br>4.0<br>5.0<br>agnético [μT]<br>**Perfil de campo magnético**<br>Circuito 13.2 kV 4.5 MW|||||3.0|||||||
|3.0<br>4.0<br>5.0<br>agnético [μT]<br>**Perfil de campo magnético**<br>Circuito 13.2 kV 4.5 MW||||||||||||
|Campo m|||||2.0|||||||
|Campo m||||||||||||
|Campo m|||||1.0|||||||
|Campo m||||||||||||
|Campo m|||||~~0.0~~|||||||
|-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m]|

Figura 5-6 Línea de 13,2 kV soterrado (4.5 MW)

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 22 de 41

Estudio de Campos Electromagnéticos Rev. A

Tabla 5-6 Valores límites de campo magnético de 13,2 [kV] (linea soterrada)

|Punto de medida|x [m]|y[m]|Campo Magnético<br>[uT]|
|---|---|---|---|
|Limite franja seguridad derecha|0,50|1|2,40|
|Limite franja seguridad izquierda|-0,50|1|2,40|
|Valor máximo en perfil|0,00|1|2,55|

5.4 Cables de fuerza en baja tensión

5.4.1 Características de la instalación

Se utilizará un conductor flexible en Aluminio del tipo XZ1 o equivalente, de sección hasta 1 x 400 mm2..

El cableado de baja tensión será canalizado a través de zanjas subterráneas, los cables se considerarán

enterrados a una profundidad mínima de 0,70 [m] y distribuidos en un ancho de 1,50 [m].

Figura 5-7 Esquema de instalación de zanjas de baja tensión

Se considerará para efectos de cálculo, el voltaje máximo de salida por los inversores (800 [V]) y la corriente

máxima de diseño para un inversor de 300 kW (217 [A]). Evidentemente, la operación a tensiones o

corrientes menores, disminuirá la intensidad de los campos eléctrico y magnético, respectivamente.

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 23 de 41

Estudio de Campos Electromagnéticos Rev. A

5.4.2 Cálculo del campo eléctrico

Cuando un cable se instala enterrado, prácticamente no produce campo eléctrico sobre la tierra, debido al

efecto de “pantalla” de la misma tierra, y en algunos cables, debido al uso de pantallas metálicas de

protección (generalmente cables de media y alta tensión). [4]

Por lo tanto, no se considera una fuente relevante de campo eléctrico.

5.4.3 Cálculo del campo magnético

Tabla 5-7 - Condiciones para cálculo del campo magnético

|Estructura|X|Y|Fase|Conductor|r|R|N|V|I|P|
|---|---|---|---|---|---|---|---|---|---|---|
|Z_BT|-0,65|-0,71|a|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,62|-0,71|b|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,64|-0,68|c|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,54|-0,71|a|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,50|-0,71|b|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,52|-0,68|c|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,42|-0,71|a|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,39|-0,71|b|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,41|-0,68|c|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,31|-0,71|a|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,27|-0,71|b|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,29|-0,68|c|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,19|-0,71|a|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,16|-0,71|b|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,18|-0,68|c|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,08|-0,71|a|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|-0,04|-0,71|b|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 24 de 41

Estudio de Campos Electromagnéticos Rev. A

|Estructura|X|Y|Fase|Conductor|r|R|N|V|I|P|
|---|---|---|---|---|---|---|---|---|---|---|
|Z_BT|-0,06|-0,68|c|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,04|-0,71|a|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,07|-0,71|a|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,06|-0,68|b|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,15|-0,71|c|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,19|-0,71|a|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,17|-0,68|b|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,27|-0,71|c|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,30|-0,71|a|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,29|-0,68|b|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,38|-0,71|c|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,42|-0,71|a|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,40|-0,68|b|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,50|-0,71|c|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,53|-0,71|a|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,52|-0,68|b|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,61|-0,71|c|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,65|-0,71|a|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|
|Z_BT|0,63|-0,68|b|Al. 400 mm2|0,012|0,012|1|0,8|217|0,3|

Donde:

 - X : Coordenada x del conductor de fase (m)

 - Y: Coordenda y del conductor de fase (m)

 - Fase : Fase modelada (a,b,c)

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 25 de 41

Estudio de Campos Electromagnéticos Rev. A

 - Conductor: Nombre comercial del conductor

 - r : Radio del conductor expresado en metros (m)

 - R : Radio equivalente del conjunto de conductores, en el caso de líneas con un solo conductor por

fase equivale a r (m)

 - N: Número de conductores por fase

 - V : Tensión nominal del conductor (kV)

 - I: Corriente nominal del conductor (A)

 - P: Potencia transmitida máxima (MVA)

La disposición de los conductores se presenta en la Figura 5-8.

Figura 5-8 Disposición de los cables soterrados

Tabla 5-8 Valores límites de campo magnético

|Punto de medida|x [m]|y[m]|Campo Magnético [T]|
|---|---|---|---|
|Limite franja seguridad derecha|1,50|1|4,22|
|Limite franja seguridad izquierda|-1,50|1|4,21|
|Valor máximo en perfil|0,00|1|6,49|

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 26 de 41

Estudio de Campos Electromagnéticos Rev. A

Figura 5-9 - Campo magnético provocado por conductores de baja tensión

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 27 de 41

Estudio de Campos Electromagnéticos Rev. A

5.5 Centro de transformación

5.5.1 Características de la instalación

El transformador eleva la energía generada por el inversor a la tensión de la red. Se ha seleccionado un

transformador con las siguientes características:

Tabla 5-9 Datos de placa del transformador

|Parámetros|Valor|
|---|---|
|Potencia nominal|3000 [kVA]|
|Tensión nominal|0,8/13,2 [kV]|
|Tensión máxima|25 [kV]|
|Frecuencia|50 [Hz]|
|Grupo de conexión|Dy11|
|Refrigeración|ONAN|
|Altitud máxima|1000 [msnm]|

Figura 5-10 - Centro de transformación típico

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 28 de 41

Estudio de Campos Electromagnéticos Rev. A

5.5.2 Cálculo del campo eléctrico

La cabina metálica al estar aterrizada encierra el campo eléctrico producido por sus elementos interiores.

Por lo tanto, no será necesaria su simulación, pues se considera una fuente nula de campo eléctrico visto

desde el exterior.

5.5.3 Cálculo del campo magnético

En el paper “Worst Case Evaluation of Magnetic Field in the vicinity of Electric Power Substations” [5] se

propone una fórmula para estimar de forma conservadora, la peor condición de campo magnético en las

inmediaciones de una subestación transformadora:

B rms (r) = k tr ∙ [P] [N]

r [3]

Donde:

 - B [uT] = Densidad de flujo magnético, expresado en micro Tesla.

 - k [Tm [3] /VA] = Coeficiente de campo, experimentalmente se determina como 0,04 [Tm [3] /VA]

 - P N [kVA] = Potencia nominal de la subestación transformadora (3000 kVA)

Reemplazando en la Fórmula 2 para valores de r desde 1 a 10 [m], se tiene:

Tabla 5-10 - Valores tabulados de densidad (B) de flujo magnético

|Col1|r [m]|B [μT]|Col4|
|---|---|---|---|
||1|120,0|120,0|
||1,5|35,6|35,6|
||2|15,0|15,0|
||2,5|7,7|7,7|
||3|4,4|4,4|
||3,5|2,8|2,8|
||4|1,9|1,9|
||4,5|1,3|1,3|
||5|1,0|1,0|
||5,5|0,7|0,7|
||6|0,6|0,6|
||6,5|0,4|0,4|
||7|0,3|0,3|
||7,5|0,3|0,3|
||8|0,2|0,2|
||8,5|0,2|0,2|
||9|0,2|0,2|

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 29 de 41

Estudio de Campos Electromagnéticos Rev. A

|r [m]|B [μT]|
|---|---|
|9,5|0,1|
|10|0,1|

Figura 5-11 - Intensidad de campo magnético a diferentes distancias r de la subestación transformadora

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 30 de 41

Estudio de Campos Electromagnéticos Rev. A

6 Límites de exposición humana a CEM

6.1 Normativa aplicable

En nuestro país los valores límites permitidos de exposición de las personas a los campos

electromagnéticos de frecuencia industrial provocados por líneas y subestaciones eléctricas, está definido

por la normativa nacional sectorial vigente. [6]

En particular, lo indicados el punto 4.7 del RPTD N°07, Franja y distancia de seguridad y por el punto 5.1.9

del RPTD N°10, Centrales de producción, correspondientes a los Pliegos Técnicos (Dto. 109/2017 Min. De

Energia). [3]

A continuación, se destacan los párrafos de esta normativa aplicable al proyecto, donde se indican los

límites máximos de exposición:

Punto 4.7 RPTD N°07:

_Los límites máximos permisibles para la seguridad de las personas, en cuanto a la emisión de campo_

_electromagnético para el diseño de líneas aéreas de corriente alterna de 50 Hz de frecuencia, y que será_

_evaluado en el exterior de la franja de seguridad, a 1 metro sobre el nivel del suelo, en condiciones_

_normales de operación de la línea, con los conductores en reposo, serán los que determinen las normas_

_respectivas. En ausencia de regulación técnica nacional, se debe cumplir con lo siguiente:_

_5 kV/m para campo eléctrico (valor RMS) /100 μT para campo magnético (valor RMS)_

Punto 5.1. 9 RPTD N°07:

_Los límites máximos permisibles para la seguridad de las personas, en cuanto a la emisión de campo_

_electromagnético para el diseño de líneas aéreas de corrientealterna de 50 Hz de frecuencia, y que será_

_evaluado en el exterior de la franja de seguridad, a 1 metro sobre el nivel del suelo, en condiciones_

_normales de operación de la línea, con los conductores en reposo, serán los que determinen las normas_

_respectivas. En ausencia de regulación técnica nacional, se debe cumplir con lo siguiente:_

_5 kV/m para campo eléctrico (valor RMS) / 100 μT para campo magnético (valor RMS)_

Por otra parte, para efectos de la evaluación de impactos en el SEIA asociados a campos electromagnéticos,

no existe normativa nacional ue considere como objetivo la protección a la salud de la población, razón por

la cual se utilizan normativas de referencia, según lo dispuesto en el artículo 11 del Reglamento del SEIA.

El Decreto No 40 del Ministerio del Medio Ambiente, “Aprueba Reglamento del Sistema de Evaluación de

Impacto Ambiental”, publicado el 12-08-2013, y que entró en vigencia el 24-12-2013, indica en su Artículo

11:

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 31 de 41

Estudio de Campos Electromagnéticos Rev. A

“ _Artículo 11.- Normas de referencia._

_Las normas de calidad ambiental y de emisión que se utilizarán como referencia para los efectos de evaluar_

_si se genera o presenta el riesgo indicado en la letra a) y los efectos adversos señalados en la letra b),_

_ambas del artículo 11 de la Ley, serán aquellas vigentes en los siguientes Estados: República Federal de_

_Alemania, República Argentina, Australia, República Federativa del Brasil, Canadá, Reino de España,_

_Estados Unidos Mexicanos, Estados Unidos de América, Nueva Zelandia, Reino de los Países Bajos,_

_República Italiana, Japón, Reino de Suecia y Confederación Suiza. Para la utilización de las normas de_

_referencia, se priorizará aquel Estado que posea similitud en sus componentes ambientales, con la_

_situación nacional y/o local, lo que será justificado razonablemente por el proponente._ ”

La Tabla N° 4, presenta las principales normas de referencia aplicables en Chile, de acuerdo con lo

señalado en el Artículo 11.

.

Tabla 6-1 - Límites de Exposición Humana a Campos Electromagnéticos de 50 [Hz]

|Col1|Público General|Col3|Exposición Ocupacional|Col5|
|---|---|---|---|---|
|País/Entidad|Intensidad de campo<br>eléctrico [V/m]|Densidad de Flujo<br>magnético [uT]|Intensidad de campo<br>eléctrico [V/m]|Densidad de Flujo<br>magnético [uT]|
|Alemania|5000|100|5000|100|
|Argentina|3000|25|3000|25|
|Australia|5000|100|10000|500|
|Canadá|N/A|N/A|N/A|N/A|
|España|5000|100|10000|500|
|Japón|3000|N/A|10000|500|
|Países Bajos|8000|120|40000|600|
|Suecia|N/A|N/A|N/A|N/A|
|Suiza|5000|100|5000|100|
|ICNIRP|5000|200|10000|500|
|IEEE|5000|900|20000|2700|
|Unión Europea|5000|100|10000|500|

Fuente: Elaboración propia

La recomendación de uso más frecuente para público general y exposición permanente es la publicada por

la ICNIRP [7] (International Commission On Non-Ionizing Radiation Protection), que establece 5.000 [V/m]

para el campo eléctrico y 200 [uT] para la inducción magnética, coincidente con lo establecido con el

Consejo de Unión Europea (Directive 2004/40/EC) y con la normativa sectorial nacional. [6]

Nota: 1 miliGauss equivale a 0,1 microTesla ( 1 [mG] = 0,1 [uT])

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 32 de 41

Estudio de Campos Electromagnéticos Rev. A

6.2 Verificación de las mediciones realizadas

A continuación, se presentan los valores de las medidas de campo eléctrico y magnético obtenidas en

diferentes puntos de la línea de evacuación en 13,2 [kV] del proyecto y se comparan con los límites

establecidos para la normativa indica en el punto 6.1.

Tabla 6-2 Medidas en la red de distribución existente

|Medida|Campo<br>Eléctrico<br>[V/m]|Límite<br>ICNIRP/UE<br>[V/m]|Cumple<br>(Si/No)|Campo<br>magnético<br>[T]|Límite<br>ICNIRP/UE<br>[μT]|Cumple<br>(Si/No)|
|---|---|---|---|---|---|---|
|Poste MT AW0820 (0m)|678|5000|SI|0,043|100|SI|
|Poste MT AW0820 (3m)|254|5000|SI|0,050|100|SI|
|Poste Sin Placa (Al. Futrono) (0 m)|883|5000|SI|0,024|100|SI|
|Poste Sin Placa (Al. Futrono) (3 m)|517|5000|SI|0,027|100|SI|
|Poste Sin Placa (Al. Futrono) (6 m)|184,8|5000|SI|0,024|100|SI|

Por lo tanto, los valores medidos en terreno en las redes de distribución aledañas están bajo los límites

establecidos por ICNIRP/UE.

Tabla 6-3 Medidas en la línea de 13.2 kV Socoepa

|Medida|Campo<br>Eléctrico<br>[V/m]|Límite<br>ICNIRP/UE<br>[V/m]|Cumple (Si/No)|Campo<br>magnético<br>[T]|Límite<br>ICNIRP/UE<br>[μT]|Cumple (Si/No)|
|---|---|---|---|---|---|---|
|-6,0|43,40|5000|SI|0,023|100|SI|
|-3,0|141,90|5000|SI|0,021|100|SI|
|0|94,70|5000|SI|0,118|100|SI|
|3,0|160,70|5000|SI|0,036|100|SI|
|6,0|99,40|5000|SI|0,038|100|SI|

Por lo tanto, los valores medidos en terreno en las redes de distribución aledañas están bajo los límites

establecidos por ICNIRP/UE.

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 33 de 41

Estudio de Campos Electromagnéticos Rev. A

6.3 Análisis de receptores

Se han caracterizado 4 receptores en las inmediaciones del proyecto, que se presentan en la Figura 6-1

En la Tabla 6-4 se presentan las coordenadas de cada receptor, sus coordendas y la distancia a la fuente

emisora, junto con los valores de campos electromagnéticos producto de la evaluación del proyecto.

No se registran receptores expuestos a valores relevantes, observando valores inferiores al 0.01% de los

límites normativos debido a la operación del proyecto.

Figura 6-1 Ubicación de receptores

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 34 de 41

Estudio de Campos Electromagnéticos Rev. A

Tabla 6-4 Análisis de receptores

|Receptor|UTM E<br>[m]|UTM N<br>[m]|Distancia a<br>fuente [m]|Campo<br>eléctrico<br>[kV/m]|Limite<br>[kV/m]|% Limite|Campo<br>magnético<br>[μT]|Limite<br>[μT]|% Limite|
|---|---|---|---|---|---|---|---|---|---|
|Rpa1|686.325|5.558.722|295|0|5|0,0%|0|100|0,00%|
|Rpa2|686.444|5.558.140|273|0|5|0,0%|0|100|0,00%|
|Rpa3|687.021|5.557.610|652|0|5|0,0%|0|100|0,00%|
|Rpa4|687.039|5.558.410|95|0|5|0,0%|0,01|100|0,01%|

A partir de los resultados se verifica que la exposición a campos eléctricos y magnéticos resulta

despreciable para todos los receptores identificados, debido a su distancia y la poca intensidad de las

fuentes.

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 35 de 41

Estudio de Campos Electromagnéticos Rev. A

6.4 Verificación de línea aérea de 13,2 [kV]

La única instalación que está accesible al público general y fuera del cerco perimetral del proyecto,

corresponde a la línea de 13,2 [kV].

Tabla 6-5 - Valores determinados en borde de franja de seguridad 13,2 kV (a 4 [m] del eje de la instalación)

|Intensidad de campo eléctrico<br>en borde de franja de seguridad<br>[V/m]|Límite<br>ICNIRP/UE<br>[V/m]|Densidad de Flujo magnético<br>en borde de franja de<br>seguridad [μT]|Límite ICNIRP/UE<br>[μT]|
|---|---|---|---|
|102|5000|1,83|100|

Se verifica que los valores obtenidos para radiaciones magnéticas son menores a los 100 [uT] (1000 [mG]),

y que la radiación de campo eléctrico también es inferior a 5000 [V] (5 [kV]), estimados al borde de la franja

de seguridad.

6.5 Verificación de línea de 13,2 [kV] soterrada

La línea de 13,2 [kV] soterrada se encuentra dentro de la subestación y no es accesible al público general.

Se verifica que los valores obtenidos para radiaciones magnéticas son menores a los 100 [uT] (1000 [mG]),

y que la radiación de campo eléctrico también es inferior a 5000 [V] (5 [kV]).

Tabla 6-6 - Valores determinados en el eje de la instalación 13,2 kV

|Intensidad de campo eléctrico<br>en borde de franja de seguridad<br>[V/m]|Límite<br>ICNIRP/UE<br>[V/m]|Densidad de Flujo magnético<br>en borde de franja de<br>seguridad [μT]|Límite ICNIRP/UE<br>[μT]|
|---|---|---|---|
|0|5000|2,40|100|

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 36 de 41

Estudio de Campos Electromagnéticos Rev. A

6.6 Verificación de línea de 800 V en baja tensión

La línea de 800 V soterrada se encuentra dentro del parque y no es accesible al público general.

Se verifica que los valores obtenidos para radiaciones magnéticas son menores a los 100 [uT] (1000 [mG]),

y que la radiación de campo eléctrico también es inferior a 5000 [V] (5 [kV]).

Tabla 6-7 - Valores determinados en el eje de la instalación 13,2 kV

|Intensidad de campo eléctrico<br>en borde de franja de seguridad<br>[V/m]|Límite<br>ICNIRP/UE<br>[V/m]|Densidad de Flujo magnético<br>en borde de franja de<br>seguridad [μT]|Límite ICNIRP/UE<br>[μT]|
|---|---|---|---|
|0|5.000|1,84|100|

6.7 Verificación de la subestación inversora y transformadora

La subestación transformadora se encuentra dentro de la planta fotovoltaica y no es accesible al público

general.

Se verifica que los valores obtenidos para radiaciones magnéticas son menores a los 20 [uT], a 2 [m] de

ésta y que la radiación de campo eléctrico es nula debido a que está contenido en un contenedor metálico

aterrizado.

Tabla 6-8 - Valores determinados a 2,5 [m] de la subestación transformadora

|Intensidad de campo eléctrico<br>en borde de franja de seguridad<br>[V/m]|Límite<br>ICNIRP/UE<br>[V/m]|Densidad de Flujo magnético<br>a 2 [m] del transformador<br>[μT]|Límite ICNIRP/UE<br>[μT]|
|---|---|---|---|
|0|5.000|15|100|

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 37 de 41

Estudio de Campos Electromagnéticos Rev. A

7 Conclusiones

De los resultados obtenidos mediante simulaciones computacionales y fórmulas empíricas se concluye:

 - La línea aérea de 13,2 [kV] no sobrepasa los valores límites de ICNIRP/UE, respecto de campos

eléctricos y magnéticos de 50 [Hz]

 - La línea soterrada en 13,2 [kV] no sobrepasa los valores límites de ICNIRP/UE, respecto de campos

eléctricos y magnéticos de 50 [Hz]

 - La línea soterrada de 0,8 [kV] no sobrepasa los valores límites de ICNIRP/UE, respecto de campos

eléctricos y magnéticos de 50 [Hz]

 - La estación transformadora, no sobrepasa los valores límites de no sobrepasa los valores límites

de ICNIRP/UE, respecto de campos eléctricos y magnéticos de 50 [Hz].

 - El análisis de receptores descarta la influencia de esta componente sobre los receptores

identificados.

 - En virtud de lo anterior, tanto el estudio como las mediciones en terreno, demuestra que no existe

riesgo para la salud de la población debido a radiación electromagnética en la condición actual, ni

tampoco considerando las emisiones atribuibles a la operación del Proyecto.

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 38 de 41

Estudio de Campos Electromagnéticos Rev. A

8 Especificaciones del equipo de medida y certificado

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 39 de 41

Estudio de Campos Electromagnéticos Rev. A

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 40 de 41

Estudio de Campos Electromagnéticos Rev. A

9 Referencias

There are no sources in the current document.

P446-E-EST-01 Parque Fotolvoltaico Nueva Paillaco Página 41 de 41

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2-1: Elementos constitutivos de campos eléctricos y/o magnéticos relevantes**

| Línea de media tensión | Transformador | Línea soterrada | Línea BT |
| --- | --- | --- | --- |
| Línea de 13,2 kV | 3000 kVA 13,2/0,8 kV | Línea de 13,2 kV | 0,8 kV / 300 A max |

**Tabla 4-2: - Perfil Línea MT 13.2 kV 52C1 Paillaco Socoepa**

| Medida | Campo Eléctrico<br>[V/m] | Campo magnético<br>[T] |
| --- | --- | --- |
| -6 | 43,40 | 0,023 |
| -3 | 141,90 | 0,021 |
| 0 | 94,70 | 0,118 |
| 3 | 160,70 | 0,036 |

**Tabla 5-2: Valores límites de campo eléctrico**

| Punto de medida | x [m] | y[m] | Campo Eléctrico [kV/m] |
| --- | --- | --- | --- |
| Limite franja seguridad derecha | 4,00 | 1 | 0,102 |
| Limite franja seguridad izquierda | -4,00 | 1 | 0,102 |
| Valor máximo en perfil | -3,50 | 1 | 0,104 |

**Tabla 5-3: - Condiciones para cálculo del campo magnético**

| Perfil de campo magnético<br>Linea MT 13.2 kV<br>10.0<br>[μT]<br>7.5<br>magnético<br>5.0<br>ampo | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 | Col13 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 5.0<br>7.5<br>10.0<br>ampo magnético [μT]<br>**Perfil de campo magnético**<br>Linea MT 13.2 kV |  |  |  |  |  |  |  |  |  |  |  |  |
| 5.0<br>7.5<br>10.0<br>ampo magnético [μT]<br>**Perfil de campo magnético**<br>Linea MT 13.2 kV |  |  |  |  | 7.5 | 7.5 |  |  |  |  |  |  |
| 5.0<br>7.5<br>10.0<br>ampo magnético [μT]<br>**Perfil de campo magnético**<br>Linea MT 13.2 kV |  |  |  |  |  |  |  |  |  |  |  |  |
| 5.0<br>7.5<br>10.0<br>ampo magnético [μT]<br>**Perfil de campo magnético**<br>Linea MT 13.2 kV |  |  |  |  | 5.0 | 5.0 |  |  |  |  |  |  |
| 5.0<br>7.5<br>10.0<br>ampo magnético [μT]<br>**Perfil de campo magnético**<br>Linea MT 13.2 kV |  |  |  |  |  |  |  |  |  |  |  |  |
| 5.0<br>7.5<br>10.0<br>ampo magnético [μT]<br>**Perfil de campo magnético**<br>Linea MT 13.2 kV |  |  |  |  |  |  |  |  |  |  |  |  |
| C |  |  |  |  |  | .5 |  |  |  |  |  |  |
| C |  |  |  |  |  |  |  |  |  |  |  |  |
| C |  |  |  |  |  |  |  |  |  |  |  |  |
| ~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | ~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | ~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | ~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | ~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | ~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | ~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | ~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | ~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | ~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | ~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | ~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | ~~0.0~~<br>-50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] |

**Tabla 5-4: Valores límites de campo magnético**

| Punto de medida | x [m] | y[m] | Campo Magnético [T] |
| --- | --- | --- | --- |
| Limite franja seguridad derecha | 4,00 | 1 | 1,83 |
| Limite franja seguridad izquierda | -4,00 | 1 | 1,83 |
| Valor máximo en perfil | 0,00 | 1 | 2,89 |

**Tabla 5-5: - Condiciones para el cálculo de campo magnético en línea soterrada de 13,2 [kV]**

| Perfil de campo magnético<br>Circuito 13.2 kV 4.5 MW<br>5.0<br>4.0<br>[μT]<br>agnético<br>3.0 | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 | Col8 | Col9 | Col10 | Col11 | Col12 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 3.0<br>4.0<br>5.0<br>agnético [μT]<br>**Perfil de campo magnético**<br>Circuito 13.2 kV 4.5 MW |  |  |  |  |  |  |  |  |  |  |  |
| 3.0<br>4.0<br>5.0<br>agnético [μT]<br>**Perfil de campo magnético**<br>Circuito 13.2 kV 4.5 MW |  |  |  |  | 4.0 |  |  |  |  |  |  |
| 3.0<br>4.0<br>5.0<br>agnético [μT]<br>**Perfil de campo magnético**<br>Circuito 13.2 kV 4.5 MW |  |  |  |  |  |  |  |  |  |  |  |
| 3.0<br>4.0<br>5.0<br>agnético [μT]<br>**Perfil de campo magnético**<br>Circuito 13.2 kV 4.5 MW |  |  |  |  | 3.0 |  |  |  |  |  |  |
| 3.0<br>4.0<br>5.0<br>agnético [μT]<br>**Perfil de campo magnético**<br>Circuito 13.2 kV 4.5 MW |  |  |  |  |  |  |  |  |  |  |  |
| Campo m |  |  |  |  | 2.0 |  |  |  |  |  |  |
| Campo m |  |  |  |  |  |  |  |  |  |  |  |
| Campo m |  |  |  |  | 1.0 |  |  |  |  |  |  |
| Campo m |  |  |  |  |  |  |  |  |  |  |  |
| Campo m |  |  |  |  | ~~0.0~~ |  |  |  |  |  |  |
| -50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | -50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | -50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | -50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | -50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | -50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | -50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | -50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | -50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | -50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | -50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] | -50<br>-40<br>-30<br>-20<br>-10<br>0<br>10<br>20<br>30<br>40<br>50<br>Distancia al eje de la línea de transmisión [m] |

**Tabla 5-6: Valores límites de campo magnético de 13,2 [kV] (linea soterrada)**

| Punto de medida | x [m] | y[m] | Campo Magnético<br>[uT] |
| --- | --- | --- | --- |
| Limite franja seguridad derecha | 0,50 | 1 | 2,40 |
| Limite franja seguridad izquierda | -0,50 | 1 | 2,40 |
| Valor máximo en perfil | 0,00 | 1 | 2,55 |

**Tabla 5-7: - Condiciones para cálculo del campo magnético**

| Estructura | X | Y | Fase | Conductor | r | R | N | V | I | P |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Z_BT | -0,65 | -0,71 | a | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,62 | -0,71 | b | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,64 | -0,68 | c | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,54 | -0,71 | a | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,50 | -0,71 | b | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,52 | -0,68 | c | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,42 | -0,71 | a | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,39 | -0,71 | b | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,41 | -0,68 | c | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,31 | -0,71 | a | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,27 | -0,71 | b | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,29 | -0,68 | c | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,19 | -0,71 | a | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,16 | -0,71 | b | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,18 | -0,68 | c | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,08 | -0,71 | a | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |
| Z_BT | -0,04 | -0,71 | b | Al. 400 mm2 | 0,012 | 0,012 | 1 | 0,8 | 217 | 0,3 |

**Tabla 5-8: Valores límites de campo magnético**

| Punto de medida | x [m] | y[m] | Campo Magnético [T] |
| --- | --- | --- | --- |
| Limite franja seguridad derecha | 1,50 | 1 | 4,22 |
| Limite franja seguridad izquierda | -1,50 | 1 | 4,21 |
| Valor máximo en perfil | 0,00 | 1 | 6,49 |

**Tabla 5-9: Datos de placa del transformador**

| Parámetros | Valor |
| --- | --- |
| Potencia nominal | 3000 [kVA] |
| Tensión nominal | 0,8/13,2 [kV] |
| Tensión máxima | 25 [kV] |
| Frecuencia | 50 [Hz] |
| Grupo de conexión | Dy11 |
| Refrigeración | ONAN |
| Altitud máxima | 1000 [msnm] |

**Tabla 5-10: - Valores tabulados de densidad (B) de flujo magnético**

| Col1 | r [m] | B [μT] | Col4 |
| --- | --- | --- | --- |
|  | 1 | 120,0 | 120,0 |
|  | 1,5 | 35,6 | 35,6 |
|  | 2 | 15,0 | 15,0 |
|  | 2,5 | 7,7 | 7,7 |
|  | 3 | 4,4 | 4,4 |
|  | 3,5 | 2,8 | 2,8 |
|  | 4 | 1,9 | 1,9 |
|  | 4,5 | 1,3 | 1,3 |
|  | 5 | 1,0 | 1,0 |
|  | 5,5 | 0,7 | 0,7 |
|  | 6 | 0,6 | 0,6 |
|  | 6,5 | 0,4 | 0,4 |
|  | 7 | 0,3 | 0,3 |
|  | 7,5 | 0,3 | 0,3 |
|  | 8 | 0,2 | 0,2 |
|  | 8,5 | 0,2 | 0,2 |
|  | 9 | 0,2 | 0,2 |

**Tabla 6-1: - Límites de Exposición Humana a Campos Electromagnéticos de 50 [Hz]**

| Col1 | Público General | Col3 | Exposición Ocupacional | Col5 |
| --- | --- | --- | --- | --- |
| País/Entidad | Intensidad de campo<br>eléctrico [V/m] | Densidad de Flujo<br>magnético [uT] | Intensidad de campo<br>eléctrico [V/m] | Densidad de Flujo<br>magnético [uT] |
| Alemania | 5000 | 100 | 5000 | 100 |
| Argentina | 3000 | 25 | 3000 | 25 |
| Australia | 5000 | 100 | 10000 | 500 |
| Canadá | N/A | N/A | N/A | N/A |
| España | 5000 | 100 | 10000 | 500 |
| Japón | 3000 | N/A | 10000 | 500 |
| Países Bajos | 8000 | 120 | 40000 | 600 |
| Suecia | N/A | N/A | N/A | N/A |
| Suiza | 5000 | 100 | 5000 | 100 |
| ICNIRP | 5000 | 200 | 10000 | 500 |
| IEEE | 5000 | 900 | 20000 | 2700 |
| Unión Europea | 5000 | 100 | 10000 | 500 |

**Tabla 6-2: Medidas en la red de distribución existente**

| Medida | Campo<br>Eléctrico<br>[V/m] | Límite<br>ICNIRP/UE<br>[V/m] | Cumple<br>(Si/No) | Campo<br>magnético<br>[T] | Límite<br>ICNIRP/UE<br>[μT] | Cumple<br>(Si/No) |
| --- | --- | --- | --- | --- | --- | --- |
| Poste MT AW0820 (0m) | 678 | 5000 | SI | 0,043 | 100 | SI |
| Poste MT AW0820 (3m) | 254 | 5000 | SI | 0,050 | 100 | SI |
| Poste Sin Placa (Al. Futrono) (0 m) | 883 | 5000 | SI | 0,024 | 100 | SI |
| Poste Sin Placa (Al. Futrono) (3 m) | 517 | 5000 | SI | 0,027 | 100 | SI |
| Poste Sin Placa (Al. Futrono) (6 m) | 184,8 | 5000 | SI | 0,024 | 100 | SI |

**Tabla 6-3: Medidas en la línea de 13.2 kV Socoepa**

| Medida | Campo<br>Eléctrico<br>[V/m] | Límite<br>ICNIRP/UE<br>[V/m] | Cumple (Si/No) | Campo<br>magnético<br>[T] | Límite<br>ICNIRP/UE<br>[μT] | Cumple (Si/No) |
| --- | --- | --- | --- | --- | --- | --- |
| -6,0 | 43,40 | 5000 | SI | 0,023 | 100 | SI |
| -3,0 | 141,90 | 5000 | SI | 0,021 | 100 | SI |
| 0 | 94,70 | 5000 | SI | 0,118 | 100 | SI |
| 3,0 | 160,70 | 5000 | SI | 0,036 | 100 | SI |
| 6,0 | 99,40 | 5000 | SI | 0,038 | 100 | SI |

**Tabla 6-4: Análisis de receptores**

| Receptor | UTM E<br>[m] | UTM N<br>[m] | Distancia a<br>fuente [m] | Campo<br>eléctrico<br>[kV/m] | Limite<br>[kV/m] | % Limite | Campo<br>magnético<br>[μT] | Limite<br>[μT] | % Limite |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Rpa1 | 686.325 | 5.558.722 | 295 | 0 | 5 | 0,0% | 0 | 100 | 0,00% |
| Rpa2 | 686.444 | 5.558.140 | 273 | 0 | 5 | 0,0% | 0 | 100 | 0,00% |
| Rpa3 | 687.021 | 5.557.610 | 652 | 0 | 5 | 0,0% | 0 | 100 | 0,00% |
| Rpa4 | 687.039 | 5.558.410 | 95 | 0 | 5 | 0,0% | 0,01 | 100 | 0,01% |

**Tabla 6-5: - Valores determinados en borde de franja de seguridad 13,2 kV (a 4 [m] del eje de la instalación)**

| Intensidad de campo eléctrico<br>en borde de franja de seguridad<br>[V/m] | Límite<br>ICNIRP/UE<br>[V/m] | Densidad de Flujo magnético<br>en borde de franja de<br>seguridad [μT] | Límite ICNIRP/UE<br>[μT] |
| --- | --- | --- | --- |
| 102 | 5000 | 1,83 | 100 |

**Tabla 6-6: - Valores determinados en el eje de la instalación 13,2 kV**

| Intensidad de campo eléctrico<br>en borde de franja de seguridad<br>[V/m] | Límite<br>ICNIRP/UE<br>[V/m] | Densidad de Flujo magnético<br>en borde de franja de<br>seguridad [μT] | Límite ICNIRP/UE<br>[μT] |
| --- | --- | --- | --- |
| 0 | 5000 | 2,40 | 100 |

**Tabla 6-7: - Valores determinados en el eje de la instalación 13,2 kV**

| Intensidad de campo eléctrico<br>en borde de franja de seguridad<br>[V/m] | Límite<br>ICNIRP/UE<br>[V/m] | Densidad de Flujo magnético<br>en borde de franja de<br>seguridad [μT] | Límite ICNIRP/UE<br>[μT] |
| --- | --- | --- | --- |
| 0 | 5.000 | 1,84 | 100 |

**Tabla 6-8: - Valores determinados a 2,5 [m] de la subestación transformadora**

| Intensidad de campo eléctrico<br>en borde de franja de seguridad<br>[V/m] | Límite<br>ICNIRP/UE<br>[V/m] | Densidad de Flujo magnético<br>a 2 [m] del transformador<br>[μT] | Límite ICNIRP/UE<br>[μT] |
| --- | --- | --- | --- |
| 0 | 5.000 | 15 | 100 |
