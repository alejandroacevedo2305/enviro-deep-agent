---
title: Sin título
author: Matias Quezada
date: D:20151211124201-03'00'
language: es
type: report
pages: 46
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Solicitado por:
  - Elaborado por:
-->

**DEPARTAMENTO DE OCEANOGRAFÍA FÍSICA Y MODELAMIENTO NUMÉRICO**

### INFORME TÉCNICO

## _“MODELACIÓN NUMÉRICA DE CAMPO CERCANO_ _Y CAMPO LEJANO DE LA DISPERSIÓN DE PLUMA_ _SALINA, PLANTA DESALADORA PISAGUA”_

### _INFORME FINAL_

**Preparado por:**

**- JULIO 2015 -**

**MODELACIÓN NUMÉRICA**

Dispersión Pluma Salina, Pisagua

**DEPARTAMENTO DE OCEANOGRAFÍA FÍSICA Y MODELAMIENTO NUMÉRICO**

# Solicitado por:
## Daes Consultores

#### Casa Central

##### Coronel Pereira 72 of 301, Las Condes. Santiago, Chile.

# Elaborado por:
## EcoTecnos S.A.

#### Casa Central
##### Limache 3405 Oficina 31, Viña del Mar Fonos 56 32 2189200 info@neotecnos.cl

**Control de Documentos**

|Control de Documentos|Col2|Col3|Col4|Col5|
|---|---|---|---|---|
|**Versión**|**Autor**|**Revisión**|**Aprobación**|**Fecha**|
|A|MQL|||14/07/2015|
||||||
||||||

B : Emitido para revisión interna
A : Emitido para aprobación del cliente
0 : Aprobado

**MODELACIÓN NUMÉRICA**

Dispersión Pluma Salina, Pisagua

**DEPARTAMENTO DE OCEANOGRAFÍA FÍSICA Y MODELAMIENTO NUMÉRICO**

## Profesionales Responsables
### EcoTecnos S.A.

**Departamento de Oceanografía Física y Modelamiento Matemático**

### Prof. Dr. Humberto Díaz O.

Dr. en Ingeniería mención Química

### Ing. Sr. Matías Quezada L.

Ingeniero Civil Oceánico, Diploma en Ingeniería Marítima

### Ing. Srta. Pía Monreal D.

Ingeniero Civil Oceánico (e)

**MODELACIÓN NUMÉRICA**

Dispersión Pluma Salina, Pisagua

**DEPARTAMENTO DE OCEANOGRAFÍA FÍSICA Y MODELAMIENTO NUMÉRICO**

**ECOTECNOS S.A.**

Calle Limache N°3405, Oficina 31

Edificio Reitz de las Empresas

El Salto, Viña del Mar, Chile

Este documento fue elaborado por la empresa EcoTecnos S.A. ha requerimiento de Daes
Consultores Ambientales, por lo que solamente puede ser utilizado y reproducido con expresa
autorización de esta última empresa, quedando terminantemente prohibido su copia, reproducción
total o parcial de él, ya que la información contenida en este documento se encuentra protegida,
entre otras normas, por la Ley N° 17.336 sobre Propiedad Intelectual, publicada en el Diario Oficial

N° 27.761, de 2 de octubre de 1970.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|5|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

##### ÍNDICE DE CONTENIDOS

**1** **INTRODUCCIÓN ........................................................................................................ 8**

**2** **OBJETIVOS ............................................................................................................. 10**

**3** **MATERIALES Y MÉTODOS .................................................................................... 11**

3.1 GENERALIDADES .................................................................................... 11

3.2 MATERIALES ........................................................................................... 12

_3.2.1_ _Descripción del modelo numérico RMA10 & 11 ........................................ 12_
_3.2.2_ _Descripción del modelo numérico Visual Plumes ...................................... 14_
3.3 METODOLOGÍA ....................................................................................... 15

_3.3.1_ _Información de campo disponible .............................................................. 17_
_3.3.2_ _Modelación numérica ................................................................................ 18_

_3.3.3_ _Explotación del modelo numérico .............................................................. 19_

**4** **RESULTADOS ......................................................................................................... 24**
4.1 MODELACIÓN NUMÉRICA ...................................................................... 24

_4.1.1_ _Resultados generales calibración/validación ............................................. 24_
4.2 EXPLOTACIÓN DEL MODELO NUMÉRICO ............................................ 27

_4.2.1_ _Hidrodinámica pura (información para simulación del campo cercano) ..... 27_
_4.2.2_ _Modelación de dilución de la sal en el campo cercano .............................. 30_
_4.2.3_ _Modelado de la dispersión de la pluma salina en el campo lejano ............ 35_

**5** **CONCLUSIONES ..................................................................................................... 45**

5.1 Respecto del uso de las herramientas numéricas y métodos aplicados .... 45
5.2 Respecto de la simulación de campo cercano .......................................... 45
5.3 Respecto de la simulación de campo lejano.............................................. 46
5.4 En términos generales .............................................................................. 46

**ANEXO A: CALIBRACIÓN Y VALIDACIÓN DEL MODELO NUMÉRICO**

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|6|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

##### LISTADO DE FIGURAS

Figura 1.1. Identificación de la zona de estudio del Proyecto. ............................................................ 9

Figura 3.1. Esquema metodológico general del estudio de modelación numérica de la pluma salina.

........................................................................................................................................................... 16

Figura 3.2. Metodología detallada de la fase de modelación del estudio en desarrollo. .................. 17

Figura 3.3. Dominio numérico empleado para la simulación de la hidrodinámica en la zona de
Pisagua. A) Distribución de los elementos y B) Batimetría. .............................................................. 18

Figura 4.1. Comparación del nivel del mar medido y simulado en el proceso de calibración. ......... 25

Figura 4.2. Comparación de la velocidad de corriente en la capa de fondo medida y simulada en el
proceso de validación. ....................................................................................................................... 26

Figura 4.3. Resultados típicos de la hidrodinámica pura asociada al escenario 01 de simulación. . 27

Figura 4.4. Perfiles de velocidad en el punto de descarga, asociados a la simulación hidrodinámica
pura de cada uno de los escenarios propuestos. A) Magnitudes de corriente y B) Direcciones. .... 28

Figura 4.5. Geometría de la pluma salina de acuerdo a cada escenario de simulación. ................. 32

Figura 4.6. Pluma salina asociada al Escenario 01. ......................................................................... 37

Figura 4.7. Pluma salina asociada al Escenario 02. ......................................................................... 38

Figura 4.8. Pluma salina asociada al Escenario 03. ......................................................................... 39

Figura 4.9. Pluma salina asociada al Escenario 04. ......................................................................... 40

Figura 4.10. Pluma salina asociada al Escenario 05. ....................................................................... 41

Figura 4.11. Pluma salina asociada al Escenario 06. ....................................................................... 42

Figura 4.12. Pluma salina asociada al Escenario 07. ....................................................................... 43

Figura 4.13. Pluma salina asociada al Escenario 08. ....................................................................... 44

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|7|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

##### LISTADO DE TABLAS

Tabla 3.1. Identificación de los casos a simular para la evaluación de la pluma de salmuera en la
zona de Pisagua. ............................................................................................................................... 20

Tabla 3.2. Identificación de los casos a simular para la evaluación del campo cercano de la pluma

<!-- INICIO TABLA 3.2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Las características ambientales del sector de estudio se definieron en función de la hidrodinámica pura simulada en la fase anterior y la información de campo provista por las campañas de CTDO. De los escenarios de hidrodinámica pura se consideró el perfil de máxima y mínima magnitud de corriente, construyéndose un total de 8 escenarios (ver -->

**Tabla 3.2: ** ).**

| Escenario | Columna de Agua |
| --- | --- |
| E01 | Características de verano |
| E02 | Características de verano |
| E03 | Características de verano |
| E04 | Características de verano |
| E05 | Características de otoño |
| E06 | Características de otoño |
| E07 | Características de otoño |
| E08 | Características de otoño |

<!-- Estadísticas: 8 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- _Fuente: Elaboración Propia_ Las características del emplazamiento del sistema de descarga se consideraron de acuerdo a la información de ingeniería, la cual fue suministrada por Subsea en el plano -->
<!-- FIN TABLA 3.2 -->

de salmuera en la zona de Pisagua .................................................................................................. 21

Tabla 3.3. Características relevantes para cada una de las tuberías de descarga de la salmuera. 22

Tabla 4.1. Perfiles vertical de velocidades de corrientes obtenido desde la simulación de la

hidrodinámica pura y que fue empleado para la modelación de campo cercano en visual plumes. 29

Tabla 4.2. Perfiles vertical de direcciones de corrientes obtenido desde la simulación de la

hidrodinámica pura y que fue empleado para la modelación de campo cercano en visual plumes. 29

Tabla 4.3. Temperatura y salinidad de la columna de agua empleadas en la modelación de campo
cercano de la pluma salina, para cada escenario simulado. ............................................................ 30

Tabla 4.4. Salinidad del efluente en el punto equilibrio de momentum (rango de validez del modelo
de campo cercano) ............................................................................................................................ 33

Tabla 4.5. Distancias esperadas por escenario de simulación para alcanzar el equilibrio salino entre
el efluente y el medio marino. ........................................................................................................... 36

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|8|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**1** **INTRODUCCIÓN**

La necesidad de contar con agua salobre para la minería en el norte de Chile y/o
consumo humado, ha impulsado el desarrollo de múltiples proyectos de plantas
desalinizadoras de agua de mar, la que luego de un proceso químico es descargada al
mar como un fluido con exceso de sal, el cual necesariamente debe interactuar con su
medio receptor.

En el proceso de descarga del referido fluido con exceso de sal hacia el medio receptor,
es de interés ambiental conocer su comportamiento tridimensional, es decir, cómo es la
interacción de este vertimiento en la vertical y en la horizontal, en un mismo instante de
tiempo tanto en escalas de mezcla turbulenta como advectiva. Sin embargo, en la
mayoría de las ocasiones es práctica usual en la ingeniería simular ambos procesos por
separado, en lo que comúnmente se llama campo cercano y lejano.

La modelación de campo cercano corresponde al proceso en el cual se estima la
capacidad del medio de diluir por procesos físicos de corta escala, es decir, en las
inmediaciones de la descarga (mezcla turbulenta preferentemente). Por otra parte, el
campo lejano comprende los procesos de dilución asociados al proceso de advección que
la hidrodinámica genera sobre el efluente.

EcoTecnos S.A. ha sido contratado para la realización de un estudio numérico orientado a
simular el comportamiento de campo cercano y lejano de la descarga de fluido con
exceso de sal, proveniente desde el sistema de desalinización de la planta desalinizadora
de Pisagua, Región de Tarapacá, de acuerdo a lo indicado en la Figura 1.1.

En el presente informe, se exponen los métodos aplicados, describiendo tanto las
herramientas de simulación como los datos de campo disponibles para el desarrollo del
estudio. Posteriormente, son presentados los resultados obtenidos y las conclusiones que
se logran, a partir de ellos.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓ<br>1/1|N<br>9<br>.|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A|Emitido por:<br>EcoTecnos S.A|

_Fuente: Elaboración Propia_
**Figura 1.1.** Identificación de la zona de estudio del Proyecto.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|10|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**2** **OBJETIVOS**

El objetivo general del presente estudio es evaluar el comportamiento de la pluma salina,
debido al proceso de desalinización que se llevará a cabo en la planta proyectada por
Aguas del Altiplano, mediante la aplicación conjunta de herramientas numéricas e
información de campo.

Para lograr el cumplimiento del antes mencionado objetivo, se procedió a desarrollar las
siguientes actividades específicas:

 Análisis general de los datos de campo, para la obtención de forzantes y
características base del cuerpo receptor.

 Calibración y validación de las herramientas numéricas utilizadas.

 - Simulación numérica de la hidrodinámica base.

 Simulación numérica de la hidrodinámica de operación.

 Simulación numérica de la pluma salina.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|11|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**3** **MATERIALES Y MÉTODOS**

**3.1** **GENERALIDADES**

La modelación numérica de la dispersión de algún elemento en el medio marino, es un
proceso complejo y requiere de una correcta selección de herramientas de simulación en
función del tipo de efluente que esté en análisis, siendo los más comunes:

 - Aguas con exceso de calor: usualmente provenientes desde sistemas de
enfriamiento de centrales termoeléctricas.

 - Aguas con exceso de sal: usualmente provenientes desde plantas
desalinizadora.

 - Aguas con presencia de agentes bacterianos: usualmente provenientes desde
plantas de tratamientos de aguas servidas.

Independiente de la característica del efluente que se requiera simular, es práctica usual
en este tipo de estudios desarrollar dos modelaciones acopladas. La primera consiste en
determinar qué sucede en las cercanías del punto (s) de descarga (s), la cual es
denominada “simulación del campo cercano” y está orientada principalmente a estimar los
efectos en la vertical y físicamente está dominada por procesos de dilución asociados a la
dinámica de la turbulencia de chorro inducida por los difusores o sistemas similares.

Posteriormente, con la vertical estabilizada en su equilibrio de momentum, es decir, el
punto dónde la velocidad del efluente se iguala a la del medio receptor, quedando la
dinámica dominada por los procesos de advección y difusión; se realiza la modelación
para ver su dispersión en planta, la cual es denominada “simulación de campo lejano” y
fundamentalmente se ejecuta para estimar la cobertura espacial que tendrá la pluma.

Para desarrollar la modelación numérica de la pluma salina proveniente desde la planta
desalinizadora de Pisagua, se ha propuesto una metodología que enfrenta el problema
considerando tanto el campo cercano como el lejano, mediante la utilización conjunta de
información de terreno y herramientas para la simulación.

Tanto la información de campo disponible como los modelos numéricos a utilizar son
descritos en la presente sección del estudio, individualizando los materiales y metodología
propiamente tal.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|12|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**3.2** **MATERIALES**

Para el desarrollo de la simulación numérica se emplearon dos modelos, uno para
representar el campo cercano denominado Visual Plumes y otro para simular el campo
lejano conocido como RMA10 & 11.

**3.2.1 Descripción del modelo numérico RMA10 & 11**

El conjunto de modelos RMA10 y 11, han sido elaborados para la simulación numérica de
la hidrodinámica de flujos estratificados (3D) y la calidad de aguas asociada a dicha
condición de flujo.

RMA10 es un modelo de elementos finitos tridimensional que ha sido elaborado para
simular la hidrodinámica en flujos estratificados. Desde un punto de vista numérico, tiene
las capacidades de construir grillas de elementos triangulares o cuadriláteros, con 6 u 8
nodos de solución de los sistemas de ecuaciones por cada elemento respectivamente. En
la vertical la discretización es realizada en coordenadas sigma.

El modelo RMA10 resuelve las ecuaciones de Reynolds derivadas desde las
formulaciones de Navier-Stokes en flujo estratificado, asumiendo una distribución
hidrostática de presiones en la vertical.

El sistema de ecuaciones que se resuelve, se presenta a continuación:

ρ [∂u]

[∂u]

∂t [+ ρu∂u] ∂x

[∂v]

∂t [+ ρu∂v] ∂x

∂y [+ ρw∂u] ∂z

∂y [+ ρw∂v] ∂z

∂z [−∂]

∂z [−∂] ∂x

∂x [(ε] [xx]

∂x [(ε] [yx]

∂u
∂x ~~[)]~~ [ −∂] ∂y [(ε] [xy]

∂u
∂x ~~[)]~~ [ −∂]

∂v
∂x ~~[)]~~ [ −∂] ∂y [(ε] [yy]

∂v
∂x ~~[)]~~ [ −∂]

∂u
∂y ~~[)]~~ [ −∂] ∂z [(ε] [xz]

∂u
∂z ~~[)]~~ [ + ∂p] ∂x [−τ] [x] [= 0]

ρ [∂v]

∂x [+ ρv∂u] ∂y

∂x [+ ρv∂v]

∂v
∂y ~~[)]~~ [ −∂] ∂z [(ε] [yz]

∂v
∂z ~~[)]~~ [ + ∂p] ∂y [−τ] [y] [= 0]

∂yp

∂z [−τ] [z] [= 0]

∂u
∂x [+ ∂v]

∂y [+ ∂w] ∂z

∂z [= 0]

ρC T

[ [∂T] ∂t

[∂T] ∂t [+ u∂T] ∂x

∂x [+ v∂T]

∂y [+ w∂T] ∂z

∂z [−∂]

∂x [(D] [x]

∂T
∂x ~~[)]~~ [ −∂] ∂y [(D] [y]

∂T
∂x ~~[)]~~ [ −∂]

∂T
∂y ~~[)]~~ [ −∂] ∂z [(D] [xz]

∂T

∂z [)] −θ] [s] [= 0]

Dónde:

x, y, z : Coordenadas cartesianas.
 : Densidad.
 xx : Coeficientes de turbulencia de Eddy.
T : Temperatura.
u, v, z : Velocidades de la corriente en x, y, z; respectivamente.
p : Presión.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|13|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

D x, D y : Coeficientes de difusión del calor.
 x,y,z : Forzantes externas.
 s : Término fuente o sumidero ( _source or sink_ ).

RMA11 es un modelo tridimensional en elementos finitos de calidad de aguas, que actúa
sobre una base hidrodinámica (campo de velocidades y direcciones) de una determinada
área (la que en este caso es proporcionada por el modelo RMA 10).

Las ecuaciones de gobierno se basan en la de continuidad y transporte de cada
constituyente, las que se describen de manera general a continuación:

Ecuación de continuidad:

h
~~(~~ [∂u] ∂x

[∂u] ∂x [+ ∂v]

∂y [) + (r−a) ∂w] ∂z

∂z [−(r−a) (T] [x]

∂v
∂z ~~[)]~~ [ −hq] [0] [ = 0]

∂u
∂z [+ T] [y]

Ecuación de transporte de constituyentes:

[∂C]

∂t [+ h∂(uC)] ∂x

+ (r−a) [∂(wC)]
∂y ∂z

∂z −(r−a)T x

∂(vC)

∂z

h [∂C]

+ h [∂(vC)]
∂x

∂(uC)

∂z −(r−a)T y

−(z−a) [∂h]

∂t

∂C

∂C

∂z [−h∂]

∂x [(D] [x]

∂C
∂x [+ D] [xy]

∂x [(r−a] h

∂
∂z [(r−a] h

h {D x T x + D xy T y } [∂C] ∂z

h {D x T x + D xy T y } [∂C] ∂z

∂C
∂y ~~[)]~~ [ + h∂]

∂z ~~[)]~~

[∂C]

∂z ~~[)]~~

∂C
∂x [+ D] [xy]

∂C
∂y ~~[)]~~ [ −(r−a)T] [x]

+ (r−a)T x

−h [∂]

∂y [(D] [xy]

+ (r−a)T y

∂
∂z [(D] [x]

∂C
∂x [+ D] [y]

∂
∂z [(D] [xy]

∂C
∂x [+ D] [y]

∂C
∂y ~~[)]~~ [ + h∂]

h {D xy T x + D y T y } [∂C] ∂z

∂y [(r−a] h

∂z ~~[)]~~

∂C
∂y ~~[)]~~ [ −(r−a)T] [y]

∂
∂z [(r−a] h

h {D xy T x + D y T y } [∂C] ∂z

∂z ~~[)]~~

−(r−a) [∂]

∂z [(D] [z]

r−a

h

∂C

∂z ~~[)]~~ [ −KhC−hθ] [s] [−(r−a) ∂(V] ∂z [s] [C)]

∂C

= 0
∂z

Dónde:

C : Concentración.
q 0 : Flujo de entrada por unidad de volumen.
r−a : Profundidad de cómputo.
D : Coeficiente de mezcla turbulenta.

K : Coeficiente de decaimiento.

Los términos T x y T y, se definen de acuerdo a:

T x = [∂x [∂a]

∂a z−a [h∂a]
∂x [+] (r−a) [2] ∂x []]

∂a z−a [h∂a]
∂y [+] (r−a) [2] ∂y ~~[]]~~

∂x [+ z−a] r−a

r−a

T
y
= [ [∂a] ∂y

∂y [+ z−a] r−a

r−a

∂h h
∂x [−] r−a

∂h h
∂y [−] r−a

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|14|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**3.2.2 Descripción del modelo numérico Visual Plumes**

Simular las condiciones en la zona de descarga es fundamental para conocer el
comportamiento del efluente en la columna de agua, además del comportamiento de la
pluma en el campo cercano.

Para realizar este tipo de simulación se ha utilizado el programa VISUAL PLUMES (VP)
v1.0, desarrollado por The United States Environmental Protection Agency. Éste incorpora
modelos que tienen la capacidad simular plumas sumergidas simples y múltiples en un
ambiente estratificado y descargas boyantes en la superficie en el campo cercano,
considerando las condiciones ambientales del medio receptor.

Visual Plumes tiene como una de sus capacidades la utilización de un módulo
denominado UM3 (Three Dimensional Update Merge), el cual es de tipo lagrangiano y
simula una descarga por medio de una o más puertas sumergidas, las cuales están en
función de las características de la descarga y del medio ambiente (Frick et al., 2003).

El modelo UM3 se caracteriza de tres puntos importantes para resolver el comportamiento
de la descarga en el medio receptor:

 Hipótesis del área proyectada del PAE (Projected Area Entrainment), la cual
cuantifica la fuerza (Rawn et al., 1960).

 - Tasa en que la masa de la pluma es incorporada a la corriente asumiendo que
la pluma está en un estado estacionario y,

 Formulación lagrangiana, la cual implica que sucesivos elementos siguen la
misma trayectoria (Baumgartner et al., 1994).

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|15|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**3.3** **METODOLOGÍA**

La zona de estudio corresponde a un sector costero de Pisagua (ver Figura 1.1), en la
Región de Tarapacá, área que se ha caracterizada por un alto valor histórico.

La geomorfología costera del sector de estudio se caracteriza por la presencia de Punta
Pichalo el que actúa sobre una parte de la Playa de Pisagua como agente controlador de
la hidrodinámica, siendo una barrera natural para el oleaje proveniente desde el tercer
cuadrante de direcciones, induciendo difracción y mermando de este modo las alturas de
ola a lo largo del litoral para esta procedencia, sin disminuirlas completamente.

La circulación costera de un determinado sector depende principalmente de la
profundidad del mar a la cual se realicen los análisis, ya que a medida que se acerca a la
zona de rompiente, la hidrodinámica comienza a depender fuertemente de las corrientes
inducidas por oleaje, mientras que fuera de ella usualmente la marea, vientos y otros
efectos sinópticos tienen una acción preponderante.

De acuerdo a las características proyectadas de la descarga de salmuera, ésta se
emplazará en profundidades en torno a los 5 metros, lugar en el cual es posible presumir
que las condiciones de oleaje están en la zona de rompientes, sin embargo, al ser estas
de alturas bajas, sus efectos son puntuales y no tendrían gran capacidad de transporte
advectivo de aguas con exceso de salinidad, por tanto la circulación inducida por esta
forzante sería poco significativa.

De este análisis preliminar y conceptual de la zona de estudio, se advierte que serían
principales forzantes las siguientes:

 - Mareas.

 - Vientos

 - Otros efectos a escala sinóptica.

Para desarrollar el presente estudio, se ha propuesto la aplicación de una serie de
modelaciones numéricas, las cuales persiguen representar de manera adecuada las
condiciones, tanto de campo cercano, como de campo lejano o hidrodinámico.

Para la simulación del campo cercano, se ha propuesto la utilización del modelo numérico
Visual Plumes; mientras que, para los objetivos del campo lejano, se empleará el modelo
RMA, con sus módulos 10 y 11, los cuales incorporan la simulación conjunta de la
hidrodinámica tridimensional (10) y la dispersión de sustancias contaminantes (11).

La estrategia de modelación aplicada contempla la utilización conjunta de las antes
indicadas herramientas numéricas y de los datos de campo, lo que se entrelazan de
acuerdo a lo señalado en la **Figura 3.1** .

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|16|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

De esta forma, en la comentada figura, se ha considerado un código de colores, los que
se describen los siguientes procesos:

 - **Tonalidades verdes** : Corresponden a las tareas propias del estudio en desarrollo.

 - **Tonalidades rojas** : Corresponde a los datos de entrada, empleados en cada tarea

del estudio.

 - **Tonalidades azules** : Corresponde a los resultados esperados para cada tarea, los
que en ocasiones son datos de entrada para las siguientes tareas.

Así, la modelación numérica se desarrolló considerando un proceso de calibración y
validación, mediante datos obtenidos en terreno (datos de campo), tanto para representar
de manera adecuada los cambios del nivel del mar, como para las corrientes del área de
estudio. Posteriormente, se dispuso de la herramienta de simulación para la fase de
explotación:

_Fuente: Elaboración Propia_
**Figura 3.1.** Esquema metodológico general del estudio de modelación numérica de la

pluma salina.

La fase de explotación del modelo numérico, fue extensa y contempló el desarrollo de
tareas complementarias, las que se implementaron de acuerdo a lo mostrado en la **Figura**
**3.2** .

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|17|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

_Fuente: Elaboración Propia_
**Figura 3.2.** Metodología detallada de la fase de modelación del estudio en desarrollo.

A continuación, se describe, de manera detallada, cada una de las actividades que se
desarrollaron con el objeto de lograr el modelamiento propuesto.

**3.3.1 Información de campo disponible**

Para el desarrollo del presente estudio, se dispuso de información de campo proveniente
de campañas de terreno de otoño y verano, la cual fue procesada previamente en los
informes de línea base ambiental elaboradors por Ecotecnos S.A. para Daes Consultores
ambientales.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|18|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**3.3.2 Modelación numérica**

_**3.3.2.1 Configuración general del modelo numérico RMA10**_

Para la realización de la calibración, validación y posterior explotación del modelo
numérico, se construyó una malla de 1.873 elementos y 1.021 nodos. Del dominio
utilizado abarcó profundidades desde 355,0 hasta 0,0 metros respecto del NRS y tuvo una
cobertura de acuerdo a lo mostrado en la **Figura 3.3** .

Desde el punto de vista numérico, se utilizó un paso temporal de 10 segundos, en función
de obtener una estabilidad con número courant máximo de 0,8, implementando un
algoritmo de celdas húmedas y secas en los bordes de tierra.

Se debe tener presente que en modelamiento numérico, el número de courant relaciona la
velocidad de cálculo con la velocidad de propagación del fenómeno estudiado. De esta
forma, atendiendo a las características aplicadas al presente estudio, se esperaba que
este número hubiere sido menor o igual a 1,0, para así obtener los resultados de la
simulación convergente y concordante, con los que esperado en la realidad.

Por otra parte, un algoritmo de celdas húmedas y secas, corresponde a un criterio de
decisión numérica, en el cual el modelo realiza inundación virtual hacia fuera del dominio
numérico, es decir, libera cierta cantidad de agua hacia el sector exterior de la zona
simulada, con la finalidad de evitar desnivelaciones del nivel del mar excesivamente
grandes en los contornos duros del modelo (bordes de tierra y fronteras oceánicas).

_Fuente: Elaboración Propia_
**Figura 3.3.** Dominio numérico empleado para la simulación de la hidrodinámica en la

zona de Pisagua. A) Distribución de los elementos y B) Batimetría.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|19|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

_**3.3.2.2 Calibración y Validación del modelo numérico RMA10**_

En el ámbito de la modelación numérica, es común utilizar dos términos convencionales:
calibración y validación. El primero de ellos corresponde al proceso en el cual los modelos
numéricos son ajustados mediante la modificación de coeficientes y parámetros para
poder representar las condiciones de terreno que han sido medidas previamente.

Por su parte, la validación corresponde a la simulación de un segundo periodo de tiempo,
diferente al de la calibración, en el cual se verifican los supuestos y modificaciones
implementadas previamente.

Considerando los datos de terreno disponible, que consistieron en mareas y corrientes de
dos campañas de mediciones, fue posible realizar tanto la calibración como la validación
del modelo RMA10.

Los detalles del proceso de calibración y validación, se presentan en el **Anexo A** .

**3.3.3 Explotación del modelo numérico**

La fase de explotación del modelo numérico correspondió a la etapa del proyecto en la
cual, mediante la base hidrodinámica calibrado y validado, se simuló un set de
características para determinar el funcionamiento hidráulico marítimo de la zona de
estudio.

Las simulaciones estuvieron orientadas a caracterizar la condición base, es decir, sin
considerar el funcionamiento de la planta. Posteriormente, se realizó la modelación de

campo cercano.

Con la información proveniente desde el campo cercano y la hidrodinámica operacional,
se simuló la dispersión de la pluma salina en el medio marino.

En los siguientes apartados se describe de manera ampliada la metodología aplicada en
cada una de las fases de explotación del modelo numérico.

_**3.3.3.1 Definición de la hidrodinámica pura**_

La definición de la hidrodinámica pura, tuvo como objetivo principal caracterizar la
circulación de Pisagua sin considerar la presencia de descargas u otro tipo de estructuras
que modifiquen el comportamiento natural de la zona de estudio.

En virtud de que se ha establecido, preliminarmente, que las mareas y el viento serían las
principales forzantes que dominan la hidrodinámica del sector, fuera de la zona de

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|20|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

rompientes de oleaje, se ha considerado en el caso de la marea, las fluctuaciones del
nivel del mar cuya probabilidad de ocurrencia sea suficientemente alta, de modo de
suceder de forma conjunta con los vientos más frecuentes.

Considerando la información del nivel del mar, proveniente desde las mediciones, se
determinó el ciclo medio diario de mareas de sicigia y cuadratura, tanto para la estación
de verano, como de invierno. De este modo, se definieron 4 curvas de mareas, de 24

horas de duración cada una de ellas.

En el caso de los vientos, se determinó el ciclo medio y máximo tanto para la estación de
verano como la de invierno, definiendo de esta manera 4 curvas de 24 horas de duración

cada una de ellas.

La combinación en escenarios de cada una de estas series de tiempo, se muestra en la
**Tabla 3.1.**

**Tabla 3.1.** Identificación de los casos a simular para la evaluación de la pluma de

salmuera en la zona de Pisagua.

|Escenario|Marea|Viento|
|---|---|---|
|E01|Ciclo diario de sicigias|Ciclo diario medio de vientos de verano|
|E02|Ciclo diario de cuadraturas|Ciclo diario medio de vientos de verano|
|E03|Ciclo diario de sicigias|Ciclo diario máximo de vientos de verano|
|E04|Ciclo diario de cuadraturas|Ciclo diario máximo de vientos de verano|
|E05|Ciclo diario de sicigias|Ciclo diario medio de vientos de invierno|
|E06|Ciclo diario de cuadraturas|Ciclo diario medio de vientos de invierno|
|E07|Ciclo diario de sicigias|Ciclo diario máximo de vientos de invierno|
|E08|Ciclo diario de cuadraturas|Ciclo diario máximo de vientos de invierno|

_Fuente: Elaboración Propia_

El modelo se configuró de igual manera que en la calibración y validación, para obtener
las velocidades de corriente (dirección y magnitud) en la columna de agua para el punto
de descarga, cada 10 minutos. Posteriormente, se obtuvieron los perfiles de corriente
promedio, tanto en cuadratura como en sicigia.

Los perfiles de velocidad promedio de cada uno de los 8 escenarios de simulación, se
incorporaron en el modelo de campo cercano.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|21|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

_**3.3.3.2 Modelación de campo cercano**_

La modelación del campo cercano, tuvo como finalidad determinar la geometría de la
pluma de descarga y el punto en el cual el efluente queda solamente expuesto al efecto
de la advección inducida por el comportamiento hidrodinámico de la Bahía.

Para la ejecución de esta fase se consideraron dos fuentes de información principal, la
primera consistió en las condiciones ambientales del sector y la segunda a las
características geométricas e hidráulicas del sistema de descarga.

Las características ambientales del sector de estudio se definieron en función de la

hidrodinámica pura simulada en la fase anterior y la información de campo provista por las
campañas de CTDO. De los escenarios de hidrodinámica pura se consideró el perfil de
máxima y mínima magnitud de corriente, construyéndose un total de 8 escenarios (ver
**Tabla 3.2** ).

**Tabla 3.2.** Identificación de los casos a simular para la evaluación del campo cercano de

la pluma de salmuera en la zona de Pisagua

|Escenario|Columna de Agua|
|---|---|
|E01|Características de verano|
|E02|Características de verano|
|E03|Características de verano|
|E04|Características de verano|
|E05|Características de otoño|
|E06|Características de otoño|
|E07|Características de otoño|
|E08|Características de otoño|

_Fuente: Elaboración Propia_

Las características del emplazamiento del sistema de descarga se consideraron de
acuerdo a la información de ingeniería, la cual fue suministrada por Subsea en el plano
SS-PDP-22-01 Arreglo General Rev.1-Layout1.pdf; mientras que la información de la
operación y geometría se suministró vía correo electrónico, siendo resumida en la **Tabla**
**3.3.**

De esta forma, los resultados fueron procesados, para obtener el punto de equilibrio de
momentum, en orden de definir la concentración de sal que comienza a moverse por
proceso de advección.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|22|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**Tabla 3.3.** Características relevantes para cada una de las tuberías de descarga de la

salmuera.

|Parámetro|Unidad|Valor|
|---|---|---|
|Longitud del difusor|m|5|
|Diámetro de tubería de difusión (ID)|mm|160|
|Profundidad descarga|mNRS|4|
|Número de puertas|-|5|
|Espaciamiento entre puertas|m|2|
|Diámetro de puertas|mm|50|
|Ángulo vertical|°|45|
|Caudal efluente|L/s|5|
|Exceso de Salinidad efluente|%|50|

_Fuente: Elaboración Propia_

_**3.3.3.3 Definición de la hidrodinámica operacional**_

El objetivo principal de la definición de la hidrodinámica operacional es construir una base
numérica de la circulación en Pisagua, sobre la cual posteriormente evaluar la capacidad
de dispersión del efluente con exceso de sal.

La modelación de la hidrodinámica operacional, se ejecutó bajo las mismas
características que la circulación pura descrita previamente; sin embargo, se ha
incorporado el efecto de la descarga en el medio en lo relativo a las corrientes de agua
inducidas al medio. Bajo este nueva configuración (términos fuente incluido), se simularon
los 8 escenarios descritos en la **Tabla 3.1**, considerando un caudal de operación
constante en el tiempo.

Numéricamente, se ubicó el punto de descarga en la capa 1 de la malla vertical en
coordenadas sigma que se construyó, es decir, en las proximidades del lecho marino.

_**3.3.3.4 Modelado de la dispersión de la pluma salina**_

El objetivo principal de la modelación de la dispersión de la pluma salina fue determinar el
máximo alcance que ésta tendrá (campo lejano), antes de igualar su salinidad con la del
cuerpo receptor.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|23|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

Se configuró en cada uno de los escenarios simulados en la definición de la hidrodinámica
operacional, la descarga de efluente con la temperatura indicada en la **Tabla 3.3** y
salinidad de acuerdo al resultado de equilibrio de momentum obtenido en la simulación de
campo lejano.

Los resultados obtenidos fueron procesado e ilustrados para identificar el comportamiento
de la pluma salina en tres capas a lo largo de la columna de agua, siendo estas: fondo,
intermedia y superficial.

_**3.3.3.5 Salinidad límite en el medio marino**_

En la actualidad Chile no cuenta con ninguna normativa o recomendación de la salinidad
en el medio marino que no afecte el comportamiento de los agentes biológicos presente
en estos cuerpos de agua, por lo que definir límites operativos y/o de bajo impacto en el
medio se torna complejo y usualmente se debe recurrir a normativas internacionales. Para
efectos del presente estudio se ha empleado la recomendación de la **AUSTRALIAN**
**WATER QUALITY GUIDELINES FOR FRESH AND MARINE WATERS. 1992,** quien fija
como cota máxima un aumento del 5% de la salinidad natural del medio por efectos de la
descarga de salmuera proveniente desde la planta.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|24|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**4** **RESULTADOS**

**4.1** **MODELACIÓN NUMÉRICA**

**4.1.1 Resultados generales calibración/validación**

Conforme se expone en la **Figura 4.1 y 4.2**, es posible apreciar los resultados típicos que
son obtenidos a partir de la calibración/validación del modelo RMA10, para el campo de
corrientes en el sector de Pisagua.

La **Figura 4.1** muestra la comparación de las series de tiempo de desnivelación del mar
para el proceso de calibración, de las cuales se advierte que existe una alta similitud entre
los resultados del modelo numérico y las mediciones realizadas. El coeficiente de
calibración obtenido fue de 99,7%.

Las corrientes en la capa de fondo para el proceso de validación, son mostradas en la
**Figura 4.2** y de la cual se aprecian que el modelo numérico representaría de manera
adecuada las magnitudes. La correlación alcanzada para esta comparación de las series
de tiempo fue de 94,1%.

Los detalles del proceso de calibración y validación, así como también las comparaciones
de todas las series de tiempo, se presentan en el **Anexo A** .

_Fuente: Elaboración Propia_

**Figura 4.1.** Comparación del nivel del mar medido y simulado en el proceso de calibración.

_Fuente: Elaboración Propia_

**Figura 4.2.** Comparación de la velocidad de corriente en la capa de fondo medida y simulada en el proceso de validación.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|27|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**4.2** **EXPLOTACIÓN DEL MODELO NUMÉRICO**

**4.2.1 Hidrodinámica pura (información para simulación del campo cercano)**

Resultados típicos de las simulaciones hidrodinámicas para el escenario 01 se muestran
en la **Figura 4.3**, tanto para la capa superficial, media y fondo. Del análisis general del
instante de tiempo ilustrado, se advierte que las mayores magnitudes de las corrientes se
producen en las cercanías de la costa y van disminuyendo en función que aumenta la
profundidad, es decir, a medida que se aleja del borde costero.

Para la ubicación de la descarga de salmuera (línea de color verde en la Figura 4.3), se
aprecia que las corrientes van hacia el Nor-Este (aproximadamente) con magnitudes del
orden de 0,2 a 0,3 m/s.

_Fuente: Elaboración Propia. Sistema coordenado: UTM-WGS84, HUSO 19._

**Figura 4.3.** Resultados típicos de la hidrodinámica pura asociada al escenario 01 de

simulación.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|28|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

Los resultados obtenidos de la extracción de los perfiles verticales de velocidades medios
en sicigia y cuadratura, para cada uno de los escenarios simulados, se muestran en la
**Figura 4.4** .

En términos generales los perfiles de velocidades desarrollaron una distribución cuasiparabólica con mayores magnitudes en superficie (debido a la acción forzante del viento),
siendo esperables las menores velocidades para el escenario 06 (del orden de 0,44 m/s
en superficie) y las mayores para el escenario 4 (del orden de 0,48 m/s en superficie)

El comportamiento del perfil vertical de las direcciones matemáticas de la corriente mostro
una variabilidad desde los 39,5o (caso E02) hasta los 42o (E05). En general las
distribuciones fueron similares, con leve tendencia a la rotación en las cercanías del
lecho, situación que es esperable, dada la interacción de la hidrodinámica con el fondo.

En función de los resultados obtenidos y recientemente comentados, se espera que la
selección de escenarios de velocidad de corriente al ser empleados en la modelación de
campo cercano, produzca una variación representativa de la salinidad del efluente al
incorporarse al medio, en lo relativo a la distancia recorrida por el chorro en el cuerpo
receptor para igualar sus propiedades con las del medio.

Se debe entender como distancia de incorporación a aquel tramo que el efluente
proveniente desde la descarga recorre en el medio marino, antes de verse sometido a la
acción del campo de velocidades propias de Pisagua, es decir, hasta el instante en que el
chorro emanado desde los difusores deja de moverse como un cuerpo libre y pasa a
desplazarse debido a la acción de las corrientes marinas.

Importante es destacar que desde un punto de vista del funcionamiento hidráulico del
sistema, una menor distancia de incorporación del efluente en el medio, producirá
teóricamente una menor disminución de su salinidad debido a la baja acción de la mezcla
turbulenta, por lo cual en la simulación de campo lejano es de esperar que la descarga
comenzará en un mayor estado salino.

_Fuente: Elaboración Propia_

**Figura 4.4.** Perfiles de velocidad en el punto de descarga, asociados a la simulación
hidrodinámica pura de cada uno de los escenarios propuestos. A) Magnitudes de corriente

y B) Direcciones.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|29|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

En la **Tabla 4.1**, se presentan las magnitudes de cada uno de los perfiles de cada uno de
los escenarios simulados, que serán empleados en la modelación de campo cercano,
mientras que la dirección matemática asociada, se indican en la **Tabla 4.2** .

**Tabla 4.1.** Perfiles vertical de velocidades de corrientes obtenido desde la simulación de
la hidrodinámica pura y que fue empleado para la modelación de campo cercano en visual

plumes.

|Profundidad<br>(m)|E01<br>(m/s)|E02<br>(m/s)|E03<br>(m/s)|E04<br>(m/s)|E05<br>(m/s)|E06<br>(m/s)|E07<br>(m/s)|E08<br>(m/s)|
|---|---|---|---|---|---|---|---|---|
|0,0|0,469|0,480|0,470|0,482|0,458|0,445|0,464|0,455|
|0,5|0,469|0,479|0,470|0,482|0,457|0,444|0,464|0,454|
|1,0|0,467|0,477|0,469|0,481|0,456|0,443|0,464|0,453|
|1,5|0,466|0,475|0,468|0,479|0,455|0,441|0,463|0,452|
|2,0|0,464|0,474|0,467|0,478|0,453|0,439|0,461|0,450|
|2,5|0,463|0,472|0,465|0,477|0,451|0,437|0,460|0,449|
|3,0|0,461|0,470|0,464|0,475|0,450|0,436|0,459|0,448|
|3,5|0,459|0,468|0,463|0,474|0,448|0,434|0,458|0,446|
|4,0|0,458|0,466|0,462|0,473|0,446|0,432|0,457|0,445|
|4,5|0,453|0,465|0,458|0,471|0,442|0,430|0,456|0,443|
|5,0|0,444|0,458|0,448|0,465|0,433|0,430|0,456|0,444|

_Fuente: Elaboración Propia_

**Tabla 4.2.** Perfiles vertical de direcciones de corrientes obtenido desde la simulación de la

hidrodinámica pura y que fue empleado para la modelación de campo cercano en visual

plumes.

|Profundidad<br>(m)|E01 (o)|E02 (o)|E03 (o)|E04 (o)|E05 (o)|E06 (o)|E07 (o)|E08 (o)|
|---|---|---|---|---|---|---|---|---|
|0,0|40,136|39,629|40,137|39,689|41,524|40,972|41,068|40,541|
|0,5|40,169|39,644|40,162|39,699|41,592|41,017|41,101|40,559|
|1,0|40,201|39,661|40,187|39,712|41,655|41,062|41,131|40,581|
|1,5|40,243|39,694|40,221|39,740|41,728|41,127|41,172|40,622|
|2,0|40,289|39,727|40,260|39,770|41,805|41,192|41,218|40,664|
|2,5|40,335|39,760|40,299|39,799|41,881|41,257|41,263|40,705|
|3,0|40,381|39,793|40,337|39,828|41,958|41,322|41,309|40,746|
|3,5|40,427|39,826|40,376|39,857|42,035|41,387|41,354|40,788|
|4,0|40,472|39,858|40,415|39,886|42,112|41,452|41,400|40,829|
|4,5|40,223|39,891|40,166|39,915|41,889|41,517|41,436|40,870|
|5,0|39,520|39,360|39,473|39,396|41,204|41,579|41,594|40,910|

_Fuente: Elaboración Propia_

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|30|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**4.2.2 Modelación de dilución de la sal en el campo cercano**

Para realizar el modelamiento de campo cercano, se utilizó la caracterización de la
columna de agua, en función de los perfiles promedio otoño (para invierno) y verano (para
verano), correspondientes al eje adyacente a la zona de descarga y cuyos resultados se
presentan en la **Tabla 4.3** .

Las curvas de salinidad promedio, para la columna de agua, permitieron advertir una
uniformidad, tanto para la condición de otoño, como la de verano, con valores entorno de
los 34,9 psu. En el caso de las temperaturas, las variaciones no superaron 1oC, siendo
indicador de una baja estratificación.

**Tabla 4.3.** Temperatura y salinidad de la columna de agua empleadas en la modelación

de campo cercano de la pluma salina **,** para cada escenario simulado.

|Profundidad (m)|Escenario 01, 02, 03 y 04|Col3|Escenario 05, 06, 07 y 08|Col5|
|---|---|---|---|---|
|**Profundidad (m)**|**Salinidad**<br>**(psu)**|**Temperatura**<br>**(°C)**|**Salinidad**<br>**(psu)**|**Temperatura**<br>**(°C)**|
|0,0|34,969|15,431|34,961|16,092|
|0,5|34,969|15,431|34,961|16,092|
|1,0|34,972|15,355|34,968|16,087|
|1,5|34,944|15,311|34,973|16,080|
|2,0|34,944|15,264|34,980|16,073|
|2,5|34,955|15,150|34,989|16,059|
|3,0|34,948|15,058|34,992|16,046|
|3,5|34,951|15,031|34,984|16,036|
|4,0|34,961|15,038|34,980|16,028|
|4,5|34,969|15,431|34,963|16,026|
|5,0|34,972|15,431|34,957|16,024|

_Fuente: Elaboración Propia_

A su vez, en la **Figura 4.5,** se presentan los resultados asociados a la geometría
esperada de la pluma salina en los 8 casos simulados, considerando el eje medio de la
pluma.

De esta forma, la geometría descrita por la pluma salina, según los resultados obtenidos,
permiten demostrar un comportamiento compatible con lo reportado en la literatura por
diversos autores, siendo destacables los siguientes puntos:

 - En los primeros metros de distancia, con respecto del punto de descarga, la pluma
salina tiene una tendencia a subir. Este ascenso, es impuesto principalmente por
el caudal de salida del efluente y la orientación del difusor o tubería de descarga,
denominado ascenso turbulento.

 Posteriormente, la energía cinética del efluente, ocasiona una disminución del flujo
hasta cero, por lo cual deja de subir la pluma en la columna de agua. A partir de

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|31|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

este punto se genera una inflexión que impulsa el descenso gravitacional, debido a
la mayor salinidad del vertido respecto del ambiente.

 Una vez descendido el efluente, comienza su desplazamiento por el fondo, el que
puede ser impulsado por las corrientes del ambiente costero o por la gravedad.

En términos generales, se logra advertir que la descarga de salmuera alcanza una mayor
altura cuando la condición hidrodinámica del ambiente está en mínima magnitud (líneas
azules), lo que se debería principalmente a la menor resistencia hidráulica que impone el
medio sobre el chorro de agua. En el caso de las máximas velocidades de corriente
(líneas roja), se puede apreciar que para todos los escenarios simulados la pluma alcanza
el mayor alcance horizontal.

La distancia horizontal que alcanzaría la pluma salina sería inferior a los 3 metros,
contados a partir del difusor de descarga y en la vertical subiría una distancia del orden de
los 80 cm. Cabe destacar que este desarrollo geométrico de la pluma salina está
íntimamente vinculado con el bajo caudal de operación de la planta.

Es importante destacar que el caudal de operación, las dimensiones de las tuberías de
descarga y las de los difusores son bajas, las que desde un punto de vista ambiental
serían favorables, pues la perturbación en el medio marino que generaría la producción
de agua desde la planta desalinizadora, es esperablemente acotada.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|32|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

_Fuente: Elaboración Propia_

**Figura 4.5.** Geometría de la pluma salina de acuerdo a cada escenario de simulación.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|33|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

Desde un punto de vista del funcionamiento hidráulico, se determinó la salinidad del
efluente en el punto de equilibrio de momentum, es decir, cuando la velocidad del chorro
es igual a la del medio, quedando de este modo la descarga sujeta a la acción forzante de
la hidrodinámica y siendo necesario aplicar técnicas de modelado de campo lejano. Los
resultados obtenidos se muestran en la Tabla 4.4.

Cada columna de la Tabla 4.4, representa los siguientes fenómenos:

 **Salinidad efluente para campo lejano:** Corresponde a la salinidad del chorro que
emite la descarga, en el punto para el cual deja de moverse como cuerpo libre, es
decir, corresponde a la concentración de sal que queda a disposición del medio
marino y de este modo, serán las corrientes de Pisagua las encargadas de diluirla.
En esencia es el valor ingresado posteriormente al modelo de campo lejano.

 - **Disminución de la salinidad:** Corresponde a la concentración de sal que es
diluida debido a la mezcla turbulenta del efluente en el medio marino. Es decir, es
la medición directa de la salinidad que pierde el efluente al mezclarse con el medio

marino.

 - **Exceso de salinidad:** Corresponde al porcentaje de salinidad adicional que tiene
el efluente al abandonar el campo cercano, con respecto del valor referencial del
5% de la línea base, en conformidad de la **AUSTRALIAN WATER QUALITY**

**GUIDELINES FOR FRESH AND MARINE WATERS. 1992.**

 **Distancia de incorporación:** Tal como se comentara previamente, corresponde a
aquel tramo que el efluente proveniente desde la descarga recorre en el medio
marino, antes de verse sometido a la acción del campo de velocidades propias de
OPisagua, es decir, hasta el instante en que el chorro emanado desde los
difusores deja de moverse como un cuerpo libre y pasa a desplazarse debido a la
acción de las corrientes marinas.

**Tabla 4.4.** Salinidad del efluente en el punto equilibrio de momentum (rango de validez del

modelo de campo cercano)

|Escenario|Salinidad efluente<br>para campo lejano<br>(psu)|Disminución de<br>la salinidad<br>(psu)|Exceso de<br>salinidad<br>(%)|Distancia de<br>incorporación (m)|
|---|---|---|---|---|
|Escenario 01|35,75|16,69|1,15|0,89|
|Escenario 02|35,76|16,68|1,57|0,88|
|Escenario 03|35,74|16,70|1,21|0,93|
|Escenario 04|35,74|16,70|1,21|0,92|
|Escenario 05|35,79|16,65|1,67|0,81|
|Escenario 06|35,78|16,66|1,05|0,81|
|Escenario 07|35,76|16,68|1,49|0,87|
|Escenario 08|35,77|16,67|1,37|0,84|

_Fuente: Elaboración Propia_

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|34|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

A partir de la Tabla 4.4, se pudo apreciar que, para cada uno de los casos simulados, la
eficiencia del sistema de descarga permite generar una disminución de la salinidad del
efluente de manera significativa, alcanzando magnitudes mínimas de 16,65 psu y
máximas de 16,70 psu, entre los primeros 0,81 a 0,93 metros de distancia respecto del
punto de emisión.

En el punto de equilibrio de momentum, el efluente impondría al medio marino una
salinidad máxima de 35,79 psu (escenario 05 máximo a 0,81metros de distancia) y
mínima de 35,74 psu (escenario 03 mínimo a 0,93 metros de distancia). Ambas
magnitudes tendrían asociada un aumento de sal en el medio de 1,67% y 1,21%.

Importante es destacar que el sistema de descarga para las condiciones hidrodinámicas y
de columna de agua consideradas, es capaz de producir una dilución de la salinidad del
efluente con valores por debajo de la recomendación Australiana considerada en el
presente estudio. Es decir, que el diseño hidráulico es el adecuado para el sitio estudiado
en función de los criterios de diseño propuestos.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|35|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**4.2.3 Modelado de la dispersión de la pluma salina en el campo lejano**

En consideración de la base hidrodinámica operacional, se realizó la simulación de la
dispersión de la pluma salina en el campo lejano empleando las salinidades de efluentes
determinadas previamente en la modelación de campo cercano, para el punto de
equilibrio de momentum (ver Tabla 4.4).

Se ha considerado como resultado ilustrado el estado salino final de la pluma, luego de
ser sometida a la acción forzante de vientos y mareas, de acuerdo a cada uno de los
escenarios simulados. Todas las figuras se han elaborado considerando los siguientes
recuadros:

 El recuadro izquierdo muestra la ubicación de la zona de estudio y las concesiones
marítimas cercanas (zona cyan y azul).

 El recuadro derecho superior, medio e inferior, ilustran las plumas salinas que se
desarrollarían en las cercanías del fondo, capa intermedia y superficie del agua.

En las Figuras 4.6 a la 4.13, se presentan los resultados de la modelación de pluma salina
de los escenarios 01 al 08 respectivamente. Nótese que las escalas de colores
empleadas van desde 1% a 0 % de exceso de sal respecto del medio, de tal modo, que
permiten obtener las zonas de influencia, pero en ninguna de ellas se presentarán efectos
adversos para el medio marino, dado el valor referencial establecido por la
recomendación Australiana.

El comportamiento de la pluma salina mostró resultados equivalente para cada uno de los
casos simulados, con bajas perturbaciones en la salinidad del medio y desplazamientos
preferentemente hacia el Norte.

Los resultados obtenidos de la modelación de pluma salina, asociados al escenario 01, se
encuentran presentados en la **Figura 4.6** . A partir de ellos se advierte que en las
cercanías del fondo se presentan las mayores concentraciones de sal, las que
alcanzarían una exceso del orden de 1% (tal como en el campo cercano).

En el escenario 01, se advirtió que para igualar la salinidad del efluente con la del medio
marino receptor, la pluma salina debe recorrer una extensión aproximada de 520 metros
(ver Tabla 4.5), la que se desarrolla en las cercanías del fondo y traslada con una
orientación principal hacia el Nor-Este.

En el caso de la pluma salina del escenario 02, sus resultados son presentados en la
**Figura 4.7** y de ellos se advierte que la salinidad entorno de la descarga alcanzaría una
excedencia de 1%, valor que cumple con el límite máximo establecidos para efectos
ambientales en el presente estudio. Situación similar puede apreciarse para los
escenarios restantes ilustrados.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA<br>PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|36|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA**<br>**PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

El alcance total de la pluma salina en la capa de fondo para el escenario 02 sería de 540
metros, mientras que en mitad de columna de agua 365 metros (ver Tabla 4.5). Para
distancias mayores a las descritas, la salinidad del efluente se iguala con la del medio
marino.

Para el escenario 03 simulado (ver Fuente: _Elaboración Propia. Sistema coordenado: UTM-WGS84,_

_HUSO 19._

Figura 4.8), el alcance horizontal de la pluma salina en la capa del fondo se prolongaría
hasta una distancia de 370 metros, mientras que el escenario 04 de 368 metros, para la
misma capa.

El escenario de menor desarrollo de la pluma salina correspondió al 05, alcanzando los
140 metros de distancia. Esto se produce principalmente debido a que las corrientes
impulsarían el flujo con exceso de sal hacia la costa.

En la Tabla 4.5 se presenta de manera resumida las distancias que alcanzaría la pluma
salina antes de igual concentración con la del cuerpo receptor, indicándose los resultados
detalla para cada caso y capa de la columna de agua analizada.

**Tabla 4.5.** Distancias esperadas por escenario de simulación para alcanzar el equilibrio

salino entre el efluente y el medio marino.

|Escenario|Distancia de equilibrio salino (m)|Col3|Col4|
|---|---|---|---|
|**Escenario**|**Fondo**|**Intermedia**|**Superficial**|
|Escenario 01|520|328|0|
|Escenario 02|540|365|0|
|Escenario 03|370|270|0|
|Escenario 04|368|315|0|
|Escenario 05|140|97|0|
|Escenario 06|530|340|0|
|Escenario 07|552|231|0|
|Escenario 08|480|336|0|

_Fuente: Elaboración Propia_

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|37|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

_Fuente: Elaboración Propia. Sistema coordenado: UTM-WGS84, HUSO 19._

**Figura 4.6.** Pluma salina asociada al Escenario 01.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|38|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

_Fuente: Elaboración Propia. Sistema coordenado: UTM-WGS84, HUSO 19._

**Figura 4.7.** Pluma salina asociada al Escenario 02.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|39|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

_Fuente: Elaboración Propia. Sistema coordenado: UTM-WGS84, HUSO 19._

**Figura 4.8.** Pluma salina asociada al Escenario 03.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|40|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

_Fuente: Elaboración Propia. Sistema coordenado: UTM-WGS84, HUSO 19._

**Figura 4.9.** Pluma salina asociada al Escenario 04.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|41|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

_Fuente: Elaboración Propia. Sistema coordenado: UTM-WGS84, HUSO 19._

**Figura 4.10.** Pluma salina asociada al Escenario 05.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|42|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

_Fuente: Elaboración Propia. Sistema coordenado: UTM-WGS84, HUSO 19._

**Figura 4.11.** Pluma salina asociada al Escenario 06.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|43|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

_Fuente: Elaboración Propia. Sistema coordenado: UTM-WGS84, HUSO 19._

**Figura 4.12.** Pluma salina asociada al Escenario 07.

|Col1|INFORME FINAL<br>MODELACIÓN PLUMA SALINA PISAGUA|No DOCUMENTO<br>IT-MOD-DAES/012014|EDICIÓN / REVISIÓN<br>1/1|44|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN PLUMA SALINA PISAGUA**|Fecha de emisión:<br>14/07/2015|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

_Fuente: Elaboración Propia. Sistema coordenado: UTM-WGS84, HUSO 19._

**Figura 4.13.** Pluma salina asociada al Escenario 08.

|Col1|INFORME FINAL<br>MODELACIÓN NUMÉRICA DE CAMPO<br>CERCANO Y CAMPO LEJANO DE LA<br>DISPERSIÓN DE PLUMA SALINA|No DOCUMENTO<br>IT-MOD-ARC/012014|EDICIÓN / REVISIÓN<br>1/1|45|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN NUMÉRICA DE CAMPO**<br>**CERCANO Y CAMPO LEJANO DE LA**<br>**DISPERSIÓN DE PLUMA SALINA**|Fecha de emisión:<br>24/11/2014|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**5** **CONCLUSIONES**

A partir de los resultados expuestos precedentemente, se ha logrado obtener las
siguientes conclusiones:

**5.1** **Respecto del uso de las herramientas numéricas y métodos aplicados**

El conjunto de herramientas numéricas y metodologías de escritorio aplicadas, resultaron
adecuadas para representar el fenómeno estudiado, tanto en la condición de verano como
de invierno.

El modelo numérico RMA10, demostró ser capaz de representar la hidrodinámica
tridimensional de Pisagua encontrándose calibrado y validado para el sector de estudio,
mediante el empleo de información de campo de dos campañas diferentes y tanto para
variación del nivel del mar como para corrientes.

La simulación hidrodinámica demostró ser robusta en la estimación de las variaciones del

nivel del mar y en las magnitudes/direcciones de las corrientes.

**5.2** **Respecto de la simulación de campo cercano**

Los resultados de la modelación de campo cercano, demostraron que el comportamiento
de la pluma salina es del **tipo parabólico**, es decir, en los primeros metros de distancia,
con respecto del punto de descarga, muestra una tendencia a subir, preferentemente
impulsado por el caudal de salida, para posteriormente cambiar su trayectoria y comenzar
un descenso, impulsado por la mayor densidad del efluente que el medio receptor.
Condición que se dio tanto para la estación de verano como de invierno.

La configuración de los difusores resulta ser eficiente para el proceso de dilución inicial,
ya que se demostró que éstos permiten disminuir la salinidad del efluente hasta
magnitudes del orden de 35 psu, siendo en todos los escenarios menor al 5% de
excedencia recomendado por la normativa Australiana, para evitar efectos adversos en
los recursos biológicos disponibles en el medio marino.

El principal agente de dilución y mezcla, entre el efluente y el medio receptor, serían los
difusores, dispuestos a lo largo del emisario, ya que al incrementar la velocidad del flujo,
aumentaría la mezcla turbulenta y de este modo la cantidad de sal tendería a igualarse
(sin llegar a serlo) con la del ambiente costero considerado en el tramo comprendido entre
el inicio del flujo y el equilibrio de momentum.

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

|Col1|INFORME FINAL<br>MODELACIÓN NUMÉRICA DE CAMPO<br>CERCANO Y CAMPO LEJANO DE LA<br>DISPERSIÓN DE PLUMA SALINA|No DOCUMENTO<br>IT-MOD-ARC/012014|EDICIÓN / REVISIÓN<br>1/1|46|
|---|---|---|---|---|
||**INFORME FINAL**<br>**MODELACIÓN NUMÉRICA DE CAMPO**<br>**CERCANO Y CAMPO LEJANO DE LA**<br>**DISPERSIÓN DE PLUMA SALINA**|Fecha de emisión:<br>24/11/2014|Emitido por:<br>EcoTecnos S.A.|Emitido por:<br>EcoTecnos S.A.|

**5.3** **Respecto de la simulación de campo lejano**

La simulación de campo lejano de la pluma salina mostró como tendencia general una
trayectoria de desplazamiento hacia el Nor-este, independiente de las condiciones
hidrodinámicas del medio receptor y la estación del año evaluada (verano e invierno).

Los desplazamientos necesarios de la pluma para alcanzar la salinidad del medio receptor
varió entre 140 metros (escenario 05) y 552 metros (escenario 07), sin embargo, la
dilución requerida del 5% de exceso respecto del medio marino, se alcanza en el campo
cercano, a distancias no superaron 1 metro.

Las condiciones forzantes de invierno combinado con las características de primavera en
la columna de agua, resultaron ser las más favorables para la extensión total de la pluma
salina por el fondo marino.

**5.4** **En términos generales**

La metodología aplicada para la evaluación del comportamiento en el campo cercano y en
el campo lejano de la pluma salina proyectada por la Desalinizadora de Pisagua,
entregaron resultados con valores dentro de lo esperado, de acuerdo al entendimiento del
problema que EcoTecnos S.A. posee, tanto para el área de estudio, como para la física
del problema.

Las herramientas numéricas tridimensionales que fueron empleadas, resultaron ser las
adecuadas para representar, en forma fidedigna, la hidrodinámica y dispersión de la
pluma salina del proyecto.

Las distancias requeridas para alcanzar la dilución límite, serían del orden de 0,9 metros,
lo cual resulta aceptable y de bajo impacto para la calidad ambiental del medio marino.

**EcoTecnos S.A.**

**Departamento de Oceanografía Física y Modelamiento Matemático**

Viña del Mar, 14 de Julio de 2015.

**Limache #3405 - Viña del Mar - Fonos:(32) 2189200 - www.neotecnos.cl - info@neotecnos.cl**

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4.3.: ** Temperatura y salinidad de la columna de agua empleadas en la modelación**

| Profundidad (m) | Escenario 01, 02, 03 y 04 | Col3 | Escenario 05, 06, 07 y 08 | Col5 |
| --- | --- | --- | --- | --- |
| **Profundidad (m)** | **Salinidad**<br>**(psu)** | **Temperatura**<br>**(°C)** | **Salinidad**<br>**(psu)** | **Temperatura**<br>**(°C)** |
| 0,0 | 34,969 | 15,431 | 34,961 | 16,092 |
| 0,5 | 34,969 | 15,431 | 34,961 | 16,092 |
| 1,0 | 34,972 | 15,355 | 34,968 | 16,087 |
| 1,5 | 34,944 | 15,311 | 34,973 | 16,080 |
| 2,0 | 34,944 | 15,264 | 34,980 | 16,073 |
| 2,5 | 34,955 | 15,150 | 34,989 | 16,059 |
| 3,0 | 34,948 | 15,058 | 34,992 | 16,046 |
| 3,5 | 34,951 | 15,031 | 34,984 | 16,036 |
| 4,0 | 34,961 | 15,038 | 34,980 | 16,028 |
| 4,5 | 34,969 | 15,431 | 34,963 | 16,026 |
| 5,0 | 34,972 | 15,431 | 34,957 | 16,024 |

**Tabla 3.1.: ****

| Escenario | Marea | Viento |
| --- | --- | --- |
| E01 | Ciclo diario de sicigias | Ciclo diario medio de vientos de verano |
| E02 | Ciclo diario de cuadraturas | Ciclo diario medio de vientos de verano |
| E03 | Ciclo diario de sicigias | Ciclo diario máximo de vientos de verano |
| E04 | Ciclo diario de cuadraturas | Ciclo diario máximo de vientos de verano |
| E05 | Ciclo diario de sicigias | Ciclo diario medio de vientos de invierno |
| E06 | Ciclo diario de cuadraturas | Ciclo diario medio de vientos de invierno |
| E07 | Ciclo diario de sicigias | Ciclo diario máximo de vientos de invierno |
| E08 | Ciclo diario de cuadraturas | Ciclo diario máximo de vientos de invierno |

**Tabla 3.3.: ** Características relevantes para cada una de las tuberías de descarga de la**

| Parámetro | Unidad | Valor |
| --- | --- | --- |
| Longitud del difusor | m | 5 |
| Diámetro de tubería de difusión (ID) | mm | 160 |
| Profundidad descarga | mNRS | 4 |
| Número de puertas | - | 5 |
| Espaciamiento entre puertas | m | 2 |
| Diámetro de puertas | mm | 50 |
| Ángulo vertical | ° | 45 |
| Caudal efluente | L/s | 5 |
| Exceso de Salinidad efluente | % | 50 |

**Tabla 4.1.: ** Perfiles vertical de velocidades de corrientes obtenido desde la simulación de**

| Profundidad<br>(m) | E01<br>(m/s) | E02<br>(m/s) | E03<br>(m/s) | E04<br>(m/s) | E05<br>(m/s) | E06<br>(m/s) | E07<br>(m/s) | E08<br>(m/s) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0,0 | 0,469 | 0,480 | 0,470 | 0,482 | 0,458 | 0,445 | 0,464 | 0,455 |
| 0,5 | 0,469 | 0,479 | 0,470 | 0,482 | 0,457 | 0,444 | 0,464 | 0,454 |
| 1,0 | 0,467 | 0,477 | 0,469 | 0,481 | 0,456 | 0,443 | 0,464 | 0,453 |
| 1,5 | 0,466 | 0,475 | 0,468 | 0,479 | 0,455 | 0,441 | 0,463 | 0,452 |
| 2,0 | 0,464 | 0,474 | 0,467 | 0,478 | 0,453 | 0,439 | 0,461 | 0,450 |
| 2,5 | 0,463 | 0,472 | 0,465 | 0,477 | 0,451 | 0,437 | 0,460 | 0,449 |
| 3,0 | 0,461 | 0,470 | 0,464 | 0,475 | 0,450 | 0,436 | 0,459 | 0,448 |
| 3,5 | 0,459 | 0,468 | 0,463 | 0,474 | 0,448 | 0,434 | 0,458 | 0,446 |
| 4,0 | 0,458 | 0,466 | 0,462 | 0,473 | 0,446 | 0,432 | 0,457 | 0,445 |
| 4,5 | 0,453 | 0,465 | 0,458 | 0,471 | 0,442 | 0,430 | 0,456 | 0,443 |
| 5,0 | 0,444 | 0,458 | 0,448 | 0,465 | 0,433 | 0,430 | 0,456 | 0,444 |

**Tabla 4.2.: ** Perfiles vertical de direcciones de corrientes obtenido desde la simulación de la**

| Profundidad<br>(m) | E01 (o) | E02 (o) | E03 (o) | E04 (o) | E05 (o) | E06 (o) | E07 (o) | E08 (o) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0,0 | 40,136 | 39,629 | 40,137 | 39,689 | 41,524 | 40,972 | 41,068 | 40,541 |
| 0,5 | 40,169 | 39,644 | 40,162 | 39,699 | 41,592 | 41,017 | 41,101 | 40,559 |
| 1,0 | 40,201 | 39,661 | 40,187 | 39,712 | 41,655 | 41,062 | 41,131 | 40,581 |
| 1,5 | 40,243 | 39,694 | 40,221 | 39,740 | 41,728 | 41,127 | 41,172 | 40,622 |
| 2,0 | 40,289 | 39,727 | 40,260 | 39,770 | 41,805 | 41,192 | 41,218 | 40,664 |
| 2,5 | 40,335 | 39,760 | 40,299 | 39,799 | 41,881 | 41,257 | 41,263 | 40,705 |
| 3,0 | 40,381 | 39,793 | 40,337 | 39,828 | 41,958 | 41,322 | 41,309 | 40,746 |
| 3,5 | 40,427 | 39,826 | 40,376 | 39,857 | 42,035 | 41,387 | 41,354 | 40,788 |
| 4,0 | 40,472 | 39,858 | 40,415 | 39,886 | 42,112 | 41,452 | 41,400 | 40,829 |
| 4,5 | 40,223 | 39,891 | 40,166 | 39,915 | 41,889 | 41,517 | 41,436 | 40,870 |
| 5,0 | 39,520 | 39,360 | 39,473 | 39,396 | 41,204 | 41,579 | 41,594 | 40,910 |

**Tabla 4.4.: ** Salinidad del efluente en el punto equilibrio de momentum (rango de validez del**

| Escenario | Salinidad efluente<br>para campo lejano<br>(psu) | Disminución de<br>la salinidad<br>(psu) | Exceso de<br>salinidad<br>(%) | Distancia de<br>incorporación (m) |
| --- | --- | --- | --- | --- |
| Escenario 01 | 35,75 | 16,69 | 1,15 | 0,89 |
| Escenario 02 | 35,76 | 16,68 | 1,57 | 0,88 |
| Escenario 03 | 35,74 | 16,70 | 1,21 | 0,93 |
| Escenario 04 | 35,74 | 16,70 | 1,21 | 0,92 |
| Escenario 05 | 35,79 | 16,65 | 1,67 | 0,81 |
| Escenario 06 | 35,78 | 16,66 | 1,05 | 0,81 |
| Escenario 07 | 35,76 | 16,68 | 1,49 | 0,87 |
| Escenario 08 | 35,77 | 16,67 | 1,37 | 0,84 |

**Tabla 4.5.: ** Distancias esperadas por escenario de simulación para alcanzar el equilibrio**

| Escenario | Distancia de equilibrio salino (m) | Col3 | Col4 |
| --- | --- | --- | --- |
| **Escenario** | **Fondo** | **Intermedia** | **Superficial** |
| Escenario 01 | 520 | 328 | 0 |
| Escenario 02 | 540 | 365 | 0 |
| Escenario 03 | 370 | 270 | 0 |
| Escenario 04 | 368 | 315 | 0 |
| Escenario 05 | 140 | 97 | 0 |
| Escenario 06 | 530 | 340 | 0 |
| Escenario 07 | 552 | 231 | 0 |
| Escenario 08 | 480 | 336 | 0 |
