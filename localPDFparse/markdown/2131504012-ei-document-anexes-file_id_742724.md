---
title: Cover Page
author: Cristián Palma/Chile/GHD/AU
date: D:20160609144454-04'00'
language: es
type: report
pages: 44
has_toc: False
has_tables: True
extraction_quality: high
---

<!-- ESTRUCTURA DEL DOCUMENTO -->
<!-- Este documento contiene las siguientes secciones principales:
  - Índice
-->

## Declaración de Impacto Ambiental “Subestación Adicional Puente Negro”

### Anexo H Informe de Campos Electromagnéticos

#### Preparado por junio de 2016

# Índice

1 Introducción 3

2 Objetivos 4

2.1 Objetivo general 4

2.2 Objetivos específicos 4

3 Metodología 5

4 Antecedentes 6

4.1 Subestación Adicional Puente Negro 6

4.2 Características de las líneas de transmisión 3

5 Resultados 7

5.1 Subestación Adicional Puente Negro 7

5.2 Líneas de transmisión 2x220 kV 14

5.3 Normativa aplicable 21

6 Conclusiones 24

6.1 Subestación Adicional Puente Negro 24

6.2 Líneas de transmisión 2x220 kV 24

7 Referencias 26

#### Índice de Tablas

Tabla 4-1 Características de las instalaciones de la subestación 2

Tabla 4-2 Distancias mínimas eléctricas para subestaciones de 220 kV 3

Tabla 4-3 Características de las derivaciones de línea 6

Tabla 5-1 Campo eléctrico y campo magnético en borde de subestación 12

Tabla 5-2 Campo eléctrico y campo magnético en borde de franja de seguridad 17

Tabla 5-3 Listado de salida del software LINEAS 18

Tabla 5-4 Normativa para campo eléctrico y magnético de 50 Hz 22

Tabla 5-5 Radio interferencia aceptable a 0,5 MHz y a 15 m de distancia de fase

externa 22

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 1

#### Índice de Figuras

Figura 4-1 Subestación seccionadora 220 kV y líneas de transmisión de 2x220 kV 6

Figura 4-2 Esquema general de la Subestación Adicional Puente Negro 1

Figura 4-3 Vista en corte A 1

Figura 4-4 Vista en corte B 2

Figura 4-5 Derivaciones de línea 4

Figura 4-6 Detalle derivaciones de líneas 5

Figura 5-1 Gráfico 3-D densidad de campo magnético medido en el interior de una
subestación GIS de 220 kV [2] 7

Figura 5-2 Mapa de inducción magnética medida alrededor de la valla de
subestación GIS 22 kV [2] 8

Figura 5-3 Medidas de RI en varias subestaciones GIS [4] 9

Figura 5-4 Esquema de Gas-Insulated Substation London-Talbot 230 kV [3] 9

Figura 5-5 Trayectoria escogida para cálculo de campos generados por líneas de

220 kV 10

Figura 5-6 Campo eléctrico a 1m sobre el suelo en Trayectoria A1 - A2 11

Figura 5-7 Inducción magnética a 1m sobre el suelo en trayectoria A1 - A2 11

Figura 5-8 Esquema de subestación Pontchartrain y puntos de medida [6] 12

Figura 5-9 Radio interferencia operando la subestación Pontchartrain a 230 kV [6] 13

Figura 5-10 Esquema de subestación Snakefarm de 230 KV y puntos de medida [6] 13

Figura 5-11 Radio interferencia medida en puntos de borde subestación Snakefarm
230 kV [6] 14

Figura 5-12 Modelo de elementos finitos para derivaciones de líneas 15

Figura 5-13 Distribución de equipotenciales eléctricas en derivaciones de líneas 15

Figura 5-14 Campo eléctrico a 1m de altura sobre el suelo en derivaciones de líneas 16

Figura 5-15 Distribución de equipotenciales magnéticas en derivaciones de líneas 16

Figura 5-16 Inducción magnética a 1m de altura sobre el suelo en derivaciones de

líneas 17

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 2

### 1 Introducción

El presente informe entrega los antecedentes y resultados correspondientes a la estimación de la
magnitud del campo electromagnético por la operación del Proyecto **Subestación adicional Puente**
**Negro**, ubicado en la Comuna de Chimbarongo, Región del Libertador General Bernardo O’Higgins.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 3

### 2 Objetivos

2.1 Objetivo general

Estimar la magnitud del campo electromagnético generado por la operación del Proyecto Subestación
Adicional Puente Negro, correspondiente a una subestación seccionadora de 220 kV y una derivación
constituida por dos líneas de transmisión de 220 kV, de doble circuito.

2.2 Objetivos específicos

Específicamente se busca determinar:

 - El campo eléctrico y el campo magnético a frecuencia industrial presentados como perfiles
internos y externos a la subestación y según perfiles transversales en el caso de las líneas.

 - La emisión de radio interferencia generada por efecto corona en la subestación y en las líneas de

transmisión.

 - Comparación de valores estimados con los respectivos máximos recomendados por las normas
de referencia de valores tolerables por las personas para los campos, y límites máximos de
emisión, para las interferencias, señaladas en el reglamento del SEIA.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 4

### 3 Metodología

Se presenta la información recogida de referencias nacionales e internacionales respecto de valores de
campo eléctrico y campo magnético medidos en instalaciones similares a la subestación en estudio. Se
incorpora además los resultados de una modelación de los conductores de barras y líneas de la
subestación y la aplicación del software QuickField [1] que utiliza el método de elementos finitos, para
obtener campo eléctrico generado por los conductores energizados y el campo magnético generado por
las respectivas corrientes.

Similarmente se realiza una estimación del nivel perturbador a frecuencias de radio generado por la
subestación debido al fenómeno corona, en base a medidas referenciales informadas en la bibliografía.
Para la línea se utilizan expresiones simplificadas de aplicación habitual.

Se entrega las normas de referencia aplicables en Chile respecto de la exposición humana a campos
electromagnéticos de 50 Hz y los valores límites de radio interferencia. Estos valores se confrontan con
las estimaciones teóricas o de referencia, para establecer finalmente una conclusión respecto al impacto
ambiental de la Subestación Adicional Puente Negro, desde el punto de vista técnico de la emisión
electromagnética de baja y alta frecuencia.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 5

### 4 Antecedentes

El Proyecto se localiza en la Región del Libertador General Bernardo O ́Higgins, provincia de Colchagua,
Comuna de Chimbarongo (Figura 4-1).

Figura 4-1 Subestación seccionadora 220 kV y líneas de transmisión de 2x220 kV

Fuente: Elaboración propia.

4.1 Subestación Adicional Puente Negro

La Subestación, incluirá las siguientes obras y equipos:

 - Interruptores (tecnología GIS)

 - Transformadores de medida (tecnología GIS)

 - Desconectadores (tecnología GIS)

 - Pararrayos (tecnología convencional)

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 6

 - Condensadores de acoplamiento y trampas de onda (tecnología convencional)

 - Transformadores de potencial para alimentación de servicios auxiliares en corriente alterna
(tecnología convencional)

 - Baterías y cargadores para alimentación de servicios auxiliares en corriente continua (tecnología
convencional)

 - Grupo electrógeno de emergencia

 - Sistemas de control y protecciones

 - Sistema de monitoreo, control y adquisición de datos (SCADA)

 - Cables de fuerza y control en baja tensión

 - Conductores desnudos de barras y conexión de equipos

 - Aislaciones y marcos de barra y de línea

A continuación se muestra un esquema general (Figura 4-2) y cortes de la subestación (Figura 4-3 y
Figura 4-4).

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 7

Figura 4-2 Esquema general de la Subestación Adicional Puente Negro

Fuente: Elaboración propia.

Figura 4-3 Vista en corte A

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 1

Figura 4-4 Vista en corte B

Fuente: Elaboración propia.

Tabla 4-1 Características de las instalaciones de la subestación

|Instalación|Característica|
|---|---|
|Voltaje nominal|220 KV|
|Voltaje máximo|245 KV|
|Capacidad máxima|760 MVA|
|Tipo de Tecnología|equipamiento aislado en gas SF6 (GIS)|
|Topología o configuración|Interruptor y medio|
|Tensión soportada a frecuencia nominal|460 KV|
|Nivel básico de impulso|1050 KV|
|Capacidad de transporte Perm. barra colectora|3150 A|
|Capacidad de transporte Perm. alimentadores|1250 A|
|Corriente de corta duración (1s) admisible|50 KA rms|
|Número de paños|6|
|Cantidad de Marcos de Línea|cuatro, dos utilizados también como marcos de barras|
|Alturas desde piso punto de anclaje/total de los<br>Marcos de Línea|16,7 m/27,2 m|
|Cantidad de Marcos de Barras|1 - Barra 1 y 1 - Barra 2, utilizados también como marcos<br>de barras|
|Alturas desde piso de los Marcos de Barra|10,27 m|

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 2

|Instalación|Característica|
|---|---|
|Conductores de barras aéreas|1 x AAC 1590 MCM (Coreopsis) o similar|
|Cable de guardia aéreo|E.H.S 3/8”de diâmetro|
|Cable de puesta a tierra subterránea|Cobre 4/0 AWG|
|Aislación de parte aérea|Cadena de aisladores de discos de vidrio templado|
|Distancia de fuga mínima parte aérea|Clase III, IEC, 60815, 25 mm/KV|
|Altura de torres proyectadas para acometida|43,2 m|

Fuente: Elaboración propia.

Los calibres del conductor se definirán en la ingeniería de detalle, sin embargo, deberán ser suficientes
para soportar corrientes de hasta 1.250 A para el caso de alimentadores y 3.150 A para el caso de barras
aéreas. Los conductores relacionados con alimentadores, serán AAAC 740,8 MCM (Flint) o similar. Las
distancias mínimas eléctricas en aire que aplican en la Subestación, cumplen con lo establecido en la
Norma NSEG 5. E n. 71. Las distancias mínimas eléctricas, son las que se indican en la Tabla 4-2.

<!-- INICIO TABLA 4-2 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- para soportar corrientes de hasta 1.250 A para el caso de alimentadores y 3.150 A para el caso de barras aéreas. Los conductores relacionados con alimentadores, serán AAAC 740,8 MCM (Flint) o similar. Las distancias mínimas eléctricas en aire que aplican en la Subestación, cumplen con lo establecido en la Norma NSEG 5. E n. 71. Las distancias mínimas eléctricas, son las que se indican en la Tabla 4-2. -->

**Tabla 4-2: Distancias mínimas eléctricas para subestaciones de 220 kV**

| Voltaje | Entre fases | Col3 | Entre fase y tierra | Col5 | Distancia al suelo del<br>punto más bajo<br>energizado |
| --- | --- | --- | --- | --- | --- |
| **Voltaje** | **Partes**<br>**flexibles** | **Partes**<br>**rígidas** | **Partes flexibles** | **Partes rígidas** | **Partes rígidas** |
| 220 kV | 6.030 mm | 2.670 mm | 3.788 mm | 2.108 mm | 4.873 |

<!-- Estadísticas: 2 filas, 6 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. 4.2 Características de las líneas de transmisión -->
<!-- FIN TABLA 4-2 -->


Tabla 4-2 Distancias mínimas eléctricas para subestaciones de 220 kV

|Voltaje|Entre fases|Col3|Entre fase y tierra|Col5|Distancia al suelo del<br>punto más bajo<br>energizado|
|---|---|---|---|---|---|
|**Voltaje**|**Partes**<br>**flexibles**|**Partes**<br>**rígidas**|**Partes flexibles**|**Partes rígidas**|**Partes rígidas**|
|220 kV|6.030 mm|2.670 mm|3.788 mm|2.108 mm|4.873|

Fuente: Elaboración propia.

4.2 Características de las líneas de transmisión

Las líneas corresponden a dos trazados de línea de 2x220 kV (ver Figura 4-5 y Figura 4-6). Uno de
longitud de atravieso de 541 metros y otro de longitud de atravieso de 561 metros.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 3

Figura 4-5 Derivaciones de línea

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 4

Figura 4-6 Detalle derivaciones de líneas

Fuente: Elaboración propia.

Ambos trazados de línea de 2x220 KV, se iniciarán en los pórticos de salida de la Subestación y se
rematarán en la estructura N° 43 de la La Higuera - Tinguiririca 2x154 kV. Las líneas (Tabla 4-3)

<!-- INICIO TABLA 4-3 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- (2) estructuras de suspensión de construcción metálica enrejada y cuatro (4) estructuras de suspensión construidas en base a postes tubulares metálicos. Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 5 -->

**Tabla 4-3: Características de las derivaciones de línea**

| Ítem | Descripción |
| --- | --- |
| Voltaje nominal | 220 KV |
| Voltaje máximo | 245 KV |
| Capacidad máxima | 760 MVA |
| N° Circuitos | 2 |
| N° Conductores/fase | 2 |
| Disposición de los circuitos | Vertical |
| Cable de guardia | Si |
| Cable de fibra óptica | Tipo OPGW, de 60 fibras |
| Conductor | AAAC 740.8 MCM (Flint) o similar |
| Temperatura máxima en emergencia | 80° C |
| Distancia de fuga mínima | Clase III, IEC, 60815, 25 mm/KV |
| Tipo de estructuras | Metálicas enrejadas o tubulares, autosoportadas con<br>disposición vertical de circuitos |
| Altura de estructuras desde piso a punto más alto de<br>engrampe cable de guardia | Enrejadas: 43,2 m. Tubulares: 10 m |
| Cantidad de estructuras de anclaje | Cuatro |
| Cantidad de estructuras de suspensión | Seis |
| Vano mínimo | 222 m |
| Vano máximo | 232 m |
| Cadena de anclaje con aisladores de disco | Simple tipo ball and socket |
| Cadena de suspensión con aisladores de disco | Simple tipo ball and socket |
| Longitud | 541 m - tramo norte<br>561 m - tramo sur |

<!-- Estadísticas: 20 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 6 -->
<!-- FIN TABLA 4-3 -->

contarán con seis (6) vértices; cuatro (4) estructuras de anclaje de construcción metálica enrejada; dos
(2) estructuras de suspensión de construcción metálica enrejada y cuatro (4) estructuras de suspensión
construidas en base a postes tubulares metálicos.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 5

Tabla 4-3 Características de las derivaciones de línea

|Ítem|Descripción|
|---|---|
|Voltaje nominal|220 KV|
|Voltaje máximo|245 KV|
|Capacidad máxima|760 MVA|
|N° Circuitos|2|
|N° Conductores/fase|2|
|Disposición de los circuitos|Vertical|
|Cable de guardia|Si|
|Cable de fibra óptica|Tipo OPGW, de 60 fibras|
|Conductor|AAAC 740.8 MCM (Flint) o similar|
|Temperatura máxima en emergencia|80° C|
|Distancia de fuga mínima|Clase III, IEC, 60815, 25 mm/KV|
|Tipo de estructuras|Metálicas enrejadas o tubulares, autosoportadas con<br>disposición vertical de circuitos|
|Altura de estructuras desde piso a punto más alto de<br>engrampe cable de guardia|Enrejadas: 43,2 m. Tubulares: 10 m|
|Cantidad de estructuras de anclaje|Cuatro|
|Cantidad de estructuras de suspensión|Seis|
|Vano mínimo|222 m|
|Vano máximo|232 m|
|Cadena de anclaje con aisladores de disco|Simple tipo ball and socket|
|Cadena de suspensión con aisladores de disco|Simple tipo ball and socket|
|Longitud|541 m - tramo norte<br>561 m - tramo sur|

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 6

### 5 Resultados

5.1 Subestación Adicional Puente Negro

5.1.1 Niveles de campos electromagnéticos y perturbaciones en subestación GIS de

220 kV

Las subestaciones tienen sus partes bajo tensión aisladas en gas hexafloruro de azufre (SF6), en lugar
de aislación en aire como en las subestaciones abiertas. Cada equipo de alta tensión, incluyendo las
barras principales o colectoras, está encapsulado independientemente en un compartimiento metálico
provisto de un ambiente de gas SF6 a presión mayor que la atmosférica. Se forman así módulos
individuales por equipo, que luego se interconectan mecánica y eléctricamente entre sí para formar
distintas configuraciones. En el caso de la subestación en estudio, los interruptores, transformadores de
medida y desconectadores son con tecnología GIS (subestación aislada en gas).

5.1.2 Campo magnético en el entorno de una subestación GIS

Para considerar el efecto de los equipos con tecnología GIS, se ha tomado la información publicada en la
referencia [2], que se reproduce en las siguientes figuras:

Figura 5-1 Gráfico 3-D densidad de campo magnético medido en el interior de una

subestación GIS de 220 kV [2]

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 7

Figura 5-2 Mapa de inducción magnética medida alrededor de la valla de

subestación GIS 22 kV [2]

Fuente: Elaboración propia.

Se observa una inducción magnética en el borde de la subestación de magnitud no superior a **13 [micro**
**Tesla]** . Los valores medidos de los campos magnéticos a lo largo de la valla de la subestación son
relativamente bajos en comparación con valores en la subestación interior, debido a su distancia al
equipo energizado. Normalmente, los valores más altos de los campos magnéticos alrededor de la valla
son causados por las líneas aéreas y cables subterráneos que entran y salen de las subestaciones y no
por equipo de subestación.

5.1.3 Campo eléctrico provocado por la subestación GIS

En una subestación GIS, el campo eléctrico está confinado al interior del encapsulado. Adicionalmente,
como se trata de una instalación interior, las estructuras, al comportarse como medio conductor en baja
frecuencia, contribuyen a apantallar el campo eléctrico. Luego, el campo eléctrico en el exterior de los
equipos encapsulados es nulo.

5.1.4 Nivel de Radio Interferencia generado por subestación GIS

La interferencia generada por descarga corona en líneas de alta tensión corresponde a descargas
eléctricas parciales en el aire alrededor de los conductores, producidas por la alta magnitud de campo
eléctrico que provoca ionización del aire. En el caso de una subestación encapsulada, las descargas
parciales existentes son mínimas por su construcción blindada, lo cual evita radio interferencias y
disminuye el nivel de ruido. Dada la condición encapsulada de los conductores, en una estación GIS se
prevé una magnitud menor de radio interferencia que en una subestación abierta. En la referencia [3] se
incluye, entre otras subestaciones de diversos voltajes, valores medidos de radio interferencia en la

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 8

vecindad de la Gas-Insulated Substation London-Talbot 230 kV. Los valores medidos se pueden apreciar
en la Figura 5-3.

Figura 5-3 Medidas de RI en varias subestaciones GIS [4]

Fuente: Elaboración propia.

Figura 5-4 Esquema de Gas-Insulated Substation London-Talbot 230 kV [3]

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 9

Los valores de RI medidos a 0,5 MHz en el exterior de esta subestación (site 1 a site 5 en la Figura 5-3 y
en la Figura 5-4), están entre 41 y 50 [dB/ 1V/m] (QP). Esta radio interferencia es generada por
terminales o partes conductoras exteriores al encapsulado. Para efectos de comparación con la norma,
corresponde considerar las medidas en “site 2” y “site 3”, siendo el máximo valor medido 44 [dB/ 1V/m]
(QP).

5.1.5 Niveles de campos electromagnéticos y perturbaciones en patio de alta

tensión de 220 KV.

La metodología utilizada para estimar el campo electromagnético de frecuencia industrial consiste en una
modelación de los conductores de las líneas de 220 kV que cruzan el perímetro de la subestación,
utilizando elementos finitos y el software utilitario QuickField [1] para la solución del campo eléctrico y del
campo magnético.

El resultado del estudio de campos se presenta en la forma de un perfil de campo evaluado a una altura
de 1,0 m sobre el suelo, a través de la trayectoria A1 - A2 en el patio de 220 kV mostrada en la Figura
Figura 5-5; se escogió este perfil por atravesar las líneas de 220 kV, llegando al borde de la subestación.

Figura 5-5 Trayectoria escogida para cálculo de campos generados por líneas de

220 kV

Fuente: Elaboración propia.

Para el estudio, en el perfil en el patio de 220 kV, los conductores se consideraron a una altura de 15 m
sobre el suelo, con 4 m de separación entre los conductores de fases de las líneas. La corriente en líneas
de 220 kV se tomó 1.250 Amperes por fase. En los gráficos de la Figura 5-6 y Figura 5-7 se indica la
posición relativa de los conductores.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 10

Figura 5-6 Campo eléctrico a 1m sobre el suelo en Trayectoria A1 - A2

Fuente: Elaboración propia.

Figura 5-7 Inducción magnética a 1m sobre el suelo en trayectoria A1 - A2

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 11

La Tabla 5-1 resume los valores de campo eléctrico y magnético en los extremos de la trayectoria A1A2, es decir en el borde de la subestación.

Tabla 5-1 Campo eléctrico y campo magnético en borde de subestación

|Campo eléctrico<br>[V/m]|Inducción magnética<br>[micro Tesla]|
|---|---|
|430|3,8|

Fuente: Elaboración propia.

5.1.6 Radio interferencia generada por patio de alta tensión de 220 kV

En un conductor de una instalación de alta tensión (línea o subestación), está aplicado un elevado nivel
de voltaje respecto de tierra (decenas o centenas de kilo Volts), lo cual provoca un campo eléctrico
extremadamente alto en la superficie del conductor (del orden de 100 veces mayor que el existente a
nivel del suelo). Este campo eléctrico, aumentado aún más por la presencia de irregularidades en la
superficie del conductor (hebras, polvo, insectos, gotas de agua, etc.) provoca la ionización del aire en su
entorno inmediato: el aire pierde localmente su propiedad dieléctrica, produciéndose gran cantidad de
pequeñas descargas eléctricas en torno a la superficie del conductor. El efecto luminoso de estas
descargas, tanto en conductores como en aisladores, ha dado nombre a este fenómeno, conociéndose

como “corona”.

En la referencia [6] se informa de medidas efectuadas en una subestación de 115 kV antes y después de
su conversión a 230 kV, y también en una subestación regularmente operando en 230 kV. La Figura 5-8
indica el esquema de la subestación Pontchartrain, que modificó su nivel de tensión, y los puntos de

medida de radio interferencia

Figura 5-8 Esquema de subestación Pontchartrain y puntos de medida [6]

Fuente: Elaboración propia.

Los valores medidos de radio interferencia a distintas frecuencias en los puntos indicados, cuando la
subestación opera a 230 kV, se muestran en la Figura 5-9.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 12

Figura 5-9 Radio interferencia operando la subestación Pontchartrain a 230 kV [6]

Fuente: Elaboración propia.

En la misma referencia se incluye los valores obtenidos en otra subestación, Snakefarm, que opera en
230kV. La Figura 5-10 indica el esquema de la subestación y los puntos de medida de radio interferencia.

Figura 5-10 Esquema de subestación Snakefarm de 230 KV y puntos de medida [6]

Fuente: Elaboración propia.

La medida de radio interferencia a distintas frecuencias, entrega los valores mostrados en la Figura 5-11.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 13

Figura 5-11 Radio interferencia medida en puntos de borde subestación Snakefarm

230 kV [6]

Fuente: Elaboración propia.

De la información anterior se observa que en el caso de una subestación que ha sido transformada a 230
kV desde un nivel inferior de tensión, y en un diseño convencional de una subestación en 230 kV, el nivel
de radio interferencia no supera el valor 50 [dB/1V/m] en el contorno interior de la subestación. Para
efectos de comparación con valores de norma, se traslada este valor a una distancia 15 m hacia afuera
del borde de la subestación, obteniendo 42,04 [dB/ 1V/m].

5.2 Líneas de transmisión 2x220 kV

5.2.1 Estimación del campo eléctrico a 1 metro de altura sobre el suelo, provocado

por las líneas de 2x220 kV

Se analiza continuación la situación de las líneas en paralelo correspondiente a las líneas de 2x220 kV.
Con este propósito se efectúa una modelación de las líneas y se aplica el software QuickField [1] que
utiliza el método de elementos finitos para obtener campo eléctrico generado por los conductores
energizados y el campo magnético generado por las respectivas corrientes de línea. Para estimar el
campo magnético, se consideró una potencia de 760 MVA, lo que determina aproximadamente 1.000
Amperes por fase

La Figura 5-12 ilustra el modelo de elementos finitos para la derivación de líneas. Cabe recordar que las
líneas tienen dos conductores por fase.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 14

Figura 5-12 Modelo de elementos finitos para derivaciones de líneas

Fuente: Elaboración propia.

Se entrega a continuación los resultados de los perfiles de campo en planos transversales a la línea y a

1m de altura sobre el suelo.

Figura 5-13 Distribución de equipotenciales eléctricas en derivaciones de líneas

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 15

Figura 5-14 Campo eléctrico a 1m de altura sobre el suelo en derivaciones de líneas

Fuente: Elaboración propia.

Figura 5-15 Distribución de equipotenciales magnéticas en derivaciones de líneas

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 16

Figura 5-16 Inducción magnética a 1m de altura sobre el suelo en derivaciones de

líneas

Fuente: Elaboración propia.

La Tabla 5-2 resume los valores de campo eléctrico y magnético en el borde de la franja de seguridad de

las derivaciones, estimada en 25 m.

Tabla 5-2 Campo eléctrico y campo magnético en borde de franja de seguridad

|Campo eléctrico<br>[V/m]|Inducción magnética<br>[micro Tesla]|
|---|---|
|310|1,85|

Fuente: Elaboración propia.

5.2.2 Radio interferencia generada por las líneas de transmisión

La descarga corona en líneas aéreas de transmisión de alta tensión, corresponde a descargas eléctricas
parciales en el aire alrededor de los conductores, producidas por la alta magnitud de campo eléctrico en
la superficie, que provoca ionización del aire. Este fenómeno genera corrientes y campos
electromagnéticos de alta frecuencia que pueden provocar perturbaciones en la banda de frecuencia de
radio y televisión.

Se incluye a continuación el listado de salida de la aplicación del software LINEAS (elaboración propia),
que permite determinar gradiente en la superficie de conductores de líneas de Alta Tensión y radio
interferencia, para las estructuras de la Línea de Transmisión de 2x220 kV en estudio.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 17

Tabla 5-3 Listado de salida del software LINEAS

|Campo eléctrico y potencial inducido entorno a líneas de transmisión|Col2|
|---|---|
|Número total de conductores|14|
|Número de conductores activos|12|
|Número de cables de guardia|2|

|Circuito 1|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Fase|1|2|3|4|5|6|
|Numero de subconductores|2|2|2|2|2|2|
|Separación entre subconductores (cm)|40.00|40.00|40.00|40.00|40.00|40.00|
|Radio del subconductor (cm)|0.966|0.966|0.966|0.966|0.966|0.966|
|Ubicacion lateral del conductor (m)|-5.000|-7.000|-5.000|5.000|7.000|5.000|
|Altura conductor sobre el suelo (m)|34.000|27.000|20.000|34.000|27.000|20.000|

|Circuito 2|Col2|Col3|Col4|Col5|Col6|Col7|
|---|---|---|---|---|---|---|
|Fase|1|2|3|4|5|6|
|Numero de subconductores|2|2|2|2|2|2|
|Separación entre subconductores (cm)|40.00|40.00|40.00|40.00|40.00|40.00|
|Radio del subconductor (cm)|0.966|0.966|0.966|0.966|0.966|0.966|
|Ubicacion lateral del conductor (m)|31.000|29.000|31.000|41.000|43.000|41.000|
|Altura conductor sobre el suelo (m)|34.000|27.000|20.000|34.000|27.000|20.000|

|Cables de guardia|Col2|Col3|
|---|---|---|
||1|2|
|Radio del subconductor(cm)|0.4762|0.4762|
|Ubicacion lateral del conductor (m)|0.000|36.000|
|Altura conductor sobre el suelo (m)|43.000|43.000|

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 18

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 19

|Col1|( -63.5085, 110.0000 ) 127.0170<br>( -63.5085, 110.0000 ) 127.0170<br>( -63.5085, -110.0000 ) 127.0170<br>( 127.0170, 0.0000 ) 127.0170<br>( 127.0170, 0.0000 ) 127.0170<br>( -63.5085, -110.0000 ) 127.0170<br>( -63.5085, 110.0000 ) 127.0170<br>( -63.5085, 110.0000 ) 127.0170<br>( -63.5085, -110.0000 ) 127.0170<br>( 127.0170, 0.0000 ) 127.0170<br>( .0000, .00000 ) .0000<br>( .0000, 0.0000 ) .0000|Col3|
|---|---|---|
||**Cargas en conductores (Cb)/(2piE0)**|**Cargas en conductores (Cb)/(2piE0)**|
||( 26.6334, 1.2252 ) 26.6615<br>( -13.7223, -23.6203 ) 27.3170<br>( -12.3689, 23.7851 ) 26.8089<br>( -12.5249, 23.9052 ) 26.9876<br>( -13.5897, -23.5067 ) 27.1522<br>( 26.9471, 1.1762 ) 26.9728<br>( 26.9649, 1.1058 ) 26.9876<br>( -13.5625, -23.5224 ) 27.1522<br>( -12.4550, 23.9250 ) 26.9728<br>( -12.2557, 23.6778 ) 26.6615<br>( -13.5946, -23.6940 ) 27.3170<br>( 26.7829, 1.1807 ) 26.8089<br>( -.6990, -.8755 ) 1.1203<br>( -.4087, -1.0431 ) 1.1203|( 26.6334, 1.2252 ) 26.6615<br>( -13.7223, -23.6203 ) 27.3170<br>( -12.3689, 23.7851 ) 26.8089<br>( -12.5249, 23.9052 ) 26.9876<br>( -13.5897, -23.5067 ) 27.1522<br>( 26.9471, 1.1762 ) 26.9728<br>( 26.9649, 1.1058 ) 26.9876<br>( -13.5625, -23.5224 ) 27.1522<br>( -12.4550, 23.9250 ) 26.9728<br>( -12.2557, 23.6778 ) 26.6615<br>( -13.5946, -23.6940 ) 27.3170<br>( 26.7829, 1.1807 ) 26.8089<br>( -.6990, -.8755 ) 1.1203<br>( -.4087, -1.0431 ) 1.1203|
||**Gradientes superficiales (kVef./cm)**|**Gradientes superficiales (kVef./cm)**|
||( 14.4512, 0.6648 ) 14.4665<br>( -7.4457, -12.8163 ) 14.8222<br>( -6.7113, 12.9057 ) 14.5465<br>( -6.7960, 12.9709 ) 14.6434<br>( -7.3738, -12.7547) 14.7328<br>( 14.6215, 0.6382) 14.6354<br>( 14.6311, 0.6000 ) 14.6434<br>( -7.3590, -12.7632 ) 14.7328<br>( -6.7581, 12.9817 ) 14.6354<br>( -6.6499, 12.8475 ) 14.4665<br>( -7.3764, -12.8563 ) 14.8222<br>( 14.5324, 0.6407 ) 14.5465<br>( -1.4677, -1.8383 ) 2.3523<br>( -.8581, -2.1902 ) 2.3523|( 14.4512, 0.6648 ) 14.4665<br>( -7.4457, -12.8163 ) 14.8222<br>( -6.7113, 12.9057 ) 14.5465<br>( -6.7960, 12.9709 ) 14.6434<br>( -7.3738, -12.7547) 14.7328<br>( 14.6215, 0.6382) 14.6354<br>( 14.6311, 0.6000 ) 14.6434<br>( -7.3590, -12.7632 ) 14.7328<br>( -6.7581, 12.9817 ) 14.6354<br>( -6.6499, 12.8475 ) 14.4665<br>( -7.3764, -12.8563 ) 14.8222<br>( 14.5324, 0.6407 ) 14.5465<br>( -1.4677, -1.8383 ) 2.3523<br>( -.8581, -2.1902 ) 2.3523|

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 20

Fuente: Elaboración propia.

5.3 Normativa aplicable

5.3.1 Normas de referencia aplicables en Chile respecto de la exposición humana a

campos electromagnéticos de 50 Hz

En nuestro país no existe reglamentación relativa a los valores límites permitidos de exposición de las
personas a los campos electromagnéticos de frecuencia industrial. No obstante, la regulación ambiental
que rige el tema de emisiones señala que de no existir una regulación nacional, debe aplicarse como
norma de referencia aquella que se encuentre vigente en estados específicos. El Decreto Supremo 40 del
Ministerio del Medio Ambiente, publicado en el D.O. del 12-08-2013, indica en su Artículo 11:

Artículo 11.- Normas de referencia.

_“Las normas de calidad ambiental y de emisión que se utilizarán como referencia para los efectos de_
_evaluar si se genera o presenta el riesgo indicado en la letra a) y los efectos adversos señalados en la_
_letra b), ambas del artículo 11 de la Ley, serán aquellas vigentes en los siguientes Estados: República_
_Federal de Alemania, República Argentina, Australia, República Federativa del Brasil, Canadá, Reino de_
_España, Estados Unidos Mexicanos, Estados Unidos de América, Nueva Zelandia, Reino de los Países_
_Bajos, República Italiana, Japón, Reino de Suecia y Confederación Suiza. Para la utilización de las_
_normas de referencia, se priorizará aquel Estado que posea similitud en sus componentes ambientales,_
_con la situación nacional y/o local, lo que será justificado razonablemente por el proponente.”_

La Tabla 5-4 presenta las principales normas de referencia aplicables en Chile, de acuerdo a lo señalado
en el Artículo anterior. Se agrega al final de la Tabla la normativa propuesta por la ICNIRP (Comisión
Internacional para la Protección contra la radiación No Ionizante), la IEEE (Instituto de Ingenieros
Eléctricos y Electrónicos) y el Consejo de Unión Europea (CEU).

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 21

Tabla 5-4 Normativa para campo eléctrico y magnético de 50 Hz

|País|Público general|Col3|Exposición ocupacional|Col5|
|---|---|---|---|---|
|**País**|**Campo Eléctrico**|**Campo**<br>**magnético**|**Campo**<br>**Eléctrico**|**Campo**<br>**magnético**|
|**País**|**[V/m]**|**[****Tesla]**|**[V/m]**|**[****Tesla]**|
|Alemania|5.000|100|5.000|100|
|Argentina|3.000|25|3.000|25|
|Australia|5.000|100|10.000|500|
|Canadá|No existe|No existe|No existe|No existe|
|España|CEU|CEU|CEU|CEU|
|Italia|5.000|10|5.000|10|
|Japón|3.000|No existe|ICNIRP|ICNIRP|
|U.S.A.|2.000|15 - 20|2.000|15 - 20|
|Reino de los Países Bajos (Gobierno)<br>(Consejo de Salud)|ICNIRP<br>8.000|ICNIRP<br>120|ICNIRP<br>40.000|ICNIRP<br>600|
|Suiza|5.000|100|5.000|1|
|ICNIRP|5.000|100|10.000|500|

Fuente: Elaboración propia.

La recomendación de uso más frecuente a nivel internacional es la establecida por la ICNIRP [6] que
define 5.000 [V/m] para campo eléctrico y 100 [micro Tesla] para campo magnético. Una de las normas
más restrictivas en cuanto a magnitudes permisibles es la norma Argentina [4], que se tomará como
referencia, considerando por lo tanto los límites 3.000 [V/m] para campo eléctrico y 25 [micro Tesla] para
campo magnético.

5.3.2 Radio Interferencia

Según norma canadiense [4], el valor de radio interferencia característica de una línea está normalizada,
para medida o estimación, a una frecuencia de 0,5 MHz; a una distancia lateral de 15 metros de la fase
externa y una altura de antena de 2 metros. Existen factores de corrección para evaluar la perturbación a
otras distancias y otras frecuencias (Tabla 5-5).

<!-- INICIO TABLA 5-5 -->
<!-- Confianza de extracción: 1.00 -->
<!-- Contexto previo: -->
<!-- Según norma canadiense [4], el valor de radio interferencia característica de una línea está normalizada, para medida o estimación, a una frecuencia de 0,5 MHz; a una distancia lateral de 15 metros de la fase externa y una altura de antena de 2 metros. Existen factores de corrección para evaluar la perturbación a otras distancias y otras frecuencias (Tabla 5-5). -->

**Tabla 5-5: Radio interferencia aceptable a 0,5 MHz y a 15 m de distancia de fase**

| Tensión eléctrica<br>nominal entre fases<br>(kV) | Intensidad del campo de ruido<br>electromagnético (dB sobre 1<br>μV/m) |
| --- | --- |
| Bajo 70 | 43 |
| 70 - 200 | 49 |
| 200 - 300 | 53 |
| 300 - 400 | 56 |
| 400 - 600 | 60 |
| Sobre 600 | 63 |

<!-- Estadísticas: 6 filas, 2 columnas -->
<!-- Contexto posterior: -->
<!-- Fuente: Elaboración propia. Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 22 -->
<!-- FIN TABLA 5-5 -->


Tabla 5-5 Radio interferencia aceptable a 0,5 MHz y a 15 m de distancia de fase

externa

|Tensión eléctrica<br>nominal entre fases<br>(kV)|Intensidad del campo de ruido<br>electromagnético (dB sobre 1<br>μV/m)|
|---|---|
|Bajo 70|43|
|70 - 200|49|
|200 - 300|53|
|300 - 400|56|
|400 - 600|60|
|Sobre 600|63|

Fuente: Elaboración propia.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 22

Para una línea de 220 kV, el límite correspondiente es 53 [dB/(1V/m)] a 15 m de distancia lateral desde

el conductor externo. Para una subestación de 220 kV, el límite es el valor anterior, a 15 m desde el

borde de la subestación.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 23

### 6 Conclusiones

6.1 Subestación Adicional Puente Negro

6.1.1 Subestación GIS de 220 kV

En la subestación el campo eléctrico está confinado al interior del encapsulado. Adicionalmente, como se
trata de una instalación interior, las estructuras, al comportarse como medio conductor en baja frecuencia,
contribuyen a apantallar el campo eléctrico. En consecuencia, el campo eléctrico en el exterior de la

subestación es nulo.

La magnitud de inducción magnética es elevada al interior de la subestación, pero se reduce en el borde
de la subestación a magnitudes no superiores a 13 [micro Tesla] inferior al límite más restrictivo de 25

[micro Tesla] considerado seguro por la normativa argentina.

La magnitud de radio interferencia generada por la subestación se estima en 44 [dB/ 1V/m] a 0,5 MHz,
inferior al valor límite de 53 [dB/1 V/m] propuesto en la reglamentación canadiense.

6.1.2 Patio de alta tensión de 220 kV

De acuerdo a la simulación efectuada, la magnitud de campo eléctrico a un metro de altura sobre el suelo
en el borde de la subestación abierta es 430 [V/m], inferior al límite más restrictivo de 3.000 [V/m]
considerado seguro por la normativa argentina.

En la simulación se observa una magnitud de inducción magnética elevada al interior de la subestación,
pero se reduce en el borde de la subestación a magnitudes no superiores a 3,8 [micro Tesla] inferior al
límite más restrictivo de 25 [micro Tesla] considerado seguro por la normativa argentina.

La magnitud de radio interferencia generada por la subestación abierta, conforme a referencias
bibliográficas, se estima en 42 [dB/ 1V/m] a 0,5 MHz, inferior al valor límite de 53 [dB/1 V/m] propuesto
en la reglamentación canadiense.

6.2 Líneas de transmisión 2x220 kV

La magnitud de campo eléctrico existente a un metro de altura sobre el suelo en el borde de la franja de
seguridad de las derivaciones de línea de 2x220 kV, no supera 310 [Volt/m], por tanto inferior al límite
más restrictivo de 3.000 [V/m] considerado seguro por la normativa argentina.

La magnitud de inducción magnética máxima existente a un metro de altura sobre el suelo en el borde de
la franja de seguridad de las líneas de 2x220 kV operando con corriente de 1.000 Amperes equilibrados
en régimen permanente, es de 1,85 [micro Tesla], inferior al límite más restrictivo de 25 [micro Tesla]
considerado seguro por la normativa argentina.

El ruido de radio frecuencia máximo estimado es 32,14 [dB/1 V/m], en condiciones de buen tiempo; bajo
lluvia intensa, condición en que se produce el mayor efecto corona, el ruido de radio frecuencia aumenta
17 dB adicionales, llegando a 49,14 [dB/1 V/m]. Ambos valores están, bajo el valor 53 [dB/ 1 V/m]

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 24

propuesto como límite tolerable por la normativa canadiense para el nivel de voltaje de la línea, en el
límite de la franja de servidumbre.

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 25

### 7 Referencias

[1] Students' QuickField (TM) Finite Element Analysis System.Copyright (C) Tera Analysis Company,
1995.

[2] Measuring human exposure to magnetic fields at LV and HV substations near residential areas

K. Ellithy ; A. Al-Jomaili ; A. Alshafai
Department of Electrical Engineering, Qatar University, Qatar
Paper C3-110 CIGRE 2012

[3] Radio interference and transient field from gas-insulated substations
S . M. Harvey, P.S. Wong, P.M. Balma,
IEEE Transactions on Power Delivery, Vol. 10, No. 1, January 1995

[4] Secretaría de Energía - Energía Eléctrica - Resolución 77/98

Amplíanse las condiciones y requerimientos fijados en el "Manual de Gestión Ambiental del
Sistema de Transporte Eléctrico de Extra Alta Tensión", aprobado por la Resolución No 15/92.
Bs. As., 12/03/98.

[5] Valeurs limites et methods de mesure du bruit électromagnétique (0,15 à 30 MHz) produit par les
reseaux de courant alternatif.
Association canadienne de normalisation, CAN3- C108.3.1 - M84. Octobre 1984.

[6] Carter R. T. ; Grille A. W. ; Bazile G. M. ; Perkins M. D. ; Mauser S. F. « Analysis of radio
interference and substation modifications for uprating a 115- KV substation to 230 KV” IEEE
Transactions on Power Delivery 1987, vol. 2, no2, pp. 544-550 (5 ref.)

Declaración de Impacto Ambiental Subestación Adicional Puente Negro Anexo H | 26

## Apéndices Apéndices

**Apéndice H.1 Norma Argentina**

(PDF Adjunto)

**Secretaría de Energía**
**ENERGIA ELECTRICA**
**Resolución 77/98**
**Amplíanse las condiciones y requerimientos fijados en el "Manual de Gestión Ambiental del Sistema de**
**Transporte Eléctrico de Extra Alta Tensión", aprobado por la Resolución No 15/92.**
**Bs. As., 12/03/98.**
**B. O.: 18/03/98.**
VISTO el Expediente N° 750-000230/97 del Registro del MINISTERIO DE ECONOMIA Y OBRAS Y SERYICIOS
PUBLICOS, y
CONSIDERANDO:
Que la Resolución SECRETARIA DE ENERGIA N° 15 de fecha 11 de septiembre de 1.992, aprobó el "Manual de
Gestión Ambiental del Sistema de Transporte Eléctrico de Extra Alta Tensión" fundada en la Resolución
SECRETARIA DE ENERGIA No 475 de fecha 4 de septiembre de 1.987 que prevé los mecanismos para la
dimensión ambiental en los proyectos y obras energéticas y en diseño, construcción y explotación de líneas de
transmisión y estaciones transformadoras y/o de compensación de Extra Alta Tensión, desde la etapa del proyecto
hasta la explotación.
Que el Artículo 17 de la Ley N° 24.065 establece que la infraestructura física, las instalaciones y la operación de los
equipos asociados a la generación, transporte y distribución de energía eléctrica deberán adecuarse a las medidas
destinadas a la protección de los ecosistemas involucrados, respondiendo a los estándares de emisión de
contaminantes vigentes y los que establezca en el futuro, en el orden nacional, la SECRETARIA DE ENERGIA del
MINISTERIO DE ECONOMIA Y OBRAS Y SERYICIOS PUBLICOS.
Que el Artículo 17 del Decreto N° 1398 del 11 de agosto de 1.992 reglamentario de la Ley N° 24.065 establece que
la ex-SECRETARIA DE ENERGIA ELECTRICA, hoy SECRETARIA DE ENERGIA del MINISTERIO DE ECONOMIA
Y OBRAS Y SERYICIOS PUBLICOS deberá determinar las normas de protección de cuencas hídricas y
ecosistemas asociados, a las cuales deberán ajustarse los generadores, transportistas y distribuidores de energía
eléctrica, en lo referente a la infraestructura física, las instalaciones y las operaciones de sus equipos.
Que para la elaboración de la norma ha intervenido el INSTITUTO DE INVESTIGACIONES TECNOLOGICAS PARA
REDES Y EQUIPOS ELECTRICOS (IITREE), en el marco del Convenio celebrado entre la ex-SUBSECRETARIA
DE ENERGIA ELECTRICA y la UNIVERSIDAD NACIONAL DE LA PLATA.
Que así también se ha dado intervención en la elaboración a la SECRETARIA DE POLITICA Y REGULACION DE
SALUD del MINISTERIO DE SALUD Y ACCION SOCIAL, al CONSEJO NACIONAL DE INVESTIGACIONES
CIENTIFICAS Y TECNICAS (CONICET) de la SECRETARIA DE CIENCIA Y TECNOLOGLA, a la SECRETARIA DE
RECURSOS NATURALES Y DESARROLLO SUSTENTABLE dependiente de PRESIDENCIA DE LA NACION, al
ENTE NACIONAL REGULADOR DE LA ELECTRICIDAD (ENRE), a la ASOCIACION DE GENERADORES DE
ENERGIA ELECTRICA DE LA REPUBLICA ARGENTINA (AGEERA), a la ASOCIACION DE DISTRIBUIDORES DE
ENERGIA ELECTRICA DE LA REPUBLICA ARGENTINA (ADEERA), a la ASOCIACION DE TRANSPORTISTAS
DE ENERGIA ELECTRICA DE LA REPUBLICA ARGENTINA (ATEERA).
Que desde el punto de vista de la protección ambiental, y atento el estudio oportunamente otorgado por el
INSTITUTO DE INVESTIGACIONES TECNOLOGICAS PARA REDES Y EQUIPOS ELECTRICOS (IITREE), es
recomendable adoptar, con un criterio de precaución, valores de exposición a campos electromagnéticos de baja
frecuencia.
Que, para ello, resulta necesario ampliar las condiciones y requerimientos fijados en el "Manual de Gestión
Ambiental del Sistema de Transporte Eléctrico de Extra Alta Tensión", aprobado por la Resolución de la
SECRETARIA DE ENERGIA N° 15 del 11 de septiembre de 1.992.
Que la DIRECCION GENERAL DE ASUNTOS JURIDICOS del MINISTERIO DE ECONOMIA Y OBRAS Y
SERVICIOS PUBLICOS ha tomado la intervención que le compete.
Que la SECRETARIA DE ENERGIA dependiente del MINISTERIO DE ECONOMIA Y OBRAS Y SERVICIOS
PUBLICOS se encuentra facultada para el dictado del presente acto, en virtud de lo dispuesto por el Artículo 17 de la
ley No 24.065 y de su Decreto Reglamentario N° 1398 del 11 de agosto de 1.992.
Por ello,
EL SECRETARIO DE ENERGIA

RESUELVE:
**Artículo 1°-** Las disposiciones del "Manual de Gestión Ambiental del Sistema de Transporte Eléctrico de Extra Alta
Tensión", aprobado por la Resolución SECRETARIA DE ENERGIA N° 15 del 11 de septiembre de 1.992, serán
aplicables a toda empresa u organismo, sea cual fuere su naturaleza jurídica, que tenga a su cargo la realización de
proyectos y/o ejecución de, obras de líneas de transmisión, estaciones transformadoras y/o compensadoras de
tensión igual o mayor a CIENTO TREINTA Y DOS KILOVOLTIOS (132 kV), por su condición de titular de una
concesión sujeta a jurisdicción nacional sea ésta de Transporte de Interconexión Internacional, de Transporte de
Energía Eléctrica en Alta Tensión, de Transporte de Energía Eléctrica por Distribución Troncal, o de distribución de
Energía Eléctrica así como para actuar como transportista independiente.
Considerase, asimismo, alcanzados por las disposiciones del "Manual de Gestión Ambiental del Sistema de
Transporte Eléctrico de Extra Alta Tensión" a todo sujeto de derecho que obtenga una autorización de excepción

para la construcción de instalaciones de transporte de energía eléctrica en los términos del Artículo 31 de la Ley N°
24.065, así como a todo transportista independiente.
**Art. 2°-** Sustitúyese la denominación "Manual de Gestión Ambiental del Sistema de Transporte Eléctrico de Extra
Alta Tensión" a que se hace referencia en el artículo precedente por la de "Manual de Gestión Ambiental del Sistema
de Transporte Eléctrico".
**Art. 3o-** Sustitúyese el Anexo I "Valores Orientativos" de la Resolución SECRETARIA DE ENERGIA N° 15 de fecha
11 de septiembre de 1.992 por los "Parámetros Ambientales" que como Anexo I forman parte integrante del presente
acto. Dichos "Parámetros Ambientales" serán de aplicación obligatoria para todo sujeto comprendido en el artículo
precedente.
**Art. 4°-** La empresa u organismo, sea cual fuere su naturaleza jurídica, cuya actividad se encuentre sujeta a
jurisdicción nacional, y tenga a su cargo la realización de proyectos y/o ejecución de obras de líneas de transmisión
y distribución de tensión igual o superior a TRECE CON DOS DECIMAS DE KILOVOLTIOS (13,2 kV) e inferiores a
CIENTO TREINTA Y DOS KILOVOLTIOS (132 kV) y estaciones transformadoras y/o puestos de transformación y
compensación, deberán cumplir con las "Condiciones y Requerimientos" que como Anexo II forman parte integrante
de la presente Resolución.
**Art. 5o-** Toda violación o incumplimiento de la presente norma deberá ser subsanado en término perentorio que a
tales efectos fije el ENTE NACIONAL REGULADOR DE LA ELECTRICIDAD (ENRE).
Si persistiera transcurrido el plazo definido en el apercibimiento, la violación o el incumplimiento, el ENTE
NACIONAL REGULADOR DE LA ELECTRICIDAD (ENRE) podrá ordenar la interrupción de la construcción y/o
funcionamiento de la instalación afectada, bajo responsabilidad y a costa y cargo del incumplidor el que
adicionalmente será pasible de la sanción de multa entre PESOS MIL ($ 1.000) y PESOS UN MILLON ($ 1.000.000).
Queda especificado que la interrupción es de carácter preventivo y se mantendrá la misma hasta que la violación o
el incumplimiento sea subsanado.
**Art. 6°-** Deróganse los Artículos 2°, 4°, 5° y 6° de la Resolución de la SECRETARIA DE ENERGIA N° 15 del 11 de
septiembre de 1.992.
**Art. 7°-** El presente acto comenzará a regir a partir del día siguiente de la fecha de su publicación.
**Art. 8°-** Notifíquese al ENTE NACIONAL REGULADOR DE LA ELECTRICIDAD (ENRE).
**Art. 9°-** Comuníquese, publíquese, dése a la Dirección Nacional del Registro Oficial y archívese. - Alfredo H. Mirkin.
ANEXO I
PARAMETROS AMBIENTALES
Con el objeto de incentivar un mejoramiento global de la compatibilidad de los electroductos con el ambiente, deben
considerarse los efectos originados por:
1 - Impacto visual
2 - Efecto corona: radiointerferencia ruido audible

3 - Ruido
4-Campos de baja frecuencia: eléctrico de inducción magnética
1. IMPACTO VISUAL
En toda instalación eléctrica se deberá considerar la relación entre la obra y el paisaje en sus aspectos directos, esto
es por la interposición física de los soportes, torres y de los conductores y en sus aspectos indirectos en la
degradación de la percepción del observador de áreas naturales, arquitectónicas, históricas o paisajísticas, ya que
representan una instrusión extraña en dicho contexto.
Para identificar la sensibilidad de los recursos naturales, predecir el impacto, incorporar cambios en la traza y en el
diseño que permitan reducir el impacto visual adverso, los proyectistas se deberán basar en TRES (3) aspectos
importantes: visibilidad, contexto e intensidad, los que juntos forman la estructura conceptual de la evaluación de tal
impacto.
Como mínimo, la visibilidad necesita ser determinada desde estos puntos particulares:
a) Areas reconocidas como de contenido escénico, recreativas, culturales, históricas
b) Corredores de electroductos
c) Areas residenciales
d) Distritos comerciales
e) Areas de visión pública significativa
La evaluación de la visibilidad debe tener en cuenta además factores topográficos, vegetativos, y estacionales (de
temporada).
La visibilidad provee un punto de partida definitivo para posteriores evaluaciones, si no hay visibilidad no hay
impacto visual, y no serían necesarios posteriores análisis.
El contexto dentro del cual la instalación será ubicada y percibida, es fundamental para el impacto visual. Los
factores que permiten considerarlo:
a) Que tipo de uso se le da a la tierra donde se hará la instalación
b) Que actividades desarrollan los potenciales espectadores
c) Cuales son las expectativas escénicas respecto del paisaje.

Dado que es imposible ocultar completamente una línea de alta tensión, es necesario establecer prioridades que
permitan determinar dónde dichas instalaciones son visualmente apropiadas o inapropiadas, es decir cuales paisajes
son particularmente sensibles.
Una forma de definir la característica de sensibilidad de un paisaje es a través de factores definidos como: calidad
escénica, uso de la tierra o actividad, número de espectadores e instalaciones existentes.
Finalmente, para evaluar tal sensibilidad, el analista debe determinar la intensidad visual, a través del estudio de
características específicas de la instalación propuesta.
Los factores que permiten considerar la intensidad son los siguientes:
a) Relieve o prominencia, es decir la posición que la intrusión visual ocupa dentro de la panorámica de una zona
dada.
b) Contraste, es decir, cómo la instalación se destaca sobre el fondo
c) Distancia desde donde es vista la instalación.
d) Duración de la instalación en el tiempo.
e) Expansión que ocupa la instalación.
f) Escala de la instalación, referida al tamaño en comparación con otros elementos, tales como árboles, sierras,
edificios, etc.
g) Diseño, en cuanto al color, material, textura y forma.
Para el análisis de las alternativas, se deberán incorporar al proyecto pautas que eviten un impacto visual
significativo y de minimización de afectación del espacio, considerando los siguientes aspectos:
a) Minimizar el impacto visual de la obra con relación a la apreciación panorámica del paisaje.
b) Seleccionar tecnologías, actualmente disponibles y con posibilidades de aplicación, que reduzcan la ocupación
del espacio y el impacto visual, tales como: la utilización de mensuras aislantes en líneas aéreas (fine post):
utilización de estructuras tubulares, etc.
c) En zonas pobladas, realizar el emplazamiento de las columnas en sitios donde la afectación a los frentistas sea la
menor posible y alejados de predios destinados a alojar o realizar actividades tales como escuelas, hospitales,
geriátricos, etc.
d) Evitar el empleo de superficies metálicas brillantes en zonas de alto valor paisajístico, sin perjuicio de cumplir con
las restricciones de seguridad que correspondan (aeropuertos, cruce de rutas, etc.).
e) Evitar la proximidad a instalaciones de almacenamiento de combustibles.
El estudio de impacto deberá comprender un examen de las diversas alternativas que la tecnología actual permite
considerar, seleccionando aquella que posea un mejor perfil ambiental.
2. EFECTO CORONA
2.1 Radiointerferencia
El campo perturbador generado por la línea ocasiona, en los radiorreceptores que se encuentran dentro de su zona
de influencia, un ruido característico. Las principales fuentes de interferencia en las comunicaciones de radio,
originadas en instalaciones de ALTA TENSION (AT), pueden ser separadas en DOS (2) tipos:
a) Descargas corona (descargas eléctricas parciales en un medio dieléctrico gaseoso, en regiones de alta intensidad
de campo eléctrico del entorno de los conductores). Estas dependen del diseño de la línea y las condiciones
climáticas, e interfieren casi exclusivamente en la banda de frecuencias inferiores a TREINTA MEGAHERTZ (30
MHz) (radio AM), fenómeno reconocido como RADIOINTERFERENCIA (RI).
b) Descargas disruptivas (microdescargas que tienen lugar generalmente en la morsetería y que se deben a falsos
contactos o a imperfecciones en el ensamble entre un aislador y su morsetería). Estas dependen de aspectos
constructivos e interfieren en un espectro que alcanzan los centenares de MHa (radio FM y TV). Los elementos de
las líneas y las subestaciones deben ser ensayados y cumplir con los requerimientos de radiointerfereneia indicados
en los procedimientos del COMITE INTERNACIONAL ESPECIAL DE PERTURBACIONES RADIOELECTRICAS
(CISPR) N° 18 Partes 1, 2 y 3. (COMITE INTERNACIONAL ESPECIAL DE PERTURBACIONES
RADIOELECTRICAS (CISPR) N° 18: Características de líneas y equipamientos de alta tensión relativas a
perturbaciones radioeléctricas; Parte 1: Descripción del problema, Parte 2: Métodos de medición y procedimientos
para la determinación de límites, Parte 3: Práctica para minimizar la generación de ruido). Cumplidos los
requerimientos anteriores, el cálculo de los niveles de RADIOINTERFERENCIA (RI) se realiza sólo por descarga
corona en los conductores. El nivel tolerable de RADIOINTERFERENCIA (RI) depende de:
c) Los tipos de comunicaciones a proteger.
d) Los niveles de señal de las comunicaciones a proteger.
e) El nivel de la calidad de la recepción.
f) Los límites de tiempo en la interferencia prevista.
Para la definición de la franja perturbada, se utilizarán los procedimientos indicados por el COMITE
INTERNACIONAL ESPECIAL DE PERTURBACIONES RADIOELECTRICAS (CISPR) N° 18- 1, 2 y 3.
De acuerdo con las normas de la Comisión Nacional de Telecomunicaciones, se fija un nivel máximo de
RADIOINTERFERENCIA (RI) en: CINCUENTA Y CUATRO DECIBELES (54 dB) durante el OCHENTA POR
CIENTO (80 %) del tiempo, en horarias diurnos (Norma SC-S3.80.02/76- Resolución ex-SC N° 117/78), medidos a
una distancia horizontal mínima de CINCO (5) veces la altura de la línea aérea en sus postes o torres de suspensión
(Norma SC-M- 150.01).

Se fija un valor de máxima interferencia de TREINTA DECIBELES (30dB), para protección de señales radiofónicas,
con calidad de recepción de interferencia no audible (Código 5 de CIGRE).
2.2 Ruido Audible
La presencia de efecto corona en conductores de líneas de alta tensión puede dar origen a sonidos audibles (RA:
ruido audible). Al igual que en el caso de RADIOINTERFERENCIA (RI), la intensidad de dicho ruido depende del
gradiente superficial de campo eléctrico en los conductores, de su estado superficial y de las condiciones
atmosféricas.
Estos niveles de perturbación de RUIDO AUDIBLE (RA) se incrementan junto con el nivel de tensión de operación
de los sistemas de transmisión, y comienza a tomar importancia para tensiones superiores a TRESCIENTOS
KILOVOLTIOS (300 kV), aproximadamente.
Se fija un límite de CINCUENTA Y TRES DECIBELES "A" [53 dB(A)], valor que no debe ser superado el
CINCUENTA POR CIENTO (50 %) de las veces en condición de conductor húmedo, a una distancia de TREINTA
METROS (30 m) desde el centro de la traza de la línea o en el límite de la franja de servidumbre o parámetro de una
estación transformadora.

3. RUIDO
En las subestaciones se evaluarán los datos garantizados de ruido máximo a producir por los transformadores u
otros equipos. Los mismos deberán cumplir con las exigencias de la norma IEC 651 (1987) e IRAM N° 4074-1/88
"Medición de niveles de presión sonora".
Se deberá cumplir con la norma IRAM N° 4062/84 (Ruidos molestos al vecindario).
4. CAMPOS DE BAJA FRECUENCIA
En presencia de campos eléctricos y magnéticos generados por las líneas, pueden aparecer por acoplamiento
electrostático (E/S) y acoplamiento magnético (E/M) tensiones y corrientes en instalaciones cercanas cuales como
alambrados, cercas, cañerías de riego, líneas de comunicación, etc., las cuales pueden tener efectos sobre las
personas y/o sobre las instalaciones.
Para atender los efectos de las líneas aéreas sobre circuitos de comunicaciones en las cercanías de instalaciones
de ALTA TENSION (A.T.) deben seguirse las directivas del COMITE CONSULTIVO INTERNACIONAL
TELEGRAFICO Y TELEFONICO (CCITT).
Para atender los efectos en las personas debidos a un eventual contacto con instalaciones cercanas a las líneas, se
adoptan valores límites de corrientes de contacto para un caso testigo, tal como se indica en los puntos 4.1 y 4.2.
Para atender los efectos en las personas debidos a la exposición a campos eléctricos y de inducción magnética, se
adoptan valores de máximo límite extremo tendientes a orientar la elección de los diseños de las futuras
instalaciones, teniendo en cuenta valores tan bajos como razonablemente alcanzables, y evitando los que puedan
producir campos de inducción magnética más intensos que los típicos para las líneas existentes, tal como se indica
en los puntos 4.1 y 4.2.
El estudio de evaluación de impacto deberá comprender un examen de las diversas alternativas de diseño que la
tecnología actual permita considerar, seleccionando aquella que contenga los valores de campos eléctricos y de
inducción magnética "tan bajos como sea razonablemente alcanzable".
4.1 Campo eléctrico:
En base a los documentos elaborados conjuntamente por la ORGANIZACION MUNDIAL DE LA SALUD (OMS), la
ASOCIACION INTERNACIONAL PROTECCION CONTRA LA RADIACION:N° IONIZANTE (IRPA), y el PROGRAMA
AMBIENTAL DE NACIONES UNIDAS, los cuales recopilan en diferente piases, los valores típicos de la mayoría de
las líneas que se encuentran en operación, se adopta el siguiente valor límite superior de campo eléctrico no
perturbado, para líneas en condiciones de tensión nominal y conductores a temperatura máxima anual: TRES
KILOVOLTIOS POR METRO (3 kV/m), en el borde de la franja de servidumbre, fuera de ella y en el borde perimetral
de las subestaciones, medido a UN METRO ( 1 M) del nivel del suelo.
Cuando no estuviera definida la franja de servidumbre, el nivel de campo deberá ser igual o inferior a dicho valor en
los puntos resultantes de la aplicación de las distancias mínimas establecidas en la Reglamentación de la
ASOCIACION ELECTRO TECNICA ARGENTINA (AEA) sobre Líneas Eléctrica Aéreas Exteriores.
El nivel máximo de campo eléctrico, en cualquier posición, deberá ser tal que las corrientes de contacto para un caso
testigo: niño sobre tierra húmeda y vehículo grande sobre asfalto seco, no deberán superar el límite de seguridad de
CINCO MILI AMPERIOS (5ma).
4.2 Campo de inducción magnética:
En base a la experiencia de otros países, algunos de los cuales han dictado normas interinas de campos de
inducción magnetices y a los valores típicos de las líneas- en operación, se adopta el siguiente valor límite
superiores de campo de inducción magnética para líneas en condiciones de máxima carga definida por el límite
térmico de los conductores: DOSCIENTOS CINCUENTA MILI GAUSSIOS (250 mG), en el borde de la franca de
servidumbre, fuera de ella y en el borde perimetral de las subestaciones, medido a UN METRO (1) del nivel del
suelo.
Cuando no estuviera definida la franca de servidumbre, el nivel de campo deberá ser igual o inferior a dicho valor en
los puntos resultantes de la aplicación de las distancias mínimas establecidas en la Reglamentación de la
ASOCIACION ELECTRO TECNICA ARGENTINA (AEA) sobre Líneas Eléctrica Aéreas Exteriores.

El nivel máximo de campo de inducción magnética, en cualquier posición, deberá ser tal que las corrientes de
contacto en régimen permanente, debido al contacto con objetos metálicos Largos cercanos a las líneas, no deberán
superar el límite de salvaguarda de CINCO MILI AMPERIOS (5mA).
CONDICIONES Y REQUERIMIENTOS
1. INTRODUCCION

ANEXO II
El presente Anexo forma parte de las acciones emprendidas por la SECRETARIA DE ENERGIA para evaluar y
controlar los efectos ambientales del abastecimiento eléctrico. y persigue alcanzar los siguientes objetivos:
Proporcionar el marco de referencia para la oportuna y adecuada consideración de aquellos aspectos ambientales
vinculados al proyecto, construcción y explotación de líneas de tensiones iguales o superiores a TRECE CON DOS
DECIMAS DE KILOVOLTIO (13,2 kV) e inferiores a CIENTO TREINTA Y DOS KILOVOLTIOS ( 132 kV) y de las
estaciones transformadoras y/o puestos de transformación y/o compensación correspondientes.
Orientar la identificación de las tareas necesarias para la gestión ambiental, en cada etapa del desarrollo de tales
obras, las que estarán integradas a la gestión global de las mismas.
La consideración de estos aspectos, permitirán optimizar la eficiencia de las instalaciones en el largo plazo y el
funcionamiento armónico con el ambiente, sobre todo cuanto a raíz de su emplazamiento se pueden generar o
potenciar determinados impactos y/o conflictos que pueden resultar gravosos para ambos componentes.
2. CONDICIONES

Se deberá:
a)Observar el cumplimiento estricto de la legislación ambiental, asumiendo la responsabilidad de adoptar las
medidas que correspondan para evitar efectos nocivos sobre el aire, el suelo, las aguas y otros componentes del
ambiente.
b) Mantener los equipos e instalaciones en condiciones tales que permitan niveles de contaminación menores o
iguales a los indicados por las leyes, decretos, reglamentaciones y normas que correspondan aplicar en cada caso
en particular.
c) Establecer y mantener durante el período de operación, sistemas de registro, a fin de facilitar la verificación del
cumplimiento de las normas de protección ambiental
3. REQUERIMIENTOS
Con el objeto de incentivar un mejoramiento global de la compatibilidad de las instalaciones con el ambiente, para
toda instalación nueva, ampliación o extensión de las existentes, deberán adecuarse las acciones a los parámetros
ambientales establecidos en el punto 4 del presente Anexo. El Informe sobre el tratamiento de tales parámetros
estará a disposición del ENTE NACIONAL REGULADOR DE LA ELECTRICIDAD (ENRE) para su presentación ante
dicho organismo, en la oportunidad que este lo requiera a los fines del cumplimiento del ejercicio de sus funciones.
Se deberá confeccionar el Plan de Gestión Ambiental correspondiente, para las etapas de construcción y operación
el cual cumplirá, en su presentación y ejecución, con los requerimientos establecidos en la Resolución ENTE
NACIONAL REGULADOR DE LA ELECTRICIDAD (ENRE) N° 32 de fecha 2° de abril de 1994, acerca de los
Procedimientos de programas de Gestión Ambiental.
4. PARAMETROS AMBIENTALES

4.1 OCUPACION DEL ESPACIO
El proyecto de un sistema de transmisión o distribución, como de cualquier otra obra, no puede prescindir de
considerar el daño potencial que puede originar al medio que lo circunda. En forma concreta ocupará un espacio
originando perturbaciones al ambiente natural y al ambiente social.
En el análisis de las alternativas de las obras, deberán considerarse los siguientes aspectos:
a) Reconocimiento de la estructura social y económica de las áreas afectadas por la traza de la línea y por el
emplazamiento de las estaciones y/o puestos de transformación y/o compensación, e identificación de los efectos
positivos y negativos a áreas productivas, zonas residenciales, de yacimientos arqueológicos o de interés histórico,
paisajístico y turístico, y a otros usos del espacio.
b) Estudio y evaluación de formas alternativas de acceso en aquellos tramos donde la línea atraviese zonas que
deban ser preservadas por razones del sistema natural, arqueológicas, históricas, paisajístas, económicas productivas. etc.
c) Prevalecer el uso de áreas en las que ya se encuentre modificado el sistema natural.
d) Evitar la proximidad e instalaciones de almacenamiento de combustibles.
e) Evitar en las estaciones transformadoras y puestos de transformación y/o de compensación. que resulten
contaminados los desagües pluviales y/o sanitarios con los líquidos de refrigeración.
f) Manejo adecuado en el movimiento de suelos, a fin de evitar la ocurrencia o aceleración de procesos erosivos, la
alteración de escurrimientos de aguas superficiales o su acumulación. '
Estas precauciones se adoptarán tanto en las zonas de servicio como en las zonas afectadas por las obras.
g) Tratamiento de las tierras afectadas por la construcción y emplazamiento de la línea y estaciones, tendientes a
restituirlas al término de los trabajos respectivos a su estado natural, al máximo que sea posible, compatible con el
servicio, y en el mínimo plazo.

h) En las zonas pobladas, se deberá respetar la trama urbana y tratar de utilizar espacios públicos no destinados a
parques, lugares turísticos o recreativos para la comunidad. Se sugiere el alejamiento de predios destinados a alojar
o realizar actividades tales como escuelas, hospitales, hospicios,: geriátricos, etc.
i) Garantizar el acceso a los inmuebles de los frentistas que se encuentren afectados a la obra, especialmnte en la
etapa de construcción de la misma.
j) Las excavaciones que se realicen para las instalaciones de cable subterráneo deben resguardar la presencia de
otros servicios, limitar la rotura de veredas y afectar mínimamente las raíces de los árboles.
k) Garantizar, en zonas pobladas, la circulación de vehículos y transeuntes en las etapas de construcción y
mantenimiento de las obras.
1) Desmontar los campamentos y obradores y demás instalaciones utilizadas durante la construcción y retirar todos
los materiales sobrantes o no usados, procurando restablecer los respectivos sitios a sus condiciones de origen.
m) Adoptar medidas de seguridad para evitar la ocurrencia de accidentes, cercando la zona de trabajo con varas que
garanticen la interrupción de la circulación.
Esta iniciativa se concreta, por un lado, con metodologías de proyecto que otorgan el peso justo a la instancia de
protección del ambiente, y por otro lado, mediante la introducción de nuevas tipologías de componentes,
particularmente compactos.
4.2 IMPACTO VISUAL
Una de las afectaciones más importantes es la que existe en la relación entre la obra y el paisaje, ya sea por
aspectos directos, esto es por la interposición física de los soportes o torres y de los conductores o por aspectos
indirectos en la degradación de la percepción del observador de áreas naturales, arquitectónicas, históricas o
paisajísticas, ya que representan una intrusión extraña en dicho contexto.
La ocupación del espacio y la perturbación visual son factores prioritarios del impacto de la línea aérea en el
ambiente.
Para identificar la sensibilidad de los recursos naturales, predecir el impacto, incorporar cambios en la traza y en el
diseño que permitan reducir el impacto visual adverso, los proyectistas se deberán basar en TRES (3) aspectos
importantes: visibilidad, contexto, e intensidad, los que/juntos forman la estructura conceptual de la valuación de tal
impacto.
Como mínimo la visibilidad necesitará ser determinada desde los siguientes puntos:
a) Areas reconocidas como de contenido escénico, recreativas, culturales, históricas .
b) Corredores de electroductos
c) Areas residenciales
d) Distritos comerciales
e) Areas de visión pública significativa
La evaluación de la visibilidad debe tener en cuenta además, factores topográficos, vegetativos y estacionales (de
temporada).
La visibilidad provee un punto de partida definitivo para posteriores evaluaciones, si no hay visibilidad no hay
impacto visual, y no serían necesarios posteriores análisis.
El contexto dentro del cual la instalación será ubicada y percibida, es fundamental para el impacto visual. Los
factores que permiten considerarlo son:
a) Que tipo de uso se le da a la tierra donde se hará la instalación
b)Que actividades desarrollan los potenciales espectadores
c) Cuales son las expectativas escénicas respecto del paisaje.
Dado que es imposible ocultar completamente una línea es necesario establecer prioridades que permitan
determinar donde dichas instalaciones son visualmente apropiadas o inapropiadas, es decir cuales paisajes son
particularmente sensibles. Una forma de definir las características de sensibilidad de un paisaje es a través de
factores definidos como: calidad escénica, uso de la tierra o actividad, número de espectadores e instalaciones
existentes.
Finalmente, para evaluar tal sensibilidad, el analista deberá determinar la intensidad visual, a través del estudio de
características específicas de la instalación propuesta.
Los factores que permiten considerar la intensidad son los siguientes:
a) Relieve o prominencia,es decir la posición que la intrusión visual ocupa dentro de la panorámica de una zona
dada.
b) Contraste, es decir como 1a instalación se destaca sobre el fondo
c) Distancia desde donde es vista la instalación.
d) Duración de la instalación en el tiempo.
e) Expansión que ocupa la instalación.
f) Escala de la instalación, referida en comparación con otros elementos tales como arboles, sierras, edificios, etc.
g) Diseño, en cuanto al color, material y forma.
Para el análisis de las alternativas, se deberán incorporar al proyecto pautas que eviten impactos visuales
significativos y de minimización de afectación del espacio mediante la consideración de los siguientes aspectos:

1. En áreas pobladas, considerar el uso de muros de elevación en la periferia las subestaciones, en lugar de
cercas metálicas. Implementar el tratamiento paisajístico con cercas vivas las que atenuarán el impacto
visual.
b) Adoptar proyectos de iluminación, para los patios externos, que sean compatibles con las necesidades de
operación y mantenimiento, de manera de evitar el realce innecesario o inadecuado de las instalaciones en el medio
que las circundan.
c) Seleccionar soportes de las líneas aéreas que se caractericen por minimizar su perceptibilidad.
d) En las líneas aéreas, considerar la utilización de ménsulas aislantes (line post), ya que disminuyen al mínimo la
distancia del conductor al soporte, reduciendo 1a ocupación del espacio y el impacto visual.
e) En las áreas pobladas, las columnas deben ser emplazadas en sitios donde la afectación a frentistas sea la menor
posible
f) Se debe minimizar la perceptibilidad de los gabinetes tipo "buzón" en los que se instalan tableros de baja tensión,
atendiendo a su diseño y al color de los mismos.
g) Considerar la utilización de conductores aislados, ya que resultan más seguras para las personas y las aves, por
reducción de la electrocución accidental, del impacto visual y de la ocupación del terreno. A la vez permite una mejor
inserción en zonas boscosas ya que se reduce drásticamente la tala de árboles, tanto en la fase de construcción
como como de operación.
h) Instalar las señalizaciones correspondientes, de acuerdo a 1as actividades que se desarrollen en las cercanías de
las líneas (aeropuertos, operaciones de grúas etc).
El estudio de evaluación de impacto deberá comprender un examen de las diversas alternativas que la tecnología
actual permite considerar, seleccionando aquella que posea un mejor perfil ambiental.
4.3 RADIOINTERFERENCIA
El campo perturbador generado por la línea ocasiona, en los radiorreceptores que se encuentren dentro de su zona
de influencia, un ruido característico.
Los elementos de las líneas y puestos de transformación, deben ser ensayados y cumplir los requerimientos de
radiointerferencia en los procedimientos del COMITE INTERNACIONAL ESPECIAL DE PERTURBACIONES
RADIOELECTRICAS (CISPR) N° 18 Partes 1,2 y 3.
Número 18: Característica de líneas y equipamientos de alta tensión relativas a perturbaciones radioeléctricas: Parte
1:Descripción del problema. Parte 2: Métodos de medición y procedimientos para la determinación de límites. Parte
3: Práctica para minimizar la generación de ruido).
Cumplidos los requerimientos anteriores, el cálculo de los niveles de RADIOINTERFERENCIA (RI) se realiza solo
por descarga corona en los conductores. El nivel tolerable de RADIOINTERFERENCIA (RI) depende de: los tipos de
comunicaciones a proteger, los niveles de señal de las comunicaciones, el nivel de calidad de la recepción y los
límites de tiempo en la interferencia prevista.
Para la definición de la franja perturbada, se utilizarán los procedimientos indicados por la norma del COMITE
INTERNACIONAL ESPECIAL DE PERTURBACIONES RADIOELECTRICAS (CISPR) N° 18 Partes 1, 2 y 3.
De acuerdo con las normas de la COMISION NACIONAL DE COMUNICACIONES, se fija un nivel máximo de
RADIOINTERFERENCIA (RI) en: CINCUENTA Y CUATRO DECIBELES (54 dB) durante el OCHENTA POR
CIENTO (80%) del tiempo, en horarios diurnos (Norma SC-S-3.80.02/76 - Resolución ex-SC No 117/78, medidos a
una distancia horizontal mínima de CINCO (5) veces la altura de la línea aérea en sus postes o torres de suspensión
(Norma SC-M- 1-50.01).
Se fija un valor de máxima interferencia de TREINTA DECIBELES (30 dB). para protección de señales radiofónica,
con calidad de recepción de interferencia no audible (Código 5 de CIGRE).
4.4. RUIDO
En las subestaciones se evaluarán los datos garantizados de ruido máximo a producir de los transformadores y otros
equipos. Los mismos, deberán cumplir con las exigencias de la norma IEC 651 (1987) e IRAM N° 4074- 1
/88"Medición de niveles de presión sonora".
Se deberá cumplir con la norma IRAM N° 4062 "Ruidos molestos al vecindario".
4.5. CAMPOS DE BAJA FRECUENCIA
En presencia de campos eléctricos y magnéticos generados por las líneas, pueden aparecer por acoplamiento
electrostático (E/S) y acoplamiento magnético (E/M) tensiones y corrientes en instalaciones cercanas, tales como
alambrados, cercas, cañerías de riego, líneas de comunicación, etc., las cuales pueden producir efectos sobre las
personas y/o las instalaciones.
Para atender los efectos de las líneas aéreas sobre circuitos de comunicaciones instalados en las cercanías de
instalaciones de ALTA TENSION (AT) deben-seguirse las directivas del COMITE CONSULTIVO INTERNACIONAL
TELEGRAFICO Y TELEFONICO (CCITT).
Para atender los efectos en las personas debidos a un eventual contacto con instalaciones cercanas, se adoptan
valores límites de corrientes de contacto para un caso testigo, tal como se indica en los puntos 4.5.1. y 4.5.2.
Para atender los efectos en las personas debidos a la exposición a campos eléctricos y de inducción magnética, se
adoptan valores de máximo límite extremo tendientes a orientar la elección de los diseños de las futuras
instalaciones de distribución de energía eléctrica, teniendo en cuenta valores tan bajos como razonablemente

alcanzables, y evitando los que puedan producir campos de inducción magnética más intensos que los típicos para
las líneas existentes, tal como se indica en los puntos 4.5.1. y 4.5.2.
El informe de los requerimientos ambientales deberá reflejar los esfuerzos razonablemente aceptables para
disminuir los valores de campo eléctrico y magnético tanto como sea posible.
4.5.1.Campo eléctrico
En base a las documentos elaborados conjuntamente por la ORGANIZACION MUNDIAL DE LA SALUD (OMS), la
ASOCIACION INTERNACIONAL DE PROTECCION CONTRA LA RADIACION NO IONIZANTE (IRPA) y el
PROGRAMA AMBIENTAL DE NACIONES UNIDAS, los cuales recopilan en diferentes países, los valores típicos de
la mayoría de las líneas que se encuentran en operación, se adopta el siguiente valor límite superior de campo
eléctrico no perturbado para las líneas, en condiciones de tensión nominal y conductores a temperatura máxima
anual: TRES KILOVOLTIOS POR METRO (3 kV/m), en el borde de la franja de servidumbre, fuera de ella y en el
borde perimetral de las subestaciones, medido a un metro del nivel del suelo.
Cuando no estuviera definida la franja de servidumbre, el nivel de campo deberá ser igual o inferior a dicho valor en
los puntos resultantes de la aplicación de las distancias mínimas establecidas en la Reglamentación de la
ASOCIACION ELECTROTECNICA ARGENTINA (AEA) sobre Líneas Eléctricas Aéreas Exteriores.
El nivel máximo de campo eléctrico, en cualquier posición, deberá ser tal que las corrientes de contacto para un caso
testigo: niño sobre tierra húmeda y vehículo grande sobre asfalto seco, no deberán superar el límite de seguridad de
CINCO MILI AMPERIOS (5mA).
4.5.2. Campo de inducción magnética
En base a la experiencia de otros países, algunos de los cuales han dictado normas interinas de campos de
inducción magnética y a los valores típicos de las líneas en operación, se adopta el siguiente valor límite de campo
de inducción magnética para líneas, en condiciones de máxima carga definida por el límite térmico de los
conductores:
DOSCIENTOS CINCUENTA MILI GAUSSIOS (250 mG), en el borde de la franja de servidumbre, fuera de ella y en
el borde perimetral de las subestaciones, medido a un metro del nivel del suelo.
Cuando no estuviera definida la franja de servidumbre, el valor de campo deberá ser igual o inferior a dicho valor en
los puntos resultantes de la aplicación de las distancias mínimas establecidas en la Reglamentación de la
ASOCIACION ELECTROTECNICA ARGENTINA (AEA) sobre Líneas Eléctricas Aéreas Exteriores.
El nivel máximo de campo de inducción magnética, en cualquier posición, deberá ser tal que las corrientes de
contacto en régimen permanente, debido al contacto con objetos metálicos largos cercanos a las líneas, no deberán
superar el límite de salvaguarda de CINCO MILI AMPERIOS (5mA).

---

## Tablas Adicionales del Documento

> **Nota:** Las siguientes tablas no tienen referencias explícitas en el texto principal pero contienen información potencialmente relevante.

**Tabla 4-1: Características de las instalaciones de la subestación**

| Instalación | Característica |
| --- | --- |
| Voltaje nominal | 220 KV |
| Voltaje máximo | 245 KV |
| Capacidad máxima | 760 MVA |
| Tipo de Tecnología | equipamiento aislado en gas SF6 (GIS) |
| Topología o configuración | Interruptor y medio |
| Tensión soportada a frecuencia nominal | 460 KV |
| Nivel básico de impulso | 1050 KV |
| Capacidad de transporte Perm. barra colectora | 3150 A |
| Capacidad de transporte Perm. alimentadores | 1250 A |
| Corriente de corta duración (1s) admisible | 50 KA rms |
| Número de paños | 6 |
| Cantidad de Marcos de Línea | cuatro, dos utilizados también como marcos de barras |
| Alturas desde piso punto de anclaje/total de los<br>Marcos de Línea | 16,7 m/27,2 m |
| Cantidad de Marcos de Barras | 1 - Barra 1 y 1 - Barra 2, utilizados también como marcos<br>de barras |
| Alturas desde piso de los Marcos de Barra | 10,27 m |

**Tabla 5-1: Campo eléctrico y campo magnético en borde de subestación**

| Campo eléctrico<br>[V/m] | Inducción magnética<br>[micro Tesla] |
| --- | --- |
| 430 | 3,8 |

**Tabla 5-2: Campo eléctrico y campo magnético en borde de franja de seguridad**

| Campo eléctrico<br>[V/m] | Inducción magnética<br>[micro Tesla] |
| --- | --- |
| 310 | 1,85 |

**Tabla 5-3: Listado de salida del software LINEAS**

| Circuito 1 | Col2 | Col3 | Col4 | Col5 | Col6 | Col7 |
| --- | --- | --- | --- | --- | --- | --- |
| Fase | 1 | 2 | 3 | 4 | 5 | 6 |
| Numero de subconductores | 2 | 2 | 2 | 2 | 2 | 2 |
| Separación entre subconductores (cm) | 40.00 | 40.00 | 40.00 | 40.00 | 40.00 | 40.00 |
| Radio del subconductor (cm) | 0.966 | 0.966 | 0.966 | 0.966 | 0.966 | 0.966 |
| Ubicacion lateral del conductor (m) | -5.000 | -7.000 | -5.000 | 5.000 | 7.000 | 5.000 |
| Altura conductor sobre el suelo (m) | 34.000 | 27.000 | 20.000 | 34.000 | 27.000 | 20.000 |

**Tabla 5-4: Normativa para campo eléctrico y magnético de 50 Hz**

| País | Público general | Col3 | Exposición ocupacional | Col5 |
| --- | --- | --- | --- | --- |
| **País** | **Campo Eléctrico** | **Campo**<br>**magnético** | **Campo**<br>**Eléctrico** | **Campo**<br>**magnético** |
| **País** | **[V/m]** | **[****Tesla]** | **[V/m]** | **[****Tesla]** |
| Alemania | 5.000 | 100 | 5.000 | 100 |
| Argentina | 3.000 | 25 | 3.000 | 25 |
| Australia | 5.000 | 100 | 10.000 | 500 |
| Canadá | No existe | No existe | No existe | No existe |
| España | CEU | CEU | CEU | CEU |
| Italia | 5.000 | 10 | 5.000 | 10 |
| Japón | 3.000 | No existe | ICNIRP | ICNIRP |
| U.S.A. | 2.000 | 15 - 20 | 2.000 | 15 - 20 |
| Reino de los Países Bajos (Gobierno)<br>(Consejo de Salud) | ICNIRP<br>8.000 | ICNIRP<br>120 | ICNIRP<br>40.000 | ICNIRP<br>600 |
| Suiza | 5.000 | 100 | 5.000 | 1 |
| ICNIRP | 5.000 | 100 | 10.000 | 500 |
