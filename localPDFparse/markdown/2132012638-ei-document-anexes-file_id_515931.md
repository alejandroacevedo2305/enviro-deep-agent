---
title: Sin título
author: Nelson MO
date: D:20161214170124-04'00'
language: es
type: report
pages: 19
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INFORME ESTUDIO DE CAMPOS ELECTROMAGNÉTICOS PROYECTO SUBESTACIÓN LLANQUIHUE 220/66 KV, 90 MVA CONEXIÓN TAP-OFF
-->

# INFORME ESTUDIO DE CAMPOS ELECTROMAGNÉTICOS PROYECTO SUBESTACIÓN LLANQUIHUE 220/66 KV, 90 MVA CONEXIÓN TAP-OFF

**Nelson Morales Osorio**

**Octubre 2016**

**CONTENIDO**

1 Objetivo y alcance ............................................................................................................... 1

2. Antecedentes ...................................................................................................................... 1

3 Campo eléctrico en subestaciones de 220 KV ................................................................... 4

3.1 Medidas internacionales ............................................................................................... 4

3.2 Medidas en Chile .......................................................................................................... 4

4 Campo magnético en subestaciones de 220/66 kV ........................................................... 5

4.1 Medidas internacionales ............................................................................................... 5

5 Simulación ........................................................................................................................... 7

5.1 Simulación Patio de 66 kV Trayectoria A - B .............................................................. 8

5.2 Simulación Patio de 220 kV Trayectoria C - D .......................................................... 10

6. Radio interferencia .......................................................................................................... 12

7. Límites de radio interferencia por instalaciones de alta tensión. .................................... 13

8 Normas de referencia para exposición humana a campos electromagnéticos de 50 Hz 13

9. Conclusiones ................................................................................................................. 14

Referencias ........................................................................................................................... 15

**LISTADO DE TABLAS**

Tabla 1 Valores medidos de Campo eléctrico en estaciones transformadoras [1] ............... 4
Tabla 2 Campo magnético máximo al interior de instalaciones ............................................ 6
Tabla 3 Campo magnético máximo en la vía pública ........................................................... 6
Tabla 4 Valores límites de Interferencias de Radio, recomendados por Asociación de
Normas Canadienses ........................................................................................................... 13

**LISTADO DE FIGURAS**

Ilustración 1 Ubicación nueva Subestación Llanquihue ....................................................... 2
Ilustración 2 Líneas de acceso a la SE Llanquihue ............................................................... 2
Ilustración 3 Disposición general SE Llanquihue ................................................................ 3
Ilustración 4 Campo eléctrico a 1 m del suelo en patio de 220 kV, ..................................... 5
Ilustración 5 Campo magnético desde la pared de un transformador 220/66 kV ................ 6
Ilustración 6 Trayectorias escogidas para la simulación ....................................................... 7
Ilustración 7 Disposición de líneas equipotenciales eléctricas .............................................. 8
Ilustración 8 Campo eléctrico a 1m sobre el suelo en trayectoria A - B ............................... 8
Ilustración 9 Disposición de líneas equipotenciales magnéticas .......................................... 9
Ilustración 10 Inducción magnética a 1m sobre el suelo en trayectoria A - B ...................... 9
Ilustración 11 Disposición de líneas equipotenciales eléctricas .......................................... 10
Ilustración 12 Campo eléctrico a 1m sobre el suelo en trayectoria C - D ........................... 10
Ilustración 13 Disposición de líneas equipotenciales magnéticas ...................................... 11
Ilustración 14 Inducción magnética a 1m sobre el suelo en trayectoria C - D .................... 11
Ilustración 15 Puntos de medida de RI en subestación Snakefarm .................................... 12

Ilustración 16 Radio interferencia medida en los diferentes puntos del borde de la
subestación Snakefarm de 230 kV [4] .............................................................................. 13

1

**1 Objetivo y alcance**

En este estudio se realiza una estimación de los campos electromagnéticos de baja
y alta frecuencia provocados por la operación de equipos de la futura subestación eléctrica
Llanquihue de 220/66 KV, 90 MVA. En particular el estudio considera:

a) Estimación de la magnitud de campo eléctrico y campo magnético de frecuencia

industrial, e interferencias en alta frecuencia en el entorno de la subestación.
b) Comparación de valores estimados mediante referencias u obtenidos en los modelos

evaluados, con los respectivos valores máximos recomendados por las normas de
referencia de valores tolerables por las personas.

La estimación de valores se efectuará mediante investigación de la literatura técnica
para subestaciones en niveles de tensión y potencia similares a la subestación Llanquihue,
recopilando información de magnitudes de campo conseguidas ya sea por medida directa
en terreno o aplicación de modelos. Adicionalmente se realizará un modelo simplificado de
la disposición de barras de la subestación, mediante un programa que aplica el método de
elementos finitos, para obtener una estimación más cercana de los valores de campos
eléctrico y magnético de baja frecuencia.

Similarmente se realiza una estimación del nivel perturbador a frecuencias de radio
generado por la subestación debido al fenómeno corona, en base a medidas de terreno
informadas en la bibliografía.

Se entrega finalmente las normas aplicables en Chile para la exposición humana a
campos electromagnéticos de 50 Hz y la normativa de referencia internacional respecto de
magnitudes aceptables de radio interferencia. Estos valores se confrontan con las
estimaciones efectuadas para establecer una conclusión respecto de la emisión
electromagnética de baja y alta frecuencia provocada por la operación de los equipos de la
Subestación Llanquihue.

**2. Antecedentes**

Para realizar el refuerzo del Sistema de Subtransmisión de 66 kV en la zona de

Puerto Varas, SAESA ha resuelto realizar la construcción de una subestación
transformadora de 220/66 kV, 90 MVA, que será denominada como SE Llanquihue, en las
cercanías de la ciudad de Llanquihue. Esta SE se alimentaría mediante una conexión en
tap-off al Circuito N° 2 de la Línea 220 kV Valdivia - Puerto Montt (Rahue - Puerto Montt a
la fecha de ejecución del proyecto) perteneciente al sistema de transmisión troncal.

2

Ilustración 1 Ubicación nueva Subestación Llanquihue

El proyecto contempla el seccionamiento de la Línea 66 kV Puerto Varas-Frutillar
con el fin de alimentar radialmente las subestaciones Puerto Varas y Frutillar desde la
nueva subestación Llanquihue 220/66 kV.

La nueva subestación se ubicaría a un costado de la línea de 220 kV existente por
lo que habría sólo un pequeño tramo de línea de interconexión, propio del desvío
necesario para la acometida de la línea al patio de la subestación proyectada. De igual
forma, las líneas de 66 kV existentes, están emplazadas a muy poca distancia de la línea
de 220 kV por lo que sería necesario construir sólo pequeños tramos de línea, para
interconexión con el patio de 66 kV de la subestación.

Ilustración 2 Líneas de acceso a la SE Llanquihue

3

El equipamiento incorporado en la subestación es el siguiente:

1.- Patio de 220 kV.

1.1.- Paño de línea para conexión en tap-off a la línea Rahue-Puerto Montt, cto. N° 2.
1.2.- Espacio para paños y barra de 220 kV aptos para el seccionamiento de la línea en

configuración Interruptor y medio.
1.3.- Espacio para dos paños de línea futuros en 220 kV.
2.- Autotransformador trifásico 220/66 kV, 90 MVA,

3.- Patio de 66 kV.

3.1.- Paño de transformación 66 kV

3.2.- Dos Paños de línea para Seccionamiento de línea Puerto Varas-Frutillar, cto. N° 2.
3.3.- Dos Paños de línea para Seccionamiento de línea Puerto Varas-Frutillar, cto. N° 1.
3.4.- Barra de 66 kV con configuración de Barra Principal más Barra Transferencia.
3.5.- Paño acoplador de Barras de 66 kV.
3.6.- Espacio para un paño de línea futuro en 66 kV.
4.- Obras de interconexión de la subestación con línea 220 kV y con líneas de 66 kV existentes,

considerando seccionamiento de estas últimas.

Ilustración 3 Disposición general SE Llanquihue

4

En las siguientes secciones se entregan valores medidos o calculados de campo
eléctrico, campo magnético y radio interferencia en diferentes instalaciones similares a la
S/E en estudio. Esta información ha sido recogida de publicaciones nacionales e
internacionales.

**3 Campo eléctrico en subestaciones de 220 KV**

En el interior de una subestación eléctrica, las magnitudes del campo eléctrico son
elevadas debido a la presencia de diversos equipos y distancias limitadas entre conductores
energizados y el suelo. No obstante, a medida que se alejan de las fuentes, estos campos
se reducen fuertemente.

Para investigar sus efectos, se acostumbra caracterizar al campo eléctrico generado
por una instalación de alta tensión por el concepto “Campo eléctrico a nivel del suelo”, que
corresponde al campo eléctrico medido o calculado a 1 metro de altura sobre el suelo. Su
magnitud es proporcional al voltaje de la instalación. A continuación se entregan valores
medidos de campo eléctrico en instalaciones de 220 kV, similares a la S/E en estudio..

**3.1 Medidas internacionales**

De la referencia [1] se reproduce a continuación la Tabla I, que indica los valores
de campo medidos en líneas de transmisión y estaciones transformadoras (ET) de
diferentes voltajes, de una empresa de transmisión de energía eléctrica del Paraguay:

Tabla 1 Valores medidos de Campo eléctrico en estaciones transformadoras [1]

Se confirma que los valores de campo eléctrico en el interior de la subestación son
elevados, en torno a 5 kV/m, y que estos decaen conforme al nivel de voltaje y también al
salir de la subestación.

**3.2 Medidas en Chile**

En la figura siguiente se muestra dos perfiles del campo eléctrico medidos a 1 m
sobre el nivel del suelo, según distintas direcciones, en un patio de 220 kV de la subestación
de 220/110 kV Los Almendros. [2]

5

Ilustración 4 Campo eléctrico a 1 m del suelo en patio de 220 kV,

Sector de acceso de empalmes a edificio S/E Los Almendros [2]

Se aprecia que el campo eléctrico baja drásticamente en los límites del patio,
llegando a valores no superiores a 1 kV/m. Medidas efectuadas en otras subestaciones de
220 kV permiten afirmar que este valor, **1 kV/m**, puede considerarse el campo eléctrico

máximo existente en el borde de la subestación de 220 kV.

**4 Campo magnético en subestaciones de 220/66 kV**

Es relevante recordar que el campo magnético es producido por la circulación de
corriente y no depende del nivel de voltaje de la instalación. Por lo tanto, en la subestación
en estudio, se espera que el mayor campo magnético se presente en el nivel de tensión
menor, 66 kV, que corresponde a la magnitud de corriente mayor. A un voltaje de 66 kV,
considerando un transformador de 90 MVA, la corriente nominal es de aproximadamente
790 Amperes. En las siguientes secciones se entregan valores medidos de campo
magnético en diferentes instalaciones similares a la S/E en estudio.

**4.1 Medidas internacionales**

De la referencia [1] se reproduce a continuación las Tabla 2 y 3 (Tablas II y Tabla
III de la referencia), que presentan los valores de inducción magnética medidos en líneas
de transmisión y estaciones transformadoras (ET) de diferentes voltajes, de una empresa
de transmisión de energía eléctrica del Paraguay:

6

Tabla 2 Campo magnético máximo al interior de instalaciones

Tabla 3 Campo magnético máximo en la vía pública

En el interior de la subestación se encuentran altos valores de campo magnético,
como lo muestra la Tabla 2; sin embargo, la Tabla 3 indica que fuera de la subestación, la
magnitud del campo magnético es muy inferior, midiendo **4,3 [micro Tesla]** .

En la misma referencia [1] se ilustra el comportamiento del campo magnético,
medido y extrapolado, desde la pared de un transformador de 220/66 kV, figura que se
reproduce a continuación.

Ilustración 5 Campo magnético desde la pared de un transformador 220/66 kV

7

Se aprecia un decaimiento en proporción inversa al logaritmo de la distancia, lo
cual determina que a 20 m desde la pared del transformador, la inducción magnética es
inferior a **1 [micro Tesla].** Por lo tanto, el efecto del transformador es muy localizado, no
alcanzando a manifestarse fuera de los límites de la subestación.

**5 Simulación**

La metodología utilizada consiste en una modelación simplificada de los
conductores de barras energizados, utilizando elementos finitos y el software utilitario
QuickField [3] para la solución de campos. Se escoge la trayectoria A - B para el patio de
66 kV y la trayectoria C - D para el patio de 220 kV, ambas mostradas en la figura siguiente.

Ilustración 6 Trayectorias escogidas para la simulación

El resultado del estudio de campo eléctrico y magnético se presenta en la forma de
perfiles de campo evaluado a una altura de 1,0 m sobre el suelo, para cada trayectoria. La
línea transversal en la figura indica la superficie del suelo. En los gráficos se indica la
posición horizontal relativa de las barras.

8

**5.1 Simulación Patio de 66 kV Trayectoria A - B**

Ilustración 7 Disposición de líneas equipotenciales eléctricas

Ilustración 8 Campo eléctrico a 1m sobre el suelo en trayectoria A - B

En el lado de 66 kV, considerando un transformador de 90 MVA, la corriente nominal
es de aproximadamente 790 Amperes.

9

Ilustración 9 Disposición de líneas equipotenciales magnéticas

Ilustración 10 Inducción magnética a 1m sobre el suelo en trayectoria A - B

Se observa en el gráfico del campo eléctrico y de la inducción magnética, mayores
valores en los bordes de la configuración de barras, produciéndose una compensación de
campos en las barras centrales. En el borde más próximo del patio de 66 kV, los valores

estimados son:

Campo eléctrico: 318 [V/m]
Inducción magnética: 4,4 [micro Tesla]

10

**5.2 Simulación Patio de 220 kV Trayectoria C - D**

Ilustración 11 Disposición de líneas equipotenciales eléctricas

Ilustración 12 Campo eléctrico a 1m sobre el suelo en trayectoria C - D

En el lado de 220 kV, considerando un transformador de 90 MVA, la corriente
nominal es de aproximadamente 240 Amperes.

11

Ilustración 13 Disposición de líneas equipotenciales magnéticas

Ilustración 14 Inducción magnética a 1m sobre el suelo en trayectoria C - D

Se observa en el gráfico del campo eléctrico mayores valores en los bordes de la
configuración de barras, produciéndose una compensación de campos en la barra central.
La inducción magnética en cambio presenta altos valores bajo las barras. En el borde más
próximo del patio de 220 kV, los valores estimados son:

Campo eléctrico: 230 [V/m]
Inducción magnética: 0,38 [micro Tesla]

12

**6. Radio interferencia**

En un conductor de una instalación de alta tensión, está aplicado un elevado nivel
de voltaje respecto de tierra (decenas o centenas de kilo Volts), lo cual provoca un campo
eléctrico extremadamente alto en la superficie del conductor (del orden de 100 veces mayor
que el existente a nivel del suelo). Este campo eléctrico, aumentado aún más por la
presencia de irregularidades en la superficie del conductor (hebras, polvo, insectos, gotas
de agua, etc.) provoca la ionización del aire en su entorno inmediato: el aire pierde
localmente su propiedad dieléctrica, produciéndose gran cantidad de pequeñas descargas
eléctricas en la superficie del conductor. El efecto luminoso de estas descargas ha dado
nombre a este fenómeno, conociéndose como “corona” y uno de sus efectos es producir
interferencias electromagnéticas en frecuencias que van desde unos pocos Hz a los GHz
(10 [9] Hz), por tanto abarca todo el espectro de las telecomunicaciones.

Dado que este fenómeno se genera por campo eléctrico, depende en consecuencia
del voltaje y su efecto será mayor a mayor nivel de voltaje. En este caso interesa en 220

kV.

En la referencia [4] se informa de medidas efectuadas en puntos del perímetro
interior de la subestación Snakefarm, operando en 230 kV; la figura siguiente muestra un
esquema de la subestación señalando los puntos de medida.

Ilustración 15 Puntos de medida de RI en subestación Snakefarm

Los valores medidos se reproducen en el gráfico siguiente:

13

Ilustración 16 Radio interferencia medida en los diferentes puntos del borde de la subestación Snakefarm de

230 kV [4]

Se aprecia que el nivel de radio interferencia generado por la subestación resulta
aproximadamente 50 [dB/1V/m. Empleando la ley de decaimiento del campo perturbador
con la distancia, para trasladar dichos valores a una distancia 15 m hacia el exterior de la
subestación, se rebaja 8 dB, quedando los valores en **42** **[dB/1**  **V/m].**
**7. Límites de radio interferencia por instalaciones de alta tensión.**

En la referencia [6], se propone la siguiente recomendación para el límite de
campo electromagnético perturbador de alta frecuencia (radio interferencia) emitida por
líneas de transmisión y subestaciones, según su nivel de tensión:

Tabla 4 Límite de Interferencias de Radio, Asociación de Normas Canadienses

|Voltaje nominal entre fases|Nivel de Radio Interferencia|
|---|---|
|**(KV)**|**(dB/ 1μV/m)**|
|Menos de 70|43|
|70 - 200|49|
|200 - 300|53|
|400 - 600|60|
|Sobre 600|63|
|Para líneas de transmisión, valores indicados a 15 m de la fase externa y a 0,5 MHz<br>Para subestaciones, valores medidos a 15 m del cerco del recinto de la subestación|Para líneas de transmisión, valores indicados a 15 m de la fase externa y a 0,5 MHz<br>Para subestaciones, valores medidos a 15 m del cerco del recinto de la subestación|

Para una subestación de 220 kV, el valor límite corresponde a **53 [dB/1**  **V/m].**
**8 Normas de referencia para exposición humana a campos electromagnéticos de 50**

**Hz**

14

En Chile no existe reglamentación relativa a los valores límites permitidos de
exposición de las personas a los campos electromagnéticos de frecuencia industrial. No
obstante, la regulación ambiental que rige el tema de emisiones señala que de no existir
una regulación nacional, debe aplicarse como norma de referencia aquella que se
encuentre vigente en estados específicos. El Decreto 95 del Ministerio Secretaría General
de la Presidencia, publicado en el Diario Oficial del 07.12.2002, indica en su Artículo 7:

“
**Artículo 7** .- _Las normas de calidad ambiental y de emisión que se utilizarán como_
_referencia para los efectos de evaluar si se generara o presenta el riesgo indicado en la_
_letra a) y los efectos adversos señalados en la letra b), ambas del artículo 11 de la ley, serán_
_aquellas vigentes en los siguientes Estados: República Federal de Alemania, República de_
_Argentina, Australia, República Federativa del Brasil, Confederación de Canadá, Reino de_
_España, Estados Unidos Mexicanos, Estados Unidos de Norteamérica, Nueva Zelandia,_
_Reino de los Países Bajos, República de Italia, Japón, Reino de Suecia y Confederación_
_Suiza. Para la utilización de las normas de referencia, se priorizará aquel Estado que posea_
_similitud, en sus componentes ambientales, con la situación nacional y/o local.”_

La recomendación de uso más frecuente para público general y exposición
permanente, es la publicada por la ICNIRP [5], organismo no gubernamental, reconocido
por la Organización Mundial de la Salud (OMS) como referente en el tema de campos
electromagnéticos, que establece **5.000 [V/m]** para el campo eléctrico y **100 [micro Tesla]**
para la inducción magnética, valores que han sido considerados en la normativa de varios
países señalados en la nómina.

**9.** **Conclusiones**

De los resultados obtenidos en la investigación bibliográfica referente a efectos
provocados por subestaciones de los niveles de voltaje y potencia similares a la subestación
Llanquihue 220/66 KV 90 MVA, se concluye:

El campo eléctrico existente a un metro de altura sobre el suelo en el borde inmediato
de subestaciones de 220/66 kV no supera **1,0** **[kV/m]** según referencias, y **0,318 [kV/m]**
según la simulación específica para la subestación Llanquihue, por tanto inferior al límite de
**5,0 [kV/m]** considerado por la ICNIRP como seguro.

La inducción magnética máxima existente a un metro de altura sobre el suelo en el
borde inmediato de subestaciones de 220/66 kV con potencias similares a los 90 MVA de
la subestación en estudio, es de **4,3 [micro Tesla]**, según referencias, y **4,4 [micro Tesla]**
según la simulación específica para la subestación Llanquihue, por tanto inferior al límite de
**100 [micro Tesla]** considerado seguro por la ICNIRP.

El máximo ruido de radio frecuencia (interferencia a las señales de radio y televisión)
generado por una subestación similar en niveles de voltaje máximo, 220 kV, es de **50**

**[dB/1**  **V/m]** en el perímetro interior de la subestación; 15 m hacia el exterior de la

15

subestación, se rebaja 8 dB, quedando en **42** **[dB/1**  **V/m]** inferior a **53 [dB/1**  **V/m]**
considerado máximo permitido para subestaciones de 220 kV.

**Referencias**

[1] Patricia Arnera, Pedro Issouribehere, et all.
“Evaluación de campos eléctricos y magnéticos en instalaciones de la Administración
Nacional de Electricidad - ANDE, Asunción, Paraguay. Trabajo presentado al Comité
de estudio 36 en el X Encuentro Regional Latinoamericano de la CIGRE, Mayo 2003,
Puerto Iguazú, Argentina.

[2] Nelson Morales; Efraín Asenjo; Cristian López:

“Medición de campo eléctrico de frecuencia industrial bajo líneas de transmisión y
en subestaciones”, Anales V ERLAC (Quinto Encuentro Regional Latino Americano
de la Cigré, Paraguay, mayo 1993)

[3] Students' QuickField (TM) Finite Element Analysis System
Version 5.8 User's Guide

Copyright (C) Tera Analysis Company, 2010.

[4] R. T. Carter, A. W. Grille, G. M. Bazile, N. D. Perkins, S. F. Mauser,
”Analysis of radio interference and substation modifications for uprating a 115-kV

substation to 230 kV “

IEEE Transactions on Power Delivery, Vol. PWRD-2, No. 2, April 1987

[5] Informe de ICNIRP ( Comisión Internacional para la Protección contra la Radiación
No Ionizante) “Interim guidelines on limits of exposure to 50/60 Hz Electric and
Magnetic Fields” 1998, Health Physics,74,4,494-522

[6] Association canadienne de normalisation
Valeurs limites et methods de mesure du bruit électromagnétique (0,15 à 30 MHz)
produit par les reseaux de courant alternatif. CAN3- C108.3.1 - M84. Octobre 1984.

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4: Límite de Interferencias de Radio, Asociación de Normas Canadienses**

| Voltaje nominal entre fases | Nivel de Radio Interferencia |
| --- | --- |
| **(KV)** | **(dB/ 1μV/m)** |
| Menos de 70 | 43 |
| 70 - 200 | 49 |
| 200 - 300 | 53 |
| 400 - 600 | 60 |
| Sobre 600 | 63 |
| Para líneas de transmisión, valores indicados a 15 m de la fase externa y a 0,5 MHz<br>Para subestaciones, valores medidos a 15 m del cerco del recinto de la subestación | Para líneas de transmisión, valores indicados a 15 m de la fase externa y a 0,5 MHz<br>Para subestaciones, valores medidos a 15 m del cerco del recinto de la subestación |
