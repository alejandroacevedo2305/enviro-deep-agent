---
title: Sin título
author: Nelson MO
date: D:20181009182311-03'00'
language: es
type: manual
pages: 33
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - ESTUDIO DE CAMPOS ELECTROMAGNÉTICOS PROYECTO; “SUBESTACIÓN SECCIONADORA RÍO TOLTÉN 2X220 KV” TITULAR: SOCIEDAD AUSTRAL DE TRANSMISIÓN TRONCAL S.A (SATT)
-->

# ESTUDIO DE CAMPOS ELECTROMAGNÉTICOS PROYECTO; “SUBESTACIÓN SECCIONADORA RÍO TOLTÉN 2X220 KV” TITULAR: SOCIEDAD AUSTRAL DE TRANSMISIÓN TRONCAL S.A (SATT)

**Nelson Morales Osorio**

**Octubre, 2018**

**CONTENIDO**

1 Objetivo ........................................................................................................................................... 5
2 Antecedentes del proyecto .......................................................................................................... 5
3 Metodología para la estimación de Campos Electromagnéticos ........................................... 9

4 Simulación de la S/E Seccionadora Río Toltén 220 kV ........................................................ 10

5 Estimación de radio interferencia de barras y líneas ........................................................... 15
6 Campo eléctrico de baja frecuencia en Subestaciones de 220 kV ..................................... 17
7 Campo magnético de baja frecuencia en Subestaciones de 220 kV ................................. 18

8 Radio Interferencia en Subestaciones de 220 kV ................................................................. 19

9 Simulación de la línea seccionada en torre E100A ............................................................... 21

10 Radio Interferencia en línea seccionada en torre E100A .................................................. 24

11 Normas en Chile para exposición a campos electromagnéticos de 50 Hz ...................... 25
12 Límites de radio interferencia provocada por instalaciones de alta tensión. ................... 25

13 Conclusiones ............................................................................................................................. 26
14 Área de influencia ..................................................................................................................... 27

15 Referencias ................................................................................................................................ 28

16 ANEXO ....................................................................................................................................... 29

16.1 Campo eléctrico superficial en Barras ................................................................................ 29
16.2 Campo eléctrico superficial en Líneas ............................................................................... 31
16.3 Campo eléctrico superficial en remate de Líneas ............................................................ 32

**LISTADO DE TABLAS**

Tabla 1 Características línea 2x220 kV Ciruelos - Cautín ................................................. 6

Tabla 2 Sección y tipo de los conductores empleados en seccionamientos ...................... 6
Tabla 3 Sección y tipo de los conductores empleados en subestación ............................. 6
Tabla 4 Conductores por fase empleados ......................................................................... 6
Tabla 5 Conjunto Aislación Subestación Seccionadora Río Toltén 220 kV ....................... 7
Tabla 6 Valores de campo electromagnético a 1,0 metro sobre el suelo.......................... 15
Tabla 7 Valores de campo electromagnético a 1,0 metro sobre el suelo.......................... 24
Tabla 8 Valores de Interferencias de Radio, recomendados por Asociación de Normas
Canadienses [7] ............................................................................................................... 26

4

**LISTADO DE ILUSTRACIONES**

Ilustración 1 Esquema ubicación Subestación Seccionadora Río Toltén 220 kV .................. 5

Ilustración 2 Torre de remate E100A ........................................................................................... 7

Ilustración 3 Layout general Subestación Seccionadora Río Toltén 220 kV .......................... 8

Ilustración 4 Vistas de seccionamientos ...................................................................................... 9

Ilustración 5 Trayectorias seleccionadas para simulación ...................................................... 10
Ilustración 6 Distribución de equipotenciales eléctricas en trayectoria A1 - A2 .................. 11
Ilustración 7 Campo eléctrico a 1m del suelo en trayectoria A1 - A2 ................................... 12
Ilustración 8 Distribución de equipotenciales magnéticas en trayectoria A1 - A2 ............... 12
Ilustración 9 Inducción magnética a 1m del suelo en trayectoria A1 - A2 ........................... 13
Ilustración 10 Distribución de equipotenciales eléctricas en trayectoria B1 - B2 ................ 13
Ilustración 11 Campo eléctrico a 1m del suelo en trayectoria B1 - B2 ................................ 14
Ilustración 12 Distribución de equipotenciales magnéticas en trayectoria B1 - B2 ............. 14
Ilustración 13 Inducción magnética a 1m del suelo en trayectoria B1 - B2 ......................... 15
Ilustración 14 Radio interferencia generada por barras ......................................................... 16
Ilustración 15 Radio interferencia generada por líneas ........................................................... 17
Ilustración 16 Campo eléctrico a 1 [m] del suelo, en patio de 220 kV, sector de acceso
de empalmes a edificio [3] ............................................................................................................ 18
Ilustración 17 Inducción magnética medida en la subestación [4] ........................................ 19
Ilustración 18 Inducción magnética calculada en la subestación [4] ..................................... 19
Ilustración 19 Esquema de la subestación Snakefarm de 230 KV y puntos de medida de
radio interferencia [5] ..................................................................................................................... 20
Ilustración 20 Radio interferencia medida en puntos de borde de subestación Snakefarm
230 kV [5] ......................................................................................................................................... 21
Ilustración 21 Malla de elementos finitos en el plano transversal ......................................... 21
Ilustración 22 Distribución de líneas equipotenciales eléctricas ............................................. 22
Ilustración 23 Campo eléctrico bajo la línea, a 1m de altura sobre el suelo ........................ 22
Ilustración 24 Distribución de líneas equipotenciales magnéticas ........................................ 23
Ilustración 25 Inducción magnética bajo la línea, a 1m de altura sobre el suelo ................. 23
Ilustración 26 Radio interferencia generada por conductores en torre E100A .................... 24

**1. Objetivo**

El objetivo de este estudio es obtener una estimación de los campos electromagnéticos
de baja y alta frecuencia que pueden estar presentes durante la operación de la
**“Subestación Seccionadora Río Toltén 220 kV”** del titular _Sociedad Austral de_

_Transmisión Troncal S.A (SATT_ ), que seccionará la línea 2x220 kV Ciruelos - Cautín,
incluyendo el tramo de seccionamiento de la línea.

**2. Antecedentes del proyecto**

El proyecto consiste en la construcción de una nueva subestación de nombre Río Toltén,
en configuración interruptor y medio, tecnología AIS y capacidad mínima de barras de
1000 MVA. En esta subestación se seccionará la línea 2x220 kV Ciruelos - Cautín. La

subestación se emplazará en la Región de La Araucanía, Comuna de Freire
aproximadamente a 31 km al sur de la actual subestación Cautín 220 kV, siguiendo el
trazado de la línea 2x220 Ciruelos - Cautín.

**Ilustración 1 Esquema ubicación Subestación Seccionadora Río Toltén 220 kV**
La línea 2x220 kV Ciruelos - Cautín existente tiene las siguientes características:

6

**Tabla 1 Características línea 2x220 kV Ciruelos - Cautín**

|Tensión de operación :|220 kV|
|---|---|
|Número de circuitos :|2|
|Número de conductores por fase :|1|
|Resistencia a 25oC en conductor :|0,0904 ohm/km|
|Conductor existente :|ACSR Grosbeak|
|Cable de guardia :|La línea no presenta cable de guardia|
|Capacidad térmica informada|506 Amperes, calculados a 50oC de temperatura<br>en conductor y 25oC de temperatura ambiente|
|Máxima capacidad|193 MVA|

En las tablas siguientes se indica la sección de los conductores para cada una de las
líneas contempladas en el proyecto.

**Tabla 2 Sección y tipo de los conductores empleados en seccionamientos**

|Línea|Tipo|Sección [mm2]|
|---|---|---|
|Seccionamiento Línea<br>2x220 kV Ciruelos - Cautín|1 x ACSR Grosbeak|1 x 375|

**Tabla 3 Sección y tipo de los conductores empleados en subestación**

|Subestación|Tipo|Sección [mm2]|
|---|---|---|
|Barras 220 kV|2 x AAC COWSLIP|2 x 1013|
|Paños de línea 220 kV|1 x AAC COWSLIP|1 x 1013|

**Tabla 4 Conductores por fase empleados**

|Línea|Descripción|
|---|---|
|Seccionamiento Línea 2x220 kV Ciruelos - Cautín|1 conductor por fase|
|Subestación|Descripción|
|Barras 220 kV|2 conductores por fase|
|Paños de línea 220 kV|1 conductor por fase|

La estructura de remate, E100A, presenta la configuración de la figura siguiente:

7

**Ilustración 2 Torre de remate E100A**

La altura de la torre es 25,75 m; se considera que los conductores (en su punto más bajo)
dispuestos de forma vertical en la torre de remate E100A, podrían alcanzar alturas de
14m, 19m y 24m.

Para el proyecto, se considera una topología de interruptor y medio en donde se
entenderá por “diagonal”, a la sección constituida por dos (2) interruptores externos
(paños externos) y un (1) interruptor central (paño central), cada uno con dos (2) juegos
de desconectadores y dos (2) juegos de transformadores de corriente, uno a cada lado.

**Tabla 5 Conjunto Aislación Subestación Seccionadora Río Toltén 220 kV**

|Tipo|Antiniebla (Fog Type)|
|---|---|
|Acople|Cuenca y Bola|
|Diámetro de la pollera|254 mm|
|Espaciamiento nominal|146 mm|
|Distancia de fuga|432 mm|
|Carga de ruptura|70 kN|
|Número de Aisladores|16|

8

**Ilustración 3 Layout general Subestación Seccionadora Río Toltén 220 kV**

Fuente: Plano SAE-RTO-SE-DPSE-0001

9

**Ilustración 4 Vistas de seccionamientos**

Fuente: Plano SAE-RTO-SE-DCSE-0001

**3. Metodología para la estimación de Campos Electromagnéticos**

La magnitud del campo electromagnético emitido por la subestación y la línea seccionada
se estima desarrollando una modelación simplificada, considerando barras y líneas de
transmisión en la subestación, utilizando el método de elementos finitos mediante el
software utilitario QuickField [1].

Se complementa la estimación teórica incorporando información recogida de la literatura
técnica de valores obtenidos en subestaciones similares en niveles de tensión y potencia,
ya sea por medida directa en terreno o aplicación de modelos. Se entrega también
información recogida de referencias internacionales respecto de valores de radio
interferencias medidas en instalaciones de 220 kV, similares a la subestación del

proyecto.

10

Finalmente se presenta las normas de referencia internacional respecto de magnitudes
aceptables de radio interferencia y las normas aplicables en Chile para la exposición
humana a campos electromagnéticos de 50 Hz, con el propósito de confrontar estos
valores con las estimaciones efectuadas y evaluar el efecto de las nuevas instalaciones.

**4. Simulación de la S/E Seccionadora Río Toltén 220 kV**

La metodología utilizada para la solución del campo eléctrico y de la inducción magnética,
consiste en una modelación de los conductores de las barras y líneas de 220 kV de la
subestación, utilizando elementos finitos y el software utilitario QuickField [1], a través de
la trayectoria A1 - A2 y de la trayectoria B1 - B2 mostradas en la figura siguiente.

**Ilustración 5 Trayectorias seleccionadas para simulación**

11

El resultado del estudio se presenta en la forma de perfiles de campo evaluados a una
altura de 1,0 m sobre el suelo; se escogió el perfil A1 - A2 por atravesar las líneas y el
perfil B1 - B2 por atravesar las barras; mediante la información de ambos perfiles se
tendrá el efecto en los bordes de la subestación. Los conductores de las barras se

consideraron a una altura de 10 m sobre el suelo, con 4,0 m de separación entre los
conductores de fases de las barras o de las líneas.

Las figuras siguientes muestran respectivamente el campo eléctrico y el campo magnético
a 1 [m] sobre el suelo en la trayectoria A1 - A2 y en la trayectoria B1 - B2. Se indica con
puntos rojos las ubicaciones relativas de los conductores de barras y líneas y en línea roja
el borde más próximo de la subestación.

Para la estimación del campo magnético se consideró conservativamente los valores
3000 Amperes para la corriente máxima de barras y 1000 Amperes para la corriente
máxima de líneas.

**Ilustración 6 Distribución de equipotenciales eléctricas en trayectoria A1 - A2**

12

**Ilustración 7 Campo eléctrico a 1m del suelo en trayectoria A1 - A2**

**Ilustración 8 Distribución de equipotenciales magnéticas en trayectoria A1 - A2**

13

**Ilustración 9** **Inducción magnética a 1m del suelo en trayectoria A1 - A2**

**Ilustración 10 Distribución de equipotenciales eléctricas en trayectoria B1 - B2**

14

**Ilustración 11 Campo eléctrico a 1m del suelo en trayectoria B1 - B2**

**Ilustración 12** **Distribución de equipotenciales magnéticas en trayectoria B1 - B2**

15

**Ilustración 13 Inducción magnética a 1m del suelo en trayectoria B1 - B2**

En la Tabla siguiente se presenta el máximo valor de campo eléctrico y de campo
magnético encontrado en cada perfil a 1,0 metro sobre el suelo, y el valor en el borde de
la subestación para ambas trayectorias.

**Tabla 6 Valores de campo electromagnético a 1,0 metro sobre el suelo**

|Col1|Campo eléctrico|Col3|Inducción magnética|Col5|
|---|---|---|---|---|
||Máximo<br> [V/m]|Borde S/E<br>[V/m]|Máximo<br>[micro Tesla]|Borde S/E<br>[micro Tesla]|
|Trayectoria A1 - A2|2.100|600|15,0|4,5|
|Trayectoria B1 - B2|2.400|250|38,0|5,8|

**5. Estimación de radio interferencia de barras y líneas**

Para evaluar radio interferencia se requiere evaluar el campo eléctrico superficial
existente en los conductores. En el Apéndice se entrega el resultado del programa
LINEAS, de elaboración propia, que calcula campo eléctrico en la superficie de un arreglo

16

de conductores de disposición arbitraria. Una vez evaluado el campo eléctrico superficial,
se aplica el método Cigre [2] para determinar la radio interferencia.

Se modela en primer lugar la disposición de barras, y el resultado en la trayectoria B1B2, graficado desde el eje de la Barra Principal N°2 se presenta en la siguiente Figura
(existe simetría hacia el otro lado de la barra).

**Ilustración 14 Radio interferencia generada por barras**

**Fuente: Elaboración propia**

Del gráfico de la i Radio interferencia generada por barrasse observa que en el borde de
la subestación (120 m desde el eje de la barra 1) la radio interferencia es 34,6 [dB/uV/m] y
a 15 m hacia el exterior, el valor es 32,8 [dB/uV/m].

A continuación se modela la disposición de líneas en la trayectoria A1-A2; el resultado,
graficado desde el eje de la línea Cautín 1 se presenta en la siguiente figura (se grafica
hacia el sector donde se encuentra más cercano el muro perimetral).

17

**Ilustración 15** **Radio interferencia generada por líneas**

**Fuente: Elaboración propia**

Del gráfico de la Radio interferencia generada por líneas se observa que en el borde de la
subestación (37 m desde el eje de la línea Cautín 1) la radio interferencia es 38,3

[dB/uV/m] y a 15 m hacia el exterior, el valor es 35,5 [dB/uV/m].

**6. Campo eléctrico de baja frecuencia en Subestaciones de 220 kV**

El campo eléctrico en un punto cualquiera del espacio representa la fuerza, en magnitud y
dirección, que sería aplicada a una carga unitaria positiva ubicada en ese punto. Sus
unidades son Volt por metro [V/m] o kilo Volt por metro [kV/m] en alta tensión.

En la vecindad de una subestación AIS, la presencia de este campo se debe a que el
conductor de alta tensión está directamente expuesto al aire (no existe aislamiento sólido,
el aislamiento está definido por espaciamientos de aire) y sobre dicho conductor está
aplicado un alto voltaje respecto de tierra, que actúa como conductor de referencia a
potencial cero. Para investigar sus efectos, se acostumbra caracterizar al campo eléctrico
cerca de una instalación de alta tensión por el concepto “Campo eléctrico a nivel del
suelo”, que corresponde al campo eléctrico medido o calculado a 1 metro de altura sobre
el suelo, en ausencia de otros objetos conductores.

En la figura siguiente se muestra dos perfiles del campo eléctrico medidos a 1 [m] sobre el
nivel del suelo, según distintas direcciones, en el patio de 220 kV de la subestación de
220/110 kV Los Almendros [3].

18

**Ilustración 16 Campo eléctrico a 1 [m] del suelo, en patio de 220 kV, sector de**

**acceso de empalmes a edificio [3]**

La gráfica muestran dos perfiles en el patio de 220 kV, en trayectorias paralelas,
separadas aproximadamente 30 m. Se aprecia que el campo eléctrico presenta altos
valores al interior del patio, en ambas gráficas, y luego baja drásticamente en los límites
del patio, (extremos de ambos gráficos) llegando a valores no superiores a **1.000 [V/m].**

**7. Campo magnético de baja frecuencia en Subestaciones de 220 kV**

De la referencia [4] se reproduce a continuación resultados de las medidas y simulación
efectuada para determinar el campo magnético en una subestación de 230 kV con 4
líneas. La Ilustración 17 Inducción magnética medida en la subestación [4]presenta el
resultado de las medidas efectuadas en la subestación y la Ilustración 18 Inducción
magnética calculada en la subestación [4]el resultado de la simulación.

19

**Ilustración 17 Inducción magnética medida en la subestación [4]**

**Ilustración 18 Inducción magnética calculada en la subestación [4]**

Se aprecia que tanto en la realidad (valores medidos) como en la estimación, la inducción
magnética en el borde de la subestación está bajo **5 [micro Tesla].**

**8. Radio Interferencia en Subestaciones de 220 kV**

La radio interferencia es generada por el fenómeno corona, el cual depende directamente
de la magnitud de campo eléctrico presente en la superficie de los conductores de alta
tensión. A su vez, este campo eléctrico superficial es directamente proporcional al nivel de

20

voltaje de la instalación, en este caso, barras de 220 kV. En la referencia [5] se informa de
medidas efectuadas en una subestación regularmente operando en 230 kV.

La Ilustración 19 Esquema de la subestación Snakefarm de 230 KV y puntos de medida
de radio interferencia [5] indica el esquema de la subestación y los puntos de medida de
radio interferencia, ubicados en el perímetro interior.

**Ilustración 19 Esquema de la subestación Snakefarm de 230 KV y puntos de**

**medida de radio interferencia [5]**

La medida de radio interferencia en los puntos indicados, a distintas frecuencias, entrega
los valores mostrados en la Ilustración 20 Radio interferencia medida en puntos de borde
de subestación Snakefarm 230 kV [5]

21

**Ilustración 20 Radio interferencia medida en puntos de borde de subestación**

**Snakefarm 230 kV [5]**
De la información anterior se observa que en el caso de una subestación abierta en 230
kV, el nivel de radio interferencia generado a 0,5 MHz no supera **50 [dB/ 1uV/m** ] en el
contorno interior de la subestación.

**9. Simulación de la línea seccionada en torre E100A**

La metodología utilizada para la solución del campo eléctrico y de la inducción magnética,
en la línea consiste en una modelación de la estructura y su entorno mediante elementos
finitos y el software utilitario QuickField [1], para resolver campo eléctrico y campo
magnético en un plano transversal a la línea.

La Ilustración siguiente muestra la malla de elementos finitos en el plano transversal. La
línea transversal señala la superficie del suelo.

**Ilustración 21 Malla de elementos finitos en el plano transversal**

La siguiente Ilustración corresponde a la distribución espacial de líneas equipotenciales
eléctricas. Las líneas rojas en los gráficos de campo indican el borde de la franja de
seguridad.

22

**Ilustración 22 Distribución de líneas equipotenciales eléctricas**

El campo eléctrico a 1m de altura sobre el suelo, según una trayectoria transversal a la
línea, considerando la torre ubicada en la posición L=50 m es la siguiente.

**Ilustración 23 Campo eléctrico bajo la línea, a 1m de altura sobre el suelo**

23

El campo magnético se calcula ocupando la capacidad de transmisión del conductor, 690
Amperes, con el siguiente resultado:

**Ilustración 24 Distribución de líneas equipotenciales magnéticas**

**Ilustración 25 Inducción magnética bajo la línea, a 1m de altura sobre el suelo**

24

En la Tabla siguiente se presenta el máximo valor de campo eléctrico y de campo
magnético encontrado en cada perfil a 1,0 metro sobre el suelo, y el valor en el borde de
la franja de seguridad, considerada en 2x20m.

**Tabla 7 Valores de campo electromagnético a 1,0 metro sobre el suelo**

|Col1|Campo eléctrico|Col3|Inducción magnética|Col5|
|---|---|---|---|---|
||Máximo<br> [V/m]|Borde franja<br>[V/m]|Máximo<br>[micro Tesla]|Borde franja<br>[micro Tesla]|
|Torre E100A|2.780|550|3,21|0,82|

**10. Radio Interferencia en línea seccionada en torre E100A**

En el Apéndice se entrega el resultado del programa LINEAS, de elaboración propia, que
calcula campo eléctrico en la superficie de un arreglo de conductores definido por la
estructura E100A. Una vez evaluado el campo eléctrico superficial, se aplica el método
Cigré [2] para determinar la radio interferencia.

El resultado para la radio interferencia emitida por la configuración de conductores
definida por la estructura de remate E100A se muestra en la figura siguiente:

**Ilustración 26 Radio interferencia generada por conductores en torre E100A**

**Fuente: Elaboración propia**

Del gráfico de la Radio interferencia generada por barras se observa que a 15 m de la
fase externa, (aproximadamente 19 m desde el eje de la línea), la radio interferencia es
40,6 [dB/uV/m].

25

**11. Normas en Chile para exposición a campos electromagnéticos de 50 Hz**

En nuestro país no existe reglamentación relativa a los valores límites permitidos de
exposición de las personas a los campos electromagnéticos de frecuencia industrial. No
obstante, la regulación ambiental que rige el tema de emisiones señala que de no existir
una regulación nacional, debe aplicarse como norma de referencia aquella que se
encuentre vigente en estados específicos.

El Decreto No40 del Ministerio del Medio Ambiente, “Aprueba Reglamento del Sistema de
Evaluación de Impacto Ambiental”, publicado el 12-08-2013, y que entró en vigencia el 2412-2013, indica en su Artículo 11:

_Artículo 11.- Normas de referencia._

_Las normas de calidad ambiental y de emisión que se utilizarán como referencia para los_
_efectos de evaluar si se genera o presenta el riesgo indicado en la letra a) y los efectos_
_adversos señalados en la letra b), ambas del artículo 11 de la Ley, serán aquellas_
_vigentes en los siguientes Estados: República Federal de Alemania, República Argentina,_
_Australia, República Federativa del Brasil, Canadá, Reino de España, Estados Unidos_
_Mexicanos, Estados Unidos de América, Nueva Zelandia, Reino de los Países Bajos,_
_República Italiana, Japón, Reino de Suecia y Confederación Suiza. Para la utilización de_
_las normas de referencia, se priorizará aquel Estado que posea similitud en sus_
_componentes ambientales, con la situación nacional y/o local, lo que será justificado_
_razonablemente por el proponente._

La recomendación de uso más frecuente para público general y exposición permanente,
es la publicada por la ICNIRP [6], organismo no gubernamental reconocido por la
Organización Mundial de la Salud como referente en el tema de campos
electromagnéticos y salud, que establece como límites seguros 5.000 [V/m] para el campo
eléctrico y 200 [micro Tesla] para la inducción magnética, valores incorporados en la
normativa de varios países mencionados en la nómina anterior.

**12 Límites de radio interferencia provocada por instalaciones de alta tensión.**

En la referencia [7], se propone la siguiente recomendación para el límite de campo
electromagnético perturbador de alta frecuencia (radio interferencia) emitida por líneas de
transmisión y subestaciones, según su nivel de tensión:

26

**Tabla 8 Valores de Interferencias de Radio, recomendados por Asociación de**

**Normas Canadienses [7]**

|Voltaje nominal entre fases|Nivel de Radio Interferencia|
|---|---|
|(KV)|[dB/ 1μV/m]|
|Menos de 70|43|
|70 - 200|49|
|200 - 300|53|
|400 - 600|60|
|Sobre 600|63|
|Para líneas de transmisión, valores a 15 m de la fase externa y a 0,5 MHz<br>Para subestaciones, valores indicados a 15 m fuera del borde y a 0,5 MHz|Para líneas de transmisión, valores a 15 m de la fase externa y a 0,5 MHz<br>Para subestaciones, valores indicados a 15 m fuera del borde y a 0,5 MHz|

Para una línea de transmisión o subestación de 220 kV, el valor límite corresponde a 53

[dB/1uV/m].

**13. Conclusiones**

De los resultados obtenidos en la revisión bibliográfica y en las simulaciones efectuadas
para la subestación seccionadora, se concluye:

 **Campo eléctrico**
La información disponible respecto de valores de campo eléctrico medidos en
instalaciones similares de 220 kV, demuestran que los valores medidos en el borde de los
recintos alcanzan magnitudes no superiores a **1.000 [V/m].** En la simulación efectuada
para el caso específico, se determinó **600 [V/m].** Se concluye que en el borde de la
subestación, el campo eléctrico no supera el valor límite recomendado por la normativa
ICNIRP de **5.000 [V/m]** .

 **Campo magnético**
Directamente de la estimación publicada en las referencias, el campo magnético en el
borde de instalaciones similares es **5 [micro Tesla]** . En la simulación efectuada para el
caso específico, se determinó **38,0 [micro Tesla].** Se concluye que en el borde de la
subestación, el campo magnético no supera el valor límite recomendado por la ICNIRP de
**200 [micro Tesla].**

 **Radio interferencia**

De la información bibliográfica recopilada, en el caso de una instalación de 230 kV, el
nivel de radio interferencia generado en el perímetro interior alcanza 50 [dB/ 1uV/m];

27

trasladado este valor a la distancia de 15m exterior a la subestación, se reduce
aproximadamente 4 dB, por lo que para efecto de confrontación con norma, este valor es
**46 [dB/ 1uV/m].** Debido a la proximidad con el borde oriente de la subestación, el mayor
efecto de radio interferencia se debe a las líneas, evaluando a 37 m desde el eje de la
línea Cautín 1, 38,3 [dB/uV/m] y a 15 m hacia el exterior, **35,5 [dB/uV/m].** Este valor no
supera por tanto el límite máximo especificado, correspondiente **a 53 [dB/uV/m]**, 15 m
hacia el exterior de la subestación.

Por su parte, para la línea cuya configuración queda definida por la estructura de remate
E100A, se concluye:

 **Campo eléctrico**
La modelación entregó el valor **550 [V/m]** en el borde de la franja, por lo tanto el campo
eléctrico no supera el valor límite recomendado por la normativa ICNIRP de **5.000 [V/m]** .

 **Campo magnético**
La modelación entregó el valor **0,82 [micro Tesla]** en el borde de la franja, por lo tanto la
inducción magnética no supera el valor límite recomendado por la normativa ICNIRP de
**200 [micro Tesla]** .

 **Radio interferencia**

La radio interferencia calculada para la configuración de conductores alcanza **40,6**

**[dB/uV/m]** a 15 m de la fase externa. Este valor no supera por tanto el límite máximo
especificado, correspondiente **a 53 [dB/uV/m]**, a 15 m de la fase externa y a 0,5 MHz.

**14. Área de influencia**

Considerando los resultados indicados anteriormente, y las distancias establecidas por las
normativas referenciadas, se estima que el área de influencia de la Subestación
Seccionadora Río Toltén 220 kV incluyendo el tramo de seccionamiento de la línea 2x220
kV Ciruelos - Cautín, debido a la componente campos electromagnéticos, se extiende
hasta 20 m hacia afuera, desde el borde de la Subestación y 20 m laterales respecto del
eje de la línea.

_Finalmente, se concluye que la_ _**Subestación seccionadora Río Toltén 220 kV**_ _y el tramo_
_de seccionamiento de la línea 2x220 kV Ciruelos - Cautín, satisfacen las normas de_
_campo electromagnético de baja frecuencia y de radio interferencia._

28

**15. Referencias**

[1] Students' QuickField (TM) Finite Element Analysis System

Version 5.8 User's Guide

Copyright (C) Tera Analysis Company, 2010.

[2] Gary, C.; Moreau, M: "L'effet de couronne en tensión alternative", Eyroller

Collection. Direction des Etudes et Recherches d'Electricité de France (N° 24),

1976

[3] Nelson Morales; Efraín Asenjo; Cristian López:
“Medición de campo eléctrico de frecuencia industrial bajo líneas de transmisión y
en subestaciones”,
Anales V ERLAC (Quinto Encuentro Regional Latino Americano de la Cigré,
Paraguay, mayo 1993)

[4] I.O. Habiballah, M.M. Dawoud, K. Al-Balawi, A.S. Farag
“Magnetic Field Measurement & Simulation of A 230 kV Substation”
Proceedings of the International Conference on Non-Ionizing Radiation at UNITEN
(ICNIR 2003) Electromagnetic Fields and Our Health 20th - 22nd October 2003

[5] CARTER R. T. ; GRILLE A. W. ; BAZILE G. M. ; PERKINS M. D. ; MAUSER S. F. ;

Analysis of radio interference and substation modifications for uprating a 115-KV
substation to 230 KV

IEEE transactions on Power Delivery (IEEE Trans. Power Deliv.) 1987, vol. 2,
n [o] 2, pp. 544-550

[6] International Commission on Non ‐ Ionizing Radiation Protection
ICNIRP Publication - 2010

‐
ICNIRP Guidelines for limiting exposure to time varying electric and magnetic fields
(1 hz - 100 kHz)

‐
Published in: Health Physics 99(6):818 836; 2010

[7] Association canadienne de normalisation, Valeurs limites et methods de mesure du

bruit électromagnétique (0,15 à 30 MHz) produit par les reseaux de courant
alternatif. CAN3- C108.3.1 - M84. Octobre 1984. (Réaffirmé 2009)

29

**16. ANEXO**

Se presenta a continuación los listados de salida del programa LINEAS, que
calcula campo eléctrico superficial en conductores de línea de alta tensión, aplicados a las
estructuras en estudio.

NOTA: El programa utiliza punto decimal (.) en lugar de coma (,). No incluye tilde

de acentos.

**16.1 Campo eléctrico superficial en Barras**

_CAMPO ELECTRICO Y POTENCIAL INDUCIDO EN TORNO A LINEAS DE TRANSMISION_

_Número total de conductores : 6_

_Número de conductores activos : 6_

|Fase|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
|_ Numero de subconductores_|_2 _|_2 _|_2 _|_2 _|_2 _|_2 _|
|_Separacion entre subconductores (cm)_|_20.00_|_20.00_|_20.00_|_20.00_|_20.00_|_20.00_|
|_ Radio del subconductor (cm)_|_2.070_|_2.070_|_2.070_|_2.070_|_2.070_|_2.070_|
|_Ubicacion lateral del conductor (m)_|_-4.00_|_0.00_|_4.00_|_60.00_|_64.00_|_68.00_|
|_ Altura conductor sobre el suelo (m)_|_10.00_|_10.00_|_10.00_|_10.00_|_10.00_|_10.00_|

_FASE -RADIO HAZ (cm) -RADIO COND. EQUIV. (cm)_

_1 10.000 6.434_

_2 10.000 6.434_

_3 10.000 6.434_

_4 10.000 6.434_

_5 10.000 6.434_

_6 10.000 6.434_

_Matriz de coeficientes (amplif. por (2_  _0_ _))_

_5.7393 1.6290 .9905 .0466 .0415 .0372_

_1.6290 5.7393 1.6290 .0527 .0466 .0415_

_.9905 1.6290 5.7393 .0600 .0527 .0466_

_.0466 .0527 .0600 5.7393 1.6290 .9905_

_.0415 .0466 .0527 1.6290 5.7393 1.6290_

_.0372 .0415 .0466 .9905 1.6290 5.7393_

30

_Matriz de capacitancias (amplif. por 1/(2_  _0_ _))_

_.1914 -.0489 -.0191 -.0007 -.0005 -.0005_

_-.0489 .2020 -.0489 -.0007 -.0005 -.0005_

_-.0191 -.0489 .1914 -.0011 -.0007 -.0007_

_-.0007 -.0007 -.0011 .1914 -.0489 -.0191_

_-.0005 -.0005 -.0007 -.0489 .2020 -.0489_

_-.0005 -.0005 -.0007 -.0191 -.0489 .1914_

_Potenciales de conductores ( KVolts)_

_( 127.0170, 0.0000 ) 127.0170_
_( -63.5085, -110.0000 ) 127.0170_
_( -63.5085, 110.0000 ) 127.0170_
_( 127.0170, 0.0000 ) 127.0170_
_( -63.5085, -110.0000 ) 127.0170_
_( -63.5085, 110.0000 ) 127.0170_

_Cargas en conductores (Cb)/(2_  _0_ _)_

_( 28.6094, 3.2723 ) 28.7959_
_( -15.9638, -27.5961 ) 31.8808_
_( -11.5325, 26.4398 ) 28.8455_
_( 28.6638, 3.2325 ) 28.8454_
_( -15.9171, -27.6231 ) 31.8808_
_( -11.4708, 26.4126 ) 28.7959_

_Gradientes superficiales (kVef./cm)_

_( 8.3410, 0.9540 ) 8.3953_
_( -4.6542, -8.0455 ) 9.2947_
_( -3.3622, 7.7084 ) 8.4098_
_( 8.3568, 0.9424 ) 8.4098_
_( -4.6406, -8.0534 ) 9.2947_
_( -3.3443, 7.7005 ) 8.3953_

31

**16.2 Campo eléctrico superficial en Líneas**

_CAMPO ELECTRICO Y POTENCIAL INDUCIDO EN TORNO A LINEAS DE TRANSMISION_

_Numero total de conductores : 6_

_Numero de conductores activos : 6_

|Fase|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
|_ Numero de subconductores_|_1 _|_1 _|_1 _|_1 _|_1 _|_1 _|
|_ Radio del subconductor (cm)_|_2.070_|_2.070_|_2.070_|_2.070_|_2.070_|_2.070_|
|_Ubicacion lateral del conductor (m)_|_-4.00_|_0.00_|_4.00_|_13.20_|_17.20_|_21.20_|
|_ Altura conductor sobre el suelo (m)_|_10.00_|_10.00_|_10.00_|_10.00_|_10.00_|_10.00_|

_Matriz de coeficientes (amplif. por (2_  _0_ _))_

_6.8734 1.6290 .9905 .4277 .3183 .2443_

_1.6290 6.8734 1.6290 .5963 .4277 .3183_

_.9905 1.6290 6.8734 .8725 .5963 .4277_

_.4277 .5963 .8725 6.8734 1.6290 .9905_

_.3183 .4277 .5963 1.6290 6.8734 1.6290_

_.2443 .3183 .4277 .9905 1.6290 6.8734_

_Matriz de capacitancias (amplif. por 1/(2_  _0_ _))_

_.1557 -.0330 -.0137 -.0042 -.0025 -.0019_

_-.0330 .1619 -.0323 -.0067 -.0036 -.0025_

_-.0137 -.0323 .1578 -.0142 -.0067 -.0042_

_-.0042 -.0067 -.0142 .1578 -.0323 -.0137_

_-.0025 -.0036 -.0067 -.0323 .1619 -.0330_

_-.0019 -.0025 -.0042 -.0137 -.0330 .1557_

_Potenciales de conductores ( KVolts)_

_( 127.0170, 0.0000 ) 127.0170_
_( -63.5085, -110.0000 ) 127.0170_
_( -63.5085, 110.0000 ) 127.0170_
_( 127.0170, 0.0000 ) 127.0170_
_( -63.5085, -110.0000 ) 127.0170_
_( -63.5085, 110.0000 ) 127.0170_

32

_Cargas en conductores (Cb)/( 2_  _0_ _)_

_( 22.5030, 2.1849 ) 22.6088_
_( -12.8917, -21.2444 ) 24.8500_
_( -10.8232, 21.1793 ) 23.7845_
_( 23.7534, 1.2165 ) 23.7845_
_( -11.9523, -21.7868 ) 24.8500_
_( -9.3593, 20.5806 ) 22.6088_

_Gradientes superficiales (kVef./cm)_

_( 10.8710, 1.0555 ) 10.9221_
_( -6.2279, -10.2630 ) 12.0048_
_( -5.2286, 10.2316 ) 11.4901_
_( 11.4751, 0.5877 ) 11.4901_
_( -5.7741, -10.5250 ) 12.0048_
_( -4.5214, 9.9423 ) 10.9221_

**16.3 Campo eléctrico superficial en remate de Líneas**

_CAMPO ELECTRICO Y POTENCIAL INDUCIDO EN TORNO A LINEAS DE TRANSMISION_

_Numero total de conductores : 6_

_Numero de conductores activos : 6_

_Numero de cables de guardia : 0_

|Fase|1|2|3|4|5|6|
|---|---|---|---|---|---|---|
|_ Numero de subconductores_|_1 _|_1 _|_1 _|_1 _|_1 _|_1 _|
|_ Radio del subconductor (cm)_|_1.258_|_1.258_|_1.258_|_.258_|_1.258_|_.258_|
|_Ubicacion lateral del conductor (m)_|_-4.00_|_-4.00_|_-4.00_|_4.00_|_4.00_|_4.00_|
|_ Altura conductor sobre el suelo (m)_|<br>_14.00_|_19.00_|_24.00_|_14.00_|_19.00_|_24.00_|

_Matriz de coeficientes (amplif. por (2_  _0_ _))_

_7.7079 1.8871 1.3350 1.2920 1.2807 1.1093_

_1.8871 8.0132 2.1518 1.2807 1.5798 1.5339_

_1.3350 2.1518 8.2468 1.1093 1.5339 1.8055_

_1.2920 1.2807 1.1093 7.7079 1.8871 1.3350_

_1.2807 1.5798 1.5339 1.8871 8.0132 2.1518_

_1.1093 1.5339 1.8055 1.3350 2.1518 8.2468_

33

_Matriz de capacitancias (amplif. por 1/(2_  _0_ _))_

_.1430 -.0249 -.0112 -.0144 -.0105 -.0071_

_-.0249 .1447 -.0271 -.0105 -.0136 -.0124_

_-.0112 -.0271 .1376 -.0071 -.0124 -.0192_

_-.0144 -.0105 -.0071 .1430 -.0249 -.0112_

_-.0105 -.0136 -.0124 -.0249 .1447 -.0271_

_-.0071 -.0124 -.0192 -.0112 -.0271 .1376_

_Potenciales de conductores ( KVolts)_

_( 127.0170, 0.0000 ) 127.0170_
_( -63.5085, -110.0000 ) 127.0170_
_( -63.5085, 110.0000 ) 127.0170_
_( 127.0170, 0.0000 ) 127.0170_
_( -63.5085, -110.0000 ) 127.0170_
_( -63.5085, 110.0000 ) 127.0170_

_Cargas en conductores (Cb)/( 2_  _0_ _)_

_( 19.7376, 1.8879 ) 19.8277_
_( -10.3206, -18.7606 ) 21.4120_
_( -7.3332, 17.3622 ) 18.8474_
_( 19.7376, 1.8879 ) 19.8277_
_( -10.3206, -18.7606 ) 21.4120_
_( -7.3332, 17.3622 ) 18.8474_

_Gradientes superficiales (kVef./cm)_

_( 15.6897, 1.5007 ) 15.7613_
_( -8.2039, -14.9131 ) 17.0207_
_( -5.8293, 13.8015 ) 14.9820_
_( 15.6897, 1.5007 ) 15.7613_
_( -8.2039, -14.9131 ) 17.0207_
_( -5.8293, 13.8015 ) 14.9820_

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 1: Características línea 2x220 kV Ciruelos - Cautín****

| Tensión de operación : | 220 kV |
| --- | --- |
| Número de circuitos : | 2 |
| Número de conductores por fase : | 1 |
| Resistencia a 25oC en conductor : | 0,0904 ohm/km |
| Conductor existente : | ACSR Grosbeak |
| Cable de guardia : | La línea no presenta cable de guardia |
| Capacidad térmica informada | 506 Amperes, calculados a 50oC de temperatura<br>en conductor y 25oC de temperatura ambiente |
| Máxima capacidad | 193 MVA |

**Tabla 2: Sección y tipo de los conductores empleados en seccionamientos****

| Subestación | Tipo | Sección [mm2] |
| --- | --- | --- |
| Barras 220 kV | 2 x AAC COWSLIP | 2 x 1013 |
| Paños de línea 220 kV | 1 x AAC COWSLIP | 1 x 1013 |

**Tabla 3: Sección y tipo de los conductores empleados en subestación****

| Línea | Descripción |
| --- | --- |
| Seccionamiento Línea 2x220 kV Ciruelos - Cautín | 1 conductor por fase |
| Subestación | Descripción |
| Barras 220 kV | 2 conductores por fase |
| Paños de línea 220 kV | 1 conductor por fase |

**Tabla 5: Conjunto Aislación Subestación Seccionadora Río Toltén 220 kV****

| Tipo | Antiniebla (Fog Type) |
| --- | --- |
| Acople | Cuenca y Bola |
| Diámetro de la pollera | 254 mm |
| Espaciamiento nominal | 146 mm |
| Distancia de fuga | 432 mm |
| Carga de ruptura | 70 kN |
| Número de Aisladores | 16 |

**Tabla 6: Valores de campo electromagnético a 1,0 metro sobre el suelo****

| Col1 | Campo eléctrico | Col3 | Inducción magnética | Col5 |
| --- | --- | --- | --- | --- |
|  | Máximo<br> [V/m] | Borde S/E<br>[V/m] | Máximo<br>[micro Tesla] | Borde S/E<br>[micro Tesla] |
| Trayectoria A1 - A2 | 2.100 | 600 | 15,0 | 4,5 |
| Trayectoria B1 - B2 | 2.400 | 250 | 38,0 | 5,8 |

**Tabla 7: Valores de campo electromagnético a 1,0 metro sobre el suelo****

| Col1 | Campo eléctrico | Col3 | Inducción magnética | Col5 |
| --- | --- | --- | --- | --- |
|  | Máximo<br> [V/m] | Borde franja<br>[V/m] | Máximo<br>[micro Tesla] | Borde franja<br>[micro Tesla] |
| Torre E100A | 2.780 | 550 | 3,21 | 0,82 |

**Tabla 8: Valores de Interferencias de Radio, recomendados por Asociación de****

| Voltaje nominal entre fases | Nivel de Radio Interferencia |
| --- | --- |
| (KV) | [dB/ 1μV/m] |
| Menos de 70 | 43 |
| 70 - 200 | 49 |
| 200 - 300 | 53 |
| 400 - 600 | 60 |
| Sobre 600 | 63 |
| Para líneas de transmisión, valores a 15 m de la fase externa y a 0,5 MHz<br>Para subestaciones, valores indicados a 15 m fuera del borde y a 0,5 MHz | Para líneas de transmisión, valores a 15 m de la fase externa y a 0,5 MHz<br>Para subestaciones, valores indicados a 15 m fuera del borde y a 0,5 MHz |
