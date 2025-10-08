---
title: Microsoft Word - 20140514 Informe Electromagnético Mesamávida.doc
author: Pablo
date: D:20151026183752-02'00'
language: es
type: report
pages: 28
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  -  2 2 2 2 (A.1.1)
  -  x y,   2
  - E X  x y,     q k x  x k  q k x  x
  - X  x y,  
  -  2 2 2 2 (A.1.2)
  -  x y,   2
  - E Y  x y,     q k y  y k  q k y  y
  - Y  x y,  
  -  x y,    2 2
  - B X  x y,    n  i k  y  y
  ... y 6 secciones más
-->

_ADENDA No 1_
_DECLARACIÓN DE IMPACTO AMBIENTAL_
_PARQUE EÓLICO LOS OLMOS_

## Anexo 7: Análisis de los Campos Electromagnéticos Sistema de Distribución Parque Eólico Los Olmos

_Inversiones Bosquemar Ltda._ KAITEK Consultores en Ciencias Ambientales Ltda.-URRUTIA& Asociados

### PROYECTO PARQUE EÓLICO LOS OLMOS

## ANÁLISIS CAMPOS ELÉCTRICOS Y MAGNÉTICOS SISTEMA DE DISTRIBUCIÓN PARQUE EÓLICO LOS OLMOS

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

1

### PROYECTO PARQUE EÓLICO LOS OLMOS

**ANÁLISIS**
**CAMPOS ELÉCTRICOS Y MAGNÉTICOS**

**SISTEMA DE DISTRIBUCIÓN**
**PARQUE EÓLICO LOS OLMOS**

### CONTENIDOS

1. Introducción ...........................................................................................................................................2

2. Conclusiones ...........................................................................................................................................4

3. Antecedentes ..........................................................................................................................................4

3.1. Inducción de campos eléctricos y magnéticos ...............................................................................4

3.2. Zonas de estudio .............................................................................................................................8

4. Cálculo de Campos Eléctricos y Magnéticos ..............................................................................................8

4.1 Circuitos C1, C3 y C4. ......................................................................................................................9

4.2 Circuito C2. ................................................................................................................................... 11

4.3 Circuitos C3 y C4. ......................................................................................................................... 13

4.4 Circuitos C5 y C6. ......................................................................................................................... 15

4.5 Circuitos C1, C2, C3 y C4. ............................................................................................................. 19

5. Referencias .......................................................................................................................................... 22

6 Apéndices ............................................................................................................................................. 23

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

2
### 1. Introducción

El Proyecto Parque Eólico Los Olmos se ubica en la comuna de Mulchén,

Provincia de Biobío, VIII Región del Biobío. El proyecto consiste en la

construcción y operación de un parque eólico compuesto por 38

aerogeneradores de 3,3 MW de potencia cada uno, con una potencia

instalada de 125,4 MW. El parque eólico cuenta con una subestación

elevadora, la cual se describe en el documento “Análisis Campos

Electromagnéticos Subestación PE Los Olmos”. La disposición geográfica del

parque y equipos asociados se muestra en la **figura 1.1** .

Este estudio tiene por objetivo calcular el campo eléctrico y magnético

máximo inducido por los cables canalizados subterráneamente y un cruce

aéreo en los escenarios donde se concentra mayor flujo de corriente. Los

resultados son comparados con las normas de referencia aplicables en Chile

respecto de la exposición humana a campos electromagnéticos.

Los resultados se obtienen a partir de los métodos de cálculo

implementados en MATLAB R2009b, junto con los parámetros y

configuraciones geométricas de los distintos circuitos eléctricos.

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

3

**C1**

**C3**

**C6**

**C5**

**Fig.** **1.1.** Disposición geográfica de equipos eléctricos del Proyecto Parque Eólico Los Olmos.

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

4

### 2. Conclusiones

Los valores calculados de campo eléctrico y magnético producidos

por el sistema de transmisión interno del Parque Eólico Los Olmos en 33 kV

cumple los límites recomendados por la normativa Argentina y por el

ICNIRP, por lo que la operación de los distintos grupos de circuitos de

aerogeneradores no representa riesgo para las personas que puedan quedar

expuestas dentro de la faja de servidumbre. El valor máximo de campo

eléctrico obtenido es 0,7693 kV/m, cuyo límite recomendado es 3.0 kV/m

por la norma Argentina y 5.0 kV/m por la ICNIRP. Por otra parte, se obtuvo

como valor máximo de campo magnético 15,87 μT, teniéndose límites

recomendados de 25 μT (Norma Argentina) y 100 μT (ICNIRP). En zonas

alejadas de la faja de servidumbre, la inducción electromagnética

producida por el cableado aéreo y subterráneo es incluso menor.

Es importante destacar que los valores máximos de campo eléctrico

y campo magnético inducidos por la operación del Proyecto Parque Eólico

Los Olmos y a las distancias consideradas son muy bajos en comparación a

los límites recomendados. En el caso del campo magnético, los resultados

obtenidos son inclusive menores a los campos magnéticos a que se ven

sometidas las personas por la manipulación de artefactos eléctricos.

### 3. Antecedentes

#### 3.1. Inducción de campos eléctricos y magnéticos

En esquemas de generación eléctrica, la potencia eléctrica es

transmitida a 50 Hz a través de cables o bien en forma de línea aérea. La

presencia de tensiones y corrientes en circuitos eléctricos provoca la inducción

de campos eléctricos y magnéticos.

La inducción de campos eléctricos se debe a la presencia de cargas

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

5

eléctricas (voltajes) en conductores. La intensidad del campo eléctrico se

relaciona con la magnitud de las tensiones, características de los conductores,

y de la distancia a la que se evalúa. Típicamente, los resultados en un lugar

determinado se informan en kV/m y es mayor a menor distancia de la fuente.

La inducción de campos magnéticos es debida a la circulación de

corriente eléctrica a través de conductores. La intensidad de campo

magnético está relacionada con la magnitud de las corrientes, la distancia a

la que se evalúa la inducción y el efecto de la inducción en el suelo. Esto

último no es significativo en proximidades de los conductores. Los resultados

de la inducción de campos magnéticos en un lugar determinado se informan

en μT y es mayor a menor distancia de la fuente.

Es de interés verificar que los valores máximos de campos eléctricos y

magnéticos a los que quedan expuestos personas, animales o plantas deben

estar por debajo de umbrales considerados perjudiciales.

Chile no cuenta con reglamentación relativa a los valores límites

permitidos de exposición de las personas a los campos electromagnéticos de

frecuencia industrial, sin embargo, el Decreto Supremo N° 40/12 del Ministerio

de Medio Ambiente, en su artículo 11, establece que:

_“Las normas de calidad ambiental y de emisión que se utilizarán como_

_referencia para los efectos de evaluar si se genera o presenta el riesgo_

_indicado en la letra a) y los efectos adversos señalados en la letra b),_

_ambas del artículo 11 de la ley, serán aquellas vigentes en los siguientes_

_Estados: República Federal de Alemania, República de Argentina,_

_Australia, República Federativa del Brasil, Canadá, Reino de España,_

_Estados Unidos Mexicanos, Estados Unidos de América, Nueva Zelandia,_

_Reino de los Países Bajos, República Italiana, Japón, Reino de Suecia y_

_Confederación Suiza. Para la utilización de las normas de referencia, se_

_priorizará aquel Estado que posea similitud en sus componentes_

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

6

_ambientales, con la situación nacional y/o local, lo que será justificado_

_razonablemente por el proponente”_

Las Tablas N°3.1 y N°3.2 presentan las principales normas de referencia

aplicables en Chile, de acuerdo a lo señalado en el Artículo anterior.

**Tabla N°3.1.-** Límites de exposición Humana a campos electromagnéticos de 50 HZ. Público

General.

|País|Campo<br>Eléctrico<br>[kV/m]|Campo<br>Magnético<br>[μT]|Observación|
|---|---|---|---|
|Alemania|5,0|100,0|-|
|Argentina|3,0|25,0|Borde franja de seguridad o<br>perímetro de subestación|
|Australia|5,0|100,0|-|
|Canadá|N.E|N.E|-|
|España|CEU|CEU|-|
|Italia|5,0|10,0|Sólo para Líneas de<br>Transmisión (LT); 3,0 μT LT<br>nueva|
|Japón|3,0|No existe|Sólo para LT|
|U.S.A|2,0 - 11,8|15,0 -<br>20,0|-|
|Reino de los Países Bajos<br>(Gobierno)|ICNIRP|ICNIRP|0,4 μT. para nuevas líneas<br>aéreas cerca de recintos con<br>niños|
|Reino de los Países Bajos<br>(Consejo de Salud)|8,0|120,0|-|
|Suecia|No<br>explícito|No<br>explícito|-|
|Suiza|5,0|100,0|1,0 μT nuevas LT y cableados|
|ICNIRP|5,0|100,0|-|
|IEEE|5,0|904,0|-|
|Consejo Unión Europea<br>(CEU)|5,0|100,0|-|

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

7

**Tabla N°3.2.-** Límites de exposición Humana a campos electromagnéticos de 50 HZ.

Exposición Ocupacional.

|País|Campo<br>Eléctrico<br>[kV/m]|Campo<br>Magnético<br>[μT]|Observación|
|---|---|---|---|
|Alemania|5,0|100,0||
|Argentina|3,0|25,0|Borde franja de seguridad o<br>perímetro de subestación|
|Australia|10,0 -<br>30,0|500,0||
|Canadá|N.E|N.E||
|España|CEU|CEU||
|Italia|5,0|10,0|Sólo para LT; 3,0 μT LT nueva|
|Japón|ICNIRP|ICNIRP||
|U.S.A|2,0 - 11,8|15,0 -<br>20,0||
|Reino de los Países Bajos<br>(Gobierno)|ICNIRP|ICNIRP|0,4 μT. para nuevas líneas<br>aéreas cerca de recintos con<br>niños|
|Reino de los Países Bajos<br>(Consejo de Salud)|40,0|600,0||
|Suecia|No<br>explícito|No<br>explícito||
|Suiza|5,0|1,0|1,0 μT nuevas LT y cableados|
|ICNIRP|10,0|500,0||
|IEEE|20,0|2710,0||
|Consejo Unión Europea<br>(CEU)|10,0|500,0||

Además de la necesaria comparación de los resultados de campos

eléctricos y magnéticos con los límites recomendados, son de interés los

valores típicos de la inducción electromagnética a que se ven sometidas

las personas por la operación de artefactos eléctricos domiciliarios. Por

ejemplo, mediciones experimentales a una distancia de 30 cm indican que un

secador de pelo produce 80 V/m y hasta 7 μT. Una aspiradora puede emitir

50 V/m y hasta 20 μT. Es importante destacar que a menor distancia estas

cantidades crecen, por lo tanto las personas pueden verse sometidas a

inducciones electromagnéticas mayores. A 3 cm el secador de pelo y la

aspiradora pueden emitir hasta 2000 μT y 800 μT respectivamente.

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

8

#### 3.2. Zonas de estudio

Respecto al equipamiento eléctrico del Proyecto Parque Eólico Los

Olmos se realizan evaluaciones electromagnéticas próximas a los siguientes

circuitos eléctricos:

Circuitos C1, C3 y C4 de media tensión.

- Circuito C2 de media tensión.

Circuitos C3 y C4 de media tensión.

Circuitos C5 y C6 de media tensión.

Circuitos C1, C2, C3 y C4 de media tensión.

Dado que son circuitos subterráneos que se canalizan de manera

paralela, se calcula el campo magnético dentro de una faja de 10 m. El campo

eléctrico es cero fuera de los cables debido a que presentan pantalla

metálica, por lo que se produce el efecto de Jaula de Faraday. La evaluación

se realiza considerando la corriente máxima dada la generación conectada en

cada circuito.

Además, se evalúa un cruce de canales con cableado aéreo

correspondiente a los Circuitos C5 y C6. En este caso se evalúa junto al campo

magnético, el campo eléctrico inducido por este cableado en una faja de 10

metros de ancho.

### 4. Cálculo de Campos Eléctricos y Magnéticos

Los cálculos de campos eléctricos y magnéticos se realizan utilizando un

análisis bidimensional (ver Anexo 1 y 2).

La evaluación electromagnética debida a los circuitos canalizados

subterráneamente se realiza a nivel del suelo. Esto representa el caso con

mayor inducción a la que las personas eventualmente pueden quedar

expuestas por la operación de los cables de media tensión. Si se considera

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

9

una altura mayor, aumenta la distancia desde los cables por lo que se

obtendrán resultados cuya magnitud será menor. Es importante destacar que

debido a la pantalla metálica presente en los cables de media tensión

considerados en el Proyecto Parque Eólico Los Olmos, el campo eléctrico sólo

sucede al interior del cable. Lo anterior es equivalente a que el conductor

no induce campo eléctrico al exterior del cable porque se produce la

denominada Jaula de Faraday (cubierta metálica a potencial cero respecto al

suelo).

La evaluación electromagnética debida a los circuitos aéreos se realiza

1,8 metros sobre el suelo (altura promedio de la cabeza). Esto representa el

caso con mayor inducción a la que las personas eventualmente pueden

quedar expuestas por la operación de los cables de media tensión. Si se

considera una altura menor, aumenta la distancia desde los cables por lo que

se obtendrán resultados cuya magnitud será menor.

**Tabla 4.1.** Características eléctricas de los circuitos.

|Col1|Aerogeneradores|Col3|Col4|Col5|Cable unipolar|Col7|
|---|---|---|---|---|---|---|
|**Circuito**<br>|**Circuito**<br>|**Circuito**<br>|**Potencia**|**Corriente**|**Corriente**|**Corriente**|
|<br>|**ID**|**Cantidad**|**[MW]**|**[A]**|**Sección**|**Diám. Ext.**<br>**[mm]**|
|<br>|**ID**|**Cantidad**|||**[mm2]**|**[mm2]**|
|C1|1 - 2 - 3 - 4 - 5 - 6|6|19,8|353,5|185|47|
|C2|7 - 8 - 9 - 10 - 11 - 12 - 13|7|23,1|412,4|240|50|
|C3|14 - 15 - 16 - 17 - 18 - 19 -<br>20 - 21|8|26,4|471,3|300|53|
|C4|22 - 23 - 24 - 25 - 26 - 27 -<br>28 - 29|8|26,4|471,3|300|53|
|C5|30 - 31 - 32 - 35 - 36|5|16,5|294,6|185|47|
|C6|37 - 38 - 39 - 40|4|13,2|235,7|185|47|

#### 4.1 Circuitos C1, C3 y C4.

Los circuitos C1, C3 y C4 presentan distinto número de aerogeneradores

conectados por lo que se tiene distintos valores de potencia, corriente y

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

10

sección de los conductores por circuito.

Los circuitos se encuentran enterrados a 1,2 m bajo el nivel del suelo,

a una distancia entre ellos de 0,225 m. En la figura 4.1 se puede ver la

disposición geométrica de los cables.

|Col1|1200 mm|1<br>300 mm|
|---|---|---|
||100 mm|100 mm|
||225 mm<br>225 mm<br>800 mm|225 mm<br>225 mm<br>800 mm|

**Fig. 4.1.** Disposición geométrica de los circuitos C1, C3 y C4.

El perfil de campo magnético a nivel del suelo se muestra en la

figura 4.2 y el valor máximo se presenta en la Tabla 4.2 junto con el límite

recomendado.

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

11

**Fig. 4.2.** Perfil de campo magnético de circuitos C1, C3 y C4 a nivel del suelo.

**Tabla. 4.2.** Campo magnético equivalente de circuitos C1, C3 y C4 a nivel del suelo y

límites Norma Argentina junto a ICNIRP.

|Campo Magnético<br>Máximo|Magnitud rms<br>[μT]|Límite<br>Argentina<br>[μT]|Límite<br>ICNIRP<br>[μT]|¿Cumple<br>límite?|
|---|---|---|---|---|
|Cableado Subterráneo|11,07|25|100|Si|

Se observa que el perfil de campo magnético producido a nivel del suelo

por los circuitos C1, C3 y C4 cumple holgadamente los límites recomendados

para personas que eventualmente puedan quedar expuestas.

#### 4.2 Circuito C2.

Las características eléctricas y la distribución geométrica del circuito C2

se muestra en la figura 4.3.

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

12

|Col1|1200 mm|1<br>300 mm|
|---|---|---|
||100 mm|100 mm|
||300 mm<br>600 mm<br>300 mm|300 mm<br>600 mm<br>300 mm|

**Fig. 4.3.** Disposición geométrica del circuito C2.

El perfil de campo magnético a nivel del suelo se muestra en la

figura 4.4 y el valor máximo se presenta en la Tabla 4.3 junto con los

límites recomendados.

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

13

**Fig. 4.4.** Perfil de campo magnético de circuito C2 a nivel del suelo.

**Tabla. 4.3.** Campo magnético equivalente de circuito C2 a nivel del suelo y límites de Norma

Argentina junto a ICNIRP.

|Campo Magnético<br>Máximo|Magnitud rms<br>[μT]|Límite<br>Argentina<br>[μT]|Límite<br>ICNIRP<br>[μT]|¿Cumple<br>límite?|
|---|---|---|---|---|
|Cableado Subterráneo|3,751|25|100|Si|

Se observa que el perfil de campo magnético producido a nivel del suelo

por el circuito C2 cumple holgadamente los límites recomendados para

personas que eventualmente puedan estar expuestas.

#### 4.3 Circuitos C3 y C4.

Los circuitos C3 y C4 presentan igual número de aerogeneradores

conectados por lo que se tiene iguales valores de potencia, corriente y sección

de los conductores por circuito.

Los circuitos se encuentran enterrados a 1,2 m bajo el nivel del suelo,

a una distancia entre ellos de 0,225 m. En la figura 4.5 se puede ver la

disposición geométrica de los cables.

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

14

|Col1|1200 mm|1<br>300 mm|
|---|---|---|
||100 mm|100 mm|
||225 mm<br>600 mm|225 mm<br>600 mm|

**Fig. 4.5.** Disposición geométrica de los circuitos C3 y C4.

El perfil de campo magnético a nivel del suelo se muestra en la

figura 4.6 y el valor máximo se presenta en la Tabla 4.4 junto con el límite

recomendado.

**Fig. 4.6.** Perfil de campo magnético de circuitos C3 y C4 a nivel del suelo.

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

15

**Tabla. 4.4.** Campo magnético equivalente de circuitos C3 y C4 a nivel del suelo y límites de

Norma Argentina junto a ICNIRP.

|Campo Magnético<br>Máximo|Magnitud rms<br>[μT]|Límite<br>Argentina<br>[μT]|Límite<br>ICNIRP<br>[μT]|¿Cumple<br>límite?|
|---|---|---|---|---|
|Cableado Subterráneo|8,871|25|100|Si|

Se observa que el perfil de campo magnético producido a nivel del suelo

por los circuitos C3 y C4 cumple holgadamente los límites recomendados para

personas que eventualmente puedan quedar expuestas.

#### 4.4 Circuitos C5 y C6.

Los circuitos C5 y C6 presentan distinto número de aerogeneradores

conectados por lo que se tiene distintos valores de potencia y corriente.

**a)** **Campos Magnéticos.**

En las canalizaciones subterráneas los circuitos se encuentran

enterrados a 1,2 m bajo el nivel del suelo, a una distancia entre ellos de 0,225

m. En la figura 4.7 se puede ver la disposición geométrica de los cables.

|Col1|1200 mm|1<br>300 mm|
|---|---|---|
||100 mm|100 mm|
||225 mm<br>600 mm|225 mm<br>600 mm|

**Fig. 4.7.** Disposición geométrica de los circuitos subterráneos C5 y C6.

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

16

El perfil de campo magnético a nivel del suelo se muestra en la

figura 4.8 y el valor máximo se presenta en la Tabla 4.5 junto con el límite

recomendado.

**Fig. 4.8.** Perfil de campo magnético de circuitos subterráneos C5 y C6 a nivel del suelo.

En el cableado aéreo, los cables que se encuentran a menor distancia

del suelo, están a 6 metros. En la Figura 4.9 se puede ver la distribución de

los cables en la postación.

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

17

**A1**

**A2**

**0,6 m**

**0,6 m**

**6 m**

**Fig. 4.9.** Disposición geométrica de los circuitos aéreos C5 y C6.

El perfil de campo magnético a 1,8 metros del suelo se muestra

en la figura 4.10 y el valor máximo se presenta en la Tabla 4.5 junto con el

límite recomendado.

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

18

**Fig. 4.10.** Perfil de campo magnético de circuitos aéreos C5 y C6 a 1,8 metros del suelo.

**Tabla. 4.5.** Campo magnético equivalente de circuitos C5 y C6 con límites de Norma

Argentina junto a ICNIRP.

|Campo Magnético<br>Máximo|Magnitud rms<br>[μT]|Límite<br>Argentina<br>[μT]|Límite<br>ICNIRP<br>[μT]|¿Cumple<br>límite?|
|---|---|---|---|---|
|Cableado Subterráneo|4,194|25|100|Si|
|Cableado Aéreo|5,052|25|100|Si|

Se observa que el perfil de campo magnético producido a nivel del suelo

y 1,8 metros del suelo por los circuitos subterráneos y aéreos C5 y C6

cumple holgadamente los límites recomendados para personas que

eventualmente puedan quedar expuestas.

**b)** **Campos Eléctricos.**

En el cableado aéreo, los cables que se encuentran a menor distancia

del suelo, están a 6 metros. En la Figura 4.9 se puede ver la distribución de

los cables en la postación.

El perfil de campo eléctrico a 1,8 metros del suelo se muestra en

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

19

la figura 4.11 y el valor máximo se presenta en la Tabla 4.6 junto con el límite

recomendado.

**Fig. 4.11.** Perfil de campo eléctrico de circuitos aéreos C5 y C6 a 1,8 metros del suelo.

**Tabla. 4.5.** Campo eléctrico equivalente de circuitos C5 y C6 a 1,8 metros del suelo y límites

de Norma Argentina junto a ICNIRP.

|Campo Eléctrico<br>Máximo|Magnitud rms<br>[kV/m]|Límite<br>Argentina<br>[kV/m]|Límite<br>ICNIRP<br>[kV/m]|¿Cumple<br>límite?|
|---|---|---|---|---|
|En el Centro|0,7693|3,0|5,0|Si|
|En el Límite de la Faja|0,2327|0,2327|0,2327||

Se observa que el perfil de campo eléctrico producido a 1,8 metros del

suelo por los circuitos aéreos C5 y C6 cumple holgadamente los límites

recomendados para personas que eventualmente puedan quedar expuestas.

#### 4.5 Circuitos C1, C2, C3 y C4.

Los circuitos C1, C2, C3 y C4 presentan distinto número de

aerogeneradores conectados por lo que se tiene distintos valores de potencia,

corriente y sección de los conductores por circuito.

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

20

Los circuitos se encuentran enterrados a 1,2 m bajo el nivel del suelo,

a una distancia entre ellos de 0,2 m. En la figura 4.9 se puede ver la

disposición geométrica de los cables.

1300 mm

|Col1|Col2|1<br>300 mm|
|---|---|---|
||150 mm|150 mm|
||200 mm<br>1000 mm<br>200 mm<br>200 mm|200 mm<br>1000 mm<br>200 mm<br>200 mm|

**Fig. 4.9.** Disposición geométrica de los circuitos C1, C2, C3 y C4.

El perfil de campo magnético a nivel del suelo se muestra en la

figura 4.10 y el valor máximo se presenta en la Tabla 4.6 junto con el límite

recomendado.

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

21

**Fig. 4.10.** Perfil de campo magnético de circuitos C1, C2, C3 y C4 a nivel del suelo.

**Tabla. 4.6.** Campo magnético equivalente de circuitos C1, C2, C3 y C4 a nivel del suelo y

límites de Norma Argentina junto a ICNIRP.

|Campo Magnético<br>Máximo|Magnitud rms<br>[μT]|Límite<br>Argentina<br>[μT]|Límite<br>ICNIRP<br>[μT]|¿Cumple<br>límite?|
|---|---|---|---|---|
|Cableado Subterráneo|15,87|25|100|Si|

Se observa que el perfil de campo magnético producido a nivel del suelo

por los circuitos C1, C2, C3 y C4 cumple holgadamente los límites

recomendados para personas que eventualmente puedan quedar expuestas.

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

22

### 5. Referencias

[1] Resolución 77/98. Amplíense las condiciones y requerimientos fijados en el

“Manual de Gestión Ambiental del Sistema de Transporte Eléctrico de Extra Alta

Tensión”, Secretaria de Energía Eléctrica, 12 de Marzo de 1998, Buenos Aires,

Argentina.

[2] Association canadienne de normalisation, Valeurs limites et methods de mesure

du bruit électromagnétique (0,15 à 30 MHz) produit par les reseaux de courant

alternatif. CAN3-C108.3.1 - M84. Octobre 1984.

[3] Informe medidas efectuadas en S/E ANDES de 345/220 kV de AES Gener.

Departamento de Ingeniería Eléctrica, Universidad de Chile, 2008.

[4] Patricia Arnera, Pedro Issouribehere, et all. “Evaluación de campos eléctricos y

magnéticos en instalaciones de la Administración Nacional de ElectricidadANDE, Asunción, Paraguay. Trabajo presentado al Comité de estudio 36 en el

X Encuentro Regional Latinoamericano de la CIGRE, Mayo 2003, Puerto Iguazú,

Argentina.

[5] I.O. Habiballah, M.M. Dawoud, K. Al-Balawi, A.S. Farag “Magnetic Field

Measurement & Simulation of A 230 kV Substation” Proceedings of the

International Conference on Non-Ionizing Radiation at UNITEN (ICNIR 2003)

Electromagnetic Fields and Our Health 20th - 22nd October 2003.

[6] CARTER R. T. (1) ; GRILLE A. W. ; BAZILE G. M. ; PERKINS M. D. ; AUSER S.

F. ; Analysis of radio interference and substation modifications for uprating a

115-KV substation to 230 KV IEEE transactions on power delivery (IEEE trans.

power deliv.) 1987, vol. 2, no2, pp. 544-550.

[7] Modeling and calculation of electromagnetic field in the surroundings of a large

power transformer. Leonardo ˇSTRAC, Franjo KELEMEN, Damir ˇZARKO. Turk

J Elec Eng & Comp Sci, Vol.17, No.3, 2009.

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

_ADENDA No 1_
_DECLARACIÓN DE IMPACTO AMBIENTAL_
_PARQUE EÓLICO LOS OLMOS_

## APÉNDICES.

_Inversiones Bosquemar Ltda._ KAITEK Consultores en Ciencias Ambientales Ltda.-URRUTIA& Asociados

23
### Apéndice 1. Método de Cálculo de Campo Eléctrico

Para el cálculo del campo eléctrico se utiliza el método de las imágenes

[2]. Este método establece las componentes del campo eléctrico en un plano

bidimensional (x,y) como se indica en las expresiones (A.1.1) y (A.1.2).

  

###  n  q k  x  x k   q k  x  x k  
#  2 2 2 2 (A.1.1)
### k  1  2    x k  x    y k  y   2    x k  x    y k  y   

     

  

###  n  q k  x  x k 
#  x y,   2
### k  1  2    x k  x    y k  y 

  

###  n  q k  x  x k   q k  x  x k 
#,   2 2 2 2
### k  1  2    x k  x    y k  y   2    x k  x    y k  y 

  

_n_

  

# E X  x y,     q k x  x k  q k x  x

  

 _k_ _k_  _k_ _k_
# X  x y,  

  

2  _x_  _x_   2

  

 1  _x_ _k_  _x_  _y_ _k_  _y_  _x_ _k_  _x_  _y_ _k_  _y_

  

_k_  1  _x_ _k_  _x_  _y_ _k_  _y_  _x_ _k_  _x_  _y_ _k_

  

###  n  q k  y  y k   q k  y  y k  
#  2 2 2 2 (A.1.2)
### k  1  2    x k  x    y k  y   2    x k  x    y k  y   

     

  

###  n  q k  y  y k 
#  x y,   2
### k  1  2    x k  x    y k  y 

  

###  n  q k  y  y k   q k  y  y k 
#,   2 2 2 2
### k  1  2    x k  x    y k  y   2    x k  x    y k  y 

  

_n_

  

# E Y  x y,     q k y  y k  q k y  y

  

 _k_ _k_  _k_ _k_
# Y  x y,  

  

2  _x_  _x_   2

  

 1  _x_ _k_  _x_  _y_ _k_  _y_  _x_ _k_  _x_  _y_ _k_  _y_

  

_k_  1  _x_ _k_  _x_  _y_ _k_  _y_  _x_ _k_  _x_  _y_ _k_

  

Donde,

_k_ : k-ésimo conductor hasta _n_
_xk_ : Posición del k-ésimo conductor en el eje x
_yk_ : Posición del k-ésimo conductor en el eje y

 Permitividad del material (típicamente      []  _F_ / _m_  
_qk_ : Carga eléctrica asociada al k-ésimo conductor.

La carga eléctrica depende de las tensiones _V_ de cada conductor y de los

coeficientes de potencial de Maxwell _P_, determinándose según (A.1.3).

 1
_Q_  _P V_ (A.1.3)

Los componentes _V_ son las tensiones de fase y en _P_ se tiene los

coeficientes que se indican en (A.1.4) y (A.1.5).

  

_k_

  

_y_
_p_ _k k_,  2  ln  _d_

  

 ln _k_

_k k_ 

  

,

  

 1 ln  4 _y_ _k_ 

2   _d_ _k_ 

  

1 4
ln 
2 

  

(A.1.4)

  

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

24

1
2 2 2

2 2
###  1 ln   x k  x n  2   y k  y n  2  2    x k  x n    y k  y n  

###  x k  x n    y k  y n 

2
###  x k  x n    y k  y n 

1 _x_ _k_  _x_ _n_  _y_ _k_  _y_ _n_
,n  _k_  ln  2 2
2    

_x_ _k_  _x_ _n_  _y_ _k_  _y_
_p_ _k_  _k_  ln 

_k_ _n_ _k_ _n_
_k_  _k_  ln  2

 2
### 2   x k  x    y k  y

(A.1.5)

_k_ _n_ _k_ _n_

Los términos de la diagonal de _P_ se determinan considerando el

diámetro del conductor _dk_ .

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

25
### Apéndice 2. Método de Cálculo de Campo Magnético

El cálculo del campo magnético se realiza a través de un análisis

bidimensional considerando conductores paralelos sobre un terreno plano [2].

Este análisis establece las componentes del campo magnético en un plano

bidimensional (x,y) producido por una corriente circulando en el eje z

paralelo al conductor como se indica en las expresiones (A.2.1) y

(A.2.2).

###  n i k  y  y k 
#  x y,    2 2
### k  1 2    x k  x    y k  y 

# B X  x y,    n  i k  y  y

_n_

_k_  _k_


#   2 2 (A.2.1)
### k  1 2    x k  x    y k  y  

 

_k_ _k_


# X  x y,   

 2
### 2    x k  x    y k  y

2

 1 

_k_  1  _x_ _k_  _x_  _y_ _k_

###  n i k  x  x k 
#  x y,    2 2
### k  1 2    x k  x    y k  y 

# B Y  x y,    n  i k  x  x

_n_

_k_  _k_


#   2 2 (A.2.2)
### k  1 2    x k  x    y k  y  

 

_k_ _k_


# Y  x y,   

 2
### 2    x k  x    y k  y

2

 1 

_k_  1  _x_ _k_  _x_  _y_ _k_

Donde,

### k : k-ésimo conductor hasta n xk : Posición del k-ésimo conductor en el eje x yk : Posición del k-ésimo conductor en el eje y  : Permeabilidad del material (típicamente  4   10 [] [7] [ H / m ] ) ik : Corriente eléctrica asociada al k-ésimo conductor.

En este análisis no se considera la corrección de Carson por tratarse de

evaluaciones dentro de una zona próxima a la fuente que emite el campo

magnético [2].

O`Higgins 940, Of. 901, Edificio del Pacifico
Tel: 56- 41- 2730097
**Concepción - Chile** **[www.eolico.cl](http://www.eolico.cl/)**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4.1.: ** Características eléctricas de los circuitos.**

| Col1 | Aerogeneradores | Col3 | Col4 | Col5 | Cable unipolar | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| **Circuito**<br> | **Circuito**<br> | **Circuito**<br> | **Potencia** | **Corriente** | **Corriente** | **Corriente** |
| <br> | **ID** | **Cantidad** | **[MW]** | **[A]** | **Sección** | **Diám. Ext.**<br>**[mm]** |
| <br> | **ID** | **Cantidad** |  |  | **[mm2]** | **[mm2]** |
| C1 | 1 - 2 - 3 - 4 - 5 - 6 | 6 | 19,8 | 353,5 | 185 | 47 |
| C2 | 7 - 8 - 9 - 10 - 11 - 12 - 13 | 7 | 23,1 | 412,4 | 240 | 50 |
| C3 | 14 - 15 - 16 - 17 - 18 - 19 -<br>20 - 21 | 8 | 26,4 | 471,3 | 300 | 53 |
| C4 | 22 - 23 - 24 - 25 - 26 - 27 -<br>28 - 29 | 8 | 26,4 | 471,3 | 300 | 53 |
| C5 | 30 - 31 - 32 - 35 - 36 | 5 | 16,5 | 294,6 | 185 | 47 |
| C6 | 37 - 38 - 39 - 40 | 4 | 13,2 | 235,7 | 185 | 47 |
