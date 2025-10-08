---
title: Sin título
author: Ivan Antonio Fuentes Olivares (ivanfuo)
date: D:20190517100630-04'00'
language: es
type: general
pages: 20
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - P ROYECTO P LANTA F OTOVOLTAICA L OCKMA G RENERGY C HILE M ODELACIÓN H IDRÁULICA
-->

# P ROYECTO P LANTA F OTOVOLTAICA L OCKMA G RENERGY C HILE M ODELACIÓN H IDRÁULICA

#### Gino Sturla Zerene [1] Iván Fuentes Olivares [2]

### S TURLA & F UENTES S PA

**12 de mayo de 2019**

1 Ingeniero Civil Hidráulico, Candidato a Doctor, Universidad de Chile.
2 Ingeniero Civil Hidráulico, Diploma en Hidrogeología, Universidad de Chile.

a

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

**Contenido**

1 Introducción ............................................................................. 3

1.1 Del proyecto ........................................................................ 3

1.2 Objetivos ............................................................................ 3

1.3 Alcance ............................................................................... 4

2 Antecedentes ........................................................................... 5

2.1 Zona de estudio y curvas de nivel .......................................... 5

2.2 Geometría para el modelo ..................................................... 6

2.3 Parámetros .......................................................................... 7

3 Resultados modelación Hec-RAS ................................................. 9

4 Área de escurrimiento ............................................................. 14

4.1 Metodología ....................................................................... 14

4.2 Mapa área escurrimiento ..................................................... 15

5 Conclusiones .......................................................................... 18

5.1 De la modelación ................................................................ 18

5.2 Consideraciones ................................................................. 19

2

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

### 1 INTRODUCCIÓN

**1.1** **Del Proyecto**

El presente estudio se sitúa en el contexto del ingreso a tramitación
ambiental del Proyecto Fotovoltaico LOCKMA, ubicado en la II Región de
Antofagasta, cuyo Titular es Grenergy.

El Proyecto se ubica en la provincia de Antofagasta, en la comuna del
mismo nombre; tiene un área de 21 hectáreas y se ubica a unos 15 km
en dirección nororiente de la ciudad de Antofagasta.

**1.2** **Objetivos**

El estudio consiste en la modelación hidráulica de la Quebrada Mantos
Blancos, la cual es de carácter intermitente y no presenta un cauce
definido en la zona donde se emplazará el proyecto.

Los objetivos principales son:

 En base al caudal de periodo de retorno de 100 años estimado en

el “Estudio Hidrológico Lockma”, construir un modelo que permita
evaluar los sectores en los cuales podría existir escurrimiento
superficial.

 Presentar los resultados de la modelación (software Hec-RAS)

para toda la extensión de estudio y en particular los perfiles
transversales y parámetros del flujo, si es que lo hay, en el lugar
de emplazamiento del Proyecto.

 Elaborar mapas de escurrimiento superficial con herramientas

SIG, que permitan ilustrar los vínculos entre el proyecto y la
superficie de agua generada por el modelo.

 Establecer conclusiones respecto a la posible afectación del

Proyecto debido a una crecida en la quebrada Mantos Blancos,
considerando el alcance y los resultados de la modelación, así
como la información de terreno.

3

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

**1.3** **Alcance**

Respecto al alcance del estudio, existen elementos propios de la
modelación y aquellos asociados a las conclusiones que podrían emanar
de los resultados.

La quebrada Mantos Blancos, además de no presentar un cauce
definido, no presenta variaciones significativas de cota de elevación en
su sección transversal.

Considerando lo anterior, se detallan los alcances del estudio:

 Dada su gran extensión transversal y la necesidad de encontrar

patrones de flujo a lo largo de la quebrada, es necesario evaluar
una zona de más de 10 km [2 ] de área, razón por la cual se ha
optado por utilizar modelos de elevación digital.

 Debido la resolución de elevación a utilizar y los objetivos

planteados previamente, la modelación en 1-D y régimen
permanente se considera apropiada. Aún más, se pueden
encontrar en la literatura comparaciones entre softwares (HecRas, Iber, Mike, Telemac), éstas indican que la necesidad de una
modelación 2-D puede justificarse para zonas donde hay
confluencias, para evaluar el cambio del fondo del lecho,
transporte de sedimentos, u otros problemas, no así las
superficies de inundación en una quebrada intermitente.

 Este estudio no se propone representar la infraestructura existente

en la zona de estudio (carretera, edificaciones, obras de arte,
etc.), no obstante, esto se menciona en las conclusiones
(fotografías) como información adicional. Se ha tomado la decisión
de hacer un análisis hidráulico sacrificando resolución y detalle,
centrando la atención en una zona de estudio extensa.

 Los resultados del modelo no pretenden establecer con certeza

cuáles serán las áreas de escurrimiento superficial, ni delimitar el
ancho de la quebrada. Éstos se plantean con el objetivo de
establecer una evaluación del potencial impacto que podría llegar
a tener una crecida en la quebrada sobre el Proyecto, para que el
Titular lo tenga presente en sus fases de construcción y operación.

4

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

### 2 ANTECEDENTES

**2.1** **Zona de estudio y curvas de nivel**

En base al Modelo de Elevación Digital (DEM) “Alos Palsar”, con
resolución espacial de 12.5 x 12.5 metros, se presenta en la Figura 2-1
curvas de nivel cada 1.5 metros, la extensión de la zona de estudio y el
área del Proyecto completa.

Se aprecia que aguas arriba del Proyecto el cauce está bastante
delimitados, no así hacia abajo donde el escurrimiento podría ser tanto
por el lado norte como sur del eje de la quebrada, o por ambos,
dependiendo del caudal de crecida. Esto quedará claro con los
resultados entregados en los capítulos siguientes.

5

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

**Figura 2-1 Curvas de nivel y área de Proyecto**

Fuente: Elaboración Propia

**2.2** **Geometría para el modelo**

A continuación, se presenta la Figura 2-2 con la geometría considerada
para la modelación. Se ha utilizado la herramienta Hec-GeoRAS a partir
de la cual se ha procesado el DEM, para obtener:

 Archivo TIN con topografía continua de la zona de estudio.

 Cauce principal para la modelación considerando el hecho, ya

mencionado, que podrían existir uno o dos cauces o patrones de
escurrimiento. Longitud de 5.3 Km aproximadamente.

 Riberas y límites del modelo, dentro de los cuales se ha

incorporado el área total del Proyecto, esto es, se considera la
posibilidad de que el escurrimiento superficial, o superficie de
agua, se superponga con las instalaciones.

6

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

 Perfiles transversales (30) espaciados entre 150 y 200 metros y

de ancho que varía, dependiendo la sección, entre los 600 y 2500

metros.

**Figura 2-2 Geometría para el modelo**

Fuente: Elaboración Propia

**2.3** **Parámetros**

Se presentan los parámetros más relevantes para la modelación,
indicando su justificación y/o procedencia.

 Caudal de crecida de periodo de retorno de 100 años igual a 60.8

m3/s, obtenido del “Estudio Hidrológico Lockma”.

7

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

Coeficiente rugosidad (Manning) de 0.035 para el lecho y las

riberas. Este valor se ha obtenido del libro “Hidráulica Aplicada al
Diseño de Obras” de Horacio Mery. Se ha considerado la
metodología de Cowan: valor base para lecho de tierra (0.020),
pocas irregularidades (0.005), variaciones de la sección
ocasionales (0.005), obstrucciones despreciables y muy poca
vegetación (0,005).

Las condiciones de borde corresponden a altura normal de

escurrimiento aguas arriba y abajo, la cual se calcula con la
pendiente; a continuación, en la Tabla 2-2, se presenta por cada
quebrada: pendiente aguas arriba, pendiente aguas abajo,
pendiente media y longitud.

**Tabla 2-2 Pendientes y Longitud Quebrada**

|Cauce|Pendiente<br>Aguas Arriba|Pendiente<br>Aguas Abajo|Pendiente<br>Media|Longitud<br>(m)|
|---|---|---|---|---|
|Quebrada<br>Mantos Blancos|1.1%<br>|0.7%<br>|0.6%|5300|

Fuente: Elaboración Propia

Las pendientes, ancho de las riberas, cotas de fondo y radio

hidráulico, entre otros, se obtienen directamente de los perfiles
transversales.

Los coeficientes de expansión, contracción y aquellos asociados a

la alcantarilla corresponden a los recomendados en la literatura,
los cuales considera por defecto el software.

8

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

### 3 RESULTADOS MODELACIÓN HEC-RAS

En esta sección se muestran los resultados obtenidos en la modelación
de la quebrada. La Tabla 3-1 presenta los principales parámetros del
flujo asociados a la modelación, por sección transversal: cota mínima
cauce, cota superficie agua, velocidad, área escurrimiento, ancho
superficie agua, número de Froude y altura máxima de escurrimiento.
La Figura 3-1 muestra el perfil longitudinal, la Figura 3-2 una vista
general y la Figura 3-3 las secciones transversales desde aguas arriba
hacia aguas abajo.

Como se verá en el capítulo siguiente los perfiles que se encuentran a la
altura de proyecto no presentan escurrimiento en sus cercanías.

_La totalidad de las secciones transversales en PDF y el modelo Hec-Ras_
_original se encuentran en el “Apéndice A Hec-Ras Lockma”._

9

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

**Tabla 3-1. Parámetros del Flujo (se destacan perfiles altura Proyecto)**

Fuente: Elaboración Propia

10

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

**Figura 3-1. Perfil Longitudinal**

Fuente: Elaboración Propia

**Figura 3-2. Vista General**

11

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

Fuente: Elaboración Propia

**Figura 3-3. Secciones Transversales (Proyecto)**

12

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

Fuente: Elaboración Propia

**Figura 3-3. Secciones Transversales (Proyecto) Cont.**

13

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

Fuente: Elaboración Propia

### 4 ÁREA DE ESCURRIMIENTO

**4.1** **Metodología**

A continuación, se detalla la metodología utilizada para generar el área
de escurrimiento:

 En base a la información georreferenciada, se utiliza la

herramienta Hec-GeoRas que permite desde ArcGIS exportar el río
(quebrada) y sus secciones con un sistema de coordenadas
asociado, en este caso Sirgas WGS84, huso 19 sur.

 La Modelación en Hec-Ras se hace bajo las mismas condiciones

hidráulicas, pero los resultados que se generan tienen un sistema
de coordenadas asociado. La modelación presentada en el capítulo
previo fue hecha de esta forma; debe quedar claro que en
términos de la hidráulica el hecho de estar o no georreferenciado
(río y perfiles) no tiene relevancia, sí la adquiere cuando se quiere
procesar los resultados como el área de escurrimiento.

14

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

 Uno de los parámetros hidráulicos relevantes corresponde a la

superficie de agua, en otras palabras, el ancho del escurrimiento
visto en planta. Dado que se tiene un modelo georreferenciado, es
posible exportar la superficie de agua en formato SIG, para luego
procesarlo.

 Con la superficie de agua en formato vectorial georreferenciado,

se efectúan algunos ajustes leves, que dependen básicamente de
la densidad de perfiles transversales, y se genera un archivo
Shape (polígono vectorial).

**4.2** **Mapa área escurrimiento**

La Figura 4-1 presenta el mapa con la superficie de agua, la cual varía
desde 0 a 1.6 metros, mientras más azul mayor la altura. El mapa
contiene además el área del Proyecto y los perfiles transversales.

La Figura 4-2 presenta la superposición del área de escurrimiento con
las curvas de nivel, se aprecia que el agua escurriría sólo por la parte
norte de la quebrada, esto tanto por el gradiente de elevación, así como
por la magnitud del caudal (ver detalle en capítulo 3).

_Los mapas y sus elementos (formato KMZ y SHP) se encuentran en el_
_“Apéndice B SIG Lockma”._

15

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

**Figura 4-1 Área Escurrimiento y Proyecto**

Fuente: Elaboración Propia

16

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

**Figura 4-2 Área de Escurrimiento y Curvas de Nivel**

Fuente: Elaboración Propia

17

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

### 5 CONCLUSIONES

Se mencionan las conclusiones principales de la modelación hidráulica
efectuada y posteriormente se presentan algunas consideraciones
tomando en cuenta información entregada por la Consultora Ambiental.

**5.1** **De la modelación**

 Los resultados corresponden a la solución numérica de las

ecuaciones de Saint-Venant 1-D en régimen permanente. Esto
implica que los parámetros del flujo obtenidos son representativos
de la sección transversal.

 Para la Quebrada Mantos Blancos el caudal de crecida es de 4.30

m [3] /s, ésta presenta una pendiente media de 0.6%, el régimen de
escurrimiento subcrítico. Para las 30 secciones transversales, el
rango de alturas es de 0.25 a 0.65 metros y el de velocidades es
0.73 a 1.53 m/s.

 Respecto al Área de Escurrimiento, ésta se ha determinado en

base al ancho de la superficie de agua en cada uno de los perfiles
transversales con herramientas SIG. Los Mapas de Escurrimiento
permiten visualizar el área de escurrimiento asociada a la crecida
de 100 años de periodo de retorno, la cual no se superpone con el
área del Proyecto, ubicándose a más de 500 metros.

 Deben considerarse los supuestos de la modelación, lo cual ha

quedado definido en el Alcance de este estudio. Lo principal
corresponde a la generación de topografía en base al DEM, lo cual
involucra la resolución en elevación, así como la infraestructura
adyacente.

18

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

**5.2** **Consideraciones**

 Si bien no hay superposición entre la superficie de escurrimiento y

el área completa del proyecto, para la modelación efectuada, se
recomienda, de igual forma al Titular elaborar planes de
contingencia y emergencia internos.

 Los patrones de escurrimiento son sensibles a las variaciones de

la topografía del terreno, lo cual queda claro en las observaciones
efectuada por la Consultora Ambiental:

_“En el Área del Proyecto no se aprecia un cauce definido, ya que la_
_topografía es completamente plana, cuyas únicas variaciones corresponden_
_solamente a movimientos de tierra de origen antrópico. Las únicas señales_
_de la existencia del cauce es la presencia de sedimentos más finos y claros_
_desde el punto de acceso al Proyecto, que se diferencian de los sedimentos_
_eólicos más oscuros. El ancho de estos sedimentos es de hasta 80-100_
_metros aproximadamente desde dicho punto de acceso, hacia el este, lo_
_que sugiere antiguos eventos de escorrentía superficial_ .”

 Las siguientes fotografías, Figura 5-1, ratifican el hecho de que la

quebrada se encuentra en una zona donde además de pocas
variaciones en la topografía hay infraestructura, lo cual podría
generar situaciones imprevistas, como también protección, sobre
todo desde el lado norte.

**Figura 5-1 Fotografías Zona Proyecto**

|Lado Norte|Lado Sur|
|---|---|
|||

19

Planta Fotovoltaica Lockma

Modelación Hidráulica

Declaración de Impacto Ambiental

Fuente: Elaboración Propia

20

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 2-2: Pendientes y Longitud Quebrada****

| Cauce | Pendiente<br>Aguas Arriba | Pendiente<br>Aguas Abajo | Pendiente<br>Media | Longitud<br>(m) |
| --- | --- | --- | --- | --- |
| Quebrada<br>Mantos Blancos | 1.1%<br> | 0.7%<br> | 0.6% | 5300 |
