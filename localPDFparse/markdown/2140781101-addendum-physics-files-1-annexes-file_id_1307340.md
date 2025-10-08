---
title: ANEXO 13_AD1_ROSAL
author: Belén Silvestre Adelantado
date: D:20181120134431-03'00'
language: es
type: report
pages: 8
has_toc: False
has_tables: True
extraction_quality: high
---

|Col1|ADENDA 1<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA EL ROSAL|Col3|Col4|
|---|---|---|---|
||ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|
||NOVIEMBRE 2018|Rev.: 0|Rev.: 0|

**ÍNDICE DE CONTENIDOS**

1.1 INTRODUCCIÓN ........................................................................................................................................................... 3

1.2 INPUTS DE ENTRADAS EN EL SIMULADOR SCREEN VIEW. ............................................................................................ 3
1.3 ANÁLISIS DE LOS RESULTADOS .................................................................................................................................... 8

**ÍNDICE DE TABLAS**

T ABLA 1: D ATOS INTRODUCIDOS PARA HACER LA SIMULACIÓN **,** ETAPA DE CONSTRUCCIÓN . ...................................................................... 4

T ABLA 2: D ATOS INTRODUCIDOS PARA HACER LA SIMULACIÓN, ETAPA DE OPERACIÓN . ............................................................................ 6

**ÍNDICE DE ILUSTRACIONES**

I LUSTRACIÓN 1: P ARÁMETROS DE ENTRADA A LA SIMULACIÓN PARA EL PROYECTO . V IENTOS .................................................................... 5

I LUSTRACIÓN 2: TRÁFICO DE RESULTADOS DE LA SIMULACIÓN CON “S CREENVIEW AIR DISPERSION ”, ETAPA DE CONSTRUCCIÓN . ...................... 5
I LUSTRACIÓN 3: TRÁFICO DE RESULTADOS DE LA SIMULACIÓN CON “S CREENVIEW AIR DISPERSION ”, ETAPA DE O PERACIÓN . ........................... 7

Anexo 13: SIMULACIÓN AIR DISPERSION CON SREEN VIEW Página **2** de 8

|Col1|ADENDA 1<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA EL ROSAL|Col3|Col4|
|---|---|---|---|
||ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|
||NOVIEMBRE 2018|Rev.: 0|Rev.: 0|

**1.** **Introducción**

El objetivo del presente informe es detallar el resultado de la simulación realizada con el software

especializado “Screen View-Screening Air Dispersion Model” con el propósito de determinar el alcance de las

concentraciones de partículas de MP10 y MP 2,5 desde el área donde se realizará la instalación del proyecto

fotovoltaico “Central Solar Fotovoltaica El Rosal” y de esta manera, determinar la potencial influencia de las

emisiones atmosféricas del proyecto en relación a la calidad del aire en su entorno más cercano.

**1.1** **Inputs de entradas en el simulador screen view.**

A continuación, se describe los pasos que se han llevado a cabo, para realizar la simulación, en el software

“Screen View-Screening Air Dispersion Model”:

En primer lugar, se ha introducido en el Screen View, los parámetros de entrada correspondientes al proyecto

fotovoltaico. De forma más concreta, se ha seleccionado en el primer apartado, concretamente en el punto
“SourceType” la información de entrada tipo “Área”. En ella a su vez se define los campos de entradas que se

describe a continuación:

**1)EmissionRate,** Índice de emisión, en gr/s/m [2]

**2) SourceReleaseHeight**, Altura en dónde se produce las emisiones atmosféricas, en metros.
**3) LargerSideLenght of Rectangular Área**, Longitud mayor del área del Proyecto, en metros.
**4) SmallerSideLength of Rectangular Área**, Longitud menor del área del Proyecto, en metros.

**5) WindDirectionRelative to Long Dimension**, Dirección relativa del viento en el área del proyecto, en grados.

PRIMER AÑO

Durante la etapa de construcción se emitirá 1,89 toneladas de MP10 durante los 4 meses de duración de esta.
Convirtiendo el valor de 1,89 toneladas a g/s/m [2], teniendo en cuenta las características de la etapa de

construcción en cuanto a su período de tiempo se refiere y a su vez su distribución a lo largo de la superficie
intervenida del proyecto (12,7 ha), se obtiene el valor introducido en la celda de cálculo, igual a 3,76·10 [-6 ]

g/s/m [2] de emisión.

En el segundo campo a rellenar, “SourceReleaseHeight (H)”, hace referencia a la altura de la fuente de emisión,

en este caso, las emisiones se originan por movimientos de tierra, levantamiento de material, combustión de

motores, por lo tanto, la altura de la fuente es más bien a nivel de suelo, es decir a una altura “Cero”, ya que se

encuentran en el mismo nivel que los receptores más próximos.

En la tercera y cuarta celda a rellenar, se introduce los valores del largo y del ancho respectivamente del

proyecto, asemejándolo a un área rectangular, cuya forma geométrica es parecida a dicho polígono. Siendo

estos valores de 702 metros para la longitud mayor y 241 metros para la longitud menor.

En la última celda o campo, se ha definido el valor promedio de la dirección del viento en la ubicación del

proyecto. Para determinar dicho valor, se ha acudido a los valores de direcciones del viento en el último año,

facilitados por la fuente “Recurso Eólico” del Ministerio de Energía del Gobierno de Chile, el cual describe como

información de una dirección ligeramente predominante de los vientos provenientes del suroeste,

concretamente a 210 grados.

Anexo 13: SIMULACIÓN AIR DISPERSION CON SREEN VIEW Página **3** de 8

|Col1|ADENDA 1<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA EL ROSAL|Col3|Col4|
|---|---|---|---|
||ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|
||NOVIEMBRE 2018|Rev.: 0|Rev.: 0|

Sabiendo el origen de todos los datos introducidos en la primera parte del simulador ScreenView, pasamos a

recopilar dichos inputs en la siguiente tabla:

**Tabla** _**1**_ **: Datos introducidos para hacer la simulación, etapa de construcción.**

|Col1|CAMPOS A RELLENAR|VALORES|UNIDADES|
|---|---|---|---|
|1|EmissionRate.|3,76·10-6|gr/s/m2|
|2|SourceReleaseHeight.|0|metros|
|3|Larger Side Lenght of Rectangular Area.|702|metros|
|4|Smaller Side Length of Rectangular<br>Area.|241|metros|
|5|Wind<br>Direction<br>Relative<br>to Long<br>Dimension.|210|grados|

Una vez rellenados todos los inputs en la primera ventana del “ScreenView”, se pasa a la segunda ventana de

inputs de datos del simulador, en ella, se fija el valor de la velocidad del viento predominante, la cual se

establece en 5,5 m/s para la ubicación del proyecto; valor que ha sido obtenido a través de la fuente online del

explorador eólico del Ministerio de Energía.

Además de la velocidad del viento, se ha de seleccionar la clase de vientos en el lugar del proyecto,

definiéndose estos como vientos Clase C- “Ligeramente inestables” (SlightlyUnstable):

Anexo 13: SIMULACIÓN AIR DISPERSION CON SREEN VIEW Página **4** de 8

|Col1|ADENDA 1<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA EL ROSAL|Col3|Col4|
|---|---|---|---|
||ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|
||NOVIEMBRE 2018|Rev.: 0|Rev.: 0|

**Ilustración 1: Parámetros de entrada a la simulación para el proyecto. Vientos**

En la tercera ventana de datos de entrada del ScreenView, se introduce las distancias mínimas y máximas

desde el foco emisor, siendo este último el propio proyecto en sí, hasta los receptores influenciados en las

emisiones atmosféricas. La distancia mínima se ha fijado a un metro y la distancia máxima a 5000 metros para

visualizar el alcance claramente.

Después de introducir todos los inputs descritos anteriormente, se realiza la simulación final a través del propio

ScreenView, y se representan los resultados de la simulación Screen View para la concentración en el aire a

través de la gráfica que se expone a continuación:

**Ilustración 2: tráfico de resultados de la simulación con “Screenview air dispersion”, etapa de construcción.**

Anexo 13: SIMULACIÓN AIR DISPERSION CON SREEN VIEW Página **5** de 8

|Col1|ADENDA 1<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA EL ROSAL|Col3|Col4|
|---|---|---|---|
||ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|
||NOVIEMBRE 2018|Rev.: 0|Rev.: 0|

Como se visualiza en el grafico anterior, la concentración máxima horaria de partículas emitidas en la fase de
construcción del proyecto es de 40,19ug/m [3] a 241 metros del foco o proyecto, dicha concentración se empieza
a estabilizar aproximadamente a 1000 metros de este, con una concentración de 3,77g/m [3] ; a partir de dicha
distancia, la concentración se reduce considerablemente hasta alcanzar valores inferiores a 0,4ug/m [3] .

Etapa de operación

Por otro lado, considerando que los primeros 4 meses del primer año se ejecutará la etapa de construcción y

luego, los 8 meses restantes se llevará a cabo la fase de operación del proyecto, también se realizó la

simulación Screen View para esta etapa.

A continuación, se presentan los inputs de la fase de operación, donde se estima generar 0,50 ton/año de

MP10:

**Tabla** _**2**_ **: Datos introducidos para hacer la simulación, etapa de operación.**

|Col1|CAMPOS A RELLENAR|VALORES|UNIDADES|
|---|---|---|---|
|1|EmissionRate.|4,98·10-7|gr/s/m2|
|2|SourceReleaseHeight.|0|metros|
|3|Larger Side Lenght of Rectangular Area.|702|metros|
|4|Smaller Side Length of Rectangular Area.|241|metros|
|5|Wind Direction Relative to Long Dimension.|210|grados|

Respecto al resto de los datos relacionados con los vientos del área del proyecto y la distancia de los

receptores, se mantienen los mismos inputs que para la simulación de la fase de construcción.

Después de introducir todos los datos, se realiza la simulación final a través del propio ScreenView, lo que se

visualiza a través de la gráfica que se expone a continuación:

Anexo 13: SIMULACIÓN AIR DISPERSION CON SREEN VIEW Página **6** de 8

|Col1|ADENDA 1<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA EL ROSAL|Col3|Col4|
|---|---|---|---|
||ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|
||NOVIEMBRE 2018|Rev.: 0|Rev.: 0|

**Ilustración** _**3**_ **: tráfico de resultados de la simulación con “Screenview air dispersion”, etapa de Operación.**

Como se visualiza en el grafico anterior, la concentración máxima horaria de partículas emitidas será de
5,32ug/m [3] a 241 metros del foco o proyecto, dicha concentración se empieza a estabilizar aproximadamente a
1000 metros de este, con una concentración de 0,5ug/m [3] ; a partir de dicha distancia, la concentración se
reduce considerablemente hasta alcanzar valores inferiores a 0,1ug/m [3] .

Finalmente, en el primer año del proyecto, el cual es el más crítico en términos de emisiones atmosféricas, se
tiene que por 4 meses se emitirán como máximo 40,19ug/m [3 ] y por los 8 meses restantes del primer año, se
emitirán 5,32ug/m [3], obteniendo un promedio ponderado de 16,94ug/m [3 ] como concentración anual del primer

año, considerando que se producirá la máxima concentración horaria de cada etapa.

Anexo 13: SIMULACIÓN AIR DISPERSION CON SREEN VIEW Página **7** de 8

|Col1|ADENDA 1<br>NUEVA CENTRAL SOLAR FOTOVOLTAICA EL ROSAL|Col3|Col4|
|---|---|---|---|
||ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|ANEXO 13: SIMULACIÓN AIR DISPERSION SCREEN<br>VIEW|
||NOVIEMBRE 2018|Rev.: 0|Rev.: 0|

**1.2** **Análisis de los resultados**

Utilizando como referencia la normativa de calidad primaria del aire para MP10, en la cual indica que el límite
de la concentración anual (promedio de 3 años consecutivos) es de 50ug/m [3], y considerando la concentración
máxima anual del proyecto de 16,94ug/m [3 ] (Promedio de 1 año, el cual es el más crítico), se concluye que se

cumple con dicha normativa ya que su concentración máxima es inferior al valor máximo permitido por la

normativa de calidad de aire para MP10.

Considerando que las partículas de MP10, están compuestas por fracciones gruesas y finas, y que por lo tanto

dentro de las partículas MP10 se encuentran las partículas correspondientes al MP2,5 en una proporción

menor a las partículas MP10, si se considera para el análisis de la concentración de MP2,5 el resultado de

concentración de las partículas MP10, siempre se está analizando una situación mucho más conservadora y

crítica que la situación real y por lo tanto el análisis proporcionaría un resultado certero y con márgenes de

seguridad. Por todo ello se utiliza a efectos de comparación de resultado de concentración de MP2,5 con los

límites establecidos con la normativa, los resultados de las concentraciones anuales del proyecto de
16,94ug/m [3], sabiendo que la concentración de MP2,5 será menor que este valor, dicho resultado se encuentra

por debajo del límite establecido por la normativa de calidad primaria del aire para MP2,5 (Decreto Supremo
no 12/2011, Ministerio de Medio Ambiente)siendo este límite de concentración anual de 20ug/m [3] . Por tanto,

se concluye que también para las partículas MP2,5 las concentraciones producidas por el proyecto son

inferiores a los límites establecidos por dicha normativa.

Expuesto lo detallado en los párrafos anteriores, se concluye que el proyecto solar fotovoltaico El Rosal, no

tienen ningún efecto adverso significativo ni impacto adverso para la salud de las personas ni la calidad del aire

en el área del proyecto y tampoco para las poblaciones cercanas.

Anexo 13: SIMULACIÓN AIR DISPERSION CON SREEN VIEW Página **8** de 8