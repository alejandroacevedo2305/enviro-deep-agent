---
title: Sin título
author: Desconocido
date: D:20171205173425-03'00'
language: es
type: report
pages: 23
has_toc: True
has_tables: False
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Categoría Edificio : II
  - Tipo de Suelo : C
-->

MEMORIA DE CÁLCULO

**LOTEO ANTUPIREN - EDIFICIO (A** **0** **/g = 0.6)**

**ANTUPIREN #10.001 - PEÑALOLEN**

**REGIÓN METROPOLITANA**

1. **Introducción:**

El conjunto de edificios consta de estructuras de hormigón armado de 4 pisos,
estructurados en ambos sentidos en base a muros y marcos capaces de resistir las
cargas verticales y sísmicas. Tanto muros y marcos poseen un espesor de 12 cm y la
combinación de estos, en ambas direcciones, provee un sistema capaz de resistir los
esfuerzos de corte y flexo tracción a la que estarán sometidos bajo la acción sísmica.

El sistema de fundaciones consiste en cimientos corridos bajo muros, verificados a la
acción de cargas estáticas y dinámicas, asegurando la transmisión de estas al sello de
fundación. Al mismo tiempo, las tensiones de trabajo del suelo son compatibles con la
capacidad de soporte indicadas en el informe de mecánica de suelos respectivo.

El entrepiso está conformado por un campo de losas de hormigón armado de un
espesor determinado según dimensiones y forma de trabajo de cada losa en
particular. Este campo conforma un diafragma rígido, distribuyendo en forma
proporcional, los esfuerzos sísmicos entre los elementos del edificio según la rigidez
de cada uno de ellos.

2. **Cargas y sobrecargas de uso:**

2.1. Losa Cielo 1° a 3° Piso (Dormitorios) (Losa e = 14 cm.)

Carga Muerta adicional : 0,100 T/m2
Sobrecarga : 0,200 T/m2
0,300 T/m2

2.2. Losa Cielo 1° a 3° Piso (Pasillos) (Losa e = 14 cm.)

Carga Muerta adicional : 0,100 T/m2
Sobrecarga : 0,400 T/m2
0,500 T/m2

2.2. Losa Cielo 4° Piso (Techo) (Losa e = 12 cm.)

Carga Muerta adicional : 0,100 T/m2
Sobrecarga : 0,100 T/m2
0,100 T/m2

**3.** **Fuerzas Horizontales:**

Cargas sísmicas: Análisis dinámico según NCh 433 Of. 96. - Mod. 2009 + Dcto 61 Of. Dic.

2011

# Categoría Edificio : II

Zona Sísmica : 2
# Tipo de Suelo : C

Ro : 4.00
Ao/g : 0.6
Corte basal mínimo (%) : 10.5
Corte basal máximo (%) : 34.7
Fórmula de combinación : CQC

Parámetros del espectro de diseño:

I : 1.0
Ao/g : 0.6
To : 0.4
p : 1.6
S : 1.05

**4.** **Materiales**

4.1. Hormigón Armado

Hormigón G-20 f ́c = 200 Kg/cm2
Acero A630-420-H f y = 4200 Kg/cm2

4.2. Estructura Metálica

Acero A 370-240-ES.

**5.** **Tensiones admisibles del suelo.**

Estático = 2.0 Kg/cm2
Dinámico = 2.8 Kg/cm2

6. **Normas**

Cargas : NCh 1537 (cargas y sobrecargas)
Análisis Sísmico : NCh 433 Of. 96 - Mod. 2009 + Dcto. 61 Of. Dic. 2011

Diseño : ACI 318 - 08
Hormigones : NCh 170

7. **Analisis Sismico**

El análisis de la estructura se realiza mediante el software de cálculo ETABS,
modelándose una maqueta en 3D en base a elementos finitos.
En este modelo se incorporan todos los elementos del edificio y se carga con los
valores descritos en el punto 2 anterior. Para el caso sísmico se considera un análisis
de tipo modal según la norma NCh 433 Of. 96 - Mod. 2009 + Dcto. 61 Of. Dic. 2011,
con la consideración de un factor de modificación de respuesta R = 4 según el punto
21.1.1.7 del Decreto 60 of Nov. 2011, que permite muros ordinarios en edificios de
hasta 5 pisos y un factor A 0 = 0.6 por la cercanía a la falla de San Ramón

**7.1.** **Vista 3D Modelo ETABS**

**7.2.** **Espectro de respuesta**

De acuerdo al artículo 12 del Decreto 61, el espectro de diseño se puede tabular
según las siguientes fórmulas

Se calcula el espectro considerando los valores del punto 3 descrito anteriormente y
se carga en el software de cálculo.

**7.3.** **Parámetros generales del edificio**

Una vez analizado el edificio se obtienen los parámetros generales del edificio, tales
como el peso sísmico de este, el periodo de mayor masa para cada una de sus
direcciones, cortes basales mínimos y máximos, factor de reducción (R*),
deformaciones sísmicas, etc. los cuales son detallados a continuación

**7.4.** **Parámetros vibratorios**

Al hacer un estudio de cualquier estructura es necesario buscar la cantidad de modos
de vibrar suficiente para alcanzar sobre el 90% de masa acumulada según las
indicaciones de la nch 433 of 1996.
En el caso particular de este edificio se puede ver que se alcanza sobre el 99% de la
masa acumulada para las direcciones X e Y.

**7.5.** **Deformaciones y separación entre edificios**

Acorde al punto 5.9 de la Nch 433 of 1996 y actualizado en el artículo 9 con el decreto
61 of Nov. 2011, las deformaciones relativas a los centros de gravedad no pueden
superar el 2 por mil de la altura de entrepiso y un punto cualquiera de la planta no
puede superar el 1 por mil de la altura cn respecto a su centro de gravedad.
En las siguientes tablas se puede observar que estas condiciones se cumplen para los
sismos en ambos sentidos

Para la separación entre edificios es necesario determinar la distancia al medianero
según el articulo 6 de la norma Nch 433 of 2009 y multiplicarlo por 2R*/3.
Acorde a los valores expuestos en el punto 7.3 anterior tenemos que la separación
debe ser:

s = 2*0.34 = 0.68 cm

Además de lo anterior, también se debe respetar un valor mínimo correspondiente al 2
por mil de la altura del edificio. Ante esta afirmación se debe tomar una separación
entre edificios s = 5 cm.

8. **DISEÑO DE ELEMENTOS**

**8.1.** **Diseño de muros y vigas**

En este punto se entregan los valores máximos de esfuerzos para cada elemento,
junto con el diseño y armadura requerida según la norma ACI 318 - 08.

**8.2.** **Diseño de losas**

El diseño de las losas se realizó utilizando el software de análisis SAFE 8,
considerando la geometría total del sistema de losas, las cargas y sobrecargas
indicadas en el punto 2 anteriormente expuesto.
El sistema de losas consiste en un campo de losas de hormigon armado de espesor
14 cm en pisos 1° a 3° y 12 cm en el piso 4°. Este campo está apoyado en muros de
hormigón armado de espesor 12 cm. Si se considera que la rigidez del muro es menor
que la rigidez de la losa, es necesario articular la unión entre ambos, por lo que se
prescinde de suples de empotramiento en los encuentros de ambos.

_Planta típica de losas_

_Modelación en SAFE_

_- Deformaciones admisibles_

Realizada la modelación se procede a cargar la estructura con los valores
mencionados y se procede a verificar las deformaciones máximas

Acorde al capítulo 9.5 del ACI 318-08, la deformación a largo plazo debe ser menor
que L/480, con L como el lado menor de la losa deformada. Calculada la losa los
resultados son los siguientes

Flecha máxima permitida f = L/480 = 453/480 = 0.94 cm

Flecha máxima calculada f = 0.80 cm < 0.94 cm => OK

_-_
_Diseño y armadura de losas_

Verificada la flecha máxima es momento de armar la losa y como primer paso se debe
determinar la armadura mínima a repartición impuesta por el ACI 318-08, capítulo
7.12.2.1

Acorde a la reglamentación la cuantía mínima es r = 0.0018, la que llevada a una losa
de 14 cm implica una cuantía mínima f8a20

Utilizando el diseño automático del software SAFE 8, se puede imponer que solo se
muestre en pantalla los sectores que necesiten sobre la cuantía mínima, para la
armadura inferior de la losa, y el valor necesario para los momentos negativos y la
armadura superior de esta.

_Diseño armadura inferior dirección X_

_Diseño armadura superior dirección X_

_Diseño armadura inferior dirección Y_

_Diseño armadura superior dirección Y_

Como se puede ver en las figuras anteriores, no necesita una cuantía inferior mayor a
f8a20 (mínimo normativo) y los refuerzos negativos en la cara superior de la losa son
valores acordes a una losa de estas dimensiones y solicitado a las cargas de uso
domiciliario.

Nota: Los valores de refuerzos negativos que se ven en las figuras anteriores tienen
como significado el área de acero necesario por cada metro de ancho de losa (cm2/m)

**8.3.** **Cálculo y diseño de fundaciones**

Al igual que el cálculo de losas, las fundaciones fueron analizadas y diseñadas con el
software SAFE 8.
Para este cálculo se consideran las reacciones estáticas del edificio, junto con las
reacciones sísmicas entregadas por el programa ETABS para los modos principales
de vibración. Se analizan los cargas de servicio según las siguientes combinaciones

 - _Análisis de tensiones admisibles:_

Estático: Peso Propio + Carga muerta + Sobrecarga
Sísmico: Peso Propio + Carga muerta + Sobrecarga + Sismo (X e Y)

 - _Análisis de levantamientos máximos:_

Sísmico: Peso Propio + Carga muerta + Sismo (X e Y)

Las tensiones del suelo no pueden superar los valores entregados en el punto 5 y el
levantamiento de la fundaciones no debe superar al 20% del área de la fundación
acorde a la norma Nch 433 of 1996.

_Modelación en SAFE_

_- Verificación de tensiones admisibles_

Como primer paso es necesario verificar que el caso estático (Peso Propio + Carga
Muerta + Sobrecarga) no supere el valor de 2.0 kg/cm2.
En la siguiente figura se detalla con color gris los valores máximos de la tensión del
suelo, sin superar nunca el valor límite.

_Diagrama de tensiones caso estático_

Verificado el caso estático es necesario pasar al caso sísmico. Como se explicó
anteriormente, no se deberá superar la tensión del suelo de 2.8 kg/cm2 ni superar un
levantamiento del 20% en las zapatas. Se presentará a continuación la figura que
muestre la mayor tensión de suelo (en este caso Peso Propio + Carga Muerta +
Sobrecarga + Sismo X), seguida por la figura que muestre el mayor levantamiento
( Peso Propio + Carga Muerta + SismoY)

_Diagrama de tensiones caso sísmico (PP + CM + SC + SX)_

_Diagrama de levantamiento caso sísmico (PP + CM + SY)_

Al iual que en el caso estático, se puede apreciar en color gris las tensiones máximas
de suelo, las que no superan nunca el valor límite impuesto. En el caso de
levantamiento se puede ver en color blanco todo el sistema de fundaciones apoyado
completamente, salvo un sector lateral de color violeta, que indica levantamiento. Este
sector representa menos del 20% en el sistema competo de fundaciones
comprometido.

______________________

Rafael Gatica
Ingeniero Civil