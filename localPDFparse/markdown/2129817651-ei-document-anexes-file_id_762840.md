---
title: Mem. Justific. Protecc. C/Incendio Tk Metanol 80 m3
author: Jorge Rodruguez
date: D:20140902125553-04'00'
language: es
type: report
pages: 13
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - INCOMEX
-->

_**Mem. Cálculo Hidráulica Sistema Extinción Bodegas**_

Almacenamiento de Sustancias Químicas Peligrosas

**INCOMEX LTDA.**

____________________________________________________________________________________________________________

# INCOMEX

## Declaración de Impacto Ambiental del Proyecto “Almacenamiento de Sustancias Químicas Peligrosas”

### Memoria de Cálculo Hidráulico Sistema Extinción Bodegas

#### Julio 2014

|Edición|Proyecto|Tipo Doc.|Por:|Apr.|
|---|---|---|---|---|
|A|DIA Almac. Sustancias Qcas. Peligrosas|Memoria Cálculo|OVR|JRH|
|Fecha|Archivo/Ruta|Archivo/Ruta|Rev.|Pág.|
|14/07/14|inc-154-1-01-m-mem-511|inc-154-1-01-m-mem-511|GVF|1/13|

Este documento es propiedad intelectual de Inning Group, no podrá ser utilizado con otro propósito que no sea el estipulado en la relación con el cliente.

_**Mem. Cálculo Hidráulica Sistema Extinción Bodegas**_

Almacenamiento de Sustancias Químicas Peligrosas

**INCOMEX LTDA.**

____________________________________________________________________________________________________________

**INDICE**

**INCOMEX ........................................................................................................................................... 1**

**1.** **INTRODUCCION ...................................................................................................................... 4**

**2.** **OBJETIVOS ............................................................................................................................. 4**

**2.1** **Objetivo General .....................................................................................................................................4**

**2.2** **Objetivos Específicos ............................................................................................................................4**

**3.** **ANTECEDENTES, NORMAS Y BIBLIOGRAFÍA ...................................................................... 4**

**3.1** **Antecedentes ..........................................................................................................................................4**

**3.2** **Normas y Bibliografía .............................................................................................................................4**

**4.** **CONSIDERACIONES DE DISEÑO .......................................................................................... 5**

**4.1** **Condiciones Generales ..........................................................................................................................5**

**4.2** **Criterios de Diseño .................................................................................................................................5**

_4.2.1_ _Sistema de extinción Bodegas Inflamables .......................................................................................5_

_4.2.2_ _Sistema de extinción Bodegas no inflamables ..................................................................................6_

**5.** **PARÁMETROS DE DISEÑO HIDRAULICO ............................................................................. 6**

**5.1** **Bodegas Inflamables ..............................................................................................................................6**

**5.2** **Bodegas de sustancias no inflamables ...............................................................................................7**

**6.** **DESARROLLO ......................................................................................................................... 7**

**6.1** **Metodología.............................................................................................................................................7**

_6.1.1_ _Ecuación de Bernoulli ........................................................................................................................8_

_6.1.2_ _Pérdida de Carga por Fricción en Tuberías ......................................................................................8_

**7.** **SIMULACIÓN HIDRÁULICA .................................................................................................. 10**

**7.1** **Simulación bodegas inflamables ........................................................................................................10**

**7.2** **Simulación bodegas NO inflamables .................................................................................................11**

**8.** **RESULTADOS ....................................................................................................................... 12**

**8.1** **Resultados simulación bodega inflamables ......................................................................................12**

**8.2** **Resultados simulación bodega no inflamables ................................................................................13**

**9.** **CONCLUSIONES Y RECOMENDACIONES .......................................................................... 13**

|Edición|Proyecto|Tipo Doc.|Por:|Apr.|
|---|---|---|---|---|
|A|DIA Almac. Sustancias Qcas. Peligrosas|Memoria Cálculo|OVR|JRH|
|Fecha|Archivo/Ruta|Archivo/Ruta|Rev.|Pág.|
|14/07/14|inc-154-1-01-m-mem-511|inc-154-1-01-m-mem-511|GVF|2/13|

Este documento es propiedad intelectual de Inning Group, no podrá ser utilizado con otro propósito que no sea el estipulado en la relación con el cliente.

_**Mem. Cálculo Hidráulica Sistema Extinción Bodegas**_

Almacenamiento de Sustancias Químicas Peligrosas

**INCOMEX LTDA.**

____________________________________________________________________________________________________________

**10.** **REPORTE SIMULACIÓN ..............................................** ¡ERROR! MARCADOR NO DEFINIDO.

**10.1** **Reporte Simulación Bodegas inflamables ..........................................** ¡Error! Marcador no definido.

**10.2** **Reporte Simulación Bodegas NO inflamables ....................................** ¡Error! Marcador no definido.

|Edición|Proyecto|Tipo Doc.|Por:|Apr.|
|---|---|---|---|---|
|A|DIA Almac. Sustancias Qcas. Peligrosas|Memoria Cálculo|OVR|JRH|
|Fecha|Archivo/Ruta|Archivo/Ruta|Rev.|Pág.|
|14/07/14|inc-154-1-01-m-mem-511|inc-154-1-01-m-mem-511|GVF|3/13|

Este documento es propiedad intelectual de Inning Group, no podrá ser utilizado con otro propósito que no sea el estipulado en la relación con el cliente.

_**Mem. Cálculo Hidráulica Sistema Extinción Bodegas**_

Almacenamiento de Sustancias Químicas Peligrosas

**INCOMEX LTDA.**

____________________________________________________________________________________________________________

**1. INTRODUCCION**

El presente documento desarrolla el cálculo hidráulico de la red de protección contra incendios para las
bodegas de productos inflamables y no inflamables ubicadas en las dependencias de INCOMEX LTDA,
Bodegaje La Pólvora, Valparaíso.

**2. OBJETIVOS**

**2.1** **Objetivo General**

La presente memoria tiene por objetivo diseñar un sistema contra incendio para las bodegas que almacenará
productos inflamables y no inflambles. Dicho diseño se realiza en base a los estándares impuestos por la
National Fire Protection Agency (NFPA).

**2.2** **Objetivos Específicos**

Los objetivos específicos de la memoria corresponden a:

- Diseñar un sistema de extinción en base a sprinklers.

- Detallar los cálculos hidráulicos para el funcionamiento óptimo del sistema

**3. ANTECEDENTES, NORMAS Y BIBLIOGRAFÍA**

**3.1** **Antecedentes**

Los antecedentes considerados para el desarrollo de la presente memoria corresponden a:

P&ID General Sistema Contra Incendio

Layout Sistema Contra Incendio

Layout Almacenamiento de Sustancias Peligrosas

Por otro lado se cuenta con planos de diseño estructural de las bodegas de almacenamiento.

**3.2** **Normas y Bibliografía**

El presente documento se elabora en base a las prescripciones y recomendaciones de la _National Fire_

_Protection Agency (NFPA)_, en particular en lo contenido en las normas indicadas a continuación:

NFPA 13 “Standard para Sistema Instalación de Sprinklers”

NFPA 30: “Código de líquidos inflamables y combustible”

DS 78: “Reglamento de Almacenamiento de Sustancias Peligrosas”

|Edición|Proyecto|Tipo Doc.|Por:|Apr.|
|---|---|---|---|---|
|A|DIA Almac. Sustancias Qcas. Peligrosas|Memoria Cálculo|OVR|JRH|
|Fecha|Archivo/Ruta|Archivo/Ruta|Rev.|Pág.|
|14/07/14|inc-154-1-01-m-mem-511|inc-154-1-01-m-mem-511|GVF|4/13|

Este documento es propiedad intelectual de Inning Group, no podrá ser utilizado con otro propósito que no sea el estipulado en la relación con el cliente.

_**Mem. Cálculo Hidráulica Sistema Extinción Bodegas**_

Almacenamiento de Sustancias Químicas Peligrosas

**INCOMEX LTDA.**

____________________________________________________________________________________________________________

**4. CONSIDERACIONES DE DISEÑO**

**4.1** **Condiciones Generales**

El diseño de protección contra incendio que se describe a continuación, considera lo siguiente:

|Ítem|Instalación|Clase<br>(DS 78)|TAG|Superficie<br>[m2]|Agente extintor|Tipo<br>Almacenam.|
|---|---|---|---|---|---|---|
|1|B. Comburentes|5.1- 5.2|106-1|672|Agua|Racks|
|2|B. Gases No inflamables|2.2|106-2A|97|Agua|Racks|
|3|B. Gases Inflamables|2.1|106-2B|100|Agua - Espuma|Racks|
|4|B. Sustancias Peligrosas|6.1-8.9|106-3|531|Agua|Racks|
|5|B. RESPEL (inflamables)|-|106-4|97|Agua - Espuma|Pallet|
|6|B. RESPEL|-|106-5|109|Agua|Pallet|
|7|B. Inflamables|3-4.1-4.2|106-7|2.000|Agua - Espuma|Racks|

- Altura al hombro: 6000 mm

- Altura máxima techo: 7600 mm

**4.2** **Criterios de Diseño**

Los criterios se establecen de conformidad con la norma NFPA y queda definido como sigue:

 - Distanciamientos de sprinklers en el techo:


Mínimo entre sprinklers: 1800 mm


Máximo entre sprinklers: 3660 mm


Mínima entre sprinklers y paredes: 110 mm


Máxima entre sprinklers y paredes: 1830 mm

 - Área máxima cubierta por sprinkler: 100 pie [2] (9,3 m [2] )

 - Diámetro mínimo de cañería para alimentación de sprinklers: 1 1⁄4”

**4.2.1** **Sistema de extinción Bodegas Inflamables**

Para las bodegas con productos inflamables se considera:

 - Agente extintor: agua más concentrado de espuma

 - Se utilizará un sistema de tipo Pre-primed, que significa que las cañerías contienen una pre-mezcla de

agua espuma, con la finalidad de generar la descarga de esta mezcla en forma inmediata.

|Edición|Proyecto|Tipo Doc.|Por:|Apr.|
|---|---|---|---|---|
|A|DIA Almac. Sustancias Qcas. Peligrosas|Memoria Cálculo|OVR|JRH|
|Fecha|Archivo/Ruta|Archivo/Ruta|Rev.|Pág.|
|14/07/14|inc-154-1-01-m-mem-511|inc-154-1-01-m-mem-511|GVF|5/13|

Este documento es propiedad intelectual de Inning Group, no podrá ser utilizado con otro propósito que no sea el estipulado en la relación con el cliente.

_**Mem. Cálculo Hidráulica Sistema Extinción Bodegas**_

Almacenamiento de Sustancias Químicas Peligrosas

**INCOMEX LTDA.**

____________________________________________________________________________________________________________

 - Tiempo de acción de la espuma: 15 minutos

 - Tiempo acción del agua: 120 minutos

 - Espumógeno mínimo: compatible con líquidos inflamable clase 3 (AFFF) al 3%.

 - Protección con Sprinkler en techo y en racks (si aplica)

**4.2.2** **Sistema de extinción Bodegas no inflamables**

Para las bodegas con productos de sustancias no inflamables tales como sustancias peligrosas, comburente y
residuos peligrosos, se considera:

 - Agente extintor: agua

 - Tiempo acción del agua: 60 minutos

 - Protección con Sprinkler en techo

 - Sprinkler en Racks: No necesita

 - Sistema de tuberías húmedas (sistema pre- cebado) con agua.

**5. PARÁMETROS DE DISEÑO HIDRAULICO**

**5.1** **Bodegas Inflamables**

De acuerdo a lo exigido por la norma DS78 articulo 109, para almacenamiento de productos inflamables se
debe disponer un sistema automático de Sprinklers.

 - Por tabla 16.5.2.3 NFPA 30 (Ver.2012):

`o` Sprinkler Techo: K=8.0. SR@140°C NPT 3⁄4 ”. Tipo pendent

`o` Sprinkler Racks: K=5,6. SR@68°C NPT 3⁄4 ”. Tipo pendent con canastillo protector

`o` Presión mínima requerida último sprinkler techo: 14 psi (1 bar)

`o` Presión mínima requerida último sprinkler racks: 28 psi (2 bar)
`o` Densidad: 0.3 gpm/ft [2]
`o` Superficie de diseño: 2000 ft [2] (utilizando sistema pre-cebado mencionado en Nota 3 tabla

16.5.2.3 NFPA 30)

`o` Numero de Sprinklers en el techo: 20 (en superficie de diseño)

`o` Numero de Sprinklers en Racks: 9 (utilizando sistema mencionado en Nota 4 tabla 16.5.2.3

NFPA 30)

`o` Caudal por sprinkler en Techo y Racks: 30 gpm

`o` Caudal total de sprinkler en el techo: 600 gpm

`o` Caudal total de sprinkler en Racks: 270

`o` Caudal apoyo de grifo: 500 gpm

|o Pr|resión máxima en conexiones de manguera: 6,9 bar|r (NFPA 14, ver 2013)|Col4|Col5|
|---|---|---|---|---|
|Edición|Proyecto|Tipo Doc.|Por:|Apr.|
|A|DIA Almac. Sustancias Qcas. Peligrosas|Memoria Cálculo|OVR|JRH|
|Fecha|Archivo/Ruta|Archivo/Ruta|Rev.|Pág.|
|14/07/14|inc-154-1-01-m-mem-511|inc-154-1-01-m-mem-511|GVF|6/13|

Este documento es propiedad intelectual de Inning Group, no podrá ser utilizado con otro propósito que no sea el estipulado en la relación con el cliente.

_**Mem. Cálculo Hidráulica Sistema Extinción Bodegas**_

Almacenamiento de Sustancias Químicas Peligrosas

**INCOMEX LTDA.**

____________________________________________________________________________________________________________

`o` Caudal teórico requerido: 1370 gpm

`o` Caudal disponible en matriz: 1250gpm

NOTA: Para la bodega de RESPEL inflamables 106-4, se considera solo sprinkler en techo (K=8), manteniendo
el sistema precebado y 2000 ft [2] como superficie de diseño. Se consideraran 20 sprinkler en techo.

**5.2** **Bodegas de sustancias no inflamables**

Para este tipo de almacenamiento y de acuerdo a la clasificación de los productos a almacenar, así también
como la altura de la Bodega, se aplica tabla 16.2.3.1 de NFPA 13 Edición 2013, donde se indica como tipo de
protección con agua, rociadores de tipo ESFR (Early Supression Fast Response), que evita colocar rociadores
dentro de los racks.

 - Por tabla 16.2.3.1 NFPA 13 (Ver. 2013):

`o` K seleccionado para los Sprinkler: factor K 25.2

`o` Presión mínima requerida en el último sprinkler: 15 psi (1 bar)

`o` Tipo de rociador : ESFR@75°C tipo pendent

`o` Número de Sprinklers en el techo de diseño: 12 (punto 14.4.3 NFPA 13)

`o` Número de ramales para sección de diseño: 3

`o` Sprinklers por ramal: 4

`o` Caudal por sprinkler techo: 97,6 gpm ( según Ec. 4)

`o` Caudal total requerido en área de diseño de 12 sprinkler: 1171 gpm

`o` Caudal apoyo una manguera: 250 gpm

`o` Presión máxima en conexiones de manguera: 6,9 bar (NFPA 14, ver 2013)

`o` Tiempo de aplicación de agua: 60 minutos

`o` Caudal teórico requerido: 1421 gpm

`o` Caudal disponible en matriz: 1250gpm

**6. DESARROLLO**

**6.1** **Metodología**

Para determinar la demanda de agua requerida por el sistema de Sprinklers de la Bodega de productos
inflamables, se utilizará el método de Área/Densidad, el cual se basa en la determinación de la cantidad de
agua por unidad de área requerido para el combate eficaz de incendio.

Por otro lado, para las bodegas no inflamables el caudal de agua requerido se determinará en base a lo
señalado en los criterios de diseño. Dado el tipo de almacenamiento de los productos el sistema se abastecerá

|Edición|Proyecto|Tipo Doc.|Por:|Apr.|
|---|---|---|---|---|
|A|DIA Almac. Sustancias Qcas. Peligrosas|Memoria Cálculo|OVR|JRH|
|Fecha|Archivo/Ruta|Archivo/Ruta|Rev.|Pág.|
|14/07/14|inc-154-1-01-m-mem-511|inc-154-1-01-m-mem-511|GVF|7/13|

Este documento es propiedad intelectual de Inning Group, no podrá ser utilizado con otro propósito que no sea el estipulado en la relación con el cliente.

_**Mem. Cálculo Hidráulica Sistema Extinción Bodegas**_

Almacenamiento de Sustancias Químicas Peligrosas

**INCOMEX LTDA.**

____________________________________________________________________________________________________________

desde la red principal y el diseño se hidráulico se calculará tomando en cuenta 3 ramales de 4 sprinkler cada
uno según lo establece la norma.

Para ambos sistemas se contará con un sistema de tubería “Húmeda” controlada por válvula de alarma.

La simulación del sistema se llevará a cabo mediante una modelación en el software Pipeflow Expert 2010.

Los cálculos efectuados por el software se realizan en base a las siguientes ecuaciones.

**6.1.1** **Ecuación de Bernoulli**

La diferencia de presión entre la entrada y la salida de un elemento de piping o cañería para un fluido
incompresible viene dada por:

1 2
P  2 v  gh E V Ec.1

Dónde:

P: diferencia de presión entre la entrada y la salida de la cañería
: densidad del fluido
v [2] : variación del cuadrado de la velocidad del fluido entre la entrada y la salida de la cañería
h: variación de altura entre la entrada y la salida de la cañería
EV: pérdida de carga en tubería por el efecto de la fricción y accesorios

**6.1.2** **Pérdida de Carga por Fricción en Tuberías**

a) Pérdida de Carga Regular

La pérdida de carga regular por efecto de la fricción del fluido con la pared interior de un elemento de cañería
viene dada por:

 6,05 C 1,85 Q m d 1,85m4,87  10 5 

1,85

E V  6,05 C 1,85 Q m d 4,87  10 5 L

V  6,05 C 1,85m d m4,87  10 5

Ec.2

Dónde:

Q m : flujo por la cañería en l/min
C: coeficiente de pérdida por fricción
d m : diámetro interior de la cañería en mm

b) Pérdida de carga singular (fittings y accesorios)
El cálculo de la pérdida de carga singular se realiza asignando a cada elemento (codos, tees, válvulas, etc.) un

largo equivalente de acuerdo Tabla 1.

|Edición|Proyecto|Tipo Doc.|Por:|Apr.|
|---|---|---|---|---|
|A|DIA Almac. Sustancias Qcas. Peligrosas|Memoria Cálculo|OVR|JRH|
|Fecha|Archivo/Ruta|Archivo/Ruta|Rev.|Pág.|
|14/07/14|inc-154-1-01-m-mem-511|inc-154-1-01-m-mem-511|GVF|8/13|

Este documento es propiedad intelectual de Inning Group, no podrá ser utilizado con otro propósito que no sea el estipulado en la relación con el cliente.

_**Mem. Cálculo Hidráulica Sistema Extinción Bodegas**_

Almacenamiento de Sustancias Químicas Peligrosas

**INCOMEX LTDA.**

____________________________________________________________________________________________________________

**Tabla 1: Largo Equivalente para Elementos Singulares de la Red**

De esta manera, la pérdida de carga queda escrita como:

 6,05 C 1,85 Q m d 1,85m4,87  10 5 

1,85

E V  6,05 C 1,85 Q m d 4,87  10 5 L

V  6,05 C 1,85m d m4,87  10 5 L eq

Ec.3

Dónde:

L eq : largo equivalente para elementos singulares de la red.

c) Caudal vs Presión en Sprinklers

Los sprinklers son elementos diseñados para proporcionar agua en forma de lluvia a la zona de protección de

incendios respectiva. El caudal de agua de aspersión entregado por éstos queda determinado por la
siguiente fórmula:

Q  K  P Ec.4

Dónde:

Q: caudal a través del sprinkler [gpm]

K: constante empírica determinada por el diámetro del orificio de aspersión particular [gpm/psi [0,5] ]
De acuerdo a lo indicado en la Norma NFPA13, se tienen las siguientes constantes K para sprinklers:

|Edición|Proyecto|Tipo Doc.|Por:|Apr.|
|---|---|---|---|---|
|A|DIA Almac. Sustancias Qcas. Peligrosas|Memoria Cálculo|OVR|JRH|
|Fecha|Archivo/Ruta|Archivo/Ruta|Rev.|Pág.|
|14/07/14|inc-154-1-01-m-mem-511|inc-154-1-01-m-mem-511|GVF|9/13|

Este documento es propiedad intelectual de Inning Group, no podrá ser utilizado con otro propósito que no sea el estipulado en la relación con el cliente.

_**Mem. Cálculo Hidráulica Sistema Extinción Bodegas**_

Almacenamiento de Sustancias Químicas Peligrosas

**INCOMEX LTDA.**

____________________________________________________________________________________________________________

**Tabla 2: Constantes K para Sprinklers**

**7. SIMULACIÓN HIDRÁULICA**

**7.1** **Simulación bodegas inflamables**

La simulación de la bodega de inflamables se ha efectuado con los siguientes elementos:

- Cañería entrada hacia bodega: 6” Sch 40

- Matriz ramales hacia sprinklers techo y racks: 4” Sch 40

- Cañería hacia sprinkler racks: 2 1/2” Sch 40

- Ramales sprinkler techo :2”

- Ramales sprinkler racks: 2”

- Cañería hacia manguera: 2 1⁄2”

- Material: acero al carbono A-53

|Edición|Proyecto|Tipo Doc.|Por:|Apr.|
|---|---|---|---|---|
|A|DIA Almac. Sustancias Qcas. Peligrosas|Memoria Cálculo|OVR|JRH|
|Fecha|Archivo/Ruta|Archivo/Ruta|Rev.|Pág.|
|14/07/14|inc-154-1-01-m-mem-511|inc-154-1-01-m-mem-511|GVF|10/13|

Este documento es propiedad intelectual de Inning Group, no podrá ser utilizado con otro propósito que no sea el estipulado en la relación con el cliente.

_**Mem. Cálculo Hidráulica Sistema Extinción Bodegas**_

Almacenamiento de Sustancias Químicas Peligrosas

**INCOMEX LTDA.**

____________________________________________________________________________________________________________

**Ilustración 1: Esquema simulación red sprinkler bodega inflamables**

**7.2** **Simulación Bodegas No Inflamables**

La simulación de la bodega de no inflamable se ha efectuado con los siguientes elementos:

Cañería entrada hacia bodega: 6” Sch 40

Matriz ramales hacia sprinklers techo: 3” Sch 40

Matriz ramales hacia manguera techo: 3” Sch 40

Cañería hacia manguera: 2 1⁄2”

Material: acero al carbono A-53

|Edición|Proyecto|Tipo Doc.|Por:|Apr.|
|---|---|---|---|---|
|A|DIA Almac. Sustancias Qcas. Peligrosas|Memoria Cálculo|OVR|JRH|
|Fecha|Archivo/Ruta|Archivo/Ruta|Rev.|Pág.|
|14/07/14|inc-154-1-01-m-mem-511|inc-154-1-01-m-mem-511|GVF|11/13|

Este documento es propiedad intelectual de Inning Group, no podrá ser utilizado con otro propósito que no sea el estipulado en la relación con el cliente.

_**Mem. Cálculo Hidráulica Sistema Extinción Bodegas**_

Almacenamiento de Sustancias Químicas Peligrosas

**INCOMEX LTDA.**

____________________________________________________________________________________________________________

**Ilustración 2: Esquema simulación red sprinkler bodegas no inflamables**

**8. RESULTADOS**

**8.1** **Resultados simulación bodega inflamables**

Los resultados de la simulación para la bopdega de inflamables fueron los siguientes:

- Caudal en el sprinkler más lejano en techo: 32,98 gpm.

- Presión en el sprinkler más lejano en techo: 1,4 barg.

- Caudal en el sprinkler más lejano en racks: 30 gpm.

- Presión en el sprinkler más lejano en racks: 2 barg.

- Presión mínima para suministro de agua: 5,3 barg aguas debajo de la válvula Riser

- Caudal en Grifo: 503 gpm

- Presión en manguera: 2,7 barg

- Presión mínima requerida en red principal: 2,8 barg

- Caudal requerido de entrada a bodega: 1460 gpm

|Edición|Proyecto|Tipo Doc.|Por:|Apr.|
|---|---|---|---|---|
|A|DIA Almac. Sustancias Qcas. Peligrosas|Memoria Cálculo|OVR|JRH|
|Fecha|Archivo/Ruta|Archivo/Ruta|Rev.|Pág.|
|14/07/14|inc-154-1-01-m-mem-511|inc-154-1-01-m-mem-511|GVF|12/13|

Este documento es propiedad intelectual de Inning Group, no podrá ser utilizado con otro propósito que no sea el estipulado en la relación con el cliente.

_**Mem. Cálculo Hidráulica Sistema Extinción Bodegas**_

Almacenamiento de Sustancias Químicas Peligrosas

**INCOMEX LTDA.**

____________________________________________________________________________________________________________

**8.2** **Resultados simulación bodega no inflamables**

Los resultados de la simulación para la bodega de inflamables fueron los siguientes:

- Caudal en el sprinkler más lejano en techo: 97,8 gpm.

- Presión en el sprinkler más lejano en techo: 1,6 barg.

- Presión mínima para suministro de agua en la red principal: 3,9 barg

- Caudal hacia manguera: 250 gpm

- Caudal requerido de entrada: 1450 gpm

**9. CONCLUSIONES Y RECOMENDACIONES**

- Se tiene un sistema equilibrado hidráulicamente.

- Los sprinklers se verifican para el caudal y presión mínimo requerido.

- El sistema de apoyo con manguera se verifican para la mínimo y bajo la presión máxima requerida.

- Se recomienda seleccionar una bomba con capacidad de hasta 1250 gpm, dado que en base a lo

establecido en el punto 4.8 de la NFPA 20 (ver 2010) el sistema cumple con esta condición. No obstante se
deberá chequear que las condiciones de instalación sean apropiadas.

|Edición|Proyecto|Tipo Doc.|Por:|Apr.|
|---|---|---|---|---|
|A|DIA Almac. Sustancias Qcas. Peligrosas|Memoria Cálculo|OVR|JRH|
|Fecha|Archivo/Ruta|Archivo/Ruta|Rev.|Pág.|
|14/07/14|inc-154-1-01-m-mem-511|inc-154-1-01-m-mem-511|GVF|13/13|

Este documento es propiedad intelectual de Inning Group, no podrá ser utilizado con otro propósito que no sea el estipulado en la relación con el cliente.