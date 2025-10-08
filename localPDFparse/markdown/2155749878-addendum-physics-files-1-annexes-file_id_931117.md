---
title: Sin título
author: Ramón Valdivia
date: D:20230327160446-03'00'
language: es
type: report
pages: 10
has_toc: False
has_tables: True
extraction_quality: high
---

|REV.|FECHA|RVIA|Col4|Col5|DESCRIPCIÓN|
|---|---|---|---|---|---|
|**REV.**|**FECHA**|**PREP.**|**REV.**|**APR.**||
|A|19-12-22|FMF|IVV|RVV|Revisión Interna|
|B|13-01-23|FMF|IVV|RVV|Revisión del Cliente|
|||||||
|||||||

2210323-00-HID-MCA-006 REV B Página 1 de 10

**ÍNDICE**

**1** **GENERAL ......................................................................................................................... 3**
**1.1** **INTRODUCCIÓN ......................................................................................................................... 3**

**1.2** **OBJETIVOS ................................................................................................................................. 3**
**1.3** **ALCANCES ................................................................................................................................. 3**

**1.4** **EXCLUSIONES ........................................................................................................................... 3**
**1.5** **REFERENCIAS ........................................................................................................................... 3**
**2** **DESCRIPCION DEL PROYECTO ................................................................................... 3**
**3** **CONSIDERACIONES DEL MODELO ............................................................................. 5**

**3.1** **TOPOGRAFIA ............................................................................................................................. 5**

**3.2** **PERIODO DE RETORNO ............................................................................................................ 5**
**3.3** **CAUDALES ................................................................................................................................. 5**

**3.4** **COEFICIENTE DE RUGOSIDAD ................................................................................................ 6**
**3.5** **CONDICIONES DE BORDE ........................................................................................................ 7**

**3.6** **COEFICIENTE DE EXPANSION Y CONTRACCION .................................................................. 7**
**4** **MODELACION DE EJES HIDRAULICOS ....................................................................... 8**

**4.1** **ESCENARIO MODELADO .......................................................................................................... 8**

**TABLAS**

Tabla 3-1 Periodos de Retorno para Diseño de Cauces, Criterio DGA. ................................... 5

Tabla 3-2 Caudales de Diseño ................................................................................................... 6

Tabla 3-3 Determinación del Coeficiente de Rugosidad ........................................................... 6

Tabla 3-4 Determinación del Coeficiente de Rugosidad ........................................................... 7

Tabla 4-1 Eje Hidráulico Situación sin Proyecto (T=100 años) ............................................... 10

**FIGURAS**

Figura 2-1. Trazado de línea de relaves .................................................................................... 4

Figura 4-1 Pretil del Cauce Natural. ........................................................................................... 8

Figura 4-2 Esquema Isométrico del Cauce en Crecida ............................................................. 9

Figura 4-3 Perfil Longitudinal del Cauce en Crecida ................................................................. 9

2210323-00-HID-MCA-006 REV B Página 2 de 10

**1** **GENERAL**

**1.1** **INTRODUCCIÓN**

RVIA desarrolló para su cliente Minera Las Cenizas (“MLC”) el Proyecto de Disposición de
Relave en Pasta en Interior Mina Faena Cabildo, incluyendo la impulsión y líneas en superficie
e interior mina para el transporte de la pasta, así como información base para preparar la
Declaración de Impacto Ambiental (“DIA”).

En el contexto de la tramitación ambiental, MLC recibió el primer Informe Consolidado de
Solicitud de Aclaraciones, Rectificaciones y/o Ampliaciones (“ICSARA”) de acuerdo a Carta
N°202205103344 del 29 de junio del 2022 por parte de la directora regional del SEA de la
región de Valparaíso, para el cual este servicio incluye la elaboración de las respuestas de
algunas consultas seleccionadas.

**1.2** **OBJETIVOS**

El presente estudio hidráulico ha sido elaborado por RV Ingenieros para MLC, en el marco de
la elaboración de la Declaración de Impacto Ambiental asociada a Proyecto de Disposición de
Relave en Pasta en Interior Mina Faena Cabildo, incluyendo la impulsión y líneas en superficie
e interior mina para el transporte de la pasta en la comuna de Cabildo de acuerdo con lo
señalado por el Decreto Supremo 40 del Ministerio de Medio Ambiente.

**1.3** **ALCANCES**

El análisis para desarrollar busca establecer el comportamiento de las quebradas para la
condición actual y el escenario proyectado (al termino de las faenas de ejecución de la línea
de relaves, se considera la restitución de la sección transversal, por lo que ambos escenarios
se consideran iguales), para las crecidas de diseño.

Se considera la simulación de la quebrada en una extensión de 100 metros agua arriba y 100
metros aguas debajo del punto de la interferencia o hasta donde sea identificable el cauce.

**1.4** **REFERENCIAS**

Los presentes criterios de diseño son complementarios a los documentos indicados a
continuación:

Ref. 1 Manual de Carreteras - Volumen 3, MOP - Junio 2002

Ref. 2 Manual de Cálculo de Crecidas en Cuencas sin Control Fluviométrico, DGAAgosto 1995.

Ref. 3 Guías Metodológica para Proyectos de Modificación de Cauces, DGA - Diciembre

2016

Ref. 4 Memoria de cálculo - Hidrología, RVIA - Diciembre 2022, 2210323-00-HID-MCA-001

2210323-00-HID-MCA-006 REV B Página 3 de 10

**2** **DESCRIPCION DEL PROYECTO**

El Proyecto consiste en la construcción de un nuevo sistema para la disposición final de relave
en pasta producido en la Planta de Procesamiento de Minerales Cabildo de Minera Las
Cenizas. Este sistema está compuesto por una tubería de transporte de relave en pasta,
desde la actual planta de pasta, hasta la Boca Mina Farellones, desde donde será distribuido
el relave en pasta a los distintos caserones existentes al interior de la mina subterránea.

Por otro lado, el Proyecto DEPIM considera la instalación de una línea Bypass, la cual
pretende ser una alternativa a la existente por la interior mina para el transporte de los
relaves espesados producidos en la Planta de Beneficio, en el tramo entre Bocamina
Sauce y Bocamina Soledad.

Se ha detectado que el trazado de la línea de impulsión proyectada genera la interferencia
con al menos 22 quebradas menores, por lo que se estudia la necesidad de obras de
protección de estas.

En la Figura 2-1 se ilustra el trazado de la línea de impulsión proyectada (en azul) y el trazado
de la línea de impulsión existente (en rojo) la que se mantiene.

Figura 2-1. Trazado de línea de relaves

2210323-00-HID-MCA-006 REV B Página 4 de 10

**3** **CONSIDERACIONES DEL MODELO**

Para la realización del modelo hidráulico se ha tenido en consideración lo siguiente:

 - En todos los casos que se analizan, se trata de un cauce de un ancho claramente

definido y regular con escasa vegetación en sus riberas.

 En general, se han incluido en el modelo todas las singularidades hidráulicas de los

cauces, de modo de obtener resultados más certeros en la modelación de las crecidas.

 El largo del pretil ha sido determinado de acuerdo con las condiciones topográficas y

a los requerimientos hidráulicos correspondientes, de modo de no alterar, en la medida
de lo posible, las condiciones hidráulicas existentes en el cauce.

**3.1** **TOPOGRAFIA**

La modelación de los cauces se realizó con una topografía proporcionada por el mandante en
base a un levantamiento Aero fotogramétrico, con curvas de nivel cada 1 m.

**3.2** **PERIODO DE RETORNO**

El proyecto en estudio considera la construcción de un pretil a fin de mejorar las condiciones
de operación del sector.

Las características de la obra proyectada la asimilan a obras de defensa fluvial, por lo que, se
adopta un periodo de retorno de 100 años, de acuerdo con las recomendaciones de la Guías
Metodológicas para Proyectos de Modificaciones de Cauces de la DGA.

**Tabla 3-1 Periodos de Retorno para Diseño de Cauces, Criterio DGA.**

**Tipo de Obra** **Detalle** **Diseño** **Verificación**

Sobre Cauce 50 100
Atravieso con Ductos
Bajo Cauce 100 150

Puente 100 150
Atravieso con Estructura Vial
Alcantarilla 50 100

Descargas Ductos 100 150

Restitución de Caudal 100 150

Modificación Trazado Abovedamiento 100 150

Contorno Abierto 100 150
Regularización Cauce Natural 100 150
**Defensas Fluviales** **Cauce Natural** **100** **-**

Fuente: Guías Metodológicas para Proyectos de Modificación de Cauces, DGA.

**3.3** **CAUDALES**

Los caudales que serán utilizados en el diseño hidráulico corresponden a los determinados
en el informe Memoria de Cálculo de Regularización de Cauce - Hidrología y se resumen en
las tablas siguientes.

2210323-00-HID-MCA-006 REV B Página 5 de 10

**Tabla 3-2 Caudales de Diseño**

|Periodo de Retorno|Caudal|
|---|---|
|(años)|(m3/s)|
|2|0,01|
|5|0,02|
|10|0,02|
|25|0,03|
|50|0,03|
|100|0,05|
|200|0,05|

**3.4** **COEFICIENTE DE RUGOSIDAD**

El coeficiente de rugosidad propuesto por Manning ha sido estimado empleando el criterio de
Cowan, el que permite considerar los factores propios del cauce como son vegetación,
meandros, obstrucciones, entre otros, razón por la cual son preponderantes las observaciones
realizadas en terreno, tendientes a cualificar y cuantificar estos factores.

El método de Cowan, utiliza como base la siguiente expresión, la cual considera los factores
más relevantes para la determinación de n:

_n_ = _m_  ( _n_ 0 + _n_ 1 + _n_ 2 + _n_ 3 + _n_ 4 )

En el siguiente cuadro se muestran los valores escogidos para determinar el n:

**Tabla 3-3 Determinación del Coeficiente de Rugosidad**

Los coeficientes de Manning han sido adoptados de acuerdo con las características del cauce
principal y riberas, obtenidas desde terreno.

En general, el cauce en el tramo en análisis presenta una pendiente longitudinal fuerte, con
baja sinuosidad, escasa presencia de meandros y sin vegetación, las secciones
transversales pueden ser clasificadas como homogéneas.

En el siguiente cuadro se muestran los valores escogidos para determinar el n:

2210323-00-HID-MCA-006 REV B Página 6 de 10

**Tabla 3-4 Determinación del Coeficiente de Rugosidad**

|Tramo|n<br>0|n<br>1|n<br>2|n<br>3|n<br>4|m|n total|
|---|---|---|---|---|---|---|---|
|Ribera Izquierda|0,020|0,000|0,000|0,010|0,001|1,00|0,040|
|Cauce Central|0,020|0,001|0,001|0,002|0,005|1,00|0,065|
|Ribera Derecha|0,020|0,000|0,000|0,010|0,001|1,00|0,040|

**3.5** **CONDICIONES DE BORDE**

La modelación hidráulica del cauce requiere definir las condiciones de borde con que se
ejecutará la simulación, cuyas condiciones dependerán del tipo de régimen de escurrimiento,
ya sea supercrítico o subcrítico.

El régimen subcrítico (o de rio), se impone cuando la pendiente longitudinal del fondo del
cauce es menor a la pendiente crítica asociada al flujo, siendo necesario definir las
condiciones de borde existentes aguas abajo del tramo en análisis.

En el caso de régimen supercrítico (o de torrente), se impone en aquellos casos en que la
pendiente longitudinal del fondo del cauce es mayor (más fuerte) que la pendiente critica
asociada al flujo, siendo necesario definir las condiciones de borde existentes aguas arriba
del tramo en análisis.

Para el caso de cauces naturales, en que la sección transversal no es constante, es complejo
estimar la pendiente critica, por lo que, la practica recomienda asumir el tipo de régimen de
escurrimiento de acuerdo con el siguiente criterio.

Régimen subcrítico, para pendientes longitudinales promedios menores a 0,001

Régimen mixto, para pendientes longitudinales promedio entre 0,001 y 0,01

Régimen supercrítico, para pendientes longitudinales promedios mayores a 0,01

En general, el cauce presenta una pendiente longitudinal promedio para la línea de energía
con valor de 0,50, por lo que se ha estimado que se impone un régimen supercrítico, lo que
en conjunto con la condición de cauce natural, genera la necesidad de modelar el flujo bajo
las condiciones de régimen mixto.

Por lo anterior, por aguas arriba se declara como condición de borde la ocurrencia de altura
critica, mientras que por aguas abajo, se declara la ocurrencia de una altura normal asociada
a la pendiente con valor de 0,50.

**3.6** **COEFICIENTE DE EXPANSION Y CONTRACCION**

La contracción o expansión de la corriente debido a cambios entre dos secciones
transversales consecutivas produce una pérdida de energía que se evalúa mediante la
aplicación de coeficientes de expansión y contracción.

En el caso de cauces naturales, se considera que las contracciones y expansiones entre dos
secciones se desarrollan de forma gradual (no brusca), por lo que, se recomienda adoptar un
coeficiente de contracción de 0,3 y de expansión de 0,1.

2210323-00-HID-MCA-006 REV B Página 7 de 10

**4** **MODELACION DE EJES HIDRAULICOS**

El cálculo de la cota de aguas máximas en el perfil batimétrico se determina mediante la
utilización del software HEC-RAS; U.S. Army Corps of Engineers Hydrologic Engineering
Center, 1997.

El cálculo se lleva a cabo por el método de factores de conducción hidráulica asumiendo
condiciones de escurrimiento gradualmente variada para cada una de las secciones de
cálculo.

El proceso se lleva a cabo mecánicamente empleando un software computacional cuyos datos
de entrada son la topografía del cauce, considerando perfiles transversales cada 20 m, en una
extensión mínima de 200 metros exigida por la DOH, lo que se complementa con los
antecedentes de hidrología representados por caudales de crecida y las condiciones
hidráulicas que definen la rugosidad.

**4.1** **ESCENARIO MODELADO**

La simulación corresponde a un cauce natural que se cruza con el trazado soterrado de la
línea de impulsión de relaves.

Los resultados obtenidos desde la modelación se representan esquemáticamente en las
siguientes figuras siguientes.

QDA_5 Plan: Plan 01 22-12-2022

River = QDA_5 Reach = QDA_5 RS = 80

.04 .065 .04

517

516

515

514

513

512

|Col1|Col2|Col3|Col4|Col5|Legend|
|---|---|---|---|---|---|
||||||WS T=100<br>Ground<br>Bank Sta|
|||||||
|||||||
|||||||
|||||||

0 20 40 60 80 100

Station (m)

Figura 4-1 Pretil del Cauce Natural.

2210323-00-HID-MCA-006 REV B Página 8 de 10

Figura 4-2 Esquema Isométrico del Cauce en Crecida

QDA_5 Plan: Plan 01 22-12-2022

530

520

510

500

490

480

470

460

|Col1|Col2|Col3|Col4|Col5|Col6|Col7|Legend|
|---|---|---|---|---|---|---|---|
||||||||WS T=100<br>Ground|
|||||||||
|||||||||
|||||||||
|||||||||

0 20 40 60 80 100 120 140

Main Channel Distance (m)

Figura 4-3 Perfil Longitudinal del Cauce en Crecida

2210323-00-HID-MCA-006 REV B Página 9 de 10

Tabla 4-1 Eje Hidráulico Situación sin Proyecto (T=100 años)

|PT -N°|Q|Z1|Z2|Z3|Z4|J|V|A|L|F|
|---|---|---|---|---|---|---|---|---|---|---|
|**PT -N°**<br>|(m3/s)<br>|(m)<br>|(m)<br>|(m)<br>|(m)<br>|(m/m)<br>|(m/s)<br>|(m2)<br>|(m)<br>|(m)<br>|

|PT-<br>126.6|0.05|526.74|526.79|526.79|526.81|0.1335|0.60|0.08|2.36|1.03|
|---|---|---|---|---|---|---|---|---|---|---|
|PT-120|0.05|524.97|525.00|525.01|525.05|0.7628|1.02|0.05|2.33|2.25|
|PT-100|0.05|519.66|519.69|519.69|519.71|0.1467|0.49|0.10|4.24|1.01|
|PT-080|0.05|512.35|512.37|512.39|512.64|15.6263|2.32|0.02|2.89|8.58|
|PT-060|0.05|500.72|500.74|500.74|500.75|0.1348|0.33|0.15|13.77|0.89|
|PT-040|0.05|486.98|487.05|487.05|487.07|0.1229|0.63|0.08|2.00|1.00|
|PT-020|0.05|473.67|473.77|473.77|473.81|0.1070|0.81|0.06|0.92|1.00|
|PT-0|0.05|461.44|461.54|461.52|461.55|0.0500|0.54|0.09|1.49|0.69|

**PT** Nombre Perfil Transversal Modelado en HEC-RAS

**Q** = Caudal (L/s) **J** = Pendiente media de la línea de energía (m/m)
**Z1** = Cota de fondo m.s.m.m. **V** = Velocidad media de la sección (m/s)
**Z2** = Cota eje hidráulico m.s.m.m. **A** = Área de la sección (m [2] )

**Z3** = Cota de línea de energía m.s.m.m. **L** = Ancho de la superficie libre (m)

**Z4** = Cota de altura critica m.s.m.m. **F** = Valor de Froude

**5** **CONCLUSIONES**

- El proyecto de disposición de Relave en Pasta en Interior Mina Faena Cabildo considera la

interferencia con el cauce natural N°5.

- La instalación de la tubería para el by pass será de forma soterrada restituyendo la forma

del cauce natural sin considerar estructuras sobre el nivel del terreno.

- Por lo anterior, se considera que el resultado del escenario sin proyecto y con proyecto son

válidos con el mismo modelo.

**FIN DEL DOCUMENTO.**

2210323-00-HID-MCA-006 REV B Página 10 de 10

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 3-2: Caudales de Diseño****

| Periodo de Retorno | Caudal |
| --- | --- |
| (años) | (m3/s) |
| 2 | 0,01 |
| 5 | 0,02 |
| 10 | 0,02 |
| 25 | 0,03 |
| 50 | 0,03 |
| 100 | 0,05 |
| 200 | 0,05 |

**Tabla 3-4: Determinación del Coeficiente de Rugosidad****

| Tramo | n<br>0 | n<br>1 | n<br>2 | n<br>3 | n<br>4 | m | n total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ribera Izquierda | 0,020 | 0,000 | 0,000 | 0,010 | 0,001 | 1,00 | 0,040 |
| Cauce Central | 0,020 | 0,001 | 0,001 | 0,002 | 0,005 | 1,00 | 0,065 |
| Ribera Derecha | 0,020 | 0,000 | 0,000 | 0,010 | 0,001 | 1,00 | 0,040 |

**Tabla 4-1: Eje Hidráulico Situación sin Proyecto (T=100 años)**

| PT-<br>126.6 | 0.05 | 526.74 | 526.79 | 526.79 | 526.81 | 0.1335 | 0.60 | 0.08 | 2.36 | 1.03 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| PT-120 | 0.05 | 524.97 | 525.00 | 525.01 | 525.05 | 0.7628 | 1.02 | 0.05 | 2.33 | 2.25 |
| PT-100 | 0.05 | 519.66 | 519.69 | 519.69 | 519.71 | 0.1467 | 0.49 | 0.10 | 4.24 | 1.01 |
| PT-080 | 0.05 | 512.35 | 512.37 | 512.39 | 512.64 | 15.6263 | 2.32 | 0.02 | 2.89 | 8.58 |
| PT-060 | 0.05 | 500.72 | 500.74 | 500.74 | 500.75 | 0.1348 | 0.33 | 0.15 | 13.77 | 0.89 |
| PT-040 | 0.05 | 486.98 | 487.05 | 487.05 | 487.07 | 0.1229 | 0.63 | 0.08 | 2.00 | 1.00 |
| PT-020 | 0.05 | 473.67 | 473.77 | 473.77 | 473.81 | 0.1070 | 0.81 | 0.06 | 0.92 | 1.00 |
| PT-0 | 0.05 | 461.44 | 461.54 | 461.52 | 461.55 | 0.0500 | 0.54 | 0.09 | 1.49 | 0.69 |
