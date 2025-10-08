---
title: Sin título
author: Camilo Wetland
date: D:20200113102846-03'00'
language: es
type: general
pages: 16
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Base de Cálculos y criterios de diseño Planta de tratamiento de residuos industriales líquidos Estación de transferencia Gersa - Lautaro
-->

# Base de Cálculos y criterios de diseño Planta de tratamiento de residuos industriales líquidos Estación de transferencia Gersa - Lautaro

1

**ÍNDICE**

1. Antecedentes ............................................................................................................... 3

2. Descripción y cálculo................................................................................................... 4

2.1. Tamiz fino de tornillo .............................................................................................. 4

2.2. Cámara desgrasadora ......................................................................................... 4

2.3. Filtro de coalescencia (Separador de Hidrocarburos) .................................... 5

2.4. Estanque de neutralización ................................................................................. 6

2.5. Reactor SBR ............................................................................................................ 6

2.5.1. Dimensiones: inventario de lodo ................................................................. 7

2.5.2. Dimensiones: volumen de tratamiento ....................................................... 9

2.5.3. Aireación ......................................................................................................... 9

2.5.4. Lodo biológico ............................................................................................. 10

3. Eficiencias de remoción ............................................................................................ 11

4. Balance de masa ....................................................................................................... 11

4.1. Escenario 1: Parámetros de diseño .................................................................. 11

4.2. Escenario 2: Análisis fisicoquímico 2 de diciembre 2018 ............................... 13

4.3. RESUMEN ............................................................................................................... 15

5. Bibliografía ................................................................................................................... 16

Miraflores 222 piso 28, Santiago, Chile. Fono 56-2-2047174

wetland@wetland.cl

www.wetland.cl

2

**1.** **ANTECEDENTES**

En la estación de transferencia de Gersa ubicada en Lautaro, se construyó una
planta de tratamiento para los residuos industriales líquidos derivados del manejo
de residuos sólidos y lavado de equipos. Esta planta debe cumplir con los
parámetros indicados en el Decreto Supremo N°609/98 tabla 4.

<!-- INICIO TABLA 4 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- **3.** **EFICIENCIAS DE REMOCIÓN** Revisitando la Tabla 2, esta se detalla con el porcentaje de remoción estimado de cada parámetro en las distintas unidades -->

**Tabla 4: Eficiencias** **de** **cada** **etapa** **en la** **planta** **de tratamiento** **de RILES.****

| Parámetro | Cámara desgrasadora | Filtro<br>coalescente | Estanque de<br>neutralización | Reactor SBR |
| --- | --- | --- | --- | --- |
| **DBO5 ** | 20% | S/I | - | 98% |
| **Fósforo** | - | - | - | <br>⁄<br> <br> |
| **NTK** | - | - | - | <br> <br>⁄<br> |
| **pH** | - | - | Neutralización | - |
| **SST** | 20% | S/I | - | 90% |
| **AyG** | 50% | 80% | - | 70% |
| **HC** | 50% | 80% | - | - |

<!-- Estadísticas: 7 filas, 5 columnas -->
<!-- Contexto posterior: -->
<!-- **4.** **BALANCE DE MASA** A continuación, se mostrarán los balances de masa obtenidos para distintos escenarios de diseño y reales. -->
<!-- FIN TABLA 4 -->


La planta fue diseñada para funcionar bajo los siguientes parámetros en el
afluente:

**Tabla 1:** **Caracterización del RIL de la** **estación de transferencia Lautaro.**

<!-- INICIO TABLA 1 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- parámetros indicados en el Decreto Supremo N°609/98 tabla 4. La planta fue diseñada para funcionar bajo los siguientes parámetros en el afluente: -->

**Tabla 1: ** **Caracterización del RIL de la** **estación de transferencia Lautaro.****

| Parámetro | Unidad | Condición de diseño |
| --- | --- | --- |
| **Caudal medio** | m3/día | 10 |
| **Caudal****_peak_ ** | m3/día | 20 |
| **DBO5 ** | mg/L | 8000 |
| **Fósforo** | mg/L | 50 |
| **Nitrógeno total Kjeldahl (NTK)** | mg/L | 200 |
| **pH** | - | 4,7 - 8,5 |
| **Sólidos suspendidos totales (SST)** | mg/L | 660 |

<!-- Estadísticas: 7 filas, 3 columnas -->
<!-- Contexto posterior: -->
<!-- Para esto, la planta cuenta con cinco etapas distintas, las cuales fueron construidas para abatir distintos parámetros según la Tabla 2. Además se incluyen otros contaminantes relevantes para el tipo de RIL a tratar. -->
<!-- FIN TABLA 1 -->


|Parámetro|Unidad|Condición de diseño|
|---|---|---|
|**Caudal medio**|m3/día|10|
|**Caudal****_peak_ **|m3/día|20|
|**DBO5 **|mg/L|8000|
|**Fósforo**|mg/L|50|
|**Nitrógeno total Kjeldahl (NTK)**|mg/L|200|
|**pH**|-|4,7 - 8,5|
|**Sólidos suspendidos totales (SST)**|mg/L|660|

Para esto, la planta cuenta con cinco etapas distintas, las cuales fueron
construidas para abatir distintos parámetros según la Tabla 2. Además se incluyen

<!-- INICIO TABLA 2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Para esto, la planta cuenta con cinco etapas distintas, las cuales fueron construidas para abatir distintos parámetros según la Tabla 2. Además se incluyen otros contaminantes relevantes para el tipo de RIL a tratar. -->

**Tabla 2: Remoción de contaminantes en las etapas de la planta,** ✔ **indica que la etapa permite****

| tratar el contaminante | Col2 | Col3 | Col4 | Col5 | Col6 |
| --- | --- | --- | --- | --- | --- |
| **Parámetro** | **Tamiz e**<br>**impulsiones** | **Cámara**<br>**desgrasadora** | **Filtro**<br>**coalescente** | **Estanque de**<br>**neutralización** | **Reactor**<br>**SBR** |
| **DBO5 ** | - | ✔ | ✔ | - | ✔ |
| **Fósforo** | - | - | - | - | ✔ |
| **NTK** | - | - | - | - | ✔ |
| **pH** | - | - | - | ✔ |  |
| **SST** | - | ✔ | ✔ | - | ✔ |
| **Aceites y grasas** | - | ✔ | ✔ | - | ✔ |
| **Hidrocarburos** | - | ✔ | ✔ | - | ✔ |

<!-- Estadísticas: 8 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- A continuación, se presentan las tecnologías utilizadas, su principio de funcionamiento, cálculos o criterios de diseño, eficiencias esperadas y flujos de masa. -->
<!-- FIN TABLA 2 -->

otros contaminantes relevantes para el tipo de RIL a tratar.

**Tabla 2: Remoción de contaminantes en las etapas de la planta,** ✔ **indica que la etapa permite**

|tratar el contaminante|Col2|Col3|Col4|Col5|Col6|
|---|---|---|---|---|---|
|**Parámetro**|**Tamiz e**<br>**impulsiones**|**Cámara**<br>**desgrasadora**|**Filtro**<br>**coalescente**|**Estanque de**<br>**neutralización**|**Reactor**<br>**SBR**|
|**DBO5 **|-|✔|✔|-|✔|
|**Fósforo**|-|-|-|-|✔|
|**NTK**|-|-|-|-|✔|
|**pH**|-|-|-|✔||
|**SST**|-|✔|✔|-|✔|
|**Aceites y grasas**|-|✔|✔|-|✔|
|**Hidrocarburos**|-|✔|✔|-|✔|

A continuación, se presentan las tecnologías utilizadas, su principio de
funcionamiento, cálculos o criterios de diseño, eficiencias esperadas y
flujos de masa.

Miraflores 222 piso 28, Santiago, Chile. Fono 56-2-2047174

wetland@wetland.cl

www.wetland.cl

3

**2.** **DESCRIPCIÓN Y CÁLCULO**

**2.1.** **Tamiz fino de tornillo**

La primera unidad de tratamiento de la planta de RILES considera un tamiz fino de
tornillo con paso de sólidos de 2 mm marca SETF, modelo FCP/V. Para términos de
cálculo y balance de masa, no se considera remoción de los contaminantes
indicados en la Tabla 1, ya que su función es evitar que ingresen sólidos de gran
tamaño y la eficiencia de remoción dependerá del tipo de sólidos.

Los elementos removidos son dispuestos como residuos sólidos, con una reducción
de volumen cercana a 40% gracias a la compactación y deshidratación que se
lleva a cabo en el tornillo sinfín.

**2.2.** **Cámara desgrasadora**

La planta cuenta con una cámara desgrasadora de cuatro cuerpos la cual
permite la retención de sólidos sedimentables en la parte inferior del estanque y
las grasas, aceites e hidrocarburos en la zona superior del estanque. Los residuos
acumulados, en la superficie y en el fondo del estanque, deben retirarse por
medio de camión limpiafosa según la capacidad máxima de la cámara.

El principio de funcionamiento de esta unidad consiste en la separación
gravitacional de los sólidos sedimentables y la flotación de grasa y aceites por
diferencias de densidad. Las bases de diseño son variables dependiendo de la
caracterización del agua, por lo cual su dimensionamiento se basa en criterios
recomendados y ampliamente aceptados (American Petroleum Institue, 1990; US
Army Corps of Engineers, 2010)

 Tiempo de retención hidráulico (TRH) mínimo = 30 min

 - Velocidad horizontal (v h ) máxima = 0,9114 m/min

 - Profundidad útil = 0,9 mts a 2,4 mts

 Largo/ancho = 3 a 5

Las dimensiones de la cámara son:

 - Ancho: 1,4 mts

 - Profundidad útil :1,55 mts

 Largo: 4,7 mts

 - Volumen: 10,2 m [3]

 - Área transversal: 2,17 m [2]

Miraflores 222 piso 28, Santiago, Chile. Fono 56-2-2047174

wetland@wetland.cl

www.wetland.cl

4

La comparativa entre los criterios de diseño y el sistema construido se observan en
la Tabla 3.

**Tabla** **3:** **Criterios** **de** **diseño** **de** **un separador convencional aceites,** **grasas** **e hidrocarburos.**

|Criterio|Sugerido|Diseñado|
|---|---|---|
|**TRH**|>30 min|1 hora|
|**vh **|<0,9114 m/min|0,003 m/min|
|**Profundidad util**|0,9 m - 2,4 m|1,55 m|
|**Largo / Ancho**|3 a 5|3,3|

En general las remociones generadas en este tipo de sistemas, va a depender del
tipo agua residual que trata. Las eficiencias de remoción para separadores de
aceites, fosas sépticas o similares son de 50% o mayores para aceites y grasas,
remoción de DBO 5 cercana al 30% y remoción de sólidos suspendidos totales 25%.
(Lopez, 2004; Odiete & Agunwamba, 2016).

Se considerarán las siguientes eficiencias de remoción:

 Aceites y grasas: 50%

 - Hidrocarburos: 50%

 - DBO 5 : 20%

 - SST: 20%

**2.3.** **Filtro de coalescencia (Separador de Hidrocarburos)**

La función de un filtro coalescente consiste en la separación líquido - líquido, en
particular cuando existen emulsiones estables de aceite e hidrocarburos, su
diseño se basa en información empírica que varía según el material del filtro y de
su estructura.

El principal contaminante removido con este equipo son las grasas, aceites e
hidrocarburos emulsionados, también permite el tratamiento de sólidos
suspendidos y carga orgánica, estos últimos no serán considerados ya que la
información existente no es aplicable al residuo líquido a tratar. Se considerará
que las eficiencias en remoción de aceites, grasas e hidrocarburos, son cercanas
a 80% (Zhao & Li, 2011)

Miraflores 222 piso 28, Santiago, Chile. Fono 56-2-2047174

wetland@wetland.cl

www.wetland.cl

5

**2.4.** **Estanque de neutralización**

El efluente del filtro coalescente es descargado hacia un estanque de
homogeneización y neutralización. Esta unidad está equipada con un sensor de
pH y temperatura, el sensor está conectado a un controlador el cual dosifica
soda caustica (NaOH), en caso de necesidad, para alcanzar pH circumneutral.

Además, el estanque está equipado con un agitador mecánico que permite la
homogeneización y mezcla completa.

Finalmente, el estanque cumple la función de cámara de impulsión hacia el
reactor biológico y es controlada de acuerdo a los ciclos del reactor SBR.

**2.5.** **Reactor SBR**

El reactor SBR (Sequencing Batch Reactor), como su nombre lo indica, opera en
modalidad _batch_ (por lotes). Por lo que para cada lote se deberán realizar las
siguientes etapas:

 Carga

 - Reacción

 - Sedimentación

 - Evacuación de clarificado

 Purga de Lodos

Miraflores 222 piso 28, Santiago, Chile. Fono 56-2-2047174

wetland@wetland.cl

www.wetland.cl

6

Como parte de este tipo de sistemas de tratamiento de aguas, se debe
mantener una relación F/M adecuada durante la etapa de reacción. Debido a
las altas concentraciones de carga orgánica, se considera adecuada una
relación F/M de alrededor de 0,3 kgDBO 5 /kgMLVSS*d. Además, esto permitirá que,
ante disminuciones de carga orgánica, se puedan mantener los reactores
trabajando en rangos óptimos de edad de lodo.

El reactor por dimensionar contempla un ciclo diario de 24 horas, con un
tiempo de descarga menor o igual a 1 hora, dependiendo del caudal que haya
ingresado durante ese ciclo al reactor. El reactor calculado tienen medidas de
4,6 m por lado y 6 m de altura construido en hormigón.

2.5.1. Dimensiones: inventario de lodo

Se consideran los siguientes supuestos para el dimensionamiento de los reactores

 La carga orgánica se distribuye uniforme entre ambos reactores.

Miraflores 222 piso 28, Santiago, Chile. Fono 56-2-2047174

wetland@wetland.cl

www.wetland.cl

7

 Se utilizará un F/M de 0,3 kg

 Se considera un IVL de 100 ml/g

 La concentración de solidos suspendidos volátiles a mantener en el reactor
a nivel mínimo es de 4000 mg/L (4 Kg/m [3] )

La carga orgánica a degradar se obtiene a partir de la concentración de
DBO 5 y el caudal, como se muestra a continuación:

Para el dimensionamiento de los reactores, se supondrá que ingresan 80

por reactor al día. Para el reactor se calcula la cantidad de Sólidos

Suspendidos Volátiles del Licor Mezcla (M):

Considerando un IVL esperado de 100 L/kgSSVLM, se obtiene un volumen
de lodos (V lodo ) de:

El área del estanque a utilizar como reactor es de 21,16 m [2 ] se obtiene una
altura de lodos (h lodo ) de:

Considerando una concentración de Sólidos Suspendidos Volátiles en el
licor mezcla de 4 kg/m [3] se tiene que el volumen del reactor a nivel mínimo (V min )
será:

Lo que equivale a una altura a nivel mínimo (h min ) de:

Miraflores 222 piso 28, Santiago, Chile. Fono 56-2-2047174

wetland@wetland.cl

www.wetland.cl

8

El reactor realizará su descarga de clarificado hasta un nivel de 3,2 m.

2.5.2. Dimensiones: volumen de tratamiento

Se espera un caudal medio aproximado de 10 m [3] a recibir en cada ciclo
(un día), lo que se traduce en una diferencia de altura a caudal medio ( ∆ h Q ) de:

Para caudales _peak_ de 20 m [3] /día se requiere una altura aproximada de 1
m. Considerando la altura mínima para inventario de lodo y altura por caudal, se
requiere un reactor de 4,3 m [3] /h

Debido a la dificultad en la caracterización de los RILES de los lixiviados
generados en una estación de transferencia, se adiciona un metro en el diseño
en caso de aumento de la carga orgánica o caudal que ingresa al sistema.
Además, se considera 0,7 metros de altura libre.

2.5.3. Aireación

Respecto de la aireación, para el cálculo de aire se considera una
ecuación simplificada que permite asegurar con holgura un caudal de aire
suficiente para RILES de características variables.

Se considera que los microorganismos tienen metabolismo heterótrofo
aerobio y por la baja edad del lodo (cercana a 3 días) existen microorganismos
nitrificantes o denitrificantes.

Este valor llevado a S.O.T.R. es de 130 kg O 2 /día. Si se consideran 17 horas de
aireación, lo que incluye periodos de anoxia para control del proceso, se requiere
suministrar 138 m [3] /h (no se considera factor de seguridad). El proyecto considera
dos sopladores de 140 m [3 ] para asegurar un respaldo en caso de fallas y aumentar
la cantidad de oxígeno en caso de ser necesario.

Se considera una eficiencia de al menos un 98% en la reducción de la carga
orgánica, mientras que los nutrientes son calculados por la razón C:N:P (100:5:1),
la cual asegura los nutrientes mínimos para el crecimiento celular. Con esto se

Miraflores 222 piso 28, Santiago, Chile. Fono 56-2-2047174

wetland@wetland.cl

www.wetland.cl

9

estiman las remociones de nutrientes según las siguientes ecuaciones, con X igual
a la masa en Kg de DBO 5 removida en el tratamiento:

Adicionalmente, se debe tener una tasa de carga de aceites y grasa a
microorganismos menor a 0,002 [Kg Aceites y grasas] / Kg SSVLM para evitar la inhibición del
metabolismo del lodo biológico (Chipasa & M ȩ drzycka, 2006). Dentro de un
reactor se pueden lograr remociones variables según el tipo de aceites, grasas e
hidrocarburos que ingresen al sistema entre. Para este proyecto se considera una
eficiencia de remoción baja de 70% dada la variabilidad del RIL

Por último, los sólidos suspendidos presentes componen gran parte de la DBO 5, los
cuales se degradan, los que no son degradados son arrastrados por el lodo
biológico durante la etapa de sedimentación, para esto se estima una eficiencia
de 90% de eficiencia de remoción de SST en esta etapa.

2.5.4. Lodo biológico

La generación de lodos dependerá de la masa que ingresa al sistema
diariamente, por la baja edad del lodo se asume una razón de 1 Kg DBO 5 /día ≈ 1
Kg SSVLM/día.

Se debe mantener una medición constante de sólidos suspendidos volátiles, o
estimarlos indirectamente por la medición de SST, para mantener una masa de
biología en el reactor de 270 Kg SSVLM.

Para régimen estacionario de funcionamiento según los parámetros de diseño,
asumiendo una concentración de lodo sedimentado de 10 Kg/m [3], se deberá
retirar lodo desde el fondo del reactor sedimentado, considerando volumen de 8
m [3 ] de lodo diario a régimen estacionario según los parámetros de diseño. Más
adelante se muestran escenarios reales de operación, en los cuales la carga
orgánica es mucho menor, permitiendo trabajar con edades del lodo mas altas y
reduciendo el volumen de lodo retirado diariamente, incluso sin necesidad de
sedimentación.

Durante la operación de la planta, este volumen será menor ya que los análisis
del afluente indican concentraciones de DBO 5 mucho menores a 8.000 mg
DBO 5 /L lo cual permitirá operar con razones F/M menores, aumentando la edad

Miraflores 222 piso 28, Santiago, Chile. Fono 56-2-2047174

wetland@wetland.cl

www.wetland.cl

10

del lodo y reduciendo la masa de lodo generada. Más adelante se presentan
ejemplos de operación en base a parámetros reales.

**3.** **EFICIENCIAS DE REMOCIÓN**

Revisitando la Tabla 2, esta se detalla con el porcentaje de remoción estimado de
cada parámetro en las distintas unidades

**Tabla 4: Eficiencias** **de** **cada** **etapa** **en la** **planta** **de tratamiento** **de RILES.**

|Parámetro|Cámara desgrasadora|Filtro<br>coalescente|Estanque de<br>neutralización|Reactor SBR|
|---|---|---|---|---|
|**DBO5 **|20%|S/I|-|98%|
|**Fósforo**|-|-|-|<br>⁄<br> <br>|
|**NTK**|-|-|-|<br> <br>⁄<br>|
|**pH**|-|-|Neutralización|-|
|**SST**|20%|S/I|-|90%|
|**AyG**|50%|80%|-|70%|
|**HC**|50%|80%|-|-|

**4.** **BALANCE DE MASA**

A continuación, se mostrarán los balances de masa obtenidos para distintos
escenarios de diseño y reales.

**4.1.** **Escenario 1: Parámetros de diseño**

Utilizando los parámetros de diseño, y un caudal de 10 m [3] /día, se obtiene el
escenario presentado en la Tabla 5.

Bajo este funcionamiento se deben tener las siguientes consideraciones:

 Adicionar fósforo y nitrógeno hasta alcanzar los requerimientos para el
correcto funcionamiento del reactor biológico

 - Se tiene una relación F/M en el reactor de 0,23 [kg DBO5] / kg SSVLM

 - Se cumple la relación [Kg Aceites y grasas] / Kg SSVLM menor a 0,04.

 Con el lodo sedimentado en el reactor biológico con una concentración
de 10 Kg/m [3] se debe retirar diariamente 6,4 m [3] de lodo.

En estas condiciones de operación se alcanzan las concentraciones requeridas
en todos los parámetros controlados.

Miraflores 222 piso 28, Santiago, Chile. Fono 56-2-2047174

wetland@wetland.cl

www.wetland.cl

11

**Tabla** **5: Balance** **de masa** **para** **escenario 1.**

|Línea de agua|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|Col12|
|---|---|---|---|---|---|---|---|---|---|---|---|
||||||Cámara desgrasadora|Cámara desgrasadora|Filtro coalescente|Filtro coalescente|Filtro coalescente|Filtro coalescente||
|**Parámetro**|Unidad|Concentración (mg/L)|Concentración (mg/L)|Masa<br>(Kg/día)|Eficiencia<br>%|Masa (Kg/día)|Eficiencia<br>%|Masa (Kg/día)|Eficiencia<br>%|Masa (Kg/día)|**Concentración efluente**<br>**(mg/L)**|
|**DBO5 **|<br>mg/L|8000|8000|80,00|20%|64,00|0%|64,00|98%|1,28|**128**|
|**Fósforo**|mg/L|50|50|0,50|0%|0,50|0%|0,50|0%|-|**<10**|
|**NTK**|mg<br>N-<br>NH4+/L|200|200|2,00|0%|2,00|0%|2,00|0%|-|**<80**|
|**SST**|mg/L|660|660|6,60|20%|5,28|0%|5,28|90%|0,53|**52,8**|
|**AyG**|mg/L|0|0|0,00|50%|0,00|80%|0,00|70%|0,00|**0 **|
|**HC**|mg/L|0|0|0,00|50%|0,00|80%|0,00|0%|0,00|**0 **|
|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|
||||||Cámara desgrasadora|Cámara desgrasadora|Filtro coalescente|Filtro coalescente|Filtro coalescente|Filtro coalescente||
||||Parámetr<br>o|Unidad|Eficiencia<br>%|Masa lodo<br>(Kg/día)|Eficiencia<br>%|Masa lodo<br>(Kg/día)|Eficiencia<br>%|Masa lodo<br>(Kg/día)|**Total masa lodo (Kg/día)**|
||||Fósforo|mg/L|0%|0,00|0%|0,00|0%|0,63|**0,63**|
||||NTK|mg N- NH4+/L|0%|0,00|0%|0,00|0%|3,14|**3,14**|
||||SST|mg/L|20%|1,32|0%|0,00|90%|64,00|**65,32**|
||||AyG|mg/L|50%|0,00|80%|0,00|70%|0,00|**0 **|
||||HC|mg/L|50%|0,00|80%|0,00|0%|0,00|**0 **|

12

**4.2.** **Escenario 2: Análisis fisicoquímico 2 de diciembre 2018**

Utilizando los parámetros medidos en las muestras del día 2 de diciembre de 2018,
y un caudal de 10 m [3] /día, se obtiene el balance de masa presentado en la Tabla
6.

Bajo este funcionamiento se deben tener las siguientes consideraciones:

 Adicionar fósforo y nitrógeno hasta alcanzar los requerimientos para el
correcto funcionamiento del reactor biológico

 - Se tiene una relación F/M en el reactor de 0,015 [kg DBO5] / kg SSVLM, se debe
aumentar esta relación a menos a un 0,05 para mantener una edad del
lodo adecuada (aproximadamente 28 días).

 Si esta composición es estable en el tiempo, se deben modificar por
programa los volúmenes de operación mínimos del reactor. Para una
concentración de SSVLM de 2 Kg/m [3] se tiene una altura mínima de 2 m

 Bajo estas condiciones se facilita la remoción de lodos, debiendo retirarse
1,5 m [3] de lodo directamente del reactor a nivel mínimo.

 - Se cumple la relación [Kg Aceites y grasas] / Kg SSVLM menor a 0,04
A una densidad de grasas, aceites e hidrocarburos de 800 kg/m [3] se retiene un
volumen diario de en el separador 0,4 Lts y 0,32 Lts en el filtro coalescente

13

**Tabla** **6: Balance** **de masa** **para** **escenario 2.**

|Línea de agua|Col2|Col3|Col4|Col5|Col6|Col7|Col8|Col9|Col10|Col11|
|---|---|---|---|---|---|---|---|---|---|---|
|||||Cámara desgrasadora|Cámara desgrasadora|Filtro coalescente|Filtro coalescente|Reactor SBR|Reactor SBR||
|**Parámetro**|Unidad|Concentración<br>(mg/L)|Masa<br>(Kg/día)|Eficiencia<br>%|Masa (Kg/día)|Eficiencia<br>%|Masa (Kg/día)|Eficiencia<br>%|Masa (Kg/día)|**Concentración efluente**|
|**DBO5 **|<br>mg/L|516|5,16|20%|4,13|0%|4,13|98%|0,08|**8,26**|
|**Fósforo**|mg/L|3,63|0,0363|0%|0,04|0%|0,04|0%|-|**<10**|
|**NTK**|mg N- NH4+/L|4,95|0,0495|0%|0,05|0%|0,05|0%|-|**<80**|
|**SST**|mg/L|660|6,6|20%|5,28|0%|5,28|90%|0,53|**52,80**|
|**AyG**|mg/L|43|0,43|50%|0,22|80%|0,04|70%|0,01|**1,29**|
|**HC**|mg/L|21|0,21|50%|0,11|80%|0,02|0%|0,02|**2,10**|
|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|**Línea de lodo**|
|||||Cámara desgrasadora|Cámara desgrasadora|Filtro coalescente|Filtro coalescente|Reactor SBR|Reactor SBR||
|||Parámetro|Unidad|Eficiencia<br>%|Masa lodo<br>(Kg/día)|Eficiencia<br>%|Masa lodo<br>(Kg/día)|Eficiencia<br>%|Masa lodo<br>(Kg/día)|**Total masa**<br>**lodo(Kg/día)**|
|||Fósforo|mg/L|0%|0,00|0%|0,00|0%|0,04|**0,04**|
|||NTK|mg N- NH4+/L|0%|0,00|0%|0,00|0%|0,20|**0,20**|
|||SST|mg/L|20%|1,32|0%|0,00|90%|4,13|**5,45**|
|||AyG|mg/L|50%|0,22|80%|0,17|70%|0,05|**0,44**|
|||HC|mg/L|50%|0,11|80%|0,08|0%|0,08|**0,27**|

14

**4.3.** **RESUMEN**

Se espera que la planta de tratamiento de RILES generados en la estación de
transferencia de Gersa en Lautaro cumpla con los parámetros fisicoquímicos. Las
primeras unidades (separador y filtro coalescente) junto con la unidad de
neutralización, se enfocan en el tratamiento primario y acondicionamiento para
un correcto funcionamiento del reactor biológico.

El reactor biológico permite abatir principalmente carga orgánica y nutrientes,
pero su correcta operación permitirá que la biología se adapte a las condiciones
de altas concentraciones de aceites, grasas e hidrocarburos, lo cual permitirá
mejorar las eficiencias de tratamiento de estos contaminantes.

El volumen de diseño del reactor biológico permite versatilidad para la
variabilidad de la carga orgánica y caudal que ingresa a la planta. Se debe
tener especial atención en mantener los requisitos de nutrientes que requiere el
sistema y mantener el control de lodo según las especificaciones de diseño o
modificarlo si se requiere según lo mostrado en el escenario 2.

15

**5.** **BIBLIOGRAFÍA**

American Petroleum Institue. (1990). _Monographs on Refinery Environmental_

_Control- Management of Water Discharges_ .
Bologo, V., Maree, J. P., & Carlsson, F. (2012). Application of magnesium hydroxide

and barium hydroxide for the removal of metals and sulphate from mine
water. _Water SA_, _38_ (1), 23-28. https://doi.org/10.4314/wsa.v38i1.4
Chipasa, K. B., & M ȩ drzycka, K. (2006). Behavior of lipids in biological wastewater

treatment processes. _Journal of Industrial Microbiology and Biotechnology_,
_33_ (8), 635-645. https://doi.org/10.1007/s10295-006-0099-y
Hlabela, P., Maree, J., & Bruinsma, D. (2007). Barium carbonate process for

sulphate and metal removal from mine water. _Mine Water and the_
_Environment_, _26_ (1), 14-22. https://doi.org/10.1007/s10230-007-0145-7
Lopez, C. (2004). Improvement of a Gravity Oil Separator Using a Designed

Experiment. _Water Air and Soil Pollution_, _157_, 31-39. https://doi.org/10.1023/B
Mulopo, J., Mashego, S. R. M. M. R., & Moalusi, M. (2009). Sulphate Removal Results

Using Barium-Carbonate and Their Analysis for Reactor Synthesis. _Forestry_,
_October_, 472-476.
Odiete, W. E., & Agunwamba, J. C. (2016). Effect Of Aspect Ratio On The Oil

Separation Efficiency Of Conventional Oil/Water Separators. _International_
_Journal of Scientific & Engineering Research_, _7_ (3), 840-847.
US Army Corps of Engineers. (2010). _AED Design Requirements: Oil/Water_

_Separators_ . _January_ .
Xiao, F., Zhang, B., & Lee, C. (2008). Effects of low temperature on aluminum(III)

hydrolysis: Theoretical and experimental studies. _Journal of Environmental_
_Sciences_, _20_ (8), 907-914. https://doi.org/10.1016/S1001-0742(08)62185-3
Zhao, H., & Li, G. (2011). Application of fibrous coalescer in the treatment of oily

wastewater. _Procedia_ _Environmental_ _Sciences_, _10_ (PART A), 158-162.
https://doi.org/10.1016/j.proenv.2011.09.028

Miraflores 222 piso 28, Santiago, Chile. Fono 56-2-2047174

wetland@wetland.cl

www.wetland.cl

16