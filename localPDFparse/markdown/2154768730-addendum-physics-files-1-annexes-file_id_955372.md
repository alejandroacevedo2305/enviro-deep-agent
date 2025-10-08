---
title: Sin título
author: Nelson MO
date: D:20220729100139-04'00'
language: es
type: report
pages: 17
has_toc: False
has_tables: True
extraction_quality: high
---

**INFORME**

**ESTUDIO DE CAMPOS ELECTROMAGNÉTICOS PARQUE SOLAR**

**FOTOVOLTAICO MAITENES**

**Julio 2022**

1

Contenido

1. Objetivos y Alcance del Estudio .......................................................................................... 3

2. Descripción del Proyecto ..................................................................................................... 3

3. Campo magnético de centros de transformación ............................................................... 6

4. Análisis del campo electromagnético de la línea ................................................................ 8

5. Normativa de referencia para radio interferencia ............................................................ 13

6. Normas de referencia para campos electromagnéticos de 50 Hz .................................... 13

7. Conclusiones...................................................................................................................... 15

_4_ Referencias ........................................................................................................................ 17

2

**1.** **Objetivos y Alcance del Estudio**

Este Informe presenta una estimación de los campos electromagnéticos de baja y alta frecuencia

que pueden presentarse en el entorno de las instalaciones del Parque Solar Fotovoltaico Maitenes,

durante su operación.

Se entrega información respecto del campo electromagnético generado por centros de

transformación y los resultados de una simulación para el campo eléctrico y el campo magnético en

el entorno de la línea de transmisión. Para determinar la magnitud de estos campos, se utiliza un

programa computacional que aplica el método de elementos finitos para modelar la configuración

a estudiar y resolver la ecuación diferencial parcial que rige el comportamiento de los campos en la

región a estudiar.

Los valores indicados se confrontan con las recomendaciones y límites admisibles para establecer

finalmente una conclusión respecto al impacto ambiental de las instalaciones del Proyecto, desde

el punto de vista técnico de la emisión electromagnética de baja frecuencia.

Similarmente se realiza una estimación del nivel perturbador a frecuencias de radio generado por

la línea de transmisión debido al fenómeno corona, en base a expresiones simplificadas de uso

habitual, y se compara con valores límites establecidos por recomendaciones internacionales.

**2.** **Descripción del Proyecto**

El Proyecto Parque Solar Fotovoltaico Maitenes corresponde a un proyecto nuevo, localizado en la

Región Metropolitana, provincia Cordillera, comuna de Pirque.

Consiste en la construcción y operación de un Parque Solar Fotovoltaico que producirá energía

mediante la conversión de energía solar en energía eléctrica por medio de 15.232 módulos fotovoltaicos

para evacuar la energía generada mediante una línea de media tensión que se conecta a la red de

distribución existente.

Para el Proyecto, se considera una vida útil de 30 años. La vida útil del Proyecto se podrá extender en

la medida que las condiciones de mercado justifiquen la inversión.

3

La realización del proyecto tiene por objetivo la generación de energía eléctrica mediante la captación

y transformación de la energía solar, para inyectar una potencia AC de 5 MW al Sistema Eléctrico

Nacional.

El Parque consta de 2 centros de transformación. Contará con una línea eléctrica aérea de 12 kV,

para realizar posteriormente la inyección al poste de distribución propiedad de CGE. En la Figura 1

se muestra la ubicación del Parque Fotovoltaico Maitenes y la línea eléctrica de 12 kV.

_Figura 1: Ubicación del proyecto y línea de evacuación_

La transmisión aérea en la que operará el proyecto tiene las siguientes características:

4

_Tabla 1 características de la línea de evacuación_

|Sistema|Corriente alterna trifásica|
|---|---|
|**Frecuencia**|50 Hz|
|**Tensión nominal**|12 kV|
|**Origen de la Línea de Media Tensión**|Parque Fotovoltaico<br>Maitenes|
|**Final de la Línea de Media Tensión**|Punto de conexión (CGE)|
|**N° de circuitos**|1|
|**Conductor aéreo**|CAIRO (AL 236 mm2)|
|**N° de conductores por fase**|1|
|**Potencia nominal**|5 MW|

El conductor de la línea tiene una sección de 236 mm [2] y un diámetro total de 8,67 mm. Esta línea

consta de un único tramo aéreo simple, circuito en configuración horizontal, compuesto por 13 vanos

desde el inicio al final de la línea aérea. El poste es de concreto, similar a un poste de alumbrado

público, de 10m de alto, enterrado a 1,8 a 2 m.

5

_Ilustración 1 Detalle del poste_

**3.** **Campo magnético de centros de transformación**

La densidad de flujo B está muy relacionada con la potencia aparente nominal de un transformador.

En base a una serie de experiencias y resultados obtenidos en una amplia gama de potencias,

International Commission on Non‐Ionizing Radiation Protection sugiere una relación simple para el

valor efectivo de la inducción magnética en la vecindad de un transformador:

B rms (r) = k Tr P N /r [3] [micro Tesla] P N :

Potencia Nominal del transformador [kVA]

r: Distancia desde el centro del transformador [m]

k Tr : Coeficiente de Campo [ms/A], [Tm [3] /VA]

Un valor establecido de k Tr en la misma referencia es: 0,04 Tm [3] /kVA.

Esta expresión indica que la densidad de flujo magnético de transformadores decrece rápidamente al

alejarse del transformador (relación inversa con la tercera potencia de la distancia). De acuerdo a esta

6

expresión, con un transformador de 3.000 KVA para cada Centro de Transformación, la densidad de

flujo magnético B a una distancia D desde el centro del transformador es la siguiente:

_Tabla 2: Variación de la inducción magnética con distancia al transformador_

|Distancia<br>D[m]|2|3|4|5|6|7|8|Col9|9|10|
|---|---|---|---|---|---|---|---|---|---|---|
|Inducción<br>magnética<br>B [micro<br>Tesla]|15|4,4|1,88|0,96|0,56|0,35|0,35|0,234|0,164|0,12|

Fuente: Elaboración propia

Se observa que a partir de 5m del transformador, la inducción magnética se reduce a un valor inferior a

1,0 [micro Tesla]. Por lo tanto, el área de influencia para el campo magnético de un transformador de

3.000 kVA abarca menos de 5m en torno al transformador.

Respecto a lo indicado en Canadian Standars Association, Standard CAN3 C108.3.1-M84, “Limits and

Measurement Methods of Electromagnetic Noise from AC Power Systems 0.15 to 30 MHz, se entrega

un ábaco que se reproduce en la Figura siguiente, de valores medidos en transformadores y switchgear

de HV y MV.

7

_Ilustración 2 Reducción de la densidad de flujo magnético de equipos con la distancia_

Fuente: Referencia [5]

Por lo tanto, el campo magnético generado por el Centro de Transformación, incluyendo

transformador y equipos anexos, a pesar de que puede ser intenso en la proximidad inmediata de

los Centros, decrece rápidamente siendo no relevante a 8 m de distancia, pues decae a menos de 1

[micro Tesla], no representando impacto hacia el exterior del Parque.

Con respecto al campo eléctrico, los equipos son en general encapsulados y además se ubican en un

recinto cerrado, lo que anula el campo eléctrico hacia el exterior.

**4.** **Análisis del campo electromagnético de la línea**

En la vecindad de una línea aérea energizada, el campo eléctrico se debe al voltaje aplicado al

conductor, el cual está expuesto al aire (no existe aislamiento sólido, el aislamiento está definido

por espaciamientos de aire). Sus unidades son Volt por metro (V/m) o Kilo Volt por metro (KV/m)

en alta tensión; en el caso en estudio, 12 kV entre fases y 12/√3 KV fase a tierra.

El campo magnético se debe a la corriente que circula por los conductores. La magnitud

representativa del campo magnético es la “Inducción Magnética” o “Densidad de Flujo Magnético”

8

B **,** que tiene como unidad de medida práctica el mili Gauss (1 mG = 10 [-3] Gauss) o el micro Tesla (1T

= 10 [-6] Tesla ) y se relacionan por: 1 T = 10 mG.

Para investigar los efectos de los campos electromagnéticos, se acostumbra a caracterizar al campo

eléctrico y el campo magnético cerca de una instalación de alta tensión por el concepto “Campo a

nivel del suelo”, que corresponde al campo eléctrico o magnético medido o calculado a 1 metro de

altura sobre el suelo, en ausencia de otros objetos.

En este caso, el análisis se realiza en un plano transversal a la línea, de 50mx50m; la línea transversal

en las figuras señala la superficie del suelo; las líneas rojas indican el borde de la franja de seguridad.

El símbolo ⇩ en los gráficos muestra la ubicación del poste. A continuación, se presentan los

resultados para el campo eléctrico, el campo magnético y la radio interferencia.

Para el estudio del campo magnético se consideró una potencia de 9 MW; por lo tanto la corriente

de fase resulta 377 Amperes.

9

_Ilustración 3: Malla de elementos finitos_

_Ilustración 4 Distribución de equipotenciales eléctricas_

10

_Ilustración 5 Campo eléctrico a 1m sobre el suelo bajo la línea_

_Ilustración 6 Distribución de equipotenciales magnéticas_

11

_Ilustración 7 Inducción magnética a 1m sobre el suelo bajo la línea_

_Ilustración 8Radio interferencia generada por la línea_

La línea verde indica el valor a la distancia de norma.

12

**5.** **Normativa de referencia para radio interferencia**

La referencia Association canadienne de normalisation, Valeurs limites et methods de mesure du

bruit électromagnétique, que indica el nivel de perturbación radio eléctrica aceptable generada por

líneas de transmisión o subestaciones, a una frecuencia de 0,5 MHz, y a 15 m de distancia lateral de

la fase externa, tabla que se reproduce a continuación:

_Tabla 3 Nivel de perturbación radiofónica aceptable a 0,5 MHz_

Para una instalación de 12 kV, el límite correspondiente es 43 [dB/ (1V/m)] .

**6.** **Normas de referencia para campos electromagnéticos de 50 Hz**

En nuestro país no existe reglamentación relativa a los valores límites permitidos de exposición de

las personas a los campos electromagnéticos de frecuencia industrial. No obstante, la regulación

ambiental que rige el tema de emisiones señala que de no existir una regulación nacional, debe

aplicarse como norma de referencia aquella que se encuentre vigente en estados específicos. El

Decreto No 40 del Ministerio del Medio Ambiente, “Aprueba Reglamento del Sistema de Evaluación

de Impacto Ambiental”, publicado el 12-08-2013, y que entró en vigencia el 24-12-2013, indica en

su Artículo 11:

13

_“Las normas de calidad ambiental y de emisión que se utilizarán como referencia para los efectos de_

_evaluar si se genera o presenta el riesgo indicado en la letra a) y los efectos adversos señalados en_

_la letra b), ambas del artículo 11 de la Ley, serán aquellas vigentes en los siguientes Estados:_

_República Federal de Alemania, República Argentina, Australia, República Federativa del Brasil,_

_Canadá, Reino de España, Estados Unidos Mexicanos, Estados Unidos de América, Nueva Zelandia,_

_Reino de los Países Bajos, República Italiana, Japón, Reino de Suecia y Confederación Suiza. Para la_

_utilización de las normas de referencia, se priorizará aquel Estado que posea similitud en sus_

_componentes ambientales, con la situación nacional y/o local, lo que será justificado_

_razonablemente por el proponente._

La recomendación de uso más frecuente para público general y exposición permanente, es la

publicada por la ICNIRP, organismo no gubernamental reconocido por la Organización Mundial de

la Salud como referente en el tema de campos electromagnéticos y salud, que establece como

límites seguros 5.000 [V/m] para el campo eléctrico y 200 [micro Tesla] para la inducción magnética,

valores incorporados en la normativa de varios países mencionados en la nómina anterior.

14

**7.** **Conclusiones**

De los resultados obtenidos en la investigación bibliográfica y en las simulaciones efectuadas, se

concluye:

 - En las Estaciones Centrales de inversión el campo eléctrico queda confinado al interior de la

instalación; por su parte, la densidad de flujo magnético a una distancia de 5m desde el centro del

transformador, alcanza apenas **0,96 [micro Tesla],** inferior al límite de **100 [micro Tesla]** considerado

seguro para las personas por la ICNIRP [4].

 - La magnitud máxima de campo eléctrico existente a un metro de altura sobre el suelo

inmediatamente bajo la línea operando en 12 kV es 135 [Volt/m]; valor muy inferior al límite de

5.000 [V/m] considerado seguro para las personas por la ICNIRP [4].

 - La magnitud máxima de inducción magnética existente a un metro de altura sobre el suelo

inmediatamente bajo la línea operando en 12 kV es 0,2 [micro Tesla], inferior al límite de 100 [micro

Tesla] considerado seguro para las personas por la ICNIRP [4].

 - El máximo ruido de radio frecuencia (interferencia a las señales de radio) generado por la línea,

es inferior el máximo de **43 [dB/1mV/m]** propuesto como límite tolerable para una línea de media

tensión [5]. Este bajo nivel de ruido justifica el hecho de que regularmente no se considere

significativa la interferencia provocada por líneas de media tensión.

Del análisis efectuado se obtuvo los siguientes valores característicos:

_Tabla 4 Valores finales para planta fotovoltaica y línea de 12 kV_

|Campo eléctrico Inducción magnética Radio<br>[V/m] [micro Tesla] Interferencia<br>[dB/uV/m]|Col2|Col3|Col4|
|---|---|---|---|
|**Centro transformación**|0|1,0|**- **|
|**Valor máximo**|135|1,21|**-0,41**|
|**Valor en borde franja**|122|1,14|**-0,93**|
|**Valor a 15m conductor**|64|0,51|**10,20**|
|**Valor límite**|5.000|200|**43**|
|**Cumplimiento**|**SI**|**SI**|**SI**|

15

De acuerdo a lo mostrado en la Tabla anterior, se concluye que las instalaciones del Proyecto

Fotovoltaico Maitenes, satisfacen la normativa vigente respecto de la componente campos

electromagnéticos.

16



**8.** **Referencias**

[1] Students' QuickField (TM) Finite Element Analysis System

Version 5.8 User's Guide

Copyright (C) Tera Analysis Company, 2010.

[2] N. Morales, "Fenómeno corona en líneas de transmisión y sus efectos".

Publicación T(P)/9, Departamento de Ingeniería Eléctrica. Noviembre 1986.

[3] Association canadienne de normalisation, Valeurs limites et methods de mesure du bruit

électromagnétique (0,15 à 30 MHz) produit par les reseaux de courant alternatif. CAN3

C108.3.1 - M84. Octobre 1984.

4 International Commission on Non‐Ionizing Radiation Protection

ICNIRP Publication - 2010

ICNIRP Guidelines for limiting exposure to time‐varying electric and magnetic fields (1 hz100 kHz)

Published in: Health Physics 99(6):818‐836; 2010

[5] Canadian Standars Association, Standard CAN3 C108.3.1-M84, “Limits and Measurement

Methods of Electromagnetic Noise from AC Power Systems 0.15 to 30 MHz

17