---
title: Sin título
author: Sergio Arriaza
date: D:20200917185013-03'00'
language: es
type: report
pages: 52
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Declaración de Impacto Ambiental Proyecto “Planta Fotovoltaica Sierra Gorda Solar” - Región de Antofagasta
-->

### Anexo 2.3 Caracterización del Medio - Campos Electromagnéticos

# Declaración de Impacto Ambiental Proyecto “Planta Fotovoltaica Sierra Gorda Solar” - Región de Antofagasta

Preparado para
Enel Green Power Chile S.A.
Septiembre, 2020

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

## Tabla de contenidos

1 Introducción ............................................................................................................................................ 4

2 Objetivos ................................................................................................................................................. 4

3 Metodología ............................................................................................................................................ 4

3.1 Aspectos generales .................................................................................................................................. 4

3.2 Descripción del método de cálculo de campo eléctrico ........................................................................ 5

3.3 Descripción del método de cálculo del campo magnético .................................................................... 5

3.4 Cálculo de radio interferencia (RI) ........................................................................................................... 6

3.5 Cálculo de TVI ........................................................................................................................................... 7

4 Antecedentes .......................................................................................................................................... 9

4.1 Información geográfica ............................................................................................................................ 9

4.2 LTE 1x220 kV El Arriero - Centinela ..................................................................................................... 10

4.2.1 Características de la línea de transmisión .................................................................................... 10

4.3 Acometida SE/E El Arriero ...................................................................................................................... 14

4.3.1 Características de la instalación ................................................................................................... 14

4.4 LTE 1x 220 kV Encuentro-El Tesoro (Existente) ................................................................................... 15

4.4.1 Características de la línea de transmisión .................................................................................... 15

4.5 LTE 1x 220 kV El Tesoro-Esperanza (Existente) ................................................................................... 18

4.5.1 Características de la línea de transmisión .................................................................................... 18

4.6 LTE 1x220 kV Parque Eólico Sierra Gorda Este (Existente) ................................................................ 21

4.6.1 Características de la línea de transmisión .................................................................................... 21

5 Resultados ............................................................................................................................................ 23

5.1 Instalaciones del proyecto ..................................................................................................................... 23

5.1.1 LTE 1x220 kV El Arriero - Centinela ............................................................................................. 23

5.1.2 Acometida en SE/E El Arriero ........................................................................................................ 31

5.2 Interacción con instalaciones existentes .............................................................................................. 33

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 2 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

5.2.1 Cruce LTE 1x220 kV Encuentro - El Tesoro con LTE 1x220 kV Arriero - Centinela ................. 33

5.2.2 Paralelismo con LTE 1x220 kV PE S. Gorda Este ......................................................................... 37

5.2.3 Cruce LTE 1x220 kV El Tesoro - Esperanza con LTE 1x220 kV Arriero - Centinela .................. 41

5.2.4 Paralelismo con LTE 1x220 kV El Tesoro Esperanza ................................................................... 45

6 Comparación de valores máximos en borde de franja de seguridad ................................................... 47

6.1 Normativa aplicable a campos electromagnéticos .............................................................................. 47

6.2 Normativa aplicable a radiointerferencia y TVI ..................................................................................... 49

6.2.1 Radiointerferencia (RI) ................................................................................................................... 49

6.2.2 Interferencias de TV (TVI) ............................................................................................................... 49

6.3 Verificación de la normativa de acuerdo con los cálculos realizados ................................................. 50

6.3.1 Verificación campos electromagnéticos en línea de transmisión ............................................... 50

6.3.2 Verificación de radio interferencia para las instalaciones del proyecto ..................................... 51

7 Conclusiones ......................................................................................................................................... 52

8 Referencias ........................................................................................................................................... 52

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 3 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

1 Introducción

El Proyecto “Planta Fotovoltaica Sierra Gorda Solar” es un proyecto nuevo y consiste en la construcción y

operación de un parque fotovoltaico, una línea de transmisión eléctrica (LTE) y una subestación elevadora

(SE/E).

Estás últimas obras cumplen la función de conectar y transmitir la energía fotovoltaica generada por el

parque al Sistema Eléctrico Nacional.

2 Objetivos

 - Determinar el campo eléctrico y magnético producido por las líneas de alta tensión existentes que

están a menos de 100 [m] del eje de la línea del Proyecto.

 - Determinar el campo eléctrico y magnético producido por la interacción de líneas de alta tensión

existentes con las instalaciones del Proyecto.

 - Determinar el campo eléctrico, magnético e interferencia producido por operación de las

instalaciones del Proyecto.

3 Metodología

3.1 Aspectos generales

Se realizarán simulaciones, utilizando la implementación computacional del método de las imágenes para

determinar los campos eléctricos y magnéticos, a un metro del suelo, generados por las siguientes

instalaciones de alta tensión:

a) Instalaciones de terceros

 - LTE 1x 220 kV Encuentro-El Tesoro.

 - LTE 1x220 kV Parque Eólico Sierra Gorda Este.

 - LTE 1x220 kV El Tesoro - Esperanza.

b) Interacción de instalaciones

 - Cruce LTE 1x 220 kV Encuentro-El Tesoro con LTE 1x220 kV El Arriero - Centinela.

 - Paralelismo LTE 1x220 kV Parque Eólico Sierra Gorda Este, con LTE 1x220 kV El Arriero - Centinela.

 - Cruce y paralelismo con LTE 1x220 kV El Tesoro - Esperanza.

c) Instalaciones propias

 - LTE 1x220 kV El Arriero - Centinela Estructura tipo 22A1.1C.

 - LTE 1x220 kV El Arriero - Centinela Estructura tipo 22A30.1C.

 - LTE 1x220 kV El Arriero - Centinela Estructura tipo 22A90.1C.

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 4 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

 - LTE 1x220 kV El Arriero - Centinela Estructura tipo Portal 10m.

 - Acometida a SE/E El Arriero.

Los valores de campo eléctrico y magnéticos obtenidos mediante simulación computacional serán

comparados con los límites de exposición humana admisibles para un entorno ocupacional y de público

general [1] [2] [3] y [4].

También se calcularán los valores de radio-interferencia producto de la ocurrencia del efecto corona en las

instalaciones del proyecto.

Para del cálculo del campo eléctrico y magnético, se utilizará el método de las imágenes [5] [6], el cual fue

implementado en el lenguaje de programación GNU Octave 4.4.0.

3.2 Descripción del método de cálculo de campo eléctrico

El método de las imágenes permite resolver problemas electromagnéticos en campos considerados

estáticos o cuasi-estacionarios. Para fines prácticos, el campo eléctrico de 50 [Hz] de comporta como un

campo cuasi-estacionario en las inmediaciones de las fuentes que lo producen.

Los datos de entrada para la función que determina el campo eléctrico son los siguientes:

Tabla 1 - Descripción de las variables de entrada al software

Variable Unidad Descripción
POS [m] Matriz de Nx2, donde N es el número de conductores y cada fila representa la ubicación espacial x,y de cada
fase.
V [V] Matriz de Nx1 donde N es el número de conductores, matriz de tensiones eficaces instantáneas en cada
conductor.

r [m] Radio del conductor de fase utilizado. En este caso ACAR 500 MCM, radio = 10,33 [mm]
N Número de conductores por fase (N=1)
e_0 [C [2] /Nm [2] ] Constante dieléctrica
X [m] Vector que contiene las abscisas de los puntos donde se calculará el campo
Y [m] Vector que contiene las ordenadas de los puntos donde se calculará el campo

Los datos de salida son tres matrices de dimensiones XY, que contienen los resultados de los campos

vectoriales en X e Y, y la resultante de ambas componentes.

Los campos eléctricos corresponden a un campo vectorial complejo, y puede estar polarizado circular o

elípticamente.

En este informe se determina el valor eficaz máximo de campo a un metro sobre el nivel del suelo.

3.3 Descripción del método de cálculo del campo magnético

Para del cálculo del campo magnético, se utilizará el método de las imágenes [5] [6], el cual fue

implementado en el lenguaje de programación GNU Octave 4.4.0.

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 5 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

El método de las imágenes permite resolver problemas electromagnéticos en campos considerados

estáticos o cuasi-estacionarios. Para fines prácticos, el campo eléctrico de 50 [Hz] se comporta como un

campo cuasi-estacionario en las inmediaciones de las fuentes que lo producen.

Los datos de entrada para la función que determina el campo magnético son los siguientes:

Tabla 2 - Descripción de las variables de entrada al software

Variable Unidad Descripción

|POS|[m]|Matriz de Nx2, donde N es el número de fases y cada fila representa la ubicación espacial x,y de cada<br>fase.|
|---|---|---|
|I|[A]|Matriz de Nx1 donde N es el número de fases, matriz de corrientes eficaces en cada fase. (267 A)|
|rho|[m]|Resistividad equivalente del terreno. Se considerará un valor de 100 [m]|
|u_0|[N/A2]|Permeabilidad magnética del aire|
|X|[m]|Vector que contiene las abscisas de los puntos donde se calculará el campo|
|Y|[m]|Vector que contiene las ordenadas de los puntos donde se calculará el campo|

Los datos de salida son tres matrices de dimensiones XY, que contienen los resultados de los campos

vectoriales en X e Y, y la resultante de ambas componentes.

Como el campo magnético es un campo vectorial complejo, el cual puede estar polarizado circular ó

elípticamente.

En este informe se determina el valor eficaz máximo de campo a un metro sobre el nivel del suelo.

3.4 Cálculo de radio interferencia (RI)

Para el cálculo de la RI se aplicará el método comparativo 400-kV - FG (Germany).

La idea detrás de este método de cálculo es el uso de un valor de referencia, en día despejado, el cual ha

sido obtenido a través de métodos estadísticos sobre datos reales de líneas de transmisión operativas y

pruebas de laboratorio.

La fórmula completa, de acuerdo con el estándar ANSI es la siguiente:

RI= 53,7 ± 5 + K(g m −16,95) + 40 log [d]

D [+ E] [f] [+ E] [FW]

[d]

3.93 [+ E] [n] [+ 20K] [d] [log 20] D

Donde:

 - RI = Interferencia RI producida por fase

 - K = 3 para líneas de 750 kV; K = 3,5 para líneas con gradientes en el orden 15-19 kV/cm

- E n = -4dB para conductor simple E n = 10 log

- K D = 1.6

n [para líneas con n sub conductores ]
4

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 6 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

 - E FW = 0 para buen tiempo, E FW = 17 para lluvia

 - g m = gradiente máximo (kV/cm)

 - d = diámetro del conductor en centímetros

 - D = distancia radial del conductor a la antena

 - f = frecuencia, MHz

Se deberá calcular para cada fase la contribución RI. Si uno de los valores obtenido es 3 dB mayor a los

otros dos valores, entonces el valor RI de la línea será el mayor.

Si la diferencia entre los dos mayores valores obtenidos es menor a 3 dB, el valor RI se calculará de acuerdo

con la ecuación:

RI linea = [(RI] [1] [ + RI] [2] [)] + 1,5

2

En el caso de fuentes en fase, se adoptará el siguiente procedimiento para sumar cada una de las

contribuciones:

 - Se determinará el valor de RI para cada fuente.

 - Se transforma la magnitud del campo perturbador de dB a V/m, luego se suman las contribuciones

de las diferentes fuentes en fase y finalmente, el resultado se transforma nuevamente a dB según

las fórmulas indicadas más abajo:

RLi

E i 20

[ [μV] m ~~[]]~~ [ = 10]

E i

[ [μV] m

2
[ [μV] m

m ~~[]]~~ [ = ∑E] [i]

m ~~[]]~~

i

RI[dB] = ∑20 log E[ [μV] m ~~[]]~~

i

3.5 Cálculo de TVI

La interferencia de televisión (TVI), se evalúa a partir de la RI producida por la línea de transmisión a una

frecuencia de 1 MHz y a una distancia de 15 metros de la fase externa, utilizando las siguientes ecuaciones:

TVI= RI−Δf+ Δbw+ ΔD

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 7 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Δf= 52 + 20 log [f]

75

ΔD = 20 log ~~[√]~~ [h] [2] [ + D] [x2]

~~√~~ h [2] + x [2]

Donde:

 - Δf valor en que la RI decrece desde el espectro de frecuencia de 1 MHz

 - Δbw es el factor de corrección del ancho de banda de 5 kHz de RI al ancho de banda de 150 kHz

del TVI, y corresponde a 17,7

 - ΔD es el ajuste por distancia

 - h, D x altura de las fases y distancia horizontal desde la fase externa, respectivamente

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 8 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

4 Antecedentes

4.1 Información geográfica

En la Figura 1 se muestran las instalaciones existentes y proyectadas en la zona donde se emplazarán las

instalaciones.

El proyecto consiste en la SE/E El Arriero y la LTE 1x220 kV El Arriero Centinela.

Las interacciones con instalaciones de terceros, son las siguientes:

 - La LTE 1x220 kV El Arriero - Centinela, establece un paralelismo de aproximadamente 17 km con

la LTE 1x220 kV P.E. Sierra Gorda Este. En este caso, los ejes de las líneas de transmisión se

encuentran separados 50 [m] entre sí.

 - Existe un cruce con la LTE 1x220 kV Encuentro - El Tesoro, la cual será cruzada por arriba.

 - Existe un paralelismo y cruce con la línea existente El Tesoro - Esperanza.

`o` La distancia entre los ejes de las líneas de una vez establecido el paralelismo es del orden

de 60 [m], por lo tanto, su interacción de campos electromagnéticos será evaluada

considerando esta distancia entre ejes.

`o` Para el caso del cruce, se considerará que la LTE del proyecto, cruzará por arriba con una

estructura similar a la del cruce con la LTE 1x220 kV Encuentro - El Tesoro.

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 9 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Figura 1 - Entorno de instalaciones existentes y proyectadas.

Por lo tanto, se modelarán las LTE 1x220 kV El Arriero-Centinela, LTE 1x220 kV Encuentro - El Tesoro y LTE

1x220 kV El Tesoro - Esperanza, y se obtendrán sus perfiles longitudinales de campo eléctrico y magnético,

para determinar eventuales efectos sinérgicos con las instalaciones proyectadas.

4.2 LTE 1x220 kV El Arriero - Centinela

4.2.1 Características de la línea de transmisión

La línea de transmisión permitirá la inyección de energía renovable de la Planta Fotovoltaica Sierra Gorda

Solar al Sistema Eléctrico Nacional, mediante la conexión de las subestaciones El Arriero y Centinela.

La línea de transmisión está conformada por estructuras de suspensión, anclaje, remate y portales.

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 10 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

**Suspensión** **Anclaje**

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 11 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Figura 2 -Siluetas de estructuras de la línea de transmisión LTE 1x220 kV El Arriero - Centinela

La ubicación respecto del suelo de los conductores (coordenada Y), se realizará considerando la altura de

tienen actualmente los conductores en el cruce proyectado con la línea de transmisión eléctrica en 220 kV

del Proyecto, y se presentan en la tablas Tabla 3, Tabla 4, Tabla 5 y Tabla 6.

<!-- INICIO TABLA 6 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Fases|X [m]|Y [m]| |A|4,71|7,32| |B|-4,71|7,32| |C|4,71|13,32| -->

**Tabla 6: - Ubicación espacial de las fases para estructura Portal 10 m**

| Tipo de estructura | Ubicación espacial de los conductores | Col3 |
| --- | --- | --- |
| Fases | X [m] | Y [m] |
| A | -6,0 | 7,32 |
| B | 0 | 7,32 |
| C | 6 | 7,32 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Los parámetros eléctricos han sido aportados por el mandante y se muestran en la Tabla 7 Tabla 7 - Parámetros eléctricos LTE 1x220 kV El Arriero - Centinela -->
<!-- FIN TABLA 6 -->


Tabla 3 - Ubicación espacial de las fases para estructura de suspensión 22A30.1

|Tipo de estructura|Ubicación espacial de los conductores|Col3|
|---|---|---|
|Fases|X [m]|Y [m]|
|A|4,6|7,32|
|B|-4,6|7,32|
|C|4,6|13,32|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 12 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Tabla 4 - Ubicación espacial de las fases para estructura de suspensión 22A1.1

|Tipo de estructura|Ubicación espacial de los conductores|Col3|
|---|---|---|
|Fases|X [m]|Y [m]|
|A|4,71|7,32|
|B|-4,71|7,32|
|C|4,71|13,32|

Tabla 5 - Ubicación espacial de las fases para estructura de suspensión 22A90.1

|Tipo de estructura|Ubicación espacial de los conductores|Col3|
|---|---|---|
|Fases|X [m]|Y [m]|
|A|4,71|7,32|
|B|-4,71|7,32|
|C|4,71|13,32|

Tabla 6 - Ubicación espacial de las fases para estructura Portal 10 m

|Tipo de estructura|Ubicación espacial de los conductores|Col3|
|---|---|---|
|Fases|X [m]|Y [m]|
|A|-6,0|7,32|
|B|0|7,32|
|C|6|7,32|

Los parámetros eléctricos han sido aportados por el mandante y se muestran en la Tabla 7

Tabla 7 - Parámetros eléctricos LTE 1x220 kV El Arriero - Centinela

|Parámetro|Valor|Unidad|
|---|---|---|
|Potencia Nominal|400|MVA|
|Tensión Nominal|220|kV|
|Corriente Nominal|1050|A|
|Conductores por fase|2|-|
|Nombre comercial del conductor|ACAR 800 MCM|-|
|Diámetro del conductor|26,1|mm|
|Separación entre subconductores|400|mm|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 13 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

4.3 Acometida SE/E El Arriero

4.3.1 Características de la instalación

Es una subestación elevadora, con equipos de transformación y un paño para la línea “1x220 kV El Arriero

Centinela”. La sección de la instalación donde se acomete la línea de alta tensión se muestra en la Figura

3. Se considerará un perfil contiguo a la zona de las barras que reciben la acometida en alta tensión en

220 kV, como peor condición.

Eje de Simetría

Figura 3 - Disposición general de equipos en planta SE/E El Arriero

Acometida

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 14 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

De acuerdo con las condiciones de diseño de la SE/E y el reglamento de corrientes fuertes, en este estudio

se considera:

 - Distancia mínima al suelo de 7,32 [m] en el cerco de la SE/E para las acometidas en 220 kV.

 - Separación entre fases de 5 [m] en los paños de 220 kV.

4.4 LTE 1x 220 kV Encuentro-El Tesoro (Existente)

4.4.1 Características de la línea de transmisión

Esta línea de transmisión permite alimentar los consumos de la mina “El Tesoro” y corresponde a la que se

muestra en la fotografía de la Figura 4.

Se modelará la ubicación horizontal de los conductores (coordenada X), a partir de los valores estándar

para una estructura de anclaje similar a la mostrada en la Figura 5.

Figura 4 - LTE 1x220kV Encuentro el Tesoro, vista desde Ruta 25 (Google Street View).

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 15 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Figura 5 -Modelo utilizado.

La ubicación respecto del suelo de los conductores (coordenada Y), se realizará considerando la altura que

tienen actualmente los conductores en el cruce proyectado con la línea de transmisión eléctrica en 220 kV

del Proyecto, y se presentan en Tabla 8 y Tabla 9.

<!-- INICIO TABLA 9 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Fases|X [m]|Y [m]| |A|-3,64|29,03| |B|3,64|29,03| |C|-3,64|24,03| -->

**Tabla 9: - Ubicación espacial de las fases para LTE 1x220kV El Arriero - Centinela en punto de cruce**

| Tipo de estructura | Ubicación espacial de los conductores existen, en el cruce con LTE<br>Proyectada | Col3 |
| --- | --- | --- |
| Fases | X [m] | Y [m] |
| A | -4,6 | 33,53 |
| B | 4,6 | 33,53 |
| C | -4,6 | 37,53 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 16 de 52 GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0 -->
<!-- FIN TABLA 9 -->


Tabla 8 - Ubicación espacial de las fases para LTE 1x220kV Encuentro - El Tesoro en punto de cruce

|Tipo de estructura|Ubicación espacial de los conductores existen, en el cruce con LTE<br>Proyectada|Col3|
|---|---|---|
|Fases|X [m]|Y [m]|
|A|-3,64|29,03|
|B|3,64|29,03|
|C|-3,64|24,03|

Tabla 9 - Ubicación espacial de las fases para LTE 1x220kV El Arriero - Centinela en punto de cruce

|Tipo de estructura|Ubicación espacial de los conductores existen, en el cruce con LTE<br>Proyectada|Col3|
|---|---|---|
|Fases|X [m]|Y [m]|
|A|-4,6|33,53|
|B|4,6|33,53|
|C|-4,6|37,53|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 16 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Los parámetros eléctricos se han obtenido desde el sitio web del Coordinador Eléctrico Nacional y se

muestran en la Tabla 10.

<!-- INICIO TABLA 10 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Los parámetros eléctricos se han obtenido desde el sitio web del Coordinador Eléctrico Nacional y se muestran en la Tabla 10. -->

**Tabla 10: - Parámetros eléctricos LTE 1x220kV Encuentro - El Tesoro**

| Parámetro | Valor | Unidad |
| --- | --- | --- |
| Potencia Nominal | 125 | MVA |
| Tensión Nominal | 220 | kV |
| Corriente Nominal | 328 | A |
| Conductores por fase | 1 | - |
| Nombre comercial del conductor | AAAC Flint | - |
| Diámetro del conductor | 25,2 | mm |

<!-- Estadísticas: 6 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 17 de 52 GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0 -->
<!-- FIN TABLA 10 -->


Tabla 10 - Parámetros eléctricos LTE 1x220kV Encuentro - El Tesoro

|Parámetro|Valor|Unidad|
|---|---|---|
|Potencia Nominal|125|MVA|
|Tensión Nominal|220|kV|
|Corriente Nominal|328|A|
|Conductores por fase|1|-|
|Nombre comercial del conductor|AAAC Flint|-|
|Diámetro del conductor|25,2|mm|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 17 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

4.5 LTE 1x 220 kV El Tesoro-Esperanza (Existente)

4.5.1 Características de la línea de transmisión

Esta línea de transmisión permite alimentar los consumos de la mina Esperanza y establece dos cruces y

paralelismo con la línea del Proyecto (1x220 kV El Arriero - Centinela).

Los parámetros eléctricos de la línea de transmisión y la ubicación horizontal de los conductores

(coordenada X), corresponden a los disponibles en la sección INFOTÉCNICA del sitio web del Coordinador

[Eléctrico Nacional (https://infotecnica.coordinador.cl/instalaciones/secciones-tramos) y se presentan en](https://infotecnica.coordinador.cl/instalaciones/secciones-tramos)

la Tabla 11.

<!-- INICIO TABLA 11 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- [Eléctrico Nacional (https://infotecnica.coordinador.cl/instalaciones/secciones-tramos) y se presentan en](https://infotecnica.coordinador.cl/instalaciones/secciones-tramos) la Tabla 11. -->

**Tabla 11: - Parámetros eléctricos LTE 1x220kV El Tesoro - Esperanza**

| Parámetro | Valor | Unidad |
| --- | --- | --- |
| Potencia Nominal | 167 | MVA |
| Tensión Nominal | 220 | kV |
| Corriente Nominal | 438 | A |
| Conductores por fase | 1 | - |
| Nombre comercial del conductor | AAAC Flint | - |
| Diámetro del conductor | 25,2 | mm |

<!-- Estadísticas: 6 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- La ubicación respecto del suelo de los conductores (coordenada Y), se realizará de forma tal que la fase más cercana al suelo cumpla con la altura mínima en metros (peor condición), indicada en el Art.107 del -->
<!-- FIN TABLA 11 -->


Tabla 11 - Parámetros eléctricos LTE 1x220kV El Tesoro - Esperanza

|Parámetro|Valor|Unidad|
|---|---|---|
|Potencia Nominal|167|MVA|
|Tensión Nominal|220|kV|
|Corriente Nominal|438|A|
|Conductores por fase|1|-|
|Nombre comercial del conductor|AAAC Flint|-|
|Diámetro del conductor|25,2|mm|

La ubicación respecto del suelo de los conductores (coordenada Y), se realizará de forma tal que la fase

más cercana al suelo cumpla con la altura mínima en metros (peor condición), indicada en el Art.107 del

Reglamento de Corrientes Fuertes [7], para líneas clase C en zonas poco transitadas, la cual se determina

con la siguiente fórmula:

H minima = 6 + 0,006 ∗kV

Donde kV corresponde a la tensión nominal de la línea, en este caso 220 [kV].

Por lo tanto, la altura mínima para este caso será:

H minima = 7,32[m].

A partir de este criterio y la silueta de la estructura de la Figura 6, se determinan las coordenadas para la

LTE 1x220 kV El Tesoro-Esperanza, las cuales se utilizan en el punto de cruce y corresponden a la Tabla

12. Las coordenadas de la estructura de cruce de la LTE 1x220kV El Arriero - Centinela se encuentran en

la Tabla 13.

<!-- INICIO TABLA 13 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Fases|X [m]|Y [m]| |A|6,00|7,32| |B|-5,00|10,82| |C|5,00|14,32| -->

**Tabla 13: - Ubicación espacial de las fases para LTE 1x220kV El Arriero - Centinela en punto de cruce**

| Tipo de estructura | Ubicación espacial de los conductores existen, en el cruce con LTE<br>Proyectada | Col3 |
| --- | --- | --- |
| Fases | X [m] | Y [m] |
| A | -4,6 | 33,53 |
| B | 4,6 | 33,53 |
| C | -4,6 | 37,53 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 14: Ubicación espacial de las fases de la LTE 1x220 kV El Tesoro-Esperanza en paralelismo (eje x = 30 m) |Tipo de estructura|Estructura de Anclaje|Col3| |---|---|---| -->
<!-- FIN TABLA 13 -->


En el caso del paralelismo con la LTE en estudio, considerando una distancia entre ejes de 60 m, las

coordenadas de las líneas de transmisión están en la Tabla 14 y Tabla 15.

<!-- INICIO TABLA 15 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Fases|X [m]|Y [m]| |A|36,00|7,32| |B|25,00|10,82| |C|35,00|14,32| -->

**Tabla 15: - Ubicación espacial de las fases para LTE 1x220kV El Arriero - Centinela en paralelismo (eje x = - 30 m)**

| Tipo de estructura | Ubicación espacial de los conductores existen, en el cruce con LTE<br>Proyectada | Col3 |
| --- | --- | --- |
| Fases | X [m] | Y [m] |
| A | -34,6 | 33,53 |
| B | -25,4 | 33,53 |
| C | -34,6 | 37,53 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 19 de 52 GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0 -->
<!-- FIN TABLA 15 -->


P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 18 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Tabla 12: Ubicación espacial de las fases de la LTE 1x220 kV El Tesoro-Esperanza

<!-- INICIO TABLA 12 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 18 de 52 GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0 -->

**Tabla 12: Ubicación espacial de las fases de la LTE 1x220 kV El Tesoro-Esperanza**

| Tipo de estructura | Estructura de Anclaje | Col3 |
| --- | --- | --- |
| Fases | X [m] | Y [m] |
| A | 6,00 | 7,32 |
| B | -5,00 | 10,82 |
| C | 5,00 | 14,32 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 13 - Ubicación espacial de las fases para LTE 1x220kV El Arriero - Centinela en punto de cruce |Tipo de estructura|Ubicación espacial de los conductores existen, en el cruce con LTE<br>Proyectada|Col3| |---|---|---| -->
<!-- FIN TABLA 12 -->


|Tipo de estructura|Estructura de Anclaje|Col3|
|---|---|---|
|Fases|X [m]|Y [m]|
|A|6,00|7,32|
|B|-5,00|10,82|
|C|5,00|14,32|

Tabla 13 - Ubicación espacial de las fases para LTE 1x220kV El Arriero - Centinela en punto de cruce

|Tipo de estructura|Ubicación espacial de los conductores existen, en el cruce con LTE<br>Proyectada|Col3|
|---|---|---|
|Fases|X [m]|Y [m]|
|A|-4,6|33,53|
|B|4,6|33,53|
|C|-4,6|37,53|

Tabla 14: Ubicación espacial de las fases de la LTE 1x220 kV El Tesoro-Esperanza en paralelismo (eje x = 30 m)

<!-- INICIO TABLA 14 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- |Fases|X [m]|Y [m]| |A|-4,6|33,53| |B|4,6|33,53| |C|-4,6|37,53| -->

**Tabla 14: Ubicación espacial de las fases de la LTE 1x220 kV El Tesoro-Esperanza en paralelismo (eje x = 30 m)**

| Tipo de estructura | Estructura de Anclaje | Col3 |
| --- | --- | --- |
| Fases | X [m] | Y [m] |
| A | 36,00 | 7,32 |
| B | 25,00 | 10,82 |
| C | 35,00 | 14,32 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Tabla 15 - Ubicación espacial de las fases para LTE 1x220kV El Arriero - Centinela en paralelismo (eje x = - 30 m) |Tipo de estructura|Ubicación espacial de los conductores existen, en el cruce con LTE<br>Proyectada|Col3| |---|---|---| -->
<!-- FIN TABLA 14 -->


|Tipo de estructura|Estructura de Anclaje|Col3|
|---|---|---|
|Fases|X [m]|Y [m]|
|A|36,00|7,32|
|B|25,00|10,82|
|C|35,00|14,32|

Tabla 15 - Ubicación espacial de las fases para LTE 1x220kV El Arriero - Centinela en paralelismo (eje x = - 30 m)

|Tipo de estructura|Ubicación espacial de los conductores existen, en el cruce con LTE<br>Proyectada|Col3|
|---|---|---|
|Fases|X [m]|Y [m]|
|A|-34,6|33,53|
|B|-25,4|33,53|
|C|-34,6|37,53|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 19 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Figura 6 -Estructura típica para LT 1x220 kV El Tesoro - Esperanza

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 20 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

4.6 LTE 1x220 kV Parque Eólico Sierra Gorda Este (Existente)

4.6.1 Características de la línea de transmisión

La línea de transmisión corresponde a la silueta que se muestra en la Figura 7, en particular, corresponde

a una estructura de suspensión en circuito simple.

Figura 7 - LTE 1x220kV Parque Eólico Sierra Gorda Este

La ubicación respecto del suelo de los conductores (coordenada Y), se realizará de forma tal que la fase

más cercana al suelo cumpla con la altura mínima en metros, indicada en el Art.107 del Reglamento de

Corrientes Fuertes [7], para líneas clase C en zonas poco transitadas, la cual se determina con la siguiente

fórmula:

H minima = 6 + 0,006 ∗kV

Donde kV corresponde a la tensión nominal de la línea, en este caso 220 [kV].

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 21 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Por lo tanto, la altura mínima para este caso será:

H minima = 7,32[m]

A partir de este criterio y la silueta de la estructura de la Figura 7, se determinan las coordenadas para la

LTE 1x220 kV Parque Eólico Sierra Gorda Este, las cuales corresponden a la Tabla 16.

<!-- INICIO TABLA 16 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- A partir de este criterio y la silueta de la estructura de la Figura 7, se determinan las coordenadas para la LTE 1x220 kV Parque Eólico Sierra Gorda Este, las cuales corresponden a la Tabla 16. -->

**Tabla 16: Ubicación espacial de las fases de la estructura**

| Tipo de estructura | Estructura de Anclaje | Col3 |
| --- | --- | --- |
| Fases | X [m] | Y [m] |
| A | 4,60 | 7,32 |
| B | -4,60 | 7,32 |
| C | 4,60 | 13,32 |

<!-- Estadísticas: 4 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- La condición antes expuesta corresponde la condición más conservadora. Los parámetros eléctricos se han obtenido desde el sitio web del Coordinador Eléctrico Nacional y se -->
<!-- FIN TABLA 16 -->


Tabla 16: Ubicación espacial de las fases de la estructura

|Tipo de estructura|Estructura de Anclaje|Col3|
|---|---|---|
|Fases|X [m]|Y [m]|
|A|4,60|7,32|
|B|-4,60|7,32|
|C|4,60|13,32|

La condición antes expuesta corresponde la condición más conservadora.

Los parámetros eléctricos se han obtenido desde el sitio web del Coordinador Eléctrico Nacional y se

muestran en la Tabla 17.

<!-- INICIO TABLA 17 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Los parámetros eléctricos se han obtenido desde el sitio web del Coordinador Eléctrico Nacional y se muestran en la Tabla 17. -->

**Tabla 17: - Parámetros eléctricos LTE 1x220kV Parque Eólico Sierra Gorda Este**

| Parámetro | Valor | Unidad |
| --- | --- | --- |
| Potencia Nominal | 178 | MVA |
| Tensión Nominal | 220 | kV |
| Corriente Nominal | 468 | A |
| Conductores por fase | 1 | - |
| Nombre comercial del conductor | AAAC Flint | - |
| Diámetro del conductor | 25,2 | mm |

<!-- Estadísticas: 6 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 22 de 52 GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0 -->
<!-- FIN TABLA 17 -->


Tabla 17 - Parámetros eléctricos LTE 1x220kV Parque Eólico Sierra Gorda Este

|Parámetro|Valor|Unidad|
|---|---|---|
|Potencia Nominal|178|MVA|
|Tensión Nominal|220|kV|
|Corriente Nominal|468|A|
|Conductores por fase|1|-|
|Nombre comercial del conductor|AAAC Flint|-|
|Diámetro del conductor|25,2|mm|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 22 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

5 Resultados

5.1 Instalaciones del proyecto

5.1.1 LTE 1x220 kV El Arriero - Centinela

Estructura 22A1.1C

Figura 8- Campo eléctrico LTE 1x220 kV El Arriero - Centinela 22A1.1C

Tabla 18 Valores de campo eléctrico LTE 1x220 kV El Arriero - Centinela 22A1.1C

Campo Eléctrico
Punto de medida x [m] y[m]

[kV/m]

|Limite franja seguridad derecha|20,00|1|0,80|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|0,73|
|Valor máximo en perfil|-5,50|1|5,14|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 23 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Figura 9 - Campo magnético LTE 1x220 kV El Arriero - Centinela 22A1.1C

Tabla 19 Valores de campo magnético LTE 1x220 kV El Arriero - Centinela 22A1.1C

Campo Magnético
Punto de medida x [m] y[m]

[uT]

|Limite franja seguridad derecha|20,00|1|5,33|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|4,98|
|Valor máximo en perfil|-1,00|1|28,81|

Tabla 20 - Cálculo de radiointerferencias para LTE 1x220 kV El Arriero - Centinela 22A1.1C

RI ANSI 1 MHz
Punto de medida x [m] y[m]

[db 1 uV/m]

TVI 71 MHz

[db 1 uV/m]

TVI 195 MHz

[db 1 uV/m]

|15 metros fase lateral derecha|19,60|2|29,03|-4,79|-13,57|
|---|---|---|---|---|---|
|15 metros fase lateral izquierda|-19,60|2|25,93|-7,89|-16,67|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 24 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Estructura 22A30.1C

Figura 10 - Campo eléctrico LTE 1x220 kV El Arriero - Centinela 22A30.1C

Tabla 21 Valores de campo eléctrico LTE 1x220 kV El Arriero - Centinela 22A30.1C

Campo Eléctrico
Punto de medida x [m] y[m]

[kV/m]

|Limite franja seguridad derecha|20,00|1|0,81|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|0,74|
|Valor máximo en perfil|-5,50|1|5,18|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 25 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Figura 11 - Campo magnético LTE 1x220 kV El Arriero - Centinela 22A30.1C

Tabla 22 Valores de campo magnético LTE 1x220 kV El Arriero - Centinela 22A30.1C

Campo Magnético
Punto de medida x [m] y[m]

[uT]

|Limite franja seguridad derecha|20,00|1|5,43|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|5,08|
|Valor máximo en perfil|-1,00|1|28,97|

Tabla 23 - Cálculo de radiointerferencias para LTE 1x220 kV El Arriero - Centinela 22A30.1C

RI ANSI 1 MHz
Punto de medida x [m] y[m]

[db 1 uV/m]

TVI 71 MHz

[db 1 uV/m]

TVI 195 MHz

[db 1 uV/m]

|15 metros fase lateral derecha|19,71|2|28,98|-4,84|-13,62|
|---|---|---|---|---|---|
|15 metros fase lateral izquierda|-19,71|2|25,81|-8,01|-16,79|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 26 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Estructura 22A90.1C

Figura 12 - Campo eléctrico LTE 1x220 kV El Arriero - Centinela 22A90.1C

Tabla 24 Valores de campo eléctrico LTE 1x220 kV El Arriero - Centinela 22A90.1C

Campo Eléctrico
Punto de medida x [m] y[m]

[kV/m]

|Limite franja seguridad derecha|20,00|1|0,81|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|0,74|
|Valor máximo en perfil|-5,50|1|5,18|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 27 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Figura 13 - Campo magnético LTE 1x220 kV El Arriero - Centinela 22A90.1C

Tabla 25 Valores de campo magnético LTE 1x220 kV El Arriero - Centinela 22A90.1C

Campo Magnético
Punto de medida x [m] y[m]

[uT]

|Limite franja seguridad derecha|20,00|1|5,43|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|5,08|
|Valor máximo en perfil|-1,00|1|28,97|

Tabla 26 - Cálculo de radiointerferencias para LTE 1x220 kV El Arriero - Centinela 22A90.1C

RI ANSI 1 MHz
Punto de medida x [m] y[m]

[db 1 uV/m]

TVI 71 MHz

[db 1 uV/m]

TVI 195 MHz

[db 1 uV/m]

|15 metros fase lateral derecha|19,71|2|28,98|-4,84|-13,62|
|---|---|---|---|---|---|
|15 metros fase lateral izquierda|-19,71|2|25,81|-8,01|-16,79|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 28 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Estructura Portal 10 m

Figura 14 - Campo eléctrico LTE 1x220 kV El Arriero - Centinela Portal 10 m

Tabla 27 Valores de campo eléctrico LTE 1x220 kV El Arriero - Centinela Portal 10 m

Campo Eléctrico
Punto de medida x [m] y[m]

[kV/m]

|Limite franja seguridad derecha|20,00|1|0,92|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|0,92|
|Valor máximo en perfil|7,00|1|4,87|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 29 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Figura 15- Campo magnético LTE 1x220 kV El Arriero - Centinela Portal 10 m

Tabla 28 Valores de campo magnético LTE 1x220 kV El Arriero - Centinela Portal 10 m

Campo Magnético
Punto de medida x [m] y[m]

[uT]

|Limite franja seguridad derecha|20,00|1|5,39|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|5,39|
|Valor máximo en perfil|0,00|1|32,77|

Tabla 29 - Cálculo de radiointerferencias para LTE 1x220 kV El Arriero - Centinela Portal 10 m

RI ANSI 1 MHz
Punto de medida x [m] y[m]

[db 1 uV/m]

TVI 71 MHz

[db 1 uV/m]

TVI 195 MHz

[db 1 uV/m]

|15 metros fase lateral derecha|21,00|2|27,86|-5,96|-14,74|
|---|---|---|---|---|---|
|15 metros fase lateral izquierda|-21,00|2|27,86|-5,96|-14,74|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 30 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

5.1.2 Acometida en SE/E El Arriero

Figura 16 - Campo eléctrico Acometida SE/E El Arriero

Tabla 30 Valores de campo eléctrico Acometida SE/E El Arriero

Campo Eléctrico
Punto de medida x [m] y[m]

[kV/m]

|Limite franja seguridad derecha|30,00|1|0,25|
|---|---|---|---|
|Limite franja seguridad izquierda|-35,00|1|0,16|
|Valor máximo en perfil|6,00|1|4,51|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 31 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Figura 17 - Campo magnético Acometida SE/E El Arriero

Tabla 31 Valores de campo magnético Acometida SE/E El Arriero

Campo Magnético
Punto de medida x [m] y[m]

[uT]

|Limite franja seguridad derecha|30,00|1|2,00|
|---|---|---|---|
|Limite franja seguridad izquierda|-35,00|1|1,47|
|Valor máximo en perfil|0,00|1|30,78|

Tabla 32 - Cálculo de radiointerferencias para Acometida SE/E El Arriero

RI ANSI 1 MHz
Punto de medida x [m] y[m]

[db 1 uV/m]

TVI 71 MHz

[db 1 uV/m]

TVI 195 MHz

[db 1 uV/m]

|15 metros fase lateral derecha|20,00|2|29,72|-4,10|-12,88|
|---|---|---|---|---|---|
|15 metros fase lateral izquierda|-20,00|2|29,72|-4,10|-12,88|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 32 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

5.2 Interacción con instalaciones existentes

5.2.1 Cruce LTE 1x220 kV Encuentro - El Tesoro con LTE 1x220 kV Arriero - Centinela

Para abordar el cálculo de los valores en el cruce, serán sumados directamente a los valores de campo

eléctrico y magnético calculados a nivel de 1 [m] en la franja de seguridad tanto para la LTE 1x220 kV El

Arriero-Centinela y para la LTE 1x220 kV Encuentro - El Tesoro.

Los resultados obtenidos serán valores de “peor escenario”, pues los campos electromagnéticos son

entidades vectoriales, por lo tanto, su superposición puede incrementarlos como en una suma directa ó

eventualmente cancelarlos, dependiendo de factores geométricos, de la magnitud de las corrientes y

tensiones involucradas y los desfases angulares entre diferentes líneas de transmisión.

A continuación se presentan los valores obtenidos para la LTE Existente y proyectada, considerando la

altura de los conductores en el punto del cruce de acuerdo a lo indicado en el numeral 4.4 del presente

informe.

Línea existente:

Figura 18 - Campo eléctrico LTE 1x220kV Encuentro - El Tesoro

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 33 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Tabla 33 Valores de campo eléctrico LTE 1x220kV Encuentro - El Tesoro

Punto de medida x [m] y[m] Campo Eléctrico

[kV/m]

|Limite franja seguridad derecha|20,00|1|0,23|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|0,25|
|Valor máximo en perfil|-7,50|1|0,38|

Figura 19 - Campo magnético LTE 1x220kV Encuentro - El Tesoro

Tabla 34 Valores de campo magnético LTE 1x220kV Encuentro - El Tesoro

Punto de medida x [m] y[m] Campo Magnético

[T]

|Limite franja seguridad derecha|20,00|1|0,51|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|0,55|
|Valor máximo en perfil|-1,00|1|0,83|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 34 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Línea Proyectada:

Figura 20 - Campo eléctrico LTE 1x220kV El Arriero - Centinela (Cruce)

Tabla 35 Valores de campo eléctrico LTE 1x220kV El Arriero - Centinela (Cruce)

Campo Eléctrico
Punto de medida x [m] y[m]

[kV/m]

|Limite franja seguridad derecha|20,00|1|0,37|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|0,17|
|Valor máximo en perfil|14,50|1|0,38|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 35 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Figura 21 - Campo magnético LTE 1x220kV El Arriero - Centinela (Cruce)

Tabla 36 Valores de campo magnético LTE 1x220kV El Arriero - Centinela (Cruce)

Campo Magnético
Punto de medida x [m] y[m]

[uT]

|Limite franja seguridad derecha|20,00|1|1,36|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|1,37|
|Valor máximo en perfil|0,00|1|1,83|

Considerando la suma algebraica directa, se tiene en el cruce:

Tabla 37 Valores de campo eléctrico resultantes para el cruce

Punto de medida x [m] y[m] Campo Eléctrico

[kV/m]

|Limite franja seguridad derecha|20,00|1|0,60|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|0,42|
|Valor máximo en perfil|-7,50|1|0,76|

Tabla 38 Valores de campo magnético resultantes para el cruce

Punto de medida x [m] y[m] Campo Magnético

[uT]

|Limite franja seguridad derecha|20,00|1|1,88|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|1,92|
|Valor máximo en perfil|-1,00|1|2,66|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 36 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

5.2.2 Paralelismo con LTE 1x220 kV PE S. Gorda Este

Para abordar el cálculo de los valores del paralelismo, se simulará la instalación existente por si sola y luego

se supondrá en paralelismo la línea proyectada.

Línea existente:

Figura 22 - Campo eléctrico LTE 1x220 kV PE S. Gorda Este

Tabla 39 Valores de campo eléctrico LTE 1x220 kV PE S. Gorda Este

Punto de medida x [m] y[m] Campo Eléctrico

[kV/m]

|Limite franja seguridad derecha|20,00|1|0,61|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|0,52|
|Valor máximo en perfil|-5,50|1|3,72|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 37 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Figura 23 - Campo magnético estructura LTE 1x220 kV PE S. Gorda Este

Tabla 40 Valores de campo magnético LTE 1x220 kV PE S. Gorda Este

Punto de medida x [m] y[m] Campo Magnético

[T]

|Limite franja seguridad derecha|20,00|1|2,38|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|2,22|
|Valor máximo en perfil|-1,00|1|12,84|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 38 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Línea proyectada y línea existente:

Figura 24 - Campo eléctrico Paralelismo entre línea proyectada y existente

Tabla 41 Valores de campo eléctrico Paralelismo entre línea proyectada y existente

Punto de medida x [m] y[m] Campo Eléctrico

[kV/m]

|Limite franja seguridad derecha<br>(proyectada)|45,00|1|0,83|
|---|---|---|---|
|Limite franja seguridad izquierda<br>(existente)|-45,00|1|0,54|
|Valor máximo en perfil|19,50|1|5,08|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 39 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Figura 25 - Campo magnético estructura Paralelismo entre línea proyectada y existente

Tabla 42 Valores de campo magnético Paralelismo entre línea proyectada y existente

Punto de medida x [m] y[m] Campo Magnético

[uT]

|Limite franja seguridad derecha<br>(proyectada)|45,00|1|5,50|
|---|---|---|---|
|Limite franja seguridad izquierda<br>(existente)|-45,00|1|2,63|
|Valor máximo en perfil|24,50|1|28,44|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 40 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

5.2.3 Cruce LTE 1x220 kV El Tesoro - Esperanza con LTE 1x220 kV Arriero - Centinela

Para abordar el cálculo de los valores en el cruce, serán sumados directamente a los valores de campo

eléctrico y magnético calculados a nivel de 1 [m] en la franja de seguridad tanto para la LTE 1x220 kV El

Arriero-Centinela y para la LTE 1x220 kV El Tesoro - Esperanza.

Los resultados obtenidos serán valores de “peor escenario”, pues los campos electromagnéticos son

entidades vectoriales, por lo tanto, su superposición puede incrementarlos como en una suma directa ó

eventualmente cancelarlos, dependiendo de factores geométricos, de la magnitud de las corrientes y

tensiones involucradas y los desfases angulares entre diferentes líneas de transmisión.

A continuación, se presentan los valores obtenidos para la LTE Existente y proyectada, considerando la

altura de los conductores en el punto del cruce de acuerdo a lo indicado en el numeral 4.5 del presente

informe.

Línea existente:

Figura 26 - Campo eléctrico LTE 1x220kV El Tesoro - Esperanza

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 41 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Tabla 43 Valores de campo eléctrico LTE 1x220kV El Tesoro - Esperanza

Punto de medida x [m] y[m] Campo Eléctrico

[kV/m]

|Limite franja seguridad derecha|20,00|1|0,60|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|0,72|
|Valor máximo en perfil|6,50|1|3,51|

Figura 27 - Campo magnético LTE 1x220kV El Tesoro - Esperanza

Tabla 44 Valores de campo magnético LTE 1x220kV El Tesoro - Esperanza

Punto de medida x [m] y[m] Campo Magnético

[T]

|Limite franja seguridad derecha|20,00|1|2,55|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|2,06|
|Valor máximo en perfil|4,00|1|10,18|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 42 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Línea Proyectada:

Figura 28 - Campo eléctrico LTE 1x220kV El Arriero - Centinela (Cruce)

Tabla 45 Valores de campo eléctrico LTE 1x220kV El Arriero - Centinela (Cruce)

Campo Eléctrico
Punto de medida x [m] y[m]

[kV/m]

|Limite franja seguridad derecha|20,00|1|0,27|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|0,13|
|Valor máximo en perfil|15,00|1|0,28|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 43 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Figura 29 - Campo magnético LTE 1x220kV El Arriero - Centinela (Cruce)

Tabla 46 Valores de campo magnético LTE 1x220kV El Arriero - Centinela (Cruce)

Campo Magnético
Punto de medida x [m] y[m]

[uT]

|Limite franja seguridad derecha|20,00|1|1,36|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|1,37|
|Valor máximo en perfil|0,00|1|1,83|

Considerando la suma algebraica directa, se tiene en el cruce:

Tabla 47 Valores de campo eléctrico resultantes para el cruce

Punto de medida x [m] y[m] Campo Eléctrico

[kV/m]

|Limite franja seguridad derecha|20,00|1|0,87|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|0,85|
|Valor máximo en perfil|6,50|1|3,75|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 44 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Tabla 48 Valores de campo magnético resultantes para el cruce

Punto de medida x [m] y[m] Campo Magnético

[uT]

|Limite franja seguridad derecha|20,00|1|3,91|
|---|---|---|---|
|Limite franja seguridad izquierda|-20,00|1|3,43|
|Valor máximo en perfil|4,00|1|11,98|

5.2.4 Paralelismo con LTE 1x220 kV El Tesoro Esperanza

Para abordar el cálculo de los valores del paralelismo, se simulará la instalación existente en x=30 [m] y la

instalación proyectada en x= -30 [m], equivalente a la distancia mínima una vez establecido el paralelismo.

Línea proyectada y línea existente:

Figura 30 - Campo eléctrico Paralelismo entre línea proyectada y existente

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 45 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

Tabla 49 Valores de campo eléctrico Paralelismo entre línea proyectada y existente

Punto de medida x [m] y[m] Campo Eléctrico

[kV/m]

|Limite franja seguridad derecha<br>(proyectada)|50,00|1|0,60|
|---|---|---|---|
|Limite franja seguridad izquierda<br>(existente)|-50,00|1|0,61|
|Valor máximo en perfil|-24,50|1|3,77|

Figura 31 - Campo magnético estructura Paralelismo entre línea proyectada y existente

Tabla 50 Valores de campo magnético Paralelismo entre línea proyectada y existente

Punto de medida x [m] y[m] Campo Magnético

[uT]

|Limite franja seguridad derecha<br>(proyectada)|50,00|1|2,50|
|---|---|---|---|
|Limite franja seguridad izquierda<br>(existente)|-50,00|1|5,28|
|Valor máximo en perfil|-29,00|1|29,03|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 46 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

6 Comparación de valores máximos en borde de franja de seguridad

6.1 Normativa aplicable a campos electromagnéticos

En Chile no existe reglamentación relativa a los valores límites permitidos de exposición de las personas a

los campos electromagnéticos de frecuencia industrial.

No obstante, la regulación ambiental que rige el tema de emisiones señala que, de no existir una regulación

nacional, debe aplicarse como norma de referencia aquella que se encuentre vigente en estados

específicos.

El Decreto No 40 del Ministerio del Medio Ambiente, “Aprueba Reglamento del Sistema de Evaluación de

Impacto Ambiental”, publicado el 12-08-2013, y que entró en vigencia el 30-10-2012, indica en su Artículo

11:

_“Artículo 11.- Normas de referencia._

_Las normas de calidad ambiental y de emisión que se utilizarán como referencia para los efectos de evaluar si se_

_genera o presenta el riesgo indicado en la letra a) y los efectos adversos señalados en la letra b), ambas del artículo_

_11 de la Ley, serán aquellas vigentes en los siguientes Estados: República Federal de Alemania, República Argentina,_

_Australia, República Federativa del Brasil, Canadá, Reino de España, Estados Unidos Mexicanos, Estados Unidos de_

_América, Nueva Zelandia, Reino de los Países Bajos, República Italiana, Japón, Reino de Suecia y Confederación_

_Suiza. Para la utilización de las normas de referencia, se priorizará aquel Estado que posea similitud en sus_

_componentes ambientales, con la situación nacional y/o local, lo que será justificado razonablemente por el_

_proponente.”_

La tabla que se muestra a continuación presenta las principales normas de referencia aplicables en Chile,

de acuerdo con lo señalado en el Artículo 11.

Tabla 51 - Límites de Exposición Humana a Campos Electromagnéticos de 50-60 [Hz]

|Col1|Público General|Col3|Exposición Ocupacional|Col5|
|---|---|---|---|---|
|País/Entidad|Intensidad de campo<br>eléctrico [V/m]|Densidad de Flujo<br>magnético [uT]|Intensidad de campo<br>eléctrico [V/m]|Densidad de Flujo<br>magnético [uT]|
|Alemania|5.000|100|5.000|100|
|Argentina|3.000|25|3.000|25|
|Australia|5.000|100|10.000|500|
|Canadá|N/A|N/A|N/A|N/A|
|España|5.000|100|10.000|500|
|Italia|5.000|10|5.000|10|
|Japón|3.000|N/A|10.000|500|
|Estados Unidos (Florida)|2.000|15|2.000|15|
|Países Bajos|8.000|120|40.000|600|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 47 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

|Col1|Público General|Col3|Exposición Ocupacional|Col5|
|---|---|---|---|---|
|País/Entidad<br>|Intensidad de campo<br>eléctrico [V/m]<br>|Densidad de Flujo<br>magnético [uT]<br>|Intensidad de campo<br>eléctrico [V/m]<br>|Densidad de Flujo<br>magnético [uT]<br>|
|~~Suecia~~|~~N/A~~|~~N/A~~|~~N/A~~|~~N/A~~|
|Suiza|5.000|100|5.000|10|
|ICNIRP|5.000|200|10.000|500|
|IEEE|5.000|900|20.000|2.700|
|Unión Europea|5.000|100|10.000|500|

La recomendación de uso más frecuente para público general y exposición permanente, es la publicada

por la ICNIRP [1] ( _International Commission On Non-Ionizing Radiation Protection_ ), que establece 5.000

[V/m] para el campo eléctrico y 200 [uT] para la inducción magnética.

Sin embargo, la normativa del estado de Florida de los Estados Unidos de Norteamérica [4], posee límites

más restrictivos.

A continuación, se destacan los párrafos de la normativa del estado de Florida (62-814.450 Electric and

Magnetic Field Standards), aplicables al proyecto, donde se indican los límites máximos de exposición:

Del campo eléctrico:

“( _a) The maximum electric field at the edge of the transmission line ROW containing a 500 kV nominal voltage or less_

_transmission line or at the property boundary of a new substation containing facilities operating at these voltages_

_shall not exceed 2.00 kV/m”._

El máximo campo eléctrico en el límite de la franja de servidumbre de una línea de transmisión de 500 kV o menor

tensión, o bien, en el límite de una subestación de ese nivel de tensión no deberá exceder los 2 kV/m.

Del campo magnético:

_“(f) The maximum magnetic field at the edge of a 230 kV or smaller transmission line ROW or at the property boundary_

_of a new substation serving such lines shall not exceed 150 milliGauss”._

El máximo campo magnético en el límite de la franja de servidumbre de una línea de transmisión de 230kV o menor

tensión, o bien, en el límite de una subestación de ese nivel de tensión no deberá exceder los 150 milliGauss.

_Nota: 1 miliGauss equivale a 0,1 microTesla ( 1 [mG] = 0,1 [uT])._

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 48 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

6.2 Normativa aplicable a radiointerferencia y TVI

6.2.1 Radiointerferencia (RI)

La _Canadian Standards Association_ [8] indica que el nivel de perturbación radioeléctrica aceptable a 500

[kHz], a 15 [m] de la fase lateral externa, para una línea de 70 a 220 [kV] es de 46 [dB] sobre 1 [kV/m].

6.2.2 Interferencias de TV (TVI)

De acuerdo con las recomendaciones que ha publicado la Federal Communications Commision (FCC) de

Estados Unidos de América y el Departamento of Communications (DOC), se definen zonas de contorno

(grado A, grado B), las cuales son caracterizadas por valores mínimos del campo que contiene la señal.

El contorno de grado A, corresponde a los límites dentro de los cuales la fuerza mediana del campo es igual

o mayor a 68 [db 1uV/m] para canales 2 a 6 (71 Mhz) y 71 [db 1uV/m] para canales 7 al 13 (195 MHz).

El contorno de grado B, corresponde a los límites dentro de los cuales la fuerza mediana del campo es igual

o mayor a 47 [db 1uV/m] para canales 2 a 6 (71 Mhz) y 56 [db 1uV/m] para canales 7 al 13 (195 MHz).

El contorno de grado A es mayor, debido a que representa una zona con ruido electromagnético asociado

a la concentración de actividades humanas (ciudades).

El contorno de Grado B por su parte, representa una zona en general con ruido electromagnético inferior,

tales como la periferia de la ciudad.

La DOC ha establecido valores límites para el contorno de Grado B, en donde no se deben exceder los 17

[db 1uV/m] para los canales 2 al 6 (71 MHz) y 12 [db 1uV/m] para los canales 7 al 13 [db 1uV/m].

En el caso particular de este informe, se considerarán los límites de la DOC para el contorno de grado B

para verificar los valores de interferencia calculados.

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 49 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

6.3 Verificación de la normativa de acuerdo con los cálculos realizados

6.3.1 Verificación campos electromagnéticos en línea de transmisión

Tabla 52 - Verificación campo eléctrico línea de transmisión

|Línea|Campo<br>eléctrico<br>borde franja<br>derecha [m]<br>[kV/m]|Campo<br>eléctrico<br>borde<br>franja<br>izquierda<br>[m] [kV/m]|Campo<br>eléctrico<br>máximo<br>[kV/m]|Ubicación<br>máximo<br>[m]|Máximo valor<br>admisible en<br>borde de franja<br>/ SE [kV/m]|Cumple|
|---|---|---|---|---|---|---|
|Cruce Encuentro - El Tesoro|0,60|0,42|0,76|-7,50|2|Sí|
|Paralelismo PE Sierra Gorda|0,83|0,54|5,08|19,50|2|Sí|
|Estructura 22A1.1C|0,80|0,73|5,14|-5,50|2|Sí|
|Estructura 22A30.1C|0,81|0,74|5,18|-5,50|2|Sí|
|Estructura 22A90.1C|0,81|0,74|5,18|-5,50|2|Sí|
|Portal 10 m|0,92|0,92|4,87|7,00|2|Sí|
|Acometida a SE/E|0,25|0,16|4,51|6,00|2|Sí|
|Cruce El Tesoro - Esperanza|0,87|0,85|3,75|6,50|2|Sí|
|Paral. El Tesoro Esperanza|0,60|0,61|3,77|-24,50|2|Sí|

Tabla 53 - Verificación campo magnético línea de transmisión

|Tipo de estructura|Campo<br>magnético<br>borde franja<br>derecha<br>[uT]|Campo<br>magnético<br>borde<br>franja<br>izquierda<br>[uT]|Campo<br>magnético<br>máximo [uT]|Ubicación<br>máximo<br>[m]|Máximo valor<br>admisible en<br>borde de franja<br>/ SE [uT]|Cumple|
|---|---|---|---|---|---|---|
|Cruce Encuentro - El Tesoro|1,88|1,92|2,66|-1,00|15|Sí|
|Paralelismo PE Sierra Gorda|5,50|2,63|28,44|24,50|15|Sí|
|Estructura 22A1.1C|5,33|4,98|28,81|-1,00|15|Sí|
|Estructura 22A30.1C|5,43|5,08|28,97|-1,00|15|Sí|
|Estructura 22A90.1C|5,43|5,08|28,97|-1,00|15|Sí|
|Portal 10 m|5,39|5,39|32,77|0,00|15|Sí|
|Acometida a SE/E|2,00|1,47|30,78|0,00|15|Sí|
|Cruce El Tesoro - Esperanza|3,91|3,43|11,98|4,00|15|Sí|
|Paral. El Tesoro Esperanza|2,50|5,28|29,03|-29,00|15|Sí|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 50 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

6.3.2 Verificación de radio interferencia para las instalaciones del proyecto

Tabla 54- Verificación de radio interferencia instalaciones del proyecto

|Tipo de estructura|RI máximo|Límite [dB]|TVI 71<br>Mhz|Límite<br>[dB]|TVI 195<br>Mhz|Límite [dB]|Cumple?|
|---|---|---|---|---|---|---|---|
|Estructura 22A1.1C|29,03|46|-4,79|17|-13,57|12|SI|
|Estructura 22A30.1C|28,98|46|-4,84|17|-13,62|12|SI|
|Estructura 22A90.1C|28,98|46|-4,84|17|-13,62|12|SI|
|Portal 10 m|27,86|46|-5,96|17|-14,74|12|SI|
|Acometida a SE/E|29,72|46|-4,10|17|-12,88|12|SI|

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 51 de 52

GEOBIOTA Estudio de Campos Electromagnéticos Rev. 0

7 Conclusiones

De los resultados obtenidos mediante simulaciones computacionales y fórmulas empíricas se concluye que

el Proyecto respecto de sus emisiones electromagnéticas y sus efectos de radio-interferencia cumple

satisfactoriamente las normas de referencia.

8 Referencias

[1] Comisión Internacional sobre Protección Frente a Radiaciones No Ionizantes, «Recomendaciones

para limitar la exposición a campos eléctricos, magnéticos y electromagnéticos,» International

Commission on Non-Ionizing Radiation Protection, 1998.

[2] Secretaría de Energía / Energía Eléctrica (República de Argentina), «Resolución 77/98,» [En

línea]. Available: http://servicios.infoleg.gob.ar/infolegInternet/anexos/45000

49999/49781/norma.htm.

[3] MINISTERIO DE TRABAJO, EMPLEO Y SEGURIDAD SOCIAL (República Argentina), «HIGIENE Y

SEGURIDAD EN EL TRABAJO, ESPECIFICACIONES TÉCNICAS,» [En línea]. Available:

http://servicios.infoleg.gob.ar/infolegInternet/verNorma.do?id=90396.

[4] State of Florida, "Electric and Magnetic Field Standards," 1 6 2008. [Online]. Available:

https://www.flrules.org/gateway/RuleNo.asp?title=ELECTRIC%20AND%20MAGNETIC%20FIELD

S&ID=62-814.450.

[5] Superintendencia de Electricidad y Combustibles, «NSEG 5 En 71 - Reglamento de Corrientes

Fuertes,» 1971.

[6] R. D. Begamudre, Extra High Voltage AC Transmission Engineering, New Delhi: New Age

International Publishers, 2006.

[7] S. M. Wentworth, Applied Electromagnetics: Early Transmission Lines Approach, 2007.

[8] Canadian Standards Associations,, _Limits and Measurement Methods of EM Noise from AC Power_

_Systems, 0.15-30 MHz,,_ 1984.

P105-E-EST-01 DIA Planta Fotovoltaica Sierra Gorda Solar Página 52 de 52

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2: - Descripción de las variables de entrada al software**

| POS | [m] | Matriz de Nx2, donde N es el número de fases y cada fila representa la ubicación espacial x,y de cada<br>fase. |
| --- | --- | --- |
| I | [A] | Matriz de Nx1 donde N es el número de fases, matriz de corrientes eficaces en cada fase. (267 A) |
| rho | [m] | Resistividad equivalente del terreno. Se considerará un valor de 100 [m] |
| u_0 | [N/A2] | Permeabilidad magnética del aire |
| X | [m] | Vector que contiene las abscisas de los puntos donde se calculará el campo |
| Y | [m] | Vector que contiene las ordenadas de los puntos donde se calculará el campo |

**Tabla 3: - Ubicación espacial de las fases para estructura de suspensión 22A30.1**

| Tipo de estructura | Ubicación espacial de los conductores | Col3 |
| --- | --- | --- |
| Fases | X [m] | Y [m] |
| A | 4,6 | 7,32 |
| B | -4,6 | 7,32 |
| C | 4,6 | 13,32 |

**Tabla 4: - Ubicación espacial de las fases para estructura de suspensión 22A1.1**

| Tipo de estructura | Ubicación espacial de los conductores | Col3 |
| --- | --- | --- |
| Fases | X [m] | Y [m] |
| A | 4,71 | 7,32 |
| B | -4,71 | 7,32 |
| C | 4,71 | 13,32 |

**Tabla 5: - Ubicación espacial de las fases para estructura de suspensión 22A90.1**

| Tipo de estructura | Ubicación espacial de los conductores | Col3 |
| --- | --- | --- |
| Fases | X [m] | Y [m] |
| A | 4,71 | 7,32 |
| B | -4,71 | 7,32 |
| C | 4,71 | 13,32 |

**Tabla 7: - Parámetros eléctricos LTE 1x220 kV El Arriero - Centinela**

| Parámetro | Valor | Unidad |
| --- | --- | --- |
| Potencia Nominal | 400 | MVA |
| Tensión Nominal | 220 | kV |
| Corriente Nominal | 1050 | A |
| Conductores por fase | 2 | - |
| Nombre comercial del conductor | ACAR 800 MCM | - |
| Diámetro del conductor | 26,1 | mm |
| Separación entre subconductores | 400 | mm |

**Tabla 8: - Ubicación espacial de las fases para LTE 1x220kV Encuentro - El Tesoro en punto de cruce**

| Tipo de estructura | Ubicación espacial de los conductores existen, en el cruce con LTE<br>Proyectada | Col3 |
| --- | --- | --- |
| Fases | X [m] | Y [m] |
| A | -3,64 | 29,03 |
| B | 3,64 | 29,03 |
| C | -3,64 | 24,03 |

**Tabla 18: Valores de campo eléctrico LTE 1x220 kV El Arriero - Centinela 22A1.1C**

| Limite franja seguridad derecha | 20,00 | 1 | 0,80 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 0,73 |
| Valor máximo en perfil | -5,50 | 1 | 5,14 |

**Tabla 19: Valores de campo magnético LTE 1x220 kV El Arriero - Centinela 22A1.1C**

| Limite franja seguridad derecha | 20,00 | 1 | 5,33 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 4,98 |
| Valor máximo en perfil | -1,00 | 1 | 28,81 |

**Tabla 21: Valores de campo eléctrico LTE 1x220 kV El Arriero - Centinela 22A30.1C**

| Limite franja seguridad derecha | 20,00 | 1 | 0,81 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 0,74 |
| Valor máximo en perfil | -5,50 | 1 | 5,18 |

**Tabla 22: Valores de campo magnético LTE 1x220 kV El Arriero - Centinela 22A30.1C**

| Limite franja seguridad derecha | 20,00 | 1 | 5,43 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 5,08 |
| Valor máximo en perfil | -1,00 | 1 | 28,97 |

**Tabla 24: Valores de campo eléctrico LTE 1x220 kV El Arriero - Centinela 22A90.1C**

| Limite franja seguridad derecha | 20,00 | 1 | 0,81 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 0,74 |
| Valor máximo en perfil | -5,50 | 1 | 5,18 |

**Tabla 25: Valores de campo magnético LTE 1x220 kV El Arriero - Centinela 22A90.1C**

| Limite franja seguridad derecha | 20,00 | 1 | 5,43 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 5,08 |
| Valor máximo en perfil | -1,00 | 1 | 28,97 |

**Tabla 27: Valores de campo eléctrico LTE 1x220 kV El Arriero - Centinela Portal 10 m**

| Limite franja seguridad derecha | 20,00 | 1 | 0,92 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 0,92 |
| Valor máximo en perfil | 7,00 | 1 | 4,87 |

**Tabla 28: Valores de campo magnético LTE 1x220 kV El Arriero - Centinela Portal 10 m**

| Limite franja seguridad derecha | 20,00 | 1 | 5,39 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 5,39 |
| Valor máximo en perfil | 0,00 | 1 | 32,77 |

**Tabla 30: Valores de campo eléctrico Acometida SE/E El Arriero**

| Limite franja seguridad derecha | 30,00 | 1 | 0,25 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -35,00 | 1 | 0,16 |
| Valor máximo en perfil | 6,00 | 1 | 4,51 |

**Tabla 31: Valores de campo magnético Acometida SE/E El Arriero**

| Limite franja seguridad derecha | 30,00 | 1 | 2,00 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -35,00 | 1 | 1,47 |
| Valor máximo en perfil | 0,00 | 1 | 30,78 |

**Tabla 33: Valores de campo eléctrico LTE 1x220kV Encuentro - El Tesoro**

| Limite franja seguridad derecha | 20,00 | 1 | 0,23 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 0,25 |
| Valor máximo en perfil | -7,50 | 1 | 0,38 |

**Tabla 34: Valores de campo magnético LTE 1x220kV Encuentro - El Tesoro**

| Limite franja seguridad derecha | 20,00 | 1 | 0,51 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 0,55 |
| Valor máximo en perfil | -1,00 | 1 | 0,83 |

**Tabla 35: Valores de campo eléctrico LTE 1x220kV El Arriero - Centinela (Cruce)**

| Limite franja seguridad derecha | 20,00 | 1 | 0,37 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 0,17 |
| Valor máximo en perfil | 14,50 | 1 | 0,38 |

**Tabla 36: Valores de campo magnético LTE 1x220kV El Arriero - Centinela (Cruce)**

| Limite franja seguridad derecha | 20,00 | 1 | 1,36 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 1,37 |
| Valor máximo en perfil | 0,00 | 1 | 1,83 |

**Tabla 37: Valores de campo eléctrico resultantes para el cruce**

| Limite franja seguridad derecha | 20,00 | 1 | 0,60 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 0,42 |
| Valor máximo en perfil | -7,50 | 1 | 0,76 |

**Tabla 38: Valores de campo magnético resultantes para el cruce**

| Limite franja seguridad derecha | 20,00 | 1 | 1,88 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 1,92 |
| Valor máximo en perfil | -1,00 | 1 | 2,66 |

**Tabla 39: Valores de campo eléctrico LTE 1x220 kV PE S. Gorda Este**

| Limite franja seguridad derecha | 20,00 | 1 | 0,61 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 0,52 |
| Valor máximo en perfil | -5,50 | 1 | 3,72 |

**Tabla 40: Valores de campo magnético LTE 1x220 kV PE S. Gorda Este**

| Limite franja seguridad derecha | 20,00 | 1 | 2,38 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 2,22 |
| Valor máximo en perfil | -1,00 | 1 | 12,84 |

**Tabla 41: Valores de campo eléctrico Paralelismo entre línea proyectada y existente**

| Limite franja seguridad derecha<br>(proyectada) | 45,00 | 1 | 0,83 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda<br>(existente) | -45,00 | 1 | 0,54 |
| Valor máximo en perfil | 19,50 | 1 | 5,08 |

**Tabla 42: Valores de campo magnético Paralelismo entre línea proyectada y existente**

| Limite franja seguridad derecha<br>(proyectada) | 45,00 | 1 | 5,50 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda<br>(existente) | -45,00 | 1 | 2,63 |
| Valor máximo en perfil | 24,50 | 1 | 28,44 |

**Tabla 43: Valores de campo eléctrico LTE 1x220kV El Tesoro - Esperanza**

| Limite franja seguridad derecha | 20,00 | 1 | 0,60 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 0,72 |
| Valor máximo en perfil | 6,50 | 1 | 3,51 |

**Tabla 44: Valores de campo magnético LTE 1x220kV El Tesoro - Esperanza**

| Limite franja seguridad derecha | 20,00 | 1 | 2,55 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 2,06 |
| Valor máximo en perfil | 4,00 | 1 | 10,18 |

**Tabla 45: Valores de campo eléctrico LTE 1x220kV El Arriero - Centinela (Cruce)**

| Limite franja seguridad derecha | 20,00 | 1 | 0,27 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 0,13 |
| Valor máximo en perfil | 15,00 | 1 | 0,28 |

**Tabla 46: Valores de campo magnético LTE 1x220kV El Arriero - Centinela (Cruce)**

| Limite franja seguridad derecha | 20,00 | 1 | 1,36 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 1,37 |
| Valor máximo en perfil | 0,00 | 1 | 1,83 |

**Tabla 47: Valores de campo eléctrico resultantes para el cruce**

| Limite franja seguridad derecha | 20,00 | 1 | 0,87 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 0,85 |
| Valor máximo en perfil | 6,50 | 1 | 3,75 |

**Tabla 48: Valores de campo magnético resultantes para el cruce**

| Limite franja seguridad derecha | 20,00 | 1 | 3,91 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda | -20,00 | 1 | 3,43 |
| Valor máximo en perfil | 4,00 | 1 | 11,98 |

**Tabla 49: Valores de campo eléctrico Paralelismo entre línea proyectada y existente**

| Limite franja seguridad derecha<br>(proyectada) | 50,00 | 1 | 0,60 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda<br>(existente) | -50,00 | 1 | 0,61 |
| Valor máximo en perfil | -24,50 | 1 | 3,77 |

**Tabla 50: Valores de campo magnético Paralelismo entre línea proyectada y existente**

| Limite franja seguridad derecha<br>(proyectada) | 50,00 | 1 | 2,50 |
| --- | --- | --- | --- |
| Limite franja seguridad izquierda<br>(existente) | -50,00 | 1 | 5,28 |
| Valor máximo en perfil | -29,00 | 1 | 29,03 |

**Tabla 51: - Límites de Exposición Humana a Campos Electromagnéticos de 50-60 [Hz]**

| Col1 | Público General | Col3 | Exposición Ocupacional | Col5 |
| --- | --- | --- | --- | --- |
| País/Entidad | Intensidad de campo<br>eléctrico [V/m] | Densidad de Flujo<br>magnético [uT] | Intensidad de campo<br>eléctrico [V/m] | Densidad de Flujo<br>magnético [uT] |
| Alemania | 5.000 | 100 | 5.000 | 100 |
| Argentina | 3.000 | 25 | 3.000 | 25 |
| Australia | 5.000 | 100 | 10.000 | 500 |
| Canadá | N/A | N/A | N/A | N/A |
| España | 5.000 | 100 | 10.000 | 500 |
| Italia | 5.000 | 10 | 5.000 | 10 |
| Japón | 3.000 | N/A | 10.000 | 500 |
| Estados Unidos (Florida) | 2.000 | 15 | 2.000 | 15 |
| Países Bajos | 8.000 | 120 | 40.000 | 600 |

**Tabla 52: - Verificación campo eléctrico línea de transmisión**

| Línea | Campo<br>eléctrico<br>borde franja<br>derecha [m]<br>[kV/m] | Campo<br>eléctrico<br>borde<br>franja<br>izquierda<br>[m] [kV/m] | Campo<br>eléctrico<br>máximo<br>[kV/m] | Ubicación<br>máximo<br>[m] | Máximo valor<br>admisible en<br>borde de franja<br>/ SE [kV/m] | Cumple |
| --- | --- | --- | --- | --- | --- | --- |
| Cruce Encuentro - El Tesoro | 0,60 | 0,42 | 0,76 | -7,50 | 2 | Sí |
| Paralelismo PE Sierra Gorda | 0,83 | 0,54 | 5,08 | 19,50 | 2 | Sí |
| Estructura 22A1.1C | 0,80 | 0,73 | 5,14 | -5,50 | 2 | Sí |
| Estructura 22A30.1C | 0,81 | 0,74 | 5,18 | -5,50 | 2 | Sí |
| Estructura 22A90.1C | 0,81 | 0,74 | 5,18 | -5,50 | 2 | Sí |
| Portal 10 m | 0,92 | 0,92 | 4,87 | 7,00 | 2 | Sí |
| Acometida a SE/E | 0,25 | 0,16 | 4,51 | 6,00 | 2 | Sí |
| Cruce El Tesoro - Esperanza | 0,87 | 0,85 | 3,75 | 6,50 | 2 | Sí |
| Paral. El Tesoro Esperanza | 0,60 | 0,61 | 3,77 | -24,50 | 2 | Sí |

**Tabla 53: - Verificación campo magnético línea de transmisión**

| Tipo de estructura | Campo<br>magnético<br>borde franja<br>derecha<br>[uT] | Campo<br>magnético<br>borde<br>franja<br>izquierda<br>[uT] | Campo<br>magnético<br>máximo [uT] | Ubicación<br>máximo<br>[m] | Máximo valor<br>admisible en<br>borde de franja<br>/ SE [uT] | Cumple |
| --- | --- | --- | --- | --- | --- | --- |
| Cruce Encuentro - El Tesoro | 1,88 | 1,92 | 2,66 | -1,00 | 15 | Sí |
| Paralelismo PE Sierra Gorda | 5,50 | 2,63 | 28,44 | 24,50 | 15 | Sí |
| Estructura 22A1.1C | 5,33 | 4,98 | 28,81 | -1,00 | 15 | Sí |
| Estructura 22A30.1C | 5,43 | 5,08 | 28,97 | -1,00 | 15 | Sí |
| Estructura 22A90.1C | 5,43 | 5,08 | 28,97 | -1,00 | 15 | Sí |
| Portal 10 m | 5,39 | 5,39 | 32,77 | 0,00 | 15 | Sí |
| Acometida a SE/E | 2,00 | 1,47 | 30,78 | 0,00 | 15 | Sí |
| Cruce El Tesoro - Esperanza | 3,91 | 3,43 | 11,98 | 4,00 | 15 | Sí |
| Paral. El Tesoro Esperanza | 2,50 | 5,28 | 29,03 | -29,00 | 15 | Sí |

**Tabla 54-: Verificación de radio interferencia instalaciones del proyecto**

| Tipo de estructura | RI máximo | Límite [dB] | TVI 71<br>Mhz | Límite<br>[dB] | TVI 195<br>Mhz | Límite [dB] | Cumple? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Estructura 22A1.1C | 29,03 | 46 | -4,79 | 17 | -13,57 | 12 | SI |
| Estructura 22A30.1C | 28,98 | 46 | -4,84 | 17 | -13,62 | 12 | SI |
| Estructura 22A90.1C | 28,98 | 46 | -4,84 | 17 | -13,62 | 12 | SI |
| Portal 10 m | 27,86 | 46 | -5,96 | 17 | -14,74 | 12 | SI |
| Acometida a SE/E | 29,72 | 46 | -4,10 | 17 | -12,88 | 12 | SI |
