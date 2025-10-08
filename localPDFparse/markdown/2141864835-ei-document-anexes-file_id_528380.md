---
title: Sin título
author: Nelson MO
date: D:20181114160921-03'00'
language: es
type: report
pages: 21
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ANEXO 2-3
-->

# ANEXO 2-3

## ESTUDIOS DE CAMPOS ELECTROMAGNÉTICOS

ANAGEA.COM

#### INFORME ESTUDIO DE CAMPOS ELECTROMAGNÉTICOS “PROYECTO AMPLIACIÓN S/E RÍO TOLTÉN”

**Nelson Morales Osorio**

**Noviembre 2018**

**CONTENIDO**

1. Objetivos y alcance del estudio ................................................................................................. 3

2. Antecedentes .............................................................................................................................. 4

3. Normas en Chile para exposición a campos electromagnéticos de 50 Hz ............................ 6

4. Límites de radio interferencia provocada por instalaciones de alta tensión. ....................... 7

5. Modelación de la Subestación ................................................................................................... 7

6. Radio interferencia en subestación ........................................................................................ 12

5. Conclusiones ............................................................................................................................ 14

6. Área de influencia .................................................................................................................... 14

7. REFERENCIAS .......................................................................................................................... 15

8. ANEXO ...................................................................................................................................... 16

A.1 Radio interferencia barras ........................................................................................................ 16

A.2 Radio interferencia líneas ......................................................................................................... 19

**LISTADO DE FIGURAS**

Figura 1 Ubicación de ampliación Río Toltén .................................................................................. 3
Figura 2. Esquema ampliación subestación Río Toltén 220 kV ..................................................... 4
Figura 3 Corte por paño de línea Cautín 2 ....................................................................................... 5
Figura 4 Capacidad de transmisión de las lìneas ............................................................................ 5
Figura 5. Trayectorias seleccionadas para evaluar campo en la subestación .............................. 8
Figura 6. Campo eléctrico a 1m sobre el suelo, bajo barras ........................................................... 9
Figura 7. Inducción magnética a 1m sobre el suelo, bajo barras ................................................. 10
Figura 8. Campo eléctrico a 1m sobre el suelo, bajo líneas .......................................................... 11
Figura 9. Inducción magnética a 1m sobre el suelo, bajo líneas .................................................. 12
Figura 10. Radio interferencia generada por las barras de la subestación ................................. 13
Figura 11. Radio interferencia generada por las líneas de la subestación .................................. 13

**LISTADO DE TABLAS**

Tabla 1. Características del conductor de fase ................................................................................ 6

Tabla 2 Límites de Radio Interferencias por Asociación de Normas Canadienses [2] ................. 7

Tabla 3. Radio interferencia en borde de subestación ................................................................. 14

3

**1.** **Objetivos y alcance del estudio**

En este Informe se efectúa una estimación de los campos electromagnéticos de baja y
alta frecuencia que pueden presentarse durante la operación del Proyecto Ampliación de
Subestación Río Toltén, en el interior y en el borde de la subestación Río Toltén producto de
su ampliación. El Proyecto se ubica en la región de la Araucanía, provincia de Cautín, comuna
de Pitrufquén.

**Figura 1 Ubicación de ampliación Río Toltén**

Se presenta en primer lugar las características de los equipos que se incorporan a la
ampliación de la subestación Río Toltén.

Posteriormente se entrega los valores límites recomendados de radio interferencia
provocada por instalaciones de alta tensión y las normas de referencia aplicables en Chile
respecto de la exposición humana a campos electromagnéticos de 50 Hz.

La estimación de campos en la subestación se obtiene mediante modelación de las
barras y líneas de la subestación ocupando la técnica de elementos finitos y la aplicación del
software QuickField para la determinación de los campos. Se realiza una estimación del nivel
perturbador a frecuencias de radio generado por la subestación debido al fenómeno corona,
en base a expresiones de cálculo de radio interferencia de uso general.

4

Finalmente, estos valores se confrontan con los respectivos valores límites fijados por
las normas, con el objeto de establecer una conclusión referente al impacto ambiental de las
nuevas instalaciones del proyecto, desde el punto de vista técnico de la emisión
electromagnética de baja y alta frecuencia.

**2.** **Antecedentes**

El Proyecto consiste en la construcción de una subestación seccionadora de la línea
2x220 kV Cautín - Ciruelos, en configuración doble barra, interruptor y medio, con plataforma
y barras extendidas para 3 diagonales adicionales, una de las cuales servirá para normalizar el
tap-off perteneciente a Transmisora Valle Allipén, y espacio para 2 diagonales adicionales, el
que quedará dentro del muro perimetral de la Subestación.

Esta ampliación hará uso de terrenos, caminos de acceso, casa de mando y
equipamientos varios asociados al tap-off existente ubicándose en el terreno colindante por el
lado norte con la actual subestación Río Toltén. En la Figura siguiente se muestra un esquema
de las instalaciones correspondientes a la ampliación.

**Figura 2. Esquema ampliación subestación Río Toltén 220 kV**

5

**Figura 3 Corte por paño de línea Cautín 2**

Las barras tendrán capacidad para 1000 MVA de potencia, para lo cual estarán
constituidas por doble conductor AAC Lupine de 2500 MCM.

La actual línea de transmisión 2x220 kV Ciruelos - Cautín, al ser seccionada quedará
dividida en dos (2), siendo estos tramos denominados:

- Línea de transmisión 2x220 kV Ciruelos - Río Toltén.

- Línea de transmisión 2x220 kV Cautín - Río Toltén.

Para los nuevos tramos de seccionamiento, se usará el mismo conductor actual: ACSR

Grosbeak, con lo cual, la capacidad de transmisión se mantendrá en los 192,8 MVA, para una
temperatura máxima del conductor de 50°C, declarada por Transelec, propietario de la línea.

**Figura 4 Capacidad de transmisión de las lìneas**

La línea de transmisión a seccionar posee un (1) conductor por fase. Las principales
características del conductor de fase que se utiliza, se detallan a continuación:

6

**Tabla 1. Características del conductor de fase**

|Tipo|ACSR|
|---|---|
|Calibre|636 [MCM]|
|Sección|375 [mm2]|
|Diámetro|25,15 [mm]|
|Peso|1,302 [kg/m]|
|Tensión nominal de rotura|11.427 [kgf]|
|Cantidad de alambres|26/7|
|Diámetro de alambre de aluminio|3,97 [mm]|
|Diámetro de alambre de acero|3,09 [mm]|
|Coeficiente de dilatación lineal|18,9·10-6[1/oC]|
|Temperatura máxima de diseño|50 [oC]|
|Resistencia a 25°C AC|0,0904 Ω/km|

**3.** **Normas en Chile para exposición a campos electromagnéticos de 50 Hz**

En nuestro país no existe reglamentación relativa a los valores límites permitidos de
exposición de las personas a los campos electromagnéticos de frecuencia industrial. No
obstante, la regulación ambiental que rige el tema de emisiones señala que de no existir una
regulación nacional, debe aplicarse como norma de referencia aquella que se encuentre
vigente en estados específicos.

El Decreto No 40 del Ministerio del Medio Ambiente, “Aprueba Reglamento del Sistema
de Evaluación de Impacto Ambiental”, publicado el 12-08-2013, y que entró en vigencia el 2412-2013, indica en su Artículo 11:

_Artículo 11.- Normas de referencia._
_Las normas de calidad ambiental y de emisión que se utilizarán como referencia para los efectos_
_de evaluar si se genera o presenta el riesgo indicado en la letra a) y los efectos adversos_
_señalados en la letra b), ambas del artículo 11 de la Ley, serán aquellas vigentes en los siguientes_
_Estados: República Federal de Alemania, República Argentina, Australia, República Federativa_
_del Brasil, Canadá, Reino de España, Estados Unidos Mexicanos, Estados Unidos de América,_
_Nueva Zelandia, Reino de los Países Bajos, República Italiana, Japón, Reino de Suecia y_
_Confederación Suiza. Para la utilización de las normas de referencia, se priorizará aquel Estado_
_que posea similitud en sus componentes ambientales, con la situación nacional y/o local, lo que_
_será justificado razonablemente por el proponente._

7

La recomendación de uso más frecuente para público general y exposición
permanente, es la publicada por la ICNIRP [1], organismo no gubernamental, reconocido por
la Organización Mundial de la Salud (OMS) como referente en el tema de los campos
electromagnéticos y efecto sobre las personas, que establece **5.000 [V/m]** para el campo
eléctrico y **200 [micro Tesla]** para la inducción magnética, valores recogidos por la
normativa de diversos países señalados en la nómina anterior.

**4.** **Límites de radio interferencia provocada por instalaciones de alta tensión.**

En la referencia [2], se propone la siguiente recomendación para el límite de campo
electromagnético perturbador de alta frecuencia (radio interferencia) emitida por líneas de
transmisión y subestaciones, según su nivel de tensión:

**Tabla 2 Límites de Radio Interferencias por Asociación de Normas Canadienses [2]**

|Voltaje nominal entre fases [KV]|Radio Interferencia [dB/1μV/m]|
|---|---|
|Menos de 70|43|
|70 - 200|49|
|200 - 300|53|
|400 - 600|60|
|Sobre 600|63|

Para líneas de transmisión, los valores indicados son a 15 m de la fase externa y a 0,5
MHz. Para subestaciones, los valores son a 15 m del borde de la subestación. Para una línea

de transmisión o subestación de 220 kV, el valor límite corresponde **a 53 [dB/1uV/m].**

**5.** **Modelación de la Subestación**

La metodología utilizada consiste en una modelación de los conductores de las barras
y líneas de 220 kV de la subestación, utilizando elementos finitos y el software utilitario
QuickField [1] para la solución del campo eléctrico y magnético en un plano transversal.

El resultado del estudio de campo eléctrico se presenta en la forma de un perfil de
campo evaluado a una altura de 1,0 m sobre el suelo, a través de la trayectoria A1-A2 y la
trayectoria B1 - B2 mostrada en la Figura siguiente; se escogió el perfil A1 - A2 por atravesar
las barras y el perfil B1 - B2 por atravesar las líneas; mediante la información de ambos
perfiles se tendrá el efecto en los bordes de la subestación. En el perfil de barras, los
conductores se consideraron a una altura de 10 m sobre el suelo, con 4,0 m de separación
entre los conductores de fases; en el perfil de líneas, los conductores se consideraron a una
altura de 7 m sobre el suelo, con 4,5 m de separación entre los conductores de fases.

8

**Figura 5. Trayectorias seleccionadas para evaluar campo en la subestación**

A continuación, se presentan los gráficos resultados de los análisis en cada trayectoria.
Se incluye en los gráficos la ubicación relativa de las barras o líneas, según corresponda y las
líneas verticales rojas que señalan los bordes de la subestación.

9

**Figura 6. Campo eléctrico a 1m sobre el suelo, bajo barras**

Se observa un valor alto de campo cerca de las barras, pero el campo eléctrico decae
rápidamente al alejarse de las fuentes, llegando a 600 [V/m] en el borde de la subestación.

Para determinar la magnitud del campo magnético, se considera el doble de la
capacidad de transmisión de las líneas a seccionar, es decir 400 MVA, lo cual define una
corriente de 1.050 Amperes por conductor.

10

**Figura 7. Inducción magnética a 1m sobre el suelo, bajo barras**

Para el campo magnético se observa también alto valor cerca de las barras, pero decae
rápidamente al alejarse de las fuentes, llegando a 4,7 [micro Tesla] en el borde de la

subestación.

A continuación, se presenta el análisis para las líneas; en este caso se considera una
altura de conductor de 7 m sobre el suelo y 4,5 m de separación entre fases.

11

**Figura 8. Campo eléctrico a 1m sobre el suelo, bajo líneas**

Se aprecia una concentración de campo en torno a las líneas, pero bajando al alejarse
de ellas, llegando al valor de 350 [V/m] en el borde de la subestación.

Para determinar la magnitud del campo magnético, se considera una capacidad de

transmisión de las líneas a seccionar, de 200 MVA, lo cual define una corriente de 524

Amperes por conductor.

12

**Figura 9. Inducción magnética a 1m sobre el suelo, bajo líneas**

El comportamiento del campo magnético en este caso es similar al de barras, con
máximos bajo líneas, pero reduciendo en magnitud al alejarse, llegando a 2,3 [micro tesla] en

el borde de la subestación.

**6.** **Radio interferencia en subestación**

En el ANEXO se incluye el listado de salida del programa LINEAS, de elaboración
propia, que ocupa el método de simulación de cargas [4] para evaluar el campo eléctrico
superficial de los conductores y la radio interferencia, aplicado a las barras y líneas de la
subestación.

El resultado para las barras se presenta en la Figura siguiente, evaluada desde la barra
1; la línea verde indica el valor en el borde de la subestación:

13

**Figura 10. Radio interferencia generada por las barras de la subestación**

El resultado para las líneas se presenta en la Figura siguiente, evaluada desde la línea

Cautín 2; la línea verde indica el valor en el borde de la subestación:

**Figura 11. Radio interferencia generada por las líneas de la subestación**

En el borde de la subestación, la radio interferencia es:

14

**Tabla 3. Radio interferencia en borde de subestación**

|Col1|[dB/ 1μV/m]|
|---|---|
|RI Generado por barras|33,2|
|RI Generada por líneas|37,5|

**5.** **Conclusiones**

De la modelación efectuada a la subestación, se puede concluir lo siguiente:

**a)** **Campo eléctrico**
De acuerdo a los resultados de las modelaciones, la magnitud de campo eléctrico existente a
un metro de altura sobre el suelo en el borde de la subestación de 220 kV, no supera 600

[V/m]; por tanto inferior al límite de 5.000 [V/m] considerado como seguro para público
general en la normativa ICNIRP.

**b)** **Campo magnético**
El valor de campo magnético en el borde de la subestación resultante de las modelaciones es
4,7 [micro Tesla], inferior al límite de 200 [micro Tesla] considerado como seguro para
público general en la normativa ICNIRP.

**c)** **Radio Interferencia**
El máximo ruido de radio frecuencia (interferencia a las señales de radio) generado por la
subestación en condiciones de norma (0,5 MHz y a 15 m del borde de la subestación), es 37,5

[dB/ 1  V/m], inferior al límite máximo de 53 [dB/ 1(V/m].

**6.** **Área de influencia**

Considerando los resultados indicados anteriormente, y las distancias establecidas por
las normativas referenciadas, se estima que el área de influencia de la Ampliación Subestación

Río Toltén 220 kV, se extiende hasta 20 m hacia afuera, desde el borde de la Subestación.

15

**7.** **REFERENCIAS**

[1] ICNIRP Guidelines for limiting exposure to time varying electric and magnetic fields (1
Hz - 100 kHz)
Published in: Health Physics 99(6):818 - 836; 2010
International Commission on Non-Ionizing Radiation Protection

ICNIRP Publication - 2010

[2] Association canadienne de normalisation, Valeurs limites et methods de mesure du bruit
électromagnétique (0,15 à 30 MHz) produit par les reseaux de courant alternatif. CAN3
C108.3.1 - M84. Octobre 1984.

16

**8.** **ANEXO**

En este ANEXO se incluye el listado de salida del programa LINEAS, de elaboración
propia, que ocupa el método de simulación de cargas [4] para evaluar el campo eléctrico
superficial de los conductores y la radio interferencia, aplicado a las barras y líneas de la
subestación.

Nota : el programa utiliza punto decimal en vez de coma; no utiliza tilde para acentos.

**A.1 Radio interferencia barras**

CAMPO ELECTRICO Y POTENCIAL INDUCIDO EN TORNO A LINEAS DE TRANSMISION

Numero total de conductores : 6

Numero de conductores activos : 6

|Fase|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
|Numero de subconductores|2|2|2|2|2|2|
|Radio del subconductor<br>(cm)|2.3150|2.3150|2.3150|2.3150|2.3150|2.3150|
|Separacion entre<br>subconductores (cm)|20.00|20.00|20.00|20.00|20.00|20.00|
|Ubicacion lateral del conductor<br>(m)|-4.000|0.000|4.000|63.000|67.000|71.000|
|Altura conductor sobre el suelo<br>(m)|10.000|10.000|10.000|10.000|10.000|10.000|

FASE -RADIO HAZ (cm) -RADIO COND. EQUIV. (cm)

1 10.000 6.804

2 10.000 6.804

3 10.000 6.804

4 10.000 6.804

5 10.000 6.804

6 10.000 6.804

Matriz de coeficientes (amplif. por (2  ))

5.6833 1.6290 .9905 .0427 .0382 .0343

1.6290 5.6833 1.6290 .0480 .0427 .0382

.9905 1.6290 5.6833 .0544 .0480 .0427

17

.0427 .0480 .0544 5.6833 1.6290 .9905

.0382 .0427 .0480 1.6290 5.6833 1.6290

.0343 .0382 .0427 .9905 1.6290 5.6833

Matriz de capacitancias (amplif. por 1/(2  ))

.1937 -.0499 -.0194 -.0006 -.0005 -.0004

-.0499 .2046 -.0499 -.0007 -.0005 -.0005

-.0194 -.0499 .1937 -.0010 -.0007 -.0006

-.0006 -.0007 -.0010 .1937 -.0499 -.0194

-.0005 -.0005 -.0007 -.0499 .2046 -.0499

-.0004 -.0005 -.0006 -.0194 -.0499 .1937

Potenciales de conductores ( KVolts)

( 127.0170, .0000 ) 127.0170
( -63.5085, -110.0000 ) 127.0170
( -63.5085, 110.0000 ) 127.0170
( 127.0170, .0000 ) 127.0170
( -63.5085, -110.0000 ) 127.0170
( -63.5085, 110.0000 ) 127.0170

Cargas en conductores (Cb)/( 2  )

( 28.9789, 3.3555 ) 29.1725
( -16.1910, -27.9956 ) 32.3404
( -11.6384, 26.7984 ) 29.2166
( 29.0273, 3.3200 ) 29.2166
( -16.1493, -28.0196 ) 32.3404
( -11.5834, 26.7742 ) 29.1725

Gradientes superficiales (kVef./cm)

( 7.7079, .8925 ) 7.7594
( -4.3065, -7.4463 ) 8.6020
( -3.0956, 7.1279 ) 7.7711
( 7.7208, .8831 ) 7.7711
( -4.2954, -7.4527 ) 8.6020
( -3.0810, 7.1215 ) 7.7594

_Radio interferencia a 15 de fase externa [dB/ 1μV/m]_

|RI1|RI2|RI3|Col4|RI|
|---|---|---|---|---|
|30,46|32,71|32,58||34,14|

18

**Figura A 1 Radio interferencia en borde de subestación**

19

**A.2 Radio interferencia líneas**

CAMPO ELECTRICO Y POTENCIAL INDUCIDO EN TORNO A LINEAS DE TRANSMISION

Numero total de conductores : 6

Numero de conductores activos : 6

|Fase|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
|Numero de subconductores|1|1|1|1|1|1|
|Radio del subconductor (cm)|1.2575|1.2575|1.2575|1.2575|1.2575|1.2575|
|Ubicacion lateral del conductor (m)|-4.500|0.000|4.500|11.700|16.200|20.700|
|Altura conductor sobre el suelo (m)|7.000|7.000|7.000|7.000|7.000|7.000|

Matriz de coeficientes (amplif. por (2  ))

7.0151 1.1841 .6148 .2789 .1883 .1345

1.1841 7.0151 1.1841 .4443 .2789 .1883

.6148 1.1841 7.0151 .7823 .4443 .2789

.2789 .4443 .7823 7.0151 1.1841 .6148

.1883 .2789 .4443 1.1841 7.0151 1.1841

.1345 .1883 .2789 .6148 1.1841 7.0151

Matriz de capacitancias (amplif. por 1/(2  ))

.1474 -.0231 -.0085 -.0030 -.0018 -.0013

-.0231 .1508 -.0226 -.0055 -.0027 -.0018

-.0085 -.0226 .1491 -.0137 -.0055 -.0030

-.0030 -.0055 -.0137 .1491 -.0226 -.0085

-.0018 -.0027 -.0055 -.0226 .1508 -.0231

-.0013 -.0018 -.0030 -.0085 -.0231 .1474

Potenciales de conductores ( KVolts)

( 127.0170, 0.0000 ) 127.0170
( -63.5085, -110.0000 ) 127.0170
( -63.5085, 110.0000 ) 127.0170
( 127.0170, 0.0000 ) 127.0170
( -63.5085, -110.0000 ) 127.0170
( -63.5085, 110.0000 ) 127.0170

20

Cargas en conductores (Cb)/( 2  )

( 20.5417, 1.6612 ) 20.6088
( -11.4958, -18.9623 ) 22.1748
( -10.3104, 19.1542 ) 21.7529
( 21.7432, 0.6480 ) 21.7529
( -10.6739, -19.4368 ) 22.1748
( -8.8322, 18.6203 ) 20.6088

Gradientes superficiales (kVef./cm)

( 16.3354, 1.3211 ) 16.3887
( -9.1418, -15.0793 ) 17.6340
( -8.1991, 15.2320 ) 17.2985
( 17.2908, 0.5153 ) 17.2985
( -8.4882, -15.4567 ) 17.6340
( -7.0236, 14.8074 ) 16.3887

_Radio interferencia a 15 de fase externa [dB/ 1μV/m]_

|RI1|RI2|RI3|Col4|RI|
|---|---|---|---|---|
|40,03|42,04|41,91||43,47|

**Figura A 2. Radio interferencia en borde de subestación**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1.: Características del conductor de fase****

| Tipo | ACSR |
| --- | --- |
| Calibre | 636 [MCM] |
| Sección | 375 [mm2] |
| Diámetro | 25,15 [mm] |
| Peso | 1,302 [kg/m] |
| Tensión nominal de rotura | 11.427 [kgf] |
| Cantidad de alambres | 26/7 |
| Diámetro de alambre de aluminio | 3,97 [mm] |
| Diámetro de alambre de acero | 3,09 [mm] |
| Coeficiente de dilatación lineal | 18,9·10-6[1/oC] |
| Temperatura máxima de diseño | 50 [oC] |
| Resistencia a 25°C AC | 0,0904 Ω/km |

**Tabla 2: Límites de Radio Interferencias por Asociación de Normas Canadienses [2]****

| Voltaje nominal entre fases [KV] | Radio Interferencia [dB/1μV/m] |
| --- | --- |
| Menos de 70 | 43 |
| 70 - 200 | 49 |
| 200 - 300 | 53 |
| 400 - 600 | 60 |
| Sobre 600 | 63 |

**Tabla 3.: Radio interferencia en borde de subestación****

| Col1 | [dB/ 1μV/m] |
| --- | --- |
| RI Generado por barras | 33,2 |
| RI Generada por líneas | 37,5 |
